# 4.1 Trigger tests (fresh sessions, 2026-10-19)

Four fresh subagent sessions (Sonnet), each with one user message and the instruction to invoke a skill only if one fits and to stop after it loads.

| # | Message | Expected | Result |
|---|---|---|---|
| T1 | `/captions https://docs.google.com/document/d/1AbC.../edit` | triggers | PASS. Chose `captions`, Skill tool call succeeded. Deciding phrase: `Use when Martin says "/captions <link or text>"`. |
| T2 | "Here is our dump for today's video, make the caption text for it: <4 German lines>" | triggers | PASS. Chose `captions`, Skill tool returned "Launching skill: captions". Deciding phrase: "here is our dump for today's video". |
| T3 | "Fix the German subtitles on the Hüwel video kElKa09l804 in YouTube Studio, 'Hübel' must be 'Hüwel'." | must NOT trigger | PASS. No skill. Rejected `captions` on "Do NOT use for ... subtitles on a client video (Hüwel, Suriya or any 741 client)". |
| T4 | "Make a 9-slide Instagram carousel for 741 about local SEO for dentists, captions for each slide included." | must NOT trigger | PASS. No skill. Rejected `captions` on "Do NOT use for ... social posts and carousels (social-visuals)". |

4/4 passed on the first run. No change to the description needed. `disable-model-invocation` is off, so the natural trigger in T2 fired (the canary build showed that with it on, natural triggers never fire).
