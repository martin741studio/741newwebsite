# GPT design doc — me&you, landing page "The Replayers" (2026-10-12)

Text source: `../04-copy/approved-copy.md` (approved: Martin „confirmed continue“ via main session). Method as on the sibling pages: one full-page image, the homepage mockup as style reference. Prompt `prompt.txt` (18.595 characters), generator `build_prompt.py`, text units `units.json` (parsed from the approved copy by `build_units.py`, nothing typed by hand).

Prompt check (`check_prompt.py`): 109 quotes, 103 found word for word. The 6 others differ only because the markdown link syntax `[text](url)` is removed (same result as on the rhetorik run). No invented text.

## Global style block
In the prompt: brand colours as hex, Libre Baskerville and Inter, pill button #4F6D90 as the only strong colour, persona rules (generous space, one idea per screen, soft edges, no grid lines, body lighter than headlines, never more than one button visible), warm interior evening photography, Michael likeness rule, real logo, header capsule without a button.

## Sections
1 Hero on dove tint, new persona photo (woman on her way home, tram window, notebook) · 2 Proof strip cream with Michael cafe photo · 3 Treppenwitz answer with the evening desk photo (homepage image `sit-replayers.webp`) · 4 Three moments, soft cards, button · 5 Why the words come late, narrow column · 6 Method navy band, light button · 7 Exercises, numbered cards · 8 Free video feature box with the real Wistia still, secondary button · 9 Book and podcast cards, text links only · 10 Michael with real portrait, button · 11 Four open quote cards · 12 Next steps soft list, button · 13 FAQ accordion · 14 Navy closer, footer.

## Images
Real: `ref-michael-cafe.jpg` (S02), Michael portrait from `../../01-input/` (S10), Wistia still `ref-video-still.jpg` (S08). Reused 741 image: `sit-replayers.webp` (S03, already on the homepage shoot list). New GPT image (Step 5b): hero persona photo. Book and podcast covers: placeholders until the client sends the cover (RP5).

## Refs to attach
`refs/ref-homepage-mockup.jpg`, `refs/ref-logo.png`, `refs/ref-michael-cafe.jpg`, `refs/ref-video-still.jpg`, `refs/ref-persona-replayers.jpg`.
