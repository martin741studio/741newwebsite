# Gate A0 (leicht plus 20 Messungen): Stürzl, Durchsuchungsbegleitung und Schulung (ST-19)

Datum: 2026-10-11. Seitentyp B (Spoke, Kind von ST-18). Modus Überarbeitung (Bestand 223 Wörter). Geldseite nach Pool-Priorität C, kein Keyword mit Volumen im Sitetree.

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth | ja | `client-baseline.md`, `assets/stuerzl/nap.json`, `source-of-truth-2026-10-11.md`, `approved-copy.md`, 2026-10-11. |
| 2 | Live-Bestand abgerufen und gezählt | ja | 223 Wörter, 2×H1, 0×H2 (`_work/bestand-metrics.json`, page_metrics.py, 2026-10-11). Inhalt: angepasste Schulung für Unternehmen, Steuerberatungsgesellschaften und Kanzleien, Notfallkontakt, Checklisten und Leitfäden je Funktion und Abteilung. Rohtext `_work/live/`. |
| 3 | Autocomplete | teilweise | Zum Stichwort keine Treffer im Baum (`autocomplete.json`: "durchsuchung steuerfahndung" 4 Treffer, "checkliste durchsuchung steuerfahndung"). SERP-Related: "102 StPO", "103 StPO", "Hausdurchsuchung ohne Beschluss". Light A0 verlangt keinen Baum. |
| 4 | Ziel-Keyword und Suchvolumen | ja, ohne Daten | Kein Sitetree-Keyword. Gewählt: "durchsuchung im unternehmen" (Entscheidung des Agenten, Martin bestätigt oder ändert). DataForSEO: durchsuchung geschäftsräume 10; "durchsuchung im unternehmen", "durchsuchung unternehmen schulung", "verhalten bei durchsuchung im unternehmen", "durchsuchung unternehmen checkliste", "durchsuchungsschulung": keine Daten (heißt keine Daten, nicht keine Nachfrage; die SERP zeigt 20 verwertbare Treffer). `_work/volume.json`, 2026-10-11. |
| 5 | SERP Top 5 und mehr | ja | `_work/serp-a.json` ("durchsuchung unternehmen schulung") und `_work/serp-b.json` ("verhalten bei durchsuchung im unternehmen"), DataForSEO serp/google/organic/live/advanced, je 0,0035 USD, 2026-10-11. Verzeichnisse, Seminaranbieter, PDFs aus dem Set genommen. |
| 6 | Echte PAA-Fragen | ja | 4 Fragen aus serp-b (2 beantwortet, 2 verworfen mit Grund, siehe brief.json). |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 20 von 20 Seiten gelesen, Median **1048** Wörter, 70-%-Untergrenze **733**. `_work/bench-metrics.json`, 2026-10-11. |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Seite. |

## Messreihe Wettbewerber

Median 1048, 70 % = 733, Seiten 20 von 20
| Wörter | Seite |
| --- | --- |
| 4217 | https://www.ccompliance.de/durchsuchung-unternehmen-rechte-pflichten/ |
| 2076 | https://www.unternehmensstrafrecht.de/wie-laeuft-eine-durchsuchung-ab-was-unternehmen-wissen-sollten/ |
| 1831 | https://www.owlaw.de/zoll-wissen/zolldurchsuchung-unternehmen-leitfaden-2025/ |
| 1693 | https://strafverteidigung-hamburg.com/64/durchsuchung/ |
| 1578 | https://pragal-rechtsanwaelte.de/blog/strategische-vorbereitung-durchsuchungen/ |
| 1554 | https://se-legal.de/verhaltenstipps-bei-einer-hausdurchsuchung/ |
| 1365 | https://www.winheller.com/wirtschaftsrecht/wirtschaftsstrafrecht/durchsuchung-unternehmen.html |
| 1188 | https://www.rostalski.legal/beratung/leitfaden-verhalten-bei-durchsuchung |
| 1085 | https://www.sicherheitsberatung.de/behoerdliche-durchsuchung-vorbereitung-auf-den-Ernstfall |
| 1052 | https://www.strafrecht-anwalt-mannheim.de/strafprozess/durchsuchung/ |
| 1044 | https://dreyenberg.com/kompetenzen/steuer-und-wirtschaftsstrafrecht/wirtschaftsstrafrecht/checkliste-hausdurchsuchung-bei-unternehmen |
| 889 | https://www.strafrecht.hamburg/durchsuchung/ |
| 834 | https://fachanwaelte-strafrecht-potsdamer-platz.de/de/verteidigung/wirtschaftsstrafrecht/durchsuchungen |
| 824 | https://stirnweiss-brenner.de/inhouse-schulungen/ |
| 759 | https://rechtsanwaelte-wirtschaftsstrafrecht-berlin.de/beschlagnahme-firmenunterlagen/ |
| 613 | https://mcb-legal.de/wissen/durchsuchung-von-geschaefts-und-wohnraeumen/ |
| 472 | https://strafrechtskanzlei-kolivas.com/wissenswertes/durchsuchung-unternehmen |
| 424 | https://kanzlei-burgert.de/wissen/durchsuchung/ |
| 403 | https://www.kanzlei-selonke.de/durchsuchung |
| 136 | https://hcm-network.com/durchsuchung-beschlagnahme/ |

## Wortzahl-Urteil

1231 Wörter eigene Seite, 223 Bestand, 1048 Median (20 Seiten, page_metrics.py, 2026-10-11), Untergrenze 733, **ausreichend** (116 % des Medians, 545 % des Bestands). Seller-Layer ohne FAQ 483 Wörter, Vertiefung 3 Blöcke, FAQ 5 Fragen.

## Konflikte im Bestand und bei Kundentexten

1. Die Live-Seite sagt "wen Sie 24/7 anrufen können". Keine Quelle belegt die Besetzungszeiten der Notfallnummern. Die neue Seite sagt kein "24/7".
2. Die Live-Seite sagt "nicht in Panik verfallen". Die neue Seite sagt "wissen, was zu tun ist" (kein Angst-Wort).
3. Kein Sitetree-Keyword: Die Seite hat kein belegtes Suchvolumen. Sie dient der Mandatsgewinnung bei Unternehmen (Core-Mandat laut Call), nicht der Reichweite.

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden (Zeile 3 und 4 mit Hinweis). Keine Blocker.
