---
name: automation-build
description: Builds and tests a client or 741 automation with safety layers and a test gate - Zapier/Make/n8n flows, CRM and email funnels (KlickTipp, Pipedrive, HubSpot, Skool, forms), webhooks, Supabase edge functions and crons, AI agents, and click work in web apps without an API. Use when Martin types /automation-build <client> <automation>, or asks to build, fix, rebuild or take live an automation, Zap, funnel flow, sync or integration ("Bau die Zapier-Strecke", "Automation für <Kunde>", "verbinde Skool mit KlickTipp"). Do NOT use for website pages or content (cro-homepage, seo-page-optimizer), review pages, one-off data pulls, or writing a message about an automation.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3:*), Agent
---

# Automation Build

Full rules: `/Users/martindrendel/741website/00_project/automation-workflow.md`. Templates: `00_project/automation-workflow/templates/`. Scripts: `00_project/automation-workflow/scripts/`.

## Critical

- No build before `go spec`. No send, switch-on or publish before Martin's `go A<n>` for exactly that action. Money, prices, delete, bulk and permissions: Martin only, write them into `martin-steps.md`.
- Every write is read back from the target system and saved as evidence. A click, "Typed" or an HTTP 200 is not proof.
- Say "done", "fertig", "läuft" or "live" only when `check_report.py` passes. The Stop hook blocks it otherwise.

## Inputs

- Client name and automation name (from the command).
- The client's docs and logins (LastPass or portal access grants). Martin enters secrets; you read env vars only.

## Workflow

Copy this checklist into your reply and tick it off.

- [ ] P0 Bind the run: `python3 00_project/automation-workflow/scripts/run_state.py init --session <session_id from the hook note> --client "<client>" --slug <slug>`. Read memory files on this client first.
- [ ] P0 Inventory (read only, Claude in Chrome or API/MCP). Open every list in full. Write `inventory.md` with account, object IDs and UI tricks. Every "missing" gets a second full check.
- [ ] P1 Spec: copy `templates/automation-spec-de.md` (or `-en`) to `spec.md` and fill it. `run_state.py phase --run <dir> --set spec`.
- [ ] CHECKPOINT A: show Martin the spec. Wait for his prompt `go spec`.
- [ ] P2 Environment: preflight (account shown, from-address, project ID, test inbox) into `evidence/preflight.md`. TEST records with `TEST-741`. Flow stays draft/off. Snapshots into `snapshots/`. Phase `environment`.
- [ ] P3 Build, one change at a time: snapshot → change → readback → screenshot into `evidence/` → `run_state.py log`. Phase `build`.
- [ ] P4 Test: fill `templates/test-plan.md`, run it, write `test-report.json` like `templates/test-report.example.json`. Max 3 fix attempts per case. Phase `test`.
- [ ] P5 Verify: start a fresh subagent with `templates/verifier-prompt.md`. Fix and re-test until VERDICT pass. Then run `python3 00_project/automation-workflow/scripts/check_report.py <dir>` until PASS. Phase `verify`.
- [ ] CHECKPOINT B: show Martin the report summary, evidence folder, `rollback.md`, `golive-checklist.md`, `martin-steps.md`, and each G action registered with `run_state.py request`. Wait.
- [ ] P6 Go-live: cleanup TEST data, reset test settings, each G action only after `go A<n>`, canary with readback. Phase `golive`.
- [ ] P7 Alerts (from alerts@741.studio to martin@741.studio only) and daily reconciliation on (G actions). `runbook-de.md` + `testprotokoll-de.md` at the client node. Client message draft (Ich-Form, du) for Martin. +24 h check. Phase `monitor`, then `done`. `run_state.py runjson --run <dir> --status "fertig, Freigabe offen"`.

## Click and tap protocol

1. API → MCP → Chrome DOM tools → coordinate clicks → computer use. Never the built-in browser.
2. Every click has an `action_summary` that names its real effect.
3. After each state change: read back and screenshot. Reload editors that cache before you trust a save.
4. Popups first (account chooser, LastPass, cookies). Locked screen or lost connection = stop and report.

## Output at each checkpoint

```
Run: <run_dir> · Phase: <phase>
Done since last checkpoint: <3 lines max, each with evidence file or record ID>
Waiting for: <go spec | go A3 (what it does, for whom, rollback) | Martin step M1>
Open: <only real blockers>
```

## References

- Rules, classes, layers, limits: `00_project/automation-workflow.md`
- Failure map with real 741 cases: `00_project/automation-failure-map.md`
- Hooks that enforce this skill: `00_project/automation-workflow/hooks/` (guard, done gate, go recorder)
