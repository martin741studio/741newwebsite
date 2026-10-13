create temp table t_res(n serial, test text, ok boolean, info text);
grant all on t_res to authenticated; grant all on sequence t_res_n_seq to authenticated;
-- foreign item for Suriya (open)
insert into approval_items (client_id, kind, type_label, title, why, why_source, why_date, variants, recommended_key, status)
values ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649','other','Test','FREMD','x','x','2026-10-13','[{"key":"A","value":"a"},{"key":"B","value":"b"}]','A','open');
-- draft for test client
insert into approval_items (client_id, kind, type_label, title, why, why_source, why_date, variants, recommended_key, status)
values ('801531ce-d861-42cc-aafb-e976c8c00634','other','Test','ENTWURF','x','x','2026-10-13','[{"key":"A","value":"a"},{"key":"B","value":"b"}]','A','draft');
-- risk forces active yes
insert into t_res(test, ok, info) select 'risk_class price/health => must_active_yes', bool_and(must_active_yes), string_agg(code,',') from approval_items where risk_class<>'none';
-- health gate
do $$ begin
  insert into approval_items (client_id, kind, type_label, title, why, why_source, why_date, variants, recommended_key, status, hwg_checked)
  values ('801531ce-d861-42cc-aafb-e976c8c00634','other','Test','OHNE HWG','x','x','2026-10-13','[{"key":"A","value":"a"},{"key":"B","value":"b"}]','A','open', false);
  insert into t_res(test, ok, info) values ('HWG gate blocks release', false, 'inserted!');
exception when others then insert into t_res(test, ok, info) values ('HWG gate blocks release', true, sqlerrm); end $$;

-- ===== as client Dr. Test =====
set local role authenticated;
select set_config('request.jwt.claims', '{"sub":"d00d9d21-8dd4-4a7f-a7a7-4bb6b12f2e15","role":"authenticated"}', true);
insert into t_res(test, ok, info) select 'client sees only own released items (expect 5)', count(*)=5, count(*)::text||' / '||string_agg(coalesce(code,title),',') from approval_items;
insert into t_res(test, ok, info) select 'client sees own settings only', count(*)=1, count(*)::text from client_approval_settings;
do $$ declare n int; begin update approval_items set title='HACK' where true; get diagnostics n = row_count;
  insert into t_res(test, ok, info) values ('client direct UPDATE blocked', n=0, n||' rows'); end $$;
do $$ begin insert into approval_decisions (client_id, actor_name, kind, action) values ('801531ce-d861-42cc-aafb-e976c8c00634','x','client','approve');
  insert into t_res(test, ok, info) values ('client direct INSERT log blocked', false, 'inserted!');
exception when others then insert into t_res(test, ok, info) values ('client direct INSERT log blocked', true, sqlerrm); end $$;
do $$ begin insert into approval_items (client_id, kind, type_label, title, why, why_source, why_date, variants, recommended_key) values ('801531ce-d861-42cc-aafb-e976c8c00634','other','x','x','x','x','2026-10-13','[{"key":"A","value":"a"},{"key":"B","value":"b"}]','A');
  insert into t_res(test, ok, info) values ('client cannot create items', false, 'inserted!');
exception when others then insert into t_res(test, ok, info) values ('client cannot create items', true, sqlerrm); end $$;
do $$ declare r approval_items; begin select * into r from approval_decide((select id from approval_items where code='E1'),'approve','A',null);
  insert into t_res(test, ok, info) values ('client approves E1 (A)', r.status='ready', r.status||' '||r.chosen_key);
exception when others then insert into t_res(test, ok, info) values ('client approves E1 (A)', false, sqlerrm); end $$;
do $$ declare r approval_items; begin select * into r from approval_decide((select id from approval_items where code='E2'),'approve_with_change','B','Bitte ohne Gedankenstrich');
  insert into t_res(test, ok, info) values ('client approve_with_change E2', r.status='ready', r.status||' '||r.chosen_key||' '||r.chosen_note);
exception when others then insert into t_res(test, ok, info) values ('client approve_with_change E2', false, sqlerrm); end $$;
do $$ begin perform approval_decide((select id from approval_items where code='E3'),'request_change','A',null);
  insert into t_res(test, ok, info) values ('request_change needs note', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('request_change needs note', true, sqlerrm); end $$;
do $$ begin perform approval_go((select id from approval_items where code='E1'));
  insert into t_res(test, ok, info) values ('client cannot give Go', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('client cannot give Go', true, sqlerrm); end $$;
reset role;
do $$ declare v uuid; begin select id into v from approval_items where title='FREMD';
  execute 'set local role authenticated';
  perform approval_decide(v,'approve','A',null);
  execute 'reset role';
  insert into t_res(test, ok, info) values ('client cannot decide other client item', false, 'accepted!');
exception when others then execute 'reset role'; insert into t_res(test, ok, info) values ('client cannot decide other client item', true, sqlerrm); end $$;
set local role authenticated;
insert into t_res(test, ok, info) select 'client log shows own entries only', bool_and(client_id='801531ce-d861-42cc-aafb-e976c8c00634'), count(*)::text||' rows' from approval_decisions;
-- ===== as admin Martin =====
select set_config('request.jwt.claims', '{"sub":"7d908ccf-629f-48b4-b439-dc3215d5ff3f","role":"authenticated"}', true);
insert into t_res(test, ok, info) select 'admin sees all items incl. draft/foreign', count(*)=7, count(*)::text from approval_items;
do $$ declare r approval_items; begin select * into r from approval_go((select id from approval_items where code='E1'));
  insert into t_res(test, ok, info) values ('admin Go on E1', r.status='go', r.status||' by '||r.go_by);
exception when others then insert into t_res(test, ok, info) values ('admin Go on E1', false, sqlerrm); end $$;
do $$ begin perform approval_go((select id from approval_items where code='E3'));
  insert into t_res(test, ok, info) values ('Go only for ready items', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('Go only for ready items', true, sqlerrm); end $$;
do $$ begin update approval_items set why='neu' where code='E1';
  insert into t_res(test, ok, info) values ('edit after Go blocked', false, 'accepted!');
exception when others then insert into t_res(test, ok, info) values ('edit after Go blocked', true, sqlerrm); end $$;
do $$ declare r approval_items; begin update approval_items set why=why||' (neu)' where code='E2' returning * into r;
  insert into t_res(test, ok, info) values ('content edit => new version, decision reset', r.version=2 and r.status='open' and r.chosen_key is null, 'v'||r.version||' '||r.status);
exception when others then insert into t_res(test, ok, info) values ('content edit => new version, decision reset', false, sqlerrm); end $$;
do $$ begin update approval_decisions set note='x' where true; delete from approval_decisions where true;
  insert into t_res(test, ok, info) values ('log is append-only (admin)', (select count(*) from approval_decisions where note='x')=0, 'no rows changed'); end $$;
insert into t_res(test, ok, info) select 'log kinds', true, string_agg(distinct kind||'/'||action, ', ') from approval_decisions;
reset role;
select n, ok, test, info from t_res order by n;
