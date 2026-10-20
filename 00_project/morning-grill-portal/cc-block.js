const CC = { tfilter: 'all', snap: null, snapId: null, created: null, mode: null, answers: {}, picks: {}, parking: null, owning: null, reopen: {}, tab: 'today', filter: 'all' };
const CC_ICON = { dec: '✅', you: '👆', msg: '✉️', appr: '⏳', wait: '🕒', block: '⛔', later: '📋' };

async function loadGrill() {
  const el = $('grill');
  if (!me || me.role !== 'admin') { el.innerHTML = '<span class="backlink" onclick="showApp(\'admin-home\')">← Übersicht</span><div class="card"><div class="muted">Nur für Admins.</div></div>'; return; }
  el.innerHTML = '<div class="muted">…</div>';
  const { data, error } = await db.from('grill_snapshots').select('id,run_date,mode,created_at,data').order('id', { ascending: false }).limit(1);
  if (error) { el.innerHTML = '<span class="backlink" onclick="showApp(\'admin-home\')">← Übersicht</span><div class="card"><div class="err" style="display:block;">' + esc(error.message) + '</div></div>'; return; }
  if (!data.length) { el.innerHTML = '<span class="backlink" onclick="showApp(\'admin-home\')">← Übersicht</span><div class="card"><div class="muted">Noch kein Snapshot. Der Morning-Grill-Lauf schreibt ihn.</div></div>'; return; }
  CC.snap = data[0].data; CC.snapId = data[0].id; CC.created = data[0].created_at; CC.mode = data[0].mode;
  const { data: ans } = await db.from('grill_answers').select('card_id,option,note,answered_at').gte('run_date', CC.snap.date).order('id', { ascending: true });
  CC.answers = {};
  (ans || []).forEach(a => { CC.answers[a.card_id] = a; });
  ccRender();
}

async function ccLoadWork() {
  try {
    const [a, b, c] = await Promise.all([
      db.from('work_items').select('id,title,status,waiting_on,due_on,next_action,status_reason,source,source_id,client_id,doer_id').neq('status', 'dropped').order('updated_at', { ascending: false }).limit(500),
      db.from('work_actors').select('id,kind,name'),
      db.from('clients').select('id,name')]);
    const err = a.error || b.error || c.error;
    if (err) throw new Error(err.message);
    const act = {}; (b.data || []).forEach(x => { act[x.id] = x; });
    const cli = {}; (c.data || []).forEach(x => { cli[x.id] = x.name; });
    CC.work = (a.data || []).map(w => { const d = act[w.doer_id] || {}; return { id: w.id, title: w.title, status: w.status, waiting_on: w.waiting_on, due: w.due_on, next: w.next_action, reason: w.status_reason, source: w.source, source_id: w.source_id, client: cli[w.client_id] || '', owner: d.kind === 'agent' ? 'agent' : (d.kind === 'external' ? 'external' : (d.kind === 'client' ? 'client' : (d.name || '?'))) }; });
    CC.workErr = null;
  } catch (e) { CC.work = null; CC.workErr = e.message; }
}

function ccEff(c) {
  const a = CC.answers[c.id];
  if (CC.reopen[c.id]) return { status: 'open', answer: null, text: null };   // "Change answer" (Martin 13.10.)
  if (a) return { status: a.option === 'park' ? 'parked' : 'decided', answer: a.option, text: (a.option === 'park' || a.option === 'own') ? a.note : ((c.options[a.option] || a.option) + (a.note ? ' (' + a.note + ')' : '')) };
  if (c.status === 'decided' || c.status === 'parked') return { status: c.status, answer: c.answer, text: c.answer_text };
  return { status: 'open', answer: null, text: null };
}
function ccWalkDone(w) { return !!CC.answers[w.id]; }

function ccTab(t) { CC.tab = t; ccRender(); }
function ccFilter(f) { CC.filter = f; ccRender(); }
function ccPick(id, k) { CC.picks[id] = k; CC.parking = null; CC.owning = null; ccRender(); }
function ccParkOpen(id) { CC.parking = id; CC.owning = null; CC.picks[id] = null; ccRender(); }
function ccOwnOpen(id) { CC.owning = id; CC.parking = null; CC.picks[id] = null; ccRender(); const ta = $('cc-own-' + id); if (ta) ta.focus(); }
function ccReopen(id) { CC.reopen[id] = true; CC.picks[id] = null; ccRender(); }
function ccSaveOwn(id) {
  const t = ($('cc-own-' + id).value || '').trim();
  if (!t) { alert('Please write your answer first.'); return; }
  ccSave(id, 'own', t);
}
async function ccSave(id, option, note) {
  const { error } = await db.from('grill_answers').insert({ card_id: id, run_date: CC.snap.date, option, note: note || null });
  if (error) { alert(error.message); return; }
  CC.answers[id] = { card_id: id, option, note: note || null, answered_at: new Date().toISOString() };
  delete CC.picks[id]; delete CC.reopen[id]; CC.parking = null; CC.owning = null; ccRender();
}
function ccSavePick(id) { if (CC.picks[id]) ccSave(id, CC.picks[id], null); }
function ccSavePark(id) {
  const t = ($('cc-ta-' + id).value || '').trim();
  if (!t) { alert('Park needs a reason.'); return; }
  ccSave(id, 'park', t);
}
function ccWalk(id) { if (!CC.answers[id]) ccSave(id, 'done', null); }

function ccCard(c) {
  const ef = ccEff(c), done = ef.status !== 'open';
  const vars = Object.keys(c.options).map(k => {
    const sel = (done ? ef.answer === k : CC.picks[c.id] === k) ? ' sel' : '';
    const then = c.then && c.then[k] ? `<div class="then">Then: ${esc(c.then[k])}</div>` : '';
    const rec = k === c.recommended ? '<span class="cc-rec">741 recommends</span>' : '';
    return `<button class="cc-var${sel}" ${done ? 'disabled' : ''} onclick="ccPick('${esc(c.id)}','${esc(k)}')"><div class="lab">Option ${esc(k.toUpperCase())} ${rec}</div><div class="val">${esc(c.options[k])}</div>${then}</button>`;
  }).join('');
  let acts = '';
  if (!done) {
    acts = `<div class="cc-acts"><button class="btn btn-yellow" ${CC.picks[c.id] ? '' : 'disabled style="opacity:.5"'} onclick="ccSavePick('${esc(c.id)}')">Save answer</button><button class="cc-link" onclick="ccOwnOpen('${esc(c.id)}')">Write own answer</button><button class="cc-link" onclick="ccParkOpen('${esc(c.id)}')">Park with reason</button>${CC.reopen[c.id] ? `<button class="cc-link" onclick="delete CC.reopen['${esc(c.id)}'];ccRender()">Cancel</button>` : ''}</div>`;
    if (CC.owning === c.id) acts += `<textarea class="cc-ta" id="cc-own-${esc(c.id)}" placeholder="Your answer in your own words. The agent works with exactly this."></textarea><div class="cc-acts"><button class="btn btn-yellow" onclick="ccSaveOwn('${esc(c.id)}')">Save own answer</button></div>`;
    if (CC.parking === c.id) acts += `<textarea class="cc-ta" id="cc-ta-${esc(c.id)}" placeholder="Why do you park this? The card returns only when the reason changes."></textarea><div class="cc-acts"><button class="btn btn-yellow" onclick="ccSavePark('${esc(c.id)}')">Park</button></div>`;
  }
  const own = ef.answer === 'own' || ef.answer === 'other';
  const res = done ? `<div class="cc-res${ef.status === 'parked' ? ' park' : ''}">${ef.status === 'parked' ? 'Parked' : own ? 'Decided (own answer)' : 'Decided'}: ${esc(ef.text || ef.answer || '')} <button class="cc-link" onclick="ccReopen('${esc(c.id)}')">Change answer</button></div>` : '';
  const ev = (c.evidence || []).map(x => `<li>${esc(x)}</li>`).join('');
  return `<article id="cc-card-${esc(c.id)}" class="cc-item p${c.priority}${done ? ' done' : ''}"><div class="cc-itop"><span class="cc-type">${esc(c.type)}</span><b>${esc(c.client)}</b><span class="dl">card ${c.n} · by ${esc(c.deadline)}</span></div>
<h3>${esc(c.headline)}</h3><div class="cc-why"><b>Why:</b> ${esc(c.why)}</div><div class="cc-vars">${vars}</div>${acts}${res}
<details class="cc-ev"><summary>Evidence (${(c.evidence || []).length})</summary><ul>${ev}</ul></details></article>`;
}

function ccDecisions() {
  const s = CC.snap;
  const eff = s.cards.map(c => ({ c, e: ccEff(c) }));
  const nOpen = eff.filter(x => x.e.status === 'open').length;
  const f = CC.filter;
  const show = eff.filter(x => f === 'all' || (f === 'open' && x.e.status === 'open') || (f === 'decided' && x.e.status !== 'open') || (f === 'p1' && x.c.priority === 1) || (f === 'p2' && x.c.priority === 2) || (f === 'clicks' && x.c.type === 'Your click') || (f === '741' && x.c.client.startsWith('741')) || (f === 'client' && !x.c.client.startsWith('741')));
  const tiles = [[`${s.cards.length - nOpen}/${s.cards.length}`, 'decisions taken'], [String(nOpen), 'cards open'], [String(s.clients.length), 'active clients'], [String(s.sources.filter(x => x.status !== 'ok').length), 'unreadable sources']];
  const chips = [['all', 'All'], ['open', 'Open'], ['decided', 'Decided'], ['p1', 'Fire'], ['p2', 'Money / contract'], ['clicks', 'Your clicks'], ['client', 'Client'], ['741', '741']].map(([k, l]) => `<button class="cc-chip${f === k ? ' on' : ''}" onclick="ccFilter('${k}')">${l}</button>`).join('');
  const walk = s.walk.map(w => `<li class="${ccWalkDone(w) ? 'done' : ''}"><input type="checkbox" ${ccWalkDone(w) ? 'checked disabled' : ''} onchange="ccWalk('${esc(w.id)}')"><span>${esc(w.text)}</span></li>`).join('') || '<li>nothing open</li>';
  const later = s.later.map(x => `<li><b>${esc(x.client)}</b> — ${esc((x.headline || '').slice(0, 120))}</li>`).join('') || '<li>nothing</li>';
  return `<div class="cc-tiles">${tiles.map(t => `<div class="cc-tile"><b>${esc(t[0])}</b><span>${esc(t[1])}</span></div>`).join('')}</div>
<div class="cc-chips">${chips}</div>${show.map(x => ccCard(x.c)).join('') || '<div class="muted">No card in this filter.</div>'}
${s.walk.length ? `<div class="cc-panel" style="margin-bottom:14px"><h4>Your walk queue (1–5 min clicks)</h4><ul class="cc-walk">${walk}</ul></div>` : ''}<div class="cc-panel"><h4>Later list (next grill or Monday)</h4><ul>${later}</ul></div>`;
}

function ccClients() {
  const s = CC.snap;
  const nav = s.clients.map(c => `<a class="cc-chip" href="#cc-${esc(c.anchor)}" onclick="document.getElementById('cc-${esc(c.anchor)}').scrollIntoView({behavior:'smooth'});return false;">${esc(c.name)}</a>`).join('');
  const body = s.clients.map(c => {
    const wk = c.week != null ? `<div class="cc-week"><div class="cc-wbar"><i style="width:${Math.min(100, Math.round(c.week / 13 * 100))}%"></i></div><span>Program week ${esc(c.week)} of 13 · onboarding ${esc(c.ob_done)}/${esc(c.ob_total)}</span></div>` : '<div class="cc-week"><span>No program week in the portal</span></div>';
    const road = c.roadmap.map(r => `<div class="cc-step ${esc(r.state)}"><span class="sid">${esc(r.id)}</span><span class="sl">${esc(r.label)}</span><div class="cc-wfs">${r.wfs.map(w => `<span class="cc-wf ${esc(w.cls)}" title="${esc(w.title)}">${esc(w.label)}</span>`).join('') || '<span class="cc-wf">—</span>'}</div></div>`).join('');
    const open = c.open.map(o => `<li class="${esc(o.kind)}"><span class="ic">${CC_ICON[o.kind] || '•'}</span><span>${esc(o.text)}</span></li>`).join('') || '<li>nothing open</li>';
    const next = c.next.map(x => `<li><span class="ic">➜</span><span>${esc(x)}</span></li>`).join('') || '<li>no next step set → define card</li>';
    const moved = c.moved.map(x => `<li class="moved"><span class="ic">✓</span><span>${esc(x)}</span></li>`).join('') || '<li>nothing since the last grill</li>';
    const nums = c.numbers.length ? `<table class="cc-nums"><tr><th>Number</th><th>Now</th><th>Target</th><th>Due</th><th></th></tr>${c.numbers.map(n => `<tr><td>${esc(n.metric)}</td><td>${esc(n.baseline ?? '?')}</td><td>${esc(n.target ?? '?')}</td><td>${esc(n.due || '')}</td><td class="${esc(n.status)}">${esc(n.status)}</td></tr>`).join('')}</table>` : '<div class="muted">No goal numbers yet → define card</div>';
    return `<section class="cc-cl" id="cc-${esc(c.anchor)}"><div class="cc-clh"><h3>${esc(c.name)}</h3><span class="pill pill-grey">${esc(c.status)}</span><span class="pill pill-yellow">${esc(c.phase)} · ${esc(c.phase_label)}</span></div>
<div class="cc-goal"><b>Goal:</b> ${esc(c.goal || 'missing')}</div>${wk}<div class="cc-road">${road}</div>
<div class="cc-cols3"><div><h5>Open now</h5><ul>${open}</ul></div><div><h5>Next steps to the goal</h5><ul>${next}</ul><h5>Moved since last grill</h5><ul>${moved}</ul></div><div><h5>Goal numbers</h5>${nums}<div class="cc-goal" style="font-size:14px"><b>Milestone:</b> ${esc(c.milestone || 'not set')}</div></div></div></section>`;
  }).join('');
  return `<div class="cc-legend"><span class="cc-wf done">approved</span> <span class="cc-wf wait">waits for your approval</span> <span class="cc-wf run">in progress</span> <span class="cc-wf dry">dry run</span> · roadmap: green = phase done, yellow = phase now</div><div class="cc-chips">${nav}</div>${body}`;
}

function ccAgents() {
  const s = CC.snap;
  const li = a => a.map(x => `<li>${esc(x)}</li>`).join('') || '<li>nothing</li>';
  const src = s.sources.map(x => `<li>${x.status === 'ok' ? '●' : '○'} ${esc(x.id)} ${x.status === 'ok' ? '' : '— ' + esc(x.error || 'unreadable')}</li>`).join('');
  return `<div class="cc-grid2"><div class="cc-panel"><h4>Agents working</h4><ul>${li(s.agents)}</ul></div><div class="cc-panel"><h4>Waiting for</h4><ul>${li(s.waiting)}</ul></div></div>
<div class="cc-panel" style="margin-top:14px"><h4>741 line</h4><ul>${li(s.line_741)}</ul></div><div class="cc-panel" style="margin-top:14px"><h4>Sources of this snapshot</h4><ul>${src}</ul></div>`;
}

function ccTfilter(f) { CC.tfilter = f; ccRender(); }
function ccGoCard(id) { CC.tab = 'dec'; CC.filter = 'all'; ccRender(); const el = document.getElementById('cc-card-' + id); if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
function ccTaskStatus(t) {
  const c = t.card && CC.snap.cards.find(x => x.id === t.card);
  if (c) {
    const ef = ccEff(c);
    if (ef.status === 'parked') return 'parked';
    if (ef.status === 'decided') return (c.type === 'Your click' && ef.answer === 'a' && c.options.a === 'Done') ? 'done' : 'decided';
  }
  return t.status;
}
function ccTasks() {
  const snapMap = {}; (CC.snap.tasks || []).forEach(t => { snapMap[CC.snap.date + '/' + t.id] = t; });
  let rows0;
  if (CC.work && CC.work.length) {
    rows0 = CC.work.map(w => {
      const sn = snapMap[w.source_id];
      let st = w.status === 'planned' || w.status === 'intake' ? 'open' : w.status;
      if (sn && sn.card) { const o = ccTaskStatus(sn); if (o === 'done' || o === 'parked' || o === 'decided') st = o; }
      return { t: { owner: w.owner, client: w.client || '741', title: w.title, due: w.due, next: w.next || w.reason, link: sn && sn.link, session: sn && sn.session, card: sn && sn.card, source_card: sn && sn.source_card, src: w.source }, st };
    });
  } else {
    rows0 = (CC.snap.tasks || []).map(t => ({ t: { ...t, src: 'snapshot' }, st: ccTaskStatus(t) }));
  }
  if (!rows0.length) return '<div class="cc-panel"><div class="muted">No tasks yet.</div></div>';
  const owners = ['Martin', 'agent', 'Dinakar', 'Tantri', 'Gayo', 'external', 'client'];
  const f = CC.tfilter;
  const order = { open: 0, in_progress: 1, waiting: 2, needs_check: 3, decided: 4, parked: 5, done: 6 };
  const label = { open: 'open', in_progress: 'in progress', waiting: 'waiting', needs_check: 'needs check', decided: 'decided', parked: 'parked', done: 'done' };
  const live = rows0.filter(x => x.st !== 'done');
  const cnt = o => live.filter(x => x.t.owner === o).length;
  const chips = [['all', `All (${live.length} open)`], ...owners.map(o => [o, `${o} (${cnt(o)})`])].map(([k, l]) => `<button class="cc-chip${f === k ? ' on' : ''}" onclick="ccTfilter('${k}')">${esc(l)}</button>`).join('');
  const rows = rows0.filter(x => f === 'all' || x.t.owner === f).sort((a, b) => (order[a.st] ?? 9) - (order[b.st] ?? 9) || a.t.owner.localeCompare(b.t.owner)).slice(0, 200).map(({ t, st }) => {
    const src = t.card || t.source_card;
    const link = src ? `<a href="#" onclick="ccGoCard('${esc(src)}');return false;">card</a>` : '';
    const extra = [t.next ? esc(t.next) : '', t.link ? 'file: ' + esc(t.link) : '', t.session ? 'chat: ' + esc(String(t.session).slice(0, 14)) : ''].filter(Boolean).join(' · ');
    return `<tr class="${esc(st)}"><td><span class="cc-st ${esc(st)}">${esc(label[st] || st)}</span></td><td><b>${esc(t.owner)}</b></td><td>${esc(t.client)}</td><td>${esc(t.title)}${extra ? `<div class="cc-sub">${extra}</div>` : ''}</td><td>${esc(t.due || '')}</td><td>${link}</td></tr>`;
  }).join('');
  const srcNote = CC.work && CC.work.length ? `Source: task model (work_items), ${CC.work.length} rows.` : `Source: snapshot (task model not readable${CC.workErr ? ': ' + esc(CC.workErr) : ''}).`;
  return `<div class="cc-chips">${chips}</div><div class="cc-panel" style="overflow-x:auto"><table class="cc-tk"><tr><th>Status</th><th>Owner</th><th>Client</th><th>Task</th><th>Due</th><th>Source</th></tr>${rows}</table></div>
<div class="cc-legend" style="margin-top:10px">${srcNote} Only a person sets 'done', with proof. An agent 'done' shows as 'needs check'. A click-card task shows 'done' as soon as you answer its card 'Done'.</div>`;
}

// "Today" tab (Martin 13.10. evening): one board per client + not delegated + waiting for + done today.
function ccToday() {
  const s = CC.snap, t = s.today;
  if (!t) return '<div class="cc-panel"><div class="muted">This snapshot has no "Today" data yet. The next run writes it.</div></div>';
  const openDec = s.cards.filter(c => ccEff(c).status === 'open').length;
  const tiles = t.tiles.map(x => `<div class="cc-tile"><b>${esc(x.label === 'decisions open' ? openDec : x.value)}</b><span>${esc(x.label)}</span></div>`).join('');
  const tr = { off: 'OFF', on: 'ON', unknown: '–' };
  const rows = t.board.map(r => {
    const pct = Math.round(r.phase_n / r.phase_max * 100);
    const det = `<div class="cc-tdet"><div><h5>Done today (${r.n_done})</h5><ul>${r.done.map(x => `<li class="moved"><span class="ic">✓</span><span>${esc(x)}</span></li>`).join('') || '<li>nothing</li>'}</ul></div>
<div><h5>Open (${r.n_open})</h5><ul>${r.open.map(x => `<li><span class="ic">•</span><span>${esc(x)}</span></li>`).join('') || '<li>nothing</li>'}</ul></div>
<div><h5>Waiting for (${r.n_waiting})</h5><ul>${r.waiting.map(x => `<li><span class="ic">🕒</span><span>${esc(x)}</span></li>`).join('') || '<li>nothing</li>'}</ul></div></div>`;
    return `<details class="cc-trow ${esc(r.track)}"><summary><span class="cc-tr ${esc(r.track)}" title="${esc(r.track_why)}">${tr[r.track]}</span>
<span class="cc-tn">${esc(r.name)}<small>${esc(r.track_why)}</small></span>
<span class="cc-tph"><span class="cc-pbar"><i style="width:${pct}%"></i></span>${esc(r.phase)} · ${esc(r.phase_label)}${r.week != null ? ' · wk ' + esc(r.week) : ''}</span>
<span class="cc-tc" title="done today">✓ ${esc(r.n_done)}</span><span class="cc-tc" title="open tasks">• ${esc(r.n_open)}</span><span class="cc-tc" title="waiting for others">🕒 ${esc(r.n_waiting)}</span>
<span class="cc-tnext">${esc(r.next || 'no next step set')}</span></summary>${det}</details>`;
  }).join('');
  const li = (a, f) => a.map(f).join('') || '<li>nothing</li>';
  const nd = li(t.not_delegated, x => `<li><b>${esc(x.client)}</b> — ${esc(x.title)}<div class="cc-sub">give to: <b>${esc(x.give_to)}</b> · ${esc(x.why)}</div></li>`);
  const you = li(t.only_you, x => `<li><b>${esc(x.client)}</b> — ${esc(x.title)}${x.due ? `<div class="cc-sub">due ${esc(x.due)}</div>` : ''}</li>`);
  const wt = li(t.waiting, x => `<li><b>${esc(x.who)}</b> · ${esc(x.client)} — ${esc(x.title)}${x.note ? `<div class="cc-sub">${esc(x.note)}</div>` : ''}</li>`);
  const dn = li(t.done, x => `<li><b>${esc(x.client)}</b> — ${esc(x.title)} <span class="cc-sub">(${esc(x.owner)})</span></li>`);
  return `<div class="cc-tiles cc-tiles6">${tiles}</div>
<div class="cc-panel" style="margin-bottom:14px"><h4>Clients · roadmap and today</h4><div class="cc-legend">OFF = overdue portal tasks. Click a row for done / open / waiting. ✓ done today · • open tasks · 🕒 waiting for others.</div>${rows}</div>
<div class="cc-grid2"><div class="cc-panel"><h4>Not delegated (${t.not_delegated.length})</h4><ul>${nd}</ul><h4 style="margin-top:14px">Only you (${t.only_you.length})</h4><ul>${you}</ul></div>
<div class="cc-panel"><h4>Waiting for (${t.waiting.length})</h4><ul>${wt}</ul></div></div>
<div class="cc-panel" style="margin-top:14px"><h4>Done today (${t.done.length} tasks)</h4><ul>${dn}</ul></div>
<div class="cc-legend" style="margin-top:10px">Evening log: ${esc(t.log_status)}. Decisions open counts your live answers.</div>`;
}

function ccRender() {
  const s = CC.snap, el = $('grill');
  const tabs = [['today', 'Today'], ['dec', 'Decisions'], ['tk', 'Tasks'], ['cli', 'Clients'], ['ag', 'Agents & waiting']].map(([k, l]) => `<button class="cc-tab${CC.tab === k ? ' on' : ''}" onclick="ccTab('${k}')">${l}</button>`).join('');
  const body = CC.tab === 'today' ? ccToday() : CC.tab === 'dec' ? ccDecisions() : CC.tab === 'tk' ? ccTasks() : CC.tab === 'cli' ? ccClients() : ccAgents();
  el.innerHTML = `<span class="backlink" onclick="showApp('admin-home')">← Übersicht</span>
<div class="cc-head"><h1>Command Center</h1><span class="cc-meta">${esc(s.date)} WITA · ${esc(CC.mode)} snapshot ${esc(CC.snapId)} · read ${esc(s.read_at)} · <a href="#" onclick="loadGrill();return false;">reload</a></span></div>
<div class="cc-tabs">${tabs}</div>${body}`;
}
