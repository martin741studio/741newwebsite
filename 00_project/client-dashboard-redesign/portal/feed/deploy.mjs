#!/usr/bin/env node
/**
 * Manual upload step. The refresh job (build.mjs) never uploads. This script does, only when somebody runs it.
 *   node portal/feed/deploy.mjs feeds [--client bali,huewel,...]      upload out/<slug>/dashboard.json to clients.741.studio/r/<feed_hash>/dashboard.json
 *   node portal/feed/deploy.mjs portal <file.html> <backupName>       back up the live index.html (same bytes as the live file) into clients.741.studio/backup/, then upload <file.html> to
 *                                                                      clients.741.studio/staging/index.html and clients.741.studio/index.html
 * Creds: .env CLIENTS_FTP_*. The path always starts with clients.741.studio/ (the FTP root is the web root of 741.studio, no public_html).
 */
import { readFileSync, existsSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, resolve } from 'node:path';
import { Client } from 'basic-ftp';

const HERE = dirname(fileURLToPath(import.meta.url)), ROOT = resolve(HERE, '../../../..');
const env = Object.fromEntries(readFileSync(join(ROOT, '.env'), 'utf8').split('\n').filter(l => /^CLIENTS_FTP_/.test(l)).map(l => { const i = l.indexOf('='); return [l.slice(0, i), l.slice(i + 1).replace(/^["']|["']$/g, '')]; }));
const [mode, ...rest] = process.argv.slice(2);
const ci = process.argv.indexOf('--client');
const all = ['bali', 'huewel', 'dumann', 'johni', 'stuerzl'];
const slugs = ci > 0 ? process.argv[ci + 1].split(',') : all;
const c = new Client(); c.ftp.verbose = false;
const curl = async url => { const r = await fetch(url + (url.includes('?') ? '&' : '?') + 'cb=' + Date.now()); return { status: r.status, text: await r.text(), lm: r.headers.get('last-modified') }; };
try {
  await c.access({ host: env.CLIENTS_FTP_HOST, user: env.CLIENTS_FTP_USER, password: env.CLIENTS_FTP_PASSWORD, secure: false });
  if (mode === 'feeds') {
    for (const s of slugs) {
      const cfg = JSON.parse(readFileSync(join(HERE, 'clients', `${s}.json`), 'utf8')), f = join(HERE, 'out', s, 'dashboard.json');
      if (!cfg.feed_hash || !existsSync(f)) { console.error(`skip ${s}: no feed_hash or no file`); continue; }
      const j = JSON.parse(readFileSync(f, 'utf8'));
      if (j.meta?.client_id !== cfg.client_id) { console.error(`STOP ${s}: client_id in the feed does not match the config`); process.exit(1); }
      await c.cd('/'); await c.ensureDir(`clients.741.studio/r/${cfg.feed_hash}`); await c.uploadFrom(f, 'dashboard.json');   // always start from the FTP root
      const url = `https://clients.741.studio/r/${cfg.feed_hash}/dashboard.json`, v = await curl(url);
      const same = v.status === 200 && JSON.parse(v.text).meta.as_of === j.meta.as_of && JSON.parse(v.text).meta.refresh.generated_at === j.meta.refresh.generated_at;
      console.log(`${same ? 'ok   ' : 'CHECK'} ${s} ${url} status ${v.status}${same ? ' (content equals the local file)' : ''}`);
    }
  } else if (mode === 'portal') {
    const [file, backupName] = rest; if (!file || !backupName || !existsSync(file)) { console.error('usage: portal <file.html> <backupName>'); process.exit(1); }
    const live = await curl('https://clients.741.studio/index.html'); if (live.status !== 200 || live.text.length < 100000) { console.error('live file not readable, stop'); process.exit(1); }
    const tmp = join(HERE, 'out', '.live-backup.html'); writeFileSync(tmp, live.text);
    await c.ensureDir('clients.741.studio/backup'); await c.uploadFrom(tmp, backupName); console.log('backup', backupName, live.text.length, 'bytes, live Last-Modified', live.lm);
    await c.cd('/'); await c.ensureDir('clients.741.studio/staging'); await c.uploadFrom(file, 'index.html');
    await c.cd('/'); await c.ensureDir('clients.741.studio'); await c.uploadFrom(file, 'index.html');
    const v = await curl('https://clients.741.studio/index.html'); console.log('live now', v.status, v.text.length, 'bytes (file', readFileSync(file).length, ')');
  } else { console.error('usage: feeds | portal'); process.exit(1); }
} finally { c.close(); }
