# Step 0.0 Inputs Grill Record: Captions for video

Date: 2026-10-19
Owner: Martin Drendel
Workflow ID: `captions`
Status: Confirmed via interactive grill (2 rounds, 8 cards)

---

## 1. The Job (Objective & Scope)
- **What enters:** One text dump per day. Martin and Celine write it during the day or at the end of the day. It holds thoughts, ideas, budget notes, plans, strategy, where they live, insights on how they live. It arrives as a Google Drive link or as pasted text. German, English or mixed.
- **What transforms:** The workflow reads the dump, orders it into a story for one voiceless daily YouTube video, and writes the on-screen caption text. Every fact stays as in the dump. Nothing is added.
- **Who uses the output:** Martin and Celine. They paste the caption blocks into the video editor as lower-third text.
- **Martin's words:** "This workflow is here to prepare the text that's going to be going into the video."

## 2. Runtime Surface
- Claude Code chat. Martin starts it with `/captions <drive link or pasted text>`.
- Not a Cowork task, not a cloud routine.

## 3. Cadence / Frequency
- Daily. One video per day. One run per day on demand, when the dump is ready.

## 4. Hard Limits (Failure Boundaries)
- **Never upload or publish.** The workflow writes text only. It never touches YouTube, never uploads, never schedules a video.
- The dump is the only source of facts. The workflow never adds a number, a place, a price or a plan that is not in the dump.
- The original dump file in Drive is read only. The workflow writes new files only.

## 5. Format decisions (grill round 2)
- **Language:** English captions. The dump can be in any language.
- **Storage:** `00_project/assets/youtube-captions/<YYYY-MM-DD>/` with `dump.md`, `captions.md`, `_run.json`. `captions.md` is also copied to the Drive folder "Captions Celine Martin" (id 1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm).
- **Style:** Short lines. One block has max 12 words and fits in 2 lines at the bottom of the image. Many short blocks per video.
- **Voice:** "We" (Martin + Celine). Casual vlog voice, first person plural.

## 6. Drive home (Martin, 2026-10-19)
- Martin gave the folder: https://drive.google.com/drive/folders/1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm
- Title "Captions Celine Martin", id `1heXhO-CGVpM2bLp5f8T-nizTf7kmXnGm`, owner 741studio18@gmail.com, created 2026-10-19, empty at 2026-10-19.
- This folder replaces the planned folder "YouTube Captions". The dump goes in as a Google Doc. The finished captions go in as a Google Doc "<date> captions".
