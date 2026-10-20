-- DRAFT. NOT APPLIED. Needs Martin's go (same go as the audit tables).
-- Target: Supabase project 741-portal (galjmtozcgxcwtzkzbpi). Written 2026-10-11.
-- RLS: admin full access. Client reads only released rows of its own client_id.

create table playbook_runs (
  id uuid primary key default gen_random_uuid(),
  client_id uuid references clients(id),          -- nullable: prospects have no client row
  subject_slug text not null,
  niche text not null check (niche in ('health','trades_local','law_tax')),
  mode text not null check (mode in ('kickoff','refresh','quickwins')),
  catalog_version text not null,
  audit_run_id uuid,                              -- link to the audit run used as evidence, if any
  as_of date not null,
  cost_eur numeric(8,2) default 0,
  falcon_credits int default 0,
  corrections_count int default 0,                -- counted at Checkpoint A
  released_to_client boolean default false,       -- Checkpoint B
  created_at timestamptz default now()
);

create table measure_status (
  run_id uuid references playbook_runs(id) on delete cascade,
  measure_id text not null,                       -- G01 .. O20, matches the catalogue
  status text not null check (status in ('done','partly','missing','n/a','unknown')),
  last_known_status text,
  stale boolean default false,
  confidence text check (confidence in ('verified','derived','client_stated','none')),
  finding_de text,
  newest_evidence_date date,
  blocked_by text[],
  primary key (run_id, measure_id)
);

create table playbook_evidence (
  id uuid primary key default gen_random_uuid(),
  run_id uuid references playbook_runs(id) on delete cascade,
  measure_id text not null,
  type text not null check (type in ('live','scan','document')),
  ref text not null,                              -- path, Drive file id, URL, report key, audit field + run id
  evidence_date date not null,
  note text,
  sha256 text
);

create table playbook_tasks (
  id uuid primary key default gen_random_uuid(),
  run_id uuid references playbook_runs(id) on delete cascade,
  measure_id text not null,
  action_text text not null,
  owner_type text[] not null,                     -- agent, client, human
  gate text[],
  score numeric(5,2),
  impact int, confidence numeric(3,2), effort numeric(3,1), risk int,
  phase text check (phase in ('d1-30','m2+','later')),
  depends_on text[],
  state text not null default 'proposed'
    check (state in ('proposed','approved','blocked','in_progress','done','verified')),
  batch_id uuid,                                  -- execution batch (Checkpoint C)
  portal_task_id uuid                             -- link to tasks table, if created
);

create table playbook_change_log (
  id uuid primary key default gen_random_uuid(),
  task_id uuid references playbook_tasks(id),
  executor text not null,
  before_value text, after_value text,
  evidence_id uuid references playbook_evidence(id),
  changed_at timestamptz default now()
);
