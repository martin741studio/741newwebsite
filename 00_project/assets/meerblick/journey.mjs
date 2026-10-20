// Entwurf B: the Meerblick homepage as one journey, built on the to-top.ch flow model
// exactly as ported for me&you v3 (prototype-v3/build_v3.py): layered hero scene with the
// rising sun as the question button, a thread (SVG) through the whole page, a CSS-3D signpost
// for the early self-selection, three stacking station cards, a taste section, the thread ends
// at the booking button. Lenis for smooth scroll (loaded from jsdelivr, allowed by the artifact CSP).

export function pageB({ img, fonts, draftbar, footer, contact, KONTAKT, SHOP_VIP, SHOP_WEBINAR, FAQ, stations }) {
  const css = `
/* Layout: to-top flow. Brand from the Meerblick logo: sea teal + deep green on a warm sand ground. */
:root{
  --sea:#1FB3A3; --sea-deep:#168C80; --deep:#3B655F; --ink:#1C2826; --muted:#5E6E6B;
  --paper:#FFFFFF; --sand:#F4F1EA; --sand-soft:#ECE6D8; --foam:#E7F6F3; --line:#DCE3E0; --sun:#F2B84B; --wood:#5B4634;
  --font-display:'Outfit','Segoe UI',Helvetica,Arial,sans-serif; --font-body:'Nunito Sans','Segoe UI',Helvetica,Arial,sans-serif; --font-accent:'Fraunces',Georgia,'Times New Roman',serif;
  --hdr:84px; --gut:clamp(20px,4vw,48px); --r:26px;
  --acc:var(--sea-deep);
  color-scheme:light;
}
body[data-persona="website"]{--acc:var(--sea-deep)}
body[data-persona="werbung"]{--acc:var(--sun)}
body[data-persona="lokal"]{--acc:var(--deep)}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font-body);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:var(--sea-deep)}
h1,h2,h3{font-family:var(--font-display);line-height:1.08;letter-spacing:-.015em;margin:0;text-wrap:balance;font-weight:600}
h2{font-size:clamp(1.9rem,min(3.4vw,6vh),2.9rem)}
h3{font-size:clamp(1.2rem,1.8vw,1.5rem)}
p{margin:0}
.wrap{width:100%;max-width:1320px;margin-inline:auto;padding-inline:var(--gut);position:relative;z-index:2;min-width:0}
.ov{font-family:var(--font-display);font-size:.76rem;letter-spacing:.18em;text-transform:uppercase;font-weight:600;color:var(--sea-deep)}
.stack{display:flex;flex-direction:column;gap:clamp(14px,2.2vh,24px);min-width:0}
.stack--tight{gap:clamp(8px,1.3vh,14px)}
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,5vw,84px);align-items:center}
.lead{font-size:clamp(1.02rem,1.3vw,1.2rem);color:var(--muted);max-width:40em}
.lnk{font-family:var(--font-display);font-weight:600;font-size:.92rem;color:var(--sea-deep);text-decoration:none;border-bottom:1.5px solid currentColor;padding-bottom:3px;align-self:flex-start}
.btn{white-space:nowrap;display:inline-flex;align-items:center;gap:.6em;background:var(--deep);color:#fff;font-family:var(--font-display);font-weight:600;font-size:.98rem;padding:.95rem 1.7rem;border-radius:999px;text-decoration:none;border:0;cursor:pointer;transition:background .25s,transform .25s,box-shadow .25s}
.btn:hover{background:var(--sea-deep);transform:translateY(-2px);box-shadow:0 12px 26px rgba(59,101,95,.22)}
.btn--sea{background:var(--sea);color:#0F2F2B}.btn--sea:hover{background:var(--sea-deep);color:#fff}
.btn--light{background:var(--paper);color:var(--deep)}.btn--light:hover{background:var(--sand)}
.btn:focus-visible,a:focus-visible,button:focus-visible{outline:3px solid var(--sun);outline-offset:3px}
.screen{position:relative;min-height:100vh;min-height:100svh;display:grid;align-items:center;padding-block:calc(var(--hdr) + 24px) clamp(36px,6vh,64px)}
.screen--sand{background:var(--sand)}
.screen--foam{background:var(--foam)}
main{position:relative}
/* reveal */
.rv{opacity:0;translate:0 18px;transition:opacity .7s ease,translate .7s ease;transition-delay:calc(var(--d,0) * 90ms)}
.rv[data-d="1"]{--d:1}.rv[data-d="2"]{--d:2}.rv[data-d="3"]{--d:3}
.rv.in{opacity:1;translate:0 0}
/* header: fixed, becomes a capsule on scroll */
.hdr{position:fixed;inset:0 0 auto 0;z-index:50;padding:calc(env(safe-area-inset-top,0px) + 14px) var(--gut) 0;pointer-events:none}
.hdr__in{pointer-events:auto;max-width:1320px;margin-inline:auto;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:8px 8px 8px 16px;border-radius:999px;border:1px solid transparent;transition:max-width .5s,background .4s,box-shadow .4s,border-color .4s}
.hdr.is-pill .hdr__in{max-width:860px;background:rgba(255,255,255,.86);backdrop-filter:blur(14px) saturate(1.2);-webkit-backdrop-filter:blur(14px) saturate(1.2);border-color:var(--line);box-shadow:0 10px 40px -18px rgba(28,40,38,.35)}
.hdr__logo img{height:40px;width:auto}
.hdr__nav{display:flex;gap:22px;font-family:var(--font-display);font-weight:500;font-size:.92rem}
.hdr__nav a{color:var(--ink);text-decoration:none;opacity:.85}.hdr__nav a:hover{opacity:1;color:var(--sea-deep)}
.hdr .btn{padding:.7rem 1.2rem;font-size:.9rem}
@media (max-width:980px){.hdr__nav{display:none}}
/* the thread */
#thread{position:absolute;left:0;top:0;width:100%;height:100%;z-index:1;pointer-events:none;overflow:visible}
#thread path{fill:none;stroke-linecap:round;stroke-linejoin:round;transition:stroke .6s}
#thread .t-n{stroke:var(--acc)}
#thread .t-l{stroke:var(--sun)}
.tend{display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--sun);margin-left:26px;vertical-align:middle;box-shadow:0 0 0 7px rgba(242,184,75,.25)}
/* hero after the to-top model: giant type, layered sea view, the sun rises between the layers */
.jhero{position:relative;overflow:hidden;background:linear-gradient(180deg,var(--paper) 0%,#F7F4EC 30%,#EAF4F1 58%,#D7EEE9 100%)}
.jhero__type{pointer-events:none;padding-top:calc(var(--hdr) + clamp(30px,8vh,90px));text-align:center;display:flex;flex-direction:column;align-items:center;gap:clamp(8px,1.6vh,16px);position:relative;z-index:6}
.jhero h1{font-size:clamp(40px,min(8vw,15vh),140px);line-height:.98;letter-spacing:-.025em}
.jhero h1 span{display:block}
.jhero h1 span + span{color:var(--sea-deep);font-size:.6em;line-height:1.1;letter-spacing:-.015em}
.jhero__sub{font-family:var(--font-accent);font-style:italic;font-size:clamp(18px,min(2vw,3.6vh),30px);line-height:1.2;color:#B8873A}
.jhero__body{max-width:36em;color:var(--muted)}
.jhero__scene{position:relative;width:100%;aspect-ratio:3/2;margin-top:-18vw;pointer-events:none}
.lay{position:absolute;left:0;bottom:0;width:100%;height:auto;will-change:transform;pointer-events:none;user-select:none}
.lay--3{z-index:1;bottom:16%}.lay--2{z-index:3;bottom:5%}.lay--1{z-index:4;bottom:-4%}
.jhero__glow{position:absolute;left:50%;top:54%;width:70vw;aspect-ratio:1;translate:-50% -50%;border-radius:50%;background:radial-gradient(circle,rgba(255,236,190,.95) 0%,rgba(255,226,170,.5) 28%,rgba(255,226,170,0) 62%);z-index:0;will-change:transform}
.sun{position:absolute;left:50%;top:40%;z-index:2;width:clamp(120px,15.5vw,230px);aspect-ratio:1;margin-left:calc(clamp(120px,15.5vw,230px) / -2);border-radius:50%;display:grid;place-items:center;text-align:center;text-decoration:none;pointer-events:auto;background:radial-gradient(circle at 34% 30%,#FBE7B4 0%,#F0C877 55%,#E3B15A 100%);color:var(--deep);box-shadow:0 0 0 14px rgba(246,214,150,.28),0 0 90px 30px rgba(246,206,130,.55);will-change:transform;transition:box-shadow .4s}
.sun:hover{box-shadow:0 0 0 20px rgba(246,214,150,.34),0 0 120px 44px rgba(246,206,130,.7)}
.sun span{display:block;rotate:-12deg;font-family:var(--font-display);font-weight:700;font-size:clamp(10.5px,1.02vw,15px);line-height:1.3;letter-spacing:.12em;text-transform:uppercase;max-width:9.5em}
.jhero__fade{position:absolute;left:0;right:0;bottom:-2px;height:22%;z-index:5;background:linear-gradient(180deg,rgba(255,255,255,0) 0%,rgba(255,255,255,.86) 62%,var(--paper) 100%)}
.jhero__known{position:relative;z-index:6;margin-top:clamp(-110px,-9vh,-50px);padding-bottom:clamp(26px,5vh,54px);display:flex;justify-content:center}
.known{display:flex;align-items:center;gap:clamp(14px,2vw,30px);flex-wrap:wrap;justify-content:center;font-family:var(--font-display);font-weight:500;color:var(--muted);font-size:.95rem}
.known span + span::before{content:"·";margin-right:clamp(14px,2vw,30px);opacity:.5}
/* signpost */
.wegw{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:clamp(24px,5vw,80px);align-items:center}
.hint{font-size:.95rem;color:var(--muted)}
.post{position:relative;height:min(64svh,600px);perspective:1400px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:clamp(12px,2.4vh,24px)}
.post__pole{z-index:0;transform:translateZ(-90px);position:absolute;left:50%;top:0;bottom:0;width:12px;margin-left:-6px;border-radius:6px;background:linear-gradient(90deg,#3f3129 0%,#7a6453 45%,#3f3129 100%);box-shadow:0 30px 40px -18px rgba(28,40,38,.5)}
.post__pole::after{content:"";position:absolute;left:50%;top:-10px;width:22px;height:22px;margin-left:-11px;border-radius:50%;background:#4a3b31}
.sign{position:relative;z-index:1;border:0;cursor:pointer;width:min(74%,380px);padding:clamp(14px,2.6vh,24px) clamp(22px,2.6vw,40px);background:var(--t-bg);color:var(--t-fg);font-family:var(--font-display);font-weight:600;font-size:clamp(19px,min(2.1vw,3.8vh),30px);line-height:1.12;text-align:left;display:flex;flex-direction:column;gap:6px;box-shadow:0 24px 40px -22px rgba(28,40,38,.6);transition:transform .6s cubic-bezier(.2,.7,.2,1),filter .4s,opacity .4s;will-change:transform}
.sign small{font-family:var(--font-body);font-weight:600;font-size:11px;letter-spacing:.18em;opacity:.7}
.sign--l{margin-right:22%;clip-path:polygon(9% 0,100% 0,100% 100%,9% 100%,0 50%);padding-left:clamp(38px,4vw,62px);transform:rotateY(calc(14deg + var(--sway,0deg))) translateZ(8px)}
.sign--r{margin-left:22%;clip-path:polygon(0 0,91% 0,100% 50%,91% 100%,0 100%);padding-right:clamp(38px,4vw,62px);transform:rotateY(calc(-14deg + var(--sway,0deg))) translateZ(8px)}
.sign:hover{transform:rotateY(var(--sway,0deg)) translateZ(26px)}
.post.has-choice .sign:not(.is-on){opacity:.5;filter:saturate(.5)}
.sign.is-on{transform:rotateY(var(--sway,0deg)) translateZ(34px) scale(1.04)}
.post .tangle-slot{position:absolute;left:-6%;top:6%;width:42%;height:34%;z-index:0}
.t-website{--t-bg:var(--foam);--t-fg:var(--ink);--t-accent:var(--sea-deep)}
.t-werbung{--t-bg:#FBE9C6;--t-fg:var(--ink);--t-accent:#9A6A17}
.t-lokal{--t-bg:var(--deep);--t-fg:#fff;--t-accent:#9FE3D8}
/* the three situations as the choice */
.sits{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,22px)}
.sit{border-radius:var(--r);overflow:hidden;display:grid;grid-template-rows:minmax(0,1fr) auto;height:min(60svh,600px);background:var(--t-bg);color:var(--t-fg);text-decoration:none;cursor:pointer;border:0;text-align:left;font:inherit;padding:0;position:relative;transition:opacity .45s,translate .45s,box-shadow .45s,filter .45s}
.sit__img{position:relative;overflow:hidden;min-height:0}
.sit__img img{width:100%;height:118%;margin-top:-9%;object-fit:cover;will-change:transform}
.sit__txt{padding:clamp(16px,2.4vh,26px) clamp(18px,1.8vw,28px);display:flex;flex-direction:column;gap:clamp(8px,1.2vh,12px)}
.sit h3{color:var(--t-fg);font-size:clamp(18px,min(1.65vw,3vh),25px)}
.sit p{font-size:.95rem;color:var(--t-fg);opacity:.86}
.sit .lnk{color:var(--t-accent)}
.sits.has-choice .sit:not(.is-on){opacity:.46;filter:saturate(.55)}
.sit.is-on{translate:0 -8px;box-shadow:0 30px 60px -34px rgba(28,40,38,.75)}
.sit__check{position:absolute;right:14px;top:14px;z-index:2;width:34px;height:34px;border-radius:50%;background:var(--paper);display:grid;place-items:center;opacity:0;scale:.6;transition:opacity .3s,scale .3s}
.sit.is-on .sit__check{opacity:1;scale:1}
.sit__check svg{width:18px;height:18px;stroke:var(--deep);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
/* route: three station cards that stack while you scroll */
.flow{position:relative;padding-block:calc(var(--hdr) + 24px) clamp(50px,9vh,100px);background:var(--sand)}
.mhead{max-width:44em;margin-bottom:clamp(22px,5vh,46px)}
.mcard{position:sticky;top:calc(var(--hdr) + 14px + var(--i) * 22px);height:min(66svh,640px);border-radius:28px;overflow:hidden;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);margin-bottom:clamp(22px,5vh,48px);background:var(--c-bg);color:var(--c-fg);box-shadow:0 -22px 60px -36px rgba(28,40,38,.55)}
.mcard__txt{padding:clamp(22px,5vh,54px) clamp(24px,4vw,64px);display:flex;flex-direction:column;justify-content:space-between;min-width:0;gap:14px}
.mcard i{font-family:var(--font-accent);font-style:normal;font-size:clamp(70px,min(10vw,18vh),160px);line-height:.9;color:var(--c-fg);opacity:.2}
.mcard h3{font-size:clamp(26px,min(3.2vw,5.8vh),52px);color:var(--c-fg)}
.mcard p{color:var(--c-fg);opacity:.88;margin-top:8px;max-width:26em}
.mcard ul{list-style:none;margin:10px 0 0;padding:0;display:grid;gap:6px;font-size:.95rem;opacity:.92}
.mcard li::before{content:"\\2713";margin-right:10px;color:var(--c-acc)}
.mcard__tag{display:none;background:var(--sun);color:#2A2412;font-family:var(--font-display);font-weight:600;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;padding:.4rem .8rem;border-radius:999px;width:max-content}
.mcard.is-rec .mcard__tag{display:inline-block}
.mcard__img{position:relative;overflow:hidden;min-height:0}
.mcard__img img{width:100%;height:100%;object-fit:cover}
.mcard--1{--c-bg:var(--foam);--c-fg:var(--ink);--c-acc:var(--sea-deep)}
.mcard--2{--c-bg:#FBE9C6;--c-fg:var(--ink);--c-acc:#9A6A17}
.mcard--3{--c-bg:var(--deep);--c-fg:#fff;--c-acc:#9FE3D8}
/* the pilot */
.poster{position:relative;height:min(66svh,660px);border-radius:var(--r);overflow:hidden;background:var(--deep)}
.poster img{width:100%;height:118%;margin-top:-9%;object-fit:cover;will-change:transform}
.quote{font-family:var(--font-accent);font-style:italic;font-size:clamp(1.25rem,2.1vw,1.7rem);line-height:1.35;color:var(--deep)}
.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(10px,1.6vw,24px);border-block:1px solid var(--line);padding-block:clamp(10px,2vh,20px)}
.stats b{display:block;font-family:var(--font-display);font-weight:600;font-size:clamp(19px,min(1.9vw,3.4vh),30px);line-height:1.15;color:var(--ink)}
.stats span{font-size:.9rem;color:var(--muted)}
/* arrival: full bleed */
.bleed{padding:0;align-items:stretch;color:#fff;overflow:hidden;background:var(--deep)}
.bleed__bg{position:absolute;inset:0}
.bleed__bg img{width:100%;height:116%;margin-top:-8%;object-fit:cover;will-change:transform}
.bleed__bg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,47,43,.84) 0%,rgba(15,47,43,.5) 45%,rgba(15,47,43,.12) 100%)}
.bleed__in{position:relative;display:grid;align-items:end;padding-block:calc(var(--hdr) + 24px) clamp(40px,9vh,96px)}
.bleed .ov{color:#9FE3D8}
.bleed h2{color:#fff;font-size:clamp(2rem,min(4vw,7vh),3.6rem);max-width:16ch}
.bleed p{max-width:34em;color:rgba(255,255,255,.9)}
/* taste */
.taste{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.5vw,20px);margin-top:clamp(16px,3vh,30px)}
.tcard{position:relative;background:var(--paper);border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column;text-decoration:none;color:inherit;transition:translate .35s,box-shadow .35s;outline:2px solid transparent;outline-offset:-2px;border:1px solid var(--line)}
.tcard:hover{translate:0 -5px;box-shadow:0 26px 50px -34px rgba(28,40,38,.7)}
.tcard__img{height:clamp(130px,25vh,240px);background:var(--sand-soft);overflow:hidden;position:relative}
.tcard__img img{width:100%;height:100%;object-fit:cover}
.tcard__txt{padding:clamp(14px,2.4vh,22px) clamp(16px,1.5vw,22px) clamp(16px,2.6vh,24px);display:flex;flex-direction:column;gap:8px;flex:1}
.tcard small{font-family:var(--font-display);font-weight:600;font-size:11px;letter-spacing:.18em;color:var(--sea-deep);text-transform:uppercase}
.tcard p{font-size:.95rem;color:var(--muted);flex:1}
.tcard .lnk{margin-top:6px}
.tcard__rec{position:absolute;left:12px;top:12px;z-index:2;background:var(--sun);color:#2A2412;font-family:var(--font-display);font-weight:600;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;padding:8px 11px;border-radius:999px;opacity:0;transition:opacity .4s}
.tcard.is-rec{outline-color:var(--sun)}
.tcard.is-rec .tcard__rec{opacity:1}
/* closing: where the thread ends */
.closing{position:relative;background:var(--deep);color:#fff;padding-block:clamp(70px,12vh,140px) clamp(50px,8vh,90px);overflow:hidden}
.closing h2{color:#fff;font-size:clamp(2rem,min(4.2vw,7.4vh),3.8rem);max-width:18ch}
.closing p{max-width:34em;color:rgba(255,255,255,.88)}
.closing .ov{color:#9FE3D8}
.float{position:fixed;right:18px;bottom:calc(18px + env(safe-area-inset-bottom,0px));z-index:48;box-shadow:0 14px 30px rgba(28,40,38,.3)}
.draft{position:fixed;left:50%;translate:-50% 0;bottom:calc(env(safe-area-inset-bottom,0px) + 14px);z-index:60;background:var(--ink);color:#fff;font-family:var(--font-display);font-size:12px;line-height:1.3;padding:10px 16px;border-radius:999px;text-align:center;max-width:calc(100% - 32px)}
.draft a{color:#9FE3D8;text-decoration:none}
/* contact + footer (shared look) */
.contact{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:start}
.contact dl{display:grid;grid-template-columns:auto 1fr;gap:10px 18px;margin:0}
.contact dt{color:var(--muted);font-size:.9rem}.contact dd{margin:0;font-weight:600}.contact dd a{text-decoration:none;color:var(--ink)}
.card{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:28px;min-width:0}
.eyebrow{display:inline-block;font-family:var(--font-display);font-size:.78rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--sea-deep);margin-bottom:14px}
.section{padding-block:clamp(64px,9vw,120px)}.section--sand{background:var(--sand)}
.btn--ghost{background:transparent;color:var(--deep);border:1.5px solid var(--deep)}.btn--ghost:hover{background:var(--deep);color:#fff}
.ftr{background:var(--ink);color:#B9CBC7;padding-block:40px;font-size:.9rem}
.ftr__in{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;align-items:center}
.ftr a{color:#DDEBE8;text-decoration:none}
.ftr img{height:34px;width:auto;filter:brightness(0) invert(1);opacity:.9}
@media (max-width:980px){
  .jhero h1{font-size:clamp(34px,11vw,64px)}
  .jhero__scene{aspect-ratio:1/1.04;margin-top:-4vw}
  .lay{width:172%;max-width:none;left:-64%}
  .sun{top:27%}
  .jhero__glow{top:42%;width:120vw}
  .jhero__fade{height:14%}
  .lay--1{bottom:0}
  .jhero__known{margin-top:0;padding-top:10px;background:var(--paper)}
  .wegw{grid-template-columns:minmax(0,1fr)}
  .post{height:auto;padding-block:26px}
  .sign{width:82%}
  #thread{display:none}
  .tangle-slot{display:none}
  .sits{grid-template-columns:minmax(0,1fr)}
  .sit{height:auto}
  .sit__img{aspect-ratio:16/9}
  .mcard{position:relative;top:auto;height:auto;grid-template-columns:minmax(0,1fr)}
  .mcard__img{aspect-ratio:16/10}
  .taste{grid-template-columns:minmax(0,1fr)}
  .split{grid-template-columns:minmax(0,1fr)}
  .poster{height:min(50svh,420px)}
  .contact{grid-template-columns:1fr}
  .stats{grid-template-columns:1fr 1fr}
  .screen{min-height:0}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}.rv{opacity:1;translate:0 0}}
`;

  // The sea view, drawn as three SVG layers (no alpha photos exist for Meerblick): far shore, lighthouse spit, pier.
  const layFar = `<svg class="lay lay--3" id="lay3" viewBox="0 0 2000 700" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="g3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3B655F" stop-opacity=".55"/><stop offset="1" stop-color="#3B655F" stop-opacity=".9"/></linearGradient></defs><path fill="url(#g3)" d="M0 520 C120 500 220 470 360 486 C470 498 520 470 640 476 C760 482 820 506 940 494 C1060 482 1120 450 1240 462 C1360 474 1420 500 1540 490 C1680 478 1760 450 1860 470 C1920 482 1960 496 2000 500 L2000 700 L0 700 Z"/><path fill="#3B655F" opacity=".35" d="M0 560 C300 540 600 548 1000 540 C1400 532 1700 548 2000 540 L2000 700 L0 700 Z"/></svg>`;
  const layMid = `<svg class="lay lay--2" id="lay2" viewBox="0 0 2000 700" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1FB3A3" stop-opacity=".55"/><stop offset="1" stop-color="#168C80" stop-opacity=".95"/></linearGradient></defs><path fill="url(#g2)" d="M0 470 C200 462 400 478 600 468 C800 458 1000 476 1200 466 C1400 456 1600 474 2000 462 L2000 700 L0 700 Z"/><g transform="translate(1380 300)"><path fill="#1C2826" d="M0 150 C40 140 90 146 130 150 L130 180 L0 180 Z"/><path fill="#F4F1EA" d="M48 40 L82 40 L90 150 L40 150 Z"/><path fill="#1C2826" d="M48 40 L82 40 L82 56 L48 56 Z M44 110 L86 110 L86 124 L44 124 Z"/><path fill="#F2B84B" d="M52 14 L78 14 L82 40 L48 40 Z"/><path fill="#1C2826" d="M52 14 L78 14 L80 24 L50 24 Z"/><circle cx="65" cy="6" r="6" fill="#F2B84B"/></g></svg>`;
  const layFront = `<svg class="lay lay--1" id="lay1" viewBox="0 0 2000 700" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#168C80" stop-opacity=".92"/><stop offset="1" stop-color="#0F4F48"/></linearGradient></defs><path fill="url(#g1)" d="M0 420 C250 408 500 430 750 418 C1000 406 1250 428 1500 416 C1750 404 1900 420 2000 414 L2000 700 L0 700 Z"/><path fill="#fff" opacity=".12" d="M0 470 C300 460 600 476 900 466 C1200 456 1500 472 2000 462 L2000 478 C1500 488 1200 472 900 482 C600 492 300 476 0 486 Z"/><g fill="#5B4634"><path d="M120 700 L430 700 L720 520 L560 520 Z" opacity=".95"/><path d="M160 700 L190 700 L300 560 L285 560 Z M330 700 L360 700 L470 560 L455 560 Z M520 700 L548 700 L640 560 L626 560 Z" opacity=".8"/></g><path fill="#7A6453" d="M560 520 L720 520 L722 532 L556 532 Z"/></svg>`;

  const CHECK = '<span class="sit__check" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m5 12.500 4.500 4.500L19 7.500"/></svg></span>';
  const sitData = [
    { key: 'website', photo: 'laptop-start', alt: 'Laptop mit dem Schriftzug Just Start', h: 'Meine Website arbeitet nicht für mich.', p: 'Sie steht seit Jahren, sieht aus wie viele andere, und niemand ruft deswegen an. Du schickst Leute lieber auf Instagram als auf deine eigene Seite.', pos: '50% 50%' },
    { key: 'werbung', photo: 'unternehmer-erfolg', alt: 'Arbeitsplatz mit Blick in eine weite Landschaft', h: 'Ich habe Besucher, aber keine Anfragen.', p: 'Empfehlungen tragen dich. Aber du willst nicht mehr vom Zufall abhängen und weißt nicht, was eine Anfrage dich kosten darf.', pos: '50% 40%' },
    { key: 'lokal', photo: 'meer-steg', alt: 'Steg am Zwischenahner Meer', h: 'In meiner Region findet mich niemand.', p: 'Bei Google stehen drei Mitbewerber vor dir, obwohl du der Bessere bist. Dein Google-Profil hat vier Bewertungen und ein altes Foto.', pos: '50% 60%' }
  ];
  const sits = sitData.map((s, i) => `<div class="sit t-${s.key} rv" data-d="${i}" role="button" tabindex="0" aria-pressed="false" data-persona="${s.key}">${CHECK}<div class="sit__img"><img data-plx="${i === 1 ? '0.11' : '0.05'}" style="object-position:${s.pos}" src="${img[s.photo]}" alt="${s.alt}" width="1200" height="800"></div><div class="sit__txt"><h3>${s.h}</h3><p>${s.p}</p><a class="lnk" href="#st-${s.key}">Zur Station →</a></div></div>`).join('');

  const mcards = stations.map((s, i) => `<article class="mcard mcard--${i + 1}" style="--i:${i}" id="st-${s.key}" data-persona="${s.key}"><div class="mcard__txt"><div><span class="mcard__tag">Dein Einstieg</span><i>0${i + 1}</i></div><div><h3>${s.name}</h3><p>${s.h}</p><ul>${s.li.slice(0, 3).map((l) => `<li>${l}</li>`).join('')}</ul></div></div><div class="mcard__img"><img src="${img[s.photo]}" alt="${s.alt}" width="1200" height="800" loading="lazy"></div></article>`).join('');

  const taste = [
    ['01', 'vip', '30 Minuten', 'VIP-Gespräch', 'Wir schauen gemeinsam auf deine Seite und dein Google-Profil. Du gehst mit konkreten Punkten raus, egal ob wir danach zusammenarbeiten.', 'Gespräch buchen', SHOP_VIP, 'kds-neu', 'Klaus-Dieter Sachs im Porträt'],
    ['02', 'webinar', '90 Minuten live', 'Webinar: Homepage leicht gemacht', 'Klaus-Dieter zeigt dir live, wie du deine Seite selbst pflegst und Änderungen einbringst.', 'Zum Webinar', SHOP_WEBINAR, 'laptop-start', 'Laptop auf einem Schreibtisch'],
    ['03', 'tipps', 'Zum Lesen', 'Tipps aus der Praxis', 'Antworten auf die Fragen, die Unternehmer ihm seit Jahren stellen: Vom Besucher zum Fan, Leuchtturm deiner Marke, Business mit Leidenschaft.', 'Zu den Tipps', FAQ, 'tuer-change', 'Holzschild mit dem Wort Change an einer grünen Tür']
  ].map(([num, step, small, h, p, link, href, photo, alt]) => `<a class="tcard rv" data-step="${step}" href="${href}"><span class="tcard__rec">Dein Einstieg</span><div class="tcard__img"><img src="${img[photo]}" alt="${alt}" width="1200" height="800" loading="lazy"></div><div class="tcard__txt"><small>${num} · ${small}</small><h3>${h}</h3><p>${p}</p><span class="lnk">${link} →</span></div></a>`).join('');

  const html = `<title>Agentur Meerblick Journey</title>${fonts}<style>${css}</style>
<header class="hdr" id="hdr"><div class="hdr__in">
  <a class="hdr__logo" href="#top" aria-label="Agentur Meerblick"><img src="${img.logo}" alt="Agentur Meerblick: Mehr Sichtbarkeit für dein Business" width="900" height="245"></a>
  <nav class="hdr__nav" aria-label="Hauptnavigation"><a href="#wegweiser">Wo stehst du?</a><a href="#route">Die Route</a><a href="#lotse">Der Lotse</a><a href="#kostprobe">Kostprobe</a><a href="#kontakt">Kontakt</a></nav>
  <a class="btn" href="${KONTAKT}">Gespräch buchen</a>
</div></header>
<main id="top"><svg id="thread" aria-hidden="true"></svg>
<section class="jhero" id="hero">
  <div class="wrap jhero__type">
    <p class="ov rv">Agentur Meerblick · Bad Zwischenahn</p>
    <h1 class="rv" data-d="1"><span>Mehr Sichtbarkeit</span><span>für dein Business.</span></h1>
    <p class="jhero__sub rv" data-d="2">Website. Werbung. Gefunden werden.</p>
    <p class="jhero__body rv" data-d="2">Vom ersten Gespräch bis zu dem Tag, an dem Kunden dich finden, ohne dass du sie suchen musst. Eine Reise in drei Stationen, mit einem Lotsen an deiner Seite.</p>
  </div>
  <div class="jhero__scene" id="scene">
    <div class="jhero__glow" id="glow"></div>
    ${layFar}
    <a class="sun" id="qbtn" href="#wegweiser"><span>Wo stehst du gerade?</span></a>
    ${layMid}
    ${layFront}
    <div class="jhero__fade"></div>
  </div>
  <div class="wrap jhero__known"><div class="known rv" data-d="3"><span>Seit 2018</span><span>Praxen, Coaches, Selbstständige</span><span>Ammerland, Oldenburg, Westerstede</span></div></div>
</section>

<section class="screen" id="wegweiser"><div class="wrap wegw">
  <div class="stack stack--tight wegw__head"><p class="ov rv">Der Wegweiser</p><h2 class="rv" data-d="1">Drei Situationen.<br>Ein gemeinsamer Punkt.</h2>
  <p class="hint rv" data-d="2">Welche kennst du? Wähle eine aus. Die Route zeigt dir dann, wo deine Reise beginnt.</p></div>
  <div class="post rv" data-d="1" id="post"><div class="tangle-slot" aria-hidden="true"></div><span class="post__pole" aria-hidden="true"></span>
    <button class="sign sign--l t-website" type="button" data-persona="website" aria-pressed="false"><small>01</small>Die Website arbeitet nicht</button>
    <button class="sign sign--r t-werbung" type="button" data-persona="werbung" aria-pressed="false"><small>02</small>Besucher, keine Anfragen</button>
    <button class="sign sign--l t-lokal" type="button" data-persona="lokal" aria-pressed="false"><small>03</small>Lokal nicht gefunden</button>
  </div>
</div></section>

<section class="screen" id="situationen"><div class="wrap"><div class="sits">${sits}</div></div></section>

<section class="flow" id="route"><div class="wrap">
  <div class="mhead stack"><p class="ov rv">Die Route</p><h2 class="rv" data-d="1">Drei Stationen vom Steg<br>zum Leuchtturm.</h2>
  <p class="rv lead" data-d="2">Jede Station baut auf der vorherigen auf. Du musst nicht alle gehen. Aber die Reihenfolge ist kein Zufall: Werbung und Google Maps sind nur so gut wie die Seite, auf der die Menschen landen.</p></div>
  ${mcards}
</div></section>

<section class="screen screen--foam" id="lotse"><div class="wrap split">
  <div class="stack"><p class="ov rv">Der Lotse</p><h2 class="rv" data-d="1">Klaus-Dieter Sachs.<br>Der Blickwinkelveränderer.</h2>
    <div class="stats rv" data-d="2"><div><b>Seit 2018</b><span>Websites für Praxen und Coaches</span></div><div><b>30+ Jahre</b><span>Motto: Verändere deinen Blickwinkel</span></div><div><b>1 Ansprechpartner</b><span>vom Gespräch bis nach dem Start</span></div></div>
    <p class="quote rv" data-d="2">„Ich verhelfe Menschen mit beneidenswertem Können auf ihren eigenen Weg in die Sichtbarkeit. Mit Herz und großem Verständnis, durch den ganzen Prozess und darüber hinaus."</p>
    <p class="rv lead" data-d="3">Erst Führungskraft, dann Lebensberater und Coach, seit 2018 Webdesigner. Technik, Werbung und Google Maps laufen im Team im Hintergrund. Dein Ansprechpartner bleibt immer derselbe.</p>
    <div class="rv" data-d="3"><a class="btn btn--ghost" href="${KONTAKT}">Mit Klaus-Dieter sprechen</a></div>
  </div>
  <div class="poster rv" data-d="1" data-plx="0.08"><img style="object-position:50% 20%" src="${img.kds}" alt="Klaus-Dieter Sachs, Agentur Meerblick, im Grünen" width="1200" height="800" loading="lazy"></div>
</div></section>

<section class="screen bleed" id="ankunft"><div class="bleed__bg"><img data-plx="0.07" style="object-position:50% 45%" src="${img.leuchtturm}" alt="Leuchtturm in der blauen Stunde, ein Weg führt über die Felsen hin" width="1200" height="800" loading="lazy"></div>
  <div class="wrap bleed__in"><div class="stack"><p class="ov rv">Die Ankunft</p><h2 class="rv" data-d="1">Dein Leuchtturm steht. Jetzt müssen ihn nur noch die Richtigen sehen.</h2>
  <p class="rv" data-d="2">Eine Seite, die du gern zeigst. Anfragen, deren Kosten du kennst. Ein Google-Profil, das in deiner Region vorne steht. Das ist das Ziel der Reise.</p>
  <div class="rv" data-d="3"><a class="btn btn--light" href="#kostprobe">Erst eine Kostprobe &darr;</a></div></div></div>
</section>

<section class="screen screen--sand" id="kostprobe"><div class="wrap">
  <div class="stack stack--tight"><p class="ov rv">Kostprobe</p><h2 class="rv" data-d="1">Erst ausprobieren.<br>Dann entscheiden.</h2>
  <p class="rv lead" data-d="2">Drei kleine Schritte, bevor du einen großen gehst.</p></div>
  <div class="taste">${taste}</div>
</div></section>

<section class="closing" id="gespraech"><div class="wrap"><div class="stack">
  <p class="ov rv">Das Gespräch</p>
  <h2 class="rv" data-d="1">Jede Reise beginnt mit einem Gespräch.</h2>
  <p class="rv" data-d="2">30 Minuten, kein Verkaufsdruck. Am Ende weißt du, ob es passt und wo dein schnellster Hebel liegt. Wenn nicht, auch gut.</p>
  <div class="rv" data-d="3"><a class="btn btn--sea" href="${KONTAKT}">Gespräch buchen</a><span class="tend" id="thread-end" aria-hidden="true"></span></div>
</div></div></section>

${contact('Lass uns miteinander reden', 'Schreib, ruf an oder buche direkt einen Termin. Klaus-Dieter antwortet persönlich.')}
</main>
${footer}
<a class="btn btn--sea float" href="${KONTAKT}">Gespräch buchen</a>
${draftbar}
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.20/dist/lenis.min.js"></script>
<script>
(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function desktop(){ return window.innerWidth > 980; }
  /* header capsule */
  var hdr = document.getElementById('hdr');
  function onScrollY(y){ if(hdr) hdr.classList.toggle('is-pill', y > 60); }
  /* reveal */
  var rvs = [].slice.call(document.querySelectorAll('.rv'));
  if(reduce || !('IntersectionObserver' in window)){ rvs.forEach(function(el){ el.classList.add('in'); }); }
  else { var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); }, {rootMargin:'0px 0px -8% 0px', threshold:0.05}); rvs.forEach(function(el){ io.observe(el); }); }
  /* parallax */
  var plx = [].slice.call(document.querySelectorAll('[data-plx]')).map(function(el){ return {box: el, img: el.tagName === 'IMG' ? el : el.querySelector('img'), f: parseFloat(el.getAttribute('data-plx')), on: false}; });
  function plxUpdate(){ if(reduce || !desktop()){ plx.forEach(function(p){ p.img.style.transform = ''; }); return; } var vh = window.innerHeight; plx.forEach(function(p){ if(!p.on) return; var r = (p.box === p.img ? p.img.parentElement : p.box).getBoundingClientRect(); p.img.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - vh / 2) * p.f).toFixed(1) + 'px,0)'; }); }
  if('IntersectionObserver' in window){ var pio = new IntersectionObserver(function(es){ es.forEach(function(e){ var p = plx.filter(function(x){ return x.box === e.target; })[0]; if(p){ p.on = e.isIntersecting; } }); plxUpdate(); }, {rootMargin:'20% 0px'}); plx.forEach(function(p){ pio.observe(p.box); }); }
  /* smooth scroll */
  var lenis = null;
  if(!reduce && window.Lenis){ try{ lenis = new window.Lenis({duration:1.1, easing:function(t){ return Math.min(1, 1.001 - Math.pow(2, -10 * t)); }, smoothWheel:true}); lenis.on('scroll', function(e){ onScrollY(e.scroll); plxUpdate(); }); var raf = function(t){ lenis.raf(t); requestAnimationFrame(raf); }; requestAnimationFrame(raf); }catch(err){ lenis = null; } }
  if(!lenis){ window.addEventListener('scroll', function(){ onScrollY(window.scrollY); plxUpdate(); }, {passive:true}); }
  window.addEventListener('resize', plxUpdate); onScrollY(window.scrollY);
  /* anchors through Lenis */
  document.addEventListener('click', function(e){ var a = e.target.closest && e.target.closest('a[href^="#"]'); if(!a) return; var t = document.querySelector(a.getAttribute('href')); if(!t) return; e.preventDefault(); if(lenis){ lenis.scrollTo(t, {offset:-20}); } else { t.scrollIntoView({behavior: reduce ? 'auto' : 'smooth'}); } });

  /* ---- the choice: one situation, remembered for this visit ---- */
  var sits = [].slice.call(document.querySelectorAll('.sit[data-persona]'));
  var signs = [].slice.call(document.querySelectorAll('.sign[data-persona]')), post = document.getElementById('post');
  var box = document.querySelector('.sits');
  var REC = {website:'webinar', werbung:'vip', lokal:'vip'};
  function choose(p, store){
    sits.forEach(function(s){ var on = s.getAttribute('data-persona') === p; s.classList.toggle('is-on', on); s.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    signs.forEach(function(g){ var on = g.getAttribute('data-persona') === p; g.classList.toggle('is-on', on); g.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    if(post) post.classList.toggle('has-choice', !!p);
    if(box) box.classList.toggle('has-choice', !!p);
    if(p){ document.body.setAttribute('data-persona', p); } else { document.body.removeAttribute('data-persona'); }
    [].slice.call(document.querySelectorAll('.mcard[data-persona]')).forEach(function(m){ m.classList.toggle('is-rec', m.getAttribute('data-persona') === p); });
    [].slice.call(document.querySelectorAll('.tcard')).forEach(function(t){ t.classList.toggle('is-rec', !!p && t.getAttribute('data-step') === REC[p]); });
    if(store){ try{ if(p){ sessionStorage.setItem('mb-persona', p); } else { sessionStorage.removeItem('mb-persona'); } }catch(e){} }
  }
  sits.forEach(function(s){ function pick(e){ if(e.target.closest && e.target.closest('a')) return; var p = s.getAttribute('data-persona'); choose(s.classList.contains('is-on') ? '' : p, true); } s.addEventListener('click', pick); s.addEventListener('keydown', function(e){ if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); pick(e); } }); });
  signs.forEach(function(g){ g.addEventListener('click', function(){ choose(g.getAttribute('data-persona'), true); var t = document.getElementById('situationen'); if(t){ if(lenis){ lenis.scrollTo(t, {offset:-20}); } else { t.scrollIntoView({behavior: reduce ? 'auto' : 'smooth'}); } } }); });
  try{ var saved = sessionStorage.getItem('mb-persona'); if(saved){ choose(saved, false); } }catch(e){}

  /* ---- hero scene: layers move at different speeds, the sun rises between them ---- */
  var scene = document.getElementById('scene'), sun = document.getElementById('qbtn'), glow = document.getElementById('glow');
  var l2 = document.getElementById('lay2'), l3 = document.getElementById('lay3'), heroEl = document.getElementById('hero');
  var calm = reduce, lastY = -1;
  function sceneTick(){
    var y = window.scrollY;
    if(y !== lastY && scene && heroEl){
      lastY = y;
      var max = heroEl.offsetHeight, p = Math.max(0, Math.min(1, y / (max * 0.72)));
      var e = 1 - Math.pow(1 - p, 2.2);
      if(calm){ p = 1; e = 1; y = 0; }
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
    var hero = S('hero'), weg = S('wegweiser'), sit = S('situationen'), met = S('route'), mic = S('lotse'), sem = S('ankunft'), kos = S('kostprobe'), boo = S('gespraech');
    var q = rect('.jhero__known'), slot = rect('.tangle-slot'), end = rect('#thread-end'), wr = rect('#route .wrap'), poster = rect('#lotse .poster'), mtxt = rect('#lotse .split > .stack');
    if(!hero || !weg || !sit || !met || !mic || !sem || !kos || !boo || !q || !slot || !end || !wr) return;
    var gut = parseFloat(getComputedStyle(document.querySelector('#route .wrap')).paddingLeft) || 40;
    var LG = wr.l + gut * 0.42, RG = wr.r - gut * 0.42;
    var gapX = (poster && mtxt) ? (mtxt.r + poster.l) / 2 : W * 0.5;
    var G = [];
    var qx = W * 0.5;
    G.push(['n', [[qx, hero.b - 34], [qx - 10, hero.b - 2]]]);
    var cx = slot.l + slot.w * 0.5, cy = slot.t + slot.h * 0.5, rr = Math.min(slot.w, slot.h) * 0.42, loop = [];
    for(var k = 0; k <= 10; k++){ var a = -Math.PI * 0.75 + k * Math.PI * 0.42, rad = rr * (0.62 + 0.24 * Math.sin(k * 1.7) + (k % 3) * 0.14); loop.push([cx + Math.cos(a) * rad * 1.5, cy + Math.sin(a) * rad * 0.82]); }
    G.push(['n', [[W * 0.44, weg.t + 40]].concat(loop, [[W * 0.5, weg.t + weg.h * 0.86], [RG, weg.b - 14]])]);
    G.push(['n', [[RG, sit.t + sit.h * 0.3], [RG, sit.b - 12]]]);
    G.push(['n', [[W * 0.5, met.t + 44], [LG, met.t + 120], [LG, met.t + met.h * 0.5], [LG, met.b - 24]]]);
    G.push(['n', [[W * 0.28, mic.t + 46], [gapX, mic.t + mic.h * 0.2], [gapX, mic.b - 24]]]);
    G.push(['l', [[W * 0.66, sem.t + 20], [W * 0.74, sem.t + sem.h * 0.5], [W * 0.64, sem.b - 12]]]);
    G.push(['n', [[W * 0.8, kos.t + 44], [RG, kos.t + kos.h * 0.3], [RG, kos.b - 16]]]);
    var ex = end.l + end.w / 2, ey = end.t + end.h / 2;
    G.push(['l', [[W * 0.92, boo.t + 50], [W * 0.78, ey - 110], [ex + 260, ey + 4], [ex + 10, ey]]]);
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
  function reveal(){ if(clipRect){ clipRect.setAttribute('height', reduce ? main.scrollHeight : Math.max(0, window.scrollY + window.innerHeight * 0.7)); } }
  var last = -1;
  (function loop(){ if(window.scrollY !== last){ last = window.scrollY; reveal(); } requestAnimationFrame(loop); })();
  var tmr = null; function rebuild(){ clearTimeout(tmr); tmr = setTimeout(build, 120); }
  window.addEventListener('resize', rebuild); window.addEventListener('load', rebuild);
  if(document.fonts && document.fonts.ready){ document.fonts.ready.then(rebuild); }
  if('ResizeObserver' in window){ new ResizeObserver(rebuild).observe(main); }
  build();
})();
</script>`;
  return html;
}
