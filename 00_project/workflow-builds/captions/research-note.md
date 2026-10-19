# 1.5 Research note: Captions for video (2026-10-19)

1. Block chosen: **Skill** in `.claude/skills/captions/` with `disable-model-invocation: true`. Reason (patterns.md section 3, item 3): one repeatable procedure Martin triggers by hand, with a side effect (a Drive copy). Not a routine: the dump is ready at a different time each day and Martin triggers it. Not a hook. Not a project.
2. Rule R1.7: intake, validation and the slop check are scripts. Beat extraction, story order and caption writing are heuristics with examples.
3. Rule R2.8: the output format is fixed. The skill gives one exact template for `captions.md` and says "ALWAYS use this exact template".
4. Rule R2.9: style needs 2 to 3 input/output example pairs (dump line to caption block). They come from the hand run (step 2.3).
5. Pattern 4.1 (sequential with gates) plus 4.3 (draft, validate, fix, re-check). One checkpoint: Martin sees the captions before the Drive copy.
6. Library: no existing workflow for subtitles or vlog captions (1.2). The prompting doc for Fable 5.1 covers writing style. Its advice: give the voice and the format as examples, not as adjectives.
7. Existing assets reused: Google Drive MCP for read and write, slopmonster for the English slop gate, `_run.json` telemetry pattern, registry script.
8. Facts source: the dump is the only source. The validator checks every number in the captions against the dump. Words like places and names are checked by Claude against the beats list, then by Martin at the checkpoint.
9. Format decided in the grill: English, "we" voice, max 12 words per block, max 2 lines per block, run folder `00_project/assets/youtube-captions/<YYYY-MM-DD>/`, Drive folder "Captions Celine Martin" (Drive id 1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm).
10. Hard limits: never upload or publish to YouTube. Never add a fact. Never edit the Drive dump.
11. Open question 1: how many blocks per video? Depends on video length. Default: 20 to 45 blocks. The hand run sets the real number.
12. Open question 2: does the dump name the day or the location? If not, the captions do not name them. No guessing.
13. Open question 3: Drive folder "Captions Celine Martin" (Drive id 1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm) does not exist yet. The first run creates it with the Drive MCP, or Martin gives the folder link.
