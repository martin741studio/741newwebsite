# 1.5 Research note — booking-sequence (2026-10-14)

**Block:** project skill `booking-sequence`, sequential with gates (patterns.md 4.1) + iterative refinement for the slop gate (4.3). Two scripts: `tz_times.py` (call time → prospect zone, send times, fireAt values) and `check_sequence.py` (hard rules on the 3 messages + slop 5/5). Two one-time Desktop scheduled tasks per booking only remind Martin.

**3 rules that shape the design**
1. R6.6 time zone: state zones explicitly; compute with zoneinfo, never by hand (CEST→CET switch on 25.10.2026 hits the reference case).
2. desktop-scheduled-tasks.md "Missed runs": a sleeping laptop fires the reminder late → the reminder prompt checks "now vs. call start" and marks the message as late/obsolete instead of "send now".
3. R2.7 feedback loop: run check → fix → re-check; deliver only at 5/5 and a clean rule check (CLAUDE.md slop rule).

**1 pattern:** 4.1 gates: intake → find page + baseline → fresh check (free first, paid ≤ 0,30 USD) → pick NEW insights → write 3 messages → check script → file + reminders → show Martin.

**Reuse:** dfs.py (cap + ledger), case-library.json, deslop_de.py --claims, Korinna file + task prompts as templates, registry `_run.json` in `prospects/<slug>/booking/`.

**Open questions (→ checkpoint 1 card):** (a) fixed send times: message 2 exactly 24 h before or "morning of the call day" (Martin's voice note said both; hand-run used 24 h); (b) reminder push vs. only task output (hand-run: PushNotification if available); (c) what if the booking is < 24 h before the call (skip message 2 or merge into 1).
