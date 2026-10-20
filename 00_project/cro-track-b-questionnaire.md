# CRO Track B: Grill-Me Questionnaire

Used in step B0 of `cro-track-b-design-intense-workflow.md`. Trigger: Martin says "let's do track B" (for a client, a lead, or a pilot).

## How the agent runs it

1. Ask in **three rounds**. Round 1 first. Wait for the answers. Then round 2, then round 3. At most 10 questions per round. Show the question numbers.
2. Before each round: read what is already known (lead info, website, GBP, dataset, earlier runs) and **skip every question the files already answer**. Say which ones were skipped and the answer found.
3. Offer 2 to 4 options for every question that has options. Mark the one the agent recommends. Martin can answer "you choose" for any question. Then the agent writes the choice and the reason.
4. **Push back on vague answers.** "Modern", "clean", "premium", "like Apple" are not answers. Ask for one example URL or one screenshot, or ask "what would be wrong about it if it were not like that?"
5. Write all answers to `00-brief-b/brief-b.md` after each round, with the date. Keep Martin's words.
6. **Gate:** the build does not start until blocks A to G are answered, the reference board has 5 or more references, and the signature idea is chosen.
7. Rule from memory: no unnecessary client questions. The agent asks Martin, not the client. The client fills in nothing.

---

## Round 1: Why, who, what (answer first)

**A. Goal and context**
1. Which client or lead, which page (home, about, service, landing)? Is it a pitch, a paid job, or a pilot?
2. What must the page do in one sentence (contacts, bookings, brand statement, sign-ups)? Which channel gets the contact (WhatsApp, phone, booking form, e-mail)?
3. Why Track B and not Track A for this one? (The answer tells us how far to go.) Options: win the lead with a wow demo · the client's brand needs it · the competition looks strong · pilot to learn.
4. Who is the visitor, in their own words? What do they feel when they land (worried, curious, in a hurry, comparing)? What should they feel after 10 seconds?
5. What happens after the page works? (Who sees the prototype, when is the decision, what counts as success.)
6. Industry limits: HWG, Anwaltswerbe-Check, financial claims, none? Anything the client may never show or say?
7. Time and effort: hours we can spend, deadline, number of rounds Martin wants to review. Autonomous run (no stops) or stops at checkpoints?

**B. Brand**
8. Logo and brand files: do they exist? Where? If not: do we make a wordmark (as with the law-firm run) or wait for a real logo?
9. Colours, fonts, imagery style that must stay. What is allowed to change? (Fixed, flexible, free.)
10. Five mood words, and three words the page must **never** feel like.

## Round 2: References and the idea (the heart of Track B)

**C. References** (target 5 to 8, at least 2 anti-references)
11. Which sites do you love, and why? For each: URL, and **what exactly** you like. Pick from: layout · typography · colour · imagery or video · motion · interaction · tone of voice · structure of the page. Use Refero, Mobbin, Awwwards, Dribbble, X search "design websites", or sites you know.
12. For each reference: what must we **not** take? (Too busy, wrong audience, wrong industry.)
13. Anti-references: 2 or more sites that look like the client's competitors or that you dislike. What is wrong with them?
14. Closest to the goal: which one reference would you choose if you could only keep one? Furthest from the goal: which one?
15. Does the client have their own favourites or a dislike list? Where is it?
16. Which parts of Ronas-type layouts (big tight headlines, number blocks, wave underlines, scroll-lit text, plus FAQ, dark closing band) do we reuse, and which do we drop?

**D. The signature idea**
17. What is the one thing a visitor should remember and describe to a friend? Options: a hero loop · a scroll story · a character or mascot · a morphing interface · a before/after interaction · a bold type moment · a surprise at the end.
18. Is there a metaphor for the brand (a door, a path, a tree, a ledger, a bridge)? Can the page tell it in 3 steps while scrolling?
19. Is a character or mascot wanted? If yes: style, name, does it react to cursor or scroll, and does it fit the industry (never for HWG pages)?
20. Where do we **not** want motion? (Legal text, prices, forms, the CTA.)

## Round 3: Media, interaction, limits

**E. Media**
21. What real photos and videos exist? (Open them. Rate each: usable, usable with edit, not usable.) Who is allowed to appear in generated images? Does the client agree to AI-made people and rooms, flagged on a shoot list?
22. Video: looping hero video wanted? Length (4 to 8 s), tool (Higgsfield or other, if connected; otherwise code graphics and stills), who pays. Sound: never autoplay.
23. Music or sound at all? (Default: none.)
24. Image style: photo, illustration, 3D, line art, mixed. Light or dark. Warm or cool. People or no people.

**F. Motion and interaction appetite** (each 0 = none, 5 = a lot)
25. Scroll effects (text lighting, reveals, pinned sections). Cursor effects (follower, hover morphs). Interactive widgets. Playful elements (games, easter eggs).
26. Pick up to 4 components from the menu in the workflow (morph menu, curtain footer, image trail, spin gallery, day/night switch, bento glide, command bar, jelly buttons, hop navigation, holographic sticker, interactive 404, game gate). For each pick: the reason (conversion or brand).
27. Intro animation allowed? (Max 2.5 s, skippable, never hides the CTA.)

**G. Content and structure**
28. Does approved copy exist? Language and form of address (du or Sie). Must-have sections and sections to drop. Page length wish.
29. Which proof must appear early (rating, years, number of clients, press, certificates)? Real data only.
30. Primary CTA text and the reassurance line under it. Secondary action.

**H. Technical and delivery**
31. Where will this live? (Wix, WordPress, Jimdo, Webflow, custom, unknown.) Does the CMS limit custom code? If it does: pitch-only prototype or buildable?
32. Targets: devices (desktop 1440 first, mobile later), weight budget, slow connections.
33. Accessibility floor: reduced motion version (always), keyboard use, contrast. Anything stricter?
34. Delivery format: local HTML plus Drive folder (default). Hosted preview only if Martin asks. A recorded screen walk-through? A short Loom for the lead?
35. What would make Martin say "this is wrong"? (The agent writes the answer into the brief as a check.)

---

## Output of B0

`00-brief-b/brief-b.md` in this shape:

```markdown
# Brief B — <Client> <Page>
Datum · Ziel · Besucher und Gefühl · Branche und Grenzen · Marke (fest / flexibel / frei)
Stimmung (5 Wörter) · Nie (3 Wörter)
Referenzen: Tabelle URL | nehmen | nicht nehmen | Sektion
Anti-Referenzen
Signature idea (ein Satz) · Metapher · Figur ja/nein
Medien: vorhanden / erzeugt / Video-Tool / Ton
Bewegung 0 bis 5: Scroll · Cursor · Widgets · Spiel
Komponenten (max 4) mit Grund
Keine-Bewegung-Zonen
Inhalt: Copy-Status, Sprache, Pflichtsektionen
CMS und Grenzen · Gewicht · Barrierefreiheit
Lieferformat · Erfolgskriterium · "Falsch wäre es, wenn …"
Offen [FEHLT]
```

## Short form (when Martin wants it fast)

Ask only: 1, 2, 4, 6, 8, 11, 14, 17, 21, 26, 28, 35. The agent fills the rest with recommendations and lists them as assumptions in the brief.
