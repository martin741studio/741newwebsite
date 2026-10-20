# 03 Decision psychology: design rules for the client approval portal

Scope: choice architecture for the 741 client approval workflow (2-3 pre-checked variants, "741 recommends", one-line "why", locks, daily digest, reminder after 3 days, default applied after 7 days).

Research date: 2026-10-13. Freshness rule: all sources published 2026-07-15 to 2026-10-09. 15 sources in `sources/`.

## Support strength scale

- **Strong**: a 2026 peer-reviewed study, or a meta-analysis named in two or more 2026 sources.
- **Medium**: one 2026 study, or a well-sourced 2026 summary of older peer-reviewed work.
- **Weak**: practitioner advice or our own inference from the sources.

## Source slugs

| Slug | Type | Date |
|---|---|---|
| uxtigers-behavioral-economics-ux | UX summary (Nielsen) | 2026-10-07 |
| uxtigers-framing-effect | UX summary (Nielsen) | 2026-08-06 |
| jdm-defaults-used-strategically | Peer-reviewed, JDM | 2026-09-04 |
| ijhm-source-transparency-recommendation | Peer-reviewed, field experiment | 2026-08-11 |
| psychsci-deadlines-replication | Peer-reviewed replication | 2026-07-15 |
| conversation-optout-default-backlash | Expert analysis, NHS data | 2026-10-09 |
| psychologyexposed-choice-overload | Research summary | 2026-08-27 |
| psychologyexposed-anticipated-regret | Research summary | 2026-08-28 |
| economictimes-two-vs-ten-choices | News summary | 2026-08-11 |
| psychologytoday-choice-overload | Expert blog | 2026-09-02 |
| psychologytoday-algorithm-or-gut | Expert blog | 2026-09-15 |
| menlo-consumer-ai-human-expert | Industry survey, n = 5,067 | 2026-09-16 |
| medium-notification-design-psychology | Practitioner article | 2026-08-28 |
| stripo-email-digest-best-practices | Practitioner guide | 2026-09-15 |
| treup-reminder-timing | Research summary | 2026-10-07 |

## Design rules

### A. Number and shape of options

1. **Show 2-3 variants per item, never more.** Overload is likely when items are complex, preferences are unclear, and the person wants low effort. Our clients meet all three. Keep 3 as the maximum and 2 as the normal case.
   Sources: psychologyexposed-choice-overload, economictimes-two-vs-ten-choices, uxtigers-behavioral-economics-ux, psychologytoday-choice-overload. **Strong**

2. **Pre-check and remove weak variants before the client sees them.** Removing weaker options and making the set easy to compare helps more than any exact option count. Every variant shown must be one we would ship.
   Sources: psychologyexposed-choice-overload, uxtigers-behavioral-economics-ux. **Medium**

3. **Make variants clearly different on one main dimension.** Similar options with many attributes cause more overload than a larger count. Label the difference ("calm / direct / local").
   Sources: psychologyexposed-choice-overload. **Medium**

4. **Show variants side by side in the same format.** Side-by-side comparison cuts comparison work. Use the same image crop, the same text length and the same layout.
   Sources: uxtigers-behavioral-economics-ux. **Medium**

5. **One decision per card.** Do not bundle a headline choice and an image choice in one card. Each extra attribute multiplies comparisons (6 options = 15 pairs).
   Sources: uxtigers-behavioral-economics-ux, psychologyexposed-choice-overload. **Weak** (inference)

### B. The "741 recommends" default

6. **Preselect the recommended variant and mark it "741 recommends".** People read a preset as advice. Defaults shift choices by about 27 points on average.
   Sources: uxtigers-behavioral-economics-ux, jdm-defaults-used-strategically. **Strong**

7. **The recommendation must truly serve the client, never 741's convenience.** People read a default as advice only while they see the setter as on their side. From a perceived opponent, they invert it. One self-serving default can damage the whole signal.
   Sources: jdm-defaults-used-strategically, psychologytoday-algorithm-or-gut. **Strong**

8. **Make "choose another" as easy as "accept".** Same size, same tone, one click. Asymmetric buttons are a hidden push and fail the symmetry test for ethical nudges.
   Sources: uxtigers-behavioral-economics-ux, uxtigers-framing-effect. **Medium**

9. **Present the recommendation as a named human expert decision, not "AI suggests".** In health and law, 59-63% prefer a human expert vs 19-21% AI. Use a person's name or "Martin / 741 team" next to the badge.
   Sources: menlo-consumer-ai-human-expert, psychologytoday-algorithm-or-gut. **Medium**

10. **Expect modest effects and measure them.** Real-world nudges average about 1.4 points, not the 8.7 points in published papers. Track the share of accepted recommendations, overrides and later change requests per client.
    Sources: uxtigers-behavioral-economics-ux. **Medium**

### C. The "why" line

11. **Every recommendation shows its basis in one line.** Source transparency raised acceptance from 83.6% to 92.7% and nearly halved rejections. It works because the advice feels authentic, not manipulative.
    Sources: ijhm-source-transparency-recommendation, uxtigers-behavioral-economics-ux. **Strong**

12. **Use an absolute number plus a named source.** Write "320 searches/month for 'Physiotherapie Nürnberg' (Google data)", not "+40% better". Absolute numbers next to any percentage resist misreading.
    Sources: uxtigers-framing-effect, ijhm-source-transparency-recommendation. **Medium**

13. **Name one honest trade-off where it exists.** Showing negative information raised adoption for all user types. Our prevention-focused clients (doctors, lawyers) respond most to this.
    Sources: ijhm-source-transparency-recommendation. **Medium**

14. **Show the client's own case in the "why".** People resist advice they think ignores what makes them unique. Mention their city, service or competitor, not a generic rule.
    Sources: psychologytoday-algorithm-or-gut. **Medium**

15. **Use gain framing by default. Use loss framing only for a real ranking risk.** Invented urgency destroys trust. For locked, ranking-critical items, state the real loss in plain words ("Without this keyword the page loses its main search term").
    Sources: uxtigers-framing-effect, uxtigers-behavioral-economics-ux. **Medium**

### D. Before/after and locks

16. **Show the final state next to the current state.** People judge change as a loss against the old version. A before/after view of the real page or profile reduces this loss feeling.
    Sources: uxtigers-behavioral-economics-ux. **Weak** (inference from loss-aversion findings; no 2026 source tests before/after views directly)

17. **Explain every lock in one line.** A lock without a reason reads as a black box and pushes clients to blanket distrust. State why the item is ranking-critical.
    Sources: psychologytoday-algorithm-or-gut, ijhm-source-transparency-recommendation. **Weak** (inference)

### E. Deadlines and default approval

18. **Show the deadline and the default on every card.** "If you do nothing, we apply the recommendation on 21.10." The client must see both the default and the date before it applies.
    Sources: uxtigers-behavioral-economics-ux, conversation-optout-default-backlash. **Medium**

19. **Offer an active "yes" and record it separately from the silent default.** In England, families agreed 87% of the time after an active opt-in but only 46% under deemed consent. Silent consent is weaker and more likely to be contested later.
    Sources: conversation-optout-default-backlash. **Medium**

20. **Log auto-applied items visibly and allow a simple undo window.** People prefer a default partly to reduce personal responsibility. They regret less when they can correct a choice. Show "applied by default on <date>" plus "change" in the portal.
    Sources: psychologyexposed-anticipated-regret, conversation-optout-default-backlash. **Medium**

21. **Keep the deadline structure simple: one deadline per item.** A 2026 replication found that spaced or complex deadline schedules did not reduce procrastination. Do not add extra deadline tiers.
    Sources: psychsci-deadlines-replication. **Medium**

22. **Use the near deadline to fight delay.** A concrete near date ("this Friday") recruits present bias. Phrase the reminder with the actual date, not "soon".
    Sources: uxtigers-behavioral-economics-ux. **Weak**

### F. Digest, reminders and fatigue

23. **One daily digest, no single-item emails.** Batching feels more useful and less intrusive. A digest needs one context switch, not five.
    Sources: medium-notification-design-psychology, stripo-email-digest-best-practices. **Medium**

24. **Skip the digest when nothing new is open.** Messages without real consequence train people to ignore all messages, including the important ones.
    Sources: medium-notification-design-psychology, stripo-email-digest-best-practices. **Medium**

25. **Digest layout: one main item first, 3-5 items visible, one primary button.** Readers spend about 9 seconds on an email. Put "N open, 1 due on <date>" in the first 30-40 characters of the subject.
    Sources: stripo-email-digest-best-practices. **Weak** (practitioner guide)

26. **Send at a fixed time when practice owners have a break.** Timing changed response by about 4-12% in a trial. Holding messages for a good moment increased response speed.
    Sources: treup-reminder-timing. **Medium**

27. **Keep reminders rare: one reminder at day 3, then the default.** Prompts lose power over weeks. Keep the "urgent" tier under 5% of all messages, so it still gets attention.
    Sources: treup-reminder-timing, medium-notification-design-psychology. **Medium**

### G. Regret and later change requests

28. **Close each decision cleanly.** After a choice, show "Done. Live on <date>." Avoid "are you sure?" loops. Second-guessing raises regret.
    Sources: psychologytoday-choice-overload, psychologyexposed-anticipated-regret. **Weak**

29. **Small, clear choice sets reduce later switching.** Overload shows up as lower confidence, more regret and switching later. That is the same as change requests for us.
    Sources: economictimes-two-vs-ten-choices, psychologyexposed-choice-overload. **Medium**

30. **Track the ethics of the default.** Monthly, check the six nudge tests: transparency, symmetry, publicity, self-judgment, regret rate, vulnerability. If a client would be upset to learn how a default was set, change it.
    Sources: uxtigers-behavioral-economics-ux. **Medium**

## Gaps and cautions

- **Before/after comparisons:** no 2026 source tests before/after views directly. Rule 16 is an inference. Another library area may cover this better.
- **Decision fatigue:** recent sources mention it, but the classic judge study is contested. No 2026 study gave usable numbers. We rely on choice-overload and digest evidence instead.
- **Choice overload is contested.** A 2010 meta-analysis found a near-zero mean effect. The effect is real only under the four moderators. Our setup meets them, so the rule still holds.
- **Excluded for freshness:** "Justification aversion: The road to more effective defaults" (Banki & Navarro-Martinez, OBHDP Vol. 196). It went online 2026-07-06, before the cutoff. It found that asking people to justify a switch raises default adherence by 22-58%. Do not use that tactic: it adds pressure and fails the symmetry test.
- **Excluded for freshness:** NN/g video "Data Isn't Enough: The Power of Narrative in UX" (2026-06-15).
