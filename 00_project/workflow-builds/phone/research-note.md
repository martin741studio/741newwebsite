# Research Note: Maps Growth Playbook

Workflow ID: phone
Name: Maps Playbook 77-Measures
Date: 2026-10-16
Owner: Martin

## 1. Building Block Chosen
- **Block:** Claude Code Skill (`.claude/skills/maps-playbook/`) with deterministic scripts in `scripts/`.
- **Reason:** The Maps Playbook evaluates a standardized 77-measure growth matrix across 3 surfaces (Google Profile, Website, Off-Page Citations/Links). Computing matrix cell statuses, gap scoring, and Excel/HTML board generation requires deterministic Python execution (`validate_catalog.py`, `build_sheet.py`, `render_board.py`, `score.py`), while task prioritization and copywriting recommendations require qualitative agent heuristics.

## 2. Library Search & Rules Applied
- Searched `00_project/knowledge/workflow-library/` for local SEO ranking factors, Google Maps 3-pack optimization, and phased campaign execution playbooks.
- Three critical rules selected from `_derived/rules.md`:
  1. **Rule R1.7 (Degrees of Freedom):** Fragile computations (score calculations, catalog validation, Excel generation) live in scripts; qualitative strategic recommendations live in `SKILL.md`.
  2. **Rule R2.7 (Checkpoints):** Explicit stops at Checkpoint A (Martin reads board), Checkpoint B (Martin releases client bundle), and Checkpoint C (Martin approves execution batch).
  3. **Rule R8.3 (Real Evidence Only):** Every cell in the 77-measure matrix requires proof: an audit field link, a live check, or an explicit `[FEHLT]` tag. Typing guessed numbers is strictly forbidden.
- One pattern selected from `_derived/patterns.md`:
  - **Pattern §4.1 (Sequential Workflow with Phased Gates):** Audit Feeds $\to$ Harvest $\to$ Matrix $\to$ Tasks $\to$ Client Bundle $\to$ Batch Execution.

## 3. Freshness & Invariant Standards
- Library sources verified (< 3 months freshness).
- Compliance with Google Maps ranking guidelines and local pack algorithms.
- Core 5 quantitative channels respected: Local Falcon reports (free/cached), GSC, Google Ads.

## 4. Existing 741 Assets Reused
- Audit workflow (`audit`): feeds 69 of the 77 measures directly from `findings.json`.
- Un-burning workflow (`unburning`): provides `harm-register.json` to lock growth measures that touch damaged areas.
- 77-measure catalog: `00_project/maps-playbook-measure-catalog.json`.
- 6 deterministic scripts in `00_project/maps-playbook-skill/maps-playbook/scripts/`.
