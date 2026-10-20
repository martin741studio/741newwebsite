#!/usr/bin/env node
/**
 * 741 Studio — Backlink Ingestion Worker
 * Ingests local markdown audits (local-sources.md, gap.md, competitors.md)
 * and CSV files from 00_project/assets/ into Supabase public.client_backlinks.
 *
 * Usage:
 *   node scripts/import-backlinks.mjs --dry-run
 *   node scripts/import-backlinks.mjs --apply
 *   node scripts/import-backlinks.mjs --client suriya --apply
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

// Known Client Map (Folder / Name to Supabase UUID)
const CLIENT_MAP = {
  'suriya': { id: '3f71ef33-8c74-4ea1-b2d3-0273c2e99649', name: 'Praxis Suriya', target_domain: 'https://suriya-praxis.de' },
  'huewel': { id: 'f0a6730f-8f56-4c61-8085-1955f3bb285a', name: 'Praxis Hüwel', target_domain: 'https://praxis-huewel.de' },
  'stuerzl': { id: 'b6f6e303-50e4-4afb-a343-337206cec316', name: 'STÜRZL Steuerstrafrecht', target_domain: 'https://stuerzl-strafrecht.de' },
  'dumann': { id: 'd01f4236-8674-45fe-a347-0751fa7b24de', name: 'Naturheilpraxis Daniela Dumann', target_domain: 'https://daniela-dumann.de' },
  'balihealing': { id: 'd0519d13-0bfc-4dfb-b512-57bf550387e6', name: 'Bali Healing', target_domain: 'https://balihealing.de' }
};

const args = process.argv.slice(2);
const DRY_RUN = !args.includes('--apply');
const CLIENT_ARG = (args.find(a => a.startsWith('--client=')) || '').split('=')[1] ||
                   (args.includes('--client') ? args[args.indexOf('--client') + 1] : null);

// ─────────────────────────── Parsers ───────────────────────────

function parseMarkdownTable(content) {
  const lines = content.split('\n');
  const tableRows = [];
  let inTable = false;
  let headers = [];

  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith('|') && trimmed.endsWith('|')) {
      const cells = trimmed.slice(1, -1).split('|').map(c => c.trim());
      if (!inTable) {
        headers = cells.map(h => h.toLowerCase());
        inTable = true;
      } else if (trimmed.includes('---')) {
        continue;
      } else {
        const row = {};
        headers.forEach((h, i) => { row[h] = cells[i] || ''; });
        tableRows.push(row);
      }
    } else {
      inTable = false;
    }
  }
  return tableRows;
}

function parseLocalSources(filePath, clientConfig) {
  if (!existsSync(filePath)) return [];
  const content = readFileSync(filePath, 'utf8');
  const rows = parseMarkdownTable(content);
  const records = [];

  for (const r of rows) {
    const rawUrl = r['url gefunden'] || r['url'] || '';
    const domain = r['domain'] || '';
    if (!domain && !rawUrl) continue;

    // extract clean target URL
    const urlMatch = rawUrl.match(/https?:\/\/[^\s\)]+/);
    const sourceUrl = urlMatch ? urlMatch[0] : (domain ? `https://${domain}` : '');
    if (!sourceUrl) continue;

    records.push({
      client_id: clientConfig.id,
      source_url: sourceUrl,
      target_url: clientConfig.target_domain,
      anchor_text: r['beleg'] || r['taktik'] || null,
      domain_authority: null,
      page_authority: null,
      toxicity_score: 0.0,
      is_toxic: false,
      is_dofollow: true,
      status: 'active',
      source_provider: 'local_sources_scan',
      metadata: {
        tactic: r['taktik'] || null,
        location_dist: r['ort + entfernung'] || null,
        contact: r['kontakt'] || null,
        cost: r['kosten'] || null,
        prerequisite: r['voraussetzung'] || null
      }
    });
  }
  return records;
}

function parseGapTable(filePath, clientConfig) {
  if (!existsSync(filePath)) return [];
  const content = readFileSync(filePath, 'utf8');
  const rows = parseMarkdownTable(content);
  const records = [];

  for (const r of rows) {
    const domain = r['domain'] || '';
    if (!domain || domain.includes('---')) continue;

    const rank = parseInt(r['rank'] || '0', 10);
    const dr = parseInt(r['dr (approx.)'] || '0', 10);
    const isSpam = (r['spam-verdacht'] || '').includes('ja');

    records.push({
      client_id: clientConfig.id,
      source_url: `https://${domain}`,
      target_url: clientConfig.target_domain,
      anchor_text: null,
      domain_authority: isNaN(dr) ? null : dr,
      page_authority: null,
      toxicity_score: isSpam ? 85.0 : (rank < 20 ? 40.0 : 5.0),
      is_toxic: isSpam,
      is_dofollow: !isSpam,
      status: isSpam ? 'disavowed' : 'active',
      source_provider: 'local_competitor_gap',
      metadata: {
        competitors_count: r['wettbewerber (anzahl)'] || null,
        competitors_list: r['welche'] || null,
        raw_rank: rank
      }
    });
  }
  return records;
}

// ─────────────────────────── Main Run ───────────────────────────

async function main() {
  console.log(`=== 741 Backlink Ingestion Worker ===`);
  console.log(`Mode: ${DRY_RUN ? 'DRY-RUN (use --apply to write to Supabase)' : 'APPLY (Live DB sync)'}\n`);

  // 1. Supabase Auth
  const authRes = await fetch(`${env.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
    method: 'POST',
    headers: { apikey: env.SUPABASE_ANON, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: env.STANDUP_EMAIL, password: env.STANDUP_PASSWORD })
  });

  const authData = await authRes.json();
  const token = authData.access_token;
  if (!token) {
    console.error('❌ Supabase Auth fehlgeschlagen:', authData);
    process.exit(1);
  }
  console.log('✅ Authentifiziert als:', env.STANDUP_EMAIL);

  const clientsToProcess = CLIENT_ARG
    ? { [CLIENT_ARG]: CLIENT_MAP[CLIENT_ARG] }
    : CLIENT_MAP;

  let totalParsed = 0;
  let totalInserted = 0;

  for (const [key, cfg] of Object.entries(clientsToProcess)) {
    if (!cfg) {
      console.warn(`⚠️ Client "${key}" nicht in CLIENT_MAP.`);
      continue;
    }
    console.log(`\n▓ Client: ${cfg.name} (${cfg.id})`);

    // Search candidate paths
    const candidatePaths = [
      join(ROOT, `.claude/worktrees/admiring-nightingale-f0f882/00_project/assets/${key}/backlinks/01-baseline/local-sources.md`),
      join(ROOT, `.claude/worktrees/admiring-nightingale-f0f882/00_project/assets/${key}/backlinks/01-baseline/gap.md`),
      join(ROOT, `00_project/assets/${key}/backlinks/local-sources.md`),
      join(ROOT, `00_project/assets/${key}/backlink/local-sources.md`),
      join(ROOT, `00_project/assets/${key}/audit/backlinks.csv`)
    ];

    const records = [];
    for (const p of candidatePaths) {
      if (!existsSync(p)) continue;
      console.log(`   📄 Lese: ${p.replace(ROOT, '.')}`);
      if (p.endsWith('local-sources.md')) {
        records.push(...parseLocalSources(p, cfg));
      } else if (p.endsWith('gap.md')) {
        records.push(...parseGapTable(p, cfg));
      }
    }

    // Deduplicate by source_url + target_url
    const seen = new Set();
    const uniqueRecords = records.filter(r => {
      const k = `${r.source_url}|${r.target_url}`;
      if (seen.has(k)) return false;
      seen.add(k);
      return true;
    });

    console.log(`   Gesamt geparst: ${uniqueRecords.length} Backlinks (${uniqueRecords.filter(r => r.is_toxic).length} toxisch/Spam)`);
    totalParsed += uniqueRecords.length;

    if (!DRY_RUN && uniqueRecords.length > 0) {
      // Chunked upsert to Supabase
      const chunkSize = 50;
      for (let i = 0; i < uniqueRecords.length; i += chunkSize) {
        const chunk = uniqueRecords.slice(i, i + chunkSize);
        const insRes = await fetch(`${env.SUPABASE_URL}/rest/v1/client_backlinks`, {
          method: 'POST',
          headers: {
            apikey: env.SUPABASE_ANON,
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
            Prefer: 'resolution=merge-duplicates'
          },
          body: JSON.stringify(chunk)
        });

        if (!insRes.ok) {
          console.error(`   ❌ Fehler beim Upsert (Chunk ${i}-${i + chunk.length}):`, insRes.status, await insRes.text());
        } else {
          totalInserted += chunk.length;
          console.log(`   ✅ ${chunk.length} Backlinks erfolgreich in Supabase synchronisiert.`);
        }
      }
    } else if (uniqueRecords.length > 0) {
      console.log(`   ℹ️ [DRY-RUN] Erste 3 Beispieldatensätze:`);
      uniqueRecords.slice(0, 3).forEach(r => console.log('     -', r.source_url, `[DA:${r.domain_authority || 'n/a'}]`, r.is_toxic ? '⚠️ TOXIC' : '✔ OK'));
    }
  }

  console.log(`\n========================================`);
  console.log(`Fertig: ${totalParsed} Backlinks verarbeitet, ${totalInserted} live geschrieben.`);
}

main().catch(err => {
  console.error('Fataler Fehler:', err);
  process.exit(1);
});
