# Automatic fact check: Thorsten Schmidt (2026-10-31, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.0 s.

- Numbers: 78 · supported 70 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 12

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `system.step3.score_draft_label` | 34 von 42 | count claim without a derived count |
| `quick_wins[5].text` | 32 von 52 | count claim without a derived count |
| `system.step1.demand_note` | Google gibt keine Zahl nur für Troisdorf heraus. | absolute word (nur) |
| `system.step1.items[0].why` | Im Fließtext steht Troisdorf nur auf „Ihr Berater“. | absolute word (nur) |
| `system.step1.items[2].why` | Dein Rechtsgebiet steht heute nur als Liste, ohne eigene Seite. | absolute word (nur) |
| `system.step1.items[4].why` | Die Zahlen zeigen nur die Nachfrage, nicht deine Einzugsgebiete. | absolute word (nur) |
| `system.step1.items[5].why` | Deine Website nennt „Optimierung des Übergangs von Vermögen auf die nächste Generation“ nur als Stichpunkt. | absolute word (nur) |
| `system.step3.five[3].a` | Heute führt nur „Kontakt aufnehmen“ zu einer E-Mail, ohne Schritte und Dauer. | absolute word (nur) |
| `check[0].rows[0].title` | Telefon nur auf einer Unterseite | absolute word (nur) |
| `check[0].rows[1].title` | Kontakt nur über einen E-Mail-Button | absolute word (nur) |
| `check[0].rows[1].text` | Ein Formular gibt es nur auf „Ihr Berater“. | absolute word (nur) |
| `check[3].rows[2].text` | Die drei mit den meisten haben 62 bis 71. | absolute word (den meisten) |
| `quick_wins[2].text` | Dann gibt es nur eine Startseite für Google. | absolute word (nur) |
| `roadmap[3].what` | Bonn und Siegburg nur, wenn du dort Mandanten annimmst. | absolute word (nur) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| NO PAIR | `system.step3.score_draft_label` | 34 von 42 | no derived count with total 42: the agent checks it |
| NO PAIR | `quick_wins[5].text` | 32 von 52 | no derived count with total 52: the agent checks it |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `headlines.hero_h1` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.hero_h1` | 20 | competitors.md, demand.md, evidence/chat-2026-10-31.md |
| SUPPORTED | `headlines.hero_sub` | 31 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.step1_h2` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, demand.md, evidence/chat-2026-10-31.md |
| SUPPORTED | `headlines.roadmap_h2` | 8 | evidence/chat-2026-10-31.md, evidence/dfs-bl-spam-refdomains.json, evidence/dfs-name-kanzlei-schmidt.json |
| SUPPORTED | `hero.sub` | 31 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[0].badge` | 2016 | evidence/rendered-berater.md, homepage.md, intake.md |
| SUPPORTED | `hero.cards[0].badge` | 2018 | evidence/rendered-berater.md, homepage.md, intake.md |
| SUPPORTED | `hero.cards[1].sub` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `hero.cards[1].badge` | 20 | competitors.md, demand.md, evidence/chat-2026-10-31.md |
| SUPPORTED | `hero.cards[2].sub` | 297 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `hero.cards[3].badge` | 31 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[3].badge` | 717 | competitors.md |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, demand.md, evidence/chat-2026-10-31.md |
| SUPPORTED | `system.intro` | 31 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.intro` | 2026 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[0].kpi` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.steps[1].kpi` | 31 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[1].kpi` | 717 | competitors.md |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, demand.md, evidence/chat-2026-10-31.md |
| SUPPORTED | `system.step1.h2` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand_sub` | 31.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step1.demand_sub` | 12 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand[0].volume` | 5400 | demand.md, evidence/dfs-volumes-ads.json, prospect-mini/case-library.json |
| SUPPORTED | `system.step1.demand[1].volume` | 1300 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[2].volume` | 390 | demand.md, evidence/dfs-name-thorsten-schmidt.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[3].volume` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[4].volume` | 210 | demand.md, evidence/dfs-name-thorsten-schmidt.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[5].volume` | 50 | competitors.md, demand.md, evidence/comp-pages.json |
| SUPPORTED | `system.step1.demand[6].volume` | 40 | demand.md, evidence/dfs-bl-spam-refdomains.json, evidence/dfs-name-thorsten-schmidt.json |
| SUPPORTED | `system.step1.depth.title` | 297 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[0].n` | 297 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[1].why` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[2].why` | 210 | demand.md, evidence/dfs-name-thorsten-schmidt.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[3].why` | 5.400 | demand.md, evidence/dfs-volumes-ads.json, prospect-mini/case-library.json |
| SUPPORTED | `system.step1.items[4].why` | 1.300 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[4].why` | 390 | demand.md, evidence/dfs-name-thorsten-schmidt.json, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[5].why` | 50 | competitors.md, demand.md, evidence/comp-pages.json |
| SUPPORTED | `system.step3.lead` | 21 | evidence/dfs-bl-spam-refdomains.json, evidence/dfs-name-thorsten-schmidt.json, evidence/dfs-serp-rechtsanwalt-troisdorf.json |
| SUPPORTED | `system.step3.score_today` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| ASSUMPTION | `system.step3.score_draft` | 34 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 34 | cost_ledger.jsonl, evidence/dfs-name-kanzlei-schmidt.json, evidence/dfs-serp-rechtsanwalt-troisdorf.json |
| SUPPORTED | `system.step3.score_draft_label` | 42 | evidence/dfs-bl-spam-refdomains.json, evidence/dfs-serp-rechtsanwalt-troisdorf.json, evidence/scorecard-today.md |
| SUPPORTED | `system.step3.five[2].a` | 2016 | evidence/rendered-berater.md, homepage.md, intake.md |
| SUPPORTED | `system.step3.five[2].a` | 2018 | evidence/rendered-berater.md, homepage.md, intake.md |
| SUPPORTED | `calc.vol` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| ASSUMPTION | `calc.vol_min` | 50 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 1.8 | prospect-mini/case-library.json |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 2000 | homepage.md |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 5000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val_label` | 2.000 | homepage.md |
| SUPPORTED | `calc.volumes_line` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 5.400 | demand.md, evidence/dfs-volumes-ads.json, prospect-mini/case-library.json |
| SUPPORTED | `calc.volumes_line` | 1.300 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `check[0].rows[4].text` | 0,2 | evidence/site.json |
| SUPPORTED | `check[2].rows[0].text` | 4 | competitors.md, demand.md, evidence/chat-2026-10-31.md |
| SUPPORTED | `check[3].rows[2].text` | 31 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[2].text` | 717 | competitors.md |
| SUPPORTED | `check[3].rows[2].text` | 62 | competitors.md, demand.md, evidence/dfs-serp-rechtsanwalt-troisdorf.json |
| SUPPORTED | `check[3].rows[2].text` | 71 | competitors.md, evidence/dfs-serp-steuerberater-troisdorf.json |
| SUPPORTED | `check[3].rows[3].text` | 2016 | evidence/rendered-berater.md, homepage.md, intake.md |
| SUPPORTED | `check[3].rows[3].text` | 2018 | evidence/rendered-berater.md, homepage.md, intake.md |
| SUPPORTED | `quick_wins[5].text` | 32 | competitors.md, demand.md, evidence/dfs-bl-spam-refdomains.json |
| SUPPORTED | `quick_wins[5].text` | 52 | competitors.md, demand.md, evidence/dfs-bl-summary.json |
| SUPPORTED | `quick_wins[5].text` | 60 | demand.md, evidence/dfs-bl-spam-refdomains.json, evidence/dfs-serp-rechtsanwalt-troisdorf.json |
| SUPPORTED | `final.p` | 30 | competitors.md, demand.md, evidence/chat-2026-10-31.md |
| SUPPORTED | `guide.point` | 320 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `guide.point` | 20 | competitors.md, demand.md, evidence/chat-2026-10-31.md |
| SUPPORTED | `guide.think` | 2016 | evidence/rendered-berater.md, homepage.md, intake.md |
| SUPPORTED | `guide.think` | 2018 | evidence/rendered-berater.md, homepage.md, intake.md |
