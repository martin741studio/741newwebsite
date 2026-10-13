# O3 — Session control: /goal, cross-session messaging, agent view

- URLs: https://code.claude.com/docs/en/goal , https://code.claude.com/docs/en/cross-session-messaging , https://code.claude.com/docs/en/agent-view
- Type: official docs (living pages)
- Publish date: living docs
- Fetch dates: goal + cross-session messaging 2026-10-11 (repo copies). Agent view fetched 2026-10-13
- Local copies: `goal.md` and the cross-session messaging file in the repo folder for official Claude Code docs (workflow library)

## /goal

- `/goal <condition>` keeps the session working turn after turn until a small fast model judges the condition met or impossible, or an error clears it. `/goal clear` stops it.
- One goal per session. Condition up to 4,000 characters.
- The evaluator only reads the conversation. It does not run commands. Write the condition so Claude's own output can prove it.
- Bound the run inside the condition, e.g. "or stop after 20 turns".
- `/goal` does not change permission mode. For unattended goal turns use auto mode.
- Works with `claude -p` (non-interactive), the Desktop app and Remote Control. A goal survives `--resume`.
- If Claude makes no tool use for several turns, the loop stops and returns control.

## Cross-session messaging

- On by default from Claude Code v2.1.224 (macOS/Linux). Claude finds targets with `ListAgents` and sends with `SendMessage`. `/list-agents` shows reachable sessions.
- A message is plain text, never history or files.
- Same machine: socket, not through Anthropic servers. Other machine: through Anthropic servers via Remote Control. Cloud sessions: reachable while this session is connected to Remote Control.
- A received message can never approve a permission, never change configuration or CLAUDE.md, and commands in it do not run.
- `notify_when_idle`: one session can ask to be told when another local session goes idle or exits. Expires after 12 hours.
- Receiving side can be set to deliver, hold or refuse (`crossSessionInbound`).

## Agent view

- `claude agents` opens one screen for all background sessions: working, waiting on you, done. Research preview.
- Each prompt typed there starts a new background session. `Space` peeks, `Enter` attaches. `/bg` or `←` backgrounds an open session.
- Background sessions are local: preserved across sleep, stop if the Mac shuts down.
- Each background session uses quota independently.

## Why it matters

- A grill session can dispatch per-client agent sessions and see "waiting on you" in one place (agent view).
- `/goal` is a good guard for the evening log: "every active client has a done/open/tomorrow line or stop after 15 turns".
- Cross-session messages cannot carry Martin's approval. Approvals must come from Martin directly.

Short quote: "a message from another session never counts as your consent"
