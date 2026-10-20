# Gate A0 (voll): Stürzl, Selbstanzeige (ST-14)

Datum: 2026-10-11. Seitentyp A (Geldseite). Quelle der Pool-Daten: `content-pool/` (Lauf 2026-10-11).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste) | ja | `content-pool/01-client/client-baseline.md`, `cro/04-copy/approved-copy.md` (Brief), 2026-10-11. Das Stammdatenblatt (Sheet 10JISY6H…) ist per Zelle nicht lesbar: NAP-Details (endgültige Adresse Frankfurt) bleiben aus dem Fließtext heraus. |
| 2 | Live-Bestand abgerufen und gezählt | ja | ST-14: 248 Wörter, 2×H1, 0×H2. ST-15: 252. ST-17: 219. ST-16 ist zu 97 % gleicher Text. `_work/bestand-metrics.json`, `bestand-st14.txt`, 2026-10-11 (page_metrics.py, Zählweise: sichtbarer Text ohne Nav/Footer). |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 260 Treffer für 'selbstanzeige', `content-pool/03-demand/autocomplete.json`, 2026-10-11. |
| 4 | Ziel-Keyword und Suchvolumen | ja | selbstanzeige anwalt 10; selbstanzeige finanzamt 720; selbstanzeige steuerhinterziehung 480; strafbefreiende selbstanzeige 170. `03-demand/volume.json`, DataForSEO 2026-10-11. Hinweis: 10 heißt wenig Daten, nicht kaum Nachfrage; das Cluster hat 1.420 Summe. |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | `02-competitors/serp-5.json` ('selbstanzeige anwalt'), 2026-10-11. Verzeichnisse (anwalt.de, anwaltssuche.de) aus dem Wettbewerberset genommen. |
| 6 | Echte PAA-Fragen | ja | 4 Fragen aus serp-5: Ist eine Selbstanzeige straffrei? Wer bezahlt den Anwalt im Strafverfahren? Kann man einen Rechtsanwalt anzeigen? (passt nicht zum Angebot, nicht verwendet) Wie hoch ist die Strafe bei 5000 € Steuerhinterziehung? |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 11 von 11 gelesen, Median **1566** Wörter, 70-%-Untergrenze **1096**. Liste unten. `_work/bench-metrics.json`, 2026-10-11. |
| 8 | Lokaler Fakt (nur wenn Stadt Teil der Positionierung) | nicht nötig | ST-14 ist eine bundesweite Themenseite. Die Büros werden genannt, Stadt-Positionierung läuft über ST-41 und ST-42. |

## Messreihe Wettbewerber (Seiten zu Selbstanzeige)

| Wörter | Seite |
| --- | --- |
| 3696 | https://www.mtrlegal.com/offices/muenchen/steuerstrafrecht/selbstanzeige/ |
| 2684 | https://kraffczyk.eu/fachanwalt-strafrecht-muenchen/selbstanzeige-steuer/ |
| 2367 | https://www.cornea-franz.de/rechtsgebiete/steuerstrafrecht/ |
| 2189 | https://www.bildt-law.de/selbstanzeige-kosten |
| 1637 | https://frankeroericht.de/selbstanzeige/ |
| 1566 | https://www.ra-kotz.de/steuerhinterziehung-selbstanzeige.htm |
| 980 | https://www.strafrecht.berlin/steuerstrafrecht/steuerhinterziehung/selbstanzeige-steuerhinterziehung/ |
| 759 | https://steuerstrafrecht.lueders-warneboldt.de/selbstanzeige/ |
| 564 | https://steuerdelikt.de/selbstanzeige/voraussetzungen/uebersicht-voraussetzungen-selbstanzeige |
| 490 | https://www.kls-law.de/kompetenzen/steuerstrafrecht-und-selbstanzeige/ |
| 303 | http://www.heidelberg-arbeitsrecht.de/Fachanwalt_Steuerrecht/Selbstanzeige_und_Steuerstrafrecht |

## Wortzahl-Urteil (vorab, Ziel)

Bestand 248 Wörter (ST-14). Wettbewerber-Median %d. Untergrenze %d. Zielkorridor 1.100 bis 1.500 Wörter. Der Bestand ist dünn und enthält ein Ergebnisversprechen in der H1 („Straffreiheit selbst im Falle von vorsätzlich hinterzogenen Steuern"). Das ist unter BRAO § 43b nicht zu übernehmen.

## Konflikte im Bestand und bei Kundentexten

1. H1 des Bestands verspricht Straffreiheit: wird nicht übernommen (Ergebnisversprechen).
2. Kostenmodell: Kundentext vom 2026-10-11 (Zeitaufwand, kein RVG) widerspricht der freigegebenen Startseite („Vergütung nach RVG") und der Live-FAQ (andere Stundensätze). Diese Seite folgt dem neuesten Kundentext und nennt keine Beträge.
3. Drei Selbstanzeige-Seiten haben fast denselben Text (97 % und 74 %). Die neue Seite ersetzt sie; Weiterleitungen nur mit Zustimmung der Kundin (Klärung mit Irsch).
4. Kundentext Kosten enthält „besonders hohe Spezialisierung": steht nicht auf dieser Seite (BRAO).

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Keine Blocker. Phase 1 (Schreiben) darf starten.
