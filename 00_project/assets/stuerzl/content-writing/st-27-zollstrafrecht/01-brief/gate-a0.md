# Gate A0 (voll): Stürzl, Zollstrafrecht (ST-27)

Datum: 2026-10-11. Seitentyp A/B (Leistungsseite, Nachfrage klein; "zollfahndung" 720 ist Informationsnachfrage). Pool-Item CP-SVC-014.

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste, Adressen) | ja | `source-of-truth-2026-10-11.md`, `nap.json` (Adressen bestätigt), `content-pool/01-client/client-baseline.md`, `cro/04-copy/approved-copy.md`, 2026-10-11 |
| 2 | Live-Bestand abgerufen und gezählt | ja | ST-27: 147 Wörter, 2×H1 ("Leistungen", "Zollstrafrecht"), 0×H2. `_work/live/zollstrafrecht.txt`, `_work/metrics.json`, 2026-10-11 |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 35 Treffer für 'zollfahndung', 'zollhinterziehung', 'zollstrafrecht'. `_work/autocomplete.json`, 2026-10-11 |
| 4 | Ziel-Keyword und Suchvolumen | ja | zollstrafrecht 20; zollstrafrecht anwalt 10; anwalt zollstrafrecht 10; zollfahndung 720; bannbruch 390; zollhinterziehung 20; schmuggel strafe 10. `_work/volume.json`, DataForSEO, de, 2276, 2026-10-11. Null-Werte bei "zollhinterziehung strafe", "zollfahndung durchsuchung", "zollstrafverfahren" heißen wenig Daten, nicht keine Nachfrage (Autocomplete zeigt 'zollhinterziehung strafe'). |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | 'zollstrafrecht anwalt' (`_work/serp.json`), 2026-10-11. Fachartikel von Steuerberatern (steuerberatung-niedersachsen.de) bleiben als Vergleich im Set, weil sie in der SERP stehen. |
| 6 | Echte PAA-Fragen | ja | 4 Fragen, alle zu Anwaltskosten und allgemeinem Strafrecht. Alle 4 verworfen mit Grund (Duplikat der Kostenseite, Superlativ, nicht im Angebot), siehe `brief.paa_questions`. Ersatz: Autocomplete-Fragen 'was ist zollhinterziehung', 'was macht zollfahndung', 'zollhinterziehung strafe' sind in der FAQ. |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 15 von 15 Seiten gelesen, Median **742** Wörter, 70-%-Untergrenze **519**. Liste unten. `_work/bench-metrics.json`, 2026-10-11 |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Themenseite. |

## Messreihe Wettbewerber (Seiten zu Zollstrafrecht)

| Wörter | Seite |
| --- | --- |
| 1553 | https://www.strafrecht-bundesweit.de/zollstrafrecht/ |
| 1328 | https://haug.law/steuer-und-zollstrafrecht-anwalt-berlin/ |
| 1275 | https://www.gw-strafrecht.de/rechtsgebiete/zoll-und-aussenwirtschaftsstrafrecht/ |
| 879 | https://www.strafrecht.hamburg/zollstrafrecht/ |
| 808 | https://steuerstrafrecht.lueders-warneboldt.de/zollstrafrecht/ |
| 805 | https://www.heidelberg-strafrecht.de/zollstrafrecht.html |
| 759 | https://www.winheller.com/steuerrecht-steuerberatung/zollrecht.html |
| 742 | https://www.kanzleimauss.de/anwalt-zollrecht-augsburg/ |
| 694 | https://dreyenberg.com/kompetenzen/zollrecht/zollstrafrecht2 |
| 675 | https://www.rechtsanwaelte-langen.de/strafrecht/zollstrafrecht/ |
| 526 | https://www.kanzlei-jkb.de/kompetenzen/zollstrafrecht/ |
| 507 | https://steuerberatung-niedersachsen.de/zollpruefung-und-zollstrafrecht/ |
| 471 | https://www.anwalt-strafverteidigung.de/strafrecht-abc/zollstrafrecht-zollordnungswidrigkeiten-150 |
| 407 | https://birkenmaier-obser.de/de/schwerpunkte/steuerstrafrecht/zollstrafrecht |
| 283 | https://www.kanzlei-kindshofer.de/rechtsanwaltskanzlei-kindshofer-zollrecht-zollstrafrecht |

## Wortzahl-Urteil (vorab, Ziel)

Bestand 147 Wörter (ST-27). Wettbewerber-Median 742. Untergrenze 519. Zielkorridor 900 bis 1.500 Wörter. Der Bestand ist dünn. Er enthält zwei Listenpunkte, die zur Seite Ordnungswidrigkeiten gehören (Steuerordnungswidrigkeiten, § 30 und § 130 OWiG, siehe Live-Text). Diese Punkte sind in die Vertiefung eingearbeitet.

## Konflikte im Bestand und bei Kundentexten

1. Die Liste am Ende der Live-Seite (Steuergefährdung, § 30 OWiG, § 130 OWiG) ist die gleiche wie auf der Seite Ordnungswidrigkeiten. Wahrscheinlich eine Kopie. Kanzlei bestätigt, ob sie hier gemeint ist.
2. Kostenmodell: Kundentext vom 2026-10-11 (Zeitaufwand, kein RVG) widerspricht der freigegebenen Startseite ("RVG") und der Live-FAQ.
3. Live-Seite nennt die alte Adresse und die alte Telefonnummer (Fußzeile). Die neue Seite nennt nur die bestätigten Daten.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Keine Blocker.
