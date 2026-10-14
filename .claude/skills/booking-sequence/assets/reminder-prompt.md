Reminder for Martin Drendel (741 Studio). Do NOT send any message yourself. Never use WhatsApp, email, LinkedIn or any messaging tool to contact {{NAME}}.

1. Run `date -u +%Y-%m-%dT%H:%M`. The call with {{NAME}} starts at {{CALL_UTC}} (UTC) = {{CALL_LINE}}.
2. If now is after the call start: send Martin a push notification (PushNotification tool, if available) with the title "Zu spät: Nachricht {{N}} an {{NAME}} nicht mehr senden" and reply only that line plus "The laptop was probably asleep at the send time." Stop here.
3. Read /Users/martindrendel/741website/00_project/prospects/{{SLUG}}/whatsapp-sequence.md and take the text of the section whose heading starts with "{{SECTION}}": the ```text block and the line that starts with "WhatsApp-Link:". If the file or the section is missing or the section says "entfällt", reply "Message {{N}} for {{NAME}} is not available (file or section missing). Nothing to send." and stop. Never write a message yourself.
4. {{LATE_RULE}}
5. {{RECHECK}}
6. Send Martin a push notification (PushNotification tool, if available) with the title "{{PUSH_TITLE}}" and the body "{{PUSH_BODY}}".
7. In your reply show the message exactly as one ```text block, then the WhatsApp-Link line (it opens WhatsApp with the text ready; Martin presses send), the WhatsApp number {{PHONE}} and the line "Call: {{CALL_LINE}}".

Reply in ASD-STE100 Simplified Technical English, except the German message itself.
