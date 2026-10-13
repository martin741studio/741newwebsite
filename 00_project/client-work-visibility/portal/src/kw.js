/* ---------- Kundenarbeit (Client work view) · 2026-10-13 ----------
   Design: 00_project/client-work-visibility/ (brief.md, data-model.md). Step 1 = admin only.
   Data: work_items, work_actors, work_client_health, work_evidence, work_outcomes, work_phases, work_goals, work_dependencies, work_events.
   Rules (the database enforces them): an agent sets only needs_check; "done" needs a person and proof. */
const KW = { data: null, kpi: null, owner: 'Alle', busy: false };
const KW_ST = { intake: 'Neu', planned: 'Geplant', in_progress: 'In Arbeit', waiting: 'Wartet', needs_check: 'Prüfen', done: 'Erledigt', dropped: 'Verworfen' };
const KW_WAIT = { client: 'Kunde', martin: 'Martin', team: 'Team', google: 'Google', external: 'Extern' };
const KW_BAND = { red: 'Rot', yellow: 'Gelb', green: 'Grün', no_data: 'Keine Daten' };
const KW_TODAY = () => new Date().toISOString().slice(0, 10);
const kwD = (d) => d ? new Date(d).toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit' }) : '';
const kwDays = (d) => d ? Math.max(0, Math.round((new Date(KW_TODAY()) - new Date(String(d).slice(0, 10))) / 864e5)) : 0;
const kwAge = (d) => { const n = kwDays(d); return n === 0 ? 'heute' : n === 1 ? 'seit 1 Tag' : 'seit ' + n + ' Tagen'; };

async function kwLoad() {
  const [it, ac, he, ev, oc, ph, go, dp, evn, cl] = await Promise.all([
    db.from('work_items').select('*').order('created_at'),
    db.from('work_actors').select('*'),
    db.from('work_client_health').select('*'),
    db.from('work_evidence').select('*'),
    db.from('work_outcomes').select('*').order('measured_at', { ascending: false }),
    db.from('work_phases').select('*'),
    db.from('work_goals').select('*'),
    db.from('work_dependencies').select('*'),
    db.from('work_events').select('*').order('at', { ascending: false }).limit(400),
    db.from('clients').select('id,name')
  ]);
  if (it.error) return { error: it.error.message };
  const A = {}; (ac.data || []).forEach(a => A[a.id] = a);
  const C = {}; (cl.data || []).forEach(c => C[c.id] = c.name);
  return { items: it.data || [], A, C, health: he.data || [], ev: ev.data || [], oc: oc.data || [], ph: ph.data || [], go: go.data || [], dp: dp.data || [], events: evn.data || [] };
}
async function kwReload() { KW.data = await kwLoad(); }
function kwMe() { const A = KW.data.A; return Object.values(A).find(a => me && a.user_id === me.user_id) || Object.values(A).find(a => a.kind === 'admin'); }
const kwName = (id) => (KW.data.A[id] || {}).name || '–';
const kwKind = (id) => (KW.data.A[id] || {}).kind || 'external';
const kwWho = (id) => `<span class="kw-who kw-w-${esc(kwKind(id))}">${esc(kwName(id))}</span>`;
const kwStatus = (i) => `<span class="kw-st kw-s-${esc(i.status)}">${KW_ST[i.status] || esc(i.status)}${i.status === 'waiting' && i.waiting_on ? ' auf ' + esc(KW_WAIT[i.waiting_on] || i.waiting_on) : ''}</span>`;
const kwClient = (i) => i.client_id ? esc(KW.data.C[i.client_id] || '') : '741 (alle)';
const kwEv = (i) => KW.data.ev.filter(e => e.work_item_id === i.id);
const kwOpen = (i) => !['done', 'dropped'].includes(i.status);

function kwRow(i, showClient) {
  const today = KW_TODAY();
  const due = i.due_on ? (i.due_on < today ? `<b style="color:#c2410c">überfällig seit ${kwD(i.due_on)}</b>` : i.due_on === today ? '<b>heute fällig</b>' : 'fällig ' + kwD(i.due_on)) : '';
  const since = i.since || i.created_at;
  const old = kwDays(since) >= 7 && kwOpen(i);
  const blk = KW.data.dp.filter(d => d.blocked_id === i.id).map(d => KW.data.items.find(x => x.id === d.blocker_id)).filter(Boolean).filter(kwOpen);
  const src = kwEv(i).slice(0, 2).map(e => `<div class="kw-src">${e.relation === 'produced' ? '↳ ' : ''}${esc(e.label)}</div>`).join('') || '<span class="kw-next">–</span>';
  return `<tr class="kw-click" onclick="kwOpenItem('${i.id}')">${showClient ? `<td><b>${kwClient(i)}</b></td>` : ''}
    <td>${esc(i.title)}${blk.length ? `<div class="kw-next">⛔ blockiert durch: ${esc(blk[0].title.slice(0, 70))}</div>` : ''}${i.next_action ? `<div class="kw-next">→ ${esc(i.next_action)}</div>` : ''}</td>
    <td>${kwWho(i.accountable_id)}${i.doer_id !== i.accountable_id ? ' → ' + kwWho(i.doer_id) : ''}</td>
    <td>${kwStatus(i)}<div class="kw-age${old ? ' old' : ''}">${due || kwAge(since)}</div></td>
    <td>${src}</td></tr>`;
}

/* ----- Ansicht "Heute" (alle Kunden) ----- */
async function loadWorkview() {
  showApp('workview');
  $('workview').innerHTML = '<div class="muted">Lädt …</div>';
  await kwReload();
  kwRenderToday();
}
function kwRenderToday() {
  const d = KW.data, el = $('workview');
  if (d.error) { el.innerHTML = `<span class="backlink" onclick="showApp('admin-home')">← Übersicht</span><div class="card"><div class="err" style="display:block">${esc(d.error)}</div></div>`; return; }
  const meId = kwMe() ? kwMe().id : null, today = KW_TODAY();
  const open = d.items.filter(kwOpen);
  const K = [
    ['mine', 'Wartet auf dich', open.filter(i => i.doer_id === meId && i.status !== 'waiting')],
    ['check', 'Prüfen (Agent/Team fertig)', open.filter(i => i.status === 'needs_check')],
    ['team', 'Team/Agent wartet auf dich', open.filter(i => i.status === 'waiting' && i.waiting_on === 'martin')],
    ['client', 'Wartet auf Kunde / Google', open.filter(i => i.status === 'waiting' && ['client', 'google', 'external'].includes(i.waiting_on))],
    ['agents', 'Agenten arbeiten', open.filter(i => ['agent', 'script'].includes(kwKind(i.doer_id)) && i.status === 'in_progress')]
  ];
  let list = KW.kpi ? K.find(k => k[0] === KW.kpi)[2] : [
    ...open.filter(i => i.doer_id === meId && i.status !== 'waiting' && i.due_on && i.due_on <= today),
    ...open.filter(i => i.status === 'needs_check'),
    ...open.filter(i => i.status === 'waiting' && i.waiting_on === 'martin')];
  list = list.slice(0, 12);
  const rank = { red: 0, yellow: 1, no_data: 2, green: 3 };
  const hs = d.health.filter(h => !/^Testpraxis/.test(h.name)).sort((a, b) => rank[a.band] - rank[b.band] || a.name.localeCompare(b.name));
  const ex = hs.filter(h => h.band !== 'green'), ok = hs.filter(h => h.band === 'green');
  el.innerHTML = `<span class="backlink" onclick="showApp('admin-home')">← Übersicht</span>
  <div class="kw-h1">Heute · ${kwD(today)}</div>
  <p class="kw-lead">Oben steht nur, was dich braucht. Jede Zeile zeigt, wer verantwortlich ist, wer es macht, den Status mit Alter und die Quelle. Ein Klick öffnet die Details.</p>
  <div class="kw-kpis">${K.map(k => `<button class="kw-kpi${KW.kpi === k[0] ? ' on' : ''}" onclick="KW.kpi=KW.kpi==='${k[0]}'?null:'${k[0]}';kwRenderToday()"><b>${k[2].length}</b><span>${k[1]}</span></button>`).join('')}</div>
  <div class="kw-grid2">
    <div class="card"><h2>${KW.kpi ? esc(K.find(k => k[0] === KW.kpi)[1]) : 'Zuerst erledigen'} <span class="muted">max. 12${KW.kpi ? ' · <a href="#" onclick="KW.kpi=null;kwRenderToday();return false">alle</a>' : ''}</span></h2>
      <table class="kw-tbl"><thead><tr><th>Kunde</th><th>Aufgabe · nächster Schritt</th><th>Verantwortlich → macht</th><th>Status</th><th>Quelle</th></tr></thead><tbody>${list.map(i => kwRow(i, true)).join('') || '<tr><td colspan="5" class="muted">Nichts offen.</td></tr>'}</tbody></table></div>
    <div class="card"><h2>Kunden <span class="muted">${ex.length} brauchen Aufmerksamkeit</span></h2>
      <table class="kw-tbl"><tbody>${ex.map(h => `<tr class="kw-click" onclick="adminSub='work';openClient('${h.client_id}')"><td><b>${esc(h.name)}</b><div class="kw-next">${esc(h.reason)}</div>${h.next_action ? `<div class="kw-next">→ ${esc(h.next_action)}</div>` : ''}</td><td><span class="kw-band kw-${esc(h.band)}">${KW_BAND[h.band]}</span><div class="kw-age">${h.open_items} offen · ${h.waiting_on_client} beim Kunden</div></td></tr>`).join('')}</tbody></table>
      ${ok.length ? `<div class="kw-ok">✓ ${ok.length} im Plan: ${ok.map(h => `<a href="#" onclick="adminSub='work';openClient('${h.client_id}');return false">${esc(h.name)}</a>`).join(', ')}</div>` : ''}
      <p class="muted" style="margin-top:10px">Die Farbe kommt automatisch aus den Aufgaben: Blocker, Überfälliges, Wartezeit, Prüfungen, ungesichtete Wünsche. Der Grund steht immer daneben.</p></div>
  </div>`;
}

/* ----- Kundenseite (im Admin-Kundenkopf: Knopf "Kundenarbeit") ----- */
function kwAdminButton(b) {
  const h = KW.data && KW.data.health ? KW.data.health.find(x => x.client_id === b.client.id) : null;
  return `<button class="btn btn-small btn-ghost" onclick="adminSub='work';rerender()">Kundenarbeit${h ? ' · ' + KW_BAND[h.band] : ''}</button>`;
}
function kwRenderClient(b) {
  if (!KW.data) { kwReload().then(rerender); return '<div class="muted">Lädt …</div>'; }
  const d = KW.data, cid = b.client.id;
  if (d.error) return `<div class="card"><div class="err" style="display:block">${esc(d.error)}</div></div>`;
  const h = d.health.find(x => x.client_id === cid);
  const goal = d.go.find(g => g.client_id === cid);
  const order = ['P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6'];
  const ph = d.ph.filter(p => p.client_id === cid).sort((a, x) => order.indexOf(a.code) - order.indexOf(x.code));
  const all = d.items.filter(i => i.client_id === cid);
  const pass = i => KW.owner === 'Alle' || (KW.owner === 'Martin' ? kwKind(i.doer_id) === 'admin' : KW.owner === 'Team' ? kwKind(i.doer_id) === 'team' : KW.owner === 'Agent' ? ['agent', 'script'].includes(kwKind(i.doer_id)) : kwKind(i.doer_id) === 'client');
  const rankS = { needs_check: 0, planned: 1, in_progress: 2, waiting: 3, intake: 4, done: 5, dropped: 6 };
  const tasks = all.filter(i => i.type !== 'client_todo' && pass(i) && kwOpen(i)).sort((a, x) => rankS[a.status] - rankS[x.status]);
  const done = all.filter(i => i.status === 'done');
  const todos = all.filter(i => i.type === 'client_todo' && kwOpen(i));
  const oc = d.oc.filter(o => o.client_id === cid);
  const feed = d.events.filter(e => e.client_id === cid).slice(0, 25);
  return `<span class="backlink" onclick="adminSub=null;rerender()">← Zur Kundenseite</span>
  <div class="kw-h1">Kundenarbeit · ${esc(b.client.name)} ${h ? `<span class="kw-band kw-${esc(h.band)}" style="vertical-align:middle">${KW_BAND[h.band]}</span>` : ''}</div>
  ${h ? `<p class="kw-lead">${esc(h.reason)}${h.next_action ? ' · → ' + esc(h.next_action) : ''}</p>` : ''}
  ${goal ? `<div class="kw-next" style="margin-bottom:4px"><b style="color:#252525">Quartalsziel:</b> ${esc(goal.title)}${goal.due_on ? ' · bis ' + kwD(goal.due_on) : ''} <span class="muted">(${esc(goal.status === 'proposed' ? 'Vorschlag' : goal.status)})</span></div>` : ''}
  ${ph.length ? `<div class="kw-phases">${ph.map(p => `<div class="kw-ph ${esc(p.status)}">${esc(p.code)}<small>${esc(p.label)}</small></div>`).join('')}</div>` : ''}
  <div class="kw-grid2" style="margin-top:14px">
   <div>
    <div class="card"><h2>Aufgaben <span class="muted">${tasks.length} offen · eine Liste für alle</span></h2>
      <div class="kw-chips">${['Alle', 'Martin', 'Team', 'Agent', 'Kunde'].map(o => `<button class="kw-chip${KW.owner === o ? ' on' : ''}" onclick="KW.owner='${o}';rerender()">${o}</button>`).join('')}</div>
      <table class="kw-tbl"><thead><tr><th>Aufgabe · nächster Schritt</th><th>Verantwortlich → macht</th><th>Status</th><th>Quelle</th></tr></thead><tbody>${tasks.map(i => kwRow(i, false)).join('') || '<tr><td colspan="4" class="muted">Nichts in diesem Filter.</td></tr>'}</tbody></table>
      ${done.length ? `<div class="kw-next" style="margin-top:8px">✓ ${done.length} erledigt mit Nachweis</div>` : ''}</div>
    <div class="card"><h2>Ergebnisse <span class="muted">mit Nachweis</span></h2>${oc.map(o => { const p = d.ev.filter(e => e.outcome_id === o.id); return `<div class="kw-outc"><div class="ct">${esc(o.client_text)}</div><div class="meta">${o.metric_key ? `<span>Zielzahl: ${esc(o.metric_key)}</span>` : ''}<span>vorher ${esc(o.value_before ?? '–')} → nachher ${esc(o.value_after ?? '–')}</span><span>${o.confidence === 'confirmed' ? 'bestätigt' : 'angenommen'}</span><span>${kwD(o.measured_at)}</span></div><div class="meta"><span>Nachweis: ${p.map(e => esc(e.label)).join(', ') || '–'}</span><span>Zeit/Kosten: ${o.minutes_spent || o.cost_eur ? esc((o.minutes_spent || '–') + ' Min · ' + (o.cost_eur || '–') + ' €') : 'nicht erfasst'}</span><span>${o.visibility === 'client' ? '👁 Kunde sieht es (später)' : '🔒 intern'}</span></div></div>`; }).join('') || '<div class="muted">Noch keine Ergebnisse erfasst.</div>'}</div>
   </div>
   <div>
    <div class="card"><h2>Wartet auf den Kunden <span class="muted">${todos.length}</span></h2><table class="kw-tbl"><tbody>${todos.map(i => `<tr class="kw-click" onclick="kwOpenItem('${i.id}')"><td>${esc(i.title)}</td><td><span class="kw-age${kwDays(i.since || i.created_at) >= 7 ? ' old' : ''}">${kwAge(i.since || i.created_at)}</span></td></tr>`).join('') || '<tr><td class="muted">Nichts.</td></tr>'}</tbody></table></div>
    <div class="card"><h2>Verlauf <span class="muted">letzte 25</span></h2><div class="kw-feed">${feed.map(e => { const it = d.items.find(x => x.id === e.work_item_id); return `<div>${kwD(e.at)} · <b>${esc(e.actor_id ? kwName(e.actor_id) : 'System')}</b> · ${e.type === 'status' ? esc((KW_ST[e.from_status] || '') + ' → ' + (KW_ST[e.to_status] || '')) : e.type === 'handoff' ? 'übergeben an ' + esc(kwName(e.to_actor)) : e.type === 'created' ? 'angelegt' : esc(e.type)}<br><i>${esc(it ? it.title.slice(0, 80) : '')}</i></div>`; }).join('') || '<div><i>Noch kein Verlauf.</i></div>'}</div></div>
   </div>
  </div>`;
}

/* ----- Detail + Aktionen ----- */
function kwCloseItem() { const d = $('kw-drawer'); if (d) d.remove(); }
function kwOpenItem(id) {
  kwCloseItem();
  const d = KW.data, i = d.items.find(x => x.id === id); if (!i) return;
  const ev = kwEv(i), hasProof = ev.some(e => ['proves', 'produced'].includes(e.relation));
  const isA = me && me.role === 'admin';
  let acts = '';
  if (isA && i.status === 'needs_check') acts = `<div class="kw-acts">${hasProof ? '' : '<input id="kw-proof" placeholder="Nachweis-Link (URL, Datei, Drive)" style="flex:1;min-width:200px">'}<button class="kw-btn kw-by" onclick="kwDone('${i.id}')">Geprüft → Erledigt</button><button class="kw-btn kw-b2" onclick="kwSetStatus('${i.id}','in_progress')">Zurück an ${esc(kwName(i.doer_id))}</button></div>`;
  else if (isA && kwOpen(i) && kwKind(i.doer_id) === 'admin') acts = `<div class="kw-acts"><input id="kw-proof" placeholder="Nachweis-Link (Pflicht für Erledigt)" style="flex:1;min-width:200px"><button class="kw-btn kw-b1" onclick="kwDone('${i.id}')">Erledigt</button></div>`;
  const blk = d.dp.filter(x => x.blocked_id === i.id).map(x => d.items.find(y => y.id === x.blocker_id)).filter(Boolean);
  const hist = d.events.filter(e => e.work_item_id === i.id).slice(0, 10);
  const el = document.createElement('aside'); el.className = 'kw-drawer'; el.id = 'kw-drawer';
  el.innerHTML = `<button class="x" onclick="kwCloseItem()">×</button><h3 style="margin:0 0 8px">${esc(i.title)}</h3>${kwStatus(i)}
  <dl class="kw-dl"><dt>Kunde</dt><dd>${kwClient(i)}</dd><dt>Verantwortlich</dt><dd>${kwWho(i.accountable_id)}</dd><dt>Macht es</dt><dd>${kwWho(i.doer_id)}</dd>
  <dt>Nächster Schritt</dt><dd>${esc(i.next_action || '–')}</dd><dt>Grund</dt><dd>${esc(i.status_reason || '–')}</dd><dt>Alter</dt><dd>${kwAge(i.since || i.created_at)}</dd>${i.due_on ? `<dt>Fällig</dt><dd>${kwD(i.due_on)}</dd>` : ''}
  ${blk.length ? `<dt>Blockiert durch</dt><dd>${blk.map(x => esc(x.title)).join('<br>')}</dd>` : ''}
  <dt>Fertig heißt</dt><dd>${esc(i.definition_of_done || '–')}</dd>
  <dt>Quellen</dt><dd>${ev.map(e => `${e.url ? `<a href="${esc(e.url)}" target="_blank" rel="noopener">${esc(e.label)}</a>` : esc(e.label)} <span class="muted">(${e.relation === 'produced' ? 'erzeugt' : e.relation === 'proves' ? 'Nachweis' : 'genutzt'})</span>`).join('<br>') || '–'}</dd>
  <dt>Herkunft</dt><dd>${esc(i.source)} · ${esc(i.source_id)}</dd><dt>Sichtbar</dt><dd>${i.visibility === 'client' ? '👁 Kunde (ab Schritt 3)' : '🔒 intern'}</dd></dl>
  ${acts}<p class="muted" style="margin-top:8px">Erledigt geht nur mit Nachweis und nur durch eine Person. Ein Agent setzt höchstens „Prüfen“.</p>
  <h3 style="margin:16px 0 6px;font-size:15px">Verlauf</h3><div class="kw-feed">${hist.map(e => `<div>${kwD(e.at)} · <b>${esc(e.actor_id ? kwName(e.actor_id) : 'System')}</b> · ${esc(e.type)}${e.to_status ? ' → ' + esc(KW_ST[e.to_status] || e.to_status) : ''}</div>`).join('')}</div>`;
  document.body.appendChild(el);
}
async function kwDone(id) {
  if (KW.busy) return; KW.busy = true;
  try {
    const i = KW.data.items.find(x => x.id === id), meA = kwMe();
    const inp = $('kw-proof'), url = inp ? inp.value.trim() : '';
    const hasProof = kwEv(i).some(e => ['proves', 'produced'].includes(e.relation));
    if (!hasProof && !url) { toast('Bitte zuerst einen Nachweis-Link eintragen.'); return; }
    if (url) {
      const r = await db.from('work_evidence').insert({ client_id: i.client_id, work_item_id: i.id, kind: 'page', relation: 'proves', label: url.slice(0, 120), url, created_by: meA.id });
      if (r.error) { toast('Fehler: ' + r.error.message); return; }
    }
    const { error } = await db.from('work_items').update({ status: 'done', verified_by: meA.id, status_reason: 'Geprüft von ' + meA.name }).eq('id', i.id);
    if (error) { toast('Fehler: ' + error.message); return; }
    toast('Erledigt, mit Nachweis.');
    kwCloseItem(); await kwReload(); kwRefresh();
  } finally { KW.busy = false; }
}
async function kwSetStatus(id, st) {
  const { error } = await db.from('work_items').update({ status: st, status_reason: 'Zurück an den Macher' }).eq('id', id);
  if (error) { toast('Fehler: ' + error.message); return; }
  kwCloseItem(); await kwReload(); kwRefresh();
}
function kwRefresh() { if (!$('workview').classList.contains('hidden')) kwRenderToday(); else rerender(); }
/* ---------- Ende Kundenarbeit ---------- */
