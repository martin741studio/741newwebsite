# Night Shift 2026-09-28 — 6 pages · 5 pass · 1 needs_martin · 0 skipped

## Praxis Suriya
- [ ] freigeben  **GBP · Öffnungszeiten & Termin-Button** (FEEDBACK) — pass
      → feedback/praxis-suriya/5bea6cb2-688d-4c24-b436-1a576e7ade75.md · Top-Fixes: —
- [ ] freigeben  **GBP · Öffnungszeiten, Termin-Button & Barrierefreiheit** (FEEDBACK) — pass
      → feedback/praxis-suriya/61abce05-2b04-49b4-b4ab-420ab4374080.md · Top-Fixes: —
- [ ] freigeben  **NAP / Citations / Domains** (FEEDBACK) — pass
      → feedback/praxis-suriya/d1c58471-eafc-4ef9-8418-1611a2345445.md · Top-Fixes: Domain-Wahl Ingelheim vs. Mainz mit Kunde bestätigen; Femalecare-Domain per Whois prüfen

## Rabenmütter Shop
- [ ] freigeben  **Seitenbaum · Zusätzliche Verkaufskanäle (Etsy)** (FEEDBACK) — pass
      → feedback/rabenmuetter-shop/66478f5c-02a4-4076-b1c3-ad9d211e3533.md · Top-Fixes: —
- [ ] freigeben  **Seitenbaum · Trauerkarten (Pillar) — handschriftliche Karte** (FEEDBACK) — pass
      → feedback/rabenmuetter-shop/801d4d7d-1a22-4d45-a08e-e0b213dff2ec.md · Top-Fixes: Modell A oder B (digitale Handschrift-Schrift vs. echte Handschrift) mit Kundin klären
- [ ] freigeben  **Trauerkarten-Kollektion (Hub)** (CREATE) — needs_martin
      → specs/rabenmuetter-shop/trauerkarten-kollektion-hub.md · Fails: kein JSON-LD (Dim 7 = 0); Dim 2 Themen-Tiefe = 15; Dim 3 GEO-Extrahierbarkeit = 35; Dim 4 E-E-A-T = 20
      Martin: [ ] DataForSEO-Zugriff für den Executor prüfen  [ ] Website-Abruf für rabenmuetter-verlag.de prüfen  [ ] echte Kategorie-, FAQ- und Preis-Daten liefern

## Notes for Martin / dev

1. **Trauerkarten-Kollektion-Hub blocked again.** The Executor had no DataForSEO tool and could
   not fetch rabenmuetter-verlag.de. This is attempt 2 of 2 (rule: never a third attempt). The
   page is marked `needs_martin`. No data was invented.
2. **De-slop tool was unreachable in 3 of 5 Critic runs.** `python3 slopmonster/tools/deslop.py`
   needed an approval that was not available in the sandbox. Each Critic did a manual check
   instead and passed the copy. Please check the Bash tool permissions for `python3` in future
   Critic invocations, so the automated check runs again.
3. **`processed-feedback.json` is still empty.** All 5 FEEDBACK items above already passed
   tonight. Once you tick `[x] freigeben` and apply a reply, add that `feedback_id` to
   `reporting/night-shift/processed-feedback.json`. This stops the same comment from being
   staged again on a future night (it happened on 2026-09-16, 09-18, and 09-22).
4. `state.json` shows `invocations_used: 5`, but the run made at least 13 calls (1 Planner +
   6 Executor + 6 Critic, one page had a retry). The counter is likely not updated by every
   role. This is a tracking bug, not a budget breach — the run stayed inside the 3 h / 23:00
   wall-clock cap either way.
