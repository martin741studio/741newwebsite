# Data package — the input contract

The output is only as good as this input. Assemble it before writing (CREATE) or before a
data-backed audit (AUDIT). Every field is either a real number from a source below or marked
`[fehlt: …]`. Never invent a value to fill a gap.

## Required fields

| Field | Where it comes from | Notes |
|---|---|---|
| Primary keyword | client / brief | the one term the page targets |
| Primary volume + difficulty | DataForSEO Labs `keyword_suggestions/live` or `ranked_keywords/live` | difficulty only comes from `ranked_keywords` |
| Secondary/cluster keywords + volumes | DataForSEO Labs `keyword_suggestions/live` | the terms the page should also cover |
| What the domain already ranks for | DataForSEO Labs `ranked_keywords/live` (target = the client domain) | avoid cannibalising an already-ranking URL — improve it instead |
| Top 3–5 SERP competitors + their subtopics | DataForSEO SERP + open the pages | defines the depth needed to compete |
| People-Also-Ask / real questions | DataForSEO SERP `people_also_ask`, Google autocomplete/PAA | feeds FAQ + GEO answer blocks |
| Client true services + method names | `client_locations`, the brief, the GBP | never a service the client does not offer |
| Canonical NAP | `client_locations` where `nap_status='locked'` | single source of truth for name/address/phone/category |
| Practitioner + credentials | the brief / GBP / about page | E-E-A-T; real person, real qualification |
| City + real catchment | GBP + Local Falcon grid | only towns with real demand get a page; small towns → body mentions |
| Market language | the client record | EN for expat/international (Bali), DE for DACH — sets the copy language |

## DataForSEO call notes

- location_code **2276** = Germany; language_code **`de`** for DACH clients. For an English/expat
  market (e.g. Bali → Indonesia), use the matching location_code + `en`.
- Prefer `dataforseo_labs/google/keyword_suggestions/live` (on-topic) and
  `dataforseo_labs/google/ranked_keywords/live` (what a domain ranks for, includes
  `keyword_difficulty`).
- **Avoid** `keyword_ideas/live` — it expands too broadly and returns junk for a single page.
- No Ahrefs (plan expired) — DataForSEO is the source. See memory `seo-tooling-dataforseo`.
- Thin data? Sense-check a term via Google autocomplete / PAA / Trends before trusting it.
  A `0` is usually "no data", not "no demand". See memory `sensecheck-keywords-google`.

## Traffic / engagement metrics (audit only)

Bounce rate, sessions, entry/exit, and engagement come **only** from GA4 / Search Console for that
property — never estimated. If you do not have GA4/GSC access for the page, the audit is
content-and-structure only; say so, and do not print a made-up bounce or traffic number.

## If a GEO citations tool is connected

When an AI-visibility tool (e.g. a brand-radar / AI-response MCP, or GSC AI-Overview data) is
available, pull the client's current AI mentions/citations for the topic as a real baseline. If not,
GEO is assessed structurally (is the page built to be quoted?), not by a fabricated citation count.
