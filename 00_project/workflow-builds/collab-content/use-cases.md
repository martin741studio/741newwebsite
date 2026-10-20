# Use Cases: Co-Marketing & Backlink Collaboration Workflow (`collab-content`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `collab-content`

---

## Use Case 1: End-to-End Reciprocal Co-Marketing Article Pair
- **Trigger:** "Starte Backlink-Kollaboration für <Kunde> mit <Partner-Domain>" or `/collab-content <client> <partner-domain>`
- **Prerequisites:** Client baseline exists in `00_project/assets/<client>/`. Partner domain is accessible online.
- **Steps:**
  1. Ingests client profile (services, geographic anchor, USP, target audience) and partner site (structure, offerings, authority).
  2. Runs synergy extraction: Identifies complementary, non-competing value intersections and audience crossovers.
  3. Formulates a Mini-Pool of 2–3 specific collaboration angles (titles, core thesis, mutual link targets).
  4. Presents angles to Martin via Decision Card for explicit selection (Checkpoint 1).
  5. Drafts Article 1 (for client site, featuring partner) and Article 2 (for partner site, featuring client).
  6. Runs deterministic compliance and plain-text linter (`scripts/lint_collab.py`).
  7. Stages deliverables in `00_project/assets/<client>/collab/<partner-slug>/` and halts for Martin's Go (Checkpoint 2).
- **Tools:** `read_url_content`, `view_file`, `write_to_file`, `ask_question`, `run_command` (`python3 scripts/lint_collab.py`).
- **Result:** Two publication-ready, YMYL-compliant editorial guides with natural contextual backlinks and zero plain-text CMS errors.

---

## Use Case 2: Synergy & Mini-Pool Formulation (Pre-Outreach Screening)
- **Trigger:** "Welche Kooperationen machen für <Kunde> mit <Partner> Sinn?" or "Analysiere Backlink-Potenzial zwischen <Kunde> und <Partner>"
- **Steps:**
  1. Scrapes partner domain and extracts core service pillars, location, and guest-post posture.
  2. Compares with client baseline to detect synergy vs. direct competition.
  3. Generates structured Mini-Pool matrix: Geographic synergy, Modality pairing, Mutual value proposition, Proposed backlink anchor texts.
  4. Returns executive summary with 2–3 pitch angles for Martin to use in direct partner negotiations.
- **Tools:** `search_web`, `read_url_content`, `view_file`.
- **Result:** High-leverage partner dossier and pitch angles created before writing full articles.

---

## Use Case 3: Inbound Guest Post Review & CMS Staging
- **Trigger:** "Partner <Name> hat den Gastartikel geliefert, prüfe und bereite vor" or "Review Collab-Entwurf von <Partner>"
- **Steps:**
  1. Ingests partner's drafted article.
  2. Checks for Google YMYL compliance (no forbidden disease cure claims, no spammy exact-match money anchors).
  3. Lints for plain text (strips raw `<span>`, `<div>`, inline styles that break client WordPress/Wix editors).
  4. Verifies outbound links to partner are contextually relevant and safe.
  5. Stages clean plain-text version in `00_project/assets/<client>/collab/<partner-slug>/inbound_approved.md`.
- **Tools:** `view_file`, `run_command` (`python3 scripts/lint_collab.py`).
- **Result:** Safe, linted, client-ready content staged for CMS publishing.
