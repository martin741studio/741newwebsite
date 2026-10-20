# Night Shift — Execution Blueprint (Page Specs + Audits)

Decisions (2026-09-15): first job = page specs + audits · budget = Mittel · morning review =
Markdown in repo. Skill: `.claude/skills/night-shift/SKILL.md`. Runner: `reporting/night-shift.sh`.

## 1. Trigger

Same pattern as the working Standup job (`studio.741.standup.plist` → bash script).
- LaunchAgent `studio.741.night-shift` runs **Mon–Fri 01:30** → `reporting/night-shift.sh`.
- Plist lives in `reporting/launchagents/studio.741.night-shift.plist` (not installed by default).
- Install: copy to `~/Library/LaunchAgents/` and `launchctl load` it. Uninstall: `launchctl unload`.
- Laptop must be awake (same constraint as the Standup job). Move to the Dev-VPS later.

## 1b. Auto-sleep after the window

A second, independent LaunchAgent `studio.741.night-shift-sleep` fires **Mon–Fri 23:02** →
`pmset sleepnow`. Deliberately decoupled from the night-shift script itself (not chained at
its end) so a manual daytime test run (`NIGHT_ALLOW_ANYTIME=1`) never puts the laptop to sleep.
The night-shift run always hard-stops by 23:00 (see §1), so by 23:02 it is done either way.

## 2. Run shape (Ralph / fresh-context pattern)

```
night-shift.sh
  ├─ 0. mkdir reporting/night-shift/<DATE>/ ; write state.json (empty)
  ├─ 1. claude -p  PLANNER   → plan.json                      (1 invocation)
  ├─ 2. for each plan item (≤6):
  │      claude -p EXECUTOR  → specs|audits/<client>/<slug>.md (1 invocation)
  │      claude -p CRITIC    → critic/<client>/<slug>.json     (1 invocation)
  │      if fail && attempts<2: repeat EXECUTOR+CRITIC once
  │      write state.json
  ├─ 3. claude -p  REVIEWER  → REVIEW.md, append LOG.md       (1 invocation)
  └─ 4. exit; LaunchAgent stdout/stderr → reporting/night-shift/night-shift.log
```
Each `claude -p` call gets **only** `state.json` + its one task. No transcript is reused.
That keeps every context small and kills context drift and re-billing of giant histories.

## 3. State tracking

- `state.json` — machine state, rewritten after every step (schema in SKILL.md).
- `plan.json` — the night's queue.
- `specs/`, `audits/`, `critic/` — one file per page.
- `REVIEW.md` — the human dashboard for the morning.
- `LOG.md` — one line per night, appended forever: date · pages planned/pass/needs_martin · stop reason.

## 4. Verification loop (Critic)

Pass = all six checks green (no placeholders in critical fields, NAP exact match, JSON-LD
valid + matching, language correct, HWG scan clean, all rubric dimensions ≥ 80).
Fail → one retry with the fail list. Second fail → `needs_martin`. No third attempt.
The Critic is a separate invocation from the Executor. The writer never grades itself.

## 5. Morning review (5–10 min)

Open `reporting/night-shift/<DATE>/REVIEW.md`:

```
# Night Shift 2026-09-15 — 5 pages · 3 pass · 1 needs_martin · 1 skipped

## Praxis Hüwel
- [ ] freigeben  **Startseite** (CREATE) — pass · 84/88/91/82/95/90/88/86
      → specs/huewel/startseite.md · Top-Fixes: —
- [ ] freigeben  **Akupunktur Nürnberg** (AUDIT) — needs_martin
      → audits/huewel/akupunktur.md · Fails: NAP-Telefon weicht ab; Dim 4 = 72
      Martin: [ ] NAP prüfen  [ ] Behandler-Credentials nachreichen
## Praxis Suriya
- [ ] freigeben  **Osteopathie** (CREATE) — pass · …
- skipped **Kinderosteopathie** — no_data (DataForSEO 0; sense-check via Autocomplete nötig)
```
Tick `[x] freigeben` → the daytime flow publishes that spec to the client's portal page node
(memory `client-textdraft-delivery`), one go per page. Untouched lines stay drafts.

## 6. Budget (Mittel) — what it costs, roughly

Per night ≤ 14 Sonnet-5 invocations × ≤ 40 turns, each with a small context. That is a
fraction of one daytime giant-session turn. If the morning shows two nights of `needs_martin`
on the same page, the page needs data from Martin, not more retries — the breaker did its job.

## 7. Not in v1 (deliberately)

- Ranking/NAP monitoring loop (next job after this one runs clean for a week).
- Any write to Supabase or a CMS.
- Telegram summary (can be added: one curl at the end of the runner).
