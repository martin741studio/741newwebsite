# Dry run summary: Praxis Suriya (read only)

Run: 2026-10-11. Catalogue v0.1.0. Done by a background agent, summary text saved by the design chat (the agent could not write this file). Nothing was written to Drive, Supabase, the site, the Google profile or the portal. Files: `matrix.json` (77 rows), `evidence-index.md`.

## 0. Update after the Local Falcon pull (11.10.2026, later the same day)

Why Falcon was "not connected": no Local Falcon MCP server is configured in this Claude session. The MCP endpoint itself works. Direct JSON-RPC calls with the key from `.env` (Bearer header) return live data. The script `scripts/falcon_read.py` does this, read-only (only list, get, search and view tools; scans are refused). The GBP is connected through OAuth in the Local Falcon account, so live profile, services, posts, media and reviews are readable. Raw files: `falcon/`.

Result: 11 measures moved from unknown to a verified status. New counts: done 2, partly 37, missing 15, n/a 7, unknown 16.
Key new facts:
- The live profile name is now "Praxis SURIYA - Nervensystemregulation · Schmerztherapie · Ayurveda-Massage" (3 keywords, pending edits). It changed since the 30.09. baseline. Gate 1 case, un-burning UB.C03.
- Service area lists 17 places including "Deutschland". Faszientherapie is still a listed service. 23 services, none with a description.
- 12 reviews, none answered. Newest review 05.07.2026, none in the last 90 days.
- 3 posts (last 07.07.), 5 photos (newest 2024).
- Profile is verified, no ownership conflict, no guideline issue.
- 10 scan reports exist (newest 16.08.2026, 56 days old, inside the 60-day scan rule until 14.10.).

### Audit fields run for Suriya (same day, free)

B10.01, B11.05 and B11.09 were derived from the Falcon reports of 15 and 16.08. with the audit chat's `analyze_drivers.py` (see `audit-fields/summary.md`). G06 and G07 moved to `done` (derived). Counts now: done 4, partly 35, missing 15, n/a 7, unknown 16.
Important: on 15.08. the profile name was "Heilpraktiker Ingelheim I Praxis Suriya - Ayurveda & Naturheilkunde". Names with the search words are 6 to 7 times more common in the top 10 for "heilpraktiker ingelheim". Today's name no longer holds those words. The 77 to 92 percent SoLV of 15.08. may have rested partly on the name. A re-scan (49 credits) needs Martin's go.

## 1. Counts (before the Falcon pull; see section 0 for the new counts)

| Pillar | done | partly | missing | n/a | unknown | total |
| --- | --- | --- | --- | --- | --- | --- |
| P1 Google-Profil | 1 | 3 | 3 | 4 | 11 | 22 |
| P2 Website | 1 | 20 | 10 | 1 | 3 | 35 |
| P3 Off-Page | 0 | 7 | 2 | 2 | 9 | 20 |
| Total | 2 | 30 | 15 | 7 | 23 | 77 |

- Confidence: verified 21, derived 33, none 23.
- 13 measures are blocked by un-burning: G01, G19, G20, G22, W15, W18, W34, O01 to O05, O19.
- G02 and G21 are not blocked. No open harm item exists for them. The address matches in 13 of 13 readable listings.
- No task is proposed for gate or OUT measures. Each row names the gate and the missing proof.
- Stale cells: 7 (G05, G08, G09, G12, G18, W01, O14).

## 2. Top 5 conflicts and surprises

1. **Name chain.** The profile, `client_locations`, `client_master_data`, the aggregator pack, the BrightLocal brief, the runbook and the Foursquare URL all keep the suffix "Ayurveda & Naturheilkunde". Gate 1 needs legal proof and none exists. Martin's decision of 01.10. (name stays) and the locked source of truth (official name "Praxis Suriya") disagree.
2. **Reviews flat at 12** on 14.08., 30.09. and 11.10. The portal marks the review-process task done (closed in bulk on 21.09.). Those closures are claims, not proof.
3. **Citations.** The portal shows 31 as live, but 30 have no URL. The un-burning live check finds 0 of 16 listings with exact NAP. Listings carry old names, three old phone numbers and duplicates (Cylex, Infobel, Theralupa, MapQuest). GoYellow returns 410. Theralupa, GoLocal and Jameda exist live, but the portal says "planned".
4. **Wrong hours in drafts.** The night-shift drafts (06.10. and 09.10.) use Di to Do 07:30 to 18:00. The aggregator pack and the BrightLocal brief use Di to Fr 09:00 to 19:00. Live hours are Mo to Sa 07:30 to 20:00. Running a draft would break NAP.
5. **Old internal records.** Memory says the site has no local schema, but the live site has MedicalBusiness JSON-LD with a fixed 5/12 rating. The profile service list and `client_locations` still list Faszientherapie, which Coralie does not offer. The cost page says "Behandlung 80 €", the confirmed price is 95 €. The imprint shows the placeholder VAT ID DE999999999. The review widget quotes use outcome words ("Besserung") and have no link to the Google profile (HWG check needed).

## 3. Missing or unreadable sources

- Local Falcon tools were not connected in the agent session. Description, services, photos, posts, replies, service area and categories could not be read (G03, G05, G06, G08, G09, G11, G12, G18).
- No audit run exists for Suriya. Audit fields B04 to B13 are missing. The Drive client folder holds no audit doc except the sheet of 20.07.
- The un-burning harm register did not exist at run time. The agent cited their result files (`nap-corrections.json`, `index-intended.json`, `link-plan.json`, crawl). There are no harm row IDs.
- The PageSpeed API returned 429. W01 stays unknown. No Ahrefs and no paid DataForSEO call was made.
- Cylex, 11880 and MapQuest block fetches. Facebook and LinkedIn are not readable.
- The Keyword & SEO Matrix sheet was listed, not read. No status needs it.
- The week-1 report is 58 days old.

## 4. Catalogue problems found and what the design chat did about them

| Problem | Fix (catalogue 0.1.0, same day) |
| --- | --- |
| `confidence_values` had no `none` | Added |
| G01 text said the suffix was removed | Corrected. Status rule now has "risk present" under `missing` |
| Age rule scope unclear (a fresh site check plus an old profile read made G08 look fresh) | Evidence `role`: `rule_source` sets status and age. `secondary_claim` never does. Validator and spec updated |
| G06, G07, G17, W07, W15 cannot be `done` without audit data | Flag `needs_audit` and spec rule 11 |
| W08 "main services" undefined | Defined: pillar pages of the approved tree, else top 5 by margin or demand |
| W10, W34 had no rule above 3 errors | `missing` = more than 3 errors |
| O02 and O03 overlapped | O02 = local directories, O03 = core and map-data listings. Separate evidence sources |
| O12 said "See O06" | Written out |
| O14 `live` age shorter than the monthly cadence | Age class set to `scan` (60 days) |
| No rule for proof of absence | Spec rule 9: logged search in repo, Drive and Supabase gives `missing`. Client-side fact without data gives `unknown` |
| `default off` is not a fact (G10 health, G13, W24) | Flag `default_off`: `n/a` until Martin switches it on |
| G18 automation codes vs "client answers reviews" | Text clarified: 741 never replies |
| Portal task `erledigt` is not evidence | Spec rule 9: claim only |

## 5. Questions only Martin can answer

1. Name: keep the suffix (needs legal proof) or rename to "Praxis Suriya"? The decision of 01.10. and the locked source of truth disagree.
2. May a later run connect Local Falcon, or use a public Maps read? 11 P1 cells wait for it.
3. Which page tree is approved: the portal tree of 13.09. or Dinakar's set of 29.09.? (W15)
4. Is there a budget for a backlink snapshot with 3 competitors? (O14 to O16)
5. Does Coralie hold a Gewerbe or an IHK entry? Without it, O07 stays n/a.
6. Does the 01.10. decision to leave the imprint VAT ID still hold?
7. Is the 10 percent 5-card lymph offer cleared for HWG section 7?
8. Which host is canonical for all listings: www or non-www?
9. Should the tasks bulk-closed on 21.09. be reopened?
10. Is "nothing found" valid proof for `missing` on 741-side artefacts (W03, W04, W05, O17, O19)? (The design chat set it as the rule. Martin confirms.)
11. Who asks for reviews, and in which channel? (G14, G15)

## 6. Time (agent estimate, no clock kept)

About 70 minutes: catalogue, memory and 00_project docs 20, Supabase SELECT 5, Drive 4, live site and crawl parse 12, un-burning files 6, matrix, index and summary 25.
