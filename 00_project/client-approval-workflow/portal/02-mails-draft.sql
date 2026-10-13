-- Kunden-Freigabe-Workflow · Mails + Tag-7-Regel · ENTWURF, NICHT AKTIV
-- Stand 2026-10-13. Erst nach 01-migration.sql und nur nach Martins ausdrücklichem Go anwenden.
-- Selbst nach dem Anwenden versendet nichts, solange:
--   (a) kein pg_cron-Job angelegt ist (Block ganz unten ist auskommentiert) und
--   (b) client_approval_settings.digest_enabled = false ist (Standard).
-- Versandregeln: Absender portal@741.studio, reply_to + BCC IMMER martin@741.studio, max. 1 Mail pro Kunde und Tag.
-- Texte: mail-digest-text.txt und mail-reminder-text.txt (Slop-Check 5/5). Du-Form, Signatur nur "Martin".
-- Englisch (13.10.): Kunden mit clients.lang <> 'de' bekommen mail-digest-text-en.txt / mail-reminder-text-en.txt (Slop-Check 5/5).
-- OFFEN für Martin: Hard Rule "E-Mails nur über Airmailer" vs. automatischer Portal-Versand über Resend (wie die Wochenmail).

begin;

-- ---------------------------------------------------------------------------
-- Tag-7-Regel: Empfehlung gilt als freigegeben
--   nur mit schriftlicher Zustimmung (auto_approve_consent)
--   nie bei aktiv-Ja-Pflicht (Preis, Gesundheit, Behandlung, Recht → must_active_yes)
--   immer mit Protokolleintrag kind = 'auto_7d'
-- ---------------------------------------------------------------------------
create or replace function public.approval_apply_day7()
returns int language plpgsql security definer set search_path = public as $$
declare it approval_items; n int := 0;
begin
  for it in
    select i.* from approval_items i
    join client_approval_settings s on s.client_id = i.client_id
    where i.status = 'open' and i.due_at <= now()
      and s.auto_approve_consent and not i.must_active_yes and i.risk_class = 'none'
    for update of i
  loop
    update approval_items set status = 'ready', chosen_key = it.recommended_key, decided_kind = 'auto_7d'
    where id = it.id;
    insert into approval_decisions (client_id, item_id, item_version, actor_user, actor_name, kind, action, variant_key, variant_value, note)
    values (it.client_id, it.id, it.version, null, 'automatisch', 'auto_7d', 'approve', it.recommended_key,
            approval_variant_value(it, it.recommended_key), 'Frist ' || to_char(it.due_at at time zone 'Europe/Berlin', 'DD.MM.') || ' abgelaufen, Zustimmung liegt vor');
    n := n + 1;
  end loop;
  return n;
end $$;

-- ---------------------------------------------------------------------------
-- Mail bauen (nur Text, sendet nichts). Gibt null zurück, wenn es nichts Neues gibt.
-- Neue Punkte seit der letzten Mail → Sammel-Mail. Sonst Punkte mit erreichtem Tag 3 → Erinnerung.
-- ---------------------------------------------------------------------------
create or replace function public.approval_build_mail(p_client uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare s client_approval_settings; c clients; v_new int; v_rem int; v_li text; v_kind text; v_subject text; v_body text;
        v_first text; v_due text; v_url text := 'https://clients.741.studio/?view=decisions';
        v_en boolean; v_fmt text;
begin
  select * into s from client_approval_settings where client_id = p_client;
  select * into c from clients where id = p_client;
  v_en := coalesce(c.lang, 'de') <> 'de';                        -- jede Sprache außer Deutsch → Englisch
  v_fmt := case when v_en then 'FMDD Mon' else 'DD.MM.' end;     -- 20 Oct / 20.10.
  -- Teamnamen ("Bali Healing Team") und Titel ("Dr. Test") bleiben ganz, sonst nur der Vorname (wie apFirst im Portal)
  v_first := coalesce(case when coalesce(s.approver_name, c.contact_person) ~* '\mteam\M|^(Dr\.|Prof\.)' then coalesce(s.approver_name, c.contact_person)
                           else split_part(coalesce(s.approver_name, c.contact_person), ' ', 1) end, '');

  select count(*) into v_new from approval_items
   where client_id = p_client and status = 'open' and released_at > coalesce(s.last_digest_at, '-infinity');
  select count(*) into v_rem from approval_items
   where client_id = p_client and status = 'open' and remind_at <= now()
     and remind_at > coalesce(s.last_digest_at, '-infinity');
  if v_new = 0 and v_rem = 0 then return null; end if;          -- nichts Neues → keine Mail

  v_kind := case when v_new > 0 then 'digest' else 'reminder' end;
  select string_agg('<li style="margin:6px 0">' || title ||
           case when must_active_yes then case when v_en then ' (I need your yes here)' else ' (hier brauche ich dein Ja)' end
                when v_kind = 'digest' then case when v_en then ' (by ' else ' (bis ' end || to_char(due_at at time zone 'Europe/Berlin', v_fmt) || ')' else '' end ||
           '</li>', '' order by must_active_yes desc, due_at),
         to_char(min(due_at) filter (where not must_active_yes) at time zone 'Europe/Berlin', v_fmt)
    into v_li, v_due
    from (select * from approval_items where client_id = p_client and status = 'open'
            and (v_kind = 'digest' and released_at > coalesce(s.last_digest_at, '-infinity')
              or v_kind = 'reminder' and remind_at <= now())
          order by must_active_yes desc, due_at limit 5) x;

  if v_en then
    if v_kind = 'digest' then
      v_subject := v_new || case when v_new = 1 then ' item is' else ' items are' end || ' waiting for your decision';
      v_body := '<p>Hi ' || v_first || ',</p><p>there ' || case when v_new = 1 then 'is one new item' else 'are ' || v_new || ' new items' end ||
        ' for your website and your Google profile in the portal:</p><ul>' || v_li || '</ul>' ||
        '<p>For each item I marked what I recommend and why, so you do not have to search. One click is enough.</p>';
    else
      v_subject := 'Reminder: ' || v_rem || case when v_rem = 1 then ' item' else ' items' end || ' open' || coalesce(' until ' || v_due, '');
      v_body := '<p>Hi ' || v_first || ',</p><p>' || case when v_rem = 1 then 'one item' else v_rem || ' items' end ||
        ' in the portal ' || case when v_rem = 1 then 'is' else 'are' end || ' still waiting for you:</p><ul>' || v_li || '</ul>' ||
        case when v_due is null then ''
             when s.auto_approve_consent then '<p>The deadline is ' || v_due || '. After that my recommendation counts as approved, as we agreed in the contract. You can still change it until it goes live.</p>'
             else '<p>The deadline is ' || v_due || '. Without your decision these items stay open, and we cannot continue with this part of the work until then.</p>' end;
    end if;
  elsif v_kind = 'digest' then
    v_subject := v_new || case when v_new = 1 then ' Punkt wartet' else ' Punkte warten' end || ' auf deine Entscheidung';
    v_body := '<p>Hallo ' || v_first || ',</p><p>im Portal liegen ' || v_new ||
      case when v_new = 1 then ' neuer Punkt' else ' neue Punkte' end || ' für deine Website und dein Google-Profil:</p><ul>' || v_li || '</ul>' ||
      '<p>Bei jedem Punkt habe ich markiert, was ich dir empfehle und warum, damit du nicht lange suchen musst. Ein Klick genügt.</p>';
  else
    v_subject := 'Erinnerung: ' || v_rem || case when v_rem = 1 then ' Punkt' else ' Punkte' end || ' offen' ||
      coalesce(' bis ' || v_due, '');
    v_body := '<p>Hallo ' || v_first || ',</p><p>' || case when v_rem = 1 then 'ein Punkt wartet' else v_rem || ' Punkte warten' end ||
      ' im Portal noch auf dich:</p><ul>' || v_li || '</ul>' ||
      case when v_due is null then ''
           when s.auto_approve_consent then '<p>Die Frist endet am ' || v_due || '. Danach gilt meine Empfehlung als freigegeben, so wie wir es im Vertrag vereinbart haben, und du kannst sie bis zum Livegang trotzdem noch ändern.</p>'
           else '<p>Die Frist endet am ' || v_due || '. Ohne deine Entscheidung bleiben diese Punkte offen, und wir können an diesen Stellen erst einmal nicht weiterarbeiten.</p>' end;
  end if;
  v_body := '<div style="font-family:Arial,sans-serif;font-size:15px;line-height:1.55;max-width:560px;color:#252525">' || v_body ||
    '<p><a href="' || v_url || '" style="display:inline-block;background:#252525;color:#fff;text-decoration:none;font-weight:700;padding:11px 18px;border-radius:9px">' ||
    case when v_en then 'Decide now' else 'Jetzt entscheiden' end || '</a></p>' ||
    case when v_en then '<p>Best regards<br>Martin</p></div>' else '<p>Herzliche Grüße<br>Martin</p></div>' end;
  return jsonb_build_object('kind', v_kind, 'to', c.contact_email, 'subject', v_subject, 'html', v_body);
end $$;

-- ---------------------------------------------------------------------------
-- Versand (nur Kunden mit digest_enabled = true, max. 1 pro Tag, zur Mittagszeit Berlin)
-- ---------------------------------------------------------------------------
create or replace function public.approval_send_mails()
returns int language plpgsql security definer set search_path = public as $$
declare r record; m jsonb; v_key text; v_cfg mail_config; n int := 0;
begin
  select value into v_key from app_secrets where key = 'resend_api_key';
  select * into v_cfg from mail_config where id = 1;
  for r in select * from client_approval_settings
           where digest_enabled
             and extract(hour from now() at time zone 'Europe/Berlin') = digest_hour_berlin
             and (last_digest_at is null or (last_digest_at at time zone 'Europe/Berlin')::date < (now() at time zone 'Europe/Berlin')::date)
  loop
    m := approval_build_mail(r.client_id);
    continue when m is null or coalesce(m->>'to', '') = '';
    perform net.http_post(
      url := 'https://api.resend.com/emails',
      headers := jsonb_build_object('Authorization', 'Bearer ' || v_key, 'Content-Type', 'application/json'),
      body := jsonb_build_object(
        'from', 'Martin · 741 Studio <' || v_cfg.from_email || '>',
        'to', array[m->>'to'],
        'bcc', array['martin@741.studio'],          -- Martin IMMER in BCC
        'reply_to', 'martin@741.studio',
        'subject', m->>'subject',
        'html', m->>'html'));
    update client_approval_settings set last_digest_at = now() where client_id = r.client_id;
    insert into emails_log (client_id, template, subject, status)
    values (r.client_id, 'approval_' || (m->>'kind'), m->>'subject', 'queued');
    n := n + 1;
  end loop;
  return n;
end $$;

revoke all on function public.approval_apply_day7()     from public, anon, authenticated;
revoke all on function public.approval_build_mail(uuid) from public, anon, authenticated;
revoke all on function public.approval_send_mails()     from public, anon, authenticated;

commit;

-- ---------------------------------------------------------------------------
-- AKTIVIERUNG — NUR nach Martins Go, pro Kunde einzeln:
--   update client_approval_settings set digest_enabled = true where client_id = '<id>';
--   select cron.schedule('approval-hourly', '5 * * * *', $$select public.approval_apply_day7(); select public.approval_send_mails();$$);
-- Vorschau ohne Versand:
--   select public.approval_build_mail('<client_id>');
-- ---------------------------------------------------------------------------
