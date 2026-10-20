// Free: Search Console URL Inspection API for a sample of 741.studio URLs. Read only.
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const KEY = JSON.parse(readFileSync('/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json', 'utf8'));
const b64 = b => Buffer.from(b).toString('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
const now = Math.floor(Date.now() / 1000);
const h = b64(JSON.stringify({ alg: 'RS256', typ: 'JWT' })), c = b64(JSON.stringify({ iss: KEY.client_email, scope: 'https://www.googleapis.com/auth/webmasters.readonly', aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600 }));
const s = createSign('RSA-SHA256'); s.update(`${h}.${c}`);
const tok = (await (await fetch('https://oauth2.googleapis.com/token', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: `${h}.${c}.${b64(s.sign(KEY.private_key))}` }) })).json()).access_token;
const urls = ['https://741.studio/', 'https://741.studio/de/', 'https://741.studio/pages/about.html', 'https://741.studio/pages/local-seo.html', 'https://741.studio/pages/website-design.html', 'https://741.studio/pages/bali-web-design.html', 'https://741.studio/pages/bali-local-seo.html', 'https://741.studio/pages/google-ads-1.html', 'https://741.studio/pages/portfolio_full.html', 'https://741.studio/pages/blog/seo-agency-bali.html', 'https://741.studio/pages/blog/best-local-seo-bali.html', 'https://741.studio/pages/blog/best-web-design-agency-bali.html', 'https://741.studio/pages/blog/best-web-designer-bali.html', 'https://741.studio/pages/blog/premium-web-development-studio-bali.html', 'https://741.studio/pages/visibility-audit.html', 'https://741.studio/pages/blog/n8n-whatsapp-automation.html'];
const out = { collected_at: new Date().toISOString(), results: [] };
for (const u of urls) {
  const r = await fetch('https://searchconsole.googleapis.com/v1/urlInspection/index:inspect', { method: 'POST', headers: { Authorization: `Bearer ${tok}`, 'Content-Type': 'application/json' }, body: JSON.stringify({ inspectionUrl: u, siteUrl: 'https://741.studio/' }) });
  const j = await r.json(); const x = j.inspectionResult?.indexStatusResult || {};
  out.results.push({ url: u, status: r.status, verdict: x.verdict, coverage: x.coverageState, indexing: x.indexingState, lastCrawl: x.lastCrawlTime, googleCanonical: x.googleCanonical, userCanonical: x.userCanonical, error: j.error?.message });
}
writeFileSync(process.argv[2], JSON.stringify(out, null, 1));
for (const r of out.results) console.log(r.verdict || r.error, '|', r.coverage, '|', r.indexing, '|', r.url.replace('https://741.studio', ''), r.googleCanonical && r.googleCanonical !== r.url ? '-> canonical ' + r.googleCanonical : '');
