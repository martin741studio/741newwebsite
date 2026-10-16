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

async function run() {
  const email = 'dinakar@741.studio';
  console.log(`Checking/signing up Dinakar (${email})...`);

  // We can generate a clean initial password
  const initialPassword = 'Dinakar741!Studio#2026';
  const res = await fetch(`${env.SUPABASE_URL}/auth/v1/signup`, {
    method: 'POST',
    headers: {
      'apikey': env.SUPABASE_ANON,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email,
      password: initialPassword
    })
  });

  const data = await res.json();
  console.log('Signup status:', res.status, data);

  if (data.id || (data.user && data.user.id)) {
    const userId = data.id || data.user.id;
    console.log(`✅ Dinakar Auth User created with ID: ${userId}`);

    // Log in as standup admin to update profile and work_actors
    const authRes = await fetch(`${env.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
      method: 'POST',
      headers: { 'apikey': env.SUPABASE_ANON, 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: env.STANDUP_EMAIL, password: env.STANDUP_PASSWORD })
    });
    const adminAuth = await authRes.json();
    const token = adminAuth.access_token;

    // Check/upsert profile
    const profileRes = await fetch(`${env.SUPABASE_URL}/rest/v1/profiles`, {
      method: 'POST',
      headers: {
        'apikey': env.SUPABASE_ANON,
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        'Prefer': 'resolution=merge-duplicates,return=representation'
      },
      body: JSON.stringify({
        user_id: userId,
        role: 'delivery',
        display_name: 'Dinakar',
        lang: 'en'
      })
    });
    console.log('Profile upsert status:', profileRes.status, await profileRes.json());

    // Link user_id in work_actors
    const actorRes = await fetch(`${env.SUPABASE_URL}/rest/v1/work_actors?id=eq.598feba9-7b77-4d5a-8aae-3905325b1338`, {
      method: 'PATCH',
      headers: {
        'apikey': env.SUPABASE_ANON,
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
      },
      body: JSON.stringify({
        user_id: userId
      })
    });
    console.log('Work actor update status:', actorRes.status, await actorRes.json());
  }
}

run().catch(console.error);
