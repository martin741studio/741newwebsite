# Maps Playbook Test Scenarios

Workflow ID: phone
Date: 2026-10-16

## Scenario 1: Obvious Trigger
- **User Prompt:** "Maps-Playbook für Martin Hüwel starten" or `/maps-playbook huewel`
- **Expected Behavior:** Workflow triggers immediately. Ingests Hüwel audit run data, checks un-burning status, maps all 77 measures against concrete evidence, identifies open gaps, generates phased task list (`d1-30`, `m2+`, `later`), and presents the visual board for Checkpoint A review.
- **Expected Deliverables:** `matrix.json`, `tasks.json`, HTML board, Excel export, and `_run.json`.

## Scenario 2: Paraphrased Trigger
- **User Prompt:** "Was fehlt, damit Praxis Suriya auf Google Maps Platz 1 für Akupunktur Mainz/Ingelheim erreicht?"
- **Expected Behavior:** Workflow detects intent to calculate Maps rank growth measures. Triggers `maps-playbook` in evaluation mode, benchmarks current profile against the 77-measure standard, filters out measures blocked by open un-burning harm, and outputs the top growth levers.
- **Expected Deliverables:** Phased growth matrix, client bundle preview, and `_run.json`.

## Scenario 3: Negative Trigger (Must NOT Trigger)
- **User Prompt:** "Führe den vollständigen 100-Punkte Maps-Audit für Dr. Stürzl durch" or "Repariere die alte Schützenpfad-Adresse bei Suriya in den Verzeichnissen"
- **Expected Behavior:** Workflow **MUST NOT trigger** / should NOT trigger. The 100-point initial diagnosis is handled exclusively by `/maps-audit`, and harm/address repair is handled by `/un-burning`. The Maps Playbook only tracks and plans growth measures on a clean bedrock.
- **Resolution:** The agent routes the prompt to `maps-audit` or `un-burning` and does NOT run the playbook generator.
