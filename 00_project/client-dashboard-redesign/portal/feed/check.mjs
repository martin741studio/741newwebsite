#!/usr/bin/env node
/**
 * Checks a feed file.  node portal/feed/check.mjs [--client bali|huewel] [feed.json]      (default file: portal/feed/out/<client>/dashboard.json)
 *  1. Schema: same keys and value types as the 13 Oct snapshot (portal/src/feed-bali.json).
 *  2. Render: runs the check of portal/src/smoke.cjs on this file (every view, both profiles; no "undefined", "NaN", "[object").
 *     The smoke file (src/smoke.cjs, or src/smoke.js) is CommonJS. This script runs a patched copy with absolute paths. The smoke file itself is not changed.
 * Exit code 0 = pass, 1 = fail.
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { dirname, join, resolve } from 'node:path';

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(HERE, '../src');
const ci = process.argv.indexOf('--client');
const CLIENT = ci > 0 ? process.argv[ci + 1] : 'bali';
const posArg = process.argv.slice(2).find((a, i, all) => !a.startsWith('--') && all[i - 1] !== '--client');
const file = resolve(posArg || join(HERE, 'out', CLIENT, 'dashboard.json'));
const feed = JSON.parse(readFileSync(file, 'utf8')), snap = JSON.parse(readFileSync(join(SRC, 'feed-bali.json'), 'utf8'));
const errs = [];
const type = v => v === null ? 'null' : Array.isArray(v) ? 'array' : typeof v;

// 0. other clients: structural checks (the Bali snapshot is not their schema)
if (CLIENT !== 'bali') {
  const CF = JSON.parse(readFileSync(join(HERE, 'clients', `${CLIENT}.json`), 'utf8'));
  const need = ['months', 'wa', 'gsc', 'reports', 'meta', 'source_note', ...(CF.ergebnisse ? ['ergebnisse'] : []), ...(CF.citations ? ['citations'] : [])];
  for (const k of need) if (!(k in feed)) errs.push(`${k}: key missing`);
  for (const k of Object.keys(snap)) if (!['nhc', 'beauty', 'beautyMap'].includes(k) && !(k in feed)) errs.push(`${k}: key of the common schema is missing (null is allowed)`);   // nhc/beauty/beautyMap are Bali profile keys
  if (feed.months?.length !== 7) errs.push('months must hold 7 labels');
  if (CF.ergebnisse) {
    const E = feed.ergebnisse || {};
    if ((E.metrics || []).length !== 4) errs.push('ergebnisse.metrics must hold 4 metrics');
    for (const m of E.metrics || []) if (typeof m.before !== 'number' || typeof m.after !== 'number') errs.push(`ergebnisse.${m.key}: before/after must be numbers`);
    if (!E.windows?.before || !E.windows?.after) errs.push('ergebnisse.windows missing');
  }
  if (!CF.local_falcon && (feed.map || feed.ai || feed.main || feed.rev)) errs.push('map/ai/main/rev must be null for a client without Local Falcon data');
  if (feed.meta?.refresh?.status !== 'ok') errs.push('meta.refresh.status is not ok: ' + (feed.meta?.refresh?.failed || []).join(', '));
  if (/local ?falcon|brightlocal|moz|localfalcon|falcon|scan/i.test(JSON.stringify(feed, (k, v) => (k === 'refresh' ? undefined : v)))) errs.push('a tool name or scan wording is in the feed');
  if (JSON.stringify(feed).includes('falcon_')) errs.push('an internal outcome (falcon_*) is in the feed');
  console.log(errs.length ? `STRUCTURE: ${errs.length} problem(s)\n  - ${errs.join('\n  - ')}` : `STRUCTURE: ok (${CLIENT})`);
}

// 1. schema (Bali only: the other clients have their own structure checks above)
if (CLIENT === 'bali') {
const NULLABLE_OK = /^(beauty\.(calls|web|dir)\[\d\]|nhc\.(calls|web|dir)\[\d\]|wa\[\d\]|ai\[\d+\]\[[123]\])$/;   // gaps are allowed here: null means "no data"
function cmp(a, b, p) {
  if (b === null || a === null) { if (a !== b && !(NULLABLE_OK.test(p))) errs.push(`${p}: type ${type(a)} -> ${type(b)}`); return; }
  if (type(a) !== type(b)) { errs.push(`${p}: type ${type(a)} -> ${type(b)}`); return; }
  if (Array.isArray(a)) {
    const fixed = /^(months|nhc\.(calls|web|dir)|beauty\.(calls|web|dir)|wa)$/.test(p);
    if (fixed && a.length !== b.length) errs.push(`${p}: length ${a.length} -> ${b.length}`);
    if (/^rev\.nhc\.(months|per)$/.test(p) && b.length < 1) errs.push(`${p}: empty`);
    const n = Math.min(a.length, b.length, 3); for (let i = 0; i < n; i++) cmp(a[i], b[i], `${p}[${i}]`);
    return;
  }
  if (type(a) === 'object') {
    for (const k of Object.keys(a)) { if (!(k in b)) errs.push(`${p ? p + '.' : ''}${k}: key missing`); else cmp(a[k], b[k], p ? `${p}.${k}` : k); }
  }
}
cmp(snap, feed, '');
const rows = (name, f) => (feed[name] || []).forEach((r, i) => { if (!f(r)) errs.push(`${name}[${i}] has a wrong shape: ${JSON.stringify(r)}`); });
rows('map', r => r.length === 3 && typeof r[0] === 'string' && Number.isInteger(r[1]) && r[1] >= 0 && r[1] <= 49 && typeof r[2] === 'string');
rows('ai', r => r.length === 4 && typeof r[0] === 'string' && r.slice(1).every(x => x === null || (typeof x === 'number' && x >= 0 && x <= 100)));
if (!(feed.beautyMap || []).every(x => typeof x === 'string')) errs.push('beautyMap must hold strings');
if (feed.months.length !== 7) errs.push('months must hold 7 labels');
if (feed.rev.nhc.months.length !== feed.rev.nhc.per.length) errs.push('rev.nhc.months and per differ in length');
const bad = JSON.stringify(feed, (k, v) => (typeof v === 'number' && !Number.isFinite(v)) ? '__BAD__' : v).includes('__BAD__');
if (bad) errs.push('a number is NaN or Infinity');
if (!/^\d{4}-\d{2}-\d{2}$/.test(feed.meta.as_of)) errs.push('meta.as_of is not a date');
if (/local ?falcon|brightlocal|moz|localfalcon/i.test(JSON.stringify(feed))) errs.push('a tool name is in the feed (client-facing file)');
console.log(errs.length ? `SCHEMA: ${errs.length} problem(s)\n  - ${errs.join('\n  - ')}` : 'SCHEMA: ok (same keys and types as the 13 Oct snapshot)');
}

// 2. render check = smoke.js on the new file
const tmp = join(HERE, 'out/.smoke'); mkdirSync(tmp, { recursive: true });
const smokeFile = existsSync(join(SRC, 'smoke.cjs')) ? 'smoke.cjs' : 'smoke.js';
let code = readFileSync(join(SRC, smokeFile), 'utf8')
  .replace("'src/dsh.js'", JSON.stringify(join(SRC, 'dsh.js'))).replace("'src/feed-bali.json'", JSON.stringify(file))
  .replace("'/tmp/smoke-run.js'", JSON.stringify(join(tmp, 'run.cjs')));
writeFileSync(join(tmp, 'gen.cjs'), code);
let render = '';
try { execFileSync('node', [join(tmp, 'gen.cjs')], { stdio: 'pipe' }); render = execFileSync('node', [join(tmp, 'run.cjs')], { encoding: 'utf8' }); }
catch (e) { render = (e.stdout || '') + (e.stderr || '') + '\nRENDER CRASH'; }
const ok = /done bad= 0/.test(render) && !/RENDER CRASH/.test(render);
console.log('RENDER: ' + render.trim().split('\n').join('\n        '));
if (!ok) errs.push('render check failed');
console.log(errs.length ? '\nCHECK FAILED' : '\nCHECK PASSED');
process.exit(errs.length ? 1 : 0);
