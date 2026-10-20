# Automatic fact check: Christian Ruether (2026-10-12, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.2 s.

- Numbers: 164 · supported 156 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 20

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `hero.cards[1].badge` | An allen 49 Punkten nicht unter den ersten 20 | absolute word (allen) |
| `grid.caption_today` | An allen 49 Punkten „20+“: | absolute word (allen) |
| `system.step1.items[4].why` | Deine Tagessätze stehen auf einer Seite, zu der nur ein Link führt, aus einem Beitrag von 2015. | absolute word (nur) |
| `system.step2.lead` | Selbst der erste, EFS Unternehmensberatung, steht nur auf rund 16 % der Karte unter den ersten drei. | absolute word (nur) |
| `system.step2.changes[0].text` | Alle vier vorn sind bei Google als „Unternehmensberater“ eingeordnet. | absolute word (alle) |
| `system.step2.changes[1].title` | Alle Leistungen eintragen | absolute word (alle) |
| `system.step2.changes[4].text` | Heute zeigt der Eintrag nur ein Street-View-Bild. | absolute word (nur) |
| `system.step2.cleanup[2].text` | Im Fuß jeder Seite steht die Nummer nur als Text, mit dem Tippfehler „++43“. | absolute word (nur) |
| `system.step3.five[0].a` | Nur aus dem Menüpunkt „Was ist Soziokratie?“. | absolute word (nur) |
| `system.step3.five[1].a` | Wien steht nicht im ersten Bildschirm, die Adresse nur im Impressum. | absolute word (nur) |
| `system.step3.five[3].a` | Nur „See More“. | absolute word (nur) |
| `check[0].rows[4].title` | Immer verschlüsselt | absolute word (immer) |
| `check[0].rows[4].text` | Deine Seite öffnet sich immer mit dem Schloss-Symbol im Browser. | absolute word (immer) |
| `check[1].rows[1].text` | Bei Google heißt sie nur „Soziokratie“, ohne Beratung und ohne Wien. | absolute word (nur) |
| `check[1].rows[3].text` | Nur ein Link aus einem Beitrag von 2015 führt hin. | absolute word (nur) |
| `quick_wins[2].text` | Heute führt nur ein Link von 2015 dorthin. | absolute word (nur) |
| `quick_wins[4].text` | Heute zeigt er nur ein Street-View-Bild. | absolute word (nur) |
| `quick_wins[5].text` | Heute gibt es dafür nur die E-Mail-Adresse und die Nummer im Fuß der Seite. | absolute word (nur) |
| `guide.point` | An allen 49 Messpunkten steht dein Eintrag nicht unter den ersten 20. | absolute word (allen) |
| `guide.point` | Auch der erste Anbieter steht nur auf rund 16 % der Karte unter den ersten drei. | absolute word (nur) |
| (text) | konsent moderation + konsent entscheidung | both forms named: say that Google counts them together (10), never add them up |
| (text) | was ist soziokratie + soziokratie ausbildung | both forms named: say that Google counts them together (10), never add them up |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.cards[1].sub` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 5 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `system.steps[1].kpi` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 5 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `system.step1.depth.note` | Keine der fünf | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 47 / 319 | evidence/visual-check.md |
| SUPPORTED | `check[3].rows[3].text` | 47 von 319 | evidence/visual-check.md |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.sub` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 34 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `hero.cards[3].badge` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[3].badge` | 44 | derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 16 | competitors.md, demand.md, evidence/dfs-backlinks-summary.json |
| SUPPORTED | `grid.caption_today` | 34 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `grid.caption_goal` | 16 | competitors.md, demand.md, evidence/dfs-backlinks-summary.json |
| SUPPORTED | `grid.caption_goal` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_goal` | 60 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[0].kpi` | 260 | demand.md, evidence/dfs-serp-4.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.steps[1].kpi` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[2].kpi` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[2].kpi` | 44 | derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step1.h2` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_sub` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step1.demand_sub` | 12 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[0].volume` | 260 | demand.md, evidence/dfs-serp-4.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[1].volume` | 50 | demand.md, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-2.json |
| SUPPORTED | `system.step1.demand[2].volume` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand[3].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[4].keyword` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[4].keyword` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[4].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[5].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[6].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[7].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[8].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_note` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.big[0].n` | 966 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[0].val` | 966 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.bars[1].label` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[1].val` | 700 | derived (evidence_lib.facts), evidence/falcon-report-b52a97742083dc4.json, evidence/visual-check.md |
| SUPPORTED | `system.step1.depth.note` | 600 | evidence/falcon-report-b52a97742083dc4.json, site-findings.md |
| SUPPORTED | `system.step1.items[1].why` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[1].why` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[2].why` | 260 | demand.md, evidence/dfs-serp-4.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[2].why` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[3].why` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[3].why` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[4].why` | 2015 | evidence/site-page-urls.txt, evidence/site-pages.json, evidence/site-urls.json |
| SUPPORTED | `system.step1.items[5].why` | 2025 | evidence/comp-pages.json, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-2.json |
| SUPPORTED | `system.step2.h2` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.h2` | 60 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 16 | competitors.md, demand.md, evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.table[0].reviews` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[0].share` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.table[1].reviews` | 34 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.table[1].share` | 16,3 | evidence/visual-check.md |
| SUPPORTED | `system.step2.table[2].reviews` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[2].share` | 12,2 | evidence/visual-check.md |
| SUPPORTED | `system.step2.table[3].reviews` | 60 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].share` | 10,2 | competitors.md, derived (evidence_lib.facts), evidence/visual-check.md |
| SUPPORTED | `system.step2.table[4].reviews` | 29 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.table[4].share` | 10,2 | competitors.md, derived (evidence_lib.facts), evidence/visual-check.md |
| SUPPORTED | `system.step2.fine` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 60 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 0,7 | competitors.md, evidence/falcon-report-b52a97742083dc4.json |
| SUPPORTED | `system.step2.meaning` | 4,6 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-b52a97742083dc4.json |
| SUPPORTED | `system.step2.changes[2].text` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[2].text` | 60 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[2].text` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[5].text` | 8 | cost_ledger.jsonl, evidence/chat-2026-10-12.md, evidence/comp-pages.json |
| SUPPORTED | `system.step2.changes[5].text` | 17 | demand.md, evidence/comp-pages.json, evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.cleanup[0].n` | 47 | demand.md, derived (evidence_lib.facts), evidence/chat-2026-10-12.md |
| SUPPORTED | `system.step2.cleanup[0].n` | 319 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.cleanup[1].n` | 9 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].text` | 9 | cost_ledger.jsonl, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[2].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].text` | 43 | derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json, evidence/dfs-serp-4.json |
| SUPPORTED | `system.step2.cleanup[3].n` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.good` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step3.lead` | 22 | cost_ledger.jsonl, evidence/comp-pages.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step3.score_today` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| ASSUMPTION | `system.step3.score_draft` | 36 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | competitors.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step3.score_draft_label` | 44 | derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `system.step3.note_draft` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.vol` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| ASSUMPTION | `calc.vol_min` | 20 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 5.3 | evidence/visual-check.md |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 1200 | evidence/falcon-report-b52a97742083dc4.json, evidence/visual-check.md, site-findings.md |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 3000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.volumes_line` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `calc.volumes_line` | 12 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `calc.volumes_line` | 260 | demand.md, evidence/dfs-serp-4.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 5,35 | evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 5,30 | evidence/visual-check.md |
| SUPPORTED | `calc.volumes_line` | 1.200 | evidence/falcon-report-b52a97742083dc4.json, evidence/visual-check.md, site-findings.md |
| SUPPORTED | `check[0].rows[0].text` | 43 | derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json, evidence/dfs-serp-4.json |
| SUPPORTED | `check[0].rows[0].text` | 699 | derived (evidence_lib.facts), evidence/dfs-serp-name2.json, evidence/falcon-report-b52a97742083dc4.json |
| SUPPORTED | `check[0].rows[0].text` | 11114398 | derived (evidence_lib.facts), evidence/dfs-serp-name2.json, evidence/google-panel-2026-10-12.md |
| SUPPORTED | `check[0].rows[2].text` | 07 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[0].rows[2].text` | 08 | cost_ledger.jsonl, evidence/chat-2026-10-12.md, evidence/comp-pages.json |
| SUPPORTED | `check[0].rows[2].text` | 2025 | evidence/comp-pages.json, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-2.json |
| SUPPORTED | `check[0].rows[3].text` | 1,4 | evidence/site.json |
| SUPPORTED | `check[1].rows[2].text` | 3 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[1].rows[3].text` | 2015 | evidence/site-page-urls.txt, evidence/site-pages.json, evidence/site-urls.json |
| SUPPORTED | `check[1].rows[4].text` | 966 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `check[1].rows[4].text` | 600 | evidence/falcon-report-b52a97742083dc4.json, site-findings.md |
| SUPPORTED | `check[1].rows[4].text` | 119 | evidence/dfs-serp-4.json, evidence/falcon-report-b52a97742083dc4.json, site-findings.md |
| SUPPORTED | `check[1].rows[4].text` | 343 | site-findings.md |
| SUPPORTED | `check[1].rows[4].text` | 700 | derived (evidence_lib.facts), evidence/falcon-report-b52a97742083dc4.json, evidence/visual-check.md |
| SUPPORTED | `check[3].rows[0].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[1].text` | 60 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[2].text` | 89 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-1.json |
| SUPPORTED | `check[3].rows[2].text` | 91 | competitors.md, derived (evidence_lib.facts), evidence/dfs-serp-1.json |
| SUPPORTED | `check[3].rows[3].text` | 47 | demand.md, derived (evidence_lib.facts), evidence/chat-2026-10-12.md |
| SUPPORTED | `check[3].rows[3].text` | 319 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `quick_wins[0].text` | 43 | derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json, evidence/dfs-serp-4.json |
| SUPPORTED | `quick_wins[2].text` | 2015 | evidence/site-page-urls.txt, evidence/site-pages.json, evidence/site-urls.json |
| SUPPORTED | `quick_wins[3].text` | 2025 | evidence/comp-pages.json, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-2.json |
| SUPPORTED | `quick_wins[3].text` | 2022 | evidence/home-images.txt, evidence/own-commercial-pages.json, evidence/scorecard-today.md |
| SUPPORTED | `final.h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `final.p` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `guide.point` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 16 | competitors.md, demand.md, evidence/dfs-backlinks-summary.json |
| SUPPORTED | `guide.celebrate` | 18 | evidence/comp-pages.json, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `guide.celebrate` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 8 | cost_ledger.jsonl, evidence/chat-2026-10-12.md, evidence/comp-pages.json |
| SUPPORTED | `headlines.hero_sub` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_sub` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.step2_h2` | 15 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step2_h2` | 60 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.roadmap_h2` | 8 | cost_ledger.jsonl, evidence/chat-2026-10-12.md, evidence/comp-pages.json |
| SUPPORTED | `headlines.final_h2` | 30 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
