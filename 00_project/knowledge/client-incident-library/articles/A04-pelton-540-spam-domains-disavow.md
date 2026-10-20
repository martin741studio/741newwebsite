# How to Disavow Backlinks Found in Ahrefs (540 Spam Domains)

- URL: https://www.nathanpelton.com/content/blog/seo/spam-backlinks-and-the-disavow-file.htm
- Published: 2026-09-01 (update section dated October 2026)
- Author/site: Nathan Pelton, nathanpelton.com
- Fetched: 2026-10-12
- Language: en

---

Ahrefs emails me when a site gains or loses backlinks. Most weeks it is noise. In May the numbers on nomadsamor.com, our RV travel site, started climbing in a way that had nothing to do with anything we published, and by the end of August the site had picked up 559 referring domains.

I went through all of them. 540 are spam. I have never bought a backlink, for that site or any other.

## What are spam backlinks (and toxic backlinks)?

A spam backlink is a link to your site from a domain that exists to sell links, scrape content or game rankings, rather than from a page someone wrote because your page was useful to them. Toxic backlinks are the same thing under a scarier name. A lot of SEO tools use "toxic" for it, usually right next to a button offering to fix it.

You can spot most of them without a tool. The ones that hit my sites had a few things in common:

- Machine-generated domain names stuffed with SEO words, like `keyword-rank-backlink-pro-and-keyword-rank-depot.store`.
- Cheap TLDs. On knowledgeerp.com, 365 of the 500 referring domains I reviewed were link-selling networks on `.shop`, `.store` and `.site`.
- Scraper directories with 100 million or more outbound links. Nobody picks your page out of a list that long.
- Randomized-string domains and expired-domain marketplaces, which is private blog network (PBN) territory.
- Arriving in a burst. On nomadsamor.com they started showing up in May, all at once, with nothing we published to explain it.

If you have Ahrefs, its referring domains report carries an `is_spam` flag that does most of this sorting for you. It caught 539 of the 559 domains on nomadsamor.com. It also flagged a couple of real, high-traffic sites by mistake, so treat it as a first pass and not a verdict. More on that below.

Is it worth disavowing them? Usually not. Google says it ignores most spam links, and a few junk domains are normal for any site that has been online for a while. It starts to make sense with a pattern like the one I found: hundreds of domains from one network, arriving together, and outnumbering your real links many times over. On knowledgeerp.com only about 26 of those 500 referring domains were legitimate. At that ratio a disavow file is cheap insurance. With thirty links you mostly recognize, it is a wasted afternoon.

## What the spam actually looks like

The bulk of it is one network, and it is not subtle. A sample of the domain names:

advanced-link-building-group-seoexpress.store
link-baron-luxury-anchor-text-partners.store
keyword-rank-backlink-pro-and-keyword-rank-depot.store
proven-consortium-for-ranking-signal-and-keyword-rank.store
seoexpress-verified-high-da-consultants.store

There are hundreds of these. They are machine-generated names assembled from a bag of SEO nouns, registered in bulk on cheap TLDs, filled with scraped text, and pointed at whatever list of domains the operator is working through. My sites are on the list. So is everyone else's.

Underneath that there is a second layer with a sense of humor about itself:

you-found-the-hidden-link.xyz
what-happens-next.xyz
this-is-not-what-you-think-it-is-at-all.us
selfie-battles-are-for-amateurs-tim--kalin-from-seodomains-here.com

Those are expired-domain marketplaces advertising to other SEOs. The links to my site are incidental. They scrape a page, republish it, and the outbound links come along for the ride.

Then the usual tail: scraper directories with a hundred million outbound links, a few gambling and crypto sites, an escort directory, and a domain that appears to be about Bitcoin mixing.

None of this was aimed at me. It is a blast. The same network hit all six of my sites within weeks of each other, and the per-site disavow lists came out at 540, 529, 500, 487, 485 and 243 domains.

## The part where I tell you it probably does not matter

If you search for what to do about this, most of what you will find is written by people who sell disavow services, and it is written to frighten you. The honest answer is duller.

Google has said for years that it ignores unsolicited spam links. SpamBrain handles it at their end. The whole point of a link-based ranking system that anyone can write links into is that it has to hold up against people writing links into it. If a competitor could sink your rankings by pointing 500 garbage domains at you, that would be a much bigger story than my travel blog.

So the correct expectation is that this is doing nothing to me. My rankings on those sites are held back by thin pages, almost no internal linking, and a blog competing with its own documentation for the same queries. Those are my fault and they are fixable. The spam is neither.

One number did move. Ahrefs' Domain Rating for knowledgeerp.com fell from 32 to 21 in August. It is tempting to read that as damage. It is not: DR is Ahrefs' metric, not Google's, and the most likely explanation is that Ahrefs devalued a batch of those spam domains inside its own index, so the links stopped counting toward my score. Nothing happened at Google. DR is not a ranking factor and chasing it is a good way to waste a month.

## So why did I disavow

Because it costs an afternoon and the downside is bounded.

The case for doing it is not "this will fix my rankings." It is that I own six sites with a shared brand, the profile is now overwhelmingly junk by volume, and if a manual review ever happens I would rather the record show I looked at all 559 domains and made a call on each one. The disavow file is a document about my intent as much as a technical instruction.

The case against is that a careless disavow does real damage. The file tells Google to discount those domains, and Google does not argue with you. Disavow a legitimate link by accident and you have thrown away something you earned.

That risk is the actual work.

## The classification problem

Ahrefs has an `is_spam` column. It is good. It is not sufficient.

On nomadsamor it flagged 539 of the 559 domains. Nine more were obviously link-selling by name and it had missed them: `addurl.in`, `backlinkup.co`, `openbacklink.com`, `seotira.com`, `rankongoogle.agency`. I catch those with a keyword and TLD heuristic.

It also goes wrong in the other direction, which is worse. `is_spam` flagged `za.com`, a domain with a DR of 90 and 465,000 monthly organic visits. It flagged `itxoft.com` at DR 81. Those are real sites and disavowing them would be a self-inflicted wound.

So neither method is trustworthy alone, and the rule I settled on is that they are combined and never subtracted. A domain gets disavowed if `is_spam` flags it or the heuristic flags it. On top of that sits a hand-maintained whitelist of domains that are never disavowed no matter what either method says: my own sites, and the dozen or so real third parties that keep getting caught.

The whitelist is the part worth being careful about. On the RV site it includes youtube.com, which Ahrefs correctly did not flag but a keyword rule easily could have. That is our own channel linking to our own site, the single most legitimate link in the entire profile, and an automated pass that swept it into the file would have been actively harmful while looking like a clean run.

Whatever you automate here, the whitelist survives it.

## The mechanics, which are worse than they should be

A few things I had to learn by hitting them:

There is no API. Not in Ahrefs, not in the Search Console API, nowhere. You upload a text file by hand at `search.google.com/search-console/disavow-links` and that is the only way.

The upload replaces the entire list. It is not a delta. If you upload a file with ten new domains in it, you have just disavowed ten domains and un-disavowed everything else. Always upload the complete file.

The tool does not accept Domain properties. Pick a `sc-domain:example.com` property and it tells you so in as many words: "Domain properties are not supported at this time." You need a URL-prefix property, so if you only ever verified the Domain property, add a URL-prefix property for the same site first, then come back. The disavow applies to that prefix, so a file uploaded against `https://www.example.com/` does not cover `shop.example.com`.

And a smaller one: Ahrefs' referring-domains endpoint caps at 250 rows per call regardless of the limit you ask for. The documented workaround of pulling 300 ascending and 300 descending leaves a silent hole in the middle for any site with more than 500 domains. On nomadsamor that hole was 59 domains I would never have seen. Sort, page it properly, and count what comes back.

## How to disavow spam backlinks found in Ahrefs, step by step

Here is the whole process in order, the way I would run it again.

1. **Pull every referring domain.** Get the full referring domains list for your site out of Ahrefs. If you use the API, page through it and count the rows, because a single call stops at 250.
2. **Flag the spam two ways.** Start with Ahrefs' `is_spam` flag, then add a keyword and TLD check for the link sellers it misses. A domain goes on the list if either one catches it.
3. **Apply your whitelist last.** Your own sites, your own channels and any real site that got flagged by mistake come off the list, whatever flagged them.
4. **Write the file in Google's format.** A plain .txt file with one entry per line, written as `domain:example.store` to cover a whole domain. Lines starting with `#` are comments, which is a good place to note the date and how you built the list.
5. **Upload it to a URL-prefix property.** Go to `search.google.com/search-console/disavow-links`, pick the URL-prefix property for your site (Domain properties are not supported, so add a URL-prefix property first if you don't have one), and upload.
6. **Re-upload the whole file every time.** Each upload replaces the previous list, so when new spam shows up, add it to your file and upload the complete thing again.

## How to avoid spammy backlink marketplaces

Every domain in that second layer, the ones with names like `you-found-the-hidden-link.xyz`, is a backlink marketplace, a shop window for someone selling links or expired domains to other SEOs. I never bought from any of them, but they are exactly what turns up when you go looking for backlinks to buy. If you are tempted, here is what I would check first:

- **Look at the seller's inventory in a backlink tool.** If their sites look like the lists in this post, keyword-stuffed names on `.store` and `.shop`, that is what you are paying for. Google can see the pattern as easily as you can.
- **Be wary of anything priced by DR or DA.** Those are third-party scores (DR is Ahrefs' metric, not Google's), and they are easy to inflate with exactly the kind of links described here.
- **Check for real organic traffic.** A domain with a high rating and almost no visitors exists to be sold.
- **Skip bulk and "permanent" link packages.** Hundreds of links from unrelated sites landing at once is the burst pattern that makes a profile look like mine.
- **Know the rules.** Buying links to move rankings is against Google's spam policies. The links worth having are the ones someone gives you because they wanted to point at your page.

For comparison, the real links to knowledgeerp.com came from places like G2, SaaSHub and AlternativeTo. Fewer links, all from sites a person would actually visit.

## What I would tell someone in the same position

Check whether you actually have this problem before you spend a day on it. Pull your referring domains and look at them. If the answer is thirty domains and you recognize most of them, close the tab.

If it is five hundred domains and they all end in `.shop`, you have the same blast I have. Write the file, keep a whitelist you maintain by hand, upload it, and then go fix your internal linking, because that is the thing that is actually costing you traffic.

The disavow is insurance. It is cheap, it is worth having, and it is not the fix.

This is the second time I have gone looking for an expensive problem and found a boring one. The first was when I measured where my AI budget actually goes and got it wrong four separate ways.

## Update, October 2026

The spam kept coming. Between August 26 and September 29, 2026, Ahrefs showed 607 new referring domains pointing at this site, nathanpelton.com, all flagged as spam by its `is_spam` column. About 350 of them showed up in one burst on September 27 to 29.

This site is the 243 in that list of six. I added the new domains to its file, which took it from 243 domains to 850, and uploaded the complete file to Search Console on October 6, 2026. Search Console confirmed it: 850 domains.

Nomads Amor, the RV site this post started with, got the same wave: 608 new spam domains. Its file went from 540 domains to 1,148.

That is step 6 from the list above in practice. The file only grows, and every upload is the whole thing.

## Spam backlinks and disavowing: common questions

## What are toxic backlinks?

Links to your site from domains that exist to sell links, scrape content or manipulate rankings. "Toxic backlinks" and "spam backlinks" mean the same thing. Common signs are keyword-stuffed domain names on cheap TLDs like `.shop` and `.store`, scraper directories with millions of outbound links, and hundreds of new referring domains arriving in a short burst.

## Does Google penalize spam backlinks?

Google says its systems ignore most spam links rather than counting them against you, so links you never asked for normally do nothing. The real risk is links you bought or arranged yourself, which break Google's spam policies. Disavowing is a precaution for large spam patterns, not a routine chore.

## How do I disavow links I found in Ahrefs?

Ahrefs can't submit anything to Google for you. Export your referring domains, flag the spam (Ahrefs' `is_spam` flag plus your own review), take out a hand-kept whitelist of real sites, and write the rest into a .txt file as `domain:example.store` lines. Then upload that file at `search.google.com/search-console/disavow-links`. Each upload replaces the last one, so always upload the complete file.

## Can I use a Domain property with Google's disavow tool?

No. Google's disavow tool says "Domain properties are not supported at this time." Add a URL-prefix property for your site in Search Console (for example `https://www.example.com/`), verify it, and upload the file there. It only covers that prefix, so a subdomain with its own property needs its own upload.
