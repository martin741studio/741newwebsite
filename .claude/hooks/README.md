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
