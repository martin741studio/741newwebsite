# Automatic fact check: Claudia Maria Steifensand (2026-10-13, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 184 · supported 176 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 17

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `grid.caption_today` | Platz 4 nur an den 4 Punkten im Nordwesten, um Strehla und Gröba. | absolute word (nur) |
| `system.step1.demand_note` | Für Riesa zeigt Google nur bei „bestattungsinstitut riesa“ eine Zahl: | absolute word (nur) |
| `system.step1.items[5].why` | Die Nummer für Tag und Nacht steht nur auf der Kontakt-Seite. | absolute word (nur) |
| `system.step2.changes[1].title` | Alle Leistungen eintragen | absolute word (alle) |
| `system.step2.cleanup[3].text` | Das steht heute nur auf der Kontakt-Seite, nicht auf der Startseite. | absolute word (nur) |
| `system.step3.five[0].a` | Nur der Name „Bestattungsinstitut Pinkert & Partner“ oben. | absolute word (nur) |
| `system.step3.five[2].a` | Nur das Zeichen des Bestatterhandwerks am unteren Rand. | absolute word (nur) |
| `system.step3.five[3].a` | Dass ihr Tag und Nacht erreichbar seid, steht nur auf der Kontakt-Seite. | absolute word (nur) |
| `check[0].rows[2].title` | Immer verschlüsselt | absolute word (immer) |
| `check[0].rows[2].text` | Eure Seite öffnet sich immer mit dem Schloss-Symbol im Browser. | absolute word (immer) |
| `check[0].rows[3].title` | Tag und Nacht nur auf der Kontakt-Seite | absolute word (nur) |
| `check[0].rows[3].text` | „Tag und Nacht sind wir telefonisch dienstbereit“ steht nur dort. | absolute word (nur) |
| `check[1].rows[2].text` | Nur Impressum und Datenschutz haben eine eigene Beschreibung. | absolute word (nur) |
| `quick_wins[0].text` | Heute steht das nur auf der Kontakt-Seite. | absolute word (nur) |
| `quick_wins[2].text` | Heute haben nur Impressum und Datenschutz eine. | absolute word (nur) |
| `roadmap[1].what` | zweite Einordnung, alle Leistungen, Fotos, Antworten auf Bewertungen. | absolute word (alle) |
| `guide.point` | Nur im Nordwesten um Strehla und Gröba seid ihr auf Platz 4. | absolute word (nur) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.cards[1].sub` | 45 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 13 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `grid.h2` | 45 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 45 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 45 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 13 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `system.step2.lead` | 45 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 30 / 68 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.good` | 45 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[4].text` | 30 von 68 | derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 45 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 45 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 45 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[0].badge` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[0].badge` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 45 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].badge` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].badge` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 40 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 3,2 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-3767da8e53c5506.json |
| SUPPORTED | `hero.cards[2].sub` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[3].badge` | 13 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[3].badge` | 44 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 45 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 13.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 45 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_goal` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_goal` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[0].kpi` | 4.400 | demand.md, evidence/dfs-volumes-ads.json, site-findings.md |
| SUPPORTED | `system.steps[1].kpi` | 45 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[2].kpi` | 13 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[2].kpi` | 44 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_sub` | 13.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step1.demand_sub` | 12 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand[0].volume` | 6600 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[1].volume` | 4400 | demand.md, evidence/dfs-volumes-ads.json, site-findings.md |
| SUPPORTED | `system.step1.demand[2].volume` | 3600 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[3].volume` | 2400 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[4].volume` | 1900 | demand.md, evidence/dfs-volumes-ads.json, site-findings.md |
| SUPPORTED | `system.step1.demand[5].volume` | 1900 | demand.md, evidence/dfs-volumes-ads.json, site-findings.md |
| SUPPORTED | `system.step1.demand[6].volume` | 1000 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-3767da8e53c5506.json |
| SUPPORTED | `system.step1.demand[7].volume` | 50 | demand.md, evidence/dfs-backlinks-summary.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[8].volume` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_note` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_note` | 25 | demand.md, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step1.depth.big[0].n` | 172 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[0].val` | 172 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.bars[1].label` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[1].val` | 564 | derived (evidence_lib.facts), evidence/visual-check.md, site-findings.md |
| SUPPORTED | `system.step1.depth.bars[2].label` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[2].val` | 324 | evidence/visual-check.md, site-findings.md |
| SUPPORTED | `system.step1.items[1].why` | 2.400 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[2].why` | 4.400 | demand.md, evidence/dfs-volumes-ads.json, site-findings.md |
| SUPPORTED | `system.step1.items[2].why` | 1.900 | demand.md, evidence/dfs-volumes-ads.json, site-findings.md |
| SUPPORTED | `system.step1.items[3].why` | 6.600 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[4].why` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[4].why` | 000 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[4].why` | 1.900 | demand.md, evidence/dfs-volumes-ads.json, site-findings.md |
| SUPPORTED | `system.step2.lead` | 45 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].reviews` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].share` | 91,8 | evidence/visual-check.md |
| SUPPORTED | `system.step2.table[1].reviews` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[1].share` | 100 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[2].reviews` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[2].share` | 98 | evidence/dfs-serp-2.json, evidence/visual-check.md |
| SUPPORTED | `system.step2.table[3].reviews` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[3].share` | 8,2 | evidence/visual-check.md |
| SUPPORTED | `system.step2.table[4].reviews` | 13 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[4].share` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.fine` | 13.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.fine` | 40 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 0,7 | competitors.md, evidence/visual-check.md |
| SUPPORTED | `system.step2.meaning` | 1,4 | competitors.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[2].text` | 40 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[2].text` | 3,2 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-3767da8e53c5506.json |
| SUPPORTED | `system.step2.changes[2].text` | 08 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[2].text` | 00 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[3].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[0].n` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.cleanup[0].n` | 68 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.cleanup[0].text` | 28 | demand.md, evidence/dfs-refdomains-spam.json, prospect-mini/case-library.json |
| SUPPORTED | `system.step2.cleanup[0].text` | 2026 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[1].n` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[1].text` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].n` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].text` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].text` | 40 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[2].text` | 3,2 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-3767da8e53c5506.json |
| SUPPORTED | `system.step2.cleanup[2].text` | 01589 | competitors.md, demand.md, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step2.cleanup[2].text` | 01594 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[3].n` | 24 | evidence/comp-pages.json, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step2.good` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 45 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.good` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.good` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 22 | evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json, evidence/dfs-serp-2.json |
| SUPPORTED | `system.step3.score_today` | 13 | competitors.md, cost_ledger.jsonl, demand.md |
| ASSUMPTION | `system.step3.score_draft` | 36 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | evidence/falcon-report-3767da8e53c5506.json |
| SUPPORTED | `system.step3.score_draft_label` | 44 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step3.note_draft` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.note_draft` | 1991 | evidence/dfs-serp-name.json, evidence/scorecard-today.md, homepage.md |
| SUPPORTED | `system.step3.note_draft` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.five[2].a` | 1991 | evidence/dfs-serp-name.json, evidence/scorecard-today.md, homepage.md |
| SUPPORTED | `system.step3.five[2].a` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.five[3].a` | 03525 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-1.json |
| SUPPORTED | `system.step3.five[3].a` | 735814 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-2.json |
| SUPPORTED | `calc.vol` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| ASSUMPTION | `calc.vol_min` | 20 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 10.3 | evidence/visual-check.md |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 1500 | evidence/visual-check.md |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 5000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.volumes_line` | 13.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `calc.volumes_line` | 12 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `calc.volumes_line` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 10,27 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 10,30 | evidence/visual-check.md |
| SUPPORTED | `calc.volumes_line` | 1.500 | evidence/visual-check.md |
| SUPPORTED (rounded) | `check[0].rows[4].text` | 0,8 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/site.json |
| SUPPORTED | `check[1].rows[3].text` | 172 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `check[1].rows[3].text` | 146 | evidence/site-pages.json, site-findings.md |
| SUPPORTED | `check[1].rows[3].text` | 564 | derived (evidence_lib.facts), evidence/visual-check.md, site-findings.md |
| SUPPORTED | `check[1].rows[3].text` | 324 | evidence/visual-check.md, site-findings.md |
| SUPPORTED | `check[3].rows[0].title` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[2].title` | 40 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[2].text` | 3,2 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-3767da8e53c5506.json |
| SUPPORTED | `check[3].rows[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[2].text` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[4].text` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `check[3].rows[4].text` | 68 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `quick_wins[3].text` | 40 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `quick_wins[5].text` | 1991 | evidence/dfs-serp-name.json, evidence/scorecard-today.md, homepage.md |
| SUPPORTED | `quick_wins[5].text` | 35 | cost_ledger.jsonl, evidence/dfs-serp-2.json, evidence/scorecard-today.md |
| SUPPORTED | `quick_wins[5].text` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `roadmap[1].what` | 40 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `roadmap[2].what` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `roadmap[2].why` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `final.h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `final.h2` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `final.p` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `guide.point` | 45 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.point` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.point` | 4 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.think` | 20 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.celebrate` | 18 | competitors.md, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `guide.celebrate` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 45 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.grid_h2` | 45 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.roadmap_h2` | 8 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.final_h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `headlines.final_h2` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.items_h3` | 6 | demand.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED | `headlines.five_h3` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
