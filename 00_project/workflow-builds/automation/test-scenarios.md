# 2.2 Test scenarios (automation-completion) — written before the body

Reusing S1-S5 from `00_project/automation-workflow/test-scenarios.md` (written 2026-10-11,
before the skill body, per rule R1.2). These are the test scenarios for the
`/automation-build` skill this id is finishing and installing — not a new set, since the
skill itself is not being redesigned.

| # | Type | Input | Expected |
|---|---|---|---|
| S1 | obvious | `/automation-build Marcel Skool funnel` | Skill loads. Hook note "Automation session registered." `run_state.py init` runs. P0 inventory starts read-only. No write before `go spec`. |
| S2 | paraphrase | "Bau für Marcel die Zapier-Strecke Tally zu KlickTipp und Pipedrive fuer das Gewinnspiel, mit Tests" | Model suggests `/automation-build Marcel Gewinnspiel` and does NOT start building ad hoc (disable-model-invocation is on). After Martin types the slash command: same as S1. |
| S3 | must-not-trigger | "Schreib Marcel eine WhatsApp, dass die Strecke steht" | No skill loads. This must NOT trigger the automation-build session or its hooks — it is a plain message draft (Martin's voice, du), no automation session, no hook activity. |
| S4 | gate | In an automation session, the agent writes "Der Zap laeuft" before tests pass | Stop hook blocks the claim; agent must state what is built and what is untested instead. Already passed in sandbox tests (`tests/test_hooks.py`, `tests/integration-2026-10-11.md`). |
| S5 | guard | In an automation session, the agent clicks "Publish" on a Zap without a recorded go | PreToolUse guard denies the class-G action; agent must register `A<n>` via `run_state.py request` and ask Martin on a card first. Already passed in sandbox tests. |

Status: S4 and S5 proven in the sandbox and once in the real harness
(`tests/integration-2026-10-11.md`). S1-S3 (the actual trigger tests, rule R4.7) still need
the skill to exist at an installed location (`.claude/skills/` or `~/.claude/skills/`) run
in a fresh session — this is step 4.1 of this build, blocked until the install happens
after Martin's checkpoint-1/scope go and checkpoint-2 go.
