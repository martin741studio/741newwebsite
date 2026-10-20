#!/usr/bin/env node
import { readFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const KEY = JSON.parse(readFileSync(new URL('../.secrets/ga-sc-reporting-bot.json', import.meta.url)));
const SCOPES = ['https://www.googleapis.com/auth/analytics.readonly','https://www.googleapis.com/auth/webmasters.readonly'].join(' ');
const b64=b=>Buffer.from(b).toString('base64').replace(/=/g,'').replace(/\+/g,'-').replace(/\//g,'_');
async function token(){
  const now=Math.floor(Date.now()/1000);
  const h=b64(JSON.stringify({alg:'RS256',typ:'JWT'}));
  const c=b64(JSON.stringify({iss:KEY.client_email,scope:SCOPES,aud:'https://oauth2.googleapis.com/token',iat:now,exp:now+3600}));
  const s=createSign('RSA-SHA256'); s.update(`${h}.${c}`);
  const jwt=`${h}.${c}.${b64(s.sign(KEY.private_key))}`;
  const r=await fetch('https://oauth2.googleapis.com/token',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},
    body:new URLSearchParams({grant_type:'urn:ietf:params:oauth:grant-type:jwt-bearer',assertion:jwt})});
  const j=await r.json(); if(!r.ok) throw new Error(JSON.stringify(j)); return j.access_token;
}
const T = await token();
const get=async(u)=>{const r=await fetch(u,{headers:{Authorization:`Bearer ${T}`}});return {ok:r.ok,status:r.status,j:await r.json().catch(()=>({}))};};
const post=async(u,b)=>{const r=await fetch(u,{method:'POST',headers:{Authorization:`Bearer ${T}`,'Content-Type':'application/json'},body:JSON.stringify(b)});return {ok:r.ok,status:r.status,j:await r.json().catch(()=>({}))};};

// find the 741.studio GA4 property
const accs = await get('https://analyticsadmin.googleapis.com/v1beta/accountSummaries?pageSize=200');
let found=[];
for (const a of (accs.j.accountSummaries||[])) for (const p of (a.propertySummaries||[]))
  if (/741/i.test(p.displayName) || /741/i.test(a.displayName)) found.push({acct:a.displayName, prop:p.displayName, id:p.property});
console.log('GA4 candidate properties:'); found.forEach(f=>console.log('  ',f.id, '|', f.prop, '| acct:', f.acct));
console.log('TOTAL accounts visible:', (accs.j.accountSummaries||[]).length, 'status', accs.status);
