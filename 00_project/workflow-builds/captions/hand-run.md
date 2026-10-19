# 2.3 Hand run: one task solved by hand (2026-10-19)

Status: SAMPLE dump. Martin said on 2026-10-19: "there is nothing yet, that will come whenever we have it." The Drive folder "Captions Celine Martin" is empty. The real dump replaces this sample at the functional test (4.2).

## Input: sample dump (as Martin and Celine would write it, mixed German and English)

```
19.10. dump
- 6 uhr surfen batu bolong, wellen klein, 40 min drin
- coworking canggu day pass 150k rupiah, laut, nie wieder montag
- celine: 2 kundencalls, einer neu (agentur aus wien), angebot geht freitag raus
- budget talk: wir leben hier von 2.500 euro im monat für uns beide. villa 1.100, scooter 70, essen ca 600, rest sparen/puffer
- idee: content batch sonntag, alle videos der woche in 3 stunden schneiden statt jeden abend
- insight: vor 10 uhr schaffen wir mehr als den ganzen nachmittag. deep work morgens, calls nachmittags
- abends warung bu made, nasi campur 35k, regen
- morgen: visa agent anschreiben wegen verlängerung, läuft 4.11. ab
- strategie: 3 kunden mehr bis dezember, dann 5k monat
- celine will mehr b-roll vom markt
```

## Step 2 by hand: beats (one fact per line, quoted from the dump)

| # | Beat | Dump words | Type |
|---|---|---|---|
| B1 | surf at 6, Batu Bolong, small waves, 40 min | "6 uhr surfen batu bolong, wellen klein, 40 min drin" | day |
| B2 | coworking Canggu, day pass 150k rupiah, loud, never again Monday | "coworking canggu day pass 150k rupiah, laut, nie wieder montag" | day |
| B3 | Celine 2 client calls, one new, agency from Vienna, offer out Friday | "celine: 2 kundencalls, einer neu (agentur aus wien), angebot geht freitag raus" | day |
| B4 | budget: 2.500 euro a month for both, villa 1.100, scooter 70, food ca 600, rest savings/buffer | "wir leben hier von 2.500 euro im monat ... rest sparen/puffer" | money |
| B5 | idea: content batch Sunday, all videos of the week in 3 hours, not every evening | "content batch sonntag, alle videos der woche in 3 stunden schneiden statt jeden abend" | idea |
| B6 | insight: before 10 we get more done than the whole afternoon; deep work mornings, calls afternoons | "vor 10 uhr schaffen wir mehr als den ganzen nachmittag" | insight |
| B7 | evening Warung Bu Made, nasi campur 35k, rain | "abends warung bu made, nasi campur 35k, regen" | day |
| B8 | tomorrow: message visa agent, extension, visa ends 4.11. | "visa agent anschreiben wegen verlängerung, läuft 4.11. ab" | plan |
| B9 | strategy: 3 more clients by December, then 5k a month | "3 kunden mehr bis dezember, dann 5k monat" | plan |
| B10 | Celine wants more b-roll from the market | "celine will mehr b-roll vom markt" | note |

Not in the dump, so not in the captions: the day of the week, the villa location, who the Vienna agency is, what "5k" is in (the dump says "5k monat", the caption says "5k a month" and nothing more).

## Step 3 by hand: story order
1. Hook: the money line (B4 first sentence). Strongest fact, most people click for it.
2. The day in order: B1, B2, B3.
3. Money detail: B4 rest.
4. Idea: B5.
5. Insight: B6.
6. Evening: B7.
7. Close with the plans: B8, B9, B10.

## Step 4 by hand: captions (English, "we", max 12 words, max 2 lines, max 42 characters per line)

```
# Captions 2026-10-19

1. We live here on 2,500 euros a month.

2. Both of us. Here is how a day looks.

3. 6 am. Surf at Batu Bolong.
   Small waves, 40 minutes in.

4. Then coworking in Canggu.
   Day pass: 150k rupiah.

5. Loud today. Never again on a Monday.

6. Celine: two client calls.
   One new, an agency from Vienna.

7. The offer goes out on Friday.

8. Budget talk.

9. Villa: 1,100 euros.
   Scooter: 70 euros.

10. Food: about 600 euros.
    The rest goes into savings.

11. New idea: a content batch on Sunday.

12. Cut all videos of the week in 3 hours.
    Not every evening.

13. Before 10 am we get more done
    than the whole afternoon.

14. Deep work in the morning.
    Calls in the afternoon.

15. Evening at Warung Bu Made.
    Nasi campur, 35k. And rain.

16. Tomorrow: message the visa agent.
    Our visa ends on 4 November.

17. The plan: three more clients by December.
    Then 5k a month.

18. Celine wants more b-roll from the market.

19. That was the day. See you tomorrow.
```

## Step 5 by hand: checks
- Words per block: max is 12 (block 12, block 17). All pass.
- Lines per block: max 2. All pass.
- Characters per line: all under 42.
- Numbers: 2,500 (dump 2.500), 6, 40, 150k, 1,100 (dump 1.100), 70, 600, 3, 10, 35k, 4, 5k. All in the dump. "two" in block 6 is the dump's "2". Word numbers under ten are allowed when the dump has the digit.
- Dashes: none. HTML: none.
- Language: English only. Place names and the warung name stay as in the dump.
- Block 19 is a close line. It has no fact. Allowed: hook and close lines may carry no fact, but they may not carry a new fact.

## Friction and edge cases found (these go into the skill)
1. Mixed language: the dump is German with English words. The beats table translates, the dump column keeps the original words. The captions are English only.
2. Number formats: the dump writes 2.500 and 1.100 (German). English captions write 2,500 and 1,100. The validator must strip dots and commas before it compares.
3. "150k", "35k", "5k": keep the "k" as in the dump. Do not expand to 150,000. The validator compares "150k" as a token.
4. "4.11." is a date. The caption says "4 November". The validator must accept "4" and "11" as parts of "4.11.".
5. Word numbers: "two" for "2" is fine for one to nine. The validator checks digits only, so word numbers pass. The beats table is the check for them.
6. Hook and close: one hook block at the start and one close block at the end may carry no fact. They may not add a fact.
7. No day of the week, no location of the villa, no names that are not in the dump.
8. One idea per block. A block with two facts of one kind (villa + scooter) is fine when it stays under 12 words.
9. Blocks per video: 19 for a 10-line dump. Rule of thumb: 1.5 to 2.5 blocks per dump line. Range 12 to 60.
10. Line split: the writer sets the line break at a natural pause. The validator checks only the limits.
11. Empty folder: when the Drive folder has no doc, the skill stops with a card. It never invents a dump.
12. The Drive folder belongs to 741studio18@gmail.com and is shared with Martin's account. The Drive MCP can read and create files there (`canAddChildren: true`).

## Script run on the hand-run captions (2026-10-19, after the scripts existed)
- `validate_captions.py` first run: FAIL, block 3 had 13 words ("6 am." counts as two words). My hand count was wrong. Fixed to "6 am. Surf at Batu Bolong. / Small waves, 40 minutes in." (11 words). Second run: PASS, 19 blocks.
- `deslop.py` first run: 4/5, "possible invented proof: 3 more clients". The fact is in the dump. Fix: the number as a word ("three more clients"). Second run: 5/5. Rule for the skill: when the lint flags a dump number as invented proof, write one to nine as a word. The fact stays.
- Negative test with a bad file: 12 problems found (numbering gap, count, words, chars, dash, wrong number 2,900, German words, 3 lines, HTML). Exit 1.
- `intake.py` second run on the same date: kept the old file as `captions-v1.md`. Status and finish work.
