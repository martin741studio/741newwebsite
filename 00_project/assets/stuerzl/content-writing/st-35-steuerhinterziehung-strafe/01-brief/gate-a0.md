# Gate A0 (leicht): steuerhinterziehung strafe (st-35-steuerhinterziehung-strafe)

Datum: 2026-10-11. Seitentyp Blog (Vorschlag). Gate: leicht (Ratgeber-Beitrag, kein Bestand: die Seite gibt es heute nicht).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Keyword und Volumen aus dem Pool | ja | 4.400 Suchen national (steuerhinterziehung strafe); Cluster haftstrafe 90, geldstrafe 70, ab welchem betrag 30, bewährung 10. `03-demand/volume.json`, DataForSEO google_ads/search_volume, 2026-10-11 |
| 2 | SERP Top 5 gelesen | ja | ihre-vorsorge.de, strafverteidigung-roth.de, advocado.de, pauls-coerper.de, bildt-law.de (`_work/serp.json`, DataForSEO serp/google/organic/live/advanced, de, 2276, 2026-10-11, Kosten 0,0035 USD) |
| 3 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 13 Messungen, Median **1469** Wörter, Untergrenze 70 % = **1028**. `_work/bench-metrics.json`, page_metrics.py, 2026-10-11 |
| 4 | Echte PAA-Fragen | ja | 4 aus der SERP: Welche Straftat ist die Steuerhinterziehung nach § 369 und 370 AO? Wie lange dauert ein Strafverfahren wegen Steuerhinterziehung? Was ist eine leichte Steuerhinterziehung? Was passiert bei 10000 Euro Steuerhinterziehung? Dazu 3 aus dem Pool (CP-SVC-021). Autocomplete: haft, geldstrafe, freiheitsstrafe, gefängnisstrafe |
| 5 | Fakten verifiziert | ja | Gesetzestexte gespeichert in `_work/gesetze/` (gesetze-im-internet.de, gelesen 2026-10-11). Die Wertgrenzen des BGH stehen im gespeicherten Urteil (`_work/bgh-1-StR-416-08.txt`, hrr-strafrecht.de). |
| 6 | Interne Link-Ziele aus der Sitemap | ja | /steuerstrafrecht/verteidigung-im-steuerstrafverfahren/ (ST-12), /selbstanzeige/ (ST-14), /ratgeber/verjaehrung/ (ST-36), /ratgeber/ (ST-34), /dr-anja-stuerzl/ (ST-45) (`sitetree.json`, 2026-10-11) |
| 7 | Bestand | keiner | Die Seite gibt es heute nicht (sitetree: Vorschlag, `live_status` missing). Kundentexte zum Thema gelesen: Live-FAQ (2.555 Wörter), Live-Seite Kanzlei, Live-Seite Dr. Stürzl, Aktuelles (Liste), Selbstanzeige-Referenzseite. Die Live-FAQ (Abschnitt I.4 Strafen) liefert die Kanzleiaussagen zu Strafrahmen und Nebenfolgen. |

## Messreihe Wettbewerber

| Wörter | Seite |
| --- | --- |
| 4239 | https://haider.legal/steuerhinterziehung/ |
| 2927 | https://www.corta.de/steuerrecht/steuerhinterziehung |
| 2231 | https://www.bildt-law.de/strafe-bei-steuerhinterziehung |
| 1784 | https://strafverteidigung-roth.de/ab-welchem-betrag-ist-steuerhinterziehung-strafbar/ |
| 1698 | https://www.zk-recht.de/wissenswertes/steuerhinterziehung-strafe |
| 1671 | https://www.advocado.de/ratgeber/steuerrecht/steuererklaerung/steuerhinterziehung.html |
| 1469 | https://strafverteidigung-hamburg.com/247/steuerhinterziehung/ |
| 920 | https://www.pauls-coerper.de/rechtsgebiete/steuerstrafrecht/steuerhinterziehung-strafe/ |
| 904 | https://www.ihre-vorsorge.de/finanzen/nachrichten/steuerhinterziehung-oder-steuerordnungswidrigkeit-diese-strafen-drohen |
| 845 | https://steuerberatung-niedersachsen.de/wann-droht-gefaengnis-bei-steuerhinterziehung/ |
| 824 | https://www.ferner-alsdorf.de/steuerhinterziehung-strafmass-bei-steuerhinterziehung/ |
| 695 | https://www.strafrecht-bundesweit.de/strafrecht-blog/die-strafzumessung-bei-steuerhinterziehung-ist-die-hoehe-der-geldsumme-entscheidend/ |
| 584 | https://steuerberater-muenchen.de/blog-und-steuernews/strafmass-steuerhinterziehung-welche-strafen-drohen-bei-steuerstraftaten.html |

Nicht gezählt:

| Wörter | Seite | Grund |
| --- | --- | --- |
| 47 | https://www.rechtsanwalt.com/news/steuerhinterziehung-was-droht/ | nicht als Messung gezählt (Seite liefert fast keinen Text, z. B. Paywall oder Skript) |

Es wurden alle 14 URLs der Top 10 bis 20 ohne Verzeichnisse, Video- und Wikipedia-Treffer gelesen. Verzeichnisse und Plattformen (anwalt.de, YouTube, Facebook) sind kein Benchmark.

## Wortzahl-Urteil

Ziel vor dem Schreiben: mindestens 1028 Wörter (70 % von 1469), Zielkorridor siehe brief.json `word_range`. Die endgültige Zählung steht in `04-gates/gates.md` (Satz "X Wörter eigene Seite, Y Bestand, Z Median, Quelle, Datum, Urteil").

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Keine Blocker für den Entwurf. Offen bleiben Autor und Freigabe (Platzhalter), siehe `OPEN-FLAGS.md`.
