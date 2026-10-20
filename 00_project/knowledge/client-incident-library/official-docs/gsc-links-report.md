# Links report

- URL: https://support.google.com/webmasters/answer/9049606?hl=en
- Fetched: 2026-10-12
- Page date: living help page (no date shown)
- Author/site: Google (support.google.com help center)

---

See who links to you the most, your top-linked pages, and more.


**What's a backlink?**A backlink is a link on a page from another site that links to a page on your site. It

*links back*to your site.


**Some notes about the data:**

- Pages on your site are grouped by canonical URL. This means that the anchor tags and possibly some parameters are omitted before grouping.
- Duplicate links are combined. A duplicate link is a link from the same source URL to the same target URL, after removal of all parameters and other normalization. In the link text report, duplicates are based on link text not URL.
- Tables are limited to 1,000 rows, so tables may be truncated in larger or more linked-to sites.
- This report isn't a comprehensive list of every link on your site. It shows a sample of internal and external links to help you understand your site’s overall link profile. Some URLs might be omitted for various reasons, such as non-indexed pages or deduped URLs.
- Although the report uses the term "site", data is actually grouped by root domain in the Links report; protocol (http/https), subdomain (m., www) and subdirectories are stripped and grouped together. Therefore, all the following are grouped under `example.com`:
  - `example.com`
  - `m.example.com`
  - `example.com/pet_store/`
  - `https://example.com`
  - `http://example.com`
- TLDs (top level domains) are *not* omitted when grouped and displayed, so the following are NOT identical:
  - `example.com`
  - `example.com.de`
- "External sites" or links are anything outside of your current property.
- The report includes links that Google has found over time. These links may have since been removed, or a page may no longer exist. The report doesn’t specify if a link is marked as `nofollow`.

**This report has the following information:**

### External links

These are links outside your site:

See which of your pages have the most backlinks from other sites. Use this to see if you're getting the recognition that you think you deserve.

### To navigate there

**Links report > External links > Top linked pages**

Click the **MORE** link at the bottom of the table for the full list. Select a URL in the list to see the top sites linking to that page. Sites are shown by their root domain, with any subdomain omitted (so `www.example.com` would show as `example.com`).

### Uses for this report

- Confirm that your most linked pages are the ones that you expect.

See which sites contain the most backlinks to your site.

This report shows the root domain of sites with the most links to your site, sorted by count of links. Sites are shown by their root domain, with any subdomain omitted (so `www.example.com` would show as `example.com`).

If you see a domain listed that is identical to your property, it is because it represents a subdomain that is omitted in the table. For example, if a link comes from `m.example.com`, the table entry will be `example.com`.

### To navigate there

**Links report > External links > Top linking sites**

Click the **MORE** link at the bottom of the table for the full list. Click a site in the list to see your most linked pages from that site.

Sites are shown by their root domain, with any subdomain omitted (so `www.example.com` would show as `example.com`).

### Uses for this report

- Confirm that you recognize the sites listed here. If you see any unknown and possibly spammy sites, you might need to ask to be removed or, if all else fails, disavow them to avoid having your ranking harmed by known spammy sites.
- See whether sites that are important to you point to your site. For example, if you have a restaurant website, are you mentioned in food blogs or review sites?

See which link text is used in backlinks to your site. Covers only links from outside your property.

Duplicates are combined, where a duplicate is a case-insensitive exact match. So "Hello world" and "HELLO WORLD" are duplicates, but "Hello world" and "Hello worlds" are not duplicates.

Links with no text (for example, image links) are shown as "(empty)" in the Link Text column on the report, and as empty rows in the exported data.

Link text is grouped by exact match and sorted by count. Sites are shown by their root domain, with any subdomain omitted (so `www.example.com` would show as `example.com`).

### To navigate there

**Links report > External links > Top linking text**

Click the **MORE** link at the bottom of the table for the full list.

### Uses for this report

- Confirm that the link text is what you expect, and not spammy text.
- Confirm that other sites are describing your site accurately. If not, you might need to clarify your site content.

See how many backlinks you get from a given site for a given page. You can only see this for a page that appears in the Top Linked Pages table.

### To navigate there

**Links report > External links > Top linked pages > MORE > *URL of page to filter by***

### More detail

Click a site in **Top sites linking to this page** to see a list of pages on that site that link to the selected page.

Sites are shown by their root domain, with any subdomain omitted (so `www.example.com` would show as `example.com`).

### Uses for this report

- If the linking site is good, see which pages are benefiting from that site.
- If the linking site is spammy, try to get these pages unlinked from this site. For known spam sites, Google typically will ignore the links, but you might want to remove or disavow these links.

See backlinks from a specific site to a specific page on your site.

### To navigate there

You can navigate here in two ways, either through the target page or through the linking site:

**Through the target page:**

- **Links report > External links > Top linked pages > MORE > *URL of page to examine > URL of site to filter by***

**Through the linking site:**

- **Links report > External links > Top linking sites > MORE > *URL of site to filter by* > *URL of page to filter by***

Sites are shown by their root domain, with any subdomain omitted (so `www.example.com` would show as `example.com`).

### 

The table includes the following columns:

- **Linking page:** The page that has a link to the target page on your site.
- **Target URL (if different):** If no value is shown, it means that the link URL on the linking page is identical to the URL of the target page. If a value **is shown**, it means that the link URL on the linking page is different from the URL of the target page. Here are two reasons why the link URL might not be the target page URL:
  - Your site redirects visitors from the link URL to the target URL. For example, your site might redirect users from `example.com/old_page` to `example.com/replacement_page`. You can test this by visiting the linking page and clicking this link, and tracking the redirects.
  - Google has decided that the canonical URL for **URL on linking page** is the target URL. In this case, if you visit the linking page and click the link, you would (probably) reach the actual link URL. However, if you do a Google search for **URL on linking page** and click the result, you would be redirected you to the (canonical) target URL.

### Uses for this report

- Track down how users get from a given site to a given page.

### Internal links

These are links within your own site to your own site:

See which of your pages is linked the most from within your own site.

### To navigate there

**Links report > Top internally-linked pages table**

### For more detail

Select a URL in the list to see which of your other pages link to it.

### Uses for this report

- Confirm that the core site pages (home page, contact page) are properly linked within your site.

See which pages on your site link to a specific page.

### To navigate there

**Links report > Internal links > Top linked pages > MORE > *URL of page to filter by***

### Uses for this report

- Clean up the traffic flow within your site by confirming that users can get from page A to page B with the fewest clicks.

You can export your link data as a CSV file or a Google Sheet.

### Landing page

Export up to 100,000 rows of data using the **Export** button. The following data slices are available:

- **Latest links**
The**most recently discovered links to your site** (up to 100,000 rows), sorted by discovery date.
- **More sample links**
A**sample of links to your site** (up to 100,000 rows), extracted from the full set of links known to Google. This is useful when you have many more than 100,000 pages linking to your site, because it shows some data truncated by the **Latest Links** export due to length limits.

### Single-table pages

Pages containing a single table offer a download button to export the entire table (up to 1,000 rows).The table sorting on the page does not affect the exported data.
