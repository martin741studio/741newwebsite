---
name: collab-content
description: Writes reciprocal co-marketing articles with contextual backlinks between a 741 client and a partner Martin names. Screens the partner on six criteria, states SEO value honestly, proposes 2-3 angles, drafts the article pair. Content only. Trigger on "/collab-content <client> <partner-domain>", "Backlink-Kollaboration für <Kunde> mit <Partner>", "Co-Marketing mit <Partner>". Not for client blog posts (content-writing).
---

# Co-Marketing & Backlink Collaboration (`collab-content`)

Owner: Martin Drendel · 741 Studio Standard v1.1 (2026-10-21). Spec: `00_project/collab-content-workflow.md`.
Role: local SEO strategist, partnership researcher and wellness content editor for the client.

Scope: Martin names the partner. The skill checks the fit, proposes ideas and writes two articles. It never recommends another partner, never touches a CMS, never publishes, never contacts the partner. Partner discovery (shortlist of local candidates) runs only when Martin asks "find partners for <client>".

## Hard Rules (one line each)

Reasons and incident history: `references/hard-rules.md`.

1. Screen the given partner, do not replace it. All six criteria, including a failed geo test. Martin decides at Checkpoint 0.
2. Never assume recommendation fit. Unclear willingness = "requires partner confirmation" + what to confirm.
3. Evidence, not invention. Verified / inferred / unanswered, each with the page that supports it.
4. One fetch per URL via `site_cache.py` (cache up to 30 days).
5. Honest SEO value. Backlink is not citation is not proximity. No map-pack promises, never "zero".
6. Plain text in client-editable boxes. No HTML tags or inline styles; Markdown only.
7. Contextual links only, inside 1,200+ words of editorial copy. No footer, sidebar or homepage swaps.
8. YMYL: no cure claims. A partner's marketing copy is not medical evidence.
9. Checkpoints 0 (fit), 1 (angle), 2 (copy) are AskUserQuestion cards. No drafting before Checkpoint 1. The skill ends at Checkpoint 2.
10. Fact and claim check is blocking: every number, name, credential traces to a source; a fresh subagent reviews both articles; below 5/5 slop or an open fact gap blocks Checkpoint 2.
11. Reciprocal backlink check is blocking: `lint_collab.py` always with `--client-domain` and `--partner-domain`. `article_client.md` must link to the partner's domain, `article_partner.md` to the client's.
12. Link only to pages in the crawl cache. Never guess a sub-page URL.
13. `article_partner.md` shows the client's full relevant offer: lead service in depth plus a section with every other fitting service, min 2 distinct client-domain URLs (aim 3-4), recorded as `secondary_client_pages` in `spec.json`.

## Process

Full step list: `references/checklist.md`. Files live in `00_project/assets/<client>/collab/<partner-slug>/`.

1. **Client first.** Read `00_project/assets/<client>/01-client/client-baseline.md` (or `content-pool/01-client/`), crawl home, about and core service pages via cache. Flag missing facts `[FEHLT]`. Save `collab/_screening/client-review.md`.
2. **Screen the partner.** Not a competitor (`02-competitors/urls.txt`). Crawl home plus the page nearest the lead service. Score the six criteria (geographic, audience, values, service compatibility, recommendation fit, editorial quality). Save `partner-fit.md`.
3. **SEO value.** Local audience relevance, organic and referral potential, limits.
4. **Checkpoint 0: fit card.** HALT until Martin confirms partner and lead service.
5. **Content approach.** 2-3 ideas (audience and intent, what each business contributes, structure, link placement, next step). Connect services through useful context, never imply proven synergy. Save `spec.json` (schema: `references/collab-schema.md`), incl. `secondary_client_pages`.
6. **Checkpoint 1: angle card.** HALT until Martin picks the angle.
7. **Draft the pair**, 1,200-1,800 words each, metadata block (Title, SEO title, Meta description, Slug). State each disclaimer once. Give both businesses the same real visibility; never undercut the partner's brand. Save `article_client.md`, `article_partner.md`.
8. **Lint loop.** `python3 .claude/skills/collab-content/scripts/lint_collab.py <article_client.md> <article_partner.md> --client-domain <client-domain> --partner-domain <partner-domain>`, then `python3 .claude/skills/slopmonster/tools/deslop.py <file>` (5/5; `cleanse.sh` below). Re-check word count after any cleanse.
9. **Fact and claim check (blocking).** `python3 .claude/skills/collab-content/scripts/check_claims.py <article> --sources <client-review.md|baseline> <partner-fit.md> <cached pages>` (pre-filter only). Then a fresh subagent without drafting context checks both articles against the dossier and reports correctness gaps only. Fix, re-lint. Max 2 reviewer rounds, then show Martin the open items. Record the result in `_run.json`.
10. **Checkpoint 2: copy card.** Send both files with word counts, lint and fact-check result. `python3 .claude/skills/collab-content/scripts/write_run.py <client> <partner-slug> <status> <checkpoint> '<details-json>'`. The skill ends here.

## Crawl cache (`scripts/site_cache.py`)

```
python3 .claude/skills/collab-content/scripts/site_cache.py get  <url> [--max-age-days 30]
python3 .claude/skills/collab-content/scripts/site_cache.py put  <url> --from-json <firecrawl.json> | --markdown-file <page.md> [--trimmed]
python3 .claude/skills/collab-content/scripts/site_cache.py show <url>
python3 .claude/skills/collab-content/scripts/site_cache.py list [<domain>]
```

Cache root: `00_project/crawl-cache/<host>/<key>.json`. Run from the repo root.

## References

- `references/hard-rules.md`: full rule text with incident history
- `references/checklist.md`: full operational checklist
- `references/collab-schema.md`: schemas for `shortlist.json` and `spec.json`
- `00_project/collab-content-workflow.md`: master workflow architecture
