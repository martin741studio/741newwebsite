# N03 — OAuth 401 kills a long-running Remote Control session (shared-credential race)

- Org/author: community reporter, archived on claudeissues.com (mirror of an anthropics/claude-code GitHub issue)
- Type: bug report / issue tracker page
- Publish date: opened **2026-07-02**, closed **2026-08-23** as "not planned." Verified from the dates printed on the issue page. The open date is 11 days before this research's freshness cutoff (2026-07-13); flagged as borderline and included only because the close/last-activity date (Aug 23) and version evidence (v2.1.197/198, ~27h uptime) are safely inside the window.
- URL: https://claudeissues.com/issue/73555-subscription-oauth-long-running-remote-control-session-dead-ends-at-401-please-r
- Fetch date: 2026-10-15

## Extract (own words)

- Reported on Claude Code v2.1.198 (native macOS installer); the long-running process had been up about 27 hours and was still executing the in-memory v2.1.197 build, because an auto-update had changed the on-disk binary mid-session without restarting the running process.
- A session driven through iPhone Remote Control fails at roughly the daily token-refresh boundary with "Please run /login" and "API Error: 401 Invalid authentication credentials."
- Reporter's root-cause theory: the long session, other local CLI sessions on the same machine, and the phone app all share one Keychain OAuth credential with single-use refresh tokens. When any other client refreshes first, the long session's own refresh token is invalidated server-side, so its later reactive refresh fails with a 401 — a race over shared credential state, not a dead/expired token per se.
- Second, compounding problem: running `/login` inside the already-stuck remote-controlled session doesn't recover it. The browser shows a success page, but the CLI session never receives the OAuth callback and sits at "Login OAuth error: Press Enter to retry," and pressing Enter just reopens the browser without advancing.
- Workaround found by the reporter: press ESC to cancel the stuck `/login` prompt, then retry the original request. This works because the reactive refresh succeeds once the shared credential has already been refreshed by some other client — i.e. the fix is "stop trying to log in again" not "log in again."

## IF/THEN rules for 741

1. IF 741-agents-01 runs more than one Claude Code identity against the same account at once (e.g. the batch `claude -p` token plus the persistent `claude remote-control` session plus Martin's laptop/phone), THEN a refresh race across those clients is a documented, reproducible failure mode — the fix is not "log in again," it is to let the other client's refresh settle, then retry.
2. IF a 741 night-shift or persistent session hits a 401 "Please run /login" at 3am with nobody there, THEN do not have the automated recovery path attempt an interactive `/login` loop — per this report that path can itself get stuck; instead the safer automated action is to back off and retry the original request once, since the credential is often already valid again from another client's refresh.
3. IF this failure shows up again on 741-agents-01, THEN check whether an in-flight CLI auto-update (changing the on-disk binary while a long session keeps running the old in-memory build) is a contributing factor, as it was here — a version mismatch between the running process and the installed binary is a specific thing to log and check for.

## Caveats

- Closed "not planned," no maintainer reply cached — Anthropic has not confirmed this root-cause theory; it is the reporter's own diagnosis from log evidence.
- 741's setup (batch token via `CLAUDE_CODE_OAUTH_TOKEN` env var kept deliberately separate from the full-login `claude remote-control` session, per decisions.md N43–N47) already avoids sharing one literal credential between the two — this reduces but may not eliminate the exposure, since Remote Control itself still uses one account-level login that Martin's own devices may also touch.
