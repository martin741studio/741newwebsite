# Trigger and function tests for `cro-homepage` (rules R1.2, R4.7, R4.8)

Run in a fresh session (new Claude Code session, only the skill list loaded). Mark the result and the date in the table. Fix the description, not the body, when triggering is wrong.

| # | Message to Claude | Must the skill load? | Expected behaviour | Result / date |
| --- | --- | --- | --- | --- |
| T1 obvious | "Run the CRO workflow for Praxis Muster, https://praxis-muster.de, GBP link, contact by WhatsApp 0170 1234567" | Yes | Reads `00-lead-info.md` or creates the folder, reads the workflow doc, starts at Step 0, does not ask for anything already given | not run |
| T2 paraphrase | "Mach mir einen Prototyp für die Startseite von Kanzlei Beispiel, www.kanzlei-beispiel.de, ich will mehr Anfragen" | Yes | Treats it as the CRO workflow, asks only for missing channel (default rules in `assets/templates/intake.md`) | not run |
| T3 must not trigger | "Write the SEO page text for the service page Erbrecht Bonn with keywords and FAQ" | No (seo-page-optimizer) | Does not start a CRO run | not run |
| T4 must not trigger | "Let's do track B for Studio Muster, I want a wow site with motion" | No (Track B) | Reads the Track B workflow and starts the grill-me questionnaire | not run |
| T5 must not trigger | "Build the Local-SEO review page for prospect X" | No (local-seo-review-page) | Does not start a CRO run | not run |
| T6 resume | "Continue the CRO run for Adel" | Yes | Reads `_status.md` of the run folder, continues at the named next step, never restarts at Step 0 | not run |

## Function test (one real task)
Use a finished run as the reference: `00_project/assets/adel/cro/`. In a fresh session, ask the skill to re-run `scripts/verify.py` and `scripts/check_text.py` against it. Expected: 24 pass, 0 fail (with `--allow "Prototyp: Bilder"`).

## Baseline log
Per real run write one line in `00_project/cro-registry/run-metrics.md` (minutes, Martin's corrections, score). After 5 runs compare with and without the new scripts.
