# Research note — agent-job-descriptions

## 1.1 Building block
Skill, triggered in chat (`/agent-job-descriptions` or "write a job description for <agent>", "Stellenbeschreibung für <Agent>"). Reason: one repeatable procedure Martin triggers with him present (cards decide scope, gate, manager), no fixed schedule for the writing itself (R0.2, patterns §3 step 3). The weekly review is a second entry mode of the same skill (`/agent-job-descriptions review`), run from the morning grill on the review day, not a separate routine (R0.7 would say routine only if nobody is present; the review needs Martin's grade). `disable-model-invocation: true`: the skill writes files that other agents load every session (rules/skill files), which is a side effect on the whole system.

## 1.2 Library search
`grep -ril "approval\|self-review\|job description" 00_project/knowledge/workflow-library/` — hits in rules.md (R0.1 CLAUDE.md vs skill, R0.5 hooks for zero-exception rules, R2.10 disable-model-invocation, R3.7 preferences/state stores, R4.5 adversarial review in a fresh context, R6.x unattended rules), patterns §4.1 (sequential workflow with gates), blog/building-effective-agent-automations.md, official-docs hooks-guide.md / sub-agents.md / memory.md. No existing pattern is a "job description"; the closest in-house precedent is the night-shift v2 prompt set and the scheduled-task SKILL.md files.

## 1.3 Freshness
workflow-library INDEX.md: built 2026-10-11, next refresh due 2026-11-22 — inside the 6-week window, no refresh. New library `agent-job-library` built today from sources dated 2026-01-15 to 2026-11-02; the OpenAI practical guide (2026-01-15) is older than 3 months but is the living web version of a reference guide, kept with that note.

## 1.4 Existing assets
See `coverage-map.md`. Summary: 741 already has the enforcement layer (go-gate hooks), the manager layer (morning grill cards + ledger), telemetry (registry `_run.json`), and per-agent prompts for scheduled tasks. Missing: a written scope per agent, a roster, a weekly per-agent review, and the mapping of never-lines to their enforcement rung.

## 1.5 This note
Block: skill with two modes (write, review). Three rules that shape the build: R1.4 (every never-line names its rung), R4.2 (grade from outside, from evidence), R2.3 (hook-enforced vs card-enforced lists, no second gate). One pattern: patterns §4.1 sequential workflow with gates, plus §4.4 plan-validate-execute for the install step (a validator checks every description before it is placed where an agent loads it). Open questions: see `_derived/agent-job-descriptions-questions.md` Q1–Q7 (cards at CP1).

## 1.6 Knowledge base (shown at Checkpoint 1)
(a) Library folder: `00_project/knowledge/agent-job-library/` — 13 sources local (INDEX.md), full transcript of the video as source 01, vendor pages 03–06, framework 07, two pointers into the existing workflow-library (08, 09), two practitioner essays (10, 11), one unverified claim recorded as such (12), the 741 internal inventory (13).
(b) Still to export: nothing required. Optional: the "12-block" X post (not locatable; Martin may have it) and Tyler Phillips' X posts (x.com unreadable from this machine).
(c) Derived layer written: `_derived/agent-job-descriptions-rules.md` (43 IF/THEN rules, one source per line), `_derived/agent-job-descriptions-questions.md` (8 answered, 7 open for CP1, 3 later), `_derived/roster-2026-11-03.md` (A1–A7 unattended, B1–B7 standing chats, C tools).
Verdict on the video: vocabulary right, enforcement/evidence/manager/roster/change-control missing; the research fills each gap and 741 must map onto its existing layers instead of building them twice.
