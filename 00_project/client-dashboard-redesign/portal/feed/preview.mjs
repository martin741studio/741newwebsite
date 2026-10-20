#!/usr/bin/env node
/**
 * Builds a local preview page of the client view: the real src/dsh.css + src/dsh.js with the feed of one client and stub functions
 * for the other portal modules (decisions, setup, chat). Opens with a double click. Nothing is uploaded.
 *   node portal/feed/preview.mjs --client huewel       -> portal/feed/out/huewel/preview.html
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
const HERE = dirname(fileURLToPath(import.meta.url));
const ci = process.argv.indexOf('--client'); const slug = ci > 0 ? process.argv[ci + 1] : 'bali';
const feed = JSON.parse(readFileSync(join(HERE, 'out', slug, 'dashboard.json'), 'utf8'));
const css = readFileSync(join(HERE, '../src/dsh.css'), 'utf8'), js = readFileSync(join(HERE, '../src/dsh.js'), 'utf8');
const lang = feed.meta?.lang || 'en';
const html = `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Preview ${slug}</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Anton&display=swap" rel="stylesheet">
<style>:root{--yellow:#ffd23f;--black:#111;--ink:#111}body{margin:0;font-family:'DM Sans',system-ui,sans-serif;background:#faf6ea;color:#111}#app{max-width:1100px;margin:0 auto;padding:16px}
.pv-note{background:#111;color:#ffd23f;padding:6px 14px;font-size:13px}</style><style>${css}</style></head>
<body><div class="pv-note">Lokale Vorschau (${slug}). Entscheidungen, Einrichtung und Chat sind hier Platzhalter. Nichts ist hochgeladen.</div><div id="app"></div>
<script>
const esc=s=>String(s??'');const apGuide=(p,t)=>'<aside class="dz-mg" style="background:#fff;border:1px solid #e3dcc6;border-radius:12px;padding:10px 14px;margin:10px 0"><b>Martin ('+p+'):</b> '+t+'</aside>';
const apOn=()=>true;const apOpenCount=()=>0;const apRenderClient=()=>'<div class="dz-card">(Entscheidungen: Modul des Portals)</div>';
const renderOnboarding=()=>'<div class="dz-card">(Einrichtung: Modul des Portals)</div>';const renderGrants=()=>'<div class="dz-card">(Zugänge: Modul des Portals)</div>';const renderChat=()=>'<div>(Chat)</div>';
const applyShellLang=()=>{};const $=()=>({});const bundleIsAdmin=false;let adminSub=null;const closeReport=()=>{};const openReport=u=>window.open(u,'_blank');
const fetch=()=>Promise.reject(new Error('preview'));
function rerender(){document.getElementById('app').innerHTML=dshPage(B);}
const B={client:{id:'x',name:${JSON.stringify(feed.meta?.client || slug)},lang:${JSON.stringify(lang)}},apReady:false,apItems:[],steps:[],grants:[],program:{start_date:${JSON.stringify(feed.meta?.as_of || '2026-01-01')}}};
${js}
DSH.d=${JSON.stringify(feed)};DSH.loaded='x';DSH.init=true;
window.dshLoad=function(){};   // the feed is embedded
rerender();
</script></body></html>`;
const out = join(HERE, 'out', slug, 'preview.html'); writeFileSync(out, html); console.log('wrote', out);
