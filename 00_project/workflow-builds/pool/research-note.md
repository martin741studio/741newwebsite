# Content Pool & Sitemap Research Note

Workflow ID: pool
Name: Content Pool & Sitemap
Date: 2026-10-16
Owner: Martin

## 1. Building Block Chosen
- **Block:** Claude Code Skill (`.claude/skills/content-pool/`) + Isolated Python Scripts (`scripts/`).
- **Reason:** Content pool analysis requires high-context qualitative judgment (evaluating clinical/legal fit, search intent, audience separation) coupled with deterministic computational tasks (SERP scraping, Google autocomplete tree generation, HTML report rendering, schema validation). A skill with script separation provides the exact degree-of-freedom boundary mandated by Rule R1.7.

## 2. Library Search & Rules Applied
- Searched `00_project/knowledge/workflow-library/` for SEO, keyword research, competitor analysis, and sitemap patterns.
- Three critical rules selected from `_derived/rules.md`:
  1. **Rule R1.7 (Degrees of Freedom):** Fragile computations (word counts, search volume calculations, priority scoring) live strictly in isolated Python scripts; qualitative synthesis (fit score, intent, copywriting angles) lives in `SKILL.md`.
  2. **Rule R2.7 (Checkpoints):** Explicit stop at Checkpoint 1 (Pool HTML report approval) and Checkpoint 2 (Sitemap approval) before any downstream work proceeds.
  3. **Rule R1.1 & R1.2 (Frontmatter & Negative Triggers):** Strict negative triggers against `seo-page-optimizer`, `cro-homepage`, `sitetree`, `behandler-seite`, and `backlink-dach`.
- One pattern selected from `_derived/patterns.md`:
  - **Pattern §5 (Standard Skill Directory Structure):** `SKILL.md` (< 500 lines) + `scripts/` + `references/` + `assets/`.

## 3. Freshness & Invariant Standards
- Library sources reviewed and verified (< 3 months freshness).
- Compliance with German regulations: HWG (Heilmittelwerbegesetz) for healthcare practices; BRAO/UWG for legal practices.
- Data channels: DataForSEO organic SERP + Google Autocomplete + GSC queries (core 5 channel alignment).

## 4. Existing 741 Assets Reused
- Existing dry runs: `00_project/assets/dumann/content-pool/`, `00_project/assets/suriya/content-pool/`, and `00_project/assets/balihealing/content-pool/`.
- 10 deterministic Python scripts in `00_project/content-pool-skill/scripts/` (`build_pool.py`, `build_sitetree.py`, `autocomplete_tree.py`, `validate_pool.py`, `render_report.py`, etc.).
- Martin character guide callouts per `00_project/assets/brand/martin-guide/README.md`.
