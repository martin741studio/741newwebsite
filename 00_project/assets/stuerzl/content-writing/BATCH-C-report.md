# Batch C: Unternehmen und Compliance (Bericht, 2026-10-11)

Schreib-Agent Batch C. Seiten ST-21, ST-26, ST-20, ST-23. Alles nur lokal. Kein Upload, keine Änderung an Website, Portal, CMS oder an fremden Dateien. Der Reviewer-Schritt wurde nicht ausgeführt (Hauptagent).

Stand der Regeln: Der Skill wurde um 13:06 während des Laufs erweitert (Gate G6, `nap.json`, `slugs.json`, `paa_questions`). Alle vier Seiten erfüllen die neue Fassung. Die Korrektur zur Adresse (Untermainkai 26 bestätigt) ist eingearbeitet.

## Ergebnis je Seite

| ID | Seite | Wörter (gesamt) | Seller-Layer (S01-S06, S09) | Bestand | Wettbewerber-Median (Untergrenze 70 %) | G1 | G2 | G3 | G4 | G5 | G6 | Platzhalter | Cleanse | Kosten USD | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ST-21 | Unternehmensvertretung | 1.520 | 554 | 291 | 1.083,5 (758), 6 Seiten | pass | pass | pass | pass | 5/5 | pass | 2 | 1 | 0,0935 | fertig, Freigabe offen |
| ST-26 | Compliance (neu) | 1.474 | 553 | keiner (404) | 853,5 (597), 14 Seiten | pass | pass | pass | pass | 5/5 | pass | 2 | 1 | 0,097 | fertig, Freigabe offen |
| ST-20 | Wirtschaftsstrafrecht | 1.361 | 543 | 142 | 780 (546), 13 Seiten | pass | pass | pass | pass | 5/5 | pass | 2 | 1 | 0,000 | fertig, Freigabe offen |
| ST-23 | Ordnungswidrigkeiten | 1.434 | 526 | 229 | 1.083 (758), 12 Seiten | pass | pass | pass | pass | 5/5 | pass | 2 | 1 | 0,097 | fertig, Freigabe offen |

Kosten: Gesamt 0,2875 USD (Suchvolumen 0,09 je Seite außer ST-20, SERP 0,0035 je Abruf). Alle Seiten liegen weit unter 1 USD. Cleanse: je Seite 1 Aufruf mit codex, Diff bestanden, nur kleine Änderungen übernommen. Die Seitenwörter kommen aus `wordcount.py` und `secwc` (gleiche Zählweise).

Die 550-Wörter-Grenze für den Seller-Layer halten die Seiten ein, wenn S08 (FAQ) nicht mitzählt (526 bis 554, ST-21 und ST-26 liegen 3 bis 4 Wörter darüber). Mit FAQ liegen sie bei etwa 800 bis 940. Siehe Vorschlag 1.

Dateien je Seite (alle in `/Users/martindrendel/741website/00_project/assets/stuerzl/content-writing/<ordner>/`): `01-brief/` (brief.json, claims.json, gate-a0.md), `02-outline/outline.md`, `03-draft/` (draft-v1, cleansed-r1, draft-v2), `04-gates/` (gates.md, gates.json, g6-hinweise.md), `05-final/` (page.md, cms-blocks.txt, placeholders.md, schema.jsonld, measure-plan.md), `OPEN-FLAGS.md`, `_run.json`, `_status.md`, `_work/` (Live-Texte, Gesetzestexte unter `_work/law/`, SERPs, Benchmark, Autocomplete). Ordner: `st-21-unternehmensvertretung`, `st-26-compliance`, `st-20-wirtschaftsstrafrecht`, `st-23-ordnungswidrigkeiten`.

## Was blockiert wurde

Nichts. Kein Seiten-Blocker.

Einschränkungen, die keine Blocker sind:

1. **ST-21:** Das Sitetree-Keyword war leer. "unternehmensvertretung" hat in DataForSEO keine Daten. Ich habe 24 Begriffe geprüft und "unternehmensstrafrecht" (70) gewählt. Die Suchabsicht ist gemischt (Lehrbuch, Politik). Martin entscheidet (OPEN-FLAGS C1).
2. **ST-26:** Der Sitetree-Auftrag lautet "tax compliance" (590). Der Kundentext nennt Steuer nicht. Ich habe "compliance beratung" (140) als Hauptbegriff gesetzt und "Tax Compliance" über einen Gesetzes-Block (§ 153 AO) und Dr. Stürzls Veröffentlichungen abgedeckt. Es gibt keine erfundene Tax-CMS-Leistung. Offene Frage an die Kanzlei steht als Platzhalter 2.
3. **ST-22 (Unterseiten) und ST-24:** haben in `slugs.json` keinen Slug. Deshalb verlinken ST-21 und ST-23 sie nicht. Die Unterseiten tragen heute den gleichen langen Einleitungstext wie ihre Hauptseite.

## Neue Widersprüche im Kundenmaterial

1. Der Bestand zu Ordnungswidrigkeiten sagt, auch "unbeabsichtigte Fehler" könnten eine Ordnungswidrigkeit sein. § 378 AO verlangt Leichtfertigkeit. ST-23 folgt dem Gesetz.
2. Der Bestand zur Strafanzeige sagt, unvollständige Angaben könnten falsche Verdächtigung sein. § 164 StGB verlangt "wider besseres Wissen". ST-21 folgt dem Gesetz.
3. Der Kundentext Compliance sagt "Haftung vermeiden", "im Einzelfall sogar vermeiden", "maßgeblich" und "ganzheitliche Verteidigungsstrategie". Nicht übernommen (BRAO, Ergebnisnähe).
4. Dr. Gloggers Profil führt Veröffentlichungen unter dem Namen "Werndl", darunter einen Beitrag zur Haftung von Vorständen für Aufsichtsmängel (2017). Nicht genutzt, bis die Namensfrage geklärt ist.
5. Dr. Glogger heißt auf dem Profil "Salary Partnerin" mit Fußnote "Angestellte Rechtsanwältin". Die Texte sagen nicht "Partnerin".
6. Der Bestand zu "Überahme von Geldbußen / Verteidigungskosten für Mitarbeiter" (ST-21) ist unklar. Was die Kanzlei damit meint, ist offen.
7. Weiter wie in der Anweisung: Vergütung "RVG" (Startseite) gegen "kein RVG" (Kundentext); Erstberatung in drei Fassungen; Rechtsschutz/Versicherung fehlt im Kostentext.

## Entfernte Platzhalter nach der Adress-Korrektur

Keine. Meine vier Seiten enthielten nie Platzhalter zu Adresse, Parken, Telefonzeiten oder Notfallnummern. Sie nennen nur beide Telefonnummern (bestätigt). In `placeholders.md` stehen nur die Pauschale der Erstberatung, die Kostenübernahme/Rechtsschutz (ST-21, ST-20, ST-23, ST-26 ohne diesen Punkt) und bei ST-26 die Tax-CMS-Frage. Das Schema (`schema.jsonld`) wurde nach der Korrektur neu erzeugt und enthält jetzt die Straße in Frankfurt.

Offene Platzhalter je Seite:

| Seite | Platzhalter |
| --- | --- |
| ST-21 | Pauschale Erstberatung; Kostenübernahme durch Rechtsschutz, D&O oder Unternehmen |
| ST-26 | Pauschale Erstberatung; ob Tax CMS als Leistung genannt werden soll |
| ST-20 | Pauschale Erstberatung; Rechtsschutz und Kostenübernahme durch ein Unternehmen |
| ST-23 | Pauschale Erstberatung; Rechtsschutz und Kostenübernahme durch ein Unternehmen |

## Rechtsgrauzonen (Details in den OPEN-FLAGS der Seiten)

1. "Anwalt für Wirtschaftsstrafrecht" (ST-20, H1 und Title) und "Unternehmensstrafrecht" (ST-21, H1): Fachgebiets-Wirkung (§ 7 BORA). Keyword braucht die Wendung.
2. Wirkung von Compliance-Strukturen (ST-26, ST-23): "können schützen", "können helfen" statt der Zusagen im Kundentext.
3. Eigene Wendungen der Kanzlei ("möglichst geräuschlos", "langjährige Erfahrung") stehen mit "möglichst" beziehungsweise ohne Zahl. Kanzlei prüft.
4. Gesetzliche Höchstbeträge (zehn Millionen Euro, 50.000 Euro) stehen sachlich mit Norm. Ton prüft Martin.
5. ST-20 Insiderhandel: § 119 WpHG gelesen, die Marktmissbrauchsverordnung (Art. 14) nicht. ST-23: § 130 Abs. 3 OWiG als "bis zu einer Million Euro" vereinfacht.
6. Die Live-Seite nutzt weiter "Expertise", "Kernkompetenz", "bestmöglich", "kompetente", "essenziell", "hart in der Sache". Nicht übernommen. Hinweis an Martin (Un-Burning D11).

## Vorschläge für den Skill

1. **Seller-Layer-Grenze:** Klarstellen, ob S08 (FAQ) in die 550 Wörter zählt. Die Referenzseite liegt mit FAQ bei 1.057. Mit 8 bis 10 FAQ-Antworten ist 550 mit S08 nicht erreichbar. Vorschlag: Grenze gilt für S01 bis S06 und S09. Das Gate G3 sollte sie prüfen (heute prüft es nur die Untergrenze).
2. **G6 H5 (Keyword-Stuffing):** Die Prüfung nutzt 5-Buchstaben-Präfixe. Ein Keyword wie "unternehmensstrafrecht" trifft damit jede Überschrift mit "Unternehmen" (12 von 20 Überschriften). Ich musste Überschriften umschreiben. Besser: volles Wort oder Wortstamm ab 8 Buchstaben.
3. **check_style "Sprecher gemischt":** zählt "ich" und "mein" in FAQ-Fragen aus Leserperspektive ("Bleibt meine Anfrage vertraulich?"). Fragen-Überschriften sollten ausgenommen werden.
4. **Lint G5:** Der Cleanse erzeugt gern Satzfragmente mit "Und" am Anfang. Ein Prüfpunkt "Satz beginnt mit Und" und "Satzfragment" würde das früh finden.
5. **Brief-Schema:** Ein Feld `benchmark_set` (welche URLs in den Median gehen) fehlt. Heute wird der Median von Hand aus `bench-metrics.json` gewählt, während G6 alle Seiten der Datei für Themen-Hinweise nutzt.
6. **Readiness:** Schritt 0 braucht eine Regel für Sitetree-Knoten ohne Keyword (ST-21: leer). Vorschlag: Volumen-Prüfung von 20 bis 25 Kandidaten (0,09 USD) als Pflichtzeile in A0, Entscheidung für Martin im Outline.
7. **`link_network.py`:** schreibt `LINK-NETWORK.md` in den gemeinsamen Ordner. Ich habe es nicht ausgeführt, weil es fremde Dateien berührt. Der Hauptagent führt es nach dem Batch mit `--final` aus.
8. **A0-Tabelle Autocomplete:** Der Pool-Baum und eigene Läufe zählen verschieden (eindeutig je Seed oder gesamt). Ein Skript, das die Zahl in `gate-a0.md` schreibt, vermeidet Zählfehler.
9. **Kundenmaterial als Quelle:** Ein Feld `claims.json: source_type` (Gesetz, Live-Seite, Kundentext, Profil) würde den Reviewer-Check beschleunigen.

## Hinweise für den Hauptagenten

1. Die vier Seiten verlinken gegenseitig: ST-21 auf ST-20, ST-23, ST-26, ST-18, ST-13, ST-31, ST-45, ST-46; ST-26 auf ST-21, ST-23, ST-14, ST-13, ST-31, ST-45, ST-46; ST-20 auf ST-11, ST-21, ST-23, ST-25, ST-28, ST-26, ST-31, ST-45, ST-46; ST-23 auf ST-14, ST-26, ST-21, ST-31, ST-45. Alle Ziele stehen in `slugs.json`. Die Ziele ST-11, ST-13, ST-14, ST-18, ST-25, ST-28, ST-31, ST-45, ST-46 gehören zu anderen Batches oder zur Vorlaufseite.
2. Keyword-Überschneidung: ST-21 und ST-23 teilen das Thema Organisationsverschulden. ST-21 verlinkt dafür auf ST-23 und führt kein eigenes Keyword. ST-26 und ST-23 teilen § 130 OWiG, aber mit unterschiedlicher Suchabsicht.
3. Gesetzestexte (gelesen 2026-10-11, gesetze-im-internet.de) liegen in `_work/law/` jeder Seite: OWiG § 17, 30, 31, 47, 67, 130; AO § 153, 370, 371, 377, 378, 379, 384, 409, 410; StPO § 55, 68b, 136, 137, 146, 152, 158, 161a; StGB § 14, 164, 203, 263, 264, 266, 283; GVG § 74c; InsO § 15a; WpHG § 119; HinSchG § 12, 16, 17; BRAO § 43a.
