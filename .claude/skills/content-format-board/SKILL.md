---
name: content-format-board
description: Builds a brainstorm-and-reference board of short-video content ideas for ONE 741 client or prospect, grounded in four verified proven formats (single-scene hook, fast-cut story, talk-to-camera, why-we-do-it educational) and in the real public questions that client's customers ask (Reddit, forums, blog roundups, the client's own reviews). Reuses the client's/prospect's existing folder, states the one real finding first, maps formats to the real situation, flags the production-readiness check and the on-camera person as open questions when unknown, verifies the board (no internal method names, slop 5/5), then waits for Martin's go. Ideas only — no scripts, no captions, never posts. Use when Martin says "content format board for <name>", "/content-format-board <name>", "what video content should we pitch <prospect> with", "plan the next content batch for <client>", "what should <client> be filming", "give <name> a video content strategy board", "social content ideas for <name>". Do NOT use for Martin's or 741's own posts (personal-posts), page or blog copy (content-writing), SEO keyword pools (content-pool), before/after result stories or image templates (social-visuals, story-automation-system), or writing the actual video script.
allowed-tools: Read, Write, Edit, Bash(python3:*), AskUserQuestion, mcp__754a7d7d-c3a6-49a5-a07f-acf0021bac2e__firecrawl_search, mcp__754a7d7d-c3a6-49a5-a07f-acf0021bac2e__firecrawl_scrape, WebSearch
---

# Content format board

## Critical
- **The board is a proposal, never a promise and never a post.** No script, caption or video gets published from this skill. Martin's go (step 9) decides what goes into a pitch or a client plan. Never promise views, reach or results in the board (`verify_board.py` blocks promise words).
- **No internal method names in anything the client or prospect sees.** The format taxonomy and the knowledge base carry creator, program and tool names — they stay in `references/`. The board uses only the client-facing labels in `references/label-map.md`. `scripts/verify_board.py` fails a board that leaks one.
- **Never invent a reference or a finding.** A search with no hit is reported as "no hit". A page that cannot be read is reported as unreadable. A number is either from the client's own data, from a live source you read, or absent. The readiness check and the on-camera person are the client's answers or `OPEN QUESTION` — never a default.
- **Client output only.** This skill never produces 741's own content and never calls `personal-posts`. A client's board carries the client's situation and voice, not 741's.
- Replies in STE. The board is written in the client's language (English or German) and must pass the slop lint at 5/5 before Martin sees it.

## Inputs
- A client or prospect name (anything `scripts/resolve_target.py` can match to `00_project/prospects/<slug>/` or `00_project/assets/<client>/`).
- Optional: the purpose — "pitch" (prospect) or "next batch" (running client). Default: prospect folder → pitch, client folder → next batch.
- Optional: language (`en`/`de`). Default: the language of the client's own site/intake.
- Optional, from Martin or the client: answers to the readiness check and the on-camera person. If absent they stay `OPEN QUESTION`.

## Workflow
Copy this checklist into your reply and tick it off:

- [ ] 1. **Resolve the target.** `python3 scripts/resolve_target.py "<name>"`. Exit 2 or `ambiguous` → ask Martin which folder (card), never guess. Note `out_dir`, `kind`, `existing_files`. Log: `python3 scripts/run_log.py <out_dir> intake ok --client "<Name>" "<kind>, <n> files reused"`.
- [ ] 2. **Read what already exists, fully.** Every file in `existing_files` (intake, demand, competitors, prospect.json, voice, roadmap, baseline). Pull out: the business, its real differentiator, its ratings/reviews vs. competitors, measured search demand, the people named on record. Do not re-run research that is already there. When two files disagree (market code, review counts, a claim vs. the raw table), use the file with the raw data table, do not repeat the claim, and list the conflict in your reply. For a running client, run the roadmap pre-flight first (`client-roadmap`) and stay inside the active milestone.
- [ ] 3. **Readiness + on-camera.** Check the files for the three readiness answers (`references/format-taxonomy.md` §Pre-step) and a named owner/staff. Known → use. Unknown → write `OPEN QUESTION: ask the client` in the board; do not stop and do not assume. If Martin is in the chat and can answer now, ask once (one card), then continue either way.
- [ ] 4. **Source the real public questions.** Read `references/playbook-notes.md` §F–G first. Then search live, logging every call (`python3 scripts/log_research_calls.py <out_dir> add <tool> "<query>" <hits>`):
  - `firecrawl_search` (web) for "<service> <city> reddit", "best <category> <city>", "<service> <city> forum/Quora", and the client's name + city. Reddit threads cannot be scraped directly — use the search snippets, never retry a direct Reddit scrape.
  - Blog roundups and review-site lists from those results (`firecrawl_scrape` on non-Reddit pages when the snippet is not enough). A page too large to read: save it, grep the saved file for the client's name and the keyword, and log the hit count; if it still cannot be read, log it as unreadable — never summarize a page you did not read.
  - The client's own reviews/FAQ page/DMs if on file; competitor comment threads only when a competitor post URL (not just a domain) is already on file.
  - `hits` in the log = results that are about the client's category and area, not the raw result count.
  - Rank with §G: top-20 % buyers' problems, sales-call objections, save-worthy answers, niche specificity. Keep 5–10 questions, each with its source. Log: `run_log.py <out_dir> questions ok --client "<Name>" "<n> questions, <m> calls"`.
- [ ] 5. **State the finding.** One paragraph, plain words, before any format: where the business stands (ratings, reviews, demand) vs. where it appears in the public conversation. If the search found nothing about the client, that absence is the finding. This becomes board §1.
- [ ] 6. **Map the formats.** Read `references/format-taxonomy.md` and `references/playbook-notes.md` §A–E, H fresh. Pick 4–8 ideas across the four formats, at least one Why-We-Do-It built on a §4 question, levels chosen by the readiness reading (unknown → phone versions first). Every idea gets the 8 fields of the template, with the hook/length/ending rules from §A–D and the quality bar from §E. Labels come from `python3 scripts/label_map.py show --lang <en|de>` — never typed from memory.
- [ ] 7. **Draft the board.** Copy `assets/board-template.md` (German boards: translate the headings exactly as `verify_board.py` expects, see its `SECTIONS`), fill every section, save as `<out_dir>/board.md`. Write in STE: active voice, one idea per sentence, 20 words or fewer, no em-dashes (the slop lint and the verifier flag them), idea headings as `### Idea N: <label>`. Add §6 (cadence, test loop, avoid-list from `playbook-notes.md` §I) and §7 (what the client decides now). Log: `run_log.py <out_dir> draft ok --client "<Name>" --result <out_dir>/board.md`.
- [ ] 8. **Verify, fix, repeat.** `python3 scripts/verify_board.py <out_dir>/board.md --lang <en|de>`. Fix every `FAIL` (sections, fields, banned terms, promise words, placeholders, slop). Below 5/5 on slop: rewrite, or `.claude/skills/slopmonster/tools/cleanse.sh` (English) / `00_project/content-writing-skill/scripts/cleanse_de.sh` (German), then verify again. Only `BOARD PASSED` continues. Then `python3 scripts/log_research_calls.py <out_dir> report` and put the call count in your reply. Log: `run_log.py <out_dir> verified ok --client "<Name>"`.
- [ ] 9. **Checkpoint — Martin's go.** Show the full board (file link; for mobile review publish it as an Artifact page and keep that URL stable on later runs). Ask with one card: go / change / drop. Record the answer: `run_log.py <out_dir> martin_go <ok|rejected> --client "<Name>" "<his words>"`. A go on one board is not a go on the next run.
- [ ] 10. **Deliver.** On go: the board stays at `<out_dir>/board.md`; state which 2 ideas Martin wants first and what the client still has to answer (§2, §3). For a prospect, say in one line how it feeds the pitch (sales-pitch / booking-sequence read it by hand — this skill never calls them). Log: `run_log.py <out_dir> delivered ok --client "<Name>" --result <out_dir>/board.md "<2 ideas first>"`.

## Output template
`assets/board-template.md` — ALWAYS use this exact structure (7 sections, 8 fields per idea). The verify script enforces it.

## Checkpoints
- After step 1: a matched folder, or Martin's answer on which one — never a guessed slug.
- After step 8: `BOARD PASSED` from `verify_board.py` before Martin sees anything.
- After step 9: Martin's explicit go per board, per run.

## References
- `references/format-taxonomy.md` — the four formats with levels and what each needs; the readiness pre-step; mapping notes. Read at step 6 every run.
- `references/playbook-notes.md` — video findings from Martin's content-marketing knowledge base: hook windows per platform, retention pacing, loop ending, 20–25 s length, quality = substance, question sourcing and ranking, on-camera rules, cadence/penalties/test loop. Read §F–G at step 4 and §A–E, H at step 6 every run.
- `references/label-map.md` — internal term → client-facing label (EN/DE) and the banned-term list. Data twin: `assets/label-map.json`.
- `references/worked-example.md` — the Little Frenchie hand-run: what a good board does and the friction it exposed.
- `00_project/knowledge/content-format-library/` — the source transcript (internal, never cited to a client).
- External: `.claude/skills/slopmonster/tools/deslop.py` + `cleanse.sh` (English lint/cleanse), `00_project/content-writing-skill/scripts/deslop_de.py` + `cleanse_de.sh` (German). Memories: `no-method-sources-in-deliverables`, `claims-need-real-data`, `never-invent-contact-history`, `client-roadmap-workflow`.
