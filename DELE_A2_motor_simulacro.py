# -*- coding: utf-8 -*-
# MOTOR DEL SIMULACRO DELE A2 (2spanishteachers.com)
# Uso: python3 DELE_A2_motor_simulacro.py DELEA2_F1_U01_datos  -> genera DELEA2_F1_U01_simulacro.html
#   y DELEA2_F1_U01_oral_profesora.html (libreta de la profesora: a la carpeta protegida biblioteca/profesora/).
# Necesita DELE_oral_profesora.py en la misma carpeta.
# Tareas soportadas: CL-T1 (mail), CL-T2 (ads), CL-T3 (people), CL-T4 (long),
# CA-T1 (pics), CA-T2 (radio), CA-T3 (friends), CA-T4 (msgs), escritura y oral completas.
# Datos: lectura/auditiva con "tasks": [{"n":3,"type":"people",...}, ...].
# Las unidades antiguas con "t1"/"t2" siguen funcionando (U01).
# Cambio U06 (oct. 2026): el texto de Inicio dice "mitad de tiempo" o "tiempo real" según los minutos de la unidad.
import json, re, sys
sys.path.insert(0,'.')
import importlib
DATA = importlib.import_module(sys.argv[1] if len(sys.argv)>1 else "DELEA2_F1_U01_datos").DATA

# CODIGO DE LA ORAL: distinto en cada examen y sin relacion entre ellos (mismo sistema que B2).
# Se calcula con esta palabra secreta + el nombre del examen. NO compartas este archivo.
# El codigo de cada examen se consulta en el panel de la profesora (carpeta protegida de la web).
SECRETO = "cc48d40b16aba76d2ebe1f29"
import hashlib
LETRAS = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"
EXAMEN = "A2-U" + DATA["unit"]
PANEL = "https://2spanishteachers.com/biblioteca/profesora/panel.html"
def codigo_oral(examen):
    d = hashlib.sha256((SECRETO + "|" + examen).encode()).digest()
    return "".join(LETRAS[b % len(LETRAS)] for b in d[:5])
def djb2(s):
    h = 5381
    for ch in s:
        h = ((h * 33) ^ ord(ch)) & 0xFFFFFFFF
    return format(h, '08x')
ORAL_CODE = codigo_oral(EXAMEN)
DATA.pop("oralCode", None)
DATA["examen"] = EXAMEN
DATA["panel"] = PANEL
DATA["oralHash"] = djb2(EXAMEN + "|" + ORAL_CODE)
# datos solo para la libreta de la profesora (no van en el archivo del estudiante)
import copy
PROF = DATA.pop("profesora", {}) or {}
PROF_ORAL, PROF_CATS = copy.deepcopy(DATA["oral"]), copy.deepcopy(DATA["cats"])

CSS = r"""
:root{--paper:#FBF9F6;--ink:#14161C;--coral:#E8603C;--coral-soft:#FCE9E1;--cta:#FF6B45;
--line:#E6DFD6;--muted:#5E5A55;--ok:#2F7D4F;--ok-soft:#E3F1E8;--amb:#B7791F;--amb-soft:#FBF0DA;
--bad:#B3261E;--bad-soft:#F8E1DE;--card:#FFFFFF}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink)}
body{font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:17px;line-height:1.6}
h1,h2,h3{font-family:Georgia,"Times New Roman",serif;font-weight:700;line-height:1.25;margin:0 0 .5em}
h1{font-size:1.9rem}h2{font-size:1.45rem}h3{font-size:1.15rem}
.wrap{max-width:820px;margin:0 auto;padding:0 20px 80px}
header.top{border-bottom:3px solid var(--coral);background:var(--card);position:sticky;top:0;z-index:10}
.top-in{max-width:820px;margin:0 auto;padding:14px 20px 0}
.brand{display:flex;justify-content:space-between;align-items:center;gap:12px}.brand>div:first-child{min-width:0}
.brand small{display:block;color:var(--muted);font-size:.85rem}
.timer{font-variant-numeric:tabular-nums;border:2px solid var(--ink);border-radius:999px;padding:4px 14px;font-weight:700;font-size:1rem;white-space:nowrap}
.timer.low{border-color:var(--bad);color:var(--bad)}
.timer[hidden]{display:none}
nav.steps{display:flex;gap:0;overflow-x:auto;margin-top:12px;padding-bottom:0}
nav.steps button{flex:0 0 auto;border:0;background:none;padding:8px 9px 10px;font:inherit;font-size:.92rem;color:var(--muted);cursor:pointer;border-bottom:4px solid transparent;display:flex;align-items:center;gap:6px}
nav.steps button .n{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;border:1.5px solid currentColor;font-size:.75rem;font-weight:700}
nav.steps button.on{color:var(--ink);border-bottom-color:var(--coral);font-weight:600}
nav.steps button.done .n{background:var(--ok);border-color:var(--ok);color:#fff}
nav.steps button.locked{opacity:.55}
nav.steps button:focus-visible,button:focus-visible,textarea:focus-visible,input:focus-visible{outline:3px solid var(--cta);outline-offset:2px}
section.view{display:none;padding-top:28px}
section.view.on{display:block}
.lead{font-size:1.05rem;color:var(--muted);max-width:62ch}
.instr{border-left:5px solid var(--ink);background:var(--card);padding:14px 18px;margin:18px 0;border-radius:0 8px 8px 0}
.instr b{display:block;font-family:Georgia,serif;margin-bottom:4px}
.tip{background:var(--coral-soft);border-radius:8px;padding:10px 14px;font-size:.95rem;margin:12px 0}
.paper{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:22px 26px;margin:16px 0;font-family:Georgia,serif;font-size:1.02rem;line-height:1.7}
.paper .mailhead{font-family:system-ui,sans-serif;font-size:.9rem;color:var(--muted);border-bottom:1px solid var(--line);padding-bottom:8px;margin-bottom:12px}
.paper p{margin:0 0 .9em}
.ad{background:var(--card);border:2px solid var(--ink);border-radius:4px;padding:16px 20px;margin:22px 0 12px}
.ad h4{margin:0 0 6px;font-family:Georgia,serif;font-size:1.05rem}
.ad .lbl{font-size:.8rem;color:var(--muted);font-weight:600;margin-bottom:6px}
.q{margin:14px 0 22px}
.q .qt{font-weight:600;margin-bottom:8px}
.q .qt .num{display:inline-block;min-width:2em;color:var(--coral);font-family:Georgia,serif}
.opt{display:flex;align-items:flex-start;gap:12px;padding:8px 10px;border-radius:8px;cursor:pointer;border:1px solid transparent}
.opt:hover{background:#F4EFE9}
.opt input{position:absolute;opacity:0;width:1px;height:1px}
.bub{flex:0 0 30px;width:30px;height:30px;border-radius:50%;border:2px solid var(--ink);display:grid;place-items:center;font-weight:700;font-size:.9rem;background:#fff}
.opt input:checked + .bub,.pic input:checked + .bub{background:var(--ink);color:#fff}
.pic:has(input:checked) .plbl{outline:2px solid var(--ink)}
.opt input:focus-visible + .bub{outline:3px solid var(--cta);outline-offset:2px}
.locked-q .opt{cursor:default}
.locked-q .opt:hover{background:none}
.pics{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.pic{border:2px solid var(--line);border-radius:10px;padding:10px;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;background:#fff;position:relative}
.pic input{position:absolute;opacity:0}
.pic .ph{width:100%;aspect-ratio:16/9;border-radius:6px;background:#F1ECE6;display:grid;place-items:center;font-size:.92rem;color:var(--ink);padding:6px}
.pic img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:6px}
.pic:has(input:checked){border-color:var(--ink);box-shadow:0 0 0 2px var(--ink)}
.pic:has(input:focus-visible){outline:3px solid var(--cta);outline-offset:2px}
.example{border:1px dashed var(--muted);border-radius:10px;padding:12px 16px;margin:14px 0;background:#FFFDFB}
.example .ex-ok{color:var(--ok);font-weight:600;margin-top:6px}
.btn{font:inherit;font-weight:600;border-radius:999px;padding:10px 22px;cursor:pointer;border:2px solid var(--ink);background:#fff;color:var(--ink)}
.btn.cta{background:var(--cta);border-color:var(--cta);color:#fff}
.btn:disabled{opacity:.5;cursor:not-allowed}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:18px 0}
.done-note{background:var(--ok-soft);border-radius:8px;padding:10px 14px;margin:16px 0}
.warn{background:var(--amb-soft);border-radius:8px;padding:10px 14px;margin:16px 0}
audio{width:100%;margin:10px 0}
.audio-miss{font-size:.9rem;color:var(--bad);background:var(--bad-soft);border-radius:8px;padding:10px 14px;margin:8px 0}
.audio-miss .btn{display:block;margin-top:8px}
textarea,input[type=text]{width:100%;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;background:#fff;color:var(--ink)}
textarea{min-height:190px;line-height:1.6;resize:vertical}
.wc{font-size:.9rem;margin-top:4px}
.wc.good{color:var(--ok)}.wc.bad{color:var(--amb)}
.vocab-row{display:grid;grid-template-columns:1fr 2fr auto;gap:8px;margin-bottom:8px}
.vocab-row button{border:0;background:none;cursor:pointer;color:var(--muted);font-size:1.3rem}
.pautas{margin:8px 0 8px 0;padding-left:1.2em}
.checks label{display:flex;gap:10px;align-items:flex-start;margin:6px 0;cursor:pointer}
.checks input{margin-top:6px;accent-color:var(--ink)}
.choice{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0}
.choice label{border:2px solid var(--line);border-radius:999px;padding:6px 16px;cursor:pointer;background:#fff}
.choice label:has(input:checked){border-color:var(--ink);background:var(--ink);color:#fff}
.choice input{position:absolute;opacity:0}
.photo{background:#F1ECE6;border-radius:8px;padding:12px 14px;font-size:.95rem;margin:8px 0}
.ficha{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px 16px;margin:10px 0}
.ficha div{margin:3px 0}
.score{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}
.score div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px}
.score b{display:block;font-family:Georgia,serif;font-size:1.9rem;line-height:1.1}
.score span{font-size:.9rem;color:var(--muted)}
.sem{width:100%;border-collapse:collapse;margin:10px 0 20px;background:#fff}
.sem td{padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.5}
.dot{display:inline-block;width:14px;height:14px;border-radius:50%;margin-right:8px;vertical-align:-2px}
.dot.g{background:var(--ok)}.dot.a{background:var(--amb)}.dot.r{background:var(--bad)}
.fail{border-left:4px solid var(--bad);background:#fff;padding:10px 14px;margin:10px 0;border-radius:0 8px 8px 0}
.fail .yours{font-size:.92rem;color:var(--muted)}
.review{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin:12px 0}
.review .reto{margin-top:8px;font-style:italic}
.lockbox{background:var(--card);border:2px solid var(--ink);border-radius:12px;padding:24px;max-width:460px}
.lockbox svg{width:34px;height:34px}
.err{color:var(--bad);font-size:.95rem;margin-top:6px}
.lamina{background:#fff;border:1px solid var(--line);border-radius:10px;padding:18px 22px;margin:16px 0}
.muted{color:var(--muted)}
footer.legal{font-size:.85rem;color:var(--muted);border-top:1px solid var(--line);padding-top:14px;margin-top:40px}

.ask{position:fixed;inset:0;background:rgba(20,22,28,.45);display:grid;place-items:center;z-index:50;padding:20px}
.ask[hidden]{display:none}
.ask-box{background:#fff;border-radius:12px;padding:22px 24px;max-width:440px;box-shadow:0 12px 40px rgba(20,22,28,.25)}
.gap{margin-top:36px}
.conv{margin-top:18px;font-weight:600;color:var(--muted)}
img.hero{width:100%;aspect-ratio:16/7;object-fit:cover;border-radius:12px;margin-bottom:18px}
img.trip{width:100%;max-width:600px;border-radius:8px;border:1px solid var(--line);margin-bottom:6px;display:block}
.withimg .pics{gap:10px;max-width:600px}
.withimg .pic{border:0;background:none;padding:4px}
.withimg .plbl{display:none}
.noimg .plbl{display:block}
.pic .plbl{background:#F1ECE6;border-radius:6px;padding:14px 6px;width:100%;font-size:.92rem}
img.lam-img{width:100%;border-radius:8px;margin:8px 0;display:block}
.lamina.q .lam-img + .photo-txt, .lamina.q .lam-img + .photo{display:none}
.lamina.q.noimg .photo-txt, .lamina.q.noimg .photo{display:block}
img.lock-img{width:100%;border-radius:8px;margin-bottom:12px;aspect-ratio:3/2;object-fit:cover}
details{background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px 14px;margin:8px 0}
summary{cursor:pointer;font-weight:600}
.tr p{margin:.35em 0;font-family:Georgia,serif}
.copied-box{background:var(--ok-soft);color:var(--ok);border-radius:10px;padding:12px 16px;margin:4px 0 10px;font-weight:500}
.copied-box.bad{background:var(--amb-soft);color:#7A4E0E}
.copied-box[hidden]{display:none}
.sendbox{border:2px solid var(--coral);border-radius:12px;padding:18px 22px;margin:26px 0;background:#fff}
.lbl-name{display:block;max-width:360px}.lbl-name input{margin-top:6px}
.small{font-size:.88rem}
.print-only{display:none}
.inl .opts{display:flex;flex-wrap:wrap;gap:4px 14px}
.inl .opt{padding:6px 8px}
.letters{display:flex;flex-wrap:wrap;gap:6px}
.letters .opt{padding:2px}
.enun{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 18px;margin:14px 0}
.enun div{margin:4px 0}.enun b{display:inline-block;width:1.6em;color:var(--coral);font-family:Georgia,serif}
.people .paper h4{margin:0 0 6px;font-family:system-ui,sans-serif;font-size:.95rem;letter-spacing:.04em}
.paper .sub{font-family:system-ui,sans-serif;font-size:.9rem;color:var(--muted);margin:-4px 0 14px}
textarea.lined{max-width:45ch;display:block;line-height:2em;padding:0 12px;background-color:#fff;background-image:repeating-linear-gradient(to bottom,transparent 0,transparent calc(2em - 1px),#E3DBD1 calc(2em - 1px),#E3DBD1 2em);background-attachment:local;min-height:18em}
@media print{.noprint,#ask,footer.legal{display:none!important}.print-only{display:block}details{border:0;padding:0}summary{display:none}body{background:#fff}}

@media (max-width:600px){body{font-size:16px}.paper{padding:16px}.pics{grid-template-columns:1fr 1fr 1fr;gap:6px}.pic{padding:6px}.pic .ph{font-size:.8rem}.score{grid-template-columns:1fr}.vocab-row{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
@media print{header.top,nav.steps,.row,.btn{display:none!important}section.view{display:block!important}}
.sw{display:inline-flex;align-items:center;gap:6px;border:1.5px solid var(--line);border-radius:999px;padding:3px 4px 3px 12px;background:#fff;font-size:.85rem;vertical-align:middle;margin-left:10px;font-family:system-ui,sans-serif;font-weight:400}
.sw-lbl{color:var(--muted)}
.sw-t{font-variant-numeric:tabular-nums;font-weight:700;min-width:3.2em;text-align:right;color:var(--ink)}
.sw-b{border:0;background:var(--coral-soft);color:var(--ink);border-radius:50%;width:28px;height:28px;cursor:pointer;font-size:.8rem;line-height:28px;padding:0}
.sw-b:hover{background:var(--coral);color:#fff}
.sw.near{border-color:#C98A1B}.sw.near .sw-t{color:#9A6512}
.sw.ok{border-color:#2F7D4F;background:#EAF5EE}.sw.ok .sw-t{color:#2F7D4F}
.sw.over{border-color:#B3261E;background:#FBEAEA}.sw.over .sw-t{color:#B3261E}
.sw.run .sw-t::after{content:" \25CF";font-size:.6em;color:#B3261E;vertical-align:middle}
.hsw{display:flex;flex-wrap:wrap;align-items:center;gap:6px}
"""

HTML_BODY = r"""
<header class="top"><div class="top-in">
 <div class="brand">
  <div><h1 style="font-size:1.35rem;margin:0">__H1__</h1>
  <small>Preparación DELE A2</small></div>
  <div id="timer" class="timer" hidden aria-live="off"></div>
 </div>
 <nav class="steps" id="steps" aria-label="Partes del simulacro"></nav>
</div></header>
<main class="wrap" id="app"></main>
<div id="ask" class="ask" hidden></div>
"""

JS = r"""
(function(){
var D = __DATA__;
var LET = 'ABCDEFGHIJK'.split('');
function tasksOf(part){
 var s = D[part]; if(s.tasks) return s.tasks;
 var ty = part==='lectura' ? ['mail','ads'] : ['pics','radio'];
 return [Object.assign({n:1,type:ty[0]}, s.t1), Object.assign({n:2,type:ty[1]}, s.t2)];
}
function nItems(part){ var c=0; tasksOf(part).forEach(function(t){ c+=t.items.length; }); return c; }
function tNums(part){ return tasksOf(part).map(function(t){return t.n;}).join(' y '); }
var TL = (D.tiempos&&D.tiempos.lectura)||30, TA = (D.tiempos&&D.tiempos.auditiva)||20;
var NT = ['','una','dos','tres','cuatro'];
var STEPS = [
 {id:'inicio', label:'Inicio'},
 {id:'lectura', label:'Lectura', mins:TL},
 {id:'auditiva', label:'Auditiva', mins:TA},
 {id:'escrita', label:'Escritura', mins:45},
 {id:'resultados', label:'Resultados'},
 {id:'vocab', label:'Vocabulario'},
 {id:'oral', label:'Oral'}
];
var S = load();
function blank(){return {cur:'inicio', ans:{}, done:{}, start:{}, vocab:[{w:'',f:''},{w:'',f:''},{w:'',f:''}], dudas:'', t1:'', t2:'', t2op:'', checks:{}, name:'', oral:false};}
function load(){
 try{ var r = localStorage.getItem(D.storageKey); if(r){ var o = JSON.parse(r); var b = blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){}
 return blank();
}
function save(){ try{ localStorage.setItem(D.storageKey, JSON.stringify(S)); }catch(e){} }
function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function $(id){ return document.getElementById(id); }
function h(s){ var x=5381; for(var i=0;i<s.length;i++){ x = (Math.imul(x,33) ^ s.charCodeAt(i)) >>> 0; } return ('00000000'+x.toString(16)).slice(-8); }
function words(t){ var m = String(t||'').trim().match(/\S+/g); return m ? m.length : 0; }
function allComp(){ return !!(S.done.lectura && S.done.auditiva && S.done.escrita); }
function img(file, alt, cls){ return D.imgBase && file ? '<img class="'+(cls||'')+'" src="'+D.imgBase+file+'" alt="'+esc(alt||'')+'" loading="lazy" onerror="this.style.display=\'none\';var q=this.closest(\'.q\');if(q)q.classList.add(\'noimg\')">' : ''; }

/* ---------- confirmacion dentro de la pagina ---------- */
var pending = null;
function ask(msg, yesTxt, fn){
 pending = fn;
 var o = $('ask'); o.innerHTML = '<div class="ask-box" role="dialog" aria-modal="true" aria-labelledby="askmsg"><p id="askmsg">'+msg+'</p><div class="row"><button class="btn cta" id="askyes">'+yesTxt+'</button><button class="btn" id="askno">Volver</button></div></div>';
 o.hidden = false; $('askyes').focus();
}
document.addEventListener('click', function(e){
 if(e.target.id==='askyes'){ $('ask').hidden=true; var f=pending; pending=null; if(f) f(); return; }
 if(e.target.id==='askno' || e.target.id==='ask'){ $('ask').hidden=true; pending=null; return; }
 var b = e.target.closest('[data-go]'); if(b){ go(b.getAttribute('data-go')); return; }
 var a = e.target.closest('[data-act]'); if(a){ var f=ACTS[a.getAttribute('data-act')]; if(f) f(a); }
});

/* ---------- navegacion ---------- */
function isLocked(id){ return ((id==='resultados'||id==='vocab') && !allComp()) || (id==='oral' && !S.oral); }
function lockSvg(s){ return '<svg width="'+s+'" height="'+s+'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'; }
function renderNav(){
 var out='';
 STEPS.forEach(function(st,i){
  var locked = isLocked(st.id);
  var cls = (S.cur===st.id?'on ':'') + (S.done[st.id]?'done ':'') + (locked?'locked':'');
  var mark = S.done[st.id] ? '✓' : (locked ? lockSvg(12) : i);
  var badge = st.id==='inicio' ? '' : '<span class="n">'+mark+'</span>';
  out += '<button type="button" class="'+cls+'" data-go="'+st.id+'"'+(S.cur===st.id?' aria-current="step"':'')+'>'+badge+st.label+'</button>';
 });
 $('steps').innerHTML = out;
}
function go(id){
 if(S.cur==='vocab' && S.vocab.some(function(v){return v.w.trim();})) S.done.vocab = true;
 S.cur = id;
 var st = STEPS.filter(function(x){return x.id===id;})[0];
 if(st && st.mins && !S.start[id] && !S.done[id]){ S.start[id] = Date.now(); }
 save(); render(); window.scrollTo(0,0);
}

/* ---------- temporizador ---------- */
var tick = null;
function runTimer(){
 var el = $('timer'); if(tick){ clearInterval(tick); tick=null; }
 var st = STEPS.filter(function(x){return x.id===S.cur;})[0];
 if(!st || !st.mins || S.done[S.cur] || !S.start[S.cur]){ el.hidden = true; return; }
 el.hidden = false;
 function upd(){
  var left = st.mins*60 - Math.floor((Date.now()-S.start[S.cur])/1000);
  if(left<=0){ el.textContent = 'Tiempo terminado'; el.className='timer low'; var w=$('timeup'); if(w) w.hidden=false; clearInterval(tick); return; }
  var m = Math.floor(left/60), s = left%60;
  el.textContent = m+':'+(s<10?'0':'')+s;
  el.className = 'timer'+(left<300?' low':'');
 }
 upd(); tick = setInterval(upd, 1000);
}

/* ---------- piezas ---------- */
function instr(t){ return '<div class="instr"><b>INSTRUCCIONES</b>'+t+'<br>Marque las opciones elegidas en la Hoja de respuestas.</div>'; }
function qBlock(key, it, part, inl){
 var lock = !!S.done[part];
 var o = '<div class="q'+(lock?' locked-q':'')+(inl?' inl':'')+'" role="radiogroup" aria-labelledby="ql-'+key+'"><div class="qt" id="ql-'+key+'"><span class="num">'+it.n+'.</span>'+it.q+'</div><div class="opts">';
 it.o.forEach(function(op,i){
  var chk = S.ans[key]===i ? ' checked' : '';
  o += '<label class="opt"><input type="radio" name="r-'+key+'" value="'+i+'" data-k="'+key+'"'+chk+(lock?' disabled':'')+'><span class="bub">'+LET[i]+'</span><span>'+op+'</span></label>';
 });
 return o+'</div></div>';
}
function lBlock(key, it, part){
 var lock = !!S.done[part];
 var o = '<div class="q'+(lock?' locked-q':'')+'" role="radiogroup" aria-labelledby="ql-'+key+'"><div class="qt" id="ql-'+key+'"><span class="num">'+it.n+'.</span>'+it.q+'</div><div class="letters">';
 it.o.forEach(function(op,i){
  var chk = S.ans[key]===i ? ' checked' : '';
  o += '<label class="opt" title="'+esc(op)+'"><input type="radio" name="r-'+key+'" value="'+i+'" data-k="'+key+'"'+chk+(lock?' disabled':'')+' aria-label="'+LET[i]+'. '+esc(op)+'"><span class="bub">'+LET[i]+'</span></label>';
 });
 return o+'</div></div>';
}
function picBlock(key, it, part){
 var lock = !!S.done[part] || it.n===0;
 var hasImg = !!(D.imgBase && it.img);
 var o = '<div class="q'+(hasImg?' withimg':' noimg')+'" role="radiogroup" aria-labelledby="ql-'+key+'"><div class="qt" id="ql-'+key+'"><span class="num">'+it.n+'.</span>'+it.q+'</div>';
 if(hasImg) o += img(it.img, 'Tres opciones: '+it.o.join(', '), 'trip');
 o += '<div class="pics">';
 it.o.forEach(function(op,i){
  var chk = (S.ans[key]===i || (it.n===0 && it.ok===i)) ? ' checked' : '';
  o += '<label class="pic"><input type="radio" name="r-'+key+'" value="'+i+'" data-k="'+key+'"'+chk+(lock?' disabled':'')+'><span class="bub">'+LET[i]+'</span><span class="plbl">'+op+'</span></label>';
 });
 return o+'</div></div>';
}
document.addEventListener('change', function(e){
 var t = e.target;
 if(t.matches('input[type=radio][data-k]')){ S.ans[t.getAttribute('data-k')] = parseInt(t.value,10); save(); }
 if(t.matches('input[name=t2op]')){ S.t2op = t.value; save(); var c=$('t2checks'); if(c) c.innerHTML = pautas(S.t2op==='1'?D.escrita.t2.op1.pautas:D.escrita.t2.op2.pautas,'t2'+S.t2op+'-'); }
 if(t.matches('input[data-check]')){ S.checks[t.getAttribute('data-check')] = t.checked; save(); }
});
document.addEventListener('input', function(e){
 var t = e.target;
 if(t.id==='t1'||t.id==='t2'){ S[t.id]=t.value; save(); var c=$(t.id+'wc'); if(c) c.outerHTML = wcHtml(t.id); }
 if(t.matches('[data-v]')){ var p=t.getAttribute('data-v').split('-'); S.vocab[+p[1]][p[0]] = t.value; save(); }
 if(t.id==='dudas'){ S.dudas=t.value; save(); }
 if(t.matches('.sname')){ S.name=t.value; save(); }
});
function wcHtml(id){
 var r = id==='t1' ? D.escrita.t1 : D.escrita.t2; var n = words(S[id]);
 var ok = n>=r.min && n<=r.max;
 return '<div id="'+id+'wc" class="wc '+(n===0?'':(ok?'good':'bad'))+'">'+n+' palabras (recomendadas: entre '+r.min+' y '+r.max+')</div>';
}
function unanswered(keys){ return keys.filter(function(k){ return S.ans[k]===undefined; }); }
function keysOf(part, p){ var k=[]; tasksOf(part).forEach(function(t){ t.items.forEach(function(i){k.push(p+i.n);}); }); return k; }
function finishPart(part){
 var keys = part==='lectura' ? keysOf('lectura','L') : keysOf('auditiva','A');
 var miss = unanswered(keys);
 var msg = miss.length ? 'Tienes '+miss.length+' pregunta(s) sin contestar. En el DELE los errores no restan: es mejor marcar algo. ¿Entregar de todos modos?' : '¿Entregar esta parte? Después ya no podrás cambiar las respuestas.';
 ask(msg, 'Entregar', function(){ S.done[part]=true; save(); go(part==='lectura'?'auditiva':'escrita'); });
}
function timeUp(){ return '<div id="timeup" class="warn" hidden>Se ha terminado el tiempo. En el examen real ya no podrías seguir: entrega esta parte ahora.</div>'; }
function doneNote(part){ return S.done[part] ? '<div class="done-note">Parte entregada. Verás la corrección en Resultados cuando termines lectura, auditiva y escritura.</div>' : ''; }
function nameField(){ return '<label class="lbl-name"><b>Tu nombre</b><input type="text" class="sname" value="'+esc(S.name)+'" autocomplete="name"></label>'; }
function sendRow(kind){ return '<div class="row noprint"><button class="btn cta" data-act="copy" data-kind="'+kind+'">Copiar</button></div><div class="copied-box noprint" role="status" hidden>✓ Copiado. Pégalo en un email para enviárselo a tu profesora.</div><p class="muted small noprint">Correo de tu profesora: '+D.email+'</p>'; }
function resetBtn(){ return '<button class="btn" data-act="reset">Repetir el simulacro desde cero</button>'; }

/* ---------- vistas ---------- */
function vInicio(){
 var o = img(D.imgs && D.imgs.portada, 'Estudiantes en una clase de idiomas', 'hero');
 var real = TL>=60 && TA>=40;
 o += '<h2>Antes de empezar</h2><p class="lead">Este simulacro tiene las mismas tareas que el examen DELE A2: mismas instrucciones, mismo tipo de textos y misma numeración. '+(real?'Todas las pruebas tienen el tiempo real del examen.':'La lectura y la auditiva duran la mitad que en el examen; la escritura y la oral son completas.')+'</p>';
 o += '<table class="sem"><tbody>'+
  '<tr><td><b>1. Lectura</b></td><td>Tareas '+tNums('lectura')+', '+nItems('lectura')+' preguntas</td><td>'+TL+' minutos</td></tr>'+
  '<tr><td><b>2. Auditiva</b></td><td>Tareas '+tNums('auditiva')+', '+nItems('auditiva')+' preguntas</td><td>'+TA+' minutos</td></tr>'+
  '<tr><td><b>3. Escritura</b></td><td>Tareas 1 y 2 completas</td><td>45 minutos</td></tr>'+
  '<tr><td><b>4. Resultados</b></td><td>Corrección, transcripciones y qué repasar</td><td>al terminar 1, 2 y 3</td></tr>'+
  '<tr><td><b>5. Vocabulario</b></td><td>Palabras nuevas y dudas</td><td>sin tiempo</td></tr>'+
  '<tr><td><b>6. Oral</b></td><td>Prueba completa con tu profesora</td><td>en clase</td></tr></tbody></table>';
 o += '<h3>Qué repasas en esta unidad</h3><ul>'; D.recordatorio.forEach(function(r){ o+='<li>'+r+'</li>'; }); o += '</ul>';
 var TI = D.tipsInicio || ['<b>Lectura:</b> lee primero las preguntas y después el texto. La opción que repite las mismas palabras del texto suele ser una trampa; la correcta dice lo mismo con otras palabras.', '<b>Auditiva:</b> lee las preguntas y mira las opciones antes de escuchar. En la primera escucha marca una respuesta provisional; en la segunda, confírmala. No dejes nada en blanco.'];
 TI.forEach(function(t){ o += '<div class="tip">'+t+'</div>'; });
 o += '<p class="muted">El reloj de cada parte empieza cuando entras en ella y no se para, como en el examen. Tus respuestas se guardan en este navegador: puedes cerrar y seguir otro día.</p>';
 o += '<div class="row"><button class="btn cta" data-go="lectura">Empezar la lectura</button>'+(S.done.lectura||S.start.lectura?resetBtn():'')+'</div>';
 return o;
}
function vLectura(){
 var o = '<h2>Prueba 1. Comprensión de lectura</h2><p class="lead">Esta prueba tiene '+NT[tasksOf('lectura').length]+' tareas. Usted debe responder a '+nItems('lectura')+' preguntas. La duración es de '+TL+' minutos.</p>'+timeUp()+doneNote('lectura');
 tasksOf('lectura').forEach(function(tk,ti){
  o += '<h3'+(ti?' class="gap"':'')+'>Tarea '+tk.n+'</h3>'+instr(tk.instr)+(tk.tip?'<div class="tip">'+tk.tip+'</div>':'');
  if(tk.type==='mail'){ o += textoMail(tk); tk.items.forEach(function(it){ o += qBlock('L'+it.n, it, 'lectura'); }); }
  else if(tk.type==='ads'){
   var ex = tk.example;
   o += '<div class="example"><b>Ejemplo</b><div class="ad"><div class="lbl">TEXTO 0</div><h4>'+ex.title+'</h4>'+ex.body+'</div><div class="qt"><b>0.</b> '+ex.q+'</div>';
   ex.o.forEach(function(op,i){ o += '<div>'+LET[i]+') '+op+'</div>'; });
   o += '<div class="ex-ok">'+ex.why+'</div></div>';
   tk.items.forEach(function(it,i){ o += adHtml(it,i+1)+qBlock('L'+it.n, it, 'lectura'); });
  }
  else if(tk.type==='people'){ tk.items.forEach(function(it){ o += qBlock('L'+it.n, it, 'lectura', true); }); o += peopleTexts(tk); }
  else if(tk.type==='long'){ o += longText(tk); tk.items.forEach(function(it){ o += qBlock('L'+it.n, it, 'lectura'); }); }
 });
 if(!S.done.lectura) o += '<div class="row"><button class="btn cta" data-act="finish" data-part="lectura">Entregar la lectura</button></div>';
 else o += '<div class="row"><button class="btn" data-go="auditiva">Ir a la auditiva</button></div>';
 return o;
}
function textoMail(tk){ var o='<div class="paper"><div class="mailhead">'+tk.head.join('<br>')+'</div>'; tk.body.forEach(function(p){ o+='<p>'+p+'</p>'; }); return o+'</div>'; }
function peopleTexts(tk){ var o='<div class="people">'; tk.texts.forEach(function(t,i){ o += '<div class="paper"><h4>'+LET[i]+'. '+t.name.toUpperCase()+'</h4><p>'+t.body+'</p></div>'; }); return o+'</div>'; }
function longText(tk){ var o='<div class="paper"><h3>'+tk.title+'</h3>'+(tk.sub?'<div class="sub">'+tk.sub+'</div>':''); tk.body.forEach(function(p){ o+='<p>'+p+'</p>'; }); return o+'</div>'; }
function readingTexts(){ var o=''; tasksOf('lectura').forEach(function(tk){ o += '<h4>Tarea '+tk.n+'</h4>';
  if(tk.type==='mail') o += textoMail(tk);
  else if(tk.type==='ads') tk.items.forEach(function(it,i){ o += adHtml(it,i+1); });
  else if(tk.type==='people') o += peopleTexts(tk);
  else if(tk.type==='long') o += longText(tk); }); return o; }
function adHtml(it,n){ return '<div class="ad"><div class="lbl">TEXTO '+n+'</div><h4>'+it.title+'</h4>'+it.body+'</div>'; }
function audioBlock(src){
 return '<audio controls preload="none" src="'+src+'" data-src="'+src+'" onerror="audioErr(this)" oncanplay="audioOk(this)"></audio>'+
  '<div class="audio-miss noprint" role="alert" hidden>No se ha podido cargar el audio. Comprueba tu conexión y pulsa el botón para intentarlo otra vez. '+
  '<button type="button" class="btn" onclick="audioRetry(this)">Volver a cargar el audio</button>'+
  '<span class="audio-help" hidden> Si sigue sin funcionar, avisa a tu profesora.</span></div>';
}
// audio: si falla, reintenta solo una vez; si vuelve a fallar, muestra el botón
function audioSrc(a){ var s=a.getAttribute('data-src'); return s+(s.indexOf('?')<0?'?':'&')+'r='+Date.now(); }
function audioErr(a){
 if(!a.getAttribute('data-try')){ a.setAttribute('data-try','1'); setTimeout(function(){ a.src=audioSrc(a); a.load(); },1500); return; }
 a.nextElementSibling.hidden=false;
}
function audioOk(a){ var b=a.nextElementSibling; if(b) b.hidden=true; }
function audioRetry(btn){
 var box=btn.parentNode, a=box.previousElementSibling, n=+(a.getAttribute('data-manual')||0)+1;
 a.setAttribute('data-manual',n); box.hidden=true; a.src=audioSrc(a); a.load();
 var pr=a.play(); if(pr&&pr.catch) pr.catch(function(){});
 if(n>=2) box.querySelector('.audio-help').hidden=false;
}
window.audioErr=audioErr; window.audioOk=audioOk; window.audioRetry=audioRetry; // los usan los atributos onerror/onclick
function vAuditiva(){
 var o = '<h2>Prueba 2. Comprensión auditiva</h2><p class="lead">Esta prueba tiene '+NT[tasksOf('auditiva').length]+' tareas. Usted debe responder a '+nItems('auditiva')+' preguntas. La duración es de '+TA+' minutos, aproximadamente.</p>'+timeUp()+doneNote('auditiva');
 o += '<div class="tip">Pon cada audio al principio y no lo pares: las instrucciones, el ejemplo, las pausas y las repeticiones ya están dentro, como en el examen.</div>';
 tasksOf('auditiva').forEach(function(tk,ti){
  o += '<h3'+(ti?' class="gap"':'')+'>Tarea '+tk.n+'</h3>'+instr(tk.instr)+(tk.tip?'<div class="tip">'+tk.tip+'</div>':'')+audioBlock(D.audio['t'+tk.n]);
  var ex = tk.example;
  if(tk.type==='pics'){
   o += '<div class="example"><b>Ejemplo</b>'+picBlock('A0',{n:0,q:ex.q,o:ex.o,ok:ex.ok,img:ex.img},'auditiva')+'<div class="ex-ok">La opción correcta es la '+LET[ex.ok]+'.</div></div>';
   tk.items.forEach(function(it){ o += '<div class="conv">'+it.conv.toUpperCase()+'</div>'+picBlock('A'+it.n, it, 'auditiva'); });
  } else if(tk.type==='radio'){
   o += '<div class="example"><b>Ejemplo</b><div class="qt"><b>0.</b> '+ex.q+'</div>'; ex.o.forEach(function(op,i){ o+='<div>'+LET[i]+') '+op+'</div>'; }); o += '<div class="ex-ok">'+ex.why+'</div></div>';
   tk.items.forEach(function(it){ o += '<div class="conv">'+it.conv.toUpperCase()+'</div>'+qBlock('A'+it.n, it, 'auditiva'); });
  } else if(tk.type==='friends'){
   tk.items.forEach(function(it){ o += qBlock('A'+it.n, it, 'auditiva', true); });
  } else if(tk.type==='msgs'){
   o += '<div class="enun"><b style="width:auto">ENUNCIADOS</b>'; tk.enun.forEach(function(e,i){ o += '<div><b>'+LET[i]+'.</b>'+e+'</div>'; }); o += '</div>';
   o += '<div class="example"><b>Ejemplo</b><div class="qt">'+ex.q+': <b>'+LET[ex.ok]+'</b> ('+tk.enun[ex.ok]+')</div></div>';
   tk.items.forEach(function(it){ o += lBlock('A'+it.n, it, 'auditiva'); });
  }
 });
 if(!S.done.auditiva) o += '<div class="row"><button class="btn cta" data-act="finish" data-part="auditiva">Entregar la auditiva</button></div>';
 else o += '<div class="row"><button class="btn" data-go="escrita">Ir a la escritura</button></div>';
 return o;
}
var TIP_LINEAS = '<b>Cuenta tus palabras con los ojos.</b> En el examen escribes a mano y no hay contador. Acostúmbrate a escribir unas 10 palabras en cada línea: la tarea 1 (60-70 palabras) son 6 o 7 líneas y la tarea 2 (70-80 palabras), 7 u 8 líneas. Para entrenar, cuenta las palabras de tu primera línea: si tienes 8, necesitas una línea más; si tienes 12, una menos. Las palabras pequeñas también cuentan (el, de, y, en, me...).';
function pautas(list, pref){
 var o = '';
 list.forEach(function(p,i){ var k=pref+i; o += '<label><input type="checkbox" data-check="'+k+'"'+(S.checks[k]?' checked':'')+'><span>'+p+'</span></label>'; });
 return o;
}
function vEscrita(){
 var E = D.escrita, lock = !!S.done.escrita;
 var o = '<h2>Prueba 3. Expresión e interacción escritas</h2><p class="lead">Esta prueba contiene dos tareas. Usted debe elaborar dos textos. La duración es de 45 minutos.</p>'+timeUp();
 if(!lock) o += '<div class="tip">Marca cada punto de la instrucción cuando lo hayas escrito. Un texto sencillo que responde a todos los puntos aprueba; un texto bonito que olvida uno, no.</div>';
 if(!lock) o += '<div class="tip">'+(E.tipLineas||TIP_LINEAS)+'</div>';
 o += '<h3>Tarea 1</h3><div class="instr"><b>INSTRUCCIONES</b>'+E.t1.instr+'</div><div class="paper">'; E.t1.input.forEach(function(p){ o+='<p>'+p+'</p>'; }); o+='</div>';
 o += '<p><b>'+(E.t1.lead||'Conteste a su amigo. En el correo tiene que:')+'</b></p><div class="checks">'+pautas(E.t1.pautas,'t1-')+'</div><p>Número de palabras recomendadas: entre '+E.t1.min+' y '+E.t1.max+'.</p>';
 o += '<textarea id="t1" class="lined" aria-label="Texto de la tarea 1">'+esc(S.t1)+'</textarea>'+wcHtml('t1');
 o += '<h3 class="gap">Tarea 2</h3><div class="instr"><b>INSTRUCCIONES</b>'+E.t2.instr+'</div>';
 var o1=E.t2.op1, o2=E.t2.op2;
 o += '<div class="lamina"><h3>'+o1.title+'</h3><p>'+o1.intro+'</p><ul class="pautas">'; o1.pautas.forEach(function(p){o+='<li>'+p+'</li>';}); o+='</ul></div>';
 o += '<div class="lamina q"><h3>'+o2.title+'</h3><p>'+o2.intro+'</p>'+img(o2.img,o2.imgAlt||'Fotos','lam-img')+'<div class="photo-txt">'; o2.photos.forEach(function(p,i){ o+='<div class="photo"><b>Foto '+(i+1)+'.</b> '+p+'</div>'; });
 o += '</div><div class="ficha">'; o2.ficha.forEach(function(f){ o+='<div>'+f+'</div>'; }); o += '</div><p>'+o2.intro2+'</p><ul class="pautas">'; o2.pautas.forEach(function(p){o+='<li>'+p+'</li>';}); o += '</ul></div>';
 o += '<p><b>¿Qué opción eliges?</b></p><div class="choice"><label><input type="radio" name="t2op" value="1"'+(S.t2op==='1'?' checked':'')+'>Opción 1</label><label><input type="radio" name="t2op" value="2"'+(S.t2op==='2'?' checked':'')+'>Opción 2</label></div>';
 o += '<div class="checks" id="t2checks">'+(S.t2op?pautas(S.t2op==='1'?o1.pautas:o2.pautas,'t2'+S.t2op+'-'):'')+'</div>';
 o += '<p>Número de palabras recomendadas: entre '+E.t2.min+' y '+E.t2.max+'.</p><textarea id="t2" class="lined" aria-label="Texto de la tarea 2">'+esc(S.t2)+'</textarea>'+wcHtml('t2');
 if(!lock){ o += '<div class="row"><button class="btn cta" data-act="finishEsc">He terminado la escritura</button></div>'; }
 else {
  o += '<div class="sendbox"><h3>Envía tu escritura a tu profesora</h3><p>Tus dos textos están guardados en este navegador. Pulsa Copiar y pégalos en un correo a tu profesora para recibir la corrección.</p>'+nameField()+sendRow('escrita')+'</div>';
  o += '<div class="row">'+(allComp()?'<button class="btn cta" data-go="resultados">Ver mis resultados</button>':'<button class="btn cta" data-go="'+(!S.done.lectura?'lectura':'auditiva')+'">Terminar '+(!S.done.lectura?'la lectura':'la auditiva')+'</button>')+'</div>';
 }
 return o;
}

/* ---------- resultados ---------- */
function allItems(){
 var r=[];
 [['lectura','L','Lectura'],['auditiva','A','Auditiva']].forEach(function(p){
  tasksOf(p[0]).forEach(function(tk){ tk.items.forEach(function(i){ r.push({k:p[1]+i.n, part:p[2], task:'tarea '+tk.n, it:i, tr:i.tr||tk.tr}); }); });
 });
 return r;
}
function results(){
 var items = allItems(), lec=0, aud=0, cats={}, es={}, fails=[];
 items.forEach(function(x){
  var ok = S.ans[x.k]===x.it.ok;
  if(ok){ if(x.part==='Lectura') lec++; else aud++; }
  else { fails.push(x); es[x.it.es]=(es[x.it.es]||0)+1; }
  x.it.cats.forEach(function(c){ cats[c]=cats[c]||{t:0,ok:0}; cats[c].t++; if(ok) cats[c].ok++; });
 });
 return {lec:lec, aud:aud, cats:cats, es:es, fails:fails, nL:nItems('lectura'), nA:nItems('auditiva')};
}
function light(p){ return p>=80?'g':(p>=60?'a':'r'); }
function trHtml(lines){ return '<div class="tr">'+lines.map(function(l){ var m=l.match(/^([^:]{2,12}):\s(.*)$/); return m ? '<p><b>'+m[1]+':</b> '+m[2]+'</p>' : '<p class="muted"><i>'+l+'</i></p>'; }).join('')+'</div>'; }
function allTranscripts(){
 var o='';
 tasksOf('auditiva').forEach(function(tk){
  o += '<h4>Tarea '+tk.n+'</h4>';
  if(tk.tr) o += '<details><summary>'+(tk.trLabel||'Conversación')+'</summary>'+trHtml(tk.tr)+'</details>';
  if(tk.example && tk.example.tr) o += '<details><summary>'+(tk.exLabel||(tk.type==='pics'?'Conversación 0 (ejemplo)':'Audio 0 (ejemplo)'))+'</summary>'+trHtml(tk.example.tr)+'</details>';
  tk.items.forEach(function(it){ if(it.tr) o += '<details><summary>'+it.conv+'</summary>'+trHtml(it.tr)+'</details>'; });
 });
 return o;
}
function lockedMsg(){
 var falta=[]; if(!S.done.lectura) falta.push('la lectura'); if(!S.done.auditiva) falta.push('la auditiva'); if(!S.done.escrita) falta.push('la escritura');
 return '<div class="lockbox">'+lockSvg(34)+'<p>Esta parte se abre cuando entregues las tres pruebas. Te falta: <b>'+falta.join(', ')+'</b>.</p></div>';
}
function vResultados(){
 if(!allComp()) return '<h2>Resultados</h2>'+lockedMsg();
 var R = results(), pL=Math.round(R.lec/R.nL*100), pA=Math.round(R.aud/R.nA*100);
 var o = '<div id="printarea"><h2>Resultados</h2><p class="muted print-only">'+esc(S.name||'')+' · '+new Date().toLocaleDateString('es-ES')+' · '+document.title+'</p>';
 o += '<div class="score"><div><b>'+R.lec+'/'+R.nL+'</b><span><span class="dot '+light(pL)+'"></span>Lectura ('+pL+' %)</span></div><div><b>'+R.aud+'/'+R.nA+'</b><span><span class="dot '+light(pA)+'"></span>Auditiva ('+pA+' %)</span></div><div><b>Escritura</b><span>La corrige tu profesora</span></div></div>';
 o += '<p class="muted">Referencia DELE: para el APTO necesitas aproximadamente un 60 % en cada grupo de pruebas.</p>';
 var rows = Object.keys(R.cats).map(function(k){ var c=R.cats[k]; return {k:k,p:Math.round(c.ok/c.t*100),c:c}; }).sort(function(a,b){return a.p-b.p;}).slice(0,8);
 o += '<h3>Semáforo por contenidos</h3><table class="sem"><tbody>';
 rows.forEach(function(r){ var l=light(r.p); var txt = l==='g'?'Dominado.':(l==='a'?'Casi. Repásalo con un ejercicio corto.':'Prioridad: repásalo antes del siguiente simulacro.');
  o += '<tr><td><span class="dot '+l+'"></span>'+D.cats[r.k].name+'</td><td>'+r.c.ok+'/'+r.c.t+'</td><td>'+txt+'</td></tr>'; });
 o += '</tbody></table>';
 var rev = rows.filter(function(r){ return r.p<80; });
 if(rev.length){ o += '<h3>Qué tienes que repasar</h3>'; rev.forEach(function(r){ var c=D.cats[r.k]; o += '<div class="review"><b><span class="dot '+light(r.p)+'"></span>'+c.name+'</b><div>'+c.repaso+'</div><div class="reto">Mini reto: '+c.reto+'</div></div>'; }); }
 else o += '<div class="done-note">¡Muy bien! No tienes contenidos en ámbar ni en rojo. Puedes pasar al siguiente simulacro.</div>';
 var tips = Object.keys(R.es).sort(function(a,b){return R.es[b]-R.es[a];}).slice(0,2);
 if(tips.length){ o += '<h3>Consejo de examen para ti</h3>'; tips.forEach(function(t){ o += '<div class="tip">'+D.estrategias[t]+'</div>'; }); }
 o += '<h3>Tus errores, uno por uno</h3>';
 if(!R.fails.length) o += '<p>No has fallado ninguna pregunta.</p>';
 R.fails.forEach(function(x){ var a=S.ans[x.k];
  o += '<div class="fail"><b>'+x.part+', '+x.task+', pregunta '+x.it.n+'.</b> '+x.it.q+'<div class="yours">Tu respuesta: '+(a===undefined?'sin contestar':LET[a]+') '+x.it.o[a])+'<br>Correcta: '+LET[x.it.ok]+') '+x.it.o[x.it.ok]+'</div><div>'+x.it.why+'</div>'+(x.tr?'<details><summary>Ver la transcripción</summary>'+trHtml(x.tr)+'</details>':'')+'</div>'; });
 o += '<h3>Transcripciones de los audios</h3><p class="muted noprint">Escucha otra vez el audio leyendo la transcripción: es la mejor forma de entrenar el oído.</p><div class="noprint">'+allTranscripts()+'</div></div>';
 o += '<div class="sendbox noprint"><h3>Guarda y envía tus resultados</h3>'+nameField()+'<div class="row"><button class="btn cta" data-act="pdf">Guardar en PDF</button></div><p class="muted small">Se abre la ventana de imprimir: en "Destino" elige "Guardar como PDF".</p>'+sendRow('resultados')+'</div>';
 o += '<div class="row noprint"><button class="btn cta" data-go="vocab">Siguiente: vocabulario</button>'+resetBtn()+'</div>';
 return o;
}
function vVocab(){
 if(!allComp()) return '<h2>Vocabulario y dudas</h2>'+lockedMsg();
 var o = '<h2>Vocabulario y dudas</h2><p class="lead">Vuelve a leer los textos y las transcripciones de los audios. ¿Qué palabras no conocías? Busca su significado y escribe una frase tuya con cada una, sobre tu vida.</p>';
 o += '<details><summary>Ver los textos de la lectura</summary>'+readingTexts()+'</details>';
 o += '<details><summary>Ver las transcripciones de los audios</summary>'+allTranscripts()+'</details>';
 o += '<h3 class="gap">Mis palabras nuevas</h3>';
 S.vocab.forEach(function(v,i){ o += '<div class="vocab-row"><input type="text" data-v="w-'+i+'" value="'+esc(v.w)+'" placeholder="Palabra" aria-label="Palabra '+(i+1)+'"><input type="text" data-v="f-'+i+'" value="'+esc(v.f)+'" placeholder="Mi frase con esta palabra" aria-label="Frase '+(i+1)+'"><button type="button" aria-label="Quitar fila" data-act="delv" data-i="'+i+'">&times;</button></div>'; });
 o += '<div class="row"><button class="btn" data-act="addv">Añadir otra palabra</button></div>';
 o += '<h3>Dudas para tu profesora</h3><p class="muted">Una frase que no entiendes, una pregunta que no sabes por qué está mal...</p><textarea id="dudas" style="min-height:110px">'+esc(S.dudas)+'</textarea>';
 o += '<div class="sendbox"><h3>Envía tu vocabulario y tus dudas</h3>'+nameField()+sendRow('vocab')+'</div>';
 return o;
}

/* ---------- paquetes para enviar ---------- */
function head(t){ return ['SIMULACRO DELE A2 - UNIDAD '+D.unit+': '+D.title, t, 'Nombre: '+(S.name||'-'), '']; }
function packEscrita(){ var L=head('EXPRESION ESCRITA');
 L.push('TAREA 1 ('+words(S.t1)+' palabras):'); L.push(S.t1||'-'); L.push('');
 L.push('TAREA 2, opcion '+(S.t2op||'-')+' ('+words(S.t2)+' palabras):'); L.push(S.t2||'-'); return L.join('\n'); }
function plain(t){ return String(t==null?'':t).replace(/<[^>]+>/g,'').replace(/&nbsp;/g,' '); }
function packRes(){ var R=results(), L=head('RESULTADOS');
 L.push('Lectura: '+R.lec+'/'+R.nL+' | Auditiva: '+R.aud+'/'+R.nA); L.push('');
 // contenidos flojos, con lo que se le ha sugerido al estudiante
 var rev=[]; Object.keys(R.cats).forEach(function(k){ var c=R.cats[k], p=Math.round(c.ok/c.t*100); if(p<80) rev.push({k:k,p:p,c:c}); });
 rev.sort(function(a,b){ return a.p-b.p; });
 L.push('A REPASAR (sugerencias para practicar):');
 if(!rev.length) L.push('- nada: todo en verde');
 rev.forEach(function(r){ var d=D.cats[r.k];
  var qs=R.fails.filter(function(x){ return x.it.cats.indexOf(r.k)>-1; }).map(function(x){ return x.part.charAt(0)+x.it.n; });
  L.push('- '+(r.p<60?'[ROJO] ':'[AMBAR] ')+d.name+' ('+r.c.ok+'/'+r.c.t+')'+(qs.length?' · falladas: '+qs.join(', '):''));
  L.push('  Repaso: '+plain(d.repaso));
  L.push('  Mini reto: '+plain(d.reto));
 });
 L.push('');
 var tips=Object.keys(R.es).sort(function(a,b){return R.es[b]-R.es[a];});
 L.push('ESTRATEGIAS QUE FALLAN:');
 if(!tips.length) L.push('- ninguna');
 tips.forEach(function(t){ L.push('- '+t+' ('+R.es[t]+' fallo'+(R.es[t]>1?'s':'')+'): '+plain(D.estrategias[t])); });
 L.push('');
 L.push('ERRORES, UNO POR UNO:');
 if(!R.fails.length) L.push('- ninguno');
 R.fails.forEach(function(x){ var a=S.ans[x.k];
  L.push('- '+x.part+', '+x.task+', pregunta '+x.it.n+': '+plain(x.it.q));
  L.push('  Marcó: '+(a===undefined?'nada':LET[a]+') '+plain(x.it.o[a]))+' | Correcta: '+LET[x.it.ok]+') '+plain(x.it.o[x.it.ok]));
  L.push('  Contenido: '+x.it.cats.map(function(c){ return D.cats[c].name; }).join(' / ')+' | Estrategia: '+(x.it.es||'-'));
 });
 return L.join('\n'); }
function packVocab(){ var L=head('VOCABULARIO Y DUDAS');
 S.vocab.filter(function(v){return v.w.trim();}).forEach(function(v){ L.push('- '+v.w+': '+(v.f||'')); });
 L.push(''); L.push('DUDAS:'); L.push(S.dudas||'-'); return L.join('\n'); }
var PACK = {escrita:packEscrita, resultados:packRes, vocab:packVocab};
var SUBJ = {escrita:'Escrita', resultados:'Resultados', vocab:'Vocabulario y dudas'};

/* ---------- acciones ---------- */
var ACTS = {
 finish: function(b){ finishPart(b.getAttribute('data-part')); },
 finishEsc: function(){
  var probs=[];
  if(words(S.t1)<20) probs.push('la tarea 1 está casi vacía');
  if(!S.t2op) probs.push('no has elegido opción en la tarea 2');
  if(words(S.t2)<20) probs.push('la tarea 2 está casi vacía');
  ask((probs.length?'Atención: '+probs.join(', ')+'. ':'')+'¿Has terminado la escritura?', 'He terminado', function(){ S.done.escrita=true; save(); render(); var sb=document.querySelector('.sendbox'); if(sb && sb.scrollIntoView) sb.scrollIntoView(); });
 },
 copy: function(b){
  var t = PACK[b.getAttribute('data-kind')](), box = b.closest('.row').nextElementSibling;
  function ok(){ box.hidden=false; box.className='copied-box noprint'; box.innerHTML='✓ Copiado. Pégalo en un email para enviárselo a tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad noprint'; box.innerHTML='No se ha podido copiar automáticamente. Selecciona tu texto, cópialo y pégalo en un email para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.top='0'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.focus(); ta.select(); try{ ta.setSelectionRange(0, t.length); }catch(e){} var done=false; try{ done=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(done) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext){ navigator.clipboard.writeText(t).then(ok, fb); } else fb();
 },
 mail: function(b){ var k=b.getAttribute('data-kind');
  location.href = 'mailto:'+D.email+'?subject='+encodeURIComponent('DELE A2 Unidad '+D.unit+' - '+SUBJ[k]+' - '+(S.name||''))+'&body='+encodeURIComponent(PACK[k]()); },
 pdf: function(){ var ds=document.querySelectorAll('#printarea details'); for(var i=0;i<ds.length;i++) ds[i].open=true; window.print(); },
 reset: function(){ ask('Se borrarán todas tus respuestas, tus textos y tu vocabulario, y el simulacro volverá a empezar. ¿Seguro?', 'Sí, empezar de cero', function(){ var n=S.name; S=blank(); S.name=n; save(); render(); window.scrollTo(0,0); }); },
 addv: function(){ S.vocab.push({w:'',f:''}); save(); render(); },
 delv: function(b){ S.vocab.splice(+b.getAttribute('data-i'),1); if(!S.vocab.length) S.vocab.push({w:'',f:''}); save(); render(); },
 unlock: function(){ var v = ($('code').value||'').toUpperCase().replace(/[^A-Z0-9]/g,''); if(h(D.examen+'|'+v)===D.oralHash){ S.oral=true; save(); render(); } else { $('cerr').textContent='Ese código no es correcto. Pídeselo a tu profesora.'; } },
 prep: function(){ var el=$('prep'), end=Date.now()+12*60000; el.hidden=false; if(ACTS._pt) clearInterval(ACTS._pt);
  ACTS._pt=setInterval(function(){ var l=Math.max(0,Math.round((end-Date.now())/1000)); el.textContent='Preparación '+Math.floor(l/60)+':'+((l%60)<10?'0':'')+(l%60); if(!l){ clearInterval(ACTS._pt); el.textContent='Preparación terminada'; el.className='timer low'; } },1000); }
};

/* ---------- cronometros (sin guardar: se reinician al recargar) ---------- */
var SW = {};
function swHtml(id, label, min, max){
 return '<span class="sw noprint" id="sw-'+id+'" data-min="'+min+'" data-max="'+max+'"><span class="sw-lbl">'+label+' · '+min+'-'+max+' min</span><span class="sw-t">0:00</span>'+
  '<button type="button" class="sw-b" data-sw="go" data-id="'+id+'" aria-label="Empezar o pausar">&#9654;</button>'+
  '<button type="button" class="sw-b" data-sw="reset" data-id="'+id+'" aria-label="Poner a cero">&#8634;</button></span>';
}
function swFmt(s){ return Math.floor(s/60)+':'+((s%60)<10?'0':'')+(s%60); }
function swSecs(id){ var w=SW[id]; if(!w) return 0; return Math.floor((w.acc + (w.run? Date.now()-w.t0 : 0))/1000); }
function swPaint(id){
 var el=document.getElementById('sw-'+id); if(!el) return;
 var s=swSecs(id), min=+el.getAttribute('data-min')*60, max=+el.getAttribute('data-max')*60;
 el.querySelector('.sw-t').textContent=swFmt(s);
 el.className='sw noprint'+(SW[id]&&SW[id].run?' run':'')+(s>=max?' over':(s>=min?' ok':(s>=min-30&&s>0?' near':'')));
 var b=el.querySelector('[data-sw=go]'); b.innerHTML = SW[id]&&SW[id].run ? '&#10074;&#10074;' : '&#9654;';
}
function swAll(){ for(var k in SW) swPaint(k); }
setInterval(function(){ for(var k in SW){ if(SW[k].run) swPaint(k); } }, 500);
document.addEventListener('click', function(e){
 var b=e.target.closest('[data-sw]'); if(!b) return;
 var id=b.getAttribute('data-id'), w=SW[id]||(SW[id]={acc:0,run:false,t0:0});
 if(b.getAttribute('data-sw')==='go'){ if(w.run){ w.acc+=Date.now()-w.t0; w.run=false; } else { w.t0=Date.now(); w.run=true; } }
 else { w.acc=0; w.run=false; }
 swPaint(id); if(window.onSwChange) window.onSwChange(id, swSecs(id));
});

/* ---------- oral ---------- */
function vOral(){
 var O = D.oral;
 if(!S.oral){
  return '<h2>Prueba 4. Expresión e interacción orales</h2><div class="lockbox">'+img(D.imgs&&D.imgs.oralLock,'Una clase de español','lock-img')+lockSvg(34)+'<h3>Esta prueba se hace en clase</h3><p class="muted small">Examen '+D.examen+'</p><p>La oral la haces con tu profesora, como en el examen. Ella te dará el código para abrirla cuando estéis juntas.</p><label for="code"><b>Código</b></label><input type="text" id="code" autocomplete="off" style="margin:6px 0"><div class="row"><button class="btn cta" data-act="unlock">Abrir la prueba oral</button></div><div id="cerr" class="err" aria-live="polite"></div><p class="small" style="margin:14px 0 0"><a href="'+D.panel+'#'+D.examen+'" target="_blank" rel="noopener" class="muted">Acceso profesora</a></p></div>';
 }
 var o = '<h2>Prueba 4. Expresión e interacción orales</h2>';
 o += '<div class="instr"><b>INSTRUCCIONES</b>La prueba tiene tres tareas. Tarea 1: monólogo sobre un tema (2-3 minutos). Tarea 2: descripción de una fotografía (2-3 minutos). Tarea 3: diálogo con el entrevistador en una situación relacionada con la fotografía de la Tarea 2 (3-4 minutos). Tiene 12 minutos para preparar las tres tareas. Puede tomar notas y escribir un esquema, pero no leerlo durante la prueba.</div>';
 o += '<div class="row"><button class="btn cta" data-act="prep">Empezar los 12 minutos de preparación</button><span id="prep" class="timer" hidden></span></div>';
 o += '<div class="tip"><b>Cronómetro:</b> cada tarea tiene uno al lado del título. Púlsalo cuando empieces a hablar: se pone verde cuando llevas el tiempo mínimo y rojo si te pasas del máximo.</div>';
 o += '<h3 class="hsw">Tarea 1. Monólogo'+swHtml('t1','Hablar',2,3)+'</h3><p>'+O.t1.instr+'</p>'; O.t1.ops.forEach(function(op){ o+='<div class="lamina"><h3>'+op.title+'</h3><p>Hable de:</p><ul class="pautas">'; op.pautas.forEach(function(p){o+='<li>'+p+'</li>';}); o+='</ul></div>'; });
 o += '<h3 class="hsw">Tarea 2. Descripción de una fotografía'+swHtml('t2','Hablar',2,3)+'</h3><p>'+O.t2.instr+'</p>'; O.t2.fotos.forEach(function(f){ o+='<div class="lamina q"><h3>'+f.title+'</h3>'+img(f.img, f.desc, 'lam-img')+'<div class="photo photo-txt">'+f.desc+'</div></div>'; });
 o += '<p><b>Hable de:</b></p><ul class="pautas">'; O.t2.pautas.forEach(function(p){o+='<li>'+p+'</li>';}); o += '</ul>';
 o += '<h3 class="hsw">Tarea 3. Diálogo en una situación imaginaria'+swHtml('t3','Conversar',3,4)+'</h3><p>'+O.t3.instr+'</p>'; O.t3.ops.forEach(function(op){ o+='<div class="lamina"><h3>'+op.title+'</h3><p>'+op.intro+'</p><ul class="pautas">'; op.pautas.forEach(function(p){o+='<li>'+p+'</li>';}); o+='</ul></div>'; });
 o += '<div class="tip"><b>Qué se valora:</b> que respondas a lo que te piden con orden (coherencia), que sigas hablando aunque hagas pausas (fluidez), que uses bien lo básico (corrección) y que tengas vocabulario del tema (alcance). Si no sabes una palabra, descríbela: también puntúa.</div>';
 o += '<p class="muted small noprint" style="margin:28px 0 0"><a href="'+D.panel+'#'+D.examen+'" target="_blank" rel="noopener" class="muted">Acceso profesora</a></p>';
 return o;
}

/* ---------- render ---------- */
var VIEWS = {inicio:vInicio, lectura:vLectura, auditiva:vAuditiva, vocab:vVocab, escrita:vEscrita, resultados:vResultados, oral:vOral};
function render(){
 renderNav();
 $('app').innerHTML = '<section class="view on">'+VIEWS[S.cur]()+'</section><footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>';
 runTimer(); swAll();
}
document.addEventListener('keydown', function(e){ if(e.key==='Escape' && !$('ask').hidden){ $('ask').hidden=true; pending=null; } });
render();
})();
"""

def enc_html(s):
    return ''.join(c if ord(c)<128 else '&#x%X;'%ord(c) for c in s)
def enc_js(s):
    out=[]
    for c in s:
        o=ord(c)
        if o<128: out.append(c)
        elif o<=0xFFFF: out.append('\\u%04X'%o)
        else:
            o-=0x10000; out.append('\\u%04X\\u%04X'%(0xD800+(o>>10),0xDC00+(o&0x3FF)))
    return ''.join(out)

H1 = 'Simulacro DELE A2 · Unidad %d: %s' % (int(DATA['unit']), DATA['title'])
HTML_BODY = HTML_BODY.replace('__H1__', H1)
js = JS.replace('__DATA__', json.dumps(DATA, ensure_ascii=True))
js = enc_js(js)
page = ('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
 '<title>'+enc_html(H1)+'</title>\n'
 '<style>'+enc_html(CSS)+'</style>\n</head>\n<body>\n'+enc_html(HTML_BODY)+
 '<script>\n'+js+'\n</script>\n</body>\n</html>\n')
open('DELEA2_F1_U%s_simulacro.html' % DATA['unit'],'w',encoding='ascii').write(page)
# libreta oral de la profesora (módulo común A2/B2: DELE_oral_profesora.py, en la misma carpeta)
import DELE_oral_profesora as OP
open('DELEA2_F1_U%s_oral_profesora.html' % DATA['unit'],'w',encoding='ascii').write(
    OP.build('A2', EXAMEN, ORAL_CODE, H1, PROF_ORAL, PROF_CATS, CSS, PROF.get('guion'), PROF.get('errores')))
open('app.js','w').write(js)
print('ok', len(page), 'examen', EXAMEN, 'codigo de la oral:', ORAL_CODE)
