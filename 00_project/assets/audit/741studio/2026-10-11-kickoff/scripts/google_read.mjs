// Free reads via service account: Search Console (741.studio URL-prefix) and GA4 (account-level viewer). Read only.
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const KEY = JSON.parse(readFileSync('/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json', 'utf8'));
const b64 = b => Buffer.from(b).toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
async function token(scope) {
  const now = Math.floor(Date.now() / 1000);
  const h = b64(JSON.stringify({ alg: 'RS256', typ: 'JWT' })), c = b64(JSON.stringify({ iss: KEY.client_email, scope, aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600 }));
  const s = createSign('RSA-SHA256'); s.update(`${h}.${c}`);
  const r = await fetch('https://oauth2.googleapis.com/token', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: `${h}.${c}.${b64(s.sign(KEY.private_key))}` }) });
  const j = await r.json(); if (!r.ok) throw new Error(JSON.stringify(j)); return j.access_token;
}
const out = { collected_at: new Date().toISOString() };
const post = async (url, tok, body) => { const r = await fetch(url, { method: 'POST', headers: { Authorization: `Bearer ${tok}`, 'Content-Type': 'application/json' }, body: JSON.stringify(body) }); return { status: r.status, json: await r.json().catch(() => ({})) }; };
const get = async (url, tok) => { const r = await fetch(url, { headers: { Authorization: `Bearer ${tok}` } }); return { status: r.status, json: await r.json().catch(() => ({})) }; };
const SITE = encodeURIComponent('https://741.studio/');
try {
  const t = await token('https://www.googleapis.com/auth/webmasters.readonly');
  const day = d => new Date(Date.now() - d * 864e5).toISOString().slice(0, 10);
  const q = (dims, n = 25, days = 28) => post(`https://www.googleapis.com/webmasters/v3/sites/${SITE}/searchAnalytics/query`, t, { startDate: day(days + 3), endDate: day(3), dimensions: dims, rowLimit: n });
  out.gsc_total = await q([], 1); out.gsc_queries = await q(['query'], 40); out.gsc_pages = await q(['page'], 40); out.gsc_countries = await q(['country'], 10); out.gsc_devices = await q(['device'], 5);
  out.gsc_total_90 = await post(`https://www.googleapis.com/webmasters/v3/sites/${SITE}/searchAnalytics/query`, t, { startDate: day(93), endDate: day(3), dimensions: [], rowLimit: 1 });
  out.gsc_sitemaps = await get(`https://www.googleapis.com/webmasters/v3/sites/${SITE}/sitemaps`, t);
  out.gsc_inspect_home = await post('https://searchconsole.googleapis.com/v1/urlInspection/index:inspect', t, { inspectionUrl: 'https://741.studio/', siteUrl: 'https://741.studio/' });
} catch (e) { out.gsc_error = String(e); }
try {
  const t = await token('https://www.googleapis.com/auth/analytics.readonly');
  out.ga_accounts = await get('https://analyticsadmin.googleapis.com/v1beta/accountSummaries?pageSize=50', t);
} catch (e) { out.ga_error = String(e); }
writeFileSync(process.argv[2], JSON.stringify(out, null, 1));
const s = JSON.stringify(out); console.log('bytes', s.length);
console.log('gsc_total', JSON.stringify(out.gsc_total?.json).slice(0, 300)); console.log('gsc_90', JSON.stringify(out.gsc_total_90?.json).slice(0, 300)); console.log('sitemaps', out.gsc_sitemaps?.status, JSON.stringify(out.gsc_sitemaps?.json).slice(0, 600)); console.log('inspect', out.gsc_inspect_home?.status, JSON.stringify(out.gsc_inspect_home?.json).slice(0, 700));
const props = (out.ga_accounts?.json?.accountSummaries || []).flatMap(a => (a.propertySummaries || []).map(p => `${a.displayName} | ${p.property} | ${p.displayName}`)); console.log(props.filter(x => /741|studio/i.test(x)).join('\n'));
