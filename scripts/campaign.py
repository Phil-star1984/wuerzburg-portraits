"""Würzburg Moments: travel discovery first, local portrait experiences within the city story."""
import html,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def e(value):return html.escape(str(value),quote=True)
def lines(values):return ''.join(f'<span>{e(v)}</span>' for v in values)
def replace_values(v,config):
 if isinstance(v,str):return v.replace('{price}',str(config['photoPortraitPriceEUR'])).replace('{min}',str(config['minimumLiveGroup']))
 if isinstance(v,list):return [replace_values(x,config) for x in v]
 if isinstance(v,dict):return {k:replace_values(x,config) for k,x in v.items()}
 return v

def redesign(doc,c,lang,config,all_content):
 n=replace_values(json.loads((ROOT/'campaign.json').read_text())[lang],config)
 rel='./' if lang=='en' else '../'
 def asset(name):return rel+'assets/'+name
 def ai_badge(extra=''):return f'<a class="ai-badge {extra}" href="#image-credits" aria-label="{e(n["aiLabel"])}" title="{e(n["aiLabel"])}">AI</a>'
 brand=f'<span class="brand-name">WÜRZBURG<span class="brand-line">MOMENTS<span class="brand-star" aria-hidden="true">✳</span></span></span><span class="brand-sub">{e(n["brandSub"])}</span>'
 langs=['en','zh-cn','zh-tw','ja','de']
 language_links=''.join(f'<a href="{rel+(l+"/" if l!="en" else "")}" lang="{all_content[l]["lang"]}" hreflang="{all_content[l]["lang"]}" '+('aria-current="page"' if l==lang else '')+f'>{e(all_content[l]["label"])}</a>' for l in langs)
 nav=''.join(f'<a href="#{id}">{e(t)}</a>' for id,t in zip(['city','photo','artist','films','faq'],n['nav']))
 header=f'''<header class="site-header"><a class="brand" href="#top" aria-label="Würzburg Moments">{brand}</a><nav class="desktop-nav" aria-label="Navigation">{nav}</nav><div class="header-actions"><details class="languages"><summary><span aria-hidden="true">◎</span>{e(c['label'])}<span aria-hidden="true">⌄</span></summary><div>{language_links}</div></details><a class="button button-small" href="#enquire">{e(c['navBook'])} ↗</a></div></header>'''
 hero=f'''<section class="campaign-hero" aria-labelledby="hero-title"><picture class="hero-backdrop"><source media="(max-width:700px)" srcset="{asset('moments-hero-v2-small.webp')}"><img src="{asset('moments-hero-v2.webp')}" width="1536" height="1024" fetchpriority="high" alt="Würzburg · {e(n['aiLabel'])}"></picture><div class="hero-shade" aria-hidden="true"></div><div class="hero-coordinate">49°47′ N &nbsp; 9°56′ E<span>WÜRZBURG MOMENTS / BAVARIA</span></div><div class="hero-copy"><p class="eyebrow">{e(n['heroEyebrow'])}</p><h1 id="hero-title">{lines(n['heroTitle'])}</h1><p class="hero-intro">{e(n['heroLead'])}</p><div class="hero-buttons"><a class="button" href="#live">{e(n['heroLiveCTA'])}<span aria-hidden="true">↗</span></a><a class="button button-outline" href="#photo">{e(n['photoCTA'])}<span aria-hidden="true">↗</span></a></div></div><figure class="hero-encounter"><a href="#live"><img src="{asset('experience-handover-v2-small.webp')}" alt="{e(n['galleryAlts'][1])}" width="768" height="512"></a>{ai_badge()}<figcaption>{e(n['heroScene'])}</figcaption></figure><a class="hero-scroll" href="#city"><span>{e(n['discoverCTA'])}</span><span aria-hidden="true">↓</span></a>{ai_badge('hero-ai')}</section>'''

 intro=f'''<section class="destination-intro section-wrap" aria-labelledby="intro-title"><p class="eyebrow">{e(n['introLabel'])}</p><div class="intro-columns"><h2 id="intro-title">{lines(n['introTitle'])}</h2><p>{e(n['introText'])}</p></div></section>'''
 sources=['https://www.wuerzburg.de/tourismus/wuerzburg-entdecken/sehenswuerdigkeiten/alte-mainbruecke/index.html','https://whc.unesco.org/en/list/169/','https://www.wuerzburg.de/tourismus/wuerzburg-entdecken/sehenswuerdigkeiten/marienkapelle']
 stories=''.join(f'''<article class="sight-story sight-story-{i}"><div class="sight-copy" data-reveal><span class="sight-number">0{i+1}</span><p class="eyebrow">{e(n['placeFacts'][i])}</p><h3>{e(title)}</h3><p>{e(text)}</p><a class="text-link" href="{sources[i]}" target="_blank" rel="noopener">{e(n['sightInfo'])} ↗</a></div></article>''' for i,(title,text) in enumerate(n['places']))
 city=f'''<section class="city-section section-wrap" id="city" aria-labelledby="city-title"><div class="split-heading"><div><p class="eyebrow">{e(n['cityLabel'])}</p><h2 id="city-title">{lines(n['cityTitle'])}</h2></div><p>{e(n['cityIntro'])}</p></div><div class="sight-stories">{stories}</div><div class="city-planning"><p>{e(n['cityNotice'])}</p><p>{e(n['aiNotice'])}</p></div></section>'''
 keys=['color','ink','original']; artwork_files=['portrait-city-color-v2.webp','portrait-city-ink-v2.webp','portrait-1.webp']
 design_payload=[{'key':keys[i],'file':asset(artwork_files[i]),'label':title,'heading':heading,'description':description,'isConcept':i<2} for i,(title,heading,description) in enumerate(n['designs'])]
 tabs=''.join(f'<button type="button" class="design-tab" data-design="{keys[i]}" aria-pressed="{"true" if i==0 else "false"}" aria-controls="portrait-stage">{e(t[0])}</button>' for i,t in enumerate(n['designs']))
 steps=''.join(f'<div><span>{e(i)}</span><p>{e(t)}</p></div>' for i,t in n['steps'])
 collection=f'''<section class="collection-section" id="experiences" aria-labelledby="collection-title"><div class="collection-layout section-wrap" id="photo"><div class="collection-art"><figure id="portrait-stage"><img id="design-image" src="{asset(artwork_files[0])}" alt="{e(n['designs'][0][1]+' — '+n['conceptLabel'])}" width="1024" height="1536" loading="lazy"><span id="design-ai-badge">{ai_badge()}</span></figure><p id="design-credit">{e(n['conceptLabel'])}</p><span id="design-edition">01 / CITY COLOR</span></div><div class="collection-copy"><p class="eyebrow">{e(n['collectionLabel'])}</p><h2 id="collection-title">{lines(n['collectionTitle'])}</h2><p>{e(n['collectionText'])}</p><div class="design-selector" role="group" aria-label="{e(n['selectDesign'])}">{tabs}</div><div class="design-description" aria-live="polite"><h3 id="design-heading">{e(n['designs'][0][1])}</h3><p id="design-description">{e(n['designs'][0][2])}</p></div><div class="collection-price"><span>€{config['photoPortraitPriceEUR']}</span><p>{e(c['perPortrait'])}</p></div><a class="button" href="#enquire" data-offer="photo">{e(n['chooseCTA'])}<span aria-hidden="true">↗</span></a><p class="fine-print">{e(n['collectionFoot'])}</p></div><div class="portrait-steps">{steps}</div></div></section>'''
 gallery_files=['experience-group-v2.webp','experience-handover-v2.webp','experience-garden-v2.webp','experience-market-v2.webp']
 gallery_images=''.join(f'<figure class="experience-scene"><div class="scene-image"><img src="{asset(file)}" width="1536" height="1024" alt="{e(n["galleryAlts"][i])}" loading="lazy">{ai_badge()}</div><figcaption><span>0{i+1}</span>{e(n["galleryCaptions"][i])}</figcaption></figure>' for i,file in enumerate(gallery_files))
 live=f'''<section class="live-encounter" id="live" aria-labelledby="live-title"><div class="section-wrap live-intro" id="artist"><div><p class="eyebrow">{e(n['liveLabel'])}</p><h2 id="live-title">{lines(n['liveTitle'])}</h2></div><div class="live-details"><p>{e(n['liveText'])}</p><p class="live-fact">{e(n['liveFact'])}</p><a class="button button-dark" href="#enquire" data-offer="live">{e(c['liveCTA'])} ↗</a><p class="fine-print">{e(c['liveFoot'])}</p></div></div><div class="experience-section section-wrap" id="gallery"><div class="gallery-heading"><div><p class="eyebrow">{e(n['galleryLabel'])}</p><h3>{e(n['galleryTitle'])}</h3></div><p>{e(n['galleryNote'])}</p></div><div class="experience-gallery">{gallery_images}</div></div><div class="artist-bio section-wrap"><div class="artist-nameplate"><span>PHIL SPLASH</span><strong>THE MILLION<br>PAINTER.</strong><a class="text-link" href="{config['artistWebsite']}" target="_blank" rel="noopener">{e(c['artistLink'])} ↗</a></div><div><p>{e(c['artistText'])}</p><p>{e(c['artistText2'])}</p></div></div></section>'''

 portraits=''.join(f'<figure><img src="{asset("portrait-"+str(i+1)+".webp")}" alt="{e(c["artAlt"][i])}" width="1131" height="1600" loading="lazy"><figcaption>PHIL SPLASH / ORIGINAL 0{i+1}</figcaption></figure>' for i in range(3))
 originals=f'''<section class="originals-section section-wrap" aria-labelledby="originals-title"><div class="split-heading"><div><p class="eyebrow">{e(n['originalLabel'])}</p><h2 id="originals-title">{e(n['originalTitle'])}</h2></div><p>{e(n['originalText'])}</p></div><div class="portrait-gallery">{portraits}</div></section>'''
 films=doc[doc.index('<section class="films-section"'):doc.index('<section class="visit ')]
 films=films.replace(e(c['filmTitle']),e(n['filmTitle']))
 tail=doc[doc.index('<section class="faq '):]
 tail=tail.replace('<h2 id="contact-title">'+e(c['contactTitle']).replace('\n','<br>')+'</h2>','<h2 id="contact-title">'+lines(n['contactTitle'])+'</h2>')
 options=''.join(f'<option value="{keys[i]}">{e(x[0]+" / "+x[1])}</option>' for i,x in enumerate(n['designs']))
 field=f'<div id="design-field" hidden><label for="portrait-design">{e(n["designField"])}</label><select id="portrait-design" name="design">{options}</select></div>'
 tail=tail.replace('<div class="form-grid">',field+'<div class="form-grid">',1)
 reference_credits=''.join(f'<li>{e(item["label"])} · {e(item["author"])} · <a href="{e(item["source"])}" target="_blank" rel="noopener">{e(item["reference"])}</a> · <a href="{e(item["licenseUrl"])}" target="_blank" rel="noopener">{e(item["license"])}</a>. {e(item["changes"])}</li>' for item in json.loads((ROOT/'image-references.json').read_text()))
 credits=f'<details class="legal-details" id="image-credits"><summary>{e(n["photoCredit"])}</summary><p>{e(n["creditIntro"])}</p><ul class="reference-credits">{reference_credits}</ul></details>'
 tail=tail.replace('<p class="credit">'+e(c['credit'])+'</p>',credits)
 oldbrand='<span class="brand-name">phil splash<span class="brand-star">✳</span></span><span class="brand-sub">THE MILLION PAINTER</span>'
 tail=tail.replace(oldbrand,brand)
 tail=tail.replace('</footer>',f'<p class="operator-disclosure">{e(n["siteDisclosure"])}</p></footer>')
 dock=f'<nav class="mobile-booking" aria-label="{e(c["navBook"])}"><a href="#enquire" data-offer="live">{e(n["stickyLive"])} ↗</a><a href="#photo">{e(n["stickyPhoto"])} ↗</a></nav>'
 design_config=json.dumps({'designs':design_payload,'conceptLabel':n['conceptLabel'],'originalLabel':n['originalLabel']},ensure_ascii=False).replace('<','\\u003c')
 head=doc[:doc.index('<body')]
 head=head.replace('wuerzburg-illustration.webp','moments-hero-v2.webp').replace(e(c['caption']),e('Würzburg Moments — '+n['aiLabel'])).replace('content="#f7f4ec"','content="#131614"')
 head=head.replace('as="image" fetchpriority="high">','as="image" media="(min-width:701px)" fetchpriority="high">')
 for filename in ['style.css','app.js','favicon.svg']:
  digest=hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()[:10]
  head=head.replace(rel+filename+'"',rel+filename+'?v='+digest+'"')
 head=head.replace('</head>',f'<meta property="og:site_name" content="Würzburg Moments"><link rel="preload" href="{asset("moments-hero-v2-small.webp")}" as="image" media="(max-width:700px)" fetchpriority="high"><script id="design-config" type="application/json">{design_config}</script></head>')
 tail=tail.replace('</footer>','</footer>'+dock)
 return head+f'<body class="campaign moments" id="top"><a class="skip" href="#main">{e(c["skip"])}</a>'+header+'<main id="main">'+hero+live+collection+intro+city+originals+films+tail
