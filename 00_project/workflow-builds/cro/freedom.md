# 2.5 Degrees of Freedom: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Workflow: CRO Homepage Track A (`cro`)
Standard: Rule R1.7 Separation of Deterministic Math/APIs vs Qualitative Heuristics

---

| Workflow Component | Execution Nature | Implementation | Governance / Script |
|---|---|---|---|
| **Server Upload Guard** | Deterministic | `scripts/guard_upload.py` | PreToolUse hook intercepts any command attempting rsync, scp, or ftp toward live servers. |
| **Copy Prompt Alignment** | Deterministic | `scripts/check_prompt.py` | Verifies exact string matching between design prompt and approved copy file. |
| **DOM Measurement** | Deterministic | `scripts/measure.js` | Measures viewport heights, button contrast, and typography sizes via JavaScript in Chrome. |
| **Prototype Verification** | Deterministic | `scripts/verify.py` | Enforces mandatory tags, meta tags, schema markup, and image dimension ratios. |
| **Drive File Staging** | Deterministic | `scripts/stage_drive.py` & `check_drive.py` | Hashes and manifest-checks files before and after upload. |
| **Registry & Excel Rebuild**| Deterministic | `00_project/cro-registry/build.py` | Compiles registry records into `Workflow-Uebersicht.xlsx`. |
| **Conversion Copywriting** | Qualitative | `content-writing` Skill | Guided prompt heuristics for headline hooks, objection handling, and client voice. |
| **Visual Hierarchy & Layout**| Qualitative | `SKILL.md` + Motion Spec | Visual composition of sections, whitespace balance, and architectural typography. |
| **Chrome Visual Inspection**| Qualitative / Heuristic| `cro-homepage-visual-check.md` | Human/agent eye check for clipping, overlap, and aesthetic wow-factor. |
