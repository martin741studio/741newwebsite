import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const SECRETS_PATH = join(process.cwd(), '.secrets', 'standup.env');
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

async function getAuthToken() {
  const res = await fetch(`${env.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
    method: 'POST',
    headers: { 'apikey': env.SUPABASE_ANON, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: env.STANDUP_EMAIL, password: env.STANDUP_PASSWORD })
  });
  const data = await res.json();
  return data.access_token;
}

async function run() {
  const token = await getAuthToken();
  const dinakarActorId = '598feba9-7b77-4d5a-8aae-3905325b1338';
  const suriyaTaskId = '591bfc3a-a856-4914-9ae7-f20b2baa5f06';

  // 1. Assign Suriya footer task to Dinakar
  const updateRes = await fetch(`${env.SUPABASE_URL}/rest/v1/work_items?id=eq.${suriyaTaskId}`, {
    method: 'PATCH',
    headers: {
      'apikey': env.SUPABASE_ANON,
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
      'Prefer': 'return=representation'
    },
    body: JSON.stringify({
      doer_id: dinakarActorId,
      status: 'in_progress',
      definition_of_done: 'In WordPress/Elementor Footer Template auf praxis-suriya.de: Links auf /impressum/ und /datenschutz/ setzen und testen (Desktop + Mobile).',
      next_action: 'Dinakar setzt Links im Elementor Theme Builder Footer'
    })
  });

  const updated = await updateRes.json();
  console.log('✅ Updated Suriya task:', updated);
}

run().catch(console.error);
