// Read-only Search Console pull for danieladumann.de (service account reporting-bot). Output: data/gsc.json
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const ROOT = '/Users/martindrendel/741website';
const key = JSON.parse(readFileSync(`${ROOT}/.secrets/ga-sc-reporting-bot.json`, 'utf8'));
const b64 = b => Buffer.from(b).toString('base64').replace(/=/g,'').replace(/\+/g,'-').replace(/\//g,'_');
async function token(){const now=Math.floor(Date.now()/1000);const u=`${b64(JSON.stringify({alg:'RS256',typ:'JWT'}))}.${b64(JSON.stringify({iss:key.client_email,scope:'https://www.googleapis.com/auth/webmasters.readonly',aud:'https://oauth2.googleapis.com/token',iat:now,exp:now+3600}))}`;const s=createSign('RSA-SHA256');s.update(u);const jwt=`${u}.${b64(s.sign(key.private_key))}`;const r=await fetch('https://oauth2.googleapis.com/token',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams({grant_type:'urn:ietf:params:oauth:grant-type:jwt-bearer',assertion:jwt})});const j=await r.json();if(!r.ok)throw new Error(JSON.stringify(j));return j.access_token;}
const site='https://www.danieladumann.de/';
const t=await token();const H={Authorization:`Bearer ${t}`,'Content-Type':'application/json'};
const q=async(body)=>{const r=await fetch(`https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(site)}/searchAnalytics/query`,{method:'POST',headers:H,body:JSON.stringify({dataState:'final',...body})});const j=await r.json();if(!r.ok)throw new Error(r.status+JSON.stringify(j));return j.rows||[]};
const r2=x=>x.map(r=>({keys:r.keys,clicks:r.clicks,impressions:r.impressions,ctr:+(r.ctr*100).toFixed(1),position:+r.position.toFixed(1)}));
const out={site,fetched:new Date().toISOString()};
out.monthly=r2(await q({startDate:'2026-04-01',endDate:'2026-10-12',dimensions:['date'],rowLimit:1000}));
out.pages90=r2(await q({startDate:'2026-07-14',endDate:'2026-10-11',dimensions:['page'],rowLimit:60}));
out.queries90=r2(await q({startDate:'2026-07-14',endDate:'2026-10-11',dimensions:['query'],rowLimit:80}));
writeFileSync('/Users/martindrendel/741website/00_project/assets/dumann/status-2026-10-13/data/gsc.json',JSON.stringify(out,null,1));
console.log(out.monthly.length,out.pages90.length,out.queries90.length, out.monthly[0].keys, out.monthly.at(-1).keys);
