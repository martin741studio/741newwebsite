# 4.1 Trigger tests — booking-sequence (fresh subagent session, Sonnet, 2026-10-14 ~14:50 WITA)

Method: a fresh general-purpose agent got the 4 prompts from test-scenarios.md, chose a skill from its available-skills list per prompt, and called the Skill tool to confirm the load. No workflow step was run.

| Prompt | Expected | Chosen | Loaded | Deciding words (agent's quote) | Result |
|---|---|---|---|---|---|
| T1 cal.com paste (Sabine) | booking-sequence | booking-sequence | yes | "A new event has been scheduled", "30 min meeting between 741 Studio and …", a phone number | PASS |
| T2 German paraphrase (Manuela, "hat … einen Termin gebucht … Bereite die Nachrichten … vor") | booking-sequence | booking-sequence | yes | "hat einen Termin gebucht", "bereite die Nachrichten nach der Buchung vor" | PASS |
| T3 Loom URL + WhatsApp message (must NOT trigger) | not booking-sequence | local-seo-review-page | yes | "a Loom URL for a review page"; booking-sequence "Do NOT use for … its Loom/final message" | PASS |
| T4 new review page (must NOT trigger) | not booking-sequence | local-seo-review-page | yes | "review page for <name>", "Use for every LOCAL prospect" | PASS |

**4/4 passed.** Agent's risk note: T2 and T3 name the same person; the negative trigger line separates them. Kept as is.
