# Test scenarios — personal-posts (written before the skill body, per R1.2)

## 1. Obvious trigger

**Input:** "/personal-post I hate the lie that gets paraded around — like a company that says 'we're all a family'..." (Martin's full quoted opinion from the grill, see `voice-interview-raw.md`).

**Expected:** Skill loads. It drafts one core voice take, adapts it into 4 platform versions, runs the slop lint on each, shows Martin all 4 for his go, and does not post or schedule anything. No client is named, no number is invented.

## 2. Paraphrased trigger

**Input:** "write a LinkedIn and X post from this thought: most agencies lie about being a family, we should say what we actually think."

**Expected:** Skill loads even without the literal word "post" command and without naming all 4 platforms explicitly — it recognizes "write a post from this thought" plus named platforms (LinkedIn, X) as the same job, and only drafts those two platforms (use case 3, text-only, no image step triggered).

## 3. Must-not-trigger (negative)

**Input:** "Write the homepage copy for Praxis Suriya" (a client page-copy request) — or — "Post this update to the client portal for Bali Healing" (a client-facing delivery task).

**Expected:** Skill does NOT load. The first is `content-writing`'s job (client-voice page copy, not Martin's personal voice). The second is a client portal/status update, not a personal social post. `personal-posts` must stay scoped to Martin's own voice on his own social channels only — never a client's voice, never a client-facing surface.
