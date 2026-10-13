# 4.2 Functional test — real night 2026-10-13 (fresh sessions by design: every run is a new `claude -p`)

Trigger: LaunchAgent studio.741.night-shift-v2 at 20:30:07 WITA, queue reporting/night-shift/queue/2026-10-13.json (4 items confirmed by Martin's card).
Result: finished 20:50:22 · 10/14 runs · est. USD 4.23/10 · stop: queue done · violations 0 · `validate_night.py 2026-10-13` → PASS (14 OK lines).

| Item | Verdict | Time | What Martin did at the 21:30 check-in |
|---|---|---|---|
| bali-beauty-similar | pass (1 attempt) | 2:17 + 0:56 | Accept, swap flagged link → done in the draft, sent to the Bali Wix chat |
| brasse-faq | needs_martin (2 attempts) | — | Premise wrong (all 12 texts have FAQs). Chose "check the live pages" → candidate for tomorrow's queue |
| stuerzl-gsc-chancen | pass | — | Found 3 profile pages with traffic; live check: Euler + Kellner pages 404, Bruckmeier current → client decision card for Anja (Stürzl chat) |
| kamil-oberhausen-audit | pass | — | "Muss raus, spam" → 2 spam footer links sent to the Kamil chat for removal |

Where it stalled or guessed: Brasse executor and critic disagreed (critic wanted [fehlt] marks on a "no work needed" result) → 2 extra runs. Fix idea: allow verdict "premise_wrong" that goes straight to needs_martin without a retry.
Check-in: in this chat via Remote Control, 4 cards, all answered in one round.
