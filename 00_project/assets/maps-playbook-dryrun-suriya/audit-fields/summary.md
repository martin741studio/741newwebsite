# Audit fields B10.01, B11.05, B11.09 for Praxis Suriya (derived, free)

Run: 2026-10-11. Method: the audit chat's script `audit-workflow/scripts/analyze_drivers.py` (reused, not rewritten) on the 8 newest Google Falcon reports from 15 and 16.08.2026 (7x7 grid, 5 km; plus one 2.5 km report of 26.07.). No scan was started. No paid call. Files: `evidence/falcon-report-*.json`, `evidence/drivers.json`.

| Field | Result | Status |
| --- | --- | --- |
| B10.01 Kategorien | Primary "Naturheilpraktiker" equals the leader's primary in "heilpraktiker ingelheim" and is the driver category in "akupunktur ingelheim". In "migräne behandlung" the leaders are neurologists and clinics, so there is no comparable primary | green (derived) |
| B11.05 Kategorien-Lücke | The client holds every category with lift near or above 2.0: naturopathic practitioner (lift 3.05 in akupunktur, 1.7 to 1.85 in heilpraktiker) and pain control clinic (1.98 in migräne). Gap 0 | green (derived) |
| B11.09 Treiber-Analyse | Driver category in "akupunktur ingelheim": naturopathic practitioner (57 percent of the top 10, 19 percent of all). Client holds it. No driver category in the other keywords. Reviews vs SoLV: rho 0.34 in "heilpraktiker ingelheim" (review data in 77 percent of places), -0.11 and -0.01 in migräne and akupunktur | green for categories, reviews a weak driver in one keyword |

Three keywords have too few places for the test (ayurveda 4, schmerztherapie 4, naturheilpraxis 2). In "vagusnerv therapie" the client has 0 percent SoLV.

## Name finding (important)

At the time of the 15.08. scans the profile name was "Heilpraktiker Ingelheim I Praxis Suriya - Ayurveda & Naturheilkunde". The name-keyword test shows names that contain the search words are 6 to 7 times more common among the top 10 for "heilpraktiker ingelheim" (lift 7.4 at 2.5 km, 6.1 at 5 km). The client's own name had them. Today the live name is "Praxis SURIYA - Nervensystemregulation · Schmerztherapie · Ayurveda-Massage". The words "Heilpraktiker Ingelheim" are gone from it.
- The 77 to 92 percent SoLV of 15.08. may have rested partly on the name. The current rank is unknown.
- A re-scan of "heilpraktiker ingelheim" (49 credits, same grid and radius) would show the effect. It needs Martin's go.
- This does not argue for keywords in the name. It shows the stake of gate 1. The legal route (DBA with proof) or the clean name decides, not the rank.

## Limits

- Falcon review data is incomplete in some reports (coverage 77 to 100 percent). Own review numbers come from the Google profile (12).
- Scan evidence is from 15.08. (57 days). It leaves the 60-day rule on 14.10.2026.
- A category lift shows a link in the data, not proof of cause.
