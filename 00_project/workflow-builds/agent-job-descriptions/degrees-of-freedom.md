# Degrees of freedom — agent-job-descriptions (2.5, Rule R1.7)

| Step | Kind | Freedom | Implementation |
|---|---|---|---|
| Roster listing (sessions, scheduled tasks, registry) | deterministic | low | `scripts/roster.py` reads registry.json + scheduled-tasks dir + a hand-kept `roster.json`; sessions list pasted from the tool output |
| Block validation (all sections present, every never-line has a rung, every tool has a rating, no "always"/"never" without rung) | deterministic | low | `scripts/validate_jd.py` |
| Placing the description (write rules file / scheduled-task header / memory line, roster update, `_run.json`) | deterministic, side effect | low, gated | `scripts/place.py` after a card "Go" |
| Evidence collection for the review | deterministic | low | `scripts/collect_evidence.py` |
| Drafting duties, goal, edge cases from the agent's real prompt and memory | qualitative | high | prompt heuristics + 2 examples in `references/` |
| Grade proposal from evidence | qualitative, advisory | medium | heuristics; Martin's card decides |
| Rung decision for a repeated mistake | qualitative | medium | ladder table in `references/rung-ladder.md`; card decides |
