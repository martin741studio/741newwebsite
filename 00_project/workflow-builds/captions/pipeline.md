# 2.4 Pipeline: Captions for video

Shape: patterns.md 4.1 (sequential with gates) + 4.3 (draft, validate, fix, re-check).

```
Martin: /captions <drive link | pasted text>
   │
   ▼
[1 Intake]  script  scripts/intake.py --date <d> --source <file|->   
   • Drive link: Claude reads the doc with the Drive MCP, writes the text to a temp file.
   • Pasted text: Claude writes the text to a temp file.
   • Script: makes 00_project/assets/youtube-captions/<date>/, saves dump.md, keeps an older captions.md as captions-v<n>.md, writes _run.json (status "in Arbeit").
   │
   ▼
[2 Beats]   heuristic  Claude writes beats.md: one line per fact in the dump (number, place, name, plan, feeling), quoted from the dump. The dump is the only source.
   │
   ▼
[3 Story]   heuristic  Claude orders the beats: hook (1 to 2 blocks), the day in order, one insight, one close. references/story-rules.md.
   │
   ▼
[4 Draft]   heuristic + template  Claude writes captions.md with the exact template (assets/captions-template.md). English, "we" voice, max 12 words, max 2 lines per block. 2 to 3 example pairs in references/examples.md.
   │
   ▼
[5 Validate]  script  scripts/validate_captions.py captions.md --dump dump.md
   • max 12 words, max 2 lines per block, numbered blocks, no dashes, no HTML, every number in the dump, no German stop words, block count 12 to 60.
   • Loop: fix, re-run, until PASS.
   │
   ▼
[6 Slop]  script  python3 .claude/skills/slopmonster/tools/deslop.py --text "<captions>" must give 5/5. Below 5/5: rewrite, cleanse.sh, lint again. Max 2 rounds.
   │
   ▼
🛑 [CHECKPOINT: Martin]  show captions.md in one text block + the validator output. Card: "go" / "change". Changes go back to step 4.
   │
   ▼
[7 Deliver]  Drive MCP create_file: captions.md as a Google Doc "<date> captions" in the folder "Captions Celine Martin" (Drive id 1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm). _run.json status "fertig", result = Drive link. Reply: local path + Drive link.
```

No step uploads to YouTube. No step edits the Drive dump.
