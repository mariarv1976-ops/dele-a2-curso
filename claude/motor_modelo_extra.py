# -*- coding: utf-8 -*-
# PIEZAS DE LOS MODELOS COMPLETOS DEL CURSO (M1-M8) que se añaden al motor de los simulacros.
# La usa DELE_A2_motor_modelo.py, que se genera con:  python3 adaptar_motor.py
# (adaptar_motor.py copia DELE_A2_motor_simulacro.py y le mete estas piezas con reemplazos comprobados).
# Lo nuevo (solo si los datos traen "modelo": true; con los datos de las unidades, el motor hace lo de siempre):
#  - Resultados: ¿listo para presentarte? con el cálculo 30/50 de cada grupo (lectura + escritura; auditiva + oral),
#    con casillas para la nota de la escritura y de la oral que da la profesora.
#  - Qué repasar: cada contenido enlaza sus fichas de remedio del curso (R01, R02...).
#  - Talleres de escritura y oral recomendados.
#  - Control de progreso estilo CRONO: tiempo por tarea, qué me ha costado, sensación de control 1-10;
#    se compara con los otros modelos hechos en el mismo navegador. Va también en lo que se copia.
#  - Escritura: textos modelo aprobado / excelente (se ven al entregar la escritura).
#  - Oral: notas, pequeño problema y diálogo modelo de la tarea 3 (plegados, para después de la prueba).
#  - 20/10/2026 (M7): al final de Resultados (que solo se abren al entregar lectura, auditiva y escritura), EL PERFIL
#    DEL MODELO Y CÓMO LEER LA NOTA: dificultad de cada prueba frente al examen (+ más difícil, = como el examen,
#    − más fácil; viene de PERFIL en la fuente), tu nota aquí, lo que sería más o menos en el examen real
#    (orientativo: ± 1-2 puntos de 25 en las pruebas que no son "=") y una lectura de los dos grupos. Va también
#    en lo que se copia. Sirve para todos los modelos: si la fuente no trae PERFIL, no sale nada.

CSS_MODELO = r"""
.xnotas{display:flex;flex-wrap:wrap;gap:12px 22px;margin:10px 0 6px}
.xnotas label{display:flex;align-items:center;gap:8px;font-weight:600}
.xnotas input[type=text],.xcr input[type=text]{width:4.6em;padding:6px 8px;text-align:center}
table.xgr{width:100%;border-collapse:collapse;background:#fff;margin:10px 0}
table.xgr td,table.xgr th{padding:9px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
table.xgr th{font-size:.85rem;color:var(--muted);font-weight:600}
.xverd{border-radius:10px;padding:12px 16px;margin:10px 0 18px;font-weight:500}
.xverd.g{background:var(--ok-soft)}.xverd.a{background:var(--amb-soft)}.xverd.r{background:var(--bad-soft)}
.xfichas{margin-top:8px;font-size:.95rem}
.xfichas a,.xtall a{color:var(--ink);font-weight:600}
.xtall{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0 18px}
.xtall ul{margin:6px 0 0;padding-left:1.1em}.xtall li{margin:6px 0;font-size:.95rem}
.xcr{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:12px 0}
.xcr h4{margin:0 0 6px;font-family:Georgia,serif;font-size:1.05rem}
.xcr .xt{display:grid;grid-template-columns:5.5em 1fr;gap:6px 12px;align-items:start;padding:8px 0;border-top:1px dashed var(--line)}
.xcr .xt:first-of-type{border-top:0}
.xchips{display:flex;flex-wrap:wrap;gap:6px}
.xchips label{border:1.5px solid var(--line);border-radius:999px;padding:3px 10px;font-size:.85rem;cursor:pointer;background:#fff}
.xchips label:has(input:checked){background:var(--ink);border-color:var(--ink);color:#fff}
.xchips input{position:absolute;opacity:0;width:1px;height:1px}
.xctrl{display:flex;align-items:center;gap:10px;margin-top:8px;font-weight:600}
.xctrl select{font:inherit;padding:4px 8px;border-radius:8px;border:1.5px solid #CFC6BB}
.mods{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0}
.mods .paper{margin:0;padding:16px 18px;font-size:.98rem}
.mods h5{margin:0 0 6px;font-family:system-ui,sans-serif;font-size:.85rem;letter-spacing:.05em;text-transform:uppercase}
.mods h5.ap{color:var(--ok)}.mods h5.ex{color:var(--coral)}
sup.pn{display:inline-block;background:var(--coral);color:#fff;border-radius:999px;font:700 .68rem/1 system-ui,sans-serif;padding:3px 6px;margin-right:3px;vertical-align:2px}
.mods u{text-decoration-color:var(--coral);text-decoration-thickness:2px;text-underline-offset:3px}
.mods .meta{font-family:system-ui,sans-serif;font-size:.85rem;color:var(--muted);margin-top:8px}
.dlg p{margin:.4em 0;font-family:Georgia,serif}
.dlg .who{display:inline-block;min-width:7.5em;font-family:system-ui,sans-serif;font-size:.85rem;font-weight:700;color:var(--muted)}
.dlg .c .who{color:var(--coral)}
.dlg .prob{background:var(--amb-soft);border-radius:6px;padding:2px 6px}
table.xn{width:100%;border-collapse:collapse;font-size:.95rem;margin:8px 0}
table.xn td{padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}
.xperf{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:16px 20px;margin:22px 0}
.xperf h3{margin-top:0}
.xsym{display:inline-grid;place-items:center;min-width:1.9em;height:1.9em;border-radius:999px;font-weight:700;margin-right:8px;font-family:system-ui,sans-serif}
.xsym.up{background:var(--coral);color:#fff}.xsym.eq{background:#E9E4DD;color:var(--ink)}.xsym.dn{background:var(--ok);color:#fff}
@media (max-width:640px){.xtall,.mods{grid-template-columns:1fr}.xcr .xt{grid-template-columns:1fr}}
"""

JS_MODELO = r"""
/* ---------- modelos del curso: grupos 30/50, fichas, talleres, control de progreso, modelos ---------- */
var PROG_KEY = 'dele_a2_curso_progreso_v1';
var PRUEBAS = [['lectura','Lectura',TL],['auditiva','Auditiva',TA],['escrita','Escritura',45]];
function xNum(v){ var n = parseFloat(String(v==null?'':v).replace(',','.')); return isNaN(n) ? null : Math.max(0, Math.min(25, n)); }
function xFmt(n){ return String(Math.round(n*10)/10).replace('.',','); }
function xMins(p){ var a=S.start&&S.start[p], b=S.fin&&S.fin[p]; return (a&&b&&b>a) ? Math.round((b-a)/60000) : null; }
function xCr(p){ S.crono=S.crono||{}; S.crono[p]=S.crono[p]||{t:{},c:{},s:''}; return S.crono[p]; }
function xGrupos(R){
 if(!D.modelo) return '<p class="muted">Referencia DELE: para el APTO necesitas aproximadamente un 60 % en cada grupo de pruebas.</p>';
 S.notas = S.notas || {};
 var o = '<h3>¿Listo para presentarte?</h3><p class="muted">En el DELE A2 necesitas <b>30 de 50 puntos en cada grupo</b>: lectura + escritura y auditiva + oral. Un grupo muy bueno no compensa el otro. Cada pregunta de lectura y de auditiva vale un punto. Cuando tu profesora te dé la nota de la escritura y de la oral (sobre 25), escríbela aquí.</p>';
 o += '<div class="xnotas noprint"><label>Escritura <input type="text" inputmode="decimal" data-nota="esc" value="'+esc(S.notas.esc||'')+'" aria-label="Nota de la escritura sobre 25"> / 25</label><label>Oral <input type="text" inputmode="decimal" data-nota="oral" value="'+esc(S.notas.oral||'')+'" aria-label="Nota de la oral sobre 25"> / 25</label></div>';
 return o + '<div id="xgr">'+xGruposOut(R)+'</div>';
}
function xGrupoData(R){
 var e = xNum(S.notas&&S.notas.esc), or = xNum(S.notas&&S.notas.oral);
 return [{n:'Grupo 1', p:'Lectura + Escritura', a:R.lec, an:'lectura', b:e, bn:'escritura'},
         {n:'Grupo 2', p:'Auditiva + Oral', a:R.aud, an:'auditiva', b:or, bn:'oral'}];
}
function xGrupoLinea(g){
 if(g.b==null){ var need = 30-g.a;
  if(need<=15) return ['a', 'Con '+g.a+' en la '+g.an+', te basta una '+g.bn+' de '+need+' de 25'+(need<=13?' (menos que un aprobado justo).':' (más o menos, un aprobado).')];
  if(need>25) return ['r', 'Con '+g.a+' en la '+g.an+', ni con un 25 en la '+g.bn+' llegas a 30. Entrena las dos destrezas.'];
  return ['r', 'Con '+g.a+' en la '+g.an+', necesitas '+need+' de 25 en la '+g.bn+': es mucho. Entrena las dos destrezas.'];
 }
 var t = g.a+g.b;
 if(t>=30) return ['g', xFmt(t)+' / 50: APTO en este grupo'+(t<33?', pero justo.':'.')];
 return ['r', xFmt(t)+' / 50: todavía no. Te faltan '+xFmt(30-t)+' puntos.'];
}
function xGruposOut(R){
 var G = xGrupoData(R), o = '<div style="overflow-x:auto"><table class="xgr"><thead><tr><th>Grupo</th><th>Comprensión</th><th>Expresión</th><th>Resultado</th></tr></thead><tbody>';
 G.forEach(function(g){ var l = xGrupoLinea(g);
  o += '<tr><td><b>'+g.n+'</b><br><span class="small muted">'+g.p+'</span></td><td>'+g.a+' / 25</td><td>'+(g.b==null?'<span class="muted">pendiente</span>':xFmt(g.b)+' / 25')+'</td><td><span class="dot '+l[0]+'"></span>'+l[1]+'</td></tr>'; });
 o += '</tbody></table></div>';
 var known = G.filter(function(g){ return g.b!=null; }), v;
 if(known.length===2){
  var t1=G[0].a+G[0].b, t2=G[1].a+G[1].b, mn=Math.min(t1,t2);
  if(mn>=33) v=['g','Sí: con este resultado apruebas el examen con margen. Sigue con los modelos de más nivel.'];
  else if(mn>=30) v=['a','Casi: apruebas, pero justo. Repasa lo que está en rojo en tu grupo más flojo ('+(t1<=t2?'lectura + escritura':'auditiva + oral')+') antes del examen.'];
  else v=['r','Todavía no. Tu grupo más débil es '+(t1<=t2?'el 1 (lectura + escritura)':'el 2 (auditiva + oral)')+': céntrate en él en las próximas semanas.'];
 } else {
  var flojo = G.filter(function(g){ return g.a<15; });
  if(!flojo.length) v=['a','Vas por buen camino: con una escritura y una oral de aprobado (unos 15 de 25) llegas a 30 en los dos grupos. Falta la nota de tu profesora.'];
  else v=['r','Cuidado con la '+flojo.map(function(g){return g.an;}).join(' y la ')+': con menos de 15 de 25, necesitas una '+flojo.map(function(g){return g.bn;}).join(' y una ')+' por encima del aprobado.'];
 }
 return o + '<div class="xverd '+v[0]+'"><b>¿Listo para presentarte?</b> '+v[1]+'</div>';
}
function xFichas(c){
 if(!c.fichas || !c.fichas.length) return '';
 return '<div class="xfichas">Para repasarlo: '+c.fichas.map(function(f){ return '<a href="'+f.u+'" target="_blank" rel="noopener">'+f.t+'</a>'; }).join(' · ')+'</div>';
}
function xPackFichas(L, d){ if(d.fichas && d.fichas.length) L.push('  Fichas: '+d.fichas.map(function(f){ return f.t+' ('+f.u+')'; }).join(' · ')); }
function xTalleres(){
 if(!D.modelo || !D.talleres) return '';
 var g = {}; D.talleres.forEach(function(t){ (g[t.g]=g[t.g]||[]).push(t); });
 var o = '<h3>Para la escritura y la oral</h3><p class="muted">La escritura y la oral las corrige tu profesora. Mientras tanto, estos talleres del curso te ayudan con lo que más cuenta en esas pruebas.</p><div class="xtall">';
 Object.keys(g).forEach(function(k){ o += '<div class="review"><b>'+k+'</b><ul>'+g[k].map(function(t){ return '<li><a href="'+t.u+'" target="_blank" rel="noopener">'+t.t+'</a><br><span class="small muted">'+t.d+'</span></li>'; }).join('')+'</ul></div>'; });
 return o + '</div>';
}
function xCrono(){
 if(!D.modelo || !D.crono) return '';
 xProgSave();
 var o = '<h3>Control de progreso</h3><p class="muted">Apunta cuánto has tardado en cada tarea, qué te ha costado y cuánto control has sentido, del 1 (ninguno) al 10 (todo). Se guarda en este navegador, se compara con los otros modelos y va en lo que copias para tu profesora.</p>';
 PRUEBAS.forEach(function(P){ var p=P[0], cf=D.crono[p]; if(!cf) return; var cr=xCr(p), m=xMins(p);
  o += '<div class="xcr"><h4>'+P[1]+'</h4><div class="small muted">'+(m!=null?'Tiempo total: <b>'+m+' min</b> de '+P[2]+'.':'Tiempo total: entre las '+P[2]+' minutos de la prueba.')+'</div>';
  cf.tareas.forEach(function(tt){ var n=tt[0], rec=tt[1], sel=cr.c[n]||[];
   o += '<div class="xt"><b>Tarea '+n+'</b><div>'+(rec?'<label class="small">Minutos <input type="text" inputmode="numeric" data-crt="'+p+'|'+n+'" value="'+esc(cr.t[n]||'')+'"> <span class="muted">(recomendado: '+rec+')</span></label>':'')+
    '<div class="small muted" style="margin:4px 0">¿Qué me ha costado?</div><div class="xchips">'+cf.costes.map(function(c,i){ return '<label><input type="checkbox" data-crc="'+p+'|'+n+'|'+i+'"'+(sel.indexOf(i)>-1?' checked':'')+'>'+c+'</label>'; }).join('')+'</div></div></div>';
  });
  o += '<div class="xctrl">Sensación de control <select data-crs="'+p+'" aria-label="Sensación de control en '+P[1]+'"><option value="">-</option>'+[1,2,3,4,5,6,7,8,9,10].map(function(i){ return '<option'+(String(cr.s)===String(i)?' selected':'')+'>'+i+'</option>'; }).join('')+'</select> / 10</div></div>';
 });
 return o + '<div id="xprog">'+xProgTabla()+'</div>';
}
function xProgLoad(){ try{ return JSON.parse(localStorage.getItem(PROG_KEY)||'{}')||{}; }catch(e){ return {}; } }
function xProgSave(){
 if(!D.modelo || !allComp()) return;
 var R = results(), st = xProgLoad(), c = function(p){ return (S.crono&&S.crono[p]&&S.crono[p].s)||''; };
 st[D.unit] = {f:new Date().toLocaleDateString('es-ES'), n:D.nombre||D.unit, lec:R.lec, aud:R.aud, esc:S.notas&&S.notas.esc||'', oral:S.notas&&S.notas.oral||'', cl:c('lectura'), ca:c('auditiva'), ce:c('escrita'), tl:xMins('lectura'), ta:xMins('auditiva'), te:xMins('escrita')};
 try{ localStorage.setItem(PROG_KEY, JSON.stringify(st)); }catch(e){}
}
function xProgTabla(){
 var st = xProgLoad(), ks = Object.keys(st).sort();
 if(!ks.length) return '';
 var o = '<h4 style="margin-top:18px">Tus modelos</h4><div style="overflow-x:auto"><table class="xgr"><thead><tr><th>Modelo</th><th>Fecha</th><th>Lectura</th><th>Auditiva</th><th>Escritura</th><th>Oral</th><th>Control L / A / E</th></tr></thead><tbody>';
 ks.forEach(function(k){ var r=st[k]; o += '<tr'+(k===D.unit?' style="font-weight:600"':'')+'><td>'+esc(r.n)+'</td><td>'+esc(r.f)+'</td><td>'+r.lec+'/25'+(r.tl?' <span class="small muted">('+r.tl+' min)</span>':'')+'</td><td>'+r.aud+'/25</td><td>'+(r.esc||'-')+'</td><td>'+(r.oral||'-')+'</td><td>'+(r.cl||'-')+' / '+(r.ca||'-')+' / '+(r.ce||'-')+'</td></tr>'; });
 return o + '</tbody></table></div>';
}
/* ---------- perfil del modelo y cómo leer la nota (solo en Resultados, después de entregar) ---------- */
var XP = [['lectura','Lectura','lec'],['auditiva','Auditiva','aud'],['escrita','Escritura','esc'],['oral','Oral','oral']];
function xSigno(s){ s=String(s||'=').trim(); return s==='+'?1:((s==='-'||s==='−')?-1:0); }
function xPerfNota(R, k){ return k==='lec'?R.lec:(k==='aud'?R.aud:xNum(S.notas&&S.notas[k])); }
function xPerfReal(n, sg){ if(n==null) return null; if(!sg) return 'más o menos lo mismo ('+xFmt(n)+')';
 var a = sg>0 ? [n, Math.min(25, n+2)] : [Math.max(0, n-2), n];
 return (sg>0?'probablemente algo más: ':'probablemente algo menos: ')+'entre '+xFmt(a[0])+' y '+xFmt(a[1]); }
function xLista(a){ return a.length<2 ? a.join('') : a.slice(0,-1).join(', ')+' y '+a[a.length-1]; }
function xPerfil(R){
 var P = D.modelo && D.perfil; if(!P || !P.pruebas) return '';
 var up=[], dn=[], o = '<div class="xperf"><h3>Cómo era este modelo y cómo leer tu nota</h3>';
 o += '<p class="muted">Cada modelo del curso tiene un perfil: algunas pruebas son más difíciles que el examen real y otras, más amables. '+(P.cuando?P.cuando+' ':'')+'Este es su perfil y lo que significa tu nota (orientativo: no es una nota oficial).</p>';
 o += '<div style="overflow-x:auto"><table class="xgr"><thead><tr><th>Prueba</th><th>Este modelo</th><th>Tu nota aquí</th><th>En el examen real</th></tr></thead><tbody>';
 XP.forEach(function(x){ var sg = xSigno(P.pruebas[x[0]]), n = xPerfNota(R, x[2]), cls = sg>0?'up':(sg<0?'dn':'eq');
  if(sg>0) up.push(x[1].toLowerCase()); if(sg<0) dn.push(x[1].toLowerCase());
  var lbl = sg>0?'más difícil que el examen':(sg<0?'más fácil que el examen':'como el examen');
  o += '<tr><td><b>'+x[1]+'</b></td><td><span class="xsym '+cls+'">'+(sg>0?'+':(sg<0?'−':'='))+'</span>'+lbl+'</td><td>'+(n==null?'<span class="muted">pendiente</span>':xFmt(n)+' / 25')+'</td><td>'+(n==null?'<span class="muted">cuando tengas la nota</span>':xPerfReal(n, sg))+'</td></tr>'; });
 o += '</tbody></table></div>';
 var t = [];
 if(up.length) t.push('Este modelo tenía '+xLista(up.map(function(p){ return 'la '+p; }))+' más difícil'+(up.length>1?'es':'')+' que el examen: tu nota real en '+(up.length>1?'esas pruebas':'esa prueba')+' será probablemente algo más alta (uno o dos puntos de 25).');
 if(dn.length) t.push('En cambio, '+xLista(dn.map(function(p){ return 'la '+p; }))+' '+(dn.length>1?'eran':'era')+' más fácil'+(dn.length>1?'es':'')+' que el examen: no te fíes de una nota muy alta ahí.');
 if(!up.length && !dn.length) t.push('Este modelo tenía la dificultad del examen real en todas las pruebas: tu nota de aquí es la mejor pista de tu nota en el examen.');
 var G = xGrupoData(R), gl = [];
 G.forEach(function(g, i){ var sgs = [XP[i][0], XP[i+2][0]].map(function(p){ return xSigno(P.pruebas[p]); }), s = sgs[0]+sgs[1];
  if(g.b==null) return; var tot = g.a+g.b;
  if(tot>=30) gl.push(g.n+' ('+g.p.toLowerCase()+'): '+xFmt(tot)+' / 50'+(s>0?'. Con un modelo así de exigente, es una buena señal.':'.'));
  else if(s>0 && tot>=27) gl.push(g.n+' ('+g.p.toLowerCase()+'): '+xFmt(tot)+' / 50. Te faltan '+xFmt(30-tot)+' puntos, pero este modelo era más duro que el examen en ese grupo: estás muy cerca.');
  else gl.push(g.n+' ('+g.p.toLowerCase()+'): '+xFmt(tot)+' / 50. Te faltan '+xFmt(30-tot)+' puntos: es el grupo que tienes que entrenar.');
 });
 o += '<div class="xverd a">'+t.join(' ')+(gl.length?'<br><br>'+gl.join('<br>'):'<br><br><span class="small">Cuando escribas arriba las notas de la escritura y de la oral, aquí verás también cómo leer cada grupo.</span>')+'</div>';
 if(P.nota) o += '<p class="small">'+P.nota+'</p>';
 return o + '</div>';
}
function xPackPerfil(L, R){
 var P = D.modelo && D.perfil; if(!P || !P.pruebas) return;
 L.push(''); L.push('PERFIL DEL MODELO (frente al examen real):');
 XP.forEach(function(x){ var sg = xSigno(P.pruebas[x[0]]), n = xPerfNota(R, x[2]);
  L.push('- '+x[1]+': '+(sg>0?'+ más difícil':(sg<0?'- más fácil':'= como el examen'))+' | aquí: '+(n==null?'pendiente':xFmt(n)+'/25')+(n==null?'':' | en el real: '+xPerfReal(n, sg))); });
}
function xPackExtra(L, R){
 if(!D.modelo) return;
 L.push(''); L.push('¿LISTO PARA PRESENTARSE? (30 de 50 en cada grupo)');
 xGrupoData(R).forEach(function(g){ L.push('- '+g.n+' ('+g.p+'): '+g.a+' + '+(g.b==null?'?':xFmt(g.b))+' -> '+xGrupoLinea(g)[1]); });
 L.push(''); L.push('CONTROL DE PROGRESO:');
 PRUEBAS.forEach(function(P){ var p=P[0], cf=D.crono&&D.crono[p]; if(!cf) return; var cr=xCr(p), m=xMins(p);
  L.push('- '+P[1]+': '+(m!=null?m+' min de '+P[2]:'tiempo sin datos')+' | control: '+(cr.s||'-')+'/10');
  cf.tareas.forEach(function(tt){ var n=tt[0], sel=(cr.c[n]||[]).map(function(i){ return cf.costes[i]; });
   L.push('  T'+n+': '+(tt[1]?(cr.t[n]?cr.t[n]+' min':'? min')+' (rec. '+tt[1]+')':'')+(sel.length?(tt[1]?' · ':'')+'me ha costado: '+sel.join(', '):(tt[1]?'':'sin marcar'))); });
 });
 xPackPerfil(L, R);
}
function xMods(m){
 function col(cls, lab, x){ return '<div><h5 class="'+cls+'">'+lab+'</h5><div class="paper">'+x.html+'<div class="meta">'+x.pal+' palabras · '+x.lin+'</div></div><p class="small"><b>'+(cls==='ap'?'Por qué aprueba':'Por qué es excelente')+':</b> '+x.porque+'</p>'+(x.mejoras?'<p class="small muted">Mejoras: '+x.mejoras.join(' · ')+'</p>':'')+'</div>'; }
 return '<details><summary>'+m.titulo+'</summary><div class="mods">'+col('ap','Aprobado',m.aprobado)+col('ex','Excelente',m.excelente)+'</div></details>';
}
function xModelosEsc(){
 var M = D.escrita && D.escrita.modelos; if(!M) return '';
 var o = '<h3>Textos modelo</h3><p class="muted">Compáralos con tus textos. El aprobado es sencillo y cumple todas las pautas; el excelente tiene dos o tres mejoras del A2. El número marca la frase de cada pauta y los conectores van subrayados.</p>';
 Object.keys(M).forEach(function(k){ o += xMods(M[k]); });
 return o;
}
function xModelosOral(){
 var M = D.oralModelos && D.oralModelos.t3; if(!M) return '';
 var o = '<h3 class="gap">Después de la prueba: modelos de la tarea 3</h3><p class="muted">Ábrelos solo cuando hayas hecho la prueba con tu profesora.</p>';
 M.forEach(function(m){
  o += '<details><summary>'+m.titulo+' ('+m.trato+')</summary><p><b>Notas modelo (palabras clave, no frases):</b></p><table class="xn"><tbody>'+m.notas.map(function(n){ return '<tr><td><b>'+n[0]+'</b></td><td>'+n[1]+'</td></tr>'; }).join('')+'</tbody></table>';
  o += '<p class="small"><b>El pequeño problema:</b> '+m.problema+'<br><b>Tu segunda opción:</b> '+m.segunda+'</p><div class="dlg">';
  m.dialogo.forEach(function(d){ o += '<p class="'+(d[0]==='C'?'c':'e')+'"><span class="who">'+(d[0]==='C'?'Candidato/a':'Examinador/a')+'</span> '+(d[2]?'<span class="prob">'+d[1]+'</span>':d[1])+'</p>'; });
  o += '</div></details>';
 });
 return o;
}
document.addEventListener('input', function(e){ var t=e.target, a;
 if((a=t.getAttribute('data-nota'))){ S.notas=S.notas||{}; S.notas[a]=t.value; save(); var g=$('xgr'); if(g) g.innerHTML=xGruposOut(results()); var pf=document.querySelector('.xperf'); if(pf) pf.outerHTML=xPerfil(results()); xProgSave(); var pr=$('xprog'); if(pr) pr.innerHTML=xProgTabla(); }
 else if((a=t.getAttribute('data-crt'))){ var q=a.split('|'); xCr(q[0]).t[q[1]]=t.value; save(); }
});
document.addEventListener('change', function(e){ var t=e.target, a;
 if((a=t.getAttribute('data-crc'))){ var q=a.split('|'), c=xCr(q[0]), l=c.c[q[1]]=c.c[q[1]]||[], i=+q[2], k=l.indexOf(i); if(t.checked&&k<0) l.push(i); if(!t.checked&&k>-1) l.splice(k,1); save(); }
 else if((a=t.getAttribute('data-crs'))){ xCr(a).s=t.value; save(); xProgSave(); var pr=$('xprog'); if(pr) pr.innerHTML=xProgTabla(); }
});
"""
