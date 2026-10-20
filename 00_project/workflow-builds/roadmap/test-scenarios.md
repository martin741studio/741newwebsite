# Test Scenarios: Client Roadmap & Goal Engine (`roadmap`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `roadmap`

---

## Scenario 1: Obvious Trigger (Direct Command)
- **Prompt:** `/client-roadmap Talkinfive` or "Zeig mir die Roadmap und Goals für Talkinfive"
- **Expected Behavior:**
  1. Identifies client `Talkinfive`.
  2. Ingests `00_project/assets/talkinfive/roadmap.json` or runs audit synthesis if none exists.
  3. Displays North Star Goal, current baseline, benchmark gap, active milestone, and next tasks.
  4. Does NOT execute code edits or mutate live WordPress.

## Scenario 2: Paraphrase Trigger (Conversational Context)
- **Prompt:** "Was sind die nächsten Zwischenschritte für Celine und wo stehen wir im Vergleich zum Wettbewerb?"
- **Expected Behavior:**
  1. Resolves alias `Celine` -> `Talkinfive`.
  2. Surfaces milestone status ($M_1$ completed, $M_2$ ready for execution).
  3. Explains the benchmark gap (10.5 MB vs <1.5 MB standard, TTFB 2s vs <200ms).
  4. Asks for confirmation before executing any speed optimization tasks.

## Scenario 3: Must-Not-Trigger (Negative Boundary Trigger)
- **Prompt:** "Schreib einen Blogartikel über Akupunktur für Praxis Suriya" or "Fix den Header-Abstand auf katharinakisser.at"
- **Expected Behavior:**
  - Must NOT trigger the full roadmap creation workflow.
  - Only performs a silent 1-line Pre-Flight check if relevant, then delegates directly to the appropriate specialized execution workflow (`content-write` or bugfix).
  - Must NOT rewrite or overwrite the client's `roadmap.json` or regenerate goals.
