# Gate A0 (Typ C, Markenseite): Stürzl, Kanzlei (ST-43)

Datum: 2026-10-11. Seitentyp C (Brand-/About-Seite, kein Rankingziel). Regel: Bestand und alle Kundentexte zum Thema, kein Wort-Benchmark. Ein Vergleichssatz von Wettbewerber-Kanzleiseiten wurde trotzdem gemessen, weil Gate G6 einen gespeicherten Benchmark verlangt. Er setzt kein Wortziel.

| # | Datenpunkt | Vorhanden | Quelle und Datum |
| --- | --- | --- | --- |
| 1 | Source of Truth (Name, Leistungen, Anrede, Nicht-Liste) | ja | `content-pool/01-client/client-baseline.md`, `cro/04-copy/approved-copy.md`, `voice.md`, 2026-10-11. Adressen, Telefone und Telefonzeiten sind bestätigt: Source of Truth Tab 00 und Tab 02 Z38, `nap.json` und `source-of-truth-2026-10-11.md` (Korrektur von Martin, 2026-10-11). Die Notfallnummern stehen öffentlich auf der Live-Kontaktseite. |
| 2 | Live-Bestand abgerufen und gezählt | ja | /index.php/kanzlei: **1082 Wörter**, 1×H1 („Kanzlei“), 3×H2. `_work/bestand-metrics.json` (page_metrics.py), 2026-10-11. Rohtext `_work/live/kanzlei.txt`. |
| 3 | Alle Kundentexte zum Thema gelesen | ja | Live: Start, Kanzlei, Team, Dr. Stürzl, Dr. Glogger, Lea Wimmer, Kontakt, FAQ (Kostenteil). Kundentexte: `kosten.txt`, `compliance.txt`, `ki-baustein.txt`, `pruefung-2026-10-11.md`, `client-input-2026-10-11.md`. Freigegebene Startseite `approved-copy.md`. |
| 4 | Keyword und Suchvolumen | Marke, kein Ziel | „wirtschaftsstrafrecht kanzlei“ 110 (Startseite rankt #94), „steuerstrafrecht kanzlei“ 10. `03-demand/volume.json`, `ranked-stuerzl-steuerstrafrecht.de.json`, 2026-10-11. 10 heißt wenig Daten, nicht kaum Nachfrage. |
| 5 | SERP Top 10 | nicht nötig (Typ C) | Kein Rankingziel. Der Pool nennt 7 von 19 Wettbewerbern mit einer Über-uns-Seite (37 %), kein Pflichtbestandteil (`pool.json` CP-BRD-005). |
| 6 | Echte PAA-Fragen | nicht nötig (Typ C) | Besucherfragen (Kosten, Vertraulichkeit, Büros, Ansprechpersonen) stehen im Text. Brief: `paa_questions: []`. |
| 7 | Vergleichsmessung Wettbewerber (nur Info) | ja | 11 von 11 Kanzleiseiten gelesen, Median **633** Wörter. Kein Wortziel. Liste unten. `_work/bench-metrics.json`, 2026-10-11. |
| 8 | Lokaler Fakt | nicht nötig | Bundesweite Markenseite. Die Büros werden genannt, die Ortsarbeit läuft über ST-41 und ST-42. |

## Vergleichsmessung (Info)

| Wörter | Seite |
| --- | --- |
| 2059 | https://www.hortmannlaw.com/ueber-uns |
| 1501 | https://www.mtrlegal.com/kanzlei/ |
| 1275 | https://rechtinfo.de/ueber-uns/ueber-uns/ |
| 692 | https://kglaw.de/kanzlei/ |
| 665 | https://dreyenberg.com/de/kanzlei |
| 633 | https://www.kanzleimauss.de/kanzlei/ |
| 606 | https://rae-sus.de/kanzlei/ |
| 480 | https://www.dnk-rechtsanwaelte.de/de/kanzlei/philosophie/ |
| 323 | https://www.kanzlei-velke.de/de/kanzlei |
| 240 | https://www.michalkerosskopf.de/profil/ |
| 200 | https://www.kanzlei-velke.de/de/philosophie |

## Wortzahl-Urteil

Bestand 1082 Wörter. Wettbewerber-Median 633 (nur Information). Zielkorridor 1.082 bis 1.500. Der Bestand enthält 275 Wörter Kollegen- und Mandantenzitate mit Superlativen (gezählt mit wordcount.py auf dem Rohtext) und 191 Wörter Lebenslauf von Dr. Stürzl (der auf die Personenseite gehört). Diese Teile stehen nicht auf der neuen Seite. Die Mindestzahl wird mit Arbeitsweise, Einordnung des Rechtsgebiets, Honorar, Büros und Engagement erreicht, alles aus Kundentexten. Kein Füllmaterial.

## Konflikte im Bestand und bei Kundentexten

1. Die Live-Seite nutzt „hochspezialisiert“, „Experten“, „Expertise“, „Festpreis“, „beste Lösung“, „bestmöglich“, „ganzheitliche Beratung“, „hohe Spezialisierung“, „Leidenschaft“. Nicht übernommen (BRAO).
2. Neun Zitate von Kollegen und Mandanten mit Superlativen. Nicht übernommen.
3. „Erstberatung zum Festpreis“ (Live) gegen „Pauschale“ (Kundentext 09.10.). Platzhalter.
4. Kostenmodell RVG (Startseite) gegen Zeitaufwand (Kundentext). Seite folgt dem Kundentext.
5. Telefonzeiten, Adresse Frankfurt: bestätigt (Source of Truth), kein Platzhalter mehr. Die Zeiten der Notfallnummern sind nicht dokumentiert.

## Gate-Ergebnis

Alle Pflichtzeilen für Typ C vorhanden. Keine Blocker.
