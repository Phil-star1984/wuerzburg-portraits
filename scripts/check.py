#!/usr/bin/env python3
"""Check the built visitor experience: routes, assets, metadata and offer consistency."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'docs'
config=json.loads((ROOT/'site.config.json').read_text())
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0;self.schema=False;self.buf='';self.graphs=[];self.lang=None;self.alternates=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='script' and a.get('type')=='application/ld+json':self.schema=True;self.buf=''
  if tag=='link' and a.get('rel')=='alternate':self.alternates.append(a)
  for attr in ['src','href']:
   if attr in a:self.refs.append((tag,a[attr]))
  if tag=='img':assert 'alt' in a,'Missing image alt'
 def handle_data(self,data):
  if self.schema:self.buf+=data
 def handle_endtag(self,tag):
  if tag=='script' and self.schema:self.graphs.append(json.loads(self.buf));self.schema=False
for locale in ['', 'de','ja','zh-cn','zh-tw']:
 path=DIST/locale/'index.html';source=path.read_text();p=Page();p.feed(source)
 assert p.lang and p.h1==1 and len(p.ids)==len(set(p.ids)),f'Invalid structure: {locale}'
 assert len(p.alternates)==6,f'Missing language links: {locale}'
 assert '{price}' not in source and '{min}' not in source,'Unrendered content'
 assert config['email'] in source and 'mailto:' in source,'Missing contact route'
 assert 'iframe' not in source,'Video must be opt-in, not loaded initially'
 for tag,ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  if not u.path:
   if u.fragment:assert u.fragment in p.ids,f'Broken anchor {ref}'
   continue
  target=(path.parent/unquote(u.path)).resolve()
  assert target.exists(),f'Missing local target {ref} in {path}'
  if target.is_dir():assert (target/'index.html').exists(),f'Missing page {target}'
 service=next(g for g in p.graphs[0]['@graph'] if g.get('@id','').endswith('/#photo'))
 assert service['offers']['price']==config['photoPortraitPriceEUR'] and service['offers']['priceCurrency']=='EUR'
 print(f'PASS {locale or "en"}: complete HTML, language links, local assets, anchors, price and contact')
ET.parse(DIST/'sitemap.xml')
facts=json.loads((DIST/'facts.json').read_text())
assert facts['offers'][0]['minimumGroupSize']==config['minimumLiveGroup']
print('PASS sitemap, structured service facts and minimum group size')
