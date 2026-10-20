# 741 Co-Marketing & Backlink Collaboration Workflow Specification (`collab-content`)

Version 1.0 · 2026-10-16 · Owner: Martin Drendel · Approved Cybernetic Architecture.
Language: STE. Registry ID: `collab-content`. Skill: `.claude/skills/collab-content/SKILL.md`.

---

## 0. Purpose & Cybernetic Context

The **Co-Marketing & Backlink Collaboration Workflow** (`collab-content`) creates high-authority, reciprocal content partnerships between 741 clients and complementary regional or niche businesses. 

Unlike primitive link exchanges (which risk Google link-scheme penalties), `collab-content` pairs a lightweight ideation engine (**Mini-Pool**) with high-standard **Co-Marketing Editorial Writing**:
1. It screens and extracts non-competing, complementary service intersections (e.g. coastal outpatient functional medicine x inland inpatient Ayurvedic retreat).
2. It generates a Mini-Pool of 2–3 specific, mutually beneficial article angles.
3. It drafts two complementary, in-depth editorial articles with natural, contextual backlinks.
4. It enforces strict plain-text CMS hygiene (zero HTML tags in client-editable boxes) and YMYL compliance.

```
[ 1. Sensory Ingestion ]
• Client baseline: services, target audience, local anchor, YMYL boundaries (`00_project/assets/<client>/`)
• Partner ingestion: live domain scrape, services, target audience, content structure
                 │
                 ▼
[ 2. Transformation Core: R1.7 Separation ]
• Deterministic: URL validation, domain parsing, anchor schema check (`scripts/extract_synergy.py`)
• Guided Heuristic: Mini-Pool formulation (3 distinct collaboration angles + thesis)
                 │
                 ▼
[ 3. Governance Gate: Checkpoint 1 ] ──► Martin Decision Card (`ask_question`)
                 │ (Approved Angle)
                 ▼
[ 4. Reciprocal Copy Generation ]
• Article 1 (Client Site): Feature guide introducing partner with natural contextual deep link
• Article 2 (Partner Site): Guest feature guide introducing client with natural contextual deep link
                 │
                 ▼
[ 5. Sensor Loop & Lint Filter ]
• Deterministic: `scripts/lint_collab.py` (checks plain text, strips raw HTML, flags YMYL cure claims, validates links)
                 │ (0 Errors)
                 ▼
[ 6. Governance Gate: Checkpoint 2 ] ──► Martin Decision Card (`ask_question`)
                 │ (Approved)
                 ▼
[ 7. Expression & Delivery ]
• Staged deliverables in `00_project/assets/<client>/collab/<partner-slug>/`
• Telemetry written to `_run.json`
• Ready for CMS pasting (strict plain text) and partner email/WhatsApp dispatch
```

---

## 1. The Collaboration Data Contract (`collab_spec.json`)

Every collaboration run maintains a structured JSON manifest at `00_project/assets/<client>/collab/<partner-slug>/spec.json`:

```json
{
  "client": "balihealing",
  "partner": {
    "name": "Ayurvedagram Bali",
    "domain": "ayurvedagrambali.com",
    "location": "Ubud, Bali",
    "core_services": ["Panchakarma", "Vaidya Consultations", "Shirodhara", "Abhyanga", "Yoga & Meditation"]
  },
  "synergy": {
    "geographic_complement": "Coast (Canggu) x Jungle (Ubud)",
    "modality_complement": "Modern Functional Medicine / IV & Ozone x Classical Kerala Ayurveda",
    "shared_audience": "Expats, wellness travelers, long-term digital nomads in Bali"
  },
  "selected_angle": {
    "id": "ANGLE-1",
    "title_working": "The Pre- & Post-Retreat Optimization Protocol",
    "thesis": "How combining coastal cellular medicine (IV therapy & medical ozone) with deep Ubud Ayurvedic Panchakarma creates a complete 360-degree longevity journey."
  },
  "articles": {
    "article_client": {
      "target_site": "balihealing.com",
      "working_title": "The Essential Guide to Authentic Ayurvedic Panchakarma in Bali: Inside Ubud's Leading Sanctuary",
      "featured_partner": "Ayurvedagram Bali",
      "target_url": "https://www.ayurvedagrambali.com/panchakarma",
      "anchor_text": "authentic Panchakarma retreats in Ubud at Ayurvedagram Bali",
      "file_path": "article_client.md"
    },
    "article_partner": {
      "target_site": "ayurvedagrambali.com",
      "working_title": "Integrating Modern Cellular Medicine with Ancient Ayurveda: How IV Therapy & Ozone Support Your Healing Journey in Bali",
      "featured_client": "Bali Healing",
      "target_urls": [
        "https://balihealing.com/infusions",
        "https://balihealing.com/ozonetherapy"
      ],
      "anchor_text": "specialized IV infusions and medical ozone therapy at Bali Healing in Canggu",
      "file_path": "article_partner.md"
    }
  },
  "status": "drafted"
}
```

---

## 2. Hard Invariants & Guardrails

### Invariant 1: Plain-Text WordPress & Wix CMS Boxes
- Deliverables destined for client-editable fields must be strict plain text.
- Never include raw HTML tags (`<span>`, `<div>`, `<br>`, inline styles) in headings or body text.
- Formatting must rely exclusively on Markdown headers (`#`, `##`, `###`), bold (`**`), bullet points (`-`), and clean markdown links (`[text](url)`).

### Invariant 2: Google YMYL & Medical Policy Compliance
- Zero disease cure promises or unverified therapeutic claims.
- Treatments must be framed accurately (e.g. "supports natural vitality and hydration", not "cures chronic fatigue").
- Practitioner qualifications must be factual (e.g. "licensed Indonesian medical doctors and nurses" for Bali Healing; "experienced resident Ayurvedic Vaidyas" for Ayurvedagram Bali).

### Invariant 3: Zero Low-Quality Reciprocal Link Footprint
- No 1:1 homepage reciprocal links.
- No sitewide footer or sidebar link swaps.
- Every backlink must be embedded contextually within 1,200+ words of genuinely valuable editorial copy.

---

## 3. Step-by-Step Operational Instructions

### Step 1: Ingest Client & Partner
1. Read client baseline from `00_project/assets/<client>/01-client/client-baseline.md`.
2. Scrape partner domain via `read_url_content` or `search_web`.
3. Extract core services, location, and audience.

### Step 2: Formulate the Mini-Pool (3 Angles)
1. Run `python3 scripts/extract_synergy.py <client> <partner-domain>`.
2. Formulate 3 distinct collaboration angles:
   - *Angle A:* Pre/Post Care or Modality Integration Protocol.
   - *Angle B:* Lifestyle, Longevity & Everyday Habit Guide.
   - *Angle C:* Curated Regional Healing Itinerary / Directory.

### Step 3: Checkpoint 1 (Angle Selection)
1. Present the 3 angles to Martin using an interactive Decision Card (`ask_question`).
2. Halt execution until Martin selects the preferred angle.

### Step 4: Draft Reciprocal Article Pair
1. Draft Article 1 (for client site, featuring partner). Word count: 1,200–1,800 words.
2. Draft Article 2 (for partner site, featuring client). Word count: 1,200–1,800 words.
3. Embed natural, contextual deep links with descriptive anchor text.

### Step 5: Deterministic Linting
1. Run `python3 scripts/lint_collab.py <path-to-article-pair>`.
2. Verify:
   - 0 raw HTML tags in client text inputs.
   - 0 forbidden YMYL cure claims.
   - 100% valid, accessible target URLs.

### Step 6: Checkpoint 2 (Publishing Sign-off)
1. Present final deliverables and lint report to Martin via Decision Card (`ask_question`).
2. On approval, stage files for CMS publishing and partner dispatch. Emitted `_run.json`.
