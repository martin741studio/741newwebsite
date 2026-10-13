# D08 — Permission modes, auto mode, Bash sandbox (unattended safety)

- Author/org: Anthropic (Claude Code docs)
- Type: official docs (living pages)
- Publish date: living docs, counted as current on fetch date
- URLs: https://code.claude.com/docs/en/permission-modes , https://code.claude.com/docs/en/sandboxing
- Fetch date: 2026-10-13

## Extract (own words)

- Modes: `default` (Manual), `acceptEdits`, `plan`, `auto`, `dontAsk` (only pre-approved tools; everything else denied), `bypassPermissions` (everything; only for isolated containers or VMs).
- Auto mode: a classifier model reviews actions. It blocks actions that go beyond the request, target unknown infrastructure, or look driven by hostile content Claude read. Available on all plans with supported models (Opus 4.6+, Sonnet 4.6+, Haiku 5.5, Fable). Built-in start mode for interactive sessions from v2.1.283.
- Blocked by default in auto mode, e.g. sending secrets out, `terraform destroy`, printing live credentials, pushing private data to public repos, writing session transcripts.
- Boundaries Martin states in the conversation ("don't push", "wait for my review") are treated as block signals. They can be lost if compaction removes the message. For a hard guarantee use a deny rule.
- Fallback: 3 blocks in a row or 20 in total pauses auto mode and returns to prompting (not configurable). In a `-p` run with no prompt tool, the blocked action does not run and Claude keeps working; the run does not stop.
- No mode auto-approves: AskUserQuestion, MCP tools marked `requiresUserInteraction`, deletes of critical paths, cross-session messaging safeguards.
- `bypassPermissions` refuses to start as root or under sudo on Linux and macOS (skipped inside a recognized sandbox). The doc says it gives no protection against prompt injection.
- Deny rules apply in every mode, also in bypass.
- Bash sandbox: off by default; `/sandbox` or `sandbox.enabled: true`. OS-enforced limits on files and network for shell commands (Seatbelt on macOS; bubblewrap + socat on Linux). Network goes through a proxy with an allowlist that starts empty. File tools, MCP servers and hooks run outside the sandbox.

## IF/THEN rules for 741

1. IF a night session runs unattended on a server, THEN use `auto` (or `dontAsk` + allowlist) plus deny rules for publish/send/delete tools. Never `bypassPermissions` on a box that holds client credentials.
2. IF a night rule must hold ("never publish to a client site"), THEN write it as a `permissions.deny` rule, not only as a prompt line, because compaction can drop the prompt line.
3. IF the server is Linux, THEN install bubblewrap and socat and turn the Bash sandbox on, with a network allowlist of the hosts the jobs need.
4. IF the morning log shows many auto-mode blocks for one job, THEN treat it as a card: the job scope or allowlist is wrong, or content tried to steer the agent.

## Limits / caveats

- The classifier is probabilistic. It reduces risk; it does not replace OS-level isolation or scoped credentials.
