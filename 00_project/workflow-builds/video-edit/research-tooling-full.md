# Video Editing Tooling for Claude Code on macOS (Apple Silicon)

Research date: 2026-10-27. Scope: short-form (9:16) and long-form (16:9) video for an agency.

Local check on this Mac: `ffmpeg version 8.0.1`. The build has `--enable-libx264`, `--enable-libx265`, and `--enable-videotoolbox`. It does NOT have `--enable-libass`. The `subtitles` and `ass` filters therefore do not run here.

Test evidence: `/private/tmp/claude-501/-Users-martindrendel-741website/77484ef0-c132-40f8-92d3-78474f37f405/scratchpad/test/run_tests.sh`. The script runs each example on synthetic clips in the scratchpad. Nothing was installed.

Date rule: "undated, fetched 2026-10-27" means the page showed no publish date.

---

## Key findings

- FFmpeg covers cuts, concat, crossfades, zoom-pan, loudness, and blurred 9:16 pads. All tested commands run, except ASS burn-in.
- The local FFmpeg lacks libass. Burn-in captions need a rebuild or a new install. Martin must approve that step.
- Remotion is free for individuals and for-profit organizations with up to 3 employees.
- The yt-dlp README names the flag `--write-auto-subs`. Some guides say `--write-auto-sub`. Use the README form.
- Pixabay content needs no attribution. The YouTube Audio Library is per track. Epidemic and Artlist prices conflict between sources.
- The strongest local Claude Code candidate is `kajisho5/ffmpeg-skill`. It has 3,065 stars and an MIT license. It was created on 2026-09-03. Review its code before any install.

---

## 1. FFmpeg pipelines

**What it is.** The `ffmpeg` command line tool. It cuts and joins video. It filters and exports it. It runs fully local.

**Source.** https://ffmpeg.org/ffmpeg-filters.html (undated, fetched 2026-10-27). Version list: https://ffmpeg.org/download.html (fetched 2026-10-27). The download page lists 9.0.2 (2026-09-18) and 8.1.3 (2026-09-21). Local version is 8.0.1. Update before production use.

| Axis | Rating |
|---|---|
| Runs on macOS | Yes. Homebrew build; VideoToolbox encoder present locally. |
| Scriptable | Yes. Shell command. Claude Code runs it through Bash. |
| Cost | Free (LGPL/GPL build). |
| Quality ceiling | Very high. Full control of codecs and timing. |
| Learning curve | Medium. Filter-graph syntax needs care. |

### 1a. Precise cuts

- Re-encode (frame-accurate). The doc says that with transcoding, accurate seek is the default. Tested: OK.
  ```
  ffmpeg -ss 0.5 -i in.mp4 -t 1.5 -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k out.mp4
  ```
- Stream copy (fast, no re-encode). Cuts start at a keyframe. Tested: OK.
  ```
  ffmpeg -ss 0 -i in.mp4 -t 1.5 -c copy -avoid_negative_ts make_zero out.mp4
  ```
- Rule: use re-encode for exact cuts. Use stream copy only when a keyframe cut is acceptable.

### 1b. Concat

- Concat demuxer. Fastest. All inputs need the same codecs and time base. Tested: OK.
  ```
  # list.txt contains lines: file 'a.mp4'  and  file 'b.mp4'
  ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4
  ```
- Concat filter. Use for mixed inputs; re-encodes. Tested: OK.
  ```
  ffmpeg -i a.mp4 -i b.mp4 -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -c:a aac out.mp4
  ```

### 1c. Speed change (constant)

- Filters: `setpts` (video) and `atempo` (audio). Tempo range is 0.5 to 100. Above 2, `atempo` skips samples. Chain instances for large changes. Tested: OK.
  ```
  ffmpeg -i in.mp4 -filter_complex "[0:v]setpts=PTS/1.25[v];[0:a]atempo=1.25[a]" -map "[v]" -map "[a]" -c:v libx264 -c:a aac out.mp4
  ```
- Variable speed ramp is not tested here. It needs split segments, one `setpts` per segment, and a `concat`.

### 1d. Crossfades

- Video: `xfade`. Audio: `acrossfade`. Doc: inputs must have the same resolution, pixel format, frame rate, and time base. `offset` equals clip A length minus `duration`. Tested: OK.
  ```
  ffmpeg -i a.mp4 -i b.mp4 -filter_complex "[0:v][1:v]xfade=transition=fade:duration=0.5:offset=2.5[v];[0:a][1:a]acrossfade=d=0.5:c1=tri:c2=tri[a]" -map "[v]" -map "[a]" -c:v libx264 -c:a aac out.mp4
  ```
- `xfade` transition list (from the doc): custom, fade, wipeleft, wiperight, wipeup, wipedown, slideleft, slideright, slideup, slidedown, circlecrop, rectcrop, distance, fadeblack, fadewhite, radial, smoothleft, smoothright, smoothup, smoothdown, circleopen, circleclose, vertopen, vertclose, horzopen, horzclose, dissolve, pixelize, diagtl, diagtr, diagbl, diagbr, hlslice, hrslice, vuslice, vdslice, hblur, fadegrays, wipetl, wipetr, wipebl, wipebr, squeezeh, squeezev, zoomin, fadefast, fadeslow, hlwind, hrwind, vuwind, vdwind, coverleft, coverright, coverup, coverdown, revealleft, revealright, revealup, revealdown.
- `acrossfade` options (doc): `d` (duration), `c1` and `c2` (curves), `o` (overlap), `n` (inputs).

### 1e. Zoom-pan

- `zoompan`. Doc default `d` is 90 frames. For video input, use `d=1` per frame. Tested: OK (1280x720 input to 1080x1920 output).
  ```
  ffmpeg -i wide.mp4 -vf "zoompan=z='min(zoom+0.0015,1.3)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30" -t 2 -c:v libx264 -an out.mp4
  ```

### 1f. Burn-in captions (ASS, karaoke)

- Filters: `subtitles=file.ass` (needs libass and libavformat) and `ass=file.ass` (ASS files only, no libavformat). Doc options: `original_size`, `fontsdir`, `force_style`, `shaping`.
  ```
  ffmpeg -i in.mp4 -vf "subtitles=captions.ass" -c:v libx264 -c:a copy out.mp4
  ```
- Test result: FAILED on this Mac. The build lacks libass. Not run.
- Karaoke tags are ASS spec, not ffmpeg doc. `\k` sets a word timing in centiseconds. `\kf` fills a sweep. `\t(...)` animates a tag over time. Example dialogue line (syntax only, not rendered):
  ```
  Dialogue: 0,0:00:00.00,0:00:02.50,Default,,0,0,0,,{\k40}Hello {\k40}short {\k60}video
  ```
- Fix: install a FFmpeg build with libass (Martin must approve the install). Then rerun `run_tests.sh`.

### 1g. Loudness (EBU R128, two pass)

- Filter: `loudnorm`. Doc: `I` default -24, range -70 to -5. `LRA` default 7. `TP` default -2, range -9 to 0. `linear` default true. Doc: set `-ar` explicitly, because dynamic mode upsamples to 192 kHz.
- Pass 1 (measure). Tested: OK. Result for the synthetic clip: input_i -21.80, input_tp -16.08, input_lra 0.10, input_thresh -31.80.
  ```
  ffmpeg -hide_banner -i in.mp4 -af loudnorm=I=-14:LRA=11:TP=-1.5:print_format=json -f null -
  ```
- Pass 2 (apply). Copy the measured values from pass 1.
  ```
  ffmpeg -i in.mp4 -af "loudnorm=I=-14:LRA=11:TP=-1.5:measured_I=-21.80:measured_LRA=0.10:measured_TP=-16.08:measured_thresh=-31.80:offset=0:linear=true" -ar 48000 -c:v copy -c:a aac -b:a 192k out.mp4
  ```
- Pass 2 was not run in this test.

### 1h. 9:16 crop with blurred background

- Filters: `split`, `scale` (with `force_original_aspect_ratio`), `crop`, `boxblur`, `overlay`, `setsar`. Tested: OK.
  ```
  ffmpeg -i wide.mp4 -filter_complex "[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=luma_radius=30:luma_power=2[bg];[b]scale=1080:1920:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1[v]" -map "[v]" -map 0:a -c:v libx264 -c:a aac out.mp4
  ```

### 1i. Export H.264 and HEVC

- H.264. Tested: OK.
  ```
  ffmpeg -i in.mp4 -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart out.mp4
  ```
- HEVC (software). Tested: OK. `-tag:v hvc1` lets Apple players open the file. The tag is Apple guidance, not in the ffmpeg doc.
  ```
  ffmpeg -i in.mp4 -c:v libx265 -crf 22 -preset medium -pix_fmt yuv420p -tag:v hvc1 -c:a aac -b:a 192k -movflags +faststart out.mp4
  ```
- HEVC (Apple hardware). The `hevc_videotoolbox` encoder is present. Not tested. Expected much faster than libx265.
  ```
  ffmpeg -i in.mp4 -c:v hevc_videotoolbox -b:v 12M -tag:v hvc1 -c:a aac -b:a 192k out.mp4
  ```

**Verdict: use as core.** Use the CLI directly from Claude Code. Build a libass-enabled version before any caption work.

---

## 2. Remotion

**What it is.** A React and TypeScript framework. Each video frame is a React render. Remotion renders the frames to MP4 with headless Chrome and a native compositor.

**Sources.**
- https://github.com/remotion-dev/remotion. Last push 2026-10-26. 67,940 stars. GitHub license field: NOASSERTION (custom license). Fetched 2026-10-27.
- https://raw.githubusercontent.com/remotion-dev/remotion/main/LICENSE.md. Undated, fetched 2026-10-27.
- npm: `remotion` 4.0.539. Release tag v4.0.539 published 2026-10-26.
- Pricing: https://www.remotion.dev/docs/license/pricing (page did not render). Prices below come from search results. Verify on the official page.

**License (primary text).**
- Individuals and small companies may use Remotion free, including commercially.
- For-profit organizations with "up to 3 employees" may use it free.
- Larger companies need a Company License.
- The license says Remotion 5.0 will "slightly change" the license. Check the terms before buying.

**Paid tiers (secondary sources, unverified).**
- Creators: about $25 per seat per month. Manual work, including AI agents.
- Automators: $0.01 per render with a $100 per month minimum. Batch rendering.
- Enterprise: from about $500 per month.

**Captions.**
- Package: `@remotion/captions`. Function `createTikTokStyleCaptions` is in v4.0.216 or later.
- Input: an array of `Caption` objects with word-level timing.
- Parameters: `combineTokensWithinMilliseconds`. Optional `breakOnSilenceAfterMilliseconds` (v4.0.514 or later).
- Output: `pages`. Each page has `text`, `startMs`, `durationMs`, and `tokens`. Each token has `text`, `fromMs`, `toMs`, and `pageBreakAfter`.
- Word highlight: compare the current frame time with each token's `fromMs` and `toMs`. Style the active word. Keep a leading space in each token. Use `white-space: pre`.
- Source: https://www.remotion.dev/docs/captions/create-tiktok-style-captions (undated, fetched 2026-10-27).

**CLI render (documented pattern, not run here).**
```
npx remotion render src/index.ts MyComposition out/video.mp4
```

**Apple Silicon.** The npm package `@remotion/compositor-darwin-arm64` exists at version 4.0.539. This shows native macOS arm64 binaries ship.

| Axis | Rating |
|---|---|
| Runs on macOS | Yes. arm64 compositor available. |
| Scriptable | Yes. CLI and Node API. |
| Cost | Free up to 3 employees. Paid above that (see above). |
| Quality ceiling | Very high for motion graphics and branded captions. |
| Learning curve | High. React and TypeScript required. |

**Verdict: use for X only.** Use for branded motion graphics and caption templates. Skip for plain cuts; FFmpeg does those faster.

---

## 3. MoviePy

**What it is.** A Python video editing library. It wraps FFmpeg.

**Sources.**
- https://pypi.org/project/moviepy/. Latest version shown: 2.2.1, released 2025-05-21. Python 3.9 or later. Fetched 2026-10-27.
- https://github.com/Zulko/moviepy. Last push 2026-08-26. 15,046 stars. MIT. Fetched 2026-10-27.
- A third-party source names v2.1.2 as the latest release. The PyPI date and this name conflict. Verify with `pip index versions moviepy`.

**2.x API.** The PyPI example uses `from moviepy import ...` and `with_*` methods, such as `with_duration`, `with_position`, and `with_volume_scaled`. The v2.0 release has breaking changes. A third-party source says `moviepy.editor` was removed. The PyPI page does not confirm that.

| Axis | Rating |
|---|---|
| Runs on macOS | Yes. |
| Scriptable | Yes. Python. |
| Cost | Free. |
| Quality ceiling | Medium. Limited by per-frame Python callbacks. |
| Learning curve | Low to medium. |

**Verdict: skip.** Raw FFmpeg commands cover the same jobs with less overhead. Speed was not measured.

---

## 4. PySceneDetect

**What it is.** Scene and cut detection in Python and a CLI. It finds cuts and fades.

**Sources.**
- https://github.com/Breakthrough/PySceneDetect. Last push 2026-10-27. 5,296 stars. BSD-3-Clause.
- Docs API page: https://www.scenedetect.com/docs/latest/api/detectors.html. Shows version 0.7.1. Fetched 2026-10-27.
- CLI page: https://www.scenedetect.com/docs/latest/cli.html. Undated, fetched 2026-10-27.

**Detectors (from the API docs).**

| Detector | Default threshold | Default min_scene_len | Detects |
|---|---|---|---|
| AdaptiveDetector | adaptive_threshold=3.0 | 15 frames | Cuts. Compares changes with a rolling average. |
| ContentDetector | threshold=27.0 | 15 frames | Cuts. HSV and intensity changes. |
| HashDetector | threshold=0.395 | 15 frames | Cuts. Perceptual hash distance. |
| HistogramDetector | threshold=0.05 | 15 frames | Cuts. YUV histogram change. |
| ThresholdDetector | threshold=12 | 15 frames | Fades in and out. |

**CLI (documented).**
```
scenedetect -i video.mp4 detect-adaptive list-scenes
scenedetect -i video.mp4 detect-content list-scenes save-images
scenedetect -i video.mp4 detect-content split-video
```
The CLI page says `detect-adaptive` and `detect-content` find fast cuts. `detect-threshold` finds fades.

**Python API (not run here).** Secondary source describes `detect(path, ContentDetector())`, which returns a list of start and end timecodes. The docs page I fetched shows no `detect()` snippet. Verify with a test run.

| Axis | Rating |
|---|---|
| Runs on macOS | Yes. |
| Scriptable | Yes. CLI and Python. |
| Cost | Free. |
| Quality ceiling | Good for hard cuts. Fades need ThresholdDetector. |
| Learning curve | Low. |

**Verdict: use as core** for scene timestamps.

---

## 5. yt-dlp

**What it is.** A command line downloader for many video sites.

**Sources.** https://github.com/yt-dlp/yt-dlp. Last push 2026-10-26. 202,657 stars. Unlicense (GitHub). README fetched 2026-10-27. The README says stable releases come roughly monthly.

**Options (from the README, fetched 2026-10-27).**
- Sections. `--download-sections REGEX`. A `*` prefix selects a time range. Negative times count from the end. Needs ffmpeg. Repeatable.
  ```
  yt-dlp --download-sections "*00:15-00:45" -o "ref.%(ext)s" "URL"
  ```
- Auto captions. `--write-auto-subs` (alias `--write-automatic-subs`). Pair with `--sub-langs` and `--skip-download`. `--sub-format` takes a preference list such as `"srt/vtt"`.
  ```
  yt-dlp --write-auto-subs --sub-langs "en" --sub-format "srt/vtt" --skip-download -o "ref.%(ext)s" "URL"
  ```
  The README does not list `--write-auto-sub` (singular). Some guides use it. Use the plural form.
- MP4 preset. `-t mp4` expands to `--merge-output-format mp4 --remux-video mp4 -S vcodec:h264,lang,quality,res,fps,hdr:12,acodec:aac`.
  ```
  yt-dlp -t mp4 "URL"
  ```
- Format selection. Merging needs ffmpeg. README example: `-f bestvideo+bestaudio`. The format-selection section was cut off in the fetch. Verify the mp4-specific selector on the local binary.

**Legal and terms (caution, not legal advice).**
- yt-dlp code is Unlicense. Release binaries include GPL code. Dependencies carry their own licenses (README).
- Most platforms restrict downloads in their terms of service. Download only your own content or material you have written permission to use.
- Copyright applies to reference clips. Use them for study or briefing only, unless the rights holder agrees otherwise.

| Axis | Rating |
|---|---|
| Runs on macOS | Yes. |
| Scriptable | Yes. CLI. |
| Cost | Free. |
| Quality ceiling | Source quality as offered by the site. |
| Learning curve | Low. |

**Verdict: use for X only.** Use for own clips and permitted references. Skip for copying third-party content.

---

## 6. mlx-whisper (Apple Silicon)

**What it is.** Whisper speech recognition on MLX, Apple's array framework. Runs on the Apple GPU.

**Sources.**
- https://pypi.org/project/mlx-whisper/. Latest version shown: 0.4.3, released 2025-08-29. Python 3.8 or later. Fetched 2026-10-27. Needs ffmpeg (`brew install ffmpeg`).
- ml-explore/mlx-examples (Whisper example). Last push 2026-04-06. 9,038 stars. MIT.

**Word timestamps (PyPI example).**
```python
import mlx_whisper

out = mlx_whisper.transcribe(
    "in.mp4",
    path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
    word_timestamps=True,
)
for seg in out["segments"]:
    for w in seg.get("words", []):
        print(w)  # inspect the keys on the local binary before you rely on them
```

- The PyPI page sets the default model to `mlx-community/whisper-tiny`. Set `path_or_hf_repo` each time.
- `large-v3-turbo` is a pruned large-v3. It is faster and slightly less accurate (Pipecat docs, fetched 2026-10-27).
- Quantized variants exist on Hugging Face (for example, a q8 build by LibraxisAI). Not tested.
- Speed was not measured in this run.

| Axis | Rating |
|---|---|
| Runs on macOS | Yes. Apple Silicon only in practice. |
| Scriptable | Yes. Python. |
| Cost | Free. First run downloads a model (about 800 MB for turbo, per a third-party page). |
| Quality ceiling | High for clear speech. Word timing is model-based. |
| Learning curve | Low. |

**Verdict: use as core** for transcripts and word timing. Feed the words into an ASS file for burn-in.

---

## 7. Music and SFX (commercial social video)

| Source | Terms (what the page says) | Cost | Verdict |
|---|---|---|---|
| Pixabay | Content License summary, undated, fetched 2026-10-27. Free use. No attribution required. Modification allowed. No standalone resale. No brand or trademark use for goods or services. No misleading or illegal use. The page covers all content, including audio. | Free | Use as core free source. Log each asset. |
| YouTube Audio Library | Official page not fetched. Third-party guides state that terms vary by track. One comparison site says standard tracks cover monetized YouTube videos only. CC-BY tracks allow commercial use with credit. | Free | Use for YouTube-only work. Check each track before client use. |
| Free Music Archive | Site says music is "free to play, download and share." It does not state commercial terms. Tracks carry different Creative Commons licenses. Fetched 2026-10-27. | Free | Use only CC tracks with a clear commercial grant. Check each file. |
| Epidemic Sound | Official pricing page fetched but no prices rendered. Page says Pro and Enterprise include ad use. All plans include unlimited downloads and usage. Third-party trackers conflict. One: Creator $17.99/mo or $119.88/yr; Pro $39.99/mo or $203.88/yr (verified 2026-07-31). Another: Personal $9.99/mo; Commercial $19.99/mo. | Subscription | Use only with a confirmed price. |
| Artlist | Official pricing returned HTTP 403. Third-party: Music and SFX about $14.99/mo or $119.88/yr. One tracker says the social plan excludes client work. | Subscription | Verify before buying. |
| Uppbeat | Official pricing returned HTTP 429. Not verified. | Unknown | Not verified. |

**Verdict.** Free and clear for commercial social video: Pixabay (no attribution) and CC-BY tracks from the YouTube Audio Library. Keep a license log per asset for every client job.

---

## 8. ElevenLabs (text-to-speech, optional)

**Source.** https://elevenlabs.io/pricing. Fetched 2026-10-27. Some dates are partial: "Until Nov 1" (no year), and a promo "Ends September 30" (no year).

| Plan | Monthly price | Credits per month | Commercial use | Instant clone | Professional clone |
|---|---|---|---|---|---|
| Free | $0 | 10k | Not listed | No | No |
| Starter | $1 shown (FAQ says $6) | 30k | Yes | Yes | No |
| Creator | $11 shown (FAQ says $22) | 121k | Yes | Yes | Yes |
| Pro | $99 | 600k | Yes | Yes | Yes |
| Scale | $299 | 1.8M (3 seats) | Yes | Yes | Yes |
| Business | $990 | 6M (10 seats) | Yes | Yes | Yes |

- Price conflict: the plan cards and the FAQ show different Starter and Creator prices. Confirm before buying.
- API rate: credits per character (1 credit per character for V2 Multilingual; 0.5 credit per character for Flash and Turbo). A third-party page says $0.10 per 1,000 characters (Multilingual v2) and $0.05 (Flash or Turbo). Check the official rate.
- Voice cloning consent and usage rules were not checked. Read the terms before cloning any voice.

| Axis | Rating |
|---|---|
| Runs on macOS | Cloud API only. |
| Scriptable | Yes. REST API. |
| Cost | From $1 to $6 per month (Starter). Confirm the price. |
| Quality ceiling | High. |
| Learning curve | Low. |

**Verdict: use for X only.** Use for voice-over where a human voice is not available. Creator is the lowest tier with professional cloning.

---

## 9. Claude Code skills, plugins, and MCP servers for video editing

Stars, last-push dates, and licenses are from the GitHub API (run 2026-10-27). Nothing was installed. Review the code before any install.

| Repo | Stars | Last push | License | What it does | Runs locally |
|---|---|---|---|---|---|
| kajisho5/ffmpeg-skill | 3,065 | 2026-10-26 | MIT | 42 FFmpeg tools and an MCP server for Claude Code. Created 2026-09-03. npm: `ffmpeg-skill`. | Yes. Python standard library. |
| haidrrrry/claude-remotion-skill | 653 | 2026-08-12 | MIT | Remotion skill for motion graphics and captions. | Yes. |
| Hainrixz/editor-pro-max | 279 | 2026-10-25 | Not checked | Remotion and Claude Code editor (25 components, 9 templates). | Yes. |
| KyaniteLabs/mcp-video (kinocut) | 222 | 2026-10-27 | Apache-2.0 | FFmpeg MCP server with typed tools and checks. Optional Whisper extras. | Yes. |
| wshuyi/remotion-video-skill | 433 | 2026-01-25 | None | Remotion skill with ffmpeg and ffprobe. | Yes. |
| wilwaldon/Claude-Code-Video-Toolkit | 101 | 2026-02-26 | None | Remotion, Manim, screen record, YouTube clip, FFmpeg post. | Yes. Needs yt-dlp, ffmpeg with libass. |
| pouyashahrdami/mimic-mcp | 27 | 2026-08-31 | MIT | Clones a reference reel style with Remotion. | Yes. |
| chandler767/mcp-video-editor | 5 | 2026-02-14 | None | Go MCP server: FFmpeg and Whisper. | Yes. |
| misbahsy/video-audio-mcp | 89 | 2025-05-24 | MIT | FFmpeg MCP: trim, overlay, subtitle burn, silence removal. Stale. | Yes. |
| KirttiVushan/claude-code | 1 | 2026-03-16 | MIT | Video-editing SKILL.md: FFmpeg, Remotion, ElevenLabs. | Yes. |
| remotion-dev/remotion | 67,940 | 2026-10-26 | Custom | Official framework. A Claude Code skill is reported (`npx skills add remotion`), not verified. | Yes. |
| anthropics/skills | 184,019 | 2026-10-09 | Mixed (Apache-2.0 and source-available for document skills) | Document skills: docx, pdf, pptx, xlsx. No video, FFmpeg, or Remotion skill in the fetched page. | n/a |

Not found: `breverdbidder/free-video-edit-mcp` returned HTTP 404 from the GitHub API. Treat the name as unverified.

**Verdict.** Evaluate `kajisho5/ffmpeg-skill` first. It is local, MIT, tested on FFmpeg 5.1 to 9, and active. Its age is about 2 months. Read its MCP and shell code before any install. Use `haidrrrry/claude-remotion-skill` as a reference for Remotion work.

---

## 10. Other tools

| Tool | Source and date | License and stars | Verdict |
|---|---|---|---|
| auto-editor | https://github.com/wyattblue/auto-editor. Last push 2026-10-26. | Unlicense. 5,634 stars. | Use as core for silence cuts. `pip install auto-editor`. Margin option `--margin 0.2sec`. Exports XML for Premiere and Resolve. Not run here. |
| whisper-ctranslate2 | https://github.com/Softcatala/whisper-ctranslate2. Last push 2026-10-05. | MIT. 1,366 stars. | Fallback only. CTranslate2 CLI. No Apple GPU path, so slower than mlx-whisper on this Mac. |
| captacity | https://github.com/unconv/captacity. Last push 2024-06-07. | MIT. 139 stars. | Skip. Stale. |
| auto-subtitle | https://github.com/m1guelpf/auto-subtitle. Last push 2024-07-12. | MIT. 2,297 stars. | Skip. Stale. |
| editly | https://github.com/mifi/editly. Last push 2025-05-12. | MIT. 5,557 stars. | Skip for now. Declarative JSON edit tool. Stale for 17 months. |
| ffmpeg-python | https://github.com/kkroening/ffmpeg-python. Last push 2024-08-04. | Apache-2.0. 11,014 stars. | Skip. Raw CLI commands are simpler for Claude to write and check. |
| Descript | Pricing via Sonix (secondary, undated): Free $0; Hobbyist $16/yr or $24/mo; Creator $24/yr or $35/mo; Business $50/yr or $65/mo, per user. Official page not checked. | Commercial. | Skip for the pipeline. GUI only. Use for manual finishing. |
| OpusClip | Third-party (undated): Starter $15/mo (150 min); Pro $29/mo (300 min). Free plan: 60 min, watermark. | Commercial, cloud. | Skip. Cloud only; no local control. |
| Vizard | Third-party (undated): Creator about $14.50 to $20/mo. Official page not checked. | Commercial, cloud. | Skip. Not verified. |
| vidstack | Not checked in this run. Prior knowledge: a web video player library, not an editor. | n/a | Skip. Verify if needed. |
| CapCut API | Not verified in this run. | n/a | Skip. |

---

## Recommended local stack

1. FFmpeg with libass. Install a libass build (Martin approves). Verify the version (8.x or 9.x).
2. mlx-whisper with `large-v3-turbo` and `word_timestamps=True`. Write an ASS file from the words.
3. `ffmpeg -vf subtitles=...` for burn-in. Use `loudnorm` (two pass) and export with libx264 or libx265 (`hvc1`).
4. auto-editor for silence cuts on talking-head footage.
5. PySceneDetect `detect-adaptive list-scenes` for scene timestamps.
6. Remotion for branded motion graphics and caption templates. Free for up to 3 employees.
7. yt-dlp only for own clips or permitted references.
8. `kajisho5/ffmpeg-skill` as a candidate, after a code review. Otherwise keep plain FFmpeg scripts.
9. Music: Pixabay (no attribution) and CC-BY tracks from the YouTube Audio Library. Log each asset's license.
10. ElevenLabs Creator tier only for voice-over that needs professional cloning.

---

## Open items (not verified in this run)

- Install a FFmpeg build with libass, then rerun the ASS test in `run_tests.sh`. Martin must approve.
- Confirm the Remotion paid prices on the official pricing page.
- Confirm Epidemic Sound and Artlist prices on the official pages. Both were blocked or empty.
- Confirm the YouTube Audio Library terms on YouTube's own help page.
- Confirm the ElevenLabs Starter and Creator prices (page and FAQ conflict).
- Confirm the MoviePy latest version with `pip index versions moviepy`.

---

## Sources

| URL | Date |
|---|---|
| https://ffmpeg.org/ffmpeg-filters.html | undated, fetched 2026-10-27 |
| https://ffmpeg.org/ffmpeg-formats.html | undated, fetched 2026-10-27 |
| https://ffmpeg.org/download.html | fetched 2026-10-27 (lists 9.0.2 on 2026-09-18; 8.1.3 on 2026-09-21) |
| https://www.remotion.dev/docs/license | undated, did not render |
| https://raw.githubusercontent.com/remotion-dev/remotion/main/LICENSE.md | undated, fetched 2026-10-27 |
| https://github.com/remotion-dev/remotion | pushed 2026-10-26 |
| https://www.remotion.dev/docs/captions/create-tiktok-style-captions | undated, fetched 2026-10-27 |
| https://www.remotion.dev/docs/license/pricing | undated, did not render (prices from secondary sources) |
| https://pypi.org/project/moviepy/ | latest 2.2.1, released 2025-05-21 |
| https://github.com/Zulko/moviepy | pushed 2026-08-26 |
| https://www.scenedetect.com/docs/latest/api/detectors.html | docs version 0.7.1, fetched 2026-10-27 |
| https://www.scenedetect.com/docs/latest/cli.html | undated, fetched 2026-10-27 |
| https://github.com/Breakthrough/PySceneDetect | pushed 2026-10-27 |
| https://github.com/yt-dlp/yt-dlp | pushed 2026-10-26 (README fetched 2026-10-27) |
| https://pypi.org/project/mlx-whisper/ | latest 0.4.3, released 2025-08-29 |
| https://github.com/ml-explore/mlx-examples | pushed 2026-04-06 |
| https://pixabay.com/service/license-summary/ | undated, fetched 2026-10-27 |
| https://support.google.com/youtube (YouTube Audio Library) | not fetched; third-party sources only |
| https://freemusicarchive.org/ | undated, fetched 2026-10-27 |
| https://www.epidemicsound.com/pricing/ | undated, no prices rendered |
| https://artlist.io/pricing | HTTP 403 |
| https://uppbeat.io/pricing | HTTP 429 |
| https://elevenlabs.io/pricing | undated, fetched 2026-10-27 |
| https://github.com/kajisho5/ffmpeg-skill | pushed 2026-10-26; created 2026-09-03 |
| https://github.com/haidrrrry/claude-remotion-skill | pushed 2026-08-12 |
| https://github.com/KyaniteLabs/mcp-video | pushed 2026-10-27 |
| https://github.com/anthropics/skills | pushed 2026-10-09 |
| https://github.com/wyattblue/auto-editor | pushed 2026-10-26 |
| https://github.com/Softcatala/whisper-ctranslate2 | pushed 2026-10-05 |
| https://github.com/unconv/captacity | pushed 2024-06-07 |
| https://github.com/m1guelpf/auto-subtitle | pushed 2024-07-12 |
| https://github.com/mifi/editly | pushed 2025-05-12 |
| https://github.com/kkroening/ffmpeg-python | pushed 2024-08-04 |
| https://sonix.ai/resources/descript-pricing/ | undated (secondary) |
| https://www.castmagic.io/blog/opus-clip-pricing | undated (secondary) |
| https://techsy.io/en/blog/opusclip-vs-vizard | undated (secondary) |
