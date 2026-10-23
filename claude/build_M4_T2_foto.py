# -*- coding: utf-8 -*-
# MODULO 4 DEL CURSO DE PREPARACION DELE A2 · ORAL TAREA 2: DESCRIPCION DE LA FOTO
# Uso: python3 build_M4_T2_foto.py
#  -> DELEA2_curso_M4_T2_foto.html  (subir a biblioteca/recursos/A2/dele-curso/)
#  -> M4T2_prompts_imagenes.txt y nombres.txt (para la accion rapida "Imagen DELE")
# Contenido (plantilla y fotos): banco_fotos_T2.py. Para anadir fotos, solo se toca ese archivo.
# La grabacion se queda en el navegador del estudiante: no se sube a ningun sitio.
import json, re
from curso_comun import CSS, EMAIL, page
import banco_fotos_T2 as B

TITLE = "Describe la foto"
FILE = "DELEA2_curso_M4_T2_foto.html"
STORAGE = "dele-a2-curso-M4-T2"
IMG_BASE = "https://2spanishteachers.com/wp-content/uploads/" + B.MES_WP.strip("/") + "/"
WPM = 115   # palabras por minuto de un candidato A2 que habla con calma

# ------------------------------------------------------------ comprobaciones del banco
CAMPOS = ("situacion", "personas", "edades", "aspecto", "espacio", "lugar", "momento", "estacion", "tiempo", "gente", "accion", "fondo", "objetos", "problema")
ids = [f["id"] for f in B.FOTOS]
assert len(ids) == len(set(ids)), "Hay dos fotos con el mismo id"
for f in B.FOTOS:
    falta = [c for c in CAMPOS if not f["perfil"].get(c)]
    assert not falta, "Foto %d: falta en el perfil %s" % (f["id"], falta)
    assert len(f["modelo"]) == 6 and len(f["fijate"]) == 6, "Foto %d: hacen falta 6 parrafos modelo y 6 pistas" % f["id"]
    assert "no readable text" in f["prompt"].lower(), "Foto %d: el prompt debe decir no readable text" % f["id"]
    n = B.NOTAS.get(f["id"])
    assert n and len(n) == 6 and all(len(x) == 3 for x in n), "Foto %d: faltan las notas modelo (6 casillas x 3)" % f["id"]

def mark(t):
    return re.sub(r"\[\[(.+?)\]\]", r'<mark>\1</mark>', t)
def plain(t):
    return re.sub(r"\[\[|\]\]", "", t)

FOTOS_JS = []
for f in B.FOTOS:
    p = f["perfil"]
    words = sum(len(plain(x).split()) for x in f["modelo"])
    FOTOS_JS.append({
        "id": f["id"], "t": f["titulo"], "img": IMG_BASE + "M4T2_foto%d.jpg" % f["id"],
        "alt": "%s: %s." % (p["situacion"][0].upper() + p["situacion"][1:], p["accion"]),
        "miss": "%s. %s. %s. Al fondo, %s." % (p["lugar"][0].upper() + p["lugar"][1:], p["aspecto"][0].upper() + p["aspecto"][1:],
                                                p["accion"][0].upper() + p["accion"][1:], p["fondo"]),
        "fij": f["fijate"], "pal": f["palabras"], "mod": [mark(x) for x in f["modelo"]],
        "tipo": f.get("tipo", "entrenamiento"), "notas": B.NOTAS[f["id"]], "w": words, "ws": [len(plain(x).split()) for x in f["modelo"]], "min": round(words / WPM * 2) / 2})

# ------------------------------------------------------------ CSS
CSS_T2 = CSS + r"""
.qlist{counter-reset:q;list-style:none;padding:0;margin:12px 0}
.qlist li{counter-increment:q;position:relative;padding:8px 0 8px 40px;border-bottom:1px dashed var(--line)}
.qlist li:before{content:counter(q);position:absolute;left:0;top:8px;width:28px;height:28px;border-radius:50%;background:var(--coral);color:#fff;font-weight:700;display:grid;place-items:center;font-size:.9rem}
.tl{display:grid;grid-template-columns:repeat(6,1fr);gap:4px;margin:14px 0 4px}
.tl div{background:var(--coral-soft);border-top:5px solid var(--coral);border-radius:4px;padding:6px 4px;text-align:center;font-size:.8rem;line-height:1.3}
.tl div b{display:block;font-size:1rem;font-family:Georgia,serif}
.tl-cap{display:flex;justify-content:space-between;font-size:.82rem;color:var(--muted)}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}
.vs div{border-radius:12px;padding:12px 16px;font-size:.95rem}
.vs .no{background:var(--bad-soft)}.vs .si{background:var(--ok-soft)}
.vs b{display:block;margin-bottom:4px}
.keys{counter-reset:k;list-style:none;padding:0}
.keys li{counter-increment:k;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 14px 10px 52px;margin:8px 0;position:relative}
.keys li:before{content:counter(k);position:absolute;left:14px;top:8px;font-family:Georgia,serif;font-size:1.5rem;font-weight:700;color:var(--coral)}
.pq{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:14px 0;border-left:6px solid var(--coral);break-inside:avoid}
.pq h3{margin:0 0 2px;display:flex;gap:10px;align-items:baseline}
.pq h3 .num{font-size:1.5rem;color:var(--coral)}
.pq .of{font-size:.88rem;color:var(--muted);font-style:italic;margin:0 0 8px}
.chipz{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 10px}
.chipz span{background:var(--coral-soft);border-radius:999px;padding:3px 12px;font-size:.92rem}
.lad{display:grid;grid-template-columns:7.5em 1fr;gap:4px 10px;font-size:.95rem;background:var(--paper);border-radius:8px;padding:8px 12px}
.lad b{font-size:.78rem;letter-spacing:.04em;color:var(--muted);padding-top:3px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px}
.box ul{margin:6px 0 0;padding-left:1.1em}
#pr h4{margin:16px 0 4px}
mark{background:#FFE2D6;color:inherit;border-radius:3px;padding:0 2px}
/* practica */
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:14px 0}
.card{background:#fff;border:2px solid var(--line);border-radius:12px;overflow:hidden;cursor:pointer;text-align:left;font:inherit;padding:0;color:inherit}
.card:hover{border-color:var(--coral)}
.card .th{aspect-ratio:3/2;background:var(--coral-soft);overflow:hidden;position:relative}
.card .th img{width:100%;height:100%;object-fit:cover;display:block}
.card .th .fb{position:absolute;inset:0;display:none;place-items:center;font-family:Georgia,serif;font-size:2.4rem;color:var(--coral)}
.card .th.miss img{display:none}.card .th.miss .fb{display:grid}
.card .cap{padding:8px 12px}
.card .cap b{display:block;font-size:.98rem}
.card .cap span{font-size:.82rem;color:var(--muted)}
figure.ph{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
figure.ph img{width:100%;display:block;aspect-ratio:3/2;object-fit:cover}
figure.ph .missbox{display:none;padding:16px 18px;background:var(--coral-soft);font-size:.95rem}
figure.ph.miss img{display:none}figure.ph.miss .missbox{display:block}
figure.ph figcaption{padding:8px 14px;font-weight:700;font-family:Georgia,serif;border-top:1px solid var(--line)}
.modes{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}
.mode{background:#fff;border:2px solid var(--line);border-radius:12px;padding:12px 16px;cursor:pointer;display:block}
.mode:has(input:checked){border-color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
.mode input{margin-right:6px;accent-color:var(--coral)}
.mode p{margin:4px 0 0;font-size:.9rem;color:var(--muted)}
.opts{background:#fff;border:1px solid var(--line);border-radius:12px;padding:6px 16px;margin:10px 0}
.opts label{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px dashed var(--line)}
.opts label:last-child{border-bottom:0}
.opts input[type=checkbox]{width:20px;height:20px;accent-color:var(--coral);flex:0 0 auto;margin-top:3px}
.opts select{font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:4px 8px;background:#fff}
.opts small{display:block;color:var(--muted);font-size:.85rem}
.run{display:grid;grid-template-columns:1.05fr 1fr;gap:16px;align-items:start;margin-top:8px}
.run .side{position:sticky;top:120px}
.pan{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px}
.pan .kk{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.pan h3{margin:2px 0 8px;font-size:1.25rem}
.clock{font-family:Georgia,serif;font-size:2.6rem;font-weight:700;font-variant-numeric:tabular-nums;line-height:1}
.clock.green{color:var(--ok)}.clock.red{color:var(--bad)}
.bar{height:12px;background:var(--line);border-radius:99px;overflow:hidden;margin:10px 0}
.bar i{display:block;height:100%;background:var(--coral);width:0}
.esc{list-style:none;padding:0;margin:10px 0}
.esc li{padding:7px 10px;border-radius:8px;margin:4px 0;color:#B5ADA4;border:1px dashed var(--line)}
.esc li.on{color:var(--ink);background:var(--coral-soft);border:1px solid transparent;font-weight:600}
.fij{font-size:.92rem;margin:8px 0;padding:8px 12px;border-left:4px solid var(--amb);background:var(--amb-soft);border-radius:0 8px 8px 0}
.dots{display:flex;gap:5px;margin:4px 0 8px}
.dots i{flex:1;height:6px;border-radius:99px;background:var(--line)}
.dots i.d{background:var(--ok)}.dots i.c{background:var(--coral)}
.recdot{display:inline-flex;align-items:center;gap:6px;font-size:.85rem;font-weight:600;color:var(--bad)}
.recdot:before{content:"";width:10px;height:10px;border-radius:50%;background:var(--bad);animation:bl 1s infinite}
@keyframes bl{50%{opacity:.25}}
.chk{list-style:none;padding:0;margin:8px 0}
.chk li label{display:flex;gap:10px;align-items:flex-start;padding:6px 0;border-bottom:1px dashed var(--line);cursor:pointer}
.chk input{width:20px;height:20px;accent-color:var(--ok);flex:0 0 auto;margin-top:3px}
.chk li label:has(input:checked) span{color:var(--muted);text-decoration:line-through}
.modtxt{font-size:.98rem;margin:6px 0 0}
.res{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 20px;margin:12px 0}
.res .big{font-family:Georgia,serif;font-size:2.4rem;font-weight:700;line-height:1}
.verd{border-radius:10px;padding:10px 14px;font-weight:600;margin:10px 0}
.verd.ok{background:var(--ok-soft);color:var(--ok)}.verd.amb{background:var(--amb-soft);color:#7A4E0E}.verd.bad{background:var(--bad-soft);color:var(--bad)}
.zone{position:relative;height:16px;background:var(--line);border-radius:99px;margin:20px 0 26px}
.zone .ok{position:absolute;top:0;bottom:0;left:50%;width:25%;background:var(--ok-soft);border-left:2px solid var(--ok);border-right:2px solid var(--ok)}
.zone .me{position:absolute;top:-6px;width:4px;height:28px;background:var(--ink);border-radius:2px}
.zone span{position:absolute;top:20px;font-size:.75rem;color:var(--muted);transform:translateX(-50%)}
.hist{font-size:.92rem;margin:6px 0}
.hist li{margin:2px 0}
audio{width:100%;margin:8px 0}
.warnbox{background:var(--amb-soft);border-radius:10px;padding:12px 14px;margin:10px 0}
.warnbox[hidden]{display:none}
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
/* preparacion y esquema */
.r12{display:flex;border-radius:10px;overflow:hidden;margin:14px 0 4px;border:2px solid var(--ink)}
.r12 div{padding:8px 6px;text-align:center;font-size:.82rem;line-height:1.25;border-right:2px solid var(--ink);background:#fff}
.r12 div:last-child{border-right:0}
.r12 div b{display:block;font-family:Georgia,serif;font-size:1.05rem}
.r12 div.me{background:var(--coral);color:#fff}
.r12cap{display:flex;justify-content:space-between;font-size:.8rem;color:var(--muted)}
.r12list{margin:10px 0;padding-left:1.1em;font-size:.95rem}
.steps4{list-style:none;padding:0;margin:12px 0;position:relative}
.steps4 li{display:grid;grid-template-columns:4em 1fr;gap:12px;padding:10px 0;border-bottom:1px dashed var(--line)}
.steps4 .tm{font-family:Georgia,serif;font-weight:700;font-size:1.15rem;color:var(--coral)}
.leg{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:.92rem;margin:8px 0}
.leg b{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:50%;background:var(--ink);color:#fff;font-size:.95rem;margin-right:4px}
.esq{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.esq.one{grid-template-columns:1fr}
.eb{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:8px 12px 10px;position:relative;min-height:7.5em}
.eb.cur{border-color:var(--coral);box-shadow:0 0 0 3px var(--coral-soft)}
.eh{display:flex;align-items:center;gap:8px;font-weight:700;font-size:.86rem;letter-spacing:.03em;text-transform:uppercase;margin-bottom:4px}
.en{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--coral);color:#fff;font-family:Georgia,serif;font-size:1.05rem;flex:0 0 auto}
.el{display:grid;grid-template-columns:1.4em 1fr;font-size:.92rem;line-height:1.4;padding:3px 0;border-bottom:1px dotted #CFC6BB;min-height:1.9em}
.el:last-child{border-bottom:0}
.el i{font-style:normal;font-weight:700;color:var(--coral)}
.esq.blank .el{min-height:2.3em}
.eb textarea{width:100%;font:inherit;font-size:.95rem;line-height:1.5;border:1px dashed #CFC6BB;border-radius:8px;padding:6px 8px;min-height:6.2em;resize:vertical;background:var(--paper)}
.eb .wn{font-size:.8rem;color:#7A4E0E;background:var(--amb-soft);border-radius:6px;padding:2px 8px;margin-top:4px;display:none}
.eb.many .wn{display:block}
.myn{white-space:pre-wrap;font-size:.95rem;background:#FFF8F2;border:1px solid var(--coral-soft);border-radius:8px;padding:8px 12px;margin:8px 0}
.myn b{display:block;font-size:.78rem;letter-spacing:.05em;color:var(--coral);white-space:normal}
.lq-n{display:block;white-space:pre-wrap;font-size:.85rem;color:var(--muted);margin-top:2px}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.cmp h4{margin:6px 0 0}
.exwrap{display:grid;grid-template-columns:.9fr 1.1fr;gap:14px;align-items:start}
#sheet{display:none}
.tg{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.04em;border-radius:999px;padding:1px 9px;margin-top:3px}
.tg.ex{background:var(--ok-soft);color:var(--ok)}.tg.en{background:var(--amb-soft);color:#7A4E0E}
h3.grp{margin:22px 0 2px}
.lvl{display:inline-block;width:60px;height:8px;background:var(--line);border-radius:99px;overflow:hidden;vertical-align:middle;margin-left:6px}
.lvl i{display:block;height:100%;width:0;background:var(--ok);transition:width .15s}
body.wide .wrap,body.wide .top-in{max-width:1240px}
body.wide .run{grid-template-columns:1.55fr 1fr}
figure.ph .zoom{float:right;font-family:system-ui,sans-serif}
figure.ph.miss .zoom{display:none}
.run figure.ph img{cursor:zoom-in}
#lb{position:fixed;inset:0;background:#14161C;z-index:50;display:none;flex-direction:column;align-items:center;justify-content:center;padding:12px}
#lb.on{display:flex}
#lb .lbbar{display:flex;gap:14px;align-items:center;justify-content:space-between;width:100%;max-width:1600px;color:#fff;margin-bottom:8px}
#lb .lbbar b{font-family:Georgia,serif;font-size:1.1rem}
#lbclk{font-family:Georgia,serif;font-size:1.5rem;font-weight:700;font-variant-numeric:tabular-nums}
#lb img{max-width:100%;max-height:calc(100vh - 80px);object-fit:contain;border-radius:6px}
#lb .btn{background:#fff}
/* modo concentracion: mientras se practica desaparece la cabecera */
body.focus header.top{display:none}
body.focus section.view{padding-top:12px}
body.focus .run .side{top:12px}
.rot{display:none}
.mini{display:none}
@media (max-width:900px){body.wide .run,.run{grid-template-columns:1fr}.run .side{position:static}.run figure.ph img{max-height:42vh}
 body.focus .run .side{position:sticky;top:0;z-index:6;background:var(--paper);padding:6px 0 8px;margin:0 -4px}
 body.focus .run figure.ph img{max-height:38vh}
 body.focus.notas .run figure.ph img{max-height:24vh}
 body.focus .run figure.ph figcaption{padding:4px 10px;font-size:.92rem}
 body.focus .pan{padding:12px 14px}body.focus .clock{font-size:2rem}
 .rot{display:block}
 body.focus .mini{display:flex;justify-content:space-between;gap:10px;background:var(--ink);color:#fff;border-radius:8px;padding:6px 12px;margin-top:6px;font-weight:600;font-size:.92rem}
 body.focus .mini b{font-family:Georgia,serif;font-variant-numeric:tabular-nums}}
@media (max-width:760px){
 .grid{grid-template-columns:1fr 1fr}.modes,.two,.vs,.esq,.cmp,.exwrap{grid-template-columns:1fr}.r12 div{font-size:.7rem;padding:6px 2px}.tl div{font-size:.7rem}.lad{grid-template-columns:1fr}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}
 body.ps main,body.ps header{display:none!important}body.ps #sheet{display:block;padding:0 4mm}
 #sheet h2{font-size:15pt;margin:0 0 2mm}#sheet .esq{grid-template-columns:1fr 1fr;gap:4mm}#sheet .eb{min-height:72mm;break-inside:avoid}#sheet .el{min-height:16mm;font-size:10pt}}
"""

# ------------------------------------------------------------ VISTAS
STEPS = [("tarea", "La tarea"), ("plantilla", "La plantilla"), ("prep", "La preparación"), ("practica", "Practica"), ("opinion", "Tu opinión")]

qs = "".join("<li>%s</li>" % q["oficial"] for q in B.PLANTILLA)
tl = "".join("<div><b>%d</b>%s</div>" % (i + 1, q["corto"].split(" y ")[0]) for i, q in enumerate(B.PLANTILLA))

V_TAREA = """
<h2>La tarea 2 de la oral: describir una foto</h2>
<p class="lead">En el examen eliges una de dos fotos y hablas de ella <b>entre 2 y 3 minutos</b>. El examinador no te pregunta nada: hablas tú solo. Tienes la foto delante y, debajo, siempre las mismas seis preguntas.</p>
<div class="note"><b>Lo que pone la lámina</b> (siempre igual, con cualquier foto):<ol class="qlist">""" + qs + """</ol></div>

<h3>El problema: terminar en un minuto</h3>
<p>Muchos candidatos dicen una frase para cada pregunta y terminan en menos de un minuto. Por los nervios, además, hablan muy deprisa. Con un minuto no hay suficiente muestra para el examinador: la tarea queda <b>incompleta</b>, aunque las frases estén bien.</p>
<div class="vs">
 <div class="no"><b>Una frase por pregunta = 1 minuto</b><i>"Hay una familia. Están en el campo. Comen. Son una familia. Están contentos. Después van a casa."</i></div>
 <div class="si"><b>Tres frases por pregunta = 2 minutos y medio</b><i>"Hay una familia grande. En el centro hay una señora mayor con el pelo blanco. Parece muy simpática, porque sonríe..."</i></div>
</div>
<p>La cuenta es fácil: <b>6 preguntas × 3 frases = 18 frases</b>. Si cada pregunta dura unos 25 segundos, llegas a 2 minutos y medio sin correr.</p>
<div class="tl" aria-hidden="true">""" + tl + """</div>
<div class="tl-cap"><span>0:00</span><span>unos 25 segundos por pregunta</span><span>2:30</span></div>

<h3>Cinco claves para no correr</h3>
<ol class="keys">
 <li><b>La regla de las tres frases.</b> En cada pregunta: lo que ves, un detalle (un color, un número, dónde está) y tu opinión con <i>creo que... porque...</i></li>
 <li><b>Sigue el orden de la lámina.</b> Las seis preguntas son tu guion. Si sigues el orden, nunca te quedas sin nada que decir.</li>
 <li><b>Usa puentes entre preguntas.</b> <i>"Bueno, ahora el lugar..."</i>, <i>"¿Y cómo se sienten? A ver..."</i>. Te ordenan y te dan un segundo para respirar.</li>
 <li><b>Puedes imaginar.</b> Nadie sabe qué piensan esas personas ni qué han hecho antes: invéntalo con <i>creo que, seguramente, parece que</i>. Imaginar no es un error; es lo que pide la tarea.</li>
 <li><b>Respira entre una pregunta y otra.</b> Una pausa corta no es un problema. Hablar despacio y claro se entiende mejor y te da tiempo para pensar la frase siguiente.</li>
</ol>
<div class="tip"><b>Cómo practicar aquí:</b> primero aprende la plantilla y cómo preparar la foto en 4 minutos con el esquema de las seis casillas. Después usa el <b>modo guiado</b>: cada pregunta sale en la pantalla con su tiempo, para que no corras. Cuando ya llegues a 2 minutos sin ayuda, prueba el <b>modo examen</b>. Si quieres, puedes grabarte y escucharte.</div>
<div class="row"><button class="btn cta" data-go="plantilla">Siguiente: la plantilla</button></div>
"""

def v_plantilla():
    o = ('<h2>La plantilla universal</h2><p class="lead">Las mismas seis preguntas, con las frases comodín que sirven para cualquier foto. '
         'Debajo de cada pregunta tienes un ejemplo de las tres frases: lo que veo, un detalle y mi opinión.</p>')
    labs = ["Lo que veo", "Un detalle", "Mi opinión"]
    for i, q in enumerate(B.PLANTILLA, 1):
        o += ('<div class="pq"><h3><span class="num">%d</span>%s</h3><p class="of">%s</p><div class="chipz">%s</div><div class="lad">%s</div></div>'
              % (i, q["corto"], q["oficial"], "".join("<span>%s</span>" % c for c in q["com"]),
                 "".join("<b>%s</b><span>%s</span>" % (labs[k].upper(), q["ej"][k]) for k in range(3))))
    o += ('<div class="two"><div class="box"><h4>Puentes entre preguntas</h4><ul>%s</ul></div><div class="box"><h4>Para ganar tiempo o si no sabes una palabra</h4><ul>%s</ul></div></div>'
          % ("".join("<li><i>%s</i></li>" % p for p in B.PUENTES), "".join("<li><i>%s</i></li>" % p for p in B.GANAR_TIEMPO)))
    o += '<div class="tip">Cuidado: describe la foto, no tu vida. Hablar de ti es la tarea 1. Aquí, si dices <i>"yo también tengo un perro"</i>, que sea solo una frase y vuelve a la foto.</div>'
    o += '<div class="row"><button class="btn" data-act="print" data-p="plantilla">Imprimir la plantilla</button><button class="btn cta" data-go="prep">Siguiente: la preparación</button></div>'
    return o

total = sum(m for m, _, _ in B.REPARTO_12)
assert total == 12, "El reparto de la preparacion tiene que sumar 12 minutos"
r12 = "".join('<div class="%s" style="flex:%d"><b>%d min</b>%s</div>' % ("me" if t == "Tarea 2" else "", m, m, t) for m, t, _ in B.REPARTO_12)
r12l = "".join("<li><b>%s (%d min):</b> %s</li>" % (t, m, d) for m, t, d in B.REPARTO_12)
p4 = "".join('<li><span class="tm">%s</span><span><b>%s.</b> %s</span></li>' % x for x in B.PASOS_FOTO)
reg = "".join("<li>%s</li>" % x for x in B.REGLAS_NOTAS)
V_PREP = ("""
<h2>La preparación: 12 minutos para tres tareas</h2>
<p class="lead">Antes de entrar en la sala tienes <b>12 minutos para preparar las tres tareas</b> de la oral. Puedes escribir notas y llevarlas contigo: en la prueba puedes <b>mirarlas</b>, pero no leerlas en voz alta.</p>
<h3>Cómo repartir los 12 minutos</h3>
<div class="r12" aria-hidden="true">""" + r12 + """</div>
<div class="r12cap"><span>0:00</span><span>12:00</span></div>
<ul class="r12list">""" + r12l + """</ul>
<div class="tip">Es una recomendación, no una regla del examen. Lo importante: no gastes 10 minutos en la tarea 1 y dejes la foto sin preparar. Mira el reloj de la sala.</div>

<h3>Tus 4 minutos con la foto, paso a paso</h3>
<ol class="steps4">""" + p4 + """</ol>

<h3>El esquema de las seis casillas</h3>
<p>Es tu hoja de notas para la foto. Cada casilla es una pregunta de la lámina, en el mismo orden. En cada casilla, tres líneas: son las tres frases que vas a decir.</p>
<div class="leg"><span><b>&bull;</b>lo que veo</span><span><b>+</b>un detalle</span><span><b>&rarr;</b>mi opinión: creo que... porque...</span></div>
<div id="esq-blank"></div>
<div class="row"><button class="btn" data-act="print" data-p="sheet">Imprimir el esquema en blanco</button></div>

<h3>Un ejemplo: así quedan las notas</h3>
<p>Estas son las notas de la foto <i>__EJT__</i>. Fíjate: <b>solo palabras</b>, flechas y signos. Con estas notas se habla dos minutos y medio, y nadie lee.</p>
<div class="exwrap"><div id="ej-foto"></div><div id="esq-ej"></div></div>

<h3>Reglas para tus notas</h3>
<ul class="keys">""" + reg + """</ul>
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica con fotos</button></div>
""").replace("__EJT__", [f["titulo"] for f in B.FOTOS if f["id"] == B.EJEMPLO_NOTAS][0])

V_PRACTICA = '<div id="pr"></div>'

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿El modo guiado te ha ayudado a hablar más despacio y más tiempo?</label>
 <div class="chips" role="group" aria-labelledby="o1l">
  <label><input type="radio" name="o1" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o1" value="Un poco">Un poco</label>
  <label><input type="radio" name="o1" value="No">No</label>
  <label><input type="radio" name="o1" value="No lo he probado">No lo he probado</label>
 </div>
 <label class="q" id="o5l">2. ¿Te ha servido el esquema de las seis casillas para preparar la foto?</label>
 <div class="chips" role="group" aria-labelledby="o5l">
  <label><input type="radio" name="o5" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o5" value="Un poco">Un poco</label>
  <label><input type="radio" name="o5" value="No">No</label>
  <label><input type="radio" name="o5" value="No lo he probado">No lo he probado</label>
 </div>
 <label class="q" for="o2">3. ¿Te has grabado? ¿Qué has notado al escucharte? (O, si no, ¿qué falta o no has entendido?)</label>
 <textarea id="o2"></textarea>
 <label class="q" id="o3l">4. ¿Qué pregunta de las seis te cuesta más?</label>
 <div class="chips" role="group" aria-labelledby="o3l">__CHIPS__</div>
 <label class="q" id="o4l">5. Ahora, ¿cuánto control sientes cuando describes una foto? (1 = nada, 10 = total)</label>
 <div class="scale" role="group" aria-labelledby="o4l" id="o4"></div>
</div>
<div class="sendbox">
 <h3>Envía tu opinión y tus tiempos a tu profesora</h3>
 <label><b>Tu nombre</b><br><input type="text" id="sname" autocomplete="name"></label>
 <div class="row"><button class="btn cta" data-act="copy">Copiar</button></div>
 <div class="copied-box" id="cbox" role="status" hidden></div>
 <p class="muted small">Pégalo en un correo para tu profesora: __EMAIL__. Tus grabaciones no se copian: si quieres que tu profesora te escuche, guarda el audio y envíalo tú.</p>
</div>
""".replace("__CHIPS__", "".join('<label><input type="radio" name="o3" value="%d. %s">%d. %s</label>' % (i, q["corto"], i, q["corto"]) for i, q in enumerate(B.PLANTILLA, 1))).replace("__EMAIL__", EMAIL)

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Oral · Tarea 2</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
<div id="lb" role="dialog" aria-modal="true" aria-label="Foto en grande"><div class="lbbar"><b id="lbt"></b><span id="lbclk"></span><button type="button" class="btn sm" data-act="unzoom">Cerrar ✕</button></div><img id="lbimg" alt=""></div>
<div id="sheet"><h2>La foto · mis notas</h2><div class="leg"><span><b>&bull;</b>lo que veo</span><span><b>+</b>un detalle</span><span><b>&rarr;</b>mi opinión: creo que... porque...</span></div><div id="esq-sheet"></div></div>
"""

views = {"tarea": V_TAREA, "plantilla": v_plantilla(), "prep": V_PREP, "practica": V_PRACTICA, "opinion": V_OPINION}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
body = BODY.replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

DATA = {"key": STORAGE, "steps": [{"id": k, "label": l} for k, l in STEPS], "fotos": FOTOS_JS,
        "ej": B.EJEMPLO_NOTAS, "pl": [{"c": q["corto"], "o": q["oficial"], "com": q["com"]} for q in B.PLANTILLA], "esc": B.ESCALONES}

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function blank(){ return {cur:'tarea', seen:{}, foto:null, o:{mode:'guiado', ritmo:25, prep:'notas', modelo:false, rec:false, beep:true}, h:{}, n:{}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } for(var j in b.o){ if(!(j in o.o)) o.o[j]=b.o[j]; } return o; } }catch(e){} return blank(); })();
if(typeof S.o.prep==='boolean') S.o.prep = S.o.prep ? 'mirar' : 'no';
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function F(id){ for(var i=0;i<D.fotos.length;i++) if(D.fotos[i].id===id) return D.fotos[i]; return null; }
function mmss(s){ s=Math.max(0,Math.round(s)); return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2); }

/* ---------------- navegacion ---------------- */
function practiced(){ return Object.keys(S.h).length>0; }
function nav(){
 var o='';
 D.steps.forEach(function(st,i){
  var done = st.id==='practica' ? practiced() : (st.id==='opinion' ? !!(S.o1||S.o2||S.o3||S.o4||S.o5) : !!S.seen[st.id]);
  var on = S.cur===st.id;
  o += '<button type="button" class="'+(on?'on ':'')+(done&&!on?'done':'')+'" data-go="'+st.id+'"'+(on?' aria-current="step"':'')+'><span class="n">'+(done&&!on?'✓':(i+1))+'</span>'+st.label+'</button>';
 });
 $('steps').innerHTML = o;
}
function go(id){
 if(R.active && id!=='practica'){ stopRun(true); }
 S.seen[S.cur]=true; S.cur=id; save();
 var vs=document.querySelectorAll('section.view');
 for(var i=0;i<vs.length;i++) vs[i].classList.toggle('on', vs[i].id==='v-'+id);
 document.body.classList.toggle('wide', id==='practica');
 if(id==='practica' && !R.active) showPick();
 nav(); window.scrollTo(0,0);
}

/* ---------------- fotos ---------------- */
function figure(f, cap){
 return '<figure class="ph"><img src="'+esc(f.img)+'" alt="'+esc(f.alt)+'" onerror="this.parentNode.classList.add(\'miss\')"><div class="missbox"><b>(Foto pendiente de subir)</b><br>'+esc(f.miss)+'</div>'+(cap?'<figcaption>'+esc(f.t)+'<button type="button" class="btn sm zoom noprint" data-act="zoom" data-id="'+f.id+'">Ver en grande</button></figcaption>':'')+'</figure>';
}
function lastTime(id){ var h=S.h[id]; return h&&h.length ? h[h.length-1] : null; }
function showPick(){
 var o='<h2>Practica con fotos</h2><p class="lead">Elige una foto. En el examen tienes dos y eliges una: aquí puedes practicar con todas.</p>';
 o+='<div class="row"><button class="btn cta" data-act="random">Foto al azar</button></div>';
 [['examen','Fotos como en el examen','Pocas personas y una escena clara, como en las l\u00E1minas oficiales. Para llegar a 2 minutos tienes que imaginar m\u00E1s.'],
  ['entrenamiento','Fotos de entrenamiento','Con much\u00EDsimos detalles: para aprender vocabulario y a estirar cada pregunta. Las del examen son m\u00E1s sencillas.']].forEach(function(g){
  var fs=D.fotos.filter(function(f){ return f.tipo===g[0]; }); if(!fs.length) return;
  o+='<h3 class="grp">'+g[1]+'</h3><p class="small muted" style="margin:0">'+g[2]+'</p><div class="grid">';
  fs.forEach(function(f){
  var l=lastTime(f.id);
  o+='<button type="button" class="card" data-act="pick" data-id="'+f.id+'"><div class="th"><img src="'+esc(f.img)+'" alt="" onerror="this.parentNode.classList.add(\'miss\')"><span class="fb">'+f.id+'</span></div><div class="cap"><b>'+f.id+'. '+esc(f.t)+'</b><span>'+(l?'Última vez: '+mmss(l.s)+(l.m==='guiado'?' (guiado)':' (examen)'):'Sin practicar')+'</span></div></button>';
  });
  o+='</div>';
 });
 $('pr').innerHTML=o;
}
function modelHTML(f){
 var o='<p class="small muted">Unas '+f.w+' palabras: unos '+String(f.min).replace('.',',')+' minutos hablando con calma. En color, las frases comodín de la plantilla.</p>';
 f.mod.forEach(function(p,i){ o+='<h4>'+(i+1)+'. '+esc(D.pl[i].c)+'</h4><p class="modtxt">'+p+'</p>'; });
 return o;
}
/* ---------------- esquema de las seis casillas ---------------- */
var SYM=['•','+','→'], NOTE_DEF='• \n+ \n→ ';
var FW={'el':1,'la':1,'los':1,'las':1,'un':1,'una':1,'unos':1,'unas':1,'que':1,'hay':1,'es':1,'son':1,'está':1,'están':1,'lleva':1,'llevan':1,'tiene':1,'tienen':1,'porque':1,'muy':1};
function wordsOf(t){ return String(t||'').toLowerCase().match(/[a-záéíóúüñ0-9]+/g)||[]; }
function tooLong(t){ var w=wordsOf(t), n=0; w.forEach(function(x){ if(FW[x]) n++; }); return n>=4 || w.length>28; }
function hasNote(i){ return !!(R.notes && R.useNotes && wordsOf(R.notes[i]).length); }
function eh(i){ return '<div class="eh"><span class="en">'+(i+1)+'</span>'+esc(D.pl[i].c)+'</div>'; }
function esqStatic(vals, cls){
 var o='<div class="esq'+(cls?' '+cls:'')+'">';
 for(var i=0;i<6;i++){ o+='<div class="eb">'+eh(i); for(var k=0;k<3;k++) o+='<div class="el"><i>'+SYM[k]+'</i><span>'+(vals?esc(vals[i][k]):'')+'</span></div>'; o+='</div>'; }
 return o+'</div>';
}
function esqMine(notes, cls){
 var o='<div class="esq'+(cls?' '+cls:'')+'">';
 for(var i=0;i<6;i++){ var t=String(notes[i]||'').trim(); o+='<div class="eb">'+eh(i)+'<div class="lq-n" style="color:var(--ink);font-size:.92rem">'+(wordsOf(t).length?esc(t):'<span class="muted">(vacía)</span>')+'</div></div>'; }
 return o+'</div>';
}
function esqEdit(notes){
 var o='<div class="esq one">';
 for(var i=0;i<6;i++){ o+='<div class="eb'+(tooLong(notes[i])?' many':'')+'">'+eh(i)+'<textarea data-ni="'+i+'" rows="3" aria-label="Notas: '+esc(D.pl[i].c)+'">'+esc(notes[i])+'</textarea><div class="wn">¿Estás escribiendo frases? Mejor solo palabras clave.</div></div>'; }
 return o+'</div>';
}
function renderPrep(){
 $('esq-blank').innerHTML=esqStatic(null,'blank');
 $('esq-sheet').innerHTML=esqStatic(null,'blank');
 var f=F(D.ej); if(f){ $('ej-foto').innerHTML=figure(f,true); $('esq-ej').innerHTML=esqStatic(f.notas,'one'); }
}

function showSetup(){
 var f=F(S.foto); if(!f){ showPick(); return; }
 var O=S.o, o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="back">← Otras fotos</button></div>';
 o+='<div class="run"><div>'+figure(f,true)+'</div><div>';
 o+=(f.tipo==='examen'?'<div class="tip"><span class="tg ex">COMO EN EL EXAMEN</span><br>Esta foto tiene pocos detalles, como las del examen. Para llegar a 2 minutos, describe con calma e <b>imagina m\u00E1s</b> en las preguntas 4, 5 y 6: qui\u00E9nes son, qu\u00E9 piensan, qu\u00E9 han hecho antes.</div>':'<div class="tip"><span class="tg en">ENTRENAMIENTO</span><br>Esta foto tiene much\u00EDsimos detalles: es para practicar vocabulario. No hace falta decirlo todo; elige lo m\u00E1s importante de cada pregunta. Las fotos del examen son m\u00E1s sencillas.</div>');
 o+='<p class="small muted rot">En el m\u00F3vil: mientras practicas, la foto se queda arriba y el men\u00FA se esconde. Para verla m\u00E1s grande, toca la foto (y gira el m\u00F3vil).</p>';
 o+='<h3>¿Cómo quieres practicar?</h3><div class="modes">'+
  '<label class="mode"><input type="radio" name="md" value="guiado"'+(O.mode==='guiado'?' checked':'')+'><b>Modo guiado</b><p>Cada pregunta en la pantalla, con su tiempo y pistas. Para aprender el ritmo.</p></label>'+
  '<label class="mode"><input type="radio" name="md" value="libre"'+(O.mode==='libre'?' checked':'')+'><b>Modo examen</b><p>Solo la foto, las 6 preguntas y el reloj. Como el día del examen.</p></label></div>';
 o+='<div class="opts">';
 o+='<label><span style="flex:1">Preparaci\u00F3n <select id="prepsel">'+[['notas','4 minutos con notas (como en el examen)'],['mirar','30 segundos mirando la foto'],['no','Sin preparaci\u00F3n']].map(function(r){ return '<option value="'+r[0]+'"'+(O.prep===r[0]?' selected':'')+'>'+r[1]+'</option>'; }).join('')+'</select><small>Con notas rellenas el esquema de las seis casillas y despu\u00E9s lo tienes a la vista mientras hablas, como tu hoja en el examen.</small></span></label>';
 if(O.mode==='guiado'){
  o+='<label><span style="flex:1">Ritmo <select id="ritmo">'+[[20,'2 minutos (20 segundos por pregunta)'],[25,'2 minutos y medio (25 segundos)'],[30,'3 minutos (30 segundos)']].map(function(r){ return '<option value="'+r[0]+'"'+(O.ritmo===r[0]?' selected':'')+'>'+r[1]+'</option>'; }).join('')+'</select><small>Empieza con 2 minutos y medio. Si te sobra tiempo en todas las preguntas, prueba 3.</small></span></label>';
  o+='<label><input type="checkbox" data-o="modelo"'+(O.modelo?' checked':'')+'><span>Con la descripción modelo en la pantalla<small>Léela en voz alta, despacio, para sentir cuánto dura cada pregunta (el tiempo se ajusta al texto). Después, inténtalo sin ella.</small></span></label>';
  o+='<label><input type="checkbox" data-o="beep"'+(O.beep?' checked':'')+'><span>Sonido al cambiar de pregunta</span></label>';
 }
 o+='<label><input type="checkbox" data-o="rec"'+(O.rec?' checked':'')+'><span>Grabarme (opcional)<small>La grabación se queda en tu ordenador o tu móvil: no se envía a ningún sitio y se borra al cerrar la página (al final puedes guardarla en Descargas). El navegador te pedirá permiso para usar el micrófono; mientras grabas, la barrita verde se mueve cuando hablas.</small></span></label>';
 o+='</div><div class="row"><button class="btn cta" data-act="start">Empezar</button></div>';
 o+='<details><summary>Palabras útiles para esta foto</summary><p>'+f.pal.map(esc).join(' · ')+'</p></details>';
 o+='<details><summary>Ver la descripción modelo</summary><p class="small muted">Mejor después de practicar: primero inténtalo tú.</p>'+modelHTML(f)+'</details>';
 o+='</div></div>';
 $('pr').innerHTML=o;
}

/* ---------------- sonido, pantalla, grabacion ---------------- */
var AC=null, WL=null;
function beep(){
 if(!S.o.beep || S.o.mode!=='guiado' || !AC) return;
 try{ var t=AC.currentTime, os=AC.createOscillator(), g=AC.createGain(); os.type='sine'; os.frequency.value=660;
  g.gain.setValueAtTime(0.0001,t); g.gain.exponentialRampToValueAtTime(0.25,t+0.02); g.gain.exponentialRampToValueAtTime(0.0001,t+0.35);
  os.connect(g); g.connect(AC.destination); os.start(t); os.stop(t+0.4); }catch(e){}
}
function wake(on){
 try{ if(on && navigator.wakeLock){ navigator.wakeLock.request('screen').then(function(w){ WL=w; }, function(){}); } else if(!on && WL){ WL.release(); WL=null; } }catch(e){}
}
var REC={stream:null, mr:null, chunks:[], url:null, ext:'webm', err:''};
function recType(){
 if(!window.MediaRecorder || !MediaRecorder.isTypeSupported) return '';
 var ts=['audio/mp4','audio/webm;codecs=opus','audio/webm','audio/ogg'];
 for(var i=0;i<ts.length;i++) if(MediaRecorder.isTypeSupported(ts[i])) return ts[i];
 return '';
}
function recClear(){ if(REC.url){ try{ URL.revokeObjectURL(REC.url); }catch(e){} } REC.url=null; REC.chunks=[]; }
function recPrepare(done){
 REC.err=''; REC.used=false; recClear();
 /* por si una grabacion anterior se quedo colgada (Safari): se suelta del todo */
 if(REC.mr){ var old=REC.mr; REC.mr=null; try{ if(old.state!=='inactive') old.stop(); }catch(e){} }
 if(REC.stream){ try{ REC.stream.getTracks().forEach(function(k){ k.stop(); }); }catch(e){} REC.stream=null; }
 if(!S.o.rec){ done(); return; }
 REC.used=true;
 if(!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia || !window.MediaRecorder){ REC.err='Este navegador no puede grabar. Practica sin grabación o prueba con otro navegador.'; done(); return; }
 navigator.mediaDevices.getUserMedia({audio:true}).then(function(st){ REC.stream=st; done(); }, function(){ REC.err='No hay permiso para usar el micrófono: practicas sin grabación.'; done(); });
}
function recStart(){
 if(!REC.stream || REC.mr) return;
 var st=REC.stream, t=recType(), mr, chunks=[];
 REC.ext = t.indexOf('mp4')>=0 ? 'm4a' : (t.indexOf('ogg')>=0 ? 'ogg' : 'webm');
 try{ mr = t ? new MediaRecorder(st,{mimeType:t}) : new MediaRecorder(st); }catch(e){ REC.err='No se ha podido empezar a grabar.'; return; }
 REC.mr=mr;
 mr.ondataavailable=function(e){ if(e.data && e.data.size) chunks.push(e.data); };
 mr.onstop=function(){
  /* cada grabacion solo toca lo suyo: su microfono y su audio */
  try{ st.getTracks().forEach(function(k){ k.stop(); }); }catch(e){}
  if(REC.stream===st) REC.stream=null;
  if(REC.mr!==mr) return;
  REC.mr=null;
  if(chunks.length){ var b=new Blob(chunks,{type:mr.mimeType||t||'audio/webm'}); REC.url=URL.createObjectURL(b); }
  else REC.err='No se ha grabado nada esta vez. Vuelve a cargar la página y prueba otra vez; si sigue igual, prueba con otro navegador (Chrome o Safari).';
  var a=$('recout'); if(a) a.innerHTML=recBlock();
 };
 try{ mr.start(); }catch(e){ REC.mr=null; REC.err='No se ha podido empezar a grabar.'; return; }
 lvStart(); R.recSince=now(); R.micWarned=false;
}
var LV={an:null, buf:null, max:0, src:null, g:null};
function lvStart(){ try{ if(!AC||!REC.stream) return; LV.src=AC.createMediaStreamSource(REC.stream); LV.an=AC.createAnalyser(); LV.an.fftSize=512; LV.buf=new Uint8Array(LV.an.fftSize);
 LV.g=AC.createGain(); LV.g.gain.value=0; LV.src.connect(LV.an); LV.an.connect(LV.g); LV.g.connect(AC.destination); LV.max=0; }catch(e){ LV.an=null; } }
function lvRead(){ if(!LV.an) return -1; try{ LV.an.getByteTimeDomainData(LV.buf); }catch(e){ return -1; } var m=0; for(var i=0;i<LV.buf.length;i++){ var v=Math.abs(LV.buf[i]-128); if(v>m) m=v; } if(m>LV.max) LV.max=m; return m/128; }
function lvStop(){ try{ if(LV.src) LV.src.disconnect(); if(LV.g) LV.g.disconnect(); }catch(e){} LV.an=null; LV.src=null; LV.g=null; }
function recPause(p){ /* no se pausa el grabador: en Safari pausar puede dejar la grabacion vacia */ }
function recStop(){
 lvStop();
 if(REC.mr && REC.mr.state!=='inactive'){ try{ REC.mr.stop(); }catch(e){ REC.mr=null; } }
 else { REC.mr=null; if(REC.stream){ try{ REC.stream.getTracks().forEach(function(k){ k.stop(); }); }catch(e){} REC.stream=null; } }
 /* si el navegador no avisa del final de la grabacion, a los 4 s se dice algo en vez de dejarlo en blanco */
 setTimeout(function(){ if(REC.mr && REC.mr.state==='inactive'){ REC.mr=null; if(!REC.url) REC.err='No se ha grabado nada esta vez. Vuelve a cargar la p\u00E1gina y prueba otra vez.'; var a=$('recout'); if(a) a.innerHTML=recBlock(); } }, 4000);
}
function recBlock(){
 if(REC.url) return '<h4>Escúchate</h4><audio controls src="'+REC.url+'"></audio><div class="row" style="margin:6px 0"><a class="btn sm" href="'+REC.url+'" download="mi_descripcion_foto'+S.foto+'.'+REC.ext+'">Guardar el audio en mi dispositivo</a><button class="btn sm" data-act="delrec">Borrar la grabación</button></div>'+
  '<p class="small muted">La grabaci\u00F3n no se guarda sola: est\u00E1 en esta p\u00E1gina hasta que la cierras o haces otra. Si quieres conservarla, pulsa \u00ABGuardar el audio en mi dispositivo\u00BB y la tendr\u00E1s en tu carpeta de Descargas.</p><p class="small muted">Al escucharte, fíjate: ¿hablas despacio y claro? ¿Haces una pausa entre una pregunta y otra? Escucha también la descripción modelo de abajo y compara.</p>';
 if(REC.mr) return '<p class="small muted">Preparando la grabación...</p>';
 if(REC.err) return '<div class="warnbox">'+REC.err+'</div>';
 if(REC.used) return '<p class="small muted">No hay grabaci\u00F3n.</p>';
 return '';
}

/* ---------------- practica: estado ---------------- */
var R={active:false, mode:'', phase:0, phases:[], t0:0, acc:0, paused:false, timer:null, spoken:0, speakStart:0, warned:false};
function now(){ return (window.performance&&performance.now)?performance.now():Date.now(); }
function elapsed(){ return R.acc + (R.paused?0:(now()-R.t0)/1000); }
function startRun(){
 var f=F(S.foto); if(!f) return;
 try{ if(!AC){ var C=window.AudioContext||window.webkitAudioContext; if(C) AC=new C(); } if(AC && AC.resume) AC.resume(); }catch(e){}
 $('pr').innerHTML='<p class="muted">Un momento...</p>';
 recPrepare(function(){
  R.active=true; R.mode=S.o.mode; R.paused=false; R.warned=false; R.spoken=0;
  R.phases=[]; R.useNotes = S.o.prep==='notas'; R.notes=[NOTE_DEF,NOTE_DEF,NOTE_DEF,NOTE_DEF,NOTE_DEF,NOTE_DEF];
  if(S.o.prep==='mirar') R.phases.push({k:'prep', d:30});
  if(S.o.prep==='notas') R.phases.push({k:'notas', d:240});
  if(R.mode==='guiado'){ for(var i=0;i<6;i++) R.phases.push({k:'q', i:i, d:(S.o.modelo ? Math.max(S.o.ritmo, Math.round(curF().ws[i]/2)+3) : S.o.ritmo)}); }
  else R.phases.push({k:'libre'});
  R.phase=0; wake(true); renderRun(); enterPhase(0);
  R.timer=setInterval(tick, 200);
 });
}
function enterPhase(n){
 R.phase=n; R.acc=0; R.t0=now(); R.paused=false;
 var ph=R.phases[n];
 document.body.classList.toggle('notas', ph.k==='notas');
 if(ph.k==='q' || ph.k==='libre') recStart();
 if(ph.k==='q' && n>0) beep();
 renderPhase(); tick();
}
function curF(){ return F(S.foto); }
function renderRun(){
 var f=curF(); document.body.classList.add('focus');
 $('pr').innerHTML='<div class="run"><div class="side">'+figure(f,true)+'<div class="mini" aria-hidden="true"><span id="minil"></span><b id="minic"></b></div></div><div><div class="pan" id="pan" aria-live="polite"></div>'+
  '<div class="warnbox" id="micw" hidden><b>No llega sonido del micr\u00F3fono.</b> Revisa que el navegador tiene permiso para usarlo (en el Mac: Ajustes del Sistema &gt; Privacidad y seguridad &gt; Micr\u00F3fono) y que no est\u00E1 silenciado. Puedes seguir practicando sin grabaci\u00F3n.</div>'+
  '<div class="row"><button class="btn" data-act="pause" id="bpause">Pausa</button><button class="btn" data-act="stop">Parar</button></div></div></div>';
}
function renderPhase(){
 var f=curF(), ph=R.phases[R.phase], o='';
 var recd = (REC.stream && (ph.k==='q'||ph.k==='libre')) ? ' <span class="recdot">Grabando</span><span class="lvl" title="Nivel del micr\u00F3fono"><i id="lvl"></i></span>' : '';
 if(ph.k==='prep'){
  o='<div class="kk">PREPARACIÓN'+recd+'</div><h3>Mira la foto en silencio</h3><div class="clock" id="clk">0:30</div><div class="bar"><i id="br"></i></div>'+
   '<p>Busca: ¿cuántas personas hay? ¿Qué llevan? ¿Qué hay al fondo? ¿Qué está pasando?</p><div class="row"><button class="btn cta" data-act="skip">Ya estoy listo</button></div>';
 } else if(ph.k==='notas'){
  o='<div class="kk">PREPARACI\u00D3N \u00B7 TUS NOTAS</div><h3>Rellena el esquema: solo palabras clave</h3><div class="clock" id="clk">4:00</div><div class="bar"><i id="br"></i></div>'+
   '<div class="leg"><span><b>\u2022</b>veo</span><span><b>+</b>detalle</span><span><b>\u2192</b>opini\u00F3n</span></div>'+esqEdit(R.notes)+
   (S.n[S.foto]?'<div class="row" style="margin:6px 0"><button class="btn sm" data-act="oldnotes">Usar mis notas de la otra vez</button></div>':'')+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="skip">Ya he terminado: a hablar</button></div>';
 } else if(ph.k==='q'){
  var q=D.pl[ph.i], dots='';
  for(var d=0; d<6; d++) dots+='<i class="'+(d<ph.i?'d':(d===ph.i?'c':''))+'"></i>';
  o='<div class="kk">PREGUNTA '+(ph.i+1)+' DE 6'+recd+'</div><div class="dots" aria-hidden="true">'+dots+'</div><h3>'+esc(q.c)+'</h3><p class="small muted" style="margin-top:-6px">'+esc(q.o)+'</p>'+
   '<div class="clock" id="clk"></div><div class="bar"><i id="br"></i></div><!--N-->';
  if(S.o.modelo){ o+='<p class="modtxt">'+f.mod[ph.i]+'</p>'; }
  else {
   o+='<ul class="esc">'+D.esc.map(function(e,k){ return '<li id="es'+k+'">'+(k+1)+'. '+esc(e)+'</li>'; }).join('')+'</ul>';
   o+='<div class="chipz">'+q.com.slice(0,4).map(function(c){ return '<span>'+esc(c)+'</span>'; }).join('')+'</div>';
   if(hasNote(ph.i)) o=o.replace('<!--N-->','<div class="myn"><b>TUS NOTAS</b>'+esc(String(R.notes[ph.i]).trim())+'</div>');
   else o+='<div class="fij"><b>Fíjate en:</b> '+esc(f.fij[ph.i])+'</div>';
  }
  o+='<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="next" id="bnext" disabled>Siguiente</button></div>';
 } else {
  o='<div class="kk">MODO EXAMEN'+recd+'</div><h3>Habla de la foto entre 2 y 3 minutos</h3><div class="clock" id="clk">0:00</div><p class="small" id="clmsg"></p>'+
   '<p class="small muted">'+(R.useNotes?'Tus notas, en orden. M\u00EDralas, pero no las leas. ':'')+'Puedes marcar cada pregunta cuando ya has hablado de ella:</p><ul class="chk">'+
   D.pl.map(function(q,k){ return '<li><label><input type="checkbox" class="lq"><span>'+(k+1)+'. '+esc(q.c)+(hasNote(k)?'<span class="lq-n">'+esc(String(R.notes[k]).trim())+'</span>':'')+'</span></label></li>'; }).join('')+'</ul>'+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="finish">Terminar</button></div>'+
   '<div class="warnbox" id="warn" hidden><b id="warnt"></b> En el examen tienes que hablar entre 2 y 3 minutos. ¿Has dicho tres frases en cada pregunta?<div class="row" style="margin:8px 0 0"><button class="btn sm cta" data-act="goon">Sigo hablando</button><button class="btn sm" data-act="finish2">Terminar igualmente</button></div></div>';
 }
 $('pan').innerHTML=o;
}
function tick(){
 if(!R.active) return;
 var ph=R.phases[R.phase], e=elapsed(), clk=$('clk'); if(!clk) return;
 var lv=lvRead(), lb=$('lvl'); if(lb && lv>=0) lb.style.width=Math.min(100, Math.round(Math.sqrt(lv)*160))+'%';
 if(lv>=0 && !R.micWarned && R.recSince && now()-R.recSince>10000){ R.micWarned=true; if(LV.max<1){ var mw=$('micw'); if(mw) mw.hidden=false; } }
 setTimeout(function(){ var ml=$('minil'), mc=$('minic'); if(ml&&mc){ ml.textContent=(ph.k==='q'?(ph.i+1)+'/6 \u00B7 '+D.pl[ph.i].c:(ph.k==='libre'?'Modo examen':'Preparaci\u00F3n')); mc.textContent=clk.textContent; mc.style.color=clk.className.indexOf('red')>=0?'#FF9C85':(clk.className.indexOf('green')>=0?'#8FE3AE':''); }
  var lc=$('lbclk'); if(lc && $('lb').classList.contains('on')) lc.textContent=(ph.k==='q'?(ph.i+1)+'. '+D.pl[ph.i].c+' \u00B7 ':(ph.k==='notas'||ph.k==='prep'?'Preparaci\u00F3n \u00B7 ':''))+clk.textContent; },0);
 if(ph.k==='libre'){
  clk.textContent=mmss(e);
  clk.className='clock'+(e>=180?' red':(e>=120?' green':''));
  var m=$('clmsg'); if(m) m.textContent = e<120 ? 'Sigue: todavía no has llegado a 2 minutos.' : (e<180 ? '¡Bien! Ya estás entre 2 y 3 minutos. Puedes terminar cuando quieras.' : (e<210 ? 'Ya has pasado de 3 minutos: termina tu frase.' : 'En el examen, el examinador te pararía aquí.'));
  return;
 }
 var rem=ph.d-e, fr=Math.min(1,e/ph.d);
 clk.textContent=mmss(Math.ceil(rem)); clk.className='clock'+(rem<=5?' red':'');
 var br=$('br'); if(br) br.style.width=(fr*100)+'%';
 if(ph.k==='q'){
  for(var k=0;k<3;k++){ var li=$('es'+k); if(li) li.classList.toggle('on', fr>=k/3); }
  var bn=$('bnext'); if(bn){ var ready=fr>=2/3; bn.disabled=!ready; bn.textContent = ready ? (R.phase===R.phases.length-1?'Terminar':'Siguiente pregunta') : 'Siguiente (en '+Math.ceil(ph.d*2/3-e)+' s)'; }
 }
 if(rem<=0) advance();
}
function advance(){
 var ph=R.phases[R.phase];
 if(ph.k==='q') R.spoken+=Math.min(elapsed(), ph.d);
 if(ph.k==='notas'){ S.n[S.foto]=R.notes.slice(); save(); window.scrollTo(0,0); }
 if(R.phase<R.phases.length-1) enterPhase(R.phase+1); else finish();
}
function togglePause(){
 if(!R.active) return;
 if(R.paused){ R.paused=false; R.t0=now(); recPause(false); } else { R.acc=elapsed(); R.paused=true; recPause(true); }
 var b=$('bpause'); if(b) b.textContent = R.paused ? 'Seguir' : 'Pausa';
}
function stopRun(silent){
 document.body.classList.remove('focus','notas');
 if(R.timer) clearInterval(R.timer); R.timer=null; R.active=false; wake(false); recStop();
 if(!silent) showSetup();
}
function finish(){
 var secs = R.mode==='libre' ? elapsed() : R.spoken;
 document.body.classList.remove('focus','notas');
 if(R.timer) clearInterval(R.timer); R.timer=null; R.active=false; wake(false); recStop(); beep();
 var h=S.h[S.foto]||[]; h.push({s:Math.round(secs), m:R.mode, d:new Date().toISOString().slice(0,10)}); S.h[S.foto]=h.slice(-10); save(); nav();
 showDone(secs);
}
function showDone(secs){
 var f=curF(), v, cl;
 if(secs<90){ cl='bad'; v='Muy corto. Vuelve a la plantilla: tres frases en cada pregunta. Prueba el modo guiado.'; }
 else if(secs<120){ cl='amb'; v='Casi. Te falta un poco para llegar a 2 minutos: añade un detalle o un «porque» en cada pregunta.'; }
 else if(secs<=180){ cl='ok'; v='¡Perfecto! Entre 2 y 3 minutos, como pide el examen.'; }
 else { cl='amb'; v='Un poco largo. No pasa nada: en el examen, el examinador te para a los 3 minutos. No hace falta decir más.'; }
 var pos=Math.min(100, secs/240*100);
 var h=(S.h[S.foto]||[]).slice(-6).reverse();
 var o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="back">← Otras fotos</button></div>';
 o+='<div class="run"><div class="side">'+figure(f,true)+'</div><div><div class="res"><div class="kk muted small">'+(R.mode==='guiado'?'MODO GUIADO':'MODO EXAMEN')+'</div><div class="big">'+mmss(secs)+'</div>'+
  '<div class="zone" aria-hidden="true"><div class="ok"></div><div class="me" style="left:calc('+pos+'% - 2px)"></div><span style="left:0;transform:none">0</span><span style="left:25%">1 min</span><span style="left:50%">2 min</span><span style="left:75%">3 min</span></div>'+
  '<div class="verd '+cl+'">'+v+'</div>';
 if(h.length>1){ o+='<p class="small" style="margin:8px 0 0"><b>Tus tiempos con esta foto:</b></p><ul class="hist">'+h.map(function(x){ return '<li>'+x.d.split('-').reverse().join('/')+' · '+mmss(x.s)+' ('+(x.m==='guiado'?'guiado':'examen')+')</li>'; }).join('')+'</ul>'; }
 o+='</div><div id="recout">'+recBlock()+'</div>';
 o+='<h4>Revísate</h4><ul class="chk">'+['He hablado de las seis preguntas, en orden.','He dicho al menos tres frases en cada pregunta.','He usado está / están + -ando, -iendo.','He opinado con creo que / parece que... porque...','He usado un pasado (han + participio) y el futuro (van a).','He hecho pausas para respirar y no he corrido.'].map(function(t){ return '<li><label><input type="checkbox"><span>'+t+'</span></label></li>'; }).join('')+'</ul>';
 o+='<details open><summary>La descripción modelo</summary>'+modelHTML(f)+'</details>';
 o+='<div class="row"><button class="btn cta" data-act="again">Otra vez con esta foto</button><button class="btn" data-act="back">Otra foto</button><button class="btn" data-go="opinion">Tu opinión</button></div></div></div>';
 if(R.useNotes){ o+='<h3 style="margin-top:24px">Tus notas y las notas modelo</h3><p class="small muted">Compara: \u00BFtienes algo en las seis casillas? \u00BFSon palabras clave o frases?</p><div class="cmp"><div><h4>Tus notas</h4>'+esqMine(R.notes,'one')+'</div><div><h4>Notas modelo</h4>'+esqStatic(f.notas,'one')+'</div></div>'; }
 else { o+='<details><summary>Ver las notas modelo de esta foto</summary>'+esqStatic(f.notas)+'</details>'; }
 $('pr').innerHTML=o; window.scrollTo(0,0);
}

/* ---------------- opinion ---------------- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o+='<label><input type="radio" name="o4" value="'+i+'"'+(String(S.o4)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o4').innerHTML=o;
 ['o1','o3','o5'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked = r[i].value===S[k]; });
 $('o2').value=S.o2; $('sname').value=S.name;
}
function pack(){
 var L=['CURSO DELE A2 - ORAL TAREA 2: DESCRIBE LA FOTO', 'Nombre: '+(S.name||'-'), '', 'Mis tiempos:'];
 var any=false;
 D.fotos.forEach(function(f){ var h=S.h[f.id]; if(h&&h.length){ any=true; L.push('  Foto '+f.id+' ('+f.t+'): '+h.map(function(x){ return mmss(x.s)+' '+(x.m==='guiado'?'guiado':'examen'); }).join(' > ')); } });
 if(!any) L.push('  (todavia no he practicado)');
 L.push('', '1. El modo guiado me ha ayudado: '+(S.o1||'-'), '2. El esquema de las seis casillas me ha servido: '+(S.o5||'-'), '3. Al escucharme / falta: '+(S.o2||'-'), '4. Me cuesta mas: '+(S.o3||'-'), '5. Sensacion de control (1-10): '+(S.o4||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 pick:function(b){ S.foto=+b.getAttribute('data-id'); save(); showSetup(); window.scrollTo(0,0); },
 random:function(){ var ids=D.fotos.map(function(f){ return f.id; }).filter(function(id){ return id!==S.foto; }); if(!ids.length) ids=[D.fotos[0].id]; S.foto=ids[Math.floor(Math.random()*ids.length)]; save(); showSetup(); window.scrollTo(0,0); },
 back:function(){ if(R.active) stopRun(true); showPick(); window.scrollTo(0,0); },
 start:function(){ startRun(); window.scrollTo(0,0); },
 skip:function(){ advance(); },
 next:function(b){ if(!b.disabled) advance(); },
 pause:function(){ togglePause(); },
 stop:function(){ stopRun(false); },
 finish:function(){ var e=elapsed(); if(e<120 && !R.warned){ R.warned=true; $('warnt').textContent='Solo llevas '+mmss(e)+'.'; $('warn').hidden=false; return; } finish(); },
 finish2:function(){ finish(); },
 goon:function(){ $('warn').hidden=true; },
 again:function(){ showSetup(); window.scrollTo(0,0); },
 delrec:function(){ recClear(); var a=$('recout'); if(a) a.innerHTML=''; },
 print:function(b){ if(b.getAttribute('data-p')==='sheet'){ document.body.classList.add('ps'); window.print(); setTimeout(function(){ document.body.classList.remove('ps'); },500); return; }
  var v=$('v-plantilla'); v.classList.add('printme'); window.print(); setTimeout(function(){ v.classList.remove('printme'); },500); },
 zoom:function(b){ var f=F(+b.getAttribute('data-id')); if(!f) return; $('lbimg').src=f.img; $('lbimg').alt=f.alt; $('lbt').textContent=f.t; $('lbclk').textContent=''; $('lb').classList.add('on'); tick(); },
 unzoom:function(){ $('lb').classList.remove('on'); },
 oldnotes:function(){ if(S.n[S.foto]){ R.notes=S.n[S.foto].slice(); renderPhase(); tick(); } },
 copy:function(){
  var t=pack(), box=$('cbox');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar automáticamente. Escribe tus respuestas en un correo para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
 }
};
document.addEventListener('click', function(e){
 if(e.target.tagName==='IMG' && e.target.closest('.run figure.ph')){ var bz=e.target.closest('figure').querySelector('[data-act=zoom]'); if(bz){ ACTS.zoom(bz); return; } }
 if(e.target.id==='lb'||e.target.id==='lbimg'){ $('lb').classList.remove('on'); return; }
 var g=e.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.name==='md'){ S.o.mode=t.value; save(); showSetup(); return; }
 if(t.id==='ritmo'){ S.o.ritmo=+t.value; save(); return; }
 if(t.getAttribute && t.getAttribute('data-o')){ S.o[t.getAttribute('data-o')]=t.checked; save(); return; }
 if(t.id==='prepsel'){ S.o.prep=t.value; save(); return; }
 if(t.name==='o1'||t.name==='o3'||t.name==='o4'||t.name==='o5'){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){ var t=e.target;
 if(t.getAttribute && t.getAttribute('data-ni')!==null){ var i=+t.getAttribute('data-ni'); R.notes[i]=t.value; t.parentNode.classList.toggle('many', tooLong(t.value)); return; }
 if(t.id==='o2'){ S.o2=t.value; save(); nav(); } if(t.id==='sname'){ S.name=t.value; save(); } });
document.addEventListener('keydown', function(e){ if(e.key==='Escape' && $('lb').classList.contains('on')){ $('lb').classList.remove('on'); return; } if(R.active && e.code==='Space' && e.target===document.body){ e.preventDefault(); togglePause(); } });
document.addEventListener('visibilitychange', function(){ if(document.hidden && R.active && !R.paused) togglePause(); });
window.addEventListener('afterprint', function(){ var v=$('v-plantilla'); if(v) v.classList.remove('printme'); document.body.classList.remove('ps'); });

renderScale(); renderPrep();
var start=S.cur; S.cur=start; go(start);
if(start==='practica' && S.foto) showSetup();
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_T2, body, js))

# ------------------------------------------------------------ prompts y nombres.txt
with open("M4T2_prompts_imagenes.txt", "w", encoding="utf-8") as fp:
    fp.write("PROMPTS DE LAS FOTOS · ORAL TAREA 2 (curso DELE A2, Modulo 4)\n")
    fp.write("Formato 3:2, horizontal. Despues: accion rapida Imagen DELE (1600 px, 90 KB).\n\n")
    for f in B.FOTOS:
        if f["id"] in getattr(B, "TANDA_ACTUAL", ids):
            fp.write("M4T2_foto%d  ·  %s\n%s\n\n" % (f["id"], f["titulo"], f["prompt"]))
def ascii_desc(s):
    s = s.replace("ñ", "n").replace("Ñ", "N")
    for a, b in zip("áéíóúüÁÉÍÓÚÜ", "aeiouuAEIOUU"): s = s.replace(a, b)
    return re.sub(r"[\"'«»]", "", s)
with open("nombres.txt", "w", encoding="utf-8") as fp:
    fp.write("CARPETA: DELE_A2_curso\n")
    for f in B.FOTOS:
        if f["id"] not in getattr(B, "TANDA_ACTUAL", ids): continue
        fp.write("M4T2_foto%d | 1600 | 90 | %s\n" % (f["id"], ascii_desc("Oral T2 foto %d %s" % (f["id"], f["perfil"]["situacion"]))))

print("ok", FILE, "·", len(B.FOTOS), "fotos ·", ", ".join("%d: %d palabras" % (f["id"], f["w"]) for f in FOTOS_JS))
