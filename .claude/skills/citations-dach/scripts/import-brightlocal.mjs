#!/usr/bin/env node
/**
 * BrightLocal-Citation-Report -> client_citations Import.
 *
 * BrightLocal liefert den Citation-Builder-Fortschritt als CSV-Export.
 * Dieses Skript matcht jede CSV-Zeile per Verzeichnisname gegen directories,
 * mappt den BrightLocal-Status auf unser Enum und schreibt client_citations.
 *
 *   node reporting/import-brightlocal.mjs --client <id> --file report.csv         # Dry-Run
 *   node reporting/import-brightlocal.mjs --client <id> --file report.csv --write  # schreiben
 *
 * Auth: .secrets/standup.env (741-Admin-Login; Admin-RLS = Lesen+Schreiben, kein service_role).
 *
 * Status-Mapping (BrightLocal -> unser Enum client_citations.status):
 *   live / listed / found / active            -> live
 *   submitted / in progress / pending / queued -> submitted
 *   inconsistent / needs update / mismatch     -> inconsistent
 *   not found / missing / n/a                   -> missing
 *   (sonst)                                     -> submitted
 */
import { readFileSync } from 'node:fs';

const ROOT = new URL('../', import.meta.url);
const SB = Object.fromEntries(
  readFileSync(new URL('.secrets/standup.env', ROOT), 'utf8')
    .split('\n').filter(Boolean).filter(l => !l.trimStart().startsWith('#'))
    .map(l => { const i = l.indexOf('='); return [l.slice(0, i).trim(), l.slice(i + 1).trim()]; }));

const args = process.argv.slice(2);
const opt = (k) => args.includes(k) ? args[args.indexOf(k) + 1] : null;
const CLIENT = opt('--client');
const FILE = opt('--file');
const WRITE = args.includes('--write');
if (!CLIENT || !FILE) { console.error('Nutzung: --client <id> --file <csv> [--write]'); process.exit(1); }

const norm = s => (s || '').toLowerCase().replace(/gmbh|e\.?k\.?|deutschland|\.de|\.com|\.at|\.ch/g, '')
  .replace(/[^a-z0-9]/g, '').trim();

function mapStatus(s) {
  const t = (s || '').toLowerCase();
  // Reihenfolge wichtig: „not found" enthält „found" -> negative Fälle zuerst prüfen.
  if (/(not found|missing|n\/a|unavailable|failed|rejected)/.test(t)) return 'missing';
  if (/(inconsist|mismatch|needs update|update required)/.test(t)) return 'inconsistent';
  if (/(live|listed|active|complete)/.test(t)) return 'live';
  return 'submitted';
}

// --- CSV-Parser (Komma, Quotes) ---
function parseCsv(text) {
  const rows = []; let row = [], cell = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (q) {
      if (ch === '"' && text[i + 1] === '"') { cell += '"'; i++; }
      else if (ch === '"') q = false;
      else cell += ch;
    } else if (ch === '"') q = true;
    else if (ch === ',') { row.push(cell); cell = ''; }
    else if (ch === '\n') { row.push(cell); rows.push(row); row = []; cell = ''; }
    else if (ch === '\r') { /* skip */ }
    else cell += ch;
  }
  if (cell.length || row.length) { row.push(cell); rows.push(row); }
  return rows.filter(r => r.some(c => c.trim()));
}

async function sbLogin() {
  const r = await fetch(`${SB.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
    method: 'POST', headers: { apikey: SB.SUPABASE_ANON, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: SB.STANDUP_EMAIL, password: SB.STANDUP_PASSWORD }) });
  const j = await r.json();
  if (!j.access_token) throw new Error('Login: ' + JSON.stringify(j));
  return j.access_token;
}

const token = await sbLogin();
const base = SB.SUPABASE_URL + '/rest/v1/';
const H = { apikey: SB.SUPABASE_ANON, Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' };

const dirs = await (await fetch(base + 'directories?select=id,name', { headers: H })).json();
const dirByNorm = new Map(dirs.map(d => [norm(d.name), d]));
const existing = await (await fetch(base + `client_citations?client_id=eq.${CLIENT}&select=directory_id`, { headers: H })).json();
const have = new Set(existing.map(e => e.directory_id));

const rows = parseCsv(readFileSync(FILE, 'utf8'));
const header = rows[0].map(h => h.trim().toLowerCase());
const col = (...names) => { for (const n of names) { const i = header.findIndex(h => h.includes(n)); if (i >= 0) return i; } return -1; };
const ci = { name: col('site', 'directory', 'citation', 'name'), status: col('status', 'result'), url: col('url', 'link', 'listing') };
if (ci.name < 0) { console.error('Keine Verzeichnisspalte gefunden. Header:', header); process.exit(1); }
console.log(`Spalten: name=${header[ci.name]}  status=${header[ci.status] || '—'}  url=${header[ci.url] || '—'}`);

let matched = 0, unmatched = [];
for (const r of rows.slice(1)) {
  const rawName = (r[ci.name] || '').trim();
  if (!rawName) continue;
  const dir = dirByNorm.get(norm(rawName));
  if (!dir) { unmatched.push(rawName); continue; }
  const status = mapStatus(ci.status >= 0 ? r[ci.status] : '');
  const url = ci.url >= 0 ? (r[ci.url] || '').trim() : '';
  matched++;
  console.log(`  ${status.padEnd(12)} ${rawName}  ->  ${dir.name}${url ? '  ' + url : ''}`);
  if (WRITE) {
    const body = { status, submitted_via: 'brightlocal', last_checked: new Date().toISOString() };
    if (url) body.listing_url = url;
    let code;
    if (have.has(dir.id)) {
      const res = await fetch(base + `client_citations?client_id=eq.${CLIENT}&directory_id=eq.${dir.id}`,
        { method: 'PATCH', headers: { ...H, Prefer: 'return=minimal' }, body: JSON.stringify(body) });
      code = res.status;
    } else {
      const res = await fetch(base + 'client_citations',
        { method: 'POST', headers: { ...H, Prefer: 'return=minimal' }, body: JSON.stringify({ client_id: CLIENT, directory_id: dir.id, ...body }) });
      code = res.status;
    }
    console.log(`     -> HTTP ${code}`);
  }
}
console.log(`\n${matched} gematcht, ${unmatched.length} ohne Verzeichnis-Match.`);
if (unmatched.length) console.log('Ohne Match (ggf. neu in directories anlegen):\n  - ' + unmatched.join('\n  - '));
if (!WRITE) console.log('\nDry-Run. Mit --write schreiben.');
