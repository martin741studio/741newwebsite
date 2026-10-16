# Reviewer prompt (fresh agent at Checkpoint 2, optional)

Why: the agent that built the prototype is biased towards its own work (rules R4.5, R5.2). A fresh agent with no build history checks the result against the files. It reports only gaps that change correctness. It must not write or edit any file.

Use: start a fresh subagent (`Agent`, type general-purpose) and paste the block below. Replace the `<…>` values. Read the report, then fix the real gaps yourself and run `verify.py` again.

```
You review a finished website prototype for correctness. Do not edit or create any file. Do not suggest redesigns or style changes.

Run folder: <path to 00_project/assets/<slug>/cro/>   Prototype: <07-prototype/index.html>
Industry rule set: <HWG for health | Anwaltswerbe-Check for law firms | claims need real data for others>

Read these files first: 04-copy/approved-copy.md, 02-data/dataset.md, 03-diagnosis/diagnosis.md, 07-prototype/index.html, 07-prototype/self-check.md, 07-prototype/visual-check.md, 06-gpt-assets/images/SLOTS.md, 08-handoff/handoff.md, and the scorecard 00_project/knowledge/cro-library/_derived/scorecard.md.

Report ONLY gaps of these kinds:
1. A fact, number, price, credential or claim on the page that is not in dataset.md or approved-copy.md, or that differs from them.
2. A legal-rule breach for the industry rule set above (healing promise, result promise, title not proven, superlative, price claim).
3. A scorecard score in self-check.md that the page does not earn (open the HTML and check). Name the item and the evidence.
4. A [FEHLT] item that the page hides, or a [FEHLT] item missing from the handoff.
5. A broken link target, a missing anchor, an image slot without a file, or a section of the plan that the page lacks.
6. A statement in visual-check.md that the HTML contradicts.

For every gap give: file and line or quote, what is wrong, the evidence, and the smallest fix. If you find no gap of these kinds, say "No correctness gaps found" and list what you checked. Maximum 15 gaps, most serious first.
```
