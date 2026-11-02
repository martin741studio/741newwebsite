# Rung ladder — where a never-line is enforced in 741 (state 2026-11-03)

| Rung | What it is | Holds when | 741 examples |
|---|---|---|---|
| hook | `PreToolUse` deny in `.claude/hooks/live_change_gate.py`; fires in every permission mode, even bypass | always | FTP deploys (`node upload.js`, `upload_one.js`, `upload_only.mjs`, `ftp-delete-old.mjs`, `npm run deploy`, `lftp`, `sftp`, `curl -T`, `ftp://`), Novamira write abilities, `execute-php` with write calls, Porkbun hosting writes, edits of settings/hook files, writes to `.claude/go/` — all need a go marker (typed "go" or card Go) |
| runner | flags of the process that starts the agent | for that runner | night shift v2: `--permission-mode dontAsk`, `--allowedTools`/`--disallowedTools`, `--max-budget-usd`, deadline kill, STOP file |
| card | an AskUserQuestion card with a Go option, same turn | when the agent asks | send, spend, delete, publish, Supabase/portal writes (Martin 03.11.), page swap, menu/slug change, tracking change |
| skill | skill frontmatter `disable-model-invocation`, `allowed-tools`; subagent `tools`/`disallowedTools` | when that skill/subagent runs | this skill: Bash limited to python3 and git |
| rule | `.claude/rules/agents/<id>.md` with `paths:`; loads when matching files are touched | in sessions that touch the paths | placed job descriptions for chat agents |
| advisory | CLAUDE.md line, memory file, prompt text | never guaranteed; checked by review evidence | page-swap rule, no HTML in client fields, body copy via /content-write, both screenshots, no private Google account |

Rules:
- A never-line gets the highest rung that really covers it; do not write "hook" for a Bash form the regex does not match.
- Hook edits are proposals for a separate turn (the hook denies edits of hook files without a go).
- The weekly review checks advisory lines by evidence (outbox files, screenshots, git log), never by the agent's word.
- Rule ladder for a repeated mistake (source 11): memory line → rules file → skill edit → hook. Twice in a week = move one rung up.
