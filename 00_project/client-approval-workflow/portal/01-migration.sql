-- Kunden-Freigabe-Workflow · Migration für Supabase 741-portal (galjmtozcgxcwtzkzbpi)
-- Stand 2026-10-13 · Entwurf · NUR nach Martins Go anwenden.
-- Quelle der Regeln: 00_project/client-approval-workflow/brief.md + client-approval-library (01–04)
--
-- Inhalt:
--   1. client_approval_settings  (ein Entscheider pro Kunde, Zustimmung 7-Tage-Regel, Gesundheitskunde)
--   2. approval_items            (Elemente mit Varianten, Empfehlung, Schloss, aktives-Ja-Pflicht, Frist)
--   3. approval_decisions        (Protokoll: Person, Zeit, Version, Art, nur anhängen)
--   4. Trigger: aktives Ja bei Preis/Gesundheit/Behandlung/Recht, HWG-Sperre, neue Version, Sperre nach Go
--   5. RPCs: approval_decide, approval_undo (Kunde) · approval_release, approval_go (nur Admin)
--   6. RLS: Kunde sieht/entscheidet nur eigene, freigegebene Elemente; nur Admin legt an und gibt Go
--
-- Kein Mailversand, kein Cron in dieser Datei. Mails + Tag-7-Regel liegen als Entwurf in 02-mails-draft.sql.

begin;

-- ---------------------------------------------------------------------------
-- 1. Kunden-Einstellungen
-- ---------------------------------------------------------------------------
create table if not exists public.client_approval_settings (
  client_id            uuid primary key references public.clients(id) on delete cascade,
  approver_user_id     uuid references auth.users(id) on delete set null,   -- EIN Entscheider
  approver_name        text,
  auto_approve_consent boolean not null default false,                       -- 7-Tage-Regel nur mit schriftlicher Zustimmung
  consent_at           timestamptz,
  consent_source       text,                                                 -- z. B. "Vertrag § 4" oder "Portal-Onboarding 13.10."
  health_client        boolean not null default false,                       -- HWG-Prüfung vor Freigabe an den Kunden
  digest_enabled       boolean not null default false,                       -- Sammel-Mail: bleibt AUS bis Martins Go
  digest_hour_berlin   int not null default 12 check (digest_hour_berlin between 6 and 20),
  last_digest_at       timestamptz,
  updated_at           timestamptz not null default now()
);

-- ---------------------------------------------------------------------------
-- 2. Elemente
-- ---------------------------------------------------------------------------
create table if not exists public.approval_items (
  id              uuid primary key default gen_random_uuid(),
  client_id       uuid not null references public.clients(id) on delete cascade,
  code            text,                                   -- z. B. "E1", nur Anzeige
  kind            text not null check (kind in ('price','text','design','gbp','node','other')),
  type_label      text not null,                          -- "Preis", "Text", "Design", "Google-Profil", "Seitenbaum"
  area            text not null default 'website' check (area in ('website','gbp')),
  title           text not null,
  why             text not null,                          -- eine Zeile, **fett** erlaubt, echte Daten
  why_source      text not null,                          -- Quelle in Kundensprache, keine Tool-Namen
  why_date        date not null,                          -- Stand der Daten
  variants        jsonb not null,                         -- [{key,value,label,design}] 2–3 Stück
  recommended_key text not null,                          -- "741 empfiehlt"
  before_value    text,                                   -- "Jetzt live" (Text-Elemente)
  keyword         text,                                   -- Keyword unter SEO-Schloss
  seo_lock        boolean not null default false,
  lock_note       text,                                   -- z. B. Felder, die nur 741 ändert
  context         jsonb not null default '{}'::jsonb,     -- z. B. {"node":"/ratgeber/…","node_kind":"Wissen / Ratgeber","hero":"…"}
  note            text,
  guide_text      text,                                   -- Sprechblase Martin (Ich-Form, du, max. 2 Sätze)
  risk_class      text not null default 'none' check (risk_class in ('none','price','health','treatment','legal')),
  must_active_yes boolean not null default false,
  hwg_checked     boolean not null default false,
  hwg_checked_at  timestamptz,
  hwg_checked_by  text,
  status          text not null default 'draft'
                  check (status in ('draft','open','ready','change','go','withdrawn')),
  -- draft = nur 741 sieht es · open = wartet auf Kunde · ready = bereit für live
  -- change = Kunde wünscht Änderung · go = Martins Go für live, gesperrt · withdrawn = zurückgezogen
  chosen_key      text,
  chosen_note     text,
  decided_kind    text check (decided_kind in ('client','auto_7d')),
  version         int not null default 1,
  released_at     timestamptz,
  remind_at       timestamptz,                            -- Tag 3
  due_at          timestamptz,                            -- Tag 7
  go_at           timestamptz,
  go_by           text,
  created_by      uuid default auth.uid(),
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now(),
  constraint approval_items_variants_count check (jsonb_typeof(variants) = 'array' and jsonb_array_length(variants) between 2 and 3)
);
create index if not exists approval_items_client_status on public.approval_items (client_id, status);

-- ---------------------------------------------------------------------------
-- 3. Protokoll (nur anhängen)
-- ---------------------------------------------------------------------------
create table if not exists public.approval_decisions (
  id            uuid primary key default gen_random_uuid(),
  client_id     uuid not null references public.clients(id) on delete cascade,
  item_id       uuid references public.approval_items(id) on delete cascade,   -- null = Einstellung
  item_version  int,
  actor_user    uuid default auth.uid(),
  actor_name    text not null,
  kind          text not null check (kind in ('client','auto_7d','admin_go','admin')),
  -- client = Kunde · auto_7d = automatisch nach 7 Tagen · admin_go = 741-Go · admin = 741-Schritt
  action        text not null check (action in ('approve','approve_with_change','request_change','undo',
                                                'released','new_version','go','withdrawn','consent_on','consent_off')),
  variant_key   text,
  variant_value text,                                     -- Kopie des Werts zum Zeitpunkt der Entscheidung
  note          text,
  created_at    timestamptz not null default now()
);
create index if not exists approval_decisions_client on public.approval_decisions (client_id, created_at desc);

-- ---------------------------------------------------------------------------
-- 4. Hilfsfunktionen + Trigger
-- ---------------------------------------------------------------------------
create or replace function public.approval_variant_value(p_item public.approval_items, p_key text)
returns text language sql immutable set search_path = public as $$
  select replace(v->>'value', '{kw}', coalesce(p_item.keyword, ''))
  from jsonb_array_elements(p_item.variants) v where v->>'key' = p_key limit 1
$$;

create or replace function public.approval_items_guard()
returns trigger language plpgsql security definer set search_path = public as $$
declare v_health boolean;
begin
  -- Empfehlung muss eine der Varianten sein
  if not exists (select 1 from jsonb_array_elements(new.variants) v where v->>'key' = new.recommended_key) then
    raise exception 'recommended_key % ist keine Variante', new.recommended_key;
  end if;
  -- Preis, Gesundheit, Behandlung, Recht: immer aktives Ja (nie Tag-7-Regel)
  if new.risk_class <> 'none' then new.must_active_yes := true; end if;
  -- SEO-Schloss braucht ein Keyword
  if new.seo_lock and coalesce(new.keyword, '') = '' then
    raise exception 'SEO-Schloss ohne Keyword';
  end if;
  -- HWG-Prüfung vor Freigabe an einen Gesundheitskunden
  select health_client into v_health from client_approval_settings where client_id = new.client_id;
  if coalesce(v_health, false) and new.status <> 'draft' and not new.hwg_checked then
    raise exception 'HWG-Prüfung fehlt: Element bleibt Entwurf';
  end if;

  if tg_op = 'UPDATE' then
    -- Inhalt geändert?
    if (new.title, new.why, new.variants, new.recommended_key, new.before_value, new.keyword, new.context)
       is distinct from
       (old.title, old.why, old.variants, old.recommended_key, old.before_value, old.keyword, old.context) then
      if old.status = 'go' then
        raise exception 'Nach dem Go gesperrt. Eine spätere Änderung ist ein neues Element.';
      end if;
      if old.status <> 'draft' then
        -- neue Version: alte Entscheidung gilt nicht mehr, neue Frist
        new.version     := old.version + 1;
        new.status      := 'open';
        new.chosen_key  := null; new.chosen_note := null; new.decided_kind := null;
        new.released_at := now();
        new.remind_at   := now() + interval '3 days';
        new.due_at      := now() + interval '7 days';
        insert into approval_decisions (client_id, item_id, item_version, actor_name, kind, action, note)
        values (new.client_id, new.id, new.version,
                coalesce((select display_name from profiles where user_id = auth.uid()), '741'),
                'admin', 'new_version', 'Neue Version, Entscheidung zurückgesetzt');
      end if;
    end if;
  end if;
  new.updated_at := now();
  return new;
end $$;

drop trigger if exists approval_items_guard on public.approval_items;
create trigger approval_items_guard before insert or update on public.approval_items
  for each row execute function public.approval_items_guard();

create or replace function public.approval_settings_log()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  if tg_op = 'INSERT' and new.auto_approve_consent
     or tg_op = 'UPDATE' and new.auto_approve_consent is distinct from old.auto_approve_consent then
    insert into approval_decisions (client_id, actor_name, kind, action, note)
    values (new.client_id, coalesce((select display_name from profiles where user_id = auth.uid()), '741'),
            'admin', case when new.auto_approve_consent then 'consent_on' else 'consent_off' end,
            new.consent_source);
    if new.auto_approve_consent then new.consent_at := coalesce(new.consent_at, now()); else new.consent_at := null; end if;
  end if;
  new.updated_at := now();
  return new;
end $$;

drop trigger if exists approval_settings_log on public.client_approval_settings;
create trigger approval_settings_log before insert or update on public.client_approval_settings
  for each row execute function public.approval_settings_log();

-- ---------------------------------------------------------------------------
-- 5. RPCs
-- ---------------------------------------------------------------------------
-- Kunde entscheidet (nur der benannte Entscheider, nur eigene, offene Elemente)
create or replace function public.approval_decide(p_item uuid, p_action text, p_variant text, p_note text default null)
returns public.approval_items language plpgsql security definer set search_path = public as $$
declare it approval_items; v_prof profiles; v_set client_approval_settings; v_note text := nullif(trim(coalesce(p_note, '')), '');
begin
  select * into v_prof from profiles where user_id = auth.uid();
  if v_prof is null or v_prof.role <> 'client' then raise exception 'Nur der Kunde entscheidet'; end if;
  select * into it from approval_items where id = p_item for update;
  if it is null or it.client_id <> v_prof.client_id then raise exception 'Element nicht gefunden'; end if;
  if it.status not in ('open','ready','change') then raise exception 'Element ist nicht offen (%)', it.status; end if;
  select * into v_set from client_approval_settings where client_id = it.client_id;
  if v_set.approver_user_id is null or v_set.approver_user_id <> auth.uid() then
    raise exception 'Entscheiden kann nur die benannte Person';
  end if;
  if p_action not in ('approve','approve_with_change','request_change') then raise exception 'Unbekannte Aktion'; end if;
  if p_action <> 'request_change' and approval_variant_value(it, p_variant) is null then raise exception 'Unbekannte Variante'; end if;
  if p_action in ('approve_with_change','request_change') and v_note is null then raise exception 'Bitte kurz beschreiben, was anders sein soll'; end if;

  update approval_items set
    status = case when p_action = 'request_change' then 'change' else 'ready' end,
    chosen_key = case when p_action = 'request_change' then null else p_variant end,
    chosen_note = v_note,
    decided_kind = case when p_action = 'request_change' then null else 'client' end
  where id = p_item returning * into it;

  insert into approval_decisions (client_id, item_id, item_version, actor_name, kind, action, variant_key, variant_value, note)
  values (it.client_id, it.id, it.version, coalesce(v_prof.display_name, 'Kunde'), 'client', p_action,
          case when p_action = 'request_change' then null else p_variant end,
          case when p_action = 'request_change' then null else approval_variant_value(it, p_variant) end, v_note);

  -- vorhandene 741-Benachrichtigungs-Warteschlange (versendet nur, wenn deren Cron läuft)
  insert into admin_notifications (client_id, event)
  values (it.client_id, 'Entscheidung: ' || it.title || ' → ' ||
          case p_action when 'approve' then 'freigegeben' when 'approve_with_change' then 'freigegeben mit Änderung' else 'Änderung gewünscht' end);
  return it;
end $$;

-- Kunde nimmt Entscheidung zurück (bis zum Go)
create or replace function public.approval_undo(p_item uuid)
returns public.approval_items language plpgsql security definer set search_path = public as $$
declare it approval_items; v_prof profiles; v_set client_approval_settings;
begin
  select * into v_prof from profiles where user_id = auth.uid();
  if v_prof is null or v_prof.role <> 'client' then raise exception 'Nur der Kunde'; end if;
  select * into it from approval_items where id = p_item for update;
  if it is null or it.client_id <> v_prof.client_id then raise exception 'Element nicht gefunden'; end if;
  if it.status not in ('ready','change') then raise exception 'Nichts zurückzunehmen (%)', it.status; end if;
  select * into v_set from client_approval_settings where client_id = it.client_id;
  if v_set.approver_user_id is distinct from auth.uid() then raise exception 'Entscheiden kann nur die benannte Person'; end if;
  update approval_items set status = 'open', chosen_key = null, chosen_note = null, decided_kind = null
  where id = p_item returning * into it;
  insert into approval_decisions (client_id, item_id, item_version, actor_name, kind, action)
  values (it.client_id, it.id, it.version, coalesce(v_prof.display_name, 'Kunde'), 'client', 'undo');
  return it;
end $$;

-- 741 gibt ein Element an den Kunden frei (setzt Frist: Erinnerung Tag 3, Ende Tag 7)
create or replace function public.approval_release(p_item uuid)
returns public.approval_items language plpgsql security definer set search_path = public as $$
declare it approval_items;
begin
  if not is_admin() then raise exception 'Nur Admin'; end if;
  update approval_items set status = 'open', released_at = now(),
         remind_at = now() + interval '3 days', due_at = now() + interval '7 days'
  where id = p_item and status = 'draft' returning * into it;
  if it is null then raise exception 'Nur Entwürfe können freigegeben werden'; end if;
  insert into approval_decisions (client_id, item_id, item_version, actor_name, kind, action)
  values (it.client_id, it.id, it.version, coalesce((select display_name from profiles where user_id = auth.uid()), '741'), 'admin', 'released');
  return it;
end $$;

-- Martins Go für live (nur Admin, nur "bereit für live"); danach gesperrt
create or replace function public.approval_go(p_item uuid)
returns public.approval_items language plpgsql security definer set search_path = public as $$
declare it approval_items; v_name text;
begin
  if not is_admin() then raise exception 'Nur Admin gibt das Go'; end if;
  v_name := coalesce((select display_name from profiles where user_id = auth.uid()), '741');
  update approval_items set status = 'go', go_at = now(), go_by = v_name
  where id = p_item and status = 'ready' returning * into it;
  if it is null then raise exception 'Go nur für Elemente in "bereit für live"'; end if;
  insert into approval_decisions (client_id, item_id, item_version, actor_name, kind, action, variant_key, variant_value)
  values (it.client_id, it.id, it.version, v_name, 'admin_go', 'go', it.chosen_key, approval_variant_value(it, it.chosen_key));
  return it;
end $$;

revoke all on function public.approval_decide(uuid, text, text, text) from public, anon;
revoke all on function public.approval_undo(uuid)    from public, anon;
revoke all on function public.approval_release(uuid) from public, anon;
revoke all on function public.approval_go(uuid)      from public, anon;
grant execute on function public.approval_decide(uuid, text, text, text) to authenticated;
grant execute on function public.approval_undo(uuid)    to authenticated;
grant execute on function public.approval_release(uuid) to authenticated;
grant execute on function public.approval_go(uuid)      to authenticated;

-- ---------------------------------------------------------------------------
-- 6. RLS
-- ---------------------------------------------------------------------------
alter table public.client_approval_settings enable row level security;
alter table public.approval_items           enable row level security;
alter table public.approval_decisions       enable row level security;

-- Einstellungen: Kunde liest eigene · Admin schreibt · Delivery liest
drop policy if exists "cas read own"   on public.client_approval_settings;
drop policy if exists "cas admin all"  on public.client_approval_settings;
drop policy if exists "cas delivery read" on public.client_approval_settings;
create policy "cas read own"      on public.client_approval_settings for select using (client_id = my_client_id());
create policy "cas admin all"     on public.client_approval_settings for all    using (is_admin()) with check (is_admin());
create policy "cas delivery read" on public.client_approval_settings for select using (is_delivery());

-- Elemente: Kunde liest nur eigene, die 741 freigegeben hat (kein Entwurf, nicht zurückgezogen)
-- Kunde schreibt NIE direkt, nur über approval_decide / approval_undo
drop policy if exists "ai read own"      on public.approval_items;
drop policy if exists "ai admin all"     on public.approval_items;
drop policy if exists "ai delivery read" on public.approval_items;
create policy "ai read own"      on public.approval_items for select
  using (client_id = my_client_id() and status not in ('draft','withdrawn'));
create policy "ai admin all"     on public.approval_items for all using (is_admin()) with check (is_admin());
create policy "ai delivery read" on public.approval_items for select using (is_delivery());

-- Protokoll: lesen ja, schreiben nur über die Funktionen (keine insert/update/delete-Policy, auch nicht für Admin)
drop policy if exists "ad read own"      on public.approval_decisions;
drop policy if exists "ad admin read"    on public.approval_decisions;
create policy "ad read own"   on public.approval_decisions for select using (client_id = my_client_id());
create policy "ad admin read" on public.approval_decisions for select using (is_admin() or is_delivery());

commit;

-- Rückbau (nur falls nötig):
-- drop table public.approval_decisions, public.approval_items, public.client_approval_settings cascade;
-- drop function public.approval_decide(uuid,text,text,text), public.approval_undo(uuid), public.approval_release(uuid),
--   public.approval_go(uuid), public.approval_items_guard(), public.approval_settings_log(), public.approval_variant_value(public.approval_items,text);
