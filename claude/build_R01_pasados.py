# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R01 DEL CURSO DE PREPARACION DELE A2: LOS PASADOS Y LAS PREGUNTAS
# Uso: python3 build_R01_pasados.py  -> DELEA2_curso_R01_pasados.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# Contenidos: solo en banco_R01_pasados.py. Este archivo monta la pagina y comprueba el banco.
# Ejemplos propios (no los de la pildora de 2ST ni los de las fichas de AIL, que los estudiantes pueden tener).
# Enfoque: gramatica cognitiva (imperfecto = la accion desde dentro, en proceso; indefinido =
# desde fuera, con su final; perfecto = la ventana de ahora). Espanol de Espana.
import json, re, sys
from curso_comun import CSS, EMAIL, page
import banco_R01_pasados as B

TITLE = "Los pasados y las preguntas"
FILE = "DELEA2_curso_R01_pasados.html"
STORAGE = "dele-a2-curso-R01"

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
MARK = re.compile(r"\[(f|i|v):([^\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")

def chk_marks(s, where):
    rest = MARK.sub("", s)
    if "[" in rest or "]" in rest: err("marca mal cerrada en " + where + ": " + s[:60])

def chk_gaps(s, where):
    n = 0
    for g in GAP.findall(s):
        n += 1
        if "#" not in g: err("hueco sin motivo en %s: %s" % (where, g)); continue
        ops, mot = g.split("#")
        ops = ops.split("|")
        if len(ops) != 3 or len(set(ops)) != 3: err("hueco sin 3 opciones distintas en %s: %s" % (where, g))
        if mot not in B.MOTIVOS: err("motivo desconocido en %s: %s" % (where, mot))
    if n == 0: err("texto sin huecos: " + where)
    if "[[" in GAP.sub("", s): err("hueco mal cerrado en " + where)
    return n

for i, p in enumerate(B.PARES):
    for k in ("a", "b"): chk_marks(p[k], "par %d" % i)
    if "[i:" not in p["a"] or "[f:" not in p["b"]: err("par %d: a debe llevar imperfecto y b indefinido" % i)
for s, _ in B.ERA_FUE: chk_marks(s, "era/fue")
for t, s in B.HISTORIA:
    chk_marks(s, "historia")
    if t not in "ADV": err("tipo de trozo desconocido en la historia")
    if t == "A" and "[f:" not in s: err("trozo de accion sin indefinido: " + s)
    if t == "D" and ("[i:" not in s or "[f:" in s): err("trozo de decorado sin imperfecto (o con indefinido): " + s)
if "".join(t for t, _ in B.HISTORIA).count("A") < 4: err("la historia necesita al menos 4 acciones")
for q, a, t in B.PREG_TABLA:
    chk_marks(q, "tabla preguntas"); chk_marks(a, "tabla preguntas")
    if t not in B.TIEMPOS: err("tiempo desconocido en la tabla de preguntas")
for row in B.SALTO:
    for s in row: chk_marks(s, "salto")
    if "[v:" not in row[0] or "[f:" not in row[2]: err("el salto debe ir de perfecto a indefinido: " + row[0])
for a, b in B.PAUTA_PREGUNTA:
    chk_marks(b, "pauta-pregunta")
    if not b.startswith("¿"): err("la pregunta directa debe abrir con ¿: " + b)

def chk_quiz(items, name, nmin, bm=False):
    if len(items) < nmin: err("%s: hacen falta al menos %d items" % (name, nmin))
    for it in items:
        if not it.get("why"): err("%s: item sin explicacion: %s" % (name, it["q"][:40]))
        if bm:
            if it["ok"] not in (0, 1): err(name + ": ok debe ser 0 (bien) o 1 (mal)")
            if it["ok"] == 1 and not it.get("fix"): err(name + ": frase mal sin correccion: " + it["q"])
            if it["ok"] == 0 and it.get("fix"): err(name + ": frase bien con correccion: " + it["q"])
        else:
            o = it["o"]
            if len(o) < 2 or len(set(o)) != len(o): err("%s: opciones repetidas o insuficientes: %s" % (name, it["q"][:40]))
chk_quiz(B.P_TIEMPO, "P_TIEMPO", 10); chk_quiz(B.P_COMPLETA, "P_COMPLETA", 12); chk_quiz(B.P_HAZ, "P_HAZ", 8)
chk_quiz(B.E_PROCESO, "E_PROCESO", 8); chk_quiz(B.E_BIENMAL, "E_BIENMAL", 10, bm=True)
if not any(i["ok"] == 0 for i in B.E_BIENMAL) or not any(i["ok"] == 1 for i in B.E_BIENMAL): err("bien/mal: hacen falta de los dos tipos")
for it in B.P_COMPLETA + B.ORAL:
    if it["q"].count("____") != 1: err("un solo hueco ____ por pregunta: " + it["q"])
for it in B.P_HAZ:
    if not it["o"][0].lstrip("—").startswith("¿") and "¿" not in it["o"][0]: err("la respuesta buena de P_HAZ debe tener pregunta: " + it["o"][0])
    for o in it["o"]:
        if o.count("?") != o.count("¿"): err("signos de interrogacion descompensados: " + o)

ngaps = {}
for t in B.TEXTOS: ngaps[t["id"]] = chk_gaps(t["texto"], t["id"])
for i, t in enumerate(B.ANTES_AHORA):
    n = chk_gaps(t["texto"], "antes-ahora %d" % i)
    if n != 2: err("antes-ahora %d: dos huecos (antes y el cambio)" % i)
    first = GAP.findall(t["texto"])[0].split("#")[1]
    if first != "cost": err("antes-ahora %d: el primer hueco es la costumbre de antes" % i)
# Los textos tienen que trabajar los tres tiempos
alltex = " ".join(t["texto"] for t in B.TEXTOS)
for tt in ("indef", "imperf", "perf"):
    if not any(B.MOTIVOS[g.split("#")[1]][0] == tt for g in GAP.findall(alltex)): err("los textos no trabajan el " + tt)
for o in B.ORAL:
    chk_marks(o["modelo"], "oral")
    if "¿" not in o["modelo"]: err("la respuesta modelo oral devuelve la pregunta: " + o["q"])
for L in B.LAMINAS:
    if len(L["pautas"]) != 5: err("lamina %s: 5 pautas" % L["id"])
    for _, ts in L["pautas"]:
        for t in ts:
            if t not in B.TIEMPOS: err("tiempo desconocido en lamina " + L["id"])
for d in B.DETECTOR:
    try: re.compile(d["re"])
    except re.error as e: err("regex del detector: %s (%s)" % (d["re"], e))
    if d["t"] not in B.TIEMPOS: err("tiempo desconocido en el detector")
if ERR:
    print("\n".join("ERROR: " + e for e in ERR)); sys.exit(1)

# ------------------------------------------------------------------ HTML ESTATICO
COL = {"indef": "f", "imperf": "i", "perf": "v"}
def mk(s):
    return MARK.sub(lambda m: '<span class="t%s">%s</span>' % (m.group(1), m.group(2)), s)

CSS_R = CSS + r"""
:root{--tf:#C2410C;--tf-soft:#FDE7DA;--ti:#9A6200;--ti-soft:#FBF0DA;--tv:#17707F;--tv-soft:#DDF0F2}
.tf,.ti,.tv{font-weight:700;border-radius:4px;padding:0 3px}
.tf{color:var(--tf);background:var(--tf-soft)}.ti{color:var(--ti);background:var(--ti-soft)}.tv{color:var(--tv);background:var(--tv-soft)}
.cams{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;border-top:6px solid}
.cam.i{border-top-color:var(--ti)}.cam.f{border-top-color:var(--tf)}.cam.v{border-top-color:var(--tv)}
.cam .k{font-size:.78rem;font-weight:700;letter-spacing:.06em}
.cam.i .k{color:var(--ti)}.cam.f .k{color:var(--tf)}.cam.v .k{color:var(--tv)}
.cam h3{margin:2px 0 6px}.cam p{margin:0;font-size:.95rem}
.cam .ej{margin-top:8px;font-size:.92rem;background:var(--paper);border-radius:8px;padding:6px 10px}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pill.ok{border-color:var(--ok)}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.duo button{font:inherit;text-align:left;border:2px solid var(--line);background:#fff;border-radius:10px;padding:10px 12px;cursor:pointer;line-height:1.45}
.duo button.on.i{border-color:var(--ti);background:var(--ti-soft)}.duo button.on.f{border-color:var(--tf);background:var(--tf-soft)}
.duo button small{display:block;font-size:.75rem;font-weight:700;letter-spacing:.05em;color:var(--muted);margin-bottom:2px}
svg.dg{width:100%;height:auto;display:block;margin:6px 0}
.expl{border-radius:8px;padding:10px 14px;margin-top:6px}
.expl.i{background:var(--ti-soft)}.expl.f{background:var(--tf-soft)}
.ef{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ef div{background:var(--paper);border-radius:8px;padding:8px 12px;font-size:.95rem}
.ef div b{display:block;font-weight:400;margin-bottom:2px}
.story{font-size:1.08rem;line-height:1.9;background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 20px}
.story .seg{transition:opacity .2s}
.story .seg.off{display:none}
.story .seg.D{border-bottom:2px dotted var(--ti)}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;margin:8px 0}
.mk3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.mk3 div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:.93rem}
.mk3 h4{margin:0 0 6px}
.mk3 .i h4{color:var(--ti)}.mk3 .f h4{color:var(--tf)}.mk3 .v h4{color:var(--tv)}
.mk3 ul{margin:0;padding-left:1.1em}
.salto{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;align-items:stretch;margin:6px 0}
.salto div{background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px 10px;font-size:.93rem}
.salto div:last-child{border-color:var(--tf)}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.tchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px}
.tchip.indef{background:var(--tf-soft);color:var(--tf)}.tchip.imperf{background:var(--ti-soft);color:var(--ti)}.tchip.perf{background:var(--tv-soft);color:var(--tv)}
.qz{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0}
.qz .cnt{font-size:.85rem;color:var(--muted)}
.qz .qq{font-size:1.05rem;margin:6px 0 10px}
.qz .ops{display:grid;gap:8px}
.qz .ops button{font:inherit;text-align:left;border:2px solid var(--line);background:#fff;border-radius:10px;padding:9px 12px;cursor:pointer}
.qz .ops.bm{grid-template-columns:1fr 1fr}
.qz .ops.bm button{text-align:center;font-weight:600}
.qz .ops button:disabled{cursor:default}
.qz .ops button.good{border-color:var(--ok);background:var(--ok-soft)}
.qz .ops button.bad{border-color:var(--bad);background:var(--bad-soft)}
.fb{margin-top:10px;border-radius:8px;padding:9px 13px;font-size:.95rem}
.fb.good{background:var(--ok-soft)}.fb.bad{background:var(--bad-soft)}
.row[hidden]{display:none}
.prog{height:8px;background:var(--line);border-radius:99px;overflow:hidden;margin:6px 0 10px}
.prog i{display:block;height:100%;background:var(--coral);width:0}
.score{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:16px 18px;margin:12px 0}
.score b.big{font-family:Georgia,serif;font-size:2rem}
.cz{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0;line-height:2.1}
.cz select{font:inherit;font-size:.95rem;border:2px solid #CFC6BB;border-radius:6px;padding:1px 4px;background:#fff;max-width:100%}
.cz select.ok{border-color:var(--ok);background:var(--ok-soft);color:var(--ok);font-weight:600}
.cz select.no{border-color:var(--bad);background:var(--bad-soft)}
.cz sup{font-size:.7rem;color:var(--muted);font-weight:700;margin-right:2px}
.cz .tema{font-family:Georgia,serif;font-weight:700;display:block;line-height:1.4}
.fbl{list-style:none;padding:0;margin:8px 0;font-size:.93rem}
.fbl li{padding:6px 10px;border-radius:8px;margin:4px 0}
.fbl li.ok{background:var(--ok-soft)}.fbl li.no{background:var(--bad-soft)}
.lam{background:#fff;border:2px solid var(--ink);border-radius:4px;padding:16px 20px;margin:12px 0}
.lam .h{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--muted)}
.lam .msg{border-left:4px solid var(--line);padding:6px 12px;margin:8px 0;font-style:italic;background:var(--paper)}
.lam ul{margin:6px 0;padding-left:1.2em}
.lam li{margin:3px 0}
textarea.wr{width:100%;min-height:220px;font:inherit;font-size:1.02rem;line-height:1.7;border:1.5px solid #CFC6BB;border-radius:8px;padding:12px 14px;background:#fff}
.rv{list-style:none;padding:0;margin:8px 0}
.rv li{border-radius:8px;padding:8px 12px;margin:6px 0;font-size:.95rem}
.rv li.r{background:var(--bad-soft)}.rv li.a{background:var(--amb-soft)}.rv li.n{background:var(--paper)}.rv li.g{background:var(--ok-soft)}
.rv mark{background:#FFE58A;border-radius:3px;padding:0 2px}
.check{list-style:none;padding:0;margin:8px 0}
.check li{padding:5px 0}
.check label{cursor:pointer}
.ocard{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:18px 20px;margin:12px 0}
.ocard .qq{font-size:1.15rem;font-family:Georgia,serif}
.tbar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:10px 0}
.tbar i{display:block;height:100%;background:var(--coral);width:0;transition:width .25s linear}
.esc{display:grid;gap:6px;margin:8px 0}
.esc div{border:2px dashed var(--line);border-radius:8px;padding:6px 10px;color:var(--muted)}
.esc div.on{border-style:solid;border-color:var(--coral);color:var(--ink);background:var(--coral-soft)}
.model{background:var(--paper);border-radius:8px;padding:10px 14px;margin-top:8px;line-height:1.8}
.scale{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.scale label{cursor:pointer}
.scale input{position:absolute;opacity:0}
.scale span{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;border:2px solid var(--line);background:#fff;font-weight:700}
.scale input:checked + span{background:var(--ink);border-color:var(--ink);color:#fff}
.opn label.q{display:block;font-weight:600;margin:18px 0 6px}
.opn textarea{width:100%;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;min-height:80px;background:#fff}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips label{border:2px solid var(--line);border-radius:999px;padding:5px 14px;cursor:pointer;background:#fff}
.chips label:has(input:checked){border-color:var(--ink);background:var(--ink);color:#fff}
.chips input{position:absolute;opacity:0}
.sendbox{border:2px solid var(--coral);border-radius:12px;padding:18px 22px;margin:26px 0;background:#fff}
.sendbox input[type=text]{width:100%;max-width:360px;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 12px;margin-top:6px}
#v-resumen{display:none}
@media (max-width:700px){.salto.sh{display:none}.salto{margin-bottom:14px}.cams,.mk3,.salto{grid-template-columns:1fr}.duo,.ef{grid-template-columns:1fr}.qz .ops.bm{grid-template-columns:1fr 1fr}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:13px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.mk3 div{break-inside:avoid}}
"""

def cams():
    return ('<div class="cams">'
      '<div class="cam i"><div class="k">IMPERFECTO</div><h3>Desde dentro</h3><p>Estás <b>dentro</b> de la acción, en medio. No ves el final. Es el <b>proceso</b> y el <b>decorado</b> de la historia.</p>'
      '<div class="ej">' + mk("Cuando [i:cruzaba] la calle...") + '<br><span class="muted small">Todavía estás en el paso de cebra.</span></div></div>'
      '<div class="cam f"><div class="k">INDEFINIDO</div><h3>Desde fuera</h3><p>Ves la acción <b>entera</b>, con su principio y su <b>final</b>. Es lo que <b>pasó</b>: la historia avanza.</p>'
      '<div class="ej">' + mk("Cuando [f:crucé] la calle...") + '<br><span class="muted small">Ya estás en la otra acera.</span></div></div>'
      '<div class="cam v"><div class="k">PERFECTO</div><h3>La ventana de ahora</h3><p>La acción pasa en un tiempo que <b>todavía no ha terminado</b>: hoy, este año, en tu vida (alguna vez, nunca).</p>'
      '<div class="ej">' + mk("Hoy [v:he cruzado] la calle sin mirar.") + '<br><span class="muted small">Hoy todavía no ha terminado.</span></div></div>'
      '</div>')

def era_fue():
    o = '<div class="ef">'
    for s, e in B.ERA_FUE:
        o += '<div><b>%s</b><span class="muted small">%s</span></div>' % (mk(s), e)
    return o + '</div>'

VENTANA_SVG = """<svg class="dg" viewBox="0 0 640 170" role="img" aria-label="Línea del tiempo: a la izquierda el pasado cerrado (ayer, el sábado, en 2019); a la derecha, hasta ahora, la ventana abierta (hoy, este año, alguna vez, nunca, ya).">
<line x1="20" y1="110" x2="618" y2="110" stroke="#14161C" stroke-width="2.5"/><polygon points="618,104 632,110 618,116" fill="#14161C"/>
<rect x="30" y="66" width="300" height="80" rx="10" fill="#FDE7DA"/>
<text x="180" y="88" text-anchor="middle" font-size="14" font-weight="700" fill="#C2410C">CERRADO · indefinido</text>
<text x="180" y="136" text-anchor="middle" font-size="13" fill="#14161C">ayer · el sábado · en 2019 · hace dos años</text>
<rect x="352" y="30" width="260" height="120" rx="10" fill="#DDF0F2" stroke="#17707F" stroke-width="3"/>
<line x1="482" y1="30" x2="482" y2="150" stroke="#17707F" stroke-width="1.5" opacity=".35"/><line x1="352" y1="90" x2="612" y2="90" stroke="#17707F" stroke-width="1.5" opacity=".35"/>
<text x="482" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="#17707F">VENTANA DE AHORA · perfecto</text>
<text x="417" y="62" text-anchor="middle" font-size="13">hoy</text><text x="547" y="62" text-anchor="middle" font-size="13">este año</text>
<text x="417" y="128" text-anchor="middle" font-size="13">alguna vez · nunca</text><text x="547" y="128" text-anchor="middle" font-size="13">ya · todavía no</text>
<circle cx="606" cy="110" r="7" fill="#E8603C"/><text x="606" y="166" text-anchor="end" font-size="12" font-weight="700">AHORA</text>
</svg>"""

def salto():
    o = '<div class="salto sh" style="font-size:.8rem;font-weight:700;color:var(--muted)"><div style="border:0;background:none">PREGUNTA (ventana abierta)</div><div style="border:0;background:none">RESPUESTA</div><div style="border:0;background:none">AÑADES CUÁNDO: SE CIERRA</div></div>'
    for a, b, c in B.SALTO:
        o += '<div class="salto"><div>%s</div><div>%s</div><div>%s</div></div>' % (mk(a), mk(b), mk(c))
    return o

def marcadores():
    o = '<div class="mk3">'
    for t, cl, nom in (("imperf", "i", "Imperfecto"), ("indef", "f", "Indefinido"), ("perf", "v", "Perfecto")):
        o += '<div class="%s"><h4>%s</h4><ul>%s</ul></div>' % (cl, nom, "".join("<li>%s</li>" % m for m in B.MARCADORES[t]))
    return o + '</div>'

def preg_tabla():
    o = '<table class="t"><thead><tr><th>La pregunta...</th><th>...y la respuesta, con el mismo tiempo</th></tr></thead><tbody>'
    for q, a, t in B.PREG_TABLA:
        o += '<tr><td>%s</td><td>%s</td></tr>' % (mk(q), mk(a))
    return o + '</tbody></table>'

def pauta_preg():
    o = '<table class="t"><thead><tr><th>La pauta dice...</th><th>Tú escribes o dices...</th></tr></thead><tbody>'
    for a, b in B.PAUTA_PREGUNTA:
        o += '<tr><td><i>%s</i></td><td>%s</td></tr>' % (a, mk(b))
    return o + '</tbody></table>'

LEG = ('<div class="legend"><span><span class="ti">imperfecto</span> desde dentro</span>'
       '<span><span class="tf">indefinido</span> desde fuera</span><span><span class="tv">perfecto</span> ventana de ahora</span></div>')

STEPS = [("idea", "La idea"), ("historia", "Contar una historia"), ("preguntas", "Las preguntas"),
         ("practica", "Practica"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_IDEA = """
<h2>Desde dentro o desde fuera</h2>
<p class="lead">El imperfecto y el indefinido no se diferencian por "cuánto dura" la acción ni por "si es más antigua". La diferencia es <b>dónde estás tú cuando la miras</b>: dentro de la acción o fuera de ella. Y el perfecto mira por la ventana de ahora.</p>
__CAMS__
<h3>Mira la diferencia</h3>
<p class="muted small">Elige una pareja de frases y toca cada una. Mira dónde estás tú y cuándo pasa lo otro.</p>
<div class="pills" id="parsel"></div>
<div class="box" id="parvis"></div>
<div class="note"><b>El truco del <i>cuando</i>:</b> <span class="ti">cuando + imperfecto</span> = <b>durante</b> (lo otro pasa en medio). <span class="tf">cuando + indefinido</span> = <b>después</b> (primero una cosa, luego la otra). Y <i>mientras</i> casi siempre va con imperfecto: te mete dentro de la acción.</div>
<h3>¿Era o fue?</h3>
<p>Con <i>ser</i> pasa lo mismo. <span class="ti">era</span> describe cómo era algo (el decorado). <span class="tf">fue</span> mira algo terminado desde fuera: muchas veces, para <b>valorarlo</b>.</p>
__EF__
<h3>La ventana de ahora: el perfecto</h3>
<p>Imagina que hablas desde una ventana. Lo que pasa <b>dentro de la ventana</b> (hoy, esta semana, este año, en toda tu vida) va en perfecto. Lo que está <b>fuera</b>, en un tiempo cerrado (ayer, el sábado, en 2019), va en indefinido.</p>
__VENTANA__
<div class="tip"><b>Español de España.</b> En España, con <i>hoy, esta mañana, este año...</i> usamos el perfecto (<i>hoy he ido</i>). En muchos países de América se usa también el indefinido (<i>hoy fui</i>). En el examen las dos formas son correctas; en este curso practicamos la de España. Lo que no vale en ningún sitio: <b>ayer + perfecto</b> (<span style="text-decoration:line-through">ayer he ido</span>).</div>
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="historia">Siguiente: contar una historia</button></div>
"""

V_HISTORIA = """
<h2>Contar una historia: el decorado y las acciones</h2>
<p class="lead">En la escritura (blog, diario, correo) y en el monólogo de la oral tienes que contar algo que pasó. Toda historia tiene dos capas: el <b>decorado</b> (cómo era todo, qué pasaba alrededor) y las <b>acciones</b> (lo que pasó, una detrás de otra).</p>
<div class="pills" id="stsel">
 <button class="pill on" data-act="story" data-m="all">Toda la historia</button>
 <button class="pill" data-act="story" data-m="A">Solo las acciones</button>
 <button class="pill" data-act="story" data-m="D">Solo el decorado</button>
</div>
<div class="story" id="story"></div>
__LEG__
<div class="note" id="storynote">Prueba los botones. <b>Solo las acciones</b>: la historia se entiende y avanza. <b>Solo el decorado</b>: sabes cómo era todo... pero no pasa nada. Necesitas las dos capas.</div>
<h3>Las palabras que te ayudan</h3>
<p>Algunas palabras suelen ir con un tiempo. No es una regla automática, pero te ayudan mucho a decidir.</p>
__MARC__
<div class="box"><h4>«Durar mucho» no significa imperfecto</h4>
<p style="margin:0">__DUR__ Aunque fueron dos horas o un año, ves la etapa <b>entera</b>, con su final: indefinido.</p></div>
<div class="box"><h4>Un plan que no se hizo: <span class="ti">iba a</span> + infinitivo</h4>
<p style="margin:0">__IBA__ Es perfecto para el examen: «el día que no salió como pensabas», «una semana horrible», disculparte en un correo...</p></div>
<div class="box"><h4>En el examen</h4>
<ul style="margin:0">
<li><b>Oral, tarea 1:</b> las pautas mezclan los tiempos. <i>¿Cómo era?</i> → imperfecto. <i>¿Qué hiciste? ¿Cuándo fue?</i> → indefinido. <i>¿Has vuelto?</i> → perfecto.</li>
<li><b>Escritura, tarea 2:</b> blog o diario: decorado en imperfecto, acciones en indefinido y, al final, una valoración: <span class="tf">fue</span> un día increíble, lo <span class="tf">pasé</span> muy bien.</li>
<li><b>Revisión final:</b> la pasada de los pasados busca justo esto: ¿cada verbo es decorado, acción o ventana de ahora?</li>
</ul></div>
<div class="row"><button class="btn cta" data-go="preguntas">Siguiente: las preguntas</button></div>
"""

V_PREG = """
<h2>Las preguntas: la pregunta te da el tiempo</h2>
<p class="lead">En la oral el examinador te pregunta, y en la tarea 3 tú también tienes que preguntar. En los correos de la escritura casi siempre hay una pauta que dice <i>pregúntale...</i>. La regla de oro: <b>contesta con el mismo tiempo de la pregunta</b>.</p>
__TABLA__
<h3>El salto: de la ventana abierta a la fecha</h3>
<p>Si te preguntan con <i>alguna vez</i> y tú dices <b>cuándo</b> fue, la ventana se cierra: pasas al indefinido. Y <i>¿Cuándo...?</i> siempre pide indefinido.</p>
__SALTO__
<h3>Cómo se hace una buena pregunta</h3>
<div class="box"><ul style="margin:0">
<li><b>¿ al principio y ? al final.</b> En español la pregunta se abre: <i>¿Qué hiciste?</i></li>
<li><b>Con tilde:</b> qué, cómo, dónde, cuándo, cuánto, quién, cuál. <i>¿Dónde vivías?</i> — <i>donde vivía</i> (sin pregunta, sin tilde).</li>
<li><b>Orden:</b> palabra de pregunta + verbo + el resto: <i>¿Cuándo empezaste a estudiar español?</i></li>
<li><b>Preguntas cortas muy útiles:</b> <i>¿Qué tal el viaje? ¿Qué tal te fue? ¿Lo pasaste bien? ¿Y tú?</i></li>
<li><b>Tú o usted:</b> a un amigo, <i>¿Has visto...?</i>; a un hotel o al examinador en una tienda, <i>¿Ha visto usted...?</i></li>
</ul></div>
<h3>De la pauta a la pregunta</h3>
<p>Nunca copies <i>pregúntale</i> ni <i>su</i> de la pauta: escribe la pregunta <b>directa</b>, como si hablaras con esa persona.</p>
__PAUTA__
<h3>Practica</h3>
<div class="pills" id="pqsel">
 <button class="pill on" data-act="pq" data-k="p1">1. ¿Qué tiempo pide?</button>
 <button class="pill" data-act="pq" data-k="p2">2. Completa la pregunta</button>
 <button class="pill" data-act="pq" data-k="p3">3. Haz la pregunta</button>
</div>
<p class="muted small" id="pqinfo"></p>
<div id="pqbox"></div>
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACT = """
<h2>Practica</h2>
<p class="lead">Cuatro ejercicios. Cada respuesta se corrige en el momento, con la explicación.</p>
<div class="pills" id="exsel">
 <button class="pill on" data-act="ex" data-k="e1">1. ¿Proceso o fin?</button>
 <button class="pill" data-act="ex" data-k="e2">2. Elige el pasado</button>
 <button class="pill" data-act="ex" data-k="e3">3. Antes, ahora y el cambio</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Ahora usa los pasados y las preguntas en una tarea del examen: escribe un texto o contesta preguntas en voz alta.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="o">Oral: preguntas en cadena</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu texto y después pulsa <b>Revisar mis pasados</b>: la página busca las palabras que piden un tiempo (ayer, hoy, de niño, alguna vez...) y te dice qué mirar. No corrige el texto: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="ato" hidden>
 <p>Como en la oral: te hacen una pregunta en pasado. Primero elige la forma correcta del verbo. Después <b>contesta en voz alta</b> durante 30 segundos: responde con el mismo tiempo, añade un detalle y devuelve la pregunta (<i>¿Y tú?</i>). También sirve para practicar en pareja.</p>
 <div class="pills" id="orsel"></div>
 <div id="orbox"></div>
</div>
<div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button></div>
"""

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan a mejorarlo. Al final, copia todo (también tus textos y resultados) y envíamelo.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué parte te ha ayudado más?</label>
 <div class="chips" role="group" aria-labelledby="o1l">
  <label><input type="radio" name="o1" value="La idea (desde dentro / desde fuera)">La idea (desde dentro / desde fuera)</label>
  <label><input type="radio" name="o1" value="Contar una historia">Contar una historia</label>
  <label><input type="radio" name="o1" value="Las preguntas">Las preguntas</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tú">Ahora tú</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué te cuesta más ahora?</label>
 <div class="chips" role="group" aria-labelledby="o2l">
  <label><input type="radio" name="o2" value="Imperfecto o indefinido">Imperfecto o indefinido</label>
  <label><input type="radio" name="o2" value="El perfecto">El perfecto</label>
  <label><input type="radio" name="o2" value="Hacer preguntas">Hacer preguntas</label>
  <label><input type="radio" name="o2" value="Contestar con el mismo tiempo">Contestar con el mismo tiempo</label>
 </div>
 <label class="q" id="o3l">3. ¿Te ayuda pensar «desde dentro / desde fuera»?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con los pasados? (1 = nada, 10 = total)</label>
 <div class="scale" role="group" aria-labelledby="o5l" id="o5"></div>
</div>
<div class="sendbox">
 <h3>Envía tus resultados y tus textos a tu profesora</h3>
 <label><b>Tu nombre</b><br><input type="text" id="sname" autocomplete="name"></label>
 <div class="row"><button class="btn cta" data-act="copy">Copiar</button></div>
 <div class="copied-box" id="cbox" role="status" hidden></div>
 <p class="muted small">Pégalo en un correo para tu profesora: __EMAIL__</p>
</div>
"""

def resumen():
    o = '<h2>Los pasados y las preguntas · resumen</h2>' + cams() + VENTANA_SVG
    o += '<h3>Las palabras que te ayudan</h3>' + marcadores()
    o += '<h3>La pregunta te da el tiempo</h3>' + preg_tabla()
    o += '<p><b>El truco del cuando:</b> cuando + imperfecto = durante; cuando + indefinido = después. <b>Iba a</b> + infinitivo = plan que no se hizo. Valoración final de algo terminado: <b>fue</b>, lo <b>pasé</b>.</p>'
    return o

dur = mk("Ayer [f:estuve] dos horas en el médico. Cuando tenía veinte años, [f:viví] un año en París.")
iba = mk("El viernes [i:iba] a cenar con Carla, pero [f:perdí] el autobús y al final [f:cenamos] por videollamada.")
views = {
    "idea": V_IDEA.replace("__CAMS__", cams()).replace("__EF__", era_fue()).replace("__VENTANA__", VENTANA_SVG),
    "historia": V_HISTORIA.replace("__LEG__", LEG).replace("__MARC__", marcadores()).replace("__DUR__", dur).replace("__IBA__", iba),
    "preguntas": V_PREG.replace("__TABLA__", preg_tabla()).replace("__SALTO__", salto()).replace("__PAUTA__", pauta_preg()),
    "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R01</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
""".replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

# ------------------------------------------------------------------ DATOS PARA EL SCRIPT
DATA = {
    "key": STORAGE, "title": TITLE,
    "steps": [{"id": k, "label": l} for k, l in STEPS],
    "motivos": {k: {"t": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "tiempos": {k: v[0] for k, v in B.TIEMPOS.items()},
    "pares": [dict(p, a=mk(p["a"]), b=mk(p["b"])) for p in B.PARES],
    "historia": [{"t": t, "h": mk(s)} for t, s in B.HISTORIA],
    "qz": {
        "p1": {"items": B.P_TIEMPO, "n": 8, "name": "¿Qué tiempo pide?", "info": "Lee la pregunta y elige la respuesta que va con ella (el mismo tiempo)."},
        "p2": {"items": B.P_COMPLETA, "n": 10, "name": "Completa la pregunta", "info": "Elige la forma del verbo. Mira las palabras que te ayudan: alguna vez, anoche, cuando eras pequeño..."},
        "p3": {"items": B.P_HAZ, "n": 7, "name": "Haz la pregunta", "info": "De la pauta o la situación a la pregunta directa. Cuidado con el tiempo y con tú / usted."},
        "e1": {"items": B.E_PROCESO, "n": 8, "name": "¿Proceso o fin?", "info": "Lee la frase y contesta: ¿qué pasa exactamente?"},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Errores típicos de los exámenes. ¿La frase está bien o mal?"},
    },
    "textos": B.TEXTOS, "antes": B.ANTES_AHORA,
    "laminas": B.LAMINAS, "detector": B.DETECTOR,
    "oral": [dict(o, modelo=mk(o["modelo"])) for o in B.ORAL],
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function blank(){ return {cur:'idea', seen:{}, par:0, pv:'a', story:'all', pq:'p1', ex:'e1', etext:D.textos[0].id, at:'w',
  qz:{}, qlog:{}, cz:{}, w:{}, wchk:{}, lam:D.laminas[0].id, oi:0, or:{}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
var TCL = {indef:'f', imperf:'i', perf:'v'};

/* ---------------- navegacion ---------------- */
function stepDone(id){
 if(id==='practica') return ['e1','e4'].some(function(k){ return !!S.qlog[k]; }) || Object.keys(S.cz).length>0;
 if(id==='ahora') return Object.keys(S.w).some(function(k){ return (S.w[k]||'').trim().length>20; }) || Object.keys(S.or).length>0;
 if(id==='opinion') return !!(S.o1||S.o2||S.o3||S.o4||S.o5);
 return !!S.seen[id];
}
function nav(){
 var o='';
 D.steps.forEach(function(st,i){
  var on=S.cur===st.id, done=!on && stepDone(st.id);
  o += '<button type="button" class="'+(on?'on ':'')+(done?'done':'')+'" data-go="'+st.id+'"'+(on?' aria-current="step"':'')+'><span class="n">'+(done?'✓':(i+1))+'</span>'+st.label+'</button>';
 });
 $('steps').innerHTML = o;
}
function go(id){
 S.seen[S.cur]=true; S.cur=id; save();
 var vs=document.querySelectorAll('section.view');
 for(var i=0;i<vs.length;i++) vs[i].classList.toggle('on', vs[i].id==='v-'+id);
 stopTimer(); nav(); window.scrollTo(0,0);
}

/* ---------------- 1. la idea: parejas con diagrama ---------------- */
function diag(mode, acc, ev){
 var o='<svg class="dg" viewBox="0 0 640 170" role="img" aria-label="'+(mode==='a'?'Estás dentro de la acción; lo otro pasa en medio.':'La acción termina; después pasa lo otro.')+'">';
 o += '<line x1="20" y1="104" x2="620" y2="104" stroke="#E6DFD6" stroke-width="2"/>';
 if(mode==='a'){
  o += '<defs><linearGradient id="fd" x1="0" x2="1"><stop offset="0" stop-color="#9A6200"/><stop offset="1" stop-color="#9A6200" stop-opacity="0"/></linearGradient></defs>';
  o += '<line x1="40" y1="96" x2="40" y2="112" stroke="#9A6200" stroke-width="3"/>';
  o += '<rect x="40" y="97" width="290" height="14" rx="3" fill="#9A6200"/><rect x="330" y="97" width="270" height="14" fill="url(#fd)"/>';
  o += '<text x="600" y="132" text-anchor="end" font-size="13" fill="#5E5A55">... no ves el final</text>';
  o += '<circle cx="300" cy="104" r="15" fill="#fff" stroke="#14161C" stroke-width="2.5"/><circle cx="300" cy="104" r="5" fill="#14161C"/>';
  o += '<text x="300" y="156" text-anchor="middle" font-size="13" font-weight="700">tú estás aquí, dentro</text>';
  if(ev){ o += star(300,44)+'<line x1="300" y1="58" x2="300" y2="86" stroke="#E8603C" stroke-width="2" stroke-dasharray="4 3"/><text x="326" y="49" font-size="14" font-weight="700" fill="#14161C">'+esc(ev)+'</text>'; }
 } else {
  o += '<line x1="40" y1="94" x2="40" y2="114" stroke="#C2410C" stroke-width="3"/><line x1="360" y1="94" x2="360" y2="114" stroke="#C2410C" stroke-width="3"/>';
  o += '<rect x="40" y="97" width="320" height="14" rx="3" fill="#C2410C"/>';
  o += '<text x="40" y="84" font-size="12" fill="#5E5A55">empieza</text><text x="360" y="84" text-anchor="middle" font-size="12" fill="#5E5A55">termina</text>';
  o += '<circle cx="200" cy="34" r="15" fill="#fff" stroke="#14161C" stroke-width="2.5"/><circle cx="200" cy="34" r="5" fill="#14161C"/><text x="222" y="39" font-size="13" font-weight="700">tú miras desde fuera: la ves entera</text>';
  if(ev){ o += '<line x1="368" y1="104" x2="452" y2="104" stroke="#14161C" stroke-width="2" marker-end=""/><polygon points="452,98 464,104 452,110" fill="#14161C"/><text x="410" y="96" text-anchor="middle" font-size="12" fill="#5E5A55">después</text>'+star(490,104)+'<text x="490" y="140" text-anchor="middle" font-size="14" font-weight="700">'+esc(ev)+'</text>'; }
  else { o += '<text x="372" y="140" font-size="13" fill="#5E5A55">... y la historia puede seguir</text>'; }
 }
 o += '<text x="'+(mode==='a'?150:200)+'" y="132" text-anchor="middle" font-size="14" fill="#14161C" font-style="italic">'+esc(acc)+'</text>';
 return o+'</svg>';
}
function star(x,y){ var p=[],r1=13,r2=6; for(var i=0;i<10;i++){ var r=i%2?r2:r1, a=Math.PI/5*i-Math.PI/2; p.push((x+r*Math.cos(a)).toFixed(1)+','+(y+r*Math.sin(a)).toFixed(1)); } return '<polygon points="'+p.join(' ')+'" fill="#E8603C"/>'; }
function renderPar(){
 var o=''; D.pares.forEach(function(p,i){ o+='<button class="pill'+(S.par===i?' on':'')+'" data-act="par" data-i="'+i+'">'+esc(p.accion)+'</button>'; });
 $('parsel').innerHTML=o;
 var p=D.pares[S.par], m=S.pv;
 $('parvis').innerHTML = '<div class="duo">'+
  '<button class="i'+(m==='a'?' on':'')+'" data-act="pv" data-m="a" aria-pressed="'+(m==='a')+'"><small>IMPERFECTO · DESDE DENTRO</small>'+p.a+'</button>'+
  '<button class="f'+(m==='b'?' on':'')+'" data-act="pv" data-m="b" aria-pressed="'+(m==='b')+'"><small>INDEFINIDO · DESDE FUERA</small>'+p.b+'</button></div>'+
  diag(m, p.accion, p.evento)+'<div class="expl '+(m==='a'?'i':'f')+'" aria-live="polite">'+(m==='a'?p.ra:p.rb)+'</div>';
}

/* ---------------- 2. historia ---------------- */
function renderStory(){
 var o='', prev='.', H=D.historia;
 function shown(x){ return x && (S.story==='all' || x.t===S.story || (S.story==='A' && x.t==='V')); }
 H.forEach(function(s,i){
  var vis=shown(s), h=s.h;
  if(vis && S.story!=='all'){
   if(/[.!?]\s*$/.test(strip(prev))) h=h.replace(/^(<span class="t."?>)?([a-záéíóú])/, function(m0,a,b){ return (a||'')+b.toUpperCase(); });
   if(/,\s*$/.test(h) && !shown(H[i+1])) h=h.replace(/,\s*$/,'...');
   prev=h;
  }
  o += '<span class="seg '+s.t+(vis?'':' off')+'">'+h+' </span>';
 });
 $('story').innerHTML=o;
 var ps=$('stsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-m')===S.story);
}

/* ---------------- motor de opcion multiple ---------------- */
function qzNew(k){ var c=D.qz[k]; S.qz[k]={order:shuffle(range(c.items.length)).slice(0,c.n), i:0, res:[], perm:{}}; save(); }
function qzRender(k, box){
 var c=D.qz[k]; if(!S.qz[k]) qzNew(k);
 var st=S.qz[k], N=st.order.length;
 if(st.i>=N){
  var ok=st.res.filter(function(r){return r.ok;}).length, fails=st.res.filter(function(r){return !r.ok;});
  var msg = ok>=N-1 ? '¡Muy bien! Lo tienes claro.' : (ok>=Math.ceil(N*0.6) ? 'Bien. Mira otra vez las explicaciones de las que has fallado.' : 'Vuelve a mirar «La idea» y repite con otras frases.');
  var o='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+msg+'</p>';
  if(fails.length){ o+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fails.forEach(function(r){ var it=c.items[r.k]; o+='<li>'+strip(it.q).slice(0,90)+' → <b>'+(c.bm?(it.ok?'Mal: '+strip(it.fix):'Bien'):esc(it.o[0]))+'</b></li>'; }); o+='</ul>'; }
  o+='<div class="row"><button class="btn cta" data-act="qrep" data-k="'+k+'">Repetir con otras frases</button></div></div>';
  box.innerHTML=o; return;
 }
 var idx=st.order[st.i], it=c.items[idx], ans=st.res[st.i];
 var opts, ok;
 if(c.bm){ opts=[[0,'Bien'],[1,'Mal']]; ok=it.ok; }
 else { if(!st.perm[idx]){ st.perm[idx]=shuffle(range(it.o.length)); save(); } opts=st.perm[idx].map(function(j){ return [j,it.o[j]]; }); ok=0; }
 var o='<div class="qz"><div class="cnt">'+esc(c.name)+' · '+(st.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(st.i/N*100)+'%"></i></div>';
 o+='<div class="qq">'+it.q+'</div><div class="ops'+(c.bm?' bm':'')+'" role="group">';
 opts.forEach(function(op){
  var cls=''; if(ans){ if(op[0]===ok) cls='good'; else if(op[0]===ans.pick) cls='bad'; }
  o+='<button type="button" data-act="qa" data-k="'+k+'" data-o="'+op[0]+'" class="'+cls+'"'+(ans?' disabled':'')+'>'+esc(op[1])+'</button>';
 });
 o+='</div>';
 if(ans){
  o+='<div class="fb '+(ans.ok?'good':'bad')+'" role="status"><b>'+(ans.ok?'¡Bien!':'No.')+'</b> '+(c.bm&&it.ok?'Corrección: '+it.fix+'<br>':'')+(!c.bm&&!ans.ok?'La buena: <b>'+esc(it.o[0])+'</b>. ':'')+it.why+'</div>';
 }
 o+='<div class="row"'+(ans?'':' hidden')+'><button class="btn cta" data-act="qnext" data-k="'+k+'">'+(st.i+1<N?'Siguiente':'Ver el resultado')+'</button></div></div>';
 box.innerHTML=o;
}
function qzAnswer(k, pick){
 var c=D.qz[k], st=S.qz[k]; if(st.res[st.i]) return;
 var it=c.items[st.order[st.i]], ok = c.bm ? (pick===it.ok) : (pick===0);
 st.res[st.i]={k:st.order[st.i], pick:pick, ok:ok};
 if(st.res.length===st.order.length || st.i===st.order.length-1){
  var n=st.res.filter(function(r){return r&&r.ok;}).length;
  var fl=[]; st.res.forEach(function(r){ if(r&&!r.ok) fl.push(strip(c.items[r.k].q).slice(0,70)); });
  S.qlog[k]={last:n+'/'+st.order.length, fails:fl, best:Math.max(n,(S.qlog[k]&&S.qlog[k].bestn)||0), bestn:Math.max(n,(S.qlog[k]&&S.qlog[k].bestn)||0)};
 }
 save();
}
function qzBox(k){ return D.qz[k] ? (k.charAt(0)==='p' ? $('pqbox') : $('exbox')) : null; }

/* ---------------- motor de huecos ---------------- */
var GAPRX=/\[\[([^\]]+)\]\]/g;
function parseGaps(id, s){
 var n=0;
 var html=s.replace(GAPRX, function(m0, inner){
  n++; var p=inner.split('#'), ops=p[0].split('|'), gid=id+'-'+n, cur=S.cz[gid];
  var order=seeded(ops, gid);
  var sel='<sup>'+n+'</sup><select data-g="'+gid+'" data-ok="'+esc(ops[0])+'" data-m="'+p[1]+'" aria-label="Hueco '+n+'"'+(cur&&cur.cur===ops[0]?' disabled class="ok"':(cur?' class="no"':''))+'><option value="">…</option>';
  order.forEach(function(o){ sel+='<option'+(cur&&cur.cur===o?' selected':'')+'>'+esc(o)+'</option>'; });
  return sel+'</select>';
 });
 return {html:html, n:n};
}
function seeded(arr, seed){ var h=0; for(var i=0;i<seed.length;i++) h=(h*31+seed.charCodeAt(i))>>>0; var a=arr.slice(); for(var j=a.length-1;j>0;j--){ h=(h*1103515245+12345)>>>0; var r=h%(j+1); var t=a[j]; a[j]=a[r]; a[r]=t; } return a; }
function gapInfo(id, s){ var list=[], n=0; s.replace(GAPRX, function(m0,inner){ n++; var p=inner.split('#'); list.push({gid:id+'-'+n, n:n, ok:p[0].split('|')[0], m:p[1]}); return m0; }); return list; }
function fbList(id, s){
 var o='', tot=0, done=0, first=0;
 gapInfo(id,s).forEach(function(g){
  tot++; var c=S.cz[g.gid]; if(!c) return; done += c.cur===g.ok?1:0; if(c.first===g.ok) first++;
  var mo=D.motivos[g.m], tn=D.tiempos[mo.t];
  if(c.cur===g.ok) o+='<li class="ok">'+g.n+'. ✓ <b>'+esc(g.ok)+'</b> · <span class="tchip '+mo.t+'">'+tn+'</span> '+mo.w+'</li>';
  else o+='<li class="no">'+g.n+'. ✗ <b>'+esc(c.cur)+'</b> no va aquí. Pista: <span class="tchip '+mo.t+'">'+tn+'</span> '+mo.w+' Prueba otra vez.</li>';
 });
 return {html:o, tot:tot, done:done, first:first};
}
function renderE2(){
 var o='<div class="pills">'; D.textos.forEach(function(t){ o+='<button class="pill'+(S.etext===t.id?' on':'')+'" data-act="etext" data-id="'+t.id+'">'+esc(t.titulo)+'</button>'; }); o+='</div>';
 var t=D.textos.filter(function(x){return x.id===S.etext;})[0], g=parseGaps(t.id, t.texto), f=fbList(t.id, t.texto);
 o+='<div class="cz"><span class="chip">'+esc(t.tipo)+'</span><span class="tema">'+esc(t.titulo)+'</span>'+g.html+'</div>';
 o+='<p class="small"><b>'+f.done+' de '+f.tot+'</b> huecos bien'+(f.done===f.tot?' · a la primera: <b>'+f.first+' de '+f.tot+'</b>':'')+'</p><ul class="fbl" aria-live="polite">'+f.html+'</ul>';
 o+='<div class="row"><button class="btn sm" data-act="czreset" data-ids="'+t.id+'">Empezar este texto de nuevo</button></div>';
 $('exbox').innerHTML=o;
}
function renderE3(){
 var o='', tot=0, done=0, first=0;
 D.antes.forEach(function(t,i){
  var id='aa'+i, g=parseGaps(id, t.texto), f=fbList(id, t.texto); tot+=f.tot; done+=f.done; first+=f.first;
  o+='<div class="cz"><span class="tema">'+esc(t.tema)+'</span>'+g.html+'<ul class="fbl">'+f.html+'</ul></div>';
 });
 $('exbox').innerHTML='<div class="box small" style="margin-top:0">Cada frase tiene tres momentos: <span class="ti">antes</span> (costumbre), <b>ahora</b> (presente) y <span class="tf">el cambio</span> (cuándo pasó). Si el cambio está en la ventana de ahora (<i>esta semana, este año</i>), va en <span class="tv">perfecto</span>.</div>'+o+
  '<p class="small"><b>'+done+' de '+tot+'</b> huecos bien'+(done===tot?' · a la primera: <b>'+first+' de '+tot+'</b>':'')+'</p><div class="row"><button class="btn sm" data-act="czreset" data-ids="'+D.antes.map(function(x,i){return 'aa'+i;}).join(',')+'">Empezar de nuevo</button></div>';
}
function czChange(sel){
 var gid=sel.getAttribute('data-g'), v=sel.value; if(!v) return;
 var c=S.cz[gid]||{}; if(!c.first) c.first=v; c.cur=v; S.cz[gid]=c; save();
 renderEx(); nav();
 var ns=document.querySelector('select[data-g="'+gid+'"]'); if(ns && ns.disabled===false) ns.focus();
}

/* ---------------- selectores ---------------- */
function renderPq(){
 var ps=$('pqsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.pq);
 $('pqinfo').textContent=D.qz[S.pq].info; qzRender(S.pq, $('pqbox'));
}
var EXINFO={e2:'Textos como los del examen. Elige el verbo de cada hueco: la corrección sale enseguida, con el motivo.', e3:'Antes, ahora y el momento que lo cambia todo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else if(S.ex==='e3') renderE3(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+'</div>';
 if(L.intro) h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(t){ return '<span class="tchip '+t+'">'+D.tiempos[t]+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas de color te dicen qué tiempo pide cada pauta. Recuerda: unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu texto</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar mis pasados</button></div><div id="rvbox" aria-live="polite"></div>';
 var CH=['Cada verbo del pasado: ¿es decorado (imperfecto), acción (indefinido) o ventana de ahora (perfecto)?','Las palabras como <i>ayer, el sábado, en 2019</i> van con indefinido, nunca con perfecto.','Lo que hacías normalmente antes (<i>siempre, todos los...</i>) va en imperfecto.','Al final, una valoración de algo terminado: <i>fue, lo pasé...</i>','Cada pregunta abre con ¿ y cierra con ?, con tilde en qué, cómo, dónde...'];
 h+='<h3>Mi lista de los pasados</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
var PERF=/\b(he|has|ha|hemos|habeis|han)\s+[a-z]*(ado|ido|to|cho|sto)\b/;
function review(){
 var L=lam(), txt=$('wtext').value, out=[];
 if(txt.trim().length<20){ $('rvbox').innerHTML='<ul class="rv"><li class="a">Escribe primero tu texto.</li></ul>'; return; }
 var sents=txt.match(/[^.!?\n]+[.!?]*/g)||[];
 var rx=D.detector.map(function(d){ return {r:new RegExp(norm(d.re),'g'), t:d.t}; });
 var nfound=0;
 sents.forEach(function(s){
  var n=norm(s); if(!n.trim()) return;
  rx.forEach(function(d){
   d.r.lastIndex=0; var m;
   while((m=d.r.exec(n))){
    nfound++;
    var w=s.substr(m.index, m[0].length), hl=esc(s.slice(0,m.index))+'<mark>'+esc(w)+'</mark>'+esc(s.slice(m.index+m[0].length));
    var perf=PERF.test(n), cls='n', msg='';
    if(d.t==='indef'){ if(perf){ cls='r'; msg='<b>¡Ojo!</b> «'+esc(w)+'» es un momento cerrado y en esta frase hay un perfecto. Usa el indefinido (fui, comí, llegó).'; } else msg='«'+esc(w)+'»: momento cerrado. Si cuentas lo que pasó, indefinido. Si describes cómo era, imperfecto.'; }
    else if(d.t==='perf'){ if(perf){ cls='g'; msg='«'+esc(w)+'» con perfecto: bien.'; } else { cls='a'; msg='«'+esc(w)+'» mira por la ventana de ahora: en España suele ir con perfecto (he ido, has visto). Mira tu verbo.'; } }
    else { if(perf){ cls='a'; msg='«'+esc(w)+'» habla de antes o de un proceso, y aquí hay un perfecto. ¿No debería ser imperfecto (iba, comía)?'; } else msg='«'+esc(w)+'»: costumbre de antes, proceso o decorado: normalmente imperfecto (iba, comía, hacía).'; }
    out.push('<li class="'+cls+'">'+msg+'<br><span class="small">'+hl+'</span></li>');
   }
  });
 });
 var qo=(txt.match(/¿/g)||[]).length, qc=(txt.match(/\?/g)||[]).length;
 if(qc>qo) out.push('<li class="r"><b>Preguntas:</b> tienes '+qc+' «?» y solo '+qo+' «¿». En español la pregunta también se abre: ¿Qué tal el concierto?</li>');
 if(L.preguntas && qc<L.preguntas) out.push('<li class="r"><b>Preguntas:</b> la lámina pide '+L.preguntas+' preguntas y has escrito '+qc+'. Cada pauta, al menos una frase.</li>');
 else if(L.preguntas) out.push('<li class="g"><b>Preguntas:</b> has escrito '+qc+'. Comprueba el tiempo: ¿preguntas por algo terminado (¿Qué tal fue?) o hasta ahora (¿Has vuelto?)?</li>');
 if(!nfound) out.unshift('<li class="a">No he encontrado palabras de tiempo (ayer, el sábado, de niño, hoy...). Ponlas: ayudan al lector y te ayudan a ti a elegir el tiempo.</li>');
 var wc=txt.trim().split(/\s+/).length;
 S.wrev=S.wrev||{}; S.wrev[L.id]={found:nfound, red:out.filter(function(x){return x.indexOf('class="r"')>0;}).length, words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul><p class="muted small">La página solo busca palabras de tiempo: no ve todos los errores. Tu profesora corrige el texto completo.</p>';
}

/* ---------------- ahora tu: oral ---------------- */
var TM=null, T0=0, TDUR=30;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } }
function renderOral(){
 var o=''; D.oral.forEach(function(c,i){ o+='<button class="pill'+(S.oi===i?' on':'')+(S.or[i]?' ok':'')+'" data-act="oc" data-i="'+i+'">'+(i+1)+(S.or[i]?' ✓':'')+'</button>'; });
 o+='<button class="pill" data-act="ornd">Al azar</button>'; $('orsel').innerHTML=o;
 var c=D.oral[S.oi], r=S.or[S.oi], h='<div class="ocard"><div class="muted small">Pregunta '+(S.oi+1)+' de '+D.oral.length+'</div>';
 var q=c.q.replace('____', r?'<b class="'+(r.ok?'':'')+'" style="color:var(--ok)">'+esc(c.o[0])+'</b>':'____');
 h+='<div class="qq">'+q+'</div>';
 if(!r){
  var perm=seeded(range(c.o.length).map(String),'or'+S.oi).map(Number);
  h+='<p class="small"><b>1. Elige la forma del verbo:</b></p><div class="pills">'; perm.forEach(function(j){ h+='<button class="pill" data-act="opick" data-j="'+j+'">'+esc(c.o[j])+'</button>'; }); h+='</div>';
 } else {
  h+='<div class="fb '+(r.ok?'good':'bad')+'">'+(r.ok?'¡Bien!':'No: era <b>'+esc(c.o[0])+'</b>.')+' Ahora contesta con el mismo tiempo.</div>';
  h+='<p class="small" style="margin-top:12px"><b>2. Contesta en voz alta (30 segundos).</b></p><div class="tbar"><i id="tbar"></i></div><div class="esc" id="esc"><div>0 s · Responde con el mismo tiempo de la pregunta.</div><div>10 s · Añade un detalle: ¿dónde?, ¿con quién?, ¿cómo era?</div><div>20 s · Devuelve la pregunta: ¿Y tú...?</div></div>';
  h+='<div class="row"><button class="btn cta" data-act="tstart" id="tbtn">Empezar a hablar</button><button class="btn" data-act="model">Ver la respuesta modelo</button></div><div id="mbox"></div>';
  h+='<div class="row"><button class="btn" data-act="onext">Siguiente pregunta</button></div>';
 }
 $('orbox').innerHTML=h+'</div>';
}
function tstart(){
 stopTimer(); T0=Date.now(); var b=$('tbtn'); if(b) b.textContent='Otra vez';
 TM=setInterval(function(){
  var t=(Date.now()-T0)/1000, bar=$('tbar'), es=$('esc'); if(!bar){ stopTimer(); return; }
  bar.style.width=Math.min(100,t/TDUR*100)+'%';
  var k=t<10?0:(t<20?1:2), ds=es.children; for(var i=0;i<ds.length;i++) ds[i].classList.toggle('on', i===k);
  if(t>=TDUR){ stopTimer(); bar.style.width='100%'; }
 }, 250);
}

/* ---------------- opinion y copiar ---------------- */
function renderOpn(){
 var o=''; for(var i=1;i<=10;i++) o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>';
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked=r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function pack(){
 var L=['CURSO DELE A2 - R01: LOS PASADOS Y LAS PREGUNTAS','Nombre: '+(S.name||'-'),''];
 L.push('EJERCICIOS (ultimo resultado)');
 ['p1','p2','p3','e1','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 function cz(name, id, s){ var f=fbList(id,s), errs=[]; gapInfo(id,s).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); }); return '- '+name+': '+(Object.keys(S.cz).some(function(k){return k.indexOf(id+'-')===0;})?f.first+'/'+f.tot+' a la primera'+(errs.length?' | '+errs.join('; '):''):'sin hacer'); }
 D.textos.forEach(function(t){ L.push(cz('Elige el pasado, '+t.titulo, t.id, t.texto)); });
 var aa=[]; D.antes.forEach(function(t,i){ aa.push(cz(t.tema,'aa'+i,t.texto)); }); L.push('Antes, ahora y el cambio:'); L=L.concat(aa);
 L.push('','ORAL: PREGUNTAS EN CADENA');
 var od=Object.keys(S.or); L.push(od.length? od.map(function(i){ return (+i+1)+(S.or[i].ok?' bien':' mal ('+S.or[i].pick+')'); }).join(', ') : 'sin hacer');
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev&&S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' ('+l.palabras[0]+'-'+l.palabras[1]+' palabras)', 'Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision de pasados: '+rv.found+' palabras de tiempo, '+rv.red+' avisos rojos');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. Lo que mas cuesta: '+(S.o2||'-'),'3. Desde dentro / desde fuera: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 par:function(b){ S.par=+b.getAttribute('data-i'); S.pv='a'; save(); renderPar(); },
 pv:function(b){ S.pv=b.getAttribute('data-m'); save(); renderPar(); },
 story:function(b){ S.story=b.getAttribute('data-m'); save(); renderStory(); },
 pq:function(b){ S.pq=b.getAttribute('data-k'); save(); renderPq(); },
 ex:function(b){ S.ex=b.getAttribute('data-k'); save(); renderEx(); },
 etext:function(b){ S.etext=b.getAttribute('data-id'); save(); renderE2(); },
 qa:function(b){ var k=b.getAttribute('data-k'); qzAnswer(k, +b.getAttribute('data-o')); qzRender(k, qzBox(k)); nav(); var f=qzBox(k).querySelector('.fb'); if(f&&f.scrollIntoView) f.scrollIntoView({block:'nearest'}); },
 qnext:function(b){ var k=b.getAttribute('data-k'); S.qz[k].i++; save(); qzRender(k, qzBox(k)); },
 qrep:function(b){ var k=b.getAttribute('data-k'); qzNew(k); qzRender(k, qzBox(k)); },
 czreset:function(b){ b.getAttribute('data-ids').split(',').forEach(function(id){ Object.keys(S.cz).forEach(function(g){ if(g.indexOf(id+'-')===0) delete S.cz[g]; }); }); save(); renderEx(); nav(); },
 at:function(b){ S.at=b.getAttribute('data-k'); save(); renderAt(); },
 lam:function(b){ S.lam=b.getAttribute('data-id'); save(); renderLam(); },
 review:function(){ review(); nav(); },
 oc:function(b){ stopTimer(); S.oi=+b.getAttribute('data-i'); save(); renderOral(); },
 ornd:function(){ stopTimer(); var free=range(D.oral.length).filter(function(i){ return !S.or[i] && i!==S.oi; }); if(!free.length) free=range(D.oral.length); S.oi=free[Math.floor(Math.random()*free.length)]; save(); renderOral(); },
 opick:function(b){ var j=+b.getAttribute('data-j'); S.or[S.oi]={ok:j===0, pick:D.oral[S.oi].o[j]}; save(); renderOral(); nav(); },
 tstart:function(){ tstart(); },
 model:function(){ $('mbox').innerHTML='<div class="model"><b>Una respuesta modelo:</b><br>'+D.oral[S.oi].modelo+'</div>'; },
 onext:function(){ stopTimer(); S.oi=(S.oi+1)%D.oral.length; save(); renderOral(); },
 printres:function(){ var v=$('v-resumen'); v.classList.add('printme'); window.print(); setTimeout(function(){ v.classList.remove('printme'); },500); },
 copy:function(){
  var t=pack(), box=$('cbox');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar automáticamente. Escribe tus respuestas en un correo para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
 }
};
function renderAt(){
 var ps=$('atsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.at);
 $('atw').hidden = S.at!=='w'; $('ato').hidden = S.at!=='o'; stopTimer();
 if(S.at==='w') renderLam(); else renderOral();
}
document.addEventListener('click', function(e){
 var g=e.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.tagName==='SELECT' && t.hasAttribute('data-g')){ czChange(t); return; }
 if(t.hasAttribute && t.hasAttribute('data-wchk')){ S.wchk[t.getAttribute('data-wchk')]=t.checked; save(); return; }
 if(['o1','o2','o3','o5'].indexOf(t.name)>=0){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){
 var t=e.target;
 if(t.id==='wtext'){ S.w[S.lam]=t.value; save(); }
 if(t.id==='o4'){ S.o4=t.value; save(); }
 if(t.id==='sname'){ S.name=t.value; save(); }
});
window.addEventListener('afterprint', function(){ var v=$('v-resumen'); if(v) v.classList.remove('printme'); });

renderPar(); renderStory(); renderPq(); renderEx(); renderAt(); renderOpn(); go(S.cur);
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_R, BODY, js))
print("ok", FILE, "| huecos:", sum(ngaps.values()), "+", 2 * len(B.ANTES_AHORA),
      "| items:", len(B.P_TIEMPO) + len(B.P_COMPLETA) + len(B.P_HAZ) + len(B.E_PROCESO) + len(B.E_BIENMAL),
      "| tarjetas orales:", len(B.ORAL))
