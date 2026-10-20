# Standard: Startseite & Leistungsseiten für lokale Health-Kunden (SEO + GEO + Local)

> **Kanonische Fassung mit WARUM je Regel (für jeden Agenten): Google Doc → https://docs.google.com/document/d/1b_TsRsUUf3s4cIXV-Kop7qu4Y5gqmpI4KFciqKqC_0E/edit**

Konsolidiert aus dem Praxis-Suriya-Prozess (Sept. 2026). Gilt für JEDE Startseite/Money-Page
im 741-Local-SEO-Programm. Ziel: (a) bei Google ranken, (b) von KI-Antwortmaschinen zitiert werden,
(c) lokal konvertieren. Referenz-Beispiel: `clients.741.studio/r/8dbd937730d2/suriya-text-startseite.html`.

---

## A · Prozess (in dieser Reihenfolge — nie überspringen)

1. **Source of Truth laden** (gelockte Stammdaten: Name, NAP, Kategorien, Leistungen, Buchungs-URL,
   Öffnungszeiten, Behandler:in, „mag / mag nicht"). Nie davon abweichen.
2. **Live-Seite prüfen, bevor geschrieben wird** — nicht bei 0 anfangen:
   Wortzahl, H1/H2-Struktur, vorhandene Sektionen, CTAs, NAP, Builder (Elementor/Enfold/…),
   Bilder (WebP?), Maps, Bewertungen, Sie/du. Was gut ist, wird übernommen und verbessert.
3. **Wettbewerber benchmarken** (Top 3–5 der SERP für das Haupt-Keyword): Wortzahl, 1×H1,
   Bewertungen auf der Home, Maps, abgedeckte Unterthemen. Erst dann weiß man, wo die echte Lücke ist.
4. **Datenpaket füllen** (nur echte Daten, siehe C).
5. **Fertigen Text schreiben** (Struktur D) — vollständig, veröffentlichungsreif, KEINE Snippets.
6. **Qualitäts-Checks** (F) + **Mindestanforderungen** (E) gegen die Live-Seite abhaken.
7. **Liefern** (G): eigene lesbare Seite, verlinkt aus dem Seitenbaum, mit Freigabe. Website bleibt unberührt.

## A0 · Verifikations-Gates (blockierend — eine Seite ist NICHT fertig, ohne dass alle vier ✓ sind)

Diese vier Punkte standen vorher schon in A/F, wurden aber als weiche Empfehlung behandelt und dadurch beim Maria-Brasse-Durchlauf (13.09.2026) für 8 von 9 Seiten übergangen — Ergebnis: Seiten mit 268–650 Wörtern gegen reale Wettbewerber-Mediane von 964–4.198 Wörtern, teils sogar dünner als der Kunden-Bestand. Ab jetzt gilt strikt:

1. **Benchmark-Fetch schlägt fehl → RETRY, nicht überspringen.** Ein 403/404 auf die erste URL ist kein Ergebnis. Die SERP liefert 5–10 organische Treffer — so viele wie nötig durchprobieren, bis mindestens 2 echte Wortzahlen vorliegen. Erst wenn ALLE Treffer der Top 10 fehlschlagen, ist „kein Benchmark verfügbar" eine ehrliche Aussage — und dann steht das explizit auf der Seite, nicht stillschweigend eine geschätzte Länge.
2. **Wortzahl wird programmatisch gemessen, nicht geschätzt.** Ein Skript zählt den sichtbaren Body-Text (von der H1 bis vor den CTA/Footer) — nicht die eigene Erinnerung an ungefähr geschriebene Länge. Vor jedem Redeploy neu zählen.
3. **Jede Seite bekommt den Wortzahl-Urteil-Satz aus Schritt 7/E2 — ausnahmslos, auch Nicht-Keyword-Seiten.** Bei Seiten ohne direkten Wettbewerb (Marken-/Mission-Seiten wie Über-mich, Philosophie) heißt das ehrliche Urteil: „kein Wettbewerbs-Keyword, Wortzahl ist hier nicht der Hebel" — das ersetzt NICHT das Vergleichs-mit-dem-eigenen-Bestand (Punkt 4), das bleibt Pflicht.
4. **Nie dünner als der Bestand.** Vor Deploy die neue Wortzahl gegen die Live-Seiten-Wortzahl aus Schritt 1 gegenprüfen (Skript, nicht Erinnerung). Unterschreitet der neue Text den Bestand, ist er nicht fertig — das ist die Lektion aus dem Suriya-Fall (Punkt I) UND ist bei Maria (Philosophie: 268 statt 294) trotz dieser dokumentierten Lektion erneut passiert.

**Selbst-Check vor „fertig": Kann ich für jede einzelne Seite eine Zeile wie „X Wörter eigene Seite vs. Y Wörter Bestand vs. Z Wörter Wettbewerber-Median, Quelle: <URL>, Datum: <Datum>" hinschreiben — mit echten Zahlen, nicht Schätzungen? Wenn nein, ist die Seite nicht fertig.**

## B · Harte Regeln

- **Nur echte Daten.** Volumina/Rankings/PAA/Wettbewerber aus DataForSEO. Fehlt eine Zahl: sagen, nicht raten.
  „0" bei DataForSEO = keine Daten, nicht keine Nachfrage.
- **Nur Aussagen, die auf den Kunden zutreffen.** Themen, die nicht vom Kunden kommen → „Vorschlag,
  abstimmen" markieren, nie als gesetzt (Regel 13, program-deliverable-rules).
- **HWG (Health):** kein Heilversprechen, keine Garantie. Relativierend („kann", „Ziel", „unterstützen",
  „wird in der Fachliteratur diskutiert", „ich prüfe individuell"). §12-Anlage prüfen (Migräne, Verspannung,
  Stress = nicht gelistet → ok). HWG-Box auf jede Seite: „ersetzt keine ärztliche Diagnose; Ergebnisse individuell".
  E-E-A-T voranstellen: echte Person + Qualifikation.
- **Harmonisch, nicht ausschließend.** Zielgruppen-Fokus (z. B. „Frauen 45–65") kommt aus der Positionierung,
  darf aber auf der Startseite NICHT exklusiv klingen („am liebsten Frauen" = unausgewogen).
  Formel: Schwerpunkt nennen + „genauso bist du hier richtig, wenn …".
- **Konsistente Ansprache** (du ODER Sie — nie gemischt). Deutsch, Ton wie die Praxis.
- **Kunden-Wissen nie erfinden:** Ausbildung/Jahre, Preise, Krankenkasse → gelber `[von Kunde bestätigen]`-Platzhalter.
- **Fertiges Produkt.** Vollständige Absätze, echte Copy — keine Stichpunkt-Snippets als „Text".

## C · Datenpaket (pro Seite)

| Feld | Quelle |
|---|---|
| Haupt-Keyword + Volumen (+ Difficulty) | DataForSEO `keywords_data/google_ads/search_volume` · Labs `keyword_overview` |
| Cluster-Keywords + Volumina | dito (national vs. lokal labeln) |
| Was die Domain schon rankt | DataForSEO Labs `ranked_keywords` |
| Top-3–5 SERP-Wettbewerber + deren Unterthemen | DataForSEO `serp/google/organic/live/advanced` (1 Task/Call; IP-Whitelist!) + Seite fetchen |
| Echte Nutzerfragen (People-Also-Ask) | dito, Items `people_also_ask` |
| Stadt + echtes Einzugsgebiet | 4-Stufen-Modell (Kern / große Nachbarn / 3. Ort / Kleinorte nur im Text) |
| Echte Leistungen / Methodennamen | Source of Truth |
| NAP (kanonisch, gelockt) | Source of Truth |
| Behandler:in + Qualifikation (E-E-A-T) | Fragebogen + `[bestätigen]`-Platzhalter |

## D · Seiten-Struktur (ERSTELLEN — genau so liefern)

1. **Ziel:** Haupt-Keyword (+Volumen) · Cluster-Keywords · Suchintention · URL-Slug
2. **Meta:** Title ≤60 Z. (Keyword vorn, Stadt, Marke) · Meta-Description ≤155 Z.
3. **Gliederung H1 → H2/H3**, gemappt auf Suchintention + Wettbewerber-Unterthemen + PAA. **Nur EINE H1.**
4. **GEO/KI-Layer:** Direkt-Antwort-Block (2–4 Sätze direkt unter H1, eigenständig zitierbar) ·
   Definitions-Box · FAQ aus echten PAA (je 2–3 Sätze, als FAQPage-Schema) · extrahierbare Fakten
   (wer/wo/wann/Preis falls öffentlich) · explizite Entitäten (Methoden, Beschwerden, Stadt/Umland)
5. **Body je Abschnitt:** vollständige Copy in echter Stimme, Thema komplett, E-E-A-T rein.
   Bewährte Startseiten-Blöcke: Hero + Direkt-Antwort · „Hier bist du richtig, wenn …" (Beschwerden-Liste) ·
   Leistungs-Säulen (je Absatz) · Für wen (harmonisch) · Über mich/Behandler:in · So läuft der erste Termin ·
   Lokaler Abschnitt (Stadt + Umland) · FAQ · CTA · HWG-Box
6. **Schema (JSON-LD):** LocalBusiness/MedicalBusiness (NAP) + Service + FAQPage + Person
7. **Interne Links:** hoch zur Pillar-Seite, quer zu Schwester-Cluster-Seiten, + Über mich + Termin
8. **Lokale Signale:** Stadt/Umland natürlich im Text; NAP identisch zum gelockten Datensatz
9. **Bilder:** echte Fotos (Behandler:in, Praxis innen/außen, Behandlung), Alt-Texte mit Leistung + Stadt, WebP

## D2 · Content-Elemente statt Fließtext (blockierend, seit 14.09.2026)

Jeder Abschnitt, dessen Inhalt von Natur aus eine Aufzählung, ein Ablauf oder ein Vergleich ist, wird als
echtes HTML-/Design-Element gebaut — NICHT als Komma- oder Punkt-Aufzählung in einem `<p>`-Fließtext.
Ein moderner Seiten-Layout (Header/Hero/Footer, siehe G) ohne strukturierte Inhalts-Elemente ist nur
halb fertig — die Optik stimmt, der Inhalt bleibt trotzdem ein Report-Absatz.

**Erkennungsmuster → Element (1:1-Zuordnung, immer prüfen bevor ein Absatz geschrieben wird):**
- Aufzählung von Eigenschaften/Vorteilen (auch wenn im Entwurf nur mit „•“/`<br>` getrennt) → `<ul class="check-list">`
- Mehrere gleichartige Kategorien mit je einem Icon/Kernbegriff (z. B. 5 Elemente, Methoden-Quellen, Leistungs-Hebel) → `.el-grid` mit `.el-card` (Icon + Titel + 1 Satz)
- Ein Ablauf mit fester Reihenfolge (z. B. „So läuft die Beratung ab“, Prozess in n Schritten) → `.step-flow` mit nummerierten `.step`
- Eine feste Matrix/ein Raster (z. B. Bagua-Neun-Felder) → `.area-grid` (3×3) oder passendes Grid
- Eine einzelne, auffällige Zahl/Statistik im Fließtext (z. B. „71.000 Kleingärten“) → `.stat-badge`
- Vergleichstabellen (Wortzahl-Urteil, Preis-Übersicht) → `<table>` in `.cmp-wrap` (schon Standard)

**Warum:** Eine Kunden-Website mit modernem Layout nutzt für genau diese Inhalte reale Web-Elemente,
kein Fließtext-Dokument. Ein Prüf-Layout, das nur Farben/Fonts kopiert, aber Inhalte weiter als Absätze
zeigt, wirkt wie ein Report, nicht wie eine Seite (Maria-Brasse-Vorfall, 14.09.2026 — siehe Sektion J).

**Nicht verändern:** Fakten, Zahlen, Reihenfolge und Wortlaut bleiben exakt wie im freigegebenen Text —
D2 ist reine Struktur-/Darstellungs-Änderung, keine Content-Überarbeitung. Erst Content nach D/A0 fertig
schreiben, dann D2 anwenden (Reihenfolge nicht umdrehen).

## E · Local-SEO-Mindestanforderungen (Startseite) — Checkliste

- [ ] **Hero über dem Falz** beantwortet in 3 Sekunden: Was? Wo? Wie buchen? (H1 mit Leistung + Stadt, sichtbares Telefon, „Termin buchen"-Button)
- [ ] **NAP im Header/Footer** exakt wie im Google-Profil und in allen Verzeichnissen
- [ ] **Google-Maps-Karte** interaktiv im unteren Bereich eingebettet
- [ ] **Lokaler Fokus** in H1, Title-Tag und Meta-Description (nicht nur im Text)
- [ ] **Ladezeit < 2 s** (Bilder WebP, Caching, mobil zuerst messen)
- [ ] **Mobile-First**: fehlerfrei bedienbar, keine zu kleinen Buttons, kein horizontales Scrollen
- [ ] **HTTPS/SSL** gültig
- [ ] **Sichtbare Google-Bewertungen/Sterne** auf der Startseite (oberes bis mittleres Drittel)
- [ ] **Echte Bilder statt Stockfotos** (Team, Inhaber:in, Praxis)
- [ ] **Klarer, farblich abgehobener CTA**, beim Scrollen immer erreichbar (sticky/mobil)
- [ ] **LocalBusiness-Schema (JSON-LD)** mit Öffnungszeiten, Leistungen, Adresse, Telefon

## E2 · Rote Punkte werden im Entwurf GELÖST, nicht nur geflaggt

Die Checkliste (E) ist kein Befund-Protokoll, sondern eine Bau-Anleitung: Jeder rote/gelbe Punkt wird
**direkt im gelieferten Entwurf gelöst** (Bewertungs-Sektion mit echtem Rating + Live-Widget, Maps-Einbettung
mit Code, Hero-Leiste Was/Wo/Buchen, genau eine H1, einheitliche Ansprache, CTA). Auf der Seite steht dann
✅ „im Entwurf gelöst" — mit dem Hinweis, dass die Live-Website erst bei der Umsetzung (nach Go) geändert wird.
Nur Dinge, die der Kunde liefern muss (Fotos, Ausbildung) oder erst bei Umsetzung passieren (WebP, Mobil-Test),
bleiben gelb.

**Wortzahl-Urteil immer schriftlich, mit Benchmark:** eigene Zahl · Bestandsseite · Marktführer (Platz 1) ·
stärkster Wettbewerber → klares „ausreichend / zu wenig" + Ziel-Korridor. Nie nur „auf Augenhöhe" sagen.

**Bewertungen:** immer echtes Rating/Anzahl (aus GBP/Local Falcon) + Live-Widget. Nie Zitate erfinden.

## F · Qualitäts-Checks vor Lieferung

- Wortzahl ≥ aktuelle Live-Seite und im Rahmen der Wettbewerber (Benchmark zeigen, nicht raten).
- Genau **eine H1**; H2/H3 sauber; FAQ als Schema.
- Ansprache einheitlich; keine exklusiven Formulierungen; HWG-Formulierungen; HWG-Box vorhanden.
- Name/NAP/Buchungs-URL = Source of Truth.
- Alle Kunden-Unbekannten als gelbe Platzhalter, nicht erfunden.
- Nur echte PAA/Volumina; Datenlücken benannt.

## G · Lieferung an den Kunden

- **Nichts an der Website ändern** bis zum expliziten Go (pro Änderung).
- Text auf **eigener, lesbarer Seite** (741-CI, echtes Logo) — NICHT in ein enges In-Karten-Fenster.
  Aus dem **Seitenbaum-Report** per Klick auf die Seite verlinkt („📄 Fertigen Text öffnen"). Kein extra Report-Eintrag nötig.
- Pro Abschnitt **✓ Passt / 💬** + **Gesamt-Freigabe** (report_feedback, eigener Slug je Seite).
- Technik (Meta, Alt, Schema, Keywords) eingeklappt am Ende — für 741, nicht Teil des sichtbaren Textes.
- Anforderungs-Checkliste (E) mit Status ✅/🟡/🔴 gegen die Live-Seite auf der Seite zeigen.

## H · PRÜFEN-Modus (bestehende Seite bewerten)

0–100 je Dimension mit Beleg-Zitat: Suchintention · thematische Tiefe · GEO-Extrahierbarkeit · E-E-A-T ·
lokale Signale · technisches On-Page (Title/Meta/H) · Schema · interne Verlinkung.
Dann Gesamt-Urteil + priorisierte Lücken-&-Fix-Liste (größter Hebel zuerst, jeder Fix konkret + Dimension).

## I · Lessons (Suriya, nicht wiederholen)

- Erst Live-Seite + Wettbewerber prüfen — der erste Entwurf (828 W.) war dünner als die Bestandsseite (1.329 W.).
- Zielgruppen-Fokus nicht 1:1 als exklusiven Satz auf die Home.
- Snippets ≠ Text. Immer die fertige Copy.
- In-Karten-Accordion ist zu eng → eigene Seite.
- Tiefe war nicht die Lücke; Reviews auf der Home, Maps, 1×H1, WebP waren es. Benchmark zeigt das.
- **Bestehende FAQ des Kunden NIE ersetzen.** Sie kommen aus echter Patientenerfahrung und beantworten oft
  schon offene Punkte (bei Suriya: Kosten/Krankenkasse + Ablauf erster Termin standen schon auf der Seite —
  ich hatte sie als Platzhalter markiert). Regel: bestehende Fragen 1:1 übernehmen (Ansprache vereinheitlichen,
  HWG-glätten), echte PAA-Fragen nur ERGÄNZEN. Gilt für alle Bestands-Inhalte: erst lesen, dann schreiben.

## J · Lessons (Maria Brasse, 13.09.2026 — nicht wiederholen)

- 8 von 9 Leistungsseiten wurden ohne funktionierenden Wettbewerber-Benchmark geschrieben: 2 fehlgeschlagene Fetches (403/404) wurden als „kein Benchmark" akzeptiert, statt die übrigen 4–8 SERP-Treffer durchzuprobieren. Erst auf explizite Nachfrage des Kunden nachgeholt → echte Mediane lagen bei 964–4.198 Wörtern, die gelieferten Seiten bei 268–650. Siehe Gate A0.1.
- Selbst wo ein Benchmark vorlag (Büro: 1.591/879 W.), wurde er nicht als verbindliches Minimum behandelt, sondern als Kontext — die gelieferte Seite blieb bei ~550 W. Siehe Gate A0.4.
- Die eigene Wortzahl-Selbstauskunft im Gespräch war grober/optimistischer als eine programmatische Nachzählung (Differenzen von 100–150 Wörtern durch mitgezählte Intro-Boilerplate). Siehe Gate A0.2.
- Eine überarbeitete Seite (Philosophie) landete nach der „Verbesserung" unter der Wortzahl des Kunden-Bestands (268 vs. 294) — exakt die in Punkt I dokumentierte Suriya-Lektion, trotzdem wiederholt, weil nicht programmatisch gegengecheckt wurde. Siehe Gate A0.4.
- Lokale Signale (Regel D.8) wurden nur als Erwähnung im Meta-Bereich abgehakt („Berlin" in der Adresszeile), nicht als echte, texturierte Lokalisierung im Fließtext. Erst nach Kritik wurde z. B. für Berlin die reale, verifizierte Kleingarten-Statistik (71.000 Kleingärten, 800+ Anlagen, Quelle: berlin.de-Kleingartenentwicklungsplan) eingebaut. Lehre: „Stadt im Text erwähnen" heißt echte lokale Textur, kein Namedropping.
- Freigabe-Seiten liefen im 741-Dashboard-CI (Regel G), obwohl der `behandler-seite`-Skill seit Längerem explizit „CI des Kunden, nicht 741-CI" vorschreibt — die beiden Standards widersprechen sich, und die ältere/laxere Fassung wurde befolgt. **Ungeklärt, wartet auf Martins Entscheidung:** Freigabe-Seiten künftig im jeweiligen Kunden-CI bauen (Farben/Fonts per `getComputedStyle` von der Live-Seite, nicht raten) — analog zum Vorgehen im `behandler-seite`-Skill.

## K · Lessons (Maria Brasse, 14.09.2026 — nicht wiederholen)

- Nachdem Punkt J's CI-Frage (echtes Kunden-CI statt 741-CI) gelöst war, blieb das Seiten-**Layout** trotzdem
  eine flache Report-Optik ohne echten Header/Nav/Hero/Footer — CI-Farben/Fonts stimmten, die Struktur einer
  echten Website fehlte weiterhin, auf Desktop wie Mobile. Fix: reales Header-/Nav-/Hero-/Footer-Markup der
  Kunden-Live-Seite per `getComputedStyle` + DOM-Read extrahieren und als Website-Shell um den Report-Content
  legen (Mobile-Hamburger inklusive). Lehre: CI-Konformität (Farbe/Font) und Layout-Konformität (Struktur)
  sind zwei getrennte Prüfpunkte — eine Seite kann bei Ersterem grün und bei Letzterem trotzdem rot sein.
- Selbst nach dem Layout-Fix war der Seiten-**Inhalt** weiterhin reiner Fließtext: Dinge, die von Natur aus
  Aufzählungen, Abläufe oder Raster sind (5 Elemente, Bagua-9-Felder, 5-Schritte-Prozess, Preis-Faktoren),
  standen als Komma-/Punkt-Listen in `<p>`-Absätzen statt als echte Web-Elemente. Erst auf explizite Nachfrage
  gefixt → neue Sektion D2 + wiederverwendbare CSS-Klassen (`.el-grid`/`.el-card`, `.step-flow`/`.step`,
  `.check-list`, `.area-grid`, `.stat-badge`) in `00_project/maria-brasse-pages/tpl-css.html`. Lehre: „modernes
  Layout“ heißt Struktur UND Content-Darstellung — ein neuer Header ersetzt keine Content-Elemente, und
  umgekehrt. Beide Prüfpunkte gehören ab sofort in jede Leistungsseiten-Lieferung (siehe D2).

Verwandt: [[client-structure-page-playbook]], [[hwg-fallstudien-guideline]], [[program-deliverable-rules]], [[stammdatenblatt-rollout]], [[page-content-qa-checklist]], `.claude/skills/behandler-seite/SKILL.md`.
