---
name: seo-page-optimizer
description: Optimises a client page's CONTENT for Google, AI answer engines (GEO/AEO) and local visibility from a real DataForSEO package. CREATE writes a content spec; AUDIT scores an existing page and returns prioritised fixes. Trigger on "optimise this page", "write the [service] page", "topical authority", "rank in AI / ChatGPT", "GEO", "AEO", "content brief", or a URL + keyword with "is this good?". Not for Maps-grid audits (local-seo-review-page).
---

# SEO / GEO Page Optimizer

Turns a real data package (keywords, competitors, questions from DataForSEO) plus the client's true services and NAP into page content that matches search intent, covers the topic deeply, and is structured so AI answer engines quote it. The same standard drives writing a new page and auditing an existing one.

## Hard rules

- **Real data only.** Every volume, competitor claim, ranking, phone number, address, price and traffic or bounce figure comes from the data package or a verified source. NAP comes from the locked canonical record (`client_locations.nap_status='locked'`), traffic and engagement from GA4 / Search Console. A missing fact is written `[fehlt: …]`, never a plausible placeholder (memory `claims-need-real-data`).
- **Language = the client's market.** English for expat or international clients (e.g. Bali Healing), German for DACH practices. Check the market first.
- **Only what is true of the client.** Use the client's actual services and facts. Never promise a treatment or result the client does not offer.
- **Health clients (most of ours):** YMYL and HWG apply. No promised cures, no before/after misuse, no fear claims; lead with E-E-A-T. Where a competitor ranks with a claim we may not make, compete on depth, trust and specificity. See `hwg-fallstudien-guideline` and `program-deliverable-rules`.

## Pick the mode

- **CREATE:** a new page or a rebuild. Target keyword plus data package in, content spec out (CMS-agnostic: Wix, WordPress, Only-Inside, Novamira).
- **AUDIT:** an existing URL or pasted content. Score against `references/scoring-rubric.md`, return a prioritised gap-and-fix list.

A URL with "is this good / aligned?" is AUDIT. "Write" or "rebuild" is CREATE. If unclear, ask one line.

## Step 1: data package (both modes)

Contract and exact DataForSEO calls: `references/data-package.md`. Minimum:

- Primary keyword with volume and difficulty (`dataforseo_labs/google/keyword_suggestions/live`; `ranked_keywords/live` for what the domain already ranks for). `location_code` 2276 = Germany, `language_code` `de`. Avoid `keyword_ideas/live` (junk).
- Secondary keywords (the cluster) with volumes.
- Top 3-5 SERP competitors with their subtopics.
- People-Also-Ask questions (feed FAQ and answer blocks).
- The client's true facts: services, method names, NAP, practitioner and credentials.
- Local context: primary city and real catchment. Only towns with real demand get their own page; small towns go into body text (thin copy-paste location pages are scaled content).

Thin DataForSEO data: sense-check via Google autocomplete, PAA, Trends (`sensecheck-keywords-google`). "0" often means no data, not no demand.

## Step 2 (CREATE): content spec

Return this structure:

```
# Content Spec — [Page name] · [client]
## Target        primary keyword (+ volume/difficulty), cluster, search intent, URL slug (keep URLs that already rank)
## Meta          title tag (≤60, keyword first, local qualifier, brand); meta description (≤155, benefit + keyword + soft CTA)
## Outline       H1 with primary keyword; H2/H3 mapped to intent, competitor subtopics and PAA
## GEO layer     2-4 sentence direct answer under the H1; definition box; FAQ from real PAA (also FAQPage schema);
                 extractable concrete facts; named entities (methods, conditions, city, neighbouring areas)
## Body          draft copy or guidance per H2 in the client's real voice; E-E-A-T: named practitioner, credentials, first-hand experience
## Schema        LocalBusiness/MedicalBusiness (locked NAP) + Service + FAQPage + Person (with sameAs)
## Internal links  up to the pillar, across to sibling cluster pages
## Local signals   city and catchment named naturally; NAP identical to the locked record
```

Self-check: read `references/scoring-rubric.md`, confirm the spec scores well on every dimension, and note any you could not satisfy and why.

De-slop the body copy (not meta or schema): `python3 .claude/skills/slopmonster/tools/deslop.py --text "..."`. Below 5/5, rewrite the flagged lines before handing over.

## Step 3 (AUDIT)

1. Fetch the URL or take the pasted content. Get the target keyword (ask if missing).
2. Score each dimension in `references/scoring-rubric.md` 0-100 with a one-line reason that quotes the page.
3. Return the overall verdict and a prioritised gap-and-fix list (biggest ranking and AI wins first), each fix concrete and tied to the dimension it lifts.
4. With a data package, compare the page against what the top results and PAA cover. Without one, say the audit is content-only and offer to pull the data.
