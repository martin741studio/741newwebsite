#!/usr/bin/env node
/**
 * Monatlicher GA4 → HTML Kunden-Report (741-Studio-Look).
 * Dependency-free (Node built-ins). Zieht den letzten vollen Kalendermonat
 * für jede konfigurierte Property, rendert ein self-contained HTML-Dashboard
 * und (mit --upload) lädt es in den Supabase-Storage + verlinkt es via client_reports.
 *
 *   node reporting/monthly-client-report.mjs                 # rendert lokal nach reporting/out/
 *   node reporting/monthly-client-report.mjs --mock          # Vorschau ohne API (Fake-Zahlen)
 *   node reporting/monthly-client-report.mjs --upload        # + Upload nach Supabase
 *   node reporting/monthly-client-report.mjs --month=2026-07 # bestimmter Monat
 *
 * Auth:
 *   GA:       .secrets/ga-sc-reporting-bot.json  ODER  env GA_SA_KEY_B64 (base64 des JSON)
 *   Supabase: env SUPABASE_URL + SUPABASE_SERVICE_KEY  (nur für --upload)
 */
import { readFileSync, mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { createSign } from 'node:crypto';

// ─────────────────────────── Konfiguration ───────────────────────────
const KAMIL = 'cc5ad406-d06d-4b5a-a33c-3386b9e3de60';   // Portal-Kunde "Kamil Böyük" (mode=reports)
// Beide Marken teilen sich EINE GA4-Property (468424260) → per hostName trennen.
const CLIENTS = [
  { key: 'physio-anatomie', name: 'Physio Anatomie', domain: 'physiotherapieoberhausen.com', property: 'properties/468424260', host: 'physiotherapieoberhausen.com', supabaseClientId: KAMIL, accent: '#fac118',
    // Manuelle Ads-Zahlen je Monat (Fallback bis GA4-Kostenimport greift; Ads-Konto 992-981-4093 seit 2026-08-14 verknüpft).
    manualAds: { '2026-07': { cost: 1150, clicks: 1530, impressions: 17500 } } },
  { key: 'physiokraft', name: 'Physiokraft', domain: 'physiotherapiekraft.de', property: 'properties/468424260', host: 'physiotherapiekraft.de', supabaseClientId: KAMIL, accent: '#fac118',
    manualAds: { '2026-07': { cost: 1220, clicks: 1630, impressions: 22700 } } },
].filter(c => c.property);

const OUT_DIR = new URL('./out/', import.meta.url);
const KEY_PATH = new URL('../.secrets/ga-sc-reporting-bot.json', import.meta.url);
// Echtes 741-Logo (Source of Truth = die Portal-Logodatei), zur Build-Zeit als data-URI eingebettet.
// GRUNDSATZ: für Reports IMMER echte Logo-Assets verwenden, nie handgemalte Platzhalter.
const LOGO_IMG = `<img src="data:image/png;base64,${readFileSync(new URL('../04_site/assets/images/logo_black.png', import.meta.url)).toString('base64')}" alt="741 Studio" style="height:34px;width:auto;display:block;">`;
const SCOPES = 'https://www.googleapis.com/auth/analytics.readonly';

const args = process.argv.slice(2);
const MOCK = args.includes('--mock');
const UPLOAD = args.includes('--upload');
const monthArg = (args.find(a => a.startsWith('--month=')) || '').split('=')[1];

// ─────────────────────────── Datum: letzter voller Monat ───────────────────────────
function monthRange(ym) {
  let y, m; // m = 0-basiert
  if (ym) { const [yy, mm] = ym.split('-').map(Number); y = yy; m = mm - 1; }
  else { const d = new Date(); const first = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), 1)); const le = new Date(first.getTime() - 864e5); y = le.getUTCFullYear(); m = le.getUTCMonth(); }
  const start = new Date(Date.UTC(y, m, 1));
  const end = new Date(Date.UTC(y, m + 1, 0));
  const prevStart = new Date(Date.UTC(y, m - 1, 1));
  const prevEnd = new Date(Date.UTC(y, m, 0));
  const iso = x => x.toISOString().slice(0, 10);
  const label = start.toLocaleDateString('de-DE', { month: 'long', year: 'numeric', timeZone: 'UTC' });
  return { start: iso(start), end: iso(end), prevStart: iso(prevStart), prevEnd: iso(prevEnd), label, ym: `${y}-${String(m + 1).padStart(2, '0')}` };
}

// ─────────────────────────── GA4 Auth + API ───────────────────────────
const b64url = b => Buffer.from(b).toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
function loadKey() {
  if (process.env.GA_SA_KEY_B64) return JSON.parse(Buffer.from(process.env.GA_SA_KEY_B64, 'base64').toString('utf8'));
  return JSON.parse(readFileSync(KEY_PATH, 'utf8'));
}
async function getToken(key) {
  const now = Math.floor(Date.now() / 1000);
  const h = b64url(JSON.stringify({ alg: 'RS256', typ: 'JWT' }));
  const c = b64url(JSON.stringify({ iss: key.client_email, scope: SCOPES, aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600 }));
  const s = createSign('RSA-SHA256'); s.update(`${h}.${c}`);
  const jwt = `${h}.${c}.${b64url(s.sign(key.private_key))}`;
  const r = await fetch('https://oauth2.googleapis.com/token', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: jwt }) });
  const j = await r.json(); if (!r.ok) throw new Error('Token: ' + JSON.stringify(j)); return j.access_token;
}
async function runReport(prop, token, body) {
  const r = await fetch(`https://analyticsdata.googleapis.com/v1beta/${prop}:runReport`, { method: 'POST', headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  const j = await r.json(); if (!r.ok) throw new Error(`${r.status} ${prop}: ${j.error?.message || JSON.stringify(j)}`); return j;
}
const num = v => Number(v || 0);
const rows = j => (j.rows || []).map(r => ({ dims: r.dimensionValues.map(d => d.value), mets: r.metricValues.map(m => num(m.value)) }));
const totalOf = (j, i = 0) => num(j.totals?.[0]?.metricValues?.[i]?.value ?? j.rows?.[0]?.metricValues?.[i]?.value);

// ─────────────────────────── Daten ziehen ───────────────────────────
async function pull(client, token, R) {
  const dr = [{ startDate: R.start, endDate: R.end }];
  const drPrev = [{ startDate: R.prevStart, endDate: R.prevEnd }];
  // Wenn mehrere Sites in einer Property liegen: per hostName filtern.
  const hostFilter = client.host ? { dimensionFilter: { filter: { fieldName: 'hostName', stringFilter: { matchType: 'EXACT', value: client.host } } } } : {};
  const rep = (body) => runReport(client.property, token, { ...body, ...hostFilter });
  const M = [{ name: 'sessions' }, { name: 'activeUsers' }, { name: 'keyEvents' }, { name: 'screenPageViews' }, { name: 'averageSessionDuration' }];
  const cur = await rep({ dateRanges: dr, metrics: M });
  const prev = await rep({ dateRanges: drPrev, metrics: M });
  const channels = await rep({ dateRanges: dr, dimensions: [{ name: 'sessionDefaultChannelGroup' }], metrics: [{ name: 'sessions' }, { name: 'keyEvents' }], orderBys: [{ metric: { metricName: 'sessions' }, desc: true }], limit: 10 });
  const sourceMedium = await rep({ dateRanges: dr, dimensions: [{ name: 'sessionSourceMedium' }], metrics: [{ name: 'sessions' }, { name: 'keyEvents' }], orderBys: [{ metric: { metricName: 'sessions' }, desc: true }], limit: 8 });
  const pages = await rep({ dateRanges: dr, dimensions: [{ name: 'pagePath' }], metrics: [{ name: 'screenPageViews' }], orderBys: [{ metric: { metricName: 'screenPageViews' }, desc: true }], limit: 8 });
  const daily = await rep({ dateRanges: dr, dimensions: [{ name: 'date' }], metrics: [{ name: 'sessions' }], orderBys: [{ dimension: { dimensionName: 'date' } }] });
  const device = await rep({ dateRanges: dr, dimensions: [{ name: 'deviceCategory' }], metrics: [{ name: 'sessions' }], orderBys: [{ metric: { metricName: 'sessions' }, desc: true }] });
  const d = shape(cur, prev, channels, sourceMedium, pages, daily, device);
  // Ads-Kosten: bevorzugt manuell (site-genau); sonst GA4-Import (greift ~24h nach Konto-Verknüpfung, property-weit).
  const man = client.manualAds && client.manualAds[R.ym];
  if (man) d.ads = { ...man, source: 'manual' };
  else {
    try {
      const ac = await runReport(client.property, token, { dateRanges: dr, dimensions: [{ name: 'sessionGoogleAdsCampaignName' }], metrics: [{ name: 'advertiserAdCost' }, { name: 'advertiserAdClicks' }, { name: 'advertiserAdImpressions' }] });
      let cost = 0, clicks = 0, impressions = 0;
      for (const r of rows(ac)) { cost += r.mets[0]; clicks += r.mets[1]; impressions += r.mets[2]; }
      d.ads = cost > 0 ? { cost, clicks, impressions, source: 'ga4' } : null;
    } catch (e) { d.ads = null; }
  }
  return d;
}
function shape(cur, prev, channels, sourceMedium, pages, daily, device) {
  const kpi = (j) => ({ sessions: totalOf(j, 0), users: totalOf(j, 1), keyEvents: totalOf(j, 2), views: totalOf(j, 3), dur: totalOf(j, 4) });
  const paidRow = rows(channels).filter(r => /paid/i.test(r.dims[0]));
  const orgRow = rows(channels).filter(r => /organic/i.test(r.dims[0]));
  return {
    cur: kpi(cur), prev: kpi(prev),
    channels: rows(channels).map(r => ({ name: r.dims[0], sessions: r.mets[0], leads: r.mets[1] })),
    sourceMedium: rows(sourceMedium).map(r => ({ name: r.dims[0], sessions: r.mets[0], leads: r.mets[1] })),
    pages: rows(pages).map(r => ({ path: r.dims[0], views: r.mets[0] })),
    daily: rows(daily).map(r => ({ date: r.dims[0], sessions: r.mets[0] })),
    device: rows(device).map(r => ({ name: r.dims[0], sessions: r.mets[0] })),
    paidSessions: paidRow.reduce((a, r) => a + r.mets[0], 0), paidLeads: paidRow.reduce((a, r) => a + r.mets[1], 0),
    orgSessions: orgRow.reduce((a, r) => a + r.mets[0], 0),
  };
}

// ─────────────────────────── Mock ───────────────────────────
function mockData() {
  const daily = Array.from({ length: 31 }, (_, i) => ({ date: `202607${String(i + 1).padStart(2, '0')}`, sessions: Math.round(30 + 25 * Math.sin(i / 3) + (i % 7 === 0 ? -12 : 6)) }));
  return {
    cur: { sessions: 1284, users: 1032, keyEvents: 47, views: 3118, dur: 96.4 },
    prev: { sessions: 1067, users: 869, keyEvents: 38, views: 2701, dur: 88.1 },
    channels: [{ name: 'Paid Search', sessions: 612, leads: 29 }, { name: 'Organic Search', sessions: 431, leads: 11 }, { name: 'Direct', sessions: 158, leads: 5 }, { name: 'Organic Social', sessions: 61, leads: 2 }, { name: 'Referral', sessions: 22, leads: 0 }],
    sourceMedium: [{ name: 'google / cpc', sessions: 612, leads: 29 }, { name: 'google / organic', sessions: 401, leads: 11 }, { name: '(direct) / (none)', sessions: 158, leads: 5 }, { name: 'bing / organic', sessions: 30, leads: 0 }, { name: 'instagram / social', sessions: 41, leads: 2 }],
    pages: [{ path: '/', views: 1044 }, { path: '/leistungen', views: 512 }, { path: '/kontakt', views: 388 }, { path: '/team', views: 201 }, { path: '/termin', views: 174 }],
    daily, device: [{ name: 'mobile', sessions: 812 }, { name: 'desktop', sessions: 402 }, { name: 'tablet', sessions: 70 }],
    paidSessions: 612, paidLeads: 29, orgSessions: 431,
    ads: { cost: 1150, clicks: 1530, impressions: 17500, source: 'manual' },
  };
}

// ─────────────────────────── HTML-Rendering ───────────────────────────
const fmt = n => Number(Math.round(n)).toLocaleString('de-DE');
const pct = (a, b) => b === 0 ? (a > 0 ? 100 : 0) : ((a - b) / b) * 100;
function delta(a, b) {
  const p = pct(a, b); const up = p >= 0;
  return `<span class="delta ${up ? 'up' : 'down'}">${up ? '▲' : '▼'} ${Math.abs(p).toFixed(0)}%</span>`;
}
function mmss(sec) { const m = Math.floor(sec / 60), s = Math.round(sec % 60); return `${m}:${String(s).padStart(2, '0')}`; }
function spark(daily, accent) {
  if (!daily.length) return '';
  const w = 640, h = 90, pad = 4;
  const max = Math.max(...daily.map(d => d.sessions), 1);
  const step = (w - pad * 2) / Math.max(daily.length - 1, 1);
  const pts = daily.map((d, i) => [pad + i * step, h - pad - (d.sessions / max) * (h - pad * 2)]);
  const line = pts.map((p, i) => `${i ? 'L' : 'M'}${p[0].toFixed(1)},${p[1].toFixed(1)}`).join(' ');
  const area = `${line} L${pts[pts.length - 1][0].toFixed(1)},${h - pad} L${pts[0][0].toFixed(1)},${h - pad} Z`;
  return `<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" style="width:100%;height:90px;">
    <path d="${area}" fill="${accent}22"/><path d="${line}" fill="none" stroke="${accent}" stroke-width="2.5" stroke-linejoin="round"/></svg>`;
}
function bars(items, accent, valKey = 'sessions') {
  const max = Math.max(...items.map(i => i[valKey]), 1);
  return items.map(i => `<div class="bar-row"><div class="bar-label">${esc(i.name || i.path)}</div>
    <div class="bar-track"><div class="bar-fill" style="width:${(i[valKey] / max) * 100}%;background:${accent}"></div></div>
    <div class="bar-val">${fmt(i[valKey])}${i.leads != null ? ` <span class="muted">· ${fmt(i.leads)} Leads</span>` : ''}</div></div>`).join('');
}
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

function summary(d, name) {
  const sd = pct(d.cur.sessions, d.prev.sessions);
  const trend = sd >= 5 ? `ein Plus von ${sd.toFixed(0)}% gegenüber dem Vormonat` : sd <= -5 ? `ein Rückgang von ${Math.abs(sd).toFixed(0)}% gegenüber dem Vormonat` : `stabil auf Vormonatsniveau`;
  const paidShare = d.cur.sessions ? Math.round((d.paidSessions / d.cur.sessions) * 100) : 0;
  const cpc = d.ads && d.ads.clicks ? (d.ads.cost / d.ads.clicks).toFixed(2) : null;
  const cost = d.ads ? ` Google-Ads-Budget im Monat: €${fmt(d.ads.cost)} bei ${fmt(d.ads.clicks)} Klicks${cpc ? ` (Ø CPC €${cpc})` : ''}.` : '';
  const cac = (d.ads && d.cur.keyEvents) ? ` CAC (Spend ÷ Leads): €${Math.round(d.ads.cost / d.cur.keyEvents)}.` : (d.ads ? ' CAC folgt, sobald Conversions in GA4 erfasst werden.' : '');
  return `${fmt(d.cur.sessions)} Sitzungen im Berichtsmonat — ${trend}. Google Ads (Paid Search) lieferte ${fmt(d.paidSessions)} Sitzungen (${paidShare}% des Traffics).${cost}${cac} Insgesamt ${fmt(d.cur.keyEvents)} Leads/Key-Events aus allen Kanälen.`;
}

function html(client, R, d) {
  const A = client.accent;
  const logo = LOGO_IMG;
  const kpi = (label, val, prevVal, sub) => `<div class="kpi"><div class="kpi-label">${label}</div><div class="kpi-val">${val}</div><div class="kpi-sub">${prevVal != null ? delta(...prevVal) + ' ' : ''}${sub || ''}</div></div>`;
  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(client.name)} — GA4 Monatsreport ${esc(R.label)}</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800&display=swap" rel="stylesheet">
<style>
:root{--y:${A};--ink:#252525;--cream:#fffcf3;--grey:#8c8c8c;--line:#efeadb;--green:#2e9e5b;--red:#c0392b;}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"DM Sans",-apple-system,Arial,sans-serif;background:var(--cream);color:var(--ink);-webkit-font-smoothing:antialiased;line-height:1.5}
.wrap{max-width:1040px;margin:0 auto;padding:32px 24px 60px}
.top{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;border-bottom:1.5px solid var(--line);padding-bottom:20px;margin-bottom:26px}
.top .r{text-align:right;font-size:13px;color:var(--grey)}
.badge{display:inline-flex;align-items:center;gap:6px;background:#e7f6ed;color:var(--green);font-weight:700;font-size:12.5px;padding:5px 12px;border-radius:20px}
h1{font-size:30px;font-weight:800;letter-spacing:-.5px}
.subtitle{color:var(--grey);font-weight:600;letter-spacing:2px;text-transform:uppercase;font-size:12.5px;margin-top:4px}
.summary{background:#fff;border-left:4px solid var(--y);border-radius:12px;padding:20px 22px;margin:22px 0 26px;box-shadow:0 2px 14px rgba(37,37,37,.06)}
.summary .h{font-weight:800;font-size:12.5px;letter-spacing:1.5px;text-transform:uppercase;color:#a07d00;margin-bottom:8px}
.summary p{font-size:16.5px;font-style:italic}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin-bottom:26px}
.kpi{background:#fff;border-radius:14px;padding:18px 18px 16px;box-shadow:0 2px 14px rgba(37,37,37,.06)}
.kpi-label{font-size:12.5px;color:var(--grey);font-weight:700;text-transform:uppercase;letter-spacing:.4px}
.kpi-val{font-size:30px;font-weight:800;margin:6px 0 2px;letter-spacing:-.5px}
.kpi-sub{font-size:12.5px;color:var(--grey)}
.delta{font-weight:800;font-size:12.5px}.delta.up{color:var(--green)}.delta.down{color:var(--red)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:18px}
@media(max-width:720px){.grid2{grid-template-columns:1fr}}
.card{background:#fff;border-radius:14px;padding:22px;box-shadow:0 2px 14px rgba(37,37,37,.06)}
.card h2{font-size:15px;font-weight:800;margin-bottom:14px;display:flex;align-items:center;gap:8px}
.bar-row{display:grid;grid-template-columns:130px 1fr auto;gap:10px;align-items:center;margin-bottom:9px;font-size:13.5px}
.bar-label{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bar-track{background:#f3f0e6;border-radius:8px;height:16px;overflow:hidden}
.bar-fill{height:100%;border-radius:8px;min-width:2px}
.bar-val{font-weight:700;white-space:nowrap;font-size:13px}
.muted{color:var(--grey);font-weight:500}
.foot{margin-top:30px;text-align:center;color:var(--grey);font-size:12.5px}
.paid-split{display:flex;gap:0;border-radius:12px;overflow:hidden;height:34px;margin:6px 0 14px;font-size:12.5px;font-weight:700}
.paid-split div{display:flex;align-items:center;justify-content:center;color:#fff;white-space:nowrap}
</style></head>
<body><div class="wrap">
  <div class="top">
    <div>${logo}</div>
    <div class="r"><div class="badge">● Kampagne aktiv</div><div style="margin-top:8px">Report erstellt: ${new Date().toLocaleDateString('de-DE', { timeZone: 'UTC' })}</div></div>
  </div>
  <h1>${esc(client.name)}</h1>
  <div class="subtitle">GA4 · Monatsreport · ${esc(R.label)}${client.domain ? ` · ${esc(client.domain)}` : ''}</div>

  <div class="summary"><div class="h">⚡ Zusammenfassung</div><p>${summary(d, client.name)}</p></div>

  <div class="kpis">
    ${kpi('Sitzungen', fmt(d.cur.sessions), [d.cur.sessions, d.prev.sessions], 'vs. Vormonat')}
    ${kpi('Nutzer', fmt(d.cur.users), [d.cur.users, d.prev.users], 'vs. Vormonat')}
    ${kpi('Leads / Key-Events', fmt(d.cur.keyEvents), [d.cur.keyEvents, d.prev.keyEvents], 'Kontakt-Aktionen')}
    ${kpi('Seitenaufrufe', fmt(d.cur.views), [d.cur.views, d.prev.views], 'vs. Vormonat')}
    ${kpi('Ø Sitzungsdauer', mmss(d.cur.dur), [d.cur.dur, d.prev.dur], 'min:sek')}
  </div>
  ${d.ads ? `<div class="kpis">
    ${kpi('Ad-Spend', '€' + fmt(d.ads.cost), null, d.ads.source === 'manual' ? 'Google Ads · manuell' : 'Google Ads')}
    ${kpi('Ø CPC', d.ads.clicks ? '€' + (d.ads.cost / d.ads.clicks).toFixed(2) : '–', null, fmt(d.ads.clicks) + ' Klicks')}
    ${kpi('Ad-Impressionen', fmt(d.ads.impressions), null, 'Google Ads')}
    ${kpi('Kosten / Sitzung', d.cur.sessions ? '€' + (d.ads.cost / d.cur.sessions).toFixed(2) : '–', null, 'Spend ÷ Sitzungen')}
    ${kpi('CAC', d.cur.keyEvents ? '€' + Math.round(d.ads.cost / d.cur.keyEvents) : '—', null, d.cur.keyEvents ? 'pro Lead' : 'Conversions fehlen')}
  </div>` : ''}

  <div class="card" style="margin-bottom:18px">
    <h2>📈 Sitzungen im Monatsverlauf</h2>
    ${spark(d.daily, A)}
  </div>

  <div class="card" style="margin-bottom:18px">
    <h2>🎯 Bezahlt vs. Organisch</h2>
    ${(() => { const tot = d.paidSessions + d.orgSessions || 1; const pp = Math.round((d.paidSessions / tot) * 100); return `<div class="paid-split"><div style="width:${pp}%;background:${A};color:#252525">Paid ${pp}%</div><div style="width:${100 - pp}%;background:#252525">Organic ${100 - pp}%</div></div><div class="muted" style="font-size:13.5px">Google Ads: <b>${fmt(d.paidSessions)}</b> Sitzungen / <b>${fmt(d.paidLeads)}</b> Leads &nbsp;·&nbsp; Organisch: <b>${fmt(d.orgSessions)}</b> Sitzungen</div>`; })()}
  </div>

  <div class="grid2">
    <div class="card"><h2>🌐 Kanäle</h2>${bars(d.channels, A)}</div>
    <div class="card"><h2>🔗 Quelle / Medium</h2>${bars(d.sourceMedium, A)}</div>
  </div>
  <div class="grid2">
    <div class="card"><h2>📄 Top-Seiten</h2>${bars(d.pages, A, 'views')}</div>
    <div class="card"><h2>📱 Geräte</h2>${bars(d.device, A)}</div>
  </div>

  <div class="foot">Erstellt von <b>741 Studio</b> · Datenquelle: Google Analytics 4 · Zeitraum ${esc(R.start)} – ${esc(R.end)}<br>Automatisch generiert · Zahlen entsprechen der GA4-Property des Kunden.</div>
</div></body></html>`;
}

// ─────────────────────────── Supabase Upload ───────────────────────────
async function upload(client, R, htmlStr) {
  const SB = process.env.SUPABASE_URL, KEY = process.env.SUPABASE_SERVICE_KEY;
  if (!SB || !KEY) throw new Error('SUPABASE_URL / SUPABASE_SERVICE_KEY fehlen für --upload');
  if (!client.supabaseClientId) { console.log(`   ⚠️  ${client.name}: kein supabaseClientId gesetzt — Upload übersprungen.`); return; }
  const path = `${client.supabaseClientId}/reports/ga4-monthly-${R.ym}.html`;
  const up = await fetch(`${SB}/storage/v1/object/materials/${path}`, { method: 'POST', headers: { Authorization: `Bearer ${KEY}`, 'Content-Type': 'text/html', 'x-upsert': 'true' }, body: htmlStr });
  if (!up.ok) throw new Error('Storage-Upload: ' + up.status + ' ' + await up.text());
  const ins = await fetch(`${SB}/rest/v1/client_reports`, { method: 'POST', headers: { Authorization: `Bearer ${KEY}`, apikey: KEY, 'Content-Type': 'application/json', Prefer: 'resolution=merge-duplicates' }, body: JSON.stringify({ client_id: client.supabaseClientId, title: `${client.name} — GA4 Monatsreport ${R.label}`, period_label: R.label, storage_path: path }) });
  if (!ins.ok) throw new Error('client_reports insert: ' + ins.status + ' ' + await ins.text());
  console.log(`   ✅ Upload + verlinkt: ${path}`);
}

// ─────────────────────────── Main ───────────────────────────
(async () => {
  const R = monthRange(monthArg);
  console.log(`📅 Berichtsmonat: ${R.label} (${R.start} – ${R.end})  ${MOCK ? '[MOCK]' : ''}`);
  if (!existsSync(OUT_DIR)) mkdirSync(OUT_DIR, { recursive: true });
  let token = null;
  if (!MOCK) token = await getToken(loadKey());
  for (const client of CLIENTS) {
    console.log(`\n▓ ${client.name} (${client.property})`);
    let d;
    try { d = MOCK ? mockData() : await pull(client, token, R); }
    catch (e) { console.error(`   ❌ ${e.message}`); continue; }
    const out = html(client, R, d);
    const file = new URL(`./out/${client.key}-${R.ym}${MOCK ? '-mock' : ''}.html`, import.meta.url);
    writeFileSync(file, out);
    console.log(`   📄 ${fmt(d.cur.sessions)} Sitzungen · ${fmt(d.cur.keyEvents)} Leads → ${file.pathname}`);
    if (UPLOAD && !MOCK) await upload(client, R, out);
  }
  console.log('\n✔ fertig.');
})().catch(e => { console.error('❌', e.message); process.exit(1); });
