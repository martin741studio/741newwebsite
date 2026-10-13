const CC = { snap: null, snapId: null, created: null, mode: null, answers: {}, picks: {}, parking: null, tab: 'dec', filter: 'all' };
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

function ccEff(c) {
  const a = CC.answers[c.id];
  if (a) return { status: a.option === 'park' ? 'parked' : 'decided', answer: a.option, text: a.option === 'park' ? a.note : ((c.options[a.option] || a.option) + (a.note ? ' (' + a.note + ')' : '')) };
  if (c.status === 'decided' || c.status === 'parked') return { status: c.status, answer: c.answer, text: c.answer_text };
  return { status: 'open', answer: null, text: null };
}
function ccWalkDone(w) { return !!CC.answers[w.id]; }

function ccTab(t) { CC.tab = t; ccRender(); }
function ccFilter(f) { CC.filter = f; ccRender(); }
function ccPick(id, k) { CC.picks[id] = k; CC.parking = null; ccRender(); }
function ccParkOpen(id) { CC.parking = id; CC.picks[id] = null; ccRender(); }
async function ccSave(id, option, note) {
  const { error } = await db.from('grill_answers').insert({ card_id: id, run_date: CC.snap.date, option, note: note || null });
  if (error) { alert(error.message); return; }
  CC.answers[id] = { card_id: id, option, note: note || null, answered_at: new Date().toISOString() };
  delete CC.picks[id]; CC.parking = null; ccRender();
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
    acts = `<div class="cc-acts"><button class="btn btn-yellow" ${CC.picks[c.id] ? '' : 'disabled style="opacity:.5"'} onclick="ccSavePick('${esc(c.id)}')">Save answer</button><button class="cc-link" onclick="ccParkOpen('${esc(c.id)}')">Park with reason</button></div>`;
    if (CC.parking === c.id) acts += `<textarea class="cc-ta" id="cc-ta-${esc(c.id)}" placeholder="Why do you park this? The card returns only when the reason changes."></textarea><div class="cc-acts"><button class="btn btn-yellow" onclick="ccSavePark('${esc(c.id)}')">Park</button></div>`;
  }
  const res = done ? `<div class="cc-res${ef.status === 'parked' ? ' park' : ''}">${ef.status === 'parked' ? 'Parked' : 'Decided'}: ${esc(ef.text || ef.answer || '')}</div>` : '';
  const ev = (c.evidence || []).map(x => `<li>${esc(x)}</li>`).join('');
  return `<article class="cc-item p${c.priority}${done ? ' done' : ''}"><div class="cc-itop"><span class="cc-type">${esc(c.type)}</span><b>${esc(c.client)}</b><span class="dl">card ${c.n} · by ${esc(c.deadline)}</span></div>
<h3>${esc(c.headline)}</h3><div class="cc-why"><b>Why:</b> ${esc(c.why)}</div><div class="cc-vars">${vars}</div>${acts}${res}
<details class="cc-ev"><summary>Evidence (${(c.evidence || []).length})</summary><ul>${ev}</ul></details></article>`;
}

function ccDecisions() {
  const s = CC.snap;
  const eff = s.cards.map(c => ({ c, e: ccEff(c) }));
  const nOpen = eff.filter(x => x.e.status === 'open').length;
  const f = CC.filter;
  const show = eff.filter(x => f === 'all' || (f === 'open' && x.e.status === 'open') || (f === 'decided' && x.e.status !== 'open') || (f === 'p1' && x.c.priority === 1) || (f === 'p2' && x.c.priority === 2) || (f === '741' && x.c.client.startsWith('741')) || (f === 'client' && !x.c.client.startsWith('741')));
  const tiles = [[`${s.cards.length - nOpen}/${s.cards.length}`, 'decisions taken'], [String(s.walk.filter(w => !ccWalkDone(w)).length), 'walk-queue clicks open'], [String(s.clients.length), 'active clients'], [String(s.sources.filter(x => x.status !== 'ok').length), 'unreadable sources']];
  const chips = [['all', 'All'], ['open', 'Open'], ['decided', 'Decided'], ['p1', 'Fire'], ['p2', 'Money / contract'], ['client', 'Client'], ['741', '741']].map(([k, l]) => `<button class="cc-chip${f === k ? ' on' : ''}" onclick="ccFilter('${k}')">${l}</button>`).join('');
  const walk = s.walk.map(w => `<li class="${ccWalkDone(w) ? 'done' : ''}"><input type="checkbox" ${ccWalkDone(w) ? 'checked disabled' : ''} onchange="ccWalk('${esc(w.id)}')"><span>${esc(w.text)}</span></li>`).join('') || '<li>nothing open</li>';
  const later = s.later.map(x => `<li><b>${esc(x.client)}</b> — ${esc((x.headline || '').slice(0, 120))}</li>`).join('') || '<li>nothing</li>';
  return `<div class="cc-tiles">${tiles.map(t => `<div class="cc-tile"><b>${esc(t[0])}</b><span>${esc(t[1])}</span></div>`).join('')}</div>
<div class="cc-chips">${chips}</div>${show.map(x => ccCard(x.c)).join('') || '<div class="muted">No card in this filter.</div>'}
<div class="cc-grid2"><div class="cc-panel"><h4>Your walk queue (1–5 min clicks)</h4><ul class="cc-walk">${walk}</ul></div><div class="cc-panel"><h4>Later list (next grill or Monday)</h4><ul>${later}</ul></div></div>`;
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

function ccRender() {
  const s = CC.snap, el = $('grill');
  const tabs = [['dec', 'Decisions'], ['cli', 'Clients'], ['ag', 'Agents & waiting']].map(([k, l]) => `<button class="cc-tab${CC.tab === k ? ' on' : ''}" onclick="ccTab('${k}')">${l}</button>`).join('');
  const body = CC.tab === 'dec' ? ccDecisions() : CC.tab === 'cli' ? ccClients() : ccAgents();
  el.innerHTML = `<span class="backlink" onclick="showApp('admin-home')">← Übersicht</span>
<div class="cc-head"><h1>Command Center</h1><span class="cc-meta">${esc(s.date)} WITA · ${esc(CC.mode)} snapshot ${esc(CC.snapId)} · read ${esc(s.read_at)} · <a href="#" onclick="loadGrill();return false;">reload</a></span></div>
<div class="cc-tabs">${tabs}</div>${body}`;
}
