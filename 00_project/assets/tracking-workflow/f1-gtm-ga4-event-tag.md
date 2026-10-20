# F1 · GA4 event tag in GTM for Suriya's lead events (prepared, NOT applied)

Status: prepared 2026-10-12 after Martin chose F1. Going live needs Martin's separate go (class G, automation-build rules).
Client: Praxis Suriya · site suriya-praxis.de · GTM container `GTM-K9MDDN7P` · GA4 `G-B93S7ZWNNR` (hard-coded gtag in the page head).

## Facts (read-only check, 2026-10-12)

- The site pushes 3 dataLayer events (inline script on every page):
  - `s741_form_submit` with `form_plugin` (cf7 / fluentforms) and `form_id`
  - `s741_whatsapp_click` with `link_url`
  - `s741_phone_click` with `link_url`
- GTM has 2 Google Ads conversion tags (`AW-18502523090`, labels `CAzzCL7XyZYdENKx2PZE`, `jCjuCLvXyZYdENKx2PZE`) on custom-event triggers `s741_form_submit` and `s741_whatsapp_click`. It has no GA4 tag and no trigger for `s741_phone_click`.
- GA4 receives page views from the hard-coded gtag only. It records none of the lead events.
- Consent: the site pushes `s741_consent_granted` and updates Consent Mode. A GA4 event tag in GTM follows the same consent state.

## Change (one tag, one trigger, no site code)

1. Trigger "741 · Lead-Events": type Custom Event, event name `s741_form_submit|s741_whatsapp_click|s741_phone_click`, regex match on.
2. Tag "741 · GA4 · Lead-Event": type Google Analytics: GA4 Event.
   - Measurement ID: `G-B93S7ZWNNR`
   - Event name: `{{Event}}` (keeps the three names)
   - Parameters: `form_plugin`, `form_id` and `link_url` (Data Layer Variables)
   - Fires on the trigger "741 · Lead-Events"
3. GA4 admin: mark `s741_form_submit` as a key event. Optionally also mark `s741_whatsapp_click` and `s741_phone_click`.

## Test gate (before publish)

- GTM Preview on `/termin-buchen/`: click the WhatsApp link and the phone link. The tag fires once per click.
- Form submit: Preview only, with the test text `TEST-741` in the message field. Coralie gets the email, so warn her first, or skip the real submit and check the trigger with a dataLayer push in Preview.
- GA4 DebugView shows the three events with parameters.
- Publish only after Martin's go. Write the GTM version number and the rollback version into the run folder.

## Rollback

Delete the tag and the trigger, or publish the previous GTM version. The site and the Ads tags are not touched.

## Also needed (F2, not chosen yet)

The service account `reporting-bot@studio-apis-503306.iam.gserviceaccount.com` needs viewer access to the GA4 property. Without it, the tab cannot read the counts automatically.
