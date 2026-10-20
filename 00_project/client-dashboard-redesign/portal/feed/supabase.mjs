// Read-only portal database helper. Logs in with the 741 admin account from .secrets/standup.env (same pattern as reporting/daily-standup.sh)
// and sends GET requests only. No writes. The password is never printed.
import { readFileSync } from 'node:fs';

const ENV_PATH = new URL('../../../../.secrets/standup.env', import.meta.url);
let session = null;

function env() {
  const e = {};
  for (const l of readFileSync(ENV_PATH, 'utf8').split('\n')) { const i = l.indexOf('='); if (i > 0) e[l.slice(0, i).trim()] = l.slice(i + 1).trim().replace(/^["']|["']$/g, ''); }
  for (const k of ['SUPABASE_URL', 'SUPABASE_ANON', 'STANDUP_EMAIL', 'STANDUP_PASSWORD']) if (!e[k]) throw new Error(`${k} missing in .secrets/standup.env`);
  return e;
}
async function login() {
  if (session) return session;
  const e = env();
  const r = await fetch(`${e.SUPABASE_URL}/auth/v1/token?grant_type=password`, { method: 'POST', headers: { apikey: e.SUPABASE_ANON, 'Content-Type': 'application/json' }, body: JSON.stringify({ email: e.STANDUP_EMAIL, password: e.STANDUP_PASSWORD }) });
  const j = await r.json(); if (!r.ok || !j.access_token) throw new Error(`portal login failed (${r.status})`);
  return (session = { url: e.SUPABASE_URL, anon: e.SUPABASE_ANON, token: j.access_token });
}
/** GET one PostgREST path, for example "client_citations?client_id=eq.<id>&select=status". */
export async function sbGet(path) {
  const s = await login();
  const r = await fetch(`${s.url}/rest/v1/${path}`, { method: 'GET', headers: { apikey: s.anon, Authorization: `Bearer ${s.token}` } });
  const j = await r.json(); if (!r.ok) throw new Error(`portal read ${path.split('?')[0]}: ${r.status} ${JSON.stringify(j).slice(0, 150)}`);
  return j;
}
