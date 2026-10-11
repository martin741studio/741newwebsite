# Automation Build workflow — design note (checkpoint 1)

Status 2026-10-11: grilling done (5 rounds). Waiting for Martin's design "go". Nothing installed. No client system touched.

## 1. Research note

- Building block: skill `/automation-build` (`disable-model-invocation: true`, side effects) + 3 hooks for enforcement + scripts for the fragile steps + a fresh verifier subagent. Reason: prose rules failed in real runs (failure map F1–F15); rules R0.5 and R2.10 say "must happen every time" = hook, "side effects" = slash command only.
- Rules used: R0.5 (hooks, not CLAUDE.md, for zero-exception steps) · R4.2/R4.5 (gate the stop, fresh reviewer) · R6.2/R6.3 (failed read is "unreadable", count a send only after confirmation) · R1.8 (plan-validate-execute for writes).
- Pattern: 4.4 plan-validate-execute + 4.6 writer/reviewer + 4.8 "confirm before ledger".
- Hook facts checked in the docs (2026-10-11): PreToolUse `deny` blocks in every permission mode, also in bypass mode. Stop hooks get `last_assistant_message` and `stop_hook_active`. UserPromptSubmit gets `prompt` and also fires on messages from other sessions and on scheduled turns. Chrome clicks carry an `action_summary`.

## 2. Decisions from the grilling

| Topic | Decision |
|---|---|
| Pain | All four clusters: fake done, live damage, silent breakage, wrong facts |
| Scope | CRM/email funnels (Zapier, KlickTipp, Pipedrive, HubSpot, Skool), browser click work in client tools, AI agents and n8n. Supabase backends are in scope as a building part |
| Test environment | TEST records in the live tool, 741 test inbox, flow stays draft/off, cleanup step deletes test data |
| Owner after go-live | 741 monitors (retainer). Client gets a runbook |
| Go class G (hook blocks until "go") | Messages to real people · switch on / publish (Zap ON, cron or LaunchAgent load, live flag true, deploy, publish) |
| Martin-only class M (hook always blocks) | Money and prices · delete · bulk updates · permissions (invites, API keys, OAuth grants). Agent prepares the steps, Martin clicks |
| Free zone | Reads, and writes to records marked TEST or to drafts that are off |
| Click work | Agent works alone, reads back every step, stops at every G or M action |
| Evidence | Readback after every write (DOM or API) + screenshot at each state change, in `evidence/` per run |
| Mandatory tests | Always: end-to-end with a TEST record, every field read back in every target. When the flow messages people or writes CRM/email records: also error paths, run-twice (no duplicates), alert test |
| Verifier | Fresh verifier subagent tries to refute, then Martin sees the evidence at the go-live gate |
| Done gate | Scoped Stop hook: blocks "done" while the test report is missing or failing |
| Alerts | Email from `alerts@741.studio` (Resend) to martin@741.studio only. Never to clients. Human mails stay on Airmailer |
| Canary | First real record end-to-end with readback, then one more check after 24 h |
| Handover | German runbook + client-safe test protocol (portal page at the client node) |
| Secrets | Martin enters keys (.secrets/.env or tool connection). Agent reads env vars only, never types or prints a secret |
| Trigger | `/automation-build <client> <automation>` |
| Dry run | Marcel Skool → Zapier → KlickTipp + Pipedrive, test mode only |

## 3. Use cases

1. `/automation-build Marcel Skool funnel` — inventory Skool, Zapier, KlickTipp, Pipedrive (read) → spec → TEST member → Zap in draft → E2E + run-twice + error tests → verifier → Martin's go per action (Zap ON) → canary → runbook.
2. `/automation-build Stürzl lead intake` — form → edge function `lead-intake` → portal `leads` → alert. Built on staging, deploy is class G.
3. `/automation-build 741 phone agent` — Twilio → ElevenLabs → n8n → Supabase. Accounts are Martin's (class M setup steps listed for him); build and test with a TEST call.

## 4. Pipeline with checkpoints

```
P0 Intake + full inventory (read only, every list opened, no "missing" without a second check)
P1 Spec (L0): trigger, systems, field map, error paths, action list with classes, test list, owner, alert, rollback idea
   ── CHECKPOINT A: Martin approves the spec ("go spec")
P2 Environment (L1, L3): preflight (account, from-address, project ID, test inbox), TEST records, flow off, snapshot of configs
P3 Build (L4): draft/off only, one change at a time, readback + evidence + change-log line per change
P4 Test (L5): run the test plan, write test-report.json with evidence paths
P5 Verify: fresh verifier subagent re-checks and tries to refute; check_report.py must pass
   ── CHECKPOINT B: Martin sees evidence, go-live checklist, rollback plan, list of G actions
P6 Go-live (L6): cleanup TEST data, reset test settings, each G action only after "go A<n>", canary record, +24 h check
P7 Monitor + handover: platform error alerts → martin@741.studio, daily reconciliation check (source count vs target count), German runbook, test protocol, client message draft (Ich-Form, du)
```

## 5. Enforcement (hook drafts, not installed)

Scope: the hooks act only in sessions that started `/automation-build`. Other chats see no change.

| Hook | Event | Job |
|---|---|---|
| `automation_session.py` | UserPromptSubmit | Registers the session when the prompt starts with `/automation-build`. Records "go A<n>" only when Martin's prompt is exactly that text (rejects text from other sessions and scheduled turns) |
| `automation_guard.py` | PreToolUse | Classifies each tool call. Class M → deny ("Martin does this"). Class G → deny unless an unused go token for this action exists. Writes with a secret pattern into normal files → deny. Edits to the go ledger by the agent → deny. Free zone → no output |
| `automation_done_gate.py` | Stop | When the last message says done/fertig/live or the run phase is past "test", run `check_report.py`. Missing or failing report → block with the reason. Uses `stop_hook_active` against loops |

How a go works: the agent runs `run_state.py request --kind send --target "Zap 378535838 ON"`. The script gives action ID `A3`. The agent shows the full action to Martin. Martin types `go A3`. The prompt hook writes the token. The guard lets exactly one matching call through and marks the token used.

Limits (stated honestly): the guard reads tool names and inputs. It cannot see what a generic `javascript_tool` script does in a page. So `javascript_tool` calls that click or POST in an automation session always need a go. A determined agent could still bypass a hook with odd Bash. The hooks stop mistakes, not attacks.

## 6. Run folder

`00_project/assets/<client>/automation/<slug>/` (the registry `sync` scans only `00_project/assets/`) with `state.json` (phase, actions, go ledger), `_run.json` (registry), `spec.md`, `test-plan.md`, `test-report.json` + `.md`, `changelog.md`, `snapshots/`, `evidence/`, `rollback.md`, `golive-checklist.md`, `runbook-de.md`, `testprotokoll-de.md`.

## 7. Test scenarios for the skill

1. Obvious: "/automation-build Marcel Skool funnel" → skill loads, P0 inventory starts, no write.
2. Paraphrase: "Bau die Zapier-Strecke Skool zu KlickTipp für Marcel, mit Tests" → skill is suggested; Martin starts it with the slash command (model invocation is off by design).
3. Must not trigger: "Schreib Marcel eine WhatsApp, dass die Strecke steht" → no skill; normal message draft.

## 8. Success measures

0 "done" claims without a passing report · 0 sends or publishes without a go token · 0 test records left after go-live · every live automation has an alert path and a runbook · time from spec go to tested build is logged per run.

## 9. Open points (not blocking the design)

- Hook install place: `~/.claude/settings.json` (all projects) or `741website/.claude/settings.json`. Proposal: user settings, because client work also runs in other folders (`~/huewel-site`).
- Daily reconciliation check runs on the Mac (LaunchAgent 08:00, before the standup). The Mac must be awake. Cloud option later.
- `alerts@741.studio` needs no new DNS (domain 741.studio is verified in Resend). First alert test needs Martin's go.
- Smartlead API key in a memory file (F13): move to `.secrets/` after Martin's go.
