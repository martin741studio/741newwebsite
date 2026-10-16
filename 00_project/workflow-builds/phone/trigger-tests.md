# Maps Playbook Trigger Tests

Workflow ID: phone
Date: 2026-10-16
Skill: `.claude/skills/maps-playbook/SKILL.md`

## Scenario 1: Obvious Trigger
- **Input:** `/maps-playbook huewel` or "Maps-Playbook für Martin Hüwel"
- **Result:** PASS. Frontmatter `description` triggered immediately. Loaded Hüwel parameters, checked existing audit run JSON, and initiated 77-measure matrix mapping.

## Scenario 2: Paraphrased Trigger
- **Input:** "Was fehlt, damit Praxis Suriya auf Google Maps Platz 1 für Akupunktur Mainz/Ingelheim erreicht?"
- **Result:** PASS. Paraphrased query detected intent to evaluate Google Maps growth levers. Triggered `maps-playbook` in evaluation mode.

## Scenario 3: Negative Trigger Guard
- **Input:** "Mach ein Maps-Audit für Stürzl"
- **Result:** PASS. Negative trigger in description (`Do NOT use for the diagnosis audit (maps-audit), for clean-up of harm (un-burning)...`) successfully blocked `maps-playbook` from loading. Routed correctly to `/maps-audit`.
