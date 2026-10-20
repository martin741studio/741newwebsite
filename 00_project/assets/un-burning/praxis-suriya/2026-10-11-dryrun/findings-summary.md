# Dry run summary — Praxis Suriya (read-only, 2026-10-11)

Mode: dry run. Nothing on any client asset was changed. Cost: 0 EUR (19 Firecrawl plan credits). Wall time: about 25 minutes.
Register: `harm-register.json` (62 items, validated with `skill-draft/scripts/validate_run.py`: VALID). Evidence: `manifest.json` (185 rows, hashes checked).
This file was written by the design session from the agent's report and my own re-checks. Area B was not scanned. Area A is verified in part only.

## Counts

| Area | Blocks revenue | Leaks link power | Cosmetic | Total |
| --- | --- | --- | --- | --- |
| A | 0 | 0 | 7 | 7 |
| C | 10 | 9 | 6 | 25 |
| D | 0 | 8 | 13 | 21 |
| E | 0 | 7 | 2 | 9 |

21 of the 62 rows are `keep` (checked and no harm, or not provable). 10 rows are `blocked` (need a browser read or the client). 9 rows are destructive and need their own go.
Bedrock (computed by `bedrock.py`): A grey, B grey, C red, D yellow, E yellow. Ready for growth: no.

## Top 5 leaks

1. Wrong phone numbers and hours on real listings (Cylex, GoLocal, Theralupa, Jameda, aerzte.de, MapQuest, Infobel). Strict NAP consistency is 0 of 16 listings checked. The address is right on 13 of 13 listings that show one. The old numbers were not called. Whether they still ring is unknown.
2. Four duplicate listing pairs (Cylex, Theralupa, Infobel, MapQuest) with other names or numbers.
3. The stored master record (`client_locations`) still holds the old name suffix, "Faszientherapie" and the old Instagram handle. 30 of 31 "live" rows in `client_citations` have no URL, so that table proves nothing. (Internal item. Hidden from the client view.)
4. The inverted link tree is missing. 19 of 22 blog posts link to no service page. All 8 city pages have 1 inbound content link. 49 links are missing in `link-plan.json`.
5. Index hygiene. `/akupunktur-ingelheim-praxis/` is not indexed. `/login/` and `/contact-2/` are indexed. A stale sitemap with 2 errors is still submitted in Search Console.

Good news: website NAP is clean on all 89 pages, the Impressum shows Schützenpfad 29, no redirect chain is longer than 1 hop, no Binger Str. appears anywhere, and no negative brand result was found.

## Tools

| Tool | Result |
| --- | --- |
| GSC URL Inspection API | Works. 25 of 25 calls OK. Limit 2000 per day. All 89 sitemap URLs fit in one later run |
| Local Falcon read | Not connected in the dry-run agent's session. GBP live data was not read |
| Firecrawl scrape and search | Works. Got Cylex and MapQuest where curl failed |
| RDAP and whois | Work. DENIC hides holder and registrar. Only Cyon name servers show |
| Google autocomplete, Supabase GET | Work |
| 11880, maptons, goyellow, Facebook, LinkedIn, branchen-info | Blocked or refused. Recorded in `run.json` `sources_unreadable` |

## Could not verify (shown as unknown, never as "nothing found")

- GBP live profile, owners and managers, GA4 roles, GSC owners, WordPress admins, registrar account, social profile content.
- Index state of 64 sitemap URLs. The GSC 404 list (the API does not expose it).
- Backlink anchors (opt-in flag off).
- Unproven suspicions: the privacy page names Raidboxes while DNS shows Cyon. The Impressum has the placeholder `DE999999999`. Four different Instagram handles are in use. HWG word hits are sorted for a human. No legal judgement was made.
- Differences from the 10.10 internal-link audit: `/praxis-fuer-naturheilkunde-ingelheim/` is now a 301. Seven inbound counts differ (largest: `/ayurveda-ingelheim/` 32 against 13).

## Design lessons from the dry run

1. The validator caught one broken evidence link (typo "der" for "den") that the agent's own check missed. Keep `validate_run.py` as the gate.
2. Area status needs `scanned_areas` in `run.params`. Without it, an unverified area A counted as green. Fixed in the run file. The skill must set it.
3. The client view must use only items with a reviewed `client_text`. Raw item text leaks internal names. Rule added to `build_report.py`.
4. The agent's data-model deviations: `index-intended.json` uses the extra verdicts `review`, `unverified`, `decision_needed`. The spec should add them.
5. Most listing damage is C-class and reversible. It can go in wave 1 after GO-1. Deletes (duplicates) stay per-item.
