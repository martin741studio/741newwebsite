# O5 — Claude Code Projects (coordinator + threads)

- URL: https://code.claude.com/docs/en/claude-projects
- Type: official doc (living page, public beta)
- Publish date: living doc
- Fetch date: 2026-10-11 (repo copy, counts as current)
- Local copy: the projects file in the repo folder for official Claude Code docs (workflow library)

## Key facts (own words)

- A project is one long-running coordinating conversation. Claude starts a "thread" (usually a cloud session) for each piece of work and tracks them.
- Public beta on Pro and Max, rolling out gradually. Not on Team/Enterprise yet.
- Overview pane shows finished threads, PRs ready, and threads under "Waiting on you". Tabs: Library (files), Pull requests, Routines.
- Project instructions and project memory reach every new thread. A rule stated once applies to all threads.
- A thread can run on your own computer through Remote Control when it needs local tools. Cloud threads keep going with the laptop closed. Local threads only while the Mac is awake.
- Claude can put part of the project's work on a schedule as a routine. Those routines appear on the project's Routines tab.
- Pause stops all threads and routines. Archive stops routines. Delete turns routines off.
- New projects default every thread to Opus at high effort, which uses the plan fastest. Set thread model/effort in Project settings.
- Docs say: a single task that repeats with no conversation around it fits a routine better than a project.

## Why it matters

A project per client (or one "741 Ops" project) could hold standing per-client instructions and show "Waiting on you" in one place on the phone. But threads are cloud sessions: they cannot see the local 741 repo unless run through Remote Control or the repo is on GitHub.

Short quote: "Every new thread starts with the project's instructions"
