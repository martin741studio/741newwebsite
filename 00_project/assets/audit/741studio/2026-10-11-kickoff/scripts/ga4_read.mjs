import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const KEY = JSON.parse(readFileSync('/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json', 'utf8'));
const b64 = b => Buffer.from(b).toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
const now = Math.floor(Date.now() / 1000);
const h = b64(JSON.stringify({ alg: 'RS256', typ: 'JWT' })), c = b64(JSON.stringify({ iss: KEY.client_email, scope: 'https://www.googleapis.com/auth/analytics.readonly', aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600 }));
const s = createSign('RSA-SHA256'); s.update(`${h}.${c}`);
const tr = await (await fetch('https://oauth2.googleapis.com/token', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: `${h}.${c}.${b64(s.sign(KEY.private_key))}` }) })).json();
const tok = tr.access_token; const out = { collected_at: new Date().toISOString(), properties: {} };
const rep = async (prop, body) => { const r = await fetch(`https://analyticsdata.googleapis.com/v1beta/${prop}:runReport`, { method: 'POST', headers: { Authorization: `Bearer ${tok}`, 'Content-Type': 'application/json' }, body: JSON.stringify(body) }); return { status: r.status, json: await r.json() }; };
const dr = [{ startDate: '28daysAgo', endDate: 'yesterday' }];
for (const p of ['properties/363739406', 'properties/380342026']) {
  const o = {};
  o.totals = await rep(p, { dateRanges: dr, metrics: [{ name: 'sessions' }, { name: 'activeUsers' }, { name: 'keyEvents' }, { name: 'screenPageViews' }] });
  if (o.totals.status === 200) {
    o.channels = await rep(p, { dateRanges: dr, dimensions: [{ name: 'sessionDefaultChannelGroup' }], metrics: [{ name: 'sessions' }, { name: 'keyEvents' }], orderBys: [{ metric: { metricName: 'sessions' }, desc: true }], limit: 10 });
    o.countries = await rep(p, { dateRanges: dr, dimensions: [{ name: 'country' }], metrics: [{ name: 'sessions' }], orderBys: [{ metric: { metricName: 'sessions' }, desc: true }], limit: 8 });
    o.events = await rep(p, { dateRanges: dr, dimensions: [{ name: 'eventName' }], metrics: [{ name: 'eventCount' }], orderBys: [{ metric: { metricName: 'eventCount' }, desc: true }], limit: 15 });
    o.hosts = await rep(p, { dateRanges: dr, dimensions: [{ name: 'hostName' }], metrics: [{ name: 'sessions' }], limit: 6 });
  }
  out.properties[p] = o;
}
writeFileSync(process.argv[2], JSON.stringify(out, null, 1));
const rows = j => (j?.json?.rows || []).map(r => r.dimensionValues.map(d => d.value).join('/') + '=' + r.metricValues.map(m => m.value).join(','));
for (const [p, o] of Object.entries(out.properties)) { console.log(p, o.totals.status, JSON.stringify(o.totals.json.rows || o.totals.json.error?.message).slice(0, 200)); if (o.channels) { console.log(' channels', rows(o.channels).join(' | ')); console.log(' countries', rows(o.countries).join(' | ')); console.log(' events', rows(o.events).join(' | ')); console.log(' hosts', rows(o.hosts).join(' | ')); } }
