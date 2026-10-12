import json, re
U = json.load(open('units.json'))
G = ("GLOBAL STYLE: Design a persona LANDING PAGE of an existing website at 1440 px desktop width as ONE tall high-fidelity website mockup image, all 13 sections in this order, realistic like a finished premium website screenshot. "
"The attached tall image is the approved HOMEPAGE mockup of the same website: copy its visual language (fonts, header capsule, pill buttons, cards, spacing, footer) so both pages belong to one website. "
"This page speaks to ONE persona, THE OVERLOOKED: experts who are right but not followed. Tone: composed, structured, precise, credible, unsentimental, cool light, respects the reader's intelligence, never motivational. "
"Visual rules for this persona: a visible thin grid with aligned hairlines, numbered steps 01 02 03, a diagram instead of decoration, clean comparison tables with thin dove-blue rules, captions under images and diagrams that carry real information. "
"Colours: COOL variant of the brand. Hero and one later band in navy #2B3C52 with cream text; other bands alternate cool off-white #F6F6F4 and light grey #E7E8E8; dove blue #7E99B6 for numbers, overlines and hairlines; ink #2A2622 for text; sand #D8CCB7 only as a tiny accent. "
"The ONLY strong button colour is deep dove blue #4F6D90 with white text, pill shape; on navy bands the button is cream #F2EDE4 with navy text. Every button has the same label. "
"Fonts: Libre Baskerville serif for headlines, numbers and quotes, Inter sans for body, tables, labels and buttons. Small overlines in letterspaced uppercase dove blue. Body text large and readable. Soft 18 px rounded corners on cards. "
"Photos: architectural, cool daylight, harder light, glass and steel lines, people in context seen with slight distance, black and white allowed. Never stage, never conference hall, never hotel ballroom, no stock look. "
"The man in the attached portrait photo is Michael Ehlers: keep his exact face, bald head, short grey-white beard, light rectangular glasses, brown jacket and age; do not invent a different person. The other attached photo shows the wanted hero mood (Michael at a glass table in a glass-walled office). The attached logo file is the real brand logo: reproduce exactly this logo. "
"Header: floating white capsule with the logo left, menu items Seminare, Michael, Was ist Rhetorik, Stimmen, FAQ, and the button „Gespräch buchen“ right. "
"Use the following German text exactly as written, letter for letter, nothing invented, nothing shortened. Text inside the image is a placeholder for the build; the layout must give it the right size. ")
L = {
'S01': "HERO on navy: text left in a visible grid, a large architectural photo right (Michael at a glass conference table in a glass-walled office, cool daylight, steel window frames, slightly desaturated) with a one-line caption under the photo. Order: H1 in two parts: small dove-blue serif kicker (up to the colon) and a very big cream serif headline in 2 lines (the rest); then the situation line in larger sans; then body; then a proof line with five small sand stars; then ONE cream pill button; then the reassurance line in small cream text.",
'S02': "PROOF STRIP on light grey directly under the hero: left a small real portrait of Michael (round crop), then four numbers in a row separated by thin vertical hairlines (big serif number, small label under it), right one short serif quote in italic with the source line and a small yellow placeholder badge.",
'S03': "DIRECT ANSWER on cool off-white: big serif H2 left (2 lines), right the answer paragraph in large text; under it a small numbered list of three practice parts as three slim columns with hairlines; then the podcast sentence as a pull quote with a small microphone icon and the caption Podcast Unübersehbar.",
'S04': "THREE SITUATIONS on light grey: serif H2; three cards side by side, each with a big dove-blue serif number 01 02 03, bold first sentence and the text; one summary line; the audience line; primary button and reassurance line.",
'S05': "METHOD AS A DIAGRAM on navy: serif H2 in cream left, intro paragraph; a horizontal diagram of three boxes 01 Persönlichkeit, 02 Kongruenz, 03 Wirkung connected by a thin arrow line, each box with its line and the guiding question as a caption under it; a small yellow placeholder badge.",
'S06': "COMPARISON TABLE on cool off-white: serif H2, intro; a two-column comparison table (left column muted grey, right column with a dove-blue top rule and slightly highlighted), three rows; one line under it; a quote in italic serif with source; primary button.",
'S07': "TRAINING TOPICS TABLE on light grey: serif H2, intro; a three-column table with numbered rows (Situation, Was du trainierst, Seminar), the seminar column as small dove-blue tags; one paragraph under it with a yellow placeholder badge and a text link.",
'S08': "FORMAT TABLE on cool off-white: serif H2, intro; a four-column table (row labels left; columns Online-Kurs, Seminar, Gespräch; the Gespräch column highlighted with a light dove-blue background); a yellow placeholder badge inside one cell; one paragraph with a placeholder badge; primary button and reassurance line.",
'S09': "FIRST STEP on light grey: serif H2; three numbered steps on one horizontal line with circles 1 2 3, each with bold title and text; a short cost line; primary button.",
'S10': "MICHAEL: two columns on cool off-white: left a large real photo of Michael (the attached portrait, brown jacket, light room) with a caption; right serif H2, one paragraph, a clean two-column evidence table with six rows (Rolle, Beleg) separated by hairlines, a closing line with a text link.",
'S11': "VOICES on light grey: serif H2, intro line; four open quote cards in a 2 by 2 grid (no carousel), each with a small bold heading, the quote in serif italic and the source; under them three vertical video thumbnails with play buttons; a text line; primary button.",
'S12': "FAQ on cool off-white: serif H2 left, accordion in two columns on the right, first question open, the others closed with plus icons; one line with links under it.",
'S13': "CLOSING on navy with a subtle thin grid pattern: cream serif H2, paragraph, three check marks, proof line with five small sand stars, ONE cream pill button, phone line. Then the navy footer with the white logo and four columns."}
out = [G]
def q(t):
    parts = [p.strip() for p in re.split(r'[„“]', t) if p.strip()]
    return ' '.join('„' + p + '“' for p in parts)
for i, (k, lay) in enumerate(L.items(), 1):
    texts = []
    for u in U[k]:
        if ' | ' in u:
            texts.append('TABLE ROW: ' + ' | '.join(q(c) if c != '·' else '(empty)' for c in u.split(' | ')))
        else:
            texts.append(q(u))
    out.append(f"SECTION {i} ({k}). LAYOUT: {lay} TEXT: " + ' '.join(texts))
out.append("Show placeholder text in square brackets as a small yellow highlighted badge. Output: one tall portrait image of the whole page, sharp text, no device frame, no watermark.")
p = ' '.join(out).replace('\n', ' ')
open('prompt.txt', 'w').write(p); print(len(p))
