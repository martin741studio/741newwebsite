# Gate A0 (voll): Stürzl, Steuerfahndung und Durchsuchung (ST-18)

Datum: 2026-10-11. Seitentyp A (Geldseite, Akutseite). Neue Seite, kein Bestand.

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste, Adressen) | ja | `content-pool/01-client/client-baseline.md`, `assets/stuerzl/nap.json`, `source-of-truth-2026-10-11.md`, `cro/04-copy/approved-copy.md`, 2026-10-11. Frankfurt Untermainkai 26 und beide Notfallnummern gelten als bestätigt (Koordinator, 2026-10-11). |
| 2 | Live-Bestand abgerufen und gezählt | ja, keiner | ST-18 ist neu. Verwandte Live-Teile: Kurzabsatz "Begleitung von Durchsuchungen" auf der Seite Verteidigung im Steuerstrafverfahren (3 Sätze), Live-FAQ I.3 und V (Durchsuchungsbeschluss, Schweigerecht), Live-Kontaktseite (Notfallnummern). Rohtexte in `selbstanzeige/_work/live/`. |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 260 Treffer für "steuerfahndung" (z. B. "steuerfahndung vor der tür", "steuerfahndung was tun", "steuerfahndung rechte", "steuerfahndung durchsuchungsbeschluss", "wann kommt die steuerfahndung", "was darf die steuerfahndung mitnehmen"), `content-pool/03-demand/autocomplete.json`, 2026-10-11. |
| 4 | Ziel-Keyword und Suchvolumen | ja | "steuerfahndung anwalt": DataForSEO ohne Daten (heißt: keine Daten, nicht keine Nachfrage). Umfeld: steuerfahndung 6.600; steuerfahndung münchen 210; steuerfahndung hessen 140; steuerfahndung frankfurt 50; wann kommt die steuerfahndung 40; steuerfahndung durchsuchung 30; hausdurchsuchung steuerfahndung 30; anwalt steuerfahndung 10. `content-pool/03-demand/volume.json` und `_work/volume.json` (google_ads/search_volume/live, de, 2276), 2026-10-11. Local-Falcon-Baseline 2026-10-01 (client-baseline.md): "steuerfahndung anwalt" SoLV 22,5 %. |
| 5 | SERP Top 10 | ja | `content-pool/02-competitors/serp-4.json` ("steuerfahndung anwalt") und `serp-10.json` ("steuerfahndung durchsuchung verhalten"), 2026-10-11. Verzeichnisse (anwalt.de, juraforum, branchenbücher) aus dem Wettbewerberset genommen. |
| 6 | Echte PAA-Fragen | ja | 12 Fragen aus serp-4, serp-10, serp-16 (siehe brief.json paa_questions: 5 beantwortet, 7 verworfen mit Grund). |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 31 von 31 Seiten gelesen, Median **1275** Wörter, 70-%-Untergrenze **892**. `_work/bench-metrics.json`, `_work/bench-table.md`, page_metrics.py, 2026-10-11. |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Akutseite. Büros werden genannt. Standortbezug läuft über ST-41 und ST-42. |

## Messreihe Wettbewerber

Median 1275, 70 % = 892, Seiten 31 von 31
| Wörter | Seite |
| --- | --- |
| 5890 | https://www.hortmannlaw.com/steuerfahndung-strafverfahren-selbstanzeige-anwalt |
| 3933 | https://rechtsanwaelte-wirtschaftsstrafrecht-berlin.de/steuerfahndung-und-zoll/ |
| 3454 | https://www.kanzlei-dannhauer.de/dienstleistungen/steuerstrafrecht/ |
| 2674 | https://www.kanzleimauss.de/steueranwalt-steuerhinterziehung/ |
| 2379 | https://www.bms-rechtsanwaelte.de/steuerstrafrecht |
| 2367 | https://www.cornea-franz.de/rechtsgebiete/steuerstrafrecht/ |
| 1762 | https://www.bildt-law.de/steuerstrafrecht |
| 1718 | https://www.strafrecht-bundesweit.de/verhalten-in-strafsachen/verhalten-bei-durchsuchung/ |
| 1716 | https://www.martin-anwaelte.de/leistung/steuerhinterziehung/ |
| 1649 | https://www.die-steuerstrafverteidiger.de/brennpunkte/berater-fuer-berater/hinweise-zur-durchsuchung-und-beschlagnahme-in-steuerberaterkanzlei/ |
| 1565 | https://www.lhp-gruppe.de/steuerstrafverfahren/soforthilfe-bei-steuerfahndung-durchsuchung/ |
| 1510 | https://nh-legal.de/steuerfahndung-vor-der-tuer/ |
| 1414 | https://www.bms-rechtsanwaelte.de/steuerstrafrecht-blog/steuerfahndung-an-der-tuer-anfangsverdacht-durchsuchung |
| 1348 | https://www.bildt-law.de/durchsuchung-der-steuerfahndung |
| 1345 | https://www.rosepartner.de/steuerberatung/durchsuchung-steuerfahndung.html |
| 1275 | https://steuerberatung-niedersachsen.de/fachanwalt-steuerrecht-steueranwalt/finanzamt-fuer-steuerstrafsachen-und-steuerfahndung-koeln/ |
| 1273 | https://www.dnk-rechtsanwaelte.de/de/kompetenzen/steuerstrafrecht/ |
| 1237 | https://www.kwa-recht.de/durchsuchung-steuerfahndung |
| 1222 | https://www.juhn.com/fachwissen/steuerhinterziehung-selbstanzeige/steuerfahndung-und-durchsuchung/ |
| 1131 | https://www.dnk-rechtsanwaelte.de/de/blog/beitraege/hausdurchsuchung_durch_die_steuerfahndung_was_sie_jetzt_tun_sollten_und_was_nicht_e2445/ |
| 1037 | https://www.strafrecht.berlin/steuerstrafrecht/ |
| 966 | https://www.kanzlei-heilmann.de/steuerfahndung-rechte-und-pflichten-bei-einer-durchsuchung/ |
| 965 | https://port7.de/publikationen/durchsuchung-im-steuerstrafverfahren-hinweise-und-tipps/ |
| 811 | https://steuerdelikt.de/anwalt-steuerfahndung |
| 757 | https://ecovis-kso.com/blog/durchsuchung-steuerfahndung/ |
| 746 | https://steuerstrafrecht-patzschke.de/schwerpunkte/steuerfahndung |
| 642 | https://steuerdelikt.de/steuerfahndung/durchsuchung |
| 628 | https://steueranwaelte-hamburg.de/steuerstrafrecht |
| 625 | https://www.winheller.com/steuerrecht-steuerberatung/steuerstrafrecht.html |
| 458 | https://www.schomerus.de/aktuelles/hinweise-zum-verhalten-wenn-die-steuerfahndung-auftaucht |
| 410 | https://www.ra-hatle-westkamp.de/steuerstrafrecht/ |

## Wortzahl-Urteil

1616 Wörter eigene Seite, kein Bestand, 1275 Median (31 Seiten, page_metrics.py, 2026-10-11), Untergrenze 892, **ausreichend** (127 % des Medians). Seller-Layer ohne FAQ 554 Wörter (Regel: höchstens 550), Vertiefung 5 Blöcke, FAQ 6 Fragen.

## Konflikte im Material

1. Die Live-Kontaktseite nennt Telefonzeiten Mo bis Fr 9:30 bis 14:30. Für die Notfallnummern nennt keine Quelle Besetzungszeiten (Kanzlei-Seite: "bei Bedarf 24/7-Erreichbarkeit"). Die Seite verspricht keine Zeiten.
2. Begleitung vor Ort: Live-Seite "Begleitung von Durchsuchungen", Startseiten-Antwort F3 "klären wir im Telefonat". Die Seite folgt F3.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Keine Blocker.
