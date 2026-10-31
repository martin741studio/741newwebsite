# Automatic fact check: Claudia Breuer (2026-10-31, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.3 s.

- Numbers: 127 · supported 119 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 18

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `system.step1.demand_note` | 9 von 14 | count claim without a derived count |
| `headlines.hero_h1` | Unter den ersten drei stehst du nur direkt vor deiner Praxis. | absolute word (nur) |
| `headlines.grid_h2` | Unter den ersten drei nur an 1 von 49 Punkten: | absolute word (nur) |
| `headlines.step3_h2` | Deine Startseite sagt ihnen heute nur „Sorgen Sie für Ihre seelische Gesundheit“. | absolute word (nur) |
| `grid.h2` | Unter den ersten drei nur an 1 von 49 Punkten: | absolute word (nur) |
| `grid.caption_today` | Unter den ersten drei nur an 1 von 49 Punkten: | absolute word (nur) |
| `grid.caption_goal` | mehr Punkte unter den ersten drei, nicht nur vor deiner Tür. | absolute word (nur) |
| `grid.caption_goal` | In deinem Eintrag steht nur Life Coach. | absolute word (nur) |
| `system.step1.items[4].why` | Das Formular steht nur auf der Kontakt-Seite. | absolute word (nur) |
| `system.step1.items[5].why` | Bei Google steht nur „Life Coach“. | absolute word (nur) |
| `system.step2.meaning` | Unter den ersten drei bist du nur an diesem einen Punkt. | absolute word (nur) |
| `system.step2.cleanup[1].text` | Ein Name überall hilft Google und Besuchern. | absolute word (überall) |
| `system.step2.good` | Alle 5 Bewertungen haben 5 Sterne. | absolute word (alle) |
| `system.step2.good` | Es ist nur noch zu wenig sichtbar. | absolute word (nur) |
| `system.step3.five[3].a` | Nur der Satz „kurzfristig Termine“ steht im Text. | absolute word (nur) |
| `check[0].rows[3].text` | Der Hinweis auf kurzfristige Termine steht nur im Text. | absolute word (nur) |
| `check[0].rows[4].title` | Formular nur auf einer Seite | absolute word (nur) |
| `check[3].rows[0].text` | Alle 5 Bewertungen haben 5 Sterne. | absolute word (alle) |
| `guide.point` | Unter den ersten drei stehst du nur an 1 von 49 Punkten, direkt vor deiner Praxis. | absolute word (nur) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `headlines.grid_h2` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 24 von 49 | derived (evidence_lib.facts) |
| NO PAIR | `system.step1.demand_note` | 9 von 14 | no derived count with total 14: the agent checks it |
| SUPPORTED | `system.step1.depth.note` | Sieben der zwölf | derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[0].why` | Sieben der zwölf | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[3].text` | Vier von fünf | homepage.md |
| SUPPORTED | `check[1].rows[1].text` | 5 von 13 | derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[2].text` | Sieben von zwölf | derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 1 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `headlines.hero_h1` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 2.900 | demand.md, evidence/dfs-volumes-ads.json, scan-search.md |
| SUPPORTED | `headlines.hero_sub` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.grid_h2` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step2_h2` | 28,57 | derived (evidence_lib.facts), evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `headlines.step2_h2` | 2,04 | derived (evidence_lib.facts), evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.roadmap_h2` | 8 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.final_h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-hp-psychotherapie-bonn.json |
| SUPPORTED | `hero.sub` | 2.900 | demand.md, evidence/dfs-volumes-ads.json, scan-search.md |
| SUPPORTED | `hero.sub` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[0].sub` | 100 | competitors.md, evidence/dfs-bl-refdomains-spam.json, evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `hero.cards[0].badge` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[0].badge` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 15 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].badge` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 31.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 8 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.chips[1]` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[0].kpi` | 2.900 | demand.md, evidence/dfs-volumes-ads.json, scan-search.md |
| SUPPORTED | `system.steps[1].kpi` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[1].kpi` | 24 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_sub` | 31.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step1.demand[0].volume` | 2900 | demand.md, evidence/dfs-volumes-ads.json, scan-search.md |
| SUPPORTED | `system.step1.demand[1].volume` | 880 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step1.demand[2].volume` | 590 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step1.demand[3].volume` | 390 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[4].volume` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-hp-psychotherapie-bonn.json |
| SUPPORTED | `system.step1.demand_note` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_note` | 14 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.sub` | 628 | derived (evidence_lib.facts), site-findings.md |
| SUPPORTED | `system.step1.depth.sub` | 745 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[0].n` | 745 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[0].val` | 745 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.bars[1].label` | 12 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `system.step1.depth.bars[1].val` | 628 | derived (evidence_lib.facts), site-findings.md |
| SUPPORTED | `system.step1.items[2].why` | 880 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step1.items[3].why` | 590 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step1.items[3].why` | 100 | competitors.md, evidence/dfs-bl-refdomains-spam.json, evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step1.items[3].why` | 80 | competitors.md, evidence/dfs-name-claudia-breuer-hp.json, evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step2.h2` | 28,57 | derived (evidence_lib.facts), evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step2.h2` | 2,04 | derived (evidence_lib.facts), evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step2.table[0].reviews` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].share` | 2,04 | derived (evidence_lib.facts), evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step2.table[1].reviews` | 15 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[1].share` | 28,57 | derived (evidence_lib.facts), evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `system.step2.table[2].reviews` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[2].share` | 26,53 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 12 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `system.step2.table[3].share` | 24,49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[4].share` | 22,45 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 31.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 15 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 2,3 | evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED (rounded) | `system.step2.meaning` | 5,3 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[0].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[1].n` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].n` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 22 | competitors.md, evidence/dfs-name-breuer-psychotherapie-bonn.json, evidence/dfs-name-claudia-breuer-hp.json |
| SUPPORTED | `system.step3.lead` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 44 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.score_today` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| ASSUMPTION | `system.step3.score_draft` | 36 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | cost_ledger.jsonl, demand.md, evidence/dfs-name-breuer-psychotherapie-bonn.json |
| SUPPORTED | `system.step3.score_draft_label` | 44 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.five[2].a` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.vol` | 2900 | demand.md, evidence/dfs-volumes-ads.json, scan-search.md |
| ASSUMPTION | `calc.vol_min` | 50 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 29000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 100 | competitors.md, evidence/dfs-bl-refdomains-spam.json, evidence/falcon-report-5d88be0ed475d1e.json |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.volumes_line` | 31.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `calc.volumes_line` | 2.900 | demand.md, evidence/dfs-volumes-ads.json, scan-search.md |
| SUPPORTED | `calc.volumes_line` | 880 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `calc.volumes_line` | 3,03 | evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 3,00 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 100 | competitors.md, evidence/dfs-bl-refdomains-spam.json, evidence/falcon-report-5d88be0ed475d1e.json |
| SUPPORTED | `check[0].rows[0].text` | 13 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED (rounded) | `check[0].rows[2].text` | 0,2 | derived (evidence_lib.facts), evidence/site.json |
| SUPPORTED | `check[1].rows[1].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[1].rows[1].text` | 13 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `check[1].rows[3].text` | 745 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `check[1].rows[3].text` | 628 | derived (evidence_lib.facts), site-findings.md |
| SUPPORTED | `check[3].rows[0].title` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 15 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 14 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[2].text` | 16 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `check[3].rows[3].text` | 16 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `roadmap[2].why` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `final.h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-hp-psychotherapie-bonn.json |
| SUPPORTED | `final.p` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-hp-psychotherapie-bonn.json |
| SUPPORTED | `guide.point` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.point` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `guide.celebrate` | 85 | evidence/dfs-name-claudia-breuer-hp.json, evidence/dfs-serp-hp-psychotherapie-bonn.json, evidence/dfs-serp-psychotherapie-bonn.json |
| SUPPORTED | `guide.celebrate` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
