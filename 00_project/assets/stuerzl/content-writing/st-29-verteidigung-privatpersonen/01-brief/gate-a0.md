# Gate A0 (leicht plus 22 Messungen): Stürzl, Verteidigung von Privatpersonen (ST-29)

Datum: 2026-10-11. Seitentyp B (Spoke unter Leistungen, Eltern von ST-30). Modus Überarbeitung (Bestand 211 Wörter auf der Hauptseite, dazu drei Unterseiten mit 290, 331, 214 Wörtern, die bleiben).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth | ja | `client-baseline.md`, `assets/stuerzl/nap.json`, `source-of-truth-2026-10-11.md`, `approved-copy.md`, 2026-10-11. |
| 2 | Live-Bestand abgerufen und gezählt | ja | Hauptseite 211 Wörter, 2×H1, 0×H2. Unterseiten Zeugenbegleitung 290, Strafanzeige 331, Ordnungswidrigkeiten 214 (`_work/bestand-metrics.json`, page_metrics.py, 2026-10-11). Rohtexte `_work/live/`. Die Antworten der Unterseiten sind in S07 aufgenommen (gekürzt). |
| 3 | Autocomplete | teilweise | Kein Baum zum Stichwort. Verwandt: "zeuge im steuerstrafverfahren" (Baum "steuerstrafverfahren", `autocomplete.json`). Light A0 verlangt keinen Baum. |
| 4 | Ziel-Keyword und Suchvolumen | ja, ohne Daten | Kein Sitetree-Keyword. Gewählt: "strafverteidiger steuerstrafrecht" (keine Daten; Entscheidung des Agenten, Martin bestätigt oder ändert). Themenbegriffe (breit, nicht steuerspezifisch): vermögensarrest 480, zeugenbeistand 320, vorladung als zeuge 320, beschuldigtenvernehmung 260, ermittlungsverfahren was tun 50, ordnungswidrigkeit anwalt 40, steuerordnungswidrigkeit 30, strafanzeige anwalt 20, haftbefehl anwalt 20, steuerstrafverteidiger 20. `_work/volume.json`, DataForSEO google_ads/search_volume/live, de, 2276, 2026-10-11. Die Zahlen belegen Themeninteresse, nicht Nachfrage nach dieser Seite. |
| 5 | SERP | ja | `_work/serp-a.json` ("strafverteidiger steuerstrafrecht") und `_work/serp-b.json` ("zeugenbeistand steuerstrafverfahren"), je 0,0035 und 0,002 USD, 2026-10-11. Verzeichnisse und Portale aus dem Set genommen. |
| 6 | Echte PAA-Fragen | ja | 4 Fragen aus serp-b (3 beantwortet, 1 verworfen mit Grund). serp-a hat keine PAA. |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 22 von 22 Seiten gelesen, Median **1008,5** Wörter, 70-%-Untergrenze **705**. `_work/bench-metrics.json`, 2026-10-11. |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Seite. |

## Messreihe Wettbewerber

Median 1008.5, 70 % = 705, Seiten 22 von 22
| Wörter | Seite |
| --- | --- |
| 3882 | https://www.strafrecht-bundesweit.de/steuerstrafrecht-privatpersonen/ |
| 3774 | https://ffpv.de/expertise/steuerstrafrecht |
| 2450 | https://www.lhp-gruppe.de/steuerstrafverfahren/zeuge-im-steuerstrafverfahren/ |
| 2410 | https://steuerstrafverteidiger.net/ |
| 2147 | https://www.die-anwalts-kanzlei.de/steuerstrafrecht/ |
| 2033 | https://rechtsanwaelte-gsp.de/rechtsberatung/steuerstrafrecht/ |
| 1777 | https://www.cornea-franz.de/anwalt-steuerhinterziehung/ |
| 1503 | https://www.kanzlei-rudnicki.de/anwalt-strafrecht-berlin/steuerstrafrecht/ |
| 1472 | https://www.sdmw.de/steuerstrafrecht/ |
| 1429 | https://se-legal.de/rechtsanwalt/strafrecht/tatigkeit-als-zeugenbeistand-in-strafsachen/ |
| 1224 | https://www.bms-rechtsanwaelte.de/wirtschaftsstrafrecht/zeugenbeistand |
| 793 | https://gwgl-hamburg.de/rechtsgebiete/steuern/steuerstrafrecht/ |
| 758 | https://fries.law/steuerstrafrecht.html |
| 712 | https://www.drburkhard.de/steuerstrafrecht/ |
| 639 | https://www.michalkerosskopf.de/ |
| 601 | https://dengler-dengler.de/leistungen/recht/steuerstrafrecht/ |
| 545 | https://kanzlei-beisenbusch.de/strafrecht/steuerstrafrecht/ |
| 461 | https://www.strafrecht.de/de/zeugenbeistand/ |
| 364 | https://www.gtkr.de/kompetenzen/steuerstrafrecht/ |
| 223 | https://www.kfdr.de/zeugenbeistand |
| 222 | https://www.verteidiger-in-zollstrafsachen.de/t%C3%A4tigkeitsbereiche/steuerstrafrecht/ |
| 67 | https://www.rechtsanwalt-bongard.de/rechtstipps/zeugenbeistand-wann-lohnt-sich-ein-anwalt-fuer-zeugen |

## Wortzahl-Urteil

1336 Wörter eigene Seite, 211 Bestand (Hauptseite), 1008,5 Median (22 Seiten, page_metrics.py, 2026-10-11), Untergrenze 705, **ausreichend** (131 % des Medians). Seller-Layer ohne FAQ 478 Wörter (Regel: höchstens 550). Vertiefung 5 Blöcke, FAQ 6 Fragen.

## Konflikte im Bestand und bei Kundentexten

1. Kein Keyword im Sitetree. Es gibt kein belegtes Suchvolumen. Die Seite dient der Mandatsgewinnung und der Verlinkung der drei Unterseiten (ST-30).
2. Live-Text: "bestmögliche Lösung", "umfassend und hartnäckig", "Worst Case". Nur "hartnäckig" ist übernommen (Wort der Kanzlei, nicht auf der Verbotsliste).
3. Mögliche Überschneidung mit ST-12 (steuerstrafverfahren), ST-21 (Zeugenbegleitung für Unternehmen) und ST-23 (Ordnungswidrigkeiten). Diese Seite nimmt die Perspektive der Privatperson und verweist auf die Schwesterseiten.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden (Zeile 3 und 4 mit Hinweis). Keine Blocker.
