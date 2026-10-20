# 741 Automation Build workflow (`/automation-build`)

Version 1 · 2026-10-11 · design approved by Martin (checkpoint 1) · skill and hooks NOT installed yet.

Purpose: build automations for clients and for 741 so that they really work. The workflow stops the four failure clusters from the failure map: fake done, live damage, silent breakage, wrong facts (`00_project/automation-failure-map.md`).

Scope: CRM and email funnels (Zapier, Make, KlickTipp, Pipedrive, HubSpot, Skool, forms), browser click work in client tools without an API, AI agents and n8n flows, and the Supabase parts (edge functions, crons, webhooks) these need.

Not in scope: website content and page builds (use `cro-homepage`, `seo-page-optimizer`), review pages, one-off data pulls without a write.

## Table of contents

1. Hard rules
2. Action classes and approvals
3. Safety layers L0–L6
4. Phases and checkpoints
5. Click and tap protocol
6. Test gate
7. Go-live, monitoring, handover
8. Credentials policy
9. Caps
10. Done criteria
11. Enforcement (hooks) and limits
12. Files and templates

## 1. Hard rules

1. No build before Martin approves the spec. He types `go spec`.
2. No message to real people and no switch-on or publish without Martin's `go A<n>` for exactly that action. One go covers one action.
3. Money, prices, delete, bulk updates and permissions: the agent never does them. It writes the steps into `martin-steps.md` and Martin clicks.
4. Every write is read back from the target system (API or DOM) and recorded with evidence. A click or an HTTP 200 is not proof.
5. "Done", "fertig", "läuft" and "live" are said only when `check_report.py` passes.
6. A failed read is "unreadable", never "nothing there". Every "missing" claim gets a second, full check.
7. Secrets stay in `.secrets/` or `.env`. The agent never prints, types or copies a secret value.

## 2. Action classes and approvals

| Class | What | Who | Enforced by |
|---|---|---|---|
| read | Reads, screenshots, inventory | agent, free | — |
| test_write | Writes on records with the marker `TEST-741`, drafts that are off, mails to a 741 test inbox (`martin@741.studio`, `test…@741.studio`, `*.test`) | agent, free, logged | guard logs it |
| G | Messages to real people (email, SMS, WhatsApp, DM, sequence start, calendar invite). Switch on or publish (Zap ON, scenario ON, cron, LaunchAgent, live flag true, deploy, git push, FTP upload, DNS). Any write on live data without `TEST-741` | agent, after Martin's `go A<n>` | guard denies until a matching go token exists |
| M | Money, payments, prices, plans, refunds. Delete or remove on live data. Bulk updates. Invites, roles, API keys, OAuth grants, sharing | Martin only | guard always denies |

How a go works:

1. The agent registers the action: `run_state.py request --run <dir> --kind send|publish|write --tool <tool regex> --contains <exact text in the call> --target "<what happens, for whom>"`. The script returns `A<n>`.
2. The agent shows Martin the full action (system, object ID, what changes, who is affected, rollback).
3. Martin types exactly `go A<n>` (several: `go A3 A4`).
4. The prompt hook records the token. The guard lets exactly the matching call through, once (or `--uses N` times).

## 3. Safety layers L0–L6

| Layer | Rule | Proof |
|---|---|---|
| L0 Spec | Spec with trigger, systems, account IDs, field map, error paths, action list with classes, test list, owner, alert path, rollback idea. Built from a full inventory | `spec.md`, `go spec` |
| L1 Environment | Preflight before the first write: right account (shown e-mail or account ID), right from-address, right project ID, test inbox. TEST records carry `TEST-741` in a name field. The flow stays draft or off. A live switch exists where the platform has one (Zap OFF, campaign inactive, `live_send_enabled=false`) | `evidence/preflight.md` |
| L2 Action classes | Section 2. Hook-enforced | `state.json` actions |
| L3 Snapshot and rollback | Before each write: export the affected config or record (JSON, screenshot of the settings). One `changelog.md` line per change. Rollback steps written before checkpoint B | `snapshots/`, `changelog.md`, `rollback.md` |
| L4 Readback | After each write: read the state back and compare with the expected state. Never chain UI steps blind | `evidence/` per step |
| L5 Test gate | Test plan, test run with TEST data, test report, fresh verifier | `test-report.json`, `check_report.py` |
| L6 Go-live | Martin's go per action, cleanup, canary, alerts, daily reconciliation, runbook | `golive-checklist.md`, `runbook-de.md` |

## 4. Phases and checkpoints

Copy this checklist into the reply and tick it off.

- [ ] **P0 Intake and inventory** (read only). Bind the run: `run_state.py init --session <id> --client "<name>" --slug <slug>`. Open every relevant list in full (all pipelines, all tags, all Zaps, all fields). Read the client's docs fully before any question. Write `inventory.md` with IDs.
- [ ] **P1 Spec.** Fill `templates/automation-spec-de.md` (client language) into `spec.md`. Phase `spec`.
- [ ] **CHECKPOINT A.** Show Martin the spec. Wait for `go spec`.
- [ ] **P2 Environment.** Preflight (L1). Create TEST records. Snapshot configs (L3). Phase `environment`.
- [ ] **P3 Build.** Draft or off only. One change at a time: snapshot → change → readback → evidence → `run_state.py log`. Phase `build`.
- [ ] **P4 Test.** Run `test-plan.md`. Write `test-report.json` (template). Phase `test`.
- [ ] **P5 Verify.** Start a fresh verifier subagent with `templates/verifier-prompt.md`. It re-reads every target system and tries to refute the report. Fix and re-test until it says pass. Run `check_report.py <run_dir>` until PASS. Phase `verify`.
- [ ] **CHECKPOINT B.** Show Martin: test report summary, evidence folder, `rollback.md`, `golive-checklist.md`, the list of G actions with IDs, `martin-steps.md`. Wait.
- [ ] **P6 Go-live.** Cleanup TEST records (TEST deletes are free). Reset test settings. Each G action after its `go A<n>`. Canary: first real record end-to-end with readback. Phase `golive`.
- [ ] **P7 Monitor and handover.** Alerts on, reconciliation check on (both are G actions). 24 h canary check. `runbook-de.md`, `testprotokoll-de.md` as a portal page at the client node. Client message draft (Ich-Form, du) for Martin. Phase `monitor`, then `done` after the 24 h check.

Registry: `run_state.py` writes `_run.json` in the run folder. The Stop hook of the registry syncs the Excel. Approval stays manual.

## 5. Click and tap protocol

1. Tool order: API → MCP → Chrome DOM tools (`read_page`, `find`, `form_input`) → coordinate clicks → computer use. Use Claude in Chrome, never the built-in browser.
2. Before the first click on a page: screenshot, close popups (account chooser, cookie banner, LastPass overlay), check the logged-in account.
3. Every click carries an `action_summary` that names the real effect ("Publishes Zap 378535838"). The guard judges clicks by it.
4. After every state change: read the state back (`read_page`, `get_page_text` or an API read) and take a screenshot into `evidence/`. Compare with the expected state. If it differs: stop, record, fix. Never continue blind.
5. Saved is only what the system shows after a reload. Reload and read again for editors that cache (KlickTipp CKEditor, ONLY INSIDE modules, Zapier fields).
6. Record stable selectors and working tricks in `inventory.md` (for example the Zapier picker: search the value, wait until the leaf is solid, then click).
7. A locked screen or a lost Chrome connection stops the run. Write the plan file and report.

## 6. Test gate

Mandatory for every automation:

- **e2e**: a TEST record goes from the trigger to the last system. Every mapped field is read back in every target system. Record IDs are in the report.

Mandatory when the flow messages people or writes CRM or email records (`flow_class` `messages` or `crm`):

- **error**: empty field, bad format, missing required value, auth failure. Each gives a clear error or an alert, never a silent loss.
- **idempotency**: the same trigger twice gives no duplicate contact, deal, tag or mail.
- **alert**: one forced failure, and the alert mail reaches martin@741.studio.

Optional: role tests (admin, client, anon) for Supabase parts; rate limit; auth expiry.

The fresh verifier subagent gets no build context. It reads the spec, the report and the target systems, and it tries to refute each pass. It reports only correctness gaps. `check_report.py` checks: report exists, e2e with readback, mandatory types passed, no fail, every evidence file exists, verifier pass after the last case.

## 7. Go-live, monitoring, handover

- Cleanup: delete TEST-741 records, cancel test memberships (Martin, class M if it touches money), reset test prices or settings, restore placeholder texts. Each line in `golive-checklist.md` is ticked with evidence.
- Canary: first real record end-to-end with readback. Check again after 24 h (`ScheduleWakeup` or a note in the daily standup).
- Alerts: platform error alerts go to martin@741.studio (Zapier error notifications, n8n error workflow). Automated alert mails come from `alerts@741.studio` via Resend, only to martin@741.studio, never to clients. Human mails stay on Airmailer.
- Daily reconciliation: count source events vs. target records for the last day (for example Skool new members vs. KlickTipp contacts with the tag vs. Pipedrive deals). Mismatch = alert. Runs before the 08:05 standup. A failed read = alert "unreadable".
- Owner after go-live: 741 monitors as part of the retainer.
- Handover to the client: German runbook and client-safe test protocol (no team names, no method sources), as a portal page at the client node. Message draft in Ich-Form with "du". Martin sends after his go.

## 8. Credentials policy

- The client grants access through LastPass or a portal access grant. Martin enters keys into `.secrets/` or `.env`, or connects the tool (OAuth in Zapier, Make, n8n).
- The agent reads environment variables. It never prints them (`cat .env`, `echo $TOKEN` are blocked), never types them into web forms, never writes them into normal files or memory.
- The agent never creates accounts, never accepts terms, never solves CAPTCHAs, never enters payment data.
- Read-only credentials where the automation only reads (rule R6.5).
- A secret found in a normal file is reported to Martin and moved after his go.

## 9. Caps

- Max 3 fix attempts per failing test case, then stop and report the blocker.
- Max 2 h of unattended click work per session, then report.
- Paid API calls (Apify, DataForSEO) per run: cap stated in the spec; default 5 EUR.
- No unattended G actions. No night-shift runs of this workflow.

## 10. Done criteria

The run is done when all hold:

1. `check_report.py` passes.
2. Every G action in `state.json` is `used` or withdrawn, and each had Martin's go.
3. `golive-checklist.md` is complete with evidence, including the TEST cleanup.
4. The canary record and the 24 h check passed.
5. The alert path and the reconciliation check were tested once.
6. `runbook-de.md` and `testprotokoll-de.md` exist; the client message draft is ready for Martin.
7. `_run.json` status is "fertig, Freigabe offen".

## 11. Enforcement (hooks) and limits

Drafts in `00_project/automation-workflow/hooks/`. Tests: `python3 00_project/automation-workflow/tests/test_hooks.py` (93 cases, sandbox only). Install snippet: `00_project/automation-workflow/settings-snippet.json` (target `~/.claude/settings.json`, only after Martin's install go).

| Hook | Event | Effect |
|---|---|---|
| `automation_session.py` | UserPromptExpansion, UserPromptSubmit | Registers `/automation-build` sessions. Records `go spec` and `go A<n>` only when the whole prompt is that text |
| `automation_guard.py` | PreToolUse | Classifies each call (read, test_write, G, M, secret, ledger) and denies G without a token, M always, secrets and ledger edits always |
| `automation_done_gate.py` | Stop | Blocks done claims while `check_report.py` fails |

State: `~/.claude/automation-runs/` (sessions, requests, ledger, activity). Run folders: `00_project/assets/<client>/automation/<slug>/`.

Limits (known, accepted):
- The guard judges calls by tool name, inputs and the click `action_summary`. A click with a harmless summary that really publishes something is not caught. The readback rule and the verifier cover this.
- Every `javascript_tool` call that clicks, posts or sets values is class G. Pure reads are free.
- A plain UI click on a live record field and "Save" (no TEST marker in the summary) is test_write. The guard cannot see which record the page shows.
- A determined agent can bypass a hook with unusual shell code. The hooks stop mistakes, not attacks.
- Messages from other sessions cannot grant a go. A scheduled turn cannot grant a go.

## 12. Files and templates

Templates in `00_project/automation-workflow/templates/`:

| File | Use |
|---|---|
| `automation-spec-de.md` / `automation-spec-en.md` | spec (L0) |
| `test-plan.md` | test cases per type |
| `test-report.example.json` | report format that `check_report.py` reads |
| `golive-checklist.md` | P6 |
| `rollback-plan.md` | L3 |
| `runbook-de.md` | client handover |
| `testprotokoll-de.md` | client-safe test protocol |
| `verifier-prompt.md` | fresh verifier subagent |
| `martin-steps.md` | class M steps for Martin |

Run folder: `state.json`, `_run.json`, `inventory.md`, `spec.md`, `test-plan.md`, `test-report.json`, `changelog.md`, `snapshots/`, `evidence/`, `rollback.md`, `golive-checklist.md`, `martin-steps.md`, `runbook-de.md`, `testprotokoll-de.md`.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: in the client runbook and handover: present at the data flow, think at the steps the client must do. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
