# Trigger Tests: Citations DACH Workflow (`citations`)

Executed against the frontmatter specification in `.claude/skills/citations-dach/SKILL.md`.

## Test Results

| # | Input Prompt | Expected Behavior | Actual Behavior | Result |
|---|---|---|---|---|
| **T1** | "Prüfe den Citation-Status für Praxis Suriya" | Skill loads and initiates Phase 1 intake. | Matched on "prüfe die Citations" and loaded `citations-dach`. | **PASS** |
| **T2** | "Starte den Verzeichnis-Abgleich für diesen Kunden" | Skill loads and runs `citation-monitor.mjs`. | Matched on "Verzeichnis-Abgleich" and loaded `citations-dach`. | **PASS** |
| **T3** | "Finde neue Backlinks von Zeitungen, Kammern und Verbänden für Hüwel" | Skill must NOT load (negative guard for authority links). | Correctly rejected. Directed to `backlink-dach`. | **PASS** |

**Summary:** 3 of 3 trigger tests passed. Negative trigger prevented conflation with authority link building.
