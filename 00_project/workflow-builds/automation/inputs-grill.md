# Step 0.0 Inputs Grill Record: P7 Automation Build

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `automation`
Status: Confirmed via Interactive Grill

---

## 1. The Job (Objective & Scope)
- **What enters:** Automation specifications, tool/account inventories (Zapier, Make, KlickTipp, Pipedrive, forms, Supabase edge functions, macOS LaunchAgents, Python/Node scripts).
- **What transforms:** Builds, tests, and hardens production scripts, LaunchAgents, and cron routines with error telemetry, automated runbooks, and rollback procedures.
- **Who uses output:** Agency operations team, Martin, and client automated workflows.

## 2. Runtime Surface
- **Primary surface:** Terminal (Claude Code CLI / Desktop IDE) and macOS `launchd` / local cron runners.
- **Enforcement surface:** Hook-level guards (`PreToolUse`, `UserPromptSubmit`, `Stop`) installed in `~/.claude/settings.json`.

## 3. Cadence / Frequency
- **Turnus:** On demand per automation build, integration task, or client funnel setup.

## 4. Hard Limits (Failure Boundaries)
- **Zero Unattended Daemon Spawns:** No script or LaunchAgent may run unattended without an explicit local dry-run, log destination, and kill switch.
- **No Unapproved Live Writes:** No messages to real people, no live Zapier/campaign publishing, no live database modifications without explicit Martin Go per action token (`go A<n>`).
- **Resource & Spend Limits:** Strict API credit spend cap and maximum execution timeout per automated job.
- **Credential Isolation:** Secrets stay strictly in `.secrets/` or `.env`; the agent never prints, types, or copies credentials into prompt context.
