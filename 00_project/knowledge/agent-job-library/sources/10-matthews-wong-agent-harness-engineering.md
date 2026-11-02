# 10 — Matthews Wong: "AI Agent Harness Engineering: What Research and Real Runs Show"

Type: practitioner essay with 20 cited sources, 2026-10-18. Fetched 2026-11-03.
URL: https://www.matthewswong.com/en/blog/ai-agent-harness-engineering-research/

## Key content
- Agent = Model + Harness (Böckeler). Harness layers: instructions, tools, context, state between runs, deterministic checks, review, runner. Guides steer before; sensors observe after. "Feedback alone gives you an agent that keeps repeating the same mistakes, and feedforward alone gives you one that encodes rules but never finds out whether they worked."
- Same model, different harness, different score (SWE-agent ablations; LangChain 52.8% → 66.5% on Terminal-Bench 2.0 with model fixed). Most common failure: the agent re-reads its own code, decides it looks fine, and stops.
- "An agent saying done is a claim, not evidence." Anthropic: "agents reliably skew positive when grading their own work"; a standalone sceptical evaluator is far more tractable than a self-critical generator. Panickssery/Bowman/Feng (NeurIPS 2024): LLM evaluators recognise and favour their own outputs.
- His sensors: judge a run by what landed (merged to main), not by exit code; a test-count gate against the merge-base; a separate review invocation that sees only the diff, on a different model. "A test the broken version also passes proves nothing."
- Instructions: ~100-line AGENTS.md as a map; rules that must always hold go into linters/tests, not prose; the runner sends facts, never a second copy of policy (copies drift); "stating a rule is not stating a priority" — a numbered run order fixed it.
- CLAUDE.md loads from every parent directory; a playbook in a parent folder applied to a second job by accident.
- Stale assumption audit: "Write down, for each component, the assumption it encodes and the observation that would retire it."
- Scope drift the other way: for ten days the agent logged the same next step and landed nothing because the playbook forbade the only work left. "The model was willing; the harness said no."

## Assessment for 741
New vs. video: the self-review in Tyler's design is self-graded, and this source shows that is the one grader known to be biased. The review must be (a) evidence-based (what landed, not what the agent says), (b) done by someone else (Martin, or a fresh session that sees only the output). Also: duplicated policy drifts — one job description per agent, in one place, never copied into prompts.
Marketing: personal site; the numbers come from cited papers and the author's own logs, marked as such.
Usable for 741: weekly review = Martin or a fresh reviewer session grades from the run records and the git/registry/portal evidence; the agent writes the facts (shipped, blocked, waiting), the grade comes from outside. Add a "stale rule" column to the review: which "never" line blocked useful work this week.
