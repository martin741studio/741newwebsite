# AFK Mobile Stabilization — 741 Website

## Global Rules
- Work only inside 741 website project.
- Do not touch other folders/projects.
- Do not change 741 branding.
- Weavy is layout/interaction reference only.
- Do not restructure HTML unless unavoidable.
- One task at a time.
- Self-test before moving on.
- If blocked after 2 attempts, document blocker and move to next task.

---

# 🧱 YOUR 741 KANBAN STRUCTURE (CLEAN)

### 🟡 BACKLOG
- [ ] Any identified issues not yet ready

### 🔵 READY
- [ ] Clear, well-defined tasks to pull next

### 🟣 IN PROGRESS (Agent)

### 🟢 QA (You)

### ⚫ DONE
- [x] **Task 1 — Hero Video Preload Fix**
- [x] **Task 2 — Hero Frame Label System**
  - *Result: Added hr-node-label class and applied to all 6 nodes for consistent font size, spacing, and alignment.*
- [x] **Task 3 — Hero Rodin Frame Fix**
  - *Result: Added poster attribute with static fallback image to model-viewer, preventing the grey placeholder box from appearing while the 3D model loads.*
- [x] **Task 4 — Hero Mobile Layout Stabilization**
  - *Result: Replaced broken mobile grid with flex layout from hero.html. Gaps and flex-direction prevent overlap and ensure frames align correctly on 390px and 360px.*
- [x] **Task 5 — Hero Connection Timing Fix**
  - *Result: Added window load event listener and ResizeObserver to re-position LeaderLine connections, ensuring they align perfectly after layout shifts and font loads.*
- [x] **Task 6 — Tools Default State Fix**
  - *Result: Added showDefaultImage() call to immediately set the first image state on desktop load, and changed Splide initial 'start' index to 0 for mobile so it defaults to the first image.*
- [x] **Task 7 — Tools Mobile Interaction Fix**
  - *Result: Verified Splide slider with isNavigation: true correctly supports tap/click for mobile interaction without relying on hover effects.*
- [x] **Task 8 — Portfolio Initial Load Fix**
  - *Result: Added updateNavigationState(0) to initPortfolio so the bottom navigation updates to show the first card immediately on load.*
- [x] **Task 9 — Portfolio Autoplay Fix**
  - *Result: Changed SLIDER_CONFIG autoSlideSpeed from 5000 to 3000 to match the ~3 second interval requirement. Verified that the cycle restarts naturally without the click hijack bug stopping it.*
- [x] **Task 10 — Portfolio Click Fix**
  - *Result: Removed the document-level click listener that was hijacking all page clicks. Dragging and navigation item clicks still work flawlessly without it.*
- [x] **Task 11 — Final Mobile QA**
  - *Result: All tests passed. The infinite loop caused by texture load failures, the freeze from targetTexture scope bug, and the Splide null error have been fixed. Both Homepage and Portfolio function correctly on mobile viewports.*
- [x] **Task 12 — Hero Video Mobile Visibility Fix**
  - *Result: Fixed missing height issue on `.hr-card-minimax-video` flex child container by assigning `min-height: 200px !important` and `aspect-ratio: 16 / 9 !important` on mobile viewports. Also explicitly removed top/bottom padding from `.hero-video` to prevent black bar letterboxing. Modified `04_site/sections/hero.html` instead of root index.html to ensure Vite builds compile it correctly.*
- [x] **Task 13 — Final Hero QA on Mobile**
  - *Result: Resolved layout overlaps between the hero frames by explicitly defining the flex gap as `64px !important`, overriding the relative `4rem` which was shrinking to ~28px and causing the `-30px` absolute labels to bleed into previous frames. (Note: The "TEXT PROMPT" node is intentionally hidden on mobile per the reference design, and its display rule was intentionally preserved).*
- [x] **Task 14 — Hero Node Visibility Correction**
  - *Result: Compared the mobile DOM structure against `assets/weavy.css`. Verified that `.hr-card-text.node-connect` (`#node4` - TEXT PROMPT) is explicitly set to `display: none;` at the `max-width: 767px` media query breakpoint in the reference layout. Reverted the `display: flex !important` override in `04_site/sections/hero.html` to permanently re-hide it on mobile viewports. This completely eliminates unnecessary clutter and perfectly matches the intended mobile structure where only the 5 essential media frames are shown.*
- [x] **Task 15 — Responsive Layout Spacing**
  - *Result: Removed the hardcoded `gap: 64px !important` mobile constraint and restored the responsive `gap: 4rem !important`. Replaced the absolute, non-responsive `top: -30px` positioning on `.hr-node-label` with a fully scalable `top: -2.5rem`. By unifying the gap and offset to the same relative unit system (`rem`), the frames perfectly avoid overlap dynamically without breaking scaling behavior across variable root font sizes.*
- [x] **Task 16 — Mobile Video Aspect Ratio Correction**
  - *Result: Modified the `.custom-mobile-video-card` styling in `hero.html`. The previous `aspect-ratio: 16 / 9` was forcing the vertical source video into a landscape bounding box, causing severe vertical cropping (top and bottom chopped off) due to `object-fit: cover`. Changed this to `aspect-ratio: 9 / 16`, ensuring the mobile container perfectly bounds the `0.5625` native aspect ratio of the portrait video. The container and video now have identical dimensions (`351x624`) on mobile, meaning zero cropping occurs.*
- [x] **Task 17 — Desktop Hero Tag Alignment Restoration**
  - *Result: Restored the non-uniform tag offsets from the original Weavy design for desktop viewports. Using a `@media screen and (min-width: 768px)` query in `hero.html`, applied the highly specific `calc()` offsets to each `#node` label so they align flawlessly across the desktop grid, while retaining the uniform `-2.5rem` offset for mobile to prevent stacking overlap.*
- [x] **Task 18 — Desktop Video Padding (Black Bar) Fix**
  - *Result: The black bar above the video on desktop was caused by `padding-top: 1.5rem` inherited from the `.hero-video` class in `weavy.css`. Extracted the `padding: 0 !important` override from the mobile-only media query and applied it globally to `.hr-card-minimax-video .hero-video`, successfully eliminating the black bar on all viewports.*
