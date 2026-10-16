# Backlink DACH Test Scenarios

Workflow ID: backlink
Date: 2026-10-16

## Scenario 1: Obvious Trigger
- **User Prompt:** "Backlink-Workflow für Martin Hüwel starten" or `/backlink-dach huewel, nürnberg`
- **Expected Behavior:** Workflow triggers immediately. Prompts once if budget/niche is missing, extracts 8+ local competitors, runs DataForSEO backlink gap analysis, classifies targets into Pillars B–E, builds the Google Sheet with Freigabe boxes, and writes `_run.json`.
- **Expected Deliverables:** `targets.csv`, target workbook with Freigabe boxes, handoff list to Citations module, and `_run.json`.

## Scenario 2: Paraphrased Trigger
- **User Prompt:** "Welche lokalen Links und Verbandseinträge können wir für Martin Hüwel in Nürnberg aufbauen?"
- **Expected Behavior:** Workflow detects intent to prospect local backlinks. Triggers `backlink-dach` in discovery mode, evaluates local Chamber/Association opportunities, and drafts outreach candidates.
- **Expected Deliverables:** Ranked target sheet preview with cost estimates and contact points.

## Scenario 3: Negative Trigger (Must NOT Trigger)
- **User Prompt:** "Trage Martin Hüwel in Das Örtliche und Gelbe Seiten ein" or "Schreibe den Text für die Leistungsseite"
- **Expected Behavior:** Workflow **MUST NOT trigger** / should NOT trigger. General and niche directory submissions belong exclusively to `/citations-dach`, and page copywriting belongs to `/content-write`. Backlink DACH only handles non-directory link targets across Pillars B–E.
- **Resolution:** The agent routes the prompt to `citations-dach` or `content-write` and does NOT run the backlink generator.
