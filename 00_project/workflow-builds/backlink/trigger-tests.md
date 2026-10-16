# Backlink DACH Trigger Tests

Workflow ID: backlink
Date: 2026-10-16
Skill: `.claude/skills/backlink-dach/SKILL.md`

## Scenario 1: Obvious Trigger
- **Input:** `/backlink-dach huewel, nürnberg` or "Backlink-Workflow für Martin Hüwel"
- **Result:** PASS. Frontmatter `description` triggered immediately. Verified client parameters, loaded existing target dataset, and initiated Step 0 read-only check.

## Scenario 2: Paraphrased Trigger
- **Input:** "Welche lokalen Links und Verbandseinträge können wir für Martin Hüwel in Nürnberg aufbauen?"
- **Result:** PASS. Paraphrased query detected intent to prospect local backlinks. Triggered `backlink-dach` in discovery mode.

## Scenario 3: Negative Trigger Guard
- **Input:** "Trage Martin Hüwel in Das Örtliche und Gelbe Seiten ein"
- **Result:** PASS. Negative trigger in description (`Do NOT use for any directory or citation entry...`) successfully blocked `backlink-dach` from loading. Routed correctly to `/citations-dach`.
