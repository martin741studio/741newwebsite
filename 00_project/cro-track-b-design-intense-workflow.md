# CRO Track B: Design-Intense Showpiece Workflow

Status: **written 2026-10-11, not run yet. Pilot later, on Martin's word.** Source of ideas: the video notes in `knowledge/design-video-notes/fq3wx-AR6B0-transcript.md`, plus our own runs. Track A (`cro-homepage-workflow.md`) is not changed by this document.

## 0. When to use Track B

| Use Track B | Use Track A |
| --- | --- |
| Martin says "let's do track B" | Default for every run |
| Pitch to a lead who buys design (agency, studio, SaaS, brand, premium service) | Local practices, law firms, trades |
| Client has budget and time for a showpiece | Fast sales artifact |
| Page is a brand statement as much as a conversion page | Page is a pure conversion page |
| | **Health clients (HWG): Track A only**, unless Martin decides otherwise in writing |

Track B is Track A plus a design layer. It does not replace the CRO rules. It adds more work before the mockup and more checks after the build.

## 1. Hard gates (the same as Track A, never relaxed)

1. CTA visible in the first screen at 701 px viewport height.
2. One CTA colour only.
3. Every word comes from `approved-copy.md`. Motion and media carry no new claims.
4. Industry rules stay (HWG, Anwaltswerbe-Check, claims need real data).
5. Visual check in Claude in Chrome before any "done" (`cro-homepage-visual-check.md`) plus the Track B checks in section 5.
6. Prototypes stay local. Never uploaded unasked.
7. Reduced-motion version exists. Nothing autoplays with sound.
8. Every exception to `cro-homepage-motion-spec.md` is written in `07-prototype/motion.md` with the reason.

## 2. The steps

Folder: the same tree as Track A (`00_project/assets/<slug>/cro/`), with extra subfolders: `00-brief-b/`, `02-data/references/`, `05-gpt-design-doc/concept/`, `06-gpt-assets/media/`.

| Step | Name | Output | Gate |
| --- | --- | --- | --- |
| B0 | **Grill-me brief** | `00-brief-b/brief-b.md` from `cro-track-b-questionnaire.md` | All blocks answered. Vague answers rejected. |
| B1 | Data (= A Step 0 to 2) | dataset, brand, diagnosis, scorecard (as Track A) | As Track A. |
| B2 | **Reference board** | `02-data/references/board.md` + screenshots | At least 5 references, each with "like" and "dislike", plus 2 anti-references. |
| B2b | **Element pool** | `00-element-pool/index.html` + `votes.json` | Martin voted on every element. |
| B3 | Copy (= A Step 3) | `04-copy/approved-copy.md` | Checkpoint 1 as Track A (Martin may waive it for the run). |
| B4 | **Concept and storyboard** | `05-gpt-design-doc/concept/concept.md` | One signature idea. One moving element per section with its job. Component list. |
| B5 | Design doc + media plan | `05-gpt-design-doc/design-doc.md`, `06-gpt-assets/media/MEDIA-PLAN.md` | Every media slot has a type (still, loop video, code graphic) and a source. |
| B6 | Mockup + media generation | full-page mockup, hero keyframes, stills, loops | Mockup as Track A. Media at full resolution. Loop test: last frame equals first frame. |
| B7 | **Build with motion layer** | `07-prototype/index.html`, `motion.md`, X-ray switch | Build rules in section 4. |
| B8 | **QA** | `visual-check.md` (Track A list + section 5), `self-check.md`, `perf.md` | Visual check line. CRO scorecard pass. Performance budget met. |
| B9 | Handoff | `08-handoff/handoff.md` + component list + media shoot list | As Track A, plus section 6. |

### B0. Grill-me brief
The agent runs the questionnaire in three rounds (see the questionnaire file). It does not accept "modern", "clean" or "premium" without an example. Answers go in `brief-b.md`. No later step starts until B0 passes.

### B2b. Element pool (Martin, 2026-10-12: he must SEE and vote, a written catalog is not enough)
After the reference research the agent builds a **live element pool**: one local HTML page in `<run>/00-element-pool/` where every shortlisted element runs as a working demo in the client's colours and fonts (hover, scroll and draw-once animations, with a replay button). Martin votes Ja, Vielleicht or Nein per element, with an optional note. Rules: 20 to 35 elements, grouped by page section. Each card names the source reference, the effort and the industry risk. A reduced-motion test switch is part of the page. Votes are saved in the browser and, through a small local server (`serve_pool.py`, POST /save writes `votes.json`), in the run folder. Export buttons copy or download the result. Use real client assets only (logo, portraits). Template: `00_project/assets/dumann/cro-b/00-element-pool/`. The agent reads `votes.json` and builds the concept and storyboard (B4) only from the Ja and Vielleicht elements. No concept is written before the pool is voted.

### B2. Reference board
Sources: Refero (refero.design), Mobbin, Awwwards, Dribbble, X search "design websites", the client's own favourites. For each reference: URL, screenshot at 1440 px (Chrome), then three lines: what to take (layout, type, motion, colour, imagery, interaction), what to leave, which section it is for. The agent reads the structure with `javascript_tool` (sizes, radius) and Firecrawl `branding`, as in Track A step 1.12. Structure only. No copying of text, images, brand marks or code of a reference.

### B4. Concept and storyboard
- **Signature idea:** one memorable moment (a hero loop, a scroll story, a character, a morph). Written in one sentence with the reason it fits the brand.
- **Section storyboard:** per section: the one thing that moves, the job it does for the visitor, the trigger (load, scroll, hover, click), the reduced-motion version.
- **Component menu** (pick at most 4 for the page, all optional): morph menu, curtain footer, image trail, spin gallery, day/night switch, bento glide, command bar, jelly buttons, hop navigation, cursor follower, scroll-linked text reveal, holographic sticker, interactive 404, a mini game gate (only if the brand is playful). Each pick needs a conversion reason or a brand reason.
- **Rules from the video, kept:** every moving part has a job; one render function per section; a loop ends on its first frame; characters react to cursor or scroll; an X-ray switch shows code layers against media layers.

### B5/B6. Media
- Stills: ChatGPT images as in Track A step 5b, one fresh chat per image.
- Loop video and motion media: **only when a video tool is connected** (Higgsfield through its Claude connector is the candidate named in the video; not connected today, needs Martin's account and budget). Without it: code-drawn loops (SVG, canvas, CSS) and GPT stills.
- Every generated person or room goes on the shoot list as in Track A.
- Media plan lists per slot: type, size, duration (loops 4 to 8 s), file weight, source tool, prompt, fallback still.

### B7. Build rules
- Same stack as Track A: one HTML file plus `assets/`, desktop 1440 px.
- Code motion layer: SVG, canvas or CSS only. No animation library unless the brief allows it (then write it in `motion.md`).
- **X-ray switch:** a hidden toggle (`?xray=1` or key `x`) that outlines code-drawn layers in one colour and media layers in another. Used in QA and in the pitch call.
- Video: `muted`, `playsinline`, `loop`, poster image, no sound, paused when off screen, hidden under reduced motion (poster shows instead).
- Interactive components never block the CTA or the content. The site works with them off.
- A fixed header or sticky CTA stays unless the concept forbids it and Martin agrees.
- Page weight: first screen under 2.5 MB, whole page under 12 MB, video loops under 2 MB each (targets, adjust in the brief).

## 3. What changes against Track A

| Area | Track A | Track B |
| --- | --- | --- |
| Start | Trigger inputs | Grill-me brief |
| Design input | Brand files and one optional reference site | Reference board with likes and dislikes |
| Media | Photos and GPT stills | Stills plus loops and code graphics |
| Motion | Calm spec, one highlight per section | Spec plus a signature idea, exceptions in `motion.md` |
| Interaction | Accordion, hover | Up to 4 chosen components |
| QA | Visual check | Visual check plus motion, performance, reduced-motion checks |
| Time | Hours | A multiple of Track A. Plan for it. |

## 4. Motion exceptions (default permissions for Track B)

Allowed when the brief and the concept say so, always with a reduced-motion fallback: a looping background video, a scroll-linked effect, a cursor-follower, a hover-triggered rotation, a one-time intro animation under 2.5 s, a character that follows the scroll. Still forbidden: autoplay sound, parallax that moves text out from under the reader, bounce or elastic easing on text, an effect that hides the CTA, anything that delays the first paint of H1 and CTA.

## 5. Track B checks (added to the visual check)

| # | Check | Pass rule |
| --- | --- | --- |
| T1 | Frame rate while scrolling the whole page | no visible stutter; no long task over 100 ms in the Performance trace |
| T2 | Loops | last frame equals first frame, no jump |
| T3 | Video off-screen | paused when not visible |
| T4 | Reduced motion (`prefers-reduced-motion`) | page readable and complete, no movement, poster images shown |
| T5 | All components off | page still works, CTA reachable |
| T6 | Weight | within the budget in `perf.md` |
| T7 | X-ray switch | works, layers labelled |
| T8 | CTA | still visible at 701 px height in the first screen with the intro running |
| T9 | Keyboard | menu, accordion and components reachable with Tab, focus visible |
| T10 | Contrast over video | text over moving media keeps contrast of at least 4.5 to 1 at every frame sampled |

## 6. Handoff additions

Component list with the file and function of each, media list with source tool and prompt, shoot list, `perf.md`, the X-ray switch note, the list of motion exceptions, and a note on what a CMS can and cannot do with it (Jimdo and Wix often cannot).

## 7. Open points before the first Track B run

1. Video tool: connect Higgsfield (or another) and set a budget, or run Track B without generated video.
2. Pick the pilot client or lead.
3. Mobile: Track B is desktop-first like Track A. A mobile version belongs to the later rebuild workflow.
4. Decide if Track B gets its own skill (`cro-track-b`) after the pilot.

## Registry entry (2026-10-11)

Every run of this workflow is recorded in the workflow registry. The Excel `~/Desktop/Workflow-Uebersicht.xlsx` shows per client whether the workflow ran, its state, the last run, Martin's approval and the folder links.
- At the start or end of a run: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py upsert --client "<client>" --workflow cro_b --status "in Arbeit|Trockenlauf|fertig, Freigabe offen" --local <folder> --drive <url> --result <file>`
- When Martin approves the result: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client "<client>" --workflow cro_b` in the same turn, then tell Martin the sheet was updated. A hook reminds Claude when a message sounds like an approval.
Workflow id: `cro_b` (CRO Track B).

## Registry: automatic (2026-10-11)

The overview Excel `~/Desktop/Workflow-Uebersicht.xlsx` updates itself. A Stop hook runs `workflow_registry.py sync --quiet` after every turn. You do not call `upsert` for normal progress. Write one dated line per step into `00_project/assets/<client>/cro-b/_status.md`. A line with the word Handoff makes the run fertig, Freigabe offen.
For any other file layout, write `_run.json` in the run folder (schema in `00_project/workflow-registry/README.md`). Only the approval stays manual: when Martin approves a result, run `approve` in the same turn and say that the Excel is updated.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: only in the presentation wrapper. Never inside the prototype. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
