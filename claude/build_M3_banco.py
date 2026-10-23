# -*- coding: utf-8 -*-
# MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 6: BANCO DE REFUERZO DE LA ESCRITURA
# Uso: python3 build_M3_banco.py
#  -> DELEA2_curso_M3_banco_escritura.html  (subir a biblioteca/recursos/A2/dele-curso/)
#  -> M3_banco_prompts_imagenes.txt + nombres.txt  (los 8 tripticos nuevos, M3_15 a M3_22)
# Contenido (20 laminas, pautas con piezas y tiempos, textos modelo): banco_escritura_M3.py. Para anadir laminas,
# solo se toca ese archivo. Mismo estilo que el kit (M3-1) y el banco de temas de la oral (M4-1).
# Pestanas: Como funciona · Practica (todas las laminas, con ayudas) · Como en el examen (T1 de tu + T2 a elegir,
# 45 minutos, sin ayudas; el correo de usted no sale) · Tu opinion (Copiar para el corrector de la profesora).
import json, re
from curso_comun import CSS, EMAIL, page
import fotos_M3 as FT
import banco_escritura_M3 as B

TITLE = "Banco de escritura"
FILE = "DELEA2_curso_M3_banco_escritura.html"
STORAGE = "dele-a2-curso-M3-banco"
# Carpeta de WordPress de los tripticos nuevos: la del MES EN QUE SE SUBEN. Si se suben en noviembre, "2026/11".
MES_WP = "2026/10"
FT.MES_WP = MES_WP
FT.IMG_BASE = "https://2spanishteachers.com/wp-content/uploads/" + MES_WP + "/"

# ------------------------------------------------------------ comprobaciones del banco
TAG = re.compile(r"\{([psafc]):(.+?)\}")
LETRA = {"p": "pres", "s": "pas", "a": "antes", "f": "fut"}
def plain(s): return TAG.sub(r"\2", s)
def words(s): return len([w for w in re.split(r"\s+", plain(s).replace("<br>", " ")) if re.search(r"\w", w)])

# formas que no son del A2 (en lo que escribe el candidato): futuro simple, condicional (salvo me gustaria / me
# encantaria y el «podria» de cortesia en el correo de usted), subjuntivo frecuente, pluscuamperfecto, aunque, ojala
COND_OK = {"gustaría", "encantaría", "podría"}
NOMBRES_RIA = {"cafetería", "cafeterías", "panadería", "librería", "frutería", "peluquería", "zapatería", "heladería", "carnicería", "pescadería", "tintorería", "enfermería", "lavandería", "ferretería", "mensajería",
               "quería", "querías", "queríamos", "querían", "queremos", "prefería", "preferían"}  # no son condicionales
B1 = re.compile(r"(?i)\b(aunque|ojalá|hubiera|hubiese|había \w+do|habían \w+do|habíamos \w+do|sea|seas|vaya|vayas|tenga|tengas|pueda|puedas|haga|hagas|quiera|quieras|esté|estés)\b")
IRR = ("tendr", "podr", "sabr", "habr", "querr", "dir", "har", "pondr", "saldr", "vendr", "cabr", "valdr")
def fut_cond(w):
    """futuro simple o condicional = infinitivo (o raiz irregular) + terminacion"""
    for suf, que in (("íamos", "condicional"), ("íais", "condicional"), ("ías", "condicional"), ("ían", "condicional"), ("ía", "condicional"),
                     ("emos", "futuro simple"), ("éis", "futuro simple"), ("ás", "futuro simple"), ("án", "futuro simple"), ("á", "futuro simple"), ("é", "futuro simple")):
        if w.endswith(suf):
            st = w[:-len(suf)]
            if len(st) > 2 and (st[-2:] in ("ar", "er", "ir") or st in IRR or any(st.endswith("_" + i) for i in IRR)):
                return que
            return None
    return None
TU = re.compile(r"(?i)\b(tú|te|ti|tu|tus|contigo|quieres|puedes|tienes|un beso|un abrazo)\b")
USTED = re.compile(r"(?i)\b(usted|ustedes|atentamente|estimad[oa]s?|le escribo|su correo)\b")

ids = [l["id"] for l in B.LAMINAS]
assert len(ids) == len(set(ids)), "Hay dos laminas con el mismo id"
titulos = [l["titulo"] for l in B.LAMINAS]
assert len(titulos) == len(set(titulos)), "Dos laminas con el mismo titulo (el corrector las reconoce por el titulo)"
for a in titulos:
    for b in titulos:
        assert a == b or a.lower() not in b.lower(), "Un titulo esta dentro de otro: %s / %s" % (a, b)
imgs = []
WC = {}
for l in B.LAMINAS:
    ref = "Lamina %s" % l["id"]
    L, tipo = l["lamina"], B.TIPOS[l["tipo"]]
    assert L["tarea"] == tipo["tarea"] and L.get("op") == tipo.get("op"), ref + ": tarea u opcion no cuadran con el tipo"
    assert bool(l.get("porsiacaso")) == (l["tipo"] == "for"), ref + ": solo el correo de usted va marcado «por si acaso»"
    mn, mx = (60, 70) if L["tarea"] == 1 else (70, 80)
    np_ = len(L["pautas"])
    assert np_ == (5 if L["tarea"] == 1 or L.get("op") == 1 else 3), ref + ": numero de pautas"
    for p in L["pautas"]:
        assert p["t"] and p["p"] and all(x in B.TIEMPOS for x in p["ti"]), ref + ": pauta mal escrita: " + p["t"]
    if L["tarea"] == 1:
        e = words(L["input"][0])
        assert 35 <= e <= 45, ref + ": el texto de entrada tiene %d palabras (35-45)" % e
    for k, x in l["modelo"]:
        assert 0 <= k <= np_, ref + ": pauta %d no existe" % k
        assert not re.search(r"\{(?![psafc]:)", x), ref + ": marca mal escrita: " + x[:50]
    assert sorted(set(k for k, _ in l["modelo"] if k)) == list(range(1, np_ + 1)), ref + ": el modelo no trata todas las pautas"
    w = sum(words(x) for _, x in l["modelo"])
    assert mn <= w <= mx, ref + ": el texto modelo tiene %d palabras (%d-%d)" % (w, mn, mx)
    WC[l["id"]] = w
    for i, p in enumerate(L["pautas"]):
        hay = set(LETRA[m] for k, x in l["modelo"] if k == i + 1 for m, _ in TAG.findall(x) if m in LETRA)
        falta = [t for t in p["ti"] if t not in hay]
        assert not falta, ref + ", pauta %d: el modelo no usa %s" % (i + 1, falta)
    usados = set(t for p in L["pautas"] for t in p["ti"])
    assert len(usados) >= 3 or L["tarea"] == 2 and L.get("op") == 2 and len(usados) >= 2, ref + ": la lamina no mezcla tiempos: %s" % usados
    txt = " ".join(plain(x) for _, x in l["modelo"])
    for w in re.findall(r"[a-záéíóúñ]+", txt.lower()):
        f = None if w in NOMBRES_RIA else fut_cond(w)
        if f and not (w in COND_OK and (w != "podría" or l["tipo"] == "for")):
            raise AssertionError(ref + ": %s (B1): %s" % (f, w))
    assert not B1.search(txt), ref + ": forma de B1: " + (B1.search(txt).group(0) if B1.search(txt) else "")
    if l["tipo"] == "inf":
        assert not USTED.search(txt), ref + ": correo de tu con algo de usted: " + USTED.search(txt).group(0)
    if l["tipo"] == "for":
        assert not TU.search(txt), ref + ": correo de usted con algo de tu: " + TU.search(txt).group(0)
    if l["tipo"] in ("bio", "dia"):
        assert FT.check(L, ref) == 3
        imgs.append(L["img"])
    else:
        assert not L.get("photos"), ref + ": solo la biografia y el dia con fotos llevan fotos"
assert len(imgs) == len(set(imgs)), "Dos laminas con la misma imagen"
nums = sorted(int(x[3:5]) for x in imgs)
assert nums == list(range(15, 15 + len(imgs))), "Los tripticos nuevos van del M3_15 en adelante, seguidos: %s" % nums
assert sum(1 for l in B.LAMINAS if l["tipo"] == "inf") >= 4, "En el modo examen hacen falta varias T1 de tu"

# ------------------------------------------------------------ HTML de apoyo
def lamina_html(l):
    L = l["lamina"]
    h = "Tarea %d" % L["tarea"] + (" · Opción %d" % L["op"] if L.get("op") else "")
    mn, mx = (60, 70) if L["tarea"] == 1 else (70, 80)
    o = ['<div class="lam"><div class="lh"><span>%s</span><span>%d-%d palabras</span></div>' % (h, mn, mx)]
    if L.get("instr"): o.append("<p>%s</p>" % L["instr"])
    if L.get("input"): o.append('<div class="msg">' + "".join("<p>%s</p>" % x for x in L["input"]) + "</div>")
    if L.get("intro"): o.append("<p>%s</p>" % L["intro"])
    if L.get("photos"): o.append(FT.fotos_html(L))
    if L.get("ficha"): o.append('<ul class="ficha">' + "".join("<li>%s</li>" % x for x in L["ficha"]) + "</ul>")
    if L.get("intro2"): o.append("<p>%s</p>" % L["intro2"])
    if L.get("lead"): o.append("<p>%s</p>" % L["lead"])
    o.append('<ul class="pa">' + "".join('<li><span class="bn">%d</span>%s</li>' % (i + 1, p["t"]) for i, p in enumerate(L["pautas"])) + "</ul>")
    o.append('<div class="pw">Número de palabras recomendadas: entre %d y %d.</div></div>' % (mn, mx))
    return "".join(o)

def marked(s):
    def rep(m):
        k, x = m.group(1), m.group(2)
        if k == "c": return '<span class="cx">%s</span>' % x
        return '<span class="v v-%s">%s</span>' % (LETRA[k], x)
    return TAG.sub(rep, s)

def modelo_html(l):
    pars, cur = [], []
    for k, x in l["modelo"]:
        seg = ('<span class="pb" title="Pauta %d">%d</span>' % (k, k) if k else "") + marked(x)
        cur.append(seg)
        if k == 0 or l["lamina"]["tarea"] == 2 or k in (1,):
            pass
    # T1: saludo + cuerpo + firma en lineas; T2: un parrafo por pauta
    if l["lamina"]["tarea"] == 1:
        body = [s for (k, _), s in zip(l["modelo"], cur) if k]
        firma = [s for (k, _), s in zip(l["modelo"], cur) if not k]
        return "<p>" + " ".join(body) + "</p>" + "".join("<p>%s</p>" % f for f in firma)
    return "".join("<p>%s</p>" % s for s in cur)

def texto_plano(l):
    return "\n".join(plain(x).replace("<br>", " ") for _, x in l["modelo"])

GENERAL = {
 "inf": ["Todo de tú: saludo, verbos («quieres», «tienes»), «te», «tu» y despedida.", "He contestado a las preguntas que me hace el correo."],
 "for": ["Todo de usted: «le», «su», «usted» y despedida sin besos ni abrazos.", "He dicho por qué escribo y he dado las gracias."],
 "blog": ["He mezclado los tiempos: lo que pasó, cómo era, cómo es ahora y mis planes.", "He usado al menos tres conectores distintos."],
 "bio": ["He escrito frases completas en pasado, no la lista de datos copiada.", "He dado mi opinión con «Creo que... porque...»."],
 "dia": ["He contado la historia en pasado, no he descrito las fotos.", "He usado al menos tres conectores distintos."],
}

LAMS = []
for l in B.LAMINAS:
    L = l["lamina"]
    mn, mx = (60, 70) if L["tarea"] == 1 else (70, 80)
    LAMS.append({"id": l["id"], "tipo": l["tipo"], "n": l["titulo"], "tarea": L["tarea"], "op": L.get("op", 0),
                 "psa": bool(l.get("porsiacaso")), "min": mn, "max": mx, "html": lamina_html(l),
                 "task": L.get("instr") or L.get("intro"),
                 "pa": [{"t": p["t"], "p": p["p"], "ti": p["ti"]} for p in L["pautas"]],
                 "gen": GENERAL[l["tipo"]], "mod": modelo_html(l), "mw": WC[l["id"]]})
TIPOS_JS = {k: {"n": v["n"], "tarea": v["tarea"], "op": v.get("op", 0), "kit": v["kit"], "fr": B.FRASES[k], "av": B.AVISO[k],
                "c": sum(1 for l in B.LAMINAS if l["tipo"] == k)} for k, v in B.TIPOS.items()}
TI = {k: v for k, v in B.TIEMPOS.items()}

# ------------------------------------------------------------ CSS
CSS_B = CSS + r"""
:root{--blu:#2B5FA8;--blu-soft:#E4ECF8;--grn-soft:#E3F1E8}
section.view > h3{margin-top:30px}
.where{display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.04em;background:var(--ink);color:#fff;border-radius:999px;padding:2px 12px;margin:0 6px 8px 0}
.where.psa{background:var(--amb)}
.v{border-radius:3px;padding:0 2px;font-weight:600}
.v-pres{background:var(--blu-soft);color:#1E4A87}.v-pas{background:#FFE2D6;color:#9C3A1E}
.v-antes{background:var(--amb-soft);color:#7A4E0E}.v-fut{background:var(--grn-soft);color:#22603C}
.ti{display:inline-block;font-size:.76rem;font-weight:700;border-radius:999px;padding:1px 9px;margin:0 3px 3px 0;white-space:nowrap}
.ti.pres{background:var(--blu-soft);color:#1E4A87}.ti.pas{background:#FFE2D6;color:#9C3A1E}
.ti.antes{background:var(--amb-soft);color:#7A4E0E}.ti.fut{background:var(--grn-soft);color:#22603C}
.cx{text-decoration:underline;text-decoration-thickness:2.5px;text-decoration-color:var(--coral);text-underline-offset:3px;font-weight:600}
.legend{display:flex;flex-wrap:wrap;gap:4px 6px;font-size:.88rem;margin:6px 0 10px;align-items:center}
/* lamina */
.lam{background:#fff;border:2px solid var(--ink);border-radius:6px;padding:14px 18px;margin:12px 0;font-size:.97rem}
.lam .lh{font-size:.78rem;letter-spacing:.06em;color:var(--muted);text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:6px;margin-bottom:8px;display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
.lam p{margin:4px 0 8px}
.lam ul.pa{margin:0;padding-left:0;list-style:none}
.lam ul.pa li{padding:4px 0 4px 30px;position:relative}
.lam ul.pa li .bn{position:absolute;left:0;top:6px;width:22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:.78rem;font-weight:700;display:grid;place-items:center}
.lam .pw{font-size:.88rem;color:var(--muted);margin-top:8px;font-style:italic}
.msg{background:#F6F3EF;border-radius:8px;padding:10px 14px;margin:8px 0;font-size:.95rem}
.msg p{margin:0 0 4px}
ul.ficha{background:#F6F3EF;border-radius:8px;padding:8px 14px 8px 30px;margin:8px 0;font-size:.93rem}
/* tarjetas */
.filt{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 14px}
.filt button{font:inherit;font-size:.9rem;border:2px solid var(--line);border-radius:999px;padding:5px 14px;background:#fff;cursor:pointer;color:inherit}
.filt button.on{border-color:var(--ink);background:var(--ink);color:#fff}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.card{display:block;width:100%;text-align:left;font:inherit;color:inherit;background:#fff;border:2px solid var(--line);border-radius:12px;padding:10px 14px;cursor:pointer}
.card:hover{border-color:var(--coral)}
.card .k{font-size:.78rem;font-weight:700;letter-spacing:.04em;color:var(--muted);text-transform:uppercase}
.card .k .ps{color:var(--amb)}
.card b{display:block;font-family:Georgia,serif;font-size:1.02rem;margin:2px 0}
.card .st{font-size:.85rem;color:var(--muted)}
.card .st.ok{color:var(--ok);font-weight:600}
/* escribir */
.aviso{background:var(--coral-soft);border-radius:8px;padding:10px 14px;font-size:.95rem;margin:10px 0}
.aviso.psa{background:var(--amb-soft)}
.tlist{list-style:none;padding:0;margin:6px 0}
.tlist li{padding:6px 0 6px 30px;position:relative;border-bottom:1px dashed var(--line);font-size:.95rem}
.tlist li .bn{position:absolute;left:0;top:7px;width:22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:.78rem;font-weight:700;display:grid;place-items:center}
.write{background:#FFF8F2;border:2px solid var(--coral);border-radius:14px;padding:16px 18px;margin:16px 0}
.write h3{margin:0 0 6px}
.write textarea,textarea.extx{width:100%;font:inherit;font-size:1rem;line-height:1.7;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;min-height:230px;background:#fff;resize:vertical}
.cnt{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;font-size:.92rem;margin:8px 0 2px}
.cnt .num{font-family:Georgia,serif;font-size:1.5rem;font-weight:700}
.cnt .bar{flex:1 1 160px;height:10px;border-radius:999px;background:#EEE8E1;position:relative;overflow:hidden;min-width:120px}
.cnt .bar i{position:absolute;top:0;bottom:0;background:var(--ok-soft);border-left:2px solid var(--ok);border-right:2px solid var(--ok)}
.cnt .bar b{position:absolute;top:0;bottom:0;left:0;background:var(--coral);opacity:.75}
.cnt.ok .num{color:var(--ok)}.cnt.low .num{color:var(--coral)}.cnt.high .num{color:var(--amb)}
.det{font-size:.9rem;margin:6px 0;padding:8px 12px;border-radius:8px;background:var(--amb-soft);color:#7A4E0E}
.det[hidden]{display:none}
.chk{list-style:none;padding:0;margin:8px 0}
.chk li label{display:flex;gap:10px;align-items:flex-start;padding:6px 0;border-bottom:1px dashed var(--line);cursor:pointer}
.chk input{width:20px;height:20px;accent-color:var(--ok);flex:0 0 auto;margin-top:3px}
.chk li label:has(input:checked) > span{color:var(--muted);text-decoration:line-through}
.chk .pn{display:inline-grid;place-items:center;min-width:19px;height:19px;border-radius:50%;background:var(--ink);color:#fff;font-size:.68rem;font-weight:700;vertical-align:1px;margin-right:4px}
.chkres{font-size:.92rem;font-weight:600}
.saved{font-size:.82rem;color:var(--ok);min-height:1.2em}
.letter{background:#fff;border:1px solid var(--line);border-left:5px solid var(--coral);border-radius:0 10px 10px 0;padding:14px 18px;font-size:1.02rem;line-height:1.85}
.letter p{margin:0 0 8px}
.pb{display:inline-grid;place-items:center;min-width:19px;height:19px;border-radius:50%;background:var(--ink);color:#fff;font-size:.68rem;font-weight:700;vertical-align:2px;margin-right:3px}
.letter.clean .v{background:none;color:inherit;font-weight:inherit;padding:0}
.letter.clean .cx{text-decoration:none;font-weight:inherit}
.letter.clean .pb{display:none}
.tg{font-size:.88rem;display:flex;gap:8px;align-items:center;cursor:pointer;margin:8px 0}
.tg input{width:18px;height:18px;accent-color:var(--coral)}
.frs{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}
.frs span{background:#fff;border:1px solid var(--line);border-radius:999px;padding:3px 12px;font-style:italic;font-size:.93rem}
/* examen */
.clock{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;background:var(--ink);color:#fff;border-radius:12px;padding:10px 16px;margin:10px 0 16px}
.clock .tm{font-family:Georgia,serif;font-size:1.7rem;font-weight:700;letter-spacing:.03em;min-width:5ch}
.clock .tm.warn{color:#FFB199}
.clock .btn{border-color:#fff}
.clock .sp{flex:1}
.opgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.opbox{border:2px solid var(--line);border-radius:12px;padding:8px 12px;background:#fff}
.opbox.on{border-color:var(--coral);background:#FFF8F2}
.opbox.off{opacity:.55}
.opbox .lam{margin:6px 0}
.hist{list-style:none;padding:0}
.hist li{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 14px;margin:6px 0;font-size:.93rem}
.fbk{border-radius:10px;padding:10px 14px;margin:10px 0;font-size:.95rem;background:var(--ok-soft)}
.fbk.bad{background:var(--amb-soft)}
.keys{counter-reset:k;list-style:none;padding:0}
.keys li{counter-increment:k;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 14px 10px 52px;margin:8px 0;position:relative}
.keys li:before{content:counter(k);position:absolute;left:14px;top:8px;font-family:Georgia,serif;font-size:1.5rem;font-weight:700;color:var(--coral)}
/* opinion */
.scale{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.scale label{cursor:pointer}
.scale input{position:absolute;opacity:0}
.scale span{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;border:2px solid var(--line);background:#fff;font-weight:700}
.scale input:checked + span{background:var(--ink);border-color:var(--ink);color:#fff}
.scale input:focus-visible + span{outline:3px solid var(--cta);outline-offset:2px}
.opn label.q{display:block;font-weight:600;margin:18px 0 6px}
.opn textarea{width:100%;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;min-height:80px;background:#fff}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips label{border:2px solid var(--line);border-radius:999px;padding:5px 14px;cursor:pointer;background:#fff}
.chips label:has(input:checked){border-color:var(--ink);background:var(--ink);color:#fff}
.chips input{position:absolute;opacity:0}
.sendbox{border:2px solid var(--coral);border-radius:12px;padding:18px 22px;margin:26px 0;background:#fff}
.sendbox input[type=text]{width:100%;max-width:360px;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 12px;margin-top:6px}
.sum{font-size:.92rem;margin:6px 0;padding-left:1.1em}
@media (max-width:760px){.cards,.opgrid{grid-template-columns:1fr}.clock .tm{font-size:1.4rem}}
@media print{header.top,.row,.noprint,footer.legal,.clock{display:none!important}body{background:#fff}.lam{break-inside:avoid}}
""" + FT.CSS

# ------------------------------------------------------------ VISTAS
STEPS = [("como", "Cómo funciona"), ("practica", "Practica"), ("examen", "Como en el examen"), ("opinion", "Tu opinión")]

def fila_tipo(k):
    t = TIPOS_JS[k]
    donde = "Tarea 1" if t["tarea"] == 1 else "Tarea 2 · opción %d" % t["op"]
    pal = "60-70" if t["tarea"] == 1 else "70-80"
    return "<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%d</td></tr>" % (t["n"], donde, pal, t["c"])

LEG = '<div class="legend">' + "".join('<span class="ti %s">%s</span>' % (k, B.TIEMPOS[k]["n"]) for k in B.ORDEN_TIEMPOS) + \
      '<span class="ti" style="background:#fff;border:1px solid var(--line)"><span class="cx">conector</span></span></div>'

V_COMO = """
<span class="where">Escritura · Módulo 3</span>
<h2>Un banco para escribir mucho</h2>
<p class="lead">Aquí tienes %d láminas nuevas, como las del examen, para escribir un texto cada día. Cada lámina tiene sus ayudas: los tiempos que pide cada pauta, frases útiles, un contador de palabras, una lista de control y un texto modelo.</p>
<table class="t"><thead><tr><th>Tipo de texto</th><th>Dónde sale</th><th>Palabras</th><th>Láminas</th></tr></thead><tbody>%s</tbody></table>
<p class="small muted">El correo de usted está «por si acaso»: en los exámenes publicados la tarea 1 es un correo de tú a un amigo o a un familiar. Por eso no sale en «Como en el examen».</p>
<h3>Cómo trabajar una lámina</h3>
<ol class="keys">
 <li><b>Lee la lámina y mira el color de cada pauta.</b> El color dice qué tiempo pide: casi todas las láminas mezclan el presente, el pasado, cómo era antes y los planes. Ese es el secreto de la escritura del A2.</li>
 <li><b>Escribe, mejor primero a mano.</b> En el examen escribes en papel: unas 10 palabras por línea. Después copia tu texto aquí.</li>
 <li><b>Mira el contador y la lista de control.</b> Cada pieza de cada pauta, al menos una frase. Las pautas olvidadas son el fallo que más nota quita.</li>
 <li><b>Compara con el texto modelo.</b> No es «la respuesta»: tu texto puede ser muy distinto. Fíjate en cómo cambia de tiempo de una pauta a otra.</li>
</ol>
<p>Colores del texto modelo:</p>
%s
<h3>Como en el examen</h3>
<p>Cuando ya tengas práctica, prueba el modo examen: un correo de tú (tarea 1) y dos opciones para la tarea 2. Tienes 45 minutos, como en el examen, y no hay ayudas hasta el final.</p>
<div class="tip">¿Te falta una frase? Las frases de cada tipo de texto están en el <b>Kit de frases</b> (DELEA2_curso_M3_kit_frases.html). Aquí solo hay unas pocas nuevas en cada lámina.</div>
<div class="row"><button class="btn cta" data-go="practica">Empezar: Practica</button></div>
""" % (len(B.LAMINAS), "".join(fila_tipo(k) for k in B.ORDEN_TIPOS), LEG)

V_PRACTICA = '<div id="pr"></div>'
V_EXAMEN = '<div id="ex"></div>'

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo. Al copiar, también se copian tus textos para que tu profesora los corrija.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué tipo de texto te parece más difícil?</label>
 <div class="chips" role="group" aria-labelledby="o1l">__CHIPS1__</div>
 <label class="q" id="o2l">2. ¿Te han ayudado los colores de los tiempos en cada pauta?</label>
 <div class="chips" role="group" aria-labelledby="o2l">__CHIPS2__</div>
 <label class="q" id="o3l">3. En «Como en el examen», ¿te ha dado tiempo a terminar?</label>
 <div class="chips" role="group" aria-labelledby="o3l">__CHIPS3__</div>
 <label class="q" for="o4">4. ¿Qué te ha costado más? ¿Falta algún tema o algo no se entiende?</label>
 <textarea id="o4"></textarea>
 <label class="q" id="o5l">5. Ahora, ¿cuánto control sientes en la prueba de Escritura? (1 = nada, 10 = total)</label>
 <div class="scale" role="group" aria-labelledby="o5l" id="o5"></div>
</div>
<div class="sendbox">
 <h3>Envía tu opinión y tus textos a tu profesora</h3>
 <ul class="sum" id="sum"></ul>
 <label><b>Tu nombre</b><br><input type="text" id="sname" autocomplete="name"></label>
 <div class="row"><button class="btn cta" data-act="copy">Copiar</button></div>
 <div class="copied-box" id="cbox" role="status" hidden></div>
 <p class="muted small">Pégalo en un correo para tu profesora: __EMAIL__.</p>
</div>
"""
def chips(name, vals):
    return "".join('<label><input type="radio" name="%s" value="%s">%s</label>' % (name, v, v) for v in vals)
V_OPINION = (V_OPINION.replace("__CHIPS1__", chips("o1", [B.TIPOS[k]["n"].replace(" (por si acaso)", "") for k in B.ORDEN_TIPOS]))
             .replace("__CHIPS2__", chips("o2", ["Sí, mucho", "Un poco", "No"]))
             .replace("__CHIPS3__", chips("o3", ["Sí, de sobra", "Justo", "No", "Todavía no lo he hecho"]))
             .replace("__EMAIL__", EMAIL))

views = {"como": V_COMO, "practica": V_PRACTICA, "examen": V_EXAMEN, "opinion": V_OPINION}
BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Escritura · Taller de escritura</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
"""
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
body = BODY.replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

DATA = {"key": STORAGE, "steps": [{"id": k, "label": l} for k, l in STEPS], "lams": LAMS, "tipos": TIPOS_JS,
        "ord": B.ORDEN_TIPOS, "ti": TI, "ordti": B.ORDEN_TIEMPOS, "min": 45}

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
var LM = {}; D.lams.forEach(function(l){ LM[l.id]=l; });
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function blank(){ return {cur:'como', seen:{}, sel:'', filt:'', w:{}, wc:{}, sim:null, sims:[], o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function pick(a){ return a[Math.floor(Math.random()*a.length)]; }

/* ---------------- recuento y detectores ---------------- */
function nWords(t){ return String(t||'').split(/\s+/).filter(function(w){ return /[A-Za-z0-9À-ɏ]/.test(w); }).length; }
function cntHtml(n, mn, mx){
 var cls=n<mn?'low':(n>mx?'high':'ok'), top=Math.max(mx+30, n), msg;
 if(!n) msg='Empieza a escribir.';
 else if(n<mn) msg='Te faltan '+(mn-n)+' para llegar a '+mn+'.';
 else if(n<=mx) msg='¡Bien! Estás entre '+mn+' y '+mx+'.';
 else msg='Te pasas '+(n-mx)+'. Unas pocas más no son un problema, pero no escribas mucho más.';
 return '<div class="cnt '+cls+'"><span class="num">'+n+'</span><span>palabras</span><span class="bar" aria-hidden="true"><i style="left:'+(mn/top*100)+'%;width:'+((mx-mn)/top*100)+'%"></i><b style="width:'+Math.min(100,n/top*100)+'%"></b></span><span class="small">'+msg+'</span></div>';
}
var RX_US=/(^|[^\wáéíóúñ])(usted|ustedes|atentamente|estimad[oa]s?|le escribo|su correo|un saludo cordial)(?=$|[^\wáéíóúñ])/gi;
var RX_TU=/(^|[^\wáéíóúñ])(tú|te|ti|tu|tus|contigo|quieres|puedes|tienes|sabes|un beso|un abrazo|besos)(?=$|[^\wáéíóúñ])/gi;
var NO_PAS={'qué':1,'café':1,'bebé':1,'sofá':1,'mamá':1,'papá':1,'está':1,'dónde':1,'cuándo':1,'también':1};
var RX_PAS=/(^|[^\wáéíóúñ])(\w*(é|ó|aste|iste|asteis|isteis|aron|ieron|aba|abas|ábamos|aban|ía|ías|íamos|ían)|fue|fui|fuimos|era|eran|había|he|ha|hemos|han)(?=$|[^\wáéíóúñ])/gi;
var CONECT=['pero','porque','además','también','después','luego','primero','al final','por eso','así que','cuando','por suerte','de repente','desde entonces','al principio','entonces','por la mañana','por la tarde','por la noche'];
function found(rx, t){ var o={}, m; rx.lastIndex=0; while((m=rx.exec(t))){ o[m[2].toLowerCase()]=1; } return Object.keys(o); }
function detect(l, t){
 var a=[];
 if(!t || nWords(t)<15) return '';
 if(l.tipo==='inf'){ var u=found(RX_US, t); if(u.length) a.push('Es un correo de <b>tú</b>, pero veo palabras de usted: <i>'+esc(u.join(', '))+'</i>.'); }
 if(l.tipo==='for'){ var x=found(RX_TU, t); if(x.length) a.push('Es un correo de <b>usted</b>, pero veo palabras de tú: <i>'+esc(x.join(', '))+'</i>.'); }
 if(l.tarea===2){
  var ps=found(RX_PAS, t).filter(function(w){ return !NO_PAS[w]; });
  if(!ps.length && nWords(t)>30) a.push('No veo verbos en pasado. ¿Has contado lo que pasó o cómo era? Mira los colores de las pautas.');
  var low=t.toLowerCase(), nc=CONECT.filter(function(c){ return new RegExp('(^|[^a-záéíóúñ])'+c+'($|[^a-záéíóúñ])').test(low); }).length;
  if(nc<3 && nWords(t)>40) a.push('Solo veo '+nc+' conector'+(nc===1?'':'es')+' distinto'+(nc===1?'':'s')+'. Prueba con <i>primero, después, al final, por eso, así que...</i>');
 }
 return a.join('<br>');
}

/* ---------------- navegacion ---------------- */
function nTexts(){ return D.lams.filter(function(l){ return S.w[l.id] && S.w[l.id].trim(); }).length; }
function tabDone(id){
 if(id==='como') return !!S.seen.como;
 if(id==='practica') return nTexts()>0;
 if(id==='examen') return S.sims.length>0;
 if(id==='opinion') return !!(S.o1||S.o2||S.o3||S.o4||S.o5);
 return false;
}
function nav(){
 var o='';
 D.steps.forEach(function(st,i){
  var done=tabDone(st.id), on=S.cur===st.id;
  o+='<button type="button" class="'+(on?'on ':'')+(done&&!on?'done':'')+'" data-go="'+st.id+'"'+(on?' aria-current="step"':'')+'><span class="n">'+(done&&!on?'✓':(i+1))+'</span>'+st.label+'</button>';
 });
 $('steps').innerHTML=o;
}
function go(id){
 S.seen[S.cur]=true; S.cur=id; save();
 var vs=document.querySelectorAll('section.view');
 for(var i=0;i<vs.length;i++) vs[i].classList.toggle('on', vs[i].id==='v-'+id);
 if(id==='practica') renderPr();
 if(id==='examen') renderEx();
 if(id==='opinion') summary();
 nav(); window.scrollTo(0,0);
}

/* ---------------- piezas comunes ---------------- */
function tiChips(ti){ return ti.map(function(k){ return '<span class="ti '+k+'" title="'+esc(D.ti[k].f)+'">'+D.ti[k].n+'</span>'; }).join(''); }
function nPieces(l){ var n=0; l.pa.forEach(function(p){ n+=p.p.length; }); return n+l.gen.length; }
function nChecked(pref, l){ var n=0; l.pa.forEach(function(p,i){ p.p.forEach(function(x,j){ if(S.wc[pref+'|'+i+'|'+j]) n++; }); }); l.gen.forEach(function(x,j){ if(S.wc[pref+'|g|'+j]) n++; }); return n; }
function checklist(pref, l){
 var o='<ul class="chk">';
 l.pa.forEach(function(p,i){ p.p.forEach(function(x,j){ var k=pref+'|'+i+'|'+j;
  o+='<li><label><input type="checkbox" data-wc="'+esc(k)+'"'+(S.wc[k]?' checked':'')+'><span><span class="pn">'+(i+1)+'</span>'+esc(x)+'</span></label></li>'; }); });
 l.gen.forEach(function(x,j){ var k=pref+'|g|'+j; o+='<li><label><input type="checkbox" data-wc="'+esc(k)+'"'+(S.wc[k]?' checked':'')+'><span>'+esc(x)+'</span></label></li>'; });
 return o+'</ul><p class="chkres" data-chkres="'+esc(pref)+'"></p>';
}
function chkRes(pref){
 var el=document.querySelector('[data-chkres="'+pref+'"]'); if(!el) return;
 var id=pref.split('#')[0].replace(/^s\d+:/,''), l=LM[id]; if(!l) return;
 var n=nChecked(pref,l), t=nPieces(l);
 el.textContent=n+' de '+t+' puntos revisados'+(n===t?' ✓':'');
}
function modeloHtml(l, key){
 return '<details><summary>Ver un texto modelo ('+l.mw+' palabras)</summary><p class="small muted">Es un texto que aprueba con buena nota. Tu texto puede ser muy distinto: fíjate en cómo cambia de tiempo de una pauta a otra.</p>'+
  '<div class="legend">'+D.ordti.map(function(k){ return '<span class="ti '+k+'">'+D.ti[k].n+'</span>'; }).join('')+'<span class="ti" style="background:#fff;border:1px solid var(--line)"><span class="cx">conector</span></span></div>'+
  '<div class="letter" id="let-'+key+'">'+l.mod+'</div><label class="tg"><input type="checkbox" data-clean="let-'+key+'"> Ver el texto sin marcas</label></details>';
}

/* ---------------- practica ---------------- */
function lamList(){ var f=S.filt; return D.lams.filter(function(l){ return !f || l.tipo===f; }); }
function renderPr(){
 var box=$('pr'), o='';
 if(!S.sel || !LM[S.sel]){
  o+='<h2>Practica</h2><p class="lead">Elige una lámina. Las que ya has escrito llevan una marca verde.</p><div class="filt" role="group" aria-label="Tipo de texto">';
  o+='<button type="button" class="'+(!S.filt?'on':'')+'" data-act="filt" data-f="">Todas ('+D.lams.length+')</button>';
  D.ord.forEach(function(k){ o+='<button type="button" class="'+(S.filt===k?'on':'')+'" data-act="filt" data-f="'+k+'">'+esc(D.tipos[k].n)+' ('+D.tipos[k].c+')</button>'; });
  o+='</div><div class="cards">';
  lamList().forEach(function(l){ var w=nWords(S.w[l.id]);
   o+='<button type="button" class="card" data-act="sel" data-id="'+l.id+'"><span class="k">'+esc(D.tipos[l.tipo].n.replace(' (por si acaso)',''))+' · tarea '+l.tarea+(l.psa?' · <span class="ps">por si acaso</span>':'')+'</span><b>'+esc(l.n)+'</b>'+
     '<span class="st'+(w?' ok':'')+'">'+(w?'✓ Escrito: '+w+' palabras':'Sin escribir')+'</span></button>'; });
  o+='</div>';
  box.innerHTML=o; return;
 }
 var l=LM[S.sel], t=D.tipos[l.tipo], L=lamList(), k=L.findIndex(function(x){ return x.id===l.id; });
 var prev=L[(k-1+L.length)%L.length], next=L[(k+1)%L.length];
 o+='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="back">← Todas las láminas</button></div>';
 o+='<span class="where">'+esc(t.n.replace(' (por si acaso)',''))+' · '+(l.tarea===1?'Tarea 1':'Tarea 2 · opción '+l.op)+'</span>'+(l.psa?'<span class="where psa">Por si acaso</span>':'');
 o+='<h2>'+esc(l.n)+'</h2><div class="aviso'+(l.psa?' psa':'')+'">'+t.av+'</div>';
 o+=l.html;
 o+='<h3>Qué tiempo pide cada pauta</h3><ul class="tlist">'+l.pa.map(function(p,i){ return '<li><span class="bn">'+(i+1)+'</span>'+esc(p.t)+'<br>'+(p.ti.length?tiChips(p.ti):'<span class="small muted">Una fórmula: no hace falta pensar en el tiempo.</span>')+'</li>'; }).join('')+'</ul>';
 o+='<details><summary>Frases nuevas para este tipo de texto</summary><div class="frs">'+t.fr.map(function(f){ return '<span>'+esc(f)+'</span>'; }).join('')+'</div><p class="small muted">Más frases en el Kit de frases, pestaña «'+esc(t.kit)+'».</p></details>';
 o+='<div class="write"><h3>Tu texto</h3><p class="small">Si puedes, escríbelo primero a mano y después cópialo aquí. Se guarda en este navegador.</p>'+
   '<textarea data-w="'+l.id+'" aria-label="Tu texto" placeholder="Escribe aquí tu texto...">'+esc(S.w[l.id]||'')+'</textarea>'+
   '<div data-cnt="'+l.id+'"></div><div class="det" data-det="'+l.id+'" hidden></div><div class="saved" data-sv="'+l.id+'" role="status"></div>'+
   '<h4 style="margin-top:12px">Lista de control: cada pieza, al menos una frase</h4>'+checklist(l.id, l)+'</div>';
 o+=modeloHtml(l, l.id);
 o+='<div class="row"><button class="btn" data-act="sel" data-id="'+prev.id+'">← Anterior</button><button class="btn cta" data-act="sel" data-id="'+next.id+'">Siguiente lámina →</button></div>';
 o+='<p class="small muted">Para enviar tus textos a tu profesora, ve a <b>Tu opinión</b> y pulsa <b>Copiar</b>.</p>';
 box.innerHTML=o; upd(l.id); chkRes(l.id);
}
function upd(id){
 var l=LM[id], t=S.w[id]||'', c=document.querySelector('[data-cnt="'+id+'"]'), d=document.querySelector('[data-det="'+id+'"]');
 if(c) c.innerHTML=cntHtml(nWords(t), l.min, l.max);
 if(d){ var h=detect(l,t); d.innerHTML=h; d.hidden=!h; }
}

/* ---------------- como en el examen ---------------- */
var TICK=null;
function simEl(s){ return (s.acc||0)+(s.run?(Date.now()-s.run)/1000:0); }
function fmt(sec){ sec=Math.max(0,Math.round(sec)); var m=Math.floor(sec/60), x=sec%60; return (m<10?'0':'')+m+':'+(x<10?'0':'')+x; }
function newSim(){
 var last=S.sims.length?S.sims[S.sims.length-1]:null;
 function pk(arr, avoid){ var a=arr.filter(function(l){ return l.id!==avoid; }); return pick(a.length?a:arr); }
 var t1=pk(D.lams.filter(function(l){ return l.tipo==='inf'; }), last&&last.t1);
 var o1=pk(D.lams.filter(function(l){ return l.tarea===2 && l.op===1; }), last&&last.o1);
 var o2=pk(D.lams.filter(function(l){ return l.tarea===2 && l.op===2; }), last&&last.o2);
 S.sim={id:Date.now(), t1:t1.id, o1:o1.id, o2:o2.id, op:'', w1:'', w2:'', acc:0, run:Date.now(), done:false, fecha:(function(d){ return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2); })(new Date())};
 save(); renderEx();
}
function renderEx(){
 var box=$('ex'), s=S.sim, o='';
 clearInterval(TICK); TICK=null;
 if(!s){
  o+='<h2>Como en el examen</h2><p class="lead">Un correo de tú (tarea 1) y dos opciones para la tarea 2: eliges una. Tienes '+D.min+' minutos para las dos tareas, como en el examen. Las ayudas (colores, frases, lista de control y textos modelo) salen al terminar.</p>';
  o+='<ul class="small"><li>Reparto aconsejado: unos 20 minutos para la tarea 1 y unos 25 para la tarea 2, con 5 minutos para revisar.</li><li>Si puedes, escribe a mano en un papel y después copia tus textos aquí.</li><li>El correo de usted no sale aquí: en los exámenes publicados la tarea 1 es de tú.</li></ul>';
  o+='<div class="row"><button class="btn cta" data-act="newsim">Empezar un examen</button></div>';
  if(S.sims.length){ o+='<h3>Tus exámenes</h3><ul class="hist">'+S.sims.slice().reverse().map(function(x){ var op=LM[x.op==='2'?x.o2:x.o1];
   return '<li><b>'+x.fecha+'</b> · '+Math.round(x.used/60)+' min · T1: '+esc(LM[x.t1].n)+' ('+nWords(x.w1)+' palabras) · T2: '+(x.op?esc(op.n)+' ('+nWords(x.w2)+' palabras)':'sin elegir')+'</li>'; }).join('')+'</ul>'; }
  box.innerHTML=o; return;
 }
 var t1=LM[s.t1], a=LM[s.o1], b=LM[s.o2];
 if(!s.done){
  o+='<div class="clock" role="timer"><span class="tm" id="tm">'+fmt(D.min*60-simEl(s))+'</span><span class="small" id="tmx">'+(s.run?'quedan':'en pausa')+'</span><span class="sp"></span>'+
     '<button class="btn sm" data-act="pause">'+(s.run?'Pausa':'Seguir')+'</button><button class="btn sm cta" data-act="finish">Terminar y ver las ayudas</button></div>';
  o+='<h2>Tarea 1</h2>'+t1.html+
     '<textarea class="extx" data-sw="w1" aria-label="Tu texto de la tarea 1" placeholder="Tu correo...">'+esc(s.w1)+'</textarea><div data-scnt="w1"></div>';
  o+='<h2 style="margin-top:28px">Tarea 2</h2><p>Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.</p><div class="opgrid">';
  [['1',a],['2',b]].forEach(function(p){ var on=s.op===p[0];
   o+='<div class="opbox'+(on?' on':(s.op?' off':''))+'">'+p[1].html+'<div class="row" style="margin:6px 0"><button class="btn sm'+(on?' cta':'')+'" data-act="opt" data-op="'+p[0]+'">'+(on?'✓ Has elegido esta opción':'Elijo esta opción')+'</button></div></div>'; });
  o+='</div>';
  if(s.op) o+='<textarea class="extx" data-sw="w2" aria-label="Tu texto de la tarea 2" placeholder="Tu texto de la opción '+s.op+'...">'+esc(s.w2)+'</textarea><div data-scnt="w2"></div>';
  o+='<div class="row"><button class="btn" data-act="quit">Dejar este examen</button></div>';
  box.innerHTML=o; sUpd(); tick();
  if(s.run) TICK=setInterval(tick, 1000);
  return;
 }
 var op=s.op?LM[s.op==='2'?s.o2:s.o1]:null, used=Math.round(s.used/60);
 o+='<h2>Has terminado</h2><div class="fbk'+(s.used>D.min*60?' bad':'')+'">Has usado <b>'+used+' minutos</b>'+(s.used>D.min*60?': más de '+D.min+'. En el examen, el tiempo es para las dos tareas; practica el reparto (20 + 25).':' de '+D.min+'.')+'</div>';
 o+='<p>Ahora revisa cada texto con la lista de control y compáralo con el modelo. Si quieres cambiar algo, cámbialo: se copia la versión final.</p>';
 [[t1,'w1'],[op,'w2']].forEach(function(p){ var l=p[0], k=p[1]; if(!l){ o+='<div class="fbk bad">No has elegido ninguna opción de la tarea 2.</div>'; return; }
  var pref='s'+s.id+':'+l.id;
  o+='<h3>'+(k==='w1'?'Tarea 1':'Tarea 2 · opción '+s.op)+': '+esc(l.n)+'</h3><details><summary>Ver la lámina</summary>'+l.html+'</details>';
  o+='<div class="write"><textarea class="extx" data-sw="'+k+'" aria-label="Tu texto">'+esc(s[k])+'</textarea><div data-scnt="'+k+'"></div><div class="det" data-sdet="'+k+'" hidden></div>'+
     '<h4 style="margin-top:12px">Lista de control</h4><ul class="tlist">'+l.pa.map(function(q,i){ return '<li><span class="bn">'+(i+1)+'</span>'+esc(q.t)+'<br>'+(q.ti.length?tiChips(q.ti):'')+'</li>'; }).join('')+'</ul>'+checklist(pref, l)+'</div>';
  o+=modeloHtml(l, 'x'+k);
 });
 o+='<div class="row"><button class="btn cta" data-act="newsim">Otro examen</button><button class="btn" data-go="opinion">Enviar a mi profesora</button></div>';
 box.innerHTML=o; sUpd();
 [t1,op].forEach(function(l){ if(l) chkRes('s'+s.id+':'+l.id); });
}
function sUpd(){
 var s=S.sim; if(!s) return;
 [['w1',LM[s.t1]],['w2',s.op?LM[s.op==='2'?s.o2:s.o1]:null]].forEach(function(p){
  var c=document.querySelector('[data-scnt="'+p[0]+'"]'), d=document.querySelector('[data-sdet="'+p[0]+'"]'); if(!p[1]) return;
  if(c) c.innerHTML=cntHtml(nWords(s[p[0]]), p[1].min, p[1].max);
  if(d){ var h=detect(p[1], s[p[0]]); d.innerHTML=h; d.hidden=!h; }
 });
}
function tick(){
 var s=S.sim, el=$('tm'); if(!s || s.done || !el) { clearInterval(TICK); return; }
 var left=D.min*60-simEl(s);
 el.textContent=left>=0?fmt(left):'+'+fmt(-left);
 el.classList.toggle('warn', left<300);
 var x=$('tmx'); if(x) x.textContent=!s.run?'en pausa':(left>=0?'quedan':'¡se ha acabado el tiempo!');
}
function finishSim(){
 var s=S.sim; if(!s) return;
 s.acc=simEl(s); s.run=0; s.used=s.acc; s.done=true;
 var copy=JSON.parse(JSON.stringify(s)); S.sims.push(copy); if(S.sims.length>10) S.sims=S.sims.slice(-10);
 save(); nav(); renderEx(); window.scrollTo(0,0);
}
function syncSims(){ if(S.sim && S.sim.done){ for(var i=0;i<S.sims.length;i++){ if(S.sims[i].id===S.sim.id){ S.sims[i].w1=S.sim.w1; S.sims[i].w2=S.sim.w2; } } } }

/* ---------------- opinion y copiar ---------------- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked = r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function summary(){
 var tx=D.lams.filter(function(l){ return S.w[l.id] && S.w[l.id].trim(); });
 $('sum').innerHTML='<li>Textos escritos en «Practica»: '+(tx.length?tx.length+' ('+tx.map(function(l){ return esc(l.n); }).join(', ')+')':'ninguno todavía')+'.</li>'+
  '<li>Exámenes terminados: '+S.sims.length+(S.sims.length>3?' (se copian los tres últimos)':'')+'.</li>';
}
function block(L, l, txt, head, pref){
 L.push('', '== Banco de escritura · '+l.n+' (tarea '+l.tarea+') ==', 'Tarea: '+l.task);
 head.forEach(function(h){ L.push(h); });
 L.push('Pautas: '+l.pa.map(function(p){ return p.t; }).join(' '), 'Lista de control: '+nChecked(pref,l)+' de '+nPieces(l)+' puntos revisados', 'Palabras: '+nWords(txt)+' (recomendadas: '+l.min+'-'+l.max+')', '---', txt.trim(), '---');
}
function pack(){
 var L=['CURSO DELE A2 - ESCRITURA: BANCO DE ESCRITURA', 'Nombre: '+(S.name||'-'), '', 'MIS TEXTOS («Practica»):'];
 var any=false;
 D.lams.forEach(function(l){ var w=(S.w[l.id]||'').trim(); if(!w) return; any=true; block(L, l, w, l.psa?['Correo de usted (por si acaso)']:[], l.id); });
 if(!any) L.push('  (todavía no he escrito ninguno)');
 L.push('', 'COMO EN EL EXAMEN:');
 var ss=S.sims.slice(-3);
 if(!ss.length) L.push('  (todavía no he hecho ninguno)');
 ss.forEach(function(s, i){
  var h='Como en el examen ('+s.fecha+') · tiempo usado: '+Math.round(s.used/60)+' de '+D.min+' minutos';
  if((s.w1||'').trim()) block(L, LM[s.t1], s.w1, [h], 's'+s.id+':'+s.t1);
  var op=s.op?LM[s.op==='2'?s.o2:s.o1]:null;
  if(op && (s.w2||'').trim()) block(L, op, s.w2, [h+' · opción '+s.op+' (la otra era: '+LM[s.op==='2'?s.o1:s.o2].n+')'], 's'+s.id+':'+op.id);
 });
 L.push('', 'OPINIÓN:', '1. El texto más difícil: '+(S.o1||'-'), '2. Los colores de los tiempos me han ayudado: '+(S.o2||'-'), '3. En el modo examen me ha dado tiempo: '+(S.o3||'-'), '4. Lo que más me ha costado / falta algo: '+(S.o4||'-'), '5. Sensación de control en la Escritura (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var svT={};
function savedMsg(id){ var el=document.querySelector('[data-sv="'+id+'"]'); if(!el) return; el.textContent='✓ Guardado en este navegador'; clearTimeout(svT[id]); svT[id]=setTimeout(function(){ el.textContent=''; },1800); }
var ACTS={
 filt:function(b){ S.filt=b.getAttribute('data-f'); save(); renderPr(); },
 sel:function(b){ S.sel=b.getAttribute('data-id'); save(); renderPr(); window.scrollTo(0,0); },
 back:function(){ S.sel=''; save(); renderPr(); window.scrollTo(0,0); },
 newsim:function(){ if(S.sim && !S.sim.done && (S.sim.w1||S.sim.w2) && !confirm('Tienes un examen sin terminar. ¿Empezar otro? El que tienes ahora se pierde.')) return; newSim(); window.scrollTo(0,0); },
 pause:function(){ var s=S.sim; if(!s) return; if(s.run){ s.acc=simEl(s); s.run=0; } else s.run=Date.now(); save(); renderEx(); },
 finish:function(){ var s=S.sim; if(!s) return; if(!(s.w1||'').trim() && !(s.w2||'').trim() && !confirm('Todavía no has escrito nada. ¿Terminar de todas formas?')) return; finishSim(); },
 quit:function(){ if(!confirm('¿Dejar este examen? Lo que has escrito en él se pierde.')) return; S.sim=null; save(); renderEx(); },
 opt:function(b){ var s=S.sim; if(!s) return; s.op=b.getAttribute('data-op'); save(); renderEx(); var t=document.querySelector('[data-sw="w2"]'); if(t) t.focus(); },
 copy:function(){
  var t=pack(), box=$('cbox');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar automáticamente. Copia tus textos a mano en un correo para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
 }
};
document.addEventListener('click', function(e){
 var g=e.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.getAttribute('data-clean')){ var el=$(t.getAttribute('data-clean')); if(el) el.classList.toggle('clean', t.checked); return; }
 if(t.getAttribute('data-wc')){ var k=t.getAttribute('data-wc'); S.wc[k]=t.checked; save(); var p=k.split('|')[0]; chkRes(p); return; }
 if(t.name==='o1'||t.name==='o2'||t.name==='o3'||t.name==='o5'){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){ var t=e.target;
 if(t.getAttribute('data-w')){ var id=t.getAttribute('data-w'); S.w[id]=t.value; save(); upd(id); savedMsg(id); nav(); return; }
 if(t.getAttribute('data-sw') && S.sim){ S.sim[t.getAttribute('data-sw')]=t.value; syncSims(); save(); sUpd(); return; }
 if(t.id==='o4'){ S.o4=t.value; save(); nav(); } if(t.id==='sname'){ S.name=t.value; save(); } });
document.addEventListener('visibilitychange', function(){ if(!document.hidden && S.sim && !S.sim.done) tick(); });

renderScale();
go(D.steps.some(function(s){ return s.id===S.cur; }) ? S.cur : 'como');
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_B, body, js))

# ------------------------------------------------------------ PROMPTS DE LOS TRIPTICOS Y nombres.txt
def ascii_desc(s):
    s = s.replace("ñ", "n").replace("Ñ", "N")
    for a, b in zip("áéíóúüÁÉÍÓÚÜ", "aeiouuAEIOUU"): s = s.replace(a, b)
    return re.sub(r"[\"'«»|]", "", s)
FOT = [l for l in B.LAMINAS if l["lamina"].get("photos")]
with open("M3_banco_prompts_imagenes.txt", "w", encoding="utf-8") as fp:
    fp.write("PROMPTS DE LAS FOTOS · BANCO DE ESCRITURA (curso DELE A2, Módulo 3, pieza 6)\n")
    fp.write("%d trípticos (%d fotos) · una imagen por lámina, 3:1, tres paneles cuadrados iguales · mismo orden que nombres.txt\n" % (len(FOT), 3 * len(FOT)))
    fp.write("Al generar las tres fotos a la vez, la persona sale igual en las tres. Fotos naturales: sin HDR ni contraste, luz plana, nadie posa.\n")
    fp.write("Si la herramienta no da 3:1, elige el formato más ancho y recorta a 3:1 sin cortar los paneles (tres tercios iguales: en el móvil\n")
    fp.write("la página recorta cada tercio).\n")
    fp.write("Después: acción rápida «Imagen DELE» (%d px, %d KB) y subir a WordPress, carpeta del mes %s (si se suben en otro mes,\n" % (FT.ANCHO, FT.KB, MES_WP))
    fp.write("cambiar MES_WP en build_M3_banco.py y volver a construir).\n\n")
    for l in FOT:
        L = l["lamina"]
        fp.write("=" * 78 + "\n%s.jpg\n%s\nLámina: %s (%s)\n" % (L["img"], L["rotulo"], l["titulo"], B.TIPOS[l["tipo"]]["n"]))
        fp.write("".join("  Foto %d: %s\n" % (i + 1, a) for i, a in enumerate(L["photos"])) + "\n")
        fp.write(FT.prompt(L) + "\n\n")
with open("nombres.txt", "w", encoding="utf-8") as fp:
    fp.write("CARPETA: DELE_A2_curso\n")
    for l in FOT:
        fp.write("%s | %d | %d | %s\n" % (l["lamina"]["img"], FT.ANCHO, FT.KB, ascii_desc(l["lamina"]["rotulo"])))

print("ok", FILE, "·", len(B.LAMINAS), "laminas ·", ", ".join("%s %d" % (k, v) for k, v in WC.items()))
print("   tripticos:", ", ".join(l["lamina"]["img"] for l in FOT), "· M3_banco_prompts_imagenes.txt, nombres.txt")
