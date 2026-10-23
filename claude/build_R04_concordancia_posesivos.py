# -*- coding: utf-8 -*-
# FICHA DE REMEDIO R04 DEL CURSO DE PREPARACION DELE A2: CONCORDANCIA Y POSESIVOS
# Uso: python3 build_R04_concordancia_posesivos.py  -> DELEA2_curso_R04_concordancia_posesivos.html
# Subir a: biblioteca/recursos/A2/dele-curso/
# Contenidos: solo en banco_R04_concordancia_posesivos.py. Este archivo monta la pagina y comprueba el banco.
# Mismo formato y motor que la R01 y la R02: pestanas, correccion inmediata, huecos con motivo, "Ahora tu"
# con escritura (detector de errores tipicos) y oral (fotos M4T2 ya subidas), Tu opinion y Copiar.
# Enfoque cognitivo: EL NOMBRE MANDA (es el capitan y todo el equipo lleva su camiseta: masculino/femenino,
# uno/varios); EL POSESIVO MIRA A LA COSA (¿de quien? -> la palabra; ¿que cosa? -> el final); los tonicos:
# el nombre se va y su camiseta se queda. Espanol de Espana. Ejemplos propios.
import json, re, sys, unicodedata
from curso_comun import CSS, EMAIL, page
import banco_R04_concordancia_posesivos as B

TITLE = "Concordancia y posesivos"
FILE = "DELEA2_curso_R04_concordancia_posesivos.html"
STORAGE = "dele-a2-curso-R04"
IMG_T2 = "https://2spanishteachers.com/wp-content/uploads/" + B.MES_WP_T2.strip("/") + "/M4T2_foto%d.jpg"

# ------------------------------------------------------------------ COMPROBACIONES
ERR = []
def err(m): ERR.append(m)
GROUP = re.compile(r"\[(ms|fs|mp|fp):([^\[\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
TAGS = {"ms", "fs", "mp", "fp"}
ENDS = {"ms": "o", "fs": "a", "mp": "os", "fp": "as"}

DET = {}
def _add(words, tags):
    for w, t in zip(words, tags): DET.setdefault(w, set()).update(t if isinstance(t, set) else {t})
FOUR = ["ms", "fs", "mp", "fp"]
_add(["el", "la", "los", "las"], FOUR); _add(["un", "una", "unos", "unas"], FOUR)
for raiz in ("est", "es", "aquel"):
    forms = {"est": ["este", "esta", "estos", "estas"], "es": ["ese", "esa", "esos", "esas"],
             "aquel": ["aquel", "aquella", "aquellos", "aquellas"]}[raiz]
    _add(forms, FOUR)
for raiz in ("nuestr", "vuestr", "much", "poc", "otr", "tod", "mí", "tuy", "suy"):
    _add([raiz + e for e in ("o", "a", "os", "as")], FOUR)
_add(["algún", "alguna", "algunos", "algunas"], FOUR); _add(["ningún", "ninguna"], ["ms", "fs"])
for w in ("mi", "tu", "su"): DET[w] = {"ms", "fs"}
for w in ("mis", "tus", "sus"): DET[w] = {"mp", "fp"}
POSS = {w for w in DET if re.match(r"^(mi|tu|su|mis|tus|sus|nuestr|vuestr|mí|tuy|suy)", w)}
INVAR = {"muy", "y", "más", "menos", "de", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "veinte"}
SING_S = {"gris", "paraguas", "cumpleaños", "lunes", "país", "mes", "autobús", "inglés", "francés"}
AGUA = {"agua", "aula", "hambre", "águila"}
PUNCT = "¿?¡!.,;:—«»()"

def words_of(body):
    out = []
    for w in body.split():
        noun = w.startswith("^")
        w = w.lstrip("^").strip(PUNCT)
        if w: out.append((w, noun))
    return out

def chk_word(w, noun, tag, where, nounword=""):
    lw = w.lower()
    plural = tag[1] == "p"
    if lw in INVAR: return
    if noun:
        if plural and not lw.endswith("s"): err("%s: el nombre «%s» no lleva -s y el grupo es de varios" % (where, w))
        if not plural and lw.endswith("s") and lw not in SING_S: err("%s: el nombre «%s» termina en -s y el grupo es de uno" % (where, w))
        return
    if lw in DET:
        ok = tag in DET[lw] or (lw in ("el", "un") and tag == "fs" and nounword in AGUA)
        if not ok: err("%s: «%s» no lleva la camiseta %s" % (where, w, tag))
        return
    if re.search(r"(o|os|a|as)$", lw):
        if tag[0] == "m" and not re.search(r"os?$", lw): err("%s: el adjetivo «%s» no es masculino" % (where, w))
        if tag[0] == "f" and not re.search(r"as?$", lw): err("%s: el adjetivo «%s» no es femenino" % (where, w))
    if plural and not lw.endswith("s"): err("%s: «%s» no lleva -s y el grupo es de varios" % (where, w))
    if not plural and lw.endswith("s") and lw not in SING_S: err("%s: «%s» lleva -s y el grupo es de uno" % (where, w))

def chk_group(tag, body, where):
    if tag not in TAGS: err("%s: camiseta desconocida %s" % (where, tag)); return
    ws = words_of(body)
    nouns = [w for w, n in ws if n]
    if len(nouns) > 1: err("%s: un grupo con dos nombres: %s" % (where, body))
    nw = nouns[0].lower() if nouns else ""
    for w, n in ws: chk_word(w, n, tag, where, nw)

def chk_marks(s, where, need=0):
    rest = GROUP.sub("", s)
    if "[" in rest or "]" in rest: err("marca mal cerrada en %s: %s" % (where, s[:70]))
    gs = GROUP.findall(s)
    for t, b in gs: chk_group(t, b, where)
    if len(gs) < need: err("%s: hacen falta al menos %d grupos marcados" % (where, need))
    return gs

def plain(s): return GROUP.sub(lambda m: m.group(2).replace("^", ""), s)

for k, (f, w) in B.MOTIVOS.items():
    if f not in B.FAMILIAS or not w: err("motivo mal definido: " + k)

for i, e in enumerate(B.EQUIPOS):
    gs = chk_marks(e["bien"], "equipo %d" % i, 1)
    if len(gs) != 1: err("equipo %d: la frase buena es un solo grupo" % i)
    nouns = [w for w, t in e["mal"] if w.startswith("^")]
    if len(nouns) != 1: err("equipo %d: la frase mala necesita un nombre (^)" % i); continue
    nt = [t for w, t in e["mal"] if w.startswith("^")][0]
    if any(t not in TAGS for _, t in e["mal"]): err("equipo %d: camiseta desconocida en la frase mala" % i)
    if all(t == nt for _, t in e["mal"]): err("equipo %d: en la frase mala todos llevan la misma camiseta" % i)
    if " ".join(w.lstrip("^") for w, _ in e["mal"]) == plain(e["bien"]): err("equipo %d: la frase mala es igual que la buena" % i)
    if not e.get("rb") or not e.get("rm"): err("equipo %d sin explicacion" % i)

for title, items in B.VISTE:
    if not items: err("viste: lista vacia")
for t, gs, why in B.ENGANAN:
    for g in gs: chk_marks(g, "enganan " + t, 1)
    if not why: err("enganan sin explicacion: " + t)
for d in B.DUENOS:
    if d["tipo"] not in ("num", "gen") or d["n"] not in (1, 2): err("dueno mal definido: " + d["id"])
for c in B.COSAS:
    if c["t"] not in TAGS: err("cosa mal definida: " + c["w"])
for q, n, g, m, why in B.SU_TRAMPA:
    gs = chk_marks(g, "su/sus " + q, 1)
    if gs and (gs[0][0][1] == "p") != (m > 1): err("su/sus %s: el numero de cosas no va con la camiseta" % q)
if not any(n == 2 and m == 1 for _, n, _, m, _ in B.SU_TRAMPA): err("su/sus: falta el caso de dos duenos y una cosa")
if not any(n == 1 and m > 1 for _, n, _, m, _ in B.SU_TRAMPA): err("su/sus: falta el caso de un dueno y varias cosas")
for a, b in B.TONICOS:
    ga = chk_marks(a, "tonicos", 1); gb = chk_marks(b, "tonicos", 1)
    if ga and gb and ga[-1][0] != gb[-1][0]: err("tonicos: el grupo sin nombre no lleva la camiseta del nombre: " + b)
    if gb and "^" in gb[-1][1]: err("tonicos: la frase sin nombre lleva nombre: " + b)
for c, d, s in B.DONDE: chk_marks(s, "donde " + c, 2)
for mal, bien, why in B.ERRORES:
    chk_marks(bien, "errores", 1)
    if plain(bien) == mal or not why: err("error tipico sin correccion o sin porque: " + mal)
for k in ("mis amigo", "la problema", "las gente", "nuestro casa", "su hijos", "chicas simpático", "mucho personas"):
    if not any(k in m.lower() for m, _, _ in B.ERRORES): err("falta el error tipico: " + k)

def chk_quiz(items, name, nmin, bm=False, pos=False):
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
            if it["q"].count("____") < 1: err("%s: falta el hueco ____: %s" % (name, it["q"]))
            if it["q"].count("____") > 1 and "/" not in o[0]: err("%s: dos huecos, la respuesta tiene que llevar /: %s" % (name, it["q"]))
            if pos and not any(w in POSS for w in re.split(r"[ /]+", o[0].lower())): err("%s: la buena no lleva posesivo: %s" % (name, it["q"]))
chk_quiz(B.P_FORMA, "P_FORMA", 12)
chk_quiz(B.P_POS, "P_POS", 10, pos=True)
chk_quiz(B.E_BIENMAL, "E_BIENMAL", 10, bm=True)
if not any(i["ok"] == 0 for i in B.E_BIENMAL) or not any(i["ok"] == 1 for i in B.E_BIENMAL): err("bien/mal: hacen falta de los dos tipos")
if sum(1 for i in B.E_BIENMAL if i["ok"] == 1) < 7: err("bien/mal: los siete errores tipicos tienen que salir")

def chk_gaps(s, where):
    n = 0
    for g in GAP.findall(s):
        n += 1
        if "#" not in g: err("hueco sin motivo en %s: %s" % (where, g)); continue
        ops, mot = g.split("#")
        ops = ops.split("|")
        if len(ops) != 3 or len(set(o.lower() for o in ops)) != 3: err("hueco sin 3 opciones distintas en %s: %s" % (where, g))
        if mot not in B.MOTIVOS: err("motivo desconocido en %s: %s" % (where, mot)); continue
        if B.MOTIVOS[mot][0] == "pos" and ops[0].lower() not in POSS: err("en %s la buena (%s) no es un posesivo, como dice su motivo" % (where, ops[0]))
    if n == 0: err("texto sin huecos: " + where)
    if "[[" in GAP.sub("", s) or "]]" in GAP.sub("", s): err("hueco mal cerrado en " + where)
    return n
ngaps = {}
for t in B.TEXTOS: ngaps[t["id"]] = chk_gaps(t["texto"], t["id"])
alltex = " ".join(t["texto"] for t in B.TEXTOS)
for f in B.FAMILIAS:
    if not any(B.MOTIVOS[g.split("#")[1]][0] == f for g in GAP.findall(alltex)): err("los textos no trabajan la familia " + f)
usados = {g.split("#")[1] for g in GAP.findall(alltex)}
for m in ("gen", "num", "inv", "engana", "gente", "mucho", "pos_cosa"):
    if m not in usados: err("los textos no usan el motivo " + m)

for L in B.LAMINAS:
    if len(L["pautas"]) != 5: err("lamina %s: 5 pautas" % L["id"])
    for _, fs in L["pautas"]:
        for f in fs:
            if f not in B.FOCOS: err("foco desconocido en lamina " + L["id"])

def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
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
if not ERR:
    for txt, exp in B.DETECTOR_PRUEBAS:
        got = sorted(d["id"] for d in B.DETECTOR if d["_rx"].search(norm(txt)))
        if got != sorted(exp): err("detector: %r da %s y deberia dar %s" % (txt, got, sorted(exp)))
    for d in B.DETECTOR:
        if not any(d["id"] in e for _, e in B.DETECTOR_PRUEBAS): err("el aviso %s no tiene ninguna prueba" % d["id"])
    if sum(1 for _, e in B.DETECTOR_PRUEBAS if not e) < 8: err("detector: hacen falta al menos 8 pruebas que NO deben saltar")
    for m in ("mis amigo", "la problema", "las gente", "nuestro casa", "su hijos", "chicas simpático", "mucho personas"):
        if not any(m in t.lower() and e for t, e in B.DETECTOR_PRUEBAS): err("detector: ninguna prueba con el error tipico " + m)

fids = [f["id"] for f in B.FOTOS]
if len(set(fids)) != len(fids): err("fotos repetidas")
for f in B.FOTOS:
    if not 7 <= f["id"] <= 12: err("foto %s: solo las fotos 7-12 de la tarea 2 (como en el examen)" % f["id"])
    chk_marks(f["como"], "foto %d como" % f["id"], 5); chk_marks(f["ropa"], "foto %d ropa" % f["id"], 5)
    if not f["como"].startswith("En la foto hay"): err("foto %d: el modelo empieza con «En la foto hay»" % f["id"])
    if f["ropa"].count("lleva") < 3: err("foto %d: el modelo de la ropa usa «lleva» al menos tres veces" % f["id"])
    if not f.get("alt"): err("foto %d sin descripcion" % f["id"])
if ERR:
    print("\n".join("ERROR: " + e for e in ERR)); sys.exit(1)
for d in B.DETECTOR: d.pop("_rx", None)

# ------------------------------------------------------------------ HTML ESTATICO
LAB = {"ms": "masculino · uno", "fs": "femenino · uno", "mp": "masculino · varios", "fp": "femenino · varios"}
def mk(s):
    def rep(m):
        t, body = m.group(1), m.group(2)
        inner = re.sub(r"\^([^\s.,;:!?»)]+)", r'<b class="cap">\1</b>', body)
        return '<span class="g %s %s" title="%s">%s</span>' % (t[0], t[1], LAB[t], inner)
    return GROUP.sub(rep, s)

COLG = {"m": ("#17707F", "#DDF0F2"), "f": ("#6B3FA0", "#EFE7F8")}
COLP = ("#1D5FA8", "#E2ECF8")   # posesivos (la palabra que elige el dueno)
INK = "#14161C"; BAD = "#B3261E"

def shirt(cx, cy, tag, s=1.0, cap=False, bad=False, text=True):
    c, soft = COLG[tag[0]]
    st = BAD if bad else c
    def one(dx, dy, fill):
        pts = [(-34, -26), (-14, -32), (0, -24), (14, -32), (34, -26), (48, -6), (32, 2), (32, 32), (-32, 32), (-32, 2), (-48, -6)]
        d = "M" + " L".join("%.1f,%.1f" % (cx + dx + x * s, cy + dy + y * s) for x, y in pts) + " Z"
        return '<path d="%s" fill="%s" stroke="%s" stroke-width="2.5" stroke-linejoin="round"/>' % (d, fill, st)
    o = ""
    if tag[1] == "p": o += one(9 * s, -9 * s, "#fff")
    o += one(0, 0, soft if not bad else "#F8E1DE")
    if text:
        o += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="700" fill="%s">%s</text>' % (cx, cy - 2 * s, 12 * s, st, "masc." if tag[0] == "m" else "fem.")
        o += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" fill="%s">%s</text>' % (cx, cy + 15 * s, 11 * s, st, "uno" if tag[1] == "s" else "varios")
    if cap:
        o += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/><text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="700" fill="#fff">C</text>' % (
            cx - 36 * s, cy - 14 * s, 9 * s, INK, cx - 36 * s, cy - 10 * s, 11 * s)
    if bad:
        o += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="700" fill="%s">✗</text>' % (cx + 40 * s, cy - 30 * s, 22 * s, BAD)
    return o

def team_svg(words, aria):
    # words: [(texto, tag, es_nombre, mala)]
    n = len(words); W = 640; slot = W / n
    nt = [t for _, t, isn, _ in words if isn][0]
    c = COLG[nt[0]][0]
    o = '<svg class="dg" viewBox="0 0 640 220" role="img" aria-label="%s">' % aria
    xs = [slot * (i + 0.5) for i in range(n)]
    o += '<line x1="%.1f" y1="196" x2="%.1f" y2="196" stroke="%s" stroke-width="3" stroke-dasharray="7 6"/>' % (xs[0], xs[-1], c)
    for (w, t, isn, bad), x in zip(words, xs):
        o += shirt(x, 74, t, 1.1 if isn else 0.95, cap=isn, bad=bad)
        o += '<text x="%.1f" y="150" text-anchor="middle" font-size="%d" font-weight="%s" fill="%s"%s>%s</text>' % (
            x, 22 if isn else 20, "700" if isn else "500", BAD if bad else INK, ' text-decoration="underline"' if isn else '', w)
        o += '<circle cx="%.1f" cy="196" r="7" fill="%s"/>' % (x, BAD if bad else c)
        if bad: o += '<text x="%.1f" y="182" text-anchor="middle" font-size="12" font-weight="700" fill="%s">otra camiseta</text>' % (x, BAD)
    o += '<text x="8" y="214" font-size="12" fill="#5E5A55">C = el capitán (el nombre)</text>'
    return o + '</svg>'

def team_bien(e):
    t, body = GROUP.findall(e["bien"])[0]
    return team_svg([(w, t, isn, False) for w, isn in words_of(body)], "Todo el equipo lleva la camiseta del nombre: " + LAB[t])

def team_mal(e):
    nt = [t for w, t in e["mal"] if w.startswith("^")][0]
    return team_svg([(w.lstrip("^"), t, w.startswith("^"), t != nt) for w, t in e["mal"]], "Una palabra lleva otra camiseta: error de concordancia")

def person(x, y, s=1.0, col=INK):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="%s" stroke-width="2.5"/>'
            '<path d="M%.1f,%.1f q%.1f,%.1f %.1f,0" fill="#fff" stroke="%s" stroke-width="2.5"/>') % (
        x, y, 13 * s, col, x - 22 * s, y + 44 * s, 22 * s, -32 * s, 44 * s, col)

def house(x, y, col, soft, s=1.0):
    return ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="2.5" stroke-linejoin="round"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#fff" stroke="%s" stroke-width="2"/>') % (
        x - 22 * s, y, x, y - 20 * s, x + 22 * s, y, x + 22 * s, y + 26 * s, x - 22 * s, y + 26 * s, soft, col, x - 6 * s, y + 10 * s, 12 * s, 16 * s, col)

def arrow(x1, y1, x2, y2, col, lab="", lx=None, ly=None):
    o = '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3"/>' % (x1, y1, x2, y2, col)
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 12 * math.cos(a - 0.4), y2 - 12 * math.sin(a - 0.4)); p2 = (x2 - 12 * math.cos(a + 0.4), y2 - 12 * math.sin(a + 0.4))
    o += '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>' % (x2, y2, p1[0], p1[1], p2[0], p2[1], col)
    if lab: o += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="14" font-weight="700" fill="%s">%s</text>' % (lx, ly, col, lab)
    return o

def dos_preguntas():
    cf, sf = COLG["f"]; cp, sp = COLP
    o = '<svg class="dg" viewBox="0 0 640 230" role="img" aria-label="Dos preguntas: de quién es elige la palabra; qué cosa es pone el final. Nosotros y una casa: nuestra casa.">'
    o += person(60, 70) + person(110, 70)
    o += '<text x="85" y="140" text-anchor="middle" font-size="14" fill="#5E5A55">nosotros</text>'
    o += house(580, 70, cf, sf, 1.3) + '<text x="580" y="140" text-anchor="middle" font-size="14" fill="#5E5A55">una casa</text>'
    o += arrow(140, 92, 238, 160, cp, "¿De quién?", 175, 60)
    o += arrow(548, 104, 398, 160, cf, "¿Qué cosa?", 470, 60)
    o += '<text x="320" y="196" text-anchor="middle" font-size="40" font-family="Georgia,serif" font-weight="700"><tspan fill="%s">nuestr</tspan><tspan fill="%s">a</tspan><tspan fill="%s"> casa</tspan></text>' % (cp, cf, INK)
    o += '<text x="220" y="222" text-anchor="middle" font-size="13" fill="%s">la palabra</text><text x="372" y="222" text-anchor="middle" font-size="13" fill="%s">la camiseta</text>' % (cp, cf)
    return o + '</svg>'

def su_svg(q, n, g, m):
    t = GROUP.findall(g)[0][0]; c, soft = COLG[t[0]]
    o = '<svg class="ic" viewBox="0 0 300 120" role="img" aria-label="%s: %s">' % (q, plain(g))
    for i in range(n): o += person(40 + i * 40, 30, 0.8)
    o += '<text x="%d" y="100" text-anchor="middle" font-size="13" fill="#5E5A55">%s</text>' % (40 + (n - 1) * 20, q)
    o += arrow(118, 50, 160, 50, "#5E5A55")
    for i in range(m): o += shirt(232 + i * 46 - (m - 1) * 23, 46, t, 0.42, text=False)
    o += '<text x="230" y="100" text-anchor="middle" font-size="15" font-weight="700" fill="%s">%s</text>' % (c, plain(g))
    return o + '</svg>'

def icon(k):
    cm, sm = COLG["m"]; cf, sf = COLG["f"]; cp, sp = COLP
    o = '<svg class="ic" viewBox="0 0 300 140" aria-hidden="true">'
    if k == 1:
        o += shirt(150, 66, "fp", 1.35, cap=True)
    elif k == 2:
        o += shirt(52, 70, "mp", 0.72) + shirt(150, 66, "mp", 0.95, cap=True) + shirt(248, 70, "mp", 0.72)
        o += '<line x1="60" y1="122" x2="240" y2="122" stroke="%s" stroke-width="3" stroke-dasharray="7 6"/>' % cm
    else:
        o += person(34, 30) + house(270, 52, cf, sf, 1.0)
        o += '<text x="150" y="122" text-anchor="middle" font-size="32" font-family="Georgia,serif" font-weight="700"><tspan fill="%s">nuestr</tspan><tspan fill="%s">a</tspan></text>' % (cp, cf)
        o += arrow(62, 60, 112, 92, cp) + arrow(244, 66, 196, 92, cf)
    return o + '</svg>'

def cards():
    txt = [("EL NOMBRE MANDA", "El capitán", "El nombre lleva una camiseta con dos datos: <b>masculino o femenino</b> y <b>uno o varios</b>. Él decide; los demás no.", "[fp:las ^amigas]: femenino y varios."),
           ("TODOS SE VISTEN IGUAL", "El equipo", "El artículo, este, mi, nuestro, mucho y los adjetivos llevan <b>la camiseta del capitán</b>.", "[mp:muchos ^amigos nuevos]"),
           ("EL POSESIVO MIRA A LA COSA", "Dos preguntas", "<b>¿De quién?</b> elige la palabra (mi, su, nuestr-). <b>¿Qué cosa?</b> le pone la camiseta.", "nosotros → [fs:nuestra ^casa]")]
    o = '<div class="cams">'
    for i, (k, h, p, ej) in enumerate(txt):
        o += '<div class="cam c%d"><div class="k">%s</div><h3>%s</h3>%s<p>%s</p><div class="ej">%s</div></div>' % (i + 1, k, h, icon(i + 1), p, mk(ej))
    return o + '</div>'

def viste():
    o = '<div class="mk3">'
    for i, (t, items) in enumerate(B.VISTE):
        o += '<div class="v%d"><h4>%s</h4><ul>%s</ul></div>' % (i, t, "".join("<li>%s</li>" % x for x in items))
    return o + '</div>'

def plural():
    return '<div class="ef">' + "".join('<div><b>%s</b><span class="small">%s</span></div>' % (a, b) for a, b in B.PLURAL) + '</div>'

def enganan():
    o = '<div class="eng">'
    for t, gs, why in B.ENGANAN:
        o += '<div class="box"><h4>%s</h4><p class="ex">%s</p><p class="small muted" style="margin:0">%s</p></div>' % (t, " · ".join(mk(g) for g in gs), why)
    return o + '</div>'

def tabla_pos():
    rows = [("yo", "mi", "mis", "mío, mía, míos, mías"), ("tú", "tu", "tus", "tuyo, tuya, tuyos, tuyas"),
            ("él, ella, usted", "su", "sus", "suyo, suya, suyos, suyas"), ("nosotros, nosotras", "nuestro · nuestra", "nuestros · nuestras", "nuestro, nuestra..."),
            ("vosotros, vosotras", "vuestro · vuestra", "vuestros · vuestras", "vuestro, vuestra..."), ("ellos, ellas, ustedes", "su", "sus", "suyo, suya, suyos, suyas")]
    o = '<div class="tw"><table class="t"><thead><tr><th>¿De quién?</th><th>una cosa</th><th>varias cosas</th><th>sin nombre detrás</th></tr></thead><tbody>'
    for a, b, c, d in rows: o += '<tr><td>%s</td><td><b class="pw">%s</b></td><td><b class="pw">%s</b></td><td class="small">%s</td></tr>' % (a, b, c, d)
    return o + '</tbody></table></div>'

def su_trampa():
    o = '<div class="sut">'
    for q, n, g, m, why in B.SU_TRAMPA:
        o += '<div class="box">%s<p class="small" style="margin:4px 0 0">%s</p></div>' % (su_svg(q, n, g, m), why)
    return o + '</div>'

def tonicos():
    o = '<div class="ton">'
    for a, b in B.TONICOS:
        o += '<div class="tn"><div><small>CON EL NOMBRE</small>%s</div><div class="arr" aria-hidden="true">→</div><div><small>SIN EL NOMBRE</small>%s</div></div>' % (mk(a), mk(b))
    return o + '</div>'

def donde():
    return "".join('<div class="box"><span class="chip">%s</span><p class="small muted" style="margin:6px 0">%s</p><p style="margin:0">%s</p></div>' % (c, d, mk(s)) for c, d, s in B.DONDE)

def errores():
    o = '<div class="errs">'
    for mal, bien, why in B.ERRORES:
        o += '<div class="err"><div class="mal"><span aria-hidden="true">✗</span> <s>%s</s></div><div class="bien"><span aria-hidden="true">✓</span> %s</div><div class="small muted">%s</div></div>' % (mal, mk(bien), why)
    return o + '</div>'

LEG = ('<div class="legend"><span><span class="g m s">masculino · uno</span></span><span><span class="g f s">femenino · uno</span></span>'
       '<span><span class="g m p">masculino · varios</span></span><span><span class="g f p">femenino · varios</span></span>'
       '<span><b class="cap">nombre</b> = el capitán</span></div>')

CSS_R = CSS + r"""
:root{--gm:#17707F;--gm-soft:#DDF0F2;--gf:#6B3FA0;--gf-soft:#EFE7F8;--ps:#1D5FA8;--ps-soft:#E2ECF8}
.g{border-radius:4px;padding:0 3px 1px;border-bottom:3px solid;line-height:1.9}
.g.m{background:var(--gm-soft);border-color:var(--gm)}.g.f{background:var(--gf-soft);border-color:var(--gf)}
.g.p{border-bottom-style:double;border-bottom-width:5px}
b.cap{text-decoration:underline;text-underline-offset:3px}
.pw{color:var(--ps)}
.cams{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}
.cam{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;border-top:6px solid var(--gm)}
.cam.c2{border-top-color:var(--gf)}.cam.c3{border-top-color:var(--ps)}
.cam .k{font-size:.78rem;font-weight:700;letter-spacing:.06em;color:var(--muted)}
.cam h3{margin:2px 0 6px}.cam p{margin:0;font-size:.95rem}
.cam .ej{margin-top:8px;font-size:.92rem;background:var(--paper);border-radius:8px;padding:6px 10px}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.box h4{margin:0 0 4px}.box .ex{margin:4px 0 6px}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.pill{font:inherit;font-size:.92rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:5px 14px;cursor:pointer}
.pill.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pill.ok{border-color:var(--ok)}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.duo button{font:inherit;text-align:left;border:2px solid var(--line);background:#fff;border-radius:10px;padding:10px 12px;cursor:pointer;line-height:1.6}
.duo button.on.ok{border-color:var(--ok);background:var(--ok-soft)}.duo button.on.no{border-color:var(--bad);background:var(--bad-soft)}
.duo button small{display:block;font-size:.75rem;font-weight:700;letter-spacing:.05em;color:var(--muted);margin-bottom:2px}
svg.dg{width:100%;height:auto;display:block;margin:6px 0}
.cam svg.ic{width:100%;max-width:260px;height:auto;display:block;margin:6px auto 10px}
.expl{border-radius:8px;padding:10px 14px;margin-top:6px}
.expl.ok{background:var(--ok-soft)}.expl.no{background:var(--bad-soft)}
.ef{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:22px}
.ef div{background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:.95rem}
.ef div b{display:block;margin-bottom:2px}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;margin:8px 0}
.mk3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:22px}
.mk3>div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:.93rem;border-top:5px solid var(--gm)}
.mk3 .v1{border-top-color:var(--amb)}.mk3 .v2{border-top-color:var(--muted)}
.mk3 h4{margin:0 0 6px}.mk3 ul{margin:0;padding-left:1.1em}.mk3 li{margin:3px 0}
.eng{display:grid;grid-template-columns:1fr 1fr;gap:0 12px}
.eng .box{margin:8px 0}
.tw{overflow-x:auto}
.cons{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0}
.cons .lbl{font-size:.78rem;font-weight:700;letter-spacing:.05em;color:var(--muted);margin:6px 0 4px}
.res{font-family:Georgia,serif;font-size:2rem;font-weight:700;text-align:center;margin:6px 0}
.res .r{color:var(--ps)}.res .e.m{color:var(--gm)}.res .e.f{color:var(--gf)}
.res2{text-align:center;font-size:1.05rem;margin:0 0 8px}
.why2{background:var(--paper);border-radius:8px;padding:8px 12px;font-size:.93rem}
.sut{display:grid;grid-template-columns:1fr 1fr;gap:0 12px}
.sut .box{margin:8px 0}.sut svg.ic{width:100%;max-width:300px;height:auto;display:block;margin:0 auto}
.ton{margin:10px 0 22px}
.tn{display:grid;grid-template-columns:1fr auto 1fr;gap:8px;align-items:stretch;margin:8px 0}
.tn>div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 12px;font-size:.95rem}
.tn small{display:block;font-size:.72rem;font-weight:700;letter-spacing:.06em;color:var(--muted)}
.tn .arr{border:0;background:none;display:grid;place-items:center;font-size:1.4rem;padding:0}
.errs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.err{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.err .mal{color:var(--bad)}.err .bien{margin:4px 0}
.chip{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin-right:6px;vertical-align:1px}
.vchip{display:inline-block;font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 8px;margin-left:4px}
.vchip.nom{background:var(--gm-soft);color:var(--gm)}.vchip.pos{background:var(--ps-soft);color:var(--ps)}
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
.clock{font-family:Georgia,serif;font-size:1.6rem;font-weight:700;font-variant-numeric:tabular-nums}
.tbar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:8px 0}
.tbar i{display:block;height:100%;background:var(--coral);width:0;transition:width .25s linear}
.esc{display:grid;gap:6px;margin:8px 0}
.esc div{border:2px dashed var(--line);border-radius:8px;padding:6px 10px;color:var(--muted);font-size:.95rem}
.esc div.on{border-style:solid;border-color:var(--coral);color:var(--ink);background:var(--coral-soft)}
.words{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}
.words span{font-size:.85rem;background:var(--gm-soft);color:var(--gm);border-radius:999px;padding:2px 10px}
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
#v-resumen{display:none}
@media (max-width:760px){.ophoto{grid-template-columns:1fr}}
@media (max-width:700px){.cams,.mk3,.errs,.eng,.sut,.ef,.cons{grid-template-columns:1fr}.duo{grid-template-columns:1fr}.tn{grid-template-columns:1fr}.tn .arr{transform:rotate(90deg);padding:2px}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff;font-size:13px}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}.box,.cam,.mk3>div,.err,.tn{break-inside:avoid}}
"""

STEPS = [("idea", "La idea"), ("posesivos", "Los posesivos"), ("examen", "En el examen"), ("practica", "Practica"),
         ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_IDEA = """
<h2>El nombre manda</h2>
<p class="lead">Imagina un equipo. El <b>nombre</b> es el capitán y lleva una camiseta con dos datos: <b>masculino o femenino</b> y <b>uno o varios</b>. Todo lo que va con él se pone <b>la misma camiseta</b>. Un error de concordancia es alguien del equipo con la camiseta de otro.</p>
__CARDS__
__LEG__
<h3>Mira el equipo</h3>
<p class="muted small">Elige un equipo y toca las dos frases: la buena y la que tiene un error. Mira las camisetas.</p>
<div class="pills" id="eqsel"></div>
<div class="box" id="eqvis"></div>
<h3>¿Quién se pone la camiseta?</h3>
<p>No todas las palabras cambian igual. Mira qué cambia y qué no.</p>
__VISTE__
<h3>Varios: cómo se hace el plural</h3>
__PLURAL__
<h3>Capitanes que engañan</h3>
<p>Casi siempre, -o es masculino y -a es femenino. Pero algunos capitanes llevan una camiseta que no esperas. Apréndelos <b>con su artículo</b>: así ves su camiseta.</p>
__ENGANAN__
<div class="tip"><b>El truco:</b> antes de escribir un adjetivo, mira hacia atrás y busca a su capitán. «Mi madre es... ¿madre? femenino: alt<b>a</b>». «Tiene el pelo... ¿pelo? masculino: rubi<b>o</b>».</div>
<div class="row"><button class="btn" data-act="printres">Imprimir el resumen</button><button class="btn cta" data-go="posesivos">Siguiente: los posesivos</button></div>
"""

V_POS = """
<h2>El posesivo mira a la cosa</h2>
<p class="lead">Un posesivo contesta a <b>dos preguntas</b>. <b>¿De quién es?</b> elige la palabra: mi, tu, su, nuestr-, vuestr-. <b>¿Qué cosa es?</b> le pone la camiseta: uno o varios y, con nuestro y vuestro, también masculino o femenino. El dueño no decide el final: <b>la cosa</b>, sí.</p>
__DOS__
<h3>Constrúyelo tú</h3>
<p class="muted small">Elige el dueño y la cosa. Mira de dónde sale cada parte.</p>
<div class="cons"><div><div class="lbl">1. ¿DE QUIÉN ES?</div><div class="pills" id="dusel"></div></div><div><div class="lbl">2. ¿QUÉ COSA ES?</div><div class="pills" id="cosel"></div></div></div>
<div class="box" id="convis" aria-live="polite"></div>
<h3>Todos los posesivos</h3>
__TABLA__
<h3>La trampa de su y sus</h3>
<p><b>Su</b> sirve para él, ella, usted, ellos, ellas y ustedes. Por eso muchos piensan: «son dos personas, entonces sus». ¡No! Cuenta <b>las cosas</b>, no las personas.</p>
__SUT__
<h3>Sin nombre detrás: el mío, la tuya</h3>
<p>Cuando no repites el nombre, usas la forma larga: <b>el mío, la tuya, los nuestros, es suya</b>. El nombre se va, pero <b>su camiseta se queda</b>: si hablas de una casa, «la mía»; de unos libros, «los míos». Después de <i>ser</i>, sin artículo: «Es mío».</p>
__TON__
<div class="note">Con las partes del cuerpo y la ropa que llevas puesta, en español casi siempre usamos el artículo y no el posesivo: <i>me duele <b>la</b> cabeza</i>, <i>se pone <b>la</b> chaqueta</i>.</div>
<div class="row"><button class="btn cta" data-go="examen">Siguiente: en el examen</button></div>
"""

V_EXAMEN = """
<h2>Dónde sale en el examen</h2>
<p class="lead">La concordancia y los posesivos están en todas las tareas donde describes a alguien o algo: la foto, tu familia, una persona importante, un piso, una biografía. Son errores pequeños, pero se repiten mucho y el examinador los ve en cada frase.</p>
__LEG__
__DONDE__
<h3>Los errores más típicos</h3>
<p>Tienes que reconocerlos en tus textos. Mira por qué fallan: en todos hay una palabra con la camiseta de otro equipo.</p>
__ERRORES__
<div class="tip"><b>Para la revisión final (5 minutos):</b> busca cada <b>mis / tus / sus / nuestros</b> y cada adjetivo de ropa o de carácter, y mira a su capitán. Es la pasada 5 de la lista de revisión.</div>
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACT = """
<h2>Practica</h2>
<p class="lead">Cuatro ejercicios. Cada respuesta se corrige en el momento, con la explicación.</p>
<div class="pills" id="exsel">
 <button class="pill on" data-act="ex" data-k="p1">1. ¿Qué camiseta lleva?</button>
 <button class="pill" data-act="ex" data-k="p2">2. Los posesivos</button>
 <button class="pill" data-act="ex" data-k="e2">3. Textos del examen</button>
 <button class="pill" data-act="ex" data-k="e4">4. ¿Bien o mal?</button>
</div>
<p class="muted small" id="exinfo"></p>
<div id="exbox"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

V_AHORA = """
<h2>Ahora tú</h2>
<p class="lead">Ahora úsalo en una tarea del examen: escribe un texto o describe a las personas de una foto en voz alta.</p>
<div class="pills" id="atsel">
 <button class="pill on" data-act="at" data-k="w">Escritura</button>
 <button class="pill" data-act="at" data-k="o">Oral: describe a las personas</button>
</div>
<div id="atw">
 <p>Elige una lámina. Escribe tu texto y después pulsa <b>Revisar concordancia y posesivos</b>: la página busca los errores típicos (mis amigo, la problema, la gente son, nuestro casa...). No corrige el texto entero: eso lo hace tu profesora.</p>
 <div class="pills" id="lamsel"></div>
 <div id="lambox"></div>
</div>
<div id="ato" hidden>
 <p>Como la primera pregunta de la tarea 2 de la oral: <b>¿cómo son las personas?</b> y <b>¿qué ropa llevan?</b> Un minuto para cada pregunta. Habla en voz alta y, en cada adjetivo, mira a su capitán.</p>
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
  <label><input type="radio" name="o1" value="El equipo y las camisetas">El equipo y las camisetas</label>
  <label><input type="radio" name="o1" value="Los posesivos (dos preguntas)">Los posesivos (dos preguntas)</label>
  <label><input type="radio" name="o1" value="En el examen y los errores típicos">En el examen y los errores típicos</label>
  <label><input type="radio" name="o1" value="Practica">Practica</label>
  <label><input type="radio" name="o1" value="Ahora tú">Ahora tú</label>
 </div>
 <label class="q" id="o2l">2. ¿Qué te cuesta más ahora?</label>
 <div class="chips" role="group" aria-labelledby="o2l">
  <label><input type="radio" name="o2" value="Masculino o femenino">Masculino o femenino</label>
  <label><input type="radio" name="o2" value="El plural (-s)">El plural (-s)</label>
  <label><input type="radio" name="o2" value="Los nombres que engañan">Los nombres que engañan</label>
  <label><input type="radio" name="o2" value="Su o sus / nuestro o nuestra">Su o sus / nuestro o nuestra</label>
  <label><input type="radio" name="o2" value="El mío, la tuya">El mío, la tuya</label>
 </div>
 <label class="q" id="o3l">3. ¿Te ayuda pensar en «el capitán y su camiseta»?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No mucho">No mucho</label>
 </div>
 <label class="q" for="o4">4. ¿Hay algo que no has entendido o que falta?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. ¿Cuánto control sientes ahora con la concordancia y los posesivos? (1 = nada, 10 = total)</label>
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
    o = '<h2>Concordancia y posesivos · resumen</h2>' + cards() + LEG
    o += '<h3>¿Quién se pone la camiseta?</h3>' + viste()
    o += '<h3>Capitanes que engañan</h3>' + enganan()
    o += '<h3>Los posesivos</h3>' + dos_preguntas() + tabla_pos()
    o += '<h3>Los errores típicos</h3>' + errores()
    return o

views = {
    "idea": V_IDEA.replace("__CARDS__", cards()).replace("__LEG__", LEG).replace("__VISTE__", viste()).replace("__PLURAL__", plural()).replace("__ENGANAN__", enganan()),
    "posesivos": V_POS.replace("__DOS__", dos_preguntas()).replace("__TABLA__", tabla_pos()).replace("__SUT__", su_trampa()).replace("__TON__", tonicos()),
    "examen": V_EXAMEN.replace("__LEG__", LEG).replace("__DONDE__", donde()).replace("__ERRORES__", errores()),
    "practica": V_PRACT, "ahora": V_AHORA, "opinion": V_OPINION.replace("__EMAIL__", EMAIL),
}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
VIEWS_HTML += '\n<section class="view" id="v-resumen">' + resumen() + '</section>'

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Ficha de remedio R04</small></div>
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
    "motivos": {k: {"f": v[0], "w": v[1]} for k, v in B.MOTIVOS.items()},
    "familias": B.FAMILIAS,
    "equipos": [{"tema": e["tema"], "bien": mk(e["bien"]), "mal": " ".join(w.lstrip("^") for w, _ in e["mal"]),
                 "db": team_bien(e), "dm": team_mal(e), "rb": e["rb"], "rm": e["rm"]} for e in B.EQUIPOS],
    "duenos": B.DUENOS, "cosas": B.COSAS, "lab": LAB,
    "qz": {
        "p1": {"items": B.P_FORMA, "n": 8, "name": "¿Qué camiseta lleva?", "three": True, "info": "Busca al capitán (el nombre) y elige la palabra que lleva su camiseta."},
        "p2": {"items": B.P_POS, "n": 8, "name": "Los posesivos", "three": True, "info": "Dos preguntas: ¿de quién es? (la palabra) y ¿qué cosa es? (el final)."},
        "e4": {"items": B.E_BIENMAL, "n": 8, "name": "¿Bien o mal?", "bm": True, "info": "Errores típicos de los exámenes. ¿La frase está bien o mal?"},
    },
    "textos": B.TEXTOS,
    "laminas": B.LAMINAS, "focos": B.FOCOS, "detector": B.DETECTOR, "pruebas": B.DETECTOR_PRUEBAS,
    "fotos": [{"id": f["id"], "titulo": f["titulo"], "alt": f["alt"], "img": IMG_T2 % f["id"], "como": mk(f["como"]), "ropa": mk(f["ropa"])} for f in B.FOTOS],
}

JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function blank(){ return {cur:'idea', seen:{}, eq:0, ev:'b', du:'nos', co:1, ex:'p1', etext:D.textos[0].id, at:'w',
  qz:{}, qlog:{}, cz:{}, w:{}, wchk:{}, wrev:{}, lam:D.laminas[0].id, foto:D.fotos[0].id, fph:{}, fchk:{}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }

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

/* ---------------- 1. la idea: equipos ---------------- */
function renderEq(){
 var o=''; D.equipos.forEach(function(e,i){ o+='<button class="pill'+(S.eq===i?' on':'')+'" data-act="eq" data-i="'+i+'">'+esc(e.tema)+'</button>'; });
 $('eqsel').innerHTML=o;
 var e=D.equipos[S.eq], m=S.ev;
 $('eqvis').innerHTML='<div class="duo">'+
  '<button class="ok'+(m==='b'?' on':'')+'" data-act="ev" data-m="b" aria-pressed="'+(m==='b')+'"><small>✓ TODO EL EQUIPO IGUAL</small>'+e.bien+'</button>'+
  '<button class="no'+(m==='m'?' on':'')+'" data-act="ev" data-m="m" aria-pressed="'+(m==='m')+'"><small>✗ CON UN ERROR</small><s>'+esc(e.mal)+'</s></button></div>'+
  (m==='b'?e.db:e.dm)+'<div class="expl '+(m==='b'?'ok':'no')+'" aria-live="polite">'+(m==='b'?e.rb:e.rm)+'</div>';
}

/* ---------------- 2. posesivos: constructor ---------------- */
var END={ms:'o',fs:'a',mp:'os',fp:'as'}, ART={ms:'el',fs:'la',mp:'los',fp:'las'};
function svgPerson(x,y){ return '<circle cx="'+x+'" cy="'+y+'" r="12" fill="#fff" stroke="#14161C" stroke-width="2.5"/><path d="M'+(x-20)+','+(y+40)+' q20,-30 40,0" fill="#fff" stroke="#14161C" stroke-width="2.5"/>'; }
function svgThing(x,y,col,soft){ var P=[[-17,-13],[-7,-16],[0,-12],[7,-16],[17,-13],[24,-3],[16,1],[16,16],[-16,16],[-16,1],[-24,-3]]; return '<path d="M'+P.map(function(p){return (x+p[0])+','+(y+p[1]);}).join(' L')+' Z" fill="'+soft+'" stroke="'+col+'" stroke-width="2.5" stroke-linejoin="round"/>'; }
function renderCon(){
 var o=''; D.duenos.forEach(function(d){ o+='<button class="pill'+(S.du===d.id?' on':'')+'" data-act="du" data-id="'+d.id+'">'+esc(d.lab)+'</button>'; }); $('dusel').innerHTML=o;
 o=''; D.cosas.forEach(function(c,i){ o+='<button class="pill'+(S.co===i?' on':'')+'" data-act="co" data-i="'+i+'">'+esc(c.w)+'</button>'; }); $('cosel').innerHTML=o;
 var d=D.duenos.filter(function(x){return x.id===S.du;})[0], c=D.cosas[S.co], pl=c.t.charAt(1)==='p', fem=c.t.charAt(0)==='f';
 var ending = d.tipo==='gen' ? END[c.t] : (pl?'s':'');
 var col=fem?'#6B3FA0':'#17707F', soft=fem?'#EFE7F8':'#DDF0F2';
 var sv='<svg class="dg" viewBox="0 0 640 120" role="img" aria-label="'+esc(d.lab+' y '+c.w)+'">';
 for(var i=0;i<d.n;i++) sv+=svgPerson(50+i*44,28);
 var nt=pl?2:1; for(var j=0;j<nt;j++) sv+=svgThing(566+j*44-(nt-1)*22,56,col,soft);
 sv+='<line x1="'+(80+(d.n-1)*44)+'" y1="58" x2="230" y2="58" stroke="#1D5FA8" stroke-width="3"/><polygon points="230,50 244,58 230,66" fill="#1D5FA8"/>';
 sv+='<text x="190" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="#1D5FA8">¿De quién? → '+esc(d.raiz)+(d.tipo==='gen'?'-':'')+'</text>';
 sv+='<line x1="'+(530-(nt-1)*24)+'" y1="58" x2="410" y2="58" stroke="'+col+'" stroke-width="3"/><polygon points="410,50 396,58 410,66" fill="'+col+'"/>';
 sv+='<text x="450" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="'+col+'">¿Qué cosa? → '+(ending?'-'+ending:'nada')+'</text>';
 sv+='<text x="320" y="110" text-anchor="middle" font-size="13" fill="#5E5A55">'+esc(D.lab[c.t])+'</text></svg>';
 var h=sv+'<div class="res"><span class="r">'+esc(d.raiz)+'</span><span class="e '+(fem?'f':'m')+'">'+esc(ending)+'</span> '+esc(c.w)+'</div>';
 h+='<p class="res2">Sin el nombre: <b>'+ART[c.t]+' '+esc(d.ton)+'<span class="e">'+END[c.t]+'</span></b> · después de ser: '+(pl?'son':'es')+' <b>'+esc(d.ton)+END[c.t]+'</b></p>';
 var why = d.tipo==='gen'
  ? 'Con <b>'+esc(d.lab)+'</b> la palabra es <b>'+d.raiz+'-</b> y la cosa le pone las dos cosas de su camiseta: '+(fem?'femenino':'masculino')+' y '+(pl?'varios':'uno')+'.'
  : 'Con <b>'+esc(d.lab)+'</b> la palabra es <b>'+d.raiz+'</b>. Esta palabra no cambia de masculino a femenino: solo mira si la cosa es '+(pl?'<b>varios</b> → -s.':'<b>una</b> → sin -s.');
 if(d.id==='ellos' && !pl) why+=' Son varios dueños, pero <b>una</b> cosa: '+d.raiz+'.';
 if(d.id==='el' && pl) why+=' Un dueño, pero <b>varias</b> cosas: '+d.raiz+'s.';
 $('convis').innerHTML=h+'<div class="why2">'+why+'</div>';
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
 var q=it.q;
 if(ans && !c.bm){ var parts=it.o[0].split(' / '), pi=0; q=q.replace(/____/g, function(){ var p=parts[Math.min(pi,parts.length-1)]; pi++; return '<b style="color:var(--ok)">'+esc(p)+'</b>'; }); }
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
var EXINFO={e2:'Textos como los del examen: la descripción de una foto, dos correos y una biografía. Elige la palabra de cada hueco: la corrección sale enseguida, con el motivo.'};
function renderEx(){
 var ps=$('exsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.ex);
 $('exinfo').textContent = D.qz[S.ex] ? D.qz[S.ex].info : EXINFO[S.ex];
 if(S.ex==='e2') renderE2(); else qzRender(S.ex, $('exbox'));
}

/* ---------------- ahora tu: escritura ---------------- */
function lam(){ return D.laminas.filter(function(l){return l.id===S.lam;})[0]; }
var CH=['He buscado el capitán de cada adjetivo (ropa, físico, carácter) y lleva su camiseta.','Con varios (amigos, padres, personas), todo el equipo lleva -s.','Los posesivos miran a la cosa: mi casa / mis casas · nuestra casa / nuestro piso.','No he escrito «la gente son» ni «las gente».','He mirado los nombres que engañan: el problema, el día, la foto, la mano.'];
function renderLam(){
 var o=''; D.laminas.forEach(function(l){ o+='<button class="pill'+(S.lam===l.id?' on':'')+'" data-act="lam" data-id="'+l.id+'">'+esc(l.tarea)+'</button>'; }); $('lamsel').innerHTML=o;
 var L=lam(), h='<div class="lam"><div class="h">'+esc(L.tarea.toUpperCase())+'</div>';
 if(L.intro) h+='<p style="margin:6px 0 0">'+esc(L.intro)+'</p><div class="msg">'+esc(L.mensaje)+'</div>';
 h+='<p style="margin:8px 0 2px">'+esc(L.consigna)+'</p><ul>';
 L.pautas.forEach(function(p){ h+='<li>'+esc(p[0])+p[1].map(function(f){ return '<span class="vchip '+(f==='pos'?'pos':'nom')+'">'+D.focos[f]+'</span>'; }).join('')+'</li>'; });
 h+='</ul><p class="small" style="margin:6px 0 0"><b>Número de palabras:</b> entre '+L.palabras[0]+' y '+L.palabras[1]+'.</p></div>';
 h+='<p class="muted small">Las etiquetas de color te dicen qué pide cada pauta. Recuerda: unas 10 palabras por línea (entre '+Math.round(L.palabras[0]/10)+' y '+Math.round(L.palabras[1]/10)+' líneas escritas a mano).</p>';
 h+='<label for="wtext"><b>Tu texto</b></label><textarea class="wr" id="wtext" spellcheck="false">'+esc(S.w[L.id]||'')+'</textarea>';
 h+='<div class="row"><button class="btn cta" data-act="review">Revisar concordancia y posesivos</button></div><div id="rvbox" aria-live="polite"></div>';
 h+='<h3>Mi lista de concordancia y posesivos</h3><ul class="check">'; CH.forEach(function(c,i){ var k=L.id+i; h+='<li><label><input type="checkbox" data-wchk="'+k+'"'+(S.wchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
 $('lambox').innerHTML=h;
}
function norm(s){ return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase(); }
function detect(s){ var n=norm(s), out=[]; D.detector.forEach(function(d){ var r=new RegExp(d.re,'g'), m; while((m=r.exec(n))){ out.push({d:d, a:m.index, w:m[0]}); if(r.lastIndex===m.index) r.lastIndex++; } }); return out; }
window.__R04detect = function(s){ var ids={}; detect(s).forEach(function(x){ ids[x.d.id]=1; }); return Object.keys(ids).sort(); };
function review(){
 var L=lam(), txt=$('wtext').value, out=[], red=0;
 if(txt.trim().length<20){ $('rvbox').innerHTML='<ul class="rv"><li class="a">Escribe primero tu texto.</li></ul>'; return; }
 var sents=txt.match(/[^.!?\n]+[.!?]*/g)||[];
 sents.forEach(function(s){
  if(!s.trim()) return;
  detect(s).forEach(function(x){
   if(x.d.t==='r') red++;
   var hl=esc(s.slice(0,x.a))+'<mark>'+esc(s.substr(x.a,x.w.length))+'</mark>'+esc(s.slice(x.a+x.w.length));
   out.push('<li class="'+x.d.t+'">'+(x.d.t==='r'?'<b>¡Ojo!</b> ':'<b>Mira esto:</b> ')+x.d.msg+'<br><span class="small">'+hl+'</span></li>');
  });
 });
 var nt=norm(txt), np=(nt.match(/\b(mi|mis|tu|tus|su|sus|nuestro|nuestra|nuestros|nuestras|vuestro|vuestra|vuestros|vuestras)\b/g)||[]).length;
 var pidePos=L.pautas.some(function(p){ return p[1].indexOf('pos')>=0; });
 if(pidePos && np<2) out.push('<li class="a"><b>Posesivos:</b> casi no los has usado. La lámina habla de tu familia o de tu casa: «mi hermana», «nuestro piso», «sus hijos».</li>');
 if(!red) out.unshift('<li class="g">No he encontrado los errores típicos. ¡Bien! Has usado '+np+' '+(np===1?'posesivo':'posesivos')+'. Mira tú también cada adjetivo con la lista de abajo.</li>');
 var wc=txt.trim().split(/\s+/).length;
 S.wrev[L.id]={red:red, amb:out.filter(function(x){return x.indexOf('class="a"')>=0;}).length, pos:np, words:wc}; save();
 $('rvbox').innerHTML='<h3>Qué mirar</h3><ul class="rv">'+out.join('')+'</ul><p class="muted small">Tu texto: '+wc+' palabras (la lámina pide '+L.palabras[0]+'-'+L.palabras[1]+'). La página solo busca estos errores: no los ve todos. Tu profesora corrige el texto completo.</p>';
}

/* ---------------- ahora tu: oral (foto) ---------------- */
var TM=null, T0=0, TDUR=60;
function stopTimer(){ if(TM){ clearInterval(TM); TM=null; } }
var ESC={1:['0 s · Empieza: «En la foto hay...». Cuenta: un hombre, dos mujeres, unos niños.','20 s · El físico: «es alto / alta», «tiene el pelo largo», «tiene unos cuarenta años».','40 s · El carácter: «parece simpático / simpática», «parecen contentos / contentas».'],
         2:['0 s · Lleva + un / una / unos / unas: «lleva una camiseta», «lleva unas gafas».','20 s · Añade el color con la camiseta del nombre: «un abrigo rojo», «una bufanda roja», «unos zapatos negros».','40 s · Compara: «los dos llevan...», «la otra mujer lleva...», «nadie lleva...».']};
var WORDS={1:['alto / alta','bajo / baja','delgado / delgada','joven / jóvenes','mayor / mayores','moreno / morena','rubio / rubia','el pelo largo / corto / rizado','parece simpático / simpática','contento / contenta'],
           2:['un abrigo','una chaqueta','un jersey','una camiseta','una camisa','un vestido','unos pantalones','unos vaqueros','unas gafas','unas zapatillas','blanco / blanca','negro / negra','rojo / roja','azul / azules','verde / verdes','gris / grises']};
var FCH=['He empezado con «En la foto hay...».','Cada adjetivo mira a su capitán: la chica alta, el chico alto.','Con varias personas: «parecen contentos / contentas».','En la ropa, el color lleva la camiseta de la prenda: una camiseta blanca, un abrigo negro.','He usado «lleva» + un / una / unos / unas.'];
function foto(){ return D.fotos.filter(function(f){return f.id===S.foto;})[0]; }
function renderFoto(){
 var o=''; D.fotos.forEach(function(f){ var d=(S.fph[f.id]||0)>=3; o+='<button class="pill'+(S.foto===f.id?' on':'')+(d?' ok':'')+'" data-act="foto" data-id="'+f.id+'">'+esc(f.titulo)+(d?' ✓':'')+'</button>'; });
 $('fosel').innerHTML=o;
 var f=foto(), ph=S.fph[f.id]||0;
 var h='<div class="ophoto"><figure class="ph" id="fig"><img src="'+f.img+'" alt="'+esc(f.alt)+'" loading="lazy"><div class="alt"><b>Foto:</b> '+esc(f.alt)+'</div><figcaption>'+esc(f.titulo)+'</figcaption></figure><div class="ocard">';
 if(ph===0){
  h+='<div class="ph1">Prepárate</div><p>Mira la foto unos segundos. Vas a hablar <b>dos minutos</b>: uno para decir cómo son las personas y otro para decir qué ropa llevan.</p><p class="small"><b>Palabras útiles:</b></p><div class="words">'+WORDS[1].concat(WORDS[2].slice(0,6)).map(function(x){return '<span>'+esc(x)+'</span>';}).join('')+'</div>';
  h+='<div class="row"><button class="btn cta" data-act="fgo" data-p="1">Empezar: cómo son (1 min)</button></div>';
 } else if(ph<3){
  h+='<div class="ph1">'+(ph===1?'1. ¿Cómo son?':'2. ¿Qué ropa llevan?')+'</div>';
  h+='<div class="clock" id="fclk" aria-live="off">1:00</div><div class="tbar"><i id="tbar"></i></div><div class="esc" id="esc">'+ESC[ph].map(function(x){return '<div>'+x+'</div>';}).join('')+'</div>';
  h+='<div class="words">'+WORDS[ph].map(function(x){return '<span>'+esc(x)+'</span>';}).join('')+'</div>';
  h+='<div class="row"><button class="btn" data-act="fstart" id="fbtn">Empezar el reloj</button><button class="btn cta" data-act="fgo" data-p="'+(ph+1)+'">'+(ph===1?'Siguiente: la ropa':'He terminado')+'</button></div>';
 } else {
  h+='<div class="ph1">¿Qué tal ha ido?</div><ul class="check">'; FCH.forEach(function(c,i){ var k=f.id+'-'+i; h+='<li><label><input type="checkbox" data-fchk="'+k+'"'+(S.fchk[k]?' checked':'')+'> '+c+'</label></li>'; }); h+='</ul>';
  h+='<div class="model"><b>Una descripción modelo: cómo son</b><br>'+f.como+'</div><div class="model"><b>Y qué ropa llevan</b><br>'+f.ropa+'</div>';
  h+='<p class="small muted">Los colores muestran los equipos: cada palabra lleva la camiseta de su capitán (subrayado). En el examen, después sigues con las otras preguntas de la lámina. Practícalas en el taller de la foto.</p>';
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
  var left=Math.max(0,Math.ceil(TDUR-t)); ck.textContent=left===60?'1:00':'0:'+(left<10?'0':'')+left;
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
 var L=['CURSO DELE A2 - R04: CONCORDANCIA Y POSESIVOS','Nombre: '+(S.name||'-'),''];
 L.push('EJERCICIOS (ultimo resultado)');
 ['p1','p2','e4'].forEach(function(k){ var g=S.qlog[k]; L.push('- '+D.qz[k].name+': '+(g?g.last+(g.fails.length?' | fallos: '+g.fails.join(' / '):''):'sin hacer')); });
 D.textos.forEach(function(t){
  var f=fbList(t.id,t.texto), errs=[];
  gapInfo(t.id,t.texto).forEach(function(g){ var c=S.cz[g.gid]; if(c&&c.first!==g.ok) errs.push(g.n+': '+c.first+' -> '+g.ok); });
  var started=Object.keys(S.cz).some(function(k){return k.indexOf(t.id+'-')===0;});
  L.push('- Textos del examen, '+t.titulo+': '+(started?f.first+'/'+f.tot+' a la primera'+(f.done<f.tot?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 L.push('','ORAL: DESCRIBE A LAS PERSONAS (como son / que ropa llevan)');
 var fd=D.fotos.filter(function(f){ return (S.fph[f.id]||0)>=3; });
 if(!fd.length) L.push('sin hacer');
 fd.forEach(function(f){ var n=0; FCH.forEach(function(c,i){ if(S.fchk[f.id+'-'+i]) n++; }); L.push('- Foto '+f.id+' ('+f.titulo+'): hecha, autorrevision '+n+'/'+FCH.length); });
 D.laminas.forEach(function(l){
  var t=(S.w[l.id]||'').trim(); if(!t) return;
  var rv=S.wrev[l.id];
  L.push('','ESCRITURA - '+l.tarea.toUpperCase()+' ('+l.palabras[0]+'-'+l.palabras[1]+' palabras)','Pautas: '+l.pautas.map(function(p){return p[0];}).join(' '));
  if(rv) L.push('Revision: '+rv.red+' avisos rojos, '+rv.amb+' ambar | '+rv.pos+' posesivos | '+rv.words+' palabras');
  L.push('---', t, '---');
 });
 L.push('','OPINION','1. Lo que mas ayuda: '+(S.o1||'-'),'2. Lo que mas cuesta: '+(S.o2||'-'),'3. El capitan y su camiseta: '+(S.o3||'-'),'4. No he entendido / falta: '+(S.o4||'-'),'5. Control (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 eq:function(b){ S.eq=+b.getAttribute('data-i'); S.ev='b'; save(); renderEq(); },
 ev:function(b){ S.ev=b.getAttribute('data-m'); save(); renderEq(); },
 du:function(b){ S.du=b.getAttribute('data-id'); save(); renderCon(); },
 co:function(b){ S.co=+b.getAttribute('data-i'); save(); renderCon(); },
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
window.__R04pack = pack;
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

renderEq(); renderCon(); renderEx(); renderAt(); renderOpn(); go(S.cur);
})();
"""

DATA_JS = dict(DATA); DATA_JS.pop("pruebas", None)
js = JS.replace("__DATA__", json.dumps(DATA_JS, ensure_ascii=False))
html = page(TITLE + " · Preparación DELE A2", CSS_R, BODY, js)
html.encode("ascii")
open(FILE, "w", encoding="ascii").write(html)
print("ok", FILE, "| huecos:", sum(ngaps.values()),
      "| items:", len(B.P_FORMA) + len(B.P_POS) + len(B.E_BIENMAL),
      "| pruebas del detector:", len(B.DETECTOR_PRUEBAS), "| equipos:", len(B.EQUIPOS), "| fotos:", len(B.FOTOS))
