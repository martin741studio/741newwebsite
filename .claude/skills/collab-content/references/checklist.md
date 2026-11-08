# collab-content: Operational Checklist (full)

Condensed version with the gates is in SKILL.md. This is the full step list.

## Operational Checklist

```
[ ] Phase 1: Understand the client first
    [ ] Read 00_project/assets/<client>/01-client/client-baseline.md (or content-pool/01-client/)
    [ ] Crawl (via cache) the home page, about page and the core service pages
    [ ] Record: services, positioning, audience, brand voice, stated values
    [ ] Record: which services complement one another; which need careful explanation
    [ ] Record: existing content, relevant service pages, internal-link opportunities
    [ ] Flag missing or conflicting facts ([FEHLT])
    [ ] Save 00_project/assets/<client>/collab/_screening/client-review.md

[ ] Phase 2: Screen the given partner (before any writing)
    [ ] Confirm it is not a competitor (02-competitors/urls.txt) and does not compete for the same appointments
    [ ] Crawl via cache: home page + the page most relevant to the lead service
    [ ] Score the six criteria, with page citations:
        1. Geographic relevance   2. Audience relevance   3. Values alignment
        4. Service compatibility  5. Recommendation fit   6. Editorial quality
    [ ] Label each line: verified / inferred / unanswered
    [ ] Mark unclear willingness "requires partner confirmation" + what to confirm
    [ ] Save 00_project/assets/<client>/collab/<partner-slug>/partner-fit.md
    (Only when Martin asks "find partners": run the same screen on local candidates and save
     collab/_screening/partner-screening.md + shortlist.json)

[ ] Phase 3: Assess SEO value
    [ ] Local audience relevance; organic + referral potential; possible local-visibility contribution
    [ ] State limits. Backlinks are not citations and do not change proximity. No map-pack promises, no "zero".

[ ] Checkpoint 0: Fit card (AskUserQuestion)
    [ ] Present the fit result, the lead service and the partner-confirmation items
    [ ] HALT until Martin confirms the partner and the lead service

[ ] Phase 4: Content approach (Mini-Pool) for the chosen partner
    [ ] 2-3 ideas. Each idea states:
        audience + search intent; primary topic + natural local search terms;
        what each business contributes; how the services relate and where roles differ;
        page structure + internal links; natural backlink placement; next step for the reader
    [ ] Connect services through useful context (different needs, stages of a visit).
        Never imply treatments must be combined or have proven synergy.
    [ ] Label every idea that depends on partner confirmation
    [ ] List secondary_client_pages: every other client service relevant to this partner's audience,
        cached URLs only (hard rule 13) — these go into article_partner.md regardless of the angle
    [ ] Save spec.json in 00_project/assets/<client>/collab/<partner-slug>/

[ ] Checkpoint 1: Angle card (AskUserQuestion). HALT until Martin picks the angle.

[ ] Phase 5: Draft the article pair (1,200-1,800 words each)
    [ ] Each draft starts with a metadata block: Title, SEO title, Meta description, Slug
    [ ] Clear intro, logical headings, specific explanations, local references where relevant
    [ ] Descriptive, varied link text; restrained call to action that fits both brands
    [ ] Warm, credible, plain language. No keyword stuffing, no wellness clichés, no promo copy as advice
    [ ] State each required disclaimer or limit ONCE, in one section. Do not restate "this isn't a
        treatment/cure for X" in three different sections in slightly different words — a partner
        (Morlinka, 2026-10-22) flagged this as feeling repetitive rather than like editorial content.
    [ ] Give both businesses comparable, real visibility. Do not undercut the partner's own brand or
        product with a generalising line like "it doesn't have to be theirs, the principle matters more
        than the brand" — if the partner is named, name them with the same weight the client gets.
    [ ] article_partner.md: lead service in depth PLUS a short section with the client's other relevant
        services, each linked to its cached page (min 2 distinct client-domain URLs; hard rule 13)
    [ ] Save article_client.md and article_partner.md

[ ] Phase 6: Lint loop
    [ ] python3 .claude/skills/collab-content/scripts/lint_collab.py <article_client.md> <article_partner.md> \
          --client-domain <client-domain> --partner-domain <partner-domain>
        (the --domain flags are required: they are what catches article_client.md linking only to the
         client's own pages instead of out to the partner, and vice versa)
    [ ] python3 .claude/skills/slopmonster/tools/deslop.py <file>  (5/5 required; cleanse.sh below 5/5)
    [ ] Re-check word count after any cleanse (1,200-1,800)

[ ] Phase 6a: Fact & claim check (BLOCKING, same standard as content-writing's G1 + fresh reviewer)
    [ ] python3 .claude/skills/collab-content/scripts/check_claims.py <article> --sources <client-review.md|baseline> <partner-fit.md> <cached partner/client pages>
        (pre-filter only; flags candidate claims not loosely found in the sources, for the reviewer to check)
    [ ] Launch a fresh subagent with NO drafting context: give it both final articles, client-review.md
        (or baseline), partner-fit.md and the relevant cached pages. Ask it to report correctness gaps
        only — unsourced or wrong number, invented credential or practitioner name, mischaracterised
        service, claim that contradicts a cited source. No style opinions.
    [ ] Fix every reported gap. Re-run Phase 6 lint on changed files. Max 2 reviewer rounds; after that,
        show Martin the open items instead of guessing.
    [ ] Record the reviewer result (clean / gaps fixed / open items) in _run.json

[ ] Checkpoint 2: Copy card (AskUserQuestion)
    [ ] Send both files to Martin (SendUserFile) with word counts, lint results and the fact-check result
    [ ] python3 .claude/skills/collab-content/scripts/write_run.py <client> <partner-slug> <status> <checkpoint> '<details-json>'
    [ ] The skill ends here. No CMS, no publishing, no partner message.
```
