#!/usr/bin/env node
/**
 * 741.studio Reporting – zieht GA4 (Zielgruppen/Quellen/Seiten) + Search Console
 * live über den Service-Account "reporting-bot" und schreibt ein HTML-Dashboard.
 *
 *   node reporting/generate-report.mjs
 *   → reporting/741studio-report.html
 *
 * Nur Node-Builtins (crypto, fetch, fs). Keine externen Pakete.
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';

// ---- Konfiguration ----
const KEY_PATH = new URL('../.secrets/ga-sc-reporting-bot.json', import.meta.url);
const OUT_PATH = new URL('./741studio-report.html', import.meta.url);
const GA4_PROPERTY = 'properties/363739406';     // "741.studio/ GA4" (741 Studio Main)
const SC_SITE = 'https://741.studio/';           // Search-Console URL-Präfix-Property
const DAYS = 90;                                  // Analysezeitraum
const SCOPES = [
  'https://www.googleapis.com/auth/analytics.readonly',
  'https://www.googleapis.com/auth/webmasters.readonly',
].join(' ');

const b64url = (b) => Buffer.from(b).toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
const iso = (d) => d.toISOString().slice(0, 10);
const START = iso(new Date(Date.now() - DAYS * 864e5));
const END = iso(new Date());

async function getToken(key) {
  const now = Math.floor(Date.now() / 1000);
  const head = b64url(JSON.stringify({ alg: 'RS256', typ: 'JWT' }));
  const claim = b64url(JSON.stringify({ iss: key.client_email, scope: SCOPES, aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600 }));
  const signer = createSign('RSA-SHA256'); signer.update(`${head}.${claim}`);
  const jwt = `${head}.${claim}.${b64url(signer.sign(key.private_key))}`;
  const res = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: jwt }),
  });
  const j = await res.json(); if (!res.ok) throw new Error(JSON.stringify(j));
  return j.access_token;
}

const post = async (url, token, body) => {
  const res = await fetch(url, { method: 'POST', headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  const j = await res.json().catch(() => ({}));
  if (!res.ok) { console.error(`  ⚠️  ${url.split('/').pop()}: ${res.status} ${JSON.stringify(j).slice(0, 100)}`); return { rows: [] }; }
  return j;
};

// GA4 runReport helper → [{key, key2?, users, sessions}]
async function ga4(token, dims, metrics = ['activeUsers', 'sessions'], limit = 15, orderDesc = true) {
  const j = await post(`https://analyticsdata.googleapis.com/v1beta/${GA4_PROPERTY}:runReport`, token, {
    dateRanges: [{ startDate: START, endDate: END }],
    dimensions: dims.map((name) => ({ name })),
    metrics: metrics.map((name) => ({ name })),
    ...(orderDesc ? { orderBys: [{ metric: { metricName: metrics[0] }, desc: true }] } : {}),
    limit,
  });
  return (j.rows || []).map((r) => ({
    keys: r.dimensionValues.map((d) => d.value),
    vals: r.metricValues.map((m) => m.value),
  }));
}

function esc(s) { return String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }

// ---- HTML rendering ----
function bar(rows, labelIdx, valIdx, unit = '') {
  const max = Math.max(1, ...rows.map((r) => +r.vals[valIdx] || +r[valIdx] || 0));
  return rows.map((r) => {
    const label = Array.isArray(r.keys) ? r.keys[labelIdx] : r[0];
    const v = +(Array.isArray(r.vals) ? r.vals[valIdx] : r[valIdx]) || 0;
    const pct = Math.round((v / max) * 100);
    return `<div class="row"><span class="lbl">${esc(label === '(not set)' ? '(unbekannt)' : label)}</span>
      <span class="track"><span class="fill" style="width:${pct}%"></span></span>
      <span class="val">${v.toLocaleString('de-DE')}${unit}</span></div>`;
  }).join('');
}

function card(title, sub, inner) {
  return `<section class="card"><h2>${esc(title)}</h2>${sub ? `<p class="sub">${esc(sub)}</p>` : ''}${inner || '<p class="empty">Keine Daten im Zeitraum.</p>'}</section>`;
}

(async () => {
  const key = JSON.parse(readFileSync(KEY_PATH, 'utf8'));
  console.log(`🔑 ${key.client_email}\n📊 741.studio Reporting · ${START} → ${END} (${DAYS} Tage)\n`);
  const token = await getToken(key);

  // --- GA4 pulls ---
  console.log('→ GA4 Overview');
  const overview = await ga4(token, ['country'], ['activeUsers', 'newUsers', 'sessions', 'averageSessionDuration', 'screenPageViews'], 1, false);
  const totalsJ = await post(`https://analyticsdata.googleapis.com/v1beta/${GA4_PROPERTY}:runReport`, token, {
    dateRanges: [{ startDate: START, endDate: END }],
    metrics: ['activeUsers', 'newUsers', 'sessions', 'screenPageViews', 'averageSessionDuration'].map((name) => ({ name })),
  });
  const T = totalsJ.rows?.[0]?.metricValues?.map((m) => m.value) || ['0', '0', '0', '0', '0'];

  console.log('→ GA4 Zielgruppen (Land/Stadt/Gerät/Alter/Geschlecht/Interessen)');
  const [country, city, device, os, browser, age, gender, channel, source, pages, trend] = await Promise.all([
    ga4(token, ['country']), ga4(token, ['city']), ga4(token, ['deviceCategory']),
    ga4(token, ['operatingSystem']), ga4(token, ['browser']),
    ga4(token, ['userAgeBracket']), ga4(token, ['userGender']),
    ga4(token, ['sessionDefaultChannelGroup']), ga4(token, ['sessionSourceMedium']),
    ga4(token, ['pagePath'], ['screenPageViews', 'activeUsers']),
    ga4(token, ['date'], ['activeUsers'], 100, false),
  ]);

  // --- Search Console ---
  console.log('→ Search Console (Suchbegriffe + Seiten)');
  const key2 = readFileSync(KEY_PATH, 'utf8'); void key2;
  const scPost = async (dim) => {
    const res = await fetch(`https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(SC_SITE)}/searchAnalytics/query`, {
      method: 'POST', headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ startDate: START, endDate: END, dimensions: [dim], rowLimit: 15 }),
    });
    const j = await res.json().catch(() => ({}));
    return j.rows || [];
  };
  const [scQueries, scPages] = await Promise.all([scPost('query'), scPost('page')]);
  const scTotals = scQueries.reduce((a, r) => ({ c: a.c + r.clicks, i: a.i + r.impressions }), { c: 0, i: 0 });

  // --- trend sparkline ---
  const trendSorted = trend.map((r) => ({ d: r.keys[0], v: +r.vals[0] })).sort((a, b) => a.d.localeCompare(b.d));
  const tMax = Math.max(1, ...trendSorted.map((x) => x.v));
  const spark = trendSorted.map((x, i) => {
    const w = 100 / trendSorted.length;
    return `<rect x="${i * w}%" y="${100 - (x.v / tMax) * 100}%" width="${w * 0.8}%" height="${(x.v / tMax) * 100}%" fill="var(--accent)" rx="0.5"/>`;
  }).join('');

  const scRow = (rows, k) => rows.length ? rows.map((r) => `<div class="row"><span class="lbl">${esc(r.keys[0])}</span>
      <span class="track"><span class="fill" style="width:${Math.round((r.clicks || r.impressions) / Math.max(1, ...rows.map((x) => x.clicks || x.impressions)) * 100)}%"></span></span>
      <span class="val">${r.clicks} Kl · ${r.impressions} Imp · Pos ${r.position.toFixed(1)}</span></div>`).join('') : '';

  const mins = Math.floor(+T[4] / 60), secs = Math.round(+T[4] % 60);

  const html = `<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>741.studio · Analytics Report</title>
<style>
:root{--bg:#0d1117;--card:#161b22;--bd:#232a34;--tx:#e6edf3;--mut:#8b949e;--accent:#3b82f6;--accent2:#22c55e}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;padding:32px 20px}
.wrap{max-width:1100px;margin:0 auto}
header h1{font-size:26px;margin:0 0 4px}header .meta{color:var(--mut);font-size:14px;margin-bottom:24px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin-bottom:24px}
.kpi{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:16px}
.kpi .n{font-size:28px;font-weight:700}.kpi .l{color:var(--mut);font-size:13px;margin-top:2px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px}
.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:18px}
.card h2{font-size:15px;margin:0 0 2px}.card .sub{color:var(--mut);font-size:12px;margin:0 0 14px}
.row{display:grid;grid-template-columns:130px 1fr auto;align-items:center;gap:10px;margin:7px 0;font-size:13px}
.lbl{color:var(--tx);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.track{background:#0d1117;border-radius:6px;height:8px;overflow:hidden}
.fill{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:6px}
.val{color:var(--mut);font-variant-numeric:tabular-nums;white-space:nowrap}
.empty{color:var(--mut);font-size:13px;font-style:italic}
.full{grid-column:1/-1}
footer{color:var(--mut);font-size:12px;margin-top:28px;border-top:1px solid var(--bd);padding-top:16px}
.note{background:#1c2333;border:1px solid #2d3a52;border-radius:10px;padding:12px 14px;font-size:13px;color:#cdd9e5;margin-bottom:22px}
svg{width:100%;height:70px;display:block}
</style></head><body><div class="wrap">
<header>
  <h1>741.studio · Analytics Report</h1>
  <div class="meta">Zeitraum ${START} bis ${END} · GA4 ${GA4_PROPERTY.split('/')[1]} · erstellt ${END}</div>
</header>

<div class="note">📌 Zielgruppen-Einblick: Wer besucht 741.studio? Basiert auf ${(+T[0]).toLocaleString('de-DE')} aktiven Nutzern der letzten ${DAYS} Tage. Alters-/Geschlechts-/Interessendaten erscheinen nur, wenn „Google-Signale" aktiv sind und genug Volumen vorhanden ist.</div>

<div class="kpis">
  <div class="kpi"><div class="n">${(+T[0]).toLocaleString('de-DE')}</div><div class="l">Aktive Nutzer</div></div>
  <div class="kpi"><div class="n">${(+T[1]).toLocaleString('de-DE')}</div><div class="l">Neue Nutzer</div></div>
  <div class="kpi"><div class="n">${(+T[2]).toLocaleString('de-DE')}</div><div class="l">Sitzungen</div></div>
  <div class="kpi"><div class="n">${(+T[3]).toLocaleString('de-DE')}</div><div class="l">Seitenaufrufe</div></div>
  <div class="kpi"><div class="n">${mins}m ${secs}s</div><div class="l">Ø Sitzungsdauer</div></div>
  <div class="kpi"><div class="n">${scTotals.c} / ${scTotals.i}</div><div class="l">Google-Klicks / Impr.</div></div>
</div>

<section class="card full" style="margin-bottom:16px"><h2>Besucher-Verlauf (täglich aktive Nutzer)</h2>
  <svg viewBox="0 0 100 100" preserveAspectRatio="none">${spark}</svg></section>

<div class="grid">
  ${card('🌍 Länder', 'Woher kommen die Besucher', bar(country, 0, 0))}
  ${card('🏙️ Städte', 'Top-Standorte', bar(city, 0, 0))}
  ${card('📱 Geräte', 'Desktop / Mobil / Tablet', bar(device, 0, 0))}
  ${card('💻 Betriebssystem', null, bar(os, 0, 0))}
  ${card('🌐 Browser', null, bar(browser, 0, 0))}
  ${card('👥 Altersgruppen', 'Nur mit Google-Signalen', age.length ? bar(age, 0, 0) : null)}
  ${card('⚧ Geschlecht', 'Nur mit Google-Signalen', gender.length ? bar(gender, 0, 0) : null)}
  ${card('🔗 Kanäle', 'Wie Besucher hereinkommen', bar(channel, 0, 0))}
  ${card('📍 Quelle / Medium', null, bar(source, 0, 0))}
  ${card('📄 Top-Seiten', 'Meistbesuchte Seiten (Aufrufe)', bar(pages, 0, 0))}
  ${card('🔎 Google-Suchbegriffe', `Search Console · ${SC_SITE}`, scRow(scQueries))}
  ${card('📑 Top-Seiten (Google-Suche)', 'Search Console', scRow(scPages))}
</div>

<footer>
  Automatisch erzeugt via GA4 Data API + Search Console API (Service-Account reporting-bot).
  Neu generieren: <code>node reporting/generate-report.mjs</code>
</footer>
</div></body></html>`;

  writeFileSync(OUT_PATH, html);
  console.log(`\n✅ Report geschrieben: reporting/741studio-report.html`);
  console.log(`   Aktive Nutzer (${DAYS}T): ${T[0]} · Sitzungen: ${T[2]} · Google-Klicks: ${scTotals.c}`);
})().catch((e) => { console.error('\n❌', e.message); process.exit(1); });
