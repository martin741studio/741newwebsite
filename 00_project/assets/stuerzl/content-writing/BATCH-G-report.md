# Batch G: Ratgeber (ST-34, ST-35, ST-36, ST-37), Bericht

Datum: 2026-10-11. Alle vier Seiten sind als Vorschlag geschrieben ("wartet auf Abstimmung mit der Kanzlei"). Nichts ist hochgeladen, nichts im CMS, kein Reviewer-Aufruf. Pfade: `/Users/martindrendel/741website/00_project/assets/stuerzl/content-writing/<ordner>/05-final/page.md`.

## Tabelle je Seite

| ID | Seite | Ordner | Wörter | Bestand | Wettbewerber-Median (Untergrenze 70 %) | G1 | G2 | G3 | G4 | G5 | G6 | Platzhalter | Cleanse-Aufrufe | Kosten USD | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-34 | Ratgeber Steuerstrafrecht (Hub) | `st-34-ratgeber` | 538 | keiner (Seite neu) | Typ C, kein Median (Vorlage 350 bis 600) | pass | pass | pass | pass | pass (5/5) | pass | 0 | 1 | 0,097 | fertig, Freigabe offen |
| ST-35 | Steuerhinterziehung: Strafe und Strafrahmen | `st-35-steuerhinterziehung-strafe` | 1.672 | keiner | 1.469 (13 Seiten), 1.028 | pass | pass | pass | pass | pass (5/5) | pass | 2 (Autor, Datum) | 1 | 0,0035 | fertig, Freigabe offen |
| ST-36 | Verjährung der Steuerhinterziehung | `st-36-verjaehrung` | 1.284 | keiner | 800 (12 Seiten), 560 | pass | pass | pass | pass | pass (5/5) | pass | 2 (Autor, Datum) | 1 | 0 (SERP aus dem Pool) | fertig, Freigabe offen |
| ST-37 | Krypto und Steuerhinterziehung | `st-37-krypto` | 1.199 | keiner | 1.214 (13 Seiten), 849 | pass | pass | pass | pass | pass (5/5) | pass | 2 (Autor, Datum) | 1 | 0,0035 | fertig, Freigabe offen |

Wörter zählt `wordcount.py` auf `05-final/page.md`. Gate-Berichte: `04-gates/gates.md` je Ordner (G1 bis G6, das Skript hat jetzt ein Gate G6 für SEO/GEO; die Batch-Anweisung nennt nur G1 bis G5). Gesamtkosten DataForSEO: etwa 0,11 USD (je eine SERP, dazu eine Volumen-Abfrage für den Hub). Lesbare Gesetzestexte, BGH-Urteil, BMF-Schreiben und KStTG liegen in `_work/` jeder Seite.

Cleanse: codex lief je einmal. ST-34 eine Änderung übernommen, eine abgelehnt. ST-35 die einzige Änderung abgelehnt (sie strich die Wendung der Kanzlei "kein Kavaliersdelikt, sondern eine Straftat"). ST-36 die Änderung übernommen. ST-37 keine Änderung. Der Diff `diff_claims.py diff` besteht in allen vier Fällen.

## Was blockiert wurde

Nichts ganz. Zwei Punkte sind Einschränkungen, keine Blocker:

1. **ST-37 Krypto** hat nur 20 Suchen (Pool-Priorität C, `needs_client`). Die Seite ist geschrieben, aber nur mit Quellen, die ich im Lauf gespeichert habe: BMF-Schreiben vom 6. März 2025, § 23 EStG, KStTG. Steuerrechtliche Aussagen soll die Fachanwältin für Steuerrecht gegenlesen.
2. **ST-34 Hub** hat kein Keyword mit Volumen ("steuerstrafrecht ratgeber": keine Daten, kein Autocomplete-Treffer). Typ-C-Gate, keine Benchmark-Pflicht.

Die Autorenfrage (Dr. Stürzl oder Dr. Glogger) bleibt bei allen drei Beiträgen offen und ist ein gelber Platzhalter.

## Korrektur des Hauptagenten (Adresse, Zeiten, Notfallnummern)

Meine vier Seiten enthielten keine Platzhalter zu Adresse, Parken, Telefonzeiten oder Notfallnummern. Es wurde kein Platzhalter entfernt. Geändert: Die Telefonnummern im Abschluss-CTA (Frankfurt +49 69 298028870, München +49 89 72444170) tragen jetzt die Quelle "Source of Truth Tab 00 / nap.json" im Claim C03. Keine Adresse, keine Öffnungszeiten und keine alte Adresse stehen im Text. Das Snapshot `source-of-truth-2026-10-11.md` wurde nach Ratgeber-relevanten Fakten durchsucht: keine neuen Fakten für die Beiträge.

## Neue Widersprüche im Kundenmaterial und in den Vorgaben

1. **Keyword-Konflikt:** Der Sitetree gibt ST-34 und ST-35 dasselbe Keyword "steuerhinterziehung strafe" (Regel S6). Entscheidung dieses Laufs: ST-35 behält es, der Hub nimmt "steuerstrafrecht ratgeber". Martin entscheidet.
2. **Live-FAQ gegen Gesetz:** Die Live-FAQ erklärt "vorbestraft" mit über 90 Tagessätzen oder mehr als 3 Monaten. Im Text steht stattdessen § 32 Abs. 2 Nr. 5 BZRG (Führungszeugnis). Die Live-FAQ nennt außerdem Folgen (Waffen-, Jagdverbot, Passentzug) ohne Norm: als Kanzleiaussage übernommen und im Flag markiert.
3. **Influencer-Beitrag:** Pool und Sitetree nennen ihn als Krypto-Material. Der Beitrag (18.07.2025) handelt von Social-Media-Einnahmen, nicht von Krypto. Nicht verwendet.
4. **BMF-Schreiben:** Es gilt das Schreiben vom 6. März 2025 (BStBl I S. 658), es ersetzt das vom 10. Mai 2022.
5. **Live-FAQ Wortschatz:** "Worst Case Szenario", "Ihre Freiheit steht auf dem Spiel", "exzellenter Ruf", "Spezialisierung", "Leidenschaft" stehen nicht in den Texten (Angst- und Werbewörter, BRAO).

## Vorschläge für Regeln und Skripte im Skill

1. **check_legal.py / legal-terms.json:** Die Regel "Superlativ / Marktführer" trifft `nr\.? ?1`. Sie schlägt bei jedem Gesetzeszitat "Nr. 1" oder "Nr. 12" an (ST-36 hatte vier Treffer). Die Regel soll nur "Nr. 1" ohne vorangehendes "Abs." oder "Satz" und ohne folgende Ziffer treffen, oder Zitate in "§ ..."-Zusammenhang ausnehmen. Bis dahin schreibe ich "Nummer".
2. **run_gates.py (G6) und Blog:** `money_page: true` verlangt `nap_file`, und `schema_tool.py` bricht bei Platzhaltern für Autor und Datum ab. Blogs mit offenem Autor brauchen ein Brief-Feld wie `schema_pending: true`. Außerdem erzwingt für Blogs nichts die 70-%-Untergrenze (ich prüfe sie mit `wordcount.py --median --money`).
3. **deslop_de.py:** Die Dreier-Reihung zählt Sachaufzählungen wie "Mining, Staking und Lending". Gesetzeslisten sollten eine Ausnahme bekommen oder die Schwelle liegt bei vier.
4. **diff_claims.py diff:** Es prüft keine Kundenwendungen. Der Cleanse strich "kein Kavaliersdelikt, sondern eine Straftat" trotz der Regel im Prompt. Vorschlag: `brief.own_phrases` als Pflicht-Liste prüfen.
5. **Blog-Vorlage:** Sie kennt keine Tabelle im Blog und keine Hub-Seite mit Karten. Die Sektionstypen `table` und `el-grid` liefen im Skript ohne Fehler, stehen aber nicht in Abschnitt 7 der Page-Templates.
6. **seo_coverage.py PAA-Check:** Die Treffer hängen am 5-Buchstaben-Präfix. Fragen mit Zahlen ("10000 Euro") lassen sich nur über die Überschrift abdecken. Das hat funktioniert, sollte aber im Skill stehen.
7. **Skill-Datei:** Schritt 6 steht doppelt ("Fresh reviewer and SEO audit" und "Fresh reviewer").

## Rechtsgrauzonen (Details in `OPEN-FLAGS.md` je Ordner)

- ST-35: BGH-Wertgrenzen stammen aus dem Urteil von 2008. Neuere Rechtsprechung nicht gelesen. Aussagen zu Nebenfolgen und Schweigerecht stammen aus der Live-FAQ ohne Norm. "Steuerhinterziehung gehört zu § 369 Abs. 1 Nummer 1 AO" ist ein Schluss aus dem Gesetzestext.
- ST-36: Beginn der Verfolgungsverjährung (Beendigung der Tat) ist ohne gelesene Rechtsprechung als Einzelfall formuliert. "37,5 Jahre" und "zehn Jahre" im Grundfall sind eigene Rechnungen aus § 376 Abs. 3 AO und § 78c Abs. 3 StGB.
- ST-37: Steuerrechtliche Aussagen nach BMF-Schreiben und § 23 EStG. Das BFH-Urteil IX R 3/22 wird nur über das BMF-Schreiben genannt. Allgemeine Steuerberatung ist laut Baseline keine belegte Leistung der Kanzlei, darum nimmt der Text keine Einordnung des Einzelfalls vor.
- Alle drei Beiträge: Das Wort "Straffreiheit" und "straffrei" kommt nicht vor (LR10). Titel von Dr. Stürzl stammen aus dem Lebenslauf (kein Kammernachweis).
- ST-34: Der Hub darf erst live, wenn ST-35 bis ST-37 und ST-18 stehen (Links).

## Dateien je Ordner

`01-brief/` (brief.json, claims.json, gate-a0.md) · `02-outline/outline.md` · `03-draft/` (draft-v1.md, draft-v2.md, Cleanse-Dateien) · `04-gates/gates.md` · `05-final/` (page.md, cms-blocks.txt, placeholders.md) · `OPEN-FLAGS.md` · `_status.md` · `_run.json` · `_work/` (SERP, Benchmark, Gesetzestexte, BGH-Urteil, BMF-Schreiben, KStTG).
