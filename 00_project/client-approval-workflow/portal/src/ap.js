/* ---------- Entscheidungen (Kunden-Freigabe) · 2026-10-13 ----------
   Regeln: 00_project/client-approval-workflow/brief.md · Daten: approval_items, approval_decisions, client_approval_settings
   Kunde entscheidet nur über RPC approval_decide / approval_undo. Admin: approval_release, approval_go.
   Martin-Figuren nur in der Kundenansicht (hello, think, point, celebrate), nie in der 741-Ansicht. */
const AP_MG = {
  hello: 'src="martin-guide/martin-hello.webp"',
  think: 'src="martin-guide/martin-think.webp"',
  point: 'src="martin-guide/martin-point.webp"',
  celebrate: 'src="martin-guide/martin-celebrate.webp"'
};
const AP_MG_ALT = { hello: 'winkt zur Begrüßung', think: 'denkt nach', point: 'zeigt auf das Schloss', celebrate: 'freut sich' };
const AP_LOCK = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17 9V7a5 5 0 0 0-10 0v2H5v13h14V9h-2zM9 7a3 3 0 0 1 6 0v2H9V7z"/></svg>';
let apSel = {};        // item_id → gewählte Variante, bis die Entscheidung gespeichert ist
let apFilter = 'Alle';
let apPreview = false; // Admin: Kundenansicht ansehen (nur lesen)
let apArmed = null;    // Admin: zweiter Klick bestätigt das Go

async function apLoad(b, clientId) {
  const [it, dec, set] = await Promise.all([
    db.from('approval_items').select('*').eq('client_id', clientId).order('created_at').order('code').order('id'),  // feste Reihenfolge, springt nach Klicks nicht
    db.from('approval_decisions').select('*').eq('client_id', clientId).order('created_at', { ascending: false }).limit(300),
    db.from('client_approval_settings').select('*').eq('client_id', clientId).maybeSingle()
  ]);
  b.apReady = !it.error;   // false = Tabellen fehlen noch (Migration nicht angewendet)
  b.apItems = it.data || []; b.apLog = dec.data || []; b.apSettings = set.data || null;
}
async function apReload() { if (!bundle) return; await apLoad(bundle, bundleClientId); rerender(); }
const apOn = (b) => !!(b && b.apReady && (b.apItems || []).some(i => i.status !== 'draft' && i.status !== 'withdrawn'));
const apMd = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
const apD = (d) => d ? new Date(d).toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit' }) : '';
const apDT = (d) => d ? apD(d) + ' ' + new Date(d).toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' }) : '';
const apVar = (i, k) => (i.variants || []).find(v => v.key === k);
const apVal = (i, k) => { const v = apVar(i, k); return v ? String(v.value).replace('{kw}', i.keyword || '') : ''; };
const apVisible = (b) => (b.apItems || []).filter(i => i.status !== 'draft' && i.status !== 'withdrawn');
const apOpenCount = (b) => apVisible(b).filter(i => i.status === 'open').length;
const apCanDecide = (b) => !bundleIsAdmin && !!(b.apSettings && me && b.apSettings.approver_user_id === me.user_id);
function apFirst(b) {
  const n = (b.apSettings && b.apSettings.approver_name) || b.client.contact_person || '';
  return /^(Dr\.|Prof\.)/.test(n) ? n : n.split(' ')[0];
}
function apGuide(pose, text, small) {
  return `<aside class="mg${small ? ' mg--small' : ''}"><img class="mg__img" ${AP_MG[pose]} alt="Martin von 741 ${AP_MG_ALT[pose]}" width="${small ? 72 : 112}"><div class="mg__bubble"><span class="mg__name">Martin</span><p>${esc(text)}</p></div></aside>`;
}

/* ----- Kundenansicht ----- */
function apVarHTML(b, i, v, selKey, ro) {
  const sel = selKey === v.key ? ' sel' : '';
  const rec = v.key === i.recommended_key ? '<span class="ap-rec">741 empfiehlt</span>' : '';
  let val;
  if (i.kind === 'price') val = `<div class="ap-big">${esc(v.value)}</div>`;
  else if (i.kind === 'text') val = `<div class="ap-val">${esc(v.value).replace('{kw}', `<span class="ap-lock">${AP_LOCK}${esc(i.keyword || '')}</span>`)}</div>`;
  else if (i.kind === 'design') {
    const head = v.design === 'head', c = i.context || {};
    val = `<div class="ap-ctx"><div class="bar"><span class="lg">${esc(b.client.name)}</span><span class="sp"></span>${head ? '<span class="ap-call">☎ Anrufen</span>' : '<span style="color:#999">Menü</span>'}</div>
      <div class="hero"><b>${esc(c.hero || '')}</b>${esc(c.cta || '')} …${head ? '' : '<span class="ap-call ap-sticky">☎ Jetzt anrufen</span>'}</div></div>
      <div class="ap-val" style="margin-top:8px">${esc(v.value)}</div>`;
  } else val = `<div class="ap-val">${esc(v.value)}</div>`;
  const click = ro ? '' : ` onclick="apPick('${i.id}','${esc(v.key)}')"`;
  return `<div class="ap-var${sel}${ro ? ' ro' : ''}"${click} role="button" aria-pressed="${sel ? 'true' : 'false'}"><div class="ap-lab">Variante ${esc(v.key)} ${rec}</div>${val}${v.label ? `<div class="ap-note">${esc(v.label)}</div>` : ''}</div>`;
}
function apLastDecision(b, i) {
  return (b.apLog || []).find(l => l.item_id === i.id && ['approve', 'approve_with_change', 'request_change'].includes(l.action) && l.item_version === i.version);
}
function apItemHTML(b, i, used, preview) {
  const can = apCanDecide(b) && !preview;
  const open = i.status === 'open';
  const consent = !!(b.apSettings && b.apSettings.auto_approve_consent);
  const dl = !open ? '' : i.must_active_yes ? '<span class="ap-dl must">Braucht dein aktives Ja</span>'
    : consent ? `<span class="ap-dl">Frist ${apD(i.due_at)} · danach gilt „741 empfiehlt“</span>`
    : `<span class="ap-dl">Bitte bis ${apD(i.due_at)} entscheiden</span>`;
  const selKey = open ? (apSel[i.id] || i.recommended_key) : i.chosen_key;
  const ro = !open || !can;
  const vars = (i.variants || []).map(v => apVarHTML(b, i, v, selKey, ro)).join('');
  let body;
  if (i.kind === 'text') body = `<div class="ap-ba"><div class="ap-before"><div class="ap-lab">Jetzt live</div><div class="ap-val">${esc(i.before_value || '')}</div></div><div class="ap-vars">${vars}</div></div>`;
  else if (i.kind === 'node') body = `<div class="ap-node"><span class="k">${esc((i.context || {}).node_kind || 'Seite')}</span><code>${esc((i.context || {}).node || '')}</code></div><div class="ap-vars" style="margin-top:12px">${vars}</div>`;
  else body = `<div class="ap-vars cols">${vars}</div>`;
  let mg = '';
  if (open && i.guide_text) {
    if (i.must_active_yes && !used.think) { used.think = true; mg = apGuide('think', i.guide_text, true); }
    else if (i.seo_lock && !used.point) { used.point = true; mg = apGuide('point', i.guide_text, true); }
  }
  const lockNote = i.lock_note ? `<div class="ap-note"><span class="ap-lock">${AP_LOCK}nur 741</span> ${esc(i.lock_note)}</div>` : '';
  let acts;
  if (i.status === 'go') {
    acts = `<div class="ap-res go">✓ Freigegeben, 741 setzt es um (${apD(i.go_at)}): <b>${esc(apVal(i, i.chosen_key))}</b></div>`;
  } else if (i.status === 'ready' || i.status === 'change') {
    const l = apLastDecision(b, i);
    const by = i.decided_kind === 'auto_7d' ? 'nach Ablauf der Frist übernommen' : (l ? esc(l.actor_name) + ', ' + apDT(l.created_at) : '');
    const what = i.status === 'change' ? `✎ Änderung gewünscht: <b>${esc(i.chosen_note || '')}</b>`
      : `✓ Entschieden: <b>${esc(apVal(i, i.chosen_key))}</b>${i.chosen_note ? ' · Notiz: ' + esc(i.chosen_note) : ''}`;
    acts = `<div class="ap-res${i.status === 'change' ? ' chg' : ''}">${what} <i style="color:#6b6862;font-style:normal">(${by})</i>${can ? `<button class="ap-undo" onclick="apUndo('${i.id}')">ändern</button>` : ''}</div>`;
  } else {
    const dis = can ? '' : ' disabled';
    // Zwei Knöpfe (Martin 13.10.): "Passt so" = gewählte Variante freigeben, "Ich möchte etwas ändern" = Wunsch mit Text
    acts = `<div class="ap-acts"><button class="ap-btn ap-b1"${dis} onclick="apAct('${i.id}','approve',this)">Passt so</button><button class="ap-btn ap-b2"${dis} onclick="apAct('${i.id}','request_change',this)">Ich möchte etwas ändern</button></div><textarea class="ap-ta" id="ap-ta-${i.id}" placeholder="Was soll anders sein? Ein Satz reicht."></textarea>`;
  }
  return `<article class="ap-item${open ? '' : ' done'}" id="ap-${i.id}"><div class="ap-top"><span class="ap-type">${esc(i.type_label)}</span>${dl}</div>
    <h3>${esc(i.title)}</h3><div class="ap-why">Warum: ${apMd(i.why)}<span class="ap-src">Quelle: ${esc(i.why_source)} · Stand ${apD(i.why_date)}</span></div>
    ${mg}${body}${i.note ? `<div class="ap-note">${esc(i.note)}</div>` : ''}${lockNote}${acts}</article>`;
}
function apRenderClient(b, preview) {
  const items = apVisible(b), open = apOpenCount(b), who = apFirst(b);
  const consent = !!(b.apSettings && b.apSettings.auto_approve_consent);
  const used = { think: false, point: false };
  const lead = consent
    ? 'Hier siehst du, was wir für deine Website und dein Google-Profil vorbereitet haben. Du wählst aus 2 oder 3 Varianten, und die Variante, die wir dir raten, trägt das Zeichen „741 empfiehlt“. Entscheidest du bis zur Frist nicht, gilt die Empfehlung. Preise und Gesundheitsthemen brauchen immer dein Ja.'
    : 'Hier siehst du, was wir für deine Website und dein Google-Profil vorbereitet haben. Du wählst aus 2 oder 3 Varianten, und die Variante, die wir dir raten, trägt das Zeichen „741 empfiehlt“. Nichts geht live, bevor du entschieden hast.';
  const hello = open ? apGuide('hello', `Hallo ${who}, hier entscheidest du mit. Bei jedem Punkt habe ich meine Empfehlung markiert, ein Klick auf „Passt so“ reicht.`) : '';
  const done = !open && items.length ? apGuide('celebrate', `Danke, ${who}! Alles ist entschieden. Ich melde mich, sobald es live ist.`) : '';
  const notApprover = !preview && !apCanDecide(b)
    ? `<div class="ap-info">Entscheiden kann nur ${esc((b.apSettings && b.apSettings.approver_name) || 'die benannte Person')}. Du kannst alles ansehen und uns im Chat schreiben.</div>` : '';
  const types = ['Alle', 'Offen', ...new Set(items.map(i => i.type_label))];
  if (!types.includes(apFilter)) apFilter = 'Alle';
  const list = items.filter(i => apFilter === 'Alle' || (apFilter === 'Offen' ? i.status === 'open' : i.type_label === apFilter));
  return `<div style="max-width:980px;"><div class="ap-h1">Deine Entscheidungen</div><p class="ap-lead">${lead}</p>${hello}
    <span class="ap-count">${open ? open + ' warten auf dich' : 'Alles entschieden, danke!'}</span>${done}${notApprover}
    <div class="ap-filters">${types.map(t => `<button class="ap-chip${t === apFilter ? ' on' : ''}" onclick="apSetFilter('${esc(t)}')">${esc(t)}</button>`).join('')}</div>
    ${list.map(i => apItemHTML(b, i, used, preview)).join('') || '<div class="muted">Hier ist gerade nichts offen.</div>'}</div>`;
}
function apSetFilter(t) { apFilter = t; rerender(); }
function apPick(id, key) {
  const i = (bundle.apItems || []).find(x => x.id === id);
  if (!i || i.status !== 'open' || !apCanDecide(bundle)) return;
  apSel[id] = key; rerender();
}
async function apAct(id, action, btn) {
  if (!apCanDecide(bundle)) return;
  const ta = $('ap-ta-' + id);
  let note = null;
  if (action !== 'approve') {
    if (!ta.classList.contains('on') || ta.dataset.a !== action) {
      ta.classList.add('on'); ta.dataset.a = action; ta.focus();
      btn.textContent = 'Wunsch senden';
      return;
    }
    note = ta.value.trim();
    if (!note) { ta.focus(); toast('Bitte kurz schreiben, was anders sein soll.'); return; }
  }
  const i = bundle.apItems.find(x => x.id === id);
  btn.disabled = true;
  const { error } = await db.rpc('approval_decide', { p_item: id, p_action: action, p_variant: apSel[id] || i.recommended_key, p_note: note });
  if (error) { btn.disabled = false; toast('Fehler: ' + error.message); return; }
  delete apSel[id];
  toast(action === 'request_change' ? 'Danke, dein Wunsch ist bei uns.' : 'Danke, gespeichert.');
  apReload();
}
async function apUndo(id) {
  const { error } = await db.rpc('approval_undo', { p_item: id });
  if (error) { toast('Fehler: ' + error.message); return; }
  apReload();
}

/* ----- 741-Ansicht (Admin) — ohne Martin-Figuren ----- */
function apStatus(b, i) {
  if (i.status === 'draft') return ['Entwurf · nur 741', 'p-draft'];
  if (i.status === 'withdrawn') return ['zurückgezogen', 'p-draft'];
  if (i.status === 'go') return ['Go gegeben', 'p-go'];
  if (i.status === 'change') return ['Änderung gewünscht', 'p-chg'];
  if (i.status === 'ready') return [i.decided_kind === 'auto_7d' ? 'bereit für live (Tag 7)' : 'bereit für live', i.decided_kind === 'auto_7d' ? 'p-auto' : 'p-ok'];
  return [i.must_active_yes ? 'offen · aktives Ja' : 'offen · Frist ' + apD(i.due_at), 'p-open'];
}
const AP_KIND = { client: 'Kunde', auto_7d: 'automatisch nach 7 Tagen', admin_go: '741-Go', admin: '741' };
function apLogText(l) {
  const v = esc(l.variant_value || ''), n = esc(l.note || '');
  switch (l.action) {
    case 'approve': return 'gewählt: ' + v;
    case 'approve_with_change': return 'gewählt: ' + v + ' · Notiz: ' + n;
    case 'request_change': return 'Änderung gewünscht: „' + n + '“';
    case 'undo': return 'Entscheidung zurückgenommen';
    case 'released': return 'an Kunde gegeben';
    case 'new_version': return 'neue Version, Entscheidung zurückgesetzt';
    case 'go': return 'Go für live: ' + v;
    case 'withdrawn': return 'zurückgezogen';
    case 'consent_on': return 'Zustimmung 7-Tage-Regel erfasst' + (n ? ' (' + n + ')' : '');
    case 'consent_off': return 'Zustimmung 7-Tage-Regel entfernt';
    default: return esc(l.action);
  }
}
function apAdminButton(b) {
  if (!b.apReady) return '';
  const all = b.apItems || [];
  const open = all.filter(i => i.status === 'open').length, ready = all.filter(i => i.status === 'ready').length;
  return `<button class="btn btn-small ${ready ? 'btn-yellow' : 'btn-ghost'}" onclick="adminSub='approvals';apPreview=false;rerender()">Entscheidungen · ${open} offen · ${ready} bereit</button>`;
}
function apRenderAdmin(b) {
  const isA = me && me.role === 'admin';
  const s = b.apSettings || {};
  const back = `<span class="backlink" onclick="adminSub=null;apPreview=false;rerender()">← Zur Kundenseite</span>`;
  const head = `<div class="ap-h1">Freigaben · ${esc(b.client.name)}</div>
    <p class="ap-lead">Was ${esc(s.approver_name || 'der Kunde')} entscheidet, landet in „bereit für live“. Live geht es erst mit deinem Go.</p>
    <div class="ap-filters"><button class="ap-chip${apPreview ? '' : ' on'}" onclick="apPreview=false;rerender()">741-Ansicht</button><button class="ap-chip${apPreview ? ' on' : ''}" onclick="apPreview=true;rerender()">Kundenansicht ansehen</button></div>`;
  if (!b.apReady) return back + head + '<div class="ap-info">Die Tabellen fehlen noch. Die Migration <code>01-migration.sql</code> wartet auf dein Go.</div>';
  if (apPreview) return back + head + `<div class="ap-preview"><div class="muted" style="margin-bottom:10px">Vorschau: So sieht ${esc(s.approver_name || 'der Kunde')} den Tab „Entscheidungen“. Die Knöpfe sind hier gesperrt.</div>${apRenderClient(b, true)}</div>`;
  const all = b.apItems || [];
  const rows = all.map(i => {
    const [st, cls] = apStatus(b, i);
    const chosen = i.status === 'change' ? esc(i.chosen_note || '') : (i.chosen_key ? esc(apVal(i, i.chosen_key)) + (i.chosen_note ? '<br><span class="muted">Notiz: ' + esc(i.chosen_note) + '</span>' : '') : '—');
    let act = '';
    if (isA && i.status === 'ready') act = `<button class="ap-go" onclick="apGo('${i.id}')">${apArmed === i.id ? 'Wirklich Go?' : 'Go für live'}</button>`;
    if (isA && i.status === 'draft') act = `<button class="ap-go" style="background:#fff;border:1.5px solid #252525" onclick="apRelease('${i.id}')">An Kunde geben</button>`;
    const flags = [i.must_active_yes ? 'aktives Ja' : '', i.seo_lock ? 'SEO-Schloss' : '', i.hwg_checked ? 'HWG geprüft' : ''].filter(Boolean).join(' · ');
    return `<tr><td><b>${esc(i.code || '')} ${esc(i.type_label)}</b> <span class="muted">v${i.version}</span><br>${esc(i.title)}${flags ? '<br><span class="muted">' + flags + '</span>' : ''}</td>
      <td><span class="ap-pill ${cls}">${st}</span></td><td>${chosen}</td><td>${act}</td></tr>`;
  }).join('') || '<tr><td colspan="4" class="muted">Noch keine Elemente. Elemente legt 741 aus Audit, Content-Pool, CRO-Lauf, Seitenbaum oder Google-Profil-Plan an.</td></tr>';
  const ready = all.filter(i => i.status === 'ready').length;
  const settings = `<div class="card"><h2>Einstellungen</h2>
    <div class="ap-sw"><span style="min-width:120px;color:var(--grey)">Entscheider</span><b>${s.approver_name ? esc(s.approver_name) : '<span style="color:#c0392b">nicht festgelegt, Kunde kann nicht entscheiden</span>'}</b></div>
    <div class="ap-sw"><span style="min-width:120px;color:var(--grey)">Gesundheit</span><span>${s.health_client ? 'Ja: HWG-Prüfung ist Pflicht, bevor ein Element rausgeht' : 'Nein'}</span></div>
    <div class="ap-sw"><span style="min-width:120px;color:var(--grey)">Sammel-Mail</span><span>${s.digest_enabled ? 'an (max. 1 pro Tag, BCC an dich)' : 'aus · Entwurf, wartet auf dein Go'}</span></div>
    <div class="ap-info"><div class="ap-sw"><input type="checkbox" id="ap-consent" ${s.auto_approve_consent ? 'checked' : ''} ${isA ? '' : 'disabled'} onchange="apConsent(this.checked)"><label for="ap-consent"><b>Zustimmung zur 7-Tage-Regel</b> liegt schriftlich vor${s.auto_approve_consent && s.consent_source ? ' (' + esc(s.consent_source) + ', ' + apD(s.consent_at) + ')' : ''}</label></div>
      <input id="ap-consent-src" placeholder="Wo steht die Zustimmung? z. B. Vertrag § 4" style="margin:4px 0 8px;${s.auto_approve_consent || !isA ? 'display:none' : ''}">
      Ohne diese Zustimmung gilt Schweigen nie als Freigabe. Preise, Gesundheits- und Behandlungsaussagen brauchen immer ein aktives Ja. Die Regel läuft erst, wenn der Mail- und Fristen-Entwurf aktiviert ist.</div></div>`;
  const log = `<div class="card"><h2>Entscheidungs-Protokoll</h2><div class="ap-log">${(b.apLog || []).map(l => {
    const it = all.find(i => i.id === l.item_id);
    return `<div>${apDT(l.created_at)} · <b>${esc(l.actor_name)}</b> · ${apLogText(l)}<br><i>${it ? esc((it.code ? it.code + ' ' : '') + it.title) : 'Einstellung'}${l.item_version ? ' · Version ' + l.item_version : ''} · Art: ${AP_KIND[l.kind] || esc(l.kind)}</i></div>`;
  }).join('') || '<div><i>Noch keine Einträge.</i></div>'}</div></div>`;
  return back + head + `<div class="ap-grid2"><div class="grid" style="align-content:start;"><div class="card"><h2>Alle Elemente <span class="muted" style="font-weight:500">${ready} bereit für live</span></h2>
      <div style="overflow-x:auto"><table class="ap-tbl"><thead><tr><th>Element</th><th>Status</th><th>Gewählt</th><th></th></tr></thead><tbody>${rows}</tbody></table></div></div>${settings}</div>
    <div class="grid" style="align-content:start;">${log}</div></div>`;
}
async function apGo(id) {
  if (apArmed !== id) { apArmed = id; rerender(); setTimeout(() => { if (apArmed === id) { apArmed = null; rerender(); } }, 6000); return; }
  apArmed = null;
  const { error } = await db.rpc('approval_go', { p_item: id });
  if (error) { toast('Fehler: ' + error.message); return; }
  toast('Go gespeichert. Das Element ist jetzt gesperrt.');
  apReload();
}
async function apRelease(id) {
  const { error } = await db.rpc('approval_release', { p_item: id });
  if (error) { toast('Fehler: ' + error.message); return; }
  toast('Element ist jetzt beim Kunden. Frist: 7 Tage.');
  apReload();
}
async function apConsent(on) {
  const src = ($('ap-consent-src') || {}).value || '';
  if (on && !src.trim()) { $('ap-consent').checked = false; $('ap-consent-src').style.display = 'block'; $('ap-consent-src').focus(); toast('Bitte zuerst eintragen, wo die Zustimmung steht.'); return; }
  const { error } = await db.from('client_approval_settings').upsert({ client_id: bundleClientId, auto_approve_consent: on, consent_source: on ? src.trim() : null });
  if (error) { toast('Fehler: ' + error.message); return; }
  apReload();
}
