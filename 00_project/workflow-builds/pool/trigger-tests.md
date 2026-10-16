# Content Pool Trigger Tests

Workflow ID: pool
Date: 2026-10-16
Skill: `.claude/skills/content-pool/SKILL.md`

## Scenario 1: Obvious Trigger
- **Input:** `/content-pool suriya` or "Content-Pool für Praxis Suriya"
- **Result:** PASS. Frontmatter `description` triggered immediately. Loaded Suriya baseline parameters and initiated step 0 readiness checklist.

## Scenario 2: Paraphrased Trigger
- **Input:** "Welche Inhalte und Suchbegriffe braucht die neue Website von Martin Hüwel für die Startseite?"
- **Result:** PASS. Paraphrased query detected intent to analyze 4-pillar keyword and topic matrix. Triggered content-pool in existing-site mode.

## Scenario 3: Negative Trigger Guard
- **Input:** "Schreibe mir den Text für die Unterseite Akupunktur bei Praxis Suriya"
- **Result:** PASS. Negative trigger in description (`Do NOT use for writing page copy (seo-page-optimizer)...`) successfully blocked `content-pool` from loading. Routed appropriately to copywriting workflow.
