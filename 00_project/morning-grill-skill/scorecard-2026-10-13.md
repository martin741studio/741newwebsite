# Scorecard — morning-grill skill draft (2026-10-13)

Scored against `00_project/knowledge/workflow-library/_derived/scorecard.md`. 0 missing · 1 partly · 2 done.

| # | Check | Score | Evidence / gap |
|---|---|---|---|
| A1 | Block fits the job | 2 | Skill + Desktop scheduled tasks (local files needed; routines cannot read the repo, ops rule R32/R33) |
| A2 | Rules in the right place | 2 | Procedure in SKILL.md, standing rules in preferences.md, no CLAUDE.md change |
| A3 | Side effects → disable-model-invocation | 2 | Removed on purpose: the skill only reads, writes its own folder and asks cards; sends nothing. Model invocation lets "Was steht heute an" work |
| A4 | Enabled where it runs | 1 | Not installed yet (needs go); Desktop tasks read `~/.claude/skills/` |
| B1 | 2–3 use cases | 2 | Morning, evening, Monday (SKILL.md modes) |
| B2 | Test scenarios before body | 2 | `test-scenarios.md` T1–T5 |
| B3 | One hard task solved by hand | 2 | Dry run 2026-10-13 with real data |
| B4 | Inputs, deliverable, out of scope | 2 | Spec §0, §3, §15 |
| B5 | Degrees of freedom | 2 | Detectors, ranking, render, validate = scripts; judgment cards = heuristic step |
| C1 | Description WHAT + WHEN + NOT | 2 | yes |
| C2 | Name | 2 | `morning-grill` |
| C3 | Body < 500 lines, references 1 level | 2 | 60 lines; references/ flat |
| C4 | Checklist | 2 | Mode A 10 steps, Mode B 4 steps |
| C5 | Scripts run, errors handled | 2 | scan.py reports unreadable sources; thresholds named as constants |
| C6 | Output template | 2 | brief-template.html, decision-card, goal-sheet, evening-log templates |
| C7 | One term per concept | 1 | "card" vs "decision" mostly consistent; "walk item" new term, defined in spec §5.2a |
| C8 | MCP tools qualified | 2 | allowed-tools lists full names |
| D1 | Check Claude can run | 2 | `validate_brief.py` V1–V7 |
| D2 | Loop stated | 2 | "Fix until it prints PASS" |
| D3 | Unattended runs gated | 1 | Validator gate exists; scheduled tasks not created; L0 propose-only defined, no Stop hook |
| D4 | Evidence in report | 2 | PASS line + brief path + screenshot |
| D5 | Trigger tests passed | 2 | 2026-10-13: T1 slash loads body; T2 "Was steht heute für die Kunden an?" + T3 "Log the day" auto-load the skill; T4 CRO and T5 news do not. Evidence: 00_project/assets/morning-grill/2026-10-13-dryrun/tests/*.jsonl, summary in test-scenarios.md |
| D6 | Baseline | 1 | 2026-10-13: fresh session without the skill, same job: 424 s, 94 tool calls, 2.71 USD, 7 decisions. It read the dry-run files too (not clean). It found 3 old memory deadlines the skill missed → new source S13 deadline sweep; after the fix the skill brief has both urgent ones. Clean baseline (fresh day, no dry-run files) still open |
| E1 | Self-contained prompt, time zone | 2 | WITA in spec, preferences, SKILL |
| E2 | Bookmarks | 1 | Designed (`state/bookmarks.json`); scan takes `--bookmark`, file not written yet |
| E3 | Failed reads = unreadable | 2 | scan.py `src()` |
| E4 | Sent only after confirmation | 2 | Agent never sends; drafts only |
| E5 | Read-only creds, spend cap | 2 | GET-only Supabase reads; spend 0 € in the scan |
| E6 | Preferences re-read, not editable | 2 | preferences.md, rule in SKILL Critical |
| E7 | Runs opened and read | 1 | Planned for the first 3 runs (spec §13) |
| F1 | Client message + Drive link | 2 | n/a internal; message drafts in ```text blocks |
| F2 | Per-change go | 2 | All live changes = cards / walk queue |
| F3 | Verified data | 2 | Every card has evidence; null + define card instead of guesses |
| F4 | STE | 2 | Brief and cards in STE |
| F5 | No method sources | 2 | Internal; none in client material |
| F6 | Runs in overview Excel | 2 | `add-workflow morning` done; `_run.json` in the run folder |
| F7 | Martin guide | 2 | Decided: not in the internal brief (spec §15.6) |

Total: 68 / 74 = **91.9 %**. Blocking zeros: **none**.
Decision: ship (Martin's install go 2026-10-13). Watch the first 3 scheduled runs; clean baseline on a fresh day.
