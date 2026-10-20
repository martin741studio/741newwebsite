# Automatic fact check: Manuela Stetter (2026-10-14, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 207 · supported 199 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 18

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `grid.h2` | Sichtbar nur am Nordrand, in der Stadtmitte nicht unter den ersten 20. | absolute word (nur) |
| `grid.caption_today` | Zu sehen bist du nur am Nordrand der Karte: | absolute word (nur) |
| `system.intro` | Im Rechner sind nur Budget, Anfrage- und Buchungsanteil Annahmen. | absolute word (nur) |
| `system.step1.demand_note` | Google zählt „heilpraktikerin landshut“ bei „heilpraktiker landshut“ mit, darum steht die Zahl nur einmal da. | absolute word (nur) |
| `system.step1.items[5].why` | Deine Adresse in Mirskofen steht nur ganz unten auf der Seite, ohne Karte und ohne Zeiten. | absolute word (nur) |
| `system.step2.lead` | Zwei der vier ersten sind an allen 49 Messpunkten unter den ersten 20 zu sehen. | absolute word (allen) |
| `system.step2.changes[0].text` | Agata Block steht als „Heilpraktiker“ eingeordnet und ist an allen 49 Punkten unter den ersten 20. | absolute word (allen) |
| `system.step2.changes[0].text` | Bei dir steht nur „Naturheilpraktiker“, als einzige Einordnung. | absolute word (nur) |
| `system.step2.changes[1].title` | Alle Leistungen eintragen | absolute word (alle) |
| `system.step2.changes[3].text` | Ohne Antwort sind nur ältere, 6 bis 9 Jahre alt. | absolute word (nur) |
| `system.step2.cleanup[1].text` | Google bekommt von deiner Seite 28 Adressen, nur 9 davon sind Praxis-Seiten. | absolute word (nur) |
| `system.step2.cleanup[3].text` | Eine Adresse überall ist klarer. | absolute word (überall) |
| `system.step3.five[3].a` | „Termine buchen“ ist nur ein Punkt in der zweiten Menüzeile. | absolute word (nur) |
| `check[0].rows[1].title` | Immer verschlüsselt | absolute word (immer) |
| `check[0].rows[1].text` | Deine Seite öffnet sich immer mit dem Schloss-Symbol im Browser, auch die Adresse ohne „https“ leitet richtig weiter. | absolute word (immer) |
| `check[1].rows[2].text` | Google bekommt von deiner Seite 28 Adressen, nur 9 davon sind Praxis-Seiten. | absolute word (nur) |
| `roadmap[0].what` | Demo- und Autoren-Seiten löschen, Seitentitel und Beschreibung bei Google neu, eine E-Mail-Adresse überall, unseriöse Links melden | absolute word (überall) |
| `headlines.grid_h2` | Sichtbar nur am Nordrand, in der Stadtmitte nicht unter den ersten 20. | absolute word (nur) |
| (text) | heilpraktiker landshut + heilpraktikerin landshut | both forms named: say that Google counts them together (320), never add them up |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.cards[1].sub` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].badge` | 29 von 39 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 12 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `grid.h2` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 7 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 12 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `system.step1.depth.note` | Eine der fünf | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | Zwei der vier | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[3].text` | 29 von 39 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 20 / 39 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].text` | 8/9 | evidence/site-pages.json |
| SUPPORTED | `check[3].rows[2].text` | 29 von 39 | derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[3].text` | 20 von 39 | derived (evidence_lib.facts) |
| SUPPORTED | `quick_wins[3].text` | 8/9 | evidence/site-pages.json |
| SUPPORTED | `headlines.hero_h1` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 0 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.sub` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 31 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `hero.sub` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[0].badge` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[0].badge` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 31 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `hero.cards[2].badge` | 29 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `hero.cards[2].badge` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[3].badge` | 12 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 44 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-1.json |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.h2` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 14.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 8,3 | competitors.md |
| SUPPORTED | `grid.caption_today` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 12 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 15 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `grid.caption_today` | 18 | competitors.md, demand.md, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `grid.caption_today` | 19 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `grid.caption_today` | 42 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 100 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `grid.caption_goal` | 320 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_goal` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_goal` | 31 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `grid.caption_goal` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[0].kpi` | 320 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 7 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 12 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 44 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-1.json |
| SUPPORTED | `system.step1.h2` | 320 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand_sub` | 14.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step1.demand_sub` | 12 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand[0].volume` | 880 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[1].volume` | 480 | demand.md, evidence/dfs-volumes-ads.json, evidence/site-pages.json |
| SUPPORTED | `system.step1.demand[2].volume` | 320 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand[3].volume` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[4].volume` | 70 | demand.md, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step1.demand[5].volume` | 40 | competitors.md, demand.md, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.demand[6].volume` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand[7].volume` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand[8].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[9].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_note` | 320 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.depth.sub` | 7 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.big[0].n` | 477 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.depth.big[1].label` | 7 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[0].val` | 477 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.bars[1].label` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.depth.bars[1].val` | 516 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[0].why` | 7 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[1].why` | 320 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[1].why` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[2].why` | 880 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[2].why` | 150 | evidence/home-images.txt, evidence/scorecard-today.md, evidence/visual-check.md |
| SUPPORTED | `system.step1.items[2].why` | 60 | demand.md, evidence/dfs-refdomains-spam.json, evidence/falcon-report-0e90f7a9f4d310d.json |
| SUPPORTED | `system.step1.items[3].why` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[3].why` | 40 | competitors.md, demand.md, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.items[4].why` | 480 | demand.md, evidence/dfs-volumes-ads.json, evidence/site-pages.json |
| SUPPORTED | `system.step2.h2` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 7 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].reviews` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].share` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[1].reviews` | 31 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `system.step2.table[1].share` | 100 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.table[2].reviews` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[2].share` | 93,9 | competitors.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[3].share` | 36,7 | competitors.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[4].share` | 16,3 | competitors.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 14.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 31 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `system.step2.meaning` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 0,2 | competitors.md, derived (evidence_lib.facts), intake.json |
| SUPPORTED | `system.step2.meaning` | 2,2 | competitors.md |
| SUPPORTED | `system.step2.meaning` | 8,3 | competitors.md |
| SUPPORTED | `system.step2.meaning` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 44 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-1.json |
| SUPPORTED | `system.step2.meaning` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[0].text` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[0].text` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[2].text` | 7 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[3].text` | 29 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `system.step2.changes[3].text` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[3].text` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[3].text` | 9 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[1].n` | 9 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].text` | 28 | derived (evidence_lib.facts), evidence/comp-pages.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.cleanup[1].text` | 9 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].text` | 8 | evidence/comp-pages.json, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.cleanup[1].text` | 9 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].text` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].text` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[2].n` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].text` | 242 | evidence/site-pages.json, evidence/site.json, site-findings.md |
| SUPPORTED | `system.step2.cleanup[3].n` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.good` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 22 | evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step3.score_today` | 12 | competitors.md, demand.md, derived (evidence_lib.facts) |
| ASSUMPTION | `system.step3.score_draft` | 36 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | evidence/dfs-refdomains-spam.json, evidence/dfs-serp-name2.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step3.score_draft_label` | 44 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-1.json |
| SUPPORTED | `system.step3.note_today` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.note_draft` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.note_draft` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.note_draft` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.note_draft` | 15 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step3.five[2].a` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.five[2].a` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.vol` | 320 | competitors.md, demand.md, derived (evidence_lib.facts) |
| ASSUMPTION | `calc.vol_min` | 50 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 3200 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 1.0 | competitors.md, cost_ledger.jsonl, demand.md |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 300 | evidence/home-images.txt, evidence/visual-check.md, site-findings.md |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val_label` | 60 | demand.md, evidence/dfs-refdomains-spam.json, evidence/falcon-report-0e90f7a9f4d310d.json |
| SUPPORTED | `calc.volumes_line` | 14.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `calc.volumes_line` | 12 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `calc.volumes_line` | 320 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `calc.volumes_line` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 1,00 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 1,00 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 150 | evidence/home-images.txt, evidence/scorecard-today.md, evidence/visual-check.md |
| SUPPORTED | `calc.volumes_line` | 60 | demand.md, evidence/dfs-refdomains-spam.json, evidence/falcon-report-0e90f7a9f4d310d.json |
| SUPPORTED | `check[0].rows[2].text` | 0,2 | competitors.md, derived (evidence_lib.facts), intake.json |
| SUPPORTED | `check[0].rows[3].text` | 15 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `check[1].rows[2].text` | 28 | derived (evidence_lib.facts), evidence/comp-pages.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `check[1].rows[2].text` | 9 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[2].text` | 242 | evidence/site-pages.json, evidence/site.json, site-findings.md |
| SUPPORTED | `check[1].rows[2].text` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[1].rows[4].text` | 477 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `check[1].rows[4].text` | 516 | derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[4].text` | 1.346 | evidence/site-pages.json, site-findings.md |
| SUPPORTED | `check[3].rows[0].title` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[0].text` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[0].text` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 31 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `check[3].rows[1].text` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[1].text` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[1].text` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[2].text` | 29 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `check[3].rows[2].text` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[3].text` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[3].text` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[1].text` | 15 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `quick_wins[2].title` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `quick_wins[2].text` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `quick_wins[2].text` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[3].text` | 8 | evidence/comp-pages.json, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `quick_wins[3].text` | 9 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `quick_wins[3].text` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `quick_wins[3].text` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `roadmap[2].what` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `final.h2` | 30 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `final.p` | 30 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `guide.point` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.point` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `guide.celebrate` | 85 | evidence/dfs-serp-name.json, evidence/dfs-serp-name2.json, evidence/falcon-report-0e90f7a9f4d310d.json |
| SUPPORTED | `guide.celebrate` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 11 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 31 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `headlines.hero_sub` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 320 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step2_h2` | 39 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.roadmap_h2` | 8 | evidence/comp-pages.json, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `headlines.final_h2` | 30 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
