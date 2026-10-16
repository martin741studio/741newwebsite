#!/usr/bin/env node
/**
 * 741 Studio — Google Drive & Supabase Cross-Platform Sync
 * Syncs Google Drive root folder URLs and IDs (account: 741studio18@gmail.com / "741 Clients")
 * into Supabase public.clients and public.client_drive_assets.
 *
 * This ensures that any LLM, AI agent, or automation platform querying Supabase
 * can immediately locate the client's working Google Drive workspace, docs, and sheets.
 *
 * Usage:
 *   node scripts/sync-gdrive-clients.mjs [--apply]
 */

import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

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

const GDRIVE_CLIENT_REGISTRY = [
  {
    clientId: '3f71ef33-8c74-4ea1-b2d3-0273c2e99649',
    name: 'Praxis Suriya',
    folderName: '741 Clients / Praxis Suriya',
    driveUrl: 'https://drive.google.com/drive/folders/1Hg7S3n1HyZmYmk4HLFmWfdTDtbI9NBis',
    driveId: '1Hg7S3n1HyZmYmk4HLFmWfdTDtbI9NBis'
  },
  {
    clientId: 'd01f4236-8674-45fe-a347-0751fa7b24de',
    name: 'Naturheilpraxis Daniela Dumann',
    folderName: '741 Clients / Daniela Dumann',
    driveUrl: 'https://drive.google.com/drive/folders/1TYstYL7lzgRBgBk8P1MvOGcXtG4nEuD5',
    driveId: '1TYstYL7lzgRBgBk8P1MvOGcXtG4nEuD5'
  },
  {
    clientId: 'f0a6730f-8f56-4c61-8085-1955f3bb285a',
    name: 'Praxis Hüwel',
    folderName: '741 Clients / Martin Hüwel',
    driveUrl: 'https://drive.google.com/drive/folders/1d_NkMF5YEDAkpuBvsfvfGJW9nnVloul6',
    driveId: '1d_NkMF5YEDAkpuBvsfvfGJW9nnVloul6'
  },
  {
    clientId: '444ac77b-747d-4855-89e5-12ac97d2363c',
    name: 'Maria Brasse',
    folderName: '741 Clients / Maria Brasse',
    driveUrl: 'https://drive.google.com/drive/folders/18Zel5nZ7jNY6yFPsHJQrrS6-mLKeUkY8',
    driveId: '18Zel5nZ7jNY6yFPsHJQrrS6-mLKeUkY8'
  },
  {
    clientId: 'b6f6e303-50e4-4afb-a343-337206cec316',
    name: 'STÜRZL Steuerstrafrecht',
    folderName: '741 Clients / Dr. Anja Stürzl',
    driveUrl: 'https://drive.google.com/drive/folders/1dF8IKY_Syjnji2CyHGAhY8SFb78dmlua',
    driveId: '1dF8IKY_Syjnji2CyHGAhY8SFb78dmlua'
  }
];

const DRY_RUN = !process.argv.includes('--apply');

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

async function main() {
  console.log('=== 741 Studio — Google Drive to Supabase Sync ===');
  console.log(`Mode: ${DRY_RUN ? 'DRY-RUN (use --apply to write to Supabase)' : 'APPLY (writing to Supabase)'}\n`);
  console.log(`Target Google Account: 741studio18@gmail.com ("741 Clients")`);
  console.log(`Primary Database: Supabase (${env.SUPABASE_URL})\n`);

  for (const client of GDRIVE_CLIENT_REGISTRY) {
    console.log(`• [${client.name}] (${client.clientId})`);
    console.log(`  Folder: ${client.folderName}`);
    console.log(`  URL:    ${client.driveUrl}`);
    console.log(`  ID:     ${client.driveId}`);

    if (!DRY_RUN) {
      const token = await getAuthToken();
      const headers = {
        'apikey': env.SUPABASE_ANON,
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
      };

      // 1. Fetch current client_stack to preserve existing keys
      const getRes = await fetch(`${env.SUPABASE_URL}/rest/v1/clients?id=eq.${client.clientId}&select=client_stack`, {
        headers
      });
      const [existing] = await getRes.json();
      const currentStack = existing?.client_stack || {};

      // 2. Patch clients with updated drive metadata
      const updatedStack = {
        ...currentStack,
        drive_account: '741studio18@gmail.com',
        drive_root_folder: client.folderName,
        drive_folder_url: client.driveUrl,
        drive_folder_id: client.driveId,
        drive_last_synced: new Date().toISOString()
      };

      const patchRes = await fetch(`${env.SUPABASE_URL}/rest/v1/clients?id=eq.${client.clientId}`, {
        method: 'PATCH',
        headers,
        body: JSON.stringify({ client_stack: updatedStack })
      });

      if (!patchRes.ok) {
        console.error(`  ❌ Failed to patch client: ${await patchRes.text()}`);
      } else {
        console.log(`  ✓ Patched public.clients.client_stack`);
      }

      // 3. Upsert root folder pointer into public.client_drive_assets
      const rootAsset = {
        client_id: client.clientId,
        drive_file_id: client.driveId,
        file_name: client.folderName,
        file_path: '_root',
        mime_type: 'application/vnd.google-apps.folder',
        category: 'drive_root',
        web_view_link: client.driveUrl,
        last_synced_at: new Date().toISOString()
      };

      const assetRes = await fetch(`${env.SUPABASE_URL}/rest/v1/client_drive_assets?on_conflict=client_id,file_path`, {
        method: 'POST',
        headers: {
          ...headers,
          'Prefer': 'resolution=merge-duplicates,return=representation'
        },
        body: JSON.stringify([rootAsset])
      });

      if (!assetRes.ok) {
        console.error(`  ❌ Failed to upsert root asset: ${await assetRes.text()}`);
      } else {
        console.log(`  ✓ Upserted root folder pointer in public.client_drive_assets`);
      }
    }
  }

  if (DRY_RUN) {
    console.log('\n[Dry-run completed. Run with --apply to commit to Supabase]');
  } else {
    console.log('\n✅ Successfully synchronized Google Drive roots to Supabase!');
  }
}

main().catch(err => {
  console.error('❌ Sync Error:', err);
  process.exit(1);
});
