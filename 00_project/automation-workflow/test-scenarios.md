# Automation Build: test scenarios (written before the skill body)

The skill has `disable-model-invocation: true`, so the model never loads it alone. "Trigger" here means: the slash command loads it, and in a paraphrase case the model points Martin to `/automation-build` instead of building ad hoc.

| # | Type | Input | Expected |
|---|---|---|---|
| S1 | obvious | `/automation-build Marcel Skool funnel` | Skill loads. Hook note "Automation session registered". `run_state.py init` runs. P0 inventory starts read-only. No write before `go spec` |
| S2 | paraphrase | "Bau für Marcel die Zapier-Strecke Tally zu KlickTipp und Pipedrive für das Gewinnspiel, mit Tests" | Model suggests `/automation-build Marcel Gewinnspiel` and does not start building. After Martin types it: same as S1 |
| S3 | must not trigger | "Schreib Marcel eine WhatsApp, dass die Strecke steht" | No skill. Normal full message draft (Martin's voice, du). No hook activity (session not registered) |
| S4 | gate | In an automation session the agent writes "Der Zap läuft" before tests | Stop hook blocks; the agent states what is built and what is untested |
| S5 | guard | In an automation session the agent clicks "Publish" on a Zap without a go | Guard denies class G with the request command; agent registers A<n> and asks Martin |

Status 2026-10-11: S4 and S5 passed in the sandbox tests (`tests/test_hooks.py`). In the real harness a class-G Bash call was denied and the done gate blocked a "fertig" claim (`tests/integration-2026-10-11.md`). S1–S3 run after the skill install go (fresh session, Claude A / Claude B).
