-- STÜRZL Steuerstrafrecht (b6f6e303-50e4-4afb-a343-337206cec316): 6 decision cards as DRAFT for the portal module "Entscheidungen".
-- Prepared 13.10.2026. NOT executed. Status draft = the client sees nothing. The main session inserts after Martin's grill review.
-- Language: German, du-form (Martin 12.10.2026: "Wir sind alle beim Du"). Text that goes on the website inside variants stays in Sie-form (live site voice).
-- Not a health client: no HWG. Law-firm advertising rules (BRAO 43b, BORA 6, UWG) apply: risk_class 'legal' where a card is about wording, categories or services of the firm. 'price' for the Erstberatung amount.
-- Facts checked 13.10.2026:
--   Live site (curl): start page title "Stürzl Steuerstrafrecht – Home", H1 "Kanzlei", no form, old address Wiesenhüttenstraße 17. Page "Kanzlei" says "Die Erstberatung erhalten Sie bei uns zum Festpreis" (no amount).
--   4 Selbstanzeige URLs return 200; 3 carry the same H1 "Selbstanzeigen: Ihre Chance auf Schutz ..."; /kosten/ and /compliance/ return 404 (new pages).
--   Google Maps (Chrome, public, 13.10.): Frankfurt "Rechtsanwalt" 5,0 / 14, old address; München "Rechtsanwalt" 5,0 / 1.
--   Search data: Google suchdaten 16 Monate bis 13.10.2026 (anwalt steuerstrafrecht frankfurt 3.600 Einblendungen, Pos. 8,6, 6 Klicks). Search volume "tax compliance" 590 (11.10.2026).
--   Category comparison of leading Frankfurt profiles: 09.10.2026 (analysis file stuerzl-wettbewerber-analyse-2026-10-09.md, source of truth tab 02 row 17).
--   Text overlap of the Selbstanzeige pages 74 % and 97 %: measurement 11.10.2026 (sitetree.json). Kostentext of the firm: file dated 09.10.2026.
--   anwalt.de 79 reviews: 09.10.2026.
-- Decisions NOT carried here (Martin decides first): Google Ads start time (no 741 recommendation allowed), wording of the firm's own live pages (OPEN-FLAGS A6).
-- E5 (Tax Compliance) was dropped by the main session on 13.10.2026: it may repeat a question of the 12.10. mail and asks the firm to claim a service. Old E6 is now E5, old E7 is now E6.
-- E3: recommended_key set to 'B' on 13.10.2026 after Martin's answer in the grill chat (relayed by the Morning Grill session). Reason line in the note: self-check B 38/44, A 37/44, not fully comparable. The INSERT below still shows 'A'; the DB row was updated.
-- Approver: no portal profile exists for this client yet (profiles = 0 rows). approver_user_id stays NULL, so the client cannot decide until a login exists.

begin;

insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('b6f6e303-50e4-4afb-a343-337206cec316', null, 'Dr. Anja Stürzl', false, false)
on conflict (client_id) do nothing;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('b6f6e303-50e4-4afb-a343-337206cec316','E1','text','Text','website',
  'Überschrift der Startseite',
  'Bei Google erschien deine Website in 16 Monaten **3.600-mal** für „anwalt steuerstrafrecht frankfurt“ (Position 8,6) und wurde nur **6-mal** angeklickt, heute heißt der Seitentitel „Home“ und die Überschrift „Kanzlei“.',
  'Google-Suchdaten deiner Website, 16 Monate bis 13.10.2026', '2026-10-13',
  '[{"key":"A","value":"{kw} und Wirtschaftsstrafrecht in Frankfurt und München","label":"nennt das Fachgebiet und beide Städte"},
    {"key":"B","value":"{kw}: Verteidigung im Steuerstrafverfahren in Frankfurt und München","label":"nennt, was ihr für Mandanten tut"},
    {"key":"C","value":"Wenn die Steuerfahndung ermittelt: {kw} in Frankfurt und München","label":"spricht den Akutfall an"}]', 'A',
  'Überschrift „Kanzlei“, Seitentitel mit dem Zusatz „Home“', 'Steuerstrafrecht', true,
  'Das Wort „Steuerstrafrecht“ bleibt in der Überschrift, weil genau danach gesucht wird. Den Seitentitel für Google setzt 741 passend dazu.',
  '{"page":"/"}',
  'Gilt für die Startseite in Entwurf A und in Entwurf B. Nichts geht live, bevor du hier entschieden hast.',
  'Das Wort „Steuerstrafrecht“ bleibt, weil genau danach gesucht wird. Den Rest der Überschrift wählst du.',
  'legal', 'draft'),

 ('b6f6e303-50e4-4afb-a343-337206cec316','E2','gbp','Google-Profil','gbp',
  'Kategorien in deinen Google-Profilen',
  'Die Profile, die in Google Maps vor dir stehen, führen **„Anwalt für Steuerrecht“ oder „Strafverteidiger“**, deine Profile in Frankfurt und München nur „Rechtsanwalt“.',
  'Vergleich der führenden Profile (09.10.2026) und deiner beiden Profile (13.10.2026)', '2026-10-09',
  '[{"key":"A","value":"„Anwalt für Steuerrecht“ und „Strafverteidiger“ ergänzen","label":"„Rechtsanwalt“ bleibt als weitere Kategorie, für Frankfurt und München"},
    {"key":"B","value":"Nur „Anwalt für Steuerrecht“ ergänzen","label":"ohne „Strafverteidiger“"},
    {"key":"C","value":"Keine Änderung","label":"nur „Rechtsanwalt“ wie heute"}]', 'A',
  null, null, false,
  'Hauptkategorie, Name, Adresse, Kartenposition und Website-Link ändert nur 741. Sie haben die größte Wirkung auf dein Ranking.',
  '{}',
  'Beim Münchner Profil klären wir vorher, wer dort Inhaber ist.',
  'Hier brauche ich dein Ja. Die Kategorie sagt Google, wofür ihr steht.',
  'legal', 'draft'),

 ('b6f6e303-50e4-4afb-a343-337206cec316','E3','design','Design','website',
  'Neue Startseite: Entwurf A, Entwurf B oder bestehende Seite',
  'Die heutige Startseite braucht **7,2 Sekunden** bis zum größten sichtbaren Element und hat kein Anfrage-Formular, beide Entwürfe haben ein Formular und einen Notfall-Streifen.',
  'Technik-Prüfung deiner Website (08.10.2026) und die beiden Entwürfe', '2026-10-08',
  '[{"key":"A","value":"Entwurf A: ruhig und klar","label":"sechs Leistungskarten, Foto rechts, Formular im dunklen Abschlussband"},
    {"key":"B","value":"Entwurf B: Briefbogen","label":"die Seite liest sich wie ein Brief der Kanzlei, mit Rückruf-Reiter"},
    {"key":"C","value":"Bestehende Seite behalten","label":"einzelne Elemente aus den Entwürfen übernehmen"}]', 'A',
  null, null, false, null,
  '{"page":"/"}',
  'Entwurf A: https://clients.741.studio/r/e006e37becd5/entwurf-a/ · Entwurf B: https://clients.741.studio/r/e006e37becd5/entwurf-b/',
  'Schau dir beide Entwürfe in Ruhe an. Beide sind für den Desktop fertig.',
  'none', 'draft'),

 ('b6f6e303-50e4-4afb-a343-337206cec316','E4','node','Seitenbaum','website',
  'Vier Selbstanzeige-Seiten zu einer zusammenführen?',
  'Auf deiner Website gibt es **vier Seiten zur Selbstanzeige**, drei davon mit derselben Überschrift und zwei mit **74 % und 97 %** gleichem Text.',
  'Textvergleich deiner Seiten (11.10.2026) und Prüfung der Live-Seiten (13.10.2026)', '2026-10-11',
  '[{"key":"A","value":"Zu einer Seite zusammenführen","label":"die alten Adressen leiten automatisch auf die neue Seite weiter"},
    {"key":"B","value":"Alle vier Seiten behalten","label":"jede bekommt einen eigenen Text"}]', 'A',
  null, null, false, null,
  '{"node":"/selbstanzeige/","node_kind":"Leistung"}',
  'Eigene Teile aus den bestehenden Seiten gehen in die neue Seite ein. Nichts wird gelöscht, ohne dass die alte Adresse weiterleitet.',
  null,
  'none', 'draft'),

 ('b6f6e303-50e4-4afb-a343-337206cec316','E5','price','Preis','website',
  'Preis der Erstberatung auf der Website',
  'Deine Seite „Kanzlei“ spricht von einem **Festpreis** ohne Betrag, dein neuer Kostentext von einer **Pauschale zwischen 250 und 350 Euro**.',
  'Deine Seite „Kanzlei“ (13.10.2026) und dein Kostentext (09.10.2026)', '2026-10-09',
  '[{"key":"A","value":"Für die Erstberatung berechnen wir üblicherweise eine Pauschale von 250 bis 350 Euro, je nach Zeit und Umfang.","label":"so steht es in deinem Kostentext"},
    {"key":"B","value":"Für die Erstberatung berechnen wir eine Pauschale. Die Höhe nennen wir Ihnen im ersten Gespräch.","label":"ohne Betrag auf der Seite"}]', 'A',
  '„Die Erstberatung erhalten Sie bei uns zum Festpreis.“', null, false, null,
  '{"page":"/kosten/"}',
  'Ob der Betrag mit oder ohne Umsatzsteuer gilt, schreibst du bitte ins Kommentarfeld.',
  'Hier brauche ich dein Ja. Auf deiner Seite stehen heute zwei verschiedene Aussagen zur Erstberatung.',
  'price', 'draft'),

 ('b6f6e303-50e4-4afb-a343-337206cec316','E6','other','Bewertungen','gbp',
  'Wie bittest du Mandanten um eine Google-Bewertung?',
  'Dein Frankfurter Google-Profil hat **14 Bewertungen**, dein Münchner **1** und dein Profil auf anwalt.de **79**.',
  'Deine Google-Profile (13.10.2026) und dein anwalt.de-Profil (09.10.2026)', '2026-10-13',
  '[{"key":"A","value":"Persönliche Bitte nach Abschluss des Mandats","label":"mit Link zum Profil und dem Hinweis, keine Falldetails zu schreiben"},
    {"key":"B","value":"Nur ein Link, keine direkte Bitte","label":"auf der Website und in der E-Mail-Signatur"},
    {"key":"C","value":"Nicht aktiv um Bewertungen bitten","label":"es bleibt bei dem, was von selbst kommt"}]', 'A',
  null, null, false, null,
  '{}',
  'Ohne Belohnung und ohne Falldetails. Wir schreiben nichts im Namen deiner Mandanten.',
  null,
  'legal', 'draft');

commit;
