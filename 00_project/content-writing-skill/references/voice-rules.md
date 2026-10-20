# Voice rules and the voice sheet

Sources: memory `always-du-with-prospects`, `client-emails-ich-form`, `program-deliverable-rules`, `behandler-seite` (Anrede), money-page standard B ("Konsistente Ansprache"), CRO R2.8.

- V1 Each client has ONE voice sheet: `00_project/assets/<client-slug>/voice.md`. Every run reads it. It is built once (step 1) and corrected when Martin or the client corrects a line.
- V2 The address form is du OR Sie, never mixed. The sheet gives it with proof (a quote from the live site). IF the client uses "du" on the live site THEN du. IF a law firm or a patient page uses "Sie" THEN Sie, even when 741 says "du" to the client. Prospects in German are "du" (memory), but a client's own site follows the client.
- V3 The speaker is one of: ich (the practitioner in first person), wir (the firm), dritte Person ("Dr. Anja Stürzl prüft …"). The sheet gives it per page type. Practitioner pages and blog posts: ich. Firm pages: wir. A person block can be third person plus one first-person quote.
- V4 Keep the client's own phrases and method names (with source). Do not smooth them out. They are the human part of the text.
- V5 Words the client never uses stay out. Words the clients use in reviews come in.
- V6 Tone in 5 words, for example "ruhig, klar, sachlich, ohne Floskeln". The tone check is part of the human-read score.
- V7 Target-group sentences are harmonious: name the focus, then "genauso bist du hier richtig, wenn …".
- V8 Client messages (emails, WhatsApp) use "ich", not "wir" (memory). This is outside page copy but the delivery note follows it.
- V9 English client pages: address "you", direct, plain words, no corporate phrases. The same slop gate runs with the English linter.
- V10 741.studio own voice is not decided yet (Martin, 2026-10-11). No run on 741.studio until a voice sheet exists.

## How the sheet is built (step 1)

The client's live website is the source of the voice (Martin, 2026-10-11). An approved page brief is a side source only. When the two differ, the live site wins and the difference goes to the open flags.

1. Scrape the live text of the home page, the about page, the FAQ page, the person page and 2 service pages. Quote 5 sentences that sound like the firm and note the slogans, the sentence rhythm, the question format and the person (wir or ich).
2. List the live-site words that break the legal rules (HWG or BRAO). They stay OUT of our copy and go to `OPEN-FLAGS.md`. The client decides about its own site.
3. Read the Google reviews if time allows. Quote 3 lines that show how clients talk about the work.
4. Read the 5 voice answers in the client form. If missing, add the 5 questions to the form draft (Martin decides if it goes out):
   1. Wie erklärst du einem neuen Patienten oder Mandanten in zwei Sätzen, was du machst?
   2. Welche Wörter benutzt du nie, weil sie nicht zu dir passen?
   3. Welcher Satz sagt dir ein Patient oder Mandant immer wieder?
   4. Wie soll sich jemand nach dem Lesen deiner Seite fühlen?
   5. Gibt es eine Seite oder einen Text von dir, der genau so klingt, wie du klingen willst?
5. Write `voice.md` from the template. Status "Entwurf" until Martin confirms du or Sie.
