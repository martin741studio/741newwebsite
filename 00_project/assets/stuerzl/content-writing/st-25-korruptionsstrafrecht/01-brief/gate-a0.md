# Gate A0 (voll): Stürzl, Korruptionsstrafrecht (ST-25)

Datum: 2026-10-11. Seitentyp A/B (Leistungsseite, Nachfrage klein, Geldseite laut Sitetree). Pool-Item CP-SVC-019 hatte keine Nachfragedaten (`keywords: []`). Die Lücke wurde in diesem Lauf geschlossen (DataForSEO, Kosten siehe `_work/spend.jsonl`).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste, Adressen) | ja | `source-of-truth-2026-10-11.md`, `nap.json` (Adressen bestätigt), `content-pool/01-client/client-baseline.md`, `cro/04-copy/approved-copy.md`, 2026-10-11 |
| 2 | Live-Bestand abgerufen und gezählt | ja | ST-25: 227 Wörter, 2×H1 ("Leistungen", "Korruptionsstrafrecht"), 0×H2. `_work/live/korruptionsstrafrecht.txt`, `_work/metrics.json` (page_metrics.py), 2026-10-11 |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 28 Treffer für 'korruptionsstrafrecht', 'bestechung strafe', 'vorteilsannahme'. `_work/autocomplete.json`, 2026-10-11 |
| 4 | Ziel-Keyword und Suchvolumen | ja | korruptionsstrafrecht 30; anwalt korruptionsstrafrecht 10; bestechlichkeit 2.900; vorteilsannahme 320; vorteilsgewährung 140; bestechung im geschäftlichen verkehr 90; bestechung strafe 30. `_work/volume.json`, DataForSEO google_ads/search_volume/live, de, 2276, 2026-10-11. "Korruptionsstrafrecht anwalt" liefert keine Daten (heißt: wenig Daten, nicht keine Nachfrage). |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | 'korruptionsstrafrecht anwalt' (`_work/serp.json`) und 'korruptionsstrafrecht' (`_work/serp2.json`), 2026-10-11. Verzeichnisse, Verlage, Behörden und Hochschulen aus dem Wettbewerberset genommen. |
| 6 | Echte PAA-Fragen | nein (keine) | Beide SERPs enthalten keine People-also-ask-Box. Ersatz: Autocomplete-Fragen 'ist vorteilsannahme strafbar', 'was ist vorteilsannahme', 'vorteilsannahme beispiele'. Die Fragen der Live-Seite (Flasche Wein, Betriebsprüfer) sind in der FAQ der Seite. |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 11 Seiten von Kanzleien, alle lesbar, Median **1181** Wörter, 70-%-Untergrenze **826**. Liste unten. `_work/bench-metrics.json`, 2026-10-11 |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Themenseite. Büros werden genannt, Stadt-Positionierung läuft über ST-41 und ST-42. |

## Messreihe Wettbewerber (Seiten zu Korruptionsstrafrecht)

| Wörter | Seite |
| --- | --- |
| 3773 | https://ffpv.de/expertise/korruptionsstrafrecht |
| 2550 | https://ht-strafrecht.de/rechtsgebiete/wirtschaftsstrafrecht/korruptionsstrafrecht/ |
| 1736 | https://rechtsanwalt-book.de/ratgeber/korruptionsstrafrecht-ein-ueberblick/ |
| 1423 | https://www.muenchner-strafverteidiger.de/korruptionsstrafrecht/ |
| 1209 | https://park-wirtschaftsstrafrecht.de/rechtsgebiete/korruptionsstrafrecht/ |
| 1181 | https://www.strafrecht.hamburg/wettbewerbsstrafrecht/korruption/ |
| 699 | https://www.zkkh.de/wirtschaftsstrafrecht/korruptionsstrafrecht/ |
| 604 | https://paulitsch.law/leistungen/antikorruptionsrecht/ |
| 572 | https://strafrecht.plus/korruptionsstrafrecht/ |
| 494 | https://fachanwaelte-strafrecht-potsdamer-platz.de/de/verteidigung/wirtschaftsstrafrecht/korruptionsstrafrecht |
| 263 | https://muegge-pitschel.de/korruptionsstrafrecht/ |

## Wortzahl-Urteil (vorab, Ziel)

Bestand 227 Wörter (ST-25). Wettbewerber-Median 1181. Untergrenze 826. Zielkorridor 900 bis 1.700 Wörter. Die Spanne der Wettbewerber ist groß (263 bis 3.773). Der Bestand ist dünn, hat 2×H1 und keine Zwischenüberschrift. Die Tiefe kommt aus dem Gesetzestext (belegt), nicht aus Füllsätzen.

## Konflikte im Bestand und bei Kundentexten

1. Der Bestand nennt Skandale mit Namen (CDU-Spendenaffäre, Siemens, DFB) und zitiert Transparency International. Quellen dazu wurden in diesem Lauf nicht gelesen. Beides steht nicht auf der neuen Seite.
2. Der Bestand schreibt "Bestechlichkeit/Bestechung im Gesundsheitswesen" (Tippfehler) und listet § 299a nur einzeln. Die neue Seite deckt § 299a und § 299b ab, mit gespeichertem Gesetzestext.
3. Kostenmodell: Kundentext vom 2026-10-11 (Zeitaufwand, kein RVG) widerspricht der freigegebenen Startseite ("RVG") und der Live-FAQ. Diese Seite folgt dem neuesten Kundentext, ohne Beträge.
4. Die Live-Seiten Kanzlei und Profil nutzen Wörter, die wir nicht übernehmen (BRAO/UWG), siehe OPEN-FLAGS.md.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. PAA-Lücke begründet. Keine Blocker.
