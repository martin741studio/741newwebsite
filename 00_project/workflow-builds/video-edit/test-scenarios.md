# Test scenarios — video-edit (written before the skill body, per R1.2)

## 1. Obvious trigger
**Input:** "/video-edit — here's my raw clip [file], here's the reference [link], make it a 9:16 reel, message is 'local SEO in 24 hours'."
**Expected:** skill loads, resolves a run folder, profiles the reference if not already profiled, transcribes the raw clip, drafts a cut plan, shows it for approval before rendering anything.

## 2. Paraphrased trigger
**Input:** "cut this talking-head footage down like that TikTok I sent you, I want it punchy for Instagram."
**Expected:** skill loads (no literal "/video-edit" needed), treats "that TikTok I sent you" as the reference (asks which link/file if ambiguous), treats "punchy" + "Instagram" as pacing/aspect-ratio signal, same pipeline.

## 3. Must-not-trigger (negative)
**Input:** "write today's captions from our dump, usual format."
**Expected:** skill does NOT load. This is the `captions` skill's job (on-screen text from a thought dump, no video file involved). `video-edit`'s frontmatter negative trigger must name this explicitly.

## 4. Must-not-trigger (negative, second case)
**Input:** "give the client some video content ideas for next month."
**Expected:** skill does NOT load. This is `content-format-board` (ideas + concept stills, no footage file to cut).
