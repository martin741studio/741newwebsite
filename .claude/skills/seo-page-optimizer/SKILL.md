---
name: seo-page-optimizer
description: >
  Optimise a client page's CONTENT for Google + AI answer engines (GEO/AEO) + local
  visibility, grounded in a real DataForSEO data package — not guesswork. Two modes:
  CREATE (produce a full content spec for a new/rebuilt page) and AUDIT (score an existing
  page/URL against the same standard and return prioritised fixes). Use this whenever the
  task is about page content, on-page SEO, "optimise this page", "write the [service] page",
  "topical authority", "rank in AI / ChatGPT / AI Overviews / Perplexity", "GEO", "AEO",
  "content brief", or checking whether an existing page is aligned with our SEO standard —
  for any 741 local-SEO client (Hüwel, Suriya/Coralie, Dumann, Kamil, Brasse, etc.).
  Trigger it even when the user just drops a URL + keyword and asks "is this good?" or
  "make this rank". For the prospect Maps-grid audit deliverable use `local-seo-review-page`
  instead; this skill is about the CONTENT of a page.
---

# SEO / GEO Page Optimizer

Turn a **real data package** (keywords, competitors, questions — pulled from DataForSEO) plus the
client's **true services & NAP** into page content that (a) matches search intent and covers the
topic deeply enough to earn **topical authority** on Google, and (b) is structured so **AI answer
engines quote it** (GEO/AEO). Same standard drives both jobs: writing a new page and auditing an
existing one.

Three hard rules, because they are where SEO content usually goes wrong:
- **Real data only — never fabricate.** Every volume, competitor claim, ranking, phone number,
  address, price, and traffic/bounce metric comes from the data package or a verified source —
  never invented. NAP comes from the locked canonical record; traffic/bounce/engagement come from
  GA4/Search Console; nothing else. If a fact is missing, write `[fehlt: …]` and say so — do not
  fill the gap with a plausible-looking placeholder presented as real. (This is the single most
  common failure: a model confidently invents a phone number or a "88% bounce rate". Don't.)
  See `claims-need-real-data`.
- **Language = the client's market.** Write the page in the language the client's audience actually
  searches in: **English** for expat/international clients (e.g. Bali Healing), **German** for DACH
  practices. Do not default to German. Mismatched language (English keywords, German copy) is a real
  mistake — check the client's market first.
- **Say only what is true of the client.** Use the client's *actual* services and facts (from
  `client_locations` / the brief). Never promise a treatment or result the client does not offer.
  For health clients this is also a legal line (HWG in DACH) — see the compliance section.

## Pick the mode

- **CREATE** — a new page, or a rebuild of a weak one. You have a target keyword/topic + the data
  package. Output = a content spec (below) the client's CMS team can implement on Wix, WordPress,
  Only-Inside, Novamira, etc. Output is CMS-agnostic content, not our HTML skeleton.
- **AUDIT** — an existing page (a URL to fetch, or pasted content). Output = a score against the
  rubric + a prioritised gap-and-fix list, so we see if it is *aligned* with the standard and what
  to change. Read `references/scoring-rubric.md` for the exact dimensions and scoring.

If the user gives a URL and asks "is this good / aligned?", that is AUDIT. If they ask to write or
rebuild, that is CREATE. When unsure, ask one line; don't guess.

## Step 1 — Assemble the data package (both modes)

The quality of the output is capped by the quality of the inputs. Gather this before writing.
The full field-by-field contract + the exact DataForSEO calls are in `references/data-package.md`
— read it so the client knows what to pull. Minimum viable set:

- **Primary keyword** + monthly volume + difficulty (`dataforseo_labs/google/keyword_suggestions/live`
  for on-topic terms; `ranked_keywords/live` for what the domain already ranks for). location_code
  2276 = Germany, language_code `de`. Avoid `keyword_ideas/live` (expands too broadly → junk).
- **Secondary / related keywords** the page should also cover (the cluster), with volumes.
- **Top 3–5 SERP competitors** for the primary keyword + which subtopics/sections they cover
  (this defines the depth needed to compete).
- **People-Also-Ask / real questions** users ask (feed the FAQ + GEO answer blocks).
- **The client's true facts**: exact services, method names, NAP, practitioner + credentials.
  Prefer the **locked canonical NAP** (`client_locations.nap_status='locked'`) as the source of
  truth for name/address/phone/category — never a second variant.
- **Local context**: primary city + real catchment (only towns with real demand get their own
  page; thin copy-paste location pages are "scaled content" and get devalued — mention small towns
  in body text instead).

If DataForSEO data is thin, sense-check via Google autocomplete / PAA / Trends before trusting a
term (see `sensecheck-keywords-google`); "0" often means "no data", not "no demand".

## Step 2 (CREATE) — produce the content spec

Always return this structure. It is deliberately ordered the way both Google and AI engines read a
page: what it is, the direct answer, then the depth.

```
# Content Spec — [Page name] · [client]

## Target
- Primary keyword (+ volume/difficulty) · secondary keywords (the cluster) · search intent
- URL slug (lowercase-hyphen; keep existing URLs where they already rank)

## Meta
- Title tag (≤60 char, primary keyword front-loaded, local qualifier, brand)
- Meta description (≤155 char, benefit + primary keyword + soft CTA)

## Page outline (H1 → H2/H3)
- H1: one clear promise with the primary keyword
- H2/H3 mapped to search intent AND the competitor subtopics AND the PAA questions
  (this is how you reach topical depth — cover what the top results cover, plus a real edge)

## GEO / AI-answer layer  ← the part most pages miss
- A 2–4 sentence DIRECT ANSWER block right under the H1 (self-contained, quotable, no fluff)
- Definition box for the core entity/term (AI engines extract clean definitions)
- FAQ: the real PAA questions, each answered in 2–3 tight sentences (also ships as FAQPage schema)
- Extractable facts: concrete specifics (who, where, how long, what it costs if public) as short
  statements — engines cite specifics, not adjectives
- Entities to name explicitly (methods, conditions, city, neighbouring areas) so the page is
  unambiguous to a machine

## Body content (per section)
- Draft copy or clear guidance per H2, in the client's real voice, covering the topic fully
- E-E-A-T: name the practitioner + credentials + real experience; first-hand, specific, honest

## Structured data (JSON-LD)
- LocalBusiness/MedicalBusiness (NAP from the locked record) + Service + FAQPage
  + Person (practitioner, with sameAs) for E-E-A-T

## Internal links
- Link up to the pillar/hub page and across to sibling cluster pages (topical authority is a mesh,
  not single pages)

## Local signals
- City + real catchment named naturally in copy; NAP identical to the locked canonical record
```

Then run the **self-check**: read `references/scoring-rubric.md` and confirm the spec would score
well on every dimension before handing it over. Note any dimension you could not satisfy and why.

Then run the **de-slop check** on the body copy (not the meta/schema blocks): the
`slopmonster` skill's `tools/deslop.py --text "..."` scores AI-sounding vocabulary and
sentence shapes out of 5. Below 5/5, rewrite the flagged lines in plainer words before
handing the spec over — a page that reads like every other AI page loses trust and, for
GEO, quotability. This is separate from the SEO rubric: a spec can score well on structure
and still sound like AI wrote it.

## Step 3 (AUDIT) — score an existing page

1. Get the page: fetch the URL (or use pasted content). Note the target keyword (ask if not given).
2. Score each dimension in `references/scoring-rubric.md` (search-intent match, topical depth,
   GEO-extractability, E-E-A-T, local signals, technical on-page, schema, internal links) 0–100,
   with a one-line reason grounded in what is actually on the page — quote the evidence.
3. Return: overall alignment verdict + a **prioritised gap-and-fix list** (biggest ranking/AI wins
   first), each fix concrete and implementable, tied to the rubric dimension it lifts.
4. If a target/competitor data package exists, compare the page against it (does it cover what the
   top results and the PAA cover?). If not, say the audit is content-only and offer to pull the data.

## Compliance (health clients — most of ours)

Health/medicine is **YMYL**: Google suppresses medical content without demonstrable expertise, and
German **HWG** forbids specific claims. So: no promised cures or guaranteed outcomes, no before/after
misuse, no fear-based claims; keep statements to what the practitioner genuinely does and is
qualified for; lead with E-E-A-T (real person, credentials). See `hwg-fallstudien-guideline` and
`program-deliverable-rules`. When a competitor ranks with a claim we may not make, compete on depth,
trust and specificity instead — never by copying a non-compliant claim.

## What good looks like (the "why")

A page wins on Google today by being the most complete, trustworthy answer for the intent — thin
pages lose. It gets *quoted by AI* by making the answer easy to lift: a clean direct answer, real
questions answered plainly, defined entities, structured data, concrete facts. These two goals
reinforce each other; this skill optimises for both at once rather than trading one off.
