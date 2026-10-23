# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R13 DEL CURSO DE PREPARACION DELE A2: LAS FUNCIONES DE LOS CORREOS
# Uso: python3 build_R13_funciones.py  -> DELEA2_curso_R13_formulas_correo.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# Contenidos: solo en banco_R13_funciones.py. Este archivo monta la pagina y comprueba el banco.
# Mismo formato y motor que R01-R08: pestanas, correccion inmediata, huecos con motivo (barajado arreglado),
# "Ahora tu" con escritura (detector de funciones y errores) y oral (responde rapido, con reloj), Tu opinion y Copiar.
# Sin imagenes: todos los dibujos son SVG.
# Enfoque cognitivo: ATRAS, ADELANTE Y CONTESTAR + EL MOLDE DE TRES PIEZAS (formula + dato + detalle), con tu y usted.
import json, os, re, shutil, subprocess, sys, tempfile, unicodedata
from curso_comun import CSS, EMAIL, page
import banco_R13_funciones as B

TITLE = "Las funciones de los correos"
FILE = "DELEA2_curso_R13_formulas_correo.html"
STORAGE = "dele-a2-curso-R13"

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
MARK = re.compile(r"\[(f|d|x|p):([^\[\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
FN = {f["id"]: f for f in B.FUNCIONES}
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
def plain(s): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", MARK.sub(lambda m: m.group(2), s))).strip()
def filled(s): return GAP.sub(lambda m: m.group(1).split("#")[0].split("|")[0], s)
RX_F = {k: re.compile(v) for k, v in B.FUNC_RX.items()}
RX_TU = re.compile(B.TU_RX); RX_US = re.compile(B.US_RX); RX_B1 = re.compile(B.B1_RX)
def has_f(txt, f): return bool(RX_F[f].search(norm(txt)))
def lane_ok(txt, t, where):
    n = norm(txt)
    other = RX_US if t == "tu" else RX_TU
    m = other.search(n)
    if m: err("%s: palabra del otro carril («%s») en un texto de %s: %s" % (where, m.group(0), B.CARRIL[t], txt[:80]))

def chk_marks(s, where, need="fdx"):
    rest = MARK.sub("", s)
    if "[" in rest or "]" in rest: err("marca mal cerrada en %s: %s" % (where, s[:80]))
    ks = [k for k, _ in MARK.findall(s)]
    for k in need:
        if k not in ks: err("%s: falta la pieza %s (%s)" % (where, k, B.PIEZAS[k][0]))
    if ks[:1] != ["f"]: err("%s: la frase empieza por la formula [f:]" % where)
    return ks

def chk_frase(s, f, t, where, need="fdx"):
    chk_marks(s, where, need)
    p = plain(s)
    if not has_f(p, f): err("%s: la frase no lleva ninguna formula de «%s»: %s" % (where, FN[f]["n"], p))
    lane_ok(p, t, where)

if set(FN) != set(B.FUNC_RX): err("FUNCIONES y FUNC_RX no coinciden")
if len(B.FUNCIONES) != 10: err("tienen que ser diez funciones")
for f in B.FUNCIONES:
    if f["dir"] not in B.DIRS: err("direccion desconocida: " + f["id"])
    for k in ("n", "q", "ojo"):
        if not f.get(k): err("funcion %s sin %s" % (f["id"], k))
    if len(f["molde"]) != 3: err("funcion %s: el molde tiene tres piezas" % f["id"])
    if len(f["tu"]) < 3 or len(f["us"]) < 3: err("funcion %s: al menos tres formulas por carril" % f["id"])
    chk_frase(f["ej_tu"], f["id"], "tu", "ejemplo de tu de " + f["id"])
    chk_frase(f["ej_us"], f["id"], "us", "ejemplo de usted de " + f["id"])
if {f["dir"] for f in B.FUNCIONES} != set(B.DIRS): err("tienen que salir las tres direcciones")
for d, fs in (("a", {"agr", "dis", "fel"}), ("d", {"inv", "pro", "ped", "con", "des"}), ("c", {"ace", "rec"})):
    if {f["id"] for f in B.FUNCIONES if f["dir"] == d} != fs: err("direccion %s mal repartida" % d)

usadas = set()
for s in B.SITUACIONES:
    if len(s["pautas"]) != 5: err("situacion %s: cinco pautas" % s["id"])
    for lane in ("tu", "us"):
        if not (s[lane]["quien"] and s[lane]["msg"]): err("situacion %s: falta quien o el mensaje (%s)" % (s["id"], lane))
    for p in s["pautas"]:
        if p["f"] not in FN: err("situacion %s: funcion desconocida %s" % (s["id"], p["f"])); continue
        usadas.add(p["f"])
        for lane in ("tu", "us"): chk_frase(p[lane], p["f"], lane, "constructor %s/%s/%s" % (s["id"], p["f"], lane))
if usadas != set(FN): err("el constructor tiene que trabajar las diez funciones: faltan %s" % (set(FN) - usadas))

for iv in B.INVITACIONES:
    chk_frase(iv["ace"], "ace", iv["t"], "invitacion (si) " + iv["quien"])
    chk_frase(iv["rec"], "rec", iv["t"], "invitacion (no) " + iv["quien"], "fdxp")
    lane_ok(iv["msg"], iv["t"], "invitacion " + iv["quien"])
    exc = r"\bes que\b" if iv["t"] == "tu" else r"\bporque\b"
    if not re.search(exc, norm(plain(iv["rec"]))): err("invitacion %s: la excusa va con %s" % (iv["quien"], "es que" if iv["t"] == "tu" else "porque"))
if {iv["t"] for iv in B.INVITACIONES} != {"tu", "us"}: err("invitaciones de los dos carriles")

for c, d, f, s in B.DONDE: chk_frase(s, f, "tu", "donde " + c)
for mal, bien, why in B.ERRORES:
    if mal == bien or not why: err("error tipico sin correccion o sin porque: " + mal)

# Ejercicios
NAMES = {f["n"]: f["id"] for f in B.FUNCIONES}
def chk_o(it, name):
    o = it["o"]
    if len(o) != 3 or len(set(x.lower() for x in o)) != 3: err("%s: hacen falta 3 opciones distintas: %s" % (name, (it.get("q") or it.get("ctx"))[:50]))
    if not it.get("why"): err("%s: item sin explicacion" % name)
if len(B.P_FUNC) < 14: err("P_FUNC: al menos 14")
for it in B.P_FUNC:
    chk_o(it, "P_FUNC")
    for o in it["o"][1:]:
        if o not in NAMES: err("P_FUNC: la opcion «%s» no es una funcion" % o)
    if "|" in it["f"]:
        if not all(x in FN for x in it["f"].split("|")): err("P_FUNC: funcion desconocida " + it["f"])
    elif NAMES.get(it["o"][0]) != it["f"]: err("P_FUNC: la buena no es la funcion %s: %s" % (it["f"], it["q"]))
if not {f for it in B.P_FUNC for f in it["f"].split("|")} >= set(FN): err("P_FUNC: tienen que salir las diez funciones")
if len(B.P_FRASE) < 14: err("P_FRASE: al menos 14")
for it in B.P_FRASE:
    chk_o(it, "P_FRASE")
    if not has_f(it["o"][0], it["f"]): err("P_FRASE: la buena no lleva la formula de %s: %s" % (it["f"], it["o"][0]))
    lane_ok(it["o"][0], it["t"], "P_FRASE")
if {it["t"] for it in B.P_FRASE} != {"tu", "us"}: err("P_FRASE: de los dos carriles")
if {it["f"] for it in B.P_FRASE} != set(FN): err("P_FRASE: tienen que salir las diez funciones")
if len(B.E_BIENMAL) < 16: err("E_BIENMAL: al menos 16")
for it in B.E_BIENMAL:
    if not it.get("why"): err("bien/mal sin explicacion: " + it["q"])
    if it["ok"] not in (0, 1): err("bien/mal: ok debe ser 0 o 1")
    if it["ok"] == 1 and not it.get("fix"): err("bien/mal: frase mal sin correccion: " + it["q"])
    if it["ok"] == 0 and it.get("fix"): err("bien/mal: frase bien con correccion: " + it["q"])
if sum(1 for i in B.E_BIENMAL if i["ok"] == 0) < 6: err("bien/mal: faltan frases bien")

# Textos con huecos
for k, (f, w, ok) in B.MOTIVOS.items():
    if f not in FN or not w or not ok: err("motivo mal definido: " + k)
def chk_gaps(t):
    n = 0
    for g in GAP.findall(t["texto"]):
        n += 1
        if "#" not in g: err("hueco sin motivo en %s: %s" % (t["id"], g)); continue
        ops, mot = g.split("#"); ops = ops.split("|")
        if len(ops) != 3 or len(set(o.lower() for o in ops)) != 3: err("hueco sin 3 opciones distintas en %s: %s" % (t["id"], g))
        if mot not in B.MOTIVOS: err("motivo desconocido en %s: %s" % (t["id"], mot)); continue
        if ops[0].lower() not in B.MOTIVOS[mot][2]: err("en %s la buena (%s) no es la de su motivo %s" % (t["id"], ops[0], mot))
    if n < 6: err("texto con pocos huecos: " + t["id"])
    rest = GAP.sub("", t["texto"])
    if "[[" in rest or "]]" in rest: err("hueco mal cerrado en " + t["id"])
    lane_ok(filled(t["texto"]), t["t"], "texto relleno " + t["id"])
    return n
ngaps = {t["id"]: chk_gaps(t) for t in B.TEXTOS}
usados = {g.split("#")[1] for t in B.TEXTOS for g in GAP.findall(t["texto"])}
for m in B.MOTIVOS:
    if m not in usados: err("los textos no usan el motivo " + m)
if {t["t"] for t in B.TEXTOS} != {"tu", "us"}: err("textos de los dos carriles")

# Laminas
for L in B.LAMINAS:
    if len(L["pautas"]) != 5: err("lamina %s: 5 pautas" % L["id"])
    for _, gs in L["pautas"]:
        for g in gs:
            for f in g.split("|"):
                if f not in FN: err("lamina %s: funcion desconocida %s" % (L["id"], f))
    nw = len(L["mensaje"].split())
    if not 35 <= nw <= 45: err("lamina %s: el mensaje tiene %d palabras (35-45)" % (L["id"], nw))
    lane_ok(L["mensaje"], L["t"], "mensaje de la lamina " + L["id"])
if {L["t"] for L in B.LAMINAS} != {"tu", "us"}: err("una lamina de tu y otra de usted")

# Oral
if len(B.ORAL) < 16: err("oral: al menos 16 tarjetas")
for o in B.ORAL:
    if o["f"] not in FN: err("oral: funcion desconocida " + o["f"]); continue
    if not has_f(o["m"], o["f"]): err("oral: el modelo no lleva la formula de %s: %s" % (o["f"], o["m"]))
    lane_ok(o["m"], o["t"], "oral " + o["sit"][:30])
if {o["f"] for o in B.ORAL} != set(FN) or {o["t"] for o in B.ORAL} != {"tu", "us"}: err("oral: las diez funciones y los dos carriles")

# Detector
ids = set()
for d in B.DETECTOR:
    if d["t"] not in ("r", "a") or d["sc"] not in ("s", "x"): err("aviso mal definido: " + d["id"])
    if d["id"] in ids: err("id repetido en el detector: " + d["id"])
    ids.add(d["id"])
    try: d["_rx"] = re.compile(d["re"])
    except re.error as e: err("regex del detector: %s (%s)" % (d["id"], e))
    if not d.get("msg"): err("aviso sin mensaje: " + d["id"])
for name, r in [("d " + d["id"], d["re"]) for d in B.DETECTOR] + [("f " + k, v) for k, v in B.FUNC_RX.items()] + [("tu", B.TU_RX), ("us", B.US_RX)]:
    if r != norm(r): err("la regex %s tiene que ir sin tildes ni mayusculas" % name)
    if "(?<" in r or "(?P" in r: err("la regex %s usa algo que no funciona igual en el navegador" % name)

SENT = re.compile(r"[^.!?\n]+[.!?]*")
def det(txt):
    out = set()
    sents = [norm(s) for s in SENT.findall(txt)]
    for d in B.DETECTOR:
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
    if sum(1 for _, e in B.DETECTOR_PRUEBAS if not e) < 14: err("detector: hacen falta al menos 14 pruebas que NO deben saltar")
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
        if k not in vistos_err | vistos_bm: err("ninguna frase mala de la ficha da el aviso " + k)
    # Las opciones malas de P_FRASE que son errores tambien se ven (las que no son de otro carril ni de otra funcion)
    # Nada de lo que la ficha da por bueno puede dar ningun aviso ni tener formas de B1
    buenos = []
    for f in B.FUNCIONES: buenos += [plain(f["ej_tu"]), plain(f["ej_us"])]
    for s in B.SITUACIONES:
        for p in s["pautas"]: buenos += [plain(p["tu"]), plain(p["us"])]
    for iv in B.INVITACIONES: buenos += [iv["msg"], plain(iv["ace"]), plain(iv["rec"])]
    buenos += [plain(s) for _, _, _, s in B.DONDE] + [b for _, b, _ in B.ERRORES] + [e for _, _, e in B.ES_QUE]
    buenos += [i["q"] for i in B.E_BIENMAL if i["ok"] == 0] + [i["o"][0] for i in B.P_FRASE]
    buenos += [filled(t["texto"]) for t in B.TEXTOS] + [o["m"] for o in B.ORAL] + [L["mensaje"] for L in B.LAMINAS]
    for b in buenos:
        r = det(b)
        if r: err("detector: aviso %s en un texto bueno: %r" % (r, b.strip()[:90]))
        m = RX_B1.search(norm(b))
        if m: err("forma de B1 («%s») en un texto bueno: %r" % (m.group(0), b[:80]))
    # en la tabla «Los veras» la forma de B1 si esta y la del A2 no la tiene
    for w, fn, ej, a2 in B.LOS_VERAS:
        if RX_B1.search(norm(a2)) or det(a2): err("los veras: la alternativa del A2 no vale: " + a2)

# Node: el detector, las funciones y los carriles tienen que dar lo mismo en el navegador
NODE_OK = None
if not ERR and shutil.which("node"):
    def fpy(t):
        n = norm(t); return sorted(k for k, r in RX_F.items() if r.search(n))
    def lpy(t):
        n = norm(t); return [bool(RX_TU.search(n)), bool(RX_US.search(n))]
    textos_c = [t for t, _ in B.DETECTOR_PRUEBAS] + [o["m"] for o in B.ORAL] + [i["o"][k] for i in B.P_FRASE for k in range(3)] + [filled(t["texto"]) for t in B.TEXTOS]
    js_t = ("var D=%s;function norm(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}"
            "function det(t){var o={},ss=(t.match(/[^.!?\\n]+[.!?]*/g)||[]).map(norm);D.d.forEach(function(d){var r=new RegExp(d.re);"
            "if(d.sc==='s'){if(ss.some(function(s){return r.test(s);}))o[d.id]=1;}else if(r.test(norm(t)))o[d.id]=1;});return Object.keys(o).sort();}"
            "function fx(t){var n=norm(t);return Object.keys(D.f).filter(function(k){return new RegExp(D.f[k]).test(n);}).sort();}"
            "function ln(t){var n=norm(t);return [new RegExp(D.tu).test(n),new RegExp(D.us).test(n)];}"
            "var bad=[];D.p.forEach(function(p){var ids=det(p[0]);if(ids.join()!==p[1].slice().sort().join())bad.push(p[0]+' -> '+ids.join());});"
            "D.t.forEach(function(x){if(fx(x[0]).join()!==x[1].join())bad.push('funciones: '+x[0].slice(0,50));if(ln(x[0]).join()!==x[2].join())bad.push('carril: '+x[0].slice(0,50));});"
            "console.log(JSON.stringify(bad));") % json.dumps(
        {"d": [{"id": d["id"], "re": d["re"], "sc": d["sc"]} for d in B.DETECTOR], "p": B.DETECTOR_PRUEBAS, "f": B.FUNC_RX,
         "tu": B.TU_RX, "us": B.US_RX, "t": [[t, fpy(t), lpy(t)] for t in textos_c]}, ensure_ascii=False)
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
def mk(s, d, num=False):
    """Pinta las piezas del molde. d = direccion de la funcion (color de la formula). num = numera las piezas (constructor)."""
    c = [0]
    def rep(m):
        k = m.group(1); c[0] += 1
        cls = "pz %s%s" % (k, (" " + d) if k == "f" else "")
        return '<span class="%s"%s>%s</span>' % (cls, (' data-n="%d"' % c[0]) if num else "", m.group(2))
    return MARK.sub(rep, s)
def nl(s): return s.replace("\n", "<br>")
INK = "#14161C"; MUT = "#5E5A55"
DCOL = {"a": ("#6B46C1", "#EEE8FA"), "d": ("#2F7D4F", "#E3F1E8"), "c": ("#0F766E", "#DDF2EF")}
LCOL = {"tu": ("#C2410C", "#FDEBDD"), "us": ("#1D5FA8", "#E2ECF8")}

def svg(vb, aria, inner, cls="dg"): return '<svg class="%s" viewBox="%s" role="img" aria-label="%s">%s</svg>' % (cls, vb, aria, inner)
def txt(x, y, s, size=16, col=INK, w="400", anchor="middle"):
    return '<text x="%s" y="%s" text-anchor="%s" font-size="%s" font-weight="%s" fill="%s">%s</text>' % (x, y, anchor, size, w, col, s)
def head(x, y, d, col, s=9):
    if d == "r": pts = (x, y, x - s * 1.5, y - s, x - s * 1.5, y + s)
    else: pts = (x, y, x + s * 1.5, y - s, x + s * 1.5, y + s)
    return '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>' % (pts + (col,))
def person(x, y, col):
    return '<circle cx="%d" cy="%d" r="11" fill="%s"/><path d="M%d,%d q15,-26 30,0 z" fill="%s"/>' % (x, y, col, x - 15, y + 34, col)
def rbox(x, y, w, h, col, soft, label, size=14):
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s" stroke="%s" stroke-width="2.5"/>' % (x, y, w, h, soft, col)
            + txt(x + w / 2, y + h / 2 + size / 3, label, size, INK, "600"))

def dir_svg(k):
    """Dibujo de cada direccion (tarjetas). 240 x 110: tu en el centro y la flecha."""
    c, s = DCOL[k]; o = ""
    if k == "a":
        o += person(170, 34, INK) + '<line x1="148" y1="52" x2="96" y2="52" stroke="%s" stroke-width="4"/>' % c + head(84, 52, "l", c)
        o += rbox(8, 30, 74, 44, c, s, "ya pasó") + txt(170, 100, "tú, ahora", 12, MUT)
    elif k == "d":
        o += person(56, 34, INK) + '<line x1="80" y1="52" x2="132" y2="52" stroke="%s" stroke-width="4"/>' % c + head(146, 52, "r", c)
        o += rbox(148, 30, 88, 44, c, s, "lo que quieres", 11.5) + txt(56, 100, "tú, ahora", 12, MUT)
    else:
        o += person(36, 34, MUT) + person(204, 34, INK)
        o += '<path d="M58,40 L182,40" stroke="%s" stroke-width="3" stroke-dasharray="5 5"/>' % MUT + head(184, 40, "r", MUT, 7)
        o += txt(120, 32, "¿vienes?", 13, MUT, "700")
        o += '<path d="M182,66 L66,66" stroke="%s" stroke-width="4"/>' % c + head(58, 66, "l", c)
        o += txt(120, 90, "sí / no + excusa", 13, c, "700")
    return svg("0 0 240 110", "Dibujo: " + B.DIRS[k]["dib"], o, "ic")

def molde_svg():
    cols = [("#14161C", "#FFFFFF"), ("#14161C", "#FFFFFF"), ("#5E5A55", "#FBF9F6")]
    o = ""; xs = [8, 214, 420]
    lab = [B.PIEZAS["f"][0], B.PIEZAS["d"][0], B.PIEZAS["x"][0]]
    ej = ["Gracias por", "las fotos del viaje.", "¡Qué bonitas!"]
    for i, x in enumerate(xs):
        col, soft = cols[i]
        dash = ' stroke-dasharray="6 5"' if i == 1 else ""
        fill = DCOL["a"][1] if i == 0 else soft
        stroke = DCOL["a"][0] if i == 0 else col
        o += '<rect x="%d" y="34" width="172" height="62" rx="12" fill="%s" stroke="%s" stroke-width="2.5"%s/>' % (x, fill, stroke, dash)
        o += txt(x + 86, 24, "%d. %s" % (i + 1, lab[i]), 15, stroke, "700") + txt(x + 86, 71, ej[i], 14, INK, "600")
        if i < 2: o += txt(x + 193, 74, "+", 24, MUT, "700")
    o += txt(300, 124, "la fórmula fija + lo concreto de la lámina + un porqué o una pregunta", 14, MUT)
    return svg("0 0 600 136", "El molde de tres piezas: la fórmula, el dato y el detalle", o, "dg pr")

def no_svg():
    c, s = DCOL["c"]; o = ""
    for i, (w, lab) in enumerate(B.PIEZAS_NO):
        x = 8 + i * 138
        o += '<rect x="%d" y="40" width="124" height="70" rx="12" fill="%s" stroke="%s" stroke-width="2.5"/>' % (x, s if i != 3 else DCOL["d"][1], c if i != 3 else DCOL["d"][0])
        o += txt(x + 62, 30, "%d · %s" % (i + 1, lab), 13, c if i != 3 else DCOL["d"][0], "700")
        parts = w.split(" / ") if " / " in w else ([w[:w.find(" + ")], w[w.find(" + ") + 1:]] if " + " in w else [w])
        for j, p in enumerate(parts[:2]): o += txt(x + 62, 70 + j * 20 - (len(parts[:2]) - 1) * 8, p, 12.5, INK, "600")
    return svg("0 0 560 120", "El no en cuatro piezas: la pena, el no, la excusa y otra propuesta", o, "dg pr")

def cards():
    o = '<div class="cams">'
    for k in B.ORDEN_DIR:
        d = B.DIRS[k]; fs = ", ".join(f["n"].lower() for f in B.FUNCIONES if f["dir"] == k)
        o += '<div class="cam c%s">%s<h3>%s</h3><p class="qf">%s</p><p>%s</p><p class="small"><b>%s</b></p></div>' % (k, dir_svg(k), d["n"], d["q"], d["txt"], fs[:1].upper() + fs[1:])
    return o + '</div>'

LEG = ('<div class="legend"><span><span class="pz f a">la fórmula</span> la frase fija</span><span><span class="pz d">el dato</span> lo concreto</span>'
       '<span><span class="pz x">el detalle</span> por qué, una pregunta</span><span><span class="lc tu">tú</span><span class="lc us">usted</span> los dos carriles (R07)</span></div>')

def vistazo():
    o = '<table class="t"><tr><th>Función</th><th>Con tú</th><th>Con usted</th></tr>'
    for f in B.FUNCIONES:
        o += '<tr><td><span class="vchip %s">%s</span> <b>%s</b></td><td>%s</td><td>%s</td></tr>' % (f["dir"], B.DIRS[f["dir"]]["n"], f["n"], f["tu"][0], f["us"][0])
    return o + '</table>'

def losveras():
    o = '<table class="t"><tr><th>Lo verás</th><th>Sirve para</th><th>En el A2 escribe</th></tr>'
    for w, fn, ej, a2 in B.LOS_VERAS: o += '<tr><td><i>%s</i></td><td>%s</td><td><b>%s</b></td></tr>' % (ej, fn, a2)
    return o + '</table>'

def otras():
    o = '<table class="t"><tr><th>La pauta dice...</th><th>Tu frase</th><th>Ficha</th></tr>'
    for p, f, r in B.OTRAS_PAUTAS: o += '<tr><td>«%s»</td><td>%s</td><td class="small">%s</td></tr>' % (p, f, r)
    return o + '</table>'

def esque():
    return '<table class="t"><tr><th>Palabra</th><th>Cuándo</th><th>Ejemplo</th></tr>' + "".join(
        '<tr><td><b>%s</b></td><td>%s</td><td><i>%s</i></td></tr>' % r for r in B.ES_QUE) + '</table>'

def donde():
    return "".join('<div class="box"><span class="chip">%s</span><p class="small muted" style="margin:6px 0">%s</p><p style="margin:0">%s</p></div>'
                   % (c, d, mk(s, FN[f]["dir"])) for c, d, f, s in B.DONDE)

def errores():
    o = '<div class="errs">'
    for mal, bien, why in B.ERRORES:
        o += '<div class="err"><div class="mal"><span aria-hidden="true">✗</span> <s>%s</s></div><div class="bien"><span aria-hidden="true">✓</span> %s</div><div class="small muted">%s</div></div>' % (mal, bien, why)
    return o + '</div>'

def si_list(lst): return "".join('<li><b>%s</b> · <span class="muted">%s</span></li>' % (w, l) for w, l in lst)

CSS_R = CSS + r"""
:root{--da:#6B46C1;--da-soft:#EEE8FA;--dd:#2F7D4F;--dd-soft:#E3F1E8;--dc:#0F766E;--dc-soft:#DDF2EF;--tu:#C2410C;--tu-soft:#FDEBDD;--us:#1D5FA8;--us-soft:#E2ECF8}
.pz{border-radius:4px;padding:0 3px 1px;line-height:1.9}
.pz.f{font-weight:700;border-bottom:3px solid}
.pz.f.a{background:var(--da-soft);border-color:var(--da)}.pz.f.d{background:var(--dd-soft);border-color:var(--dd)}.pz.f.c{background:var(--dc-soft);border-color:var(--dc)}
.pz.d{border-bottom:2px dashed var(--ink)}
.pz.x{color:var(--muted);font-style:italic;background:var(--paper)}
.pz.p{background:var(--dd-soft);border-bottom:3px dotted var(--dd)}
.pz.hid{visibility:hidden}
.lc{display:inline-block;font-size:.78rem;font-weight:700;border-radius:999px;padding:1px 9px;margin-right:4px}
.lc.tu{background:var(--tu-soft);color:var(--tu)}.lc.us{background:var(--us-soft);color:var(--us)}
.cams{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:18px 0}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px 14px;border-top:6px solid var(--da)}
.cam.cd{border-top-color:var(--dd)}.cam.cc{border-top-color:var(--dc)}
.cam h3{margin:4px 0 2px}.cam p{margin:0 0 4px;font-size:.95rem}.cam p.qf{color:var(--muted);font-style:italic;margin-bottom:6px}
svg.ic{width:100%;max-width:220px;height:auto;display:block}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.box h4{margin:0 0 4px}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
.fgrp{margin:6px 0}.fgrp .lab{font-size:.8rem;font-weight:700;letter-spacing:.03em;margin-right:6px}
.fgrp.a .lab{color:var(--da)}.fgrp.d .lab{color:var(--dd)}.fgrp.c .lab{color:var(--dc)}
.fgrp .pills{display:inline-flex;margin:4px 0}
.lanes{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.lanes button{font:inherit;font-weight:700;border:3px solid var(--line);background:#fff;border-radius:10px;padding:10px 12px;cursor:pointer}
.lanes button.tu.on{border-color:var(--tu);background:var(--tu-soft)}.lanes button.us.on{border-color:var(--us);background:var(--us-soft)}
.lanes button.ac.on{border-color:var(--dc);background:var(--dc-soft)}.lanes button.re.on{border-color:var(--bad);background:var(--bad-soft)}
svg.dg{width:100%;height:auto;display:block;margin:6px 0}
svg.pr{max-width:600px;margin:6px auto}
.fcard{background:#fff;border:2px solid var(--line);border-radius:14px;padding:16px 18px;margin:12px 0}
.fcard.tu{border-color:var(--tu)}.fcard.us{border-color:var(--us)}
.fcard h3{margin:0 0 2px}
.molde{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:10px 0}
.molde div{border-radius:10px;padding:8px 10px;font-size:.92rem;background:var(--paper)}
.molde div b{display:block;font-size:.75rem;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.molde .m1{border:2px solid var(--ink)}.molde .m2{border:2px dashed var(--ink)}.molde .m3{border:2px solid var(--line)}
.res{font-family:Georgia,serif;font-size:1.22rem;font-weight:700;margin:10px 0;line-height:1.85}
.expl{border-radius:8px;padding:10px 14px;margin-top:6px;background:var(--paper)}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;margin:8px 0}
.lamini{background:var(--paper);border-left:4px solid var(--line);border-radius:0 8px 8px 0;padding:8px 12px;margin:8px 0}
.lamini.tu{border-left-color:var(--tu)}.lamini.us{border-left-color:var(--us)}
.steps3{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.steps3 span{font-size:.8rem;font-weight:700;border-radius:999px;padding:2px 10px;background:var(--line);color:var(--muted)}
.steps3 span.on{background:var(--ink);color:#fff}
.errs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.err{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.err .mal{color:var(--bad)}.err .bien{margin:4px 0}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.vchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px;background:var(--paper);color:var(--muted)}
.vchip.a{background:var(--da-soft);color:var(--da)}.vchip.d{background:var(--dd-soft);color:var(--dd)}.vchip.c{background:var(--dc-soft);color:var(--dc)}
.vchip.tu{background:var(--tu-soft);color:var(--tu)}.vchip.us{background:var(--us-soft);color:var(--us)}
.vchip.ok{background:var(--ok-soft);color:var(--ok)}.vchip.no{background:var(--line);color:var(--muted);text-decoration:line-through}
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
.cnts{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.check{list-style:none;padding:0;margin:8px 0}.check li{padding:5px 0}.check label{cursor:pointer}
.ocard{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin-top:12px}
.ocard .ph1{font-family:Georgia,serif;font-size:1.15rem;font-weight:700}
.sit{font-family:Georgia,serif;font-size:1.25rem;font-weight:700;margin:8px 0;line-height:1.35}
.clock{font-family:Georgia,serif;font-size:1.6rem;font-weight:700;font-variant-numeric:tabular-nums}
.tbar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:8px 0}
.tbar i{display:block;height:100%;background:var(--coral);width:0;transition:width .25s linear}
.model{background:var(--paper);border-radius:8px;padding:10px 14px;margin-top:8px;line-height:1.9}
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
@media (max-width:700px){.errs,.lanes{grid-template-columns:1fr}.molde{grid-template-columns:1fr}.qz .ops.bm{grid-template-columns:1fr 1fr}table.t{font-size:.88rem}table.t td,table.t th{padding:6px 5px}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:13px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.err,.fcard{break-inside:avoid}}
"""

STEPS = [("idea", "Atrás y adelante"), ("pauta", "De la pauta a la frase"), ("sino", "Sí y no"), ("examen", "En el examen"),
         ("practica", "Practica"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_IDEA = """
<h2>Atrás, adelante y contestar</h2>
<p class="lead">En la tarea 1 casi todas las pautas son un verbo: <i>agradecer, felicitar, invitar, decir si puedes ir...</i> Cada verbo es un <b>gesto hacia la otra persona</b>, y solo hay tres direcciones. Si sabes hacia dónde mira la pauta, ya sabes qué fórmula usar.</p>
__CARDS__
<h3>El molde de tres piezas</h3>
<p>Cada pauta se convierte en una frase con el mismo molde: <b>la fórmula</b> (la frase fija de la función) + <b>el dato</b> (lo concreto de tu lámina) + <b>el detalle</b> (por qué, cómo te sientes o una pregunta). Con la fórmula sola la pauta queda a medias; con las tres piezas, la pauta está completa.</p>
__MOLDE__
__LEG__
<h3>Las diez funciones</h3>
<p class="muted small">Elige una función y un carril: de tú (un amigo, la familia) o de usted (alguien que no conoces, un servicio).</p>
<div id="fnsel"></div>
<div class="lanes" id="flsel"><button class="tu" data-act="fl" data-k="tu">De tú</button><button class="us" data-act="fl" data-k="us">De usted</button></div>
<div id="fnvis" aria-live="polite"></div>
<h3>Las diez en un vistazo</h3>
__VISTAZO__
<p class="small muted">__NOTA__</p>
<details><summary>Lo verás en los textos (no lo necesitas para aprobar)</summary>
<p>Estas formas salen en correos y en la lectura. Está bien entenderlas, pero son de B1 o solo para leer. Para escribir en el A2, usa la columna de la derecha.</p>
__VERAS__</details>
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="pauta">Siguiente: de la pauta a la frase</button></div>
"""

V_PAUTA = """
<h2>De la pauta a la frase</h2>
<p class="lead">Lee la pauta, busca el verbo y conviértelo en su frase con el molde. Así no se te queda ninguna pauta sin escribir.</p>
<h3>Cómo se lee una pauta</h3>
<ul>__LEER__</ul>
<h3>Monta la frase</h3>
<p class="muted small">Elige una situación y un carril. Después toca una pauta y monta la frase pieza a pieza.</p>
<div class="pills" id="cssel"></div>
<div class="lanes" id="clsel"><button class="tu" data-act="cl" data-k="tu">Le escribes a alguien cercano (tú)</button><button class="us" data-act="cl" data-k="us">Le escribes de usted</button></div>
<div class="box" id="csvis" aria-live="polite"></div>
<h3>Las otras pautas del correo</h3>
<p>No todas las pautas son una de las diez funciones. Estas también salen mucho; cada una tiene su ficha.</p>
__OTRAS__
<div class="row"><button class="btn cta" data-go="sino">Siguiente: sí y no</button></div>
"""

V_SINO = """
<h2>Decir que sí y decir que no</h2>
<p class="lead">Aceptar y rechazar contestan a lo que te propone el otro. Son las pautas que más se quedan a medias: un «sí» seco o un «no» sin razón.</p>
<h3>El no en cuatro piezas</h3>
__NOSVG__
<ol>__NOLIST__</ol>
<div class="tip">Las tres primeras piezas son obligatorias; la cuarta es la que sube la nota (y en la tarea 3 de la oral, la que necesitas cuando el examinador te dice que no).</div>
<h3>El sí con un detalle</h3>
<ol>__SILIST__</ol>
<h3>¿Es que o porque?</h3>
__ESQUE__
<h3>Contesta tú</h3>
<p class="muted small">Elige una invitación y decide: ¿sí o no?</p>
<div class="pills" id="ivsel"></div>
<div class="lanes" id="iasel"><button class="ac" data-act="ia" data-k="ace">Digo que sí</button><button class="re" data-act="ia" data-k="rec">Digo que no</button></div>
<div class="box" id="ivvis" aria-live="polite"></div>
<div class="row"><button class="btn cta" data-go="examen">Siguiente: en el examen</button></div>
"""

V_EXAMEN = """
<h2>Dónde sale en el examen</h2>
<p class="lead">Las funciones son el corazón de la tarea 1 de la escritura y de la tarea 3 de la oral. Y en la lectura y la auditiva te ayudan a entender para qué escribe o llama alguien.</p>
__DONDE__
<div class="note">__REGLA__</div>
<h3>Los errores más típicos</h3>
<p>Tienes que reconocerlos en tus correos y en tu oral. Mira por qué fallan.</p>
__ERRORES__
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACT = """
<h2>Practica</h2>
<p class="lead">Cuatro ejercicios. Cada respuesta se corrige en el momento, con la explicación.</p>
<div class="pills" id="exsel">
 <button class="pill on" data-act="ex" data-k="p1">1. ¿Qué pide la pauta?</button>
 <button class="pill" data-act="ex" data-k="p2">2. ¿Qué frase escribes?</button>
 <button class="pill" data-act="ex" data-k="e2">3. Textos del examen</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Ahora úsalo en una tarea del examen: escribe un correo o contesta en voz alta.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="o">Oral: responde rápido</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu correo y después pulsa <b>Revisar mis funciones</b>: la página mira si cada pauta tiene su fórmula y te avisa de los errores típicos. No corrige el texto entero: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="ato" hidden>
 <p>Vas a ver una situación, la función que pide y el carril (tú o usted). Di la frase <b>en voz alta</b> antes de que termine el reloj: la fórmula y un detalle. Después compara con el modelo. Esto también te sirve para la tarea 3 de la oral.</p>
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
  <label><input type="radio" name="o1" value="Atras y adelante">Atrás y adelante</label>
  <label><input type="radio" name="o1" value="El molde de tres piezas">El molde de tres piezas</label>
  <label><input type="radio" name="o1" value="Monta la frase">Monta la frase</label>
  <label><input type="radio" name="o1" value="Si y no">Sí y no</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tu">Ahora tú</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué función te cuesta más?</label>
 <div class="chips" role="group" aria-labelledby="o2l">__O2__</div>
 <label class="q" id="o3l">3. ¿Te ayuda la idea de «atrás, adelante y contestar»?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Si, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con las pautas del correo? (1 = nada, 10 = total)</label>
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
    o = '<h2>Las funciones de los correos · resumen</h2>' + cards() + '<h3>El molde de tres piezas</h3>' + molde_svg() + LEG
    o += '<h3>Las diez en un vistazo</h3>' + vistazo()
    o += '<h3>El no en cuatro piezas</h3>' + no_svg()
    o += '<h3>Los errores típicos</h3>' + errores()
    return o

O2 = "".join('<label><input type="radio" name="o2" value="%s">%s</label>' % (f["n"], f["n"]) for f in B.FUNCIONES)
views = {
    "idea": V_IDEA.replace("__CARDS__", cards()).replace("__MOLDE__", molde_svg()).replace("__LEG__", LEG).replace("__VISTAZO__", vistazo())
                  .replace("__NOTA__", B.VISTAZO_NOTA).replace("__VERAS__", losveras()),
    "pauta": V_PAUTA.replace("__LEER__", "".join("<li>%s</li>" % s for s in B.LEER_PAUTA)).replace("__OTRAS__", otras()),
    "sino": V_SINO.replace("__NOSVG__", no_svg()).replace("__NOLIST__", si_list(B.PIEZAS_NO)).replace("__SILIST__", si_list(B.PIEZAS_SI)).replace("__ESQUE__", esque()),
    "examen": V_EXAMEN.replace("__DONDE__", donde()).replace("__REGLA__", B.REGLA).replace("__ERRORES__", errores()),
    "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL).replace("__O2__", O2),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R13</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
""".replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

# ------------------------------------------------------------------ DATOS PARA EL SCRIPT
def fdata(f):
    return {"id": f["id"], "n": f["n"], "dir": f["dir"], "q": f["q"], "molde": f["molde"], "tu": f["tu"], "us": f["us"],
            "ej": {"tu": mk(f["ej_tu"], f["dir"]), "us": mk(f["ej_us"], f["dir"])}, "ojo": f["ojo"]}
DATA = {
    "key": STORAGE, "title": TITLE,
    "steps": [{"id": k, "label": l} for k, l in STEPS],
    "dirs": {k: B.DIRS[k]["n"] for k in B.ORDEN_DIR}, "order": B.ORDEN_DIR, "carril": B.CARRIL,
    "funcs": [fdata(f) for f in B.FUNCIONES], "fn": {f["id"]: f["n"] for f in B.FUNCIONES}, "fdir": {f["id"]: f["dir"] for f in B.FUNCIONES},
    "piezas": {k: v[0] for k, v in B.PIEZAS.items()},
    "sits": [{"id": s["id"], "tit": s["tit"], "tu": s["tu"], "us": s["us"],
              "pautas": [{"f": p["f"], "p": p["p"], "tu": mk(p["tu"], FN[p["f"]]["dir"], True), "us": mk(p["us"], FN[p["f"]]["dir"], True)} for p in s["pautas"]]}
             for s in B.SITUACIONES],
    "inv": [{"t": i["t"], "quien": i["quien"], "msg": i["msg"], "ace": mk(i["ace"], "c"), "rec": mk(i["rec"], "c")} for i in B.INVITACIONES],
    "qz": {
        "p1": {"items": B.P_FUNC, "n": 8, "name": "¿Qué pide la pauta?", "info": "Lee la pauta como en el examen y busca el verbo: ¿qué función pide?"},
        "p2": {"items": B.P_FRASE, "n": 8, "name": "¿Qué frase escribes?", "info": "Mira la situación y el carril (tú o usted). Elige la frase que cumple la función, en su carril y sin errores."},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Errores típicos de los exámenes. ¿La frase está bien o falla?"},
    },
    "motivos": {k: {"f": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "textos": B.TEXTOS,
    "laminas": B.LAMINAS, "funcrx": B.FUNC_RX, "turx": B.TU_RX, "usrx": B.US_RX, "detector": B.DETECTOR,
    "oral": B.ORAL,
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function lc(t){ return '<span class="lc '+t+'">'+D.carril[t]+'</span>'; }
function blank(){ return {cur:'idea', seen:{}, fn:'agr', fl:'tu', cs:0, cl:'tu', cp:0, cst:1, iv:0, ia:'ace', ex:'p1', etext:D.textos[0].id, at:'w',
  qz:{}, qlog:{}, cz:{}, w:{}, wchk:{}, wrev:{}, lam:D.laminas[0].id, oc:{n:10,t:8}, ro:null, olog:[],
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
function lanesOn(boxId, val){ var bs=$(boxId).querySelectorAll('button'); for(var i=0;i<bs.length;i++){ var on=bs[i].getAttribute('data-k')===val; bs[i].classList.toggle('on',on); bs[i].setAttribute('aria-pressed',on); } }

/* ---------------- 1. las diez funciones ---------------- */
function fget(id){ return D.funcs.filter(function(f){ return f.id===id; })[0]; }
function renderFn(){
 var o='';
 D.order.forEach(function(d){
  o+='<div class="fgrp '+d+'"><span class="lab">'+esc(D.dirs[d].toUpperCase())+'</span><span class="pills">';
  D.funcs.forEach(function(f){ if(f.dir===d) o+='<button class="pill'+(S.fn===f.id?' on':'')+'" data-act="fn" data-k="'+f.id+'">'+esc(f.n)+'</button>'; });
  o+='</span></div>';
 });
 $('fnsel').innerHTML=o; lanesOn('flsel', S.fl);
 var f=fget(S.fn), L=S.fl;
 var h='<div class="fcard '+L+'"><span class="vchip '+f.dir+'">'+esc(D.dirs[f.dir])+'</span> '+lc(L)+'<h3 style="margin-top:6px">'+esc(f.n)+'</h3><p class="muted" style="margin:0"><i>'+esc(f.q)+'</i></p>';
 h+='<div class="molde"><div class="m1"><b>1 · '+D.piezas.f+'</b>'+esc(f.molde[0])+'</div><div class="m2"><b>2 · '+D.piezas.d+'</b>'+esc(f.molde[1])+'</div><div class="m3"><b>3 · '+D.piezas.x+'</b>'+esc(f.molde[2])+'</div></div>';
 h+='<p class="res">'+f.ej[L]+'</p>';
 h+='<p class="small" style="margin:8px 0 2px"><b>Más fórmulas '+(L==='tu'?'de tú':'de usted')+':</b></p><ul class="small" style="margin:0">'+f[L].map(function(x){ return '<li>'+esc(x)+'</li>'; }).join('')+'</ul>';
 h+='<div class="expl"><b>Ojo:</b> '+f.ojo+'</div></div>';
 $('fnvis').innerHTML=h;
}
/* ---------------- 2. monta la frase ---------------- */
function renderCs(){
 var o=''; D.sits.forEach(function(s,i){ o+='<button class="pill'+(S.cs===i?' on':'')+'" data-act="cs" data-i="'+i+'">'+esc(s.tit)+'</button>'; });
 $('cssel').innerHTML=o; lanesOn('clsel', S.cl);
 var s=D.sits[S.cs], L=S.cl, who=s[L], p=s.pautas[S.cp]||s.pautas[0];
 var h='<div class="lamini '+L+'">'+lc(L)+' <b>'+esc(who.quien)+'</b>. '+esc(who.msg)+'</div>';
 h+='<p class="small" style="margin:10px 0 4px"><b>Las pautas</b> (toca una):</p><div class="pills">';
 s.pautas.forEach(function(q,i){ h+='<button class="pill'+(S.cp===i?' on':'')+'" data-act="cp" data-i="'+i+'">'+esc(q.p.replace(/;$/,''))+'</button>'; });
 h+='</div>';
 var st=S.cst, names=['1 · '+D.piezas.f,'2 · '+D.piezas.d,'3 · '+D.piezas.x];
 h+='<p style="margin:12px 0 2px">La pauta pide <span class="vchip '+D.fdir[p.f]+'">'+esc(D.fn[p.f])+'</span>.</p><div class="steps3">'+names.map(function(n,i){ return '<span class="'+(i<st?'on':'')+'">'+n+'</span>'; }).join('')+'</div>';
 h+='<p class="res" id="csres">'+p[L]+'</p>';
 h+='<div class="row">'+(st<3?'<button class="btn cta" data-act="cnext">Añadir la pieza '+(st+1)+'</button>':'<span class="small"><b>¡Frase completa!</b> Prueba con el otro carril o con otra pauta.</span>')+(st>1?'<button class="btn sm" data-act="creset">Empezar otra vez</button>':'')+'</div>';
 $('csvis').innerHTML=h;
 var ps=$('csres').querySelectorAll('.pz'); for(var i=0;i<ps.length;i++){ var n=+ps[i].getAttribute('data-n'); ps[i].classList.toggle('hid', n>st); }
}
/* ---------------- 3. si y no ---------------- */
function renderIv(){
 var o=''; D.inv.forEach(function(v,i){ o+='<button class="pill'+(S.iv===i?' on':'')+'" data-act="iv" data-i="'+i+'">'+esc(v.quien)+'</button>'; });
 $('ivsel').innerHTML=o; lanesOn('iasel', S.ia);
 var v=D.inv[S.iv];
 $('ivvis').innerHTML='<div class="lamini '+v.t+'">'+lc(v.t)+' <b>'+esc(v.quien)+':</b> «'+esc(v.msg)+'»</div><p class="res">'+v[S.ia]+'</p><div class="expl">'+
  (S.ia==='ace'?'El sí: la fórmula, a qué dices que sí y un detalle o una pregunta. ':'El no: la pena, el no, la excusa ('+(v.t==='tu'?'«es que», con alguien cercano':'«porque», de usted')+') y otra propuesta. ')+'Pulsa el otro botón para ver la otra respuesta.</div>';
}

/* ---------------- motor de opcion multiple ---------------- */
function qzNew(k){ var c=D.qz[k]; S.qz[k]={order:shuffle(range(c.items.length)).slice(0,c.n), i:0, res:[], perm:{}}; save(); }
function qLabel(it){ return it.q || it.ctx; }
function qHead(k, it){
 if(k==='p1') return '<span class="chip">La pauta dice</span> «'+esc(it.q)+'»<br><b>¿Qué función pide?</b>';
 if(k==='p2') return lc(it.t)+' '+esc(it.ctx)+'<br><b>¿Qué escribes?</b>';
 return esc(it.q);
}
function qzRender(k, box){
 var c=D.qz[k]; if(!S.qz[k]) qzNew(k);
 var st=S.qz[k], N=st.order.length;
 if(st.i>=N){
  var ok=st.res.filter(function(r){return r.ok;}).length, fails=st.res.filter(function(r){return !r.ok;});
  var msg = ok>=N-1 ? '¡Muy bien! Conviertes las pautas en frases sin problemas.' : (ok>=Math.ceil(N*0.6) ? 'Bien. Mira otra vez las explicaciones de las que has fallado.' : 'Vuelve a mirar las diez funciones y el molde, y repite con otras frases.');
  var o='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+msg+'</p>';
  if(fails.length){ o+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fails.forEach(function(r){ var it=c.items[r.k]; o+='<li>'+esc(strip(qLabel(it)).slice(0,90))+' → <b>'+(c.bm?(it.ok?'Mal: '+esc(it.fix):'Bien'):esc(it.o[0]))+'</b></li>'; }); o+='</ul>'; }
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
 if(ans) o+='<div class="fb '+(ans.ok?'good':'bad')+'" role="status"><b>'+(ans.ok?'¡Bien!':'No.')+'</b> '+(c.bm&&it.ok?'Corrección: <i>'+esc(it.fix)+'</i><br>':'')+it.why+'</div>';
 o+='<div class="row"'+(ans?'':' hidden')+'><button class="btn cta" data-act="qnext" data-k="'+k+'">'+(st.i+1<N?'Siguiente':'Ver el resultado')+'</button></div></div>';
 box.innerHTML=o;
}
function qzAnswer(k, pick){
 var c=D.qz[k], st=S.qz[k]; if(st.res[st.i]) return;
 var it=c.items[st.order[st.i]], ok = c.bm ? (pick===it.ok) : (pick===0);
 st.res[st.i]={k:st.order[st.i], pick:pick, ok:ok};
 if(st.i===st.order.length-1){
  var n=st.res.filter(function(r){return r&&r.ok;}).length;
  var fl=[]; st.res.forEach(function(r){ if(r&&!r.ok) fl.push(strip(qLabel(c.items[r.k])).slice(0,70)); });
  S.qlog[k]={last:n+'/'+st.order.length, fails:fl};
 }
 save();
}

/* ---------------- motor de huecos ---------------- */
var GAPRX=/\[\[([^\]]+)\]\]/g;
function seeded(arr, seed){ var h=0; for(var i=0;i<seed.length;i++) h=(h*31+seed.charCodeAt(i))>>>0; var a=arr.slice(); for(var j=a.length-1;j>0;j--){ h=(Math.imul(h,1103515245)+12345)>>>0; var r=(h>>>16)%(j+1); var t=a[j]; a[j]=a[r]; a[r]=t; } return a; }
function parseGaps(id, s){
 var n=0;
 var html=esc(s).replace(GAPRX, function(m0, inner){
  n++; var p=inner.split('#'), ops=p[0].split('|'), gid=id+'-'+n, cur=S.cz[gid];
  var sel='<sup>'+n+'</sup><select data-g="'+gid+'" aria-label="Hueco '+n+'"'+(cur&&cur.cur===strip(ops[0])?' disabled class="ok"':(cur?' class="no"':''))+'><option value="">…</option>';
  seeded(ops, gid).forEach(function(o){ sel+='<option'+(cur&&cur.cur===o?' selected':'')+'>'+o+'</option>'; });
  return sel+'</select>';
 });
 return {html:html.replace(/\n/g,'<br>').replace(/(EXAMINADOR|CANDIDATO):/g,'<b>$1:</b>'), n:n};
}
function gapInfo(id, s){ var list=[], n=0; s.replace(GAPRX, function(m0,inner){ n++; var p=inner.split('#'); list.push({gid:id+'-'+n, n:n, ok:p[0].split('|')[0], m:p[1]}); return m0; }); return list; }
function fbList(id, s){
 var o='', tot=0, done=0, first=0;
 gapInfo(id,s).forEach(function(g){
  tot++; var c=S.cz[g.gid]; if(!c) return; done += c.cur===g.ok?1:0; if(c.first===g.ok) first++;
  var mo=D.motivos[g.m], fn=D.fn[mo.f], dr=D.fdir[mo.f];
  if(c.cur===g.ok) o+='<li class="ok">'+g.n+'. ✓ <b>'+esc(g.ok)+'</b> · <span class="vchip '+dr+'">'+fn+'</span> '+mo.w+'</li>';
  else o+='<li class="no">'+g.n+'. ✗ <b>'+esc(c.cur)+'</b> no va aquí. Pista: <span class="vchip '+dr+'">'+fn+'</span> '+mo.w+' Prueba otra vez.</li>';
 });
 return {html:o, tot:tot, done:done, first:first};
}
function renderE2(){
 var o='<div class="pills">'; D.textos.forEach(function(t){ o+='<button class="pill'+(S.etext===t.id?' on':'')+'" data-act="etext" data-id="'+t.id+'">'+esc(t.titulo)+'</button>'; }); o+='</div>';
 var t=D.textos.filter(function(x){return x.id===S.etext;})[0], g=parseGaps(t.id, t.texto), f=fbList(t.id, t.texto);
 o+='<div class="cz"><span class="chip">'+esc(t.tipo)+'</span>'+lc(t.t)+'<span class="tema">'+esc(t.titulo)+'</span>'+g.html+'</div>';
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
var EXINFO={e2:'Dos correos de tú, uno de usted y un diálogo de la tarea 3. Elige la fórmula de cada hueco: la corrección sale enseguida, con el motivo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
var CH=['Cada pauta tiene su frase, con la fórmula de su función.','Cada frase tiene sus tres piezas: la fórmula, el dato y un detalle.','Si digo que no, he puesto la excusa (y, si puedo, otra propuesta).','Todo el correo va en el mismo carril, del saludo a la despedida.','He mirado los errores típicos: gracias por, siento + infinitivo, ¡que te mejores!...'];
function grpTxt(g){ return g.split('|').map(function(f){ return D.fn[f].toLowerCase(); }).join(' o '); }
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+' '+lc(L.t)+'</div>';
 h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(g){ return '<span class="vchip '+D.fdir[g.split('|')[0]]+'">'+esc(grpTxt(g))+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas te dicen qué función pide cada pauta. Recuerda: unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu correo</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar mis funciones</button></div><div id="rvbox" aria-live="polite"></div>';
 h+='<h3>Mi lista de las funciones</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
function sents(t){ return t.match(/[^.!?\n]+[.!?]*/g)||[]; }
function detIds(t){ var o={}, ss=sents(t).map(norm); D.detector.forEach(function(d){ var r=new RegExp(d.re); if(d.sc==='s'){ if(ss.some(function(s){ return r.test(s); })) o[d.id]=1; } else if(r.test(norm(t))) o[d.id]=1; }); return Object.keys(o).sort(); }
function funcs(t){ var n=norm(t); return Object.keys(D.funcrx).filter(function(k){ return new RegExp(D.funcrx[k]).test(n); }); }
function carril(t){ var n=norm(t), a=n.match(new RegExp(D.turx,'g'))||[], b=n.match(new RegExp(D.usrx,'g'))||[]; return {tu:a, us:b}; }
window.__R13detect = detIds; window.__R13funcs = funcs; window.__R13carril = carril;
function review(){
 var L=lam(), txt=$('wtext').value, out=[], red=0, amb=0;
 if(txt.trim().length<20){ $('rvbox').innerHTML='<ul class="rv"><li class="a">Escribe primero tu correo.</li></ul>'; return; }
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
 // 3. el carril de la lamina
 var c=carril(txt), otro=L.t==='tu'?c.us:c.tu;
 if(otro.length){ red++; out.push('<li class="r"><b>¡Ojo!</b> La lámina es <b>de '+D.carril[L.t]+'</b>, pero veo palabras del otro carril: <mark>'+esc(otro.slice(0,4).join(', '))+'</mark>. Todo el correo va en el mismo carril (mira la ficha R07).</li>'); }
 // 4. cada pauta, su funcion
 var fs=funcs(txt), falta=0;
 L.pautas.forEach(function(p,i){ p[1].forEach(function(g){ var ok=g.split('|').some(function(f){ return fs.indexOf(f)>=0; }); if(!ok){ amb++; falta++; out.push('<li class="a"><b>Mira esto:</b> la pauta '+(i+1)+' («'+esc(p[0].replace(/;$|\.$/,''))+'») pide <b>'+esc(grpTxt(g))+'</b>, y no veo ninguna fórmula de esa función.</li>'); } }); });
 var wc=txt.trim().split(/\s+/).length;
 if(!red && !amb) out.unshift('<li class="g">Cada pauta tiene su fórmula y no he encontrado errores típicos. ¡Bien! Mira tú también la lista de abajo.</li>');
 else if(!red) out.unshift('<li class="g">No he encontrado errores seguros. Mira los puntos ámbar: son cosas que conviene comprobar.</li>');
 var cn='<div class="cnts">'+D.funcs.map(function(f){ var on=fs.indexOf(f.id)>=0; return '<span class="vchip '+(on?'ok':'no')+'">'+esc(f.n)+'</span>'; }).join('')+'</div>';
 S.wrev[L.id]={red:red, amb:amb, falta:falta, funcs:fs.map(function(k){ return D.fn[k]; }).join(', '), words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul><p class="small"><b>Las funciones que veo en tu correo:</b></p>'+cn+'<p class="muted small">Tu correo: '+wc+' palabras (la lámina pide '+L.palabras[0]+'-'+L.palabras[1]+'). La página no lo ve todo: tu profesora corrige el texto completo.</p>';
}

/* ---------------- relojes ---------------- */
var TM=null;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } }
function clockTxt(s){ s=Math.max(0,Math.ceil(s)); return Math.floor(s/60)+':'+(s%60<10?'0':'')+(s%60); }

/* ---------------- ahora tu: oral, responde rapido ---------------- */
function oNew(){
 var tu=shuffle(D.oral.map(function(o,i){ return o.t==='tu'?i:-1; }).filter(function(i){ return i>=0; }));
 var us=shuffle(D.oral.map(function(o,i){ return o.t==='us'?i:-1; }).filter(function(i){ return i>=0; }));
 var deck=[]; for(var i=0;deck.length<S.oc.n && (i<tu.length||i<us.length);i++){ if(i<tu.length) deck.push(tu[i]); if(deck.length<S.oc.n && i<us.length) deck.push(us[i]); }
 S.ro={deck:shuffle(deck), i:0, ph:0, res:[]}; save();
}
function renderO(){
 var box=$('obox'), R=S.ro, h='';
 if(!R){
  h+='<div class="ocard"><div class="ph1">Prepárate</div><p>Cada tarjeta es una situación, mitad de tú y mitad de usted. Lee, pulsa el reloj y di la frase en voz alta. Después mira el modelo y marca si lo has hecho bien: la fórmula de la función, en su carril, y un detalle.</p>';
  h+='<p class="small"><b>Tarjetas:</b></p><div class="pills">'+[6,10,14].map(function(n){ return '<button class="pill'+(S.oc.n===n?' on':'')+'" data-act="on" data-n="'+n+'">'+n+'</button>'; }).join('')+'</div>';
  h+='<p class="small"><b>Tiempo para contestar:</b></p><div class="pills">'+[6,8,10].map(function(t){ return '<button class="pill'+(S.oc.t===t?' on':'')+'" data-act="ot" data-t="'+t+'">'+t+' s</button>'; }).join('')+'</div>';
  h+='<div class="row"><button class="btn cta" data-act="ostart">Empezar</button></div>';
  if(S.olog.length){ h+='<p class="hist"><b>Tus últimas prácticas:</b> '+S.olog.map(function(r){ return r.d+': '+r.ok+'/'+r.n+' ('+r.t+' s)'; }).join(' · ')+'</p>'; }
  box.innerHTML=h+'</div>'; return;
 }
 var N=R.deck.length;
 if(R.i>=N){
  var ok=R.res.filter(function(r){ return r.ok; }).length;
  h+='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+(ok>=N-1?'¡Muy bien! Tienes las fórmulas a mano y en su carril.':'Vuelve a mirar las diez funciones y repite: las fórmulas tienen que salir solas.')+'</p>';
  var fl=R.res.filter(function(r){ return !r.ok; });
  if(fl.length){ h+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fl.forEach(function(r){ var o=D.oral[r.k]; h+='<li>'+lc(o.t)+' '+esc(o.sit)+'<br><b>'+esc(o.m)+'</b></li>'; }); h+='</ul>'; }
  h+='<div class="row"><button class="btn cta" data-act="oagain">Otra vez</button></div></div>';
  box.innerHTML=h; return;
 }
 var o=D.oral[R.deck[R.i]];
 h+='<div class="ocard"><div class="cnt small muted">Tarjeta '+(R.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(R.i/N*100)+'%"></i></div>';
 h+='<p style="margin:4px 0">'+lc(o.t)+'<span class="vchip '+D.fdir[o.f]+'">'+esc(D.fn[o.f])+'</span></p><div class="sit">'+esc(o.sit)+'</div>';
 if(R.ph===0){
  h+='<p class="small muted">Piensa: ¿qué fórmula de '+esc(D.fn[o.f].toLowerCase())+' usas '+(o.t==='tu'?'con tú':'de usted')+'?</p><div class="row"><button class="btn cta" data-act="ogo">Empezar con el reloj</button></div>';
 } else if(R.ph===1){
  h+='<div class="clock" id="oclk">'+clockTxt(S.oc.t)+'</div><div class="tbar"><i id="obar"></i></div>';
  h+='<div class="row"><button class="btn cta" data-act="oskip">Ya está</button></div>';
 } else {
  h+='<div class="model"><b>Una respuesta modelo</b><br>'+esc(o.m)+'</div>';
  h+='<p class="small" style="margin-top:12px"><b>¿Has dicho la fórmula, en su carril, y un detalle?</b></p>';
  h+='<div class="row"><button class="btn cta" data-act="oeval" data-ok="1">✓ Sí</button><button class="btn" data-act="oeval" data-ok="0">✗ Todavía no</button></div>';
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
function oNext(){ stopTimer(); var R=S.ro; R.ph=2; save(); renderO(); }

/* ---------------- opinion y copiar ---------------- */
function renderOpn(){
 var o=''; for(var i=1;i<=10;i++) o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>';
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked=r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function pack(){
 var L=['CURSO DELE A2 - R13: LAS FUNCIONES DE LOS CORREOS','Nombre: '+(S.name||'-'),''];
 L.push('EJERCICIOS (ultimo resultado)');
 ['p1','p2','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 D.textos.forEach(function(t){
  var f=fbList(t.id,t.texto), errs=[];
  gapInfo(t.id,t.texto).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); });
  var started=Object.keys(S.cz).some(function(k){return k.indexOf(t.id+'-')===0;});
  L.push('- Textos del examen, '+t.titulo+': '+(started?f.first+'/'+f.tot+' a la primera'+(f.done<f.tot?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 L.push('','ORAL: RESPONDE RAPIDO');
 if(!S.olog.length) L.push('sin hacer');
 S.olog.forEach(function(r){ L.push('- '+r.d+': '+r.ok+'/'+r.n+' bien (autoevaluacion), '+r.t+' s'+(r.fails&&r.fails.length?' | a repasar: '+r.fails.join(' / '):'')); });
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' (de '+D.carril[l.t]+', '+l.palabras[0]+'-'+l.palabras[1]+' palabras)','Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision: '+rv.red+' avisos rojos, '+rv.amb+' ambar | pautas sin formula: '+rv.falta+' | funciones: '+(rv.funcs||'-')+' | '+rv.words+' palabras');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. La funcion que mas cuesta: '+(S.o2||'-'),'3. Atras, adelante y contestar: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}
window.__R13pack = pack;

/* ---------------- eventos ---------------- */
var ACTS={
 fn:function(b){ S.fn=b.getAttribute('data-k'); save(); renderFn(); },
 fl:function(b){ S.fl=b.getAttribute('data-k'); save(); renderFn(); },
 cs:function(b){ S.cs=+b.getAttribute('data-i'); S.cp=0; S.cst=1; save(); renderCs(); },
 cl:function(b){ S.cl=b.getAttribute('data-k'); S.cst=1; save(); renderCs(); },
 cp:function(b){ S.cp=+b.getAttribute('data-i'); S.cst=1; save(); renderCs(); },
 cnext:function(){ S.cst=Math.min(3,S.cst+1); save(); renderCs(); },
 creset:function(){ S.cst=1; save(); renderCs(); },
 iv:function(b){ S.iv=+b.getAttribute('data-i'); save(); renderIv(); },
 ia:function(b){ S.ia=b.getAttribute('data-k'); save(); renderIv(); },
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
 oeval:function(b){
  var R=S.ro; R.res.push({k:R.deck[R.i], ok:b.getAttribute('data-ok')==='1'}); R.i++; R.ph=0; save();
  if(R.i>=R.deck.length){
   var ok=R.res.filter(function(r){return r.ok;}).length, d=new Date();
   S.olog.push({d:d.getDate()+'/'+(d.getMonth()+1), n:R.deck.length, t:S.oc.t, ok:ok, fails:R.res.filter(function(r){ return !r.ok; }).map(function(r){ var o=D.oral[r.k]; return D.fn[o.f]+' ('+D.carril[o.t]+')'; })});
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

renderFn(); renderCs(); renderIv(); renderEx(); renderAt(); renderOpn(); go(S.cur);
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
      "| items:", len(B.P_FUNC) + len(B.P_FRASE) + len(B.E_BIENMAL),
      "| pruebas del detector:", len(B.DETECTOR_PRUEBAS), "(navegador: %s)" % ("igual que Python" if NODE_OK else "sin probar"),
      "| buena en el desplegable (1a/2a/3a):", POS_TXT, "| situaciones:", len(B.SITUACIONES), "| tarjetas orales:", len(B.ORAL))
