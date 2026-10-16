# Build Note: 741 House Rules Compliance for CRO Track B (`cro_b`)

Date: 2026-10-16
Workflow ID: `cro_b`
Reference: `_derived/rules.md` and `_derived/patterns.md`

---

## 1. Compliance Checklist

- [x] **Rule R1.1 (Building Block Selection):** Implemented as a clean Skill package (`.claude/skills/cro-track-b`) containing `SKILL.md`, deterministic scripts in `scripts/`, templates in `assets/`, and tests in `tests/`.
- [x] **Rule R1.2 (Frontmatter Precision):** WHAT, WHEN, and strict negative trigger (`NOT: standard conversion runs, health clients under HWG, plain SEO briefs`) specified in frontmatter.
- [x] **Rule R1.3 (Body Length & Depth):** `SKILL.md` is 135 lines (well under the 500-line maximum). References are strictly one level deep.
- [x] **Rule R1.4 (Step-by-Step Checklist):** Body structured as a clear sequential checklist with distinct gates.
- [x] **Rule R1.5 (House Rules & Tone):** ASD-STE100 technical English for agent instructions; German for client deliverables; no vague claims or placeholder text; zero method sources cited.
- [x] **Rule R1.6 (Deterministic Safety & Upload Guard):** Security hook `scripts/guard_upload.py` intercepts remote deployment commands (`rsync`, `scp`, `curl`, `sftp`). Local server `scripts/serve_pool.py` binds strictly to `127.0.0.1`.
- [x] **Rule R1.7 (Degrees of Freedom):** Deterministic verification (`verify.py`), metrics parsing (`measure.js`), and vote saving isolated into scripts; qualitative synthesis bounded in `SKILL.md`.
- [x] **Rule R1.8 (Sensor Loop & Telemetry):** Standardized `_run.json` telemetry emitted at every checkpoint and milestone.
