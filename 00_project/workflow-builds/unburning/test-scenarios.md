# Un-Burning Test Scenarios

Workflow ID: unburning
Date: 2026-10-16

## Scenario 1: Obvious Trigger
- **User Prompt:** "Starte Un-Burning für Praxis Suriya" or `/un-burning suriya`
- **Expected Behavior:** Workflow triggers immediately. Validates access preconditions, loads audit findings, initializes `harm-register.json`, runs triage, generates the Bedrock Pack, and prompts Martin for batch approval before executing any live fixes.
- **Expected Deliverables:** `harm-register.json`, `bedrock-status.json`, internal HTML damage map, and `_run.json`.

## Scenario 2: Paraphrased Trigger
- **User Prompt:** "Welche Altlasten, falschen Adressen und schädlichen Einträge müssen wir bei Bali Healing reparieren?"
- **Expected Behavior:** Workflow detects intent to identify digital harm and damage. Triggers `un-burning` workflow in triage mode, scans GBP and citation duplicates, and presents the keep/fix/kill list.
- **Expected Deliverables:** Damage register with B–E area classification, rollback snapshots, and `_run.json`.

## Scenario 3: Negative Trigger (Must NOT Trigger)
- **User Prompt:** "Baue 15 neue Citations für Praxis Suriya in Branchenverzeichnissen auf" or "Erstelle eine neue Landingpage für Akupunktur"
- **Expected Behavior:** Workflow **MUST NOT trigger** / should NOT trigger. New directory submissions belong to `/citations-dach`, and new page builds belong to `/cro-homepage`. Un-Burning only removes or repairs existing harm; it never performs growth building.
- **Resolution:** The agent routes the prompt to `citations-dach` or `cro-homepage` and does NOT run the harm remediation skill.
