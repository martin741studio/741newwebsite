# 1.1 Building block — canary (2026-10-14)

Source: _derived/rules.md sections 0+1, patterns.md section 3 (decision tree).

Decision tree walk:
1. Runs on a schedule with nobody present? YES. But the target is "no outage longer than 1 hour".
   - Cloud routine: minimum interval 1 hour (official-docs/claude-code/routines.md:143). Too slow alone: detect (≤60 min) + alert + fix > 60 min.
   - Desktop scheduled task: 1-minute interval, but runs only while the laptop is awake (desktop-scheduled-tasks.md:68). Martin's laptop sleeps. Not reliable for detection.
   - So: DETECTION must not depend on an LLM run or on the laptop.
5. Must one step happen every time without fail? YES (the check itself) → deterministic script, not an advisory prompt (R0.5 logic).
6. Needs external systems (Zapier, Tally, Pipedrive, KlickTipp, Google Ads, websites)? YES → MCP / API + skill that teaches the usage (R0.6).

Choice (one line): **Hybrid — a deterministic always-on check layer (scripts on an off-laptop scheduler, every 5–15 min, plus a monitor service as watcher-of-the-watcher) feeds incidents to an agent skill `/canary` that diagnoses, self-heals inside an allow-list, and escalates by phone push; the same skill adds new canaries to one registry.**

Reason: an LLM is too slow and too costly for minute checks and the laptop sleeps; an agent is right for diagnosis, safe fixes and the registry work. Rules used: R0.5 (must-happen → deterministic), R0.6 (MCP + skill), R0.7 (schedule), R0.9 (unattended + external systems → vault credentials, budget), R1.7 (fragile step → script), R1.8 (fixes = plan-validate-execute).
Open: which always-on host (Supabase pg_cron / Edge Function, Hetzner server from Night Shift, or an external monitor SaaS) — decided after 1.4 and the research.
