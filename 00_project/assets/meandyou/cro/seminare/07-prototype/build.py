"""Build the CRO prototype of the me&you seminar page (desktop 1440 px). Text = 04-copy/approved-copy.md.
Design system = homepage prototype (../../07-prototype/build.py): CSS, JS and icons are imported from there.
Run: python3 build.py  ->  index.html"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '07-prototype'))
import build as home  # noqa: E402

V2 = 'https://clients.741.studio/meandyou/v2/'
BOOK = V2 + 'termin.html?utm_source=seminare&utm_content='
TEL = 'tel:+4915888367664'
e, STARS, CHECK, PLAY = home.e, home.STARS, home.CHECK, home.PLAY


def btn(utm, cls='btn'):
    return f'<a class="{cls}" href="{BOOK}{utm}">Gespräch buchen</a>'


def t(s):
    """Escape text and turn [von Kunde bestätigen: …] into a yellow badge."""
    s = e(s)
    return re.sub(r'\[von Kunde bestätigen: ([^\]]+)\]', lambda m: f'<span class="fehlt" title="[FEHLT]">[von Kunde bestätigen: {m.group(1)}]</span>', s)


CSS = home.CSS + r"""
/* seminar page additions */
.hero--split .hero__img{width:50%}
.hero--split .hero__img img{object-position:50% 18%}
.hero--split .hero__img::after{background:linear-gradient(90deg,var(--paper) 0%,rgba(250,248,244,.7) 14%,rgba(250,248,244,0) 40%)}
.hero--split .hero__txt{max-width:740px}
.hero--split .proofline{white-space:nowrap}
.hero--split .body{max-width:30em}
.hero--split .hero__txt .body{max-width:34em}
.voices{display:grid;grid-template-columns:1.45fr .8fr;gap:40px;margin-top:48px;align-items:start}
.voices .qgrid{margin-top:0}
.voices .vids{grid-template-columns:repeat(3,1fr);margin-top:14px;gap:12px}
.voices .vcap{margin-top:0;text-align:left}
.factgrid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.factgrid .badge:first-child{grid-column:1/-1}
.factgrid .badge{padding:18px 22px}
.factgrid .badge b{font-size:21px}
.feat{display:grid;grid-template-columns:.92fr 1.08fr;gap:64px;align-items:start}
.feat__img{border-radius:var(--r);overflow:hidden;height:760px;position:sticky;top:110px}
.feat__img img{width:100%;height:112%;object-fit:cover;object-position:36% 50%}
.feat h2{font-size:44px}
.topics{list-style:none;margin:6px 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:14px 28px}
.topics li{display:flex;gap:10px;font-size:17px;line-height:1.45;color:var(--muted)}
.topics li::before{content:"";flex:none;width:8px;height:8px;border-radius:50%;background:var(--dove);margin-top:9px}
.topics b{color:var(--ink);font-weight:600}
.info{background:var(--cream);border-radius:18px;padding:20px 24px;display:flex;flex-direction:column;gap:8px;font-size:16.5px;color:var(--muted)}
.info b{color:var(--ink);font-weight:600}
.info .seats{font:400 22px/1.2 var(--serif);color:var(--cta)}
.dl{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:4px}
.dl li{display:flex;gap:10px}.dl li span:first-child{min-width:92px;font-weight:600;color:var(--ink)}
.fmts{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}
.fmts .fmt__img{height:240px}
.fmts .fmt__txt{gap:14px}
.fmts h3{font-size:25px}
.fmts .info{margin-top:auto;background:var(--cream)}
.fmts .btn{align-self:flex-start}
.cmp{width:100%;border-collapse:collapse;margin-top:40px;background:#fff;border-radius:var(--r);overflow:hidden;font-size:17px}
.cmp th{font:600 14px/1.2 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--cta);text-align:left;padding:20px 22px;background:var(--paper)}
.cmp td{padding:20px 22px;border-top:1px solid var(--line);vertical-align:top;color:var(--muted)}
.cmp td:first-child{font:400 19px/1.35 var(--serif);color:var(--ink)}
.cmp td.n{font:400 22px/1.2 var(--serif);color:var(--cta)}
.cmp-note{margin-top:22px;font-size:17px;color:var(--muted)}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:-56px;position:relative;z-index:3}
.col{background:var(--paper);border-radius:18px;padding:30px 30px 32px;box-shadow:0 10px 30px rgba(42,38,34,.08);display:flex;flex-direction:column;gap:12px}
.col svg{width:34px;height:34px;color:var(--cta)}
.col h3{font-size:23px}.col p{font-size:17px;color:var(--muted)}
.incl{margin-top:44px;display:grid;grid-template-columns:auto 1fr;gap:20px;background:var(--cream);border-radius:var(--r);padding:30px 36px;align-items:start}
.incl svg{width:28px;height:28px;color:var(--cta);margin-top:3px}
.incl p{font-size:17px;color:var(--muted)}
.gt{margin-top:28px;font:italic 400 21px/1.4 var(--serif);color:var(--ink)}
.q4{grid-template-columns:repeat(2,1fr)}
.q .meta{font-size:15.5px;color:var(--muted)}
.who2{display:grid;grid-template-columns:.75fr 1.25fr;gap:72px;align-items:center}
.who2 .portrait{height:640px}
.who2 p{font-size:18px;color:var(--muted)}
.erfolg{display:flex;align-items:center;gap:16px;margin-top:8px;font-size:16px;color:var(--muted)}
.erfolg img{height:96px;width:auto;border-radius:6px;box-shadow:0 4px 14px rgba(42,38,34,.15)}
#faq h2{font-size:34px}
#ablauf .band__bg img{object-position:50% 8%;margin-top:0}
.back{color:rgba(255,255,255,.8);font-size:16px}.back a{color:#fff}
"""

ICON_SPEAK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="7" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M17 8c1 .8 1.6 2 1.6 3.3S18 13.8 17 14.6M19.5 5.5c1.6 1.4 2.5 3.4 2.5 5.8s-.9 4.4-2.5 5.8"/></svg>'
ICON_CAM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="6" width="13" height="12" rx="2.5"/><path d="M15.5 10.5l6-3.5v10l-6-3.5z"/></svg>'
ICON_VR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8.5A2.5 2.5 0 0 1 5.5 6h13A2.5 2.5 0 0 1 21 8.5v6a2.5 2.5 0 0 1-2.5 2.5h-3.2l-1.8-2.4a1.9 1.9 0 0 0-3 0L8.7 17H5.5A2.5 2.5 0 0 1 3 14.5z"/><circle cx="8" cy="11.5" r="1.4"/><circle cx="16" cy="11.5" r="1.4"/></svg>'

R1 = [('Mallorca', '3. bis 6. Dezember 2026'), ('Mallorca', '4. bis 7. März 2027'), ('Mallorca', '29. April bis 2. Mai 2027'),
      ('Frankfurt', '17. bis 20. Juni 2027'), ('Berlin', '12. bis 15. August 2027'), ('Mallorca', '14. bis 17. Oktober 2027')]


def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="{V2}index.html"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="#top" aria-current="page" style="color:var(--cta)">Seminare</a><a href="{V2}michael.html">Michael</a><a href="{V2}rhetorik.html">Was ist Rhetorik</a><a href="#stimmen">Stimmen</a><a href="#faq">FAQ</a></nav>
 {btn('header')}
</div></header>'''


def s01():
    return f'''
<section class="hero hero--split" id="top">
 <div class="hero__img"><img data-plx src="assets/michael-jacket.webp" alt="Michael Ehlers, Rhetoriktrainer, im braunen Sakko in einem hellen Raum" width="1122" height="1600"></div>
 <div class="wrap hero__in"><div class="hero__txt">
  <p class="proofline rv">{STARS} 227 von 250 Bewertungen mit 5 Sternen auf ProvenExpert · über 8.000 Teilnehmer</p>
  <h1 class="rv"><span class="kicker">Rhetorik-Seminare mit Michael Ehlers:</span><span class="big">Ein Einstieg.<br>Dann dein eigener Weg.</span></h1>
  <p class="body rv">Drei Seminare zur Wahl, dazu ein kompaktes Bundle. Im Einstieg lernst du, frei und klar zu sprechen. Danach wählst du selbst, ob du an deiner Schlagfertigkeit arbeitest oder daran, mit Sprache zu führen. Die drei Seminare dauern je drei Tage plus einen Tag Get Together, in einer Gruppe von höchstens 14 Menschen.</p>
  <div class="cta-row rv">
   <div class="btns">{btn('hero', 'btn cta--breathe')}<a class="btn btn--ghost" href="#termine">Termine ansehen</a></div>
   <p class="assure">{CHECK}30 Minuten, kostenlos, per Video. Du klärst, welches Seminar zu dir passt.</p>
  </div>
 </div></div>
</section>'''


def s02():
    logos = ''.join(f'<img src="assets/logo-{n}.webp" alt="{a}">' for n, a in [('zdf', 'ZDF'), ('ard', 'ARD'), ('rtl', 'RTL'), ('stern', 'stern'), ('mdr', 'MDR'), ('hr2', 'hr2')])
    facts = [('Bewertungen:', '227 von 250 auf ProvenExpert mit 5 Sternen'), ('Dauer:', 'drei Trainingstage, dazu ein Tag Get Together'),
             ('Kamera:', 'drei Videoanalysen, Auswertung direkt danach'), ('VR:', 'Reden vor einem virtuellen Saal'), ('Gruppe:', 'je nach Seminar 10, 12 oder 14 Plätze')]
    b = ''
    for k, v in facts:
        st = STARS if k == 'Bewertungen:' else ''
        b += f'<div class="badge">{st}<b>{k}</b><span>{v}</span></div>'
    return f'''
<section class="proof" id="kurz">
 <div class="wrap">
  <div class="proof__grid">
   <div class="proof__ans rv"><h2>Welches Rhetorik-Seminar passt zu dir?</h2>
    <p>Wenn du noch kein Seminar bei Michael Ehlers besucht hast, beginnst du mit dem Einstieg zu freier Rede und Struktur. Danach wählst du frei: Schlagfertigkeit im Meeting oder Führung mit Sprache. Welches Seminar zu dir passt, klärst du im kostenlosen Gespräch.</p></div>
   <div class="rv" data-in>
    <div class="factgrid">{b}</div>
    <p class="pquote">„Ich fand es spannend, dass wir Teilnehmer ein Mix von Anfänger bis Profi waren und Michael uns alle, egal auf welchem Level, weiterbringen konnte.“<small>Christin R., ProvenExpert</small></p>
   </div>
  </div>
  <div class="media rv"><span>Bekannt aus ZDF, ARD, RTL, stern, MDR und hr2</span>{logos}</div>
 </div>
</section>'''


def s03():
    topics = [('Sicher auftreten:', 'vor Menschen reden, auch mit Lampenfieber'), ('Rede halten:', 'in zwei Minuten ein starkes Statement setzen'),
              ('Struktur lernen:', 'mit einer klaren Formel jede Rede aufbauen'), ('Echt wirken:', 'deinen eigenen Redestil finden'),
              ('Sprache nutzen:', 'auch Kritik charmant und souverän ausdrücken'), ('Körper lesen:', 'Gestik gezielt einsetzen statt unbewusst zappeln'),
              ('Fragen stellen:', 'mit den richtigen Fragen Gespräche lenken')]
    li = ''.join(f'<li><span><b>{k}</b> {v}</span></li>' for k, v in topics)
    dl = ''.join(f'<li><span>{o},</span><span>{d}</span></li>' for o, d in R1)
    return f'''
<section class="sec" id="frei-sprechen">
 <div class="wrap feat">
  <div class="feat__img rv"><img data-plx src="assets/einstieg-group.webp" alt="Kleine Gruppe im hellen Seminarraum, eine Teilnehmerin spricht im Stehen" width="1536" height="1024"></div>
  <div class="stack">
   <p class="ov rv">Der Einstieg</p>
   <h2 class="rv">Frei sprechen, auch mit Lampenfieber</h2>
   <p class="lead rv">{t('Arbeitstitel Rhetorik I [von Kunde bestätigen: Seminarname]. Dieses Seminar ist für dich, wenn du vor Menschen sprechen musst und dich dabei unsicher fühlst. Oder wenn du gut vorbereitet bist und trotzdem nicht so wirkst, wie du willst. Du arbeitest an sieben Themen:')}</p>
   <ul class="topics rv">{li}</ul>
   <p class="lead rv">Du sprichst an allen drei Tagen selbst und bekommst Feedback von Michael und der Gruppe. Dazu arbeitest du mit Worksheets und Übungen.</p>
   <div class="info rv"><p><span class="seats">14 Plätze.</span> Orte und Termine:</p><ul class="dl">{dl}</ul></div>
   <div class="cta-row rv">{btn('einstieg')}</div>
  </div>
 </div>
</section>'''


def s04():
    cards = [
     ('ruhig-bleiben', 'fmt-ruhig.webp', 'Zwei Kolleginnen und Kollegen in einem ruhigen, ernsten Gespräch am Besprechungstisch', 'Ruhig bleiben, wenn es eng wird',
      'Arbeitstitel Rhetorik II [von Kunde bestätigen: Seminarname]. Für dich, wenn du im Meeting öfter angegriffen als gehört wirst. Du trainierst Schlagfertigkeit, damit du auf Angriffe schnell und präzise reagierst. Mit Überzeugungspsychologie erkennst du Motive und platzierst deine Argumente gezielt. Du lernst, unfaire Methoden zu durchschauen und ruhig zu kontern. Dazu kommen Körpersprache und Meetings, in denen du Diskussionen leitest und Ergebnisse klar sicherst. Du arbeitest mit Strategien und Workbooks.',
      '10 Plätze.', [('Barcelona,', '15. bis 18. April 2027'), ('Barcelona,', '21. bis 24. Oktober 2027')], 'format-ruhig'),
     ('mit-sprache-fuehren', 'fmt-fuehren.webp', 'Eine Teamleiterin spricht zu einer kleinen Gruppe in einem hellen Raum', 'Mit Sprache führen',
      'Arbeitstitel Rhetorik III [von Kunde bestätigen: Seminarname]. Für dich, wenn du ein Team führst oder Gruppen überzeugen musst. Du formulierst Kritik klar und motivierend. Du übst Zuhören, damit du Kunden und Partner wirklich verstehst. Du hältst Stegreifreden vor der Gruppe und lernst Methoden großer Redner für den Alltag. Mit DeepOcean siehst du, wie deine Persönlichkeit deine Rhetorik prägt. Du arbeitest mit Strategien und Workbooks.',
      '12 Plätze.', [('Dubai,', '10. bis 13. Dezember 2026'), ('Zypern,', '7. bis 10. Oktober 2027')], 'format-fuehren'),
     ('bundle', 'bundle-pitch.webp', 'Eine Frau übt einen kurzen Pitch vor zwei Zuhörern', 'Rhetorik Bundle',
      'Inhalte aus Rhetorik I und Rhetorik II in einem Seminar von zwei Tagen [von Kunde bestätigen: Seminarname]. Für Führungskräfte, Unternehmerinnen und Unternehmer sowie für Menschen aus Vertrieb, Marketing und Kommunikation. Du arbeitest an Körpersprache und Wirkung. Dazu kommen Storytelling, Elevator Pitches und Schlagfertigkeit. Im Auftrittscoaching mit Videoanalyse siehst du dich so, wie andere dich sehen.',
      '', [], 'format-bundle'),
    ]
    c = ''
    for aid, img, alt, h, body, seats, ds, utm in cards:
        if ds:
            info = f'<div class="info"><p><span class="seats">{seats}</span></p><ul class="dl">' + ''.join(f'<li><span>{o}</span><span>{d}</span></li>' for o, d in ds) + '</ul></div>'
        else:
            info = f'<div class="info"><p>{t("Termine und Ort: [von Kunde bestätigen: Termine und Ort Bundle]")}</p></div>'
        c += f'''<article class="fmt rv" id="{aid}" style="scroll-margin-top:96px"><div class="fmt__img"><img src="assets/{img}" alt="{alt}"></div><div class="fmt__txt"><h3>{h}</h3><p>{t(body)}</p>{info}{btn(utm)}</div></article>'''
    return f'''
<section class="sec" id="formate" style="padding-top:40px">
 <div class="wrap">
  <div class="stack center"><p class="ov rv">Die Formate</p><h2 class="rv">Rhetorik ist kein Stufenmodell. Menschen sind es auch nicht.</h2>
   <p class="lead rv" style="margin:0 auto">Nach dem Einstieg wählst du frei, in beliebiger Reihenfolge. Die Formate bauen nicht aufeinander auf. Du nimmst das Thema, das in deinem Alltag gerade zählt.</p></div>
  <div class="fmts">{c}</div>
 </div>
</section>'''


def s05():
    rows = [('Frei sprechen (Einstieg)', 'Auftreten, Rede, Struktur', 'Du musst präsentieren und fühlst dich unsicher', '14', 'Mallorca, Frankfurt, Berlin'),
            ('Ruhig bleiben', 'Schlagfertigkeit, Argumentation', 'Du wirst im Meeting unterbrochen oder angegriffen', '10', 'Barcelona'),
            ('Mit Sprache führen', 'Führung, Zuhören, Stegreifrede', 'Du führst ein Team und willst Gruppen gewinnen', '12', 'Dubai, Zypern'),
            ('Rhetorik Bundle', 'Wirkung, Pitch, Auftritt', 'Du willst Inhalte aus Rhetorik I und II kompakt in zwei Tagen', '[von Kunde bestätigen: Plätze]', '[von Kunde bestätigen: Termine und Ort Bundle]')]
    tr = ''.join('<tr>' + ''.join(f'<td{" class=n" if i == 3 and r[3].isdigit() else ""}>{t(x)}</td>' for i, x in enumerate(r)) + '</tr>' for r in rows)
    return f'''
<section class="sec sec--cream" id="vergleich">
 <div class="wrap">
  <h2 class="rv">Welches Seminar passt zu welcher Situation?</h2>
  <table class="cmp rv"><thead><tr><th>Seminar</th><th>Schwerpunkt</th><th>Typische Situation</th><th>Plätze</th><th>Orte</th></tr></thead><tbody>{tr}</tbody></table>
  <p class="cmp-note rv">Wenn du dir nicht sicher bist, ist das kostenlose Gespräch dafür da.</p>
 </div>
</section>'''


def s06():
    cols = [(ICON_SPEAK, 'Du sprichst selbst.', 'Du hältst Reden vor der Gruppe und bekommst Rückmeldung von Michael und von den anderen Teilnehmern.'),
            (ICON_CAM, 'Du siehst dich selbst.', 'Dreimal wirst du auf Video aufgenommen. Die Auswertung kommt sofort. So siehst du, wie du auf andere wirkst.'),
            (ICON_VR, 'Du übst vor virtuellem Publikum.', 'Im VR-Training sprichst du vor einem großen virtuellen Publikum. Michael B. nennt das auf ProvenExpert „unglaublich real“.')]
    c = ''.join(f'<div class="col rv">{i}<h3>{h}</h3><p>{e(p)}</p></div>' for i, h, p in cols)
    incl = ('Enthalten sind die drei Trainingstage und der Tag Get Together. Dazu kommen die Übernachtungen im offiziellen Seminarzeitraum, bei vier Seminartagen sind das drei Nächte [von Kunde bestätigen: Übernachtung]. '
            'Zusätzliche Nächte zahlst du selbst. Während des Programms gibt es Snacks, Getränke und ein leichtes Frühstück. Hotelfrühstück und Abendessen sind nicht enthalten [von Kunde bestätigen: Verpflegung]. Anreise und Transfer organisierst du selbst.')
    return f'''
<section class="band" id="ablauf">
 <div class="band__bg"><img data-plx src="assets/vr-band.webp" alt="Ein Teilnehmer spricht mit VR-Brille in einem hellen Raum, zwei andere hören zu" width="1536" height="1024"></div>
 <div class="wrap band__in"><div>
  <h2 class="rv">Drei Tage, kleine Gruppe, keine Zuschauer.</h2>
  <p class="rv">Kleine Gruppe, damit jeder drankommt. Kein Zuschauen, kein Verstecken in der letzten Reihe.</p>
 </div></div>
</section>
<section class="sec" style="padding-top:0">
 <div class="wrap">
  <div class="cols3">{c}</div>
  <p class="gt rv">Ein weiterer Tag gehört dem Get Together.</p>
  <div class="incl rv">{CHECK}<p>{t(incl)}</p></div>
  <div class="cta-row rv" style="margin-top:34px">{btn('ablauf')}</div>
 </div>
</section>'''


def s07():
    Q = [('Vor einem virtuellen Saal', '„Mein persönliches Highlight war das VR-Training, bei dem wir vor einem großen KI-gesteuerten Publikum sprechen durften […]“', 'Michael B.', 'Rhetorik I auf Mallorca'),
         ('Steile Lernkurve', '„Steile Lernkurve mit Soforteffekt. Eines der besten Seminare die ich besucht habe.“', 'Justus S.', 'Rhetorik I auf Mallorca'),
         ('Raus aus der Komfortzone', '„Dieses Training hat beruflich wie privat einiges in Bewegung gebracht. Ein intensiver Stretch der Komfortzone in wunderschönem Ambiente, mit effektiven Techniken, zielgerichtetem Training und einer großen Portion Humor.“', 'V.', 'Rhetorik II in Barcelona'),
         ('Lernen mit Abstand zum Alltag', '„Aufgrund der tollen Atmosphäre und einzigartigen Lage lernt es sich sehr entspannt.“', 'Christian S.', 'Rhetorik I auf Mallorca')]
    c = ''.join(f'<article class="q rv"><h3>{h}</h3>{STARS}<blockquote>{e(q)}</blockquote><p class="who"><span>{n}, {s}, <span class="src">ProvenExpert</span></span></p></article>' for h, q, n, s in Q)
    vids = ''.join(f'<div class="vid rv"><img src="assets/v-stimme-{i}.webp" alt="Video-Stimme eines Teilnehmers"><b>{PLAY}</b><span>{d}</span></div>' for i, d in [(1, '1:00'), (2, '1:12'), (3, '1:23')])
    return f'''
<section class="sec sec--cream" id="stimmen">
 <div class="wrap">
  <div class="stack"><h2 class="rv">Was Teilnehmer aus den Seminaren mitnehmen</h2>
   <p class="lead rv">250 Bewertungen auf ProvenExpert, 227 davon mit 5 Sternen. Vier Auszüge, jeweils mit Seminar und Ort. Auslassungen sind mit […] markiert.</p></div>
  <div class="voices"><div class="qgrid q4">{c}</div>
   <div class="stack" style="gap:0"><p class="vcap rv">Dazu drei kurze Videos, in denen Teilnehmer von ihren Seminartagen berichten.</p><div class="vids">{vids}</div></div></div>
 </div>
</section>'''


def s08():
    P = [('city-mallorca.webp', 'Mallorca', 'Frei sprechen', ['3. bis 6. Dezember 2026', '4. bis 7. März 2027', '29. April bis 2. Mai 2027', '14. bis 17. Oktober 2027']),
         ('city-dubai.webp', 'Dubai', 'Mit Sprache führen', ['10. bis 13. Dezember 2026']),
         ('city-barcelona.webp', 'Barcelona', 'Ruhig bleiben', ['15. bis 18. April 2027', '21. bis 24. Oktober 2027']),
         ('city-frankfurt.webp', 'Frankfurt', 'Frei sprechen', ['17. bis 20. Juni 2027']),
         ('city-berlin.webp', 'Berlin', 'Frei sprechen', ['12. bis 15. August 2027']),
         ('city-zypern.webp', 'Zypern', 'Mit Sprache führen', ['7. bis 10. Oktober 2027'])]
    c = ''.join(f'<article class="place rv"><div class="place__img"><img data-plx src="assets/{img}" alt="Seminarort {n}"></div><div class="place__t"><p class="fmtn">{fm}</p><h3>{n}</h3><p class="dates">{"<br>".join(ds)}</p></div></article>' for img, n, fm, ds in P)
    return f'''
<section class="sec sec--navy" id="termine">
 <div class="wrap">
  <div class="stack"><h2 class="rv" style="color:#fff">Der Ort ist Teil der Arbeit.</h2>
   <p class="lead rv" style="color:rgba(242,237,228,.85)">Sechs Orte, an denen du Abstand vom Büro gewinnst. Hier siehst du jeden Termin mit dem passenden Seminar. Jeder Termin umfasst vier Seminartage.</p></div>
  <div class="places">{c}</div>
  <p class="stand rv">Wer nicht fliegen will, macht den Einstieg in Frankfurt oder Berlin. Ob noch Plätze frei sind, erfährst du im Gespräch. Termine mit Stand Oktober 2026.</p>
  <div class="cta-row rv" style="margin-top:30px">{btn('termine', 'btn btn--light')}</div>
 </div>
</section>'''


def s09():
    return f'''
<section class="sec" id="michael">
 <div class="wrap who2">
  <div class="portrait rv"><img data-plx src="assets/michael-olive.webp" alt="Michael Ehlers, Rhetoriktrainer, in olivgrüner Jacke" width="1066" height="1600"></div>
  <div class="stack">
   <h2 class="rv">Für wen das gedacht ist, und wer dich trainiert</h2>
   <p class="rv">Die Seminare sind für Führungskräfte, Gründerinnen und Gründer sowie Beraterinnen und Berater. Sie passen zu Menschen, die fachlich überzeugen und trotzdem nicht gehört werden.</p>
   <p class="rv">Michael Ehlers ist seit über 30 Jahren Rhetoriktrainer und hat in dieser Zeit über 8.000 Menschen trainiert. Laut ERFOLG Magazin zählte er zu den Top 100 Trainern im deutschsprachigen Raum. <a class="tlink" href="{V2}michael.html">Mehr über Michael</a></p>
   <div class="erfolg rv"><img src="assets/erfolg-top100.webp" alt="Titelseite ERFOLG Magazin, Top 100 Erfolgstrainer"></div>
  </div>
 </div>
</section>'''


def s10():
    steps = [('Online buchen.', 'Im Kalender wählst du eine Zeit, die dir passt. Die Bestätigung kommt per E-Mail, die Erinnerung per WhatsApp.'),
             ('Gespräch per Video.', '30 Minuten mit Michaels Team [von Kunde bestätigen: Name und Rolle der Person im Gespräch]. Es geht um deine Ziele und um das Seminar, das dazu passt.'),
             ('Selbst entscheiden.', 'Nach dem Gespräch hast du alle Details zu Seminar und Termin. Die Entscheidung triffst du danach, ohne Druck.')]
    c = ''.join(f'<div class="fstep"><span class="n">{i}</span><div class="fstep__t"><h3>{h}</h3><p>{t(p)}</p></div></div>' for i, (h, p) in enumerate(steps, 1))
    return f'''
<section class="sec sec--cream" id="gespraech">
 <div class="wrap">
  <h2 class="center rv">Der nächste Schritt ist ein Gespräch.</h2>
  <div class="flow rv" data-in><div class="flow__line"><i></i></div>{c}</div>
  <div class="center"><div class="cta-row rv" style="margin-top:56px">{btn('gespraech')}<p class="assure">{CHECK}Das Gespräch kostet nichts. Telefon: <a href="{TEL}">+49 15888367664</a></p></div></div>
 </div>
</section>'''


FAQ = [
 ('Muss ich mit dem Einstieg beginnen?', 'In der Regel ja. Der Einstieg legt die Grundlagen für Auftreten und freie Rede. Danach wählst du die Formate frei. Ob mit viel Erfahrung ein anderer Start passt, zum Beispiel das Rhetorik Bundle, klärst du im Gespräch.'),
 ('In welcher Reihenfolge besuche ich die Formate?', 'In jeder Reihenfolge. Die Formate bauen nicht aufeinander auf. Du wählst das Thema, das gerade zu deinem Alltag passt.'),
 ('Gibt es ein Rhetorik-Seminar für Anfänger?', 'Ja, dafür ist der Einstieg gemacht. Du brauchst keine Erfahrung als Redner. In den Gruppen trainieren Anfänger und Profis zusammen, wie Christin R. in ihrer Bewertung beschreibt.'),
 ('Welches Seminar passt für Führungskräfte?', 'Für Führung mit Sprache passt das Format „Mit Sprache führen“. Der Einstieg legt dafür die Basis mit Auftreten und Struktur. Wenn du wenig Zeit hast, frag im Gespräch nach dem Rhetorik Bundle.'),
 ('Was passiert an den Seminartagen?', 'Du hältst viele kurze Reden und bekommst darauf Rückmeldung. Drei Aufnahmen auf Video zeigen dir deine Wirkung. Im VR-Training stehst du vor einem virtuellen Saal. Die Themen hängen vom gewählten Seminar ab.'),
 ('Was kostet ein Rhetorik-Seminar?', 'Den Preis für dein Seminar nennt dir Michaels Team im kostenlosen Gespräch. Bei den dreitägigen Seminaren sind die Trainingstage, der Tag Get Together und die Übernachtungen im Seminarzeitraum enthalten [von Kunde bestätigen: Übernachtung].'),
 ('Wie groß sind die Gruppen?', 'Im Einstieg 14 Plätze, bei „Ruhig bleiben“ 10 Plätze, bei „Mit Sprache führen“ 12 Plätze. So kommt jeder dran.'),
 ('Sind Übernachtung und Anreise enthalten?', 'Drei Nächte im Seminarzeitraum zahlt Michaels Team [von Kunde bestätigen: Übernachtung]. Zusätzliche Nächte, Anreise und Transfer zum Hotel organisierst du selbst.'),
 ('Kann ich ein gebuchtes Seminar stornieren?', 'Ja, bis 8 Wochen vor dem Start. Dann berechnet Michaels Team laut AGB 30 Prozent des Preises. Bei einer späteren Absage ist der volle Preis fällig.'),
]


def s11():
    items = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div class="a">{t(a)}</div></details>' for i, (q, a) in enumerate(FAQ))
    return f'''
<section class="sec" id="faq">
 <div class="wrap faqgrid">
  <div class="stack" style="position:sticky;top:120px"><p class="ov rv">FAQ</p><h2 class="rv">Häufige Fragen zu den Rhetorik-Seminaren</h2>
   <p class="morelinks rv">Noch mehr Antworten stehen in den <a class="tlink" href="{V2}faq.html">häufigen Fragen</a>. Neu beim Thema? Lies zuerst <a class="tlink" href="{V2}rhetorik.html">Was ist Rhetorik?</a></p></div>
  <div class="acc rv">{items}</div>
 </div>
</section>'''


def s12():
    li = ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in ['per Video, von überall', 'Termin online wählen', 'sechs Orte, darunter Frankfurt und Berlin'])
    foot = home.section_closer().split('<footer', 1)[1]
    foot = '<footer' + foot.replace(home.BOOK, BOOK).replace('href="https://clients.741.studio/meandyou/v2/seminare.html">Seminare', 'href="#top">Seminare')
    return f'''
<section class="closer" id="abschluss">
 <div class="closer__bg"><img data-plx src="assets/closer-terrace.webp" alt="Abendstimmung auf einer Steinterrasse über dem Meer, Menschen im Gespräch" width="1536" height="1024"></div>
 <div class="wrap"><div class="closer__in">
  <h2 class="rv">Finde das Seminar,<br>das zu deinem Alltag passt.</h2>
  <p class="rv">Ein Gespräch, 30 Minuten, kostenlos. Du klärst, wo du stehst und welcher Termin für dich geht. Danach entscheidest du in Ruhe.</p>
  <ul class="rv">{li}</ul>
  <p class="proofline rv">{STARS} 250 Bewertungen auf ProvenExpert, davon 227 mit 5 Sternen</p>
  <div class="cta-row rv">{btn('abschluss', 'btn btn--light cta--breathe')}<p class="tel">Lieber anrufen: <a href="{TEL}">+49 15888367664</a></p></div>
  <p class="back rv">Zurück zur <a href="{V2}index.html">Startseite</a></p>
 </div></div>
</section>
{foot}'''


ORG = 'https://www.meandyou.de/#organization'
COURSES = [
 ('frei-sprechen', 'Frei sprechen, auch mit Lampenfieber (Arbeitstitel Rhetorik I)', 'Sicher auftreten, Rede halten, Struktur, eigener Redestil, Sprache, Körpersprache, Fragen stellen. 3 Trainingstage und 1 Tag Get Together, 14 Plätze.',
  [('Mallorca', '2026-12-03', '2026-12-06'), ('Mallorca', '2027-03-04', '2027-03-07'), ('Mallorca', '2027-04-29', '2027-05-02'), ('Frankfurt', '2027-06-17', '2027-06-20'), ('Berlin', '2027-08-12', '2027-08-15'), ('Mallorca', '2027-10-14', '2027-10-17')]),
 ('ruhig-bleiben', 'Ruhig bleiben, wenn es eng wird (Arbeitstitel Rhetorik II)', 'Schlagfertigkeit, Überzeugungspsychologie, unfaire Methoden kontern, Körpersprache, Meetings leiten. 10 Plätze.',
  [('Barcelona', '2027-04-15', '2027-04-18'), ('Barcelona', '2027-10-21', '2027-10-24')]),
 ('mit-sprache-fuehren', 'Mit Sprache führen (Arbeitstitel Rhetorik III)', 'Kritik klar formulieren, Zuhören, Stegreifrede, Gruppen überzeugen, DeepOcean. 12 Plätze.',
  [('Dubai', '2026-12-10', '2026-12-13'), ('Zypern', '2027-10-07', '2027-10-10')]),
]


def schema():
    import json
    g = [{"@type": "WebPage", "@id": "https://www.meandyou.de/seminare#webpage", "url": "https://www.meandyou.de/seminare", "name": "Rhetorik-Seminare mit Michael Ehlers | Inhalte und Termine", "inLanguage": "de"},
         {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://www.meandyou.de/"}, {"@type": "ListItem", "position": 2, "name": "Seminare", "item": "https://www.meandyou.de/seminare"}]},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Institut Michael Ehlers GmbH", "alternateName": "me&you Communication", "url": "https://www.meandyou.de/",
          "address": {"@type": "PostalAddress", "streetAddress": "Landsknechtstraße 50", "postalCode": "96103", "addressLocality": "Hallstadt", "addressCountry": "DE"}},
         {"@type": "Person", "@id": "https://www.meandyou.de/#michael", "name": "Michael Ehlers", "jobTitle": "Rhetoriktrainer", "worksFor": {"@id": ORG}}]
    for cid, name, desc, inst in COURSES:
        g.append({"@type": "Course", "@id": f"https://www.meandyou.de/seminare#{cid}", "name": name, "description": desc, "inLanguage": "de", "provider": {"@id": ORG},
                  "hasCourseInstance": [{"@type": "CourseInstance", "courseMode": "Onsite", "startDate": s, "endDate": en, "location": {"@type": "Place", "name": o, "address": o},
                                         "instructor": {"@id": "https://www.meandyou.de/#michael"}} for o, s, en in inst]})
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


def page():
    body = header() + '<main>' + s01() + s02() + s03() + s04() + s05() + s06() + s07() + s08() + s09() + s10() + s11() + '</main>' + s12() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Rhetorik-Seminare mit Michael Ehlers | Inhalte und Termine</title>
<meta name="description" content="Drei Rhetorik-Seminare zur Wahl: frei sprechen, schlagfertig bleiben, mit Sprache führen. Drei Tage in kleiner Gruppe. Kostenloses Gespräch buchen.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema()}</script>
</head><body>{body}<script>{home.JS}</script></body></html>'''


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
