# Inputs grill — content-format-board

Date: 2026-10-24. Martin's answers (AskUserQuestion round 1).

## Job
Input: a client name (running client) or a prospect name (for a pitch).
Transform: research the client/prospect's field, find real public questions their audience asks, map their situation onto a verified proven-format taxonomy, and write concrete execution steps, a quality bar, and a plan for who at the client appears on camera.
Output: a brainstorm-and-reference board (markdown + optional sheet) per client/prospect. Ideas only — no scripts, no final copy, no captions.
Who uses it: Martin, for a pitch deck (prospect) or for planning a running client's content batch. A later step (content-writing, or a human) turns one chosen idea into an actual script.

Boundary decision (confirmed): **Board only.** This workflow never calls personal-posts and personal-posts never calls this workflow. personal-posts stays scoped to Martin's/741's own accounts; this workflow stays scoped to client/prospect output. No shared module between them — client content must never carry 741's own brand voice, and a shared dependency risks that leak.

## Runtime Surface
Terminal / Claude Code skill. Same architecture as `cro-homepage`, `personal-posts`, `local-seo-review-page`: lives at `.claude/skills/content-format-board/`, triggered inside a client or prospect chat.

## Cadence
On demand, per client or prospect. No schedule. Triggered when Martin preps a pitch, or plans a running client's next content batch.

## Hard Limits
Workflow-specific limit confirmed by Martin: **no outside-method-name leakage** — "Alex Garcia", "One Shot", "Ten Shot", "Yapping" or any named external framework stays internal-only; client/prospect-facing text uses 741's own neutral labels (per `no-method-sources-in-deliverables`).

Inherited house rules that apply regardless (not re-asked, already standing hard rules):
- No auto-publish — every idea is a proposal, never a script/caption that gets posted without a go (`no-website-changes-without-go`, `feedback-always-draft-the-message`).
- No invented reference examples — if a cited example 404s or can't be verified live, say so; never substitute a plausible-sounding fake (`never-invent-contact-history`, `claims-need-real-data`).

Not selected: a hard research-spend cap on DataForSEO/Apify/YouTube-scrape calls per run. Not baked in as a blocking rule; the build should still keep an eye on call volume per run and report it, but it is not a gate.
