# V4 — Claude Is Moving to the Cloud (Here's What Breaks)

- Channel: Mansel Scheffel
- URL: https://www.youtube.com/watch?v=Mr-8DdrZDjo
- Type: YouTube explainer, 12m 57s
- Upload date: 2026-10-05
- Views: 74,189 (at fetch)
- Fetch date: 2026-10-13 (transcript via Apify johnvc/YoutubeTranscripts. Raw transcript not stored here)

## Key points (paraphrased from transcript. Checked against O6 where possible)

1. From 6 Oct 2026 (Pro/Max), Chat and Cowork merge and new Cowork work runs in Anthropic cloud. Existing local tasks finish locally. (Confirmed by O6.)
2. Team: both modes, cloud on by default. Enterprise: both modes, cloud off by default. (The help article, see source O6, marks the Team plan as beta and the Enterprise plan as admin-enabled. That is roughly consistent.)
3. The local-folder picker disappears for new work. Anything that depends on local files, local SQLite databases or local context breaks unless the Desktop app stays open or the data moves to a cloud store (Supabase, Notion, GitHub, the Project Library).
4. In his account, scheduled tasks for new-format projects could not yet be created from the Scheduled panel. You ask the project's orchestrator instead. He flags this as an in-between state.
5. Dispatch: no new sign-ups after 6 Oct. (Confirmed by O6: not available to new users.)
6. Skills added locally in the Desktop app do not auto-sync to the claude.ai account. Upload skills and connectors via claude.ai, and add plugins there or through a GitHub plugin marketplace, so cloud tasks and the phone can use them.
7. Design advice: decide before building which data may go to which system, and keep context in portable files you own.

## Use for 741

Warns that any cloud-scheduled morning scan cannot read the local 741 repo, local scripts or the local Supabase helpers unless the Mac and Desktop app are on. Skills the grill needs must be uploaded to claude.ai for cloud runs.

Short quote: "Context is the most important thing for any AI system."
