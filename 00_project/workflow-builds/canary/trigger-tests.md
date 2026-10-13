# 4.1 Trigger tests — canary (fresh sessions, 2026-10-14)

First run (disable-model-invocation: true): T1/T2 FAIL — the Skill tool refused invocation outright ("cannot be used with Skill tool due to disable-model-invocation... Ask the user to run /canary themselves"). T3/T4 passed by description text. Finding, independently confirmed by the trigger-test agent AND the functional-test agent (which stalled at the very first step): the natural-language triggers listed in the description could never fire, which contradicts the skill's own stated design and these test scenarios.

Fix: `disable-model-invocation` false→... wait, true→false in SKILL.md frontmatter (matches house convention: night-shift-v2 also has side effects and is `false`; internal gates — Critical, allowlist.py, Martin's go-cards — protect against unwanted writes regardless of how the skill is triggered). Added one Critical line explaining why auto-trigger is safe here.

Re-run after fix, fresh session:
- T1 "Set up a canary for Marcel's Gewinnspiel funnel." → PASS, Skill tool invocation succeeded.
- T2 (German paraphrase, no word "canary") "Pass auf, dass das Kontaktformular von Bali Healing nicht wieder still ausfällt, und sag mir sofort Bescheid, wenn keine Anfragen mehr reinkommen." → PASS, Skill tool invocation succeeded.
- T3 "Baue für Marcel die Zapier-Automation für sein neues Webinar…" → PASS, correctly does not trigger (hits the "Do NOT use to build the automation itself" exclusion).
- T4 "Wie lief Google Ads bei Bali Healing diese Woche?…" → PASS, correctly does not trigger (hits the "performance/reporting questions with no outage" exclusion, description names this almost verbatim).

**4/4 passed.** Also confirmed: this session's own available-skills list picked up "canary" immediately after the fix, with the full description.
