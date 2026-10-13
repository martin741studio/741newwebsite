-- Client work view · Migration v1 for Supabase 741-portal (galjmtozcgxcwtzkzbpi)
-- Status 2026-10-13: draft. Apply ONLY after Martin's go. Basis: ../data-model.md, ../brief.md (design go 13.10.)
-- Step 1 = admin views. Team policies (step 2) and the client view (step 3, pilot Bali Healing EN) come with their builds.
--
-- Rules enforced in the database:
--   R1 one accountable person (actor kind admin/team) per item, plus a separate doer (any actor)
--   R2 "done" only with proof (evidence relation proves/produced) and verified_by = a person
--   R3 every producer writes idempotently: unique (source, source_id) / idempotency_key
--   R4 history is append-only (work_events: no update/delete policy)
--   R5 client colour is computed automatically (view work_client_health), with reason, owner, next step

begin;

-- ---------- actors: people, agents, scripts, clients, outside parties ----------
create table if not exists public.work_actors (
  id             uuid primary key default gen_random_uuid(),
  kind           text not null check (kind in ('admin','team','agent','script','client','external')),
  name           text not null,
  user_id        uuid references auth.users(id) on delete set null,
  client_id      uuid references public.clients(id) on delete cascade,      -- for kind client
  owner_actor_id uuid references public.work_actors(id),                    -- human owner of an agent/script
  active         boolean not null default true,
  created_at     timestamptz not null default now(),
  unique nulls not distinct (kind, name, client_id)
);

-- ---------- goals and phases (13 weeks -> milestones P0–P6) ----------
create table if not exists public.work_goals (
  id          uuid primary key default gen_random_uuid(),
  client_id   uuid not null references public.clients(id) on delete cascade,
  title       text not null,
  metric_key  text,
  baseline    text,
  target      text,
  due_on      date,
  source_link text,
  status      text not null default 'proposed' check (status in ('proposed','agreed','reached','dropped')),
  created_at  timestamptz not null default now()
);

create table if not exists public.work_phases (
  id           uuid primary key default gen_random_uuid(),
  client_id    uuid not null references public.clients(id) on delete cascade,
  code         text not null check (code in ('P0','P1','P2','P3','P4','P5','P6')),
  label        text not null,
  planned_from date,
  planned_to   date,
  status       text not null default 'open' check (status in ('open','current','done')),
  unique (client_id, code)
);

-- ---------- work items: one list for all work ----------
create table if not exists public.work_items (
  id                 uuid primary key default gen_random_uuid(),
  client_id          uuid references public.clients(id) on delete cascade,   -- null = 741 internal (all clients)
  phase_id           uuid references public.work_phases(id) on delete set null,
  parent_id          uuid references public.work_items(id) on delete set null,
  goal_id            uuid references public.work_goals(id) on delete set null,
  type               text not null default 'task' check (type in ('task','deliverable','approval','client_todo','intake')),
  title              text not null,
  client_text        text,                         -- wording for the client view (step 3)
  definition_of_done text,
  status             text not null default 'planned'
                     check (status in ('intake','planned','in_progress','waiting','needs_check','done','dropped')),
  waiting_on         text check (waiting_on in ('client','martin','team','google','external')),
  status_reason      text,
  priority           text not null default 'normal' check (priority in ('blocker','high','normal','low')),
  accountable_id     uuid not null references public.work_actors(id),
  doer_id            uuid not null references public.work_actors(id),
  due_on             date,
  next_action        text,
  since              date,                         -- when the current wait or intake started (real date from the source)
  week               int,                          -- kept from the old 13-week template
  visibility         text not null default 'internal' check (visibility in ('internal','client')),
  done_at            timestamptz,
  verified_by        uuid references public.work_actors(id),
  verified_at        timestamptz,
  resolution         text check (resolution in ('completed','canceled','duplicate','replaced')),
  source             text not null,                -- template | grill | session | registry | approval | nightshift | report_feedback | access | manual
  source_id          text not null,
  created_at         timestamptz not null default now(),
  updated_at         timestamptz not null default now(),
  unique (source, source_id)
);
create index if not exists work_items_client_status on public.work_items (client_id, status);
create index if not exists work_items_doer on public.work_items (doer_id, status);

create table if not exists public.work_items_internal (
  work_item_id   uuid primary key references public.work_items(id) on delete cascade,
  notes          text,
  minutes_spent  int,
  agent_cost_eur numeric(8,2),
  risk           text
);

create table if not exists public.work_dependencies (
  blocker_id uuid not null references public.work_items(id) on delete cascade,
  blocked_id uuid not null references public.work_items(id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (blocker_id, blocked_id),
  check (blocker_id <> blocked_id)
);

-- ---------- agent runs, evidence, outcomes ----------
create table if not exists public.work_agent_runs (
  id           uuid primary key default gen_random_uuid(),
  client_id    uuid references public.clients(id) on delete cascade,
  work_item_id uuid references public.work_items(id) on delete set null,
  agent_id     uuid not null references public.work_actors(id),
  delegated_by uuid references public.work_actors(id),
  state        text not null default 'running' check (state in ('running','needs_input','needs_approval','stale','finished','failed')),
  summary      text,
  session_ref  text,                               -- chat id or run folder
  started_at   timestamptz not null default now(),
  ended_at     timestamptz,
  cost_eur     numeric(8,2),
  source       text not null,
  source_id    text not null,
  unique (source, source_id)
);

create table if not exists public.work_evidence (
  id           uuid primary key default gen_random_uuid(),
  client_id    uuid references public.clients(id) on delete cascade,
  work_item_id uuid references public.work_items(id) on delete cascade,
  run_id       uuid references public.work_agent_runs(id) on delete cascade,
  outcome_id   uuid,                               -- fk added below
  kind         text not null check (kind in ('page','file','drive','screenshot','report','run','chat','commit','portal')),
  relation     text not null check (relation in ('used','produced','proves')),
  label        text not null,
  url          text,
  captured_at  timestamptz not null default now(),
  content_hash text,
  visibility   text not null default 'internal' check (visibility in ('internal','client')),
  created_by   uuid references public.work_actors(id),
  unique (work_item_id, label, relation)
);

create table if not exists public.work_outcomes (
  id           uuid primary key default gen_random_uuid(),
  client_id    uuid not null references public.clients(id) on delete cascade,
  work_item_id uuid references public.work_items(id) on delete set null,
  goal_id      uuid references public.work_goals(id) on delete set null,
  client_text  text not null,                      -- result in client words
  metric_key   text,
  value_before text,
  value_after  text,
  measured_at  date,
  confidence   text not null default 'assumed' check (confidence in ('confirmed','assumed')),
  verified_by  uuid references public.work_actors(id),
  minutes_spent int,
  cost_eur     numeric(8,2),
  visibility   text not null default 'internal' check (visibility in ('internal','client')),
  source       text not null,
  source_id    text not null,
  created_at   timestamptz not null default now(),
  unique (source, source_id)
);
alter table public.work_evidence drop constraint if exists work_evidence_outcome_fk;
alter table public.work_evidence add constraint work_evidence_outcome_fk foreign key (outcome_id) references public.work_outcomes(id) on delete cascade;

-- ---------- append-only history ----------
create table if not exists public.work_events (
  id              bigint generated always as identity primary key,
  client_id       uuid references public.clients(id) on delete cascade,
  work_item_id    uuid references public.work_items(id) on delete cascade,
  actor_id        uuid references public.work_actors(id),
  type            text not null check (type in ('created','status','handoff','comment','proof','decision')),
  from_status     text,
  to_status       text,
  from_actor      uuid references public.work_actors(id),
  to_actor        uuid references public.work_actors(id),
  note            text,
  visibility      text not null default 'internal' check (visibility in ('internal','client')),
  idempotency_key text unique,
  at              timestamptz not null default now()
);
create index if not exists work_events_client_at on public.work_events (client_id, at desc);

-- ---------- triggers: rules R1, R2 and automatic history ----------
create or replace function public.work_items_guard()
returns trigger language plpgsql security definer set search_path = public as $$
declare v_kind text; v_vkind text;
begin
  select kind into v_kind from work_actors where id = new.accountable_id;
  if v_kind not in ('admin','team') then raise exception 'R1: accountable must be a person (admin/team), not %', v_kind; end if;
  if new.status = 'waiting' and new.waiting_on is null then raise exception 'waiting needs waiting_on'; end if;
  if new.status <> 'waiting' then new.waiting_on := null; end if;
  if new.status = 'done' and (tg_op = 'INSERT' or old.status <> 'done') then
    if new.verified_by is null then raise exception 'R2: done needs verified_by (a person)'; end if;
    select kind into v_vkind from work_actors where id = new.verified_by;
    if v_vkind not in ('admin','team') then raise exception 'R2: only a person can verify'; end if;
    if tg_op = 'UPDATE' and not exists (select 1 from work_evidence e where e.work_item_id = new.id and e.relation in ('proves','produced')) then
      raise exception 'R2: done needs proof (evidence relation proves/produced)';
    end if;
    new.done_at := coalesce(new.done_at, now()); new.verified_at := coalesce(new.verified_at, now());
    new.resolution := coalesce(new.resolution, 'completed');
  end if;
  new.updated_at := now();
  return new;
end $$;
drop trigger if exists work_items_guard on public.work_items;
create trigger work_items_guard before insert or update on public.work_items for each row execute function public.work_items_guard();

-- done on INSERT: proof must arrive in the same transaction (deferred check)
create or replace function public.work_items_done_proof_check()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  if new.status = 'done' and not exists (select 1 from work_evidence e where e.work_item_id = new.id and e.relation in ('proves','produced')) then
    raise exception 'R2: done needs proof (evidence relation proves/produced)';
  end if;
  return null;
end $$;
drop trigger if exists work_items_done_proof_check on public.work_items;
create constraint trigger work_items_done_proof_check after insert on public.work_items
  deferrable initially deferred for each row execute function public.work_items_done_proof_check();

create or replace function public.work_items_log()
returns trigger language plpgsql security definer set search_path = public as $$
declare v_actor uuid;
begin
  select id into v_actor from work_actors where user_id = auth.uid() limit 1;
  if tg_op = 'INSERT' then
    insert into work_events (client_id, work_item_id, actor_id, type, to_status, to_actor, note)
    values (new.client_id, new.id, v_actor, 'created', new.status, new.doer_id, new.source || ':' || new.source_id);
  else
    if new.status is distinct from old.status then
      insert into work_events (client_id, work_item_id, actor_id, type, from_status, to_status, note)
      values (new.client_id, new.id, v_actor, 'status', old.status, new.status, new.status_reason);
    end if;
    if new.doer_id is distinct from old.doer_id then
      insert into work_events (client_id, work_item_id, actor_id, type, from_actor, to_actor, note)
      values (new.client_id, new.id, v_actor, 'handoff', old.doer_id, new.doer_id, new.next_action);
    end if;
  end if;
  return null;
end $$;
drop trigger if exists work_items_log on public.work_items;
create trigger work_items_log after insert or update on public.work_items for each row execute function public.work_items_log();

revoke all on function public.work_items_guard() from public, anon, authenticated;
revoke all on function public.work_items_done_proof_check() from public, anon, authenticated;
revoke all on function public.work_items_log() from public, anon, authenticated;

-- ---------- R5: automatic client colour ----------
-- red:    an open blocker, an item overdue by more than 7 days, or a wait of more than 14 days that blocks another item
--         (calibrated 13.10.: old unticked access grants made 7 of 9 clients red; plain waits now count as yellow)
-- yellow: overdue, waiting on someone for more than 3 days, items that need a check, or intake unsorted for more than 7 days
-- no_data: no open item and no event in the last 14 days
-- green:  everything else
create or replace view public.work_client_health with (security_invoker = true) as
with open_items as (
  select i.*, (current_date - i.created_at::date) as age_days,
         case when i.status in ('waiting','intake') then (current_date - coalesce(i.since, (select max(e.at)::date from work_events e where e.work_item_id = i.id and e.to_status = i.status), i.created_at::date)) end as wait_days
  from work_items i where i.status not in ('done','dropped') and i.client_id is not null
), scored as (
  select o.*,
    case when o.priority = 'blocker' then 3
         when o.due_on is not null and o.due_on < current_date - 7 then 3
         when o.status = 'waiting' and o.wait_days > 14 and exists (select 1 from work_dependencies d where d.blocker_id = o.id) then 3
         when o.due_on is not null and o.due_on < current_date then 2
         when o.status = 'waiting' and o.wait_days > 3 then 2
         when o.status = 'needs_check' then 2
         when o.status = 'intake' and o.wait_days > 7 then 2
         else 1 end as score,
    case when o.priority = 'blocker' then 'Blocker'
         when o.due_on is not null and o.due_on < current_date then 'Überfällig seit ' || (current_date - o.due_on) || ' Tagen'
         when o.status = 'waiting' then 'Wartet auf ' || o.waiting_on || ' seit ' || coalesce(o.wait_days, 0) || ' Tagen'
         when o.status = 'needs_check' then 'Wartet auf Prüfung'
         when o.status = 'intake' then 'Ungesichtet seit ' || coalesce(o.wait_days, 0) || ' Tagen'
         else 'Im Plan' end as signal
  from open_items o
), worst as (
  select distinct on (client_id) client_id, score, signal, title, next_action, accountable_id, doer_id, id as item_id
  from scored order by client_id, score desc, due_on nulls last, created_at
)
select c.id as client_id, c.name,
  case when w.client_id is null and not exists (select 1 from work_events e where e.client_id = c.id and e.at > now() - interval '14 days') then 'no_data'
       when w.score = 3 then 'red' when w.score = 2 then 'yellow' else 'green' end as band,
  coalesce(w.signal || ': ' || w.title, 'Keine offenen Aufgaben erfasst') as reason,
  w.next_action, w.accountable_id, w.doer_id, w.item_id,
  (select count(*) from scored s where s.client_id = c.id) as open_items,
  (select count(*) from scored s where s.client_id = c.id and s.status = 'waiting' and s.waiting_on = 'client') as waiting_on_client,
  (select count(*) from scored s where s.client_id = c.id and s.status = 'needs_check') as needs_check,
  (select max(e.at) from work_events e where e.client_id = c.id) as last_event
from clients c left join worst w on w.client_id = c.id
where c.status <> 'archived';

-- ---------- RLS (step 1: admin writes, delivery reads; team + client policies come with steps 2 and 3) ----------
do $$ declare t text; begin
  foreach t in array array['work_actors','work_goals','work_phases','work_items','work_items_internal','work_dependencies','work_agent_runs','work_evidence','work_outcomes','work_events'] loop
    execute format('alter table public.%I enable row level security', t);
    execute format('drop policy if exists "admin all" on public.%I', t);
    execute format('drop policy if exists "delivery read" on public.%I', t);
    execute format('create policy "delivery read" on public.%I for select to authenticated using (is_delivery())', t);
    if t = 'work_events' then
      -- append-only: admin may read and insert, never update or delete
      execute 'create policy "admin read" on public.work_events for select to authenticated using (is_admin())';
      execute 'create policy "admin insert" on public.work_events for insert to authenticated with check (is_admin())';
    else
      execute format('create policy "admin all" on public.%I for all to authenticated using (is_admin()) with check (is_admin())', t);
    end if;
  end loop;
end $$;
revoke all on public.work_client_health from anon;

commit;
