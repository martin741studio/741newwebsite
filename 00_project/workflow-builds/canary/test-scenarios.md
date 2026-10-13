# 2.2 Test scenarios — canary (written 2026-10-14, BEFORE the skill body)

Run each in a fresh session (step 4.1). Pass = skill loads for T1 and T2, not for T3–T4.

## T1 — obvious trigger
Prompt: "Set up a canary for Marcel's Gewinnspiel funnel."
Expected:
- `/canary` loads (add mode).
- Reads the registry and the incident file. Proposes checks from the catalogue: page + form liveness, Zap state, Zap error push, reconciliation Tally → Pipedrive / KlickTipp.
- Writes one registry row per check: client, system, check type, interval, threshold, owner, self-heal action (allow-list id), escalation path.
- Runs the check once and shows the result. Fires ONE test alert and proves it reached the agreed channel (timestamp sent vs received).
- Changes nothing in Marcel's systems without a go. Sends no message to Marcel.

## T2 — paraphrase (German, no keyword "canary")
Prompt: "Pass auf, dass das Kontaktformular von Bali Healing nicht wieder still ausfällt, und sag mir sofort Bescheid, wenn keine Anfragen mehr reinkommen."
Expected:
- `/canary` loads (add mode). Recognises an absence-of-signal case.
- Proposes a heartbeat / reconciliation check (expected leads per window from real history, not a guess) plus page + form liveness.
- Asks only what it cannot read itself, as AskUserQuestion cards. Registry row + test alert as in T1.

## T3 — must NOT trigger (build work)
Prompt: "Baue für Marcel die Zapier-Automation für sein neues Webinar: Tally → KlickTipp → Pipedrive."
Expected: `/canary` does NOT load. The automation-build workflow handles it. (Its go-live step may later hand over to `/canary` to add a check.)

## T4 — must NOT trigger (performance reporting)
Prompt: "Wie lief Google Ads bei Bali Healing diese Woche? Kosten pro Lead bitte."
Expected: `/canary` does NOT load. This is reporting, not an outage. (An Ads canary covers only "stopped / not spending / disapproved / billing / tracking dead".)

## T5 — incident mode (functional, used in 4.2)
Input: alert payload "CANARY marcel-gewinnspiel-recon: 6 Tally submissions, 0 Pipedrive deals in 60 min".
Expected:
- `/canary` incident mode. Re-checks the signal first (no alert on one failed read).
- Diagnoses from the Zap run history (read-only), names the failing step and the error.
- Runs only allow-listed fixes (for example replay after root-cause fix), else escalates with one decision card: what broke, since when, impact, proposed fix, what go is needed.
- Logs the incident with detect / alert / ack / restore times. Never edits Ads, never edits a live site, never messages the client, never types a credential.
