# Scan summary — STÜRZL Steuerstrafrecht (Un-Burning, mode scan, 2026-10-11)

Read only. Nothing on any client asset was changed. DataForSEO cost 0 EUR. Firecrawl used plan credits (not summed; S1 about 47, S3 16). Local Falcon not connected in this session: GBP live data was read only through Business Profile Manager (manager list and address).
Register: `harm-register.json` (110 items, VALID by `validate_run.py`). Evidence: `manifest.json` (186 rows with hashes). Reports: `report/internal.html`, `report/client.html` (client-safe draft, Sie).
Merged from four parts: `part-AC` (agent S1), `part-D` (agent S2), `part-E` (agent S3), `part-Abrowser` (browser read by the design session). Area A items and the access items moved to `preconditions.json` (not harm). The raw parts stay unchanged. The merged register holds the reconciliation (see `run.params.reconcile_notes`).

## Bedrock (computed)

B grey (not scanned) · C red · D red · E yellow. Ready for growth: no. Area A is retired: ownership and access are onboarding preconditions, not Un-Burning items (Martin, 2026-10-11).

| Area | Blocks revenue | Leaks link power | Cosmetic | Total | Open after dedupe |
| --- | --- | --- | --- | --- | --- |
| C NAP | 6 | 7 | 15 | 28 | 18 |
| D Site damage | 1 | 14 | 31 | 46 | 24 |
| E Index and links | 0 | 12 | 12 | 24 | 17 |

46 rows are `keep` (checked and fine, or closed as duplicate/superseded). 28 rows are blocked by access. 7 open rows are destructive and need a per-item go.

## Preconditions (onboarding, not Un-Burning items)

Ownership and access are solved with the client at the start (Martin, 2026-10-11). They are recorded in `preconditions.json` and are not harm items, lights or bedrock criteria. State seen on 2026-10-11 (read only): the Frankfurt Google profile has Anja Stürzl as Primary owner and 741 as manager; the München profile is not in the 741 account; 741 has no Administrator role in GA4; the 741 Joomla account is Administrator, not Super User; the service account has no Search Console access. These facts only mark some actions as blocked.

## Top findings

1. **Old address on every high-traffic source.** Wiesenhüttenstraße 17 still shows on the Impressum, the contact page and footer of all 13 sampled pages, the JSON-LD schema, GBP, both anwalt.de profiles (79 and 55 reviews), the BRAK directory (through a mirror), 11880, Cylex and LinkedIn. Untermainkai 26 appears nowhere public. Strict NAP consistency is 1 of 13 listings (7.7 percent). The address is now locked (Martin, 2026-10-11).
2. **Many repairs wait on access** (a precondition, not a finding): footer, schema, contact page, sitemap and redirects need a Joomla Super User. The disavow upload needs Search Console.
3. **Wrong Munich data on third-party sources.** A second Cylex entry, rechtecheck.de and two auto-generated bestattorneyusa.com profiles show another firm's street (Neuhauser Str. 3a) or wrong cities (Tucson, Boston, Frankfurt (Oder)). The real Munich entries (Oberanger 32) are correct. The Munich office is not a duplicate.
4. **Site damage that costs reach or calls.** Four team pages carry a broken phone link (`tel.+49…` instead of `tel:+49…`). The home page links to a dead page (`/schwerpunkte`). Every URL variant returns 200 with a self-canonical, so ad parameters will create duplicates. robots.txt blocks `/components/` and `/cache/` while all pages load CSS and JS from there. The sitemap exists only as an OSMap route and lists 22 of about 59 URLs (no service page, no article). 26 pages have two H1.
5. **No inverted link tree.** None of the 26 service pages links back to the home page in its text. The 9 area pages do not link up to the Leistungen hub. 85 proposed links are in `link-plan.json`. The 25 service pages are thin (111 to 376 words) and four page pairs have identical text.
6. **Spam backlinks.** 37 domains with a Premium-PBN anchor since 08/2026. The disavow file exists (2026-10-09). It is not uploaded and needs Search Console access.

Checked and fine: no noindex anywhere, one-hop redirects to https://www, real 404 pages, click depth at most 3 to every service page, website phone numbers match, no negative page-one result. "RAK Köln" on anwalt.de is the chamber named on the Fachanwalt certificate, not an address error.

## Items for human review (no judgement made)

- Advertising-law wording (BRAO, BORA, UWG): "beste" and award claims, a "Straffreiheit" heading, "garantieren wir", and the title "Fachanwältin für Steuerrecht" on Lea Wimmer's page. All rows are cosmetic, marked for review. No use of "Fachanwalt für Strafrecht" was found.
- A public forum thread (two mirror domains, 21 anonymous posts) disparages the principal's and team members' appearance. It does not mention legal work, clients or cases. It is not in the top 10 brand results. This is a reputation item, not a link case. The legal route is Martin's and the client's lawyer's decision. Nobody was contacted.
- Google autocomplete for the person's name adds political terms. The reason is not proven. Internal note only. It is not shown to the client.
- `/index.php/component/search/` returns a 500 error with database error text.
- Our own review page for this client says "München: kein Profil auffindbar". That is wrong. One fix item (H-D-046).

## Not verifiable (shown as unknown, never as "nothing found")

See `sources-unreadable.json` (12 entries): GBP live details, GBP München owners, GA4 users, Search Console, Joomla users, registrar holder, several directories behind captcha or login, index state of any URL, LCP (PageSpeed 429), anwalt.de review dates.

## Differences from the earlier manual findings

16 sub pages (not 17). 26 pages with two H1 (not 27). 14 pages without H1 (not 18). A sitemap route exists but is incomplete (earlier note: none). The 2025 note "27 JS and 12 CSS files" replaces the earlier "35 JS and 13 CSS".
