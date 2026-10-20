-- Kamil Böyük (cc5ad406-d06d-4b5a-a33c-3386b9e3de60): 4 decisions as DRAFT for the portal decision module.
-- NOT EXECUTED. The main session inserts after Martin's review. Status draft = the client sees nothing.
-- Client facts: lang de, mode 'reports', health client (HWG applies), two WordPress sites:
--   Physio Anatomie GmbH = physiotherapieoberhausen.com (Oberhausen)   |   Physiotherapie Kraft = physiotherapiekraft.de (Gelsenkirchen, Hausbesuche)
-- Voice: card text to Kamil in "du" (as in the 13.10. draft report). Website copy inside the variants uses "Sie" or neutral wording, like the live sites.
-- Facts checked 13.10.2026:
--   Live sites (curl 13.10.): Anatomie title "Physio Anatomie – Individuelle Physiotherapie"; /leistungen/ H1 "Unsere Therapien in Oberhausen sind das Nonplusultra
--     der Krankengymnastik / Physiotherapie!"; Startseite H1 "Experten für Physiotherapie und Krankengymnastik in Oberhausen, Altenheim, Bottrop Mülheim an der Ruhr
--     und Duisburg. Schmerzfrei bewegen & Mobilität zurückgewinnen! Hausbesuche möglich".
--     Kraft /leistungen/hausbesuche/ and /uber-uns/: placeholder quotes, "Physio Pathologie", Lorem ipsum, "Dr. James Anderson, D.C. – Chief Chiropractor" and two more Dr. placeholders.
--   Visit data (GA4 property 468424260, split by hostName, 1 Sep - 12 Oct 2026, read 13.10.):
--     Anatomie 1,229 visits: /leistungen 918, / 201, organic search 107. Kraft: /leistungen/hausbesuche 427.
--   Services named in the Anatomie variants all stand on the live /leistungen/ page: Krankengymnastik, Manuelle Therapie, Manuelle Lymphdrainage, Hausbesuch auf Anfrage.
--   Address Marktstraße 163-165, 46045 Oberhausen stands on the live /profil/ page.
-- Keyword demand (search volume) is NOT used: no saved data for these terms and no paid pull allowed. The why lines use visit counts only.
-- HWG: no healing promise in any variant. hwg_checked stays false until Martin's check. risk_class health/legal = active yes needed (no 7-day rule).
-- No tool names, no prices, no deadlines. Slop check (deslop_de.py) 5/5 on all client text.
-- OPEN BEFORE RELEASE: approver. A client profile exists (user_id 1384d5b2-4e9d-4912-86d9-296fd893717c, display_name 'Kamil Böyük', role client).
--   The brief says leave approver_user_id NULL. Main session: after Martin's yes run
--   update public.client_approval_settings set approver_user_id = '1384d5b2-4e9d-4912-86d9-296fd893717c' where client_id = 'cc5ad406-d06d-4b5a-a33c-3386b9e3de60';
-- Website changes behind these cards need Martin's per-change go (no program, no tasks, no access grants for Kamil in the portal).

begin;

insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('cc5ad406-d06d-4b5a-a33c-3386b9e3de60', null, 'Kamil Böyük', false, true)
on conflict (client_id) do nothing;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('cc5ad406-d06d-4b5a-a33c-3386b9e3de60','E1','other','Inhalt','website',
  'Platzhalter-Texte auf physiotherapiekraft.de entfernen?',
  'Auf deiner Kraft-Website stehen noch **Platzhalter mit fremdem Praxisnamen, Blindtext und ein Team mit Dr.-Titeln**, und die Hausbesuche-Seite bekam in sechs Wochen **427 Besuche**.',
  'Abgleich deiner Website und Besuchsdaten (1. Sep – 12. Okt 2026)', '2026-10-13',
  '[{"key":"A","value":"Platzhalter entfernen","label":"Stimmen und Team verschwinden, echte Angaben setzen wir ein, sobald du sie schickst"},
    {"key":"B","value":"Entfernen und „Über uns“ neu schreiben","label":"du schickst mir Namen, Qualifikation und Foto deines Teams"},
    {"key":"C","value":"So lassen","label":"die Platzhalter bleiben sichtbar"}]', 'A',
  null, null, false, null, '{"page":"/leistungen/hausbesuche/","also":"/uber-uns/","site":"physiotherapiekraft.de"}',
  'Auf der Hausbesuche-Seite stehen Platzhalter-Patientenstimmen mit dem Namen „Physio Pathologie“, auf „Über uns“ ein Platzhalter-Team. Stimmen mit Heilaussagen und Titel ohne echte Person sind in der Gesundheitswerbung heikel.',
  'Hier brauche ich dein Ja. Diese Platzhalter gehören nicht auf eine Praxis-Website.',
  'legal', 'draft'),

 ('cc5ad406-d06d-4b5a-a33c-3386b9e3de60','E2','text','Text','website',
  'Überschrift der Seite „Leistungen“ bei Physio Anatomie',
  'Eine Spitzenaussage wie „Nonplusultra“ lässt sich in der Gesundheitswerbung kaum belegen, und genau auf dieser Seite landen **918 von 1.229 Besuchen** (75 %).',
  'Besuchsdaten deiner Website (1. Sep – 12. Okt 2026)', '2026-10-12',
  '[{"key":"A","value":"{kw}: Krankengymnastik, Manuelle Therapie und Lymphdrainage","label":"nennt drei deiner Leistungen"},
    {"key":"B","value":"{kw} – persönliche Behandlung in der Praxis, Hausbesuch auf Anfrage","label":"betont Praxis und Hausbesuch auf Anfrage"},
    {"key":"C","value":"{kw} bei Physio Anatomie","label":"kurz, ohne Aufzählung"}]', 'A',
  'Unsere Therapien in Oberhausen sind das Nonplusultra der Krankengymnastik / Physiotherapie!',
  'Physiotherapie in Oberhausen', true, null, '{"page":"/leistungen/","site":"physiotherapieoberhausen.com"}',
  'Weitere Aussagen auf der Seite, zum Beispiel „heilend bei Schmerzen“, sind ein eigener nächster Punkt.',
  'Der Ort und das Wort „Physiotherapie“ bleiben stehen, damit Google die Seite deiner Stadt zuordnet. Den Rest wählst du.',
  'health', 'draft'),

 ('cc5ad406-d06d-4b5a-a33c-3386b9e3de60','E3','text','Text','website',
  'Titel der Startseite bei Physio Anatomie',
  'Der Titel nennt keinen Ort, und nur **107 von 1.229 Besuchen** (9 %) kamen über die Google-Suche.',
  'Besuchsdaten deiner Website (1. Sep – 12. Okt 2026)', '2026-10-12',
  '[{"key":"A","value":"{kw} | Physio Anatomie","label":"kurz, Ort steht vorn"},
    {"key":"B","value":"Physio Anatomie: {kw} und Krankengymnastik","label":"nennt zwei Leistungen"},
    {"key":"C","value":"{kw} – individuelle Therapie | Physio Anatomie","label":"behält das Wort „individuell“ vom bisherigen Titel"}]', 'A',
  'Physio Anatomie – Individuelle Physiotherapie',
  'Physiotherapie in Oberhausen', true, null, '{"page":"/","element":"Seitentitel","site":"physiotherapieoberhausen.com"}',
  'Das ist der blaue Titel, den Google in den Suchergebnissen zeigt.',
  'Das Schloss bleibt auf dem Ort und auf „Physiotherapie“. Den Rest des Titels wählst du.',
  'none', 'draft'),

 ('cc5ad406-d06d-4b5a-a33c-3386b9e3de60','E4','text','Text','website',
  'Hauptüberschrift der Startseite von Physio Anatomie',
  'Die Überschrift verspricht „Schmerzfrei bewegen“, ein Erfolgsversprechen ist in der Gesundheitswerbung heikel, und die Startseite bekam in sechs Wochen **201 Besuche**.',
  'Besuchsdaten deiner Website (1. Sep – 12. Okt 2026)', '2026-10-12',
  '[{"key":"A","value":"{kw} und Krankengymnastik – auch in Bottrop, Mülheim an der Ruhr und Duisburg. Hausbesuche möglich","label":"wie bisher, ohne das Versprechen"},
    {"key":"B","value":"{kw}: Krankengymnastik, Manuelle Therapie und Lymphdrainage. Hausbesuche möglich","label":"nennt drei Leistungen"},
    {"key":"C","value":"{kw} – Hausbesuche möglich","label":"kurz"}]', 'A',
  'Experten für Physiotherapie und Krankengymnastik in Oberhausen, Altenheim, Bottrop Mülheim an der Ruhr und Duisburg. Schmerzfrei bewegen & Mobilität zurückgewinnen! Hausbesuche möglich',
  'Physiotherapie in Oberhausen', true, null, '{"page":"/","element":"H1","site":"physiotherapieoberhausen.com"}',
  '„Altenheim“ steht in der Ortsliste, ist aber kein Ort. Bietest du Altenheim-Besuche an, nehmen wir sie als eigenen Satz auf.',
  'Ort und „Physiotherapie“ bleiben stehen, das Versprechen fällt weg.',
  'health', 'draft');

commit;
