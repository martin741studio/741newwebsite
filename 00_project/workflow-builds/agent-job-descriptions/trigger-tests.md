# Trigger tests (Step 4.1) — fresh Explore subagents, 2026-11-03

Method (same as the marketing-grill and content-format-board builds): five fresh Explore subagents, each reading ONLY the frontmatter `description` of every `.claude/skills/*/SKILL.md`, naming the single skill it would invoke. No task executed.

| # | Scenario | Message | Picked | Result |
|---|---|---|---|---|
| T1 | Obvious | "/agent-job-descriptions — write the job description for the night shift agent." | `agent-job-descriptions` ("night-shift-v2 only runs the night queue and doesn't write job descriptions") | PASS |
| T2 | Paraphrase (German) | "Der Morning-Grill-Agent driftet. Gib ihm eine Stellenbeschreibung mit Nie-Regeln und einem wöchentlichen Review." | `agent-job-descriptions` (matched "the <agent> drifts, give it a scope", "Stellenbeschreibung für den <Agent>") | PASS |
| T5 | Paraphrase (new hire) | "I want to hire a new AI agent that does social media for 741. Give it a title, duties, what it may never do, and a Friday review." | `agent-job-descriptions` (matched "hire a new agent for <job>") | PASS |
| T3 | Negative (human hire) | "Write a job description for a part-time SEO assistant we want to hire on Upwork." | none; AJD explicitly wrong ("Do NOT use for human job ads or Upwork/Fiverr briefs") | PASS (not this skill) |
| T4 | Negative (run the agent) | "Run the canary check for Marcel." | `canary`; AJD explicitly wrong ("not for running an agent's own job") | PASS (not this skill) |

Result: 5/5 on the first draft of the description; no `description` change needed (R4.8).

Observation recorded by three of the five subagents: `disable-model-invocation: true` means the skill never auto-loads on a paraphrase; Martin starts it with `/agent-job-descriptions`. This is intended (R2.10): the skill places files that other agents load every session, which is a side effect on the whole system. The trigger phrases in the description still matter for the `/` listing and for the chat base when it briefs a session.
