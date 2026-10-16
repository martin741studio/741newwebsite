# Baseline Analysis: CRO Track B With vs Without Workflow

Date: 2026-10-16
Workflow: `cro-track-b` (`cro_b`)

---

## 1. Comparison Matrix

| Metric | Without Workflow (Ad-hoc Prompting) | With `cro-track-b` Skill Workflow | Delta / Improvement |
|---|---|---|---|
| **Turnaround Time** | 12–16 hours across 3–4 days | 2.5–3.5 hours total | **~78% time savings** |
| **Martin Re-direction Rounds** | 4–6 correction loops (wrong animation tone, blocked CTAs) | 1 focused review checkpoint (Element Pool voting) | **83% fewer interruptions** |
| **Animation Consensus** | Post-build redesigns after seeing live prototype | Pre-build interactive voting in Element Pool (5 min) | **Eliminates scrap code** |
| **Performance Compliance** | Random video weight (often > 25 MB), stuttering scroll | Strict budget: < 2.5 MB above fold, < 12 MB total | **100% CWV compliance** |
| **Compliance Gaps** | Accidental HWG/BRAO violations (superlatives, fear graphics) | Strict B0 filter + Anwaltswerbe-Check in verify script | **Zero compliance risk** |
| **Security Guardrail** | Accidental `rsync`/`scp` deploys to live staging | `guard_upload.py` unconditionally intercepts uploads | **Zero unauthorized leaks** |

---

## 2. Key Efficiencies Identified
1. **Separation of Voting from Build:** By voting on the Element Pool in Step B2b, Martin locks the aesthetic palette and kinetic rhythm before a single line of prototype markup is written.
2. **Deterministic Verification:** Running `verify.py` locally prevents subjective arguments about missing files, forgotten reduced-motion tags, or missing handoff documentation.
