# Manual actions report

- URL: https://support.google.com/webmasters/answer/9044175?hl=en
- Fetched: 2026-10-12
- Page date: living help page (no date shown)
- Author/site: Google (support.google.com help center)

---

See if your site has any manual actions issued against it and view the site's manual action history.

**If a site has a manual action, some or all of that site will not be shown in Google search results.**

Open the Manual actions report


Manual Actions report in Search Console - Google Search Console Training

## What is a manual action?

Google issues a manual action against a site when a human reviewer at Google has determined that pages on the site are not compliant with Google's spam policies. Most manual actions address attempts to manipulate our search index. Most issues reported here will result in pages or sites being ranked lower or omitted from search results without any visual indication to the user.

If your site is affected by a manual action, we will notify you in the Manual actions report and in the Search Console message center.

**Why do manual actions exist?**

Ever since there have been search engines, there have been people dedicated to tricking their way to the top of the results page. This is bad for searchers because more relevant pages get buried under irrelevant results, and it's bad for legitimate websites because these sites become harder to find. For these reasons, we've been working since the earliest days of Google to fight spammers, helping people find the answers they're looking for, and helping legitimate websites get traffic from search.

Google is constantly working to improve search. We take a data-driven approach and employ analysts, researchers, and statisticians to evaluate search quality on a full-time basis. Changes to our algorithms undergo extensive quality evaluation before being released. More information about our algorithm.

Our algorithms are extremely good at detecting spam, and in most cases we automatically discover it and remove it from our search results. However, to protect the quality of our index, we're also willing to take manual action to remove spam from our search results.

## Do I have any manual actions against my site?

You'll see a count of manual actions against your site at the top of the report. If your site has no manual actions, you'll see a green check mark and an appropriate message.

If you recently bought a site that violated our spam policies before you owned it, fix the issues listed in this report, then let us know in your reconsideration request that you recently acquired the site and that it now no longer violates the policies.

## What pages are affected?

Expand the manual action description to see a list of patterns of affected pages. This can be a subset of your site, or the entire site. Not all of the pages matching the pattern are necessarily affected.

**Example:**

- `https://example.com/real-estate/*` – some or all pages under the `real-estate/` directory are affected.
- **Affects all pages** – Manual actions with this description affect the entire site.

## How do I fix the problem?

**To fix a manual action on your site:**

1. Expand the manual action description panel on the report for more information.
2. See which pages are affected.
3. See the type and short description of the issue, and follow the "Learn more" link to see detailed information and steps to fix the issue. (You can find the detailed information for each action below on this page).
4. Fix the issue on *all affected pages***.** Fixing the issue on just some pages will not earn you a partial return to search results. If you have multiple manual actions on your site, read about and fix all of them.
5. Be sure that Google can reach your pages; affected pages should not require a login, be behind a paywall, or be blocked by robots.txt or a noindex directive. You can test accessibility by using the URL Inspection tool.
6. When **all issues** listed in the report are fixed in **all pages**, select **Request Review** in this report. In your reconsideration request, describe your fixes. A good request does three things:
  - Explains the exact quality issue on your site.
  - Describes the steps you've taken to fix the issue.
  - Documents the outcome of your efforts.
7. Reconsideration reviews can take some time (see below). You will be informed of progress by email. You will get a review confirmation message when you send your request, to inform you that the review is in progress; don't resubmit your request before you get a final decision on your outstanding request.

## How long will my reconsideration review take?

Most reconsideration reviews can take several days or weeks, although in some cases, such as link-related reconsideration requests, it may take longer than usual to review your request. You will be informed by email when we receive your request, so you'll know it is active. You will also receive an email when the review is complete. Please don't resubmit your request before you get a decision on any outstanding requests.

## List of manual actions

Here are the manual actions that can be applied by Google and how to fix them.

## Back button hijacking

Google has detected that a portion of your site may exhibit back button hijacking behavior, which violates our spam policy on <u>malicious practices</u>.

Back button hijacking is when a site interferes with the user's browser navigation by manipulating the browser history or other functionalities, preventing them from using their back button to immediately get back to the page they came from.

The current manual action affects pages with content that violates our policy. If your site repeatedly violates our back button hijack policy, this may lead to further manual actions and affect your site’s overall ranking.

### **Recommended actions:**

Review Google’s spam policy on <u>malicious practices</u>, then follow these steps to identify and correct the violation(s) on your site:

1. Disable or remove any code or imports that are responsible for back button hijacking.
2. Click <u>Request review</u> in the <u>Manual actions report</u> once you're sure your site is no longer violating our spam policies.
3. Watch for review status messages in your Search Console account—we’ll let you know when we’ve reviewed your site. If we determine that your site is no longer violating our spam policies, we’ll revoke the manual action.

### Recommended actions

Review Google's Spam policies on user-generated spam, documentation on preventing comment spam and free host spam, and how to fix hacked pages, then follow these steps to identify and correct the violation(s) on your site:

1. Identify pages on your site where users, visitors, or other third-parties could add content or interact with: these could be your forums, guestbooks, social media platforms, file uploader, free hosting services, or internal search pages that users can send queries to.
2. Review the example URLs in the messages you received in the Search Console Messages center or by email to gain a better sense of where the spammy content appears. In addition, please search your site for unexpected or spammy content using the "site:" operator in Google search, adding commercial or adult keywords that are unrelated to your site's topic. For example, search for \[site:*your-domain-name* viagra\] or \[site:*your-domain-name* free movie watch online\] to detect the irrelevant content on your site. Search for things such as:
  - Out-of-context text or off-topic links with the sole purpose of promoting a third-party website or service (for example, "Free movie download" or "watch online”)
  - Gibberish or text that appears to be auto-generated
  - Comments or information submitted by users with unrealistic, commercial-sounding keywords; that is, user names like "Discount Insurance" that don't sound like real usernames and link to unrelated sites
  - Internal search results where the user's query appears geared at promoting a third-party website or service
3. Monitor your web server log files for sudden unexpected or unexplained traffic spikes, especially for newly created pages. Look for any URLs with keywords in URL patterns that are completely irrelevant to your website. You can see your top clicked pages in Google Search by using the Performance report for Search.
4. Remove any inappropriate content and block obviously inappropriate third-party content from being published to your platform with a list of spammy terms (such as streaming, download, adult, gambling, or pharma terms).
5. Where appropriate, use these guides:
6. Consider consolidating your interactive content into a concentrated file path for easier maintenance and spam detection.
7. When you're sure that your site is no longer in violation of our spam policies, select **Request Review** on the Manual Actions report.
8. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.
9. In the meanwhile, it is also recommended to continue actively monitoring and cleaning up such spammy content, improve your site's system and fix system vulnerability to prevent such spam in the future.

Google has detected spam on your pages submitted by site visitors. Typically, this kind of spam is found on forum pages, guestbook pages, or in user profiles.

Matt Cutts explains the "User-Generated Spam" manual action

### Recommended actions

Review the Google's policies on user-generated spam, then follow these steps to identify and correct the violation(s) on your site:

1. Users commonly add content to sites in forums, blog comments, and user profiles. Identify pages on your site where users could have added content.
2. Look for profiles with commercial usernames like "Discount Insurance” or posts with advertisements, off-topic links, or gibberish text. Check these areas for the following:
        
  - Posts or profiles that look like advertisements
  - Posts or profiles with out-of-context or off-topic links
  - Posts or profiles with commercial usernames — names like "Discount Insurance," that don't sound like real human names — that link to unrelated sites
  - Posts or profiles that appear to be automatically generated (not written by a real user)
3. Search your site for unexpected or spammy content using the `site:` operator in Google search, adding commercial or adult keywords that are unrelated to your site's topic. For example, search for \[site:example.com viagra\] to search for the term "viagra" on your site.
4. Remove any inappropriate content.
5. Consider implementing measures to prevent user-generated spam.
6. When you're sure that your site is no longer in violation of our spam policies, select **Request Review** on the Manual Actions report.
7. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

A significant fraction of sites hosted on your free web hosting service are spammy.

Google tries to be precise when taking manual action related to spam. However, if a significant fraction of the pages on a given web hosting service are spammy, we may take manual action on the whole service.

### Recommended actions

1. Get tips for preventing and identifying abuse of your service.
2. Remove any existing spammy accounts from your service.
3. Contact the technical team at your hosting service and tell them about the manual action.
4. When you're satisfied that your site follows our spam policies, select **Request Review** on the Manual Actions report.
5. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

Google has detected that some of the markup on your pages may be using techniques that are outside our structured data guidelines, for example: marking up content that is invisible to users, marking up irrelevant or misleading content, or other manipulative behavior.

Here are some of the structured data issues that might apply to your site:

| Title | Description | 
|---|---|
| Content on page differs from structured data | JobPosting structured data found on pages that don't have job posting content. This is against our guidelines. Learn more | 
| Can't submit application on job offer page | Content on pages found to be different than structured data on the page. This is against our guidelines. Learn more | 
| Structured data does not match content | Content on pages found to be different than structured data on the page. This is against our guidelines. Learn more | 
| Job application requires payment | Pages with JobPosting structured data charge a fee to apply for the job. This is against our guidelines. Learn more | 
| Job request found on job offer pages | Pages with JobPosting structured data are seeking a job, not offering a job. This is against our guidelines. Learn more | 
| Misleading job location | Pages with JobPosting structured data include a misleading job location field. This is against our guidelines. Learn more | 
| Job poster not hiring | Pages with JobPosting structured data are collecting applications but not hiring. This is against our guidelines. Learn more | 
| Structured data issues on list page | Pages with a list of items need to have each item marked up individually. Aggregating data from multiple items into one structured data element is against our spam policies. Learn more | 
| JobPosting structured data on listing page | A list page should not include structured data for individual jobs. Learn more | 
| JobPosting structured data on expired job | JobPosting markup used on an expired job without the validThrough Property set in the past. Learn more | 
| Content on page differs from structured data | ClaimReview structured data found on pages that don't contain a claim review. This is against our guidelines. Learn more | 
| ClaimReview lacks reference, or reference does not match verdict | Pages with ClaimReview structured data do not include a supporting source or reference. This is against our guidelines. Learn more | 
| Structured data found on hidden content | Structured data found on elements that are not visible to the user. This is against our guidelines. Learn more | 
| No mechanism for submitting a new review | If a page includes a review, the page must also provide a way to provide a review or clearly show where the reviews come from. Learn more | 
| Company marked as product | A company has been labeled as a product in structured data. Learn more | 
| Non-product labeled as product | A non-product, or generic item, has been marked as a product. Learn more | 
| Review written by the site or person providing the service | Reviews must not be written or provided by the business or content provider unless they are customer, independent, and unpaid editorial reviews. Learn more | 
| Event structured data is actually a promotion | The visible text or structured data description is more concerned with promoting or selling the event than describing it. Learn more | 
| Non-event labeled as an event | A non-event item has been marked as an event. For example, a holiday or a coupon. Learn more | 
| Non-recipe marked as a recipe | A non-recipe item has been marked as a recipe. A recipe must be for a food item and include both ingredients and steps. Learn more | 
| Structured data policy violation | You have a structured data policy violation on one or more pages. Learn more | 
| Incorrect Employer | The employer in the hiringOrganization field should match the employer in the job posting. Learn more | 
| Incomplete Job Description | The description field is incomplete or unintelligible. Learn more | 

### Recommended actions

1. Make sure that the markup on your site meets Google's structured data guidelines if you would like it featured in Google search results. This might require updating existing markup or removing any markup that violates our guidelines.
2. When you've made these changes, select **Request Review** on the Manual Actions report.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our guidelines, we'll revoke the manual action.

***to***your site

Google has detected a pattern of unnatural, artificial, deceptive, or manipulative links pointing to your site. Buying links or participating in link schemes in order to manipulate ranking in Google Search results is a violation of our spam policies. This can result in some or all of your site getting a manual action.

Matt Cutts and Alex explain the "Unnatural links to your site" manual action

### Recommended actions

First, review Google's link spam policy.

Next, follow the steps below to identify and correct the violation(s):

1. Download a list of links to your site from Search Console. You can download your links arranged either by hostname (**Top linking sites > Export**) or in chronological order (Links report > **Export external links > Latest links**).
2. Check this list for any links that violate our link spam policy. If the list is large, start by looking at the sites that link to you the most, or links that were created recently (in the last few months).
3. For any links that violate our spam policies, contact the owner of that site and ask that they either remove the links or prevent them from passing PageRank, such as by adding a rel=”nofollow” or a more specific attribute.
4. Use the Disavow links tool in Search Console to disavow any links that you could not get removed. We often see the Disavow links tool used incorrectly so **keep the following things in mind when using the tool**:
  - If you can get a backlink removed, make a good-faith effort to remove the link first. Blindly adding all backlinks to the disavow file is not considered a good-faith effort, and will not be enough to make your reconsideration request successful.
  - For multiple links from the same domain to your site, use the "domain:" operator in the disavow file for convenience.
  - Make sure that you don't disavow organic links to your site.
  - Simply disavowing all backlinks without attempting to remove them might lead to rejection of your request.
5. When you've removed or disavowed the artificial links, select **Request Review** on the Manual Actions report. Include documentation about the links you've had removed and an explanation of any links you were unable to remove, to help us process your request.
6. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

***from***your site

Google has detected a pattern of unnatural artificial, deceptive, or manipulative outbound links on your site. Buying links or participating in link schemes in order to manipulate ranking in Google Search results is a violation of Google's spam policies.

Matt Cutts and Sandy discuss the "Unnatural links from your site" manual action.
### Recommended actions

First, review Google's link spam policy.

Next, follow the steps below to identify and correct the violation(s) on your site:

1. Identify any links on your site that were paid for or that appear to violate our link spam policy, such as excessive link exchanges.
2. Either remove these links, or change them so that they no longer pass PageRank, for example by adding a rel=”nofollow” or a more specific attribute, or by redirecting them through a page blocked by robots.txt.
3. When you're sure that your site is no longer in violation of our spam policies, select **Request Review** on the Manual Actions report. Provide examples of bad content that you removed and good content that you added.
4. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

Google has detected low-quality pages or shallow pages on your site. Here are a few common examples of pages that often have thin content with little or no added value:

- Thin affiliate pages
- Content from other sources. For example: scraped content or low-quality guest blog posts
- Doorways

These techniques don't provide users with substantially unique or valuable content, and are in violation of our spam policies.

Matt Cutts explains the "Thin Content with little or no added value" manual action.

### Recommended actions

First, review the following sections of our spam policies:

Next, follow the steps below to identify and correct the violation(s) on your site:

1. Check for content on your site that duplicates content found elsewhere.
2. Check for thin content pages with affiliate links on your site.
3. Check for doorway pages on your site.
4. If your site contains any of these types of content, think about whether your site provides significant added value for your users. 
*Tip: Consider asking friends or family — real people not affiliated with your site — to use or critique your site to get ideas for improving it.*
5. Improve your website so that it provides significant value for your users.
6. When you're sure that your site is no longer in violation of our spam policies, select **Request Review** on the Manual Actions report. Provide examples of bad content that you removed and good content that you added.
7. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

Your site may be showing different pages to users than are shown to Google, or redirecting users to a different page than Google saw. Cloaking and sneaky redirects are a violation of Google's spam policies.

**Subscription and paywalled content:** Publishers should enclose paywalled content with structured data in order to help Google differentiate paywalled content from the practice of cloaking, where the content served to Googlebot is different from the content served to users.

### Recommended actions

First, review Google's spam policies on cloaking and sneaky redirects.

Next, follow the steps below to identify and correct the violation(s) on your site:

1. Use the URL Inspection tool in Search Console to fetch pages from the affected area of your site.
2. Compare the content fetched by Google to the content seen by a human user (you!) when visiting the site.
3. If the content differs, identify and remove the part of your site that's serving different content to Google and users. This will require looking through your site's code on the server.
4. Check for URLs on your site that redirect users to somewhere other than where they expected to go.
5. Check for URLs on your site that redirect conditionally, for example that redirect only users coming from Google search, or only users coming from a particular range of IP addresses.
6. If your site redirects users in any of these ways, identify and remove the part of your site that generates these redirects. This will require looking through your site's code on the server.
*Tip: These types of redirects are often written in JavaScript or in your .htaccess file. You might also check your content management system and any plugins.*
7. When you're sure that your site is no longer in violation of our spam policies, select **Request Review** on the Manual Actions report.
8. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

The site appears to use aggressive spam techniques such as scaled content abuse, cloaking, and/or other repeated or egregious violations of Google's spam policies.

### Recommended actions

1. Update your site so that it no longer violates Google's spam policies.
2. When you're sure that your site is no longer in violation of our spam policies, select **Request Review** on the Manual Actions report. Provide examples of bad content that you removed and good content that you added.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

Some of your site's images may display differently in Google's search results than when viewed on your site. *Cloaking* is the practice of presenting different content to human users than to search engines. Cloaking is considered a violation of Google's spam policies because it provides our users with different results than they expected. Cloaking images can provide a bad user experience for Google image search results, as obscured images and mismatched thumbnails do not present the user with the image that they are searching for.

**Examples of cloaked images**

Here are some examples of image cloaking behavior:

- Serving images to Google that are obscured by another image, for example: a block of text blocking an image.
- Serving images to Google that are different than the image served to a page visitor.

**If you need to block images from Google search results**, use the method described below.

### Recommended actions

1. Ensure that your site displays exactly the same images to users on your site and in Google search results. Cloaking is acceptable only for opting out of image search inline linking as detailed below.
2. When you're sure that your site's images are exactly the same whether viewed directly on your site or from Google search results, select **Request Review** on the Manual Actions report.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account; we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.


**Minimize or block an image in search results**

- To prevent the **full-sized image** from appearing in the Google search results, **opt out of inline linking**.
- To **prevent the image from appearing at all** in search results, follow these steps.


**To opt out of inline linking:**

1. When your image is requested, examine the HTTP referrer header in the request.
2. If the request is coming from a Google domain, reply with HTTP 200 or 204 and no content.

Google will still crawl your page and see the image, but will display a thumbnail image generated at crawl time in search results. This opt-out is possible at any time, and does not require re-processing of a website's images. This behavior is not considered image cloaking and will not result in a manual action.

Some of your pages may contain hidden text or keyword stuffing, techniques that are not allowed by Google's spam policies.

### Recommended actions

First, review Google's spam policies on hidden text and keyword stuffing.

Next, follow the steps below to identify and correct the violation(s) on your site:

1. Use the URL Inspection tool in Search Console to check for content that's visible to our crawler but isn't visible to a human user (you!) when visiting the site.
2. Check for text that's the same, or similar, color as the background of the webpage.
*Tip: You can often reveal such text by selecting all the text on the page, for example by pressing Ctrl + A or Command + A.*
3. Check for any text hidden using CSS styling or positioning.
4. Remove or re-style any hidden text so that it's equally discoverable by search engine crawlers and by human users.
5. Check for lists or paragraphs of repeated words without any context.
6. Check `<title>` tags and alt text for strings of repeated words.
7. Remove any such words or other instances of keyword stuffing.
8. When you're sure your site is no longer in violation of our spam policies, select **Request Review** on the Manual Actions report.
9. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

There is a difference in content between the AMP version and its canonical web page.

The content of the AMP version and its canonical web page should be essentially the same. The text need not be identical, but the topic should be the same, and users should be able to accomplish the same tasks on both the AMP and the canonical page.

AMP pages affected by this manual action will not be shown in Google Search: the canonical page will be shown instead.

### Recommended actions

1. Ensure that the AMP is referencing the correct canonical web page.
2. Ensure that the general content of the AMP and canonical page are the same.
3. Check that Google's view of the page is not different from the user's view of the page by using the URL Inspection tool for both the AMP and the canonical page. A mismatch can occur when a robots.txt file blocks significant resources on one or the other. Blocked resources will also be shown in the URL Inspection tool.
4. When your AMP and canonical pages are essentially the same, select **Request Review** on the Manual Actions report.
5. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

Some pages on this site appear to be redirecting mobile device users to content not available to search engine crawlers. These sneaky redirects are a violation of Google spam policies. To ensure quality search results for our users, the Google Search Quality team can take action on such sites, including removal of URLs from our index.

### Overview

In many cases, it is okay to show slightly different content on different devices. For example, optimizing for the smaller space of a smartphone screen can mean that some content, like images, need to be modified. Similarly, for mobile-only redirects, redirecting mobile users to improve their mobile experience (like redirecting mobile users from example.com/url1 to m.example.com/url1) is often beneficial to them. However, redirecting mobile users sneakily to different content is bad for the user experience.

**A frustrating experience:**The same URL shows up in search result pages on desktop and on mobile. However, when a user clicks on this result on their desktop computer, they visit URL A, but users clicking on the same result on a smartphone are redirected to unrelated URL B.

Sneaky mobile redirects can be created intentionally by a site owner, but we've also seen situations where mobile-only sneaky redirects happen without the site owner's knowledge. The following are examples of configurations that can cause sneaky mobile redirects:

- Adding code that creates redirection rules for mobile users
- Using a script or element to display ads and monetize content that redirect mobile users
- A script or element added by hackers that redirects your mobile users to malicious sites

### Recommended actions

1. **If you are not engaging in this behavior intentionally:**
  1. **Make sure that your site is not hacked** Check the Security Issues report to see if Google thinks you have been hacked.
  2. **Audit third-party scripts/elements on your site** If your site is not hacked, then we recommend that you take the time to investigate if third-party scripts or elements are causing the redirects. You can follow these steps: 
    1. Remove any third-party scripts or elements you do not control from the redirecting page(s) one by one.
    2. After removing each script or element, check your site behavior on a mobile device or in Chrome mobile emulator (or any other emulator) to see if the redirection stops.
    3. If you think a particular script or element is responsible for the sneaky redirect, consider removing it from your site and possibly debugging the issue with the script or element provider.
2. **If you are engaging in this behavior intentionally:**
Fix your pages.
3. **Confirm your fix** by visiting your pages from Google search results with a smartphone or in a mobile device emulator.
4. When the issue is fixed on all pages in your site, select **Request Review** on the Manual Actions report.
5. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our spam policies, we'll revoke the manual action.

### Avoiding sneaky mobile redirects in the future

To diminish the risk of unknowingly redirecting your own users, be sure to choose advertisers who are transparent on how they handle user traffic. If you are interested in building trust in the online advertising space, you should research industry-wide best practices when participating in ad networks. For example, the Trustworthy Accountability Group's (Interactive Advertising Bureau) Inventory Quality Guidelines are a good place to start. There are many ways to monetize your content with mobile solutions that provide a high quality user experience. Be sure to use them.

To check for sneaky mobile redirects on your site, walk through the following steps:

1. **Check if you are redirected when you navigate to your site on your smartphone** We recommend you check the mobile user experience of your site by visiting your pages from Google search results with a smartphone. When debugging, mobile emulation in desktop browsers is handy because you can test for many different devices. You can, for example, view pages as a mobile device straight from your browser in Chrome, Firefox or Safari (for the latter, make sure you have enabled the "Show Develop menu in menu bar” feature).
2. **Listen to your users** Your users can see your site in different ways than you. It's always important to pay attention to user complaints, so you can hear of any issue related to the mobile user experience.
3. **Monitor your mobile users in your site's analytics data** Unusual mobile user activity can be detected by looking at some of the data in your website's analytics data. For example, keep an eye on the average time spent on your site by your mobile users: if all of a sudden, only your mobile users start spending much less time on your site than they used to, there might be an issue related to mobile redirections. Monitoring for any large changes in your mobile user activity can help you proactively identify sneaky mobile redirects. You can set up Google Analytics alerts that will warn you of sharp drops in average time spent on your site by mobile users or drops in mobile users. While these alerts do not necessarily mean that you have mobile sneaky redirects, it's something worth investigating.

You have violated content policies for Google News and/or Discover. The following sections describe the type of violation.

**Recommended actions**

1. Review and update your pages to comply with the policy by removing the dangerous content. (News policy / Discover policy)
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your site so that it clearly discloses any financial or otherwise meaningful relationships with governments and political interest groups. You may want to review who has access to your site's analytic, content management, and ecommerce systems, and decide whether those parties should be mentioned on your site as stakeholders.
2. When you're sure that your site is no longer in violation of our guidelines, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial guidelines and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our guidelines, we'll revoke the manual action.

**Recommended actions**

1. Review and update your site so that it clearly discloses any financial or otherwise meaningful relationships with governments and political interest groups. You may want to review who has access to your site's analytic, content management, and ecommerce systems, and decide whether those parties should be mentioned on your site as stakeholders.
2. When you're sure that your site is no longer in violation of our guidelines, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial guidelines and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our guidelines, we'll revoke the manual action.

**Recommended actions**

1. Review and update your site to clearly disclose the satirical nature of your site or provide evidence that disclosing accurate identities would create a personal security risk.
2. When you're sure that your site is no longer in violation of our guidelines, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial guidelines and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our guidelines, we'll revoke the manual action.

**Recommended actions**

1. Review and update your site so that it clearly discloses any financial and editorial relationships with governments and political interest groups or provide evidence that this disclosure would create a personal security risk.
2. When you're sure that your site is no longer in violation of our guidelines, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial guidelines and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our guidelines, we'll revoke the manual action.

**Recommended actions**

1. Review and update your site so that it clearly clearly discloses an accurate location or locations for your organization or provide evidence that this disclosure would create a personal security risk.
2. When you're sure that your site is no longer in violation of our guidelines, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial guidelines and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our guidelines, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the policy by removing the harassing content. (News policy / Discover policy)
2. When you're sure that your site is no longer in violation of policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the policy by removing the hateful content. (News policy / Discover policy)
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the policy by identifying media manipulation, disclosing satirical or parody intent, or removing misleading content that significantly undermines participation or trust in civic or electoral processes. (News policy / Discover policy)
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the policy by removing the medical content. (News policy / Discover policy)
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the Discover policy by removing the misleading content.
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the policy by removing the sexually explicit content. (News policy / Discover policy)
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the policy by removing the terrorist content. (News policy / Discover policy)
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the News policy by providing clear dates, non-generic information about authors, the publication, the publisher, editorial board, company or network behind it, and non-generic contact information.
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the policy by removing the violent or gory content. (News policy / Discover policy)
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

**Recommended actions**

1. Review and update your pages to comply with the policy by removing the offensive content. (News policy / Discover policy)
2. When you're sure that your site is no longer in violation of our policies, select Request Review on the Manual Actions report and provide evidence of changed editorial practices including new editorial policies and an editorial board with a history of improved practices.
3. After you've submitted a reconsideration request, be patient and watch for review status messages in your Search Console account — we'll let you know when we've reviewed your site. If we determine that your site is no longer in violation of our policies, we'll revoke the manual action.

## Site reputation policy

Google has detected that a portion of your site is inconsistent with our spam policy on site reputation.

The current manual action affects pages with content that is inconsistent with our site reputation policy. However, if your site is repeatedly inconsistent with our site reputation policy, that may lead to further manual actions and/or affect your site’s overall ranking. The impact of the manual action doesn't apply to search results shown to users in the <u>European Economic Area</u> (EEA).

**If you wish to ensure consistency with this policy, you could:**


Review Google’s policy on site reputation, then follow these steps to identify and ensure consistency with the policy:

1. Look for any third-party content on your site that's inconsistent with the <u>site reputation</u> policy. To get a better sense of where the inconsistent content appears, review the list of patterns of affected pages in the message you received from Search Console (either in the Search Console Messages center, Manual Actions report, or by email).
2. Decide what to do with the inconsistent content and take action.
For example:
  - **Move the inconsistent content to a new domain.** If you link from the old site to the new site, use the <u>nofollow attribute</u> in those links. Avoid <u>redirecting URLs</u> from the old site to the new site, as redirecting may be inconsistent with the site reputation policy again.
  - **Use** `noindex` to exclude the inconsistent content from Search indexing. To make sure your noindex rule is effective, don't block that content with your robots.txt file.
  - **Redo the inconsistent conten**t as first-party content.
  - **Remove the inconsistent content** from your site.
**Caution**: Moving the content to another established site or to a subdomain/subdirectory within your site may not resolve the underlying issue:
    - **Moving to a subdomain/subdirectory** may be viewed as an <u>attempt to circumvent</u> our spam policy, which could lead to broader actions against your site in Google Search.
    - **Moving to an established site** may introduce a site reputation issue to the established site if that site has its own reputation and the third-party nature is unchanged. Note that in the EEA, failure to take these steps isn't considered an attempt to circumvent or avoid the policy in itself.
3. When you're sure that your site is no longer inconsistent with policies, select “Request Review” on the <u>Manual Actions report</u>.
4. After you’ve submitted a reconsideration request, look for review status messages in your Search Console account — we’ll let you know when we’ve reviewed your site. If we determine that your site is no longer inconsistent with our spam policies, we’ll revoke the manual action.

### What's the difference between the Manual Actions report and the Security Issues report?

There is some conceptual overlap between the Manual Actions report and the Security Issues report, so it is useful to know the difference between them:

**The Manual Actions report** lists manually detected issues with a page or site that are mostly attempts to manipulate our search index, but are not necessarily dangerous for users. Most issues reported here will result in pages or site being ranked lower or omitted from search results without any visual indication to the user.

**The Security Issues report** lists indications that your site was hacked, or behavior on your site that could potentially harm a visitor or their computer: for example, phishing attacks or installing malware or unwanted software on the user's computer. These pages can appear with a warning label in search results, or a browser can display an interstitial warning page when a user tries to visit them.
