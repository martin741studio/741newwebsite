"""Daniela Dumann: new approval cards (DRAFT) E8+ for table approval_items. E1-E7 already exist as drafts (Freigabe chat, 13.10.).
Run: python3 cards_dumann.py  -> writes cards.json, approval-drafts-dumann.sql, approval-cards-draft.md (nothing is sent to the database).
Facts: live crawl 13.10.2026 (data/live-crawl-2026-10-13.json), Search Console pull 13.10. (data/gsc.json), 00_project/dumann-seo-arbeitsplan-2026-10.md."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
LIVE = json.load(open(os.path.join(HERE, 'data/live-crawl-2026-10-13.json'), encoding='utf-8'))
CLIENT = 'd01f4236-8674-45fe-a347-0751fa7b24de'
SRC = 'Google-Suchdaten (90 Tage bis 11.10.) und Abgleich deiner Website'
SEP = '\n'

def clean(s): return re.sub(r'\s+', ' ', (s or '').replace('\xa0', ' ')).strip()
def before(page):
    p = LIVE[page]
    return SEP.join([f'Google-Titel: {clean(p["title"])}', f'Google-Text: {clean(p["desc"])}', f'Überschrift: {clean(" ".join(p["h1"]))}'])
def pack(title, desc, h1=None, extra=None):
    parts = [f'Google-Titel: {title}', f'Google-Text: {desc}']
    if h1: parts.append(f'Überschrift: {h1}')
    if extra: parts.append(extra)
    return SEP.join(parts)

CARDS = []
def card(**k):
    k.setdefault('kind', 'text'); k.setdefault('type_label', 'Text'); k.setdefault('area', 'website')
    k.setdefault('why_source', SRC); k.setdefault('why_date', '2026-10-13'); k.setdefault('seo_lock', False)
    k.setdefault('keyword', None); k.setdefault('lock_note', None); k.setdefault('note', None); k.setdefault('guide_text', None)
    k.setdefault('risk_class', 'none'); k.setdefault('before_value', None); k.setdefault('context', {})
    CARDS.append(k)

NAMENS_HINWEIS = 'Der Name am Ende des Google-Titels folgt deiner Wahl in der Karte „Der Name hinter jedem Seitentitel bei Google“.'
KEEP = lambda what='Alles': {'key': 'C', 'value': f'{what} bleibt unverändert', 'label': 'nichts ändert sich'}

# ---------------- Wave 1: Seiten mit den größten Hebeln ----------------
card(code='E8', title='Seite „Behandlungen“: Auftritt bei Google und Überschrift', wave=1,
     why='Die Seite steht im Schnitt auf **Platz 2,7** und bekam in 90 Tagen **13 Klicks bei 305 Anzeigen**. Der Google-Titel endet auf den fremden Namen „hildegardbingen“.',
     before_value=before('behandlungen'),
     variants=[
       {'key': 'A', 'label': 'nennt den Ort, deine Leistungen und die Preise', 'value': pack('Behandlungen & Preise | Naturheilpraxis Daniela Dumann', 'Behandlungen nach Hildegard von Bingen in Berlin-Charlottenburg: Aderlass, Ernährung, Homöopathie, Massagen. Preise & Ablauf im Überblick.', 'Behandlungen in Berlin-Charlottenburg: Heilkunde nach Hildegard von Bingen')},
       {'key': 'B', 'label': 'Hildegard von Bingen steht in der Überschrift vorn', 'value': pack('Behandlungen in Berlin-Charlottenburg | Naturheilpraxis Daniela Dumann', 'Behandlungen nach Hildegard von Bingen in Berlin-Charlottenburg: Aderlass, Ernährung, Homöopathie, Massagen. Preise & Ablauf im Überblick.', 'Behandlungen nach Hildegard von Bingen in Berlin-Charlottenburg')},
       KEEP()],
     recommended_key='A', keyword='Behandlungen', seo_lock=True,
     lock_note='„Behandlungen“ und „Berlin-Charlottenburg“ bleiben in Titel und Überschrift, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/behandlungen'}, note=NAMENS_HINWEIS,
     guide_text='Hier entscheidest du nur den Wortlaut. Die Suchbegriffe bleiben, damit die Seite gefunden wird.')

card(code='E9', title='Seite „Behandlungen“: drei Formulierungen zu Salbe, Test und Beschwerden', wave=1, risk_class='health',
     why='Auf der Seite stehen **drei Stellen, die Heilwirkung oder eine Krebs-Vorstufe nennen**: die Amethystsalbe bei Neurodermitis, der „Präkanzerose Test“ und eine Liste mit Magen-Darm-Erkrankungen.',
     why_source='Abgleich deiner Website', before_value='Amethystsalbe: „… die bei Neurodermitis und auch bei Warzen und Altersflecken hervorragende Dienste leistet.“\nTest: „Präkanzerose Test (Untersuchung auf Vorstufen einer Krebserkrankung)“\nListe: „… meine Schwerpunkte bei der Behandlung von Magen-Darm-Erkrankungen (chronische) Durchfälle, (chronische) Verstopfung, Blähungen …“',
     variants=[
       {'key': 'A', 'label': 'die Angebote bleiben, die Aussagen werden neutral', 'value': 'Amethystsalbe: „Eine Salbe mit Amethyst, die ich in meiner Praxis entwickelt habe. Sie kann unterstützend angewendet werden.“\nTest: „Urintest (Morgenurin), 48 €“\nListe: „Themenfelder, bei denen ich Sie begleite: Verdauung, Bauchbeschwerden und Nahrungsmittelunverträglichkeiten.“'},
       {'key': 'B', 'label': 'die drei Stellen verschwinden von der Seite', 'value': 'Die drei Absätze entfallen. Die Preisliste und alle anderen Angebote bleiben.'}],
     recommended_key='A', context={'page': '/behandlungen'},
     note='Der neue Wortlaut wird vor dem Einbau noch einmal auf das Heilmittelwerbegesetz geprüft. Wie der Test künftig heißen soll, kannst du im Kommentarfeld schreiben.',
     guide_text='Hier brauche ich dein Ja. Solche Sätze können für Heilpraktikerinnen unangenehm werden, deshalb schlage ich neutrale Formulierungen vor.')

card(code='E10', title='Seite „Ernährungsberatung“: Auftritt bei Google und Überschrift', wave=1, risk_class='health',
     why='**„ernährungsberatung berlin“ wird 1.600-mal im Monat gesucht.** Der Google-Text nennt Berlin nicht und beginnt mit der Zahl „80 % aller Erkrankungen“, die ich aus der Seite nehmen möchte.',
     why_source='Google-Suchdaten und Abgleich deiner Website', before_value=before('ernährungsberatung'),
     variants=[
       {'key': 'A', 'label': 'nennt Berlin-Charlottenburg und den Preis des Erstgesprächs', 'value': pack('Ernährungsberatung Berlin-Charlottenburg | Daniela Dumann', 'Ernährungsberatung nach Hildegard von Bingen in Berlin-Charlottenburg. Erstanamnese 220 €, persönlicher Plan bei Unverträglichkeiten. Termin: 030 36430358.', 'Ernährungsberatung in Berlin-Charlottenburg nach Hildegard von Bingen')},
       {'key': 'B', 'label': 'ohne Preis im Google-Text', 'value': pack('Ernährungsberatung Berlin-Charlottenburg | Daniela Dumann', 'Ernährungsberatung nach Hildegard von Bingen in Berlin-Charlottenburg. Persönlicher Plan, auch bei Unverträglichkeiten. Termin: 030 36430358.', 'Ernährungsberatung in Berlin-Charlottenburg nach Hildegard von Bingen')},
       KEEP()],
     recommended_key='A', keyword='Ernährungsberatung', seo_lock=True,
     lock_note='„Ernährungsberatung“ und „Berlin-Charlottenburg“ bleiben, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/ernährungsberatung'}, note=NAMENS_HINWEIS + ' Der alte Google-Text enthält die Zahl „80 %“. Bleibt sie stehen, ist das ein Risiko, siehe Karte E1.',
     guide_text='Wenn der Google-Text die Zahl behält, steht sie weiter in jeder Suche. Deshalb empfehle ich Variante A oder B.')

card(code='E11', kind='price', type_label='Preise', title='Kosten auf der Seite „Ernährungsberatung“ zeigen?', wave=1, risk_class='price',
     why='Die meistgestellten Fragen bei Google zu diesem Thema drehen sich um **Kosten und Krankenkasse**. Deine Preise stehen heute nur auf der Seite „Behandlungen“.',
     why_source='Google-Suchdaten (Fragen zu deinem Thema)', why_date='2026-09-13',
     variants=[
       {'key': 'A', 'label': 'Preisbox mit deinen Angaben von der Seite „Behandlungen“, mit deiner Formulierung zur Gebührenordnung', 'value': 'Erstanamnese (60 Minuten): 220 €. Folgetermine: 150 € je angefangene Stunde, nach der an die Teuerung angepassten Gebührenordnung für Heilpraktiker (GebüH).'},
       {'key': 'B', 'label': 'keine Preise auf dieser Seite', 'value': 'Auf der Seite steht ein Hinweis auf „Behandlungen“ mit den Preisen.'}],
     recommended_key='A', note='Die Formulierung zur Gebührenordnung stammt aus deinem Kommentar vom 17.09. Ich übernehme nur Preise, die du bestätigst.',
     context={'page': '/ernährungsberatung'}, guide_text='Ich brauche dein Ja zu den Preisen und zur Formulierung. Danach setze ich sie ein.')

card(code='E12', title='Seite „Darmsanierung“: Auftritt bei Google und Überschrift', wave=2, risk_class='health',
     why='**„darmsanierung hildegard von bingen“ wird 210-mal im Monat gesucht.** Deine Seite bekam in 90 Tagen 377 Anzeigen und 4 Klicks, im Schnitt auf Platz 16.',
     before_value=before('darmsanierung'),
     variants=[
       {'key': 'A', 'label': 'nennt Hildegard von Bingen, den Ort und den Ablauf', 'value': pack('Darmsanierung nach Hildegard von Bingen in Berlin | Daniela Dumann', 'Darmsanierung nach Hildegard von Bingen in Berlin-Charlottenburg: Ablauf, Dinkel-Ernährung und sanfte Begleitung durch Heilpraktikerin Daniela Dumann.', 'Darmsanierung nach Hildegard von Bingen in Berlin')},
       KEEP()],
     recommended_key='A', keyword='Darmsanierung', seo_lock=True, lock_note='„Darmsanierung“ bleibt, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/darmsanierung'}, note=NAMENS_HINWEIS + ' Der alte Google-Text zitiert „Der Tod sitzt im Darm“.',
     guide_text='Auf dieser Seite fehlt oft nur ein klarer Titel, um auf Seite 1 zu kommen.')

card(code='E13', title='Seite „Kräuterheilkunde“: Auftritt bei Google und Überschrift', wave=2, risk_class='health',
     why='**„hildegard von bingen kräuter“ wird 320-mal im Monat gesucht.** Deine Seite steht im Schnitt auf Platz 49 und bekam in 90 Tagen nur 1 Klick. Der Google-Text beginnt mit einer Aufzählung von Heilmitteln gegen bestimmte Beschwerden.',
     before_value=before('kräuterheilkunde'),
     variants=[
       {'key': 'A', 'label': 'nennt die Kräuter statt der Heilmittel-Zahlen', 'value': pack('Kräuterheilkunde nach Hildegard von Bingen in Berlin', 'Kräuterheilkunde nach Hildegard von Bingen in Berlin-Charlottenburg: Galgant, Bertram, Quendel und überlieferte Rezepturen. Praxis und Kräutersalon.', 'Kräuterheilkunde nach Hildegard von Bingen')},
       KEEP()],
     recommended_key='A', keyword='Kräuterheilkunde', seo_lock=True, lock_note='„Kräuterheilkunde“ bleibt, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/kräuterheilkunde'}, note='Die Aufzählung „Herzmittel, Rheumamittel, Hautmittel“ steht auch im Text der Seite. Sie wird vor dem Einbau auf das Heilmittelwerbegesetz geprüft.',
     guide_text='Zahlen zu Heilmitteln für bestimmte Krankheiten sind riskant, weil sie wie ein Heilversprechen wirken. Die Kräuter selbst sind sicher.')

card(code='E14', title='Seite „Aderlass-Therapie“: Auftritt bei Google und eine Aussage zur Wirkung', wave=2, risk_class='health',
     why='Der Google-Text und die Seite nennen den Aderlass „das wichtigste Mittel zur Behandlung aller chronischen Erkrankungen“. Das ist eine **Heilaussage ohne Beleg**.',
     why_source='Abgleich deiner Website', before_value=before('aderlass-therapie') + SEP + 'Satz auf der Seite: „In der Hildegard Heilkunde ist der Aderlass das wichtigste Mittel zur Behandlung aller chronischen Erkrankungen.“',
     variants=[
       {'key': 'A', 'label': 'mit Termin-Hinweis, die Wirkaussage wird zur Überlieferung', 'value': pack('Aderlass nach Hildegard von Bingen in Berlin | Daniela Dumann', 'Aderlass nach Hildegard von Bingen in Berlin-Charlottenburg: Termine im Frühjahr und Herbst, Ablauf und Kosten. Heilpraktikerin Daniela Dumann.', None, 'Satz auf der Seite: „In der Hildegard-Heilkunde gilt der Aderlass als eines der wichtigsten Verfahren. Hildegard von Bingen beschreibt ihn als Weg, den Körper zu entlasten.“')},
       {'key': 'B', 'label': 'nur Titel und Google-Text, der Satz auf der Seite bleibt', 'value': pack('Aderlass nach Hildegard von Bingen in Berlin | Daniela Dumann', 'Aderlass nach Hildegard von Bingen in Berlin-Charlottenburg: Termine im Frühjahr und Herbst, Ablauf und Kosten. Heilpraktikerin Daniela Dumann.')}],
     recommended_key='A', keyword='Aderlass', seo_lock=True, lock_note='„Aderlass“ und „Hildegard von Bingen“ bleiben, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/aderlass-therapie'}, note='Variante B lässt die Heilaussage auf der Seite stehen. Das ist rechtlich das größere Risiko. Der Satz „Hauptverursacherin aller Erkrankungen“ (Schwarzgalle) steht ebenfalls auf der Seite und wird mit A mit geprüft.',
     guide_text='Hier brauche ich dein Ja. Die Überlieferung bleibt, nur die Heilaussage wird zur Überlieferung.')

card(code='E15', title='Seite „Hildegard-Fasten“: Auftritt bei Google und Einleitung', wave=2, risk_class='health',
     why='**„fasten hildegard von bingen“ wird 480-mal im Monat gesucht.** Deine Seite bekam in 90 Tagen 980 Anzeigen und nur 3 Klicks, im Schnitt auf Platz 56. Der Google-Text ist 495 Zeichen lang, Google zeigt etwa 155.',
     before_value=before('hildegard-fasten') + SEP + 'Einleitung: „… eine einfache, aber wirkungsvolle Methode, um den Körper von seinen Gift- und Schlackenstoffen zu reinigen und die Seele von ihren Belastungen zu befreien.“',
     variants=[
       {'key': 'A', 'label': 'kurz, mit Preis ab 170 €, die Einleitung ohne Entgiftungs-Aussage', 'value': pack('Hildegard-Fasten in Berlin-Charlottenburg | Daniela Dumann', 'Gemäßigtes Fasten nach Hildegard von Bingen in Berlin-Charlottenburg, online oder live, mit persönlicher Begleitung. Termine ab 170 €.', 'Hildegard-Fasten: gemäßigtes Dinkelfasten, online und in Berlin', 'Einleitung: „Das Hildegard-Fasten ist eine überlieferte Form des gemäßigten Fastens mit Dinkel. Ich begleite Sie persönlich, online oder vor Ort.“')},
       {'key': 'B', 'label': 'nur Titel und Google-Text, die Einleitung bleibt', 'value': pack('Hildegard-Fasten in Berlin-Charlottenburg | Daniela Dumann', 'Gemäßigtes Fasten nach Hildegard von Bingen in Berlin-Charlottenburg, online oder live, mit persönlicher Begleitung. Termine ab 170 €.', 'Hildegard-Fasten: gemäßigtes Dinkelfasten, online und in Berlin')}],
     recommended_key='A', keyword='Hildegard-Fasten', seo_lock=True, lock_note='„Hildegard-Fasten“ bleibt, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/hildegard-fasten'}, note='Die Preise („ab 170 €“) stammen von deiner Seite. Der Satz zu „Gift- und Schlackenstoffen“ wird vor dem Einbau auf das Heilmittelwerbegesetz geprüft. ' + NAMENS_HINWEIS,
     guide_text='Hier ist der größte Sprung drin: viele Anzeigen, kaum Klicks. Ein kurzer, klarer Google-Text hilft sofort.')

# ---------------- Wave 2/3: Kurse, Behandlerin, Sammelkarte ----------------
card(code='E16', title='Seite „Ausbildung Gesundheitsberater/in“: Auftritt bei Google und Überschrift', wave=3,
     why='**„gesundheitsberater ausbildung“ wird 720-mal im Monat gesucht.** Deine Seite bekam in 90 Tagen 672 Anzeigen und 9 Klicks, im Schnitt auf Platz 58. Der Google-Titel ist 94 Zeichen lang.',
     before_value=before('ausbildung-ganzheitsmedizin-gesundheitsberater'),
     variants=[
       {'key': 'A', 'label': 'nennt den Suchbegriff und beide Wege: Fernstudium oder Berlin', 'value': pack('Ausbildung Gesundheitsberater/in nach Hildegard von Bingen', 'Gesundheitsberater-Ausbildung nach Hildegard von Bingen: Fernstudium oder vor Ort in Berlin. Inhalte, Dauer, Kosten und Zertifikat im Überblick.', 'Ausbildung Gesundheitsberater/in nach Hildegard von Bingen: Fernstudium und Berlin')},
       KEEP()],
     recommended_key='A', keyword='Gesundheitsberater', seo_lock=True, lock_note='„Gesundheitsberater“ bleibt, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/ausbildung-ganzheitsmedizin-gesundheitsberater'}, note='Dauer, Kosten und Zertifikat übernehme ich nur aus deiner Kursbeschreibung. ' + NAMENS_HINWEIS,
     guide_text='Die Seite wird oft angezeigt, aber selten geklickt. Der Titel ist der schnellste Hebel.')

card(code='E17', title='Seite „Ausbildung Kräuterheilkunde“: Auftritt bei Google und Überschrift', wave=3,
     why='Die Seite ist mit **17 Klicks bei 1.115 Anzeigen** deine Nummer 4 und steht im Schnitt auf Platz 32. Die Suche „ausbildung heilkräuter“ zeigt sie 56-mal, auf Platz 66.',
     before_value=before('ausbildung-kraeuterheilkunde'),
     variants=[
       {'key': 'A', 'label': 'kurz, mit dem Hinweis auf selbst hergestellte Tinkturen', 'value': pack('Ausbildung Kräuterheilkunde nach Hildegard von Bingen', 'Ausbildung Kräuterheilkunde nach Hildegard von Bingen: Tinkturen, Salben, Elixiere selbst herstellen, online und in Berlin. Kursaufbau, Termine, Kosten.', 'Ausbildung Kräuterheilkunde nach Hildegard von Bingen')},
       KEEP()],
     recommended_key='A', keyword='Kräuterheilkunde', seo_lock=True, lock_note='„Kräuterheilkunde“ bleibt, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/ausbildung-kraeuterheilkunde'}, note=NAMENS_HINWEIS, guide_text='Hier ist ein Sprung auf Seite 1 nah.')

card(code='E18', title='Seite „Ausbildung Fastenleiter/in“: Auftritt bei Google und Überschrift', wave=3,
     why='**„fastenleiter ausbildung“ wird 170-mal im Monat gesucht.** Deine Seite steht im Schnitt auf Platz 34 und der Google-Titel ist 88 Zeichen lang.',
     before_value=before('ausbildung-fastenleiterin'),
     variants=[
       {'key': 'A', 'label': 'nennt Inhalte und Dauer sowie Kosten und Termine', 'value': pack('Ausbildung Fastenleiter/in nach Hildegard von Bingen', 'Fastenleiter-Ausbildung nach Hildegard von Bingen: gemäßigtes Dinkelfasten, Inhalte, Dauer, Kosten und Termine, online und in Berlin.', 'Ausbildung Fastenleiter/in nach Hildegard von Bingen')},
       KEEP()],
     recommended_key='A', keyword='Fastenleiter', seo_lock=True, lock_note='„Fastenleiter“ bleibt, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/ausbildung-fastenleiterin'}, note=NAMENS_HINWEIS)

card(code='E19', title='Seite „Ernährungstherapie nach Hildegard“: Auftritt bei Google und Rezepte', wave=3,
     why='**„ernährung hildegard von bingen“ wird 1.410-mal im Monat gesucht**, „hildegard von bingen rezepte“ 1.300-mal. Die Seite steht im Schnitt auf Platz 27 und hat keine Rezepte.',
     before_value=before('ernaehrungstherapie-hildegard-von-bingen'),
     variants=[
       {'key': 'A', 'label': 'Titel und Google-Text neu, dazu ein Rezepte-Abschnitt mit 3 bis 5 Rezepten von dir', 'value': pack('Ernährung nach Hildegard von Bingen: Onlinekurs | Daniela Dumann', 'Onlinekurs Ernährung nach Hildegard von Bingen: acht Lektionen zu Dinkel, Gewürzen und dem rechten Maß, mit Rezepten, für Einsteiger und Fachkräfte.', 'Ernährungstherapie Hildegard von Bingen (bleibt)', 'Neu auf der Seite: Rezepte-Abschnitt')},
       {'key': 'B', 'label': 'nur Titel und Google-Text', 'value': pack('Ernährung nach Hildegard von Bingen: Onlinekurs | Daniela Dumann', 'Onlinekurs Ernährung nach Hildegard von Bingen: acht Lektionen zu Dinkel, Gewürzen und dem rechten Maß, mit Rezepten, für Einsteiger und Fachkräfte.')}],
     recommended_key='A', keyword='Ernährung', seo_lock=True, lock_note='„Ernährung nach Hildegard von Bingen“ bleibt, weil danach gesucht wird. Die Formulierung wählst du.',
     context={'page': '/ernaehrungstherapie-hildegard-von-bingen'}, note='Welche Rezepte du zeigen möchtest, schreibst du bei Variante A in das Kommentarfeld. Ich erfinde keine.', guide_text='Rezepte sind ein eigener Suchbegriff. Wenn du Rezepte hast, lohnt sich Variante A.')

card(code='E20', title='Seite „Lebenslauf“ wird zur Behandlerseite: Auftritt bei Google und Überschrift', wave=3,
     why='Google bewertet Gesundheitsseiten nach **nachweisbarer Erfahrung**. Die Seite „Lebenslauf“ hat heute die Hauptüberschrift „Über mich“, die weder deinen Namen noch deinen Beruf nennt. Die Seite bekam in 90 Tagen 10 Klicks bei 305 Anzeigen, im Schnitt auf Platz 2.',
     before_value=before('lebenslauf'),
     variants=[
       {'key': 'A', 'label': 'dein Name, dein Beruf, seit wann du praktizierst', 'value': pack('Daniela Dumann, Heilpraktikerin in Berlin-Charlottenburg', 'Heilpraktikerin seit 2002, Vizepräsidentin der Internationalen Gesellschaft Hildegard von Bingen. Ausbildung, Mitgliedschaften und mein Weg zur Heilkunde.', 'Daniela Dumann, Heilpraktikerin in Berlin-Charlottenburg')},
       KEEP()],
     recommended_key='A', context={'page': '/lebenslauf'},
     note='Die Adresse /lebenslauf und der Menüpunkt „Lebenslauf“ bleiben. Alle Angaben stammen aus deinem Briefing vom 09.09. Ausbildung, Verband und Viriditas ergänze ich nach deinen Wünschen vom 17.09. (siehe Karte zu „Über mich“).',
     guide_text='Hier geht es um dich als Person. Ich nehme nur Angaben, die du mir gegeben hast.')

card(code='E21', title='Vier weitere Seiten: Oligoscan, Homöopathie, Massage, Kurse & Seminare', wave=3,
     why='Diese vier Seiten haben **Titel mit fremdem Namen, zu lange Google-Texte oder keine Hauptüberschrift**. Die Seite „Kurse & Seminare“ ist mit 53 Klicks deine Nummer 2.',
     before_value='Oligoscan: Titel „Orthomolekulare Medizin Berlin - Oligoscan & Mikronährstoffe | hildegardbingen“\nHomöopathie: Titel „Homöopathie Berlin | Hildegard von Bingen Naturheilkunde | Berlin“\nMassage: Titel „Massage | Hildegard von Bingen Naturheilkunde | Berlin“\nKurse & Seminare: Titel „Kurse & Seminare | Ausbildung Hildegard von Bingen Daniela Dumann | Berlin hildegardbingen“, Google-Text 432 Zeichen',
     variants=[
       {'key': 'A', 'label': 'kurze, klare Titel und Texte für alle vier', 'value': 'Oligoscan: „Oligoscan & Mikronährstoffe in Berlin | Daniela Dumann“\nHomöopathie: „Homöopathie in Berlin-Charlottenburg | Daniela Dumann“\nMassage: „Massagen & Schröpfen nach Hildegard in Berlin | Daniela Dumann“\nKurse & Seminare: „Kurse & Seminare nach Hildegard von Bingen | Daniela Dumann“ mit der Überschrift „Kurse, Seminare & Ausbildungen nach Hildegard von Bingen“'},
       KEEP('Bei allen vier Seiten')],
     recommended_key='A', context={'page': 'mehrere'}, note='Die vollständigen Google-Texte stehen im SEO-Arbeitsplan. ' + NAMENS_HINWEIS)

# ---------------- Design ----------------
card(code='E22', kind='other', type_label='Neues Design', title='Neues Design deiner Startseite', wave=1,
     why='Dein neues Startseiten-Design ist fertig. Es wächst beim Scrollen wie eine Ranke von oben nach unten, nennt **fünf Themen, sechs Leistungen und den Ablauf des ersten Termins** und zeigt deine Bewertung bei Google. Du hast die Vorschau am Freitag, 9. Oktober, per E-Mail bekommen.',
     why_source='Vorschau der neuen Startseite (E-Mail vom 9. Oktober)',
     variants=[
       {'key': 'A', 'label': 'das Design wie in der Vorschau, mit der wachsenden Ranke', 'value': 'Neue Startseite komplett: Ranke, fünf Themen, sechs Leistungen, Ablauf, Bewertungen'},
       {'key': 'B', 'label': 'dieselbe Seite ohne Bewegung, ruhig und schnell', 'value': 'Neue Startseite ohne Ranke und ohne Animationen'},
       {'key': 'C', 'label': 'die Optik bleibt wie heute, nur die Texte aus deinen Freigaben kommen rein', 'value': 'Optik wie heute, neue Texte'}],
     recommended_key='A', context={'page': '/', 'preview_url': 'https://clients.741.studio/r/58f0e3689022/v3/index.html'},
     note='Nichts wird ohne dein Ja umgebaut. Die Kachelbilder sind noch Entwürfe und werden durch deine echten Fotos ersetzt. Für Praxisraum, Garten, Hände bei einer Anwendung und Heilpflanzen brauche ich später Fotos von dir.',
     guide_text='Schau dir die Vorschau in Ruhe an. Variante A ist das Design, das ich empfehle.')

card(code='E23', title='Hauptüberschrift der neuen Startseite', wave=1, risk_class='none',
     why='Die Hauptüberschrift ist das Erste, was Besucher und Google lesen. **„Heilpraktikerin in Berlin-Charlottenburg“** bleibt in jeder Variante, weil danach gesucht wird (1.600 Suchen im Monat bei „heilpraktiker berlin“).',
     why_source='Google-Suchdaten und Text zur neuen Startseite', before_value='Heilpraktikerin in Berlin-Charlottenburg – Heilkunde nach Hildegard von Bingen',
     variants=[
       {'key': 'A', 'label': 'nennt Ort, Schwerpunkt und persönliche Begleitung', 'value': 'Ihre Heilpraktikerin in Berlin-Charlottenburg: Hildegard-Heilkunde, persönlich begleitet.'},
       {'key': 'B', 'label': 'stellt Hildegard von Bingen voran und nennt „seit 2002“', 'value': 'Hildegard-Heilkunde in Charlottenburg, begleitet von einer Heilpraktikerin seit 2002.'},
       {'key': 'C', 'label': 'sagt, was die Patientin sucht, und nennt den Ort', 'value': 'Ihr Weg zu mehr Wohlbefinden, persönlich begleitet von einer Heilpraktikerin in Berlin-Charlottenburg seit 2002.'}],
     recommended_key='A', keyword='Heilpraktikerin in Berlin-Charlottenburg', seo_lock=True,
     lock_note='„Heilpraktikerin“ und „Berlin-Charlottenburg“ bleiben in der Überschrift. Die Formulierung wählst du.',
     context={'page': '/'}, note='Die aktuelle Überschrift auf deiner Seite gilt seit dem 09.10. und ist ein Zwischenstand. Die Variante ersetzt sie nur, wenn du das neue Design wählst.')


card(code='E24', title='Seite „Über mich“: deine drei Ergänzungen vom 17.09.', wave=2, risk_class='legal',
     why='Du hast am 17.09. drei Ergänzungen für deine Vorstellung gewünscht: **Ausbildung, Berufsverband und die Gründung von Viriditas**. Sie sind noch nicht auf der Seite.',
     why_source='Dein Kommentar im Portal vom 17.09. und dein Briefing vom 09.09.', why_date='2026-09-17',
     before_value='Ausbildung: Hildegard-Heilkunde bei Gudrun und Peter Germann (Phytaro, Dortmund)\nMitgliedschaften: Internationale Gesellschaft Hildegard von Bingen, Medizinischer Arbeitskreis Engelberg, Fachverband Freie Heilpraktiker, FET, MeGeMit\nViriditas: Schule seit 2021',
     variants=[
       {'key': 'A', 'label': 'mit den Namen aus deinem Kommentar', 'value': 'Ausbildung: „unter anderem bei Dr. Wighard Strehlow sowie Gudrun und Peter Germann (Phytaro, Dortmund)“\nMitgliedschaften: zusätzlich „Lachesis, Berufsverband für Heilpraktikerinnen und Frauengesundheit“\nViriditas: „Gründerin der Schule Viriditas Grünkraft (2021)“', 'ask_note': True},
       {'key': 'B', 'label': 'nur „unter anderem“, ohne Namen', 'value': 'Ausbildung: „unter anderem Hildegard-Heilkunde und Homöopathie“\nMitgliedschaften wie bisher\nViriditas: „Gründerin der Schule Viriditas (2021)“'}],
     recommended_key='A', context={'page': '/lebenslauf'},
     note='Bitte prüfe Namen, Schreibweise und das Jahr deiner Mitgliedschaft im Lachesis-Verband, denn ich nehme nur Angaben, die du bestätigst. [von Daniela zu bestätigen]',
     guide_text='Hier brauche ich dein Ja. Titel und Mitgliedschaften müssen genau stimmen.')

card(code='E25', title='Seite „Ernährungsberatung“: drei neue Fragen mit Antworten', wave=2, risk_class='price',
     why='Die meistgestellten Fragen bei Google zu diesem Thema drehen sich um **Kosten, Krankenkasse und Ablauf**. Die Seite beantwortet sie heute nicht.',
     why_source='Google-Suchdaten und Abgleich deiner Website', why_date='2026-09-13', before_value='Keine Antworten zu Kosten, Krankenkasse und Verordnung auf der Seite',
     variants=[
       {'key': 'A', 'label': 'drei Fragen mit kurzen Antworten, ohne Heilaussage', 'value': 'Wie viel kostet eine Ernährungsberatung in Berlin? „In meiner Praxis kostet die Erstanamnese (60 Minuten) 220 €, Folgetermine 150 € je angefangene Stunde, abgerechnet nach der Gebührenordnung für Heilpraktiker.“\nWelche Krankenkasse bezahlt Ernährungsberatung? „Gesetzliche Krankenkassen übernehmen die Kosten für die Beratung bei einer Heilpraktikerin in der Regel nicht. Private Krankenversicherungen, Beihilfe und Zusatzversicherungen erstatten teilweise, je nach Tarif.“\nBrauche ich eine ärztliche Verordnung? „Bei mir als Heilpraktikerin ist keine Verordnung nötig. Sie können direkt einen Termin anfragen.“'},
       {'key': 'B', 'label': 'nur die Frage zu den Kosten', 'value': 'Wie viel kostet eine Ernährungsberatung in Berlin? „In meiner Praxis kostet die Erstanamnese (60 Minuten) 220 €, Folgetermine 150 € je angefangene Stunde, abgerechnet nach der Gebührenordnung für Heilpraktiker.“'}],
     recommended_key='A', context={'page': '/ernährungsberatung'}, note='Die Antworten stammen aus dem Textentwurf vom 16.09. und enthalten nur Angaben von deiner Seite. Die Aussage zu den Kassen prüfst du bitte auf Richtigkeit.',
     guide_text='Hier brauche ich dein Ja zu den Preisen und zur Aussage über die Kassen.')

card(code='E26', title='Seite „Hildegard-Fasten“: drei neue Fragen mit Antworten', wave=2, risk_class='health',
     why='Die Seite bekam in 90 Tagen **980 Anzeigen und 3 Klicks**. Wer „fasten nach hildegard von bingen“ sucht, findet auf der Seite heute keine Antwort auf die ersten Fragen.',
     before_value='Keine Fragen und Antworten auf der Seite',
     variants=[
       {'key': 'A', 'label': 'ohne Entgiftungs-Aussage, mit Hinweis auf ein Vorgespräch', 'value': 'Wie fastet man nach Hildegard von Bingen? „Gemäßigt, mit Dinkel oder glutenfrei. Der Körper bekommt weiterhin alle nötigen Dinge in ausreichendem Maß, ergänzt durch Hildegards Gewürze.“\nWas bringt Fasten nach Hildegard von Bingen? „Viele erleben die Fastenwoche als Zeit der Ruhe. Die Erfahrung ist bei jedem Menschen anders.“\nKann ich ohne Vorerfahrung teilnehmen? „Ja. Wir besprechen zu Beginn kurz Ihre gesundheitliche Ausgangslage. Bei Vorerkrankungen empfehle ich vorab ein Einzelgespräch.“'},
       {'key': 'B', 'label': 'wie im Entwurf vom 16.09., mit „Entgiftung und Entschlackung“', 'value': 'Wie A, nur die zweite Antwort lautet: „Es soll bei der Entgiftung und Entschlackung des Körpers unterstützen und Raum für Ruhe und Lebensfreude schaffen, individuell verschieden.“'}],
     recommended_key='A', context={'page': '/hildegard-fasten'}, note='Variante B bleibt ein Risiko: Entgiftung und Entschlackung sind Wirkversprechen, die sich nicht belegen lassen. Die Texte stammen aus dem Entwurf vom 16.09. und werden vor dem Einbau noch einmal geprüft.',
     guide_text='Hier brauche ich dein Ja. Die neutrale Antwort ist rechtlich sicherer, die Wirkung bleibt für dich beschreibbar.')

card(code='E27', title='Seite „Behandlungen“: vier Abschnitte statt einer langen Seite', wave=3,
     why='Die Seite „Behandlungen“ ist eine deiner längsten Seiten. **Vier klare Abschnitte** helfen Besuchern und Google, die Themen zu finden, ohne dass sich ein Wort an deinen Texten ändert.',
     before_value='Eine durchgehende Seite ohne Zwischenüberschriften zu den Schwerpunkten. Die Preisliste bleibt unverändert.',
     variants=[
       {'key': 'A', 'label': 'vier Abschnitte, deine Texte bleiben', 'value': 'Zwischenüberschriften: „Ernährung und Fasten“\n„Aderlass, Schröpfen und Darmsanierung“\n„Kräuter und Rezepturen“\n„Diagnostik: Oligoscan, Labor und Schilddrüse“'},
       {'key': 'B', 'label': 'die Seite bleibt wie sie ist', 'value': 'Keine neuen Zwischenüberschriften'}],
     recommended_key='A', context={'page': '/behandlungen'}, note='Es ändert sich nur die Gliederung. Die Preisliste bleibt unverändert.', guide_text='Das ist eine kleine Änderung ohne Risiko.')

CARDS.sort(key=lambda c: int(c['code'][1:]))

# ---------------- Output ----------------
def sql_str(v):
    if v is None: return 'null'
    return "'" + str(v).replace("'", "''") + "'"

def write_outputs():
    cols = ['client_id', 'code', 'kind', 'type_label', 'area', 'title', 'why', 'why_source', 'why_date', 'variants', 'recommended_key',
            'before_value', 'keyword', 'seo_lock', 'lock_note', 'context', 'note', 'guide_text', 'risk_class', 'status']
    rows = []
    for c in CARDS:
        assert 2 <= len(c['variants']) <= 3, c['code']
        assert any(v['key'] == c['recommended_key'] for v in c['variants']), c['code']
        vals = [sql_str(CLIENT), sql_str(c['code']), sql_str(c['kind']), sql_str(c['type_label']), sql_str(c['area']), sql_str(c['title']),
                sql_str(c['why']), sql_str(c['why_source']), sql_str(c['why_date']), sql_str(json.dumps(c['variants'], ensure_ascii=False)) + '::jsonb',
                sql_str(c['recommended_key']), sql_str(c['before_value']), sql_str(c['keyword']), 'true' if c['seo_lock'] else 'false',
                sql_str(c['lock_note']), sql_str(json.dumps(c['context'], ensure_ascii=False)) + '::jsonb', sql_str(c['note']), sql_str(c['guide_text']),
                sql_str(c['risk_class']), "'draft'"]
        rows.append('  (' + ', '.join(vals) + ')')
    sql = ('-- Daniela Dumann (%s): new approval cards as DRAFT (hidden from the client). E1-E7 already exist as drafts (13.10.).\n'
           '-- EXECUTED 13.10.2026 (insert via REST, 20 rows E8-E27, status draft). Status draft = Daniela sees nothing. Release only per item after Martin\'s yes in the chat (release-decisions-from-chat).\n'
           '-- Health rule: every card with risk_class <> \'none\' needs hwg_checked = true before any status other than draft (trigger approval_items_guard).\n'
           '-- German, du, Martin in first person. No tool names. Facts: live crawl 13.10., Search Console 13.10., SEO-Arbeitsplan 09.10.\n'
           'begin;\ninsert into public.approval_items\n  (%s)\nvalues\n%s;\ncommit;\n') % (CLIENT, ', '.join(cols), ',\n'.join(rows))
    open(os.path.join(HERE, 'approval-drafts-dumann.sql'), 'w', encoding='utf-8').write(sql)
    json.dump(CARDS, open(os.path.join(HERE, 'cards.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    md = ['# Daniela Dumann: Entscheidungskarten, Entwurf (13.10.2026)', '',
          'Status aller Karten: **draft** (Daniela sieht nichts). Martin gibt jede Karte einzeln im Chat frei. E1 bis E7 liegen schon als Entwurf in der Datenbank (Freigabe-Chat, 13.10.). E8 bis E%s sind neu in diesem Lauf.' % CARDS[-1]['code'][1:], '',
          'Welle 1 = zuerst freigeben, Welle 2 = danach, Welle 3 = später. Gesundheits-Karten brauchen vor der Freigabe `hwg_checked = true`.', '']
    for c in CARDS:
        md += [f'## {c["code"]} · {c["title"]}', f'Welle {c.get("wave", "-")} · Art `{c["kind"]}` · Risiko `{c["risk_class"]}` · SEO-Schloss: {"ja, Wort: " + c["keyword"] if c["seo_lock"] else "nein"}', '',
               f'**Warum (Kunde sieht):** {c["why"]}', f'Quelle: {c["why_source"]}, Stand {c["why_date"]}', '']
        if c['before_value']: md += [f'**Vorher (live):** {c["before_value"]}', '']
        md.append('**Optionen:**')
        for v in c['variants']:
            md.append(f'- {v["key"]}{" (741 empfiehlt)" if v["key"] == c["recommended_key"] else ""}: {v["value"]} _({v.get("label", "")})_')
        if c['lock_note']: md += ['', f'Schloss-Hinweis: {c["lock_note"]}']
        if c['note']: md += ['', f'Hinweis: {c["note"]}']
        if c['guide_text']: md += ['', f'Martin-Figur: „{c["guide_text"]}“']
        md.append('')
    open(os.path.join(HERE, 'approval-cards-draft.md'), 'w', encoding='utf-8').write('\n'.join(md))
    return len(CARDS)

if __name__ == '__main__':
    print(write_outputs(), 'cards written')
