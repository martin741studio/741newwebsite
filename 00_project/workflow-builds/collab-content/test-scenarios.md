# Test Scenarios: Co-Marketing & Backlink Collaboration Workflow (`collab-content`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `collab-content`

---

## Scenario 1: Obvious Trigger (Direct Command)
- **Prompt:** `/collab-content balihealing https://ayurvedagrambali.com` or "Starte die Backlink-Kollaboration zwischen Bali Healing und Ayurvedagram Bali"
- **Expected Behavior:**
  1. Identifies client `balihealing` and partner `ayurvedagrambali.com`.
  2. Ingests client baseline from `00_project/assets/balihealing/`.
  3. Analyzes partner domain for complementary offerings.
  4. Generates Mini-Pool of 2–3 collaboration angles.
  5. Stops at Checkpoint 1 and presents Decision Card to Martin.
  6. Does NOT publish to WordPress or Wix without approval.

## Scenario 2: Paraphrase Trigger (Conversational Request)
- **Prompt:** "Wir wollen für Bali Healing was mit Ayurveda Gram machen, was können wir denen vorschlagen und worüber schreiben?"
- **Expected Behavior:**
  1. Resolves `Bali Healing` and `Ayurveda Gram`.
  2. Triggers Mini-Pool analysis mode (Use Case 2).
  3. Evaluates geographic and clinical synergies (Canggu outpatient vs. Ubud inpatient).
  4. Delivers 2–3 concrete editorial pitch angles with suggested backlink destinations.
  5. Prompts Martin whether to proceed with drafting the reciprocal articles.

## Scenario 3: Must-Not-Trigger (Negative Boundary Trigger)
- **Prompt:** "Schreib einen Blogartikel über Akupunktur für Bali Healing" or "Kauf 10 Backlinks für Hüwel"
- **Expected Behavior:**
  - Must NOT trigger the `collab-content` workflow.
  - Normal internal blog articles are handled by `/content-writing` or `/content-pool`.
  - Directory or paid link acquisition is handled by `/backlink-dach` or the Citation module.
  - Does NOT initiate partner scraping or create collaboration files.
