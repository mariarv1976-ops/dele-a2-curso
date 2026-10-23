# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R05 DEL CURSO DE PREPARACION DELE A2: MUY / MUCHO; TAMBIEN / TAMPOCO
# Uso: python3 build_R05_muy_mucho.py  -> DELEA2_curso_R05_muy_mucho_tambien_tampoco.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# Contenidos: solo en banco_R05_muy_mucho.py. Este archivo monta la pagina y comprueba el banco.
# Mismo formato y motor que R01, R02 y R04: pestanas, correccion inmediata, huecos con motivo, "Ahora tu"
# con escritura (detector de errores tipicos) y oral (reacciona con tambien / tampoco / si / no, con reloj;
# y la foto con muy y mucho, fotos M4T2 ya subidas), Tu opinion y Copiar.
# Enfoque cognitivo: ¿COMO? -> MUY (el volumen: sube un adjetivo o un adverbio y no se viste);
# ¿CUANTO? -> MUCHO (la cantidad: delante del nombre lleva su camiseta, detras del verbo no cambia);
# TAMBIEN / TAMPOCO = EL ECO (+ o -; repito o cambio; ¿yo o a mi?). Espanol de Espana. Ejemplos propios.
import json, os, re, shutil, subprocess, sys, tempfile, unicodedata
from curso_comun import CSS, EMAIL, page
import banco_R05_muy_mucho as B

TITLE = "Muy y mucho, también y tampoco"
FILE = "DELEA2_curso_R05_muy_mucho_tambien_tampoco.html"
STORAGE = "dele-a2-curso-R05"
IMG_T2 = "https://2spanishteachers.com/wp-content/uploads/" + B.MES_WP_T2.strip("/") + "/M4T2_foto%d.jpg"

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
MARK = re.compile(r"\[(m|c|t|x):([^\[\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
KINDS = {"m", "c", "t", "x"}
ECOW = {"también", "tampoco", "sí", "no"}

def chk_marks(s, where, need=0):
    rest = MARK.sub("", s)
    if "[" in rest or "]" in rest: err("marca mal cerrada en %s: %s" % (where, s[:70]))
    gs = MARK.findall(s)
    for k, b in gs:
        lb = b.lower()
        if k == "m" and not lb.startswith("muy "): err("%s: [m:] tiene que empezar por «muy»: %s" % (where, b))
        if k == "c" and not re.search(r"(^|\s)(much|poc)", lb): err("%s: [c:] sin mucho / poco: %s" % (where, b))
        if k == "t" and not re.search(r"también|tampoco", lb): err("%s: [t:] sin también / tampoco: %s" % (where, b))
        if k == "x" and not re.search(r"\b(sí|no)\b", lb): err("%s: [x:] sin sí / no: %s" % (where, b))
    if len(gs) < need: err("%s: hacen falta al menos %d marcas" % (where, need))
    return gs

def plain(s): return re.sub(r"<[^>]+>", "", MARK.sub(lambda m: m.group(2), s))
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()

def corto(s, g, a):
    w = ("también" if s == "+" else "tampoco") if a else ("no" if s == "+" else "sí")
    return ("A mí " if g else "Yo ") + w + "."

for k, (f, w) in B.MOTIVOS.items():
    if f not in B.FAMILIAS or not w: err("motivo mal definido: " + k)

# 1. Muy y mucho
for i, p in enumerate(B.PAREJAS):
    ga = chk_marks(p["a"], "pareja %d a" % i, 1); gb = chk_marks(p["b"], "pareja %d b" % i, 1)
    if any(k != "m" for k, _ in ga): err("pareja %d: la frase a solo lleva [m:]" % i)
    if any(k != "c" for k, _ in gb): err("pareja %d: la frase b solo lleva [c:]" % i)
    if p["kind"] not in ("nom", "verb", "comp"): err("pareja %d: kind desconocido" % i)
    if p["kind"] == "nom" and p.get("bt") not in ("ms", "fs", "mp", "fp"): err("pareja %d: falta la camiseta (bt)" % i)
    if p["kind"] == "nom" and len(gb[0][1].split()) != 2: err("pareja %d: el grupo con nombre es «mucho + nombre»" % i)
    if p["kind"] == "verb" and gb[0][1] != "mucho": err("pareja %d: detras del verbo, solo «mucho»" % i)
    if p["kind"] == "comp" and not re.match(r"mucho (más|menos|mejor|peor)$", gb[0][1]): err("pareja %d: comparar = mucho + mas/menos/mejor/peor" % i)
    if not p.get("ea") or not p.get("eb"): err("pareja %d sin explicacion" % i)
if {p["kind"] for p in B.PAREJAS} != {"nom", "verb", "comp"}: err("las parejas tienen que mostrar los tres sitios de mucho")
for t, cl, items in B.LADO:
    if cl not in ("vol", "can") or not items: err("lado mal definido: " + t)
    for it in items: chk_marks(it, "lado " + t, 1)
for t, bien, mal, why in B.CIERRES:
    chk_marks(bien, "cierres " + t, 1)
    chk_marks(why, "cierres " + t)
    if not why: err("cierre sin explicacion: " + t)

# 2. El eco
for i, e in enumerate(B.ECO_FRASES):
    if e["s"] not in "+-": err("eco %d: s tiene que ser + o -" % i)
    if e["s"] == "-" and not re.match(r"No\b", e["f"]): err("eco %d: una frase negativa empieza con «No»" % i)
    if e["s"] == "+" and re.match(r"No\b", e["f"]): err("eco %d: frase positiva que empieza con «No»" % i)
    g_frase = bool(re.match(r"(No )?(me|te|le) ", e["f"], re.I))
    if g_frase != e["g"]: err("eco %d: g no va con la frase (me gusta... = True)" % i)
    for a, key in ((1, "igual"), (0, "dif")):
        if not e[key].startswith(corto(e["s"], e["g"], a)): err("eco %d: «%s» tiene que empezar por «%s»" % (i, e[key], corto(e["s"], e["g"], a)))
celdas = {(e["s"], e["g"]) for e in B.ECO_FRASES}
if len(celdas) != 4: err("eco: hacen falta frases + y -, con gustar y sin gustar")
for k, lst in B.YO_AMI.items():
    for f, r in lst:
        chk_marks(r, "yo / a mí", 1)
        if (k == "ami") != plain(r).startswith("A mí"): err("yo / a mí: columna equivocada: " + r)
for f, why in B.TAMPOCO:
    chk_marks(f, "tampoco", 1)
    if "también no" in f or "tampoco no" in f: err("tampoco: frase con error en los ejemplos buenos")

# 3. En el examen
for c, d, s in B.DONDE: chk_marks(s, "donde " + c, 1)
for mal, bien, why in B.ERRORES:
    chk_marks(bien, "errores", 1)
    if plain(bien) == mal or not why: err("error tipico sin correccion o sin porque: " + mal)
REQ = ["mucho bonit", "muy gente", "mucho cansad", "gusta muy", "muy mucho", "mucho personas", "yo también no", "a mí también no", "yo tampoco me gusta"]
for k in REQ:
    if not any(k in m.lower() for m, _, _ in B.ERRORES): err("falta el error tipico: " + k)

# Ejercicios
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
            if len(o) != 3 or len(set(x.lower() for x in o)) != 3: err("%s: hacen falta 3 opciones distintas: %s" % (name, it["q"][:40]))
            if it["q"].count("____") != 1: err("%s: un solo hueco ____: %s" % (name, it["q"]))
            if "s" in it and o[0] != corto(it["s"], it["g"], it["a"]): err("%s: la buena tiene que ser «%s»: %s" % (name, corto(it["s"], it["g"], it["a"]), it["q"][:50]))
chk_quiz(B.P_MM, "P_MM", 12)
chk_quiz(B.P_ECO, "P_ECO", 10)
if sum(1 for it in B.P_ECO if "s" in it) < 8: err("P_ECO: al menos 8 reacciones con s/g/a")
for it in B.P_MM:
    if it["o"][0] not in ("muy", "mucho", "mucha", "muchos", "muchas"): err("P_MM: la buena es muy o una forma de mucho: " + it["q"])
if not any(it["o"][0] == "muy" for it in B.P_MM) or not any(it["o"][0] != "muy" for it in B.P_MM): err("P_MM: hacen falta de muy y de mucho")
chk_quiz(B.E_BIENMAL, "E_BIENMAL", 12, bm=True)
if not any(i["ok"] == 0 for i in B.E_BIENMAL): err("bien/mal: faltan frases bien")
for k in REQ:
    if not any(k in i["q"].lower() and i["ok"] == 1 for i in B.E_BIENMAL): err("bien/mal: falta el error tipico " + k)

# Textos con huecos
def chk_gaps(s, where):
    n = 0
    for g in GAP.findall(s):
        n += 1
        if "#" not in g: err("hueco sin motivo en %s: %s" % (where, g)); continue
        ops, mot = g.split("#"); ops = ops.split("|")
        if len(ops) != 3 or len(set(o.lower() for o in ops)) != 3: err("hueco sin 3 opciones distintas en %s: %s" % (where, g))
        if mot not in B.MOTIVOS: err("motivo desconocido en %s: %s" % (where, mot)); continue
        f, b = B.MOTIVOS[mot][0], ops[0].lower()
        if f == "vol" and b != "muy": err("en %s la buena (%s) tendria que ser muy, como dice su motivo" % (where, ops[0]))
        if f == "can" and not re.match(r"(much|poc)", b): err("en %s la buena (%s) tendria que ser mucho, como dice su motivo" % (where, ops[0]))
        if f == "eco" and b not in ECOW: err("en %s la buena (%s) tendria que ser tambien / tampoco / si / no" % (where, ops[0]))
        if mot == "igual_pos" and b != "también": err("%s: igual_pos -> también" % where)
        if mot == "igual_neg" and b != "tampoco": err("%s: igual_neg -> tampoco" % where)
        if mot == "cambio" and b not in ("sí", "no"): err("%s: cambio -> sí / no" % where)
    if n == 0: err("texto sin huecos: " + where)
    if "[[" in GAP.sub("", s) or "]]" in GAP.sub("", s): err("hueco mal cerrado en " + where)
    return n
ngaps = {t["id"]: chk_gaps(t["texto"], t["id"]) for t in B.TEXTOS}
alltex = " ".join(t["texto"] for t in B.TEXTOS)
usados = {g.split("#")[1] for g in GAP.findall(alltex)}
for m in B.MOTIVOS:
    if m not in usados: err("los textos no usan el motivo " + m)
def filled(s): return re.sub(r"<[^>]+>", " ", GAP.sub(lambda m: m.group(1).split("#")[0].split("|")[0], s))

for L in B.LAMINAS:
    if len(L["pautas"]) != 5: err("lamina %s: 5 pautas" % L["id"])
    for _, fs in L["pautas"]:
        for f in fs:
            if f not in B.FOCOS: err("foco desconocido en lamina " + L["id"])
if not any("eco" in fs for L in B.LAMINAS for _, fs in L["pautas"]): err("ninguna lamina pide reaccionar (eco)")

# Detector
ids = set()
for d in B.DETECTOR:
    if d["t"] not in ("r", "a"): err("tipo de aviso desconocido en el detector: " + d["id"])
    if d["id"] in ids: err("id repetido en el detector: " + d["id"])
    ids.add(d["id"])
    try: d["_rx"] = re.compile(d["re"])
    except re.error as e: err("regex del detector: %s (%s)" % (d["id"], e))
    if not d.get("msg"): err("aviso sin mensaje: " + d["id"])
    if d["re"] != norm(d["re"]): err("la regex de %s tiene que ir sin tildes ni mayusculas" % d["id"])
    if "(?<" in d["re"] or "(?P" in d["re"]: err("la regex de %s usa algo que no funciona igual en el navegador" % d["id"])

def det(txt, only_red=False):
    return sorted({d["id"] for d in B.DETECTOR if (not only_red or d["t"] == "r") and d["_rx"].search(norm(txt))})

if not ERR:
    for txt, exp in B.DETECTOR_PRUEBAS:
        got = det(txt)
        if got != sorted(exp): err("detector: %r da %s y deberia dar %s" % (txt, got, sorted(exp)))
    for d in B.DETECTOR:
        if not any(d["id"] in e for _, e in B.DETECTOR_PRUEBAS): err("el aviso %s no tiene ninguna prueba" % d["id"])
    if sum(1 for _, e in B.DETECTOR_PRUEBAS if not e) < 10: err("detector: hacen falta al menos 10 pruebas que NO deben saltar")
    for k in REQ:
        if not any(k in t.lower() and e for t, e in B.DETECTOR_PRUEBAS): err("detector: ninguna prueba con el error tipico " + k)
    # Los errores tipicos y las frases malas tienen que saltar...
    for mal, _, _ in B.ERRORES:
        if not det(mal): err("detector: no ve el error tipico «%s»" % mal)
    for it in B.E_BIENMAL:
        if it["ok"] == 1 and not det(it["q"]): err("detector: no ve la frase mala «%s»" % it["q"])
    # ...y nada de lo que la ficha da por bueno puede dar un aviso rojo (frase a frase, como en la pagina).
    buenos = []
    buenos += [p["a"] for p in B.PAREJAS] + [p["b"] for p in B.PAREJAS]
    buenos += [x for _, _, items in B.LADO for x in items] + [b for _, b, _, _ in B.CIERRES]
    buenos += [e["f"] for e in B.ECO_FRASES] + [e["igual"] for e in B.ECO_FRASES] + [e["dif"] for e in B.ECO_FRASES]
    buenos += [f + " " + r for lst in B.YO_AMI.values() for f, r in lst] + [f for f, _ in B.TAMPOCO]
    buenos += [s for _, _, s in B.DONDE] + [b for _, b, _ in B.ERRORES]
    buenos += [filled(t["texto"]) for t in B.TEXTOS] + [o["f"] + " " + o["igual"] + " " + o["dif"] for o in B.ORAL]
    buenos += [f["mm"] for f in B.FOTOS] + [i["q"] for i in B.E_BIENMAL if i["ok"] == 0]
    buenos += [i["q"].replace("____", i["o"][0]) for i in B.P_MM + B.P_ECO]
    buenos += [L["mensaje"] for L in B.LAMINAS]
    for b in buenos:
        for s in re.findall(r"[^.!?\n]+[.!?]*", plain(b).replace(" / ", ". ")):
            r = det(s, only_red=True)
            if r: err("detector: aviso rojo %s en un texto bueno: %r" % (r, s.strip()))

# Oral
for i, o in enumerate(B.ORAL):
    for a, key in ((1, "igual"), (0, "dif")):
        if not o[key].startswith(corto(o["s"], o["g"], a)): err("oral %d: «%s» tiene que empezar por «%s»" % (i, o[key], corto(o["s"], o["g"], a)))
    if (o["s"] == "-") != bool(re.match(r"No\b", o["f"])): err("oral %d: el signo no va con la frase" % i)
    if bool(re.match(r"(No )?(me|te|le) ", o["f"], re.I)) != o["g"]: err("oral %d: g no va con la frase" % i)
if len({(o["s"], o["g"]) for o in B.ORAL}) != 4 or len(B.ORAL) < 16: err("oral: al menos 16 frases, de los cuatro tipos")
for c in {(o["s"], o["g"]) for o in B.ORAL}:
    if sum(1 for o in B.ORAL if (o["s"], o["g"]) == c) < 3: err("oral: pocas frases del tipo %s" % (c,))
fids = [f["id"] for f in B.FOTOS]
if len(set(fids)) != len(fids): err("fotos repetidas")
for f in B.FOTOS:
    if not 7 <= f["id"] <= 12: err("foto %s: solo las fotos 7-12 de la tarea 2 (como en el examen)" % f["id"])
    gs = chk_marks(f["mm"], "foto %d" % f["id"], 4)
    if sum(1 for k, _ in gs if k == "m") < 2 or sum(1 for k, _ in gs if k == "c") < 2: err("foto %d: el modelo usa al menos dos muy y dos mucho" % f["id"])
    if not f["mm"].startswith("En la foto hay"): err("foto %d: el modelo empieza con «En la foto hay»" % f["id"])
    if not f.get("alt"): err("foto %d sin descripcion" % f["id"])

# Node: el detector tiene que dar lo mismo en el navegador
NODE_OK = None
if not ERR and shutil.which("node"):
    js_t = ("var D=%s;function norm(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}"
            "var bad=[];D.p.forEach(function(p){var n=norm(p[0]),ids=[];D.d.forEach(function(d){if(new RegExp(d.re).test(n))ids.push(d.id);});"
            "ids.sort();if(ids.join()!==p[1].slice().sort().join())bad.push(p[0]+' -> '+ids.join());});console.log(JSON.stringify(bad));") % json.dumps(
        {"d": [{"id": d["id"], "re": d["re"]} for d in B.DETECTOR], "p": B.DETECTOR_PRUEBAS}, ensure_ascii=False)
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
CLS = {"m": "m", "c": "c", "t": "t", "x": "x"}
def mk(s): return MARK.sub(lambda m: '<span class="k %s">%s</span>' % (CLS[m.group(1)], m.group(2)), s)

INK = "#14161C"; MUT = "#5E5A55"; LINE = "#E6DFD6"
VOL, VOL_S = "#B7791F", "#FBF0DA"
CAN, CAN_S = "#17707F", "#DDF0F2"
ECO, ECO_S = "#1D5FA8", "#E2ECF8"
CAM, CAM_S = "#C2492A", "#FCE9E1"
GEN = {"m": ("#17707F", "#DDF0F2"), "f": ("#6B3FA0", "#EFE7F8")}

def bars(x, base, filled, col, light, s=1.0):
    o = ""
    for i in range(6):
        h = (14 + i * 10) * s
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s"/>' % (x + i * 22 * s, base - h, 16 * s, h, col if i < filled else light)
    return o

def shirt(cx, cy, tag, s=1.0, text=True):
    c, soft = GEN[tag[0]]
    def one(dx, dy, fill):
        pts = [(-34, -26), (-14, -32), (0, -24), (14, -32), (34, -26), (48, -6), (32, 2), (32, 32), (-32, 32), (-32, 2), (-48, -6)]
        d = "M" + " L".join("%.1f,%.1f" % (cx + dx + x * s, cy + dy + y * s) for x, y in pts) + " Z"
        return '<path d="%s" fill="%s" stroke="%s" stroke-width="2.5" stroke-linejoin="round"/>' % (d, fill, c)
    o = ""
    if tag[1] == "p": o += one(9 * s, -9 * s, "#fff")
    o += one(0, 0, soft)
    if text:
        o += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="700" fill="%s">%s</text>' % (cx, cy - 2 * s, 12 * s, c, "masc." if tag[0] == "m" else "fem.")
        o += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" fill="%s">%s</text>' % (cx, cy + 15 * s, 11 * s, c, "uno" if tag[1] == "s" else "varios")
    return o

def svg(vb, aria, inner): return '<svg class="dg" viewBox="%s" role="img" aria-label="%s">%s</svg>' % (vb, aria, inner)
def txt(x, y, s, size=16, col=INK, w="400", anchor="middle", extra=""):
    return '<text x="%s" y="%s" text-anchor="%s" font-size="%s" font-weight="%s" fill="%s"%s>%s</text>' % (x, y, anchor, size, w, col, extra, s)

def vol_svg(group):
    word = group[4:]
    o = bars(52, 128, 2, "#E9C98F", LINE)
    o += txt(107, 162, word, 24)
    o += '<circle cx="320" cy="92" r="38" fill="%s" stroke="%s" stroke-width="4"/>' % (VOL_S, VOL)
    o += '<line x1="320" y1="92" x2="344" y2="66" stroke="%s" stroke-width="5" stroke-linecap="round"/>' % VOL
    o += txt(320, 156, "muy", 26, VOL, "700")
    o += '<path d="M200,92 L268,92" stroke="%s" stroke-width="3"/><path d="M372,92 L432,92" stroke="%s" stroke-width="3"/><polygon points="432,84 446,92 432,100" fill="%s"/>' % (MUT, VOL, VOL)
    o += bars(460, 128, 6, VOL, LINE)
    o += '<text x="515" y="162" text-anchor="middle" font-size="24" font-weight="700"><tspan fill="%s">muy</tspan><tspan fill="%s"> %s</tspan></text>' % (VOL, INK, word)
    return svg("0 0 640 176", "Muy sube el volumen de " + word, o)

def pile(cx, base, rows, col, soft, r=9):
    o = ""
    for i, n in enumerate(rows):
        y = base - i * (2 * r - 2)
        for j in range(n):
            x = cx + (j - (n - 1) / 2) * (2 * r + 2)
            o += '<circle cx="%.1f" cy="%.1f" r="%d" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, r, soft, col)
    return o

def nom_svg(group, tag):
    w1, noun = group.split()
    c, soft = GEN[tag[0]]
    o = pile(120, 132, [6, 5, 4, 3, 2, 1], CAN, CAN_S)
    o += txt(120, 164, "¿cuánto? un montón", 18, MUT)
    o += '<text x="330" y="102" text-anchor="middle" font-size="34" font-family="Georgia,serif" font-weight="700"><tspan fill="%s">much</tspan><tspan fill="%s">%s</tspan><tspan fill="%s"> %s</tspan></text>' % (CAN, c, w1[4:], INK, noun)
    o += txt(330, 134, "con la camiseta del nombre", 18, c)
    o += shirt(540, 84, tag, 1.15)
    o += txt(540, 156, "«%s»" % noun, 18, MUT)
    return svg("0 0 640 176", "Mucho delante del nombre " + noun + " lleva su camiseta", o)

def verb_svg(verb):
    o = '<rect x="40" y="58" width="250" height="68" rx="12" fill="#fff" stroke="%s" stroke-width="2.5"/>' % INK
    o += txt(165, 101, verb, 24, INK, "700")
    o += txt(165, 44, "el verbo", 18, MUT)
    o += '<path d="M290,92 L360,92" stroke="%s" stroke-width="3" stroke-dasharray="6 5"/>' % CAN
    o += txt(450, 104, "mucho", 34, CAN, "700", extra=' font-family="Georgia,serif"')
    for i in range(5):
        o += '<rect x="%d" y="122" width="30" height="12" rx="3" fill="%s"/>' % (378 + i * 30, CAN)
    o += txt(450, 160, "siempre igual", 18, MUT)
    return svg("0 0 640 176", "Mucho detrás del verbo " + verb + " no cambia", o)

def comp_svg(group):
    o = '<line x1="60" y1="150" x2="340" y2="150" stroke="%s" stroke-width="2"/>' % MUT
    o += '<rect x="90" y="112" width="70" height="38" rx="4" fill="%s" stroke="%s" stroke-width="2"/>' % (LINE, MUT)
    o += '<rect x="230" y="34" width="70" height="116" rx="4" fill="%s" stroke="%s" stroke-width="2"/>' % (CAN_S, CAN)
    o += txt(125, 172, "antes", 17, MUT) + txt(265, 172, "ahora", 17, MUT)
    o += '<path d="M168,112 L210,112 M210,112 L210,34 M200,34 L222,34 M200,112 L222,112" stroke="%s" stroke-width="3" fill="none"/>' % CAN
    o += txt(196, 80, "mucho", 18, CAN, "700", "end")
    o += '<text x="490" y="104" text-anchor="middle" font-size="34" font-family="Georgia,serif" font-weight="700"><tspan fill="%s">mucho</tspan><tspan fill="%s"> %s</tspan></text>' % (CAN, INK, group.split()[1])
    o += txt(490, 136, "ya compara", 18, MUT)
    return svg("0 0 640 176", "Mucho con palabras que comparan: " + group, o)

CAP_VOL = "El volumen sube. Muy no se viste: muy cansado, muy cansada, muy cansados."
CAP_NOM = "Delante de un nombre, mucho se viste como él (mucho, mucha, muchos, muchas)."
CAP_VERB = "Detrás del verbo, mucho no cambia: trabajo mucho, trabaja mucho, trabajan mucho."
CAP_COMP = "Mucho dice cuánta diferencia hay. Nunca «muy mejor»."
def pareja_svgs(p):
    a = MARK.findall(p["a"])[0][1]
    kk, b = MARK.findall(p["b"])[0]
    if p["kind"] == "nom": db, cb = nom_svg(b, p["bt"]), CAP_NOM
    elif p["kind"] == "comp": db, cb = comp_svg(b), CAP_COMP
    else:
        before = plain(p["b"].split("[c:")[0]).strip().rstrip(",")
        db, cb = verb_svg(" ".join(before.split()[-2:])), CAP_VERB
    return vol_svg(a), db, CAP_VOL, cb

def eco_cuadro(hl=None):
    cells = [("+", 1, 190, 58, "también", ECO, ECO_S), ("+", 0, 330, 58, "no", CAM, CAM_S),
             ("-", 1, 190, 156, "tampoco", ECO, ECO_S), ("-", 0, 330, 156, "sí", CAM, CAM_S)]
    o = txt(255, 30, "REPITO", 14, ECO, "700") + txt(255, 46, "pienso lo mismo", 11, MUT)
    o += txt(390, 30, "CAMBIO", 14, CAM, "700") + txt(390, 46, "pienso lo contrario", 11, MUT)
    o += txt(8, 38, "LO QUE DICE EL OTRO", 11, MUT, "700", "start")
    for sg, y, f1, f2 in (("+", 98, "Me gusta", "el mar."), ("-", 196, "No me gusta", "el frío.")):
        o += '<circle cx="22" cy="%d" r="14" fill="#fff" stroke="%s" stroke-width="2.5"/>' % (y - 4, INK)
        o += txt(22, y + 3, "+" if sg == "+" else "\u2212", 20, INK, "700")
        o += txt(44, y - 10, f1, 15, INK, "600", "start") + txt(44, y + 8, f2, 15, INK, "600", "start")
        o += txt(44, y + 26, "(positivo)" if sg == "+" else "(con no)", 11, MUT, "400", "start")
    for sg, a, x, y, w, c, soft in cells:
        on = hl is None or hl == sg + str(a)
        o += '<g opacity="%s"><rect x="%d" y="%d" width="%d" height="84" rx="12" fill="%s" stroke="%s" stroke-width="%s"/>' % (
            "1" if on else ".3", x, y, 130 if x == 190 else 120, soft, INK if (hl and on) else c, "4" if (hl and on) else "2")
        cx = x + (65 if x == 190 else 60)
        o += txt(cx, y + 34, w, 24, c, "700", extra=' font-family="Georgia,serif"')
        o += txt(cx, y + 56, "yo " + w, 12, INK) + txt(cx, y + 72, "a mí " + w, 12, INK) + '</g>'
    o += txt(230, 266, "1. ¿Qué dice el otro: + o \u2212?  2. ¿Repites o cambias?", 13, MUT)
    return '<svg class="dg cu" viewBox="0 0 460 280" role="img" aria-label="%s">%s</svg>' % (
        "El eco: si el otro dice algo positivo, repites con también o cambias con no; si dice algo con no, repites con tampoco o cambias con sí.", o)

def icon(k):
    o = '<svg class="ic" viewBox="0 0 300 140" aria-hidden="true">'
    if k == 1:
        o += bars(28, 118, 2, "#E9C98F", LINE, 0.6) + '<path d="M118,90 L146,90" stroke="%s" stroke-width="3"/><polygon points="146,83 158,90 146,97" fill="%s"/>' % (VOL, VOL)
        o += bars(166, 118, 6, VOL, LINE, 0.9)
    elif k == 2:
        o += pile(78, 118, [5, 4, 3, 2, 1], CAN, CAN_S, 8) + shirt(222, 74, "fs", 0.95, text=False)
    else:
        for x in (75, 230):
            o += '<circle cx="%d" cy="76" r="14" fill="#fff" stroke="%s" stroke-width="2.5"/>' % (x, INK)
            o += '<path d="M%d,132 q22,-40 44,0" fill="#fff" stroke="%s" stroke-width="2.5"/>' % (x - 22, INK)
        o += '<path d="M120,104 q32,-18 64,0" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="5 4"/><polygon points="184,104 172,96 174,108" fill="%s"/>' % (ECO, ECO)
        o += '<rect x="10" y="8" width="130" height="34" rx="10" fill="#fff" stroke="%s" stroke-width="2"/>' % INK + txt(75, 30, "No me gusta...", 14)
        o += '<rect x="166" y="8" width="128" height="34" rx="10" fill="%s" stroke="%s" stroke-width="2"/>' % (ECO_S, ECO) + txt(230, 30, "A mí tampoco.", 14, ECO, "700")
    return o + '</svg>'

def cards():
    txts = [("¿CÓMO? → MUY", "El volumen", "Sube la intensidad de un <b>adjetivo</b> o de un <b>adverbio</b>. No se viste nunca: muy alto, muy alta, muy altos.", "[m:muy cansada] · [m:muy lejos] · [m:muy bien]"),
            ("¿CUÁNTO? → MUCHO", "La cantidad", "Delante de un <b>nombre</b> se pone su camiseta. Detrás del <b>verbo</b> no cambia.", "[c:mucha gente] · [c:muchos amigos] · trabajo [c:mucho]"),
            ("¿ESTÁS DE ACUERDO?", "El eco", "Repites lo que dice el otro (<b>también, tampoco</b>) o cambias (<b>sí, no</b>).", "—No me gusta el frío. —[t:A mí tampoco].")]
    o = '<div class="cams">'
    for i, (k, h, p, ej) in enumerate(txts):
        o += '<div class="cam c%d"><div class="k0">%s</div><h3>%s</h3>%s<p>%s</p><div class="ej">%s</div></div>' % (i + 1, k, h, icon(i + 1), p, mk(ej))
    return o + '</div>'

def lado():
    o = '<div class="lado">'
    for t, cl, items in B.LADO:
        o += '<div class="%s"><h4>%s</h4><ul>%s</ul></div>' % (cl, t, "".join("<li>%s</li>" % mk(x) for x in items))
    return o + '</div>'

def cierres():
    o = '<div class="cier">'
    for t, bien, mal, why in B.CIERRES:
        o += '<div class="box"><h4>%s</h4><p class="ex"><span class="okm" aria-hidden="true">✓</span> %s%s</p><p class="small muted" style="margin:0">%s</p></div>' % (
            t, mk(bien), (' &nbsp; <span class="badm"><span aria-hidden="true">✗</span> <s>%s</s></span>' % mal) if mal else "", mk(why))
    return o + '</div>'

def yo_ami():
    o = '<div class="yoami">'
    for k, h, sub in (("yo", "YO también / tampoco / sí / no", "con los verbos normales: vivir, tener, trabajar, saber, ir..."),
                      ("ami", "A MÍ también / tampoco / sí / no", "con gustar y sus amigos: " + B.GUSTAR_AMIGOS)):
        o += '<div class="box"><h4>%s</h4><p class="small muted" style="margin:0 0 6px">%s</p><ul class="dl">' % (h, sub)
        for f, r in B.YO_AMI[k]: o += '<li><span class="exm">—%s</span> —%s</li>' % (f, mk(r))
        o += '</ul></div>'
    return o + '</div>'

def tampoco():
    return '<ul class="tl">' + "".join('<li>%s<br><span class="small muted">%s</span></li>' % (mk(f), why) for f, why in B.TAMPOCO) + '</ul>'

def devolver():
    return '<div class="tw"><table class="t"><tbody>' + "".join('<tr><td><b class="kt">%s</b></td><td class="small">%s</td></tr>' % (a, b) for a, b in B.DEVOLVER) + '</tbody></table></div>'

def donde():
    return "".join('<div class="box"><span class="chip">%s</span><p class="small muted" style="margin:6px 0">%s</p><p style="margin:0">%s</p></div>' % (c, d, mk(s)) for c, d, s in B.DONDE)

def errores():
    o = '<div class="errs">'
    for mal, bien, why in B.ERRORES:
        o += '<div class="err"><div class="mal"><span aria-hidden="true">✗</span> <s>%s</s></div><div class="bien"><span aria-hidden="true">✓</span> %s</div><div class="small muted">%s</div></div>' % (mal, mk(bien), why)
    return o + '</div>'

LEG = ('<div class="legend"><span><span class="k m">muy</span> el volumen</span><span><span class="k c">mucho</span> la cantidad</span>'
       '<span><span class="k t">también / tampoco</span> repito</span><span><span class="k x">sí / no</span> cambio</span></div>')

CSS_R = CSS + r"""
:root{--vo:#B7791F;--vo-soft:#FBF0DA;--ca:#17707F;--ca-soft:#DDF0F2;--ec:#1D5FA8;--ec-soft:#E2ECF8;--cb:#C2492A;--cb-soft:#FCE9E1}
.k{border-radius:4px;padding:0 3px 1px;border-bottom:3px solid;line-height:1.9}
.k.m{background:var(--vo-soft);border-color:var(--vo)}.k.c{background:var(--ca-soft);border-color:var(--ca)}
.k.t{background:var(--ec-soft);border-color:var(--ec)}.k.x{background:var(--cb-soft);border-color:var(--cb)}
.kt{color:var(--ec)}
.cams{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;border-top:6px solid var(--vo)}
.cam.c2{border-top-color:var(--ca)}.cam.c3{border-top-color:var(--ec)}
.cam .k0{font-size:.78rem;font-weight:700;letter-spacing:.06em;color:var(--muted)}
.cam h3{margin:2px 0 6px}.cam p{margin:0;font-size:.95rem}
.cam .ej{margin-top:8px;font-size:.92rem;background:var(--paper);border-radius:8px;padding:6px 10px}
.cam svg.ic{width:100%;max-width:260px;height:auto;display:block;margin:6px auto 10px}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.box h4{margin:0 0 4px}.box .ex{margin:4px 0 6px}
.okm{color:var(--ok);font-weight:700}.badm{color:var(--bad)}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pill.ok{border-color:var(--ok)}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.duo button{font:inherit;text-align:left;border:2px solid var(--line);background:#fff;border-radius:10px;padding:10px 12px;cursor:pointer;line-height:1.6}
.duo button.on.m{border-color:var(--vo);background:var(--vo-soft)}.duo button.on.c{border-color:var(--ca);background:var(--ca-soft)}
.duo button.on.t{border-color:var(--ec);background:var(--ec-soft)}.duo button.on.x{border-color:var(--cb);background:var(--cb-soft)}
.duo button small{display:block;font-size:.75rem;font-weight:700;letter-spacing:.05em;color:var(--muted);margin-bottom:2px}
svg.dg{width:100%;height:auto;display:block;margin:6px 0}
svg.cu{max-width:560px;margin:6px auto}
.cap{text-align:center;font-size:.85rem;color:var(--muted);margin:0 0 6px}
.expl{border-radius:8px;padding:10px 14px;margin-top:6px;background:var(--paper)}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;margin:8px 0}
.lado{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-bottom:22px}
.lado>div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:.93rem;border-top:5px solid var(--vo)}
.lado>div.can{border-top-color:var(--ca)}
.lado h4{margin:0 0 6px}.lado ul{margin:0;padding-left:1.1em}.lado li{margin:3px 0}
.cier{display:grid;grid-template-columns:1fr 1fr;gap:0 12px}.cier .box{margin:8px 0}
.yoami{display:grid;grid-template-columns:1fr 1fr;gap:0 12px}.yoami .box{margin:8px 0}
.dl{list-style:none;padding:0;margin:0}.dl li{padding:4px 0;border-bottom:1px dashed var(--line)}
.exm{color:var(--muted)}
.tl{padding-left:1.1em}.tl li{margin:8px 0}
.tw{overflow-x:auto}
.res{font-family:Georgia,serif;font-size:2rem;font-weight:700;text-align:center;margin:6px 0}
.res2{text-align:center;font-size:1.05rem;margin:0 0 8px}
.why2{background:var(--paper);border-radius:8px;padding:8px 12px;font-size:.93rem}
.errs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.err{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.err .mal{color:var(--bad)}.err .bien{margin:4px 0}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.vchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px}
.vchip.vol{background:var(--vo-soft);color:#7A4E0E}.vchip.can{background:var(--ca-soft);color:var(--ca)}.vchip.eco{background:var(--ec-soft);color:var(--ec)}
.qz{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0}
.qz .cnt{font-size:.85rem;color:var(--muted)}
.qz .qq{font-size:1.05rem;margin:6px 0 10px}
.qz .ops{display:grid;gap:8px}
.qz .ops.three{grid-template-columns:repeat(3,1fr)}
.qz .ops button{font:inherit;text-align:center;font-weight:600;border:2px solid var(--line);background:#fff;border-radius:10px;padding:9px 12px;cursor:pointer}
.qz .ops.bm{grid-template-columns:1fr 1fr}
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
.check{list-style:none;padding:0;margin:8px 0}.check li{padding:5px 0}.check label{cursor:pointer}
.ophoto{display:grid;grid-template-columns:1.2fr 1fr;gap:16px;align-items:start}
figure.ph{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;padding:8px}
figure.ph img{width:100%;height:auto;display:block;border-radius:8px}
figure.ph figcaption{font-size:.85rem;color:var(--muted);padding:6px 4px 0}
figure.ph .alt{display:none;font-size:.95rem;padding:12px;background:var(--paper);border-radius:8px}
figure.ph.miss img{display:none}figure.ph.miss .alt{display:block}
.ocard{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px}
.ocard .ph1{font-family:Georgia,serif;font-size:1.15rem;font-weight:700}
.exq{font-family:Georgia,serif;font-size:1.5rem;font-weight:700;margin:10px 0;line-height:1.35}
.exq small{display:block;font-family:system-ui,sans-serif;font-size:.8rem;letter-spacing:.06em;color:var(--muted);font-weight:700}
.task{display:inline-block;font-weight:700;border-radius:999px;padding:3px 14px;margin:4px 0 8px}
.task.t{background:var(--ec-soft);color:var(--ec)}.task.x{background:var(--cb-soft);color:var(--cb)}
.clock{font-family:Georgia,serif;font-size:1.6rem;font-weight:700;font-variant-numeric:tabular-nums}
.tbar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:8px 0}
.tbar i{display:block;height:100%;background:var(--coral);width:0;transition:width .25s linear}
.esc{display:grid;gap:6px;margin:8px 0}
.esc div{border:2px dashed var(--line);border-radius:8px;padding:6px 10px;color:var(--muted);font-size:.95rem}
.esc div.on{border-style:solid;border-color:var(--coral);color:var(--ink);background:var(--coral-soft)}
.words{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}
.words span{font-size:.85rem;background:var(--ca-soft);color:var(--ca);border-radius:999px;padding:2px 10px}
.words span.m{background:var(--vo-soft);color:#7A4E0E}
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
@media (max-width:760px){.ophoto{grid-template-columns:1fr}}
@media (max-width:700px){.cams,.errs,.cier,.yoami,.lado{grid-template-columns:1fr}.duo{grid-template-columns:1fr}.qz .ops.three{grid-template-columns:1fr}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:13px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.lado>div,.err{break-inside:avoid}}
"""

STEPS = [("idea", "Muy y mucho"), ("eco", "También y tampoco"), ("examen", "En el examen"), ("practica", "Practica"),
         ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_IDEA = """
<h2>¿Cómo? Muy. ¿Cuánto? Mucho.</h2>
<p class="lead">Dos preguntas te dicen qué palabra va. Si hablas de <b>cómo</b> es o está algo, subes el <b>volumen</b>: <b>muy</b>. Si hablas de <b>cuánto</b> hay o cuánto haces algo, es una <b>cantidad</b>: <b>mucho</b>. Y para no fallar, mira siempre la palabra de al lado.</p>
__CARDS__
__LEG__
<h3>Mira la diferencia</h3>
<p class="muted small">Elige un tema y toca las dos frases: una con muy y otra con mucho. Mira el dibujo de cada una.</p>
<div class="pills" id="parsel"></div>
<div class="box" id="parvis"></div>
<h3>¿Qué va al lado?</h3>
<p>Mira la palabra que va con muy o con mucho: ella decide.</p>
__LADO__
<div class="tip"><b>El truco:</b> antes de escribir muy o mucho, mira la palabra de al lado. ¿Un adjetivo o un adverbio (bonita, cansado, lejos, bien)? <b>Muy</b>. ¿Un nombre (gente, tiempo, amigos)? <b>Mucho</b> con su camiseta. ¿Un verbo o nada (me gusta, trabajo, «sí, ...»)? <b>Mucho</b>.</div>
<h3>Cuidado con...</h3>
__CIERRES__
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="eco">Siguiente: también y tampoco</button></div>
"""

V_ECO = """
<h2>El eco: también, tampoco, sí y no</h2>
<p class="lead">Alguien dice algo y tú reaccionas. Es como un eco: primero escuchas <b>qué dice el otro</b>: ¿es positivo (+) o lleva <i>no</i> (−)? Después decides: ¿<b>repites</b> lo mismo o <b>cambias</b>?</p>
__CUADRO__
<div class="tip"><b>Repito:</b> también después de algo positivo; <b>tampoco</b> después de un no. <b>Cambio:</b> <b>no</b> después de algo positivo; <b>sí</b> después de un no.</div>
<h3>Pruébalo</h3>
<p class="muted small">Elige lo que dice el otro y si piensas lo mismo o lo contrario. Mira tu respuesta.</p>
<div class="pills" id="ecosel"></div>
<div class="duo" id="ecoduo"></div>
<div class="box" id="ecovis" aria-live="polite"></div>
<h3>¿Yo o a mí?</h3>
<p>Lo decide el verbo de la frase del otro. ¿Empieza con <b>me / te / le</b> (me gusta, me encanta, me interesa, me duele)? Entonces tú contestas con <b>a mí</b>. ¿Es un verbo normal (vivo, tengo, sé, trabajo)? Contestas con <b>yo</b>.</p>
__YOAMI__
<h3>Tampoco ya es un no</h3>
<p>Tampoco = también + no. Por eso nunca va con otro <i>no</i> delante: «también no» y «tampoco no» no existen.</p>
__TAMPOCO__
<h3>Devuelve la pregunta</h3>
<p>En la tarea 3 de la oral, reacciona y después pregunta tú. Así el diálogo sigue y no contestas solo «sí» o «no».</p>
__DEVOLVER__
<div class="row"><button class="btn cta" data-go="examen">Siguiente: en el examen</button></div>
"""

V_EXAMEN = """
<h2>Dónde sale en el examen</h2>
<p class="lead">Muy, mucho, también y tampoco salen en casi todas las tareas: cuando describes, cuando cuentas qué te gusta y, sobre todo, cuando hablas con el examinador. Son palabras pequeñas, pero el examinador las oye y las ve muchas veces.</p>
__LEG__
__DONDE__
<h3>Los errores más típicos</h3>
<p>Tienes que reconocerlos en tus textos y en tu oral. Mira por qué fallan.</p>
__ERRORES__
<div class="tip"><b>Para la revisión final (5 minutos):</b> busca cada <b>muy</b> y cada <b>mucho</b> y mira la palabra de al lado. Es la pasada 6 de la lista de revisión.</div>
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACT = """
<h2>Practica</h2>
<p class="lead">Cuatro ejercicios. Cada respuesta se corrige en el momento, con la explicación.</p>
<div class="pills" id="exsel">
 <button class="pill on" data-act="ex" data-k="p1">1. ¿Muy o mucho?</button>
 <button class="pill" data-act="ex" data-k="p2">2. ¿Qué dices tú?</button>
 <button class="pill" data-act="ex" data-k="e2">3. Textos del examen</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Ahora úsalo en una tarea del examen: escribe un texto, reacciona en voz alta a lo que dice el examinador o describe una foto.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="r">Oral: reacciona</button>
 <button class="pill" data-act="at" data-k="o">Oral: la foto</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu texto y después pulsa <b>Revisar muy, mucho, también y tampoco</b>: la página busca los errores típicos (mucho bonito, muy gente, me gusta muy, yo también no...). No corrige el texto entero: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="atr" hidden>
 <p>Como en la tarea 3 de la oral: el examinador dice algo y tú reaccionas <b>en voz alta</b>, rápido. La página te dice si piensas lo mismo o lo contrario. Primero reacciona (¿yo o a mí? ¿también, tampoco, sí o no?); después añade un detalle o devuelve la pregunta.</p>
 <div id="rxbox"></div>
</div>
<div id="ato" hidden>
 <p>Como en la tarea 2 de la oral: describe la foto <b>un minuto</b> en voz alta. Usa muy (cómo son, cómo están) y mucho (qué hay, qué hacen).</p>
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
  <label><input type="radio" name="o1" value="El volumen y la cantidad">El volumen y la cantidad</label>
  <label><input type="radio" name="o1" value="El eco (también, tampoco)">El eco (también, tampoco)</label>
  <label><input type="radio" name="o1" value="En el examen y los errores típicos">En el examen y los errores típicos</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tú">Ahora tú</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué te cuesta más ahora?</label>
 <div class="chips" role="group" aria-labelledby="o2l">
  <label><input type="radio" name="o2" value="Muy o mucho">Muy o mucho</label>
  <label><input type="radio" name="o2" value="Mucho, mucha, muchos, muchas">Mucho, mucha, muchos, muchas</label>
  <label><input type="radio" name="o2" value="Hace frío, tengo hambre">Hace frío, tengo hambre</label>
  <label><input type="radio" name="o2" value="También o tampoco">También o tampoco</label>
  <label><input type="radio" name="o2" value="Yo o a mí">Yo o a mí</label>
  <label><input type="radio" name="o2" value="Reaccionar rápido al hablar">Reaccionar rápido al hablar</label>
 </div>
 <label class="q" id="o3l">3. ¿Te ayudan las ideas del «volumen», la «cantidad» y el «eco»?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con muy, mucho, también y tampoco? (1 = nada, 10 = total)</label>
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
    o = '<h2>Muy y mucho, también y tampoco · resumen</h2>' + cards() + LEG
    o += '<h3>¿Qué va al lado?</h3>' + lado() + '<h3>Cuidado con...</h3>' + cierres()
    o += '<h3>El eco</h3>' + eco_cuadro() + yo_ami() + tampoco()
    o += '<h3>Los errores típicos</h3>' + errores()
    return o

views = {
    "idea": V_IDEA.replace("__CARDS__", cards()).replace("__LEG__", LEG).replace("__LADO__", lado()).replace("__CIERRES__", cierres()),
    "eco": V_ECO.replace("__CUADRO__", eco_cuadro()).replace("__YOAMI__", yo_ami()).replace("__TAMPOCO__", tampoco()).replace("__DEVOLVER__", devolver()),
    "examen": V_EXAMEN.replace("__LEG__", LEG).replace("__DONDE__", donde()).replace("__ERRORES__", errores()),
    "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R05</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
""".replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

# ------------------------------------------------------------------ DATOS PARA EL SCRIPT
def parejas_data():
    out = []
    for p in B.PAREJAS:
        da, db, ca, cb = pareja_svgs(p)
        out.append({"tema": p["tema"], "a": mk(p["a"]), "b": mk(p["b"]), "da": da, "db": db, "ca": ca, "cb": cb, "ea": p["ea"], "eb": p["eb"]})
    return out

def eco_data(lst):
    return [{"f": e["f"], "s": e["s"], "g": e["g"], "c1": corto(e["s"], e["g"], 1), "c0": corto(e["s"], e["g"], 0), "l1": e["igual"], "l0": e["dif"]} for e in lst]

DATA = {
    "key": STORAGE, "title": TITLE,
    "steps": [{"id": k, "label": l} for k, l in STEPS],
    "motivos": {k: {"f": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "familias": B.FAMILIAS,
    "parejas": parejas_data(),
    "eco": eco_data(B.ECO_FRASES),
    "cuadros": {k: eco_cuadro(k) for k in ("+1", "+0", "-1", "-0")},
    "qz": {
        "p1": {"items": B.P_MM, "n": 8, "name": "¿Muy o mucho?", "three": True, "info": "Mira la palabra de al lado: ¿adjetivo o adverbio (muy)? ¿Nombre o verbo (mucho)?"},
        "p2": {"items": [{k: v for k, v in it.items() if k in ("q", "o", "why")} for it in B.P_ECO], "n": 8, "name": "¿Qué dices tú?", "three": True,
               "info": "¿Qué dice el otro: + o −? ¿Repites o cambias? ¿Yo o a mí?"},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Errores típicos de los exámenes. ¿La frase está bien o mal?"},
    },
    "textos": B.TEXTOS,
    "laminas": B.LAMINAS, "focos": B.FOCOS, "detector": B.DETECTOR,
    "oral": eco_data(B.ORAL),
    "fotos": [{"id": f["id"], "titulo": f["titulo"], "alt": f["alt"], "img": IMG_T2 % f["id"], "mm": mk(f["mm"])} for f in B.FOTOS],
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function blank(){ return {cur:'idea', seen:{}, par:0, pv:'a', eco:0, ea:1, ex:'p1', etext:D.textos[0].id, at:'w',
  qz:{}, qlog:{}, cz:{}, w:{}, wchk:{}, wrev:{}, lam:D.laminas[0].id, foto:D.fotos[0].id, fph:{}, fchk:{},
  rxc:{n:8,t:6}, rx:null, rxlog:[], o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }

/* ---------------- navegacion ---------------- */
function stepDone(id){
 if(id==='practica') return ['p1','p2','e4'].some(function(k){ return !!S.qlog[k]; }) || Object.keys(S.cz).length>0;
 if(id==='ahora') return Object.keys(S.w).some(function(k){ return (S.w[k]||'').trim().length>20; }) || S.rxlog.length>0 || Object.keys(S.fph).some(function(k){ return S.fph[k]>=2; });
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
 stopTimer(); if(S.rx && S.rx.ph<3 && S.rx.i<S.rx.deck.length){ RXRUN=false; }
 nav(); if(id==='ahora') renderAt(); window.scrollTo(0,0);
}

/* ---------------- 1. muy y mucho: parejas ---------------- */
function renderPar(){
 var o=''; D.parejas.forEach(function(p,i){ o+='<button class="pill'+(S.par===i?' on':'')+'" data-act="par" data-i="'+i+'">'+esc(p.tema)+'</button>'; });
 $('parsel').innerHTML=o;
 var p=D.parejas[S.par], v=S.pv;
 $('parvis').innerHTML='<div class="duo">'+
  '<button class="m'+(v==='a'?' on':'')+'" data-act="pv" data-v="a" aria-pressed="'+(v==='a')+'"><small>¿CÓMO? · MUY</small>'+p.a+'</button>'+
  '<button class="c'+(v==='b'?' on':'')+'" data-act="pv" data-v="b" aria-pressed="'+(v==='b')+'"><small>¿CUÁNTO? · MUCHO</small>'+p.b+'</button></div>'+
  (v==='a'?p.da:p.db)+'<p class="cap">'+(v==='a'?p.ca:p.cb)+'</p><div class="expl" aria-live="polite">'+(v==='a'?p.ea:p.eb)+'</div>';
}

/* ---------------- 2. el eco: constructor ---------------- */
function renderEco(){
 var o=''; D.eco.forEach(function(e,i){ o+='<button class="pill'+(S.eco===i?' on':'')+'" data-act="eco" data-i="'+i+'">'+esc(e.f)+'</button>'; });
 $('ecosel').innerHTML=o;
 $('ecoduo').innerHTML='<button class="t'+(S.ea===1?' on':'')+'" data-act="ea" data-a="1" aria-pressed="'+(S.ea===1)+'"><small>REPITO</small>Pienso lo mismo</button>'+
  '<button class="x'+(S.ea===0?' on':'')+'" data-act="ea" data-a="0" aria-pressed="'+(S.ea===0)+'"><small>CAMBIO</small>Pienso lo contrario</button>';
 var e=D.eco[S.eco], a=S.ea, c=a?e.c1:e.c0, l=a?e.l1:e.l0, cls=a?'t':'x';
 var why = (e.s==='+'?'Lo que dice es <b>positivo (+)</b>. ':'Lo que dice lleva <b>no (−)</b>. ');
 why += a ? (e.s==='+'?'Piensas lo mismo: repites con <b>también</b>. ':'Piensas lo mismo: repites el no con <b>tampoco</b>. ') : (e.s==='+'?'Piensas lo contrario: cambias con <b>no</b>. ':'Piensas lo contrario: cambias con <b>sí</b>. ');
 why += e.g ? 'El verbo es como gustar (me gusta, me encanta, me interesa...): <b>a mí</b>.' : 'Es un verbo normal (vivo, tengo, sé, hago...): <b>yo</b>.';
 $('ecovis').innerHTML = D.cuadros[e.s+a] + '<p class="res2"><span class="exm">—'+esc(e.f)+'</span></p><div class="res"><span class="k '+cls+'">'+esc(c.replace(/\.$/,''))+'</span>.</div>'+
  '<p class="res2">'+esc(l)+' <span class="muted small">'+(e.g?'¿Y a ti?':'¿Y tú?')+'</span></p><div class="why2">'+why+'</div>';
}

/* ---------------- motor de opcion multiple ---------------- */
function qzNew(k){ var c=D.qz[k]; S.qz[k]={order:shuffle(range(c.items.length)).slice(0,c.n), i:0, res:[], perm:{}}; save(); }
function qzRender(k, box){
 var c=D.qz[k]; if(!S.qz[k]) qzNew(k);
 var st=S.qz[k], N=st.order.length;
 if(st.i>=N){
  var ok=st.res.filter(function(r){return r.ok;}).length, fails=st.res.filter(function(r){return !r.ok;});
  var msg = ok>=N-1 ? '¡Muy bien! Lo tienes claro.' : (ok>=Math.ceil(N*0.6) ? 'Bien. Mira otra vez las explicaciones de las que has fallado.' : 'Vuelve a mirar la idea y repite con otras frases.');
  var o='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+msg+'</p>';
  if(fails.length){ o+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fails.forEach(function(r){ var it=c.items[r.k]; o+='<li>'+esc(strip(it.q).slice(0,90))+' → <b>'+(c.bm?(it.ok?'Mal: '+strip(it.fix):'Bien'):esc(it.o[0]))+'</b></li>'; }); o+='</ul>'; }
  o+='<div class="row"><button class="btn cta" data-act="qrep" data-k="'+k+'">Repetir con otras frases</button></div></div>';
  box.innerHTML=o; return;
 }
 var idx=st.order[st.i], it=c.items[idx], ans=st.res[st.i];
 var opts, ok;
 if(c.bm){ opts=[[0,'Bien'],[1,'Mal']]; ok=it.ok; }
 else { if(!st.perm[idx]){ st.perm[idx]=shuffle(range(it.o.length)); save(); } opts=st.perm[idx].map(function(j){ return [j,it.o[j]]; }); ok=0; }
 var q=esc(it.q);
 if(ans && !c.bm){ q=q.replace(/____/g, '<b style="color:var(--ok)">'+esc(it.o[0])+'</b>'); }
 var o='<div class="qz"><div class="cnt">'+esc(c.name)+' · '+(st.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(st.i/N*100)+'%"></i></div>';
 o+='<div class="qq">'+q+'</div><div class="ops'+(c.bm?' bm':(c.three?' three':''))+'" role="group">';
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
  var mo=D.motivos[g.m], fn=D.familias[mo.f];
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
var EXINFO={e2:'Textos como los del examen: un correo, un blog, un diálogo de la tarea 3 y la descripción de una foto. Elige la palabra de cada hueco: la corrección sale enseguida, con el motivo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
var CH=['Delante de cada adjetivo o adverbio (bonito, cansada, lejos, bien) he puesto muy, no mucho.','Delante de un nombre, mucho lleva su camiseta: mucha gente, muchos amigos, muchas veces.','Con el verbo (me gusta, trabajo) he puesto mucho, nunca muy.','Hace mucho frío, tengo mucha hambre: con hacer y tener, mucho.','Para repetir un no: tampoco (nunca «también no»).','Con gustar, encantar, interesar: a mí también / a mí tampoco.'];
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+'</div>';
 if(L.intro) h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(f){ return '<span class="vchip '+f+'">'+D.focos[f]+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas de color te dicen qué pide cada pauta. Recuerda: unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu texto</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar muy, mucho, también y tampoco</button></div><div id="rvbox" aria-live="polite"></div>';
 h+='<h3>Mi lista de muy, mucho, también y tampoco</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
function detect(s){ var n=norm(s), out=[]; D.detector.forEach(function(d){ var r=new RegExp(d.re,'g'), m; while((m=r.exec(n))){ out.push({d:d, a:m.index, w:m[0]}); if(r.lastIndex===m.index) r.lastIndex++; } }); return out; }
window.__R05detect = function(s){ var ids={}; detect(s).forEach(function(x){ ids[x.d.id]=1; }); return Object.keys(ids).sort(); };
function review(){
 var L=lam(), txt=$('wtext').value, out=[], red=0, amb=0;
 if(txt.trim().length<20){ $('rvbox').innerHTML='<ul class="rv"><li class="a">Escribe primero tu texto.</li></ul>'; return; }
 var sents=txt.match(/[^.!?\n]+[.!?]*/g)||[];
 sents.forEach(function(s){
  if(!s.trim()) return;
  detect(s).forEach(function(x){
   if(x.d.t==='r') red++; else amb++;
   var hl=esc(s.slice(0,x.a))+'<mark>'+esc(s.substr(x.a,x.w.length))+'</mark>'+esc(s.slice(x.a+x.w.length));
   out.push('<li class="'+x.d.t+'">'+(x.d.t==='r'?'<b>¡Ojo!</b> ':'<b>Mira esto:</b> ')+x.d.msg+'<br><span class="small">'+hl+'</span></li>');
  });
 });
 var nt=norm(txt);
 var nmuy=(nt.match(/\bmuy\b/g)||[]).length, nmu=(nt.match(/\b(mucho|mucha|muchos|muchas|muchisimo|muchisima)\b/g)||[]).length;
 var neco=(nt.match(/\b(tambien|tampoco)\b|\b(yo|a mi)\s+(si|no)\b/g)||[]).length;
 var pide=function(f){ return L.pautas.some(function(p){ return p[1].indexOf(f)>=0; }); };
 if(pide('eco') && !neco){ amb++; out.push('<li class="a"><b>Reaccionar:</b> la lámina te pide decir qué tenéis en común y qué no. Usa <b>yo también</b>, <b>a mí tampoco</b>, <b>yo no</b>, <b>a mí sí</b>...</li>'); }
 if(pide('vol') && !nmuy){ amb++; out.push('<li class="a"><b>Muy:</b> no lo has usado. Para decir cómo es algo: «es muy bonito», «está muy cerca».</li>'); }
 if(pide('can') && !nmu){ amb++; out.push('<li class="a"><b>Mucho:</b> no lo has usado. Para decir cuánto: «hay muchas tiendas», «me gusta mucho».</li>'); }
 if(!red) out.unshift('<li class="g">No he encontrado los errores típicos. ¡Bien! Has usado muy '+nmuy+' '+(nmuy===1?'vez':'veces')+', mucho '+nmu+' '+(nmu===1?'vez':'veces')+' y '+neco+' '+(neco===1?'reacción':'reacciones')+'. Mira tú también la lista de abajo.</li>');
 var wc=txt.trim().split(/\s+/).length;
 S.wrev[L.id]={red:red, amb:amb, muy:nmuy, mucho:nmu, eco:neco, words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul><p class="muted small">Tu texto: '+wc+' palabras (la lámina pide '+L.palabras[0]+'-'+L.palabras[1]+'). La página solo busca estos errores: no los ve todos. Tu profesora corrige el texto completo.</p>';
}

/* ---------------- relojes ---------------- */
var TM=null, RXRUN=false;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } RXRUN=false; }
function clockTxt(s){ s=Math.max(0,Math.ceil(s)); return Math.floor(s/60)+':'+(s%60<10?'0':'')+(s%60); }

/* ---------------- ahora tu: oral 1, reacciona ---------------- */
var DET_T=8;
function rxNew(){
 var n=S.rxc.n, ks=shuffle(range(D.oral.length)).slice(0,n), as=shuffle(range(n).map(function(i){ return i%2; }));
 S.rx={deck:ks.map(function(k,i){ return {k:k, a:as[i]}; }), i:0, ph:1, res:[]}; save();
}
function renderRx(){
 var box=$('rxbox'), R=S.rx, h='';
 if(!R){
  h+='<div class="ocard"><div class="ph1">Prepárate</div><p>El examinador dice una frase. Arriba ves si <b>piensas lo mismo</b> o <b>lo contrario</b>. Tienes poco tiempo: ¡reacciona en voz alta!</p>';
  h+='<p class="small"><b>Tarjetas:</b></p><div class="pills">'+[8,12,16].map(function(n){ return '<button class="pill'+(S.rxc.n===n?' on':'')+'" data-act="rxn" data-n="'+n+'">'+n+'</button>'; }).join('')+'</div>';
  h+='<p class="small"><b>Tiempo para reaccionar:</b></p><div class="pills">'+[4,6,8].map(function(t){ return '<button class="pill'+(S.rxc.t===t?' on':'')+'" data-act="rxt" data-t="'+t+'">'+t+' s</button>'; }).join('')+'</div>';
  h+='<p class="small muted">Después de reaccionar tienes '+DET_T+' s más para añadir un detalle o devolver la pregunta (¿y tú? / ¿y a ti?).</p>';
  h+='<div class="row"><button class="btn cta" data-act="rxstart">Empezar</button></div>';
  if(S.rxlog.length){ h+='<p class="hist"><b>Tus últimas prácticas:</b> '+S.rxlog.map(function(r){ return r.d+': '+r.ok+'/'+r.n+' ('+r.t+' s)'; }).join(' · ')+'</p>'; }
  box.innerHTML=h+'</div>'; return;
 }
 var N=R.deck.length;
 if(R.i>=N){
  var ok=R.res.filter(function(r){ return r.ok; }).length;
  h+='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+(ok>=N-1?'¡Muy bien! Reaccionas rápido y bien.':'Mira otra vez «El eco» y repite: la rapidez llega con la práctica.')+'</p>';
  var fl=R.res.filter(function(r){ return !r.ok; });
  if(fl.length){ h+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fl.forEach(function(r){ var o=D.oral[r.k]; h+='<li>«'+esc(o.f)+'» → <b>'+esc(r.a?o.c1:o.c0)+'</b></li>'; }); h+='</ul>'; }
  h+='<div class="row"><button class="btn cta" data-act="rxagain">Otra vez</button></div></div>';
  box.innerHTML=h; return;
 }
 var c=R.deck[R.i], o=D.oral[c.k];
 h+='<div class="ocard"><div class="cnt small muted">Tarjeta '+(R.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(R.i/N*100)+'%"></i></div>';
 h+='<div class="exq"><small>EL EXAMINADOR</small>«'+esc(o.f)+'»</div>';
 h+='<span class="task '+(c.a?'t">✓ Piensas lo mismo':'x">✗ Piensas lo contrario')+'</span>';
 if(R.ph<3){
  h+='<div class="clock" id="rxclk">'+clockTxt(R.ph===1?S.rxc.t:DET_T)+'</div><div class="tbar"><i id="rxbar"></i></div>';
  h+='<div class="esc"><div class="'+(R.ph===1?'on':'')+'">1 · Reacciona: ¿yo o a mí? ¿también, tampoco, sí o no?</div><div class="'+(R.ph===2?'on':'')+'">2 · Añade un detalle o devuelve la pregunta: ¿y tú? / ¿y a ti?</div></div>';
  h+='<div class="row">'+(RXRUN?'':'<button class="btn" data-act="rxgo">Seguir con el reloj</button>')+'<button class="btn cta" data-act="rxskip">Ya está</button></div>';
 } else {
  var cls=c.a?'t':'x', sh=c.a?o.c1:o.c0, lg=c.a?o.l1:o.l0;
  h+='<div class="model"><b>Una respuesta modelo:</b><br><span class="k '+cls+'">'+esc(sh.replace(/\.$/,''))+'</span>.'+esc(lg.slice(sh.length))+' <span class="muted">'+(o.g?'¿Y a ti?':'¿Y tú?')+'</span></div>';
  h+='<p class="small" style="margin-top:12px"><b>¿Lo has dicho bien?</b> (¿también, tampoco, sí o no? ¿yo o a mí?)</p>';
  h+='<div class="row"><button class="btn cta" data-act="rxeval" data-ok="1">✓ Sí</button><button class="btn" data-act="rxeval" data-ok="0">✗ Me he equivocado</button></div>';
 }
 box.innerHTML=h+'</div>';
}
function rxRun(){
 stopTimer(); var R=S.rx; if(!R || R.ph>=3) return;
 RXRUN=true; renderRx();
 var T0=Date.now(), dur=R.ph===1?S.rxc.t:DET_T;
 TM=setInterval(function(){
  var t=(Date.now()-T0)/1000, bar=$('rxbar'), ck=$('rxclk'); if(!bar){ stopTimer(); return; }
  ck.textContent=clockTxt(dur-t); bar.style.width=Math.min(100,t/dur*100)+'%';
  if(t>=dur){ rxNext(); }
 }, 200);
}
function rxNext(){ stopTimer(); var R=S.rx; R.ph++; save(); if(R.ph<3) rxRun(); else renderRx(); }

/* ---------------- ahora tu: oral 2, la foto ---------------- */
var TDUR=60;
var ESC=['0 s · ¿Qué hay? «En la foto hay mucha gente / muchas cosas / poca gente...»','20 s · ¿Cómo son? ¿Cómo están? «Es muy..., parece muy..., está muy...»','40 s · ¿Qué hacen? «Trabaja mucho, le gusta mucho..., creo que...»'];
var WORDS=[['m','muy contento / contenta'],['m','muy cansado / cansada'],['m','muy tranquilo / tranquila'],['m','muy bien, muy temprano, muy tarde'],['c','mucha gente'],['c','muchas cosas, muchas personas'],['c','muchos años, muchos amigos'],['c','hace mucho sol / calor / frío'],['c','tiene mucha prisa'],['c','le gusta mucho, trabaja mucho']];
var FCH=['He empezado con «En la foto hay...».','He usado muy con adjetivos (muy contentos, muy nerviosa).','He usado mucho con nombres, con su camiseta (mucha gente, muchos años).','Con los verbos he dicho mucho (le gusta mucho, trabajan mucho).'];
function foto(){ return D.fotos.filter(function(f){return f.id===S.foto;})[0]; }
function renderFoto(){
 var o=''; D.fotos.forEach(function(f){ var d=(S.fph[f.id]||0)>=2; o+='<button class="pill'+(S.foto===f.id?' on':'')+(d?' ok':'')+'" data-act="foto" data-id="'+f.id+'">'+esc(f.titulo)+(d?' ✓':'')+'</button>'; });
 $('fosel').innerHTML=o;
 var f=foto(), ph=S.fph[f.id]||0;
 var h='<div class="ophoto"><figure class="ph" id="fig"><img src="'+f.img+'" alt="'+esc(f.alt)+'" loading="lazy"><div class="alt"><b>Foto:</b> '+esc(f.alt)+'</div><figcaption>'+esc(f.titulo)+'</figcaption></figure><div class="ocard">';
 if(ph===0){
  h+='<div class="ph1">Prepárate</div><p>Mira la foto unos segundos. Vas a hablar <b>un minuto</b>. En cada frase, pregúntate: ¿cómo? (muy) o ¿cuánto? (mucho).</p><p class="small"><b>Palabras útiles:</b></p><div class="words">'+WORDS.map(function(x){return '<span class="'+x[0]+'">'+esc(x[1])+'</span>';}).join('')+'</div>';
  h+='<div class="row"><button class="btn cta" data-act="fgo" data-p="1">Empezar (1 min)</button></div>';
 } else if(ph===1){
  h+='<div class="ph1">Describe la foto</div><div class="clock" id="fclk">1:00</div><div class="tbar"><i id="tbar"></i></div><div class="esc" id="esc">'+ESC.map(function(x){return '<div>'+x+'</div>';}).join('')+'</div>';
  h+='<div class="row"><button class="btn" data-act="fstart" id="fbtn">Empezar el reloj</button><button class="btn cta" data-act="fgo" data-p="2">He terminado</button></div>';
 } else {
  h+='<div class="ph1">¿Qué tal ha ido?</div><ul class="check">'; FCH.forEach(function(c,i){ var k=f.id+'-'+i; h+='<li><label><input type="checkbox" data-fchk="'+k+'"'+(S.fchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
  h+='<div class="model"><b>Una descripción modelo</b><br>'+f.mm+'</div>';
  h+='<p class="small muted">En ámbar, muy (el volumen); en turquesa, mucho (la cantidad). En el examen, después sigues con las otras preguntas de la lámina: practícalas en el taller de la foto.</p>';
  h+='<div class="row"><button class="btn" data-act="fgo" data-p="0">Otra vez</button><button class="btn cta" data-act="fnext">Otra foto</button></div>';
 }
 $('fobox').innerHTML=h+'</div></div>';
 var im=$('fig').querySelector('img'); im.addEventListener('error', function(){ $('fig').classList.add('miss'); });
 if(im.complete && im.naturalWidth===0 && im.src) $('fig').classList.add('miss');
}
function fstart(){
 stopTimer(); var T0=Date.now(); var b=$('fbtn'); if(b) b.textContent='Otra vez';
 TM=setInterval(function(){
  var t=(Date.now()-T0)/1000, bar=$('tbar'), es=$('esc'), ck=$('fclk'); if(!bar){ stopTimer(); return; }
  ck.textContent=clockTxt(TDUR-t); bar.style.width=Math.min(100,t/TDUR*100)+'%';
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
 var L=['CURSO DELE A2 - R05: MUY / MUCHO; TAMBIEN / TAMPOCO','Nombre: '+(S.name||'-'),''];
 L.push('EJERCICIOS (ultimo resultado)');
 ['p1','p2','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 D.textos.forEach(function(t){
  var f=fbList(t.id,t.texto), errs=[];
  gapInfo(t.id,t.texto).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); });
  var started=Object.keys(S.cz).some(function(k){return k.indexOf(t.id+'-')===0;});
  L.push('- Textos del examen, '+t.titulo+': '+(started?f.first+'/'+f.tot+' a la primera'+(f.done<f.tot?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 L.push('','ORAL: REACCIONA (tambien / tampoco / si / no)');
 if(!S.rxlog.length) L.push('sin hacer');
 S.rxlog.forEach(function(r){ L.push('- '+r.d+': '+r.ok+'/'+r.n+' bien (autoevaluacion), '+r.t+' s para reaccionar'+(r.fails&&r.fails.length?' | fallos: '+r.fails.join(' / '):'')); });
 L.push('','ORAL: LA FOTO CON MUY Y MUCHO');
 var fd=D.fotos.filter(function(f){ return (S.fph[f.id]||0)>=2; });
 if(!fd.length) L.push('sin hacer');
 fd.forEach(function(f){ var n=0; FCH.forEach(function(c,i){ if(S.fchk[f.id+'-'+i]) n++; }); L.push('- Foto '+f.id+' ('+f.titulo+'): hecha, autorrevision '+n+'/'+FCH.length); });
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' ('+l.palabras[0]+'-'+l.palabras[1]+' palabras)','Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision: '+rv.red+' avisos rojos, '+rv.amb+' ambar | muy: '+rv.muy+', mucho: '+rv.mucho+', reacciones: '+rv.eco+' | '+rv.words+' palabras');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. Lo que mas cuesta: '+(S.o2||'-'),'3. Volumen, cantidad y eco: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 par:function(b){ S.par=+b.getAttribute('data-i'); S.pv='a'; save(); renderPar(); },
 pv:function(b){ S.pv=b.getAttribute('data-v'); save(); renderPar(); },
 eco:function(b){ S.eco=+b.getAttribute('data-i'); save(); renderEco(); },
 ea:function(b){ S.ea=+b.getAttribute('data-a'); save(); renderEco(); },
 ex:function(b){ S.ex=b.getAttribute('data-k'); save(); renderEx(); },
 etext:function(b){ S.etext=b.getAttribute('data-id'); save(); renderE2(); },
 qa:function(b){ var k=b.getAttribute('data-k'); qzAnswer(k, +b.getAttribute('data-o')); qzRender(k, $('exbox')); nav(); var f=$('exbox').querySelector('.fb'); if(f&&f.scrollIntoView) f.scrollIntoView({block:'nearest'}); },
 qnext:function(b){ var k=b.getAttribute('data-k'); S.qz[k].i++; save(); qzRender(k, $('exbox')); },
 qrep:function(b){ var k=b.getAttribute('data-k'); qzNew(k); qzRender(k, $('exbox')); },
 czreset:function(b){ b.getAttribute('data-ids').split(',').forEach(function(id){ Object.keys(S.cz).forEach(function(g){ if(g.indexOf(id+'-')===0) delete S.cz[g]; }); }); save(); renderEx(); nav(); },
 at:function(b){ S.at=b.getAttribute('data-k'); save(); renderAt(); },
 lam:function(b){ S.lam=b.getAttribute('data-id'); save(); renderLam(); },
 review:function(){ review(); nav(); },
 rxn:function(b){ S.rxc.n=+b.getAttribute('data-n'); save(); renderRx(); },
 rxt:function(b){ S.rxc.t=+b.getAttribute('data-t'); save(); renderRx(); },
 rxstart:function(){ rxNew(); rxRun(); },
 rxgo:function(){ rxRun(); },
 rxskip:function(){ rxNext(); },
 rxeval:function(b){
  var R=S.rx, c=R.deck[R.i]; R.res.push({k:c.k, a:c.a, ok:b.getAttribute('data-ok')==='1'}); R.i++; R.ph=1; save();
  if(R.i>=R.deck.length){
   var ok=R.res.filter(function(r){return r.ok;}).length, d=new Date();
   S.rxlog.push({d:d.getDate()+'/'+(d.getMonth()+1), n:R.deck.length, t:S.rxc.t, ok:ok, fails:R.res.filter(function(r){return !r.ok;}).map(function(r){ return D.oral[r.k].f; })});
   if(S.rxlog.length>6) S.rxlog=S.rxlog.slice(-6);
   save(); renderRx(); nav();
  } else rxRun();
 },
 rxagain:function(){ stopTimer(); S.rx=null; save(); renderRx(); },
 foto:function(b){ stopTimer(); S.foto=+b.getAttribute('data-id'); save(); renderFoto(); },
 fgo:function(b){ stopTimer(); var p=+b.getAttribute('data-p'), f=S.foto; S.fph[f]=p; save(); renderFoto(); nav(); if(p===1) fstart(); },
 fstart:function(){ fstart(); },
 fnext:function(){ stopTimer(); var ids=D.fotos.map(function(f){return f.id;}), free=ids.filter(function(i){ return (S.fph[i]||0)<2 && i!==S.foto; }); if(!free.length) free=ids.filter(function(i){return i!==S.foto;}); S.foto=free[Math.floor(Math.random()*free.length)]; save(); renderFoto(); },
 printres:function(){ var v=$('v-resumen'); v.classList.add('printme'); window.print(); setTimeout(function(){ v.classList.remove('printme'); },500); },
 copy:function(){
  var t=pack(), box=$('cbox');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar automáticamente. Escribe tus respuestas en un correo para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
 }
};
window.__R05pack = pack;
function renderAt(){
 var ps=$('atsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.at);
 $('atw').hidden = S.at!=='w'; $('atr').hidden = S.at!=='r'; $('ato').hidden = S.at!=='o'; stopTimer();
 if(S.rx && S.rx.ph<3) S.rx.ph=1;
 if(S.at==='w') renderLam(); else if(S.at==='r') renderRx(); else renderFoto();
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
if(S.fph){ Object.keys(S.fph).forEach(function(k){ if(S.fph[k]===1) S.fph[k]=0; }); }

renderPar(); renderEco(); renderEx(); renderAt(); renderOpn(); go(S.cur);
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
      "| items:", len(B.P_MM) + len(B.P_ECO) + len(B.E_BIENMAL),
      "| pruebas del detector:", len(B.DETECTOR_PRUEBAS), "(navegador: %s)" % ("igual que Python" if NODE_OK else "sin probar"),
      "| buena en el desplegable (1a/2a/3a):", POS_TXT, "| parejas:", len(B.PAREJAS), "| frases orales:", len(B.ORAL), "| fotos:", len(B.FOTOS))
