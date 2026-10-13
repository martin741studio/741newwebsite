-- Praxis Suriya (3f71ef33-8c74-4ea1-b2d3-0273c2e99649): die 5 Beispiel-Elemente als ENTWURF (Martins Go 13.10.: "Alle 5 Beispiel-Elemente").
-- Status draft = Coralie sieht nichts. Sichtbar erst, wenn Martin im Portal "An Kunde geben" klickt.
-- Geprüft am 13.10.2026 gegen die Live-Website (curl) und die Content-Pool-Daten:
--   E1 /kosten-abrechnung/ 80 €, /nacken-schulter/ 85 € + 95 €, /ganzheitliche-schmerztherapie/ 95 €
--   E2 H1 /massage-ingelheim/ = "Massage in Ingelheim"; "massage ingelheim" 480/Monat (03-demand/volume.json);
--      Massage = 2.804 von 4.809 Einblendungen = 58 % (Search Console, 90 Tage, 05-report, Stand 11.10.)
--   E3 0 tel:-Links auf 9 geprüften Seiten; 7 von 11 Praxen mit Anruf-Knopf (06-abgleich-live-2026-10-13.md)
--   E4 /migraene-analyse-ingelheim/ und /suriya-cranio-neuro-analyse/ beide live; beide als Leistung im Google-Profil
--   E5 "nervensystem beruhigen" 6.600/Monat (03-demand/volume.json); /nervensystem-vagus-beruhigen/ live; Ratgeber-URL 404 (neu)
-- HWG: keine Heil- oder Erfolgsversprechen; E1 Preis, E4 Behandlungsname, E5 Gesundheitsthema = aktives Ja (keine 7-Tage-Regel).
-- Keine 7-Tage-Zustimmung, keine Mails.

begin;
insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649', 'd0e5d993-246a-4079-9c9a-a7f5c6d76963', 'Coralie', false, true)
on conflict (client_id) do update set approver_user_id = excluded.approver_user_id, approver_name = excluded.approver_name, health_client = true;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class,
   hwg_checked, hwg_checked_at, hwg_checked_by, status)
values
 ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649','E1','price','Preis','website',
  'Preis für eine Einzelsitzung Schmerztherapie',
  'Auf deiner Website stehen für dieselbe Sitzung **80 €, 85 € und 95 €**. Ein Preis überall schafft Vertrauen.',
  'Abgleich deiner Website', '2026-10-13',
  '[{"key":"A","value":"95 €","label":"steht so auf /ganzheitliche-schmerztherapie/"},
    {"key":"B","value":"85 €","label":"steht als Überschrift auf /nacken-schulter/"}]', 'A',
  null, null, false, null, '{}',
  'Gilt dann auf allen Seiten: Schmerztherapie, Nacken & Schulter, Kosten & Abrechnung.',
  'Hier brauche ich dein Ja. Für dieselbe Sitzung stehen auf deiner Website drei verschiedene Preise.',
  'price', true, now(), '741-Vorprüfung 13.10. (Live-Abgleich + HWG)', 'draft'),

 ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649','E2','text','Text','website',
  'Überschrift der Seite „Massage in Ingelheim“',
  '**„massage ingelheim“ wird 480-mal im Monat gesucht.** Massage-Suchen bringen 58 % deiner Einblendungen bei Google. Das Keyword bleibt, die Formulierung wählst du.',
  'Google-Suchdaten und deine Search Console (90 Tage)', '2026-10-11',
  '[{"key":"A","value":"{kw} – Ayurveda, Rücken & Nervenregulation","label":"nennt drei deiner Massage-Arten"},
    {"key":"B","value":"{kw} – Zeit, in der dein Körper loslassen darf","label":"gefühlvoller"},
    {"key":"C","value":"{kw}","label":"bleibt wie bisher"}]', 'A',
  'Massage in Ingelheim', 'Massage in Ingelheim', true, null, '{"page":"/massage-ingelheim/"}', null,
  'Das gelbe Schloss bleibt stehen, weil genau danach gesucht wird. Den Rest des Satzes wählst du.',
  'none', true, now(), '741-Vorprüfung 13.10. (Live-Abgleich + HWG)', 'draft'),

 ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649','E3','design','Design','website',
  'Anruf-Button: wo soll er stehen?',
  '**7 von 11 Praxen in deiner Umgebung** haben einen Knopf, der direkt anruft. Auf deiner Seite steht die Nummer nur als Text.',
  'Vergleich mit 11 Praxen in deiner Umgebung', '2026-10-13',
  '[{"key":"A","value":"Im Kopf der Seite","label":"immer oben sichtbar","design":"head"},
    {"key":"B","value":"Leiste unten am Handy","label":"nur auf dem Handy","design":"sticky"}]', 'A',
  null, null, false, null, '{"hero":"Naturheilpraxis in Ingelheim für Migräne & Nervensystem","cta":"Termin vereinbaren"}',
  'Die Nummer bleibt 0174 7411087, wie im Google-Profil.', null,
  'none', true, now(), '741-Vorprüfung 13.10. (Live-Abgleich + HWG)', 'draft'),

 ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649','E4','gbp','Google-Profil','gbp',
  'Migräne-Analyse und SURIYA Cranio-Neuro-Analyse zusammenlegen?',
  'Auf deiner Website und im Google-Profil stehen **zwei Einträge für denselben Einstieg**, und Patientinnen wissen dann nicht, womit sie anfangen sollen. Ein Name überall macht es klarer.',
  'Abgleich Website und Google-Profil', '2026-10-13',
  '[{"key":"A","value":"Zusammenlegen: überall nur „SURIYA Cranio-Neuro-Analyse“","label":"eine Seite, ein Eintrag im Profil; die alte Adresse leitet weiter"},
    {"key":"B","value":"Beide behalten","label":"zwei Seiten, zwei Einträge im Profil"}]', 'A',
  null, null, false,
  'Hauptkategorie „Heilpraktiker/in“, Name, Adresse und Website-Link ändert nur 741. Sie haben die größte Wirkung auf dein Ranking.',
  '{}', null, null,
  'treatment', true, now(), '741-Vorprüfung 13.10. (Live-Abgleich + HWG)', 'draft'),

 ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649','E5','node','Seitenbaum','website',
  'Neuer Ratgeber: „Vagusnerv und Nervensystem beruhigen“',
  '**„nervensystem beruhigen“ wird 6.600-mal im Monat gesucht.** Ein Ratgeber beantwortet die Fragen und verweist auf deine Seite „Nervensystem & Vagusnerv“.',
  'Google-Suchdaten', '2026-10-11',
  '[{"key":"A","value":"Ja, das passt zu mir – ich liefere 3–5 Fragen meiner Patientinnen"},
    {"key":"B","value":"Ja, aber schreibt ihr den Entwurf, ich prüfe"},
    {"key":"C","value":"Nein, das ist nicht mein Thema"}]', 'A',
  null, null, false, null, '{"node":"/ratgeber/vagusnerv-nervensystem-beruhigen/","node_kind":"Wissen / Ratgeber"}', null, null,
  'health', true, now(), '741-Vorprüfung 13.10. (Live-Abgleich + HWG)', 'draft');
commit;
