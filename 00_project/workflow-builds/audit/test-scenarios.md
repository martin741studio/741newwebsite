# Test Scenarios: Maps Audit Workflow (`audit`)

Written BEFORE the body of the skill (Rule R1.2).

## Scenario 1: Obvious Trigger
* **Prompt:** "Starte den Maps-Audit für Praxis Suriya"
* **Expected Result:** The `audit` skill loads. Reads client GBP, site, keywords, and competitor data from local assets. Executes deterministic audit scoring scripts, outputs report and harm separation.

## Scenario 2: Paraphrased Trigger
* **Prompt:** "Führe die Maps-Readiness Prüfung für diesen Kunden durch"
* **Expected Result:** The `audit` skill loads. Recognizes "Maps-Readiness" as the core deliverable. Prepares data intake checklist.

## Scenario 3: Negative Trigger (Must NOT Trigger)
* **Prompt:** "Mach einen neuen Google Maps Ranking Scan für Hüwel"
* **Expected Result:** The `audit` skill must NOT trigger. A single spatial ranking check belongs to `ranking-tracking-master-prompt.md` or Local Falcon grid scans, NOT the comprehensive 100-point Maps Audit.
