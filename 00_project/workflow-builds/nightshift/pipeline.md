# 2.4 Pipeline with checkpoints · 2.5 Degrees of freedom

Times in WITA (UTC+8). Server clock = `Asia/Makassar`. CP = checkpoint where Martin decides.

```
LAPTOP (day machine)                                SERVER (Hetzner VPS, Nuremberg)
17:00  morning-grill-1700 → evening log
       + "Night queue" card (≤ 8 items, class, client)
       ── CP-A  Martin ticks / removes items (phone or chat)
17:30                                               P0 start (systemd timer)
                                                     ├ kill switch? (Command Center flag + /srv/nightshift/STOP)
                                                     ├ git pull main (read) · read queue + answers (Supabase, read)
                                                     ├ no answer → only read-only items (research, audits)
                                                     └ plan.json = queue (SCRIPT, no LLM planner)
17:35–19:10                                         P1 batch 1: per item  Executor (claude -p) → Critic (claude -p)
                                                        pass → night card · fail → 1 retry · 2nd fail → needs_martin card
19:15                                               P2 mail "Night shift: n cards ready" → martin@741.studio
19:30  ── CP-B  check-in 1 (≤ 5 cards, ~5 min, Command Center on phone)
19:35–21:10                                         P3 pull answers → batch 2 (redo notes, next items)
21:15                                               P2 mail
21:30  ── CP-C  check-in 2 (≤ 5 cards)
21:35–04:45                                         P4 batch 3: long items (server builds + QA); no card waits
05:00                                               P5 stop · REVIEW.md + night-report.json (SCRIPT)
                                                     · push branch nightshift/<date> · pulse line · _run.json
06:13  morning-grill-0600 reads S6 = night report   (after 22:00 no mail; open items wait here)
       ── CP-D  morning grill: release / redo / park
```

Breakers (any one stops the night): 14 `claude -p` runs · est. USD 10 (sum of `total_cost_usd`) · plan-limit error · 05:00 · kill switch. Stop before 22:00 → one stop mail. After 22:00 → silent, shown at 06:13.

Budget math (N7 = 14 runs): planner and reviewer are scripts, so 14 runs = 7 items × (Executor + Critic) with no retries. Each retry or redo costs 2 runs. Success target "≥ 5 items pass per night" (N15) leaves room for 2 retries. This is tight; the first week shows if 14 is enough.

## 2.5 Degrees of freedom per step

| Step | Freedom | Form | Why |
|---|---|---|---|
| Kill switch, window, breakers, lock | none | script (runner) | must hold every time |
| Queue read, plan.json | none | script | Martin already decided the queue; old LLM planner had the count bug |
| Class check (night vs never) | low | script + deny list, LLM only for unknown items → then `needs_martin` | a wrong "night" is the main risk |
| Data pulls (DataForSEO, GSC, GA4, Falcon reads) | low | scripts with read keys | real data only, reproducible |
| Executor (spec, draft, audit, build) | high | skill heuristics (`night-shift` v2 + seo-page-optimizer, content-writing rules) | open creative work |
| Critic | medium | checklist rubric + scripts (deslop, NAP match, JSON-LD validate, HWG scan, screenshot QA) | writer never grades itself |
| Night card text | medium | template (headline, evidence link, options, recommendation) | one-minute cards |
| Mail ping | none | fixed template, fixed address, sent by runner (not by Claude) | no client data, no free text |
| REVIEW / night report / pulse / _run.json | none | script | morning grill parses it |
| Push to branch `nightshift/<date>` | none | script; deny `git push` to main in Claude's rules | server never writes main |
