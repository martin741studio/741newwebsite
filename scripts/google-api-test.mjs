#!/usr/bin/env node
/**
 * Live-Test der Google-APIs über den Service-Account "reporting-bot".
 * Liest read-only: GA4 (Admin + Data API) und Search Console.
 * Keine externen Pakete – nur Node-Builtins (crypto, fetch).
 *
 *   node scripts/google-api-test.mjs
 */
import { readFileSync } from 'node:fs';
import { createSign } from 'node:crypto';

const KEY_PATH = new URL('../.secrets/ga-sc-reporting-bot.json', import.meta.url);
const SC_SITE = 'https://741.studio/';           // Search-Console URL-Präfix-Property
const SCOPES = [
  'https://www.googleapis.com/auth/analytics.readonly',
  'https://www.googleapis.com/auth/webmasters.readonly',
].join(' ');

const b64url = (buf) =>
  Buffer.from(buf).toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');

function iso(d) { return d.toISOString().slice(0, 10); }

// ---- 1) OAuth2 access token via signed JWT ----
async function getAccessToken(key) {
  const now = Math.floor(Date.now() / 1000);
  const header = b64url(JSON.stringify({ alg: 'RS256', typ: 'JWT' }));
  const claim = b64url(JSON.stringify({
    iss: key.client_email, scope: SCOPES,
    aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600,
  }));
  const signer = createSign('RSA-SHA256');
  signer.update(`${header}.${claim}`);
  const jwt = `${header}.${claim}.${b64url(signer.sign(key.private_key))}`;

  const res = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
      assertion: jwt,
    }),
  });
  const j = await res.json();
  if (!res.ok) throw new Error(`Token error: ${JSON.stringify(j)}`);
  return j.access_token;
}

const api = async (url, token, opts = {}) => {
  const res = await fetch(url, {
    ...opts,
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json', ...(opts.headers || {}) },
  });
  const j = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(`${res.status} ${url}\n${JSON.stringify(j)}`);
  return j;
};

(async () => {
  const key = JSON.parse(readFileSync(KEY_PATH, 'utf8'));
  console.log(`🔑 Service-Account: ${key.client_email}\n`);
  const token = await getAccessToken(key);
  console.log('✅ Access-Token erhalten.\n');

  // ---- 2) GA4 Admin API: alle zugänglichen Properties ----
  console.log('── GA4: zugängliche Properties (Admin API) ─────────────');
  const summaries = await api('https://analyticsadmin.googleapis.com/v1beta/accountSummaries?pageSize=200', token);
  const props = [];
  for (const acc of summaries.accountSummaries || []) {
    for (const p of acc.propertySummaries || []) {
      props.push({ name: p.property, display: p.displayName, account: acc.displayName });
    }
  }
  console.log(`Gefundene Properties: ${props.length}`);
  for (const p of props) console.log(`  • ${p.display}  (${p.name})  [Konto: ${p.account}]`);
  console.log();

  // 741.studio-eigene Property finden (Fallback: erste)
  const own = props.find((p) => /741/i.test(p.display)) || props[0];

  // ---- 3) GA4 Data API: 7-Tage-Report für eine Property ----
  if (own) {
    console.log(`── GA4: 7-Tage-Report für "${own.display}" ────────────`);
    const end = new Date(); const start = new Date(Date.now() - 7 * 864e5);
    const report = await api(
      `https://analyticsdata.googleapis.com/v1beta/${own.name}:runReport`,
      token,
      {
        method: 'POST',
        body: JSON.stringify({
          dateRanges: [{ startDate: iso(start), endDate: iso(end) }],
          dimensions: [{ name: 'sessionDefaultChannelGroup' }],
          metrics: [{ name: 'activeUsers' }, { name: 'sessions' }],
          limit: 10,
        }),
      },
    );
    const totalUsers = report.totals?.[0]?.metricValues?.[0]?.value ?? '0';
    console.log(`Aktive Nutzer (7 Tage gesamt): ${totalUsers}`);
    for (const row of report.rows || []) {
      console.log(`  • ${row.dimensionValues[0].value}: ${row.metricValues[0].value} Nutzer / ${row.metricValues[1].value} Sessions`);
    }
    console.log();
  }

  // ---- 4) Search Console: Top-Suchbegriffe 28 Tage ----
  console.log(`── Search Console: Top-Suchbegriffe für ${SC_SITE} (28 Tage) ──`);
  const end = new Date(); const start = new Date(Date.now() - 28 * 864e5);
  const sc = await api(
    `https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(SC_SITE)}/searchAnalytics/query`,
    token,
    {
      method: 'POST',
      body: JSON.stringify({
        startDate: iso(start), endDate: iso(end),
        dimensions: ['query'], rowLimit: 10,
      }),
    },
  );
  if (!sc.rows || sc.rows.length === 0) {
    console.log('  (keine Query-Daten im Zeitraum – normal bei wenig Traffic)');
  } else {
    for (const r of sc.rows) {
      console.log(`  • "${r.keys[0]}"  –  ${r.clicks} Klicks, ${r.impressions} Impr., Pos. ${r.position.toFixed(1)}`);
    }
  }
  console.log('\n🎉 Alle API-Aufrufe erfolgreich – GA4 + Search Console sind angebunden.');
})().catch((e) => { console.error('\n❌ Fehler:', e.message); process.exit(1); });
