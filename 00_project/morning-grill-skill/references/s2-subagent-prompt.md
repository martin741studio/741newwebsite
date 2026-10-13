# S2 subagent prompt (transcript reader)

READ-ONLY. Write only `<run>/inputs/s2-chats.json`.

Find what was DONE in Claude Code chats since the bookmark `<BOOKMARK WITA>` (= `<UTC>`), grouped per client.
Transcripts: `~/.claude/projects/-Users-martindrendel-741website*/*.jsonl` (main dir + one dir per worktree). Select files with mtime after the bookmark. Skip the morning-grill session itself and sidechains.
Per file: only messages after the bookmark. Read user text and assistant text blocks; never tool outputs. Focus on the last 3–6 assistant messages.
Map to clients with the aliases in `00_project/morning-grill-goals.json`; else "741 internal" or the prospect name.
Output shape:
{"bookmark": "...", "read_at": "...", "files_read": N, "files_unreadable": [],
 "clients": {"<Client>": {"done": [], "open": [], "waiting_for": [{"who": "client|team|google|martin", "what": "", "since": ""}],
  "client_promises": [], "needs_martin": [], "last_activity": ""}}}
Lines under 160 characters, facts only, max 8 per list, file basename in brackets. Never copy passwords, tokens or keys.
