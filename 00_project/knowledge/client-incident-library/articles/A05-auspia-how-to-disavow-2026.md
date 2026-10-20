# How to Disavow Toxic Backlinks in 2026: Google's Disavow Tool, Step by Step

- URL: https://auspia.ai/blog/how-to-disavow-toxic-backlinks-2026
- Published: 2026-09-03 (modified 2026-09-09)
- Author/site: Julian Mercer, Auspia
- Fetched: 2026-10-12
- Language: en

---

## The 2026 answer, and what John Mueller actually said

Yes: Google's disavow tool still has real effects in 2026. In early September 2026, John Mueller confirmed as much in a Reddit exchange picked up by Search Engine Roundtable: the tool *"does have effects,"* but it *"has its place & time."*

That quote matters because the context was a site owner who blamed the disavow file for a ranking drop. Mueller pushed back: disavowing a handful of links will not pull a site out of Search, and drops like that usually come from something else (a spam update, which can take *many months* to recover from, or technical trouble such as a site-wide block). His practical advice in that same discussion was simple: make sure the disavow file accurately reflects what the site actually needs ("might be empty, or might not be empty"), then audit the real cause of the drop.

So the honest 2026 position is neither "disavow everything" nor "the tool is dead." It is: the tool works, but only for a narrow set of situations, and it is easy to misuse. Google's own documentation says to use it only when you have a considerable number of spammy links and those links have caused, or are likely to cause, a manual action. Most sites should never touch it.

## Who this playbook is for

| Outcome | One valid disavow file uploaded to the right Search Console property, plus a plan for judging whether it worked. | 
| You need | Owner (or full-permission) access to a Search Console **URL-prefix** property. The disavow tool does not support Domain properties. | 
| Inputs | The Links report export from Search Console, and roughly 1 to 3 hours of hands-on work. | 
| Done looks like | File uploaded with zero format errors, manual action lifted or clearly recovering, and a dated note on your calendar telling you when to judge the result. | 

If you only have a Domain property today, create a URL-prefix property before you continue (add a property, choose URL prefix, enter `https://www.yourdomain.com` and verify it).

## Before you start: decide if disavowing is actually the fix

Run this gate before you export anything. It is the step most 2026 guides skip, and it is the one Mueller keeps pointing at.

| Your situation | Verdict | 
|---|---|
| Manual action "Unnatural links to your site" in Search Console, or a clear link-scheme violation you caused | **Disavow** after trying removal first | 
| Confirmed negative SEO attack: a pattern of spammy links you never placed | **Disavow**, and keep evidence | 
| Inherited link footprint: you bought an existing site with old paid-link or PBN links | **Disavow** the confirmed junk | 
| Third-party tool flagged some links as "toxic" | **Do not disavow yet.** Review manually first | 
| No manual action, just a ranking drop | **Do not disavow.** Investigate the drop first | 
| Weekly link hygiene ("let's clean up any low-quality links") | **Do not disavow.** Google's algorithms ignore the vast majority of weak links on their own, and disavowing real editorial links can cost you equity | 

*Gate: disavow only when a manual action, a confirmed negative SEO attack, or an inherited paid-link profile is involved.*

## Pull one master list of who links to you

In Search Console, open the **Links** report for the property, switch to "Links" (external links view), then export all of them. You want the full totals, not the first page, because the report's default view is truncated.

Output: one master list of referring pages plus their targets on your site. Check: the export covers both full pages and connected domains, and the URL-count column matches the totals shown on screen. If they do not match, pull the report again and wait for it to finish generating.

A second opinion (Ahrefs, Semrush, or Majestic) is useful here for one reason only: finding links GSC does not show. Do not import their "toxic" flags into your disavow file. Toxicity scores are not evidence of a manual action.

## Try removal first, and keep the paper trail

Google's own documentation prioritizes removal: you are supposed to try to get the bad links taken down, and only then disavow what you could not remove. Skip this step and a reconsideration request (if you need one later) gets much harder to defend, because Google asks what you actually did.

For each link you want gone: find a contact, e-mail or use the site's contact form, and log the attempt. Keep the date, the address you used, and the reply.

Output: a small log, say five rows: URL, contact route, date, outcome. Check: every domain you disavow falls into one of two boxes for your records: "removal was impossible" or "site has clear paid-link/PBN footprints." If a spam link comes down after one polite note, great: leave it off the disavow list.

## Judge the links like an editor would

This is a human pass; do not automate the verdict. Sort your list into buckets:

| Bucket | Examples | Disavow? | 
|---|---|---|
| Clear manipulation | PBNs, paid posts with exact-match anchors, link farms, adult/area-dating spam, spammy directories | Yes | 
| Irrelevant or low value | Most forum profiles, random comments, old press releases | Not by themselves; Google already ignores most of this | 
| Editorial or semirelevant | Product mentions, press, guest content, partner links | Never | 
| Your own domain or subdomain | Self-referencing links | Never (it can strip internal signal) | 

Two decisions happen here, and they are the ones people get wrong:

1. `domain:` versus full URL. Use `domain:` for the spammy site as a whole; it covers all subdomains and is the option that survives a site moving URLs. Use a full URL only when the domain is mostly legitimate but one page is a scraped copy or a paid placement.
2. The unusual case: whole-TLD disavow. Mueller confirmed in March 2026 that you can disavow every domain from one top-level extension by writing `domain:.xyz`: a "big hammer," as he put it, and not something the official documentation describes. Use it only when a spam wave is flooding you from one extension and you can see the pattern yourself. Great at stopping a bulk attack; easy to regret, because it also cancels every real link from that TLD.

## Build a file that passes Google's format checks

The disavow tool is picky in ways that silently separate working uploads from worthless ones. Google accepts a plain-text file only:

- UTF-8 or 7-bit ASCII encoding, `.txt` extension (CSV and Excel files are rejected).
- One entry per line, no order requirement.
- Up to 100,000 lines (counted including blanks and comments) or 2 MB, whichever comes first.
- URLs capped at 2,048 characters.
- Paths are not allowed: `example.com/blog/spam-post` will not disavow anything. Only `domain:example.com` or a full root-level URL.
- Lines starting with `#` are comments. Use them: they are the only audit trail Google's interface gives you.

A line-by-line example, annotated:

```
# Disavow file for example.com - updated 2026-09-03
# Reason: Manual action "unnatural links to your site" (2026-08-27)
# Removal attempts logged in /outreach-log; 14 sites unreachable
# Link farm discovered by manual review of GSC export
domain:spam-site-a.com
domain:linkfarm-b.net
# Only this paid placement was confirmed; the rest of the site is legit
https://legit-site.com/paid-post-about-watch-dials
# TLD flood: budget insurance spam from one extension (Mueller-confirmed method)
domain:.xyz
```
Expected output: one `.txt` file, under 2 MB, with every entry matching `domain:` or a full https URL. Check: read the file top to bottom and verify no `https://` slipped in front of a `domain:` entry, and no `www.`-lite abbreviations. Recovery path if the upload later reports errors: fix, re-upload the corrected file; Google keeps your previous list if the new one fails validation, so a bad file never leaves you with nothing.

*The four format rules that decide whether a disavow file actually does anything.*

## Upload once, to the right property

Open `search.google.com/search-console/disavow-links`, pick the property, and upload.

Three rules from Google's documentation that most people break:

1. URL-prefix only. Domain properties cannot be used, so if you converted to a Domain property, add a URL-prefix equivalent.
2. One list per property, and each upload replaces the last one. The file is never additive. If you later want to disavow more links, re-upload the whole updated file, and keep the master copy somewhere you can find it next month.
3. Separate lists for http and https (and www vs non-www) if you keep those as separate properties. A list for `example.com` will also apply to `m.example.com`, but not to the `https://` property.

Expected output: a success confirmation, or an immediate error list. Check: no format errors. If there are any, correct the file and re-upload, since the previous list stays active until a clean file lands.

## Verify what's verifiable, and wait the right amount of time

There is no status dashboard. In practice, most people check their rankings daily for the first week after uploading and declare victory or doom. That week tells you nothing. Google gives you exactly one honest signal path, and it is indirect:

- Still in Links report? Yes, and that is expected. Disavowed links keep appearing there. Seeing them is not proof of failure.
- The real signal: the manual action. If you disavowed because of a manual action, the Security & Manual Actions page is your indicator: submitted a reconsideration request after cleanup, the action lifts, and only then do rankings move.
- Traffic and rankings. Judge only after Google has had time to recrawl. Roughly:

| Time from upload | What to look for | 
|---|---|
| Week 1 | File accepted, no errors. Nothing else should change. | 
| 2 to 6 weeks | Google "incorporates your list into the index as Google recrawls the web." Whipsaw rankings here are noise, not signal. | 
| 2 to 6 months | The honest window for a recovery story, and longer if your drop happened around a spam update (Mueller's word: many months). | 
| Any time | If you need to undo everything, open the property and click *Cancel Disavowals*: the whole list clears with the same weeks-long lag in reverse. | 

Prevention for next time: keep the master file and the outreach log together, and set a calendar note at month 2 and month 6 so you judge the result on a plan, not through daily refresh anxiety.

## If nothing changes, go back to Mueller's checklist

Suppose three months pass and nothing moved. In the September 2026 exchange, Mueller's own three checks are the right order here:

1. Is the file accurate? In his words, it "might be empty, or might not be empty." If your file disavows 300 domains and the manual action remains, ask what really links badly. Also check the reverse: if you disavowed links that were not actually harmful, trim the file and re-upload.
2. Was there a spam update in the window? Recovery from spam updates can take many months, independent of anything you did with links. Timing is not evidence a disavow failed.
3. Is anything technical blocking the site? A blocked or inaccessible site shows up as "ranking drop" and no disavow can fix it (crawlability, hoster blocks, redirect chains, and similar).

Only when the manual action is real and the file is clean should you use the final lever: a reconsideration request, which still exists in 2026. File it after the work is genuinely done: removal evidence, disavow file, and the fix that prevents recurrence. Reviews usually come back within days to two weeks. Practitioners tracking these cases through 2026 report rejections have become more common, with sites that completed the whole cleanup still getting refused; that evidence is anecdotal rather than official, and the practical lesson is blunt: a half-done fix has close to no chance either way. If a request is rejected, that is a message about the depth of the fix, not a signal to add another thousand domains to a file.

## Mistakes that make the file worse

| Mistake | What actually happens | 
|---|---|
| Disavowing 1,000 domains from a third-party "toxic" flag | You lose real equity; Google ignores most of those links anyway | 
| `domain:https://example.com` | The entry is malformed and does nothing | 
| Uploading CSV on the theory that it's easier | Rejected by the validator | 
| Treating the upload as additive | The old file is silently replaced; keep your master copy | 
| Disavowing your own domain or subdomain | You cancel internal signal | 
| Judging the outcome after ten days | You decided before the recrawl; nothing you observe is informative | 
| Disavowing a real editorial link | You strip a legitimate signal, the exact opposite of what a recovery needs | 

## FAQ

**Does disavowing links hurt rankings?** Not in the way the site owner in Mueller's September 2026 example suspected. Disavowing a handful of links will not drop a site out of Search. What can hurt you is over-disavowing: a file full of real editorial and commercial links costs equity, and a file full of noise changes nothing. The risk runs in both directions, which is why the qualify-then-trim order matters.

**Can I disavow an entire top-level domain?** Yes. `domain:.xyz` (any extension) in your file disavows every domain using that extension. Mueller confirmed the method in March 2026 and called it a big hammer. It works, it is undocumented, and it only makes sense against a bulk spam flood from one TLD.

**How long until disavowing takes effect?** Google says it can take a few weeks to incorporate the list as it recrawls the web, and the same applies in reverse when you cancel. A ranking recovery worth calling a recovery usually takes two to six months, longer if a spam update happened in the same window.

**The disavow tool will not accept my Domain property. What do I do?** That is expected: the tool does not support Domain properties. Add a URL-prefix property for `https://www.yourdomain.com`, verify it, and upload there. Alternatively, keep the Domain property for other reporting and run the disavow on the URL-prefix one.

**Do I still need a reconsideration request when I disavow?** If your goal is a link-spam manual action, yes. The disavow file alone does not clear it. Submit the request after removal attempts, an honest cleanup note, and the disavow file are all in place. If there is no manual action, no request is needed or useful.

**The links I disavowed still show in the Links report. Does that mean it failed?** No. Google keeps disavowed links in the report by design. Roughly: the report never proves failure, and the manual action page never lies. Judge on that page and on traffic, not on the report.

Author: Julian Mercer, 14-Year Technical SEO Practitioner at Auspia. Julian writes about crawlability, site architecture, and the technical foundations that keep a site readable by Google, and by AI answer systems.
