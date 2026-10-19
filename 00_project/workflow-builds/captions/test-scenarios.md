# 2.2 Test scenarios (written before the body, 2026-10-19)

## Scenario 1: obvious trigger
Input: `/captions https://docs.google.com/document/d/1AbC/edit`
Expected: the skill loads. It reads the doc, creates `00_project/assets/youtube-captions/<today>/`, writes `dump.md`, `beats.md`, `captions.md`, runs the validator to PASS and the slop lint to 5/5, shows the captions, waits for "go" before the Drive copy.

## Scenario 2: paraphrased trigger
Input: "Here is our dump for today's video, make the caption text for it: <pasted text>"
Expected: the skill loads (phrases "dump", "today's video", "caption text"). Same run as scenario 1, with the pasted text as the source and no Drive read.

## Scenario 3: must NOT trigger
Input: "Fix the German subtitles on the Hüwel video kElKa09l804, Hübel must be Hüwel."
Expected: the skill must NOT trigger. This is a YouTube Studio subtitle edit on a client video, not a caption text for the daily vlog. The description names this as a negative trigger ("Do NOT use for YouTube subtitle files, SRT files, client videos or uploads").

## Scenario 4 (functional, from the hand run): facts
Input: a dump with the line "Rent here is 450 a month, we pay 8 million rupiah for the villa."
Expected: the captions may say "Rent: 450 a month." They may not say "Rent: 500 a month" or add "for a 2-bedroom villa" if the dump does not say it. The validator fails on any number that is not in the dump.
