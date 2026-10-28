(() => {
  'use strict';
  const config = JSON.parse(document.getElementById('app-config').textContent);
  const form = document.getElementById('enquiry-form');
  const offer = form.elements.offer, count = form.elements.count, date = form.elements.date;
  const status = document.getElementById('form-status');
  const preview = document.getElementById('enquiry-preview'), draft = document.getElementById('draft-text');
  const portraitData = JSON.parse(document.getElementById('design-config').textContent).portraits;
  document.querySelectorAll('[data-portrait-index]').forEach(button => button.addEventListener('click', () => {
    const index = Number(button.dataset.portraitIndex), portrait = portraitData[index];
    if (!portrait) return;
    const image = document.getElementById('portrait-image');
    image.src = portrait.file; image.alt = portrait.alt;
    document.getElementById('portrait-counter').textContent = '0' + (index + 1) + ' / 04';
    document.querySelectorAll('[data-portrait-index]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  }));
  const today = new Date();
  date.min = [today.getFullYear(), String(today.getMonth()+1).padStart(2,'0'), String(today.getDate()).padStart(2,'0')].join('-');
  let activeOffer = offer.value;
  const counts = { live: String(config.min), photo: '1' };
  function setOffer(value) {
    counts[activeOffer] = count.value;
    activeOffer = value;
    offer.value=value; count.value=counts[value]; count.min=value==='live'?String(config.min):'1';
    if(Number(count.value)<Number(count.min)) count.value=count.min;
    count.setCustomValidity(''); status.textContent='';
  }
  offer.addEventListener('change',()=>setOffer(offer.value));
  count.addEventListener('input',()=>count.setCustomValidity(''));
  document.querySelectorAll('[data-offer]').forEach(link=>link.addEventListener('click',()=>setOffer(link.dataset.offer)));
  function prepare() {
    count.setCustomValidity('');
    if(offer.value==='live'&&Number(count.value)<config.min) count.setCustomValidity(config.text.minError);
    if(!form.reportValidity()) return null;
    const d=new FormData(form);
    const kind=offer.value==='photo'?`Portraits from photos — EUR ${config.price} per portrait`:`Live iPad portraits for a tour group (from ${config.min} people)`;
    const body=['Hello Phil,','','I would like to enquire about: '+kind,
      'Preferred correspondence language: '+document.documentElement.lang,
      'Name / tour company: '+String(d.get('name')).trim(),
      'Reply email: '+(String(d.get('email')).trim()||'(use sender address)'),
      'Visit date / desired completion date: '+d.get('date'),
      'Number of people / portraits: '+d.get('count'),
      'Hotel / meeting point / destination: '+(String(d.get('place')).trim()||'To be agreed'),'',
      'Wishes / format / background / schedule:',String(d.get('message')).trim()||'Please advise.','',
      'Please confirm availability, the total price, format, deadline and handover details.',
      'I understand this is a non-binding enquiry and any booking or order requires agreement.','','Thank you!',String(d.get('name')).trim()].join('\n');
    const subject='Würzburg — '+(offer.value==='photo'?'Photo portrait enquiry':'Tour group portrait enquiry')+' — '+d.get('date');
    draft.value=body; preview.hidden=false; return {body,subject};
  }
  form.addEventListener('submit',event=>{
    event.preventDefault();const q=prepare();if(!q)return;
    window.location.href='mailto:'+config.email+'?subject='+encodeURIComponent(q.subject)+'&body='+encodeURIComponent(q.body);
  });
  document.getElementById('copy-enquiry').addEventListener('click',async()=>{
    const q=prepare();if(!q)return;
    try {await navigator.clipboard.writeText('To: '+config.email+'\nSubject: '+q.subject+'\n\n'+q.body);status.textContent=config.text.copied;}
    catch {draft.focus();draft.select();status.textContent=config.text.copyFail;}
  });
  const dialog=document.getElementById('video-dialog'),stage=document.getElementById('video-stage'),consent=stage.firstElementChild;
  let activeVideo='';
  document.querySelectorAll('[data-video]').forEach(trigger=>trigger.addEventListener('click',()=>{
    activeVideo=trigger.dataset.video;
    document.getElementById('video-external').href='https://www.youtube.com/watch?v='+activeVideo;dialog.showModal();
  }));
  document.getElementById('load-video').addEventListener('click',()=>{
    const frame=document.createElement('iframe');frame.className='video-frame';
    frame.src='https://www.youtube-nocookie.com/embed/'+activeVideo+'?autoplay=1&rel=0';frame.title=config.videoTitle;
    frame.allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';frame.allowFullscreen=true;
    frame.referrerPolicy='strict-origin-when-cross-origin';stage.replaceChildren(frame);
  });
  document.getElementById('close-video').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',event=>{
    if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}
  });
  dialog.addEventListener('close',()=>stage.replaceChildren(consent));
  function openLegal(){if(['#legal','#privacy','#image-credits'].includes(location.hash))document.querySelector(location.hash).open=true;}
  window.addEventListener('hashchange',openLegal);openLegal();
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('reveal-visible'); observer.unobserve(entry.target); }
    }), { threshold: 0.1 });
    document.querySelectorAll('[data-reveal]').forEach(element => observer.observe(element));
  }
  const menu=document.querySelector('.languages');
  document.addEventListener('click',e=>{if(!menu.contains(e.target))menu.open=false;});
  document.addEventListener('keydown',e=>{if(e.key==='Escape')menu.open=false;});
})();
