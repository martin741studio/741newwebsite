# V01 — How auto mode works with Claude Code

- Channel: Claude (official Anthropic channel)
- URL: https://www.youtube.com/watch?v=b8SV4U6fEIc
- Type: official explainer, 5m 41s
- Upload date: 2026-08-04
- Views: 1,974,832 (at fetch)
- Fetch date: 2026-10-13 (discovery: Apify `streamers/youtube-scraper`. Transcript: Apify `johnvc/YoutubeTranscripts`, dataset `jkrUikamYc0lfnl76`. Raw transcript not stored here.)

## Extract (own words)

1. Anthropic says users approve about 97% of permission prompts. Many prompts cause approval fatigue on long tasks.
2. Auto mode does not let Claude approve its own actions. A separate classifier checks each proposed action.
3. The classifier sees the user's messages and Claude's tool calls. It does not see Claude's reasoning, Claude's replies or tool output. Thus Claude's text cannot steer it.
4. The classifier looks for actions that go past the user's intent toward something destructive or irreversible. Example: delete remote branches when the user asked for a local tidy-up.
5. After a denial, Claude usually tries a safer path (for example, push to a new branch instead of a force push to main). After repeated denials, auto mode pauses and asks the human.
6. A server-side probe scans every tool result (web pages, files) for hidden instructions and adds a warning. An attack must pass the probe and the classifier. Anthropic reports zero attack success in its own evals (vendor claim).
7. Order of checks: deny, ask and allow rules run first. Then a tier check sends only risky actions to the classifier. Read-only and recoverable actions (search, edit files in the project) skip it. Shell commands, web fetches and anything outside the environment go to it.
8. By default only the working directory and its git remotes count as "internal". Your own servers and buckets count as external until you describe them.
9. Configuration: an `environment` field in plain English (GitHub org, buckets, internal services). Setting it replaces the built-in entries, so keep the default string. Admins set it in managed settings. Users can add but not remove admin entries.
10. Finer control: `allow`, `soft deny` and `hard deny` are guidance for the classifier, not hard rules. For hard limits, use permission deny rules and ask rules. Broad allow rules that grant arbitrary code execution still go to the classifier.
11. Rollout advice: start narrow, watch the denials, then widen. Review high-stakes actions (production infrastructure) yourself.

Short quote: "These fields are guidance the classifier factors into each check, not hard rules."

## Setup details

- Host: any Claude Code session (local, VPS, Remote Control). Auto mode is one of the phone modes in Remote Control (see O4).
- Cost: no extra cost named.
- Config: `environment`, `allow`, `soft deny`, `hard deny` (classifier guidance) plus normal permission `deny` / `ask` / `allow` rules (hard limits). Exact settings keys: check the auto-mode doc before use.

## IF/THEN rules for 741

1. IF an agent runs at night without Martin, THEN run it in auto mode, never in bypass mode, and put hard `deny` rules on FTP deploy, `wp` writes on live sites, mail send and `git push --force`.
2. IF a night agent must reach 741 infrastructure (Supabase project, portal host, Drive), THEN describe these in the auto-mode `environment` field. Otherwise the classifier treats them as external and blocks or pauses.
3. IF a rule must hold in every case (for example "never publish to a client site"), THEN write it as a permission deny rule. Do not rely on `soft deny` or prompt text.
4. IF auto mode pauses on a repeated denial overnight, THEN log it as a morning card. Do not widen the rule at night.
5. IF a new night workflow starts, THEN begin with a narrow allow set for one week and read the denial log before you widen it.

## Caveats

- Official vendor video. The 97% figure and the zero attack success rate come from Anthropic's own evals. No third-party check.
- The classifier is a model. It can still miss an action. Anthropic itself says to review production changes by hand.
- Field names in the video are spoken. Verify the exact settings syntax in the live docs.
