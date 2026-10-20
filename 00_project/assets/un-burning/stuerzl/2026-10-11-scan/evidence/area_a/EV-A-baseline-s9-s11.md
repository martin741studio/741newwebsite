## 9 · Zugänge & Eigentum (Stand 06.10.2026)

Quelle: Mail von Constantin Voss (constantin.voss@wearekemb.com, Agentur KEMB) an Anja vom 27.05.2025 (Screenshot von Martin). Nicht „Foss".
- GA4-Property **483853149** (von KEMB angelegt, Tracking seit Mai 2025); Anja wurde mit **anja.stuerzl@googlemail.com** hinzugefügt (Rolle unbekannt).
- Search Console: Domain-Property `sc-domain:stuerzl-steuerstrafrecht.de`; Voss hatte dort keine Rechte → **Herr Linkemann** hat die GSC vermutlich angelegt/verifiziert.
- Kanzlei-Mailadresse von Anja: stuerzl@stuerzl-steuerstrafrecht.de.
- Portal-Reports (Hash e006e37becd5): Ausgangsmessung (HTML) + „📝 Zusammenfassung Onboarding-Gespräch" (Viewer-Seite `onboarding-zusammenfassung-2026-10-06.html` mit pdf.js, PDF daneben). **PDFs nie direkt als storage_path eintragen** — der Report-Frame ist sandboxed und zeigt PDFs nicht an; immer eine Viewer-HTML davor.
- Ziel: Anja (bzw. ein Kanzlei-Google-Konto) = Inhaberin/Primary Owner von GBP Frankfurt + München, GA4-Konto, GSC, GTM-Konto, Hosting, Domain; 741studio18@gmail.com = Verwalter/Bearbeiter.

### Update 07.10.2026
- Constantin Voss (KEMB) hat Zugänge erteilt: **Google Tag Manager, Google-Unternehmensprofil, Google Analytics** (an 741studio18@gmail.com).
- Noch offen: Search Console (vermutlich Linkemann), Hosting/Domain-Angaben, Übersicht der KEMB-Arbeiten, Eigentümer-Check (ist Anja Hauptinhaberin/Admin?), Google Ads, Dashboard-Login.

### Neue Adressen Frankfurt (Mail Florentine Jilg, 07.10.2026)
- Zugang/Empfang, vor allem Post: **Wilhelm-Leuschner-Straße 23, 60329 Frankfurt**
- Meldeadresse + Eingang für Mandanten: **Untermainkai 26, 60329 Frankfurt am Main** → Vorschlag: kanonische NAP-Adresse (GBP, Impressum, Schema, anwalt.de, RAK, Verzeichnisse)
- Tiefgarage/Parken: Wilhelm-Leuschner-Straße 27-29, 60329 Frankfurt am Main, Plätze 148 und 146
- Alt (bis 05.10.2026): Wiesenhüttenstraße 17. Baseline-Scans 01.10. sind auf die alten Koordinaten zentriert (50.1044088, 8.6671099).
- Noch nicht umgestellt: Portal `locations`, GBP, Website, Schema, Report-Text. Erst nach Martins Go.


## 11 · Tracking-Check 09.10.2026 (GA4 483853149 + GTM-WFPFSTK2, als 741studio18)

Zugriff im Browser: Konto-Wechsel auf 741studio18 per `?authuser=1` (Standardkonto ist martin.stylectric → „Missing permissions").
- GA4 liefert echte Daten, 11.09.–08.10.: 226 aktive Nutzer, 191 neue. Sessions: Organic Search 316, Direct 127, Organic Social 16, AI Assistant 4, Referral 2, Unassigned 1. Länder: DE 213, CH 4.
- Events (28 Tage): page_view 1.320 · link_click 977 · user_engagement 632 · scroll 555 · menu_item_click 495 · session_start 466 · first_visit 191 · expand_sections 43 · **email_click 40 (32 Nutzer)** · **phone_click 19 (18 Nutzer)**.
- **Key Events: keine.** email_click/phone_click sind nicht als Conversion markiert.
- GTM: Container quality „Excellent", „sending data, no issues", Workspace Changes 0/0/0. Google-Tag G-FCG9RTJ1YQ + GT-PJ7PTX6P (7 Destinations, Inhalt ungeprüft).
- GA4-Auto-Insights: 28.09. nur 15 page_views statt 66 erwartet; Safari page_views/Woche 36 → 7; /team 27 → 7.
- Offen: Safari-Rückgang prüfen (Consent-Banner n3t?), Key Events setzen (nur mit Go), GBP/GSC/Ads noch ohne Zugang.
- Joomla: Konto martin@741.studio ist Gruppe „Administrator" (nicht Super User) → SP Page Builder Editor + Global Config liefern „Session mismatched"/403. Linkemann (adminmili) und Framotec sind Super Users. Hosting = Artfiles (212.53.214.189), nicht 741-Server.

### Update 09.10.2026 (nach Martins Go)
- **Key Events gesetzt** in GA4 483853149: `email_click`, `phone_click` (Toast „enabled as a key event"). Davor: nur Standard-Eintrag `purchase`, ohne Daten.
- Weitere Events in der Property: click, expand_sections, first_visit, form_start, form_submit (je <20, Herkunft unklar, NICHT als Key Event gesetzt), link_click, menu_item_click, on_page_navigation, page_view, scroll, session_start, user_engagement.
- **Safari ist kein Tracking-Bruch:** Safari = größter Browser (120 von 226 Nutzern, 2.608 Events, Engagement 66,8 %). Der Rückgang (page_views/Woche 36 → 7) ist ein Traffic-Rückgang. Hypothese (ungeprüft): Recruiting-Traffic (Seiten Team 488 Views, Join our Team 103; Stellenanzeigen auf LinkedIn/Kanzleiwelt/Uni Frankfurt).
- **GTM-Tags (9):** Consent Default, Consent Update, GA4 config, GA4 email click, Expand sections, Link clicks, Menu item clicks, On page navigation, Phone click. **Alle GA4-Tags feuern nur mit Analytics-Einwilligung** (Blocking Trigger „analytics consent is not given") → Zahlen = nur Einwilligende. Kein Google-Ads-Tag, kein Conversion Linker, kein Remarketing, kein Tag für Chat-Button/Formular.
- Nicht getrackt: Klick auf „Hier Online-Anfrage stellen" (Chat), Aufruf der Kontaktseite, Unterscheidung der Rufnummern (FFM/MUC/Notfall).

