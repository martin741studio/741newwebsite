# German AI tells (slop gate G5)

The machine list is `de-tells.json`. This page explains it. Start list v1, 2026-10-11. Martin can veto a word: the entry moves to the "allowed" list below and out of the JSON in the same edit.

**Why this exists.** The slopmonster linter (`deslop.py`) has an English word list. A German test text full of tells scored 5/5 CLEAN. So `scripts/deslop_de.py` scores German with this list. English text goes to the original linter.

## Five groups (one point each, 5/5 to pass)

1. **Vocabulary.** Hard words fail at one hit: ganzheitlich, nahtlos, maßgeschneidert, eintauchen, wegweisend, bahnbrechend, Synergie, Eckpfeiler, "auf Augenhöhe", "in der heutigen schnelllebigen Welt", "es ist wichtig zu beachten", "spielt eine entscheidende Rolle", "Reise" in the sense of process, and similar. Soft words (individuell, nachhaltig, innovativ, kompetent, professionell, umfassend, optimal, hochwertig, effektiv, transparent, …) fail only at 4 or more in one text.
2. **Constructions.** "nicht nur …, sondern auch …", "es geht nicht um X, sondern um Y", "mehr als nur", "Ob … oder …, wir …", "Egal ob … oder", Zeitgeist-Einstieg ("In der heutigen …"), closing summary words at a sentence start (zusammenfassend, abschließend, Fazit), self-answered question ("Das Ergebnis?"), "Wir verstehen, wie belastend …".
3. **Punctuation.** Any Gedankenstrich (— or –) or " - " used as a dash. Three or more exclamation marks.
4. **Rhythm.** Three or more lists of exactly three items ("A, B und C"). Sentence lengths too even (spread under 3,5 words over 8 or more sentences).
5. **Invented proof.** A number with a noun ("über 500 Mandanten", "98 %", "seit 2008") that no claim in `claims.json` backs.

## What the linter reads

Visible text only: no frontmatter, no `<!-- TECH -->` block, no HTML comments, no placeholders.

## Allowed (Martin's vetoes)

None yet. Candidates to decide: "auf Augenhöhe", "individuell", "transparent" (many law and health clients use them honestly). Until Martin decides, they stay on the list.

## What a pass does not mean

5/5 means no tell found. It does not mean the text is good. The scorecard line "human read" checks one concrete detail per section, varied sentence length and the voice sheet.

## Cleanse prompt

`prompts/cleanse-de.txt` runs on a different model family than the writer (GPT via codex). After it: `diff_claims.py diff` guards numbers, claims, placeholders, section IDs and length. Then the lint runs again.
