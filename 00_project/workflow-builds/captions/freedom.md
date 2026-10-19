# 2.5 Degrees of freedom (Rule R1.7)

| Step | Kind | Freedom | Where |
|---|---|---|---|
| 1 Intake: folder, dump.md, versioning, _run.json | fragile, exact order | low: script | `scripts/intake.py` |
| 1a Read the Drive doc | tool call | low: one MCP call, fully qualified name | SKILL.md |
| 2 Beats: list every fact from the dump | qualitative, but strict (quote, do not add) | medium: heuristic with the rule "quote the dump" | SKILL.md |
| 3 Story order | qualitative | high: heuristic, 4-part shape | `references/story-rules.md` |
| 4 Draft captions | creative | high within a fixed format: template + 3 example pairs | `assets/captions-template.md`, `references/examples.md` |
| 5 Validate format and numbers | deterministic | low: script, loop until PASS | `scripts/validate_captions.py` |
| 6 Slop lint | deterministic | low: script, 5/5 | slopmonster `deslop.py`, `cleanse.sh` |
| Checkpoint | Martin | - | AskUserQuestion card |
| 7 Drive copy, _run.json final | side effect | low: one MCP call after "go", then `scripts/intake.py finish` | SKILL.md + script |
