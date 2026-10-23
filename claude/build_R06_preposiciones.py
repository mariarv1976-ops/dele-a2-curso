# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R06 DEL CURSO DE PREPARACION DELE A2: PREPOSICIONES FRECUENTES
# Uso: python3 build_R06_preposiciones.py  -> DELEA2_curso_R06_preposiciones.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# Contenidos: solo en banco_R06_preposiciones.py. Este archivo monta la pagina y comprueba el banco.
# Mismo formato y motor que R01, R02, R04 y R05: pestanas, correccion inmediata, huecos con motivo (barajado
# arreglado), "Ahora tu" con escritura (detector de errores tipicos) y oral (quedamos, con reloj; y como se
# llega, con un plano dibujado en SVG, sin fotos), Tu opinion y Copiar.
# Enfoque cognitivo: EL MAPA DEL VIAJE. A = la flecha; EN = la caja; DE...A / DESDE...HASTA = la linea;
# POR = la zona y lo que esta detras; PARA = la diana, la meta delante. Espanol de Espana. Ejemplos propios.
import json, os, re, shutil, subprocess, sys, tempfile, unicodedata
from curso_comun import CSS, EMAIL, page
import banco_R06_preposiciones as B

TITLE = "Preposiciones frecuentes"
FILE = "DELEA2_curso_R06_preposiciones.html"
STORAGE = "dele-a2-curso-R06"

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
MARK = re.compile(r"\[(a|e|l|p|m):([^\[\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
KIND_FAM = {"a": "flecha", "e": "caja", "l": "linea", "p": "por", "m": "para"}
FAM_KIND = {v: k for k, v in KIND_FAM.items()}

def chk_marks(s, where, need=0):
    rest = MARK.sub("", s)
    if "[" in rest or "]" in rest: err("marca mal cerrada en %s: %s" % (where, s[:70]))
    gs = MARK.findall(s)
    for k, b in gs:
        lb = b.lower()
        if k == "a" and not re.search(r"(^|\s)(a|al)\s", lb): err("%s: [a:] sin a / al: %s" % (where, b))
        if k == "e" and not re.match(r"en\s", lb): err("%s: [e:] tiene que empezar por «en»: %s" % (where, b))
        if k == "l" and not re.match(r"(de|del|desde|hasta)\s", lb): err("%s: [l:] tiene que empezar por de / del / desde / hasta: %s" % (where, b))
        if k == "p" and not re.match(r"por\s", lb): err("%s: [p:] tiene que empezar por «por»: %s" % (where, b))
        if k == "m" and not re.match(r"para\s", lb): err("%s: [m:] tiene que empezar por «para»: %s" % (where, b))
    if len(gs) < need: err("%s: hacen falta al menos %d marcas" % (where, need))
    return gs

def plain(s): return re.sub(r"<[^>]+>", "", MARK.sub(lambda m: m.group(2), s))
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()

for k, (f, w, ok) in B.MOTIVOS.items():
    if f not in B.FAMILIAS or not w or not ok: err("motivo mal definido: " + k)

# 1. El mapa
DKINDS = {"a", "en", "l", "p", "m", "pie"}
DK_MARK = {"a": "a", "en": "e", "l": "l", "p": "p", "m": "m", "pie": "a"}
for i, p in enumerate(B.PAREJAS):
    for s, k, lab, ex in (("a", "ka", "la", "ea"), ("b", "kb", "lb", "eb")):
        gs = chk_marks(p[s], "pareja %d %s" % (i, s), 1)
        if p[k] not in DKINDS: err("pareja %d: dibujo desconocido %s" % (i, p[k])); continue
        if any(g[0] != DK_MARK[p[k]] for g in gs): err("pareja %d %s: la marca no va con el dibujo %s" % (i, s, p[k]))
        if p[k] == "l" and "|" not in p[lab]: err("pareja %d: el dibujo de la linea necesita «principio|final»" % i)
        if not p.get(ex): err("pareja %d %s sin explicacion" % (i, s))
    if p["ka"] == p["kb"]: err("pareja %d: las dos frases con el mismo dibujo" % i)
used_k = {p["ka"] for p in B.PAREJAS} | {p["kb"] for p in B.PAREJAS}
if used_k != DKINDS: err("las parejas tienen que mostrar los seis dibujos: faltan %s" % (DKINDS - used_k))
for t, cl, items in B.VERBOS:
    for it in items:
        gs = chk_marks(it, "verbos " + t, 0 if cl == "con" else 1)
        if cl != "con" and any(KIND_FAM[g[0]] != cl for g in gs): err("verbos %s: la marca no es de %s: %s" % (t, cl, it))
        if cl == "con" and " con " not in " " + it + " ": err("verbos con: el ejemplo no lleva con: " + it)
for t, bien, mal, why in B.CIERRES:
    chk_marks(bien, "cierres " + t)
    if not why or not mal: err("cierre sin explicacion o sin error: " + t)
for k in ("donde", "hora", "como", "destino"):
    if not B.PLAN.get(k) or not B.PLAN_WHY.get(k): err("plan: falta " + k)
    for it in B.PLAN[k]:
        gs = chk_marks(it, "plan " + k)
        if not gs and it != "andando": err("plan %s: sin marca: %s" % (k, it))
for it in B.PLAN["donde"]:
    if not it.startswith("[e:"): err("plan donde: con en: " + it)
for it in B.PLAN["hora"] + B.PLAN["destino"]:
    if not it.startswith("[a:"): err("plan hora / destino: con a: " + it)

# 2. El reloj
RFAM = set(B.FAMILIAS) | {"nada"}
for t, cl, items, why in B.RELOJ:
    if cl not in RFAM: err("reloj: familia desconocida en " + t)
    for it in items:
        gs = chk_marks(it, "reloj " + t)
        if cl == "nada" and gs: err("reloj %s: sin preposicion, sin marcas: %s" % (t, it))
        if cl != "nada" and (not gs or any(KIND_FAM[g[0]] != cl for g in gs)): err("reloj %s: la marca no es de %s: %s" % (t, cl, it))
    if not why: err("reloj sin explicacion: " + t)
if {r[1] for r in B.RELOJ} != RFAM: err("el reloj tiene que mostrar todas las familias y los dias sin nada")

# 3. Por y para
for i, f in enumerate(B.POR_PARA):
    gs = chk_marks(f["f"], "por/para %d" % i, 1)
    if f["k"] not in ("p", "m") or any(g[0] != f["k"] for g in gs): err("por/para %d: la marca no va con k" % i)
    if not f.get("why") or not f.get("uso"): err("por/para %d sin explicacion" % i)
if {f["k"] for f in B.POR_PARA} != {"p", "m"}: err("por/para: hacen falta de los dos")

# 4. En el examen
for c, d, s in B.DONDE: chk_marks(s, "donde " + c, 1)
for mal, bien, why in B.ERRORES:
    chk_marks(bien, "errores", 1)
    if plain(bien) == mal or not why: err("error tipico sin correccion o sin porque: " + mal)
for k in B.REQ:
    if not any(k in m.lower() for m, _, _ in B.ERRORES): err("falta el error tipico: " + k)

# Ejercicios
PREPS = {"a", "en", "de", "por", "para", "con", "hasta", "desde"}
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
            if any(x.lower() not in PREPS for x in o): err("%s: las opciones tienen que ser preposiciones: %s" % (name, it["q"][:40]))
chk_quiz(B.P_PREP, "P_PREP", 12)
chk_quiz(B.P_PP, "P_PP", 10)
for it in B.P_PP:
    if it["o"][0].lower() not in ("por", "para") or not {"por", "para"} <= {x.lower() for x in it["o"]}: err("P_PP: por y para tienen que estar y la buena es una de las dos: " + it["q"])
if {it["o"][0].lower() for it in B.P_PP} != {"por", "para"}: err("P_PP: hacen falta de por y de para")
if not {"a", "en", "de", "por", "hasta"} <= {it["o"][0].lower() for it in B.P_PREP}: err("P_PREP: faltan buenas de a / en / de / por / hasta")
chk_quiz(B.E_BIENMAL, "E_BIENMAL", 12, bm=True)
if not any(i["ok"] == 0 for i in B.E_BIENMAL): err("bien/mal: faltan frases bien")
for k in B.REQ:
    if not any(k in i["q"].lower() and i["ok"] == 1 for i in B.E_BIENMAL): err("bien/mal: falta el error tipico " + k)

# Textos con huecos
def chk_gaps(s, where):
    n = 0
    for g in GAP.findall(s):
        n += 1
        if "#" not in g: err("hueco sin motivo en %s: %s" % (where, g)); continue
        ops, mot = g.split("#"); ops = ops.split("|")
        if len(ops) != 3 or len(set(o.lower() for o in ops)) != 3: err("hueco sin 3 opciones distintas en %s: %s" % (where, g))
        if any(o.lower() not in PREPS for o in ops): err("hueco con opciones que no son preposiciones en %s: %s" % (where, g))
        if mot not in B.MOTIVOS: err("motivo desconocido en %s: %s" % (where, mot)); continue
        if ops[0].lower() not in B.MOTIVOS[mot][2]: err("en %s la buena (%s) no es la de su motivo %s" % (where, ops[0], mot))
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
if {f for L in B.LAMINAS for _, fs in L["pautas"] for f in fs} != set(B.FOCOS): err("las laminas tienen que trabajar las cinco piezas")

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
    for k in B.REQ:
        if not any(k in t.lower() and e for t, e in B.DETECTOR_PRUEBAS): err("detector: ninguna prueba con el error tipico " + k)
    for mal, _, _ in B.ERRORES:
        if not det(mal): err("detector: no ve el error tipico «%s»" % mal)
    for it in B.E_BIENMAL:
        if it["ok"] == 1 and not det(it["q"]): err("detector: no ve la frase mala «%s»" % it["q"])
    # Nada de lo que la ficha da por bueno puede dar un aviso rojo (frase a frase, como en la pagina).
    buenos = []
    buenos += [p["a"] for p in B.PAREJAS] + [p["b"] for p in B.PAREJAS]
    buenos += [x for _, _, items in B.VERBOS for x in items] + [b for _, b, _, _ in B.CIERRES]
    buenos += ["Quedamos %s %s y vamos %s %s." % (d, h, c, x) for d in B.PLAN["donde"] for h in B.PLAN["hora"] for c in B.PLAN["como"] for x in B.PLAN["destino"]]
    buenos += [x for _, _, items, _ in B.RELOJ for x in items] + [f["f"] for f in B.POR_PARA]
    buenos += [s for _, _, s in B.DONDE] + [b for _, b, _ in B.ERRORES]
    buenos += [filled(t["texto"]) for t in B.TEXTOS] + [o["m"] for o in B.ORAL] + [r["m"] for r in B.RUTAS]
    buenos += [i["q"] for i in B.E_BIENMAL if i["ok"] == 0]
    buenos += [i["q"].replace("____", i["o"][0]) for i in B.P_PREP + B.P_PP]
    buenos += [L["mensaje"] for L in B.LAMINAS]
    for b in buenos:
        for s in re.findall(r"[^.!?\n]+[.!?]*", plain(b)):
            r = det(s, only_red=True)
            if r: err("detector: aviso rojo %s en un texto bueno: %r" % (r, s.strip()))

# Oral
for i, o in enumerate(B.ORAL):
    chk_marks(o["m"], "oral %d" % i, 1)
    if not o.get("q") or not o.get("pista"): err("oral %d: falta la pregunta o la pista" % i)
if len(B.ORAL) < 16: err("oral: al menos 16 tarjetas")
if {g[0] for o in B.ORAL for g in MARK.findall(o["m"])} != set(KIND_FAM): err("oral: las tarjetas tienen que trabajar las cinco piezas")
lids = {l[0] for l in B.LUGARES}
for r in B.RUTAS:
    chk_marks(r["m"], "ruta " + r["id"], 3)
    if r["id"] not in lids: err("ruta %s: no hay lugar con ese id en el plano" % r["id"])
    if len(r["pts"]) < 2: err("ruta %s: hacen falta puntos" % r["id"])
    for x, y in r["pts"]:
        if not (0 <= x <= 640 and 0 <= y <= 420): err("ruta %s: punto fuera del plano" % r["id"])
    if r["modo"] not in ("a pie", "en autobús"): err("ruta %s: modo desconocido" % r["id"])
if {r["modo"] for r in B.RUTAS} != {"a pie", "en autobús"}: err("rutas: una a pie y otra en autobus como minimo")

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
def mk(s): return MARK.sub(lambda m: '<span class="k %s">%s</span>' % (m.group(1), m.group(2)), s)

INK = "#14161C"; MUT = "#5E5A55"; LINE = "#E6DFD6"
COL = {"a": ("#1D5FA8", "#E2ECF8"), "e": ("#17707F", "#DDF0F2"), "l": ("#B7791F", "#FBF0DA"),
       "p": ("#6B3FA0", "#EFE7F8"), "m": ("#C2492A", "#FCE9E1")}
FAMCOL = {KIND_FAM[k]: v for k, v in COL.items()}

def svg(vb, aria, inner, cls="dg"): return '<svg class="%s" viewBox="%s" role="img" aria-label="%s">%s</svg>' % (cls, vb, aria, inner)
def txt(x, y, s, size=16, col=INK, w="400", anchor="middle", extra=""):
    return '<text x="%s" y="%s" text-anchor="%s" font-size="%s" font-weight="%s" fill="%s"%s>%s</text>' % (x, y, anchor, size, w, col, extra, s)
def person(x, y, s=1.0, col=INK):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="%s" stroke-width="2.5"/>'
            '<path d="M%.1f,%.1f q%.1f,%.1f %.1f,0" fill="#fff" stroke="%s" stroke-width="2.5"/>') % (
        x, y, 12 * s, col, x - 20 * s, y + 42 * s, 20 * s, -30 * s, 40 * s, col)
def arrowhead(x, y, col, d="r", s=1.0):
    if d == "r": pts = (x, y, x - 14 * s, y - 8 * s, x - 14 * s, y + 8 * s)
    elif d == "l": pts = (x, y, x + 14 * s, y - 8 * s, x + 14 * s, y + 8 * s)
    else: pts = (x, y, x - 8 * s, y - 14 * s, x + 8 * s, y - 14 * s)
    return '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>' % (pts + (col,))
def flag(x, y, col, soft):
    return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>'
            '<path d="M%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="2"/>') % (x, y, x, y - 70, INK, x, y - 70, x + 44, y - 56, x, y - 42, soft, col)
def target(x, y, col, r=40):
    return ('<circle cx="%d" cy="%d" r="%d" fill="#fff" stroke="%s" stroke-width="3"/><circle cx="%d" cy="%d" r="%d" fill="#fff" stroke="%s" stroke-width="3"/>'
            '<circle cx="%d" cy="%d" r="%d" fill="%s"/>') % (x, y, r, col, x, y, int(r * .6), col, x, y, int(r * .25), col)

def diag(kind, lab):
    """Dibujo de una pieza del viaje (640 x 200)."""
    if kind == "a":
        c, s = COL["a"]
        o = person(90, 70) + '<line x1="130" y1="100" x2="470" y2="100" stroke="%s" stroke-width="5"/>' % c + arrowhead(486, 100, c, s=1.3)
        o += flag(520, 150, c, s) + txt(300, 84, "A", 30, c, "700", extra=' font-family="Georgia,serif"')
        o += txt(540, 180, lab, 18, INK, "700") + txt(300, 132, "la flecha llega a un punto", 15, MUT)
        return svg("0 0 640 200", "A: una flecha que llega a " + lab, o)
    if kind == "en":
        c, s = COL["e"]
        o = '<rect x="190" y="26" width="260" height="150" rx="18" fill="%s" stroke="%s" stroke-width="4"/>' % (s, c)
        o += txt(320, 56, lab, 20, INK, "700") + person(320, 92)
        o += txt(560, 100, "EN", 30, c, "700", extra=' font-family="Georgia,serif"') + txt(560, 126, "dentro", 15, MUT)
        o += txt(90, 100, "no hay", 15, MUT) + txt(90, 120, "movimiento", 15, MUT)
        return svg("0 0 640 200", "EN: una caja; estás dentro de " + lab, o)
    if kind == "l":
        c, s = COL["l"]; a, b = lab.split("|")
        o = '<line x1="120" y1="100" x2="520" y2="100" stroke="%s" stroke-width="8" stroke-linecap="round"/>' % c
        o += '<circle cx="120" cy="100" r="13" fill="#fff" stroke="%s" stroke-width="4"/><circle cx="520" cy="100" r="13" fill="%s" stroke="%s" stroke-width="4"/>' % (c, c, c)
        o += txt(120, 66, "DE", 22, c, "700") + txt(520, 66, "A", 22, c, "700")
        o += txt(120, 142, a, 18, INK, "700") + txt(520, 142, b, 18, INK, "700")
        o += txt(320, 178, "principio y final: van en pareja", 15, MUT)
        return svg("0 0 640 200", "DE... A: una línea de %s a %s" % (a, b), o)
    if kind == "p":
        c, s = COL["p"]
        o = '<rect x="170" y="30" width="300" height="140" rx="40" fill="%s" stroke="%s" stroke-width="3" stroke-dasharray="8 6"/>' % (s, c)
        o += txt(320, 160, lab, 18, INK, "700")
        o += '<path d="M60,150 C150,150 200,60 300,90 S420,140 540,60" fill="none" stroke="%s" stroke-width="4" stroke-dasharray="2 9" stroke-linecap="round"/>' % INK
        o += arrowhead(556, 52, INK, s=1.0) + txt(320, 62, "POR", 28, c, "700", extra=' font-family="Georgia,serif"')
        o += txt(320, 190, "pasas por una zona (o es lo que está detrás)", 14, MUT)
        return svg("0 0 640 200", "POR: una zona por donde pasas: " + lab, o)
    if kind == "m":
        c, s = COL["m"]
        o = person(90, 70) + '<line x1="130" y1="100" x2="440" y2="100" stroke="%s" stroke-width="4" stroke-dasharray="10 6"/>' % c + arrowhead(456, 100, c, s=1.2)
        o += target(510, 100, c) + txt(510, 172, lab, 18, INK, "700")
        o += txt(290, 84, "PARA", 28, c, "700", extra=' font-family="Georgia,serif"') + txt(290, 132, "la meta, delante", 15, MUT)
        return svg("0 0 640 200", "PARA: la meta es " + lab, o)
    # pie: andando, sin caja
    c, s = COL["a"]
    o = '<circle cx="150" cy="58" r="13" fill="#fff" stroke="%s" stroke-width="2.5"/>' % INK
    o += '<path d="M150,72 L150,118 M150,84 L128,104 M150,84 L172,100 M150,118 L132,152 M150,118 L170,150" stroke="%s" stroke-width="3" fill="none" stroke-linecap="round"/>' % INK
    for i, x in enumerate(range(210, 470, 44)):
        o += '<ellipse cx="%d" cy="%d" rx="9" ry="5" fill="%s"/>' % (x, 146 if i % 2 else 132, c)
    o += '<rect x="500" y="70" width="90" height="70" rx="12" fill="#fff" stroke="%s" stroke-width="3" stroke-dasharray="6 5"/>' % MUT
    o += '<line x1="500" y1="70" x2="590" y2="140" stroke="#B3261E" stroke-width="4"/><line x1="590" y1="70" x2="500" y2="140" stroke="#B3261E" stroke-width="4"/>'
    o += txt(545, 166, "sin caja", 15, MUT) + txt(330, 76, "A PIE", 26, c, "700", extra=' font-family="Georgia,serif"') + txt(330, 102, "o andando", 15, MUT)
    return svg("0 0 640 200", "A pie: andando, sin vehículo; no estás dentro de nada", o)

def icon(k):
    c, s = COL[k]
    o = '<svg class="ic" viewBox="0 0 300 120" aria-hidden="true">'
    if k == "a": o += '<circle cx="40" cy="60" r="10" fill="%s"/><line x1="54" y1="60" x2="220" y2="60" stroke="%s" stroke-width="5"/>' % (INK, c) + arrowhead(236, 60, c, s=1.3) + flag(255, 100, c, s)
    elif k == "e": o += '<rect x="70" y="14" width="160" height="92" rx="16" fill="%s" stroke="%s" stroke-width="4"/><circle cx="150" cy="60" r="12" fill="%s"/>' % (s, c, INK)
    elif k == "l": o += '<line x1="50" y1="60" x2="250" y2="60" stroke="%s" stroke-width="8" stroke-linecap="round"/><circle cx="50" cy="60" r="12" fill="#fff" stroke="%s" stroke-width="4"/><circle cx="250" cy="60" r="12" fill="%s"/>' % (c, c, c)
    elif k == "p": o += '<rect x="70" y="14" width="160" height="92" rx="30" fill="%s" stroke="%s" stroke-width="3" stroke-dasharray="7 5"/><path d="M20,96 C90,96 120,30 170,50 S240,80 280,24" fill="none" stroke="%s" stroke-width="4" stroke-dasharray="2 8" stroke-linecap="round"/>' % (s, c, INK)
    else: o += '<circle cx="40" cy="60" r="10" fill="%s"/><line x1="54" y1="60" x2="180" y2="60" stroke="%s" stroke-width="4" stroke-dasharray="9 6"/>' % (INK, c) + arrowhead(196, 60, c) + target(240, 60, c, 36)
    return o + '</svg>'

CARDS = [("a", "A", "La flecha", "Llegas a un punto: un sitio, una hora, una persona.", "voy [a:a Madrid] · [a:a las cinco] · veo [a:a mi madre]"),
         ("e", "EN", "La caja", "Estás dentro: de un sitio, de un vehículo, de un mes o un año.", "estoy [e:en casa] · [e:en tren] · [e:en mayo]"),
         ("l", "DE... A", "La línea", "Principio y final. Los extremos van en pareja.", "[l:de 9 a 2] · [l:desde las 9 hasta las 2] · soy [l:de Perú]"),
         ("p", "POR", "La zona y lo que está detrás", "Pasas por un sitio o una parte del día. O es la causa.", "[p:por el parque] · [p:por la mañana] · gracias [p:por todo]"),
         ("m", "PARA", "La diana", "La meta que tienes delante: una persona, un objetivo, un día límite.", "[m:para ti] · [m:para aprender] · [m:para el lunes]")]
def cards():
    o = '<div class="cams">'
    for k, w, h, p, ej in CARDS:
        o += '<div class="cam c%s"><div class="k0">%s</div><h3>%s</h3>%s<p>%s</p><div class="ej">%s</div></div>' % (k, w, h, icon(k), p, mk(ej))
    return o + '</div>'

def frase_viaje():
    a, e, l, p, m = (COL[k][0] for k in "aelpm")
    o = '<div class="viaje">'
    for t, k in (("Salgo", None), ("[l:de casa]", "l"), ("[a:a las ocho]", "a"), ("y voy", None), ("[e:en bici]", "e"), ("[p:por el parque]", "p"), ("[a:al trabajo]", "a"), ("con Marta,", None), ("[m:para llegar pronto]", "m")):
        o += '<span class="vt%s">%s</span>' % (" " + k if k else "", mk(t))
    return o + '</div>'

def verbos():
    o = '<div class="lado">'
    for t, cl, items in B.VERBOS:
        o += '<div class="%s"><h4>%s</h4><ul>%s</ul></div>' % (cl, t, "".join("<li>%s</li>" % mk(x) for x in items))
    return o + '</div>'

def cierres():
    o = '<div class="cier">'
    for t, bien, mal, why in B.CIERRES:
        o += '<div class="box"><h4>%s</h4><p class="ex"><span class="okm" aria-hidden="true">✓</span> %s &nbsp; <span class="badm"><span aria-hidden="true">✗</span> <s>%s</s></span></p><p class="small muted" style="margin:0">%s</p></div>' % (t, mk(bien), mal, why)
    return o + '</div>'

def reloj_svg():
    X0, PX = 40, 35  # 7:00 en x=40, 35 px por hora
    def hx(h): return X0 + (h - 7) * PX
    c_p, s_p = COL["p"]; c_a, _ = COL["a"]; c_l, s_l = COL["l"]
    o = ""
    for h0, h1, lab in ((7, 14, "por la mañana"), (14, 20, "por la tarde"), (20, 23, "por la noche")):
        o += '<rect x="%d" y="40" width="%d" height="64" rx="10" fill="%s" stroke="%s" stroke-width="2" stroke-dasharray="6 5"/>' % (hx(h0) + 2, (h1 - h0) * PX - 4, s_p, c_p)
        o += txt((hx(h0) + hx(h1)) / 2, 30, lab, 14, c_p, "700")
    o += '<line x1="%d" y1="120" x2="%d" y2="120" stroke="%s" stroke-width="3"/>' % (hx(7), hx(23), INK)
    for h in range(7, 24, 2):
        o += '<line x1="%d" y1="114" x2="%d" y2="126" stroke="%s" stroke-width="2"/>' % (hx(h), hx(h), INK) + txt(hx(h), 142, "%d:00" % h, 12, MUT)
    o += '<circle cx="%d" cy="120" r="8" fill="%s"/>' % (hx(8), c_a) + '<line x1="%d" y1="62" x2="%d" y2="106" stroke="%s" stroke-width="4"/>' % (hx(8), hx(8), c_a) + arrowhead(hx(8), 112, c_a, "d")
    o += '<rect x="%d" y="54" width="70" height="24" rx="6" fill="#fff" stroke="%s" stroke-width="2"/>' % (hx(8) - 10, c_a) + txt(hx(8) + 25, 71, "a las 8", 14, c_a, "700")
    o += '<line x1="%d" y1="166" x2="%d" y2="166" stroke="%s" stroke-width="10" stroke-linecap="round"/>' % (hx(9), hx(14), c_l)
    o += '<circle cx="%d" cy="166" r="8" fill="#fff" stroke="%s" stroke-width="3"/><circle cx="%d" cy="166" r="8" fill="%s"/>' % (hx(9), c_l, hx(14), c_l)
    o += txt((hx(9) + hx(14)) / 2, 196, "de 9 a 2 · desde las 9 hasta las 2", 14, c_l, "700")
    o += '<line x1="%d" y1="166" x2="%d" y2="166" stroke="%s" stroke-width="10" stroke-linecap="round"/>' % (hx(17), hx(21), c_l)
    o += txt((hx(17) + hx(21)) / 2, 196, "de 5 a 9", 14, c_l, "700")
    return svg("0 0 640 210", "Un día: por la mañana, por la tarde y por la noche son zonas; a las 8 es un punto; de 9 a 2 es una línea.", o)

def reloj():
    o = '<div class="lado reloj">'
    cls = {"flecha": "flecha", "caja": "caja", "linea": "linea", "por": "por", "para": "para", "nada": "nada"}
    for t, cl, items, why in B.RELOJ:
        o += '<div class="%s"><h4>%s</h4><p class="small" style="margin:0 0 6px">%s</p><p style="margin:0">%s</p></div>' % (cls[cl], t, " · ".join(mk(x) for x in items), why)
    return o + '</div>'

def porpara_svg(hl=None):
    c_p, s_p = COL["p"]; c_m, s_m = COL["m"]
    op_p = "1" if hl in (None, "p") else ".25"; op_m = "1" if hl in (None, "m") else ".25"
    o = person(320, 70, 1.2)
    o += txt(320, 30, "TÚ, AHORA", 13, MUT, "700")
    o += '<g opacity="%s"><path d="M40,150 C120,150 160,100 270,110" fill="none" stroke="%s" stroke-width="4" stroke-dasharray="2 9" stroke-linecap="round"/>' % (op_p, INK)
    o += '<line x1="270" y1="140" x2="120" y2="140" stroke="%s" stroke-width="4"/>' % c_p + arrowhead(104, 140, c_p, "l")
    o += txt(150, 72, "POR", 30, c_p, "700", extra=' font-family="Georgia,serif"') + txt(150, 96, "mira hacia atrás", 14, MUT)
    o += txt(150, 176, "el camino · la zona · la causa", 14, c_p, "700") + '</g>'
    o += '<g opacity="%s"><line x1="370" y1="140" x2="530" y2="140" stroke="%s" stroke-width="4" stroke-dasharray="10 6"/>' % (op_m, c_m) + arrowhead(546, 140, c_m)
    o += target(588, 124, c_m, 34)
    o += txt(450, 72, "PARA", 30, c_m, "700", extra=' font-family="Georgia,serif"') + txt(450, 96, "mira hacia delante", 14, MUT)
    o += txt(520, 186, "la persona · el objetivo · el día límite", 14, c_m, "700", "end") + '</g>'
    return svg("0 0 640 200", "Por mira hacia atrás: el camino, la zona y la causa. Para mira hacia delante: la meta.", o, "dg cu")

def donde():
    return "".join('<div class="box"><span class="chip">%s</span><p class="small muted" style="margin:6px 0">%s</p><p style="margin:0">%s</p></div>' % (c, d, mk(s)) for c, d, s in B.DONDE)

def errores():
    o = '<div class="errs">'
    for mal, bien, why in B.ERRORES:
        o += '<div class="err"><div class="mal"><span aria-hidden="true">✗</span> <s>%s</s></div><div class="bien"><span aria-hidden="true">✓</span> %s</div><div class="small muted">%s</div></div>' % (mal, mk(bien), why)
    return o + '</div>'

def plano(route=None):
    o = '<rect x="0" y="0" width="640" height="420" rx="14" fill="#F4EFE6"/>'
    for lab, x1, y1, x2, y2 in B.CALLES:
        o += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#FFFFFF" stroke-width="26" stroke-linecap="round"/>' % (x1, y1, x2, y2)
        o += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#D9D0C3" stroke-width="2" stroke-dasharray="10 8"/>' % (x1, y1, x2, y2)
    for lid, lab, x, y, w, h, tp in B.LUGARES:
        if tp == "parque":
            o += '<rect x="%d" y="%d" width="%d" height="%d" rx="18" fill="#D8ECCF" stroke="#5E8F4E" stroke-width="2"/>' % (x, y, w, h)
            for tx, ty in ((x + 40, y + 40), (x + 150, y + 50), (x + 80, y + 100), (x + 170, y + 110)):
                o += '<circle cx="%d" cy="%d" r="12" fill="#9CC98A"/>' % (tx, ty)
            o += txt(x + w / 2, y + h / 2 + 6, lab, 17, "#2F5A22", "700")
        else:
            fill = "#FFFFFF" if tp == "edif" else "#FCE9E1"
            o += '<rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, w, h, fill, INK)
            o += txt(x + w / 2, y + h / 2 + 6, lab, 15, INK, "700")
    pn, px, py = B.PLAZA
    o += '<circle cx="%d" cy="%d" r="22" fill="#FBF0DA" stroke="%s" stroke-width="2"/>' % (px, py, COL["l"][0]) + txt(px - 34, py - 30, pn, 13, INK, "700", "end")
    for lab, x1, y1, x2, y2, lx, ly in B.CALLES_ROT:
        if y1 == y2: o += txt(lx, ly + 4, lab, 12, MUT, "700", "start")
        else: o += txt(lx + 4, ly, lab, 12, MUT, "700", "start", ' transform="rotate(-90 %d %d)"' % (lx + 4, ly))
    for x, y in B.PARADAS:
        o += '<circle cx="%d" cy="%d" r="11" fill="%s"/>' % (x, y, COL["a"][0]) + txt(x, y + 5, "P", 13, "#fff", "700")
    aria = "Plano del barrio: estación, parque, plaza Mayor, biblioteca, mercado, cine y casa de Lucía."
    if route:
        pts = " ".join("%d,%d" % p for p in route["pts"])
        o += '<polyline points="%s" fill="none" stroke="%s" stroke-width="6" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="1 12"/>' % (pts, COL["m"][0])
        sx, sy = route["pts"][0]; ex, ey = route["pts"][-1]
        o += '<circle cx="%d" cy="%d" r="9" fill="%s"/>' % (sx, sy, INK)
        o += '<rect x="%d" y="%d" width="84" height="22" rx="6" fill="%s"/>' % (sx - 92, sy - 74, INK) + txt(sx - 50, sy - 58, "Estás aquí", 12, "#fff", "700")
        o += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (sx - 50, sy - 52, sx - 6, sy - 6, INK)
        o += target(ex, ey, COL["m"][0], 14)
        aria = "Plano con el camino desde la estación: " + route["titulo"] + ", " + route["modo"] + "."
    return svg("0 0 640 420", aria, o, "dg plano")

LEG = ('<div class="legend"><span><span class="k a">a</span> la flecha</span><span><span class="k e">en</span> la caja</span>'
       '<span><span class="k l">de... a</span> la línea</span><span><span class="k p">por</span> zona y causa</span><span><span class="k m">para</span> la meta</span></div>')

CSS_R = CSS + r"""
:root{--pa:#1D5FA8;--pa-soft:#E2ECF8;--pe:#17707F;--pe-soft:#DDF0F2;--pl:#B7791F;--pl-soft:#FBF0DA;--pp:#6B3FA0;--pp-soft:#EFE7F8;--pm:#C2492A;--pm-soft:#FCE9E1}
.k{border-radius:4px;padding:0 3px 1px;border-bottom:3px solid;line-height:1.9}
.k.a{background:var(--pa-soft);border-color:var(--pa)}.k.e{background:var(--pe-soft);border-color:var(--pe)}
.k.l{background:var(--pl-soft);border-color:var(--pl)}.k.p{background:var(--pp-soft);border-color:var(--pp)}.k.m{background:var(--pm-soft);border-color:var(--pm)}
.cams{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;border-top:6px solid var(--pa)}
.cam.ce{border-top-color:var(--pe)}.cam.cl{border-top-color:var(--pl)}.cam.cp{border-top-color:var(--pp)}.cam.cm{border-top-color:var(--pm)}
.cam .k0{font-family:Georgia,serif;font-size:1.3rem;font-weight:700}
.cam.ca .k0{color:var(--pa)}.cam.ce .k0{color:var(--pe)}.cam.cl .k0{color:#8A5A12}.cam.cp .k0{color:var(--pp)}.cam.cm .k0{color:var(--pm)}
.cam h3{margin:0 0 6px}.cam p{margin:0;font-size:.95rem}
.cam .ej{margin-top:8px;font-size:.92rem;background:var(--paper);border-radius:8px;padding:6px 10px}
.cam svg.ic{width:100%;max-width:240px;height:auto;display:block;margin:6px auto 10px}
.viaje{display:flex;flex-wrap:wrap;gap:6px 8px;align-items:center;font-size:1.08rem;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:12px 0}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.box h4{margin:0 0 4px}.box .ex{margin:4px 0 6px}
.okm{color:var(--ok);font-weight:700}.badm{color:var(--bad)}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pill.ok{border-color:var(--ok)}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.duo button{font:inherit;text-align:left;border:2px solid var(--line);background:#fff;border-radius:10px;padding:10px 12px;cursor:pointer;line-height:1.6}
.duo button.on{border-color:var(--ink);background:var(--paper)}
.duo button small{display:block;font-size:.75rem;font-weight:700;letter-spacing:.05em;color:var(--muted);margin-bottom:2px}
svg.dg{width:100%;height:auto;display:block;margin:6px 0}
svg.cu{max-width:620px;margin:6px auto}
svg.plano{max-width:640px;margin:0 auto;border-radius:14px}
.expl{border-radius:8px;padding:10px 14px;margin-top:6px;background:var(--paper)}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;margin:8px 0}
.lado{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-bottom:22px}
.lado>div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:.93rem;border-top:5px solid var(--muted)}
.lado>div.flecha{border-top-color:var(--pa)}.lado>div.caja{border-top-color:var(--pe)}.lado>div.linea{border-top-color:var(--pl)}
.lado>div.por{border-top-color:var(--pp)}.lado>div.para{border-top-color:var(--pm)}
.lado h4{margin:0 0 6px}.lado ul{margin:0;padding-left:1.1em}.lado li{margin:3px 0}
.cier{display:grid;grid-template-columns:1fr 1fr;gap:0 12px}.cier .box{margin:8px 0}
.plan{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:10px 0}
.plan .lbl{font-size:.75rem;font-weight:700;letter-spacing:.05em;color:var(--muted);margin:0 0 4px}
.plan .pills{flex-direction:column;align-items:stretch;margin:0}
.plan .pill{text-align:left}
.res{font-family:Georgia,serif;font-size:1.35rem;font-weight:700;text-align:center;margin:8px 0;line-height:1.8}
.why2{background:var(--paper);border-radius:8px;padding:8px 12px;font-size:.93rem}
.why2 p{margin:4px 0}
.errs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.err{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.err .mal{color:var(--bad)}.err .bien{margin:4px 0}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.vchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px}
.vchip.flecha{background:var(--pa-soft);color:var(--pa)}.vchip.caja{background:var(--pe-soft);color:var(--pe)}.vchip.linea{background:var(--pl-soft);color:#7A4E0E}
.vchip.por{background:var(--pp-soft);color:var(--pp)}.vchip.para{background:var(--pm-soft);color:var(--pm)}
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
.ocard{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin-top:12px}
.ocard .ph1{font-family:Georgia,serif;font-size:1.15rem;font-weight:700}
.exq{font-family:Georgia,serif;font-size:1.5rem;font-weight:700;margin:10px 0;line-height:1.35}
.exq small{display:block;font-family:system-ui,sans-serif;font-size:.8rem;letter-spacing:.06em;color:var(--muted);font-weight:700}
.pista{display:inline-block;font-weight:700;border-radius:10px;padding:6px 14px;margin:4px 0 8px;background:var(--pl-soft);color:#7A4E0E;font-size:1.1rem}
.modo{display:inline-block;font-weight:700;border-radius:999px;padding:3px 14px;margin:6px 0;background:var(--pm-soft);color:var(--pm)}
.clock{font-family:Georgia,serif;font-size:1.6rem;font-weight:700;font-variant-numeric:tabular-nums}
.tbar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:8px 0}
.tbar i{display:block;height:100%;background:var(--coral);width:0;transition:width .25s linear}
.esc{display:grid;gap:6px;margin:8px 0}
.esc div{border:2px dashed var(--line);border-radius:8px;padding:6px 10px;color:var(--muted);font-size:.95rem}
.esc div.on{border-style:solid;border-color:var(--coral);color:var(--ink);background:var(--coral-soft)}
.words{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}
.words span{font-size:.85rem;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:2px 10px}
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
@media (max-width:700px){.cams,.errs,.cier,.lado,.duo{grid-template-columns:1fr}.plan{grid-template-columns:1fr 1fr}.qz .ops.three{grid-template-columns:1fr 1fr 1fr}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:13px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.lado>div,.err{break-inside:avoid}}
"""

STEPS = [("mapa", "El mapa"), ("reloj", "El reloj"), ("porpara", "Por y para"), ("examen", "En el examen"),
         ("practica", "Practica"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_MAPA = """
<h2>El mapa del viaje</h2>
<p class="lead">Imagina un viaje dibujado en un plano. Cada preposición es una pieza del dibujo: <b>la flecha</b> que llega, <b>la caja</b> donde estás, <b>la línea</b> con principio y final, <b>la zona</b> por donde pasas y <b>la diana</b> que tienes delante. El mismo dibujo sirve para los sitios y para las horas.</p>
__CARDS__
__LEG__
<p>Todas juntas cuentan un viaje:</p>
__VIAJE__
<h3>Mira la diferencia</h3>
<p class="muted small">Elige una pareja y toca las dos frases. Mira el dibujo de cada una.</p>
<div class="pills" id="parsel"></div>
<div class="box" id="parvis"></div>
<h3>El verbo te ayuda</h3>
<p>Mira el verbo: si hay movimiento, la flecha; si no, la caja. Y no confundas <b>con</b> (una persona) con <b>en</b> (el vehículo).</p>
__VERBOS__
<h3>Cuidado con...</h3>
__CIERRES__
<h3>Monta tu plan</h3>
<p class="muted small">La frase que más vas a usar en la tarea 3: elige una pieza de cada columna y mira por qué lleva esa preposición.</p>
<div class="plan" id="plansel"></div>
<div class="box" id="planvis" aria-live="polite"></div>
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="reloj">Siguiente: el reloj</button></div>
"""

V_RELOJ = """
<h2>El reloj: el mismo mapa, con horas</h2>
<p class="lead">Con el tiempo pasa lo mismo que con los sitios. Una hora exacta es un <b>punto</b> (a). Un mes o un año es una <b>caja</b> (en). Una parte del día es una <b>zona</b> sin hora exacta (por). Un horario es una <b>línea</b> con principio y final (de... a).</p>
__RELOJSVG__
__RELOJ__
<div class="tip"><b>El truco del horario:</b> elige la pareja al principio y no la cambies. Si empiezas con <b>de</b>, terminas con <b>a</b>; si empiezas con <b>desde</b>, terminas con <b>hasta</b>.</div>
<div class="row"><button class="btn cta" data-go="porpara">Siguiente: por y para</button></div>
"""

V_PORPARA = """
<h2>Por y para: hacia atrás y hacia delante</h2>
<p class="lead">Ponte en el centro del dibujo. <b>Por</b> mira hacia atrás: el camino por donde pasas, la zona, lo que está detrás de algo (la causa). <b>Para</b> mira hacia delante: la meta que quieres alcanzar, una persona, un objetivo, un día límite.</p>
<div id="ppbig">__PPSVG__</div>
<h3>Pruébalo</h3>
<p class="muted small">Toca una frase y mira hacia dónde mira la preposición.</p>
<div class="pills" id="ppsel"></div>
<div class="box" id="ppvis" aria-live="polite"></div>
<div class="tip"><b>Dos frases para recordarlo:</b> «Gracias <b>por</b> el regalo» (el regalo ya está detrás) · «El regalo es <b>para</b> ti» (tú eres la meta).</div>
<div class="row"><button class="btn cta" data-go="examen">Siguiente: en el examen</button></div>
"""

V_EXAMEN = """
<h2>Dónde sale en el examen</h2>
<p class="lead">Las preposiciones están en todas las tareas donde hablas de planes, horarios, sitios y rutinas: quedar con el examinador, dar indicaciones en un correo, contar tu semana o entender un horario. Son palabras pequeñas, pero si fallan, la frase cambia de sentido.</p>
__LEG__
__DONDE__
<h3>Los errores más típicos</h3>
<p>Tienes que reconocerlos en tus textos y en tu oral. Mira por qué fallan.</p>
__ERRORES__
<div class="tip"><b>Para la revisión final (5 minutos):</b> busca los verbos de movimiento (ir, venir, llegar, volver) y mira que vayan con <b>a</b>; busca los horarios y mira que las parejas no se mezclen.</div>
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACT = """
<h2>Practica</h2>
<p class="lead">Cuatro ejercicios. Cada respuesta se corrige en el momento, con la explicación.</p>
<div class="pills" id="exsel">
 <button class="pill on" data-act="ex" data-k="p1">1. ¿Qué preposición?</button>
 <button class="pill" data-act="ex" data-k="p2">2. ¿Por o para?</button>
 <button class="pill" data-act="ex" data-k="e2">3. Textos del examen</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Ahora úsalas en una tarea del examen: escribe un texto, queda con el examinador en voz alta o explica cómo se llega a un sitio.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="q">Oral: quedamos</button>
 <button class="pill" data-act="at" data-k="r">Oral: cómo se llega</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu texto y después pulsa <b>Revisar las preposiciones</b>: la página busca los errores típicos (voy en Madrid, con tren, de 9 hasta 2, a la mañana...). No corrige el texto entero: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="atq" hidden>
 <p>Como en la tarea 3 de la oral: el examinador te pregunta y tú contestas <b>en voz alta</b> con los datos de la tarjeta. Tienes pocos segundos: ¿a, en, de, por o para? Después ves una respuesta modelo.</p>
 <div id="qbox"></div>
</div>
<div id="atr" hidden>
 <p>Mira el plano. El camino está marcado desde la estación. Explica en voz alta, <b>en un minuto</b>, cómo se llega: de dónde sales, cómo vas, por dónde pasas, hasta dónde y dónde está.</p>
 <div class="pills" id="rusel"></div>
 <div id="rubox"></div>
</div>
<div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button></div>
"""

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan a mejorarlo. Al final, copia todo (también tus textos y resultados) y envíamelo.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué parte te ha ayudado más?</label>
 <div class="chips" role="group" aria-labelledby="o1l">
  <label><input type="radio" name="o1" value="El mapa del viaje">El mapa del viaje</label>
  <label><input type="radio" name="o1" value="El reloj">El reloj</label>
  <label><input type="radio" name="o1" value="Por y para">Por y para</label>
  <label><input type="radio" name="o1" value="En el examen y los errores típicos">En el examen y los errores típicos</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tú">Ahora tú</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué te cuesta más ahora?</label>
 <div class="chips" role="group" aria-labelledby="o2l">
  <label><input type="radio" name="o2" value="A o en">A o en</label>
  <label><input type="radio" name="o2" value="En o con (el vehículo)">En o con (el vehículo)</label>
  <label><input type="radio" name="o2" value="Las horas y los horarios">Las horas y los horarios</label>
  <label><input type="radio" name="o2" value="Por o para">Por o para</label>
  <label><input type="radio" name="o2" value="Explicar un camino al hablar">Explicar un camino al hablar</label>
 </div>
 <label class="q" id="o3l">3. ¿Te ayuda la idea del «mapa del viaje» (flecha, caja, línea, zona, diana)?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con estas preposiciones? (1 = nada, 10 = total)</label>
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
    o = '<h2>Preposiciones frecuentes · resumen</h2>' + cards() + LEG + frase_viaje()
    o += '<h3>El verbo te ayuda</h3>' + verbos() + '<h3>Cuidado con...</h3>' + cierres()
    o += '<h3>El reloj</h3>' + reloj_svg() + reloj()
    o += '<h3>Por y para</h3>' + porpara_svg()
    o += '<h3>Los errores típicos</h3>' + errores()
    return o

views = {
    "mapa": V_MAPA.replace("__CARDS__", cards()).replace("__LEG__", LEG).replace("__VIAJE__", frase_viaje()).replace("__VERBOS__", verbos()).replace("__CIERRES__", cierres()),
    "reloj": V_RELOJ.replace("__RELOJSVG__", reloj_svg()).replace("__RELOJ__", reloj()),
    "porpara": V_PORPARA.replace("__PPSVG__", porpara_svg()),
    "examen": V_EXAMEN.replace("__LEG__", LEG).replace("__DONDE__", donde()).replace("__ERRORES__", errores()),
    "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R06</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
""".replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

# ------------------------------------------------------------------ DATOS PARA EL SCRIPT
DLAB = {"a": "A · LA FLECHA", "en": "EN · LA CAJA", "l": "DE... A · LA LÍNEA", "p": "POR · LA ZONA", "m": "PARA · LA META", "pie": "A PIE · SIN CAJA"}
def parejas_data():
    return [{"tema": p["tema"], "a": mk(p["a"]), "b": mk(p["b"]), "da": diag(p["ka"], p["la"]), "db": diag(p["kb"], p["lb"]),
             "ta": DLAB[p["ka"]], "tb": DLAB[p["kb"]], "ea": p["ea"], "eb": p["eb"]} for p in B.PAREJAS]

DATA = {
    "key": STORAGE, "title": TITLE,
    "steps": [{"id": k, "label": l} for k, l in STEPS],
    "motivos": {k: {"f": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "familias": B.FAMILIAS,
    "parejas": parejas_data(),
    "plan": {k: [mk(x) for x in v] for k, v in B.PLAN.items()}, "planwhy": B.PLAN_WHY,
    "pp": [{"f": mk(f["f"]), "k": f["k"], "uso": f["uso"], "why": f["why"]} for f in B.POR_PARA],
    "ppsvg": {"p": porpara_svg("p"), "m": porpara_svg("m")},
    "qz": {
        "p1": {"items": B.P_PREP, "n": 8, "name": "¿Qué preposición?", "three": True, "info": "Piensa en el dibujo: ¿una flecha que llega, una caja, una línea, una zona o una meta?"},
        "p2": {"items": B.P_PP, "n": 8, "name": "¿Por o para?", "three": True, "info": "¿Mira hacia atrás (camino, zona, causa) o hacia delante (persona, objetivo, día límite)?"},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Errores típicos de los exámenes. ¿La frase está bien o mal?"},
    },
    "textos": B.TEXTOS,
    "laminas": B.LAMINAS, "focos": B.FOCOS, "detector": B.DETECTOR,
    "oral": [{"q": o["q"], "pista": o["pista"], "m": mk(o["m"])} for o in B.ORAL],
    "rutas": [{"id": r["id"], "titulo": r["titulo"], "modo": r["modo"], "m": mk(r["m"]), "svg": plano(r)} for r in B.RUTAS],
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function blank(){ return {cur:'mapa', seen:{}, par:0, pv:'a', plan:{donde:0,hora:0,como:0,destino:0}, pp:0, ex:'p1', etext:D.textos[0].id, at:'w',
  qz:{}, qlog:{}, cz:{}, w:{}, wchk:{}, wrev:{}, lam:D.laminas[0].id, qc:{n:8,t:8}, rq:null, qlog2:[], ru:D.rutas[0].id, rph:{}, rchk:{},
  o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }

/* ---------------- navegacion ---------------- */
function stepDone(id){
 if(id==='practica') return ['p1','p2','e4'].some(function(k){ return !!S.qlog[k]; }) || Object.keys(S.cz).length>0;
 if(id==='ahora') return Object.keys(S.w).some(function(k){ return (S.w[k]||'').trim().length>20; }) || S.qlog2.length>0 || Object.keys(S.rph).some(function(k){ return S.rph[k]>=2; });
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

/* ---------------- 1. el mapa: parejas y plan ---------------- */
function renderPar(){
 var o=''; D.parejas.forEach(function(p,i){ o+='<button class="pill'+(S.par===i?' on':'')+'" data-act="par" data-i="'+i+'">'+esc(p.tema)+'</button>'; });
 $('parsel').innerHTML=o;
 var p=D.parejas[S.par], v=S.pv;
 $('parvis').innerHTML='<div class="duo">'+
  '<button class="'+(v==='a'?'on':'')+'" data-act="pv" data-v="a" aria-pressed="'+(v==='a')+'"><small>'+esc(p.ta)+'</small>'+p.a+'</button>'+
  '<button class="'+(v==='b'?'on':'')+'" data-act="pv" data-v="b" aria-pressed="'+(v==='b')+'"><small>'+esc(p.tb)+'</small>'+p.b+'</button></div>'+
  (v==='a'?p.da:p.db)+'<div class="expl" aria-live="polite">'+(v==='a'?p.ea:p.eb)+'</div>';
}
var PLANLAB={donde:'¿DÓNDE QUEDÁIS?', hora:'¿A QUÉ HORA?', como:'¿CÓMO VAIS?', destino:'¿ADÓNDE?'};
function renderPlan(){
 var o='';
 ['donde','hora','como','destino'].forEach(function(k){
  o+='<div><div class="lbl">'+PLANLAB[k]+'</div><div class="pills">';
  D.plan[k].forEach(function(x,i){ o+='<button class="pill'+(S.plan[k]===i?' on':'')+'" data-act="plan" data-k="'+k+'" data-i="'+i+'">'+strip(x)+'</button>'; });
  o+='</div></div>';
 });
 $('plansel').innerHTML=o;
 var P=S.plan;
 $('planvis').innerHTML='<div class="res">Quedamos '+D.plan.donde[P.donde]+' '+D.plan.hora[P.hora]+' y vamos '+D.plan.como[P.como]+' '+D.plan.destino[P.destino]+'.</div>'+
  '<div class="why2">'+['donde','hora','como','destino'].map(function(k){ return '<p>'+D.planwhy[k]+'</p>'; }).join('')+'</div>';
}

/* ---------------- 3. por y para ---------------- */
function renderPP(){
 var o=''; D.pp.forEach(function(f,i){ o+='<button class="pill'+(S.pp===i?' on':'')+'" data-act="pp" data-i="'+i+'">'+strip(f.f)+'</button>'; });
 $('ppsel').innerHTML=o;
 var f=D.pp[S.pp];
 $('ppvis').innerHTML=D.ppsvg[f.k]+'<div class="res">'+f.f+'</div><div class="why2"><b>'+(f.k==='p'?'Por':'Para')+' · '+esc(f.uso)+'.</b> '+f.why+' '+(f.k==='p'?'Mira hacia atrás.':'Mira hacia delante.')+'</div>';
}

/* ---------------- motor de opcion multiple ---------------- */
function qzNew(k){ var c=D.qz[k]; S.qz[k]={order:shuffle(range(c.items.length)).slice(0,c.n), i:0, res:[], perm:{}}; save(); }
function qzRender(k, box){
 var c=D.qz[k]; if(!S.qz[k]) qzNew(k);
 var st=S.qz[k], N=st.order.length;
 if(st.i>=N){
  var ok=st.res.filter(function(r){return r.ok;}).length, fails=st.res.filter(function(r){return !r.ok;});
  var msg = ok>=N-1 ? '¡Muy bien! Lo tienes claro.' : (ok>=Math.ceil(N*0.6) ? 'Bien. Mira otra vez las explicaciones de las que has fallado.' : 'Vuelve a mirar el mapa y repite con otras frases.');
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
var EXINFO={e2:'Textos como los del examen: dos correos, un anuncio con horarios y un diálogo de la tarea 3. Elige la preposición de cada hueco: la corrección sale enseguida, con el motivo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
var CH=['Con ir, venir, llegar y volver he puesto a (o al).','Con estar, vivir, trabajar y quedar en un sitio he puesto en.','El vehículo va con en; con es para personas; sin vehículo, a pie o andando.','Las horas exactas van con a; los meses y los años, con en; las partes del día, con por.','En los horarios no he mezclado las parejas: de... a o desde... hasta.','Gracias por (la causa) · para ti, para aprender, para el lunes (la meta).'];
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+'</div>';
 if(L.intro) h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(f){ return '<span class="vchip '+f+'">'+D.focos[f]+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas de color te dicen qué preposición pide cada pauta. Recuerda: unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu texto</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar las preposiciones</button></div><div id="rvbox" aria-live="polite"></div>';
 h+='<h3>Mi lista de preposiciones</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
function detect(s){ var n=norm(s), out=[]; D.detector.forEach(function(d){ var r=new RegExp(d.re,'g'), m; while((m=r.exec(n))){ out.push({d:d, a:m.index, w:m[0]}); if(r.lastIndex===m.index) r.lastIndex++; } }); return out; }
window.__R06detect = function(s){ var ids={}; detect(s).forEach(function(x){ ids[x.d.id]=1; }); return Object.keys(ids).sort(); };
function cnt(nt, rx){ return (nt.match(rx)||[]).length; }
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
 var nt=norm(txt), n={a:cnt(nt,/\b(a|al)\b/g), en:cnt(nt,/\ben\b/g), por:cnt(nt,/\bpor\b/g), para:cnt(nt,/\bpara\b/g), linea:cnt(nt,/\b(desde|hasta)\b/g)+cnt(nt,/\bde\s+[a-z0-9:]+\s+a\b/g)};
 var pide=function(f){ return L.pautas.some(function(p){ return p[1].indexOf(f)>=0; }); };
 if(pide('flecha') && !n.a){ amb++; out.push('<li class="a"><b>A:</b> no lo has usado. La lámina te pide decir adónde vais y a qué hora: «vamos al cine», «a las ocho».</li>'); }
 if(pide('caja') && !n.en){ amb++; out.push('<li class="a"><b>En:</b> no lo has usado. ¿Dónde estás o en qué vas? «Quedamos en la plaza», «voy en metro».</li>'); }
 if(pide('linea') && !n.linea){ amb++; out.push('<li class="a"><b>El horario:</b> no encuentro de... a ni desde... hasta. «Trabajo de nueve a tres».</li>'); }
 if(pide('por') && !n.por){ amb++; out.push('<li class="a"><b>Por:</b> no lo has usado. «Por la mañana estudio, por la tarde...»</li>'); }
 if(pide('para') && !n.para){ amb++; out.push('<li class="a"><b>Para:</b> no lo has usado. La lámina pregunta para qué: «Estudio español para...».</li>'); }
 if(!red) out.unshift('<li class="g">No he encontrado los errores típicos. ¡Bien! Has usado a '+n.a+' '+(n.a===1?'vez':'veces')+', en '+n.en+', por '+n.por+' y para '+n.para+'. Mira tú también la lista de abajo.</li>');
 var wc=txt.trim().split(/\s+/).length;
 S.wrev[L.id]={red:red, amb:amb, a:n.a, en:n.en, por:n.por, para:n.para, words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul><p class="muted small">Tu texto: '+wc+' palabras (la lámina pide '+L.palabras[0]+'-'+L.palabras[1]+'). La página solo busca estos errores: no los ve todos. Tu profesora corrige el texto completo.</p>';
}

/* ---------------- relojes ---------------- */
var TM=null, QRUN=false;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } QRUN=false; }
function clockTxt(s){ s=Math.max(0,Math.ceil(s)); return Math.floor(s/60)+':'+(s%60<10?'0':'')+(s%60); }

/* ---------------- ahora tu: oral 1, quedamos ---------------- */
function qNew(){ S.rq={deck:shuffle(range(D.oral.length)).slice(0,S.qc.n), i:0, ph:1, res:[]}; save(); }
function renderQ(){
 var box=$('qbox'), R=S.rq, h='';
 if(!R){
  h+='<div class="ocard"><div class="ph1">Prepárate</div><p>El examinador te pregunta. Abajo tienes los datos (la hora, el sitio, el transporte...). Contesta en voz alta, con una frase completa.</p>';
  h+='<p class="small"><b>Tarjetas:</b></p><div class="pills">'+[8,12,16].map(function(n){ return '<button class="pill'+(S.qc.n===n?' on':'')+'" data-act="qn" data-n="'+n+'">'+n+'</button>'; }).join('')+'</div>';
  h+='<p class="small"><b>Tiempo para contestar:</b></p><div class="pills">'+[6,8,10].map(function(t){ return '<button class="pill'+(S.qc.t===t?' on':'')+'" data-act="qt" data-t="'+t+'">'+t+' s</button>'; }).join('')+'</div>';
  h+='<div class="row"><button class="btn cta" data-act="qstart">Empezar</button></div>';
  if(S.qlog2.length){ h+='<p class="hist"><b>Tus últimas prácticas:</b> '+S.qlog2.map(function(r){ return r.d+': '+r.ok+'/'+r.n+' ('+r.t+' s)'; }).join(' · ')+'</p>'; }
  box.innerHTML=h+'</div>'; return;
 }
 var N=R.deck.length;
 if(R.i>=N){
  var ok=R.res.filter(function(r){ return r.ok; }).length;
  h+='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+(ok>=N-1?'¡Muy bien! Quedas con el examinador sin dudar.':'Mira otra vez el mapa y el reloj, y repite: la rapidez llega con la práctica.')+'</p>';
  var fl=R.res.filter(function(r){ return !r.ok; });
  if(fl.length){ h+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fl.forEach(function(r){ var o=D.oral[r.k]; h+='<li>«'+esc(o.q)+'» → '+o.m+'</li>'; }); h+='</ul>'; }
  h+='<div class="row"><button class="btn cta" data-act="qagain">Otra vez</button></div></div>';
  box.innerHTML=h; return;
 }
 var o=D.oral[R.deck[R.i]];
 h+='<div class="ocard"><div class="cnt small muted">Tarjeta '+(R.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(R.i/N*100)+'%"></i></div>';
 h+='<div class="exq"><small>EL EXAMINADOR</small>«'+esc(o.q)+'»</div><div class="pista">'+esc(o.pista)+'</div>';
 if(R.ph===1){
  h+='<div class="clock" id="qclk">'+clockTxt(S.qc.t)+'</div><div class="tbar"><i id="qbar"></i></div>';
  h+='<div class="row">'+(QRUN?'':'<button class="btn" data-act="qgo">Seguir con el reloj</button>')+'<button class="btn cta" data-act="qskip">Ya está</button></div>';
 } else {
  h+='<div class="model"><b>Una respuesta modelo:</b><br>'+o.m+'</div>';
  h+='<p class="small" style="margin-top:12px"><b>¿Lo has dicho bien?</b> (¿a, en, de, por o para?)</p>';
  h+='<div class="row"><button class="btn cta" data-act="qeval" data-ok="1">✓ Sí</button><button class="btn" data-act="qeval" data-ok="0">✗ Me he equivocado</button></div>';
 }
 box.innerHTML=h+'</div>';
}
function qRun(){
 stopTimer(); var R=S.rq; if(!R || R.ph!==1) return;
 QRUN=true; renderQ();
 var T0=Date.now(), dur=S.qc.t;
 TM=setInterval(function(){
  var t=(Date.now()-T0)/1000, bar=$('qbar'), ck=$('qclk'); if(!bar){ stopTimer(); return; }
  ck.textContent=clockTxt(dur-t); bar.style.width=Math.min(100,t/dur*100)+'%';
  if(t>=dur){ qNext(); }
 }, 200);
}
function qNext(){ stopTimer(); S.rq.ph=2; save(); renderQ(); }

/* ---------------- ahora tu: oral 2, como se llega ---------------- */
var RDUR=60;
var RESC=['0 s · De dónde sales: «Sales de la estación...», «Desde la estación...».','20 s · Cómo vas y por dónde: «vas a pie / en autobús», «por la avenida...», «por el parque».','40 s · Hasta dónde y dónde está: «hasta la plaza...», «está en la esquina, a la derecha».'];
var RWORDS=['sales de...','desde... hasta...','vas a pie / andando','en autobús, en metro','coges la línea...','bajas en...','por la calle...','por el parque','todo recto','hasta el final','a la derecha / a la izquierda','está en la esquina'];
var RCH=['He empezado por el principio: de / desde la estación.','He dicho cómo se va: a pie, andando o en autobús (nunca «en pie» ni «con autobús»).','He dicho por dónde se pasa: por la calle..., por el parque.','He terminado con hasta... y dónde está: en la plaza, en la esquina.'];
function ruta(){ return D.rutas.filter(function(r){return r.id===S.ru;})[0]; }
function renderRuta(){
 var o=''; D.rutas.forEach(function(r){ var d=(S.rph[r.id]||0)>=2; o+='<button class="pill'+(S.ru===r.id?' on':'')+(d?' ok':'')+'" data-act="ru" data-id="'+r.id+'">'+esc(r.titulo)+(d?' ✓':'')+'</button>'; });
 $('rusel').innerHTML=o;
 var r=ruta(), ph=S.rph[r.id]||0;
 var h=r.svg+'<div class="ocard"><span class="modo">'+esc(r.titulo)+' · '+esc(r.modo)+'</span>';
 if(ph===0){
  h+='<div class="ph1">Prepárate</div><p>Sigue el camino con el dedo, desde «Estás aquí» hasta la diana. Vas a hablar <b>un minuto</b>.</p><p class="small"><b>Palabras útiles:</b></p><div class="words">'+RWORDS.map(function(x){return '<span>'+esc(x)+'</span>';}).join('')+'</div>';
  h+='<div class="row"><button class="btn cta" data-act="rgo" data-p="1">Empezar (1 min)</button></div>';
 } else if(ph===1){
  h+='<div class="ph1">Explica el camino</div><div class="clock" id="rclk">1:00</div><div class="tbar"><i id="rbar"></i></div><div class="esc" id="resc">'+RESC.map(function(x){return '<div>'+x+'</div>';}).join('')+'</div>';
  h+='<div class="row"><button class="btn" data-act="rstart" id="rbtn">Empezar el reloj</button><button class="btn cta" data-act="rgo" data-p="2">He terminado</button></div>';
 } else {
  h+='<div class="ph1">¿Qué tal ha ido?</div><ul class="check">'; RCH.forEach(function(c,i){ var k=r.id+'-'+i; h+='<li><label><input type="checkbox" data-rchk="'+k+'"'+(S.rchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
  h+='<div class="model"><b>Una explicación modelo</b><br>'+r.m+'</div>';
  h+='<div class="row"><button class="btn" data-act="rgo" data-p="0">Otra vez</button><button class="btn cta" data-act="rnext">Otro camino</button></div>';
 }
 $('rubox').innerHTML=h+'</div>';
}
function rstart(){
 stopTimer(); var T0=Date.now(); var b=$('rbtn'); if(b) b.textContent='Otra vez';
 TM=setInterval(function(){
  var t=(Date.now()-T0)/1000, bar=$('rbar'), es=$('resc'), ck=$('rclk'); if(!bar){ stopTimer(); return; }
  ck.textContent=clockTxt(RDUR-t); bar.style.width=Math.min(100,t/RDUR*100)+'%';
  var k=t<20?0:(t<40?1:2), ds=es.children; for(var i=0;i<ds.length;i++) ds[i].classList.toggle('on', i===k);
  if(t>=RDUR){ stopTimer(); bar.style.width='100%'; ck.textContent='0:00'; }
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
 var L=['CURSO DELE A2 - R06: PREPOSICIONES FRECUENTES','Nombre: '+(S.name||'-'),''];
 L.push('EJERCICIOS (ultimo resultado)');
 ['p1','p2','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 D.textos.forEach(function(t){
  var f=fbList(t.id,t.texto), errs=[];
  gapInfo(t.id,t.texto).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); });
  var started=Object.keys(S.cz).some(function(k){return k.indexOf(t.id+'-')===0;});
  L.push('- Textos del examen, '+t.titulo+': '+(started?f.first+'/'+f.tot+' a la primera'+(f.done<f.tot?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 L.push('','ORAL: QUEDAMOS');
 if(!S.qlog2.length) L.push('sin hacer');
 S.qlog2.forEach(function(r){ L.push('- '+r.d+': '+r.ok+'/'+r.n+' bien (autoevaluacion), '+r.t+' s para contestar'+(r.fails&&r.fails.length?' | fallos: '+r.fails.join(' / '):'')); });
 L.push('','ORAL: COMO SE LLEGA');
 var rd=D.rutas.filter(function(r){ return (S.rph[r.id]||0)>=2; });
 if(!rd.length) L.push('sin hacer');
 rd.forEach(function(r){ var n=0; RCH.forEach(function(c,i){ if(S.rchk[r.id+'-'+i]) n++; }); L.push('- '+r.titulo+' ('+r.modo+'): hecho, autorrevision '+n+'/'+RCH.length); });
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' ('+l.palabras[0]+'-'+l.palabras[1]+' palabras)','Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision: '+rv.red+' avisos rojos, '+rv.amb+' ambar | a: '+rv.a+', en: '+rv.en+', por: '+rv.por+', para: '+rv.para+' | '+rv.words+' palabras');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. Lo que mas cuesta: '+(S.o2||'-'),'3. El mapa del viaje: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 par:function(b){ S.par=+b.getAttribute('data-i'); S.pv='a'; save(); renderPar(); },
 pv:function(b){ S.pv=b.getAttribute('data-v'); save(); renderPar(); },
 plan:function(b){ S.plan[b.getAttribute('data-k')]=+b.getAttribute('data-i'); save(); renderPlan(); },
 pp:function(b){ S.pp=+b.getAttribute('data-i'); save(); renderPP(); },
 ex:function(b){ S.ex=b.getAttribute('data-k'); save(); renderEx(); },
 etext:function(b){ S.etext=b.getAttribute('data-id'); save(); renderE2(); },
 qa:function(b){ var k=b.getAttribute('data-k'); qzAnswer(k, +b.getAttribute('data-o')); qzRender(k, $('exbox')); nav(); var f=$('exbox').querySelector('.fb'); if(f&&f.scrollIntoView) f.scrollIntoView({block:'nearest'}); },
 qnext:function(b){ var k=b.getAttribute('data-k'); S.qz[k].i++; save(); qzRender(k, $('exbox')); },
 qrep:function(b){ var k=b.getAttribute('data-k'); qzNew(k); qzRender(k, $('exbox')); },
 czreset:function(b){ b.getAttribute('data-ids').split(',').forEach(function(id){ Object.keys(S.cz).forEach(function(g){ if(g.indexOf(id+'-')===0) delete S.cz[g]; }); }); save(); renderEx(); nav(); },
 at:function(b){ S.at=b.getAttribute('data-k'); save(); renderAt(); },
 lam:function(b){ S.lam=b.getAttribute('data-id'); save(); renderLam(); },
 review:function(){ review(); nav(); },
 qn:function(b){ S.qc.n=+b.getAttribute('data-n'); save(); renderQ(); },
 qt:function(b){ S.qc.t=+b.getAttribute('data-t'); save(); renderQ(); },
 qstart:function(){ qNew(); qRun(); },
 qgo:function(){ qRun(); },
 qskip:function(){ qNext(); },
 qeval:function(b){
  var R=S.rq; R.res.push({k:R.deck[R.i], ok:b.getAttribute('data-ok')==='1'}); R.i++; R.ph=1; save();
  if(R.i>=R.deck.length){
   var ok=R.res.filter(function(r){return r.ok;}).length, d=new Date();
   S.qlog2.push({d:d.getDate()+'/'+(d.getMonth()+1), n:R.deck.length, t:S.qc.t, ok:ok, fails:R.res.filter(function(r){return !r.ok;}).map(function(r){ return D.oral[r.k].q; })});
   if(S.qlog2.length>6) S.qlog2=S.qlog2.slice(-6);
   save(); renderQ(); nav();
  } else qRun();
 },
 qagain:function(){ stopTimer(); S.rq=null; save(); renderQ(); },
 ru:function(b){ stopTimer(); S.ru=b.getAttribute('data-id'); save(); renderRuta(); },
 rgo:function(b){ stopTimer(); var p=+b.getAttribute('data-p'); S.rph[S.ru]=p; save(); renderRuta(); nav(); if(p===1) rstart(); },
 rstart:function(){ rstart(); },
 rnext:function(){ stopTimer(); var ids=D.rutas.map(function(r){return r.id;}), free=ids.filter(function(i){ return (S.rph[i]||0)<2 && i!==S.ru; }); if(!free.length) free=ids.filter(function(i){return i!==S.ru;}); S.ru=free[Math.floor(Math.random()*free.length)]; save(); renderRuta(); },
 printres:function(){ var v=$('v-resumen'); v.classList.add('printme'); window.print(); setTimeout(function(){ v.classList.remove('printme'); },500); },
 copy:function(){
  var t=pack(), box=$('cbox');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar automáticamente. Escribe tus respuestas en un correo para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
 }
};
window.__R06pack = pack;
function renderAt(){
 var ps=$('atsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.at);
 $('atw').hidden = S.at!=='w'; $('atq').hidden = S.at!=='q'; $('atr').hidden = S.at!=='r'; stopTimer();
 if(S.rq && S.rq.ph===1) QRUN=false;
 if(S.at==='w') renderLam(); else if(S.at==='q') renderQ(); else renderRuta();
}
document.addEventListener('click', function(e){
 var g=e.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.tagName==='SELECT' && t.hasAttribute('data-g')){ czChange(t); return; }
 if(t.hasAttribute && t.hasAttribute('data-wchk')){ S.wchk[t.getAttribute('data-wchk')]=t.checked; save(); return; }
 if(t.hasAttribute && t.hasAttribute('data-rchk')){ S.rchk[t.getAttribute('data-rchk')]=t.checked; save(); return; }
 if(['o1','o2','o3','o5'].indexOf(t.name)>=0){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){
 var t=e.target;
 if(t.id==='wtext'){ S.w[S.lam]=t.value; save(); }
 if(t.id==='o4'){ S.o4=t.value; save(); }
 if(t.id==='sname'){ S.name=t.value; save(); }
});
window.addEventListener('afterprint', function(){ var v=$('v-resumen'); if(v) v.classList.remove('printme'); });
if(S.rph){ Object.keys(S.rph).forEach(function(k){ if(S.rph[k]===1) S.rph[k]=0; }); }

renderPar(); renderPlan(); renderPP(); renderEx(); renderAt(); renderOpn(); go(S.cur);
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
      "| items:", len(B.P_PREP) + len(B.P_PP) + len(B.E_BIENMAL),
      "| pruebas del detector:", len(B.DETECTOR_PRUEBAS), "(navegador: %s)" % ("igual que Python" if NODE_OK else "sin probar"),
      "| buena en el desplegable (1a/2a/3a):", POS_TXT, "| parejas:", len(B.PAREJAS), "| tarjetas orales:", len(B.ORAL), "| caminos:", len(B.RUTAS))
