# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R08 DEL CURSO DE PREPARACION DELE A2: CONECTORES (LAS FLECHAS ENTRE FRASES)
# Uso: python3 build_R08_conectores.py  -> DELEA2_curso_R08_conectores.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# Contenidos: solo en banco_R08_conectores.py. Este archivo monta la pagina y comprueba el banco.
# Mismo formato y motor que R01-R07: pestanas, correccion inmediata, huecos con motivo (barajado arreglado),
# "Ahora tu" con escritura (detector de conectores) y oral (cuentalo en orden, con reloj), Tu opinion y Copiar.
# Sin imagenes: todos los dibujos son SVG.
# Enfoque cognitivo: LAS FLECHAS ENTRE FRASES. Ordenar (la linea de pasos), sumar (el mas), girar (la curva),
# la causa (la flecha hacia atras) y lo que pasa (la flecha hacia delante). El espejo: porque / por eso.
# Solo conectores [P] del Plan curricular; los [R] (asi que, aunque, como, sin embargo) solo en un recuadro.
import json, os, re, shutil, subprocess, sys, tempfile, unicodedata
from curso_comun import CSS, EMAIL, page
import banco_R08_conectores as B

TITLE = "Conectores: las flechas entre frases"
FILE = "DELEA2_curso_R08_conectores.html"
STORAGE = "dele-a2-curso-R08"

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
MARK = re.compile(r"\[(o|s|g|c|r):([^\[\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
FAM = B.FAMILIAS
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
def plain(s): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", MARK.sub(lambda m: m.group(2), s))).strip()
def filled(s): return re.sub(r"<[^>]+>", " ", GAP.sub(lambda m: m.group(1).split("#")[0].split("|")[0], s))
def low(w): return w.strip(" ,.;:¡!¿?").lower()

def chk_marks(s, where, need=0, fams=None):
    rest = MARK.sub("", s)
    if "[" in rest or "]" in rest: err("marca mal cerrada en %s: %s" % (where, s[:80]))
    gs = MARK.findall(s)
    for k, w in gs:
        if low(w) not in FAM[k]["words"]: err("%s: «%s» no es una flecha de %s" % (where, w, FAM[k]["n"]))
        if fams is not None and k not in fams: err("%s: marca de otra flecha (%s): %s" % (where, k, s[:70]))
    if len(gs) < need: err("%s: hacen falta al menos %d marcas" % (where, need))
    return gs

if list(FAM) != B.ORDEN_FAM: err("FAMILIAS y ORDEN_FAM no coinciden")
for k, f in FAM.items():
    if not (f["n"] and f["txt"] and f["words"]): err("familia mal definida: " + k)
for k, (f, w, ok) in B.MOTIVOS.items():
    if f not in FAM or not w or not ok: err("motivo mal definido: " + k)
    for x in ok:
        if x not in FAM[f]["words"]: err("motivo %s: «%s» no es de su flecha" % (k, x))

# 1. Las flechas
for p in B.PAREJAS:
    for side in ("a", "b"):
        d = p[side]
        gs = chk_marks(d["f"], "pareja %s" % p["tema"], 1)
        if d["fam"] not in [k for k, _ in gs]: err("pareja %s: la frase %s no lleva la flecha %s" % (p["tema"], side, d["fam"]))
        if not (d["x"] and d["y"]): err("pareja %s: faltan las cajas del dibujo" % p["tema"])
    if p["a"]["fam"] == p["b"]["fam"]: err("pareja %s: las dos frases tienen la misma flecha" % p["tema"])
    if not p.get("expl"): err("pareja sin explicacion: " + p["tema"])
if {p[s]["fam"] for p in B.PAREJAS for s in "ab"} != set(FAM): err("parejas: tienen que salir las cinco flechas")
if {k for k, *_ in B.VISTAZO} != set(FAM): err("vistazo: una fila por flecha")
for k, w, ej, d in B.VISTAZO: chk_marks(ej, "vistazo " + k, 1, k)
gs = chk_marks(B.DESPUES, "historia (despues)", 6)
if {k for k, _ in gs} != set(FAM): err("la historia con flechas tiene que usar las cinco flechas")
if MARK.search(B.ANTES) or len(re.findall(r"\by\b", B.ANTES)) < 6: err("la historia sin flechas tiene que ir solo con y (6 o mas)")
for e in B.ESPEJO:
    if [x for x in chk_marks(e["c"], "espejo " + e["tema"], 1)] != [("c", "porque")]: err("espejo %s: la frase c lleva solo [c:porque]" % e["tema"])
    if [(k, low(w)) for k, w in chk_marks(e["r"], "espejo " + e["tema"], 1)] != [("r", "por eso")]: err("espejo %s: la frase r lleva solo [r:por eso]" % e["tema"])
for s in B.ES_QUE: chk_marks(s, "es que", 1, "c")
chk_marks(B.ES_QUE_USTED, "es que de usted", 1, "c")
for s in B.ENTONCES_CONV: chk_marks(s, "entonces", 1, "r")
for c, d, s in B.DONDE: chk_marks(s, "donde " + c, 1)
for mal, bien, why in B.ERRORES:
    chk_marks(bien, "errores", 1)
    if plain(bien) == mal or not why: err("error tipico sin correccion o sin porque: " + mal)
for a in B.AL_FINAL:
    if "al final" not in a["txt"].lower() or not (a["q"] and a["a"]): err("al final mal definido: " + a["txt"][:40])
# los [R] no salen en los ejercicios
R_WORDS = re.compile(r"\b(?:asi que|aunque|sin embargo)\b|(?:^|[.!?]\s*)como\s+(?!se\b)")

# Ejercicios
def chk_opts(it, name):
    o = it["o"]
    if len(o) != 3 or len(set(x.lower() for x in o)) != 3: err("%s: hacen falta 3 opciones distintas: %s" % (name, it["q"][:50]))
    if not it.get("why"): err("%s: item sin explicacion: %s" % (name, it["q"][:50]))
    if it["q"].count("____") != 1: err("%s: un solo ____ por frase: %s" % (name, it["q"][:50]))
def fill(it): return it["q"].replace("____", it["o"][0])
if len(B.P_FLECHA) < 14: err("P_FLECHA: al menos 14")
for it in B.P_FLECHA:
    chk_opts(it, "P_FLECHA")
    good = low(it["o"][0])
    if it["f"] not in FAM: err("P_FLECHA: flecha desconocida " + it["q"]); continue
    if good not in FAM[it["f"]]["words"] and not (it["f"] == "s" and good == "o"): err("P_FLECHA: la buena (%s) no es de su flecha: %s" % (good, it["q"]))
    for o in it["o"]:
        if R_WORDS.search(norm(o)): err("P_FLECHA: conector [R] en las opciones: " + o)
if {it["f"] for it in B.P_FLECHA} != set(FAM): err("P_FLECHA: tienen que salir las cinco flechas")
if len(B.P_PORQUE) < 12: err("P_PORQUE: al menos 12")
for it in B.P_PORQUE:
    chk_opts(it, "P_PORQUE")
    if sorted(it["o"][:2]) != ["por eso", "porque"]: err("P_PORQUE: las dos primeras opciones son porque y por eso: " + it["q"])
if len({it["o"][0] for it in B.P_PORQUE}) != 2: err("P_PORQUE: hacen falta frases con porque y con por eso")
if len(B.E_BIENMAL) < 14: err("E_BIENMAL: al menos 14")
for it in B.E_BIENMAL:
    if not it.get("why"): err("bien/mal sin explicacion: " + it["q"])
    if it["ok"] not in (0, 1): err("bien/mal: ok debe ser 0 o 1")
    if it["ok"] == 1 and not it.get("fix"): err("bien/mal: frase mal sin correccion: " + it["q"])
    if it["ok"] == 0 and it.get("fix"): err("bien/mal: frase bien con correccion: " + it["q"])
if sum(1 for i in B.E_BIENMAL if i["ok"] == 0) < 5: err("bien/mal: faltan frases bien")

# Textos con huecos
def chk_gaps(t):
    n = 0
    for g in GAP.findall(t["texto"]):
        n += 1
        if "#" not in g: err("hueco sin motivo en %s: %s" % (t["id"], g)); continue
        ops, mot = g.split("#"); ops = ops.split("|")
        if len(ops) != 3 or len(set(o.lower() for o in ops)) != 3: err("hueco sin 3 opciones distintas en %s: %s" % (t["id"], g))
        if mot not in B.MOTIVOS: err("motivo desconocido en %s: %s" % (t["id"], mot)); continue
        if ops[0].lower() not in B.MOTIVOS[mot][2]: err("en %s la buena (%s) no es la de su motivo %s" % (t["id"], ops[0], mot))
        for o in ops:
            if R_WORDS.search(norm(o)): err("hueco con conector [R] en %s: %s" % (t["id"], o))
    if n < 5: err("texto con pocos huecos: " + t["id"])
    if "[[" in GAP.sub("", t["texto"]) or "]]" in GAP.sub("", t["texto"]): err("hueco mal cerrado en " + t["id"])
    return n
ngaps = {t["id"]: chk_gaps(t) for t in B.TEXTOS}
usados = {g.split("#")[1] for t in B.TEXTOS for g in GAP.findall(t["texto"])}
for m in B.MOTIVOS:
    if m not in usados: err("los textos no usan el motivo " + m)

for L in B.LAMINAS:
    if len(L["pautas"]) != 5: err("lamina %s: 5 pautas" % L["id"])
    for _, fs in L["pautas"]:
        for f in fs:
            if f not in B.FOCOS: err("foco desconocido en lamina " + L["id"])
    nw = len(L["mensaje"].split())
    if L["tarea"].startswith("Tarea 1") and not 35 <= nw <= 45: err("lamina %s: el mensaje de entrada tiene %d palabras (35-45)" % (L["id"], nw))
if {f for L in B.LAMINAS for _, fs in L["pautas"] for f in fs} != set(B.FOCOS): err("las laminas tienen que trabajar todas las flechas")
if set(B.FOCO_FAM) != set(B.FOCOS) or set(B.FOCO_FAM.values()) != set(FAM): err("FOCO_FAM mal definido")
if set(B.CUENTA) != set(FAM): err("CUENTA: una regex por flecha")

# Oral
if len(B.ORAL) < 10: err("oral: al menos 10 tarjetas")
for o in B.ORAL:
    gs = chk_marks(o["m"], "oral " + o["tema"], 3)
    if len({k for k, _ in gs}) < 3: err("oral %s: el modelo tiene que usar al menos tres flechas distintas" % o["tema"])
    if len(o["hechos"]) != 4: err("oral %s: cuatro hechos" % o["tema"])

# Detector
ids = set()
for d in B.DETECTOR:
    if d["t"] not in ("r", "a") or d["sc"] not in ("s", "x"): err("aviso mal definido: " + d["id"])
    if d["id"] in ids: err("id repetido en el detector: " + d["id"])
    ids.add(d["id"])
    try: d["_rx"] = re.compile(d["re"])
    except re.error as e: err("regex del detector: %s (%s)" % (d["id"], e))
    if not d.get("msg"): err("aviso sin mensaje: " + d["id"])
    if d["re"] != norm(d["re"]): err("la regex de %s tiene que ir sin tildes ni mayusculas" % d["id"])
    if "(?<" in d["re"] or "(?P" in d["re"]: err("la regex de %s usa algo que no funciona igual en el navegador" % d["id"])
for k, r in B.CUENTA.items():
    if r != norm(r) or "(?<" in r: err("cuenta no valida para el navegador: " + k)
for k in B.REQ:
    if k not in ids: err("REQ: id desconocido " + k)

SENT = re.compile(r"[^.!?\n]+[.!?]*")
def det(txt, only_red=False):
    out = set()
    sents = [norm(s) for s in SENT.findall(txt)]
    for d in B.DETECTOR:
        if only_red and d["t"] != "r": continue
        if d["sc"] == "s":
            if any(d["_rx"].search(s) for s in sents): out.add(d["id"])
        elif d["_rx"].search(norm(txt)): out.add(d["id"])
    return sorted(out)

if not ERR:
    for txt, exp in B.DETECTOR_PRUEBAS:
        got = det(txt)
        if got != sorted(exp): err("detector: %r da %s y deberia dar %s" % (txt, got, sorted(exp)))
    for d in B.DETECTOR:
        if not any(d["id"] in e for _, e in B.DETECTOR_PRUEBAS): err("el aviso %s no tiene ninguna prueba" % d["id"])
    if sum(1 for _, e in B.DETECTOR_PRUEBAS if not e) < 10: err("detector: hacen falta al menos 10 pruebas que NO deben saltar")
    vistos_err = set()
    for mal, _, _ in B.ERRORES:
        r = det(mal)
        if not r: err("detector: no ve el error tipico «%s»" % mal)
        vistos_err |= set(r)
    vistos_bm = set()
    for it in B.E_BIENMAL:
        if it["ok"] == 1:
            r = det(it["q"])
            if not r: err("detector: no ve la frase mala «%s»" % it["q"])
            vistos_bm |= set(r)
    for k in B.REQ:
        if k not in vistos_err: err("ningun error tipico de «En el examen» da el aviso " + k)
        if k not in vistos_bm: err("ninguna frase mala de ¿Bien o mal? da el aviso " + k)
    # Nada de lo que la ficha da por bueno puede dar NINGUN aviso (ni rojo ni ambar)
    buenos = [plain(p[s]["f"]) for p in B.PAREJAS for s in "ab"] + [plain(ej) for _, _, ej, _ in B.VISTAZO]
    buenos += [plain(B.DESPUES)] + [plain(e[k]) for e in B.ESPEJO for k in "cr"]
    buenos += [plain(s) for s in B.ES_QUE + B.ENTONCES_CONV] + [plain(B.ES_QUE_USTED)]
    buenos += [plain(s) for _, _, s in B.DONDE] + [plain(b) for _, b, _ in B.ERRORES]
    buenos += [i["q"] for i in B.E_BIENMAL if i["ok"] == 0] + [fill(i) for i in B.P_FLECHA + B.P_PORQUE]
    buenos += [filled(t["texto"]) for t in B.TEXTOS] + [plain(o["m"]) for o in B.ORAL] + [L["mensaje"] for L in B.LAMINAS]
    buenos += [a["txt"] for a in B.AL_FINAL]
    for b in buenos:
        r = det(b)
        if r: err("detector: aviso %s en un texto bueno: %r" % (r, b.strip()[:90]))
        if R_WORDS.search(norm(b)) and b not in [a["txt"] for a in B.AL_FINAL]: err("conector [R] en un texto bueno: %r" % b[:80])

# Node: el detector y las cuentas tienen que dar lo mismo en el navegador
NODE_OK = None
if not ERR and shutil.which("node"):
    def cuenta_py(t):
        n = norm(t); return {k: len(re.findall(r, n)) for k, r in B.CUENTA.items()}
    textos_c = [t for t, _ in B.DETECTOR_PRUEBAS] + [plain(o["m"]) for o in B.ORAL]
    js_t = ("var D=%s;function norm(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}"
            "function det(t){var o={},ss=(t.match(/[^.!?\\n]+[.!?]*/g)||[]).map(norm);D.d.forEach(function(d){var r=new RegExp(d.re);"
            "if(d.sc==='s'){if(ss.some(function(s){return r.test(s);}))o[d.id]=1;}else if(r.test(norm(t)))o[d.id]=1;});return Object.keys(o).sort();}"
            "function cnt(t){var n=norm(t),o={};Object.keys(D.c).forEach(function(k){o[k]=(n.match(new RegExp(D.c[k],'g'))||[]).length;});return o;}"
            "var bad=[];D.p.forEach(function(p){var ids=det(p[0]);if(ids.join()!==p[1].slice().sort().join())bad.push(p[0]+' -> '+ids.join());});"
            "D.t.forEach(function(x){var c=cnt(x[0]);Object.keys(c).forEach(function(k){if(c[k]!==x[1][k])bad.push('cuenta '+k+': '+x[0].slice(0,40));});});"
            "console.log(JSON.stringify(bad));") % json.dumps(
        {"d": [{"id": d["id"], "re": d["re"], "sc": d["sc"]} for d in B.DETECTOR], "p": B.DETECTOR_PRUEBAS, "c": B.CUENTA,
         "t": [[t, cuenta_py(t)] for t in textos_c]}, ensure_ascii=False)
    fd, path = tempfile.mkstemp(suffix=".js"); os.write(fd, js_t.encode("utf-8")); os.close(fd)
    try:
        out = subprocess.run(["node", path], capture_output=True, text=True, timeout=30)
        bad = json.loads(out.stdout or "null")
        if bad is None: err("node: no se ha podido probar el detector: " + out.stderr[:200])
        elif bad: err("detector en el navegador distinto de Python: " + "; ".join(bad))
        else: NODE_OK = True
    finally: os.unlink(path)

if ERR:
    print("\n".join("ERROR: " + e for e in ERR)); sys.exit(1)
for d in B.DETECTOR: d.pop("_rx", None)

# ------------------------------------------------------------------ HTML ESTATICO
def mk(s): return MARK.sub(lambda m: '<span class="k %s">%s</span>' % (m.group(1), m.group(2)), s)
INK = "#14161C"; MUT = "#5E5A55"
COL = {"o": ("#1D5FA8", "#E2ECF8"), "s": ("#2F7D4F", "#E3F1E8"), "g": ("#6B46C1", "#EEE8FA"), "c": ("#9A6412", "#FBF0DA"), "r": ("#C2451E", "#FCE6DC")}

def svg(vb, aria, inner, cls="dg"): return '<svg class="%s" viewBox="%s" role="img" aria-label="%s">%s</svg>' % (cls, vb, aria, inner)
def txt(x, y, s, size=16, col=INK, w="400", anchor="middle", extra=""):
    return '<text x="%s" y="%s" text-anchor="%s" font-size="%s" font-weight="%s" fill="%s"%s>%s</text>' % (x, y, anchor, size, w, col, extra, s)
def head(x, y, d, col, s=9):
    """Punta de flecha en (x, y) que mira hacia d = r / l / u / d."""
    if d == "r": pts = (x, y, x - s * 1.5, y - s, x - s * 1.5, y + s)
    elif d == "l": pts = (x, y, x + s * 1.5, y - s, x + s * 1.5, y + s)
    elif d == "u": pts = (x, y, x - s, y + s * 1.5, x + s, y + s * 1.5)
    else: pts = (x, y, x - s, y - s * 1.5, x + s, y - s * 1.5)
    return '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>' % (pts + (col,))
def wrap(s, n=17):
    out, cur = [], ""
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > n: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    if cur: out.append(cur)
    return out[:3]
def box(x, y, w, h, label, col, soft):
    o = '<rect x="%d" y="%d" width="%d" height="%d" rx="12" fill="%s" stroke="%s" stroke-width="2.5"/>' % (x, y, w, h, soft, col)
    ls = wrap(label); y0 = y + h / 2 - (len(ls) - 1) * 10.5 + 6
    for i, l in enumerate(ls): o += txt(x + w / 2, "%.1f" % (y0 + i * 21), l, 17, INK, "600")
    return o

def icon_svg(k):
    """Dibujo pequeno de cada flecha (tarjetas). 220 x 100."""
    c, s = COL[k]; o = ""
    if k == "o":
        o += '<line x1="20" y1="52" x2="196" y2="52" stroke="%s" stroke-width="4"/>' % c + head(208, 52, "r", c)
        for i, x in enumerate((48, 108, 168)):
            o += '<circle cx="%d" cy="52" r="15" fill="%s" stroke="%s" stroke-width="3"/>' % (x, s, c) + txt(x, 58, str(i + 1), 15, c, "700")
    elif k == "s":
        o += '<rect x="14" y="28" width="66" height="48" rx="10" fill="%s" stroke="%s" stroke-width="2.5"/>' % (s, c)
        o += '<rect x="140" y="28" width="66" height="48" rx="10" fill="%s" stroke="%s" stroke-width="2.5"/>' % (s, c)
        o += '<circle cx="110" cy="52" r="20" fill="%s"/>' % c + txt(110, 61, "+", 28, "#fff", "700")
    elif k == "g":
        o += '<path d="M14,78 L70,78 C120,78 104,24 150,24 L196,24" fill="none" stroke="%s" stroke-width="4"/>' % c + head(208, 24, "r", c)
    elif k == "c":
        o += '<rect x="8" y="30" width="62" height="44" rx="10" fill="%s" stroke="%s" stroke-width="2.5"/>' % (s, c)
        o += '<rect x="150" y="30" width="62" height="44" rx="10" fill="%s" stroke="%s" stroke-width="2.5"/>' % (s, c)
        o += '<line x1="148" y1="52" x2="86" y2="52" stroke="%s" stroke-width="4"/>' % c + head(74, 52, "l", c)
        o += txt(39, 92, "pasó", 12, MUT) + txt(181, 92, "causa", 12, MUT) + txt(110, 22, "¿por qué?", 13, c, "700")
    else:
        o += '<rect x="8" y="30" width="62" height="44" rx="10" fill="%s" stroke="%s" stroke-width="2.5"/>' % (s, c)
        o += '<rect x="150" y="30" width="62" height="44" rx="10" fill="%s" stroke="%s" stroke-width="2.5"/>' % (s, c)
        o += '<line x1="72" y1="52" x2="134" y2="52" stroke="%s" stroke-width="4"/>' % c + head(146, 52, "r", c)
        o += txt(39, 92, "causa", 12, MUT) + txt(181, 92, "pasa", 12, MUT) + txt(110, 22, "¿y qué pasa?", 13, c, "700")
    return svg("0 0 220 100", "Dibujo de la flecha: " + FAM[k]["dib"], o, "ic")

def pair_svg(k, x, y, word):
    """Dos cajas (en el orden de la frase) y la flecha entre ellas. 480 x 165 (estrecho para que la letra se lea en el movil)."""
    c, s = COL[k]; o = box(8, 38, 172, 84, x, c, s) + box(300, 38, 172, 84, y, c, s)
    if k == "o":
        o += '<line x1="184" y1="80" x2="284" y2="80" stroke="%s" stroke-width="4"/>' % c + head(296, 80, "r", c)
        o += '<circle cx="22" cy="38" r="14" fill="%s"/>' % c + txt(22, 43, "1", 14, "#fff", "700")
        o += '<circle cx="314" cy="38" r="14" fill="%s"/>' % c + txt(314, 43, "2", 14, "#fff", "700")
        lab = "primero una, después la otra"
    elif k == "s":
        o += '<line x1="184" y1="80" x2="296" y2="80" stroke="%s" stroke-width="3" stroke-dasharray="5 5"/>' % c
        o += '<circle cx="240" cy="80" r="22" fill="%s"/>' % c + txt(240, 90, "+", 30, "#fff", "700")
        lab = "las dos en la misma dirección"
    elif k == "g":
        o += '<path d="M184,100 C226,100 222,46 256,46 L284,46" fill="none" stroke="%s" stroke-width="4"/>' % c + head(296, 46, "r", c)
        lab = "la segunda va al revés"
    elif k == "c":
        o += '<line x1="296" y1="80" x2="196" y2="80" stroke="%s" stroke-width="4"/>' % c + head(184, 80, "l", c)
        o += txt(94, 146, "lo que pasó", 15, MUT) + txt(386, 146, "la causa", 15, c, "700")
        lab = "miras hacia atrás"
    else:
        o += '<line x1="184" y1="80" x2="284" y2="80" stroke="%s" stroke-width="4"/>' % c + head(296, 80, "r", c)
        o += txt(94, 146, "la causa", 15, c, "700") + txt(386, 146, "lo que pasa", 15, MUT)
        lab = "miras hacia delante"
    o += '<rect x="186" y="108" width="108" height="28" rx="14" fill="%s"/>' % c + txt(240, 127, word, 15, "#fff", "700")
    o += txt(240, 22, lab, 15, c, "700")
    return svg("0 0 480 165", "%s: %s %s %s" % (FAM[k]["dib"], x, word, y), o, "dg pr")

def linea_svg():
    c, s = COL["o"]; o = '<line x1="14" y1="58" x2="388" y2="58" stroke="%s" stroke-width="5"/>' % c + head(404, 58, "r", c, 11)
    xs = [52, 150, 250, 348]
    for i, (x, w) in enumerate(zip(xs, B.LINEA)):
        o += '<circle cx="%d" cy="58" r="19" fill="%s" stroke="%s" stroke-width="3"/>' % (x, s, c) + txt(x, 65, str(i + 1), 17, c, "700")
        for j, part in enumerate(w.split(" / ")): o += txt(x, 104 + j * 18, ("o " if j else "") + part, 16, INK, "700")
    o += txt(208, 20, "Cada hecho, en su sitio", 15, MUT)
    return svg("0 0 412 132", "La línea de pasos: primero, después o luego, más tarde, al final", o, "dg pr")

LEG = '<div class="legend">' + "".join('<span><span class="k %s">%s</span> %s</span>' % (k, FAM[k]["n"].lower(), FAM[k]["dib"]) for k in B.ORDEN_FAM) + '</div>'

def cards():
    o = '<div class="cams">'
    for k in B.ORDEN_FAM:
        f = FAM[k]
        o += '<div class="cam c%s">%s<h3>%s</h3><p class="qf">%s</p><p>%s</p></div>' % (k, icon_svg(k), f["n"], f["q"], f["txt"])
    return o + '</div>'

def vistazo():
    o = '<table class="t"><tr><th>Flecha</th><th>Palabras</th><th>Ejemplo</th><th>Para qué</th></tr>'
    for k, w, ej, d in B.VISTAZO:
        o += '<tr><td><span class="k %s">%s</span></td><td>%s</td><td>%s</td><td class="small">%s</td></tr>' % (k, FAM[k]["n"], w, mk(ej), d)
    return o + '</table>'

def losveras():
    o = '<table class="t"><tr><th>Palabra</th><th>Es como...</th><th>Ejemplo</th></tr>'
    for w, eq, ej in B.LOS_VERAS: o += '<tr><td><b>%s</b></td><td>%s</td><td><i>%s</i></td></tr>' % (w, eq, ej)
    return o + '</table>'

def alfinal():
    o = ""
    for a in B.AL_FINAL:
        t = a["txt"].replace("al final", "<b>al final</b>").replace("Al final", "<b>Al final</b>")
        o += '<div class="box"><span class="chip">%s</span><p style="margin:6px 0">%s</p><details><summary>%s</summary><p style="margin:0">%s</p></details></div>' % (a["tipo"], t, a["q"], a["a"])
    return o

def donde():
    return "".join('<div class="box"><span class="chip">%s</span><p class="small muted" style="margin:6px 0">%s</p><p style="margin:0">%s</p></div>' % (c, d, mk(s)) for c, d, s in B.DONDE)

def errores():
    o = '<div class="errs">'
    for mal, bien, why in B.ERRORES:
        o += '<div class="err"><div class="mal"><span aria-hidden="true">✗</span> <s>%s</s></div><div class="bien"><span aria-hidden="true">✓</span> %s</div><div class="small muted">%s</div></div>' % (mal, mk(bien), why)
    return o + '</div>'

def porque_tab():
    return '<table class="t"><tr><th>Forma</th><th>Cuándo</th><th>Ejemplo</th></tr>' + "".join(
        '<tr><td><b>%s</b></td><td>%s</td><td><i>%s</i></td></tr>' % r for r in B.POR_QUE) + '</table>'

CSS_R = CSS + r"""
:root{--co:#1D5FA8;--co-soft:#E2ECF8;--cs:#2F7D4F;--cs-soft:#E3F1E8;--cg:#6B46C1;--cg-soft:#EEE8FA;--cc:#9A6412;--cc-soft:#FBF0DA;--cr:#C2451E;--cr-soft:#FCE6DC}
.k{border-radius:4px;padding:0 3px 1px;border-bottom:3px solid;line-height:1.9}
.k.o{background:var(--co-soft);border-color:var(--co)}.k.s{background:var(--cs-soft);border-color:var(--cs)}.k.g{background:var(--cg-soft);border-color:var(--cg)}
.k.c{background:var(--cc-soft);border-color:var(--cc)}.k.r{background:var(--cr-soft);border-color:var(--cr)}
.cams{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:18px 0}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px 14px;border-top:6px solid var(--co)}
.cam.cs{border-top-color:var(--cs)}.cam.cg{border-top-color:var(--cg)}.cam.cc{border-top-color:var(--cc)}.cam.cr{border-top-color:var(--cr)}
.cam h3{margin:4px 0 2px}.cam p{margin:0;font-size:.95rem}.cam p.qf{color:var(--muted);font-style:italic;margin-bottom:6px}
svg.ic{width:100%;max-width:200px;height:auto;display:block}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.box h4{margin:0 0 4px}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
.lanes{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.lanes button{font:inherit;font-weight:700;border:3px solid var(--line);background:#fff;border-radius:10px;padding:10px 12px;cursor:pointer}
.lanes button.c.on{border-color:var(--cc);background:var(--cc-soft)}.lanes button.r.on{border-color:var(--cr);background:var(--cr-soft)}
.lanes button.y.on{border-color:var(--bad);background:var(--bad-soft)}.lanes button.f.on{border-color:var(--co);background:var(--co-soft)}
svg.dg{width:100%;height:auto;display:block;margin:6px 0}
.expl{border-radius:8px;padding:10px 14px;margin-top:6px;background:var(--paper)}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;margin:8px 0}
.res{font-family:Georgia,serif;font-size:1.25rem;font-weight:700;text-align:center;margin:8px 0;line-height:1.8}
.duo2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.stack{display:grid;gap:12px;margin:12px 0}
svg.pr{max-width:560px;margin:6px auto}
.half{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.half .res{font-size:1.08rem;text-align:left}
.story{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 16px;line-height:2}
.story .yy{background:var(--bad-soft);border-bottom:3px solid var(--bad);border-radius:4px;padding:0 3px}
.errs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.err{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.err .mal{color:var(--bad)}.err .bien{margin:4px 0}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.vchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px;background:var(--paper);color:var(--muted)}
.vchip.o{background:var(--co-soft);color:var(--co)}.vchip.s{background:var(--cs-soft);color:var(--cs)}.vchip.g{background:var(--cg-soft);color:var(--cg)}
.vchip.c{background:var(--cc-soft);color:var(--cc)}.vchip.r{background:var(--cr-soft);color:var(--cr)}
.blank{display:inline-block;min-width:64px;border-bottom:2px solid var(--ink);text-align:center}
.qz{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0}
.qz .cnt{font-size:.85rem;color:var(--muted)}
.qz .qq{font-size:1.05rem;margin:6px 0 10px}
.qz .ops{display:grid;gap:8px}
.qz .ops.bm{grid-template-columns:1fr 1fr}
.qz .ops button{font:inherit;text-align:left;font-weight:500;border:2px solid var(--line);background:#fff;border-radius:10px;padding:9px 12px;cursor:pointer}
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
.lam ul{margin:6px 0;padding-left:1.2em}.lam li{margin:3px 0}
textarea.wr{width:100%;min-height:220px;font:inherit;font-size:1.02rem;line-height:1.7;border:1.5px solid #CFC6BB;border-radius:8px;padding:12px 14px;background:#fff}
.rv{list-style:none;padding:0;margin:8px 0}
.rv li{border-radius:8px;padding:8px 12px;margin:6px 0;font-size:.95rem}
.rv li.r{background:var(--bad-soft)}.rv li.a{background:var(--amb-soft)}.rv li.g{background:var(--ok-soft)}
.rv mark{background:#FFE58A;border-radius:3px;padding:0 2px}
.cnts{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}
.cnts span{border-radius:999px;padding:3px 12px;font-size:.9rem;font-weight:600}
.check{list-style:none;padding:0;margin:8px 0}.check li{padding:5px 0}.check label{cursor:pointer}
.ocard{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin-top:12px}
.ocard .ph1{font-family:Georgia,serif;font-size:1.15rem;font-weight:700}
.sit{font-family:Georgia,serif;font-size:1.3rem;font-weight:700;margin:8px 0;line-height:1.35}
.hechos{counter-reset:h;list-style:none;padding:0;margin:8px 0;display:grid;gap:6px}
.hechos li{counter-increment:h;background:var(--paper);border-radius:8px;padding:6px 12px 6px 40px;position:relative}
.hechos li::before{content:counter(h);position:absolute;left:10px;top:6px;width:22px;height:22px;border-radius:50%;background:var(--co);color:#fff;font-weight:700;font-size:.8rem;display:grid;place-items:center}
.clock{font-family:Georgia,serif;font-size:1.6rem;font-weight:700;font-variant-numeric:tabular-nums}
.tbar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:8px 0}
.tbar i{display:block;height:100%;background:var(--coral);width:0;transition:width .25s linear}
.model{background:var(--paper);border-radius:8px;padding:10px 14px;margin-top:8px;line-height:1.9}
.famsel{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}
.famsel button{font:inherit;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.famsel button.on{font-weight:700}
.famsel button.o.on{border-color:var(--co);background:var(--co-soft)}.famsel button.s.on{border-color:var(--cs);background:var(--cs-soft)}
.famsel button.g.on{border-color:var(--cg);background:var(--cg-soft)}.famsel button.c.on{border-color:var(--cc);background:var(--cc-soft)}
.famsel button.r.on{border-color:var(--cr);background:var(--cr-soft)}
.scale{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.scale label{cursor:pointer}.scale input{position:absolute;opacity:0}
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
.hist{font-size:.88rem;color:var(--muted)}
#v-resumen{display:none}
@media (max-width:700px){.errs,.duo2,.lanes{grid-template-columns:1fr}.qz .ops.bm{grid-template-columns:1fr 1fr}table.t{font-size:.88rem}table.t td,table.t th{padding:6px 5px}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:13px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.err,.half{break-inside:avoid}}
"""

STEPS = [("flechas", "Las flechas"), ("orden", "Contar en orden"), ("porque", "Porque y por eso"), ("examen", "En el examen"),
         ("practica", "Practica"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_FLECHAS = """
<h2>Las flechas entre frases</h2>
<p class="lead">Un conector es una <b>flecha</b>: le dice al que lee hacia dónde va la frase siguiente. ¿Viene el paso siguiente? ¿Otra cosa del mismo lado? ¿Algo al revés? ¿La causa? ¿Lo que pasa por eso? Con cinco flechas tienes todo lo que necesitas para el A2.</p>
__CARDS__
__LEG__
<h3>Mira la diferencia</h3>
<p class="muted small">Casi las mismas palabras, otra flecha... y otro mensaje. Elige una pareja.</p>
<div class="pills" id="parsel"></div>
<div class="box" id="parvis" aria-live="polite"></div>
<h3>Las flechas en un vistazo</h3>
__VISTAZO__
<p>__ELEGIR__</p>
<details><summary>Los verás en los textos (no los necesitas para aprobar)</summary>
<p>En la lectura y en algunos ejemplos del curso salen estas palabras. Está bien entenderlas, pero para escribir y hablar en el A2 tienes bastante con las cinco flechas.</p>
__VERAS__</details>
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="orden">Siguiente: contar en orden</button></div>
"""

V_ORDEN = """
<h2>Contar en orden: la línea de pasos</h2>
<p class="lead">Cuando cuentas algo que pasó (un día, un viaje, la vida de una persona), los hechos van en fila. Las flechas de orden le dicen al que lee en qué paso está.</p>
__LINEA__
<h3>Solo con «y» o con flechas</h3>
<p>Es la misma historia. Pulsa los botones y mira la diferencia.</p>
<div class="lanes" id="stsel"><button class="y" data-act="story" data-k="y">Solo con «y»</button><button class="f" data-act="story" data-k="f">Con flechas</button></div>
<div class="story" id="stvis" aria-live="polite"></div>
<h3>Cuatro trucos</h3>
<ul>__TIPS__</ul>
<h3>«Al final»: el plan cambió</h3>
<p><b>Al final</b> cierra la fila, pero también te dice que <b>el plan cambió</b>: lo que pasó de verdad va detrás. En la lectura y la auditiva es una trampa típica, porque el plan que no pasó también sale en el texto. Lee y contesta antes de abrir la respuesta.</p>
__ALFINAL__
<div class="row"><button class="btn cta" data-go="porque">Siguiente: porque y por eso</button></div>
"""

V_PORQUE = """
<h2>Porque y por eso: el espejo</h2>
<p class="lead">Son los mismos dos hechos: una causa y lo que pasa. Solo cambia el orden en que los dices, y la flecha se da la vuelta.</p>
<div class="stack"><div class="half">__ESP_C__</div><div class="half">__ESP_R__</div></div>
<div class="tip">El truco: <b>porque</b> mira hacia atrás (detrás va la causa); <b>por eso</b> mira hacia delante (detrás va lo que pasa). Si dudas, pregúntate: ¿lo de detrás es el porqué o el resultado?</div>
<h3>Dale la vuelta</h3>
<p class="muted small">Elige dos hechos y decide por dónde empiezas.</p>
<div class="pills" id="essel"></div>
<div class="lanes" id="esdir"><button class="c" data-act="esdir" data-k="c">Empiezo por lo que pasó: porque</button><button class="r" data-act="esdir" data-k="r">Empiezo por la causa: por eso</button></div>
<div class="box" id="esvis" aria-live="polite"></div>
<h3>«Es que»: la excusa de los amigos</h3>
<p><b>Es que</b> también mira hacia atrás, pero es de la conversación: sirve para explicar un «no» o un problema a alguien cercano. Va al principio de la explicación.</p>
<ul>__ESQUE__</ul>
<div class="note">En un correo <b>de usted</b>, mejor <b>porque</b>: __ESQUEU__</div>
<h3>«Entonces» en la conversación</h3>
<p>En un diálogo, <b>entonces</b> mira hacia delante, como <b>por eso</b>: propones algo por lo que te acaban de decir. Es perfecto para la tarea 3 de la oral.</p>
<ul>__ENTONCES__</ul>
<h3>¿Por qué? / Porque</h3>
__PORQUE__
<div class="row"><button class="btn cta" data-go="examen">Siguiente: en el examen</button></div>
"""

V_EXAMEN = """
<h2>Dónde sale en el examen</h2>
<p class="lead">Las flechas no son solo un adorno: en la escritura y en la oral hacen que tu texto se entienda y se siga bien, y en la lectura y la auditiva te avisan de dónde está la respuesta.</p>
__LEG__
__DONDE__
<div class="note">__ORO__</div>
<h3>Los errores más típicos</h3>
<p>Tienes que reconocerlos en tus textos y en tu oral. Mira por qué fallan.</p>
__ERRORES__
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACT = """
<h2>Practica</h2>
<p class="lead">Cuatro ejercicios. Cada respuesta se corrige en el momento, con la explicación.</p>
<div class="pills" id="exsel">
 <button class="pill on" data-act="ex" data-k="p1">1. ¿Qué flecha?</button>
 <button class="pill" data-act="ex" data-k="p2">2. ¿Porque o por eso?</button>
 <button class="pill" data-act="ex" data-k="e2">3. Textos del examen</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Ahora úsalo en una tarea del examen: escribe un texto o cuenta una historia en voz alta con flechas.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="o">Oral: cuéntalo en orden</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu texto y después pulsa <b>Revisar mis flechas</b>: la página cuenta tus flechas y te avisa de los errores típicos. No corrige el texto entero: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="ato" hidden>
 <p>Vas a ver cuatro hechos en palabras clave, como tus notas del examen. Cuéntalos <b>en voz alta</b> como una historia en pasado, con <b>al menos tres flechas distintas</b>. El reloj pasa solo.</p>
 <div id="obox"></div>
</div>
<div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button></div>
"""

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan a mejorarlo. Al final, copia todo (también tus textos y resultados) y envíamelo.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué parte te ha ayudado más?</label>
 <div class="chips" role="group" aria-labelledby="o1l">
  <label><input type="radio" name="o1" value="Las flechas">Las flechas</label>
  <label><input type="radio" name="o1" value="Contar en orden">Contar en orden</label>
  <label><input type="radio" name="o1" value="El espejo porque / por eso">El espejo porque / por eso</label>
  <label><input type="radio" name="o1" value="En el examen y los errores típicos">En el examen y los errores típicos</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tú">Ahora tú</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué te cuesta más ahora?</label>
 <div class="chips" role="group" aria-labelledby="o2l">
  <label><input type="radio" name="o2" value="No escribir todo con y">No escribir todo con «y»</label>
  <label><input type="radio" name="o2" value="Ordenar sin repetir después">Ordenar sin repetir «después»</label>
  <label><input type="radio" name="o2" value="Porque y por eso">Porque y por eso</label>
  <label><input type="radio" name="o2" value="Pero y además">Pero y además</label>
  <label><input type="radio" name="o2" value="Es que y entonces">Es que y entonces</label>
 </div>
 <label class="q" id="o3l">3. ¿Te ayuda la idea de «las flechas entre frases»?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con los conectores? (1 = nada, 10 = total)</label>
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

ESP0 = B.PAREJAS[0]
def resumen():
    o = '<h2>Conectores: las flechas entre frases · resumen</h2>' + cards() + LEG
    o += '<h3>Las flechas en un vistazo</h3>' + vistazo() + '<p>' + B.ELEGIR + '</p>'
    o += '<h3>La línea de pasos</h3>' + linea_svg()
    o += '<h3>El espejo: porque y por eso</h3>' + '<div class="stack"><div class="half">%s</div><div class="half">%s</div></div>' % (
        pair_svg("c", ESP0["a"]["x"], ESP0["a"]["y"], "porque"), pair_svg("r", ESP0["b"]["x"], ESP0["b"]["y"], "por eso"))
    o += '<h3>Los errores típicos</h3>' + errores()
    return o

views = {
    "flechas": V_FLECHAS.replace("__CARDS__", cards()).replace("__LEG__", LEG).replace("__VISTAZO__", vistazo()).replace("__ELEGIR__", B.ELEGIR).replace("__VERAS__", losveras()),
    "orden": V_ORDEN.replace("__LINEA__", linea_svg()).replace("__TIPS__", "".join("<li>%s</li>" % t for t in B.ORDEN_TIPS)).replace("__ALFINAL__", alfinal()),
    "porque": V_PORQUE.replace("__ESP_C__", '<p class="res">%s</p>%s' % (mk(ESP0["a"]["f"]), pair_svg("c", ESP0["a"]["x"], ESP0["a"]["y"], "porque")))
                      .replace("__ESP_R__", '<p class="res">%s</p>%s' % (mk(ESP0["b"]["f"]), pair_svg("r", ESP0["b"]["x"], ESP0["b"]["y"], "por eso")))
                      .replace("__ESQUE__", "".join("<li>%s</li>" % mk(s) for s in B.ES_QUE)).replace("__ESQUEU__", "<i>%s</i>" % mk(B.ES_QUE_USTED))
                      .replace("__ENTONCES__", "".join("<li>%s</li>" % mk(s) for s in B.ENTONCES_CONV)).replace("__PORQUE__", porque_tab()),
    "examen": V_EXAMEN.replace("__LEG__", LEG).replace("__DONDE__", donde()).replace("__ORO__", B.REGLA_ORO).replace("__ERRORES__", errores()),
    "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R08</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
""".replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

# ------------------------------------------------------------------ DATOS PARA EL SCRIPT
def side(d, k):
    w = [x for kk, x in MARK.findall(d["f"]) if kk == d["fam"]][0]
    return {"f": mk(d["f"]), "svg": pair_svg(d["fam"], d["x"], d["y"], low(w))}
ANTES_HTML = re.sub(r"\by\b", '<span class="yy">y</span>', B.ANTES)
DATA = {
    "key": STORAGE, "title": TITLE,
    "steps": [{"id": k, "label": l} for k, l in STEPS],
    "fams": {k: FAM[k]["n"] for k in B.ORDEN_FAM}, "order": B.ORDEN_FAM,
    "motivos": {k: {"f": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "parejas": [{"tema": p["tema"], "a": side(p["a"], "a"), "b": side(p["b"], "b"), "expl": p["expl"]} for p in B.PAREJAS],
    "story": {"y": ANTES_HTML, "f": mk(B.DESPUES), "ny": len(re.findall(r"\by\b", B.ANTES)), "nf": len(MARK.findall(B.DESPUES))},
    "espejo": [{"tema": e["tema"], "c": mk(e["c"]), "r": mk(e["r"]), "csvg": pair_svg("c", e["b"], e["a"], "porque"),
                "rsvg": pair_svg("r", e["a"], e["b"], "por eso")} for e in B.ESPEJO],
    "qz": {
        "p1": {"items": B.P_FLECHA, "n": 8, "name": "¿Qué flecha?", "info": "Lee la frase entera y pregúntate hacia dónde va la segunda parte: ¿orden, suma, giro, causa o lo que pasa?"},
        "p2": {"items": B.P_PORQUE, "n": 8, "name": "¿Porque o por eso?", "info": "¿Lo que va detrás es la causa (porque) o lo que pasa (por eso)?"},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Errores típicos de los exámenes. ¿La frase está bien o la flecha falla?"},
    },
    "textos": B.TEXTOS,
    "laminas": B.LAMINAS, "focos": B.FOCOS, "focofam": B.FOCO_FAM, "cuenta": B.CUENTA, "detector": B.DETECTOR,
    "oral": [{"tema": o["tema"], "hechos": o["hechos"], "m": mk(o["m"])} for o in B.ORAL],
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function blank(){ return {cur:'flechas', seen:{}, par:0, st:'y', es:0, esd:'c', ex:'p1', etext:D.textos[0].id, at:'w',
  qz:{}, qlog:{}, cz:{}, w:{}, wchk:{}, wrev:{}, lam:D.laminas[0].id, oc:{n:4,t:45}, ro:null, olog:[],
  o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }

/* ---------------- navegacion ---------------- */
function stepDone(id){
 if(id==='practica') return ['p1','p2','e4'].some(function(k){ return !!S.qlog[k]; }) || Object.keys(S.cz).length>0;
 if(id==='ahora') return Object.keys(S.w).some(function(k){ return (S.w[k]||'').trim().length>20; }) || S.olog.length>0;
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
 stopTimer(); nav(); if(id==='ahora') renderAt(); window.scrollTo(0,0);
}

/* ---------------- 1. las flechas: parejas ---------------- */
function renderPar(){
 var o=''; D.parejas.forEach(function(p,i){ o+='<button class="pill'+(S.par===i?' on':'')+'" data-act="par" data-i="'+i+'">'+esc(p.tema)+'</button>'; });
 $('parsel').innerHTML=o;
 var p=D.parejas[S.par];
 $('parvis').innerHTML='<div class="stack"><div class="half"><p class="res">'+p.a.f+'</p>'+p.a.svg+'</div><div class="half"><p class="res">'+p.b.f+'</p>'+p.b.svg+'</div></div><div class="expl">'+p.expl+'</div>';
}
/* ---------------- 2. contar en orden ---------------- */
function renderStory(){
 var bs=$('stsel').querySelectorAll('button'); for(var i=0;i<bs.length;i++){ var on=bs[i].getAttribute('data-k')===S.st; bs[i].classList.toggle('on',on); bs[i].setAttribute('aria-pressed',on); }
 $('stvis').innerHTML = S.st==='y'
  ? '<p style="margin:0">'+D.story.y+'</p><p class="small muted" style="margin:8px 0 0">'+D.story.ny+' veces «y» y ninguna flecha: es difícil saber en qué paso estás.</p>'
  : '<p style="margin:0">'+D.story.f+'</p><p class="small muted" style="margin:8px 0 0">'+D.story.nf+' flechas, de las cinco familias. Las mismas cosas, pero ahora se siguen sin esfuerzo.</p>';
}
/* ---------------- 3. el espejo ---------------- */
function renderEsp(){
 var o=''; D.espejo.forEach(function(e,i){ o+='<button class="pill'+(S.es===i?' on':'')+'" data-act="es" data-i="'+i+'">'+esc(e.tema)+'</button>'; });
 $('essel').innerHTML=o;
 var bs=$('esdir').querySelectorAll('button'); for(var i=0;i<bs.length;i++){ var on=bs[i].getAttribute('data-k')===S.esd; bs[i].classList.toggle('on',on); bs[i].setAttribute('aria-pressed',on); }
 var e=D.espejo[S.es], c=S.esd==='c';
 $('esvis').innerHTML='<p class="res">'+(c?e.c:e.r)+'</p>'+(c?e.csvg:e.rsvg)+'<div class="expl">'+(c?'Empiezas por lo que pasó y miras hacia atrás: detrás de <b>porque</b> va la causa.':'Empiezas por la causa y miras hacia delante: detrás de <b>por eso</b> va lo que pasa.')+' Pulsa el otro botón: los mismos hechos, la flecha al revés.</div>';
}

/* ---------------- motor de opcion multiple ---------------- */
function qzNew(k){ var c=D.qz[k]; S.qz[k]={order:shuffle(range(c.items.length)).slice(0,c.n), i:0, res:[], perm:{}}; save(); }
function qHead(k, it){ if(k==='e4') return esc(it.q); return esc(it.q).replace('____','<span class="blank">____</span>'); }
function qzRender(k, box){
 var c=D.qz[k]; if(!S.qz[k]) qzNew(k);
 var st=S.qz[k], N=st.order.length;
 if(st.i>=N){
  var ok=st.res.filter(function(r){return r.ok;}).length, fails=st.res.filter(function(r){return !r.ok;});
  var msg = ok>=N-1 ? '¡Muy bien! Tus flechas apuntan bien.' : (ok>=Math.ceil(N*0.6) ? 'Bien. Mira otra vez las explicaciones de las que has fallado.' : 'Vuelve a mirar las cinco flechas y el espejo, y repite con otras frases.');
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
 o+='<div class="qq">'+qHead(k,it)+'</div><div class="ops'+(c.bm?' bm':'')+'" role="group">';
 opts.forEach(function(op){
  var cls=''; if(ans){ if(op[0]===ok) cls='good'; else if(op[0]===ans.pick) cls='bad'; }
  o+='<button type="button" data-act="qa" data-k="'+k+'" data-o="'+op[0]+'" class="'+cls+'"'+(ans?' disabled':'')+'>'+esc(op[1])+'</button>';
 });
 o+='</div>';
 if(ans){
  var full = c.bm ? '' : '<br><i>'+esc(it.q).replace('____','<b>'+esc(it.o[0])+'</b>')+'</i>';
  o+='<div class="fb '+(ans.ok?'good':'bad')+'" role="status"><b>'+(ans.ok?'¡Bien!':'No.')+'</b> '+(c.bm&&it.ok?'Corrección: '+it.fix+'<br>':'')+it.why+full+'</div>';
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
function seeded(arr, seed){ var h=0; for(var i=0;i<seed.length;i++) h=(h*31+seed.charCodeAt(i))>>>0; var a=arr.slice(); for(var j=a.length-1;j>0;j--){ h=(Math.imul(h,1103515245)+12345)>>>0; var r=(h>>>16)%(j+1); var t=a[j]; a[j]=a[r]; a[r]=t; } return a; }
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
  var mo=D.motivos[g.m], fn=D.fams[mo.f];
  if(c.cur===g.ok) o+='<li class="ok">'+g.n+'. ✓ <b>'+esc(g.ok)+'</b> · <span class="vchip '+mo.f+'">'+fn+'</span> '+mo.w+'</li>';
  else o+='<li class="no">'+g.n+'. ✗ <b>'+esc(c.cur)+'</b> no va aquí. Pista: <span class="vchip '+mo.f+'">'+fn+'</span> '+mo.w+' Prueba otra vez.</li>';
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
var EXINFO={e2:'Un correo, un blog, una biografía y un diálogo de la tarea 3. Elige la flecha de cada hueco: la corrección sale enseguida, con el motivo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
var CH=['Mis hechos van en orden: primero, después / luego, más tarde, al final.','No hay frases con tres «y»: he cambiado alguna por una flecha.','Detrás de porque va la causa; detrás de por eso, lo que pasa.','Además suma del mismo lado; si la frase gira, he puesto pero.','He usado al menos tres flechas distintas.'];
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+'</div>';
 h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(f){ return '<span class="vchip '+D.focofam[f]+'">'+D.focos[f]+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas te dicen qué flecha te va a ayudar en cada pauta. Recuerda: unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu texto</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar mis flechas</button></div><div id="rvbox" aria-live="polite"></div>';
 h+='<h3>Mi lista de las flechas</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
function sents(t){ return t.match(/[^.!?\n]+[.!?]*/g)||[]; }
function detIds(t){ var o={}, ss=sents(t).map(norm); D.detector.forEach(function(d){ var r=new RegExp(d.re); if(d.sc==='s'){ if(ss.some(function(s){ return r.test(s); })) o[d.id]=1; } else if(r.test(norm(t))) o[d.id]=1; }); return Object.keys(o).sort(); }
function cuenta(t){ var n=norm(t), o={}; D.order.forEach(function(k){ o[k]=(n.match(new RegExp(D.cuenta[k],'g'))||[]).length; }); o.y=(n.match(/\by\b/g)||[]).length; return o; }
window.__R08detect = detIds; window.__R08cuenta = cuenta;
function review(){
 var L=lam(), txt=$('wtext').value, out=[], red=0, amb=0;
 if(txt.trim().length<20){ $('rvbox').innerHTML='<ul class="rv"><li class="a">Escribe primero tu texto.</li></ul>'; return; }
 // 1. frase a frase
 sents(txt).forEach(function(s){
  if(!s.trim()) return; var n=norm(s);
  D.detector.forEach(function(d){
   if(d.sc!=='s') return; var m=new RegExp(d.re).exec(n); if(!m) return;
   if(d.t==='r') red++; else amb++;
   var hl=esc(s.slice(0,m.index))+'<mark>'+esc(s.substr(m.index,m[0].length))+'</mark>'+esc(s.slice(m.index+m[0].length));
   out.push('<li class="'+d.t+'">'+(d.t==='r'?'<b>¡Ojo!</b> ':'<b>Mira esto:</b> ')+d.msg+'<br><span class="small">'+hl+'</span></li>');
  });
 });
 // 2. el texto entero
 D.detector.forEach(function(d){
  if(d.sc!=='x' || !new RegExp(d.re).test(norm(txt))) return;
  if(d.t==='r') red++; else amb++;
  out.push('<li class="'+d.t+'">'+(d.t==='r'?'<b>¡Ojo!</b> ':'<b>Mira esto:</b> ')+d.msg+'</li>');
 });
 // 3. las flechas: cuantas y de que tipo
 var c=cuenta(txt), wc=txt.trim().split(/\s+/).length, kinds=D.order.filter(function(k){ return c[k]>0; });
 if(wc>=40 && kinds.length<3){ amb++; out.push('<li class="a"><b>Mira esto:</b> solo usas '+kinds.length+' tipo'+(kinds.length===1?'':'s')+' de flecha. Para un texto de examen, intenta al menos <b>tres</b> distintas.</li>'); }
 L.pautas.forEach(function(p,i){ p[1].forEach(function(f){ var k=D.focofam[f]; if(!c[k]){ amb++; out.push('<li class="a"><b>Mira esto:</b> la pauta '+(i+1)+' («'+esc(p[0].replace(/;$|\.$/,''))+'») va bien con una flecha de <b>'+D.fams[k].toLowerCase()+'</b>, y no veo ninguna.</li>'); } }); });
 if(!red && !amb) out.unshift('<li class="g">No he encontrado errores típicos y usas '+kinds.length+' flechas distintas. ¡Bien! Mira tú también la lista de abajo.</li>');
 else if(!red) out.unshift('<li class="g">No he encontrado errores seguros. Mira los puntos ámbar: son cosas que conviene comprobar.</li>');
 var cn='<div class="cnts">'+D.order.map(function(k){ return '<span class="vchip '+k+'">'+D.fams[k]+': '+c[k]+'</span>'; }).join('')+'<span class="vchip">y: '+c.y+'</span></div>';
 S.wrev[L.id]={red:red, amb:amb, kinds:kinds.length, cnt:D.order.map(function(k){ return D.fams[k]+' '+c[k]; }).join(', ')+', y '+c.y, words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul><p class="small"><b>Tus flechas</b> ('+kinds.length+' de 5 tipos):</p>'+cn+'<p class="muted small">Tu texto: '+wc+' palabras (la lámina pide '+L.palabras[0]+'-'+L.palabras[1]+'). La página no lo ve todo: tu profesora corrige el texto completo.</p>';
}

/* ---------------- relojes ---------------- */
var TM=null;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } }
function clockTxt(s){ s=Math.max(0,Math.ceil(s)); return Math.floor(s/60)+':'+(s%60<10?'0':'')+(s%60); }

/* ---------------- ahora tu: oral, cuentalo en orden ---------------- */
function oNew(){ S.ro={deck:shuffle(range(D.oral.length)).slice(0,S.oc.n), i:0, ph:0, res:[], pick:{}}; save(); }
function renderO(){
 var box=$('obox'), R=S.ro, h='';
 if(!R){
  h+='<div class="ocard"><div class="ph1">Prepárate</div><p>En cada tarjeta ves una historia en cuatro hechos. Mírala un momento, pulsa el reloj y cuéntala en voz alta, en pasado. Al final, compara con el modelo y marca las flechas que has usado.</p>';
  h+='<p class="small"><b>Tarjetas:</b></p><div class="pills">'+[3,4,6].map(function(n){ return '<button class="pill'+(S.oc.n===n?' on':'')+'" data-act="on" data-n="'+n+'">'+n+'</button>'; }).join('')+'</div>';
  h+='<p class="small"><b>Tiempo para cada historia:</b></p><div class="pills">'+[30,45,60].map(function(t){ return '<button class="pill'+(S.oc.t===t?' on':'')+'" data-act="ot" data-t="'+t+'">'+t+' s</button>'; }).join('')+'</div>';
  h+='<div class="row"><button class="btn cta" data-act="ostart">Empezar</button></div>';
  if(S.olog.length){ h+='<p class="hist"><b>Tus últimas prácticas:</b> '+S.olog.map(function(r){ return r.d+': '+r.ok+'/'+r.n+' con 3 flechas o más ('+r.t+' s)'; }).join(' · ')+'</p>'; }
  box.innerHTML=h+'</div>'; return;
 }
 var N=R.deck.length;
 if(R.i>=N){
  var ok=R.res.filter(function(r){ return r.ok; }).length;
  h+='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+(ok>=N-1?'¡Muy bien! Tus historias tienen flechas variadas.':'Vuelve a mirar las cinco flechas y repite: la próxima vez, piensa antes en una flecha para cada hecho.')+'</p>';
  var fl=R.res.filter(function(r){ return !r.ok; });
  if(fl.length){ h+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fl.forEach(function(r){ var o=D.oral[r.k]; h+='<li><b>'+esc(o.tema)+'</b><br>'+o.m+'</li>'; }); h+='</ul>'; }
  h+='<div class="row"><button class="btn cta" data-act="oagain">Otra vez</button></div></div>';
  box.innerHTML=h; return;
 }
 var o=D.oral[R.deck[R.i]];
 h+='<div class="ocard"><div class="cnt small muted">Tarjeta '+(R.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(R.i/N*100)+'%"></i></div>';
 h+='<div class="sit">'+esc(o.tema)+'</div><ol class="hechos">'+o.hechos.map(function(x){ return '<li>'+esc(x)+'</li>'; }).join('')+'</ol>';
 if(R.ph===0){
  h+='<p class="small muted">Piensa: ¿con qué flecha empiezas?, ¿dónde hay una causa?, ¿algo gira?</p><div class="row"><button class="btn cta" data-act="ogo">Empezar con el reloj</button></div>';
 } else if(R.ph===1){
  h+='<div class="clock" id="oclk">'+clockTxt(S.oc.t)+'</div><div class="tbar"><i id="obar"></i></div>';
  h+='<div class="row"><button class="btn cta" data-act="oskip">Ya está</button></div>';
 } else {
  h+='<div class="model"><b>Una historia modelo</b><br>'+o.m+'</div>';
  h+='<p class="small" style="margin-top:12px"><b>¿Qué flechas has usado tú?</b> (toca las que has dicho)</p><div class="famsel">';
  D.order.forEach(function(k){ var on=!!(R.pick&&R.pick[k]); h+='<button type="button" class="'+k+(on?' on':'')+'" data-act="ofam" data-k="'+k+'" aria-pressed="'+on+'">'+D.fams[k]+'</button>'; });
  h+='</div><div class="row"><button class="btn cta" data-act="oeval">Guardar y seguir</button></div>';
 }
 box.innerHTML=h+'</div>';
}
function oRun(){
 stopTimer(); var R=S.ro; if(!R || R.ph!==1) return;
 renderO();
 var T0=Date.now(), dur=S.oc.t;
 TM=setInterval(function(){
  var t=(Date.now()-T0)/1000, bar=$('obar'), ck=$('oclk'); if(!bar){ stopTimer(); return; }
  ck.textContent=clockTxt(dur-t); bar.style.width=Math.min(100,t/dur*100)+'%';
  if(t>=dur) oNext();
 }, 200);
}
function oNext(){ stopTimer(); var R=S.ro; R.ph=2; R.pick={}; save(); renderO(); }

/* ---------------- opinion y copiar ---------------- */
function renderOpn(){
 var o=''; for(var i=1;i<=10;i++) o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>';
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked=r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function pack(){
 var L=['CURSO DELE A2 - R08: CONECTORES','Nombre: '+(S.name||'-'),''];
 L.push('EJERCICIOS (ultimo resultado)');
 ['p1','p2','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 D.textos.forEach(function(t){
  var f=fbList(t.id,t.texto), errs=[];
  gapInfo(t.id,t.texto).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); });
  var started=Object.keys(S.cz).some(function(k){return k.indexOf(t.id+'-')===0;});
  L.push('- Textos del examen, '+t.titulo+': '+(started?f.first+'/'+f.tot+' a la primera'+(f.done<f.tot?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 L.push('','ORAL: CUENTALO EN ORDEN');
 if(!S.olog.length) L.push('sin hacer');
 S.olog.forEach(function(r){ L.push('- '+r.d+': '+r.ok+'/'+r.n+' historias con 3 flechas o mas (autoevaluacion), '+r.t+' s'+(r.det&&r.det.length?' | '+r.det.join(' / '):'')); });
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' ('+l.palabras[0]+'-'+l.palabras[1]+' palabras)','Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision: '+rv.red+' avisos rojos, '+rv.amb+' ambar | flechas: '+rv.kinds+' tipos ('+rv.cnt+') | '+rv.words+' palabras');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. Lo que mas cuesta: '+(S.o2||'-'),'3. Las flechas entre frases: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}
window.__R08pack = pack;

/* ---------------- eventos ---------------- */
var ACTS={
 par:function(b){ S.par=+b.getAttribute('data-i'); save(); renderPar(); },
 story:function(b){ S.st=b.getAttribute('data-k'); save(); renderStory(); },
 es:function(b){ S.es=+b.getAttribute('data-i'); save(); renderEsp(); },
 esdir:function(b){ S.esd=b.getAttribute('data-k'); save(); renderEsp(); },
 ex:function(b){ S.ex=b.getAttribute('data-k'); save(); renderEx(); },
 etext:function(b){ S.etext=b.getAttribute('data-id'); save(); renderE2(); },
 qa:function(b){ var k=b.getAttribute('data-k'); qzAnswer(k, +b.getAttribute('data-o')); qzRender(k, $('exbox')); nav(); var f=$('exbox').querySelector('.fb'); if(f&&f.scrollIntoView) f.scrollIntoView({block:'nearest'}); },
 qnext:function(b){ var k=b.getAttribute('data-k'); S.qz[k].i++; save(); qzRender(k, $('exbox')); },
 qrep:function(b){ var k=b.getAttribute('data-k'); qzNew(k); qzRender(k, $('exbox')); },
 czreset:function(b){ b.getAttribute('data-ids').split(',').forEach(function(id){ Object.keys(S.cz).forEach(function(g){ if(g.indexOf(id+'-')===0) delete S.cz[g]; }); }); save(); renderEx(); nav(); },
 at:function(b){ S.at=b.getAttribute('data-k'); save(); renderAt(); },
 lam:function(b){ S.lam=b.getAttribute('data-id'); save(); renderLam(); },
 review:function(){ review(); nav(); },
 on:function(b){ S.oc.n=+b.getAttribute('data-n'); save(); renderO(); },
 ot:function(b){ S.oc.t=+b.getAttribute('data-t'); save(); renderO(); },
 ostart:function(){ oNew(); renderO(); },
 ogo:function(){ S.ro.ph=1; save(); oRun(); },
 oskip:function(){ oNext(); },
 ofam:function(b){ var R=S.ro, k=b.getAttribute('data-k'); R.pick=R.pick||{}; R.pick[k]=!R.pick[k]; save(); renderO(); },
 oeval:function(){
  var R=S.ro, n=Object.keys(R.pick||{}).filter(function(k){ return R.pick[k]; }).length;
  R.res.push({k:R.deck[R.i], ok:n>=3, n:n}); R.i++; R.ph=0; R.pick={}; save();
  if(R.i>=R.deck.length){
   var ok=R.res.filter(function(r){return r.ok;}).length, d=new Date();
   S.olog.push({d:d.getDate()+'/'+(d.getMonth()+1), n:R.deck.length, t:S.oc.t, ok:ok, det:R.res.map(function(r){ return D.oral[r.k].tema+': '+r.n+' flechas'; })});
   if(S.olog.length>6) S.olog=S.olog.slice(-6);
   save(); nav();
  }
  renderO();
 },
 oagain:function(){ stopTimer(); S.ro=null; save(); renderO(); },
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
 if(S.ro && S.ro.ph===1) S.ro.ph=0;
 if(S.at==='w') renderLam(); else renderO();
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

renderPar(); renderStory(); renderEsp(); renderEx(); renderAt(); renderOpn(); go(S.cur);
})();
"""

# La opcion buena de los huecos no puede caer siempre en el mismo sitio del desplegable (con la funcion real).
POS_TXT = "sin probar"
if shutil.which("node"):
    src = re.search(r"function seeded\(.*", JS).group(0)
    gids = [(t["id"] + "-" + str(n + 1), g.split("#")[0].split("|")) for t in B.TEXTOS for n, g in enumerate(GAP.findall(t["texto"]))]
    fd, path = tempfile.mkstemp(suffix=".js")
    os.write(fd, (src + "\nvar G=%s, c=[0,0,0]; G.forEach(function(g){ c[seeded(g[1], g[0]).indexOf(g[1][0])]++; }); console.log(JSON.stringify(c));" % json.dumps(gids)).encode("utf-8")); os.close(fd)
    try: pos = json.loads(subprocess.run(["node", path], capture_output=True, text=True, timeout=30).stdout)
    finally: os.unlink(path)
    if min(pos) < len(gids) // 6:
        print("ERROR: la opcion buena de los huecos casi siempre cae en el mismo sitio:", pos); sys.exit(1)
    POS_TXT = "/".join(map(str, pos))

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
html = page(TITLE + " · Preparación DELE A2", CSS_R, BODY, js)
html.encode("ascii")
open(FILE, "w", encoding="ascii").write(html)
print("ok", FILE, "| huecos:", sum(ngaps.values()),
      "| items:", len(B.P_FLECHA) + len(B.P_PORQUE) + len(B.E_BIENMAL),
      "| pruebas del detector:", len(B.DETECTOR_PRUEBAS), "(navegador: %s)" % ("igual que Python" if NODE_OK else "sin probar"),
      "| buena en el desplegable (1a/2a/3a):", POS_TXT, "| parejas:", len(B.PAREJAS), "| tarjetas orales:", len(B.ORAL))
