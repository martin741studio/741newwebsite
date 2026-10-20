"""Build the CRO prototype of the me&you Michael page (desktop 1440 px). Text = 04-copy/approved-copy.md.
Design system = homepage prototype + seminar page additions (imported). Run: python3 build.py -> index.html"""
import importlib.util, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


sem = load('sem_build', os.path.join(HERE, '..', '..', 'seminare', '07-prototype', 'build.py'))
home = sem.home
V2 = sem.V2
BOOK = V2 + 'termin.html?utm_source=michael&utm_content='
TEL = sem.TEL
e, STARS, CHECK, t = home.e, home.STARS, home.CHECK, sem.t


def btn(utm, cls='btn'):
    return f'<a class="{cls}" href="{BOOK}{utm}">Gespräch buchen</a>'


CSS = sem.CSS + r"""
/* michael page additions */
.hero--split .hero__img{width:44%}
.hero--split .hero__img img{object-position:50% 30%}
.tl{position:relative;display:grid;grid-template-columns:repeat(5,1fr);gap:28px;margin-top:56px}
.tl::before{content:"";position:absolute;left:0;right:0;top:15px;height:2px;background:var(--line)}
.tl__i{position:relative;display:flex;flex-direction:column;gap:12px;padding-top:44px}
.tl__i::before{content:"";position:absolute;top:7px;left:0;width:18px;height:18px;border-radius:50%;background:var(--paper);border:2px solid var(--cta)}
.tl__i b{font:400 30px/1 var(--serif);color:var(--cta)}
.tl__i p{font-size:17px;color:var(--muted)}
.tl-text{margin-top:48px;max-width:48em;font-size:18px;color:var(--muted)}
.motto{font-size:46px;text-align:center;max-width:20em;margin:0 auto}
.motto-sub{text-align:center;max-width:40em;margin:20px auto 0;font-size:18px;color:var(--muted)}
.trio-h{font:italic 400 24px/1.3 var(--serif);color:var(--cta);margin-bottom:6px}
.trio{display:grid;grid-template-columns:.8fr 1.2fr;gap:64px;align-items:center;margin-top:64px}
.trio .portrait{height:600px}
.trio-list{display:flex;flex-direction:column;gap:22px}
.trio-list h3{font-size:24px;margin-bottom:6px}
.trio-list p{font-size:17px;color:var(--muted)}
.books{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.book{border-radius:16px;padding:26px 24px;min-height:120px;display:flex;align-items:flex-end;font:400 19px/1.35 var(--serif)}
.book:nth-child(3n+1){background:var(--navy);color:var(--on-dark)}
.book:nth-child(3n+2){background:var(--sand);color:var(--ink)}
.book:nth-child(3n){background:#fff;color:var(--ink)}
.pod{margin-top:22px;background:#fff;border-radius:var(--r);padding:28px 32px;display:grid;grid-template-columns:auto 1fr;gap:22px;align-items:start}
.pod svg{width:34px;height:34px;color:var(--cta);margin-top:2px}
.pod p{font-size:17px;color:var(--muted)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:56px;margin-top:48px}
.two h3{color:#fff;font-size:26px;margin-bottom:12px}
.two p{color:rgba(242,237,228,.85);font-size:17px}
.erf{display:flex;align-items:center;gap:20px;margin-top:44px;color:rgba(242,237,228,.85);font-size:17px}
.erf img{height:110px;width:auto;border-radius:6px}
.grp{border-radius:var(--r);overflow:hidden;height:700px}
.grp img{width:100%;height:112%;object-fit:cover;object-position:8% 70%}
"""

ICON_MIC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3M8.5 21h7"/></svg>'


def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="{V2}index.html"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="{V2}seminare.html">Seminare</a><a href="#top" aria-current="page" style="color:var(--cta)">Michael</a><a href="{V2}rhetorik.html">Was ist Rhetorik</a><a href="#stimmen">Stimmen</a><a href="#faq">FAQ</a></nav>
 {btn('header')}
</div></header>'''


def s01():
    return f'''
<section class="hero hero--split" id="top">
 <div class="hero__img"><img data-plx src="assets/michael-chair.webp" alt="Michael Ehlers, Rhetoriktrainer, sitzt im Ledersessel" width="720" height="1280"></div>
 <div class="wrap hero__in"><div class="hero__txt">
  <p class="proofline rv">{STARS} 227 von 250 Bewertungen mit 5 Sternen auf ProvenExpert · über 8.000 Teilnehmer</p>
  <h1 class="rv"><span class="kicker">Michael Ehlers, Rhetoriktrainer:</span><span class="big">Dreißig Jahre<br>vor vollen Räumen.</span></h1>
  <p class="sub rv">Autorität, die man nicht behaupten muss.</p>
  <p class="body rv">Michael Ehlers arbeitet seit 1990 als Rhetoriktrainer. Seit über 30 Jahren trainiert er in Seminaren und im Coaching Menschen, deren Worte Gewicht haben. Er lehrt auch an der Universität St. Gallen.</p>
  <div class="cta-row rv">
   <div class="btns">{btn('hero', 'btn cta--breathe')}<a class="btn btn--ghost" href="{V2}seminare.html">Seminare ansehen</a></div>
   <p class="assure">{CHECK}30 Minuten, kostenlos, per Video. Du klärst, welches Seminar zu dir passt.</p>
  </div>
 </div></div>
</section>'''


def s02():
    logos = ''.join(f'<img src="assets/logo-{n}.webp" alt="{a}">' for n, a in [('zdf', 'ZDF'), ('ard', 'ARD'), ('rtl', 'RTL'), ('stern', 'stern'), ('mdr', 'MDR'), ('hr2', 'hr2')])
    facts = [('Seit 1990:', 'Rhetoriktraining, heute über 8.000 Teilnehmer'), ('Neun Bücher', 'als Autor oder Herausgeber'), ('St. Gallen:', 'Lehrbeauftragter an der Universität'),
             ('Medien:', 'Rhetorik-Analyst für ARTE und WELT TV'), ('Podcast:', '„Unübersehbar“ seit 2008')]
    b = ''.join(f'<div class="badge"><b>{k}</b><span>{e(v)}</span></div>' for k, v in facts)
    return f'''
<section class="proof" id="kurz">
 <div class="wrap">
  <div class="proof__grid">
   <div class="proof__ans rv"><h2>Wer ist Michael Ehlers?</h2>
    <p>Michael Ehlers ist Rhetoriktrainer und Executive Coach. Seit 1990 bereitet er Menschen auf Auftritte und Gespräche vor, bei denen jedes Wort zählt. Er hat neun Bücher geschrieben oder herausgegeben und lehrt Rhetorik an der Universität St. Gallen.</p></div>
   <div class="rv" data-in><div class="factgrid">{b}</div></div>
  </div>
  <div class="media rv"><span>Michael Ehlers in den Medien: ZDF, ARD, RTL, stern, MDR, hr2</span>{logos}</div>
 </div>
</section>'''


def s03():
    items = [('1990.', 'Michael Ehlers gibt sein erstes Rhetorikseminar.'), ('2008.', 'Er beginnt seinen Podcast, den es bis heute gibt: „Unübersehbar“.'),
             ('2014.', 'Als Motivationstrainer „Hein Hansen“ schreibt er das Buch „Der Fisch stinkt vom Kopf“.'), ('2018.', 'Es erscheint „Rhetorik. Die Kunst der Rede im digitalen Zeitalter“.'),
             ('Heute.', 'Er lehrt an der Universität St. Gallen. Als Rhetorik-Analyst ordnet er Auftritte im Fernsehen ein.')]
    c = ''.join(f'<div class="tl__i rv"><b>{y}</b><p>{e(p)}</p></div>' for y, p in items)
    return f'''
<section class="sec" id="werdegang">
 <div class="wrap">
  <h2 class="rv">Aus der Praxis entstand ein Beruf</h2>
  <div class="tl">{c}</div>
  <p class="tl-text rv">Aus dem Rhetoriktraining wurde mit den Jahren eine Beratung. Sie reicht heute von der Vorbereitung eines einzelnen Auftritts bis zur Begleitung in einer öffentlichen Krise. Mit Vorständen und Geschäftsleitungen arbeitet Michael persönlich. Das gilt auch, wenn eine Lage öffentlich wird und es um Krisenkommunikation geht. Für Rhetoriktraining auf weiteren Ebenen in Unternehmen hat er zwei Trainer selbst ausgebildet und lizenziert. Namen von Mandanten nennt er nicht.</p>
  <div class="cta-row rv" style="margin-top:28px">{btn('werdegang')}</div>
 </div>
</section>'''


def s04():
    trio = [('Persönlichkeit.', 'Du lernst keine fremde Rolle. Michael bringt dir nicht bei zu schauspielern. Er arbeitet mit dem, was du schon mitbringst.'),
            ('Kongruenz.', 'Was du sagst, und wie du es sagst, passt zusammen. Das macht dich glaubwürdig.'),
            ('Wirkung.', 'Michael schaut genau hin, wie eine Aussage im Raum ankommt. Und was von ihr bleibt, wenn jemand widerspricht. Seine Rückmeldung ist direkt.')]
    li = ''.join(f'<div class="rv"><h3>{h}</h3><p>{e(p)}</p></div>' for h, p in trio)
    return f'''
<section class="sec sec--cream" id="methode">
 <div class="wrap">
  <h2 class="motto rv">Wer etwas zu sagen hat, sollte es sagen können.</h2>
  <p class="motto-sub rv">{t('So beschreibt Michael Ehlers seine Arbeit [von Kunde bestätigen: Wortlaut Motto]. Er sieht Wirkung als Handwerk. Und er traut sie auch Menschen zu, die sich selbst schon abgeschrieben haben.')}</p>
  <div class="trio">
   <div class="portrait rv"><img data-plx src="assets/michael-white.webp" alt="Michael Ehlers im weißen Hemd" width="988" height="1312"></div>
   <div class="trio-list"><p class="trio-h rv">Persönlichkeit. Kongruenz. Wirkung.</p>{li}<div class="cta-row rv">{btn('methode')}</div></div>
  </div>
 </div>
</section>'''


def s05():
    titles = ['Nie wieder sprachlos!', 'Rhetorik. Die Kunst der Rede im digitalen Zeitalter', 'Die 5 Säulen der positiven Kommunikation', 'Sales Code 55',
              'Social Audio. Willkommen am digitalen Lagerfeuer', 'Herzlich willkommen im Datengefängnis', 'Kommunikationsrevolution Social Media',
              'Rhetorik: Sales-up-Call, mit Stephan Heinrich', 'Der Fisch stinkt vom Kopf, als Hein Hansen']
    b = ''.join(f'<div class="book rv">{e(x)}</div>' for x in titles)
    return f'''
<section class="sec" id="buecher">
 <div class="wrap">
  <div class="stack"><h2 class="rv">Neun Bücher, ein Podcast, ein Thema</h2>
   <p class="lead rv">Michael Ehlers hat neun Bücher als Autor oder Herausgeber veröffentlicht. Sie reichen von Rhetorik und Führung bis zur Kommunikation in digitalen Räumen.</p></div>
  <div class="books">{b}</div>
  <div class="pod rv">{ICON_MIC}<p>Seit 2008 spricht er in seinem Podcast „Unübersehbar“ darüber, was Menschen überzeugend macht. Alle zwei Wochen erscheint eine neue Folge. Auf LinkedIn folgen ihm mehr als 18.000 Menschen, sein Rhetorik-Newsletter hat mehr als 7.500 Abonnenten.</p></div>
 </div>
</section>'''


def s06():
    return f'''
<section class="sec sec--navy" id="lehre">
 <div class="wrap">
  <h2 class="rv" style="color:#fff">Lehre in St. Gallen, Analysen im Fernsehen</h2>
  <div class="two">
   <div class="rv"><h3>Universität St. Gallen.</h3><p>Michael Ehlers ist Lehrbeauftragter an der Universität St. Gallen. Dort arbeitet er mit Studierenden an Rhetorik und Kommunikation. Daneben ist er Expert Lead am SGMI Center for Rhetoric. Diese Rolle gehört zum SGMI Management Institut St. Gallen und ist vom Lehrauftrag an der Universität getrennt.</p></div>
   <div class="rv"><h3>Im Fernsehen.</h3><p>Als Rhetorik-Analyst fragen ihn ARTE und WELT TV an. Einordnungen von ihm erschienen auch bei ARD, ZDF, RTL, n-tv, RP Online und FOCUS online. Bei FOCUS online schreibt er auch als Autor.</p></div>
  </div>
  <div class="erf rv"><img src="assets/erfolg-top100.webp" alt="Titelseite ERFOLG Magazin, Top 100 Erfolgstrainer"><p>Laut ERFOLG Magazin zählte Michael Ehlers zu den Top 100 Trainern im deutschsprachigen Raum.</p></div>
  <div class="cta-row rv" style="margin-top:36px">{btn('medien', 'btn btn--light')}</div>
 </div>
</section>'''


def s07():
    Q = [('Fordern, um zu fördern', '„Keiner versteht es besser seine Teilnehmer durch fordern zu fördern.“', 'Christian S., Rhetorik I auf Mallorca', 'ProvenExpert'),
         ('Feedback, das trägt', '„Die Redeübungen haben mich definitiv auf ein anderes Level gebracht und Michaels Feedback war unheimlich wertschätzend, klar und unglaublich hilfreich.“', 'Jenny E.', 'Google'),
         ('Auch nach 40 Jahren Medienerfahrung', '„Trotz 40 Jahren Medienerfahrung konnte ich erstaunlich viel vom Rhetoriktraining profitieren.“', 'Peter Escher', 'Moderator MDR'),
         ('Mit Humor', '„Ein begeisterndes Training mit einer anregenden und humorvollen Atmosphäre. Rundum gelungen.“', 'Sarna Röser', 'Bundesvorsitzende „Die Jungen Unternehmer“')]
    c = ''.join(f'<article class="q rv"><h3>{h}</h3>{STARS}<blockquote>{e(q)}</blockquote><p class="who"><span>{e(n)}, <span class="src">{e(s)}</span></span></p></article>' for h, q, n, s in Q)
    return f'''
<section class="sec" id="stimmen">
 <div class="wrap">
  <h2 class="rv">Wie Teilnehmer Michael als Trainer erleben</h2>
  <div class="qgrid q4">{c}</div>
  <p class="vcap rv" style="margin-top:28px">250 Bewertungen auf ProvenExpert, 227 davon mit 5 Sternen.</p>
 </div>
</section>'''


def s08():
    return f'''
<section class="sec sec--cream" id="seminare">
 <div class="wrap feat">
  <div class="grp rv"><img data-plx src="assets/seminar-group.webp" alt="Seminargruppe mit Zertifikaten unter Palmen, Michael Ehlers vorne links" width="1350" height="1800"></div>
  <div class="stack">
   <h2 class="rv">Seminare mit Michael</h2>
   <p class="lead rv">{t('In den Seminaren von me&you trainierst du drei Tage in einer kleinen Gruppe von höchstens 14 Menschen. Dazu kommt ein Tag Get Together. Du hältst Reden und siehst dich dreimal auf Video. Rückmeldung bekommst du sofort. Im VR-Training sprichst du vor einem virtuellen Publikum. Die Seminare finden auf Mallorca, in Barcelona, Zypern und Dubai statt, den Einstieg gibt es auch in Frankfurt und Berlin [von Kunde bestätigen: Leitet Michael die Seminare selbst].')}</p>
   <p class="lead rv">Du beginnst mit dem Einstieg „Frei sprechen“. Danach wählst du frei: ruhig bleiben, wenn es eng wird, oder mit Sprache führen. Der nächste Termin: Mallorca, 3. bis 6. Dezember 2026. Alle Formate und Termine findest du auf der Seite <a class="tlink" href="{V2}seminare.html">Seminare</a>.</p>
   <div class="cta-row rv">{btn('seminare')}</div>
  </div>
 </div>
</section>'''


def s09():
    steps = [('Termin wählen.', 'Online, zu einer Zeit, die dir passt. Bestätigung per E-Mail, Erinnerung per WhatsApp.'),
             ('30 Minuten per Video.', 'Mit Michaels Team [von Kunde bestätigen: Name und Rolle der Person im Gespräch] sprichst du über deine Situation und deine Ziele.'),
             ('Danach entscheiden.', 'Du weißt, welches Seminar passt, und entscheidest in Ruhe.')]
    c = ''.join(f'<div class="fstep"><span class="n">{i}</span><div class="fstep__t"><h3>{h}</h3><p>{t(p)}</p></div></div>' for i, (h, p) in enumerate(steps, 1))
    return f'''
<section class="sec" id="gespraech">
 <div class="wrap">
  <h2 class="center rv">Der erste Schritt ist ein Gespräch</h2>
  <div class="flow rv" data-in><div class="flow__line"><i></i></div>{c}</div>
  <div class="center"><div class="cta-row rv" style="margin-top:56px">{btn('gespraech')}<p class="assure">{CHECK}Kostenlos. Lieber anrufen: <a href="{TEL}">+49 15888367664</a></p></div></div>
 </div>
</section>'''


FAQ = [
 ('Wer ist Michael Ehlers?', 'Michael Ehlers ist Rhetoriktrainer, Executive Coach und Autor. Er arbeitet seit 1990 mit Menschen an Rede, Auftritt und Wirkung. An der Universität St. Gallen hat er einen Lehrauftrag für Rhetorik und Kommunikation.'),
 ('Welche Bücher hat er geschrieben?', 'Neun Bücher als Autor oder Herausgeber. Darunter sind „Nie wieder sprachlos!“ und „Rhetorik. Die Kunst der Rede im digitalen Zeitalter“. Als „Hein Hansen“ schrieb er 2014 „Der Fisch stinkt vom Kopf“.'),
 ('Wo kann ich ihn hören?', 'In seinem Podcast „Unübersehbar“, alle zwei Wochen mit einer neuen Folge. Als Rhetorik-Analyst fragen ihn außerdem ARTE und WELT TV an.'),
 ('Mit wem arbeitet er?', 'Mit Vorständen, Unternehmerinnen und Unternehmern, Profisportlern und Menschen, die in der Öffentlichkeit stehen. In den Seminaren trainieren Anfänger und erfahrene Redner zusammen. Namen von Mandanten nennt er nicht.'),
 ('Wo sitzt sein Institut?', 'Das Institut Michael Ehlers GmbH sitzt in Hallstadt bei Bamberg. Die Seminare finden an wechselnden Orten statt.'),
 ('Was ist das SGMI Center for Rhetoric?', 'Ein Bereich des SGMI Management Institut St. Gallen. Michael Ehlers ist dort Expert Lead. Diese Rolle ist von seinem Lehrauftrag an der Universität St. Gallen getrennt.'),
 ('Arbeitet Michael auch mit Unternehmen?', 'Ja. Coachings für Vorstände und Geschäftsleitungen führt er persönlich. Für Trainings auf weiteren Ebenen arbeiten zwei von ihm ausgebildete und lizenzierte Trainer.'),
 ('Was kostet ein Seminar bei Michael Ehlers?', 'Den Preis für dein Seminar nennt dir Michaels Team im kostenlosen Gespräch.'),
]


def s10():
    items = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div class="a">{t(a)}</div></details>' for i, (q, a) in enumerate(FAQ))
    return f'''
<section class="sec sec--cream" id="faq">
 <div class="wrap faqgrid">
  <div class="stack" style="position:sticky;top:120px"><p class="ov rv">FAQ</p><h2 class="rv">Häufige Fragen zu Michael Ehlers</h2>
   <p class="morelinks rv">Weitere Antworten findest du in den <a class="tlink" href="{V2}faq.html">häufigen Fragen</a>.</p></div>
  <div class="acc rv">{items}</div>
 </div>
</section>'''


def s11():
    li = ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in ['per Video, von überall', 'Termin online wählen', 'Seminare an sechs Orten'])
    foot = home.section_closer().split('<footer', 1)[1]
    foot = '<footer' + foot.replace(home.BOOK, BOOK).replace(f'href="{V2}michael.html">Über Michael', 'href="#top">Über Michael').replace('href="#termine"', f'href="{V2}seminare.html#termine"')
    return f'''
<section class="closer" id="abschluss">
 <div class="closer__bg"><img data-plx src="assets/closer-terrace.webp" alt="Abendstimmung auf einer Steinterrasse über dem Meer, Menschen im Gespräch" width="1536" height="1024"></div>
 <div class="wrap"><div class="closer__in">
  <h2 class="rv">Dreißig Jahre Erfahrung,<br>ein Gespräch entfernt.</h2>
  <p class="rv">Der erste Schritt ist ein Gespräch von 30 Minuten. Kostenlos und per Video. Danach weißt du, welches Seminar zu dir passt.</p>
  <ul class="rv">{li}</ul>
  <p class="proofline rv">{STARS} 227 von 250 Bewertungen mit 5 Sternen auf ProvenExpert</p>
  <div class="cta-row rv">{btn('abschluss', 'btn btn--light cta--breathe')}<p class="tel">Lieber anrufen: <a href="{TEL}">+49 15888367664</a></p></div>
  <p class="back rv">Zurück zur <a href="{V2}index.html">Startseite</a></p>
 </div></div>
</section>
{foot}'''


def schema():
    ORG = 'https://www.meandyou.de/#organization'
    g = [{"@type": "ProfilePage", "@id": "https://www.meandyou.de/michael#webpage", "url": "https://www.meandyou.de/michael", "name": "Michael Ehlers | Rhetoriktrainer seit 1990 und Autor", "inLanguage": "de", "mainEntity": {"@id": "https://www.meandyou.de/michael#person"}},
         {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://www.meandyou.de/"}, {"@type": "ListItem", "position": 2, "name": "Michael", "item": "https://www.meandyou.de/michael"}]},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Institut Michael Ehlers GmbH", "alternateName": "me&you Communication", "url": "https://www.meandyou.de/",
          "address": {"@type": "PostalAddress", "streetAddress": "Landsknechtstraße 50", "postalCode": "96103", "addressLocality": "Hallstadt", "addressCountry": "DE"}},
         {"@type": "Person", "@id": "https://www.meandyou.de/michael#person", "name": "Michael Ehlers", "jobTitle": "Rhetoriktrainer und Executive Coach", "worksFor": {"@id": ORG},
          "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": "Lehrbeauftragter für Rhetorik und Kommunikation, Universität St. Gallen"}],
          "affiliation": [{"@type": "CollegeOrUniversity", "name": "Universität St. Gallen"}, {"@type": "Organization", "name": "SGMI Management Institut St. Gallen"}],
          "knowsAbout": ["Rhetorik", "Kommunikation", "Krisenkommunikation", "Führung"],
          "sameAs": ["https://institut-ehlers.de/michael-ehlers", "https://de.linkedin.com/in/rhetoriktrainer", "https://www.focus.de/autoren/michael-ehlers_e598339a-a33c-4231-8f5e-8c9e4a424fc9.html", "https://open.spotify.com/show/06KoTy9DZC61mNvf4X2L2E"]}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


def page():
    body = header() + '<main>' + s01() + s02() + s03() + s04() + s05() + s06() + s07() + s08() + s09() + s10() + '</main>' + s11() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Michael Ehlers | Rhetoriktrainer seit 1990 und Autor</title>
<meta name="description" content="Michael Ehlers trainiert seit 1990 Menschen in Rhetorik. Autor von neun Büchern, Lehrauftrag an der Universität St. Gallen. Jetzt Gespräch buchen.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema()}</script>
</head><body>{body}<script>{home.JS}</script></body></html>'''


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
