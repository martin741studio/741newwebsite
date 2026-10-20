// Deploy Entwurf C (v4) without an empty window: upload to v4_next, then swap folders.
// Run: node 00_project/assets/meandyou/deploy/ftp-v4-safe.mjs   (source: deploy/meandyou/v4 = copy of cro/_site)
import * as ftp from "/Users/martindrendel/741website/node_modules/basic-ftp/dist/index.js";
import dotenv from "/Users/martindrendel/741website/node_modules/dotenv/lib/main.js";
dotenv.config({path:"/Users/martindrendel/741website/.env",quiet:true});
const D="/Users/martindrendel/741website/00_project/assets/meandyou/deploy/meandyou";
const BASE="/clients.741.studio/meandyou";
const c=new ftp.Client(180000);
await c.access({host:process.env.CLIENTS_FTP_HOST,user:process.env.CLIENTS_FTP_USER,password:process.env.CLIENTS_FTP_PASSWORD,secure:false});
// 1. upload the full new version next to the live one; the live v4 stays untouched
await c.cd(BASE); await c.ensureDir("v4_next"); await c.clearWorkingDir(); await c.uploadFromDir(D+"/v4");
// 2. swap: live v4 -> v4_prev, v4_next -> v4 (two renames, the gap is under a second)
await c.cd(BASE);
const names=(await c.list()).map(f=>f.name);
if(names.includes("v4_prev")) await c.removeDir("v4_prev");
if(names.includes("v4")) await c.rename("v4","v4_prev");
await c.rename("v4_next","v4");
// 3. overview page, then remove the old version
await c.uploadFrom(D+"/index.html","index.html");
await c.cd(BASE); await c.removeDir("v4_prev");
console.log("ok: v4 swapped"); c.close();
