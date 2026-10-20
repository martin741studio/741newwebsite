#!/usr/bin/env node
/**
 * Search-Console-Export für eine Kunden-Property (read-only, Service-Account "reporting-bot").
 * Voraussetzung: Die Property ist in der Search Console für
 *   reporting-bot@studio-apis-503306.iam.gserviceaccount.com  (Berechtigung: "Uneingeschränkt" oder "Eingeschränkt")
 * freigegeben. Sonst Fehler 403 "User does not have sufficient permission".
 *
 *   node scripts/gsc-client-export.mjs <siteUrl> [days=90] [out.json]
 *   node scripts/gsc-client-export.mjs https://www.suriya-praxis.de/ 90 /tmp/suriya-gsc.json
 *   node scripts/gsc-client-export.mjs sc-domain:suriya-praxis.de           (Domain-Property)
 *   node scripts/gsc-client-export.mjs --list                                 (welche Properties sind freigegeben?)
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';

const KEY_PATH = new URL('../.secrets/ga-sc-reporting-bot.json', import.meta.url);
const key = JSON.parse(readFileSync(KEY_PATH, 'utf8'));
const b64url = (b) => Buffer.from(b).toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');

async function token() {
  const now = Math.floor(Date.now() / 1000);
  const unsigned = `${b64url(JSON.stringify({ alg: 'RS256', typ: 'JWT' }))}.${b64url(JSON.stringify({
    iss: key.client_email, scope: 'https://www.googleapis.com/auth/webmasters.readonly',
    aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600 }))}`;
  const s = createSign('RSA-SHA256'); s.update(unsigned);
  const jwt = `${unsigned}.${b64url(s.sign(key.private_key))}`;
  const r = await fetch('https://oauth2.googleapis.com/token', { method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: jwt }) });
  const j = await r.json(); if (!r.ok) throw new Error(JSON.stringify(j)); return j.access_token;
}
const iso = (d) => d.toISOString().slice(0, 10);

(async () => {
  const [a, b, c] = process.argv.slice(2);
  const t = await token();
  const H = { Authorization: `Bearer ${t}`, 'Content-Type': 'application/json' };
  if (!a || a === '--list') {
    const j = await (await fetch('https://www.googleapis.com/webmasters/v3/sites', { headers: H })).json();
    console.log('Service-Account:', key.client_email);
    console.log(JSON.stringify(j.siteEntry || j, null, 1)); return;
  }
  const site = a, days = Number(b || 90), out = c;
  const end = new Date(); end.setDate(end.getDate() - 2);            // GSC hat ~2 Tage Verzug
  const start = new Date(end); start.setDate(start.getDate() - days);
  const q = async (dimensions, rowLimit = 500) => {
    const r = await fetch(`https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(site)}/searchAnalytics/query`,
      { method: 'POST', headers: H, body: JSON.stringify({ startDate: iso(start), endDate: iso(end), dimensions, rowLimit, dataState: 'final' }) });
    const j = await r.json(); if (!r.ok) throw new Error(`${r.status} ${JSON.stringify(j)}`); return j.rows || [];
  };
  const fmt = (rows, n) => rows.map(r => ({ keys: r.keys, clicks: r.clicks, impressions: r.impressions,
    ctr: +(r.ctr * 100).toFixed(1), position: +r.position.toFixed(1) })).slice(0, n);
  const queries = fmt(await q(['query']), 300);
  const pages = fmt(await q(['page']), 200);
  const qp = fmt(await q(['query', 'page'], 1000), 1000);
  // Chancen: Impressionen da, aber Position 8–30 (Seite 1 unten / Seite 2–3) → Text schärfen lohnt
  const chancen = queries.filter(r => r.impressions >= 20 && r.position > 8 && r.position <= 30)
    .sort((x, y) => y.impressions - x.impressions).slice(0, 60);
  const result = { site, range: { start: iso(start), end: iso(end), days },
    totals: { clicks: queries.reduce((s, r) => s + r.clicks, 0), impressions: queries.reduce((s, r) => s + r.impressions, 0) },
    queries, pages, query_page: qp, chancen };
  if (out) { writeFileSync(out, JSON.stringify(result, null, 1)); console.log('written', out); }
  console.log(`${site}  ${iso(start)}→${iso(end)}  clicks=${result.totals.clicks} impressions=${result.totals.impressions}`);
  console.log('Top-Queries:'); for (const r of queries.slice(0, 15)) console.log(`  ${r.keys[0]}  ${r.clicks}c/${r.impressions}i  pos ${r.position}`);
  console.log('Chancen (Pos 8–30, ≥20 Impr.):'); for (const r of chancen.slice(0, 15)) console.log(`  ${r.keys[0]}  ${r.impressions}i  pos ${r.position}`);
})().catch(e => { console.error('FEHLER:', e.message); process.exit(1); });
