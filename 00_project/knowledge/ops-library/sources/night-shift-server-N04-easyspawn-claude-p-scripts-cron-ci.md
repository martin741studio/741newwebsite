# N04 — Running Claude Code headless: claude -p in scripts, cron, and CI

- Author/org: EasySpawn (persistent agent server vendor; blog)
- Type: practitioner guide
- Publish date: 2026-09-24 (verified: article:published_time and JSON-LD)
- URL: https://easyspawn.com/blog/claude-code-headless-mode
- Fetch date: 2026-10-13

## Extract (own words)

- `claude -p` exits 0 or non-zero, so scripts can branch on it. Pipe content in (diff, logs) so the run needs fewer permissions.
- Use `--output-format json` with `--json-schema` when a script must read the result; read `structured_output`.
- Set both `--max-turns` and `--max-budget-usd` on anything scheduled. A prompt that works by hand can loop at 3 am.
- Use `--bare` for reproducible runs and for code you did not write; it needs an API key.
- Chain steps with `--resume <session_id>` captured from JSON output.
- Where runs live: laptop (only while awake), CI runner (clean but forgets everything, minutes billed), or a persistent server (keeps dependencies and last night's results on disk).
- Start with read-only jobs (reports, reviews). When a job may change code, have it open a pull request, not push to main.
- Proposed safe default: `claude --bare -p "$(cat prompt.md)" --permission-mode dontAsk --allowedTools "Read,Bash(npm test *)" --max-turns 15 --max-budget-usd 3 --output-format json > reports/$(date +%F).json`.

## IF/THEN rules for 741

1. IF a new night job is added, THEN it starts read-only (reports, specs, audits) and writes a dated JSON report. Write rights come later, one tool at a time.
2. IF a night job changes a repo, THEN it ends in a branch or draft PR, never a push to main.
3. IF a night job has several steps, THEN store the session_id and resume it, so the morning card links to one transcript.

## Limits / caveats

- Vendor blog. It says unapproved actions in `-p` are denied; the official doc says the result depends on the permission mode (see D04).
