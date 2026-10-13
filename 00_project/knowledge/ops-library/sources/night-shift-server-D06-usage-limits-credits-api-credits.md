# D06 — Usage limits, usage credits, and the new monthly API credits (Max)

- Author/org: Anthropic (Claude Code docs + Claude Help Center)
- Type: official docs and help articles (living pages)
- Publish date: living pages. Help article 15036540 shows an "Update October 7, 2026" note.
- URLs: https://code.claude.com/docs/en/costs , https://code.claude.com/docs/en/errors , https://support.claude.com/en/articles/11145838 , https://support.claude.com/en/articles/12429409 , https://support.claude.com/en/articles/11049741 , https://support.claude.com/en/articles/17154008 , https://support.claude.com/en/articles/15036540
- Fetch date: 2026-10-13

## Extract (own words)

- Pro and Max have a 5-hour session limit and a weekly limit. Max also has a separate weekly Fable limit. Claude, Claude Code and Desktop share one pool.
- Max weekly limit resets at a fixed weekday and time assigned to the account (see Settings > Usage). Anthropic may add other caps at its discretion.
- At the limit, Claude Code blocks requests until the reset shown ("resets 3:45pm" / "resets Mon 12:00am"). Session and weekly limits apply to all models; switching model does not help. One heavy burst can use the weekly limit before the 5-hour window resets.
- Interactive CLI sessions on a subscription can wait and continue after the reset ("Continue automatically at usage limit" in `/config`, v2.1.234+). Desktop has an "Auto-continue when limits reset" box for the session limit only, not the weekly limit.
- Usage credits (Pro/Max): when on, requests switch to pay-as-you-go at API rates and keep working, up to a monthly spend limit you set. Prepaid, with optional auto-reload.
- **New (7 Oct 2026): monthly API credits.** Max 5x gets $100, Max 20x $200 per month in a linked Claude Console organization. Claim on claude.ai > Settings > Billing after 7 days on the plan. No card needed. One Console org only.
- The API credits cover the Claude API, Message Batches, Claude Managed Agents and the Agent SDK. They cover `claude -p` **only when run with an API key from the linked org**. They do not cover interactive Claude Code, extra usage, GitHub Action runs, or Bedrock/Vertex.
- The credits do not roll over, are spent before purchased credits, and when gone (and no purchased credits) API requests stop until next month. They never bill the Claude plan.
- `claude -p` and Agent SDK runs signed in with the plan still draw from plan limits. The June "Agent SDK credit" was paused and is not available.

## IF/THEN rules for 741

1. IF Martin is on Max, THEN claim the monthly API credit into one Console org and point server `claude -p` jobs and Managed Agents at that org's API key. The night shift then stops eating his daytime plan limits.
2. IF the API credit runs out, THEN jobs stop by design (no auto-reload). Keep auto-reload off unless Martin approves a cap, and log "credit exhausted" as a morning card.
3. IF a night run uses the plan login instead, THEN the weekly limit is the real ceiling. Schedule heavy jobs right after the weekly reset and keep a reserve for daytime client work.
4. IF a run hits a limit mid-task, THEN it must leave a resumable state file. Only interactive sessions auto-continue after reset; `-p` runs simply fail.

## Limits / caveats

- Weekly limit sizes are not published in numbers.
- The API-credit offer is rolling out over a few days; it may not show yet.
