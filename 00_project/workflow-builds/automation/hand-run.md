# 2.3 One real task, solved by hand (automation-completion)

Real task used: the client chat "Marcel Rosenbach — NLP-Funnel Automation"
(session local_61b8f208-18a7-4a11-981d-0fb3170dad82), read directly (list_events, paged
back through ~380 of 3,521 messages across 2026-10-14, plus the existing synthesis at
`00_project/workflow-builds/canary/incident-marcel-2026-10-13.md` which was built from the
same transcript with exact timestamps). Not sent a message to the session, per the brief.

What the incident showed (2026-10-08 to 10-14), already catalogued by the canary workflow
and cross-checked here:
- Zap built 2026-10-08, published and reported as "live and tested" with step tests
  skipped ("no junk data in Marcel's accounts").
- A custom-value tag (`100456`) was later found to be a KlickTipp *label*, not a *tag* —
  the write silently failed with HTTP 406 on every real signup from 2026-10-11 onward.
- 23 real signups lost before detection; Zapier auto-paused the Zap and mailed the error to
  Marcel's own inbox, not 741's; Martin saw it 8.5 hours after Marcel forwarded it.
- Fix required Martin's own logins (expired Zapier/KlickTipp sessions) because the agent
  never holds write credentials itself.

What I observed directly in the 2026-10-14 recovery (the "context I had to supply" that
rule 2.3 asks to extract):
- A second root cause only surfaced because someone manually re-read the Tally form
  settings: "redirect on completion" was off, so participants never saw the confirmation
  page — a check nobody had written down as a thing to verify.
- The recovery work already applied, by hand and under direct instruction each time, the
  exact rules automation-build encodes: test only in a separate test campaign/tag
  ("Ich teste nie an etwas, das live laeuft" — added as a hard rule the same day), read the
  state back after every click (screenshots), get an explicit "go" before starting the
  live campaign for all contacts, and stop entirely afterward ("Heute fasse ich in Marcels
  Konto nichts mehr an").
- Martin raised, unprompted, in this same chat: "zapier has ai teammates i think you could
  even with them setup very fast zaps" — this is the direct source of topic 2 in the brief.
  The agent had already added a P3a step to the skill draft the same day: let Zapier's own
  Copilot/Agents draft the first version, check which account it's bound to first, and
  never count the AI's own draft (or its own "tested"/"published" prompts) as evidence.

Conclusion for the skill body: every piece of context supplied by hand on 2026-10-14 is
already a line in the automation-build skill draft or its hooks (test-only data, readback,
per-action go, P3a). Nothing new needs to be invented. What needs to happen is: install it,
so the NEXT real task runs inside the guard rails instead of needing a human to remember
and re-apply them live, under pressure, after real signups were already lost.
