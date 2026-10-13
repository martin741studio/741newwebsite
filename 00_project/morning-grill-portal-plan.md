# Morning Grill → Command Center in the admin panel (plan, not built)

Version 0.2 · 2026-10-13 · Decision D29 (Martin): "Admin tab + admin-only table". Status: LIVE since 2026-10-13 (staging + live identical, 400,166 bytes). Scheduled runs publish a snapshot and pull answers (Martin's go 13.10.).
Order of portal writers (D28): Freigabe-Dashboard → outreach numbers per client → this build. Start only when both earlier chats report their portal work is done.

## 1. Goal
The Command Center that Martin approved on 13.10. (local page `00_project/assets/morning-grill/command-center.html`) moves into his admin panel on clients.741.studio, behind the admin login. Same three tabs: Decisions, Clients, Agents & waiting. Card clicks save to the database, so the grill session reads them.

## 2. Data flow
```
06:13 / 17:00 run (Mac) → brief.json + goal sheet + registry + ledger
   → scripts/publish_snapshot.py (NEW) → Supabase table grill_snapshots (one row per run, jsonb)
Portal admin tab "Command Center" (NEW, renderCommandCenter()) → reads the latest snapshot
   → Martin clicks an option → RPC grill_answer(card_id, option, note) → table grill_answers
Next grill run → reads grill_answers → writes the answers into state/cards.json (ledger) before acting
```

## 3. Schema draft (NOT applied; needs GO-DB)
```sql
create table public.grill_snapshots (
  id bigserial primary key,
  run_date date not null,
  mode text not null check (mode in ('morning','evening')),
  created_at timestamptz not null default now(),
  data jsonb not null            -- cards, walk queue, clients (goal, roadmap, open, next), agents, sources
);
create table public.grill_answers (
  id bigserial primary key,
  card_id text not null,
  run_date date not null,
  option text not null,          -- a | b | c | park
  note text,                     -- park reason or change wish
  answered_by uuid not null default auth.uid(),
  answered_at timestamptz not null default now()
);
alter table public.grill_snapshots enable row level security;
alter table public.grill_answers  enable row level security;
create policy "admin read snapshots"  on public.grill_snapshots for select using (is_admin());
create policy "admin write snapshots" on public.grill_snapshots for insert with check (is_admin());
create policy "admin read answers"    on public.grill_answers  for select using (is_admin());
create policy "admin write answers"   on public.grill_answers  for insert with check (is_admin());
-- no client, delivery or outreach policy: clients, Dinakar/Tantri (delivery) and Gayo (outreach) see nothing
```
A park answer without a note is rejected in the tab (park needs a reason, R12).

## 4. Portal tab (staging first, memory `portal-single-file-workflow`)
- Admin only (`is_admin()`), new tab next to the existing admin views. Same design as the approved local page and the client-approval dashboard (Anton headline, option cards, "741 recommends", green "Decided" bar).
- Decisions: open cards clickable → RPC insert; decided cards read-only with the answer. Walk queue as checkboxes (saved as answers with option `done`).
- Clients: roadmap P0–P6, goal numbers, open now, next steps; filter chips per client.
- Mobile 390 px works (Martin uses the phone).

## 5. Change to the runs (after the build, needs its own go)
- The scan stays read only. One new write: `publish_snapshot.py` inserts ONE row into `grill_snapshots` with the admin JWT. This is the only write the scheduled run may do (exception to hard rule 1 in the spec, approved only with this build).
- Step A1 reads new rows from `grill_answers` since the bookmark into the ledger.

## 6. Test gate (before live)
1. Staging: the admin sees the tab, a client account and the delivery role see nothing (RLS test with the test client "Testpraxis Musterstadt").
2. Click test at 1440 and 390 px: one answer per card, park without a reason is refused, the next run reads the answers.
3. Screenshot desktop + mobile, then GO-PORTAL for the live upload.

## 7. Gos needed (asked as cards when the build starts)
GO-DB (two tables + RLS) · GO-PORTAL staging · GO-PORTAL live · go to add the snapshot write to the scheduled runs.

## 8. Build log 2026-10-13
- GO-DB (Martin): migration `grill_snapshots_and_answers` applied. Tables `grill_snapshots`, `grill_answers`, RLS admin-only, park needs a reason (check constraint).
- RLS test: admin read+write OK; client sees 0 rows (even when a row exists); client insert refused; delivery sees 0; park with blank reason refused. Test rows rolled back, 0 rows left.
- GO-PORTAL staging (Martin): patched `clients.741.studio/staging/index.html` with `00_project/morning-grill-portal/patch_portal.py` (anchor-based, idempotent, never touches the Freigabe block). Backup: `clients.741.studio/backup/staging-2026-10-13-before-command-center.html`. Live unchanged (380,700 bytes).
- Tab test as admin (Martin's Chrome, 1440 px): button '→ Command Center' visible, snapshot rendered, cards from the database, client roadmaps. 390 px: measured in a 390 px frame, no overflow, 1-column options and open items.
- Write path test: one answer saved as Martin's user, `pull_answers.py` brought it into the ledger, test row deleted, ledger restored.
- Scripts: `scripts/sb.py`, `publish_snapshot.py` (one insert into grill_snapshots), `pull_answers.py` (reads grill_answers). Snapshot ids 4 and 5 are real snapshots of 13.10.
- Found while testing: Chrome was logged in as the client account 'Coralie Suriyapperuma' on staging (left by another chat's test). Martin switched to admin.

## 9. Live (Martin's gos 13.10.)
- Live upload done: fresh pull, FTP file equal to my pull, backup `clients.741.studio/backup/index-2026-10-13-before-command-center.html`, patch, upload. Live check: a client session (Coralie, seen in a second Chrome window) sees no button, 0 snapshots, 0 answers, and 'Nur für Admins'.
- Scheduled runs now start with `pull_answers.py` and end with `publish_snapshot.py` (prompts of morning-grill-0600 and morning-grill-1700 updated).
- Open: Martin confirms the live admin view with his own login (the admin session is in his Chrome, not in the second window).
- Portal rule for all chats: pull fresh before any upload; the patch is idempotent (re-run `patch_portal.py` on a fresh pull if the tab is lost).
