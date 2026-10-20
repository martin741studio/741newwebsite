# Automatic fact check: Stephan Meyer (2026-10-12, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.1 s.

- Numbers: 151 · supported 143 · not found 0 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 23

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `grid.h2` | Selbst bei „business coach jena“ stehen an allen 49 Punkten andere Anbieter vor dir | absolute word (allen) |
| `grid.intro` | Die Karte ist hier nur ein Nebenbefund: | absolute word (nur) |
| `grid.caption_today` | An allen 49 Punkten „20+“: | absolute word (allen) |
| `grid.caption_goal` | Ziel-Szenario, nur zur Veranschaulichung. | absolute word (nur) |
| `grid.caption_goal` | Alle vier haben Bewertungen (1 bis 39) und eine Adresse in Jena. | absolute word (alle) |
| `grid.chips[0]` | 🧭 Einordnung als Coach, nicht nur als Unternehmensberater | absolute word (nur) |
| `system.step1.items[1].why` | Den Begriff gibt es bei dir nur in Blogbeiträgen, nicht auf einer Leistungsseite. | absolute word (nur) |
| `system.step1.items[2].why` | Deine Seite „Der Coach“ heißt bei Google nur „Coach \| Dr. | absolute word (nur) |
| `system.step1.items[4].why` | Deine Seite „Der Coach“ (/de/coach/) steht für deinen Namen auf Platz 8, fehlt aber, wie alle Seiten unter /de/, in der Liste, die deine Website an Google meldet. | absolute word (alle) |
| `system.step2.lead` | Die vier ersten sind an allen 49 Messpunkten unter den ersten 20 zu sehen, dein Eintrag an keinem. | absolute word (allen) |
| `system.step2.meaning` | Alle vier haben Bewertungen (1 bis 39) und eine Adresse in Jena. | absolute word (alle) |
| `system.step2.changes[0].text` | Dein Eintrag hat keine Coaching-Einordnung, nur Unternehmensberater, Dienstleister und Personalberatung. | absolute word (nur) |
| `system.step2.changes[5].text` | Ein Beitrag alle zwei Wochen und Fotos von dir bei Vorträgen und im Coaching halten den Eintrag aktuell. | absolute word (alle) |
| `system.step3.five[2].a` | Nur „Dr.“ im Kopf der Seite. | absolute word (nur) |
| `system.step3.five[3].a` | Die Buchung des Videocalls gibt es nur auf der Kontaktseite. | absolute word (nur) |
| `system.step3.five[4].a` | Dein Name steht nur im Kopf der Seite. | absolute word (nur) |
| `check[0].rows[1].text` | Die Kontaktseite sagt „use the form below“, darunter steht aber nur die Buchung eines Videocalls. | absolute word (nur) |
| `check[0].rows[4].title` | Immer verschlüsselt | absolute word (immer) |
| `check[0].rows[4].text` | Deine Seite öffnet sich immer mit dem Schloss-Symbol im Browser. | absolute word (immer) |
| `check[3].rows[0].text` | Auf der Website stehen drei Stimmen von Kunden, nur mit Kürzeln wie „B.L., CEO“. | absolute word (nur) |
| `quick_wins[4].text` | Für alle, die erst eine Frage stellen wollen, bevor sie einen Termin buchen. | absolute word (alle) |
| `guide.point` | Nach „business coach jena“ wird nur rund 10 Mal im Monat gesucht, die Karte ist also eine Stichprobe. | absolute word (nur) |
| `headlines.grid_h2` | Selbst bei „business coach jena“ stehen an allen 49 Punkten andere Anbieter vor dir | absolute word (allen) |
| (text) | executive coach + executive coaching | both forms named: say that Google counts them together (210), never add them up |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.cards[1].sub` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[3].badge` | 15 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `grid.caption_goal` | Drei der vier | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 0 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].kpi` | 15 von 44 | evidence/scorecard-today.md |
| SUPPORTED | `system.step2.meaning` | Drei der vier | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[0].text` | Drei der vier | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 63 / 1139 | evidence/visual-check.md |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 25 | evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `hero.cards[0].badge` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `hero.cards[2].sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 39 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `hero.cards[3].badge` | 15 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `hero.cards[3].badge` | 44 | derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 53 | competitors.md, evidence/chat-2026-10-12.md, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `grid.caption_today` | 91,8 | evidence/visual-check.md |
| SUPPORTED | `grid.caption_today` | 39 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `grid.caption_goal` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `grid.caption_goal` | 39 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `grid.caption_goal` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[0].kpi` | 2.900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.steps[1].kpi` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.steps[2].kpi` | 15 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.steps[2].kpi` | 44 | derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step1.h2` | 2.900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand_sub` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step1.demand_sub` | 12 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[0].volume` | 2900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[1].volume` | 2900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[2].volume` | 390 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[3].volume` | 390 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.demand[4].volume` | 260 | demand.md, evidence/dfs-volumes-ads.json, evidence/site.json |
| SUPPORTED | `system.step1.demand[5].volume` | 210 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-name2.json |
| SUPPORTED | `system.step1.demand[6].volume` | 90 | demand.md, evidence/dfs-volumes-ads.json, evidence/falcon-report-9e36ae89b77f5f2.json |
| SUPPORTED | `system.step1.demand[7].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand[8].volume` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.demand_note` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.demand_note` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.big[0].n` | 2.166 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.big[1].n` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.depth.bars[0].val` | 2166 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step1.depth.bars[1].label` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.depth.bars[1].val` | 1616 | derived (evidence_lib.facts), evidence/visual-check.md, site-findings.md |
| SUPPORTED | `system.step1.items[0].why` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[1].why` | 2.900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[1].why` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.items[2].why` | 2.900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[3].why` | 260 | demand.md, evidence/dfs-volumes-ads.json, evidence/site.json |
| SUPPORTED | `system.step1.items[3].why` | 390 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[3].why` | 17,63 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[4].why` | 390 | demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step1.items[4].why` | 8 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step1.items[5].why` | 1.940 | evidence/site-urls.json, evidence/site.json, site-findings.md |
| SUPPORTED | `system.step1.items[5].why` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.h2` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.h2` | 39 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.lead` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].reviews` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].share` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[1].reviews` | 39 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.table[1].share` | 91,8 | evidence/visual-check.md |
| SUPPORTED | `system.step2.table[2].reviews` | 3 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[2].share` | 83,7 | competitors.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 23 | competitors.md, derived (evidence_lib.facts), evidence/comp-pages.json |
| SUPPORTED (rounded) | `system.step2.table[3].share` | 77,5 | competitors.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED (rounded) | `system.step2.table[4].share` | 24,5 | competitors.md, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.meaning` | 39 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.meaning` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 53 | competitors.md, evidence/chat-2026-10-12.md, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.changes[2].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.changes[2].text` | 39 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.changes[2].text` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.changes[5].text` | 15.09.2026 | evidence/google-panel-2026-10-12.md, evidence/site-pages.json |
| SUPPORTED | `system.step2.cleanup[0].n` | 63 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step2.cleanup[0].n` | 1139 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `system.step2.cleanup[1].n` | 8 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[1].text` | 8 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].n` | 8 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].text` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[2].text` | 8 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `system.step2.cleanup[3].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.good` | 2.166 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `system.step2.good` | 1.616 | derived (evidence_lib.facts), evidence/visual-check.md, site-findings.md |
| SUPPORTED | `system.step3.lead` | 22 | evidence/chat-2026-10-12.md, evidence/comp-pages.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step3.score_today` | 15 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| ASSUMPTION | `system.step3.score_draft` | 36 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step3.score_draft_label` | 44 | derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `system.step3.note_draft` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.vol` | 210 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-name2.json |
| ASSUMPTION | `calc.vol_min` | 50 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 3000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| SUPPORTED | `calc.cpc` | 6.9 | evidence/visual-check.md |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 3000 | evidence/falcon-report-9e36ae89b77f5f2.json, evidence/visual-check.md |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 10000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.volumes_line` | 12.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `calc.volumes_line` | 12 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `calc.volumes_line` | 210 | demand.md, derived (evidence_lib.facts), evidence/dfs-serp-name2.json |
| SUPPORTED | `calc.volumes_line` | 2.900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 2.900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 6,94 | demand.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `calc.volumes_line` | 6,90 | evidence/visual-check.md |
| SUPPORTED | `calc.volumes_line` | 3.000 | evidence/falcon-report-9e36ae89b77f5f2.json, evidence/visual-check.md |
| SUPPORTED (rounded) | `check[0].rows[2].text` | 3,3 | derived (evidence_lib.facts) |
| SUPPORTED | `check[1].rows[3].text` | 1.940 | evidence/site-urls.json, evidence/site.json, site-findings.md |
| SUPPORTED | `check[1].rows[3].text` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[1].rows[4].text` | 2.166 | derived (evidence_lib.facts), evidence/site-pages.json, evidence/site.json |
| SUPPORTED | `check[1].rows[4].text` | 1.616 | derived (evidence_lib.facts), evidence/visual-check.md, site-findings.md |
| SUPPORTED | `check[3].rows[0].text` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[1].text` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 2 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[1].text` | 8 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `check[3].rows[3].text` | 50 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `check[3].rows[4].text` | 63 | demand.md, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `check[3].rows[4].text` | 1.139 | demand.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `roadmap[1].why` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `final.h2` | 30 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `final.p` | 30 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
| SUPPORTED | `guide.point` | 10 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `guide.celebrate` | 18 | evidence/chat-2026-10-12.md, evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json |
| SUPPORTED | `guide.celebrate` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.hero_h1` | 2.900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.hero_h1` | 20 | competitors.md, demand.md, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 25 | evidence/dfs-backlinks-summary.json, evidence/dfs-refdomains-spam.json, evidence/dfs-serp-1.json |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 2.900 | competitors.md, demand.md, evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.step2_h2` | 1 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.step2_h2` | 39 | competitors.md, derived (evidence_lib.facts), evidence/dfs-backlinks-summary.json |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.roadmap_h2` | 8 | competitors.md, cost_ledger.jsonl, demand.md |
| SUPPORTED | `headlines.final_h2` | 30 | cost_ledger.jsonl, derived (evidence_lib.facts), evidence/dfs-refdomains-spam.json |
