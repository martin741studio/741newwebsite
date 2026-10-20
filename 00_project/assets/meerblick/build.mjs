// Agentur Meerblick: two homepage drafts (A = klar, B = Journey "Vom Steg zum Leuchtturm").
// Builds out/a.html and out/b.html with all photos inlined as data URIs (artifact CSP blocks external images).
// Run: node build.mjs   (images: web/*.webp, created with cwebp from the originals of agentur-meerblick.de)
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { pageB as pageBJourney } from './journey.mjs';
const here = path.dirname(fileURLToPath(import.meta.url));
const img = {};
for (const f of fs.readdirSync(path.join(here, 'web'))) if (f.endsWith('.webp')) img[f.replace('.webp', '')] = 'data:image/webp;base64,' + fs.readFileSync(path.join(here, 'web', f)).toString('base64');

const KONTAKT = 'https://www.agentur-meerblick.de/kontakt.html';
const SHOP_VIP = 'https://www.agentur-meerblick.de/shop/shopartikel/erstgespraech-homepage.html';
const SHOP_WEBINAR = 'https://www.agentur-meerblick.de/shop/shopartikel/webseite-systemanwendung-leicht-gemacht.html';
const FAQ = 'https://www.agentur-meerblick.de/faq.html';
const BLOG = 'https://www.agentur-meerblick.de/blog.html';
const LINK_A = process.env.LINK_A || '#';
const LINK_B = process.env.LINK_B || '#';

/* ---------- shared CSS ---------- */
const baseCss = `
/* Layout: one column, max 1180px, generous sections. Brand from the Meerblick logo: sea teal + deep green, warm sand ground. */
:root{
  --sea:#1FB3A3; --sea-deep:#168C80; --deep:#3B655F; --ink:#1C2826; --muted:#5E6E6B;
  --paper:#FFFFFF; --sand:#F4F1EA; --foam:#E7F6F3; --line:#DCE3E0; --sun:#F2B84B;
  --font-display:'Outfit', 'Segoe UI', Helvetica, Arial, sans-serif;
  --font-body:'Nunito Sans', 'Segoe UI', Helvetica, Arial, sans-serif;
  --font-accent:'Fraunces', Georgia, 'Times New Roman', serif;
  color-scheme: light;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--font-body);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:var(--sea-deep)}
h1,h2,h3,h4{font-family:var(--font-display);line-height:1.1;letter-spacing:-.01em;margin:0;text-wrap:balance}
h2{font-size:clamp(1.9rem,3.4vw,2.8rem);font-weight:600}
h3{font-size:clamp(1.2rem,1.8vw,1.45rem);font-weight:600}
p{margin:0}
.accent{font-family:var(--font-accent);font-style:italic;font-weight:400;color:var(--sea-deep)}
.wrap{width:min(1180px,100% - 40px);margin-inline:auto}
.narrow{width:min(760px,100% - 40px);margin-inline:auto}
.section{padding-block:clamp(64px,9vw,120px)}
.section--sand{background:var(--sand)}
.section--foam{background:var(--foam)}
.section--deep{background:var(--deep);color:#fff}
.eyebrow{display:inline-block;font-family:var(--font-display);font-size:.78rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--sea-deep);margin-bottom:14px}
.section--deep .eyebrow{color:#9FE3D8}
.lead{font-size:clamp(1.05rem,1.4vw,1.25rem);color:var(--muted);max-width:62ch}
.section--deep .lead{color:#D6E6E2}
.btn{display:inline-flex;align-items:center;gap:.6rem;background:var(--deep);color:#fff;font-family:var(--font-display);font-weight:600;font-size:1rem;padding:.95rem 1.7rem;border-radius:999px;text-decoration:none;border:0;cursor:pointer;transition:transform .2s,background .2s,box-shadow .2s}
.btn:hover{background:var(--sea-deep);transform:translateY(-2px);box-shadow:0 12px 26px rgba(59,101,95,.22)}
.btn--sea{background:var(--sea);color:#0F2F2B}
.btn--sea:hover{background:var(--sea-deep);color:#fff}
.btn--ghost{background:transparent;color:var(--deep);border:1.5px solid var(--deep)}
.btn--ghost:hover{background:var(--deep);color:#fff}
.btn:focus-visible,a:focus-visible,button:focus-visible{outline:3px solid var(--sun);outline-offset:3px}
.draftbar{position:sticky;top:env(safe-area-inset-top,0px);z-index:60;background:#1C2826;color:#CFE3DF;font-size:.8rem;padding:.45rem 20px;display:flex;gap:14px;align-items:center;justify-content:center;flex-wrap:wrap}
.draftbar b{color:#fff}
.draftbar a{color:#9FE3D8;text-decoration:none;border-bottom:1px solid rgba(159,227,216,.5)}
/* header */
.hdr{position:sticky;top:calc(env(safe-area-inset-top,0px) + 31px);z-index:50;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.hdr__in{display:flex;align-items:center;justify-content:space-between;gap:20px;height:72px}
.hdr__logo img{height:44px;width:auto}
.hdr__nav{display:flex;gap:26px;font-family:var(--font-display);font-weight:500;font-size:.95rem}
.hdr__nav a{color:var(--ink);text-decoration:none}
.hdr__nav a:hover{color:var(--sea-deep)}
.hdr .btn{padding:.7rem 1.25rem;font-size:.92rem}
@media (max-width:900px){.hdr__nav{display:none}}
/* grids */
.grid-3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.grid-2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:40px;align-items:center}
@media (max-width:900px){.grid-3{grid-template-columns:1fr}.grid-2{grid-template-columns:1fr;gap:28px}}
.card{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:28px;min-width:0}
.card h3{margin-bottom:10px}
.check{list-style:none;padding:0;margin:18px 0 0;display:grid;gap:10px}
.check li{position:relative;padding-left:30px}
.check li::before{content:"";position:absolute;left:0;top:.42em;width:18px;height:18px;border-radius:50%;background:var(--sea);mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23000' d='M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-1.2 14.4-4-4 1.6-1.6 2.4 2.4 5.2-5.2 1.6 1.6-6.8 6.8z'/%3E%3C/svg%3E") center/contain no-repeat;-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23000' d='M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-1.2 14.4-4-4 1.6-1.6 2.4 2.4 5.2-5.2 1.6 1.6-6.8 6.8z'/%3E%3C/svg%3E") center/contain no-repeat}
.photo{border-radius:24px;overflow:hidden;aspect-ratio:3/2;background:var(--sand)}
.photo img{width:100%;height:100%;object-fit:cover}
.photo--portrait{aspect-ratio:5/4}
/* FAQ */
.faq{display:grid;gap:12px}
.faq details{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:18px 22px}
.faq summary{cursor:pointer;font-family:var(--font-display);font-weight:600;font-size:1.05rem;list-style:none;display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";color:var(--sea-deep);font-size:1.4rem;line-height:1}
.faq details[open] summary::after{content:"\\2013"}
.faq details p{margin-top:12px;color:var(--muted)}
/* contact */
.contact{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:start}
@media (max-width:900px){.contact{grid-template-columns:1fr}}
.contact dl{display:grid;grid-template-columns:auto 1fr;gap:10px 18px;margin:0}
.contact dt{color:var(--muted);font-size:.9rem}
.contact dd{margin:0;font-weight:600}
.contact dd a{text-decoration:none;color:var(--ink)}
/* footer */
.ftr{background:var(--ink);color:#B9CBC7;padding-block:40px;font-size:.9rem}
.ftr__in{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;align-items:center}
.ftr a{color:#DDEBE8;text-decoration:none}
.ftr img{height:34px;width:auto;filter:brightness(0) invert(1);opacity:.9}
.steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;counter-reset:step}
@media (max-width:900px){.steps{grid-template-columns:1fr}}
.step{position:relative;padding:28px;border-radius:20px;background:var(--paper);border:1px solid var(--line);min-width:0}
.step__n{font-family:var(--font-display);font-size:.8rem;font-weight:600;letter-spacing:.12em;color:var(--sea-deep);text-transform:uppercase;margin-bottom:10px}
.step h3{margin-bottom:10px}
.step p{color:var(--muted)}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
`;

const fonts = `<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&family=Nunito+Sans:ital,wght@0,400;0,600;0,700;1,400&family=Fraunces:ital,opsz,wght@1,9..144,400&display=swap">`;

const draftbar = (which) => `<div class="draftbar"><span><b>Entwurf ${which === 'A' ? 'A · Klar' : 'B · Journey'}</b> für Agentur Meerblick</span><span>${which === 'A' ? `<a href="${LINK_B}">Entwurf B ansehen: die Journey &rarr;</a>` : `<a href="${LINK_A}">Entwurf A ansehen: die klare Version &rarr;</a>`}</span></div>`;

const header = (nav) => `<header class="hdr"><div class="wrap hdr__in">
  <a class="hdr__logo" href="#top" aria-label="Agentur Meerblick"><img src="${img.logo}" alt="Agentur Meerblick: Mehr Sichtbarkeit für dein Business" width="900" height="245"></a>
  <nav class="hdr__nav" aria-label="Hauptnavigation">${nav.map(([h, t]) => `<a href="${h}">${t}</a>`).join('')}</nav>
  <a class="btn" href="${KONTAKT}">Gespräch buchen</a>
</div></header>`;

const contact = (headline, sub) => `<section class="section section--sand" id="kontakt"><div class="wrap contact">
  <div><span class="eyebrow">Kontakt</span><h2>${headline}</h2><p class="lead" style="margin-top:16px">${sub}</p>
    <div style="margin-top:28px;display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="${KONTAKT}">Gesprächstermin vereinbaren</a><a class="btn btn--ghost" href="${SHOP_VIP}">30 Min VIP-Gespräch</a></div></div>
  <div class="card"><dl>
    <dt>Agentur</dt><dd>Agentur-Meerblick · Klaus-Dieter Sachs</dd>
    <dt>Adresse</dt><dd>Am Delf 29, 26160 Bad Zwischenahn</dd>
    <dt>Telefon</dt><dd><a href="tel:+4944039396811">+49 4403 9396811</a></dd>
    <dt>E-Mail</dt><dd><a href="mailto:info@agentur-meerblick.de">info@agentur-meerblick.de</a></dd>
    <dt>Region</dt><dd>Ammerland, Oldenburg, Westerstede und der ganze Nordwesten</dd>
  </dl></div>
</div></section>`;

const footer = `<footer class="ftr"><div class="wrap ftr__in">
  <img src="${img.logo}" alt="" width="900" height="245">
  <div>Agentur-Meerblick · Am Delf 29 · 26160 Bad Zwischenahn · <a href="tel:+4944039396811">+49 4403 9396811</a> · <a href="mailto:info@agentur-meerblick.de">info@agentur-meerblick.de</a></div>
  <div><a href="https://www.agentur-meerblick.de/impressum.html">Impressum</a> · <a href="https://www.agentur-meerblick.de/datenschutz.html">Datenschutz</a></div>
</div></footer>`;

/* ---------- shared copy blocks ---------- */
const services = [
  {
    key: 'website', badge: 'Deine Website',
    h: 'Eine handgebaute Website, die in 30 Tagen online ist und aus Besuchern Anfragen macht',
    p: 'Kein Baukasten, keine Vorlage, die bei allen gleich aussieht. Eine Seite, die zu dir passt, auf dem Handy schnell lädt und den Besucher an die Hand nimmt.',
    li: ['Konzept und Texte entstehen mit dir im Gespräch', 'Klare Startseite mit einer Handlung: anrufen, buchen oder schreiben', 'Du änderst Texte später selbst, ohne Technik', 'Domain, Website und alle Zugänge gehören dir'],
    photo: 'laptop-start', alt: 'Laptop auf einem Schreibtisch mit dem Schriftzug Just Start'
  },
  {
    key: 'werbung', badge: 'Bezahlte Werbung',
    h: 'Google und Meta Anzeigen, die in 14 Tagen die ersten Anfragen bringen, mit klaren Kosten pro Anfrage',
    p: 'Werbung ist nur dann gut, wenn du weißt, was eine Anfrage kostet. Deshalb bauen wir erst das Angebot und die Landingpage, dann schalten wir die Anzeigen.',
    li: ['Ein Angebot, das Menschen in deiner Region wirklich suchen', 'Eine Seite, die genau zu der Anzeige passt', 'Jede Anfrage wird gemessen, jeden Monat siehst du die Zahlen', 'Das Werbebudget bleibt in deinem Konto'],
    photo: 'unternehmer-erfolg', alt: 'Arbeitsplatz mit Blick über eine weite Landschaft'
  },
  {
    key: 'lokal', badge: 'Lokal gefunden werden',
    h: 'In 90 Tagen vorne in Google Maps, wenn Menschen in deiner Nähe nach dir suchen',
    p: 'Die meisten Kunden einer Praxis oder eines Coaches kommen aus dem Umkreis. Genau dort muss dein Google-Profil stehen, mit Bewertungen und richtigen Daten.',
    li: ['Google-Unternehmensprofil vollständig und richtig eingerichtet', 'Bewertungen als fester Ablauf, nicht als Zufall', 'Einträge in Verzeichnissen mit überall gleichen Daten', 'Monatlicher Bericht mit Anrufen und Anfragen, nicht mit Fachbegriffen'],
    photo: 'leuchtturm', alt: 'Leuchtturm am Meer in der blauen Stunde'
  }
];

const faqItems = [
  ['Wie lange dauert eine neue Website?', 'Vom ersten Gespräch bis zum Start rechnen wir mit etwa 30 Tagen. Texte und Bilder, die du schon hast, verkürzen die Zeit. Die Seite geht erst online, wenn du sie freigegeben hast.'],
  ['Brauche ich einen Baukasten?', 'Nein. Wir bauen deine Seite von Hand. Sie lädt schneller, sieht nicht aus wie tausend andere und hat keine laufenden Lizenzkosten für ein System.'],
  ['Wem gehören Domain, Website und Zugänge?', 'Dir. Immer. Domain, Website, Google-Profil und alle Konten laufen auf deinen Namen. Du bekommst jeden Zugang in deine Hand.'],
  ['Was kostet das?', 'Das hängt vom Umfang ab, deshalb nennen wir Preise im Gespräch und nicht auf der Seite. Du bekommst vorher ein festes Angebot und weißt, was du bekommst und was nicht.'],
  ['Kann ich Texte später selbst ändern?', 'Ja. Du änderst Texte und Bilder ohne Technikkenntnisse. Feste Leitplanken sorgen dafür, dass dabei nichts kaputtgeht.'],
  ['Muss ich Website, Werbung und Google Maps zusammen buchen?', 'Nein. Wir gehen Schritt für Schritt. Meistens beginnt es mit der Website, weil Werbung und Google Maps nur so gut sind wie die Seite, auf der die Menschen landen.']
];
const faqHtml = `<div class="faq">${faqItems.map(([q, a]) => `<details><summary>${q}</summary><p>${a}</p></details>`).join('')}</div>`;

const about = (variant) => `<section class="section" id="klaus-dieter"><div class="wrap grid-2">
  <div class="photo photo--portrait"><img src="${img['kds-neu']}" alt="Klaus-Dieter Sachs, Inhaber der Agentur Meerblick" width="1000" height="800" loading="lazy"></div>
  <div>
    <span class="eyebrow">Über Klaus-Dieter Sachs</span>
    <h2>Der Blickwinkel<wbr>veränderer</h2>
    <p class="lead" style="margin-top:18px">Seit mehr als 30 Jahren lebe ich nach dem Motto: Verändere deinen Blickwinkel. Erst als Führungskraft, dann als Lebensberater und Coach, seit 2018 als Webdesigner.</p>
    <p style="margin-top:18px;color:var(--muted)">Ich habe viele Unternehmer getroffen und ihre Sorgen gehört. Viele zweifelten, ob eine Website überhaupt etwas bringt. Heute sind sie mit einer Seite von mir im Netz zu finden. Meine Aufgabe sehe ich darin, meine Kunden mit Herz und großem Verständnis durch diesen Prozess zu begleiten, und darüber hinaus.</p>
    <p style="margin-top:18px;font-family:var(--font-accent);font-style:italic;font-size:1.25rem;color:var(--deep)">„Du verdienst es, gesehen und gehört zu werden."</p>
    <div style="margin-top:26px"><a class="btn btn--ghost" href="${KONTAKT}">${variant === 'B' ? 'Mit Klaus-Dieter sprechen' : 'Lass uns zusammenkommen'}</a></div>
  </div>
</div></section>`;

const forWhom = `<section class="section section--foam" id="fuer-wen"><div class="wrap">
  <span class="eyebrow">Für wen</span>
  <h2>Für Menschen mit Können, die mehr gesehen werden wollen</h2>
  <p class="lead" style="margin-top:16px">Praxen, Coaches und Selbstständige im Nordwesten, die lieber bei ihren Kunden sind als am Computer.</p>
  <div class="grid-3" style="margin-top:36px">
    <div class="card"><h3>Praxen und Heilberufe</h3><p style="color:var(--muted)">Heilpraktiker, Physiotherapie, Osteopathie, Naturheilkunde. Patienten suchen in Google Maps, und sie wählen die Praxis mit dem besseren Eindruck.</p></div>
    <div class="card"><h3>Coaches und Berater</h3><p style="color:var(--muted)">Lebensberatung, Energiearbeit, Business-Coaching. Dein Angebot lebt von Vertrauen. Deine Seite muss es in Sekunden aufbauen.</p></div>
    <div class="card"><h3>Selbstständige und Start-ups</h3><p style="color:var(--muted)">Handwerk, Dienstleistung, neue Ideen aus dem Ammerland und Oldenburg. Du brauchst eine Seite, die Anfragen bringt, und einen Ansprechpartner, der bleibt.</p></div>
  </div>
</div></section>`;

/* ---------- PAGE A: klar ---------- */
const cssA = `
.hero{background:radial-gradient(90% 70% at 90% 0%,rgba(31,179,163,.16) 0%,rgba(31,179,163,0) 60%),linear-gradient(180deg,#FBFAF7 0%,var(--sand) 100%);padding-block:clamp(40px,6vw,80px) clamp(40px,5vw,64px);overflow:hidden}
.hero__stage{position:relative}
.slide{display:none}
.slide.is-active{display:block;animation:fadeIn .5s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.slide__in{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center;min-height:min(560px,70vh)}
@media (max-width:900px){.slide__in{grid-template-columns:1fr;gap:28px;min-height:0}}
.badge{display:inline-block;background:var(--sea);color:#0F2F2B;font-family:var(--font-display);font-weight:600;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;padding:.5rem 1rem;border-radius:999px;margin-bottom:22px}
.hero h1{font-size:clamp(2.2rem,4.2vw,3.7rem);font-weight:600;margin-bottom:18px}
.hero .sub{font-size:clamp(1.02rem,1.3vw,1.2rem);color:var(--muted);max-width:34rem;margin-bottom:28px}
.hero__actions{display:flex;flex-direction:column;gap:16px;align-items:flex-start}
.trust{display:flex;align-items:center;gap:10px;color:var(--muted);font-size:.92rem}
.trust::before{content:"";width:10px;height:10px;border-radius:50%;background:var(--sea);box-shadow:0 0 0 4px rgba(31,179,163,.2)}
.hero__visual{position:relative}
.hero__visual .photo{aspect-ratio:3/2;box-shadow:0 30px 60px -30px rgba(28,40,38,.45)}
.chip{position:absolute;left:18px;bottom:18px;background:rgba(255,255,255,.94);border-radius:14px;padding:12px 16px;font-size:.9rem;box-shadow:0 10px 30px rgba(0,0,0,.12);max-width:min(300px,80%)}
.chip b{font-family:var(--font-display);display:block;font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:var(--sea-deep);margin-bottom:2px}
.tabs{display:flex;gap:10px;flex-wrap:wrap;margin-top:34px}
.tab{font-family:var(--font-display);font-weight:600;font-size:.92rem;border:1.5px solid var(--line);background:rgba(255,255,255,.7);border-radius:999px;padding:.6rem 1.1rem;cursor:pointer;color:var(--ink)}
.tab.is-active{background:var(--deep);color:#fff;border-color:var(--deep)}
.pain{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start}
@media (max-width:900px){.pain{grid-template-columns:1fr}}
.pain h2{font-size:clamp(1.7rem,3vw,2.4rem)}
.pain .big{font-family:var(--font-display);font-weight:600;font-size:1.15rem}
.svc{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding-block:36px;border-top:1px solid var(--line)}
.svc:first-of-type{border-top:0}
.svc:nth-of-type(even) .photo{order:-1}
@media (max-width:900px){.svc{grid-template-columns:1fr;gap:22px}.svc:nth-of-type(even) .photo{order:0}}
.svc h3{font-size:clamp(1.35rem,2.2vw,1.9rem)}
`;

const slides = [
  {
    badge: 'Deine neue Website', h: 'Schluss mit der Website, für die du dich entschuldigst. <span class="accent">Deine neue Seite ist in 30 Tagen online</span> und bringt Anfragen, nicht nur Besucher.',
    sub: 'Handgebaut statt Baukasten. Texte und Aufbau, die den Besucher in eine Handlung führen. Und ein Ansprechpartner, der dich vom ersten Gespräch bis nach dem Start begleitet.',
    cta: 'Website-Gespräch buchen', trust: 'Seit 2018 Websites für Praxen, Coaches und Selbstständige', photo: 'kds', alt: 'Klaus-Dieter Sachs, Agentur Meerblick', chipT: 'Dein Ansprechpartner', chipB: 'Klaus-Dieter Sachs, Bad Zwischenahn'
  },
  {
    badge: 'Bezahlte Werbung', h: 'Schluss mit Warten auf Empfehlungen. <span class="accent">Anzeigen, die in 14 Tagen die ersten Anfragen bringen</span>, mit Kosten, die du kennst.',
    sub: 'Google und Meta Anzeigen mit einem klaren Angebot und einer Seite, die dazu passt. Jede Anfrage wird gemessen. Du siehst, was eine Anfrage kostet, bevor du mehr Budget gibst.',
    cta: 'Werbe-Gespräch buchen', trust: 'Werbebudget bleibt in deinem Konto, Zahlen jeden Monat offen', photo: 'unternehmer-erfolg', alt: 'Arbeitsplatz mit Blick über eine weite Landschaft', chipT: 'Messbar', chipB: 'Kosten pro Anfrage statt Klicks'
  },
  {
    badge: 'Lokal gefunden werden', h: 'Schluss mit Unsichtbarkeit in deiner Region. <span class="accent">In 90 Tagen vorne in Google Maps</span>, wenn Menschen in deiner Nähe suchen.',
    sub: 'Dein Google-Unternehmensprofil, Bewertungen und lokale Einträge als System. Nicht als Zufall. Damit das Telefon klingelt, wenn jemand in Bad Zwischenahn, Oldenburg oder Westerstede nach deinem Angebot sucht.',
    cta: 'Sichtbarkeits-Gespräch buchen', trust: 'Aus dem Ammerland, für den ganzen Nordwesten', photo: 'meer-steg', alt: 'Steg am Zwischenahner Meer im Sonnenlicht', chipT: 'Dein Umkreis', chipB: 'Ammerland, Oldenburg, Westerstede'
  }
];

const pageA = () => `<title>Agentur Meerblick</title>${fonts}<style>${baseCss}${cssA}</style>
${draftbar('A')}
${header([['#leistungen', 'Leistungen'], ['#ablauf', 'So arbeiten wir'], ['#klaus-dieter', 'Über Klaus-Dieter'], ['#faq', 'Fragen'], ['#kontakt', 'Kontakt']])}
<main id="top">
<section class="hero"><div class="wrap">
  <div class="hero__stage" id="stage">
    ${slides.map((s, i) => `<div class="slide${i === 0 ? ' is-active' : ''}" data-i="${i}" role="group" aria-roledescription="Slide" aria-label="${s.badge}"><div class="slide__in">
      <div><span class="badge">${s.badge}</span>
        ${i === 0 ? '<h1>' : '<h2 style="font-size:clamp(2.2rem,4.2vw,3.7rem);margin-bottom:18px">'}${s.h}${i === 0 ? '</h1>' : '</h2>'}
        <p class="sub">${s.sub}</p>
        <div class="hero__actions"><a class="btn" href="${KONTAKT}">${s.cta} &rarr;</a><span class="trust">${s.trust}</span></div>
      </div>
      <div class="hero__visual"><div class="photo"><img src="${img[s.photo]}" alt="${s.alt}" width="1200" height="800"${i === 0 ? '' : ' loading="lazy"'}></div><div class="chip"><b>${s.chipT}</b>${s.chipB}</div></div>
    </div></div>`).join('')}
  </div>
  <div class="tabs" role="tablist" aria-label="Leistung wählen">
    <button class="tab is-active" role="tab" data-i="0" id="tab0">Neue Website</button>
    <button class="tab" role="tab" data-i="1" id="tab1">Bezahlte Werbung</button>
    <button class="tab" role="tab" data-i="2" id="tab2">Google Maps und lokale Suche</button>
  </div>
</div></section>

<section class="section" id="warum"><div class="wrap pain">
  <div>
    <span class="eyebrow">Kennst du das?</span>
    <h2>Liebe Praxisinhaberin, lieber Coach,</h2>
    <ul class="check" style="margin-top:22px;font-size:1.05rem">
      <li>Hast du eine Website, die seit Jahren steht, aber nie jemand darüber anruft?</li>
      <li>Kommen deine Kunden nur über Empfehlungen, und du weißt nicht, was passiert, wenn die ausbleiben?</li>
      <li>Suchst du dich selbst bei Google und findest drei Mitbewerber vor dir?</li>
    </ul>
  </div>
  <div>
    <p class="big">Du bist gut in dem, was du tust. Das sieht nur niemand.</p>
    <p style="margin-top:14px;color:var(--muted)">Viele Selbstständige haben irgendwann eine Seite bauen lassen. Dann kam der Alltag. Die Seite blieb stehen. Werbung wirkte zu teuer, Google zu kompliziert. Und jeder Monat ohne neue Anfragen ist ein Monat, in dem andere die Kunden bekommen, die eigentlich zu dir passen.</p>
    <p style="margin-top:14px;color:var(--muted)">Du brauchst keinen Baukasten mit tausend Funktionen. Du brauchst keine Agentur, die dir 15 Seiten Bericht schickt. Du brauchst <strong>eine Seite, die Vertrauen aufbaut</strong>, <strong>Werbung, die du messen kannst</strong>, und <strong>ein Google-Profil, das dich in deiner Region nach vorne bringt</strong>. Und einen Menschen, der das mit dir durchgeht.</p>
    <div style="margin-top:24px"><a class="btn btn--sea" href="#leistungen">So helfen wir dir &darr;</a></div>
  </div>
</div></section>

<section class="section section--sand" id="leistungen"><div class="wrap">
  <span class="eyebrow">Leistungen</span>
  <h2>Drei Dinge, die zusammen das Telefon klingeln lassen</h2>
  <p class="lead" style="margin-top:16px">Alles aus einer Hand, Schritt für Schritt. Die Website ist das Fundament. Werbung und Google Maps bringen die Menschen darauf.</p>
  <div style="margin-top:40px">
  ${services.map((s) => `<div class="svc" id="${s.key}">
    <div><span class="eyebrow">${s.badge}</span><h3>${s.h}</h3><p style="margin-top:14px;color:var(--muted)">${s.p}</p><ul class="check">${s.li.map((l) => `<li>${l}</li>`).join('')}</ul></div>
    <div class="photo"><img src="${img[s.photo]}" alt="${s.alt}" width="1200" height="800" loading="lazy"></div>
  </div>`).join('')}
  </div>
</div></section>

<section class="section" id="ablauf"><div class="wrap">
  <span class="eyebrow">So arbeiten wir</span>
  <h2>Erst der Blickwinkel, dann die Technik</h2>
  <p class="lead" style="margin-top:16px">Wir fangen nicht mit Farben und Schriften an. Wir fangen mit der Frage an, wer bei dir kauft und warum.</p>
  <div class="steps" style="margin-top:36px">
    <div class="step"><div class="step__n">Schritt 1</div><h3>Das Gespräch</h3><p>30 Minuten, in denen wir deine Situation anschauen: Was läuft schon, wo kommen deine Kunden her, was soll sich ändern. Ohne Verkaufsdruck. Am Ende weißt du, ob es passt.</p></div>
    <div class="step"><div class="step__n">Schritt 2</div><h3>Das Konzept</h3><p>Wir legen fest, was deine Seite sagen muss, welche Leistung im Mittelpunkt steht und was der Besucher als Nächstes tun soll. Du bekommst ein festes Angebot und einen Zeitplan.</p></div>
    <div class="step"><div class="step__n">Schritt 3</div><h3>Umsetzung und Betreuung</h3><p>Wir bauen, du gibst frei. Nach dem Start bleibt Klaus-Dieter dein Ansprechpartner. Technik, Werbung und Google Maps laufen im Hintergrund weiter, mit Zahlen, die du verstehst.</p></div>
  </div>
</div></section>

${about('A')}
${forWhom}

<section class="section" id="faq"><div class="narrow">
  <span class="eyebrow">Fragen</span>
  <h2>Was Kunden vor dem ersten Gespräch wissen wollen</h2>
  <div style="margin-top:30px">${faqHtml}</div>
</div></section>

${contact('Bereit, deine Vision zum Leben zu erwecken?', 'Lass uns miteinander reden. Ein kurzes Gespräch zeigt, ob wir zueinander passen und wo der schnellste Hebel für dich liegt.')}
</main>
${footer}
<script>
(function(){
  var slides=[].slice.call(document.querySelectorAll('.slide')), tabs=[].slice.call(document.querySelectorAll('.tab')), cur=0, timer=null;
  function show(i){ cur=i; slides.forEach(function(s,k){ s.classList.toggle('is-active',k===i); }); tabs.forEach(function(t,k){ t.classList.toggle('is-active',k===i); t.setAttribute('aria-selected',k===i?'true':'false'); }); }
  function auto(){ clearInterval(timer); timer=setInterval(function(){ show((cur+1)%slides.length); },7000); }
  tabs.forEach(function(t){ t.addEventListener('click',function(){ show(+t.dataset.i); auto(); }); });
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches; if(!reduce) auto();
  document.getElementById('stage').addEventListener('mouseenter',function(){ clearInterval(timer); });
  document.getElementById('stage').addEventListener('mouseleave',function(){ if(!reduce) auto(); });
})();
</script>`;

/* ---------- PAGE B: Journey "Vom Steg zum Leuchtturm" ---------- */
const cssB = `
body{background:var(--sand)}
.jhero{position:relative;min-height:min(92vh,860px);display:grid;align-items:end;overflow:hidden;color:#fff;isolation:isolate}
.jhero__bg{position:absolute;inset:0;z-index:-1}
.jhero__bg img{width:100%;height:100%;object-fit:cover;object-position:50% 60%}
.jhero__bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,47,43,.2) 0%,rgba(15,47,43,.55) 45%,rgba(15,47,43,.9) 100%)}
.jhero h1,.jhero .lead{text-shadow:0 2px 18px rgba(15,47,43,.55)}
.jhero__in{padding-block:clamp(60px,10vw,120px) clamp(48px,7vw,90px)}
.jhero .eyebrow{color:#9FE3D8}
.jhero h1{font-size:clamp(2.6rem,7vw,6.2rem);font-weight:600;line-height:.98;letter-spacing:-.02em;max-width:14ch}
.jhero .lead{color:#DCEBE7;margin-top:22px;max-width:40ch;font-size:clamp(1.05rem,1.5vw,1.3rem)}
.sun{display:inline-grid;place-items:center;text-align:center;width:clamp(130px,16vw,190px);aspect-ratio:1;border-radius:50%;margin-top:34px;background:radial-gradient(circle at 34% 30%,#FBE7B4 0%,#F2C76A 55%,#E3AE4A 100%);color:#2A2412;text-decoration:none;font-family:var(--font-display);font-weight:600;font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;box-shadow:0 0 0 12px rgba(242,199,106,.25),0 0 80px 20px rgba(242,199,106,.35);transition:transform .3s,box-shadow .3s}
.sun:hover{transform:scale(1.04);box-shadow:0 0 0 16px rgba(242,199,106,.3),0 0 110px 30px rgba(242,199,106,.5)}
.sun span{max-width:9em;rotate:-6deg}
/* the route: a dashed line with station markers on the left */
.route{position:relative}
.route::before{content:"";position:absolute;left:calc(50% - 590px + 19px);top:0;bottom:0;border-left:3px dashed rgba(59,101,95,.35);z-index:0}
@media (max-width:1240px){.route::before{left:39px}}
@media (max-width:700px){.route::before{left:19px}}
.route.chosen::before{border-color:var(--sun)}
.station{position:relative}
.marker{position:absolute;left:calc(50% - 590px + 8px);top:clamp(64px,9vw,120px);width:26px;height:26px;border-radius:50%;background:var(--sea);border:4px solid var(--sand);box-shadow:0 0 0 3px var(--sea);z-index:1}
@media (max-width:1240px){.marker{left:28px}}
@media (max-width:700px){.marker{left:8px}}
.section--deep .marker{border-color:var(--deep)}
.route .wrap{position:relative;z-index:1;padding-left:56px}
@media (max-width:700px){.route .wrap{padding-left:36px}}
/* signpost */
.signs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:36px}
@media (max-width:900px){.signs{grid-template-columns:1fr}}
.sign{text-align:left;background:var(--paper);border:1.5px solid var(--line);border-radius:18px;padding:24px;cursor:pointer;font:inherit;color:var(--ink);transition:transform .2s,border-color .2s,box-shadow .2s;min-width:0}
.sign:hover{transform:translateY(-3px);border-color:var(--sea);box-shadow:0 14px 30px -18px rgba(28,40,38,.4)}
.sign.is-on{border-color:var(--sun);box-shadow:0 0 0 3px rgba(242,184,75,.35)}
.sign small{display:block;font-family:var(--font-display);font-size:.76rem;letter-spacing:.12em;text-transform:uppercase;color:var(--sea-deep);margin-bottom:8px}
.sign b{font-family:var(--font-display);font-size:1.15rem;font-weight:600;display:block;line-height:1.25}
.sign p{color:var(--muted);margin-top:8px;font-size:.95rem}
.sign::after{content:"Hier starten \\2192";display:inline-block;margin-top:14px;font-family:var(--font-display);font-weight:600;color:var(--sea-deep);font-size:.9rem}
/* stacking station cards */
.stack{display:grid;gap:clamp(22px,4vh,40px)}
.scard{position:sticky;top:calc(31px + 72px + 18px + var(--i,0) * 18px);border-radius:28px;overflow:hidden;background:var(--paper);display:grid;grid-template-columns:1fr 1fr;min-height:min(560px,70vh);box-shadow:0 -20px 50px -30px rgba(28,40,38,.4);border:1px solid var(--line)}
.scard:nth-child(2){background:var(--foam)}
.scard:nth-child(3){background:var(--deep);color:#fff;border-color:var(--deep)}
.scard:nth-child(3) .muted{color:#D6E6E2}
.scard:nth-child(3) .eyebrow{color:#9FE3D8}
@media (max-width:900px){.scard{grid-template-columns:1fr;position:relative;top:auto;min-height:0}.scard .photo{aspect-ratio:16/9;border-radius:0}}
.scard__body{padding:clamp(26px,3.6vw,48px);display:grid;align-content:center;gap:12px;min-width:0}
.scard .photo{border-radius:0;aspect-ratio:auto;min-height:260px}
.scard h3{font-size:clamp(1.45rem,2.4vw,2.1rem)}
.muted{color:var(--muted)}
.tag{display:none;background:var(--sun);color:#2A2412;font-family:var(--font-display);font-weight:600;font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;padding:.4rem .8rem;border-radius:999px;width:max-content}
.scard.is-entry .tag{display:inline-block}
.after{margin-top:8px;padding:14px 16px;border-radius:14px;background:rgba(31,179,163,.12);font-size:.95rem}
.scard:nth-child(3) .after{background:rgba(255,255,255,.1)}
.after b{font-family:var(--font-display);display:block;font-size:.76rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px}
/* pilot */
.pilot{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
@media (max-width:900px){.pilot{grid-template-columns:1fr}}
.pilot .photo{aspect-ratio:3/2;box-shadow:0 30px 60px -30px rgba(28,40,38,.5)}
.quote{font-family:var(--font-accent);font-style:italic;font-size:clamp(1.3rem,2.2vw,1.8rem);line-height:1.35;color:var(--deep)}
/* taste */
.taste{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:36px}
@media (max-width:900px){.taste{grid-template-columns:1fr}}
.taste a{display:block;text-decoration:none;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:26px;transition:transform .2s,border-color .2s}
.taste a:hover{transform:translateY(-3px);border-color:var(--sea)}
.taste small{display:block;font-family:var(--font-display);font-size:.76rem;letter-spacing:.12em;text-transform:uppercase;color:var(--sea-deep);margin-bottom:8px}
.taste b{font-family:var(--font-display);font-size:1.15rem;font-weight:600;display:block}
.taste p{color:var(--muted);margin-top:8px;font-size:.95rem}
/* arrival */
.arrive{position:relative;min-height:min(70vh,640px);display:grid;align-items:center;color:#fff;isolation:isolate;overflow:hidden}
.arrive__bg{position:absolute;inset:0;z-index:-1}
.arrive__bg img{width:100%;height:100%;object-fit:cover}
.arrive__bg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,47,43,.78) 0%,rgba(15,47,43,.35) 60%,rgba(15,47,43,.2) 100%)}
.arrive h2{font-size:clamp(2.2rem,4.6vw,3.8rem);max-width:16ch}
.arrive .lead{color:#DCEBE7}
.float{position:fixed;right:18px;bottom:calc(18px + env(safe-area-inset-bottom,0px));z-index:70;box-shadow:0 14px 30px rgba(28,40,38,.3)}
@media (max-width:700px){.float{right:12px;bottom:calc(12px + env(safe-area-inset-bottom,0px));padding:.8rem 1.2rem}}
`;

const stations = [
  { ...services[0], n: 'Station 1', name: 'Das Fundament: deine Website', after: 'Eine Seite, die du gern zeigst. Mit einer klaren Handlung für jeden Besucher und Zugängen, die dir gehören.' },
  { ...services[1], n: 'Station 2', name: 'Der Wind: bezahlte Werbung', after: 'Du weißt, was eine Anfrage kostet. Und du kannst entscheiden, wann du mehr Wind in die Segel gibst.' },
  { ...services[2], n: 'Station 3', name: 'Das Leuchtfeuer: lokal gefunden werden', after: 'Wer in deiner Region sucht, sieht dich vorne. Das Telefon klingelt, ohne dass du dafür Anzeigen brauchst.' }
];

const pageB = () => `<title>Agentur Meerblick Journey</title>${fonts}<style>${baseCss}${cssB}</style>
${draftbar('B')}
${header([['#wegweiser', 'Wo stehst du?'], ['#route', 'Die Route'], ['#lotse', 'Der Lotse'], ['#kostprobe', 'Kostprobe'], ['#kontakt', 'Kontakt']])}
<main id="top">
<section class="jhero" id="hero">
  <div class="jhero__bg"><img src="${img['meer-steg']}" alt="Steg am Zwischenahner Meer, das Wasser glitzert in der Sonne" width="1200" height="800"></div>
  <div class="wrap jhero__in">
    <span class="eyebrow">Agentur Meerblick · Bad Zwischenahn</span>
    <h1>Mehr Sichtbarkeit für dein Business.</h1>
    <p class="lead">Vom ersten Gespräch bis zu dem Tag, an dem Kunden dich finden, ohne dass du sie suchen musst. Eine Reise, Schritt für Schritt, mit einem Lotsen an deiner Seite.</p>
    <a class="sun" href="#wegweiser"><span>Wo stehst du gerade?</span></a>
  </div>
</section>

<div class="route" id="route-line">
<section class="section station" id="wegweiser"><span class="marker" aria-hidden="true"></span><div class="wrap">
  <span class="eyebrow">Der Wegweiser</span>
  <h2>Wo stehst du gerade?</h2>
  <p class="lead" style="margin-top:16px">Wähle den Satz, der am besten passt. Die Route zeigt dir dann, wo deine Reise beginnt.</p>
  <div class="signs" role="group" aria-label="Deine Situation">
    <button class="sign" data-target="st-website"><small>Situation 1</small><b>Meine Website arbeitet nicht für mich.</b><p>Sie steht seit Jahren, sieht aus wie viele andere, und niemand ruft deswegen an.</p></button>
    <button class="sign" data-target="st-werbung"><small>Situation 2</small><b>Ich habe Besucher, aber keine Anfragen.</b><p>Empfehlungen tragen dich, aber du willst nicht mehr vom Zufall abhängen.</p></button>
    <button class="sign" data-target="st-lokal"><small>Situation 3</small><b>In meiner Region findet mich niemand.</b><p>Bei Google stehen drei Mitbewerber vor dir, obwohl du der Bessere bist.</p></button>
  </div>
</div></section>

<section class="section section--sand station" id="route"><span class="marker" aria-hidden="true"></span><div class="wrap">
  <span class="eyebrow">Die Route</span>
  <h2>Drei Stationen vom Steg zum Leuchtturm</h2>
  <p class="lead" style="margin-top:16px">Jede Station baut auf der vorherigen auf. Du musst nicht alle gehen. Aber die Reihenfolge ist kein Zufall.</p>
  <div class="stack" style="margin-top:40px">
  ${stations.map((s, i) => `<article class="scard" id="st-${s.key}" style="--i:${i}">
    <div class="scard__body"><span class="tag">Dein Einstieg</span><span class="eyebrow">${s.n} · ${s.badge}</span><h3>${s.name}</h3><p class="muted">${s.p}</p><ul class="check">${s.li.slice(0, 3).map((l) => `<li>${l}</li>`).join('')}</ul><div class="after"><b>Was du danach hast</b>${s.after}</div></div>
    <div class="photo"><img src="${img[s.photo]}" alt="${s.alt}" width="1200" height="800" loading="lazy"></div>
  </article>`).join('')}
  </div>
</div></section>

<section class="section station" id="lotse"><span class="marker" aria-hidden="true"></span><div class="wrap pilot">
  <div class="photo"><img src="${img.kds}" alt="Klaus-Dieter Sachs, Agentur Meerblick, im Grünen" width="1200" height="800" loading="lazy"></div>
  <div>
    <span class="eyebrow">Der Lotse</span>
    <h2>Klaus-Dieter Sachs</h2>
    <p class="quote" style="margin-top:18px">„Ich verhelfe Menschen mit beneidenswertem Können auf ihren eigenen Weg in die Sichtbarkeit. Mit Herz und großem Verständnis, durch den ganzen Prozess und darüber hinaus."</p>
    <p class="muted" style="margin-top:18px">Seit mehr als 30 Jahren nach dem Motto „Verändere deinen Blickwinkel". Erst Führungskraft, dann Lebensberater und Coach, seit 2018 Webdesigner für Praxen, Coaches und Selbstständige im Nordwesten. Technik, Werbung und Google Maps laufen im Team im Hintergrund. Dein Ansprechpartner bleibt immer derselbe.</p>
    <div style="margin-top:26px"><a class="btn btn--ghost" href="${KONTAKT}">Mit Klaus-Dieter sprechen</a></div>
  </div>
</div></section>

<section class="section section--foam station" id="kostprobe"><span class="marker" aria-hidden="true"></span><div class="wrap">
  <span class="eyebrow">Kostprobe</span>
  <h2>Erst ausprobieren. Dann entscheiden.</h2>
  <p class="lead" style="margin-top:16px">Drei kleine Schritte, bevor du einen großen gehst.</p>
  <div class="taste">
    <a href="${SHOP_VIP}"><small>30 Minuten</small><b>VIP-Gespräch</b><p>Wir schauen gemeinsam auf deine Seite und dein Google-Profil. Du gehst mit konkreten Punkten raus, egal ob wir danach zusammenarbeiten.</p></a>
    <a href="${SHOP_WEBINAR}"><small>90 Minuten live</small><b>Webinar: Homepage leicht gemacht</b><p>Klaus-Dieter zeigt dir live, wie du deine Seite selbst pflegst und Änderungen einbringst.</p></a>
    <a href="${FAQ}"><small>Zum Lesen</small><b>Tipps aus der Praxis</b><p>Antworten auf die Fragen, die Unternehmer ihm seit Jahren stellen. Vom Besucher zum Fan, Leuchtturm deiner Marke, Business mit Leidenschaft.</p></a>
  </div>
</div></section>
</div>

<section class="arrive" id="ankunft">
  <div class="arrive__bg"><img src="${img.leuchtturm}" alt="Leuchtturm in der blauen Stunde, ein Weg führt über die Felsen hin" width="1200" height="800" loading="lazy"></div>
  <div class="wrap" style="padding-block:clamp(64px,9vw,120px)">
    <span class="eyebrow" style="color:#9FE3D8">Die Ankunft</span>
    <h2>Dein Leuchtturm steht. Jetzt müssen ihn nur noch die Richtigen sehen.</h2>
    <p class="lead" style="margin-top:18px;max-width:46ch">Jede Reise beginnt mit einem Gespräch. 30 Minuten, kein Verkaufsdruck. Am Ende weißt du, ob es passt und wo dein schnellster Hebel liegt.</p>
    <div style="margin-top:28px"><a class="btn btn--sea" href="${KONTAKT}">Gespräch buchen &rarr;</a></div>
  </div>
</section>

${contact('Lass uns miteinander reden', 'Schreib, ruf an oder buche direkt einen Termin. Klaus-Dieter antwortet persönlich.')}
</main>
${footer}
<a class="btn btn--sea float" href="${KONTAKT}">Gespräch buchen</a>
<script>
(function(){
  var signs=[].slice.call(document.querySelectorAll('.sign')), route=document.getElementById('route-line');
  signs.forEach(function(s){ s.addEventListener('click',function(){
    signs.forEach(function(x){ x.classList.toggle('is-on',x===s); });
    [].slice.call(document.querySelectorAll('.scard')).forEach(function(c){ c.classList.toggle('is-entry',c.id===s.dataset.target); });
    route.classList.add('chosen');
    var t=document.getElementById(s.dataset.target); if(t){ t.scrollIntoView({behavior:'smooth',block:'start'}); }
  }); });
})();
</script>`;

fs.mkdirSync(path.join(here, 'out'), { recursive: true });
fs.writeFileSync(path.join(here, 'out', 'a.html'), pageA());
fs.writeFileSync(path.join(here, 'out', 'b.html'), pageBJourney({ img, fonts, draftbar: '<div class="draft"><b>Entwurf B · Journey</b> &nbsp;·&nbsp; <a href="' + LINK_A + '">Entwurf A ansehen: die klare Version &rarr;</a></div>', footer, contact, KONTAKT, SHOP_VIP, SHOP_WEBINAR, FAQ, stations }));
console.log('built', fs.statSync(path.join(here, 'out', 'a.html')).size, fs.statSync(path.join(here, 'out', 'b.html')).size);
