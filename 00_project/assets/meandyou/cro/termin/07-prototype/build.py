"""Build the CRO prototype of the me&you booking page "Gespräch buchen" (desktop 1440 px). Text = 04-copy/approved-copy.md.
Design system = homepage + seminar + Michael + Rhetorik pages (imported). Main CTA = Calendly inline (#kalender).
UTM values of the page URL go into the Calendly URL before the widget loads. After a booking (postMessage
calendly.event_scheduled) the left column switches to the confirmation state S08. Preview of that state: ?booked=1.
Run: python3 build.py"""
import importlib.util, json, os
HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


rh = load('rh_build', os.path.join(HERE, '..', '..', 'rhetorik', '07-prototype', 'build.py'))
mic, sem, home = rh.mic, rh.sem, rh.home
e, STARS, CHECK, PLAY, t = home.e, home.STARS, home.CHECK, home.PLAY, sem.t
TEL = 'tel:+4915888367664'
CAL = 'https://calendly.com/me-you/sichtbarkeit-neu'
CAL_OPTS = 'hide_event_type_details=1&hide_gdpr_banner=1&background_color=ffffff&text_color=2a2622&primary_color=4f6d90'


def btn(cls='btn'):
    return f'<a class="{cls}" href="#kalender" data-jump>Termin wählen</a>'


ICON = {
 'room': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18M5 21V9l7-5 7 5v12"/><path d="M10 21v-6h4v6"/></svg>',
 'sit': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h7M8.5 14h4"/></svg>',
 'pen': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 6l3 3"/></svg>',
 'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
 'user': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="8.5" r="4"/><path d="M4 21a8 8 0 0 1 16 0z"/></svg>',
 'lock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
 'ok': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
}

CSS = rh.CSS + r"""
/* booking page */
.hdr--min{position:absolute;top:0}
.hdr--min .hdr__in{gap:20px;background:none;box-shadow:none;backdrop-filter:none;-webkit-backdrop-filter:none;border-radius:0;padding:24px 40px}
.hdr--min .tel{margin-left:auto;display:flex;align-items:center;gap:8px;font-weight:600;font-size:16px;text-decoration:none;color:var(--ink);padding:10px 14px}
.hdr--min .tel svg{width:18px;height:18px;color:var(--cta)}
.bk{padding:104px 0 80px;background:var(--paper)}
.bk__grid{display:grid;grid-template-columns:minmax(0,.86fr) minmax(0,1.14fr);gap:56px;align-items:start}
.bk__side{display:flex;flex-direction:column;gap:18px;padding-top:10px}
.bk .ov{white-space:nowrap;letter-spacing:.14em}
.bk h1{display:flex;flex-direction:column;gap:12px}
.bk h1 .kicker{font:400 22px/1.3 var(--serif);color:var(--cta)}
.bk h1 .big{font-size:46px;line-height:1.1;color:var(--ink)}
.bk .body{font-size:18.5px;color:var(--muted);max-width:30em}
.ticks{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.ticks li{display:flex;gap:10px;font-size:17.5px}.ticks li svg{width:20px;height:20px;color:var(--cta);flex:none;margin-top:4px}
.whoami{display:flex;align-items:center;gap:14px;padding-top:16px;border-top:1px solid var(--line);font-size:16.5px;color:var(--muted)}
.ava{flex:none;width:52px;height:52px;border-radius:50%;background:var(--dove-soft);color:var(--dove);display:grid;place-items:center;overflow:hidden}
.ava svg{width:34px;height:34px;margin-top:10px}
.bk .proofline{font-size:15.5px}
.bk .proofline img{height:22px;width:auto}
.bkc{background:#fff;border-radius:var(--r);box-shadow:0 18px 50px rgba(42,38,34,.09);padding:10px 14px 6px;border:1px solid rgba(71,64,58,.08)}
.bkc__proof{display:flex;align-items:center;gap:10px;padding:10px 10px 12px;border-bottom:1px solid var(--line);font-size:15px;line-height:1.45;color:var(--muted)}
.bkc__proof img{height:30px;width:auto}
.pick{display:flex;flex-direction:column;gap:4px;padding-top:4px}
.pick b{font:600 17px/1.3 var(--sans);color:var(--ink)}
.pick span{font-size:16px;color:var(--muted)}
.calendly-inline-widget{min-width:320px;height:640px;position:relative}
.calendly-inline-widget iframe{border-radius:12px}
.cal-load{position:absolute;inset:0;display:grid;place-items:center;color:var(--muted);font-size:15px;pointer-events:none}
.bk__under{display:flex;flex-direction:column;gap:8px;padding:16px 8px 0;font-size:16px;color:var(--muted)}
.bk__under .row{display:flex;align-items:center;gap:10px}
.bk__under svg{width:17px;height:17px;color:var(--cta);flex:none}
.bk__under a{color:var(--ink);font-weight:600}
.bk__under .small{font-size:15px}
/* confirmation state (S08) */
.bk__pre{display:flex;flex-direction:column;gap:18px}
.done{display:none}
.booked .bk__pre{display:none}.booked .done{display:flex}
.done{flex-direction:column;gap:18px;padding-top:10px}
.done .okic{width:52px;height:52px;border-radius:50%;background:var(--cta);color:#fff;display:grid;place-items:center}.done .okic svg{width:26px;height:26px}
.done h2{font-size:46px}
.done .body{font-size:18.5px;color:var(--muted)}
.nsteps{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:14px;counter-reset:n}
.nsteps li{display:grid;grid-template-columns:40px 1fr;gap:14px;font-size:17px;color:var(--muted)}
.nsteps li::before{counter-increment:n;content:counter(n);width:40px;height:40px;border-radius:50%;border:2px solid var(--cta);color:var(--cta);font:400 18px/36px var(--serif);text-align:center}
.nsteps b{display:block;color:var(--ink)}
.nsteps a{color:var(--ink);font-weight:600}
.vidph{position:relative;aspect-ratio:16/9;border-radius:18px;overflow:hidden;background:#1f2a38;margin-top:10px;max-width:420px}
.vidph img{width:100%;height:100%;object-fit:cover;object-position:50% 18%;opacity:.55}
.vidph b{position:absolute;inset:0;margin:auto;width:62px;height:62px;border-radius:50%;background:rgba(255,255,255,.94);display:grid;place-items:center}
.vidph b svg{width:24px;height:24px;fill:var(--navy);margin-left:3px}
.vidph .fehlt{position:absolute;left:12px;bottom:12px;font-size:13px}
/* sections */
.talk2{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:44px}
.pcard{background:#fff;border-radius:var(--r);padding:30px;display:grid;grid-template-columns:210px 1fr;gap:28px;align-items:start}
.pcard .ph{width:210px;height:250px;border-radius:16px;overflow:hidden;background:var(--dove-soft);color:var(--dove);display:grid;place-items:center}
.pcard .ph svg{width:84px;height:84px;margin-top:40px}
.pcard .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 16%}
.pcard h3{font-size:23px;margin-bottom:10px}
.pcard p{font-size:17px;color:var(--muted)}
.pcard .fehlt{margin-top:8px}
.facts3{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.facts3 span{background:var(--cream);border-radius:999px;padding:6px 12px;font-size:15px;color:var(--ink)}
.pe{display:flex;align-items:center;gap:14px;margin-top:6px;font-size:17px;color:var(--muted)}.pe img{height:40px;width:auto}
.qgrid3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px}
.q3{background:#fff;border-radius:var(--r);padding:30px 28px;display:flex;flex-direction:column;gap:14px}
.q3 h3{font-size:21px}
.q3 blockquote{margin:0;font:italic 400 18px/1.55 var(--serif);color:var(--ink)}
.q3 .src{font-size:15px;color:var(--muted)}.q3 .src b{color:var(--ink);font-weight:600}
.prep{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:40px}
.pc{background:var(--paper);border-radius:var(--r);padding:28px 26px;display:flex;flex-direction:column;gap:10px}
.pc i{width:46px;height:46px;border-radius:50%;background:#fff;color:var(--cta);display:grid;place-items:center}.pc i svg{width:22px;height:22px}
.pc b{font:400 21px/1.3 var(--serif)}
.pc p{font-size:16.5px;color:var(--muted)}
.prep-note{margin-top:30px;max-width:52em;font-size:17.5px;color:var(--muted)}
.faq6{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,auto);grid-auto-flow:column;gap:34px 56px;margin-top:44px}
.faq6 h3{font-size:21px;margin-bottom:8px}
.faq6 p{font-size:17px;color:var(--muted)}
.faq6 a{color:var(--ink);font-weight:600}
.closer--plain{background:var(--navy);padding:96px 0 88px}
.closer--plain .closer__in{margin:0 auto;align-items:center;text-align:center;max-width:none}
.closer--plain .cta-row{align-items:center}
.closer--plain h2{font-size:44px}
.closer--plain::after{display:none}
.foot--min{padding:44px 0}
.foot--min .foot__in{grid-template-columns:1.2fr 1.6fr 1fr;align-items:center}
.foot--min .legal{display:flex;gap:32px}.foot--min .legal a{margin:0}
.foot--min .kon{border-left:1px solid rgba(242,237,228,.25);padding-left:28px}
.bkpage .sec{padding:96px 0}
.bkpage h2{font-size:40px}
.bkpage .center h2,.bkpage h2.center{text-align:center}
.bkpage .fstep .n{background:var(--cta);color:#fff;border-color:var(--cta);font-size:22px}
.bkpage .flow{margin-top:52px}
.bkpage .clarify{grid-template-columns:1fr;max-width:520px;padding:26px 34px;margin-top:44px}
.shot .proto{display:none}
.ctabar{display:flex;justify-content:center;margin-top:36px}
.prep .pc{flex-direction:row;align-items:flex-start;gap:18px;background:#fff}
.prep .pc i{flex:none;background:var(--cream)}
.faq6 h3 i{font-style:normal;color:var(--cta);margin-right:10px}
.sec .ctaline{margin-top:40px}
"""


def header():
    return f'''<header class="hdr hdr--min"><div class="hdr__in">
 <a class="hdr__logo" href="#top"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication" width="1794" height="647"></a>
 <a class="tel" href="{TEL}">{ICON['phone']}+49 15888367664</a>
</div></header>'''


def s01_s08():
    ticks = ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in ['30 Minuten per Video, von überall', 'kostenlos, danach entscheidest du in Ruhe', 'Bestätigung per E-Mail, Erinnerung per WhatsApp'])
    return f'''
<section class="bk" id="top">
 <div class="wrap bk__grid">
  <div class="bk__side">
   <div class="bk__pre">
    <p class="ov rv">Kostenloses Gespräch · 30 Minuten · per Video</p>
    <h1 class="rv"><span class="kicker">Gespräch buchen:</span><span class="big">Finde heraus, wo du gerade Wirkung verlierst.</span></h1>
    <p class="body rv">In 30 Minuten klären wir, wo du stehst und welches Seminar zu deiner Situation passt. Danach entscheidest du in Ruhe.</p>
    <ul class="ticks rv">{ticks}</ul>
    <div class="whoami rv"><span class="ava">{ICON['user']}</span><p>{t('Du sprichst mit einem Mitglied aus Michaels Team. [von Kunde bestätigen: Name und Rolle der Person im Gespräch]')}</p></div>
    <div class="pick rv"><b>Termin wählen</b><span>Wähle rechts einen freien Termin. Die Uhrzeiten zeigt der Kalender in deiner Zeitzone.</span></div>
   </div>
   <div class="done" aria-live="polite">
    <span class="okic">{ICON['ok']}</span>
    <h2>Dein Termin steht.</h2>
    <p class="body">Schön, dass du dabei bist. Datum und Uhrzeit siehst du rechts, die Bestätigung ist auf dem Weg in dein Postfach.</p>
    <ol class="nsteps">
     <li><p><b>Schau in dein Postfach.</b>{t('In der Bestätigungsmail stehen alle Details und der Link zum Umbuchen. [von Kunde bestätigen: Umbuchen-Link in der Bestätigungsmail]')} Keine Mail bekommen? Ruf an: <a href="{TEL}">+49 15888367664</a></p></li>
     <li><p><b>Antworte auf die WhatsApp.</b>{t('Kurz nach der Buchung meldet sich das Team mit einer Frage zu deiner Situation. Zwei Sätze als Antwort genügen. [von Kunde bestätigen: erste WhatsApp nach der Buchung eingerichtet]')}</p></li>
     <li><p><b>Schau dir die Nachricht von Michael an.</b>Er erzählt dir in rund einer Minute, worum es im Gespräch geht.</p>
      <div class="vidph"><img src="assets/michael-door.webp" alt="" width="1200" height="1800"><b>{PLAY}</b>{t('[von Kunde bestätigen: Video von Michael für die Bestätigung]')}</div></li>
    </ol>
    <p class="body">Am meisten hast du davon, wenn du eine konkrete Situation mitbringst.</p>
   </div>
  </div>
  <div class="bk__main rv" id="kalender">
   <div class="bkc">
    <p class="bkc__proof"><img src="assets/logo-provenexpert.png" alt="ProvenExpert" width="404" height="180">{STARS}<span>227 von 250 Bewertungen auf ProvenExpert mit 5 Sternen · seit 1990 Rhetoriktraining mit Michael Ehlers</span></p>
    <div class="calendly-inline-widget" data-base="{CAL}" data-opts="{CAL_OPTS}"><span class="cal-load">Kalender lädt …</span></div>
   </div>
   <div class="bk__under">
    <p class="row">{ICON['phone']}<span>Lieber anrufen? <a href="{TEL}">+49 15888367664</a></span></p>
    <p class="row">{CHECK}<span>Deine Handynummer brauchen wir für die Erinnerung per WhatsApp.</span></p>
    <p class="row small">{ICON['lock']}<span>Deine Angaben verarbeitet der Kalenderdienst Calendly. Mehr dazu in den <a href="https://www.meandyou.de/datenschutz">Datenschutzhinweisen</a>.</span></p>
   </div>
  </div>
 </div>
</section>'''


def s02():
    clar = ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in ['wo du heute Wirkung verlierst', 'welches Seminar zu deiner Situation passt', 'welcher Ort und welcher Termin für dich gehen'])
    return f'''
<section class="sec sec--cream" id="ablauf">
 <div class="wrap">
  <div class="center"><h2 class="rv">Erst ein Gespräch. Dann entscheidest du.</h2></div>
  <div class="flow" data-in>
   <div class="flow__line"><i></i></div>
   <div class="fstep rv"><span class="n">01</span><div class="fstep__t"><h3>Termin wählen.</h3><p>{t('Du suchst dir oben einen freien Termin aus und trägst deine Kontaktdaten ein. [von Kunde bestätigen: drei kurze Fragen im Formular eingerichtet] Danach bekommst du eine Bestätigung per E-Mail.')}</p></div></div>
   <div class="fstep rv"><span class="n">02</span><div class="fstep__t"><h3>Gespräch per Video.</h3><p>30 Minuten mit Michaels Team. Wir klären, wo du stehst und welches Format passt.</p></div></div>
   <div class="fstep rv"><span class="n">03</span><div class="fstep__t"><h3>In Ruhe entscheiden.</h3><p>Wenn ein Seminar passt, bekommst du Termine und alle Details. Ob und wann du buchst, entscheidest du danach.</p></div></div>
  </div>
  <div class="clarify rv"><div><p class="clar-h" style="margin:0;color:var(--ink)">Im Gespräch klärst du:</p><ul>{clar}</ul></div></div>
  <div class="ctabar rv">{btn()}</div>
 </div>
</section>'''


def s03():
    return f'''
<section class="sec" id="mit-wem">
 <div class="wrap">
  <h2 class="rv">Mit wem du sprichst</h2>
  <div class="talk2">
   <div class="pcard rv"><div class="ph">{ICON['user']}</div><div><h3>Dein Gesprächspartner</h3><p>{t('Ein Mitglied aus Michaels Team führt das Gespräch. [von Kunde bestätigen: Name und Rolle der Person im Gespräch] [von Kunde bestätigen: Foto der Person im Gespräch]')}</p></div></div>
   <div class="pcard rv"><div class="ph"><img src="assets/michael-door.webp" alt="Michael Ehlers lächelt, an einen Holzrahmen gelehnt" width="1200" height="1800"></div><div><h3>Der Kopf dahinter: Michael Ehlers</h3><p>Im Gespräch ist Michael nicht dabei. Er trainiert seit 1990 Menschen in Rhetorik und ist Lehrbeauftragter an der Universität St. Gallen. Das ERFOLG Magazin zählte ihn 2017 zu den Top 100 Trainern im deutschsprachigen Raum. Über 8.000 Menschen haben bei ihm trainiert.</p></div></div>
  </div>
 </div>
</section>'''


def s04():
    Q = [('Egal, auf welchem Level', '„Ich fand es spannend, dass wir Teilnehmer ein Mix von Anfänger bis Profi waren und Michael uns alle, egal auf welchem Level, weiterbringen konnte.“', 'Christin R.', 'ProvenExpert'),
         ('Reden vor der Gruppe', '„Besonders beeindruckt hat mich der Praxisteil, in dem wir freie Reden vor der Gruppe hielten und sowohl von Michael Ehlers als auch von den anderen Teilnehmern wertvolles Feedback bekamen.“', 'Michael B.', 'ProvenExpert'),
         ('Auch für Profis', '„Trotz 40 Jahren Medienerfahrung konnte ich erstaunlich viel vom Rhetoriktraining profitieren.“', 'Peter Escher', 'Moderator MDR')]
    q = ''.join(f'<article class="q3 rv">{STARS if s == "ProvenExpert" else ""}<h3>{e(h)}</h3><blockquote>{e(x)}</blockquote><p class="src"><b>{e(n)}</b>, {e(s)}</p></article>' for h, x, n, s in Q)
    return f'''
<section class="sec sec--cream" id="stimmen">
 <div class="wrap">
  <div class="stack" style="align-items:center"><h2 class="rv center">Was Teilnehmer nach dem Seminar schreiben</h2>
   <p class="pe rv"><img src="assets/logo-provenexpert.png" alt="ProvenExpert" width="404" height="180">{STARS}<span>227 von 250 Bewertungen auf ProvenExpert vergeben 5 Sterne.</span></p></div>
  <div class="qgrid3">{q}</div>
  <div class="ctabar rv">{btn()}</div>
 </div>
</section>'''


def s05():
    P = [('room', 'Ein ruhiger Ort.', '30 Minuten ohne Unterbrechung, Kamera an.'),
         ('sit', 'Eine konkrete Situation.', 'Zum Beispiel das Meeting, in dem du zuletzt nicht durchgedrungen bist.'),
         ('pen', 'Stift und Papier.', 'Du wirst dir etwas notieren wollen.')]
    c = ''.join(f'<div class="pc rv"><i>{ICON[k]}</i><div><b>{h}</b><p>{p}</p></div></div>' for k, h, p in P)
    return f'''
<section class="sec sec--cream" id="vorbereitung">
 <div class="wrap">
  <h2 class="rv center">So holst du das meiste aus den 30 Minuten</h2>
  <div class="prep">{c}</div>
  <p class="prep-note rv">{t('Vor dem Termin erinnert dich das Team per WhatsApp. 15 Minuten vorher kommt dort auch der Link zum Gespräch. Wenn du doch nicht kannst, findest du in deiner Bestätigungsmail einen Link, mit dem du umbuchst, statt den Termin verfallen zu lassen. [von Kunde bestätigen: Umbuchen-Link in der Bestätigungsmail]')}</p>
 </div>
</section>'''


FAQ = [
 ('Was kostet das Gespräch?', 'Nichts. Das Gespräch ist kostenlos.'),
 ('Muss ich danach ein Seminar buchen?', 'Nein. Wenn ein Seminar passt, bekommst du Termine und Details. Ob und wann du buchst, entscheidest du danach.'),
 ('Spreche ich mit Michael Ehlers?', 'Du sprichst mit einem Mitglied aus Michaels Team. Es klärt mit dir, ob und welches Format zu dir passt. [von Kunde bestätigen: Name und Rolle der Person im Gespräch]'),
 ('Wie läuft das Gespräch technisch?', 'Per Videocall am Laptop oder Handy. Den Link schickt dir das Team per WhatsApp, spätestens 15 Minuten vorher. [von Kunde bestätigen: Video-Tool des Gesprächs]'),
 ('Was, wenn mir etwas dazwischenkommt?', 'Buch einfach um. Den Link dafür findest du in deiner Bestätigungsmail. [von Kunde bestätigen: Umbuchen-Link in der Bestätigungsmail]'),
]


def s06():
    qa = ''.join(f'<div class="rv"><h3><i>{i}.</i>{e(q)}</h3><p>{t(a)}</p></div>' for i, (q, a) in enumerate(FAQ, 1))
    qa += f'<div class="rv"><h3><i>6.</i>Kann ich auch anrufen?</h3><p>Ja. Du erreichst das Team unter <a href="{TEL}">+49 15888367664</a>.</p></div>'
    return f'''
<section class="sec" id="fragen">
 <div class="wrap">
  <h2 class="rv center">Bevor du buchst: sechs kurze Antworten</h2>
  <div class="faq6">{qa}</div>
  <div class="ctabar rv">{btn()}</div>
 </div>
</section>'''


def s07():
    return f'''
<section class="closer closer--plain" id="abschluss">
 <div class="wrap"><div class="closer__in">
  <h2 class="rv">Unübersehbar wird man nicht, indem man lauter wird.</h2>
  <p class="rv">Ein Gespräch, 30 Minuten, kostenlos. Wir klären, wo du stehst und welches Format passt.</p>
  <div class="cta-row rv">{btn('btn btn--light cta--breathe')}<p class="tel">Lieber anrufen: <a href="{TEL}">+49 15888367664</a></p></div>
 </div></div>
</section>
<footer class="foot foot--min">
 <div class="wrap foot__in">
  <div><img src="assets/logo-light.png" alt="Michael Ehlers &amp; You Communication" width="1794" height="647"></div>
  <nav class="legal" aria-label="Rechtliches"><a href="https://www.meandyou.de/impressum">Impressum</a><a href="https://www.meandyou.de/datenschutz">Datenschutz</a><a href="https://www.meandyou.de/agb">AGB</a></nav>
  <div class="kon"><h4>Kontakt</h4><a href="{TEL}">+49 15888367664</a><a href="mailto:management@meandyou.de">management@meandyou.de</a></div>
 </div>
</footer>'''


BOOK_JS = r"""
(function(){
 var KEYS=['utm_source','utm_medium','utm_campaign','utm_content','utm_term'];
 var p=new URLSearchParams(location.search);
 var el=document.querySelector('.calendly-inline-widget');
 var q=el.getAttribute('data-opts');
 KEYS.forEach(function(k){var v=p.get(k); if(v){q+='&'+k+'='+encodeURIComponent(v);}});
 var url=el.getAttribute('data-base')+'?'+q;
 el.setAttribute('data-url',url); window.__calendlyUrl=url;
 var s=document.createElement('script'); s.src='https://assets.calendly.com/assets/external/widget.js'; s.async=true;
 s.onload=function(){var l=el.querySelector('.cal-load'); if(l) setTimeout(function(){l.remove();},1500);};
 document.body.appendChild(s);
 function booked(){document.documentElement.classList.add('booked'); scrollTo({top:0,behavior:'smooth'});}
 window.addEventListener('message',function(ev){
  if(ev.origin==='https://calendly.com' && ev.data && ev.data.event==='calendly.event_scheduled'){booked();}
 });
 if(p.get('booked')==='1'){document.documentElement.classList.add('booked');}
 document.querySelectorAll('[data-jump]').forEach(function(a){a.addEventListener('click',function(ev){ev.preventDefault();var k=document.getElementById('kalender');scrollTo({top:k.getBoundingClientRect().top+scrollY-96,behavior:'smooth'});});});
})();
"""


def schema():
    ORG = 'https://www.meandyou.de/#organization'
    g = [{"@type": "WebPage", "@id": "https://www.meandyou.de/gespraech-buchen#webpage", "url": "https://www.meandyou.de/gespraech-buchen", "name": "Kostenloses Gespräch buchen · me&you Michael Ehlers", "inLanguage": "de", "publisher": {"@id": ORG}},
         {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://www.meandyou.de/"}, {"@type": "ListItem", "position": 2, "name": "Gespräch buchen", "item": "https://www.meandyou.de/gespraech-buchen"}]},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Institut Michael Ehlers GmbH", "alternateName": "me&you Communication", "url": "https://www.meandyou.de/", "email": "management@meandyou.de",
          "contactPoint": {"@type": "ContactPoint", "telephone": "+49 15888367664", "contactType": "sales", "availableLanguage": "de"}}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


def page():
    body = header() + '<main>' + s01_s08() + s02() + s03() + s04() + s05() + s06() + '</main>' + s07() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Kostenloses Gespräch buchen · me&amp;you Michael Ehlers</title>
<meta name="description" content="Buch dir ein kostenloses Gespräch mit dem Team von Michael Ehlers. 30 Minuten per Video. Wir klären, wo du stehst und welches Seminar zu dir passt.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema()}</script>
</head><body class="bkpage">{body}<script>{home.JS}</script><script>{BOOK_JS}</script></body></html>'''


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
