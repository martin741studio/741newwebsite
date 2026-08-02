#!/usr/bin/env node
/**
 * 741.Studio Prospect-Pipeline — generiert automatisch eine persönliche
 * Review-Page (wie tanja-neumann) aus Lead-Daten.
 *
 * Ablauf: Local-Falcon-Scan → PageSpeed → On-Page-Audit → Seite aus Template
 * → Scan-Bild herunterladen → (optional) Build + Deploy → (optional) Mail an Lead.
 *
 * Aufruf (manuell oder später vom VPS/Webhook):
 *   node scripts/prospect-pipeline/generate.mjs \
 *     --company "Tanja Neumann" --firstname Tanja --city Lindlar \
 *     --branch "Heilpraktikerin für Psychotherapie" --domain tanja-neumann.com \
 *     --keyword "psychotherapie lindlar" --email lead@example.com \
 *     [--slug tanja-neumann] [--deploy] [--send]
 *
 * Test ohne Local-Falcon-Credits:
 *   node scripts/prospect-pipeline/generate.mjs --fixture fixtures/tanja.json --slug test-fixture
 *
 * Benötigte .env-Einträge:
 *   PAGESPEED_API_KEY=…   (vorhanden)
 *   LF_API_KEY=…          (Local Falcon → Settings → API)
 *   RESEND_API_KEY=…      (nur für --send)
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { execSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '../..');

/* ---------- .env laden ---------- */
for (const line of (existsSync(path.join(ROOT, '.env')) ? readFileSync(path.join(ROOT, '.env'), 'utf8').split('\n') : [])) {
  const m = line.match(/^([A-Z_]+)=(.*)$/);
  if (m && !process.env[m[1]]) process.env[m[1]] = m[2].trim();
}

/* ---------- CLI-Args ---------- */
const args = {};
const argv = process.argv.slice(2);
for (let i = 0; i < argv.length; i++) {
  if (argv[i].startsWith('--')) {
    const key = argv[i].slice(2);
    const val = argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[++i] : true;
    args[key] = val;
  }
}

const slugify = (s) => s.toLowerCase()
  .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
  .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

const log = (m) => console.log(`▸ ${m}`);
const fail = (m) => { console.error(`✗ ${m}`); process.exit(1); };

/* =========================================================
 * 1) LOCAL FALCON API  (Data-Retrieval-Endpoints — im Tarif enthalten,
 * verifiziert 2026-07-25). Places-Suche & Scan-START sind On-Demand-
 * Endpoints (separates Abo) — Scans werden daher in der LF-UI oder
 * per MCP gestartet; hier reicht der report_key bzw. die place_id.
 * ========================================================= */
const LF = {
  base: 'https://api.localfalcon.com/v1',
  key() { return process.env.LF_API_KEY || fail('LF_API_KEY fehlt in .env (Local Falcon → Developers → API & MCP Credentials)'); },
  async get(p, params = {}) {
    const u = new URL(this.base + p);
    u.searchParams.set('api_key', this.key());
    for (const [k, v] of Object.entries(params)) u.searchParams.set(k, v);
    const r = await fetch(u);
    const j = await r.json();
    if (!r.ok || j.success === false) throw new Error(`LF ${p}: ${JSON.stringify(j).slice(0, 300)}`);
    return j;
  },
  /** Vollständigen Scan-Report holen (enthält location, places, image, solv/arp). */
  async getReport(reportKey) {
    const j = await this.get(`/reports/${reportKey}/`);
    return j.data;
  },
  /** Neuesten Report für eine place_id finden (durchsucht die Report-Liste). */
  async latestReportForPlace(placeId, maxPages = 5) {
    let token = null;
    for (let page = 0; page < maxPages; page++) {
      const j = await this.get('/reports/', token ? { next_token: token } : {});
      const hit = (j.data?.reports || []).find((r) => r.place_id === placeId);
      if (hit) return hit.report_key;
      token = j.data?.next_token;
      if (!token) break;
    }
    return null;
  },
  /** Report → normalisierte Scan- & Place-Objekte fürs Template. */
  normalize(report) {
    const placesDict = report.places || {};
    const list = Array.isArray(placesDict) ? placesDict : Object.entries(placesDict).map(([pid, p]) => ({ place_id: pid, ...p }));
    const competitors = list
      .filter((p) => p.place_id !== report.place_id && p.name)
      .sort((a, b) => parseFloat(b.solv) - parseFloat(a.solv))
      .slice(0, 5);
    const loc = report.location || {};
    return {
      scan: {
        report_key: report.report_key, arp: report.arp, solv: report.solv, found_in: report.found_in,
        grid_size: report.grid_size, radius: parseFloat(report.radius) || 7,
        image: report.image, keyword: report.keyword, competitors,
      },
      place: {
        place_id: report.place_id, name: loc.name, lat: report.lat, lng: report.lng,
        rating: loc.rating, reviews: loc.reviews ?? (list.find((p) => p.place_id === report.place_id) || {}).reviews ?? 0,
        address: loc.address || '',
      },
    };
  },
};

/* =========================================================
 * 2) PAGESPEED
 * ========================================================= */
async function pageSpeed(domain) {
  const key = process.env.PAGESPEED_API_KEY;
  const url = `https://${domain.replace(/^https?:\/\//, '')}`;
  const scores = {};
  for (const strategy of ['mobile', 'desktop']) {
    try {
      const r = await fetch(`https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${encodeURIComponent(url)}&strategy=${strategy}&category=performance&key=${key}`);
      const j = await r.json();
      scores[strategy] = Math.round((j.lighthouseResult?.categories?.performance?.score || 0) * 100);
      if (strategy === 'mobile') scores.lcp = j.lighthouseResult?.audits?.['largest-contentful-paint']?.displayValue || '';
    } catch { scores[strategy] = null; }
  }
  return scores;
}

/* =========================================================
 * 3) ON-PAGE-AUDIT (rein aus dem HTML der Prospect-Seite)
 * ========================================================= */
async function onPageAudit(domain) {
  const url = `https://${domain.replace(/^https?:\/\//, '')}`;
  const a = { url };
  try {
    const r = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0' }, redirect: 'follow' });
    const html = await r.text();
    a.title = (html.match(/<title[^>]*>([^<]*)/i) || [])[1]?.trim() || '';
    a.metaDesc = /<meta[^>]+name=["']description["'][^>]+content=["']([^"']+)/i.test(html);
    a.h1Count = (html.match(/<h1[\s>]/gi) || []).length;
    a.schema = html.includes('application/ld+json');
    a.ogCount = (html.match(/property=["']og:/g) || []).length;
    const imgs = html.match(/<img [^>]*>/gi) || [];
    a.imgTotal = imgs.length;
    a.imgWithAlt = imgs.filter((t) => /alt=["'][^"']+["']/.test(t)).length;
    a.https = r.url.startsWith('https');
    a.titleWeak = a.title.length < 25 || /willkommen|home|start/i.test(a.title);
  } catch (e) { a.error = e.message; }
  return a;
}

/* =========================================================
 * 4) SEITE ZUSAMMENBAUEN
 * ========================================================= */
function composePage({ lead, scan, place, speed, onpage }) {
  const tpl = readFileSync(path.join(__dirname, 'template.html'), 'utf8');
  const gridPoints = Math.pow(parseInt(scan.grid_size || 7), 2);
  const topComp = scan.competitors?.[0];
  const compReviews = scan.competitors?.map((c) => parseInt(c.reviews) || 0).filter((n) => n > 0) || [];
  const revRange = compReviews.length ? `${Math.min(...compReviews)}–${Math.max(...compReviews)}` : 'wenige';

  const today = new Date().toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit', year: 'numeric' });
  const solv = parseFloat(scan.solv) || 0;
  const arp = parseFloat(scan.arp) || 0;
  const tierEarly = solv >= 60 ? 'high' : solv >= 15 ? 'mid' : 'low';
  const noSiteEarly = !lead.domain;

  const data = {
    companyName: lead.company, contactName: lead.firstname, prospectSlug: lead.slug,
    city: lead.city, branch: lead.branch, loomUrl: '', loomDuration: '3–4 Minuten',
    mapsRankDesktop: `Ø Position ${arp.toFixed(0)} (SoLV ${solv.toFixed(0)}%)`,
    mapsRankMobile: 'live prüfen', focusKeyword: lead.keyword,
    currentReviewsCount: parseInt(place.reviews) || 0, currentRating: place.rating ? parseFloat(place.rating).toFixed(1) : '–',
    mobileSpeedScore: !lead.domain ? 'Keine Website vorhanden' : speed.mobile ? `Mobil ${speed.mobile} · Desktop ${speed.desktop}` : 'live prüfen',
    personalMessageGreeting: `Hallo ${lead.firstname},`,
    authorName: 'Martin Drendel', authorRole: 'Senior Local SEO & Growth Consultancy',
    positives: [
      place.rating >= 4.8 ? `Starke ${parseFloat(place.rating).toFixed(1)}-Sterne-Bewertung auf deinem Google-Profil.` : 'Dein Google-Profil ist vorhanden und erreichbar.',
      `Klares Angebot als ${lead.branch} in ${lead.city}.`,
      speed.mobile >= 80 ? `Solide Technik-Basis (PageSpeed mobil ${speed.mobile}).` : 'Website vorhanden – Basis zum Ausbauen.',
    ],
    opportunities: tierEarly === 'high' ? [
      `Nr.-1-Position bei '${lead.keyword}' absichern – Wettbewerber können mit wenigen Bewertungen aufholen.`,
      noSiteEarly ? 'Eigene Website aufbauen – aus Google-Sichtbarkeit werden dann buchbare Anfragen.' : `Sichtbarkeit in Anfragen verwandeln – Buchungsweg & Website-Conversion optimieren.`,
      `${place.reviews || 0} Bewertung(en) weiter ausbauen – je größer der Abstand, desto sicherer die Spitzenposition.`,
    ] : [
      `Google Maps: Top-3-Sichtbarkeit (SoLV) ${tierEarly === 'mid' ? 'bei' : 'nur'} ${solv.toFixed(0)} %${topComp ? ` – ${tierEarly === 'mid' ? 'der stärkste Verfolger hat' : 'der Marktführer hat'} ${parseFloat(topComp.solv).toFixed(0)} %` : ''}. ${tierEarly === 'mid' ? 'Ausbau auf volle Marktabdeckung möglich' : `Riesiges Potenzial bei '${lead.keyword}'`}.`,
      `${place.reviews || 0} Google-Bewertung(en) – die Top-Wettbewerber haben ${revRange}. ${(place.reviews || 0) > 10 ? 'Vorsprung ausbauen.' : 'Diese Lücke ist aufholbar.'}`,
      noSiteEarly ? 'Eigene Website als größter einzelner Hebel.' : 'Website-SEO-Basics (Title, Meta, Struktur) – schnelle, wirksame Hebel.',
    ],
    criticalIssues: [
      noSiteEarly ? 'Keine eigene Website – Interessenten finden dich, können sich aber nirgends informieren oder buchen.' : onpage.titleWeak ? `Meta-Title ist '${onpage.title || 'leer'}' – kein Keyword, kein Ort.` : onpage.h1Count !== 1 ? `${onpage.h1Count}× H1 auf der Startseite – saubere Struktur fehlt.` : `Ladezeit mobil ausbaufähig (PageSpeed ${speed.mobile ?? '–'}).`,
      !onpage.metaDesc && !noSiteEarly ? 'Meta-Description fehlt komplett.' : tierEarly === 'low' ? `Nur ${solv.toFixed(0)} % Top-3-Sichtbarkeit im Umkreis.` : `Spitzenposition ist ungeschützt – ${(place.reviews || 0)} Bewertungen sind schnell überholbar.`,
      !onpage.schema && !noSiteEarly ? 'Kein LocalBusiness-Schema – Google fehlen strukturierte Unternehmensdaten.' : 'Google-Profil nicht vollständig ausgebaut (Leistungen, Beschreibung, Fotos).',
    ],
    gbpAudit: [
      { title: 'Profil vorhanden & erreichbar', status: 'good', desc: 'Profil mit Kategorie, Telefon, Adresse & Website hinterlegt.' },
      { title: 'Bewertungen (Anzahl)', status: (place.reviews || 0) < 10 ? 'critical' : 'warning', desc: `${place.reviews || 0} Bewertung(en) – Top-Wettbewerber: ${revRange}.` },
      { title: `Maps-Sichtbarkeit (Scan ${today})`, status: solv < 20 ? 'critical' : 'warning', desc: `Ø Position ${arp.toFixed(1)}, Top-3-Sichtbarkeit ${solv.toFixed(0)} %${topComp ? ` – Marktführer: ${parseFloat(topComp.solv).toFixed(0)} %` : ''}.` },
      { title: 'Kategorien & Leistungen', status: 'warning', desc: 'Neben- Kategorien & einzelne Leistungen prüfen und vollständig eintragen.' },
      { title: 'Unternehmensbeschreibung', status: 'warning', desc: 'Beschreibung mit Keywords & Einzugsgebiet ausbauen.' },
      { title: 'Fotos, Beiträge & Q&A', status: 'warning', desc: 'Aktuelle Fotos & regelmäßige Beiträge stärken das Ranking.' },
    ],
    websiteAudit: onpage.noSite ? [
      { title: 'Website vorhanden', status: 'critical', desc: 'Keine eigene Website – der größte einzelne Hebel. Ohne Website fehlen Vertrauen, Informationen & Buchungsweg für alle, die dich bei Google finden.' },
      { title: 'Google-Profil als einzige Präsenz', status: 'warning', desc: 'Das Google-Profil trägt aktuell alles – umso wichtiger, es vollständig zu pflegen.' },
      { title: 'Buchungs-/Kontaktweg', status: 'warning', desc: 'Ohne Website: Telefon als einziger Kanal – Online-Terminbuchung oder zumindest eine Landingpage ergänzen.' },
    ] : [
      { title: 'SSL & Ladezeit', status: onpage.https && speed.mobile >= 70 ? 'good' : 'warning', desc: `https ${onpage.https ? 'aktiv' : 'prüfen'}; PageSpeed mobil ${speed.mobile ?? '–'} / Desktop ${speed.desktop ?? '–'}${speed.lcp ? ` (LCP ${speed.lcp})` : ''}.` },
      { title: 'Meta-Title', status: onpage.titleWeak ? 'critical' : 'good', desc: onpage.titleWeak ? `Aktuell: '${onpage.title || 'leer'}' – Keyword + Ort fehlen.` : `'${onpage.title.slice(0, 60)}'` },
      { title: 'Meta-Description', status: onpage.metaDesc ? 'good' : 'critical', desc: onpage.metaDesc ? 'Vorhanden.' : 'Fehlt komplett – Google zeigt zufälligen Text.' },
      { title: 'Überschriften-Struktur (H1)', status: onpage.h1Count === 1 ? 'good' : 'critical', desc: `${onpage.h1Count}× H1 auf der Startseite${onpage.h1Count !== 1 ? ' – genau eine Keyword-H1 ist der Standard' : ''}.` },
      { title: 'Schema / Rich Results', status: onpage.schema ? 'good' : 'critical', desc: onpage.schema ? 'Strukturierte Daten vorhanden.' : 'Kein LocalBusiness-Schema (JSON-LD).' },
      { title: 'Bilder / Alt-Texte', status: onpage.imgWithAlt >= onpage.imgTotal ? 'good' : 'warning', desc: `${onpage.imgWithAlt} von ${onpage.imgTotal} Bildern mit Alt-Text.` },
      { title: 'Open Graph / Vorschau', status: onpage.ogCount >= 4 ? 'good' : 'warning', desc: `${onpage.ogCount} OG-Tags – Link-Vorschau ${onpage.ogCount >= 4 ? 'ok' : 'unvollständig'}.` },
    ],
    citationAudit: [
      { title: 'NAP-Konsistenz', status: 'warning', desc: 'Name/Adresse/Telefon über alle Verzeichnisse prüfen.' },
      { title: 'Branchenbuch-Citations', status: 'warning', desc: 'jameda/branchenspezifisch, 11880, Gelbe Seiten prüfen & aufbauen.' },
      { title: 'Apple Maps & Bing Places', status: 'warning', desc: 'Einträge prüfen bzw. anlegen.' },
      { title: 'Lokale Backlinks', status: 'warning', desc: 'Lokale & Themen-Backlinks aufbauen.' },
    ],
    keywords: [
      { keyword: lead.keyword, region: `${lead.city} + ${scan.radius || 7} km`, volume: 'live ermitteln', currentRank: `Ø Pos. ${arp.toFixed(1)} – SoLV ${solv.toFixed(0)} % (Scan ${today})` },
    ],
    competitors: (scan.competitors || []).slice(0, 3).map((c) => ({
      name: c.name, rank: `SoLV ${parseFloat(c.solv).toFixed(0)}%`,
      reviews: `${c.reviews} (${parseFloat(c.rating || 0).toFixed(1)} ★)`,
      category: lead.branch, advantage: 'Dominiert das Einzugsgebiet in Maps',
    })),
    quickWins: [
      { title: 'Google-Bewertungen aktiv einsammeln', desc: `Top-Wettbewerber haben ${revRange} Bewertungen – mit Bewertungs-Link & QR-Code schnell aufholbar.` },
      { title: 'Google-Profil ausbauen', desc: 'Kategorien, Leistungen & Beschreibung vervollständigen.' },
      { title: 'Meta-Title & Description setzen', desc: `Keyword '${lead.keyword}' + Ort in Title & Description.` },
      { title: 'Struktur & Schema', desc: 'Saubere H1-Struktur + LocalBusiness-Schema (JSON-LD).' },
    ],
    growthMetrics: {
      currentRank: `Ø Pos. ${arp.toFixed(0)} (SoLV ${solv.toFixed(0)}%)`, targetRank: 'Top 3 Maps Pack',
      callsIncrease: '+180%', routesIncrease: '+240%', leadsIncrease: '+150%', trustLabel: 'Top 3 lokal',
    },
    roadmap: [
      { step: 'Phase 1', action: 'Bewertungsstrategie starten (QR-Karte, E-Mail-Vorlage, WhatsApp-Link)', priority: 'Hoch', effort: 'Gering' },
      { step: 'Phase 1', action: 'Google-Business-Profil vollständig optimieren', priority: 'Hoch', effort: 'Mittel' },
      { step: 'Phase 2', action: `Website-SEO-Basics: Title/Meta/H1 mit '${lead.keyword}'`, priority: 'Hoch', effort: 'Gering' },
      { step: 'Phase 2', action: 'LocalBusiness-Schema + Open-Graph-Tags einbauen', priority: 'Mittel', effort: 'Gering' },
      { step: 'Phase 3', action: 'Citations & lokale Backlinks aufbauen', priority: 'Mittel', effort: 'Mittel' },
    ],
  };

  const found = parseInt(scan.found_in) || 0;
  const greenPoints = solv > 0 ? Math.max(1, Math.round(gridPoints * solv / 100)) : 0;
  /* Erzähl-Stufe nach Marktposition: low = unsichtbar, mid = Aufholjagd, high = Marktführer absichern */
  const tier = solv >= 60 ? 'high' : solv >= 15 ? 'mid' : 'low';
  const noSite = !lead.domain;

  const scanCaption = tier === 'high'
    ? `<b>${greenPoints} von ${gridPoints} Punkten grün – du dominierst dein Einzugsgebiet.</b> Diese Spitzenposition ist bares Geld wert – und genau deshalb lohnt es sich jetzt, sie abzusichern und in Anfragen zu verwandeln.`
    : tier === 'mid'
      ? `<b>${greenPoints} von ${gridPoints} Punkten grün – eine solide Basis.</b> Aber an den gelben und roten Punkten gehen Kund:innen an den Wettbewerb verloren, obwohl sie nach '${lead.keyword.split(' ')[0]}' suchen.`
      : `<b>Nur ${greenPoints || 'kein einziger'} von ${gridPoints} Punkten grün.</b> An den roten Punkten stehst du jenseits von Position 10 – <b>dort wirst du praktisch nie gefunden</b>, obwohl die Menschen dort nach '${lead.keyword.split(' ')[0]}' suchen.`;
  const targetCaption = tier === 'high'
    ? `<b>Das Ziel: die Nr.-1-Position halten UND in Anfragen verwandeln.</b> ${noSite ? 'Ohne eigene Website und' : 'Mit'} ${(place.reviews || 0) < 15 ? 'mehr Bewertungen' : 'starken Bewertungen'} wird aus Sichtbarkeit planbarer Umsatz – bevor ein Wettbewerber die Lücke nutzt.`
    : `<b>Top-3-Sichtbarkeit im gesamten Einzugsgebiet.</b> Genau das haben die aktuellen Marktführer heute schon${compReviews.length ? ` – <b>mit nur ${revRange} Bewertungen</b>` : ''}. Diese Lücke ist mit sauberem Profil, Bewertungen und Website-Basics realistisch erreichbar.`;
  const letterP1 = `Dein${/praxis/i.test(lead.branch) ? 'e Praxis' : ' Unternehmen'} hat eine echte Stärke: ${place.rating ? `${parseFloat(place.rating).toFixed(1)} Sterne` : 'ein klares Angebot'} und ein klares Profil als ${lead.branch} in ${lead.city}.`;
  const letterP2 = tier === 'high'
    ? `Bei „${lead.keyword}“ bist du im Umkreis bereits die klare Nummer 1 (Ø Position ${arp.toFixed(1)}) – Glückwunsch! Genau jetzt entscheidet sich aber, ob aus dieser Sichtbarkeit auch Anfragen werden: ${noSite ? 'Ohne eigene Website und mit einem nicht beanspruchten Profil' : 'Mit den richtigen nächsten Schritten'} bleibt viel Potenzial liegen. Wir haben die wichtigsten Hebel zusammengefasst.`
    : tier === 'mid'
      ? `Bei „${lead.keyword}“ stehst du im Umkreis schon gut da (Ø Position ${arp.toFixed(1)}) – aber zwischen dir und der vollen Marktabdeckung liegt noch echtes Potenzial${topComp ? `, und Wettbewerber wie ${topComp.name} sind dir dicht auf den Fersen` : ''}. Wir haben uns deine Website, dein Google-Profil und deine lokale Sichtbarkeit angesehen und die wichtigsten Hebel zusammengefasst.`
      : `Gleichzeitig bleibt genau diese Stärke bei Google aktuell fast unsichtbar: Bei „${lead.keyword}“ erscheinst du im Umkreis ${found === 0 ? 'praktisch gar nicht' : `nur auf Ø Position ${arp.toFixed(0)}`}${topComp ? ` – während ${topComp.name} mit ${topComp.reviews} Bewertungen das Gebiet dominiert` : ''}. Wir haben uns ${noSite ? 'dein Google-Profil' : 'deine Website, dein Google-Profil'} und deine lokale Sichtbarkeit angesehen und die wichtigsten Hebel zusammengefasst.`;

  let out = tpl
    .replaceAll('__COMPANY__', lead.company).replaceAll('__FIRSTNAME__', lead.firstname)
    .replaceAll('__SLUG__', lead.slug).replaceAll('__CITY__', lead.city).replaceAll('__BRANCH__', lead.branch)
    .replaceAll('__KEYWORD__', lead.keyword).replaceAll('__SCAN_DATE__', today)
    .replaceAll('__GRID_POINTS__', String(gridPoints)).replaceAll('__RADIUS__', String(scan.radius || 7))
    .replaceAll('__MAPS_URL__', `https://www.google.com/maps/search/?api=1&amp;query=${encodeURIComponent(lead.company)}&amp;query_place_id=${place.place_id}`)
    .replaceAll('__WEBSITE_URL__', lead.domain ? `https://${lead.domain.replace(/^https?:\/\//, '')}/` : `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(lead.company)}&query_place_id=${place.place_id}`)
    .replaceAll('__SCAN_CAPTION__', scanCaption).replaceAll('__TARGET_CAPTION__', targetCaption)
    .replaceAll('__LETTER_P1__', letterP1).replaceAll('__LETTER_P2__', letterP2)
    .replace('__PROSPECT_JSON__', JSON.stringify(data, null, 2));
  return out;
}

/* =========================================================
 * 5) MAIN
 * ========================================================= */
(async () => {
  let lead, scan, place, speed, onpage;

  if (args.fixture) {
    const fx = JSON.parse(readFileSync(path.join(__dirname, args.fixture), 'utf8'));
    ({ lead, scan, place } = fx);
    if (args.slug) lead.slug = args.slug;
    log(`Fixture geladen: ${lead.company}`);
  } else {
    /* Scan wurde vorher in der Local-Falcon-UI (oder per MCP) gestartet.
       Hier reicht --report-key ODER --place-id (nimmt den neuesten Report). */
    let reportKey = args['report-key'];
    if (!reportKey && args['place-id']) {
      log(`Suche neuesten Report für place_id ${args['place-id']} …`);
      reportKey = await LF.latestReportForPlace(args['place-id']);
      if (!reportKey) fail('Kein Report für diese place_id gefunden — Scan zuerst in Local Falcon starten.');
    }
    if (!reportKey) fail('--report-key oder --place-id fehlt (Scan vorher in Local Falcon starten).');

    log(`Hole Report ${reportKey} …`);
    const report = await LF.getReport(reportKey);
    ({ scan, place } = LF.normalize(report));
    log(`Report: '${scan.keyword}' — Ø Pos. ${parseFloat(scan.arp).toFixed(1)}, SoLV ${parseFloat(scan.solv).toFixed(1)}% | ${place.name} (${place.reviews} Bew., ${place.rating}★)`);

    lead = {
      company: args.company || place.name,
      firstname: args.firstname || (args.name || args.company || place.name).split(' ')[0],
      city: args.city || (place.address.match(/\d{5}\s+([A-Za-zÄÖÜäöüß .-]+)/) || [])[1] || fail('--city fehlt (nicht aus Adresse ableitbar)'),
      branch: args.branch || 'Lokales Unternehmen',
      domain: args.domain || (args['no-website'] ? '' : fail('--domain fehlt (oder --no-website setzen)')),
      keyword: args.keyword || scan.keyword,
      email: args.email || '',
    };
    lead.slug = args.slug || slugify(lead.company);
  }

  if (lead.domain) {
    log('PageSpeed …'); speed = args.fixture ? (JSON.parse(readFileSync(path.join(__dirname, args.fixture), 'utf8')).speed || {}) : await pageSpeed(lead.domain);
    log('On-Page-Audit …'); onpage = args.fixture ? (JSON.parse(readFileSync(path.join(__dirname, args.fixture), 'utf8')).onpage || {}) : await onPageAudit(lead.domain);
  } else {
    log('Keine Website — überspringe PageSpeed & On-Page.'); speed = {}; onpage = { noSite: true, title: '', titleWeak: false, metaDesc: false, h1Count: 0, schema: false, ogCount: 0, imgTotal: 0, imgWithAlt: 0, https: false };
  }

  /* Seite schreiben */
  const html = composePage({ lead, scan, place, speed, onpage });
  const pageDir = path.join(ROOT, '04_site/review', lead.slug);
  mkdirSync(pageDir, { recursive: true });
  writeFileSync(path.join(pageDir, 'index.html'), html);
  log(`Seite geschrieben: 04_site/review/${lead.slug}/index.html`);

  /* Scan-Bild */
  const assetDir = path.join(ROOT, '04_site/public/review-assets', lead.slug);
  mkdirSync(assetDir, { recursive: true });
  if (scan.image || scan.image_url) {
    const imgUrl = scan.image || scan.image_url;
    const buf = Buffer.from(await (await fetch(imgUrl)).arrayBuffer());
    writeFileSync(path.join(assetDir, 'scan-grid.png'), buf);
    try { execSync(`cwebp -q 82 "${path.join(assetDir, 'scan-grid.png')}" -o "${path.join(assetDir, 'scan-grid.webp')}"`, { stdio: 'ignore' }); }
    catch { execSync(`cp "${path.join(assetDir, 'scan-grid.png')}" "${path.join(assetDir, 'scan-grid.webp')}"`); }
    log('Scan-Bild gespeichert & optimiert.');
  } else {
    log('⚠ Kein Scan-Bild im Report — Bild-URL manuell nachziehen.');
  }

  /* Build + Deploy */
  if (args.deploy) {
    log('Build + Deploy …');
    execSync('npm run build', { cwd: ROOT, stdio: 'inherit' });
    execSync('npm run deploy', { cwd: ROOT, stdio: 'inherit' });
  }

  /* Mail an den Lead */
  const pageUrl = `https://741.studio/review/${lead.slug}/`;
  if (args.send && lead.email) {
    const key = process.env.RESEND_API_KEY || fail('RESEND_API_KEY fehlt in .env');
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST', headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: '741.Studio <hello@741.studio>', to: [lead.email],
        subject: `Deine Sichtbarkeits-Analyse ist fertig, ${lead.firstname}!`,
        html: `<div style="font-family:-apple-system,Segoe UI,Roboto,sans-serif;max-width:560px">
          <h2>Hallo ${lead.firstname}, deine Analyse ist fertig! ✅</h2>
          <p>Wir haben deine Google-Sichtbarkeit in ${lead.city} analysiert – inklusive einer Karte, die zeigt, wo du heute stehst, wer dich verdrängt und welche drei Schritte den größten Hebel haben.</p>
          <p style="margin:24px 0"><a href="${pageUrl}" style="background:#fac118;color:#111;padding:12px 22px;border-radius:10px;text-decoration:none;font-weight:700">Deine persönliche Analyse ansehen →</a></p>
          <p style="color:#666;font-size:13px">Dein individuelles Analyse-Video wird gerade erstellt und erscheint in Kürze direkt auf der Seite.</p>
          <p style="color:#666;font-size:13px">Fragen? Antworte einfach auf diese E-Mail.<br>Martin · 741.Studio</p></div>`,
      }),
    });
    log(r.ok ? `Mail an ${lead.email} gesendet.` : `⚠ Mail-Fehler: ${await r.text()}`);
  }

  console.log(`\n✅ Fertig: ${pageUrl}${args.deploy ? ' (live)' : ' (lokal — mit --deploy veröffentlichen)'}`);
})();
