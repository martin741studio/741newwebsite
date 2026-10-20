import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const ROOT = process.cwd();
const SECRETS_PATH = join(ROOT, '.secrets', 'standup.env');

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

async function queryTable(token, endpoint) {
  const res = await fetch(`${env.SUPABASE_URL}/rest/v1/${endpoint}`, {
    headers: {
      'apikey': env.SUPABASE_ANON,
      'Authorization': `Bearer ${token}`
    }
  });
  if (!res.ok) {
    return { error: `HTTP ${res.status}: ${await res.text()}` };
  }
  return await res.json();
}

async function run() {
  const token = await getAuthToken();
  const clients = await queryTable(token, 'clients?select=id,name,status&order=name.asc');
  const clientMap = Object.fromEntries(clients.map(c => [c.id, c.name]));

  // 1. Recent Client Decisions / Responses (Last 7 days)
  console.log('=== CLIENT DECISIONS & CHANGE REQUESTS (RECENT) ===');
  const decisions = await queryTable(token, 'approval_decisions?select=*&order=created_at.desc&limit=15');
  for (const d of decisions) {
    const clientName = clientMap[d.client_id] || d.client_id;
    console.log(`\n• Client: ${clientName} (${d.actor_name}, action: ${d.action})`);
    console.log(`  Item ID: ${d.item_id}`);
    console.log(`  Date: ${d.created_at}`);
    if (d.variant_key) console.log(`  Variant Key: ${d.variant_key}`);
    if (d.note) console.log(`  Note/Feedback: "${d.note}"`);
  }

  // 2. Open / Pending Approval Items
  console.log('\n=== OPEN / PENDING APPROVAL ITEMS IN PORTAL ===');
  const openItems = await queryTable(token, 'approval_items?status=neq.approved&order=created_at.desc&limit=20');
  for (const item of openItems) {
    const clientName = clientMap[item.client_id] || item.client_id;
    console.log(`\n• [${item.status.toUpperCase()}] ${clientName} | ${item.title}`);
    console.log(`  Item ID: ${item.id} (Category: ${item.category || item.module || 'N/A'})`);
    console.log(`  Variants: ${Object.keys(item.variants || {}).join(', ')}`);
    console.log(`  Recommendation: ${item.recommendation || item.recommended_variant || 'None'}`);
  }

  // 3. Active Work Items (Kundenarbeit)
  console.log('\n=== ACTIVE WORK ITEMS (KUNDENARBEIT) ===');
  const activeWork = await queryTable(token, 'work_items?status=in.(in_progress,needs_check,planned,waiting)&order=priority.asc,due_on.asc&limit=25');
  for (const w of activeWork) {
    const clientName = clientMap[w.client_id] || w.client_id;
    console.log(`\n• [${w.status.toUpperCase()}] ${clientName}: "${w.title}"`);
    console.log(`  Type: ${w.type} | Priority: ${w.priority} | Due: ${w.due_on || 'No due date'}`);
    if (w.waiting_on) console.log(`  Waiting On: ${w.waiting_on} (Reason: ${w.status_reason || 'N/A'})`);
    if (w.definition_of_done) console.log(`  DoD: ${w.definition_of_done}`);
    if (w.next_action) console.log(`  Next Action: ${w.next_action}`);
  }
}

run().catch(console.error);
