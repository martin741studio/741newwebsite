# Content Pool Test Scenarios

Workflow ID: pool
Date: 2026-10-16

## Scenario 1: Obvious Trigger
- **User Prompt:** "Content-Pool für Praxis Suriya erstellen" or `/content-pool suriya`
- **Expected Behavior:** Workflow triggers immediately. Prompts once if any input parameter is missing, initializes run directory at `00_project/assets/suriya/content-pool/`, and executes Step 0 through Step 8.
- **Expected Deliverables:** `candidates.json`, `pool.json`, `summary.json`, `pool-top.md`, rendered HTML report, and `_run.json`.

## Scenario 2: Paraphrased Trigger
- **User Prompt:** "Welche Inhalte und Suchbegriffe braucht die neue Website von Martin Hüwel für die Startseite?"
- **Expected Behavior:** Workflow detects intent to build the 4-pillar keyword and topic matrix. Triggers `content-pool` skill in existing-site or new-site mode, loads Hüwel services list, and initiates research sequence.
- **Expected Deliverables:** Validated pool report, four-pillar cards, and `_run.json` status at Checkpoint 1.

## Scenario 3: Negative Trigger (Must NOT Trigger)
- **User Prompt:** "Schreibe mir den Text für die Unterseite Akupunktur bei Praxis Suriya" or "Erstelle den CRO-Prototypen für die Startseite"
- **Expected Behavior:** Workflow **MUST NOT trigger** / should NOT trigger. Text generation is handled exclusively by `/content-write` (`copy`), and homepage wireframing/prototyping is handled by `/cro-homepage` (`cro`).
- **Resolution:** The agent routes the prompt to `content-write` or `cro-homepage` and does NOT run the content pool generator.
