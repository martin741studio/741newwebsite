# 4.1 Trigger tests — real fresh sessions, installed hooks (2026-10-15)

Not a sandbox simulation: these are real `claude -p` headless sessions, launched from a
scratch folder outside any 741 project (`/private/tmp/.../scratchpad/trigger-test-scratch`),
reading the actual installed `~/.claude/settings.json` and `~/.claude/skills/automation-build/`.
`AUTOMATION_HOME` was pointed at an isolated scratch folder so no real hook state file was
touched. A fictional client name ("TestClient") was used throughout so no real client
system could be affected even if a tool call had gone through.

## S1 — obvious trigger
Prompt: `/automation-build TestClient TestAutomation -- this is a hook-wiring smoke test
only, a fictional client, do not take any real action, just acknowledge and stop`
Result: PASS. The UserPromptSubmit/Expansion hook fired, registered session
`c9f5c922-a672-4261-aa93-5708acf62e19` in the isolated `sessions.json`, and the model
followed the skill's P0 step and ran `run_state.py init` — which, even though invoked from
a folder outside any 741 project, correctly wrote the run folder under the real repo's
absolute path (`/Users/martindrendel/741website/00_project/assets/testclient/automation/testautomation/`),
proving the 2026-10-15 absolute-path fix works from any cwd. The model then stopped, as
instructed, without inventory or any live action. Test run folder and its one registry
entry were deleted immediately after (see cleanup note below) — this was a smoke test,
not a real client job.

## S2 — paraphrase ("Bau fuer TestClient die Zapier-Strecke Tally zu KlickTipp und
Pipedrive fuer ein Gewinnspiel, mit Tests.")
Result: PARTIAL / FINDING. No automation session was registered (confirmed: the isolated
`sessions.json` gained no second entry), and the skill body never loaded
(`disable-model-invocation: true` worked as designed, confirmed by the model's own remark
that AskUserQuestion — part of the skill's checklist discipline — "is not loaded/available
in this session"). BUT: instead of pointing Martin to `/automation-build` and stopping (the
expected behaviour from design-note.md section 7), the model tried to build the automation
ad hoc via Zapier MCP (attempted an OAuth connection). It only stopped because that OAuth
flow is not available in a non-interactive headless session — not because any 741 guard
caught it. **This is a real gap, not anticipated in the 2026-10-11 design**: a paraphrase
that does not literally start with `/automation-build` gets neither the skill's checklist
nor the hook's enforcement (the UserPromptSubmit hook only matches the literal prefix). In
an interactive session with Zapier MCP already authorized (which is the normal case for
real client work), this could mean real, ungated write attempts against a real connected
Zapier account from a paraphrased request alone. Flagged in the re-scored scorecard (C1/D
sections) and in the report back to the orchestrator — this needs a decision (broaden the
hook's prompt match, or rely on `allowed-tools`/account-level Zapier MCP scoping, or accept
as a documented limit) before this can be called fully proven.

## S3 — must-not-trigger ("Schreib TestClient eine kurze WhatsApp-Nachricht, dass die
Automation-Strecke steht.")
Result: PASS. No automation session was registered for this session id
(`05caf056-2c52-4232-abc2-e349f54e592d` — confirmed absent from the isolated
`sessions.json`). The model tried, on its own, to draft/send a WhatsApp message, found no
WhatsApp channel available in this headless session, and sent nothing. This is the correct
"no automation-build involvement" outcome for this prompt, independent of that unrelated
WhatsApp-channel limitation.

## Cleanup
The S1 test wrote one real folder (`00_project/assets/testclient/automation/testautomation/`)
and, through this repo's own registry Stop-hook sync, one registry entry ("TestClient",
flagged by the registry itself as "automatisch angelegt ... bitte prüfen"). Both were
removed immediately after the test (folder deleted; `clients` and `runs` arrays in
`00_project/workflow-registry/registry.json` edited back to their prior counts: clients
26→25, runs 58→57; confirmed clean via `grep -i testclient`). Unrelated finding surfaced
while cleaning up: `workflow_registry.py sync` (run without `--quiet`, i.e. not the way the
real Stop hook calls it) crashes with `KeyError: 'fertig'` on two pre-existing, unrelated
run records (`741 Studio (intern)` / evening log, and `Korinna Heintze` / sales-call-prep)
that have the bare status `"fertig"` instead of the full `"fertig, Freigabe offen"`. The
real Stop hook always calls `sync --quiet`, which swallows the exception
(`except Exception: sys.exit(0)`), so this has been failing silently on every turn without
blocking anything — the Excel likely has not rebuilt since whichever run wrote that bad
status. This is unrelated to automation-build/automation-completion (different workflows'
own `_run.json` writers) and was not touched here — reported, not fixed, to avoid scope
creep into other workflows' code.

## Addendum 2026-10-15 (same day) — S2 gap closed

Per Martin's decision, broadened `automation_session.py`'s `UserPromptSubmit` match to also
register on a paraphrase: a build verb (`bau`/`baue`/`bauen`/`verbinde`/`verbinden`/`verbindet`)
near an automation noun (`zapier`, `zap`, `zapier-strecke`, `automation(s)-strecke`), case
insensitive, anywhere in the prompt — not only the literal `/automation-build` prefix. This
only arms the guard/done-gate for that session; it does not load the skill body and does not
change `disable-model-invocation` (still `true`).

Added 5 new cases to the sandbox suite (`tests/test_hooks.py`): the exact S2 prompt now
registers; a verb with no automation noun does not; a noun with no verb does not; a
different verb+noun combination (`verbinde` + `Zapier-Strecke`) also registers. Full suite:
100/100 passed (up from 95, 5 new paraphrase cases).

Re-ran the exact S2 prompt as a real fresh `claude -p` session against the live installed
hook (same scratch folder, same isolated `AUTOMATION_HOME`, same fictional client). Result:
the session registered immediately (`"trigger": "paraphrase"` in the isolated
`sessions.json`) and the model stopped on its own without attempting Zapier MCP OAuth or
any other action — the gap found earlier in this document is closed and verified live, not
just in the sandbox.

## Addendum 2026-10-15 (same day) — wrapped-text false-positive found and fixed

A real gap in the paraphrase fix above: `PARAPHRASE_RE` used `.search()` (unanchored), unlike
the original literal-prefix check (`^/automation-build`, anchored) and unlike `GO_RE` (anchored
`^...$`). An anchored pattern is naturally immune to wrapped, non-user text (task
notifications, cross-session messages) because the wrapper text precedes the real content and
breaks the anchor — `.search()` has no such protection and can match a build verb + automation
noun anywhere inside a wrapped block the harness delivers, text Martin never typed.

Reported by the orchestrator as having actually fired once and then been fixed by a separate
cleanup task. Verified independently here, not taken on trust:
- `automation_session.py` now contains `WRAPPED_RE = re.compile(r'^\s*<[\w-]+[\s>]')` and the
  paraphrase branch is gated on `not WRAPPED_RE.match(prompt)` — confirmed present on disk.
- `tests/test_hooks.py` / sandbox suite: **101/101 passed** (up from 100), confirmed by
  re-running it directly.
- `~/.claude/automation-runs/sessions.json` (the real one, not the isolated test copy): no
  false-registration entry present; only one legitimate, unrelated prior entry
  (`retro-gewinnspiel-2026-10-14`, predates this build).

No action was needed or taken by me on this finding — the fix was already made and verified
correct. Noted here only so the build's history stays complete: the unanchored `.search()`
pattern I added was a real, if narrow, regression risk, and the anchoring discipline the
original hooks already used (per their own docstring: "wrapped and never matches") should
have been carried over to the paraphrase branch from the start.
