# Master-Spezifikation: MMM-Anmeldung um Growth-Identity-Coaching erweitern

**Kunde:** Marcel Rosenbach (`deep-nlp.com`)  
**Datum:** 17.10.2026  
**Status:** Bereit zur Umsetzung in WordPress, Tally, Zapier, Pipedrive & KlickTipp  

---

## 1. Übersicht & Architektur

```text
[Bestehende MMM Landingpage]
https://deep-nlp.com/make-more-money-baby/ (UNVERÄNDERT)
               │
               ▼
[Bestehendes Tally-Formular 7RaKgP]
(Text-Update: "Aktuell die Chance auf ein kostenfreies Growth-Identity-Coaching. Reduzierte Plätze!")
(Redirect-Umstellung erst GANZ AM ENDE nach erfolgreichem Test)
               │
               ▼
[NEUE Danke-Seite 1] ───> https://deep-nlp.com/more-money-now
(Headline, Subline, Video-Platzhalter "NEUE IDENTITÄT, MEHR GELD?!", Button "Jetzt für 1zu1-Coaching bewerben!")
               │
               ▼
[NEUES Tally-Bewerbungsformular]
(5 Inhaltsfragen auf je 1 Seite + Seite 6 Kontaktdaten, Redirect: /grow-now)
               │
               ├─────────────────────────────────────────┐
               ▼                                         ▼
      [Zapier Automation]                        [NEUE Danke-Seite 2]
               │                                 https://deep-nlp.com/grow-now
       ┌───────┴───────┐                         (Marcel Foto, Bestätigung,
       ▼               ▼                          Aufgabe: Starte direkt mit MMM)
  [Pipedrive]     [KlickTipp]
  Pipeline:       Tag: Growth-Identity-Coaching
  GROW WITH NLP!  Sofort-Mail: 🙌🏼 Dein Growth-
  Phase 3:        Identity-Coaching - Next Steps
  Growth akt.
```

---

## 2. Fertiggestellte Artefakte & Vorlagen

Alle Code-Dateien und Vorlagen wurden im Projektordner vorbereitet:
- **Danke-Seite 1 HTML:** [`pages/more-money-now.html`](file:///Users/martindrendel/741website/00_project/assets/marcel/automation/mmm-growth-coaching/pages/more-money-now.html)
- **Danke-Seite 2 HTML:** [`pages/grow-now.html`](file:///Users/martindrendel/741website/00_project/assets/marcel/automation/mmm-growth-coaching/pages/grow-now.html)
- **Tally Formular-Spec:** [`tally-form-specification.md`](file:///Users/martindrendel/741website/00_project/assets/marcel/automation/mmm-growth-coaching/tally-form-specification.md)
- **Zapier & CRM-Spec:** [`zapier-automation-specification.md`](file:///Users/martindrendel/741website/00_project/assets/marcel/automation/mmm-growth-coaching/zapier-automation-specification.md)
- **Testplan & Gating:** [`test-plan-and-safety-protocol.md`](file:///Users/martindrendel/741website/00_project/assets/marcel/automation/mmm-growth-coaching/test-plan-and-safety-protocol.md)
