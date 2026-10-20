# Gate A0 (voll): Stürzl, Unternehmensvertretung (ST-21)

Datum: 2026-10-11. Seitentyp A (Geldseite, Pool-Priorität C). Quelle der Pool-Daten: `content-pool/` (Lauf 2026-10-11).

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste) | ja | `content-pool/01-client/client-baseline.md`, `cro/04-copy/approved-copy.md`, `source-of-truth-2026-10-11.md`, `nap.json`, 2026-10-11. |
| 2 | Live-Bestand abgerufen und gezählt | ja | Hauptseite 291 Wörter, 2×H1, 0×H2. Vier Unterseiten: Strafanzeigen 403, Verteidigung bei Ordnungswidrigkeitenverfahren gegen das Unternehmen 309, Vertretung bei Strafverfahren gegen Mitarbeiter 306, Zeugenbegleitung 362 (alle zeigen denselben Einleitungstext). `_work/bestand-metrics.json`, page_metrics.py, 2026-10-11. |
| 3 | Autocomplete-Themenbaum (mindestens 15) | ja | 134 Treffer über vier Seeds (unternehmensstrafrecht 25, unternehmensvertretung 3, zeugenbeistand 102, sockelverteidigung 4). `_work/autocomplete.json`, 2026-10-11. Hinweis: "unternehmensstrafrecht" zeigt vor allem Lehrbuch- und Hochschul-Suchen. |
| 4 | Ziel-Keyword und Suchvolumen | ja, mit Einschränkung | Das Sitetree-Feld "Keyword" ist leer; der Begriff "unternehmensvertretung" hat in DataForSEO keine Daten (kein Volumen heißt keine Daten, nicht keine Nachfrage). Gewählt: **unternehmensstrafrecht 70** (national). Weitere: zeugenbeistand 320, sockelverteidigung 50, unternehmensverteidigung 40, verbandsgeldbuße 40; organisationsverschulden 480 und aufsichtspflichtverletzung 320 gehören zu ST-23. `_work/vol.json` (24 Begriffe), DataForSEO google_ads/search_volume/live, de, 2276, 2026-10-11, Kosten 0,09 USD. Entscheidung für Martin: siehe OPEN-FLAGS C1. |
| 5 | SERP Top 10 für das Ziel-Keyword | ja | `_work/serp-unternehmensstrafrecht.json` ('unternehmensstrafrecht'), DataForSEO, 2026-10-11, Kosten 0,0035 USD. Die SERP ist überwiegend wissenschaftlich und politisch (Landtag, Springer, Bundestag, PwC, Lehrbuch). Kanzlei-Seiten: al-st.de, kanzlei-burgert.de, law.ch. |
| 6 | Echte PAA-Fragen | ja | 4 Fragen: Wann macht sich ein Geschäftsführer strafbar? (beantwortet, FAQ); Was fällt unter Wirtschaftsstrafrecht? (verworfen, Duplikat ST-20); Was sind Beispiele für Straftaten? und Welche 3 Elemente müssen zwingend erfüllt sein, damit man vom Vorliegen einer strafbaren Handlung sprechen kann? (verworfen, off-offer). |
| 7 | Wettbewerber-Wortzahl, mindestens 2 erfolgreiche Messungen | ja | 6 von 6 Kanzlei-Seiten gelesen (Treffer der SERP plus drei verwandte Seiten von dr-buchert.de und rae-sus.de, weil die SERP nur drei Kanzlei-Seiten liefert). `_work/bench-metrics.json`, 2026-10-11. Liste unten. |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Themenseite. Die Büros werden genannt, Stadt-Positionierung läuft über ST-41 und ST-42. |

## Messreihe Wettbewerber (Seiten zu Unternehmensstrafrecht und Unternehmensvertretung)

| Wörter | Seite |
| --- | --- |
| 4212 | https://www.dr-buchert.de/compliance-beratung/strafrechtliche-unternehmensberatung/ |
| 1807 | https://www.dr-buchert.de/strafverteidigung/wirtschaftsstrafrecht/ |
| 1561 | https://www.dr-buchert.de/strafverteidigung/unternehmensstrafrecht/ |
| 606 | https://rae-sus.de/kanzlei/ |
| 573 | https://www.al-st.de/t%C3%A4tigkeitsgebiete/strafrecht/unternehmensstrafrecht/ |
| 424 | https://kanzlei-burgert.de/rechtsgebiete/wirtschaftsstrafrecht/unternehmensstrafrecht/ |

Messwerte: 6, Median 1083.5, 70 % = 758

## Wortzahl-Urteil (vorab, Ziel)

Bestand 291 Wörter (Hauptseite). Wettbewerber-Median 1083,5 (6 Seiten, Spannweite 424 bis 4212). Untergrenze 758. Zielkorridor 900 bis 1500 Wörter. Der Median ist von einer Seite mit 4212 Wörtern geprägt, die eine ganze Rubrik bündelt. Die Seite bleibt deshalb unter dem Mittel der großen Treffer und füllt die Tiefe mit Gesetzestext (§ 30, § 130 OWiG, StPO) statt mit Füllwörtern.

## Konflikte im Bestand und bei Kundentexten

1. Die vier Live-Unterseiten tragen denselben langen Einleitungstext wie die Hauptseite (Duplikat). Sie bleiben laut Sitetree (ST-22) und bekommen später eigene Texte.
2. Der Bestand nennt "Expertise", "kompetente" und "effektiv": nicht übernommen (BRAO).
3. Der Bestand zur Strafanzeige sagt, man könne sich wegen falscher Verdächtigung strafbar machen, wenn der Sachverhalt nicht vollständig und richtig dargestellt ist. § 164 StGB verlangt "wider besseres Wissen". Die Seite folgt dem Gesetz.
4. Kostenmodell: Kundentext vom 2026-10-11 (Zeitaufwand, kein RVG) gegen freigegebene Startseite ("RVG").

## Gate-Ergebnis

Alle Pflichtzeilen vorhanden. Kein Blocker. Einschränkung: Das Keyword hat nur 70 Suchen und gemischte Suchabsicht (siehe OPEN-FLAGS C1).
