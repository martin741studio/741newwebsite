# 3.6 House rules applied in the canary skill

- Client message + Drive link at the end: N/A — a canary's deliverable is an alert/registry row, not a client deliverable. The Marcel key-request message (00_project/assets/marcel/canary/msg-marcel-read-keys.txt) went through the German slop check (5/5) before being handed to Martin.
- Per-change "go" for live sites: enforced in Critical — canaries never change a client website; Mode B step 4 requires `allowlist.py` + Martin's go for any write.
- Verified data only: Mode A step 7 runs each check once by hand before marking it live; Mode B step 2 re-checks the signal before acting.
- STE in replies: SKILL.md itself and all references are written in STE (active voice, short sentences, one idea per sentence), matching this build's own replies.
- Questions to Martin only as AskUserQuestion cards with a recommendation first: stated in Critical, used throughout the hand-run (C1–C13).
- No tool/provider names in client-facing messages: N/A, canaries never message clients; internal messages and the Zapier/UptimeRobot names are fine in 741-internal references.
- Ads hard limit (no change without reasoned go): stated in Critical and in references/allowlist.md "Never allowed".
- Email only via Airmailer with a go: canaries alert via Telegram, not email, so this does not apply to the alert path; if an email alert is ever added it must go through Resend `alerts@741.studio` per the Automation Build plan, never via Airmailer (Airmailer is for human-to-human mail).
