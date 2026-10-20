// Read-only Google API helper (service account "reporting-bot"). Scopes: Search Console read-only, Analytics read-only.
// Dependency-free: signs the JWT with node:crypto. The key file is read, never printed.
import { readFileSync } from 'node:fs';
import { createSign } from 'node:crypto';

const KEY_PATH = new URL('../../../../.secrets/ga-sc-reporting-bot.json', import.meta.url);
const b64url = b => Buffer.from(b).toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
const cache = {};

export async function gToken(scope) {
  if (cache[scope]) return cache[scope];
  const key = JSON.parse(readFileSync(KEY_PATH, 'utf8'));
  const now = Math.floor(Date.now() / 1000);
  const unsigned = `${b64url(JSON.stringify({ alg: 'RS256', typ: 'JWT' }))}.${b64url(JSON.stringify({
    iss: key.client_email, scope, aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600 }))}`;
  const s = createSign('RSA-SHA256'); s.update(unsigned);
  const jwt = `${unsigned}.${b64url(s.sign(key.private_key))}`;
  const r = await fetch('https://oauth2.googleapis.com/token', { method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: jwt }) });
  const j = await r.json(); if (!r.ok) throw new Error('token: ' + (j.error_description || j.error || r.status));
  return (cache[scope] = j.access_token);
}

async function post(url, scope, body) {
  const r = await fetch(url, { method: 'POST', headers: { Authorization: `Bearer ${await gToken(scope)}`, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  const j = await r.json(); if (!r.ok) throw new Error(`${r.status} ${JSON.stringify(j.error || j).slice(0, 300)}`);
  return j;
}
const SC = 'https://www.googleapis.com/auth/webmasters.readonly', GA = 'https://www.googleapis.com/auth/analytics.readonly';

/** Search Console searchAnalytics.query (POST, read-only). */
export const gsc = (site, body) => post(`https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(site)}/searchAnalytics/query`, SC, body);
/** GA4 Data API runReport (POST, read-only). */
export const ga4 = (property, body) => post(`https://analyticsdata.googleapis.com/v1beta/properties/${property}:runReport`, GA, body);
