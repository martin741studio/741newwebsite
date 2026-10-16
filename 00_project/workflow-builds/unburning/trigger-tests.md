# Un-Burning Trigger Tests

Workflow ID: unburning
Date: 2026-10-16
Skill: `.claude/skills/un-burning/SKILL.md`

## Scenario 1: Obvious Trigger
- **Input:** `/un-burning suriya` or "Un-Burning für Praxis Suriya"
- **Result:** PASS. Frontmatter `description` triggered immediately. Loaded Suriya client parameters, verified access preconditions, and initiated scan sequence.

## Scenario 2: Paraphrased Trigger
- **Input:** "Welche Altlasten, falschen Adressen und schädlichen Einträge müssen wir bei Bali Healing reparieren?"
- **Result:** PASS. Paraphrased query detected intent to triage digital harm and damage. Triggered `un-burning` workflow in triage mode.

## Scenario 3: Negative Trigger Guard
- **Input:** "Baue 15 neue Citations für Praxis Suriya in Branchenverzeichnissen auf"
- **Result:** PASS. Negative trigger in description (`Do NOT use for the Maps audit (maps-audit), for writing or rewriting page copy...`) successfully blocked `un-burning` from loading. Routed correctly to `/citations-dach`.
