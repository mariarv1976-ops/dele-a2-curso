# -*- coding: utf-8 -*-
# Anade al corrector de la escritura (corrector_escritura.html, todos los niveles) las tareas del curso de
# preparacion DELE A2: modelos completos (M6...), laminas de "Ahora tu" de los talleres de escritura (M3) y de las
# fichas de remedio (R01-R07), el lector de lo que copian esas piezas y los enlaces a las fichas publicadas.
# Uso:  python3 patch_corrector.py corrector_escritura.html  ->  corrector_escritura_curso.html
# Los datos estan en curso_tareas.py. Si el corrector ya lleva el parche, se vuelve a aplicar sobre los datos nuevos.
import json, re, sys
from curso_tareas import NUEVOS, FICHAS, FICHAS_LISTAS

SRC = sys.argv[1] if len(sys.argv) > 1 else "corrector_escritura.html"
DST = sys.argv[2] if len(sys.argv) > 2 else "corrector_escritura_curso.html"
s = open(SRC, encoding="utf-8").read()

def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit("PARADO: el trozo %r aparece %d veces (tenía que aparecer %d)." % (old[:80], n, count))
    s = s.replace(old, new)

def between(a, b, new):
    """Sustituye desde `a` (incluido) hasta `b` (excluido)."""
    global s
    i = s.find(a); j = s.find(b, i + 1)
    if i < 0 or j < 0 or s.count(a) != 1:
        sys.exit("PARADO: no encuentro el bloque que empieza por %r" % a[:60])
    s = s[:i] + new + s[j:]

# ------------------------------------------------------------------ 1. datos
m = re.search(r"^var D = (\{.*\});$", s, re.M)
D = json.loads(m.group(1))
ids = {e["id"] for e in NUEVOS}
D["ex"] = [e for e in D["ex"] if e["id"] not in ids] + NUEVOS
D["fichas"] = FICHAS
D["listas"] = FICHAS_LISTAS
s = s[:m.start(1)] + json.dumps(D, ensure_ascii=True) + s[m.end(1):]

YA = "/* curso-dele-a2 */" in s
if not YA:
    # ------------------------------------------------------------------ 2. estado y ayudas
    rep("breve:false, which:'ambas',", "breve:false, found:[], fsel:'', which:'ambas',")
    rep("function tasks(){ if(unidad()) return [1];",
        "/* curso-dele-a2 */\nfunction isSolo(){ var e=exam(); return !!(e&&e.solo); }\nfunction tasks(){ if(unidad()) return [1]; if(isSolo()) return [exam().solo];")
    rep("function opN(){ return S.t2op==='auto'", "function opN(){ if(isSolo()) return '1'; return S.t2op==='auto'")
    rep("function opTxt(){ var n=opN();", "function opTxt(){ if(isSolo()) return exam().nombre; var n=opN();")
    rep("'Tarea '+k.tarea+(k.tarea===2?' \\u00B7 '+esc(opTxt()):'')",
        "'Tarea '+k.tarea+((k.tarea===2||isSolo())?' \\u00B7 '+esc(opTxt()):'')")

    # ------------------------------------------------------------------ 3. las tareas de referencia (laminas sueltas)
    between("function refHtml(){", "function wcHtml(n){", r"""function lamHtml(p, tit){
 var o='<b>'+tit+'.</b> '+esc(p.intro);
 if(p.photos&&p.photos.length) o+='<ul>'+p.photos.map(function(f,i){return '<li>Foto '+(i+1)+': '+esc(f)+'</li>';}).join('')+'</ul>';
 if(p.ficha&&p.ficha.length) o+='<div class="in">'+p.ficha.map(esc).join('<br>')+'</div>';
 if(p.intro2) o+=esc(p.intro2);
 return o+'<ol>'+p.pautas.map(function(q){return '<li>'+esc(q)+'</li>';}).join('')+'</ol>';
}
function refHtml(){
 var e=exam(); if(!e) return '';
 var o='<div class="task-ref">';
 if(e.t1) o+='<b>Tarea 1.</b> '+esc(e.t1.instr)+(e.t1.input&&e.t1.input.length?'<div class="in">'+e.t1.input.map(esc).join('<br>')+'</div>':'')+esc(e.t1.lead)+'<ol>'+e.t1.pautas.map(function(p){return '<li>'+esc(p)+'</li>';}).join('')+'</ol>';
 if(e.t2.op1) o+=lamHtml(e.t2.op1, e.solo?'Tarea 2':'Tarea 2 · Opción 1');
 if(e.t2.op2) o+=lamHtml(e.t2.op2, 'Tarea 2 · Opción 2');
 return o+'</div>';
}
""")

    # ------------------------------------------------------------------ 4. paso 1: desplegable agrupado, tarea suelta, textos encontrados
    rep("""<label class="f" for="fexam">Examen</label><select id="fexam">'+L.map(function(e){ return '<option value="'+e.id+'"'+(S.exam===e.id?' selected':'')+'>'+esc(e.nombre)+'</option>'; }).join('')+'<option""",
        """<label class="f" for="fexam">Examen o tarea</label><select id="fexam">'+exOpts(L)+'<option""")
    rep("""  o+='<div class="grid2"><div><label class="f">Qu\\u00E9 corriges</label>'+chips('which'""",
        """  if(isSolo()) o+='<p class="muted small" style="margin:8px 0 0">Tarea suelta: la tarea '+exam().solo+' de una l\\u00E1mina del curso. Se corrige con los criterios del DELE '+S.nivel+' y la nota es la de esta tarea.</p>';
  else { o+='<div class="grid2"><div><label class="f">Qu\\u00E9 corriges</label>'+chips('which'""")
    rep("""cu\\u00E1l ha elegido.</p></div></div>';\n""", """cu\\u00E1l ha elegido.</p></div></div>'; }\n""")
    rep("""  o+='<div class="grid2"><div><label class="f" for="t1">Texto de la tarea 1</label>""",
        """  if(isSolo()){ var sn=exam().solo; o+='<label class="f" for="t'+sn+'">Texto del estudiante (tarea '+sn+')</label><textarea id="t'+sn+'" class="big">'+esc(S['t'+sn])+'</textarea>'+wcHtml(sn); }
  else o+='<div class="grid2"><div><label class="f" for="t1">Texto de la tarea 1</label>""")
    rep("""Ver las tareas de este examen</summary>""", """'+(isSolo()?'Ver la l\\u00E1mina':'Ver las tareas de este examen')+'</summary>""")
    rep("""<div class="row"><button class="btn cta" data-act="parse">Leer</button></div><div class="msg" id="pmsg" hidden></div></div>';""",
        """<div class="row"><button class="btn cta" data-act="parse">Leer</button></div><div class="msg" id="pmsg" hidden></div>'+foundHtml()+'</div>';""")
    rep("El corrector saca el nivel, el nombre, el examen, la opci\\u00F3n y los dos textos.",
        "Tambi\\u00E9n lo que copian los talleres de escritura y las fichas de remedio del curso: el corrector busca los textos de \\u00ABAhora t\\u00FA\\u00BB y su l\\u00E1mina.")

    # ------------------------------------------------------------------ 5. paso 2: peticion con lamina suelta
    rep("  L.push('TAREA 1 \\u00B7 entre '+r[0]+' y '+r[1]+' palabras');\n  if(e){ L.push('Instrucci\\u00F3n: '+e.t1.instr); L.push('Texto de entrada:'); e.t1.input.forEach(",
        "  L.push('TAREA 1 \\u00B7 entre '+r[0]+' y '+r[1]+' palabras');\n  if(e){ L.push('Instrucci\\u00F3n: '+e.t1.instr); if(e.t1.input.length) L.push('Texto de entrada:'); e.t1.input.forEach(")
    rep("  var auto=S.t2op==='auto';\n  L.push('TAREA 2 \\u00B7 entre '+r[0]+' y '+r[1]+' palabras \\u00B7 '+(auto?",
        "  var so=!!(e&&e.solo), auto=S.t2op==='auto'&&!so;\n  L.push('TAREA 2 \\u00B7 entre '+r[0]+' y '+r[1]+' palabras \\u00B7 '+(so?'una sola l\\u00E1mina (no hay opciones)':auto?")
    rep("  if(e){ (auto?['1','2']:[S.t2op]).forEach(", "  if(e){ (so?['1']:auto?['1','2']:[S.t2op]).forEach(")
    rep("Solo un bloque de c\\u00F3digo json con esta estructura. En \"tareas\" van solo las tareas corregidas: '+T.join(' y ')+'.'+(S.t2op==='auto'&&T.indexOf(2)>-1?",
        "Solo un bloque de c\\u00F3digo json con esta estructura. En \"tareas\" van solo las tareas corregidas: '+T.join(' y ')+'.'+(S.t2op==='auto'&&T.indexOf(2)>-1&&!isSolo()?")

    # ------------------------------------------------------------------ 6. nota: tarea suelta (sin grupo 1)
    rep("<span>Escritura'+(sc.parcial?' (solo una tarea: orientativo)':'')+'</span>",
        "<span>'+(isSolo()?'Nota de esta tarea':'Escritura'+(sc.parcial?' (solo una tarea: orientativo)':''))+'</span>")
    rep(" var lc=N().lect;\n if(lc){", " var lc=isSolo()?null:N().lect;\n if(lc){")
    rep(" if(!U && N().lect) o+='<label class=\"f\" for=\"lect\">", " if(!U && N().lect && !isSolo()) o+='<label class=\"f\" for=\"lect\">")
    rep("var sc=score(), lc=N().lect, cr=N().crit;", "var sc=score(), lc=isSolo()?null:N().lect, cr=N().crit;")
    rep("<span>Tu nota de escritura'+(sc.parcial?' (solo una tarea)':'')+'</span>",
        "<span>'+(isSolo()?'Tu nota en esta tarea':'Tu nota de escritura'+(sc.parcial?' (solo una tarea)':''))+'</span>", count=2)
    rep("L.push('Nota de escritura: '+fmt(sc.puntos)+' / 25'+(sc.parcial?' (solo una tarea)':''));",
        "L.push((isSolo()?'Nota en esta tarea: ':'Nota de escritura: ')+fmt(sc.puntos)+' / 25'+(sc.parcial&&!isSolo()?' (solo una tarea)':''));", count=2)

    # ------------------------------------------------------------------ 7. leer lo que copia el estudiante
    rep("m=t.match(/MODELO\\s+(\\d+)/i); if(m) r.exam=r.nivel+'-M'+parseInt(m[1],10);",
        "m=t.match(/MODELO\\s+(\\d+)/i); if(m) r.exam=r.nivel+'-M'+('0'+parseInt(m[1],10)).slice(-2);")
    rep(" parse:function(){ var t=$('pack').value; if(!t.trim()){ msg('pmsg','bad','Pega primero el texto.'); return; }\n",
        " parse:function(){ var t=$('pack').value; if(!t.trim()){ msg('pmsg','bad','Pega primero el texto.'); return; }\n"
        "  var fc=parseCurso(t); S.found=fc.items; S.fsel='';\n"
        "  if(fc.items.length){ S.nivel='A2'; S.modo='examen'; if(fc.name) S.name=fc.name; S.C=null; S.resp=''; S.hid=null; save(); render();\n"
        "   msg('pmsg','ok','He encontrado '+fc.items.length+(fc.items.length>1?' textos':' texto')+(fc.pieza?' ('+fc.pieza+')':'')+'. Elige abajo cu\\u00E1l corriges.'); return; }\n"
        "  S.found=[];\n")
    rep(" toClaude:function(){", r""" usar:function(b){ var f=S.found[+b.getAttribute('data-i')], v=b.getAttribute('data-v'); if(!f) return;
  var txt=(v==='ini'?f.ini:f.fin)||'', e=f.lam?EX[f.lam]:null, ta=e?e.solo:f.tarea;
  S.nivel='A2'; S.modo='examen'; S.t1=''; S.t2=''; S.t2det=''; S.lect=''; S.C=null; S.resp=''; S.hid=null;
  S['t'+ta]=txt; S.which=ta===1?'t1':'t2'; S.t2op=ta===2?'1':'auto'; S.fsel=b.getAttribute('data-i')+'|'+v;
  if(e) S.exam=e.id; else { S.exam='otra'; S['otra'+ta]='Texto de «Ahora tú» ('+f.name+'). No tengo la lámina: pega aquí las instrucciones y las pautas.'; }
  save(); render();
  msg('pmsg', e?'ok':'amb', e?'Listo: '+f.name+' · lámina «'+e.nombre+'». Comprueba el texto y pulsa «Preparar la petición».':'No reconozco la lámina de «'+f.name+'»: pega las instrucciones en la casilla de la tarea '+ta+'.');
 },
 toClaude:function(){""")

    CODE = r"""
/* ------------ curso DELE A2: modelos, talleres y fichas ------------ */
var GRUPOS=[['','Simulacros por unidad'],['Modelos completos','Modelos completos del curso'],['Taller de escritura','Taller de escritura · Ahora tú'],['Fichas de remedio','Fichas de remedio · Ahora tú']];
function exOpts(L){
 var o='';
 GRUPOS.forEach(function(g){ var es=L.filter(function(e){ return (e.pz||'')===g[0]; }); if(!es.length) return;
  o+='<optgroup label="'+esc(g[1])+'">'+es.map(function(e){ return '<option value="'+e.id+'"'+(S.exam===e.id?' selected':'')+'>'+esc(e.nombre)+'</option>'; }).join('')+'</optgroup>'; });
 var otros=L.filter(function(e){ return !GRUPOS.some(function(g){ return (e.pz||'')===g[0]; }); });
 return o+otros.map(function(e){ return '<option value="'+e.id+'"'+(S.exam===e.id?' selected':'')+'>'+esc(e.nombre)+'</option>'; }).join('');
}
function normN(s){ return String(s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[«»"]/g,'').replace(/\s+/g,' ').trim(); }
function lamPautas(e){ return e.solo===1?e.t1.pautas:e.t2.op1.pautas; }
function lamByName(name){
 var n=normN(name), best=null, bl=0;
 D.ex.forEach(function(e){ (e.keys||[]).forEach(function(k){ var kk=normN(k); if(kk && n.indexOf(kk)>-1 && kk.length>bl){ best=e; bl=kk.length; } }); });
 return best;
}
function lamByText(txt){
 var n=normN(txt), best=null, bs=0;
 D.ex.forEach(function(e){ if(!e.solo) return; var sc=0;
  lamPautas(e).forEach(function(p){ var q=normN(p).replace(/[;.]$/,''); if(q.length>10 && n.indexOf(q)>-1) sc++; });
  var ins=normN(e.solo===1?e.t1.instr:e.t2.op1.intro); if(ins.length>20 && n.indexOf(ins)>-1) sc+=3;
  if(sc>bs){ bs=sc; best=e; } });
 return bs>=2?best:null;
}
function cleanTxt(a){ while(a.length && !a[0].trim()) a.shift(); while(a.length && !a[a.length-1].trim()) a.pop(); var t=a.join('\n').trim(); return /^\(sin texto/.test(t)?'':t; }
function bodyParts(body){
 var ia=-1, id=-1, kind='rev';
 body.forEach(function(l,i){ var x=l.trim(); if(/^ANTES( \(aprobado\))?:$/i.test(x)) ia=i; if(/^DESPU[EÉ]S( \(excelente\))?:$/i.test(x)) id=i; if(/aprobado\):$/i.test(x)) kind='mod'; });
 if(ia>-1 && id>ia) return {ini:cleanTxt(body.slice(ia+1,id)), fin:cleanTxt(body.slice(id+1)), kind:kind, head:body.slice(0,ia).join('\n')};
 var dash=[]; body.forEach(function(l,i){ if(/^-{3,}\s*$/.test(l.trim())) dash.push(i); });
 if(dash.length>=2) return {fin:cleanTxt(body.slice(dash[0]+1,dash[1])), head:body.slice(0,dash[0]).join('\n')};
 var b=body.findIndex(function(l){ return !l.trim(); });
 return {fin:cleanTxt(b>-1?body.slice(b+1):body), head:(b>-1?body.slice(0,b):[]).join('\n')};
}
function parseCurso(t){
 var lines=String(t).replace(/\r/g,'').split('\n'), items=[], out={items:items, name:'', pieza:''};
 var first=lines.filter(function(l){ return l.trim(); })[0]||'', hd=normN(first);
 if(!/^curso dele/.test(hd) && !/^==|^escritura\s*-/m.test(t)) return out;
 out.pieza=first.replace(/^CURSO DELE A2\s*-\s*/i,'').replace(/^ESCRITURA:\s*/i,'').trim();
 var nm=t.match(/Nombre:\s*(.*)/); if(nm && nm[1].trim()!=='-') out.name=nm[1].trim();
 var pre=/kit de frases/.test(hd)?'Kit de frases · ':(/las pautas como lista/.test(hd)?'Las pautas · ':'');
 var END=/^(==\s|OPINI[OÓ]N\b|ESCRITURA\s*-\s|MIS TEXTOS|MIS REVISIONES)/i;
 for(var i=0;i<lines.length;i++){
  var L=lines[i], mb=L.match(/^==\s*(.+?)\s*==\s*$/), me=L.match(/^ESCRITURA\s*-\s*(.+)$/i);
  if(!mb && !me) continue;
  var j=i+1, body=[]; while(j<lines.length && !END.test(lines[j])){ body.push(lines[j]); j++; }
  var p=bodyParts(body), it;
  if(mb){
   var raw=mb[1], name=raw.replace(/^\d+\.\s*/,'').replace(/\s*\((tarea\s*\d|\d{4}-\d\d-\d\d)\)\s*$/i,'').trim(), tm=raw.match(/\(tarea\s*(\d)\)/i);
   var full=(pre && name.indexOf(pre)!==0?pre:'')+name, lam=lamByName(full)||lamByText(p.head);
   it={name:full, lam:lam?lam.id:'', tarea:lam?lam.solo:(tm?+tm[1]:(/correo/i.test(name)?1:2)), fin:p.fin, ini:p.ini||'', kind:p.kind||''};
  } else {
   var lamE=lamByText(L+'\n'+p.head), tt=L.match(/TAREA\s*(\d)/i);
   it={name:'Ficha · '+me[1].replace(/\s*\(\d+-\d+ palabras\)\s*$/i,'').trim(), lam:lamE?lamE.id:'', tarea:lamE?lamE.solo:(tt?+tt[1]:1), fin:p.fin, ini:'', kind:''};
  }
  if(it.fin || it.ini) items.push(it);
  i=j-1;
 }
 return out;
}
function foundHtml(){
 if(!S.found || !S.found.length) return '';
 var o='<div class="found"><p class="small" style="margin:12px 0 4px"><b>Textos encontrados</b> · elige cuál corriges (uno cada vez):</p>';
 S.found.forEach(function(f,i){ var e=f.lam?EX[f.lam]:null, lf=f.kind==='mod'?'el excelente':'la versión revisada', li=f.kind==='mod'?'el aprobado':'la primera versión';
  var on=S.fsel && S.fsel.split('|')[0]===String(i);
  o+='<div class="fitem'+(on?' on':'')+'"><div><b>'+esc(f.name)+'</b> <span class="muted small">· tarea '+f.tarea+' · '+words(f.fin||f.ini)+' palabras'+(f.ini?' ('+(f.kind==='mod'?'excelente':'revisada')+') / '+words(f.ini)+' ('+(f.kind==='mod'?'aprobado':'primera versión')+')':'')+'</span><br>'+
   '<span class="small">'+(e?'Lámina: '+esc(e.nombre):'<span style="color:#7A4E0E">Lámina no reconocida: tendrás que pegar las instrucciones</span>')+'</span>'+
   '<div class="small muted">'+esc(String(f.fin||f.ini).slice(0,140))+'…</div></div>'+
   '<div class="row" style="margin:6px 0 0">'+(f.fin?'<button class="btn sm cta" data-act="usar" data-i="'+i+'" data-v="fin">Corregir '+(f.ini?lf:'este texto')+'</button>':'')+(f.ini?'<button class="btn sm" data-act="usar" data-i="'+i+'" data-v="ini">Corregir '+li+'</button>':'')+'</div></div>'; });
 return o+'</div>';
}
"""
    rep("/* ------------ paso 2: peticion ------------ */", CODE + "\n/* ------------ paso 2: peticion ------------ */")

    # ------------------------------------------------------------------ 8. estilos
    rep("</style>", ".fitem{border:1.5px solid var(--line);border-radius:10px;padding:10px 14px;margin:8px 0;background:#fff}\n.fitem.on{border-color:var(--ok);background:var(--ok-soft)}\noptgroup{font-style:normal;font-weight:700}\n</style>")

# ------------------------------------------------------------------ 9. todo en ASCII (como el resto de ejecutables)
def enc_script(js):
    out = []
    for c in js:
        o = ord(c)
        if o < 128: out.append(c)
        elif o <= 0xFFFF: out.append("\\u%04X" % o)
        else:
            o -= 0x10000; out.append("\\u%04X\\u%04X" % (0xD800 + (o >> 10), 0xDC00 + (o & 0x3FF)))
    return "".join(out)
a = s.index("<script>"); b = s.index("</script>")
s = s[:a] + enc_script(s[a:b]) + s[b:]
s = "".join(c if ord(c) < 128 else "&#x%X;" % ord(c) for c in s)
open(DST, "w", encoding="ascii").write(s)
print("ok", DST, "·", len(D["ex"]), "tareas ·", len(NUEVOS), "del curso · fichas enlazadas:", ", ".join(FICHAS_LISTAS))
