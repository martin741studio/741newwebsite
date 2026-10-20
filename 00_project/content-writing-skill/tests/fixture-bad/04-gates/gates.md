# Gate report 2026-10-12
Page: `draft-v1.md`. Result: **FAIL**

| Gate | Result | Findings |
| --- | --- | --- |
| G1 facts | FAIL | Zahlen ohne Beleg in der Claim-Liste: ['500']; Pflicht-Claims fehlen im Text: ['C01'] |
| G2 legal | FAIL | Spezialisierung / Experte ohne Titel: "spezialist"; Ergebnisversprechen: "garantieren"; Ergebnisversprechen: "straffreiheit" |
| G3 seo | FAIL | Title 83 Zeichen (max 60); H1-Anzahl 2 (genau 1 nötig); Abschnitts-IDs weichen vom Plan ab: Seite ['S01'] gegen Plan ['S01', 'S02', 'S03', 'S04', 'S05']; Wortzahl 36 unter Bestand 60; Direkt-Antwort-Block fehlt (Abschnitt mit element: answer); FAQ: 0 Fragen (mindestens 2, Format '### Frage?'); interne Links im sichtbaren Text: 0 (mindestens 1); CTA-Abschnitte: 1 (mindestens 2); Primärer CTA-Text "Vertraulich anfragen" fehlt |
| G4 style | FAIL | Gedankenstrich im Frontmatter title; Gedankenstrich — x1 |
| G5 slop (lint) | FAIL | vocabulary: ganzheitliche, nahtlos, maßgeschneidert; constructions: nicht nur ..., sondern auch: "nicht nur um ihr steuerproblem, sondern", es geht nicht um X, sondern um Y: "es geht nicht nur um ihr steuerproblem, sondern", Zeitgeist-Einstieg: "in der heutigen"; punctuation: Gedankenstrich — x1; invented proof: "über 500 mandanten" ohne Beleg in der Claim-Liste |
| G6 seo/geo coverage + schema | FAIL | kein Benchmark gespeichert (_work/bench-metrics.json fehlt oder leer); H2 Direkt-Antwort-Block fehlt; H7 keine belegte Qualifikation sichtbar auf der Seite (E-E-A-T); brief.nap_file fehlt (Schema braucht gesperrte Stammdaten) |

## Warnings

- G3 seo: Haupt-Keyword "selbstanzeige anwalt" nicht (vollständig) im H1
- G3 seo: Technik-Block (<!-- TECH -->) fehlt
- G6 seo/geo coverage + schema: brief.paa_questions fehlt (PAA-Prüfung nicht möglich)
