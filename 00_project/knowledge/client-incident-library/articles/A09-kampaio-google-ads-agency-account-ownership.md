# Google Ads Agency Account Ownership: Who Owns What, and How Exposed Are You

- URL: https://www.kampaio.com/blog/google-ads-agency-account-ownership
- Published: 2026-07-27
- Author/site: Kampaio (Google Ads software vendor)
- Fetched: 2026-10-12
- Language: en

---

# Google Ads Agency Account Ownership: Who Owns What, and How Exposed Are You

Google Ads agency account ownership hinges on one setting: who holds owner status, not who built your campaigns. If your agency created your account inside its own manager account, the agency is the owner and you are exposed. If you created the account and only linked the agency's manager account, you are in control. Check which one you are today.

## The Short Answer: You Own the Account, the Agency Gets Linked

Access levels and ownership rules below are verified against Google Ads Help on 27 July 2026.

Most owners find out which side of that line they are on during the week they try to leave, the worst possible week to learn it.

This page covers which of five access levels you hold, which of six Google assets your agency might hold independently of the account, and what to put in a contract before you sign. It does not cover the leaving process itself, that lives in a separate guide, linked further down.

## Who Owns a Google Ads Account?

A Google Ads account has exactly one owner. Google Ads Help states plainly that "a client account can only have one owner" (Google Ads Help, 2026), either the Google account that created it or a manager account made owner afterward. Data ownership and administrative ownership are separate.

Three terms get blurred, and that is where owners lose track of their exposure. **Owner manager**: a manager account holding owner status; "if a manager creates a new account, the manager will automatically become the owner of that account." **Linked manager**: access but no ownership by default. **Data owner**: the client account, which never changes hands; owners get full administrative access but "do not take data ownership or administrative rights away from client accounts."

Ownership is also transitive. If your agency's manager account owns yours, every manager above it in the hierarchy has ownership too, which means the chain runs longer than the one agency you actually talk to, especially if it is a white-label reseller.

Owner status decides who can remove whom, which is why it matters more than whose name is on the invoice. Whether to work with an agency at all is a separate question; our Google Ads agency guide covers that decision, and running the account on software instead keeps owner status with you by default.

### What Is a Google Agency Account?

There is no Google product called a "Google agency account." People mean a Google Ads manager account, also called an MCC (My Client Center), a container that lets one login manage many advertiser accounts, the only practical way to run dozens of clients.

A manager account is not where your money or data lives; campaigns, conversion history, and billing sit in your own account, and the manager account is only an access layer on top.

Using an MCC is normal, correct, and expected. The problem is never the MCC, only whether your account was created inside the agency's manager account, making it owner, or linked to it, which does not. The MCC question settles who is attached to your account. The access-level question, next, settles what you can still do about it.

## The Five Access Levels and What Each One Costs You at Exit

Google Ads has five access levels: Email-only, Billing, Read-only, Standard, and Admin. Only Admin lets you remove an agency's manager account. Everything else can look like control while leaving the relationship itself in someone else's hands (Google Ads Help, 2026):

| Access level | What you can do | Enough for you as the advertiser | What happens if the relationship ends today | 
|---|---|---|---|
| Email-only | Notification emails and reports only. | No, the weakest level, for stakeholders who just need to be informed. | You cannot see or control anything. | 
| Billing | Edit billing, payment forms, and payments profile details. | No, more money control than most expect, but no campaign view. | You can pay the bill but not remove the agency. | 
| Read-only | View campaigns, reports, users, managers. Cannot edit. | No, despite feeling like real access. | You can document, but not unlink. | 
| Standard | Edit campaigns and billing. Cannot touch access or manager links. | The trap level: most owners who "have access" hold this and are not in control. | You can pause campaigns, not unlink the agency. | 
| Admin | Everything Standard does, plus grant or change access, accept or reject manager links, unlink managers. | Yes, the only level that controls the relationship. | You can unlink the agency yourself, immediately. | 

Only Admin can grant access, change access levels, accept or reject manager link requests, and unlink managers. If you are Standard, you can edit every campaign and still not remove the agency.

### How Do I Give an Agency Access to My Google Ads Account?

Create the account yourself, then link the agency's manager account to it, rather than letting the agency create it for you. Ask for the agency's manager account ID, send or accept the link, and confirm your own access still shows Admin once the link completes.

1. Create the account under an email on your own company domain.
2. Get the agency's manager account ID.
3. In Account access and security > Managers, send or accept the link request.
4. Confirm your access level still shows Admin after linking.

Link a manager, do not transfer ownership. Transfer (Google Ads Help, 2026) is for a genuine change of custodian, not routine management. Some agencies genuinely need owner status, usually for invoicing or a credit line; negotiate it explicitly and time-box it. One community contributor put the default plainly: "Always create the account yourself, then permit the agency to access it via their MCC... so you can revoke their access, not the other way round" (Jason King, Google Ads Community, 2021). Getting the manager link right handles just one part of the picture. The other five pieces are just as easy to lose track of, and that is the actual exposure check below.

## The Ownership Exposure Check: Six Google Assets Your Agency Might Hold

Your Google Ads account is one of six separate objects an agency can hold, and they strand independently. Losing the ads account is the obvious risk. Losing the payments profile, the conversion tags, the GA4 link, the remarketing audiences, or Merchant Center is the one that actually stops you rebuilding.

| Asset | Who typically holds it | How to check | What you lose if the relationship ends today | 
|---|---|---|---|
| Google Ads account (owner status) | Whichever manager account is Owner, automatic if it created the account. Ownership is transitive up the chain. | Account access and security > Managers tab, check the Owner column. | If no one on your side holds Admin, you cannot unlink anyone. | 
| Your own access level | Assigned per user by whoever holds Admin. | Same screen, Access level column next to your name. | Everything above your level in Table 1. Only Admin unlinks a manager. | 
| Payments profile | A separate object, often the agency's contact if it set up billing. | The profile's own user list, or ask who the primary contact is. | Users "can't directly add or remove users from the payments profile or change existing user permissions" (Google Ads Help, 2026); fixing this needs the primary contact, or someone on your domain, contacting support with the Payments Profile ID. An invite lapses after two weeks (Google Ads Help, 2026). | 
| Conversion tags and GTM container | Whoever set up the container, often the agency's own GTM account. | Google Ads' automatic Tag Diagnostics notice; the GTM container's own ownership. | "If your account has only one administrator, you may lose access to your tags if that user becomes unavailable" (Google Ads Help, 2026). Fix: add a second admin. | 
| GA4 property and its Ads link | Whoever created the GA4 property; only an Admin can link it. | GA4 Property Access Management; Ads Account access and security. | Conversions stop feeding Smart Bidding without an Admin on your side. Agency-owned GA4 means losing the historical view too. | 
| Remarketing audiences and Merchant Center | Lists tied to whichever manager's shared tag; Merchant Center is a separate account system. | Audience Manager for list source; Merchant Center's own settings. | Lists stop populating on unlink (Google Ads Help, 2026). Merchant Center access does not transfer; one email creates only one account (Google Ads Help, 2026). | 

Run this as a ten-minute checklist, not a source of alarm.

### Can You Find Out Who Owns a Google Account?

For a Google Ads account, yes. Open Settings > Account information or Account access and security to see the owner, linked manager accounts, and every user's access level. For a personal Google account, a plain Gmail address, no: Google does not publish who owns an email address.

An unrecognized manager account name is usually a white-label reseller or a parent MCC above your agency; ownership is transitive, so it has access too. If you cannot open Account access and security at all, that itself is the answer: your access level is below Standard. That is the quiet version of this problem, the one you catch by checking a settings screen. The loud version shows up in agency disputes, and it looks remarkably similar.

## What Ownership Disputes Actually Look Like

In December 2023, an advertiser on r/PPC titled a thread "Agency says they can't give access to our Google Ads account because it'll expose all client payment info" (r/PPC, 2023). The reason an agency gives for withholding access is almost always a consequence of setup, not a policy Google requires.

Of the 10 threads we reviewed on agency access disputes, December 2023 to March 2026 across Reddit, the Google Ads Community, and LocalSearchForum, three situations repeat: the client holds Standard or Read-only and cannot unlink; the account sits inside the agency's manager account, so there is nothing to transfer, only a rebuild; and the dispute reaches Google Ads support, which mediates access but does not arbitrate the contract. This is a light scan, not a survey, which is why the numbers stay counts, never percentages.

If the relationship already feels over, the signs you need to fire your PPC agency covers recognizing that.

## What to Negotiate Before You Sign

Ownership is cheap to fix before you sign a contract and expensive to fix after the relationship sours. Six items belong in writing before the engagement starts.

1. Account creationYou create the account under your own company-domain email; the agency links its manager account to it.
2. Admin accessYou keep Admin for the whole engagement, plus at least one other person at your company.
3. Payments profileThe payments profile stays under your company, with your own primary contact.
4. Conversion tags and GTMConversion tags and the GTM container live in your own GTM account, not the agency's.
5. GA4 propertyThe GA4 property is yours; the agency is granted access rather than owning it.
6. Offboarding clauseA written offboarding clause: access handed over within a stated number of business days of termination, not contingent on final invoice settlement.

Item six matters most. Most disputes are not about ownership in principle, they are about ownership used as a bargaining chip during a billing disagreement. Asking for these is not distrust, it is the same due diligence you would apply to a bookkeeper or a domain registrar. A good agency already defaults to this and will say so.

Vet an agency before you sign with our guide to choosing a PPC agency. See our breakdown of PPC management cost for how the offboarding clause interacts with final billing. All of that is prevention, for the reader who has not signed yet. If you already have, the questions change.

## Already Exposed? Three Moves That Actually Work

If you do not have Admin access today, the order of operations is request, document, escalate. Do not start by threatening to leave.

Request Admin access in writing, framed as internal governance, not distrust. Document what you can see today: access level, linked managers, conversion actions, payments profile, with dated screenshots. If refused or ignored, escalate to Google Ads support, which helps with access and recovery but does not arbitrate a commercial dispute.

One honest fallback: if the account was built entirely inside the agency's manager account and you never held Admin, starting a new account is sometimes the fastest path, costing conversion history and bidding learning. There is no reliable number for that loss.

For the full handover checklist, billing transfer, and escalation sequence, see how to switch Google Ads agencies.

## Where Kampaio Fits

Kampaio runs inside your own Google Ads account. You create the account, hold Admin, and the software is granted access like any other user. There is no Kampaio manager account that owns your account, nothing to transfer back if you cancel.

The ownership risk here is a property of the arrangement, not of agencies. Any setup where someone else creates the account carries it; any setup where you create it and grant access does not, whether you are granting it to an agency or software.

If you would rather run Google Ads yourself, with software instead of an agency, running Google Ads without an agency covers that path.

## FAQ: Google Ads Agency Account Ownership

Can an agency legally keep my Google Ads account?

No Google policy lets an agency keep an account against the owner's wishes. Disputes usually stem from setup, not a right the agency holds. Google Ads support helps with access but does not arbitrate the underlying contract (Google Ads Help, 2026).

What is the difference between manager access and account ownership?

Manager access lets an agency manage campaigns, billing, and reporting inside your account. Ownership is separate; it determines who can grant, change, or remove that access. An agency can have full manager access without ever holding ownership.

Can two agencies have access to my Google Ads account at the same time?

Yes, access is granted per user. However, an account can only have one direct manager account linked at a time (Google Ads Help, 2026).

Does my conversion history transfer if I have to start a new account?

No. Conversion history, Smart Bidding learning, and Quality Score signals stay inside the specific account. A cross-account conversion tag keeps recording pre-unlink clicks only for the typical 30-day window (Google Ads Help, 2026).

Should the agency's billing sit on my account or theirs?

Your own payments profile is cleaner. It keeps the primary contact, payment forms, and billing history under your control, and avoids the payments-profile issues in the exposure check above.

Can I remove an agency's manager account myself?

Only if you hold Admin on your own account. Users with ownership can always unlink a manager with ownership; anyone below Admin cannot (Google Ads Help, 2026).

## Check Your Access Before You Need To

Open Tools > Setup > Account access and security and confirm Admin sits next to your name. It takes under a minute, and it is the only thing on this page that is genuinely urgent today.

Kampaio is software that runs inside the account you own, not another account you have to worry about owning.

### Keep the account, keep the control

kampaio is granted access to the account you already own, and shows every change before it ships. See kampaio's plans, or connect your own account and watch what it would change first.

Start with your own account
Access levels, ownership rules, and interface paths were verified against Google Ads Help in July 2026 and can change. This article is informational and does not constitute legal advice.
