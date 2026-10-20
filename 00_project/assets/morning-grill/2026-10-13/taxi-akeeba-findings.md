# Taxi Nürnberg: Akeeba download key + spam (read only, 13.10.2026)

Request: Daniel Leibold (partner agency) via Martin. Screenshot: Joomla Update Sites show "The Download Key is missing" for "Admin Tools Professional package" (latest 7.9.3) and "Akeeba Backup Professional for Joomla!" (latest 10.4.0). Daniel: the key was entered in July 26 as "yearly" (75,-). He also asks if Akeeba is the spam protection (900 spam mails in the Zentrale overnight).

## Verified
1. Joomla admin (taxi-nuernberg.de/administrator) is NOT logged in in my Chrome window. I did not enter credentials.
2. Earlier dump of 03.08.2026 (taxi chat scratch, `joomla_status.json`): Admin Tools 7.8.9, Akeeba Backup 10.3.6 installed; both update sites point to the Pro package XML files. Latest versions on Daniel's screenshot are 7.9.3 and 10.4.0, so updates are pending.
3. Daniel's hours sheet (Drive): July 26 "Taxi updates 2 h", "Taxi Malware 15.07: DDOS attack and menu fix, password reset through database 3.5 h". The "Akeeba Plugin 75,- Yearly" line is in his spreadsheet picture, not in the Drive file I could read.
4. Public forms (checked in Chrome, no login):
   • /kontakt/formulare: 3 SP Page Builder forms (Fundsachen, Bestellung Fahraufträge, a third) with captcha_type "default" and NO captcha widget; 1 RSForm complaint form WITH reCAPTCHA.
   • /kontakt: form 1 has a simple question field (captcha_question); form 2 (first name, last name, email, subject, message) has no captcha.
   • /ihretaxizentrale/taxi-aussenwerbung-buchen: SP Page Builder ajax form, honeypot field only.
   • On 03.08. the Joomla invisible reCAPTCHA plugin was disabled; only the RSForm reCAPTCHA plugin was enabled. "default" in SP Page Builder therefore most likely means no captcha (current setting not verified).

## Not verified (needs a login)
• Akeeba subscription status and Download ID (akeeba.com account).
• Whether the key was ever saved in Joomla, and why it is missing now.
• Which form sent the 900 mails (needs 2 to 3 sample mails with full headers).
• Current Admin Tools and Akeeba versions installed.

## What this means
• A missing download key does not switch off the installed plugins. It blocks updates (security rule updates included). Confirm in the Joomla admin.
• Akeeba is not a form spam filter. Admin Tools Pro is the firewall, Akeeba Backup only makes backups.
• The likely spam source is a form without captcha. Not proven.

## Next steps (all need Martin's own login or go)
1. akeeba.com account: check the subscription is active (bought July 26, yearly) and copy the Download ID.
2. Joomla admin > System > Update Sites: open both Pro entries, paste the key, save. Use Martin's real Chrome (Cloudflare blocks automated admin saves). A download key is a licence key: Martin enters it, not the agent.
3. Backup first (Akeeba Backup), then update Admin Tools and Akeeba Backup.
4. Spam: get sample mails, then add a captcha to the forms without one (Joomla reCAPTCHA or Cloudflare Turnstile) and a rate limit in Cloudflare. Each live change needs Martin's go.

## Verified later on 13.10.2026 (read-only, Martin's own akeeba.com session on screen)
• akeeba.com > My product subscriptions: "Admin Tools for Joomla!" = Active, valid until 15 July 2027. "Akeeba Backup for Joomla!" = Active, valid until 15 July 2027.
• So the licences did not expire. Only Joomla has no Download Key. Daniel needs nothing from us on the licence.
• Joomla dashboard already showed "2 Download Keys are missing" on 01.09.2026. The key was missing for at least six weeks.
• Guess, not proven: the 15.07 malware cleanup (password reset through the database) wiped the key.
• Martin does the key step himself (licence key rule). Path: Joomla > System > Update Sites > both Pro entries > field "Download Key" > Save. The main Download ID is on akeeba.com > Add-on Download IDs.

## DONE 13.10.2026 (evening, in chat)
• Backup #53 (full site, 772.75 MB) made. Daniel's own backup from 12.10. (#52) also exists.
• Installed by upload: Akeeba Backup Pro 10.4.0 and Admin Tools Pro 7.9.3. Both "Installation of the package was successful".
• Martin pasted the main Download ID into both Update Sites (IDs 452 and 453). Joomla: "Item saved". Update Sites list: 0 "Download Key is missing".
• Update list now shows no Admin Tools or Akeeba update. Still pending (not touched, needs go): GDPR 2.25 to 2.27, RSForm! Pro.
• Tests after install: /, /preisrechner/, tarif js files, /taxi-rechner/ (302 to /preisrechner/), Preise, Kontakt, Datenschutz, /administrator/ all OK. Root .htaccess unchanged (33,848 bytes, 01.09.).
• Open: spam source (needs 2 to 3 sample mails with headers), captcha on forms without one (needs go).

## GDPR cookie banner (14.10.2026)
• Provider: Joomla! Extensions Store (storejextensions.org), product "GDPR". RSForm! Pro is another publisher (rsjoomla.com).
• Licence is paid: order 05.05.2026, 49.99 EUR, order email martin@741.studio. Store account shows "updates valid until 06 May 2027".
• Why Joomla said "expired 2025-07-10": the plugin asks the store with the registration email in GDPR settings. That field held info@werbeagentur-bamberger.de (old licence). The new licence belongs to martin@741.studio.
• Update done by package upload (vendor package gdpr_v2.27_forjoomla6.x_5.x_4.x.zip, downloaded from Martin's logged-in store account): component 2.27 and plugin 2.27 installed and active. No new backup (Martin: Daniel's backup of 12.10. is enough, and #53 of 13.10.).
• Tests: site, calculator, redirect, forms, admin OK. Banner shows (German, Google Consent Mode v2).
• NOT done (classifier blocked the settings change, not forced): (1) registration email to martin@741.studio so Joomla's own updater finds the licence next time; (2) "Use popup for links" = No (fixes the jQuery(...)[b] console error). Both need a save of the GDPR settings; Cloudflare also blocked that save on 01.09.
• Still open: RSForm! Pro licence status (rsjoomla.com), spam source, captcha.

## 14.10.2026 later: GDPR email + RSForm
• Martin: "und email ändern". Done: GDPR > Configuration > General settings > "Registration email address for updater" changed from info@werbeagentur-bamberger.de to martin@741.studio. "Parameters saved successfully" (Cloudflare did not block this time). Old value kept here for rollback: info@werbeagentur-bamberger.de.
• Gotcha: the GDPR config page opens on the last used tab ("Cookie consent"). The email field is on "General settings". A click on the hidden field hit the Joomla menu and jumped to the dashboard. Open the tab first.
• RSForm! Pro: Daniel bought a new licence on 13.10. (old one had expired). Component is 3.4.10 (the version offered on 13.10.). Fresh "Check For Updates": no pending updates for any extension.
• Not done, not asked: "Use popup for links" = No (console error), Joomla core 5.4.9 to 5.4.10 (dashboard shows it as available).
