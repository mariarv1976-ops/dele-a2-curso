# -*- coding: utf-8 -*-
# MODULO 0 DEL CURSO DE PREPARACION DELE A2: CONOCE EL EXAMEN
# Uso: python3 build_M0.py  -> DELEA2_curso_M0_conoce_el_examen.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# 12/10/2026: regla de oro 7 matizada para que diga lo mismo que la escala oficial (y que M3-3 y M3-5): una pauta que
# falta te deja en el limite; dos (o una que falta y otra a medias), banda 1.
import json
from curso_comun import CSS, EMAIL, page

TITLE = "Conoce el examen DELE A2"
FILE = "DELEA2_curso_M0_conoce_el_examen.html"
STORAGE = "dele-a2-curso-M0"

CSS_M0 = CSS + r"""
.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin:18px 0}
.pc{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;border-top:5px solid var(--coral)}
.pc .k{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.pc h3{margin:2px 0 6px}
.pc .big{font-family:Georgia,serif;font-size:1.6rem;font-weight:700;line-height:1.1}
.pc .big span{font-family:system-ui,sans-serif;font-size:.9rem;font-weight:400;color:var(--muted)}
.pc ul{margin:8px 0 0;padding-left:1.1em;font-size:.95rem}
.grp{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:16px 0}
.grp div{border:2px solid var(--ink);border-radius:12px;padding:14px 16px;background:#fff}
.grp b{font-family:Georgia,serif;font-size:1.1rem;display:block;margin-bottom:4px}
.calc{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin:16px 0}
.calc .ln{display:grid;grid-template-columns:9.5em 1fr 6.5em;gap:10px;align-items:center;margin:8px 0}
.calc input[type=range]{width:100%;accent-color:var(--coral)}
.calc .val{font-variant-numeric:tabular-nums;text-align:right;font-weight:600}
.calc h4{margin:14px 0 4px}
.verdict{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.verdict div{border-radius:10px;padding:10px 14px;font-weight:600}
.verdict .ok{background:var(--ok-soft);color:var(--ok)}.verdict .no{background:var(--bad-soft);color:var(--bad)}
.final{margin-top:10px;border-radius:10px;padding:10px 14px;font-weight:700;text-align:center}
.final.ok{background:var(--ok);color:#fff}.final.no{background:var(--bad);color:#fff}
.check{list-style:none;padding:0;margin:8px 0}
.check li{padding:6px 0 6px 30px;position:relative;border-bottom:1px dashed var(--line)}
.check li:before{content:"";position:absolute;left:4px;top:11px;width:14px;height:14px;border:2px solid var(--ink);border-radius:3px}
.bubbles{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin:8px 0}
.bb{display:inline-flex;align-items:center;gap:6px;font-size:.92rem}
.bb i{display:inline-block;width:22px;height:22px;border-radius:50%;border:2px solid var(--ink)}
.bb i.f{background:var(--ink)}.bb i.h{background:linear-gradient(90deg,var(--ink) 50%,#fff 50%)}
.bb i.x{position:relative}.bb i.x:after{content:"";position:absolute;left:3px;right:3px;top:8px;height:2px;background:var(--ink);transform:rotate(45deg)}
.rule{display:grid;grid-template-columns:52px 1fr;gap:14px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:12px 0}
.rule .num{font-family:Georgia,serif;font-size:2rem;font-weight:700;color:var(--coral);line-height:1}
.rule h3{margin:0 0 4px}
.rule .why{margin:6px 0 0;font-size:.95rem}
.rule .ex{margin-top:8px;background:var(--paper);border-radius:8px;padding:8px 12px;font-size:.93rem}
.rule .ex b{font-size:.8rem;letter-spacing:.05em;color:var(--muted)}
.ok-w{color:var(--ok);font-weight:600}.no-w{color:var(--bad);font-weight:600;text-decoration:line-through}
.vf{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:12px 0}
.vf .st{font-weight:600}
.vf .st .num{color:var(--coral);font-family:Georgia,serif;margin-right:6px}
.vf .bt{display:flex;gap:10px;margin-top:8px}
.vf .bt button{font:inherit;font-weight:600;border:2px solid var(--ink);background:#fff;border-radius:999px;padding:5px 18px;cursor:pointer}
.vf .bt button:disabled{cursor:default}
.vf .bt button.sel.good{background:var(--ok);border-color:var(--ok);color:#fff}
.vf .bt button.sel.bad{background:var(--bad);border-color:var(--bad);color:#fff}
.vf .fb{margin-top:8px;border-radius:8px;padding:8px 12px;font-size:.95rem}
.vf .fb.good{background:var(--ok-soft)}.vf .fb.bad{background:var(--bad-soft)}
.prog{height:8px;background:var(--line);border-radius:99px;overflow:hidden;margin:6px 0 14px}
.prog i{display:block;height:100%;background:var(--coral);width:0}
.score{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:16px 18px;margin:18px 0}
.score b.big{font-family:Georgia,serif;font-size:2rem}
.scale{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.scale label{cursor:pointer}
.scale input{position:absolute;opacity:0}
.scale span{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;border:2px solid var(--line);background:#fff;font-weight:700}
.scale input:checked + span{background:var(--ink);border-color:var(--ink);color:#fff}
.scale input:focus-visible + span{outline:3px solid var(--cta);outline-offset:2px}
.opn label.q{display:block;font-weight:600;margin:18px 0 6px}
.opn textarea{width:100%;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;min-height:80px;background:#fff}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips label{border:2px solid var(--line);border-radius:999px;padding:5px 14px;cursor:pointer;background:#fff}
.chips label:has(input:checked){border-color:var(--ink);background:var(--ink);color:#fff}
.chips input{position:absolute;opacity:0}
.sendbox{border:2px solid var(--coral);border-radius:12px;padding:18px 22px;margin:26px 0;background:#fff}
.sendbox input[type=text]{width:100%;max-width:360px;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 12px;margin-top:6px}
@media (max-width:600px){.cards,.grp,.verdict{grid-template-columns:1fr}.calc .ln{grid-template-columns:1fr 5.5em}.calc .ln label{grid-column:1 / -1}.rule{grid-template-columns:1fr;gap:4px}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.rule{break-inside:avoid}}
"""

# ------------------------------------------------------------------ CONTENIDO
STEPS = [
    ("examen", "El examen"),
    ("aprobar", "Cómo se aprueba"),
    ("dia", "El día del examen"),
    ("reglas", "Reglas de oro"),
    ("test", "Test"),
    ("opinion", "Tu opinión"),
]

V_EXAMEN = """
<h2>El examen en un vistazo</h2>
<p class="lead">El DELE A2 tiene cuatro pruebas. En total son 13 tareas, y cada tarea es siempre igual: el mismo tipo de texto, el mismo número de preguntas y la misma numeración. Si conoces las tareas, el día del examen no hay sorpresas.</p>
<div class="cards">
 <div class="pc"><div class="k">PRUEBA 1</div><h3>Comprensión de lectura</h3><div class="big">60 min <span>· 4 tareas · 25 preguntas</span></div><ul><li>Lees textos y eliges la opción correcta (A, B o C).</li></ul></div>
 <div class="pc"><div class="k">PRUEBA 2</div><h3>Comprensión auditiva</h3><div class="big">40 min <span>· 4 tareas · 25 preguntas</span></div><ul><li>Escuchas cada audio <b>dos veces</b>.</li><li>El audio no se para: las pausas ya están dentro.</li></ul></div>
 <div class="pc"><div class="k">PRUEBA 3</div><h3>Expresión e interacción escritas</h3><div class="big">45 min <span>· 2 tareas</span></div><ul><li>Tarea 1: 60-70 palabras.</li><li>Tarea 2: 70-80 palabras (eliges una de dos opciones).</li></ul></div>
 <div class="pc"><div class="k">PRUEBA 4</div><h3>Expresión e interacción orales</h3><div class="big">12 min <span>· 3 tareas</span></div><ul><li>Antes tienes 12 minutos para prepararte.</li><li>Hablas con un examinador; otro escucha y pone la nota.</li></ul></div>
</div>
<div class="tip">Normalmente, la lectura, la auditiva y la escritura se hacen seguidas, el mismo día (unas dos horas y media). La oral puede ser ese día o en otra fecha: el centro de examen te dice el día y la hora.</div>

<h3>Las 13 tareas, una por una</h3>
<p class="muted small">Toca cada prueba para ver sus tareas. El tiempo de la lectura es una recomendación para repartir los 60 minutos.</p>
<details><summary>Prueba 1 · Lectura · 60 minutos</summary>
<table class="t"><thead><tr><th>Tarea</th><th>Qué lees</th><th>Preguntas</th><th>Tiempo</th></tr></thead><tbody>
<tr><td><b>1</b></td><td>Un correo o un mensaje personal (unas 250-300 palabras).</td><td class="mono">1-5</td><td>12 min</td></tr>
<tr><td><b>2</b></td><td>Ocho anuncios o textos cortos (carteles, avisos, folletos), más un ejemplo resuelto.</td><td class="mono">6-13</td><td>15 min</td></tr>
<tr><td><b>3</b></td><td>Tres personas (A, B, C) hablan del mismo tema. Tienes que decir quién dice cada cosa.</td><td class="mono">14-19</td><td>13 min</td></tr>
<tr><td><b>4</b></td><td>Un texto más largo: un blog, una biografía, una noticia... (unas 375-425 palabras).</td><td class="mono">20-25</td><td>18 min</td></tr>
</tbody></table></details>
<details><summary>Prueba 2 · Auditiva · 40 minutos</summary>
<table class="t"><thead><tr><th>Tarea</th><th>Qué escuchas</th><th>Preguntas</th></tr></thead><tbody>
<tr><td><b>1</b></td><td>Seis conversaciones cortas (más un ejemplo). Para cada una eliges una de tres <b>imágenes</b>.</td><td class="mono">1-6</td></tr>
<tr><td><b>2</b></td><td>Seis anuncios o noticias de la radio (más un ejemplo).</td><td class="mono">7-12</td></tr>
<tr><td><b>3</b></td><td>Una conversación entre dos amigos. Para cada frase decides: la dice él (A), ella (B) o ninguno de los dos (C).</td><td class="mono">13-18</td></tr>
<tr><td><b>4</b></td><td>Ocho mensajes cortos (megafonía, contestador...), con el ejemplo. Hay once frases (A-K): usas siete y sobran tres.</td><td class="mono">19-25</td></tr>
</tbody></table>
<p class="small muted">Antes de cada audio tienes unos segundos para leer las preguntas. Después de cada tarea, unos segundos para pasar las respuestas a la hoja.</p></details>
<details><summary>Prueba 3 · Escritura · 45 minutos</summary>
<table class="t"><thead><tr><th>Tarea</th><th>Qué escribes</th><th>Palabras</th><th>Tiempo</th></tr></thead><tbody>
<tr><td><b>1</b></td><td>Respondes a un correo o a un mensaje corto. La instrucción te dice 4 o 5 cosas que tienes que hacer (saludar, contar, proponer, preguntar, despedirte...).</td><td class="mono">60-70</td><td>20 min</td></tr>
<tr><td><b>2</b></td><td>Eliges <b>una</b> opción. Opción 1: un texto sobre tu vida (una fiesta, unas vacaciones, un cambio...). Opción 2: un texto a partir de fotos o datos (la vida de una persona, un viaje...).</td><td class="mono">70-80</td><td>25 min</td></tr>
</tbody></table>
<p class="small muted">En los 45 minutos, guarda 5 para revisar los dos textos.</p></details>
<details><summary>Prueba 4 · Oral · 12 minutos + 12 de preparación</summary>
<table class="t"><thead><tr><th>Tarea</th><th>Qué haces</th><th>Tiempo</th></tr></thead><tbody>
<tr><td><b>1</b></td><td>Monólogo: eliges uno de dos temas de tu vida (una persona importante, tu plato favorito, un viaje...) y hablas tú solo.</td><td>2-3 min</td></tr>
<tr><td><b>2</b></td><td>Describes una fotografía (eliges una de dos): las personas, el lugar, qué hacen, qué sienten...</td><td>2-3 min</td></tr>
<tr><td><b>3</b></td><td>Conversación con el examinador en una situación relacionada con la foto (planificar algo con un amigo, comprar en una tienda...).</td><td>3-4 min</td></tr>
</tbody></table>
<p class="small muted">Al empezar, el examinador te hace unas preguntas sencillas para conocerte y que estés tranquilo.</p></details>
<div class="row"><button class="btn cta" data-go="aprobar">Siguiente: cómo se aprueba</button></div>
"""

V_APROBAR = """
<h2>Cómo se aprueba</h2>
<p class="lead">Cada prueba vale 25 puntos. Pero no se suma todo junto: las cuatro pruebas van en <b>dos grupos</b>, y necesitas <b>30 de 50 puntos en cada grupo</b>.</p>
<div class="grp">
 <div><b>Grupo 1</b>Lectura (25) + Escritura (25)<br><span class="muted">Mínimo: 30 de 50</span></div>
 <div><b>Grupo 2</b>Auditiva (25) + Oral (25)<br><span class="muted">Mínimo: 30 de 50</span></div>
</div>
<div class="note"><b>Muy importante:</b> un grupo muy bueno <b>no salva</b> al otro. Con 45 puntos en el grupo 1 y 28 en el grupo 2, el resultado es <b>no apto</b>. Dentro del mismo grupo, en cambio, sí: una buena lectura puede ayudar a una escritura floja.</div>

<h3>Lectura y auditiva: 1 punto por pregunta</h3>
<p>Cada acierto vale 1 punto. Un error vale 0: <b>no te quitan puntos</b>. Por eso nunca debes dejar una pregunta en blanco.</p>

<h3>Escritura y oral: bandas de 0 a 3</h3>
<p>Los examinadores te dan una nota de 0 a 3 en dos aspectos: cómo usas la lengua (gramática, vocabulario, orden del texto) y si haces bien la tarea (todo lo que pide la instrucción, la extensión, el tipo de texto).</p>
<table class="t"><tbody>
<tr><td class="mono"><b>3</b></td><td>Mejor que A2</td><td class="mono">25 puntos</td></tr>
<tr><td class="mono"><b>2</b></td><td><b>Es un A2: aprobado</b></td><td class="mono">16,67 puntos</td></tr>
<tr><td class="mono"><b>1</b></td><td>Todavía no es un A2</td><td class="mono">8,33 puntos</td></tr>
<tr><td class="mono"><b>0</b></td><td>No hay muestra suficiente</td><td class="mono">0 puntos</td></tr>
</tbody></table>
<div class="tip"><b>La cuenta que tienes que recordar:</b> si en la escritura sacas un 2 (16,67 puntos), en la lectura necesitas solo <b>14 aciertos de 25</b> para llegar a 30. Lo mismo con la oral y la auditiva. Pero si sacas un 1, necesitas 22 aciertos: casi perfecto. Por eso la escritura y la oral son tan importantes.</div>

<h3>Calcula tu resultado</h3>
<p class="muted">Mueve los controles y mira qué pasa con cada grupo.</p>
<div class="calc" id="calc">
 <h4>Grupo 1</h4>
 <div class="ln"><label for="cL">Lectura (aciertos)</label><input type="range" id="cL" min="0" max="25" step="1" value="17"><span class="val" id="vL"></span></div>
 <div class="ln"><label for="cE">Escritura (banda)</label><input type="range" id="cE" min="0" max="3" step="0.5" value="2"><span class="val" id="vE"></span></div>
 <h4>Grupo 2</h4>
 <div class="ln"><label for="cA">Auditiva (aciertos)</label><input type="range" id="cA" min="0" max="25" step="1" value="12"><span class="val" id="vA"></span></div>
 <div class="ln"><label for="cO">Oral (banda)</label><input type="range" id="cO" min="0" max="3" step="0.5" value="2"><span class="val" id="vO"></span></div>
 <div class="verdict" aria-live="polite"><div id="g1"></div><div id="g2"></div></div>
 <div class="final" id="gf" aria-live="polite"></div>
</div>
<div class="row"><button class="btn cta" data-go="dia">Siguiente: el día del examen</button></div>
"""

V_DIA = """
<h2>El día del examen</h2>
<h3>Qué tienes que llevar</h3>
<ul class="check">
 <li>Tu <b>documento de identidad original</b> (pasaporte, DNI, NIE...): el mismo que usaste en la inscripción.</li>
 <li>La <b>convocatoria</b> del examen (el centro te la envía antes).</li>
 <li><b>Lápiz del número 2</b>, goma de borrar y sacapuntas, para las hojas de respuestas de la lectura y la auditiva.</li>
 <li><b>Bolígrafo</b> para la escritura.</li>
 <li>Un reloj sencillo (no de móvil ni inteligente) te ayuda a controlar el tiempo, si en la sala no hay uno a la vista.</li>
</ul>
<p class="muted small">No puedes usar el móvil ni el diccionario. Llega con tiempo: si llegas tarde, puedes perder la prueba.</p>

<h3>La hoja de respuestas</h3>
<p>En la lectura y la auditiva tienes dos papeles: el <b>cuadernillo</b> (con los textos y las preguntas) y la <b>hoja de respuestas</b>. Solo cuenta lo que marcas en la hoja de respuestas. Lo que escribes en el cuadernillo no lo corrige nadie.</p>
<div class="bubbles"><span class="bb"><i class="f"></i> Así: rellena el círculo entero</span><span class="bb"><i class="h"></i> Así no</span><span class="bb"><i class="x"></i> Así no</span></div>
<p class="small">Si te equivocas, borra bien con la goma y marca la otra opción. Al principio de cada prueba escribes tus datos y tu código de inscripción en la hoja.</p>
<ul>
 <li><b>Lectura:</b> no te dan tiempo extra para pasar las respuestas. Pásalas a la hoja al terminar cada tarea, no al final de todo.</li>
 <li><b>Auditiva:</b> después de cada tarea, el audio dice <i>"Complete ahora la Hoja de respuestas"</i> y tienes unos segundos.</li>
 <li><b>Escritura:</b> puedes hacer un borrador, pero tu texto final va en la hoja de respuestas, con bolígrafo y con letra clara. El borrador no se corrige.</li>
</ul>

<h3>La prueba oral</h3>
<ul>
 <li>Primero vas a una sala para <b>preparar las tres tareas durante 12 minutos</b>. Puedes escribir notas y un esquema.</li>
 <li>Después entras en otra sala con <b>dos examinadores</b>. Uno habla contigo; el otro solo escucha y pone la nota.</li>
 <li>Al empezar, te hacen unas preguntas fáciles para conocerte (cómo te llamas, de dónde eres...). Sirven para que estés tranquilo.</li>
 <li>Puedes <b>mirar tus notas</b>, pero no leerlas en voz alta: tienes que hablar.</li>
</ul>

<h3>Después del examen</h3>
<p>Los resultados salen <b>entre uno y tres meses</b> después, en la web oficial de los diplomas. Ves los puntos de cada prueba y de cada grupo. El diploma DELE <b>no caduca</b>: es para toda la vida.</p>
<div class="row"><button class="btn cta" data-go="reglas">Siguiente: las 10 reglas de oro</button></div>
"""

RULES = [
  ("Necesitas 30 de 50 en cada grupo",
   "Lectura y escritura van juntas; auditiva y oral, también. Si un grupo no llega a 30, no apruebas, aunque el otro sea perfecto. Entrena más tu grupo débil.",
   None),
  ("Nunca dejes una pregunta en blanco",
   "Una respuesta mal vale 0, lo mismo que una pregunta sin contestar. Si marcas algo, tienes una posibilidad entre tres de acertar.",
   None),
  ("Primero las preguntas, después el texto o el audio",
   "Si lees antes las preguntas, sabes qué información buscas. Así lees y escuchas con un objetivo.",
   None),
  ("Cuidado con las palabras repetidas",
   "La opción que copia palabras exactas del texto suele ser la trampa. La correcta dice lo mismo con otras palabras.",
   'El texto dice: <i>"No hace falta reservar: puedes venir directamente."</i><br>A) <span class="no-w">Hay que reservar antes.</span> (repite "reservar", pero es falso)<br>B) <span class="ok-w">Puedes ir sin reserva.</span> (otras palabras, misma idea)'),
  ("Atención a los cambios de plan y a quién hace cada cosa",
   "En los textos y los audios la gente cambia de idea y habla de otras personas. Busca lo que pasa <b>al final</b> y quién lo hace.",
   '<i>"Iba a ir al cine con Ana, pero al final me quedé en casa. Ana sí fue."</i><br>¿Quién fue al cine? <span class="ok-w">Ana.</span> ¿Y él? <span class="ok-w">Se quedó en casa.</span>'),
  ("Controla el reloj",
   "En la lectura: unos 12-15 minutos para cada una de las tres primeras tareas y 18 para la última. Si una pregunta te bloquea, marca una opción y sigue: si te sobra tiempo, vuelves.",
   None),
  ("Escritura: cada pauta, al menos una frase",
   "La instrucción te dice qué tienes que hacer (saludar, contar, proponer, preguntar...). Un texto sencillo que hace todo aprueba. Si falta una pauta, te quedas en el límite, aunque tus frases sean difíciles; si faltan dos (o falta una y otra está a medias), ya no es un A2.",
   None),
  ("Escritura: tú o usted, del principio al final, y 5 minutos para revisar",
   "Si saludas con tú (<i>Hola, Marta</i>), sigue con tú hasta la despedida. En los últimos 5 minutos revisa: pautas, tú o usted, pasados, masculino y femenino, singular y plural, conectores y número de palabras (unas 10 palabras por línea).",
   'Saludo con tú y despedida con usted: <span class="no-w">Hola, Pedro: ... Atentamente.</span><br>Mejor: <span class="ok-w">Hola, Pedro: ... Un abrazo.</span>'),
  ("Oral: palabras clave, no un texto de memoria",
   "En la preparación escribe palabras clave, no frases enteras. En la foto, describe lo que ves y sigue las 6 preguntas de la lámina en orden: las personas y su ropa, el lugar y los objetos, qué hacen, qué relación tienen, qué sienten y qué han hecho antes o van a hacer después.",
   None),
  ("Oral: nunca te quedes callado",
   "Si no sabes una palabra, descríbela. Si no entiendes, pide que te repitan. Para pensar, usa palabras como <i>pues</i>, <i>a ver</i>, <i>bueno</i>.",
   '<i>"¿Puede repetir, por favor?"</i> · <i>"No sé cómo se dice: es una cosa para abrir botellas."</i> · <i>"Pues... a ver..."</i>'),
]

def v_reglas():
    o = '<h2>Las 10 reglas de oro</h2><p class="lead">Diez ideas para el día del examen. Léelas ahora y vuelve a leerlas la semana antes.</p>'
    for i, (t, w, ex) in enumerate(RULES, 1):
        o += '<div class="rule"><div class="num">%d</div><div><h3>%s</h3><p class="why">%s</p>%s</div></div>' % (
            i, t, w, ('<div class="ex"><b>EJEMPLO</b><br>%s</div>' % ex) if ex else '')
    o += '<div class="row"><button class="btn" data-act="print">Imprimir las reglas</button><button class="btn cta" data-go="test">Siguiente: el test</button></div>'
    return o

# Test de verdadero o falso (estilo "gestion del examen"): v = True si es verdadero
TEST = [
 ("La prueba de lectura dura 60 minutos y tiene 25 preguntas.", True,
  "Correcto: 60 minutos, 4 tareas y 25 preguntas."),
 ("Si contestas mal una pregunta de lectura, te quitan puntos.", False,
  "Un error vale 0, como una pregunta en blanco. No te quitan nada: contesta siempre."),
 ("En la auditiva escuchas cada audio una sola vez.", False,
  "Escuchas cada audio dos veces. En la primera marca una respuesta; en la segunda, compruébala."),
 ("Si tienes 60 puntos de 100 en total, siempre apruebas.", False,
  "No: necesitas 30 de 50 en cada grupo. Con 40 en el grupo 1 y 20 en el grupo 2 tienes 60, pero no apruebas."),
 ("La lectura y la escritura van en el mismo grupo.", True,
  "Sí: grupo 1 = lectura + escritura. Grupo 2 = auditiva + oral."),
 ("Una lectura muy buena puede compensar una auditiva floja.", False,
  "No: están en grupos distintos. Un grupo no salva al otro."),
 ("Una auditiva muy buena puede ayudar si la oral no es muy buena.", True,
  "Sí, porque están en el mismo grupo: se suman las dos."),
 ("En la tarea 2 de la escritura eliges una de dos opciones.", True,
  "Sí. Lee las dos y elige la que te permite cumplir todas las pautas con más facilidad."),
 ("Si en la tarea 1 escribes 120 palabras en vez de 60-70, sacas más nota.", False,
  "No. Escribir mucho más no da puntos y aumenta los errores. Lo importante es hacer todas las pautas."),
 ("Lo que marcas en el cuadernillo de preguntas también cuenta para la nota.", False,
  "Solo cuenta la hoja de respuestas. Pasa tus respuestas a la hoja al terminar cada tarea."),
 ("En la auditiva, después de cada tarea, tienes unos segundos para pasar las respuestas a la hoja.", True,
  "Sí: el audio te dice \"Complete ahora la Hoja de respuestas\". Aprovecha esos segundos."),
 ("Antes de la oral tienes 12 minutos para preparar las tres tareas.", True,
  "Sí: 12 minutos de preparación y 12 minutos de prueba."),
 ("En la oral puedes leer en voz alta el texto que has preparado.", False,
  "Puedes mirar tus notas, pero no leerlas. Escribe palabras clave, no un texto entero."),
 ("En la tarea 2 de la oral tienes que hablar de tu vida.", False,
  "No: tienes que describir la foto (las personas, el lugar, qué hacen...). Hablar de tu vida es la tarea 1."),
 ("En la oral hay dos examinadores, pero solo uno habla contigo.", True,
  "Sí. El otro escucha y te pone la nota de cada tarea."),
 ("En la lectura, la respuesta correcta suele repetir las mismas palabras del texto.", False,
  "Al revés: la correcta suele decir lo mismo con otras palabras. La que repite palabras exactas suele ser la trampa."),
]

V_TEST = """
<h2>Test: ¿conoces el examen?</h2>
<p class="lead">16 frases sobre el DELE A2. ¿Verdadero o falso? Después de cada respuesta ves la explicación.</p>
<div class="prog" aria-hidden="true"><i id="tprog"></i></div>
<div id="tlist"></div>
<div id="tscore"></div>
"""

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo. Solo son cuatro preguntas.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué parte de esta página te ha sido más útil?</label>
 <div class="chips" role="group" aria-labelledby="o1l">
  <label><input type="radio" name="o1" value="El examen en un vistazo">El examen en un vistazo</label>
  <label><input type="radio" name="o1" value="Cómo se aprueba">Cómo se aprueba</label>
  <label><input type="radio" name="o1" value="El día del examen">El día del examen</label>
  <label><input type="radio" name="o1" value="Las reglas de oro">Las reglas de oro</label>
  <label><input type="radio" name="o1" value="El test">El test</label>
 </div>
 <label class="q" for="o2">2. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o2"></textarea>
 <label class="q" id="o3l">3. ¿Qué prueba del examen te preocupa más?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Lectura">Lectura</label>
  <label><input type="radio" name="o3" value="Auditiva">Auditiva</label>
  <label><input type="radio" name="o3" value="Escritura">Escritura</label>
  <label><input type="radio" name="o3" value="Oral">Oral</label>
 </div>
 <label class="q" id="o4l">4. Ahora que conoces el examen, ¿cuánto control sientes? (1 = nada, 10 = total)</label>
 <div class="scale" role="group" aria-labelledby="o4l" id="o4"></div>
</div>
<div class="sendbox">
 <h3>Envía tu opinión a tu profesora</h3>
 <label><b>Tu nombre</b><br><input type="text" id="sname" autocomplete="name"></label>
 <div class="row"><button class="btn cta" data-act="copy">Copiar</button></div>
 <div class="copied-box" id="cbox" role="status" hidden></div>
 <p class="muted small">Pégalo en un correo para tu profesora: __EMAIL__</p>
</div>
"""

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Módulo 0</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
"""

views = {"examen": V_EXAMEN, "aprobar": V_APROBAR, "dia": V_DIA, "reglas": v_reglas(),
         "test": V_TEST, "opinion": V_OPINION.replace("__EMAIL__", EMAIL)}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
body = BODY.replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

DATA = {"key": STORAGE, "steps": [{"id": k, "label": l} for k, l in STEPS],
        "test": [{"s": s, "v": v, "why": w} for s, v, w in TEST], "title": TITLE}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function blank(){ return {cur:'examen', seen:{}, t:{}, o1:'', o2:'', o3:'', o4:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }

/* ---- navegacion ---- */
function nav(){
 var o='';
 D.steps.forEach(function(st,i){
  var done = st.id==='test' ? testDone() : (st.id==='opinion' ? !!(S.o1||S.o2||S.o3||S.o4) : !!S.seen[st.id]);
  o += '<button type="button" class="'+(S.cur===st.id?'on ':'')+(done&&S.cur!==st.id?'done':'')+'" data-go="'+st.id+'"'+(S.cur===st.id?' aria-current="step"':'')+'><span class="n">'+(done&&S.cur!==st.id?'✓':(i+1))+'</span>'+st.label+'</button>';
 });
 $('steps').innerHTML = o;
}
function go(id){
 S.seen[S.cur] = true; S.cur = id; save();
 var vs = document.querySelectorAll('section.view');
 for(var i=0;i<vs.length;i++) vs[i].classList.toggle('on', vs[i].id==='v-'+id);
 nav(); window.scrollTo(0,0);
}
document.addEventListener('click', function(e){
 var g = e.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var a = e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});

/* ---- calculadora 30/50 ---- */
function fmt(n){ return (Math.round(n*100)/100).toFixed(2).replace('.',',').replace(',00',''); }
function calc(){
 var L=+$('cL').value, E=+$('cE').value*25/3, A=+$('cA').value, O=+$('cO').value*25/3;
 $('vL').textContent = L+' pts'; $('vE').textContent = fmt(E)+' pts'; $('vA').textContent = A+' pts'; $('vO').textContent = fmt(O)+' pts';
 var g1=L+E, g2=A+O, ok1=g1>=30, ok2=g2>=30;
 $('g1').className = ok1?'ok':'no'; $('g1').textContent = 'Grupo 1: '+fmt(g1)+' / 50 · '+(ok1?'apto':'no apto');
 $('g2').className = ok2?'ok':'no'; $('g2').textContent = 'Grupo 2: '+fmt(g2)+' / 50 · '+(ok2?'apto':'no apto');
 var f=$('gf'); f.className = 'final '+(ok1&&ok2?'ok':'no');
 f.textContent = ok1&&ok2 ? 'Resultado final: APTO' : 'Resultado final: NO APTO'+(ok1!==ok2?' (aunque un grupo está aprobado)':'');
}
['cL','cE','cA','cO'].forEach(function(id){ $(id).addEventListener('input', calc); });

/* ---- test ---- */
function testDone(){ return Object.keys(S.t).length===D.test.length; }
function renderTest(){
 var o='', n=0, ok=0;
 D.test.forEach(function(q,i){
  var a = S.t[i], has = a!==undefined, good = has && a===q.v;
  if(has){ n++; if(good) ok++; }
  o += '<div class="vf"><div class="st"><span class="num">'+(i+1)+'.</span>'+q.s+'</div><div class="bt" role="group" aria-label="Pregunta '+(i+1)+'">';
  [[true,'Verdadero'],[false,'Falso']].forEach(function(b){
   var sel = has && a===b[0];
   o += '<button type="button" data-act="tf" data-i="'+i+'" data-v="'+(b[0]?1:0)+'"'+(has?' disabled':'')+' class="'+(sel?'sel '+(good?'good':'bad'):'')+'"'+(sel?' aria-pressed="true"':'')+'>'+b[1]+'</button>';
  });
  o += '</div>'+(has?'<div class="fb '+(good?'good':'bad')+'" role="status"><b>'+(good?'¡Bien! ':'No. ')+(q.v?'Es verdadero.':'Es falso.')+'</b> '+q.why+'</div>':'')+'</div>';
 });
 $('tlist').innerHTML = o;
 $('tprog').style.width = Math.round(n/D.test.length*100)+'%';
 var sc='';
 if(testDone()){
  var msg = ok>=14 ? 'Conoces muy bien el examen. Ya puedes empezar a entrenar las tareas.' : (ok>=11 ? 'Lo conoces bastante bien. Vuelve a leer las explicaciones de las frases que has fallado.' : 'Vuelve a mirar las partes "El examen" y "Cómo se aprueba" y repite el test.');
  sc = '<div class="score"><b class="big">'+ok+'/'+D.test.length+'</b><p>'+msg+'</p><div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button><button class="btn" data-act="retest">Repetir el test</button></div></div>';
 }
 $('tscore').innerHTML = sc;
}

/* ---- opinion ---- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o += '<label><input type="radio" name="o4" value="'+i+'"'+(String(S.o4)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o4').innerHTML = o;
 ['o1','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked = r[i].value===S[k]; });
 $('o2').value = S.o2; $('sname').value = S.name;
}
document.addEventListener('change', function(e){ var t=e.target; if(t.name==='o1'||t.name==='o3'||t.name==='o4'){ S[t.name]=t.value; save(); nav(); } });
document.addEventListener('input', function(e){ var t=e.target; if(t.id==='o2'){ S.o2=t.value; save(); } if(t.id==='sname'){ S.name=t.value; save(); } });
function pack(){
 var ok=0, n=0; D.test.forEach(function(q,i){ if(S.t[i]!==undefined){ n++; if(S.t[i]===q.v) ok++; } });
 var fails=[]; D.test.forEach(function(q,i){ if(S.t[i]!==undefined && S.t[i]!==q.v) fails.push(i+1); });
 return ['CURSO DELE A2 - MODULO 0: CONOCE EL EXAMEN', 'Nombre: '+(S.name||'-'), '',
  'Test: '+ok+'/'+D.test.length+(n<D.test.length?' (sin terminar: '+n+' contestadas)':'')+(fails.length?' | falladas: '+fails.join(', '):''),
  '1. Lo mas util: '+(S.o1||'-'), '2. No he entendido / falta: '+(S.o2||'-'), '3. Me preocupa mas: '+(S.o3||'-'), '4. Sensacion de control (1-10): '+(S.o4||'-')].join('\n');
}

/* ---- acciones ---- */
var ACTS = {
 tf: function(b){ S.t[+b.getAttribute('data-i')] = b.getAttribute('data-v')==='1'; save(); renderTest(); nav();
  var fb = document.querySelectorAll('.vf')[+b.getAttribute('data-i')]; if(fb){ var x=fb.querySelector('.fb'); if(x && x.scrollIntoView) x.scrollIntoView({block:'nearest'}); } },
 retest: function(){ S.t={}; save(); renderTest(); nav(); window.scrollTo(0,0); },
 print: function(){ var v=$('v-reglas'); v.classList.add('printme'); window.print(); setTimeout(function(){ v.classList.remove('printme'); }, 500); },
 copy: function(){
  var t=pack(), box=$('cbox');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar automáticamente. Escribe tus respuestas en un correo para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
 }
};
window.addEventListener('afterprint', function(){ var v=$('v-reglas'); if(v) v.classList.remove('printme'); });

renderTest(); renderScale(); calc(); go(S.cur);
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_M0, body, js))
print("ok", FILE)
