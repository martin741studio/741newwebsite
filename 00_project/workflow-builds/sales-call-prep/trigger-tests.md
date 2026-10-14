# Trigger tests (step 4.1) — fresh subagents, frontmatter only

Each test used a fresh Agent (general-purpose subagent, no memory of this build) that read
ONLY the frontmatter `description` of `sales-call-prep` (and, for scenario 3, `booking-sequence`
too) and judged whether it would trigger for the exact message — a direct proxy for how the
real skill-loader decides from the description alone.

## Scenario 1 — obvious trigger
Message: "Bereite mich auf den Call mit Korinna Heintze vor, der ist am 26.10."
Result: **YES** — "The message matches its German trigger phrase 'Call mit <name>
vorbereiten' almost exactly ... squarely in scope." PASS.

## Scenario 2 — paraphrase
Message: "Ich hab in 20 Minuten den Call mit Korinna, gib mir schnell die wichtigsten Punkte."
Result: **YES** — "The description's phrasing is broad enough (covers paraphrases naming a
call + a person), not literal-phrase-only, so it would catch this message." PASS.

## Scenario 3 — must NOT trigger (on sales-call-prep); booking-sequence should
Message: "Schreib die WhatsApp-Nachricht für morgen an Korinna."
Result: **booking-sequence only** — "sales-call-prep's description explicitly scopes to
Martin's own call prep and says 'Do NOT use to write or send any message TO the prospect' ...
the separation works clearly." PASS.

All three match the expected outcome from `test-scenarios.md`. No description change needed.
