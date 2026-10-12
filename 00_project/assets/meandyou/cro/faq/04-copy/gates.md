# Gate report 2026-10-12
Page: `page.md`. Result: **PASS**

| Gate | Result | Findings |
| --- | --- | --- |
| G1 facts | PASS | none |
| G2 legal | PASS | none |
| G3 seo | PASS | none |
| G4 style | PASS | none |
| G5 slop (lint) | PASS | none |
| G6 seo/geo coverage + schema | PASS | none |

## Warnings

- G1 facts: Claims nicht verwendet: ['C05', 'S21', 'S22', 'M05', 'R03', 'R04']
- G6 seo/geo coverage + schema: Begriffs- und Norm-Prüfung nicht gelaufen (mit --fetch starten)

## Slop-Schleife (G5)


cleanse_de: what changed -
- Kontrastformel „Nicht anders werden, klarer werden.“ auf „Klarer werden.“ gekürzt. Übrige Sätze ohne eindeutigen Tell wortgleich belassen.
- 741: Änderung abgelehnt. „Nicht anders werden, klarer werden.“ ist eine eigene Wendung des Kunden (Live-FAQ, voice.md, Startseite). draft-v2 bleibt unverändert.
R2 cleanse_de: what changed -
R2 - Dreierfolge „Preis, passendes Seminar und freie Plätze“ aufgelöst; „Den Preis ebenfalls.“ setzt einen kurzen Gegenrhythmus.
R2 - Werblicher Dreiklang „dein Seminar, deinen Ort und deinen Termin“ in eine schlichte Aussage umgebaut. Entscheidung als kurzen Satz abgesetzt.
R2 - Sachliche Dreierlisten und Originalzitate beibehalten.
- 741 Runde 2: Abschluss-Satz übernommen; Antwort-Block umformuliert ohne Satzfragment „Den Preis ebenfalls.“; Tippfehler „Ebenenen“ abgelehnt. Ergebnis draft-v4.md.

diff_claims.py diff draft-v2 → cleansed: PASS; draft-v3 → cleansed: PASS

## Frischer Reviewer (Subagent, 2026-10-12)

Score 80/100 auf draft-v2, 14 Lücken. Behoben in draft-v3/v4: Bundle-Ausnahme (4 Tage nur für die drei Seminare), Seminarleitung nur mit gelber Marke, Verkaufsgespräch ehrlich beantwortet, Workbooks nur für „Ruhig bleiben“, „acht weitere Termine“ auf die drei Seminare bezogen, Anreise ergänzt, Gruppengröße 10, 12 oder 14 Plätze, Hallstadt-Satz, Verpflegung-Marke im Preis, Übungs-Frage = PAA-Wortlaut, Fortschritt ohne Ergebnisversprechen, Peter Escher wörtlich, Zitat im Antwort-Block Jasmina L. statt „Redeangst“, VR-Beschreibung als Zitat. Nicht übernommen: CTA-Ziel /gespraech-buchen statt termin.html (Auftrag nennt termin.html für den Prototyp, Flag Q13); Christian-S.-Zitat bleibt (auf Michael-Seite freigegeben, Flag Q11).

## Link-Netz und Ähnlichkeit (G6c, link_network.py --final)

PASS, 6 Seiten. FAQ: 6 ausgehende, 4 eingehende Textlinks. Ähnlichkeit (5-Wort-Shingles) zu Startseite 6,5 %, Seminare 5,3 %, Michael 6,3 %, Rhetorik 2,7 %, Gespräch buchen 3,1 % (Grenze 25 %).

Wörter: 2.004 (Bestand v2 286, Benchmark-Median 858, Zielbereich 1.600 bis 2.600). 52 Fragen in 7 Gruppen.
