# 1.5 Research note — Night Shift + Server (2026-10-13)

Block (provisional): skill `night-shift` v2 + runner + hook guards on a self-hosted Linux box; Routine if Martin picks Anthropic cloud (see block-choice.md).
Evidence: ops-library new sources `night-shift-server-D01–D10, N01–N08` (+ V01… from the video agent), facts `ops-library/_derived/night-shift-server-facts.md`, coverage `00_project/night-shift-server-coverage-map.md`.

Key facts (official, fetched 13.10.):
- Cloud routines: no local files, no local MCP, no `.secrets/`; min interval 1 h; no approvals. Self-hosted runners need Team/Enterprise (Martin is Max).
- Remote Control: machine must stay on; needs the full claude.ai login (not setup-token, not API key). Push only while active.
- setup-token: 1 year, model requests only, "for CI and scripts"; logins must not be shared; "ordinary use" not defined for 24/7.
- Since 7 Oct 2026 Max includes monthly API credits (help 15036540 confirms; amounts $100/$200 per D06). They cover `claude -p` only with that Console org's API key → night runs stop eating the day's plan limits.
- `claude -p` has `--max-turns`, `--max-budget-usd` (estimate), `--permission-prompts none`, `dontAsk` + allowlist; deny rules hold in every mode. Bypass refuses root; Bash sandbox on Linux = bubblewrap.
- Claude in Chrome needs a visible Chrome with full login → not on a headless VPS. Playwright MCP headless works for public pages.

3 rules that drive the design:
1. Gate by consequence: night = drafts, research, data pulls, local builds, QA. Never sends, deploys, live writes, ads, money (ops R20/R21, automation classes G/M).
2. Hard money cap outside the agent (API credit with no auto-reload + `--max-budget-usd` + invocation breaker); deny rules for "never publish", not prompt lines (D04, D08, N07).
3. Night results become cards in the existing Command Center; done only via Martin's click with independent proof (ops R26, N05).

Pattern: Ralph / fresh context per item (existing blueprint) + Critic + REVIEW → cards.

Open questions (→ grill): host and region; budget source; task classes; phone channel and times; wake rules; pilot workflow; fix the 6 known night-shift bugs before or during the move.
