-- Naturheilpraxis Daniela Dumann (d01f4236-8674-45fe-a347-0751fa7b24de): 7 Entwurfs-Karten, alle status 'draft'.
-- Status draft = Daniela sieht nichts. Freigabe nur durch Martin im Chat (Grill-Karten), danach approval_release-Schritte.
-- Geprüft am 13.10.2026. Alle Live-Befunde per curl auf www.danieladumann.de (34 Seiten der pages-sitemap), Google-Daten per Search-Console-API.
--   E1 /ernährungsberatung live: "Östrogene ... verantwortlich für die Zunahme von Tumoren an Brust, Prostata und Darm", "Vegetarier ... viel geringeres Krebsrisiko",
--      "80% aller Erkrankungen ernährungsbedingt" (Text und Google-Beschreibung der Seite). Quelle: curl 13.10.2026.
--   E2 /schilddrüse live: H1 "Heilpraktiker für Schilddrüse und Mikroimmuntherapie - Ihr Schilddrüsenspezialist Berlin" (curl 13.10.).
--      Search Console API 13.07.-11.10.2026: Seite 37 Klicks / 569 Impressionen, Platz 3 nach Klicks (Start 163, Kurse & Seminare 53).
--      Anfrage "hildegard von bingen schilddrüse": 53 Impressionen, 5 Klicks, Position 4,3 (Chrome-Lesung 11.10.). Kein Suchvolumen für "heilpraktiker schilddrüse" (DataForSEO 11.10.: null), darum keine Zahl im Text.
--   E3 Google-Profil öffentlich (Maps-Ansicht 13.10.): keine Öffnungszeiten ("Öffnungszeiten hinzufügen"), 5,0 mit 9 Bewertungen. Website-Fußzeile: "Termine nach Vereinbarung".
--      NAP-Sperre in client_locations: "nach Vereinbarung", Status unbestätigt. Verzeichnis-Kampagne vom 09.10.: Di 9-13+15-18, Mi 10-13, Do 9-13+15-19, Fr 15-18 (Martins Vorgabe aus dem früheren zweiten Profil).
--      Telefonsprechstunde werktags 13-14 Uhr: Daniela im GBP-Report-Feedback vom 17.09.2026.
--   E4 Seitentitel: 21 von 34 Seiten enden auf "hildegardbingen" (Wix-Seitenname, og:site_name "hildegardbingen"); curl 13.10. Search Console: Anfrage "daniela dumann" 69 Klicks / 107 Impressionen (13.07.-11.10.).
--   E5 Videosprechstunde: Kommentar von Daniela zum Startseiten-Text vom 17.09.2026 (report_feedback, Abschnitt "Lokaler Abschnitt"). Live-Site: 0 Treffer für Video/Videosprechstunde.
--   E6 /behandlungen nennt den Kräutergarten in der Schorfheide; /kräuterheilkunde und /workshops nennen Schöneberg (Gartenarbeitsschule, dreimal im Jahr). curl 13.10.
--   E7 /kurse-seminare: 11 Karten "Beendet" (Widget zeigt alle Kurse). Seite: 53 Klicks, Position 4,4 (Search Console API 13.07.-11.10.).
-- Bereits erledigt, darum keine Karte: Startseiten-H1 und Intro-Absatz (09.10./live), Footer "Termine nach Vereinbarung" (live), Hausbesuche (nur /behandlungen sagt "nicht mehr").
-- HWG: gilt (Gesundheitskundin). Keine Heil- oder Erfolgsversprechen in den Varianten. hwg_checked bleibt false: Martin prüft vor der Freigabe.
-- Kein Preis, keine Rechnung, keine Frist, kein Tool-Name. Anrede: Karten-Text in du (so spricht das Portal mit Daniela), Varianten-Text für die Website in Sie (Stimme der Website).
-- Einstellungen: approver_user_id bleibt NULL (Vorgabe). Daniela hat ein Client-Profil (user_id 34937572-ec83-4c1e-ac45-88c4cb2b60c9). Ohne Verknüpfung kann sie nicht entscheiden.

begin;

insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('d01f4236-8674-45fe-a347-0751fa7b24de', null, 'Daniela Dumann', false, true)
on conflict (client_id) do nothing;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('d01f4236-8674-45fe-a347-0751fa7b24de','E1','text','Text','website',
  'Seite „Ernährungsberatung“: drei Aussagen zu Krebs und Erkrankungen',
  'Auf der Seite stehen **drei Aussagen, die Krebs oder eine Prozentzahl ohne Beleg nennen**, eine davon auch im Google-Text zur Seite.',
  'Abgleich deiner Website', '2026-10-13',
  '[{"key":"A","value":"Die drei Sätze streichen","label":"der Rest der Seite bleibt, der Google-Text zur Seite wird ohne die Zahl neu geschrieben"},
    {"key":"B","value":"Durch eine neutrale Aussage ersetzen: „Hildegard von Bingen sah in der Ernährung die Grundlage für ein Leben im rechten Maß. In der Beratung besprechen wir, was zu Ihnen passt.“","label":"ersetzt die drei Sätze durch eine Aussage ohne Krebs und ohne Zahl"}]',
  'A',
  'Vor allem die Östrogene (bei Frau und Mann) sind verantwortlich für die Zunahme von Tumoren an Brust, Prostata und Darm. | Schon seit den 80er Jahren weiß man, dass Vegetarier ein viel geringeres Krebsrisiko haben. | Man geht davon aus, dass heutzutage 80% aller Erkrankungen ernährungsbedingt sind.',
  null, false, null, '{"page":"/ernährungsberatung"}',
  'Die neue Formulierung wird vor dem Einbau noch einmal auf das Heilmittelwerbegesetz geprüft.',
  'Hier brauche ich dein Ja. Solche Sätze können für Heilpraktikerinnen unangenehm werden, deshalb schlage ich vor, sie zu streichen.',
  'health', 'draft'),

 ('d01f4236-8674-45fe-a347-0751fa7b24de','E2','text','Text','website',
  'Überschrift der Seite „Schilddrüse“',
  'Die Überschrift nennt dich „Schilddrüsenspezialist“, und die Seite ist mit **37 Google-Klicks in 90 Tagen** deine Nummer 3.',
  'Google-Suchdaten (90 Tage) und Abgleich deiner Website', '2026-10-11',
  '[{"key":"A","value":"Heilpraktikerin für Schilddrüse in Berlin: naturheilkundliche Begleitung und Mikroimmuntherapie","label":"ohne „Spezialist“, nennt Berlin und deine Methode"},
    {"key":"B","value":"Schilddrüse und Hildegard von Bingen: naturheilkundliche Begleitung in Berlin-Charlottenburg","label":"greift die Suche „hildegard von bingen schilddrüse“ auf, die dich auf Platz 4 zeigt"},
    {"key":"C","value":"Heilpraktikerin für Schilddrüse in Berlin","label":"kurz und schlicht"}]',
  'B',
  'Heilpraktiker für Schilddrüse und Mikroimmuntherapie - Ihr Schilddrüsenspezialist Berlin',
  'Schilddrüse', true,
  'Das Wort „Schilddrüse“ bleibt in der Überschrift, weil danach gesucht wird. Die Formulierung wählst du.',
  '{"page":"/schilddrüse"}', null,
  'Das Wort „Spezialist“ lasse ich lieber weg, weil für Gesundheitsthemen strenge Regeln gelten. Hier brauche ich dein Ja.',
  'health', 'draft'),

 ('d01f4236-8674-45fe-a347-0751fa7b24de','E3','gbp','Google-Profil','gbp',
  'Öffnungszeiten: überall dieselbe Version',
  '**Drei Stellen, drei Versionen:** Bei Google stehen keine Zeiten, deine Website schreibt „Termine nach Vereinbarung“, und für die Verzeichnis-Einträge sind Dienstag bis Freitag hinterlegt.',
  'Abgleich Google-Profil, Website und Verzeichnis-Einträge', '2026-10-13',
  '[{"key":"A","value":"Termine nach Vereinbarung · Telefonsprechstunde werktags 13–14 Uhr","label":"bei Google ohne feste Zeiten, überall derselbe Satz"},
    {"key":"B","value":"Di 9–13 und 15–18 Uhr · Mi 10–13 Uhr · Do 9–13 und 15–19 Uhr · Fr 15–18 Uhr · Telefonsprechstunde werktags 13–14 Uhr","label":"feste Zeiten bei Google, auf der Website und in den Verzeichnissen"}]',
  'B',
  null, null, false,
  'Name, Adresse, Hauptkategorie und Website-Link ändert nur 741.',
  '{}',
  'Stimmen die Zeiten nicht mehr, wähle „Mit kleiner Änderung“ und schreibe die richtigen auf.',
  'Ich möchte, dass überall dieselben Zeiten stehen. Sag mir bitte, welche Version stimmt.',
  'none', 'draft'),

 ('d01f4236-8674-45fe-a347-0751fa7b24de','E4','text','Text','website',
  'Der Name hinter jedem Seitentitel bei Google',
  'Bei **21 von 34 Seiten** hängt an der Google-Überschrift noch der Name „hildegardbingen“ statt deines Praxisnamens.',
  'Abgleich deiner Website und Google-Suchdaten (90 Tage)', '2026-10-13',
  '[{"key":"A","value":"Naturheilpraxis Daniela Dumann","label":"wie in der Fußzeile und im Impressum, kurz genug für die Google-Überschrift"},
    {"key":"B","value":"Hildegard von Bingen Berlin Naturheilpraxis Daniela Dumann","label":"genau wie dein Google-Profil, aber lang"},
    {"key":"C","value":"Daniela Dumann","label":"am kürzesten, „daniela dumann“ ist deine häufigste Suche"}]',
  'A',
  'hildegardbingen', null, false, null, '{"scope":"alle Seitentitel"}',
  'Der volle Name aus dem Google-Profil bleibt in den Verzeichnissen und im Profil.',
  'Dein Name steht hinter jeder Überschrift bei Google. Welcher soll es sein?',
  'none', 'draft'),

 ('d01f4236-8674-45fe-a347-0751fa7b24de','E5','other','Leistung','website',
  'Videosprechstunde auf der Website nennen?',
  'Du hast am 17.09. vorgeschlagen, **Videosprechstunden über eine datensichere Verbindung** aufzunehmen; auf der Website steht dazu bisher nichts.',
  'Dein Hinweis zum Startseiten-Text', '2026-09-17',
  '[{"key":"A","value":"Als Beratung nennen: „Beratungs- und Vorgespräche sind auch per Video möglich, über eine datensichere Verbindung. Behandlungen finden in der Praxis statt.“","label":"ein Satz im Abschnitt zum ersten Termin"},
    {"key":"B","value":"Nicht nennen","label":"bleibt wie jetzt: Termine in der Praxis, Kurse online"}]',
  'A',
  null, null, false, null, '{"page":"/"}',
  'Der Satz wird vor dem Einbau auf das Heilmittelwerbegesetz geprüft (Behandlung aus der Ferne).',
  'Gute Idee von dir. Bei Gesundheitsleistungen gelten feste Regeln, deshalb brauche ich dein klares Ja zur Formulierung.',
  'legal', 'draft'),

 ('d01f4236-8674-45fe-a347-0751fa7b24de','E6','text','Text','website',
  'Kräutergarten: Schorfheide oder Schöneberg?',
  '**Zwei Orte für einen Garten:** Die Seite „Behandlungen“ spricht von der Schorfheide, „Kräuterheilkunde“ und „Workshops“ von der Gartenarbeitsschule in Schöneberg.',
  'Abgleich deiner Website', '2026-10-13',
  '[{"key":"A","value":"Den Hildegard-Heilkräutergarten gibt es in Berlin-Schöneberg (Gartenarbeitsschule). Dreimal im Jahr führe ich dort durch den Garten. Bei Seminaren und Workshops stellen wir aus den Pflanzen Elixiere und Salben her.","label":"passt zu den Seiten „Kräuterheilkunde“ und „Workshops“"},
    {"key":"B","value":"Bei Seminaren und Workshops stellen wir aus heimischen Hildegardpflanzen Elixiere und Salben her.","label":"ohne Ortsangabe"}]',
  'A',
  'In meinem Hildegard Kräutergarten in der Schorfheide sind die meisten unserer heimischen Hildegardpflanzen zu sehen. Bei Seminaren und Workshops verwenden wir sie zur Herstellung von Elixieren und Salben.',
  null, false, null, '{"page":"/behandlungen"}', null,
  'Dein Garten gehört zu dem, was deine Praxis besonders macht. Er soll überall am richtigen Ort stehen.',
  'none', 'draft'),

 ('d01f4236-8674-45fe-a347-0751fa7b24de','E7','other','Kursseiten','website',
  'Beendete Termine auf den Kursseiten',
  '**11 Karten** auf „Kurse & Seminare“ zeigen „Beendet“, dabei ist die Seite mit 53 Google-Klicks in 90 Tagen deine Nummer 2.',
  'Abgleich deiner Website und Google-Suchdaten (90 Tage)', '2026-10-11',
  '[{"key":"A","value":"Nur Termine zeigen, die noch laufen oder kommen","label":"beendete Karten verschwinden von den Kursseiten"},
    {"key":"B","value":"Beendete Karten bleiben sichtbar","label":"wie jetzt, mit dem Hinweis „Beendet“"}]',
  'A',
  null, null, false, null, '{"page":"/kurse-seminare"}',
  'Gilt auch für Vorträge, Workshops und Kräutersalon. Kommt ein Vortrag wieder, steht er mit dem neuen Termin zurück auf der Seite.',
  null,
  'none', 'draft');

commit;
