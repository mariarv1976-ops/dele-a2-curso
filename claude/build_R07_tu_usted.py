# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R07 DEL CURSO DE PREPARACION DELE A2: TU Y USTED, REGISTRO COHERENTE DEL SALUDO A LA DESPEDIDA
# Uso: python3 build_R07_tu_usted.py  -> DELEA2_curso_R07_tu_usted.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# Contenidos: solo en banco_R07_tu_usted.py. Este archivo monta la pagina y comprueba el banco.
# Mismo formato y motor que R01-R06: pestanas, correccion inmediata, huecos con motivo (barajado arreglado),
# "Ahora tu" con escritura (detector de mezcla tu / usted) y oral (la misma peticion dos veces, con reloj),
# Tu opinion y Copiar. Sin imagenes: todos los dibujos son SVG.
# Enfoque cognitivo: LA DISTANCIA Y EL CARRIL. Cerca -> tu; un paso de distancia -> usted, que habla como
# "el / ella" (tiene, le, su); al saludar eliges carril y no lo cambias hasta la despedida.
import json, os, re, shutil, subprocess, sys, tempfile, unicodedata
from curso_comun import CSS, EMAIL, page
import banco_R07_tu_usted as B

TITLE = "Tú y usted"
FILE = "DELEA2_curso_R07_tu_usted.html"
STORAGE = "dele-a2-curso-R07"

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
MARK = re.compile(r"\[(t|u|n):([^\[\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
def plain(s): return re.sub(r"<[^>]+>", " ", MARK.sub(lambda m: m.group(2), s)).replace("  ", " ")
def filled(s): return re.sub(r"<[^>]+>", " ", GAP.sub(lambda m: m.group(1).split("#")[0].split("|")[0], s))

def chk_marks(s, where, only=None, need=0):
    rest = MARK.sub("", s)
    if "[" in rest or "]" in rest: err("marca mal cerrada en %s: %s" % (where, s[:80]))
    gs = MARK.findall(s)
    if only is not None and any(k not in only for k, _ in gs): err("%s: marcas de otro carril (solo %s): %s" % (where, "/".join(only), s[:80]))
    if len(gs) < need: err("%s: hacen falta al menos %d marcas" % (where, need))
    return gs

TU_C = [re.compile(r) for r in B.TU_RX]
US_C = [re.compile(r) for r in B.US_RX]
def words(txt, lst): n = norm(txt); return [m.group(0) for r in lst for m in r.finditer(n)]
def has_tu(txt): return bool(words(txt, TU_C))
def has_us(txt): return bool(words(txt, US_C))

for k, (c, w, ok) in B.MOTIVOS.items():
    if c not in B.CARRILES or not w or not ok: err("motivo mal definido: " + k)

# 1. La distancia
if {p[1] for p in B.PERSONAS} != {"tu", "usted"}: err("personas: hacen falta de tu y de usted")
for q, c, why in B.PERSONAS:
    if c not in B.CARRILES or not why: err("persona mal definida: " + q)
for q, c, d in B.LAMINA_DICE:
    if c not in B.CARRILES: err("lamina_dice: carril desconocido " + q)
for a, b, c in B.EL_ELLA:
    chk_marks(a, "el/ella tu", "t", 1); chk_marks(b, "el/ella usted", "u", 1); chk_marks(c, "el/ella el", "u", 1)
for a, b in B.FIJAS: chk_marks(a, "fijas tu", "t", 1); chk_marks(b, "fijas usted", "u", 1)
# 2. El carril
for p, a, b in B.CAMBIA: chk_marks(a, "cambia " + p, "t", 1); chk_marks(b, "cambia " + p, "u", 1)
chk_marks(B.PARA_LOS_DOS, "para los dos", "n", 2)
for f in B.FRASES_CARRIL:
    gt = chk_marks(f["t"], "frase %s tu" % f["tema"], "t", 1); gu = chk_marks(f["u"], "frase %s usted" % f["tema"], "u", 1)
    if len(gt) != len(gu): err("frase %s: las dos versiones tienen que tener las mismas piezas marcadas" % f["tema"])
    if MARK.sub("#", f["t"]) != MARK.sub("#", f["u"]): err("frase %s: fuera de las marcas, las dos versiones tienen que ser iguales" % f["tema"])
    if has_us(plain(f["t"])) or has_tu(plain(f["u"])): err("frase %s: palabras del otro carril" % f["tema"])
# 3. Los correos
for k, only in (("tu", "t"), ("usted", "u"), ("dos", "n")):
    for x in B.SALUDOS[k] + B.DESPEDIDAS[k]: chk_marks(x, "saludos/despedidas " + k, only, 1)
for k, only in (("tu", "tn"), ("usted", "un")):
    t = B.DOS_CORREOS[k]["texto"]; chk_marks(t, "dos correos " + k, only, 5)
    nw = len(plain(t).split())
    if not 55 <= nw <= 75: err("dos correos %s: %d palabras (55-75)" % (k, nw))
if has_us(plain(B.DOS_CORREOS["tu"]["texto"])) or has_tu(plain(B.DOS_CORREOS["usted"]["texto"])): err("dos correos: palabras del otro carril")
# 4. En el examen
for c, d, s in B.DONDE: chk_marks(s, "donde " + c, None, 1)
for mal, bien, why in B.ERRORES:
    chk_marks(bien, "errores", None, 1)
    if plain(bien).strip() == mal or not why: err("error tipico sin correccion o sin porque: " + mal)
for k in B.REQ:
    if not any(k in m.lower() for m, _, _ in B.ERRORES): err("falta el error tipico: " + k)

# Ejercicios
def chk_opts(it, name):
    o = it["o"]
    if len(o) != 3 or len(set(x.lower() for x in o)) != 3: err("%s: hacen falta 3 opciones distintas: %s" % (name, it["q"][:50]))
    if not it.get("why"): err("%s: item sin explicacion: %s" % (name, it["q"][:50]))
if len(B.P_DICES) < 12: err("P_DICES: al menos 12")
for it in B.P_DICES:
    chk_opts(it, "P_DICES")
    if it["c"] not in B.CARRILES: err("P_DICES: carril desconocido " + it["q"]); continue
    good, otro, mez = it["o"]
    if (it["c"] == "tu" and has_us(good)) or (it["c"] == "usted" and has_tu(good)): err("P_DICES: la buena tiene palabras del otro carril: " + good)
    if not (has_tu(mez) and has_us(mez)): err("P_DICES: la opcion mezcla no mezcla (o el detector no la ve): " + mez)
    if (it["c"] == "tu" and has_tu(otro)) or (it["c"] == "usted" and has_us(otro)): err("P_DICES: la opcion del otro carril tiene palabras del bueno: " + otro)
if {it["c"] for it in B.P_DICES} != {"tu", "usted"}: err("P_DICES: hacen falta de tu y de usted")
if len(B.P_CARRIL) < 10: err("P_CARRIL: al menos 10")
for it in B.P_CARRIL:
    chk_opts(it, "P_CARRIL")
    if it["d"] not in B.CARRILES: err("P_CARRIL: carril desconocido " + it["q"]); continue
    if (it["d"] == "usted" and has_tu(it["o"][0])) or (it["d"] == "tu" and has_us(it["o"][0])): err("P_CARRIL: la buena tiene palabras del carril de antes: " + it["o"][0])
if {it["d"] for it in B.P_CARRIL} != {"tu", "usted"}: err("P_CARRIL: hacen falta cambios hacia los dos carriles")
if len(B.E_BIENMAL) < 12: err("E_BIENMAL: al menos 12")
for it in B.E_BIENMAL:
    if not it.get("why"): err("bien/mal sin explicacion: " + it["q"])
    if it["ok"] not in (0, 1): err("bien/mal: ok debe ser 0 o 1")
    if it["ok"] == 1 and not it.get("fix"): err("bien/mal: frase mal sin correccion: " + it["q"])
    if it["ok"] == 0 and it.get("fix"): err("bien/mal: frase bien con correccion: " + it["q"])
if not any(i["ok"] == 0 for i in B.E_BIENMAL): err("bien/mal: faltan frases bien")
for k in B.REQ:
    if not any(k in i["q"].lower() and i["ok"] == 1 for i in B.E_BIENMAL): err("bien/mal: falta el error tipico " + k)

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
        if B.MOTIVOS[mot][0] != t["c"]: err("en %s (carril %s) hay un hueco del otro carril: %s" % (t["id"], t["c"], g))
    if n < 5: err("texto con pocos huecos: " + t["id"])
    if "[[" in GAP.sub("", t["texto"]) or "]]" in GAP.sub("", t["texto"]): err("hueco mal cerrado en " + t["id"])
    return n
ngaps = {t["id"]: chk_gaps(t) for t in B.TEXTOS}
usados = {g.split("#")[1] for t in B.TEXTOS for g in GAP.findall(t["texto"])}
for m in B.MOTIVOS:
    if m not in usados: err("los textos no usan el motivo " + m)
if {t["c"] for t in B.TEXTOS} != {"tu", "usted"}: err("textos: hacen falta de tu y de usted")
for t in B.TEXTOS:
    f = filled(t["texto"])
    if (t["c"] == "tu" and has_us(f)) or (t["c"] == "usted" and has_tu(f)): err("texto %s relleno: palabras del otro carril %s" % (t["id"], words(f, US_C if t["c"] == "tu" else TU_C)))

for L in B.LAMINAS:
    if len(L["pautas"]) != 5: err("lamina %s: 5 pautas" % L["id"])
    if L["c"] not in B.CARRILES: err("lamina %s: carril" % L["id"])
    for _, fs in L["pautas"]:
        for f in fs:
            if f not in B.FOCOS: err("foco desconocido en lamina " + L["id"])
if {f for L in B.LAMINAS for _, fs in L["pautas"] for f in fs} != set(B.FOCOS): err("las laminas tienen que trabajar todos los focos")
if {L["c"] for L in B.LAMINAS} != {"tu", "usted"}: err("laminas: una de tu y otra de usted")

# Oral
if len(B.ORAL) < 12: err("oral: al menos 12 tarjetas")
for o in B.ORAL:
    chk_marks(o["mt"], "oral tu " + o["sit"], "t", 1); chk_marks(o["mu"], "oral usted " + o["sit"], "u", 1)
    if has_us(plain(o["mt"])) or has_tu(plain(o["mu"])): err("oral %s: palabras del otro carril" % o["sit"])
    if not (o.get("a") and o.get("b")): err("oral sin a quien: " + o["sit"])

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
for r in B.TU_RX + B.US_RX:
    if r != norm(r) or "(?<" in r: err("marcador no valido para el navegador: " + r)

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
    for k in B.REQ:
        if not any(k in t.lower() and e for t, e in B.DETECTOR_PRUEBAS): err("detector: ninguna prueba con el error tipico " + k)
    for mal, _, _ in B.ERRORES:
        if not det(mal): err("detector: no ve el error tipico «%s»" % mal)
    for it in B.E_BIENMAL:
        if it["ok"] == 1 and not det(it["q"]): err("detector: no ve la frase mala «%s»" % it["q"])
    for it in B.P_DICES:
        if not det(it["o"][2], True): err("detector: no da aviso rojo con la opcion que mezcla «%s»" % it["o"][2])
    # Nada de lo que la ficha da por bueno puede dar un aviso rojo (textos enteros: tambien los avisos del texto)
    enteros = [plain(B.DOS_CORREOS[k]["texto"]) for k in B.DOS_CORREOS] + [plain(b) for _, b, _ in B.ERRORES]
    enteros += [filled(t["texto"]) for t in B.TEXTOS] + [L["mensaje"] for L in B.LAMINAS]
    enteros += [i["q"] for i in B.E_BIENMAL if i["ok"] == 0] + [it["o"][0] for it in B.P_DICES + B.P_CARRIL]
    enteros += [plain(o["mt"]) for o in B.ORAL] + [plain(o["mu"]) for o in B.ORAL]
    enteros += [plain(f["t"]) for f in B.FRASES_CARRIL] + [plain(f["u"]) for f in B.FRASES_CARRIL]
    enteros += [plain(x) for k in ("tu", "usted", "dos") for x in B.SALUDOS[k] + B.DESPEDIDAS[k]]
    for b in enteros:
        r = det(b, True)
        if r: err("detector: aviso rojo %s en un texto bueno: %r" % (r, b.strip()[:90]))
    # Las tablas mezclan columnas a proposito: solo se miran las columnas por separado y los avisos de frase.
    for _, _, s in B.DONDE:
        for sent in SENT.findall(plain(s)):
            r = [x for x in det(sent, True) if x in {d["id"] for d in B.DETECTOR if d["sc"] == "s"}]
            if r: err("detector: aviso rojo %s en un ejemplo: %r" % (r, sent))

# Node: el detector tiene que dar lo mismo en el navegador (frase a frase + texto entero, como la pagina)
NODE_OK = None
if not ERR and shutil.which("node"):
    js_t = ("var D=%s;function norm(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}"
            "function det(t){var o={},ss=(t.match(/[^.!?\\n]+[.!?]*/g)||[]).map(norm);D.d.forEach(function(d){var r=new RegExp(d.re);"
            "if(d.sc==='s'){if(ss.some(function(s){return r.test(s);}))o[d.id]=1;}else if(r.test(norm(t)))o[d.id]=1;});return Object.keys(o).sort();}"
            "var bad=[];D.p.forEach(function(p){var ids=det(p[0]);if(ids.join()!==p[1].slice().sort().join())bad.push(p[0]+' -> '+ids.join());});"
            "console.log(JSON.stringify(bad));") % json.dumps(
        {"d": [{"id": d["id"], "re": d["re"], "sc": d["sc"]} for d in B.DETECTOR], "p": B.DETECTOR_PRUEBAS}, ensure_ascii=False)
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
COL = {"t": ("#C05621", "#FDEBDD"), "u": ("#1D5FA8", "#E2ECF8"), "n": ("#2F7D4F", "#E3F1E8")}

def svg(vb, aria, inner, cls="dg"): return '<svg class="%s" viewBox="%s" role="img" aria-label="%s">%s</svg>' % (cls, vb, aria, inner)
def txt(x, y, s, size=16, col=INK, w="400", anchor="middle", extra=""):
    return '<text x="%s" y="%s" text-anchor="%s" font-size="%s" font-weight="%s" fill="%s"%s>%s</text>' % (x, y, anchor, size, w, col, extra, s)
def person(x, y, s=1.0, col=INK, fill="#fff"):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="2.5"/>'
            '<path d="M%.1f,%.1f q%.1f,%.1f %.1f,0" fill="%s" stroke="%s" stroke-width="2.5"/>') % (
        x, y, 13 * s, fill, col, x - 22 * s, y + 46 * s, 22 * s, -32 * s, 44 * s, fill, col)
def bubble(x, y, w, s, col, soft):
    return ('<rect x="%d" y="%d" width="%d" height="34" rx="12" fill="%s" stroke="%s" stroke-width="2"/>' % (x - w / 2, y, w, soft, col)) + txt(x, y + 23, s, 15, INK, "700")

def dist_svg(k):
    """La distancia: cerca (tu) o a un paso, con un mostrador en medio (usted). 640 x 210."""
    if k == "t":
        c, s = COL["t"]
        o = '<ellipse cx="320" cy="120" rx="150" ry="78" fill="%s" stroke="%s" stroke-width="2" stroke-dasharray="7 5"/>' % (s, c)
        o += person(270, 98) + person(370, 98)
        o += bubble(320, 18, 210, "¿Tienes un momento?", c, "#fff")
        o += txt(320, 204, "CERCA → TÚ", 17, c, "700")
        return svg("0 0 640 210", "Tú: dos personas cerca, dentro del mismo círculo", o)
    c, s = COL["u"]
    o = person(140, 98) + person(500, 98)
    o += '<rect x="265" y="118" width="110" height="60" rx="6" fill="%s" stroke="%s" stroke-width="2.5"/>' % (s, c) + txt(320, 154, "mostrador", 13, MUT)
    o += '<line x1="180" y1="92" x2="460" y2="92" stroke="%s" stroke-width="2.5" stroke-dasharray="6 5"/>' % c
    o += '<polygon points="176,92 190,85 190,99" fill="%s"/><polygon points="464,92 450,85 450,99" fill="%s"/>' % (c, c)
    o += txt(320, 84, "un paso de distancia", 14, c, "700")
    o += bubble(320, 18, 200, "¿Tiene un momento?", c, "#fff")
    o += txt(320, 204, "A UN PASO → USTED", 17, c, "700")
    return svg("0 0 640 210", "Usted: dos personas con un mostrador en medio, a un paso de distancia", o)

def el_svg():
    """Tres casillas: yo, tu (cerca), el / ella (lejos). Usted se pone en la casilla de el y te mira."""
    ct, st = COL["t"]; cu, su = COL["u"]
    o = ""
    for x, lab, sub, col, soft in ((90, "YO", "tengo", INK, "#fff"), (300, "TÚ", "tienes", ct, st), (530, "ÉL / ELLA", "tiene", cu, su)):
        o += '<rect x="%d" y="40" width="150" height="150" rx="16" fill="%s" stroke="%s" stroke-width="2.5"/>' % (x - 75, soft, col)
        o += txt(x, 30, lab, 15, col, "700") + txt(x, 182, sub, 17, col, "700")
    o += person(90, 86) + person(300, 86, 1, ct)
    o += person(530, 86, 1, cu, su)
    o += txt(530, 152, "USTED", 13, cu, "700")
    o += '<path d="M500,14 C430,-40 160,-40 110,14" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="6 5"/>' % cu
    o += '<polygon points="106,20 106,4 118,12" fill="%s"/>' % cu
    o += txt(310, 236, "Usted se pone en la casilla de «él / ella», pero te habla a ti.", 15, MUT)
    return svg("0 -36 640 286", "Yo, tú y él o ella: usted se pone en la casilla de él o ella y usa sus formas: tiene, le, su", o)

SIGNS = ["SALUDO", "VERBO", "TE / LE", "TU / SU", "¿Y TÚ?", "DESPEDIDA"]
def road_svg(lane=None, crash=True):
    """El carril: dos carriles del saludo a la despedida, con las senales. lane = t / u / None."""
    ct, st = COL["t"]; cu, su = COL["u"]
    o = '<rect x="20" y="60" width="600" height="56" fill="%s"/><rect x="20" y="116" width="600" height="56" fill="%s"/>' % (st, su)
    o += '<line x1="20" y1="116" x2="620" y2="116" stroke="#fff" stroke-width="4" stroke-dasharray="18 12"/>'
    o += txt(30, 94, "TÚ", 15, ct, "700", "start") + txt(30, 150, "USTED", 15, cu, "700", "start")
    for i, s in enumerate(SIGNS):
        x = 150 + i * 86
        o += '<line x1="%d" y1="56" x2="%d" y2="176" stroke="#fff" stroke-width="2"/>' % (x, x)
        o += '<rect x="%d" y="18" width="80" height="28" rx="6" fill="%s"/>' % (x - 40, INK) + txt(x, 37, s, 11, "#fff", "700")
    def car(x, y, col):
        return '<rect x="%d" y="%d" width="46" height="26" rx="8" fill="%s"/><circle cx="%d" cy="%d" r="5" fill="%s"/><circle cx="%d" cy="%d" r="5" fill="%s"/>' % (
            x, y, col, x + 11, y + 26, INK, x + 35, y + 26, INK)
    if lane in ("t", "u"):
        y = 74 if lane == "t" else 130; col = ct if lane == "t" else cu
        o += '<line x1="110" y1="%d" x2="560" y2="%d" stroke="%s" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>' % (y + 13, y + 13, col)
        o += car(566, y, col)
        aria = "El coche va por el carril de %s del saludo a la despedida" % ("tú" if lane == "t" else "usted")
    else:
        o += car(70, 74, ct)
        o += '<path d="M120,87 C220,87 260,87 300,100 S360,140 420,143" fill="none" stroke="#B3261E" stroke-width="3" stroke-dasharray="4 7"/>'
        o += car(424, 130, "#B3261E")
        o += '<circle cx="330" cy="116" r="15" fill="#B3261E"/>' + txt(330, 122, "✗", 17, "#fff", "700")
        o += txt(330, 200, "Cambiar de carril a mitad del camino = el error", 15, "#B3261E", "700")
        aria = "El carril: del saludo a la despedida hay dos carriles; cambiar de carril a mitad es el error"
    return svg("0 0 640 210", aria, o)

LEG = ('<div class="legend"><span><span class="k t">tú</span> cerca</span><span><span class="k u">usted</span> a un paso: habla como «él»</span>'
       '<span><span class="k n">para los dos</span></span></div>')

CARDS = [("t", "La distancia", "Antes de saludar, mira el hueco entre tú y la otra persona. Cerca: <b>tú</b>. A un paso (un servicio, alguien mayor que no conoces, un correo formal): <b>usted</b>."),
         ("u", "Usted habla como «él»", "Usted es la persona que pones un paso más allá, en la casilla de <b>él / ella</b>. Por eso sus formas son las de él: <b>tiene</b>, <b>le</b>, <b>su</b>."),
         ("n", "El carril", "Al saludar eliges carril. Verbo, pronombres, posesivos, perdona / perdone, ¿y tú? / ¿y usted?: todo en el mismo carril <b>hasta la despedida</b>.")]
def cards():
    o = '<div class="cams">'
    for k, h, p in CARDS:
        o += '<div class="cam c%s"><h3>%s</h3><p>%s</p></div>' % (k, h, p)
    return o + '</div>'

def tabla(rows, heads):
    o = '<table class="t"><tr>%s</tr>' % "".join("<th>%s</th>" % h for h in heads)
    for r in rows: o += "<tr>%s</tr>" % "".join("<td>%s</td>" % mk(x) for x in r)
    return o + "</table>"

def lamina_dice():
    o = '<div class="lado">'
    for q, c, d in B.LAMINA_DICE:
        o += '<div class="%s"><span class="chip">%s</span><p style="margin:6px 0 4px"><i>%s</i></p><p style="margin:0">→ <b class="k %s">%s</b></p></div>' % (
            c, d, q, "t" if c == "tu" else "u", "tú" if c == "tu" else "usted")
    return o + '</div>'

def correos():
    o = '<div class="lado">'
    for k, h in (("tu", "Tú"), ("usted", "Usted"), ("dos", "Para los dos")):
        o += '<div class="%s"><h4>%s</h4><p class="small muted" style="margin:0 0 4px">Saludo</p><ul>%s</ul><p class="small muted" style="margin:6px 0 4px">Despedida</p><ul>%s</ul></div>' % (
            k, h, "".join("<li>%s</li>" % mk(x) for x in B.SALUDOS[k]), "".join("<li>%s</li>" % mk(x) for x in B.DESPEDIDAS[k]))
    return o + '</div>'

def dos_correos():
    o = '<div class="duo2">'
    for k in ("tu", "usted"):
        c = B.DOS_CORREOS[k]
        o += '<div class="mail %s"><div class="h">%s</div><div class="body">%s</div><p class="small muted" style="margin:6px 0 0">%d palabras</p></div>' % (
            k, c["para"], mk(c["texto"]), len(plain(c["texto"]).split()))
    return o + '</div>'

def donde():
    return "".join('<div class="box"><span class="chip">%s</span><p class="small muted" style="margin:6px 0">%s</p><p style="margin:0">%s</p></div>' % (c, d, mk(s)) for c, d, s in B.DONDE)

def errores():
    o = '<div class="errs">'
    for mal, bien, why in B.ERRORES:
        o += '<div class="err"><div class="mal"><span aria-hidden="true">✗</span> <s>%s</s></div><div class="bien"><span aria-hidden="true">✓</span> %s</div><div class="small muted">%s</div></div>' % (mal, mk(bien), why)
    return o + '</div>'

CSS_R = CSS + r"""
:root{--ct:#C05621;--ct-soft:#FDEBDD;--cu:#1D5FA8;--cu-soft:#E2ECF8;--cn:#2F7D4F;--cn-soft:#E3F1E8}
.k{border-radius:4px;padding:0 3px 1px;border-bottom:3px solid;line-height:1.9}
.k.t{background:var(--ct-soft);border-color:var(--ct)}.k.u{background:var(--cu-soft);border-color:var(--cu)}.k.n{background:var(--cn-soft);border-color:var(--cn)}
.cams{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;border-top:6px solid var(--ct)}
.cam.cu{border-top-color:var(--cu)}.cam.cn{border-top-color:var(--ink)}
.cam h3{margin:0 0 6px}.cam p{margin:0;font-size:.95rem}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.box h4{margin:0 0 4px}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pill.ok{border-color:var(--ok)}
.pill.t.done{border-color:var(--ct)}.pill.u.done{border-color:var(--cu)}
.lanes{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.lanes button{font:inherit;font-weight:700;border:3px solid var(--line);background:#fff;border-radius:10px;padding:10px 12px;cursor:pointer}
.lanes button.t.on{border-color:var(--ct);background:var(--ct-soft)}.lanes button.u.on{border-color:var(--cu);background:var(--cu-soft)}
svg.dg{width:100%;height:auto;display:block;margin:6px 0}
.expl{border-radius:8px;padding:10px 14px;margin-top:6px;background:var(--paper)}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;margin:8px 0}
.lado{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-bottom:18px}
.lado>div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:.93rem;border-top:5px solid var(--muted)}
.lado>div.tu{border-top-color:var(--ct)}.lado>div.usted{border-top-color:var(--cu)}.lado>div.dos{border-top-color:var(--cn)}
.lado h4{margin:0 0 6px}.lado ul{margin:0;padding-left:1.1em}.lado li{margin:3px 0}
.lado3{grid-template-columns:repeat(3,1fr)}
.res{font-family:Georgia,serif;font-size:1.3rem;font-weight:700;text-align:center;margin:8px 0;line-height:1.8}
.chg{list-style:none;padding:0;margin:8px 0;display:flex;flex-wrap:wrap;gap:8px}
.chg li{background:var(--paper);border-radius:8px;padding:4px 10px;font-size:.93rem}
.duo2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.mail{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 14px;border-top:6px solid var(--ct);line-height:1.9}
.mail.usted{border-top-color:var(--cu)}
.mail .h{font-size:.8rem;font-weight:700;letter-spacing:.04em;color:var(--muted);margin-bottom:6px;line-height:1.4}
.errs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.err{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.err .mal{color:var(--bad)}.err .bien{margin:4px 0}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.vchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px;background:var(--paper);color:var(--muted)}
.vchip.tu{background:var(--ct-soft);color:#8A3A12}.vchip.usted{background:var(--cu-soft);color:var(--cu)}
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
.wl span{display:inline-block;border-radius:999px;padding:0 8px;margin:2px;font-size:.88rem}
.wl .wt{background:var(--ct-soft);color:#8A3A12}.wl .wu{background:var(--cu-soft);color:var(--cu)}
.check{list-style:none;padding:0;margin:8px 0}.check li{padding:5px 0}.check label{cursor:pointer}
.ocard{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin-top:12px}
.ocard .ph1{font-family:Georgia,serif;font-size:1.15rem;font-weight:700}
.sit{font-family:Georgia,serif;font-size:1.35rem;font-weight:700;margin:8px 0;line-height:1.35}
.who{display:inline-block;font-weight:700;border-radius:10px;padding:6px 14px;margin:6px 0 8px;font-size:1.05rem}
.who.t{background:var(--ct-soft);color:#8A3A12}.who.u{background:var(--cu-soft);color:var(--cu)}
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
@media (max-width:700px){.cams,.errs,.lado,.lado3,.duo2,.lanes{grid-template-columns:1fr}.qz .ops.bm{grid-template-columns:1fr 1fr}table.t{font-size:.9rem}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:13px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.lado>div,.err,.mail{break-inside:avoid}}
"""

STEPS = [("distancia", "La distancia"), ("carril", "El carril"), ("correos", "Los correos"), ("examen", "En el examen"),
         ("practica", "Practica"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_DIST = """
<h2>La distancia y el carril</h2>
<p class="lead">Antes de hablar con alguien, mira la distancia que hay entre los dos. Esa distancia decide si usas <b>tú</b> o <b>usted</b>. Y cuando ya has elegido, no cambias: del saludo a la despedida, el mismo carril.</p>
__CARDS__
__LEG__
<h3>Cerca o a un paso</h3>
<div class="duo2"><div>__DT__</div><div>__DU__</div></div>
<h3>¿Tú o usted? Toca una persona</h3>
<p class="muted small">Piensa primero tu respuesta y después toca la persona.</p>
<div class="pills" id="persel"></div>
<div class="box" id="pervis" aria-live="polite"></div>
<h3>En el examen, la lámina te lo dice</h3>
__LAMDICE__
<div class="tip"><b>En España</b> se usa mucho el tú: entre compañeros, con gente joven, a veces también en las tiendas. Si la otra persona te habla de tú, puedes pasar a tú. Pero en el examen, si la lámina dice que es un servicio o un correo a alguien que no conoces, usa <b>usted</b>.</div>
<h3>El truco: usted habla como «él»</h3>
<p>Usted es la persona que pones un paso más allá: en la casilla de <b>él / ella</b>. Por eso, si no sabes la forma de usted, piensa en «él»: <i>él tiene</i> → <i>usted tiene</i>.</p>
__ELSVG__
__ELTAB__
<p><b>Formas fijas</b> (estas no salen de «él», apréndelas):</p>
__FIJAS__
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="carril">Siguiente: el carril</button></div>
"""

V_CARRIL = """
<h2>El carril: todo cambia a la vez</h2>
<p class="lead">Cuando eliges tú o usted, no cambia una palabra: cambian todas las señales del camino. El verbo, te / le, tu / su, perdona / perdone, ¿y tú? / ¿y usted?. Si cambias solo una, el coche se queda entre dos carriles.</p>
__ROAD__
<h3>Todo lo que cambia</h3>
__CAMBIA__
<p>Sirven para los dos carriles: __DOS__</p>
<h3>Cambia de carril</h3>
<p class="muted small">Elige una frase y cámbiala de carril. Mira qué piezas cambian: todas a la vez.</p>
<div class="pills" id="frsel"></div>
<div class="lanes" id="lanesel"><button class="t" data-act="lane" data-l="t">Carril de tú</button><button class="u" data-act="lane" data-l="u">Carril de usted</button></div>
<div class="box" id="frvis" aria-live="polite"></div>
<details><summary>¿Y si hablo con varias personas? (vosotros / ustedes)</summary>
<p>En España, con varios amigos: <b>vosotros</b> (tenéis, os, vuestro). Con varias personas de usted: <b>ustedes</b>, que habla como «ellos» (tienen, les, su). En el examen casi siempre hablas con una sola persona.</p></details>
<div class="row"><button class="btn cta" data-go="correos">Siguiente: los correos</button></div>
"""

V_CORREOS = """
<h2>Los correos: del saludo a la despedida</h2>
<p class="lead">En la tarea 1 de la escritura, el saludo elige el carril y la despedida lo cierra. Entre los dos, todo el correo va por el mismo.</p>
__CORREOS__
<div class="tip"><b>Un saludo</b> y <b>Muchas gracias</b> sirven para los dos. Si no estás seguro de la despedida de un correo de usted, «Un saludo» nunca falla.</div>
<h3>La misma petición, dos veces</h3>
<p>Leo quiere comprar una bici de segunda mano. Escribe dos correos con lo mismo: uno a su amigo Iker y otro a un señor que no conoce. Mira cuántas piezas cambian.</p>
__DOSC__
<div class="row"><button class="btn cta" data-go="examen">Siguiente: en el examen</button></div>
"""

V_EXAMEN = """
<h2>Dónde sale en el examen</h2>
<p class="lead">Mezclar tú y usted es uno de los fallos más típicos del DELE A2. No es difícil, pero se escapa si no lo miras: por eso tiene su propia regla de oro y su propia pasada en la revisión final.</p>
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
 <button class="pill on" data-act="ex" data-k="p1">1. ¿Qué dices?</button>
 <button class="pill" data-act="ex" data-k="p2">2. Cambia de carril</button>
 <button class="pill" data-act="ex" data-k="e2">3. Textos del examen</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Ahora úsalo en una tarea del examen: escribe un correo o di la misma petición a dos personas en voz alta.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="o">Oral: dos veces lo mismo</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu correo y después pulsa <b>Revisar tú y usted</b>: la página busca las palabras de cada carril y te avisa si los mezclas. No corrige el texto entero: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="ato" hidden>
 <p>Tienes que decir lo mismo dos veces, <b>en voz alta</b>: primero a alguien cercano (tú) y después al examinador, que hace de persona que no conoces (usted). Cambia todas las piezas: el verbo, te / le, tu / su, oye / oiga...</p>
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
  <label><input type="radio" name="o1" value="La distancia">La distancia</label>
  <label><input type="radio" name="o1" value="El truco de él / ella">El truco de él / ella</label>
  <label><input type="radio" name="o1" value="El carril">El carril</label>
  <label><input type="radio" name="o1" value="Los correos">Los correos</label>
  <label><input type="radio" name="o1" value="En el examen y los errores típicos">En el examen y los errores típicos</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tú">Ahora tú</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué te cuesta más ahora?</label>
 <div class="chips" role="group" aria-labelledby="o2l">
  <label><input type="radio" name="o2" value="Saber cuándo usar usted">Saber cuándo usar usted</label>
  <label><input type="radio" name="o2" value="Las formas de usted (tiene, le, su)">Las formas de usted (tiene, le, su)</label>
  <label><input type="radio" name="o2" value="Perdone, oiga, mire">Perdone, oiga, mire</label>
  <label><input type="radio" name="o2" value="Saludos y despedidas de los correos">Saludos y despedidas de los correos</label>
  <label><input type="radio" name="o2" value="No cambiar de trato a mitad">No cambiar de trato a mitad</label>
 </div>
 <label class="q" id="o3l">3. ¿Te ayuda la idea de «la distancia y el carril»?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con tú y usted? (1 = nada, 10 = total)</label>
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

def eltab(): return tabla(B.EL_ELLA, ["Tú (cerca)", "Usted (a un paso)", "Él / ella"])
def fijas(): return tabla(B.FIJAS, ["Tú", "Usted"])
def cambia(): return tabla(B.CAMBIA, ["", "Tú", "Usted"])

def resumen():
    o = '<h2>Tú y usted · resumen</h2>' + cards() + LEG + '<div class="duo2"><div>%s</div><div>%s</div></div>' % (dist_svg("t"), dist_svg("u"))
    o += '<h3>Usted habla como «él»</h3>' + eltab() + fijas()
    o += '<h3>El carril</h3>' + road_svg() + cambia()
    o += '<h3>Los correos</h3>' + correos()
    o += '<h3>Los errores típicos</h3>' + errores()
    return o

views = {
    "distancia": V_DIST.replace("__CARDS__", cards()).replace("__LEG__", LEG).replace("__DT__", dist_svg("t")).replace("__DU__", dist_svg("u"))
                       .replace("__LAMDICE__", lamina_dice()).replace("__ELSVG__", el_svg()).replace("__ELTAB__", eltab()).replace("__FIJAS__", fijas()),
    "carril": V_CARRIL.replace("__ROAD__", road_svg()).replace("__CAMBIA__", cambia()).replace("__DOS__", mk(B.PARA_LOS_DOS)),
    "correos": V_CORREOS.replace("__CORREOS__", correos()).replace("__DOSC__", dos_correos()),
    "examen": V_EXAMEN.replace("__LEG__", LEG).replace("__DONDE__", donde()).replace("__ORO__", B.REGLA_ORO).replace("__ERRORES__", errores()),
    "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R07</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
""".replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

# ------------------------------------------------------------------ DATOS PARA EL SCRIPT
def frase_data(f):
    gt = MARK.findall(f["t"]); gu = MARK.findall(f["u"])
    return {"tema": f["tema"], "t": mk(f["t"]), "u": mk(f["u"]), "ch": [[a[1], b[1]] for a, b in zip(gt, gu)]}

DATA = {
    "key": STORAGE, "title": TITLE,
    "steps": [{"id": k, "label": l} for k, l in STEPS],
    "motivos": {k: {"c": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "carriles": B.CARRILES,
    "personas": [{"q": q, "c": c, "why": w} for q, c, w in B.PERSONAS],
    "distsvg": {"tu": dist_svg("t"), "usted": dist_svg("u")},
    "frases": [frase_data(f) for f in B.FRASES_CARRIL],
    "roadsvg": {"t": road_svg("t"), "u": road_svg("u")},
    "qz": {
        "p1": {"items": [{"q": it["q"], "o": it["o"], "why": it["why"], "c": it["c"]} for it in B.P_DICES], "n": 8, "name": "¿Qué dices?",
               "info": "Mira la distancia: ¿cerca (tú) o a un paso (usted)? Y comprueba que todas las piezas van por el mismo carril."},
        "p2": {"items": [{"q": it["q"], "o": it["o"], "why": it["why"], "d": it["d"]} for it in B.P_CARRIL], "n": 8, "name": "Cambia de carril",
               "info": "Pasa la frase al otro carril. Cuidado: tienen que cambiar TODAS las piezas."},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Errores típicos de los exámenes. ¿Está bien o mezcla los carriles?"},
    },
    "textos": B.TEXTOS,
    "laminas": B.LAMINAS, "focos": B.FOCOS, "detector": B.DETECTOR, "turx": B.TU_RX, "usrx": B.US_RX,
    "oral": [{"sit": o["sit"], "a": o["a"], "b": o["b"], "mt": mk(o["mt"]), "mu": mk(o["mu"])} for o in B.ORAL],
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function blank(){ return {cur:'distancia', seen:{}, per:-1, fr:0, lane:'t', ex:'p1', etext:D.textos[0].id, at:'w',
  qz:{}, qlog:{}, cz:{}, w:{}, wchk:{}, wrev:{}, lam:D.laminas[0].id, oc:{n:6,t:10}, ro:null, olog:[],
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

/* ---------------- 1. la distancia ---------------- */
function renderPer(){
 var o=''; D.personas.forEach(function(p,i){ o+='<button class="pill'+(S.per===i?' on':'')+'" data-act="per" data-i="'+i+'">'+esc(p.q)+'</button>'; });
 $('persel').innerHTML=o;
 if(S.per<0){ $('pervis').innerHTML='<p class="muted" style="margin:0">Toca una persona: ¿está cerca o a un paso?</p>'; return; }
 var p=D.personas[S.per];
 $('pervis').innerHTML='<div class="res"><span class="k '+(p.c==='tu'?'t':'u')+'">'+(p.c==='tu'?'tú':'usted')+'</span></div>'+D.distsvg[p.c]+'<div class="expl">'+esc(p.q)+': '+p.why+'</div>';
}

/* ---------------- 2. el carril: cambia de carril ---------------- */
function renderFr(){
 var o=''; D.frases.forEach(function(f,i){ o+='<button class="pill'+(S.fr===i?' on':'')+'" data-act="fr" data-i="'+i+'">'+esc(f.tema)+'</button>'; });
 $('frsel').innerHTML=o;
 var bs=$('lanesel').querySelectorAll('button'); for(var i=0;i<bs.length;i++){ var on=bs[i].getAttribute('data-l')===S.lane; bs[i].classList.toggle('on',on); bs[i].setAttribute('aria-pressed',on); }
 var f=D.frases[S.fr], l=S.lane;
 var ch='<p class="small" style="margin:8px 0 2px"><b>Las piezas que cambian ('+f.ch.length+'):</b></p><ul class="chg">'+f.ch.map(function(c){ return '<li><span class="k t">'+esc(c[0])+'</span> ↔ <span class="k u">'+esc(c[1])+'</span></li>'; }).join('')+'</ul>';
 $('frvis').innerHTML=D.roadsvg[l]+'<div class="res">'+(l==='t'?f.t:f.u)+'</div>'+ch;
}

/* ---------------- motor de opcion multiple ---------------- */
function qzNew(k){ var c=D.qz[k]; S.qz[k]={order:shuffle(range(c.items.length)).slice(0,c.n), i:0, res:[], perm:{}}; save(); }
function qHead(k, it){
 if(k==='p1') return esc(it.q);
 if(k==='p2') return '«'+esc(it.q)+'» → <span class="k '+(it.d==='tu'?'t':'u')+'">'+(it.d==='tu'?'pásala a tú':'pásala a usted')+'</span>';
 return esc(it.q);
}
function qzRender(k, box){
 var c=D.qz[k]; if(!S.qz[k]) qzNew(k);
 var st=S.qz[k], N=st.order.length;
 if(st.i>=N){
  var ok=st.res.filter(function(r){return r.ok;}).length, fails=st.res.filter(function(r){return !r.ok;});
  var msg = ok>=N-1 ? '¡Muy bien! No te sales del carril.' : (ok>=Math.ceil(N*0.6) ? 'Bien. Mira otra vez las explicaciones de las que has fallado.' : 'Vuelve a mirar la distancia y el carril, y repite con otras frases.');
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
  var mo=D.motivos[g.m], fn=D.carriles[mo.c];
  if(c.cur===g.ok) o+='<li class="ok">'+g.n+'. ✓ <b>'+esc(g.ok)+'</b> · <span class="vchip '+mo.c+'">'+fn+'</span> '+mo.w+'</li>';
  else o+='<li class="no">'+g.n+'. ✗ <b>'+esc(c.cur)+'</b> no va aquí. Pista: <span class="vchip '+mo.c+'">'+fn+'</span> '+mo.w+' Prueba otra vez.</li>';
 });
 return {html:o, tot:tot, done:done, first:first};
}
function renderE2(){
 var o='<div class="pills">'; D.textos.forEach(function(t){ o+='<button class="pill'+(S.etext===t.id?' on':'')+'" data-act="etext" data-id="'+t.id+'">'+esc(t.titulo)+'</button>'; }); o+='</div>';
 var t=D.textos.filter(function(x){return x.id===S.etext;})[0], g=parseGaps(t.id, t.texto), f=fbList(t.id, t.texto);
 o+='<div class="cz"><span class="chip">'+esc(t.tipo)+'</span><span class="vchip '+t.c+'">'+D.carriles[t.c]+'</span><span class="tema">'+esc(t.titulo)+'</span>'+g.html+'</div>';
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
var EXINFO={e2:'Dos correos y dos diálogos de la tarea 3: dos de tú y dos de usted. Mira el carril del texto y elige la forma de cada hueco: la corrección sale enseguida, con el motivo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
var CH=['He mirado a quién escribo: ¿cerca (tú) o a un paso (usted)?','El saludo y la despedida son del mismo carril.','Todos los verbos que hablan a la otra persona van en el mismo carril (tienes / tiene).','Te / le, para ti / para usted, tu / su: en el mismo carril.','Si devuelvo una pregunta: ¿y tú? / ¿y usted?, en el mismo carril.'];
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+'</div>';
 h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(f){ return '<span class="vchip '+L.c+'">'+D.focos[f]+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas te dicen qué pieza del carril vas a usar en cada pauta. Primero decide: ¿tú o usted? Recuerda: unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu correo</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar tú y usted</button></div><div id="rvbox" aria-live="polite"></div>';
 h+='<h3>Mi lista del carril</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
function findAll(txt, list){ var n=norm(txt), out=[]; list.forEach(function(re){ var r=new RegExp(re,'g'), m; while((m=r.exec(n))){ out.push({a:m.index, w:txt.substr(m.index, m[0].length)}); if(r.lastIndex===m.index) r.lastIndex++; } }); out.sort(function(x,y){ return x.a-y.a; }); return out; }
function sents(t){ return t.match(/[^.!?\n]+[.!?]*/g)||[]; }
function detIds(t){ var o={}, ss=sents(t).map(norm); D.detector.forEach(function(d){ var r=new RegExp(d.re); if(d.sc==='s'){ if(ss.some(function(s){ return r.test(s); })) o[d.id]=1; } else if(r.test(norm(t))) o[d.id]=1; }); return Object.keys(o).sort(); }
window.__R07detect = detIds;
function uniq(a){ var s={}, o=[]; a.forEach(function(x){ var k=x.w.toLowerCase(); if(!s[k]){ s[k]=1; o.push(x.w); } }); return o; }
function review(){
 var L=lam(), txt=$('wtext').value, out=[], red=0, amb=0;
 if(txt.trim().length<20){ $('rvbox').innerHTML='<ul class="rv"><li class="a">Escribe primero tu correo.</li></ul>'; return; }
 var tw=uniq(findAll(txt, D.turx)), uw=uniq(findAll(txt, D.usrx));
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
  if(d.id==='su_y_tu' && L.c==='usted') return; /* en un correo de usted, su es lo correcto */
  if(d.t==='r') red++; else amb++;
  out.push('<li class="'+d.t+'">'+(d.t==='r'?'<b>¡Ojo!</b> ':'<b>Mira esto:</b> ')+d.msg+'</li>');
 });
 // 3. el carril de la lamina
 var nombre = L.c==='tu' ? 'tú' : 'usted';
 if(L.c==='tu' && uw.length){ red++; out.push('<li class="r"><b>¡Ojo!</b> Esta lámina es de <b>tú</b> (escribes a una amiga) y hay palabras de usted: <b>'+uw.map(esc).join(', ')+'</b>.</li>'); }
 if(L.c==='usted' && tw.length){ red++; out.push('<li class="r"><b>¡Ojo!</b> Esta lámina es de <b>usted</b> (no conoces a la señora Ferrer) y hay palabras de tú: <b>'+tw.map(esc).join(', ')+'</b>.</li>'); }
 if(L.c==='usted' && !uw.length){ amb++; out.push('<li class="a"><b>Mira esto:</b> no veo ninguna palabra segura de usted (Estimada..., usted, Atentamente, perdone...). ¿Has empezado con «Estimada señora Ferrer»?</li>'); }
 if(L.c==='tu' && !tw.length){ amb++; out.push('<li class="a"><b>Mira esto:</b> no veo ninguna palabra segura de tú (tu, te escribo, ¿quieres...?, un abrazo...). ¿Le hablas a Noa de tú?</li>'); }
 if(!red) out.unshift('<li class="g">No he encontrado mezcla de tú y usted: todo va por el carril de <b>'+nombre+'</b>. ¡Bien! Mira tú también la lista de abajo.</li>');
 var wl='<p class="wl small"><b>Palabras de tú:</b> '+(tw.length?tw.map(function(w){ return '<span class="wt">'+esc(w)+'</span>'; }).join(''):'ninguna')+'<br><b>Palabras de usted:</b> '+(uw.length?uw.map(function(w){ return '<span class="wu">'+esc(w)+'</span>'; }).join(''):'ninguna')+'</p>';
 var wc=txt.trim().split(/\s+/).length;
 S.wrev[L.id]={red:red, amb:amb, tu:tw.join(', '), us:uw.join(', '), words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul>'+wl+'<p class="muted small">Tu texto: '+wc+' palabras (la lámina pide '+L.palabras[0]+'-'+L.palabras[1]+'). Ojo: <i>su</i>, <i>le</i> o <i>tiene</i> no salen en las listas, porque también son de «él». La página no lo ve todo: tu profesora corrige el texto completo.</p>';
}

/* ---------------- relojes ---------------- */
var TM=null;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } }
function clockTxt(s){ s=Math.max(0,Math.ceil(s)); return Math.floor(s/60)+':'+(s%60<10?'0':'')+(s%60); }

/* ---------------- ahora tu: oral, dos veces lo mismo ---------------- */
function oNew(){ S.ro={deck:shuffle(range(D.oral.length)).slice(0,S.oc.n), i:0, ph:0, res:[]}; save(); }
function renderO(){
 var box=$('obox'), R=S.ro, h='';
 if(!R){
  h+='<div class="ocard"><div class="ph1">Prepárate</div><p>En cada tarjeta ves una situación. Primero se lo dices a alguien cercano, de <b>tú</b>; después, al examinador, que hace de persona que no conoces, de <b>usted</b>. El reloj pasa solo.</p>';
  h+='<p class="small"><b>Tarjetas:</b></p><div class="pills">'+[4,6,8].map(function(n){ return '<button class="pill'+(S.oc.n===n?' on':'')+'" data-act="on" data-n="'+n+'">'+n+'</button>'; }).join('')+'</div>';
  h+='<p class="small"><b>Tiempo para cada frase:</b></p><div class="pills">'+[8,10,15].map(function(t){ return '<button class="pill'+(S.oc.t===t?' on':'')+'" data-act="ot" data-t="'+t+'">'+t+' s</button>'; }).join('')+'</div>';
  h+='<div class="row"><button class="btn cta" data-act="ostart">Empezar</button></div>';
  if(S.olog.length){ h+='<p class="hist"><b>Tus últimas prácticas:</b> '+S.olog.map(function(r){ return r.d+': '+r.ok+'/'+r.n+' ('+r.t+' s)'; }).join(' · ')+'</p>'; }
  box.innerHTML=h+'</div>'; return;
 }
 var N=R.deck.length;
 if(R.i>=N){
  var ok=R.res.filter(function(r){ return r.ok; }).length;
  h+='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+(ok>=N-1?'¡Muy bien! Cambias de carril sin dejarte ninguna pieza.':'Mira otra vez «Todo lo que cambia» y repite: la rapidez llega con la práctica.')+'</p>';
  var fl=R.res.filter(function(r){ return !r.ok; });
  if(fl.length){ h+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fl.forEach(function(r){ var o=D.oral[r.k]; h+='<li>'+esc(o.sit)+'<br>'+o.mt+' · '+o.mu+'</li>'; }); h+='</ul>'; }
  h+='<div class="row"><button class="btn cta" data-act="oagain">Otra vez</button></div></div>';
  box.innerHTML=h; return;
 }
 var o=D.oral[R.deck[R.i]];
 h+='<div class="ocard"><div class="cnt small muted">Tarjeta '+(R.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(R.i/N*100)+'%"></i></div>';
 h+='<div class="sit">'+esc(o.sit)+'</div>';
 if(R.ph===0){
  h+='<p>1. <span class="who t">'+esc(o.a)+' (tú)</span><br>2. <span class="who u">'+esc(o.b)+' (usted)</span></p>';
  h+='<div class="row"><button class="btn cta" data-act="ogo">Empezar con el reloj</button></div>';
 } else if(R.ph===1 || R.ph===2){
  var t=R.ph===1;
  h+='<div class="who '+(t?'t':'u')+'">'+(t?'1. Díselo '+esc(o.a)+' · TÚ':'2. Ahora díselo '+esc(o.b)+' · USTED')+'</div>';
  h+='<div class="clock" id="oclk">'+clockTxt(S.oc.t)+'</div><div class="tbar"><i id="obar"></i></div>';
  h+='<div class="row"><button class="btn cta" data-act="oskip">Ya está</button></div>';
 } else {
  h+='<div class="model"><b>Una respuesta modelo</b><br><span class="who t" style="font-size:.85rem;padding:2px 10px">tú</span> '+o.mt+'<br><span class="who u" style="font-size:.85rem;padding:2px 10px">usted</span> '+o.mu+'</div>';
  h+='<p class="small" style="margin-top:12px"><b>¿Has cambiado todas las piezas?</b> (el verbo, te / le, tu / su, oye / oiga...)</p>';
  h+='<div class="row"><button class="btn cta" data-act="oeval" data-ok="1">✓ Sí</button><button class="btn" data-act="oeval" data-ok="0">✗ Me he dejado alguna</button></div>';
 }
 box.innerHTML=h+'</div>';
}
function oRun(){
 stopTimer(); var R=S.ro; if(!R || (R.ph!==1 && R.ph!==2)) return;
 renderO();
 var T0=Date.now(), dur=S.oc.t;
 TM=setInterval(function(){
  var t=(Date.now()-T0)/1000, bar=$('obar'), ck=$('oclk'); if(!bar){ stopTimer(); return; }
  ck.textContent=clockTxt(dur-t); bar.style.width=Math.min(100,t/dur*100)+'%';
  if(t>=dur) oNext();
 }, 200);
}
function oNext(){ stopTimer(); var R=S.ro; R.ph++; save(); if(R.ph===2) oRun(); else renderO(); }

/* ---------------- opinion y copiar ---------------- */
function renderOpn(){
 var o=''; for(var i=1;i<=10;i++) o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>';
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked=r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function pack(){
 var L=['CURSO DELE A2 - R07: TU Y USTED','Nombre: '+(S.name||'-'),''];
 L.push('EJERCICIOS (ultimo resultado)');
 ['p1','p2','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 D.textos.forEach(function(t){
  var f=fbList(t.id,t.texto), errs=[];
  gapInfo(t.id,t.texto).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); });
  var started=Object.keys(S.cz).some(function(k){return k.indexOf(t.id+'-')===0;});
  L.push('- Textos del examen, '+t.titulo+': '+(started?f.first+'/'+f.tot+' a la primera'+(f.done<f.tot?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 L.push('','ORAL: DOS VECES LO MISMO');
 if(!S.olog.length) L.push('sin hacer');
 S.olog.forEach(function(r){ L.push('- '+r.d+': '+r.ok+'/'+r.n+' bien (autoevaluacion), '+r.t+' s por frase'+(r.fails&&r.fails.length?' | fallos: '+r.fails.join(' / '):'')); });
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' ('+(l.c==='tu'?'tu':'usted')+', '+l.palabras[0]+'-'+l.palabras[1]+' palabras)','Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision: '+rv.red+' avisos rojos, '+rv.amb+' ambar | palabras de tu: '+(rv.tu||'-')+' | palabras de usted: '+(rv.us||'-')+' | '+rv.words+' palabras');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. Lo que mas cuesta: '+(S.o2||'-'),'3. La distancia y el carril: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}
window.__R07pack = pack;

/* ---------------- eventos ---------------- */
var ACTS={
 per:function(b){ S.per=+b.getAttribute('data-i'); save(); renderPer(); },
 fr:function(b){ S.fr=+b.getAttribute('data-i'); save(); renderFr(); },
 lane:function(b){ S.lane=b.getAttribute('data-l'); save(); renderFr(); },
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
   S.olog.push({d:d.getDate()+'/'+(d.getMonth()+1), n:R.deck.length, t:S.oc.t, ok:ok, fails:R.res.filter(function(r){return !r.ok;}).map(function(r){ return D.oral[r.k].sit; })});
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
 if(S.ro && (S.ro.ph===1 || S.ro.ph===2)) S.ro.ph=0;
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

renderPer(); renderFr(); renderEx(); renderAt(); renderOpn(); go(S.cur);
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
      "| items:", len(B.P_DICES) + len(B.P_CARRIL) + len(B.E_BIENMAL),
      "| pruebas del detector:", len(B.DETECTOR_PRUEBAS), "(navegador: %s)" % ("igual que Python" if NODE_OK else "sin probar"),
      "| buena en el desplegable (1a/2a/3a):", POS_TXT, "| frases del carril:", len(B.FRASES_CARRIL), "| tarjetas orales:", len(B.ORAL))
