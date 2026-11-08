// The tool evaluates with top-level await, so the result must be the last expression (done below).
// Paste into javascript_tool (Claude in Chrome) on the open prototype, viewport 1440 wide.
// Scrolls the page once, then returns one JSON string with the measured checks M1 to M10.
// Pass rules: see 00_project/cro-homepage-visual-check.md section 1.
const __cro = await (async () => {
  const H = document.documentElement.scrollHeight;
  for (let y = 0; y <= H; y += 500) { scrollTo({top:y,behavior:'instant'}); await new Promise(r=>setTimeout(r,160)); }
  await new Promise(r=>setTimeout(r,900));
  scrollTo({top:0,behavior:'instant'});
  const out = {M1_innerWidth: innerWidth, M1_innerHeight: innerHeight, pageHeight: H};
  out.M2_noHScroll = document.documentElement.scrollWidth <= innerWidth + 1;
  out.M4_images = [...document.images].map(i => ({src:i.getAttribute('src'), natural:i.naturalWidth+'x'+i.naturalHeight, shown:i.clientWidth+'x'+i.clientHeight, ok:i.complete&&i.naturalWidth>0, upscaled:i.naturalWidth<i.clientWidth, distorted: getComputedStyle(i).objectFit==='fill' && Math.abs(i.clientWidth/i.clientHeight - i.naturalWidth/i.naturalHeight)/(i.naturalWidth/i.naturalHeight) > .02}));
  const fams = new Set(); document.querySelectorAll('h1,h2,h3,p,a,button,li').forEach(e=>fams.add(getComputedStyle(e).fontFamily.split(',')[0].replace(/["']/g,'').trim()));
  out.M5_fonts = [...fams].map(f => f+':'+[...document.fonts].some(ff=>ff.family.replace(/["']/g,'')===f&&ff.status==='loaded'));
  const links = [...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'));
  const ids = new Set([...document.querySelectorAll('[id]')].map(e=>e.id));
  out.M6_anchorsMissing = links.filter(h=>h.startsWith('#')&&h.length>1&&!ids.has(h.slice(1)));
  out.M6_hashPlaceholders = links.filter(h=>h==='#').length;
  out.M6_tel = [...new Set(links.filter(h=>h.startsWith('tel:')))];
  out.M6_externalHosts = [...new Set(links.filter(h=>/^https?:/.test(h)||h==='WA').map(h=>{try{return new URL(h).host}catch(e){return h}}))];
  out.M7_hiddenAfterScroll = [...document.querySelectorAll('.rv,.rv-up,.rv-h,.reveal')].filter(e=>parseFloat(getComputedStyle(e).opacity)<0.99).length;
  const cta = document.querySelector('.hero .btn, .hero a.cta, .hero a[class*=btn]'); out.M8_heroCtaBottom = cta ? Math.round(cta.getBoundingClientRect().bottom) : null;
  const small = []; document.querySelectorAll('body *').forEach(e=>{const t=[...e.childNodes].filter(n=>n.nodeType===3&&n.textContent.trim()).map(n=>n.textContent.trim()).join(' '); if(!t||e.closest('svg,script,style'))return; const fs=parseFloat(getComputedStyle(e).fontSize); if(fs<16) small.push(fs+'px|'+e.tagName+'.'+(e.className||'')+'|'+t.slice(0,30));});
  out.M9_textBelow16_count = small.length; out.M9_textBelow16 = small.slice(0,25);
  out.M10_breathingElements = [...document.querySelectorAll('*')].filter(e=>/breath/i.test(getComputedStyle(e).animationName)).length;
  out.placeholders_FEHLT = [...document.body.innerText.matchAll(/\[FEHLT[^\]]*\]/g)].map(m=>m[0]);
  return JSON.stringify(out);
})();
__cro;
