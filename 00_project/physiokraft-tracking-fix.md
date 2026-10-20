# Fix: Tracking auf physiotherapiekraft.de (Physiokraft) — Angleichen an Anatomie

**Für:** Dinakar (Website-Edit)  ·  **Erstellt:** 2026-08-14  ·  **Kunde:** Kamil Böyük (Physiokraft + Physio Anatomie)

## Problem in einem Satz
physiotherapiekraft.de gibt im Google-Ads-Report ~5× höhere Kosten/Sitzung als physiotherapieoberhausen.com aus — **nicht weil die Ads schlecht sind, sondern weil das GA4-Tracking auf der Seite fast nichts erfasst.**

## Die Zahlen (Juli 2026, gleiches Ads-Konto, gleicher CPC €0,75)
| | Ad-Klicks | GA4 Paid-Sessions | Erfasst | Kosten/Paid-Session |
|---|---|---|---|---|
| Anatomie (physiotherapieoberhausen.com) | 1.530 | 780 | **51 %** | €1,47 |
| Physiokraft (physiotherapiekraft.de) | 1.630 | **112** | **7 %** | **€10,89** |

→ 93 % der bezahlten Klicks tauchen in GA4 nie auf.

## Ursache (im HTML beider Seiten verglichen)
Beide: WordPress + Elementor + **GTM-TBPCSH3W**.
- **Anatomie** hat ZUSÄTZLICH das Plugin **MonsterInsights** (google-analytics-for-wordpress), das den GA4-Tag **`G-LGVVEBHS8D` hart im `<head>` verdrahtet** (feuert sofort) — plus den **Google-Ads-Conversion-Tag `AW-16730108784`** (Telefon-Klick-Conversion).
- **Physiokraft** hat **nur** den GTM-Container, **kein** hartes gtag, **keinen** Ads-Conversion-Tag. GA4 wird nur über GTM (verzögert) geladen; auf einer 2× schwereren Seite (179 KB, ~2,1 s) mit 93 % Mobile-Traffic bouncen die Leute, bevor der Tag feuert.

## Fix (auf physiotherapiekraft.de, WordPress-Admin)
Beide Sites teilen sich EINE GA4-Property (468424260, Stream `G-LGVVEBHS8D`) — getrennt wird über den Hostnamen. Physiokraft soll dieselbe ID feuern wie Anatomie.

1. **MonsterInsights installieren & verbinden** (genau wie Anatomie):
   - Plugin „Google Analytics for WordPress (MonsterInsights)" installieren + aktivieren.
   - Mit der GA4-Property verbinden bzw. Measurement-ID **`G-LGVVEBHS8D`** eintragen (v4_id).
   - Das verdrahtet `gtag('config','G-LGVVEBHS8D')` hart in den `<head>` → sofortiges, zuverlässiges Tracking.
   - *Alternative wenn kein MonsterInsights gewünscht:* Site-Kit ODER manuell den `gtag.js`-Block aus Anatomies `<head>` 1:1 einsetzen (`<script src="//www.googletagmanager.com/gtag/js?id=G-LGVVEBHS8D" async></script>` + `gtag('config','G-LGVVEBHS8D')`).
2. **Google-Ads-Conversion-Tag ergänzen** (wie Anatomie): globaler Tag **`AW-16730108784`** + `gtag_report_conversion(...)` auf Telefon-/WhatsApp-Klick.
   - Anatomies Snippet: `gtag('event','conversion',{'send_to':'AW-16730108784/b4yGCN7nvtoZEPDmxKk-','event_callback':cb});`
   - ⚠️ **Conversion-Label** (`b4yGCN7…`) bei Kamils Media-Buyer bestätigen — ggf. eigenes Label für Physiokraft. Konto ist dasselbe (Kamil Physio 992-981-4093), daher AW-ID identisch.
3. **Verifizieren:** GA4 → Realtime öffnen, physiotherapiekraft.de aufrufen → eigener Aufruf muss als aktiver Nutzer erscheinen (hostName physiotherapiekraft.de). Tag Assistant „connected".

## Zusätzlich (Media-Buyer / Ads, nicht Website)
- **Landingpage:** Physiokraft-Kampagne zeigt aktuell auf die **Startseite `/`** (36 % Engagement). Anatomie zeigt auf **`/leistungen/`** (50–64 %). → Auf eine fokussierte Leistungsseite umstellen, z. B. `/leistungen/hausbesuche/`.
- **Netzwerk:** prüfen, ob Such-Partner/Display an sind (viele Billig-Klicks, hoher Bounce) → ggf. Search-only.
- **Speed:** Landingpage ist 179 KB / ~2 s → für Mobile abspecken.

## Danach
Sobald der Tag zuverlässig feuert, steigen Physiokrafts erfasste Sessions stark → Kosten/Sitzung fällt Richtung Anatomie-Niveau, und der Monatsreport (clients.741.studio, Kunde Kamil Böyük) zeigt die echten Zahlen. Key-Events (Formular/Anruf/WhatsApp) dann als GA4-Conversion markieren → echtes CAC.
