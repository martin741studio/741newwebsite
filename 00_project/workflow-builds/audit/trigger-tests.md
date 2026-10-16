# Trigger Tests: Maps Audit Workflow (`audit`)

Executed against the frontmatter specification in `.claude/skills/maps-audit/SKILL.md`.

## Test Results

| # | Input Prompt | Expected Behavior | Actual Behavior | Result |
|---|---|---|---|---|
| **T1** | "Starte den Maps-Audit für Praxis Suriya" | Skill loads and initializes Phase 1 checklist. | Skill matched on "starte den Maps-Audit" and initialized run. | **PASS** |
| **T2** | "Führe die Maps-Readiness Analyse für diesen Kunden durch" | Skill loads and prepares data collection checklist. | Skill matched on "Maps-Readiness prüfen" and prepared intake. | **PASS** |
| **T3** | "Mach einen neuen Google Maps Ranking Scan für Hüwel" | Skill must NOT load (negative guard for single scans). | Rejected. Skill did not load; redirected to ranking tracking scan. | **PASS** |

**Summary:** 3 of 3 trigger tests passed. Negative trigger successfully prevented unintended invocation for single ranking checks.
