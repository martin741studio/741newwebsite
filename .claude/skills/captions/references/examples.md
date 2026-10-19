# Example pairs: dump line to caption block

From the hand run of 2026-10-19 (sample dump). Each pair shows the dump line, the beat and the block.

## Pair 1: a day beat with numbers

Dump: `6 uhr surfen batu bolong, wellen klein, 40 min drin`
Beat: surf at 6, Batu Bolong, small waves, 40 min (day)
Block:
```
3. 6 am. Surf at Batu Bolong.
   Small waves, 40 minutes in.
```
Why: time as "6 am". Place as in the dump. "40 min" becomes "40 minutes". 11 words ("6" and "am." count as two), 2 lines, longest line 28 characters. The first try "Surfing at Batu Bolong. Small waves, 40 minutes in the water." had 13 words and failed the validator.

## Pair 2: a money beat with German number format

Dump: `budget talk: wir leben hier von 2.500 euro im monat für uns beide. villa 1.100, scooter 70, essen ca 600, rest sparen/puffer`
Beat: budget 2.500 a month for both, villa 1.100, scooter 70, food ca 600, rest savings (money)
Blocks:
```
1. We live here on 2,500 euros a month.

9. Villa: 1,100 euros.
   Scooter: 70 euros.

10. Food: about 600 euros.
    The rest goes into savings.
```
Why: the strongest number is the hook (block 1). The dump says "hier", so the caption says "here", not "Bali". The first hand run wrote "in Bali" and the functional test caught it. German 2.500 becomes 2,500. "ca" becomes "about". "sparen/puffer" becomes "savings". One kind of fact per block.

## Pair 3: an insight beat, too long at first

Dump: `insight: vor 10 uhr schaffen wir mehr als den ganzen nachmittag. deep work morgens, calls nachmittags`
First try (rejected, 14 words): "Insight of the day: before 10 am we get more done than all afternoon."
Blocks:
```
13. Before 10 am we get more done
    than the whole afternoon.

14. Deep work in the morning.
    Calls in the afternoon.
```
Why: the label "Insight of the day" costs words and adds nothing. Split one dump line into two blocks when it has two ideas.

## Pair 4: a date and a plan

Dump: `morgen: visa agent anschreiben wegen verlängerung, läuft 4.11. ab`
Block:
```
16. Tomorrow: message the visa agent.
    Our visa ends on 4 November.
```
Why: "4.11." becomes "4 November". The validator accepts the parts 4 and 11 from the dump. Nothing about the agent's name or the cost, the dump has none.

## Anti-example: an added fact

Dump: `abends warung bu made, nasi campur 35k, regen`
Wrong: "Evening at Warung Bu Made, our favourite." The dump does not say favourite.
Right:
```
15. Evening at Warung Bu Made.
    Nasi campur, 35k. And rain.
```
