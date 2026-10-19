# Decisions: Captions for video

## 2026-10-19 Checkpoint 1 (design)
- Martin: "Go (Recommended)" on the AskUserQuestion card "Checkpoint 1: do you give the go on this design?".
- Design approved: Skill `.claude/skills/captions/`, 7-step pipeline, one checkpoint before the Drive copy, English "we" captions, max 12 words, max 2 lines, max 42 characters per line, Drive folder "Captions Celine Martin".
- Note: hand run used a sample dump. The real dump comes at the functional test.

## 2026-10-19 Checkpoint 2 (ship)
- Martin: "Go (Recommended)" on the AskUserQuestion card "Checkpoint 2: do you give the go to ship the captions skill?".
- Shown: cp2 gate output (GATE PASSED), scorecard 98.3 % with 0 blocking zeros, trigger tests 4/4, functional test (24 blocks, PASS, 5/5), baseline, and the functional-test captions as the real output.
- Open: the first run on a real dump. The Drive folder was empty on 2026-10-19.
