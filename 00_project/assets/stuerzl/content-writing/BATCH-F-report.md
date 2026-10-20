# Batch F: Kontakt und Standorte (Stürzl), Bericht

Stand 2026-10-11. Nur lokal, nichts live, kein Upload. Reviewer-Schritt nicht gelaufen (startet der Hauptagent). Kosten DataForSEO: 0 USD (vorhandene SERPs, Volumen und Metriken des Pools genutzt, Wettbewerber-Seiten mit `page_metrics.py` gemessen).

## Tabelle je Seite

| ID | Seite | Wörter | Bestand | Wettbewerber-Median (70 %) | G1 | G2 | G3 | G4 | G5 | G6 | Platzhalter | Cleanse-Aufrufe | Kosten USD | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-40 | Kontakt und Anfahrt | 771 | 255 | Typ C, kein Median (12 Kontaktseiten nur für G6-Überschriften) | pass | pass | pass | pass | 5/5 | pass | 5 | 2 | 0 | fertig, Freigabe offen |
| ST-41 | Standort Frankfurt | 1021 | 0 (neu) | 656 (459), 13 von 14 Seiten gelesen | pass | pass | pass | pass | 5/5 | pass | 3 | 2 | 0 | fertig, Freigabe offen |
| ST-42 | Standort München | 906 | 0 (neu) | 625 (437), 11 von 11 Seiten gelesen | pass | pass | pass | pass | 5/5 | pass | 2 | 1 | 0 | fertig, Freigabe offen |
| ST-33 | Aktuelles | 51 (nur Einleitung) | 0 Einleitung (338 Wörter Beitragsliste, CMS) | Typ C, kein Median (8 Nachrichtenseiten nur für G6) | pass | pass | pass | pass | 5/5 | pass | 0 | 1 | 0 | fertig, Freigabe offen |

Pfade: `/Users/martindrendel/741website/00_project/assets/stuerzl/content-writing/<st-id>-<slug>/05-final/page.md` mit den Ordnern `st-40-kontakt`, `st-41-standort-frankfurt`, `st-42-standort-muenchen`, `st-33-aktuelles`. Je Ordner auch `cms-blocks.txt`, `placeholders.md`, `schema.jsonld`, `measure-plan.md`, `04-gates/gates.md`, `OPEN-FLAGS.md`, `_run.json`, `_status.md`.

Hinweise zur Tabelle:

1. Der Auftrag nennt G1 bis G5. Das Skill-Skript hat inzwischen ein Gate G6 (SEO/GEO-Abdeckung und Schema). Alle vier Seiten bestehen es. Es verlangt `_work/bench-metrics.json`, `paa_questions`, `nap_file`, einen Direkt-Antwort-Block und bei Gesetzeszitat eine sichtbare Rechtsstand-Zeile. Ich habe dafür für Typ-C-Seiten Wettbewerber-Seiten gemessen (nur für den Überschriften-Vergleich, kein Wortziel).
2. Cleanse: ST-40 und ST-41 liefen zweimal (r1 auf einer früheren Fassung, r2 auf der Endfassung), ST-42 und ST-33 einmal. Alle Diffs bestanden, Lint 5/5. Übernommen: ST-41 r2 voll, ST-40 nur die Überschrift „Eine Durchsuchung läuft gerade“ (der Satzfragment-Einstieg der Cleanse wurde nicht übernommen), ST-42 und ST-33 ohne Änderung. Danach habe ich ST-42 von Hand umformuliert, weil G6c (Link-Netz) 32 % Ähnlichkeit zu ST-41 meldete (Grenze 25 %). Lint, Claims-Diff und alle Gates liefen danach wieder grün.
3. Link-Netz (G6c), geprüft mit einer Kopie nur meiner vier Seiten (die gemeinsame Datei `LINK-NETWORK.md` habe ich nicht angefasst): PASS. Hinweise: ST-41 hat 10 und ST-42 13 Textlinks (Bibliothek: 3 bis 8, nur Warnung, Ortsseiten verlinken auf die Leistungen). ST-33 hat 0 eingehende Links von meinen Seiten (kommt von der Startseite und dem Menü).
4. G6-Hinweise (nur Hinweise, beantwortet): „strafre*“ fehlt in ST-41: Die Seite nutzt Zusammensetzungen (Steuerstrafrecht, Wirtschaftsstrafrecht). „Schwerpunkt“, „Interessen“, „Tätigkeit“, „Jahren“ fehlen: „Schwerpunkt“ steht bewusst nicht im Text (BRAO, nur mit Beleg), die anderen Begriffe sind allgemein.

## Platzhalter und was nach der Korrektur des Hauptagenten entfernt wurde

Entfernt (jetzt bestätigte Fakten mit Quelle Source of Truth / `nap.json` / Live-Kontaktseite): Anschrift Frankfurt (Untermainkai 26, 60329 Frankfurt am Main), Post und Empfang (Wilhelm-Leuschner-Straße 23), Tiefgarage Wilhelm-Leuschner-Straße 27 bis 29 (Plätze 148 und 146), Telefonzeiten Montag bis Freitag durchgehend 9:30 bis 14:30 Uhr (beide Büros), Live-Werte der Notfallnummern (0160 3396513, 0160 95945730). Das waren 4 Platzhalter in ST-40 (Anschrift, Zeiten Frankfurt, Anfahrt und Parken Frankfurt, Zeiten München) und 3 in ST-41 (Anschrift, Zeiten, Anfahrt und Parken). Der Platzhalter „Notfall-Rufnummern mit Live-Werten“ in ST-40 wurde durch die Nummern im Text und einen engeren Platzhalter nur für die Besetzungszeiten ersetzt (wie vom Hauptagenten verlangt).

Offen: ST-40: Besetzungszeiten der Notfallnummern, Videogespräch und Termine vor Ort, Bearbeiter und Reaktionszeit, Pauschale der Erstberatung, Einwilligungstext des Formulars. ST-41: Leistungen und Fachgebiete vor Ort, weitere Personen im Büro, Pauschale. ST-42: Leistungen im Münchner Büro, Pauschale. ST-33: keine.

## Was blockiert wurde

Nichts. Kein Blocker bei den vier Seiten. ST-50 und die in der Anweisung ausgenommenen Seiten wurden nicht angefasst.

## Neue Widersprüche im Kundenmaterial

1. **Beginn in München:** Das Live-Profil von Lea Wimmer nennt „7/2025 Salary Partnerin bei STÜRZL (München)“. Dr. Stürzls Lebenslauf nennt „03/2026 Eröffnung einer Zweigstelle in München“, die Source of Truth „München seit Anfang 2026“. Dr. Glogger: 4/2026, Thorben Hoppe: 06/2026. Die Seiten nennen keine Eintrittsdaten.
2. **Zeiten München:** Google-Profil Dienstag bis Freitag 9:00 bis 18:00 Uhr, montags geschlossen, gegen Live und Source of Truth Montag bis Freitag 9:30 bis 14:30 Uhr. Google Frankfurt 9:00 bis 18:00 Uhr. Die Seiten folgen Live und Source of Truth.
3. **Zwei Hauseingänge in Frankfurt:** Die Source of Truth nennt „zwei Hauseingänge mit unterschiedlichen Adressen (Haupteingang/Post)“. Die Seiten nennen „Post und Empfang: Wilhelm-Leuschner-Straße 23“. Welcher Eingang für Besucher gilt, steht nirgends.
4. **Keine ÖPNV-Anfahrt für Frankfurt:** Die Live-Anfahrt gilt für die alte Anschrift. Für Untermainkai 26 ist keine belegt, deshalb steht keine im Text.
5. **Vergütung:** Startseite „RVG“ gegen Kostentext „kein RVG“. Erstberatung: Live-Kanzleiseite „Festpreis“, Kostentext „Pauschale EUR 250 bis 350“, Live-FAQ andere Sätze. Die Seiten sagen nur „Erstberatung gegen Pauschale“ ohne Betrag.
6. **Erreichbarkeit:** Live-Kanzleiseite und Live-FAQ „24/7 bei Bedarf“, Kostentext „persönlich erreichbar auch außerhalb der klassischen Bürozeiten“, Kontaktseite „Telefon 9:30 bis 14:30 Uhr“. Die Seiten übernehmen die beiden letzten, nicht „24/7“.
7. **Live-Profile mit Auszeichnungen:** Lea Wimmer („Beste Anwältin“, WirtschaftsWoche „TOP Anwalt“), Dr. Stürzl (Handelsblatt, JUVE, WirtschaftsWoche). Nicht übernommen (nicht freigegeben, BRAO-Risiko).
8. **Live-Aktuelles:** Die Teaser der Beitragsliste (CMS) nennen „JUVE-Rankings“ und „Spezialisierung, Personal Brand“. Nicht im Einleitungstext, im Flag vermerkt.

## Vorschläge für Regeln im Skill

1. Der Skill-Text und die Seitenvorlagen sollten G6 und seine Pflichtfelder (`nap_file`, `paa_questions`, `_work/bench-metrics.json`) im Brief-Template nennen. Für Typ-C-Seiten (Kontakt, News-Hub, Team) fehlt eine Regel, ob G6 ohne Benchmark bestehen darf. Aktuell scheitert G6 ohne Benchmark-Datei. Vorschlag: für Typ C ein Flag `brief.g6_type_c: true`, das Benchmark und Direkt-Antwort-Block nicht erzwingt.
2. Das Template „Kontaktseite“ hat keinen `answer`-Block, G6 verlangt ihn. Template ergänzen: S02 `answer`.
3. `make_cms_blocks.py` erkennt Marken wie `hero+answer` nicht (Regex `[\w-]+`). G6 erlaubt sie aber. Entweder `+` im Skript zulassen oder in G6 verbieten.
4. G6c: Ortsseiten teilen zwangsläufig Leistungsraster und Beruhigungszeilen. Die 25-%-Grenze der 5-Wort-Shingles trifft Standortpaare schnell. Vorschlag: Beruhigungszeile, CTA-Satz und Rechtsstand-Zeile aus dem Vergleich nehmen, oder die Grenze für Standortpaare auf 30 % setzen.
5. `run_gates.py` sollte `--page` auf `05-final/page.md` standardmäßig prüfen, wenn die Datei existiert (sonst wird die Entwurfsdatei geprüft).
6. Gesetzes-Lokalfakten: Als wiederverwendbarer Baustein für Ortsseiten taugt „Zuständige Finanzbehörde nach § 388 AO plus die Stellenliste der Landesfinanzverwaltung“. Für weitere Orte (Düsseldorf, Hamburg) gleiche Quellenart nutzen: Datenschutzhinweise der Steuerfahndung des Landes.
7. Die Fakten-Regel „Titel anderer Personen nur, wenn die Live-Profilseite sie nennt“ sollte den Hinweis tragen, dass Kammerverzeichnisse (BRAK-Suche) der bessere Beleg sind.

## Rechtsgrauzonen

1. „Anwalt für Steuerstrafrecht“ in der H1 der Ortsseiten (Zielkeyword): kann als Fachgebietsbezeichnung gelesen werden (BORA, FAO). Gleiche Frage wie bei der Selbstanzeige-Seite (A3).
2. Titel von Lea Wimmer (Fachanwältin für Steuerrecht seit 2017) und Dr. Glogger (Zertifizierter Compliance Officer, Univ. Münster) nur aus Live-Profilen, nicht von der Kanzlei bestätigt.
3. Der Satz „Wir vertreten Sie gegenüber allen diesen Stellen, auch wenn Sie nicht in Frankfurt/München wohnen“ ist eine Folgerung aus „Mandate in ganz Deutschland“.
4. Telefon-Notfallaussage („Wir beraten Sie am Telefon zum weiteren Vorgehen …“) stammt aus dem Startseiten-Brief (F3), dort Entwurf. Abgleich mit der Akutseite ST-18 nötig.
5. Notfallnummern stehen öffentlich auf der Live-Seite und sind im Text. Besetzungszeiten sind nicht dokumentiert (Platzhalter).
6. Kontaktformular: Das Formular gibt es heute nicht. Einwilligungstext (DSGVO, § 203 StGB) fehlt. Kein WhatsApp. Die Seite beschreibt das Formular, ohne seine Existenz zuzusagen.
7. Lokale Rechtsfakten (sechs hessische und neun bayerische Steuerfahndungsstellen) stammen von Behördenseiten vom 2026-10-11 und tragen „Rechtsstand: Oktober 2026“. Jährlich prüfen.
8. Link-Pfade ohne `/index.php/` nach `assets/stuerzl/slugs.json`; Links auf `/lea-wimmer/`, `/dr-monika-glogger/`, `/ratgeber/`, `/publikationen/` zeigen auf Seiten, die in anderen Läufen entstehen oder Vorschläge sind (`/ratgeber/`).
