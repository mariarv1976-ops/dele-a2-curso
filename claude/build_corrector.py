# -*- coding: utf-8 -*-
# CORRECTOR DE LA ESCRITURA DE LA PROFESORA (curso DELE A2)
# Uso: python3 build_corrector.py -> DELEA2_corrector_escritura.html
# Va en la carpeta protegida biblioteca/profesora/ (nunca en la parte publica).
# Flujo: pegar lo que envia el estudiante -> copiar la peticion para Claude -> pegar la respuesta
#        -> revisar bandas y errores -> informe en PDF / texto para el correo.
# Para que el informe enlace una ficha de remedio, pon su codigo en FICHAS_LISTAS cuando este publicada.
import json
from curso_comun import CSS, BASE_URL, page
from corrector_tareas import EXAMENES

FILE = "DELEA2_corrector_escritura.html"
FICHAS_LISTAS = []   # p. ej. ["R01", "R02", "R07"] cuando esten subidas a dele-curso/

FICHAS = {
 "R01": ("Pasados: perfecto, indefinido e imperfecto", "DELEA2_curso_R01_pasados.html"),
 "R02": ("Hay / está / es", "DELEA2_curso_R02_hay_esta_es.html"),
 "R03": ("Ser y estar", "DELEA2_curso_R03_ser_estar.html"),
 "R04": ("Concordancia y posesivos", "DELEA2_curso_R04_concordancia.html"),
 "R05": ("Muy / mucho · también / tampoco", "DELEA2_curso_R05_muy_mucho.html"),
 "R06": ("Preposiciones frecuentes", "DELEA2_curso_R06_preposiciones.html"),
 "R07": ("Tú y usted", "DELEA2_curso_R07_tu_usted.html"),
 "R08": ("Conectores para enlazar", "DELEA2_curso_R08_conectores.html"),
 "R09": ("Verbos como gustar", "DELEA2_curso_R09_gustar.html"),
 "R10": ("Pronombres lo / la / le", "DELEA2_curso_R10_pronombres.html"),
 "R11": ("Planes y futuro", "DELEA2_curso_R11_futuro.html"),
 "R12": ("Traer / llevar · ir / venir · pedir / preguntar", "DELEA2_curso_R12_traer_llevar.html"),
 "R13": ("Fórmulas de los correos", "DELEA2_curso_R13_formulas_correo.html"),
 "R14": ("Vocabulario", "DELEA2_curso_R14_vocabulario.html"),
}

RUBRICA = """CUMPLIMIENTO DE LA TAREA
3 = Cumple sobradamente los objetivos comunicativos. Incluye, junto con la información pedida, algún detalle, comentario, valoración, opinión o motivo relevantes.
2 = Responde a la situación planteada y aporta la información requerida de forma comprensible, aunque puede que omita, malinterprete o responda de forma incomprensible UNO de los puntos.
1 = Se aproxima, pero no logra cumplir el objetivo: aporta solo algunos datos, insuficientes. Omite, malinterpreta o responde de forma incomprensible DOS O MÁS puntos.
0 = En blanco, no sigue los puntos de orientación, información irrelevante o texto ilegible.

USO DE LA LENGUA
3 = Bastante precisión y control razonable de elementos relativamente sencillos (combinación de pasados, perífrasis, futuro...), aunque con algún error. Texto cohesionado, con subordinadas (de relativo, sustantivas), conectores frecuentes (además, sin embargo, aunque, como...) y organizadores (por otro lado, en primer lugar...).
2 = Repertorio limitado (presente y pasados de indicativo, pronombres, posesivos, perífrasis frecuentes como tener que o ir a) que le permite transmitir el mensaje con oraciones breves enlazadas con organizadores (primero, después...), conectores sencillos (por eso...) y relativos. Errores básicos y sistemáticos (ser/estar/haber, concordancias, pasados regulares e irregulares, referencias, puntuación) que NO dificultan la comprensión.
1 = Léxico y estructuras muy básicos, insuficientes para transmitir la información. Abundantes errores básicos, ortográficos e imprecisiones léxicas que dificultan la comprensión. Frases aisladas o enlazadas solo con y, pero, porque; texto desorganizado y mal puntuado.
0 = Sin muestra suficiente para evaluar."""

ESQUEMA = """{
  "tareas": [
    {
      "tarea": 1,
      "pautas": [
        {"pauta": "saludar", "estado": "si", "comentario": "Saludas con «Hola, Elena»."}
      ],
      "cumplimiento": 2,
      "uso": 2,
      "justificacion": "Para la profesora: por qué estas bandas.",
      "errores": [
        {"original": "fui muy cansado", "correccion": "estaba muy cansado", "tipo": "GR", "ficha": "R03", "explicacion": "Para hablar de cómo te sientes usamos estar.", "importante": true}
      ],
      "bien": ["...", "..."],
      "prioridad": "...",
      "modelo": "..."
    }
  ],
  "comentario_global": "..."
}"""

CSS_C = CSS + r"""
.wrap{max-width:900px}.top-in{max-width:900px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin:14px 0}
.card h3{margin-top:0}
label.f{display:block;font-weight:600;margin:12px 0 4px}
input[type=text],input[type=number],select,textarea{font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 12px;background:#fff;color:var(--ink);width:100%}
input[type=number]{width:7em}
textarea{min-height:120px;line-height:1.5;resize:vertical}
textarea.big{min-height:220px}
textarea.mono{font-family:'SF Mono',Consolas,monospace;font-size:.85rem}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.wc{font-size:.85rem;color:var(--muted);margin-top:2px}.wc.ok{color:var(--ok)}.wc.no{color:var(--amb)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0}
.chips label{border:2px solid var(--line);border-radius:999px;padding:4px 14px;cursor:pointer;background:#fff;font-weight:500}
.chips label:has(input:checked){border-color:var(--ink);background:var(--ink);color:#fff}
.chips input{position:absolute;opacity:0}
.msg{border-radius:8px;padding:10px 14px;margin:10px 0}
.msg.ok{background:var(--ok-soft);color:var(--ok)}.msg.bad{background:var(--bad-soft);color:var(--bad)}.msg.amb{background:var(--amb-soft);color:#7A4E0E}
.msg[hidden]{display:none}
.task-ref{font-size:.93rem}.task-ref ol,.task-ref ul{margin:4px 0 8px;padding-left:1.3em}
.task-ref .in{background:var(--paper);border-radius:8px;padding:8px 12px;margin:6px 0;font-family:Georgia,serif}
.bands{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0}
.bands select{font-weight:700}
.bands .d{font-size:.82rem;color:var(--muted);margin-top:4px;line-height:1.4}
.just{font-size:.9rem;background:#EEF0F7;color:#2B3270;border-radius:8px;padding:8px 12px;margin:8px 0}
table.t td select{width:auto;padding:4px 8px}
table.t td input[type=text]{padding:4px 8px;font-size:.9rem}
.err-off td{opacity:.45;text-decoration:line-through}
.score-box{display:flex;gap:12px;flex-wrap:wrap;align-items:stretch;margin:12px 0}
.score-box div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 16px}
.score-box b{font-family:Georgia,serif;font-size:1.6rem;display:block;line-height:1.1}
.score-box span{font-size:.85rem;color:var(--muted)}
.hist td{font-size:.9rem}
.hist .btn{padding:3px 12px;font-size:.82rem}
/* informe */
#rep{-webkit-print-color-adjust:exact;print-color-adjust:exact;background:#fff;border:1px solid var(--line);border-radius:12px;padding:26px 30px}
#rep h2{margin-top:0}
#rep .sub{color:var(--muted);font-size:.92rem;margin-top:-6px}
#rep .tk{border-top:3px solid var(--coral);margin-top:26px;padding-top:12px}
#rep .pl{list-style:none;padding:0;margin:6px 0}
#rep .pl li{padding:5px 0 5px 30px;position:relative;border-bottom:1px dashed var(--line);line-height:1.45}
#rep .pl li:before{position:absolute;left:2px;top:5px;width:20px;height:20px;border-radius:50%;display:grid;place-items:center;font-size:.75rem;font-weight:700;color:#fff}
#rep .pl li.si:before{content:"\2713";background:var(--ok)}
#rep .pl li.parcial:before{content:"\00BD";background:var(--amb)}
#rep .pl li.no:before{content:"\2715";background:var(--bad)}
#rep .pl small{color:var(--muted);display:block}
#rep .txt{font-family:Georgia,serif;line-height:1.9;background:var(--paper);border-radius:8px;padding:12px 16px;white-space:pre-wrap}
#rep mark{background:var(--bad-soft);color:inherit;border-bottom:2px solid var(--bad);padding:0 1px;border-radius:2px}
#rep mark sup{color:var(--bad);font-weight:700;font-family:system-ui,sans-serif;font-size:.7em;margin-left:1px}
#rep .el{margin:6px 0;padding-left:0;list-style:none}
#rep .el li{margin:6px 0;line-height:1.45}
#rep .el .n{display:inline-block;min-width:1.8em;color:var(--bad);font-weight:700}
#rep .el .o{text-decoration:line-through;color:var(--bad)}
#rep .el .c{color:var(--ok);font-weight:600}
#rep .el .tg{font-size:.72rem;font-weight:700;border-radius:4px;padding:1px 6px;background:#EFEAE4;color:var(--muted);margin-left:4px}
#rep .imp{background:var(--coral-soft);border-radius:10px;padding:10px 14px;margin:10px 0}
#rep .imp li{margin:6px 0}
#rep .good{background:var(--ok-soft);border-radius:10px;padding:10px 14px;margin:10px 0}
#rep .model{font-family:Georgia,serif;line-height:1.7;border-left:4px solid var(--ok);padding:6px 14px;white-space:pre-wrap}
#rep .sem{width:100%;border-collapse:collapse;margin:8px 0}
#rep .sem td{padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
.dot{display:inline-block;width:13px;height:13px;border-radius:50%;margin-right:8px;vertical-align:-1px}
.dot.a{background:var(--amb)}.dot.r{background:var(--bad)}.dot.g{background:var(--ok)}
#rep .big{display:flex;gap:12px;flex-wrap:wrap;margin:12px 0}
#rep .big div{border:2px solid var(--ink);border-radius:10px;padding:10px 16px}
#rep .big b{font-family:Georgia,serif;font-size:1.7rem;display:block;line-height:1.1}
#rep .big span{font-size:.85rem;color:var(--muted)}
#rep .foot{font-size:.82rem;color:var(--muted);border-top:1px solid var(--line);margin-top:24px;padding-top:10px}
@media (max-width:700px){.grid2,.bands{grid-template-columns:1fr}#rep{padding:16px}}
@media print{header.top,.noprint,footer.legal{display:none!important}body{background:#fff}section.view{display:none!important}#v-informe{display:block!important;padding:0}#rep{border:0;padding:0}.tk{break-inside:auto}#rep .imp,#rep .good{break-inside:avoid}}
"""

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">Corrector de la escritura · DELE A2</h1><small>Solo para la profesora · el informe del estudiante sale en el paso 4</small></div>
 <nav class="steps" id="steps" aria-label="Pasos"></nav>
</div></header>
<main class="wrap">
<section class="view" id="v-texto"></section>
<section class="view" id="v-claude"></section>
<section class="view" id="v-revisar"></section>
<section class="view" id="v-informe"></section>
<footer class="legal">Corrección con la escala oficial del DELE A2 (uso de la lengua 66 % y cumplimiento de la tarea 34 %, bandas de 0 a 3). Lo que guardas aquí se queda en este navegador.</footer>
</main>
"""

JS = r"""
(function(){
var D = __DATA__;
var EX = {}; D.ex.forEach(function(e){ EX[e.id]=e; });
var KEY='dele-a2-corrector-actual', HKEY='dele-a2-corrector-hist';
var STEPS=[['texto','Texto'],['claude','Claude'],['revisar','Revisar'],['informe','Informe']];
var BL={0:'Sin muestra válida',1:'No llega al A2',2:'A2: aprobado',3:'Supera el A2'};
var TIPOS={GR:'gramática',LEX:'vocabulario',ORT:'ortografía',COH:'conectores y orden',ADE:'registro y tipo de texto'};
var EST={si:'Hecho',parcial:'A medias',no:'Falta'};
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function words(t){ var m=String(t||'').trim().match(/\S+/g); return m?m.length:0; }
function fmt(n){ return (Math.round(n*100)/100).toFixed(2).replace('.',','); }
function blank(){ return {step:'texto', exam:D.ex[0].id, name:'', t1:'', t2:'', t2op:'1', which:'ambas', otra1:'', otra2:'', lect:'', resp:'', C:null, hid:null}; }
function load(k,d){ try{ var r=localStorage.getItem(k); if(r) return JSON.parse(r); }catch(e){} return d; }
function save(){ try{ localStorage.setItem(KEY, JSON.stringify(S)); }catch(e){} }
var S = load(KEY, null) || blank(); (function(){ var b=blank(); for(var k in b) if(!(k in S)) S[k]=b[k]; })();
var H = load(HKEY, []);
function saveH(){ try{ localStorage.setItem(HKEY, JSON.stringify(H)); }catch(e){ alert('No se ha podido guardar el historial (el navegador no tiene espacio). Borra correcciones antiguas.'); } }

/* ------------ navegacion ------------ */
function nav(){
 var o='', can={texto:true, claude:true, revisar:!!S.C, informe:!!S.C};
 STEPS.forEach(function(st,i){ o+='<button type="button" class="'+(S.step===st[0]?'on':'')+'" data-go="'+st[0]+'"'+(can[st[0]]?'':' disabled')+(S.step===st[0]?' aria-current="step"':'')+'><span class="n">'+(i+1)+'</span>'+st[1]+'</button>'; });
 $('steps').innerHTML=o;
}
function go(id){ S.step=id; save(); render(); window.scrollTo(0,0); }
function render(){
 nav();
 var V={texto:vTexto, claude:vClaude, revisar:vRevisar, informe:vInforme};
 for(var k in V){ var el=$('v-'+k); el.classList.toggle('on', k===S.step); if(k===S.step) el.innerHTML=V[k](); else el.innerHTML=''; }
}
document.addEventListener('click', function(e){
 var g=e.target.closest('[data-go]'); if(g && !g.disabled){ go(g.getAttribute('data-go')); return; }
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});

/* ------------ examen ------------ */
function exam(){ return EX[S.exam] || null; }
function tasks(){ return S.which==='ambas'?[1,2]:(S.which==='t1'?[1]:[2]); }
function op(){ var e=exam(); return e ? (S.t2op==='2'?e.t2.op2:e.t2.op1) : null; }
function range(n){ return n===1?[60,70]:[70,80]; }
function refHtml(){
 var e=exam(); if(!e) return '<p class="muted">Tarea pegada a mano (ver arriba).</p>';
 var o='<div class="task-ref"><b>Tarea 1.</b> '+esc(e.t1.instr)+'<div class="in">'+e.t1.input.map(esc).join('<br>')+'</div>'+esc(e.t1.lead)+'<ol>'+e.t1.pautas.map(function(p){return '<li>'+esc(p)+'</li>';}).join('')+'</ol>';
 [['1',e.t2.op1],['2',e.t2.op2]].forEach(function(x){ var p=x[1];
  o+='<b>Tarea 2 · Opción '+x[0]+'.</b> '+esc(p.intro);
  if(p.photos) o+='<ul>'+p.photos.map(function(f,i){return '<li>Foto '+(i+1)+': '+esc(f)+'</li>';}).join('')+'</ul>';
  if(p.ficha&&p.ficha.length) o+='<div class="in">'+p.ficha.map(esc).join('<br>')+'</div>';
  if(p.intro2) o+=esc(p.intro2);
  o+='<ol>'+p.pautas.map(function(q){return '<li>'+esc(q)+'</li>';}).join('')+'</ol>'; });
 return o+'</div>';
}
function wcHtml(n){ var w=words(S['t'+n]), r=range(n), ok=w>=r[0]&&w<=r[1]; return '<div class="wc '+(w?(ok?'ok':'no'):'')+'" id="wc'+n+'">'+w+' palabras (recomendadas: '+r[0]+'-'+r[1]+')</div>'; }

/* ------------ paso 1 ------------ */
function vTexto(){
 var o='<h2>1. El texto del estudiante</h2>';
 o+='<div class="card"><h3>Pega lo que te ha enviado</h3><p class="muted small">El texto que sale con el botón «Copiar» de la escritura. El corrector saca el nombre, el examen, la opción y los dos textos.</p><textarea id="pack" class="mono" placeholder="SIMULACRO DELE A2 - UNIDAD 05: ...&#10;EXPRESION ESCRITA&#10;Nombre: ...&#10;&#10;TAREA 1 (64 palabras):&#10;..."></textarea><div class="row"><button class="btn cta" data-act="parse">Leer</button></div><div class="msg" id="pmsg" hidden></div></div>';
 o+='<div class="card"><h3>Datos de la corrección</h3><div class="grid2"><div><label class="f" for="fname">Nombre del estudiante</label><input type="text" id="fname" value="'+esc(S.name)+'"></div>';
 o+='<div><label class="f" for="fexam">Examen</label><select id="fexam">'+D.ex.map(function(e){ return '<option value="'+e.id+'"'+(S.exam===e.id?' selected':'')+'>'+esc(e.nombre)+'</option>'; }).join('')+'<option value="otra"'+(S.exam==='otra'?' selected':'')+'>Otra tarea (pegar las instrucciones)</option></select></div></div>';
 o+='<div class="grid2"><div><label class="f">Qué corriges</label><div class="chips">'+[['ambas','Las dos tareas'],['t1','Solo tarea 1'],['t2','Solo tarea 2']].map(function(x){ return '<label><input type="radio" name="which" value="'+x[0]+'"'+(S.which===x[0]?' checked':'')+'>'+x[1]+'</label>'; }).join('')+'</div></div>';
 o+='<div><label class="f">Opción de la tarea 2</label><div class="chips">'+['1','2'].map(function(x){ return '<label><input type="radio" name="t2op" value="'+x+'"'+(S.t2op===x?' checked':'')+'>Opción '+x+'</label>'; }).join('')+'</div></div></div>';
 if(S.exam==='otra'){
  o+='<label class="f" for="otra1">Instrucciones de la tarea 1 (copia la lámina entera: texto de entrada y pautas)</label><textarea id="otra1">'+esc(S.otra1)+'</textarea>';
  o+='<label class="f" for="otra2">Instrucciones de la tarea 2 (la opción que eligió el estudiante, con fotos o datos y pautas)</label><textarea id="otra2">'+esc(S.otra2)+'</textarea>';
 }
 o+='<div class="grid2"><div><label class="f" for="t1">Texto de la tarea 1</label><textarea id="t1" class="big">'+esc(S.t1)+'</textarea>'+wcHtml(1)+'</div><div><label class="f" for="t2">Texto de la tarea 2</label><textarea id="t2" class="big">'+esc(S.t2)+'</textarea>'+wcHtml(2)+'</div></div>';
 if(exam()) o+='<details><summary>Ver las tareas de este examen</summary>'+refHtml()+'</details>';
 o+='<div class="msg bad" id="tmsg" hidden></div><div class="row"><button class="btn cta" data-act="toClaude">Preparar la petición para Claude</button><button class="btn" data-act="nueva">Empezar una corrección nueva</button></div></div>';
 o+=histHtml();
 return o;
}
function histHtml(){
 if(!H.length) return '';
 var o='<div class="card"><h3>Correcciones guardadas</h3><table class="t hist"><thead><tr><th>Fecha</th><th>Estudiante</th><th>Examen</th><th>Nota</th><th></th></tr></thead><tbody>';
 H.forEach(function(h){ o+='<tr><td>'+esc(h.fecha)+'</td><td>'+esc(h.name||'-')+'</td><td>'+esc(h.examName)+'</td><td>'+esc(h.nota)+'</td><td style="white-space:nowrap"><button class="btn" data-act="hopen" data-id="'+h.id+'">Abrir</button> <button class="btn" data-act="hdel" data-id="'+h.id+'" aria-label="Borrar">&times;</button></td></tr>'; });
 return o+'</tbody></table><p class="muted small">Se guardan en este navegador (las últimas 60).</p></div>';
}
function parsePack(t){
 var r={};
 var m=t.match(/Nombre:\s*(.*)/); if(m && m[1].trim()!=='-') r.name=m[1].trim();
 m=t.match(/UNIDAD\s+(\d+)/i); if(m) r.exam='A2-U'+('0'+parseInt(m[1],10)).slice(-2);
 m=t.match(/MODELO\s+(\d+)/i); if(m) r.exam='A2-M'+parseInt(m[1],10);
 var a=t.search(/TAREA 1[^\n]*\n/), b=t.search(/\nTAREA 2/);
 if(a>-1){ var s=t.slice(a).replace(/^TAREA 1[^\n]*\n/,''); var e=s.search(/\nTAREA 2/); r.t1=(e>-1?s.slice(0,e):s).trim(); }
 if(b>-1){ var s2=t.slice(b+1); m=s2.match(/^TAREA 2,?\s*opci[oó]n\s*(\d|-)/i); if(m && m[1]!=='-') r.t2op=m[1]; r.t2=s2.replace(/^TAREA 2[^\n]*\n/,'').trim(); }
 ['t1','t2'].forEach(function(k){ if(r[k]==='-') r[k]=''; });
 return r;
}

/* ------------ paso 2: peticion ------------ */
function taskBlock(n){
 var e=exam(), r=range(n), L=[];
 if(n===1){
  L.push('TAREA 1 · entre '+r[0]+' y '+r[1]+' palabras');
  if(e){ L.push('Instrucción: '+e.t1.instr); L.push('Texto de entrada:'); e.t1.input.forEach(function(x){ L.push('  '+x); }); L.push(e.t1.lead); e.t1.pautas.forEach(function(p,i){ L.push('  '+(i+1)+'. '+p); }); }
  else L.push(S.otra1);
 } else {
  L.push('TAREA 2 · entre '+r[0]+' y '+r[1]+' palabras · el estudiante eligió la OPCIÓN '+S.t2op);
  if(e){ var p=op(); L.push(p.intro);
   if(p.photos) p.photos.forEach(function(f,i){ L.push('  Foto '+(i+1)+': '+f); });
   if(p.ficha && p.ficha.length){ L.push('  Datos:'); p.ficha.forEach(function(f){ L.push('    '+f); }); }
   if(p.intro2) L.push(p.intro2);
   p.pautas.forEach(function(q,i){ L.push('  '+(i+1)+'. '+q); }); }
  else L.push(S.otra2);
 }
 return L.join('\n');
}
function prompt(){
 var T=tasks(), e=exam(), L=[];
 L.push('Eres examinador/a acreditado/a del DELE A2 del Instituto Cervantes y profesor/a de español para extranjeros. Vas a corregir la prueba de Expresión e interacción escritas de un estudiante adulto con la escala oficial. Tu respuesta la lee un programa: responde SOLO con el bloque JSON del apartado 6, sin texto antes ni después.');
 L.push(''); L.push('## 1. La tarea'+(e?' ('+e.nombre+')':''));
 T.forEach(function(n){ L.push(''); L.push(taskBlock(n)); });
 L.push(''); L.push('## 2. Los textos del estudiante');
 T.forEach(function(n){ var t=S['t'+n]; L.push(''); L.push('TAREA '+n+' ('+words(t)+' palabras):'); L.push('<<<'); L.push(t.trim()||'(en blanco)'); L.push('>>>'); });
 L.push(''); L.push('## 3. Cómo puntuar (escala oficial DELE A2, la misma para las dos tareas)'); L.push(D.rubrica);
 L.push(''); L.push('Reglas: la banda 2 es el nivel A2 (aprobado). Un texto sencillo y comprensible que trata todos los puntos es banda 2 en cumplimiento: no bajes la nota por no usar estructuras de B1. Si falta un punto, como máximo banda 2; si faltan dos o más, banda 1. La extensión fuera del rango solo baja el cumplimiento si es muy corta o si por eso no trata los puntos. Una tarea en blanco tiene 0 en las dos categorías.');
 L.push(''); L.push('## 4. Cómo marcar los errores');
 L.push('- Solo errores reales en el español de España, en estructuras de nivel A2 o inferior. Si algo es correcto aunque tú lo dirías de otra forma, no es un error. Una estructura de nivel superior mal usada se marca, pero se explica con suavidad.');
 L.push('- "original": copia EXACTA del fragmento del texto del estudiante (mismas letras, tildes, mayúsculas y signos), lo más corto posible para que se entienda (de 1 a 5 palabras).');
 L.push('- "correccion": cómo se dice bien ese fragmento.');
 L.push('- "tipo": GR (gramática), LEX (vocabulario), ORT (ortografía, tildes y puntuación), COH (conectores, orden y referencias) o ADE (registro tú/usted, tipo de texto, saludo y despedida).');
 L.push('- "ficha": el código del contenido que tiene que repasar, de esta lista, o "" si ninguno encaja: R01 pasados (perfecto, indefinido, imperfecto) · R02 hay / está / es · R03 ser y estar · R04 concordancia de género y número, posesivos · R05 muy / mucho, también / tampoco · R06 preposiciones (a, en, de, desde... hasta, por / para) · R07 tú y usted · R08 conectores · R09 verbos como gustar · R10 pronombres lo / la / le · R11 planes y futuro (ir a, pensar, querer) · R12 traer / llevar, ir / venir, pedir / preguntar · R13 fórmulas de los correos · R14 vocabulario.');
 L.push('- "explicacion": una frase muy sencilla para el estudiante (nivel A2, de tú) que diga la regla, no solo la corrección.');
 L.push('- "importante": true solo en los 3 errores que más le conviene trabajar en cada tarea (los más básicos o repetidos); en el resto, false.');
 L.push('- Si el mismo error se repite, márcalo cada vez que aparece.');
 L.push(''); L.push('## 5. Qué más devuelves');
 L.push('Para cada tarea:');
 L.push('- "pautas": todas las pautas de la tarea, en el mismo orden y con su texto, con "estado": "si", "parcial" o "no", y un "comentario" breve para el estudiante (dónde la cumple o qué falta).');
 L.push('- "cumplimiento" y "uso": la banda (número entero de 0 a 3).');
 L.push('- "justificacion": una o dos frases para la profesora: por qué das esas bandas.');
 L.push('- "bien": dos cosas concretas que hace bien, citando su texto.');
 L.push('- "prioridad": la UNA cosa más importante que tiene que mejorar.');
 L.push('- "modelo": su texto reescrito como lo haría un buen candidato de A2 (banda 3 sin salir del nivel): las mismas ideas y la misma opción, todas las pautas, entre el mínimo y el máximo de palabras de la tarea, en español de España.');
 L.push('Para toda la prueba, "comentario_global": dos o tres frases positivas y concretas, de tú.');
 L.push('Todo lo que lee el estudiante (comentarios, explicaciones, "bien", "prioridad" y "comentario_global") va en español sencillo de nivel A2, de tú, sin tecnicismos.');
 L.push(''); L.push('## 6. Formato de la respuesta');
 L.push('Solo un bloque de código json con esta estructura. En "tareas" van solo las tareas corregidas: '+T.join(' y ')+'.');
 L.push('```json'); L.push(D.esquema); L.push('```');
 return L.join('\n');
}
function vClaude(){
 var o='<h2>2. Corregir con Claude</h2>';
 o+='<div class="card"><h3>Copia la petición</h3><p>Lleva la escala oficial, las pautas de '+(exam()?esc(exam().nombre):'la tarea')+' y '+(tasks().length>1?'los dos textos':'el texto')+' de '+esc(S.name||'el estudiante')+'. Pégala en un chat nuevo de Claude.</p><div class="row"><button class="btn cta" data-act="copyPrompt">Copiar la petición</button><span class="small" id="cpmsg" role="status"></span></div><details><summary>Ver la petición</summary><textarea class="mono big" readonly>'+esc(prompt())+'</textarea></details></div>';
 o+='<div class="card"><h3>Pega la respuesta de Claude</h3><p class="muted small">Copia la respuesta entera (con el botón de copiar de Claude). Si Claude añade algo de texto, no pasa nada: el corrector busca el bloque de datos.</p><textarea id="resp" class="mono big">'+esc(S.resp)+'</textarea><div class="msg" id="rmsg" hidden></div><div class="row"><button class="btn cta" data-act="readResp">Leer la corrección</button></div></div>';
 return o;
}
function parseResp(t){
 var s=String(t||''), m=s.match(/```(?:json)?\s*([\s\S]*?)```/);
 if(m) s=m[1];
 var a=s.indexOf('{'), b=s.lastIndexOf('}');
 if(a<0||b<a) throw new Error('No encuentro el bloque de datos. Copia la respuesta entera de Claude.');
 s=s.slice(a,b+1).replace(/[“”]/g,'"').replace(/,\s*([}\]])/g,'$1');
 var C; try{ C=JSON.parse(s); }catch(e){ throw new Error('La respuesta está incompleta o mal formada ('+e.message+'). Pide a Claude: «Repite solo el bloque JSON completo».'); }
 if(!C.tareas || !C.tareas.length) throw new Error('La respuesta no trae tareas.');
 C.tareas.forEach(function(k){
  k.tarea=parseInt(k.tarea,10);
  ['cumplimiento','uso'].forEach(function(f){ var v=parseInt(k[f],10); k[f]=isNaN(v)?2:Math.max(0,Math.min(3,v)); });
  k.pautas=(k.pautas||[]).map(function(p){ var st=String(p.estado||'').toLowerCase(); if(st==='sí') st='si'; if(['si','parcial','no'].indexOf(st)<0) st='parcial'; return {pauta:p.pauta||'', estado:st, comentario:p.comentario||''}; });
  k.errores=(k.errores||[]).map(function(x){ var tp=String(x.tipo||'GR').toUpperCase(); return {original:x.original||'', correccion:x.correccion||'', tipo:TIPOS[tp]?tp:'GR', ficha:D.fichas[x.ficha]?x.ficha:'', explicacion:x.explicacion||'', importante:!!x.importante, on:true}; });
  k.bien=k.bien||[]; k.prioridad=k.prioridad||''; k.modelo=k.modelo||''; k.justificacion=k.justificacion||'';
 });
 C.tareas.sort(function(x,y){ return x.tarea-y.tarea; });
 C.comentario_global=C.comentario_global||'';
 return C;
}

/* ------------ paso 3: revisar ------------ */
function tscore(k){ return k.uso*0.66+k.cumplimiento*0.34; }
function score(){
 var ks=S.C.tareas, d=0; ks.forEach(function(k){ d+=tscore(k); }); d=d/ks.length;
 return {directa:d, puntos:d*25/3, parcial:ks.length<2};
}
function bandSel(i,f,v){ var o='<select data-band="'+i+'|'+f+'">'; [3,2,1,0].forEach(function(b){ o+='<option value="'+b+'"'+(v===b?' selected':'')+'>'+b+' · '+BL[b]+'</option>'; }); return o+'</select>'; }
function vRevisar(){
 var C=S.C, sc=score(), o='<h2>3. Revisa la corrección</h2><p class="lead">Cambia lo que no te convenza: las bandas, el estado de las pautas, los errores que salen en el informe y los comentarios.</p>';
 o+=scoreBox(sc);
 C.tareas.forEach(function(k,i){
  var r=range(k.tarea);
  o+='<div class="card"><h3>Tarea '+k.tarea+(k.tarea===2?' · opción '+esc(S.t2op):'')+' <span class="muted small">('+words(S['t'+k.tarea])+' palabras; recomendadas '+r[0]+'-'+r[1]+')</span></h3>';
  o+='<div class="bands"><div><label class="f">Cumplimiento de la tarea (34 %)</label>'+bandSel(i,'cumplimiento',k.cumplimiento)+'</div><div><label class="f">Uso de la lengua (66 %)</label>'+bandSel(i,'uso',k.uso)+'</div></div>';
  if(k.justificacion) o+='<div class="just"><b>Claude:</b> '+esc(k.justificacion)+'</div>';
  o+='<label class="f">Pautas</label><table class="t"><tbody>'+k.pautas.map(function(p,j){ return '<tr><td>'+esc(p.pauta)+'</td><td><select data-pst="'+i+'|'+j+'">'+['si','parcial','no'].map(function(s){ return '<option value="'+s+'"'+(p.estado===s?' selected':'')+'>'+EST[s]+'</option>'; }).join('')+'</select></td><td><input type="text" data-pco="'+i+'|'+j+'" value="'+esc(p.comentario)+'" aria-label="Comentario de la pauta"></td></tr>'; }).join('')+'</tbody></table>';
  o+='<label class="f">Errores ('+k.errores.length+') · marca los 3 importantes y quita los que no quieras en el informe</label><table class="t"><thead><tr><th>Sale</th><th>Imp.</th><th>Error → corrección</th><th>Tipo</th><th>Ficha</th></tr></thead><tbody>';
  k.errores.forEach(function(x,j){ o+='<tr class="'+(x.on?'':'err-off')+'"><td><input type="checkbox" data-eon="'+i+'|'+j+'"'+(x.on?' checked':'')+' aria-label="Incluir"></td><td><input type="checkbox" data-eimp="'+i+'|'+j+'"'+(x.importante?' checked':'')+' aria-label="Importante"></td><td><s>'+esc(x.original)+'</s> → <b>'+esc(x.correccion)+'</b><br><span class="muted small">'+esc(x.explicacion)+'</span></td><td class="mono">'+x.tipo+'</td><td class="mono">'+(x.ficha||'-')+'</td></tr>'; });
  if(!k.errores.length) o+='<tr><td colspan="5" class="muted">Sin errores marcados.</td></tr>';
  o+='</tbody></table>';
  o+='<label class="f" for="prio'+i+'">Lo más importante para mejorar</label><input type="text" id="prio'+i+'" data-prio="'+i+'" value="'+esc(k.prioridad)+'">';
  o+='</div>';
 });
 o+='<div class="card"><label class="f" for="cglob">Comentario general para el estudiante</label><textarea id="cglob">'+esc(C.comentario_global)+'</textarea>';
 o+='<label class="f" for="lect">Aciertos de lectura del mismo examen (opcional: calcula el grupo 1)</label><input type="number" id="lect" min="0" max="25" value="'+esc(S.lect)+'"></div>';
 o+='<div class="row"><button class="btn cta" data-go="informe">Ver el informe</button><button class="btn" data-go="claude">Volver a la respuesta de Claude</button></div>';
 return o;
}
function needL(p){ var n=Math.ceil(30-p-1e-9); return n<=0?0:n; }
function scoreBox(sc){
 var o='<div class="score-box" id="scorebox"><div><b>'+fmt(sc.puntos)+' / 25</b><span>Escritura'+(sc.parcial?' (solo una tarea: orientativo)':'')+'</span></div><div><b>'+fmt(sc.directa)+'</b><span>Puntuación directa (0-3)</span></div>';
 var L=parseInt(S.lect,10);
 if(!isNaN(L)){ var g=L+sc.puntos; o+='<div><b>'+fmt(g)+' / 50</b><span>Grupo 1 · '+(g>=30?'apto':'no apto')+'</span></div>'; }
 else { var n=needL(sc.puntos); o+='<div><b>'+(n>25?'—':n+'/25')+'</b><span>'+(n>25?'No llega a 30 ni con la lectura perfecta':'Aciertos de lectura que necesita para el 30/50')+'</span></div>'; }
 return o+'</div>';
}
document.addEventListener('change', function(e){
 var t=e.target, v;
 if(t.matches('[data-band]')){ v=t.getAttribute('data-band').split('|'); S.C.tareas[+v[0]][v[1]]=parseInt(t.value,10); save(); refreshScore(); }
 else if(t.matches('[data-pst]')){ v=t.getAttribute('data-pst').split('|'); S.C.tareas[+v[0]].pautas[+v[1]].estado=t.value; save(); }
 else if(t.matches('[data-eon]')){ v=t.getAttribute('data-eon').split('|'); S.C.tareas[+v[0]].errores[+v[1]].on=t.checked; t.closest('tr').classList.toggle('err-off',!t.checked); save(); }
 else if(t.matches('[data-eimp]')){ v=t.getAttribute('data-eimp').split('|'); S.C.tareas[+v[0]].errores[+v[1]].importante=t.checked; save(); }
 else if(t.name==='which'||t.name==='t2op'){ S[t.name]=t.value; save(); }
 else if(t.id==='fexam'){ S.exam=t.value; save(); render(); }
});
document.addEventListener('input', function(e){
 var t=e.target, v;
 if(t.id==='fname'){ S.name=t.value; save(); }
 else if(t.id==='t1'||t.id==='t2'){ S[t.id]=t.value; save(); var n=+t.id.charAt(1); $('wc'+n).outerHTML=wcHtml(n); }
 else if(t.id==='otra1'||t.id==='otra2'||t.id==='resp'){ S[t.id]=t.value; save(); }
 else if(t.matches('[data-pco]')){ v=t.getAttribute('data-pco').split('|'); S.C.tareas[+v[0]].pautas[+v[1]].comentario=t.value; save(); }
 else if(t.matches('[data-prio]')){ S.C.tareas[+t.getAttribute('data-prio')].prioridad=t.value; save(); }
 else if(t.id==='cglob'){ S.C.comentario_global=t.value; save(); }
 else if(t.id==='lect'){ S.lect=t.value; save(); refreshScore(); }
});
function refreshScore(){ var b=$('scorebox'); if(b) b.outerHTML=scoreBox(score()); }

/* ------------ paso 4: informe ------------ */
function marked(text, errs){
 var t=String(text||''), used=[], from=0;
 errs.forEach(function(x){
  if(!x.original) return;
  var i=t.indexOf(x.original, from); if(i<0) i=t.indexOf(x.original);
  if(i<0){ var lo=t.toLowerCase(); i=lo.indexOf(x.original.toLowerCase()); }
  if(i<0) return;
  var j=i+x.original.length;
  if(used.some(function(u){ return i<u.b && j>u.a; })) return;
  used.push({a:i,b:j,n:x.n}); from=j;
 });
 used.sort(function(p,q){ return p.a-q.a; });
 var o='', p=0; used.forEach(function(u){ o+=esc(t.slice(p,u.a))+'<mark>'+esc(t.slice(u.a,u.b))+'<sup>'+u.n+'</sup></mark>'; p=u.b; });
 return o+esc(t.slice(p));
}
function onErrs(k){ var n=0; return k.errores.filter(function(x){ return x.on; }).map(function(x){ n++; x.n=n; return x; }); }
function sem(){
 var c={}, pend=false;
 S.C.tareas.forEach(function(k){ onErrs(k).forEach(function(x){ if(x.ficha) c[x.ficha]=(c[x.ficha]||0)+1; }); k.pautas.forEach(function(p){ if(p.estado!=='si') pend=true; }); });
 var rows=Object.keys(c).map(function(f){ return {f:f,n:c[f]}; }).sort(function(a,b){ return b.n-a.n; });
 return {rows:rows, pend:pend};
}
function fichaLink(f){ var x=D.fichas[f]; return D.listas.indexOf(f)>-1 ? '<a href="'+D.base+x[1]+'" target="_blank" rel="noopener">'+esc(x[0])+'</a>' : esc(x[0]); }
function examName(){ return exam()?exam().nombre:'Escritura DELE A2'; }
function vInforme(){
 var C=S.C, sc=score(), sm=sem();
 var o='<div class="row noprint"><button class="btn cta" data-act="pdf">Guardar en PDF</button><button class="btn" data-act="copyRep">Copiar el texto para el correo</button><button class="btn" data-act="saveH">Guardar en el historial</button><button class="btn" data-go="revisar">Volver a revisar</button><span class="small" id="repmsg" role="status"></span></div>';
 o+='<div id="rep"><h2>Corrección de tu escritura</h2><p class="sub">'+esc(S.name||'')+(S.name?' · ':'')+esc(examName())+' · '+new Date().toLocaleDateString('es-ES')+'</p>';
 o+='<div class="big"><div><b>'+fmt(sc.puntos)+' / 25</b><span>Tu nota de escritura'+(sc.parcial?' (solo una tarea)':'')+'</span></div>';
 C.tareas.forEach(function(k){ o+='<div><b>'+k.uso+' · '+k.cumplimiento+'</b><span>Tarea '+k.tarea+': lengua · tarea (de 0 a 3)</span></div>'; });
 o+='</div>';
 var L=parseInt(S.lect,10), n=needL(sc.puntos);
 if(!isNaN(L)) o+='<p>Con tu lectura ('+L+' aciertos), en el <b>grupo 1</b> (lectura + escritura) tienes <b>'+fmt(L+sc.puntos)+' de 50</b>. Necesitas 30: '+(L+sc.puntos>=30?'<b>¡apto!</b>':'<b>todavía no llegas</b>.')+'</p>';
 else if(!sc.parcial) o+='<p>Con esta escritura, en la lectura necesitas <b>'+(n>25?'más de 25 aciertos: la escritura tiene que mejorar':n+' aciertos de 25')+'</b> para llegar a 30 en el grupo 1.</p>';
 o+='<p class="muted small">En cada tarea hay dos notas de 0 a 3: cómo usas la lengua y si haces bien la tarea. El 2 es el nivel A2.</p>';
 if(C.comentario_global) o+='<p>'+esc(C.comentario_global)+'</p>';
 C.tareas.forEach(function(k){
  var r=range(k.tarea), errs=onErrs(k), w=words(S['t'+k.tarea]), imp=errs.filter(function(x){ return x.importante; }).slice(0,3);
  o+='<div class="tk"><h3>Tarea '+k.tarea+(k.tarea===2?' · opción '+esc(S.t2op):'')+'</h3>';
  o+='<p class="small">Palabras: <b>'+w+'</b> (entre '+r[0]+' y '+r[1]+')'+(w<r[0]?' · un poco corto':(w>r[1]?' · un poco largo':' · bien'))+'</p>';
  o+='<h4>Lo que pide la tarea</h4><ul class="pl">'+k.pautas.map(function(p){ return '<li class="'+p.estado+'">'+esc(p.pauta)+' <b>· '+EST[p.estado]+'</b>'+(p.comentario?'<small>'+esc(p.comentario)+'</small>':'')+'</li>'; }).join('')+'</ul>';
  if(k.bien.length) o+='<div class="good"><b>Lo que haces bien</b><ul>'+k.bien.map(function(b){ return '<li>'+esc(b)+'</li>'; }).join('')+'</ul></div>';
  o+='<h4>Tu texto</h4><div class="txt">'+marked(S['t'+k.tarea], errs)+'</div>';
  if(errs.length){ o+='<ul class="el">'+errs.map(function(x){ return '<li><span class="n">'+x.n+'</span><span class="o">'+esc(x.original)+'</span> → <span class="c">'+esc(x.correccion)+'</span><span class="tg">'+TIPOS[x.tipo]+'</span><br><span class="small">'+esc(x.explicacion)+'</span></li>'; }).join('')+'</ul>'; }
  if(imp.length) o+='<div class="imp"><b>Los '+(imp.length===1?'errores':imp.length+' errores')+' más importantes</b><ul>'+imp.map(function(x){ return '<li><b>'+esc(x.original)+' → '+esc(x.correccion)+'.</b> '+esc(x.explicacion)+'</li>'; }).join('')+'</ul></div>';
  if(k.prioridad) o+='<p><b>Para la próxima vez:</b> '+esc(k.prioridad)+'</p>';
  if(k.modelo) o+='<h4>Texto modelo (para comparar, no para copiar)</h4><div class="model">'+esc(k.modelo)+'</div>';
  o+='</div>';
 });
 o+='<div class="tk"><h3>Qué repasar</h3>';
 if(!sm.rows.length && !sm.pend) o+='<p>¡Muy bien! No hay ningún contenido que repasar ahora.</p>';
 else { o+='<table class="sem"><tbody>';
  if(sm.pend) o+='<tr><td><span class="dot r"></span><b>Hacer todos los puntos de la tarea</b></td><td>Antes de escribir, numera los puntos; al final, comprueba que cada uno tiene al menos una frase.</td></tr>';
  sm.rows.forEach(function(x){ o+='<tr><td><span class="dot '+(x.n>=2?'r':'a')+'"></span>'+fichaLink(x.f)+'</td><td>'+x.n+(x.n>1?' errores':' error')+' · '+(x.n>=2?'Prioridad: repásalo antes del próximo examen.':'Casi: repásalo con un ejercicio corto.')+'</td></tr>'; });
  o+='</tbody></table>'; }
 o+='</div><p class="foot">Corrección orientativa con la escala oficial del DELE A2. Material de preparación original, independiente del Instituto Cervantes.</p></div>';
 return o;
}
function repText(){
 var C=S.C, sc=score(), sm=sem(), L=[];
 L.push('CORRECCIÓN DE TU ESCRITURA'); L.push((S.name?S.name+' · ':'')+examName()); L.push('');
 L.push('Nota de escritura: '+fmt(sc.puntos)+' / 25'+(sc.parcial?' (solo una tarea)':''));
 C.tareas.forEach(function(k){ L.push('Tarea '+k.tarea+': uso de la lengua '+k.uso+' · cumplimiento de la tarea '+k.cumplimiento+' (de 0 a 3; el 2 es el nivel A2)'); });
 var Lc=parseInt(S.lect,10); if(!isNaN(Lc)) L.push('Grupo 1 (lectura '+Lc+' + escritura): '+fmt(Lc+sc.puntos)+' / 50 (necesitas 30)');
 if(C.comentario_global){ L.push(''); L.push(C.comentario_global); }
 C.tareas.forEach(function(k){
  var errs=onErrs(k); L.push(''); L.push('— TAREA '+k.tarea+' ('+words(S['t'+k.tarea])+' palabras) —');
  k.pautas.forEach(function(p){ L.push('['+EST[p.estado]+'] '+p.pauta+(p.comentario?' · '+p.comentario:'')); });
  if(k.bien.length){ L.push(''); L.push('Lo que haces bien:'); k.bien.forEach(function(b){ L.push('- '+b); }); }
  if(errs.length){ L.push(''); L.push('Errores:'); errs.forEach(function(x){ L.push(x.n+'. '+x.original+' → '+x.correccion+(x.importante?' (importante)':'')+' · '+x.explicacion); }); }
  if(k.prioridad){ L.push(''); L.push('Para la próxima vez: '+k.prioridad); }
  if(k.modelo){ L.push(''); L.push('Texto modelo (para comparar, no para copiar):'); L.push(k.modelo); }
 });
 if(sm.rows.length||sm.pend){ L.push(''); L.push('QUÉ REPASAR'); if(sm.pend) L.push('- Hacer todos los puntos de la tarea'); sm.rows.forEach(function(x){ var f=D.fichas[x.f]; L.push('- '+f[0]+' ('+x.n+(x.n>1?' errores':' error')+')'+(D.listas.indexOf(x.f)>-1?': '+D.base+f[1]:'')); }); }
 return L.join('\n');
}

/* ------------ acciones ------------ */
function copy(t, ok, bad){
 function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
 if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
}
function msg(id, cls, txt){ var m=$(id); m.hidden=false; m.className='msg '+cls; m.textContent=txt; }
function histSave(){
 var sc=score(), id=S.hid||String(Date.now());
 var e={id:id, fecha:new Date().toLocaleDateString('es-ES'), name:S.name, examName:examName(), nota:fmt(sc.puntos)+'/25', S:JSON.parse(JSON.stringify(S))};
 e.S.hid=id; S.hid=id; save();
 H=H.filter(function(h){ return h.id!==id; }); H.unshift(e); if(H.length>60) H=H.slice(0,60); saveH();
}
var ACTS={
 parse:function(){ var t=$('pack').value; if(!t.trim()){ msg('pmsg','bad','Pega primero el texto.'); return; }
  var r=parsePack(t), got=[];
  if(r.name){ S.name=r.name; got.push('nombre'); }
  if(r.exam){ if(EX[r.exam]){ S.exam=r.exam; got.push('examen'); } else msg('pmsg','amb','El examen '+r.exam+' todavía no está en el corrector: elige «Otra tarea» y pega las instrucciones.'); }
  if(r.t1!=null){ S.t1=r.t1; got.push('tarea 1'); } if(r.t2!=null){ S.t2=r.t2; got.push('tarea 2'); } if(r.t2op){ S.t2op=r.t2op; got.push('opción '+r.t2op); }
  S.which = S.t1.trim() && S.t2.trim() ? 'ambas' : (S.t1.trim() ? 't1' : 't2');
  S.C=null; S.resp=''; S.hid=null; save(); render();
  if(got.length) msg('pmsg','ok','Leído: '+got.join(', ')+'. Comprueba los datos y pulsa «Preparar la petición».'); else msg('pmsg','bad','No he reconocido el formato. Pega los textos a mano en sus casillas.');
 },
 toClaude:function(){ var T=tasks(), err=[];
  T.forEach(function(n){ if(!S['t'+n].trim()) err.push('falta el texto de la tarea '+n); });
  if(S.exam==='otra') T.forEach(function(n){ if(!S['otra'+n].trim()) err.push('faltan las instrucciones de la tarea '+n); });
  if(err.length){ msg('tmsg','bad','No se puede preparar: '+err.join(', ')+'.'); return; }
  go('claude'); },
 copyPrompt:function(){ var s=$('cpmsg'); copy(prompt(), function(){ s.textContent='✓ Copiada. Pégala en un chat nuevo de Claude.'; }, function(){ s.textContent='No se ha podido copiar: ábrela en «Ver la petición» y cópiala a mano.'; }); },
 readResp:function(){ S.resp=$('resp').value; try{ S.C=parseResp(S.resp); save(); go('revisar'); }catch(e){ msg('rmsg','bad',e.message); } },
 pdf:function(){ histSave(); window.print(); },
 copyRep:function(){ var s=$('repmsg'); copy(repText(), function(){ s.textContent='✓ Copiado. Pégalo en el correo al estudiante.'; }, function(){ s.textContent='No se ha podido copiar.'; }); },
 saveH:function(){ histSave(); $('repmsg').textContent='✓ Guardado en el historial.'; },
 nueva:function(){ if(confirm('¿Empezar una corrección nueva? Lo que no hayas guardado en el historial se pierde.')){ S=blank(); save(); render(); } },
 hopen:function(b){ var h=H.filter(function(x){ return x.id===b.getAttribute('data-id'); })[0]; if(h){ S=JSON.parse(JSON.stringify(h.S)); S.step=S.C?'informe':'texto'; save(); render(); window.scrollTo(0,0); } },
 hdel:function(b){ if(!confirm('¿Borrar esta corrección del historial?')) return; H=H.filter(function(x){ return x.id!==b.getAttribute('data-id'); }); saveH(); render(); }
};
if(S.step!=='texto' && S.step!=='claude' && !S.C) S.step='texto';
render();
})();
"""

DATA = {"ex": EXAMENES, "rubrica": RUBRICA, "esquema": ESQUEMA, "base": BASE_URL,
        "fichas": {k: list(v) for k, v in FICHAS.items()}, "listas": FICHAS_LISTAS}
js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page("Corrector de la escritura · DELE A2", CSS_C, BODY, js))
print("ok", FILE, len(EXAMENES), "examenes")
