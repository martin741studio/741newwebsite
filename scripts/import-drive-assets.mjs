#!/usr/bin/env node
/**
 * 741 Studio — Client Drive Assets Ingestion Worker
 * Scans local client _drive directories (PDF deliverables, spreadsheets, exports, CRO prototypes)
 * and catalogs them into Supabase public.client_drive_assets with SHA256 checksums.
 *
 * Usage:
 *   node scripts/import-drive-assets.mjs --dry-run
 *   node scripts/import-drive-assets.mjs --apply
 */

import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { resolve, join, relative, extname, basename } from 'node:path';
import { createHash } from 'node:crypto';

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
  'huewel': 'f0a6730f-8f56-4c61-8085-1955f3bb285a',
  'stuerzl': 'b6f6e303-50e4-4afb-a343-337206cec316',
  'suriya': '3f71ef33-8c74-4ea1-b2d3-0273c2e99649'
};

const MIME_MAP = {
  '.pdf': 'application/pdf',
  '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  '.html': 'text/html',
  '.json': 'application/json',
  '.zip': 'application/zip',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.md': 'text/markdown',
  '.csv': 'text/csv'
};

function getCategory(filePath, ext) {
  const lower = filePath.toLowerCase();
  if (ext === '.xlsx' || ext === '.csv') return 'sheet';
  if (ext === '.png' || ext === '.jpg' || ext === '.jpeg' || lower.includes('prototype') || lower.includes('/cro')) return 'cro_asset';
  if (ext === '.pdf') {
    if (lower.includes('angebot') || lower.includes('proposal') || lower.includes('vertrag')) return 'offer_pdf';
    return 'content_export';
  }
  return 'content_export';
}

function calculateSha256(filePath) {
  const buffer = readFileSync(filePath);
  return createHash('sha256').update(buffer).digest('hex');
}

const args = process.argv.slice(2);
const DRY_RUN = !args.includes('--apply');

async function getAuthToken() {
  const res = await fetch(`${env.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
    method: 'POST',
    headers: { 'apikey': env.SUPABASE_ANON, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: env.STANDUP_EMAIL, password: env.STANDUP_PASSWORD })
  });
  if (!res.ok) {
    throw new Error(`Auth failed (${res.status}): ${await res.text()}`);
  }
  const data = await res.json();
  return data.access_token;
}

function scanClientDriveAssets(clientSlug, clientId) {
  const clientRoot = join(ROOT, '00_project', 'assets', clientSlug);
  if (!existsSync(clientRoot)) return [];

  const assets = [];

  function walk(currentDir) {
    const entries = readdirSync(currentDir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = join(currentDir, entry.name);
      if (entry.isDirectory()) {
        // Skip hidden or non-asset directories
        if (!entry.name.startsWith('.')) {
          walk(fullPath);
        }
      } else if (entry.isFile()) {
        // Check if inside a _drive folder
        if (fullPath.includes('/_drive/') || fullPath.includes('/_drive-')) {
          const relPath = relative(clientRoot, fullPath);
          const ext = extname(entry.name).toLowerCase();
          const stats = statSync(fullPath);
          const hash = calculateSha256(fullPath);
          const category = getCategory(relPath, ext);
          const mimeType = MIME_MAP[ext] || 'application/octet-stream';

          assets.push({
            client_id: clientId,
            file_name: entry.name,
            file_path: relPath,
            mime_type: mimeType,
            size_bytes: stats.size,
            sha256_hash: hash,
            category: category,
            last_synced_at: new Date().toISOString()
          });
        }
      }
    }
  }

  walk(clientRoot);
  return assets;
}

async function main() {
  console.log('=== 741 Studio Client Drive Assets Ingestion Worker ===');
  console.log(`Mode: ${DRY_RUN ? 'DRY-RUN (use --apply to write to Supabase)' : 'APPLY (writing to Supabase)'}\n`);

  let allAssets = [];

  for (const [slug, clientId] of Object.entries(CLIENT_MAP)) {
    const clientAssets = scanClientDriveAssets(slug, clientId);
    console.log(`• [${slug}] Found ${clientAssets.length} drive assets`);
    allAssets = allAssets.concat(clientAssets);
  }

  console.log(`\nTotal assets cataloged: ${allAssets.length}`);

  // Summary by category and file type
  const catCounts = {};
  const extCounts = {};
  for (const a of allAssets) {
    catCounts[a.category] = (catCounts[a.category] || 0) + 1;
    const ext = extname(a.file_name);
    extCounts[ext] = (extCounts[ext] || 0) + 1;
  }
  console.log('By Category:', catCounts);
  console.log('By Extension:', extCounts);

  if (DRY_RUN) {
    console.log('\n[DRY-RUN completed. Run with --apply to commit to Supabase]');
    return;
  }

  const token = await getAuthToken();
  const headers = {
    'apikey': env.SUPABASE_ANON,
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  };

  // Upsert in batches of 50 to avoid request size limits
  console.log('\nWriting to public.client_drive_assets in batches...');
  const BATCH_SIZE = 50;
  let insertedCount = 0;

  for (let i = 0; i < allAssets.length; i += BATCH_SIZE) {
    const batch = allAssets.slice(i, i + BATCH_SIZE);
    const res = await fetch(`${env.SUPABASE_URL}/rest/v1/client_drive_assets?on_conflict=client_id,file_path`, {
      method: 'POST',
      headers: {
        ...headers,
        'Prefer': 'resolution=merge-duplicates,return=representation'
      },
      body: JSON.stringify(batch)
    });

    if (!res.ok) {
      const errText = await res.text();
      throw new Error(`Failed to upsert client_drive_assets batch ${i} (${res.status}): ${errText}`);
    }

    const inserted = await res.json();
    insertedCount += inserted.length;
    console.log(`  Uploaded batch ${i / BATCH_SIZE + 1} (${inserted.length} records)...`);
  }

  console.log(`\n✅ Successfully upserted ${insertedCount} client drive assets into public.client_drive_assets!`);
}

main().catch(err => {
  console.error('❌ Ingestion Error:', err);
  process.exit(1);
});
