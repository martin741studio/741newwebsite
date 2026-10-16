# Research Note: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Owner: Martin Drendel
Workflow: CRO Homepage Track A (`cro`)

---

## 1.1 Building Block Selection
- **Chosen Block:** **Skill (`~/.claude/skills/cro-homepage/`) with isolated Python/Shell verification scripts and upload guard hook.**
- **Reason:** CRO Homepage blends complex editorial/copywriting gates (via content-writing skill), visual layout critique, and HTML prototype generation with deterministic verification scripts (`verify.py`, `shot.sh`, `check_prompt.py`, `guard_upload.py`).

## 1.2 Library Search
- Searched in `00_project/knowledge/cro-library/` and `workflow-library/`:
  - `rules.md`: Desktop-first at 1440px; first screen at 701px viewport; proof hover; direct-response headlines.
  - `patterns.md`: Checkpoint 1 (copy approval) & Checkpoint 2 (prototype approval); Drive resumable home.
  - `scorecard.md`: 54-point scorecard grid; required elimination of blocking zeros D5 (trigger tests) and D6 (baseline).

## 1.3 Freshness Rule
- Master knowledge library `INDEX.md` and `cro-library` derived rules are fresh (< 1 week old). Motion spec and visual check checklists approved and active.

## 1.4 Existing 741 Assets Check
- Master Spec: `00_project/cro-homepage-workflow.md` (53 KB exhaustive spec).
- Motion Spec: `00_project/cro-homepage-motion-spec.md`.
- Visual Check: `00_project/cro-homepage-visual-check.md`.
- Registry & Spreadsheet: `00_project/cro-registry/registry.json`, `build.py` syncing `Workflow-Uebersicht.xlsx`.
- Pilots Verified: Daniela Dumann, Aydan Adel.

## 1.5 Research Note & Scope Boundaries
- **Track A vs Track B:** Track A is the standard conversion-optimized desktop prototype. Track B (design-intense interactive pitch) is strictly separate.
- **Upload Safety:** Prototype files must NEVER be deployed to live client servers without Martin's explicit written approval.
- **Gating Upgrade:** Formalize trigger tests and baseline to remove blocking zeros and raise scorecard from 80% to $\ge 90\%$.
