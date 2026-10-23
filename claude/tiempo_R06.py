# -*- coding: utf-8 -*-
# R06 PREPOSICIONES FRECUENTES: PESTANA "HACE Y DURANTE" (hace, desde, desde hace, durante, en + tiempo)
# Anadida el 14/10 (Maria: "lo dejamos ya arreglado" en la R06, en vez de una ficha R15 aparte).
# Contenidos, comprobaciones, HTML y JS de la pestana, todo aqui. build_R06_preposiciones.py lo usa con
# cinco lineas (las pone arreglar_R06_tiempo.py); el mismo script mete la pestana en el HTML ya subido.
#
# ENFOQUE COGNITIVO (sigue el mapa del viaje de la R06): LA LINEA DEL TIEMPO CON EL AHORA.
#   HACE + tiempo      = desde AHORA miras hacia atras hasta un punto: llegue hace dos anos (pasado).
#   DESDE + momento    = el punto donde EMPIEZA algo que sigue hasta ahora: vivo aqui desde 2024.
#   DESDE HACE + tiempo= la misma linea que llega hasta ahora, pero cuentas lo larga que es: vivo aqui
#                        desde hace dos anos (presente: todavia vives aqui).
#   DURANTE + tiempo   = un trozo CERRADO, con principio y final: vivi en Roma durante tres anos.
#   EN + tiempo        = la CAJA de lo que tardas: lo termine en una hora; llego en diez minutos.
# MARCAS (colores de la R06): [h:hace...] azul (la flecha hacia atras), [d:desde...] ambar (la linea),
#   [u:durante...] violeta, [n:en...] turquesa (la caja).
# Huecos: [[buena|d1|d2#motivo]]. Espanol de Espana. Ejemplos propios.
import json, os, re, shutil, subprocess, sys, tempfile, unicodedata

STORAGE = "dele-a2-curso-R06-tiempo"
STEP = ("tiempo", "Hace y durante")

MOTIVOS = {
    "hace": ("Miras hacia atrás desde hoy hasta un punto del pasado: <b>hace</b> + tiempo (llegué hace tres meses).", ["hace"]),
    "desde": ("El punto donde empieza algo que sigue hasta hoy, con una fecha o un momento: <b>desde</b> octubre, <b>desde</b> el verano.", ["desde"]),
    "desde_hace": ("Algo que empezó y sigue hasta hoy, y dices cuánto tiempo: <b>desde hace</b> + tiempo (desde hace dos semanas).", ["desde hace"]),
    "durante": ("Un trozo cerrado, con principio y final: <b>durante</b> + tiempo (durante cuatro años, y se terminó).", ["durante"]),
    "en": ("La caja de lo que tardas: <b>en</b> + tiempo (lo hago en media hora).", ["en"]),
}
VALIDAS = {"hace", "desde", "desde hace", "durante", "en"}
KIND = {"h": "hace", "d": "desde", "u": "durante", "n": "en"}   # marca -> palabra con la que empieza
CLS = {"h": "a", "d": "l", "u": "p", "n": "e"}                 # clases de color de la R06

# Tarjetas de la idea: (marca, titulo, explicacion, ejemplo marcado, tiempo verbal)
CARDS = [
    ("h", "HACE", "Desde hoy miras hacia atrás y cuentas hasta un punto.", "Llegué a Alicante [h:hace tres meses].", "con pasado: llegué, empecé, conocí"),
    ("d", "DESDE", "El punto donde empieza algo que sigue hasta hoy: una fecha, un mes, un día.", "Vivo en este piso [d:desde octubre].", "con presente: vivo, tengo, trabajo"),
    ("dh", "DESDE HACE", "La misma línea que llega hasta hoy, pero dices lo larga que es.", "Trabajo en una librería [d:desde hace dos semanas].", "con presente: todavía sigue"),
    ("u", "DURANTE", "Un trozo cerrado: tiene principio y final.", "Viví en Roma [u:durante tres años]; después volví.", "con pasado terminado: viví, estudié"),
    ("n", "EN", "La caja de lo que tardas en hacer algo.", "Hice el puzle [n:en una hora].", "lo que tardas: lo hice, llego"),
]
# Preguntas y respuestas
PREGUNTAS = [
    ("¿Cuándo llegaste a España?", "Llegué [h:hace un año]."),
    ("¿Desde cuándo vives aquí?", "Vivo aquí [d:desde 2025]. / Vivo aquí [d:desde hace un año]."),
    ("¿Cuánto tiempo estuviste en Roma?", "Estuve allí [u:durante tres años]. (También: «estuve tres años».)"),
    ("¿Cuánto tiempo tardas en llegar al trabajo?", "Llego [n:en veinte minutos]."),
    ("¿Cuánto tiempo hace que estudias español?", "Estudio español [d:desde hace un año]. (También: «hace un año que estudio».)"),
]
# Errores tipicos: (mal, bien marcado, porque)
ERRORES = [
    ("Vivo en Alicante desde dos años.", "Vivo en Alicante [d:desde hace dos años].", "Con una cantidad de tiempo (dos años) que llega hasta hoy: <b>desde hace</b>. <i>Desde</i> solo va con una fecha o un momento: desde 2024."),
    ("Llegué a España antes dos años.", "Llegué a España [h:hace dos años].", "Para mirar hacia atrás desde hoy, en español es <b>hace</b> + tiempo, delante."),
    ("Estudio español desde hace 2023.", "Estudio español [d:desde 2023].", "Con una fecha (2023, enero, el lunes) solo <b>desde</b>. <i>Desde hace</i> va con una cantidad: desde hace dos años."),
    ("Viví en Roma desde tres años.", "Viví en Roma [u:durante tres años].", "Es un trozo cerrado (ya no vives allí): <b>durante</b>."),
    ("Vivo aquí durante dos años.", "Vivo aquí [d:desde hace dos años].", "Todavía vives aquí: la línea llega hasta hoy. <i>Durante</i> es para un trozo cerrado."),
    ("Estudié español desde hace un año.", "Estudio español [d:desde hace un año].", "<i>Desde hace</i> dice que sigue hasta hoy: el verbo va en <b>presente</b>."),
]
# Opcion multiple: la PRIMERA es la buena
QUIZ = [
    {"q": "Llegué a Alicante ____ dos años.", "o": ["hace", "desde hace", "durante"], "why": "Miras hacia atrás desde hoy hasta el día que llegaste: <b>hace</b> + pasado."},
    {"q": "Vivo en Alicante ____ dos años.", "o": ["desde hace", "desde", "durante"], "why": "Todavía vives allí y dices cuánto tiempo: <b>desde hace</b>."},
    {"q": "Estudio español ____ 2024.", "o": ["desde", "desde hace", "hace"], "why": "Con una fecha, el punto donde empieza: <b>desde</b> 2024."},
    {"q": "Mi abuela vivió en Francia ____ diez años; después volvió a España.", "o": ["durante", "desde hace", "desde"], "why": "Un trozo cerrado: ya no vive allí. <b>Durante</b>."},
    {"q": "Terminé el examen ____ cuarenta minutos: era muy fácil.", "o": ["en", "desde", "desde hace"], "why": "Lo que tardaste: la caja, <b>en</b> cuarenta minutos."},
    {"q": "—¿Desde cuándo trabajas aquí? —____ el lunes.", "o": ["Desde", "Hace", "Durante"], "why": "El lunes es el punto donde empieza: <b>desde</b> el lunes."},
    {"q": "Tengo este móvil ____ tres meses y ya está roto.", "o": ["desde hace", "durante", "desde"], "why": "Todavía lo tienes: <b>desde hace</b> + cantidad de tiempo."},
    {"q": "Ana y Luis se conocieron ____ cinco años, en una boda.", "o": ["hace", "desde hace", "en"], "why": "Un punto del pasado contado desde hoy: <b>hace</b> cinco años."},
    {"q": "____ el verano trabajé en un hotel de la playa.", "o": ["Durante", "Desde hace", "Hace"], "why": "Todo el verano, un trozo cerrado: <b>durante</b>."},
    {"q": "Llego a tu casa ____ diez minutos: ya estoy en el autobús.", "o": ["en", "durante", "desde"], "why": "Lo que tardas en llegar: <b>en</b> diez minutos."},
    {"q": "No veo a mi primo ____ Navidad.", "o": ["desde", "desde hace", "durante"], "why": "Navidad es el momento donde empieza: <b>desde</b> Navidad."},
    {"q": "Estuve en el hospital ____ una semana.", "o": ["durante", "desde hace", "desde"], "why": "Una semana con principio y final, ya terminada: <b>durante</b>."},
    {"q": "Mis padres están casados ____ 1990.", "o": ["desde", "desde hace", "hace"], "why": "Con un año, el punto donde empieza: <b>desde</b> 1990."},
    {"q": "Pinté toda la habitación ____ una tarde.", "o": ["en", "desde", "desde hace"], "why": "Lo que tardaste: <b>en</b> una tarde."},
]
TEXTOS = [
    {"id": "t_valencia", "tipo": "Escritura · tarea 1 · correo a una amiga", "titulo": "Mi vida en Valencia",
     "texto": "¡Hola, Irene! ¿Qué tal? Te escribo desde Valencia: llegué aquí [[hace|desde hace|durante#hace]] tres meses. "
              "Vivo en un piso compartido [[desde|desde hace|hace#desde]] octubre y trabajo en una librería [[desde hace|desde|durante#desde_hace]] dos semanas. "
              "Antes estudié en Madrid [[durante|desde hace|desde#durante]] cuatro años. El trabajo me gusta: por la mañana abro la tienda y lo preparo todo [[en|durante|desde#en]] media hora. "
              "Te echo de menos: no te veo [[desde|desde hace|durante#desde]] el verano. ¿Vienes a verme? El tren llega [[en|desde|desde hace#en]] dos horas. Un abrazo, Elsa"},
    {"id": "t_curso", "tipo": "Oral · tarea 1 · monólogo: un curso que hice", "titulo": "Un curso que hice",
     "texto": "[[Hace|Desde hace|Durante#hace]] dos años hice un curso de fotografía en mi ciudad. "
              "Fui a clase [[durante|desde hace|desde#durante]] seis meses, todos los sábados por la mañana. "
              "El primer día aprendí a usar la cámara [[en|durante|desde#en]] una hora: ¡fue muy fácil! "
              "Ahora hago fotos de pájaros. Tengo una cámara nueva [[desde|desde hace|durante#desde]] el año pasado y "
              "salgo al campo los domingos [[desde hace|desde|durante#desde_hace]] un año. La semana que viene empiezo otro curso, de vídeo."},
]
# Detector: avisos que se anaden al de la R06 (sobre el texto sin tildes y en minusculas)
_CANT = r"(?:un|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|quince|veinte|muchos|muchas|pocos|pocas|varios|varias|algunos|algunas|\d+)"
_UNI = r"(?:anos|ano|meses|mes|semanas|semana|dias|dia|horas|hora|minutos|minuto)"
_MES = r"(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)"
DETECTOR = [
    {"id": "desde_cant", "t": "r", "re": r"\bdesde\s+" + _CANT + r"\s+" + _UNI + r"\b",
     "msg": "Con una cantidad de tiempo que llega hasta hoy se dice <b>desde hace</b>: vivo aquí desde hace dos años. (<i>Desde</i> solo, con una fecha: desde 2024.) Si ya terminó: <b>durante</b>."},
    {"id": "antes_cant", "t": "r", "re": r"\b(antes|atras)\s+" + _CANT + r"\s+" + _UNI + r"\b",
     "msg": "Para mirar hacia atrás desde hoy se dice <b>hace</b> + tiempo: llegué hace dos años."},
    {"id": "desde_hace_fecha", "t": "r", "re": r"\bdesde\s+hace\s+(?:(?:19|20)\d\d|" + _MES + r"|el\s+(?:lunes|martes|miercoles|jueves|viernes|sabado|domingo|verano|invierno))\b",
     "msg": "Con una fecha o un momento, solo <b>desde</b>: desde 2023, desde enero. <i>Desde hace</i> va con una cantidad: desde hace dos años."},
    {"id": "durante_sigue", "t": "a", "re": r"\b(vivo|vives|vive|vivimos|viven|estudio|estudias|estudia|estudiamos|estudian|tengo|tienes|tiene|tenemos|tienen)\s+(?:[a-z]+\s+){0,2}durante\s+" + _CANT + r"\s+" + _UNI + r"\b",
     "msg": "¿Todavía sigue hoy? Entonces es <b>desde hace</b> (vivo aquí desde hace dos años). <i>Durante</i> es para un trozo cerrado."},
]
PRUEBAS = [
    ("Vivo en Alicante desde dos años.", ["desde_cant"]),
    ("Viví en Roma desde tres años.", ["desde_cant"]),
    ("Llegué a España antes dos años.", ["antes_cant"]),
    ("Estudio español desde hace 2023.", ["desde_hace_fecha"]),
    ("No te veo desde hace enero.", ["desde_hace_fecha"]),
    ("Vivo aquí durante dos años.", ["durante_sigue"]),
    ("Vivo en Alicante desde hace dos años.", []),
    ("Estudio español desde 2023 y trabajo desde el lunes.", []),
    ("Llegué hace dos años; dos años antes vivía en Roma.", []),
    ("Viví en Roma durante tres años.", []),
    ("Lo terminé en una hora.", []),
    ("Hace dos años que vivo aquí.", []),
    ("Antes de las dos no puedo.", []),
    ("Trabajo durante el día y estudio por la noche.", []),
]

MARK = re.compile(r"\[(h|d|u|n):([^\[\]]+)\]")
GAP = re.compile(r"\[\[([^\]]+)\]\]")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
def mk(s): return MARK.sub(lambda m: '<span class="k %s">%s</span>' % (CLS[m.group(1)], m.group(2)), s)
def plain(s): return re.sub(r"<[^>]+>", "", MARK.sub(lambda m: m.group(2), s))
def filled(s): return re.sub(r"<[^>]+>", " ", GAP.sub(lambda m: m.group(1).split("#")[0].split("|")[0], s))

def extend(B):
    """Anade los avisos y las pruebas al detector de la R06 (antes de sus comprobaciones)."""
    have = {d["id"] for d in B.DETECTOR}
    for d in DETECTOR:
        if d["id"] not in have: B.DETECTOR.append(dict(d))
    for p in PRUEBAS:
        if p not in B.DETECTOR_PRUEBAS: B.DETECTOR_PRUEBAS.append(p)

def check(detector=None):
    """Comprueba el banco de la pestana. detector = lista completa {id,t,re} (la de la R06 + estos)."""
    E = []
    def chk_marks(s, where, need=1):
        rest = MARK.sub("", s)
        if "[" in rest or "]" in rest: E.append("marca mal cerrada en %s: %s" % (where, s))
        gs = MARK.findall(s)
        for k, b in gs:
            w = norm(b)
            want = "desde" if k == "d" else norm(KIND[k])
            if not w.startswith(want + " "): E.append("%s: [%s:] tiene que empezar por %s: %s" % (where, k, want, b))
        if len(gs) < need: E.append("%s: falta la marca" % where)
        return gs
    for k, t, e, ej, tv in CARDS:
        chk_marks(ej, "tarjeta " + t)
        if k == "dh" and "desde hace" not in norm(ej): E.append("tarjeta desde hace sin desde hace")
    for q, a in PREGUNTAS: chk_marks(a, "pregunta " + q)
    for mal, bien, why in ERRORES:
        chk_marks(bien, "error " + mal)
        if plain(bien) == mal or not why: E.append("error tipico sin correccion o sin porque: " + mal)
    if len(QUIZ) < 12: E.append("hacen falta al menos 12 preguntas")
    for it in QUIZ:
        o = [x.lower() for x in it["o"]]
        if len(o) != 3 or len(set(o)) != 3 or any(x not in VALIDAS for x in o): E.append("pregunta sin 3 opciones validas distintas: " + it["q"])
        if it["q"].count("____") != 1 or not it.get("why"): E.append("pregunta sin un hueco o sin explicacion: " + it["q"])
    if {it["o"][0].lower() for it in QUIZ} != VALIDAS: E.append("las preguntas tienen que tener buenas de las cinco palabras")
    used = set()
    for t in TEXTOS:
        n = 0
        for g in GAP.findall(t["texto"]):
            n += 1
            if "#" not in g: E.append("hueco sin motivo en " + t["id"]); continue
            ops, m = g.split("#"); ops = [x.lower() for x in ops.split("|")]
            if len(ops) != 3 or len(set(ops)) != 3 or any(x not in VALIDAS for x in ops): E.append("hueco sin 3 opciones validas en %s: %s" % (t["id"], g))
            if m not in MOTIVOS: E.append("motivo desconocido en %s: %s" % (t["id"], m)); continue
            used.add(m)
            if ops[0] not in MOTIVOS[m][1]: E.append("en %s la buena (%s) no es la de su motivo %s" % (t["id"], ops[0], m))
        if n < 5: E.append("texto con pocos huecos: " + t["id"])
    if used != set(MOTIVOS): E.append("los textos no usan todos los motivos: faltan %s" % (set(MOTIVOS) - used))
    rx = {}
    for d in DETECTOR:
        if d["re"] != norm(d["re"]) or "(?<" in d["re"] or "(?P" in d["re"]: E.append("regex del detector no valida para el navegador: " + d["id"])
    full = detector if detector is not None else DETECTOR
    for d in full: rx[d["id"]] = (d["t"], re.compile(d["re"]))
    def det(s, red=False): return sorted(i for i, (t, r) in rx.items() if (not red or t == "r") and r.search(norm(s)))
    mine = {d["id"] for d in DETECTOR}
    for txt, exp in PRUEBAS:
        got = [x for x in det(txt) if x in mine]
        if got != sorted(exp): E.append("detector: %r da %s y deberia dar %s" % (txt, got, sorted(exp)))
    for d in DETECTOR:
        if not any(d["id"] in e for _, e in PRUEBAS): E.append("aviso sin prueba: " + d["id"])
    for mal, _, _ in ERRORES[:5]:
        if not det(mal): E.append("el detector no ve el error tipico: " + mal)
    buenos = [ej for _, _, _, ej, _ in CARDS] + [a for _, a in PREGUNTAS] + [b for _, b, _ in ERRORES]
    buenos += [filled(t["texto"]) for t in TEXTOS] + [it["q"].replace("____", it["o"][0]) for it in QUIZ]
    for b in buenos:
        for s in re.findall(r"[^.!?\n]+[.!?]*", plain(b)):
            r = det(s, red=True)
            if r: E.append("aviso rojo %s en una frase buena: %r" % (r, s.strip()))
    # node: el detector da lo mismo en el navegador
    if shutil.which("node"):
        js = ("var D=%s;function norm(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}"
              "var bad=[];D.p.forEach(function(p){var n=norm(p[0]),ids=[];D.d.forEach(function(d){if(new RegExp(d.re).test(n))ids.push(d.id);});"
              "ids.sort();if(ids.join()!==p[1].slice().sort().join())bad.push(p[0]+' -> '+ids.join());});console.log(JSON.stringify(bad));") % json.dumps(
            {"d": [{"id": d["id"], "re": d["re"]} for d in DETECTOR], "p": PRUEBAS}, ensure_ascii=False)
        fd, path = tempfile.mkstemp(suffix=".js"); os.write(fd, js.encode("utf-8")); os.close(fd)
        try:
            out = subprocess.run(["node", path], capture_output=True, text=True, timeout=30)
            bad = json.loads(out.stdout or "null")
            if bad is None: E.append("node: no se ha podido probar el detector")
            elif bad: E.append("detector en el navegador distinto de Python: " + "; ".join(bad))
        finally: os.unlink(path)
        # la buena no cae siempre en el mismo sitio del desplegable (misma funcion seeded que la R06)
        src = re.search(r"function seeded\(.*", JS).group(0)
        gids = [(t["id"] + "-" + str(n + 1), g.split("#")[0].split("|")) for t in TEXTOS for n, g in enumerate(GAP.findall(t["texto"]))]
        fd, path = tempfile.mkstemp(suffix=".js")
        os.write(fd, (src + "\nvar G=%s, c=[0,0,0]; G.forEach(function(g){ c[seeded(g[1], g[0]).indexOf(g[1][0])]++; }); console.log(JSON.stringify(c));" % json.dumps(gids)).encode("utf-8")); os.close(fd)
        try: pos = json.loads(subprocess.run(["node", path], capture_output=True, text=True, timeout=30).stdout)
        finally: os.unlink(path)
        if min(pos) < len(gids) // 6: E.append("la buena de los huecos casi siempre cae en el mismo sitio: %s" % pos)
        global POS
        POS = pos
    if E:
        print("\n".join("ERROR (Hace y durante): " + e for e in E)); sys.exit(1)
    return True
POS = None

# ------------------------------------------------------------------ DIBUJOS
INK = "#14161C"; MUT = "#5E5A55"
COLS = {"h": ("#1D5FA8", "#E2ECF8"), "d": ("#B7791F", "#FBF0DA"), "dh": ("#B7791F", "#FBF0DA"), "u": ("#6B3FA0", "#EFE7F8"), "n": ("#17707F", "#DDF0F2")}
def _t(x, y, s, size=15, col=INK, w="400", a="middle"):
    return '<text x="%s" y="%s" text-anchor="%s" font-size="%s" font-weight="%s" fill="%s">%s</text>' % (x, y, a, size, w, col, s)
def _ah(x, y, col, d="r"):
    p = (x, y, x - 13, y - 7, x - 13, y + 7) if d == "r" else (x, y, x + 13, y - 7, x + 13, y + 7)
    return '<polygon points="%d,%d %d,%d %d,%d" fill="%s"/>' % (p + (col,))
def _base(now=True):
    o = '<line x1="30" y1="110" x2="610" y2="110" stroke="#CFC6BB" stroke-width="3"/>' + _ah(616, 110, "#CFC6BB")
    o += _t(40, 140, "antes", 13, MUT, "400", "start") + _t(600, 140, "después", 13, MUT, "400", "end")
    if now:
        o += '<line x1="470" y1="70" x2="470" y2="128" stroke="%s" stroke-width="3"/>' % INK
        o += '<rect x="436" y="44" width="68" height="24" rx="6" fill="%s"/>' % INK + _t(470, 61, "AHORA", 13, "#fff", "700")
    return o
def _brace(x1, x2, y, lab, col):
    return ('<path d="M%d,%d v-8 H%d v8" fill="none" stroke="%s" stroke-width="2"/>' % (x1, y, x2, col)) + _t((x1 + x2) / 2, y - 14, lab, 14, col, "700")
def diagram(k):
    c, s = COLS[k]
    if k == "h":
        o = _base() + '<circle cx="230" cy="110" r="9" fill="%s"/>' % c
        o += '<path d="M466,98 C420,60 280,60 238,98" fill="none" stroke="%s" stroke-width="3"/>' % c + _ah(236, 100, c, "l")
        o += _t(350, 52, "hace tres meses", 15, c, "700") + _t(230, 162, "llegué", 15, INK, "700")
        aria = "Hace: desde ahora miras hacia atrás hasta un punto"
    elif k == "d":
        o = _base() + '<line x1="230" y1="110" x2="556" y2="110" stroke="%s" stroke-width="9" stroke-linecap="round"/>' % c + _ah(580, 110, c)
        o += '<circle cx="230" cy="110" r="10" fill="#fff" stroke="%s" stroke-width="4"/>' % c
        o += _t(230, 86, "octubre", 15, c, "700") + _t(230, 162, "desde octubre", 15, INK, "700") + _t(530, 162, "sigue", 13, MUT)
        aria = "Desde: el punto donde empieza algo que sigue hasta ahora"
    elif k == "dh":
        o = _base() + '<line x1="230" y1="110" x2="556" y2="110" stroke="%s" stroke-width="9" stroke-linecap="round"/>' % c + _ah(580, 110, c)
        o += '<circle cx="230" cy="110" r="10" fill="#fff" stroke="%s" stroke-width="4"/>' % c
        o += _brace(230, 470, 34, "dos semanas", c) + _t(350, 162, "desde hace dos semanas", 15, INK, "700")
        aria = "Desde hace: la línea llega hasta ahora y dices cuánto mide"
    elif k == "u":
        o = _base() + '<line x1="90" y1="110" x2="300" y2="110" stroke="%s" stroke-width="9" stroke-linecap="round"/>' % c
        o += '<circle cx="90" cy="110" r="9" fill="%s"/><circle cx="300" cy="110" r="9" fill="%s"/>' % (c, c)
        o += _brace(90, 300, 86, "tres años", c) + _t(195, 162, "durante tres años", 15, INK, "700") + _t(385, 100, "ya no", 13, MUT)
        aria = "Durante: un trozo cerrado, con principio y final"
    else:
        o = _base(False) + '<rect x="190" y="62" width="260" height="78" rx="14" fill="%s" stroke="%s" stroke-width="4"/>' % (s, c)
        o += '<circle cx="250" cy="101" r="22" fill="#fff" stroke="%s" stroke-width="3"/><line x1="250" y1="101" x2="250" y2="86" stroke="%s" stroke-width="3"/><line x1="250" y1="101" x2="262" y2="108" stroke="%s" stroke-width="3"/>' % (c, c, c)
        o += _t(350, 96, "el puzle", 15, INK, "700") + _t(350, 120, "una hora", 14, c, "700") + _t(320, 164, "lo hice en una hora", 15, INK, "700")
        aria = "En: la caja del tiempo que tardas"
    return '<svg class="dg" viewBox="0 0 640 175" role="img" aria-label="%s">%s</svg>' % (aria, o)

CSS = r"""
.tcards{display:grid;grid-template-columns:1fr;gap:12px;margin:14px 0}
.tcard{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px;border-left:6px solid var(--line)}
.tcard.h{border-left-color:var(--pa)}.tcard.d,.tcard.dh{border-left-color:var(--pl)}.tcard.u{border-left-color:var(--pp)}.tcard.n{border-left-color:var(--pe)}
.tcard h3{margin:0 0 2px;font-size:1.1rem}.tcard p{margin:4px 0}
.tcard .tv{font-size:.85rem;color:var(--muted)}
#tq .ops button{min-width:0}
"""

def view():
    o = '<h2>Hace, desde, desde hace, durante, en</h2>'
    o += ('<p class="lead">Es el mismo mapa, pero ahora la línea es <b>el tiempo</b> y en ella hay un punto fijo: <b>AHORA</b>. '
          'Pregúntate dos cosas: ¿miro hacia atrás desde hoy o hablo de algo que <b>sigue</b> hasta hoy? ¿Es un trozo cerrado o lo que tardo?</p>')
    o += '<div class="tcards">'
    for k, t, e, ej, tv in CARDS:
        o += '<div class="tcard %s"><h3>%s</h3><p>%s</p>%s<p>%s</p><p class="tv">El verbo: %s.</p></div>' % (k, t, e, diagram(k), mk(ej), tv)
    o += '</div>'
    o += ('<div class="tip"><b>El truco del verbo:</b> <b>hace</b> + pasado (llegué hace un año) · <b>desde / desde hace</b> + presente, porque sigue '
          '(vivo aquí desde hace un año) · <b>durante</b> + pasado terminado (viví allí durante un año). Y otra forma de decir lo mismo: '
          '<i>hace un año que vivo aquí</i> = <i>vivo aquí desde hace un año</i>.</div>')
    o += '<h3>Preguntas y respuestas</h3><table class="t"><tr><th>Te preguntan</th><th>Contestas</th></tr>'
    for q, a in PREGUNTAS: o += '<tr><td>%s</td><td>%s</td></tr>' % (q, mk(a))
    o += '</table>'
    o += ('<p class="small muted">Dónde sale: oral tarea 1 (un curso que hice, mi trabajo, la ciudad donde vivo), escritura (biografías, '
          'correos que cuentan tu vida nueva) y auditiva y lectura (fechas y duraciones como trampa).</p>')
    o += '<h3>Los errores más típicos</h3><div class="errs">'
    for mal, bien, why in ERRORES:
        o += '<div class="err"><div class="mal"><span aria-hidden="true">✗</span> <s>%s</s></div><div class="bien"><span aria-hidden="true">✓</span> %s</div><div class="small muted">%s</div></div>' % (mal, mk(bien), why)
    o += '</div>'
    o += '<h3>Practica</h3><div class="pills" id="tsel"><button class="pill on" data-tact="sel" data-k="q">¿Qué palabra?</button>'
    for t in TEXTOS: o += '<button class="pill" data-tact="sel" data-k="%s">%s</button>' % (t["id"], t["titulo"])
    o += '</div><div id="tbox"></div>'
    o += '<div class="row"><button class="btn cta" data-go="examen">Siguiente: en el examen</button></div>'
    return o

def resumen():
    o = '<h3>Hace, desde, desde hace, durante, en</h3><div class="tcards">'
    for k, t, e, ej, tv in CARDS:
        o += '<div class="tcard %s"><h3>%s</h3><p>%s %s</p></div>' % (k, t, e, mk(ej))
    return o + '</div>'

JS = r"""
(function(){
var T = __TDATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function strip(s){ return String(s).replace(/<[^>]+>/g,''); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function seeded(arr, seed){ var h=0; for(var i=0;i<seed.length;i++) h=(h*31+seed.charCodeAt(i))>>>0; var a=arr.slice(); for(var j=a.length-1;j>0;j--){ h=(Math.imul(h,1103515245)+12345)>>>0; var r=(h>>>16)%(j+1); var t=a[j]; a[j]=a[r]; a[r]=t; } return a; }
function blank(){ return {sel:'q', qz:null, log:null, cz:{}}; }
var S=(function(){ try{ var r=localStorage.getItem(T.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b) if(!(k in o)) o[k]=b[k]; return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(T.key, JSON.stringify(S)); }catch(e){} }
if(!$('tbox')) return;

function qzNew(){ S.qz={order:shuffle(range(T.quiz.length)).slice(0,8), i:0, res:[], perm:{}}; save(); }
function renderQ(){
 if(!S.qz) qzNew();
 var st=S.qz, N=st.order.length, box=$('tbox');
 if(st.i>=N){
  var ok=st.res.filter(function(r){return r.ok;}).length, fl=st.res.filter(function(r){return !r.ok;});
  var o='<div class="score"><b class="big">'+ok+'/'+N+'</b><p>'+(ok>=N-1?'¡Muy bien! Lo tienes claro.':'Mira otra vez los dibujos de la línea del tiempo y repite con otras frases.')+'</p>';
  if(fl.length){ o+='<ul class="small">'; fl.forEach(function(r){ var it=T.quiz[r.k]; o+='<li>'+esc(it.q)+' → <b>'+esc(it.o[0])+'</b></li>'; }); o+='</ul>'; }
  box.innerHTML=o+'<div class="row"><button class="btn cta" data-tact="rep">Repetir con otras frases</button></div></div>'; return;
 }
 var idx=st.order[st.i], it=T.quiz[idx], ans=st.res[st.i];
 if(!st.perm[idx]){ st.perm[idx]=shuffle(range(3)); save(); }
 var q=esc(it.q); if(ans) q=q.replace('____','<b style="color:var(--ok)">'+esc(it.o[0])+'</b>');
 var o='<div class="qz"><div class="cnt">¿Qué palabra? · '+(st.i+1)+' de '+N+'</div><div class="prog"><i style="width:'+Math.round(st.i/N*100)+'%"></i></div><div class="qq">'+q+'</div><div class="ops three" role="group">';
 st.perm[idx].forEach(function(j){ var cls=''; if(ans){ if(j===0) cls='good'; else if(j===ans.pick) cls='bad'; } o+='<button type="button" data-tact="qa" data-o="'+j+'" class="'+cls+'"'+(ans?' disabled':'')+'>'+esc(it.o[j])+'</button>'; });
 o+='</div>';
 if(ans) o+='<div class="fb '+(ans.ok?'good':'bad')+'" role="status"><b>'+(ans.ok?'¡Bien!':'No.')+'</b> '+(ans.ok?'':'La buena: <b>'+esc(it.o[0])+'</b>. ')+it.why+'</div>';
 o+='<div class="row"'+(ans?'':' hidden')+'><button class="btn cta" data-tact="next">'+(st.i+1<N?'Siguiente':'Ver el resultado')+'</button></div></div>';
 box.innerHTML=o;
}
var GAPRX=/\[\[([^\]]+)\]\]/g;
function gaps(t){ var l=[], n=0; t.texto.replace(GAPRX,function(m,inner){ n++; var p=inner.split('#'); l.push({gid:t.id+'-'+n, n:n, ok:p[0].split('|')[0], m:p[1]}); return m; }); return l; }
function renderT(id){
 var t=T.textos.filter(function(x){return x.id===id;})[0], n=0;
 var html=t.texto.replace(GAPRX,function(m,inner){
  n++; var ops=inner.split('#')[0].split('|'), gid=t.id+'-'+n, c=S.cz[gid];
  var s='<sup>'+n+'</sup><select data-tg="'+gid+'" aria-label="Hueco '+n+'"'+(c&&c.cur===ops[0]?' disabled class="ok"':(c?' class="no"':''))+'><option value="">…</option>';
  seeded(ops,gid).forEach(function(x){ s+='<option'+(c&&c.cur===x?' selected':'')+'>'+esc(x)+'</option>'; });
  return s+'</select>';
 });
 var fb='', tot=0, done=0, first=0;
 gaps(t).forEach(function(g){ tot++; var c=S.cz[g.gid]; if(!c) return; if(c.cur===g.ok) done++; if(c.first===g.ok) first++;
  fb+= c.cur===g.ok ? '<li class="ok">'+g.n+'. ✓ <b>'+esc(g.ok)+'</b> · '+T.motivos[g.m]+'</li>' : '<li class="no">'+g.n+'. ✗ <b>'+esc(c.cur)+'</b> no va aquí. Pista: '+T.motivos[g.m]+' Prueba otra vez.</li>'; });
 $('tbox').innerHTML='<div class="cz"><span class="chip">'+esc(t.tipo)+'</span><span class="tema">'+esc(t.titulo)+'</span>'+html+'</div>'+
  '<p class="small"><b>'+done+' de '+tot+'</b> huecos bien'+(done===tot?' · a la primera: <b>'+first+' de '+tot+'</b>':'')+'</p><ul class="fbl" aria-live="polite">'+fb+'</ul>'+
  '<div class="row"><button class="btn sm" data-tact="reset" data-id="'+t.id+'">Empezar este texto de nuevo</button></div>';
}
function render(){
 var ps=$('tsel').querySelectorAll('.pill'); for(var i=0;i<ps.length;i++) ps[i].classList.toggle('on', ps[i].getAttribute('data-k')===S.sel);
 if(S.sel==='q') renderQ(); else renderT(S.sel);
}
document.addEventListener('click', function(e){
 var b=e.target.closest('[data-tact]'); if(!b) return; var a=b.getAttribute('data-tact');
 if(a==='sel'){ S.sel=b.getAttribute('data-k'); save(); render(); }
 else if(a==='qa'){ var st=S.qz; if(st.res[st.i]) return; var pick=+b.getAttribute('data-o'); st.res[st.i]={k:st.order[st.i], pick:pick, ok:pick===0};
  if(st.i===st.order.length-1){ var n=st.res.filter(function(r){return r.ok;}).length; S.log={last:n+'/'+st.order.length, fails:st.res.filter(function(r){return !r.ok;}).map(function(r){ return T.quiz[r.k].q; })}; }
  save(); renderQ(); }
 else if(a==='next'){ S.qz.i++; save(); renderQ(); }
 else if(a==='rep'){ qzNew(); renderQ(); }
 else if(a==='reset'){ var id=b.getAttribute('data-id'); Object.keys(S.cz).forEach(function(g){ if(g.indexOf(id+'-')===0) delete S.cz[g]; }); save(); render(); }
});
document.addEventListener('change', function(e){
 var t=e.target; if(t.tagName!=='SELECT' || !t.hasAttribute('data-tg') || !t.value) return;
 var gid=t.getAttribute('data-tg'), c=S.cz[gid]||{}; if(!c.first) c.first=t.value; c.cur=t.value; S.cz[gid]=c; save(); render();
 var ns=document.querySelector('select[data-tg="'+gid+'"]'); if(ns && !ns.disabled) ns.focus();
});
window.__R06tiempo=function(){
 var L=['','HACE, DESDE, DESDE HACE, DURANTE, EN'];
 L.push('- ¿Que palabra?: '+(S.log?S.log.last+(S.log.fails.length?' | fallos: '+S.log.fails.join(' / '):''):'sin hacer'));
 T.textos.forEach(function(t){
  var g=gaps(t), started=g.some(function(x){ return S.cz[x.gid]; }), first=0, done=0, errs=[];
  g.forEach(function(x){ var c=S.cz[x.gid]; if(!c) return; if(c.cur===x.ok) done++; if(c.first===x.ok) first++; else errs.push(x.n+': '+c.first+' -> '+x.ok); });
  L.push('- '+t.titulo+': '+(started?first+'/'+g.length+' a la primera'+(done<g.length?' (sin terminar)':'')+(errs.length?' | '+errs.join('; '):''):'sin hacer'));
 });
 return L;
};
render();
})();
"""

def js():
    data = {"key": STORAGE, "quiz": QUIZ, "textos": TEXTOS, "motivos": {k: v[0] for k, v in MOTIVOS.items()}}
    return JS.replace("__TDATA__", json.dumps(data, ensure_ascii=False))

if __name__ == "__main__":
    check()
    print("ok: pestana Hace y durante | preguntas:", len(QUIZ), "| huecos:", sum(len(GAP.findall(t["texto"])) for t in TEXTOS),
          "| buena en el desplegable (1a/2a/3a):", "/".join(map(str, POS)) if POS else "sin probar", "| pruebas del detector:", len(PRUEBAS))
