# Test scenarios — marketing-grill (Step 2.2, written BEFORE the skill body)

## 1. Obvious trigger
Input: "marketing grill" (or `/marketing-grill`).
Expected: the skill loads, confirms 741's current state is readable (knowledge base + memory files), and starts Round 1 (what to do) as an AskUserQuestion card, recommended option first, max 4 cards.

## 2. Paraphrased trigger
Input: "I don't know if I should be doing cold email or LinkedIn outreach right now, help me figure out 741's lead gen."
Expected: same pipeline as scenario 1 triggers — the skill does NOT give a quick opinion from memory. It reads the real infra state (e.g. `smartlead-cold-email` EXPIRED) before presenting options, so the cold-email option in the card is either removed or marked "needs a fix first," never presented as ready when it is not.

## 3. Must-NOT-trigger (negative)
Input: "write a LinkedIn post for 741 about our new pricing."
Expected: the skill does NOT trigger. This routes to `personal-posts` instead — the user is asking for content EXECUTION on an already-decided channel, not a channel-strategy decision. A correct non-trigger here is the single clearest signal that the `description` frontmatter's negative-trigger line is working (Rule R4.8).

## Additional must-NOT-trigger checks (not required by the gate, kept for Step 4.1 trigger testing)
- "build the content board for Praxis Suriya" → must NOT trigger (client workflow, `content-format-board`, out of this skill's scope).
- "prep me for my call with Katharina Kisser" → must NOT trigger (`sales-call-prep`, downstream of an engaged lead).
