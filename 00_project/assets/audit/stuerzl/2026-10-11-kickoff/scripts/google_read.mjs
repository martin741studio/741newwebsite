// Phase 1: GA4 + Search Console read via service account. Read only. Reports access status honestly.
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const KEY = JSON.parse(readFileSync('/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json', 'utf8'));
const b64 = b => Buffer.from(b).toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
async function token(scope) {
  const now = Math.floor(Date.now() / 1000);
  const h = b64(JSON.stringify({ alg: 'RS256', typ: 'JWT' }));
  const c = b64(JSON.stringify({ iss: KEY.client_email, scope, aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600 }));
  const s = createSign('RSA-SHA256'); s.update(`${h}.${c}`);
  const r = await fetch('https://oauth2.googleapis.com/token', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: `${h}.${c}.${b64(s.sign(KEY.private_key))}` }) });
  const j = await r.json(); if (!r.ok) throw new Error(JSON.stringify(j)); return j.access_token;
}
const out = { collected_at: new Date().toISOString(), sa: KEY.client_email };
async function post(url, tok, body) { const r = await fetch(url, { method: 'POST', headers: { Authorization: `Bearer ${tok}`, 'Content-Type': 'application/json' }, body: JSON.stringify(body) }); return { status: r.status, json: await r.json().catch(() => ({})) }; }
try {
  const t = await token('https://www.googleapis.com/auth/analytics.readonly');
  const dr = [{ startDate: '28daysAgo', endDate: 'yesterday' }];
  out.ga4_channels = await post('https://analyticsdata.googleapis.com/v1beta/properties/483853149:runReport', t, { dateRanges: dr, dimensions: [{ name: 'sessionDefaultChannelGroup' }], metrics: [{ name: 'sessions' }, { name: 'keyEvents' }] });
} catch (e) { out.ga4_error = String(e); }
try {
  const t = await token('https://www.googleapis.com/auth/webmasters.readonly');
  const end = new Date(Date.now() - 3 * 864e5).toISOString().slice(0, 10), start = new Date(Date.now() - 31 * 864e5).toISOString().slice(0, 10);
  out.gsc_query = await post('https://www.googleapis.com/webmasters/v3/sites/sc-domain%3Astuerzl-steuerstrafrecht.de/searchAnalytics/query', t, { startDate: start, endDate: end, dimensions: ['query'], rowLimit: 25 });
  out.gsc_sites = await fetch('https://www.googleapis.com/webmasters/v3/sites', { headers: { Authorization: `Bearer ${t}` } }).then(async r => ({ status: r.status, json: await r.json().catch(() => ({})) }));
} catch (e) { out.gsc_error = String(e); }
const slim = JSON.stringify(out, null, 1);
writeFileSync(new URL('../evidence/google-read-2026-10-11.json', import.meta.url), slim);
console.log(slim.slice(0, 2500));
