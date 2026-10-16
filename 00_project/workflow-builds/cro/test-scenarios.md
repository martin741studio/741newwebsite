# 2.2 Test Scenarios: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Workflow: CRO Homepage Track A (`cro`)

---

## Scenario 1: Obvious Trigger (Full Standard Command)
- **Prompt:** `/cro-homepage "Praxis Dumann", https://osteopathie-dumann.de, https://maps.app.goo.gl/xyz, WhatsApp: +49170123456`
- **Expected Action:**
  - Skill activates in Track A standard mode.
  - Ingests practice details, creates `00_project/assets/praxis-dumann/cro/` folder structure.
  - Loads run-checklist and begins Step 1 intake.
  - Pauses at Checkpoint 1 (copy approval) and Checkpoint 2 (prototype approval).
- **Expected Deliverable:** Full CRO run initialized with standard checklist.

## Scenario 2: Paraphrased Trigger
- **Prompt:** "Erstelle einen neuen CRO-Startseiten-Prototyp für Daniela Dumann mit ihrer aktuellen Website"
- **Expected Action:**
  - Skill activates. Identifies Dumann URL from context/memory.
  - Queries for missing GBP or contact channel parameters if not found.
  - Loads Track A execution pipeline.
- **Expected Deliverable:** Skill activates and prompts for any missing mandatory inputs.

## Scenario 3: Negative Trigger (Must NOT Trigger)
- **Prompt:** "Baue einen Track B Showpiece Prototyp mit WebGL und 3D Partikeln für Dumann"
- **Expected Action:**
  - Skill must NOT trigger.
  - Track B (design-intense interactive showpiece) is strictly excluded via frontmatter (`Do NOT use for Track B design-intense runs ("track B", showpiece, motion-heavy pitch)`).
- **Expected Result:** Routes to `cro_b` workflow spec or asks B0 questionnaire questions; `cro-homepage` remains uninvoked.
