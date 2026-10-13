# 4.3 Baseline — with vs without the canary skill (2026-10-14)

Same task, same incident text, two fresh sessions. "Without" was told not to look at the canary build at all.

| | Without skill (baseline agent) | With skill (functional test, after fix) |
|---|---|---|
| Tool calls | ~17–18 (repo-wide grep/find, read 5+ files, write its own note) | 8 (Skill tool, registry.py, runbooks.md, allowlist.py ×3, verify.py) |
| Tokens | 143,191 | 112,370 (–21%) |
| Course corrections | 3 (switched hypothesis after finding another chat's retro-check; raised confidence after a second source; found but deliberately avoided the canary folder) | 0 (direct path: registry → runbook → allowlist → stop) |
| Severity | Guessed ("high", invented from business impact — no scale existed) | Read from the registry row (SEV2, pre-set by the design) |
| Escalation channel/recipient | Guessed (unclear mail vs chat vs portal; drafted but did not send) | Defined (Telegram, Martin → Dinakar after 10 min; alert.py ready, correctly not invoked for a fictional incident) |
| Self-heal vs escalate | Inferred from automation-workflow.md's class table (reasonable, but had to derive it) | Looked up directly: `allowlist.py check <id>` |
| Incident note | Improvised its own template at a path it chose itself | Used `assets/incident-log.template.md` (not exercised in this dry run, but exists and is named in SKILL.md step 7) |
| What it wanted | "a fixed severity scale; a named escalation channel; explicit self-heal-allowed actions; a standard incident note template" (agent's own words) | All four already exist in the skill |

Result: the skill cuts tool calls by more than half, tokens by about a fifth, and removes all 3 course corrections — by replacing four separate judgment calls (severity, channel, self-heal-or-not, note format) with lookups in a registry/runbook/allow-list built once. The baseline agent independently asked for exactly the four things the skill provides.
