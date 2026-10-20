# Bulk decision cards: index (final, 13 Oct 2026)

Status: IN PROGRESS. 6 of 9 clients are fully through the grill and released. 3 clients (Kamil, Rabenmütter, Johni Jaya Motor) still have only drafts, hidden from their clients, waiting for review.
Per client folder: `queue.md` (candidates, checks, keep or drop, dashboard readiness, grill result) and `drafts.sql` (the INSERTs that ran).

## 1. Overview

| Client | Candidates | Kept | Dropped | Status now | Top 3 to ask first |
| --- | --- | --- | --- | --- | --- |
| Praxis Hüwel | 45 | 6 (E4 dropped) | 39 | RELEASED (main chat): E1, E2, E3, E5, E6, E7, E8 open, hwg_checked, approver info@praxis-huewel.de. Done, do not reopen. | — done — |
| Praxis Suriya | 15 | 6 | 9 | RELEASED: E1-E4, E6, E7 open, hwg_checked, approver Coralie. Done. | — done — |
| Stürzl Steuerstrafrecht | 22 | 6 | 16 | RELEASED: E1-E6 open. Login created, approver set. Welcome mail not sent yet (Martin sends it). | — done — |
| Maria Brasse | 16 | 6 (E1 taken out) | 10 | RELEASED: E2-E7 open, approver set, not a health client any more. | — done — |
| Bali Healing | 20 | 1 new (B9) | 19 | RELEASED: B9 open. B8 deleted (pages must be indexed, not a client question). B10 open from an earlier run. | — done — |
| Naturheilpraxis Dumann | 26 (mine) + 20 more found by another session | 27 released (6 dropped: my E3 taken out, see note) | 19 | RELEASED: all 27 cards (E1-E27) open. Done, grilled across two sessions on 13 and 14 Oct. | — done — |
| Kamil Böyük | 17 | 4 | 13 | DRAFT, approver set. Not yet reviewed. | E1 Platzhalter auf physiotherapiekraft.de, E2 Leistungen-Überschrift, E3 Startseiten-Titel |
| Rabenmütter Shop | 20 | 7 | 13 | DRAFT, approver set. Not yet reviewed. | E1 Standardtext Produktseiten, E2 Trauerkarte "Ballon", E3 Startseite zu Ratgebern |
| Johni Jaya Motor | 30 | 7 | 23 | DRAFT, approver set. Not yet reviewed. | E1 Öffnungszeiten, E2 Buchungsformular (Spam), E3 abgelaufene Angebote |
| **Total** | **211** | **49** | **162** | 5 clients done, 4 waiting | |

Dropped for a common reason (details in each `queue.md`): already done, already decided by Martin or the client, not provable today, or merged into a kept card.

## 2. Next up for review
1. **Kamil Böyük**: E1 flags a compromised site (physiotherapiekraft.de), separate from the card itself.
2. **Rabenmütter Shop** and **Johni Jaya Motor**: straightforward content and structure cards, no legal risk.

Dumann is now done (27/27 released, across two sessions). The remaining three still-draft clients have an approver set, so release works as soon as Martin reviews each card.

**Important for any future session working this bulk run: before grilling a client, always re-check the live database state first.** On 14 Oct, Dumann's card count had grown from 7 to 27 and 13 were already released by another session, without this chat's knowledge. Re-querying `approval_items` by `status` before starting a round avoided a duplicate release and caught the real backlog.

## 3. Status of fixes (updated through the grill rounds)
| # | Item | Client | Status |
| --- | --- | --- | --- |
| 1 | Approver set | Hüwel, Dumann, Kamil, Maria, Rabenmütter, Johni, Stürzl (new login), Suriya, Bali | Done for all 9 clients. |
| 2 | Hüwel E1 wording check | Hüwel | Done — hwg_checked true, E1 released in the main chat. |
| 3 | Stürzl E3 recommendation | Stürzl | Done — set to B, released. |
| 4 | Maria health_client flag | Maria | Done — set to false (she only offers room consulting). |
| 5 | Dumann E3 hours recommendation | Dumann | Superseded — the other session's E3 ("Öffnungszeiten: überall dieselbe Version") was already released before my fix landed; my fix was a no-op. Dumann is fully released now (27/27). |
| 6 | Suriya hwg_checked on E2/E4 | Suriya | Done — all six cards (E1-E4, E6, E7) now hwg_checked true and released. |
| 7 | Bali B10 vs B8 overlap | Bali | B8 deleted (Martin: pages must be indexed, not a client question — see section 7 fix task). B10 stays open as is. |
| 8 | Bali health_client flag | Bali | Already false. No action needed. |

### Released so far
- **Stürzl**: E1-E6 (6/6) — done.
- **Suriya**: E1-E4, E6, E7 (6/6) — done.
- **Maria Brasse**: E2-E7 (6/7, E1 taken out) — done.
- **Hüwel**: E1, E2, E3, E5, E6, E7, E8 (7/7, E4 dropped) — done in the main chat.
- **Bali Healing**: B9 (1/2 new drafts, B8 taken out), B10 open from earlier — done.
- **Dumann**: E1-E27 (27/27), spanning two sessions on 13 and 14 Oct — done.

### Still draft, not yet reviewed
- **Kamil**: E1-E4 (4).
- **Rabenmütter**: E1-E7 (7).
- **Johni Jaya Motor**: E1-E7 (7).

## 4. Runbook: review in the Claude chat
1. Open the chat. Say "Entscheidungskarten Hüwel" (or another client).
2. The chat reads the drafts: `select code, title, why, variants, recommended_key, risk_class from approval_items where client_id = '<id>' and status = 'draft' order by code;`
3. The chat shows the drafts as AskUserQuestion cards. Rules:
   - 4 cards per round. More rounds if needed.
   - The recommended variant comes first and carries "(Recommended)".
   - The option text is what the client sees (variant value plus label).
   - Extra options per card: "Release as is", "Change wording" and "Take out".
   - The chat checks the live site once more before each round (curl). Bali lesson: facts can change within hours.
4. Martin answers. For each card, the chat acts:
   - **Release** (only after Martin's explicit yes for that card; needs the approver, section 3):
     ```sql
     update approval_items set status='open', released_at=now(), remind_at=now()+interval '3 days', due_at=now()+interval '7 days' where id='<item id>' and status='draft';
     insert into approval_decisions (client_id, item_id, item_version, actor_name, kind, action, note)
     values ('<client id>', '<item id>', 1, 'Martin (via Claude)', 'admin', 'released', 'Released from the chat');
     ```
     The actor name is `Martin (via Claude)`. For a German health client the guard trigger needs `hwg_checked = true` first.
   - **HWG check:** set `hwg_checked = true, hwg_checked_at = now(), hwg_checked_by = 'Martin (via Claude)'` only on a German health client's card, and only when Martin says the wording is checked.
   - **Change wording:** update the draft (a draft update creates no new version), show it again.
   - **Take out:** `delete from approval_items where id='<item id>' and status='draft';` The text stays in `drafts.sql`.
5. After a round, the chat writes the result into the client's `queue.md` (released, deleted, changed).
6. Never release in bulk. Never release a card whose facts are older than the last check.

## 5. Dashboard readiness (new dashboard module, feed per client)
Question: can the feed be filled today from Search Console (GSC), GA4, Local Falcon free reads (LF) and the Ads account?
Bali is the only client with a working feed job (`client-dashboard-redesign/portal/feed/`). All other clients need grants first.

| Client | GSC | GA4 | LF free reads | Ads | Fill the feed today? | Gaps and owner |
| --- | --- | --- | --- | --- | --- | --- |
| Bali Healing | yes | yes | yes (limits) | partial (paused, Chrome read only) | **Yes** (job built, 13 Oct run clean) | Save grid points at each scan (agent). Booked jobs: ask Peggy and Pasha (Martin). Texts hard-coded in `dsh.js` go stale each month (Dinakar or agent). |
| Praxis Hüwel | yes (URL prefix, from 6 Oct clean) | no (403) | yes (profile actions, reviews), map ranking old (18 Aug) | none | **Partial** | GA4 viewer for `reporting-bot` (Martin). Maps rescan needs credits and Martin's go. Form storage test (agent). |
| Praxis Suriya | no (403, access removed 12 Oct) | no (not visible) | partial (not connected here; saved scans) | partial (paused, no API token) | **No** | Re-grant only for agreed work, ask Coralie (Martin). GA4 grant (Martin). Form enquiries not counted (Dinakar). |
| Dumann | yes | yes (young, from 30 Sep) | partial (saved scans 1 Oct) | unknown (account seen, status not read) | **Partial** | Define which GA4 event means "enquiry" (agent, Martin confirms). Ads read in Chrome (Martin). No lead path in portal (Dinakar). |
| Kamil Böyük | no (sites not in the list) | yes (both sites, one property, split by host) | no (no place IDs, connector off) | partial (UI numbers, no API) | **Partial** (GA4 and Ads totals only) | Search Console user on both sites (Dinakar, Martin's go for site writes). Place IDs and connector (Martin). Key events are 0. Booked patients: ask Kamil (Martin). |
| Maria Brasse | no (403, not in list) | no (403) | partial (saved scans) | none | **No** | GSC and GA4 grants (Martin). Büro scan needs credits (Martin). Lead capture (Dinakar). |
| Stürzl | no (403) | no (403) | partial (baseline 1 Oct saved, not read live) | none (no account) | **No** | GSC user and GA4 viewer (Martin). Profile actions need the GBP link (Martin and the firm). Form comes with the new start page (Dinakar). |
| Rabenmütter | yes (URL prefix, from 29 Aug) | no (403) | not relevant (online shop) | unknown (tag seen) | **Partial** | GA4 grant (Martin). Shopify `read_orders` for revenue (Martin). Domain property in GSC (Martin). Stale tasks in the portal (Dinakar). |
| Johni Jaya Motor | yes (tiny volume) | partial (property 488665039, no WhatsApp or call events, tag mismatch) | no (connector off) | none | **Partial** (GSC only, very thin) | Submit sitemap (needs Martin's go). Fix GA4 tag and add WhatsApp and call events (Dinakar). Reconnect Local Falcon (Martin). |

Short answer: Bali yes. Hüwel, Dumann, Rabenmütter, Kamil, Johni partial. Suriya, Maria, Stürzl no.
Biggest single fix: add `reporting-bot` to the GA4 properties and to the Search Console of Suriya, Maria, Stürzl, Kamil (owner: Martin). The Local Falcon connector is off in several sessions (owner: Martin).

## 6. Things I could not verify
- Google Business Profile service lists and secondary categories (not public): Suriya, Dumann, Hüwel, Maria, Kamil, Stürzl.
- Whether Stürzl answered the 12 Oct mail (E3 choice) and whether Maria's 15 Oct action still runs.
- Whether Hüwel accepts the word "Magnetfeldtherapie" (E5).
- Acupuncture at Bali Healing: closed. Martin confirmed on 13 Oct that Bali does not offer it. B8 was rewritten without it.
- No Local Falcon scan was run. No paid call was made. No secret was printed.
- The SQL files were run through Supabase `execute_sql`. Pre-existing drafts of Suriya E1-E4 were edited (see `suriya/queue.md`) and E5 was deleted.

## 7. Not cards, but found on the way (for Martin)
- FIX (Bali, urgent): the IV drip and breathwork pages on balihealing.com have a noindex tag (Wix page setting). Martin: they must be indexed. Fix in Wix page SEO settings, then re-submit in Search Console. The /acupuncture page is not a Bali offer and also carries noindex. Owner: Dinakar or Pasha, Martin's go per change.
- physiotherapiekraft.de (Kamil) is compromised: hidden casino links and fake sitemap URLs. Clean it before any budget increase.
- Suriya: wrong live facts (contact hours, "Prof. Gret" typo, Impressum placeholder, review count). List in `suriya/queue.md`.
- Bali: new dashboard text and roadmap v3.1 still show the old B1, B6, B7 topics.
- Rabenmütter: the task "Etsy-Shop" is open although the client declined.
- Maria: `/kaeffchen/` still shows an old line ("Tipselwelt").
