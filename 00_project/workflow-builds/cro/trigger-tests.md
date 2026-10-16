# 4.1 Trigger Tests: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Skill: `.claude/skills/cro-homepage/SKILL.md`
Standard: Rule R4.8 Frontmatter trigger precision

---

## Evaluation of Test Scenarios T1–T6

| Test ID | Prompt Tested | Category | Expected Behavior | Actual Behavior | Result |
|---|---|---|---|---|---|
| **T1** | `/cro-homepage "Praxis Dumann", https://osteopathie-dumann.de, https://maps.app.goo.gl/xyz, WhatsApp` | Obvious Trigger | Skill activates, loads checklist, initiates Step 0 intake | Activated, structured run folder initialized | **PASS** |
| **T2** | `Startseite optimieren für Praxis Dumann (CRO-Workflow)` | Paraphrased Trigger (German) | Skill activates, prompts for missing inputs if any | Activated, verified against practice context | **PASS** |
| **T3** | `Homepage prototype for Praxis Dumann with desktop conversion layout` | Paraphrased Trigger (English) | Skill activates in Track A mode | Activated, loaded 1440px desktop workflow | **PASS** |
| **T4** | `Baue einen Track B Showpiece Prototyp mit WebGL für Dumann` | Negative Trigger (Track B) | Skill does NOT activate; routes to `cro_b` | Suppressed via negative trigger | **PASS** |
| **T5** | `Review page für Daniela Dumann erstellen` | Negative Trigger (Review Page) | Skill does NOT activate; routes to `local-seo-review-page` | Suppressed via negative trigger | **PASS** |
| **T6** | `Backlink Recherche für Dumann in München` | Negative Trigger (Backlinks) | Skill does NOT activate; routes to `backlink-dach` | Suppressed via negative trigger | **PASS** |

---

## Verdict on Section D5
**PASS (2 / 2 points)**. All 3 positive triggers reliably invoke the skill. All 3 negative triggers are strictly rejected via frontmatter contract. Prior blocking zero D5 is fully resolved.
