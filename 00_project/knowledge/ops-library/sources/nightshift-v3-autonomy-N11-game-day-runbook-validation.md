# N11 — "Validate On-Call Runbooks with a 3 A.M. Game Day"

- Org/author: OneUptime (vendor blog, technical review dated same day as publish)
- Type: article / practitioner guide
- Publish date: **2026-08-06** (shown on page as "Aug 06, 2026")
- URL: https://oneuptime.com/blog/post/2026-08-06-on-call-runbook-game-day-validation/view
- Fetch date: 2026-10-15

## Extract (own words)

- Core argument: a runbook that only looks complete on paper is not validated — validation requires actually running the drill with realistic alert delivery, current access credentials, production-like evidence, and a bounded failure injected into a real (or production-equivalent) environment.
- The central, most transferable rule: **verify recovery at the user/outcome level, not at the orchestrator's status level.** Quoted directly: "A deployment rollback completing successfully does not prove checkout recovered." The equivalent for 741: systemd reporting a unit as "active" does not prove the agent process is actually doing useful work.
- Procedure: pick one failure mode the runbook claims to handle; define the environment and blast-radius boundary and abort condition *before* starting; inject the bounded failure; measure specific things — decision latency, missing information, unsafe ambiguity, tool failure, and dependence on undocumented/tribal knowledge — explicitly **not** typing speed or how fast the response "looked."
- Explicitly rejects a single pass/fail score in favour of three outcomes: pass, pass-with-finding, fail — because a fast, confident-looking response can still have taken an unsafe or wrong action; a single score would hide that.
- A run counts as a fail if the responder needed undocumented privileged access, applied a fix to the wrong scope, could not separate cause from impact, could not verify recovery, or reached an obsolete contact.
- After the drill: for every deviation from the runbook, decide explicitly whether to fix the runbook, fix access/tooling, or add missing telemetry — assign an owner and a due date, and re-run the specific affected path after a material fix (not the whole drill).
- States directly that a review/revalidation date alone does not keep a runbook current — it must be re-validated after any architecture, permission, or alerting change, not just on a calendar.

## IF/THEN rules for 741

1. IF decisions.md's "actually rebooted the server, not just trusted the config" test (N43–N47, done 2026-10-14) is treated as sufficient proof the stack is reboot-proof, THEN re-run that exact framing with this source's correction: confirming the 6 systemd units came back "active" within ~25s is orchestrator-level verification, not outcome-level — the real test is whether the browser/CDP/Remote-Control stack can actually complete one real task end-to-end right after that reboot, not just whether the ports are listening.
2. IF 741 schedules a recurring drill for 741-agents-01 (recommended, since this was done once as a one-off), THEN define the failure mode, blast radius and abort condition in writing before each drill (kill one specific service, not "see what happens"), and re-run it after any change to systemd units, permissions, or the Tailscale/firewall setup — not on a fixed calendar alone.
3. IF Martin or an agent evaluates "was last night's run OK," THEN apply the three-way rating (pass / pass-with-finding / fail) instead of a binary — a run that technically completed but needed an undocumented manual fix, or that used an access path nobody wrote down, is a "pass with finding" that should generate a follow-up, not a silent pass.
4. IF a drill or an incident reveals a deviation (wrong scope, missing access, missing telemetry), THEN assign an explicit owner and due date for the fix and re-test only that path afterward — don't close it as "noted" without a scheduled re-check.

## Caveats

- Written for on-call incident-response runbooks in a team context (the article assumes "a cold responder" reading someone else's runbook), not specifically for a solo-operator's unattended server — the adaptation to 741's single-operator, mostly-autonomous setup above is this research's own translation, not the article's own framing.
- Vendor blog (OneUptime sells observability tooling); the guidance itself is methodology, not a product pitch, but noted for balance.
