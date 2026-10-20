#!/usr/bin/env node
/**
 * 741 Studio — Geo Grid Scans Ingestion Worker
 * Ingests Local Falcon JSON reports and map scan metadata from local assets
 * into Supabase public.geo_grid_scans without spending third-party credits.
 *
 * Usage:
 *   node scripts/import-geo-grids.mjs --dry-run
 *   node scripts/import-geo-grids.mjs --apply
 */

import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { resolve, join } from 'node:path';

const ROOT = process.cwd();
const SECRETS_PATH = join(ROOT, '.secrets', 'standup.env');

if (!existsSync(SECRETS_PATH)) {
  console.error('❌ .secrets/standup.env nicht gefunden');
  process.exit(1);
}

const env = Object.fromEntries(
  readFileSync(SECRETS_PATH, 'utf8')
    .split('\n')
    .filter(Boolean)
    .filter(l => !l.trimStart().startsWith('#'))
    .map(l => {
      const idx = l.indexOf('=');
      return [l.slice(0, idx).trim(), l.slice(idx + 1).trim()];
    })
);

const CLIENT_MAP = {
  'balihealing': 'd0519d13-0bfc-4dfb-b512-57bf550387e6',
  'dumann': 'd01f4236-8674-45fe-a347-0751fa7b24de',
  'maria': '444ac77b-747d-4855-89e5-12ac97d2363c',
  'suriya': '3f71ef33-8c74-4ea1-b2d3-0273c2e99649',
  'huewel': 'f0a6730f-8f56-4c61-8085-1955f3bb285a',
  'stuerzl': 'b6f6e303-50e4-4afb-a343-337206cec316'
};

const args = process.argv.slice(2);
const DRY_RUN = !args.includes('--apply');

async function getAuthToken() {
  const res = await fetch(`${env.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
    method: 'POST',
    headers: { 'apikey': env.SUPABASE_ANON, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: env.STANDUP_EMAIL, password: env.STANDUP_PASSWORD })
  });
  if (!res.ok) throw new Error(`Auth failed: ${res.status} ${await res.text()}`);
  const data = await res.json();
  return data.access_token;
}

function parseDate(str) {
  if (!str) return new Date().toISOString();
  try {
    const d = new Date(str);
    if (!isNaN(d.getTime())) return d.toISOString();
  } catch (e) {}
  return new Date().toISOString();
}

function collectScans() {
  const scans = [];

  // 1. Bali Healing Individual Falcon Reports
  const baliDir = join(ROOT, '00_project/assets/audit/balihealing/2026-10-11-kickoff/evidence');
  if (existsSync(baliDir)) {
    const files = readdirSync(baliDir).filter(f => f.startsWith('falcon-report-') && f.endsWith('.json') && !f.includes('index'));
    for (const f of files) {
      try {
        const raw = JSON.parse(readFileSync(join(baliDir, f), 'utf8'));
        if (raw.report_key && raw.keyword) {
          const gridSize = raw.grid_size ? `${raw.grid_size}x${raw.grid_size}` : '7x7';
          scans.push({
            client_id: CLIENT_MAP['balihealing'],
            keyword: raw.keyword,
            scan_date: parseDate(raw.date),
            grid_size: gridSize,
            radius_km: parseFloat(raw.radius) ? (raw.measurement === 'mi' ? parseFloat(raw.radius) * 1.60934 : parseFloat(raw.radius)) : 5.0,
            center_lat: parseFloat(raw.lat) || null,
            center_lng: parseFloat(raw.lng) || null,
            arp: parseFloat(raw.arp) || 0,
            atrp: parseFloat(raw.atrp) || 0,
            solv: parseFloat(raw.solv) || 0,
            top3_count: parseInt(raw.found_in, 10) || 0,
            points: raw.places ? Object.values(raw.places).slice(0, 10) : [],
            screenshot_url: `https://lf-static-v2.localfalcon.com/image/${raw.report_key}.png`,
            provider: 'local_falcon',
            metadata: {
              report_key: raw.report_key,
              platform: raw.platform || 'google',
              unique_competitors: raw.unique_competitors || 0
            }
          });
        }
      } catch (err) {}
    }
  }

  // 2. Daniela Dumann Historical Scans (from verified memory/logs)
  const dumannScans = [
    { report_key: 'fc58366779fb5da', keyword: 'heilpraktiker charlottenburg', date: '2026-10-01T00:00:00Z', arp: 14.6, atrp: 20.35, solv: 0.0, grid: '7x7', radius: 2.0, lat: 52.5189293, lng: 13.2986296 },
    { report_key: '77db56c6e18d130', keyword: 'ernährungsberatung charlottenburg', date: '2026-10-01T00:00:00Z', arp: 14.0, atrp: 20.86, solv: 0.0, grid: '7x7', radius: 2.0, lat: 52.5189293, lng: 13.2986296 },
    { report_key: 'd6faf9c98d1d772', keyword: 'heilpraktiker charlottenburg', date: '2026-07-22T00:00:00Z', arp: 21.0, atrp: 21.0, solv: 0.0, grid: '7x7', radius: 2.0, lat: 52.5189293, lng: 13.2986296 },
    { report_key: 'b2f660a44ec59b1', keyword: 'ernährungsberatung charlottenburg', date: '2026-08-31T00:00:00Z', arp: 21.0, atrp: 21.0, solv: 0.0, grid: '7x7', radius: 2.0, lat: 52.5189293, lng: 13.2986296 }
  ];

  for (const s of dumannScans) {
    scans.push({
      client_id: CLIENT_MAP['dumann'],
      keyword: s.keyword,
      scan_date: s.date,
      grid_size: s.grid,
      radius_km: s.radius,
      center_lat: s.lat,
      center_lng: s.lng,
      arp: s.arp,
      atrp: s.atrp,
      solv: s.solv,
      top3_count: 0,
      points: [],
      screenshot_url: `https://lf-static-v2.localfalcon.com/image/${s.report_key}.png`,
      provider: 'local_falcon',
      metadata: { report_key: s.report_key, profile: 'Keeper A' }
    });
  }

  // 3. Maria Brasse (Shui Guru)
  scans.push({
    client_id: CLIENT_MAP['maria'],
    keyword: 'feng shui garten',
    scan_date: '2026-10-08T00:00:00Z',
    grid_size: '7x7',
    radius_km: 5.0,
    center_lat: null,
    center_lng: null,
    arp: 0,
    atrp: 0,
    solv: 0,
    top3_count: 0,
    points: [],
    screenshot_url: `https://lf-static-v2.localfalcon.com/image/cb390c619f7c04b.png`,
    provider: 'local_falcon',
    metadata: { report_key: 'cb390c619f7c04b', local_file: '00_project/assets/maria/falcon/garten-2026-10-08-cb390c619f7c04b.png' }
  });

  return scans;
}

async function main() {
  console.log('=== 741 Geo Grid Scans Ingestion Worker ===');
  console.log(`Mode: ${DRY_RUN ? 'DRY-RUN (use --apply to write to Supabase)' : 'APPLY (Live DB sync)'}\n`);

  const token = await getAuthToken();
  console.log(`✅ Authentifiziert als: standup-bot@741.studio\n`);

  const scans = collectScans();
  console.log(`Gefundene Scan-Datensätze: ${scans.length}`);

  if (DRY_RUN) {
    console.log('\nBeispieldatensätze (erste 3):');
    scans.slice(0, 3).forEach((s, idx) => {
      console.log(` ${idx + 1}. [${s.keyword}] ARP: ${s.arp} | SoLV: ${s.solv}% | Grid: ${s.grid_size} | Image: ${s.screenshot_url}`);
    });
    console.log('\n[DRY-RUN abgeschlossen. Führe mit --apply aus, um Daten live zu schreiben]');
    return;
  }

  // Batch insert into Supabase
  const chunkSize = 25;
  let inserted = 0;

  for (let i = 0; i < scans.length; i += chunkSize) {
    const chunk = scans.slice(i, i + chunkSize);
    const res = await fetch(`${env.SUPABASE_URL}/rest/v1/geo_grid_scans`, {
      method: 'POST',
      headers: {
        'apikey': env.SUPABASE_ANON,
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
      },
      body: JSON.stringify(chunk)
    });

    if (!res.ok) {
      console.error(`❌ Fehler beim Einfügen (Chunk ${i}-${i + chunk.length}):`, res.status, await res.text());
    } else {
      inserted += chunk.length;
      console.log(`✅ ${chunk.length} Scans synchronisiert (Fortschritt: ${inserted}/${scans.length})`);
    }
  }

  console.log(`\n========================================`);
  console.log(`Fertig: ${inserted} von ${scans.length} Geo Grid Scans live in Supabase gespeichert.`);
}

main().catch(err => {
  console.error('Fataler Fehler:', err);
  process.exit(1);
});
