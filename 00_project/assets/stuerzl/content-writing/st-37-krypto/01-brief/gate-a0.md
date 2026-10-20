# Gate A0 (leicht): krypto steuerhinterziehung (st-37-krypto)

Datum: 2026-10-11. Seitentyp Blog (Vorschlag). Gate: leicht (Ratgeber-Beitrag, kein Bestand: die Seite gibt es heute nicht).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Keyword und Volumen aus dem Pool | ja | 20 Suchen national (`03-demand/volume.json`, DataForSEO, 2026-10-11): wenig Daten, nicht kaum Nachfrage; Autocomplete "selbstanzeige krypto", "steuerstrafverfahren krypto"; Pool-Priorität C |
| 2 | SERP Top 5 gelesen | ja | rosepartner.de, t-online.de, crypto-crime.de, kleinstb.de, winheller.com (`_work/serp.json`, DataForSEO serp/google/organic/live/advanced, de, 2276, 2026-10-11, Kosten 0,0035 USD) |
| 3 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 13 Messungen, Median **1214** Wörter, Untergrenze 70 % = **849**. `_work/bench-metrics.json`, page_metrics.py, 2026-10-11 |
| 4 | Echte PAA-Fragen | ja | 4 aus der SERP: Wie funktioniert Krypto-Steuer? Muss ich Kryptogewinne unter 600 Euro bei der Steuer angeben? Wird Krypto bald besteuert? (verworfen: nicht rechtssicher) Was passiert, wenn man Krypto-Gewinne nicht angibt? |
| 5 | Fakten verifiziert | ja | Gesetzestexte gespeichert in `_work/gesetze/` (gesetze-im-internet.de, gelesen 2026-10-11). Das BMF-Schreiben vom 6. März 2025 ist im Lauf gespeichert (`_work/bmf-krypto-2025-03-06.md`, Quelle lsth.bundesfinanzministerium.de), das KStTG in `_work/gesetze/ksttg.txt`. |
| 6 | Interne Link-Ziele aus der Sitemap | ja | /selbstanzeige/ (ST-14), /ratgeber/steuerhinterziehung-strafe/ (ST-35), /ratgeber/ (ST-34), /dr-anja-stuerzl/ (ST-45) (`sitetree.json`, 2026-10-11) |
| 7 | Bestand | keiner | Die Seite gibt es heute nicht (sitetree: Vorschlag, `live_status` missing). Kundentexte zum Thema gelesen: Live-FAQ (2.555 Wörter), Live-Seite Kanzlei, Live-Seite Dr. Stürzl, Aktuelles (Liste), Selbstanzeige-Referenzseite. Der Influencer-Beitrag auf der Live-Seite (18. Juli 2025) ist kein Krypto-Beitrag und wurde nicht verwendet. |

## Messreihe Wettbewerber

| Wörter | Seite |
| --- | --- |
| 13235 | https://www.ksw-recht.de/kryptowaehrung-selbstanzeige-steuerrecht |
| 5413 | https://www.lhp-gruppe.de/kryptowaehrungen-bitcoin-steuer/post-vom-finanzamt-wegen-krypto/ |
| 4550 | https://www.hortmannlaw.com/articles/krypto-steuerstrafrecht-selbstanzeige-anwalt |
| 2833 | https://www.rosepartner.de/bitcoin-recht-steuern.html |
| 1631 | https://www.acconsis.de/steuerstrafverfahren-gegen-krypto-trader-finanzamt-hat-ersten-daten-vorliegen/ |
| 1501 | https://bitcoin-2go.de/wissen/steuern/steuerhinterziehung |
| 1214 | https://www.winheller.com/bankrecht-finanzrecht/bitcointrading/bitcoinundsteuer/kryptosteuererklaerung.html |
| 1073 | https://www.crypto-crime.de/crypto-crime-selbstanzeige-bei-steuerhinterziehungen-mit-bitcoin-und-anderen-kryptowaehrungen |
| 1057 | https://fm.baden-wuerttemberg.de/de/steuern/steuern-aktuelle-themen/besteuerung-von-kryptowaehrungen |
| 1033 | https://www.gkanzlei.de/bundesfinanzhof-urteil-krypto-gewinne-sind-steuerpflichtig/ |
| 924 | https://kleinstb.de/blog/krypto-versteuern-selbstanzeige-wichtige-infos-zu-mica-dac8/ |
| 763 | https://www.t-online.de/finanzen/aktuelles/kryptowaehrung/id_100929886/krypto-steuerfahndung-nrw-prueft-daten-tausender-anleger-auf-betrug.html |
| 434 | https://kleinstb.de/blog/steuern-hinterzogen-durch-kryptowaehrungen/ |

Nicht gezählt:

| Wörter | Seite | Grund |
| --- | --- | --- |
| 20 | https://www.blockpit.io/de-de/blog/krypto-steuerhinterziehung-aeb33 | nicht als Messung gezählt (Seite liefert fast keinen Text, z. B. Paywall oder Skript) |

Es wurden alle 14 URLs der Top 10 bis 20 ohne Verzeichnisse, Video- und Wikipedia-Treffer gelesen. Verzeichnisse und Plattformen (anwalt.de, YouTube, Facebook) sind kein Benchmark.

## Wortzahl-Urteil

Ziel vor dem Schreiben: mindestens 849 Wörter (70 % von 1214), Zielkorridor siehe brief.json `word_range`. Die endgültige Zählung steht in `04-gates/gates.md` (Satz "X Wörter eigene Seite, Y Bestand, Z Median, Quelle, Datum, Urteil").

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Keine Blocker für den Entwurf. Offen bleiben Autor und Freigabe (Platzhalter), siehe `OPEN-FLAGS.md`.
