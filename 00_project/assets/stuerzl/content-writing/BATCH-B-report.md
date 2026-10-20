# Batch B: Bericht (Säule, Gutachten, Hub, FAQ)

Datum 2026-10-11. Agent: Schreib-Agent Batch B. Anweisung: `00_project/content-writing-stuerzl-batch.md`. Nichts ist live, nichts auf Drive, Portal oder CMS. Der Reviewer-Schritt ist nicht gelaufen (Hauptagent).

## Tabelle je Seite

| ID | Seite | Wörter | Bestand | Wettbewerber-Median (Seiten) | G1 | G2 | G3 | G4 | G5 | G6 | Platzhalter | Cleanse-Aufrufe | Kosten USD | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-11 | Steuerstrafrecht (Säule) | 1752 | 217 | 1408 (13) | pass | pass | pass | pass | pass 5/5 | pass | 1 | 1 | 0 | fertig, Freigabe offen |
| ST-13 | Gutachten und Risikobewertung | 1216 | 282 | 888 (12) | pass | pass | pass | pass | pass 5/5 | pass | 2 | 1 | 0,0035 | fertig, Freigabe offen |
| ST-10 | Leistungen (Hub, Typ C) | 512 | 152 | Referenz 466 (10 Hubs), keine Untergrenze | pass | pass | pass | pass | pass 5/5 | pass | 0 | 1 | 0 | fertig, Freigabe offen |
| ST-32 | FAQ | 2616 | 2555 (1807 ohne Kostenteil) | 1481 (16) | pass | pass | pass | pass | pass 5/5 | pass | 0 | 1 | 0,0035 | fertig, Freigabe offen |

Alle vier Seiten haben die Gates G1 bis G6 bestanden (`run_gates.py` auf `05-final/page.md`). Die Skill-Dateien wurden während des Laufs um G6 erweitert (SEO/GEO-Abdeckung, Schema, Link-Netz). G6 gilt in dieser Tabelle mit. Summe Kosten: 0,007 USD. Cleanse insgesamt 4 Aufrufe (1 je Seite).

Seller-Layer ohne Vertiefung und FAQ: ST-11 524 Wörter, ST-13 489 Wörter (Grenze 550). Die FAQ-Blöcke zählen wie im Referenzlauf extra.

Ordner: `/Users/martindrendel/741website/00_project/assets/stuerzl/content-writing/st-11-steuerstrafrecht/`, `st-13-gutachten-risikobewertung/`, `st-10-leistungen/`, `st-32-faq/`. Je Ordner: `05-final/page.md`, `cms-blocks.txt`, `placeholders.md`, `schema.jsonld`, `measure-plan.md`, dazu `04-gates/gates.md`, `OPEN-FLAGS.md`, `_status.md`, `_run.json`.

## Was blockiert wurde

Nichts. Keine Seite ohne Daten. Hinweise:

- ST-13: Das Pool-Item CP-SVC-011 hat keine Keywords und keine Nachfrage-Daten. Das Sitetree-Keyword 'tax compliance' (590) gehört im Pool zu CP-SVC-012 (ST-26). Die SERP für 'tax compliance' ist rein informativ (Steuerberater, Lexika). Der Autocomplete-Baum fehlt, die SERP ersetzt ihn (Gate-Zeile 3 "teilweise").
- ST-10: Typ C, es gibt keinen Benchmark. Für G6 wurden 10 Wettbewerber-Hubs als Referenz gemessen.

## Entfernte Platzhalter nach der Korrektur des Hauptagenten (Adresse, Parken, Zeiten, Notfallnummern)

Keine. Meine vier Seiten enthielten nie Platzhalter zu Adresse, Parken, Telefonzeiten oder Notfallnummern. Ich habe die bestätigten Büros und Adressen (Source of Truth Tab 00, `nap.json`) in die Claims aufgenommen (ST-11 C28, ST-13 C17, ST-10 C06, ST-32 C25). Das Schema (`schema.jsonld`) trägt jetzt die Straße Untermainkai 26 für Frankfurt. Im Text stehen weiter nur die Ortsnamen und die Telefonnummern, keine Zeiten. Die alte Adresse Wiesenhüttenstraße kommt nirgends vor.

Offene Platzhalter (bleiben): Pauschale der Erstberatung (ST-11 S06, ST-13 S06), Tax-Compliance-Systeme als Leistung (ST-13 S07). ST-10 und ST-32 haben keine.

## Neue Widersprüche im Kundenmaterial

1. Live-FAQ nennt den Einleitungsvermerk ein "behördliches Schreiben". § 397 Abs. 2 AO verlangt einen Aktenvermerk (Mitteilung an den Beschuldigten: Abs. 3). Die FAQ folgt dem Gesetz.
2. Live-FAQ "vorbestraft ab über 90 Tagessätzen": vereinfacht. Ersetzt durch § 32 Abs. 2 Nr. 5 und § 53 BZRG.
3. Live-FAQ "ab dem ersten Tag ... Steuerhinterziehung durch Unterlassen": vom Gesetzeswortlaut nur als "kann" gestützt. Abgeschwächt.
4. Der Compliance-Text der Kanzlei nennt "Steuer" nicht, Dr. Stürzl hat aber zu Tax Compliance veröffentlicht (Live-Profil). Ob die Kanzlei Tax-CMS anbietet, ist offen.
5. Der KI-Baustein enthält die absolute Zusage "allen datenschutzrechtlichen und berufsständischen Anforderungen gerecht". Nicht übernommen.
6. Bekannt aus dem Referenzlauf und hier bestätigt: Kostenmodell (RVG gegen Zeitaufwand), drei Fassungen der Erstberatung, Live-Wörter wie "Spezialisierung", "Expertise", "bestmögliche", "garantieren ... höchstem Niveau".
7. Der Kostenteil II der Live-FAQ (748 Wörter) entfällt. Das Thema Rechtsschutz geht dabei verloren.

## Rechtsgrauzonen (Details je Seite in OPEN-FLAGS.md)

- ST-32: Fünf Aussagen der Kanzlei ohne gelesene Gesetzes- oder Rechtsprechungsquelle, mit "kann" übernommen: Nebenfolgen einer Verurteilung, Vorsatzdefinition, "Schweigen darf nicht als Schuldeingeständnis gewertet werden", Behörden-Kurzbeschreibungen, Hinterziehung durch Unterlassen bei verspäteter Abgabe. Hoeneß-Beispiel gestrichen (keine Quelle).
- ST-11, ST-13, ST-10: H1 "Anwalt für Steuerstrafrecht" (Fachgebietsangabe), Titel von Dr. Stürzl aus dem Lebenslauf, Dritte als Mit-Autoren genannt (Rolletschke, Schwartz), hohe Bußgeldzahlen aus § 130 und § 30 OWiG ("eine Million", "zehn Millionen") ohne Angstwörter.
- Alle vier: Die Live-Seiten nutzen verbotene Wörter. Sie stehen nur in `OPEN-FLAGS.md`.
- ST-32: Neue Gesetzes-Zusätze, die nicht in der Live-FAQ stehen (Einspruchsfrist zwei Wochen § 410 StPO, Bewährung § 56 StGB, Verjährung). Die Kanzlei prüft, ob sie sie möchte.

## Keyword- und Link-Hinweise (Regel S6, für den Hauptagenten)

- 'anwalt steuerstrafrecht' steht im Sitetree bei ST-00, ST-10 und ST-11. ST-11 behält es. ST-10 nutzt 'leistungen steuerstrafrecht'. ST-00 (freigegebene CRO-Fassung) trägt es ebenfalls. Martin entscheidet.
- 'tax compliance' bei ST-13 und ST-26: ST-26 nutzt jetzt 'compliance beratung'. Kein exakter Konflikt, aber Themen-Nähe.
- 'steuerstrafverfahren' bei ST-12 und ST-32: ST-12 behält es, ST-32 nutzt 'steuerstrafverfahren ablauf'.
- Links auf Seiten mit Status "Vorschlag" (/ratgeber/steuerhinterziehung-strafe/, /ratgeber/verjaehrung/ in ST-11 und ST-32) und auf /compliance/ (ST-10, ST-13) müssen entfallen, wenn die Ziele nicht gebaut werden.
- `link_network.py --final` ist nicht gelaufen (ein Lauf schreibt `LINK-NETWORK.md` in das gemeinsame Verzeichnis). ST-11 und ST-32 zitieren Gesetzestexte nah am Wortlaut. Die Ähnlichkeit zu ST-12, ST-14 und ST-18 muss der Hauptagent prüfen (Grenze 25 %).

## Vorschläge für Regeln im Skill

1. G6 H5 vergleicht die ersten fünf Buchstaben. Ein Hauptkeyword, das mit "steue" beginnt (zum Beispiel 'steuerstrafrecht'), trifft fast jede Überschrift und scheitert zu Unrecht. Besser: ganzes Wort oder Stamm mit mindestens 8 Buchstaben.
2. `legal-terms.json` blockiert "bestem" in der Gesetzesformel "nach bestem Wissen und Gewissen" (§ 150 Abs. 2 AO). Zitate aus Gesetzen brauchen eine Ausnahme oder eine Paraphrase-Regel.
3. `legal-terms.json` blockiert "Nr. 1" (Superlativ), trifft aber "Nr. 1 bis 6" in Paragrafenangaben. Muster auf "Nr. 1" ohne Paragraf davor eingrenzen.
4. G6 zählt die Überschrift der Direkt-Antwort als Satz (Frage mit "?"). Eine Frage-Überschrift kostet damit einen der vier erlaubten Sätze.
5. Die Seller-Layer-Grenze (550 Wörter) hat kein Skript. Vorschlag: `validate_page.py` summiert S01 bis S06 und S09 ohne FAQ und Akkordeon.
6. Für FAQ-Seiten fehlt ein Seitentyp-Hinweis zu Bestand ohne entfallene Teile. `bestand_words` im Brief mit Begründung hat funktioniert; ein Feld `bestand_note` wäre sauberer.
7. Die Typ-C-Seite (Hub) braucht für G6 einen Benchmark-Eintrag. Sonst scheitert `seo_coverage.py`. Vorschlag: Typ C von der Benchmark-Pflicht ausnehmen.

## Sonstiges

- Die Skill-Dateien wurden von einem anderen Prozess um 13:06 aktualisiert (G6, `schema_tool.py`, `nap.json`, `slugs.json`). Ich habe alle vier Seiten gegen die neue Fassung geprüft.
- Wörter nur mit `wordcount.py` gezählt. Gesetzestexte liegen in `_work/law/` jedes Ordners, gelesen am 2026-10-11.
