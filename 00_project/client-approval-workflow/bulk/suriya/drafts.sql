-- Praxis Suriya (3f71ef33-8c74-4ea1-b2d3-0273c2e99649): Re-Check E1-E5 und 2 neue Karten E6, E7. Stand 13.10.2026.
-- Alles ENTWURF (status draft). Nichts ist ausgefuehrt. Der Haupt-Chat fuehrt die INSERTs aus.
-- Die Korrekturen zu E1-E5 stehen unten als auskommentierte UPDATEs. Martin entscheidet je Karte.
--
-- Geprueft am 13.10.2026:
--   Live-Website: curl auf 54 Seiten der page-sitemap (alle 200), Titel, H1, Preise, tel:-Links, Formular-Text.
--   Google-Profil: oeffentliche Maps-Seite (Name, Oeffnungszeiten Mo-Sa 07:30-20:00, Telefon, 13 Bewertungen, Attribute).
--     Die Leistungs- und Nebenkategorien-Liste ist oeffentlich NICHT sichtbar. Kein Local-Falcon-Zugriff in dieser Sitzung.
--   Datenbank (SELECT): E1-E5 sind draft, Einstellung vorhanden (Entscheiderin Coralie, health_client true). Kein Settings-INSERT noetig.
--   Memory: praxis-suriya-client, suriya-ayurveda-massage-page-untouchable, suriya-conversion-paths-must-stay,
--     suriya-elementor-dinakar-set, suriya-baseline-tracking, no-review-answering. Coralies harte Vorgaben vom 13.10.:
--     keine Seitenadressen aendern, nichts loeschen, keine groesseren Aenderungen ohne Absprache, vorher Backup, nur vorhandene Bilder.
--   Notizen: assets/suriya/content-pool/06-abgleich-live-2026-10-13.md, 07-umsetzung-2026-10-13.md, 03-demand (Search Console bis 09.10.),
--     02-competitors/metrics.json (11 Praxen, tel_link), Incident-Dossier 12./13.10. (Worktree admiring-nightingale-f0f882).
--
-- Ergebnis Re-Check:
--   E1 gueltig, kleine Korrektur (zweite Seite mit 85 EUR gefunden).
--   E2 gueltig, Variante A korrigieren ("Ayurveda" nicht in die Ueberschrift: Kannibalisierung mit Coralies Ayurveda-Massage-Seite).
--   E3 gueltig, Hinweis zu den Telefonzeiten ergaenzen.
--   E4 ueberholt: GBP-Teil nicht belegbar, Seiten grenzen sich seit 07.10. selbst ab. Neu als Website-Karte formulieren.
--   E5 ueberholt: Martin 13.10. "mehr Blog-Beitraege nicht noetig", /blog/ und Beitrag zum Thema existieren, Seite hat das Keyword schon. Empfehlung: loeschen.
--
-- Neue Karten:
--   E6 "Wer behandelt dich?" auf 15 von 19 Leistungsseiten (Live-Pruefung 13.10.; Fakten von /heilpraktikerin-ingelheim/).
--   E7 Anrede im Terminformular: 32 Seiten haben "du" im Text und "Sie" im Formular (Live-Pruefung 13.10.).
-- HWG: keine Heil- oder Erfolgsversprechen. hwg_checked bleibt false (Martin setzt es).

begin;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649','E6','text','Text','website',
  'Kurzer Block „Wer behandelt dich?“ auf den Leistungsseiten',
  'Auf **15 von 19 Leistungsseiten** steht nicht, wer dich behandelt. Menschen mit Beschwerden achten genau darauf, bei wem sie landen.',
  'Abgleich deiner Website', '2026-10-13',
  '[{"key":"A","value":"Heilpraktikerin seit 2010 (Erlaubnis der Landeshauptstadt Wiesbaden), Diplom in ayurvedischer Heilkunde in Sri Lanka (2012), Fortbildung zu CMD und Kiefergelenk in Frankfurt (2016).","label":"drei Stationen, genau wie auf deiner Seite „Über mich“"},
    {"key":"B","value":"Heilpraktikerin seit 2010, ausgebildet in Deutschland und Sri Lanka.","label":"nur der Satz, der schon auf 4 Seiten steht"},
    {"key":"C","value":"Nicht ergänzen","label":"die Seiten bleiben, wie sie sind"}]', 'A',
  'Auf 15 von 19 Seiten steht kein Block. Auf 4 Seiten steht: „Heilpraktikerin seit 2010 · ausgebildet in Deutschland und Sri Lanka (Akupunktur, Ayurveda, hnc)“',
  null, false, null,
  '{"page":"/nacken-schulter/"}',
  'Das Foto ist dein vorhandenes Porträt, es kommt kein neues Motiv dazu. Deine Seite „Ayurveda-Massage“ bleibt unberührt.',
  'Hier geht es um deine Ausbildung. Ich nehme nur, was schon auf deiner Seite „Über mich“ steht.',
  'none', 'draft'),

 ('3f71ef33-8c74-4ea1-b2d3-0273c2e99649','E7','text','Text','website',
  'Terminformular: du oder Sie?',
  'Auf **32 Seiten** sprichst du deine Patientinnen oben mit „du“ an, im Terminformular darunter mit „Sie“. Eine Anrede wirkt ruhiger, genau dort, wo jemand anfragt.',
  'Abgleich deiner Website', '2026-10-13',
  '[{"key":"A","value":"Schreib mir, wie ich dich in Ingelheim unterstützen kann, ob bei Migräne, Nackenbeschwerden oder für eine ayurvedische Ganzkörpermassage. Ich melde mich zeitnah bei dir zurück, um gemeinsam den passenden Weg für dich zu finden.","label":"„du“, passt zum Text auf den Seiten"},
    {"key":"B","value":"Schreib mir kurz, worum es geht, ob Migräne, Nackenbeschwerden oder Massage. Ich melde mich zeitnah bei dir, dann finden wir gemeinsam den passenden Weg.","label":"„du“, kürzer"},
    {"key":"C","value":"Lassen Sie mich wissen, wie ich Sie in Ingelheim unterstützen kann, ob bei Migräne, Nackenbeschwerden oder für eine ayurvedische Ganzkörpermassage. Ich melde mich zeitnah bei Ihnen zurück, um gemeinsam den passenden Weg für Sie zu finden.","label":"bleibt wie bisher, mit „Sie“"}]', 'A',
  'Lassen Sie mich wissen, wie ich Sie in Ingelheim unterstützen kann – ob bei Migräne, Nackenbeschwerden oder für eine ayurvedische Ganzkörpermassage. Ich melde mich zeitnah bei Ihnen zurück, um gemeinsam den passenden Weg für Sie zu finden.',
  null, false, null,
  '{"page":"/nacken-schulter/"}',
  'Das Formular selbst bleibt gleich: gleiche Felder, gleiche Wege zu dir. Nur der Satz darüber ändert sich.',
  'Hier entscheidest du, wie du deine Patientinnen an der wichtigsten Stelle ansprichst. Der Rest der Seite bleibt, wie er ist.',
  'none', 'draft');

commit;

-- =====================================================================================
-- KORREKTUREN zu E1-E5 (NICHT ausgefuehrt). Je Block einzeln pruefen. Alle Karten sind draft,
-- darum erzeugt ein UPDATE keine neue Version (Trigger approval_items_guard).
-- =====================================================================================

-- E1 (gueltig, kleine Korrektur): zweite Seite mit zwei Preisen gefunden (/hexenschuss-ruecken/: 85 EUR im Text, 95 EUR in der FAQ).
-- update public.approval_items set
--   why  = 'Auf deiner Website stehen für dieselbe Sitzung **80 €, 85 € und 95 €**. Auf „Nacken & Schulter“ und „Rücken & Hexenschuss“ stehen sogar zwei Preise auf einer Seite. Ein Preis überall schafft Vertrauen.',
--   note = 'Gilt dann auf allen Seiten: Schmerztherapie, Nacken & Schulter, Rücken & Hexenschuss, Kosten & Abrechnung.'
-- where client_id = '3f71ef33-8c74-4ea1-b2d3-0273c2e99649' and code = 'E1' and status = 'draft';

-- E2 (gueltig, Variante A korrigieren): "Ayurveda" nicht in die Ueberschrift. Die neue Massage-Seite rankt schon vor Coralies
-- /ayurveda-therapie/ fuer "ayurveda massage ingelheim" (Befund 12.10.). Coralies Seite bleibt unberuehrt.
-- Die Texte in den Varianten nennen nur Massage-Arten, die auf der Seite stehen (Rueckenmassage, Nervenregulationsmassage).
-- update public.approval_items set
--   variants = '[{"key":"A","value":"{kw} – Rückenmassage & Nervenregulation","label":"nennt zwei deiner Massage-Arten"},
--                {"key":"B","value":"{kw} – Zeit, in der dein Körper loslassen darf","label":"gefühlvoller"},
--                {"key":"C","value":"{kw}","label":"bleibt wie bisher"}]',
--   note = 'Das Wort „Ayurveda“ steht bewusst nicht in der Überschrift: Deine Seite „Ayurveda-Massage“ soll bei Google dafür vorne bleiben.'
-- where client_id = '3f71ef33-8c74-4ea1-b2d3-0273c2e99649' and code = 'E2' and status = 'draft';

-- E3 (gueltig, Hinweis ergaenzen): Startseite sagt "telefonisch montags 12-14 Uhr". Ein Anruf-Knopf weckt sonst falsche Erwartung.
-- update public.approval_items set
--   note = 'Die Nummer bleibt 0174 7411087, wie im Google-Profil. Auf deiner Startseite steht „telefonisch montags von 12 bis 14 Uhr“. Das bleibt so, daneben bleibt WhatsApp.'
-- where client_id = '3f71ef33-8c74-4ea1-b2d3-0273c2e99649' and code = 'E3' and status = 'draft';

-- E4 (ueberholt): GBP-Teil nicht belegbar (Leistungsliste oeffentlich nicht sichtbar; die geplante Liste in client_locations
-- enthaelt "Migraene-Analyse" nicht). Die Migraene-Analyse-Seite sagt seit 07.10. selbst "Ueberblick", die Cranio-Neuro-Analyse
-- ist der Termin. Beide nicht im Menue. Coralies Regel: keine Seitenadressen aendern, darum aktives Ja, Sicherung, nichts loeschen.
-- Neu als Website-Karte (Seitenbaum). Martin 13.10.: Zusammenlegen ja (06-abgleich Punkt 6).
-- update public.approval_items set
--   kind = 'node', type_label = 'Seitenbaum', area = 'website',
--   title = 'Migräne-Analyse und Cranio-Neuro-Analyse zu einer Seite zusammenlegen?',
--   why = 'Deine Seite „Migräne-Analyse“ gibt einen **Überblick über mögliche Ursachen**, die „SURIYA Cranio-Neuro-Analyse“ ist der **erste Termin**. Beide führen dieselbe Frau zum selben Termin.',
--   why_source = 'Abgleich deiner Website', why_date = '2026-10-13',
--   variants = '[{"key":"A","value":"Zusammenlegen: Die Texte der „Migräne-Analyse“ ziehen auf die Seite „SURIYA Cranio-Neuro-Analyse“ um. Die alte Adresse leitet automatisch dorthin weiter.","label":"eine Seite, ein Weg zum Termin"},
--                {"key":"B","value":"Beide Seiten behalten: Die „Migräne-Analyse“ bleibt der Überblick, die „SURIYA Cranio-Neuro-Analyse“ der Termin.","label":"keine Adresse ändert sich"}]',
--   recommended_key = 'A',
--   lock_note = null,
--   context = '{"node":"/suriya-cranio-neuro-analyse/","node_kind":"Leistungsseite"}',
--   note = 'Die alte Adresse leitet dann weiter. Vorher mache ich eine Sicherung, und nichts wird gelöscht.',
--   guide_text = 'Hier brauche ich dein Ja, weil sich eine Seitenadresse ändert. Vorher sichere ich alles.'
-- where client_id = '3f71ef33-8c74-4ea1-b2d3-0273c2e99649' and code = 'E4' and status = 'draft';

-- E5 (ueberholt, Empfehlung: loeschen). Gruende: Martin 13.10. "mehr Blog-Beitraege nicht noetig"; /blog/ (Gesundheitsjournal) und der
-- Beitrag /nervenregulation-vagusnerv/ (Okt 2025) existieren; /nervensystem-vagus-beruhigen/ hat "Nervensystem beruhigen" schon in Title und H1;
-- ein neuer /ratgeber/-Bereich widerspricht Coralies Wunsch nach weniger Seiten (07.10.) und nationale Suchanfragen bringen kaum Patientinnen aus Ingelheim.
-- delete from public.approval_items
-- where client_id = '3f71ef33-8c74-4ea1-b2d3-0273c2e99649' and code = 'E5' and status = 'draft';
--
-- Falls Martin die Karte als Beispiel fuer den Typ "Seitenbaum" behalten will, dann so (gleiche Adresse, kein neuer Bereich):
-- update public.approval_items set
--   title = 'Beitrag „Nervenregulation & Vagusnerv“ zum Ratgeber ausbauen?',
--   why = 'Zu **„nervensystem beruhigen“ (6.600 Suchen im Monat)** hast du schon eine Seite und einen Beitrag von Oktober 2025. Ein ausgebauter Beitrag beantwortet die Fragen deiner Patientinnen und verweist auf die Seite.',
--   why_source = 'Google-Suchdaten und Abgleich deiner Website', why_date = '2026-10-11',
--   variants = '[{"key":"A","value":"Ja, ausbauen: Ich liefere 3 bis 5 Fragen meiner Patientinnen."},
--                {"key":"B","value":"Ja, aber ihr schreibt den Entwurf, ich prüfe."},
--                {"key":"C","value":"Nein, der Beitrag bleibt so."}]',
--   recommended_key = 'B',
--   context = '{"node":"/nervenregulation-vagusnerv/","node_kind":"Wissen / Beitrag"}'
-- where client_id = '3f71ef33-8c74-4ea1-b2d3-0273c2e99649' and code = 'E5' and status = 'draft';
