# V04 — I Turned Claude Into a 24/7 Person Assistant (Full Guide)

- Channel: Albert Olgaard
- URL: https://www.youtube.com/watch?v=rRjvzY4h1xU
- Type: beginner guide with sponsor and course pitch, 11m 55s
- Upload date: 2026-09-22 (from the search listing. The transcript actor returned no upload date.)
- Views: 13,174 (at fetch)
- Fetch date: 2026-10-13 (Apify discovery + `johnvc/YoutubeTranscripts`, dataset `jkrUikamYc0lfnl76`. Raw transcript not stored here.)

## Extract (own words)

1. Core point: a local session stops when the computer shuts down. A Claude Code cloud session keeps running on Anthropic's machine.
2. Setup: create a private GitHub repo (he calls it "Claude OS"), connect GitHub in Claude Code on the web, install the Claude GitHub app, pick the cloud environment and the repo.
3. He says the cloud machine costs nothing extra, unlike a $10–20 per month server for OpenClaw or Hermes. Runs still use plan usage (see O1).
4. Routines: a saved task that runs on a schedule. His example: every morning, read new Gmail mail through the Gmail connector and draft replies.
5. Easiest way: ask Claude in a session to "create a routine in the cloud". He stresses the word cloud, because a local routine needs the computer on.
6. He tests the routine with a manual run from the same thread, then iterates on the prompt.
7. Drafts only: the routine writes reply drafts. He sends them himself.
8. Phone: in the Claude mobile app Code tab he sees cloud sessions, starts new ones and creates new routines (example: daily calendar plan sent as an email to himself).
9. His advice: do not chase every new agent tool (OpenClaw, Hermes). Stay with Claude or ChatGPT and automate real tasks.


## Setup details

- Host: Anthropic cloud (Claude Code on the web, cloud environment). No server to rent.
- Tools: GitHub repo, Claude GitHub app, claude.ai connectors (Gmail, Google Calendar), Routines page, Claude mobile app.
- Cost: subscription only. He gives no usage numbers.

## IF/THEN rules for 741

1. IF a night task needs only connectors and a GitHub repo (mail drafts, calendar brief, report pulls), THEN use a cloud routine. The Mac in Bali can sleep.
2. IF a routine has a write-capable connector (Gmail, Drive), THEN its prompt says "drafts only" AND you remove every connector it does not need. Routines run with no approval prompt (O1).
3. IF a routine is new, THEN run it once by hand and read the run output. A green status means only "no infrastructure error" (O1).
4. IF Martin is on the phone, THEN he reviews night drafts in the app and sends them himself. The agent never sends client mail.

## Caveats

- Thin on safety: it does not mention that routines run every connector tool with no approval. That fact comes from the official doc (O1), not from this video.
- Sponsor (HubSpot), own dictation tool and course pitch inside the video.
- Claim that "almost no one" uses routines is opinion.
- He signs into GitHub with Google and gives the app access to all repos. For 741, grant access to the one repo only.
