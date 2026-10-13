# 1.2 Library search — 2026-10-14

## grep -ril "canary": 0 hits
## grep -ril "heartbeat": 2 hits
- official-docs/claude-code/changelog-recent.md
- official-docs/whats-new/2026-w30.md
## grep -ril "dead.man": 0 hits
## grep -ril "uptime": 0 hits
## grep -ril "healthcheck": 0 hits
## grep -ril "synthetic": 2 hits
- official-docs/claude-code/changelog-recent.md
- blog/automating-eval-design-and-hillclimbing.md
## grep -ril "monitor": 29 hits
- official-docs/claude-code/best-practices.md
- official-docs/claude-code/common-workflows.md
- official-docs/claude-code/routines.md
- official-docs/claude-code/worktrees.md
- official-docs/claude-code/scheduled-tasks.md
- official-docs/claude-code/changelog-recent.md
- official-docs/claude-code/whats-new.md
- official-docs/claude-code/large-codebases.md
## grep -ril "alert": 8 hits
- official-docs/claude-code/routines.md
- official-docs/claude-code/hooks-guide.md
- official-docs/claude-code/changelog-recent.md
- blog/automating-eval-design-and-hillclimbing.md
- videos/045-context-engineering-explained-what-every-ai-developer-should-know.md
- _derived/rules.md
- _derived/extracts/045.md
- videos/036-how-anthropic-uses-claude-code-agentic-software-engineering-at-scale-d.md

## What the relevant hits say (read order: official doc → blog → extract)
- official-docs/claude-code/routines.md:33 — **"Alert triage" use case**: the monitoring tool calls the routine's API endpoint when an error threshold is crossed and passes the alert body as `text`; the prompt tells Claude to investigate the alert in the fire payload. → This is the official shape for canary step "diagnose + self-heal".
- routines.md:163-205 — API trigger: POST `/fire` with a per-routine bearer token; `text` arrives as untrusted `<routine-fire-payload>`; the prompt must opt in ("Investigate the alert in the routine-fire-payload block"). Beta header `experimental-cc-routine-2026-04-01`; claude.ai users only.
- routines.md:143 — schedule minimum interval 1 hour → routines cannot be the detection layer for a 1-hour outage target.
- scheduled-tasks.md:25 / desktop-scheduled-tasks.md:25,68,72 — Desktop/CLI tasks: 1-minute interval, but only while the app runs and the computer is awake; missed runs get ONE catch-up run. CLI `/loop` tasks expire after 7 days. → not reliable alone for detection.
- whats-new/2026-w30 + changelog: "heartbeat" hits are about tool-call progress, not monitoring (not relevant).
- blog/automating-eval-design-and-hillclimbing.md: "alert" = eval headroom warning (not relevant).
- rules.md section 6 (R6.1–R6.12): bookmarks per source, failed read ≠ "nothing new", confirm before ledger, read-only credentials, spend cap, time zone, open the run even when green. All apply to canaries.

Conclusion: library covers the agent/routine half (alert triage via API trigger, unattended rules). It has nothing on canary/heartbeat/synthetic monitoring → fresh web research (step 1.3, ops-library files).
