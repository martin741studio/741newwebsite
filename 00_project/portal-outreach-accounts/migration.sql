-- 741 portal (Supabase 741-portal, galjmtozcgxcwtzkzbpi) · area B "Outreach & Sales"
-- Outreach numbers per account (LinkedIn account the work comes from).
-- Status: APPLIED 13.10.2026 after Martin's go (migrations outreach_numbers_per_account + outreach_accounts_revoke_anon).
-- Decisions (Martin, 13.10.2026): account list + child rows · accepted = daily count per account ·
-- Gayo keeps the list · totals in daily_reports are auto-sums · 6 fields · plan targets per account.
-- RLS model stays: manager (Gayo, admin) = all; staff = own rows only; no link to area A (clients).

begin;

-- 1) Account list. client_label is free text on purpose: no FK to clients (area A),
--    so Gayo and staff never get a path into client data.
create table public.outreach_accounts (
  id           uuid primary key default gen_random_uuid(),
  label        text not null unique,          -- 'Peggy LinkedIn'
  client_label text,                          -- 'Bali Healing' (free text)
  kind         text not null default 'client' check (kind in ('client','741')),
  active       boolean not null default true,
  sort         int not null default 0,
  created_at   timestamptz not null default now()
);

-- 2) Which person works which account. Staff see only their assigned accounts.
create table public.outreach_account_members (
  account_id uuid not null references public.outreach_accounts(id) on delete cascade,
  member_id  uuid not null references public.team_members(id) on delete cascade,
  primary key (account_id, member_id)
);

-- 3) Evening report, one row per account. Deleted with the report ("Change" button).
create table public.daily_report_accounts (
  id            uuid primary key default gen_random_uuid(),
  report_id     uuid not null references public.daily_reports(id) on delete cascade,
  account_id    uuid not null references public.outreach_accounts(id),
  requests_sent int not null default 0 check (requests_sent >= 0),
  accepted      int not null default 0 check (accepted >= 0),
  pitched       int not null default 0 check (pitched >= 0),     -- first message to a new connection
  follow_ups    int not null default 0 check (follow_ups >= 0),
  replies       int not null default 0 check (replies >= 0),
  interested    int not null default 0 check (interested >= 0),
  unique (report_id, account_id)
);
create index on public.daily_report_accounts (account_id);

-- 4) Morning plan targets, one row per account.
create table public.daily_plan_accounts (
  id               uuid primary key default gen_random_uuid(),
  plan_id          uuid not null references public.daily_plans(id) on delete cascade,
  account_id       uuid not null references public.outreach_accounts(id),
  requests_target  int not null default 0 check (requests_target >= 0),
  messages_target  int not null default 0 check (messages_target >= 0),
  unique (plan_id, account_id)
);
create index on public.daily_plan_accounts (account_id);

-- 5) RLS
alter table public.outreach_accounts        enable row level security;
alter table public.outreach_account_members enable row level security;
alter table public.daily_report_accounts    enable row level security;
alter table public.daily_plan_accounts      enable row level security;

create policy oa_manager_all on public.outreach_accounts for all
  using (is_team_manager()) with check (is_team_manager());
create policy oa_staff_read on public.outreach_accounts for select
  using (exists (select 1 from public.outreach_account_members x
                 where x.account_id = outreach_accounts.id and x.member_id = my_team_member_id()));

create policy oam_manager_all on public.outreach_account_members for all
  using (is_team_manager()) with check (is_team_manager());
create policy oam_self_read on public.outreach_account_members for select
  using (member_id = my_team_member_id());

create policy dra_manager_all on public.daily_report_accounts for all
  using (is_team_manager()) with check (is_team_manager());
create policy dra_self_rw on public.daily_report_accounts for all
  using (exists (select 1 from public.daily_reports r
                 where r.id = report_id and r.member_id = my_team_member_id()))
  with check (exists (select 1 from public.daily_reports r
                      where r.id = report_id and r.member_id = my_team_member_id())
              and exists (select 1 from public.outreach_account_members x
                          where x.account_id = daily_report_accounts.account_id
                            and x.member_id = my_team_member_id()));

create policy dpa_manager_all on public.daily_plan_accounts for all
  using (is_team_manager()) with check (is_team_manager());
create policy dpa_self_rw on public.daily_plan_accounts for all
  using (exists (select 1 from public.daily_plans p
                 where p.id = plan_id and p.member_id = my_team_member_id()))
  with check (exists (select 1 from public.daily_plans p
                      where p.id = plan_id and p.member_id = my_team_member_id())
              and exists (select 1 from public.outreach_account_members x
                          where x.account_id = daily_plan_accounts.account_id
                            and x.member_id = my_team_member_id()));

-- 6) Auto-sum: account rows fill the old total fields, so board, history and team_period keep working.
--    messages_sent = pitched + follow_ups. connection_requests = {account label: requests_sent}.
--    Runs as the caller (no SECURITY DEFINER): RLS on daily_reports still applies.
create or replace function public.sync_report_totals() returns trigger
language plpgsql set search_path = public as $$
declare v_report uuid := coalesce(new.report_id, old.report_id);
begin
  update daily_reports r set
    messages_sent = coalesce(s.pitched,0) + coalesce(s.follow_ups,0),
    follow_ups    = coalesce(s.follow_ups,0),
    new_replies   = coalesce(s.replies,0),
    interested    = coalesce(s.interested,0),
    connection_requests = coalesce(s.conns,'{}'::jsonb)
  from (select sum(a.pitched) pitched, sum(a.follow_ups) follow_ups, sum(a.replies) replies,
               sum(a.interested) interested,
               jsonb_object_agg(o.label, a.requests_sent) filter (where a.requests_sent > 0) conns
        from daily_report_accounts a join outreach_accounts o on o.id = a.account_id
        where a.report_id = v_report) s
  where r.id = v_report;
  return null;
end $$;

create trigger daily_report_accounts_sync
  after insert or update or delete on public.daily_report_accounts
  for each row execute function public.sync_report_totals();

-- 7) Save in one call (report + account rows). Runs as the caller, so RLS decides.
--    p_fields: {hours_worked, progress, blockers, next_plan}
--    p_accounts: [{account_id, requests_sent, accepted, pitched, follow_ups, replies, interested}, ...]
create or replace function public.submit_daily_report(p_day date, p_fields jsonb, p_accounts jsonb)
returns uuid language plpgsql set search_path = public as $$
declare v_id uuid; v_member uuid := my_team_member_id();
begin
  if v_member is null then raise exception 'no team member'; end if;
  insert into daily_reports (member_id, day, hours_worked, progress, blockers, next_plan)
  values (v_member, p_day, nullif(p_fields->>'hours_worked','')::numeric,
          nullif(p_fields->>'progress',''), nullif(p_fields->>'blockers',''), nullif(p_fields->>'next_plan',''))
  returning id into v_id;
  insert into daily_report_accounts (report_id, account_id, requests_sent, accepted, pitched, follow_ups, replies, interested)
  select v_id, (a->>'account_id')::uuid,
         coalesce((a->>'requests_sent')::int,0), coalesce((a->>'accepted')::int,0),
         coalesce((a->>'pitched')::int,0),       coalesce((a->>'follow_ups')::int,0),
         coalesce((a->>'replies')::int,0),       coalesce((a->>'interested')::int,0)
  from jsonb_array_elements(coalesce(p_accounts,'[]'::jsonb)) a;
  return v_id;
end $$;

-- p_targets: [{account_id, requests_target, messages_target}, ...]
-- Old targets jsonb is filled too, so the old work card still shows a sum.
create or replace function public.submit_daily_plan(p_day date, p_intent text, p_targets jsonb)
returns uuid language plpgsql set search_path = public as $$
declare v_id uuid; v_member uuid := my_team_member_id();
begin
  if v_member is null then raise exception 'no team member'; end if;
  insert into daily_plans (member_id, day, intent, targets)
  select v_member, p_day, p_intent,
         jsonb_build_object(
           'messages', coalesce(sum((t->>'messages_target')::int),0),
           'connections', coalesce(jsonb_object_agg(o.label, (t->>'requests_target')::int)
                                   filter (where coalesce((t->>'requests_target')::int,0) > 0), '{}'::jsonb))
  from jsonb_array_elements(coalesce(p_targets,'[]'::jsonb)) t
  left join outreach_accounts o on o.id = (t->>'account_id')::uuid
  returning id into v_id;
  insert into daily_plan_accounts (plan_id, account_id, requests_target, messages_target)
  select v_id, (t->>'account_id')::uuid,
         coalesce((t->>'requests_target')::int,0), coalesce((t->>'messages_target')::int,0)
  from jsonb_array_elements(coalesce(p_targets,'[]'::jsonb)) t;
  return v_id;
end $$;

grant execute on function public.submit_daily_report(date, jsonb, jsonb) to authenticated;
grant execute on function public.submit_daily_plan(date, text, jsonb)    to authenticated;

-- 8) Period view per account (manager only). Answers "Bali: X sent, Y accepted, Z pitched".
create or replace function public.team_period_accounts(p_from date, p_to date)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare v jsonb;
begin
  if not is_team_manager() then raise exception 'team manager only'; end if;
  select coalesce(jsonb_agg(row_to_json(x)::jsonb order by x.kind, x.client_label nulls last, x.label), '[]'::jsonb)
  into v from (
    select o.id, o.label, o.client_label, o.kind,
           count(distinct a.day)               as days,
           coalesce(sum(a.requests_sent),0)    as requests_sent,
           coalesce(sum(a.accepted),0)         as accepted,
           coalesce(sum(a.pitched),0)          as pitched,
           coalesce(sum(a.follow_ups),0)       as follow_ups,
           coalesce(sum(a.replies),0)          as replies,
           coalesce(sum(a.interested),0)       as interested,
           round(100.0*sum(a.accepted)/nullif(sum(a.requests_sent),0),1)              as accept_rate,
           round(100.0*sum(a.replies)/nullif(sum(a.pitched)+sum(a.follow_ups),0),1)   as reply_rate,
           coalesce(jsonb_agg(distinct m.display_name) filter (where m.id is not null),'[]'::jsonb) as people
    from outreach_accounts o
    left join (select a.*, r.day, r.member_id
                 from daily_report_accounts a join daily_reports r on r.id = a.report_id
                where r.day between p_from and p_to) a on a.account_id = o.id
    left join team_members m on m.id = a.member_id
    where o.active or a.id is not null
    group by o.id
  ) x;
  return v;
end $$;

-- 9) Seed list (Martin 13.10.2026). Gayo corrects labels, clients and assignments in the portal.
insert into public.outreach_accounts (label, client_label, kind, sort) values
  ('Martin Hüwel LinkedIn',      'Praxis Hüwel',  'client', 10),
  ('Coralie LinkedIn',           'Praxis Suriya', 'client', 20),
  ('Felix Meinhardt LinkedIn',   'Felix Meinhardt','client', 30),
  ('Peggy LinkedIn',             'Bali Healing',  'client', 40),
  ('Celine LinkedIn',            'Celine',        'client', 50),
  ('741 Main LinkedIn',          '741 Studio',    '741',    60),
  ('741 Second LinkedIn',        '741 Studio',    '741',    70),
  ('741 Third LinkedIn',         '741 Studio',    '741',    80);

-- 10) Start assignments (from the reports up to 12.10.2026: Rias took over Bali Healing and works Celine).
--     Gayo corrects them in the portal.
insert into public.outreach_account_members (account_id, member_id)
select o.id, m.id from public.outreach_accounts o join public.team_members m
  on (m.display_name = 'Rias' and o.label in ('Peggy LinkedIn','Celine LinkedIn'))
  or (m.display_name = 'Gayo' and o.label not in ('Peggy LinkedIn','Celine LinkedIn'))
where m.active;

-- 11) Same as team_period: no anon access (second migration outreach_accounts_revoke_anon).
revoke execute on function public.team_period_accounts(date, date) from public, anon;
revoke execute on function public.submit_daily_report(date, jsonb, jsonb) from public, anon;
revoke execute on function public.submit_daily_plan(date, text, jsonb) from public, anon;
grant execute on function public.team_period_accounts(date, date) to authenticated;

commit;
