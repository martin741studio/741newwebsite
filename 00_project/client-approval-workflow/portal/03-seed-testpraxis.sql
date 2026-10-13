-- Testkunde "Testpraxis Musterstadt" (801531ce-d861-42cc-aafb-e976c8c00634) mit den 5 Beispiel-Elementen aus dem Prototyp.
-- Stand 2026-10-13 · NUR nach Martins Go und NACH 01-migration.sql anwenden. Suriya erst nach eigenem Go.
-- Die Inhalte sind Beispieldaten aus dem Prototyp (Content-Pool 11.10., Live-Abgleich 13.10.), nur zum Testen.

begin;

insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('801531ce-d861-42cc-aafb-e976c8c00634', 'd00d9d21-8dd4-4a7f-a7a7-4bb6b12f2e15', 'Dr. Test', false, true)
on conflict (client_id) do update set approver_user_id = excluded.approver_user_id, approver_name = excluded.approver_name,
  health_client = excluded.health_client;

delete from public.approval_items where client_id = '801531ce-d861-42cc-aafb-e976c8c00634';

with ins as (
insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class,
   hwg_checked, hwg_checked_at, hwg_checked_by, status, released_at, remind_at, due_at)
values
 ('801531ce-d861-42cc-aafb-e976c8c00634','E1','price','Preis','website',
  'Preis für eine Einzelsitzung Schmerztherapie',
  'Auf deiner Website stehen für dieselbe Sitzung **80 €, 85 € und 95 €**. Ein Preis überall schafft Vertrauen.',
  'Abgleich deiner Website', '2026-10-13',
  '[{"key":"A","value":"95 €","label":"steht so auf /ganzheitliche-schmerztherapie/"},
    {"key":"B","value":"85 €","label":"steht als Überschrift auf /nacken-schulter/"}]', 'A',
  null, null, false, null, '{}',
  'Gilt dann auf allen Seiten: Schmerztherapie, Nacken & Schulter, Kosten & Abrechnung.',
  'Hier brauche ich dein Ja. Für dieselbe Sitzung stehen auf deiner Website drei verschiedene Preise.',
  'price', true, now(), 'Martin (Testdaten)', 'open', '2026-10-13 03:00+02', '2026-10-16 08:00+02', '2026-10-20 08:00+02'),

 ('801531ce-d861-42cc-aafb-e976c8c00634','E2','text','Text','website',
  'Überschrift der Seite „Massage in Ingelheim“',
  '**„massage ingelheim“ wird 480-mal im Monat gesucht.** Massage bringt 58 % deiner Sichtbarkeit bei Google. Das Keyword bleibt, die Formulierung wählst du.',
  'Google-Suchdaten und Sichtbarkeits-Messung', '2026-10-11',
  '[{"key":"A","value":"{kw} – Ayurveda, Rücken & Nervenregulation","label":"nennt drei deiner Massage-Arten"},
    {"key":"B","value":"{kw} – Zeit, in der dein Körper loslassen darf","label":"gefühlvoller"},
    {"key":"C","value":"{kw}","label":"bleibt wie bisher"}]', 'A',
  'Massage in Ingelheim', 'Massage in Ingelheim', true, null, '{}', null,
  'Das gelbe Schloss bleibt stehen, weil genau danach gesucht wird. Den Rest des Satzes wählst du.',
  'none', true, now(), 'Martin (Testdaten)', 'open', '2026-10-13 03:00+02', '2026-10-16 08:00+02', '2026-10-20 08:00+02'),

 ('801531ce-d861-42cc-aafb-e976c8c00634','E3','design','Design','website',
  'Anruf-Button: wo soll er stehen?',
  '**7 von 11 Praxen in deiner Umgebung** haben einen Knopf, der direkt anruft. Auf deiner Seite steht die Nummer nur als Text.',
  'Vergleich mit 11 Praxen in deiner Umgebung', '2026-10-11',
  '[{"key":"A","value":"Im Kopf der Seite","label":"immer oben sichtbar","design":"head"},
    {"key":"B","value":"Leiste unten am Handy","label":"nur auf dem Handy","design":"sticky"}]', 'A',
  null, null, false, null, '{"hero":"Naturheilpraxis in Ingelheim für Migräne & Nervensystem","cta":"Termin vereinbaren"}', null, null,
  'none', true, now(), 'Martin (Testdaten)', 'open', '2026-10-13 03:00+02', '2026-10-16 08:00+02', '2026-10-20 08:00+02'),

 ('801531ce-d861-42cc-aafb-e976c8c00634','E4','gbp','Google-Profil','gbp',
  'Leistung im Google-Profil umbenennen',
  'Die Migräne-Analyse und die SURIYA Cranio-Neuro-Analyse werden auf der Website **eine Seite**. Das Profil soll dasselbe zeigen.',
  'Abgleich Website und Google-Profil', '2026-10-13',
  '[{"key":"A","value":"„Migräne-Analyse“ → „SURIYA Cranio-Neuro-Analyse“","label":"ein Name, wie auf der Website"},
    {"key":"B","value":"Beide Leistungen behalten","label":"zwei Einträge im Profil"}]', 'A',
  null, null, false,
  'Hauptkategorie „Heilpraktiker/in“, Name, Adresse und Website-Link ändert nur 741. Sie haben die größte Wirkung auf dein Ranking.',
  '{}', null, null,
  'none', true, now(), 'Martin (Testdaten)', 'open', '2026-10-13 03:00+02', '2026-10-16 08:00+02', '2026-10-20 08:00+02'),

 ('801531ce-d861-42cc-aafb-e976c8c00634','E5','node','Seitenbaum','website',
  'Neuer Ratgeber: „Vagusnerv und Nervensystem beruhigen“',
  '**„nervensystem beruhigen“ wird 6.600-mal im Monat gesucht.** Ein Ratgeber beantwortet die Fragen und verweist auf deine Seite „Nervensystem & Vagusnerv“.',
  'Google-Suchdaten', '2026-10-11',
  '[{"key":"A","value":"Ja, das passt zu mir – ich liefere 3–5 Fragen meiner Patientinnen"},
    {"key":"B","value":"Ja, aber schreibt ihr den Entwurf, ich prüfe"},
    {"key":"C","value":"Nein, das ist nicht mein Thema"}]', 'A',
  null, null, false, null, '{"node":"/ratgeber/vagusnerv-nervensystem-beruhigen/","node_kind":"Wissen / Ratgeber"}', null, null,
  'health', true, now(), 'Martin (Testdaten)', 'open', '2026-10-13 03:00+02', '2026-10-16 08:00+02', '2026-10-20 08:00+02')
returning id, client_id, version)
insert into public.approval_decisions (client_id, item_id, item_version, actor_name, kind, action, created_at)
select client_id, id, version, 'Martin', 'admin', 'released', '2026-10-13 03:00+02' from ins;

commit;
