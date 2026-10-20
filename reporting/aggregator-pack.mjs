#!/usr/bin/env node
/**
 * Layer-1-Aggregator-Submission-Pack — Generator.
 *
 * Liest die kanonische NAP eines Kunden aus client_locations (Supabase, Admin-JWT)
 * und baut einen fertigen Einreichungs-Pack (Markdown) für die kostenlosen
 * Layer-1-Ziele: Bing Places, Apple Business Connect, Foursquare, TomTom, HERE, Facebook.
 *
 * Diese Ziele haben KEINE Auto-Submit-API — sie sind Portal-Flows mit Konto +
 * Verifizierung. Der Pack liefert pro Ziel: URL, Methode, Aufwand und die exakt
 * einzutragenden Felder. Ein Mensch klickt sich durch. Wiederverwendbar je Kunde.
 *
 *   node reporting/aggregator-pack.mjs --client <id>
 *
 * Auth: .secrets/standup.env (741-Admin-Login).
 */
import { readFileSync } from 'node:fs';

const ROOT = new URL('../', import.meta.url);
const SB = Object.fromEntries(
  readFileSync(new URL('.secrets/standup.env', ROOT), 'utf8')
    .split('\n').filter(Boolean).filter(l => !l.trimStart().startsWith('#'))
    .map(l => { const i = l.indexOf('='); return [l.slice(0, i).trim(), l.slice(i + 1).trim()]; }));

const args = process.argv.slice(2);
const CLIENT = args.includes('--client') ? args[args.indexOf('--client') + 1] : null;
if (!CLIENT) { console.error('Nutzung: --client <id>'); process.exit(1); }

const r = await fetch(`${SB.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
  method: 'POST', headers: { apikey: SB.SUPABASE_ANON, 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: SB.STANDUP_EMAIL, password: SB.STANDUP_PASSWORD }) });
const token = (await r.json()).access_token;
if (!token) { console.error('Login fehlgeschlagen'); process.exit(1); }
const loc = (await (await fetch(
  `${SB.SUPABASE_URL}/rest/v1/client_locations?client_id=eq.${CLIENT}&select=*`,
  { headers: { apikey: SB.SUPABASE_ANON, Authorization: 'Bearer ' + token } })).json())[0];
if (!loc) { console.error('Kein client_locations-Eintrag'); process.exit(1); }

const hours = loc.hours ? Object.entries(loc.hours).filter(([k]) => k !== 'hinweis')
  .map(([d, v]) => `${d} ${v}`).join(', ') + (loc.hours.hinweis ? ` (${loc.hours.hinweis})` : '') : '—';

const TARGETS = [
  { n: 'Bing Places', url: 'https://www.bingplaces.com', effort: '~2 Min',
    method: 'Import direkt aus Google Business Profile (Button „Import from Google"). Bestes Preis-Leistungs-Verhältnis.',
    cat: 'Health & Medical → Alternative Medicine / Naturopath',
    note: 'Braucht Microsoft-Konto + GBP-Verknüpfung. Verifizierung meist über GBP-Import automatisch.' },
  { n: 'Apple Business Connect', url: 'https://businessconnect.apple.com', effort: '~10 Min + Verifizierung',
    method: 'Business anlegen/claimen. Speist Apple Maps + Siri. Hoher Wert.',
    cat: 'Medical / Health → Alternative or Complementary Medicine',
    note: 'Braucht Apple-ID. Verifizierung per Telefon/Dokument.' },
  { n: 'Foursquare', url: 'https://foursquare.com/venue/claim', effort: '~10 Min',
    method: 'Listing suchen + claimen (kostenlos). Speist Apple Maps, ChatGPT/KI-Antworten.',
    cat: 'Health & Medicine → Alternative / Holistic Health (o. Acupuncture Clinic)',
    note: 'Kostenlos. Optional $20 einmalig für Management-Tools — für uns nicht nötig.' },
  { n: 'TomTom', url: 'https://www.tomtom.com/mapshare/tools/', effort: '~10 Min (oder automatisch via GBP)',
    method: 'MapShare → „Single company" → Firmendaten eintragen. TomTom zieht Firmendaten inzwischen auch aus Google Maps → sauberes GBP propagiert evtl. schon.',
    cat: 'Health Care / Practitioner',
    note: 'Konto nötig. Niedrige Priorität, wenn GBP sauber ist.' },
  { n: 'HERE', url: 'https://mapcreator.here.com', effort: 'schwach — beste DIY-Route fehlt',
    method: 'Kein sauberer Einzel-Business-Flow. Über WeGo-App „Suggest an edit" oder Map Creator (wird abgebaut). HERE zieht sonst von Partnern.',
    cat: 'Health / Medical',
    note: 'Geringster DIY-Wert. Das war der Teil, den BrightLocals $60 wirklich abdeckte. Für eine DE-Praxis vernachlässigbar vs. Bing/Apple.' },
  { n: 'Facebook Page', url: 'https://www.facebook.com/pages/create', effort: '~15 Min',
    method: 'Unternehmensseite anlegen (Social + Karten-Signal).',
    cat: 'Medical & Health → Alternative & Holistic Health Service',
    note: 'Manuell. Separat vom Karten-Layer, aber NAP-Signal.' },
];

const L = [];
L.push(`# Layer-1-Aggregator-Pack — ${loc.business_name}`);
L.push(`\nErzeugt aus client_locations. Diese Ziele sind kostenlos und werden von uns selbst gepflegt.`);
L.push(`Kein Auto-Submit möglich — Portal-Flow mit Konto + Verifizierung. Reihenfolge = Wert/Aufwand.`);
L.push(`\n## Einzutragende Daten (überall identisch — NAP-Konsistenz!)`);
L.push('```');
L.push(`Name:      ${loc.business_name}`);
L.push(`Straße:    ${loc.street}`);
L.push(`PLZ/Ort:   ${loc.postal_code} ${loc.city}`);
L.push(`Land:      ${loc.country === 'DE' ? 'Deutschland' : loc.country}`);
L.push(`Telefon:   ${loc.phone}`);
L.push(`Website:   ${loc.website}`);
L.push(`E-Mail:    ${loc.email || '—'}`);
L.push(`Kategorie: ${loc.primary_category} (pro Portal die nächste Entsprechung wählen)`);
L.push(`Öffnungszeiten: ${hours}`);
L.push('```');
if (loc.description) { L.push(`\n**Beschreibung (wo möglich):**\n> ${loc.description}`); }
L.push(`\n## Ziele\n`);
for (const t of TARGETS) {
  L.push(`### ${t.n}  ·  ${t.effort}`);
  L.push(`- URL: ${t.url}`);
  L.push(`- Vorgehen: ${t.method}`);
  L.push(`- Kategorie: ${t.cat}`);
  L.push(`- Hinweis: ${t.note}`);
  L.push(`- Status: ☐ offen  ☐ eingereicht  ☐ live\n`);
}
L.push(`## Reihenfolge-Empfehlung`);
L.push(`1. **Bing Places** (GBP-Import, schnellster Gewinn)`);
L.push(`2. **Apple Business Connect** (Apple Maps + Siri)`);
L.push(`3. **Foursquare** (Apple + KI-Antworten)`);
L.push(`4. **TomTom** (evtl. schon via GBP)`);
L.push(`5. **Facebook Page**`);
L.push(`6. **HERE** (nur wenn Zeit — geringer Wert)`);
console.log(L.join('\n'));
