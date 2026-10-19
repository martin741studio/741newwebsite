# Story rules for the daily captions

The dump is a list of thoughts. The captions are a story with one shape. Use this shape every day.

## 1. The shape (4 parts)

1. **Hook** (block 1, maybe block 2): the strongest fact of the day. A number beats a feeling. Money, a decision, a change. Example: "We live here on 2,500 euros a month." (the dump said "hier", so no "Bali")
2. **The day** in time order: morning, work, afternoon, evening. Keep the order the dump gives when it has one.
3. **Insight or idea**: one block pair for the "insight:" or "idea:" line of the dump. Put it after the work part and before the evening.
4. **Close** (last 1 to 3 blocks): the plan for tomorrow, the strategy line, then one close line. The close line carries no fact ("That was the day. See you tomorrow.").

## 2. Picking the hook

- Order of strength: a money number, a decision or change, a plan with a date, a feeling.
- The hook may use a fact from the middle of the dump. The fact then does not repeat later, or repeats only as a detail.
- No question hooks. No "you will not believe".

## 3. Beats first, then blocks

- Write `beats.md` first: one line per fact, with the dump words in quotes. Types: day, money, idea, insight, plan, note.
- Every block comes from one beat. One idea per block. Two facts of one kind in one block are fine under 12 words (villa and scooter price).
- A beat with no place in the story is dropped, never invented around.
- Rule of thumb: 1.5 to 2.5 blocks per dump line. 12 to 60 blocks per video.

## 4. What stays out

- The day of the week, the place of the villa, names of people or companies, prices, dates: only when the dump has them.
- No opinion the dump does not have. No "amazing", "incredible", "game changer".
- No hashtags, no emoji, no calls to subscribe.
- No dashes. No HTML. No German words.

## 5. Voice

- "We" for Martin and Celine. "Celine" or "Martin" when one of them did it.
- Short. Plain words. Present tense for the day, future for tomorrow.
- Numbers as digits, English format: 2,500 and 1,100. Keep "k" as in the dump: 150k, 35k, 5k.
- Dates as "4 November". Times as "6 am".
- Place names and food names stay as written in the dump (Batu Bolong, Warung Bu Made, nasi campur).

## 6. Slop lint and numbers

- `deslop.py` can flag a dump number as "possible invented proof" (hand run: "3 more clients"). The fact is real. Write the number as a word for one to nine ("three more clients"). Keep digits for money, times, dates and anything over nine.
- "6 am." counts as two words for the validator. Count tokens, not ideas.

## 7. Unclear words, tense, notes (from the functional test 2026-10-19)

- **Unclear dump word** (two readings, like "laut" = loud, or "nie wieder montag"): take the plain reading, mark the beat with "?" in `beats.md`, and list the open words under the captions at the checkpoint card. Do not stop the run. Martin decides at the card.
- **Supported inference**: "visa agent ... verlängerung ... läuft 4.11. ab" lets you write "Our visa ends on 4 November". The dump supports it. An inference with no support in the dump is an added fact. Leave it out.
- **Times**: "6 uhr" with a morning activity is "6 am". "Uhr" with an evening activity is "pm". Unclear: "?" in beats.
- **Tense**: past tense for what happened today ("Celine had two client calls"). Present for states and insights ("Before 10 am we get more done"). Future for tomorrow and plans.
- **Note beats** (a wish, a loose remark): put them right before the close line, after the plans. Or drop them when they fit nowhere. Never force one into the day part.
- **Examples are shapes, not text to copy.** Never copy an example block when its words are not in today's dump.
- **Block count**: the validator range 12 to 60 is the hard limit. "1.5 to 2.5 blocks per dump line" is the guide.
