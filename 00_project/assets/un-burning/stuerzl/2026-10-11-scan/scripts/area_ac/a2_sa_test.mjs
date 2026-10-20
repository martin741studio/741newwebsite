// READ-ONLY test: can the reporting service account read GA4 483853149 or Search Console for the client domain?
// Prints status codes and non-secret result fields only. Never prints the key or the token.
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const KEY = JSON.parse(readFileSync('/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json', 'utf8'));
const b64u = (b) => Buffer.from(b).toString('base64').replace(/=/g,'').replace(/\+/g,'-').replace(/\//g,'_');
async function token(scope) {
  const now = Math.floor(Date.now()/1000);
  const u = `${b64u(JSON.stringify({alg:'RS256',typ:'JWT'}))}.${b64u(JSON.stringify({iss:KEY.client_email,scope,aud:'https://oauth2.googleapis.com/token',iat:now,exp:now+3600}))}`;
  const s = createSign('RSA-SHA256'); s.update(u);
  const r = await fetch('https://oauth2.googleapis.com/token',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams({grant_type:'urn:ietf:params:oauth:grant-type:jwt-bearer',assertion:`${u}.${b64u(s.sign(KEY.private_key))}`})});
  const j = await r.json(); if (!r.ok) return {err: r.status+' '+(j.error||'')};
  return {tok: j.access_token};
}
const out = { service_account: KEY.client_email, tests: [] };
const t = (name, status, body) => { out.tests.push({name, status, body}); };
// 1 GSC site list
let a = await token('https://www.googleapis.com/auth/webmasters.readonly');
if (a.err) t('gsc_token', 'fail', a.err); else {
  const r = await fetch('https://www.googleapis.com/webmasters/v3/sites',{headers:{Authorization:'Bearer '+a.tok}});
  const j = await r.json();
  const entries = (j.siteEntry||[]).map(e=>({siteUrl:e.siteUrl,permissionLevel:e.permissionLevel}));
  t('gsc_sites_list', r.status, {total_properties_visible: entries.length, stuerzl_matches: entries.filter(e=>/stuerzl/i.test(e.siteUrl)), error: j.error?.message});
  for (const site of ['sc-domain:stuerzl-steuerstrafrecht.de','https://stuerzl-steuerstrafrecht.de/','https://www.stuerzl-steuerstrafrecht.de/']) {
    const r2 = await fetch('https://www.googleapis.com/webmasters/v3/sites/'+encodeURIComponent(site),{headers:{Authorization:'Bearer '+a.tok}});
    const j2 = await r2.json();
    t('gsc_site_get '+site, r2.status, j2.error ? {error: j2.error.message} : j2);
  }
}
// 2 GA4
let g = await token('https://www.googleapis.com/auth/analytics.readonly');
if (g.err) t('ga4_token','fail',g.err); else {
  const r = await fetch('https://analyticsadmin.googleapis.com/v1beta/accountSummaries?pageSize=200',{headers:{Authorization:'Bearer '+g.tok}});
  const j = await r.json();
  const props = (j.accountSummaries||[]).flatMap(a=>(a.propertySummaries||[]).map(p=>({account:a.displayName,property:p.property,name:p.displayName})));
  t('ga4_account_summaries', r.status, {properties_visible: props.length, matches_483853149: props.filter(p=>p.property==='properties/483853149'), error: j.error?.message});
  const r3 = await fetch('https://analyticsdata.googleapis.com/v1beta/properties/483853149:runReport',{method:'POST',headers:{Authorization:'Bearer '+g.tok,'Content-Type':'application/json'},body:JSON.stringify({dateRanges:[{startDate:'7daysAgo',endDate:'yesterday'}],metrics:[{name:'activeUsers'}]})});
  const j3 = await r3.json();
  t('ga4_runReport_483853149', r3.status, j3.error ? {error: j3.error.message, reason: j3.error.status} : {rows: j3.rows, rowCount: j3.rowCount});
}
writeFileSync(process.argv[2], JSON.stringify(out,null,1));
console.log(JSON.stringify(out,null,1));
