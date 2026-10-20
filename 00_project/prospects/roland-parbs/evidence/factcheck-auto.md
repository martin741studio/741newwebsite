# Automatic fact check: Roland Parbs (2026-10-16, factcheck.py)

Input: `prospect.json`. Evidence: `evidence/*`, findings files, `case-library.json`, derived counts. Run time 0.0 s.

- Numbers: 128 · supported 102 · not found 18 · rule constants 0 · assumptions 8
- Merged-variant errors: 0 · count-claim mismatches: 0 · absolute words: 16

## Must fix (mechanical)

- none

## For the fresh agent: check only these claims

| Field | Claim | Why listed |
| --- | --- | --- |
| `hero.sub` | 404 | number not in any evidence file |
| `hero.cards[3].sub` | 404 | number not in any evidence file |
| `hero.cards[3].badge` | 404 | number not in any evidence file |
| `grid.chips[1]` | 404 | number not in any evidence file |
| `system.steps[2].kpi` | 404 | number not in any evidence file |
| `system.step1.depth.title` | 404 | number not in any evidence file |
| `system.step1.depth.sub` | 404 | number not in any evidence file |
| `system.step2.changes[1].text` | 404 | number not in any evidence file |
| `system.step3.note_today` | 404 | number not in any evidence file |
| `system.step3.five[0].a` | 404 | number not in any evidence file |
| `calc.cpc` | 0.7 | number not in any evidence file |
| `check[0].rows[0].text` | 404 | number not in any evidence file |
| `check[1].rows[1].text` | 404 | number not in any evidence file |
| `roadmap[0].what` | 404 | number not in any evidence file |
| `final.p` | 404 | number not in any evidence file |
| `guide.point` | 404 | number not in any evidence file |
| `headlines.hero_sub` | 404 | number not in any evidence file |
| `headlines.step3_h2` | 404 | number not in any evidence file |
| `system.step3.score_draft_label` | 36 / 44 | count claim without a derived count |
| `hero.sub` | Bei der Suche „heilpraktiker dannenberg“ ist deine Praxis an nur 1 von 49 Punkten unter den ersten drei – und deine hinterlegte Website zeigt einen 404-Fehler. | absolute word (nur) |
| `grid.h2` | Unter den ersten drei an nur 1 von 49 Punkten. | absolute word (nur) |
| `grid.caption_today` | Unter den ersten drei an nur 1 von 49 Punkten (2,04 % Sichtbarkeit). | absolute word (nur) |
| `grid.caption_today` | Herr Günther Bentz erreicht mit nur 2 Bewertungen 32,65 % Sichtbarkeit. | absolute word (nur) |
| `system.step2.h2` | Günther Bentz führt mit nur 2 Bewertungen. | absolute word (nur) |
| `system.step2.lead` | Eine der vier ersten sind an allen 49 Messpunkten unter den ersten 20 zu sehen. | absolute word (allen) |
| `system.step2.good` | Weil im Landkreis Lüchow-Dannenberg selbst die Top-Profile nur 0 bis 11 Bewertungen haben, genügen wenige gezielte Optimierungen, um ganz oben zu stehen. | absolute word (nur) |
| `check[0].rows[1].title` | Nicht immer verschlüsselt | absolute word (immer) |
| `quick_wins[0].text` | Den Eintrag bei Google offiziell als Inhaber bestätigen, um alle Profilfunktionen freizuschalten. | absolute word (alle) |
| `roadmap[0].why` | Ohne funktionierenden Link und Telefonnummer gehen heute alle Interessenten verloren | absolute word (alle) |
| `roadmap[1].why` | Mitbewerber führen mit nur 2 bis 11 Bewertungen – die Lücke ist schnell geschlossen | absolute word (nur) |
| `guide.point` | Günther Bentz führt mit nur 2 Bewertungen die Karte an. | absolute word (nur) |
| `headlines.hero_h1` | Bei „heilpraktiker dannenberg“ steht deine Praxis an nur 1 von 49 Punkten unter den Top 3. | absolute word (nur) |
| `headlines.hero_sub` | Bei der Suche „heilpraktiker dannenberg“ ist deine Praxis an nur 1 von 49 Punkten unter den ersten drei – und deine hinterlegte Website zeigt einen 404-Fehler. | absolute word (nur) |
| `headlines.grid_h2` | Unter den ersten drei an nur 1 von 49 Punkten. | absolute word (nur) |
| `headlines.step2_h2` | Günther Bentz führt mit nur 2 Bewertungen. | absolute word (nur) |

## Count claims

| Verdict | Field | Claim | Evidence |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].sub` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.h2` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[1].kpi` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | Eine der vier | derived (evidence_lib.facts) |
| NO PAIR | `system.step3.score_draft_label` | 36 / 44 | no derived count with total 44: the agent checks it |
| SUPPORTED | `guide.point` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 1 von 49 | derived (evidence_lib.facts) |
| SUPPORTED | `headlines.grid_h2` | 1 von 49 | derived (evidence_lib.facts) |

## All numbers

| Verdict | Field | Value | Evidence file |
| --- | --- | --- | --- |
| SUPPORTED | `hero.sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.sub` | 1 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `hero.sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| NOT FOUND | `hero.sub` | 404 |  |
| SUPPORTED | `hero.cards[1].sub` | 1 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `hero.cards[1].sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[1].badge` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `hero.cards[1].badge` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `hero.cards[2].sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `hero.cards[2].sub` | 2 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| NOT FOUND | `hero.cards[3].sub` | 404 |  |
| NOT FOUND | `hero.cards[3].badge` | 404 |  |
| SUPPORTED | `grid.grid_size` | 7 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `grid.h2` | 1 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `grid.h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `grid.intro` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.intro` | 10 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 1 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `grid.caption_today` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_today` | 2,04 | derived (evidence_lib.facts), evidence/falcon-report-65631fcef076bb8.json |
| SUPPORTED | `grid.caption_today` | 2 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `grid.caption_today` | 32,65 | derived (evidence_lib.facts), evidence/falcon-report-65631fcef076bb8.json |
| SUPPORTED | `grid.caption_goal` | 3 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `grid.caption_goal` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `grid.caption_goal` | 11 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| NOT FOUND | `grid.chips[1]` | 404 |  |
| SUPPORTED | `system.steps[0].kpi` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `system.steps[1].kpi` | 1 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.steps[1].kpi` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.steps[2].text` | 5 | competitors.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| NOT FOUND | `system.steps[2].kpi` | 404 |  |
| SUPPORTED | `system.step1.h2` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `system.step1.demand_sub` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step1.demand_sub` | 12 | evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json, evidence/falcon-report-65631fcef076bb8.json |
| SUPPORTED | `system.step1.demand[0].volume` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `system.step1.demand_note` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| NOT FOUND | `system.step1.depth.title` | 404 |  |
| NOT FOUND | `system.step1.depth.sub` | 404 |  |
| SUPPORTED | `system.step1.depth.big[0].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step1.depth.big[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.h2` | 2 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step2.lead` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.lead` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `system.step2.lead` | 29 | competitors.md, derived (evidence_lib.facts), evidence/falcon-report-65631fcef076bb8.json |
| SUPPORTED | `system.step2.table[0].reviews` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[0].share` | 2 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step2.table[1].reviews` | 2 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED (rounded) | `system.step2.table[1].share` | 32,6 | derived (evidence_lib.facts), evidence/falcon-report-65631fcef076bb8.json |
| SUPPORTED | `system.step2.table[2].reviews` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[2].share` | 30,6 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[3].reviews` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED (rounded) | `system.step2.table[3].share` | 30,6 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.table[4].reviews` | 11 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED (rounded) | `system.step2.table[4].share` | 26,5 | derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 16.10.2026 | competitors.md, cost_ledger.jsonl |
| SUPPORTED | `system.step2.fine` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.fine` | 10 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.meaning` | 11 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step2.meaning` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| NOT FOUND | `system.step2.changes[1].text` | 404 |  |
| SUPPORTED | `system.step2.changes[3].title` | 3 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step2.changes[3].title` | 5 | competitors.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `system.step2.cleanup[0].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[0].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.cleanup[1].n` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.good` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `system.step2.good` | 11 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `system.step3.lead` | 22 | evidence/falcon-report-65631fcef076bb8.json |
| SUPPORTED | `system.step3.score_today` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| ASSUMPTION | `system.step3.score_draft` | 0 | calc start value or target, label it on the page |
| SUPPORTED | `system.step3.score_draft_label` | 36 | evidence/falcon-report-65631fcef076bb8.json, intake.md |
| SUPPORTED | `system.step3.score_draft_label` | 44 | evidence/falcon-report-65631fcef076bb8.json |
| NOT FOUND | `system.step3.note_today` | 404 |  |
| NOT FOUND | `system.step3.five[0].a` | 404 |  |
| SUPPORTED | `calc.vol` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| ASSUMPTION | `calc.vol_min` | 20 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.vol_max` | 2000 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.budget` | 150 | calc start value or target, label it on the page |
| NOT FOUND | `calc.cpc` | 0.7 |  |
| ASSUMPTION | `calc.conv` | 4 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.deal` | 40 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val` | 100 | evidence/falcon-report-65631fcef076bb8.json, prospect-mini/case-library.json |
| ASSUMPTION | `calc.val_min` | 100 | calc start value or target, label it on the page |
| ASSUMPTION | `calc.val_max` | 2000 | calc start value or target, label it on the page |
| SUPPORTED | `calc.val_label` | 100 | evidence/falcon-report-65631fcef076bb8.json, prospect-mini/case-library.json |
| SUPPORTED | `calc.volumes_line` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `calc.volumes_line` | 70 | evidence/dfs-volumes-regional.json |
| SUPPORTED | `calc.volumes_line` | 50 | evidence/dfs-volumes-regional.json, evidence/falcon-report-65631fcef076bb8.json |
| SUPPORTED | `calc.volumes_line` | 100 | evidence/falcon-report-65631fcef076bb8.json, prospect-mini/case-library.json |
| NOT FOUND | `check[0].rows[0].text` | 404 |  |
| NOT FOUND | `check[1].rows[1].text` | 404 |  |
| SUPPORTED | `check[3].rows[0].text` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `check[3].rows[0].text` | 2 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `check[3].rows[0].text` | 11 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `quick_wins[3].title` | 3 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| NOT FOUND | `roadmap[0].what` | 404 |  |
| SUPPORTED | `roadmap[1].what` | 3 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `roadmap[1].what` | 5 | competitors.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `roadmap[1].why` | 2 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `roadmap[1].why` | 11 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `final.h2` | 30 | competitors.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `final.p` | 30 | competitors.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| NOT FOUND | `final.p` | 404 |  |
| SUPPORTED | `guide.point` | 2 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `guide.point` | 1 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `guide.point` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `guide.point` | 3 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| NOT FOUND | `guide.point` | 404 |  |
| SUPPORTED | `guide.think` | 3 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `guide.insight` | 3 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.hero_h1` | 1 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.hero_h1` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_h1` | 3 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.hero_sub` | 0 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.hero_sub` | 1 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.hero_sub` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| NOT FOUND | `headlines.hero_sub` | 404 |  |
| SUPPORTED | `headlines.grid_h2` | 1 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.grid_h2` | 49 | competitors.md, cost_ledger.jsonl, derived (evidence_lib.facts) |
| SUPPORTED | `headlines.step1_h2` | 20 | derived (evidence_lib.facts), evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| SUPPORTED | `headlines.step2_h2` | 2 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.step3_h2` | 5 | competitors.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
| NOT FOUND | `headlines.step3_h2` | 404 |  |
| SUPPORTED | `headlines.roadmap_h2` | 8 | competitors.md, derived (evidence_lib.facts), evidence/dfs-volumes-ads.json |
| SUPPORTED | `headlines.final_h2` | 30 | competitors.md, evidence/dfs-volumes-ads.json, evidence/dfs-volumes-regional.json |
