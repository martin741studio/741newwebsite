#!/usr/bin/env node
/**
 * Competitor backlink gap analysis — Process B of 00_project/backlink-workflow-dach.md.
 * Replaces the ad-hoc Node one-liners written by hand on every Hüwel run (v1–v4);
 * this is the single reusable script, run not rewritten (rules.md C5 / workflow-creation
 * scorecard C5).
 *
 * Usage:
 *   node gap-analysis.mjs --client praxis-huewel.de \
 *     --competitor naturheilpraxis-brahmer.de --competitor go-neuro.de \
 *     --competitor naturheilkunde-praxis-trojahn.de --competitor heilpraktiker-steiner-nuernberg.de \
 *     --competitor carolin-heilmann.de --competitor heilzentrum-helios.de \
 *     --competitor heilpraktiker-franken.de --competitor heilpraktiker-carmen-bauer.de \
 *     --out /path/to/01-baseline/
 *
 * Needs .secrets/dataforseo.env (DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD) in the repo root
 * this is run from, or pass --secrets <path>.
 *
 * Minimum 8 competitors is enforced (rules.md RH — 5 competitors gave 10 gap domains on
 * the Hüwel pilot, 8 gave 23; below 8 the API cost rarely pays for the hit rate).
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

const args = process.argv.slice(2);
const get = (flag) => { const i = args.indexOf(flag); return i === -1 ? null : args[i + 1]; };
const getAll = (flag) => args.reduce((acc, a, i) => (a === flag ? [...acc, args[i + 1]] : acc), []);

const client = get('--client');
const competitors = getAll('--competitor');
const outDir = get('--out') || '.';
const secretsPath = get('--secrets') || '.secrets/dataforseo.env';
const limit = Number(get('--limit') || 300);

if (!client) { console.error('Usage: --client <domain> --competitor <domain> (x8+) [--out <dir>] [--secrets <path>]'); process.exit(1); }
if (competitors.length < 8) {
  console.error(`Only ${competitors.length} competitors given. rules.md RH requires 8+ — a smaller pool gave too few real gap hits on the Hüwel pilot. Pass more with --competitor, or override with --force.`);
  if (!args.includes('--force')) process.exit(1);
}

const env = Object.fromEntries(
  readFileSync(secretsPath, 'utf8').split('\n').filter(Boolean)
    .filter(l => !l.trimStart().startsWith('#'))
    .map(l => { const i = l.indexOf('='); return [l.slice(0, i).trim(), l.slice(i + 1).trim()]; }));
const auth = 'Basic ' + Buffer.from(`${env.DATAFORSEO_LOGIN}:${env.DATAFORSEO_PASSWORD}`).toString('base64');

async function summary(target) {
  const r = await fetch('https://api.dataforseo.com/v3/backlinks/summary/live', {
    method: 'POST', headers: { Authorization: auth, 'Content-Type': 'application/json' },
    body: JSON.stringify([{ target }]) });
  const j = await r.json(); const t = j.tasks?.[0]; const s = t?.result?.[0];
  return { ok: t?.status_code === 20000, rank: s?.rank ?? null, backlinks: s?.backlinks ?? null, referring_domains: s?.referring_domains ?? null, err: t?.status_message };
}

async function referringDomains(target) {
  const r = await fetch('https://api.dataforseo.com/v3/backlinks/referring_domains/live', {
    method: 'POST', headers: { Authorization: auth, 'Content-Type': 'application/json' },
    body: JSON.stringify([{ target, limit, order_by: ['rank,desc'] }]) });
  const j = await r.json(); const t = j.tasks?.[0];
  if (t?.status_code !== 20000) return { ok: false, items: [], err: t?.status_message };
  return { ok: true, items: (t.result?.[0]?.items || []).map(i => ({ domain: i.domain, rank: i.rank || 0 })) };
}

// rank 0–1000ish DataForSEO scale → approx familiar 0–100 DR, for display only (not an official DR figure)
const toDR = (rank) => rank == null ? null : Math.round(Math.min(rank / 10, 100));

// Drop a domain if its own authority is near-0 despite high volume on itself — the
// spam/link-farm signature confirmed repeatedly on the Hüwel pilot (rules.md RG.3).
const SPAM_RANK_CEILING = 20;

(async () => {
  console.log(`Client: ${client} · Competitors: ${competitors.length} · limit ${limit}/competitor\n`);

  const clientSummary = await summary(client);
  const clientDomains = await referringDomains(client);
  const known = new Set(clientDomains.items.map(d => d.domain.toLowerCase()));

  const profileRows = [{ domain: client, role: 'eigen', ...clientSummary, DR: toDR(clientSummary.rank) }];
  const count = {}, who = {}, rankMap = {};

  for (const c of competitors) {
    const s = await summary(c);
    profileRows.push({ domain: c, role: 'wettbewerber', ...s, DR: toDR(s.rank) });
    if (!s.ok) { console.error(`  SKIP ${c}: ${s.err}`); continue; }
    const rd = await referringDomains(c);
    if (!rd.ok) { console.error(`  SKIP referring_domains ${c}: ${rd.err}`); continue; }
    for (const d of rd.items) {
      const dom = d.domain.toLowerCase();
      count[dom] = (count[dom] || 0) + 1;
      (who[dom] ||= []).push(c);
      rankMap[dom] = Math.max(rankMap[dom] || 0, d.rank || 0);
    }
    await new Promise(r => setTimeout(r, 200));
  }

  const gap = Object.keys(count)
    .filter(d => count[d] >= 2 && !known.has(d))
    .map(d => ({
      domain: d, competitors: count[d], who: who[d], rank: rankMap[d], DR: toDR(rankMap[d]),
      spamFlag: rankMap[d] < SPAM_RANK_CEILING,
    }))
    .sort((a, b) => b.competitors - a.competitors || b.rank - a.rank);

  mkdirSync(outDir, { recursive: true });
  const profilePath = resolve(outDir, 'profile.md');
  const gapPath = resolve(outDir, 'gap.md');

  const profileMd = [
    '# Baseline — Linkprofile (DataForSEO, generated by gap-analysis.mjs)', '',
    '| Domain | Rolle | Rank | DR (approx.) | Backlinks | Referring Domains |',
    '| --- | --- | --- | --- | --- | --- |',
    ...profileRows.map(r => `| ${r.domain} | ${r.role} | ${r.rank ?? '–'} | ${r.DR ?? '–'} | ${r.backlinks ?? '–'} | ${r.referring_domains ?? '–'} |`),
  ].join('\n') + '\n';
  writeFileSync(profilePath, profileMd);

  const spamCount = gap.filter(g => g.spamFlag).length;
  const gapMd = [
    `# Link-Gap — ${competitors.length} Wettbewerber, ${limit} Referring Domains je Wettbewerber`, '',
    `${gap.length} Gap-Domains gefunden, davon ${spamCount} mit Spam-Flag (Rank < ${SPAM_RANK_CEILING} trotz Volumen — rules.md RG.3, von Hand prüfen vor Übernahme ins Sheet).`, '',
    '| Domain | Wettbewerber (Anzahl) | Welche | Rank | DR (approx.) | Spam-Verdacht |',
    '| --- | --- | --- | --- | --- | --- |',
    ...gap.map(g => `| ${g.domain} | ${g.competitors} | ${g.who.join(', ')} | ${g.rank} | ${g.DR} | ${g.spamFlag ? '⚠️ ja' : ''} |`),
  ].join('\n') + '\n';
  writeFileSync(gapPath, gapMd);

  console.log(`\nWrote ${profilePath}`);
  console.log(`Wrote ${gapPath}`);
  console.log(`${gap.length} gap domains (${spamCount} flagged as likely spam — review before scoring, don't auto-drop silently).`);
})();
