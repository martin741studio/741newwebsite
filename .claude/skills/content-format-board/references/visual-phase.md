# Phase 2 — the visual board, in detail

Built from the first real run (Little Frenchie, 2026-10-24, `00_project/assets/little-frenchie-bali/content-format-board/2026-10-24/visual/`). Three corrections from Martin during that run are now rules; they are repeated at the end so the reason stays with the rule.

## Contents
1. Brand inventory (`visual/brand.md`)
2. Reference research (`visual/refs.md`)
3. The candid shared block (verbatim)
4. Concept prompts (`visual/prompts.md`)
5. ChatGPT operating rules (Martin's Chrome)
6. The board page (`visual.json` → `build_visual_page.py`)
7. Guide character
8. The three corrections and why

## 1. Brand inventory
Sources, in this order: the client's site (firecrawl_scrape with `branding` + `images` → logo URL, colours, fonts, photo URLs; `curl` the originals into `visual/brand/`), the review-page draft (`prospects/<slug>/draft/logo.png`, `food.jpg`, `sign.jpg` if present), Instagram in Martin's Chrome (profile header + grid screenshots, `brand/ig-profile-header.jpg`, `brand/ig-grid.jpg`). Make 1400 px web copies of the big photos with `sips -Z 1400` into `visual/brand-web/` (ChatGPT uploads must stay under 10 MB per call).
`brand.md` sections: Logo (files, rule: reproduce exactly, never redraw — memory `real-logos-only`) · Colours (hex table by role) · Fonts · Photos on file (table: file, size, what it shows — every one opened) · Instagram look (bio, highlights, grid pattern in words) · Image style and mood (3–5 words, plus "not:") · Open questions.

## 2. Reference research
Goal: 3–5 live references per idea that show what the RESULT should look like in the client's category, before any prompt. Method that worked: Instagram keyword search in Martin's Chrome (`instagram.com/explore/search/keyword/?q=<dish or format> reel`), open the tiles that look like a venue (not a creator kitchen), screenshot the open post (cover frame + caption + likes), press Escape, next. Save as `refs/<ideaN>-r<k>-<account>-<likes>.jpg`. Note per reference: type (venue/creator/local competitor), the likes shown, what to take from it (camera, motion, text placement, light). Also keep 1–2 format-level references from `outcome-references.md`. Then write the **rules block per idea** — these rules, not the brand file, drive the prompts.
Also capture the client's own best-performing post if it appears in the search (Little Frenchie's "steak frites, encore." ranked first for "bistro steak frites"): their own language is the strongest reference.

## 3. The candid shared block (paste at the top of every concept prompt)
The attached Instagram grid is this restaurant's real feed: use its visual language exactly: [plate style, backgrounds, text style, logo — from brand.md]. The attached photo frame shows the subject and composition to keep, but re-render it as a candid phone-video still shot by a guest on an iPhone: ordinary daylight that is slightly uneven, a little harsh in places, real table clutter (a used napkin, a phone, a water glass, crumbs), slight motion blur on the moving hand, natural skin, no cinematic glow, no soft dreamy light, no perfect styling, no editorial polish, nothing that looks like an advert or an AI render. The attached logo is the real logo; reproduce it exactly where it appears. Output: one vertical Reel cover concept, 1024×1536, hand-lettered text rendered cleanly and legibly, no other UI, no watermark.
Never write "hyperrealistic photograph", "editorial", "full-frame camera", "cinematic" — that produced the "princess in a fable book" look Martin rejected.

## 4. Concept prompts
Per idea 2–3 concepts. Each prompt = shared block + one scene with the mechanism IN the image: a hand-lettered line in the client's script, a big word centred, labels with arrows, a second action in the background. Attach: the base frame or a real photo (subject + composition), `brand/ig-grid.jpg` (style), the logo. A table above the prompts: concept · mechanism (why it draws attention) · reference proof. Save each prompt as `prompts-v3/<id>.txt` = shared block + scene, one paragraph, no blank lines.
Plain base frames (food only, no text) may be generated first as inputs, but they are never shown as the result.

## 5. ChatGPT operating rules (Martin's Chrome, tested 2026-10-24)
- Fresh chat per image: navigate the tab to `https://chatgpt.com/` (not the sidebar button). Check the top toggle shows **Chat**, not Work.
- `find` "hidden file input 'Attach photos'" → `file_upload` with absolute paths (≤10 MB per call). Wait 5 s. `find` the composer textbox.
- **Clear the stale draft:** click the composer, cmd+a, Delete — ChatGPT carries the previous chat's draft into a new chat.
- `LC_ALL=en_US.UTF-8 pbcopy < prompt.txt`, click composer, cmd+v, then JS: `document.querySelector('[contenteditable="true"]').innerText.length` must equal the file length minus 1.
- Effort: the dropdown at the right of the composer → slider to **High** (persists across tabs).
- `find` "send message button" → click. Generation takes 60–120 s. Up to 3 tabs in parallel.
- Download: click the image → lightbox → download icon (top right) → `~/Downloads/<ChatGPT title>.png` → `mv` by newest file into `visual/images/...`. Open every image.
- Edit follow-ups in the same thread stall; a redo is a fresh chat.

## 6. The board page
`visual.json`: client, place, date, lang, guide, bubbles (hello, idea1, idea2 — the guide's own voice, 2 short sentences), brand (logo, colors, mood, grid, grid_note), ideas[] (n, label, idea, concepts[] {file, title, mechanism, ref, proof}, base[], too_polished), open[] (empty by default — Martin: no "what we need from you" summary block on the page).
`build_visual_page.py <visual_dir>` writes `board.html` (full document, relative links, guide assets in `mg/`) and `board-artifact.html` (no skeleton, guide CSS/JS/poses inlined, side-gutter padding per the artifact contract). Web copies go to `images/web/<folder>-<name>.jpg`.
Checks: headless Chrome shot at 1440 (`--window-size=1440,900` and a tall one); for mobile, headless clamps the window, so open `board.html` through a local `python3 -m http.server` in Martin's Chrome and inject `<iframe src="board.html" style="width:390px;height:800px">`, then compare `contentDocument.documentElement.scrollWidth` with the iframe `innerWidth`. Grid tracks must be `minmax(0,1fr)` and `img{max-width:100%}` or an image's intrinsic width pushes the page wide.
Slop lint on the extracted page text (`deslop.py --text`), banned terms (`label_map.py scan board.html`), both must pass. Publish with `root=<visual_dir>` and the `images/web/*` + logo paths in `files`; redeploy to the same path keeps the URL.

## 7. Guide character
`guide: "celine"` for clients where TALKNFIVE (Céline) is the creative lead — Bali hospitality and creative clients, anything she presents; `guide: "martin"` for 741-only clients. Céline's set: `04_site/public/review-assets/celine-guide/celine-<pose>.webp` (hello, present, point, think, strategy, celebrate, front, three-quarter, side; wine-red trousers set, memory `celine-guide-character`). Rules as in the Martin guide README: max one callout per section, bubble text in the guide's first person, no tool names, no promises. Martin, 2026-10-24: for Little Frenchie and the prospect review pages everything is presented from Céline's character, in TALKNFIVE identity, not Martin's.

## 8. The three corrections and why (Martin, 2026-10-24)
1. "We had to actually research reference material for how it should look beforehand, before we create anything in GPT." → step 12 is a gate before step 13. The first run skipped it (used only the format-level links) and produced plain plates.
2. "I don't want to see only food images. I want to see concepts and why they're actually drawing attention." → concept frames carry the mechanism; the page shows mechanism + reference proof per frame; plain plates are inputs only.
3. "Not so high-key. They're looking like AI, out of a fable book where the princess is eating." → the candid shared block; never editorial/cinematic wording.
Also from the run: no "what we need from you" summary block on the client page; the creative director (Céline) reviews before the client sees it; her verdict on the first run: the scope shown is already enough — do not add more layers.
