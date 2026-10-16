# Research Note: Backlink DACH Workflow

Workflow ID: backlink
Name: Backlink DACH (Link Building)
Date: 2026-10-16
Owner: Martin

## 1. Building Block Chosen
- **Block:** Claude Code Skill (`.claude/skills/backlink-dach/`) with deterministic scripts in `scripts/`.
- **Reason:** Link prospecting, competitor gap analysis, and target qualification require structured data fetching from DataForSEO, CSV/XLSX generation, and strict gatekeeping (`disable-model-invocation: true`). Human execution of outreach is mandatory (zero automated sending).

## 2. Library Search & Rules Applied
- Searched `00_project/knowledge/link-library/` and `_derived/rules.md` for DACH link building standards.
- Three critical rules selected from `_derived/rules.md`:
  1. **Rule R1.7 (Degrees of Freedom):** Fragile computations (gap analysis math, Google Sheet workbook generation, DataForSEO parsing) live in scripts; outreach angle copywriting and qualification heuristics live in `SKILL.md`.
  2. **Rule RH.4/RH.5 (Fixed Local Priority):** Fixed local priority: IHK/HWK (if Gewerbe) $\to$ Berufsverband $\to$ distance to client address.
  3. **Rule R8.2 (Approval Gate):** Every target sheet row requires an explicit `Freigabe` checkbox. The agent never sends outreach or pays.
- One pattern selected from `_derived/patterns.md`:
  - **Pattern §4.1 (Sequential Workflow with Checkpoint Gates):** Harvest $\to$ Gap Analysis $\to$ Sheet Generation $\to$ Martin Approval $\to$ Human Outreach.

## 3. Freshness & Invariant Standards
- Library sources verified (< 3 months freshness).
- White-hat DACH only: zero PBNs, zero hidden sponsored posts (`[KENNZEICHNUNG]` mandatory for paid links).
- Pillar A border: Directories belong exclusively to the Citations module (`citations-dach`).

## 4. Existing 741 Assets Reused
- DataForSEO API client in `scripts/gap-analysis.mjs`.
- XlsxWriter sheet builder in `scripts/build_sheet.py`.
- Run telemetry writer in `scripts/write_run.py`.
- Hüwel pilot target dataset in `00_project/assets/huewel/backlinks/`.
