# Gate A0 (voll): Stürzl, Steuerstrafrecht Säulenseite (ST-11)

Datum: 2026-10-11. Seitentyp A (Geldseite, Säule). Quelle der Pool-Daten: `content-pool/` (Lauf 2026-10-11).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste) | ja | `content-pool/01-client/client-baseline.md`, `cro/04-copy/approved-copy.md`, `assets/stuerzl/voice.md`, `nap.json`, 2026-10-11. Endgültige Adresse Frankfurt offen: bleibt aus dem Text heraus. |
| 2 | Live-Bestand abgerufen und gezählt | ja | `/index.php/steuerstrafrecht`: 217 Wörter, 2×H1 ("Leistungen", "Steuerstrafrecht"), 0×H2. Inhalt: ein Absatz zur "Spezialisierung" plus vier Kacheln (Selbstanzeige, Gutachten, Durchsuchung, Verteidigung). `_work/bestand-metrics.json`, `_work/live/x_steuerstrafrecht.txt`, 2026-10-11 (page_metrics.py). |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 43 Treffer für die Familie 'anwalt steuerstrafrecht / steuerstrafrecht / anwalt steuerhinterziehung', `content-pool/03-demand/autocomplete.json` (Pool CP-SVC-005 `autocomplete_hits` 43), 2026-10-11. |
| 4 | Ziel-Keyword und Suchvolumen | ja | anwalt steuerstrafrecht 480; steuerstrafrecht 590; steuerstrafverfahren 260; anwalt steuerhinterziehung 210; steuerhinterziehung anwalt 210; rechtsanwalt steuerstrafrecht 170; steuerstrafverteidiger 20. `03-demand/volume.json`, DataForSEO 2026-10-11. Summe des Clusters 1.940 (Pool). |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | `02-competitors/serp-2.json` ('anwalt steuerstrafrecht', Deutschland), 2026-10-11. Verzeichnisse (anwalt.de) aus dem Wettbewerberset genommen, alle übrigen 12 Treffer gelesen. |
| 6 | Echte PAA-Fragen | ja | serp-2 liefert keine PAA. PAA der Cluster-SERPs: serp-3 ('anwalt steuerhinterziehung'), serp-4, serp-8 ('steuerstrafverfahren ablauf'), serp-9, serp-15. Im Brief unter `paa_questions` (8 beantwortet, 5 mit Grund verworfen). |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 13 von 13 gelesen (12 Treffer der SERP serp-2 plus mtrlegal Frankfurt aus dem Pool). Median **1408** Wörter, 70-%-Untergrenze **985**. Liste unten. `_work/bench-metrics.json`, 2026-10-11. |
| 8 | Lokaler Fakt (nur wenn Stadt Teil der Positionierung) | nicht nötig | ST-11 ist eine bundesweite Themenseite. Stadt-Positionierung läuft über ST-41 und ST-42. |

## Messreihe Wettbewerber (Seiten zu Steuerstrafrecht, serp-2)

| Wörter | Seite |
| --- | --- |
| 3774 | https://ffpv.de/expertise/steuerstrafrecht |
| 2296 | https://www.kk-strafrecht.de/fachbereiche/strafrecht/wirtschaftsstrafrecht-steuerstrafrecht-selbstanzeige |
| 2171 | https://www.mtrlegal.com/offices/frankfurt/steuerstrafrecht/ |
| 2147 | https://www.die-anwalts-kanzlei.de/steuerstrafrecht/ |
| 2086 | https://www.mtrlegal.com/offices/koeln/steuerstrafrecht/ |
| 1787 | https://motzenbaecker-adam.de/rechtsgebiete/steuer-steuerstrafrecht/ |
| 1408 | https://www.muenchner-strafverteidiger.de/steuerstrafrecht/ |
| 793 | https://gwgl-hamburg.de/rechtsgebiete/steuern/steuerstrafrecht/ |
| 741 | https://www.strafverteidiger-zeller.de/rechtsgebiete/steuerstrafrecht/ |
| 619 | https://steueranwaelte-hamburg.de/ |
| 578 | https://www.bietmann.eu/rechtsberatung/anwalt-steuerrecht |
| 545 | https://kanzlei-beisenbusch.de/strafrecht/steuerstrafrecht/ |
| 520 | https://www.hw-anwalt.de/fachanwalt-strafrecht-berlin/steuerstrafrecht/ |

Die vier Verzeichnis-Treffer von anwalt.de (Düsseldorf, Hamburg, Hannover, Fürth, Bonn, Stuttgart, Frankfurt) zählen nicht (Listen, keine Anwaltsseiten).

## Wortzahl-Urteil (vorab, Ziel)

Bestand 217 Wörter. Wettbewerber-Median 1408. Untergrenze 985. Pool-Vorgabe 1.500 bis 2.000 Wörter. Zielkorridor 1.400 bis 1.900 Wörter. Seller-Layer (ohne Vertiefung und FAQ) höchstens 550 Wörter, Tiefe in fünf Akkordeon-Blöcken.

## Konflikte im Bestand und bei Kundentexten

1. Live-Text nutzt "Spezialisierung", "besondere fachliche Expertise", "Experten", "bestmögliche Beratung": nicht übernommen (BRAO).
2. Kostenmodell: Kundentext vom 2026-10-11 (Zeitaufwand, kein RVG) gegen freigegebene Startseite ("RVG oder Vergütungsvereinbarung"). Diese Seite folgt dem Kundentext, keine Beträge.
3. Das Hauptkeyword 'anwalt steuerstrafrecht' steht im Sitetree bei ST-00, ST-10 und ST-11 (Kannibalisierung, Regel S6). Entscheidung in OPEN-FLAGS B3.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Keine Blocker. Schreiben darf starten.
