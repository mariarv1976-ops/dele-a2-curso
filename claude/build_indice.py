# -*- coding: utf-8 -*-
# INDICE DEL CURSO DE PREPARACION DELE A2 (solo para la profesora)
# Uso: python3 build_indice.py -> DELEA2_curso_indice.html
# Subir a la carpeta protegida biblioteca/profesora/ (no se enlaza desde ningun sitio).
# NO HACE FALTA REGENERARLO CADA VEZ: al abrirse en la web, el indice comprueba que piezas estan subidas
# (si el archivo existe en el servidor, la pieza sale activa con sus botones; si no, sale en gris).
# Solo hay que regenerarlo si cambia la lista de piezas (una pieza nueva, OTRO NOMBRE DE ARCHIVO).
# OJO: el nombre de archivo de cada pieza tiene que ser EXACTAMENTE el que escribe su build (FILE = ...).
# Si no coincide, el indice no la encuentra en la web aunque este subida (paso con R04 y R05, 14/10, y con
# los modelos completos, 22/10: el indice buscaba DELEA2_curso_M2_modeloN.html y el motor escribe
# DELEA2_curso_M0N_examen.html y DELEA2_curso_M0N_oral_profesora.html).
# El estado "listo" de PIEZAS solo se usa si el indice se abre desde el ordenador (sin servidor).
import json
from curso_comun import CSS, BASE_URL, page

FILE = "DELEA2_curso_indice.html"
PROF_URL = "https://2spanishteachers.com/biblioteca/profesora/"

MODULOS = [
 ("M0", "Módulo 0 · Conoce el examen"),
 ("M1", "Módulo 1 · Entrenador por tareas"),
 ("M2", "Módulo 2 · Modelos completos"),
 ("M3", "Módulo 3 · Taller de escritura"),
 ("M4", "Módulo 4 · Taller de oral"),
 ("M5", "Módulo 5 · Fichas de remedio"),
 ("PR", "Herramientas de la profesora"),
]

# (modulo, codigo, titulo, descripcion, archivo, estado, piloto, paso de produccion)
# estado: listo | en curso | pendiente · paso = orden de produccion del plan (apartado 7)
P = []
def add(m, c, t, d, f, st="pendiente", pil=False, paso=0, prof=False):
    P.append({"m": m, "c": c, "t": t, "d": d, "f": f, "st": st, "pil": pil, "paso": paso, "prof": prof})

add("M0", "M0", "Conoce el examen", "Las 4 pruebas y las 13 tareas, la regla del 30/50 con calculadora, el día del examen y la hoja de respuestas, las 10 reglas de oro, test de verdadero o falso y opinión.", "DELEA2_curso_M0_conoce_el_examen.html", "listo", True, 2)

TAREAS = [
 ("CL1", "Lectura · Tarea 1", "Correo o mensaje personal · ítems 1-5"),
 ("CL2", "Lectura · Tarea 2", "Ocho anuncios y textos breves · ítems 6-13"),
 ("CL3", "Lectura · Tarea 3", "Tres personas, un tema: relacionar · ítems 14-19"),
 ("CL4", "Lectura · Tarea 4", "Texto largo (blog, biografía, noticia) · ítems 20-25"),
 ("CA1", "Auditiva · Tarea 1", "Seis conversaciones con imágenes · ítems 1-6"),
 ("CA2", "Auditiva · Tarea 2", "Anuncios y noticias de radio · ítems 7-12"),
 ("CA3", "Auditiva · Tarea 3", "Conversación entre amigos: él, ella o ninguno · ítems 13-18"),
 ("CA4", "Auditiva · Tarea 4", "Ocho mensajes, once enunciados · ítems 19-25"),
 ("EIE1", "Escritura · Tarea 1", "Responder a un correo (60-70 palabras): pautas y fórmulas"),
 ("EIE2", "Escritura · Tarea 2", "Opción 1 vida personal / opción 2 fotos o datos (70-80 palabras)"),
 ("EIO1", "Oral · Tarea 1", "Monólogo: los tres tiempos y el esquema de palabras clave"),
 ("EIO2", "Oral · Tarea 2", "Descripción de la foto: las 6 preguntas en orden"),
 ("EIO3", "Oral · Tarea 3", "Diálogo con un amigo o un familiar: planificar y contar"),
]
for c, t, d in TAREAS:
    add("M1", "M1-" + c, t, d + ". Así es la tarea, estrategia, trampas (ES-01 a ES-11) y práctica con los ítems de los simulacros de unidad.",
        "DELEA2_curso_M1_%s.html" % c, paso=7)

# MODELOS COMPLETOS. Archivos: los que escribe el motor (DELE_A2_motor_modelo.py):
#   DELEA2_curso_M0N_examen.html (dele-curso/) y DELEA2_curso_M0N_oral_profesora.html (profesora/).
# Perfil: lectura / auditiva / escritura / oral (− parte fácil del examen · = como el examen · + parte alta).
MODELOS = [
 ("1", "de entrada · = − = −", "listo", True,
  "Carlos, profesor de música en Logroño · unas vacaciones diferentes · Sandra, árbitra · salud. Oral: mi familia / las estaciones. Código de la oral A2-M01."),
 ("2", "+ = − =", "pendiente", True,
  "Por hacer. Lectura más exigente; escritura amable. Oral (de tú): clases para adultos / elegir restaurante."),
 ("3", "= + = =", "pendiente", False, "Por hacer. La auditiva aprieta."),
 ("4", "− = + +", "pendiente", False, "Por hacer. Escritura y oral exigentes (pautas densas, tarea 3 larga)."),
 ("5", "termómetro · = = = =", "pendiente", False, "Por hacer. Examen calibrado: el que mejor predice la nota."),
 ("6", "como el examen · = + = =", "listo", False,
  "Tango, el perro adoptado · voluntariado · el bibliobús · redes y reloj inteligente · Pablo viene de visita · Bruno en la heladería. Oral: preparar un viaje a la montaña / pintar la casa. Código A2-M06."),
 ("7", "nivel alto · + + + =", "listo", False,
  "El más exigente, para 2-3 semanas antes del examen. Escritura con la biografía de Encarna. Oral: buscar piso de alquiler con una amiga / el huerto urbano. Código A2-M07."),
 ("8", "ensayo general · = = = =", "pendiente", False, "Por hacer. Condiciones reales, la última semana."),
]
for n, dif, st, pil, d in MODELOS:
    add("M2", "M2-%s" % n, "Modelo completo %s (%s)" % (n, dif),
        d + " Con informe de repaso, grupos 30/50, perfil del modelo, control de progreso y modelos de respuesta.",
        "DELEA2_curso_M%02d_examen.html" % int(n), st, pil=pil, paso=6)

add("M3", "M3-1", "Kit de frases por tipo de texto", "Correo informal (saludar, agradecer, disculparse, invitar, aceptar, rechazar, proponer, despedirse), correo formal de usted, blog o diario, biografía, texto a partir de fotos. Textos modelo marcados, dos trampas (tú/usted y conectores), ejercicios y «Ahora tú».", "DELEA2_curso_M3_kit_frases.html", "listo", paso=4)
add("M3", "M3-2", "Las pautas como lista de control", "Cada pauta, al menos una frase: leer una pauta y sus piezas, la mini lista de 1 minuto, ¿qué falta? en 8 textos de estudiantes y «Ahora tú» con revisión pieza por pieza.", "DELEA2_curso_M3_pautas.html", "listo", paso=4)
add("M3", "M3-3", "De la banda 1 a la banda 2", "La operación rescate en 5 pasos: textos con los fallos típicos para diagnosticar, corregir y llevar a la banda 2.", "DELEA2_curso_M3_banda1_a_banda2.html", "listo", paso=4)
add("M3", "M3-4", "Revisión final de 5 minutos", "La lista fija de 8 pasadas (pautas, tú/usted, pasados, hay/está/es, concordancias, muy/mucho, conectores, líneas a ojo), caza por pasadas, a contrarreloj y «Ahora tú» con cronómetro.", "DELEA2_curso_M3_revision_final.html", "listo", paso=4)
add("M3", "M3-5", "Textos modelo: aprobado y excelente", "Las bandas en sencillo, textos aprobado y excelente lado a lado para 5 tipos, las 6 mejoras, ¿aprueba? con 6 textos de estudiantes y «Ahora tú».", "DELEA2_curso_M3_textos_modelo.html", "listo", paso=4)

add("M4", "M4-1", "Tarea 1: banco de temas", "20 temas (9 de las láminas oficiales y 11 frecuentes) con lámina original, notas modelo en palabras clave y monólogo modelo con los verbos marcados por tiempo. Los cuatro tiempos y el ejercicio «¿Qué tiempo pide?», preparación de 4 minutos con el esquema de cinco casillas, modo guiado pauta a pauta, modo examen con reloj, dos temas al azar como en el examen y grabación opcional (banco_temas_T1.py).", "DELEA2_curso_M4_T1_temas.html", "listo", paso=3)
add("M4", "M4-2", "Tarea 2: plantilla universal de la foto", "Las 6 preguntas + frases comodín y la regla de las tres frases. Modo guiado con ritmo (cada pregunta con su tiempo), modo examen con reloj, grabación opcional en el navegador, preparación de 4 minutos con el esquema de las seis casillas y descripción y notas modelo. 12 fotos: 6 como en el examen y 6 de entrenamiento (banco_fotos_T2.py).", "DELEA2_curso_M4_T2_foto.html", "listo", pil=True, paso=3)
add("M4", "M4-3", "Tarea 3: diálogos", "12 situaciones (6 de planificar con tú y 6 de servicio con usted) con lámina, notas modelo, el pequeño problema y diálogo modelo turno a turno. Frases por función, preparación de 2 minutos, modo guiado y modo examen con reloj.", "DELEA2_curso_M4_T3_dialogos.html", "listo", paso=3)
add("M4", "M4-4", "Qué hacer si me bloqueo", "Seis situaciones de bloqueo con frases de rescate (tú/usted), ¿Qué dices?, describe la palabra, entrenador con medidor de silencios y «Ahora tú» con las láminas de las tres tareas.", "DELEA2_curso_M4_bloqueo.html", "listo", paso=3)
add("M4", "M4-5", "Dosier oral A2 de estructuras", "La prueba por dentro, los 12 minutos de preparación, las tres tareas con frases y modelos, si me bloqueo, 9 ejercicios con corrección y tarjeta de bolsillo. También en PDF (DELEA2_dosier_oral_estructuras.pdf).", "DELEA2_curso_M4_dosier_oral.html", "listo", paso=3)

# Fichas de remedio: (codigo, titulo, piloto, archivo exacto o None, descripcion o None)
FICHAS = [
 ("R01", "Pasados: perfecto, indefinido e imperfecto", True, "DELEA2_curso_R01_pasados.html",
  "Desde dentro / desde fuera / la ventana de ahora, preguntas en pasado, textos del examen con huecos, detector de pasados en la escritura y preguntas orales en cadena."),
 ("R02", "Hay / está / es", True, "DELEA2_curso_R02_hay_esta_es.html",
  "Presenta / sitúa / evento, errores típicos, textos con huecos, detector en la escritura y describir una foto (qué hay y dónde está)."),
 ("R03", "Ser y estar", False, None, None),
 ("R04", "Concordancia y posesivos", False, "DELEA2_curso_R04_concordancia_posesivos.html",
  "El nombre manda (el capitán y su camiseta), el posesivo mira a la cosa, errores típicos, textos con huecos, detector en la escritura y describir a las personas de una foto."),
 ("R05", "Muy / mucho · también / tampoco", False, "DELEA2_curso_R05_muy_mucho_tambien_tampoco.html",
  "Muy = el volumen, mucho = la cantidad, también/tampoco = el eco (yo o a mí), errores típicos, textos con huecos, detector en la escritura, reacciona al examinador con reloj y la foto con muy y mucho."),
 ("R06", "Preposiciones frecuentes y por / para básico", False, "DELEA2_curso_R06_preposiciones.html",
  "El mapa del viaje: a, en, de... a, desde... hasta, por y para; hace / desde hace / durante; errores típicos, textos con huecos, detector en la escritura y práctica oral con reloj."),
 ("R07", "Tú y usted: registro coherente", True, "DELEA2_curso_R07_tu_usted.html",
  "La distancia y el carril: usted habla como él/ella, del saludo a la despedida en el mismo carril; textos con huecos, detector de mezcla en la escritura y la misma petición dos veces en la oral."),
 ("R08", "Conectores para enlazar", False, None, None),
 ("R09", "Verbos como gustar", False, None, None),
 ("R10", "Pronombres lo / la / le", False, None, None),
 ("R11", "Planes y futuro", False, None, None),
 ("R12", "Traer / llevar · ir / venir · pedir / preguntar", False, None, None),
 ("R13", "Fórmulas de los correos", False, None, None),
 ("R14", "Vocabulario por áreas", False, None, None),
]
SLUG = {"R03": "ser_estar", "R08": "conectores", "R09": "gustar", "R10": "pronombres",
        "R11": "futuro", "R12": "traer_llevar", "R13": "formulas_correo", "R14": "vocabulario"}
for c, t, pil, f, d in FICHAS:
    add("M5", c, t, d or "Teoría breve + práctica. El informe de repaso enlaza aquí.",
        f or "DELEA2_curso_%s_%s.html" % (c, SLUG[c]), "listo" if f else "pendiente", pil=pil, paso=5)
ESTR = [("E01", "La trampa literal", "trampa_literal"), ("E02", "El cambio de plan", "cambio_plan"),
        ("E03", "Quién dice qué", "quien_dice_que"), ("E04", "Condiciones y negaciones", "condiciones_negaciones")]
for c, t, s in ESTR:
    add("M5", c, "Estrategia: " + t, "Ficha de estrategia ligada a las etiquetas ES del informe.", "DELEA2_curso_%s_%s.html" % (c, s), paso=5)

add("PR", "PR-1", "Corrector de la escritura", "Prepara la petición para Claude con la rúbrica y las pautas de cada tarea y genera el informe del estudiante en PDF.", "DELEA2_corrector_escritura.html", "listo", paso=2, prof=True)
# Una libreta oral por modelo completo (la escribe el motor junto con el examen)
for n, dif, st, pil, d in MODELOS:
    add("PR", "PR-M%s" % n, "Libreta oral del modelo %s" % n,
        "Código de la oral A2-M%02d, guion del entrevistador con el esquema de la tarea 3, diálogos modelo y plantilla de evaluación." % int(n),
        "DELEA2_curso_M%02d_oral_profesora.html" % int(n), st, paso=6, prof=True)

# Comprobacion: ningun archivo repetido
_fs = [p["f"] for p in P]
assert len(_fs) == len(set(_fs)), "archivo repetido en el indice"

CSS_IDX = CSS + r"""
.wrap{max-width:980px}
.top-in{max-width:980px;padding-bottom:14px}
.stats{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}
.stats div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 16px}
.stats b{font-family:Georgia,serif;font-size:1.5rem;display:block;line-height:1.1}
.stats span{font-size:.85rem;color:var(--muted)}
.bar{height:8px;background:var(--line);border-radius:99px;overflow:hidden;margin-top:6px;width:160px}
.bar i{display:block;height:100%;background:var(--coral)}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
.filters button{font:inherit;font-size:.9rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.filters button.on{background:var(--ink);border-color:var(--ink);color:#fff}
#q{font:inherit;border:1.5px solid #CFC6BB;border-radius:999px;padding:8px 16px;width:100%;max-width:340px;background:#fff}
h2.mod{margin-top:30px;padding-bottom:6px;border-bottom:2px solid var(--coral);font-size:1.25rem}
.it{display:grid;grid-template-columns:5.2em 1fr auto;gap:14px;align-items:start;background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:8px 0}
.it .code{font-family:'SF Mono',Consolas,monospace;font-weight:700;font-size:.9rem;color:var(--coral)}
.it h3{margin:0 0 2px;font-size:1.05rem}
.it p{margin:0;font-size:.93rem;color:var(--muted)}
.it .file{font-family:'SF Mono',Consolas,monospace;font-size:.78rem;color:var(--muted);margin-top:4px;word-break:break-all}
.it .acts{display:flex;flex-direction:column;gap:6px;align-items:flex-end;min-width:9.5em}
.badge{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:2px 10px;letter-spacing:.03em}
.b-listo{background:var(--ok-soft);color:var(--ok)}.b-curso{background:var(--amb-soft);color:#7A4E0E}.b-pend{background:#EFEAE4;color:var(--muted)}
.b-pil{background:var(--coral-soft);color:#9C3A1E;margin-left:4px}
.b-prof{background:#E6E8F2;color:#2B3270;margin-left:4px}
.it.off{opacity:.78}
.cp-ok{font-size:.8rem;color:var(--ok);font-weight:600}
.b-check{background:#EFEAE4;color:var(--muted)}
.chkmsg{font-size:.85rem;color:var(--muted);margin:4px 0 0}
@media (max-width:700px){.it{grid-template-columns:1fr}.it .acts{flex-direction:row;align-items:center;min-width:0}}
"""

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">Curso de preparación DELE A2 · Índice</h1><small>Solo para la profesora · los estudiantes reciben el enlace directo de cada parte</small></div>
</div></header>
<main class="wrap">
 <div class="stats" id="stats"></div>
 <p class="chkmsg" id="chkmsg"></p>
 <div class="filters" id="filters"></div>
 <input type="search" id="q" placeholder="Buscar (pasados, foto, modelo 3...)" aria-label="Buscar en el índice">
 <div id="list"></div>
 <footer class="legal">Carpeta del curso: <span class="mono">__BASE__</span> · Herramientas: <span class="mono">__PROF__</span></footer>
</main>
"""

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
var F = 'todo', Q = '', LIVE = /^https?:$/.test(location.protocol), CHECKING = LIVE;
try{ F = localStorage.getItem('dele-a2-indice-filtro') || 'todo'; }catch(e){}
function url(p){ return (p.prof ? D.prof : D.base) + p.f; }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function norm(s){ return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,''); }
function stats(){
 var n=D.p.length, l=D.p.filter(function(p){return p.st==='listo';}).length;
 var pil=D.p.filter(function(p){return p.pil;}), pl=pil.filter(function(p){return p.st==='listo';}).length;
 $('stats').innerHTML = '<div><b>'+l+'/'+n+'</b><span>piezas listas</span><div class="bar"><i style="width:'+Math.round(l/n*100)+'%"></i></div></div>'+
  '<div><b>'+pl+'/'+pil.length+'</b><span>versión piloto (+ este índice)</span><div class="bar"><i style="width:'+Math.round(pl/pil.length*100)+'%"></i></div></div>';
}
function filters(){
 var fs=[['todo','Todo'],['piloto','Piloto'],['listo','Listo']].concat(D.mods.map(function(m){ return [m[0], m[0]==='PR'?'Profesora':m[0]]; }));
 $('filters').innerHTML = fs.map(function(f){ return '<button type="button" data-f="'+f[0]+'" class="'+(F===f[0]?'on':'')+'"'+(F===f[0]?' aria-pressed="true"':'')+'>'+f[1]+'</button>'; }).join('');
}
function match(p){
 if(F==='piloto' && !p.pil) return false;
 if(F==='listo' && p.st!=='listo') return false;
 if(F!=='todo' && F!=='piloto' && F!=='listo' && p.m!==F) return false;
 if(Q){ var h=norm(p.c+' '+p.t+' '+p.d+' '+p.f); if(h.indexOf(Q)<0) return false; }
 return true;
}
function list(){
 var o='';
 D.mods.forEach(function(m){
  var ps = D.p.filter(function(p){ return p.m===m[0] && match(p); });
  if(!ps.length) return;
  o += '<h2 class="mod">'+m[1]+'</h2>';
  ps.forEach(function(p){
   var ready = !CHECKING && p.st==='listo', cls = CHECKING?'b-check':(ready?'b-listo':(p.st==='en curso'?'b-curso':'b-pend'));
   o += '<div class="it'+(ready?'':' off')+'"><div class="code">'+p.c+'</div><div><h3>'+p.t+'</h3><p>'+p.d+'</p><div class="file">'+(p.prof?'profesora/':'dele-curso/')+p.f+' · paso '+p.paso+' del plan</div></div>'+
    '<div class="acts"><div><span class="badge '+cls+'">'+(CHECKING?'COMPROBANDO':(ready?'SUBIDO':p.st.toUpperCase()))+'</span>'+(p.pil?'<span class="badge b-pil">PILOTO</span>':'')+(p.prof?'<span class="badge b-prof">PROFESORA</span>':'')+'</div>'+
    (ready ? (p.prof?'':'<button class="btn sm cta" data-copy="'+esc(url(p))+'">Copiar enlace</button>')+'<a class="btn sm" href="'+esc(url(p))+'" target="_blank" rel="noopener">Abrir</a>' : '')+
    '<span class="cp-ok" role="status"></span></div></div>';
  });
 });
 $('list').innerHTML = o || '<p class="muted">No hay nada con ese filtro.</p>';
}
function copy(t, done, fail){
 function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) done(); else fail(); }
 if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(done, fb); else fb();
}
document.addEventListener('click', function(e){
 var f=e.target.closest('[data-f]'); if(f){ F=f.getAttribute('data-f'); try{ localStorage.setItem('dele-a2-indice-filtro',F); }catch(x){} filters(); list(); return; }
 var c=e.target.closest('[data-copy]'); if(c){ var s=c.parentNode.querySelector('.cp-ok'); copy(c.getAttribute('data-copy'), function(){ s.textContent='✓ Enlace copiado'; setTimeout(function(){ s.textContent=''; },2500); }, function(){ s.textContent=c.getAttribute('data-copy'); }); }
});
$('q').addEventListener('input', function(){ Q=norm(this.value).trim(); list(); });
/* comprobar en el servidor que piezas estan subidas */
function check(){
 if(!LIVE){ $('chkmsg').textContent='Abierto desde el ordenador: el estado sale de la lista del archivo, no de la web.'; return; }
 $('chkmsg').textContent='Comprobando qué piezas están subidas...';
 var n=0;
 D.p.forEach(function(p){
  fetch(url(p)+'?v='+Date.now(), {method:'HEAD', cache:'no-store', credentials:'same-origin'}).then(function(r){
   p.st = r.ok ? 'listo' : 'pendiente';
  }, function(){ /* sin respuesta: se queda lo que diga la lista */ }).then(function(){
   n++; if(n===D.p.length){ CHECKING=false; $('chkmsg').textContent='Estado comprobado en la web ahora mismo: en verde, lo que ya está subido.'; stats(); list(); }
  });
 });
}
stats(); filters(); list(); check();
})();
"""

DATA = {"base": BASE_URL, "prof": PROF_URL, "mods": MODULOS, "p": P}
js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
body = BODY.replace("__BASE__", BASE_URL).replace("__PROF__", PROF_URL)
open(FILE, "w", encoding="ascii").write(page("Índice · Curso DELE A2", CSS_IDX, body, js))
print("ok", FILE, len(P), "piezas |", sum(1 for p in P if p["st"] == "listo"), "listas")
