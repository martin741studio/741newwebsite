# Extract: approval and proofing tool UX, rules for the 741 client portal

Area: 01, approval and proofing tools. Research date: 2026-10-13.
Sources: 16 files in `sources/`. Dated sources run from 2026-07-29 to 2026-10-06.
Help-center pages count as current on the fetch date (2026-10-13).

Strength labels:
- **official doc**: stated in a vendor help center or product doc.
- **2+ sources**: two or more independent sources agree.
- **1 source**: one source only (often a vendor blog). Treat as a hint.

---

## A. Access and entry (keep the client fast)

1. **One link, no password.** The client opens a magic link and lands on the open items. Account creation stalls reviews.
   Sources: marker-client-proofing-2026, socialpilot-fix-client-approval-workflows, pastel-approvals-deadlines, agency-portals-assembly-superokay, webflow-comments. Strength: **2+ sources + official doc**.

2. **Approval needs a known identity; viewing does not.** Planable public links allow comments but no approval. Webflow guests must verify an email. Our magic link is tied to one client email, so it covers this. Do not allow approval from an anonymous forwarded link.
   Sources: planable-client-approval, webflow-comments. Strength: **official doc**.

3. **Check the forwarded-link case.** Decide what happens when the client forwards the mail. Safe default: the receiver can view, but must confirm their email before a decision counts.
   Sources: socialpilot-fix-client-approval-workflows, webflow-comments. Strength: **2+ sources**.

4. **Show only what is ready.** Draft items stay hidden until the team releases them, in a batch. The client never sees half-done work.
   Sources: planable-client-approval. Strength: **official doc**.

5. **One inbox view, "inbox zero".** The client sees one list of open items. Each decided item leaves the list. The same link works every month.
   Sources: planable-client-approval, pastel-august-2026-roundup. Strength: **official doc**.

## B. The decision itself

6. **Few, fixed decision buttons.** Tools use two to four choices: approve, approve with small changes, request changes. Keep the labels plain, and keep the logic behind them fixed.
   Sources: ziflow-decision-calculation, pastel-approvals-deadlines, figma-branch-review, filestage-versions-audit. Strength: **official doc (4 tools)**.

7. **Allow a decision without a comment.** Pastel lets a reviewer approve with zero comments. For us: one tap on a variant is a full decision.
   Sources: pastel-approvals-deadlines. Strength: **official doc**.

8. **Add "approve with small change" as a middle option.** Ziflow separates "approved with changes" (no new version) from "changes required" (new version). This fits our SEO lock: the client can tweak wording while the keyword stays.
   Sources: ziflow-decision-calculation. Strength: **official doc**.

9. **Approve the whole item, not parts of it.** Figma approves a branch as a whole. One item in our portal gets one decision. Split big changes into separate items.
   Sources: figma-branch-review. Strength: **official doc**.

10. **Decision is not go-live.** Figma separates "Approved" from "Merged". Filestage moves approved files to "Ready for publishing". This matches our "ready for live" list plus Martin's final go.
    Sources: figma-branch-review, filestage-automations. Strength: **official doc (2 tools)**.

11. **A decision can change until the item is locked.** Ziflow lets a reviewer change a decision and recalculates. Lock the item once Martin gives the go.
    Sources: ziflow-decision-calculation, figma-branch-review. Strength: **official doc**.

## C. Showing the work (variants, context, versions)

12. **Show the change in its real context.** Comments and reviews sit on the live page or design, not on a separate file. For us: hero image in page context, text as before/after in place.
    Sources: pastel-approvals-deadlines, webflow-comments, marker-client-proofing-2026. Strength: **2+ sources + official doc**.

13. **Show before and after, with change marks.** Filestage marks added text green and removed text red. Tools offer side by side, overlay and swipe compare. Mark the keyword in the same way.
    Sources: filestage-versions-audit, simple-best-proofing-2026, reviewstudio-proofing-at-scale. Strength: **2+ sources + official doc**.

14. **Always open the current version.** Old versions cause wasted rounds. A new version resets earlier approvals (Pastel).
    Sources: marker-client-proofing-2026, simple-best-proofing-2026, pastel-approvals-deadlines. Strength: **2+ sources + official doc**.

15. **Store the screen size with each item and comment.** Webflow and Pastel save device, viewport and browser. Pastel restores that width when you open the comment. Show variants in desktop and mobile view.
    Sources: webflow-comments, pastel-august-2026-roundup. Strength: **official doc + 1 blog**.

16. **Pin comments to an element.** A comment sticks to an element and moves with it. The client points, and does not describe in words.
    Sources: webflow-comments, marker-client-proofing-2026, pastel-approvals-deadlines. Strength: **2+ sources + official doc**.

17. **Run automatic checks before the client sees anything.** Pastel scans for broken links. Ziflow ReviewAI checks rules and gives a written reason. A human always makes the final call. Use this as a pre-check of each variant (keyword present, length, broken links).
    Sources: pastel-august-2026-roundup, ziflow-reviewai-content-check, simple-best-proofing-2026. Strength: **2+ sources (vendor blogs)**.

18. **Re-check every new version, not only the fix.** In Ziflow's own test, a fix added a new problem. Compare old and new versions on every rework.
    Sources: ziflow-reviewai-content-check. Strength: **1 source**.

## D. Deadlines, reminders, digest

19. **Set the deadline automatically when the item goes out.** Filestage adds "due in N days" by rule. Ziflow supports relative deadlines and business days only. For us: due date = release date + 3 days, business days.
    Sources: filestage-automations, ziflow-deadlines-reminders. Strength: **official doc (2 tools)**.

20. **Send one daily digest, not one mail per item.** Filestage sends one morning roundup, no weekends. It lists "due soon" and "overdue" items. Planable lets clients pick hourly or idle mails.
    Sources: filestage-due-date-reminders, planable-client-approval. Strength: **official doc**.

21. **Remind before, at, and after the deadline.** Ziflow sends all three. After the deadline, reminders repeat at a set rate. Map to ours: digest shows "due soon", reminder on day 3, last notice before day 7.
    Sources: ziflow-deadlines-reminders, marker-client-proofing-2026. Strength: **official doc + 1 blog**.

22. **Stop reminders the moment a decision is in.** Both Filestage and Ziflow stop reminders per person, per item, once a decision exists.
    Sources: filestage-due-date-reminders, ziflow-deadlines-reminders. Strength: **official doc (2 tools)**.

23. **Only decision-makers get reminders.** Ziflow skips comment-only reviewers. Name one approver per client, plus a deputy.
    Sources: ziflow-deadlines-reminders, socialpilot-fix-client-approval-workflows. Strength: **official doc + 1 blog**.

24. **Close input at the deadline.** Pastel pauses comments at a set time; the page turns read-only. The team can still comment inside.
    Sources: pastel-approvals-deadlines. Strength: **official doc**.

## E. Auto-approval and the record

25. **Auto-approval is a rule agreed at onboarding.** No proofing tool in this set documents native "approve after X days". SocialPilot advises: set the window early, and decide per type what happens at the end. Our 7-day rule is our own design. Put it in the contract and the onboarding mail.
    Sources: socialpilot-fix-client-approval-workflows, marker-client-proofing-2026. Strength: **1 source (blog) + gap in official docs**.

26. **Exclude high-risk items from auto-approval.** Items with claims, prices or third-party names need an explicit yes. For us: consider GBP changes and legal or health claims (HWG) as "explicit only".
    Sources: socialpilot-fix-client-approval-workflows. Strength: **1 source**.

27. **Log every decision with person, time, version, and type.** Filestage and Simple log who decided, when, and on which version. Add a field `decided_by = client | auto_7d`. Export as PDF on demand.
    Sources: filestage-versions-audit, simple-best-proofing-2026, pastel-august-2026-roundup, marker-client-proofing-2026. Strength: **2+ sources + official doc**.

28. **Show the team a live status board.** Pastel's "Next Steps" shows opened, approved, pending and changes requested per person. Use it to see which client is stuck.
    Sources: pastel-august-2026-roundup, planable-client-approval. Strength: **official doc + 1 blog**.

29. **Keep all feedback inside the item.** Feedback in email or chat breaks the record. Reply links in the digest must open the item, not a mail thread.
    Sources: marker-client-proofing-2026, socialpilot-fix-client-approval-workflows, reviewstudio-proofing-at-scale. Strength: **2+ sources**.

30. **Use stages and automatic hand-off.** Filestage moves an item to the next group when one group approves. Ziflow uses staged workflows. Our flow: 741 internal check, then client, then Martin's go.
    Sources: filestage-automations, ziflow-deadlines-reminders, planable-client-approval. Strength: **official doc (3 tools)**.

---

## Gaps and warnings

- **Variant choice (pick 1 of 3):** No tool in this set offers a "pick one of N variants, one recommended" pattern. Tools approve one item at a time. Our variant picker is new. Area 03 (decision psychology) should cover option count and default effects.
- **Auto-approval:** Only blog advice supports it. No proofing tool documents it natively. Treat it as a contract rule, and log it as "auto".
- **Mobile:** Only Pastel (responsive preview) and SocialPilot (approve on phone) address it. No tool documents a mobile-first approval screen.
- **Webflow warning:** comments on a page branch are deleted on merge. Keep our decision log separate from any CMS or branch.
- **Moxo and ClickUp:** help pages were offline or not found on the fetch date. Not covered.
- **Bias:** marker, simple, socialpilot, reviewstudio and ziflow blogs are vendor content.
</content>
</invoke>
