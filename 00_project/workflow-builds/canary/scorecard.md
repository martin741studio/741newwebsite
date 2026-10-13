# Scorecard — canary (2026-10-14)

Rubric: `00_project/knowledge/workflow-library/_derived/scorecard.md`. Ship at 80% with no 0 in section A or D.

## A. Fit
| # | Check | Score | Note |
|---|---|---|---|
| A1 | Block matches the job | 2 | Hybrid chosen with explicit reasoning against the decision tree (block-choice.md): routines/desktop tasks can't detect within 1 h, so detection is deterministic/off-laptop, agent does triage. |
| A2 | Always-on rules in CLAUDE.md, procedures in skill, enforcement in hooks | 1 | Procedures are in the skill (good). No hook enforces the hard limits (no Ads change, no client message) yet — they rely on the skill's Critical section + allowlist.py, not a PreToolUse hook like automation-build's. Noted as an open item, not built this round. |
| A3 | Side-effect skills have `disable-model-invocation: true` | 1 | Deliberately deviates: set to `false` after the trigger test proved `true` blocks natural-language incident response entirely, and after matching house precedent (night-shift-v2 = false). Side effects stay gated per-action (allowlist.py + Martin's go), not by blocking the skill's own invocation. Documented in trigger-tests.md and SKILL.md Critical. |
| A4 | Enabled on claude.ai or committed to repo | 2 | Project skill, committed to `.claude/skills/canary/`. |
**A: 6/8 = 75%**

## B. Design
| # | Check | Score | Note |
|---|---|---|---|
| B1 | 2–3 use cases with trigger/steps/tools/result | 2 | use-cases.md: UC1 add, UC2 incident, UC3 daily watch. |
| B2 | 3 test scenarios before the body | 2 | test-scenarios.md written before SKILL.md; T1–T5. |
| B3 | One hard task solved by hand, approach extracted | 2 | hand-run.md: Marcel's real outage, 2 live Zapier Manager Zaps built+tested, Tally-browser-unreadable finding fed into the design (R checks need API keys, never a browser session). |
| B4 | Inputs, deliverable, out-of-scope stated | 2 | SKILL.md frontmatter negative triggers + Critical; pipeline.md shows gates. |
| B5 | Degrees of freedom match fragility | 2 | freedom.md: scripts for checks/alerts/registry/allow-list, heuristics for diagnosis/catalogue picks. |
**B: 10/10 = 100%**

## C. SKILL.md quality
| # | Check | Score | Note |
|---|---|---|---|
| C1 | description WHAT+WHEN, trigger phrases, negative trigger | 2 | Confirmed by the trigger-test agent against T1–T4, 4/4. |
| C2 | kebab-case name, no reserved words/brackets | 2 | `canary`. |
| C3 | Body <500 lines, references one level deep | 2 | verify.py checks this automatically (currently ~95 lines); 4 reference files, no nesting. |
| C4 | Checklist Claude copies and ticks | 1 | 3 numbered mode-checklists exist, but they are not written as literal `- [ ]` copy-tick lists like night-shift-v2's. Functional/baseline tests show they were followed correctly anyway; cosmetic gap. |
| C5 | Deterministic steps are run scripts, no magic numbers | 2 | registry.py/alert.py/allowlist.py/verify.py; thresholds come from canaries.json, not hardcoded. |
| C6 | Output template + examples where style matters | 2 | incident-log.template.md, telegram alert templates in zapier-manager-setup.md, decision-card pattern reused from morning-grill. |
| C7 | One term per concept, no time-sensitive text, one default + escape hatch | 2 | "Open items" section isolates what's not built yet instead of mixing it into the steady-state instructions. |
| C8 | MCP tools fully qualified; dependencies listed | 2 | No MCP tools used directly (plain scripts + Telegram HTTP API); dependencies (.secrets file, canaries.json) named explicitly. |
**C: 15/16 = 94%**

## D. Verification
| # | Check | Score | Note |
|---|---|---|---|
| D1 | A check Claude can run | 2 | verify.py, 14 checks. |
| D2 | Loop: run → fix → repeat → "only proceed when it passes" | 2 | SKILL.md Verification section states this explicitly; actually exercised (disable-model-invocation bug found and fixed before re-verifying). |
| D3 | Unattended runs are gated | 2 | allowlist.py + Martin's go-cards gate every write; E-type pushes (the only unattended path live today) have no write capability at all. |
| D4 | Evidence demanded in the final report | 2 | Mode A step 8 requires pasting the `sent ...` line and Martin's confirmation; this build delivered 3 real Telegram sends, 1 confirmed receipt with a screenshot. |
| D5 | Trigger tests: obvious, paraphrase, unrelated does not trigger | 2 | 4/4 after the fix, independently re-verified. |
| D6 | Baseline comparison (tool calls, corrections, tokens) | 2 | baseline.md: -21% tokens, under half the tool calls, 0 vs 3 corrections. |
**D: 12/12 = 100%**

## E. Unattended and scheduled
| # | Check | Score | Note |
|---|---|---|---|
| E1 | Self-contained prompt, success stated, time zone | 2 | unattended-rules.md R6.6/R6.7; alert.py and templates use WITA explicitly. |
| E2 | Per-source bookmarks, not fixed windows | 1 | alerts.log is append-only with timestamps (a bookmark base exists), but no poller for S/R/A types exists yet to need real per-source bookmarks — applies fully only once the runner is built. |
| E3 | Failed reads reported as unreadable | 2 | Critical + Mode B step 2 + canaries.json's own reconciliation row models this live (status explicitly "BLOCKED... unreadable"). |
| E4 | Posts count as sent only after confirmation | 2 | alert.py logs SENT only on Telegram `ok:true`, ACK only on a received callback. |
| E5 | Read-only credentials, spend cap | 1 | Ads/Tally/Pipedrive are specified read-only by design and in the drafted Marcel message; no spend cap exists yet because no paid runner is live — applies fully once the Hetzner server or a paid tier exists. |
| E6 | Preferences re-read every run from an agent-can't-edit store | 1 | canaries.json is the preference store and is agent-writable via registry.py (by design, for Mode A) — not a hard separation like morning-grill's read-only vs read-write memory split. Noted as a gap to fix if abuse becomes a real risk. |
| E7 | Runs opened and read, not judged by green status | 2 | Mode C explicitly reads incident files, not just status flags; unattended-rules.md R6.10 applies the lesson to canary's own future routine runs. |
**E: 11/14 = 79%** (below 80 on its own, but E only fully matters once a scheduled unattended runner exists — today's only unattended path, the Zapier push, scores well on E1/E3/E4/E7)

## F. 741 house rules
| # | Check | Score | Note |
|---|---|---|---|
| F1 | Client message + Drive link where a client deliverable exists | 2 (N/A scored as met) | No client deliverable from a canary itself; the one client-facing text (Marcel key request) went through the German slop check (5/5) before hand-off. |
| F2 | Per-change go before any live website change | 2 | Critical states this; canaries never touch a website. |
| F3 | Every data point verified, no guesses | 2 | Zap history read live, pages curl-verified, Tally-unreadable reported as unreadable (not "0"). |
| F4 | STE in replies/artifacts | 2 | SKILL.md and references written in STE. |
| F5 | No method sources named; "741-…-Raster" | 2 | house-rules.md confirms no provider/vendor jargon leaks into anything client-facing. |
| F6 | Runs show up in the Excel overview automatically | 1 | `add-workflow` not yet run (step 5.3a, next). `_run.json` convention is designed (SKILL.md Mode A step 9) but not yet written for a real client run. |
| F7 | Martin guide where a client/prospect sees the deliverable | 2 (N/A scored as met) | No client/prospect ever sees canary output directly — alerts and registry are 741-internal. |
**F: 13/14 = 93%**

## Result
Total: 67/74 = **90.5%**. Blocking zeros in A or D: **none**.
Decision: **ship** (proceed to checkpoint 2), with two open follow-ups carried forward rather than blocking: A2 (a PreToolUse hook enforcing the hard limits, matching automation-build's pattern) and E2/E5/E6 (fully apply once a scheduled runner and read-only API keys exist — today's only unattended path, the Zapier push, is already compliant).
