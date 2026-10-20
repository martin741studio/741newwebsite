# Automatic fact check: Sabine Schwarz (2026-10-12, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 187 · supported 179 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 14

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `system.step2.changes[1].text` | eine von sechs | count claim without a derived count |
| `grid.h2` | Unter den ersten drei an 5 von 49 Punkten, alle im Südwesten. | absolute word (alle) |
| `grid.caption_today` | Alle fünf liegen im Südwesten, rund um Schorkendorf und Witzmannsberg, nahe deiner Praxis. | absolute word (alle) |
| `system.step1.items[5].why` | Alle 15 Bewertungen bei Google haben 5 Sterne. | absolute word (alle) |
| `system.step2.lead` | Die vier vorn sind an allen 49 Messpunkten unter den ersten 20 zu sehen, dein Eintrag mit den Bewertungen an 26. | absolute word (allen) |
| `system.step2.meaning` | Doch Franziska Bartsch sitzt auch in Ahorn und steht mit 3 Bewertungen an allen 49 Punkten unter den ersten 20, die Entfernung allein erklärt die Lücke also nicht. | absolute word (allen) |
| `system.step2.meaning` | an allen 49 Punkten unter den ersten 20, in der Stadtmitte auf Platz 4, aber ohne Bewertung. | absolute word (allen) |
| `system.step2.changes[1].text` | Bei dir steht das nur als eine von sechs Einordnungen, dazu „Internet-Marketing“ und „Feng-Shui-Berater“, die nicht zu Paartherapie passen. | absolute word (nur) |
| `system.step2.good` | Dazu haben alle 15 Bewertungen 5 Sterne, jede mit deiner Antwort. | absolute word (alle) |
| `system.step3.note_today` | Im ersten Bildschirm fehlen der Ort, deine 5 Sterne und eine Nummer, und der Button heißt nur „Kontakt“. | absolute word (nur) |
| `system.step3.five[3].a` | Das kostenlose Erstgespräch steht nur im halb durchsichtigen Knopf unten rechts, eine Nummer fehlt. | absolute word (nur) |
| `check[0].rows[1].title` | Nicht immer verschlüsselt | absolute word (immer) |
| `check[3].rows[0].text` | 5,0 Sterne bei 15 Bewertungen, alle mit 5 Sternen. | absolute word (alle) |
| `quick_wins[4].title` | Immer verschlüsselt, eine Startseite | absolute word (immer) |
| `headlines.grid_h2` | Unter den ersten drei an 5 von 49 Punkten, alle im Südwesten. | absolute word (alle) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.cards[1].sub` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].badge` | 15 von 15 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 22 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `grid.h2` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 26 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 22 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `system.step1.depth.note` | Keine der fünf | derived (evidence_lib.facts) |
| NO PAIR | `system.step2.changes[1].text` | eine von sechs | no derived count with total 6: the agent checks it |
| SUPPORTED | `system.step2.changes[4].text` | 15 von 15 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 38 / 1018 | derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[1].text` | 15 von 15 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 5 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 5 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.sub` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.sub` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[0].badge` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[0].badge` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 11 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].badge` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].badge` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 22 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 44 | derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 23 | competitors.md, derived (evidence_lib.facts), evidence/chat-2026-10-12.md |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 61,2 | evidence/visual-check.md |
| SUPPORTED | `grid.caption_goal` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_goal` | 11 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_goal` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[0].kpi` | 1.900 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.steps[1].kpi` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 26 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[2].kpi` | 22 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 44 | derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step1.h2` | 614 | evidence/site-pages.json, evidence/visual-check.md, site-findings.md |
| SUPPORTED | `system.step1.demand_sub` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step1.demand_sub` | 12 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[0].volume` | 1900 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.demand[1].volume` | 1300 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.demand[2].volume` | 260 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.demand[3].volume` | 110 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.demand[4].volume` | 110 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.demand[5].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_note` | 260 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.demand_note` | 110 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.depth.big[0].n` | 614 | evidence/site-pages.json, evidence/visual-check.md, site-findings.md |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[0].val` | 614 | evidence/site-pages.json, evidence/visual-check.md, site-findings.md |
| SUPPORTED | `system.step1.depth.bars[1].label` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[1].val` | 421 | derived (evidence_lib.facts), evidence/visual-check.md, site-findings.md |
| SUPPORTED | `system.step1.items[1].why` | 110 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.items[1].why` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[2].why` | 1.900 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.items[2].why` | 150 | evidence/visual-check.md, site-findings.md |
| SUPPORTED | `system.step1.items[2].why` | 75 | demand.md, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step1.items[3].why` | 1.300 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.items[4].why` | 260 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.items[5].why` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[5].why` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.h2` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 26 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].name` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].reviews` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].share` | 10,2 | derived (evidence_lib.facts), evidence/falcon-report-5544ec2c473e732.json, evidence/visual-check.md |
| SUPPORTED | `system.step2.table[1].reviews` | 11 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[1].share` | 61,2 | evidence/visual-check.md |
| SUPPORTED | `system.step2.table[2].reviews` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[2].share` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[3].share` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[4].share` | 26,5 | evidence/visual-check.md |
| SUPPORTED | `system.step2.fine` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 11 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED (rounded) | `system.step2.meaning` | 2,7 | derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.meaning` | 4,3 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 4 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[0].text` | 33 | competitors.md, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step2.changes[0].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[3].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[4].text` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[4].text` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 38 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[0].n` | 1018 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.cleanup[1].n` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[1].text` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].n` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[3].n` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[3].text` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[3].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[3].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.good` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 22 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.score_today` | 22 | competitors.md, demand.md, derived (evidence_lib.facts) |
| ASSUMPTION | `system.step3.score_draft` | 36 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | evidence/chat-2026-10-12.md, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step3.score_draft_label` | 44 | derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step3.note_today` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.note_draft` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.note_draft` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.note_draft` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.five[2].a` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.five[2].a` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `calc.vol` | 110 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| ASSUMPTION | `calc.vol_min` | 50 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 2.0 | competitors.md, cost_ledger.jsonl, demand.md |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 300 | evidence/visual-check.md |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.volumes_line` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `calc.volumes_line` | 12 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 110 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `calc.volumes_line` | 1.900 | demand.md, evidence/dfs-volumes-ads.json, evidence/visual-check.md |
| SUPPORTED | `calc.volumes_line` | 1,96 | evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 2,00 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 150 | evidence/visual-check.md, site-findings.md |
| SUPPORTED | `calc.volumes_line` | 75 | demand.md, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `check[0].rows[2].text` | 0,5 | evidence/site.json |
| SUPPORTED | `check[0].rows[4].text` | 56 | derived (evidence_lib.facts), evidence/chat-2026-10-12.md, evidence/comp-pages.json |
| SUPPORTED | `check[1].rows[1].text` | 1.040 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `check[1].rows[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[1].rows[4].text` | 614 | evidence/site-pages.json, evidence/visual-check.md, site-findings.md |
| SUPPORTED | `check[1].rows[4].text` | 421 | derived (evidence_lib.facts), evidence/visual-check.md, site-findings.md |
| SUPPORTED | `check[3].rows[0].title` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[0].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[1].text` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[2].text` | 9 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[2].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[3].text` | 38 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[3].text` | 1.018 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `quick_wins[2].title` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[2].text` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[2].text` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `roadmap[1].why` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `roadmap[1].why` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `roadmap[2].what` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `final.h2` | 30 | competitors.md, demand.md, evidence/chat-2026-10-12.md |
| SUPPORTED | `final.p` | 30 | competitors.md, demand.md, evidence/chat-2026-10-12.md |
| SUPPORTED | `guide.point` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `guide.insight` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `guide.insight` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.celebrate` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 614 | evidence/site-pages.json, evidence/visual-check.md, site-findings.md |
| SUPPORTED | `headlines.step2_h2` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step2_h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.roadmap_h2` | 8 | competitors.md, demand.md, evidence/chat-2026-10-12.md |
| SUPPORTED | `headlines.final_h2` | 30 | competitors.md, demand.md, evidence/chat-2026-10-12.md |
