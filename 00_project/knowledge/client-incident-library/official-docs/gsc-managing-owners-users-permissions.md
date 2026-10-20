# Managing owners, users, and permissions

- URL: https://support.google.com/webmasters/answer/7687615?hl=en
- Fetched: 2026-10-12
- Page date: living help page (no date shown)
- Author/site: Google (support.google.com help center)

---

You can be an owner or user of a property. Each of these roles has different rights and capabilities. You can grant permissions to other users only if you are a property owner.

See and manage the user list in (site) **Settings**  > **Users and permissions** in Search Console.

## Permissions

Each user for a Search Console property is assigned one of the following permissions:

- **Owner**: Has full control over properties in Search Console. Owners can add and remove other users, configure settings, view all data, and use all tools. A property must have at least one verified owner, or no users will have access to the property. There are two types of owners, both have the same permissions:
  - **Verified owner:** Someone who verified ownership of the property using a token to prove ownership (such as an HTML file uploaded to the website). To add or remove a verified owner, you must add or remove a token on the site.
  - **Delegated owner:** Someone granted ownership status by a verified owner without the use of a verification token (such as an HTML file or tag). To add or remove a delegated owner, an owner of any type simply adds or removes the new owner using the Search Console user management screen.
- **Full user**: Has view rights to all data and can take some actions.
- **Restricted user**: Has simple view rights on most data.
- **Associate**: Associates are **people** or **accounts** that can take certain actions on behalf of your site, or access certain data. Unlike site owners and users, associates can't open or view your Search Console account or data directly but they are authorized to perform other tasks. The actions and permissions vary depending on the type of association (for example, Chrome Web store). Learn more about association.

| Feature | Owner | Full user | Restricted user | 
|---|---|---|---|
| Add / remove property owners | YES |  |  | 
| Add users | YES |  |  | 
| Blocked URLs | YES | YES | YES | 
| Change of Address | YES | View only | View only | 
| Data Highlighter | YES | YES |  | 
| Disavow links | YES | YES |  | 
| Index Coverage | YES | YES | View only | 
| Link Google Analytics account | YES |  |  | 
| Link Merchant Center account | YES | YES | View only | 
| Links | YES | YES | YES | 
| Performance | YES | YES | YES | 
| Property settings (crawl rate) | YES | YES | View only | 
| Receive messages | YES | YES | YES <sup><sub>1</sub></sup> | 
| Reconsideration request | YES | YES |  | 
| Remove URLs | YES | YES | View only | 
| Rich result status reports | YES | YES | YES | 
| Share report links | YES | YES |  | 
| Shipping and returns | YES | YES |  | 
| Submit sitemap | YES | YES |  | 
| URL Inspection | YES | YES | Fetch only | 
| User administration | YES | Details | Details | 
| Verify fixes | YES | YES |  | 
| View all reports | YES | YES | YES | 


<sup>1</sup> Restricted users receive only messages that specifically affect them.

**We lost our only verified site owner!**

If the only verified owner of your site leaves your team, you should verify ownership to maintain (or regain) access to the property.

If you are taking over a site from another owner, after you verify ownership you can unverify previous owners by removing their verification token (for example, removing the HTML tag from the site, for HTML-tag-verified owners). See Add or remove owners for more information.

**Limits:**

- **Full/restricted/associate users:** A property can have a maximum of 100 non-owners.
- **Delegated owners** can be added to a property until the property reaches 500 total verified + delegated owners. That is, if a property has 200 verified owners and 300 delegated owners, no new delegated owners can be added to that property.
- **Verified owners** have no maximum per property. That is, if a property already has 500 owners of any type, you can still verify additional owners.

**You must be a property owner** (or an owner of a parent property) to add or remove another user.

### Add a new user or delegated owner

1. Open the property in Search Console.
2. Open the Users and permissions page in property settings (**Settings    > Users and permissions)**. This page is visible only if you're a property owner.
3. Click **Add user**
  1. Enter the Google Account name (email) of the new user
            
    - Users must have a valid Google Account.
    - An email group cannot be added as a user.
  2. Choose the permission level (role) to grant the user.
  3. Save your changes.

### Remove a user or delegated owner

1. Open the property in Search Console.
2. Open the Users and permissions page in property settings (**Settings > Users and permissions)**. This page is visible only if you're a property owner.
3. Select the  menu next to the user to delete and click **Remove access**. The change should take effect very quickly. If you see a notification warning that the user might regain access, this means that the user was a verified owner, and has one or more ownership tokens that might be used to regain access to this property. Remove the tokens listed in the notification to prevent the user from regaining access. You can also find this list by clicking **Unused ownership tokens** in the Users and permissions page.

### Add a verified owner

- **To add yourself** as a verified owner
  1. Follow the verification flow to prove ownership of a site.
- **To add another person** as a verified owner, you must add their personal verification token to the property:
  1. Ask the other user to start the verification flow to generate a personal token (an HTML file, HTML tag, or whatever type you want to use).
  2. Post their personal token in a place appropriate for that token(for instance, for HTML file verification, have them give you their HTML file and then upload it for them to the website).
  3. Tell the user to open the property in Search Console and click **Verify**.

### Remove a verified owner

**If all verified owners are removed**, then all remaining users and delegated owners will lose access to the property after a grace period. Data for the property will continue to be collected, but nobody will have access to it until someone verifies ownership of the property.

1. Follow the instructions for removing a delegated owner. When complete, you will be shown a popup that lists all verification tokens for this user in this property. You can also find this list by clicking **Unused ownership tokens** in the Users and permissions page.
2. The deleted owner will immediately lose access to the property.
3. Delete all verification tokens for this user in this property. If you do not delete these tokens, the removed owner will be able to re-verify ownership if they choose to (all current owners will be notified if this happens). When you remove the owner in the previous step, you will be shown the list of tokens associated with the removed owner. You can also see this list in the Unused tokens list for the property.If an owner used several verification methods, you should remove all tokens for that person.

#### Don't recognize an owner?

If you've found an owner that you don't recognize, you might have been hacked. A hacker can probably add their token back after you've removed it, so you should either visit the web.dev site and try to secure your website yourself, or else contact a website security professional to help you secure your site.

**Requirements:**

- You must be an owner to be able to change permissions of another user.
- You can change permissions for any non-verified owner.

**To change permission level for another user:**

1. Open the property in Search Console.
2. Open the Users and permissions page in property settings (**Settings > Users and permissions)**. This page is visible only if you're a property owner.
3. Select the  menu next to the user to delete and click **Change permissions**. If this option is not active, it means that the user is a verified owner; you can remove a verified owner, but not downgrade their access level.
4. Choose the new permission level and save your change. The change should take effect very quickly. If the changed user does not see the change, ask them to refresh their page in the browser.

### Determine your own permission level

- Open Settings page (click the settings icon - Find the **Ownership verification** row to see your permission. If you are an owner, you can click the row to see your verification details.

### Determine someone else's permission level

1. You must be an owner to determine someone else's access level.
2. Open the Users and permissions page in property settings (**Settings > Users and permissions)**. This page is visible only if you're a property owner.
3. Find the user that you're interested in. The **Permission** row will show each user's permission level. If the user is listed as both **Owner** and **Verified**, it means that they are a verified owner. If a user is listed as **Owner** without the word **Verified**, it means that they are a delegated owner.

If you are a verified owner, you can determine the method(s) used to verify yourself or any other verified owners.

**For yourself:**

1. Open the Ownership page in property settings (**Settings > Ownership verification**)
2. Click the **Ownership verification** row in the property settings table to see the method(s) used. To see the details about the exact tokens used, use Search Console as described below.

**For another user, or to see your own token details**:

1. Open the Users and permissions page in property settings (**Settings > Users and permissions)**.
2. Find the user that you're interested in.
3. Click the (*more* icon) next to the user that you're interested in.
4. Click **Ownership verification details** to see information about the tokens and methods used to verify this owner.

**To see the list of unused ownership verification tokens:**

1. Open the Users and permissions page in property settings (**Settings > Users and permissions)**.
2. Click **Unused ownership tokens** to see any remaining tokens for that property, and the user that they are associated with.
3. Click a token in the list for more information.

**To remove these tokens:**

<u>verify your site ownership</u>.

- **HTML file upload:** Look for the HTML file associated with the user at the root location for your site. The file will have a long alphanumeric name, and a single line of text that includes the string "google-site-verification". Remove this tag. Make sure that you remove only the tag assigned to the person you wish to remove.
- **HTML tag:** Look in the page source of your homepage for the user's tag, which looks something like this: `<meta name="google-site-verification" content="`*some value*" />
. You must remove the tag from the page source HTML. Make sure that you remove only the tag associated with the user that you wish to remove.
- **Domain name provider:** You must find and remove the DNS record associated with the user.
- **Google Analytics account:** In order to permanently disable this verification mechanism for this user, you must either switch Google Analytics accounts for this site, or else revoke edit rights given to this person in the Google Analytics account for this site. To determine which Google Analytics account is used for this site, look at the rendered source of the page (in Chrome, right-click and choose **Inspect**), and search for "UA-" or "G-" in the page code, which should correspond to your Google Analytics account.
- **Google Tag Manager account:** In order to permanently disable this verification method for this user, you must either switch Google Tag Manager accounts used on this site, or remove the person's Publish or Admin permission in the associated Google Tag Manager account.
- **Google Sites/Blogger account:** The owner of a Google Site or Blogger website will always have access to the associated property in Search Console. To completely remove access, the owner of the Google Site or Blogger website must be switched (because a Google Site or Blogger account must always have one and only one owner).

1. Open the Users and permissions page in property settings (**Settings > Users and permissions)**.
2. Click **Ownership history**.
