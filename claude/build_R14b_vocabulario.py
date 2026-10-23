# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R14b DEL CURSO DE PREPARACION DELE A2: VOCABULARIO EN ESCENAS (2) · FUERA DE CASA
# (copia del build de la R14a: mismo motor y mismas pestanas; cambia solo el contenido y lo que nombraba la R14a)
# Uso: python3 build_R14b_vocabulario.py
#   -> DELEA2_curso_R14b_vocabulario_fuera_de_casa.html   (subir a biblioteca/recursos/A2/dele-curso/)
#   -> DELEA2_curso_R14b_guion.txt   (audios: python3 generar_audios.py DELEA2_curso_R14b_guion.txt en Documentos/DELE_AUDIO)
#   -> R14b_prompts_imagenes.txt y nombres.txt (12 tripticos de vinetas A-B-C de la tarea 1 de la auditiva)
# Contenidos: solo en banco_R14b_vocabulario.py. Este archivo monta la pagina y comprueba el banco.
# Mismo formato y motor que R01-R08 (curso_comun.py, barra de pestanas nueva, correccion inmediata, huecos con el
# barajado arreglado, "Ahora tu" con detector, Copiar para el corrector de Maria).
# Enfoque cognitivo: LAS PALABRAS VIVEN EN ESCENAS. La escena (red de cuatro ramas + texto + tapa y recuerda),
# el trio (las tres vinetas de la tarea 1, dos se descartan) y la pareja de parafrasis (lectura y auditiva).
import json, os, re, shutil, subprocess, sys, tempfile, unicodedata
from curso_comun import CSS, EMAIL, page
import banco_R14b_vocabulario as B

TITLE = "Vocabulario en escenas (2): fuera de casa"
FILE = "DELEA2_curso_R14b_vocabulario_fuera_de_casa.html"
STORAGE = "dele-a2-curso-R14b"
GUION = "DELEA2_curso_R14b_guion.txt"
PROMPTS = "R14b_prompts_imagenes.txt"
WP = "https://2spanishteachers.com/wp-content/uploads/" + B.MES_WP.strip("/") + "/"
WP_T2 = "https://2spanishteachers.com/wp-content/uploads/" + B.MES_WP_T2.strip("/") + "/"
VIN = ("Simple flat vector illustration in the style of an exam booklet, thin dark outlines, limited palette of soft coral, teal "
       "and warm grey, plain white background, three separate panels side by side of equal size with white space between them, "
       "one subject per panel, centred, no text, no letters, no labels, 3:1. ")

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
MARK = re.compile(r"\[([1-4]):([^\[\]]+)\]")
AMARK = re.compile(r"\[(v|x):([^\[\]]+)\]")
TAG = re.compile(r"^\[([a-z ]+)\]\s+")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
ART = re.compile(r"^(?:el|la|los|las|un|una|unos|unas)\s+", re.I)
def lem(w): return norm(ART.sub("", w.strip()))
def plain(s): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", MARK.sub(lambda m: m.group(2).split("=")[0], s))).strip()
def aplain(s): return AMARK.sub(lambda m: m.group(2), TAG.sub("", s))
def filled(s): return re.sub(r"<[^>]+>", " ", GAP.sub(lambda m: m.group(1).split("#")[0].split("|")[0], s))
def nwords(s): return len(re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", s))
# Estructuras [R] que no pueden salir en los textos ni en los audios de la ficha
R_TXT = re.compile(r"\b(?:me|te|se|nos|os)\s+(?:lo|la|los|las)\b|(?:rme|rte|rse|rnos)(?:lo|la|los|las)\b|\blo que\b|\baunque\b|\bsin embargo\b|\basi que\b")
def chk_r(s, where):
    m = R_TXT.search(norm(s))
    if m: err("%s: estructura [R] o de B1 (%s): %s" % (where, m.group(0), s[:80]))

AREAS = B.AREAS
if list(AREAS) != B.ORDEN_AREAS: err("AREAS y ORDEN_AREAS no coinciden")
ESC = {e["id"]: e for e in B.ESCENAS}
if len(ESC) != len(B.ESCENAS): err("ids de escena repetidos")
DICES = lambda r: all(re.search(r"[.?!]$", w) for w in r[1])   # rama de frases ("Lo que dices")
for a in B.ORDEN_AREAS:
    if sum(1 for e in B.ESCENAS if e["area"] == a) != 2: err("cada area lleva dos escenas: " + a)
for e in B.ESCENAS:
    where = "escena " + e["id"]
    if e["area"] not in AREAS: err(where + ": area desconocida")
    if len(e["ramas"]) != 4: err(where + ": cuatro ramas")
    for nom, ws in e["ramas"]:
        if len(ws) < 4: err("%s: la rama %s tiene pocas palabras" % (where, nom))
        if len({lem(w) for w in ws}) != len(ws): err("%s: palabras repetidas en la rama %s" % (where, nom))
    rest = MARK.sub("", e["texto"])
    if "[" in rest or "]" in rest: err(where + ": marca mal cerrada")
    ms = MARK.findall(e["texto"])
    if len(ms) < 10: err(where + ": el texto tiene pocas palabras marcadas (%d)" % len(ms))
    used = set()
    for n, w in ms:
        form, _, lema = w.partition("=")
        lema = lema or form
        rama = e["ramas"][int(n) - 1]
        if lem(lema) not in [lem(x) for x in rama[1]]: err("%s: «%s» no está en la rama %s (%s)" % (where, lema, n, rama[0]))
        used.add(int(n))
    for i, r in enumerate(e["ramas"]):
        if not DICES(r) and i + 1 not in used: err("%s: el texto no usa la rama %d (%s)" % (where, i + 1, r[0]))
    nw = nwords(plain(e["texto"]))
    if not 60 <= nw <= 110: err("%s: el texto tiene %d palabras (60-110)" % (where, nw))
    chk_r(plain(e["texto"]), where)
REDWORDS = {a: [lem(w) for e in B.ESCENAS if e["area"] == a for _, ws in e["ramas"] for w in ws] for a in AREAS}
for a, ts in B.TRIOS.items():
    if a not in AREAS or len(ts) < 3: err("trios: tres por area (%s)" % a)
    for nom, tres in ts:
        if len(tres) != 3: err("trio %s: tres palabras" % nom)
        for w in tres:
            if lem(w) not in REDWORDS[a]: err("trio %s (%s): «%s» no está en las escenas de su area" % (nom, a, w))
for a in AREAS:
    if len(B.PAREJAS.get(a, [])) != 5: err("parejas: cinco por area (%s)" % a)
    for t, p in B.PAREJAS[a]:
        if norm(t) == norm(p): err("pareja igual: " + t)
        chk_r(t + " " + p, "pareja")

# Escucha y elige
VOCES = None
ESP = None
for d in (".", os.path.dirname(os.path.abspath(__file__))):
    vp = os.path.join(d, "voces.txt")
    if os.path.exists(vp):
        VOCES = {l.split("=")[0].strip().upper() for l in open(vp, encoding="utf-8") if "=" in l.split("#")[0]}
        ESP = {l.split("=")[0].strip().upper() for l in open(vp, encoding="utf-8") if "=" in l.split("#")[0] and "· España ·" in l}
        break
IMGN = re.compile(r"^R14b_CA1_\d\d_[a-z]+(?:_[a-z]+)+$")
if len(B.CA1) != 12: err("CA1: doce conversaciones")
seen_img = set()
for i, it in enumerate(B.CA1):
    where = "escucha %d" % (i + 1)
    if it["area"] not in AREAS: err(where + ": area desconocida")
    if len(it["o"]) != 3 or len(set(it["o"])) != 3: err(where + ": tres opciones distintas")
    if it["ok"] not in (0, 1, 2): err(where + ": ok 0-2")
    vs = [l[2] for l in it["lines"]]
    for l in it["lines"]:
        if not TAG.match(l[2]): err("%s: cada intervención empieza con su etiqueta de emoción: %s" % (where, l[2][:40]))
        if VOCES is not None and l[1] not in VOCES: err("%s: la voz %s no está en voces.txt" % (where, l[1]))
        if l[1] in B.VOCES_EVITAR: err("%s: la voz %s es del último modelo o está descartada" % (where, l[1]))
        if l[1] == "0": err(where + ": el narrador no habla en la conversación")
    if len({l[1] for l in it["lines"]}) < 2: err(where + ": dos voces")
    vz = {l[1] for l in it["lines"]}
    for v in vz:
        if v in B.VOCES_R14A and ESP is not None and v not in ESP: err("%s: de la R14a solo se repiten voces peninsulares (%s)" % (where, v))
    if ESP is not None and len(vz & ESP) != 1: err("%s: una voz peninsular y una latinoamericana (Maria, 23/10): %s" % (where, sorted(vz)))
    allm = [m for l in vs for m in AMARK.findall(l)]
    if sum(1 for k, _ in allm if k == "v") != 1 or sum(1 for k, _ in allm if k == "x") < 2: err(where + ": un [v:] y al menos dos [x:]")
    txt = " ".join(aplain(l) for l in vs)
    nw = nwords(txt)
    if not 50 <= nw <= 80: err("%s: la conversación tiene %d palabras (50-80, como la tarea 1)" % (where, nw))
    if re.search(r"\d", txt + it["pres"]): err(where + ": cifras con letras en el audio")
    chk_r(txt, where)
    if not it["pres"].startswith("Va a escuchar a "): err(where + ": la presentación del narrador empieza «Va a escuchar a...»")
    if not IMGN.match(it["img"]) or it["img"] in seen_img: err(where + ": nombre de imagen que diga qué es (R14b_CA1_NN_a_b_c) y único")
    seen_img.add(it["img"])
    if not all("Panel %d:" % k in it["prompt"] for k in (1, 2, 3)): err(where + ": el prompt tiene un panel por opción")
    if not it.get("why"): err(where + ": falta el porqué")
if len({it["ok"] for it in B.CA1}) < 3: err("CA1: la buena tiene que caer en A, B y C")
for a in AREAS:
    if sum(1 for it in B.CA1 if it["area"] == a) < (1 if a == B.RINCON else 2): err("CA1: al menos dos conversaciones por area, una en el rincon (%s)" % a)

# Dilo de otra forma
for it in B.ANUNCIOS:
    where = "anuncio " + it["titulo"]
    nw = nwords(it["texto"])
    if not 30 <= nw <= 65: err("%s: %d palabras (30-65)" % (where, nw))
    if len(it["o"]) != 3 or len(set(it["o"])) != 3: err(where + ": tres opciones distintas")
    if it["lit"] not in (1, 2): err(where + ": lit = indice del distractor literal (1 o 2)")
    if it["area"] not in AREAS or not it.get("why"): err(where + ": area o porqué")
    chk_r(it["texto"], where)
if {it["area"] for it in B.ANUNCIOS} != set(AREAS): err("anuncios: de todas las areas")
# Practica
for it in B.P_SOBRA:
    if len(it["o"]) != 4 or len(set(it["o"])) != 4 or not it.get("why"): err("¿Qué sobra?: cuatro opciones distintas y porqué: " + it["q"])
for it in B.P_VERBO:
    if it["q"].count("____") != 1 or len(it["o"]) != 3 or len(set(it["o"])) != 3 or not it.get("why"): err("verbo: un ____ y tres opciones: " + it["q"])
    chk_r(it["q"].replace("____", it["o"][0]), "verbo")
for k in ("P_SOBRA", "P_VERBO"):
    if {it["area"] for it in getattr(B, k)} != set(AREAS): err(k + ": de todas las areas")
for it in B.E_BIENMAL:
    if it["ok"] not in (0, 1) or not it.get("why"): err("bien/mal mal definido: " + it["q"])
    if it["ok"] == 1 and not it.get("fix"): err("bien/mal: frase mal sin corrección: " + it["q"])
    if it["ok"] == 0 and (it.get("fix") or it.get("det")): err("bien/mal: frase bien con corrección o aviso: " + it["q"])
if sum(1 for i in B.E_BIENMAL if i["ok"] == 0) < 5: err("bien/mal: faltan frases bien")
# Textos con huecos
for k, (a, w, ok) in B.MOTIVOS.items():
    if a not in AREAS or not w or not ok: err("motivo mal definido: " + k)
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
    chk_r(filled(t["texto"]), "texto " + t["id"])
    return n
ngaps = {t["id"]: chk_gaps(t) for t in B.TEXTOS}
usados = {g.split("#")[1] for t in B.TEXTOS for g in GAP.findall(t["texto"])}
for m in B.MOTIVOS:
    if m not in usados: err("los textos no usan el motivo " + m)
# Laminas
for L in B.LAMINAS:
    if len(L["pautas"]) != 5: err("lamina %s: 5 pautas" % L["id"])
    for _, ars in L["pautas"]:
        for a in ars:
            if a not in AREAS: err("lamina %s: area desconocida %s" % (L["id"], a))
    nw = nwords(L["mensaje"])
    if L["tarea"].startswith("Tarea 1") and not 35 <= nw <= 45: err("lamina %s: el mensaje de entrada tiene %d palabras (35-45)" % (L["id"], nw))
if {a for L in B.LAMINAS for _, ars in L["pautas"] for a in ars} != set(AREAS): err("las laminas tienen que trabajar todas las areas")
# Oral
if [o["id"] for o in B.ORAL] != [1, 2, 3, 4, 5, 6]: err("oral: fotos 1-6 del taller de la foto (la R14a usa las 7-12)")
for o in B.ORAL:
    if len(o["grupos"]) != 3 or sum(len(g[1]) for g in o["grupos"]) < 16: err("oral foto %d: tres grupos y al menos 16 palabras" % o["id"])

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
for k in B.REQ:
    if k not in ids: err("REQ: id desconocido " + k)
for it in B.E_BIENMAL:
    if it.get("det") and it["det"] not in ids: err("bien/mal: aviso desconocido " + it["det"])

# Palabras de cada area para contar en la escritura: se sacan de las redes (nombres y adjetivos, sin verbos ni frases)
VERB = re.compile(r"^(\w+?)(ar|er|ir)(se)?(?:\s+(.*))?$")
STOP = {"bien", "mal", "grande", "pequeno", "a alguien", "alguien"}
def noun_pat(b, adj=False):
    """Nombres: singular y plural. Adjetivos: tambien masculino y femenino."""
    if " " in b: return re.escape(b) + r"(?:s|es)?"
    if b.endswith("o") and (adj or " " not in b): return re.escape(b[:-1]) + r"(?:o|a|os|as)"   # el medico / la medica
    if adj and b.endswith("a"): return re.escape(b[:-1]) + r"(?:a|as)"
    if b.endswith("s"): return re.escape(b)
    if b[-1] in "aeiouy": return re.escape(b) + r"s?"
    if b.endswith("z"): return re.escape(b[:-1]) + r"(?:z|ces)"
    return re.escape(b) + r"(?:es)?"
ARTS = ("el ", "la ", "los ", "las ", "un ", "una ")
def forms(w):
    """(palabra que se ensena, regex) para contar las palabras de las escenas en la escritura, o None.
    Nombres (con articulo en la red) en singular y plural; adjetivos con su genero y numero; verbos regulares por su
    raiz (5 letras o mas); en las expresiones con verbo (pedir cita, fregar los platos), lo que va detras del verbo."""
    if re.search(r"[.?!]$", w): return None
    b = lem(w)
    if b.endswith(" de"): return None
    noun = w.strip().lower().startswith(ARTS)
    m = None if noun else VERB.match(b)
    if m:
        obj = m.group(4)
        if obj:
            o = lem(obj)
            if o in STOP: return None
            adj = m.group(1) + m.group(2) in ("estar", "comer")
            return (ART.sub("", w.split(" ", 1)[1]), r"\b" + noun_pat(o, adj) + r"\b")
        stem = m.group(1)
        return (w, r"\b" + re.escape(stem) + r"\w*") if len(stem) >= 5 else None
    return (ART.sub("", w), r"\b" + noun_pat(b, not noun) + r"\b")
CUENTA = {}
for a in AREAS:
    seen = {}
    for e in B.ESCENAS:
        if e["area"] != a: continue
        for _, ws in e["ramas"]:
            for w in ws:
                f = forms(w)
                if f and norm(f[0]) not in seen: seen[norm(f[0])] = [f[0], f[1]]
    CUENTA[a] = list(seen.values())
    if len(CUENTA[a]) < 25: err("cuenta del area %s: pocas palabras (%d)" % (a, len(CUENTA[a])))
def cuenta_py(t):
    n = norm(t); return {a: sorted({d for d, r in CUENTA[a] if re.search(r, n)}) for a in AREAS}

SENT = re.compile(r"[^.!?\n]+[.!?]*")
def det(txt):
    out = set(); sents = [norm(s) for s in SENT.findall(txt)]
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
    vistos = set()
    for it in B.E_BIENMAL:
        if it.get("det"):
            r = det(it["q"])
            if it["det"] not in r: err("detector: la frase mala «%s» no da el aviso %s (da %s)" % (it["q"], it["det"], r))
            vistos |= set(r)
    for k in B.REQ:
        if k not in vistos: err("ninguna frase mala de ¿Bien o mal? da el aviso " + k)
    # Nada de lo que la ficha da por bueno puede dar NINGUN aviso
    buenos = [plain(e["texto"]) for e in B.ESCENAS] + [w for e in B.ESCENAS for r in e["ramas"] if DICES(r) for w in r[1]]
    buenos += [" ".join(aplain(l[2]) for l in it["lines"]) for it in B.CA1] + [it["pres"] for it in B.CA1]
    buenos += [it["texto"] for it in B.ANUNCIOS] + [filled(t["texto"]) for t in B.TEXTOS] + [L["mensaje"] for L in B.LAMINAS]
    buenos += [x for a in AREAS for p in B.PAREJAS[a] for x in p] + [d[2] for d in B.DESCARTE]
    buenos += [it["q"] for it in B.E_BIENMAL if it["ok"] == 0] + [it["q"].replace("____", it["o"][0]) for it in B.P_VERBO]
    for b in buenos:
        r = det(b)
        if r: err("detector: aviso %s en un texto bueno: %r" % (r, b.strip()[:90]))

NODE_OK = None
if not ERR and shutil.which("node"):
    textos_c = [t for t, _ in B.DETECTOR_PRUEBAS] + [plain(e["texto"]) for e in B.ESCENAS] + [filled(t["texto"]) for t in B.TEXTOS]
    js_t = ("var D=%s;function norm(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}"
            "function det(t){var o={},ss=(t.match(/[^.!?\\n]+[.!?]*/g)||[]).map(norm);D.d.forEach(function(d){var r=new RegExp(d.re);"
            "if(d.sc==='s'){if(ss.some(function(s){return r.test(s);}))o[d.id]=1;}else if(r.test(norm(t)))o[d.id]=1;});return Object.keys(o).sort();}"
            "function cnt(t){var n=norm(t),o={};Object.keys(D.c).forEach(function(a){var f={};D.c[a].forEach(function(p){if(new RegExp(p[1]).test(n))f[p[0]]=1;});o[a]=Object.keys(f).sort();});return o;}"
            "var bad=[];D.p.forEach(function(p){var ids=det(p[0]);if(ids.join()!==p[1].slice().sort().join())bad.push(p[0]+' -> '+ids.join());});"
            "D.t.forEach(function(x){var c=cnt(x[0]);Object.keys(c).forEach(function(a){if(c[a].join('|')!==x[1][a].join('|'))bad.push('cuenta '+a+': '+x[0].slice(0,40)+' '+c[a].join(',')+' / '+x[1][a].join(','));});});"
            "console.log(JSON.stringify(bad));") % json.dumps(
        {"d": [{"id": d["id"], "re": d["re"], "sc": d["sc"]} for d in B.DETECTOR], "p": B.DETECTOR_PRUEBAS, "c": CUENTA,
         "t": [[t, cuenta_py(t)] for t in textos_c]}, ensure_ascii=False)
    fd, path = tempfile.mkstemp(suffix=".js"); os.write(fd, js_t.encode("utf-8")); os.close(fd)
    try:
        out = subprocess.run(["node", path], capture_output=True, text=True, timeout=30)
        bad = json.loads(out.stdout or "null")
        if bad is None: err("node: no se ha podido probar el detector: " + out.stderr[:200])
        elif bad: err("detector en el navegador distinto de Python: " + "; ".join(bad[:6]))
        else: NODE_OK = True
    finally: os.unlink(path)
    # Las escenas tienen que contar palabras de su area (si no, la cuenta de la escritura no sirve)
    for e in B.ESCENAS:
        if len(cuenta_py(plain(e["texto"]))[e["area"]]) < 8: err("la cuenta de palabras no ve la escena %s" % e["id"])

if ERR:
    print("\n".join("ERROR: " + e for e in ERR)); sys.exit(1)
for d in B.DETECTOR: d.pop("_rx", None)

# ------------------------------------------------------------------ SALIDAS PARA MARIA: GUION, PROMPTS, NOMBRES
NUM = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce"]
def audio_name(i): return "DELEA2_curso_R14b_CA1_%02d" % (i + 1)
voces_usadas = sorted({l[1] for it in B.CA1 for l in it["lines"]})
G = ["# GUION DE AUDIO · Curso DELE A2 · Ficha R14b «Vocabulario en escenas (2)» · Escucha y elige (como la tarea 1 de la auditiva)",
     "# Un audio por conversación (doce): la página lo deja escuchar dos veces, como en el examen.",
     "# SIN EFECTOS DE SONIDO (ni sintonía, ni din-don, ni pitido). Cada intervención con su etiqueta de emoción de ElevenLabs v3.",
     "# Cifras escritas con letras. Ninguna voz del M1 (el último modelo) ni de las descartadas.",
     "# Cada conversación: una voz peninsular (repetida de la R14a, María 23/10) y una latinoamericana libre.",
     "# Voces: " + ", ".join(voces_usadas),
     "# En Terminal (carpeta Documentos/DELE_AUDIO):",
     "#   cd ~/Documents/DELE_AUDIO && python3 generar_audios.py " + GUION,
     "# Los audios salen en la carpeta salida: " + audio_name(0) + ".m4a ... " + audio_name(11) + ".m4a",
     "# Subirlos a WordPress, Medios, carpeta del mes " + B.MES_WP + " (si es otro mes, cambiar MES_WP en el banco y regenerar).", ""]
for i, it in enumerate(B.CA1):
    G.append("# ARCHIVO " + audio_name(i))
    G.append("# Conversación %d (%s) · %s · buena: %s" % (i + 1, AREAS[it["area"]]["n"], it["q"], "ABC"[it["ok"]]))
    G.append("0: " + it["pres"]); G.append("[1]")
    for lab, voz, t in it["lines"]:
        G.append("%s: %s" % (voz, AMARK.sub(lambda m: m.group(2), t)))
    G.append("")
guion = "\n".join(G)
habla = [l.split(":", 1)[1] for l in guion.split("\n") if ":" in l and not l.startswith("#")]
assert not [h for h in habla if re.search(r"\d", h)], "cifras en el guion"
open(GUION, "w", encoding="utf-8").write(guion)

def asc(s): return re.sub(r"[\"'|«»]", "", norm(s))
N = ["# LISTA DE IMAGENES · Curso DELE A2 · Ficha R14b (vinetas A-B-C de Escucha y elige)", "# nombre | ancho px | KB max | descripcion",
     "CARPETA: DELE_A2_curso", ""]
R = ["PROMPTS DE IMÁGENES · Curso DELE A2 · Ficha R14b «Vocabulario en escenas (2)» (en inglés, uno por imagen; nombres en nombres.txt)",
     "Doce trípticos de viñetas A-B-C, como los de la tarea 1 de la auditiva: tres paneles iguales, un objeto o una acción en cada uno, en el orden A, B, C.",
     "=" * 75]
for i, it in enumerate(B.CA1):
    N.append("%s | 1200 | 90 | R14b escucha %d: %s" % (it["img"], i + 1, " / ".join(asc(o) for o in it["o"])))
    R.append("\n%s.jpg  (1200 px, viñetas A-B-C)\n%s%s" % (it["img"], VIN, it["prompt"]))
open("nombres.txt", "w", encoding="utf-8").write("\n".join(N) + "\n")
open(PROMPTS, "w", encoding="utf-8").write("\n".join(R) + "\n")
for l in N[4:]:
    assert not re.search(r"[áéíóúñÁÉÍÓÚÑ\"']", l), l

# ------------------------------------------------------------------ HTML ESTATICO
INK = "#14161C"; MUT = "#5E5A55"
BCOL = ["#1D5FA8", "#2F7D4F", "#9A6412", "#C2451E"]
ACOL = {"vi": "#1D5FA8", "oc": "#C2451E", "es": "#6B46C1", "tr": "#9A6412", "ti": "#0F7C7C", "ri": "#2F7D4F"}
def svg(vb, aria, inner, cls="ic"): return '<svg class="%s" viewBox="%s" role="img" aria-label="%s">%s</svg>' % (cls, vb, aria, inner)
def t_(x, y, s, size=14, col=INK, w="600"): return '<text x="%s" y="%s" text-anchor="middle" font-size="%s" font-weight="%s" fill="%s">%s</text>' % (x, y, size, w, col, s)

def tool_svg(k):
    o = ""
    if k == "escena":
        o += '<circle cx="110" cy="52" r="24" fill="#FCE9E1" stroke="#E8603C" stroke-width="3"/>' + t_(110, 57, "escena", 12, "#C2451E", "700")
        for (x, y), c in zip(((30, 18), (190, 18), (30, 86), (190, 86)), BCOL):
            o += '<line x1="110" y1="52" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x, y, c)
            o += '<rect x="%d" y="%d" width="36" height="20" rx="6" fill="#fff" stroke="%s" stroke-width="3"/>' % (x - 18, y - 10, c)
    elif k == "trio":
        for i, x in enumerate((20, 84, 148)):
            ok = i == 2
            o += '<rect x="%d" y="22" width="52" height="52" rx="8" fill="%s" stroke="%s" stroke-width="3"/>' % (x, "#E3F1E8" if ok else "#fff", "#2F7D4F" if ok else "#B3261E")
            o += t_(x + 26, 18, "ABC"[i], 12, MUT, "700")
            if ok: o += '<path d="M%d,48 l9,9 l17,-19" fill="none" stroke="#2F7D4F" stroke-width="4"/>' % (x + 14)
            else: o += '<path d="M%d,35 l26,26 M%d,35 l-26,26" stroke="#B3261E" stroke-width="4"/>' % (x + 13, x + 39)
    else:
        o += '<rect x="10" y="26" width="84" height="44" rx="14" fill="#fff" stroke="#1D5FA8" stroke-width="3"/>' + t_(52, 53, "gratis", 14, "#1D5FA8", "700")
        o += '<rect x="126" y="26" width="84" height="44" rx="14" fill="#fff" stroke="#2F7D4F" stroke-width="3"/>' + t_(168, 47, "no se", 13, "#2F7D4F", "700") + t_(168, 62, "paga", 13, "#2F7D4F", "700")
        o += t_(110, 56, "=", 26, "#E8603C", "700")
    return svg("0 0 220 100", {"escena": "Una escena con cuatro ramas", "trio": "Tres viñetas: dos se descartan", "pareja": "Dos maneras de decir lo mismo"}[k], o)

def area_svg(a):
    c = ACOL[a]; o = '<circle cx="20" cy="20" r="19" fill="#fff" stroke="%s" stroke-width="2.5"/>' % c
    if a == "vi": o += '<rect x="11" y="16" width="18" height="15" rx="2" fill="none" stroke="%s" stroke-width="2.5"/><path d="M16,16 v-4 h8 v4" fill="none" stroke="%s" stroke-width="2.5"/>' % (c, c)
    elif a == "oc": o += '<circle cx="20" cy="20" r="9" fill="none" stroke="%s" stroke-width="2.5"/><path d="M11,20 h18 M20,11 q6,9 0,18 M20,11 q-6,9 0,18" fill="none" stroke="%s" stroke-width="1.8"/>' % (c, c)
    elif a == "es": o += '<path d="M8,17 L20,11 L32,17 L20,23 Z" fill="%s"/><path d="M13,20 v6 q7,4 14,0 v-6" fill="none" stroke="%s" stroke-width="2.5"/>' % (c, c)
    elif a == "tr": o += '<rect x="9" y="15" width="22" height="15" rx="2" fill="none" stroke="%s" stroke-width="2.5"/><path d="M16,15 v-4 h8 v4 M9,21 h22" fill="none" stroke="%s" stroke-width="2.5"/>' % (c, c)
    elif a == "ti": o += '<circle cx="16" cy="16" r="5" fill="%s"/><path d="M14,30 h14 a5,5 0 0 0 0,-10 a7,7 0 0 0 -13,2 a4,4 0 0 0 -1,8 z" fill="#fff" stroke="%s" stroke-width="2.2"/>' % (c, c)
    else: o += '<rect x="14" y="9" width="12" height="22" rx="3" fill="none" stroke="%s" stroke-width="2.5"/><circle cx="20" cy="27" r="1.6" fill="%s"/>' % (c, c)
    return '<svg class="aic" viewBox="0 0 40 40" aria-hidden="true">%s</svg>' % o

def art(w):
    m = re.match(r"^(el|los|un|unos|la|las|una|unas)\s+(.*)$", w)
    if not m: return w
    g = "m" if m.group(1) in ("el", "los", "un", "unos") else "f"
    return '<span class="art %s">%s</span> %s' % (g, m.group(1), m.group(2))

def red_html(e):
    o = '<div class="red"><div class="rc" style="border-color:%s">%s<b>%s</b><span class="small muted">%s</span></div>' % (ACOL[e["area"]], area_svg(e["area"]), e["titulo"], e["lugar"])
    for i, (nom, ws) in enumerate(e["ramas"]):
        o += '<div class="rb b%d"><h4>%s</h4><ul>%s</ul></div>' % (i + 1, nom, "".join("<li>%s</li>" % (("<i>%s</i>" % w) if re.search(r"[.?!]$", w) else art(w)) for w in ws))
    return o + '</div>'

def tools():
    T = [("escena", "La escena", "¿Dónde vive esta palabra?",
          "Guarda cada palabra en un sitio (la estación, el teatro, la oficina) y en una de sus cuatro ramas: quién, qué cosas, qué haces, qué dices. Para recordarla, vuelve a la escena."),
         ("trio", "El trío", "¿Con qué palabras se confunde?",
          "En la tarea 1 de la auditiva, las tres viñetas son de la misma familia (tres transportes, tres espectáculos) y se oyen las tres. Aprende las palabras de tres en tres, con las frases que descartan."),
         ("pareja", "La pareja", "¿Cómo se dice con otras palabras?",
          "En la lectura y la auditiva, la respuesta buena dice lo mismo que el texto con otras palabras: desayuno incluido = no pagas aparte el desayuno; gratis = no se paga. Aprende las parejas.")]
    return '<div class="cams">' + "".join('<div class="cam">%s<h3>%s</h3><p class="qf">%s</p><p>%s</p></div>' % (tool_svg(k), n, q, d) for k, n, q, d in T) + '</div>'

DONDE = [
    ("Auditiva · tarea 1", "Seis conversaciones con tres viñetas cada una. Las tres cosas se oyen; dos se descartan. Si conoces el trío, oyes el descarte.", "escucha"),
    ("Lectura · tareas 2 y 3", "Anuncios, carteles y textos de hoteles, cursos, ofertas de trabajo, espectáculos... La opción buena casi nunca repite la palabra del texto: la dice de otra forma.", "otra"),
    ("Auditiva · tareas 2 y 4", "Radio y mensajes: «la primera clase es gratis» → «no se paga la primera clase». Otra vez, la pareja.", "otra"),
    ("Escritura", "La escala oficial mira si tu vocabulario es «suficiente» y si escoges bien las palabras. Una palabra precisa (el andén, la matrícula) sube el uso de la lengua; «cosa» tres veces, no.", "ahora"),
    ("Oral · tarea 2", "La foto: nombrar a las personas, la ropa, el lugar y los objetos. Cuantas más palabras tienes, más tiempo hablas sin pararte.", "ahora"),
]
def donde():
    return "".join('<div class="box"><span class="chip">%s</span><p style="margin:6px 0 0">%s</p></div>' % (c, d) for c, d, _ in DONDE)

REGLAS = [
    "Apunta las palabras <b>por escenas</b>, no en una lista: «en la estación», «en la taquilla del teatro».",
    "Los nombres, siempre <b>con su artículo</b>: <i>el</i> andén, <i>la</i> taquilla (así aciertas la concordancia, R04).",
    "Cada palabra, <b>con su verbo</b>: jugar al tenis, tocar la guitarra, facturar la maleta, aprobar un examen.",
    "Escribe <b>una frase tuya</b> con la palabra: tu trabajo, tus viajes, tu fin de semana. Se recuerda mucho mejor.",
    "Repasa <b>tapando</b>: mira la escena, tapa las palabras e intenta decirlas. Lo que no sale, vuelve a tu cuaderno.",
]

def descarte_tab():
    return '<table class="t"><tr><th>Si oyes...</th><th>Qué pasa</th><th>Ejemplo</th></tr>' + "".join(
        '<tr><td><b>%s</b></td><td>%s</td><td><i>%s</i></td></tr>' % r for r in B.DESCARTE) + '</table>'

def trios_all():
    o = ""
    for a in B.ORDEN_AREAS:
        o += '<div class="box"><h4>%s%s</h4><div class="trios">' % (area_svg(a), AREAS[a]["n"])
        for nom, tres in B.TRIOS[a]:
            o += '<div class="trio"><span class="small muted">%s</span><div>%s</div></div>' % (nom, " · ".join(art(w) for w in tres))
        o += '</div></div>'
    return o

def parejas_all():
    o = '<table class="t"><tr><th>Área</th><th>El texto dice...</th><th>La pregunta dice...</th></tr>'
    for a in B.ORDEN_AREAS:
        for t, p in B.PAREJAS[a]: o += '<tr><td class="small">%s</td><td>%s</td><td>%s</td></tr>' % (AREAS[a]["n"], t, p)
    return o + '</table>'

CSS_R = CSS + r"""
:root{--b1:#1D5FA8;--b1s:#E2ECF8;--b2:#2F7D4F;--b2s:#E3F1E8;--b3:#9A6412;--b3s:#FBF0DA;--b4:#C2451E;--b4s:#FCE6DC;--am:#0F7C7C;--af:#6B46C1}
.k{border-radius:4px;padding:0 3px 1px;border-bottom:3px solid;line-height:1.9}
.k.b1{background:var(--b1s);border-color:var(--b1)}.k.b2{background:var(--b2s);border-color:var(--b2)}.k.b3{background:var(--b3s);border-color:var(--b3)}.k.b4{background:var(--b4s);border-color:var(--b4)}
.art{font-weight:700}.art.m{color:var(--am)}.art.f{color:var(--af)}
.cams{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:18px 0}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px 14px;border-top:6px solid var(--coral)}
.cam h3{margin:4px 0 2px}.cam p{margin:0;font-size:.95rem}.cam p.qf{color:var(--muted);font-style:italic;margin-bottom:6px}
svg.ic{width:100%;max-width:200px;height:auto;display:block}
svg.aic{width:26px;height:26px;vertical-align:-7px;margin-right:6px;flex:0 0 auto}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.box h4{margin:0 0 6px;display:flex;align-items:center}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer;display:inline-flex;align-items:center}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pill.on svg.aic circle{fill:#fff}
.pill .dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px}
.pill.okd{border-color:var(--ok)}.pill.nod{border-color:var(--bad)}
.red{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0}
.red .rc{grid-column:1/-1;display:flex;align-items:center;gap:8px;flex-wrap:wrap;background:#fff;border:3px solid;border-radius:999px;padding:8px 16px;justify-self:center}
.red .rc b{font-family:Georgia,serif;font-size:1.1rem}
.rb{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 14px;border-left:6px solid}
.rb.b1{border-left-color:var(--b1)}.rb.b2{border-left-color:var(--b2)}.rb.b3{border-left-color:var(--b3)}.rb.b4{border-left-color:var(--b4)}
.rb h4{margin:0 0 4px;font-size:.95rem}.rb.b1 h4{color:var(--b1)}.rb.b2 h4{color:var(--b2)}.rb.b3 h4{color:var(--b3)}.rb.b4 h4{color:var(--b4)}
.rb ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px 12px;font-size:.95rem}
.scene{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;line-height:2.05}
.scene input{font:inherit;font-size:.95rem;border:0;border-bottom:2px solid var(--ink);background:var(--paper);padding:0 4px;border-radius:4px 4px 0 0;max-width:100%}
.scene input.ok{background:var(--ok-soft);border-color:var(--ok);color:var(--ok);font-weight:600}
.scene input.no{background:var(--bad-soft);border-color:var(--bad)}
.lanes{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.lanes button{font:inherit;font-weight:700;border:3px solid var(--line);background:#fff;border-radius:10px;padding:10px 12px;cursor:pointer}
.lanes button.on{border-color:var(--coral);background:var(--coral-soft)}
.legend{display:flex;flex-wrap:wrap;gap:12px;font-size:.88rem;margin:8px 0}
.trios{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px}
.trio{background:var(--paper);border-radius:8px;padding:6px 10px}
.miss{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}.miss span{background:var(--amb-soft);border-radius:999px;padding:2px 10px;font-size:.88rem}
.cuad{background:#fff;border:2px dashed var(--coral);border-radius:12px;padding:14px 16px;margin:16px 0}
.cuad .f{display:grid;grid-template-columns:1fr 2fr auto;gap:8px;align-items:end}
.cuad input,.cuad select{font:inherit;font-size:.95rem;border:1.5px solid #CFC6BB;border-radius:8px;padding:6px 10px;width:100%;background:#fff}
.cuad ul{list-style:none;padding:0;margin:10px 0 0}.cuad li{padding:5px 0;border-bottom:1px solid var(--line);display:flex;gap:8px;align-items:baseline;justify-content:space-between}
.cuad li button{border:0;background:none;color:var(--bad);cursor:pointer;font:inherit;font-size:.85rem}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.ca{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0}
.ca .qq{font-family:Georgia,serif;font-size:1.15rem;font-weight:700;margin:6px 0 10px}
.vin{position:relative;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.vin img{display:block;width:100%;height:auto;aspect-ratio:3/1;object-fit:cover;background:#EEE8E1}
.vin .lb{position:absolute;top:0;left:0;right:0;display:grid;grid-template-columns:repeat(3,1fr)}
.vin .lb span{font-weight:700;font-size:.85rem;padding:2px 10px;color:var(--muted)}
.vin.noimg img,.vin.noimg .lb{display:none}
.vin .noi{display:none;padding:10px 14px;font-size:.9rem;color:var(--muted)}.vin.noimg .noi{display:block}
.abc{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:10px 0}
.abc button{font:inherit;font-weight:700;border:2px solid var(--line);background:#fff;border-radius:10px;padding:9px 8px;cursor:pointer;text-align:center}
.abc button:disabled{cursor:default}
.abc button.good{border-color:var(--ok);background:var(--ok-soft)}.abc button.bad{border-color:var(--bad);background:var(--bad-soft)}
.abc button small{display:block;font-weight:500;font-size:.85rem}
.play{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:6px 0}
.trans{background:var(--paper);border-radius:8px;padding:10px 14px;margin-top:8px;line-height:1.85;font-size:.95rem}
.trans p{margin:2px 0}.trans .v{background:var(--ok-soft);border-bottom:3px solid var(--ok);border-radius:3px;padding:0 3px}
.trans .x{background:var(--bad-soft);border-bottom:3px solid var(--bad);border-radius:3px;padding:0 3px;text-decoration:line-through;text-decoration-color:rgba(179,38,30,.5)}
.flip{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;margin:10px 0}
.flip button{font:inherit;text-align:left;border:2px solid var(--line);background:#fff;border-radius:12px;padding:12px 14px;cursor:pointer;min-height:84px}
.flip button.on{border-color:var(--ok);background:var(--ok-soft)}
.flip button .p{display:block;font-size:.85rem;color:var(--muted);margin-bottom:4px}
.ad{border:2px solid var(--ink);border-radius:4px;padding:12px 16px;background:#fff;margin:8px 0 12px}
.ad b.h{display:block;font-size:.82rem;letter-spacing:.05em;margin-bottom:4px}
.qz{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0}
.qz .cnt{font-size:.85rem;color:var(--muted)}
.qz .qq{font-size:1.05rem;margin:6px 0 10px}
.qz .ops{display:grid;gap:8px}
.qz .ops.bm{grid-template-columns:1fr 1fr}.qz .ops.g4{grid-template-columns:1fr 1fr}
.qz .ops button{font:inherit;text-align:left;font-weight:500;border:2px solid var(--line);background:#fff;border-radius:10px;padding:9px 12px;cursor:pointer}
.qz .ops.bm button{text-align:center;font-weight:600}
.qz .ops button:disabled{cursor:default}
.qz .ops button.good{border-color:var(--ok);background:var(--ok-soft)}
.qz .ops button.bad{border-color:var(--bad);background:var(--bad-soft)}
.blank{display:inline-block;min-width:64px;border-bottom:2px solid var(--ink);text-align:center}
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
.vchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px;background:var(--paper);color:var(--muted);border:1px solid var(--line)}
textarea.wr{width:100%;min-height:220px;font:inherit;font-size:1.02rem;line-height:1.7;border:1.5px solid #CFC6BB;border-radius:8px;padding:12px 14px;background:#fff}
.rv{list-style:none;padding:0;margin:8px 0}
.rv li{border-radius:8px;padding:8px 12px;margin:6px 0;font-size:.95rem}
.rv li.r{background:var(--bad-soft)}.rv li.a{background:var(--amb-soft)}.rv li.g{background:var(--ok-soft)}
.rv mark{background:#FFE58A;border-radius:3px;padding:0 2px}
.cnts{display:grid;gap:6px;margin:8px 0}.cnts div{font-size:.92rem;background:#fff;border:1px solid var(--line);border-radius:8px;padding:6px 10px}
.check{list-style:none;padding:0;margin:8px 0}.check li{padding:5px 0}.check label{cursor:pointer}
.ocard{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin-top:12px}
.ofoto{background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden;margin:8px 0}
.ofoto img{display:block;width:100%;height:auto;max-height:420px;object-fit:contain;background:#EEE8E1}
.ofoto .d{display:none;padding:10px 14px;font-style:italic;font-size:.92rem}.ofoto.noimg img{display:none}.ofoto.noimg .d{display:block}
.clock{font-family:Georgia,serif;font-size:1.6rem;font-weight:700;font-variant-numeric:tabular-nums}
.tbar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:8px 0}
.tbar i{display:block;height:100%;background:var(--coral);width:0;transition:width .25s linear}
.esc{font-family:Georgia,serif;font-size:1.2rem;font-weight:700;margin:8px 0}
.wchecks{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:4px 10px;font-size:.95rem}
.wchecks label{cursor:pointer}
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
@media (max-width:700px){.red{grid-template-columns:1fr}.red .rc{border-radius:12px;justify-self:stretch}.lanes{grid-template-columns:1fr}.qz .ops.g4{grid-template-columns:1fr}.cuad .f{grid-template-columns:1fr}table.t{font-size:.88rem}table.t td,table.t th{padding:6px 5px}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:12.5px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.rb,.red{break-inside:avoid}}
"""

STEPS = [("idea", "La idea"), ("escenas", "Las escenas"), ("escucha", "Escucha y elige"), ("otra", "Dilo de otra forma"),
         ("practica", "Practica"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]
LEG = '<div class="legend">' + "".join('<span><span class="k b%d">rama %d</span></span>' % (i, i) for i in range(1, 5)) + \
      '<span><span class="art m">el</span> / <span class="art f">la</span>: el artículo te dice si es masculino o femenino</span></div>'

V_IDEA = """
<h2>Las palabras viven en escenas</h2>
<p class="lead">Una lista de cien palabras se olvida en una semana. Una palabra que has visto en su sitio (en la estación, en la taquilla del teatro, en una entrevista de trabajo), con su verbo y con la palabra que se confunde con ella, se queda. Esta ficha trabaja las palabras de fuera de casa con las mismas tres herramientas de la R14a.</p>
__TOOLS__
<h3>Las áreas de esta ficha</h3>
<p>Las cinco primeras son de frecuencia <b>alta</b> en el DELE A2: salen casi en todos los exámenes. La última es un rincón corto de frecuencia <b>media</b>: los recados, el móvil y las fiestas. Las palabras de la casa y del día a día (personas, casa, comida, compras, salud) están en la ficha R14a.</p>
<div class="pills">__AREAS__</div>
<h3>Dónde salen en el examen</h3>
__DONDE__
<h3>Tu cuaderno de escenas: cinco reglas</h3>
<ol>__REGLAS__</ol>
<div class="tip">En la pestaña <b>Las escenas</b> tienes un cuaderno: apunta allí tus palabras nuevas, con su frase. Se queda guardado en este navegador y se envía con <b>Copiar</b> a tu profesora.</div>
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="escenas">Siguiente: las escenas</button></div>
"""

V_ESC = """
<h2>Las escenas</h2>
<p class="lead">Elige un área y una escena. Primero mira la red y lee la escena; después pulsa <b>Tapa y recuerda</b>: las palabras desaparecen y tienes que escribirlas solo con la primera letra.</p>
<div class="pills" id="arsel"></div>
<div class="pills" id="essel"></div>
<div id="esbox"></div>
<div class="cuad" id="cuad"></div>
<div class="row"><button class="btn cta" data-go="escucha">Siguiente: escucha y elige</button></div>
"""

V_ESCU = """
<h2>Escucha y elige</h2>
<p class="lead">Así es la tarea 1 de la auditiva: una conversación corta, una pregunta y tres viñetas. <b>Las tres cosas se oyen</b>, pero dos se descartan. Escucha hasta el final antes de marcar: la respuesta suele estar en la última frase.</p>
<h3>Las frases que descartan</h3>
__DESCARTE__
<h3>Practica</h3>
<p class="muted small">Como en el examen, puedes escuchar cada conversación <b>dos veces</b> antes de contestar. Después, la transcripción te enseña qué se dice y qué se descarta.</p>
<div class="row" style="margin:8px 0"><button class="btn sm" data-act="caall">Las doce, en orden</button><button class="btn sm" data-act="carnd">Una ronda de seis al azar</button></div>
<div class="pills" id="casel"></div>
<div id="cabox" aria-live="polite"></div>
<details><summary>Los tríos de cada área (las palabras que el examen pone juntas)</summary>__TRIOS__</details>
<div class="row"><button class="btn cta" data-go="otra">Siguiente: dilo de otra forma</button></div>
"""

V_OTRA = """
<h2>Dilo de otra forma</h2>
<p class="lead">En la lectura (tareas 2 y 3) y en la radio o los mensajes de la auditiva (tareas 2 y 4), la opción buena casi nunca repite la palabra del texto: la dice de otra forma. La opción que repite las mismas palabras suele ser la trampa.</p>
<div class="pills" id="otsel">
 <button class="pill on" data-act="ot" data-k="cards">1. Las parejas</button>
 <button class="pill" data-act="ot" data-k="pa">2. Une la pareja</button>
 <button class="pill" data-act="ot" data-k="an">3. Anuncios del examen</button>
</div>
<p class="muted small" id="otinfo"></p>
<div id="otbox"></div>
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACT = """
<h2>Practica</h2>
<p class="lead">Cuatro ejercicios. Cada respuesta se corrige en el momento, con la explicación.</p>
<div class="pills" id="exsel">
 <button class="pill on" data-act="ex" data-k="p1">1. ¿Qué sobra?</button>
 <button class="pill" data-act="ex" data-k="p2">2. ¿Qué palabra va con...?</button>
 <button class="pill" data-act="ex" data-k="e2">3. Textos del examen</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Usa las palabras en una tarea del examen: escribe un texto o di en voz alta todo lo que ves en una foto.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="o">Oral: la escena en un minuto</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu texto y pulsa <b>Revisar mis palabras</b>: la página cuenta las palabras de cada área que usas y te avisa de las confusiones típicas. No corrige el texto entero: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="ato" hidden>
 <p>Como en la tarea 2 de la oral: mira la foto y, durante <b>un minuto</b>, di en voz alta todas las palabras que puedas, en frases cortas (<i>Hay un olivo. La abuela lleva un vestido de flores...</i>). La página te va diciendo de qué hablar. Al final, marca las palabras que has dicho.</p>
 <div id="obox"></div>
</div>
<div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button></div>
"""

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan a mejorarlo. Al final, copia todo (también tus textos, tu cuaderno y tus resultados) y envíamelo.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué parte te ha ayudado más?</label>
 <div class="chips" role="group" aria-labelledby="o1l">
  <label><input type="radio" name="o1" value="Las escenas y tapa y recuerda">Las escenas y «tapa y recuerda»</label>
  <label><input type="radio" name="o1" value="Escucha y elige">Escucha y elige</label>
  <label><input type="radio" name="o1" value="Dilo de otra forma">Dilo de otra forma</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tú">Ahora tú</label>
  <label><input type="radio" name="o1" value="Mi cuaderno">Mi cuaderno</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué área te cuesta más?</label>
 <div class="chips" role="group" aria-labelledby="o2l">
  <label><input type="radio" name="o2" value="Los viajes">Los viajes</label>
  <label><input type="radio" name="o2" value="El ocio">El ocio</label>
  <label><input type="radio" name="o2" value="Los estudios">Los estudios</label>
  <label><input type="radio" name="o2" value="El trabajo">El trabajo</label>
  <label><input type="radio" name="o2" value="El tiempo">El tiempo</label>
  <label><input type="radio" name="o2" value="Servicios, móvil y fiestas">Servicios, móvil y fiestas</label>
 </div>
 <label class="q" id="o3l">3. ¿Te ayuda aprender las palabras por escenas y no en listas?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con el vocabulario de estas áreas? (1 = nada, 10 = total)</label>
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
    o = '<h2>Vocabulario en escenas (2) · resumen</h2>' + tools()
    o += '<h3>Tu cuaderno de escenas</h3><ol>' + "".join("<li>%s</li>" % r for r in REGLAS) + '</ol>'
    for e in B.ESCENAS: o += red_html(e)
    o += '<h3>Las frases que descartan</h3>' + descarte_tab()
    o += '<h3>Los tríos</h3>' + trios_all()
    o += '<h3>Las parejas</h3>' + parejas_all()
    return o

AREAPILLS = "".join('<span class="pill" style="cursor:default">%s%s</span>' % (area_svg(a), AREAS[a]["n"]) for a in B.ORDEN_AREAS)
views = {
    "idea": V_IDEA.replace("__TOOLS__", tools()).replace("__AREAS__", AREAPILLS).replace("__DONDE__", donde()).replace("__REGLAS__", "".join("<li>%s</li>" % r for r in REGLAS)),
    "escenas": V_ESC, "escucha": V_ESCU.replace("__DESCARTE__", descarte_tab()).replace("__TRIOS__", trios_all()),
    "otra": V_OTRA, "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R14b</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
""".replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

# ------------------------------------------------------------------ DATOS PARA EL SCRIPT
def mk_scene(s): return MARK.sub(lambda m: '<span class="k b%s" title="%s">%s</span>' % (m.group(1), m.group(2).partition("=")[2] or m.group(2), m.group(2).split("=")[0]), s)
def mk_trans(s): return AMARK.sub(lambda m: '<span class="%s">%s</span>' % (m.group(1), m.group(2)), TAG.sub("", s))
def tap_parts(s):
    """El texto de la escena partido en trozos: texto normal y huecos (forma, lema, rama)."""
    out, pos = [], 0
    for m in MARK.finditer(s):
        out.append(s[pos:m.start()]); form, _, lema = m.group(2).partition("=")
        out.append({"f": form, "l": lema or form, "b": int(m.group(1))}); pos = m.end()
    out.append(s[pos:]); return out
PA = []
for a in B.ORDEN_AREAS:
    ps = B.PAREJAS[a]
    for i, (t, p) in enumerate(ps):
        PA.append({"q": "El texto dice: «%s» ¿Qué dice lo mismo?" % t, "o": [p, ps[(i + 1) % 5][1], ps[(i + 2) % 5][1]], "area": a,
                   "why": "«%s» = «%s»." % (t, p)})
DATA = {
    "key": STORAGE, "title": TITLE,
    "steps": [{"id": k, "label": l} for k, l in STEPS],
    "areas": {a: AREAS[a]["n"] for a in B.ORDEN_AREAS}, "order": B.ORDEN_AREAS, "acol": ACOL,
    "aic": {a: area_svg(a) for a in B.ORDEN_AREAS},
    "escenas": [{"id": e["id"], "area": e["area"], "titulo": e["titulo"], "lugar": e["lugar"], "red": red_html(e),
                 "html": mk_scene(e["texto"]), "parts": tap_parts(e["texto"]),
                 "trios": B.TRIOS[e["area"]]} for e in B.ESCENAS],
    "ca": [{"area": it["area"], "q": it["q"], "o": it["o"], "ok": it["ok"], "pres": it["pres"], "why": it["why"],
            "img": WP + it["img"] + ".jpg", "au": WP + audio_name(i) + ".m4a",
            "lines": [[l[0], mk_trans(l[2])] for l in it["lines"]]} for i, it in enumerate(B.CA1)],
    "parejas": {a: B.PAREJAS[a] for a in B.ORDEN_AREAS},
    "qz": {
        "p1": {"items": B.P_SOBRA, "n": 8, "name": "¿Qué sobra?", "info": "Cuatro palabras de una escena. Una no es de ese sitio: ¿cuál?", "pre": "Escena: "},
        "p2": {"items": B.P_VERBO, "n": 8, "name": "¿Qué palabra va con...?", "info": "Las palabras viajan con su verbo (o su preposición): pedir cita, poner la mesa, pagar en efectivo."},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Confusiones típicas de los exámenes. ¿La frase está bien o hay una palabra que falla?"},
        "pa": {"items": PA, "n": 8, "name": "Une la pareja", "info": "Lo que dice el texto y lo que dice la pregunta: ¿cuál es la misma idea?"},
        "an": {"items": [{"q": it["q"], "o": it["o"], "why": it["why"], "area": it["area"], "ad": [it["titulo"], it["texto"]], "lit": it["lit"]} for it in B.ANUNCIOS],
               "n": 6, "name": "Anuncios del examen", "info": "Como la tarea 2 de la lectura: lee el anuncio y elige. Cuidado con la opción que repite las mismas palabras."},
    },
    "motivos": {k: {"a": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "textos": B.TEXTOS,
    "laminas": B.LAMINAS, "cuenta": CUENTA, "detector": B.DETECTOR,
    "oral": [{"id": o["id"], "titulo": o["titulo"], "desc": o["desc"], "img": WP_T2 + "M4T2_foto%d.jpg" % o["id"], "grupos": o["grupos"]} for o in B.ORAL],
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function norm(s){ return String(s).normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
function blank(){ return {cur:'idea', seen:{}, ar:D.order[0], es:D.escenas[0].id, mode:'leer', tap:{}, miss:{}, cuad:[],
  caseq:range(D.ca.length), cai:0, ca:{}, plays:{}, ot:'cards', flip:{}, ex:'p1', etext:D.textos[0].id,
  qz:{}, qlog:{}, cz:{}, at:'w', w:{}, wchk:{}, wrev:{}, lam:D.laminas[0].id, of:D.oral[0].id, ro:null, olog:[],
  o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }

/* ---------------- navegacion ---------------- */
function stepDone(id){
 if(id==='escenas') return Object.keys(S.tap).length>0;
 if(id==='escucha') return Object.keys(S.ca).length>0;
 if(id==='otra') return !!(S.qlog.pa||S.qlog.an);
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
 stopTimer(); stopAudio(); nav(); if(id==='ahora') renderAt(); if(id==='escucha') renderCa(); window.scrollTo(0,0);
}

/* ---------------- las escenas ---------------- */
function escena(){ return D.escenas.filter(function(e){ return e.id===S.es; })[0]; }
function renderEsc(){
 var o=''; D.order.forEach(function(a){ o+='<button class="pill'+(S.ar===a?' on':'')+'" data-act="ar" data-a="'+a+'">'+D.aic[a]+esc(D.areas[a])+'</button>'; });
 $('arsel').innerHTML=o;
 o=''; D.escenas.forEach(function(e){ if(e.area!==S.ar) return; var t=S.tap[e.id]; o+='<button class="pill'+(S.es===e.id?' on':'')+'" data-act="es" data-id="'+e.id+'">'+esc(e.titulo)+(t&&t.done?' · '+t.first+'/'+t.tot:'')+'</button>'; });
 $('essel').innerHTML=o;
 var e=escena(), h=e.red;
 h+='<div class="lanes" role="group"><button data-act="mode" data-k="leer" class="'+(S.mode==='leer'?'on':'')+'" aria-pressed="'+(S.mode==='leer')+'">Leer la escena</button><button data-act="mode" data-k="tapa" class="'+(S.mode==='tapa'?'on':'')+'" aria-pressed="'+(S.mode==='tapa')+'">Tapa y recuerda</button></div>';
 if(S.mode==='leer'){
  h+='<p class="small muted" style="margin:4px 0"><b>'+esc(e.lugar)+'.</b> Cada palabra tiene el color de su rama.</p><div class="scene">'+e.html+'</div>';
 } else {
  var t=S.tap[e.id]||{};
  h+='<p class="small muted" style="margin:4px 0">Escribe cada palabra (tienes la primera letra). Las tildes cuentan, pero si solo falla la tilde, te lo decimos.</p><div class="scene" id="tapbox">';
  var n=0;
  e.parts.forEach(function(p){
   if(typeof p==='string'){ h+=p; return; }
   var k=e.id+'-'+n, st=(t.g||{})[n], w=Math.max(4,p.f.length+1);
   h+='<input type="text" data-tap="'+n+'" aria-label="Palabra '+(n+1)+' (empieza por '+esc(p.f.charAt(0))+')" placeholder="'+esc(p.f.charAt(0))+'…" style="width:'+w+'ch" autocomplete="off" autocapitalize="off" spellcheck="false"'+(st?' value="'+esc(st.v)+'" class="'+(st.ok?'ok':'no')+'"':'')+(st&&st.ok?' readonly':'')+'>';
   n++;
  });
  h+='</div><div class="row"><button class="btn cta" data-act="tapchk">Comprobar</button><button class="btn sm" data-act="tapshow">Ver las palabras</button><button class="btn sm" data-act="tapreset">Empezar otra vez</button></div><div id="tapfb" aria-live="polite">'+tapFb(e)+'</div>';
 }
 h+='<h3>Los tríos de esta área</h3><div class="trios">'+e.trios.map(function(tr){ return '<div class="trio"><span class="small muted">'+esc(tr[0])+'</span><div>'+tr[1].map(esc).join(' · ')+'</div></div>'; }).join('')+'</div>';
 $('esbox').innerHTML=h;
 renderCuad();
}
function tapFb(e){
 var t=S.tap[e.id]; if(!t||!t.g) return '';
 var tot=e.parts.filter(function(p){ return typeof p!=='string'; }).length, ok=0, notes=[];
 Object.keys(t.g).forEach(function(k){ if(t.g[k].ok) ok++; if(t.g[k].til) notes.push(t.g[k].v); });
 var o='<p class="small"><b>'+ok+' de '+tot+'</b> palabras'+(t.done?' · a la primera: <b>'+t.first+' de '+tot+'</b>':'')+'</p>';
 if(notes.length) o+='<p class="small">Ojo con la tilde: '+notes.map(esc).join(', ')+'.</p>';
 var ms=Object.keys(S.miss).filter(function(k){ return S.miss[k].a===e.area; });
 if(ms.length) o+='<p class="small" style="margin-bottom:0"><b>Las palabras que se te resisten</b> (apúntalas en tu cuaderno):</p><div class="miss">'+ms.map(function(k){ return '<span>'+esc(k)+'</span>'; }).join('')+'</div>';
 return o;
}
function tapCheck(showAll){
 var e=escena(), t=S.tap[e.id]||(S.tap[e.id]={g:{}, tot:0, first:0, done:false}), hs=e.parts.filter(function(p){ return typeof p!=='string'; });
 t.tot=hs.length;
 var ins=document.querySelectorAll('#tapbox input[data-tap]');
 for(var i=0;i<ins.length;i++){
  var n=+ins[i].getAttribute('data-tap'), p=hs[n], v=ins[i].value.trim(), prev=t.g[n];
  if(showAll && !(prev&&prev.ok)){ t.g[n]={v:p.f, ok:true, shown:true}; if(!prev){ S.miss[p.l]={a:e.area}; } continue; }
  if(!v || (prev&&prev.ok)) continue;
  var good=v.toLowerCase()===p.f.toLowerCase(), close=!good && norm(v)===norm(p.f);
  var first=!prev;
  t.g[n]={v:v, ok:good||close, til:close};
  if(first && (good||close)) t.first=(t.first||0)+1;
  if(first && !(good||close)) S.miss[p.l]={a:e.area};
 }
 t.done=hs.every(function(p,i){ return t.g[i]&&t.g[i].ok; });
 save(); renderEsc(); nav();
}
function renderCuad(){
 var o='<h3 style="margin-top:0">Mi cuaderno de escenas</h3><p class="small muted" style="margin:0 0 8px">Apunta aquí las palabras nuevas de esta área: la palabra (con su artículo) y una frase tuya.</p>';
 o+='<div class="f"><label class="small"><b>Palabra</b><input type="text" id="cw" placeholder="la taquilla"></label><label class="small"><b>Mi frase</b><input type="text" id="cf" placeholder="Compro las entradas del cine en la taquilla."></label><button class="btn sm" data-act="cadd">Añadir</button></div>';
 var mine=S.cuad.map(function(c,i){ return [c,i]; }).filter(function(x){ return x[0].a===S.ar; });
 if(mine.length) o+='<ul>'+mine.map(function(x){ return '<li><span><b>'+esc(x[0].w)+'</b>'+(x[0].f?' — <i>'+esc(x[0].f)+'</i>':'')+'</span><button data-act="cdel" data-i="'+x[1]+'" aria-label="Borrar">borrar</button></li>'; }).join('')+'</ul>';
 else o+='<p class="small muted" style="margin:8px 0 0">Todavía no tienes palabras en esta área.</p>';
 if(S.cuad.length) o+='<p class="small muted" style="margin:8px 0 0">En total: '+S.cuad.length+' palabras en tu cuaderno.</p>';
 $('cuad').innerHTML=o;
}

/* ---------------- escucha y elige ---------------- */
var AU=null;
function stopAudio(){ if(AU){ try{ AU.pause(); }catch(e){} AU=null; } }
function renderCa(){
 var o=''; S.caseq.forEach(function(idx,pos){ var r=S.ca[idx]; o+='<button class="pill'+(S.cai===pos?' on':'')+(r?(r.ok?' okd':' nod'):'')+'" data-act="cago" data-p="'+pos+'"><span class="dot" style="background:'+D.acol[D.ca[idx].area]+'"></span>'+(pos+1)+'</button>'; });
 $('casel').innerHTML=o;
 var box=$('cabox');
 if(S.cai>=S.caseq.length){
  var ok=S.caseq.filter(function(i){ return S.ca[i]&&S.ca[i].ok; }).length, N=S.caseq.length;
  box.innerHTML='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+(ok>=N-1?'¡Muy bien! Oyes los descartes.':'Mira otra vez las frases que descartan y repite las que has fallado.')+'</p><div class="row"><button class="btn cta" data-act="carnd">Otra ronda de seis</button></div></div>';
  return;
 }
 var idx=S.caseq[S.cai], it=D.ca[idx], r=S.ca[idx], pl=S.plays[idx]||0;
 var h='<div class="ca"><span class="chip">'+D.aic[it.area].replace('class="aic"','class="aic" style="width:18px;height:18px;vertical-align:-4px"')+esc(D.areas[it.area])+'</span><span class="small muted">Conversación '+(S.cai+1)+' de '+S.caseq.length+'</span>';
 h+='<div class="qq">'+esc(it.q)+'</div>';
 h+='<div class="vin" id="vin"><img src="'+it.img+'" alt="Tres viñetas: A, '+esc(it.o[0])+'; B, '+esc(it.o[1])+'; C, '+esc(it.o[2])+'" loading="lazy" onerror="this.parentNode.classList.add(\'noimg\')"><div class="lb" aria-hidden="true"><span>A</span><span>B</span><span>C</span></div><div class="noi">Las viñetas todavía no están: mira las tres opciones en los botones.</div></div>';
 h+='<div class="play"><button class="btn'+(r?'':' cta')+'" data-act="caplay" id="caplay"'+(!r&&pl>=2?' disabled':'')+'>▶ Escuchar</button><span class="small muted" id="caplays">'+(r?'Ya has contestado: puedes escuchar las veces que quieras.':(pl>=2?'Ya la has escuchado dos veces: elige.':'Te quedan '+(2-pl)+' escucha'+(2-pl===1?'':'s')+'.'))+'</span></div>';
 h+='<div id="caerr"></div>';
 h+='<div class="abc" role="group" id="abc">';
 it.o.forEach(function(op,i){
  var cls=''; if(r){ if(i===it.ok) cls='good'; else if(i===r.pick) cls='bad'; }
  h+='<button type="button" data-act="caans" data-o="'+i+'" class="'+cls+'"'+(r?' disabled':'')+'>'+'ABC'.charAt(i)+'<small class="ot">'+esc(op)+'</small></button>';
 });
 h+='</div>';
 if(r){
  h+='<div class="fb '+(r.ok?'good':'bad')+'" role="status"><b>'+(r.ok?'¡Bien!':'No.')+'</b> '+it.why+'</div>';
  h+='<div class="trans"><p class="small muted" style="margin:0 0 4px"><i>'+esc(it.pres)+'</i> · <span class="v">lo que es</span> · <span class="x">lo que se descarta</span></p>'+it.lines.map(function(l){ return '<p><b>'+esc(l[0])+':</b> '+l[1]+'</p>'; }).join('')+'</div>';
 } else if(S.readT===idx){
  h+='<div class="trans"><p class="small muted" style="margin:0 0 4px"><i>'+esc(it.pres)+'</i></p>'+it.lines.map(function(l){ return '<p><b>'+esc(l[0])+':</b> '+strip(l[1])+'</p>'; }).join('')+'</div>';
 }
 h+='<div class="row"'+(r?'':' hidden')+'><button class="btn cta" data-act="canext">'+(S.cai+1<S.caseq.length?'Siguiente':'Ver el resultado')+'</button></div></div>';
 box.innerHTML=h;
 var vin=$('vin'); if(vin && vin.classList.contains('noimg')){}
 var img=vin&&vin.querySelector('img'); if(img){ img.addEventListener('error',function(){ $('abc').classList.add('txt'); }); }
}
function caPlay(){
 var idx=S.caseq[S.cai], it=D.ca[idx], r=S.ca[idx];
 if(!r && (S.plays[idx]||0)>=2) return;
 stopAudio();
 var a=new Audio(it.au); AU=a;
 var btn=$('caplay'); if(btn){ btn.disabled=true; btn.textContent='… Escuchando'; }
 a.addEventListener('ended',function(){ if(AU!==a) return; AU=null; if(!S.ca[idx]){ S.plays[idx]=(S.plays[idx]||0)+1; save(); } renderCa(); });
 a.addEventListener('error',function(){ if(AU!==a) return; AU=null; audioFail(idx); });
 var p=a.play(); if(p && p.catch) p.catch(function(){ if(AU===a){ AU=null; audioFail(idx); } });
}
function audioFail(idx){
 var btn=$('caplay'); if(btn){ btn.disabled=false; btn.textContent='▶ Escuchar'; }
 var box=$('caerr'); if(!box) return;
 box.innerHTML='<div class="tip">El audio todavía no está disponible. Puedes <button class="btn sm" data-act="caread">leer la conversación</button> y contestar.</div>';
}
function caAnswer(pick){
 var idx=S.caseq[S.cai], it=D.ca[idx]; if(S.ca[idx]) return;
 stopAudio(); S.ca[idx]={pick:pick, ok:pick===it.ok}; save(); renderCa(); nav();
 var f=$('cabox').querySelector('.fb'); if(f&&f.scrollIntoView) f.scrollIntoView({block:'nearest'});
}

/* ---------------- motor de opcion multiple ---------------- */
function qzNew(k){ var c=D.qz[k]; S.qz[k]={order:shuffle(range(c.items.length)).slice(0,c.n), i:0, res:[], perm:{}}; save(); }
function qHead(k, c, it){
 var h=''; if(it.ad) h+='<div class="ad"><b class="h">'+esc(it.ad[0])+'</b>'+esc(it.ad[1])+'</div>';
 if(c.bm) return h+esc(it.q);
 if(c.pre) return h+'<span class="small muted">'+esc(c.pre)+'</span><b>'+esc(it.q)+'</b>';
 return h+esc(it.q).replace('____','<span class="blank">____</span>');
}
function qzRender(k, box){
 var c=D.qz[k]; if(!S.qz[k]) qzNew(k);
 var st=S.qz[k], N=st.order.length;
 if(st.i>=N){
  var ok=st.res.filter(function(r){return r.ok;}).length, fails=st.res.filter(function(r){return !r.ok;});
  var msg = ok>=N-1 ? '¡Muy bien!' : (ok>=Math.ceil(N*0.6) ? 'Bien. Mira otra vez las explicaciones de las que has fallado.' : 'Vuelve a las escenas de esas áreas y repite con otras frases.');
  var o='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+msg+'</p>';
  if(fails.length){ o+='<p class="small"><b>Para repasar:</b></p><ul class="small">'; fails.forEach(function(r){ var it=c.items[r.k]; o+='<li>'+esc(strip(it.q).slice(0,90))+' → <b>'+(c.bm?(it.ok?'Mal: '+strip(it.fix):'Bien'):esc(it.o[0]))+'</b></li>'; }); o+='</ul>'; }
  o+='<div class="row"><button class="btn cta" data-act="qrep" data-k="'+k+'">Repetir con otras frases</button></div></div>';
  box.innerHTML=o; return;
 }
 var idx=st.order[st.i], it=c.items[idx], ans=st.res[st.i], opts, ok;
 if(c.bm){ opts=[[0,'Bien'],[1,'Mal']]; ok=it.ok; }
 else { if(!st.perm[idx]){ st.perm[idx]=shuffle(range(it.o.length)); save(); } opts=st.perm[idx].map(function(j){ return [j,it.o[j]]; }); ok=0; }
 var o='<div class="qz"><div class="cnt">'+esc(c.name)+' · '+(st.i+1)+' de '+N+(it.area?' · '+esc(D.areas[it.area]):'')+'</div><div class="prog"><i style="width:'+Math.round(st.i/N*100)+'%"></i></div>';
 o+='<div class="qq">'+qHead(k,c,it)+'</div><div class="ops'+(c.bm?' bm':(it.o.length===4?' g4':''))+'" role="group">';
 opts.forEach(function(op){
  var cls=''; if(ans){ if(op[0]===ok) cls='good'; else if(op[0]===ans.pick) cls='bad'; }
  o+='<button type="button" data-act="qa" data-k="'+k+'" data-o="'+op[0]+'" class="'+cls+'"'+(ans?' disabled':'')+'>'+esc(op[1])+'</button>';
 });
 o+='</div>';
 if(ans){
  var extra=''; if(!c.bm && it.lit!==undefined && ans.pick===it.lit) extra=' <i>Has caído en la trampa: esa opción repite palabras del anuncio, pero dice otra cosa.</i>';
  o+='<div class="fb '+(ans.ok?'good':'bad')+'" role="status"><b>'+(ans.ok?'¡Bien!':'No.')+'</b> '+(c.bm&&it.ok?'Corrección: '+it.fix+'<br>':'')+it.why+extra+'</div>';
 }
 o+='<div class="row"'+(ans?'':' hidden')+'><button class="btn cta" data-act="qnext" data-k="'+k+'">'+(st.i+1<N?'Siguiente':'Ver el resultado')+'</button></div></div>';
 box.innerHTML=o;
}
function qzAnswer(k, pick){
 var c=D.qz[k], st=S.qz[k]; if(st.res[st.i]) return;
 var it=c.items[st.order[st.i]], ok = c.bm ? (pick===it.ok) : (pick===0);
 st.res[st.i]={k:st.order[st.i], pick:pick, ok:ok};
 if(st.i===st.order.length-1){
  var n=st.res.filter(function(r){return r&&r.ok;}).length, fl=[];
  st.res.forEach(function(r){ if(r&&!r.ok) fl.push(strip(c.items[r.k].q).slice(0,70)); });
  S.qlog[k]={last:n+'/'+st.order.length, fails:fl};
 }
 save();
}

/* ---------------- dilo de otra forma ---------------- */
function renderOt(){
 var ps=$('otsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ot);
 if(S.ot==='cards'){
  $('otinfo').textContent='Lee lo que dice el texto y piensa cómo lo puede decir la pregunta. Pulsa la tarjeta para verlo.';
  var o='<div class="pills">'; D.order.forEach(function(a){ o+='<button class="pill'+(S.ar===a?' on':'')+'" data-act="otar" data-a="'+a+'">'+D.aic[a]+esc(D.areas[a])+'</button>'; }); o+='</div><div class="flip">';
  D.parejas[S.ar].forEach(function(p,i){ var k=S.ar+i, on=!!S.flip[k]; o+='<button type="button" data-act="flip" data-k="'+k+'" class="'+(on?'on':'')+'" aria-pressed="'+on+'"><span class="p">El texto dice</span><b>'+esc(p[0])+'</b>'+(on?'<span class="p" style="margin-top:8px">La pregunta dice</span>'+esc(p[1]):'<span class="p" style="margin-top:8px">¿Y la pregunta? Toca.</span>')+'</button>'; });
  $('otbox').innerHTML=o+'</div>';
 } else { $('otinfo').textContent=D.qz[S.ot].info; qzRender(S.ot, $('otbox')); }
}

/* ---------------- practica: huecos ---------------- */
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
  var mo=D.motivos[g.m];
  if(c.cur===g.ok) o+='<li class="ok">'+g.n+'. ✓ <b>'+esc(g.ok)+'</b> · <span class="vchip">'+esc(D.areas[mo.a])+'</span> '+mo.w+'</li>';
  else o+='<li class="no">'+g.n+'. ✗ <b>'+esc(c.cur)+'</b> no va aquí. Pista: <span class="vchip">'+esc(D.areas[mo.a])+'</span> '+mo.w+' Prueba otra vez.</li>';
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
var EXINFO={e2:'Un correo, un blog, un mensaje y la descripción de una foto. Elige la palabra de cada hueco: la corrección sale enseguida, con el motivo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
var CH=['Cada pauta tiene sus palabras: los viajes, el trabajo, los estudios, el tiempo...','He usado el nombre de verdad y no «cosa».','Los nombres llevan bien el artículo: el andén, la taquilla.','Cada palabra va con su verbo: jugar al tenis, tocar la guitarra, aprobar un examen.','El tiempo con hacer (hace sol) y con llover (llueve); la entrada del teatro y el billete del tren: lo he revisado.'];
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+'</div>';
 h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(a){ return '<span class="vchip">'+esc(D.areas[a])+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas te dicen de qué área son las palabras de cada pauta: abre sus escenas si las necesitas. Unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu texto</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar mis palabras</button></div><div id="rvbox" aria-live="polite"></div>';
 h+='<h3>Mi lista de las palabras</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function sents(t){ return t.match(/[^.!?\n]+[.!?]*/g)||[]; }
function detIds(t){ var o={}, ss=sents(t).map(norm); D.detector.forEach(function(d){ var r=new RegExp(d.re); if(d.sc==='s'){ if(ss.some(function(s){ return r.test(s); })) o[d.id]=1; } else if(r.test(norm(t))) o[d.id]=1; }); return Object.keys(o).sort(); }
function cuenta(t){ var n=norm(t), o={}; D.order.forEach(function(a){ var f={}; D.cuenta[a].forEach(function(p){ if(new RegExp(p[1]).test(n)) f[p[0]]=1; }); o[a]=Object.keys(f).sort(); }); return o; }
window.__R14detect=detIds; window.__R14cuenta=cuenta;
function review(){
 var L=lam(), txt=$('wtext').value, out=[], red=0, amb=0;
 if(txt.trim().length<20){ $('rvbox').innerHTML='<ul class="rv"><li class="a">Escribe primero tu texto.</li></ul>'; return; }
 sents(txt).forEach(function(s){
  if(!s.trim()) return; var n=norm(s);
  D.detector.forEach(function(d){
   if(d.sc!=='s') return; var m=new RegExp(d.re).exec(n); if(!m) return;
   if(d.t==='r') red++; else amb++;
   var a=m.index, b=m.index+m[0].length; if(d.re.charAt(0)==='^'){ a=0; b=s.length; }
   var hl=esc(s.slice(0,a))+'<mark>'+esc(s.slice(a,b))+'</mark>'+esc(s.slice(b));
   out.push('<li class="'+d.t+'">'+(d.t==='r'?'<b>¡Ojo!</b> ':'<b>Mira esto:</b> ')+d.msg+'<br><span class="small">'+hl+'</span></li>');
  });
 });
 D.detector.forEach(function(d){
  if(d.sc!=='x' || !new RegExp(d.re).test(norm(txt))) return;
  if(d.t==='r') red++; else amb++;
  out.push('<li class="'+d.t+'">'+(d.t==='r'?'<b>¡Ojo!</b> ':'<b>Mira esto:</b> ')+d.msg+'</li>');
 });
 var c=cuenta(txt), wc=txt.trim().split(/\s+/).length, tot=0; D.order.forEach(function(a){ tot+=c[a].length; });
 L.pautas.forEach(function(p,i){ p[1].forEach(function(a){ if(!c[a].length){ amb++; out.push('<li class="a"><b>Mira esto:</b> la pauta '+(i+1)+' («'+esc(p[0].replace(/[;.]$/,''))+'») necesita palabras de <b>'+esc(D.areas[a].toLowerCase())+'</b>, y no veo ninguna de sus escenas.</li>'); } }); });
 if(wc>=40 && tot<8){ amb++; out.push('<li class="a"><b>Mira esto:</b> solo veo '+tot+' palabras de las escenas. Usa más nombres precisos: el andén, la taquilla, el currículum...</li>'); }
 if(!red && !amb) out.unshift('<li class="g">No he encontrado confusiones típicas y usas '+tot+' palabras de las escenas. ¡Bien! Mira tú también la lista de abajo.</li>');
 else if(!red) out.unshift('<li class="g">No he encontrado errores seguros. Mira los puntos ámbar: son cosas que conviene comprobar.</li>');
 var cn='<div class="cnts">'+D.order.map(function(a){ return '<div>'+D.aic[a]+'<b>'+esc(D.areas[a])+': '+c[a].length+'</b>'+(c[a].length?' · '+c[a].map(esc).join(', '):'')+'</div>'; }).join('')+'</div>';
 S.wrev[L.id]={red:red, amb:amb, tot:tot, cnt:D.order.map(function(a){ return D.areas[a]+' '+c[a].length; }).join(', '), words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul><p class="small"><b>Tus palabras de las escenas</b> ('+tot+'):</p>'+cn+'<p class="muted small">Tu texto: '+wc+' palabras (la lámina pide '+L.palabras[0]+'-'+L.palabras[1]+'). La página solo ve las palabras de esta ficha: tu profesora corrige el texto completo.</p>';
}

/* ---------------- relojes ---------------- */
var TM=null;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } }
function clockTxt(s){ s=Math.max(0,Math.ceil(s)); return Math.floor(s/60)+':'+(s%60<10?'0':'')+(s%60); }

/* ---------------- ahora tu: oral, la escena en un minuto ---------------- */
function foto(){ return D.oral.filter(function(f){ return f.id===S.of; })[0]; }
function renderO(){
 var box=$('obox'), f=foto(), R=S.ro, h='<div class="pills">';
 D.oral.forEach(function(x){ h+='<button class="pill'+(S.of===x.id?' on':'')+'" data-act="of" data-id="'+x.id+'">'+esc(x.titulo)+'</button>'; });
 h+='</div><div class="ocard"><div class="ofoto" id="ofoto"><img src="'+f.img+'" alt="'+esc(f.desc)+'" onerror="this.parentNode.classList.add(\'noimg\')"><p class="d">'+esc(f.desc)+'</p></div>';
 if(!R || R.f!==f.id){
  h+='<p class="small">Un minuto en tres partes: <b>'+f.grupos.map(function(g){ return esc(g[0].toLowerCase()); }).join('</b>, <b>')+'</b>. Habla en frases cortas: <i>Hay..., lleva..., está + -ando...</i></p><div class="row"><button class="btn cta" data-act="ostart">Empezar (1 minuto)</button></div>';
  var lg=S.olog.filter(function(x){ return x.f===f.id; });
  if(S.olog.length) h+='<p class="hist"><b>Tus últimas prácticas:</b> '+S.olog.map(function(x){ return x.d+' · '+esc(x.t)+': '+x.n+'/'+x.tot+' palabras'; }).join(' · ')+'</p>';
 } else if(R.ph===1){
  h+='<div class="esc" id="oesc">'+esc(f.grupos[0][0])+'</div><div class="clock" id="oclk">1:00</div><div class="tbar"><i id="obar"></i></div><div class="row"><button class="btn cta" data-act="ostop">Ya está</button></div>';
 } else {
  h+='<p><b>¿Qué palabras has dicho?</b> Márcalas con sinceridad: son las que se esperan en esta foto.</p>';
  f.grupos.forEach(function(g,gi){ h+='<h4 style="margin:12px 0 4px">'+esc(g[0])+'</h4><div class="wchecks">'+g[1].map(function(w,wi){ var k=gi+'-'+wi; return '<label><input type="checkbox" data-ow="'+k+'"'+(R.pick[k]?' checked':'')+'> '+esc(w)+'</label>'; }).join('')+'</div>'; });
  h+='<div class="row"><button class="btn cta" data-act="osave">Guardar</button><button class="btn sm" data-act="oagain">Otra vez</button></div><div id="ores"></div>';
 }
 box.innerHTML=h+'</div>';
}
function oRun(){
 stopTimer(); var f=foto(), T0=Date.now(), dur=60;
 TM=setInterval(function(){
  var t=(Date.now()-T0)/1000, bar=$('obar'); if(!bar){ stopTimer(); return; }
  $('oclk').textContent=clockTxt(dur-t); bar.style.width=Math.min(100,t/dur*100)+'%';
  $('oesc').textContent=f.grupos[Math.min(2,Math.floor(t/20))][0];
  if(t>=dur){ stopTimer(); S.ro.ph=2; save(); renderO(); }
 }, 200);
}

/* ---------------- opinion y copiar ---------------- */
function renderOpn(){
 var o=''; for(var i=1;i<=10;i++) o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>';
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked=r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function pack(){
 var L=['CURSO DELE A2 - R14b: VOCABULARIO EN ESCENAS (2) - FUERA DE CASA','Nombre: '+(S.name||'-'),''];
 L.push('LAS ESCENAS: TAPA Y RECUERDA');
 var any=false; D.escenas.forEach(function(e){ var t=S.tap[e.id]; if(!t) return; any=true; L.push('- '+D.areas[e.area]+', '+e.titulo+': '+(t.done?t.first+'/'+t.tot+' a la primera':'sin terminar')); });
 if(!any) L.push('sin hacer');
 var ms=Object.keys(S.miss); L.push('Palabras que se resisten: '+(ms.length?ms.join(', '):'-'));
 L.push('','MI CUADERNO DE ESCENAS');
 if(!S.cuad.length) L.push('vacio');
 S.cuad.forEach(function(c){ L.push('- ['+D.areas[c.a]+'] '+c.w+(c.f?' | '+c.f:'')); });
 L.push('','ESCUCHA Y ELIGE');
 var cs=Object.keys(S.ca); if(!cs.length) L.push('sin hacer');
 else { var ok=cs.filter(function(k){ return S.ca[k].ok; }).length; L.push(ok+'/'+cs.length+' bien a la primera'); cs.forEach(function(k){ var it=D.ca[k], r=S.ca[k]; if(!r.ok) L.push('- fallo: '+it.q+' -> eligio '+it.o[r.pick]+', era '+it.o[it.ok]); }); }
 L.push('','EJERCICIOS (ultimo resultado)');
 ['pa','an','p1','p2','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 D.textos.forEach(function(t){
  var f=fbList(t.id,t.texto), errs=[];
  gapInfo(t.id,t.texto).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); });
  var started=Object.keys(S.cz).some(function(k){return k.indexOf(t.id+'-')===0;});
  L.push('- Textos del examen, '+t.titulo+': '+(started?f.first+'/'+f.tot+' a la primera'+(f.done<f.tot?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 L.push('','ORAL: LA ESCENA EN UN MINUTO');
 if(!S.olog.length) L.push('sin hacer');
 S.olog.forEach(function(r){ L.push('- '+r.d+', foto '+r.f+' ('+r.t+'): '+r.n+'/'+r.tot+' palabras dichas (autoevaluacion)'); });
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' ('+l.palabras[0]+'-'+l.palabras[1]+' palabras)','Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision: '+rv.red+' avisos rojos, '+rv.amb+' ambar | palabras de las escenas: '+rv.tot+' ('+rv.cnt+') | '+rv.words+' palabras');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. El area que mas cuesta: '+(S.o2||'-'),'3. Escenas en vez de listas: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}
window.__R14pack=pack;

/* ---------------- eventos ---------------- */
var ACTS={
 ar:function(b){ S.ar=b.getAttribute('data-a'); var f=D.escenas.filter(function(e){ return e.area===S.ar; })[0]; S.es=f.id; save(); renderEsc(); },
 es:function(b){ S.es=b.getAttribute('data-id'); save(); renderEsc(); },
 mode:function(b){ S.mode=b.getAttribute('data-k'); save(); renderEsc(); },
 tapchk:function(){ tapCheck(false); },
 tapshow:function(){ tapCheck(true); },
 tapreset:function(){ delete S.tap[S.es]; save(); renderEsc(); nav(); },
 cadd:function(){ var w=$('cw').value.trim(), f=$('cf').value.trim(); if(!w) { $('cw').focus(); return; } S.cuad.push({a:S.ar, w:w, f:f}); save(); renderCuad(); var n=$('cw'); if(n) n.focus(); },
 cdel:function(b){ S.cuad.splice(+b.getAttribute('data-i'),1); save(); renderCuad(); },
 caall:function(){ stopAudio(); S.caseq=range(D.ca.length); S.cai=0; S.readT=null; save(); renderCa(); },
 carnd:function(){ stopAudio(); S.caseq=shuffle(range(D.ca.length)).slice(0,6); S.caseq.forEach(function(i){ delete S.ca[i]; delete S.plays[i]; }); S.cai=0; S.readT=null; save(); renderCa(); nav(); },
 cago:function(b){ stopAudio(); S.cai=+b.getAttribute('data-p'); S.readT=null; save(); renderCa(); },
 caplay:function(){ caPlay(); },
 caread:function(){ S.readT=S.caseq[S.cai]; renderCa(); },
 caans:function(b){ caAnswer(+b.getAttribute('data-o')); },
 canext:function(){ stopAudio(); S.cai++; S.readT=null; save(); renderCa(); },
 ot:function(b){ S.ot=b.getAttribute('data-k'); save(); renderOt(); },
 otar:function(b){ S.ar=b.getAttribute('data-a'); save(); renderOt(); },
 flip:function(b){ var k=b.getAttribute('data-k'); S.flip[k]=!S.flip[k]; save(); renderOt(); },
 ex:function(b){ S.ex=b.getAttribute('data-k'); save(); renderEx(); },
 etext:function(b){ S.etext=b.getAttribute('data-id'); save(); renderE2(); },
 qa:function(b){ var k=b.getAttribute('data-k'), box=D.qz[k]&&(k==='pa'||k==='an')?$('otbox'):$('exbox'); qzAnswer(k, +b.getAttribute('data-o')); qzRender(k, box); nav(); var f=box.querySelector('.fb'); if(f&&f.scrollIntoView) f.scrollIntoView({block:'nearest'}); },
 qnext:function(b){ var k=b.getAttribute('data-k'), box=(k==='pa'||k==='an')?$('otbox'):$('exbox'); S.qz[k].i++; save(); qzRender(k, box); },
 qrep:function(b){ var k=b.getAttribute('data-k'), box=(k==='pa'||k==='an')?$('otbox'):$('exbox'); qzNew(k); qzRender(k, box); },
 czreset:function(b){ b.getAttribute('data-ids').split(',').forEach(function(id){ Object.keys(S.cz).forEach(function(g){ if(g.indexOf(id+'-')===0) delete S.cz[g]; }); }); save(); renderEx(); nav(); },
 at:function(b){ S.at=b.getAttribute('data-k'); save(); renderAt(); },
 lam:function(b){ S.lam=b.getAttribute('data-id'); save(); renderLam(); },
 review:function(){ review(); nav(); },
 of:function(b){ stopTimer(); S.of=+b.getAttribute('data-id'); S.ro=null; save(); renderO(); },
 ostart:function(){ S.ro={f:S.of, ph:1, pick:{}}; save(); renderO(); oRun(); },
 ostop:function(){ stopTimer(); S.ro.ph=2; save(); renderO(); },
 osave:function(){
  var f=foto(), R=S.ro, n=Object.keys(R.pick).filter(function(k){ return R.pick[k]; }).length, tot=0; f.grupos.forEach(function(g){ tot+=g[1].length; });
  var d=new Date(); S.olog.push({d:d.getDate()+'/'+(d.getMonth()+1), f:f.id, t:f.titulo, n:n, tot:tot}); if(S.olog.length>6) S.olog=S.olog.slice(-6);
  save(); nav();
  $('ores').innerHTML='<div class="fb '+(n>=Math.ceil(tot*0.6)?'good':'bad')+'"><b>'+n+' de '+tot+' palabras.</b> '+(n>=Math.ceil(tot*0.6)?'¡Muy bien! Con estas palabras puedes llegar a los dos o tres minutos de la tarea 2.':'Mira las que no has dicho, apúntalas en tu cuaderno y repite con la misma foto.')+'</div>';
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
 if(S.ro && S.ro.ph===1) S.ro=null;
 if(S.at==='w') renderLam(); else renderO();
}
document.addEventListener('click', function(e){
 var g=e.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
document.addEventListener('keydown', function(e){
 if(e.key==='Enter' && e.target.hasAttribute && e.target.hasAttribute('data-tap')){ e.preventDefault(); tapCheck(false); }
 if(e.key==='Enter' && (e.target.id==='cw'||e.target.id==='cf')){ e.preventDefault(); ACTS.cadd(); }
});
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.tagName==='SELECT' && t.hasAttribute('data-g')){ czChange(t); return; }
 if(t.hasAttribute && t.hasAttribute('data-wchk')){ S.wchk[t.getAttribute('data-wchk')]=t.checked; save(); return; }
 if(t.hasAttribute && t.hasAttribute('data-ow')){ S.ro.pick[t.getAttribute('data-ow')]=t.checked; save(); return; }
 if(['o1','o2','o3','o5'].indexOf(t.name)>=0){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){
 var t=e.target;
 if(t.id==='wtext'){ S.w[S.lam]=t.value; save(); }
 if(t.id==='o4'){ S.o4=t.value; save(); }
 if(t.id==='sname'){ S.name=t.value; save(); }
});
window.addEventListener('afterprint', function(){ var v=$('v-resumen'); if(v) v.classList.remove('printme'); });

renderEsc(); renderCa(); renderOt(); renderEx(); renderAt(); renderOpn(); go(S.cur);
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
print("ok", FILE, "| escenas:", len(B.ESCENAS), "| palabras en las redes:", sum(len(ws) for e in B.ESCENAS for _, ws in e["ramas"]),
      "| conversaciones:", len(B.CA1), "| anuncios:", len(B.ANUNCIOS), "| huecos:", sum(ngaps.values()),
      "| items:", len(B.P_SOBRA) + len(B.P_VERBO) + len(B.E_BIENMAL) + len(PA),
      "| pruebas del detector:", len(B.DETECTOR_PRUEBAS), "(navegador: %s)" % ("igual que Python" if NODE_OK else "sin probar"),
      "| buena en el desplegable (1a/2a/3a):", POS_TXT, "| voces.txt:", "comprobado" if VOCES is not None else "no está en la carpeta")
