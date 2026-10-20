#!/usr/bin/env node
/**
 * One command for the weekly refresh of all client feeds.
 *   node portal/feed/refresh.mjs                      build + check every client, print a summary. Uploads nothing.
 *   node portal/feed/refresh.mjs --only bali,huewel   only these clients
 *   node portal/feed/refresh.mjs --deploy             after a clean build and check, also upload the feeds (deploy.mjs feeds). Only when somebody decides to.
 * Exit code: 0 = all clients built and checked, 1 = a build or check failed, 2 = a source failed (partial feed).
 * A missing grant (403) is a known gap, not a failure: the block stays empty and the summary lists it.
 */
import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const HERE = dirname(fileURLToPath(import.meta.url));
const arg = n => { const i = process.argv.indexOf('--' + n); return i < 0 ? null : (process.argv[i + 1] && !process.argv[i + 1].startsWith('--') ? process.argv[i + 1] : true); };
const ORDER = ['bali', 'huewel', 'dumann', 'stuerzl', 'johni', 'suriya', 'maria', 'rabenmuetter', 'kamil'];
const all = readdirSync(join(HERE, 'clients')).filter(f => /^[a-z]+\.json$/.test(f)).map(f => f.replace('.json', '')).sort((a, b) => (ORDER.indexOf(a) + 99) % 99 - (ORDER.indexOf(b) + 99) % 99);
const only = arg('only'); const slugs = only ? only.split(',') : all;
const run = (script, args) => spawnSync('node', [join(HERE, script), ...args], { encoding: 'utf8', cwd: join(HERE, '../../../..') });
const rows = []; let worst = 0;
for (const s of slugs) {
  const cfg = JSON.parse(readFileSync(join(HERE, 'clients', `${s}.json`), 'utf8'));
  const b = run('build.mjs', ['--client', s]);
  const log = existsSync(join(HERE, 'out', s, 'refresh-log.json')) ? JSON.parse(readFileSync(join(HERE, 'out', s, 'refresh-log.json'), 'utf8')) : { failed: ['no log'], gaps: [], warnings: [] };
  const c = b.status === 1 ? { status: 1 } : run('check.mjs', ['--client', s]);
  const buildState = b.status === 0 ? 'ok' : b.status === 2 ? 'PARTIAL' : 'FAILED';
  const checkState = c.status === 0 ? 'ok' : 'FAILED';
  if (b.status === 2) worst = Math.max(worst, 2); if (b.status === 1 || c.status !== 0) worst = 1;
  rows.push({ s, buildState, checkState, gaps: (log.gaps || []).join(',') || '-', failed: (log.failed || []).join(',') || '-', warn: (log.warnings || []).filter(w => !/no access \(403\)/.test(w)).length, hash: cfg.feed_hash || null, ok: b.status === 0 && c.status === 0 });
  if (cfg.local_falcon !== false) await new Promise(r => setTimeout(r, 20000));   // Local Falcon allows few requests per minute
}
const pad = (x, n) => String(x).padEnd(n);
console.log(`\n${pad('client', 14)}${pad('build', 9)}${pad('check', 8)}${pad('gaps (no access)', 20)}${pad('failed', 18)}warnings`);
for (const r of rows) console.log(`${pad(r.s, 14)}${pad(r.buildState, 9)}${pad(r.checkState, 8)}${pad(r.gaps, 20)}${pad(r.failed, 18)}${r.warn}`);
if (arg('deploy')) {
  const okSlugs = rows.filter(r => r.ok && r.hash).map(r => r.s);
  console.log(`\nDeploy: ${okSlugs.join(', ') || '(none)'}`);
  if (okSlugs.length) { const d = run('deploy.mjs', ['feeds', '--client', okSlugs.join(',')]); process.stdout.write(d.stdout); if (d.status !== 0) { process.stderr.write(d.stderr); worst = 1; } }
} else console.log('\nNothing uploaded. Add --deploy to upload the feeds of the clients that built and checked clean.');
process.exit(worst);
