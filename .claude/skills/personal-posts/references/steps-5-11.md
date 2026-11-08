# Steps 5-11 in detail

Back to the body: `../SKILL.md`. Paths are relative to the skill folder.

## Step 5: first-principles note, then angle generation
Default on every post; skip only if Martin explicitly says "skip angles". Card by card, never one prose block (`voice-profile.md` §"First-principles note", correction 2026-10-22: "it can't be too much comfort... decision card by decision card"). Three separate stops:
- 5a. Card: the root mechanism, offered as real candidate framings to choose or correct, not asserted as a finished paragraph. Wait for Martin's answer.
- 5b. Card: the cross-domain translation, especially to business, built on the 5a answer. Candidates, not a finished paragraph. Wait for his answer.
- 5c. Card: angle hooks. Read `strategy-notes.md` fresh ("Directly actionable" and "Useful mental models") and propose 3-4 distinct angles built on the confirmed mechanism from 5a/5b. Each angle is ONE hook line plus: the technique it leans on (negative/contrarian framing, numerical specificity, "How I not How To" narrative, a damaging admission, an SPCL pillar Status/Power/Credibility/Likeness, a BVT-calibrated edge, a save-worthy framework/checklist shape) and one line on why it reaches further, citing the strategy-notes figure where one exists. For a personal pillar-1 post the editorial method is itself a good source of angles. Martin picks one, asks for a blend, or rejects all and gives a new thought.
  Log: `python3 scripts/run_log.py write angle_picked ok --account <personal|business> "<picked technique>"`.

## Step 6: core draft
Read the matching voice file in full every time (`voice-profile.md` for `/personal-post`, `voice-profile-business.md` for `/741-post`), not from memory of a previous run. Draft ONE core argument in that voice, built on the chosen angle: claim first, then the one reason to believe it.

## Step 7: platform adaptation
Use the voice file's §"Per-platform adaptation" and `platform-specs.md`. Write only the platform versions needed (default: all 4). Save each as `draft-<platform>.txt` (`draft-x.txt`, `draft-linkedin.txt`, `draft-instagram.txt`, `draft-facebook.txt`) so the verification script can infer the platform. Self-check each draft against copy-rules C4.1 (2 sentences per paragraph at most); `verify_draft.py` does not check this.

## Step 8: verify, every version separately
`python3 scripts/verify_draft.py draft-*.txt`. Any file below 5/5 or over its hard length limit: shorten/rewrite, or for the slop gate run `.claude/skills/slopmonster/tools/cleanse.sh draft-<platform>.txt`, then re-run `verify_draft.py` until every file exits 0. `cleanse.sh` is the one external send (rival-model pass) and only runs when a draft scores below 5/5.

## Step 9: Martin's go
Show every verified platform version together, labeled with the account, in one `AskUserQuestion` card (not a prose list). He may approve some, reject others, or ask for a rewrite. Log: `python3 scripts/run_log.py write martin_go <ok|rejected> --account <personal|business> "<one-line note>"`.

## Step 10: image (Instagram + Facebook only)
- Business account: `python3 scripts/build_business_image.py "<pull-quote line>" <instagram|facebook>` (full 741 branding), one style only.
- Personal account has two styles (`voice-profile.md` §"Image"). Ask which fits (card) when not obvious; default is the quote card: `python3 scripts/build_personal_image.py "<pull-quote line>" "Martin Drendel" <instagram|facebook>` (no branding). For a clean "assume X / actually Y" post: `python3 scripts/build_personal_mechanism.py "<assumption>" "<reality>" "Martin Drendel" <instagram|facebook>`, built from the confirmed 5a/5b answers.
- Never cross a personal style with the business template. Skip for LinkedIn/X-only runs or when Martin did not approve the Instagram/Facebook version. Read the rendered PNG back (`Read`) to check for collisions or overflow before delivering.
- Other builders in `scripts/`: `build_carousel_photo.py`, `build_video_cover.py` (carousel pipeline, see `outlier-carousel-pipeline.md`).

## Step 11: deliver
Hand Martin the approved text (and image), ready to paste, labeled with the account.
**Business account: also upload to Drive** (Martin, 2026-10-29). Folder `Socials Martin > Fertige Posts` (exact Drive IDs and the browser upload method are in `outlier-carousel-pipeline.md`), one subfolder per post named `<date> <post-name>`, containing every slide/video and `caption.txt`. Files over ~10 MB combined go in a separate upload call (split images+caption from any video). Also replace the top-level `fertige-posts-texte.txt` in that Drive folder with the current local version.
Log: `python3 scripts/run_log.py write delivered ok --account <personal|business> "<platforms delivered>"`. Never post or schedule it.
