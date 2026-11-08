# Producer formats — carousel, story, reel (business account, German Instagram)

Source: Martin's NotebookLM notebook "The Content Marketing Playbook" (73 sources, `notebook.google.com/notebook/7f6a765f-7a30-446e-9259-e1a497c318eb`), queried 2026-10-29 in Martin's Chrome. Numbers are the notebook's synthesis of industry sources, not 741's own measured data. Use them to shape technique, never quote them in a post as a fact about 741 (`claims-need-real-data`). Lines marked **741 default** are our own choice, not from the sources.

Decisions behind this file: `00_project/workflow-builds/personal-posts-producer/decisions.md` (Martin, 2026-10-29).

## Carousel

- Cover = the hook. High-contrast title over the image, clear hierarchy, one specific, contrarian or curiosity hook. (notebook: carousel engagement ~6.6 % vs ~2 % text-only, dwell time from swiping)
- Slide count: 6-8 is the sweet spot (range 5-12). (notebook)
- One point per slide. Short lines. Calm, clean background behind the text. The sources give no word count. **741 default:** max ~30 words on a body slide, max ~12 on the cover.
- Middle slides = one step each, in an escalating order (a named framework or numbered process). (notebook)
- Saves are the #1 signal (cited 5× a like, 2× a comment). Saves come from bookmarkable assets: named frameworks, step-by-step processes, checklists, benchmark tables. (notebook)
- Shares come from a contrarian view backed by own data or an own case study. (notebook) → use Martin's real 741 case, never a borrowed claim.
- Last slide: a short recap or ONE logical next action (resource in the comments, or a context-rich question). (notebook)
- Keyword CTA ("Kommentiere PLAYBOOK"): helps lead capture on Instagram when an auto-DM tool sends the resource. A one-word comment does not count as a "substantive" comment (10+ words), so it adds little reach weight. On LinkedIn, engagement bait like "comment YES" gets flagged as low quality. (notebook) **741 default:** no auto-DM yet (decision 2026-10-29: Martin answers by hand). Use the keyword CTA on Instagram only, and pair it with a real question in the caption so people also write full comments. Never on LinkedIn.
- **The keyword CTA is also a required final slide, not just a caption line (Martin, 2026-10-29).** Every carousel's LAST slide (`type: "end"`) is the CTA itself: "Kommentiere <WORT>." as the title, one line on what they get as the text. Move any closing punchline into the second-to-last slide (`type: "statement"`) instead of cutting it. The CTA needs a real destination — a link Martin can paste when he replies by hand: an existing 741.studio page, or (default when none exists) a new blog post under `04_site/de/pages/blog/` written for this topic, SEO/GEO-structured (real H2s, an FAQ section, Article+FAQPage JSON-LD), slop-checked to 5/5, verified in the dev server before it's referenced anywhere. Never promise a resource that doesn't exist yet. This is the standing reach/contact mechanism Martin asked for ("verhilft, mehr Reichweite zu generieren und mit den Leuten in Kontakt zu bleiben") — apply it to every future post, not just a one-off fix.
- Look (Martin, 2026-10-29): matthgray style. Cover = photo of Martin (real or ChatGPT image from his reference photos), calm image backgrounds, clean sans type, 741 yellow `#fac118` as accent only. Format 3:4, 1080×1440.
- **Video cover (Martin, 2026-10-29):** when Martin's own real video clip is the cover instead of a photo, crop it to the carousel's own ratio (`ffmpeg -vf "crop=<w>:<h>:<x>:<y>"`), trim to the span where he stays fully in frame, then burn the SAME headline/hook + logo/counter/footer chrome onto it: render those as a transparent PNG (headless Chrome, `--default-background-color=00000000`, same CSS as `cover-mid`) and composite with `ffmpeg -filter_complex "[0:v][1:v]overlay=0:0:format=auto"` (this machine's ffmpeg build has no `drawtext`/libfreetype, so text must come from a rendered PNG, never ffmpeg drawtext). The headline still needs a real hook (one specific, contrarian or curiosity line, ≤12 words main claim) — a raw video with no headline is not a finished cover, "Cover = the hook" applies here too.

## Story

- The sources give no frame count. **741 default:** 3-5 frames per post.
- Stories are relationship and conversion touchpoints. Interactive stickers (poll, question box, quiz) pull active participation. (notebook)
- Share every new feed post or reel to the story right away. Core followers see it first and give it early engagement velocity. (notebook)
- **741 default frame order:** 1 hook frame (the post's tension in one line) → 1-2 frames with one point each → 1 sticker frame (poll or question box tied to the topic) → 1 frame "Neuer Post" pointing to the post or reel.

## Reel (talking head)

- Length: 20-25 s is the completion sweet spot (~42 %+), easiest to loop. B2B ceiling: under 60-90 s, captions mandatory. (notebook; same as `content-format-board/references/playbook-notes.md` §D) Martin's own target was 2-3 min (2026-10-27). His approved Ep. 1-2 run ~70-80 s, inside the B2B ceiling. Do not pad a script to reach 2-3 min.
- Hook: visual pattern interrupt within 1.0 s, value promise by 3.0 s. Say the core industry terms in the first 3-5 s (search indexing). (notebook)
- Hook shapes: specific outcome ("von X auf Y in Z Tagen"), unpopular opinion ("Hör auf mit X"), POV realism. Negative framing cited 1.3-1.8× hook rate; exact numbers cited 2.4× hold. (notebook) Numbers only from real 741 data.
- Zero-delay entry: no greeting, no intro. Start in the problem. (notebook)
- On-screen text: under 8 words per overlay, high contrast, centered. (notebook)
- Captions always, with the real professional terms in them. (notebook)
- Ending: cut the moment the payoff lands, or loop the last line back into the first. No "danke fürs Zuschauen, folg für mehr". (notebook)
- Series framing: "Episode 1 of a series" was cited at 57,000 vs 17,000 followers for the same concept as a standalone video. (notebook) Martin chose "themed but unbranded" for the mini-series (2026-10-27). Mention this tension in one line when relevant; do not re-argue it.
- Performer element: the `[WHITEBOARD: <falsche Annahme> durchstreichen, <echter Mechanismus> daneben schreiben]` cue at the reveal (`voice-profile-business.md` §"On-camera persona").
