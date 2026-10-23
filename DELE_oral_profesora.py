# -*- coding: utf-8 -*-
# LIBRETA ORAL DE LA PROFESORA · común a los simulacros DELE A2 y B2 (2spanishteachers.com)
# La usan DELE_A2_motor_simulacro.py y DELE_B2_motor_simulacro.py: tiene que estar junto a ellos.
# Genera DELEA2_F1_Uxx_oral_profesora.html / DELEB2_F1_xxx_oral_profesora.html
# (van a la carpeta protegida biblioteca/profesora/ de la web; nunca a la parte pública).
# - Escala analítica por tarea (coherencia, fluidez, corrección, alcance, 0-3) y holística global.
# - Nota orientativa /25: holística 40 % + analítica 60 % (B2: T1 35 %, T2 35 %, T3 30 %; A2: tercios).
# - Apuntes al vuelo por categorías, recuento rápido, cronómetros, informe con consejos automáticos,
#   PDF para el estudiante y PDF completo, historial por estudiante (compartido entre todas las libretas).
import json, re
TALLIES = [["pausa", "Silencio largo", False], ["muletilla", "Muletilla", False], ["repetir", "Pide que repita", False],
           ["autocorr", "Se corrige solo", True], ["parafrasis", "Explica con otras palabras", True]]
LEVELS = {
"B2": {
 "pesos": [0.35, 0.35, 0.30],
 "crit": [
  {"k": "coh", "n": "Coherencia", "d": [
   "Grupos de palabras con conectores muy simples (y, pero, porque); necesita mucha ayuda del interlocutor.",
   "Ideas en línea, frases breves con conectores habituales (es que, por eso, además); a veces pide aclaraciones.",
   "Discurso claro y ordenado, con conectores adecuados aunque limitados; colabora en la conversación.",
   "Discurso bien trabado, con conectores y recursos variados; conversa y toma el turno con naturalidad."]},
  {"k": "flu", "n": "Fluidez", "d": [
   "Frases muy breves; pausas, dudas y reformulaciones constantes; entenderle cuesta esfuerzo.",
   "Habla de forma continuada, pero con pausas evidentes para pensar la gramática y las palabras.",
   "Ritmo bastante regular; duda al buscar expresiones, pero hay pocas pausas largas. Se le entiende sin esfuerzo.",
   "Espontáneo y fluido incluso en intervenciones largas; parafrasea lo que no sabe; entonación expresiva."]},
  {"k": "cor", "n": "Corrección", "d": [
   "Errores básicos sistemáticos: confunde tiempos verbales y falla la concordancia.",
   "Controla estructuras habituales de situaciones previsibles; comete errores que no impiden entender.",
   "Control gramatical relativamente alto; sus errores no impiden entender y a veces los corrige.",
   "Control gramatical alto; errores escasos y pequeños que a menudo corrige."]},
  {"k": "alc", "n": "Alcance", "d": [
   "Vocabulario para temas personales y cotidianos; tiene que simplificar lo que quiere decir.",
   "Transmite información sencilla, pero no le alcanza para describir u opinar con claridad; busca las palabras.",
   "Vocabulario amplio para describir y opinar sobre temas generales, con oraciones complejas; alguna imprecisión.",
   "Repertorio amplio: dice lo que quiere sin limitarse; solo alguna imprecisión ocasional."]}],
 "hol": [
  "Apenas expresa opiniones ni describe; no cumple el objetivo de las tareas y necesita mucha ayuda.",
  "Aporta ideas poco claras o incompletas; no cumple del todo las tareas; sus limitaciones se notan mucho.",
  "Opina y describe con claridad y cumple las tareas; comete errores que a veces corrige; conversa de forma adecuada.",
  "Desarrolla sus ideas con detalle y claridad; muy buen control; conversa con facilidad y retoma lo que dice el interlocutor."],
 "errcats": [["conj", "Conjugación"], ["tiempos", "Tiempos del pasado"], ["subj", "Indicativo / subjuntivo"], ["serestar", "Ser / estar"],
  ["conc", "Concordancia"], ["prep", "Preposiciones"], ["pron", "Pronombres"], ["lex", "Léxico impreciso"],
  ["calco", "Palabra de otra lengua"], ["pronun", "Pronunciación"], ["conect", "Conectores y orden"], ["reg", "Registro (tú / usted)"]],
 "tips": {
  "crit": {
   "coh": {"t": "Ordena tu intervención.", "x": "Presenta el tema, desarrolla dos o tres ideas con un ejemplo cada una y termina con una conclusión.", "e": "En primer lugar... · Por un lado..., por otro... · Además... · Sin embargo... · En definitiva..."},
   "flu": {"t": "Gana tiempo sin quedarte en silencio.", "x": "Cuando necesites pensar, usa expresiones naturales en lugar de callarte: el silencio largo es lo que más penaliza.", "e": "Pues mira, la verdad es que... · ¿Cómo te diría? · A ver, lo que quiero decir es que..."},
   "cor": {"t": "Controla lo que más se nota.", "x": "Antes que estructuras difíciles, asegura los tiempos del pasado y el subjuntivo después de valorar o de negar una opinión.", "e": "Es importante que + subjuntivo · No creo que + subjuntivo · Me parece lógico que + subjuntivo"},
   "alc": {"t": "Si te falta una palabra, explícala.", "x": "Parafrasear no resta: demuestra recursos. Y amplía el vocabulario del tema antes del examen.", "e": "Es una especie de... · Es algo que sirve para... · No sé cómo se dice, pero es..."}},
  "task": {
   "1": {"t": "Tarea 1: valora de verdad las propuestas.", "x": "Comenta al menos cuatro. No digas solo si te gustan: da ventajas, inconvenientes, a quién beneficia o perjudica, y propón alguna mejora.", "e": "Esta propuesta tiene la ventaja de que... · El inconveniente es que... · Yo, en cambio, propondría... · Sería buena idea siempre que + subjuntivo"},
   "2": {"t": "Tarea 2: describe e imagina.", "x": "No sabes qué pasa en la foto: haz hipótesis sobre quiénes son, qué ha pasado antes y qué pasará después, y habla de sus sentimientos.", "e": "Parece que... · Puede que + subjuntivo · Estarán + gerundio · Deben de ser... · Seguramente acaban de..."},
   "3": {"t": "Tarea 3: compara y reacciona.", "x": "Explica tus respuestas y compáralas con los resultados: coincidencias, diferencias y qué te sorprende.", "e": "Me sorprende que + subjuntivo · Coincido con la mayoría en que... · A diferencia de los encuestados, yo... · Es curioso que..."}},
  "err": {
   "conj": {"t": "Repasa los verbos que has conjugado mal.", "x": "Escribe tres frases con cada uno y dilas en voz alta hasta que te suenen naturales."},
   "tiempos": {"t": "Pasado: acción terminada o contexto.", "x": "Indefinido para lo que pasó y terminó; imperfecto para describir la situación; pluscuamperfecto para lo que había pasado antes."},
   "subj": {"t": "Subjuntivo al valorar y al negar opiniones.", "x": "Después de es bueno que, me parece normal que, no creo que o no pienso que, el verbo va en subjuntivo."},
   "serestar": {"t": "Ser para definir, estar para situar y valorar un estado.", "x": "Repasa los casos que has fallado con ejemplos de la tarea."},
   "conc": {"t": "Revisa la concordancia.", "x": "Cuando hables de grupos o de nombres femeninos, fíjate en el final del adjetivo y del participio."},
   "prep": {"t": "Aprende los verbos con su preposición.", "x": "Estudia verbo y preposición juntos, como un bloque.", "e": "depender de · pensar en · estar de acuerdo con · consistir en · tratarse de"},
   "pron": {"t": "Cuidado con los pronombres.", "x": "Repasa le/lo, se y la posición del pronombre con infinitivo y gerundio."},
   "lex": {"t": "Busca la palabra exacta.", "x": "Apunta las palabras imprecisas que has usado y aprende la forma exacta del tema."},
   "calco": {"t": "Evita las palabras de otra lengua.", "x": "Si no sabes la palabra en español, explícala con otras: puntúa mejor que decirla en otra lengua."},
   "pronun": {"t": "Trabaja la pronunciación.", "x": "Grábate un minuto al día leyendo en voz alta y compara con un audio de modelo."},
   "conect": {"t": "Une tus ideas.", "x": "Usa conectores para ordenar y contrastar, no solo y y pero.", "e": "además · sin embargo · por eso · aun así · por último"},
   "reg": {"t": "Mantén el tratamiento.", "x": "Decide tú o usted al principio y mantenlo durante toda la conversación."}},
  "corto": {"t": "Habla un poco más.", "x": "Te has quedado corto de tiempo: prepara más ideas y desarrolla cada una con un ejemplo o una experiencia."},
  "largo": {"t": "Ajusta el tiempo.", "x": "Te has pasado: selecciona las ideas más importantes y ve al grano."},
  "muletillas": {"t": "Varía tus expresiones de relleno.", "x": "Repetir siempre la misma muletilla se nota. Alterna varias.", "e": "pues · bueno · la verdad es que · a ver"},
  "repetir": {"t": "Pedir aclaraciones está bien.", "x": "Si no entiendes, pídelo con naturalidad; pero intenta primero reaccionar con lo que sí has entendido.", "e": "¿Te refieres a...? · Perdona, ¿puedes repetir la última parte?"},
  "general": {"t": "¡Muy buena prueba!", "x": "Sigue practicando con temas de actualidad y cronometrándote para mantener este nivel."}}},
"A2": {
 "pesos": [1/3, 1/3, 1/3],
 "crit": [
  {"k": "coh", "n": "Coherencia", "d": [
   "Palabras sueltas o frases aisladas; casi no une las ideas.",
   "Frases sueltas unidas a veces con y o pero; cuesta seguir el orden.",
   "Frases sencillas bien enlazadas con conectores básicos (y, pero, porque, primero, después); se le sigue bien.",
   "Describe y cuenta con orden y con conectores sencillos variados; conversa con soltura sobre temas cotidianos."]},
  {"k": "flu", "n": "Fluidez", "d": [
   "Silencios largos; abandona las frases y necesita ayuda constante.",
   "Pausas y reformulaciones frecuentes; mantiene el discurso con dificultad.",
   "Hace pausas para buscar palabras, pero sigue hablando y se le entiende.",
   "Habla con bastante soltura para el nivel, con pocas pausas."]},
  {"k": "cor", "n": "Corrección", "d": [
   "Errores en casi todas las frases, incluso en lo más básico.",
   "Algunas estructuras básicas bien, pero errores repetidos en concordancia, presente o ser/estar.",
   "Usa bien las estructuras básicas; comete errores, pero se entiende lo que quiere decir.",
   "Buen control de lo básico y de los pasados frecuentes; pocos errores."]},
  {"k": "alc", "n": "Alcance", "d": [
   "Vocabulario muy limitado: no puede tratar el tema.",
   "Vocabulario básico insuficiente para parte del tema; recurre a otra lengua.",
   "Vocabulario suficiente para el tema cotidiano; alguna imprecisión o explicación con otras palabras.",
   "Vocabulario variado del tema; casi no busca palabras."]}],
 "hol": [
  "No consigue comunicar lo que se le pide; necesita ayuda constante.",
  "Comunica algo, pero de forma incompleta; muchas pausas y errores que dificultan entender.",
  "Cumple las tareas con frases sencillas y claras; errores que no impiden entender.",
  "Cumple las tareas con soltura para el nivel, con orden y buen vocabulario."],
 "errcats": [["conj", "Conjugación"], ["tiempos", "Tiempo verbal"], ["serestar", "Ser / estar / hay"], ["conc", "Concordancia"],
  ["prep", "Preposiciones"], ["pron", "Pronombres (me, le, gustar)"], ["lex", "Palabra equivocada"], ["calco", "Palabra de otra lengua"],
  ["pronun", "Pronunciación"], ["conect", "Orden y conectores"]],
 "tips": {
  "crit": {
   "coh": {"t": "Ordena lo que dices.", "x": "Empieza presentando el tema, habla de las pautas una a una y termina con tu opinión.", "e": "Primero... · Después... · También... · Al final... · Para mí es importante porque..."},
   "flu": {"t": "No te quedes en silencio.", "x": "Pensar está bien: usa una expresión para ganar tiempo y sigue hablando.", "e": "Pues... · A ver... · Bueno... · Es que..."},
   "cor": {"t": "Asegura lo básico.", "x": "Mejor una frase sencilla correcta que una frase larga con errores. Cuida el presente, la concordancia y ser/estar."},
   "alc": {"t": "Si no sabes una palabra, descríbela.", "x": "Explicar una palabra con otras suma puntos: es una estrategia, no un fallo.", "e": "Es una cosa que sirve para... · Es como... · Es un lugar donde..."}},
  "task": {
   "1": {"t": "Tarea 1: habla de todas las pautas.", "x": "Presenta el tema, dedica dos o tres frases a cada pauta y cierra con tu opinión. No recites un texto memorizado.", "e": "Voy a hablar de... · Por ejemplo... · Para mí..."},
   "2": {"t": "Tarea 2: sigue siempre el mismo orden.", "x": "Quiénes son, dónde están, qué hacen, qué ropa llevan, qué hay y qué va a pasar después.", "e": "Hay... · Está / están + gerundio · Lleva... · Parece que... · Creo que van a..."},
   "3": {"t": "Tarea 3: interactúa.", "x": "Saluda, pregunta, reacciona a lo que dice el entrevistador y despídete. No respondas solo sí o no.", "e": "Perdone, ¿tiene...? · ¿Cuánto cuesta? · ¡Qué bien! · Vale, perfecto · Muchas gracias, adiós"}},
  "err": {
   "conj": {"t": "Repasa los verbos que has conjugado mal.", "x": "Escribe tres frases con cada uno y dilas en voz alta."},
   "tiempos": {"t": "Presente o pasado.", "x": "Hoy, esta semana → he + participio; ayer, el año pasado → pasado (fui, comí, estuve)."},
   "serestar": {"t": "Ser, estar o hay.", "x": "Ser para cómo es algo, estar para dónde está o cómo está, hay para decir que existe algo."},
   "conc": {"t": "Masculino y femenino, singular y plural.", "x": "El adjetivo cambia con el nombre: mi hermana es alta, los pisos son caros."},
   "prep": {"t": "Preposiciones frecuentes.", "x": "Ir a, estar en, venir de, salir con: apréndelas con el verbo."},
   "pron": {"t": "Gustar y los pronombres.", "x": "A mí me gusta, a él le gusta, nos gustan las fiestas."},
   "lex": {"t": "Vocabulario del tema.", "x": "Haz una lista con las palabras del tema de la unidad y úsalas en frases tuyas."},
   "calco": {"t": "Sin palabras de otra lengua.", "x": "Si no sabes una palabra, descríbela en español."},
   "pronun": {"t": "Pronunciación.", "x": "Lee en voz alta un minuto al día y grábate."},
   "conect": {"t": "Une las frases.", "x": "Usa y, pero, porque, también, entonces, primero, después."}},
  "corto": {"t": "Habla un poco más.", "x": "Te has quedado corto: prepara dos o tres frases para cada pauta."},
  "largo": {"t": "Ajusta el tiempo.", "x": "Te has pasado un poco: di lo importante de cada pauta y pasa a la siguiente."},
  "muletillas": {"t": "Varía tus expresiones.", "x": "Alterna pues, bueno, a ver, es que: no repitas siempre la misma."},
  "repetir": {"t": "Pedir que repitan está bien.", "x": "Hazlo con naturalidad.", "e": "¿Puede repetir, por favor? · Perdone, no entiendo."},
  "general": {"t": "¡Muy buena prueba!", "x": "Sigue practicando cada semana con un tema y cronómetro."}}}}
for k in LEVELS: LEVELS[k]["tallies"] = TALLIES


CSS = r""".sw{display:inline-flex;align-items:center;gap:6px;border:1.5px solid var(--line);border-radius:999px;padding:3px 4px 3px 12px;background:#fff;font-size:.85rem;vertical-align:middle;margin-left:10px;font-family:system-ui,sans-serif;font-weight:400}
.sw-lbl{color:var(--muted)}
.sw-t{font-variant-numeric:tabular-nums;font-weight:700;min-width:3.2em;text-align:right;color:var(--ink)}
.sw-b{border:0;background:var(--coral-soft);color:var(--ink);border-radius:50%;width:28px;height:28px;cursor:pointer;font-size:.8rem;line-height:28px;padding:0}
.sw-b:hover{background:var(--coral);color:#fff}
.sw.near{border-color:#C98A1B}.sw.near .sw-t{color:#9A6512}
.sw.ok{border-color:#2F7D4F;background:#EAF5EE}.sw.ok .sw-t{color:#2F7D4F}
.sw.over{border-color:#B3261E;background:#FBEAEA}.sw.over .sw-t{color:#B3261E}
.sw.run .sw-t::after{content:" \25CF";font-size:.6em;color:#B3261E;vertical-align:middle}
.hsw{display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.topbar{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin:0 0 10px}
.topbar input,.topbar select{margin-left:6px;padding:6px 10px;border:1.5px solid var(--line);border-radius:8px;font:inherit;width:auto}
.cols{display:grid;grid-template-columns:1fr 1.15fr;gap:16px;align-items:start}
@media (max-width:860px){.cols{grid-template-columns:1fr}}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:0 0 14px}
.card h4{margin:0 0 8px;font-size:1rem}
.phrow{margin:6px 0}.phrow .sw{margin-left:0;font-size:.95rem}
.opsel{margin:6px 0 14px}
.chip{border:1.5px solid var(--line);background:#fff;border-radius:999px;padding:5px 12px;margin:3px 4px 3px 0;cursor:pointer;font:inherit;font-size:.9rem}
.chip.on{background:var(--coral);border-color:var(--coral);color:#fff}
.chip.good{border-color:#2F7D4F;color:#2F7D4F}
.small-chip{font-size:.82rem;padding:4px 10px}
ol.ent{margin:0;padding-left:20px}ol.ent li{margin:4px 0}
ul.mini{margin:0;padding-left:18px;font-size:.9rem}ul.mini li{margin:2px 0}
table.mini-t{font-size:.85rem;margin-top:6px;border-collapse:collapse}table.mini-t td{padding:2px 8px 2px 0;border-bottom:1px solid var(--line)}
.ckrow{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:6px 0;border-bottom:1px solid var(--line);font-size:.93rem}
.tri{display:inline-flex;flex-shrink:0}
.tb{border:1.5px solid var(--line);background:#fff;padding:4px 9px;font:inherit;font-size:.8rem;cursor:pointer;margin-left:-1.5px}
.tb:first-child{border-radius:8px 0 0 8px}.tb:last-child{border-radius:0 8px 8px 0}
.tb.t0.on{background:#2F7D4F;border-color:#2F7D4F;color:#fff}.tb.t1.on{background:#C98A1B;border-color:#C98A1B;color:#fff}.tb.t2.on{background:#B3261E;border-color:#B3261E;color:#fff}
.crow{display:grid;grid-template-columns:110px auto;gap:4px 10px;align-items:center;padding:6px 0;border-bottom:1px solid var(--line)}
.nums{display:inline-flex;gap:6px}
.nb{width:34px;height:34px;border-radius:50%;border:1.5px solid var(--line);background:#fff;font:inherit;font-weight:700;cursor:pointer}
.nb.on{background:var(--coral);border-color:var(--coral);color:#fff}
.cdesc{grid-column:1/-1;font-size:.83rem;color:var(--muted);min-height:0}
.mrow{margin:10px 0 0}
.logrow{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0}
.logrow input{flex:1 1 180px;padding:7px 10px;border:1.5px solid var(--line);border-radius:8px;font:inherit}
ul.log{list-style:none;padding:0;margin:8px 0 0;font-size:.9rem}ul.log li{padding:4px 0;border-bottom:1px dashed var(--line)}
.tag{display:inline-block;font-size:.72rem;background:#F1EEE8;border-radius:6px;padding:1px 6px;margin-right:4px}
.lg-good{color:#2F7D4F}
.x{border:0;background:none;color:var(--muted);cursor:pointer;font-size:1rem}
ul.pick{list-style:none;padding:0}ul.pick li{padding:6px 10px;border:1.5px solid var(--line);border-radius:8px;margin:4px 0;cursor:pointer;background:#fff}
ul.pick li.on{border-color:#2F7D4F;background:#EAF5EE}
#printarea textarea{min-height:70px}
.sem th{text-align:left;font-size:.85rem;color:var(--muted);padding:6px}
.codebox{display:flex;flex-wrap:wrap;align-items:center;gap:14px;background:#fff;border:1.5px solid var(--line);border-radius:12px;padding:10px 16px;margin:0 0 14px}
.codebox .code{font:700 1.7rem/1.1 ui-monospace,Menlo,monospace;letter-spacing:.18em}
.btn-copy{background:#0B4F3C;color:#fff;border:0;border-radius:999px;padding:8px 16px;font:inherit;font-weight:700;cursor:pointer}
.btn-copy:hover{background:#08382B}
.catrow{display:flex;flex-wrap:wrap;gap:4px;margin:6px 0}
.chip.last{border-color:var(--ink);font-weight:700}
.chip.vocab{border-color:#3A5BA0;color:#3A5BA0}
.lg-voc{color:#3A5BA0}
.tallies{display:grid;grid-template-columns:1fr 1fr;gap:6px 14px}
.tally{display:flex;align-items:center;gap:6px;font-size:.88rem}
.tally span{flex:1}.tally.pos span{color:#2F7D4F}
.tally button{width:26px;height:26px;border-radius:50%;border:1.5px solid var(--line);background:#fff;cursor:pointer;font-weight:700;line-height:1;padding:0}
.tally b{min-width:1.4em;text-align:center}
.pre{white-space:pre-wrap;background:#F6F3EE;border-radius:8px;padding:8px 10px;margin:6px 0}
.nums.big .nb{width:44px;height:44px;font-size:1.1rem}
.notaline{font-size:1.2rem;margin:4px 0}.notaline b{font-size:2rem;font-family:Georgia,serif}
.estr{margin-top:6px;font-style:italic;color:var(--ink)}
.linkbtn{border:0;background:none;color:var(--ink);text-decoration:underline;cursor:pointer;font:inherit;font-size:.85rem;padding:0}
.nowrap{white-space:nowrap}
.endcard{border:2px solid var(--coral)}
textarea{min-height:70px}
#print{display:none}
@media print{
 body.printing > *:not(#print){display:none !important}
 body.printing #print{display:block !important}
 .printdoc{font-size:11pt;line-height:1.45}.printdoc h4{margin:14px 0 4px;font-size:11pt}
}

main.wrap,.top-in{max-width:1240px}
"""
JS = r"""(function(){
var D = __DATA__;
var ALL = __LEVELS__, LV = ALL[D.level];
var UP='ABCDEFGH'.split('');
var KEY_ALL='2st_oral_historial_v1', KEY_CUR='2st_oral_actual_'+D.examen;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function fmt(s){ s=s||0; return Math.floor(s/60)+':'+((s%60)<10?'0':'')+(s%60); }
function today(){ return new Date().toLocaleDateString('es-ES'); }

/* ---------- estado ---------- */
function blank(){ var t={}; D.tasks.forEach(function(tk){ t[tk.n]={op:0,sc:{},ck:{},times:{},tal:{},nota:''}; });
 return {id:'', name:'', fecha:today(), examen:D.examen, level:D.level, title:D.title, tab:D.tasks[0].n, t:t, hol:null, log:[], prioridad:'', pick:{}, cats:{}, priv:'', lastCat:LV.errcats[0][0]}; }
function loadJ(k,d){ try{ var r=localStorage.getItem(k); return r?JSON.parse(r):d; }catch(e){ return d; } }
function saveJ(k,v){ try{ localStorage.setItem(k, JSON.stringify(v)); return true; }catch(e){ return false; } }
var E = loadJ(KEY_CUR, null) || blank();
var HIST = loadJ(KEY_ALL, []);
function save(){ saveJ(KEY_CUR, E); }

/* ---------- calculos ---------- */
function tmean(n){ var s=E.t[n].sc, v=LV.crit.map(function(c){return s[c.k];}).filter(function(x){return x!=null;}); return v.length? v.reduce(function(a,b){return a+b;},0)/v.length : null; }
function cmean(k){ var v=D.tasks.map(function(tk){return E.t[tk.n].sc[k];}).filter(function(x){return x!=null;}); return v.length? v.reduce(function(a,b){return a+b;},0)/v.length : null; }
function nota(ev){ ev=ev||E; var ok=true, an=0;
 D.tasks.forEach(function(tk,i){ var s=ev.t[tk.n].sc, v=LV.crit.map(function(c){return s[c.k];}); if(v.some(function(x){return x==null;})) ok=false; else an += LV.pesos[i]*(v.reduce(function(a,b){return a+b;},0)/v.length); });
 if(!ok || ev.hol==null) return null;
 return Math.round(25*(0.4*ev.hol/3 + 0.6*an/3)*10)/10; }
function light(m){ return m==null?'':(m>=2?'g':(m>=1.5?'a':'r')); }
function banda(m){ return m==null?'sin evaluar':(m>=2.5?'supera el nivel '+D.level:(m>=2?'alcanza el nivel '+D.level:(m>=1.5?'cerca del nivel '+D.level+', pero todavía no lo alcanza':'todavía no alcanza el nivel '+D.level))); }
function dec(m){ return m==null?'-':m.toFixed(1).replace('.',','); }
function catName(k){ var lv=[LV].concat(Object.keys(ALL).map(function(x){return ALL[x];})); for(var j=0;j<lv.length;j++) for(var i=0;i<lv[j].errcats.length;i++) if(lv[j].errcats[i][0]===k) return lv[j].errcats[i][1]; return k==='vocab'?'Palabra que no sabía':(k==='bien'?'Buen uso':k); }
function errs(ev){ return (ev||E).log.filter(function(x){ return x.c!=='vocab' && x.c!=='bien'; }); }
function freq(ev){ var f={}; errs(ev).forEach(function(x){ f[x.c]=(f[x.c]||0)+1; }); return Object.keys(f).sort(function(a,b){return f[b]-f[a];}).map(function(k){return [k,f[k]];}); }

/* ---------- cronometros ---------- */
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

window.onSwChange=function(id){ var p=id.split('-'); E.t[p[0]].times[p[1]]=swSecs(id); save(); };
function restoreSW(){ SW={}; D.tasks.forEach(function(tk){ var tm=E.t[tk.n].times; for(var ph in tm){ SW[tk.n+'-'+ph]={acc:tm[ph]*1000,run:false,t0:0}; } }); }
setInterval(function(){ var any=false; for(var k in SW){ if(SW[k].run){ var p=k.split('-'); E.t[p[0]].times[p[1]]=swSecs(k); any=true; } } if(any) save(); }, 3000);

/* ---------- vistas ---------- */
function head(){
 var o='<div class="codebox noprint"><div><span class="small muted">Código de la oral · '+D.examen+'</span><div class="code">'+D.codigo+'</div></div><button class="btn-copy" data-a="copycode">Copiar código</button><span id="ccok" class="small muted"></span></div>';
 o+='<div class="topbar noprint"><label>Estudiante <input id="ename" value="'+esc(E.name)+'" placeholder="Nombre y apellido" autocomplete="off" list="alumnos"></label><datalist id="alumnos">'+alumnos().map(function(n){return '<option value="'+esc(n)+'">';}).join('')+'</datalist><span class="small muted">'+esc(E.fecha)+'</span></div>';
 var tabs=D.tasks.map(function(tk){ var m=tmean(tk.n); return [tk.n,'Tarea '+tk.n+(m!=null?' <span class="dot '+light(m)+'"></span>':'')]; }).concat([['inf','Nota e informe'],['his','Historial']]);
 o+='<nav class="steps noprint">'+tabs.map(function(t){ return '<button class="'+(String(E.tab)===String(t[0])?'on':'')+'" data-a="tab" data-t="'+t[0]+'">'+t[1]+'</button>'; }).join('')+'</nav>';
 return o;
}
function vTask(n){
 var tk=D.tasks.filter(function(x){return x.n===n;})[0], st=E.t[n], op=tk.opts[st.op]||tk.opts[0], o='<h3>'+tk.name+' <span class="muted small">'+tk.dur+'</span></h3>';
 if(tk.opts.length>1){ o+='<div class="opsel">Ha elegido: '+tk.opts.map(function(x,i){ return '<button class="chip'+(st.op===i?' on':'')+'" data-a="op" data-n="'+n+'" data-i="'+i+'">'+esc(x.title)+'</button>'; }).join('')+'</div>'; }
 o+='<div class="cols"><div class="col">';
 o+='<div class="card"><h4>Tiempos</h4>'+tk.phases.map(function(ph){ return '<div class="phrow">'+swHtml(n+'-'+ph[0],ph[1],ph[2],ph[3])+'</div>'; }).join('')+'</div>';
 o+=noteCard(n);
 o+='<div class="card"><h4>Recuento rápido</h4><div class="tallies">'+LV.tallies.map(function(t){ var v=st.tal[t[0]]||0; return '<div class="tally'+(t[2]?' pos':'')+'"><span>'+t[1]+'</span><button data-a="tal" data-n="'+n+'" data-k="'+t[0]+'" data-d="-1" aria-label="Restar">&minus;</button><b>'+v+'</b><button data-a="tal" data-n="'+n+'" data-k="'+t[0]+'" data-d="1" aria-label="Sumar">+</button></div>'; }).join('')+'</div></div>';
 o+='<div class="card"><h4>Lo que ve el estudiante</h4>'+op.lamina+'</div>';
 o+='<div class="card"><h4>'+(tk.guionTitle||'Guion del entrevistador')+'</h4>'+(op.ent&&op.ent.length?'<ol class="ent">'+op.ent.map(function(q){return '<li>'+q+'</li>';}).join('')+'</ol>':'')+(tk.guion?'<div class="small pre">'+tk.guion+'</div>':'')+'<p class="small muted"><b>Si se bloquea:</b> '+tk.ayudas.join(' · ')+'</p></div>';
 if(D.errores) o+='<div class="card"><h4>Errores esperables en esta unidad</h4><div class="small pre">'+D.errores+'</div></div>';
 o+='</div><div class="col">';
 o+='<div class="card"><h4>¿Cumple la tarea?</h4>'+tk.checks.map(function(c,i){ var v=st.ck[i]; return '<div class="ckrow"><span>'+c+'</span><span class="tri">'+['Sí','A medias','No'].map(function(l,j){ return '<button class="tb t'+j+(v===j?' on':'')+'" data-a="ck" data-n="'+n+'" data-i="'+i+'" data-v="'+j+'">'+l+'</button>'; }).join('')+'</span></div>'; }).join('')+'</div>';
 o+='<div class="card"><h4>Escala analítica de la tarea (0-3)</h4><p class="small muted">2 = alcanza el nivel '+D.level+' · 3 = lo supera con claridad · 1 = todavía no lo alcanza · 0 = muy lejos</p>';
 LV.crit.forEach(function(c){ var v=st.sc[c.k]; o+='<div class="crow"><b>'+c.n+'</b><span class="nums">'+[0,1,2,3].map(function(j){ return '<button class="nb'+(v===j?' on':'')+'" data-a="sc" data-n="'+n+'" data-k="'+c.k+'" data-v="'+j+'" title="'+esc(c.d[j])+'">'+j+'</button>'; }).join('')+'</span><div class="cdesc">'+(v!=null?c.d[v]:'<span class="muted">Pasa el ratón o toca un número para ver la descripción.</span>')+'</div></div>'; });
 var m=tmean(n); o+='<p class="mrow">Media de la tarea: <b>'+dec(m)+'</b> '+(m==null?'':'<span class="dot '+light(m)+'"></span>'+banda(m))+'</p></div>';
 o+='<div class="card"><h4>Notas libres de esta tarea</h4><textarea data-f="nota" data-n="'+n+'" placeholder="Ideas que ha dado, cómo ha organizado, qué le ha faltado...">'+esc(st.nota)+'</textarea></div>';
 o+='</div></div>';
 return o;
}
function noteCard(n){
 var o='<div class="card notecard"><h4>Apuntes al vuelo</h4>';
 o+='<div class="logrow"><input id="dijo" placeholder="Lo que ha dicho (ej.: *yo sabo)" autocomplete="off"><input id="corr" placeholder="Forma correcta (opcional)" autocomplete="off"></div>';
 o+='<div class="catrow">'+LV.errcats.map(function(c){ return '<button class="chip small-chip'+(E.lastCat===c[0]?' last':'')+'" data-a="add" data-n="'+n+'" data-c="'+c[0]+'">'+c[1]+'</button>'; }).join('')+'</div>';
 o+='<div class="catrow"><button class="chip small-chip vocab" data-a="add" data-n="'+n+'" data-c="vocab">+ Palabra que no sabía</button><button class="chip small-chip good" data-a="add" data-n="'+n+'" data-c="bien">+ Buen uso</button></div>';
 o+='<p class="small muted">Escribe y toca la categoría. <b>Intro</b> la guarda en la última categoría usada (<b>'+catName(E.lastCat)+'</b>).</p>';
 var L=E.log.filter(function(x){return x.n===n;});
 if(L.length){ o+='<ul class="log">'+L.map(function(x){ var i=E.log.indexOf(x); var cls=x.c==='bien'?'lg-good':(x.c==='vocab'?'lg-voc':'');
  return '<li class="'+cls+'"><span class="tag">'+catName(x.c)+'</span> '+(x.c==='bien'?'\u2713 ':'')+'«'+esc(x.dijo)+'»'+(x.corr?' \u2192 «'+esc(x.corr)+'»':'')+' <button class="x" data-a="del" data-i="'+i+'" aria-label="Borrar">&times;</button></li>'; }).reverse().join('')+'</ul>'; }
 return o+'</div>';
}

/* ---------- consejos ---------- */
function tips(ev){
 ev=ev||E; var out=[], seen={};
 function add(t){ if(t && !seen[t.t]){ seen[t.t]=1; out.push(t); } }
 var cm=LV.crit.map(function(c){ var v=D.tasks.map(function(tk){return ev.t[tk.n].sc[c.k];}).filter(function(x){return x!=null;}); return [c.k, v.length? v.reduce(function(a,b){return a+b;},0)/v.length : null]; }).filter(function(x){return x[1]!=null;}).sort(function(a,b){return a[1]-b[1];});
 cm.forEach(function(x){ if(x[1]<2) add(LV.tips.crit[x[0]]); });
 D.tasks.forEach(function(tk){ var st=ev.t[tk.n], v=LV.crit.map(function(c){return st.sc[c.k];}).filter(function(x){return x!=null;}), m=v.length?v.reduce(function(a,b){return a+b;},0)/v.length:null;
  var falta=Object.keys(st.ck).some(function(i){ return st.ck[i]>0; });
  if((m!=null&&m<2)||falta) add(LV.tips.task[tk.n]);
  tk.phases.forEach(function(ph){ var s=st.times[ph[0]]||0; if(s && s<ph[2]*60-15) add(LV.tips.corto); if(s>ph[3]*60+30) add(LV.tips.largo); });
  if((st.tal.pausa||0)>=3) add(LV.tips.crit.flu); if((st.tal.muletilla||0)>=4) add(LV.tips.muletillas); if((st.tal.repetir||0)>=2) add(LV.tips.repetir);
 });
 freq(ev).slice(0,3).forEach(function(f){ if(f[1]>=2 || freq(ev).length<=2) add(LV.tips.err[f[0]]); });
 if(!out.length) add(LV.tips.general);
 return out.slice(0,5);
}

/* ---------- informe ---------- */
function vInforme(){
 var o='<div class="card"><h4>Escala holística · toda la prueba (40 % de la nota)</h4><p class="small muted">Impresión global de las tres tareas, como la del entrevistador del Instituto Cervantes.</p><div class="nums big">'+[0,1,2,3].map(function(j){ return '<button class="nb'+(E.hol===j?' on':'')+'" data-a="hol" data-v="'+j+'" title="'+esc(LV.hol[j])+'">'+j+'</button>'; }).join('')+'</div><div class="cdesc">'+(E.hol!=null?LV.hol[E.hol]:'')+'</div></div>';
 var nt=nota();
 o+='<div class="card"><h4>Nota orientativa</h4>'+(nt==null?'<p class="muted">Completa la escala analítica de las tres tareas y la holística para ver la nota.</p>':'<p class="notaline"><b>'+nt.toString().replace('.',',')+'</b> / 25 <span class="dot '+(nt>=15?'g':(nt>=12.5?'a':'r'))+'"></span>'+(nt>=15?'Por encima del 60 %':'Por debajo del 60 %')+'</p><p class="small muted">Cálculo como en el DELE: holística 40 % + analítica 60 % (tareas '+LV.pesos.map(function(p,i){return 'T'+(i+1)+' '+Math.round(p*100)+' %';}).join(', ')+'). En el examen, el 60 % de esta prueba son 15 puntos. Es una estimación: no es una calificación oficial.</p>')+'</div>';
 o+='<div class="card"><h4>Resumen</h4><table class="sem"><thead><tr><th></th>'+D.tasks.map(function(tk){return '<th>T'+tk.n+'</th>';}).join('')+'<th>Media</th></tr></thead><tbody>';
 LV.crit.forEach(function(c){ var m=cmean(c.k); o+='<tr><td><b>'+c.n+'</b></td>'+D.tasks.map(function(tk){ var v=E.t[tk.n].sc[c.k]; return '<td>'+(v==null?'-':v)+'</td>'; }).join('')+'<td><span class="dot '+light(m)+'"></span>'+dec(m)+'</td></tr>'; });
 o+='</tbody></table></div>';
 var bien=E.log.filter(function(x){return x.c==='bien';});
 o+='<div class="card"><h4>Lo que ha hecho bien <span class="small muted">· elige dos</span></h4>'+(bien.length?'<ul class="pick">'+bien.map(function(b){ var i=E.log.indexOf(b); return '<li class="'+(E.pick[i]?'on':'')+'" data-a="pick" data-i="'+i+'">'+(E.pick[i]?'\u2713 ':'')+'«'+esc(b.dijo)+'»'+(b.corr?' ('+esc(b.corr)+')':'')+' <span class="muted small">T'+b.n+'</span></li>'; }).join('')+'</ul>':'<p class="muted small">Apúntalo durante la prueba con «+ Buen uso».</p>')+'</div>';
 o+='<div class="card"><h4>Una sola prioridad para mejorar</h4><textarea data-f="prioridad" placeholder="La que más le va a ayudar en el examen">'+esc(E.prioridad)+'</textarea></div>';
 var fr=freq(); o+='<div class="card"><h4>Errores por tipo</h4>'+(fr.length?'<ul>'+fr.map(function(f){ return '<li><b>'+catName(f[0])+'</b> ('+f[1]+')</li>'; }).join('')+'</ul>':'<p class="muted small">Ninguno anotado.</p>')+'</div>';
 var tp=tips(); o+='<div class="card"><h4>Consejos que recibirá</h4><p class="small muted">Se eligen solos según sus puntuaciones, sus errores y sus tiempos.</p>'+tp.map(function(t){ return '<div class="tip"><b>'+t.t+'</b><br>'+t.x+(t.e?'<div class="estr">'+t.e+'</div>':'')+'</div>'; }).join('')+'</div>';
 o+='<div class="card"><h4>Contenidos que tiene que repasar</h4><div>'+Object.keys(D.cats).map(function(k){ return '<button class="chip'+(E.cats[k]?' on':'')+'" data-a="cat" data-k="'+k+'">'+D.cats[k].name+'</button>'; }).join('')+'</div></div>';
 o+='<div class="card"><h4>Notas privadas <span class="small muted">· solo en tu PDF, nunca en el del estudiante</span></h4><textarea data-f="priv">'+esc(E.priv)+'</textarea></div>';
 o+='<div class="row"><button class="btn cta" data-a="copyrep">Copiar informe para el estudiante</button><button class="btn" data-a="print" data-m="est">PDF para el estudiante</button><button class="btn" data-a="print" data-m="prof">PDF completo para mi archivo</button></div><div id="repok" class="copied-box" hidden></div>';
 o+='<div class="card endcard"><h4>Terminar</h4><p class="small">Guarda la evaluación en el historial del estudiante y deja la libreta limpia para el siguiente.</p><button class="btn cta" data-a="guardar">Guardar en el historial y limpiar</button></div>';
 return o;
}
function studentText(ev){
 ev=ev||E; var L=['INFORME DE LA PRUEBA ORAL', D.title+' ('+ev.examen+')', 'Nombre: '+(ev.name||'-')+' · Fecha: '+ev.fecha, ''];
 var nt=nota(ev); L.push('NOTA ORIENTATIVA: '+(nt==null?'-':String(nt).replace('.',',')+' / 25')+'  (en el examen, el 60 % son 15 puntos)');
 LV.crit.forEach(function(c){ var v=D.tasks.map(function(tk){return ev.t[tk.n].sc[c.k];}).filter(function(x){return x!=null;}), m=v.length?v.reduce(function(a,b){return a+b;},0)/v.length:null; L.push('- '+c.n+': '+dec(m)+' / 3 ('+banda(m)+')'); });
 L.push(''); L.push('TIEMPOS:'); D.tasks.forEach(function(tk){ L.push('- Tarea '+tk.n+': '+tk.phases.map(function(ph){ var s=ev.t[tk.n].times[ph[0]]; return ph[1]+' '+(s?fmt(s):'sin cronometrar')+' (objetivo '+ph[2]+'-'+ph[3]+' min)'; }).join(' · ')); });
 var falt=[]; D.tasks.forEach(function(tk){ var ck=ev.t[tk.n].ck; tk.checks.forEach(function(c,i){ if(ck[i]>0) falt.push('Tarea '+tk.n+': '+c.charAt(0).toLowerCase()+c.slice(1)+(ck[i]===1?' (a medias)':'')); }); });
 if(falt.length){ L.push(''); L.push('LO QUE TE FALTÓ EN LAS TAREAS:'); falt.forEach(function(f){ L.push('- '+f); }); }
 var pk=ev.log.filter(function(x,i){return x.c==='bien' && ev.pick[i];}); if(!pk.length) pk=ev.log.filter(function(x){return x.c==='bien';}).slice(0,2);
 L.push(''); L.push('LO QUE HAS HECHO BIEN:'); if(!pk.length) L.push('-'); pk.forEach(function(b){ L.push('- «'+b.dijo+'»'+(b.corr?' ('+b.corr+')':'')); });
 L.push(''); L.push('TU PRIORIDAD PARA MEJORAR:'); L.push(ev.prioridad||'-');
 var fr=freq(ev); L.push(''); L.push('TUS ERRORES:'); if(!fr.length) L.push('- ninguno anotado');
 fr.forEach(function(f){ L.push('* '+catName(f[0])+' ('+f[1]+')'); errs(ev).filter(function(x){return x.c===f[0];}).forEach(function(x){ L.push('   Dijiste «'+x.dijo+'»'+(x.corr?' -> mejor: «'+x.corr+'»':'')); }); });
 var vo=ev.log.filter(function(x){return x.c==='vocab';}); if(vo.length){ L.push(''); L.push('PALABRAS PARA APRENDER:'); vo.forEach(function(x){ L.push('- '+x.dijo+(x.corr?': '+x.corr:'')); }); }
 L.push(''); L.push('CONSEJOS PARA TU PRÓXIMA PRUEBA ORAL:'); tips(ev).forEach(function(t){ L.push('- '+t.t+' '+t.x); if(t.e) L.push('  Estructuras útiles: '+t.e.replace(/<[^>]+>/g,'')); });
 var sel=Object.keys(ev.cats).filter(function(k){return ev.cats[k];}); if(sel.length){ L.push(''); L.push('QUÉ REPASAR:'); sel.forEach(function(k){ L.push('- '+D.cats[k].name+': '+String(D.cats[k].repaso||'').replace(/<[^>]+>/g,'')); }); }
 L.push(''); L.push('Material de preparación para el examen DELE, no oficial e independiente del Instituto Cervantes.');
 return L.join('\n');
}
function printHtml(ev, mode){
 var t=studentText(ev).split('\n').map(function(l){ return l===''?'<br>':(/^[A-ZÁÉÍÓÚÑ ]{6,}:/.test(l)||/^INFORME/.test(l)?'<h4>'+esc(l)+'</h4>':'<div>'+esc(l)+'</div>'); }).join('');
 if(mode==='prof'){
  t+='<h4>REGISTRO COMPLETO (PROFESORA)</h4>';
  D.tasks.forEach(function(tk){ var st=ev.t[tk.n]; t+='<div><b>Tarea '+tk.n+'</b> · opción: '+esc((tk.opts[st.op]||{}).title||'-')+' · '+LV.crit.map(function(c){return c.n+' '+(st.sc[c.k]==null?'-':st.sc[c.k]);}).join(' · ')+'</div>';
   t+='<div class="small">Recuento: '+LV.tallies.map(function(x){ return x[1]+' '+(st.tal[x[0]]||0); }).join(' · ')+'</div>'; if(st.nota) t+='<div class="small">Notas: '+esc(st.nota)+'</div>'; });
  t+='<div>Holística: '+(ev.hol==null?'-':ev.hol)+'</div>';
  if(ev.priv) t+='<h4>NOTAS PRIVADAS</h4><div>'+esc(ev.priv)+'</div>';
 }
 return '<div class="printdoc">'+t+'</div>';
}

/* ---------- historial ---------- */
function alumnos(){ var s={}; HIST.forEach(function(h){ if(h.name) s[h.name]=1; }); return Object.keys(s).sort(); }
function vHist(){
 var names=alumnos(), sel=E.histSel||E.name||names[0]||'';
 var o='<div class="card"><h4>Historial de estudiantes</h4><p class="small muted">Aquí se guardan todas las orales que corriges con estas libretas (A2 y B2), en este navegador.</p>';
 if(!names.length) return o+'<p class="muted">Todavía no hay evaluaciones guardadas. Al terminar una prueba, pulsa «Guardar en el historial y limpiar».</p></div>'+backup();
 o+='<label>Estudiante <select id="hsel">'+names.map(function(n){return '<option'+(n===sel?' selected':'')+'>'+esc(n)+'</option>';}).join('')+'</select></label>';
 var H=HIST.filter(function(h){return h.name===sel;});
 o+='<table class="sem"><thead><tr><th>Fecha</th><th>Examen</th><th>Nota</th><th>Hol.</th>'+LV.crit.map(function(c){return '<th>'+c.n.slice(0,4)+'.</th>';}).join('')+'<th>Errores</th><th></th></tr></thead><tbody>';
 H.forEach(function(h){ var i=HIST.indexOf(h); o+='<tr><td>'+esc(h.fecha)+'</td><td>'+esc(h.examen)+'</td><td><b>'+(h.nota==null?'-':String(h.nota).replace('.',','))+'</b></td><td>'+(h.hol==null?'-':h.hol)+'</td>'+LV.crit.map(function(c){ return '<td>'+(h.cm?dec(h.cm[c.k]):'-')+'</td>'; }).join('')+'<td>'+(h.nerr||0)+'</td><td class="nowrap"><button class="linkbtn" data-a="hpdf" data-i="'+i+'">PDF</button> <button class="linkbtn" data-a="hopen" data-i="'+i+'">Abrir</button> <button class="linkbtn" data-a="hdel" data-i="'+i+'">Borrar</button></td></tr>'; });
 o+='</tbody></table>';
 var agg={}; H.forEach(function(h){ (h.freq||[]).forEach(function(f){ agg[f[0]]=(agg[f[0]]||0)+f[1]; }); });
 var ag=Object.keys(agg).sort(function(a,b){return agg[b]-agg[a];});
 if(ag.length) o+='<p><b>Errores que más se repiten:</b> '+ag.slice(0,6).map(function(k){return catName(k)+' ('+agg[k]+')';}).join(' · ')+'</p>';
 o+='<div class="row"><button class="btn" data-a="histpdf">PDF del historial de '+esc(sel)+'</button></div></div>';
 return o+backup();
}
function backup(){ return '<div class="card"><h4>Copia de seguridad</h4><p class="small muted">El historial vive en este navegador. Descarga una copia de vez en cuando; si cambias de ordenador, la recuperas con «Cargar copia».</p><div class="row"><button class="btn" data-a="export">Descargar copia</button><label class="btn">Cargar copia<input type="file" id="imp" accept=".json" hidden></label></div></div>'; }
function histPrint(name){
 var H=HIST.filter(function(h){return h.name===name;});
 var o='<div class="printdoc"><h4>HISTORIAL DE PRUEBAS ORALES · '+esc(name)+'</h4><table class="sem"><thead><tr><th>Fecha</th><th>Examen</th><th>Nota /25</th><th>Holística</th>'+LV.crit.map(function(c){return '<th>'+c.n+'</th>';}).join('')+'</tr></thead><tbody>';
 H.forEach(function(h){ o+='<tr><td>'+esc(h.fecha)+'</td><td>'+esc(h.examen)+'</td><td>'+(h.nota==null?'-':String(h.nota).replace('.',','))+'</td><td>'+(h.hol==null?'-':h.hol)+'</td>'+LV.crit.map(function(c){ return '<td>'+(h.cm?dec(h.cm[c.k]):'-')+'</td>'; }).join('')+'</tr>'; });
 o+='</tbody></table>';
 H.forEach(function(h){ o+='<hr>'+(h.html||''); });
 return o+'</div>';
}
function snapshot(){
 var cm={}; LV.crit.forEach(function(c){ cm[c.k]=cmean(c.k); });
 return {id:E.id||String(Date.now()), name:E.name.trim(), fecha:E.fecha, examen:D.examen, nota:nota(), hol:E.hol, cm:cm, nerr:errs().length, freq:freq(), html:printHtml(E,'prof'), ev:JSON.parse(JSON.stringify(E))};
}

/* ---------- render y acciones ---------- */
function render(){
 var tab=E.tab, body = tab==='inf'?vInforme():(tab==='his'?vHist():vTask(+tab));
 $('app').innerHTML=head()+body; swAll();
}
function printNow(html){ var p=$('print'); p.innerHTML=html; document.body.classList.add('printing'); window.print(); setTimeout(function(){ document.body.classList.remove('printing'); },500); }
function copyText(t, okEl){ function ok(){ if(okEl){ okEl.hidden=false; okEl.textContent='\u2713 Copiado'; } }
 function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); try{ document.execCommand('copy'); ok(); }catch(e){} document.body.removeChild(ta); }
 if(navigator.clipboard&&window.isSecureContext) navigator.clipboard.writeText(t).then(ok,fb); else fb(); }
function addLog(n,c){ var d=$('dijo').value.trim(); if(!d){ $('dijo').focus(); return false; } E.log.push({n:n,c:c,dijo:d,corr:$('corr').value.trim()}); if(c!=='vocab'&&c!=='bien') E.lastCat=c; return true; }
document.addEventListener('click', function(e){
 var b=e.target.closest('[data-a]'); if(!b) return; var a=b.getAttribute('data-a'), n=+b.getAttribute('data-n');
 if(a==='tab'){ var t=b.getAttribute('data-t'); E.tab = (t==='inf'||t==='his')?t:+t; }
 else if(a==='copycode'){ copyText(D.codigo, $('ccok')); return; }
 else if(a==='op'){ E.t[n].op=+b.getAttribute('data-i'); }
 else if(a==='ck'){ var i=b.getAttribute('data-i'), v=+b.getAttribute('data-v'); if(E.t[n].ck[i]===v) delete E.t[n].ck[i]; else E.t[n].ck[i]=v; }
 else if(a==='sc'){ var k=b.getAttribute('data-k'), v2=+b.getAttribute('data-v'); if(E.t[n].sc[k]===v2) delete E.t[n].sc[k]; else E.t[n].sc[k]=v2; }
 else if(a==='hol'){ var v3=+b.getAttribute('data-v'); E.hol = E.hol===v3?null:v3; }
 else if(a==='tal'){ var kk=b.getAttribute('data-k'); E.t[n].tal[kk]=Math.max(0,(E.t[n].tal[kk]||0)+(+b.getAttribute('data-d'))); }
 else if(a==='add'){ if(!addLog(n,b.getAttribute('data-c'))) return; save(); render(); $('dijo').focus(); return; }
 else if(a==='del'){ E.log.splice(+b.getAttribute('data-i'),1); E.pick={}; }
 else if(a==='pick'){ var pi=b.getAttribute('data-i'); E.pick[pi]=!E.pick[pi]; }
 else if(a==='cat'){ var ck=b.getAttribute('data-k'); E.cats[ck]=!E.cats[ck]; }
 else if(a==='copyrep'){ copyText(studentText(), $('repok')); return; }
 else if(a==='print'){ printNow(printHtml(E, b.getAttribute('data-m'))); return; }
 else if(a==='guardar'){ if(!E.name.trim()){ alert('Escribe el nombre del estudiante antes de guardar.'); $('ename').focus(); return; }
  if(!confirm('¿Guardar la evaluación de '+E.name+' en el historial y dejar la libreta limpia?')) return;
  var s=snapshot(), ix=-1; HIST.forEach(function(h,i){ if(h.id===s.id) ix=i; }); if(ix>-1) HIST[ix]=s; else HIST.push(s);
  saveJ(KEY_ALL,HIST); var nm=E.name; E=blank(); E.histSel=nm; E.tab='his'; restoreSW(); }
 else if(a==='hpdf'){ printNow(HIST[+b.getAttribute('data-i')].html); return; }
 else if(a==='hopen'){ var h=HIST[+b.getAttribute('data-i')]; if(h.examen!==D.examen){ alert('Esta evaluación es del examen '+h.examen+'. Ábrela desde la libreta de ese examen.'); return; } if(!confirm('¿Abrir esta evaluación para corregirla? Lo que tengas ahora en la libreta se perderá si no lo has guardado.')) return; E=JSON.parse(JSON.stringify(h.ev)); E.id=h.id; E.tab='inf'; restoreSW(); }
 else if(a==='hdel'){ var hi=+b.getAttribute('data-i'); if(!confirm('¿Borrar del historial la evaluación de '+HIST[hi].name+' ('+HIST[hi].fecha+')?')) return; HIST.splice(hi,1); saveJ(KEY_ALL,HIST); }
 else if(a==='histpdf'){ printNow(histPrint(E.histSel||$('hsel').value)); return; }
 else if(a==='export'){ var blob=new Blob([JSON.stringify({historial:HIST},null,1)],{type:'application/json'}); var u=URL.createObjectURL(blob), l=document.createElement('a'); l.href=u; l.download='historial_orales_'+new Date().toISOString().slice(0,10)+'.json'; document.body.appendChild(l); l.click(); l.remove(); setTimeout(function(){URL.revokeObjectURL(u);},1000); return; }
 else return;
 save(); render();
});
document.addEventListener('keydown', function(e){ if(e.key==='Enter' && (e.target.id==='dijo'||e.target.id==='corr')){ e.preventDefault(); if(addLog(+E.tab, E.lastCat)){ save(); render(); $('dijo').focus(); } } });
document.addEventListener('input', function(e){ var t=e.target;
 if(t.id==='ename'){ E.name=t.value; save(); }
 var f=t.getAttribute('data-f'); if(f){ if(f==='nota') E.t[+t.getAttribute('data-n')].nota=t.value; else E[f]=t.value; save(); } });
document.addEventListener('change', function(e){ var t=e.target;
 if(t.id==='hsel'){ E.histSel=t.value; save(); render(); }
 if(t.id==='imp' && t.files[0]){ var r=new FileReader(); r.onload=function(){ try{ var j=JSON.parse(r.result).historial||[]; var ids={}; HIST.forEach(function(h){ids[h.id]=1;}); var nuevos=j.filter(function(h){return !ids[h.id];}); HIST=HIST.concat(nuevos); saveJ(KEY_ALL,HIST); alert('Copia cargada: '+nuevos.length+' evaluaciones nuevas.'); render(); }catch(err){ alert('Ese archivo no es una copia válida.'); } }; r.readAsText(t.files[0]); } });
restoreSW(); render();
})();
"""

def _ul(items): return "<ul class='mini'>" + "".join("<li>%s</li>" % x for x in items) + "</ul>"

def tareas_b2(oral):
    t1, t2, t3 = oral["t1"], oral["t2"], oral["t3"]
    return [
     {"n": 1, "name": "Tarea 1 · Valorar propuestas", "dur": "6-7 min",
      "opts": [{"title": o["title"], "lamina": "<p class='small'>%s</p>" % o["situacion"] + _ul(o["propuestas"]), "ent": o.get("ent", [])} for o in t1["ops"]],
      "phases": [["mono", "Monólogo", 3, 4], ["conv", "Conversación", 2, 3]],
      "checks": ["Habla de al menos cuatro propuestas", "Da ventajas e inconvenientes", "Justifica sus opiniones con argumentos o ejemplos", "Compara propuestas o propone alternativas", "En la conversación, defiende y matiza su postura"],
      "ayudas": ["¿Y esta propuesta, qué le parece? (señale una que no haya comentado)", "¿A quién beneficiaría? ¿A quién perjudicaría?", "¿Qué problema podría causar?"]},
     {"n": 2, "name": "Tarea 2 · Describir una situación", "dur": "5-6 min",
      "opts": [{"title": f["title"], "lamina": "<p class='small'>%s</p>" % f["desc"] + _ul(f["preguntas"]), "ent": f.get("ent", [])} for f in t2["fotos"]],
      "phases": [["mono", "Descripción", 2, 3], ["conv", "Conversación", 2, 3]],
      "checks": ["Describe a las personas, el lugar y lo que ocurre", "Formula hipótesis (creo que, puede que, debe de, estará...)", "Imagina lo que ha pasado antes y lo que pasará después", "Habla de sentimientos y relaciones", "En la conversación, relaciona el tema con su experiencia"],
      "ayudas": ["¿Qué cree que ha pasado antes?", "¿Cómo cree que se sienten?", "¿Qué cree que va a pasar después?"]},
     {"n": 3, "name": "Tarea 3 · Opinar sobre una encuesta", "dur": "3-4 min",
      "opts": [{"title": o["title"], "lamina": _ul(["<b>%s.</b> %s" % ("ABCDEF"[i], q["q"]) for i, q in enumerate(o["preguntas"])]) + "<table class='mini-t'>" + "".join("<tr><td>%s</td><td><b>%s</b></td></tr>" % (r[0], r[1]) for r in o["resultados"]["filas"]) + "</table>", "ent": o.get("ent", [])} for o in t3["ops"]],
      "phases": [["conv", "Conversación", 3, 4]],
      "checks": ["Responde a la encuesta y justifica sus respuestas", "Compara sus respuestas con los resultados", "Valora los datos (sorpresa, acuerdo, desacuerdo)", "Da posibles causas o explica las diferencias"],
      "ayudas": ["¿Por qué ha elegido esa respuesta?", "¿Le sorprende este dato?", "¿Por qué cree que la mayoría piensa así?"]}]

def _trozos(guion):
    """Reparte el GUION_ENTREVISTADOR de A2 por tareas (bloques que empiezan por 'Tarea N')."""
    out, cur = {}, None
    for l in (guion or "").split("\n"):
        m = re.match(r"\s*Tarea (\d)", l)
        if m: cur = int(m.group(1))
        elif re.match(r"\s*Qué mirar", l): cur = "mirar"
        if cur is not None: out.setdefault(cur, []).append(l.strip())
    return {k: "\n".join(v) for k, v in out.items()}

def tareas_a2(oral, guion=None):
    t1, t2, t3 = oral["t1"], oral["t2"], oral["t3"]
    g = _trozos(guion)
    return [
     {"n": 1, "name": "Tarea 1 · Monólogo", "dur": "2-3 min · sin intervención del entrevistador", "guion": g.get(1, ""),
      "guionTitle": "Solo si se bloquea o se queda muy corto",
      "opts": [{"title": o["title"], "lamina": _ul(o["pautas"])} for o in t1["ops"]],
      "phases": [["mono", "Monólogo", 2, 3]],
      "checks": ["Habla de todas o casi todas las pautas", "Ordena lo que dice (empieza, desarrolla, termina)", "Da ejemplos o detalles personales", "Habla sin necesitar ayuda del entrevistador"],
      "ayudas": ["¿Y qué más puede decir de...? (una pauta que no haya tocado)", "¿Por qué?", "¿Puede darme un ejemplo?"]},
     {"n": 2, "name": "Tarea 2 · Descripción de una fotografía", "dur": "2-3 min · sin intervención del entrevistador", "guion": g.get(2, ""),
      "guionTitle": "Solo si se bloquea o se queda muy corto",
      "opts": [{"title": f["title"], "lamina": "<p class='small'>%s</p>" % f["desc"] + _ul(t2.get("pautas", []))} for f in t2["fotos"]],
      "phases": [["mono", "Descripción", 2, 3]],
      "checks": ["Describe a las personas (cómo son, ropa, qué hacen)", "Describe el lugar y las cosas", "Imagina qué piensan o qué va a pasar", "Habla sin necesitar ayuda del entrevistador"],
      "ayudas": ["¿Qué ropa lleva?", "¿Dónde cree que están?", "¿Qué van a hacer después?"]},
     {"n": 3, "name": "Tarea 3 · Diálogo en una situación", "dur": "3-4 min · aquí sí interviene el entrevistador", "guion": g.get(3, ""),
      "guionTitle": "Su papel en el diálogo",
      "opts": [{"title": o["title"], "lamina": "<p class='small'>%s</p>" % o["intro"] + _ul(o["pautas"])} for o in t3["ops"]],
      "phases": [["conv", "Diálogo", 3, 4]],
      "checks": ["Saluda y se despide", "Cumple todas las pautas de la situación", "Pregunta y reacciona a lo que dice el entrevistador", "Usa tú o usted según la situación"],
      "ayudas": ["¿Qué necesita?", "¿Algo más?", "(Haga una pregunta que le obligue a reaccionar)"]}], g.get("mirar", "")

def _enc_html(s): return "".join(c if ord(c) < 128 else "&#x%X;" % ord(c) for c in s)
def _enc_js(s):
    out = []
    for c in s:
        o = ord(c)
        if o < 128: out.append(c)
        elif o <= 0xFFFF: out.append("\\u%04X" % o)
        else:
            o -= 0x10000; out.append("\\u%04X\\u%04X" % (0xD800 + (o >> 10), 0xDC00 + (o & 0x3FF)))
    return "".join(out)

def build(level, examen, codigo, title, oral, cats, base_css, guion=None, errores=None):
    """Devuelve el HTML de la libreta oral de la profesora."""
    if level == "B2":
        tasks, mirar = tareas_b2(oral), ""
    else:
        tasks, mirar = tareas_a2(oral, guion)
    err = "\n".join(x for x in [mirar, (errores or "").strip()] if x).strip()
    data = {"level": level, "examen": examen, "codigo": codigo, "title": title, "tasks": tasks,
            "cats": {k: {"name": v["name"], "repaso": v.get("repaso", "")} for k, v in cats.items()}, "errores": err}
    js = JS.replace("__DATA__", json.dumps(data, ensure_ascii=True)).replace("__LEVELS__", json.dumps(LEVELS, ensure_ascii=True))
    body = ('<header class="top"><div class="top-in"><div class="brand"><div><h1 style="font-size:1.3rem;margin:0">' + title +
            ' · Oral</h1><small>Libreta de la profesora · ' + examen + ' · no compartir</small></div></div></div></header>'
            '<main class="wrap" id="app"></main><div id="print"></div>')
    return ('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="robots" content="noindex, nofollow">\n<title>' + _enc_html(title + ' · Oral · Profesora') + '</title>\n'
            '<style>' + _enc_html(base_css + CSS) + '</style>\n</head>\n<body>\n' + _enc_html(body) +
            '<script>\n' + _enc_js(js) + '\n</script>\n</body>\n</html>\n')
