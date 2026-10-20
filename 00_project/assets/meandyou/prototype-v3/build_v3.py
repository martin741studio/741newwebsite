#!/usr/bin/env python3
"""me&you prototype v3: homepage as one journey (flow model: to-top.ch).

Concept: UNÜBERSEHBAR. One thread runs through the page. It starts thin and broken
and ends strong. The visitor picks a situation early, the page adapts.
Reuses helpers, CSS and sub pages from ../prototype-v2/build_v2.py.
Run: python3 build_v3.py
"""
import importlib.util, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
V2DIR = os.path.join(HERE, '..', 'prototype-v2')
spec = importlib.util.spec_from_file_location('build_v2', os.path.join(V2DIR, 'build_v2.py'))
v2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v2)   # also rebuilds the v2 pages

CSS_V3 = r"""
/* ---------- v3: the journey ---------- */
:root{--acc:var(--dove-deep)}
body[data-persona="overlooked"]{--acc:var(--navy)}
body[data-persona="undersold"]{--acc:var(--char)}
main{position:relative}
.wrap{position:relative;z-index:2}
#thread{position:absolute;left:0;top:0;width:100%;height:100%;z-index:1;pointer-events:none;overflow:visible}
#thread path{fill:none;stroke-linecap:round;stroke-linejoin:round;transition:stroke .6s}
#thread .t-n{stroke:var(--acc)}
#thread .t-l{stroke:var(--sand)}

/* hero: question button + media row */
.hero2 h1{font-size:clamp(34px,min(4.5vw,8vh),68px)}
.qbtn{text-decoration:none;position:absolute;left:50%;translate:-50% 0;bottom:clamp(18px,3.6vh,36px);z-index:3;width:clamp(120px,10.5vw,156px);aspect-ratio:1;border-radius:50%;border:0;cursor:pointer;background:var(--navy);color:var(--paper);font:600 clamp(10.5px,.82vw,12.5px)/1.35 var(--sans);letter-spacing:.14em;text-transform:uppercase;display:grid;place-items:center;text-align:center;padding:18px;rotate:-8deg;box-shadow:0 22px 50px -20px rgba(43,60,82,.7);transition:scale .3s,background .3s}
.qbtn:hover{scale:1.06;background:var(--dove-deep)}
.qbtn::after{content:"";position:absolute;inset:-9px;border-radius:50%;border:1px solid var(--navy);opacity:.25}
.known{max-width:min(40vw,520px);display:flex;align-items:center;gap:clamp(14px,2vw,30px);flex-wrap:wrap;margin-top:clamp(10px,2.4vh,26px)}
.known span{font:400 var(--h3)/1 var(--serif);color:var(--ink);padding-right:clamp(12px,1.6vw,24px);border-right:1px solid var(--line)}
.known img{height:clamp(18px,2.9vh,28px);width:auto;filter:grayscale(1) contrast(1.1);opacity:.78;mix-blend-mode:multiply}

/* situations as the choice */
.shead{display:flex;justify-content:space-between;align-items:flex-end;gap:24px}
.tangle-slot{flex:none;width:min(26vw,340px);height:clamp(90px,16vh,150px)}
.hint{font-size:var(--small);color:var(--muted)}
.sit{cursor:pointer;border:0;text-align:left;font:inherit;padding:0;position:relative;transition:opacity .45s,translate .45s,box-shadow .45s,filter .45s}
.sit:focus-visible{outline:2px solid var(--navy);outline-offset:4px}
.sits.has-choice .sit:not(.is-on){opacity:.46;filter:saturate(.55)}
.sit.is-on{translate:0 -8px;box-shadow:0 30px 60px -34px rgba(43,60,82,.75)}
.sit__check{position:absolute;right:14px;top:14px;z-index:2;width:34px;height:34px;border-radius:50%;background:var(--paper);display:grid;place-items:center;opacity:0;scale:.6;transition:opacity .3s,scale .3s}
.sit.is-on .sit__check{opacity:1;scale:1}
.sit__check svg{width:18px;height:18px;stroke:var(--navy);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.sit .lnk{text-decoration:none}

/* method: three cards that stack while you scroll, from pale to strong */
.flow{position:relative;padding-block:calc(var(--hdr) + 24px) clamp(50px,9vh,100px)}
.mhead{max-width:44em;margin-bottom:clamp(22px,5vh,46px)}
.mcard{position:sticky;top:calc(var(--hdr) + 14px + var(--i) * 22px);height:min(66svh,640px);border-radius:28px;overflow:hidden;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);margin-bottom:clamp(22px,5vh,48px);background:var(--c-bg);color:var(--c-fg);box-shadow:0 -22px 60px -36px rgba(43,60,82,.55)}
.mcard__txt{padding:clamp(22px,5vh,54px) clamp(24px,4vw,64px);display:flex;flex-direction:column;justify-content:space-between;min-width:0}
.mcard i{font:400 clamp(70px,min(10vw,18vh),160px)/.9 var(--serif);font-style:normal;color:var(--c-fg);opacity:.22}
.mcard h3{font-size:clamp(30px,min(3.8vw,6.8vh),60px);color:var(--c-fg)}
.mcard p{font:400 var(--h3)/1.35 var(--sans);color:var(--c-fg);opacity:.88;margin-top:10px;max-width:22em}
.mcard__img{position:relative;overflow:hidden;min-height:0}
.mcard__img img{width:100%;height:100%;object-fit:cover}
.mcard--1{--c-bg:var(--dove-soft);--c-fg:var(--ink)}
.mcard--2{--c-bg:var(--sand);--c-fg:var(--ink)}
.mcard--3{--c-bg:var(--navy);--c-fg:var(--on-navy)}

/* places on the teaser */
.placesrow{display:flex;flex-wrap:wrap;gap:6px clamp(16px,2.4vw,36px);font:400 clamp(20px,min(2.1vw,3.8vh),32px)/1.2 var(--serif);color:var(--white)}
.placesrow span + span::before{content:"·";margin-right:clamp(16px,2.4vw,36px);opacity:.6}

/* taste: small first steps */
.taste{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(12px,1.5vw,20px);margin-top:clamp(16px,3vh,30px)}
.tcard{position:relative;background:var(--paper);border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column;text-decoration:none;color:inherit;transition:translate .35s,box-shadow .35s;outline:2px solid transparent;outline-offset:-2px}
.tcard:hover{translate:0 -5px;box-shadow:0 26px 50px -34px rgba(43,60,82,.7)}
.tcard__img{height:clamp(130px,25vh,240px);background:var(--sand-soft);display:grid;place-items:center;overflow:hidden;position:relative}
.tcard__img img{width:100%;height:100%;object-fit:cover}
.tcard__img--cut{align-items:end}
.tcard__img--cut img{object-fit:contain;width:auto;height:90%}
.tcard__img--box{align-items:center}
.tcard__img--box img{height:84%}
.tcard__play{position:absolute;width:54px;height:54px;border-radius:50%;background:rgba(250,248,244,.94);display:grid;place-items:center}
.tcard__play::after{content:"";border-left:14px solid var(--navy);border-block:8.5px solid transparent;margin-left:5px}
.tcard__txt{padding:clamp(14px,2.4vh,22px) clamp(16px,1.5vw,22px) clamp(16px,2.6vh,24px);display:flex;flex-direction:column;gap:8px;flex:1}
.tcard small{font:600 11px/1 var(--sans);letter-spacing:.18em;color:var(--dove-deep)}
.tcard h3{font-size:clamp(19px,min(1.6vw,2.9vh),25px)}
.tcard p{font-size:var(--small);flex:1}
.tcard .lnk{margin-top:6px}
.tcard__rec{position:absolute;left:12px;top:12px;z-index:2;background:var(--navy);color:var(--paper);font:600 10.5px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;padding:8px 11px;border-radius:999px;opacity:0;transition:opacity .4s}
.tcard.is-rec{outline-color:var(--navy)}
.tcard.is-rec .tcard__rec{opacity:1}

/* the thread ends here */
.tend{display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--sand);margin-left:26px;vertical-align:middle;box-shadow:0 0 0 7px rgba(216,204,183,.22)}

/* ---------- hero after the to-top model: type, layered landscape, rising sun ---------- */
.jhero{position:relative;overflow:hidden;background:linear-gradient(180deg,var(--paper) 0%,#F6EEDF 38%,#F3DFC0 62%,#EFD2A6 100%)}
.jhero__type{pointer-events:none;padding-top:calc(var(--hdr) + clamp(34px,9vh,96px));text-align:center;display:flex;flex-direction:column;align-items:center;gap:clamp(8px,1.6vh,16px);position:relative;z-index:6}
.jhero h1{font-size:clamp(40px,min(8.2vw,15.5vh),150px);line-height:.98;letter-spacing:-.025em}
.jhero h1 span{display:block}
.jhero h1 span + span{color:var(--dove-deep);font-size:.66em;line-height:1.1;letter-spacing:-.015em}
.jhero__sub{font:italic 400 clamp(18px,min(2.1vw,3.8vh),32px)/1.2 var(--serif);color:#B5863B}
.jhero__body{max-width:36em;font-size:var(--body);color:var(--char)}
.jhero__scene{position:relative;width:100%;aspect-ratio:3/2;margin-top:-24vw;pointer-events:none}
.lay{position:absolute;left:0;bottom:0;width:100%;height:auto;will-change:transform;pointer-events:none;user-select:none}
.lay--3{z-index:1;bottom:8%}.lay--2{z-index:3;bottom:3%}.lay--1{z-index:4;bottom:-7%}
.jhero__glow{position:absolute;left:50%;top:56%;width:70vw;aspect-ratio:1;translate:-50% -50%;border-radius:50%;background:radial-gradient(circle,rgba(255,236,190,.95) 0%,rgba(255,226,170,.5) 28%,rgba(255,226,170,0) 62%);z-index:0;will-change:transform}
.sun{position:absolute;left:50%;top:41%;z-index:2;width:clamp(120px,15.5vw,230px);aspect-ratio:1;margin-left:calc(clamp(120px,15.5vw,230px) / -2);border-radius:50%;display:grid;place-items:center;text-align:center;text-decoration:none;pointer-events:auto;background:radial-gradient(circle at 34% 30%,#FBE7B4 0%,#F0C877 55%,#E3B15A 100%);color:var(--navy);box-shadow:0 0 0 14px rgba(246,214,150,.28),0 0 90px 30px rgba(246,206,130,.55);will-change:transform;transition:box-shadow .4s}
.sun:hover{box-shadow:0 0 0 20px rgba(246,214,150,.34),0 0 120px 44px rgba(246,206,130,.7)}
.sun span{display:block;rotate:-12deg;font:700 clamp(10.5px,1.02vw,15px)/1.3 var(--sans);letter-spacing:.12em;text-transform:uppercase;max-width:9.5em}
.jhero__fade{position:absolute;left:0;right:0;bottom:-2px;height:24%;z-index:5;background:linear-gradient(180deg,rgba(250,248,244,0) 0%,rgba(250,248,244,.86) 62%,var(--paper) 100%)}
.jhero__known{position:relative;z-index:6;margin-top:clamp(-120px,-10vh,-56px);padding-bottom:clamp(26px,5vh,54px);display:flex;justify-content:center}
.jhero__known .known{max-width:none;justify-content:center;margin:0}

/* ---------- signpost ---------- */
.wegw{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:clamp(24px,5vw,80px);align-items:center}
.post{position:relative;height:min(64svh,600px);perspective:1400px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:clamp(12px,2.4vh,24px)}
.post__pole{z-index:0;transform:translateZ(-90px);position:absolute;left:50%;top:0;bottom:0;width:12px;margin-left:-6px;border-radius:6px;background:linear-gradient(90deg,#3a342f 0%,#6a5f55 45%,#3a342f 100%);box-shadow:0 30px 40px -18px rgba(43,60,82,.5)}
.post__pole::after{content:"";position:absolute;left:50%;top:-10px;width:22px;height:22px;margin-left:-11px;border-radius:50%;background:#4a423b}
.sign{position:relative;z-index:1;border:0;cursor:pointer;width:min(74%,380px);padding:clamp(14px,2.6vh,24px) clamp(22px,2.6vw,40px);background:var(--t-bg);color:var(--t-fg);font:400 clamp(22px,min(2.5vw,4.4vh),38px)/1.1 var(--serif);text-align:left;display:flex;align-items:baseline;gap:14px;box-shadow:0 24px 40px -22px rgba(43,60,82,.6);transition:transform .6s cubic-bezier(.2,.7,.2,1),filter .4s,opacity .4s;will-change:transform}
.sign small{font:600 11px/1 var(--sans);letter-spacing:.18em;opacity:.7}
.sign--l{margin-right:22%;clip-path:polygon(9% 0,100% 0,100% 100%,9% 100%,0 50%);padding-left:clamp(38px,4vw,62px);transform:rotateY(calc(14deg + var(--sway,0deg))) translateZ(8px)}
.sign--r{margin-left:22%;clip-path:polygon(0 0,91% 0,100% 50%,91% 100%,0 100%);padding-right:clamp(38px,4vw,62px);transform:rotateY(calc(-14deg + var(--sway,0deg))) translateZ(8px)}
.sign:hover{transform:rotateY(var(--sway,0deg)) translateZ(26px)}
.sign:focus-visible{outline:2px solid var(--navy);outline-offset:6px}
.post.has-choice .sign:not(.is-on){opacity:.5;filter:saturate(.5)}
.sign.is-on{transform:rotateY(var(--sway,0deg)) translateZ(34px) scale(1.04)}
.post .tangle-slot{position:absolute;left:-6%;top:6%;width:42%;height:34%;z-index:0}
.sits--solo{margin-top:0}

@media (max-width:980px){
  .jhero h1{font-size:clamp(34px,11vw,64px)}
  .jhero__scene{aspect-ratio:1/1.04;margin-top:-4vw}
  .lay{width:172%;max-width:none;left:-64%}
  .sun{top:27%}
  .jhero__glow{top:42%;width:120vw}
  .jhero__fade{height:14%}
  .lay--1{bottom:0}
  .jhero__known{margin-top:0;padding-top:10px;background:var(--paper)}
  .jhero__known .known span{border-right:0;padding-right:0;width:100%;text-align:center}
  .wegw{grid-template-columns:minmax(0,1fr)}
  .post{height:auto;padding-block:26px}
  .sign{width:82%}
}

@media (max-width:980px){
  #thread{display:none}
  .qbtn{position:static;rotate:0deg;width:auto;aspect-ratio:auto;border-radius:999px;padding:14px 20px;margin:0 var(--gut) 24px;justify-self:start}
  .qbtn::after{display:none}
  .tangle-slot{display:none}
  .mcard{position:relative;top:auto;height:auto;grid-template-columns:minmax(0,1fr)}
  .mcard__img{aspect-ratio:16/10}
  .taste{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width:560px){.taste{grid-template-columns:minmax(0,1fr)}}
"""

JS_V3 = r"""
(function(){
  /* ---- the choice: one situation, remembered for this visit ---- */
  var sits = [].slice.call(document.querySelectorAll('.sit[data-persona]'));
  var signs = [].slice.call(document.querySelectorAll('.sign[data-persona]')), post = document.getElementById('post');
  var box = document.querySelector('.sits');
  var REC = {replayers:'training', overlooked:'kurs'};
  function choose(p, store){
    sits.forEach(function(s){ var on = s.getAttribute('data-persona') === p; s.classList.toggle('is-on', on); s.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    signs.forEach(function(g){ var on = g.getAttribute('data-persona') === p; g.classList.toggle('is-on', on); g.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    if(post) post.classList.toggle('has-choice', !!p);
    if(box) box.classList.toggle('has-choice', !!p);
    if(p){ document.body.setAttribute('data-persona', p); } else { document.body.removeAttribute('data-persona'); }
    [].slice.call(document.querySelectorAll('.tcard')).forEach(function(t){ t.classList.toggle('is-rec', !!p && t.getAttribute('data-step') === REC[p]); });
    if(store){ try{ if(p){ sessionStorage.setItem('mey-persona', p); } else { sessionStorage.removeItem('mey-persona'); } }catch(e){} }
  }
  sits.forEach(function(s){
    function pick(e){
      if(e.target.closest && e.target.closest('a')) return;
      var p = s.getAttribute('data-persona');
      choose(s.classList.contains('is-on') ? '' : p, true);
    }
    s.addEventListener('click', pick);
    s.addEventListener('keydown', function(e){ if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); pick(e); } });
  });
  signs.forEach(function(g){
    g.addEventListener('click', function(){
      choose(g.getAttribute('data-persona'), true);
      var t = document.getElementById('situationen');
      if(t){ var a = document.createElement('a'); a.href = '#situationen'; a.style.display = 'none'; document.body.appendChild(a); a.click(); a.remove(); }
    });
  });
  try{ var saved = sessionStorage.getItem('mey-persona'); if(saved){ choose(saved, false); } }catch(e){}

  /* ---- hero scene: layers move at different speeds, the sun rises between them ---- */
  var scene = document.getElementById('scene'), sun = document.getElementById('qbtn'), glow = document.getElementById('glow');
  var l2 = document.getElementById('lay2'), l3 = document.getElementById('lay3'), heroEl = document.getElementById('hero');
  var calm = !!window.__export || window.matchMedia('(prefers-reduced-motion: reduce)').matches, lastY = -1;
  function sceneTick(){
    var y = window.scrollY;
    if(y !== lastY && scene && heroEl){
      lastY = y;
      var max = heroEl.offsetHeight, p = Math.max(0, Math.min(1, y / (max * 0.72)));
      var e = 1 - Math.pow(1 - p, 2.2);
      if(calm){ p = 1; e = window.__export ? 0.3 : 1; y = 0; }
      var h = scene.offsetHeight;
      if(l3) l3.style.transform = 'translate3d(0,' + (y * 0.34).toFixed(1) + 'px,0)';
      if(l2) l2.style.transform = 'translate3d(0,' + (y * 0.16).toFixed(1) + 'px,0)';
      var sy = h * (-0.19 * e) + y * 0.07;
      if(sun) sun.style.transform = 'translate3d(0,' + sy.toFixed(1) + 'px,0) scale(' + (0.88 + 0.12 * e).toFixed(3) + ')';
      if(glow){ glow.style.transform = 'translate3d(0,' + sy.toFixed(1) + 'px,0)'; glow.style.opacity = (0.4 + 0.6 * e).toFixed(2); }
      if(post){ var r = post.getBoundingClientRect(), k = (r.top + r.height / 2 - window.innerHeight / 2) / window.innerHeight; post.style.setProperty('--sway', (Math.max(-1, Math.min(1, k)) * -9).toFixed(2) + 'deg'); }
    }
    requestAnimationFrame(sceneTick);
  }
  sceneTick();

  /* ---- the thread: one line through the page, thin and broken at the start, strong at the end ---- */
  var svg = document.getElementById('thread'), main = document.getElementById('top');
  if(!svg || !main) return;
  var NS = 'http://www.w3.org/2000/svg', clipRect = null;
  function rect(sel){ var el = typeof sel === 'string' ? document.querySelector(sel) : sel; if(!el) return null; var r = el.getBoundingClientRect(), m = main.getBoundingClientRect(); return {l:r.left - m.left, t:r.top - m.top, w:r.width, h:r.height, r:r.right - m.left, b:r.bottom - m.top}; }
  function build(){
    while(svg.firstChild) svg.removeChild(svg.firstChild);
    if(window.innerWidth < 981) return;
    var W = main.clientWidth, H = main.scrollHeight;
    svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H); svg.setAttribute('preserveAspectRatio', 'none');
    var S = function(id){ return rect('#' + id); };
    var hero = S('hero'), weg = S('wegweiser'), sit = S('situationen'), met = S('methode'), mic = S('michael'), sti = S('stimmen'), sem = S('seminare'), kos = S('einstieg'), boo = S('gespraech');
    var q = rect('.jhero__known'), slot = rect('.tangle-slot'), end = rect('#thread-end'), wr = rect('#methode .wrap'), poster = rect('#michael .poster'), mtxt = rect('#michael .split > .stack');
    if(!hero || !weg || !sit || !met || !mic || !sti || !sem || !kos || !boo || !q || !slot || !end) return;
    var gut = parseFloat(getComputedStyle(document.querySelector('#methode .wrap')).paddingLeft) || 40;
    var LG = wr.l + gut * 0.42, RG = wr.r - gut * 0.42;
    var gapX = (poster && mtxt) ? (mtxt.r + poster.l) / 2 : W * 0.5;
    var G = [];  /* groups: [tone, points] */
    var qx = W * 0.5;
    G.push(['n', [[qx, hero.b - 34], [qx - 10, hero.b - 2]]]);
    /* signpost: the thread is tangled */
    var cx = slot.l + slot.w * 0.5, cy = slot.t + slot.h * 0.5, rr = Math.min(slot.w, slot.h) * 0.42, loop = [];
    for(var k = 0; k <= 10; k++){ var a = -Math.PI * 0.75 + k * Math.PI * 0.42, rad = rr * (0.62 + 0.24 * Math.sin(k * 1.7) + (k % 3) * 0.14); loop.push([cx + Math.cos(a) * rad * 1.5, cy + Math.sin(a) * rad * 0.82]); }
    G.push(['n', [[W * 0.44, weg.t + 40]].concat(loop, [[W * 0.5, weg.t + weg.h * 0.86], [RG, weg.b - 14]])]);
    G.push(['n', [[RG, sit.t + sit.h * 0.3], [RG, sit.b - 12]]]);
    /* method: it becomes straight */
    G.push(['n', [[W * 0.5, met.t + 44], [LG, met.t + 120], [LG, met.t + met.h * 0.5], [LG, met.b - 24]]]);
    G.push(['n', [[W * 0.28, mic.t + 46], [gapX, mic.t + mic.h * 0.2], [gapX, mic.b - 24]]]);
    G.push(['n', [[W * 0.66, sti.t + 44], [W * 0.86, sti.t + sti.h * 0.2], [W * 0.86, sti.b - 16]]]);
    G.push(['l', [[W * 0.86, sem.t + 20], [W * 0.74, sem.t + sem.h * 0.5], [W * 0.64, sem.b - 12]]]);
    G.push(['n', [[W * 0.8, kos.t + 44], [RG, kos.t + kos.h * 0.3], [RG, kos.b - 16]]]);
    var ex = end.l + end.w / 2, ey = end.t + end.h / 2;
    G.push(['l', [[W * 0.92, boo.t + 50], [W * 0.78, ey - 110], [ex + 260, ey + 4], [ex + 10, ey]]]);
    /* one smooth spline through all points, cut into groups */
    var P = [], gi = [];
    G.forEach(function(g, i){ g[1].forEach(function(p){ P.push(p); gi.push(i); }); });
    var defs = document.createElementNS(NS, 'defs'), cp = document.createElementNS(NS, 'clipPath'); cp.setAttribute('id', 'thread-clip');
    clipRect = document.createElementNS(NS, 'rect'); clipRect.setAttribute('x', '0'); clipRect.setAttribute('y', '0'); clipRect.setAttribute('width', W); clipRect.setAttribute('height', '0');
    cp.appendChild(clipRect); defs.appendChild(cp); svg.appendChild(defs);
    var grp = document.createElementNS(NS, 'g'); grp.setAttribute('clip-path', 'url(#thread-clip)'); svg.appendChild(grp);
    var d = {}, n = G.length;
    for(var i = 0; i < P.length - 1; i++){
      var p0 = P[Math.max(0, i - 1)], p1 = P[i], p2 = P[i + 1], p3 = P[Math.min(P.length - 1, i + 2)];
      var c1 = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6], c2 = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
      var g = gi[i + 1];
      d[g] = (d[g] || ('M' + p1[0].toFixed(1) + ' ' + p1[1].toFixed(1))) + ' C' + c1[0].toFixed(1) + ' ' + c1[1].toFixed(1) + ',' + c2[0].toFixed(1) + ' ' + c2[1].toFixed(1) + ',' + p2[0].toFixed(1) + ' ' + p2[1].toFixed(1);
    }
    var DASH = ['1.5 11', '2 9', '6 9', '14 9', '28 9'];
    for(var j = 0; j < n; j++){
      if(!d[j]) continue;
      var path = document.createElementNS(NS, 'path'), t = j / (n - 1);
      path.setAttribute('d', d[j]); path.setAttribute('class', G[j][0] === 'l' ? 't-l' : 't-n');
      path.setAttribute('stroke-width', (1.4 + t * 2.4).toFixed(2)); path.setAttribute('stroke-opacity', (0.5 + t * 0.5).toFixed(2));
      path.setAttribute('vector-effect', 'non-scaling-stroke');
      if(DASH[j]) path.setAttribute('stroke-dasharray', DASH[j]);
      grp.appendChild(path);
    }
    reveal();
  }
  var reduce = !!window.__export || window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function reveal(){ if(clipRect){ clipRect.setAttribute('height', reduce ? main.scrollHeight : Math.max(0, window.scrollY + window.innerHeight * 0.7)); } }
  var last = -1;
  (function loop(){ if(window.scrollY !== last){ last = window.scrollY; reveal(); } requestAnimationFrame(loop); })();
  var tmr = null; function rebuild(){ clearTimeout(tmr); tmr = setTimeout(build, 120); }
  window.addEventListener('resize', rebuild); window.addEventListener('load', rebuild);
  if(document.fonts && document.fonts.ready){ document.fonts.ready.then(rebuild); }
  if('ResizeObserver' in window){ new ResizeObserver(rebuild).observe(main); }
  build();
})();
"""

CHECK = '<span class="sit__check" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m5 12.500 4.500 4.500L19 7.500"/></svg></span>'

def page_home():
    sits = ''
    for i, (key, href, img, pos, alt, h, body) in enumerate(v2.SITS):
        sits += ('<div class="sit t-%s rv" data-d="%d" role="button" tabindex="0" aria-pressed="false" data-persona="%s">%s'
                 '<div class="sit__img"><img data-plx="%s" style="object-position:%s" src="assets/%s" alt="%s" width="1536" height="1024"></div>'
                 '<div class="sit__txt"><h3>%s</h3><p>%s</p><a class="lnk" href="%s">Mehr dazu →</a></div></div>'
                 ) % (key, i, key, CHECK, '0.05' if i != 1 else '0.11', pos, img, alt, v2.br(h), body, href)
    known = ('<div class="known rv" data-d="3"><span>Bekannt aus</span>'
             '<img src="assets/logo-zdf.webp" alt="ZDF"><img src="assets/logo-ard.webp" alt="ARD"><img src="assets/logo-rtl.webp" alt="RTL">'
             '<img src="assets/logo-stern.webp" alt="stern"><img src="assets/logo-mdr.webp" alt="mdr"><img src="assets/logo-hr2.webp" alt="hr2"></div>')
    mcards = ''
    for i, (num, title, line, img, pos, alt) in enumerate([
        ('01', 'Persönlichkeit', 'Wer du bist, bevor du sprichst.', 'michael-olive.webp', '50% 22%', 'Michael Ehlers sitzt entspannt und lächelt'),
        ('02', 'Kongruenz', 'Wenn Haltung und Worte dasselbe sagen.', 'michael-table.webp', '50% 28%', 'Michael Ehlers sitzt mit gefalteten Händen an einem Tisch'),
        ('03', 'Wirkung', 'Was davon im Raum ankommt.', 'ai-seminar-room.webp', '42% 40%', 'Michael Ehlers spricht vor einer kleinen Seminargruppe')]):
        mcards += ('<article class="mcard mcard--%d" style="--i:%d"><div class="mcard__txt"><i>%s</i><div><h3>%s</h3><p>%s</p></div></div>'
                   '<div class="mcard__img"><img style="object-position:%s" src="assets/%s" alt="%s"></div></article>') % (i + 1, i, num, title, line, pos, img, alt)
    taste = ''
    for num, step, title, text, link, href, img in [
        ('01', 'training', 'Kostenloses Training', 'Ein Video-Training, das zeigt, wo Wirkung wirklich beginnt.', 'Kostenloses Training ansehen', 'rhetorik.html#training',
         '<div class="tcard__img"><img style="object-position:50% 26%" src="assets/michael-table.webp" alt="Michael Ehlers am Tisch, Standbild des Trainings"><span class="tcard__play" aria-hidden="true"></span></div>'),
        ('02', 'buch', 'Das Buch', '<span class="ph">[Platzhalter: Buchtitel und ein Satz zum Inhalt]</span>', 'Zum Buch', '#einstieg',
         '<div class="tcard__img tcard__img--cut"><img src="assets/michael-buch.webp" alt="Michael Ehlers liest in einem Buch"></div>'),
        ('03', 'community', 'Talk to Me', 'Die Community: täglich ein kleiner Impuls, wöchentliche Live-Calls mit Michael und ein geschützter Raum zum Üben.', 'Zur Community', 'https://www.skool.com/talk-to-me-9409/about',
         '<div class="tcard__img"><img style="object-position:50% 38%" src="assets/pdf-undersold-table.webp" alt="Kleine Gruppe lacht gemeinsam an einem Tisch"></div>'),
        ('04', 'kurs', 'Der Onlinekurs', 'Rhetorik für Intelligente: das Training im eigenen Tempo, mit Feedback.', 'Zum Onlinekurs', 'https://myablefy.com/s/meandyoucommunication/rhetorik-fuer-intelligente-7186974c/payment',
         '<div class="tcard__img tcard__img--cut tcard__img--box"><img src="assets/kurs-box.webp" alt="Verpackung des Onlinekurses, Modul 1"></div>')]:
        taste += ('<a class="tcard rv" data-step="%s" href="%s"><span class="tcard__rec">Dein Einstieg</span>%s'
                  '<div class="tcard__txt"><small>%s</small><h3>%s</h3><p>%s</p><span class="lnk">%s →</span></div></a>') % (step, href, img, num, title, text, link)
    close = v2.closing('Unübersehbar wird man nicht, | indem man lauter wird.', 'Ein Gespräch, 30 Minuten, kostenlos. Wir klären, wo du stehst und welches Format passt.')
    close = close.replace('Gespräch buchen</a></div></div></div></div>', 'Gespräch buchen</a><span class="tend" id="thread-end" aria-hidden="true"></span></div></div></div></div>', 1)
    assert 'thread-end' in close
    return ('<main id="top"><svg id="thread" aria-hidden="true"></svg>'
     # 1 hero: giant type over a layered landscape, the sun is the question button
     '<section class="jhero" id="hero">'
     '<div class="wrap jhero__type">'
     '<p class="eyebrow-c rv">UNÜBERSEHBAR</p>'
     '<h1 class="rv" data-d="1"><span>Werde unübersehbar,</span><span>wenn es darauf ankommt.</span></h1>'
     '<p class="jhero__sub rv" data-d="2">Persönlichkeit. Kongruenz. Wirkung.</p>'
     '<p class="jhero__body rv" data-d="2">Michael Ehlers trainiert seit über 30 Jahren Menschen, die fachlich längst überzeugen und trotzdem nicht gehört werden.</p>'
     '</div>'
     '<div class="jhero__scene" id="scene">'
     '<div class="jhero__glow" id="glow"></div>'
     '<img class="lay lay--3" id="lay3" src="assets/hero-l3.webp" alt="" width="2000" height="1333">'
     '<a class="sun" id="qbtn" href="#wegweiser"><span>Kommt dir das bekannt vor?</span></a>'
     '<img class="lay lay--2" id="lay2" src="assets/hero-l2.webp" alt="" width="2000" height="1333">'
     '<img class="lay lay--1" id="lay1" src="assets/hero-l1.webp" alt="Ein Mensch steht auf einer Steinterrasse und blickt zum Horizont" width="2000" height="1333">'
     '<div class="jhero__fade"></div>'
     '</div>'
     '<div class="wrap jhero__known">' + known + '</div>'
     '</section>'
     # 2a signpost
     '<section class="screen" id="wegweiser"><div class="wrap wegw">'
     '<div class="stack stack--tight wegw__head"><p class="ov rv">Kommt dir das bekannt vor?</p><h2 class="rv" data-d="1">Drei Situationen.<br>Ein gemeinsamer Punkt.</h2>'
     '<p class="hint rv" data-d="2">Welche Situation kennst du? Wähle eine aus.</p></div>'
     '<div class="post rv" data-d="1" id="post"><div class="tangle-slot" aria-hidden="true"></div><span class="post__pole" aria-hidden="true"></span>'
     '<button class="sign sign--l t-replayers" type="button" data-persona="replayers" aria-pressed="false"><small>01</small>Der Nachdenker</button>'
     '<button class="sign sign--r t-overlooked" type="button" data-persona="overlooked" aria-pressed="false"><small>02</small>Das Problem</button>'
     '<button class="sign sign--l t-undersold" type="button" data-persona="undersold" aria-pressed="false"><small>03</small>Unter Wert</button>'
     '</div></div></section>'
     # 2b the three situations
     '<section class="screen" id="situationen"><div class="wrap">'
     '<div class="sits sits--solo">' + sits + '</div></div></section>'
     # 3 method = the climb
     '<section class="flow" id="methode"><div class="wrap">'
     '<div class="mhead stack"><p class="ov rv">Die Methode</p><h2 class="rv" data-d="1">Wirkung beginnt nicht<br>bei der Technik.</h2>'
     '<p class="rv" data-d="2">Die meisten Rhetoriktrainings starten bei Werkzeugen. Wir starten davor: bei Persönlichkeit, Selbstbild, Mustern und innerer Stabilität. Erst wenn das steht, tragen die Werkzeuge.</p></div>'
     + mcards + '</div></section>'
     # 4 Michael = the guide
     '<section class="screen screen--cream" id="michael"><div class="wrap split">'
     '<div class="stack"><p class="ov rv">Warum Michael</p><h2 class="rv" data-d="1">30 Jahre. Über 8.000 Menschen.<br>Eine Methode.</h2>'
     + v2.STATS +
     '<p class="rv" data-d="2">Michael Ehlers gehört zu den bekanntesten Rhetoriktrainern im deutschsprachigen Raum. Seine Arbeit steht in Büchern, auf Bühnen und in den Unternehmen, die ihn seit Jahren buchen.</p>'
     '<div class="award rv" data-d="3"><img src="assets/erfolg-top100.webp" alt="ERFOLG Magazin Top 100" width="202" height="249">'
     '<div class="stack stack--tight"><h3>Ausgezeichnet statt austauschbar.</h3><a class="lnk" href="michael.html">Mehr über Michael →</a></div></div></div>'
     '<div class="poster rv" data-d="1" data-plx="0.08"><img style="object-position:50% 12%" src="assets/michael-door.webp" alt="Michael Ehlers in weißem Leinenhemd, Standbild für das Video" width="1300" height="1950">'
     '<span class="poster__play" aria-hidden="true"></span><p class="poster__cap"><span class="ph">[Platzhalter: Videountertitel, eine Zeile]</span></p></div>'
     '</div></section>'
     # 5 voices
     '<section class="screen" id="stimmen"><div class="wrap">'
     '<div class="stack stack--tight" style="margin-bottom:clamp(16px,3vh,30px)"><p class="ov rv">Stimmen</p><h2 class="rv" data-d="1">Vorher. Nachher.</h2></div>'
     + v2.voices() + '</div></section>'
     # 6 seminars = the place
     '<section class="screen bleed" id="seminare"><div class="bleed__bg"><img data-plx="0.07" style="object-position:50% 45%" src="assets/gen-mallorca.webp" alt="Finca-Terrasse über einer ruhigen Bucht im Abendlicht" width="1536" height="1024"></div>'
     '<div class="wrap bleed__in"><div class="stack"><p class="ov rv">Seminare</p><h2 class="rv" data-d="1">Drei Tage. Kleine Gruppe.<br>Ein Ort, der dazu passt.</h2>'
     '<p class="rv" data-d="2">Kein Konferenzraum, kein Hotelsaal. Die Orte sind Teil der Arbeit, nicht die Kulisse dahinter.</p>'
     '<p class="placesrow rv" data-d="2"><span>Mallorca</span><span>Barcelona</span><span>Zypern</span><span>Frankfurt</span><span>Berlin</span><span>Dubai</span></p>'
     '<div class="rv" data-d="3">' + v2.btn('Seminare ansehen', 'btn btn--light', 'seminare.html') + '</div></div></div></section>'
     # 7 taste
     '<section class="screen screen--cream" id="einstieg"><div class="wrap">'
     '<div class="stack stack--tight"><p class="ov rv">Zum Einstieg</p><h2 class="rv" data-d="1">Erst ausprobieren.<br>Dann entscheiden.</h2>'
     '<p class="rv" data-d="2">Vier Wege, Michaels Arbeit kennenzulernen, bevor wir sprechen.</p></div>'
     '<div class="taste">' + taste + '</div></div></section>'
     # 8 booking = where the thread ends
     + close + '</main>')

def doc(title, body):
    return ('<title>%s</title>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">\n'
            '<style>%s%s%s</style>\n%s\n%s\n'
            '<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.20/dist/lenis.min.js"></script>\n<script>%s</script>\n<script>%s</script>\n'
            ) % (title, v2.BASE_CSS, v2.CSS_V2, CSS_V3, v2.header('home'), body, v2.JS, JS_V3)

content = doc('me&you Journey v3', page_home())
open(os.path.join(HERE, 'page.html'), 'w', encoding='utf-8').write(content)
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(v2.full(content))
for name in v2.PAGES:
    if name != 'index.html':
        shutil.copyfile(os.path.join(V2DIR, name), os.path.join(HERE, name))
print('v3 page.html', len(content))
