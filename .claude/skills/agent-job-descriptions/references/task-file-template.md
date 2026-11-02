# Task handoff — written into `00_project/agent-jobs/<agent-id>/inbox/<YYYY-MM-DD>-<client>-<slug>.md`

```
---
agent: webdev
client: suriya
site: https://suriya-praxis.de
page: /leistungen/ayurveda           # the page or "new"
spec: 00_project/assets/suriya/cro/07-prototype/index.html   # or 05-final/page.md
milestone: M2                        # from roadmap.json; the agent refuses tasks outside the active milestone
from: client chat 👥🪷 Coralie / Praxis Suriya   # or "morning grill plan <date>"
deadline: 2026-11-07
done_when: new page built as draft, desktop+mobile screenshots in outbox, QA checklist PASS, swap steps listed; nothing live
---
Notes: <2–5 lines, what matters, what must not change>
```

Rules: one task = one client site = one page or one fix list. No task without `done_when`. The agent moves the file to `outbox/` with its report appended when done or BLOCKED.
