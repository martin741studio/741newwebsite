# Automatic fact check: Lena Fistler (2026-10-16, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 148 · supported 140 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 9

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `system.step2.h2` | Selbst die führende Praxis erreicht nur 8,2 % der Karte. | absolute word (nur) |
| `system.step2.lead` | Null der vier ersten sind an allen 49 Messpunkten unter den ersten 20 zu sehen. | absolute word (allen) |
| `system.step2.changes[0].text` | Die Bestätigung schützt dein Profil und schaltet alle Funktionen frei. | absolute word (alle) |
| `system.step3.five[0].a` | Der Begriff Körpertherapie steht nur klein im Logo-Schriftzug. | absolute word (nur) |
| `check[0].rows[1].title` | Immer verschlüsselt | absolute word (immer) |
| `check[0].rows[1].text` | Deine Seite öffnet sich immer mit dem Schloss-Symbol im Browser. | absolute word (immer) |
| `check[1].rows[1].text` | 15 von 17 Unterseiten haben keine Hauptüberschrift (nur Datenschutz und Impressum nutzen ein H1-Tag). | absolute word (nur) |
| `guide.point` | Selbst der Spitzenreiter hat nur 8,2 % Sichtbarkeit. | absolute word (nur) |
| `headlines.step2_h2` | Selbst die führende Praxis erreicht nur 8,2 % der Karte. | absolute word (nur) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 13 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `grid.h2` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 35 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 13 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `system.step2.lead` | Null der vier | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 / 2 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.score_draft_label` | 36 / 44 | evidence/scorecard-today.md |
| SUPPORTED | `check[1].rows[1].text` | 15 von 17 | derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 5 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 14 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-craniosacrale-osteopathie.json |
| SUPPORTED | `hero.sub` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[0].badge` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[0].badge` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 35 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 13 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 44 | derived (evidence_lib.facts), evidence/dfs-serp-heilpraktikerin-muenchen.json, evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED (rounded) | `grid.caption_today` | 8,2 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_goal` | 1 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_goal` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[0].kpi` | 170 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `system.steps[1].kpi` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[1].kpi` | 35 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 13 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 44 | derived (evidence_lib.facts), evidence/dfs-serp-heilpraktikerin-muenchen.json, evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `system.step1.h2` | 110 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.h2` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_sub` | 15.10.2026 | cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_sub` | 12 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[0].volume` | 170 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `system.step1.demand[1].volume` | 110 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[2].volume` | 90 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `system.step1.demand[3].volume` | 70 | demand.md, evidence/dfs-name-lena-fistler.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[4].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[5].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_note` | 110 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand_note` | 90 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `system.step1.depth.sub` | 253 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[0].n` | 253 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[1].why` | 90 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `system.step1.items[3].why` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED (rounded) | `system.step2.h2` | 8,2 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.lead` | 35 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].reviews` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].share` | 10,2 | derived (evidence_lib.facts), evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `system.step2.table[1].reviews` | 35 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[1].share` | 8,2 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[2].reviews` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[2].share` | 8,2 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 1 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[3].share` | 6,1 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[4].share` | 6,1 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 1 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[2].text` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[2].text` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[0].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[0].n` | 1 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[1].n` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.lead` | 22 | evidence/dfs-serp-craniosacrale-osteopathie.json, evidence/dfs-serp-heilpraktikerin-muenchen.json, evidence/dfs-serp-koerpertherapie-muenchen.json |
| SUPPORTED | `system.step3.score_today` | 13 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| ASSUMPTION | `system.step3.score_draft` | 13 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | evidence/dfs-serp-koerpertherapie-muenchen.json, evidence/falcon-report-4fe389eb4e0685a.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step3.score_draft_label` | 44 | derived (evidence_lib.facts), evidence/dfs-serp-heilpraktikerin-muenchen.json, evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `system.step3.note_draft` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `calc.vol` | 110 | demand.md, evidence/dfs-volumes-ads.json |
| ASSUMPTION | `calc.vol_min` | 50 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 1.5 | evidence/dfs-volumes-ads.json |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 100 | evidence/dfs-refdomains-spam.json, evidence/falcon-report-4fe389eb4e0685a.json, prospect-mini/case-library.json |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val_label` | 100 | evidence/dfs-refdomains-spam.json, evidence/falcon-report-4fe389eb4e0685a.json, prospect-mini/case-library.json |
| SUPPORTED | `calc.volumes_line` | 15.10.2026 | cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 12 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 110 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 90 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `calc.volumes_line` | 1,52 | evidence/dfs-volumes-ads.json |
| SUPPORTED (rounded) | `calc.volumes_line` | 1,50 | evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 100 | evidence/dfs-refdomains-spam.json, evidence/falcon-report-4fe389eb4e0685a.json, prospect-mini/case-library.json |
| SUPPORTED | `calc.volumes_line` | 99 | evidence/falcon-report-4fe389eb4e0685a.json, evidence/site-price-page.txt, site-findings.md |
| SUPPORTED | `check[0].rows[2].text` | 0,8 | evidence/falcon-report-4fe389eb4e0685a.json |
| SUPPORTED | `check[1].rows[1].text` | 15 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[1].text` | 17 | derived (evidence_lib.facts), evidence/demand-menu-homepage.txt, evidence/dfs-name-lena-fistler.json |
| SUPPORTED | `check[1].rows[1].text` | 1 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[2].rows[1].text` | 14 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-craniosacrale-osteopathie.json |
| SUPPORTED | `check[2].rows[1].text` | 166 | derived (evidence_lib.facts), evidence/demand-menu-homepage.txt, evidence/dfs-name-lena-fistler.json |
| SUPPORTED | `check[3].rows[0].title` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[0].text` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[0].text` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 35 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[1].text` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[2].text` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[3].text` | 1 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `quick_wins[0].text` | 14 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-craniosacrale-osteopathie.json |
| SUPPORTED | `quick_wins[0].text` | 166 | derived (evidence_lib.facts), evidence/demand-menu-homepage.txt, evidence/dfs-name-lena-fistler.json |
| SUPPORTED | `quick_wins[3].title` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `quick_wins[3].text` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `quick_wins[5].text` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[5].text` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `roadmap[1].why` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `roadmap[2].what` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `final.h2` | 30 | demand.md, evidence/dfs-serp-craniosacrale-osteopathie.json, evidence/dfs-serp-heilpraktikerin-muenchen.json |
| SUPPORTED | `final.p` | 30 | demand.md, evidence/dfs-serp-craniosacrale-osteopathie.json, evidence/dfs-serp-heilpraktikerin-muenchen.json |
| SUPPORTED (rounded) | `guide.point` | 8,2 | derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `guide.insight` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 5,0 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 14 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-craniosacrale-osteopathie.json |
| SUPPORTED | `headlines.hero_sub` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.grid_h2` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 110 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.step1_h2` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED (rounded) | `headlines.step2_h2` | 8,2 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.roadmap_h2` | 8 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.final_h2` | 30 | demand.md, evidence/dfs-serp-craniosacrale-osteopathie.json, evidence/dfs-serp-heilpraktikerin-muenchen.json |
