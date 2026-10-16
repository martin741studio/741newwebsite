# 2.3 One Real Task Solved by Hand: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Clients: Daniela Dumann (Osteopathie München) & Aydan Adel (Psychotherapie Berlin)
Workflow: CRO Homepage Track A (`cro`)

---

## 1. Real Pilot Execution Context
- **Task:** Build complete conversion-optimized desktop prototypes from raw live site URLs, GBP profiles, and brand assets.
- **Pilot 1 (Daniela Dumann):** Osteopathy practice in Munich. Live site lacked direct conversion paths and mobile-first proof. Hand-coded 1440px desktop HTML prototype with 701px hero, proof hover, and WhatsApp booking trigger.
- **Pilot 2 (Aydan Adel):** Psychotherapy practice in Berlin. Evaluated via fresh reviewer agent at Checkpoint 2.

## 2. Hard Context Extracted During Hand Runs
1. **Accidental Server Upload Risk:** During manual staging, an agent almost executed an rsync command toward a live server. We immediately developed and installed `scripts/guard_upload.py` to intercept and block any server upload commands.
2. **Reviewer Evaluation Findings (Adel Run):** Running a fresh reviewer subagent at Checkpoint 2 caught 12 real gaps that self-evaluation missed:
   - Score inflation on copywriting clarity.
   - One incorrect phone number transposed from old website footer.
   - Broken anchor link on proof badges.
3. **Copy Gating Dependency:** Writing copy directly inside the CRO prompt caused AI slop and weak local relevance. We codified Step 3 to strictly delegate copywriting to the `content-writing` skill (`run_gates.py` G1–G6).
4. **Drive Mirror as Resumable Home:** Runs often span across multiple sessions. Staging state into `00_project/assets/<client>/cro/` and mirroring to Google Drive with `_status.md` allows seamless resumption at any step without re-crawling.

## 3. Impact on Skill Architecture
- Hard requirement for `verify.py` passing before reporting done.
- Mandatory Chrome visual check line ("Visual check done in Chrome, N items checked, N fixed, N open").
- Mandatory Drive upload guard hook.
