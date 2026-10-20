#!/usr/bin/env node
/**
 * 741 Studio — Google Search Console Performance Ingestion Worker
 * Ingests daily Search Console metrics (clicks, impressions, CTR, position)
 * from existing client feed datasets into Supabase public.gsc_daily_performance.
 *
 * Usage:
 *   node scripts/import-gsc-performance.mjs --dry-run
 *   node scripts/import-gsc-performance.mjs --apply
 */

import { readFileSync, existsSync } from 'node:fs';
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
  'huewel': { id: 'f0a6730f-8f56-4c61-8085-1955f3bb285a', name: 'Praxis Hüwel' },
  'stuerzl': { id: 'b6f6e303-50e4-4afb-a343-337206cec316', name: 'STÜRZL Steuerstrafrecht' },
  'bali': { id: 'd0519d13-0bfc-4dfb-b512-57bf550387e6', name: 'Bali Healing' },
  'dumann': { id: 'd01f4236-8674-45fe-a347-0751fa7b24de', name: 'Daniela Dumann' },
  'johni': { id: 'b84427b9-57bc-4145-83fc-ec284d2de785', name: 'Johni Jaya Motor' },
  'rabenmuetter': { id: 'fbcc70d1-4c56-437c-b5fb-8056e48d3f62', name: 'Rabenmütter Shop' },
  'suriya': { id: '3f71ef33-8c74-4ea1-b2d3-0273c2e99649', name: 'Praxis Suriya' }
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

function collectDailyPerformance() {
  const records = [];

  // 1. Process feed datasets (6 clients with 195+ days of daily time series)
  const feedBase = join(ROOT, '00_project/client-dashboard-redesign/portal/feed/data');

  for (const [key, cfg] of Object.entries(CLIENT_MAP)) {
    const dailyPath = join(feedBase, key, 'gsc-daily.json');
    if (!existsSync(dailyPath)) continue;

    try {
      const data = JSON.parse(readFileSync(dailyPath, 'utf8'));
      const site = data.site || 'https://example.com';
      const days = data.days || [];

      for (const d of days) {
        if (!d.date) continue;
        const clicks = parseInt(d.clicks, 10) || 0;
        const impressions = parseInt(d.impressions, 10) || 0;
        const rawCtr = impressions > 0 ? (clicks / impressions) * 100 : 0;
        const ctr = Number(Math.min(99.9999, rawCtr).toFixed(4));
        const position = parseFloat(d.position) ? Number(parseFloat(d.position).toFixed(2)) : 0;

        records.push({
          client_id: cfg.id,
          date: d.date,
          page: site,
          query: null,
          is_target_keyword: false,
          clicks: clicks,
          impressions: impressions,
          ctr: ctr,
          position: position,
          country: 'deu',
          device: 'all'
        });
      }
    } catch (err) {
      console.warn(`⚠️ Konnte ${dailyPath} nicht parsen:`, err.message);
    }
  }

  // 2. Process Praxis Suriya baseline export
  const suriyaExportPath = join(ROOT, '.claude/worktrees/admiring-nightingale-f0f882/00_project/assets/suriya/baseline/2026-10-01-gsc-export-90d.json');
  if (existsSync(suriyaExportPath)) {
    try {
      const sData = JSON.parse(readFileSync(suriyaExportPath, 'utf8'));
      const site = sData.site || 'https://suriya-praxis.de/';
      // Top target queries
      const queries = (sData.queries || []).slice(0, 25);
      for (const q of queries) {
        const queryText = (q.keys && q.keys[0]) || '';
        if (!queryText) continue;
        records.push({
          client_id: CLIENT_MAP['suriya'].id,
          date: '2026-09-30',
          page: site,
          query: queryText,
          is_target_keyword: true,
          clicks: parseInt(q.clicks, 10) || 0,
          impressions: parseInt(q.impressions, 10) || 0,
          ctr: parseFloat(q.ctr) ? Number(Math.min(99.9999, parseFloat(q.ctr)).toFixed(4)) : 0,
          position: parseFloat(q.position) ? Number(parseFloat(q.position).toFixed(2)) : 0,
          country: 'deu',
          device: 'all'
        });
      }
    } catch (err) {}
  }

  return records;
}

async function main() {
  console.log('=== 741 Search Console Performance Ingestion Worker ===');
  console.log(`Mode: ${DRY_RUN ? 'DRY-RUN (use --apply to write to Supabase)' : 'APPLY (Live DB sync)'}\n`);

  const token = await getAuthToken();
  console.log(`✅ Authentifiziert als: standup-bot@741.studio\n`);

  const records = collectDailyPerformance();
  console.log(`Gefundene GSC-Performance Datensätze: ${records.length}`);

  if (DRY_RUN) {
    console.log('\nBeispieldatensätze (erste 5):');
    records.slice(0, 5).forEach((r, idx) => {
      console.log(` ${idx + 1}. [${r.date}] Clicks: ${r.clicks} | Impr: ${r.impressions} | CTR: ${r.ctr}% | Pos: ${r.position} | Query: ${r.query || '(total rollup)'}`);
    });
    console.log('\n[DRY-RUN abgeschlossen. Führe mit --apply aus, um Daten live zu schreiben]');
    return;
  }

  // Ensure idempotency: delete existing entries for these clients before inserting fresh
  const clientIds = [...new Set(records.map(r => r.client_id))].join(',');
  console.log(`Prüfe und bereinige bestehende Einträge für Clients: ${clientIds}...`);
  await fetch(`${env.SUPABASE_URL}/rest/v1/gsc_daily_performance?client_id=in.(${clientIds})`, {
    method: 'DELETE',
    headers: {
      'apikey': env.SUPABASE_ANON,
      'Authorization': `Bearer ${token}`
    }
  });

  // Batch insert into Supabase
  const chunkSize = 50;
  let inserted = 0;

  for (let i = 0; i < records.length; i += chunkSize) {
    const chunk = records.slice(i, i + chunkSize);
    const res = await fetch(`${env.SUPABASE_URL}/rest/v1/gsc_daily_performance`, {
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
      if (inserted % 200 === 0 || inserted === records.length) {
        console.log(`✅ ${inserted}/${records.length} Zeilen synchronisiert...`);
      }
    }
  }

  console.log(`\n========================================`);
  console.log(`Fertig: ${inserted} von ${records.length} GSC-Tageseinträgen live in Supabase gespeichert.`);
}

main().catch(err => {
  console.error('Fataler Fehler:', err);
  process.exit(1);
});
