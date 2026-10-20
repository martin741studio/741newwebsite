/* ---- Generic view for any client feed (German or English). Used when the feed has no Bali profile blocks (nhc). Bali keeps its own pages above. ---- */
const DSHL = {
  de: {
    tabs: { overview: 'Übersicht', results: 'Ergebnisse', plan: 'Plan', decisions: 'Entscheidungen', reports: 'Berichte', setup: 'Einrichtung' },
    sub: { enquiries: 'Anfragen', found: 'Bei Google gefunden', reviews: 'Bewertungen' },
    q1: 'Bekomme ich mehr Anfragen?', q2: 'Werde ich besser gefunden?', q3: 'Was hat sich seit dem Start verändert?', q3w: 'Was macht 741?',
    week: (n, m) => `Woche ${n} von ${m}`, lastUpdate: 'Letztes Update von 741:',
    needsTitle: n => `Braucht dich (${n})`, needsSub: '741 wartet auf diese Punkte. Auf deiner Live-Seite ändert sich nichts ohne dein Ja.',
    needsChip: 'Braucht dich', decide: 'Entscheiden', draft: 'Entwurf: dem Kunden noch nicht freigegeben', openSetup: 'Einrichtung öffnen',
    setupOpen: n => `Einrichtung: ${n} Schritt${n === 1 ? '' : 'e'} noch offen.`,
    seeEnq: 'Anfragen ansehen', seeFound: 'Ergebnisse ansehen', seeResults: 'Vorher und nachher ansehen',
    notMeasured: 'Noch nicht gemessen', checked: 'Von 741 geprüft',
    chat: 'Chat mit 741', closeChat: 'Chat schließen',
    ev: { phone_click: 'Klicks auf die Telefonnummer', email_click: 'Klicks auf die E-Mail-Adresse', whatsapp_click: 'Klicks auf WhatsApp', generate_lead: 'Formular-Anfragen' },
    evNote: { phone_click: 'Gezählt wird der Klick, nicht der Anruf.', email_click: 'Gezählt wird der Klick, nicht die Nachricht.', whatsapp_click: 'Gezählt wird der Klick, nicht das Gespräch.', generate_lead: 'Gesendete Anfragen über das Formular.' },
    enqLead: n => `<b>${n} Anfragen seit dem Start der Messung.</b> Davor wurde nicht gemessen, das ist kein Nullwert.`,
    enqNone: 'Die Messung der Anfragen läuft. Es gibt noch keinen Wert.',
    foundLead: (c, d, mo, prev) => `<b>${c} Klicks aus der Google-Suche im ${mo}</b>, ${d === 0 ? 'so viele wie' : d > 0 ? d + ' mehr als' : Math.abs(d) + ' weniger als'} im ${prev}.`,
    posText: (p, pj, mj) => `Durchschnittsposition ${p} (${p <= 10 ? 'Seite 1' : p <= 20 ? 'Seite 2' : 'weiter hinten'}), im ${mj} waren es ${pj}.`,
    clicksMonth: 'Klicks aus der Google-Suche pro Monat', fullMonthNote: 'Nur volle Monate. Google trägt die letzten Tage verspätet nach.',
    beforeAfter: 'Vorher und nachher', before: 'Vorher', after: 'Nachher', latest: 'Zuletzt', better: 'besser', worse: 'schlechter', same: 'gleich',
    queries: 'Dein wichtigster Suchbegriff', listings: 'Verzeichniseinträge online', of: 'von',
    reviewsTitle: 'Google-Bewertungen', reviewsLead: (n, s) => `<b>${n} Bewertungen, ${s} Sterne.</b>`,
    reports: 'Berichte', reportsLead: 'Jeder Bericht mit Datum. Ältere Fassungen verweisen auf die aktuelle Seite.', repReport: 'Bericht', repPeriod: 'Zeitraum', repState: 'Stand', open: 'Öffnen',
    current: 'Aktuell', replaced: 'Ersetzt', foot: 'Sätze werden aus den Zahlen vorbereitet und von 741 geprüft.', loading: 'Dein Dashboard lädt …',
    resultsTitle: 'Ergebnisse', setupTitle: 'Einrichtung', decisionsTitle: 'Deine Entscheidungen', back: '← Zur Kundenseite',
    status: { red: 'Blockiert', amber: 'Braucht dich', green: 'Im Plan', grey: 'Noch keine Daten' },
    locale: 'de-DE'
  },
  en: {
    tabs: { overview: 'Overview', results: 'Results', plan: 'Plan', decisions: 'Decisions', reports: 'Reports', setup: 'Setup' },
    sub: { enquiries: 'Enquiries', found: 'Found on Google', reviews: 'Reviews' },
    q1: 'Do I get more enquiries?', q2: 'Am I easier to find?', q3: 'What changed since the start?', q3w: 'What is 741 doing?',
    week: (n, m) => `Week ${n} of ${m}`, lastUpdate: 'Last update from 741:',
    needsTitle: n => `Needs you (${n})`, needsSub: '741 waits for these. Nothing changes on your live site without your OK.',
    needsChip: 'Needs you', decide: 'Decide', draft: 'Draft: not released to the client', openSetup: 'Open setup',
    setupOpen: n => `Setup: ${n} step${n === 1 ? '' : 's'} still open.`,
    seeEnq: 'See enquiries', seeFound: 'See results', seeResults: 'See before and after',
    notMeasured: 'Not measured yet', checked: 'Checked by 741',
    chat: 'Chat with 741', closeChat: 'Close chat',
    ev: { phone_click: 'Taps on the phone number', email_click: 'Taps on the email address', whatsapp_click: 'Taps on WhatsApp', generate_lead: 'Form enquiries' },
    evNote: { phone_click: 'We count the tap, not the call.', email_click: 'We count the tap, not the message.', whatsapp_click: 'We count the tap, not the chat.', generate_lead: 'Enquiries sent through the form.' },
    enqLead: n => `<b>${n} enquiries since the measurement started.</b> Before that nothing was measured. That is not zero.`,
    enqNone: 'Measuring enquiries has started. There is no value yet.',
    foundLead: (c, d, mo, prev) => `<b>${c} clicks from Google Search in ${mo}</b>, ${d === 0 ? 'the same as' : d > 0 ? d + ' more than' : Math.abs(d) + ' fewer than'} in ${prev}.`,
    posText: (p, pj, mj) => `Average position ${p} (${p <= 10 ? 'page 1' : p <= 20 ? 'page 2' : 'further back'}), in ${mj} it was ${pj}.`,
    clicksMonth: 'Clicks from Google Search per month', fullMonthNote: 'Full months only. Google adds the latest days late.',
    beforeAfter: 'Before and after', before: 'Before', after: 'After', latest: 'Latest', better: 'better', worse: 'worse', same: 'same',
    queries: 'Your most important search term', listings: 'Directory listings online', of: 'of',
    reviewsTitle: 'Google reviews', reviewsLead: (n, s) => `<b>${n} reviews, ${s} stars.</b>`,
    reports: 'Reports', reportsLead: 'Every report with its date. Older versions point to the current page.', repReport: 'Report', repPeriod: 'Period', repState: 'State', open: 'Open',
    current: 'Current', replaced: 'Replaced', foot: 'Sentences are drafted from the numbers and checked by 741.', loading: 'Loading your dashboard…',
    resultsTitle: 'Results', setupTitle: 'Setup', decisionsTitle: 'Your decisions', back: '← Back to the client page',
    status: { red: 'Blocked', amber: 'Needs you', green: 'On track', grey: 'No data yet' },
    locale: 'en-US'
  }
};
const dshLang = () => (DD && DD.meta && DD.meta.lang === 'de') ? 'de' : 'en';
const dshT = () => DSHL[dshLang()];
const dshGen = () => !(DD && DD.nhc);
function dshN(n, frac) { return n == null ? '—' : new Intl.NumberFormat(dshT().locale, frac ? { minimumFractionDigits: frac, maximumFractionDigits: frac } : {}).format(n); }
function dshGSt(c, w) { return `<span class="dz-st dz-${c}">${DSHS[c][2]}${w || dshT().status[c]}</span>`; }
function dshGHasResults() { return !!(DD.ga4_events || DD.gsc || DD.ergebnisse || DD.citations); }
function dshGHasPlan() { return !!((DD.tracks && DD.tracks.length) || (DD.tree && DD.tree.length)); }
function dshGMonthNames() { const g = DD.meta && DD.meta.derived && DD.meta.derived.gsc; return (g && g.months) || ['', '', '']; }
function dshGTabs(b, cur) {
  const T = dshT(), nDec = dshDecOpen(b).length, nSet = dshOpenSteps(b), items = [['overview', T.tabs.overview]];
  if (dshGHasResults()) items.push(['results', T.tabs.results]);
  if (dshGHasPlan()) items.push(['plan', T.tabs.plan]);
  if (dshDecItems(b).length) items.push(['decisions', T.tabs.decisions, nDec]);
  if (DD.reports && DD.reports.length) items.push(['reports', T.tabs.reports]);
  if (nSet) items.push(['setup', T.tabs.setup, nSet]);
  return `<nav class="dz-tabs">${items.map(t => `<a class="dz-tab ${cur === t[0] ? 'dz-on' : ''}" href="#" onclick="dshGo('${t[0]}');return false">${t[1]}${t[2] ? `<span class="dz-n">${t[2]}</span>` : ''}</a>`).join('')}</nav>`;
}
function dshGSub(cur) {
  const T = dshT(), items = [];
  if (DD.ga4_events) items.push(['enquiries', T.sub.enquiries]);
  if (DD.gsc || DD.ergebnisse || DD.citations) items.push(['found', T.sub.found]);
  if ((DD.rev && DD.rev.nhc) || (DD.ergebnisse && DD.ergebnisse.reviews)) items.push(['reviews', T.sub.reviews]);
  return `<div class="dz-sub">${items.map(t => `<a class="dz-pill ${cur === t[0] ? 'dz-on' : ''}" href="#" onclick="dshGo('results/${t[0]}');return false">${t[1]}</a>`).join('')}</div>`;
}
function dshGEvTotal() {
  if (!DD.ga4_events) return null;
  const i = DD.meta.partial != null ? DD.meta.partial : DD.months.length - 1; let n = 0, any = false;
  Object.keys(DD.ga4_events).forEach(k => { const v = DD.ga4_events[k][i]; if (v != null) { any = true; n += v; } });
  return any ? n : null;
}
function dshGDelta(m) {   // neutral wording, no status colours in numbers
  const T = dshT(); if (m.before == null || m.after == null) return '';
  const d = m.after - m.before; if (d === 0) return T.same;
  const good = (m.better === 'lower') ? d < 0 : d > 0;
  return `${good ? '▲' : '▼'} ${good ? T.better : T.worse}`;
}
function dshGOverview(b) {
  const T = dshT(), nDec = dshDecOpen(b).length, nSet = dshOpenSteps(b), bn = DD.banner;
  const needs = dshDecOpen(b).map(i => `<li>${dshGSt('amber', T.needsChip)}<span class="dz-tx"><b>${esc(i.title)}</b>${i.status === 'draft' ? ` <span class="dz-badge">${T.draft}</span>` : ''}</span><a class="dz-btn" href="#" onclick="dshGo('decisions');return false">${T.decide}</a></li>`);
  (DD.needs || []).filter(n => n.go !== 'decisions').forEach(n => needs.push(`<li>${dshGSt('amber', T.needsChip)}<span class="dz-tx">${n.t}</span><a class="dz-btn dz-o" href="#" onclick="dshGo('${n.go}');return false">${n.btn}</a></li>`));
  if (nSet) needs.push(`<li>${dshGSt('amber', T.needsChip)}<span class="dz-tx"><b>${T.setupOpen(nSet)}</b></span><a class="dz-btn dz-o" href="#" onclick="dshGo('setup');return false">${T.openSetup}</a></li>`);
  const cards = [];
  if (DD.ga4_events) {
    const n = dshGEvTotal(); const src = DD.meta.sources && DD.meta.sources.whatsapp;
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q1}</div><div class="dz-big">${n == null ? '—' : dshN(n)}</div><p class="dz-sentence">${n == null ? T.enqNone : T.enqLead(dshN(n))}</p>${src && src.note ? `<p class="dz-mut">${esc(src.note)}</p>` : ''}<div class="dz-chk">${T.checked} · ${esc(DD.meta.as_of)}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/enquiries');return false">${T.seeEnq}</a></div>`);
  }
  if (DD.gsc) {
    const m = dshGMonthNames(), g = DD.gsc, pos = g.pos, c = g.sep;
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q2}</div><div class="dz-big">${dshN(c)}</div><p class="dz-sentence">${T.foundLead(dshN(c), c - g.aug, m[2] || '', m[1] || '')}</p><p class="dz-mut">${T.posText(dshN(pos, 1), dshN(g.posJul, 1), m[0] || '')}</p>${DD.citations ? `<p class="dz-mut">${T.listings}: <b>${DD.citations.live} ${T.of} ${DD.citations.total}</b></p>` : ''}<div class="dz-chk">${T.checked} · ${esc(DD.meta.as_of)}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/found');return false">${T.seeFound}</a></div>`);
  }
  if (DD.ergebnisse && DD.ergebnisse.metrics) {
    const mm = DD.ergebnisse.metrics.filter(x => x.key === 'clicks' || x.key === 'position');
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q3}</div>${mm.map(x => `<p class="dz-sentence"><b>${esc(x.label)}</b><br>${dshN(x.before, x.key === 'position' ? 1 : 0)} → <b>${dshN(x.after, x.key === 'position' ? 1 : 0)}</b> <span class="dz-dl">${dshGDelta(x)}</span></p>`).join('')}<p class="dz-mut dz-s">${esc(DD.ergebnisse.windows.before.label)} → ${esc(DD.ergebnisse.windows.after.label)}</p><div class="dz-chk">${T.checked} · ${esc(DD.ergebnisse.read)}</div><a class="dz-btn dz-o dz-gap" href="#" onclick="dshGo('results/found');return false">${T.seeResults}</a></div>`);
  } else if (DD.work && (DD.work.this_week || DD.work.done)) {
    cards.push(`<div class="dz-card"><div class="dz-q">${T.q3w}</div>${DD.work.this_week ? `<p class="dz-sentence">${DD.work.this_week}</p>` : ''}${DD.work.done ? `<p class="dz-mut">${DD.work.done}</p>` : ''}<div class="dz-chk">${T.checked} · ${esc(DD.meta.as_of)}</div></div>`);
  }
  const guide = DD.guide && DD.guide.overview ? dshMg(DD.guide.overview.pose, DD.guide.overview.text) : '';
  return `${dshGTabs(b, 'overview')}
 <div class="dz-strip"><b>${esc(DD.meta.client)}</b>${DD.meta.week ? `<span class="dz-mut">${T.week(DD.meta.week, DD.meta.weeks)}</span>${dshSeg()}` : ''}${DD.meta.last_update ? `<span class="dz-mut">${T.lastUpdate} ${esc(DD.meta.last_update)}</span>` : ''}</div>
 ${bn ? `<div class="dz-banner dz-${bn.color}">${dshGSt(bn.color, bn.label)}<span>${bn.html}</span></div>` : ''}${guide}
 <div class="${cards.length === 2 ? 'dz-grid2' : 'dz-grid3'}">${cards.join('')}</div>
 ${needs.length ? `<div class="dz-need dz-gap2"><h2>${T.needsTitle(needs.length)}</h2><span class="dz-mut">${T.needsSub}</span><ul>${needs.join('')}</ul></div>` : ''}
 <p class="dz-foot">${esc(DD.source_note || '')} ${T.foot}</p>`;
}
function dshGEnquiries() {
  const T = dshT(), ev = DD.ga4_events || {}, order = ['phone_click', 'email_click', 'whatsapp_click', 'generate_lead'].filter(k => ev[k]);
  const n = dshGEvTotal();
  const tiles = order.map((k, i) => {
    const v = ev[k], p = DD.meta.partial, last = p != null ? v[p] : v[v.length - 1];
    return `<div class="dz-card dz-tile"><div class="dz-q">${T.ev[k]}</div><div class="dz-num">${last == null ? '—' : dshN(last)}</div><div class="dz-d">${T.evNote[k]}</div>${dshBars(v, DD.months, { partial: p, full: DD.meta.full, id: 'g' + i, aria: T.ev[k] })}</div>`;
  });
  const src = DD.meta.sources && DD.meta.sources.whatsapp;
  return `${dshGTabs(DSH.b, 'results')}${dshGSub('enquiries')}<h1 class="dz-t">${T.q1}</h1>
 <p class="dz-lead">${n == null ? T.enqNone : T.enqLead(dshN(n))}</p>
 <div class="dz-grid2">${tiles.join('')}</div>
 <p class="dz-foot">${src && src.note ? esc(src.note) + ' ' : ''}${T.notMeasured}: ${dshLang() === 'de' ? 'gestrichelte Felder. Schraffierter Balken: laufender Monat.' : 'dashed slots. Hatched bar: month in progress.'}</p>`;
}
function dshGFound() {
  const T = dshT(), g = DD.gsc, m = dshGMonthNames(), E = DD.ergebnisse;
  let html = `${dshGTabs(DSH.b, 'results')}${dshGSub('found')}<h1 class="dz-t">${T.q2}</h1>`;
  if (g) {
    html += `<p class="dz-lead">${T.foundLead(dshN(g.sep), g.sep - g.aug, m[2] || '', m[1] || '')} ${T.posText(dshN(g.pos, 1), dshN(g.posJul, 1), m[0] || '')}</p>
 <div class="dz-card"><div class="dz-q">${T.clicksMonth}</div>${dshBars([g.jul, g.aug, g.sep], m, { full: 2, id: 'gf', w: 420, h: 110, aria: T.clicksMonth })}<p class="dz-mut dz-s">${T.fullMonthNote}</p></div>`;
  }
  if (E && E.metrics) {
    const rows = E.metrics.map(x => { const f = x.key === 'position' || x.key === 'ctr' ? 1 : 0; return `<tr><td><b>${esc(x.label)}</b></td><td>${dshN(x.before, f)}${x.unit ? ' ' + x.unit : ''}</td><td><b>${dshN(x.after, f)}${x.unit ? ' ' + x.unit : ''}</b></td><td>${dshN(x.latest, f)}${x.unit ? ' ' + x.unit : ''}</td><td>${dshGDelta(x)}</td></tr>`; }).join('');
    html += `<div class="dz-card dz-gap2"><h2>${esc(E.title)}</h2><p class="dz-mut">${T.before}: ${esc(E.windows.before.label)} · ${T.after}: ${esc(E.windows.after.label)} · ${T.latest}: ${esc(E.windows.latest.label)}</p>
 <table class="dz-t"><tr><th></th><th>${T.before}</th><th>${T.after}</th><th>${T.latest}</th><th></th></tr>${rows}</table>
 ${(E.queries || []).map(q => `<p class="dz-sentence"><b>${T.queries}: „${esc(q.query)}“</b><br>${dshN(q.before.position, 1)} → <b>${dshN(q.after.position, 1)}</b> (${T.latest}: ${dshN(q.latest.position, 1)}) · ${dshN(q.before.clicks)} → <b>${dshN(q.after.clicks)}</b> ${dshLang() === 'de' ? 'Klicks' : 'clicks'}</p>`).join('')}
 ${E.note ? `<p class="dz-mut dz-s">${esc(E.note)}</p>` : ''}<p class="dz-chk">${T.checked} · ${esc(E.read)}</p></div>`;
  }
  if (DD.citations) {
    const c = DD.citations, pct = c.total ? Math.round(c.live / c.total * 100) : 0;
    html += `<div class="dz-card dz-gap2"><h2>${T.listings}</h2><div class="dz-row"><span class="dz-b"><i style="width:${pct}%"></i></span><span class="dz-c" style="flex-basis:90px">${c.live} ${T.of} ${c.total}</span></div></div>`;
  }
  return html;
}
function dshGReviews() {
  const T = dshT(), r = DD.ergebnisse && DD.ergebnisse.reviews;
  if (!r) return `${dshGTabs(DSH.b, 'results')}${dshGSub('reviews')}<h1 class="dz-t">${T.reviewsTitle}</h1><div class="dz-gapcard"><p class="dz-mut">${T.notMeasured}</p></div>`;
  const row = (l, x) => x ? `<tr><td><b>${l}</b> <span class="dz-mut dz-s">${esc(x.date || '')}</span></td><td>${dshN(x.n)}</td><td>${dshN(x.star, 1)} ★</td></tr>` : '';
  return `${dshGTabs(DSH.b, 'results')}${dshGSub('reviews')}<h1 class="dz-t">${T.reviewsTitle}</h1>
 <p class="dz-lead">${T.reviewsLead(dshN(r.after.n), dshN(r.after.star, 1))}</p>
 <div class="dz-card"><table class="dz-t"><tr><th></th><th>${dshLang() === 'de' ? 'Bewertungen' : 'Reviews'}</th><th>${dshLang() === 'de' ? 'Sterne' : 'Stars'}</th></tr>${row(T.before, r.before)}${row(T.after, r.after)}</table>${r.note ? `<p class="dz-mut dz-s">${esc(r.note)}</p>` : ''}<p class="dz-chk">${esc(r.source || '')}</p></div>`;
}
function dshGReports() {
  const T = dshT(), isRep = s => /Replaced|Ersetzt/i.test(s || '');
  return `${dshGTabs(DSH.b, 'reports')}<h1 class="dz-t">${T.reports}</h1><p class="dz-lead">${T.reportsLead}</p>
 <div class="dz-card"><table class="dz-t"><tr><th>${T.repReport}</th><th>${T.repPeriod}</th><th>${T.repState}</th><th></th></tr>${(DD.reports || []).map(r => `<tr><td><b>${esc(r[0])}</b></td><td>${esc(r[1])}</td><td>${isRep(r[3]) ? dshGSt('grey', T.replaced) : dshGSt('green', T.current)}</td><td>${r[4] ? `<a class="dz-btn dz-o" href="#" onclick="dshOpenReport('${r[4]}','${esc(r[0]).replace(/'/g, '')}');return false">${T.open}</a>` : ''}</td></tr>`).join('')}</table></div>`;
}
function dshGDecisions(b) { const T = dshT(); const draft = DSH.admin && dshDecItems(b).some(i => i.status === 'draft'); return `${dshGTabs(b, 'decisions')}<h1 class="dz-t">${T.decisionsTitle}</h1>${draft ? `<div class="dz-banner dz-amber"><span><b>Vorschau für 741.</b> Diese Karten sind Entwürfe. Der Kunde sieht sie erst nach der Freigabe im Chat.</span></div>` : ''}${apRenderClient(b, DSH.admin)}`; }
function dshGSetup(b) { const T = dshT(), st = dshSteps(b), nb = Object.assign({}, b, { steps: st }); return `${dshGTabs(b, 'setup')}<h1 class="dz-t">${T.setupTitle}</h1><div class="dz-grid">${renderOnboarding(nb, false)}${renderGrants(b, false)}</div>`; }
function dshGInner(b) {
  const v = DSH.view.split('/'), sub = v[1] || 'enquiries';
  if (v[0] === 'results') return ({ enquiries: dshGEnquiries, found: dshGFound, reviews: dshGReviews }[sub] || (DD.ga4_events ? dshGEnquiries : dshGFound))();
  if (v[0] === 'reports') return dshGReports();
  if (v[0] === 'decisions') return dshGDecisions(b);
  if (v[0] === 'setup') return dshGSetup(b);
  if (v[0] === 'plan' && dshGHasPlan()) return dshPlan();
  return dshGOverview(b);
}
