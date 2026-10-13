# O1 — Claude Code Routines (cloud)

- URL: https://code.claude.com/docs/en/routines
- Type: official doc (living page, research preview)
- Publish date: living doc, no fixed date
- Fetch date: 2026-10-11 (repo copy, counts as current), checked 2026-10-13
- Local full copy: `00_project/knowledge/workflow-library/official-docs/claude-code/routines.md`

## Key facts (own words)

- A routine is a saved prompt + one or more GitHub repos + an environment + connectors. It runs on Anthropic cloud, so it runs with the laptop closed.
- Triggers: schedule (hourly, daily, weekdays, weekly, or one-off at a timestamp), API (`/fire` POST with bearer token), GitHub events (pull request, release). One routine can have several triggers.
- Minimum schedule interval is 1 hour. Custom cron only via `/schedule update` in the CLI. Times are entered in local time zone.
- Runs on the hour can start several minutes late. The doc advises e.g. 9:07 instead of 9:00.
- No permission-mode picker. The run is fully autonomous. It can use every tool of every included connector, including writes, without asking.
- All your claude.ai connectors are included by default. Remove the ones the routine does not need.
- Local MCP servers (`claude mcp add`) are not visible to routines. Add them as claude.ai connectors or declare them in a committed `.mcp.json`.
- Each run clones the repos fresh. No access to local files on the Mac. Changes go to `claude/`-prefixed branches unless the prompt says otherwise.
- Default network is "Trusted" (allowlist). Other hosts fail with 403 unless you edit the environment. Connector traffic is not affected by the allowlist.
- Fire text (API or Run now) arrives wrapped as untrusted data. The saved prompt must explicitly tell Claude to act on it.
- A green run status only means no infrastructure error. You must open the run to see if the task succeeded.
- Limits: 100 scheduled runs per hour per account. Run now + API fires 30 per hour per routine. Runs draw normal subscription usage.
- If GitHub access is missing, the routine skips runs for up to 72 hours, then turns off.
- Routines belong to one claude.ai account. Actions through connectors appear as you.
- Manage: claude.ai/code/routines, the Desktop "Routines" page (choose Cloud), or `/schedule` in the CLI (`/schedule list`, `/schedule update`, `/schedule run`).

## Why it matters for the morning grill

A cloud routine is the only Claude-native way to produce the morning scan when Martin's Mac is asleep or off. It cannot read local files, so the scan inputs must live in a repo or a connector (Gmail, Calendar, Drive, Notion, Supabase via MCP).

Short quote: "the prompt must be self-contained and explicit about what to do"
