# Baseline comparison (Step 4.3) — agent-job-descriptions, 2026-11-03

## Without the skill (a plain "give the night shift agent a job description" request)
- The block would be recalled from the video vocabulary (title, duties, do-not list, Friday grade): 7 parts, no rung per never-line, no tool risk rating, no report shape, no caps, no edge cases. The research shows exactly those missing parts are where agents drift (sources 09, 10, 11).
- The "do not" lines would be prose in a memory file; nothing would state which of them the go-gate really blocks. A chat would later report "blocked by the hook" for an action the regex does not match.
- The agent would be asked to grade itself A–F; source 10 shows that grader is biased, so the grade would be noise.
- No roster: the same agent would get two descriptions from two chats (this build found 8 agents and no joined list).
- No validator: a description with a missing section ships; copies in a scheduled task drift from the source with nobody noticing (source 10, "copies drift").
- Approvals: a second approval mechanism would be invented ("leave an approval card") next to the existing go-gate and decision cards.

## With the skill
- 15 fixed sections, validated by `validate_jd.py` (14 checks). The first real description (webdev) failed 3 checks on the first pass and passed after the fixes; all three were real gaps (an unrated tool, a Go section with no named card actions, no missing-source rule).
- Every never-line carries its rung; the Web Developer description has 2 hook-enforced lines and 7 advisory lines and says so.
- Two gate lists per agent map onto `live_change_gate.py` and the card Go; nothing new to maintain.
- Roster (`roster.json`, 8 agents, ids fixed), inbox/outbox handoff convention, evidence collector for the review (tested on the night shift: 3 REVIEW.md files and one ledger entry found, one unreadable path reported as such).
- Tool calls for one description in this build: 1 roster list, 3–6 reads of the real prompt/skill/memories, 1–3 card rounds, 1 write, 1–2 validator runs, 1 card Go, 1 place run, 1 copies check, 1 roster set+render. Bounded and repeatable.
- Corrections during the build: 1 (Martin redirected the first agent from the unattended set to a new Web Developer agent). Now a `## Critical`/step-1 rule: new agents enter the roster first, the roster is read before any draft.

## Corrections avoided going forward
- A description that names a video or creator source is rejected by the validator (house rule: no method sources).
- A never-line without a rung is rejected, so "it is blocked" claims without a hook cannot ship.
- A scheduled task whose header drifted from the source fails `validate_jd.py --copies`.
