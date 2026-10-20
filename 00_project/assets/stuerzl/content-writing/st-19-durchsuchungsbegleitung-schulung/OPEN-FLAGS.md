# OFFENE FLAGS FÜR DEN NÄCHSTEN AGENTEN (Stürzl, Durchsuchungsbegleitung und Schulung, ST-19)

Lies diese Datei, bevor du an dieser Seite weiterarbeitest. Stand nach der Korrekturrunde 2026-10-11 (Review REVIEW-A). Die Vorversion des Textes liegt in `05-final/page-vorreview.md`. Fragen an die Kanzlei stellen wir erst, wenn sie alles zur Bestätigung bekommt (Entscheidung Martin).

## A. Rechtsgrauzonen (BRAO / UWG), nicht vom Agenten zu entscheiden

| # | Stelle im Text | Frage | Aktueller Stand |
| --- | --- | --- | --- |
| A1 | S02, S07 Block 1, FAQ 1: "Bei anderen Personen und Unternehmen, die selbst nicht verdächtig sind, gelten engere Voraussetzungen (§ 103 Abs. 1 StPO)" | § 103 spricht von "anderen Personen". Dass ein nicht verdächtiges Unternehmen darunter fällt, ist übliche Auslegung, steht aber nicht im Gesetzestext. | Text steht so. Kanzlei bestätigt. |
| A2 | früher S07 Block 3: "Aus einem Zeugen kann schnell ein Beschuldigter werden. Manchmal versucht man auch, eine Person bewusst im Zeugenstatus zu halten, denn als Zeuge muss man aussagen" | Live-Aussage ohne Beleg, Unterstellung gegenüber Behörden, und "muss man aussagen" stimmt bei Befragung durch Polizei nicht ohne Weiteres. | **Gestrichen.** Statt dessen stehen die Rechte nach §§ 55, 68b, 136, 161a, 163 StPO. |
| A3 | S07 Block 2 (neu): "Verhalten bei einer Durchsuchung im Unternehmen: Was das Gesetz regelt" | Allgemeine Information aus §§ 94, 98, 105, 106, 107, 136 StPO, eingeleitet mit "allgemeine Informationen ... im Einzelfall". Aufforderungen an Mitarbeiter sind vermieden (Fix-Auftrag Punkt 7). Der Hinweis "Wer im Unternehmen diese Rolle übernimmt, lässt sich vorab festlegen" und "Mitarbeiter können die Beamten nach der Anordnung fragen" sind praktische Hinweise ohne eigene Norm. | Text steht so. Kanzlei prüft. |
| A4 | S01, S04 Schritt 4, FAQ 6: Notfallkontakt am Telefon, danach Klärung der Anwesenheit vor Ort | Neu festgelegt: Die Kanzlei berät zuerst am Telefon und klärt danach, ob eine Anwesenheit vor Ort möglich ist. Kein Versprechen einer Begleitung in H1, Title, Meta und Hero. Title heißt jetzt "Schulung & Notfall" (60-Zeichen-Grenze), H1 "Schulung und Notfallkontakt". Der Slug und der Seitenname "Durchsuchungsbegleitung" bleiben (Sitetree). | Text folgt der Vorgabe. Die Kanzlei bestätigt. Gleiche Linie auf ST-18. |
| A5 | **Die Live-Seite selbst** nutzt "nicht in Panik verfallen" und "24/7". | Panik ist ein Angst-Wort in unserer Liste. "24/7" ist unbelegt. | Nicht übernommen. |

## B. Widersprüche im Kundenmaterial, die vor Livegang gelöst sein müssen

| # | Widerspruch | Quellen | Stand |
| --- | --- | --- | --- |
| B1 | Vergütung: freigegebene Startseite "nach RVG", neuer Kundentext "kein RVG, nach Zeitaufwand". | `approved-copy.md` gegen `kosten.txt` | Diese Seite folgt dem neuen Kundentext, ohne Beträge. |
| B2 | Erstberatung: Kanzlei-Seite "Festpreis", Kundentext "Pauschale 250 bis 350 Euro". | `kanzlei.txt`, `kosten.txt` | Der Platzhalter für den Betrag ist gestrichen (Fix-Auftrag Punkt 3). Der Betrag steht nur auf /kosten/ (ST-31). |
| B3 | Notfallnummern: öffentlich, Besetzungszeiten nirgends dokumentiert. | Live-Kontaktseite | Nummern im Text, keine Zeiten. |
| B4 | Schulungsinhalt, Format, Dauer, Preis: nirgends dokumentiert. | Live-Seite ST-19 | Platzhalter 1 (S04 Schritt 2). Die Seite beschreibt nur die Aussagen der Live-Seite. |
| B5 | Sitetree: ST-19 hat kein Keyword. Die Wettbewerber-Seiten sind überwiegend Verhaltens-Ratgeber und Seminaranbieter, kaum Kanzlei-Leistungsseiten. | Pool, SERP | Keyword gewählt (Entscheidung Martin). |

## C. Workflow-Hinweise

1. Cleanse (codex) in der Korrekturrunde: Der Aufruf ist am Nutzungslimit von codex gescheitert (siehe `03-draft/cleanse-notes-fix.txt`). Es gibt keine Cleanse-Fassung. Lint G5 ist 5/5. Ein Cleanse nach dem Limit-Ende (17:20 Uhr laut Fehlermeldung) bleibt möglich; dann `diff_claims.py diff` prüfen.
2. Link-Ziele ST-18, ST-21, ST-26, ST-29, ST-31, ST-45 sind erst gültig, wenn die Zielseiten live sind. ST-26 (Compliance) ist ebenfalls ein Batch-Auftrag.
3. Diese Seite ist ein Kind von ST-18 und teilt die Notfallnummern und mehrere Gesetzesstellen mit ihr. Der Inhalt ist nicht kopiert, sondern auf Betriebe zugeschnitten (S07 Blöcke 1 bis 4). Die Seite wird jetzt von ST-18, ST-12 und ST-29 verlinkt.
4. `brief.word_range` oben von 1400 auf 1600 erhöht (neuer Abschnitt zum Verhalten der Mitarbeiter).
5. Person und Service im Schema kommen aus `_work/add-schema.py`, nach jedem Lauf von `run_gates.py` neu starten.
