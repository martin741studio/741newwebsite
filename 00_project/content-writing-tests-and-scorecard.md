# Content Writing: Tests, Dry Run and Workflow Scorecard

Date: 2026-10-11. Spec: `00_project/content-writing-workflow.md`. Skill: `00_project/content-writing-skill/`, **installed 2026-10-11** in `~/.claude/skills/content-writing/` (Martin's go). Slash command `/content-write` appears in new sessions.

## 1. Test scenarios (written before the skill body, spec section 14)

| # | Type | Status | Result |
| --- | --- | --- | --- |
| T1 | Obvious trigger `/content-write stuerzl Selbstanzeige Leistungsseite` | Not run as a trigger test (skill not installed). Run by hand as the dry run | The dry run followed the path: readiness, brief from pool items, A0, outline, draft, gates. |
| T2 | Paraphrase, blog | Not run | Needs installation and a fresh session. |
| T3 | Paraphrase, health, location page | Not run | Needs installation. |
| T4 | Must NOT trigger: audit of an existing page | Not run | Needs installation. |
| T5 | Must NOT trigger: content pool, CRO prototype | Not run | Needs installation. |
| T6 | Gate test: bad German draft | **PASS** | `tests/run_tests.sh`: fixture-bad fails G1, G2, G3, G4 and G5. fixture-good passes all. 13 of 13 checks. |
| T7 | Blocker test: no pool item, no keyword | Not run | The skill must stop in step 0. Needs installation. |

The skill is installed now. The trigger tests T1 to T5 and T7 still need a fresh session. Note: the skill has `disable-model-invocation: true` (it sends text to OpenAI). So it starts only with `/content-write` or with the chat phrase from the registry. T2 and T3 (paraphrases) therefore do not auto-load the skill by design. Decision for Martin: keep it explicit (recommended) or allow auto-load.

## 2. What the gate scripts proved

| Check | Result |
| --- | --- |
| English linter on German tell text | 5/5 CLEAN (the gap) |
| `deslop_de.py` on the same text | 1/5, and on the dry-run draft 5/5 |
| Cleanse round 1 (dry run) | Claim diff REJECTED it: new `[braucht Zahl]` markers and the client phrase "Wir stehen Ihnen zur Seite" removed. Lint alone said 5/5 CLEAN. |
| Cleanse prompt fix, round 2 and 3 | Round 2: one change. Round 3: no change. Claim diff PASS, lint 5/5. |
| Time per cleanse call | about 60 to 70 seconds (codex, GPT via ChatGPT login) |
| Reviewer round 1 | FIX FIRST, 13 points, including real legal errors (§ 398a condition, statute terms) |
| Reviewer round 2 | 10 closed, 3 new gaps (2 caused by my own edits). All fixed. |

## 3. Dry run: Stürzl, Selbstanzeige (ST-14)

Folder: `00_project/assets/stuerzl/content-writing/selbstanzeige/`. Mode: rewrite. BRAO. Sie, wir.

| Item | Value |
| --- | --- |
| Final copy | **v3 approved by Martin 2026-10-11** (`05-final/page-v3-freigegeben.md`, 1.329 words). **v4** (`05-final/page.md`, 1.576 words) rebuilds the voice from the live website, adds the client's own Selbstanzeige FAQ and two quotes. v4 waits for Martin's look. Also `cms-blocks.txt`, `placeholders.md`, `OPEN-FLAGS.md` |
| Benchmark | Bestand 248 words. Competitor median 1.566 (11 pages). Floor 1.096. |
| Gates | G1 to G5 PASS (`04-gates/gates.md`) |
| Scorecard | 87 of 100, no block fail (`04-gates/scorecard.md`). Soft points come from reviewer round 1. |
| Open placeholders | 2: Erstberatung Pauschale, Rechtsschutzversicherung |
| Cleanse calls | 4 (cap 3 plus one for the v4 revision). The last 10 small wording fixes (reviewer round 2) were NOT cleansed again. Lint 5/5 and claim diff PASS on the final text. |
| Deviation from the workflow | Checkpoint 1 (outline) was not waited for. It is a dry run with local files only. The outline (`02-outline/outline.md`) waits for Martin together with the result. |
| Not done | Render check (the output is Markdown, no HTML preview). Drive upload (no go). Portal page (not asked). |

### Findings that matter beyond this page

0. The live site is the voice source (Martin). It also holds a Selbstanzeige FAQ (sections III and IV) that the first draft had missed. Lesson written into the skill: read the whole live site on the topic, including the FAQ and person page. The live site itself uses BRAO-risky words ("Spezialisierung", "Expertise", "hart in der Sache", "Festpreis"). Flagged in `OPEN-FLAGS.md` A6.
1. The approved Stürzl homepage says "Vergütung nach RVG". The newest client text says "kein RVG, nach Zeitaufwand". The two must match before anything goes live.
2. The live H1 of this page promises "Straffreiheit selbst im Falle von vorsätzlich hinterzogenen Steuern". That is a result promise under BRAO § 43b. The new page drops it.
3. The client's cost text uses "besonders hohe Spezialisierung". Check it before the cost page.
4. Three more live pages (ST-15, ST-16, ST-17) carry almost the same text. The new page replaces them. Redirects need the client's consent.
5. The titles of Dr. Stürzl come from her CV, not from a Kammer proof.

## 4. Workflow scorecard (library `scorecard.md`)

Score 0 (missing), 1 (partly), 2 (done). Ship at 80 % with no 0 in A or D. Section E does not apply (the workflow is not unattended).

| # | Check | Score | Note |
| --- | --- | --- | --- |
| A1 | Block matches the job (skill with scripts) | 2 | |
| A2 | Always-on rules in memory, procedure in skill, enforcement in hooks | 1 | Gates are scripts the skill calls. No hook enforces them. |
| A3 | Side-effect skills set `disable-model-invocation` | 2 | Set in the frontmatter. |
| A4 | Skill available where used | 2 | Terminal use only. Not for Cowork or routines (n/a). |
| B1 | 2 to 3 use cases | 2 | Spec section 14. |
| B2 | Three test scenarios before the body | 2 | Seven written in the spec. |
| B3 | One hard task solved by hand, then extracted | 1 | The dry run came after the skill draft. The rules were extracted from the sibling assets and the Stürzl work. |
| B4 | Inputs, deliverable, out of scope stated | 2 | |
| B5 | Degrees of freedom match fragility | 2 | Scripts for gates. Heuristics for copy. |
| C1 | `description` states WHAT, WHEN, NOT | 2 | |
| C2 | Name kebab-case | 2 | `content-writing` |
| C3 | Body under 500 lines, references one level deep | 2 | SKILL.md is about 110 lines. |
| C4 | Workflow is a checklist | 2 | |
| C5 | Deterministic steps are scripts, no magic numbers | 1 | Scripts run and handle errors. Thresholds (0.7, 3.5, 4) sit in code, not in one config file. |
| C6 | Output template and 2 to 3 example pairs | 1 | Templates exist. Example pairs (before/after copy) are missing. |
| C7 | One term per concept | 2 | |
| C8 | MCP tools fully qualified | 2 | No MCP tools used (n/a). |
| D1 | A check Claude can run | 2 | `run_gates.py`, `tests/run_tests.sh` |
| D2 | Loop stated | 2 | |
| D3 | Unattended runs gated | 2 | Not unattended (n/a). |
| D4 | Evidence demanded | 2 | |
| D5 | Trigger tests passed | **0** | Skill is installed. Tests need a fresh session. |
| D6 | Baseline comparison | **0** | Not done. The dry run is one data point only. |
| F1 | Ends with client message draft and Drive link | 1 | In the skill (step 8). Not exercised: no upload without go. |
| F2 | Per-change go before live changes | 2 | |
| F3 | Every data point verified | 2 | Claim list and G1 script. |
| F4 | STE in replies and working files | 2 | |
| F5 | No method sources in client material | 2 | |
| F6 | Runs show up in the overview Excel | 2 | `add-workflow` done, `_run.json` written, `sync` registered the run. |

Total: 49 of 58 = **84.5 %**. Blocking zeros: D5, D6.
Decision: **fix first.** Install the skill after Martin's final go, run T1 to T5 and T7 in a fresh session, and run one baseline (the same page without the skill, counting corrections, tool calls and tokens). Then re-score. Also add 2 before/after example pairs (C6) and move the thresholds into one config (C5).

## 5. Known gaps

1. Trigger tests and baseline (above).
2. Batch mode is out of version 1.
3. The German tell list is a first list. Martin's vetoes are open ("auf Augenhöhe", "individuell", "transparent").
4. 741.studio voice is open. No run on 741.studio before a voice sheet exists.
5. English copy uses slopmonster's English linter through `deslop_de.py`. No English cleanse prompt yet (the original `cleanse.sh` works for English).
6. Page templates for service, location, cost, FAQ and blog are "draft template, first use". Only the homepage and practitioner page are proven patterns.
7. The CMS blocks follow Elementor-style field names. A WordPress or Joomla client may need different names.
