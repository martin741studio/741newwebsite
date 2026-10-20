-- Maria Brasse / ShuiGuru (444ac77b-747d-4855-89e5-12ac97d2363c): 7 decisions as DRAFT for the portal decision module.
-- NOT EXECUTED. The main session inserts after Martin's review. Status draft = the client sees nothing.
-- Language: German, du-form in the card text (Martin writes to Maria with "du"). Website texts in the variants use Sie, like the live site.
-- Facts checked 13.10.2026 (live site by curl, shuiguru.de, 15 URLs):
--   E1 /kosten/ and /online-beratung/ show the box "Aktuell: Kostenlose Online-Beratung gegen Google-Bewertung", valid until 15 October.
--      Maria proposed the idea herself in report feedback of 02.09.2026 ("im Gegenzug fuer eine Google Bewertung") and wrote the final text on 21.09.2026.
--   E2 /ueber-mich-maria-brasse/ has no question "Was macht eine Feng-Shui-Beraterin?". Volumes: feng shui berater 320, feng shui beratung 260 (31.08.2026), PAA question seen 08.10.2026.
--   E3 /feng-shui-garten/ has no neighbour question (grep "Nachbarn": 0 hits). "feng shui garten schutz vor nachbarn" = 90 per month (SERP check 08.10.2026).
--   E4 Startseite still shows "So laeuft die Beratung - in 5 Schritten". Maria's note 17.09.2026: she wants to rethink the order. No later change found.
--   E5 /feng-shui-in-der-arbeitswelt/ has no Reichtumsecke answer (only /feng-shui-arbeitszimmer/ has). "feng shui buero" = 320 per month.
--   E6 /plancheck-vor-baubeginn/ has no science question. "feng shui hausbau" = 260 per month.
--   E7 /kosten/ shows "Positive Resultate sind vorprogrammiert" and "Heilrituale". Both texts come from Maria's own feedback of 22.09.2026.
-- Ruled out or done (not in this file): hero photo (live, glasses), Kaeffchen button in hero (live), GBP categories/hours/services (done 30.09.), profile name (locked 14.09.), Grundriss page (Martin 25.09.: later), GBP posts (not approved).
-- Health: the live site has therapy wording (Quantenheilung, heilender Prozess, Heilrituale, Heilpraktikerin fuer Psychotherapie, Fallstudie mit psychohygienischen Gespraechen).
--   So health_client = true (precaution). No healing promises, no success guarantees in any variant. hwg_checked stays false.
-- Open gap: approver_user_id stays NULL as the brief says. A client profile exists (user_id 44edf23a-c80a-4c49-90d9-58fcc42f4c19, role client, display_name Maria Brasse).
--   Without an approver Maria cannot decide. The main session may set it, as in the Suriya seed.
-- No prices, no fee talk, no tool names, no deadlines except the one Maria wrote on her own page (E1).

begin;

insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('444ac77b-747d-4855-89e5-12ac97d2363c', null, 'Maria Brasse', false, true)
on conflict (client_id) do nothing;
-- optional, main session: update public.client_approval_settings set approver_user_id = '44edf23a-c80a-4c49-90d9-58fcc42f4c19' where client_id = '444ac77b-747d-4855-89e5-12ac97d2363c' and approver_user_id is null;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('444ac77b-747d-4855-89e5-12ac97d2363c','E1','text','Text','website',
  'Kostenlose Kurzberatung „gegen Google-Bewertung“',
  'Google erlaubt keine **Bewertungen als Gegenleistung**, und dein Hinweis bis 15. Oktober verknüpft die kostenlose Kurzberatung genau damit.',
  'Google-Richtlinien für Bewertungen und deine Seiten „Kosten“ und „Online-Beratung“', '2026-10-13',
  '[{"key":"A","value":"Kostenlose Online-Kurzberatung per Video bis zum 15. Oktober, ohne Bedingung. Ideal, um Feng Shui unverbindlich kennenzulernen. Nach Absprache täglich, Montag bis Sonntag, von 10 bis 19 Uhr.","label":"die Aktion bleibt, die Bewertung wird nicht mehr genannt"},
    {"key":"B","value":"Der Hinweis verschwindet jetzt von beiden Seiten.","label":"die Aktion endet sofort"},
    {"key":"C","value":"Bleibt wie jetzt, mit Hinweis auf die Google-Bewertung.","label":"Risiko für dein Google-Profil"}]', 'A',
  'Bis zum 15. Oktober biete ich eine kostenlose Kurzberatung per Video an – im Gegenzug freue ich mich über eine ehrliche Google-Bewertung.', null, false, null, '{"page":"/kosten/"}',
  'Das gilt auch für /online-beratung/ und die FAQ-Antwort auf /kosten/, die Überschrift „… gegen Google-Bewertung“ ändert sich mit, und nach dem 15. Oktober nehmen wir den Kasten in jedem Fall heraus.',
  'Die Aktion ist eine gute Idee, nur die Bedingung ist das Problem, und um Bewertungen bitten wir deine Kund:innen danach getrennt und ohne Gegenleistung.',
  'legal', 'draft'),

 ('444ac77b-747d-4855-89e5-12ac97d2363c','E2','text','Text','website',
  'Antwort auf „Was macht eine Feng-Shui-Beraterin?“',
  'Google zeigt diese Frage bei **„feng shui berater“ (320 Suchen im Monat) und „feng shui beratung“ (260)**, aber auf deiner Seite „Über mich“ steht noch keine Antwort.',
  'Google-Suchdaten und deine Website', '2026-10-08',
  '[{"key":"A","value":"Was macht eine {kw}? Ich schaue mir an, wie Menschen einen Raum tatsächlich nutzen und wo er sie dabei bremst. Dazu erfasse ich Gebäude, Grundstück und die Geschichte des Ortes, arbeite mit den vier Himmelsrichtungen und Elementen und übersetze das in konkrete Schritte: Was wird umgestellt, was kommt weg, was fehlt. Sie bekommen keine Regelliste, sondern eine Rückmeldung für genau Ihren Raum.","label":"ausführlich, mit deinen vier Himmelsrichtungen"},
    {"key":"B","value":"Was macht eine {kw}? Sie schaut, wie ein Raum auf Menschen wirkt, und schlägt konkrete Veränderungen vor. Ich arbeite mit schamanischem Feng Shui: Ich beziehe die Geschichte des Ortes und die Menschen ein, die ihn nutzen. Das Ergebnis sind klare Schritte für Ihren Raum.","label":"kürzer, nennt das schamanische Feng Shui"}]', 'A',
  null, 'Feng-Shui-Beraterin', true, 'Die Frage bleibt, weil Google sie bei diesen Suchen zeigt. Die Antwort wählst du.', '{"page":"/ueber-mich-maria-brasse/"}',
  'Die Frage erscheint auch als FAQ-Daten für Google.',
  'Ich habe die Antwort aus deinen eigenen Worten gebaut. Im Kommentar kannst du sie ändern.',
  'none', 'draft'),

 ('444ac77b-747d-4855-89e5-12ac97d2363c','E3','text','Text','website',
  'Garten-Seite: Frage zu den Blicken der Nachbarn',
  '**„feng shui garten schutz vor nachbarn“ wird 90-mal im Monat gesucht**, aber deine Garten-Seite beantwortet die Frage noch nicht.',
  'Google-Suchdaten und deine Website', '2026-10-08',
  '[{"key":"A","value":"Wie schütze ich meinen Garten vor den Blicken der Nachbarn? Schutz muss keine Mauer sein. Ich schaue, wo Sie sich beobachtet fühlen, und setze genau dort Sichtschutz: eine Hecke, eine Bepflanzung oder ein Rankgerüst. Die anderen Seiten bleiben offen, damit der Garten nicht wie ein Käfig wirkt.","label":"mit konkreten Beispielen"},
    {"key":"B","value":"Wie schütze ich meinen Garten vor den Blicken der Nachbarn? Ich schaue zuerst, wo Sie sich beobachtet fühlen. Dort entsteht Sichtschutz aus Pflanzen statt aus Mauern, damit der Garten offen und lebendig bleibt.","label":"kürzer"},
    {"key":"C","value":"Die Frage kommt nicht auf die Seite.","label":"die Seite bleibt wie sie ist"}]', 'A',
  null, null, false, null, '{"page":"/feng-shui-garten/"}',
  'Weitere Garten-Fragen (Brunnen, kleiner Garten oder Balkon) besprechen wir danach.',
  'Die Antwort nennt keine Himmelsrichtung, damit sie zu deinem Ansatz mit vier Elementen passt.',
  'none', 'draft'),

 ('444ac77b-747d-4855-89e5-12ac97d2363c','E4','text','Text','website',
  'Startseite: „So läuft die Beratung“',
  'Du hast geschrieben, dass eine **Online-Kurzberatung und eine längere Begleitung** nicht gleich ablaufen, die Startseite zeigt aber einen Ablauf in 5 Schritten für beides.',
  'Dein Feedback vom 17.09. und deine Startseite', '2026-09-17',
  '[{"key":"A","value":"Drei feste Schritte für alle: 1. Käffchen, 2. Analyse, 3. Konzept. Wenn Sie mehr wünschen, begleite ich Sie danach bei der Umsetzung und der Nachschau.","label":"die ersten Schritte sind immer gleich, danach je nach Umfang"},
    {"key":"B","value":"Kurzberatung (online, 45 Minuten): Käffchen, Analyse, klare nächste Schritte. Begleitung (mehrere Wochen): zusätzlich Umsetzung und Nachschau mit mir.","label":"Kurzberatung und Begleitung getrennt"},
    {"key":"C","value":"5 Schritte: Käffchen, Analyse, Konzept, Umsetzung, Nachschau.","label":"bleibt wie jetzt"}]', 'A',
  '5 Schritte: Käffchen, Analyse, Konzept, Umsetzung, Nachschau', null, false, null, '{"page":"/"}',
  'Die Schritte-Zeile auf der Startseite ändert sich. Die Homeoffice-Seite hat ihren eigenen Ablauf und bleibt.',
  'Das ist dein eigener Gedanke aus dem Feedback: am Anfang gleich, danach je nach Umfang.',
  'none', 'draft'),

 ('444ac77b-747d-4855-89e5-12ac97d2363c','E5','text','Text','website',
  'Büro-Seite: Frage zur Reichtumsecke',
  '**„feng shui büro“ wird 320-mal im Monat gesucht**, und Google zeigt dort die Frage nach der Reichtumsecke, aber auf deiner Seite „Feng Shui in der Arbeitswelt“ fehlt die Antwort.',
  'Google-Suchdaten und deine Website', '2026-10-08',
  '[{"key":"A","value":"Wo ist die Reichtumsecke, und gibt es sie im Büro? Die Reichtumsecke gehört zum klassischen Feng Shui. Ich arbeite schamanisch mit den vier Himmelsrichtungen und den vier Elementen Feuer, Wasser, Luft und Erde, ohne Berechnung. Im Büro schaue ich, wo Ihr Team konzentriert arbeiten kann: Schreibtisch mit Rücken zur Wand und Blick zur Tür, klare Wege und kein Durchgangsverkehr am Arbeitsplatz.","label":"wie deine Antwort auf der Homeoffice-Seite, mit Büro-Beispielen"},
    {"key":"B","value":"Wo ist die Reichtumsecke, und gibt es sie im Büro? Die Reichtumsecke ist ein Konzept aus dem klassischen Feng Shui. Ich arbeite mit den vier Himmelsrichtungen und Elementen und prüfe, was Ihr Team im Büro braucht.","label":"kürzer"},
    {"key":"C","value":"Die Frage kommt nicht auf die Seite.","label":"die Seite bleibt wie sie ist"}]', 'A',
  null, null, false, null, '{"page":"/feng-shui-in-der-arbeitswelt/"}',
  'Auf /feng-shui-arbeitszimmer/ steht schon eine Antwort mit demselben Inhalt.',
  'Die Antwort folgt deinem Text von der Homeoffice-Seite, damit beide Seiten gleich klingen.',
  'none', 'draft'),

 ('444ac77b-747d-4855-89e5-12ac97d2363c','E6','text','Text','website',
  'Plancheck-Seite: „Ist Feng Shui wissenschaftlich belegt?“',
  '**„feng shui hausbau“ wird 260-mal im Monat gesucht**, und Google zeigt dort die Frage nach dem wissenschaftlichen Beleg, aber auf deiner Plancheck-Seite fehlt eine Antwort.',
  'Google-Suchdaten und deine Website', '2026-10-08',
  '[{"key":"A","value":"Ist Feng Shui wissenschaftlich belegt? Feng Shui ist keine Naturwissenschaft und will es nicht sein. Ich arbeite schamanisch mit den vier Himmelsrichtungen und Elementen und beziehe die Geschichte des Ortes ein. Ich verspreche keine messbaren Ergebnisse, aber ich sage Ihnen immer, welche Schritte sich praktisch umsetzen lassen.","label":"ehrlich, ohne Versprechen"},
    {"key":"B","value":"Ist Feng Shui wissenschaftlich belegt? Nein. Feng Shui ist eine Erfahrungslehre darüber, wie Menschen auf Räume reagieren. Beim Plancheck prüfe ich Ihren Plan nach dieser Erfahrung: Ausrichtung, Licht, Wege und Nutzung. Was Sie davon umsetzen, entscheiden Sie.","label":"kurz und klar"},
    {"key":"C","value":"Die Frage kommt nicht auf die Seite.","label":"die Seite bleibt wie sie ist"}]', 'A',
  null, null, false, null, '{"page":"/plancheck-vor-baubeginn/"}',
  'Hier zählt deine Haltung. Du kannst die Antwort im Kommentar umschreiben.',
  'Beide Antworten versprechen nichts, was sich nicht belegen lässt.',
  'none', 'draft'),

 ('444ac77b-747d-4855-89e5-12ac97d2363c','E7','text','Text','website',
  'Kosten-Seite: „Positive Resultate sind vorprogrammiert“',
  'Der Satz klingt wie eine **Erfolgsgarantie** und kann abgemahnt werden, und auf derselben Seite steht außerdem „Heilrituale“.',
  'Deine Seite „Kosten“', '2026-10-13',
  '[{"key":"A","value":"Nach einer Online-Beratung haben Sie klare Ideen für Ihre ersten Umsetzungsschritte, Aufbruchsstimmung und können sofort mit Veränderungen loslegen. Dadurch kommt der Stein ins Rollen und der Knoten für Ihr Thema platzt.","label":"ohne den Satz mit „vorprogrammiert“"},
    {"key":"B","value":"Nach einer Online-Beratung haben Sie klare Ideen für Ihre ersten Umsetzungsschritte, Aufbruchsstimmung und können sofort mit Veränderungen loslegen. Dadurch kommt der Stein ins Rollen. Welche Ergebnisse sich zeigen, hängt auch davon ab, was Sie umsetzen.","label":"mit Hinweis auf die Umsetzung"},
    {"key":"C","value":"Bleibt wie jetzt, mit „Positive Resultate sind vorprogrammiert“.","label":"Risiko einer Abmahnung"}]', 'A',
  'Nach einer Online-Beratung haben Sie klare Ideen für Ihre ersten Umsetzungsschritte, Aufbruchsstimmung und können sofort mit Veränderungen loslegen. Dadurch kommt der Stein ins Rollen und der Knoten für Ihr Thema platzt. Positive Resultate sind vorprogrammiert.', null, false, null, '{"page":"/kosten/"}',
  'Mit A oder B ändere ich auch „Heilrituale“ in „Rituale“ (Vor-Ort-Beratung). Alles andere auf der Seite bleibt.',
  'Das ist dein Text von der Kosten-Seite. Nur der letzte Satz ist ein Versprechen, das wir nicht belegen können.',
  'legal', 'draft');

commit;
