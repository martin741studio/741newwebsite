# Scan search: Christian Ruether (agent D, 2026-10-12)

## Profile
- Google business profile: YES.
- Evidence file: `evidence/maps-match.md`. The website (soziokratie.org) and the phone (+43 699 11114398) both match.
- Name on Google: Soziokratie. Address: Neustiftgasse 89-91, 1070 Wien (in: Cult Café).
- Panel state (`evidence/google-panel-2026-10-12.md`): no rating, 0 reviews, no category, no opening hours, no owner photos. The panel shows "Als Inhaber eintragen".
- Coordinates: 48.2053627, 16.3462806.

## place_id
- place_id: `ChIJK4gOPu0HbUcRTbTf3oxEphI`
- Check: the hex part of this id (0x476d07ed3e0e882b) equals the FID in `evidence/maps-match.md`. The match is exact.
- Source: `python3 prospect-mini/scripts/find_scan.py --place "Soziokratie" --proximity "Wien"` (run once, 2 credits).
- The same call returned a second place: "Soziokratie Zentrum" (`ChIJS6FLxCambUcRbnaZqATfm-U`, Maria-Lassnig-Straße 32/2, 1100 Wien). This is a different business with a different phone. Do not use it.

## Existing scans
- `find_scan.py "ChIJK4gOPu0HbUcRTbTf3oxEphI"` returned: total 0. No scan exists for this place.

## Gap keyword (from `demand.md`, agent A)
- Proposal: "organisationsberatung wien" (20 per month, CPC 5.35 USD, competition HIGH). soziokratie.org is not in the organic top 20.
- Rejected by agent A: "soziokratie" (rank 1 already), "konsent moderation" (rank 1 already), "moderation wien" (wrong intent).

## Risks for the scan (for the gate decision)
- The profile has no category and no reviews. A red or empty grid is likely. This fits the story "profile exists but is not set up".
- The address is a café (Cult Café). Local Falcon scans from the profile coordinates. The center point is correct.
- The site has no consulting page today. The grid would show the gap on the map and the gap on the site.
- Alternative keyword if the gate wants a service match close to his own wording: none has volume. Agent A found "organisationsberatung wien" as the only gap term with a real CPC.

## Decision
**scan possible: run under the standing G1 go.**
- Suggested scan: place_id `ChIJK4gOPu0HbUcRTbTf3oxEphI`, keyword "organisationsberatung wien", proximity Wien, gridSize 7 (Local Falcon MCP only).
- No new scan was run. Credits used in part 1: 2 (place search).
