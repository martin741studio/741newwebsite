# 741 hooks (status: written, NOT active)

These hooks turn three hard rules from memory into checks that Claude Code runs itself.
They are not active. To activate them, merge `settings.snippet.json` into `.claude/settings.json`.
Do this only after Martin gives the go.

| Hook | Event | What it does |
|---|---|---|
| `go_marker.py` | UserPromptSubmit | Sets `.claude/go/<session>.json` when Martin's prompt has a go. Deletes it on each prompt without a go. A go is valid for one turn and 30 minutes. |
| `live_change_gate.py` | PreToolUse | Denies FTP deploys (`node upload.js`, `upload_one.js`, `upload_only.mjs`, `ftp-delete-old.mjs`, `npm run deploy`, `lftp`, `sftp`, `curl -T`, `ftp://`), Novamira write abilities, `execute-php` with write calls, Porkbun hosting writes, and edits of settings/hooks files. Each passes when a go marker exists. Writes to `.claude/go/` are always denied. Unknown Novamira abilities get "ask". |
| `slop_gate.py` | Stop | Finds every ```text block in the last reply. Runs `deslop_de.py` (German) or slopmonster `deslop.py` (English). Blocks the stop below 5/5. On the retry it only warns, so a false positive cannot cause a loop. |

Tests: `bash .claude/hooks/test_hooks.sh` (27 cases, about 1 s).

Limits: the go detector is a regex. It accepts a standalone "go" and rejects "go through", "go back", "go to", "go over", "go on". The Bash check is a regex too, so a command with a new form can pass it.

## go_card.py (PostToolUse on AskUserQuestion, added 2026-11-01)

A go chosen on a decision card counts like a typed go. Martin pressed "Go, jetzt hochladen"
on a card and was then asked to type the go again; that was a tool gap, not his job.
The hook reads only the chosen answer texts (never the question or the option list),
needs a standalone "Go" (same regex as go_marker.py) and ignores wait answers
("Go später", "noch kein Go", "nicht", "warten", "erst"). Same marker, same TTL, same
per-turn scope. Card labels that mean "wait" must not carry the word "Go" as the action.

## destructive_guard.py (PreToolUse on Bash and Supabase SQL, added 2026-11-06)

741 version of the "Codeguard" bash parser from the TokenMade podcast (Alexander Weipprecht,
2026-11-05). Every command is split into segments (quote-aware, incl. `bash -c`, `$(...)`,
`xargs`, heredocs fed to a shell) and checked against a deny list: recursive deletes outside
throwaway paths (/tmp, node_modules, __pycache__, dist, build ...), `find -delete`,
`git reset --hard`, `git clean -f`, force push, `git checkout .` / `git restore .`,
`git branch -D`, `git stash drop`, history rewrites, destructive SQL (DROP, TRUNCATE,
DELETE/UPDATE without WHERE) in psql/mysql/sqlite and in Supabase `execute_sql` /
`apply_migration`, disk and system commands, curl piped into a shell, killing Chrome.

A go from Martin in the lead session lets the command pass (same marker as the go-gate).
Agent-team teammates and subagents run as their own sessions and never hold that go.
Heredoc bodies that only write a file are not checked, so scripts and docs can contain
the words. Limit: a parser over shell text, not a sandbox; obfuscated commands can pass.

Tests: `bash .claude/hooks/test_destructive_guard.sh` (69 cases).

Activation (in `.claude/settings.json`, under `PreToolUse`):

    {"matcher": "Bash|mcp__.*__execute_sql|mcp__.*__apply_migration",
     "hooks": [{"type": "command",
                "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/destructive_guard.py\"",
                "timeout": 5}]}
