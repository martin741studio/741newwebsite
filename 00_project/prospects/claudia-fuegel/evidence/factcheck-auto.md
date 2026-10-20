# Automatic fact check: Claudia Fügel (2026-10-16, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 139 · supported 131 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 5

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `system.step2.lead` | Zwei der vier ersten sind an allen 49 Messpunkten unter den ersten 20 zu sehen. | absolute word (allen) |
| `system.step2.changes[0].text` | Die offizielle Bestätigung schützt deinen Eintrag und schaltet alle Funktionen frei. | absolute word (alle) |
| `system.step3.five[1].a` | Stuttgart wird im ersten Bildschirm nicht genannt; die Adresse in Plieningen steht nur im Footer. | absolute word (nur) |
| `check[0].rows[1].title` | Immer verschlüsselt | absolute word (immer) |
| `check[0].rows[1].text` | Deine Seite öffnet sich immer mit dem Schloss-Symbol im Browser. | absolute word (immer) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 9 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 9 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 12 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `grid.h2` | 9 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 9 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 35 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 12 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `system.step2.lead` | Zwei der vier | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 0 / 5 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 / 6 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.score_draft_label` | 34 / 44 | evidence/scorecard-today.md |
| SUPPORTED | `check[1].rows[1].text` | 3 von 30 | derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 9 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 9 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 9 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 9 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 5,0 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `hero.sub` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 14 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 20 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `hero.cards[0].badge` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `hero.cards[0].badge` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[3].badge` | 12 | derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `hero.cards[3].badge` | 44 | derived (evidence_lib.facts), evidence/scorecard-today.md |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `grid.caption_today` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 100 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `grid.caption_goal` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `grid.caption_goal` | 48 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `system.steps[0].kpi` | 60.500 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.steps[1].kpi` | 20 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `system.steps[1].kpi` | 35 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.steps[2].kpi` | 12 | derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.steps[2].kpi` | 44 | derived (evidence_lib.facts), evidence/scorecard-today.md |
| SUPPORTED | `system.step1.h2` | 40 | cost_ledger.jsonl, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.h2` | 20 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `system.step1.demand_sub` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step1.demand_sub` | 12 | derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[0].volume` | 60500 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[1].volume` | 50 | demand.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-batch2.json |
| SUPPORTED | `system.step1.demand[2].volume` | 40 | cost_ledger.jsonl, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand_note` | 480 | demand.md, evidence/dfs-volumes-batch2.json |
| SUPPORTED | `system.step1.depth.sub` | 1.818 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[0].n` | 1.818 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[1].why` | 40 | cost_ledger.jsonl, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[2].why` | 50 | demand.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-batch2.json |
| SUPPORTED | `system.step1.items[3].why` | 480 | demand.md, evidence/dfs-volumes-batch2.json |
| SUPPORTED | `system.step1.items[5].why` | 15 | evidence/dfs-serp-astrologie-stuttgart.json, evidence/falcon-report-6ab0269fea7c8e3.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step2.h2` | 100 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 20 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `system.step2.lead` | 35 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].reviews` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[0].share` | 18,4 | derived (evidence_lib.facts), evidence/falcon-report-6ab0269fea7c8e3.json |
| SUPPORTED | `system.step2.table[1].reviews` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[1].share` | 100 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.table[2].reviews` | 33 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `system.step2.table[2].share` | 100 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.table[3].reviews` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED (rounded) | `system.step2.table[3].share` | 26,5 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 48 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED (rounded) | `system.step2.table[4].share` | 24,5 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.meaning` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.meaning` | 48 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `system.step2.meaning` | 5,0 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.meaning` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[2].text` | 15 | evidence/dfs-serp-astrologie-stuttgart.json, evidence/falcon-report-6ab0269fea7c8e3.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step2.changes[3].text` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[4].text` | 24 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `system.step2.cleanup[0].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.good` | 5,0 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step3.lead` | 22 | evidence/dfs-serp-astrologie-stuttgart.json, evidence/falcon-report-6ab0269fea7c8e3.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step3.score_today` | 12 | derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json, evidence/dfs-volumes-ads.json |
| ASSUMPTION | `system.step3.score_draft` | 12 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 34 | derived (evidence_lib.facts), evidence/falcon-report-6ab0269fea7c8e3.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step3.score_draft_label` | 44 | derived (evidence_lib.facts), evidence/scorecard-today.md |
| SUPPORTED | `system.step3.note_draft` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step3.note_draft` | 15 | evidence/dfs-serp-astrologie-stuttgart.json, evidence/falcon-report-6ab0269fea7c8e3.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step3.strip[1].why` | 24 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `calc.vol` | 40 | cost_ledger.jsonl, demand.md, evidence/dfs-volumes-ads.json |
| ASSUMPTION | `calc.vol_min` | 40 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 1 | competitors.md, demand.md, derived (evidence_lib.facts) |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 150 | evidence/dfs-serp-astrologie-stuttgart.json, evidence/site-price-page.txt |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val_label` | 150 | evidence/dfs-serp-astrologie-stuttgart.json, evidence/site-price-page.txt |
| SUPPORTED | `calc.volumes_line` | 40 | cost_ledger.jsonl, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 50 | demand.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-batch2.json |
| SUPPORTED | `calc.volumes_line` | 480 | demand.md, evidence/dfs-volumes-batch2.json |
| SUPPORTED | `calc.volumes_line` | 150 | evidence/dfs-serp-astrologie-stuttgart.json, evidence/site-price-page.txt |
| SUPPORTED | `calc.volumes_line` | 120 | evidence/site-price-page.txt |
| SUPPORTED | `calc.volumes_line` | 180 | evidence/site-price-page.txt |
| SUPPORTED | `calc.volumes_line` | 1,5 | evidence/site-price-page.txt |
| SUPPORTED (rounded) | `check[0].rows[2].text` | 1,7 | derived (evidence_lib.facts), evidence/site.json |
| SUPPORTED | `check[1].rows[1].text` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[1].text` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `check[3].rows[0].title` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `check[3].rows[0].text` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `check[3].rows[0].text` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[1].text` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[1].text` | 48 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `check[3].rows[1].text` | 33 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `check[3].rows[2].text` | 6 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[3].text` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `quick_wins[3].text` | 15 | evidence/dfs-serp-astrologie-stuttgart.json, evidence/falcon-report-6ab0269fea7c8e3.json, evidence/scorecard-today.md |
| SUPPORTED | `roadmap[1].why` | 100 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `roadmap[2].what` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `roadmap[2].what` | 15 | evidence/dfs-serp-astrologie-stuttgart.json, evidence/falcon-report-6ab0269fea7c8e3.json, evidence/scorecard-today.md |
| SUPPORTED | `final.h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `final.p` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `guide.point` | 100 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `guide.point` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.point` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 5,0 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `headlines.hero_sub` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 14 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 20 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `headlines.grid_h2` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 40 | cost_ledger.jsonl, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.step1_h2` | 20 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `headlines.step2_h2` | 100 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `headlines.roadmap_h2` | 8 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-astrologie-stuttgart.json |
| SUPPORTED | `headlines.final_h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
