#!/usr/bin/env node
/**
 * Citation-/NAP-Monitor via DataForSEO — Produktiv-Version.
 *
 * Liest die kanonische NAP je Kunden-Standort aus Supabase (client_locations),
 * zieht das Google-Listing (Maps live) via DataForSEO, gleicht NAP ab, misst
 * den lokalen Map-Pack-Rank und schreibt den Status in client_citations
 * (nur die Google-Business-Profile-Zeile).
 *
 *   node reporting/citation-monitor.mjs                 # alle Kunden mit Standort, nur Report
 *   node reporting/citation-monitor.mjs --client <id>   # nur ein Kunde (client_id)
 *   node reporting/citation-monitor.mjs --write         # Ergebnis in client_citations schreiben
 *
 * Auth:
 *   .secrets/dataforseo.env  -> DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD
 *   .secrets/standup.env     -> SUPABASE_URL / SUPABASE_ANON / STANDUP_EMAIL / STANDUP_PASSWORD
 *                               (STANDUP_* = 741-Admin-Login; Admin-RLS erlaubt Lesen+Schreiben,
 *                                daher KEIN service_role-Key nötig.)
 *
 * ⚠ DataForSEO-IP-Whitelist: der Job muss von einer festen, gewhitelisteten IP laufen
 *   (Dev-VPS), nicht vom Laptop/GitHub-Actions. Sonst 40207 „IP not whitelisted".
 */
import { readFileSync } from 'node:fs';

const ROOT = new URL('../', import.meta.url);
const readEnv = (name) => Object.fromEntries(
  readFileSync(new URL('.secrets/' + name, ROOT), 'utf8')
    .split('\n').filter(Boolean).filter(l => !l.trimStart().startsWith('#'))
    .map(l => { const i = l.indexOf('='); return [l.slice(0, i).trim(), l.slice(i + 1).trim()]; })
);
const DFS = readEnv('dataforseo.env');
const SB = readEnv('standup.env');

const AUTH = 'Basic ' + Buffer.from(`${DFS.DATAFORSEO_LOGIN}:${DFS.DATAFORSEO_PASSWORD}`).toString('base64');
const LOC = { DE: 2276, AT: 2040, CH: 2756 };

const args = process.argv.slice(2);
const WRITE = args.includes('--write');
const CLIENT = args.includes('--client') ? args[args.indexOf('--client') + 1] : null;

// ---- Supabase (Admin-JWT über 741-Admin-Login) ----
async function sbLogin() {
  const r = await fetch(`${SB.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
    method: 'POST', headers: { apikey: SB.SUPABASE_ANON, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: SB.STANDUP_EMAIL, password: SB.STANDUP_PASSWORD }),
  });
  const j = await r.json();
  if (!j.access_token) throw new Error('Supabase-Login fehlgeschlagen: ' + (j.error_description || j.msg || JSON.stringify(j)));
  return j.access_token;
}
function sb(token) {
  const base = SB.SUPABASE_URL + '/rest/v1/';
  const H = { apikey: SB.SUPABASE_ANON, Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' };
  return {
    get: async (path) => { const r = await fetch(base + path, { headers: H }); return r.json(); },
    patch: async (path, body) => {
      const r = await fetch(base + path, { method: 'PATCH', headers: { ...H, Prefer: 'return=minimal' }, body: JSON.stringify(body) });
      return r.status;
    },
  };
}

// ---- DataForSEO ----
async function dfs(path, body) {
  const r = await fetch('https://api.dataforseo.com/v3/' + path, {
    method: 'POST', headers: { Authorization: AUTH, 'Content-Type': 'application/json' },
    body: JSON.stringify([body]),
  });
  const j = await r.json();
  const t = (j.tasks || [{}])[0];
  if (t.status_code !== 20000) throw new Error(`DFS ${path}: ${t.status_message}`);
  return (t.result || [{}])[0];
}

const norm = s => (s || '').toLowerCase().replace(/[.,\-\/]/g, ' ').replace(/\s+/g, ' ').trim();
const digits = s => (s || '').replace(/\D/g, '').replace(/^49/, '').replace(/^0/, '');

async function monitor(c) {
  const loc = LOC[c.country] || LOC.DE;
  const rankKw = `${c.primary_category} ${(c.city || '').split(' ')[0]}`.toLowerCase().trim();
  console.log(`\n════ ${c.business_name} (${c.city}) ════`);
  const card = await dfs('serp/google/maps/live/advanced',
    { keyword: `${c.business_name} ${c.city}`, location_code: loc, language_code: 'de' });
  const g = (card.items || [])[0] || {};
  const checks = {
    name: norm(g.title || '').includes(norm(c.business_name)),
    strasse: norm(g.address || '').includes(norm(c.street)),
    plz: (g.address_info?.zip || g.address || '').includes(c.postal_code),
    ort: norm(g.address || '').includes(norm((c.city || '').split(' ')[0])),
    telefon: digits(g.phone) === digits(c.phone),
  };
  const ok = Object.values(checks).filter(Boolean).length;
  const consistent = ok === 5;
  console.log(`  Google-Listing: ${g.title || '—'}`);
  console.log(`  Adresse: ${g.address || '—'}   Tel: ${g.phone || '—'}`);
  console.log(`  Kategorie (Google): ${g.category || '—'}   Rating: ${(g.rating || {}).value ?? '—'} (${(g.rating || {}).votes_count ?? '—'})`);
  console.log(`  Öffnungszeiten hinterlegt: ${g.work_hours?.timetable ? 'JA' : 'NEIN'}`);
  console.log(`  NAP-Abgleich: ${ok}/5  ${Object.entries(checks).map(([k, v]) => `${v ? '✓' : '✗'}${k}`).join(' ')}`);
  console.log(`  Kategorie stimmt: ${norm(g.category) === norm(c.primary_category) ? '✓' : `✗ (Ist „${g.category}" / Soll „${c.primary_category}")`}`);
  const pack = await dfs('serp/google/maps/live/advanced',
    { keyword: rankKw, location_code: loc, language_code: 'de' });
  const items = pack.items || [];
  const mine = items.find(i => norm(i.title).includes(norm(c.business_name)));
  console.log(`  Map-Pack-Rank „${rankKw}": ${mine ? '#' + mine.rank_absolute : 'nicht in Top-' + items.length}`);
  return {
    client_id: c.client_id, listing: g.title, listing_url: g.url || null,
    nap_score: `${ok}/5`, consistent, checks,
    hours_set: !!g.work_hours?.timetable, category_ok: norm(g.category) === norm(c.primary_category),
    rating: (g.rating || {}).value, reviews: (g.rating || {}).votes_count,
    rank: mine ? mine.rank_absolute : null,
    status: consistent ? 'live' : 'inconsistent',
  };
}

// ---- Lauf ----
const token = await sbLogin();
const db = sb(token);

let filter = 'client_locations?select=client_id,business_name,legal_name,street,postal_code,city,country,phone,email,website,primary_category';
if (CLIENT) filter += `&client_id=eq.${CLIENT}`;
const locations = await db.get(filter);
if (!Array.isArray(locations)) throw new Error('client_locations lesen fehlgeschlagen: ' + JSON.stringify(locations));

// Directory-ID der GBP-Zeile (einmalig)
const gbpRow = (await db.get(`directories?name=eq.Google%20Business%20Profile&select=id`))[0];
const GBP_ID = gbpRow?.id;

const out = [];
for (const c of locations) {
  try {
    const res = await monitor(c);
    out.push(res);
    if (WRITE && GBP_ID) {
      const notes = `NAP ${res.nap_score}; Rating ${res.rating ?? '—'}/${res.reviews ?? '—'}; Rank ${res.rank ? '#' + res.rank : '—'}; Öffnungszeiten ${res.hours_set ? 'ja' : 'nein'}`;
      const code = await db.patch(
        `client_citations?client_id=eq.${c.client_id}&directory_id=eq.${GBP_ID}`,
        { status: res.status, nap_match: res.consistent, listing_url: res.listing_url, last_checked: new Date().toISOString(), notes });
      console.log(`  → client_citations (GBP) geschrieben: HTTP ${code}`);
    }
  } catch (e) { console.error('  ❌', e.message); }
}
console.log('\n── JSON ──');
console.log(JSON.stringify(out, null, 2));
