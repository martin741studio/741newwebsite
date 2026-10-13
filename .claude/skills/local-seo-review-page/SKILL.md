---
name: local-seo-review-page
description: >
  Build a 741 prospect review page (personal Google-visibility analysis at 741.studio/review/<slug>/)
  with the installed workflow v2.1 (Martin, 2026-10-12): intake.py, parallel agents A-G, ONE Chrome
  operator with a job queue, standing G1 scan go, draft_prospect.py skeleton, factcheck.py, build +
  validate, deploy, Loom script, Loom transcript, WhatsApp message with the email ask. Use for every
  LOCAL prospect (practice, firm, consultant with a Google entry), in every chat and in batches.
  Trigger on "review page for <name>", "audit page", "make the review page", "Review-Page", a
  LinkedIn/contact card or a prospect URL, a Loom URL for a review page ("video for X"), or
  "LI Review-Pages Batch". For ONLINE / no-Google-entry / English prospects use the variant at the end.
---

# 741 Review Page: installed workflow v2.1 (standard since 2026-10-12)

Martin (2026-10-12): "This is the workflow that needs to be the installed workflow." Every review-page request in any chat (also the LI Review-Pages batch) runs these steps. Reference run: Christian Rüther, `00_project/prospects/christian-ruether-v2/` (19 minutes, live at https://741.studio/review/christian-ruether-v2/).

Read first, every time: `00_project/prospect-mini-workflow.md` (sections 1, 1b, 1c, steps 0–13) and `00_project/prospect-mini/agent-briefs.md`. Working folder: `/Users/martindrendel/741website/00_project`. Prospect folder: `prospects/<slug>/`. Images: `../04_site/public/review-assets/<slug>/`.

## Run (orchestrator = this chat)

1. **Intake (30 s):** `python3 prospect-mini/scripts/intake.py "<name>" <website> [maps-link] --business "<name on Google>" --city <city> --linkedin <url>`. A Maps link with a place_id costs 0 credits; without it ONE place search runs (2 Local Falcon credits per hit). If an old page exists (gate G4), build a new slug with `--slug <slug>-v2` and keep the old page online.
2. **Start O, A, B, C, D in ONE message** (agent briefs file). Only agent O uses Claude in Chrome (never the built-in browser); the others queue jobs in `browser-queue.jsonl`. A, B, D, O on the cheaper model. Every agent writes start and end time into `run-state.json`.
3. **G1 standing go:** when D reports a Google entry, 0 usable scans and a keyword that passes the gap rule, tell D to run the scan (49 credits) at once. Ask Martin only when the rule does not pass.
4. **Writer E** right after A, D and O (do not wait for B and C): `python3 prospect-mini/scripts/draft_prospect.py <slug>` builds the skeleton (all numbers, tables, calc on slider steps, sources); E replaces every TODO, adds the map texts when the Falcon report arrives.
5. **Build + check:** `python3 prospect-mini/scripts/build_page.py prospects/<slug>` → `validate.py` (0 errors; it fails on TODO, jargon and a hero longer than 14/28/35 words) → `factcheck.py <slug>` (fix every WRONG and MISMATCH).
6. **F (fresh fact check) and G (visual check) at the same time.** F checks only the list in `evidence/factcheck-auto.md` plus the map image. G: desktop headless 1500 px + 375 px mobile in Chrome. Fix, rebuild, validate.
7. **Show Martin the page** in his Chrome (http://localhost:3000/review/<slug>/) and send a screenshot file. Never end a run without showing the page.
8. **Deploy (G3):** `npm run build`, then `node 00_project/prospect-mini/scripts/upload_only.mjs review/<slug> review-assets/<slug>` (+ any new shared asset), then curl every URL (200 + size). Do not leave a link that Martin may already have sent in a 404 state.
9. **Loom script:** write `prospects/<slug>/loom-script.md` from `prospect-mini/loom-video-leitfaden.md` (about 5 minutes, page order, 3 messages, what to show and say; at the end Martin, 10+ Jahre, 250+ Unternehmen, Gewinnspiel only for Heilberufler/Praxen, 741 Circle).
10. **When Martin sends the Loom URL:** read the transcript (Loom share page → Transcript tab in Claude in Chrome), save `evidence/loom-transcript.md` with a check against the page, list every statement in the video that the page does not support, set `loom_url` (`https://www.loom.com/embed/<id>`), rebuild, validate, deploy, curl.
11. **Message:** ready for WhatsApp, in the prospect's language and form of address, plain text, `https://` link to the page, no booking link, 1–2 real findings from both page and video. It always ends with the email ask: „Ich schicke dir die Analyse auch gern per E-Mail, dann hast du alles an einem Ort. Magst du mir deine E-Mail-Adresse geben? Das wäre super.“ Never frame it as a process (no „Das gehört bei uns zum Ablauf“, „Workflow“, „Prozess“).
12. When Martin approves a page: `python3 workflow-registry/workflow_registry.py approve --client "<Name>" --workflow prospect`.

## Page standard (built into template.html, build_page.py, case-library.json)

- Hero: H1 max 40 px, subline and paragraph 17 px, button in the first screen at 1440×757, Loom video in the hero.
- Map scan today vs. goal, then "Ist der Sprung realistisch?": case cards with the real "Nachher" map on hover, Vorher/Nachher images in the open cases, the block "Wer dahintersteht" (Martin, 10+ Jahre, 250+ Unternehmen).
- Three levers (search topics, Google entry, homepage today vs. draft), calculator, website check, quick wins, 8-week plan.
- "Deine Ausgangslage auf einen Blick", then the workflow video "Was Agenturen verstecken" (YouTube dQ9OE8GSolw), then the final CTA.
- Plain language for non-technical owners, "du", every number from `evidence/`, no healing or result promises, no method sources.

## Batch (several prospects)

Run intake.py for all prospects first, then one operator, one demand agent and one scan agent serve all of them (workflow section 4 and proposal 31). Each prospect gets its own folder, queue file and run-state.

## VARIANT — online / no-GBP / English prospect (e.g. House of Eluma)
`searchForLocalFalconBusinessLocation` returns nothing for them → pivot to an **English organic/website audit**: in the SHEET mark §2 GBP + §4 local-citation rows `n/a`; core = §3 Website/Technik + §5 keywords + §6 ORGANIC competitors. On the PAGE `cp praxis-suriya`, swap `{{> header_de}}`→`{{> header}}` & `footer_de`→`footer`, English "Hi <Name>," style, **drop the Maps-scan** (there is none), reframe the 4 audit tabs to Website·On-Page·Analytics·Authority. Example: `04_site/review/house-of-eluma/`.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: hello in the hero, point at the grid scan result, insight at the biggest lever, think at open data, celebrate at proof. Use the hosted files `/review-assets/martin-guide/` (CSS, JS, poses). Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
