# 2.1 Use cases (automation-completion)

Reusing the 3 use cases already approved for `automation-build` at checkpoint 1
(design-note.md, 2026-10-11), plus one new one for this specific build:

1. `/automation-build Marcel Skool funnel` — trigger: Martin or a client chat starts a new
   CRM/email funnel build. Steps: P0 inventory (read only) -> P1 spec -> go spec -> P2
   environment/TEST data -> P3 build draft/off -> P4 test -> P5 verify -> go-live gate ->
   P6 go-live per action -> P7 monitor/handover. Tools: Claude in Chrome, Bash/python
   scripts, Agent (verifier subagent). Result: a built, tested, documented automation with
   a runbook, no untested "done" claim possible (Stop hook blocks it).
2. `/automation-build Stürzl lead intake` — trigger: a Supabase-backed funnel (edge
   function + portal write) needs building or fixing. Same pipeline; deploy step is class
   G (needs `go A<n>`).
3. `/automation-build 741 phone agent` — trigger: an internal 741 automation (Twilio ->
   ElevenLabs -> n8n -> Supabase). Martin owns the accounts; class-M setup steps go into
   `martin-steps.md` for him to click; build/test proceeds around that.
4. (New, for this id) "Martin says the Marcel automation kept failing to finish cleanly,
   we need our own workflow for this" — trigger: a repeat failure of the kind
   automation-build already targets. Steps: confirm whether a workflow already exists for
   this (it does) -> finish/install it rather than redesign -> prove it on the next real
   automation task. Result: the existing safety net (hooks + skill) actually runs, instead
   of a second design document that risks the same fate (approved, then unused).
