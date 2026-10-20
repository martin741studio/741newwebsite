# Step 0.0 Inputs Grill Record: Co-Marketing & Backlink Collaboration Workflow (`collab-content`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `collab-content`
Status: Confirmed via Interactive Decision Cards

---

## 1. The Job (Objective & Scope)
- **What enters:**
  - Client profile & baseline (services, target audience, local presence, core assets from `00_project/assets/<client>/`).
  - Partner profile (services, location, domain, existing content, audience).
  - Geographic/niche context (e.g. Bali health & wellness ecosystem: Canggu outpatient vs. Ubud inpatient retreat).
- **What transforms:**
  1. *Mini-Pool Extraction:* Identifies high-synergy, non-competing service intersections and audience overlaps between the two brands.
  2. *Collaboration Angle Formulator:* Generates 2–3 reciprocal collaboration pitches (e.g. "Coast to Jungle Vitality", "Preparing & Integrating Panchakarma with Cellular Medicine").
  3. *Co-Marketing Content Writing:* Following Martin's approval of an angle, drafts two complementary editorial articles:
     - Article 1 (Client site): Educational feature introducing the partner with deep contextual anchor links.
     - Article 2 (Partner site): Educational guest/feature guide introducing the client with contextual anchor links back to core services.
  4. *Quality & Compliance Gate:* Lints for plain text (no broken HTML for CMS text boxes), verifies E-E-A-T factual grounding, and ensures adherence to Google health/YMYL policies.
- **Who uses output:**
  - Martin Drendel (for partnership outreach, client review, and final publishing sign-off).
  - 741 Content Team & Client (ready-to-pitch proposals and copy for WordPress/Wix CMS).
  - The Collaboration Partner (clean, value-additive guest editorial ready to publish).

## 2. Runtime Surface
- **Primary surface:** Multi-Surface Agent Skill in Antigravity IDE and Claude Code (`/collab-content <client> <partner-domain>` or conversational prompt).
- **Data substrate:**
  - Client profiles stored in `00_project/assets/<client>/`.
  - Workflow run telemetry recorded in `00_project/assets/<client>/collab/<partner-slug>/_run.json`.
  - Staged article deliverables in `00_project/assets/<client>/collab/<partner-slug>/`.
- **Reporting surface:** Telemetry synced to workflow registry (`00_project/workflow-registry/registry.json`) and Morning Grill.

## 3. Cadence / Frequency
- **Turnus:** On-demand per partner collaboration opportunity or strategic link-building milestone in the client's roadmap.

## 4. Hard Limits (Failure Boundaries)
- **Zero Low-Quality / Reciprocal Link Spam Schemes:** Never produce artificial 1:1 footer, sidebar, or keyword-stuffed reciprocal links. All backlinks must be contextually embedded within high-value, comprehensive editorial guides that pass Google Webmaster Guidelines.
- **Zero Direct Live Publishing Without Go:** The workflow NEVER publishes directly to a live website or sends unapproved emails/WhatsApp messages to partners without Martin's explicit Go via Decision Card.
- **Zero Health / Disease Cures (YMYL Compliance):** Strictly enforce health policy rules (no cure promises, no unauthorized medical claims, factual practitioner/treatment framing).
- **Strict Plain Text in CMS Text Boxes:** Deliverables destined for client-editable fields must be strict plain text — no raw `<span>`, `<div>`, or inline styles.
- **Zero Billable API Credit Burn:** Free open web extraction and existing client data must be prioritized before any billable API calls.
