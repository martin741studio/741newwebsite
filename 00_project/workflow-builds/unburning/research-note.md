# Research Note: Un-Burning Harm Remediation

Workflow ID: unburning
Name: Un-Burning Harm Remediation
Date: 2026-10-16
Owner: Martin

## 1. Building Block Chosen
- **Block:** Claude Code Skill (`.claude/skills/un-burning/`) with deterministic scripts in `scripts/`.
- **Reason:** Remediating harmful digital assets requires strict gatekeeping, plan-validate-execute patterns, and side-effect control (`disable-model-invocation: true`). A skill wrapping deterministic verification and report-generation scripts guarantees safe, reversible executions.

## 2. Library Search & Rules Applied
- Searched `00_project/knowledge/workflow-library/` for digital forensics, harm remediation, duplicate citation removal, and Google profile recovery.
- Three critical rules selected from `_derived/rules.md`:
  1. **Rule R1.8 (Destructive Actions):** Any destructive action (deleting listings, disavowing links, submitting review appeals) requires an explicit plan file (`harm-register.json`), automated pre-validation, execution, and post-verification.
  2. **Rule R8.2 (Per-Change Go):** Live production changes require Martin's explicit Go; one Go never covers downstream changes.
  3. **Rule R8.3 (Real Evidence Only):** Every harm item must cite exact raw evidence (URL, screenshot, API error code). Guesses are strictly forbidden.
- One pattern selected from `_derived/patterns.md`:
  - **Pattern §4.4 (Plan-Validate-Execute):** Scan $\to$ Triage Plan $\to$ Validate $\to$ Martin Go $\to$ Execute $\to$ Verify Bedrock.

## 3. Freshness & Invariant Standards
- Library sources verified (< 3 months freshness).
- Compliance with Google Business Profile policies and search quality rater guidelines.
- Area A (ownership/contracts) strictly managed at onboarding; Un-Burning treats ownership as a read-only precondition.

## 4. Existing 741 Assets Reused
- Audit workflow (`audit`): input diagnosis for yellow/red fields.
- Citations DACH (`citations`): duplicate directory identification and NAP reconciliation.
- Suriya dry run: `00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/`.
- 5 deterministic Python scripts in `00_project/un-burning-workflow/skill-draft/scripts/` (`bedrock.py`, `build_report.py`, `merge_parts.py`, `validate_changes.py`, `validate_run.py`).
