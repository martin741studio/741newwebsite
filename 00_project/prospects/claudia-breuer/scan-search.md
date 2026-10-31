# Scan search: Claudia Breuer (agent D, part 1, 2026-10-31)

## Existing scans (0 credits)

- `python3 prospect-mini/scripts/find_scan.py "ChIJK1UCsI_lvkcREbu_yXcCZ1M"` returned `total: 0`.
- `python3 prospect-mini/scripts/find_scan.py "Breuer"` returned `total: 0`.
- **Usable scan: NO.** No Local Falcon scan report exists for this place, so there is nothing to reuse.

## Place confirmed (searchForLocalFalconBusinessLocation, term "Claudia Breuer Heilpraktikerin für Psychotherapie", proximity "Bonn", 2 credits)

| Field | Local Falcon value |
| --- | --- |
| Name | Claudia Breuer Heilpraktikerin für Psychotherapie |
| place_id | ChIJK1UCsI_lvkcREbu_yXcCZ1M (matches intake.md) |
| Address | Wurzerstraße 100, 53175 Bonn |
| lat / lng | 50.6958612 / 7.1589297 |
| Rating | 5.000 |
| Review count | 5 |
| Category (Local Falcon, English) | Counselor |
| claimed flag (Local Falcon) | 0 |
| Service-area business (sab) | false |
| Website | https://www.breuer-psychotherapie.de/ |
| Phone | 015225699074 |

Notes:
- Rating, review count, address and coordinates match the Maps panel in `evidence/google-panel-2026-10-30.md` (5,0, 5 reviews, same lat/lng).
- The category differs: Local Falcon says "Counselor", the panel shows "Life Coach". The panel decides (workflow lesson 2).
- The Local Falcon `claimed` flag is 0, but the panel shows an owner reply and no "Inhaber dieses Unternehmens?" prompt. Do not write "unclaimed" on the page. Use only what the panel shows.

## Gap keyword and scan status (updated 2026-10-31 after demand re-run)

- `demand.md` now passes the gap rule for "psychotherapie bonn" (volume 2900, own site not in the organic top 20).
- Scan run once: report_key 5d88be0ed475d1e, 7x7, radius 5 km, centre 50.6958612 / 7.1589297, platform google. 49 credits (ledger). Result in `competitors.md`.
