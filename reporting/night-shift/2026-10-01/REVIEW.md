# Night Shift 2026-10-01 — 6 pages · 5 pass · 0 needs_martin · 0 skipped · 1 not executed

## Praxis Suriya
- [ ] freigeben  **GBP · Öffnungszeiten & Termin-Button** (FEEDBACK) — pass
      → feedback/praxis-suriya/5bea6cb2-688d-4c24-b436-1a576e7ade75.md · Top-Fixes: —
- [ ] freigeben  **GBP · Öffnungszeiten, Termin-Button & Barrierefreiheit** (FEEDBACK) — pass
      → feedback/praxis-suriya/61abce05-2b04-49b4-b4ab-420ab4374080.md · Top-Fixes: Samstag/Sonntag-Öffnungszeiten beim Kunden bestätigen
- [ ] freigeben  **NAP / Citations / Domains — Ayurveda Domains** (FEEDBACK) — pass
      → feedback/praxis-suriya/d1c58471-eafc-4ef9-8418-1611a2345445.md · Top-Fixes: Domain-Wahl Ingelheim vs. Mainz mit Kunde bestätigen; Femalecare-Domain per Whois prüfen

## Praxis Hüwel
- [ ] freigeben  **Blog/Wissen — Homöopathie in den Wechseljahren** (FEEDBACK) — pass
      → feedback/praxis-huewel/9c65b15f-fac9-40a3-9b0a-0eafd41b1655.md · Top-Fixes: HWG-Beispielformulierung vor Veröffentlichung gegen `hwg-fallstudien-guideline` gegenprüfen; NAP für diesen Kunden fehlt in `client_locations`
- [ ] freigeben  **Einstieg & Angebot — Kontaktformular statt Weiterleitung** (FEEDBACK) — pass
      → feedback/praxis-huewel/44804cf6-c791-4a6a-b37d-836ec647aeb1.md · Top-Fixes: aktuell weiterleitende URL(s) auf der Live-Site identifizieren; NAP für diesen Kunden fehlt in `client_locations`
- **not executed:** Nachbarorte — tatsächliches Patienten-Einzugsgebiet (FEEDBACK, feedback_id `8c34ca68-c80e-4425-b32c-12f57a4953a0`) — plan item 5, Executor never started. See Note 1.

## Notes for Martin / dev

1. **A page was skipped by a script bug, not by the budget.** Plan item 5 (Hüwel,
   Nachbarorte) never ran. Cause: `reporting/night-shift.sh` line 113 counts pages with
   `len(p)` on the full `plan.json` object. `plan.json` now has 5 top-level keys (`date`,
   `generated_by`, `selection_rule`, `plan`, `deferred_note`), not 6 — the real page list is
   `plan.json["plan"]`. So `PAGES` was set to 5, and the loop stopped after index 4. This is
   the same bug the 2026-09-22 log named as "found" (then described as `len(plan.json)` read
   as a dict), but the fix was never applied to the script. It needs a one-line change: count
   `len(p["plan"])` instead of `len(p)`. No budget limit was hit — only 11–12 of 14
   invocations were used.
2. **`processed-feedback.json` is still empty.** All 5 items above have each, in their own
   "Hinweis an Martin" section, already flagged that they are repeats: the same comments
   passed in the 2026-09-15, 09-16, 09-18, 09-22, and 09-28 runs. This is the 5th run in a
   row reporting this. Once you tick `[x] freigeben` and apply a reply, add that
   `feedback_id` to `reporting/night-shift/processed-feedback.json` so the night run stops
   re-staging the same comment.
3. **`state.json.budget.invocations_used` shows 2**, but the run made at least 1 Planner +
   5 × (Executor + Critic) = 11 calls for the 5 executed items, plus this Reviewer call. The
   counter is not updated by every role — same tracking gap flagged on 2026-09-28. Not a
   budget breach (wall-clock and invocation caps were respected), just an inaccurate number.
4. **Missing locked NAP record for Praxis Hüwel.** Both Hüwel items tonight
   (`9c65b15f`, `44804cf6`) flag that `context.json.nap_locked` has no entry for client_id
   `f0a6730f-8f56-4c61-8085-1955f3bb285a`. Please add a `client_locations` row with
   `nap_status='locked'` for this client so future runs can NAP-check Hüwel drafts
   automatically.
5. **A newer, still-open client comment is relevant to item 2 above.** The
   `61abce05` draft notes that on 2026-08-31 the Suriya client left a further comment
   (feedback_id `7fd15e89-27b8-426c-a28a-d88998ef37b1`, same GBP section): "Öffnungszeiten
   kannst DU ändern wie du möchtest" — an explicit go-ahead for the hours change in items 1
   and 2. That comment was not part of tonight's plan and was not processed, but worth
   knowing when you approve the hours change.
