# Dataset — 741 KI-Website, Landingpage (Stand 2026-10-13)
Quellen: Hüwel-Repo und -Anleitung (`~/huewel-site/ANLEITUNG.md`, `AGENTS.md`, `.github/workflows/pruefung.yml`), Konzept `huewel-selbstpflege-konzept.md` (Worktree dazzling-bhabha), Memory (huewel-website-live-state, huewel-repo-ai-rules, huewel-onlyinside-ersatz), Live-Seiten praxis-huewel.de und 741.studio (Chrome, headless Chrome), DataForSEO (Google Ads Suchvolumen, 2276/de), Google Autocomplete, Martin (Grill-me 13.10.2026).

## 1. Aktuelle Seite (Section-Map)
Es gibt noch keine Seite für dieses Angebot. Nächste bestehende Seite: https://741.studio/de/pages/website-design.html · Title "Maßgeschneidertes Webdesign und -entwicklung | 741.Studio | Webflow, WordPress und benutzerdefinierter Code" · H1 "Wir bauen hochkonvertierende Website-Systeme" · H2: "Maßgeschneiderte Lösungen für jeden Technologie-Stack", "Verabschieden Sie sich von langsamen Vorlagen …", "Sind Sie bereit, Ihre Website für die Konvertierung neu zu gestalten?" (Sie-Form, kein KI-Bezug). Screenshot `02-data/741-website-design-1440-first.png`.
Ein Text-Entwurf ohne Workflow liegt vor (`../../ki-website-landingpage/content-v2.md`, `sections.html`, du-Form). Er ist Eingabe für Step 3, keine freigegebene Copy.

### 1.1 Technischer Zustand
Neue Seite. Zielpfad `/de/pages/ki-website.html` (in den Build-Eingaben von `vite.config.ts`). Header/Footer/Consent als Partials. Buchungslink DE: https://cal.com/741-studio-simjzw/30min.

## 2. Fakten zum Produkt (mit Quelle)
| # | Fakt | Quelle |
| --- | --- | --- |
| F1 | Hüwel-Website live seit 06.10.2026 unter www.praxis-huewel.de, gehostet auf GitHub Pages, Hosting-Kosten 0 € | Memory huewel-website-live-state; Konzept §6 |
| F2 | Gemessen 13.10.2026 in Chrome (Standort Bali): größtes Element nach 1,3 s geladen, 6 Anfragen, 0 fremde Skripte (nur eigene embeds.js, forms.js), CLS 0 | 741-Messung (PerformanceObserver) |
| F3 | Der Kunde ändert die Seite per Chat mit seiner eigenen KI (ChatGPT, bestehendes Plus-Konto). Die KI ändert eine Kopie, nie die Live-Seite | ANLEITUNG.md Teil 1–2 |
| F4 | Feste Regeln für die KI: AGENTS.md (Frage-Protokoll vor jeder Änderung), DESIGN.md (gesperrte Farben, Schriften, Bausteine) | Memory huewel-repo-ai-rules |
| F5 | Automatische Prüfung bei jeder Änderung blockt: Löschungen, fremde Skripte/Schriften/iframes, `<style>`-Blöcke, Seiten ohne Sitemap-Eintrag, Bildnamen/-größe, HWG-Risikowörter, kaputte Links/Bilder, SEO-Fehler | Memory huewel-repo-ai-rules, `pruefung.yml` |
| F6 | 741 gibt jede Änderung frei, bevor sie live geht. Jede Version bleibt gespeichert und lässt sich in wenigen Minuten zurückholen | ANLEITUNG.md "Gut zu wissen" |
| F7 | Einmalige Einrichtung ca. 15 Minuten, zusammen mit 741, nichts zu installieren | ANLEITUNG.md Teil 1 |
| F8 | Formulare über eigenes Backend (Supabase + Resend), Mails vom Praxis-Absender; 58 Kontakte aus dem alten Tool übernommen. Newsletter/Kontakte im Portal sind bei Hüwel noch Staging | Memory huewel-website-live-state, huewel-onlyinside-ersatz |
| F9 | JSON-LD auf allen Seiten, 88 alte Adressen weitergeleitet, eigene 404-Seite | Memory huewel-website-live-state |
| F10 | Altes System (ONLY INSIDE) kostete 2.000 € pro Jahr, ohne weitere Abos | Martin, Grill-me 13.10.2026 |
| F11 | 741 bietet 24/7 Hilfe (Zusage von Martin) | Martin, Grill-me 13.10.2026 |
| F12 | Praxis Hüwel darf als Referenz mit Namen genannt werden | Martin, Grill-me 13.10.2026 |
| F13 | Nach Freigabe ist eine Änderung in ein bis zwei Minuten live (GitHub-Pages-Deploy) | Konzept §4.7 |
| F14 | Domain und E-Mail liegen weiter bei ONLY INSIDE (laufen separat) | Hüwel README.md, Memory |

## 3. Google-Unternehmensprofil
Kein eigenes Profil für diese Produktseite (Seite von 741.studio). Keine Daten, Grund: Produkt-Landingpage, kein lokales Geschäft.

## 4. Bewertungen
Keine Bewertungen zum Produkt KI-Website. Keine Daten, Grund: Produkt seit 06.10.2026 bei einem Kunden live. `[FEHLT: Stimme von Martin Hüwel zur neuen Website, mit Erlaubnis]`.

## 5. Suchnachfrage (DataForSEO Google Ads, 2276/de, 13.10.2026, Kosten 0,09 USD)
| Keyword | Volumen | CPC € | Wettbewerb |
| --- | --- | --- | --- |
| website mit ki erstellen | 1.300 | 13,32 | HIGH |
| ki website | 1.300 | 6,07 | MEDIUM |
| ki website erstellen | 1.000 | 13,23 | HIGH |
| homepage erstellen lassen | 720 | 19,59 | HIGH |
| wordpress alternative | 480 | 4,80 | MEDIUM |
| website erstellen lassen kosten | 480 | 11,22 | MEDIUM |
| wix alternative | 140 | 4,64 | HIGH |
| website hosting kostenlos | 110 | 8,12 | HIGH |
| webdesign heilpraktiker | 70 | 11,16 | MEDIUM |
| website mit chatgpt erstellen | 70 | 7,11 | HIGH |
| chatgpt website erstellen | 70 | 8,60 | HIGH |
| jimdo alternative | 70 | 3,78 | HIGH |
| website für heilpraktiker | 50 | 6,61 | MEDIUM |
| ki homepage | 30 | 9,10 | HIGH |
| website ladezeit verbessern | 30 | 3,71 | MEDIUM |
Ohne Volumen (Tool liefert nichts): website selbst ändern, website ohne baukasten, website ohne abo, website mit chatgpt bearbeiten. Rohdaten `02-data/volume.json`.
**Autocomplete (Google, de, 13.10.2026)** belegt Nachfrage trotzdem: "website mit ki erstellen lassen", "website mit ki erstellen erfahrungen", "website mit ki erstellen claude", "website baukasten ohne abo", "website erstellen ohne abo", "website selbst pflegen", "website erstellen und pflegen lassen", "website für heilpraktiker erstellen". Rohdaten `02-data/autocomplete.json`.
Hinweis Suchintention: "ki website erstellen" sucht oft Baukasten-Generatoren (Autocomplete "ki website builder", "generator"). Unser Angebot ist "erstellen lassen + selbst per KI pflegen". Die Seite muss den Unterschied im ersten Bildschirm klar machen.

## 6. Aktuelle Rankings
Keine Daten, Grund: Seite existiert noch nicht.

## 7. Konflikte und Compliance
| # | Fund | Quelle | Behandlung im Prototyp |
| --- | --- | --- | --- |
| K1 | "2.000 € gespart" wäre falsch: Domain und E-Mail kosten weiter (F14) | Martin, README | Nur "Hosting 0 € statt 2.000 € Abo im Jahr" |
| K2 | "Deine Website gehört dir" nicht belegt: Repo liegt im 741-GitHub-Konto (martin741studio/martihuewel) | Memory huewel-repo-ai-rules | Aussage weglassen |
| K3 | Newsletter/Kontakte bei Hüwel nur Staging | F8 | nur "auf Wunsch" |
| K4 | 1,3 s ist eine Einzelmessung von Bali aus | F2 | immer mit Datum und "gemessen" nennen |
| K5 | "24/7 Hilfe von 741" ist eine Zusage | F11 | Martin hat sie bestätigt; Bereitschaft muss dazu passen (Handoff) |
| K6 | Kunde braucht ein KI-Konto (bei Hüwel ChatGPT Plus) | F3 | "Ein ChatGPT-Plus-Konto reicht" ehrlich nennen, keine "kostenlos"-Aussage zur KI |
| K7 | Beispiele aus Gesundheitsberufen | — | HWG-sicher, keine Heilaussagen; die Prüfung erkennt HWG-Wörter (F5) |

## 8. Bestehende 741-Daten
Konzept Selbstpflege (Seitenmodell, Blöcke, KI-Kosten pro Aktion 1,4–2,8 Cent, Stand 25.09.2026), ANLEITUNG.md (Kundensicht), Hüwel-Chat (Sidebar "🩺 Martin Hüwel / Praxis Hüwel"). Interne Links: /de/pages/website-design.html, /de/pages/local-seo.html, /de/pages/wachstums-abo.html, /de/pages/about.html, /de/pages/portfolio_full.html.

## 9. Brand, Foto, Logo
→ `02-data/brand.md`, `01-input/INVENTORY.md`.

## 10. Offene Punkte [FEHLT]
1. `[FEHLT: Stimme Hüwel]` Ein Satz von Martin Hüwel zur neuen Website, mit Erlaubnis.
2. `[FEHLT: Preis]` Preis des Angebots: nicht auf der Seite (Regel: Zahlen nur im Call).
3. `[FEHLT: 24/7-Kanal]` Über welchen Kanal die 24/7 Hilfe läuft (WhatsApp, Portal-Chat, Telefon).

## 11. Step-1-Zeilen (Gate)
| Zeile | Stand |
| --- | --- |
| 1.0 Content-Pool | keine Daten, Grund: Produktseite von 741, kein Kunden-Pool; Nachfrage direkt erhoben (Abschnitt 5) |
| 1.1 Aktuelle Seite | keine eigene Seite; nächste Seite website-design.html erfasst (Abschnitt 1) |
| 1.2 Screenshots | `02-data/741-de-home-1440-first.png`, `741-website-design-1440-first.png`, Hüwel-Screens in `01-input/` |
| 1.3 First-Screen-Check | Live-Startseite 741: H1 53 px, CTA im ersten Bildschirm (Screenshot) |
| 1.4 Struktur | interne Zielseiten Abschnitt 8 |
| 1.5 Suchnachfrage | Abschnitt 5 |
| 1.6 Rankings | keine Daten, Grund: neue Seite |
| 1.7 GBP | keine Daten, Grund: Produktseite |
| 1.8 Bewertungen | keine Daten, Grund: Produkt neu; [FEHLT: Stimme Hüwel] |
| 1.9 741-Daten | Abschnitt 2 und 8 |
| 1.11 Assets | Logo 982 px (≥800), Foto, Hüwel-Screens: `01-input/INVENTORY.md` |
