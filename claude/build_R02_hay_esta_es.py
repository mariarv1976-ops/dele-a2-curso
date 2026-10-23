# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R02 DEL CURSO DE PREPARACION DELE A2: HAY / ESTA / ES
# Uso: python3 build_R02_hay_esta_es.py  -> DELEA2_curso_R02_hay_esta_es.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# Contenidos: solo en banco_R02_hay_esta_es.py. Este archivo monta la pagina y comprueba el banco.
# Mismo formato y motor que la R01 (build_R01_pasados.py): pestanas, correccion inmediata, huecos con
# motivo, "Ahora tu" con escritura (detector de errores tipicos) y oral (fotos M4T2 ya subidas), Tu opinion y Copiar.
# Enfoque cognitivo: HAY = algo nuevo para el otro; ESTA = algo que los dos ya conocemos (solo falta donde);
# ES = donde pasa un evento. Espanol de Espana. Ejemplos propios.
import json, re, sys, unicodedata
from curso_comun import CSS, EMAIL, page
import banco_R02_hay_esta_es as B

TITLE = "Hay, está y es"
FILE = "DELEA2_curso_R02_hay_esta_es.html"
STORAGE = "dele-a2-curso-R02"
IMG_T2 = "https://2spanishteachers.com/wp-content/uploads/" + B.MES_WP_T2.strip("/") + "/M4T2_foto%d.jpg"

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
MARK = re.compile(r"\[(h|e|s):([^\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
VCODE = {"hay": "h", "esta": "e", "es": "s"}
FORMAS = {"hay": {"hay"}, "esta": {"está", "están"}, "es": {"es", "son"}}

def chk_marks(s, where):
    rest = MARK.sub("", s)
    if "[" in rest or "]" in rest: err("marca mal cerrada en " + where + ": " + s[:60])
    for c, w in MARK.findall(s):
        v = {"h": "hay", "e": "esta", "s": "es"}[c]
        if w.lower() not in FORMAS[v]: err("marca [%s:] con una forma que no es de %s en %s: %s" % (c, v, where, w))

def chk_gaps(s, where):
    n = 0
    for g in GAP.findall(s):
        n += 1
        if "#" not in g: err("hueco sin motivo en %s: %s" % (where, g)); continue
        ops, mot = g.split("#")
        ops = ops.split("|")
        if len(ops) != 3 or len(set(o.lower() for o in ops)) != 3: err("hueco sin 3 opciones distintas en %s: %s" % (where, g))
        if mot not in B.MOTIVOS: err("motivo desconocido en %s: %s" % (where, mot)); continue
        v = B.MOTIVOS[mot][0]
        if ops[0].lower() not in FORMAS[v]: err("en %s la buena (%s) no es de %s, como dice su motivo" % (where, ops[0], v))
    if n == 0: err("texto sin huecos: " + where)
    if "[[" in GAP.sub("", s): err("hueco mal cerrado en " + where)
    return n

for k, (v, w) in B.MOTIVOS.items():
    if v not in B.VERBOS or not w: err("motivo mal definido: " + k)
for i, p in enumerate(B.PARES):
    for k in ("a", "b"): chk_marks(p[k], "par %d" % i)
    for k, t in (("a", "ta"), ("b", "tb")):
        if p[t] not in B.VERBOS: err("par %d: verbo desconocido" % i)
        elif "[%s:" % VCODE[p[t]] not in p[k]: err("par %d: la frase %s no lleva %s" % (i, k, p[t]))
    if p["ta"] == p["tb"]: err("par %d: las dos frases con el mismo verbo" % i)
    if not p.get("ra") or not p.get("rb"): err("par %d sin explicacion" % i)
if {p["ta"] for p in B.PARES} | {p["tb"] for p in B.PARES} != set(B.VERBOS): err("las parejas no trabajan los tres verbos")
for v, lst in B.DETRAS.items():
    for s in lst:
        chk_marks(s, "detras " + v)
        if "[%s:" % VCODE[v] not in s: err("detras de %s: el ejemplo no lleva %s: %s" % (v, v, s))
for a, b in B.CADENA:
    chk_marks(a, "cadena"); chk_marks(b, "cadena")
    if "[h:" not in a: err("la cadena empieza con hay: " + a)
for t, s in B.AVISOS: chk_marks(s, "avisos")
for c, d, s in B.DONDE: chk_marks(s, "donde")
for mal, bien, why in B.ERRORES:
    chk_marks(bien, "errores")
    if MARK.sub(r"\2", bien) == mal or not why: err("error tipico sin correccion o sin porque: " + mal)
for k in ("está un parque", "hay el museo", "la fiesta está en", "hay mi hermano"):
    if not any(k in m.lower() for m, _, _ in B.ERRORES): err("falta el error tipico: " + k)

def chk_quiz(items, name, nmin, bm=False, verb=False):
    if len(items) < nmin: err("%s: hacen falta al menos %d items" % (name, nmin))
    for it in items:
        if not it.get("why"): err("%s: item sin explicacion: %s" % (name, it["q"][:40]))
        if bm:
            if it["ok"] not in (0, 1): err(name + ": ok debe ser 0 (bien) o 1 (mal)")
            if it["ok"] == 1 and not it.get("fix"): err(name + ": frase mal sin correccion: " + it["q"])
            if it["ok"] == 0 and it.get("fix"): err(name + ": frase bien con correccion: " + it["q"])
        else:
            o = it["o"]
            if len(o) != 3 or len(set(o)) != 3: err("%s: hacen falta 3 opciones distintas: %s" % (name, it["q"][:40]))
            if it["q"].count("____") != 1: err("%s: un solo hueco ____: %s" % (name, it["q"]))
            if verb:
                fam = [x for x in B.VERBOS if o[0] in FORMAS[x]]
                if not fam: err("%s: la buena no es hay/esta/es: %s" % (name, it["q"]))
                if len({x for op in o for x in B.VERBOS if op in FORMAS[x]}) != 3: err("%s: las opciones tienen que ser hay, esta(n) y es(son): %s" % (name, it["q"]))
chk_quiz(B.P_VERBO, "P_VERBO", 12, verb=True)
chk_quiz(B.P_DETRAS, "P_DETRAS", 8)
chk_quiz(B.E_BIENMAL, "E_BIENMAL", 10, bm=True)
for v in B.VERBOS:
    if not any(i["o"][0] in FORMAS[v] for i in B.P_VERBO): err("P_VERBO: ninguna respuesta buena con " + v)
if not any(i["ok"] == 0 for i in B.E_BIENMAL) or not any(i["ok"] == 1 for i in B.E_BIENMAL): err("bien/mal: hacen falta de los dos tipos")

ngaps = {}
for t in B.TEXTOS: ngaps[t["id"]] = chk_gaps(t["texto"], t["id"])
alltex = " ".join(t["texto"] for t in B.TEXTOS)
for v in B.VERBOS:
    if not any(B.MOTIVOS[g.split("#")[1]][0] == v for g in GAP.findall(alltex)): err("los textos no trabajan " + v)

for L in B.LAMINAS:
    if len(L["pautas"]) != 5: err("lamina %s: 5 pautas" % L["id"])
    for _, vs in L["pautas"]:
        for v in vs:
            if v not in B.VERBOS: err("verbo desconocido en lamina " + L["id"])
    if L.get("pide_es") and not any("es" in vs for _, vs in L["pautas"]): err("lamina %s: pide_es sin pauta de es" % L["id"])

def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
ids = set()
for d in B.DETECTOR:
    if d["t"] not in ("r", "a"): err("tipo de aviso desconocido en el detector: " + d["id"])
    if d["id"] in ids: err("id repetido en el detector: " + d["id"])
    ids.add(d["id"])
    try: d["_rx"] = re.compile(d["re"])
    except re.error as e: err("regex del detector: %s (%s)" % (d["re"], e))
    if not d.get("msg"): err("aviso sin mensaje: " + d["id"])
    if not d.get("case") and d["re"] != norm(d["re"]): err("la regex de %s tiene que ir sin tildes ni mayusculas" % d["id"])
if not ERR:
    for txt, exp in B.DETECTOR_PRUEBAS:
        got = sorted(d["id"] for d in B.DETECTOR if d["_rx"].search(txt if d.get("case") else norm(txt)))
        if got != sorted(exp): err("detector: %r da %s y deberia dar %s" % (txt, got, sorted(exp)))
    for d in B.DETECTOR:
        if not any(d["id"] in e for _, e in B.DETECTOR_PRUEBAS): err("el aviso %s no tiene ninguna prueba" % d["id"])

fids = [f["id"] for f in B.FOTOS]
if len(set(fids)) != len(fids): err("fotos repetidas")
for f in B.FOTOS:
    if not 7 <= f["id"] <= 12: err("foto %s: solo las fotos 7-12 de la tarea 2 (como en el examen)" % f["id"])
    chk_marks(f["hay"], "foto %d hay" % f["id"]); chk_marks(f["esta"], "foto %d esta" % f["id"])
    if f["hay"].count("[h:") < 3 or "[e:" in f["hay"] or "[s:" in f["hay"]: err("foto %d: el modelo de hay lleva solo hay (3 o mas)" % f["id"])
    if f["esta"].count("[e:") < 3 or "[h:" in f["esta"]: err("foto %d: el modelo de esta lleva solo esta (3 o mas)" % f["id"])
    if not f["hay"].startswith("En la foto [h:hay]"): err("foto %d: el modelo empieza con «En la foto hay»" % f["id"])
    if not f.get("alt"): err("foto %d sin descripcion" % f["id"])
if ERR:
    print("\n".join("ERROR: " + e for e in ERR)); sys.exit(1)
for d in B.DETECTOR: d.pop("_rx", None)

# ------------------------------------------------------------------ HTML ESTATICO
def mk(s):
    return MARK.sub(lambda m: '<span class="t%s">%s</span>' % (m.group(1), m.group(2)), s)

COL = {"hay": ("#6B3FA0", "#EFE7F8"), "esta": ("#1D5FA8", "#E2ECF8"), "es": ("#17707F", "#DDF0F2")}
INK = "#14161C"

def person(x, lab):
    return ('<circle cx="%d" cy="152" r="21" fill="#fff" stroke="%s" stroke-width="2.5"/>'
            '<path d="M%d,212 q36,-46 72,0" fill="#fff" stroke="%s" stroke-width="2.5"/>'
            '<text x="%d" y="232" text-anchor="middle" font-size="13" fill="#5E5A55">%s</text>') % (x, INK, x - 36, INK, x, lab)

def bubble(x, txt, stroke, fill, dash=False, sub="", subcol=INK):
    d = ' stroke-dasharray="6 4"' if dash else ''
    ty = 56 if sub else 64
    extra = '<text x="%d" y="80" text-anchor="middle" font-size="13" font-weight="700" fill="%s">%s</text>' % (x, subcol, sub) if sub else ''
    return ('<rect x="%d" y="22" width="190" height="70" rx="14" fill="%s" stroke="%s" stroke-width="2.5"%s/>'
            '<polygon points="%d,92 %d,92 %d,118" fill="%s" stroke="%s" stroke-width="2.5" stroke-linejoin="round"/>'
            '<rect x="%d" y="88" width="20" height="5" fill="%s"/>'
            '<text x="%d" y="%d" text-anchor="middle" font-size="17" font-weight="700" fill="%s">%s</text>') % (
        x - 95, fill, stroke, d, x - 12, x + 8, x - 4, fill, stroke, x - 11, fill, x, ty, INK, txt) + extra

def pin(x, y, col):
    return ('<path d="M%d,%d L%d,%d A17,17 0 1 1 %d,%d Z" fill="%s"/><circle cx="%d" cy="%d" r="6" fill="#fff"/>') % (
        x, y + 34, x - 15, y + 8, x + 15, y + 8, col, x, y)

def diagram(v, obj):
    c, soft = COL[v]
    o = '<svg class="dg" viewBox="0 0 640 240" role="img" aria-label="%s">'
    if v == "hay":
        aria = "Yo conozco algo y el otro no: se lo presento con hay. Para el otro es nuevo."
        o += bubble(120, obj, INK, "#fff") + bubble(520, "+ " + obj, c, soft, dash=True, sub="¡nuevo para mí!", subcol=c)
        o += '<line x1="222" y1="57" x2="404" y2="57" stroke="%s" stroke-width="3"/><polygon points="404,49 420,57 404,65" fill="%s"/>' % (c, c)
        o += '<text x="314" y="45" text-anchor="middle" font-size="18" font-weight="700" fill="%s">HAY</text>' % c
        o += '<text x="314" y="82" text-anchor="middle" font-size="13" fill="#5E5A55">te lo presento</text>'
        o += person(120, "yo") + person(520, "el otro")
    elif v == "esta":
        aria = "Los dos conocemos la misma cosa; con está solo digo dónde está."
        o += bubble(120, obj, c, soft) + bubble(520, obj, c, soft)
        o += '<line x1="222" y1="57" x2="418" y2="57" stroke="%s" stroke-width="2.5" stroke-dasharray="5 5"/>' % c
        o += '<text x="320" y="47" text-anchor="middle" font-size="13" fill="#5E5A55">los dos lo conocemos</text>'
        o += pin(320, 132, c)
        o += '<text x="320" y="110" text-anchor="middle" font-size="18" font-weight="700" fill="%s">ESTÁ</text>' % c
        o += '<text x="320" y="196" text-anchor="middle" font-size="13" font-weight="700" fill="%s">¿dónde?</text>' % c
        o += person(120, "yo") + person(520, "el otro")
    else:
        aria = "Un evento pasa en un sitio y a una hora: con es digo dónde pasa."
        o += '<rect x="330" y="22" width="270" height="196" rx="10" fill="%s" stroke="%s" stroke-width="3"/>' % (soft, c)
        o += '<rect x="330" y="22" width="270" height="44" rx="10" fill="%s"/><rect x="330" y="52" width="270" height="14" fill="%s"/>' % (c, c)
        o += '<text x="465" y="52" text-anchor="middle" font-size="19" font-weight="700" fill="#fff">%s</text>' % obj.upper()
        o += '<circle cx="360" cy="104" r="15" fill="#fff" stroke="%s" stroke-width="2.5"/><line x1="360" y1="104" x2="360" y2="94" stroke="%s" stroke-width="2.5"/><line x1="360" y1="104" x2="368" y2="108" stroke="%s" stroke-width="2.5"/>' % (c, c, c)
        o += '<text x="386" y="110" font-size="15" fill="%s">¿cuándo? → es a las...</text>' % INK
        o += pin(360, 158, c)
        o += '<text x="386" y="172" font-size="15" fill="%s">¿dónde? → es en...</text>' % INK
        o += '<text x="465" y="208" text-anchor="middle" font-size="13" fill="#5E5A55">pasa allí, a esa hora</text>'
        o += bubble(130, obj, INK, "#fff")
        o += '<line x1="232" y1="57" x2="314" y2="57" stroke="%s" stroke-width="3"/><polygon points="314,49 328,57 314,65" fill="%s"/>' % (c, c)
        o += '<text x="272" y="45" text-anchor="middle" font-size="18" font-weight="700" fill="%s">ES</text>' % c
        o += person(130, "yo")
    return (o % aria) + '</svg>'

def icon(v):
    c, soft = COL[v]
    def star(x, y, col, r=13):
        import math
        pts = []
        for i in range(10):
            rr = r if i % 2 == 0 else r * 0.45
            a = math.pi / 5 * i - math.pi / 2
            pts.append("%.1f,%.1f" % (x + rr * math.cos(a), y + rr * math.sin(a)))
        return '<polygon points="%s" fill="%s"/>' % (" ".join(pts), col)
    def head(x):
        return ('<circle cx="%d" cy="112" r="15" fill="#fff" stroke="%s" stroke-width="3"/>'
                '<path d="M%d,152 q26,-34 52,0" fill="#fff" stroke="%s" stroke-width="3"/>') % (x, INK, x - 26, INK)
    def bub(x, col, fill, dash=False):
        dd = ' stroke-dasharray="6 4"' if dash else ''
        return ('<rect x="%d" y="12" width="84" height="56" rx="12" fill="%s" stroke="%s" stroke-width="3"%s/>'
                '<polygon points="%d,68 %d,68 %d,86" fill="%s" stroke="%s" stroke-width="3" stroke-linejoin="round"/>'
                '<rect x="%d" y="64" width="13" height="6" fill="%s"/>') % (x - 42, fill, col, dd, x - 8, x + 6, x - 2, fill, col, x - 7, fill)
    o = '<svg class="ic" viewBox="0 0 300 160" aria-hidden="true">'
    if v == "hay":
        o += bub(60, INK, "#fff") + star(60, 40, INK) + bub(240, c, soft, True) + star(250, 40, c)
        o += '<text x="222" y="49" font-size="26" font-weight="700" fill="%s">+</text>' % c
        o += '<line x1="108" y1="40" x2="182" y2="40" stroke="%s" stroke-width="4"/><polygon points="180,32 194,40 180,48" fill="%s"/>' % (c, c)
        o += head(60) + head(240)
    elif v == "esta":
        o += bub(60, c, soft) + star(60, 40, c) + bub(240, c, soft) + star(240, 40, c)
        o += '<line x1="108" y1="40" x2="194" y2="40" stroke="%s" stroke-width="3" stroke-dasharray="6 6"/>' % c
        o += '<path d="M150,138 L132,106 A21,21 0 1 1 168,106 Z" fill="%s"/><circle cx="150" cy="98" r="8" fill="#fff"/>' % c
        o += head(60) + head(240)
    else:
        o += bub(60, INK, "#fff") + star(60, 40, INK)
        o += '<rect x="138" y="10" width="150" height="140" rx="10" fill="%s" stroke="%s" stroke-width="3"/><rect x="138" y="10" width="150" height="34" rx="10" fill="%s"/><rect x="138" y="32" width="150" height="12" fill="%s"/>' % (soft, c, c, c)
        o += star(213, 27, "#fff", 11)
        o += '<circle cx="165" cy="72" r="13" fill="#fff" stroke="%s" stroke-width="3"/><line x1="165" y1="72" x2="165" y2="63" stroke="%s" stroke-width="3"/><line x1="165" y1="72" x2="172" y2="76" stroke="%s" stroke-width="3"/>' % (c, c, c)
        o += '<rect x="188" y="67" width="82" height="9" rx="4" fill="%s" opacity=".45"/>' % c
        o += '<path d="M165,136 L153,114 A14,14 0 1 1 177,114 Z" fill="%s"/><circle cx="165" cy="108" r="5" fill="#fff"/>' % c
        o += '<rect x="188" y="104" width="70" height="9" rx="4" fill="%s" opacity=".45"/>' % c
        o += '<line x1="104" y1="40" x2="128" y2="40" stroke="%s" stroke-width="4"/><polygon points="126,32 138,40 126,48" fill="%s"/>' % (c, c)
        o += head(60)
    return o + '</svg>'

def cards():
    ej = {"hay": ("En mi barrio [h:hay] un parque.", "El otro no lo conoce: es nuevo."),
          "esta": ("El parque [e:está] al final de mi calle.", "Ya sabemos qué parque: solo falta dónde."),
          "es": ("La fiesta [s:es] en el parque.", "La fiesta pasa allí.")}
    txt = {"hay": ("PRESENTA", "Algo nuevo", "El que escucha <b>no lo conoce</b> todavía. Tú se lo presentas: <b>un, una</b>, un número, mucho, nada..."),
           "esta": ("SITÚA", "Algo conocido", "Los dos <b>ya sabéis de qué cosa habláis</b> (el, la, mi, este, un nombre). Solo dices <b>dónde está</b>."),
           "es": ("EVENTO", "Dónde pasa", "Una fiesta, una boda, una reunión... <b>pasan</b> en un sitio: <b>es en</b> mi casa, <b>es a</b> las nueve.")}
    o = '<div class="cams">'
    for v, cl in (("hay", "h"), ("esta", "e"), ("es", "s")):
        k, h, p = txt[v]
        o += ('<div class="cam %s"><div class="k">%s · %s</div><h3>%s</h3>%s<p>%s</p><div class="ej">%s<br><span class="muted small">%s</span></div></div>'
              % (cl, B.VERBOS[v][0].upper(), k, h, icon(v), p, mk(ej[v][0]), ej[v][1]))
    return o + '</div>'

def detras():
    o = '<div class="mk3">'
    for v, cl in (("hay", "h"), ("esta", "e"), ("es", "s")):
        o += '<div class="%s"><h4>%s + ...</h4><ul>%s</ul></div>' % (cl, B.VERBOS[v][0], "".join("<li>%s</li>" % mk(x) for x in B.DETRAS[v]))
    return o + '</div>'

def cadena():
    o = ''
    for a, b in B.CADENA:
        o += '<div class="chain"><div class="c1"><small>1. PRESENTAS</small>%s</div><div class="arr" aria-hidden="true">→</div><div class="c2"><small>2. SITÚAS</small>%s</div></div>' % (mk(a), mk(b))
    return o

def avisos():
    return '<div class="ef">' + "".join('<div><b>%s</b><span class="small">%s</span></div>' % (t, mk(s)) for t, s in B.AVISOS) + '</div>'

def donde():
    o = ''
    for c, d, s in B.DONDE:
        o += '<div class="box"><span class="chip">%s</span><p class="small muted" style="margin:6px 0">%s</p><p style="margin:0">%s</p></div>' % (c, d, mk(s))
    return o

def errores():
    o = '<div class="errs">'
    for mal, bien, why in B.ERRORES:
        o += '<div class="err"><div class="mal"><span aria-hidden="true">✗</span> <s>%s</s></div><div class="bien"><span aria-hidden="true">✓</span> %s</div><div class="small muted">%s</div></div>' % (mal, mk(bien), why)
    return o + '</div>'

LEG = ('<div class="legend"><span><span class="th">hay</span> presenta algo nuevo</span>'
       '<span><span class="te">está</span> sitúa algo conocido</span><span><span class="ts">es</span> dónde pasa un evento</span></div>')

CSS_R = CSS + r"""
:root{--th:#6B3FA0;--th-soft:#EFE7F8;--te:#1D5FA8;--te-soft:#E2ECF8;--ts:#17707F;--ts-soft:#DDF0F2}
.th,.te,.ts{font-weight:700;border-radius:4px;padding:0 3px}
.th{color:var(--th);background:var(--th-soft)}.te{color:var(--te);background:var(--te-soft)}.ts{color:var(--ts);background:var(--ts-soft)}
.cams{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;border-top:6px solid}
.cam.h{border-top-color:var(--th)}.cam.e{border-top-color:var(--te)}.cam.s{border-top-color:var(--ts)}
.cam .k{font-size:.78rem;font-weight:700;letter-spacing:.06em}
.cam.h .k{color:var(--th)}.cam.e .k{color:var(--te)}.cam.s .k{color:var(--ts)}
.cam h3{margin:2px 0 6px}.cam p{margin:0;font-size:.95rem}
.cam .ej{margin-top:8px;font-size:.92rem;background:var(--paper);border-radius:8px;padding:6px 10px}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pill.ok{border-color:var(--ok)}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.duo button{font:inherit;text-align:left;border:2px solid var(--line);background:#fff;border-radius:10px;padding:10px 12px;cursor:pointer;line-height:1.45}
.duo button.on.h{border-color:var(--th);background:var(--th-soft)}.duo button.on.e{border-color:var(--te);background:var(--te-soft)}.duo button.on.s{border-color:var(--ts);background:var(--ts-soft)}
.duo button small{display:block;font-size:.75rem;font-weight:700;letter-spacing:.05em;color:var(--muted);margin-bottom:2px}
svg.dg{width:100%;height:auto;display:block;margin:6px 0}
.cam svg.ic{width:100%;max-width:260px;height:auto;display:block;margin:6px auto 10px}
.expl{border-radius:8px;padding:10px 14px;margin-top:6px}
.expl.h{background:var(--th-soft)}.expl.e{background:var(--te-soft)}.expl.s{background:var(--ts-soft)}
.ef{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ef div{background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:.95rem}
.mk3,.ef{margin-bottom:22px}
.ef div b{display:block;margin-bottom:2px}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;margin:8px 0}
.mk3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.mk3>div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:.93rem}
.mk3 h4{margin:0 0 6px}
.mk3 .h h4{color:var(--th)}.mk3 .e h4{color:var(--te)}.mk3 .s h4{color:var(--ts)}
.mk3 ul{margin:0;padding-left:1.1em}.mk3 li{margin:3px 0}
.chain{display:grid;grid-template-columns:1fr auto 1fr;gap:8px;align-items:stretch;margin:8px 0}
.chain>div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 12px;font-size:.95rem}
.chain small{display:block;font-size:.72rem;font-weight:700;letter-spacing:.06em;color:var(--muted)}
.chain .c1{border-left:5px solid var(--th)}.chain .c2{border-left:5px solid var(--te)}
.chain .arr{border:0;background:none;display:grid;place-items:center;font-size:1.4rem;padding:0}
.errs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.err{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.err .mal{color:var(--bad)}.err .bien{margin:4px 0}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.vchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px}
.vchip.hay{background:var(--th-soft);color:var(--th)}.vchip.esta{background:var(--te-soft);color:var(--te)}.vchip.es{background:var(--ts-soft);color:var(--ts)}
.qz{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0}
.qz .cnt{font-size:.85rem;color:var(--muted)}
.qz .qq{font-size:1.05rem;margin:6px 0 10px}
.qz .ops{display:grid;gap:8px}
.qz .ops.three{grid-template-columns:repeat(3,1fr)}
.qz .ops button{font:inherit;text-align:left;border:2px solid var(--line);background:#fff;border-radius:10px;padding:9px 12px;cursor:pointer}
.qz .ops.bm{grid-template-columns:1fr 1fr}
.qz .ops.bm button,.qz .ops.three button{text-align:center;font-weight:600}
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
.ophoto{display:grid;grid-template-columns:1.2fr 1fr;gap:16px;align-items:start}
figure.ph{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;padding:8px}
figure.ph img{width:100%;height:auto;display:block;border-radius:8px}
figure.ph figcaption{font-size:.85rem;color:var(--muted);padding:6px 4px 0}
figure.ph .alt{display:none;font-size:.95rem;padding:12px;background:var(--paper);border-radius:8px}
figure.ph.miss img{display:none}figure.ph.miss .alt{display:block}
.ocard{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px}
.ocard .ph1{font-family:Georgia,serif;font-size:1.15rem;font-weight:700}
.clock{font-family:Georgia,serif;font-size:1.6rem;font-weight:700;font-variant-numeric:tabular-nums}
.tbar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:8px 0}
.tbar i{display:block;height:100%;background:var(--coral);width:0;transition:width .25s linear}
.esc{display:grid;gap:6px;margin:8px 0}
.esc div{border:2px dashed var(--line);border-radius:8px;padding:6px 10px;color:var(--muted);font-size:.95rem}
.esc div.on{border-style:solid;border-color:var(--coral);color:var(--ink);background:var(--coral-soft)}
.lugar{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}
.lugar span{font-size:.85rem;background:var(--te-soft);color:var(--te);border-radius:999px;padding:2px 10px}
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
@media (max-width:760px){.ophoto{grid-template-columns:1fr}}
@media (max-width:700px){.cams,.mk3,.errs{grid-template-columns:1fr}.duo,.ef{grid-template-columns:1fr}.chain{grid-template-columns:1fr}.chain .arr{transform:rotate(90deg);padding:2px}.qz .ops.three{grid-template-columns:1fr 1fr 1fr}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:13px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.mk3>div,.err,.chain{break-inside:avoid}}
"""

STEPS = [("idea", "La idea"), ("examen", "En el examen"), ("practica", "Practica"),
         ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_IDEA = """
<h2>¿Nuevo para el otro o ya lo conocemos?</h2>
<p class="lead">Para elegir entre <b>hay</b> y <b>está</b> no pienses en la gramática: piensa en <b>la otra persona</b>. ¿Sabe ya de qué cosa hablas? Y si hablas de un evento (una fiesta, una boda), lo que necesitas es <b>es</b>.</p>
__CARDS__
<h3>Mira la diferencia</h3>
<p class="muted small">Elige una pareja de frases y toca cada una. Mira qué sabe cada persona.</p>
<div class="pills" id="parsel"></div>
<div class="box" id="parvis"></div>
<h3>Lo que va detrás</h3>
<p>Las palabras que van detrás del verbo te ayudan mucho a decidir.</p>
__DETRAS__
<h3>La cadena: primero hay, después está</h3>
<p>En una descripción, las cosas aparecen dos veces: la primera vez las <b>presentas</b> (hay + un, una) y después ya son <b>conocidas</b> (el, la): las <b>sitúas</b> con está. Así se describe una foto, un piso o un barrio.</p>
__CADENA__
<h3>Cuatro cosas que conviene saber</h3>
__AVISOS__
<div class="note">Hay, está y es no son toda la historia de <i>ser</i> y <i>estar</i>: aquí solo miramos <b>qué hay y dónde</b>. El resto (es simpático, está cansado...) lo trabajamos en otra ficha.</div>
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="examen">Siguiente: en el examen</button></div>
"""

V_EXAMEN = """
<h2>Dónde sale en el examen</h2>
<p class="lead">Hay, está y es aparecen en casi todas las pruebas: describir la foto, escribir un correo con un piso o un barrio, dar indicaciones, invitar, leer anuncios. Son errores pequeños, pero se repiten mucho y el examinador los ve.</p>
__LEG__
__DONDE__
<h3>Los errores más típicos</h3>
<p>Tienes que reconocerlos en tus textos. Mira por qué fallan.</p>
__ERRORES__
<div class="tip"><b>Un truco para la foto y para los textos:</b> empieza por el lugar y después hay: «<span class="th">A la izquierda hay</span> una mujer», «<span class="th">En mi barrio hay</span> dos mercados». Así no se te escapa el <s>está un</s>.</div>
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACT = """
<h2>Practica</h2>
<p class="lead">Cuatro ejercicios. Cada respuesta se corrige en el momento, con la explicación.</p>
<div class="pills" id="exsel">
 <button class="pill on" data-act="ex" data-k="p1">1. ¿Hay, está o es?</button>
 <button class="pill" data-act="ex" data-k="p2">2. ¿Qué va detrás?</button>
 <button class="pill" data-act="ex" data-k="e2">3. Textos del examen</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Ahora úsalos en una tarea del examen: escribe un texto o describe una foto en voz alta.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="o">Oral: describe una foto</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu texto y después pulsa <b>Revisar hay / está / es</b>: la página busca los errores típicos (está un..., hay el..., la fiesta está en...). No corrige el texto entero: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="ato" hidden>
 <p>Como en la tarea 2 de la oral, pero solo con una parte: <b>qué hay</b> en la foto y <b>dónde está</b> cada cosa. Primero un minuto con <span class="th">hay</span> (presentas personas y cosas), después un minuto con <span class="te">está</span> (las sitúas). Habla en voz alta.</p>
 <div class="pills" id="fosel"></div>
 <div id="fobox"></div>
</div>
<div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button></div>
"""

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan a mejorarlo. Al final, copia todo (también tus textos y resultados) y envíamelo.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué parte te ha ayudado más?</label>
 <div class="chips" role="group" aria-labelledby="o1l">
  <label><input type="radio" name="o1" value="La idea (nuevo / conocido / evento)">La idea (nuevo / conocido / evento)</label>
  <label><input type="radio" name="o1" value="En el examen y los errores típicos">En el examen y los errores típicos</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tú">Ahora tú</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué te cuesta más ahora?</label>
 <div class="chips" role="group" aria-labelledby="o2l">
  <label><input type="radio" name="o2" value="Hay o está">Hay o está</label>
  <label><input type="radio" name="o2" value="Es con los eventos">Es con los eventos</label>
  <label><input type="radio" name="o2" value="El artículo detrás (un / el)">El artículo detrás (un / el)</label>
  <label><input type="radio" name="o2" value="Describir la foto">Describir la foto</label>
 </div>
 <label class="q" id="o3l">3. ¿Te ayuda pensar «¿es nuevo para el otro o ya lo conocemos?»?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con hay, está y es? (1 = nada, 10 = total)</label>
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
    o = '<h2>Hay, está y es · resumen</h2>' + cards()
    o += '<h3>Lo que va detrás</h3>' + detras()
    o += '<h3>La cadena</h3>' + cadena()
    o += '<h3>Los errores típicos</h3>' + errores()
    return o

views = {
    "idea": V_IDEA.replace("__CARDS__", cards()).replace("__DETRAS__", detras()).replace("__CADENA__", cadena()).replace("__AVISOS__", avisos()),
    "examen": V_EXAMEN.replace("__LEG__", LEG).replace("__DONDE__", donde()).replace("__ERRORES__", errores()),
    "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R02</small></div>
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
    "motivos": {k: {"v": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "verbos": {k: v[0] for k, v in B.VERBOS.items()},
    "pares": [dict(p, a=mk(p["a"]), b=mk(p["b"]), da=diagram(p["ta"], p["obj"]), db=diagram(p["tb"], p["obj"])) for p in B.PARES],
    "qz": {
        "p1": {"items": B.P_VERBO, "n": 8, "name": "¿Hay, está o es?", "three": True, "info": "Elige el verbo. Piensa: ¿es nuevo para el otro, ya lo conocemos o es un evento?"},
        "p2": {"items": B.P_DETRAS, "n": 8, "name": "¿Qué va detrás?", "three": True, "info": "Mira el verbo (en negrita) y elige la palabra que va con él."},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Errores típicos de los exámenes. ¿La frase está bien o mal?"},
    },
    "textos": B.TEXTOS,
    "laminas": B.LAMINAS, "detector": B.DETECTOR,
    "fotos": [{"id": f["id"], "titulo": f["titulo"], "alt": f["alt"], "img": IMG_T2 % f["id"], "hay": mk(f["hay"]), "esta": mk(f["esta"])} for f in B.FOTOS],
    "lugar": B.LUGAR,
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function blank(){ return {cur:'idea', seen:{}, par:0, pv:'a', ex:'p1', etext:D.textos[0].id, at:'w',
  qz:{}, qlog:{}, cz:{}, w:{}, wchk:{}, wrev:{}, lam:D.laminas[0].id, foto:D.fotos[0].id, fph:{}, fchk:{}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
var VCL = {hay:'h', esta:'e', es:'s'};

/* ---------------- navegacion ---------------- */
function stepDone(id){
 if(id==='practica') return ['p1','p2','e4'].some(function(k){ return !!S.qlog[k]; }) || Object.keys(S.cz).length>0;
 if(id==='ahora') return Object.keys(S.w).some(function(k){ return (S.w[k]||'').trim().length>20; }) || Object.keys(S.fph).some(function(k){ return S.fph[k]>=3; });
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

/* ---------------- 1. la idea: parejas ---------------- */
function renderPar(){
 var o=''; D.pares.forEach(function(p,i){ o+='<button class="pill'+(S.par===i?' on':'')+'" data-act="par" data-i="'+i+'">'+esc(p.tema)+'</button>'; });
 $('parsel').innerHTML=o;
 var p=D.pares[S.par], m=S.pv, t=(m==='a'?p.ta:p.tb);
 function lab(v){ return D.verbos[v].toUpperCase()+' · '+(v==='hay'?'ALGO NUEVO':(v==='esta'?'ALGO CONOCIDO':'UN EVENTO')); }
 $('parvis').innerHTML = '<div class="duo">'+
  '<button class="'+VCL[p.ta]+(m==='a'?' on':'')+'" data-act="pv" data-m="a" aria-pressed="'+(m==='a')+'"><small>'+lab(p.ta)+'</small>'+p.a+'</button>'+
  '<button class="'+VCL[p.tb]+(m==='b'?' on':'')+'" data-act="pv" data-m="b" aria-pressed="'+(m==='b')+'"><small>'+lab(p.tb)+'</small>'+p.b+'</button></div>'+
  (m==='a'?p.da:p.db)+'<div class="expl '+VCL[t]+'" aria-live="polite">'+(m==='a'?p.ra:p.rb)+'</div>';
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
  if(fails.length){ o+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fails.forEach(function(r){ var it=c.items[r.k]; o+='<li>'+esc(strip(it.q).slice(0,90))+' → <b>'+(c.bm?(it.ok?'Mal: '+strip(it.fix):'Bien'):esc(it.o[0]))+'</b></li>'; }); o+='</ul>'; }
  o+='<div class="row"><button class="btn cta" data-act="qrep" data-k="'+k+'">Repetir con otras frases</button></div></div>';
  box.innerHTML=o; return;
 }
 var idx=st.order[st.i], it=c.items[idx], ans=st.res[st.i];
 var opts, ok;
 if(c.bm){ opts=[[0,'Bien'],[1,'Mal']]; ok=it.ok; }
 else { if(!st.perm[idx]){ st.perm[idx]=shuffle(range(it.o.length)); save(); } opts=st.perm[idx].map(function(j){ return [j,it.o[j]]; }); ok=0; }
 var o='<div class="qz"><div class="cnt">'+esc(c.name)+' · '+(st.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(st.i/N*100)+'%"></i></div>';
 o+='<div class="qq">'+it.q.replace('____', ans&&!c.bm?'<b style="color:var(--ok)">'+esc(it.o[0])+'</b>':'____')+'</div><div class="ops'+(c.bm?' bm':(c.three?' three':''))+'" role="group">';
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
 if(st.i===st.order.length-1){
  var n=st.res.filter(function(r){return r&&r.ok;}).length;
  var fl=[]; st.res.forEach(function(r){ if(r&&!r.ok) fl.push(strip(c.items[r.k].q).slice(0,70)); });
  S.qlog[k]={last:n+'/'+st.order.length, fails:fl};
 }
 save();
}

/* ---------------- motor de huecos ---------------- */
var GAPRX=/\[\[([^\]]+)\]\]/g;
function seeded(arr, seed){ var h=0; for(var i=0;i<seed.length;i++) h=(h*31+seed.charCodeAt(i))>>>0; var a=arr.slice(); for(var j=a.length-1;j>0;j--){ h=(h*1103515245+12345)>>>0; var r=h%(j+1); var t=a[j]; a[j]=a[r]; a[r]=t; } return a; }
function parseGaps(id, s){
 var n=0;
 var html=s.replace(GAPRX, function(m0, inner){
  n++; var p=inner.split('#'), ops=p[0].split('|'), gid=id+'-'+n, cur=S.cz[gid];
  var sel='<sup>'+n+'</sup><select data-g="'+gid+'" aria-label="Hueco '+n+'"'+(cur&&cur.cur===ops[0]?' disabled class="ok"':(cur?' class="no"':''))+'><option value="">…</option>';
  seeded(ops, gid).forEach(function(o){ sel+='<option'+(cur&&cur.cur===o?' selected':'')+'>'+esc(o)+'</option>'; });
  return sel+'</select>';
 });
 return {html:html, n:n};
}
function gapInfo(id, s){ var list=[], n=0; s.replace(GAPRX, function(m0,inner){ n++; var p=inner.split('#'); list.push({gid:id+'-'+n, n:n, ok:p[0].split('|')[0], m:p[1]}); return m0; }); return list; }
function fbList(id, s){
 var o='', tot=0, done=0, first=0;
 gapInfo(id,s).forEach(function(g){
  tot++; var c=S.cz[g.gid]; if(!c) return; done += c.cur===g.ok?1:0; if(c.first===g.ok) first++;
  var mo=D.motivos[g.m], vn=D.verbos[mo.v];
  if(c.cur===g.ok) o+='<li class="ok">'+g.n+'. ✓ <b>'+esc(g.ok)+'</b> · <span class="vchip '+mo.v+'">'+vn+'</span> '+mo.w+'</li>';
  else o+='<li class="no">'+g.n+'. ✗ <b>'+esc(c.cur)+'</b> no va aquí. Pista: <span class="vchip '+mo.v+'">'+vn+'</span> '+mo.w+' Prueba otra vez.</li>';
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
function czChange(sel){
 var gid=sel.getAttribute('data-g'), v=sel.value; if(!v) return;
 var c=S.cz[gid]||{}; if(!c.first) c.first=v; c.cur=v; S.cz[gid]=c; save();
 renderEx(); nav();
 var ns=document.querySelector('select[data-g="'+gid+'"]'); if(ns && ns.disabled===false) ns.focus();
}
var EXINFO={e2:'Textos como los del examen: un anuncio, un correo, la descripción de una foto y un texto para una revista. Elige el verbo de cada hueco: la corrección sale enseguida, con el motivo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+'</div>';
 if(L.intro) h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(v){ return '<span class="vchip '+v+'">'+D.verbos[v]+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas de color te dicen qué verbo pide cada pauta. Recuerda: unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu texto</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar hay / está / es</button></div><div id="rvbox" aria-live="polite"></div>';
 var CH=['Lo nuevo (un, una, números, muchos) va con <b>hay</b>.','Lo conocido (el, la, mi, este, nombres) va con <b>está</b> o <b>están</b>.','Las fiestas, comidas y celebraciones: <b>es en</b> (dónde) y <b>es a las...</b> (cuándo).','Hay no cambia: hay dos, hay muchos.','Primero presento (hay) y después sitúo (está).'];
 h+='<h3>Mi lista de hay / está / es</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
function review(){
 var L=lam(), txt=$('wtext').value, out=[], red=0;
 if(txt.trim().length<20){ $('rvbox').innerHTML='<ul class="rv"><li class="a">Escribe primero tu texto.</li></ul>'; return; }
 var sents=txt.match(/[^.!?\n]+[.!?]*/g)||[];
 sents.forEach(function(s){
  if(!s.trim()) return;
  var n=norm(s);
  D.detector.forEach(function(d){
   var src=d.case?s:n, r=new RegExp(d.re,'g'), m;
   while((m=r.exec(src))){
    var a=m.index, w=m[0];
    if(d.case && /^[^A-Za-z]/.test(w)){ a++; w=w.slice(1); }
    if(d.t==='r') red++;
    var hl=esc(s.slice(0,a))+'<mark>'+esc(s.substr(a,w.length))+'</mark>'+esc(s.slice(a+w.length));
    out.push('<li class="'+d.t+'">'+(d.t==='r'?'<b>¡Ojo!</b> ':'<b>Mira esto:</b> ')+d.msg+'<br><span class="small">'+hl+'</span></li>');
    if(r.lastIndex===m.index) r.lastIndex++;
   }
  });
 });
 var nt=norm(txt), nh=(nt.match(/\bhay\b/g)||[]).length, ne=(nt.match(/\b(esta|estan)\b/g)||[]).length, ns=(nt.match(/\bes (en|a las|el|la|los|las)\b/g)||[]).length;
 if(L.pide_es && !ns) out.push('<li class="a"><b>La pauta del evento:</b> no encuentro «es en» ni «es a las». ¿Has dicho dónde y cuándo es? «La fiesta es en mi casa, el sábado a las nueve».</li>');
 if(!nh) out.push('<li class="a"><b>Hay:</b> no lo has usado. La lámina te pide contar qué hay: «En mi barrio hay...».</li>');
 if(!red) out.unshift('<li class="g">No he encontrado los errores típicos. ¡Bien! Has usado <b>hay</b> '+nh+' '+(nh===1?'vez':'veces')+' y <b>está / están</b> '+ne+' '+(ne===1?'vez':'veces')+'. Mira tú también cada frase con la lista de abajo.</li>');
 var wc=txt.trim().split(/\s+/).length;
 S.wrev[L.id]={red:red, hay:nh, esta:ne, es:ns, words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul><p class="muted small">Tu texto: '+wc+' palabras (la lámina pide '+L.palabras[0]+'-'+L.palabras[1]+'). La página solo busca estos errores: no los ve todos. Tu profesora corrige el texto completo.</p>';
}

/* ---------------- ahora tu: oral (foto) ---------------- */
var TM=null, T0=0, TDUR=60;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } }
var ESC={1:['0 s · Empieza: «En la foto hay...». Cuenta las personas.','20 s · Presenta cosas con el lugar delante: «A la izquierda hay..., en la pared hay...».','40 s · Usa números y cantidades: dos, tres, muchos, algunos...'],
         2:['0 s · Ahora ya las conocemos: «La mujer está..., el niño está...».','20 s · Sitúa las cosas: «Los abrigos están en..., la mesa está delante de...».','40 s · Usa palabras de lugar distintas: al fondo, entre..., al lado de...']};
var FCH=['He empezado con «En la foto hay...».','Después de hay he dicho un, una, números o muchos.','Con está he dicho el, la, los o una persona concreta.','No he dicho «está un...» ni «hay el...».','He usado al menos cuatro palabras de lugar distintas.'];
function foto(){ return D.fotos.filter(function(f){return f.id===S.foto;})[0]; }
function renderFoto(){
 var o=''; D.fotos.forEach(function(f){ var d=(S.fph[f.id]||0)>=3; o+='<button class="pill'+(S.foto===f.id?' on':'')+(d?' ok':'')+'" data-act="foto" data-id="'+f.id+'">'+esc(f.titulo)+(d?' ✓':'')+'</button>'; });
 $('fosel').innerHTML=o;
 var f=foto(), ph=S.fph[f.id]||0;
 var h='<div class="ophoto"><figure class="ph" id="fig"><img src="'+f.img+'" alt="'+esc(f.alt)+'" loading="lazy"><div class="alt"><b>Foto:</b> '+esc(f.alt)+'</div><figcaption>'+esc(f.titulo)+'</figcaption></figure><div class="ocard">';
 if(ph===0){
  h+='<div class="ph1">Prepárate</div><p>Mira la foto unos segundos. Vas a hablar <b>dos minutos</b>: uno para decir qué hay y otro para decir dónde está cada cosa.</p><p class="small"><b>Palabras de lugar:</b></p><div class="lugar">'+D.lugar.map(function(x){return '<span>'+esc(x)+'</span>';}).join('')+'</div>';
  h+='<div class="row"><button class="btn cta" data-act="fgo" data-p="1">Empezar: qué hay (1 min)</button></div>';
 } else if(ph<3){
  h+='<div class="ph1">'+(ph===1?'1. Qué hay <span class="th">hay</span>':'2. Dónde está <span class="te">está</span>')+'</div>';
  h+='<div class="clock" id="fclk" aria-live="off">1:00</div><div class="tbar"><i id="tbar"></i></div><div class="esc" id="esc">'+ESC[ph].map(function(x){return '<div>'+x+'</div>';}).join('')+'</div>';
  if(ph===2) h+='<div class="lugar">'+D.lugar.map(function(x){return '<span>'+esc(x)+'</span>';}).join('')+'</div>';
  h+='<div class="row"><button class="btn" data-act="fstart" id="fbtn">Empezar el reloj</button><button class="btn cta" data-act="fgo" data-p="'+(ph+1)+'">'+(ph===1?'Siguiente: dónde está':'He terminado')+'</button></div>';
 } else {
  h+='<div class="ph1">¿Qué tal ha ido?</div><ul class="check">'; FCH.forEach(function(c,i){ var k=f.id+'-'+i; h+='<li><label><input type="checkbox" data-fchk="'+k+'"'+(S.fchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
  h+='<div class="model"><b>Una descripción modelo: qué hay</b><br>'+f.hay+'</div><div class="model"><b>Y dónde está</b><br>'+f.esta+'</div>';
  h+='<p class="small muted">En el examen, después sigues con las otras preguntas de la lámina (qué hacen, cómo se sienten...). Practícalas en el taller de la foto.</p>';
  h+='<div class="row"><button class="btn" data-act="fgo" data-p="0">Otra vez</button><button class="btn cta" data-act="fnext">Otra foto</button></div>';
 }
 $('fobox').innerHTML=h+'</div></div>';
 var im=$('fig').querySelector('img'); im.addEventListener('error', function(){ $('fig').classList.add('miss'); });
 if(im.complete && im.naturalWidth===0 && im.src) $('fig').classList.add('miss');
}
function fstart(){
 stopTimer(); T0=Date.now(); var b=$('fbtn'); if(b) b.textContent='Otra vez';
 TM=setInterval(function(){
  var t=(Date.now()-T0)/1000, bar=$('tbar'), es=$('esc'), ck=$('fclk'); if(!bar){ stopTimer(); return; }
  var left=Math.max(0,Math.ceil(TDUR-t)); ck.textContent='0:'+(left<10?'0':'')+left; if(left===60) ck.textContent='1:00';
  bar.style.width=Math.min(100,t/TDUR*100)+'%';
  var k=t<20?0:(t<40?1:2), ds=es.children; for(var i=0;i<ds.length;i++) ds[i].classList.toggle('on', i===k);
  if(t>=TDUR){ stopTimer(); bar.style.width='100%'; ck.textContent='0:00'; }
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
 var L=['CURSO DELE A2 - R02: HAY, ESTA Y ES','Nombre: '+(S.name||'-'),''];
 L.push('EJERCICIOS (ultimo resultado)');
 ['p1','p2','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 D.textos.forEach(function(t){
  var f=fbList(t.id,t.texto), errs=[];
  gapInfo(t.id,t.texto).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); });
  var started=Object.keys(S.cz).some(function(k){return k.indexOf(t.id+'-')===0;});
  L.push('- Textos del examen, '+t.titulo+': '+(started?f.first+'/'+f.tot+' a la primera'+(f.done<f.tot?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 L.push('','ORAL: DESCRIBE UNA FOTO (hay / esta)');
 var fd=D.fotos.filter(function(f){ return (S.fph[f.id]||0)>=3; });
 if(!fd.length) L.push('sin hacer');
 fd.forEach(function(f){ var n=0; FCH.forEach(function(c,i){ if(S.fchk[f.id+'-'+i]) n++; }); L.push('- Foto '+f.id+' ('+f.titulo+'): hecha, autorrevision '+n+'/'+FCH.length); });
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' ('+l.palabras[0]+'-'+l.palabras[1]+' palabras)','Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision: '+rv.red+' avisos rojos | hay '+rv.hay+', esta(n) '+rv.esta+', es '+rv.es+' | '+rv.words+' palabras');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. Lo que mas cuesta: '+(S.o2||'-'),'3. Nuevo / conocido: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 par:function(b){ S.par=+b.getAttribute('data-i'); S.pv='a'; save(); renderPar(); },
 pv:function(b){ S.pv=b.getAttribute('data-m'); save(); renderPar(); },
 ex:function(b){ S.ex=b.getAttribute('data-k'); save(); renderEx(); },
 etext:function(b){ S.etext=b.getAttribute('data-id'); save(); renderE2(); },
 qa:function(b){ var k=b.getAttribute('data-k'); qzAnswer(k, +b.getAttribute('data-o')); qzRender(k, $('exbox')); nav(); var f=$('exbox').querySelector('.fb'); if(f&&f.scrollIntoView) f.scrollIntoView({block:'nearest'}); },
 qnext:function(b){ var k=b.getAttribute('data-k'); S.qz[k].i++; save(); qzRender(k, $('exbox')); },
 qrep:function(b){ var k=b.getAttribute('data-k'); qzNew(k); qzRender(k, $('exbox')); },
 czreset:function(b){ b.getAttribute('data-ids').split(',').forEach(function(id){ Object.keys(S.cz).forEach(function(g){ if(g.indexOf(id+'-')===0) delete S.cz[g]; }); }); save(); renderEx(); nav(); },
 at:function(b){ S.at=b.getAttribute('data-k'); save(); renderAt(); },
 lam:function(b){ S.lam=b.getAttribute('data-id'); save(); renderLam(); },
 review:function(){ review(); nav(); },
 foto:function(b){ stopTimer(); S.foto=+b.getAttribute('data-id'); save(); renderFoto(); },
 fgo:function(b){ stopTimer(); var p=+b.getAttribute('data-p'), f=S.foto; S.fph[f]=p; save(); renderFoto(); nav(); if(p===1||p===2) fstart(); },
 fstart:function(){ fstart(); },
 fnext:function(){ stopTimer(); var ids=D.fotos.map(function(f){return f.id;}), free=ids.filter(function(i){ return (S.fph[i]||0)<3 && i!==S.foto; }); if(!free.length) free=ids.filter(function(i){return i!==S.foto;}); S.foto=free[Math.floor(Math.random()*free.length)]; save(); renderFoto(); },
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
 if(S.at==='w') renderLam(); else renderFoto();
}
document.addEventListener('click', function(e){
 var g=e.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.tagName==='SELECT' && t.hasAttribute('data-g')){ czChange(t); return; }
 if(t.hasAttribute && t.hasAttribute('data-wchk')){ S.wchk[t.getAttribute('data-wchk')]=t.checked; save(); return; }
 if(t.hasAttribute && t.hasAttribute('data-fchk')){ S.fchk[t.getAttribute('data-fchk')]=t.checked; save(); return; }
 if(['o1','o2','o3','o5'].indexOf(t.name)>=0){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){
 var t=e.target;
 if(t.id==='wtext'){ S.w[S.lam]=t.value; save(); }
 if(t.id==='o4'){ S.o4=t.value; save(); }
 if(t.id==='sname'){ S.name=t.value; save(); }
});
window.addEventListener('afterprint', function(){ var v=$('v-resumen'); if(v) v.classList.remove('printme'); });
if(S.fph){ Object.keys(S.fph).forEach(function(k){ if(S.fph[k]===1||S.fph[k]===2) S.fph[k]=0; }); }

renderPar(); renderEx(); renderAt(); renderOpn(); go(S.cur);
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_R, BODY, js))
print("ok", FILE, "| huecos:", sum(ngaps.values()),
      "| items:", len(B.P_VERBO) + len(B.P_DETRAS) + len(B.E_BIENMAL),
      "| pruebas del detector:", len(B.DETECTOR_PRUEBAS), "| fotos:", len(B.FOTOS))
