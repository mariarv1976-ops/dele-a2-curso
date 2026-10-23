# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R10 DEL CURSO DE PREPARACION DELE A2: LO, LA, LE (EL PAQUETE Y EL DESTINATARIO)
# Uso: python3 build_R10_pronombres.py  -> DELEA2_curso_R10_lo_la_le.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# Contenidos: solo en banco_R10_pronombres.py. Este archivo monta la pagina y comprueba el banco.
# Mismo formato y motor que R01-R08: pestanas, correccion inmediata, huecos con motivo (barajado arreglado),
# "Ahora tu" con escritura (detector de pronombres) y oral (contesta sin repetir, con reloj), Tu opinion y Copiar.
# Sin imagenes: todos los dibujos son SVG.
# Enfoque cognitivo: EL PAQUETE Y EL DESTINATARIO (lo/la/los/las y le/les; me/te/nos/os para los dos) y EL IMAN
# (delante del verbo conjugado o pegado al infinitivo, al gerundio y al imperativo afirmativo).
# Solo lo [P] del Plan curricular (GR-06, GR-16): combinaciones, duplicacion e imperativo negativo solo en un recuadro.
import json, os, re, shutil, subprocess, sys, tempfile, unicodedata
from curso_comun import CSS, EMAIL, page
import banco_R10_pronombres as B

TITLE = "Lo, la, le: el paquete y el destinatario"
FILE = "DELEA2_curso_R10_lo_la_le.html"
STORAGE = "dele-a2-curso-R10"

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
MARK = re.compile(r"\[(d|i|m|p):([^\[\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
FAM = B.FAMILIAS
PR = B.PRONOMBRES
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
def plain(s): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", MARK.sub(lambda m: m.group(2), s))).strip()
def filled(s): return re.sub(r"<[^>]+>", " ", GAP.sub(lambda m: m.group(1).split("#")[0].split("|")[0], s))
def low(w): return w.strip(" ,.;:¡!¿?").lower()
PEG = re.compile(r"(?:lo|la|los|las|le|les|me|te|nos|os)$")
INFGER = re.compile(r"(?:ar|er|ir|ando|iendo|yendo)(?:lo|la|los|las|le|les|me|te|nos|os)$")
MONO = {"dame", "dime", "hazlo", "hazla", "ponlo", "ponla", "tenlo", "dile", "dales", "danos"}
ACC = re.compile(r"[áéíóú]")

def chk_marks(s, where, need=0, fams=None):
    rest = MARK.sub("", s)
    if "[" in rest or "]" in rest: err("marca mal cerrada en %s: %s" % (where, s[:80]))
    gs = MARK.findall(s)
    for k, w in gs:
        lw = low(w)
        if k == "p":
            n = norm(lw)
            if " " in lw or not PEG.search(n): err("%s: «%s» no es una palabra con el pronombre pegado" % (where, w))
            elif INFGER.search(n) and re.search(r"(?:ando|iendo|yendo)(?:lo|la|los|las|le|les|me|te|nos|os)$", n) and not ACC.search(lw):
                err("%s: el gerundio con pronombre pegado lleva tilde: %s" % (where, w))
            elif not INFGER.search(n) and n not in MONO and not ACC.search(lw):
                err("%s: el imperativo con pronombre pegado lleva tilde: %s" % (where, w))
        elif lw not in FAM[k]["words"]: err("%s: «%s» no es de la pieza %s" % (where, w, FAM[k]["n"]))
        if fams is not None and k not in fams: err("%s: marca de otra pieza (%s): %s" % (where, k, s[:70]))
    if len(gs) < need: err("%s: hacen falta al menos %d marcas" % (where, need))
    return gs

def pron_of(gs):
    """Los pronombres de una frase marcada (los sueltos y los pegados)."""
    out = []
    for k, w in gs:
        lw = norm(low(w))
        if k == "p": out.append(PEG.search(lw).group(0) if PEG.search(lw) else "")
        else: out.append(lw)
    return out

if list(FAM) != B.ORDEN_FAM: err("FAMILIAS y ORDEN_FAM no coinciden")
for k, f in FAM.items():
    if not (f["n"] and f["txt"]): err("pieza mal definida: " + k)
for k, (f, w, ok) in B.MOTIVOS.items():
    if f not in FAM or not w or not ok: err("motivo mal definido: " + k)
    if isinstance(ok, list):
        for x in ok:
            if x not in FAM[f]["words"]: err("motivo %s: «%s» no es de su pieza" % (k, x))
    else:
        try: re.compile(ok)
        except re.error as e: err("motivo %s: regex mal escrita (%s)" % (k, e))

# 1. El paquete: parejas
for p in B.PAREJAS:
    for side in ("a", "b"):
        d = p[side]
        gs = chk_marks(d["f"], "pareja %s" % p["tema"], 1)
        if d["k"] not in ("d", "i"): err("pareja %s: k es d o i" % p["tema"])
        if d["pron"] not in pron_of(gs): err("pareja %s: la frase %s no lleva %s" % (p["tema"], side, d["pron"]))
        want = {"d": ("d", "m"), "i": ("i", "m")}[d["k"]]
        if not any(k in want for k, _ in gs): err("pareja %s: la frase %s no lleva la pieza de su dibujo" % (p["tema"], side))
        if not (d["verbo"] and d["paq"]): err("pareja %s: faltan el verbo o el paquete del dibujo" % p["tema"])
        if d["k"] == "i" and not d["per"]: err("pareja %s: falta la persona que recibe el paquete" % p["tema"])
    if p["a"]["k"] == p["b"]["k"]: err("pareja %s: las dos frases tienen el mismo papel" % p["tema"])
    if not p.get("expl"): err("pareja sin explicacion: " + p["tema"])
if not any(MARK.search(p[s]["f"]) and MARK.findall(p[s]["f"])[0][0] == "m" for p in B.PAREJAS for s in "ab"): err("parejas: falta una con me/te/nos/os")
chk_marks(B.CON_OK, "con pronombres", 2)

# 2. Donde va
FKEYS = [k for k, _, _ in B.FORMAS]
for v in B.VERBOS:
    if v["pron"] not in PR: err("verbo %s: pronombre desconocido" % v["id"])
    if set(v["f"]) != set(FKEYS): err("verbo %s: tiene que tener todas las formas" % v["id"])
    for fk, ss in v["f"].items():
        want = 2 if fk in ("ira", "tener", "estar") else 1
        if len(ss) != want: err("verbo %s, %s: hacen falta %d frases" % (v["id"], fk, want))
        for s in ss:
            gs = chk_marks(s, "verbo %s %s" % (v["id"], fk), 1)
            if pron_of(gs) != [v["pron"]]: err("verbo %s, %s: la frase lleva otro pronombre: %s" % (v["id"], fk, s))
            peg = [k for k, _ in gs] == ["p"]
            if fk in ("imp_tu", "imp_ud") and not peg: err("verbo %s: el imperativo va pegado: %s" % (v["id"], s))
            if fk in ("pres", "perf", "neg") and peg: err("verbo %s: con %s el pronombre va delante: %s" % (v["id"], fk, s))
        if want == 2 and [MARK.findall(s)[0][0] == "p" for s in ss] != [False, True]: err("verbo %s, %s: primero delante y despues pegado" % (v["id"], fk))
if {v["k"] for v in B.VERBOS} != {"d", "i", "m"}: err("constructor: hacen falta verbos de paquete, de destinatario y con me/te/nos/os")
if set(PR) - {v["pron"] for v in B.VERBOS} - {"me", "te", "os"}: err("constructor: faltan pronombres: %s" % (set(PR) - {v["pron"] for v in B.VERBOS}))

# 3. Lo, la o le
for v, s in B.SOLO_PAQ: chk_marks(s, "solo paquete " + v, 1, "d")
for v, s in B.PAQ_DEST: chk_marks(s, "paquete y destinatario " + v, 1, "i")
for s in B.USTED: chk_marks(s, "usted", 1)
for c, d, s in B.DONDE: chk_marks(s, "donde " + c, 1)
for mal, bien, why in B.ERRORES:
    chk_marks(bien, "errores", 1)
    if plain(bien) == mal or not why: err("error tipico sin correccion o sin porque: " + mal)

# Ejercicios
def chk_opts(it, name):
    o = it["o"]
    if len(o) != 3 or len(set(x.lower() for x in o)) != 3: err("%s: hacen falta 3 opciones distintas: %s" % (name, it["q"][:50]))
    if not it.get("why"): err("%s: item sin explicacion: %s" % (name, it["q"][:50]))
    if it["q"].count("____") != 1: err("%s: un solo ____ por frase: %s" % (name, it["q"][:50]))
def fill(it): return it["q"].replace("____", it["o"][0])
if len(B.P_PRON) < 14: err("P_PRON: al menos 14")
for it in B.P_PRON:
    chk_opts(it, "P_PRON")
    if it["f"] not in ("d", "i", "m"): err("P_PRON: pieza desconocida " + it["q"]); continue
    if it["o"][0].lower() not in FAM[it["f"]]["words"]: err("P_PRON: la buena no es de su pieza: " + it["q"])
    for o in it["o"]:
        if o.lower() not in PR: err("P_PRON: opcion que no es un pronombre: " + o)
if {it["f"] for it in B.P_PRON} != {"d", "i", "m"}: err("P_PRON: tienen que salir las tres piezas")
if {it["o"][0].lower() for it in B.P_PRON} < {"lo", "la", "los", "las", "le", "les"}: err("P_PRON: tienen que salir lo, la, los, las, le y les")
if len(B.P_DONDE) < 12: err("P_DONDE: al menos 12")
for it in B.P_DONDE: chk_opts(it, "P_DONDE")
if len(B.E_BIENMAL) < 14: err("E_BIENMAL: al menos 14")
for it in B.E_BIENMAL:
    if not it.get("why"): err("bien/mal sin explicacion: " + it["q"])
    if it["ok"] not in (0, 1): err("bien/mal: ok debe ser 0 o 1")
    if it["ok"] == 1 and not it.get("fix"): err("bien/mal: frase mal sin correccion: " + it["q"])
    if it["ok"] == 0 and it.get("fix"): err("bien/mal: frase bien con correccion: " + it["q"])
if sum(1 for i in B.E_BIENMAL if i["ok"] == 0) < 5: err("bien/mal: faltan frases bien")

# Textos con huecos
def mot_ok(mot, x):
    ok = B.MOTIVOS[mot][2]
    return x.lower() in ok if isinstance(ok, list) else bool(re.match(ok, x.lower()))
def chk_gaps(t):
    n = 0
    for g in GAP.findall(t["texto"]):
        n += 1
        if "#" not in g: err("hueco sin motivo en %s: %s" % (t["id"], g)); continue
        ops, mot = g.split("#"); ops = ops.split("|")
        if len(ops) != 3 or len(set(o.lower() for o in ops)) != 3: err("hueco sin 3 opciones distintas en %s: %s" % (t["id"], g))
        if mot not in B.MOTIVOS: err("motivo desconocido en %s: %s" % (t["id"], mot)); continue
        if not mot_ok(mot, ops[0]): err("en %s la buena (%s) no es la de su motivo %s" % (t["id"], ops[0], mot))
        if B.MOTIVOS[mot][0] != "p":
            for o in ops:
                if o.lower() not in PR: err("hueco de pronombre con una opcion que no lo es en %s: %s" % (t["id"], o))
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
if {f for L in B.LAMINAS for _, fs in L["pautas"] for f in fs} != set(B.FOCOS): err("las laminas tienen que trabajar todos los focos")
if set(B.FOCO_FAM) != set(B.FOCOS) or set(B.FOCO_FAM.values()) != set(FAM): err("FOCO_FAM mal definido")
if set(B.CUENTA) != set(FAM): err("CUENTA: una regex por pieza")

# Oral
if len(B.ORAL) < 12: err("oral: al menos 12 tarjetas")
for o in B.ORAL:
    chk_marks(o["m"], "oral " + o["q"], 1)
    if not (o["q"].strip() and o["dato"].strip()): err("oral: falta la pregunta o el dato")
if {k for o in B.ORAL for k, _ in MARK.findall(o["m"])} != set(FAM): err("oral: tienen que salir las cuatro piezas")

# [R]: combinaciones de dos pronombres (no pueden salir en lo que se practica)
R_COMBO = re.compile(r"\b(?:me|te|se|nos|os)\s+(?:lo|la|los|las)\b|\b[a-z]+(?:ar|er|ir|ando|iendo|yendo)(?:me|te|se|nos)(?:lo|la|los|las)\b|\b[a-z]+se(?:lo|la|los|las)\b")

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
    if r != norm(r) or "(?<" in r or "(" in r.replace("(?:", "").replace("(?=", "").replace("(?!", ""): err("cuenta no valida para el navegador: " + k)
for k in B.REQ:
    if k not in ids: err("REQ: id desconocido " + k)

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
    if sum(1 for _, e in B.DETECTOR_PRUEBAS if not e) < 12: err("detector: hacen falta al menos 12 pruebas que NO deben saltar")
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
    if not det(B.SIN): err("detector: el texto sin pronombres de «Para qué sirven» tiene que dar un aviso")
    # Nada de lo que la ficha da por bueno puede dar NINGUN aviso ni llevar dos pronombres juntos
    buenos = [plain(p[s]["f"]) for p in B.PAREJAS for s in "ab"] + [plain(B.CON_OK)]
    buenos += [plain(s) for v in B.VERBOS for ss in v["f"].values() for s in ss]
    buenos += [plain(s) for _, s in B.SOLO_PAQ + B.PAQ_DEST] + [plain(s) for s in B.USTED]
    buenos += [plain(s) for _, _, s in B.DONDE] + [x for _, b, _ in B.ERRORES for x in plain(b).split(" O: ")]
    buenos += [i["q"] for i in B.E_BIENMAL if i["ok"] == 0] + [fill(i) for i in B.P_PRON + B.P_DONDE]
    buenos += [filled(t["texto"]) for t in B.TEXTOS] + [plain(o["m"]) for o in B.ORAL] + [L["mensaje"] for L in B.LAMINAS]
    for b in buenos:
        r = det(b)
        if r: err("detector: aviso %s en un texto bueno: %r" % (r, b.strip()[:90]))
        if R_COMBO.search(norm(b)): err("dos pronombres juntos ([R]) en un texto bueno: %r" % b[:80])

# Node: el detector y las cuentas tienen que dar lo mismo en el navegador
NODE_OK = None
if not ERR and shutil.which("node"):
    def cuenta_py(t):
        n = norm(t); return {k: len(re.findall(r, n)) for k, r in B.CUENTA.items()}
    textos_c = [t for t, _ in B.DETECTOR_PRUEBAS] + [plain(o["m"]) for o in B.ORAL] + [filled(t["texto"]) for t in B.TEXTOS]
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
INK = "#14161C"; MUT = "#5E5A55"; NEU = "#F3EFEA"; BAD = "#B3261E"
COL = {"d": ("#0F766E", "#DDF1EE"), "i": ("#6B46C1", "#EEE8FA"), "m": ("#2F7D4F", "#E3F1E8"), "p": ("#C2451E", "#FCE6DC")}

def svg(vb, aria, inner, cls="dg"): return '<svg class="%s" viewBox="%s" role="img" aria-label="%s">%s</svg>' % (cls, vb, aria, inner)
def txt(x, y, s, size=16, col=INK, w="400", anchor="middle", extra=""):
    return '<text x="%s" y="%s" text-anchor="%s" font-size="%s" font-weight="%s" fill="%s"%s>%s</text>' % (x, y, anchor, size, w, col, extra, s)
def head(x, y, d, col, s=9):
    if d == "r": pts = (x, y, x - s * 1.5, y - s, x - s * 1.5, y + s)
    else: pts = (x, y, x + s * 1.5, y - s, x + s * 1.5, y + s)
    return '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>' % (pts + (col,))
def arrow(x1, x2, y, col, w=4):
    return '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%d"/>' % (x1, y, x2 - 10, y, col, w) + head(x2, y, "r", col)
def wrap(s, n=15):
    out, cur = [], ""
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > n: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    if cur: out.append(cur)
    return out[:3]
def labels(cx, cy, s, size=17, col=INK, n=15, w="600"):
    ls = wrap(s, n); y0 = cy - (len(ls) - 1) * (size * 0.62) + size * 0.36; o = ""
    for i, l in enumerate(ls): o += txt(cx, "%.1f" % (y0 + i * size * 1.24), l, size, col, w)
    return o
def rbox(x, y, w, h, fill, stroke, sw=2.5, rx=12):
    return '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, w, h, rx, fill, stroke, sw)
def package(x, y, w, h, col, soft):
    """Una caja con cinta: el paquete."""
    cx = x + w / 2
    o = rbox(x, y, w, h, soft, col, 2.5, 8)
    o += '<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2" opacity=".5"/>' % (cx, y, cx, y + min(12, h / 5), col)
    o += '<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2" opacity=".5"/>' % (cx, y + h - min(12, h / 5), cx, y + h, col)
    o += '<path d="M%.1f,%d c-12,-14 -22,-2 0,0 c22,-2 12,-14 0,0" fill="none" stroke="%s" stroke-width="2.2"/>' % (cx, y, col)
    return o
def person2(cx, cy, col, soft, r=15):
    o = '<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s" stroke-width="2.5"/>' % (cx, cy, r, soft, col)
    o += '<path d="M%d,%d a%d,%d 0 0 1 %d,0 z" fill="%s" stroke="%s" stroke-width="2.5"/>' % (cx - r - 8, cy + r * 2 + 18, r + 8, r + 6, 2 * (r + 8), soft, col)
    return o
def pill(cx, y, s, col, w=None):
    w = w or (len(s) * 10 + 34)
    return rbox(int(cx - w / 2), y, int(w), 28, col, col, 0, 14) + txt(cx, y + 20, s, 16, "#fff", "700")

def icon_svg(k):
    """Dibujo pequeno de cada pieza (tarjetas). 220 x 100."""
    c, s = COL[k]; o = ""
    if k == "d":
        o += rbox(8, 34, 72, 36, NEU, INK, 1.5, 8) + txt(44, 58, "verbo", 14, INK, "600")
        o += arrow(84, 132, 52, c) + package(140, 26, 70, 52, c, s) + txt(175, 94, "lo · la · los · las", 12, c, "700")
    elif k == "i":
        o += rbox(4, 36, 54, 32, NEU, INK, 1.5, 8) + txt(31, 57, "verbo", 12, INK, "600")
        o += arrow(60, 84, 52, MUT, 3) + package(88, 34, 46, 36, COL["d"][0], COL["d"][1])
        o += arrow(138, 168, 52, c) + person2(190, 34, c, s, 11) + txt(190, 96, "le · les", 13, c, "700")
    elif k == "m":
        o += package(18, 38, 56, 40, COL["d"][0], COL["d"][1]) + person2(160, 44, COL["i"][0], COL["i"][1], 10)
        o += pill(46, 2, "te", c, 44) + pill(160, 2, "te", c, 44)
        o += txt(110, 66, "=", 26, c, "700") + txt(110, 97, "sirven para los dos", 12, c, "700")
    else:
        o += '<path d="M14,22 v34 a22,22 0 0 0 44,0 v-34" fill="none" stroke="%s" stroke-width="10"/>' % c
        o += '<line x1="14" y1="22" x2="14" y2="32" stroke="%s" stroke-width="10"/><line x1="58" y1="22" x2="58" y2="32" stroke="%s" stroke-width="10"/>' % (NEU, NEU)
        o += rbox(78, 34, 92, 36, NEU, c, 2.5, 8) + txt(124, 58, "comprar", 15, INK, "600")
        o += rbox(170, 34, 40, 36, s, c, 2.5, 8) + txt(190, 58, "lo", 15, c, "700") + txt(144, 94, "una sola palabra", 12, c, "700")
    return svg("0 0 220 100", "Dibujo: " + FAM[k]["dib"], o, "ic")

def pair_svg(d):
    """El dibujo de una frase: verbo -> paquete (d) o verbo -> paquete -> persona (i). 480 x 175."""
    marks = MARK.findall(d["f"]); fk = marks[0][0] if marks else d["k"]
    c, s = COL[fk]; dc, ds = COL["d"]; ic, isoft = COL["i"]
    if d["k"] == "d":
        o = rbox(8, 54, 140, 66, NEU, INK, 1.8, 10) + labels(78, 87, d["verbo"], 18)
        o += arrow(152, 292, 87, c) + package(300, 44, 172, 86, c, s) + labels(386, 90, d["paq"], 17, INK, 14)
        o += pill(222, 104, "= " + d["pron"], c, 80) + txt(240, 26, "el verbo toca el paquete", 15, c, "700")
    else:
        o = rbox(4, 58, 108, 58, NEU, INK, 1.8, 10) + labels(58, 87, d["verbo"], 17)
        o += arrow(114, 152, 87, MUT, 3) + package(158, 50, 132, 74, dc, ds) + labels(224, 90, d["paq"], 15, INK, 12)
        o += arrow(294, 346, 87, c) + person2(408, 52, c, s, 15) + labels(408, 132, d["per"], 15, INK, 14)
        o += pill(320, 118, "= " + d["pron"], c, 70) + txt(240, 26, "el paquete llega a una persona", 15, c, "700")
    return svg("0 0 480 175", "%s: %s" % ("paquete" if d["k"] == "d" else "paquete y destinatario", plain(d["f"])), o, "dg pr")

def chip_w(t): return int(len(t) * 9.6 + 20)
def iman_svg():
    """Donde va el pronombre: delante del verbo conjugado o pegado. 480 x 360."""
    dc, ds = COL["d"]; pc, ps = COL["p"]
    rows = [
        ("Verbo conjugado: delante", [[("lo", "p"), ("compro", "v")]], False),
        ("Ir a / tener que + infinitivo: delante o pegado", [[("lo", "p"), ("voy a", "v"), ("comprar", "v")], [("voy a", "v"), ("comprar+lo", "j")]], False),
        ("Estar + gerundio: delante o pegado (con tilde)", [[("lo", "p"), ("estoy", "v"), ("comprando", "v")], [("estoy", "v"), ("comprándo+lo", "j")]], False),
        ("Imperativo afirmativo: siempre pegado", [[("cómpra+lo", "j")]], False),
        ("Nunca en medio", [[("voy a", "v"), ("lo", "p"), ("comprar", "v")]], True),
        ("Nunca dos veces", [[("lo", "p"), ("voy a", "v"), ("comprar+lo", "j")]], True),
    ]
    o = ""; y = 30
    for lab, groups, bad in rows:
        o += txt(10, y, ("✗ " if bad else "") + lab, 14, BAD if bad else MUT, "700", "start")
        x = 10; yb = y + 10
        for gi, g in enumerate(groups):
            if gi:
                o += txt(x + 12, yb + 24, "o" if not bad else "·", 15, MUT, "700"); x += 28
            for t, kind in g:
                if kind == "j":
                    a, b = t.split("+"); wa, wb = chip_w(a) - 6, chip_w(b) - 4
                    o += rbox(x, yb, wa + wb, 34, "none", BAD if bad else pc, 3, 9)
                    o += txt(x + wa / 2, yb + 23, a, 16, INK, "600") + rbox(x + wa, yb + 3, wb - 3, 28, ds, dc, 0, 6) + txt(x + wa + (wb - 3) / 2, yb + 23, b, 16, dc, "700")
                    x += wa + wb + 8
                else:
                    w = chip_w(t)
                    fill, st, col = (ds, dc, dc) if kind == "p" else (NEU, "#CFC6BB", INK)
                    if bad and kind == "p": fill, st, col = ("#F8E1DE", BAD, BAD)
                    o += rbox(x, yb, w, 34, fill, st, 2, 9) + txt(x + w / 2, yb + 23, t, 16, col, "700" if kind == "p" else "600")
                    x += w + 6
        y += 70
    return svg("0 0 480 430", "El imán: el pronombre va delante del verbo conjugado o pegado al infinitivo, al gerundio y al imperativo afirmativo", o, "dg pr")

LEG = '<div class="legend">' + "".join('<span><span class="k %s">%s</span> %s</span>' % (k, FAM[k]["n"].lower(), FAM[k]["dib"]) for k in B.ORDEN_FAM) + '</div>'

def cards():
    o = '<div class="cams">'
    for k in B.ORDEN_FAM:
        f = FAM[k]
        o += '<div class="cam c%s">%s<h3>%s</h3><p class="qf">%s</p><p>%s</p></div>' % (k, icon_svg(k), f["n"], f["q"], f["txt"])
    return o + '</div>'

def tabla_dos():
    o = '<div class="duo2"><div class="half"><h4><span class="k d">lo, la, los, las</span> solo un paquete</h4><table class="t">'
    for v, s in B.SOLO_PAQ: o += '<tr><td><b>%s</b></td><td>%s</td></tr>' % (v, mk(s))
    o += '</table></div><div class="half"><h4><span class="k i">le, les</span> paquete + destinatario</h4><table class="t">'
    for v, s in B.PAQ_DEST: o += '<tr><td><b>%s</b></td><td>%s</td></tr>' % (v, mk(s))
    return o + '</table></div></div>'

def losveras():
    o = '<table class="t"><tr><th>Forma</th><th>Qué es</th><th>Ejemplo</th></tr>'
    for w, eq, ej in B.LOS_VERAS: o += '<tr><td><b>%s</b></td><td>%s</td><td><i>%s</i></td></tr>' % (w, eq, ej)
    return o + '</table>'

def donde():
    return "".join('<div class="box"><span class="chip">%s</span><p class="small muted" style="margin:6px 0">%s</p><p style="margin:0">%s</p></div>' % (c, d, mk(s)) for c, d, s in B.DONDE)

def errores():
    o = '<div class="errs">'
    for mal, bien, why in B.ERRORES:
        o += '<div class="err"><div class="mal"><span aria-hidden="true">✗</span> <s>%s</s></div><div class="bien"><span aria-hidden="true">✓</span> %s</div><div class="small muted">%s</div></div>' % (mal, mk(bien), why)
    return o + '</div>'

def nunca():
    return '<ul class="small nunca">' + "".join('<li><span class="mal">✗ %s</span> <span class="muted">(%s)</span></li>' % (a[1:], b) for a, b in B.NUNCA) + '</ul>'

SIN_HTML = re.sub(r"\b(el piso)\b", r'<span class="yy">\1</span>', B.SIN, flags=re.I)

CSS_R = CSS + r"""
:root{--cd:#0F766E;--cd-soft:#DDF1EE;--ci:#6B46C1;--ci-soft:#EEE8FA;--cm:#2F7D4F;--cm-soft:#E3F1E8;--cp:#C2451E;--cp-soft:#FCE6DC}
.k{border-radius:4px;padding:0 3px 1px;border-bottom:3px solid;line-height:1.9}
.k.d{background:var(--cd-soft);border-color:var(--cd)}.k.i{background:var(--ci-soft);border-color:var(--ci)}
.k.m{background:var(--cm-soft);border-color:var(--cm)}.k.p{background:var(--cp-soft);border-color:var(--cp)}
.cams{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin:18px 0}
.nunca{list-style:none;padding-left:4px}.nunca .mal{color:var(--bad);font-weight:600}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px 14px;border-top:6px solid var(--cd)}
.cam.ci{border-top-color:var(--ci)}.cam.cm{border-top-color:var(--cm)}.cam.cp{border-top-color:var(--cp)}
.cam h3{margin:4px 0 2px}.cam p{margin:0;font-size:.95rem}.cam p.qf{color:var(--muted);font-style:italic;margin-bottom:6px}
svg.ic{width:100%;max-width:200px;height:auto;display:block}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.box h4{margin:0 0 4px}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
svg.dg{width:100%;height:auto;display:block;margin:6px 0}
.expl{border-radius:8px;padding:10px 14px;margin-top:6px;background:var(--paper)}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;margin:8px 0}
.res{font-family:Georgia,serif;font-size:1.25rem;font-weight:700;text-align:center;margin:8px 0;line-height:1.8}
.duo2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.stack{display:grid;gap:12px;margin:12px 0}
svg.pr{max-width:560px;margin:6px auto}
.half{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.half .res{font-size:1.08rem;text-align:left}
.half h4{margin:4px 0 6px}
.story{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 16px;line-height:2}
.story .yy,.yy{background:var(--bad-soft);border-bottom:3px solid var(--bad);border-radius:4px;padding:0 3px}
.cv .res{margin:4px 0}
.cv .or{text-align:center;color:var(--muted);font-weight:700;margin:0}
.errs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.err{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.err .mal{color:var(--bad)}.err .bien{margin:4px 0}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.vchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px;background:var(--paper);color:var(--muted)}
.vchip.d{background:var(--cd-soft);color:var(--cd)}.vchip.i{background:var(--ci-soft);color:var(--ci)}
.vchip.m{background:var(--cm-soft);color:var(--cm)}.vchip.p{background:var(--cp-soft);color:var(--cp)}
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
.check{list-style:none;padding:0;margin:8px 0}.check li{padding:5px 0}.check label{cursor:pointer}
.ocard{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin-top:12px}
.ocard .ph1{font-family:Georgia,serif;font-size:1.15rem;font-weight:700}
.sit{font-family:Georgia,serif;font-size:1.3rem;font-weight:700;margin:8px 0;line-height:1.35}
.dato{display:inline-block;background:var(--paper);border:1px dashed #CFC6BB;border-radius:8px;padding:4px 12px;font-weight:600}
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
@media (max-width:700px){.errs,.duo2,.cams{grid-template-columns:1fr}.qz .ops.bm{grid-template-columns:1fr 1fr}table.t{font-size:.88rem}table.t td,table.t th{padding:6px 5px}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:13px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.err,.half{break-inside:avoid}}
"""

STEPS = [("idea", "El paquete"), ("donde", "¿Dónde va?"), ("lole", "¿Lo, la o le?"), ("examen", "En el examen"),
         ("practica", "Practica"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_IDEA = """
<h2>El paquete y el destinatario</h2>
<p class="lead">Piensa en el verbo como en alguien que <b>mueve un paquete</b>. A veces solo hay paquete (compras la tarta, llamas a Ana). Otras veces el paquete <b>le llega a una persona</b> (le compras una tarta a tu madre, le escribes un mensaje a Ana). El paquete y la persona tienen pronombres distintos.</p>
__CARDS__
__LEG__
<h3>Mira la diferencia</h3>
<p class="muted small">Casi las mismas palabras, otro papel... y otro pronombre. Elige una pareja.</p>
<div class="pills" id="parsel"></div>
<div class="box" id="parvis" aria-live="polite"></div>
<h3>¿Para qué sirven?</h3>
<p>Para <b>no repetir</b>. Lee los dos textos: dicen lo mismo.</p>
<div class="duo2"><div class="half"><h4>Sin pronombres</h4><p style="margin:0">__SIN__</p></div><div class="half"><h4>Con pronombres</h4><p style="margin:0">__CON__</p></div></div>
<p class="small muted">Repetir el mismo nombre una y otra vez hace el texto pesado. Los pronombres son una de las formas de unir tus frases, y el examinador lo nota en la escritura y en la oral.</p>
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="donde">Siguiente: ¿dónde va?</button></div>
"""

V_DONDE = """
<h2>¿Dónde va? El imán</h2>
<p class="lead">El pronombre es como un imán: se pega al verbo. Hay dos sitios buenos y nada más: <b>delante</b> del verbo conjugado o <b>pegado al final</b> del infinitivo, del gerundio o del imperativo afirmativo.</p>
__IMAN__
<div class="tip">El truco: busca el <b>verbo conjugado</b> (compro, voy, estoy, tengo, he). El pronombre va justo delante. Si hay un infinitivo o un gerundio, también lo puedes pegar al final. Elige un sitio, solo uno.</div>
<p class="small"><b>Lo que nunca se hace:</b></p>
__NUNCA__
<h3>Pruébalo: monta la frase</h3>
<p class="muted small">Elige qué haces y con qué forma del verbo. Mira dónde va el pronombre.</p>
<div class="pills" id="cvsel"></div>
<div class="pills" id="cfsel"></div>
<div class="box cv" id="cvvis" aria-live="polite"></div>
<div class="note">__REFLEX__</div>
<div class="row"><button class="btn cta" data-go="lole">Siguiente: ¿lo, la o le?</button></div>
"""

V_LOLE = """
<h2>¿Lo, la o le?</h2>
<p class="lead">Dos preguntas, siempre en este orden. Así no tienes que adivinar.</p>
<div class="box"><p style="margin:0 0 8px">__P1__</p><p style="margin:0">__P2__</p></div>
__TABLA__
<p class="small muted">Algunos verbos están en las dos listas: <i>la compro</i> (la tarta) y <i>le compro una tarta</i> (a mi madre). Mira siempre si ya hay otro paquete en la frase.</p>
<h3>En España: «le vi»</h3>
<div class="note">__LEISMO__</div>
<h3>Con usted</h3>
<p>__USTEDT__</p>
<ul>__USTED__</ul>
<details><summary>Lo verás en los textos (no lo necesitas para aprobar)</summary>
<p>En la lectura y en la auditiva salen también estas formas. Está bien entenderlas, pero para escribir y hablar en el A2 tienes bastante con un pronombre cada vez.</p>
__VERAS__</details>
<div class="row"><button class="btn cta" data-go="examen">Siguiente: en el examen</button></div>
"""

V_EXAMEN = """
<h2>Dónde sale en el examen</h2>
<p class="lead">Los pronombres hacen que tus textos y tu oral suenen naturales y no repitan. En la lectura y en la auditiva, una pregunta típica es a quién se refiere un <b>le</b> o un <b>la</b>.</p>
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
 <button class="pill on" data-act="ex" data-k="p1">1. ¿Qué pronombre?</button>
 <button class="pill" data-act="ex" data-k="p2">2. ¿Dónde va?</button>
 <button class="pill" data-act="ex" data-k="e2">3. Textos del examen</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Ahora úsalo en una tarea del examen: escribe un texto o contesta al examinador en voz alta sin repetir.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="o">Oral: contesta sin repetir</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu texto y después pulsa <b>Revisar mis pronombres</b>: la página te avisa de los errores típicos y de los nombres que repites. No corrige el texto entero: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="ato" hidden>
 <p>Como en la tarea 3 de la oral: el examinador te pregunta quién hace cada cosa. Contesta <b>en voz alta</b>, con un pronombre y <b>sin repetir</b> el nombre. El reloj pasa solo.</p>
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
  <label><input type="radio" name="o1" value="El paquete y el destinatario">El paquete y el destinatario</label>
  <label><input type="radio" name="o1" value="El iman (donde va)">El imán (dónde va)</label>
  <label><input type="radio" name="o1" value="Lo, la o le">¿Lo, la o le?</label>
  <label><input type="radio" name="o1" value="En el examen y los errores tipicos">En el examen y los errores típicos</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tu">Ahora tú</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué te cuesta más ahora?</label>
 <div class="chips" role="group" aria-labelledby="o2l">
  <label><input type="radio" name="o2" value="Elegir entre lo / la y le">Elegir entre lo / la y le</label>
  <label><input type="radio" name="o2" value="Donde va el pronombre">Dónde va el pronombre</label>
  <label><input type="radio" name="o2" value="Pegarlo al infinitivo o al imperativo">Pegarlo al infinitivo o al imperativo</label>
  <label><input type="radio" name="o2" value="Usarlos al hablar, rapido">Usarlos al hablar, rápido</label>
  <label><input type="radio" name="o2" value="No repetir los nombres">No repetir los nombres</label>
 </div>
 <label class="q" id="o3l">3. ¿Te ayuda la idea del paquete y el destinatario?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Si, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con lo, la y le? (1 = nada, 10 = total)</label>
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
    o = '<h2>Lo, la, le: el paquete y el destinatario · resumen</h2>' + cards() + LEG
    p = B.PAREJAS[0]
    o += '<h3>Mira la diferencia</h3><div class="stack"><div class="half"><p class="res">%s</p>%s</div><div class="half"><p class="res">%s</p>%s</div></div>' % (
        mk(p["a"]["f"]), pair_svg(p["a"]), mk(p["b"]["f"]), pair_svg(p["b"]))
    o += '<h3>¿Lo, la o le?</h3><div class="box"><p>%s</p><p>%s</p></div>' % tuple(B.DOS_PREGUNTAS) + tabla_dos()
    o += '<h3>¿Dónde va?</h3>' + iman_svg()
    o += '<h3>Los errores típicos</h3>' + errores()
    return o

views = {
    "idea": V_IDEA.replace("__CARDS__", cards()).replace("__LEG__", LEG).replace("__SIN__", SIN_HTML).replace("__CON__", mk(B.CON_OK)),
    "donde": V_DONDE.replace("__IMAN__", iman_svg()).replace("__NUNCA__", nunca()).replace("__REFLEX__", B.REFLEXIVOS),
    "lole": V_LOLE.replace("__P1__", B.DOS_PREGUNTAS[0]).replace("__P2__", B.DOS_PREGUNTAS[1]).replace("__TABLA__", tabla_dos())
                  .replace("__LEISMO__", B.LEISMO).replace("__USTEDT__", B.USTED_TXT).replace("__USTED__", "".join("<li>%s</li>" % mk(s) for s in B.USTED))
                  .replace("__VERAS__", losveras()),
    "examen": V_EXAMEN.replace("__LEG__", LEG).replace("__DONDE__", donde()).replace("__ORO__", B.REGLA_ORO).replace("__ERRORES__", errores()),
    "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R10</small></div>
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
    "fams": {k: FAM[k]["n"] for k in B.ORDEN_FAM}, "order": B.ORDEN_FAM,
    "motivos": {k: {"f": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "parejas": [{"tema": p["tema"], "a": {"f": mk(p["a"]["f"]), "svg": pair_svg(p["a"])}, "b": {"f": mk(p["b"]["f"]), "svg": pair_svg(p["b"])},
                 "expl": p["expl"]} for p in B.PAREJAS],
    "formas": [{"k": k, "l": l, "e": e} for k, l, e in B.FORMAS],
    "verbos": [{"txt": v["txt"], "pron": v["pron"], "k": v["k"], "f": {fk: [mk(s) for s in ss] for fk, ss in v["f"].items()}} for v in B.VERBOS],
    "qz": {
        "p1": {"items": B.P_PRON, "n": 8, "name": "¿Qué pronombre?", "info": "Primero: ¿hay otro paquete en la frase? Si lo hay, la persona es le / les. Si no, mira la camiseta del paquete: lo, la, los, las."},
        "p2": {"items": B.P_DONDE, "n": 8, "name": "¿Dónde va?", "info": "Busca el verbo conjugado: el pronombre va delante. Con infinitivo, gerundio o imperativo, también pegado al final."},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Errores típicos de los exámenes. ¿La frase está bien o el pronombre falla?"},
    },
    "textos": B.TEXTOS,
    "laminas": B.LAMINAS, "focos": B.FOCOS, "focofam": B.FOCO_FAM, "cuenta": B.CUENTA, "detector": B.DETECTOR,
    "oral": [{"q": o["q"], "dato": o["dato"], "m": mk(o["m"])} for o in B.ORAL],
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function blank(){ return {cur:'idea', seen:{}, par:0, cv:0, cf:'ira', ex:'p1', etext:D.textos[0].id, at:'w',
  qz:{}, qlog:{}, cz:{}, w:{}, wchk:{}, wrev:{}, lam:D.laminas[0].id, oc:{n:8,t:8}, ro:null, olog:[],
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

/* ---------------- 1. el paquete: parejas ---------------- */
function renderPar(){
 var o=''; D.parejas.forEach(function(p,i){ o+='<button class="pill'+(S.par===i?' on':'')+'" data-act="par" data-i="'+i+'">'+esc(p.tema)+'</button>'; });
 $('parsel').innerHTML=o;
 var p=D.parejas[S.par];
 $('parvis').innerHTML='<div class="stack"><div class="half"><p class="res">'+p.a.f+'</p>'+p.a.svg+'</div><div class="half"><p class="res">'+p.b.f+'</p>'+p.b.svg+'</div></div><div class="expl">'+p.expl+'</div>';
}
/* ---------------- 2. donde va: constructor ---------------- */
function renderCv(){
 var o=''; D.verbos.forEach(function(v,i){ o+='<button class="pill'+(S.cv===i?' on':'')+'" data-act="cv" data-i="'+i+'">'+esc(v.txt)+'</button>'; });
 $('cvsel').innerHTML=o;
 o=''; D.formas.forEach(function(f){ o+='<button class="pill'+(S.cf===f.k?' on':'')+'" data-act="cf" data-k="'+f.k+'">'+esc(f.l)+'</button>'; });
 $('cfsel').innerHTML=o;
 var v=D.verbos[S.cv], f=D.formas.filter(function(x){ return x.k===S.cf; })[0], ss=v.f[S.cf];
 var h='<p class="small muted" style="margin:0">'+esc(v.txt)+' · '+esc(f.l)+' · pronombre: <b>'+esc(v.pron)+'</b></p>';
 ss.forEach(function(s,i){ if(i) h+='<p class="or">o</p>'; h+='<p class="res">'+s+'</p>'; });
 h+='<div class="expl">'+f.e+'</div>';
 $('cvvis').innerHTML=h;
}

/* ---------------- motor de opcion multiple ---------------- */
function qzNew(k){ var c=D.qz[k]; S.qz[k]={order:shuffle(range(c.items.length)).slice(0,c.n), i:0, res:[], perm:{}}; save(); }
function qHead(k, it){ if(k==='e4') return esc(it.q); return esc(it.q).replace('____','<span class="blank">____</span>'); }
function qzRender(k, box){
 var c=D.qz[k]; if(!S.qz[k]) qzNew(k);
 var st=S.qz[k], N=st.order.length;
 if(st.i>=N){
  var ok=st.res.filter(function(r){return r.ok;}).length, fails=st.res.filter(function(r){return !r.ok;});
  var msg = ok>=N-1 ? '¡Muy bien! Tus pronombres están en su sitio.' : (ok>=Math.ceil(N*0.6) ? 'Bien. Mira otra vez las explicaciones de las que has fallado.' : 'Vuelve a mirar el paquete, el destinatario y el imán, y repite con otras frases.');
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
var EXINFO={e2:'Un correo a una amiga, un blog, un diálogo de la tarea 3 y un correo de usted. Elige el pronombre (o la forma) de cada hueco: la corrección sale enseguida, con el motivo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
var CH=['Cada lo, la, los, las lleva la camiseta de su nombre (masculino o femenino, uno o varios).','Para la persona que recibe algo (le das, le dices, le escribes...), le o les, también para una mujer.','Con el verbo conjugado, el pronombre va delante: lo compro, lo voy a comprar.','Con el infinitivo, el gerundio o el imperativo, también puede ir pegado: comprarlo, comprándolo, cómpralo (¡con tilde!).','No repito el mismo nombre en dos frases seguidas.'];
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+'</div>';
 h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(f){ return '<span class="vchip '+D.focofam[f]+'">'+D.focos[f]+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas te dicen qué pronombre te va a ayudar en cada pauta. Recuerda: unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu texto</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar mis pronombres</button></div><div id="rvbox" aria-live="polite"></div>';
 h+='<h3>Mi lista de los pronombres</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
function sents(t){ return t.match(/[^.!?\n]+[.!?]*/g)||[]; }
function detIds(t){ var o={}, ss=sents(t).map(norm); D.detector.forEach(function(d){ var r=new RegExp(d.re); if(d.sc==='s'){ if(ss.some(function(s){ return r.test(s); })) o[d.id]=1; } else if(r.test(norm(t))) o[d.id]=1; }); return Object.keys(o).sort(); }
function cuenta(t){ var n=norm(t), o={}; D.order.forEach(function(k){ o[k]=(n.match(new RegExp(D.cuenta[k],'g'))||[]).length; }); return o; }
window.__R10detect = detIds; window.__R10cuenta = cuenta;
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
  if(d.sc!=='x') return; var m=new RegExp(d.re).exec(norm(txt)); if(!m) return;
  if(d.t==='r') red++; else amb++;
  out.push('<li class="'+d.t+'">'+(d.t==='r'?'<b>¡Ojo!</b> ':'<b>Mira esto:</b> ')+d.msg+(m[1]?' <span class="small">(«'+esc(m[1])+'»)</span>':'')+'</li>');
 });
 // 3. los pronombres: cuantos y de que tipo (orientativo)
 var c=cuenta(txt), wc=txt.trim().split(/\s+/).length, tot=c.d+c.i+c.p;
 if(wc>=40 && !tot){ amb++; out.push('<li class="a"><b>Mira esto:</b> no veo ningún <b>lo, la, le</b> en tu texto. ¿Hay algún nombre que repites y puedes cambiar?</li>'); }
 L.pautas.forEach(function(p,i){ p[1].forEach(function(f){ var k=D.focofam[f]; if(!c[k]){ amb++; out.push('<li class="a"><b>Mira esto:</b> la pauta '+(i+1)+' («'+esc(p[0].replace(/;$|\.$/,''))+'») va bien con <b>'+D.focos[f]+'</b>, y no lo veo. Puede que la página no lo vea: compruébalo tú.</li>'); } }); });
 if(!red && !amb) out.unshift('<li class="g">No he encontrado errores típicos. ¡Bien! Mira tú también la lista de abajo.</li>');
 else if(!red) out.unshift('<li class="g">No he encontrado errores seguros. Mira los puntos ámbar: son cosas que conviene comprobar.</li>');
 var cn='<div class="cnts">'+D.order.map(function(k){ return '<span class="vchip '+k+'">'+D.fams[k]+': '+c[k]+'</span>'; }).join('')+'</div>';
 S.wrev[L.id]={red:red, amb:amb, cnt:D.order.map(function(k){ return D.fams[k]+' '+c[k]; }).join(', '), words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul><p class="small"><b>Tus pronombres</b> (cuenta aproximada):</p>'+cn+'<p class="muted small">Tu texto: '+wc+' palabras (la lámina pide '+L.palabras[0]+'-'+L.palabras[1]+'). La página no lo ve todo: tu profesora corrige el texto completo.</p>';
}

/* ---------------- relojes ---------------- */
var TM=null;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } }
function clockTxt(s){ s=Math.max(0,Math.ceil(s)); return Math.floor(s/60)+':'+(s%60<10?'0':'')+(s%60); }

/* ---------------- ahora tu: oral, contesta sin repetir ---------------- */
function oNew(){ S.ro={deck:shuffle(range(D.oral.length)).slice(0,S.oc.n), i:0, ph:1, res:[]}; save(); }
function renderO(){
 var box=$('obox'), R=S.ro, h='';
 if(!R){
  h+='<div class="ocard"><div class="ph1">Prepárate</div><p>En cada tarjeta, el examinador te hace una pregunta y tú ves lo que tienes que contestar. Contesta en voz alta con <b>un pronombre</b> y sin repetir el nombre: <i>—¿Quién compra el pan? —Lo compro yo.</i> Después, compara con la respuesta modelo.</p>';
  h+='<p class="small"><b>Tarjetas:</b></p><div class="pills">'+[8,12,16].map(function(n){ return '<button class="pill'+(S.oc.n===n?' on':'')+'" data-act="on" data-n="'+n+'">'+n+'</button>'; }).join('')+'</div>';
  h+='<p class="small"><b>Tiempo para contestar:</b></p><div class="pills">'+[6,8,10].map(function(t){ return '<button class="pill'+(S.oc.t===t?' on':'')+'" data-act="ot" data-t="'+t+'">'+t+' s</button>'; }).join('')+'</div>';
  h+='<div class="row"><button class="btn cta" data-act="ostart">Empezar</button></div>';
  if(S.olog.length){ h+='<p class="hist"><b>Tus últimas prácticas:</b> '+S.olog.map(function(r){ return r.d+': '+r.ok+'/'+r.n+' ('+r.t+' s)'; }).join(' · ')+'</p>'; }
  box.innerHTML=h+'</div>'; return;
 }
 var N=R.deck.length;
 if(R.i>=N){
  var ok=R.res.filter(function(r){ return r.ok; }).length;
  h+='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+(ok>=N-1?'¡Muy bien! Contestas rápido y sin repetir.':'Vuelve a mirar el imán y el paquete, y repite: ¡cada vez saldrá más rápido!')+'</p>';
  var fl=R.res.filter(function(r){ return !r.ok; });
  if(fl.length){ h+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fl.forEach(function(r){ var o=D.oral[r.k]; h+='<li>'+esc(o.q)+' → '+o.m+'</li>'; }); h+='</ul>'; }
  h+='<div class="row"><button class="btn cta" data-act="oagain">Otra vez</button></div></div>';
  box.innerHTML=h; return;
 }
 var o=D.oral[R.deck[R.i]];
 h+='<div class="ocard"><div class="cnt small muted">Tarjeta '+(R.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(R.i/N*100)+'%"></i></div>';
 h+='<p class="small muted" style="margin:0">El examinador:</p><div class="sit">'+esc(o.q)+'</div><p style="margin:4px 0">Tú dices: <span class="dato">'+esc(o.dato)+'</span></p>';
 if(R.ph===1){
  h+='<div class="clock" id="oclk">'+clockTxt(S.oc.t)+'</div><div class="tbar"><i id="obar"></i></div>';
  h+='<div class="row"><button class="btn cta" data-act="oskip">Ya está</button></div>';
 } else {
  h+='<div class="model"><b>Respuesta modelo</b><br>'+o.m+'</div>';
  h+='<p class="small" style="margin-top:12px"><b>¿Has contestado con un pronombre en su sitio, sin repetir el nombre?</b></p>';
  h+='<div class="row"><button class="btn cta" data-act="oeval" data-v="1">✓ Sí</button><button class="btn" data-act="oeval" data-v="0">✗ No</button></div>';
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
 var L=['CURSO DELE A2 - R10: LO, LA, LE','Nombre: '+(S.name||'-'),''];
 L.push('EJERCICIOS (ultimo resultado)');
 ['p1','p2','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 D.textos.forEach(function(t){
  var f=fbList(t.id,t.texto), errs=[];
  gapInfo(t.id,t.texto).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); });
  var started=Object.keys(S.cz).some(function(k){return k.indexOf(t.id+'-')===0;});
  L.push('- Textos del examen, '+t.titulo+': '+(started?f.first+'/'+f.tot+' a la primera'+(f.done<f.tot?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 L.push('','ORAL: CONTESTA SIN REPETIR');
 if(!S.olog.length) L.push('sin hacer');
 S.olog.forEach(function(r){ L.push('- '+r.d+': '+r.ok+'/'+r.n+' bien (autoevaluacion), '+r.t+' s'+(r.fails&&r.fails.length?' | fallos: '+r.fails.join(' / '):'')); });
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' ('+l.palabras[0]+'-'+l.palabras[1]+' palabras)','Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision: '+rv.red+' avisos rojos, '+rv.amb+' ambar | pronombres: '+rv.cnt+' | '+rv.words+' palabras');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. Lo que mas cuesta: '+(S.o2||'-'),'3. El paquete y el destinatario: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}
window.__R10pack = pack;

/* ---------------- eventos ---------------- */
var ACTS={
 par:function(b){ S.par=+b.getAttribute('data-i'); save(); renderPar(); },
 cv:function(b){ S.cv=+b.getAttribute('data-i'); save(); renderCv(); },
 cf:function(b){ S.cf=b.getAttribute('data-k'); save(); renderCv(); },
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
 ostart:function(){ oNew(); oRun(); },
 oskip:function(){ oNext(); },
 oeval:function(b){
  var R=S.ro; R.res.push({k:R.deck[R.i], ok:b.getAttribute('data-v')==='1'}); R.i++; R.ph=1; save();
  if(R.i>=R.deck.length){
   var ok=R.res.filter(function(r){return r.ok;}).length, d=new Date();
   S.olog.push({d:d.getDate()+'/'+(d.getMonth()+1), n:R.deck.length, t:S.oc.t, ok:ok, fails:R.res.filter(function(r){ return !r.ok; }).map(function(r){ return D.oral[r.k].q; })});
   if(S.olog.length>6) S.olog=S.olog.slice(-6);
   save(); nav(); renderO(); return;
  }
  oRun();
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
 if(S.at==='w') renderLam();
 else if(S.ro && S.ro.i<S.ro.deck.length && S.ro.ph===1) oRun();
 else renderO();
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

renderPar(); renderCv(); renderEx(); renderOpn(); go(S.cur);
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
      "| items:", len(B.P_PRON) + len(B.P_DONDE) + len(B.E_BIENMAL),
      "| pruebas del detector:", len(B.DETECTOR_PRUEBAS), "(navegador: %s)" % ("igual que Python" if NODE_OK else "sin probar"),
      "| buena en el desplegable (1a/2a/3a):", POS_TXT, "| parejas:", len(B.PAREJAS), "| verbos del iman:", len(B.VERBOS), "| tarjetas orales:", len(B.ORAL))
