# 1.1 Building block — booking-sequence (2026-10-14)

Source: _derived/rules.md sections 0+1, patterns.md section 3 (decision tree).

Decision tree walk:
1. Runs on a schedule with nobody present? NO for the main run (Martin pastes a booking). The two follow-up reminders are time-bound, so they use one-time Desktop scheduled tasks (`fireAt`), not a routine.
2. Stream of related tasks over weeks? NO (one run per booking).
3. One repeatable procedure Martin triggers? YES → project skill `.claude/skills/booking-sequence/`.
   Side effects: it spends a little money (DataForSEO, cap 0,30 USD) and creates 2 scheduled tasks. It never sends anything. → `disable-model-invocation` is NOT set, because Martin pastes a cal.com booking without a slash command, and the skill must trigger on that (same choice as local-seo-review-page). The safety comes from the Critical rules + the check script, not from slash-only.
5. Must one step happen every time? YES: slop 5/5, no booking link, no tool names, time-zone maths → deterministic scripts (`check_sequence.py`, `tz_times.py`).
6. External systems? DataForSEO via existing `dfs.py`, scheduled-tasks MCP for reminders.

Choice (one line): **Project skill `booking-sequence` (sequential workflow with gates, patterns.md 4.1) + 2 scripts (time zones, message check) + 2 one-time Desktop scheduled tasks per booking that only remind Martin.**
