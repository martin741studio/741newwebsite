# Morning Grill Decisions (2026-10-21)

## Card 1: Portal bug — Kontakte/Newsletter/Anfragen tabs hidden (Hüwel, Suriya, Stürzl)
**CORRECTED (investigated live):** Not a bug. Each client has only ONE of two feature flags (`client_stack.contacts`/`leads`) set: STÜRZL has leads (Anfragen shows, her own lead-CRM feature), Suriya and Hüwel have contacts (Kontakte/Newsletter shows). Kontakte/Newsletter was built specifically for Hüwel as his ONLY INSIDE replacement — not meant to roll out to Suriya/Stürzl.
**Martin's answer:** Hüwel should also get the Anfragen tab (leads).
**Action done:** `client_stack.leads = true` set for Praxis Hüwel (f0a6730f...) in Supabase 741-portal. Tab is live now. Note: 0 leads exist yet (contact form not wired to the leads table) — tab will show empty until that separate build is done.
**Owner:** Agent (done)
**Due:** 2026-10-21
**Status:** done

## Card 2: Gayo contract v7.2 — signing channel
**Martin's answer:** a — Email to Gayo, cc Ibu Made, Gayo signs first
**Action done:** Email drafted (5/5 slop-checked), both v7.2 Google Doc links included (EN + Bahasa). Martin sends himself — no email address on file locally for Gayo/Ibu Made.
**Owner:** Martin (send)
**Due:** 2026-10-21
**Status:** done (draft delivered)

## Card 3: Malware watch — Katharina Kisser + Physio Kraft
**Martin's answer:** b — Step down to hourly checks
**Action:** Agent switches both sites from 30-min to hourly watch cadence.
**Owner:** Agent
**Due:** 2026-10-21
**Status:** open

## Card 4: Hüwel content-pool report — review
**Martin's answer:** a — Open now (walk queue)
**Action:** Martin reviews 00_project/assets/huewel/content-pool/05-report/content-pool-report.html himself.
**Owner:** Martin
**Due:** 2026-10-21
**Status:** open (walk queue)

## Card 5: Bali Healing audit report — review
**Martin's answer:** a — Open now (walk queue)
**Action:** Martin reviews 00_project/assets/audit/balihealing/<run>/findings.json himself (Score 46/100, Verdikt Offen).
**Owner:** Martin
**Due:** 2026-10-21
**Status:** open (walk queue)

## Not re-asked (already decided 2026-10-20, still in progress)
- Suriya 29/25 directory emails: list delivered (suriya-directory-citations-full.csv), Martin has not gone through it yet — carried forward as waiting_for, not a new card.
- 741 overdue tasks (71 today vs 58 yesterday — portal counter not yet updated from yesterday's reconciliation work): carried forward, not re-asked.

## Gaps found by the 06:13 scheduled run (gaps-scheduled-run.md) — resolved or deferred, not re-asked
1. Ulrike Röth call-time contradiction: moot, the 20.10. 16:00 slot has passed; 21.10. 14:00 is the one on calendar, matches Martin's 20.10. decision.
2. Katharina Kisser / Physio Kraft new admin passwords + Wordfence 2FA + forms/booking plan + Physio GSC spam cleanup: ALL already queued for today by the dedicated security-incident session (transcript f203e46d), which has full WHM context and Martin's "yes, tomorrow morning" answer from 20.10. 21:30. Not duplicated here — that session owns execution.
3. STÜRZL reminder email contradiction: resolved live in this session — Martin confirmed "das war von mir heute beauftragt, es ist ok" (he commissioned the email send himself, overriding yesterday's "no client email" correction for that specific case).
4. Night queue (8 candidates from 20.10. evening): deferred to tonight's 17:00 run.
5. Katharina Kisser / me&you overlay rows: fixed — both added to morning-grill-goals-overlay.json, regenerated goal sheet now shows 15 clients, old warning gone (new smaller warning: no work_phases row, lower priority).
6. Evening log 20.10.: still Martin's to confirm — carried to next evening run if not confirmed today.
