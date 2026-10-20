# Step 0.0 Inputs Grill Record: Sales Call & High-Ticket Pitch Architecture (`sales-pitch`)

Date: 2026-10-17  
Owner: Martin Drendel  
Workflow ID: `sales-pitch`  
Status: Confirmed via Interactive Decision Cards  

---

## 1. The Job (Objective & Scope)

### What Enters:
1. **Prospect Profile & Intelligence Baseline:**
   - Prospect Name, Domain, Location, Business Niche (e.g. Health, Law, Local B2B).
   - Review-Page Audit Data: Local Falcon Rank-Grid (SoLV), Website Speed / Core Web Vitals, Google Business Profile optimization gaps, Google Search Console / organic traffic gaps.
   - Identified competitor positioning in their direct regional radius.
2. **Prior Touchpoint History:**
   - Lead source (cold outreach, referral, content).
   - Review-Page watch status and WhatsApp pre-call sequence touchpoints (M1–M3).
   - Stated goals or initial pain points expressed in the booking form.

### What Transforms:
1. **60-Minute Tactical Call-Raster (Hybrid Architecture):**
   - **Phase 1 (Min 00–05): Frame & Agenda Setting (Oren Klaff / Hormozi):** Martin establishes calm peer status, removes immediate sales pressure, and frames the meeting as a joint diagnostic review.
   - **Phase 2 (Min 05–20): Deep Discovery & Consequence Diagnosis (Jeremy Miner NEPQ):** Solution-neutral, emotion-uncovering questioning that exposes current bottleneck, past failed agency attempts, and the financial/emotional cost of inaction.
   - **Phase 3 (Min 20–35): The Proof & System Prescription (Gap Selling / 741 Engine):** Grounded presentation of the specific cure (90-Day Local SEO, CRO Landing Page Prototyping, Content Pool, Ads) without "feature vomit", referencing exact audit proof from their Review-Page.
   - **Phase 4 (Min 35–45): The 3-Tier Offer Stack & Price Anchoring (Alex Hormozi $100M Offers):**
     - Anchoring against full-time in-house salary or annual customer lifetime value (LTV).
     - Presenting the 3-Tier Ladder:
       - **Core Offer:** 90-Tage Local SEO & Growth Engine (3.699 €) mit klarer Leistungs-Garantie (Messziel nicht erreicht = kostenlose Weiterarbeit oder Geld zurück).
       - **Upsell:** Power Engine (7.999 €) inkl. Paid Ads Management, High-End CRO Redesign und Content-Cluster.
       - **Downsell:** Starter Setup (1.999 €) für reine technische/Maps-Basisbereinigung ohne Garantie.
   - **Phase 5 (Min 45–55): Systematic Objection Handling (Chris Voss Tactical Empathy / 741 Matrix):**
     - Pre-emptive Accusation Audit ("You probably think this is expensive / risky...").
     - Reframe & Proof protocols for: Budget ("Zu teuer"), Delay ("Muss nachdenken"), Authority ("Partner fragen"), Bad Agency Past ("Schlechte Erfahrungen"), In-House ("Haben schon jemanden").
   - **Phase 6 (Min 55–60): Seamless Close & Immediate Onboarding Kickoff:**
     - Clear decision commitment, setup of agreement, calendar hold for Kick-off, prevention of buyer's remorse.

### Who Uses Output:
- **Martin Drendel:** Uses the generated tailored Call-Cockpit before and during the live 60-minute Zoom/Google Meet call with the prospect.

---

## 2. Runtime Surface

- **Primary Surface:** Multi-Surface Agent Skill (`/sales-pitch <Prospect>` or conversational trigger in Antigravity IDE and Claude Code).
- **Deliverables Generated per Run:**
  - `00_project/prospects/<prospect-slug>/sales-cockpit.md`: A structured 1-page live call cockpit with customized questions, personalized math/LTV calculations, dynamic price anchor, and the top 3 anticipated objections with custom rebuttals.
  - Telemetry record in `_run.json`.

---

## 3. Cadence & Frequency

- **Mode:** On-Demand / Just-In-Time.
- **Trigger:** Whenever Martin has an upcoming sales call or runs `/sales-pitch <prospect>`. Never scheduled unattended.

---

## 4. Hard Limits & Invariants

1. **Zero Sleazy / High-Pressure Closing Tactics:** No artificial urgency ("Preis gilt nur heute"), no manipulative pressure. Authority and conviction come from factual data (Local Falcon, Speed-Audit, Case Proofs).
2. **Strict Risk Reversal Discipline:** The 90-Day Guarantee (3.699 €) must be tied to objective, transparent metrics (e.g. Top-3 Local Falcon rank improvement, verified rankings), never vague subjective goals.
3. **No External Guru Names in Prospect-Facing Assets:** Martin references the "741 Call-Raster" and "741 Wachstums-System", never Hormozi, Miner, or Voss.
4. **Data Anchoring Invariant:** Every financial calculation in the call cockpit must be derived from the prospect's actual average ticket value / patient lifetime value.
