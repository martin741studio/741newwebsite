# 3.1–3.7 Build Note: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Skill Locations: `.claude/skills/cro-homepage/` & `~/.claude/skills/cro-homepage/`

---

## 1. Directory Structure (Step 3.1)
```
.claude/skills/cro-homepage/
  SKILL.md                       # Checklist body (127 lines, < 500 limit)
  assets/                        # Run checklist, intake form, templates
  scripts/
    guard_upload.py              # PreToolUse hook preventing accidental server upload
    verify.py                    # Verification script (structure, tags, schema, links)
    check_prompt.py              # String-match check between prompt and copy
    check_text.py                # Text encoding and copy check
    measure.js                   # DOM metrics (701px hero, font scale, button contrast)
    shot.sh                      # Headless screenshot generator
    stage_drive.py               # Drive manifest packager
    check_drive.py               # Drive manifest validator
  tests/                         # Test scenarios T1–T6
```

## 2. Frontmatter Contract (Step 3.2)
- WHAT + WHEN clearly stated.
- Negative triggers: `Do NOT use for Track B design-intense runs ("track B", showpiece, motion-heavy pitch), SEO content specs (seo-page-optimizer), review pages (local-seo-review-page), backlink work (backlink-dach), or copy for one practitioner page without a prototype (behandler-seite).`

## 3. Checklist & Gates (Step 3.3)
- Checkpoint 1: Copy approval (`04-copy/copy.md`, HWG/BRAO pass, G1–G6 gates via `content-writing`).
- Checkpoint 2: Prototype self-check passed at 1440px viewport + Chrome visual check.

## 4. References & Conciseness (Step 3.4)
- Master reference: `00_project/cro-homepage-workflow.md` (TOC included).
- Motion spec: `00_project/cro-homepage-motion-spec.md`.
- Visual check: `00_project/cro-homepage-visual-check.md`.
- `SKILL.md` is 127 lines.

## 5. Verification Step (Step 3.5)
- Automated verification loop via `python3 scripts/verify.py <cro-dir>`.
- Mandatory Chrome visual check statement.

## 6. 741 House Rules (Step 3.6)
- Prototypes local only; upload guard hook enforced.
- Drive link and screenshot sent in final report.
- Direct-response copy prompts, zero method names in client deliverables.

## 7. Unattended Rules (Step 3.7)
- Skipped: CRO Homepage is an interactive workflow with Martin checkpoints (CP1 copy, CP2 prototype).
