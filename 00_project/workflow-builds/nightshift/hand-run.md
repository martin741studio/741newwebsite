# 2.3 One real task by hand — evening hand-over 2026-10-13

Task: turn today's real evening log (`00_project/assets/morning-grill/2026-10-13/evening-log.md`, draft 17:00) into a night queue card, the way the 17:00 run will do it (decision N10). Done by hand at 18:05 WITA.

## Step 1 — filter the log by hand

Rule used: an item is a night candidate only if (a) the owner is "agent" or nobody, (b) it is in a night class (N3: research/data pull, draft, server build + QA, public audit), (c) it needs no login in Chrome, no live write, no send, no spend.

| Log line | Client | Class | Night? | Why |
|---|---|---|---|---|
| Full scan of the Oberhausen site | Kamil | public audit | YES | read-only crawl of public pages after the Kraft hack |
| FAQ questions missing on 4 pages | Maria Brasse | draft | YES | FAQ drafts as files, release by day |
| Similar Treatments + video on 10 Beauty pages, due 16.10. | Bali Healing | draft | YES (draft part) | copy blocks as drafts; the live edit stays a day task |
| GSC export: 35 opportunities | STÜRZL | research | YES | analysis + page recommendations from the existing export |
| 30-day measurement + before/after grid | Suriya | data pull | PARTLY | read existing Falcon scans only; a new scan spends credits → day card |
| Mark 2 GA4 key events | Hüwel | live config | NO | live change in GA4 → day, owner agent with go |
| Cleanup physiotherapiekraft.de | Kamil | live server | NO | live write, security incident → day |
| Quarter goal empty | Taxi Nürnberg | draft | MAYBE | proposal only; Martin's words needed → morning card |
| Night-shift feedback items (Suriya, Rabenmütter) | — | draft | NO | the repeat bug (processed-feedback.json never written) |
| Content-pool upload to Drive | Bali | write to Drive | NO | external write → day |

## Step 2 — the card

Card "Night queue 13.10." with the 4 YES items, max 8 items, class + client per line, recommendation = run all 4. Asked in grill round 4 (AskUserQuestion, multiSelect). Martin's answer → `decisions.md`.

## Context I had to supply by hand (→ becomes skill body / scripts)

1. The routing table "owner agent vs Martin" exists only in the log text. The night planner needs it as data (`tasks.json` owner + class field).
2. A class per item (N3 classes + "never" list). The log has no class field → the 17:00 run must add `night_class` per open agent task.
3. "Spends money/credits" is not visible in the log (Falcon scan). Needs a deny list of credit-spending tools (Local Falcon run_scan, DataForSEO live SERP beyond a cap).
4. Chrome-bound or login-bound items must be marked → they go to the morning click cards, never to the night.
5. Live-system words (GA4, Wix publish, FTP, cleanup, upload) → automatic NO.
6. Due dates (Bali 16.10.) raise the rank.
7. Security state matters: the log names an infostealer on the Mac (13:49 WITA) and a password rotation. The server must only get keys that were rotated after that.
8. The old night-shift planner reads only portal tasks + `report_feedback`. It must read the confirmed night queue instead (N10).
