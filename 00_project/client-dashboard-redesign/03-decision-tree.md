# Decision tree — client dashboard and reports (state 2026-10-13, after round 6)

All 24 decisions come from Martin's grill-me answers. Detail and wording: `decisions.md`. Sources: `00_project/knowledge/client-dashboard-library/` (A–F).

```
Client portal (EN for Bali, per clients.lang)
|
+-- Look (21): cream, 741 yellow as accent, DM Sans, neutral chart ramp, four fixed status colours (14)
+-- Figure (22): Overview + empty states, max 1 per page
+-- Words (3): plain words, technical term in small grey print; "Top-3 coverage 31 of 49 spots" (12)
+-- Numbers: every number has a date and a source; gaps show as "Not measured yet", never zero or estimate
|
+-- Tabs (17): Overview | Results | Plan | Decisions | Reports   (+ Setup while open, Chat button always)
    |
    +-- Overview (5, 8): three cards, each one number + one sentence
    |     Enquiries | Found on Google | 741 at work   -> then "Needs you" (13)
    |     Sentence: auto-draft, 741 checks weekly (8)
    |     Frame (13): banner sentence -> Needs you -> phase line -> 741 works on (max 5) -> next 4 weeks -> done -> who to ask
    |
    +-- Results (first screen: 4 numbers + 1 sentence per page, 1)
    |     +-- Enquiries (9): answer line + 4 tiles, 6 monthly columns, current month hatched, dashed "not tracked" slot
    |     +-- Found on Google (11): sentence + 3 tiles -> big grid -> You win / Close / Missing -> competitors -> AI strip; all keywords behind a link
    |     +-- Reviews (10): rating, count, unanswered + bars you / leader / target (2x) + monthly pace
    |     +-- Ads (6, 7, 15): IDR only, no 741 fee; 3 tiles + weekly bars + "Booked jobs: not tracked yet" card
    |     +-- Backlinks (16): 5 step rows + 4 health tiles, plain words
    |
    +-- Plan (19): 12 tracks in 3 stages | site structure outline | content plan 19 first
    +-- Decisions: existing module (client-approval-workflow)
    +-- Reports (24, 2): dated archive, old versions "replaced"
    +-- Setup (18): while open; 7 platforms with check date; open steps go to "Needs you" after week 2
|
+-- Status (14, 20): colour = health only; thresholds red / amber 3 and 7 days / grey 10 days; client banner only after Martin releases
+-- Production (23): Results pages from data in one template; special documents by hand with the same rules
+-- Pilot (4): Bali Healing only; roll out after Martin's go
```

## Still open
1. Data readiness for Bali: `02-data-readiness-bali.md` (agent running).
2. Clickable prototype (desktop 1440 and mobile 390) with real Bali data.
3. Build on staging, tests, Martin's go for live (portal single-file rules).
4. Roll-out order for the other clients.
5. Link to the tracking design: which of the 34 metrics (M01–M34) feed which page. Draft after the data check.
