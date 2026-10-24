# Test scenarios (step 2.2) — written before the skill body

## 1. Obvious trigger
"Build a content format board for Little Frenchie Bali."
Expected: skill loads, finds `00_project/prospects/little-frenchie-bali/`, reuses existing intake/demand/competitors data, sources real public questions, produces `content-format-board.md` with the plain-English format labels, flags readiness check + on-camera person as open questions.

## 2. Paraphrased trigger
"What video content should we pitch Little Frenchie with — give me some format ideas."
Expected: same skill loads and produces the same deliverable; the paraphrase ("format ideas", "video content", "pitch... with") must not require the exact words "content format board".

## 3. Negative trigger (must NOT load)
Three distinct must-not-trigger cases, each belonging to a different existing skill:
- "Write the homepage copy for Little Frenchie." → must NOT trigger `content-format-board`; belongs to `content-writing`.
- "What keywords should Little Frenchie's blog target?" → must NOT trigger; belongs to `content-pool`.
- "Write a LinkedIn post about my own take on Bali restaurants." → must NOT trigger; belongs to `personal-posts` (Martin's own voice, out of scope per `inputs-grill.md`).
- "Make a before/after Local Falcon story for Little Frenchie." → must NOT trigger; belongs to `social-visuals`/`story-automation-system`.
