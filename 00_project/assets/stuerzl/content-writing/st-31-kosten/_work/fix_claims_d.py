import sys,json
sys.path.insert(0,'/private/tmp/claude-501/-Users-martindrendel-741website/3f99edcd-8910-41d2-bfe6-7066dd615cee/scratchpad')
from upsert import upsert
S='gesetze-im-internet.de, gelesen 2026-10-11, gespeichert in _work/'
K='client-texte/kosten.txt (Kanzlei, Datei 09.10.2026), gelesen 2026-10-11'
items=[
 dict(id='C08',type='fact',text='Vier-Augen-Prinzip (kosten.txt): jedes Mandat üblicherweise von zwei Anwältinnen/Anwälten betreut; zusätzliche Kontrolle wichtiger Entscheidungen. Die Aussagen "hohe fachliche Qualität sicherstellen" und "verlässliche Erreichbarkeit sicherstellen" stehen nicht auf der Seite (Review D, Punkt 6 und 7). Kostenaussage aus der Live-FAQ: Zusammenarbeit erfahrener und jüngerer Anwälte kann Kosten sparen, jüngere haben geringere Stundensätze und übernehmen weniger komplexe Tätigkeiten',source=K+'; Live-FAQ (_work/live/faq.txt Zeile 57)'),
 dict(id='C09',type='fact',text='Erstberatung: erste Sachverhalts- und Risikoeinschätzung sowie transparente Information zu den voraussichtlichen Kosten einer tatsächlichen Mandatsübernahme; üblicherweise Pauschale, je nach Zeit und Umfang. Keine Zusage, die Höhe "vor dem Gespräch" zu nennen',source=K+'; approved-copy.md F1 (Zeile 155)'),
 dict(id='C13',type='fact',text='Kostenmodell: Abrechnung grundsätzlich nach Zeitaufwand in Sechs-Minuten-Einheiten, Vergütung zu Beginn des Mandats in Textform vereinbart (Entscheidung Fixrunde, Punkt 3), kein RVG; in der Regel Vorschuss mit Rückzahlung nicht benötigter Teile nach Endabrechnung; Erstberatung üblicherweise gegen Pauschale; Tätigkeitsnachweis je Rechnung; Vier-Augen-Prinzip',source=K+'; content-writing-stuerzl-fixes.md Abschnitt 2 Punkt 3'),
 dict(id='C04',type='fact',text='Pauschalvergütung im Einzelfall möglich, beispielsweise wenn der Umfang des Verfahrens vollumfänglich abzuschätzen ist oder wenn das Mandat eine Beratungstätigkeit betrifft und Ziel der Tätigkeit die Erstellung eines Gutachtens ist (Beispiele, keine abschließende Liste)',source=K),
 dict(id='C16',type='legal',required=True,text='§ 3a Abs. 1 RVG: Vereinbarung über die Vergütung bedarf der Textform (Satz 1); muss als Vergütungsvereinbarung oder in vergleichbarer Weise bezeichnet werden, von anderen Vereinbarungen mit Ausnahme der Auftragserteilung deutlich abgesetzt sein und darf nicht in der Vollmacht enthalten sein (Satz 2); enthält einen Hinweis, dass die gegnerische Partei, ein Verfahrensbeteiligter oder die Staatskasse im Falle der Kostenerstattung regelmäßig nicht mehr als die gesetzliche Vergütung erstatten muss (Satz 3); Sätze 1 und 2 gelten nicht für eine Gebührenvereinbarung nach § 34 (Satz 4); Abs. 3: unangemessen hohe Vergütung kann im Rechtsstreit auf den angemessenen Betrag bis zur Höhe der gesetzlichen Vergütung herabgesetzt werden',source=S+'rvg__3a.txt',numbers=['3a','1','3','34'],must_appear=['§ 3a Abs. 1 RVG']),
 dict(id='C23',type='fact',text="Zitat Dr. Stürzl: 'Jedes Mandat und jeder Mandant ist anders.' (steht auf der Startseite; auf dieser Seite nicht verwendet)",source='Live-Startseite, 2026-10-11'),
 dict(id='C30',type='fact',text='Telefonisch erreichbar Montag bis Freitag durchgehend 09:30 bis 14:30 Uhr; Termine und Erstberatung auch außerhalb nach Vereinbarung. Keine Zusage zur Erreichbarkeit außerhalb dieser Zeiten',source='Live-Kontaktseite und Source of Truth Tab 02 Zeile 38 / nap.json phone_hours, 2026-10-11',numbers=['09:30','14:30','09','30','14']),
 dict(id='C30b',type='fact',text='Kostentransparenz: Die Kanzlei informiert von Beginn an über die zu erwartenden Kosten, soweit Art und Umfang des Verfahrens dies im Vorfeld zulassen; die Transparenz endet nicht nach Auftragserteilung und Unterzeichnung der Vergütungsvereinbarung; im laufenden Mandat behält die Kanzlei die Kosten im Blick und kommuniziert kostenrelevante Aspekte und Entwicklungen offen. Mandate sind so unterschiedlich wie die Sachverhalte und Menschen dahinter. Qualifizierte, persönliche und strategisch durchdachte Beratung erfordert Erfahrung, Sorgfalt und Zeit',source=K),
 dict(id='C31',type='fact',text='Kundentext "Warum sich die Investition in uns lohnt": Anspruch ist nicht, die günstigste Kanzlei zu sein, sondern eine wirtschaftlich sinnvolle Vertretung; Punkte: Praxiserfahrung in wirtschafts- und insbesondere steuerstrafrechtlichen Verfahren, Lehr-, Vortrags- und Veröffentlichungstätigkeit, Back-Office zur Mandatsorganisation, digitale Prozesse und KI zur Zeit- und Kostenersparnis, Einsatzbereitschaft für die Interessen der Mandanten. Nicht übernommen: Spezialisierung, Ruf, Netzwerk, Leidenschaft, hochqualifiziert, persönliche Erreichbarkeit außerhalb der Bürozeiten',source=K),
 dict(id='C32',type='credential',text='Dr. Stürzl ist Dozentin im Masterstudiengang Wirtschafts- und Steuerstrafrecht (LL.M.), Rechtswissenschaftliche Fakultät, Universität zu Köln; Dozentin für den Lehrgang "Zertifizierter Berater für Steuerstrafrecht (DAA)"; Gastdozentin an der Bundesfinanzakademie; regelmäßige Publikationen zum Steuerstrafrecht in Fachzeitschriften',source='Live-Profilseite dr-anja-stuerzl (_work/live/dr-anja-stuerzl.txt), Rubrik Vorträge und Publikationen, gelesen 2026-10-11',numbers=['LL.M.']),
 dict(id='C33',type='fact',text='Selbstanzeige ist ein steuerstrafrechtliches Mandat und wird grundsätzlich nach Zeitaufwand abgerechnet (Ableitung aus kosten.txt: steuerstrafrechtliche Mandate werden grundsätzlich nach Zeitaufwand abgerechnet). Ob Selbstanzeige-Mandate anders abgerechnet werden, ist offen (Platzhalter, Frage an die Kanzlei)',source=K+'; OPEN-FLAGS A8'),
 dict(id='C34',type='fact',text='Tätigkeitsnachweis aus spezieller Anwaltssoftware; Zeiterfassung per Software, Stoppuhr oder manuell (Live-FAQ)',source=K+'; Live-FAQ'),
]
upsert('01-brief/claims.json',items)
b=json.load(open('01-brief/brief.json',encoding='utf-8'))
b['schema_faq']=True
b['word_range']=[520,1750]
b['sections']=[
 {"id":"S01","element":"hero","job":"H1 mit Kosten-Keyword, Haltung (offen über Geld)","cta":"primary"},
 {"id":"S02","element":"answer","job":"Kostenmodell in 4 Sätzen"},
 {"id":"S03","element":"el-grid","job":"Wovon die Kosten abhängen"},
 {"id":"S04","element":"table","job":"So wird abgerechnet (Zeit, Stundensatz, Selbstanzeige, Pauschale, Vorschuss, Rechnung, Erstberatung), RVG-Begründung, § 3a RVG, Vier-Augen-Prinzip","cta":"secondary"},
 {"id":"S05","element":"text","job":"Wer die Kosten trägt (Vergütungsvereinbarung, Rechtsschutz, Staatskasse)"},
 {"id":"S06","element":"el-grid","job":"Warum sich die Investition lohnt (belegbare Punkte aus dem Kundentext, ohne BRAO-Risikowörter)"},
 {"id":"S07","element":"text","job":"KI-Einsatz (Baustein der Kanzlei, Prüfhinweis)"},
 {"id":"S08","element":"faq","job":"FAQ Kosten, Preis zuerst"},
 {"id":"S09","element":"cta","job":"Abschluss","cta":"primary"}]
b['placeholders_allowed']=list(dict.fromkeys(b['placeholders_allowed']+['Abrechnung von Selbstanzeige-Mandaten']))
tg=[t['url'] for t in b['internal_link_targets']]
for u,a,r in [('/steuerstrafrecht/gutachten-risikobewertung/','Gutachten und Risikobewertung','sibling'),('/kontakt/','Kontakt','contact')]:
    if u not in tg: b['internal_link_targets'].append({'url':u,'anchor':a,'role':r})
json.dump(b,open('01-brief/brief.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
