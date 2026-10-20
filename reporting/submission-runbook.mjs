#!/usr/bin/env node
/**
 * Einreichungs-Runbook-Generator (Self-Submit-Verzeichnisse).
 *
 * Liest die kanonische NAP + alle noch „planned" Citations eines Kunden und baut
 * ein abarbeitbares Runbook: pro Verzeichnis URL, Gruppe (741 macht / Kunde nötig /
 * Eignung prüfen), vorbefüllte Daten, Schritte, Status-Häkchen. Inkl. Loop-Signal-
 * Pflichtfeldern (siehe loop-signals-playbook).
 *
 *   node reporting/submission-runbook.mjs --client <id>
 *
 * Auth: .secrets/standup.env (741-Admin-Login).
 */
import { readFileSync } from 'node:fs';

const ROOT = new URL('../', import.meta.url);
const SB = Object.fromEntries(readFileSync(new URL('.secrets/standup.env', ROOT), 'utf8')
  .split('\n').filter(Boolean).filter(l => !l.trimStart().startsWith('#'))
  .map(l => { const i = l.indexOf('='); return [l.slice(0, i).trim(), l.slice(i + 1).trim()]; }));
const CLIENT = process.argv.includes('--client') ? process.argv[process.argv.indexOf('--client') + 1] : null;
if (!CLIENT) { console.error('Nutzung: --client <id>'); process.exit(1); }

const tok = (await (await fetch(`${SB.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
  method: 'POST', headers: { apikey: SB.SUPABASE_ANON, 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: SB.STANDUP_EMAIL, password: SB.STANDUP_PASSWORD }) })).json()).access_token;
const H = { apikey: SB.SUPABASE_ANON, Authorization: 'Bearer ' + tok };
const get = p => fetch(SB.SUPABASE_URL + '/rest/v1/' + p, { headers: H }).then(r => r.json());

const loc = (await get(`client_locations?client_id=eq.${CLIENT}&select=*`))[0];
const cits = await get(`client_citations?client_id=eq.${CLIENT}&status=eq.planned&select=directory:directories(name,homepage,submit_url,category,method,tier,guide)&order=directory(tier)`);
const acct = (await get(`client_directory_accounts?client_id=eq.${CLIENT}&directory_name=eq.${encodeURIComponent('(Listings-Identität)')}&select=login_email`))[0];
const listingsEmail = acct?.login_email || `${(loc.business_name || 'kunde').toLowerCase().split(/\s+/)[0].replace(/[^a-z0-9]/g, '')}@listings.741.studio`;

const GROUP_B = new Set(['Apple Business Connect', 'Bing Places', 'Facebook / Meta Page', 'Instagram Business', 'LinkedIn Company', 'XING']);
const ELIG = new Set(['jameda', 'Doctolib']);
const classify = (n) => GROUP_B.has(n) ? 'B' : (ELIG.has(n) ? 'E' : 'A');

const rows = cits.map(c => c.directory).filter(Boolean);
const groups = { A: [], B: [], E: [] };
for (const d of rows) groups[classify(d.name)].push(d);

const L = [];
L.push(`# Einreichungs-Runbook — ${loc.business_name}`);
L.push(`\nSelf-Submit-Verzeichnisse (nicht BrightLocal). Abarbeiten in Reihenfolge A → E.`);
L.push(`Listings-Login-Mail: **${listingsEmail}** (alle Bestätigungen laufen automatisch in \`listing_emails\`).`);

L.push(`\n## Immer eintragen (NAP-Konsistenz — überall identisch)`);
L.push('```');
L.push(`Name:      ${loc.business_name}`);
L.push(`Straße:    ${loc.street}`);
L.push(`PLZ/Ort:   ${loc.postal_code} ${loc.city}`);
L.push(`Land:      ${loc.country === 'DE' ? 'Deutschland' : loc.country}`);
L.push(`Telefon:   ${loc.phone}`);
L.push(`Website:   ${loc.website}`);
L.push(`Login-Mail:${listingsEmail}`);
L.push(`Kategorie: ${loc.primary_category}`);
L.push('```');

L.push(`\n## Loop-Signal-Pflicht bei JEDEM Bild-Upload (siehe loop-signals-playbook)`);
L.push(`- Dateiname: \`leistung-stadtteil-brandname.jpg\` (z. B. \`akupunktur-ingelheim-${(loc.business_name||'').toLowerCase().split(/\s+/)[0]}.jpg\`)`);
L.push(`- EXIF-Geotag der Praxis-Koordinaten vor Upload einbetten`);
L.push(`- Caption verweist auf ein ANDERES verifiziertes Profil (Co-Citation-Wheel)`);
L.push(`- echte Vor-Ort-Fotos, keine Stockbilder`);

const genericSteps = (d) => [
  `Konto mit ${listingsEmail} anlegen`,
  `NAP exakt wie oben eintragen (Kategorie „${loc.primary_category}")`,
  `Bestätigungs-Link kommt automatisch in listing_emails → klicken`,
];
const render = (d) => {
  const url = d.submit_url || d.homepage || '';
  const steps = (d.guide && d.guide.steps && (d.guide.steps.de || d.guide.steps)) || genericSteps(d);
  const arr = Array.isArray(steps) ? steps : genericSteps(d);
  L.push(`\n### ${d.name}`);
  if (url) L.push(`- URL: ${url}`);
  L.push(`- Kategorie-Bereich: ${d.category}`);
  arr.forEach((s, i) => L.push(`- Schritt ${i + 1}: ${s}`));
  L.push(`- Status: ☐ offen  ☐ eingereicht  ☐ live`);
};

L.push(`\n---\n## Gruppe A — 741 macht selbst (${groups.A.length}) · nur E-Mail-Bestätigung`);
groups.A.forEach(render);
L.push(`\n---\n## Gruppe B — nur der Kunde (${groups.B.length}) · eigenes Konto/Verifizierung nötig`);
L.push(`> Diese gehen NUR mit Coralies eigenen Accounts (Apple-ID, Microsoft, Facebook, persönliches Profil). Per Kunden-Mail anstoßen (client-listing-email-template).`);
groups.B.forEach(render);
L.push(`\n---\n## Gruppe E — Eignung prüfen (${groups.E.length})`);
L.push(`> Health-Plattformen mit Zulassungsprüfung. Erst klären, ob Heilpraktiker gelistet werden darf.`);
groups.E.forEach(render);

console.log(L.join('\n'));
