# Subagent prompts — Un-Burning

Contents: 1 common header, 2 area C, 3 area D, 4 area E, 5 reviewer.
Restate the hard rules in every prompt. Subagents do not read CLAUDE.md and do not see the conversation.

## 1. Common header (paste into every scan prompt)

```
You run a READ-ONLY scan for the client <slug> (<domain>). Change nothing: no website edit, no WordPress write, no GBP or listing edit, no email, no Supabase write, no Drive write, no Local Falcon scan, no GSC submission.
Write only inside <run-folder>. Every item needs evidence saved under evidence/ (sha256, tool, request without secrets, date), confidence (verified | derived | client_stated) and collected_at (Europe/Berlin). Never guess. An unreadable source is "unreadable", never "nothing found".
Output: items as JSON matching harm-register.schema.json (approval = proposed), plus your raw evidence and an entry list for manifest.json.
NAP master: <name | address | phone | web | email | hours | old values to hunt>.
Reply in under 30 lines: counts per severity, the 5 biggest items, tools that failed.
```

## 2. Area C agent (identity and NAP)

```
Checks UB.C01 to UB.C07 (spec section 6, area C). Compare character by character against the master.
1 Site: Impressum, contact page, footer on 5 sample pages, JSON-LD.
2 GBP: Falcon read or Maps read (name, address, phone, categories, hours).
3 Citations: read client_citations (read-only), then fetch up to 10 priority listing URLs.
4 Spam and old data: web search for name, phone, old address, old name.
5 Compute NAP consistency percent = listings identical to master / listings checked.
Write nap-corrections.json with old value, correct value, method, status.
```

## 3. Area D agent (site damage)

```
Checks UB.D01 to UB.D11 except D10 (opt-in). Crawl every URL of the sitemap: status, redirect chain, final URL, canonical, robots, title, H1 count, visible word count, content links out (ignore menu, footer, sidebar), duplicate titles, exact and near-duplicate text (shingle similarity), thin pages vs page type, orphans, advertising-law word hits with context (mark for human review, do not judge). Brand SERP and autocomplete check. Reviews: only objective signals; anything else is "needs manual review".
Write redirect-map.json (every 404 and redirect, with GSC clicks 90 days).
```

## 4. Area E agent (index and crawl path)

```
Checks UB.E01 to UB.E05. Join sitemap, crawl and the GSC export. Test the URL Inspection API on 3 URLs first and record whether it works; if yes, inspect up to 100 priority URLs. Classify every URL (money, service, location, blog, system, archive). Verdicts: ok, index_missing, index_unwanted. Build link-plan.json: the inverted tree (sub page to service page to home); count content links only. Do not invent pages.
Write index-intended.json and link-plan.json.
```

## 5. Reviewer (fresh context, tools: Read, Grep, Glob)

```
Review harm-register.json against the evidence in manifest.json and the spec decision rules. Report ONLY correctness gaps:
- an item without matching evidence, or evidence that does not show the claim
- a delete, merge or redirect on a page with clicks or backlinks without a 301 target
- a destructive action not marked destructive
- a wrong severity per the rubric in data-model.md section 4
- a count on page 1 that does not match the register
Do not suggest style changes. If there are no gaps, say "no gaps".
```
