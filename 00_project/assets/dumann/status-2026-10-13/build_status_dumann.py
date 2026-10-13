"""Daniela Dumann: status page (German) 13.10.2026, DRAFT. Uses the shared builder 00_project/assets/client-status/build_status.py.
Run: python3 build_status_dumann.py  -> status-dumann-2026-10-13.html (self-contained, noindex).
Sources for every number: SOURCES.md next to this script."""
import os, sys
sys.path.insert(0, '/Users/martindrendel/741website/00_project/assets/client-status')
from build_status import render, chip
HERE = os.path.dirname(os.path.abspath(__file__))

DONE, RUN, OPEN = 'done', 'progress', 'pending'
cfg = dict(
    lang='de', title='Dein SEO-Fahrplan | Naturheilpraxis Daniela Dumann', brand_sub='Local-SEO-<br>Programm',
    meta_lines=['Naturheilpraxis Daniela Dumann · Berlin-Charlottenburg', 'danieladumann.de · Stand 13. Oktober 2026 · Woche 5 von 13'],
    h1='Dein SEO-<em>Fahrplan</em>',
    lead='<b>Neu am 13. Oktober:</b> Hier siehst du, wo wir stehen, was uns bremst, was aus deinen Wünschen wurde und was in den nächsten vier Wochen passiert. Deine Entscheidungen findest du im Bereich „Entscheidungen“.',
    status_h='Status · 13. Oktober 2026', status_badge='Wo wir stehen',
    status_lead='Seit dem Programmstart am 14. September haben wir viel im Hintergrund gebaut. Auf deiner Website ist davon noch wenig zu sehen, weil jede Änderung erst nach deinem Ja live geht. Darum haben sich die Zahlen noch nicht bewegt. Diese Seite zeigt, was als Nächstes passiert.',
    sources='Quellen: Google Search Console (Daten bis 10. Oktober), dein Google-Profil, unsere Sichtbarkeitsmessung vom 1. Oktober, Abgleich deiner Website am 13. Oktober 2026.',
    sections=[
        {'kind': 'mg', 'pose': 'hello', 'text': 'Hallo Daniela, hier steht alles an einem Ort. Die Karten mit deinen Entscheidungen kommen einzeln, damit du nie alles auf einmal prüfen musst.', 'flip': False},
        {'kind': 'kpis', 'items': [
            {'cls': 'k-rev', 'l': 'Klicks aus der Google-Suche', 'n': '159', 'd': 'September. August 110, Juli 111. Vom 1. bis 10. Oktober: 47 (gleiche Tage im September: 69)'},
            {'cls': 'k-dead', 'l': 'Anzeigen in der Google-Suche', 'n': '1.976', 'd': 'September. August 2.602, Juli 3.167, April 5.477. Der Rückgang begann vor unserem Start'},
            {'cls': 'k-new', 'l': 'Google-Bewertungen', 'n': '9 von 53', 'd': '5,0 Sterne, Stand 13. Oktober. Ziel: 53 bis Tag 90 (um den 13. Dezember)'},
            {'cls': 'k-pend', 'l': 'Top-3-Anteil in Google Maps', 'n': '0 %', 'd': 'Messung vom 1. Oktober, Suche „heilpraktiker charlottenburg“. An 5 von 49 Messpunkten erscheinst du überhaupt. Ziel: Top 3'},
        ]},
        {'kind': 'table', 'h': 'Was uns bremst', 'head': ['Bremse', 'Wirkung', 'Lösung', 'Wer'], 'rows': [
            ['Google-Titel und Google-Texte sind noch die alten', 'Bei 21 von 34 Seiten hängt der Name „hildegardbingen“ am Titel. Mehrere Google-Texte sind 200 bis 500 Zeichen lang und werden abgeschnitten', 'Für jede Seite ein neuer Titel mit passendem Text und neuer Überschrift. Du wählst im Bereich „Entscheidungen“', '741 baut ein, du entscheidest'],
            ['Einige Aussagen auf Seiten sind riskant', 'Sätze zu Krebs, eine Prozentzahl ohne Beleg und „wichtigstes Mittel bei allen chronischen Erkrankungen“. Sie können für Heilpraktikerinnen rechtlich unangenehm werden', 'Streichen oder neutral umschreiben. Ich prüfe jeden Wortlaut vorher auf das Heilmittelwerbegesetz', 'Du entscheidest, 741 baut ein'],
            ['Wenige Bewertungen', 'Du hast 9 Bewertungen. Die führende Praxis für „heilpraktiker charlottenburg“ hat 52, die führende Ernährungsberaterin 163 (Messung vom 31. August)', 'Deine Anleitung für Bewertungen (WhatsApp-Bild und A4-Blatt) liegt bereit. Je mehr Patient:innen sie erhalten, desto schneller wächst die Zahl', 'Du, mit unserer Anleitung'],
            ['Maps und KI-Antworten zeigen dich noch nicht', 'In Google Maps hast du 0 % Top-3-Anteil. In fünf Suchen mit KI-Antworten (Stand 9. Oktober) wirst du nirgends genannt', 'Dein Profil, deine Bewertungen und deine Seiten wirken zusammen, dazu kommen Verzeichnis-Einträge. Wir messen im November neu', '741'],
            ['Veraltete und uneinheitliche Angaben', 'Elf Kurskarten zeigen „Beendet“. Die Öffnungszeiten stehen an vier Stellen in vier Versionen', 'Beendete Karten ausblenden, eine Version der Zeiten überall', 'Du entscheidest, 741 baut ein'],
        ]},
        {'kind': 'para', 'h': 'Wie verlässlich sind die Zahlen?', 'text': 'Die Klicks und Anzeigen kommen aus der Google Search Console deiner Website. Sie sind echt und bis zum 10. Oktober vollständig. Die Analytics-Messung läuft seit dem 30. September, darum haben wir noch keinen Verlauf. Die Bewertungen habe ich am 13. Oktober direkt in deinem Google-Profil gelesen.'},
        {'kind': 'table', 'h': 'Deine Wünsche und wo sie stehen', 'head': ['Wunsch', 'Stand', 'Nächster Schritt'], 'rows': [
            ['Heilkunde statt „Naturheilkunde“ in der Überschrift (WhatsApp, 12. Okt)', chip(DONE, 'Erledigt'), 'Die Überschrift der Startseite lautet jetzt „Heilkunde nach Hildegard von Bingen“'],
            ['Kräuterheilkunde und Aderlass als weitere Google-Kategorien (17. Sep)', chip(DONE, 'Beantwortet'), 'Google bietet beides nicht als Kategorie an. Beide stehen als Leistungen in deinem Profil, dort werden sie gefunden'],
            ['„Diagnostik und Behandlung“ bei HPU und KPU (17. Sep)', chip(DONE, 'Erledigt'), 'Der Leistungstext in deinem Profil ist ergänzt'],
            ['Telefonsprechstunde werktags 13 bis 14 Uhr (17. Sep)', chip(RUN, 'Karte kommt'), 'Sie steht in der Karte zu den Öffnungszeiten, damit überall dieselben Zeiten stehen'],
            ['Satz zur Gebührenordnung beim ersten Termin (17. Sep)', chip(RUN, 'Karte kommt'), 'Ich habe deine Formulierung in die Karte zu den Kosten übernommen'],
            ['Über mich: Ausbildung, Berufsverband, Gründung von Viriditas (17. Sep)', chip(RUN, 'Karte kommt'), 'Du bestätigst Namen und Jahre in einer Karte, dann kommt alles auf die Behandlerseite'],
            ['Videosprechstunde nennen (17. Sep)', chip(RUN, 'Karte kommt'), 'Ich habe einen Satz vorbereitet, den ich vorher rechtlich prüfe'],
            ['Wer überarbeitet die Startseite? (4. Sep)', chip(DONE, 'Beantwortet'), 'Ich setze alle Änderungen selbst um, jede erst nach deinem Ja. Du musst nichts in Wix ändern'],
            ['Eigene Seite zur Ernährungsberatung nach Hildegard, Texte zu Arthrose und Wechseljahren (4. Sep)', chip(OPEN, 'Offen'), 'Zuerst verbessern wir die bestehenden Seiten. Ob und wo diese Themen dazukommen, besprechen wir danach. Du musst nichts schreiben'],
            ['Öffentliche E-Mail-Adresse (17. Sep)', chip(OPEN, 'Frage an dich'), 'Auf deiner Website steht praxis@danieladumann.de. Soll das so bleiben? Bei Google gibt es dafür kein Feld'],
        ]},
        {'kind': 'table', 'h': 'Was auf deiner Website schon live ist', 'head': ['Änderung', 'Stand'], 'rows': [
            ['Überschrift der Startseite', 'Live seit dem 9. Oktober, am 12. Oktober auf „Heilkunde“ angepasst'],
            ['Einleitungsabsatz unter dem Titelbild der Startseite', 'Live seit dem 9. Oktober'],
            ['Fußzeile: „Termine nach Vereinbarung“', 'Live, die Zeile zu Hausbesuchen ist weg'],
            ['Google-Titel und Google-Text der Startseite', 'Noch nicht: Die Werte vom 9. Oktober wurden beim letzten Veröffentlichen zurückgesetzt. Ich setze sie neu, sobald du bei den ersten Karten zustimmst'],
        ]},
        {'kind': 'table', 'h': 'Was wir im Hintergrund für dich gebaut haben', 'head': ['Baustein', 'Was er dir bringt'], 'rows': [
            ['Google-Profil', 'Sieben Kategorien und 40 Leistungen sind gesetzt. Das doppelte Profil ist bereinigt, jetzt läuft alles auf einem Profil'],
            ['Messung', 'Analytics und Search Console sind seit dem 30. September neu eingerichtet. Dazu ein Sichtbarkeits-Report und eine erste Messung der KI-Sichtbarkeit'],
            ['SEO-Arbeitsplan für die Website', '16 Seiten mit Ist und Soll für Google-Titel, Google-Text und Überschrift. Jede Änderung zeige ich dir vorher und nachher'],
            ['Seitentexte', 'Für die Startseite und drei weitere Seiten (Ernährungsberatung, Behandlungen, Hildegard-Fasten) liegen Entwürfe im Seitenbaum. Du kannst sie lesen und freigeben'],
            ['Verzeichnis-Einträge', '35 Einträge in Branchenverzeichnissen sind beauftragt, die Datenprüfung läuft. Doppelte und falsche Einträge (zum Beispiel eine falsche Telefonnummer) werden bereinigt'],
            ['Neues Design der Startseite', 'Die Vorschau ist fertig. Sie zeigt eine Ranke, fünf Themen, sechs Leistungen und den Ablauf des ersten Termins. Du entscheidest in einer Karte'],
        ]},
        {'kind': 'table', 'h': 'Die nächsten vier Wochen', 'head': ['Woche', 'Was passiert', 'Wer'], 'rows': [
            ['13. Okt', 'Die ersten Karten kommen zu dir: der Name hinter dem Seitentitel, die Titel der Seiten „Behandlungen“, „Ernährungsberatung“ und „Schilddrüse“ sowie das neue Design', '741, du (Entscheidungen)'],
            ['20. Okt', 'Was du freigegeben hast, geht auf die ersten Seiten. Weitere Karten folgen zu Darmsanierung, Kräutern, Aderlass und Fasten. Die Bewertungs-Anleitung geht an deine Patient:innen', '741, du (Karten, Bewertungen)'],
            ['27. Okt', 'Die Behandlerseite „Über mich“ entsteht nach deinen Angaben, danach die Kurs-Seiten. Die Verzeichnis-Einträge gehen online', '741, du (Angaben)'],
            ['3. Nov', 'Neue Messung in Maps und Suche, Vergleich mit den Zahlen von heute. Danach planen wir die nächsten Seiten', '741'],
        ]},
        {'kind': 'mg', 'pose': 'point', 'text': 'Der schnellste Hebel: Google zeigt bei jeder Suche deinen alten Titel. Sobald du bei den ersten Karten zustimmst, geht der neue Titel live.', 'flip': True},
        {'kind': 'table', 'h': 'Was wir von dir brauchen', 'head': ['Entscheidung', 'Warum sie wichtig ist'], 'rows': [
            ['Name hinter jedem Seitentitel', 'Der Name steht bei 21 von 34 Seiten noch falsch'],
            ['Titel, Texte und Überschriften der wichtigsten Seiten', 'Hier liegt der größte Hebel für deine Klicks'],
            ['Aussagen, die ich streichen oder umschreiben möchte', 'Sie schützen dich rechtlich'],
            ['Neues Design und Hauptüberschrift der Startseite', 'Danach kann ich die Seite umbauen'],
            ['Öffnungszeiten, Garten, Videosprechstunde und beendete Termine', 'Überall dieselben, aktuellen Angaben'],
            ['Fragebogen Positionierung', 'Der letzte offene Schritt aus dem Start. Er schärft, für wen die Seite schreibt'],
        ]},
    ])

if __name__ == '__main__':
    render(cfg, os.path.join(HERE, 'status-dumann-2026-10-13.html'))
    print('ok')
