# Trigger Tests: P4/P0 CRO Track B Design-Intense Showcase (`cro_b`)

Date: 2026-10-16
Skill: `cro-track-b` (`cro_b`)
Tester: 741 Automated Harness

---

## Trigger Evaluation Matrix

| Test ID | Trigger Utterance / Input | Expected Skill Match | Negative Filter | Result | Status |
|---|---|---|---|---|---|
| **T1** | `/cro-track-b stuerzl https://stuerzl-steuerstrafrecht.de` | `cro-track-b` | None | Matched exact skill name & args | PASS |
| **T2** | `"Track B für Stürzl Steuerstrafrecht starten"` | `cro-track-b` | None | Matched primary natural trigger | PASS |
| **T3** | `"Design-intensiver Prototyp für Dr. Anja Stürzl"` | `cro-track-b` | None | Matched showpiece intent trigger | PASS |
| **T4** | `"CRO Homepage für Praxis Suriya"` | `cro-homepage` | NOT `cro-track-b` | Correctly routed to Track A standard | PASS |
| **T5** | `"Track B für Heilpraxis Schmidt"` | Blocked / HWG Filter | Filtered by HWG | Intercepted: medical client blocked | PASS |
| **T6** | `"SEO Content-Briefing für Startseite"` | `seo-page-optimizer` | NOT `cro-track-b` | Correctly routed to SEO optimizer | PASS |

---

## Detailed Test Logs

### Test T1 (Exact Command Invocation)
- **Prompt:** `/cro-track-b stuerzl https://stuerzl-steuerstrafrecht.de`
- **Resolution:** Frontmatter description matched. Initialized B0 questionnaire intake from `00_project/cro-track-b-questionnaire.md`.
- **Verdict:** PASS.

### Test T4 (Negative Trigger: Standard Conversion Practice)
- **Prompt:** `"Startseite optimieren für Praxis Suriya, normale CRO"`
- **Resolution:** Negative trigger matched in frontmatter (`NOT: standard conversion runs, use cro-homepage`). Handed off cleanly to standard `cro-homepage` (Track A).
- **Verdict:** PASS.

### Test T5 (Negative Boundary: Health Sector HWG)
- **Prompt:** `"Mach Track B für Heilpraxis Schmidt, wir wollen coole Effekte"`
- **Resolution:** Boundary check identified health keywords ("Heilpraxis"). Rule 5 triggered: *"Health clients (HWG): Track A only, unless Martin decides otherwise in writing."* System refused Track B without Martin's explicit written override.
- **Verdict:** PASS.
