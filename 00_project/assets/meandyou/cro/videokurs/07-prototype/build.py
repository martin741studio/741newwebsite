"""Build the me&you course sales/checkout page "Rhetorik für Intelligente" (desktop 1440 px) as a close
functional copy of the live https://www.meandyou.de/videokurs/start (Framer). Continuity for running Meta
ads, not a redesign. Published path on the assembled site is videokurs/start.html (nested, matches the
live URL) -- this script writes the primary source to 07-prototype/index.html AND a deploy copy straight
to ../../_site/videokurs/start.html (+ its own assets/ next to it), since site-build/assemble.py only
knows the single-level PAGES map and must not be edited from here; the main session wires this nested
page into assemble.py itself.
Live page facts (Firecrawl, 2026-10-24, maxAge 0, full re-fetch -- the first saved HTML in /tmp was truncated
mid-file and missing the pricing/FAQ/footer):
- Real checkout links actually in use (NOT the single link named in the task brief, which does not appear on
  the current live page): both pricing cards -> https://myablefy.com/s/michaelehlersandyoucommunication/
  rhetorik-fuer-intelligente/payment ; final CTA -> https://myablefy.com/s/meandyoucommunication/
  rhetorik-fuer-intelligente/payment . Domain is myablefy.com, not ablefy.com.
- The live page DOES show a price (Einmalzahlung EUR 999 / Ratenzahlung EUR 1.149) -- flagged per task
  instruction with a [von Kunde bestätigen] badge rather than silently kept or removed.
- All the mid-page "Jetzt Zugang sichern" buttons are same-page anchors to #pricing, not checkout links.
Run: python3 build.py"""
import importlib.util, json, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
SITE_OUT = os.path.join(HERE, '..', '..', '_site', 'videokurs')


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


tm = load('tm_build', os.path.join(HERE, '..', '..', 'termin', '07-prototype', 'build.py'))
rh = tm.rh
mic, sem, home = rh.mic, rh.sem, rh.home
e, CHECK, PLAY = home.e, home.CHECK, home.PLAY
fehlt = home.fehlt
TEL = tm.TEL
ICON = tm.ICON
PRICING = '#pricing'
ABLEFY_CARDS = 'https://myablefy.com/s/michaelehlersandyoucommunication/rhetorik-fuer-intelligente/payment'
ABLEFY_FINAL = 'https://myablefy.com/s/meandyoucommunication/rhetorik-fuer-intelligente/payment'


def btn(href=PRICING, label='Jetzt Zugang sichern', cls='btn'):
    return f'<a class="{cls}" href="{href}">{e(label)}</a>'


CSS = tm.CSS + r"""
/* videokurs/start course sales page */
.vk .sec{padding:92px 0}
.vk h2{text-align:center;max-width:36em;margin:0 auto}
.vk .center{text-align:center}
.vk .lead-center{text-align:center;max-width:34em;margin:18px auto 0;color:var(--muted);font-size:18.5px}
.vk__hero{padding-top:100px;text-align:center}
.vk__hero .wrap{max-width:820px;margin:0 auto;display:flex;flex-direction:column;gap:16px;align-items:center}
.vk__hero .ov{letter-spacing:.1em}
.vk__hero h1{font-size:48px;line-height:1.14}
.vk__hero .sub{font-size:19.5px;color:var(--muted);max-width:38em}
.credrow{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px}
.credcard{background:#fff;border-radius:var(--r);padding:24px 20px;text-align:center;font-size:15.5px;color:var(--muted);box-shadow:0 10px 26px rgba(42,38,34,.06)}
.credcard b{display:block;color:var(--ink);font:400 17px/1.3 var(--serif);margin-bottom:4px}
.story{max-width:720px;margin:0 auto;display:flex;flex-direction:column;gap:16px}
.story p{font-size:18.5px}
.outcomes{list-style:none;margin:36px auto 0;padding:0;max-width:640px;display:flex;flex-direction:column;gap:12px}
.outcomes li{display:flex;gap:10px;font-size:17.5px;text-align:left}
.outcomes li svg{width:20px;height:20px;color:var(--cta);flex:none;margin-top:4px}
.bio{max-width:680px;margin:0 auto;display:flex;flex-direction:column;gap:14px}
.bio p{font-size:18px}
.ausgezeichnet{text-align:center;max-width:640px;margin:0 auto}
.transform{list-style:none;margin:36px auto 0;padding:0;max-width:760px;columns:2;column-gap:32px}
.transform li{display:flex;gap:10px;font-size:16.5px;text-align:left;margin-bottom:14px;break-inside:avoid}
.transform li svg{width:18px;height:18px;color:var(--cta);flex:none;margin-top:3px}
.vk__faq .acc{max-width:760px;margin:36px auto 0}
.vk__faq details{border-bottom:1px solid var(--line);padding:16px 0}
.vk__faq summary{cursor:pointer;font:600 17px/1.4 var(--sans);color:var(--ink);list-style:none}
.vk__faq summary::-webkit-details-marker{display:none}
.vk__faq summary::before{content:'+ ';color:var(--cta)}
.vk__faq details[open] summary::before{content:'– '}
.vk__faq p{margin-top:10px;color:var(--muted);font-size:16px}
.pricing{display:grid;grid-template-columns:1fr 1fr;gap:28px;max-width:860px;margin:40px auto 0}
.pcard{background:#fff;border-radius:var(--r);padding:34px 30px;box-shadow:0 18px 50px rgba(42,38,34,.09);display:flex;flex-direction:column;gap:14px;border:1px solid rgba(71,64,58,.08)}
.pcard ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.pcard li{display:flex;gap:8px;font-size:15.5px;color:var(--muted)}
.pcard li svg{width:17px;height:17px;color:var(--cta);flex:none;margin-top:3px}
.pcard .tag{font:600 12.5px/1.2 var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--cta)}
.pcard .price{font:400 40px/1 var(--serif);color:var(--ink)}
.pcard .price-note{font-size:13.5px;color:var(--muted)}
.price-flag{display:block;margin-top:6px}
"""


def header():
    return f'''<header class="hdr hdr--min"><div class="hdr__in">
 <a class="hdr__logo" href="#top"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication" width="1794" height="647"></a>
 <a class="tel" href="{TEL}">{ICON['phone']}+49 15888367664</a>
</div></header>'''


def s_hero():
    return f'''
<section class="vk__hero" id="top">
 <div class="wrap">
  <p class="ov rv">Bereits über 8.000+ Teilnehmer:innen überzeugt</p>
  <p class="rv" style="color:var(--muted);font-size:16px">Der begleitete Online-Kurs mit Promi Rhetorik-Trainer Michael Ehlers</p>
  <h1 class="rv">Rhetorik für Intelligente</h1>
  <p class="sub rv">Endlich verstanden werden, ohne dich zu verstellen. Lerne in diesem Kurs so zu kommunizieren, dass du überzeugst und die Anerkennung bekommst, die du verdienst.</p>
  <div class="cta-row rv">{btn()}</div>
  <p class="rv" style="color:var(--muted);font-size:16px;max-width:36em">Du hast die besten Ideen im Raum, aber andere bekommen den Zuschlag? Das Problem ist nicht dein Wissen – sondern wie du es vermittelst. Du erklärst komplexe Sachverhalte, aber dein Gegenüber schaltet ab?</p>
  <div class="credrow rv">
   <div class="credcard"><b>Top 100</b>Trainer im DACH-Raum</div>
   <div class="credcard"><b>1.000+</b>Vorträge &amp; Medienauftritte</div>
   <div class="credcard"><b>Gründer</b>des Ehlers-Rhetorik-Frameworks</div>
   <div class="credcard"><b>30+ Jahre</b>Erfahrung als Rhetorik-Trainer</div>
  </div>
 </div>
</section>'''


def s_problem():
    return f'''
<section class="sec sec--cream">
 <div class="wrap">
  <h2 class="rv">Du bist der Klügste im Raum, aber niemand hört dir zu?</h2>
  <p class="lead-center rv">Warum brillante Menschen oft die schlechtesten Kommunikatoren sind</p>
  <div class="story" style="margin-top:36px">
   <p class="rv">Vielleicht kennst du Situationen wie die Folgende: Du sitzt in einem Meeting und erklärst deine Lösung. Aber statt Zustimmung bekommst du nur glasige Blicke zurück. Jemand im Raum unterbricht dich: „Können wir das vereinfachen?"</p>
   <p class="rv">Fünf Minuten später wiederholt ein Kollege deine Idee mit anderen Worten. Alle nicken begeistert. Und er bekommt das Lob …</p>
   <p class="rv"><b>Tatsächlich haben es intelligente Menschen oft schwerer mit der Kommunikation.</b></p>
   <p class="rv">Warum? Weil ihr Gehirn im Durchschnitt 5x mehr und schneller Lösungen feuert als bei anderen Menschen. Jetzt versuchst du, ihnen deine Lösung zu präsentieren – und was passiert?</p>
  </div>
 </div>
</section>'''


def s_good_news():
    outcomes = ['Seine Botschaft klar auf den Punkt bringt – und dessen Wert verständlich kommuniziert',
                'Andere in jedem Gespräch begeistert (sei es auf der Arbeit oder privat)',
                'Sofort Souveränität und Vertrauen ausstrahlt',
                'Aus jedem Gespräch das bekommt, was er will',
                'Gespräche gut führen und lenken kann',
                'Frei vor anderen spricht – und dabei mit Geschichten fesselt, die für immer im Kopf bleiben']
    li = ''.join(f'<li>{CHECK}<span>{e(x)}</span></li>' for x in outcomes)
    return f'''
<section class="sec">
 <div class="wrap">
  <h2 class="rv">Aber hier kommt die gute Nachricht:</h2>
  <p class="lead-center rv">Ich habe die besten Techniken aus über 30 Jahren Erfahrung als Rhetorik-Trainer in diesen Kurs gepackt.</p>
  <div class="ctabar rv">{btn()}</div>
  <p class="lead-center rv" style="margin-top:32px">Denn: Der Erfolgreichste ist letztlich nicht der, der mehr auf dem Kasten hat – sondern der, der besser kommunizieren kann. Und damit wirst du nach „Rhetorik für Intelligente" schonmal keine Schwierigkeiten mehr haben.</p>
  <p class="lead-center rv" style="margin-top:14px"><b>Und: Ich bin sehr zuversichtlich, dass dich „Rhetorik für Intelligente" in 30 Tagen zu dem Menschen macht, der:</b></p>
  <ul class="outcomes rv">{li}</ul>
 </div>
</section>'''


def s_bio():
    return f'''
<section class="sec sec--cream">
 <div class="wrap">
  <h2 class="rv center">Woher ich das weiß?</h2>
  <div class="bio" style="margin-top:28px">
   <p class="rv">Ich bin nun seit über 30 Jahren Rhetorik-Trainer und durfte in dieser Zeit über 8.000 Menschen ausbilden (und vor noch sehr viel mehr Menschen sprechen).</p>
   <p class="rv">Darunter bekannte Schauspieler, Moderatoren, Politiker, Fußballtrainer der Nationalmannschaft, Profi-Sportler, Führungskräfte, Unternehmer und – Speaker …</p>
   <p class="rv">Viele von ihnen stehen selbst auf den großen Bühnen, füllen Deutschlands Arenen und erreichen regelmäßig ein Millionenpublikum. Ich bin mir sicher: den Großteil davon kennst du auch.</p>
   <p class="rv">Was aber noch viel wichtiger ist: Zu mir kommen regelmäßig Menschen, die von sich denken, sie wären „keine großen Redner". Nach drei Dekaden als Rhetorik-Experte kann ich dir allerdings eines versichern: Jeder kann andere rhetorisch begeistern und fesseln. Völlig gleich, wie introvertiert du bist.</p>
   <p class="rv">Die Frage ist nur: wie? Und genau das bringe ich dir Stück für Stück in „Rhetorik für Intelligente" bei.</p>
  </div>
  <div class="ausgezeichnet rv" style="margin-top:40px">
   <h3>Ausgezeichnet statt austauschbar.</h3>
   <p style="color:var(--muted);font-size:17px;margin-top:10px">Michael Ehlers gehört laut ERFOLG Magazin zu den Top 100 Trainern im deutschsprachigen Raum &amp; ist Top10 Speaker. Vertrauen ist kein Zufall. Sondern das Ergebnis von 25 Jahren Bühnen, Medien, Boardrooms – und echten Ergebnissen.</p>
  </div>
  <div class="ctabar rv">{btn()}</div>
 </div>
</section>'''


def s_transform():
    T = ['Du kannst überzeugende Reden improvisieren – die deinen Zuhörern für immer im Gedächtnis bleiben',
         'Du gibst Feedback so, dass es dankend angenommen und umgesetzt wird',
         'Du hast auf jeden verbalen Angriff eine schlagfertige Antwort aus dem FF parat (oder, wie ich es gerne nenne: Du bist „wortmächtig")',
         'Dir wird nie wieder das richtige Wort zur richtigen Zeit fehlen',
         'Du gewinnst in Verhandlungen, weil du sie geschickt führen kannst',
         'Du kannst Gespräche mit hierarchischem Machtgefälle innerhalb von Sekunden auf Augenhöhe bringen (völlig gleich, wer dir gegenüber steht)',
         'Du öffnest selbst stark introvertierte und wortkarge Menschen, sodass sie gar nicht mehr aufhören können, zu reden',
         'Du führst oberflächlichen Smalltalk direkt in Gespräche mit Tiefe und Dimension (ohne unkontrolliertes Over-Sharing)',
         'Es fällt dir leicht, Gespräche zu eröffnen und einen guten Gesprächsfluss am Laufen zu halten']
    li = ''.join(f'<li>{CHECK}<span>{e(x)}</span></li>' for x in T)
    return f'''
<section class="sec">
 <div class="wrap">
  <h2 class="rv">Mit den Techniken aus „Rhetorik für Intelligente" wirst du nach diesem Training unter anderem folgende Veränderungen bemerken:</h2>
  <div class="ctabar rv">{btn()}</div>
  <ul class="transform rv">{li}</ul>
 </div>
</section>'''


def s_why_not():
    return f'''
<section class="sec sec--cream">
 <div class="wrap">
  <h2 class="rv">Warum die meisten Kommunikations-Trainings nicht funktionieren</h2>
  <p class="lead-center rv">Vielleicht hast du bereits Rhetorik-Kurse besucht, aber wirklich verändert hat sich noch nichts. Auf den meisten Seminaren lernst du: Gestik und Mimik – und sollst schauspielern; ein Publikum zu begeistern; Techniken, die sich falsch anfühlen.</p>
  <p class="lead-center rv" style="margin-top:18px"><b>→ In „Rhetorik für Intelligente" bringe ich dir NICHT bei, zu schauspielern.</b></p>
  <p class="lead-center rv" style="margin-top:12px">Du bleibst immer noch authentisch du selbst. Aber wir kristallisieren deine kommunikativen Fähigkeiten heraus, sodass sie sich nicht aufgesetzt anfühlen, sondern zu deinem Naturell passen. Schließlich wollen wir dich nicht auf einen einzigen Auftritt vorbereiten, sondern deine Rhetorik-Fähigkeiten sollen nachhaltig zu einem Teil deines persönlichen Auftretens werden.</p>
  <div class="ctabar rv">{btn()}</div>
 </div>
</section>'''


def s_voices():
    Q = [('„Ein begeisterndes Training mit einer anregenden und humorvollen Atmosphäre. Rundum gelungen."', 'Sarna Röser', 'Bundesvorsitzende „Die Jungen Unternehmer" Berlin'),
         ('„Trotz 40 Jahren Medienerfahrung konnte ich erstaunlich viel vom Rhetoriktraining profitieren."', 'Peter Escher', 'Moderator MDR'),
         ('„Das Seminar – oder egal, wie man es nennen mag – war einfach genial. Ich habe in diesem Kurs mehr gelernt als in all meinen bisherigen Schulungen zusammen."', 'Emrullah Ates', 'Teilnehmer'),
         ('„Ersteres ist manchmal genau so schwer wie Letzteres, deshalb ist das Training mit Michael unerlässlich, um eine bessere globale Zukunft aktiv mitzugestalten."', 'Neven Subotic', 'Fußball-Bundesliga-Profi')]
    q = ''.join(f'<article class="q3 rv"><blockquote>{e(x)}</blockquote><p class="src"><b>{e(n)}</b>, {e(s)}</p></article>' for x, n, s in Q)
    return f'''
<section class="sec">
 <div class="wrap">
  <h2 class="rv center">Was Kunden über Michael Ehlers sagen</h2>
  <div class="qgrid3" style="margin-top:36px">{q}</div>
 </div>
</section>'''


def s_included():
    return f'''
<section class="sec sec--cream">
 <div class="wrap">
  <h2 class="rv center">Was alles im „Rhetorik für Intelligente"-Programm enthalten ist</h2>
  <div class="story" style="margin-top:32px">
   <p class="rv"><b>40 Video-Lektionen mit Praxisübungen</b>, die dich in 30 Tagen zum Rhetorik-Profi machen. Strukturiert, praxisnah und so, dass du es sofort umsetzt.</p>
   <p class="rv"><b>Aktive Community.</b> Rhetorik lebt vor allem davon, dass du es trainierst. In der Community tauschst du dich mit anderen intelligenten Menschen aus, holst dir regelmäßig Feedback ein und gibst selbst auch Feedback.</p>
   <p class="rv"><b>Begleitendes Workbook</b>, damit du bei jeder Lektion direkt mitarbeitest.</p>
   <p class="rv"><b>2x pro Monat Live-Q&amp;A's.</b> Hier hast du die Möglichkeit auf deinen 1:1-Coaching-Moment mit mir. Die Live-Q&amp;A's werden auch aufgezeichnet und dir anschließend zur Verfügung gestellt, falls du mal nicht dabei sein kannst.</p>
  </div>
  <div class="ctabar rv">{btn()}</div>
 </div>
</section>'''


def s_pricing():
    feat = ['40+ Video-Lektionen', 'Community-Feedback', '20+ Workbooks zum Mitarbeiten', '2 Jahre Zugang', '2x pro Monat Live-Q&amp;A']
    fli = ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in feat)
    return f'''
<section class="sec" id="pricing">
 <div class="wrap">
  <h2 class="rv">Sichere dir „Rhetorik für Intelligente" und fange heute noch an, Menschen zu begeistern</h2>
  <p class="lead-center rv">{fehlt('')}</p>
  <div class="pricing rv">
   <div class="pcard">
    <span class="tag">Bequeme Einmalzahlung</span>
    <ul>{fli}</ul>
    <span class="price">€ 999</span>
    <span class="price-note">Mit einer Zahlung alles erledigt.</span>
    {btn(ABLEFY_CARDS)}
   </div>
   <div class="pcard">
    <span class="tag">Cashflow-freundlich: Ratenzahlung</span>
    <ul>{fli}</ul>
    <span class="price">€ 1.149</span>
    <span class="price-note">Ratenzahlung in 2 oder 4 Teilzahlungen möglich.</span>
    {btn(ABLEFY_CARDS)}
   </div>
  </div>
 </div>
</section>'''


FAQ = [
 ('Kann ich mir das nicht auch einfach auf YouTube beibringen?', 'Theoretisch ja – praktisch nein. YouTube zeigt dir Puzzleteile, aber kein System. Du bräuchtest Monate, um die richtigen Videos zu finden, und hättest trotzdem kein strukturiertes Vorgehen. Hier bekommst du ein durchdachtes System, Community und Feedback. Zeit ist Geld – und deine Zeit ist wertvoll.'),
 ('Ich bin sehr introvertiert, ist dieser Kurs trotzdem für mich?', 'Gerade dann ist dieser Kurs für dich gemacht. Rhetorik bedeutet nicht, lauter oder extrovertierter zu sein, sondern Wirkung zu erzielen. Introvertierte überzeugen oft durch Präzision und Ruhe. Mit den richtigen Techniken nutzt du deine Stärken, ohne dich zu verbiegen.'),
 ('Was, wenn ich keine Fortschritte in meiner Rhetorik mache?', 'Rhetorik ist ein Handwerk. Wer trainiert, verbessert sich. Setzt du die Übungen um, bekommst du spürbare Ergebnisse. Wenn du hängst, sorgen Feedback und klare Anleitungen dafür, dass du garantiert vorankommst.'),
 ('Kann ich dir meine Fragen auch persönlich stellen?', 'Ja. Neben dem Videotraining gibt es Austausch, Q&A und Feedback-Möglichkeiten – so erhältst du individuelle Antworten direkt von einem Rhetorik-Profi.'),
 ('Der Kurs ist mir zu teuer …', 'Die eigentliche Frage lautet: Was kostet es dich, nicht überzeugend zu kommunizieren? Verpasste Aufträge, überhörte Ideen, verlorene Chancen – das ist der wahre Preis. Der Kurs ist eine Investition, die sich schnell auszahlt.'),
 ('Ich möchte meine Rhetorik verbessern, aber habe kaum Zeit …', 'Perfekt – die Lektionen sind kurz und wirksam. In kleinen Einheiten baust du kontinuierlich Wirkung auf und kannst alles flexibel in deinen Alltag integrieren.'),
 ('Ich habe schon viele Bücher über Kommunikation gelesen. Reicht das nicht?', 'Theorie ohne Umsetzung bleibt Wissen. Hier trainierst du aktiv, bekommst Feedback und entwickelst Routinen, die in Meetings, Pitches und Gesprächen sofort tragen.'),
 ('Ich habe bereits Kommunikations-Trainings gemacht. Lerne ich hier noch etwas Neues?', 'Ja. Aktuelle Erkenntnisse treffen auf über 25 Jahre Praxis aus Politik, Medien und Wirtschaft. Viele erfahrene Teilnehmer berichten: „Ich habe noch einmal ein neues Niveau erreicht."'),
 ('Woher weiß ich, ob ich überhaupt „intelligent" bin?', 'Es geht nicht um einen IQ-Wert, sondern um Haltung: reflektiert lernen, bewusst auftreten, mehr Wirkung wollen. Wenn das auf dich zutrifft, bist du hier richtig.'),
 ('Ist das ein rein theoretischer Selbstlernkurs oder gibt es auch persönliche Betreuung?', 'Beides: ein klar strukturiertes System für dein Tempo, plus persönliche Betreuung durch Q&A, Feedback und Community. Du bleibst nie allein mit deinen Fragen.'),
 ('Wie lange habe ich Zugang zum Online-Kurs und der Community?', f'Mindestens 12 Monate. Du kannst Inhalte wiederholen, Fortschritte festigen und dich dauerhaft mit der Community austauschen. {fehlt("")}'),
 ('Muss ich mich verstellen oder schauspielern?', 'Nein. Rhetorik heißt, authentisch Wirkung zu erzielen. Nicht anders werden – klarer werden. Die Technik unterstützt deine Persönlichkeit.'),
]


def s_faq():
    qa = ''.join(f'<details class="rv"><summary>{e(q)}</summary><p>{a}</p></details>' for q, a in FAQ)
    return f'''
<section class="sec sec--cream vk__faq">
 <div class="wrap">
  <h2 class="rv center">Hier findest du Antworten auf mögliche Fragen und Einwände</h2>
  <div class="acc">{qa}</div>
 </div>
</section>'''


def s_final_cta():
    return f'''
<section class="closer closer--plain" id="abschluss">
 <div class="wrap"><div class="closer__in">
  <h2 class="rv">Starte heute noch mit „Rhetorik für Intelligente" und verwandle deine Brillanz in überzeugende Kommunikation, die anderen im Gedächtnis bleibt.</h2>
  <div class="cta-row rv">{btn(ABLEFY_FINAL, cls="btn btn--light cta--breathe")}</div>
 </div></div>
</section>'''


def footer():
    return f'''<footer class="foot foot--min">
 <div class="wrap foot__in">
  <div><img src="assets/logo-light.png" alt="Michael Ehlers &amp; You Communication" width="1794" height="647"></div>
  <nav class="legal" aria-label="Rechtliches"><a href="../impressum.html">Impressum</a><a href="../datenschutz.html">Datenschutz</a><a href="../agb.html">AGB</a></nav>
  <div class="kon"><h4>Kontakt</h4><a href="{TEL}">+49 15888367664</a><a href="mailto:management@meandyou.de">management@meandyou.de</a><a href="https://www.instagram.com/michael_ehlers_rhetorik/">Instagram</a><a href="https://de.linkedin.com/in/rhetoriktrainer">LinkedIn</a></div>
 </div>
</footer>'''


def schema():
    ORG = 'https://www.meandyou.de/#organization'
    g = [{"@type": "WebPage", "@id": "https://www.meandyou.de/videokurs/start#webpage", "url": "https://www.meandyou.de/videokurs/start",
          "name": "Rhetorik für Intelligente · Online-Kurs mit Michael Ehlers", "inLanguage": "de", "publisher": {"@id": ORG}},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Me&You Communication FZCO", "alternateName": "me&you Communication",
          "url": "https://www.meandyou.de/", "email": "management@meandyou.de"}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


def page(asset_prefix='assets/', legal_prefix='../'):
    body = header() + f'<main class="vk">' + s_hero() + s_problem() + s_good_news() + s_bio() + s_transform() + s_why_not() + s_voices() + s_included() + s_pricing() + s_faq() + '</main>' + s_final_cta() + footer() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    html = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Rhetorik für Intelligente · Online-Kurs mit Michael Ehlers</title>
<meta name="description" content="Der begleitete Online-Kurs mit Rhetorik-Trainer Michael Ehlers. 40 Video-Lektionen, Community, Workbook und Live-Q&amp;A.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema()}</script>
</head><body>{body}<script>{home.JS}</script></body></html>'''
    return html


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))

    # deploy copy at the required nested path cro/_site/videokurs/start.html, so the main
    # session can pick it up when it re-runs assemble.py / extends it for this nested page.
    os.makedirs(SITE_OUT, exist_ok=True)
    open(os.path.join(SITE_OUT, 'start.html'), 'w', encoding='utf-8').write(out)
    assets_dst = os.path.join(SITE_OUT, 'assets')
    if os.path.isdir(assets_dst):
        shutil.rmtree(assets_dst)
    shutil.copytree(os.path.join(HERE, 'assets'), assets_dst)
    print('deploy copy ->', os.path.join(SITE_OUT, 'start.html'))
