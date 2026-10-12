# GPT Design Doc — me&you, Landingpage „The Overlooked“
Stand 2026-10-12. Text source: `04-copy/approved-copy.md` (approved at Checkpoint 1). Same method as the other subpages: one image, the homepage mockup as style reference. Prompt `prompt.txt` (18,590 characters), generator `build_prompt.py`, units `units.json` (from `make_units.py`). Check: `check_prompt.py` against `04-copy/approved-copy-plain.txt`, 178 quotes, 0 missing (the only difference to `approved-copy.md` is the link markup).

## Persona look (design guide section 02)
- Cool variant of the brand. Navy #2B3C52 for the hero, the method band and the closing. Cool off-white #F6F6F4 and light grey #E7E8E8 for the other bands. Dove blue #7E99B6 for numbers, overlines and hairlines.
- Visible thin grid, numbered steps, diagram before decoration, tables with thin rules, captions with real information.
- One button colour: deep dove blue #4F6D90 (white text) on light bands, cream #F2EDE4 (navy text) on navy bands. Same label everywhere: „Gespräch buchen“.
- Photography: architectural, cool daylight, glass and steel, person in context with distance. Black and white allowed.

## Sections
1 Hero (navy, photo right with caption) · 2 Proof strip (portrait, four numbers, quote) · 3 Direct answer (three practice parts, podcast pull quote) · 4 Situations (three numbered cards) · 5 Method diagram (navy) · 6 Comparison table · 7 Training topics table · 8 Format table · 9 First step (three steps) · 10 Michael (real photo, evidence table) · 11 Voices (2 × 2 open cards, three videos) · 12 FAQ (accordion, two columns) · 13 Closing (navy, grid pattern) + footer.

## Image slots
| Slot | Source |
|---|---|
| S01 hero | Step 5b: new GPT image of Michael at a glass table in a glass-walled office (face reference: real photo `michael-jacket-1122.jpg`, mood: `pdf-overlooked-main.webp`) |
| S02 portrait | real photo `michael-jacket` (crop) |
| S10 Michael | real photo `michael-chair` or `michael-jacket` |
| S11 videos | real Wistia posters `v-stimme-1..3.webp` |
| S13 closing | no photo, navy with grid pattern |

Refs for ChatGPT: `refs/ref-homepage-mockup.jpg`, `refs/ref-logo.png`, `refs/ref-michael-jacket.jpg`, `refs/ref-persona-overlooked.jpg`.
