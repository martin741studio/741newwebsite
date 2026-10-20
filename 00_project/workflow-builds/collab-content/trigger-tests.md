# Trigger Tests: Co-Marketing & Backlink Collaboration Workflow (`collab-content`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `collab-content`

---

## Test 1: Obvious Trigger (Direct Command)
- **Input Prompt:** `/collab-content balihealing https://ayurvedagrambali.com`
- **Observed Behavior:**
  - Skill correctly identified client `balihealing` and partner `https://ayurvedagrambali.com`.
  - Ingested client baseline from `00_project/assets/balihealing/01-client/client-baseline.md`.
  - Scraped partner domain and generated Mini-Pool with 3 collaboration angles.
  - Halted at Checkpoint 1 and requested angle confirmation via Decision Card.
- **Result:** PASS (100% compliant).

---

## Test 2: Paraphrase Trigger (Conversational Request)
- **Input Prompt:** "Wir wollen für Bali Healing was mit Ayurveda Gram machen, was können wir denen vorschlagen und worüber schreiben?"
- **Observed Behavior:**
  - Correctly resolved `Bali Healing` and `Ayurveda Gram`.
  - Activated Phase 2 (Synergy Extraction & Mini-Pool Formulation).
  - Formulated 3 distinct angles (Pre/Post Care Protocol, Expat Lifestyle Habits, Curated Bali Wellness Itinerary).
  - Prompted operator for angle choice via Decision Card.
- **Result:** PASS (100% compliant).

---

## Test 3: Must-Not-Trigger (Negative Boundary Trigger)
- **Input Prompt:** "Schreib einen Blogartikel über Akupunktur für Bali Healing"
- **Observed Behavior:**
  - Evaluated prompt against negative trigger `NOT:`.
  - Did NOT trigger `collab-content`.
  - Correctly routed the request to standard `/content-writing` for internal blog production.
  - Zero unwanted collaboration files created.
- **Result:** PASS (100% compliant).
