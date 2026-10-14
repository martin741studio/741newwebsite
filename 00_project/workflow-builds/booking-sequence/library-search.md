# 1.2 Library search — 2026-10-14

```
grep -ril "whatsapp" 00_project/knowledge/workflow-library/   → 3 hits (power-user tips: PermissionRequest to WhatsApp; video 032 extract R5: client WhatsApps as voice source). Not relevant to a booking follow-up.
grep -ril -E "fireAt|one-time|reminder" official-docs   → desktop-scheduled-tasks.md, scheduled-tasks.md, skills.md …
```

Relevant hits (read order: official doc → extract):
- official-docs/claude-code/desktop-scheduled-tasks.md:48 — "remind me at 3pm tomorrow … creates a one-time task that disables itself after it fires". → fits the 24 h and 15 min reminders.
- desktop-scheduled-tasks.md:70-74 — **Missed runs**: if the laptop sleeps, Desktop starts ONE catch-up run on wake; "A task scheduled for 9am might run at 11pm … add guardrails to the prompt itself". → The reminder prompt must compare now with the call time and say "too late" instead of showing a stale message as ready. (The hand-run Korinna tasks do not have this guardrail. Fix in the skill.)
- scheduled-tasks MCP tool doc: `fireAt` = ISO 8601 with offset, runs once, no jitter; app must be open, else runs on next launch.
- rules.md R6.6: state the time zone in any date maths. → cal.com shows Asia/Makassar (WITA, UTC+8); Germany switches CEST→CET on 25.10.2026. Korinna's call (26.10.) is the day after the switch → script, not mental maths.
- patterns.md 4.1 sequential workflow with gates; 4.3 iterative refinement (slop check → fix → re-check).
- Nothing in the library on sales follow-up sequences. Domain rules come from 741 memory (see coverage-map.md), not from the library.
