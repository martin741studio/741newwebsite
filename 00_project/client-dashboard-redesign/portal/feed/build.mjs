#!/usr/bin/env node
/**
 * Weekly refresh job for a client dashboard feed (dashboard.json). One config file per client: feed/clients/<slug>.json.
 *
 *   node portal/feed/build.mjs [--client bali|huewel] [--as-of YYYY-MM-DD] [--base file] [--out file] [--ads-file file] [--no-points]
 *
 * READ-ONLY. It reads Search Console, GA4, Local Falcon (read tools only, free), the portal database (GET only) and the saved Ads snapshot file.
 * It writes only inside portal/feed/out/<slug>/ and portal/feed/data/<slug>/. It does NOT upload, does NOT touch the live portal,
 * does NOT run scans and makes no paid call.
 *
 * Rules: a number that cannot be read stays null (never an estimate). A block whose source fails keeps the value of the
 * base feed, is listed in meta.refresh.failed, and the job exits with code 2. Hand-written blocks are carried over from
 * the base feed unchanged (listed in meta.refresh.carried).
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, resolve } from 'node:path';
import { lfCall } from './lf.mjs';
import { gsc as gscRaw, ga4 as ga4Raw } from './google.mjs';
import { sbGet as sbGetRaw } from './supabase.mjs';
import { diffLines } from './diff.mjs';

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = join(HERE, '../../../..');
const arg = (n, d) => { const i = process.argv.indexOf('--' + n); return i < 0 ? d : (process.argv[i + 1] && !process.argv[i + 1].startsWith('--') ? process.argv[i + 1] : true); };

/* ---------- client config ---------- */
const SLUG = arg('client', 'bali');
const CFG_FILE = join(HERE, 'clients', `${SLUG}.json`);
if (!existsSync(CFG_FILE)) { console.error(`No config file ${CFG_FILE}`); process.exit(1); }
const CFG = JSON.parse(readFileSync(CFG_FILE, 'utf8'));
const LANG = CFG.lang === 'de' ? 'de' : 'en';
const PROFILES = CFG.profiles, PRIMARY = PROFILES[0].key;
const FILL_DAYS = CFG.fill_days ?? 3;
const USE_LF = CFG.local_falcon !== false;                                         // false: no Local Falcon call at all (profile actions, reviews, map, leader, AI)
const GRID = CFG.map.grid_points;
if (CFG.domain && CFG.gsc_site && !new URL(CFG.gsc_site).hostname.replace(/^www\./, '').endsWith(CFG.domain)) { console.error(`Guard: gsc_site ${CFG.gsc_site} does not belong to domain ${CFG.domain}. Nothing written.`); process.exit(1); }
const BASE_FILE = arg('base', resolve(HERE, CFG.base));
const SNAPSHOT_FILE = CFG.snapshot ? resolve(HERE, CFG.snapshot) : null;
const OUT_FILE = arg('out', join(HERE, 'out', SLUG, 'dashboard.json'));
const DATA = join(HERE, 'data', SLUG);
mkdirSync(join(DATA, CFG.local_falcon === false ? '.' : 'scans'), { recursive: true }); mkdirSync(dirname(OUT_FILE), { recursive: true });

/* ---------- language of the texts the job writes ---------- */
const MONTHS = { en: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], de: ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'] };
const MON = MONTHS[LANG];
const nf = (n, dec = 0) => new Intl.NumberFormat(LANG === 'de' ? 'de-DE' : 'en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec }).format(n);
const T = {
  en: {
    partial: (d, m) => `1–${d} ${m}`, dMon: (d, m) => `${d} ${m}`, range: (a, b) => `${a} to ${b}`,
    today: 'today, ', roadmap: 'Roadmap with status.',
    src_profile: 'Google profile data (calls, website visits, direction requests)', src_profile_note: n => `Newest ${n} days (from DATE) can still grow.`,
    src_wa: 'Google Analytics (taps on WhatsApp links on the website)', src_wa_note: d => `Counted since ${d}. Counts the tap, not the chat.`,
    src_gsc: 'Google Search Console (clicks and average position in Google Search)', src_gsc_note: 'Final data for full months. Average position of the last full month.',
    src_rev: 'Google profile reviews (live list)', src_rev_note: 'New reviews per month counted by the date Google shows (local time).',
    src_map: 'Google Maps checks (49 spots around the practice, top-3 coverage)', src_map_note: 'Latest check per keyword. Check dates differ. Check settings can differ between keywords.',
    src_leader: 'Google Maps check, competitor with the highest top-3 share for the main keyword', leader_note: d => `Scan of ${d}.`, src_ai: 'AI answer checks (ChatGPT, Gemini, Google AI mode), 9 spots per keyword', ai_note: (a, b) => `Run of ${a}${b && b !== a ? ' to ' + b : ''}. One run: no trend before 3 runs.`,
    src_ads: d => `Google Ads account (saved read of ${d})`, src_ads_note: 'Campaign cost without tax. All time since the first ad. Not read live.',
    src_cit: 'Directory entries in the 741 portal (status per directory)', src_reports: 'Reports published in the 741 portal',
    source_note: (d, o) => {
      const parts = [...(o.gsc ? ['Google Search Console'] : []), ...(o.ga4 ? ['Google Analytics'] : []), ...(o.profiles ? ['the Google profiles'] : []), ...(o.ads ? ['the Google Ads account'] : [])];
      const list = parts.length > 1 ? `${parts.slice(0, -1).join(', ')} and ${parts[parts.length - 1]}` : parts[0];
      const portal = [...(o.reviews ? ['reviews'] : []), ...(o.citations ? ['directory entries'] : [])];
      return `${parts.length ? `Numbers read ${d} from ${list}${o.adsAt ? ` (Ads read ${o.adsAt})` : ''}.` : ''}${portal.length ? `${parts.length ? ' ' : ''}${portal.join(' and ').replace(/^./, c => c.toUpperCase())} from the 741 portal.` : ''}`;
    },
    reviewLine: (n, replied, total) => `<b>Reply to the ${n === 1 ? 'newest review' : n + ' newest reviews'}.</b> ${replied} of ${total} reviews have a reply. The newest do not.`,
    fill_note: 'Google can add the newest days late. Numbers for these days can still grow.',
    erg: {
      title: 'Before and after: the first 30 days', clicks: 'Clicks from Google Search', impressions: 'Times shown in Google Search', ctr: 'Click rate', position: 'Average position in Google Search',
      reviews: 'Google reviews', citations: 'Directory entries live', src_gsc: 'Google Search Console', src_rev: 'Google profile reviews', src_cit: '741 portal',
      note_event: (d, w, pos) => `The website moved on ${d}. For ${w} Google shows an average position of ${pos}.`,
      note_reviews: 'Counted from the review list as it is today. Deleted reviews are not visible.', src_rev_portal: d => `Google reviews, measured ${d} (741 portal)`, note_reviews_portal: 'Stored measurement, confirmed by 741.', note_cit: 'The portal stores the status today, not its history. No value before the start.'
    }
  },
  de: {
    partial: (d, m) => `1.–${d}. ${m}`, dMon: (d, m) => `${d}. ${m}${m === 'Mai' ? '' : '.'}`, range: (a, b) => `${a} bis ${b}`,
    today: 'heute, ', roadmap: 'Fahrplan mit Status.',
    src_profile: 'Google-Profil-Daten (Anrufe, Website-Besuche, Routenanfragen)', src_profile_note: n => `Die neuesten ${n} Tage (ab DATE) können noch steigen.`,
    src_wa: 'Google Analytics (Klicks auf WhatsApp-Links der Website)', src_wa_note: d => `Gezählt seit ${d}${d.endsWith('.') ? '' : '.'} Gezählt wird der Klick, nicht das Gespräch.`,
    src_gsc: 'Google Search Console (Klicks und Durchschnittsposition in der Google-Suche)', src_gsc_note: 'Endgültige Daten für volle Monate. Durchschnittsposition des letzten vollen Monats.',
    src_rev: 'Google-Bewertungen des Profils (aktuelle Liste)', src_rev_note: 'Neue Bewertungen pro Monat nach dem Datum, das Google zeigt (Ortszeit).',
    src_map: 'Google-Maps-Prüfungen (49 Punkte rund um die Praxis, Top-3-Abdeckung)', src_map_note: 'Neueste Prüfung je Suchbegriff. Die Prüfdaten unterscheiden sich. Die Einstellungen können je Suchbegriff abweichen.',
    src_leader: 'Google-Maps-Prüfung, Wettbewerber mit dem höchsten Top-3-Anteil für den wichtigsten Suchbegriff', leader_note: d => `Prüfung vom ${d}${d.endsWith('.') ? '' : '.'}`, src_ai: 'KI-Antwort-Prüfungen (ChatGPT, Gemini, Google KI-Modus)', ai_note: (a, b) => `Lauf vom ${a}${b && b !== a ? ' bis ' + b : ''}. Ein Lauf: kein Verlauf vor 3 Läufen.`,
    src_ads: d => `Google-Ads-Konto (gespeicherter Abruf vom ${d})`, src_ads_note: 'Kampagnenkosten ohne Steuer. Gesamtzeit seit der ersten Anzeige. Nicht live gelesen.',
    src_cit: 'Verzeichniseinträge im 741-Portal (Status je Verzeichnis)', src_reports: 'Berichte im 741-Portal',
    source_note: (d, o) => {
      const parts = [...(o.gsc ? ['der Google Search Console'] : []), ...(o.ga4 ? ['Google Analytics'] : []), ...(o.profiles ? ['den Google-Profilen'] : []), ...(o.ads ? ['dem Google-Ads-Konto'] : [])];
      const list = parts.length > 1 ? `${parts.slice(0, -1).join(', ')} und ${parts[parts.length - 1]}` : parts[0];
      const portal = [...(o.reviews ? ['Bewertungen'] : []), ...(o.citations ? ['Eintragsstände'] : [])];
      return `${parts.length ? `Zahlen gelesen am ${d} aus ${list}${o.adsAt ? ` (Ads gelesen am ${o.adsAt})` : ''}.` : ''}${portal.length ? `${parts.length ? ' ' : ''}${portal.join(' und ')} aus dem 741-Portal.` : ''}`;
    },
    reviewLine: (n, replied, total) => `<b>Antworte auf die ${n === 1 ? 'neueste Bewertung' : n + ' neuesten Bewertungen'}.</b> ${replied} von ${total} Bewertungen haben eine Antwort. Die neuesten nicht.`,
    fill_note: 'Google trägt die neuesten Tage verspätet nach. Die Zahlen dieser Tage können noch steigen.',
    erg: {
      title: 'Vorher und nachher: die ersten 30 Tage', clicks: 'Klicks aus der Google-Suche', impressions: 'Einblendungen in der Google-Suche', ctr: 'Klickrate', position: 'Durchschnittliche Position in der Google-Suche',
      reviews: 'Google-Bewertungen', citations: 'Verzeichniseinträge online', src_gsc: 'Google Search Console', src_rev: 'Google-Bewertungen des Profils', src_cit: '741-Portal',
      note_event: (d, w, pos) => `Die Website ist am ${d} umgezogen. Für ${w} zeigt Google eine Durchschnittsposition von ${pos}.`,
      note_reviews: 'Gezählt aus der Bewertungsliste von heute. Gelöschte Bewertungen sind nicht sichtbar.', src_rev_portal: d => `Google-Bewertungen, Messung vom ${d} (741-Portal)`, note_reviews_portal: 'Gespeicherte Messung, von 741 bestätigt.', note_cit: 'Das Portal speichert den Status von heute, keinen Verlauf. Für die Zeit vor dem Start gibt es keinen Wert.'
    }
  }
}[LANG];
Object.assign(T, CFG.texts || {});                                              // a client config can override single texts

/* ---------- date helpers (all ISO strings, client time zone) ---------- */
const fmtYmd = new Intl.DateTimeFormat('en-CA', { timeZone: CFG.tz });
const ymd = d => fmtYmd.format(d);
const utc = s => new Date(s + 'T00:00:00Z');
const addDays = (s, n) => { const d = utc(s); d.setUTCDate(d.getUTCDate() + n); return d.toISOString().slice(0, 10); };
const daysBetween = (a, b) => Math.round((utc(b) - utc(a)) / 864e5);
const dMon = s => T.dMon(+s.slice(8), MON[+s.slice(5, 7) - 1]);
const dMonY = s => `${dMon(s)} ${s.slice(0, 4)}`;
const monthEnd = (y, m) => new Date(Date.UTC(y, m, 0)).toISOString().slice(0, 10);   // m = 1..12
const pad = n => String(n).padStart(2, '0');
const AS_OF = arg('as-of', ymd(new Date()));
const FILL_FROM = addDays(AS_OF, -(FILL_DAYS - 1));
const SETTLED_TO = addDays(AS_OF, -FILL_DAYS);

const [ay, am] = [+AS_OF.slice(0, 4), +AS_OF.slice(5, 7)];
const months = [];                                                              // 6 full months, then the running month
for (let i = 6; i >= 1; i--) {
  let y = ay, m = am - i; while (m < 1) { m += 12; y--; }
  months.push({ y, m, start: `${y}-${pad(m)}-01`, end: monthEnd(y, m), label: MON[m - 1], partial: false });
}
months.push({ y: ay, m: am, start: `${ay}-${pad(am)}-01`, end: AS_OF, label: T.partial(+AS_OF.slice(8), MON[am - 1]), partial: true });
const monthOf = d => months.findIndex(x => d >= x.start && d <= x.end);

/* ---------- misc helpers ---------- */
const log = (...a) => console.error('[feed]', ...a);
const retry = async (fn, n = 3) => { let e; for (let i = 0; i < n; i++) { try { return await fn(); } catch (x) { e = x; if (/refused/.test(x.message)) throw x; await new Promise(r => setTimeout(r, (/quota|429|rate/i.test(x.message) ? 25000 : 1500) * (i + 1))); } } throw e; };   // a quota message waits longer
const lf = (name, args) => retry(() => lfCall(name, args));
const gsc = (...a) => retry(() => gscRaw(...a)), ga4 = (...a) => retry(() => ga4Raw(...a)), sbGet = (...a) => retry(() => sbGetRaw(...a));   // a short Google or portal hiccup should not drop a block
const num = v => (v === false || v === null || v === undefined || v === '' ? null : Number.isFinite(+v) ? +v : null);
const save = (rel, obj) => { const p = join(DATA, rel); mkdirSync(dirname(p), { recursive: true }); writeFileSync(p, JSON.stringify(obj, null, 1)); };
const tsToLocal = ts => ymd(new Date(+ts * 1000));                              // LF dates are US Eastern; the unix timestamp is exact
const base = JSON.parse(readFileSync(BASE_FILE, 'utf8'));
const snapshot = SNAPSHOT_FILE ? JSON.parse(readFileSync(SNAPSHOT_FILE, 'utf8')) : (existsSync(OUT_FILE) ? JSON.parse(readFileSync(OUT_FILE, 'utf8')) : {});
const feed = JSON.parse(JSON.stringify(base));                                  // start from the curated feed, then overwrite measured blocks
feed.months = months.map(m => m.label);
const failed = [], warn = [], gaps = [];
const sources = {};
const derived = {};
const r1 = x => +x.toFixed(1);
const orderLike = (prevRows, key) => { const m = new Map((prevRows || []).map((r, i) => [r[0], i])); return r => (m.has(key(r)) ? m.get(key(r)) : 1e6); };
const SUFFIX = new RegExp(CFG.map.suffix.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$', 'i');
const norm = kw => { const k = kw.replace(SUFFIX, '').trim().toLowerCase(); return CFG.map.alias[k] || k; };

async function block(name, fn) {
  try { await fn(); log('ok  ', name); }
  catch (e) {
    const msg = String(e.message);
    if (/\b403\b|PERMISSION_DENIED|sufficient permission|not have access|not connected to a Google account|no location in review list/i.test(msg)) { gaps.push(name); log('GAP ', name, '- no access or not connected. The block stays empty.'); warn.push(`${name}: no access or not connected, block stays empty`); return; }   // a missing grant is a known gap, not a failed run
    failed.push(name); log('FAIL', name, '-', msg.slice(0, 200)); warn.push(`${name}: ${msg.slice(0, 160)}`);
  }
}

/* ---------- 1. Google profile actions (calls, website clicks, directions), every profile ---------- */
const perfDaily = {};
if (USE_LF) await block('profile_actions', async () => {
  const out = {};
  for (const { key: k, place_id: id } of PROFILES) {
    const r = await lf('getLocalFalconGbpPerformanceMetrics', { placeId: id, metrics: 'CALL_CLICKS,WEBSITE_CLICKS,BUSINESS_DIRECTION_REQUESTS', startDate: months[0].start, endDate: AS_OF });
    const days = (r.data?.days || []).map(d => ({ date: d.date, calls: num(d.metrics.CALL_CLICKS), web: num(d.metrics.WEBSITE_CLICKS), dir: num(d.metrics.BUSINESS_DIRECTION_REQUESTS) }));
    if (!days.length) throw new Error(`no days for ${k}`);
    perfDaily[k] = days; save(`profile-actions-${k}.json`, { profile: k, read_on: AS_OF, start: months[0].start, end: AS_OF, filling_from: FILL_FROM, days });
    const agg = { calls: [], web: [], dir: [] };
    months.forEach(m => {
      const need = daysBetween(m.start, m.end) + 1, ds = days.filter(d => d.date >= m.start && d.date <= m.end);
      const full = ds.length === need;                                          // a missing day is not a zero: the month stays null
      for (const f of ['calls', 'web', 'dir']) agg[f].push(full && ds.every(d => d[f] !== null) ? ds.reduce((s, d) => s + d[f], 0) : null);
    });
    out[k] = agg;
  }
  for (const k of Object.keys(out)) feed[k] = out[k];
  feed.months = months.map(m => m.label);
  // settled part of the running month (without the days that can still grow)
  const settled = {};
  for (const k of Object.keys(CFG.profiles.reduce((o, p) => (o[p.key] = 1, o), {}))) {
    const ds = perfDaily[k].filter(d => d.date >= months[6].start && d.date <= SETTLED_TO);
    settled[k] = ds.length ? { calls: ds.reduce((s, d) => s + d.calls, 0), web: ds.reduce((s, d) => s + d.web, 0), dir: ds.reduce((s, d) => s + d.dir, 0) } : null;
  }
  derived.running_month_settled = { from: months[6].start, to: SETTLED_TO, ...settled };
  sources.profile_actions = { source: T.src_profile, read: AS_OF, note: T.src_profile_note(FILL_DAYS).replace('DATE', FILL_FROM) };
});

/* ---------- 2. Website contact events (GA4): WhatsApp taps = feed.wa; more events for clients that track them ---------- */
if (CFG.ga4) await block('whatsapp', async () => {
  const G = CFG.ga4, events = [G.wa_event, ...(G.extra_events || [])];
  const run = async ev => {
    const r = await ga4(G.property, { dateRanges: [{ startDate: G.tracking_start, endDate: AS_OF }], dimensions: [{ name: 'date' }], metrics: [{ name: 'eventCount' }],
      dimensionFilter: { filter: { fieldName: 'eventName', stringFilter: { matchType: 'EXACT', value: ev } } }, orderBys: [{ dimension: { dimensionName: 'date' } }], limit: 1000 });
    return (r.rows || []).map(x => { const d = x.dimensionValues[0].value; return { date: `${d.slice(0, 4)}-${d.slice(4, 6)}-${d.slice(6)}`, taps: +x.metricValues[0].value }; });
  };
  const monthly = days => months.map(m => {
    if (m.end < G.tracking_start) return null;                                  // before the tracking start: not tracked, not zero
    return days.filter(d => d.date >= m.start && d.date <= m.end).reduce((s, d) => s + d.taps, 0);
  });
  const all = {};
  for (const ev of events) all[ev] = await run(ev);
  save('ga4-whatsapp-daily.json', { property: G.property, event: G.wa_event, read_on: AS_OF, tracking_start: G.tracking_start, days: all[G.wa_event] });
  if (G.extra_events?.length) save('ga4-events-daily.json', { property: G.property, read_on: AS_OF, tracking_start: G.tracking_start, events: all });
  feed.wa = monthly(all[G.wa_event]);
  if (G.extra_events?.length) feed.ga4_events = Object.fromEntries(events.map(ev => [ev, monthly(all[ev])]));
  sources.whatsapp = { source: T.src_wa, read: AS_OF, note: T.src_wa_note(dMon(G.tracking_start)) };
});

/* ---------- 3. Search Console ---------- */
if (CFG.gsc_site) await block('search_console', async () => {
  const last = months[5], prev = months[4], prev2 = months[3];
  const curEnd = addDays(AS_OF, -2);                                           // Search Console lags about 2 days
  const daily = await gsc(CFG.gsc_site, { startDate: months[0].start, endDate: curEnd, dimensions: ['date'], dataState: 'all', rowLimit: 1000 });
  const firstDay = daily.rows?.[0]?.keys[0] ?? null;                           // first day with data: a month before it has no data (null), a later month without rows is a real zero
  save('gsc-daily.json', { site: CFG.gsc_site, read_on: AS_OF, days: (daily.rows || []).map(r => ({ date: r.keys[0], clicks: r.clicks, impressions: r.impressions, position: +r.position.toFixed(2) })) });
  const q = async (s, e, st) => {
    const r = await gsc(CFG.gsc_site, { startDate: s, endDate: e, dataState: st });
    if (r.rows?.[0]) return r.rows[0];
    return firstDay && e >= firstDay ? { clicks: 0, impressions: 0, position: null } : null;
  };
  const covered = m => !!firstDay && firstDay <= m.start;                       // a month that starts before the first day of data is only partly covered: it stays null
  const [a, b, c] = [covered(last) ? await q(last.start, last.end, 'final') : null, covered(prev) ? await q(prev.start, prev.end, 'final') : null, covered(prev2) ? await q(prev2.start, prev2.end, 'final') : null];
  if (!a) throw new Error('no complete Search Console month yet (first day of data: ' + firstDay + ')');
  let cur = null; if (curEnd >= months[6].start) cur = await q(months[6].start, curEnd, 'all');
  const pos = x => (x && x.position != null ? r1(x.position) : null), val = (x, k) => (x ? x[k] : null);
  feed.gsc = { sep: a.clicks, aug: val(b, 'clicks'), jul: val(c, 'clicks'), pos: pos(a), posJul: pos(c) };   // key names are fixed by the feed schema: last full month, the month before, two before
  derived.gsc = { months: [prev2.label, prev.label, last.label], impressions: [val(c, 'impressions'), val(b, 'impressions'), a.impressions], position: [pos(c), pos(b), pos(a)],
    running_month: cur ? { from: months[6].start, to: curEnd, clicks: cur.clicks, impressions: cur.impressions, position: pos(cur) } : null };
  sources.search_console = { source: T.src_gsc, read: AS_OF, note: T.src_gsc_note };
});

/* ---------- 4. Reviews, every profile ---------- */
const reviewData = {};
if (USE_LF) await block('reviews', async () => {
  for (const { key: k, place_id: id } of PROFILES) {
    let tok = null, all = [], total = null, avg = null;
    do {
      const r = await lf('listLocalFalconGbpReviews', { placeId: id, limit: 100, ...(tok ? { nextToken: tok } : {}) });
      const loc = r.data?.locations?.[0]; if (!loc) throw new Error('no location in review list');
      total = num(loc.total_reviews); avg = num(loc.average_rating);
      all.push(...loc.reviews.map(x => ({ date: ymd(new Date(x.date_created)), rating: x.rating, replied: x.reply !== false && x.reply !== null && x.reply !== undefined, reply_date: x.reply_date ? ymd(new Date(x.reply_date)) : null })));
      tok = loc.next_token || null;
    } while (tok && all.length < 2000);
    if (total === null) throw new Error('no location in review list (the Google listing is not connected)');
    if (all.length !== total) throw new Error(`${k}: read ${all.length} of ${total} reviews`);
    all.sort((x, y) => y.date.localeCompare(x.date));
    reviewData[k] = { n: total, star: avg, list: all };
    save(`reviews-${k}.json`, { profile: k, read_on: AS_OF, total_reviews: total, average_rating: avg, reviews: all });   // no names, no texts
  }
  const R = reviewData, unans = k => R[k].list.filter(x => !x.replied).length;
  const labels = [], per = [];                                                  // new reviews per month of the year of the last full month
  const ly = months[5].y; for (let m = 1; m <= months[5].m; m++) { labels.push(MON[m - 1]); per.push(R[PRIMARY].list.filter(x => x.date.startsWith(`${ly}-${pad(m)}`)).length); }
  feed.rev = {};
  for (const { key: k } of PROFILES) {
    feed.rev[k] = k === PRIMARY ? { n: R[k].n, star: R[k].star, unans: unans(k), leader: base.rev?.[k]?.leader ?? null, months: labels, per } : { n: R[k].n, star: R[k].star, unans: unans(k) };
  }
  let streak = 0; for (const x of R[PRIMARY].list) { if (x.replied) break; streak++; }
  derived.reviews = {};
  for (const { key: k } of PROFILES) {
    derived.reviews[k] = k === PRIMARY ? { replied: R[k].n - unans(k), newest_without_reply: streak, latest_without_reply: R[k].list.find(x => !x.replied)?.date ?? null, newest_review: R[k].list[0]?.date ?? null } : { replied: R[k].n - unans(k) };
  }
  sources.reviews = { source: T.src_rev, read: AS_OF, note: T.src_rev_note };
});

/* ---------- 5. Map scans (latest per keyword) + save the 49 grid points ---------- */
async function listReports(placeId, platform) {
  let tok = null, out = [];
  do {
    const r = await lf('listLocalFalconScanReports', { placeId, ...(platform ? { platform } : {}), ...(tok ? { nextToken: tok } : {}),
      fieldmask: 'report_key,date,timestamp,keyword,arp,atrp,solv,found_in,grid_size,radius,measurement,platform,place_id' });
    out.push(...(r.reports || [])); tok = r.next_token || null;
  } while (tok);
  return out.map(x => ({ ...x, bali_date: tsToLocal(x.timestamp), grid: +x.grid_size, radius_txt: `${+x.radius} ${x.measurement}` }));
}
const trimPoints = pts => pts.map(p => ({ lat: num(p.lat), lng: num(p.lng), found: !!p.found, rank: num(p.rank), top: (p.results || []).slice(0, 5).map(r => ({ rank: r.rank, place_id: r.place_id, name: r.name, rating: num(r.rating), reviews: num(r.reviews) })) }));
async function ensurePoints(rep) {
  const file = join(DATA, 'scans', `${rep.report_key}.json`);
  if (existsSync(file)) return JSON.parse(readFileSync(file, 'utf8'));
  const r = await lf('getLocalFalconReport', { reportKey: rep.report_key, fieldmask: 'report_key,date,timestamp,platform,keyword,place_id,lat,lng,grid_size,radius,measurement,arp,atrp,solv,found_in,data_points' });
  if (!Array.isArray(r.data_points) || !r.data_points.length) throw new Error(`no data_points for ${rep.report_key}`);
  const rec = { report_key: rep.report_key, keyword: r.keyword, platform: r.platform, place_id: r.place_id, scan_date_bali: rep.bali_date, lf_date_us_eastern: r.date, timestamp: r.timestamp,
    grid_size: +r.grid_size, radius: r.radius, measurement: r.measurement, center: { lat: num(r.lat), lng: num(r.lng) }, arp: num(r.arp), atrp: num(r.atrp), solv: num(r.solv), found_in: num(r.found_in),
    saved_on: AS_OF, data_points: trimPoints(r.data_points) };
  writeFileSync(file, JSON.stringify(rec)); return rec;
}
const latestPerKeyword = (reps, keep) => { const m = new Map(); for (const r of reps.filter(keep).sort((a, b) => b.timestamp - a.timestamp)) { const k = norm(r.keyword); if (!m.has(k)) m.set(k, r); } return m; };
const scanIdx = {};
if (USE_LF && CFG.map_enabled !== false) await block('map_scans', async () => {
  const keep = r => daysBetween(r.bali_date, AS_OF) <= CFG.map.max_age_days && r.grid * r.grid === GRID;
  const skipped = [], detail = {};
  for (const { key: k, place_id: id } of PROFILES) {
    const reps = await listReports(id, 'google'); scanIdx[k] = reps; save(`scans-index-${k}.json`, { profile: k, read_on: AS_OF, reports: reps });
    reps.filter(r => daysBetween(r.bali_date, AS_OF) <= CFG.map.max_age_days && r.grid * r.grid !== GRID).forEach(r => skipped.push(`${k}:${r.keyword} (${r.grid}x${r.grid})`));
    const pick = [...latestPerKeyword(reps, keep).entries()];
    detail[k] = [];
    for (const [name, rep] of pick) {
      let top3 = null, pts = null;
      if (!arg('no-points', false)) { try { pts = await ensurePoints(rep); } catch (e) { warn.push(`points ${rep.report_key}: ${e.message.slice(0, 100)}`); } }
      if (pts && pts.data_points.length === GRID) top3 = pts.data_points.filter(p => p.found && p.rank <= 3).length;
      const bySolv = Math.round(num(rep.solv) * GRID / 100);
      if (top3 === null) { top3 = bySolv; warn.push(`${k}:${name} top-3 count taken from the share value (no grid points)`); }
      else if (top3 !== bySolv) warn.push(`${k}:${name} top-3 count ${top3} differs from share ${rep.solv}% (${bySolv})`);
      detail[k].push({ name, keyword: rep.keyword, top3, of: GRID, date: rep.bali_date, found_in: num(rep.found_in), arp: num(rep.arp), atrp: num(rep.atrp), solv: num(rep.solv), grid: `${rep.grid}x${rep.grid}`, radius: rep.radius_txt });
    }
  }
  const ord = orderLike(base.map, r => r[0]);
  feed.map = detail[PRIMARY].map(d => [d.name, d.top3, dMon(d.date)]).sort((a, b) => b[1] - a[1] || ord(a) - ord(b) || a[0].localeCompare(b[0]));
  for (const p of PROFILES.filter(p => p.zero_list)) {
    const ordB = orderLike((base[p.zero_list] || []).map(x => [x]), r => r[0]);
    feed[p.zero_list] = detail[p.key].filter(d => d.top3 === 0).map(d => d.name).sort((a, b) => ordB([a]) - ordB([b]) || a.localeCompare(b));
  }
  derived.map_detail = detail; derived.map_skipped_other_grid = skipped;
  for (const p of PROFILES.slice(1)) derived[`${p.key}_found`] = detail[p.key].filter(d => d.top3 > 0).map(d => [d.name, d.top3, dMon(d.date)]);
  const settings = new Set(detail[PRIMARY].map(d => `${d.grid} ${d.radius}`)); derived.map_settings_mixed = settings.size > 1;
  // same-setting series for the main keyword
  const L = CFG.leader;
  if (L) {
    const oz = scanIdx[PRIMARY].filter(r => norm(r.keyword) === L.keyword && r.grid * r.grid === GRID && r.radius_txt === L.series_radius).sort((a, b) => a.timestamp - b.timestamp);
    derived[L.series_key] = oz.map(r => ({ date: r.bali_date, top3: Math.round(num(r.solv) * GRID / 100), of: GRID, solv: num(r.solv), arp: num(r.arp) }));
  }
  sources.map = { source: T.src_map, read: AS_OF, note: T.src_map_note };
});

/* ---------- 6. Local leader (main keyword): review count ---------- */
if (CFG.leader && USE_LF) await block('leader', async () => {
  const reps = scanIdx[PRIMARY] || await listReports(PROFILES[0].place_id, 'google');
  const rep = reps.filter(r => norm(r.keyword) === CFG.leader.keyword).sort((a, b) => b.timestamp - a.timestamp)[0];
  if (!rep) throw new Error('no scan for the main keyword');
  const r = await lf('getLocalFalconReport', { reportKey: rep.report_key, fieldmask: 'report_key,date,timestamp,places' });
  const ownId = PROFILES[0].place_id;
  const pl = Object.values(r.places || {}).filter(p => p.place_id !== ownId).sort((a, b) => num(b.solv) - num(a.solv));
  if (!pl.length) throw new Error('no competitor places');
  const top = pl[0], own = (r.places || {})[ownId];
  if (feed.rev?.[PRIMARY]) feed.rev[PRIMARY].leader = num(top.reviews);
  derived.leader = { keyword: CFG.leader.keyword, name: top.name, reviews: num(top.reviews), rating: num(top.rating), top3_share: num(top.solv), scan_date: rep.bali_date, own_reviews_at_scan: num(own?.reviews) };
  sources.leader = { source: T.src_leader, read: AS_OF, note: T.leader_note(dMon(rep.bali_date)) };
});

/* ---------- 7. AI answers (latest run per keyword and AI tool) ---------- */
if (CFG.ai && USE_LF) await block('ai_answers', async () => {
  const plat = { chatgpt: new Map(), gemini: new Map(), aimode: new Map() }; let first = null, lastD = null;
  for (const p of Object.keys(plat)) {
    const reps = await listReports(PROFILES[0].place_id, p); save(`scans-index-${PRIMARY}-${p}.json`, { platform: p, read_on: AS_OF, reports: reps });
    for (const [k, r] of latestPerKeyword(reps, () => true)) { plat[p].set(k, r); first = !first || r.bali_date < first ? r.bali_date : first; lastD = !lastD || r.bali_date > lastD ? r.bali_date : lastD; }
  }
  const names = [...new Set(Object.values(plat).flatMap(m => [...m.keys()]))];
  const val = (p, k) => { const r = plat[p].get(k); return r ? num(r.solv) : null; };
  const rows = names.map(k => [k, val('chatgpt', k), val('gemini', k), val('aimode', k)]);
  const ord = orderLike(base.ai, r => r[0]);
  feed.ai = rows.sort((a, b) => ord(a) - ord(b) || a[0].localeCompare(b[0]));
  const mean = i => { const v = rows.map(r => r[i]).filter(x => x !== null); return v.length ? +(v.reduce((s, x) => s + x, 0) / v.length).toFixed(1) : null; };
  derived.ai = { from: first, to: lastD, runs_per_cell: 1, samples_per_cell: 9, platform_means: { chatgpt: mean(1), gemini: mean(2), ai_mode: mean(3) } };
  sources.ai_answers = { source: T.src_ai, read: AS_OF, note: T.ai_note(dMon(first), dMon(lastD)) };
});

/* ---------- 8. Ads (saved snapshot file, no live read) ---------- */
if (CFG.ads) await block('ads', async () => {
  const dir = join(ROOT, CFG.ads.dir);
  const f = arg('ads-file', null) || join(dir, readdirSync(dir).filter(n => /^ads-read-\d{4}-\d{2}-\d{2}\.json$/.test(n)).sort().pop());
  const j = JSON.parse(readFileSync(f, 'utf8')), at = j.collected_at.slice(0, 10), cs = j.campaigns || [];
  if (!cs.length) throw new Error('no campaigns in ads file');
  const sum = k => cs.reduce((s, c) => s + (num(c.all_time?.[k]) ?? 0), 0);
  const spent = sum('cost_idr'), clicks = sum('clicks'), imp = sum('impressions'), wa = sum('conversions');
  feed.ads = { spent, clicks, wa, per: wa ? Math.round(spent / wa) : null, cpc: clicks ? Math.round(spent / clicks) : null, imp };
  const age = daysBetween(at, AS_OF);
  derived.ads = { snapshot_file: f.replace(ROOT + '/', ''), snapshot_date: at, age_days: age, last_7_days: j.last_7_days_2026_10_06_to_12 ?? null, billing_net_cost_idr: j.billing?.net_cost_idr ?? null };
  if (age > CFG.ads.max_age_days) warn.push(`ads snapshot is ${age} days old (${at}). Numbers are as of ${at}.`);
  sources.ads = { source: T.src_ads(dMonY(at)), read: at, note: T.src_ads_note };
});

/* ---------- 9. Portal database (read only): directory entries and reports ---------- */
let citationRows = null, portalReports = null;
if (CFG.citations) await block('citations', async () => {
  citationRows = await sbGet(`client_citations?client_id=eq.${CFG.client_id}&select=status`);
  const by = {}; citationRows.forEach(x => { by[x.status] = (by[x.status] || 0) + 1; });
  feed.citations = citationRows.length ? { live: by.live || 0, total: citationRows.length, by_status: by, read: AS_OF } : null;   // no rows = no data, not zero
  sources.citations = { source: T.src_cit, read: AS_OF, note: '' };
});
if (CFG.reports_from_portal || CFG.last_update?.type === 'client_reports') await block('portal_reports', async () => {
  portalReports = await sbGet(`client_reports?client_id=eq.${CFG.client_id}&select=title,period_label,storage_path,created_at&order=created_at.desc`);
  if (CFG.reports_from_portal) {
    feed.reports = portalReports.map(r => [r.title, r.period_label || '', (r.storage_path || '').split('?')[0].split('/').filter(Boolean).pop() || '', LANG === 'de' ? 'Aktuell' : 'Current', r.storage_path || '']);
    sources.reports = { source: T.src_reports, read: AS_OF, note: '' };
  }
});

/* ---------- 10. Ergebnisse: before and after the first 30 days (Search Console, review list, directory entries) ---------- */
if (CFG.ergebnisse) await block('ergebnisse', async () => {
  const E = CFG.ergebnisse, [b0, b1] = E.before, [a0, a1] = E.after, E_ = T.erg;
  const lagEnd = addDays(AS_OF, -2);
  const latest = addDays(a1, 1) <= lagEnd ? [addDays(a1, 1), lagEnd] : null;     // the time after the second window, up to the last day Search Console has
  const state = e => (e <= lagEnd ? 'final' : 'all');
  const win = async (s, e, query) => {
    const body = { startDate: s, endDate: e, dataState: state(e), ...(query ? { dimensionFilterGroups: [{ filters: [{ dimension: 'query', operator: 'equals', expression: query }] }] } : {}) };
    const x = (await gsc(CFG.gsc_site, query ? { ...body, dimensions: ['query'] } : body)).rows?.[0];
    return x ? { clicks: x.clicks, impressions: x.impressions, ctr: r1(x.ctr * 100), position: r1(x.position) } : { clicks: 0, impressions: 0, ctr: null, position: null };
  };
  const W = { before: await win(b0, b1), after: await win(a0, a1), latest: latest ? await win(...latest) : null };
  const lbl = (s, e) => T.range(dMon(s), dMon(e));
  const metric = (key, label, unit, better) => ({ key, label, unit, better, before: W.before[key], after: W.after[key], latest: W.latest ? W.latest[key] : null, source: E_.src_gsc, read: AS_OF });
  const metrics = [metric('clicks', E_.clicks, '', 'higher'), metric('impressions', E_.impressions, '', 'higher'), metric('ctr', E_.ctr, '%', 'higher'), metric('position', E_.position, '', 'lower')];
  const queries = [];
  for (const qy of E.queries || []) {
    const qb = await win(b0, b1, qy), qa = await win(a0, a1, qy), ql = latest ? await win(...latest, qy) : null;
    const cut = o => o && { clicks: o.clicks, impressions: o.impressions, position: o.position };
    queries.push({ query: qy, before: cut(qb), after: cut(qa), latest: cut(ql), source: E_.src_gsc, read: AS_OF });
  }
  let reviews = null;
  const RL = reviewData[PRIMARY]?.list;
  if (!RL && E.reviews_outcome) {                                               // no live review list for this client: take the stored measurement (portal row, visible to the client)
    const O = E.reviews_outcome;
    const rows = await sbGet(`work_outcomes?work_item_id=eq.${O.work_item_id}&metric_key=eq.${O.metric_key}&visibility=eq.client&select=value_before,value_after,measured_at,confidence&limit=1`);
    const parse = v => { const m = String(v ?? '').match(/^\s*(\d+)\s*\(\s*([\d.,]+)\s*\)/); return m ? { n: +m[1], star: +m[2].replace(',', '.') } : null; };
    const row = rows[0], bf = row && parse(row.value_before), af = row && parse(row.value_after);
    if (bf && af) reviews = { label: E_.reviews, before: { ...bf, date: b1 }, after: { ...af, date: row.measured_at }, now: null, source: E_.src_rev_portal(dMonY(row.measured_at)), read: AS_OF, note: E_.note_reviews_portal };
    else warn.push('reviews: stored measurement not readable');
  }
  if (RL) {
    const at = d => { const l = RL.filter(x => x.date <= d); return { n: l.length, star: l.length ? r1(l.reduce((s, x) => s + x.rating, 0) / l.length) : null, date: d }; };
    reviews = { label: E_.reviews, before: at(b1), after: at(a1), now: { n: reviewData[PRIMARY].n, star: r1(reviewData[PRIMARY].star), date: AS_OF }, source: E_.src_rev, read: AS_OF, note: E_.note_reviews };
  }
  const citations = feed.citations ? { label: E_.citations, before: null, after: { live: feed.citations.live, total: feed.citations.total, date: AS_OF }, source: E_.src_cit, read: AS_OF, note: E_.note_cit } : null;
  let note = null;
  if (E.event && W.latest) note = E_.note_event(dMon(E.event.date), lbl(...latest), nf(W.latest.position, 1));
  feed.ergebnisse = {
    title: E_.title, read: AS_OF,
    windows: { before: { from: b0, to: b1, label: lbl(b0, b1) }, after: { from: a0, to: a1, label: lbl(a0, a1) }, latest: latest ? { from: latest[0], to: latest[1], label: lbl(...latest) } : null },
    metrics, queries, reviews, citations, note
  };
  for (const [key, [eb, ea]] of Object.entries(E.expect || {})) {                // numbers stated by the client chat are checked against what Google returns now
    const m = metrics.find(x => x.key === key);
    if (m && (m.before !== eb || m.after !== ea)) warn.push(`ergebnisse ${key}: expected ${eb} -> ${ea}, Google returns ${m.before} -> ${m.after}`);
  }
  sources.ergebnisse = { source: E_.src_gsc, read: AS_OF, note: '' };
});

/* ---------- 11. meta, text lines derived from the numbers ---------- */
const week = CFG.program ? Math.min(CFG.program.weeks, Math.max(1, Math.floor(daysBetween(CFG.program.start, AS_OF) / 7) + 1)) : null;   // no program (mode "reports"): no week
if (PROFILES.length > 1 && PROFILES.every(p => p.name)) feed.profiles = PROFILES.map(p => [p.key, p.name]);   // profile switch for clients with several Google listings
feed.meta = { ...base.meta, as_of: AS_OF, week, weeks: CFG.program ? CFG.program.weeks : null, full: months.length - 2, partial: months.length - 1 };
if (CFG.last_update?.type === 'head') await block('last_update', async () => {
  const r = await fetch(base.meta[CFG.last_update.url_key], { method: 'HEAD' }); const lm = r.headers.get('last-modified'); if (!r.ok || !lm) throw new Error('no Last-Modified');
  const d = ymd(new Date(lm)); feed.meta.last_update = `${d === AS_OF ? T.today : ''}${dMon(d)}. ${T.roadmap}`;
  sources.last_update = { source: 'Publish date of the roadmap page', read: AS_OF, note: dMonY(d) };
});
if (CFG.last_update?.type === 'client_reports' && portalReports) {
  const r0 = portalReports[0];
  if (r0) {
    const d = ymd(new Date(r0.created_at)), title = r0.title.replace(/^[^\p{L}\p{N}]+/u, '').trim();
    feed.meta.last_update = `${d === AS_OF ? T.today : ''}${dMon(d)}${LANG === 'de' ? ':' : '.'} ${title}`;
    sources.last_update = { source: T.src_reports, read: AS_OF, note: dMonY(d) };
  }
}
if (reviewData[PRIMARY] && Array.isArray(feed.needs)) {                          // "Needs you" line about unanswered reviews comes from the live review list
  const dn = derived.reviews[PRIMARY], n = reviewData[PRIMARY].n, i = feed.needs.findIndex(x => x.go === 'results/reviews');
  if (i >= 0) {
    if (dn.newest_without_reply === 0) feed.needs.splice(i, 1);
    else feed.needs[i] = { ...feed.needs[i], t: T.reviewLine(dn.newest_without_reply, dn.replied, n) };
  }
}
const adsAt = derived.ads?.snapshot_date;
feed.source_note = T.source_note(dMonY(AS_OF), { gsc: !!feed.gsc?.pos, ga4: !!CFG.ga4, profiles: USE_LF, ads: !!CFG.ads, adsAt: adsAt && adsAt !== AS_OF ? dMonY(adsAt) : null, reviews: !USE_LF && !!feed.ergebnisse?.reviews, citations: !!feed.citations });

feed.meta.refresh = { generated_at: new Date().toISOString(), job: 'portal/feed/build.mjs', as_of: AS_OF, status: failed.length ? 'partial' : 'ok', failed, gaps, filling_from: FILL_FROM, carried: CFG.carried };
feed.meta.filling = { from: FILL_FROM, to: AS_OF, month_index: [...new Set([FILL_FROM, AS_OF].map(monthOf).filter(x => x >= 0))], note: T.fill_note };
feed.meta.sources = sources; feed.meta.derived = derived;

writeFileSync(OUT_FILE, JSON.stringify(feed, null, 1));
writeFileSync(join(dirname(OUT_FILE), 'refresh-log.json'), JSON.stringify({ generated_at: feed.meta.refresh.generated_at, client: SLUG, as_of: AS_OF, failed, gaps, warnings: warn }, null, 1));
const lines = diffLines(snapshot, feed);
writeFileSync(join(dirname(OUT_FILE), 'diff.txt'), lines.join('\n') + '\n');
console.log(`\nWrote ${OUT_FILE.replace(ROOT + '/', '')}  (client ${SLUG}, as of ${AS_OF}, status ${feed.meta.refresh.status})`);
console.log(`\nDiff against ${SNAPSHOT_FILE ? SNAPSHOT_FILE.replace(ROOT + '/', '') : 'the previous run (no snapshot for this client)'}  (${lines.length} lines):`);
console.log(lines.join('\n'));
if (warn.length) { console.log('\nWarnings:'); warn.forEach(w => console.log('  - ' + w)); }
if (gaps.length) console.log('\nGAPS (no access, block stays empty):', gaps.join(', '));
if (failed.length) { console.log('\nFAILED blocks (kept from base feed):', failed.join(', ')); process.exit(2); }
