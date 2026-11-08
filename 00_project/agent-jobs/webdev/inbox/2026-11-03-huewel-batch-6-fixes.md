---
agent: webdev
client: huewel
site: https://praxis-huewel.de
page: multiple (see list below) — each on its own test branch already
spec: existing test-branch builds; no new prototype needed
milestone: none — Hüwel has no roadmap.json; this comes from the Project Manager's day-1 batch review, 2026-11-03
from: Project Manager day-1 list, 2026-11-03 (card "Hüwel 6 fixes", Martin answered "Go for all 6 today")
deadline: 2026-11-03
done_when: each of the 6 items below is swapped live, with before/after desktop + mobile screenshots in the outbox and the page-content QA checklist passed
---
Notes: All 6 are already built on a test branch; none is blocked by anything except Martin's go, which is now given. Work one at a time, screenshot each, swap, then move to the next.

1. `work_items` `a2e6e657-4c9d-45d0-b8a1-14ef224dd351` — replace "Bioscan" with Hüwel's own term. Client approval on file: `approval_items` E3, chosen A, go 2026-10-14.
2. `work_items` `f1b3fa29-4c59-4d0d-9b61-986dddf2cffd` — Ondamed-Therapie page heading: add "Magnetfeldtherapie (PEMF)". Client approval on file: E5, chosen A, go 2026-10-14.
3. `work_items` `96147eb0-e3ea-4d72-852c-a4dd8b3f2d1e` — two new Anliegen pages (Schmerzen und Verletzungen; Stress und Erschöpfung). Client approval on file for building them: E8, chosen A, go 2026-10-14. **Flag:** the page TEXT for "Schmerzen und Verletzungen" (E11) is still `ready`, not `go` — check with Martin before swapping that one page's text live; the structural go does not cover its final wording.
4. `work_items` `9155336a-4080-4211-8849-23e981a85634` — 3 blog posts: adjust the sentences that state a treatment effect. Client approval on file: E6, chosen A, go 2026-10-14.
5. `work_items` `9d32c600-1f0a-47c5-a28d-38e3741081fe` — homepage: remove 3 of 5 testimonials, keep 2 neutral ones. Client approval on file: E2, chosen A, go 2026-10-14.
6. `work_items` `59b58540-d1ce-40a7-8726-df2dee61d619` — re-cut the intro video: remove two sentences that state a treatment effect ("sehr effektiv", "Freude und Lebensqualität zurückbringen"). **Flag:** no `approval_items` row matches this exact edit. E7 (go, chosen C) and E9 (ready, chosen B) both concern a different question — the video's size and position in the header, not these two sentences. Confirm with Martin that the sentence removal itself has the client's go before this one ships; it is a health/effect claim, so treat it like any other HWG-relevant text under the usual review.

Report back into this inbox folder's outbox, or the Project Manager's outbox, naming which of the 6 shipped and which (if any) you held for the two flagged reasons above.
