# 2.5 Degrees of freedom per step (rule R1.7) — canary

| Step | Fragile? | Freedom | Form |
|---|---|---|---|
| Run a check (HTTP, keyword, state, counts) | yes — must be exact, fast, cheap | LOW | `scripts/run_checks.py` (no LLM), reads `canaries.json` |
| Confirm failure (2 consecutive, recovery period) | yes | LOW | inside run_checks.py, state in `state/results.json` |
| Send alert + ack button + escalation timer | yes | LOW | `scripts/alert.py` (Telegram API) |
| Registry row add / change | yes (schema) | LOW | `scripts/registry.py add|validate|list` |
| Decide if a fix is allowed | yes — safety | LOW | `scripts/allowlist.py check <action>` = allow-list in `references/allowlist.md` |
| Execute an allowed fix | medium | LOW–MEDIUM | runbook per system type in `references/runbooks.md`, one attempt |
| Diagnose an incident (read run history, error text) | no — many valid paths | HIGH | heuristics in SKILL.md + runbooks |
| Pick checks for a new system (add mode) | no | MEDIUM | catalogue table L/S/E/R/A in `references/check-catalogue.md` |
| Write the decision card / incident log | medium (format) | MEDIUM | templates in `assets/` |
| Post-incident note + new check | no | HIGH | template + "every outage becomes a canary" rule |
