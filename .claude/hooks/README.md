# 741 hooks (status: ACTIVE since 2026-10-30, settings in `.claude/settings.json`; see also `~/.claude/settings.json` for the global ones)

These hooks turn Martin's hard rules into checks that Claude Code runs itself. Prose in CLAUDE.md or memory only explains them; the hooks enforce them.

| Hook | Event | Scope | What it does |
|---|---|---|---|
| `go_marker.py` | UserPromptSubmit | project | Sets `.claude/go/<session>.json` when Martin's prompt has a standalone "go". Deletes it on each prompt without a go. A go is valid for one turn and 30 minutes. |
| `go_card.py` | PostToolUse on AskUserQuestion | project | A go chosen on a decision card counts like a typed go (added 2026-11-01). Reads only the chosen answer texts, needs a standalone "Go", ignores wait answers ("später", "noch", "kein", "nicht", "warten", "erst"). Same marker, same TTL. |
| `live_change_gate.py` | PreToolUse (Bash, Edit, Write, Novamira, Porkbun) | project | Denies FTP deploys (`node upload*.js`, `ftp-delete-old.mjs`, `npm run deploy`, `lftp`/`sftp`/`ftp` as a command, `curl -T`, `ftp://`), Novamira write abilities, `execute-php` with write calls, Porkbun hosting writes, and edits of settings/hooks files. Each passes when a go marker exists. Writes to `.claude/go/` are always denied. Unknown Novamira abilities get "ask". Since 2026-11-08 heredoc bodies and `/dev/null` redirects are stripped before matching, so a note that mentions "FTP deploy" or `settings.json` no longer trips the gate. |
| `destructive_guard.py` | PreToolUse (Bash, Supabase SQL) | project | See below. |
| `slop_gate.py` | Stop | project | Finds every ```text block in the last reply. Runs `deslop_de.py` (German) or slopmonster `deslop.py` (English). Blocks the stop below 5/5. On the retry it only warns, so a false positive cannot cause a loop. |
| `presend_sweep_hook.py` | Stop | global (`~/.claude/settings.json`, file at `00_project/presend-sweep/`) | Blocks a reply that ends with open points for Martin in prose: headings like "Offen bei dir", closing questions, "du"-step lists. They must be AskUserQuestion cards. |

Also global in `~/.claude/settings.json`: `automation_guard.py`, `automation_done_gate.py`, `automation_session.py` (automation-build workflow).

Tests: `bash .claude/hooks/test_hooks.sh` (go-gate and slop-gate cases, about 1 s).

Limits: the go detector is a regex. It accepts a standalone "go" and rejects "go through", "go back", "go to", "go over", "go on". The Bash check is a regex too, so a command with a new form can pass it. Card labels that mean "wait" must not carry the word "Go" as the action.

## destructive_guard.py (added 2026-11-06)

741 version of the "Codeguard" bash parser from the TokenMade podcast (Alexander Weipprecht, 2026-11-05). Every command is split into segments (quote-aware, incl. `bash -c`, `$(...)`, `xargs`, heredocs fed to a shell) and checked against a deny list: recursive deletes outside throwaway paths (/tmp, node_modules, __pycache__, dist, build ...), `find -delete`, `git reset --hard`, `git clean -f`, force push, `git checkout .` / `git restore .`, `git branch -D`, `git stash drop`, history rewrites, destructive SQL (DROP, TRUNCATE, DELETE/UPDATE without WHERE) in psql/mysql/sqlite and in Supabase `execute_sql` / `apply_migration`, disk and system commands, curl piped into a shell, killing Chrome.

A go from Martin in the lead session lets the command pass (same marker as the go-gate). Agent-team teammates and subagents run as their own sessions and never hold that go. Heredoc bodies that only write a file are not checked. Limit: a parser over shell text, not a sandbox; obfuscated commands can pass. Gap: INSERT/UPDATE with WHERE passes; memory `db-write-needs-isolated-confirmation` covers that in prose.

Tests: `bash .claude/hooks/test_destructive_guard.sh` (69 cases).

`settings.snippet.json` is the historical activation snippet; the live configuration is in `.claude/settings.json`.
