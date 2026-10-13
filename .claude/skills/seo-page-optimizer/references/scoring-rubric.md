# Scoring rubric + GEO principles

Used two ways: as a **self-check** after a CREATE spec, and as the **scoring grid** for an AUDIT.
Score each dimension 0–100 with a one-line reason. In AUDIT, every reason quotes real evidence from
the page — never a guess. If you did not fetch the page, you cannot score it; fetch it first.

## The eight dimensions

| # | Dimension | 90–100 (aligned) | 0–40 (broken) |
|---|---|---|---|
| 1 | **Search-intent match** | page type matches intent (local-commercial → clinic/booking page, not an essay) | wrong page type for the intent |
| 2 | **Topical depth** | covers what the top results cover + a real edge; answers the cluster | thin; misses subtopics competitors rank with |
| 3 | **GEO-extractability** | direct-answer block, clean definition, FAQ, factual statements, named entities | wall of prose, no liftable answer, no lists |
| 4 | **E-E-A-T** | real named practitioner + credentials + first-hand specifics | anonymous, generic, no author/qualification |
| 5 | **Local signals** | city + real catchment in copy; NAP matches the locked record | no place named, or NAP mismatch |
| 6 | **Technical on-page** | title ≤60 with keyword front-loaded, meta ≤155, one H1, logical H2/H3 | missing/duplicate title, no H1, keyword absent |
| 7 | **Schema** | LocalBusiness/MedicalBusiness + Service + FAQPage + Person, valid JSON-LD | none, or invalid/irrelevant |
| 8 | **Internal links** | links up to a pillar + across to sibling cluster pages | orphan page, no internal links |

Overall verdict = aligned / partially aligned / not aligned, with the reason. Then a **prioritised
gap-and-fix list**: biggest ranking/AI win first, each fix concrete and tied to a dimension above.

## Why these, and what GEO actually means

**Google side (topical authority).** A page wins by being the most complete, trustworthy answer for
the intent. Depth (dimensions 1–2), trust (4), and clean structure (6–8) are what earn that. Thin or
off-intent pages lose regardless of keywords.

**AI-answer side (GEO/AEO).** Answer engines (ChatGPT, Google AI Overviews, Perplexity, Gemini) quote
what is easy to lift. That is dimension 3, and it is the part most pages miss:

- **Direct answer up top** — 2–4 self-contained sentences right under the H1 that answer the query
  without needing the rest of the page.
- **Clean definitions** — one crisp definition of the core term; engines extract these verbatim.
- **Real questions, plainly answered** — the actual PAA questions, each answered in 2–3 tight
  sentences, and shipped as `FAQPage` schema.
- **Concrete facts, not adjectives** — who, where, how long, what it costs (if public). Engines cite
  specifics; they ignore "leading" and "world-class".
- **Named entities** — methods, conditions, city, neighbouring areas stated explicitly so a machine
  is never guessing what the page is about.
- **Structured data** — schema is the machine-readable spine that ties facts, service, and author
  together.

The two sides reinforce each other: the same clarity that makes a page quotable also makes it a
better Google result. Optimise for both at once.

## Compliance is scored too

For health/YMYL clients, a page that ranks by making claims we cannot legally or ethically make is
**not** "aligned" — flag it. DACH health copy follows HWG (no promised cures, no guaranteed
outcomes, no fear-based claims). Compete on depth, trust, and specificity instead. See
`hwg-fallstudien-guideline` and `program-deliverable-rules`.
