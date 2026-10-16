# Test Scenarios: Citations DACH Workflow (`citations`)

Written BEFORE writing the skill body (Rule R1.2).

## Scenario 1: Obvious Trigger
* **Prompt:** "Prüfe den Citation-Status für Praxis Suriya" (or `/citations-dach suriya`)
* **Expected Result:** The `citations-dach` skill loads. Reads canonical NAP from `client_locations`, checks status of the 44 DACH directories in `client_citations`, and prepares the submission runbook.

## Scenario 2: Paraphrased Trigger
* **Prompt:** "Starte den Verzeichnis-Abgleich für diesen Kunden"
* **Expected Result:** The `citations-dach` skill loads. Identifies directory listings task. Executes `citation-monitor.mjs` to check live directory URLs.

## Scenario 3: Negative Trigger (Must NOT Trigger)
* **Prompt:** "Finde neue Backlinks von Zeitungen, Kammern und Verbänden für Hüwel"
* **Expected Result:** The `citations-dach` skill must NOT trigger. Authority link building belongs to `/backlink-dach`, NOT local directory citations.
