// Upload local files to a Google Drive folder via the reporting service account.
// Usage: node scripts/drive-upload.mjs <folderId> <file1> [file2 ...]
// Requires: Drive API enabled in the SA's GCP project + folder shared with the SA email (Editor).
import { GoogleAuth } from 'google-auth-library';
import { readFileSync, statSync } from 'node:fs';
import { basename } from 'node:path';

const KEY = '/Users/martindrendel/741website/.secrets/ga-sc-reporting-bot.json';
const [folderId, ...files] = process.argv.slice(2);
if (!folderId || files.length === 0) { console.error('need <folderId> <file...>'); process.exit(1); }

const auth = new GoogleAuth({ keyFile: KEY, scopes: ['https://www.googleapis.com/auth/drive'] });
const client = await auth.getClient();
const { token } = await client.getAccessToken();

function guessMime(f){ return f.endsWith('.png') ? 'image/png' : f.endsWith('.jpg')||f.endsWith('.jpeg') ? 'image/jpeg' : 'application/octet-stream'; }

let ok = 0;
for (const f of files) {
  try {
    const meta = { name: basename(f), parents: [folderId] };
    const mime = guessMime(f);
    const boundary = 'bnd' + Math.random().toString(36).slice(2);
    const pre = `--${boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n${JSON.stringify(meta)}\r\n--${boundary}\r\nContent-Type: ${mime}\r\n\r\n`;
    const post = `\r\n--${boundary}--`;
    const body = Buffer.concat([Buffer.from(pre,'utf8'), readFileSync(f), Buffer.from(post,'utf8')]);
    const res = await fetch('https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&supportsAllDrives=true&fields=id,name', {
      method:'POST',
      headers:{ Authorization:`Bearer ${token}`, 'Content-Type':`multipart/related; boundary=${boundary}` },
      body
    });
    const j = await res.json();
    if (res.ok) { console.log('OK', j.name, j.id); ok++; }
    else { console.error('FAIL', basename(f), res.status, JSON.stringify(j.error?.message||j)); }
  } catch(e){ console.error('ERR', basename(f), e.message); }
}
console.log(`\n${ok}/${files.length} uploaded`);
