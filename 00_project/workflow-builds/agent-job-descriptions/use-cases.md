# Use cases — agent-job-descriptions (2.1)

## UC1 Write the first job descriptions for the unattended agents
Trigger: "/agent-job-descriptions" or "write job descriptions for the night shift and the morning grill".
Steps: load roster → pick agents (card) → for each agent: read its real prompt/skill/memory, fill the block (R1.1) from evidence, mark every never-line with its rung, rate tools → validator passes → show the description → Martin's go (card with "Go") → place it at the agreed rung (Q2) → roster line → `_run.json`.
Tools: Read/Grep on skills and scheduled tasks, registry script, `scripts/validate_jd.py`, `scripts/roster.py`, AskUserQuestion.
Deliverable: one `agent-jobs/<agent-id>.md` per agent, `agent-jobs/roster.md` + `roster.json`, the placed copy (rules file or scheduled-task header).

## UC2 Weekly review of all agents with a description
Trigger: "/agent-job-descriptions review" from the morning grill on the review day, or "wöchentliches Agenten-Review".
Steps: for each agent: collect evidence since last review (`_run.json`, git log for its files, grill ledger, scheduled-task run list, night-shift REVIEW.md) → draft the review (shipped / wrong / needs from Martin / stale rule / proposals) → one card per agent with the draft and a grade proposal from evidence → Martin grades A–F in one sentence or accepts → mistakes seen twice get a rung decision card → write `agent-jobs/reviews/<week>/<agent-id>.md`, update roster (last grade), apply approved rung fixes (memory line / rule / skill edit; hook edits need a separate go).
Tools: scripts/collect_evidence.py, AskUserQuestion, registry.
Deliverable: review files, roster update, applied fixes with evidence.

## UC3 Add a description for a new client chat from the template
Trigger: "Stellenbeschreibung für den Hüwel-Chat" / "job description for the Stürzl chat".
Steps: load the client template (role, goal, duties, risk list with client-specific never-lines such as "Ayurveda page untouchable" for Suriya) → fill from the client memory + roadmap → validator → card → place.
Deliverable: `agent-jobs/client-<slug>.md` + roster line.
