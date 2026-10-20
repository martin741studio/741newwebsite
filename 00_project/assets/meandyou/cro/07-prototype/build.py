"""Build the CRO prototype of the me&you homepage (desktop 1440 px). Text = 04-copy/approved-copy.md.
Run: python3 build.py  ->  index.html (open locally or serve the folder)."""
import html, os
HERE = os.path.dirname(os.path.abspath(__file__))
V2 = 'https://clients.741.studio/meandyou/v2/'
BOOK = V2 + 'termin.html?utm_source=startseite&utm_content='
TEL = 'tel:+4915888367664'

def e(s):
    return html.escape(s, quote=False)

def btn(utm, cls='btn'):
    return f'<a class="{cls}" href="{BOOK}{utm}">Gespräch buchen</a>'

def fehlt(t):
    return f'<span class="fehlt" title="[FEHLT]">{e(t)}</span>'

STAR = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.5 5.3 5.8.7-4.3 4 1.1 5.8L10 14.6l-5.1 2.8 1.1-5.8-4.3-4 5.8-.7z"/></svg>'
STARS = '<span class="stars" aria-label="5 Sterne">' + STAR * 5 + '</span>'
CHECK = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10.5l4 4 8-9" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'

CSS = r"""
:root{--paper:#FAF8F4;--cream:#F2EDE4;--sand:#D8CCB7;--dove:#7E99B6;--dove-soft:#DFE6EE;--cta:#4F6D90;--cta-h:#3F5E8C;
--navy:#2B3C52;--char:#47403A;--ink:#2A2622;--muted:#5E5650;--on-dark:#F2EDE4;--line:rgba(71,64,58,.16);--gold:#C9A24A;
--serif:"Libre Baskerville",Georgia,serif;--sans:"Inter",system-ui,-apple-system,"Segoe UI",Arial,sans-serif;--r:22px;--w:1240px}
*{box-sizing:border-box}html{scroll-behavior:auto}
body{margin:0;background:var(--paper);color:var(--ink);font:400 18px/1.62 var(--sans);-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block;height:auto}
a{color:inherit}
a[href^="tel:"]{white-space:nowrap}
section[id]{scroll-margin-top:96px}
h1,h2,h3{font-family:var(--serif);font-weight:400;margin:0;letter-spacing:-.01em;text-wrap:balance}
h2{font-size:44px;line-height:1.16}
h3{font-size:24px;line-height:1.3}
p{margin:0}
.wrap{max-width:var(--w);margin:0 auto;padding:0 40px}
.ov{font:600 14px/1.2 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--cta)}
.sec{padding:120px 0}
.sec--cream{background:var(--cream)}
.sec--navy{background:var(--navy);color:var(--on-dark)}
.stack{display:flex;flex-direction:column;gap:22px}
.lead{font-size:19px;color:var(--muted);max-width:36em}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.5em;background:var(--cta);color:#fff;font:600 17px/1 var(--sans);padding:19px 34px;border-radius:999px;text-decoration:none;white-space:nowrap;box-shadow:0 6px 18px rgba(63,94,140,.22);transition:background .18s cubic-bezier(.22,1,.36,1),transform .18s cubic-bezier(.22,1,.36,1),box-shadow .18s}
.btn:hover{background:var(--cta-h);transform:translateY(-2px);box-shadow:0 10px 26px rgba(63,94,140,.3)}
.btn--ghost{background:transparent;color:var(--ink);box-shadow:none;border:1.5px solid rgba(42,38,34,.28)}
.btn--ghost:hover{background:rgba(42,38,34,.05);box-shadow:none}
.btn--light{background:var(--paper);color:var(--navy);box-shadow:0 6px 18px rgba(0,0,0,.18)}
.btn--light:hover{background:#fff}
.assure{display:flex;align-items:center;gap:8px;font-size:16px;color:var(--muted)}
.assure svg{width:18px;height:18px;color:var(--cta);flex:none}
.cta-row{display:flex;flex-direction:column;align-items:flex-start;gap:14px;margin-top:8px}
.center{text-align:center}.center .cta-row{align-items:center}
.stars{display:inline-flex;gap:2px;vertical-align:-2px}.stars svg{width:17px;height:17px;fill:var(--gold)}
.fehlt{display:inline-block;background:#FFE680;color:#5a4a00;font:600 15px/1.3 var(--sans);padding:2px 8px;border-radius:6px;letter-spacing:0}
.tlink{font-weight:600;color:var(--cta);text-decoration:none;border-bottom:1.5px solid rgba(79,109,144,.35);padding-bottom:2px}
.tlink:hover{border-color:var(--cta)}
/* header */
.hdr{position:fixed;top:18px;left:0;right:0;z-index:50;pointer-events:none}
.hdr__in{pointer-events:auto;max-width:var(--w);margin:0 auto;display:flex;align-items:center;gap:36px;padding:12px 14px 12px 28px;background:rgba(250,248,244,.86);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-radius:999px;box-shadow:0 8px 30px rgba(42,38,34,.08)}
.hdr__logo img{height:34px;width:auto}
.hdr nav{display:flex;gap:30px;margin-left:auto;font-size:16px;font-weight:500}
.hdr nav a{text-decoration:none;color:var(--ink)}.hdr nav a:hover{color:var(--cta)}
.hdr .btn{padding:14px 24px;font-size:16px}
/* hero */
.hero{position:relative;min-height:760px;height:100vh;max-height:900px;display:flex;align-items:center;overflow:hidden;background:var(--paper)}
.hero__img{position:absolute;inset:0 0 0 auto;width:66%;overflow:hidden}
.hero__img img{width:100%;height:118%;margin-top:-6%;object-fit:cover;object-position:62% 30%}
.hero__img::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,var(--paper) 0%,rgba(250,248,244,.86) 22%,rgba(250,248,244,0) 52%)}
.hero__in{position:relative;z-index:2;width:100%}
.hero__txt{max-width:780px;display:flex;flex-direction:column;gap:18px;padding-top:64px}
.proofline{display:flex;align-items:center;gap:10px;font-size:16px;font-weight:500;color:var(--muted)}
.hero h1{display:flex;flex-direction:column;gap:14px}
.hero h1 .kicker{font:600 16px/1.3 var(--sans);letter-spacing:.06em;color:var(--cta)}
.hero h1 .big{font-size:56px;line-height:1.08;color:var(--ink)}
.hero .sub{font:italic 400 23px/1.35 var(--serif);color:var(--cta)}
.hero .body{font-size:19px;color:var(--muted);max-width:31em}
.hero .btns{display:flex;gap:14px;flex-wrap:nowrap}
/* proof band */
.proof{padding:84px 0 70px;background:var(--cream)}
.proof__grid{display:grid;grid-template-columns:1.05fr 1fr;gap:72px;align-items:start}
.proof__ans h2{font-size:34px;margin-bottom:22px}
.proof__ans p{font-size:18px;color:var(--muted)}
.badges{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.badges .badge:first-child{grid-column:1/-1}
.badge{background:var(--paper);border-radius:18px;padding:22px 24px;display:flex;flex-direction:column;gap:6px}
.badge b{font:400 26px/1.15 var(--serif);color:var(--ink)}
.badge span{font-size:16px;color:var(--muted);line-height:1.4}
.badge .stars{margin-bottom:2px}
.pquote{margin-top:16px;padding:20px 24px;border-left:3px solid var(--dove);font:italic 400 20px/1.45 var(--serif)}
.pquote small{display:block;margin-top:8px;font:500 16px/1.3 var(--sans);font-style:normal;color:var(--muted)}
.media{margin-top:54px;padding-top:30px;border-top:1px solid var(--line);display:flex;align-items:center;gap:44px}
.media span{font-size:16px;color:var(--muted);white-space:nowrap}
.media img{height:34px;width:auto;opacity:.55;filter:grayscale(1)}
/* situations */
.sits{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}
.sit{border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column;background:var(--bg);color:var(--fg);text-decoration:none}
.sit__img{height:300px;overflow:hidden}.sit__img img{width:100%;height:116%;object-fit:cover}
.sit__txt{padding:30px 30px 34px;display:flex;flex-direction:column;gap:14px;flex:1}
.sit h3{color:var(--fg);font-size:25px}
.sit p{font-size:17px;opacity:.9}
.sit .tlink{color:var(--acc);border-color:currentColor;margin-top:auto;font-size:16px}
.t1{--bg:var(--dove-soft);--fg:var(--ink);--acc:var(--cta)}
.t2{--bg:var(--navy);--fg:var(--on-dark);--acc:var(--sand)}
.t3{--bg:var(--char);--fg:var(--on-dark);--acc:var(--sand)}
.after{display:grid;grid-template-columns:1.1fr 1fr;gap:64px;margin-top:64px;align-items:start}
.after p.strong{font:400 26px/1.4 var(--serif)}
.forwho{display:flex;flex-direction:column;gap:12px}
.forwho ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.forwho li{display:flex;gap:10px;font-size:17px}.forwho li svg{width:20px;height:20px;color:var(--cta);flex:none;margin-top:4px}
/* michael */
.split{display:grid;grid-template-columns:1.2fr .8fr;gap:72px;align-items:center}
.stats{display:grid;grid-template-columns:repeat(4,1fr);border-block:1px solid var(--line);padding:22px 0;margin:6px 0}
.stats div{display:flex;flex-direction:column;gap:4px;padding-right:12px}
.stats b{font:400 28px/1.1 var(--serif);color:var(--cta);white-space:nowrap}
.stats span{font-size:16px;color:var(--muted);line-height:1.35}
.mquote{border-left:3px solid var(--dove);padding:6px 0 6px 22px;font:italic 400 20px/1.5 var(--serif)}
.mquote small{display:block;margin-top:10px;font:500 16px/1 var(--sans);font-style:normal;color:var(--muted)}
.portrait{border-radius:var(--r);overflow:hidden;height:720px}
.portrait img{width:100%;height:112%;object-fit:cover;object-position:50% 25%}
.row-links{display:flex;align-items:center;gap:28px;flex-wrap:wrap}
/* method */
#methode h2,#faq h2{font-size:38px}
#michael h2{font-size:40px}
.method{display:grid;grid-template-columns:1fr 1.05fr .9fr;gap:64px;align-items:start}
.steps{border-top:1px solid var(--line)}
.step{display:grid;grid-template-columns:86px 1fr;gap:18px;align-items:baseline;padding:28px 0;border-bottom:1px solid var(--line)}
.step i{font:400 46px/1 var(--serif);color:var(--dove);font-style:normal}
.step h3{font-size:26px;margin-bottom:6px}.step p{color:var(--muted)}
/* seminars */
.band{position:relative;height:640px;overflow:hidden;color:var(--on-dark)}
.band__bg{position:absolute;inset:0}.band__bg img{width:100%;height:116%;object-fit:cover;margin-top:-4%}
.band::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(28,32,40,.72) 0%,rgba(28,32,40,.35) 45%,rgba(28,32,40,0) 75%)}
.band__in{position:relative;z-index:2;height:100%;display:flex;align-items:flex-end;padding-bottom:84px}
.band h2{color:#fff;font-size:50px;max-width:17em}
.band p{font-size:19px;max-width:30em;color:rgba(255,255,255,.9);margin-top:18px}
.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:-56px;position:relative;z-index:3}
.fact{background:var(--paper);border-radius:18px;padding:24px 26px;box-shadow:0 10px 30px rgba(42,38,34,.08)}
.fact b{display:block;font:400 25px/1.15 var(--serif);white-space:nowrap;color:var(--cta);margin-bottom:6px}
.fact span{font-size:16px;color:var(--muted)}
.noladder{margin:56px 0 30px;font:400 24px/1.4 var(--serif)}
.formats{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.fmt{background:#fff;border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column;box-shadow:0 1px 0 var(--line)}
.fmt__img{height:220px;overflow:hidden}.fmt__img img{width:100%;height:100%;object-fit:cover;transition:transform .5s cubic-bezier(.22,1,.36,1)}
.fmt:hover .fmt__img img{transform:scale(1.03)}
.fmt__txt{padding:26px 28px 30px;display:flex;flex-direction:column;gap:12px;flex:1}
.fmt .wt{font-size:16px;color:var(--muted)}
.fmt p{font-size:17px;color:var(--muted)}
.fmt .tlink{margin-top:auto;font-size:16px}
/* first call */
.flow{display:grid;grid-template-columns:repeat(3,1fr);gap:44px;position:relative;margin-top:64px}
.flow__line{position:absolute;top:27px;left:56px;right:calc(33.3% - 14px);height:2px;background:var(--line)}
.flow__line i{position:absolute;inset:0;background:var(--cta);transform-origin:left;transform:scaleX(0);transition:transform .9s cubic-bezier(.22,1,.36,1)}
.is-in .flow__line i,.shot .flow__line i{transform:scaleX(1)}
.fstep{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:16px}
.fstep__t{display:flex;flex-direction:column;gap:10px}
.clar-h{margin-top:12px;font-weight:600;font-size:17px}
.clar{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.clar li{display:flex;gap:9px;font-size:16.5px}.clar li svg{width:19px;height:19px;color:var(--cta);flex:none;margin-top:4px}
.clar-note{font-size:16px;color:var(--muted);background:var(--paper);border-radius:14px;padding:14px 16px;margin-top:6px}
.fstep .n{flex:none;width:56px;height:56px;border-radius:50%;background:var(--paper);border:2px solid var(--cta);color:var(--cta);font:400 24px/52px var(--serif);text-align:center;position:relative;z-index:2;transition:background .3s,color .3s}
.is-in .fstep .n,.shot .fstep .n{background:var(--cta);color:#fff}
.fstep h3{font-size:23px}.fstep__t>p{font-size:17px;color:var(--muted)}
.fstep .fehlt{margin-top:2px}
.clarify{margin:56px auto 0;max-width:760px;background:var(--paper);border-radius:var(--r);padding:30px 38px;display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
.clarify ul{list-style:none;margin:10px 0 0;padding:0;display:flex;flex-direction:column;gap:8px}
.clarify li{display:flex;gap:10px;font-size:17px}.clarify li svg{width:20px;height:20px;color:var(--cta);flex:none;margin-top:4px}
.clarify p{font-size:17px;color:var(--muted)}
/* voices */
.qgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:48px}
.q{background:#fff;border-radius:var(--r);padding:30px 30px 26px;display:flex;flex-direction:column;gap:14px}
.q h3{font:600 17px/1.3 var(--sans)}
.q blockquote{margin:0;font:400 18px/1.55 var(--serif);flex:1}
.q .who{display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:16px;color:var(--muted);padding-top:14px;border-top:1px solid var(--line)}
.src{font-weight:600;color:var(--ink)}
.vids{display:grid;grid-template-columns:repeat(3,250px);gap:22px;justify-content:center;margin-top:56px}
.vid{position:relative;border-radius:18px;overflow:hidden;aspect-ratio:9/14}
.vid img{width:100%;height:100%;object-fit:cover}
.vid b{position:absolute;inset:0;margin:auto;width:58px;height:58px;border-radius:50%;background:rgba(255,255,255,.92);display:grid;place-items:center}
.vid b svg{width:24px;height:24px;fill:var(--navy);margin-left:3px}
.vid span{position:absolute;left:12px;bottom:10px;color:#fff;font-size:16px;font-weight:600;text-shadow:0 1px 4px rgba(0,0,0,.5)}
.vcap{margin-top:18px;font-size:16px;color:var(--muted)}
/* places */
.places{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px}
.place{display:grid;grid-template-columns:42% 1fr;gap:18px;background:rgba(255,255,255,.06);border:1px solid rgba(242,237,228,.12);border-radius:var(--r);overflow:hidden;align-items:stretch}
.place__img{overflow:hidden;min-height:190px}.place__img img{width:100%;height:116%;object-fit:cover}
.place__t{padding:20px 18px 20px 0;display:flex;flex-direction:column;gap:6px}
.place h3{color:#fff;font-size:25px}
.place .fmtn{font:600 14px/1.2 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--sand)}
.place .claim{font:italic 400 17px/1.4 var(--serif);color:rgba(242,237,228,.85)}
.place .dates{font-size:16px;line-height:1.5;color:var(--on-dark);margin-top:auto}
.place .dates b{font-weight:600}
.stand{margin-top:44px;color:rgba(242,237,228,.8);font-size:17px;max-width:44em}
/* faq */
.faqgrid{display:grid;grid-template-columns:.62fr 1.38fr;gap:64px;align-items:start}
.acc{display:grid;grid-template-columns:1fr 1fr;column-gap:40px;align-items:start}
.acc details{border-bottom:1px solid var(--line)}
.acc details:nth-child(-n+2){border-top:1px solid var(--line)}
.acc summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:20px;padding:20px 0;font:400 18.5px/1.4 var(--serif)}
.acc summary::-webkit-details-marker{display:none}
.acc summary::after{content:"+";font:300 28px/1 var(--sans);color:var(--cta);transition:transform .25s}
.acc details[open] summary{color:var(--cta)}
.acc details[open] summary::after{transform:rotate(45deg)}
.acc .a{padding:0 20px 22px 0;color:var(--muted);font-size:17px}
.morelinks{margin-top:26px;font-size:17px;color:var(--muted)}
/* closer */
.closer{position:relative;overflow:hidden;color:var(--on-dark);padding:150px 0 130px}
.closer__bg{position:absolute;inset:0}.closer__bg img{width:100%;height:116%;object-fit:cover;margin-top:-4%}
.closer::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(24,30,40,.86) 0%,rgba(24,30,40,.6) 48%,rgba(24,30,40,.2) 100%)}
.closer__in{position:relative;z-index:2;max-width:780px;display:flex;flex-direction:column;gap:22px}
.closer h2{color:#fff;font-size:50px}
.closer p{font-size:19px;color:rgba(255,255,255,.9);max-width:34em}
.closer ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.closer li{display:flex;gap:10px;font-size:18px}.closer li svg{width:20px;height:20px;color:var(--sand);flex:none;margin-top:4px}
.closer .proofline{color:rgba(255,255,255,.85)}
.closer .tel{color:rgba(255,255,255,.85);font-size:17px}.closer .tel a{color:#fff}
/* footer */
.foot{background:var(--navy);color:rgba(242,237,228,.85);padding:72px 0 56px;font-size:16px}
.foot__in{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr 1.2fr;gap:40px}
.foot img{height:44px;width:auto}
.foot h4{margin:0 0 14px;font:600 14px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:#fff}
.foot a{display:block;text-decoration:none;margin-bottom:8px}.foot a:hover{color:#fff}
.foot .addr{margin-top:18px;line-height:1.6}
.proto{position:fixed;right:16px;bottom:16px;z-index:60;background:var(--ink);color:#fff;font-size:14px;padding:8px 12px;border-radius:8px;opacity:.82}
/* motion */
.rv{opacity:0;transform:translateY(24px);transition:opacity .5s cubic-bezier(.22,1,.36,1),transform .5s cubic-bezier(.22,1,.36,1)}
.rv.is-in{opacity:1;transform:none}
.badge .stars svg,.q .stars svg{fill:none;stroke:var(--gold);stroke-width:1.4;transition:fill .3s}
.is-in .stars svg{fill:var(--gold)}
.is-in .stars svg:nth-child(2){transition-delay:.08s}.is-in .stars svg:nth-child(3){transition-delay:.16s}.is-in .stars svg:nth-child(4){transition-delay:.24s}.is-in .stars svg:nth-child(5){transition-delay:.32s}
.cta--breathe{animation:breathe 4.5s ease-in-out infinite}
.cta--breathe:hover{animation-play-state:paused}
@keyframes breathe{0%,100%{transform:scale(1);box-shadow:0 6px 18px rgba(63,94,140,.22)}50%{transform:scale(1.025);box-shadow:0 10px 28px rgba(63,94,140,.32)}}
.shot .rv{opacity:1;transform:none;transition:none}.shot .stars svg{fill:var(--gold)}.shot .cta--breathe{animation:none}
@media (prefers-reduced-motion:reduce){.rv{transform:none;transition:opacity .3s}.cta--breathe{animation:none}.flow__line i{transition:none}}
"""

JS = r"""
(function(){
 var shot = /[?&]shot=1/.test(location.search);
 if(shot){document.documentElement.classList.add('shot');}
 var io = new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('is-in');io.unobserve(x.target);}});},{threshold:.2});
 document.querySelectorAll('.rv,[data-in]').forEach(function(el){ if(shot){el.classList.add('is-in');} else {io.observe(el);} });
 // hero reveals on load, 90 ms apart
 document.querySelectorAll('.hero .rv').forEach(function(el,i){setTimeout(function(){el.classList.add('is-in');},80+i*90);});
 // one parallax factor for all large photos (Martin, me&you override)
 var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
 var px = [].slice.call(document.querySelectorAll('[data-plx]'));
 function plx(){ if(reduce||shot) return; var vh = innerHeight; px.forEach(function(el){ var r = el.parentElement.getBoundingClientRect(); if(r.bottom<0||r.top>vh) return; var c = (r.top + r.height/2 - vh/2); el.style.transform = 'translate3d(0,' + (c*-0.05).toFixed(1) + 'px,0)'; }); }
 addEventListener('scroll', plx, {passive:true}); plx();
 // one FAQ open at a time
 var ds = document.querySelectorAll('.acc details');
 ds.forEach(function(d){ d.addEventListener('toggle', function(){ if(d.open){ ds.forEach(function(o){ if(o!==d) o.open=false; }); } }); });
})();
"""

def section_hero():
    return f'''
<section class="hero" id="top">
 <div class="hero__img"><img data-plx src="assets/michael-magazine.webp" alt="Michael Ehlers, Rhetoriktrainer, liest an einem Café-Tisch im Freien" width="1467" height="2200"></div>
 <div class="wrap hero__in"><div class="hero__txt">
  <p class="proofline rv">{STARS} 227 von 250 Bewertungen mit 5 Sternen auf ProvenExpert · 4,8 bei Google · über 8.000 Teilnehmer</p>
  <h1 class="rv"><span class="kicker">Rhetorik-Seminar mit Michael Ehlers:</span><span class="big">Werde unübersehbar, wenn es darauf ankommt.</span></h1>
  <p class="sub rv">Persönlichkeit. Kongruenz. Wirkung.</p>
  <p class="body rv">Michael Ehlers trainiert seit über 30 Jahren Menschen, die fachlich längst überzeugen und trotzdem nicht gehört werden. Drei Tage Intensivtraining in kleiner Gruppe, mit Videoanalyse und Sofort-Feedback.</p>
  <div class="cta-row rv">
   <div class="btns">{btn('hero','btn cta--breathe')}<a class="btn btn--ghost" href="#termine">Termine ansehen</a></div>
   <p class="assure">{CHECK}30 Minuten, kostenlos, per Video. Du klärst, welches Seminar zu dir passt.</p>
  </div>
 </div></div>
</section>'''

def section_proof():
    logos = ''.join(f'<img src="assets/logo-{n}.webp" alt="{a}">' for n, a in [('zdf','ZDF'),('ard','ARD'),('rtl','RTL'),('stern','stern'),('mdr','MDR'),('hr2','hr2')])
    return f'''
<section class="proof" id="kurz">
 <div class="wrap">
  <div class="proof__grid">
   <div class="proof__ans rv"><h2>Wie läuft das Rhetorik-Seminar von Michael Ehlers ab?</h2>
    <p>Das Rhetorik-Seminar dauert drei Tage, dazu kommt ein Tag Get Together. Du trainierst in einer Gruppe von höchstens 14 Menschen, mit drei Videoanalysen und VR-Training. Seminarorte sind Mallorca, Barcelona, Zypern, Dubai, Frankfurt und Berlin. Der erste Schritt ist ein kostenloses Gespräch von 30 Minuten.</p></div>
   <div class="rv" data-in>
    <div class="badges">
     <div class="badge">{STARS}<b>250 Bewertungen</b><span>auf ProvenExpert, 227 davon mit 5 Sternen</span></div>
     <div class="badge"><b>Top 100 Trainer</b><span>im deutschsprachigen Raum laut ERFOLG Magazin</span></div>
     <div class="badge"><b>über 8.000</b><span>Teilnehmer seit über 30 Jahren</span></div>
    </div>
    <p class="pquote">„[…] zwischen der ersten und der letzten Rede lagen wirklich Welten.“<small>Jenny E., Teilnehmerin, Google</small></p>
   </div>
  </div>
  <div class="media rv"><span>Michael Ehlers in den Medien: ZDF, ARD, RTL, stern, MDR, hr2</span>{logos}</div>
 </div>
</section>'''

def section_sits():
    cards = [
     ('t1','sit-replayers.webp','Eine Frau schreibt abends am Schreibtisch in ein Notizbuch','Dir fehlen nicht die Worte. Sie kommen nur zu spät.','Im Meeting bleibst du still. Auf dem Heimweg hast du den perfekten Satz. Das Problem ist nicht dein Wissen, sondern der Moment.','https://clients.741.studio/meandyou/v2/lp-replayers.html','Mehr dazu: Wenn dir die Worte zu spät kommen'),
     ('t2','sit-overlooked.webp','Besprechung an einem Glastisch, eine Frau spricht, die anderen sehen weg','Recht zu haben war nie das Problem.','Du bist bestinformiert im Raum. Gefolgt wird trotzdem jemand anderem. Zwischen Kompetenz und Wirkung liegt eine Lücke.','https://clients.741.studio/meandyou/v2/lp-overlooked.html','Mehr dazu: Recht haben und trotzdem überhört werden'),
     ('t3','sit-undersold.webp','Eine Gründerin erklärt zwei Kunden am Holztisch ihr Unternehmen, warmes Licht','Dein Unternehmen ist größer, als es nach außen wirkt.','Die Substanz stimmt. Der Auftritt bleibt darunter. Nach außen wirkt das Unternehmen kleiner, als es ist.','https://clients.741.studio/meandyou/v2/lp-undersold.html','Mehr dazu: Wenn dein Unternehmen kleiner wirkt'),
    ]
    c = ''.join(f'<a class="sit {t} rv" href="{href}"><div class="sit__img"><img data-plx src="assets/{img}" alt="{alt}"></div><div class="sit__txt"><h3>{e(h)}</h3><p>{e(b)}</p><span class="tlink">{e(l)}</span></div></a>' for t,img,alt,h,b,href,l in cards)
    items = ['als überzeugend und vertrauenswürdig wahrgenommen werden willst','sicher auftreten willst, ohne laut oder aufdringlich zu sein','den Wert deiner Ideen auf den Punkt bringen willst, ohne dich in Fachwissen zu verlieren','Gespräche lenken willst, statt nur zu reagieren']
    li = ''.join(f'<li>{CHECK}<span>{e(x)}</span></li>' for x in items)
    return f'''
<section class="sec" id="situationen">
 <div class="wrap">
  <div class="stack"><p class="ov rv">Kommt dir das bekannt vor?</p><h2 class="rv">Drei Situationen.<br>Ein gemeinsamer Punkt.</h2></div>
  <div class="sits">{c}</div>
  <div class="after">
   <div class="stack rv"><p class="strong">Der gemeinsame Punkt: Was du weißt, kommt im entscheidenden Moment nicht an. Genau dort setzt das Seminar an. Bei deiner Haltung, bevor es um Techniken geht.</p>
    <div class="cta-row">{btn('situationen')}<p class="assure">{CHECK}30 Minuten, kostenlos, per Video.</p></div></div>
   <div class="forwho rv"><p>Gedacht ist es für Führungskräfte, Gründerinnen und Gründer, Beraterinnen und Berater. Genauso bist du hier richtig, wenn du:</p><ul>{li}</ul></div>
  </div>
 </div>
</section>'''

def section_michael():
    return f'''
<section class="sec sec--cream" id="michael">
 <div class="wrap split">
  <div class="stack">
   <p class="ov rv">Warum Michael</p>
   <h2 class="rv">30 Jahre. Über 8.000 Menschen.<br>Eine Methode.</h2>
   <div class="stats rv"><div><b>30+</b><span>Jahre als Rhetoriktrainer</span></div><div><b>8.000+</b><span>Teilnehmer</span></div><div><b>Top 100</b><span>Trainer laut ERFOLG Magazin</span></div><div><b>1.000+</b><span>Vorträge und Medienauftritte</span></div></div>
   <p class="lead rv">Das ERFOLG Magazin hat Michael Ehlers zu den Top 100 Trainern im deutschsprachigen Raum gezählt und als Top-10-Speaker genannt. Er hat Führungskräfte und Unternehmer trainiert, dazu Moderatoren, Politiker sowie Profisportler. Seine Arbeit steht in Büchern, auf Bühnen und in den Unternehmen, die ihn seit Jahren buchen. Aus dieser Arbeit stammt das Ehlers-Rhetorik-Framework.</p>
   <p class="mquote rv">„Zu mir kommen regelmäßig Menschen, die von sich denken, sie wären ‚keine großen Redner‘. Nach 3 Dekaden als Rhetorik-Experte kann ich dir allerdings eines versichern: Jeder kann andere rhetorisch begeistern und fesseln. Völlig gleich, wie introvertiert du bist.“<small>Michael Ehlers</small></p>
   <div class="row-links rv">{btn('michael')}<a class="tlink" href="https://clients.741.studio/meandyou/v2/michael.html">Mehr über Michael</a></div>
  </div>
  <div class="portrait rv"><img data-plx src="assets/michael-door.webp" alt="Michael Ehlers im weißen Leinenhemd an einem Holzrahmen" width="1200" height="1800"></div>
 </div>
</section>'''

def section_method():
    steps = [('01','Persönlichkeit.','Wer du bist, bevor du sprichst.'),('02','Kongruenz.','Wenn Haltung und Worte dasselbe sagen.'),('03','Wirkung.','Was davon im Raum ankommt.')]
    s = ''.join(f'<div class="step rv"><i>{n}</i><div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>' for n,t,d in steps)
    return f'''
<section class="sec" id="methode">
 <div class="wrap method">
  <div class="stack">
   <p class="ov rv">Die Methode</p>
   <h2 class="rv">Wirkung beginnt nicht bei der Technik.</h2>
   <p class="lead rv">Die meisten Rhetoriktrainings starten bei Werkzeugen. Wir starten davor: bei Persönlichkeit, Selbstbild, Mustern und innerer Stabilität. Erst wenn das steht, tragen die Werkzeuge.</p>
  </div>
  <div class="stack">
   <p class="ov rv">Die Methode hat drei Schritte:</p>
   <div class="steps">{s}</div>
  </div>
  <div class="stack" style="padding-top:44px">
   <p class="lead rv">Vielleicht hast du schon Rhetorik-Kurse besucht, und wirklich verändert hat sich nichts. Auf vielen Seminaren lernst du Gestik und Mimik und sollst dabei schauspielern. Die Techniken fühlen sich falsch an. Unter Druck sind sie weg.</p>
   <p class="lead rv" style="color:var(--ink)">Hier musst du nicht schauspielern. Deine kommunikativen Fähigkeiten werden herausgearbeitet, damit sie zu deinem Naturell passen. Das Ziel: Rhetorik wird ein fester Teil deines Auftretens.</p>
  </div>
 </div>
</section>'''

def section_seminars():
    fmts = [
     ('fmt-frei.webp','Kleine Gruppe übt freie Rede in einem hellen Raum','Frei sprechen, auch mit Lampenfieber','Der Einstieg. Arbeitstitel Rhetorik I',' Du lernst, sicher aufzutreten, eine Rede oder Präsentation mit klarer Struktur aufzubauen und in zwei Minuten ein starkes Statement zu setzen. Dazu kommen Körpersprache und Sprache. Mit den richtigen Fragen lenkst du Gespräche in deine Richtung. Am Ende hast du deinen eigenen Redestil.','https://clients.741.studio/meandyou/v2/seminare.html#frei-sprechen','Frei sprechen im Detail'),
     ('fmt-ruhig.webp','Zwei Menschen im ruhigen Streitgespräch an einem Tisch','Ruhig bleiben, wenn es eng wird','Arbeitstitel Rhetorik II',' Schlagfertigkeit und Argumentation mit Überzeugungspsychologie. Dazu Meetings, die zu klaren Ergebnissen führen. Du lernst, unfaire Methoden zu durchschauen und Angriffe ruhig zu kontern. Du liest die Signale deines Gegenübers und setzt deine eigene Körpersprache bewusst ein. Für alle, die im Meeting öfter angegriffen als gehört werden.','https://clients.741.studio/meandyou/v2/seminare.html#ruhig-bleiben','Schlagfertigkeit im Detail'),
     ('fmt-fuehren.webp','Eine Frau spricht frei vor einer kleinen Gruppe','Mit Sprache führen','Arbeitstitel Rhetorik III',' Kritik, die motiviert, und Zuhören, das verbindet. Dazu Stegreifreden vor einer Gruppe und Methoden großer Redner, die du im Alltag nutzt. Mit dem Persönlichkeitsmodell DeepOcean verstehst du, wie deine Persönlichkeit deine Rhetorik prägt.','https://clients.741.studio/meandyou/v2/seminare.html#mit-sprache-fuehren','Führen mit Sprache im Detail'),
    ]
    f = ''.join(f'<article class="fmt rv"><div class="fmt__img"><img src="assets/{img}" alt="{alt}"></div><div class="fmt__txt"><h3>{e(h)}</h3><p class="wt">{e(wt)} {fehlt("[von Kunde bestätigen: Seminarname]")}.</p><p>{e(b.strip())}</p><a class="tlink" href="{href}">{e(l)}</a></div></article>' for img,alt,h,wt,b,href,l in fmts)
    return f'''
<section id="seminare">
 <div class="band">
  <div class="band__bg"><img data-plx src="assets/band-finca.webp" alt="Kleine Seminargruppe an einem langen Holztisch auf einer Finca-Terrasse über dem Meer" width="1536" height="1024"></div>
  <div class="wrap band__in"><div><p class="ov rv" style="color:var(--sand)">Seminare</p><h2 class="rv">Drei Tage. Kleine Gruppe.<br>Ein Ort, der dazu passt.</h2><p class="rv">Kein Konferenzraum, kein Hotelsaal. Die Orte sind Teil der Arbeit, nicht die Kulisse dahinter.</p></div></div>
 </div>
 <div class="sec" style="padding-top:0">
  <div class="wrap">
   <div class="facts">
    <div class="fact rv"><b>3 + 1 Tage:</b><span>Intensivtraining und ein Tag Get Together</span></div>
    <div class="fact rv"><b>3 Videoanalysen</b><span>mit Sofort-Feedback</span></div>
    <div class="fact rv"><b>VR-Training</b><span>vor virtuellem Publikum</span></div>
    <div class="fact rv"><b>10 bis 14 Plätze</b><span>je Seminar</span></div>
   </div>
   <p class="noladder rv">Kein Stufenmodell. Ein klarer Einstieg, danach eigenständige Formate, die du frei wählst.</p>
   <div class="formats">{f}</div>
   <div class="center" style="margin-top:56px"><div class="cta-row">{btn('seminare')}</div></div>
  </div>
 </div>
</section>'''

def section_call():
    clar = ['wo du heute Wirkung verlierst','welches Seminar zu deiner Situation passt','welcher Ort und welcher Termin für dich gehen']
    li = ''.join(f'<li>{CHECK}<span>{e(x)}</span></li>' for x in clar)
    return f'''
<section class="sec sec--cream" id="gespraech">
 <div class="wrap">
  <div class="center"><p class="ov rv">Dein erster Schritt</p>
  <h2 class="rv" style="margin-top:16px">Erst ein Gespräch. Dann entscheidest du.</h2></div>
  <div class="flow" data-in>
   <div class="flow__line"><i></i></div>
   <div class="fstep rv"><span class="n">1</span><div class="fstep__t"><h3>Termin wählen.</h3><p>Du suchst dir online einen freien Termin aus. Danach bekommst du eine Bestätigung per E-Mail und vor dem Termin eine kurze Erinnerung per WhatsApp.</p></div></div>
   <div class="fstep rv"><span class="n">2</span><div class="fstep__t"><h3>Gespräch per Video.</h3><p>30 Minuten mit Michaels Team. Das Gespräch ist kein Rhetoriktest. Wir klären, wo du stehst und welches Format passt.</p>{fehlt('[von Kunde bestätigen: Name und Rolle der Person im Gespräch]')}
     <p class="clar-h">Im Gespräch klärst du:</p><ul class="clar">{li}</ul>
     <p class="clar-note">Bring gern eine konkrete Situation mit, über die du sprechen willst.</p></div></div>
   <div class="fstep rv"><span class="n">3</span><div class="fstep__t"><h3>In Ruhe entscheiden.</h3><p>Du bekommst Termine und Details zu deinem Seminar. Ob und wann du buchst, entscheidest du danach.</p>
     <div class="cta-row" style="margin-top:22px">{btn('ablauf')}<p class="assure">{CHECK}<span>Kostenlos, per Video. Lieber anrufen: <a href="{TEL}">+49 15888367664</a></span></p></div></div></div>
  </div>
 </div>
</section>'''

def section_voices():
    Q = [
     ('Feedback, das trägt','„Die Redeübungen haben mich definitiv auf ein anderes Level gebracht und Michaels Feedback war unheimlich wertschätzend, klar und unglaublich hilfreich.“','Jenny E.','Google'),
     ('Haltung zuerst','„Ich habe gelernt, meine innere Haltung zum Ausgangspunkt jeder Präsentation zu machen […] Wie ich spreche, wie ich wirke, wie ich wahrgenommen werde.“','Adrian B.','Google'),
     ('Freie Reden vor der Gruppe','„Besonders beeindruckt hat mich der Praxisteil, in dem wir freie Reden vor der Gruppe hielten und sowohl von Michael Ehlers als auch von den anderen Teilnehmern wertvolles Feedback bekamen.“','Michael B.','ProvenExpert'),
     ('Für Anfänger und Profis','„Ich fand es spannend, dass wir Teilnehmer ein Mix von Anfänger bis Profi waren und Michael uns alle, egal auf welchem Level, weiterbringen konnte.“','Christin R.','ProvenExpert'),
     ('Training vor der Kamera','„Die Trainings vor der Kamera mit den darauf folgenden Auswertungen helfen die Selbst- und Fremdwahrnehmung zu schärfen.“','Julian L.','ProvenExpert'),
     ('Auch nach 40 Jahren Medienerfahrung','„Trotz 40 Jahren Medienerfahrung konnte ich erstaunlich viel vom Rhetoriktraining profitieren.“','Peter Escher','Moderator MDR'),
    ]
    q = ''.join(f'<article class="q rv">{STARS if s != "Moderator MDR" else ""}<h3>{e(h)}</h3><blockquote>{e(t)}</blockquote><div class="who"><span>{e(n)}</span><span class="src">{e(s)}</span></div></article>' for h,t,n,s in Q)
    v = ''.join(f'<div class="vid"><img src="assets/v-stimme-{i}.webp" alt="Teilnehmer-Video {i}"><b>{PLAY}</b><span>{d}</span></div>' for i,d in [(1,'1:00'),(2,'1:12'),(3,'1:23')])
    return f'''
<section class="sec" id="stimmen">
 <div class="wrap">
  <div class="stack"><p class="ov rv">Stimmen</p><h2 class="rv">Was Teilnehmer über das Seminar schreiben</h2>
   <p class="lead rv">250 Bewertungen auf ProvenExpert, 227 davon mit 5 Sternen, und 4,8 von 5 bei Google. Sechs Auszüge aus öffentlichen Bewertungen und von der bisherigen Website. Auslassungen innerhalb eines Zitats sind mit […] markiert.</p></div>
  <div class="qgrid">{q}</div>
  <div class="vids rv">{v}</div>
  <p class="vcap center rv">Drei Teilnehmer erzählen im Video, wie sie das Seminar erlebt haben. Jedes Video dauert etwa eine Minute.</p>
  <div class="center" style="margin-top:40px"><div class="cta-row">{btn('stimmen')}</div></div>
 </div>
</section>'''

def section_places():
    P = [
     ('city-mallorca.webp','Mallorca','Frei sprechen','Insel. Klarheit. Umsetzung.','Termine:',['3. bis 6. Dezember 2026','4. bis 7. März 2027','29. April bis 2. Mai 2027','14. bis 17. Oktober 2027']),
     ('city-dubai.webp','Dubai','Mit Sprache führen','Wachstum trifft Wüste.','Termin:',['10. bis 13. Dezember 2026']),
     ('city-barcelona.webp','Barcelona','Ruhig bleiben','Verändere deine Sprache. Verändere deine Wirkung.','Termine:',['15. bis 18. April 2027','21. bis 24. Oktober 2027']),
     ('city-frankfurt.webp','Frankfurt','Frei sprechen','','Termin:',['17. bis 20. Juni 2027']),
     ('city-berlin.webp','Berlin','Frei sprechen','','Termin:',['12. bis 15. August 2027']),
     ('city-zypern.webp','Zypern','Mit Sprache führen','','Termin:',['7. bis 10. Oktober 2027']),
    ]
    c = ''
    for img,name,fm,claim,lab,ds in P:
        cl = f'<p class="claim">{e(claim)}</p>' if claim else ''
        c += f'<article class="place rv"><div class="place__img"><img data-plx src="assets/{img}" alt="Seminarort {name}"></div><div class="place__t"><p class="fmtn">{e(fm)}</p><h3>{name}</h3>{cl}<p class="dates"><b>{lab}</b> {" · ".join(ds)}</p></div></article>'
    return f'''
<section class="sec sec--navy" id="termine">
 <div class="wrap">
  <div class="stack"><p class="ov rv" style="color:var(--sand)">Orte und Termine</p><h2 class="rv" style="color:#fff">Sechs Orte. Die nächsten Termine.</h2>
   <p class="lead rv" style="color:rgba(242,237,228,.85)">Die Seminare finden an Orten statt, die Abstand zum Alltag schaffen. Jeder Termin dauert vier Tage: drei Tage Training und ein Tag Get Together.</p></div>
  <div class="places">{c}</div>
  <p class="stand rv">Den Einstieg gibt es auch in Deutschland: in Frankfurt und in Berlin. Freie Plätze und den passenden Termin klärst du im Gespräch. Stand der Termine: Oktober 2026.</p>
  <div class="cta-row rv" style="margin-top:30px">{btn('termine','btn btn--light')}</div>
 </div>
</section>'''

FAQ = [
 ('Was kostet ein Rhetorik-Seminar bei Michael Ehlers?','Den Preis für dein Seminar nennt dir Michaels Team im kostenlosen Gespräch. Enthalten sind die drei Trainingstage, der Tag Get Together und die Übernachtungen im Seminarzeitraum.'),
 ('Was macht man in einem Rhetorik-Seminar bei Michael Ehlers?','Du sprichst selbst, und zwar viel. Dreimal wirst du auf Video aufgenommen und bekommst sofort Feedback. Im VR-Training sprichst du vor einem virtuellen Publikum. Die Themen hängen vom Seminar ab: im Einstieg zum Beispiel freie Rede und Struktur, in den anderen Formaten Schlagfertigkeit oder die Stegreifrede.'),
 ('Wie lernt man Rhetorik am besten?','Durch Üben mit ehrlichem Feedback. Bücher geben dir das Wissen. Unter Druck hilft dir aber nur, was du geübt hast. Deshalb arbeitet das Seminar mit Reden vor der Gruppe und mit Videoanalyse. Dazu kommt die Rückmeldung von Michael und den anderen Teilnehmern.'),
 ('Ich bin sehr introvertiert. Ist das Seminar trotzdem etwas für mich?','Gerade dann. Rhetorik bedeutet nicht, lauter oder extrovertierter zu sein. Introvertierte überzeugen oft durch Präzision und Ruhe. Mit den richtigen Techniken nutzt du diese Stärken, ohne dich zu verbiegen.'),
 ('Muss ich mich verstellen oder schauspielern?','Nein. Rhetorik heißt, mit deiner eigenen Art Wirkung zu erzielen. Nicht anders werden, klarer werden. Die Technik unterstützt deine Persönlichkeit.'),
 ('Ich habe schon Kommunikationstrainings gemacht. Lerne ich hier noch etwas Neues?','Ja. Auch erfahrene Teilnehmer lernen hier dazu. Emrullah A. schreibt bei Google: „Ich habe in diesem Kurs mehr gelernt als in all meinen bisherigen Schulungen zusammen.“'),
 ('Bin ich als Anfänger richtig?','Ja. In den Gruppen trainieren Anfänger und erfahrene Redner zusammen. Christin R. schreibt auf ProvenExpert, dass Michael alle weiterbringt, egal auf welchem Level.'),
 ('Wie groß sind die Gruppen?','Je nach Seminar 10 bis 14 Plätze. So kommt jeder dran. Kein Zuschauen, kein Verstecken in der letzten Reihe.'),
 ('Sind Übernachtung und Anreise enthalten?','Die Übernachtungen im offiziellen Seminarzeitraum sind enthalten, bei vier Seminartagen sind das drei Nächte. Anreise und Transfer zum Hotel organisierst du selbst.'),
 ('Was ist der Unterschied zwischen Seminar und Online-Kurs?','Im Seminar trainierst du vor Ort in der Gruppe, mit Videoanalyse und persönlichem Feedback. Der Online-Kurs ist ein Selbstlernkurs mit Video-Lektionen. Was zu dir passt, klärst du im Gespräch.'),
 ('Was passiert im kostenlosen Gespräch?','Du sprichst 30 Minuten per Video mit Michaels Team über deine Situation und deine Ziele. Danach weißt du, welches Seminar und welcher Ort zu dir passen. Du entscheidest in Ruhe.'),
 ('Was passiert, wenn ich absagen muss?','Laut AGB kannst du bis 8 Wochen vor Beginn stornieren, gegen eine Stornogebühr von 30 Prozent. Danach ist der volle Preis fällig.'),
]

def section_faq():
    items = ''
    for i,(q,a) in enumerate(FAQ):
        mark = ' ' + fehlt('[FEHLT: Freigabe Übernachtung]') if i == 0 else ''
        items += f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div class="a">{e(a)}{mark}</div></details>'
    return f'''
<section class="sec sec--cream" id="faq">
 <div class="wrap faqgrid">
  <div class="stack" style="position:sticky;top:120px"><p class="ov rv">FAQ</p><h2 class="rv">Häufige Fragen zum Rhetorik-Seminar</h2>
   <p class="morelinks rv">Weitere Antworten findest du in den <a class="tlink" href="https://clients.741.studio/meandyou/v2/faq.html">häufigen Fragen</a>. Wenn du Rhetorik erst kennenlernen willst: <a class="tlink" href="https://clients.741.studio/meandyou/v2/rhetorik.html">Was ist Rhetorik?</a></p></div>
  <div class="acc rv">{items}</div>
 </div>
</section>'''

def section_closer():
    items = ['per Video, von überall','Termin online wählen','Termine auf Mallorca, in Barcelona, in Deutschland und an weiteren Orten']
    li = ''.join(f'<li>{CHECK}<span>{e(x)}</span></li>' for x in items)
    return f'''
<section class="closer" id="abschluss">
 <div class="closer__bg"><img data-plx src="assets/closer-terrace.webp" alt="Abendstimmung auf einer Steinterrasse über dem Meer, Menschen im Gespräch" width="1536" height="1024"></div>
 <div class="wrap"><div class="closer__in">
  <h2 class="rv">Unübersehbar wird man nicht,<br>indem man lauter wird.</h2>
  <p class="rv">Ein Gespräch, 30 Minuten, kostenlos. Wir klären, wo du stehst und welches Format passt. Danach entscheidest du in Ruhe, ob du dabei bist.</p>
  <ul class="rv">{li}</ul>
  <p class="proofline rv">{STARS} 227 von 250 Bewertungen mit 5 Sternen auf ProvenExpert</p>
  <div class="cta-row rv">{btn('abschluss','btn btn--light cta--breathe')}<p class="tel">Lieber anrufen: <a href="{TEL}">+49 15888367664</a></p></div>
 </div></div>
</section>
<footer class="foot">
 <div class="wrap foot__in">
  <div><img src="assets/logo-light.png" alt="Michael Ehlers &amp; You Communication" width="1794" height="647"><p class="addr">Institut Michael Ehlers GmbH<br>Landsknechtstraße 50<br>96103 Hallstadt</p></div>
  <div><h4>Seminare</h4><a href="https://clients.741.studio/meandyou/v2/seminare.html">Seminare</a><a href="#termine">Termine</a><a href="{BOOK}footer">Gespräch buchen</a></div>
  <div><h4>Michael</h4><a href="https://clients.741.studio/meandyou/v2/michael.html">Über Michael</a><a href="https://clients.741.studio/meandyou/v2/rhetorik.html">Was ist Rhetorik</a><a href="https://clients.741.studio/meandyou/v2/faq.html">FAQ</a></div>
  <div><h4>Rechtliches</h4><a href="https://www.meandyou.de/impressum">Impressum</a><a href="https://www.meandyou.de/datenschutz">Datenschutz</a><a href="https://www.meandyou.de/agb">AGB</a></div>
  <div><h4>Kontakt</h4><a href="{TEL}">+49 15888367664</a><a href="mailto:management@meandyou.de">management@meandyou.de</a><a href="https://www.instagram.com/michael_ehlers_rhetorik/">Instagram</a><a href="https://de.linkedin.com/in/rhetoriktrainer">LinkedIn</a></div>
 </div>
</footer>'''

def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="#top"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="https://clients.741.studio/meandyou/v2/seminare.html">Seminare</a><a href="https://clients.741.studio/meandyou/v2/michael.html">Michael</a><a href="https://clients.741.studio/meandyou/v2/rhetorik.html">Was ist Rhetorik</a><a href="#stimmen">Stimmen</a><a href="#faq">FAQ</a></nav>
 {btn('header')}
</div></header>'''

SCHEMA = '''{"@context":"https://schema.org","@graph":[
{"@type":"WebPage","@id":"https://www.meandyou.de/#webpage","url":"https://www.meandyou.de/","name":"Rhetorik-Seminar mit Michael Ehlers | 3 Tage, kleine Gruppe","inLanguage":"de","about":{"@id":"https://www.meandyou.de/#michael"}},
{"@type":"EducationalOrganization","@id":"https://www.meandyou.de/#organization","name":"Institut Michael Ehlers GmbH","alternateName":"me&you Communication","url":"https://www.meandyou.de/","email":"management@meandyou.de","logo":"https://www.meandyou.de/logo.png","address":{"@type":"PostalAddress","streetAddress":"Landsknechtstraße 50","postalCode":"96103","addressLocality":"Hallstadt","addressCountry":"DE"},"sameAs":["https://www.provenexpert.com/de-de/michael-ehlers/"]},
{"@type":"Person","@id":"https://www.meandyou.de/#michael","name":"Michael Ehlers","jobTitle":"Rhetoriktrainer","worksFor":{"@id":"https://www.meandyou.de/#organization"},"url":"https://www.meandyou.de/michael"}''' + ''.join(
 ',\n{"@type":"EducationEvent","name":"Rhetorik-Seminar ' + n + '","startDate":"' + s + '","endDate":"' + t + '","eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode","location":{"@type":"Place","name":"' + n + '","address":"' + n + '"},"organizer":{"@id":"https://www.meandyou.de/#organization"}}'
 for n,s,t in [('Mallorca','2026-12-03','2026-12-06'),('Dubai','2026-12-10','2026-12-13'),('Mallorca','2027-03-04','2027-03-07'),('Barcelona','2027-04-15','2027-04-18'),('Mallorca','2027-04-29','2027-05-02'),('Frankfurt','2027-06-17','2027-06-20'),('Berlin','2027-08-12','2027-08-15'),('Zypern','2027-10-07','2027-10-10'),('Mallorca','2027-10-14','2027-10-17'),('Barcelona','2027-10-21','2027-10-24')]) + ']}'

def page():
    body = header() + '<main>' + section_hero() + section_proof() + section_sits() + section_michael() + section_method() + section_seminars() + section_call() + section_voices() + section_places() + section_faq() + '</main>' + section_closer() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Rhetorik-Seminar mit Michael Ehlers | 3 Tage, kleine Gruppe</title>
<meta name="description" content="Rhetorik-Seminare in kleinen Gruppen auf Mallorca, in Barcelona, Frankfurt und Berlin. Drei Tage mit Videoanalyse. Kostenloses Gespräch buchen.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{SCHEMA}</script>
</head><body>{body}<script>{JS}</script></body></html>'''

if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
