# Gate A0 (leicht): steuerhinterziehung verjährung (st-36-verjaehrung)

Datum: 2026-10-11. Seitentyp Blog (Vorschlag). Gate: leicht (Ratgeber-Beitrag, kein Bestand: die Seite gibt es heute nicht).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Keyword und Volumen aus dem Pool | ja | 2.400 Suchen national (`03-demand/volume.json`, DataForSEO, 2026-10-11); Autocomplete: 22 Treffer zu "verjähr", darunter "5 jahre" und "10 jahre" |
| 2 | SERP Top 5 gelesen | ja | steuer-gonze.de, rechtsanwaelte-wirtschaftsstrafrecht-berlin.de, taxfix.de, steueranwalt-leipzig.de, steuerdelikt.de (serp-9 des Pools, `_work/serp.json`) (`_work/serp.json`, DataForSEO serp/google/organic/live/advanced, de, 2276, 2026-10-11, aus dem Pool übernommen, in diesem Lauf 0 USD) |
| 3 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 12 Messungen, Median **800** Wörter, Untergrenze 70 % = **560**. `_work/bench-metrics.json`, page_metrics.py, 2026-10-11 |
| 4 | Echte PAA-Fragen | ja | 3 aus der SERP: Wann fängt Steuerhinterziehung an? Wann verjährt die Steuerschuld? Wie lange kann das Finanzamt Steuerbescheide rückwirkend ändern? (Wann verjähren Betrugsfälle? verworfen: off-offer) |
| 5 | Fakten verifiziert | ja | Gesetzestexte gespeichert in `_work/gesetze/` (gesetze-im-internet.de, gelesen 2026-10-11). Beginn der Verfolgungsverjährung (Beendigung der Tat) ist ohne Rechtsprechung nur als Einzelfall formuliert. |
| 6 | Interne Link-Ziele aus der Sitemap | ja | /selbstanzeige/ (ST-14), /ratgeber/steuerhinterziehung-strafe/ (ST-35), /ratgeber/ (ST-34), /dr-anja-stuerzl/ (ST-45) (`sitetree.json`, 2026-10-11) |
| 7 | Bestand | keiner | Die Seite gibt es heute nicht (sitetree: Vorschlag, `live_status` missing). Kundentexte zum Thema gelesen: Live-FAQ (2.555 Wörter), Live-Seite Kanzlei, Live-Seite Dr. Stürzl, Aktuelles (Liste), Selbstanzeige-Referenzseite. Die Referenzseite Selbstanzeige nennt schon die Zehn-Jahres-Regel (§ 371 Abs. 1 AO). |

## Messreihe Wettbewerber

| Wörter | Seite |
| --- | --- |
| 2027 | https://rechtsanwaelte-gsp.de/lp/steuerhinterziehung-verjaehrung-13/ |
| 1940 | https://www.juhn.com/fachwissen/betriebspruefung-einspruch-klage/verjaehrung-steuerfestsetzung/ |
| 1086 | https://www.steuer-gonze.de/verjaehrung-im-steuerrecht/ |
| 943 | https://www.dr-buchert.de/rechtslexikon/verjaehrung-im-steuerstrafrecht-verfolungsverjaehrung-und-festsetzungsverjaehrung/ |
| 855 | https://taxfix.de/ratgeber/allgemein/wann-verjaehrt-steuerhinterziehung/ |
| 809 | https://www.vlh.de/wissen-service/steuer-abc/wann-verjaehren-steuerschulden.html |
| 792 | https://www.lhp-gruppe.de/themen/aus-der-trickkiste-des-gesetzgebers-steuereintreibung-nach-verjaehrung/ |
| 788 | https://www.raekoeln.de/steuerhinterziehung-und-verjahrung/ |
| 627 | https://steuerdelikt.de/steuerverfahren-steuerstrafrecht/festsetzungsverjaehrung-und-steuerhinterziehung |
| 575 | https://www.steueranwalt-leipzig.de/verjaehrungsbeginn-steuerhinterziehung-erstbescheid-oder-aenderungsbescheid/5486/ |
| 571 | https://rechtsanwaelte-wirtschaftsstrafrecht-berlin.de/verjaehrungsbeginn/ |
| 528 | https://steuerberater-muenchen.de/blog-und-steuernews/die-arten-der-verjaehrungsfrist-wann-verjaehren-steuerschulden.html |

Nicht gezählt:

| Wörter | Seite | Grund |
| --- | --- | --- |
| 39 | https://datenbank.nwb.de/Dokument/521806/ | nicht als Messung gezählt (Seite liefert fast keinen Text, z. B. Paywall oder Skript) |
| 39 | https://datenbank.nwb.de/Dokument/878797/ | nicht als Messung gezählt (Seite liefert fast keinen Text, z. B. Paywall oder Skript) |

Es wurden alle 14 URLs der Top 10 bis 20 ohne Verzeichnisse, Video- und Wikipedia-Treffer gelesen. Verzeichnisse und Plattformen (anwalt.de, YouTube, Facebook) sind kein Benchmark.

## Wortzahl-Urteil

Ziel vor dem Schreiben: mindestens 560 Wörter (70 % von 800), Zielkorridor siehe brief.json `word_range`. Die endgültige Zählung steht in `04-gates/gates.md` (Satz "X Wörter eigene Seite, Y Bestand, Z Median, Quelle, Datum, Urteil").

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Keine Blocker für den Entwurf. Offen bleiben Autor und Freigabe (Platzhalter), siehe `OPEN-FLAGS.md`.
