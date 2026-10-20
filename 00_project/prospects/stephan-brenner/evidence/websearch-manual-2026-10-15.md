# Manual web search (fallback), 2026-10-15

Not DataForSEO data. No volumes, no positions, not Google's local results. Used only because all DataForSEO calls returned task 40207 (IP not whitelisted, cost 0).

## Query 1: "rechtsanwalt gesellschaftsrecht stuttgart" (WebSearch, standard)

Firm pages with Gesellschaftsrecht focus in Stuttgart, in the order returned:
1. MTR Legal, Gesellschaftsrecht Stuttgart: https://www.mtrlegal.com/offices/Stuttgart/Gesellschaftsrecht/ (firm page)
2. MTR Legal, GmbH-Recht Stuttgart: https://www.mtrlegal.com/offices/Stuttgart/gesellschaftsrecht/gmbh-recht/ (firm page)
3. HWS Rechtsanwaltsgesellschaft mbh, Stuttgart: https://www.hws.de/en/locations/stuttgart/hws-rechtsanwaltsgesellschaft-mbh (firm page)
4. Gleiss Lutz, Stuttgart office has a Gesellschaftsrecht group (source: search summary, no direct URL in result list)
5. Menold Bezler, job ad for Gesellschaftsrecht (job board, not a provider page)
6. Flick Gocke Schaumburg, job ad (job board, not a provider page)
7. PwC Legal, job ad (job board, not a provider page)
8. fachanwalt.de directory, Stuttgart list (directory, excluded from competitor URLs)

contiq.de does not appear in the result list.

## Query 2: "CONTIQ Rechtsanwaltsgesellschaft Stuttgart" (WebSearch, standard)

No CONTIQ page in the results. Other Stuttgart firms returned: STR Rechtsanwaltsgesellschaft mbH (cylex directory entry), HWS Rechtsanwaltsgesellschaft mbh.

Reading: the index did not return the firm's own site for its name. This is a gap of this search tool. It is not proof that the firm or its site is missing. The Google panel (evidence/google-panel-2026-10-15.md) shows the firm, the phone number and contiq.de.

## Not done (blocked)

- Volumes (keywords_data, 12 terms): task 40207, cost 0.
- SERP organic, 2 main services: task 40207, cost 0.
- Spam links (backlinks/summary, referring_domains): task 40207, cost 0.
- Name search "<business> <city>" via SERP: not run (same block).

Cause: DataForSEO account IP whitelist. Outbound IP at run time: 179.65.207.101. Fix is a Martin step in the DataForSEO panel (API access). Not changed by the agent.
