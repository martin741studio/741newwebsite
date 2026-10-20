// READ-ONLY: list sitemaps registered for the property (webmasters.readonly)
import { readFileSync, writeFileSync } from 'node:fs';
import { createSign } from 'node:crypto';
const KEY = JSON.parse(readFileSync('/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json', 'utf8'));
const b64u = b => Buffer.from(b).toString('base64').replace(/=/g,'').replace(/\+/g,'-').replace(/\//g,'_');
const now = Math.floor(Date.now()/1000);
const u = `${b64u(JSON.stringify({alg:'RS256',typ:'JWT'}))}.${b64u(JSON.stringify({iss:KEY.client_email,scope:'https://www.googleapis.com/auth/webmasters.readonly',aud:'https://oauth2.googleapis.com/token',iat:now,exp:now+3600}))}`;
const s = createSign('RSA-SHA256'); s.update(u);
const t = (await (await fetch('https://oauth2.googleapis.com/token',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams({grant_type:'urn:ietf:params:oauth:grant-type:jwt-bearer',assertion:`${u}.${b64u(s.sign(KEY.private_key))}`})})).json()).access_token;
const H = {Authorization:`Bearer ${t}`};
const sites = await (await fetch('https://www.googleapis.com/webmasters/v3/sites',{headers:H})).json();
const mine = (sites.siteEntry||[]).filter(x=>x.siteUrl.includes('suriya'));
const sm = await fetch('https://www.googleapis.com/webmasters/v3/sites/'+encodeURIComponent('https://suriya-praxis.de/')+'/sitemaps',{headers:H});
writeFileSync(process.argv[2], JSON.stringify({sites_filtered_to_suriya:mine, sitemaps_status:sm.status, sitemaps:await sm.json()},null,1));
console.log('ok', sm.status);
