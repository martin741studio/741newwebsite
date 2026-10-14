# N04 — Claude Code v2.1.259–v2.1.260: `--permission-prompts none` and a permission-rule security fix

- Org/author: dev.classmethod.jp (third-party write-up of Anthropic's official release notes, in English)
- Type: article (changelog summary/translation)
- Publish date: **2026-09-04**, covering releases v2.1.259 (2026-09-02) and v2.1.260 (2026-09-03). Dates shown on the page.
- URL: https://dev.classmethod.jp/en/articles/20260904-cc-updates-v2-1-260/
- Fetch date: 2026-10-15

## Extract (own words)

- v2.1.259 added `--permission-prompts none`, built specifically for unattended headless environments: "operations that would require prompts are automatically denied," while normal permission-mode logic (including auto mode) keeps working as before. The stated use case is "environments like CI or scheduled tasks where waiting for input is not an option."
- This is a materially different default than `dontAsk`/`bypassPermissions`: instead of silently allowing or silently waiting forever, an operation that would need a prompt is denied outright and the run can continue or fail cleanly rather than hanging.
- v2.1.260 fixed three ways permission/deny rules were silently not taking effect:
  1. `Edit`/`Write`/`Read` rules whose path contained parentheses were discarded as invalid and ignored by the Bash sandbox — paths meant to be read-only were in fact writable.
  2. A single malformed file-rule pattern (e.g. an unclosed `[`) made ALL file-edit permission checks fail with "Invalid regular expression" — one bad rule broke every other rule's enforcement.
  3. The Bash permission check was auto-approving zsh commands that hid command substitutions inside assignments to `REPORTTIME`, `REPORTMEMORY`, `DIRSTACKSIZE` — these now correctly require approval.

## IF/THEN rules for 741

1. IF 741's night-shift-v2 runner wants a stricter unattended mode than today's `--permission-mode dontAsk` + allowlist (decisions.md N28), THEN `--permission-prompts none` (v2.1.259+) is the more defensive choice for anything outside the allowlist — it denies-and-continues instead of leaving a prompt no one answers, which matters for 3am runs.
2. IF 741's deny rules (curl/ftp/scp/rsync/ssh outbound, `git push` to `main`, etc. — night-shift-server-workflow.md section 6) use any path containing parentheses, or any single malformed pattern anywhere in the rule set, THEN re-verify them were actually enforced before v2.1.260 — one bad rule could have silently disabled every other `Edit`/`Write`/`Read` deny rule, and a path with parentheses specifically bypassed the Bash sandbox.
3. IF 741 adds `--permission-prompts none` to the night runner, THEN pin to v2.1.259 or later (it did not exist before) and re-run the permission test from decisions.md N28 (curl denied, write outside `reporting/night-shift/**` denied) to confirm the new flag doesn't change those outcomes.

## Caveats

- This is a translated third-party summary of Anthropic's own release notes, not the primary changelog text; the direct quotes above are the summary's own quoted wording from that changelog, not independently re-verified against code.claude.com by this research pass.
- The article's section heading says "Security Fix for Permission Rules" but its body text is headed "Fix for Permission Rules Not Taking Effect" — treat this as a real security-relevant fix regardless of the exact title Anthropic used internally.
