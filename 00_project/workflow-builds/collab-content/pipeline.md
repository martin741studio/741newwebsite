# Pipeline & Architecture Specification: Co-Marketing & Backlink Collaboration Workflow (`collab-content`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `collab-content`

---

## 1. Architectural Shape (Cybernetic Regulation Loop)

```
[ Ingestion Membrane ]
• Client Profile: Baseline services, audience, local geography, compliance rules
• Partner Ingestion: Scrape domain, services, target audience, content structure
                 │
                 ▼
[ Transformation Core: R1.7 Separation ]
• Deterministic: Synergy extraction (`scripts/extract_synergy.py`), URL & anchor schema checks
• Heuristic: Synergy matrix synthesis, Mini-Pool angle ideation (3 distinct collaboration angles)
                 │
                 ▼
[ Checkpoint 1: Angle Selection Gate ] ──► Martin Decision Card (`ask_question`)
                 │ (Approved Angle)
                 ▼
[ Editorial Generation: Reciprocal Drafting ]
• Article 1 (Client Site): In-depth guide introducing partner with natural contextual link
• Article 2 (Partner Site): Guest feature guide introducing client with natural contextual link
                 │
                 ▼
[ Verification Loop & Sensor Filter ]
• Deterministic: `scripts/lint_collab.py` (checks plain text, strips raw HTML, flags YMYL cure claims, validates links)
                 │ (Passed: 0 Lint Errors)
                 ▼
[ Checkpoint 2: Publishing & Outreach Gate ] ──► Martin Decision Card (`ask_question`)
                 │ (Approved)
                 ▼
[ Delivery & Expression ]
• Staged Markdown in `00_project/assets/<client>/collab/<partner-slug>/`
• Telemetry written to `_run.json`
• Ready for CMS pasting (strict plain text) and partner email/WhatsApp dispatch
```

---

## 2. Checkpoints & Gates

| Checkpoint | Gate Requirement | Verification Method | Enforcement |
|---|---|---|---|
| **CP0 (Ingestion)** | Client baseline and partner site successfully scraped and verified. | File existence & schema check | Pre-flight validation |
| **CP1 (Angle Selection)** | Martin selects 1 of the 3 Mini-Pool angles via Decision Card. | Interactive Decision Card (`ask_question`) | Mandatory human Go |
| **CP2 (Draft Approval)** | Both articles pass `lint_collab.py` (0 HTML tags in client text, 0 YMYL violations, valid anchors). Martin approves final copy. | `python3 scripts/lint_collab.py` + Decision Card | Mandatory human Go before outreach |

---

## 3. Degrees of Freedom per Step (Rule R1.7)

| Step | Freedom Level | Mechanism | Rationale |
|---|---|---|---|
| **1. Partner Scraping & Parsing** | Zero (Deterministic) | `read_url_content` / Python parser | Raw page structure, services, and URLs must be exact. |
| **2. Synergy Matrix & Angle Ideation** | Medium (Heuristic) | LLM prompt guided by non-competing complementary rules | Strategic business creativity needed to find compelling cross-brand narratives. |
| **3. Angle Selection Gate (CP1)** | Zero (Human Gate) | Decision Card (`ask_question`) | Martin decides strategic direction before copy generation starts. |
| **4. Article Copy Drafting** | High (Heuristic) | LLM prompt adhering to 741 editorial style & E-E-A-T | Needs compelling storytelling, natural flow, and high editorial value. |
| **5. Plain-Text & Compliance Linting** | Zero (Deterministic) | Python script (`scripts/lint_collab.py`) | Plain text for CMS boxes, link schema, and banned medical terms must be 100% deterministic. |
| **6. Final Publishing Gate (CP2)** | Zero (Human Gate) | Decision Card (`ask_question`) | No drafts leave 741 or hit client CMS without Martin's explicit sign-off. |
