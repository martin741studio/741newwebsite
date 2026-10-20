-- DRAFT. NOT APPLIED. Do not run before Martin says "go".
-- Target: Supabase 741-portal (galjmtozcgxcwtzkzbpi), schema public.
-- Purpose: Maps audit database. See data-model.md.
-- Admin-only access. The client reads static HTML through client_reports, never these tables.

create table if not exists audit_fields (
  field_id        text primary key,                 -- 'B05.03'
  block           text not null,                    -- 'B05'
  label_de        text not null,
  input_type      text not null check (input_type in ('C','A','B','D','M','C+A','A+C','C+B','A+B','A+D','A+M','A+B+C','C+D')),
  tool            text,
  weight          numeric not null default 1,
  critical        boolean not null default false,
  light           boolean not null default false,
  rule            jsonb not null default '{}'::jsonb,
  client_safe     boolean not null default true,
  active          boolean not null default true,
  catalog_version text not null
);

create table if not exists audit_runs (
  id                uuid primary key default gen_random_uuid(),
  client_id         uuid references clients(id),    -- null for a prospect
  subject_slug      text not null,
  subject_name      text not null,
  subject_type      text not null check (subject_type in ('client','prospect')),
  mode              text not null check (mode in ('call','kickoff','reaudit')),
  depth             text not null default 'deep' check (depth in ('light','deep')),
  status            text not null default 'planned'
                    check (status in ('planned','collecting','scored','reviewed','released')),
  params            jsonb not null default '{}'::jsonb,   -- keywords, grid, radius, competitor ids
  previous_run_id   uuid references audit_runs(id),
  score_total       numeric,
  score_coverage    numeric,
  verdict           text check (verdict in ('Ja','Noch nicht','Nein','Offen')),
  verdict_reason    text,
  cost_eur          numeric not null default 0,
  cost_credits      integer not null default 0,
  corrections_count integer,
  catalog_version   text not null,
  started_at        timestamptz not null default now(),
  finished_at       timestamptz,
  released_at       timestamptz
);
create index if not exists audit_runs_subject_idx on audit_runs (subject_slug, started_at desc);

create table if not exists audit_evidence (
  id             text not null,                     -- 'ev_0007', unique inside one run
  run_id         uuid not null references audit_runs(id) on delete cascade,
  kind           text not null check (kind in ('falcon_report','api_json','screenshot','html_snapshot','form_answers','drive_file','file')),
  storage_path   text not null,
  drive_file_id  text,
  sha256         text not null,
  tool           text not null,
  request        jsonb not null default '{}'::jsonb, -- no secrets
  cost_eur       numeric not null default 0,
  cost_credits   integer not null default 0,
  collected_at   timestamptz not null,
  refetch_after  timestamptz,
  primary key (run_id, id)
);

create table if not exists audit_findings (
  id              uuid primary key default gen_random_uuid(),
  run_id          uuid not null references audit_runs(id) on delete cascade,
  field_id        text not null references audit_fields(field_id),
  status          text not null check (status in ('green','yellow','red','grey','unknown')),
  value           jsonb,
  finding_de      text not null,
  why_de          text,
  severity        smallint check (severity between 1 and 5),
  impact          smallint check (impact between 1 and 5),
  effort          text check (effort in ('S','M','L')),
  owner           text,
  action_de       text,
  confidence      text not null check (confidence in ('verified','derived','client_stated')),
  evidence_ids    text[] not null default '{}',
  source_tool     text not null,
  source_ref      text,
  refetch         jsonb,
  depends_on      text[] not null default '{}',
  drilldown_hint  text,
  client_safe     boolean not null default true,
  priority_rank   integer,
  collected_at    timestamptz not null,
  unique (run_id, field_id)
);
-- A finding with status other than 'unknown'/'grey' must have evidence or be client_stated/derived.
alter table audit_findings add constraint audit_findings_evidence_chk
  check (status in ('unknown','grey') or confidence in ('client_stated','derived') or array_length(evidence_ids,1) >= 1);

create table if not exists audit_answers (
  id            uuid primary key default gen_random_uuid(),
  subject_slug  text not null,
  client_id     uuid references clients(id),
  question_id   text not null,                      -- 'Q-B02-02'
  answer        jsonb not null,
  version       integer not null default 1,
  answered_by   text,
  answered_at   timestamptz not null default now(),
  source        text not null check (source in ('form','martin','sheet_import'))
);
create index if not exists audit_answers_lookup_idx on audit_answers (subject_slug, question_id, version desc);

create table if not exists audit_keywords (
  run_id        uuid not null references audit_runs(id) on delete cascade,
  keyword       text not null,
  priority      smallint not null check (priority between 1 and 3),
  cluster       text,
  service_ref   text,
  volume        integer,
  volume_source text,
  falcon        jsonb not null default '{}'::jsonb,  -- per platform: report_key, solv, arp, grid, radius, scanned_at
  credits       integer not null default 0,
  primary key (run_id, keyword)
);

create table if not exists audit_competitors (
  run_id       uuid not null references audit_runs(id) on delete cascade,
  rank         smallint not null,
  name         text not null,
  place_id     text,
  domain       text,
  reviews      integer,
  rating       numeric,
  categories   jsonb,
  solv         numeric,
  arp          numeric,
  ref_domains  integer,
  backlinks    integer,
  first_seen   date,
  weakness     text,
  pick_reason  text,
  primary key (run_id, rank)
);

create table if not exists audit_actions (
  id          uuid primary key default gen_random_uuid(),
  run_id      uuid not null references audit_runs(id) on delete cascade,
  finding_ids uuid[] not null default '{}',
  action_de   text not null,
  owner       text,
  impact      smallint check (impact between 1 and 5),
  effort      text check (effort in ('S','M','L')),
  go_required boolean not null default true,
  status      text not null default 'proposed' check (status in ('proposed','approved','done')),
  task_id     uuid references tasks(id)
);

create or replace view audit_run_deltas as
select n.run_id,
       n.field_id,
       p.status  as status_before,
       n.status  as status_now,
       p.value   as value_before,
       n.value   as value_now,
       (rn.params->'keywords' = rp.params->'keywords'
        and rn.params->>'grid' = rp.params->>'grid'
        and rn.params->>'radius' = rp.params->>'radius') as comparable
from audit_findings n
join audit_runs rn on rn.id = n.run_id
left join audit_runs rp on rp.id = rn.previous_run_id
left join audit_findings p on p.run_id = rp.id and p.field_id = n.field_id;

-- RLS: enable on every table. Policies follow the existing admin/team pattern of the portal.
-- Policies are NOT written here. Copy them from the pattern used on scans / client_reports before applying.
alter table audit_fields      enable row level security;
alter table audit_runs        enable row level security;
alter table audit_evidence    enable row level security;
alter table audit_findings    enable row level security;
alter table audit_answers     enable row level security;
alter table audit_keywords    enable row level security;
alter table audit_competitors enable row level security;
alter table audit_actions     enable row level security;
