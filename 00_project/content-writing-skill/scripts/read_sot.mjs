// Read-only dump of ALL tabs of a client's Source-of-Truth Google Sheet through the 741 service account.
// Usage: node read_sot.mjs <sheet-id> <out.json>   (Drive MCP only returns tab 00, so use this)
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const [SHEET, OUT] = process.argv.slice(2);
if (!SHEET || !OUT) { console.error('usage: node read_sot.mjs <sheet-id> <out.json>'); process.exit(2); }
const key = JSON.parse(readFileSync('/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json', 'utf8'));
const b64 = s => Buffer.from(s).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
async function token() {
  const now = Math.floor(Date.now() / 1000);
  const h = b64(JSON.stringify({ alg: 'RS256', typ: 'JWT' }));
  const c = b64(JSON.stringify({ iss: key.client_email, scope: 'https://www.googleapis.com/auth/spreadsheets.readonly', aud: key.token_uri, iat: now, exp: now + 3600 }));
  const sg = createSign('RSA-SHA256'); sg.update(`${h}.${c}`);
  const r = await fetch(key.token_uri, { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: `${h}.${c}.${b64(sg.sign(key.private_key))}` }) });
  const j = await r.json(); if (!j.access_token) throw new Error('token: ' + JSON.stringify(j)); return j.access_token;
}
async function api(path) {
  const r = await fetch(`https://sheets.googleapis.com/v4/spreadsheets/${SHEET}${path}`, { headers: { Authorization: 'Bearer ' + await token() } });
  const j = await r.json(); if (!r.ok) throw new Error(`${r.status} ${JSON.stringify(j).slice(0, 300)}`); return j;
}
const meta = await api('?fields=sheets.properties(title)');
const out = {};
for (const s of meta.sheets) {
  const t = s.properties.title;
  const r = await api('/values/' + encodeURIComponent("'" + t + "'") + '?majorDimension=ROWS');
  out[t] = r.values || [];
}
writeFileSync(OUT, JSON.stringify(out, null, 1));
console.log(Object.entries(out).map(([k, v]) => k + ': ' + v.length + ' rows').join('\n'));
