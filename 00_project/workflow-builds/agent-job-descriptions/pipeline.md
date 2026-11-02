# Pipeline — agent-job-descriptions (2.4)

Shape: patterns §4.1 sequential with gates; install step uses §4.4 plan-validate-execute.

```
WRITE mode
[roster.py list] → [card: which agents]  ◄ Martin
   → per agent: [read real prompt/skill/memory/registry] (read-only)
   → [draft block from template, every never-line with rung, tools rated]
   → [validate_jd.py] fix until PASS
   → [show draft + validator output] → [card "Go" per agent] ◄ Martin
   → [place.py: write to agreed rung + roster line + _run.json]   (write, gated)
   → [report: files, roster, what is advisory-only]

REVIEW mode (review day, from the morning grill)
[collect_evidence.py per agent: _run.json, git log, grill ledger, task runs, night REVIEW.md]
   → [draft review: shipped / wrong / needs / stale rule / proposals; grade proposal from evidence]
   → [card per agent: grade A–F + one sentence]  ◄ Martin
   → [card per repeated mistake: rung decision]  ◄ Martin
   → [write review file, update roster.last_grade, apply approved memory/rule/skill fixes]
   → hook edits → separate go-gate turn
```
Checkpoints: card "which agents"; card "Go" per description; card grade per agent; card rung per repeated mistake. Nothing is placed or edited without a card.
