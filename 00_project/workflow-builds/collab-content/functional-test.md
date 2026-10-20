# Functional Test: Co-Marketing & Backlink Collaboration Workflow (`collab-content`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `collab-content`

---

## 1. Test Overview
- **Pairing:** Bali Healing (`balihealing.com`) x Ayurvedagram Bali (`ayurvedagrambali.com`).
- **Input Baseline:** `00_project/assets/balihealing/01-client/client-baseline.md`.
- **Target Deliverables:**
  - Manifest: `00_project/assets/balihealing/collab/ayurvedagrambali/spec.json`
  - Article 1: `00_project/assets/balihealing/collab/ayurvedagrambali/article_client.md`
  - Article 2: `00_project/assets/balihealing/collab/ayurvedagrambali/article_partner.md`
  - Telemetry: `00_project/assets/balihealing/collab/ayurvedagrambali/_run.json`

---

## 2. Test Execution & Evidence

### Phase 1 & 2: Ingestion & Mini-Pool Formulation
- Ingested Bali Healing services: IV Drips, medical ozone, TCM acupuncture, dermatoscopy, aesthetic clinic.
- Scraped Ayurvedagram Bali: Inpatient Kerala Ayurvedic retreat resort in Ubud, Panchakarma, resident Vaidyas, yoga, vegan nutrition.
- Generated 3 complementary angles without geographic or modal competition.
- Staged in `spec.json`.

### Phase 3: Checkpoint 1
- Presented angles to Martin via Decision Card (`ask_question`).
- Martin selected Angle 1: "The Pre- & Post-Retreat Optimization Protocol".

### Phase 4: Reciprocal Drafting
- Drafted Article 1 (on `balihealing.com`): ~800 words educating readers on authentic Ubud Panchakarma at Ayurvedagram Bali, linking to `https://www.ayurvedagrambali.com/panchakarma`.
- Drafted Article 2 (on `ayurvedagrambali.com`): ~850 words educating retreat guests on cellular preparation and post-cleanse integration with IV drips and ozone therapy at Bali Healing in Canggu, linking to `https://balihealing.com/infusions` and `https://balihealing.com/ozonetherapy`.

### Phase 5: Verification & Linting
- Executed `scripts/lint_collab.py`:
  ```bash
  python3 .claude/skills/collab-content/scripts/lint_collab.py \
    00_project/assets/balihealing/collab/ayurvedagrambali/article_client.md \
    00_project/assets/balihealing/collab/ayurvedagrambali/article_partner.md
  ```
  Result:
  - 0 raw HTML tags detected.
  - 0 forbidden YMYL cure claims detected.
  - Valid, descriptive markdown contextual backlinks confirmed.
  - Exit code: 0.

### Phase 6: Telemetry Emitted
- Executed `scripts/write_run.py`:
  - `_run.json` successfully written to `00_project/assets/balihealing/collab/ayurvedagrambali/_run.json`.

---

## 3. Verdict
Functional test fully PASSED. Both editorial deliverables are verified, safe, and staged.
