-- Praxis Hüwel (f0a6730f-8f56-4c61-8085-1955f3bb285a): 7 Entscheidungs-Karten E2-E8 als ENTWURF.
-- E1 (Datenschutz-Abschnitt Google Analytics) existiert schon, Status open. Nicht doppelt angelegt.
-- Geprüft am 13.10.2026 gegen Live-Website (curl), Hüwels Rückmeldungen vom 31.08.2026 (report_feedback),
-- Google-Suchdaten (90 Tage bis 09.10.) und Suchmengen (Stand 11.10.). Quellen je Karte:
--   E2 Startseite und /heilpraktiker-nürnberg.html zeigen dieselben 5 Erfahrungsberichte (Anita B., Axel C., Vera V., Susanne S., Barbara N.);
--      3 davon beschreiben einen Heilerfolg. Google-Profil: 10 Bewertungen, 4,9 (Local Falcon Lesezugriff 13.10.).
--   E3 Hüwel schrieb am 31.08.: wegen „Bioscan“ 2018 abgemahnt, eigene Umschreibung „computergestützte Regulations- und Belastungstestung“.
--      „Bioscan“ steht live im Titel oder in einer Überschrift von 4 Seiten (/bioscan.html, /methoden-als-werkzeuge/gesundheitscheck.html, /, /heilpraktiker-nürnberg.html).
--   E4 „heilpraktiker nürnberg“ 1.000/Monat (Suchmengen 11.10.). Startseite und /heilpraktiker-nürnberg.html haben je eigenen Canonical und fast gleichen Inhalt.
--      Search Console 90 Tage: 62 von 72 Klicks auf die Startseite, zweite Seite ohne Daten. Offene Frage aus dem Seitenbaum ST-01.
--   E5 „magnetfeldtherapie“ 9.900/Monat in Deutschland, „magnetfeldtherapie nürnberg“ 10 (Suchmengen 11.10.). Das Wort steht auf keiner Seite der Website (alle Sitemap-Seiten geprüft).
--      Live: H1 „Ondamed-Therapie (PEMF)“, Titel „Ondamed-Therapie (PEMF) Nürnberg | Praxis Hüwel“.
--   E6 Live-Texte der 5 Blog-Beiträge gelesen. Aussagen zu Beweis und Behandlung in „Hortensien-Homöopathie-Experiment“, „Homöopathie im Krankenhaus“, „Körper und Seele im Stillstand“.
--   E7 Video kElKa09l804 (52 Sekunden, 6 Aufrufe), Transkript am 13.10. gelesen. Auf der Startseite per Klick-Fassade eingebunden.
--   E8 Alte Seite „Schmerzen und Verletzungen“: 7 Klicks, 71 Einblendungen in 90 Tagen (zweitmeiste Klicks nach der Startseite), heute nur Weiterleitung auf einen Anker.
--      Hüwel am 31.08.: Weiterleitung sei „sicherlich nicht die Ideal-Lösung“. Entscheidung Martin 11.10.: Anliegen-Seiten gehen voran.
-- HWG: keine Heil- oder Erfolgsversprechen in den Karten. hwg_checked bleibt false. Martin prüft vor der Freigabe.
-- Aktives Ja: E2, E3, E6, E7 (legal), E5 (treatment), E8 (health). E4 ohne Risikoklasse.
-- Keine 7-Tage-Zustimmung, keine Mails, keine Preise.
--
-- WICHTIG vor dem Einspielen (siehe queue.md, Abschnitt Lücken):
--  1. Der Entscheider fehlt. approver_user_id bleibt hier NULL. Ohne ihn kann Hüwel nichts entscheiden, auch E1 nicht.
--     Kandidat im Portal: profiles.user_id 8a596070-1f02-4452-810d-4d3d738df1c7 ("Martin Hüwel", Rolle client). Martin bestätigt vorher.
--  2. Mit health_client = true blockiert der Guard-Trigger jede Änderung an E1 (Status open, hwg_checked false).
--     E1 muss vorher auf hwg_checked = true gesetzt werden, sonst schlägt approval_decide für E1 fehl.

begin;

insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('f0a6730f-8f56-4c61-8085-1955f3bb285a', null, 'Martin Hüwel', false, true)
on conflict (client_id) do nothing;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('f0a6730f-8f56-4c61-8085-1955f3bb285a','E2','text','Text','website',
  'Erfahrungsberichte auf der Startseite: welche bleiben?',
  '**3 von 5 Erfahrungsberichten auf deiner Startseite beschreiben einen Behandlungserfolg**, und solche Sätze können Mitbewerber abmahnen.',
  'Abgleich deiner Website (Startseite und „Heilpraktiker Nürnberg“)', '2026-10-13',
  '[{"key":"A","value":"Die 2 neutralen Berichte bleiben (Susanne S., Barbara N.). Die 3 mit Erfolgsaussage nehmen wir heraus.","label":"2 von 5 bleiben"},
    {"key":"B","value":"Alle 5 Berichte entfallen. Dort steht stattdessen deine Google-Bewertung: 4,9 von 5 Sternen bei 10 Bewertungen, mit Link zu Google.","label":"nur die Google-Bewertung"},
    {"key":"C","value":"Die 2 neutralen Berichte bleiben. Für die anderen 3 schicken Patientinnen und Patienten neue Berichte, die nur Ablauf und Atmosphäre beschreiben, mit schriftlicher Zustimmung.","label":"2 bleiben, 3 werden ersetzt"}]', 'A',
  'Anita B.: „… seitdem sind meine Beschwerden verschwunden.“ · Axel C.: „… meinen Heilungsprozess drastisch abgekürzt.“ · Vera V.: „Nachdem die Allgemeinmedizin versagt hatte, konnte mir hier endlich weitergeholfen werden.“ · Susanne S. · Barbara N.',
  null, false, null, '{"page":"/","also":"/heilpraktiker-nürnberg.html"}',
  'Gilt auf der Startseite und auf der Seite „Heilpraktiker Nürnberg“. Deine Bewertungen bei Google bleiben, wie sie sind. Die Texte sind rechtlich nicht geprüft.',
  'Das hier ist mir wichtig, deshalb brauche ich dein Ja. Nach der Abmahnung von 2018 möchte ich kein Risiko auf deiner Startseite lassen.',
  'legal', 'draft'),

 ('f0a6730f-8f56-4c61-8085-1955f3bb285a','E3','text','Text','website',
  'Messverfahren: „Bioscan“ oder deine eigene Bezeichnung?',
  '**Du hast am 31.08. geschrieben, dass du wegen des Begriffs „Bioscan“ 2018 abgemahnt wurdest**, und er steht heute in Titel oder Überschrift von 4 Seiten deiner Website.',
  'Deine Rückmeldung vom 31.08. und Abgleich deiner Website', '2026-10-13',
  '[{"key":"A","value":"Überall deine eigene Bezeichnung: „Gesundheitscheck mit computergestützter Regulations- und Belastungstestung“. Das Wort „Bioscan“ verschwindet aus Titeln, Überschriften und Menü.","label":"so, wie du es am 31.08. umschrieben hast"},
    {"key":"B","value":"„Bioscan“ steht nur noch einmal im Fließtext als Erklärung. Titel, Überschriften und Menü nutzen deine Bezeichnung.","label":"Begriff nur als Erklärung"},
    {"key":"C","value":"„Bioscan“ bleibt in Titeln, Überschriften und Menü wie jetzt.","label":"unverändert"}]', 'A',
  'Titel „Bioscan Nürnberg – 240 Parameter erklärt“ · Titel und Überschrift „Gesundheitscheck in Nürnberg (Bioscan)“ · Zwischenüberschrift „Gesundheitscheck mit Bioscan“ auf Startseite und „Heilpraktiker Nürnberg“',
  null, false, null, '{"page":"/bioscan.html","also":"/methoden-als-werkzeuge/gesundheitscheck.html"}',
  'Die Seite „Bioscan“ behält ihre Adresse, bis eine Weiterleitung steht. Die Texte sind rechtlich nicht geprüft.',
  'Du hast mir geschrieben, dass du bei „Bioscan“ vorsichtig bist. Deshalb frage ich dich, bevor wir die Seite ausbauen.',
  'legal', 'draft'),

 ('f0a6730f-8f56-4c61-8085-1955f3bb285a','E4','node','Seitenbaum','website',
  'Welche Seite steht für „Heilpraktiker Nürnberg“?',
  '**„heilpraktiker nürnberg“ wird 1.000-mal im Monat gesucht, und zwei sehr ähnliche Seiten deiner Website sind dafür gedacht**: die Startseite und „Heilpraktiker Nürnberg“.',
  'Google-Suchdaten und Abgleich deiner Website', '2026-10-11',
  '[{"key":"A","value":"Die Startseite ist die Hauptseite. „Heilpraktiker Nürnberg“ wird mit ihr zusammengeführt und leitet auf sie weiter.","label":"eine starke Seite"},
    {"key":"B","value":"Beide Seiten bleiben. „Heilpraktiker Nürnberg“ bekommt einen eigenen Schwerpunkt (Südstadt, Anfahrt, Ablauf). Die Startseite behält die Methoden.","label":"zwei Seiten, zwei Aufgaben"}]', 'A',
  null, null, false, null, '{"node":"/heilpraktiker-nürnberg.html","node_kind":"Standort / Startseite","keyword":"heilpraktiker nürnberg"}',
  'In den letzten 90 Tagen kamen 62 von 72 Klicks aus der Suche auf die Startseite. Für die zweite Seite liegen keine Suchdaten vor. Dein Text bleibt in beiden Fällen deiner.',
  null,
  'none', 'draft'),

 ('f0a6730f-8f56-4c61-8085-1955f3bb285a','E5','text','Text','website',
  'Überschrift der Seite „Ondamed-Therapie (PEMF)“',
  '**„Magnetfeldtherapie“ wird in Deutschland 9.900-mal im Monat gesucht, das Wort steht aber auf keiner Seite deiner Website**; dein Verfahren heißt dort nur „Ondamed“ und „PEMF“.',
  'Google-Suchdaten und Abgleich deiner Website', '2026-10-11',
  '[{"key":"A","value":"{kw} (PEMF) mit Ondamed in Nürnberg","label":"nennt Verfahren und Gerät"},
    {"key":"B","value":"Ondamed-Therapie: {kw} mit gepulsten Feldern (PEMF)","label":"Gerätename zuerst"},
    {"key":"C","value":"{kw} in Nürnberg: PEMF mit dem Ondamed-Gerät","label":"Ort und Gerät"}]', 'A',
  'Ondamed-Therapie (PEMF)', 'Magnetfeldtherapie', true,
  'Das Wort bleibt in Überschrift und Seitentitel stehen, weil genau danach gesucht wird. Du wählst die Formulierung.',
  '{"page":"/methoden-als-werkzeuge/ondamed-therapie.html"}',
  'Für „Magnetfeldtherapie Nürnberg“ liegt die Suche bei etwa 10 im Monat. Die Seite wird also vor allem bundesweit gefunden. Die Adresse der Seite bleibt. Der Text darunter beschreibt nur das Verfahren, ohne Wirkversprechen.',
  'Das Wort bleibt in der Überschrift, weil genau danach gesucht wird. Wie der Satz drumherum klingt, entscheidest du.',
  'treatment', 'draft'),

 ('f0a6730f-8f56-4c61-8085-1955f3bb285a','E6','text','Text','website',
  'Drei Blog-Beiträge mit Aussagen zur Wirkung',
  '**3 von 5 Beiträgen im Blog sagen, die Wirkung der Homöopathie sei belegt, oder sie schreiben, energetische Blockaden würden „behoben“**, und das kann als Wirkversprechen abgemahnt werden.',
  'Abgleich deines Blogs', '2026-10-13',
  '[{"key":"A","value":"Die 3 Beiträge bleiben online. Die Sätze mit Beweis- und Behandlungsaussage werden gestrichen oder neutral umgeschrieben. Du liest die neue Fassung vor dem Start gegen.","label":"Beiträge bleiben, Sätze werden angepasst"},
    {"key":"B","value":"Die 3 Beiträge gehen vom Netz und leiten auf den Blog weiter. Die anderen 2 bleiben.","label":"3 Beiträge entfallen"}]', 'A',
  '„Hortensien-Homöopathie-Experiment“: „… kann die Wissenschaft die Wirkung der Homöopathie … belegen“ · „Homöopathie im Krankenhaus“: „… als evidence based medicine“ · „Körper und Seele im Stillstand“: „… energetische Blockaden aufgedeckt und behoben“',
  null, false, null, '{"page":"/artikel/"}',
  'Den Beitrag zu Antibiotika habe ich auch gelesen. Er berichtet über eine Studie, enthält aber den Satz „Alternative zu Antibiotika“. Den schauen wir mit an. Die Texte sind rechtlich nicht geprüft.',
  'Hier brauche ich dein Ja. Ein Satz mit „belegt“ oder „behoben“ kann schon für eine Abmahnung reichen.',
  'legal', 'draft'),

 ('f0a6730f-8f56-4c61-8085-1955f3bb285a','E7','other','Video','website',
  'Vorstellungsvideo auf der Startseite: Sätze mit Wirkaussage',
  '**Im Video sagst du, deine Methode sei „sehr effektiv“ und könne „Freude und Lebensqualität zurückbringen“**, und das kann als Wirkversprechen gelten.',
  'Abgleich des Videos auf YouTube und deiner Startseite', '2026-10-13',
  '[{"key":"A","value":"Das Video kommt jetzt von der Startseite. Ein neuer Schnitt ohne diese Sätze kommt später wieder hinein.","label":"Video erst nach dem neuen Schnitt"},
    {"key":"B","value":"Das Video bleibt auf der Startseite, bis der neue Schnitt ohne diese Sätze fertig ist. Dann tauschen wir es aus.","label":"Video bleibt bis zum Tausch"}]', 'A',
  null, null, false, null, '{"page":"/"}',
  'Das Video hat bisher 6 Aufrufe auf YouTube. Die Beschreibung unter dem Video überarbeiten wir mit. Die Texte sind rechtlich nicht geprüft.',
  'Das ist dein Video, deshalb entscheidest du. Ich schneide gern eine neue Fassung, in der diese Sätze fehlen.',
  'legal', 'draft'),

 ('f0a6730f-8f56-4c61-8085-1955f3bb285a','E8','node','Seitenbaum','website',
  'Eigene Seiten für deine Anliegen: Schmerzen und Stress',
  '**Die alte Seite „Schmerzen und Verletzungen“ brachte nach der Startseite die meisten Klicks aus der Suche (7 von 72)** und ist heute nur noch eine Weiterleitung auf eine Sammelseite.',
  'Google-Suchdaten (90 Tage bis 09.10.) und deine Rückmeldung vom 31.08.', '2026-10-09',
  '[{"key":"A","value":"Beide Seiten kommen: „Schmerzen und Verletzungen“ zuerst, danach „Stress, Erschöpfung und Psyche“. Du gibst jeden Text frei, bevor er online geht.","label":"zwei Anliegen-Seiten"},
    {"key":"B","value":"Nur „Schmerzen und Verletzungen“ kommt jetzt. Die zweite Seite folgt später.","label":"erst eine Seite"},
    {"key":"C","value":"Es gibt keine eigenen Anliegen-Seiten. Es bleibt bei der Sammelseite „Was ist Ihr Anliegen?“.","label":"bleibt wie jetzt"}]', 'A',
  null, null, false, null, '{"node":"/anliegen-schmerzen-verletzungen.html","node_kind":"Anliegen","also":"/anliegen-stress-psyche.html"}',
  'Es geht um Anliegen im Alltag, nicht um Diagnosen. Du hast am 31.08. geschrieben, dass die Weiterleitung nicht die ideale Lösung ist.',
  'Hier brauche ich dein Ja, weil es um Gesundheitsthemen geht. Jeden Text siehst du vorher.',
  'health', 'draft');

commit;
