# Scorecard — booking-sequence (2026-10-14)

Rubric: `00_project/knowledge/workflow-library/_derived/scorecard.md`. Ship at 80 % with no 0 in section A or D.

## A. Fit
| # | Check | Score | Note |
|---|---|---|---|
| A1 | Block matches the job | 2 | Project skill (Martin pastes a booking) + one-time Desktop tasks for the 2 time-bound reminders (block-choice.md). |
| A2 | Always-on rules in CLAUDE.md, procedures in skill, enforcement in hooks | 1 | Procedure in the skill, hard rules enforced by check_sequence.py (script gate, not a hook). No hook needed: the skill never sends, and the file is written only on PASS. |
| A3 | Side-effect skills have `disable-model-invocation: true` | 1 | Deliberately false: the trigger is a pasted booking without a slash command (same reason as canary/local-seo-review-page). Side effects are small (≤ 0,30 USD, 2 reminders), nothing is ever sent. |
| A4 | Enabled on claude.ai or committed to repo | 2 | Project skill `.claude/skills/booking-sequence/`, committed. |
**A: 6/8**

## B. Design
| # | Check | Score | Note |
|---|---|---|---|
| B1 | Use cases | 2 | UC1 booking, UC2 late / no page, UC3 moved / cancelled. |
| B2 | 3 test scenarios before the body | 2 | test-scenarios.md T1–T5 written before SKILL.md. |
| B3 | One hard task by hand | 2 | Korinna 14.10. (hand-run.md); context gaps became scripts (time zones, ledger dir, late guard). |
| B4 | Inputs, deliverable, out-of-scope | 2 | SKILL Inputs + Output + negative triggers. |
| B5 | Freedom matches fragility | 2 | 5 scripts for times / find / site facts / rules / reminders; heuristics for insight and case pick. |
**B: 10/10**

## C. SKILL.md quality
| # | Check | Score | Note |
|---|---|---|---|
| C1 | description WHAT + WHEN + NOT | 2 | 4/4 trigger tests. |
| C2 | name | 2 | `booking-sequence`. |
| C3 | < 500 lines, refs one level | 2 | ~125 lines, 2 references + 2 assets, none > 100 lines. |
| C4 | Copy-tick checklist | 2 | 8-step `- [ ]` checklist. |
| C5 | Deterministic steps are run scripts | 2 | tz_times, find_prospect, quick_check, check_sequence, reminders; constants named at the top. |
| C6 | Template + examples | 2 | message-templates.md shape + full Korinna example + variants (no change, late booking); reminder-prompt template. |
| C7 | One term per concept, no time-sensitive text | 2 | m1/m2/m3, "booking folder", "claim"; Martin's dated decisions only as rule sources. |
| C8 | MCP tools fully qualified; dependencies | 2 | `mcp__scheduled-tasks__create_scheduled_task` / `list_` / `update_`; dfs.py, deslop_de.py, case-library.json named. |
**C: 16/16**

## D. Verification
| # | Check | Score | Note |
|---|---|---|---|
| D1 | A check Claude can run | 2 | check_sequence.py (rules + slop + claims), tz/reminder fireAt compare. |
| D2 | Loop to PASS | 2 | Step 6 + Verification; exercised in the functional test (2 FAIL → rewrite → PASS). |
| D3 | Unattended runs gated | 2 | Reminder prompt: never send, too-late stop, missing-file stop, never write a message; tested live (5.4). |
| D4 | Evidence in the final report | 2 | Step 8 + Verification: check line, file times, fireAt_utc. |
| D5 | Trigger tests | 2 | 4/4 (trigger-tests.md). |
| D6 | Baseline | 2 | baseline.md: same speed/tokens, but the baseline missed 2 of Martin's asks + used an unclear case fact; skill met all. |
**D: 12/12**

## E. Unattended and scheduled (the 2 reminders)
| # | Check | Score | Note |
|---|---|---|---|
| E1 | Self-contained, success + time zone | 2 | UTC + prospect zone + WITA in the prompt; `date -u` first. |
| E2 | Bookmarks | 2 (N/A as met) | One-time task, no source stream. |
| E3 | Failed reads = unreadable | 2 | Missing file/section → "not available, nothing to send". |
| E4 | Sent only after confirmation | 2 (N/A as met) | Nothing is sent by a task; Martin sends. |
| E5 | Read-only, spend cap | 2 | Task reads one file; booking run cap 0,30 USD in dfs.py. |
| E6 | Preferences re-read, not agent-editable | 1 | The task reads whatsapp-sequence.md at fire time (so edits are picked up), but the file is agent-writable. |
| E7 | Runs opened and read | 2 | 5.4: both test runs opened and read (late + on time). |
**E: 13/14**

## F. 741 house rules
| # | Check | Score | Note |
|---|---|---|---|
| F1 | Client message + Drive link | 2 | The deliverable IS the message, ready in ```text blocks; no document for the prospect, so no Drive link. |
| F2 | Go before live website change | 2 (N/A as met) | No website change. |
| F3 | Every data point verified | 2 | claims.json with source per number, "quote" for facts without numbers, checked by script. |
| F4 | STE in replies | 2 | Step 8 + reminder prompt. |
| F5 | No method sources / tool names | 2 | TOOLS regex in the check. |
| F6 | Runs in the Excel by themselves | 2 | `booking/_run.json` written by `check_sequence.py --write`; add-workflow at install (5.3a). |
| F7 | Martin guide where a prospect sees output | 2 (N/A as met) | Plain WhatsApp text, no visual deliverable. |
**F: 14/14**

## Result
Total: 71/74 → **95,9 %**. Blocking zeros: 0.
Decision: ship (checkpoint 2), open follow-up: none blocking. Watch item: SERP "Platz" claims for local terms must be measured from the town (insight-menu §3), check this in the first 3 real runs.
