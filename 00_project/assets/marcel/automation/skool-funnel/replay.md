# Dry run 1: replay of the real Skool funnel build through the guard

Date: 2026-10-11 · Mode: Trockenlauf (paper). Source: memory `marcel-rosenbach-client` (2026-09-01 to 2026-09-04). No system was touched.

Each real action from the build history goes through `automation_lib.classify()` (the guard code). Column "Workflow rule" says what the new workflow would have required.

| Date | Real action | Class | Workflow rule | Guard reason |
|---|---|---|---|---|
| 2026-09-01 | Turn on Skool plugins "Mitgliedschaftsfragen" + "Zapier" | G | needs Martin's go A<n> | click: "Enables the Zapier plugin in the DEEP NLP group" (send, publish or switch on) |
| 2026-09-01 | Create KlickTipp tags + fields | test_write | free (logged, evidence + readback) | UI input (read the state back after it) |
| 2026-09-01 | Build Zap 378535838 as draft (steps 1-4) | test_write | free (logged, evidence + readback) | UI input (read the state back after it) |
| 2026-09-01 | $1 test purchase in Skool (Martin) | M | Martin does it | click: "Buys the Standard plan for $1" (delete, money, prices, invites or permissions) |
| 2026-09-01 | Delete test Zap 378583310 | M | Martin does it | click: "Deletes Zap 378583310" (delete, money, prices, invites or permissions) |
| 2026-09-02 | Run "Test step" with Martin's real record (not TEST-741) | test_write | free (logged, evidence + readback) | UI input (read the state back after it) |
| 2026-09-02 | Write KlickTipp mail body via JS (CKEditor setData + Save) | G | needs Martin's go A<n> | page script that clicks, posts or changes values |
| 2026-09-03 | Activate KlickTipp campaign 2048561 | G | needs Martin's go A<n> | click: "Aktiviert die Kampagne 2048561" (send, publish or switch on) |
| 2026-09-03 | Publish Zap v1 ("Your Zap is on") | G | needs Martin's go A<n> | click: "Publishes Zap 378535838" (send, publish or switch on) |
| 2026-09-03 | Delete test contact in KlickTipp + 3 test deals in Pipedrive | M | Martin does it | click: "Deletes deal 2524" (delete, money, prices, invites or permissions) |
| 2026-09-04 | Pipedrive demo deal via Zapier MCP | G | needs Martin's go A<n> | execute_zapier_write_action: write on live data without the TEST-741 marker |
| 2026-09-04 | Same, with TEST marker | test_write | free (logged, evidence + readback) | execute_zapier_write_action: write on TEST-741 data |
| 2026-09-04 | DELETE /v1/deals/2531 via raw request | G | needs Martin's go A<n> | execute_zapier_write_action: write on live data without the TEST-741 marker |
| 2026-09-04 | Publish Zap v3 | G | needs Martin's go A<n> | click: "Publishes Zap 378535838 version v3" (send, publish or switch on) |

## What the workflow would have caught (real failures of this build)

| Real failure | When | Layer that catches it |
|---|---|---|
| Zap v1 published "live" with 2 critical bugs: KlickTipp 406 (phone + ISO date) and Pipedrive 400 (name + first/last name). No contact, no tag, no mail series, no person | 2026-09-03 | L5: e2e case needs a passed readback in KlickTipp AND Pipedrive. The 406/400 show as "no record" → fail → no `check_report` pass → no go-live checkpoint |
| 8 of 9 KlickTipp mails had no subject and no body; the content was never saved | 2026-09-02/03 | L4: reload and read back after each save (`CKEDITOR.getData()` length > 0, subject field) |
| Early tests were all skipped ("no junk data in Marcel's accounts") | 2026-09-01 | L1: TEST-741 records are the default, so tests are never skipped for that reason |
| Pipedrive pipeline reported "missing", it existed | 2026-09-01 | L0: full inventory, every dropdown opened |
| Test deals created with Martin's real name, then deleted by hand | 2026-09-02/04 | L1 + guard: TEST-741 name makes cleanup a free, logged test_write; without the marker a delete is class M |

## Gaps found in the guard by this replay

1. Raw `DELETE` through the Zapier MCP was class G. Fixed the same day: now class M, TEST-741 deletes stay free (sandbox tests 95/95).
2. A "Test step" click with a real person's data is test_write, because the click summary carries no record data. Covered by rule: the spec names the TEST record, the preflight checks it, the verifier searches for non-TEST records in the test window.
3. Building 8 mails in a draft campaign via JS means 8 class-G calls. Use one request with `--uses 20 --contains "CKEDITOR" --contains "2048561"` and one go, or build with `form_input` and clicks (free) and read back.
