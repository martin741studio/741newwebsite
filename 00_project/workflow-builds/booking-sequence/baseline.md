# 4.3 Baseline — with vs without the booking-sequence skill (2026-10-14, same booking, two fresh agents in parallel)

"Without" got the full task text (3 messages, timing, video URL, slop check, limits) but no skill and no access to the skill, the build folder or the Korinna example.

| | Without skill | With skill (functional test) |
|---|---|---|
| Wall time | 14:41:56–14:44:42 (≈ 3 min) | 14:41:46–14:44:25 (≈ 3 min) |
| Tool calls | ≈ 24 | ≈ 28 |
| Tokens | 159 786 | 155 138 (−3 %) |
| Cost | 0,094 USD | 0,106 USD |
| Slop 5/5 | yes (after building its own claims list) | yes (check loop, 2 rewrites) |
| 5 % traffic example (Martin's ask) | **missing** (volumes only) | present ("rund 95 Besucher … als Rechenbeispiel") |
| Success story facts | used Laserstein "um Platz 6 → Platz 1": the start rank is marked **unclear** in the library | used only the library's safe facts (Platz 1, 91 % der Karte) |
| Time zone | correct (by hand, noted DST) | correct (script, DST warning) |
| Reminders | **not created**; would set 5 min early, no late guard | created + verified + (dry run) deleted; late guard in prompt |
| File + registry | scratchpad only; "no home for these messages" | whatsapp-sequence.md + booking/_run.json (Excel) |
| HWG / tool names / booking link / formal address | checked by hand | checked by script on every run |
| Wishes listed by the agent | slug in the booking, list of facts already shown, a case-pick rule, a home for messages, one phone rule | all exist in the skill now (baseline.md, insight-menu §4, booking/ folder, step 2 phone rule) |
| Best idea | internal links: a June article on Bindungstrauma (1.600/month) linked only from "Seminare" | — → **adopted** as insight-menu item 6 |

Result: no speed or token gain (both ≈ 3 min, ≈ 155–160 k tokens). The gain is correctness and completeness: the skill run met all of Martin's rules (5 % example, safe case facts, reminders with late guard, file + registry), the baseline missed 2 of Martin's explicit asks and used one unsafe fact. One baseline idea made the skill better (item 6).
