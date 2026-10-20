#!/usr/bin/env node
/**
 * Listings-Inbox-Poller.
 *
 * Liest das Catch-all-Postfach der Listings-Domain (suriya@listings.741.studio,
 * huewel@listings.741.studio, …), zieht aus jeder Mail den Bestätigungs-Link und
 * schreibt alles nach Supabase `listing_emails`. So landen alle Verzeichnis-
 * Bestätigungen an EINEM Ort — nie wieder im Postfach suchen.
 *
 *   node reporting/listings-inbox-poller.mjs           # neue Mails holen
 *   node reporting/listings-inbox-poller.mjs --all     # auch schon gelesene
 *
 * Läuft am besten als Cron auf dem Dev-VPS (fixe Umgebung), z. B. alle 10 Min.
 *
 * Auth:
 *   .secrets/listings-imap.env  -> IMAP_HOST / IMAP_PORT / IMAP_USER / IMAP_PASS
 *   .secrets/standup.env        -> SUPABASE_URL / SUPABASE_ANON / STANDUP_EMAIL / STANDUP_PASSWORD
 *
 * Abhängigkeit: `imapflow` (einmalig `npm i imapflow` im Repo). Rest = Node-Builtins.
 */
import { readFileSync } from 'node:fs';
import { ImapFlow } from 'imapflow';

const ROOT = new URL('../', import.meta.url);
const env = (name) => Object.fromEntries(
  readFileSync(new URL('.secrets/' + name, ROOT), 'utf8')
    .split('\n').filter(Boolean).filter(l => !l.trimStart().startsWith('#'))
    .map(l => { const i = l.indexOf('='); return [l.slice(0, i).trim(), l.slice(i + 1).trim()]; }));
const IM = env('listings-imap.env');
const SB = env('standup.env');
const ALL = process.argv.includes('--all');

// --- Supabase admin ---
const login = await (await fetch(`${SB.SUPABASE_URL}/auth/v1/token?grant_type=password`, {
  method: 'POST', headers: { apikey: SB.SUPABASE_ANON, 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: SB.STANDUP_EMAIL, password: SB.STANDUP_PASSWORD }) })).json();
const TOKEN = login.access_token;
if (!TOKEN) { console.error('Supabase-Login fehlgeschlagen'); process.exit(1); }
const H = { apikey: SB.SUPABASE_ANON, Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' };
const insert = (row) => fetch(SB.SUPABASE_URL + '/rest/v1/listing_emails', {
  method: 'POST', headers: { ...H, Prefer: 'return=minimal,resolution=ignore-duplicates' }, body: JSON.stringify(row) }).then(r => r.status);

// --- Bestätigungs-Link heuristisch ziehen ---
const KEYS = /(verify|confirm|activate|validat|aktivier|bestätig|bestaetig|token|complete|freischalt|opt-in|optin)/i;
function extractVerifyLink(text) {
  const urls = [...(text || '').matchAll(/https?:\/\/[^\s"'<>)]+/gi)].map(m => m[0]);
  if (!urls.length) return null;
  const scored = urls.map(u => ({ u, s: KEYS.test(u) ? 2 : 0 }));
  scored.sort((a, b) => b.s - a.s);
  return scored[0].u;
}

// Hard guard: never let a cron run hang forever.
setTimeout(() => { console.error('Timeout-Guard: beende nach 80s.'); process.exit(0); }, 80000).unref();

const client = new ImapFlow({
  host: IM.IMAP_HOST, port: Number(IM.IMAP_PORT || 993), secure: true,
  auth: { user: IM.IMAP_USER, pass: IM.IMAP_PASS }, logger: false,
  greetingTimeout: 15000, disableAutoIdle: true });
// Swallow post-processing socket errors so a hung logout never crashes the cron.
client.on('error', () => {});

await client.connect();
const lock = await client.getMailboxLock('INBOX');
let seen = 0, saved = 0;
try {
  const uids = await client.search(ALL ? { all: true } : { seen: false }, { uid: true });
  const msgs = (uids && uids.length) ? await client.fetchAll(uids, { envelope: true, source: true }, { uid: true }) : [];
  for (const msg of msgs) {
    seen++;
    const env2 = msg.envelope || {};
    const to = (env2.to || []).map(a => a.address).join(',');
    const toAddr = (env2.to || [])[0]?.address || '';
    const slug = toAddr.split('@')[0] || null;
    const from = (env2.from || [])[0]?.address || '';
    const raw = msg.source ? msg.source.toString('utf8') : '';
    // simpler: whole raw source for link extraction (works for text + html parts)
    const verify = extractVerifyLink(raw);
    const domainGuess = from.split('@')[1] || null;
    // Auto-confirm: fetch the verify link immediately so no manual click needed.
    let confirmed = false;
    if (verify) {
      try {
        const r = await fetch(verify, { redirect: 'follow', signal: AbortSignal.timeout(15000) });
        confirmed = r.ok || r.status < 400;
        console.log(`Auto-confirm ${r.status}: ${verify.slice(0, 80)}`);
      } catch (e) { console.log(`Auto-confirm error: ${e.message}`); }
    }
    const code = await insert({
      to_addr: to, client_slug: slug, from_addr: from,
      subject: env2.subject || '', body: raw.slice(0, 20000),
      verify_link: verify, directory_guess: domainGuess,
      received_at: env2.date ? new Date(env2.date).toISOString() : null,
      message_uid: `${IM.IMAP_USER}:${msg.uid}`,
      confirmed,
    });
    if (code < 300) saved++;
  }
  if (!ALL && uids && uids.length) { try { await client.messageFlagsAdd(uids, ['\\Seen'], { uid: true }); } catch { /* ignore */ } }
} finally {
  try { lock.release(); } catch { /* ignore */ }
  try { client.close(); } catch { /* ignore */ }  // force-close; graceful logout hangs on this server
}
console.log(`Geprüft: ${seen}, gespeichert: ${saved}.`);
process.exit(0);
