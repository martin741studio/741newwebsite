#!/usr/bin/env node
/**
 * 741 Studio — GBP Daily Conversion Actions Ingestion Worker
 * Ingests Google Business Profile daily action metrics (calls, website clicks, directions)
 * into Supabase public.gbp_daily_actions.
 *
 * Usage:
 *   node scripts/import-gbp-actions.mjs --dry-run
 *   node scripts/import-gbp-actions.mjs --client suriya --apply
 *   node scripts/import-gbp-actions.mjs --client all --apply
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
  'suriya': {
    id: '3f71ef33-8c74-4ea1-b2d3-0273c2e99649',
    name: 'Praxis Suriya',
    feedDir: 'suriya',
    filePattern: 'profile-actions-main.json'
  },
  'balihealing': {
    id: 'd0519d13-0bfc-4dfb-b512-57bf550387e6',
    name: 'Bali Healing',
    feedDir: 'bali',
    filePattern: 'profile-actions-nhc.json'
  },
  'dumann': {
    id: 'd01f4236-8674-45fe-a347-0751fa7b24de',
    name: 'Dumann & Kollegen',
    feedDir: 'dumann',
    filePattern: 'profile-actions-main.json'
  },
  'huewel': {
    id: 'f0a6730f-8f56-4c61-8085-1955f3bb285a',
    name: 'Zahnarztpraxis Hüwel',
    feedDir: 'huewel',
    filePattern: 'profile-actions-main.json'
  },
  'stuerzl': {
    id: 'b6f6e303-50e4-4afb-a343-337206cec316',
    name: 'Stürzl Rechtsanwälte',
    feedDir: 'stuerzl',
    filePattern: 'profile-actions-main.json'
  },
  'maria': {
    id: '444ac77b-747d-4855-89e5-12ac97d2363c',
    name: 'Praxis Maria',
    feedDir: 'maria',
    filePattern: 'profile-actions-main.json'
  },
  'kamil': {
    id: 'b3378396-03f4-441d-91b5-ebfbe4fbc267',
    name: 'Kraft & Ausdauer (Kamil)',
    feedDir: 'kamil',
    filePattern: 'profile-actions-main.json'
  }
};

const args = process.argv.slice(2);
const DRY_RUN = !args.includes('--apply');
const clientArg = args.find(a => a.startsWith('--client='))?.split('=')[1] || 
                  (args.includes('--client') ? args[args.indexOf('--client') + 1] : 'suriya');

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

function collectActions(targetKey) {
  const feedBase = join(ROOT, '00_project/client-dashboard-redesign/portal/feed/data');
  const targets = targetKey === 'all' ? Object.keys(CLIENT_MAP) : [targetKey];
  const allRecords = [];

  for (const key of targets) {
    const cfg = CLIENT_MAP[key];
    if (!cfg) {
      console.warn(`⚠️ Unbekannter Client-Schlüssel: ${key}`);
      continue;
    }

    const filePath = join(feedBase, cfg.feedDir, cfg.filePattern);
    if (!existsSync(filePath)) {
      console.warn(`⚠️ Datei nicht gefunden für ${key}: ${filePath}`);
      continue;
    }

    try {
      const data = JSON.parse(readFileSync(filePath, 'utf8'));
      const days = data.days || [];

      for (const d of days) {
        if (!d.date) continue;
        allRecords.push({
          client_id: cfg.id,
          date: d.date,
          call_clicks: parseInt(d.calls, 10) || 0,
          website_clicks: parseInt(d.web, 10) || 0,
          direction_requests: parseInt(d.dir, 10) || 0,
          message_conversations: parseInt(d.msg || d.messages || 0, 10) || 0,
          bookings: parseInt(d.bookings || 0, 10) || 0,
          raw_payload: { source: 'feed', profile: data.profile || 'main' }
        });
      }
      console.log(`📊 ${cfg.name}: ${days.length} Tage Conversion-Actions geladen.`);
    } catch (err) {
      console.error(`❌ Fehler beim Parsen von ${filePath}:`, err.message);
    }
  }

  return allRecords;
}

async function main() {
  console.log('=== 741 GBP Daily Actions Ingestion Worker ===');
  console.log(`Modus: ${DRY_RUN ? 'DRY-RUN (Nutze --apply zum Schreiben)' : 'LIVE-IMPORT (--apply aktiv)'}`);
  console.log(`Ziel-Client: ${clientArg}`);

  const records = collectActions(clientArg);
  console.log(`Gesamtanzahl Datensätze vorbereitet: ${records.length}`);

  if (records.length === 0) {
    console.log('Keine Datensätze zu importieren.');
    return;
  }

  const sample = records.slice(0, 3);
  console.log('\nBeispieldatensätze:');
  sample.forEach((r, i) => {
    console.log(` ${i + 1}. [${r.date}] Calls: ${r.call_clicks} | Web: ${r.website_clicks} | Directions: ${r.direction_requests}`);
  });

  if (DRY_RUN) {
    console.log('\n[DRY-RUN abgeschlossen. Führe mit --apply aus, um Daten live in Supabase zu schreiben]');
    return;
  }

  const token = await getAuthToken();
  console.log('\n✅ Supabase Authentifizierung erfolgreich.');

  // Idempotente Einspielung: Batches von 100
  const BATCH_SIZE = 100;
  let inserted = 0;

  for (let i = 0; i < records.length; i += BATCH_SIZE) {
    const batch = records.slice(i, i + BATCH_SIZE);
    const res = await fetch(`${env.SUPABASE_URL}/rest/v1/gbp_daily_actions`, {
      method: 'POST',
      headers: {
        'apikey': env.SUPABASE_ANON,
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        'Prefer': 'resolution=merge-duplicates'
      },
      body: JSON.stringify(batch)
    });

    if (!res.ok) {
      const errText = await res.text();
      console.error(`❌ Batch-Fehler bei Offset ${i}: ${res.status} ${errText}`);
      // Wenn Tabelle nicht existiert, informieren
      if (res.status === 404) {
        console.error('⚠️ Die Tabelle public.gbp_daily_actions existiert noch nicht in Supabase. Bitte Migration 002 ausführen.');
        process.exit(1);
      }
    } else {
      inserted += batch.length;
      process.stdout.write(`\rFortschritt: ${inserted}/${records.length} Datensätze geschrieben...`);
    }
  }

  console.log(`\n🎉 Erfolgreich ${inserted} Datensätze in public.gbp_daily_actions gespeichert.`);
}

main().catch(err => {
  console.error('Fataler Fehler:', err);
  process.exit(1);
});
