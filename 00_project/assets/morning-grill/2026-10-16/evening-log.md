# Evening log 2026-10-16 (WITA) · draft 18:00 · status: draft

Sources since the morning bookmark: S1–S13, Supabase `work_items`, `clients`, git log, FTP live state.
Time zone: WITA (UTC+8). Local time: 18:00.

## 1. Roadmap — where each client stands
| Client | Phase | Week | Track | Next step |
|---|---|---|---|---|
| STÜRZL Steuerstrafrecht | P1 Onboarding | 1 | ON | Outbound update email (Anja, Jilg, Glogger) with dashboard access + Startseiten-Konzepte + Compliance text |
| Katharina Kisser | Maintenance / Recovery | – | ON | Cleaned 3-byte malware dropper & 27 spam/casino posts; frontend 228 KB restored; client debrief |
| Maria Brasse (ShuiGuru) | P4 Build-up | 5 | ON | Live copy & FAQ verified on /ueber-mich-maria-brasse/ and /feng-shui-garten/; digest ready |
| Praxis Suriya | P4 Build-up | 6 | OFF (5 overdue portal tasks) | Dinakar assigned footer legal links (Impressum + Datenschutz); Tantri to verify 28 directory links |
| Praxis Hüwel | P4 Build-up | 8 | ON | GA4 key events created & verified live (phone_click, email_click, whatsapp_click, generate_lead) |
| Daniela Dumann | P4 Build-up | 5 | ON | Wave 1 approval cards released to dashboard; waiting for Wix-publish on 3 subpages |
| Bali Healing | P1 Onboarding | 5 | WAITING (Google NIB check) | Identity verification review pending; GoPay Ads top-up reminder |
| me&you / Pauspapier | P4 Build-up | – | ON | Standalone GitHub repository & deploy workflow created; Loom recording & DNS switch next |
| Kamil (Physio Anatomie + Kraft) | P6 Proof + Quarter | – | ON | Physiotherapiekraft.de analysis & Oberhausen scan done; waiting on yearly security offer decision |
| Johni Jaya Motor | P1 Onboarding | 9 | RE-PLAN | Re-plan of 25 overdue tasks; Local Falcon connector setup |

---

## 2. What was done today (2026-10-16)

### 1. Katharina Kisser (Akut-Rettung Website-Ausfall & Weiße Bar beseitigt)
- **Problem 1 (Website offline):** Blanker Bildschirm / 3-Byte UTF-8 BOM Response auf `https://katharinakisser.at/`.
- **Problem 2 (Weiße Bar unter Menü):** Auffälliger weißer Balken (100px+) zwischen rotem Menü und Hero-Slider auf Desktop und Mobile.
- **Root Cause & Fix:** 
  - Maliziösen Dropper in `public_html/index.php` (Zeitstempel 06:49:51 UTC) isoliert und durch saubere WordPress Core `index.php` ersetzt.
  - **Ursache der weißen Bar:** Die Angreifer hatten 20.775 Bytes versteckten Spam-Code (`data-seo-links-block`) direkt in den regulären `post_content` der Startseite (ID 1871) injiziert. Da die Startseite rein im GoodLayers PageBuilder aufgebaut ist, muss `post_content` leer sein. Durch den injizierten Inhalt triggerte das Theme `Infinite` automatisch den Standard-Container `.infinite-content-area` mit 60px Top- und 40px Bottom-Padding (100px leere weiße Box).
  - Datenbank-Bereinigung durchgeführt: `post_content` der Startseite geleert sowie 41 weitere infizierte Unterseiten/Revisionen restlos bereinigt.
  - WP Rocket Cache geleert.
  - **Verifikation:** Auf Desktop (1440x900) und Mobile (375x812) via Browser verifiziert: Der Hero-Slider schließt wieder bündig an die rote Menüleiste an. Die weiße Bar ist vollständig verschwunden.

### 2. Team & Portal: Dinakar Onboarding & Portal Release 9
- **Dinakar Supabase Setup:**
  - Password Reset & Bestätigung auf `Dinakar741!Studio#2026` via Supabase API durchgeführt.
  - Rolle `delivery` geprüft und Praxis Suriya Footer-Task zugewiesen.
- **Kundenportal Englisch-Lokalisierung (Release 9):**
  - Tab „Kundenarbeit“ komplett ins Englische übersetzt (KPI Cards, Tabellenköpfe, Drawer, Age-Formatting, Status-Pills).
  - Live deployed auf `clients.741.studio` via FTP (Backup: `backup-before-release9.html`).
  - Mit Headless Chrome Subagent verifiziert (Login als Dinakar, reaktives DE/EN Umschalten).

### 3. Maria Brasse (ShuiGuru)
- **Live-Updates via Novamira REST API:**
  - Neue FAQ-Abschnitte auf `/ueber-mich-maria-brasse/` („Was macht eine Feng-Shui-Beraterin?“) und `/feng-shui-garten/` („Wie schütze ich meinen Garten vor den Blicken der Nachbarn?“) integriert.
  - Schema.org FAQPage Strukturdaten hinterlegt.
  - Desktop- und Mobile-Screenshots zur Verifikation erstellt und committet (`a5a6cb9`).
  - Tages-Update E-Mail-Entwurf liegt versandfertig bereit.

### 4. Praxis Hüwel
- **GA4 Key Events:**
  - `phone_click`, `email_click`, `whatsapp_click`, `generate_lead` als Schlüsselereignisse in GA4 eingerichtet und live verifiziert.
  - Client Feed aktualisiert und ins Portal eingespielt (`951a3dd`).

### 5. STÜRZL Steuerstrafrecht
- **Entscheidungskarte E3:** Auf Variante B entschieden und Stürzl-Karten im Portal freigegeben.
- **Compliance-Text:** Liegt vollständig im Content-Pool (`compliance.txt` und `.docx`) für die Abstimmung bereit.
- **Startseiten-Konzepte:** CRO-Prototypen (Variante A & B) im Review-Status.

### 6. me&you / Pauspapier
- Standalone-Repo mit GitHub Actions Deployment-Pipeline für `meandyou.de` aufgesetzt (`deploy.yml`).
- DNS-Settings dokumentiert.

---

## 3. What is open / Blockers & Waiting-on
- **STÜRZL:** E-Mail-Versand an Anja Stürzl, Florentine Jilg und Maximilian Glogger mit Logins und Dashboard-Überblick ausstehend.
- **Praxis Suriya:** Dinakar arbeitet an Footer-Links; Tantri wartet auf Freigabe der 28 Verifizierungslinks.
- **Daniela Dumann:** Martin Wix-Publish Klick für 3 gespeicherte Unterseiten-Fixes offen.
- **Bali Healing:** Wartet auf Google Überprüfung der NIB-Verifizierung; Ads-Guthaben muss via GoPay nachgeladen werden.
- **me&you:** Martin Loom-Video & Freigabe zur DNS-Umschaltung.
