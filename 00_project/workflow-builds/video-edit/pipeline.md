# Pipeline — video-edit

```
[ Martin gives: raw footage/script + reference(s) + message + platform ]
                         │
                         ▼
   1. RUN FOLDER  00_project/assets/<client-or-741>/video-edit/<date>-<slug>/
      raw/ (Martin's footage, copied in, never overwritten)
      reference/ (profile of the reference, reused if already profiled)
                         │
                         ▼
   2. REFERENCE PROFILE  scripts/reference_profile.py
      (skip if this exact reference is already in the knowledge base)
      → reference_profile.json, contact_sheet.jpg, transcript.json, summary.md
                         │
                         ▼
   3. TRANSCRIBE RAW FOOTAGE  mlx_whisper CLI, word-level timestamps
      → transcript/words.json
                         │
                         ▼
   4. EDIT PLAN (qualitative — Claude reads the transcript + reference profile)
      Draft kept spans: cut filler/dead air/false starts, best take of a
      repeated line. Pick hook line, caption line groups, pacing target
      from the reference's shot-length stats.
      scripts/build_cut_plan.py → cuts.json (padded, frame-snapped, validated)
                         │
                         ▼
   ◆ CHECKPOINT 1 — show the cut plan (spans + reasons). Wait for go/changes.
                         │ go
                         ▼
   5. ROUGH CUT  scripts/render_cut.py → rough_cut.mp4
      (verified: output duration matches the plan, frame-accurate concat,
      -fps_mode passthrough never -r)
                         │
                         ▼
   6. CAPTIONS + LOOK
      scripts/caption_render.py (word-highlight PNG overlay burn-in)
      + 9:16 crop/blur-pad if source is 16:9 and target is vertical
      + loudnorm two-pass
                         │
                         ▼
   7. EXPORT  export/<slug>_9x16.mp4 (and _16x9.mp4 if both requested)
      per R-EXPORT rules (resolution/codec/bitrate/loudness)
                         │
                         ▼
   ◆ CHECKPOINT 2 — show the export + why-these-choices.md (incl. the
     "what this run did not do" disclosure). Wait for go/notes.
                         │ notes
                         └──► back to step 4 (new edit plan) or step 6 (look/caption only)
```

## Run-folder convention

`00_project/assets/<client-or-741>/video-edit/<YYYY-MM-DD>-<slug>/` — mirrors the `captions` and `content-format-board` run-folder pattern. `<client-or-741>` is `741` for Martin's own videos, or the client slug for client work (later extension — v1 ships for 741's own videos per the brief).

## Checkpoints (Martin's go, both mandatory, no skip)

1. **Edit plan go** — before any rendering. This is the expensive-to-undo step (padding/overlap logic, hook choice).
2. **Export go** — before Martin is told the job is "done." The export is the thing he reviews in CapCut.
