# -*- coding: utf-8 -*-
# MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 1: KIT DE FRASES POR TIPO DE TEXTO
# Uso: python3 build_M3_kit_frases.py
#  -> DELEA2_curso_M3_kit_frases.html  (subir a biblioteca/recursos/A2/dele-curso/)
# Contenido (frases, ejemplos marcados, ejercicios y tareas de "Ahora tu"): banco_frases_M3.py.
# Mismo estilo que los talleres orales (build_M4_T1_temas.py, build_M4_T3_dialogos.py): pestanas, progreso en el
# navegador (storageKey propio), boton Copiar y preguntas de opinion al final. Sin contador de palabras: el consejo
# es contar a ojo (unas 10 palabras por linea), como en el examen.
# 12/10/2026: .row[hidden]{display:none} (el boton Siguiente del ejercicio "elige" salia antes de responder).
# 12/10/2026: las laminas con fotos llevan imagenes de verdad (fotos_M3.py); el build comprueba nombre, prompt y alt.
# 12/10/2026: regla 1 matizada para que diga lo mismo que la escala oficial (y que M3-3 y M3-5): una pauta que falta
# te deja en el limite; dos (o una que falta y otra a medias), banda 1.
import json, re
from curso_comun import CSS, EMAIL, page
import banco_frases_M3 as B
import fotos_M3 as FT

TITLE = "Kit de frases para la escritura"
FILE = "DELEA2_curso_M3_kit_frases.html"
STORAGE = "dele-a2-curso-M3-kit"

# ------------------------------------------------------------ comprobaciones del banco
TAG = re.compile(r"\{([a-z]):(.+?)\}")
PAL = re.compile(r"[\wÀ-ſ]+(?:-[\wÀ-ſ]+)*")
TU_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(tú|tu|tus|te|ti|contigo|tienes|puedes|quieres|sabes|eres|estás|vienes|perdona|dime|escríbeme|cuéntame|oye|beso|abrazo)(?![\wÀ-ſ])")
US_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(usted|ustedes|atentamente|estimad[oa]s?|cordiales|perdone|disculpe)(?![\wÀ-ſ])")

def plain(s):
    return TAG.sub(r"\2", s)
def words(s):
    return len(PAL.findall(plain(s)))
def lamina_words(l):
    return sum(words(x) for x in l.get("input", []))

def check_lamina(l, ref):
    assert l["tarea"] in (1, 2) and l["pautas"], ref
    if l["tarea"] == 2: assert l.get("op") in (1, 2), ref + ": falta la opcion"
    if l.get("input"):
        n = lamina_words(l)
        assert 30 <= n <= 50, ref + ": el texto de entrada tiene %d palabras (35-45)" % n
    return FT.check(l, ref)

TEXTS = {}
NFOTOS = 0
ids = [t["id"] for t in B.TIPOS]
assert len(ids) == len(set(ids))
for t in B.TIPOS:
    ref = "Tipo " + t["id"]
    keys = [f[0] for f in t["funciones"]]
    assert "c" not in keys and len(keys) == len(set(keys)) and len(keys) <= 8, ref + ": claves de funciones"
    NFOTOS += check_lamina(t["lamina"], ref + " (lamina)") + check_lamina(t["ahora"], ref + " (ahora tu)")
    segs = [s for par in t["ejemplo"] for s in par]
    todo = " ".join(x for _, x in segs)
    assert not re.search(r"\{(?![a-z]:)", todo), ref + ": marca mal escrita"
    usadas = set(m for m, _ in TAG.findall(todo))
    assert usadas <= set(keys) | {"c"}, ref + ": marca desconocida %s" % (usadas - set(keys) - {"c"})
    n = words(todo)
    assert t["min"] <= n <= t["max"], ref + ": el ejemplo tiene %d palabras (%d-%d)" % (n, t["min"], t["max"])
    np = len(t["lamina"]["pautas"])
    cub = set(p for p, _ in segs if p)
    assert cub == set(range(1, np + 1)), ref + ": pautas sin frase %s" % (set(range(1, np + 1)) - cub)
    txt = plain(todo)
    if t["trato"] == "tu":
        assert not US_PAL.search(txt), ref + ": hay usted en un correo de tu: " + US_PAL.search(txt).group(0)
        assert len(usadas - {"c"}) >= 6, ref + ": el ejemplo usa pocas funciones"
    elif t["trato"] == "usted":
        assert not TU_PAL.search(txt), ref + ": hay tu en un correo de usted: " + TU_PAL.search(txt).group(0)
    else:
        con = set(x.lower() for k, x in TAG.findall(todo) if k == "c" or (t["id"] == "bio" and k == "t"))
        assert len(con) >= 3, ref + ": pocos conectores o marcadores (%d)" % len(con)
    for e in t["ej"]: assert e in B.EJ, ref + ": ejercicio %s no existe" % e
    TEXTS[t["id"]] = n
for k, e in B.EJ.items():
    if e["tipo"] in ("q",):
        for q in e["items"]: assert len(q["ops"]) == 3 and 0 <= q["ok"] < 3, k
    if e["tipo"] == "h":
        gaps = [int(x) for x in re.findall(r"\[\[(\d+)\]\]", e["texto"])]
        assert gaps == list(range(len(e["huecos"]))), k + ": huecos mal numerados"
        for h in e["huecos"]: assert len(h["ops"]) == 3 and len(set(h["ops"])) == 3 and 0 <= h["ok"] < 3, k
    if e["tipo"] == "c":
        assert sum(1 for s in e["seg"] if s.get("fix")) >= 3, k + ": pocos errores para cazar"
for e in B.EJ_TRAMPAS: assert e in B.EJ
# los errores de tu/usted del ejercicio de caza son de verdad errores (y las frases correctas, correctas)
for k, trato in (("tu_c1", "usted"), ("tu_c2", "tu")):
    bad = TU_PAL if trato == "usted" else US_PAL
    for s in B.EJ[k]["seg"]:
        if s.get("fix"):
            assert bad.search(s["t"]) or (trato == "usted" and re.search(r"(?i)\b(tienes|puedes)\b", s["t"])) or (trato == "tu" and re.search(r"(?i)\b(su|puede|saludos)\b", s["t"])), k + ": no veo el error en: " + s["t"]
            assert not bad.search(s["fix"]), k + ": la correccion sigue mal: " + s["fix"]
        else:
            assert not bad.search(s["t"]), k + ": frase marcada como correcta con error: " + s["t"]
ANTES_Y = len(re.findall(r"(?i)\b(y|porque)\b", B.ANTES))
DESP_C = len(set(x.lower() for k, x in TAG.findall(B.DESPUES) if k == "c"))

# ------------------------------------------------------------ CSS
CSS_M3 = CSS + r"""
:root{--blu:#2B5FA8;--blu-soft:#E4ECF8}
section.view > h3{margin-top:30px}
.row[hidden]{display:none}
.where{display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.04em;background:var(--ink);color:#fff;border-radius:999px;padding:2px 12px;margin-bottom:8px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px}
.box h4{margin:0 0 4px}.box ul{margin:6px 0 0;padding-left:1.1em}.box p{margin:4px 0}
.keys{counter-reset:k;list-style:none;padding:0}
.keys li{counter-increment:k;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 14px 10px 52px;margin:8px 0;position:relative}
.keys li:before{content:counter(k);position:absolute;left:14px;top:8px;font-family:Georgia,serif;font-size:1.5rem;font-weight:700;color:var(--coral)}
/* colores de las funciones */
.f{border-radius:3px;padding:0 2px;font-weight:600}
.f0{background:#E4ECF8;color:#1E4A87}.f1{background:#E3F1E8;color:#22603C}.f2{background:#FBF0DA;color:#7A4E0E}.f3{background:#FFE2D6;color:#9C3A1E}
.f4{background:#ECE6F7;color:#4B3486}.f5{background:#DDF1F0;color:#1D5E5A}.f6{background:#F8E1EC;color:#8A2357}.f7{background:#EEF0D9;color:#545B16}
.cx{text-decoration:underline;text-decoration-thickness:2.5px;text-decoration-color:var(--coral);text-underline-offset:3px;font-weight:600}
.ch{display:inline-block;font-size:.76rem;font-weight:700;letter-spacing:.03em;border-radius:999px;padding:1px 9px;margin:0 3px 3px 0;white-space:nowrap}
.ch.cxl{background:#fff;border:1px solid var(--line)}
.legend{display:flex;flex-wrap:wrap;gap:4px 6px;font-size:.88rem;margin:6px 0 10px;align-items:center}
.fgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.fcard{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 16px 12px;border-top:6px solid var(--line)}
.fcard h4{margin:0}.fcard .qq{color:var(--muted);font-size:.88rem;margin:0 0 6px}
.fcard ul{margin:0;padding-left:1.1em}.fcard li{font-style:italic;font-size:.95rem}
.b0{border-top-color:#2B5FA8}.b1{border-top-color:#2F7D4F}.b2{border-top-color:#B7791F}.b3{border-top-color:#E8603C}
.b4{border-top-color:#6E4FB8}.b5{border-top-color:#2A8C86}.b6{border-top-color:#B8407A}.b7{border-top-color:#7C8424}
/* lamina */
.lam{background:#fff;border:2px solid var(--ink);border-radius:6px;padding:14px 18px;margin:12px 0;font-size:.97rem}
.lam .lh{font-size:.78rem;letter-spacing:.06em;color:var(--muted);text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:6px;margin-bottom:8px;display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
.lam p{margin:4px 0 8px}
.lam ul.pa{margin:0;padding-left:0;list-style:none}
.lam ul.pa li{padding:4px 0 4px 30px;position:relative}
.lam ul.pa li .bn{position:absolute;left:0;top:6px;width:22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:.78rem;font-weight:700;display:grid;place-items:center}
.lam .pw{font-size:.88rem;color:var(--muted);margin-top:8px;font-style:italic}
.msg{background:#F6F3EF;border-radius:8px;padding:10px 14px;margin:8px 0;font-size:.95rem}
.msg p{margin:0 0 4px}
.ad{border:2px dashed var(--ink);border-radius:8px;padding:10px 14px;margin:8px 0;text-align:center;font-size:.95rem}
.ad p{margin:2px 0}.ad p:first-child{font-weight:800;letter-spacing:.05em;font-family:Georgia,serif}
ul.ficha{background:#F6F3EF;border-radius:8px;padding:8px 14px 8px 30px;margin:8px 0;font-size:.93rem}
/* ejemplo */
.letter{background:#fff;border:1px solid var(--line);border-left:5px solid var(--coral);border-radius:0 10px 10px 0;padding:14px 18px;font-size:1.02rem;line-height:1.85}
.letter p{margin:0 0 8px}
.pb{display:inline-grid;place-items:center;min-width:19px;height:19px;border-radius:50%;background:var(--ink);color:#fff;font-size:.68rem;font-weight:700;vertical-align:2px;margin-right:3px}
.letter.clean .f{background:none;color:inherit;font-weight:inherit;padding:0}
.letter.clean .cx{text-decoration:none;font-weight:inherit}
.letter.clean .pb{display:none}
.wc{font-size:.88rem;color:var(--muted);margin:6px 0}
.tg{font-size:.88rem;display:flex;gap:8px;align-items:center;cursor:pointer;margin:8px 0}
.tg input{width:18px;height:18px;accent-color:var(--coral)}
.why{list-style:none;padding:0;margin:8px 0}
.why li{padding:6px 0 6px 28px;position:relative;border-bottom:1px dashed var(--line)}
.why li:before{content:"\2713";position:absolute;left:4px;top:5px;color:var(--ok);font-weight:700}
.trap{background:var(--amb-soft);border-left:5px solid var(--amb);border-radius:0 10px 10px 0;padding:10px 14px;margin:14px 0;font-size:.96rem}
/* ejercicios */
.ex{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin:14px 0}
.ex h4{margin:0 0 2px}.ex .ei{font-size:.92rem;color:var(--muted);margin:0 0 10px}
.ex .qn{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.ex .qs{font-size:.95rem;margin:4px 0 2px}
.ex .qp{font-weight:600;margin:4px 0}
.qop{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:10px;padding:9px 14px;margin:6px 0;cursor:pointer;color:inherit}
.qop:hover:not(:disabled){border-color:var(--coral)}
.qop:disabled{cursor:default}
.qop.ok,.seg.ok{border-color:var(--ok);background:var(--ok-soft)}
.qop.bad,.seg.bad{border-color:var(--bad);background:var(--bad-soft)}
.fb{border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
.fb.ok{background:var(--ok-soft)}.fb.bad{background:var(--bad-soft)}
.score{font-family:Georgia,serif;font-size:2.2rem;font-weight:700}
.htxt{line-height:2.2;font-size:1rem;background:#FBF9F6;border-radius:10px;padding:10px 14px}
.htxt p{margin:0 0 6px}
.htxt select{font:inherit;font-size:.95rem;border:2px solid #CFC6BB;border-radius:8px;padding:2px 6px;background:#fff;max-width:100%}
.htxt select.ok{border-color:var(--ok);background:var(--ok-soft)}.htxt select.bad{border-color:var(--bad);background:var(--bad-soft)}
.hfb{font-size:.92rem;margin:8px 0 0;padding-left:1.2em}
.hfb li{margin:4px 0}.hfb li.ok{color:var(--ok)}
.segs{background:#FBF9F6;border-radius:10px;padding:10px 12px}
.seg{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:8px;padding:6px 12px;margin:5px 0;cursor:pointer;color:inherit}
.seg:hover:not(:disabled){border-color:var(--coral)}
.seg.mk{border-color:var(--coral);background:var(--coral-soft)}
.seg.miss{border-color:var(--amb);background:var(--amb-soft)}
.seg:disabled{cursor:default}
.seg .fix{display:block;font-size:.88rem;font-weight:600;color:var(--ok);margin-top:2px}
.seg .fix.w{color:var(--bad)}
/* ahora tu */
.ahora{background:#FFF8F2;border:2px solid var(--coral);border-radius:14px;padding:16px 18px;margin:14px 0}
.ahora h3{margin:0 0 6px}
.ahora textarea{width:100%;font:inherit;font-size:1rem;line-height:1.7;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;min-height:220px;background:#fff;resize:vertical}
.chk{list-style:none;padding:0;margin:8px 0}
.chk li label{display:flex;gap:10px;align-items:flex-start;padding:6px 0;border-bottom:1px dashed var(--line);cursor:pointer}
.chk input{width:20px;height:20px;accent-color:var(--ok);flex:0 0 auto;margin-top:3px}
.chk li label:has(input:checked) > span{color:var(--muted);text-decoration:line-through}
.saved{font-size:.82rem;color:var(--ok);min-height:1.2em}
/* tareas */
.r45{display:flex;border-radius:10px;overflow:hidden;margin:14px 0 4px;border:2px solid var(--ink)}
.r45 div{padding:8px 6px;text-align:center;font-size:.82rem;line-height:1.25;border-right:2px solid var(--ink);background:#fff}
.r45 div:last-child{border-right:0}
.r45 div b{display:block;font-family:Georgia,serif;font-size:1.05rem}
.r45 div.me{background:var(--coral);color:#fff}
.r45cap{display:flex;justify-content:space-between;font-size:.8rem;color:var(--muted)}
.hand{font-family:"Bradley Hand","Segoe Print","Comic Sans MS",cursive;font-size:1.15rem;border-bottom:1.5px solid #9DB3D3;padding:2px 4px;margin:6px 0;background:#fff}
.hand .w{border-radius:3px;padding:0 1px}
.hand .w:nth-child(odd){background:var(--coral-soft)}
.lines{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0}
.lines div{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:10px 14px;text-align:center}
.lines b{display:block;font-family:Georgia,serif;font-size:1.8rem;line-height:1.1;color:var(--coral)}
table.t td .btn{white-space:nowrap}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}
.vs div{border-radius:12px;padding:12px 16px;font-size:.95rem;line-height:1.7}
.vs .no{background:var(--bad-soft)}.vs .si{background:var(--ok-soft)}
.vs b.h{display:block;margin-bottom:4px}
.yp{background:#F6C9BE;border-radius:3px;padding:0 2px;font-weight:700}
.ctab td:nth-child(2){font-style:italic}
/* opinion */
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
.sum{font-size:.92rem;margin:6px 0;padding-left:1.1em}
@media (max-width:760px){.two,.fgrid,.vs,.lines{grid-template-columns:1fr}.r45 div{font-size:.7rem;padding:6px 2px}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff}section.view{display:none!important}
 section.view.printme{display:block!important;padding-top:0}.fcard,.lam,.box,.letter{break-inside:avoid}}
""" + FT.CSS

# ------------------------------------------------------------ HTML de apoyo
def lamina_html(l):
    h = "Tarea %d" % l["tarea"] + (" · Opción %d" % l["op"] if l.get("op") else "")
    mn, mx = (60, 70) if l["tarea"] == 1 else (70, 80)
    o = ['<div class="lam"><div class="lh"><span>%s</span><span>%d-%d palabras</span></div>' % (h, mn, mx)]
    if l.get("instr"): o.append("<p>%s</p>" % l["instr"])
    if l.get("input"): o.append('<div class="msg">' + "".join("<p>%s</p>" % x for x in l["input"]) + "</div>")
    if l.get("anuncio"): o.append('<div class="ad">' + "".join("<p>%s</p>" % x for x in l["anuncio"]) + "</div>")
    if l.get("intro"): o.append("<p>%s</p>" % l["intro"])
    if l.get("photos"): o.append(FT.fotos_html(l))
    if l.get("ficha"): o.append('<ul class="ficha">' + "".join("<li>%s</li>" % x for x in l["ficha"]) + "</ul>")
    if l.get("intro2"): o.append("<p>%s</p>" % l["intro2"])
    if l.get("lead"): o.append("<p>%s</p>" % l["lead"])
    o.append('<ul class="pa">' + "".join('<li><span class="bn">%d</span>%s</li>' % (i + 1, p) for i, p in enumerate(l["pautas"])) + "</ul>")
    o.append('<div class="pw">Número de palabras recomendadas: entre %d y %d.</div></div>' % (mn, mx))
    return "".join(o)

def marked(s, idx, names):
    def rep(m):
        k, x = m.group(1), m.group(2)
        if k == "c": return '<span class="cx">%s</span>' % x
        return '<span class="f f%d" title="%s">%s</span>' % (idx[k], names[k], x)
    return TAG.sub(rep, s)

def ejemplo_html(t):
    idx = {f[0]: i for i, f in enumerate(t["funciones"])}
    names = {f[0]: f[1] for f in t["funciones"]}
    o = []
    for par in t["ejemplo"]:
        o.append("<p>" + " ".join(('<span class="pb" title="Pauta %d">%d</span>' % (p, p) if p else "") + marked(x, idx, names) for p, x in par) + "</p>")
    return "".join(o)

def legend_html(t):
    segs = " ".join(x for par in t["ejemplo"] for _, x in par)
    usadas = set(m for m, _ in TAG.findall(segs))
    o = ['<div class="legend">']
    for i, f in enumerate(t["funciones"]):
        if f[0] in usadas: o.append('<span class="ch f%d">%s</span>' % (i, f[1]))
    if "c" in usadas: o.append('<span class="ch cxl"><span class="cx">conector</span></span>')
    o.append('<span class="ch cxl"><span class="pb">1</span> pauta</span></div>')
    return "".join(o)

def fcards(t):
    return '<div class="fgrid">' + "".join(
        '<div class="fcard b%d"><h4>%s</h4><p class="qq">%s</p><ul>%s</ul></div>' % (i, f[1], f[2], "".join("<li>%s</li>" % x for x in f[3]))
        for i, f in enumerate(t["funciones"])) + "</div>"

def checks_for(t):
    c = list(B.CHECK_COMUN)
    c += B.CHECK_CORREO if t["trato"] else B.CHECK_TEXTO
    return c

def tipo_view(t, nxt):
    n = TEXTS[t["id"]]
    exs = "".join('<div class="ex" id="ex-%s"></div>' % e for e in t["ej"])
    chk = "".join('<li><label><input type="checkbox" data-wc="%s|%d"><span>%s</span></label></li>' % (t["id"], i, x) for i, x in enumerate(checks_for(t)))
    return ("""
<span class="where">%s</span>
<h2>%s</h2>
<p class="lead">%s</p>
<h3>Las frases</h3>
%s
<h3>Un ejemplo</h3>
<p>Esta es la tarea:</p>
%s
<p>Y este es un texto que aprueba. Cada número es una pauta; en color, las frases del kit; subrayados, los conectores.</p>
%s
<div class="letter" id="let-%s">%s</div>
<p class="wc">%d palabras: unas %d líneas escritas a mano.</p>
<label class="tg noprint"><input type="checkbox" data-clean="let-%s"> Ver el texto sin marcas</label>
<h4>Por qué aprueba</h4>
<ul class="why">%s</ul>
<div class="trap">%s</div>
<div class="noprint">
<h3>Practica</h3>
%s
<div class="ahora">
<h3>Ahora tú</h3>
<p class="small">Escribe con las frases de esta página. En el examen escribes a mano: si puedes, escribe primero en papel y cuenta las líneas (unas 10 palabras por línea). Después cópialo aquí para enviarlo a tu profesora.</p>
%s
<textarea data-w="%s" aria-label="Tu texto" placeholder="Escribe aquí tu texto..."></textarea>
<div class="saved" data-sv="%s" role="status"></div>
<h4 style="margin-top:10px">Antes de enviarlo, revisa</h4>
<ul class="chk">%s</ul>
<p class="small muted">Tu texto se guarda en este navegador. Para enviarlo, ve a <b>Tu opinión</b> y pulsa <b>Copiar</b>: se copia con todo lo demás.</p>
</div>
</div>
<div class="row"><button class="btn" data-act="print" data-p="%s">Imprimir las frases y el ejemplo</button><button class="btn cta" data-go="%s">Siguiente: %s</button></div>
""" % (t["donde"], t["titulo"], t["intro"], fcards(t), lamina_html(t["lamina"]), legend_html(t), t["id"], ejemplo_html(t),
       n, round(n / 10), t["id"], "".join("<li>%s</li>" % x for x in t["porque"]), t["trampa"], exs,
       lamina_html(t["ahora"]), t["id"], t["id"], chk, t["id"], nxt[0], nxt[1].lower()))

# ------------------------------------------------------------ VISTAS
STEPS = [("tareas", "Las dos tareas"), ("inf", "Correo a un amigo"), ("for", "Correo de usted"), ("trampas", "Dos trampas"),
         ("blog", "Blog o diario"), ("bio", "Biografía"), ("fotos", "Con fotos"), ("opinion", "Tu opinión")]
LABEL = dict(STEPS)
def nxt(k):
    i = [s[0] for s in STEPS].index(k)
    return STEPS[i + 1]

r45 = "".join('<div class="%s" style="flex:%d"><b>%d min</b>%s</div>' % ("me" if t == "Revisar" else "", m, m, t) for m, t, _ in B.REPARTO)
assert sum(m for m, _, _ in B.REPARTO) == 45
r45l = "".join("<li><b>%s (%d min):</b> %s</li>" % (t, m, d) for m, t, d in B.REPARTO)
mapa = "".join('<tr><td>%s</td><td>%s</td><td>%s</td><td><button class="btn sm" data-go="%s">Ver</button></td></tr>' % (a, b, c, d) for a, b, c, d in B.MAPA)
LINEA = "El sábado pasado fui con mis amigos a la playa."
assert len(LINEA.split()) == 10
hand = '<div class="hand">' + " ".join('<span class="w">%s</span>' % w for w in LINEA.split()) + "</div>"

V_TAREAS = """
<span class="where">Escritura · 45 minutos</span>
<h2>La prueba de Escritura: dos textos en 45 minutos</h2>
<p class="lead">En la prueba de Escritura escribes dos textos cortos. No tienes que escribir difícil: tienes que <b>hacer todo lo que piden las pautas</b>, con frases sencillas y correctas. Este kit te da las frases para cada tipo de texto.</p>
<div class="two">
 <div class="box"><h4>Tarea 1 · 60-70 palabras</h4><p>Lees un correo corto (de un amigo, casi siempre) y contestas. Tienes 4-5 pautas: saludar, contar algo, aceptar o rechazar, proponer, despedirse...</p></div>
 <div class="box"><h4>Tarea 2 · 70-80 palabras</h4><p>Eliges <b>una</b> de dos opciones. Opción 1: un texto sobre tu vida (un blog, un diario, una revista). Opción 2: un texto a partir de fotos o datos (una biografía, la historia de un día).</p></div>
</div>
<h3>Los tipos de texto de este kit</h3>
<table class="t"><thead><tr><th>Tipo de texto</th><th>Dónde sale</th><th>Palabras</th><th></th></tr></thead><tbody>""" + mapa + """</tbody></table>

<h3>Cómo repartir los 45 minutos</h3>
<div class="r45" aria-hidden="true">""" + r45 + """</div>
<div class="r45cap"><span>0:00</span><span>45:00</span></div>
<ul>""" + r45l + """</ul>
<div class="tip">Es una recomendación, no una regla del examen. Lo importante: <b>guarda 5 minutos al final para revisar</b>. Muchos candidatos pierden puntos por fallos que ven en un minuto.</div>

<h3>Cómo contar las palabras sin contador</h3>
<p>En el examen escribes a mano y no hay contador. No pierdas tiempo contando palabra por palabra: <b>cuenta las líneas</b>. Una línea escrita a mano tiene <b>unas 10 palabras</b>, como esta:</p>
""" + hand + """
<div class="lines">
 <div><b>6-7 líneas</b>Tarea 1 (60-70 palabras)</div>
 <div><b>7-8 líneas</b>Tarea 2 (70-80 palabras)</div>
</div>
<div class="tip"><b>Haz la prueba en casa:</b> escribe a mano unas líneas y cuenta las palabras de una. Si tu letra es grande y te caben 7 u 8 palabras, escribe una línea más; si es pequeña y te caben 12, una línea menos. Unas palabras de más o de menos no son un problema; muy corto o muy largo, sí.</div>

<h3>Tres reglas para aprobar</h3>
<ol class="keys">
 <li><b>Cada pauta, al menos una frase.</b> Un texto sencillo que cumple todas las pautas aprueba. Si a un texto difícil le falta una pauta, se queda en el límite; si le falta otra (o una está a medias), ya no es un A2.</li>
 <li><b>Tú o usted, del saludo a la despedida.</b> Si empiezas de tú, todo de tú; si empiezas de usted, todo de usted (también la despedida).</li>
 <li><b>No solo «y» y «porque».</b> Ordena y une tus frases con otros conectores: primero, después, además, por eso, así que, al final...</li>
</ol>
<div class="tip"><b>Cómo usar este kit:</b> en cada tipo de texto, lee las frases, mira el ejemplo (con las frases en color y las pautas numeradas), haz los ejercicios y escribe tu texto en «Ahora tú». Las dos trampas más típicas (tú y usted, y los conectores) tienen su propia pestaña.</div>
<div class="row"><button class="btn cta" data-go="inf">Empezar: el correo a un amigo</button></div>
"""

tu_rows = "".join("<tr><td><i>%s</i></td><td><i>%s</i></td></tr>" % x for x in B.TU_USTED)
con_rows = "".join("<tr><td><b>%s</b></td><td>%s</td><td class=\"small\">%s</td></tr>" % (a, ", ".join(b), c) for a, b, c in B.CONECTORES)
antes_html = re.sub(r"(?i)\b(y|porque)\b", r'<span class="yp">\1</span>', B.ANTES)
despues_html = TAG.sub(lambda m: '<span class="cx">%s</span>' % m.group(2), B.DESPUES)
V_TRAMPAS = """
<span class="where">Las dos trampas más típicas</span>
<h2>Dos trampas: tú y usted, y los conectores</h2>
<p class="lead">Son dos de los fallos que más bajan la nota en la Escritura del A2. Los dos tienen arreglo fácil si los conoces.</p>

<h3>Trampa 1: mezclar tú y usted</h3>
<p>Pasa así: el candidato empieza bien («Estimada señora Gómez:») y, a mitad del correo, se le escapa un «¿Puedes...?» o termina con «Un beso». O al revés: escribe a un amigo y termina con «Atentamente». Para el corrector, el texto no es adecuado.</p>
<div class="two">
 <div class="box"><h4>Antes de escribir, decide</h4><p>¿Quién me escribe o a quién escribo? Un amigo, un familiar, un compañero → <b>tú</b>. Una escuela, un hotel, una tienda, una persona que no conozco → <b>usted</b>.</p></div>
 <div class="box"><h4>Un truco</h4><p>Escribe <b>TÚ</b> o <b>USTED</b> arriba, en tu hoja de notas. Al revisar, lee solo los verbos, «te / le», «tu / su» y la despedida.</p></div>
</div>
<table class="t"><thead><tr><th>Con un amigo (tú)</th><th>De usted</th></tr></thead><tbody>""" + tu_rows + """</tbody></table>
<div class="noprint"><div class="ex" id="ex-tu_c1"></div><div class="ex" id="ex-tu_c2"></div></div>

<h3>Trampa 2: solo «y» y «porque»</h3>
<p>«Y» y «porque» están bien, pero si son los únicos conectores, el texto parece una lista y la nota de <i>uso de la lengua</i> baja. Mira la diferencia:</p>
<div class="vs">
 <div class="no"><b class="h">Solo «y» y «porque» (""" + str(ANTES_Y) + """ veces)</b>""" + antes_html + """</div>
 <div class="si"><b class="h">Con """ + str(DESP_C) + """ conectores distintos</b>""" + despues_html + """</div>
</div>
<p>Las mismas ideas, casi las mismas palabras, pero el segundo texto se lee mejor: está ordenado y explica qué pasa por qué.</p>
<table class="t ctab"><thead><tr><th>Para...</th><th>Conectores</th><th>Ejemplo</th></tr></thead><tbody>""" + con_rows + """</tbody></table>
<div class="tip"><b>Objetivo:</b> en la tarea 2 (70-80 palabras), usa <b>3 o 4 conectores distintos</b> además de «y». No hace falta más: no es un examen de conectores.</div>
<div class="noprint"><div class="ex" id="ex-con_h"></div></div>
<div class="row"><button class="btn" data-act="print" data-p="trampas">Imprimir las tablas</button><button class="btn cta" data-go="blog">Siguiente: blog o diario</button></div>
"""

DIFICIL = [LABEL[t["id"]] for t in B.TIPOS]
V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo. Al copiar, también se copian tus textos de «Ahora tú» para que tu profesora los corrija.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué tipo de texto te parece más difícil?</label>
 <div class="chips" role="group" aria-labelledby="o1l">__CHIPS1__</div>
 <label class="q" id="o2l">2. ¿Te han ayudado los ejemplos con las frases en color y las pautas numeradas?</label>
 <div class="chips" role="group" aria-labelledby="o2l">__CHIPS2__</div>
 <label class="q" id="o3l">3. ¿Cuál de las dos trampas te pasa más a ti?</label>
 <div class="chips" role="group" aria-labelledby="o3l">__CHIPS3__</div>
 <label class="q" for="o4">4. ¿Qué frase nueva vas a usar en tu próximo texto? ¿Falta algo en el kit o hay algo que no has entendido?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. Ahora, ¿cuánto control sientes en la prueba de Escritura? (1 = nada, 10 = total)</label>
 <div class="scale" role="group" aria-labelledby="o5l" id="o5"></div>
</div>
<div class="sendbox">
 <h3>Envía tu opinión y tus textos a tu profesora</h3>
 <ul class="sum" id="sum"></ul>
 <label><b>Tu nombre</b><br><input type="text" id="sname" autocomplete="name"></label>
 <div class="row"><button class="btn cta" data-act="copy">Copiar</button></div>
 <div class="copied-box" id="cbox" role="status" hidden></div>
 <p class="muted small">Pégalo en un correo para tu profesora: __EMAIL__.</p>
</div>
"""
def chips(name, vals):
    return "".join('<label><input type="radio" name="%s" value="%s">%s</label>' % (name, v, v) for v in vals)
V_OPINION = (V_OPINION.replace("__CHIPS1__", chips("o1", DIFICIL))
             .replace("__CHIPS2__", chips("o2", ["Sí, mucho", "Un poco", "No"]))
             .replace("__CHIPS3__", chips("o3", ["Mezclar tú y usted", "Usar solo «y» y «porque»", "Las dos", "Ninguna"]))
             .replace("__EMAIL__", EMAIL))

views = {"tareas": V_TAREAS, "trampas": V_TRAMPAS, "opinion": V_OPINION}
for t in B.TIPOS: views[t["id"]] = tipo_view(t, nxt(t["id"]))

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Escritura · Taller de escritura</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
"""
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
body = BODY.replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

EJ_JS = {}
for k, e in B.EJ.items():
    d = {"tipo": e["tipo"], "t": e["titulo"], "i": e["intro"]}
    if e["tipo"] == "q": d["items"] = e["items"]
    if e["tipo"] == "h": d["txt"] = e["texto"]; d["h"] = e["huecos"]
    if e["tipo"] == "c": d["seg"] = [{"t": s["t"], "fix": s.get("fix", "")} for s in e["seg"]]
    EJ_JS[k] = d
TABS_EX = {t["id"]: t["ej"] for t in B.TIPOS}
TABS_EX["trampas"] = B.EJ_TRAMPAS
DATA = {"key": STORAGE, "steps": [{"id": k, "label": l} for k, l in STEPS], "ej": EJ_JS, "tabex": TABS_EX,
        "tipos": [{"id": t["id"], "n": LABEL[t["id"]], "tarea": t["ahora"]["tarea"],
                   "task": (t["ahora"].get("instr") or t["ahora"].get("intro")), "nchk": len(checks_for(t))} for t in B.TIPOS]}

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function blank(){ return {cur:'tareas', seen:{}, ex:{}, w:{}, wc:{}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function shuffle(a){ for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function rec(id, ok, n){ var r=S.ex[id]; if(!r || ok>r.b) S.ex[id]={b:ok, n:n, l:ok}; else r.l=ok; save(); nav(); }

/* ---------------- navegacion ---------------- */
function tabDone(id){
 if(id==='tareas') return !!S.seen.tareas;
 if(id==='opinion') return !!(S.o1||S.o2||S.o3||S.o4||S.o5);
 var ex=D.tabex[id]||[], all=ex.length>0;
 ex.forEach(function(e){ if(!S.ex[e]) all=false; });
 if(id==='trampas') return all;
 return all && !!(S.w[id] && S.w[id].trim());
}
function nav(){
 var o='';
 D.steps.forEach(function(st,i){
  var done=tabDone(st.id), on=S.cur===st.id;
  o+='<button type="button" class="'+(on?'on ':'')+(done&&!on?'done':'')+'" data-go="'+st.id+'"'+(on?' aria-current="step"':'')+'><span class="n">'+(done&&!on?'✓':(i+1))+'</span>'+st.label+'</button>';
 });
 $('steps').innerHTML=o;
}
function go(id){
 S.seen[S.cur]=true; S.cur=id; save();
 var vs=document.querySelectorAll('section.view');
 for(var i=0;i<vs.length;i++) vs[i].classList.toggle('on', vs[i].id==='v-'+id);
 if(id==='opinion') summary();
 nav(); window.scrollTo(0,0);
}

/* ---------------- ejercicio q: elige ---------------- */
var Q={};
function qNew(id){ var e=D.ej[id]; Q[id]={k:0, ok:0, ans:false, ord:e.items.map(function(){ return shuffle([0,1,2]); })}; qRender(id); }
function qRender(id){
 var e=D.ej[id], q=Q[id], box=$('ex-'+id), n=e.items.length;
 var head='<h4>'+esc(e.t)+'</h4><p class="ei">'+esc(e.i)+'</p>';
 if(q.k>=n){
  rec(id, q.ok, n);
  box.innerHTML=head+'<div class="qn">RESULTADO</div><div class="score">'+q.ok+' / '+n+'</div><p>'+(q.ok===n?'¡Perfecto!':(q.ok>=n-2?'¡Muy bien! Mira otra vez las que has fallado.':'Vuelve a mirar las frases de arriba y prueba otra vez.'))+'</p>'+
   '<p class="small muted">Tu mejor resultado: '+S.ex[id].b+' / '+n+'</p><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="qnew" data-ex="'+id+'">Otra vez</button></div>';
  return;
 }
 var it=e.items[q.k], o=head+'<div class="qn">'+(q.k+1)+' DE '+n+'</div><p class="qs">'+esc(it.ctx)+'</p>'+(it.p?'<p class="qp">'+esc(it.p)+'</p>':'')+'<div role="group" aria-label="Opciones">';
 q.ord[q.k].forEach(function(i){ o+='<button type="button" class="qop" data-act="qpick" data-ex="'+id+'" data-i="'+i+'">'+esc(it.ops[i])+'</button>'; });
 o+='</div><div class="qfb"></div><div class="row qnx" style="margin-bottom:0" hidden><button class="btn cta" data-act="qnext" data-ex="'+id+'">'+(q.k===n-1?'Ver el resultado':'Siguiente')+'</button></div>';
 box.innerHTML=o;
}
function qPick(b){
 var id=b.getAttribute('data-ex'), q=Q[id], it=D.ej[id].items[q.k], box=$('ex-'+id); if(q.ans) return;
 var i=+b.getAttribute('data-i'), ok=i===it.ok; if(ok) q.ok++; q.ans=true;
 [].forEach.call(box.querySelectorAll('.qop'), function(x){ x.disabled=true; var j=+x.getAttribute('data-i'); if(j===it.ok) x.classList.add('ok'); else if(j===i) x.classList.add('bad'); });
 box.querySelector('.qfb').innerHTML='<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Correcto!':'Mejor la otra.')+'</b> '+esc(it.por)+'</div>';
 box.querySelector('.qnx').hidden=false;
}

/* ---------------- ejercicio h: huecos ---------------- */
var H={};
function hNew(id){ var e=D.ej[id]; H[id]={ord:e.h.map(function(){ return shuffle([0,1,2]); }), done:false}; hRender(id); }
function hRender(id){
 var e=D.ej[id], h=H[id];
 var txt=e.txt.split('\n').map(function(line){
  return '<p>'+esc(line).replace(/\[\[(\d+)\]\]/g, function(m,n){ n=+n;
   return '<select data-h="'+id+'" data-n="'+n+'" aria-label="Hueco '+(n+1)+'"><option value="">— elige —</option>'+h.ord[n].map(function(i){ return '<option value="'+i+'">'+esc(e.h[n].ops[i])+'</option>'; }).join('')+'</select>'; })+'</p>';
 }).join('');
 $('ex-'+id).innerHTML='<h4>'+esc(e.t)+'</h4><p class="ei">'+esc(e.i)+'</p><div class="htxt">'+txt+'</div><div class="hres"></div><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="hcheck" data-ex="'+id+'">Comprobar</button><button class="btn" data-act="hnew" data-ex="'+id+'">Empezar otra vez</button></div>';
}
function hCheck(id){
 var e=D.ej[id], box=$('ex-'+id), sel=box.querySelectorAll('select'), ok=0, fb='';
 [].forEach.call(sel, function(s){ var n=+s.getAttribute('data-n'), g=e.h[n], v=s.value===''?-1:+s.value, good=v===g.ok;
  s.classList.remove('ok','bad'); s.classList.add(good?'ok':'bad'); if(good) ok++;
  fb+='<li class="'+(good?'ok':'')+'"><b>'+(n+1)+'. '+esc(g.ops[g.ok])+'</b>'+(good?' ✓':'')+' — '+esc(g.por)+'</li>'; });
 box.querySelector('.hres').innerHTML='<div class="fb '+(ok===sel.length?'ok':'bad')+'"><b>'+ok+' de '+sel.length+' bien.</b> '+(ok===sel.length?'¡Perfecto!':'Mira las explicaciones:')+'</div><ol class="hfb" style="list-style:none;padding-left:0">'+fb+'</ol>';
 rec(id, ok, sel.length);
}

/* ---------------- ejercicio c: caza los errores ---------------- */
function cRender(id){
 var e=D.ej[id], o='<h4>'+esc(e.t)+'</h4><p class="ei">'+esc(e.i)+'</p><div class="segs" role="group" aria-label="Frases del correo">';
 e.seg.forEach(function(s,i){ o+='<button type="button" class="seg" data-act="cmark" data-ex="'+id+'" data-i="'+i+'" aria-pressed="false">'+esc(s.t)+'</button>'; });
 o+='</div><div class="cres"></div><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="ccheck" data-ex="'+id+'">Comprobar</button><button class="btn" data-act="cnew" data-ex="'+id+'">Empezar otra vez</button></div>';
 $('ex-'+id).innerHTML=o;
}
function cMark(b){ if(b.disabled) return; var on=!b.classList.contains('mk'); b.classList.toggle('mk', on); b.setAttribute('aria-pressed', on?'true':'false'); }
function cCheck(id){
 var e=D.ej[id], box=$('ex-'+id), found=0, tot=0, fp=0;
 [].forEach.call(box.querySelectorAll('.seg'), function(b){
  var s=e.seg[+b.getAttribute('data-i')], mk=b.classList.contains('mk'); b.disabled=true; b.classList.remove('mk');
  if(s.fix){ tot++; if(mk){ found++; b.classList.add('ok'); } else b.classList.add('miss'); b.innerHTML+='<span class="fix">→ '+esc(s.fix)+'</span>'; }
  else if(mk){ fp++; b.classList.add('bad'); b.innerHTML+='<span class="fix w">Esta frase está bien.</span>'; }
 });
 var all=found===tot && fp===0;
 box.querySelector('.cres').innerHTML='<div class="fb '+(all?'ok':'bad')+'"><b>Has encontrado '+found+' de '+tot+' errores.</b> '+(fp?'Has marcado '+fp+' frase'+(fp>1?'s':'')+' sin error. ':'')+(all?'¡Perfecto!':'En amarillo, los errores que se te han escapado; en verde, la frase correcta.')+'</div>';
 rec(id, Math.max(0, found-fp), tot);
}

function initEx(){ Object.keys(D.ej).forEach(function(id){ if(!$('ex-'+id)) return; var t=D.ej[id].tipo; if(t==='q') qNew(id); else if(t==='h') hNew(id); else cRender(id); }); }

/* ---------------- ahora tu ---------------- */
function initWriting(){
 [].forEach.call(document.querySelectorAll('textarea[data-w]'), function(t){ t.value=S.w[t.getAttribute('data-w')]||''; });
 [].forEach.call(document.querySelectorAll('input[data-wc]'), function(c){ c.checked=!!S.wc[c.getAttribute('data-wc')]; });
}
var svT={};
function savedMsg(id){ var el=document.querySelector('[data-sv="'+id+'"]'); if(!el) return; el.textContent='✓ Guardado en este navegador'; clearTimeout(svT[id]); svT[id]=setTimeout(function(){ el.textContent=''; },1800); }

/* ---------------- opinion ---------------- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked = r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function nChecks(id){ var n=0; for(var k in S.wc){ if(S.wc[k] && k.split('|')[0]===id) n++; } return n; }
function summary(){
 var nex=Object.keys(D.ej).length, done=Object.keys(S.ex).length, tx=D.tipos.filter(function(t){ return S.w[t.id] && S.w[t.id].trim(); });
 $('sum').innerHTML='<li>Ejercicios hechos: '+done+' de '+nex+'.</li><li>Textos escritos en «Ahora tú»: '+(tx.length?tx.map(function(t){ return esc(t.n); }).join(', '):'ninguno todavía')+'.</li>';
}
function pack(){
 var L=['CURSO DELE A2 - ESCRITURA: KIT DE FRASES', 'Nombre: '+(S.name||'-'), '', 'EJERCICIOS (mejor resultado):'];
 D.steps.forEach(function(st){ (D.tabex[st.id]||[]).forEach(function(id){ var r=S.ex[id]; L.push('  '+st.label+' - '+D.ej[id].t+': '+(r?r.b+'/'+r.n:'sin hacer')); }); });
 L.push('', 'MIS TEXTOS ("Ahora tú"):');
 var any=false;
 D.tipos.forEach(function(t){ var w=(S.w[t.id]||'').trim(); if(!w) return; any=true;
  L.push('', '== '+t.n+' (tarea '+t.tarea+') ==', 'Tarea: '+t.task, 'Revisión hecha: '+nChecks(t.id)+' de '+t.nchk+' puntos', '', w); });
 if(!any) L.push('  (todavía no he escrito ninguno)');
 L.push('', 'OPINIÓN:', '1. El texto más difícil: '+(S.o1||'-'), '2. Los ejemplos marcados me han ayudado: '+(S.o2||'-'), '3. La trampa que más me pasa: '+(S.o3||'-'), '4. Frase nueva / falta algo: '+(S.o4||'-'), '5. Sensación de control en la Escritura (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 qnew:function(b){ qNew(b.getAttribute('data-ex')); },
 qpick:function(b){ qPick(b); },
 qnext:function(b){ var id=b.getAttribute('data-ex'); Q[id].k++; Q[id].ans=false; qRender(id); },
 hcheck:function(b){ hCheck(b.getAttribute('data-ex')); },
 hnew:function(b){ hNew(b.getAttribute('data-ex')); },
 cmark:function(b){ cMark(b); },
 ccheck:function(b){ cCheck(b.getAttribute('data-ex')); },
 cnew:function(b){ cRender(b.getAttribute('data-ex')); },
 print:function(b){ var v=$('v-'+b.getAttribute('data-p')); v.classList.add('printme'); window.print(); setTimeout(function(){ v.classList.remove('printme'); },500); },
 copy:function(){
  var t=pack(), box=$('cbox');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar automáticamente. Copia tus textos a mano en un correo para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
 }
};
document.addEventListener('click', function(e){
 var g=e.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.getAttribute('data-clean')){ $(t.getAttribute('data-clean')).classList.toggle('clean', t.checked); return; }
 if(t.getAttribute('data-wc')){ S.wc[t.getAttribute('data-wc')]=t.checked; save(); return; }
 if(t.name==='o1'||t.name==='o2'||t.name==='o3'||t.name==='o5'){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){ var t=e.target;
 if(t.getAttribute('data-w')){ var id=t.getAttribute('data-w'); S.w[id]=t.value; save(); nav(); savedMsg(id); return; }
 if(t.id==='o4'){ S.o4=t.value; save(); nav(); } if(t.id==='sname'){ S.name=t.value; save(); } });
window.addEventListener('afterprint', function(){ [].forEach.call(document.querySelectorAll('.printme'), function(v){ v.classList.remove('printme'); }); });

initEx(); initWriting(); renderScale();
go(D.steps.some(function(s){ return s.id===S.cur; }) ? S.cur : 'tareas');
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_M3, body, js))
print("ok", FILE, "·", ", ".join("%s: %d palabras" % (k, v) for k, v in TEXTS.items()),
      "· entradas:", ", ".join("%s %d" % (t["id"], lamina_words(t["lamina"])) for t in B.TIPOS if t["lamina"].get("input")),
      "· ahora:", ", ".join("%s %d" % (t["id"], lamina_words(t["ahora"])) for t in B.TIPOS if t["ahora"].get("input")),
      "· ejercicios:", len(B.EJ), "· fotos:", NFOTOS)
