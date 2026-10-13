# D05 — Authentication on a server: setup-token, API key, terms

- Author/org: Anthropic (Claude Code docs)
- Type: official docs (living pages)
- Publish date: living docs, counted as current on fetch date
- URLs: https://code.claude.com/docs/en/authentication , https://code.claude.com/docs/en/legal-and-compliance
- Fetch date: 2026-10-13

## Extract (own words)

- On a machine without a browser, `/login` shows a code in the browser that you paste back into the terminal ("Paste code here if prompted"). Common over SSH.
- `claude setup-token` creates a **one-year** OAuth token after a browser approval. It is not saved; you set it as `CLAUDE_CODE_OAUTH_TOKEN`. Needs Pro, Max, Team or Enterprise.
- That token can **only make model requests**. It cannot start Remote Control, cannot fetch claude.ai connectors, and Chrome integration stays off with it. Locally configured MCP servers still work. `--bare` ignores it.
- Credential order: cloud-provider vars, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_API_KEY`, `apiKeyHelper`, `CLAUDE_CODE_OAUTH_TOKEN`, profile/federation, then the `/login` subscription login. An approved API key wins over the subscription and bills the API.
- `/schedule` and claude.ai connectors are unavailable while an API-key-type source is selected.
- Terms: Free, Pro and Max fall under the Consumer Terms; Team, Enterprise and API under the Commercial Terms.
- OAuth (subscription) login is meant for "ordinary use" of Claude Code and Anthropic apps by the plan purchaser. Third-party developers may not route requests through Free/Pro/Max credentials on behalf of their users.
- The doc says nothing prevents an end user from signing in to the unmodified Claude Code binary with their own subscription. Anthropic may enforce these limits without notice.
- Hosting Claude Code inside your own product for others needs Commercial Terms, and each end user must bring their own credentials.

## IF/THEN rules for 741

1. IF the server runs Remote Control or needs claude.ai connectors, THEN sign in with `claude auth login` (full login). Do not use setup-token there.
2. IF the server runs plain scripted `claude -p` jobs on Martin's plan, THEN `CLAUDE_CODE_OAUTH_TOKEN` is the documented route. Put a renewal date 11 months out in the calendar.
3. IF any ANTHROPIC_API_KEY is in the server environment, THEN Claude Code uses it ahead of the plan. Set it only for jobs that should bill the API.
4. IF the night shift ever serves clients directly (clients trigger runs), THEN it must move to an API key under Commercial Terms. A personal Max login is only for Martin's own use.

## Limits / caveats

- "Ordinary use" is not defined in numbers. Heavy 24/7 automation on one Max login is a grey zone; the API path is the safe one.
- Token lifetime is stated as one year; there is no auto-refresh in the doc.
