# D10 — Browser tasks on a server: Claude in Chrome limits, Playwright MCP

- Author/org: Anthropic (Claude Code docs) and Microsoft (Playwright MCP README)
- Type: official docs (living pages)
- Publish date: living docs. Playwright MCP repo last push 2026-10-08.
- URLs: https://code.claude.com/docs/en/chrome , https://github.com/microsoft/playwright-mcp (README)
- Fetch date: 2026-10-13

## Extract (own words)

- Claude in Chrome needs Chrome, Edge or another Chromium browser with the extension (v1.0.36+) and a direct Anthropic plan.
- Browser actions run in a **visible** Chrome window. It shares the browser's login state. On a login page or CAPTCHA it pauses and asks a human.
- It needs a `/login` claude.ai login. With an API key or a `setup-token` token, Claude Code keeps Chrome integration off, even with `--chrome`.
- Not supported in WSL. The extension talks to Claude Code through Chrome native messaging on the same machine.
- Remote Control server mode can start sessions with Chrome on (`claude remote-control --chrome`), so a phone-driven session can use the server's Chrome, if that machine has a desktop and Chrome.
- Playwright MCP: `--headless` runs without a window (headed by default). Default is a persistent profile that keeps logins; `--user-data-dir` sets where. `--isolated` keeps the profile in memory; `--storage-state` loads saved cookies. A persistent profile serves one browser at a time; parallel clients need `--isolated` or separate dirs. Headless browsers close after one idle hour by default (`--idle-timeout`). `--extension` connects to an existing Chrome/Edge.
- Cloud sessions (D02) cannot do interactive SSO logins.

## IF/THEN rules for 741

1. IF a night task needs Martin's logged-in Google tools in Chrome, THEN it needs a machine with a real desktop session and full login (Mac mini, or a VPS with a virtual desktop). A pure headless VPS with setup-token cannot use Claude in Chrome.
2. IF a browser task only reads public pages or a test site, THEN use Playwright MCP `--headless` on the server instead of Claude in Chrome.
3. IF a browser task needs a client login, THEN keep a dedicated profile dir per client with Playwright MCP and never share Martin's personal Chrome profile with the night agent.
4. IF the task hits a CAPTCHA or login wall, THEN stop and make a card. Do not try to get around it.

## Limits / caveats

- No official doc covers Claude in Chrome on a Linux VPS with Xvfb or VNC. Treat that as untested.
