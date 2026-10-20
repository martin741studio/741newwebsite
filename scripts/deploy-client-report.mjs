#!/usr/bin/env node
/**
 * Report-Seiten ins Kundenportal hochladen (FTP → clients.741.studio/r/<hash>/).
 * Aus dem Repo-Root ausführen (node_modules/basic-ftp liegt dort). Creds: .env CLIENTS_FTP_*.
 *
 *   node scripts/deploy-client-report.mjs <hash> <datei.html> [weitere.html …]
 *   node scripts/deploy-client-report.mjs 8dbd937730d2 /tmp/suriya-seitenbaum.html
 *
 * Danach in Supabase (741-portal) client_reports.storage_path setzen/bumpen:
 *   https://clients.741.studio/r/<hash>/<datei>.html?v=YYYYMMDD
 * Der Hash je Kunde steht in dessen bestehenden storage_path-Werten (select … from client_reports where client_id=…).
 */
import { readFileSync, existsSync } from 'node:fs';
import { basename, resolve } from 'node:path';
import { Client } from 'basic-ftp';

const env = Object.fromEntries(readFileSync(resolve('.env'), 'utf8').split('\n')
  .filter(l => /^CLIENTS_FTP_/.test(l)).map(l => { const i = l.indexOf('='); return [l.slice(0, i), l.slice(i + 1).replace(/^["']|["']$/g, '')]; }));
const [hash, ...files] = process.argv.slice(2);
if (!hash || !files.length) { console.error('usage: deploy-client-report.mjs <hash> <file…>'); process.exit(1); }
for (const f of files) if (!existsSync(f)) { console.error('fehlt:', f); process.exit(1); }

const dir = `clients.741.studio/r/${hash}`;   // ausgelieferter Docroot – NICHT /r/<hash>, KEIN public_html
const c = new Client(); c.ftp.verbose = false;
try {
  await c.access({ host: env.CLIENTS_FTP_HOST, user: env.CLIENTS_FTP_USER, password: env.CLIENTS_FTP_PASSWORD, secure: false });
  await c.ensureDir(dir);            // wechselt hinein (legt bei neuem Kunden den Ordner an)
  for (const f of files) {
    await c.uploadFrom(f, basename(f));
    console.log(`✓ https://clients.741.studio/r/${hash}/${basename(f)}`);
  }
} finally { c.close(); }
