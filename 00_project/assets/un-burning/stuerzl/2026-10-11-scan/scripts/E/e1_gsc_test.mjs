// READ-ONLY. Tests whether the 741 reporting service account can read Search Console for the STÜRZL domain.
// Prints no secrets. Writes JSON result to argv[2].
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const KEY = JSON.parse(readFileSync('/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json', 'utf8'));
const b64u = b => Buffer.from(b).toString('base64').replace(/=/g,'').replace(/\+/g,'-').replace(/\//g,'_');
async function token() {
  const now = Math.floor(Date.now()/1000);
  const u = `${b64u(JSON.stringify({alg:'RS256',typ:'JWT'}))}.${b64u(JSON.stringify({iss:KEY.client_email,scope:'https://www.googleapis.com/auth/webmasters.readonly',aud:'https://oauth2.googleapis.com/token',iat:now,exp:now+3600}))}`;
  const s = createSign('RSA-SHA256'); s.update(u);
  const r = await fetch('https://oauth2.googleapis.com/token',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams({grant_type:'urn:ietf:params:oauth:grant-type:jwt-bearer',assertion:`${u}.${b64u(s.sign(KEY.private_key))}`})});
  const j = await r.json(); if(!r.ok) throw new Error('token '+r.status+' '+(j.error||'')); return j.access_token;
}
const out = { collected_at: new Date().toISOString(), service_account: KEY.client_email, steps: [] };
const t = await token();
out.steps.push({ step: 'token', ok: true });
const H = {Authorization:`Bearer ${t}`,'Content-Type':'application/json'};
// 1 sites.list
let r = await fetch('https://www.googleapis.com/webmasters/v3/sites',{headers:H});
let j = await r.json();
out.steps.push({ step: 'sites.list', http_status: r.status, sites: (j.siteEntry||[]).map(s=>({siteUrl:s.siteUrl,permissionLevel:s.permissionLevel})), error: j.error?.message || null });
const props = ['sc-domain:stuerzl-steuerstrafrecht.de','https://stuerzl-steuerstrafrecht.de/','https://www.stuerzl-steuerstrafrecht.de/'];
const urls = ['https://www.stuerzl-steuerstrafrecht.de/','https://www.stuerzl-steuerstrafrecht.de/index.php/steuerstrafrecht','https://www.stuerzl-steuerstrafrecht.de/index.php/selbstanzeigen-steuerliche-korrekturen'];
// 2 searchAnalytics (1 tiny query) per property
for (const p of props) {
  r = await fetch(`https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(p)}/searchAnalytics/query`,{method:'POST',headers:H,body:JSON.stringify({startDate:'2026-09-01',endDate:'2026-09-30',dimensions:['page'],rowLimit:1})});
  j = await r.json();
  out.steps.push({ step: 'searchAnalytics.query', property: p, http_status: r.status, error: j.error?.message || null, rows: j.rows ? j.rows.length : null });
}
// 3 URL inspection on 3 URLs for each property
for (const p of props) for (const u of urls) {
  r = await fetch('https://searchconsole.googleapis.com/v1/urlInspection/index:inspect',{method:'POST',headers:H,body:JSON.stringify({inspectionUrl:u,siteUrl:p,languageCode:'de'})});
  j = await r.json();
  out.steps.push({ step: 'urlInspection.inspect', property: p, url: u, http_status: r.status, error: j.error?.message || null, coverageState: j.inspectionResult?.indexStatusResult?.coverageState || null });
  await new Promise(r=>setTimeout(r,700));
}
writeFileSync(process.argv[2], JSON.stringify(out,null,1));
for (const s of out.steps) console.log(s.step, s.property||'', s.url||'', s.http_status||'', s.error||'');
