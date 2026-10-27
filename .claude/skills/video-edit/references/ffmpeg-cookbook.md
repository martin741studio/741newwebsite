# ffmpeg cookbook — video-edit

Tested working on this Mac's ffmpeg 8.0.1 (2026-10-27). Full research with every source: `00_project/knowledge/video-editing-library/sources/001-tooling-stack-research.md`.

## 9:16 pad (16:9 source → vertical, blurred background)

```bash
ffmpeg -i wide.mp4 -filter_complex \
  "[0:v]split[a][b];\
   [a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=luma_radius=30:luma_power=2[bg];\
   [b]scale=1080:1920:force_original_aspect_ratio=decrease[fg];\
   [bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1[v]" \
  -map "[v]" -map 0:a -c:v libx264 -c:a aac out.mp4
```

## Loudness (two-pass loudnorm, target -14 LUFS / -1 dBTP, R-EXPORT.3)

Pass 1 — measure (TP=-1 here is fine, this pass only measures):
```bash
ffmpeg -hide_banner -i in.mp4 -af loudnorm=I=-14:LRA=11:TP=-1:print_format=json -f null -
```
Read `input_i`, `input_tp`, `input_lra`, `input_thresh` from the printed JSON. Pass 2 — apply, **TP=-1.5** (not -1):
```bash
ffmpeg -i in.mp4 -af "loudnorm=I=-14:LRA=11:TP=-1.5:measured_I=<input_i>:measured_LRA=<input_lra>:measured_TP=<input_tp>:measured_thresh=<input_thresh>:offset=0:linear=true" -ar 48000 -c:v copy -c:a aac -b:a 192k -shortest out.mp4
```
Two things found running this for real (2026-10-27, functional test):
- Asking pass 2 for TP=-1 overshoots to roughly -0.87 dBTP after encoding — the real ceiling needs headroom. Ask for **TP=-1.5** to land at or below the -1 dBTP target.
- loudnorm's output audio can end up a touch longer than the video. Always add **`-shortest`** on the final export so picture and sound end together.

## Speed ramp (constant)

```bash
ffmpeg -i in.mp4 -filter_complex "[0:v]setpts=PTS/1.25[v];[0:a]atempo=1.25[a]" -map "[v]" -map "[a]" -c:v libx264 -c:a aac out.mp4
```
`atempo` range is 0.5-2 per instance; chain two for a bigger change (e.g. 1.25 then 1.25 again for ~1.56x).

## Crossfade between two clips (same resolution/fps/pixel format required)

```bash
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
  "[0:v][1:v]xfade=transition=fade:duration=0.5:offset=<A_len_minus_0.5>[v];\
   [0:a][1:a]acrossfade=d=0.5:c1=tri:c2=tri[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -c:a aac out.mp4
```
`transition=` options (ffmpeg doc): fade, wipeleft/right/up/down, slideleft/right/up/down, circlecrop, dissolve, pixelize, radial, smoothleft/right/up/down, zoomin, and more — see ffmpeg.org/ffmpeg-filters.html#xfade.

## Zoom-pan (punch-in / pattern interrupt)

```bash
ffmpeg -i in.mp4 -vf "zoompan=z='min(zoom+0.0015,1.3)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30" out.mp4
```

## Export (H.264, platform-safe)

```bash
ffmpeg -i in.mp4 -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart out.mp4
```

## What NOT to use on this Mac (confirmed missing, R-TOOL.2)

- `-vf subtitles=file.ass` / `-vf ass=file.ass` — needs libass, not linked in this ffmpeg build.
- `-vf drawtext=...` — needs libfreetype, also not linked.
- Captions go through `caption_render.py` (Pillow PNG overlay) instead — see SKILL.md step 6.
