# V03 — Your GitHub Repo Is Now a Research Robot (Claude Code + GitHub Actions)

- Channel: Taylor Sparks (university professor, "vibe coding 101" series)
- URL: https://www.youtube.com/watch?v=U5sB19DLnOk
- Type: setup tutorial, 37m 18s
- Upload date: 2026-08-10
- Views: 37,439 (at fetch)
- Fetch date: 2026-10-13 (Apify discovery + `johnvc/YoutubeTranscripts`, dataset `jkrUikamYc0lfnl76`. Raw transcript not stored here.)

## Extract (own words)

1. Idea: a team writes "@claude do X" in a GitHub issue. GitHub Actions starts a runner, Claude Code does the task and replies in the issue thread, with commits or PRs if needed.
2. All tool keys live once as encrypted repository secrets. Team members with write access can use the agent without their own keys or Claude accounts.
3. Setup steps: create a private repo with `gh`, run `claude /install-github-app` (prefix with `claude` in PowerShell), run `claude setup-token` to make an OAuth token, store it as the secret `CLAUDE_CODE_OAUTH_TOKEN`, add a workflow YAML and a `CLAUDE.md`.
4. He uses the subscription OAuth token, not an API key, so runs count against the Pro/Max quota. He warns that team use can burn the hourly or weekly limits.
5. The workflow YAML passes secrets as environment variables, sets long bash timeouts (about 60 minutes for slow tools) and uses bypass permissions. He says to do that only in repos where you trust every writer.
6. `CLAUDE.md` is the agent's onboarding file: tool playbooks, safety rails (never echo secrets, no heavy jobs on login nodes), style rules and a failure protocol. Each agent mistake becomes a new line.
7. Gotcha: the runner dies when the job ends. Background processes die with it. Poll long jobs in the foreground, and commit a task ID when a job outlives the run.
8. Gotcha: the installer can create an extra `claude-code-review.yml` wired to an API-key secret. Delete or fix it.
9. Phone use: he opens an issue or comment from the phone while out running. Runs are async and parallel, and every run is logged.
10. Downsides he lists: slow feedback, no steering mid-task, small 2-core runners, wall-clock limits, debug by re-run. Secrets do not carry to a new repo. Expired tool tokens fail mid-run.
11. 2FA case: the agent posts "approve the Duo push" in the thread, and he approves on the phone. That is a human gate in the loop.
12. He warns that prompt injection can still leak secrets, so add only trusted collaborators.

Short quote: "Don't just fix it. Add a new line to your claude.md."

## Setup details

- Host: GitHub-hosted Actions runners (free tier works per his account). Claude Pro ($20) or Max ($200) subscription.
- Tools: GitHub CLI `gh`, Claude GitHub app, `claude setup-token`, repo secrets, `.github/workflows/claude.yml`, root `CLAUDE.md`, MCP/plugins (Asta, Edison Scientific), SSH to a cluster.
- Commands named: `gh repo create ... --private --clone`, `git commit --allow-empty`, `claude /install-github-app`, `claude setup-token`, `gh secret set CLAUDE_CODE_OAUTH_TOKEN`, `gh issue create --title ... --body "@claude ..."`.

## IF/THEN rules for 741

1. IF a night job only needs repo files and web APIs (no local Mac, no Chrome), THEN a GitHub Actions run on a private repo is a valid host with a full audit log.
2. IF Martin wants to give a task from the phone without Remote Control, THEN an "@claude" issue on a private repo works. Keep the repo private and the collaborator list to Martin only.
3. IF a workflow uses bypass permissions, THEN the repo holds no client deploy credentials (no FTP, no WordPress app passwords). Drafts and PRs only.
4. IF a night job calls a slow external tool, THEN poll in the foreground and write the job ID to a file before the run ends.
5. IF the night agent makes a mistake, THEN add one rule line to the repo `CLAUDE.md` the next morning.

## Caveats

- Sharing one personal subscription token across a team may conflict with Anthropic's consumer terms. Not checked here. For 741 (solo use) the risk is lower, but check the terms before any team use.
- Bypass permissions in CI plus repo secrets is a real leak path. He says so himself.
- Academic use case (supercomputer, literature tools). The pattern transfers, the tools do not.
