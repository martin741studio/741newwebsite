import json
U=json.load(open('units.json'))
G=("GLOBAL STYLE: Design the FAQ subpage (a calm, well ordered page of frequently asked questions, grouped in seven topics) of an existing website at 1440 px desktop width as ONE tall high-fidelity website mockup image, all 10 sections in this order, realistic like a finished premium website screenshot. "
"The attached tall image is the approved HOMEPAGE mockup of the same website: copy its exact visual language (colours, fonts, header capsule, buttons, cards, photo style, spacing, footer) so both pages clearly belong to one website. "
"Brand: me&you Communication, Michael Ehlers, rhetoric trainer with 3-day seminars in small groups. Colours: background warm off-white #FAF8F4, cream #F2EDE4 for alternate bands, sand #D8CCB7, dove blue #7E99B6 for small accents and numbers, navy #2B3C52 for the footer, warm anthracite #47403A, text ink #2A2622. The ONLY strong button colour is deep dove blue #4F6D90 with white text, pill shape; on dark bands the button is cream with navy text. "
"Fonts: Libre Baskerville serif for all headlines, group titles and quotes, Inter sans for body, questions, labels and buttons. Small overlines in letterspaced uppercase dove blue. Body text large and readable. Soft 22 px rounded corners, thin hairline dividers between accordion rows, lots of white space. "
"Accordion style: each question is one row with the question in Inter semibold 18 px and a small plus icon right; the first question of every group is open and shows its answer below in regular text; all other rows are closed (show only the question). "
"The man in the attached portrait photos is Michael Ehlers: use these real photos as they are, do not redraw his face, keep his exact face, bald head, short grey-white beard, light rectangular glasses and age. The attached logo file is the real brand logo: reproduce exactly this logo top left. "
"Header: floating white capsule with the logo left, menu items Seminare, Michael, Was ist Rhetorik, Stimmen, FAQ (active, underlined), and the button „Gespräch buchen“ right. "
"Use the following German text exactly as written, letter for letter, nothing invented, nothing shortened. For closed accordion rows the answer text is given for completeness, show only the question. Text inside the image is a placeholder for the build, the layout must give it the right size. ")
L={
'S01':"HERO, compact (about 620 px tall): text left on warm off-white, the attached real photo of Michael smiling in a white shirt leaning on a wooden door frame on the right in a tall rounded frame. Order: proof line with gold stars, small serif kicker line in dove blue, big serif H1 „Häufige Fragen“ with the rest of the H1 as smaller second line, one intro paragraph, then a row of seven rounded topic chips (outlined pills with small numbers 01 to 07) as jump navigation, then the primary pill button (deep dove blue, white text) and a reassurance line under it.",
'S02':"SHORT ANSWER BAND on cream: left the serif H2 and the answer paragraph in a large calm serif size; right four white fact tiles in a 2 by 2 grid with a big number and a short label; a quote line in italic serif with the name under the tiles.",
'S03':"GROUP 01 on off-white: two columns. Left a sticky column (about 30 %): big dove blue number 01, serif group title, a text link to the detail page, and the primary button. Right (70 %): the accordion with the questions of this group.",
'S04':"GROUP 02 on cream: same two-column pattern, number 02. Above the accordion a slim row of six small place names as pills. Under the accordion a small italic line with the date stand.",
'S05':"GROUP 03 on off-white: same pattern, number 03, no button, the accordion rows split into two columns because there are many.",
'S06':"GROUP 04 on cream: same pattern, number 04, the price question open first, a small text link to the free video, primary button left.",
'S07':"GROUP 05 on off-white: same pattern, number 05. Left column additionally a small white card „30 Minuten, kostenlos, per Video“ with the button.",
'S08':"GROUP 06 on cream: same pattern, number 06, left column shows a small rounded real portrait of Michael (attached photo in a brown jacket) above the group title.",
'S09':"GROUP 07 on off-white: same pattern, number 07, accordion in two columns, a text link line at the end.",
'S10':"CLOSING: dark photo band (evening stone terrace above the sea, people talking, warm light, dark overlay), cream text: serif H2, paragraph, three check marks, the proof line, light cream pill button, phone line, a back link. Then the navy footer with the white logo and four columns, like the homepage."}
out=[G]
for i,(k,lay) in enumerate(L.items(),1):
    out.append(f"SECTION {i} ({k}). LAYOUT: {lay} TEXT: "+' '.join('„'+u+'“' for u in U[k]))
out.append("Show placeholder text in square brackets as a small yellow highlighted badge. Output: one tall portrait image of the whole page, sharp text, no device frame, no watermark.")
p=' '.join(out); open('prompt.txt','w').write(p); print(len(p))
