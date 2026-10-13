-- Tests for 01-migration.sql + 02-seed.sql. Run inside one transaction that is rolled back (dry run).
create temp table t_res(n serial, test text, ok boolean, info text);
grant all on t_res to authenticated; grant all on sequence t_res_n_seq to authenticated;
insert into t_res(test, ok, info) select 'seed: actors', count(*) >= 20, count(*)::text from work_actors;
insert into t_res(test, ok, info) select 'seed: phases (7 per client)', count(*) = 63, count(*)::text from work_phases;
insert into t_res(test, ok, info) select 'seed: grill tasks', count(*) = 23, count(*)::text from work_items where source = 'grill';
insert into t_res(test, ok, info) select 'seed: client todos from access', count(*) > 0, count(*)::text from work_items where source = 'access';
insert into t_res(test, ok, info) select 'seed: intake from report feedback', count(*) = 5, string_agg(title, ' | ') from work_items where source = 'report_feedback';
insert into t_res(test, ok, info) select 'seed: no agent-done item is done', count(*) = 0, count(*)::text from work_items where status = 'done';
insert into t_res(test, ok, info) select 'history: created events', count(*) = (select count(*) from work_items), count(*)::text from work_events where type = 'created';
-- R1
do $$ begin
  insert into work_items (title, accountable_id, doer_id, source, source_id) values ('x', (select id from work_actors where name='Agent (Chat)'), (select id from work_actors where name='Agent (Chat)'), 'test', 'r1');
  insert into t_res(test, ok, info) values ('R1 agent cannot be accountable', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('R1 agent cannot be accountable', true, sqlerrm); end $$;
do $$ begin
  update work_items set status = 'waiting', waiting_on = null where source_id = '2026-10-13/t06';
  insert into t_res(test, ok, info) values ('waiting needs waiting_on', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('waiting needs waiting_on', true, sqlerrm); end $$;
-- R2
do $$ begin
  update work_items set status = 'done' where source_id = '2026-10-13/t13';
  insert into t_res(test, ok, info) values ('R2 done needs verified_by', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('R2 done needs verified_by', true, sqlerrm); end $$;
do $$ begin
  update work_items set status = 'done', verified_by = (select id from work_actors where name='Agent (Chat)') where source_id = '2026-10-13/t13';
  insert into t_res(test, ok, info) values ('R2 agent cannot verify', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('R2 agent cannot verify', true, sqlerrm); end $$;
do $$ begin
  update work_items set status = 'done', verified_by = (select id from work_actors where name='Martin') where source_id = '2026-10-13/t06';
  insert into t_res(test, ok, info) values ('R2 done needs proof', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('R2 done needs proof', true, sqlerrm); end $$;
do $$ declare r work_items; begin
  update work_items set status = 'done', verified_by = (select id from work_actors where name='Martin') where source_id = '2026-10-13/t13' returning * into r;
  insert into t_res(test, ok, info) values ('R2 done with proof + person works', r.status = 'done' and r.done_at is not null, r.status || ' ' || r.resolution);
exception when others then insert into t_res(test, ok, info) values ('R2 done with proof + person works', false, sqlerrm); end $$;
do $$ begin
  set constraints all immediate;
  insert into work_items (title, status, accountable_id, doer_id, verified_by, source, source_id) values ('x', 'done', (select id from work_actors where name='Martin'), (select id from work_actors where name='Martin'), (select id from work_actors where name='Martin'), 'test', 'r2-insert');
  insert into t_res(test, ok, info) values ('R2 insert as done without proof', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('R2 insert as done without proof', true, sqlerrm); end $$;
insert into t_res(test, ok, info) select 'history: status event written', count(*) >= 1, count(*)::text from work_events e join work_items i on i.id = e.work_item_id where i.source_id = '2026-10-13/t13' and e.type = 'status' and e.to_status = 'done';
-- R3 idempotency
insert into work_items (client_id, title, accountable_id, doer_id, source, source_id) values (null, 'again', (select id from work_actors where name='Martin'), (select id from work_actors where name='Martin'), 'grill', '2026-10-13/t01') on conflict (source, source_id) do nothing;
insert into t_res(test, ok, info) select 'R3 repeated producer write = no duplicate', count(*) = 1, count(*)::text from work_items where source = 'grill' and source_id = '2026-10-13/t01';
-- R5 health
insert into t_res(test, ok, info) select 'R5 health bands', count(*) >= 9, string_agg(name || '=' || band, ', ' order by name) from work_client_health where name not like 'Testpraxis%';
insert into t_res(test, ok, info) select 'R5 Bali red (blocker)', band = 'red', reason from work_client_health where name = 'Bali Healing';
-- RLS: client sees nothing, events append-only for admin
set local role authenticated;
select set_config('request.jwt.claims', '{"sub":"d0e5d993-246a-4079-9c9a-a7f5c6d76963","role":"authenticated"}', true);
insert into t_res(test, ok, info) select 'RLS client sees no work items (step 1)', count(*) = 0, count(*)::text from work_items;
insert into t_res(test, ok, info) select 'RLS client sees no health rows data', coalesce(sum(open_items), 0) = 0, coalesce(sum(open_items), 0)::text from work_client_health;
select set_config('request.jwt.claims', '{"sub":"7d908ccf-629f-48b4-b439-dc3215d5ff3f","role":"authenticated"}', true);
insert into t_res(test, ok, info) select 'RLS admin sees all items', count(*) = (select count(*) from work_items), count(*)::text from work_items;
do $$ declare n1 int; n2 int; begin
  update work_events set note = 'x' where true; get diagnostics n1 = row_count;
  delete from work_events where true; get diagnostics n2 = row_count;
  insert into t_res(test, ok, info) values ('R4 history append-only (admin)', n1 = 0 and n2 = 0, n1 || ' upd / ' || n2 || ' del'); end $$;
reset role;
