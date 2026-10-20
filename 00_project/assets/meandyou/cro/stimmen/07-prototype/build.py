"""Build the CRO prototype of the me&you page "Stimmen" (desktop 1440 px). Text = 04-copy/approved-copy.md.
Design system = homepage + seminar + Michael page (imported, same chain as cro/rhetorik). Run: python3 build.py -> index.html.
Serve: python3 -m http.server 8816"""
import importlib.util, json, os
HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


mic = load('mic_build', os.path.join(HERE, '..', '..', 'michael', '07-prototype', 'build.py'))
sem, home = mic.sem, mic.home
V2 = sem.V2
TEL = sem.TEL
BOOK = V2 + 'termin.html?utm_source=stimmen&utm_content='
VID = 'assets/v-stimme-%d.mp4'  # Wistia MP4 re-encoded (crf 30), posters cut above the burned-in captions
e, STARS, CHECK, PLAY, t = home.e, home.STARS, home.CHECK, home.PLAY, sem.t


def btn(utm, cls='btn'):
    return f'<a class="{cls}" href="{BOOK}{utm}">Gespräch buchen</a>'


def ico(d):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'


I_SPEAK = ico('<path d="M4 5h16v10H9l-5 4z"/><path d="M8 9h8M8 12h5"/>')
I_CAM = ico('<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3"/>')
I_VR = ico('<path d="M3 8h18v8h-6l-3-3-3 3H3z"/><circle cx="8" cy="12" r="1.2"/><circle cx="16" cy="12" r="1.2"/>')
I_PIN = ico('<path d="M12 21s-6-5.6-6-11a6 6 0 0 1 12 0c0 5.4-6 11-6 11z"/><circle cx="12" cy="10" r="2.2"/>')

CSS = mic.CSS + r"""
/* stimmen page additions */
.hero--vids{min-height:820px}
.hero__vids{position:absolute;top:40px;bottom:0;right:10px;width:46%;display:flex;align-items:center;justify-content:center;text-decoration:none;cursor:pointer;z-index:3}
.hero__vids .hv{width:196px;aspect-ratio:9/16;border-radius:22px;overflow:hidden;box-shadow:0 18px 44px rgba(42,38,34,.18);position:relative;background:#ddd;transition:transform .35s cubic-bezier(.22,1,.36,1),box-shadow .35s}
.hero__vids .hv img{width:100%;height:100%;object-fit:cover}
.hero__vids .hv:nth-child(1){transform:translate(26px,40px) rotate(-3deg)}
.hero__vids .hv:nth-child(2){transform:translateY(-20px);z-index:2;width:216px}
.hero__vids .hv:nth-child(3){transform:translate(-26px,56px) rotate(3deg)}
.hero__vids:hover .hv{box-shadow:0 24px 54px rgba(42,38,34,.26)}
.hero__vids:hover .hv:nth-child(2){transform:translateY(-28px)}
.hero__vids .hv b{position:absolute;left:0;right:0;top:52%;margin:auto;transform:translateY(-50%);width:52px;height:52px;border-radius:50%;background:rgba(255,255,255,.92);display:grid;place-items:center}
.hero__vids .hv b svg{width:20px;height:20px;fill:var(--navy);margin-left:3px}
.hero__vids .hv span{position:absolute;left:12px;bottom:10px;color:#fff;font-size:15px;font-weight:600;text-shadow:0 1px 4px rgba(0,0,0,.5)}
.hero__vids .go{position:absolute;top:calc(50% + 196px);left:50%;transform:translateX(-50%);z-index:4;display:inline-flex;align-items:center;gap:8px;background:var(--paper);color:var(--cta);font:600 16px/1 var(--sans);padding:12px 18px;border-radius:999px;box-shadow:0 6px 18px rgba(42,38,34,.14);white-space:nowrap}
.hero__vids .go svg{width:16px;height:16px}
.hero__vids .hv:nth-child(3) span{left:auto;right:12px}
#videos{scroll-margin-top:110px}
.hero--vids .hero__txt{max-width:640px}
.hero--vids .proofline{white-space:nowrap}
.hero .skip{font-size:16px}
.ans{font:400 23px/1.5 var(--serif);color:var(--ink);max-width:34em}
#erfahrungen h2{font-size:38px}
#erfahrungen .proof__grid{grid-template-columns:1.35fr .9fr;gap:56px}
.nums{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.num{background:var(--paper);border-radius:18px;padding:24px 24px 22px;display:flex;flex-direction:column;gap:6px}
.num b{font:400 40px/1 var(--serif);color:var(--cta)}
.num span{font-size:16px;color:var(--muted);line-height:1.4}
.vcols{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:52px}
.vcol{display:flex;flex-direction:column;gap:16px}
.vcol .vid{width:100%;max-width:340px;aspect-ratio:9/16;border-radius:22px;cursor:pointer}
.vcol .vid b{top:52%;bottom:auto;transform:translateY(-50%);width:64px;height:64px}
.vcol .vid b svg{width:26px;height:26px}
.vbox{position:fixed;inset:0;z-index:200;background:rgba(24,30,40,.82);display:none;align-items:center;justify-content:center}
.vbox.open{display:flex}
.vbox video{height:86vh;aspect-ratio:9/16;border-radius:18px;background:#000}
.vbox button{position:absolute;top:24px;right:32px;width:48px;height:48px;border-radius:50%;border:0;background:var(--paper);color:var(--navy);font:400 28px/1 var(--sans);cursor:pointer}
.vcol h3{font:600 18px/1.35 var(--sans)}
.vcol h3 .fehlt{margin-left:4px;font-size:14px}
.vcol blockquote{margin:0;font:italic 400 21px/1.45 var(--serif);color:var(--ink)}
.vcol p{font-size:17px;color:var(--muted)}
.note{font-size:16px;color:var(--muted);margin-top:36px}
.themes{display:grid;grid-template-columns:repeat(6,1fr);gap:22px;margin-top:48px}
.theme{grid-column:span 2;background:#fff;border-radius:var(--r);padding:30px 28px;display:flex;flex-direction:column;gap:18px}
.theme:nth-child(4),.theme:nth-child(5){grid-column:span 3}
.theme h3{font:400 21px/1.3 var(--serif);color:var(--cta)}
.theme figure{margin:0;display:flex;flex-direction:column;gap:8px}
.theme figure+figure{padding-top:16px;border-top:1px solid var(--line)}
.theme blockquote{margin:0;font:italic 400 17.5px/1.55 var(--serif);color:var(--ink)}
.theme figcaption{font-size:15px;color:var(--muted)}.theme figcaption b{color:var(--ink);font-weight:600}
.pub{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:44px}
.pq{background:var(--cream);border-radius:var(--r);padding:28px 26px;display:flex;flex-direction:column;gap:14px}
.pq .mk{height:34px;display:flex;align-items:center;justify-content:flex-end;order:3}
.pq .mk img{max-height:34px;max-width:140px;object-fit:contain;filter:grayscale(1);opacity:.75}
.pq .mk i{font:400 54px/1 var(--serif);color:var(--dove);font-style:normal;height:34px;overflow:hidden}
.pq{background:#fff;margin:0}
.pq blockquote{margin:0;font:italic 400 18px/1.5 var(--serif);color:var(--ink);flex:1;order:1}
.pq p{order:2}
.pq p{font-size:15px;color:var(--muted)}.pq p b{display:block;color:var(--ink);font-size:16px}
.seminar{display:grid;grid-template-columns:.8fr 1.2fr;gap:56px;align-items:start}
.seminar .grp{height:640px}
.blocks{display:grid;grid-template-columns:1fr 1fr;gap:30px 32px;margin-top:10px}
.blk{display:grid;grid-template-columns:44px 1fr;gap:16px}
.blk svg{width:30px;height:30px;color:var(--cta);margin-top:2px}
.blk h3{font:600 19px/1.35 var(--sans);margin-bottom:6px}
.blk p{font-size:17px;color:var(--muted)}
.blk blockquote{margin:10px 0 0;font:italic 400 16.5px/1.5 var(--serif);color:var(--ink)}
.blk blockquote small{display:block;font:400 14.5px/1.4 var(--sans);color:var(--muted);margin-top:4px}
.mic{display:grid;grid-template-columns:.8fr 1.2fr;gap:64px;align-items:center}
.mic{grid-template-columns:.62fr 1.38fr}
.mic .portrait{height:520px;border-radius:var(--r);overflow:hidden}
.mic .qq{display:grid;grid-template-columns:1fr 1fr;gap:32px}
.mic .row{display:flex;align-items:center;gap:28px}
.mic .portrait img{width:100%;height:108%;object-fit:cover;object-position:50% 0}
.mic blockquote{margin:0;font:italic 400 19px/1.5 var(--serif);color:var(--ink);padding-left:20px;border-left:2px solid var(--sand)}
.mic blockquote small{display:block;font:400 15px/1.4 var(--sans);color:var(--muted);margin-top:6px}
.trans{display:grid;grid-template-columns:1.15fr .85fr;gap:64px;align-items:start}
.trans p{font-size:18px;color:var(--muted);max-width:36em}
.bars{background:#fff;border-radius:var(--r);padding:32px 32px 28px;display:flex;flex-direction:column;gap:14px}
.bars h3{font:600 17px/1.3 var(--sans)}
.bar{display:grid;grid-template-columns:70px 1fr 44px;align-items:center;gap:14px;font-size:16px;color:var(--muted)}
.bar i{display:block;height:12px;border-radius:6px;background:var(--cream);position:relative;overflow:hidden}
.bar i::after{content:"";position:absolute;inset:0 auto 0 0;width:var(--w);background:var(--cta);border-radius:6px;transform-origin:left;transform:scaleX(0);transition:transform .9s cubic-bezier(.22,1,.36,1)}
.is-in .bar i::after,.shot .bar i::after{transform:scaleX(1)}
.bar b{color:var(--ink);text-align:right}
.bars .srcs{font-size:14.5px;color:var(--muted);border-top:1px solid var(--line);padding-top:14px;margin-top:4px}
.closer .links{color:rgba(255,255,255,.85);font-size:17px}
#faq .acc{grid-template-columns:1fr}
#faq .acc details:nth-child(2){border-top:0}
#oeffentlich{padding:100px 0}
"""


def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="{V2}index.html"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="{V2}seminare.html">Seminare</a><a href="{V2}michael.html">Michael</a><a href="{V2}rhetorik.html">Was ist Rhetorik</a><a href="#top" aria-current="page" style="color:var(--cta)">Stimmen</a><a href="{V2}faq.html">FAQ</a></nav>
 <a class="btn" href="{BOOK}header">Gespräch buchen</a>
</div></header>'''


def s01():
    v = ''.join(f'<div class="hv"><img src="assets/vp-{i}-tall.webp" alt="" width="540" height="960"><b>{PLAY}</b><span>{d}</span></div>' for i, d in [(1, '1:00'), (2, '1:12'), (3, '1:23')])
    arrow = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>'
    return f'''
<section class="hero hero--vids" id="top">
 <a class="hero__vids js-tovideos" href="#videos" aria-label="Direkt zu den Videos">{v}<span class="go" aria-hidden="true">Direkt zu den Videos {arrow}</span></a>
 <div class="wrap hero__in"><div class="hero__txt">
  <p class="proofline rv">{STARS} 227 von 250 Bewertungen mit 5 Sternen auf ProvenExpert · über 8.000 Teilnehmer</p>
  <h1 class="rv"><span class="kicker">Michael Ehlers Erfahrungen:</span><span class="big">Vorher.<br>Nachher.</span></h1>
  <p class="sub rv">Was Teilnehmer nach ihrem Seminar mit Michael Ehlers anders machen. In ihren eigenen Worten.</p>
  <p class="body rv">Hier findest du Kundenstimmen zum Rhetorik-Seminar: wie Menschen es erlebt haben und was sich an ihrer Kommunikation geändert hat. Jede Stimme steht mit ihrer Quelle da. Wir zeigen Ausschnitte, Kürzungen im Satz markieren wir mit […].</p>
  <div class="cta-row rv">
   {btn('hero', 'btn cta--breathe')}
   <p class="assure">{CHECK}30 Minuten, kostenlos, per Video. Du klärst, ob das Seminar zu dir passt.</p>
   <a class="tlink skip js-tovideos" href="#videos">Direkt zu den Videos</a>
  </div>
 </div></div>
</section>'''


def s02():
    N = [('250', 'Bewertungen auf ProvenExpert, 227 davon mit 5 Sternen'), ('Seit 2016', 'ist Michaels Profil dort aktiv'),
         ('Über 8.000', 'Teilnehmer in seinen Seminaren'), ('3 Videos', 'in denen Teilnehmer selbst erzählen')]
    b = ''.join(f'<div class="num"><b>{k}</b><span>{v}</span></div>' for k, v in N)
    return f'''
<section class="proof" id="erfahrungen">
 <div class="wrap"><div class="proof__grid">
  <div class="stack rv"><h2>Welche Erfahrungen machen Teilnehmer mit Michael Ehlers?</h2>
   <p class="ans">Teilnehmer beschreiben vor allem drei Dinge: viel Übung vor der Gruppe, eine direkte Rückmeldung von Michael und mehr Sicherheit beim Sprechen. Auf ProvenExpert haben 227 von 250 Bewertungen 5 Sterne, keine Bewertung dort liegt unter 3 Sternen.</p></div>
  <div class="rv" data-in><div class="nums">{b}</div></div>
 </div></div>
</section>'''


VIDS = [
 (1, '1:00', 'Video 1 (1:00): Klarer erklären.', '„Früher brauchte ich zehn Minuten, Dinge zu erklären. Heute gelingt mir das in zwei Minuten und jeder versteht mich gleich.“',
  'Vorher hatte er im Internet recherchiert und Bücher gelesen. „Es ist kein echtes Üben, man bekommt kein Feedback.“ „Es gab auf jeden Fall Missverständnisse.“ Heute sagt er: „Ja, mein Selbstbewusstsein ist auf jeden Fall gewachsen.“'),
 (2, '1:12', 'Video 2 (1:12): Weniger Herzpochen.', '„Ich hab mich tatsächlich jetzt auch kurz vor dem Seminar zum Teil vor den Konflikten gescheut.“',
  'Es fehlten ihr die Werkzeuge, um frei zu sprechen. Sie war noch etwas aufgeregt, „aber gar nicht mehr dieses extreme Herzpochen“. Ein Mitarbeitergespräch hatte sie lange aufgeschoben.'),
 (3, '1:23', 'Video 3 (1:23): Kürzere Meetings.', '„Unsere Teammeetings gingen von zwei Stunden auf fünfundvierzig Minuten runter und wir sind produktiver geworden.“',
  'Vor dem Seminar lag ihr Selbstbewusstsein in Gesprächen nach eigenen Worten „bei minus eins“. „Nach der ersten Übung haben wir Feedback bekommen. Das hat sich eingeprägt.“ Heute spricht sie langsamer: „früher war ich schneller, viel zu schnell eigentlich“.'),
]


def s03():
    c = ''.join(f'''<div class="vcol rv" data-d="{i-1}">
   <div class="vid" data-src="{VID % i}" role="button" tabindex="0" aria-label="Video {i} abspielen"><img src="assets/vp-{i}-tall.webp" alt="Standbild aus Video {i}: Teilnehmerstimme" width="540" height="960"><b>{PLAY}</b><span>{d}</span></div>
   <h3>{e(h)} {t('[von Kunde bestätigen: Vorname und Rolle]')}</h3>
   <blockquote>{e(q)}</blockquote>
   <p>{e(p)}</p>
  </div>''' for i, d, h, q, p in VIDS)
    return f'''
<section class="sec" id="videos">
 <div class="wrap">
  <div class="stack"><p class="ov rv">Stimmen</p><h2 class="rv">Vorher. Nachher.</h2>
   <p class="lead rv">Drei Teilnehmer erzählen vor der Kamera, wo sie vor dem Seminar standen und was sich danach geändert hat.</p></div>
  <div class="vcols">{c}</div>
  <p class="note center rv">Das sind Erfahrungen einzelner Teilnehmer, wörtlich aus den Videos. Diese Erfahrungen sind keine Zusage für dein Ergebnis.</p>
  <div class="center"><div class="cta-row rv" style="margin-top:26px">{btn('videos')}</div></div>
 </div>
</section>'''


THEMES = [
 ('Redeangst: was Teilnehmer erleben', [
   ('„Michael schafft es, das Maximum aus einem rauszuholen und die Redeangst zu nehmen.“', 'Julian L.', 'Rhetorik 1 auf Mallorca, ProvenExpert, 2023'),
   ('„Zu beobachten und selbst zu erfahren beim Sprechen viel sicherer und dadurch viel authentischer zu sein war einfach der Wahnsinn.“', 'Jenny E.', 'Google')]),
 ('Praxis statt Theorie', [
   ('„Seine Tipps sind soo wertvoll und die praktischen Übungen zeigten direkt einen Unterschied!“', 'Anna H.', 'Google'),
   ('„Zudem habe ich Werkzeuge mitnehmen dürfen die mir in der Rhetorik und meinen Presentationen enorm weiterhelfen werden.“', 'Oliver E.', 'Google')]),
 ('Eine Rückmeldung, mit der du arbeiten kannst', [
   ('„Die Herangehensweise und das individuelle Feedback haben mich sehr motiviert und mir unheimlich viel Selbstvertrauen geschenkt um das Beste aus mir rauszuholen.“', 'Jasmina L.', 'Rhetorik 1 auf Mallorca, ProvenExpert, 2023'),
   ('„Neben den witzigen Übungen zu den Vortragstechniken, haben mir auch die Feedback-Übungen sehr gut gefallen […]“', 'Anonym', 'Rhetorik 1 auf Mallorca, ProvenExpert, 2023')]),
 ('Für Anfänger und für Profis', [
   ('„Ich fand es spannend, dass wir Teilnehmer ein Mix von Anfänger bis Profi waren und Michael uns alle, egal auf welchem Level, weiterbringen konnte.“', 'Christin R.', 'Rhetorik 1 auf Mallorca, ProvenExpert, 2023'),
   ('„Herr Ehlers versteht es auf die Bedürfnisse aller Teilnehmenden einzugehen und dabei das Gesamtziel nicht aus dem Auge zu verlieren.“', 'Moritz B.', 'Rhetorik 1 auf Mallorca, ProvenExpert, 2023')]),
 ('Mehr über dich selbst erfahren', [
   ('„Ich habe viel über mich selbst herausgefunden.“', 'Tino R.', 'Google'),
   ('„[…] jeder von uns durfte sich selbst besser kennenlernen und mehr darüber erfahren wer er wirklich ist.“', 'Jenny E.', 'Google')]),
]


def s04():
    c = ''.join('<div class="theme rv"><h3>%s</h3>%s</div>' % (e(h), ''.join(f'<figure><blockquote>{e(q)}</blockquote><figcaption><b>{e(n)}</b>, {e(s)}</figcaption></figure>' for q, n, s in Q)) for h, Q in THEMES)
    return f'''
<section class="sec sec--cream" id="themen">
 <div class="wrap">
  <div class="stack"><h2 class="rv">Was sich für Teilnehmer verändert</h2><p class="lead rv">Jeder kommt mit einem anderen Anliegen. Wir haben die Stimmen nach fünf Themen geordnet.</p></div>
  <div class="themes">{c}</div>
  <p class="note center rv">Alle Stimmen sind einzelne Erfahrungen und keine Zusage für dein Ergebnis.</p>
 </div>
</section>'''


def s05():
    P = [('<img src="assets/logo-bju.webp" alt="Die Jungen Unternehmer">', '„Ein begeisterndes Training mit einer anregenden und humorvollen Atmosphäre. Rundum gelungen.“', 'Sarna Röser', 'Bundesvorsitzende „Die Jungen Unternehmer“ Berlin'),
         ('<img src="assets/logo-mdr.webp" alt="MDR">', '„Trotz 40 Jahren Medienerfahrung konnte ich erstaunlich viel vom Rhetoriktraining profitieren.“', 'Peter Escher', 'Moderator MDR'),
         ('<i aria-hidden="true">„</i>', '„Ich habe in diesem Kurs mehr gelernt als in all meinen bisherigen Schulungen zusammen.“', 'Emrullah Ates', 'Teilnehmer, Google')]
    c = ''.join(f'<figure class="pq rv"><div class="mk">{m}</div><blockquote>{e(q)}</blockquote><p><b>{e(n)}</b>{e(r)}</p></figure>' for m, q, n, r in P)
    c += f'<figure class="pq rv"><div class="mk"><i aria-hidden="true">„</i></div><blockquote>{t("[von Kunde bestätigen: vollständiger Wortlaut]")}</blockquote><p><b>Neven Subotic</b>Fußball-Bundesliga-Profi</p></figure>'
    return f'''
<section class="sec" id="oeffentlich">
 <div class="wrap">
  <div class="stack"><h2 class="rv">Auch wer schon viel weiß, lernt dazu</h2><p class="lead rv">Diese Stimmen stehen schon heute auf der Website von me&amp;you.</p></div>
  <div class="pub">{c}</div>
 </div>
</section>'''


def s06():
    B = [(I_SPEAK, 'Du hältst Reden vor der Gruppe.', 'Drei Tage Training, dazu ein Tag Get Together.', '„Besonders beeindruckt hat mich der Praxisteil, in dem wir freie Reden vor der Gruppe hielten […]“', 'Michael B., Rhetorik 1 auf Mallorca, ProvenExpert, 2023'),
         (I_CAM, 'Du siehst dich auf Video.', 'Drei Videoanalysen mit sofortiger Rückmeldung.', '„Die Trainings vor der Kamera mit den darauf folgenden Auswertungen helfen die Selbst- und Fremdwahrnehmung zu schärfen.“', 'Julian L., Rhetorik 1 auf Mallorca, ProvenExpert, 2023'),
         (I_VR, 'Du sprichst vor virtuellem Publikum.', 'Im VR-Training sprichst du vor einem großen virtuellen Publikum. Michael B. nennt das „unglaublich real“.', '', ''),
         (I_PIN, 'Du lernst an besonderen Orten.', 'Die Seminare finden auf Mallorca, in Barcelona, Zypern, Dubai, Frankfurt und Berlin statt.', '„Ich war vergangenes Wochenende 4 Tage auf Mallorca zum Rhetorikseminar auf Empfehlung von einem Bekannten. Es war wirklich richtig gut !“', 'Belinda E., Google')]
    c = ''.join(f'<div class="blk rv">{i}<div><h3>{h}</h3><p>{e(p)}</p>' + (f'<blockquote>{e(q)}<small>{e(s)}</small></blockquote>' if q else '') + '</div></div>' for i, h, p, q, s in B)
    return f'''
<section class="sec sec--cream" id="seminar">
 <div class="wrap seminar">
  <div class="grp rv"><img data-plx src="assets/seminar-group.webp" alt="Eine Seminargruppe mit Zertifikaten unter Palmen" width="1350" height="1800"></div>
  <div class="stack">
   <h2 class="rv">Was Teilnehmer im Seminar erleben</h2>
   <p class="lead rv">Die Stimmen beschreiben immer wieder dieselben Bausteine. So sieht ein Seminar mit Michael aus.</p>
   <div class="blocks">{c}</div>
   <p class="lead rv">Alle Formate, Orte und Termine findest du auf der Seite <a class="tlink" href="{V2}seminare.html">Seminare</a>.</p>
   <div class="cta-row rv">{btn('seminar')}</div>
  </div>
 </div>
</section>'''


def s07():
    return f'''
<section class="sec" id="michael">
 <div class="wrap mic">
  <div class="portrait rv"><img data-plx src="assets/michael-white.webp" alt="Michael Ehlers im weißen Hemd" width="988" height="1312"></div>
  <div class="stack">
   <h2 class="rv">Wer hinter den Stimmen steht</h2>
   <p class="lead rv">Michael Ehlers gibt seit 1990 Rhetorikseminare, also seit über 30 Jahren. Er hat neun Bücher als Autor oder Herausgeber veröffentlicht und hat einen Lehrauftrag an der Universität St. Gallen. Seine Methode hat drei Teile: Persönlichkeit. Kongruenz. Wirkung. Du sprichst so, dass es zu dir passt.</p>
   <div class="qq rv"><blockquote>„Ich habe gelernt, meine innere Haltung zum Ausgangspunkt jeder Präsentation zu machen […]“<small>Adrian B., Google</small></blockquote>
   <blockquote>„Mit Humor und Leichtigkeit verschmelzen Theorie und Praxis miteinander und das Lernen wird einfach.“<small>Andreas M., ProvenExpert, 2023</small></blockquote></div>
   <div class="row rv"><a class="tlink" href="{V2}michael.html">Mehr über Michael</a>{btn('michael')}</div>
  </div>
 </div>
</section>'''


def s08():
    R = [('5 Sterne', 227), ('4 Sterne', 21), ('3 Sterne', 2), ('2 Sterne', 0), ('1 Stern', 0)]
    bars = ''.join(f'<div class="bar"><span>{k}</span><i style="--w:{max(v / 227 * 100, 0):.1f}%"></i><b>{v}</b></div>' for k, v in R)
    return f'''
<section class="sec sec--cream" id="herkunft">
 <div class="wrap trans">
  <div class="stack">
   <h2 class="rv">Woher die Stimmen kommen</h2>
   <p class="rv">Die Zitate auf dieser Seite stammen aus vier Quellen: aus dem Profil von Michael Ehlers auf ProvenExpert, aus Bewertungen bei Google, aus drei Videos, in denen Teilnehmer erzählen, und aus Stimmen, die schon auf meandyou.de stehen.</p>
   <p class="rv">Auf ProvenExpert stehen 250 veröffentlichte Bewertungen. 227 davon haben 5 Sterne, 21 haben 4 Sterne und 2 haben 3 Sterne. Keine Bewertung hat 1 oder 2 Sterne. Das Profil ist seit 2016 aktiv. ProvenExpert schreibt selbst, dass die Bewertungen freiwillig sind und nicht gekauft werden können.</p>
   <p class="rv">Wir zitieren wörtlich, auch mit Tippfehlern. Wir zeigen Ausschnitte. Kürzungen im Satz markieren wir mit […]. Bei ProvenExpert nennen wir Vorname und Initial (oder Anonym), das Seminar, wenn angegeben, und das Jahr. Bei Google nennen wir Vorname und Initial. Jede Stimme gibt die Meinung eines Menschen wieder. Dein Weg kann anders aussehen.</p>
  </div>
  <div class="bars rv" data-in><h3>250 Bewertungen auf ProvenExpert</h3>{bars}</div>
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
  <h2 class="center rv">Erst reden wir. Dann entscheidest du.</h2>
  <div class="flow rv" data-in><div class="flow__line"><i></i></div>{c}</div>
  <div class="center"><div class="cta-row rv" style="margin-top:56px">{btn('gespraech')}<p class="assure">{CHECK}Kostenlos. Lieber anrufen: <a href="{TEL}">+49 15888367664</a></p></div></div>
 </div>
</section>'''


FAQ = [
 ('Wie sind die Erfahrungen mit Michael Ehlers?', 'Auf ProvenExpert haben 227 von 250 Bewertungen 5 Sterne. In den Texten geht es oft um Übung vor der Gruppe, um Michaels direkte Rückmeldung und um mehr Sicherheit beim Sprechen. Auch bei Google schreiben Teilnehmer über ihre Seminartage.'),
 ('Gibt es auch Kritik an Michael Ehlers?', 'Ja, nicht jede Stimme ist begeistert. Auf ProvenExpert haben 21 Bewertungen 4 Sterne und zwei Bewertungen 3 Sterne. Auch bei Google stehen nicht nur positive Bewertungen. Alle Bewertungen kannst du dort selbst lesen.'),
 ('Sind die Bewertungen echt?', 'Die Zitate stammen aus öffentlichen Profilen bei ProvenExpert und Google, aus drei Videos und von der Website von me&you. Laut ProvenExpert sind Bewertungen dort freiwillig und können nicht gekauft werden. In den Videos sprechen Teilnehmer selbst über ihr Seminar.'),
 ('Für wen ist das Seminar laut Teilnehmern geeignet?', 'Teilnehmer beschreiben Gruppen von Anfängern bis Profis. In den Videos empfehlen zwei Teilnehmer das Seminar ausdrücklich Geschäftsführern. Ob es für dich passt, klärst du im kostenlosen Gespräch.'),
 ('Wie kann ich Rhetorik trainieren?', 'Teilnehmer nennen oft dasselbe: reden und Rückmeldung bekommen. Dann wieder reden. Ein Teilnehmer sagt im Video über Bücher und Internet: „Es ist kein echtes Üben, man bekommt kein Feedback.“ Mehr dazu liest du in den <a class="tlink" href="' + V2 + 'faq.html">häufigen Fragen</a>.'),
 ('Was kostet ein Rhetorikkurs bei Michael Ehlers?', 'Den Preis für dein Seminar nennt dir Michaels Team im kostenlosen Gespräch. Dort klärst du auch, welches Format zu dir passt.'),
]


def s10():
    def ans(a):
        return a if '<a ' in a else e(a)
    items = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div class="a">{ans(a)}</div></details>' for i, (q, a) in enumerate(FAQ))
    return f'''
<section class="sec" id="faq">
 <div class="wrap faqgrid">
  <div class="stack" style="position:sticky;top:120px"><p class="ov rv">FAQ</p><h2 class="rv">Häufige Fragen zu den Erfahrungen</h2></div>
  <div class="acc rv">{items}</div>
 </div>
</section>'''


def s11():
    li = ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in ['per Video, von überall', 'Termin online wählen', 'Seminare an sechs Orten'])
    foot = home.section_closer().split('<footer', 1)[1]
    foot = '<footer' + foot.replace(home.BOOK, BOOK).replace('href="#termine"', f'href="{V2}seminare.html#termine"')
    return f'''
<section class="closer" id="abschluss">
 <div class="closer__bg"><img data-plx src="assets/closer-terrace.webp" alt="Abendstimmung auf einer Steinterrasse über dem Meer, Menschen im Gespräch" width="1536" height="1024"></div>
 <div class="wrap"><div class="closer__in">
  <h2 class="rv">Deine Stimme kommt später.<br>Erst kommt das Gespräch.</h2>
  <p class="rv">Der erste Schritt ist ein Gespräch von 30 Minuten. Kostenlos und per Video. Danach weißt du, ob das Seminar zu dir passt.</p>
  <ul class="rv">{li}</ul>
  <p class="proofline rv">{STARS} 227 von 250 Bewertungen mit 5 Sternen auf ProvenExpert</p>
  <div class="cta-row rv">{btn('abschluss', 'btn btn--light cta--breathe')}<p class="tel">Lieber anrufen: <a href="{TEL}">+49 15888367664</a></p></div>
  <p class="back rv">Zurück zur <a href="{V2}index.html">Startseite</a></p>
 </div></div>
</section>
{foot}'''


def schema():
    ORG = 'https://www.meandyou.de/#organization'
    URL = 'https://www.meandyou.de/stimmen'
    g = [{"@type": "WebPage", "@id": URL + "#webpage", "url": URL, "name": "Michael Ehlers Erfahrungen: Stimmen von Teilnehmern", "inLanguage": "de",
          "about": {"@id": ORG}, "isPartOf": {"@id": "https://www.meandyou.de/#website"}},
         {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://www.meandyou.de/"}, {"@type": "ListItem", "position": 2, "name": "Stimmen", "item": URL}]},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Institut Michael Ehlers GmbH", "alternateName": "me&you Communication", "url": "https://www.meandyou.de/",
          "address": {"@type": "PostalAddress", "streetAddress": "Landsknechtstraße 50", "postalCode": "96103", "addressLocality": "Hallstadt", "addressCountry": "DE"}}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


VJS = r"""
(function(){
 var rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
 document.querySelectorAll('.js-tovideos').forEach(function(a){ a.addEventListener('click', function(ev){ var t=document.getElementById('videos'); if(!t) return; ev.preventDefault(); t.scrollIntoView({behavior: rm ? 'auto' : 'smooth', block:'start'}); history.replaceState(null,'','#videos'); }); });
})();
(function(){
 var box=document.createElement('div'); box.className='vbox'; box.setAttribute('role','dialog'); box.setAttribute('aria-label','Teilnehmervideo');
 box.innerHTML='<video controls playsinline></video><button type="button" aria-label="Video schließen">×</button>'; document.body.appendChild(box);
 var v=box.querySelector('video');
 function close(){ v.pause(); box.classList.remove('open'); }
 box.querySelector('button').addEventListener('click', close); box.addEventListener('click', function(ev){ if(ev.target===box) close(); });
 addEventListener('keydown', function(ev){ if(ev.key==='Escape') close(); });
 document.querySelectorAll('.vcol .vid').forEach(function(el){
  function open(){ v.src=el.dataset.src; box.classList.add('open'); v.play().catch(function(){}); }
  el.addEventListener('click', open); el.addEventListener('keydown', function(ev){ if(ev.key==='Enter'||ev.key===' '){ ev.preventDefault(); open(); } });
 });
})();
"""


def page():
    body = header() + '<main>' + s01() + s02() + s03() + s04() + s05() + s06() + s07() + s08() + s09() + s10() + '</main>' + s11() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Michael Ehlers Erfahrungen: Stimmen von Teilnehmern</title>
<meta name="description" content="Michael Ehlers Erfahrungen: 227 von 250 Bewertungen auf ProvenExpert mit 5 Sternen. Videos und Zitate, wörtlich und mit Quelle. Was Teilnehmer erleben.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema()}</script>
</head><body>{body}<script>{home.JS}{VJS}</script></body></html>'''


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
