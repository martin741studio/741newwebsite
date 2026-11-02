# Test scenarios — agent-job-descriptions (2.2, written before the body)

## T1 Obvious trigger (must load)
Prompt: "/agent-job-descriptions — write the job description for the night shift agent."
Expected: skill loads; reads the roster; reads `reporting/night-shift-v2/` prompts and the memory `night-shift-server-workflow`; drafts the block with every never-line marked hook/runner/advisory; runs the validator; shows the draft; asks one card with a "Go" option before placing anything.

## T2 Paraphrased trigger (must load)
Prompt: "Der Morning-Grill-Agent driftet. Gib ihm eine Stellenbeschreibung mit Nie-Regeln und einem wöchentlichen Review."
Expected: same as T1 for the morning grill agent; the review day is taken from the roster config; language per Q6.

## T3 Must NOT trigger
Prompt: "Write a job description for a part-time SEO assistant we want to hire on Upwork."
Expected: the skill does not load (human hiring, not a 741 agent); the chat answers normally or routes to the Upwork memory. Negative trigger in the description: "NOT for human job ads, Upwork/Fiverr briefs, or client staff."

## T4 Must NOT trigger (second negative)
Prompt: "Run the canary check for Marcel." Expected: `/canary` handles it; this skill stays silent.
