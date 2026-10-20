import json
U=json.load(open('units.json'))
G=("GLOBAL STYLE: Design the WHAT IS RHETORIC subpage (a calm explainer page for newcomers) of an existing website at 1440 px desktop width as ONE tall high-fidelity website mockup image, all 13 sections in this order, realistic like a finished premium website screenshot. "
"The attached tall image is the approved HOMEPAGE mockup of the same website: copy its exact visual language (colours, fonts, header capsule, buttons, cards, photo style, spacing, footer) so both pages clearly belong to one website. "
"Brand: me&you Communication, Michael Ehlers, rhetoric trainer with 3-day seminars in small groups. Colours: background warm off-white #FAF8F4, cream #F2EDE4 for alternate bands, sand #D8CCB7, dove blue #7E99B6 for small accents and numbers, navy #2B3C52 for one dark band and the footer, warm anthracite #47403A, text ink #2A2622. The ONLY strong button colour is deep dove blue #4F6D90 with white text, pill shape; on dark bands the button is cream with navy text. "
"Fonts: Libre Baskerville serif for all headlines and quotes, Inter sans for body, labels and buttons. Small overlines in letterspaced uppercase dove blue. Body text large and readable. Soft 22 px rounded corners, no hard lines, lots of white space. "
"Photos: real-looking candid reportage photography, natural light, light film grain, small groups, nobody looks at the camera except portraits of Michael, never stage, never conference, never hotel ballroom, no lanyards, no stock look. None of the other people is bald or wears glasses. "
"The man in the attached portrait photos is Michael Ehlers: use these real photos as they are, do not redraw his face, keep his exact face, bald head, short grey-white beard, light rectangular glasses and age. The attached logo file is the real brand logo: reproduce exactly this logo top left. "
"Header: floating white capsule with the logo left, menu items Seminare, Michael, Was ist Rhetorik (active, underlined), Stimmen, FAQ, and the button „Gespräch buchen“ right. "
"Use the following German text exactly as written, letter for letter, nothing invented, nothing shortened. Text inside the image is a placeholder for the build, the layout must give it the right size. ")
L={
'S01':"HERO: text left on warm off-white, the attached real photo of Michael (white shirt, sitting at a restaurant table, looking to the side) on the right fading into the off-white. Order: proof line with gold stars, small serif kicker in dove blue (H1 up to the question mark), big serif headline in 2 lines (the rest of the H1), italic serif subline, 3 lines body, one primary pill button (deep dove blue, white text) for the free video training, reassurance line with a small play icon, a small text link under it.",
'S02':"ANSWER BAND on cream: large serif H2 left, the definition as a big calm paragraph; right three small fact tiles about Michael.",
'S03':"MYTHS: four cards in a row, each with a small crossed-out label at the top, bold serif first sentence and 2 to 3 lines of text.",
'S04':"THREE MEANS OF PERSUASION: serif H2 and one line; three tall cards side by side, each with a big serif Greek word (Ethos, Pathos, Logos) in dove blue, the German word, 3 to 4 lines, an everyday example in italic; one closing paragraph; primary button.",
'S05':"FIVE STEPS OF A SPEECH: cream band, serif H2 and intro; a horizontal row of five numbered steps connected by a thin line, Latin word small under the German word, 2 lines each; one line about the book under it.",
'S06':"WHERE YOU NEED IT AT WORK: serif H2, intro, six small tiles in a 3 by 2 grid with a tiny line icon and a bold label, one closing paragraph.",
'S07':"TYPICAL MISTAKES: cream band, serif H2, five rows each with a small warning dot, bold mistake and the better way.",
'S08':"METHOD: dark navy band with the serif H2 in cream, intro paragraph, three columns numbered 01 02 03 (Persönlichkeit, Kongruenz, Wirkung) with one line each, a paragraph with a text link, light cream button.",
'S09':"THREE EXAMPLES: serif H2 and intro, three quote-style cards with a small microphone icon and the label Podcast Unübersehbar, title in serif and short text.",
'S10':"HOW TO LEARN: two columns. Left: serif H2 and paragraphs. Right: three numbered exercise cards. Under both the seminar paragraph with a text link and the primary button.",
'S11':"FREE TRAINING: feature box on cream: left a large 16:9 video still of Michael sitting in an armchair in a studio with a microphone and a white play button; right serif H2, paragraph with a yellow placeholder badge, paragraph, primary button.",
'S12':"FAQ: serif H2 left, accordion in two columns on the right, first question open, the others with plus icons, one line with a link.",
'S13':"CLOSING: dark photo band (evening terrace above the sea), cream text: serif H2, paragraph, three check marks, light cream button, a line of three text links. Then the navy footer with the white logo and four columns."}
out=[G]
for i,(k,lay) in enumerate(L.items(),1):
    out.append(f"SECTION {i} ({k}). LAYOUT: {lay} TEXT: "+' '.join('„'+u+'“' for u in U[k]))
out.append("Show placeholder text in square brackets as a small yellow highlighted badge. Output: one tall portrait image of the whole page, sharp text, no device frame, no watermark.")
p=' '.join(out); open('prompt.txt','w').write(p); print(len(p))
