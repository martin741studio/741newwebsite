# Spezifikation: Neues Tally-Bewerbungsformular

**Projekt:** Marcel Rosenbach (`deep-nlp.com`) · Growth-Identity-Coaching  
**Typ:** Qualifizierungs- & Bewerbungsformular (Multi-Step / One Question Per Page)  
**Ziel-URL nach Abschluss:** `https://deep-nlp.com/grow-now`  

---

## 1. Globale Formular-Einstellungen (Tally Settings)

| Einstellung | Wert | Rationale / Quelle |
|---|---|---|
| **Form Title (Intern & Extern)** | `Deine Chance auf ein persönliches Money-Coaching` | Briefing & Referenztexte |
| **Subtitle / Einleitung** | `Nur wenige Plätze verfügbar. Zeig mir, wo Du finanziell stehst und wo Du hinwillst!` | Briefing |
| **Formular-Layout** | Centered, Minimal, Light Background (`#FFFFFF` oder `#FAFAFA`) | Referenz & Screenshot |
| **Fortschrittsanzeige (Progress bar)** | **Aktiviert: Seitenzahl / Page Indicator (z.B. "Seite 1 von 6")** | Briefing fordert explizit reale Seitenzahl |
| **Button-Beschriftung Seiten 1–5** | `Weiter →` | Hohe Usability |
| **Button-Beschriftung Seite 6 (Absenden)** | `Bewerbung jetzt absenden 🚀` | Klarer Call to Action |
| **Redirect on completion** | **AKTIVIERT** &rarr; `https://deep-nlp.com/grow-now` | **HARD RULE:** Pflichtfeld, darf nicht leer sein! |
| **E-Mail-Benachrichtigung an Marcel/Team** | Optional / Self-Notification an `kontakt@marcel-rosenbach.de` | Back-Up neben Zapier |

---

## 2. Seiten- & Fragen-Struktur (Exakt 1 Frage pro Seite + Kontaktdaten)

### Seite 1: Aktuelle Situation
- **Typ:** Multiple Choice / Einfachauswahl (**Nur 1 Antwort erlaubt**)
- **Fragentext:**  
  `1. Welche Situation beschreibt Dich aktuell am besten?`
- **Pflichtfeld:** Ja
- **Optionen (wortgetreu):**
  1. `Selbstständig / Unternehmer`
  2. `Führungskraft / leitender Angestellter`
  3. `Angestellt und möchte mehr verdienen`
  4. `Im Aufbau einer Selbstständigkeit`
  5. `Sonstiges`

---

### Seite 2: Einkommensziel in 12 Monaten
- **Typ:** Multiple Choice / Einfachauswahl (**Nur 1 Antwort erlaubt**)
- **Fragentext:**  
  `2. Welches monatliche Einkommen oder welchen Umsatz möchtest Du in den nächsten 12 Monaten erreichen?`
- **Pflichtfeld:** Ja
- **Optionen (wortgetreu):**
  1. `5.000 €`
  2. `10.000 €`
  3. `20.000 €`
  4. `50.000 €`
  5. `100.000 € oder mehr`

---

### Seite 3: Finanzielle Hindernisse
- **Typ:** Multiple Choice / **Mehrfachauswahl** (Checkboxes: mehrere Antworten möglich)
- **Fragentext:**  
  `3. Was hält Dich aktuell am stärksten davon ab, finanziell mehr zu erreichen? Kreuze gern mehrere Punkte an!`
- **Pflichtfeld:** Ja (mindestens 1 Auswahl)
- **Optionen (wortgetreu):**
  1. `Ich denke oft zu klein über Geld und meine Möglichkeiten`
  2. `Ich verkaufe mich oder meine Leistung unter Wert`
  3. `Ich vermeide wichtige Verkaufs- oder Umsatz-Aktivitäten`
  4. `Ich habe Angst vor Ablehnung oder finanziellen Risiken`
  5. `Ich weiß nicht, wie ich den nächsten Einkommens-Sprung schaffen soll`
  6. `Ich will neue Wege öffnen, mehr Einkommen zu generieren`

---

### Seite 4: Konkrete Veränderung bei Einkommensverdopplung
- **Typ:** Long Text / Freitext (Mehrzeilig)
- **Fragentext:**  
  `4. Wenn Du Dein Einkommen verdoppeln würdest: Was würde sich dadurch konkret in Deinem Leben verändern? Notiere 2-3 Punkte.`
- **Placeholder:** `Z.B. Mehr finanzielle Freiheit für meine Familie, Ausbau meines Unternehmens, weniger Existenzsorgen...`
- **Pflichtfeld:** Ja

---

### Seite 5: Veränderungsbereitschaft
- **Typ:** Multiple Choice / Einfachauswahl (**Nur 1 Antwort erlaubt**)
- **Fragentext:**  
  `5. Wie bereit bist Du, Deine bisherigen Denk- und Verhaltensmuster rund um Geld aktiv zu verändern?`
- **Pflichtfeld:** Ja
- **Optionen (wortgetreu):**
  1. `ZU 110%! Ich will finanziell richtig durchstarten.`
  2. `VOLLER ENERGIE! Ich bin bereit für mein nächstes Money-Level.`
  3. `MOTIVIERT! Ich will mein Money-Mindset verändern.`
  4. `INTERESSIERT! Ich bin aber noch etwas unsicher.`
  5. `NEUGIERIG! Ich will gern erst mal schauen.`

---

### Seite 6: Gemeinsame Kontaktseite
- **Seiten-Überschrift:**  
  `Deine Kontaktdaten für die Rückmeldung`
- **Einleitungstext:**  
  `Wenn Dein Profil für einen der Coaching-Plätze infrage kommt, melden wir uns persönlich bei Dir.`
- **Felder:**
  1. **Vorname**
     - Typ: Short Text
     - Label: `Vorname`
     - Pflichtfeld: Ja
  2. **Nachname**
     - Typ: Short Text
     - Label: `Nachname`
     - Pflichtfeld: Ja
     - *Hinweis Technik:* Getrennte Felder für Vor- und Nachname (verhindert Pipedrive-API-400-Fehler und KlickTipp-Fehlmapping).
  3. **E-Mail-Adresse**
     - Typ: Email
     - Label: `Deine beste E-Mail`
     - Pflichtfeld: Ja
  4. **Handynummer / WhatsApp**
     - Typ: Phone number
     - Label: `Deine Handynummer`
     - Pflichtfeld: Ja (internationale Validierung aktiv)
  5. **Datenschutzhinweis & Einwilligung**
     - Typ: Checkbox / Consent
     - Text: `Ich stimme der Verarbeitung meiner Daten gemäß der Datenschutzerklärung zu, damit Marcel und das Team mich bezüglich meiner Bewerbung kontaktieren können.`
     - Pflichtfeld: Ja

---

## 3. Einbettung auf `/more-money-now`

Das Formular wird über das Tally Embed Script als modales Popup über den Button eingebunden:
```html
<a href="https://tally.so/r/<FORM_ID>" 
   class="btn-apply" 
   data-tally-open="<FORM_ID>" 
   data-tally-layout="modal" 
   data-tally-width="680" 
   data-tally-auto-close="0">
  <span>Jetzt für 1zu1-Coaching bewerben!</span>
</a>
```
Sollte der Nutzer JavaScript blockieren, greift der direkte Fallback-Link auf `https://tally.so/r/<FORM_ID>`.
