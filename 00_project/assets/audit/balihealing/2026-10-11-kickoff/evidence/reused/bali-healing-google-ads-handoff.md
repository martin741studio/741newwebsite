# TASK: Finish the Bali Healing Google Ads campaign (needs Google Ads UI access)

**Goal:** Launch a Google Ads Search campaign for Bali Healing Center, leading with **Ozone therapy**, driving **WhatsApp enquiries**. **€10/day.** Run under 741 to prove it works before renegotiating with the client.

## ✅ Already done (do NOT redo)
- Ads account **"Bali Healing – Ozone"** created under the **741.Studio manager (476-158-5143)**; billing set up and went through.
- Advertiser **identity verification submitted** (client entity: **PT. Amana Events Indonesia**, doc uploaded = NIB business license). The "financial services" verification task was correctly **dismissed** — Bali Healing is wellness, not finance.
- **WhatsApp conversion tracking is LIVE & VERIFIED** on the website (Wix). A click on any WhatsApp button fires `contact_whatsapp` to GA4 (`G-773QRR6N6H`) and `WhatsAppInquiry` to Meta — confirmed on both the ozone page (wa.me) and the live-blood-analysis page (wa.link). Nothing more needed on the site.

## ⬜ Remaining — all inside Google Ads

### 1. Link GA4 + import the conversion (do this BEFORE publishing)
- Link GA4 property **`G-773QRR6N6H`** to the Ads account.
- Goals → Conversions → **+ New → Import → Google Analytics 4 → Web** → select **`contact_whatsapp`** → set as **Primary**.

### 2. Build the Search campaign
- Expert Mode, type **Search**, name **`Ozone – Search – Bali`**
- Bidding: **Maximize clicks, max CPC €0.60** (switch to Max Conversions once `contact_whatsapp` has data)
- Networks: **Search only** — uncheck Search Partners AND Display
- Location: **Bali, Indonesia** → **"Presence: people in or regularly in"** (NOT "presence or interest")
- Language: **English** · Budget: **€10/day**
- Ad group: **`Ozone Therapy`**
- **Keywords:**
```
"ozone therapy bali"
"ozone therapy canggu"
"ozone therapy ubud"
"eboo bali"
"blood ozone bali"
[ozone therapy bali]
[eboo therapy bali]
```
(❌ do NOT add "autohemotherapy" — mostly veterinary searches)
- **Negative keywords:**
```
jobs, career, salary, course, training, certification, school, learn,
machine, device, generator, buy, for sale, diy, kit, free,
dog, dogs, cat, horse, animal, veterinary, pet,
dentist, dental, oxygen chamber, hyperbaric chamber
```
- **Final URL:** `https://www.balihealing.com/ozone-hyperbaric-major-autohemotherapy`
- **Display path:** `/Ozone-Therapy` `/Canggu-Bali`
- **Headlines:**
```
Ozone Therapy in Canggu Bali
Feel Recharged & Refreshed
Ozone Wellness Treatments
German CE-Certified Devices
Doctor-Supervised Care
Wellness Center Since 2006
Book Easily via WhatsApp
Trusted by 300,000+ Guests
Ozone Therapy Bali
Relax, Recharge, Restore
```
- **Descriptions:**
```
Modern ozone wellness therapy in Canggu. Support your energy and wellbeing.
Performed by qualified doctors & nurses using German CE-certified equipment.
Trusted Bali wellness center since 2006. Book your session via WhatsApp.
Relax, recharge and feel your best — message us today.
```
- **Assets:** Sitelinks (About Ozone Therapy · Our Team · Live Blood Analysis · Chat on WhatsApp) + Callouts (German-Certified Equipment · Doctor-Supervised · Open Mon–Sat · Since 2006)

### 3. Publish — but only after step 1 is done.

## ⚠️ Non-negotiables
- **Conversion tracking set BEFORE publishing** — otherwise the campaign runs blind (no lead measurement = can't prove ROI, which is the whole point).
- **Wellness wording only** — no naming diseases or "treat/cure/prevent" (Google health-ad policy).
- Identity verification may still be **"under review" (1–10 days)** — ads won't serve until approved, so publishing now just queues them. That's fine.
