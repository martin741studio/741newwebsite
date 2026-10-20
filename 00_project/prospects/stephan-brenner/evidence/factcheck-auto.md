# Automatic fact check: Stephan Brenner (2026-10-16, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 127 · supported 119 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 10

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `hero.cards[3].badge` | 8 von 42 | count claim without a derived count |
| `system.steps[2].kpi` | 8 von 42 | count claim without a derived count |
| `system.step1.items[0].why` | Die Startseite nennt Stuttgart heute nur im Impressum und Footer, nicht im sichtbaren Kopfbereich. | absolute word (nur) |
| `system.step1.items[3].why` | Konkrete Mandatsanlässe abfangen, statt nur abstrakte Rechtsgebiete aufzuzählen. | absolute word (nur) |
| `system.step2.lead` | Eine der vier ersten sind an allen 49 Messpunkten unter den ersten 20 zu sehen. | absolute word (allen) |
| `system.step2.changes[1].title` | Alle juristischen Fachbereiche hinterlegen | absolute word (alle) |
| `system.step2.changes[4].text` | Einblicke in die Kanzleiräume in der Calwer Straße und Porträts aller Partner schaffen sofortiges Vertrauen. | absolute word (aller) |
| `system.step3.five[1].a` | Stuttgart wird im ersten Bildschirm nicht genannt; die Kanzlei-Adresse steht nur im Footer. | absolute word (nur) |
| `system.step3.five[3].a` | Nur Menü-Icons und Links zu offenen Stellen. | absolute word (nur) |
| `check[0].rows[1].title` | Immer verschlüsselt | absolute word (immer) |
| `check[0].rows[1].text` | Deine Seite öffnet sich immer mit dem Schloss-Symbol im Browser. | absolute word (immer) |
| `quick_wins[3].text` | Alle Schwerpunkte von M&A bis Gesellschafterstreit als konkrete Leistungen im Profil hinterlegen. | absolute word (alle) |
| (text) | rechtsanwalt stuttgart + rechtsanwältin stuttgart | both forms named: say that Google counts them together (1000), never add them up |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.cards[1].sub` | 0 von 49 | derived (evidence_lib.facts) |
| NO PAIR | `hero.cards[3].badge` | 8 von 42 | no derived count with total 42: the agent checks it |
| SUPPORTED | `grid.h2` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 1 von 49 | derived (evidence_lib.facts) |
| NO PAIR | `system.steps[2].kpi` | 8 von 42 | no derived count with total 42: the agent checks it |
| SUPPORTED | `system.step2.lead` | Eine der vier | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 94 / 1352 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 / 5 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 0 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[0].badge` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[0].badge` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 202 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `hero.cards[3].badge` | 8 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 42 | evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.h2` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.intro` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 97,96 | derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `grid.caption_goal` | 78 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `grid.caption_goal` | 202 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `system.steps[0].kpi` | 2.400 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.steps[1].kpi` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[2].kpi` | 8 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 42 | evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand_sub` | 15.10.2026 | cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_sub` | 12 | derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json, evidence/dfs-name-contiq.json |
| SUPPORTED | `system.step1.demand[0].volume` | 2400 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[1].volume` | 1900 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[2].volume` | 1000 | demand.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[3].volume` | 720 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[4].volume` | 390 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[5].volume` | 260 | demand.md, evidence/dfs-volumes-ads.json, evidence/site-pages.json |
| SUPPORTED | `system.step1.demand[6].volume` | 40 | demand.md, evidence/dfs-name-contiq.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.demand[7].volume` | 30 | demand.md, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.demand[8].volume` | 30 | demand.md, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.demand[9].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.big[0].n` | 771 | derived (evidence_lib.facts), evidence/site-checks.md, evidence/site-pages.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.depth.bars[0].val` | 771 | derived (evidence_lib.facts), evidence/site-checks.md, evidence/site-pages.json |
| SUPPORTED | `system.step1.depth.bars[1].label` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[1].val` | 1894 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.h2` | 98 | evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].reviews` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].share` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[1].reviews` | 202 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `system.step2.table[1].share` | 98 | evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `system.step2.table[2].reviews` | 78 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED (rounded) | `system.step2.table[2].share` | 34,7 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 155 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED (rounded) | `system.step2.table[3].share` | 18,4 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 102 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED (rounded) | `system.step2.table[4].share` | 16,3 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 78 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `system.step2.meaning` | 202 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `system.step2.meaning` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 94 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.cleanup[0].n` | 1352 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 22 | evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-anwalt-gesellschaftsrecht.json |
| SUPPORTED | `system.step3.score_today` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| ASSUMPTION | `system.step3.score_draft` | 0 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 34 | competitors.md, cost_ledger.jsonl, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step3.score_draft_label` | 42 | evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.vol` | 40 | demand.md, evidence/dfs-name-contiq.json, evidence/dfs-refdomains-spam.json |
| ASSUMPTION | `calc.vol_min` | 40 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 27.1 | evidence/dfs-volumes-ads.json |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 1500 | evidence/site.json |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val_label` | 1.500 | evidence/site.json |
| SUPPORTED | `calc.volumes_line` | 15.10.2026 | cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 40 | demand.md, evidence/dfs-name-contiq.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `calc.volumes_line` | 30 | demand.md, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED (rounded) | `calc.volumes_line` | 3,50 | evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 1.500 | evidence/site.json |
| SUPPORTED | `check[0].rows[2].text` | 1,7 | evidence/site.json |
| SUPPORTED | `check[3].rows[0].title` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[0].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 202 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `check[3].rows[1].text` | 102 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `check[3].rows[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[3].text` | 94 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `check[3].rows[3].text` | 1.352 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `quick_wins[2].title` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[2].text` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `quick_wins[5].text` | 94 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `roadmap[1].why` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `roadmap[2].what` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `final.h2` | 30 | demand.md, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `final.p` | 30 | demand.md, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `guide.point` | 98 | evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `guide.point` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.point` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 5,0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.step2_h2` | 98 | evidence/falcon-report-da6ceb86d5e2406.json |
| SUPPORTED | `headlines.step2_h2` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.roadmap_h2` | 8 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.final_h2` | 30 | demand.md, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
