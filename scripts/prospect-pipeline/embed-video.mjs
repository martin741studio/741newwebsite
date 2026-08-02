#!/usr/bin/env node
/**
 * Loom-Video in eine Prospect-Page einbetten + deployen (+ optional Mail).
 *   node scripts/prospect-pipeline/embed-video.mjs <slug> <loom-share-oder-embed-url> [--send email@x.de] [--no-deploy]
 */
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { execSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
for (const line of readFileSync(path.join(ROOT, '.env'), 'utf8').split('\n')) {
  const m = line.match(/^([A-Z_]+)=(.*)$/); if (m && !process.env[m[1]]) process.env[m[1]] = m[2].trim();
}

const [slug, loomUrl] = process.argv.slice(2).filter((a) => !a.startsWith('--'));
const sendTo = process.argv.includes('--send') ? process.argv[process.argv.indexOf('--send') + 1] : null;
const deploy = !process.argv.includes('--no-deploy');
if (!slug || !loomUrl) { console.error('Usage: embed-video.mjs <slug> <loom-url> [--send email] [--no-deploy]'); process.exit(1); }

const idMatch = loomUrl.match(/(?:share|embed)\/([a-f0-9]{32})/);
if (!idMatch) { console.error('✗ Keine Loom-Video-ID in der URL gefunden.'); process.exit(1); }
const embed = `<iframe src="https://www.loom.com/embed/${idMatch[1]}" allowfullscreen></iframe>`;

const file = path.join(ROOT, '04_site/review', slug, 'index.html');
if (!existsSync(file)) { console.error(`✗ Seite nicht gefunden: ${file}`); process.exit(1); }
let html = readFileSync(file, 'utf8');

/* Platzhalter-Block (TODO-Kommentar + Overlay-Div) ODER bestehendes Loom-iframe ersetzen */
const placeholderRe = /<!-- TODO: Loom-Embed[\s\S]*?<\/div>(?=\s*<\/div>)/;
const iframeRe = /<iframe src="https:\/\/www\.loom\.com\/embed\/[a-f0-9]{32}" allowfullscreen><\/iframe>/;
if (placeholderRe.test(html)) html = html.replace(placeholderRe, embed);
else if (iframeRe.test(html)) html = html.replace(iframeRe, embed);
else { console.error('✗ Weder Platzhalter noch bestehendes Loom-iframe gefunden — Seite manuell prüfen.'); process.exit(1); }
writeFileSync(file, html);
console.log(`▸ Video eingebettet in 04_site/review/${slug}/index.html`);

if (deploy) {
  execSync('npm run build', { cwd: ROOT, stdio: 'ignore' });
  execSync('npm run deploy', { cwd: ROOT, stdio: 'inherit' });
}

const pageUrl = `https://741.studio/review/${slug}/`;
if (sendTo) {
  const key = process.env.RESEND_API_KEY;
  const firstname = (html.match(/Hallo ([A-Za-zÄÖÜäöü]+),/) || [, ''])[1];
  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST', headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: '741.Studio <hello@741.studio>', to: [sendTo],
      subject: `Dein persönliches Analyse-Video ist da${firstname ? `, ${firstname}` : ''}! 🎥`,
      html: `<div style="font-family:-apple-system,Segoe UI,Roboto,sans-serif;max-width:560px">
        <h2>Dein Video ist online${firstname ? `, ${firstname}` : ''}! 🎥</h2>
        <p>Dein persönliches Analyse-Video ist jetzt direkt auf deiner Auswertungs-Seite eingebettet – zusammen mit der Karte deines Einzugsgebiets und allen Empfehlungen.</p>
        <p style="margin:24px 0"><a href="${pageUrl}" style="background:#fac118;color:#111;padding:12px 22px;border-radius:10px;text-decoration:none;font-weight:700">Video & Analyse ansehen →</a></p>
        <p style="color:#666;font-size:13px">Fragen? Antworte einfach auf diese E-Mail.<br>Martin · 741.Studio</p></div>`,
    }),
  });
  console.log(r.ok ? `▸ Mail an ${sendTo} gesendet.` : `⚠ Mail-Fehler: ${await r.text()}`);
}
console.log(`✅ Fertig: ${pageUrl}`);
