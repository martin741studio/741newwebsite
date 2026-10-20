// READ-ONLY. Tests Search Console URL Inspection API. Usage: node e1_inspect.mjs sites | test | run <urlsfile>
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
const mode = process.argv[2];
const SITE = 'https://suriya-praxis.de/';
const t = await token();
const H = {Authorization:`Bearer ${t}`,'Content-Type':'application/json'};
if (mode === 'sites') {
  const r = await fetch('https://www.googleapis.com/webmasters/v3/sites',{headers:H});
  const j = await r.json();
  console.log(JSON.stringify({status:r.status, sites:(j.siteEntry||[]).map(s=>({siteUrl:s.siteUrl,permissionLevel:s.permissionLevel})), error:j.error?.message}));
} else {
  const urls = JSON.parse(readFileSync(process.argv[3],'utf8'));
  const out = [];
  for (const u of urls) {
    const r = await fetch('https://searchconsole.googleapis.com/v1/urlInspection/index:inspect',{method:'POST',headers:H,body:JSON.stringify({inspectionUrl:u,siteUrl:SITE,languageCode:'de'})});
    const j = await r.json();
    out.push({url:u,http_status:r.status,collected_at:new Date().toISOString(),response:j});
    console.log(r.status, u, j.inspectionResult?.indexStatusResult?.coverageState || j.error?.message);
    if (r.status === 429) { console.log('quota hit, stop'); break; }
    await new Promise(r=>setTimeout(r,700));
  }
  writeFileSync(process.argv[4] || '/dev/null', JSON.stringify(out,null,1));
}
