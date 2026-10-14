# What 741-agents-01 needs access to — full inventory

Requested by Martin (14.10., "list down what it needs to have access to so that's all done, I don't want to do it when it comes to the point"). One list, grant in one sitting instead of piecemeal. Nothing below is done yet except where marked DONE.

## A. Already working (no action needed)

| What | How | Status |
|---|---|---|
| GitHub repo | `git clone` / `git pull main`, deploy key | DONE (cloned 14.10., 88ad0b69) |
| Claude Code — batch calls (`claude -p`) | `CLAUDE_CODE_OAUTH_TOKEN` in `~/.claude-oauth-token.env` | DONE |
| Claude Code — interactive / Remote Control | `claude auth login` (full account login) | DONE |
| Tailscale (private network) | joined, public SSH closed | DONE |

## B. Easy to add — API key or service account, no browser, no ongoing login

These never need Chrome. Once added they just work, same as on your laptop. Recommend read-only keys where a read-only key exists.

| What | For | Where the key lives today | Action |
|---|---|---|---|
| DataForSEO | keyword/volume/backlink data (audit, pool, CRO) | `.secrets/dataforseo.env` | copy the key to the server's `.secrets/` (read-only key if DataForSEO offers one) |
| Apify | scraping actors (research, YouTube transcripts) | `.secrets/apify.env` | copy key |
| Google service account (GSC/GA4 reporting) | Search Console + GA4 reads for client sites | `.secrets/ga-sc-reporting-bot.json` | copy file |
| Local Falcon | ranking grid scans | remote MCP, key in Claude config | add the Local Falcon MCP + key to the server's Claude config |
| Supabase (portal) | reading tasks/clients, writing scoped rows (e.g. night cards) | machine users already exist for other jobs (`standup-bot@741.studio` pattern) | create one more scoped machine user for general server work, RLS-limited |
| **Google Drive** | uploading deliverables, reading client folders | currently browser-only (risky JS-click workaround) | **recommend switching to a Drive API service account** instead of browser upload — handles binary files properly, works from the server with zero Chrome. One-time setup: create the service account in Google Cloud, share the relevant Drive folders with its email address |
| Novamira (WordPress) MCPs | reading/auditing client WordPress sites | API token, already connects | works from server already for reads; **writes stay day-only, per-change go**, same rule as the laptop |

## C. Hard — needs a real logged-in browser (not built yet)

This is the noVNC/Chrome build we scoped and paused ("finish Remote Control first"). Until it exists, these stay on the laptop:

| What | Why it's hard | Workaround until built |
|---|---|---|
| Google Business Profile (GBP) edits/reads via UI | needs your logged-in Google account in a real browser | stays laptop, or switch specific reads to the GBP API (possible, separate small project) |
| ChatGPT (image mockups in CRO workflow) | tied to your personal ChatGPT subscription/session | stays laptop — this one is hardest to move since it's literally your account, not a service |
| LinkedIn CRM | needs your logged-in LinkedIn session | stays laptop |
| Any ad-hoc "log in and look" check (client CMS without API, etc.) | one-off logins, 2FA, CAPTCHAs | stays laptop until the browser-blocker build exists |

## What this means for a given workflow right now

A workflow only runs fully on the server if NONE of its steps touch section C. Today, that's: Night Shift's item types (drafts/research/public audits), and any workflow's early DATA-GATHERING steps (DataForSEO pulls, Firecrawl crawls, content drafting). Final visual checks, Drive uploads (until B's Drive API fix lands), GBP, and ChatGPT steps still need the laptop.

## Recommended order to grant B (one sitting)

1. Google Drive service account (biggest unlock — removes Drive from the "hard" list entirely)
2. DataForSEO + Apify + GSC/GA4 service account (copy existing keys, 5 minutes)
3. Local Falcon MCP + Supabase machine user (needs me to wire the config, you just approve)
4. Novamira read access (already works, just confirm it on the server once)
