# Research Note: Co-Marketing & Backlink Collaboration Workflow (`collab-content`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow ID: `collab-content`

---

## 1.1 Building Block Selection (Patterns §3)
- **Primary Block:** Skill (`.claude/skills/collab-content/SKILL.md` and Antigravity IDE agent skill integration).
- **Secondary Pattern:** Deterministic Python helper script (`scripts/extract_synergy.py` and `scripts/lint_collab.py`) + Checkpoint Gates (R1.7 separation).
- **Rationale:** The workflow executes an interactive, multi-step creative and editorial procedure: ingesting partner profiles, determining topical synergy, generating angle briefs, and writing two reciprocal editorial articles. Creative reasoning and editorial voice belong in guided prompt instructions (`SKILL.md`), while link verification, anchor text validation, and plain-text CMS linting belong in deterministic scripts.

## 1.2 Library Search Results
- Searched `00_project/knowledge/workflow-library/` for `content`, `backlink`, `collaboration`, `eval`.
- Key Patterns identified:
  - `_derived/rules.md` §1 (Design workflow before writing: 2–3 use cases, 3 test scenarios, extract winning context from 1 real task).
  - `_derived/rules.md` §2 (SKILL.md < 500 lines, references 1 level deep, deterministic scripts in `scripts/`, template pattern).
  - `_derived/patterns.md` §4.1 (Sequential workflow with strict gates: Ingestion -> Mini-Pool -> Checkpoint 1 -> Drafting -> Validation -> Checkpoint 2).
  - `official-docs/claude-code/skills.md` (Explicit trigger phrases, negative trigger `NOT:`, strict side-effect isolation).

## 1.3 Library Freshness Check
- Library indexed on: 2026-10-11.
- Freshness status: Active (< 1 week old, well within the 6-week freshness ceiling).
- Next scheduled refresh: 2026-11-22.

## 1.4 Existing 741 Asset Coverage & Reuse
- `00_project/content-pool-workflow.md`: Provides the foundational content pool architecture (demand vs. service matrix). `collab-content` extracts a lightweight "Mini-Pool" focused exclusively on the intersection between the client and a specific external partner.
- `00_project/assets/balihealing/`: Client baseline (`01-client/client-baseline.md`), service catalog (IV therapy, medical ozone, dermatoscopy, TCM), and brand guidelines (Indonesian licensed medical staff, no disease promises).
- `.claude/skills/content-writing/`: Production writing rules (anti-slop linting, HWG/YMYL guardrails, structured headings).
- `00_project/workflow-registry/registry.json`: Central tracking for all 741 workflows and execution telemetry.

## 1.5 Synthesis & Architecture Direction
Traditional reciprocal link swaps ("I link you, you link me") trigger search engine manipulation penalties if low-quality or irrelevant. In local and regional high-ticket wellness ecosystems (such as Bali), the winning standard is **Co-Marketing Editorial Guides**:
1. Zero geographic competition: Coastal Canggu outpatient clinic (Bali Healing) partners with inland Ubud residential retreat (Ayurvedagram Bali).
2. Complementary modalities: Modern Western cellular medicine (IV drips, medical ozone, blood work) integrates with ancient Eastern restoration (Kerala Panchakarma, Ayurvedic Vaidyas, yoga).
3. The workflow codifies this into a 4-stage pipeline: Profile Ingestion -> Synergistic Mini-Pool Formulation -> Angle Selection (Checkpoint 1) -> Reciprocal Article Drafting & Plain-Text Linting -> Delivery (Checkpoint 2).
