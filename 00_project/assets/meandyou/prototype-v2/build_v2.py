#!/usr/bin/env python3
"""me&you prototype v2: multi-page site from Copy Deck Round 3.

Writes page.html (home, artifact body), index.html (home, local preview) and the
sub pages. Shared CSS comes from ../prototype/page.html plus the additions below.
Run: python3 build_v2.py
"""
import os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))
V1 = open(os.path.join(HERE, '..', 'prototype', 'page.html'), encoding='utf-8').read()
BASE_CSS = re.search(r'<style>(.*?)</style>', V1, re.S).group(1)
BOOK = 'https://www.meandyou.de/seminare-termin'

CSS_V2 = r"""
/* ---------- v2 additions (Copy Deck Round 3) ---------- */
:root{--dove-soft:#DFE6EE;--sand-soft:#EDE5D6}
.hdr__nav a[aria-current="page"]{opacity:1;box-shadow:0 1px 0 var(--ink)}
.lnk{font:600 14px/1 var(--sans);color:var(--dove-deep);text-decoration:none;border-bottom:1px solid currentColor;padding-bottom:3px;align-self:flex-start}
.lnk:hover{color:var(--navy)}
.btns{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.ph{display:inline-block;border:1px dashed var(--dove);border-radius:10px;padding:8px 12px;color:var(--dove-deep);font:500 var(--small)/1.45 var(--sans);background:rgba(126,153,182,.07)}
h2 .ph,h3 .ph{font:inherit;color:var(--dove-deep)}

/* home hero: headline over the poster frame of the hero video */
.hero2{padding:0;align-items:stretch;overflow:hidden;background:var(--cream)}
.hero2__bg{position:absolute;inset:0 0 0 40%}
.hero2__bg img{width:100%;height:112%;margin-top:-4%;object-fit:cover;object-position:50% 34%;will-change:transform}
.hero2__bg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(242,237,228,1) 0%,rgba(242,237,228,.75) 14%,rgba(242,237,228,0) 42%)}
.hero2__in{position:relative;display:grid;align-items:center;padding-block:calc(var(--hdr) + 24px) clamp(36px,6vh,64px)}
.hero2 .stack{max-width:min(52vw,740px)}
.hero2 h1{font-size:clamp(32px,min(4vw,7.4vh),60px);line-height:1.1}
.split h2{font-size:clamp(24px,min(2.5vw,4.6vh),38px)}
.hero2 h1{text-wrap:wrap}
@media (min-width:981px){.hero2 h1{white-space:nowrap}}
.eyebrow-c{font:600 12px/1 var(--sans);letter-spacing:.34em;text-transform:uppercase;color:var(--navy)}
.hero2__sub{font:italic 400 var(--h3)/1.3 var(--serif);color:var(--dove-deep)}
.hero2[data-campaign="on"] .c-off,.hero2[data-campaign="off"] .c-on{display:none}
.hero2[data-campaign="off"] .eyebrow-c{visibility:hidden}
.cswitch{position:absolute;right:var(--gut);bottom:clamp(18px,4vh,34px);z-index:2;display:flex;align-items:center;gap:10px;background:rgba(250,248,244,.9);border:1px solid var(--line);border-radius:999px;padding:6px 6px 6px 14px;font:500 12px/1 var(--sans);color:var(--char)}
.cswitch button{border:0;border-radius:999px;background:var(--navy);color:var(--paper);font:600 12px/1 var(--sans);padding:9px 14px;cursor:pointer}

/* three situations */
.sits{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,22px);margin-top:clamp(14px,2.6vh,28px)}
.sit{border-radius:var(--r);overflow:hidden;display:grid;grid-template-rows:minmax(0,1fr) auto;height:min(60svh,600px);background:var(--t-bg);color:var(--t-fg);text-decoration:none}
.sit__img{position:relative;overflow:hidden;min-height:0}
.sit__img img{width:100%;height:118%;margin-top:-9%;object-fit:cover;will-change:transform}
.sit__txt{padding:clamp(16px,2.4vh,26px) clamp(18px,1.8vw,28px);display:flex;flex-direction:column;gap:clamp(8px,1.2vh,12px)}
.sit h3{color:var(--t-fg);font-size:clamp(18px,min(1.65vw,3vh),25px)}
.sit p{font-size:var(--small);color:var(--t-fg);opacity:.86}
.sit .lnk{color:var(--t-accent)}
.t-replayers{--t-bg:var(--dove-soft);--t-fg:var(--ink);--t-accent:var(--dove-deep)}
.t-overlooked{--t-bg:var(--navy);--t-fg:var(--on-navy);--t-accent:var(--sand)}
.t-undersold{--t-bg:var(--char);--t-fg:var(--on-navy);--t-accent:var(--sand)}
.t-coaches{--t-bg:var(--sand-soft);--t-fg:var(--ink);--t-accent:var(--dove-deep)}

/* authority */
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(10px,1.6vw,24px);border-block:1px solid var(--line);padding-block:clamp(10px,2vh,20px)}
.stats b{display:block;white-space:nowrap;font:400 clamp(19px,min(1.9vw,3.4vh),30px)/1.15 var(--serif);color:var(--ink)}
.stats span{font-size:var(--small);color:var(--muted)}
.poster{position:relative;height:min(66svh,660px);border-radius:var(--r);overflow:hidden;background:var(--navy)}
.poster img{width:100%;height:118%;margin-top:-9%;object-fit:cover;will-change:transform}
.poster::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(30,38,50,0) 55%,rgba(30,38,50,.7) 100%)}
.poster__play{position:absolute;left:50%;top:50%;translate:-50% -50%;z-index:1;width:84px;height:84px;border-radius:50%;background:rgba(250,248,244,.94);display:grid;place-items:center;box-shadow:0 18px 50px -18px rgba(0,0,0,.6)}
.poster__play::after{content:"";border-left:20px solid var(--navy);border-block:12px solid transparent;margin-left:6px}
.poster__cap{position:absolute;left:20px;right:20px;bottom:18px;z-index:1}
.poster__cap .ph{color:var(--paper);border-color:rgba(250,248,244,.6);background:rgba(250,248,244,.1)}

/* method */
.steps{display:grid;gap:0}
.step{display:grid;grid-template-columns:auto minmax(0,1fr);gap:clamp(16px,2.4vw,40px);align-items:baseline;border-top:1px solid var(--line);padding:clamp(16px,3.2vh,32px) 0}
.step:last-child{border-bottom:1px solid var(--line)}
.step i{font:400 clamp(30px,min(3.4vw,6vh),54px)/1 var(--serif);font-style:normal;color:var(--dove)}
.step h3{font-size:clamp(22px,min(2.2vw,4vh),34px)}
.step p{margin-top:6px}

/* full-bleed teaser */
.bleed{padding:0;align-items:stretch;color:var(--white);overflow:hidden;background:var(--navy)}
.bleed__bg{position:absolute;inset:0}
.bleed__bg img{width:100%;height:116%;margin-top:-8%;object-fit:cover;will-change:transform}
.bleed__bg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(26,34,46,.82) 0%,rgba(26,34,46,.5) 45%,rgba(26,34,46,.1) 100%)}
.bleed__in{position:relative;display:grid;align-items:end;padding-block:calc(var(--hdr) + 24px) clamp(40px,9vh,96px)}
.bleed .ov{color:var(--sand)}
.bleed h1,.bleed h2{color:var(--white)}
.bleed p{max-width:34em;color:rgba(255,255,255,.9)}

/* closing (no form in v2) */
.closing2 .closing__grid{grid-template-columns:minmax(0,1fr)}
.closing2 h2{max-width:18em}
.closing2 p{max-width:34em;color:rgba(255,255,255,.9)}
.foot__in--v2{grid-template-columns:minmax(0,1.3fr) repeat(4,minmax(0,1fr))}

/* seminar formats */
.featured{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);border-radius:var(--r);overflow:hidden;background:var(--cream);min-height:min(58svh,560px)}
.featured__img{position:relative;overflow:hidden;min-height:240px}
.featured__img img{width:100%;height:118%;margin-top:-9%;object-fit:cover;will-change:transform}
.featured__txt{padding:clamp(22px,4vh,48px) clamp(22px,3vw,48px);display:flex;flex-direction:column;justify-content:center;gap:clamp(12px,2vh,20px)}
.formats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,22px);margin-top:clamp(14px,2.6vh,28px)}
.format{background:var(--paper);border-radius:var(--r);padding:clamp(20px,3.4vh,36px) clamp(20px,2vw,32px);display:flex;flex-direction:column;justify-content:space-between;gap:clamp(18px,4vh,44px);min-height:min(40svh,360px)}
.whom3{display:flex;flex-direction:column}
.whom3 li{font:400 clamp(26px,min(3.6vw,6.4vh),58px)/1.2 var(--serif);color:var(--ink);border-top:1px solid var(--line);padding:clamp(12px,2.6vh,26px) 0}
.whom3 li:last-child{border-bottom:1px solid var(--line)}
.locs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,22px);height:min(60svh,620px);margin-top:clamp(14px,2.6vh,28px)}

/* landing pages: one structure, treatments change colour and photo */
.lp-hero{background:var(--t-bg);color:var(--t-fg)}
.lp-hero h1{color:var(--t-fg);font-size:clamp(28px,min(2.9vw,5.4vh),42px);line-height:1.16}
.lp-hero .ov{color:var(--t-accent)}
.lp-hero p{color:var(--t-fg);opacity:.9;max-width:30em}
.lp-hero__media{height:min(72svh,720px)}
.draft{position:fixed;left:50%;translate:-50% 0;bottom:calc(env(safe-area-inset-bottom,0px) + 14px);z-index:60;background:var(--ink);color:var(--paper);font:600 12px/1.3 var(--sans);padding:10px 16px;border-radius:999px;text-align:center;max-width:calc(100% - 32px)}

/* voices: written testimonials as a moving gallery, video interviews below */
.screen > .wrap,.flow > .wrap{min-width:0}
.gal{width:auto;margin-inline:calc(50% - 50vw);overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 7%,#000 93%,transparent 100%);mask-image:linear-gradient(90deg,transparent 0,#000 7%,#000 93%,transparent 100%)}
.gal__track{display:flex;gap:clamp(12px,1.4vw,20px);width:max-content;padding:4px clamp(12px,1.4vw,20px) 4px 0;animation:gal 46s linear infinite}
.gal:hover .gal__track,.gal:focus-within .gal__track{animation-play-state:paused}
@keyframes gal{to{transform:translateX(calc(-100% / 3))}}
.gcard{flex:none;width:clamp(280px,29vw,420px);background:var(--cream);border-radius:var(--r);padding:clamp(14px,2.2vh,22px) clamp(18px,1.7vw,26px);display:flex;flex-direction:column;gap:clamp(8px,1.3vh,14px)}
.gcard__top{height:28px;display:flex;align-items:center}
.gcard__logo{height:28px;width:auto;max-width:110px;object-fit:contain;object-position:left center;filter:grayscale(1) contrast(1.05);opacity:.72;mix-blend-mode:multiply}
.gcard__mark{font:400 50px/1 var(--serif);color:var(--dove);height:28px;overflow:hidden}
.gcard p{font:400 clamp(14px,min(1.12vw,2.05vh),17px)/1.45 var(--serif);color:var(--ink);flex:1}
.gcard footer{font-size:var(--small);color:var(--muted)}
.gcard footer b{display:block;color:var(--ink);font-weight:600}
.vids{display:flex;justify-content:center;gap:clamp(12px,2vw,28px);margin-top:clamp(14px,2.6vh,26px)}
.vid{position:relative;flex:none;height:clamp(250px,calc(100svh - 540px),470px);aspect-ratio:9/16;border-radius:var(--r);overflow:hidden;background:var(--navy)}
.vid video{display:block;width:100%;height:100%;object-fit:cover}
.vid__play{position:absolute;inset:0;display:grid;place-items:center;border:0;padding:0;cursor:pointer;background:linear-gradient(180deg,rgba(30,38,50,0) 55%,rgba(30,38,50,.6) 100%)}
.vid__play::before{content:"";width:56px;height:56px;border-radius:50%;background:rgba(250,248,244,.94);transition:transform .25s}
.vid__play:hover::before{transform:scale(1.06)}
.vid__play::after{content:"";position:absolute;border-left:14px solid var(--navy);border-block:8.5px solid transparent;margin-left:5px}
.vid__play span{position:absolute;left:14px;bottom:12px;color:var(--white);font:500 12px/1 var(--sans);letter-spacing:.06em;font-variant-numeric:tabular-nums}
.vid.is-playing .vid__play{display:none}
@media (prefers-reduced-motion:reduce){.gal{overflow-x:auto}.gal__track{animation:none}}


/* export mode for design tools */
html.is-export .rv{opacity:1!important;transform:none!important;transition:none!important}
html.is-export .hdr{position:absolute}
html.is-export .gal__track{animation:none}
html.is-export .cswitch,html.is-export .draft{display:none}
html.is-export .mcard{position:relative;top:auto}
@media (min-width:981px){html.is-export .screen{min-height:900px}}

/* video modal (training button) */
.vmodal{position:fixed;inset:0;z-index:200;display:grid;place-items:center;padding:24px;background:rgba(43,60,82,.82);opacity:0;pointer-events:none;transition:opacity .3s}
.vmodal.is-open{opacity:1;pointer-events:auto}
.vmodal__box{position:relative;width:min(960px,100%);aspect-ratio:16/9;background:#000;border-radius:var(--r);box-shadow:0 30px 80px rgba(0,0,0,.4);transform:translateY(16px);transition:transform .35s}
.vmodal.is-open .vmodal__box{transform:none}
.vmodal__box iframe{position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:var(--r)}
.vmodal__x{position:absolute;top:-44px;right:0;background:none;border:0;color:#fff;font:500 14px/1 var(--sans);cursor:pointer;padding:8px 0;letter-spacing:.02em}
.vmodal__x::after{content:" ×";font-size:20px;vertical-align:-2px}

/* phone menu */
main{overflow-x:clip}
.hdr__end{display:flex;align-items:center;gap:8px}
.hdr__burger{display:none}
.mnav{position:fixed;inset:0;z-index:49;background:var(--paper);padding:calc(var(--hdr) + 34px) var(--gut) calc(env(safe-area-inset-bottom,0px) + 30px);display:flex;flex-direction:column;justify-content:space-between;gap:24px;overflow-y:auto}
.mnav nav{display:flex;flex-direction:column}
.mnav nav a{font:400 clamp(28px,8.4vw,40px)/1.2 var(--serif);color:var(--ink);text-decoration:none;padding:16px 0;border-bottom:1px solid var(--line)}
.mnav nav a[aria-current="page"]{color:var(--dove-deep)}
.mnav .btn{align-self:flex-start;padding:18px 30px;font-size:16px}

/* header on pages that start with a dark screen */
.hdr--light:not(.is-pill) .hdr__logo img{filter:brightness(0) invert(1)}
.hdr--light:not(.is-pill) .hdr__nav a{color:var(--white);opacity:.94}
.hdr--light:not(.is-pill) .hdr__nav a[aria-current="page"]{box-shadow:0 1px 0 var(--white)}
.hdr--light:not(.is-pill):not(.is-open) .hdr__burger span{background:var(--white)}
.hdr.is-open .hdr__logo img{filter:none}
.bleed__bg::before{content:"";position:absolute;inset:0 0 auto 0;height:180px;z-index:1;background:linear-gradient(180deg,rgba(26,34,46,.62),rgba(26,34,46,0));pointer-events:none}

/* content from the client documents */
.work{font:600 11px/1.2 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.topics{display:flex;flex-direction:column;margin-top:6px}
.topics li{font-size:var(--small);color:var(--ink);padding:clamp(5px,.9vh,8px) 0;border-top:1px solid var(--line)}
.topics li:last-child{border-bottom:1px solid var(--line)}
.topics--2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 18px}
.topics--2 li:last-child{border-bottom:0}
.format__foot{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.format__foot span{font:600 12.5px/1 var(--sans);letter-spacing:.06em;color:var(--dove-deep)}
.format{min-height:0;gap:clamp(14px,2.6vh,26px)}
.facts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 clamp(16px,2vw,30px);max-width:34em}
.facts li{border-top:1px solid var(--line);padding:clamp(8px,1.6vh,14px) 0;font-size:var(--small);color:var(--char)}
.facts b{display:block;font:400 clamp(22px,min(2.2vw,3.9vh),32px)/1.1 var(--serif);color:var(--ink);margin-bottom:2px}
.locs--6{grid-template-rows:repeat(2,minmax(0,1fr));height:min(64svh,640px);gap:clamp(10px,1.2vw,16px)}
.locs--6 .place:nth-child(2){margin:0}
.locs--6 .place__txt{padding:clamp(12px,1.5vw,20px);gap:3px}
.locs--6 .place__txt h3{font-size:clamp(19px,min(1.8vw,3.2vh),27px)}
.locs--6 .place__txt p{font-size:clamp(12px,min(.92vw,1.7vh),14px);opacity:.95}
.locs--6 .place__txt b{font-weight:600;opacity:.75;margin-left:4px}

@media (max-width:980px){
  .hero2 .stack{max-width:none}
  .vid{height:auto;flex:1 1 0;min-width:0}
  .gcard{width:78vw}
  .hero2__bg{inset:0}
  .hero2__bg::after{background:linear-gradient(180deg,rgba(250,248,244,.94) 0%,rgba(250,248,244,.86) 55%,rgba(250,248,244,.5) 100%)}
  .sits,.stats,.formats,.locs,.featured,.foot__in--v2{grid-template-columns:minmax(0,1fr)}
  .stats{grid-template-columns:repeat(2,minmax(0,1fr))}
  .sit,.locs,.locs--6{height:auto}
  .locs--6{grid-template-rows:none}
  .locs--6 .place{aspect-ratio:16/10}
  .facts,.topics--2{grid-template-columns:minmax(0,1fr)}
  .sit__img{aspect-ratio:16/10}
  .poster,.lp-hero__media{height:auto;aspect-ratio:4/3}
  .cswitch{position:static;margin:0 var(--gut) 20px;align-self:end;justify-self:start}
  .bleed__in{padding-top:120px}
}

@media (min-width:981px){.mnav{display:none}}

/* ---------- phone layout ---------- */
@media (max-width:980px){
  .gal{margin-inline:calc(-1 * var(--gut))}
  .hdr{padding-top:calc(env(safe-area-inset-top,0px) + 12px)}
  .hdr__in{gap:10px;padding:8px 8px 8px 14px}
  .hdr__logo img{height:32px}
  .hdr .btn{padding:12px 16px;font-size:13px}
  .hdr__burger{display:grid;place-content:center;gap:6px;width:44px;height:44px;border:0;border-radius:50%;background:transparent;cursor:pointer;padding:0}
  .hdr__burger span{display:block;width:22px;height:2px;border-radius:2px;background:var(--ink);transition:transform .3s,background .3s}
  .hdr.is-open .hdr__burger span:first-child{transform:translateY(4px) rotate(45deg)}
  .hdr.is-open .hdr__burger span:last-child{transform:translateY(-4px) rotate(-45deg)}
  .hdr.is-open .hdr__in{background:transparent;border-color:transparent;box-shadow:none}
  .hero2{display:flex;flex-direction:column;align-items:stretch}
  .hero2__in{order:1;padding-block:calc(var(--hdr) + 26px) 26px}
  .hero2__bg{position:relative;inset:auto;order:2;align-self:stretch;width:auto;min-width:0;margin-inline:var(--gut);aspect-ratio:4/5;border-radius:var(--r);overflow:hidden}
  .hero2__bg img{height:100%;margin:0;object-position:58% 22%}
  .hero2__bg::after{display:none}
  .cswitch{order:3;align-self:flex-start;max-width:calc(100% - 2 * var(--gut));margin:16px var(--gut) 30px}
  .michael__media{aspect-ratio:4/5}
  .michael__media img{object-position:50% 14%}
  .bleed__bg::after{background:linear-gradient(180deg,rgba(26,34,46,.5) 0%,rgba(26,34,46,.62) 45%,rgba(26,34,46,.84) 100%)}
  .locs--6{grid-template-columns:repeat(2,minmax(0,1fr))}
  .locs--6 .place{aspect-ratio:4/5}
  .locs--6 .place__txt h3{font-size:19px}
  .locs--6 .place__txt p{font-size:11.5px}
}
"""

JS = r"""
(function(){
  document.documentElement.classList.add('js');
  /* export mode (?export=1): a still page for design tools. No scroll effects, everything visible. */
  var exp = /[?&]export/.test(location.search); window.__export = exp;
  if(exp) document.documentElement.classList.add('is-export');
  var reduce = exp || window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var desktop = function(){ return window.innerWidth >= 1024; };

  /* campaign layer switch (home hero) */
  var hero = document.getElementById('hero'), sw = document.getElementById('cswitch-btn');
  if(hero && sw){
    sw.addEventListener('click', function(){
      var on = hero.getAttribute('data-campaign') === 'on';
      hero.setAttribute('data-campaign', on ? 'off' : 'on');
      sw.textContent = on ? 'einschalten' : 'ausschalten';
      sw.setAttribute('aria-pressed', on ? 'false' : 'true');
    });
  }

  /* FAQ */
  var list = document.getElementById('faq-list');
  if(list && window.FAQ){
    var cols = [document.createElement('div'), document.createElement('div')];
    cols.forEach(function(c){ c.className = 'faq__col'; list.appendChild(c); });
    var items = [];
    window.FAQ.forEach(function(qa, i){
      var el = document.createElement('div'); el.className = 'qa'; el.setAttribute('open-state', i === 0 ? '1' : '0');
      var b = document.createElement('button'); b.type = 'button'; b.id = 'faq-q-' + i;
      b.setAttribute('aria-expanded', i === 0 ? 'true' : 'false'); b.setAttribute('aria-controls', 'faq-a-' + i);
      var s = document.createElement('span'); s.textContent = (i + 1) + '.  ' + qa[0]; b.appendChild(s);
      var a = document.createElement('div'); a.className = 'qa__a'; a.id = 'faq-a-' + i; a.setAttribute('role', 'region'); a.setAttribute('aria-labelledby', b.id);
      var inner = document.createElement('div'); var p = document.createElement('p'); p.textContent = qa[1]; inner.appendChild(p); a.appendChild(inner);
      el.appendChild(b); el.appendChild(a); cols[i < Math.ceil(window.FAQ.length / 2) ? 0 : 1].appendChild(el); items.push(el);
      b.addEventListener('click', function(){
        var open = el.getAttribute('open-state') === '1';
        items.forEach(function(o){ o.setAttribute('open-state', '0'); o.querySelector('button').setAttribute('aria-expanded', 'false'); });
        if(!open){ el.setAttribute('open-state', '1'); b.setAttribute('aria-expanded', 'true'); }
      });
    });
  }

  /* participant videos: play on click, one at a time */
  [].slice.call(document.querySelectorAll('.vid')).forEach(function(v){
    var video = v.querySelector('video'), b = v.querySelector('.vid__play');
    b.addEventListener('click', function(){
      [].slice.call(document.querySelectorAll('.vid video')).forEach(function(o){ if(o !== video){ o.pause(); } });
      video.controls = true; v.classList.add('is-playing');
      var p = video.play(); if(p && p.catch){ p.catch(function(){}); }
    });
    video.addEventListener('ended', function(){ v.classList.remove('is-playing'); video.controls = false; video.load(); });
  });

  /* phone menu */
  var burger = document.getElementById('burger'), mnav = document.getElementById('mnav'), hdrEl = document.getElementById('hdr');
  function menu(open){
    if(!burger || !mnav) return;
    mnav.hidden = !open; hdrEl.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false'); burger.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
    document.documentElement.style.overflow = open ? 'hidden' : '';
  }
  if(burger && mnav){
    burger.addEventListener('click', function(){ menu(mnav.hidden); });
    mnav.addEventListener('click', function(e){ if(e.target.closest('a')) menu(false); });
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') menu(false); });
    window.addEventListener('resize', function(){ if(window.innerWidth > 980) menu(false); });
  }

  /* header capsule */
  var hdr = document.getElementById('hdr');
  function onScrollY(y){ if(hdr) hdr.classList.toggle('is-pill', y > 60); }

  /* reveal */
  var rvs = [].slice.call(document.querySelectorAll('.rv'));
  if(reduce || !('IntersectionObserver' in window)){ rvs.forEach(function(el){ el.classList.add('in'); }); }
  else {
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); }, {rootMargin:'0px 0px -8% 0px', threshold:0.05});
    rvs.forEach(function(el){ io.observe(el); });
  }

  /* parallax */
  var plx = [].slice.call(document.querySelectorAll('[data-plx]')).map(function(el){
    return {box: el, img: el.tagName === 'IMG' ? el : el.querySelector('img'), f: parseFloat(el.getAttribute('data-plx')), on: false};
  });
  function plxUpdate(){
    if(reduce || !desktop()){ plx.forEach(function(p){ p.img.style.transform = ''; }); return; }
    var vh = window.innerHeight;
    plx.forEach(function(p){
      if(!p.on) return;
      var r = (p.box === p.img ? p.img.parentElement : p.box).getBoundingClientRect();
      p.img.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - vh / 2) * p.f).toFixed(1) + 'px,0)';
    });
  }
  if('IntersectionObserver' in window){
    var pio = new IntersectionObserver(function(es){ es.forEach(function(e){ var p = plx.filter(function(x){ return x.box === e.target; })[0]; if(p){ p.on = e.isIntersecting; } }); plxUpdate(); }, {rootMargin:'20% 0px'});
    plx.forEach(function(p){ pio.observe(p.box); });
  }

  /* smooth scroll (Remedy values) */
  var lenis = null;
  if(!reduce && window.Lenis && location.search.indexOf('still') < 0){
    try{
      lenis = new window.Lenis({duration:1.1, easing:function(t){ return Math.min(1, 1.001 - Math.pow(2, -10 * t)); }, smoothWheel:true});
      lenis.on('scroll', function(e){ onScrollY(e.scroll); plxUpdate(); });
      var raf = function(t){ lenis.raf(t); requestAnimationFrame(raf); }; requestAnimationFrame(raf);
    }catch(err){ lenis = null; }
  }
  if(!lenis){ window.addEventListener('scroll', function(){ onScrollY(window.scrollY); plxUpdate(); }, {passive:true}); }
  window.addEventListener('resize', plxUpdate);
  onScrollY(window.scrollY);

  /* video modal: <a data-video="wistia:ID"> opens the video in place of following the link */
  var vb = document.querySelector('[data-video]');
  if(vb){
    var vm = document.createElement('div'); vm.className = 'vmodal'; vm.setAttribute('aria-hidden', 'true');
    vm.innerHTML = '<div class="vmodal__box"><button type="button" class="vmodal__x">Schließen</button></div>';
    document.body.appendChild(vm);
    var box = vm.firstChild, closeBtn = box.firstChild;
    var openV = function(e){
      e.preventDefault();
      var id = vb.getAttribute('data-video').split(':')[1];
      var f = document.createElement('iframe'); f.allow = 'autoplay; fullscreen'; f.title = 'Kostenloses Training';
      f.src = 'https://fast.wistia.net/embed/iframe/' + id + '?autoPlay=true&videoFoam=true';
      box.appendChild(f); vm.classList.add('is-open'); vm.setAttribute('aria-hidden', 'false');
      if(lenis) lenis.stop();
    };
    var closeV = function(){
      vm.classList.remove('is-open'); vm.setAttribute('aria-hidden', 'true');
      var f = box.querySelector('iframe'); if(f) f.remove();
      if(lenis) lenis.start();
    };
    vb.addEventListener('click', openV);
    closeBtn.addEventListener('click', closeV);
    vm.addEventListener('click', function(e){ if(e.target === vm) closeV(); });
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && vm.classList.contains('is-open')) closeV(); });
  }

  /* presenter keys: arrow right = next section, arrow left = previous section */
  document.addEventListener('keydown', function(e){
    if(e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
    if(e.metaKey || e.ctrlKey || e.altKey) return;
    var tag = (e.target && e.target.tagName) || '';
    if(tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'VIDEO') return;
    var now = Date.now(), secs = [].slice.call(document.querySelectorAll('main > section')), y = (window.__navY != null && now - window.__navT < 1500) ? window.__navY : window.scrollY, goal = null;
    if(e.key === 'ArrowRight'){ for(var i = 0; i < secs.length; i++){ if(secs[i].offsetTop > y + 8){ goal = secs[i].offsetTop; break; } } }
    else { for(var j = secs.length - 1; j >= 0; j--){ if(secs[j].offsetTop < y - 8){ goal = secs[j].offsetTop; break; } } }
    if(goal === null) return;
    e.preventDefault(); window.__navY = goal; window.__navT = now;
    if(lenis){ lenis.scrollTo(goal, {duration:1.1}); } else { window.scrollTo({top:goal, behavior: reduce ? 'auto' : 'smooth'}); }
  });

  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href^="#"]'); if(!a) return;
    var id = a.getAttribute('href'); if(id.length < 2) return;
    var t = document.querySelector(id); if(!t) return;
    e.preventDefault();
    if(lenis){ lenis.scrollTo(t, {offset:0}); } else { t.scrollIntoView({behavior: reduce ? 'auto' : 'smooth'}); }
  });
})();
"""

FAQ = [
 # from "Kursinhalte R1-R3"
 ["Wie läuft ein Seminar ab?","Drei Tage Intensivtraining und ein Tag Get Together. Dazu gehören drei Videoanalysen mit Sofort-Feedback, VR-Training und Arbeitsmaterial. Die Gruppen haben 10 bis 14 Plätze."],
 # from "Checkliste Sales" (wording is a draft, the client must approve it)
 ["Ist die Übernachtung enthalten?","Ja. Enthalten sind die Übernachtungen im offiziellen Seminarzeitraum. Bei einem Seminar vom 05. bis 08. sind das drei Nächte und vier Seminartage. Zusätzliche Nächte davor oder danach buchst du selbst."],
 ["Sind An- und Abreise enthalten?","Nein. Flug, Bahn oder Auto organisierst und zahlst du selbst. Auch der Transfer zwischen Flughafen und Hotel ist nicht enthalten."],
 ["Welche Verpflegung ist enthalten?","Enthalten sind Snacks und Getränke während des Programms und ein leichtes Frühstück im Rahmen des Seminars. Das Hotelfrühstück, das Abendessen und eigene Verpflegung außerhalb des Seminars sind nicht enthalten."],
 ["Kann ich eine Begleitperson mitbringen?","Ja. Die Kosten dafür trägst du selbst. Ein Upgrade, zum Beispiel auf ein Doppelzimmer, buchst und bezahlst du direkt beim Hotel."],
 ["Was passiert, wenn ich absagen muss?","Die Seminarkosten werden laut AGB nicht erstattet. Du erhältst stattdessen einen Gutschein für ein späteres Seminar."],
 # from the current site
 ["Muss ich mich verstellen oder schauspielern?","Nein. Rhetorik heißt, authentisch Wirkung zu erzielen. Nicht anders werden – klarer werden. Die Technik unterstützt deine Persönlichkeit."],
 ["Ich habe bereits Kommunikations-Trainings gemacht. Lerne ich hier noch was Neues?","Ja. Aktuelle Erkenntnisse treffen auf über 25 Jahre Praxis aus Politik, Medien und Wirtschaft. Viele erfahrene Teilnehmer berichten: „Ich habe noch einmal ein neues Niveau erreicht.“"],
 # from the Skool briefing "Talk to Me"
 ["Ich stehe nie auf großen Bühnen. Bringt mir das im Alltag etwas?","Ja, absolut. Die Gesetze der Rhetorik sind im Gehaltsgespräch oder Meeting exakt dieselben wie in einer politischen Debatte."],
 ["Ist die Community Talk to Me wieder nur ein starrer Videokurs?","Nein. Sie ist ein lebendiger Trainingsraum mit täglichen Impulsen, wöchentlichen Live-Calls, Live-Feedback und starker Community."],
]

def br(s):
    return html.escape(s, quote=False).replace(' | ', '<br>')

def btn(label='Gespräch buchen', cls='btn', href=BOOK):
    return '<a class="%s" href="%s">%s</a>' % (cls, href, label)

def header(active='', lp=False, light=False):
    items = [('seminare.html', 'Seminare', 'seminare'), ('michael.html', 'Michael', 'michael'),
             ('rhetorik.html', 'Was ist Rhetorik', 'rhetorik'), ('index.html#stimmen', 'Stimmen', 'stimmen'),
             ('faq.html', 'FAQ', 'faq')]
    nav = burger = panel = ''
    if not lp:
        links = ''
        for href, label, key in items:
            if active == 'home' and key == 'stimmen':
                href = '#stimmen'
            cur = ' aria-current="page"' if key == active else ''
            links += '<a href="%s"%s>%s</a>' % (href, cur, label)
        nav = '<nav class="hdr__nav" aria-label="Hauptnavigation">%s</nav>' % links
        burger = ('<button class="hdr__burger" id="burger" type="button" aria-label="Menü öffnen" aria-expanded="false" aria-controls="mnav">'
                  '<span></span><span></span></button>')
        panel = ('<div class="mnav" id="mnav" hidden><nav aria-label="Menü">%s</nav>%s</div>'
                 ) % (links, btn())
    return ('<header class="hdr' + (' hdr--light' if light else '') + '" id="hdr"><div class="hdr__in">'
            '<a class="hdr__logo" href="index.html" aria-label="Michael Ehlers &amp; You Communication, Startseite">'
            '<img src="assets/logo-dark.webp" alt="Michael Ehlers &amp; You Communication" width="600" height="216"></a>'
            + nav + '<div class="hdr__end">' + btn() + burger + '</div></div></header>' + panel)

def footer():
    return ('<footer class="foot"><div class="wrap foot__in foot__in--v2">'
            '<img src="assets/logo-light.webp" alt="Michael Ehlers &amp; You Communication" width="600" height="187">'
            '<div><h4>Seminare</h4><a href="seminare.html">Seminare</a><a href="' + BOOK + '">Gespräch buchen</a></div>'
            '<div><h4>Michael</h4><a href="michael.html">Über Michael</a><a href="rhetorik.html">Was ist Rhetorik</a><a href="faq.html">FAQ</a></div>'
            '<div><h4>Rechtliches</h4><a href="https://www.meandyou.de/impressum">Impressum</a><a href="https://www.meandyou.de/datenschutz">Datenschutz</a><a href="https://www.meandyou.de/agb">AGB</a></div>'
            '<div><h4>Kontakt</h4><span class="sel">+49 15888367664</span><br><span class="sel">management@meandyou.de</span><br>'
            '<a href="https://www.instagram.com/michael_ehlers_rhetorik/">Instagram</a><a href="https://de.linkedin.com/in/rhetoriktrainer">LinkedIn</a></div>'
            '</div></footer>')

def closing(h2, body='', img='gen-closing.webp', pos='50% 72%', sid='gespraech'):
    b = '<p class="rv" data-d="1">%s</p>' % body if body else ''
    return ('<section class="screen closing closing2" id="%s"><div class="closing__stage">'
            '<div class="closing__bg"><img data-plx="0.08" style="object-position:%s" src="assets/%s" alt="" width="1536" height="1024"></div>'
            '<div class="wrap closing__grid"><div class="stack">'
            '<h2 class="rv">%s</h2>%s<div class="rv" data-d="2">%s</div>'
            '</div></div></div>%s</section>') % (sid, pos, img, br(h2), b, btn(cls='btn btn--light'), footer())

QUOTES = [
 ('"Ein begeisterndes Training mit einer anregenden und humorvollen Atmosphäre. Rundum gelungen."', 'Sarna Röser', 'Bundesvorsitzende „Die Jungen Unternehmer“ Berlin', 'logo-bju.webp', 'Die Jungen Unternehmer'),
 ('„Trotz 40 Jahren Medienerfahrung konnte ich erstaunlich viel vom Rhetoriktraining profitieren.“', 'Peter Escher', 'Moderator MDR', 'logo-mdr.webp', 'MDR'),
 ('„Das Seminar – oder egal, wie man es nennen mag – war einfach genial. Ich habe in diesem Kurs mehr gelernt als in all meinen bisherigen Schulungen zusammen.“', 'Emrullah Ates', 'Teilnehmer', '', ''),
 ('"Ersteres ist manchmal genau so schwer wie Letzteres, deshalb ist das Training mit Michael unerlässlich, um eine bessere globale Zukunft aktiv mitzugestalten.“', 'Neven Subotic', 'Fußball-Bundesliga-Profi', 'logo-bundesliga.webp', 'Bundesliga'),
]

def quote_cards(hidden=False):
    out = ''
    for q, name, role, logo, logo_alt in QUOTES:
        mark = ('<img class="gcard__logo" src="assets/%s" alt="%s">' % (logo, '' if hidden else logo_alt)) if logo else '<span class="gcard__mark" aria-hidden="true">“</span>'
        out += ('<figure class="gcard"%s><div class="gcard__top">%s</div><p>%s</p><footer><b>%s</b>%s</footer></figure>'
                ) % (' aria-hidden="true"' if hidden else '', mark, q, name, role)
    return out

VIDEOS = [('1', '1:00'), ('2', '1:12'), ('3', '1:23')]

def voices():
    """Written testimonials as a moving gallery, the three video interviews below."""
    vids = ''
    for i, (n, dur) in enumerate(VIDEOS):
        vids += ('<div class="vid rv" data-d="%d"><video preload="none" playsinline poster="assets/v-stimme-%s.webp" src="assets/v-stimme-%s.mp4"></video>'
                 '<button class="vid__play" type="button" aria-label="Teilnehmerstimme %s abspielen"><span>%s</span></button></div>') % (i, n, n, n, dur)
    return ('<div class="gal" aria-label="Kundenstimmen"><div class="gal__track">%s%s%s</div></div>'
            '<div class="vids">%s</div>') % (quote_cards(), quote_cards(True), quote_cards(True), vids)

STATS = ('<div class="stats rv" data-d="2"><div><b>30+</b><span>Jahre Erfahrung</span></div><div><b>8.000+</b><span>Teilnehmer</span></div>'
         '<div><b>Top 100</b><span>Trainer</span></div><div><b>9</b><span>Bücher</span></div></div>')
LOGOS = ('<div class="logos rv" data-d="3" aria-label="Medien"><img src="assets/logo-zdf.webp" alt="ZDF"><img src="assets/logo-ard.webp" alt="ARD">'
         '<img src="assets/logo-rtl.webp" alt="RTL"><img src="assets/logo-stern.webp" alt="stern"><img src="assets/logo-mdr.webp" alt="mdr"><img src="assets/logo-hr2.webp" alt="hr2"></div>')

STEPS = ('<div class="steps">'
         '<div class="step rv"><i>01</i><div><h3>Persönlichkeit</h3><p>Wer du bist, bevor du sprichst.</p></div></div>'
         '<div class="step rv" data-d="1"><i>02</i><div><h3>Kongruenz</h3><p>Wenn Haltung und Worte dasselbe sagen.</p></div></div>'
         '<div class="step rv" data-d="2"><i>03</i><div><h3>Wirkung</h3><p>Was davon im Raum ankommt.</p></div></div></div>')

SITS = [
 ('replayers', 'lp-replayers.html', 'ai-replayers-desk.webp', '52% 45%', 'Eine Frau sitzt in warmem Licht an einem Schreibtisch und schreibt',
  'Dir fehlen nicht die Worte. | Sie kommen nur zu spät.',
  'Im Meeting bleibst du still. Auf dem Heimweg hast du den perfekten Satz. Das Problem ist nicht dein Wissen, sondern der Moment.'),
 ('overlooked', 'lp-overlooked.html', 'pdf-overlooked-main.webp', '45% 35%', 'Gespräch an einem Glastisch in einem Büro mit kühlem Licht',
  'Recht zu haben | war nie das Problem.',
  'Du bist bestinformiert im Raum. Gefolgt wird trotzdem jemand anderem. Zwischen Kompetenz und Wirkung liegt eine Lücke.'),
 ('undersold', 'lp-undersold.html', 'pdf-undersold-main.webp', '45% 30%', 'Handschlag über einen Tisch, die Gruppe applaudiert, warmes Licht',
  'Ihr Unternehmen ist größer, | als es nach außen wirkt.',
  'Die Substanz stimmt. Der Auftritt bleibt darunter. Nach außen wirkt das Unternehmen kleiner, als es ist.'),
]

def page_home():
    sits = ''
    for i, (key, href, img, pos, alt, h, body) in enumerate(SITS):
        sits += ('<a class="sit t-%s rv" data-d="%d" href="%s"><div class="sit__img"><img data-plx="%s" style="object-position:%s" src="assets/%s" alt="%s" width="1536" height="1024"></div>'
                 '<div class="sit__txt"><h3>%s</h3><p>%s</p><span class="lnk">Mehr dazu →</span></div></a>') % (key, i, href, '0.05', pos, img, alt, br(h), body)
    return ('<main id="top">'
     # 1 hero
     '<section class="screen hero2" id="hero" data-campaign="on">'
     '<div class="hero2__bg"><img data-plx="0.05" src="assets/michael-cafe.webp" alt="Michael Ehlers an einem Tisch im Freien" width="1400" height="2100"></div>'
     '<div class="wrap hero2__in"><div class="stack">'
     '<p class="eyebrow-c rv">UNÜBERSEHBAR</p>'
     '<h1 class="rv" data-d="1"><span class="c-on">Werde unübersehbar,<br>wenn es darauf ankommt.</span><span class="c-off">Rhetorik beginnt nicht<br>bei den Worten.</span></h1>'
     '<p class="hero2__sub rv" data-d="2">Persönlichkeit. Kongruenz. Wirkung.</p>'
     '<p class="rv" data-d="2">Michael Ehlers trainiert seit über 30 Jahren Menschen, die fachlich längst überzeugen und trotzdem nicht gehört werden.</p>'
     '<div class="btns rv" data-d="3">' + btn() + btn('Seminare ansehen', 'btn btn--ghost', 'seminare.html') + '</div>'
     '</div></div>'
     '<div class="cswitch"><span>Prototyp: Kampagnen-Layer</span><button type="button" id="cswitch-btn" aria-pressed="true">ausschalten</button></div>'
     '</section>'
     # 2 problem
     '<section class="screen" id="situationen"><div class="wrap">'
     '<div class="stack stack--tight"><p class="ov rv">Kommt dir das bekannt vor?</p><h2 class="rv" data-d="1">Drei Situationen.<br>Ein gemeinsamer Punkt.</h2></div>'
     '<div class="sits">' + sits + '</div></div></section>'
     # 3 authority
     '<section class="screen screen--cream" id="michael"><div class="wrap split">'
     '<div class="stack"><p class="ov rv">Warum Michael</p><h2 class="rv" data-d="1">30 Jahre. Über 8.000 Menschen.<br>Eine Methode.</h2>'
     + STATS +
     '<p class="rv" data-d="2">Michael Ehlers gehört laut ERFOLG Magazin zu den Top 100 Trainern im deutschsprachigen Raum. Seine Arbeit steht in Büchern, auf Bühnen und in den Unternehmen, die ihn seit Jahren buchen.</p>'
     '<a class="lnk rv" data-d="3" href="michael.html">Mehr über Michael →</a>' + LOGOS + '</div>'
     '<div class="poster rv" data-d="1" data-plx="0.08"><img style="object-position:50% 30%" src="assets/michael-table.webp" alt="Michael Ehlers sitzt an einem Tisch, Standbild für das Video" width="1300" height="1840">'
     '<span class="poster__play" aria-hidden="true"></span><p class="poster__cap"><span class="ph">[Platzhalter: Videountertitel, eine Zeile]</span></p></div>'
     '</div></section>'
     # 4 method
     '<section class="screen" id="methode"><div class="wrap split">'
     '<div class="stack"><p class="ov rv">Die Methode</p><h2 class="rv" data-d="1">Wirkung beginnt nicht<br>bei der Technik.</h2>'
     '<p class="rv" data-d="2" style="max-width:32em">Die meisten Rhetoriktrainings starten bei Werkzeugen. Wir starten davor: bei Persönlichkeit, Selbstbild, Mustern und innerer Stabilität. Erst wenn das steht, tragen die Werkzeuge.</p></div>'
     + STEPS + '</div></section>'
     # 5 seminar teaser
     '<section class="screen bleed" id="seminare"><div class="bleed__bg"><img data-plx="0.07" style="object-position:50% 45%" src="assets/gen-mallorca.webp" alt="Finca-Terrasse über einer ruhigen Bucht im Abendlicht" width="1536" height="1024"></div>'
     '<div class="wrap bleed__in"><div class="stack"><p class="ov rv">Seminare</p><h2 class="rv" data-d="1">Drei Tage. Kleine Gruppe.<br>Ein Ort, der dazu passt.</h2>'
     '<p class="rv" data-d="2">Kein Konferenzraum, kein Hotelsaal. Die Orte sind Teil der Arbeit, nicht die Kulisse dahinter.</p>'
     '<div class="rv" data-d="3">' + btn('Seminare ansehen', 'btn btn--light', 'seminare.html') + '</div></div></div></section>'
     # 6 proof
     '<section class="screen" id="stimmen"><div class="wrap">'
     '<div class="stack stack--tight" style="margin-bottom:clamp(16px,3vh,30px)"><p class="ov rv">Stimmen</p><h2 class="rv" data-d="1">Was Teilnehmer sagen.</h2></div>'
     + voices() + '</div></section>'
     # 7 booking
     + closing('Unübersehbar wird man nicht, | indem man lauter wird.', 'Ein Gespräch, 30 Minuten, kostenlos. Wir klären, wo du stehst und welches Format passt.')
     + '</main>')

PLACES = [
 # (name, months, year, image, object-position, alt)  dates: "Rhetorik-Seminar Termine 2027" (PDF); Dubai: current site, December 2026
 # Phil (06.10.): licence-free city photos (Pexels) instead of generated scenes. IDs in assets/city-credits.txt; gen-*.webp kept as fallback.
 ('Mallorca', 'März · April · September · Oktober', '2027', 'city-mallorca.webp', '50% 45%', 'Cap de Formentor auf Mallorca im Abendlicht'),
 ('Barcelona', 'April · Oktober', '2027', 'city-barcelona.webp', '50% 55%', 'Blick über Barcelona bei Sonnenuntergang'),
 ('Zypern', 'Oktober', '2027', 'city-zypern.webp', '50% 50%', 'Der alte Hafen von Kyrenia in der Abenddämmerung'),
 ('Frankfurt', 'Juni', '2027', 'city-frankfurt.webp', '50% 50%', 'Skyline von Frankfurt am Main im Abendlicht'),
 ('Berlin', 'August', '2027', 'city-berlin.webp', '50% 50%', 'Oberbaumbrücke und Fernsehturm in Berlin bei Sonnenuntergang'),
 ('Dubai', 'Dezember', '2026', 'city-dubai.webp', '50% 45%', 'Wüste vor Dubai bei Sonnenuntergang, die Skyline am Horizont'),
]

# topics: "2026 Michael Ehlers Kursinhalte R1-R3" and "Rhetorik Bundle" (PDF). Names stay placeholders.
FORMATS = [
 ('[Seminar B]', 'Arbeitstitel: Rhetorik II', ['Schlagfertigkeit zeigen', 'Überzeugungspsychologie nutzen', 'Angriffe abwehren', 'Körpersprache lesen', 'Meetings führen'], '10 Plätze'),
 ('[Seminar C]', 'Arbeitstitel: Rhetorik III', ['Persönlichkeit prägt deine Rhetorik', 'Führen lernen', 'Zuhören meistern', 'Stegreifrede halten', 'Gruppen überzeugen'], '12 Plätze'),
 ('[Seminar D]', 'Arbeitstitel: Rhetorik Bundle', ['Analyse deiner Körpersprache & Wirkung', 'Sprache als Führungsinstrument', 'Storytelling, Elevator Pitches, Schlagfertigkeit', 'Auftrittscoaching mit Videoanalyse'], 'Rhetorik I und II'),
]

def page_seminare():
    fmt = ''
    for i, (name, work, topics, meta) in enumerate(FORMATS):
        fmt += ('<article class="format rv" data-d="%d"><div class="stack stack--tight"><p class="work">%s</p><h3><span class="ph">%s</span></h3>'
                '<ul class="topics">%s</ul></div><div class="format__foot"><span>%s</span>%s</div></article>'
                ) % (i, work, name, ''.join('<li>%s</li>' % t for t in topics), meta, btn())
    locs = ''
    for i, (name, months, year, img, pos, alt) in enumerate(PLACES):
        locs += ('<article class="place rv" data-d="%d"><img data-plx="%s" style="object-position:%s" src="assets/%s" alt="%s" width="1536" height="1024">'
                 '<div class="place__txt"><h3>%s</h3><p>%s <b>%s</b></p></div></article>') % (i % 3, '0.05' if i % 2 == 0 else '0.09', pos, img, alt, name, months, year)
    return ('<main id="top">'
     '<section class="screen bleed" id="hero"><div class="bleed__bg"><img data-plx="0.06" style="object-position:50% 35%" src="assets/ai-seminar-room.webp" alt="Michael Ehlers leitet ein Seminar mit einer kleinen Gruppe im Halbkreis" width="1536" height="1024"></div>'
     '<div class="wrap bleed__in"><div class="stack"><p class="ov rv">Seminare</p><h1 class="rv" data-d="1" style="font-size:clamp(38px,min(5vw,8.6vh),80px)">Ein Einstieg.<br>Dann dein eigener Weg.</h1>'
     '<p class="rv" data-d="2">Kein Stufenmodell mehr. Ein klarer Einstieg, danach eigenständige Formate, die du frei wählst.</p></div></div></section>'
     '<section class="screen" id="einstieg"><div class="wrap"><div class="featured rv">'
     '<div class="featured__img"><img data-plx="0.07" style="object-position:45% 35%" src="assets/pdf-undersold-main.webp" alt="Handschlag über einen Tisch, die Gruppe applaudiert, warmes Licht" width="1082" height="1024"></div>'
     '<div class="featured__txt"><p class="ov">Der Einstieg</p><p class="work">Arbeitstitel: Rhetorik I</p><h2><span class="ph">[Seminar A]</span></h2>'
     '<p>In jeder Situation sprichst du frei und professionell, ohne dich zu verhaspeln.</p>'
     '<ul class="topics topics--2"><li>Sicher auftreten</li><li>Rede halten</li><li>Struktur lernen</li><li>Echt wirken</li><li>Sprache nutzen</li><li>Körper lesen</li><li>Fragen stellen</li></ul>'
     '<div class="format__foot"><span>14 Plätze</span>' + btn() + '</div></div>'
     '</div></div></section>'
     '<section class="screen screen--cream" id="formate"><div class="wrap">'
     '<div class="stack stack--tight"><p class="ov rv">Die Formate</p><h2 class="rv" data-d="1">Eigenständig.<br>In beliebiger Reihenfolge.</h2></div>'
     '<div class="formats">' + fmt + '</div></div></section>'
     '<section class="screen" id="raum"><div class="wrap split">'
     '<div class="stack"><h2 class="rv">Drei Tage, zwölf Menschen,<br>kein Publikum.</h2>'
     '<p class="rv" data-d="1" style="max-width:30em">Kleine Gruppe, damit jeder drankommt. Kein Zuschauen, kein Verstecken in der letzten Reihe.</p>'
     '<ul class="facts rv" data-d="2"><li><b>3 + 1</b>Tage Intensivtraining und ein Tag Get Together</li><li><b>3</b>Videoanalysen mit Sofort-Feedback</li>'
     '<li><b>VR</b>Einzigartiges VR-Training</li><li><b>10–14</b>Plätze je Seminar</li></ul></div>'
     '<div class="frame plx whom__media rv" data-d="1" data-plx="0.1"><img style="object-position:50% 40%" src="assets/pdf-undersold-table.webp" alt="Kleine Gruppe lacht gemeinsam an einem Holztisch" width="590" height="700"></div>'
     '</div></section>'
     '<section class="screen" id="orte"><div class="wrap">'
     '<div class="stack stack--tight"><p class="ov rv">Orte</p><h2 class="rv" data-d="1">Der Ort ist Teil der Arbeit.</h2></div>'
     '<div class="locs locs--6">' + locs + '</div></div></section>'
     '<section class="screen screen--cream" id="fuerwen"><div class="wrap cols">'
     '<h2 class="rv">Für wen das gedacht ist</h2>'
     '<ul class="whom3"><li class="rv">Führungskräfte</li><li class="rv" data-d="1">Gründerinnen und Gründer</li><li class="rv" data-d="2">Beraterinnen und Berater</li></ul>'
     '</div></section>'
     + closing('Der nächste Schritt ist | ein Gespräch.') + '</main>')

def page_michael():
    # Phil (06.10.): the "30 Jahre" slide comes first, the portrait slide second.
    return ('<main id="top">'
     '<section class="screen screen--cream" id="hero"><div class="wrap split">'
     '<div class="frame plx michael__media rv" data-plx="0.09"><img style="object-position:50% 20%" src="assets/michael-jacket.webp" alt="Michael Ehlers sitzt in einem braunen Sakko auf einem Hocker" width="1122" height="1600"></div>'
     '<div class="stack"><p class="ov rv">Über Michael</p><h1 class="rv" data-d="1" style="font-size:var(--h2)">30 Jahre. Über 8.000 Menschen.<br>Eine Methode.</h1>' + STATS +
     '<p class="rv" data-d="2"><span class="ph">[Platzhalter: Fließtext über Michael. Stationen, Bücher, Bühnen, Kunden.]</span></p>'
     '<div class="award rv" data-d="3"><img src="assets/erfolg-top100.webp" alt="ERFOLG Magazin Top 100" width="202" height="249">'
     '<div class="stack stack--tight"><h3>Ausgezeichnet statt austauschbar.</h3><p>Michael Ehlers gehört laut ERFOLG Magazin zu den Top 100 Trainern im deutschsprachigen Raum &amp; ist Top10 Speaker.</p></div></div>'
     + LOGOS + '</div></div></section>'
     # slide 2: real stage photo from the live site (meandyou.de media library, 06.10.)
     '<section class="screen bleed" id="buehne"><div class="bleed__bg"><img data-plx="0.06" style="object-position:50% 40%" src="assets/michael-stage.webp" alt="Michael Ehlers auf der Bühne vor vollem Saal" width="2400" height="1389"></div>'
     '<div class="wrap bleed__in"><div class="stack"><h2 class="rv" data-d="1" style="font-size:clamp(38px,min(5vw,8.6vh),80px)">Dreißig Jahre<br>vor vollen Räumen.</h2>'
     '<p class="rv" data-d="2">Autorität, die man nicht behaupten muss.</p></div></div></section>'
     + closing('Der nächste Schritt ist | ein Gespräch.') + '</main>')

def page_rhetorik():
    return ('<main id="top">'
     '<section class="screen" id="hero"><div class="wrap split">'
     '<div class="stack"><p class="ov rv">Was ist Rhetorik</p><h1 class="rv" data-d="1" style="font-size:clamp(34px,min(4.4vw,7.8vh),70px)">Was Rhetorik wirklich ist<br>und was sie nicht ist.</h1>'
     '<p class="hero__sub rv" data-d="2">Kein Verkaufstext. Eine Erklärung, für alle, die hier zum ersten Mal sind.</p>'
     '<div class="rv" data-d="3"><a class="btn" href="https://www.meandyou.de/sichtbarkeit-neu" data-video="wistia:wb51mevk7b">Kostenloses Training ansehen</a></div></div>'
     '<div class="frame plx michael__media rv" data-d="1" data-plx="0.09"><img style="object-position:50% 25%" src="assets/michael-olive.webp" alt="Michael Ehlers sitzt entspannt in einer olivgrünen Jacke und lächelt" width="1066" height="1600"></div>'
     '</div></section>'
     '<section class="screen screen--cream" id="training"><div class="wrap split">'
     '<div class="stack"><p class="ov rv">Die Methode</p><h2 class="rv" data-d="1">Wirkung beginnt nicht<br>bei der Technik.</h2>'
     '<p class="rv" data-d="2" style="max-width:32em">Die meisten Rhetoriktrainings starten bei Werkzeugen. Wir starten davor: bei Persönlichkeit, Selbstbild, Mustern und innerer Stabilität. Erst wenn das steht, tragen die Werkzeuge.</p>'
     '<p class="rv" data-d="2"><span class="ph">[Platzhalter: Erklärtext für Einsteiger und Einbindung des kostenlosen Trainings.]</span></p></div>'
     + STEPS + '</div></section>'
     + closing('Der nächste Schritt ist | ein Gespräch.') + '</main>')

def page_faq():
    return ('<main id="top">'
     '<section class="screen screen--cream" id="faq"><div class="wrap">'
     '<div class="stack stack--tight"><p class="ov rv">FAQ</p><h1 class="rv" data-d="1" style="font-size:var(--h2)">Häufige Fragen</h1></div>'
     '<div class="faq" id="faq-list"></div></div></section>'
     + closing('Der nächste Schritt ist | ein Gespräch.') + '</main>')

LPS = {
 'replayers': dict(label='Der Nachdenker', img='pdf-replayers-main.webp', pos='90% 45%', alt='Menschen in einer Bahn, eine Frau schreibt in ein Notizbuch',
                   h='Dir fehlen nicht die Worte. | Sie kommen nur zu spät.',
                   body='Im Meeting bleibst du still. Auf dem Heimweg hast du den perfekten Satz. Das Problem ist nicht dein Wissen, sondern der Moment.',
                   pull='Das Schlimmste daran ist, dass dir die perfekte Antwort erst Stunden später einfällt, wenn du abends im Bett liegst oder im Auto nach Hause fährst.'),
 'overlooked': dict(label='Das Problem', img='pdf-overlooked-main.webp', pos='45% 40%', alt='Gespräch an einem Glastisch in einem Büro mit kühlem Licht',
                    h='Recht zu haben | war nie das Problem.',
                    body='Du bist bestinformiert im Raum. Gefolgt wird trotzdem jemand anderem. Zwischen Kompetenz und Wirkung liegt eine Lücke.'),
 'undersold': dict(label='Unter Wert', img='pdf-undersold-main.webp', pos='45% 40%', alt='Handschlag über einen Tisch, die Gruppe applaudiert, warmes Licht',
                   h='Ihr Unternehmen ist größer, | als es nach außen wirkt.',
                   body='Die Substanz stimmt. Der Auftritt bleibt darunter. Nach außen wirkt das Unternehmen kleiner, als es ist.'),
 'coaches': dict(label='Coaches, Berater, Experten', img='pdf-overlooked-thinker.webp', pos='50% 35%', alt='Ein Mann sitzt nachdenklich am Fenster, im Hintergrund eine Stadt',
                 h='Dein Angebot ist nicht das Problem. | Wie du darüber sprichst, vielleicht schon.',
                 body='Du bist fachlich besser als dein Wettbewerb. Aber dein Wettbewerb verkauft sich besser.',
                 draft='Entwurf · Zielgruppe und Texte sind nicht vom Kunden freigegeben'),
}

def page_lp(key):
    d = LPS[key]
    draft = '<div class="draft">%s</div>' % d['draft'] if d.get('draft') else ''
    return ('<main id="top" class="t-%s">' % key +
     '<section class="screen lp-hero" id="hero"><div class="wrap split">'
     '<div class="stack"><p class="ov rv">%s</p><h1 class="rv" data-d="1">%s</h1><p class="rv" data-d="2">%s</p>%s<div class="rv" data-d="3">%s</div></div>' % (d['label'], br(d['h']), d['body'], ('<p class="pull rv" data-d="2" style="font-size:var(--body);max-width:30em">%s</p>' % d['pull']) if d.get('pull') else '', btn(cls='btn btn--light' if key in ('overlooked', 'undersold') else 'btn'))
     + '<div class="frame plx lp-hero__media rv" data-d="1" data-plx="0.1"><img style="object-position:%s" src="assets/%s" alt="%s" width="1536" height="1024"></div>' % (d['pos'], d['img'], d['alt'])
     + '</div></section>'
     '<section class="screen" id="michael"><div class="wrap split">'
     '<div class="frame plx michael__media rv" data-plx="0.09"><img src="assets/michael-door.webp" alt="Michael Ehlers lehnt in weißem Leinenhemd an einem Holzrahmen" width="1300" height="1950"></div>'
     '<div class="stack"><p class="ov rv">Warum Michael</p><h2 class="rv" data-d="1">30 Jahre. Über 8.000 Menschen.<br>Eine Methode.</h2>' + STATS +
     '<p class="rv" data-d="2">Michael Ehlers gehört laut ERFOLG Magazin zu den Top 100 Trainern im deutschsprachigen Raum. Seine Arbeit steht in Büchern, auf Bühnen und in den Unternehmen, die ihn seit Jahren buchen.</p>'
     '<div class="rv" data-d="3">' + btn() + '</div></div></div></section>'
     '<section class="screen screen--cream" id="methode"><div class="wrap split">'
     '<div class="stack"><p class="ov rv">Die Methode</p><h2 class="rv" data-d="1">Wirkung beginnt nicht<br>bei der Technik.</h2>'
     '<p class="rv" data-d="2" style="max-width:32em">Die meisten Rhetoriktrainings starten bei Werkzeugen. Wir starten davor: bei Persönlichkeit, Selbstbild, Mustern und innerer Stabilität. Erst wenn das steht, tragen die Werkzeuge.</p></div>'
     + STEPS + '</div></section>'
     '<section class="screen" id="stimmen"><div class="wrap">'
     '<div class="stack stack--tight" style="margin-bottom:clamp(16px,3vh,30px)"><p class="ov rv">Stimmen</p><h2 class="rv" data-d="1">Was Teilnehmer sagen.</h2></div>'
     + voices() + '</div></section>'
     + closing('Der nächste Schritt ist | ein Gespräch.') + draft + '</main>')

CALENDLY = 'https://calendly.com/me-you/sichtbarkeit-neu?hide_event_type_details=1&hide_gdpr_banner=1&background_color=ffffff&text_color=2a2622&primary_color=64809e'

TERMIN_CSS = ('<style>'
 '.hdr__end .btn{display:none}'
 '.termin{min-height:auto;align-items:start;padding-bottom:clamp(28px,5vh,56px)}'
 '.termin__grid{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(28px,4vw,72px);align-items:start}'
 '.termin h1{font-size:clamp(30px,min(3.4vw,6vh),52px);line-height:1.1}'
 '.termin .step{padding:clamp(12px,2vh,20px) 0}.termin .step:first-child{border-top:0}'
 '.termin .steps{margin-top:clamp(6px,1vh,12px)}'
 '.who{display:flex;align-items:center;gap:14px;padding-top:clamp(12px,2vh,20px);border-top:1px solid var(--line)}'
 '.who img{width:56px;height:56px;border-radius:50%;object-fit:cover;object-position:50% 20%}'
 '.who b{display:block;font-weight:600}.who span{font-size:var(--small);opacity:.8}'
 '.book{background:var(--white,#fff);border:1px solid var(--line);border-radius:var(--r);padding:clamp(16px,2vw,28px);box-shadow:0 12px 40px rgba(42,38,34,.06)}'
 '.book__head{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:8px}'
 '.book__head h2{font-size:clamp(20px,1.6vw,24px)}.book__head span{font-size:var(--small);opacity:.7}'
 '.calendly-inline-widget{min-width:280px;min-height:700px;border-radius:12px;overflow:hidden}.calendly-inline-widget iframe{min-height:700px}'
 '.bring{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,2vw,28px)}'
 '.bring div{background:var(--white,#fff);border-radius:16px;padding:clamp(16px,2vw,24px)}'
 '.bring b{display:block;font-family:var(--serif);font-weight:400;font-size:clamp(18px,1.5vw,22px);margin-bottom:6px}'
 '.bring p{font-size:var(--small)}'
 '.tfaq{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,2vw,28px)}'
 '.tfaq h3{font-size:clamp(16px,1.2vw,18px);margin-bottom:6px}.tfaq p{font-size:var(--small)}'
 '@media (max-width:900px){.termin__grid{grid-template-columns:1fr}.termin__side{order:2}.termin__main{order:1}'
 '.bring,.tfaq{grid-template-columns:1fr}.calendly-inline-widget{height:640px}}'
 '</style>')

def page_termin():
    return ('<main id="top">' + TERMIN_CSS +
     '<section class="screen termin" id="termin"><div class="wrap termin__grid">'
     '<div class="stack termin__side">'
     '<p class="ov rv">Kostenloses Gespräch · 30 Minuten · Online</p>'
     '<h1 class="rv" data-d="1">Finde heraus, wo du<br>gerade Wirkung verlierst.</h1>'
     '<p class="rv" data-d="2" style="max-width:30em">30 Minuten mit dem Team von Michael Ehlers. Du bekommst eine ehrliche Einschätzung und einen Vorschlag für den nächsten Schritt. Kein Verkaufsdruck.</p>'
     '<div class="steps rv" data-d="2">'
     '<div class="step"><i>01</i><div><h3>Termin wählen</h3><p>Rechts im Kalender. Dauert zwei Minuten.</p></div></div>'
     '<div class="step"><i>02</i><div><h3>Drei kurze Fragen</h3><p>Damit wir uns auf dich vorbereiten können.</p></div></div>'
     '<div class="step"><i>03</i><div><h3>Gespräch per Video</h3><p>30 Minuten. Du gehst mit einer klaren Einschätzung raus.</p></div></div>'
     '</div>'
     '<div class="who rv" data-d="3"><img src="assets/michael-jacket.webp" alt="Michael Ehlers" width="112" height="112" style="object-position:50% 12%"><div><b>Michael Ehlers</b><span>Rhetoriktrainer seit über 30 Jahren · über 8.000 Teilnehmer · ERFOLG Magazin Top 100 Trainer</span></div></div>'
     '</div>'
     '<div class="termin__main rv" data-d="1"><div class="book">'
     '<div class="book__head"><h2>Wähle deinen Termin</h2><span>Zeitzone Berlin · nur die nächsten Tage buchbar</span></div>'
     '<div class="calendly-inline-widget" data-url="' + CALENDLY + '" data-resize="true"></div>'
     '<script src="https://assets.calendly.com/assets/external/widget.js" async></script>'
     '</div></div>'
     '</div></section>'
     '<section class="screen screen--cream" id="vorbereitung" style="min-height:auto"><div class="wrap">'
     '<div class="stack stack--tight" style="margin-bottom:clamp(16px,3vh,30px)"><p class="ov rv">Vorbereitung</p><h2 class="rv" data-d="1">Das bringst du mit.</h2></div>'
     '<div class="bring rv" data-d="2">'
     '<div><b>Einen ruhigen Ort</b><p>30 Minuten ohne Unterbrechung, Kamera an.</p></div>'
     '<div><b>Stift und Papier</b><p>Du wirst dir etwas notieren wollen.</p></div>'
     '<div><b>Eine konkrete Situation</b><p>Ein Meeting, ein Pitch, ein Gespräch, in dem du mehr Wirkung willst.</p></div>'
     '</div>'
     '<p class="rv" data-d="3" style="margin-top:clamp(14px,2.4vh,24px);font-size:var(--small);opacity:.8">Du kannst doch nicht? Kein Problem. In deiner Bestätigung ist ein Link, mit dem du in zwei Klicks umbuchst.</p>'
     '</div></section>'
     '<section class="screen" id="fragen" style="min-height:auto"><div class="wrap">'
     '<div class="stack stack--tight" style="margin-bottom:clamp(16px,3vh,30px)"><p class="ov rv">Kurz beantwortet</p><h2 class="rv" data-d="1">Drei Fragen vorab.</h2></div>'
     '<div class="tfaq rv" data-d="2">'
     '<div><h3>Mit wem spreche ich?</h3><p>Mit einem Mitglied aus Michaels Team. Es kennt die Seminare und sagt dir ehrlich, ob und was für dich passt.</p></div>'
     '<div><h3>Was kostet das Gespräch?</h3><p>Nichts. Es gibt keine Verpflichtung. Du entscheidest danach in Ruhe.</p></div>'
     '<div><h3>Was passiert danach?</h3><p>Wenn ein Seminar passt, bekommst du Termine und alle Details. Wenn nicht, hast du trotzdem eine klare Einschätzung.</p></div>'
     '</div></div></section>'
     + footer() + '</main>')

def doc(title, body, active, lp=False, faq=False, light=False):
    faq_js = '<script>window.FAQ=%s;</script>' % __import__('json').dumps(FAQ, ensure_ascii=False) if faq else ''
    return ('<title>%s</title>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">\n'
            '<style>%s%s</style>\n%s\n%s\n'
            '<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.20/dist/lenis.min.js"></script>\n%s<script>%s</script>\n'
            ) % (title, BASE_CSS, CSS_V2, header(active, lp, light), body, faq_js, JS)

def full(content):
    return ('<!doctype html><html lang="de"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>' + content + '</body></html>')

PAGES = {
 'index.html': ('me&you Prototyp v2', page_home(), 'home', False, False),
 'seminare.html': ('Seminare · me&you Prototyp v2', page_seminare(), 'seminare', False, False),
 'michael.html': ('Über Michael · me&you Prototyp v2', page_michael(), 'michael', False, False),
 'rhetorik.html': ('Was ist Rhetorik · me&you Prototyp v2', page_rhetorik(), 'rhetorik', False, False),
 'faq.html': ('FAQ · me&you Prototyp v2', page_faq(), 'faq', False, True),
 'lp-replayers.html': ('Landingpage Replayers · me&you Prototyp v2', page_lp('replayers'), '', True, False),
 'lp-overlooked.html': ('Landingpage Overlooked · me&you Prototyp v2', page_lp('overlooked'), '', True, False),
 'lp-undersold.html': ('Landingpage Undersold · me&you Prototyp v2', page_lp('undersold'), '', True, False),
 'lp-coaches.html': ('Landingpage Coaches (Entwurf) · me&you Prototyp v2', page_lp('coaches'), '', True, False),
 'termin.html': ('Gespräch buchen · me&you Prototyp v2', page_termin(), '', True, False),
}

for name, (title, body, active, lp, faq) in PAGES.items():
    content = doc(title, body, active, lp, faq, name in ('seminare.html', 'lp-overlooked.html', 'lp-undersold.html'))
    open(os.path.join(HERE, name), 'w', encoding='utf-8').write(full(content))
    if name == 'index.html':
        open(os.path.join(HERE, 'page.html'), 'w', encoding='utf-8').write(content)
    print(name, len(content))
