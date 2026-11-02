# 13 — 741 internal: the control mechanisms a job description must map onto (state 2026-11-03)

Type: internal inventory, read from the repo and memory on 2026-11-03.

## Enforcement that exists today
- Go-gate (hook rung): `.claude/hooks/live_change_gate.py` (PreToolUse on Bash/Edit/Write/Novamira/Porkbun) denies FTP deploys, Novamira write abilities, PHP write calls, Porkbun hosting writes, and edits of settings/hook files unless a go marker exists. Markers come from `go_marker.py` (typed standalone "go" in Martin's prompt) or `go_card.py` (a chosen AskUserQuestion answer with a standalone "Go"). One turn, 30-minute TTL. Memory: `go-gate-hook-needs-typed-go`. README: `.claude/hooks/README.md`.
- Slop gate (Stop rung): `slop_gate.py` blocks a reply whose ```text block scores below 5/5.
- Per-change go rules in memory (prose rung): `no-website-changes-without-go`, `ads-changes-need-reasoned-go`, `db-write-needs-isolated-confirmation`, `email-sending-airmailer` (Claude never sends e-mails), `never-ask-about-posting-timing`, `analysis-request-no-build-cards`.
- Night shift v2 (runner rung): runs only when `reporting/night-shift/queue/<date>.json` exists (written by the 17:00 grill card); `--permission-mode dontAsk --setting-sources user --strict-mcp-config`; Write/Edit only under reporting/night-shift/**; curl/ftp/ssh/git push/rm denied; caps 14 runs / USD 10; STOP file. Memory: `night-shift-server-workflow`.
- Morning grill (manager rung): 06:13 brief, max 7 decision cards, `state/cards.json` ledger, 17:00 evening log with 5 checks (roadmap position, done, open, not delegated, waiting for). Command Center admin tab on clients.741.studio. Memory: `morning-grill-workflow`. Automation currently OFF (`morning-grill-automation-disabled`, 02.11.).
- Workflow registry: `00_project/workflow-registry/registry.json` (28 ids) and `_run.json` telemetry per run; creation process `00_project/workflow-creation-workflow.md` with gates cp1/cp2/install.
- Desktop scheduled tasks (`~/.claude/scheduled-tasks/<id>/SKILL.md`): the prompt file IS the agent's only standing instruction for that run.
- Memory files (prose rung): `~/.claude/projects/-Users-martindrendel-741website/memory/`, MEMORY.md index (hard rules marked HARD).
- CLAUDE.md layers: `~/.claude/CLAUDE.md` (grill rule, pre-send sweep, login prep, Vorab-Bestätigung, e-mails only Martin), `741website/CLAUDE.md` (STE, slop check, Supabase backbone, WP plain-text fields, roadmap pre-flight, body copy only via /content-write).

## Roster inputs (what runs as an "agent" today)
See `_derived/roster-2026-11-03.md`.

## Assessment for 741
What Tyler's design would duplicate if copied blindly: a second approval system next to the go-gate; a second manager next to the morning grill; a second memory next to MEMORY.md. The job description must point at these, not replace them.
Gap the research exposes: no agent today has a written scope with a "never" list bound to its hook rung; no weekly review exists (the evening log is daily and per client, not per agent); scheduled-task prompts are the only per-agent standing instruction and they are not reviewed; worktree client chats run with bypass permissions where only the PreToolUse hook holds.
