# Devin API v3: get session (status, status_detail, ACUs, pull requests)

- URL: https://docs.devin.ai/api-reference/v3/sessions/get-organizations-session.md ; https://docs.devin.ai/api-reference/v3/sessions/get-organizations-session-insights.md
- Type: official doc (API reference)
- Published: living page, fetched 2026-10-13
- Fetched: 2026-10-13

## Key points
- A session has a top status: new, claimed, running, exit, error, suspended, or resuming.
- A second field, status_detail, makes "running" exact: working, waiting_for_user, waiting_for_approval, or finished.
- "Suspended" has a reason, for example inactivity, user request, usage limit, or out of credits.
- Each session records the compute used (acus_consumed). This gives a cost per run.
- Each session lists its pull requests with URL and state. The task links to the result.
- Sessions carry tags, a title, a category, and the origin (web app, Slack, API, CLI, or automation).
- Sessions can have a parent and child sessions. This shows delegation chains.
- A structured_output field holds validated output in a fixed schema.
- A separate insights endpoint gives message counts, a size class, and an AI analysis of the session.

## Gaps / bias notes
- The API reference does not show how the web app presents these states.
- An older schema used "blocked" for the same idea as waiting_for_user. Status names change between versions.
- The unit "ACU" has no plain definition on the page.
