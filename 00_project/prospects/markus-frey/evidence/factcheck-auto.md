# Automatic fact check: Markus Frey (2026-10-16, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 139 · supported 131 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 6

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `hero.cards[3].badge` | 13 von 42 | count claim without a derived count |
| `system.steps[2].kpi` | 13 von 42 | count claim without a derived count |
| `system.step2.lead` | Null der vier ersten sind an allen 49 Messpunkten unter den ersten 20 zu sehen. | absolute word (allen) |
| `system.step2.table[3].name` | Anfänge aller Art • Coaching und psychologische Beratung • Köln | absolute word (aller) |
| `system.step2.changes[1].title` | Alle Leistungen eintragen | absolute word (alle) |
| `check[0].rows[1].title` | Immer verschlüsselt | absolute word (immer) |
| `check[0].rows[1].text` | Deine Seite öffnet sich immer mit dem Schloss-Symbol im Browser. | absolute word (immer) |
| `quick_wins[4].text` | Alle Coaching-Leistungen und genaue Öffnungszeiten im Profil hinterlegen. | absolute word (alle) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 5 von 49 | derived (evidence_lib.facts) |
| NO PAIR | `hero.cards[3].badge` | 13 von 42 | no derived count with total 42: the agent checks it |
| SUPPORTED | `grid.h2` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 9 von 49 | derived (evidence_lib.facts) |
| NO PAIR | `system.steps[2].kpi` | 13 von 42 | no derived count with total 42: the agent checks it |
| SUPPORTED | `system.step2.lead` | Null der vier | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 34 / 95 | derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[1].text` | 1 von 30 | derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[3].text` | 34 von 95 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 5 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.sub` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[0].badge` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[0].badge` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 17 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `hero.cards[3].badge` | 13 | cost_ledger.jsonl, evidence/dfs-backlinks-summary.json, evidence/dfs-name-stressfrey.json |
| SUPPORTED | `hero.cards[3].badge` | 42 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `grid.caption_today` | 42,9 | derived (evidence_lib.facts), evidence/falcon-report-5bd7097be1b0e31.json |
| SUPPORTED | `grid.caption_goal` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `grid.caption_goal` | 17 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `grid.caption_goal` | 42 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.steps[0].kpi` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[2].kpi` | 13 | cost_ledger.jsonl, evidence/dfs-backlinks-summary.json, evidence/dfs-name-stressfrey.json |
| SUPPORTED | `system.steps[2].kpi` | 42 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.h2` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand_sub` | 15.10.2026 | cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_sub` | 12 | demand.md, evidence/dfs-name-stressfrey.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.demand[0].volume` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[1].volume` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand[2].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[3].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[4].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_note` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.depth.sub` | 324 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[0].n` | 324 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[1].why` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[2].why` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].reviews` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].share` | 10,2 | derived (evidence_lib.facts), evidence/falcon-report-5bd7097be1b0e31.json |
| SUPPORTED | `system.step2.table[1].reviews` | 17 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED (rounded) | `system.step2.table[1].share` | 42,9 | derived (evidence_lib.facts), evidence/falcon-report-5bd7097be1b0e31.json |
| SUPPORTED | `system.step2.table[2].reviews` | 26 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED (rounded) | `system.step2.table[2].share` | 28,6 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 42 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED (rounded) | `system.step2.table[3].share` | 26,5 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 27 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED (rounded) | `system.step2.table[4].share` | 20,4 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 17 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.meaning` | 42 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.meaning` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[2].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[2].text` | 15 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 34 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.cleanup[0].n` | 95 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 22 | evidence/dfs-backlinks-summary.json, evidence/dfs-serp-life-coach-koeln.json, evidence/dfs-serp-stresscoaching-koeln.json |
| SUPPORTED | `system.step3.score_today` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| ASSUMPTION | `system.step3.score_draft` | 0 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 34 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step3.score_draft_label` | 42 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `calc.vol` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| ASSUMPTION | `calc.vol_min` | 50 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 2.5 | evidence/dfs-volumes-ads.json |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 300 | evidence/site-urls.json |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val_label` | 300 | evidence/site-urls.json |
| SUPPORTED | `calc.volumes_line` | 15.10.2026 | cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 12 | demand.md, evidence/dfs-name-stressfrey.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `calc.volumes_line` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `calc.volumes_line` | 2,53 | evidence/dfs-volumes-ads.json |
| SUPPORTED (rounded) | `calc.volumes_line` | 2,50 | evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 300 | evidence/site-urls.json |
| SUPPORTED | `check[0].rows[2].text` | 2,2 | derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[0].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[1].rows[1].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[1].rows[1].text` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `check[1].rows[1].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].title` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 17 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `check[3].rows[2].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[3].text` | 34 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `check[3].rows[3].text` | 95 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `quick_wins[2].title` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[3].text` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `roadmap[1].why` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `roadmap[2].what` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `final.h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `final.p` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `guide.point` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.point` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `guide.point` | 42,9 | derived (evidence_lib.facts), evidence/falcon-report-5bd7097be1b0e31.json |
| SUPPORTED | `guide.think` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.hero_h1` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 210 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.step1_h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `headlines.step2_h2` | 42,9 | derived (evidence_lib.facts), evidence/falcon-report-5bd7097be1b0e31.json |
| SUPPORTED | `headlines.step2_h2` | 10,2 | derived (evidence_lib.facts), evidence/falcon-report-5bd7097be1b0e31.json |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.roadmap_h2` | 8 | competitors.md, demand.md, evidence/dfs-backlinks-summary.json |
| SUPPORTED | `headlines.final_h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
