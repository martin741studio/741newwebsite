# Automatic fact check: Yvonne Bossard-Serio (2026-10-29, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 105 · supported 97 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 7

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `system.step1.items[3].why` | Die Adresse steht nur im Footer und auf der Kontakt-Seite. | absolute word (nur) |
| `system.step1.items[5].why` | Die Überschrift der Seite „Über mich“ lautet nur „Über mich“, ohne Titel und Ort. | absolute word (nur) |
| `system.step2.changes[0].text` | Die vier vorn haben alle eine Naturheil-Kategorie. | absolute word (alle) |
| `system.step2.changes[1].title` | Alle Leistungen eintragen | absolute word (alle) |
| `system.step3.five[1].a` | Die Adresse steht nur im Footer. | absolute word (nur) |
| `system.step3.five[3].a` | Kein Termin-Button im ersten Bildschirm, nur die Navigation. | absolute word (nur) |
| `quick_wins[1].text` | Auf der Startseite nur eine Hauptüberschrift. | absolute word (nur) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.cards[1].sub` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 3 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `grid.caption_today` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 3 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `check[1].rows[1].text` | 6 von 27 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 49 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `hero.sub` | 20 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `hero.cards[1].sub` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `hero.cards[1].sub` | 49 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `hero.cards[1].sub` | 20 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `hero.cards[2].sub` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `hero.cards[2].sub` | 10 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `hero.cards[2].sub` | 24 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED | `hero.cards[3].badge` | 3 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `hero.cards[3].badge` | 44 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/scorecard-today.md |
| SUPPORTED | `grid.grid_size` | 7 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `grid.intro` | 29.10.2026 | cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 49 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `grid.intro` | 5 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `grid.alt` | 49 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `grid.alt` | 20 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `grid.caption_today` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `grid.caption_today` | 49 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `grid.caption_today` | 49 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `grid.caption_today` | 20 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `grid.caption_today` | 51 | evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED | `grid.caption_goal` | 10 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `grid.caption_goal` | 24 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED | `grid.caption_goal` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `system.steps[0].kpi` | 110 | evidence/dfs-maps-serp2.json, evidence/dfs-volumes.json |
| SUPPORTED | `system.steps[1].kpi` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `system.steps[1].kpi` | 49 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `system.steps[2].text` | 5 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `system.steps[2].kpi` | 3 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `system.steps[2].kpi` | 44 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step1.demand_sub` | 29.10.2026 | cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand[0].volume` | 110 | evidence/dfs-maps-serp2.json, evidence/dfs-volumes.json |
| SUPPORTED | `system.step1.demand[1].volume` | 110 | evidence/dfs-maps-serp2.json, evidence/dfs-volumes.json |
| SUPPORTED | `system.step1.depth.big[0].n` | 643 | derived (evidence_lib.facts), evidence/site-check-notes.md, evidence/site-pages.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `system.step1.items[1].why` | 110 | evidence/dfs-maps-serp2.json, evidence/dfs-volumes.json |
| SUPPORTED | `system.step1.items[1].why` | 27 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/site-check-notes.md |
| SUPPORTED | `system.step1.items[2].why` | 110 | evidence/dfs-maps-serp2.json, evidence/dfs-volumes.json |
| SUPPORTED | `system.step1.items[2].why` | 27 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/site-check-notes.md |
| SUPPORTED | `system.step1.items[4].why` | 60 | evidence/dfs-maps-serp2.json, evidence/site-pages.json, evidence/site-prices.md |
| SUPPORTED | `system.step1.items[4].why` | 140 | evidence/dfs-volumes.json, evidence/site-pages.json, evidence/site-prices.md |
| SUPPORTED | `system.step2.lead` | 51 | evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED | `system.step2.lead` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `system.step2.table[0].reviews` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `system.step2.table[0].share` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `system.step2.table[1].reviews` | 18 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `system.step2.table[1].share` | 51 | evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED | `system.step2.table[2].reviews` | 10 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED (rounded) | `system.step2.table[2].share` | 26,5 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 24 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED (rounded) | `system.step2.table[3].share` | 26,5 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 24 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED (rounded) | `system.step2.table[4].share` | 16,3 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 29.10.2026 | cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 49 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `system.step2.fine` | 5 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `system.step2.meaning` | 10 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `system.step2.meaning` | 24 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED | `system.step2.meaning` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `system.step2.cleanup[0].n` | 1 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `system.step2.cleanup[1].n` | 3 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `system.step2.cleanup[2].n` | 91 | evidence/dfs-maps-serp2.json, evidence/site-check-notes.md, prospect-mini/case-library.json |
| SUPPORTED | `system.step3.lead` | 22 | evidence/dfs-maps-serp2.json, evidence/scorecard-today.md, evidence/site-check-notes.md |
| SUPPORTED | `system.step3.score_today` | 3 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| ASSUMPTION | `system.step3.score_draft` | 36 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | cost_ledger.jsonl, evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `system.step3.score_draft_label` | 44 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step3.note_draft` | 5 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `calc.vol` | 110 | evidence/dfs-maps-serp2.json, evidence/dfs-volumes.json |
| ASSUMPTION | `calc.vol_min` | 50 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 4 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 150 | evidence/site-prices.md |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val_label` | 60 | evidence/dfs-maps-serp2.json, evidence/site-pages.json, evidence/site-prices.md |
| SUPPORTED | `calc.val_label` | 140 | evidence/dfs-volumes.json, evidence/site-pages.json, evidence/site-prices.md |
| SUPPORTED | `calc.volumes_line` | 110 | evidence/dfs-maps-serp2.json, evidence/dfs-volumes.json |
| SUPPORTED | `calc.volumes_line` | 110 | evidence/dfs-maps-serp2.json, evidence/dfs-volumes.json |
| SUPPORTED | `calc.volumes_line` | 4 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `calc.volumes_line` | 2026 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED (rounded) | `check[0].rows[2].text` | 2,2 | derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `check[0].rows[2].text` | 0,9 | evidence/dfs-volumes.json, evidence/site.json |
| SUPPORTED | `check[0].rows[2].text` | 4,2 | evidence/dfs-maps-serp2.json |
| SUPPORTED | `check[1].rows[1].text` | 6 | derived (evidence_lib.facts), evidence/dfs-gbp-info.json, evidence/dfs-gbp-info2.json |
| SUPPORTED | `check[1].rows[1].text` | 27 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/site-check-notes.md |
| SUPPORTED | `check[1].rows[2].text` | 91 | evidence/dfs-maps-serp2.json, evidence/site-check-notes.md, prospect-mini/case-library.json |
| SUPPORTED | `check[1].rows[2].text` | 55 | evidence/dfs-maps-serp2.json, evidence/site-check-notes.md, evidence/site-pages.json |
| SUPPORTED | `check[3].rows[0].text` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `check[3].rows[0].text` | 10 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `check[3].rows[0].text` | 24 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED | `quick_wins[2].text` | 91 | evidence/dfs-maps-serp2.json, evidence/site-check-notes.md, prospect-mini/case-library.json |
| SUPPORTED | `roadmap[1].why` | 10 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `roadmap[1].why` | 24 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED | `roadmap[1].why` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `final.p` | 30 | cost_ledger.jsonl, evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `guide.point` | 49 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
| SUPPORTED | `guide.point` | 20 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `guide.insight` | 10 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `guide.insight` | 24 | derived (evidence_lib.facts), evidence/dfs-maps-serp2.json, evidence/falcon-report-f2f576a1f993b40.json |
| SUPPORTED | `guide.insight` | 0 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-gbp-info.json |
| SUPPORTED | `guide.celebrate` | 8 | derived (evidence_lib.facts), evidence/dfs-maps-serp.json, evidence/dfs-maps-serp2.json |
