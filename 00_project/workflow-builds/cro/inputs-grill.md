# Step 0.0 Inputs Grill Record: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `cro`
Status: Confirmed

---

## 1. The Job (Objective & Scope)
- **What enters:** Practice/business name, live website URL, Google Business Profile link, preferred contact channel (WhatsApp, phone, booking link).
- **What transforms:** Scrapes live site content and branding; generates SEO/GEO and conversion copy through content-writing gates; creates GPT visual style reference; codes 1440px desktop HTML prototype; validates visual hierarchy and motion; packages deliverable into client Drive folder.
- **Who uses output:** Martin, agency designer/developer (Dinakar), and prospective/onboarded client.

## 2. Runtime Surface
- **Primary surface:** Terminal (Claude Code `/cro-homepage`), Claude in Chrome (for visual check and Drive upload), local HTTP server (`python3 -m http.server`).
- **Enforcement surface:** `scripts/guard_upload.py` (blocks accidental server uploads), `scripts/verify.py`, `run_gates.py` for copy.

## 3. Cadence / Frequency
- **Turnus:** On demand per client during Phase 4 (Build-up) or Phase 0 (Prospect showcase).

## 4. Hard Limits (Failure Boundaries)
- **Zero Live Server Uploads:** Prototypes remain strictly local; never deploy to live server without Martin's explicit written approval.
- **Zero Invented Facts:** Every claim, price, or duration must trace directly to `02-data/dataset.md` or carry `[FEHLT]`.
- **Compliance Rules:** Health practices run in strict HWG mode (no healing promises, no fear framing); law firms run in BRAO mode (no unverified specialist claims, address form Sie).
- **Scope Restriction:** Track A is desktop-only at 1440px viewport matching GPT mockup; mobile is strictly deferred. Track B (design-intense interactive showpiece) is a separate workflow.
