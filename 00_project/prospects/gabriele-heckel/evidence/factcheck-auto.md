# Automatic fact check: Gabriele Heckel (2026-10-16, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 141 · supported 132 · not found 1 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 10

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `calc.volumes_line` | 140 | number not in any evidence file |
| `system.step3.score_draft_label` | 36 / 44 | count claim without a derived count |
| `hero.cards[1].badge` | An allen 49 Punkten nicht unter den Top 20 | absolute word (allen) |
| `system.step1.demand_note` | Deine Praxis in Hirschau liegt nur 13 Kilometer entfernt – ein kurzer Weg für qualifizierte Hilfe. | absolute word (nur) |
| `system.step1.items[4].why` | Hilfesuchende aus Amberg wollen sehen, dass die Praxis in Hirschau in nur 15 Minuten bequem erreichbar ist. | absolute word (nur) |
| `system.step2.lead` | Vier der vier ersten sind an allen 49 Messpunkten unter den ersten 20 zu sehen. | absolute word (allen) |
| `system.step2.changes[0].text` | Aktuell ist nur „Psychologischer Berater“ eingetragen. | absolute word (nur) |
| `system.step2.changes[2].text` | Mitbewerber wie Martina Braun-Zweck führen bereits mit nur 2 Bewertungen. | absolute word (nur) |
| `system.step3.note_today` | Die Telefonnummer ist nur als normaler Text hinterlegt und nicht mit einem Klick wählbar. | absolute word (nur) |
| `check[0].rows[1].title` | Immer verschlüsselt | absolute word (immer) |
| `check[1].rows[2].text` | Eine Meta-Beschreibung für Google fehlt auf allen 30 gemessenen Unterseiten. | absolute word (allen) |
| `guide.think` | Hirschau liegt nur 13 Kilometer von Amberg entfernt. | absolute word (nur) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.cards[1].sub` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | Vier der vier | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 21 / 51 | derived (evidence_lib.facts) |
| NO PAIR | `system.step3.score_draft_label` | 36 / 44 | no derived count with total 44: the agent checks it |
| SUPPORTED | `check[1].rows[1].text` | 1 von 30 | derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[2].text` | 21 von 51 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 0 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 73 | competitors.md, evidence/falcon-report-fad24349417e181.json |
| SUPPORTED | `hero.cards[0].badge` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 20 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 9 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 15 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 0,00 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 20 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 73,47 | derived (evidence_lib.facts), evidence/falcon-report-fad24349417e181.json |
| SUPPORTED | `grid.caption_goal` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_goal` | 19 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.steps[0].kpi` | 210 | demand.md, evidence/dfs-sanity-national.json |
| SUPPORTED | `system.steps[1].kpi` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.h2` | 210 | demand.md, evidence/dfs-sanity-national.json |
| SUPPORTED | `system.step1.demand_sub` | 15.10.2026 | cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_sub` | 12 | evidence/dfs-backlinks-summary.json, evidence/dfs-name-gabriele-heckel.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.demand[0].volume` | 20 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand_note` | 210 | demand.md, evidence/dfs-sanity-national.json |
| SUPPORTED | `system.step1.demand_note` | 13 | cost_ledger.jsonl, demand.md, evidence/dfs-serp-coaching-hirschau.json |
| SUPPORTED | `system.step1.depth.sub` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.big[0].n` | 205 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[1].why` | 210 | demand.md, evidence/dfs-sanity-national.json |
| SUPPORTED | `system.step1.items[4].why` | 15 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[5].why` | 45 | evidence/dfs-refdomains-spam.json, evidence/falcon-report-fad24349417e181.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step2.h2` | 73 | competitors.md, evidence/falcon-report-fad24349417e181.json |
| SUPPORTED | `system.step2.h2` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 20 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].reviews` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].share` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[1].reviews` | 9 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[1].share` | 73,5 | derived (evidence_lib.facts), evidence/falcon-report-fad24349417e181.json |
| SUPPORTED | `system.step2.table[2].reviews` | 19 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED (rounded) | `system.step2.table[2].share` | 63,3 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED (rounded) | `system.step2.table[3].share` | 30,6 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED (rounded) | `system.step2.table[4].share` | 24,5 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 15 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 19 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.meaning` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[2].title` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[2].title` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[2].text` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[3].text` | 09622 | derived (evidence_lib.facts), evidence/curl-checks-2026-10-15.txt, evidence/dfs-name-gabriele-heckel.json |
| SUPPORTED | `system.step2.changes[3].text` | 70 | evidence/curl-checks-2026-10-15.txt, evidence/dfs-name-gabriele-heckel.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.changes[3].text` | 31 | cost_ledger.jsonl, evidence/curl-checks-2026-10-15.txt, evidence/dfs-serp-coaching-hirschau.json |
| SUPPORTED | `system.step2.changes[3].text` | 90 | evidence/curl-checks-2026-10-15.txt, evidence/falcon-report-fad24349417e181.json, evidence/site-menu-2026-10-15.txt |
| SUPPORTED | `system.step2.changes[5].text` | 21 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[0].n` | 21 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[0].n` | 51 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.lead` | 22 | evidence/dfs-refdomains-spam.json, evidence/dfs-sanity-national.json, evidence/dfs-serp-coaching-hirschau.json |
| SUPPORTED | `system.step3.score_today` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| ASSUMPTION | `system.step3.score_draft` | 0 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | evidence/dfs-refdomains-spam.json, evidence/falcon-report-fad24349417e181.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step3.score_draft_label` | 44 | evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json, evidence/falcon-report-fad24349417e181.json |
| SUPPORTED | `calc.vol` | 20 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| ASSUMPTION | `calc.vol_min` | 20 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 1 | competitors.md, demand.md, derived (evidence_lib.facts) |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 100 | evidence/dfs-refdomains-spam.json, evidence/dfs-serp-coaching-hirschau.json, evidence/dfs-serp-psychotherapie-hirschau.json |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val_label` | 100 | evidence/dfs-refdomains-spam.json, evidence/dfs-serp-coaching-hirschau.json, evidence/dfs-serp-psychotherapie-hirschau.json |
| SUPPORTED | `calc.volumes_line` | 210 | demand.md, evidence/dfs-sanity-national.json |
| NOT FOUND | `calc.volumes_line` | 140 |  |
| SUPPORTED | `calc.volumes_line` | 90 | evidence/curl-checks-2026-10-15.txt, evidence/falcon-report-fad24349417e181.json, evidence/site-menu-2026-10-15.txt |
| SUPPORTED | `calc.volumes_line` | 100 | evidence/dfs-refdomains-spam.json, evidence/dfs-serp-coaching-hirschau.json, evidence/dfs-serp-psychotherapie-hirschau.json |
| SUPPORTED | `calc.volumes_line` | 70 | evidence/curl-checks-2026-10-15.txt, evidence/dfs-name-gabriele-heckel.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `calc.volumes_line` | 60 | demand.md, evidence/dfs-refdomains-spam.json, evidence/site-prices-claims-2026-10-15.md |
| SUPPORTED | `check[0].rows[0].text` | 09622 | derived (evidence_lib.facts), evidence/curl-checks-2026-10-15.txt, evidence/dfs-name-gabriele-heckel.json |
| SUPPORTED | `check[0].rows[0].text` | 70 | evidence/curl-checks-2026-10-15.txt, evidence/dfs-name-gabriele-heckel.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `check[0].rows[0].text` | 31 | cost_ledger.jsonl, evidence/curl-checks-2026-10-15.txt, evidence/dfs-serp-coaching-hirschau.json |
| SUPPORTED | `check[0].rows[0].text` | 90 | evidence/curl-checks-2026-10-15.txt, evidence/falcon-report-fad24349417e181.json, evidence/site-menu-2026-10-15.txt |
| SUPPORTED | `check[0].rows[2].text` | 1,1 | evidence/site.json |
| SUPPORTED | `check[1].rows[1].text` | 1 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[1].text` | 30 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[2].text` | 30 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[0].text` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[0].text` | 19 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `check[3].rows[0].text` | 23 | derived (evidence_lib.facts), evidence/dfs-name-gabriele-heckel.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `check[3].rows[2].text` | 21 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[2].text` | 51 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `quick_wins[0].text` | 09622 | derived (evidence_lib.facts), evidence/curl-checks-2026-10-15.txt, evidence/dfs-name-gabriele-heckel.json |
| SUPPORTED | `quick_wins[0].text` | 70 | evidence/curl-checks-2026-10-15.txt, evidence/dfs-name-gabriele-heckel.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `quick_wins[0].text` | 31 | cost_ledger.jsonl, evidence/curl-checks-2026-10-15.txt, evidence/dfs-serp-coaching-hirschau.json |
| SUPPORTED | `quick_wins[0].text` | 90 | evidence/curl-checks-2026-10-15.txt, evidence/falcon-report-fad24349417e181.json, evidence/site-menu-2026-10-15.txt |
| SUPPORTED | `quick_wins[3].title` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[5].text` | 21 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `roadmap[1].what` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `roadmap[1].what` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `roadmap[1].why` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `roadmap[1].why` | 19 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `roadmap[1].why` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `roadmap[2].what` | 45 | evidence/dfs-refdomains-spam.json, evidence/falcon-report-fad24349417e181.json, evidence/scorecard-today.md |
| SUPPORTED | `roadmap[3].why` | 210 | demand.md, evidence/dfs-sanity-national.json |
| SUPPORTED | `final.h2` | 30 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `final.p` | 30 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `final.p` | 210 | demand.md, evidence/dfs-sanity-national.json |
| SUPPORTED | `guide.point` | 210 | demand.md, evidence/dfs-sanity-national.json |
| SUPPORTED | `guide.point` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `guide.think` | 13 | cost_ledger.jsonl, demand.md, evidence/dfs-serp-coaching-hirschau.json |
| SUPPORTED | `guide.insight` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 73 | competitors.md, evidence/falcon-report-fad24349417e181.json |
| SUPPORTED | `headlines.grid_h2` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 210 | demand.md, evidence/dfs-sanity-national.json |
| SUPPORTED | `headlines.step2_h2` | 73 | competitors.md, evidence/falcon-report-fad24349417e181.json |
| SUPPORTED | `headlines.step2_h2` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.roadmap_h2` | 8 | cost_ledger.jsonl, evidence/curl-checks-2026-10-15.txt, evidence/dfs-name-gabriele-heckel.json |
| SUPPORTED | `headlines.final_h2` | 30 | competitors.md, demand.md, derived (evidence_lib.facts) |
