"""Build the CRO prototype of the me&you page "Was ist Rhetorik" (desktop 1440 px). Text = 04-copy/approved-copy.md.
Design system = homepage + seminar + Michael page (imported). Main CTA = free video training (Copy Deck). Run: python3 build.py"""
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
TRAIN = 'https://www.meandyou.de/sichtbarkeit-neu?utm_source=rhetorik&utm_content='
BOOK = V2 + 'termin.html?utm_source=rhetorik&utm_content='
e, STARS, CHECK, PLAY, t = home.e, home.STARS, home.CHECK, home.PLAY, sem.t


def btn(utm, cls='btn'):
    return f'<a class="{cls}" href="{TRAIN}{utm}">Kostenloses Training ansehen</a>'


CSS = mic.CSS + r"""
/* rhetorik page additions */
.hero--split .hero__img{width:46%}
.hero--split .hero__img img{object-position:40% 25%}
.assure .play{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:var(--cta);flex:none}
.assure .play svg{width:10px;height:10px;fill:#fff;margin-left:1px}
.hero .skip{font-size:16px}
.ans{font:400 24px/1.5 var(--serif);color:var(--ink);max-width:34em}
.myths{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:44px}
.myth{background:#fff;border-radius:var(--r);padding:26px 24px;display:flex;flex-direction:column;gap:10px}
.myth s{font:600 14px/1.2 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);text-decoration-color:var(--dove)}
.myth h3{font-size:21px}.myth p{font-size:16.5px;color:var(--muted)}
.epl{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:44px}
.ep{background:#fff;border-radius:var(--r);padding:32px 30px;display:flex;flex-direction:column;gap:12px}
.ep b{font:400 40px/1 var(--serif);color:var(--cta)}
.ep h3{font-size:20px;font-family:var(--sans);font-weight:600}
.ep p{font-size:17px;color:var(--muted)}
.ep i{font:italic 400 17px/1.5 var(--serif);color:var(--ink)}
.steps5{display:grid;grid-template-columns:repeat(5,1fr);gap:22px;margin-top:52px;position:relative}
.steps5::before{content:"";position:absolute;left:0;right:0;top:27px;height:2px;background:var(--line)}
.s5{position:relative;display:flex;flex-direction:column;gap:10px}
.s5 .n{width:56px;height:56px;border-radius:50%;background:var(--cta);color:#fff;font:400 24px/56px var(--serif);text-align:center}
.s5 h3{font-size:22px}.s5 small{font:italic 400 16px/1 var(--serif);color:var(--cta)}
.s5 p{font-size:16.5px;color:var(--muted)}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.tile{background:var(--cream);border-radius:18px;padding:22px 24px;font-size:17px;color:var(--muted)}
.tile b{display:block;color:var(--ink);font-weight:600;margin-bottom:4px}
.errs{display:flex;flex-direction:column;margin-top:36px;border-top:1px solid var(--line)}
.err{display:grid;grid-template-columns:28px 1fr;gap:14px;padding:20px 0;border-bottom:1px solid var(--line);font-size:17px;color:var(--muted)}
.err::before{content:"";width:12px;height:12px;border-radius:50%;background:var(--sand);margin-top:8px}
.err b{color:var(--ink)}
.cols01{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:44px}
.cols01 div{border-top:1px solid rgba(242,237,228,.25);padding-top:18px}
.cols01 i{font:400 34px/1 var(--serif);color:var(--sand);font-style:normal}
.cols01 h3{color:#fff;font-size:24px;margin:10px 0 6px}
.cols01 p{color:rgba(242,237,228,.85);font-size:17px}
.pods{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:44px}
.pod2{background:#fff;border-radius:var(--r);padding:30px 28px;display:flex;flex-direction:column;gap:12px}
.pod2 .lab{display:flex;align-items:center;gap:8px;font:600 14px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--cta)}
.pod2 .lab svg{width:18px;height:18px}
.pod2 h3{font-size:22px}.pod2 p{font-size:16.5px;color:var(--muted)}
.learn{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start}
.ex{display:flex;flex-direction:column;gap:14px}
.exc{background:#fff;border-radius:18px;padding:22px 24px;display:grid;grid-template-columns:44px 1fr;gap:14px;font-size:17px;color:var(--muted)}
.exc i{font:400 30px/1 var(--serif);color:var(--cta);font-style:normal}
.exc b{display:block;color:var(--ink)}
.vsl{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center}
#training h2{font-size:38px}
.vsl__v{position:relative;border-radius:var(--r);overflow:hidden;aspect-ratio:16/9;display:block}
.vsl__v img{width:100%;height:100%;object-fit:cover}
.vsl__v b{position:absolute;inset:0;margin:auto;width:78px;height:78px;border-radius:50%;background:rgba(255,255,255,.94);display:grid;place-items:center}
.vsl__v b svg{width:30px;height:30px;fill:var(--navy);margin-left:4px}
.closer .links{color:rgba(255,255,255,.85);font-size:17px}.closer .links a{color:#fff}
"""


def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="{V2}index.html"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="{V2}seminare.html">Seminare</a><a href="{V2}michael.html">Michael</a><a href="#top" aria-current="page" style="color:var(--cta)">Was ist Rhetorik</a><a href="{V2}index.html#stimmen">Stimmen</a><a href="#faq">FAQ</a></nav>
 <a class="btn" href="{BOOK}header">Gespräch buchen</a>
</div></header>'''


def assure(txt):
    return f'<p class="assure"><span class="play">{PLAY}</span>{txt}</p>'


def s01():
    return f'''
<section class="hero hero--split" id="top">
 <div class="hero__img"><img data-plx src="assets/michael-cafe.webp" alt="Michael Ehlers im weißen Hemd an einem Tisch" width="1400" height="1982"></div>
 <div class="wrap hero__in"><div class="hero__txt">
  <p class="proofline rv">{STARS} 227 von 250 Bewertungen mit 5 Sternen auf ProvenExpert · über 8.000 Teilnehmer</p>
  <h1 class="rv"><span class="kicker">Was ist Rhetorik?</span><span class="big">Was Rhetorik wirklich ist<br>und was sie nicht ist.</span></h1>
  <p class="sub rv">Kein Verkaufstext. Eine Erklärung, für alle, die hier zum ersten Mal sind.</p>
  <p class="body rv">Rhetorik ist die Kunst der Rede. Hier erfährst du, woher sie kommt, wie sie wirkt und wie du sie lernst. Mit Beispielen von Michael Ehlers, der seit 1990 Menschen in Rhetorik trainiert.</p>
  <div class="cta-row rv">
   {btn('hero', 'btn cta--breathe')}
   {assure('Kostenlos, ein Video von Michael Ehlers. Ein persönliches Gespräch danach ist freiwillig.')}
   <a class="tlink skip" href="#was-ist-rhetorik">Direkt zur Erklärung</a>
  </div>
 </div></div>
</section>'''


def s02():
    facts = [('Seit 1990:', 'Michael Ehlers trainiert Menschen in Rhetorik'), ('Neun Bücher', 'als Autor oder Herausgeber'), ('St. Gallen:', 'Lehrbeauftragter an der Universität')]
    b = ''.join(f'<div class="badge"><b>{k}</b><span>{v}</span></div>' for k, v in facts)
    return f'''
<section class="proof" id="was-ist-rhetorik">
 <div class="wrap"><div class="proof__grid">
  <div class="stack rv"><h2>Was ist Rhetorik, einfach erklärt?</h2>
   <p class="ans">Rhetorik ist die Kunst der Rede. Das Wort kommt aus dem Altgriechischen und heißt übersetzt Redekunst. Schon Aristoteles beschrieb sie als Fähigkeit, bei jeder Sache das zu erkennen, was überzeugen kann. Heute meint Rhetorik alles, was dafür sorgt, dass deine Worte bei anderen ankommen: im Meeting, auf der Bühne und im Gespräch.</p></div>
  <div class="rv" data-in><div class="factgrid">{b}</div></div>
 </div></div>
</section>'''


def s03():
    M = [('Rhetorik ist kein Schauspiel.', 'Du lernst keine fremde Rolle und keine einstudierten Gesten. Gute Rhetorik passt zu deiner Person. Nicht anders werden, klarer werden.'),
         ('Rhetorik ist keine Frage der Lautstärke.', 'Wer am lautesten spricht, überzeugt nicht automatisch. Rhetorik bedeutet, Wirkung zu erzielen.'),
         ('Rhetorik ist kein Talent nur für Extrovertierte.', 'Introvertierte überzeugen oft durch Präzision und Ruhe. Mit den richtigen Techniken nutzt du diese Stärken, ohne dich zu verbiegen.'),
         ('Rhetorik ist keine Manipulation.', 'Manipulation will andere gegen ihr Interesse lenken. Rhetorik hilft dir, deine Sache klar und ehrlich zu vertreten. Wer die Muster kennt, erkennt auch Manipulation schneller.')]
    c = ''.join(f'<div class="myth rv"><h3>{h}</h3><p>{p}</p></div>' for h, p in M)
    return f'''
<section class="sec sec--cream" id="mythen">
 <div class="wrap">
  <div class="stack"><h2 class="rv">Was Rhetorik nicht ist</h2><p class="lead rv">Viele Menschen haben ein falsches Bild von Rhetorik. Vier Missverständnisse kommen besonders oft vor.</p></div>
  <div class="myths">{c}</div>
 </div>
</section>'''


def s04():
    E = [('Ethos', 'Ethos: Glaubwürdigkeit', 'Wie glaubwürdig der Redner wirkt. Oft zählt zuerst, wer spricht, und erst danach, was gesagt wird.', 'Ein Beispiel aus dem Alltag: Eine Kollegin hält Wort und kennt ihr Thema. Wenn sie etwas vorschlägt, hört das Team zu.'),
         ('Pathos', 'Pathos: Gefühl', 'Der emotionale Zustand der Zuhörer. Eine Rede wirkt, wenn sie Menschen berührt.', 'Ein Beispiel: Eine Geschichte von einem echten Kunden bleibt länger im Kopf als jede Tabelle.'),
         ('Logos', 'Logos: Argument', 'Das Argument selbst, also Fakten und Gründe.', 'Ein Beispiel: Du zeigst drei Zahlen, die deinen Vorschlag stützen, und erklärst, was daraus folgt.')]
    c = ''.join(f'<div class="ep rv"><b aria-hidden="true">{g}</b><h3>{h}</h3><p>{p}</p><i>{x}</i></div>' for g, h, p, x in E)
    return f'''
<section class="sec" id="ethos-pathos-logos">
 <div class="wrap">
  <div class="stack"><h2 class="rv">Ethos, Pathos, Logos: Die drei Mittel der Überzeugung</h2><p class="lead rv">Aristoteles unterschied drei Formen der Überzeugung. Sie gelten bis heute als Grundlage der Rhetorik.</p></div>
  <div class="epl">{c}</div>
  <p class="lead rv" style="margin-top:32px">Gute Rhetorik braucht alle drei. Ein starkes Argument ohne Glaubwürdigkeit verpufft. Gefühl ohne Argument wirkt schnell wie Show.</p>
  <div class="cta-row rv" style="margin-top:26px">{btn('ethos')}</div>
 </div>
</section>'''


def s05():
    S = [('Finden', 'inventio', 'Du sammelst Gedanken und Argumente. Was willst du sagen, und was braucht dein Publikum? Hier entscheidest du auch, welches Beispiel deinen Punkt am besten zeigt.'),
         ('Ordnen', 'dispositio', 'Du baust eine Struktur: Einstieg, Hauptteil, Schluss. So können andere dir folgen. Der Einstieg holt die Aufmerksamkeit, der Schluss sagt, was bleiben soll.'),
         ('Formulieren', 'elocutio', 'Du suchst die passenden Worte und Bilder. Kurze Sätze, klare Begriffe.'),
         ('Einprägen', 'memoria', 'Du merkst dir die Rede so, dass du frei sprechen kannst. Ein paar Stichworte reichen, wenn die Struktur steht.'),
         ('Vortragen', 'actio', 'Stimme, Blick, Haltung und Pausen. Hier entscheidet sich, was im Raum ankommt.')]
    c = ''.join(f'<div class="s5 rv"><span class="n">{i}</span><h3>{h}</h3><small>({l})</small><p>{p}</p></div>' for i, (h, l, p) in enumerate(S, 1))
    return f'''
<section class="sec sec--cream" id="fuenf-schritte">
 <div class="wrap">
  <div class="stack"><h2 class="rv">Die fünf Schritte einer Rede</h2><p class="lead rv">Die klassische Rhetorik beschreibt fünf Schritte von der Idee bis zum Vortrag. Mit den fünf Säulen der Rhetorik sind oft diese fünf Schritte gemeint. Eine feste Einteilung gibt es nicht.</p></div>
  <div class="steps5">{c}</div>
  <p class="vcap rv" style="margin-top:36px">Von Michael Ehlers stammt das Buch „Die 5 Säulen der positiven Kommunikation“.</p>
 </div>
</section>'''


def s06():
    T = [('Präsentationen und Pitches:', 'Du stellst eine Idee vor und willst, dass sie hängen bleibt.'), ('Meetings:', 'Du bringst deinen Punkt durch, auch wenn andere schneller reden.'),
         ('Verhandlungen:', 'Du bleibst ruhig und klar, wenn Druck kommt.'), ('Führung:', 'Du gibst Kritik so, dass sie ankommt und motiviert.'),
         ('Schwierige Gespräche:', 'Du findest Worte, auch wenn es unangenehm wird.'), ('Small Talk und Netzwerken:', 'Du kommst leichter ins Gespräch und bleibst in Erinnerung.')]
    c = ''.join(f'<div class="tile rv"><b>{h}</b>{p}</div>' for h, p in T)
    return f'''
<section class="sec" id="beruf">
 <div class="wrap">
  <div class="stack"><h2 class="rv">Wo es im Beruf auf Rhetorik ankommt</h2><p class="lead rv">Rhetorik ist kein Thema nur für Redner auf großen Bühnen. Sie steckt in vielen Momenten, die du jede Woche erlebst.</p></div>
  <div class="tiles">{c}</div>
  <p class="lead rv" style="margin-top:32px;max-width:48em">Die Bedeutung von Rhetorik wächst mit deiner Verantwortung. Je mehr Menschen dir zuhören, desto mehr zählt jedes Wort. Das gilt für die Teamleiterin im Montagsmeeting genauso wie für den Gründer vor Investoren. Wer fachlich gut ist, hat oft viel zu sagen. Rhetorik sorgt dafür, dass es auch gehört wird.</p>
 </div>
</section>'''


def s07():
    F = [('Zu viel auf einmal.', 'Wer alles sagen will, sagt am Ende nichts. Besser: ein Kerngedanke pro Rede, dazu ein Beispiel.'),
         ('Verneinungen.', 'Ein Satz wie „Das ist kein Problem“ lässt das Wort Problem im Kopf. Besser: Sag, was ist, statt was nicht ist.'),
         ('Keine Pausen.', 'Viele Redner füllen jede Sekunde. Eine Pause gibt deinen Worten Gewicht und dir Zeit zum Denken.'),
         ('Ablesen statt sprechen.', 'Wer abliest, verliert den Kontakt zum Publikum. Besser: Stichworte statt ganzer Sätze.'),
         ('Ein fremder Stil.', 'Wer eine Rolle spielt, wirkt unecht. Besser: Arbeite mit deiner eigenen Art und mach sie klarer.')]
    c = ''.join(f'<div class="err rv"><p><b>{h}</b> {e(p)}</p></div>' for h, p in F)
    return f'''
<section class="sec sec--cream" id="fehler">
 <div class="wrap"><h2 class="rv">Typische Fehler und wie du sie vermeidest</h2><div class="errs">{c}</div></div>
</section>'''


def s08():
    C = [('01', 'Persönlichkeit.', 'Wer du bist, bevor du sprichst.'), ('02', 'Kongruenz.', 'Wenn Haltung und Worte dasselbe sagen.'), ('03', 'Wirkung.', 'Was davon im Raum ankommt.')]
    c = ''.join(f'<div class="rv"><i>{n}</i><h3>{h}</h3><p>{p}</p></div>' for n, h, p in C)
    return f'''
<section class="sec sec--navy" id="methode">
 <div class="wrap">
  <h2 class="rv" style="color:#fff">Wirkung beginnt nicht bei der Technik.</h2>
  <p class="lead rv" style="color:rgba(242,237,228,.85);margin-top:20px">Die meisten Rhetoriktrainings starten bei Werkzeugen. Michael Ehlers startet davor: bei Persönlichkeit, Selbstbild, Mustern und innerer Stabilität. Erst wenn das steht, tragen die Werkzeuge.</p>
  <p class="trio-h rv" style="color:var(--sand);margin-top:36px">Persönlichkeit. Kongruenz. Wirkung.</p>
  <div class="cols01" style="margin-top:14px">{c}</div>
  <p class="lead rv" style="color:rgba(242,237,228,.85);margin-top:36px;max-width:48em">{t('In den Seminaren schaut Michael genau hin [von Kunde bestätigen: Leitet Michael die Seminare selbst], wie eine Aussage im Raum ankommt. Und was von ihr bleibt, wenn jemand widerspricht. Seine Rückmeldung ist direkt. Du arbeitest mit dem, was du schon mitbringst.')} <a class="tlink" style="color:#fff" href="{V2}michael.html">Mehr über Michael</a></p>
  <div class="cta-row rv" style="margin-top:30px">{btn('methode', 'btn btn--light')}</div>
 </div>
</section>'''


def s09():
    P = [('Sag nie, was du nicht bist', '1973 sagte Richard Nixon mitten in der Watergate-Affäre: „I am not a crook.“ Hängen blieb ein Wort: crook, also Gauner. Michael erklärt das so: Unser Gehirn macht aus Verneinungen Bilder. Darum wird ein Vorwurf, den du bestreitest, oft stärker. Besser ist ein Satz, der sagt, was du bist.'),
         ('Wer den Rahmen setzt, gewinnt', '„Steuerlast“ und „Steuerbeitrag“ meinen dasselbe Geld. Trotzdem wirken die Wörter ganz verschieden. Das nennt man Framing. Michaels Rat: Ein Dementi verstärkt oft den fremden Rahmen. Setze lieber deinen eigenen Rahmen, statt am fremden zu reparieren.'),
         ('Kommunikation ist ein Raum', 'So sagt es Michael in seinem Podcast: Wer den Raum nicht selbst bespielt, überlässt ihn anderen. Das gilt im Meeting genauso wie in der Öffentlichkeit. Auch dein Schweigen wird gelesen. Wenn du nichts sagst, füllen andere die Lücke mit ihrer Version.')]
    c = ''.join(f'<div class="pod2 rv"><span class="lab">{mic.ICON_MIC}Podcast</span><h3>{h}</h3><p>{e(p)}</p></div>' for h, p in P)
    return f'''
<section class="sec" id="beispiele">
 <div class="wrap">
  <div class="stack"><h2 class="rv">Drei Beispiele aus dem Alltag</h2><p class="lead rv">In seinem Podcast „Unübersehbar“ zeigt Michael Ehlers an echten Fällen und Gedanken, wie Rhetorik wirkt. Drei Beispiele daraus.</p></div>
  <div class="pods">{c}</div>
 </div>
</section>'''


def s10():
    X = [('Zwei Minuten, ein Gedanke.', 'Nimm ein Thema aus deinem Alltag und sprich zwei Minuten frei darüber. Ein Gedanke, ein Beispiel, ein Satz zum Schluss.'),
         ('Sieh dich selbst.', 'Nimm dich mit dem Handy auf und schau dir die Aufnahme an. Achte zuerst auf Pausen und Blick, dann auf die Worte.'),
         ('Frag nach Rückmeldung.', 'Bitte eine Person, der du vertraust, um ein ehrliches Feedback. Was kam an? Was blieb hängen?')]
    c = ''.join(f'<div class="exc rv"><i>{i}</i><p><b>{h}</b>{p}</p></div>' for i, (h, p) in enumerate(X, 1))
    return f'''
<section class="sec sec--cream" id="lernen">
 <div class="wrap learn">
  <div class="stack">
   <h2 class="rv">Wie lernt man Rhetorik?</h2>
   <p class="lead rv">Durch Üben mit ehrlichem Feedback. Bücher geben dir das Wissen. Unter Druck hilft dir aber nur, was du geübt hast. Rhetorik ist ein Handwerk. Wer regelmäßig übt, wird sicherer.</p>
   <p class="lead rv">Im Seminar übst du genau so, nur intensiver: drei Tage in einer kleinen Gruppe von höchstens 14 Menschen, dazu ein Tag Get Together. Du hältst Reden vor der Gruppe und wirst dreimal auf Video aufgenommen. Die Auswertung kommt sofort. Im VR-Training sprichst du vor einem virtuellen Publikum. Mehr dazu auf der Seite <a class="tlink" href="{V2}seminare.html">Seminare</a>.</p>
   <div class="cta-row rv">{btn('lernen')}</div>
  </div>
  <div class="ex"><p class="trio-h rv">Drei Übungen, die du heute beginnen kannst:</p>{c}</div>
 </div>
</section>'''


def s11():
    return f'''
<section class="sec" id="training">
 <div class="wrap vsl">
  <a class="vsl__v rv" href="{TRAIN}video"><img src="assets/vsl-poster.webp" alt="Standbild aus dem kostenlosen Video: Michael Ehlers im Studio" width="1920" height="1080"><b>{PLAY}</b></a>
  <div class="stack">
   <h2 class="rv">Das kostenlose Training von Michael Ehlers</h2>
   <p class="lead rv">{t('Nicht mehr überhört, sondern unübersehbar. In einem kostenlosen Video zeigt Michael Ehlers, wie du Aufmerksamkeit und Vertrauen gewinnst, ohne laut zu werden oder dich zu verbiegen [von Kunde bestätigen: Inhalt und Länge des Trainings]. In seine Arbeit fließen über 30 Jahre Erfahrung mit Executives, Unternehmern, Politikern und Profisportlern.')}</p>
   <p class="lead rv">Das Video ist für alle, die gehört werden wollen, ohne sich zu verstellen. Nach dem Video kannst du ein kostenloses persönliches Gespräch buchen. Das ist freiwillig.</p>
   <div class="cta-row rv">{btn('training')}</div>
  </div>
 </div>
</section>'''


FAQ = [
 ('Woher kommt das Wort?', 'Aus dem Altgriechischen. Übersetzt heißt es Redekunst. Gemeint ist alles, was dafür sorgt, dass das, was du sagst, bei anderen so ankommt, wie du es meinst.'),
 ('Was sind die drei Säulen der Rhetorik?', 'Ethos, Pathos und Logos. Ethos ist die Glaubwürdigkeit des Redners, Pathos das Gefühl der Zuhörer, Logos das Argument. Die Einteilung stammt von Aristoteles.'),
 ('Was sind die fünf Säulen der Rhetorik?', 'Oft sind die fünf Schritte einer Rede gemeint. Eine feste Einteilung gibt es nicht. Die Schritte heißen Finden, Ordnen, Formulieren, Einprägen und Vortragen. Auf Latein heißen sie inventio, dispositio, elocutio, memoria und actio.'),
 ('Kann jeder gut reden lernen?', 'Rhetorik ist ein Handwerk, das man üben kann. Mit Übung und ehrlichem Feedback wirst du in der Regel sicherer. Die Grundlage ist deine eigene Persönlichkeit, nicht eine fremde Technik.'),
 ('Welche Übungen helfen beim Training?', 'Kurze freie Reden von zwei Minuten, Aufnahmen von dir selbst und ehrliche Rückmeldung von anderen. Im Seminar kommt das VR-Training vor einem virtuellen Publikum dazu.'),
 ('Ist Überzeugen dasselbe wie Manipulieren?', 'Nein. Rhetorik hilft dir, deine Sache klar zu vertreten. Wer rhetorische Muster kennt, erkennt Manipulation sogar schneller.'),
 ('Bin ich zu introvertiert dafür?', 'Nein. Rhetorik bedeutet nicht, lauter oder extrovertierter zu sein. Introvertierte überzeugen oft durch Präzision und Ruhe.'),
 ('Was ist ein Stilmittel?', 'Ein sprachliches Mittel, das eine Aussage stärker macht. Bekannte Beispiele sind die Metapher, die Wiederholung und die rhetorische Frage. Sie wirken am besten sparsam und passend zur Person.'),
 ('Was ist der Unterschied zwischen Rhetorik und Kommunikation?', 'Kommunikation ist jeder Austausch zwischen Menschen. Rhetorik ist der Teil davon, der dafür sorgt, dass deine Botschaft ankommt und überzeugt.'),
 ('Wie lange dauert es, bis ich sicherer werde?', 'Das hängt davon ab, wo du stehst und wie viel du übst. Die erste Videoaufnahme zeigt dir, wie du auf andere wirkst. Ein Seminar von drei Tagen gibt dir eine feste Grundlage.'),
]


def s12():
    items = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div class="a">{e(a)}</div></details>' for i, (q, a) in enumerate(FAQ))
    return f'''
<section class="sec" id="faq">
 <div class="wrap faqgrid">
  <div class="stack" style="position:sticky;top:120px"><p class="ov rv">FAQ</p><h2 class="rv">Häufige Fragen zur Rhetorik</h2>
   <p class="morelinks rv">Weitere Antworten findest du in den <a class="tlink" href="{V2}faq.html">häufigen Fragen</a>.</p></div>
  <div class="acc rv">{items}</div>
 </div>
</section>'''


def s13():
    li = ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in ['kostenlos', 'von Michael Ehlers, seit 1990 Rhetoriktrainer', 'danach auf Wunsch ein persönliches Gespräch'])
    foot = home.section_closer().split('<footer', 1)[1]
    foot = '<footer' + foot.replace(home.BOOK, BOOK).replace('href="#termine"', f'href="{V2}seminare.html#termine"').replace(f'href="{V2}rhetorik.html">Was ist Rhetorik', 'href="#top">Was ist Rhetorik')
    return f'''
<section class="closer" id="abschluss">
 <div class="closer__bg"><img data-plx src="assets/closer-terrace.webp" alt="Abendstimmung auf einer Steinterrasse über dem Meer, Menschen im Gespräch" width="1536" height="1024"></div>
 <div class="wrap"><div class="closer__in">
  <h2 class="rv">Fang mit einem Video an.</h2>
  <p class="rv">Rhetorik ist die Kunst, mit Worten zu wirken. Sie beginnt bei deiner Persönlichkeit und wird durch Übung sicherer. Die Begriffe kennst du jetzt. Der nächste Schritt ist, sie auszuprobieren. Du musst nichts buchen und dich zu nichts verpflichten. Schau dir das kostenlose Training an und entscheide danach, ob du weitermachen willst.</p>
  <ul class="rv">{li}</ul>
  <div class="cta-row rv">{btn('abschluss', 'btn btn--light cta--breathe')}</div>
  <p class="links rv">Lieber direkt sprechen? <a href="{BOOK}abschluss-textlink">Gespräch buchen</a>. Mehr über den Trainer: <a href="{V2}michael.html">Mehr über Michael</a>. Zurück zur <a href="{V2}index.html">Startseite</a></p>
 </div></div>
</section>
{foot}'''


def schema():
    ORG = 'https://www.meandyou.de/#organization'
    g = [{"@type": "WebPage", "@id": "https://www.meandyou.de/rhetorik#webpage", "url": "https://www.meandyou.de/rhetorik", "name": "Was ist Rhetorik? Einfach erklärt mit Beispielen", "inLanguage": "de"},
         {"@type": "Article", "headline": "Was ist Rhetorik? Was Rhetorik wirklich ist und was sie nicht ist.", "inLanguage": "de", "mainEntityOfPage": {"@id": "https://www.meandyou.de/rhetorik#webpage"},
          "author": {"@type": "Person", "@id": "https://www.meandyou.de/michael#person", "name": "Michael Ehlers", "url": "https://www.meandyou.de/michael"}, "publisher": {"@id": ORG},
          "about": [{"@type": "Thing", "name": "Rhetorik", "sameAs": "https://de.wikipedia.org/wiki/Rhetorik"}]},
         {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://www.meandyou.de/"}, {"@type": "ListItem", "position": 2, "name": "Was ist Rhetorik", "item": "https://www.meandyou.de/rhetorik"}]},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Institut Michael Ehlers GmbH", "alternateName": "me&you Communication", "url": "https://www.meandyou.de/"}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


def page():
    body = header() + '<main>' + s01() + s02() + s03() + s04() + s05() + s06() + s07() + s08() + s09() + s10() + s11() + s12() + '</main>' + s13() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Was ist Rhetorik? Einfach erklärt mit Beispielen</title>
<meta name="description" content="Was ist Rhetorik? Die Kunst der Rede einfach erklärt: Ethos, Pathos, Logos, die fünf Schritte einer Rede und Übungen. Mit kostenlosem Video-Training.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema()}</script>
</head><body>{body}<script>{home.JS}</script></body></html>'''


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
