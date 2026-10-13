# Portal-Antworten 13.10.2026 (Entwürfe, nichts gesendet)

Martin sendet jede Antwort selbst. Quelle: Supabase 741-portal, nur GET-Abfragen am 13.10.2026 (Tabellen `messages`, `access_grants`, `activity_log`, `emails_log`). Anrede: alle fünf Kunden duzen (geprüft an den gesendeten Portal-Mails).

**Wichtig:** Eine "Hilfe-Anfrage" im Standup ist kein Text. Es ist der Status `hilfe_angefragt` in `access_grants`. Der Kunde hat im Portal bei einem Zugang auf "Hilfe" geklickt. Es gibt keinen Fragetext. Nur Suriya hat eine echte Nachricht (`messages`).

Alle Entwürfe: `deslop_de.py` 5/5.

## 1. Praxis Suriya (Coralie)

**Was der Kunde wollte:**
• Nachricht (ungelesen): nur der Link `https://www.facebook.com/coraliesuriyapperuma`, Quelle `messages`, 06.09.2026 06:54, kein Text dazu.
• Hilfe-Anfrage: Google Tag Manager, Quelle `access_grants`, Status seit 12.08.2026.

**Fakten (Memory `praxis-suriya-client`):**
• Tag Manager Container GTM-K9MDDN7P liegt unter dem 741-Konto. Er ist seit 09.10. live über `mu-plugins/741-gtm.php`, Consent Mode default denied.
• Die Facebook-Seite steht schon im Footer und im Schema der Website.
• Harte Vorgaben von Coralie (13.10.): keine Backlink-/Disavow-Änderung, Backup vor Änderungen, keine Seitenadressen ändern. Der Entwurf berührt nichts davon.
• Martin entschied per Karte: Tag Manager erklären, dazu den Facebook-Link bestätigen.

**Entwurf:**

```text
Hallo Coralie,

danke für den Link zu deiner Facebook-Seite. Er ist da.

Beim Google Tag Manager musst du nichts tun. Den habe ich selbst für dich eingerichtet.

Auf deiner Website läuft dafür ein kleiner Messcode, der Formular-Anfragen und WhatsApp-Klicks zählt, aber erst dann, wenn ein Besucher im Cookie-Banner zustimmt. An Texten, Bildern und Seitenadressen hat sich nichts geändert.

Falls du Fragen hast oder den Messcode lieber nicht möchtest: Schreib mir kurz. Wir klären das, bevor ich irgendetwas anfasse.
```

**Hinweis für Martin:**
• Das Portal zeigt die Search Console bei Suriya weiter als "erteilt". Coralie hat den Zugang am 12.10. entfernt. Der Portalstatus ist veraltet.
• "Google Tag Manager" steht im Entwurf mit Namen, weil der Zugang im Portal so heißt und sie danach gefragt hat. Es ist kein Anbieter-Tool von 741.

## 2. Praxis Hüwel (Martin Hüwel)

**Was der Kunde wollte:** Hilfe-Anfrage zum Google Tag Manager. Quelle `access_grants`, Status seit 19.08.2026. Notiz im Portal: "Hüwel hat keinen GTM — 741 richtet den Container ein (bestätigt 18.08.2026)". Keine Nachricht im Thread.

**Fakten:**
• Memory `huewel-client`: GTM hatte er nie, 741 richtet ihn ein. GA4 und Search Console sind erteilt.
• Aktualisiert am 13.10. (Nachmittag): GA4 `G-4FP95Y92XY` läuft jetzt über `assets/js/consent.js` auf der Live-Seite, mit Consent Mode (erst nach Zustimmung). Es gibt keinen Tag Manager. Der Entwurf sagt deshalb: nicht nötig, das Messen läuft direkt.

**Entwurf:**

```text
Hallo Martin,

zum Google Tag Manager: Du musst dafür nichts tun. Du hast keinen, und du brauchst auch keinen.

Das Messen läuft seit Kurzem direkt über Google Analytics auf deiner neuen Website. Es startet erst, wenn ein Besucher im Cookie-Banner zustimmt.
```

**Hinweis für Martin:** Die frühere Messlücke ist geschlossen. GA4 läuft live über `consent.js`.

## 3. Naturheilpraxis Daniela Dumann

**Was der Kunde wollte:** 4 Hilfe-Anfragen, Quelle `access_grants`: Domain-Verwaltung (29.08.), Google Analytics GA4 (28.08.), Search Console (29.08.), Google Tag Manager (29.08.). Keine Nachricht von ihr im Thread. Letzte Nachricht im Thread ist die von 741 vom 01.10.2026.

**Fakten:**
• GA4 und Search Console sind seit 30.09. neu eingerichtet (Memory `dumann-client`). Das Google-Tag in Wix ist "Connected" auf allen Seiten. Die 01.10.-Nachricht hat ihr das schon gesagt. Die Portal-Flags sind also veraltet.
• Domain und Tag Manager: In keinem Memory-Eintrag braucht 741 diese Zugänge. Die Search-Console-Bestätigung lief über Wix, nicht über DNS.
• Die Seite `https://www.danieladumann.de/vortraege` zeigt am 13.10.: "Sanfte Entgiftung nach Hildegard" und "Vortrag Hildegard Ernährung" = Beendet. "Gesund durch die kalte Jahreszeit" beginnt am 21. Okt. Das ist die offene Frage von Martin vom 09.10., die noch nicht gestellt wurde. Martin entschied per Karte: als zweiter Absatz mitsenden.

**Entwurf:**

```text
Hallo Daniela,

zu deinen Hilfe-Anfragen im Portal: Du musst bei den Zugängen nichts mehr tun.

• Google Analytics und Search Console: Beides habe ich am 30.09. neu eingerichtet. Das Messen läuft seitdem auf allen Seiten deiner Website.
• Google Tag Manager: Den brauche ich aktuell nicht von dir.
• Domain-Verwaltung: Auch hier brauche ich aktuell nichts von dir. Sollte sich das ändern, melde ich mich und führe dich Schritt für Schritt durch.

Eine Frage zu deiner Seite „Vorträge": Zwei der drei Vorträge stehen dort auf „Beendet", nämlich „Sanfte Entgiftung nach Hildegard" und „Vortrag Hildegard Ernährung". Buchbar ist nur „Gesund durch die kalte Jahreszeit" am 21.10.

Kommen neue Vorträge dazu? Wenn nicht, schlage ich vor, die beendeten Karten auszublenden. Dann wirkt die Seite aktuell.
```

**Hinweis für Martin:** Nach dem Senden die 3 Zugangs-Flags im Portal auf "erteilt" oder "nicht nötig" setzen, sonst bleiben "3 fehlende Zugänge" im Standup stehen. Die Antwort ändert das nicht selbst.

## 4. Maria Brasse

**Was der Kunde wollte:** Hilfe-Anfrage zum Google Tag Manager. Quelle `access_grants`, Status seit 02.09.2026. Keine Nachricht im Thread.

**Fakten (Memory `maria-brasse-client`):**
• Auf shuiguru.de läuft Google Analytics direkt (`G-8B0M7DXENR`, MU-Plugin mit Consent-Banner), live seit 30.09. Es gibt keinen Tag Manager und 741 braucht keinen.
• Marias GA4-Zugang für das 741-Konto ist erteilt (`access_grants`).

**Entwurf:**

```text
Hallo Maria,

den Google Tag Manager brauchst du nicht. Du musst dafür nichts tun.

Das Messen deiner Website läuft seit dem 30.09. direkt über Google Analytics. Es startet erst, wenn ein Besucher im Cookie-Banner zustimmt. Der Zugang, den du mir dafür gegeben hast, reicht dafür aus.
```

## 5. Rabenmütter Shop (Franziska)

**Was der Kunde wollte:** Hilfe-Anfrage zur Domain-Verwaltung. Quelle `access_grants`, Status seit 30.08.2026. Keine Nachricht im Thread.

**Fakten (Memory `franziska-rabenmuetter-client`):**
• Die Shop-Domain `rabenmuetter-shop.com` wird von Shopify verwaltet. Der TXT-Eintrag für die Search Console steht dort seit 30.08.2026. Die Property ist verifiziert. Shopify-Staff-Zugang ist erteilt, 741 braucht keinen weiteren DNS-Zugang.
• Der Entwurf nennt keine Rechnungs- oder Zahlungsthemen.

**Entwurf:**

```text
Hallo Franziska,

bei der Domain-Verwaltung musst du nichts tun. Deine Shop-Domain läuft über Shopify. Den Eintrag für die Search Console habe ich dort schon am 30.08. gesetzt, und er ist bestätigt. Ich brauche keinen weiteren Zugang dafür.
```

## Offen / Folgeaufgaben (nicht in den Entwürfen)

• Portal-Flags nach dem Senden aktualisieren: Suriya GTM, Hüwel GTM, Dumann ×4, Maria GTM, Rabenmütter Domain. Das ist ein Portal-Schreibzugriff und braucht GO-PORTAL.
• Hüwel: Messcode auf der neuen Seite einbauen (Go nötig).
• Rabenmütter: Zugangsstatus "Konto & Stammdaten" ist der offene Onboarding-Schritt, nicht Teil dieser Antwort.
