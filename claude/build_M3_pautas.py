# -*- coding: utf-8 -*-
# MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 2: LAS PAUTAS COMO LISTA DE CONTROL
# Uso: python3 build_M3_pautas.py
#  -> DELEA2_curso_M3_pautas.html  (subir a biblioteca/recursos/A2/dele-curso/)
# Contenido (láminas, piezas de cada pauta, textos de estudiantes, ejercicios y tareas de "Ahora tú"): banco_pautas_M3.py.
# Mismo estilo que el kit de frases (build_M3_kit_frases.py): pestañas, progreso en el navegador (storageKey propio),
# botón Copiar con los textos escritos y preguntas de opinión al final. Sin contador de palabras: contar a ojo.
# 12/10/2026: las laminas con fotos llevan imagenes de verdad (fotos_M3.py); el build comprueba nombre, prompt y alt.
# 12/10/2026: la regla dice lo mismo que la escala oficial (y que M3-3 y M3-5): una pauta que falta te deja en el
# límite; dos (o una que falta y otra a medias), banda 1.
import json, re
from curso_comun import CSS, EMAIL, page
import banco_pautas_M3 as B
import fotos_M3 as FT

TITLE = "Las pautas como lista de control"
FILE = "DELEA2_curso_M3_pautas.html"
STORAGE = "dele-a2-curso-M3-pautas"

PAL = re.compile(r"[\wÀ-ſ]+(?:-[\wÀ-ſ]+)*")
TU_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(tú|tu|tus|te|ti|contigo|tienes|puedes|quieres|perdona|oye|beso|abrazo)(?![\wÀ-ſ])")
US_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(usted|ustedes|atentamente|estimad[oa]s?|cordiales|perdone|disculpe)(?![\wÀ-ſ])")
def words(s): return len(PAL.findall(s))
def tw(par): return sum(words(x) for p in par for _, x in p)
def lam_words(l): return sum(words(x) for x in l.get("input", []))

# ------------------------------------------------------------ comprobaciones del banco
NFOTOS = [0]
def check_lamina(l, ref):
    assert l["tarea"] in (1, 2) and l["pautas"], ref
    if l["tarea"] == 2: assert l.get("op") in (1, 2), ref + ": falta la opción"
    for p in l["pautas"]:
        assert p["t"] and 1 <= len(p["p"]) <= 4, ref + ": piezas de «%s»" % p["t"]
    assert l["pautas"][-1]["t"].endswith("."), ref + ": la última pauta termina en punto"
    if l.get("input"):
        n = lam_words(l)
        assert 30 <= n <= 50, ref + ": el texto de entrada tiene %d palabras (35-45)" % n
    NFOTOS[0] += FT.check(l, ref)

# la regla
R = B.REGLA
check_lamina(R["lamina"], "Regla")
NPR = len(R["lamina"]["pautas"])
REGLA_W = []
for t in R["textos"]:
    cub = set(p for par in t["par"] for p, _ in par if p)
    falta = set(range(1, NPR + 1)) - cub
    assert (not falta) == t["ok"], "Regla %s: pautas sin frase %s" % (t["autor"], falta)
    n = tw(t["par"]); REGLA_W.append(n)
    assert 60 <= n <= 70, "Regla %s: %d palabras (60-70)" % (t["autor"], n)
    assert not US_PAL.search(" ".join(x for par in t["par"] for _, x in par)), "Regla: usted en un correo de tú"
assert R["textos"][0]["ok"] and not R["textos"][1]["ok"]

# piezas, tiempos, mini lista
for pauta, pz, nota in B.PIEZAS: assert 1 <= len(pz) <= 4, pauta
assert len(B.PIEZAS) >= 12
for _, k, _ in B.TIEMPOS: assert 0 <= k < len(B.TIEMPOS_OPS)
check_lamina(B.MINI["lamina"], "Mini lista")
assert [len(x) for x in B.MINI["lista"]] == [len(p["p"]) for p in B.MINI["lamina"]["pautas"]], "Mini lista: piezas y líneas no cuadran"
check_lamina(B.ML_PRACT["lamina"], "Haz tu mini lista")
assert [len(x) for x in B.ML_PRACT["modelo"]] == [len(p["p"]) for p in B.ML_PRACT["lamina"]["pautas"]], "Haz tu mini lista: modelo"
for q in B.ML_Q: assert len(q["ops"]) == 3 and 0 <= q["ok"] < 3

# textos de estudiantes
STATS = []
ids = [t["id"] for t in B.TEXTOS]; assert len(ids) == len(set(ids))
for t in B.TEXTOS:
    l = t["lamina"]; ref = "Texto " + t["id"]
    check_lamina(l, ref)
    np_ = len(l["pautas"]); assert len(t["est"]) == np_, ref + ": falta el estado de alguna pauta"
    cub = set(p for par in t["par"] for p, _ in par if p)
    assert cub <= set(range(1, np_ + 1)), ref
    for i, (pa, e) in enumerate(zip(l["pautas"], t["est"])):
        assert all(0 <= m < len(pa["p"]) for m in e["miss"]) and len(set(e["miss"])) == len(e["miss"]), ref
        falta = len(e["miss"]) == len(pa["p"])
        assert falta == ((i + 1) not in cub), ref + ": pauta %d: %s pero %s frase" % (i + 1, "falta" if falta else "no falta", "tiene" if not falta else "no tiene")
        assert e["por"], ref
    n = tw(t["par"])
    lo, hi = (55, 75) if l["tarea"] == 1 else (60, 85)
    assert lo <= n <= hi, ref + ": %d palabras" % n
    txt = " ".join(x for par in t["par"] for _, x in par)
    if t["tipo"] == "Correo a un amigo": assert not US_PAL.search(txt), ref + ": usted en un correo de tú"
    if t["tipo"] == "Correo de usted": assert not TU_PAL.search(txt), ref + ": tú en un correo de usted: " + TU_PAL.search(txt).group(0)
    est = ["ok" if not e["miss"] else ("falta" if len(e["miss"]) == len(pa["p"]) else "medias") for pa, e in zip(l["pautas"], t["est"])]
    STATS.append((t["id"], n, est))
tipos = set(t["tipo"] for t in B.TEXTOS)
assert len(tipos) >= 5 and any(all(s == "ok" for s in st) for _, _, st in STATS), "Hace falta variedad y un texto completo"
assert all(any(s == k for _, _, st in STATS for s in st) for k in ("ok", "medias", "falta"))
for q in B.CUMPLE: assert 0 <= q["ok"] < len(B.CUMPLE_OPS)
for a in B.AHORA: check_lamina(a["lamina"], "Ahora tú " + a["id"])

# ------------------------------------------------------------ CSS
CSS_P = CSS + r"""
section.view > h3{margin-top:30px}
.row[hidden]{display:none}
.where{display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.04em;background:var(--ink);color:#fff;border-radius:999px;padding:2px 12px;margin-bottom:8px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px}
.box h4{margin:0 0 4px}.box p{margin:4px 0}
.keys{counter-reset:k;list-style:none;padding:0}
.keys li{counter-increment:k;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 14px 10px 52px;margin:8px 0;position:relative}
.keys li:before{content:counter(k);position:absolute;left:14px;top:8px;font-family:Georgia,serif;font-size:1.5rem;font-weight:700;color:var(--coral)}
.big{font-family:Georgia,serif;font-size:1.35rem;line-height:1.35;background:#fff;border:3px solid var(--coral);border-radius:14px;padding:16px 20px;margin:14px 0}
.big small{display:block;font-family:system-ui,sans-serif;font-size:.9rem;color:var(--muted);margin-top:6px}
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
.ad{border:2px dashed var(--ink);border-radius:8px;padding:10px 14px;margin:8px 0;text-align:center;font-size:.95rem}
.ad p{margin:2px 0}.ad p:first-child{font-weight:800;letter-spacing:.05em;font-family:Georgia,serif}
ul.ficha{background:#F6F3EF;border-radius:8px;padding:8px 14px 8px 30px;margin:8px 0;font-size:.93rem}
/* textos */
.letter{background:#fff;border:1px solid var(--line);border-left:5px solid var(--coral);border-radius:0 10px 10px 0;padding:14px 18px;font-size:1.02rem;line-height:1.85}
.letter p{margin:0 0 8px}
.pb{display:inline-grid;place-items:center;min-width:19px;height:19px;border-radius:50%;background:var(--ink);color:#fff;font-size:.68rem;font-weight:700;vertical-align:2px;margin-right:3px}
.letter .sg .pb{display:none}
.letter.shown .sg .pb{display:inline-grid}
.letter.shown .sg{border-radius:3px;padding:1px 2px}
.letter.shown .sg[data-p="1"]{background:#E4ECF8}.letter.shown .sg[data-p="2"]{background:#E3F1E8}.letter.shown .sg[data-p="3"]{background:#FBF0DA}
.letter.shown .sg[data-p="4"]{background:#ECE6F7}.letter.shown .sg[data-p="5"]{background:#DDF1F0}
.letter.shown .sg[data-p="0"].nf{background:var(--bad-soft);text-decoration:underline wavy var(--bad);text-underline-offset:4px}
.letter.shown .sg[data-p="0"].nf .pb{background:var(--bad)}
.ckrow{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}
.ck{display:inline-flex;align-items:center;gap:4px;border-radius:999px;padding:2px 10px;font-size:.85rem;font-weight:700}
.ck.y{background:var(--ok-soft);color:var(--ok)}.ck.n{background:var(--bad-soft);color:var(--bad)}.ck.h{background:var(--amb-soft);color:#7A4E0E}
.verd{border-radius:10px;padding:10px 14px;margin:8px 0;font-size:.95rem}
.verd.ok{background:var(--ok-soft)}.verd.bad{background:var(--bad-soft)}
.wc{font-size:.88rem;color:var(--muted);margin:6px 0}
/* piezas */
.anat{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:14px 18px;margin:12px 0}
.anat .pt{font-size:1.08rem;margin-bottom:8px}
.anat .pt span{border-radius:4px;padding:1px 3px}
.u1{background:#E4ECF8}.u2{background:#E3F1E8}.u3{background:#FBF0DA}
.pz{display:inline-block;border:1.5px solid var(--ink);border-radius:999px;padding:1px 10px;margin:2px 4px 2px 0;font-size:.86rem;font-weight:600;background:#fff}
.pz.ok{border-color:var(--ok);background:var(--ok-soft);color:var(--ok)}
.pz.no{border-color:var(--bad);background:var(--bad-soft);color:var(--bad);text-decoration:line-through}
/* mini lista */
.card{background:#FFFDF6;border:1px solid #D9CFA8;border-radius:4px;padding:12px 16px 12px 16px;font-family:"Bradley Hand","Segoe Print","Comic Sans MS",cursive;font-size:1.08rem;line-height:1.7;box-shadow:2px 3px 0 #EDE6CC;background-image:repeating-linear-gradient(transparent,transparent 29px,#D7E2F0 30px)}
.card .hd{font-weight:700;color:var(--coral);border-bottom:1.5px solid var(--coral);margin-bottom:4px}
.card .ln{display:flex;gap:8px;align-items:baseline}
.card .ln b{min-width:1.2em}
.card .bx{display:inline-block;width:14px;height:14px;border:1.5px solid #555;border-radius:2px;margin-left:4px;vertical-align:-1px}
.card .bx.v:after{content:"\2713";display:block;line-height:12px;font-size:14px;color:var(--ok);font-weight:700}
.card .gap{color:var(--bad);font-family:system-ui,sans-serif;font-size:.8rem;font-weight:700}
.cards3{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.cards3 .card{font-size:.95rem}
.cap{font-family:system-ui,sans-serif;font-size:.85rem;font-weight:700;margin:0 0 4px}
.cap.y{color:var(--ok)}.cap.n{color:var(--bad)}
.mlrow{display:grid;grid-template-columns:2.2em 1fr;gap:6px 10px;align-items:start;margin:8px 0}
.mlrow .bn{width:24px;height:24px;border-radius:50%;background:var(--ink);color:#fff;font-size:.8rem;font-weight:700;display:grid;place-items:center;margin-top:6px}
.mlrow .pt{font-size:.9rem;color:var(--muted)}
.mlrow input{width:100%;font:inherit;font-family:"Bradley Hand","Segoe Print","Comic Sans MS",cursive;font-size:1.05rem;border:1.5px solid #CFC6BB;border-radius:8px;padding:6px 10px;background:#FFFDF6}
.mlfb{font-size:.88rem;margin-top:3px}
.mlfb.ok{color:var(--ok)}.mlfb.no{color:var(--bad)}.mlfb.am{color:#7A4E0E}
.mlfb .mod{display:block;color:var(--ink);font-family:"Bradley Hand","Segoe Print","Comic Sans MS",cursive;font-size:1rem}
.blank .ln{min-height:30px}
/* ejercicios */
.ex{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin:14px 0}
.ex h4{margin:0 0 2px}.ex .ei{font-size:.92rem;color:var(--muted);margin:0 0 10px}
.ex .qn{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.ex .qs{font-size:.95rem;margin:4px 0 2px}
.ex .qp{font-weight:600;margin:4px 0}
.qop{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:10px;padding:9px 14px;margin:6px 0;cursor:pointer;color:inherit}
.qops.nums{display:flex;gap:8px;flex-wrap:wrap}
.qops.nums .qop{width:auto;min-width:110px;text-align:center}
.qop:hover:not(:disabled){border-color:var(--coral)}
.qop:disabled{cursor:default}
.qop.ok{border-color:var(--ok);background:var(--ok-soft)}
.qop.bad{border-color:var(--bad);background:var(--bad-soft)}
.fb{border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
.fb.ok{background:var(--ok-soft)}.fb.bad{background:var(--bad-soft)}
.score{font-family:Georgia,serif;font-size:2.2rem;font-weight:700}
.pick{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 12px}
.pick button{font:inherit;font-size:.86rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:4px 12px;cursor:pointer}
.pick button.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pick button.dn:not(.on){border-color:var(--ok);color:var(--ok)}
.prow{border-top:1px dashed var(--line);padding:10px 0}
.prow .pt{display:flex;gap:8px;align-items:flex-start}
.prow .pt .bn{flex:0 0 22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:.78rem;font-weight:700;display:grid;place-items:center;margin-top:2px}
.tri{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0 0 30px}
.tri button{font:inherit;font-size:.88rem;font-weight:600;border:2px solid var(--line);background:#fff;border-radius:999px;padding:4px 12px;cursor:pointer;color:inherit}
.tri button[aria-pressed="true"]{border-color:var(--ink);background:var(--ink);color:#fff}
.tri button.right{border-color:var(--ok);background:var(--ok-soft);color:var(--ok)}
.tri button.wrong{border-color:var(--bad);background:var(--bad-soft);color:var(--bad)}
.tri button:disabled{cursor:default}
.pres{margin:6px 0 0 30px;font-size:.93rem}
.legend3{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
.legend3 div{flex:1 1 200px;border-radius:10px;padding:8px 12px;font-size:.92rem}
.lec{background:var(--coral-soft);border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
/* ahora tu */
.ahora{background:#FFF8F2;border:2px solid var(--coral);border-radius:14px;padding:16px 18px;margin:14px 0}
.ahora h4{margin:16px 0 6px}
.ahora textarea{width:100%;font:inherit;font-size:1rem;line-height:1.7;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;min-height:220px;background:#fff;resize:vertical}
.ahora .sub{display:none}.ahora .sub.on{display:block}
.chk{list-style:none;padding:0;margin:8px 0}
.chk li{padding:6px 0;border-bottom:1px dashed var(--line)}
.chk label{display:inline-flex;gap:6px;align-items:center;cursor:pointer;margin-right:12px}
.chk input{width:19px;height:19px;accent-color:var(--ok)}
.chk label:has(input:checked) > span{color:var(--muted);text-decoration:line-through}
.chk .bn{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:.78rem;font-weight:700;margin-right:6px}
.saved{font-size:.82rem;color:var(--ok);min-height:1.2em}
.prog{font-weight:700;font-size:.95rem}
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
@media (max-width:760px){.two,.cards3{grid-template-columns:1fr}.tri,.pres{margin-left:0}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff}section.view{display:none!important}
 section.view.printme{display:block!important;padding-top:0}.card,.lam,.box{break-inside:avoid}}
""" + FT.CSS

# ------------------------------------------------------------ HTML de apoyo
def lamina_html(l):
    h = "Tarea %d" % l["tarea"] + (" · Opción %d" % l["op"] if l.get("op") else "")
    mn, mx = (60, 70) if l["tarea"] == 1 else (70, 80)
    o = ['<div class="lam"><div class="lh"><span>%s</span><span>%d-%d palabras</span></div>' % (h, mn, mx)]
    if l.get("instr"): o.append("<p>%s</p>" % l["instr"])
    if l.get("input"): o.append('<div class="msg">' + "".join("<p>%s</p>" % x for x in l["input"]) + "</div>")
    if l.get("anuncio"): o.append('<div class="ad">' + "".join("<p>%s</p>" % x for x in l["anuncio"]) + "</div>")
    if l.get("intro"): o.append("<p>%s</p>" % l["intro"])
    if l.get("photos"): o.append(FT.fotos_html(l))
    if l.get("ficha"): o.append('<ul class="ficha">' + "".join("<li>%s</li>" % x for x in l["ficha"]) + "</ul>")
    if l.get("intro2"): o.append("<p>%s</p>" % l["intro2"])
    if l.get("lead"): o.append("<p>%s</p>" % l["lead"])
    o.append('<ul class="pa">' + "".join('<li><span class="bn">%d</span>%s</li>' % (i + 1, p["t"]) for i, p in enumerate(l["pautas"])) + "</ul>")
    o.append('<div class="pw">Número de palabras recomendadas: entre %d y %d.</div></div>' % (mn, mx))
    return "".join(o)

def letter_html(par, shown=False, lid=""):
    o = []
    last = [s for p in par for s in p][-1]
    for p in par:
        segs = []
        for n, x in p:
            firma = n == 0 and (n, x) == last and words(x) <= 3
            cls = "sg" + ("" if n or firma else " nf")
            segs.append('<span class="%s" data-p="%d"><span class="pb" title="%s">%s</span>%s</span>' % (cls, n, "Pauta %d" % n if n else "sin pauta", n if n else "–", x) if not firma else x)
        o.append("<p>" + " ".join(segs) + "</p>")
    return '<div class="letter%s"%s>%s</div>' % (" shown" if shown else "", ' id="%s"' % lid if lid else "", "".join(o))

def pz_html(pz, miss=()):
    return "".join('<span class="pz%s">%s</span>' % ((" no" if i in miss else " ok") if miss is not None else "", x) for i, x in enumerate(pz))

def card_html(cab, lineas, ticks=False, gaps=None):
    o = ['<div class="card"><div class="hd">%s</div>' % cab]
    for i, ln in enumerate(lineas):
        txt = ", ".join(ln) if ln else ""
        bx = "".join('<span class="bx%s"></span>' % (" v" if ticks else "") for _ in ln)
        gap = ' <span class="gap">%s</span>' % gaps[i] if gaps and gaps[i] else ""
        o.append('<div class="ln"><b>%d.</b><span>%s%s%s</span></div>' % (i + 1, txt, bx, gap))
    return "".join(o) + "</div>"

# ------------------------------------------------------------ 1. LA REGLA
def regla_col(t):
    cub = set(p for par in t["par"] for p, _ in par if p)
    ck = "".join('<span class="ck %s">%d %s</span>' % ("y" if i in cub else "n", i, "✓" if i in cub else "✗") for i in range(1, NPR + 1))
    return ('<div><h4>%s</h4>%s<p class="wc">%d palabras</p><div class="ckrow" aria-label="Pautas">%s</div><div class="verd %s">%s</div></div>'
            % (t["tit"], letter_html(t["par"], True), tw(t["par"]), ck, "ok" if t["ok"] else "bad", t["nota"]))

rep_rows = "".join("<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>" % r for r in B.REPARTO)
V_REGLA = """
<span class="where">Escritura · Taller de escritura</span>
<h2>Cada pauta, al menos una frase</h2>
<p class="lead">En la prueba de Escritura, las <b>pautas</b> son los puntos de la lámina: lo que tienes que escribir. Son tu lista de control: antes de escribir, mientras escribes y al revisar.</p>
<div class="big">Un texto sencillo que cumple todas las pautas aprueba.<br>Uno difícil al que le falta una se queda en el límite.<small>El corrector pone dos notas: cómo escribes y si haces todo lo que pide la tarea. Son notas separadas: las frases difíciles no arreglan una pauta que falta. Si falta una, ya no puedes tener la nota más alta y estás en el límite; si falta otra (o una está a medias), todavía no es un A2.</small></div>
<h3>Míralo con un ejemplo</h3>
<p>Esta es la tarea. Dos estudiantes, Lucía y Max, contestan a Jorge.</p>
""" + lamina_html(R["lamina"]) + """
<div class="two">""" + "".join(regla_col(t) for t in R["textos"]) + """</div>
<p>Cada número es una pauta. Max escribe mejor que Lucía, con frases de nivel B1... pero Jorge le hacía una pregunta y Max no la contesta. Para el corrector, <b>la tarea de Max no está completa</b>: con una pauta que falta, Max se queda en el límite del aprobado, aunque sus frases sean mejores. Lucía, con frases sencillas, aprueba tranquila.</p>

<h3>Tres formas de perder una pauta</h3>
<div class="legend3">
 <div style="background:var(--ok-soft)"><b>✓ Completa</b><br>Cada parte de la pauta tiene su frase.</div>
 <div style="background:var(--amb-soft)"><b>½ A medias</b><br>Falta una parte: el «por qué», el «con quién», la despedida...</div>
 <div style="background:var(--bad-soft)"><b>✗ Falta</b><br>No hay ninguna frase para esa pauta (o la frase habla de otra cosa).</div>
</div>
<p>Una pauta a medias también baja la nota. Por eso en este taller vas a aprender a <b>desmontar</b> cada pauta en sus partes (las llamamos <b>piezas</b>) y a hacer una <b>mini lista</b> antes de escribir.</p>

<h3>Una frase... pero no cinco</h3>
<p>Si escribes mucho de una pauta, no te quedan palabras para la última. Reparte las líneas (en el examen escribes a mano: <b>unas 10 palabras por línea</b>, cuéntalas a ojo, sin contar palabra por palabra):</p>
<table class="t"><thead><tr><th>Tarea</th><th>Extensión</th><th>Para cada pauta</th></tr></thead><tbody>""" + rep_rows + """</tbody></table>
<div class="tip">No es una regla exacta: una pauta puede tener una línea y otra dos. Lo importante es que <b>ninguna pauta se quede sin su frase</b> y que ninguna se coma el espacio de las demás.</div>
<div class="row"><button class="btn cta" data-go="leer">Siguiente: leer una pauta</button></div>
"""

# ------------------------------------------------------------ 2. LEER UNA PAUTA
verb_rows = "".join("<tr><td><b>%s</b></td><td>%s</td><td><i>%s</i></td></tr>" % v for v in B.VERBOS)
pis_rows = "".join("<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>" % v for v in B.PISTAS)
V_LEER = """
<span class="where">Paso 1 · Leer</span>
<h2>Leer una pauta: desmontarla en piezas</h2>
<p class="lead">Muchas pautas piden dos o tres cosas a la vez. Si lees rápido, ves una y te olvidas de las otras. Antes de escribir, desmonta cada pauta: <b>cada pieza, una frase</b> (o una parte de una frase).</p>
<h3>Una pauta tiene tres cosas</h3>
<div class="anat">
 <div class="pt"><span class="u1">decir</span> <span class="u2">qué plato</span> <span class="u3">va a llevar</span> y <span class="u1">explicar</span> <span class="u2">cómo se prepara</span>;</div>
 <ol style="margin:0;padding-left:1.2em">
  <li><span class="u1"><b>Qué haces</b></span>: el verbo (decir, explicar, contar, proponer...).</li>
  <li><span class="u2"><b>Las piezas</b></span>: las preguntas escondidas (qué, dónde, cuándo, con quién, cómo, por qué...). Aquí hay dos: <span class="pz">qué plato</span><span class="pz">cómo se prepara</span></li>
  <li><span class="u3"><b>El tiempo</b></span>: «va a llevar» pide futuro (<i>voy a llevar...</i>); «cómo se prepara», presente.</li>
 </ol>
</div>
<div class="tip"><b>Las pautas dobles cuentan como dos cosas.</b> «Decir qué hizo y con quién» son dos piezas: si solo cuentas qué hiciste, la pauta queda a medias.</div>
<h3>Cómo contar las piezas</h3>
<table class="t"><thead><tr><th>En la pauta</th><th>Quiere decir</th><th>Ejemplo</th></tr></thead><tbody>""" + pis_rows + """</tbody></table>
<h3>Qué pide cada verbo</h3>
<table class="t"><thead><tr><th>Si la pauta dice...</th><th>Escribe...</th><th>Por ejemplo</th></tr></thead><tbody>""" + verb_rows + """</tbody></table>
<div class="tip"><b>En la tarea 1, lee también el correo que recibes.</b> Las preguntas de tu amigo («¿Tú conoces Bilbao?») casi siempre son una pauta: «responder a su pregunta».</div>
<div class="noprint">
<h3>Practica</h3>
<div class="ex" id="ex-piezas"></div>
<div class="ex" id="ex-tiempos"></div>
</div>
<div class="row"><button class="btn" data-act="print" data-p="leer">Imprimir las tablas</button><button class="btn cta" data-go="lista">Siguiente: tu mini lista</button></div>
"""

# ------------------------------------------------------------ 3. LA MINI LISTA
M = B.MINI
pasos = "".join("<li><b>%s.</b> %s</li>" % p for p in B.MINI_PASOS)
gaps_inc = []
for full, inc in zip(M["lista"], M["incompleta"]):
    gaps_inc.append("" if len(inc) == len(full) else ("← falta la pauta" if not inc else "← falta %d" % (len(full) - len(inc))))
mlp_rows = "".join('<div class="mlrow"><span class="bn">%d</span><div><div class="pt">%s</div><input type="text" data-ml="%d" aria-label="Mini lista, pauta %d" autocomplete="off"><div class="mlfb" data-mlfb="%d" role="status"></div></div></div>'
                   % (i + 1, p["t"], i, i + 1, i) for i, p in enumerate(B.ML_PRACT["lamina"]["pautas"]))
blank = '<div class="card blank"><div class="hd">TÚ / USTED · tipo de texto: ..................</div>' + "".join('<div class="ln"><b>%d.</b><span></span></div>' % i for i in range(1, 6)) + "</div>"
V_LISTA = """
<span class="where">Paso 2 · Antes de escribir</span>
<h2>Tu mini lista: un minuto que salva la tarea</h2>
<p class="lead">Antes de escribir, convierte las pautas en una <b>mini lista</b> en tu hoja de notas: palabras clave, no frases. Te ayuda a no olvidar nada y te dice qué escribir en cada momento.</p>
<div class="tip"><b>¿Cuándo?</b> En los 5 minutos de leer y elegir: <b>un minuto por tarea</b>. Es tiempo bien usado: después escribes más rápido porque ya sabes qué decir.</div>
<h3>Cómo se hace</h3>
<ol class="keys">""" + pasos + """</ol>
<h3>Un ejemplo</h3>
""" + lamina_html(M["lamina"]) + """
<p>Así es una buena mini lista para esta tarea: cinco líneas, las piezas separadas por comas y una casilla para marcar cada pieza cuando la escribes.</p>
""" + card_html(M["cabecera"], M["lista"], ticks=True) + """
<p class="small muted">«(pres.)» al lado de la línea 5: esa pauta va en presente, no en pasado como las demás.</p>
<div class="cards3">
 <div><p class="cap n">✗ Con frases: tardas mucho</p><div class="card"><div class="hd">&nbsp;</div><div class="ln"><span>""" + M["frases"] + """</span></div></div><p class="small">A los 4 minutos todavía estás en la pauta 1. La frase la escribes en el texto, no en la lista.</p></div>
 <div><p class="cap n">✗ Sin todas las piezas</p>""" + card_html(M["cabecera"], M["incompleta"], gaps=gaps_inc) + """<p class="small">Rápida, pero con huecos: falta el «por qué», «a quién conoció»... y la pauta 4 entera.</p></div>
</div>
<div class="noprint">
<h3>Practica</h3>
<div class="ex" id="ex-mlq"></div>
<div class="ex" id="ex-mlp">
 <h4>Haz tu mini lista</h4>
 <p class="ei">Lee la tarea y escribe tu mini lista: una línea por pauta, piezas separadas por comas, palabras clave. Después compárala con la lista modelo.</p>
 """ + lamina_html(B.ML_PRACT["lamina"]) + """
 <p class="small"><b>Arriba de tu lista:</b> ¿tú o usted? Inés es una amiga: <b>TÚ</b>.</p>
 """ + mlp_rows + """
 <div class="mlres"></div>
 <div class="row" style="margin-bottom:0"><button class="btn cta" data-act="mlcheck">Comparar con la lista modelo</button></div>
</div>
</div>
<h3>Tu mini lista en blanco</h3>
<p>Imprímela y úsala en casa hasta que la hagas sin pensar. En el examen la escribes en la hoja de notas.</p>
""" + blank + """
<div class="row"><button class="btn" data-act="print" data-p="lista">Imprimir el ejemplo y la lista en blanco</button><button class="btn cta" data-go="falta">Siguiente: ¿qué falta?</button></div>
"""

# ------------------------------------------------------------ 4. ¿QUE FALTA?
casos = "".join("<li>%s</li>" % c for c in B.CASOS)
V_FALTA = """
<span class="where">Paso 3 · Revisar</span>
<h2>¿Qué falta? Revisa textos de otros estudiantes</h2>
<p class="lead">Es más fácil ver los fallos en el texto de otra persona. Lee cada texto con la lámina al lado y decide, pauta por pauta: <b>✓ completa</b>, <b>½ a medias</b> o <b>✗ falta</b>. Así entrenas los ojos para revisar tus textos.</p>
<h3>Lo que más se olvida</h3>
<ul>""" + casos + """</ul>
<div class="noprint">
<h3>Practica</h3>
<div class="ex" id="ex-pp"></div>
<div class="ex" id="ex-cumple"></div>
</div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

# ------------------------------------------------------------ 5. AHORA TU
def checks_for(a):
    return B.CHECK_COMUN + (B.CHECK_CORREO if a["trato"] else B.CHECK_TEXTO)

def ahora_html(a):
    l = a["lamina"]
    ml = "".join('<div class="mlrow"><span class="bn">%d</span><div><div class="pt">%s</div><input type="text" data-al="%s|%d" aria-label="Mini lista, pauta %d" autocomplete="off"><div class="mlfb" data-alfb="%s|%d" role="status"></div></div></div>'
                 % (i + 1, p["t"], a["id"], i, i + 1, a["id"], i) for i, p in enumerate(l["pautas"]))
    rev = "".join('<li><span class="bn">%d</span>%s</li>' % (i + 1, "".join('<label><input type="checkbox" data-wc="%s|p%d-%d"><span>%s</span></label>' % (a["id"], i, j, x) for j, x in enumerate(p["p"])))
                  for i, p in enumerate(l["pautas"]))
    rev += "".join('<li><label><input type="checkbox" data-wc="%s|c%d"><span>%s</span></label></li>' % (a["id"], k, x) for k, x in enumerate(checks_for(a)))
    trato = {"tu": "Arriba de tu lista: <b>TÚ</b> (escribes a una amiga).", "usted": "Arriba de tu lista: <b>USTED</b> (escribes a alguien que no conoces).", None: "Arriba de tu lista: el tipo de texto y el tiempo principal."}[a["trato"]]
    return ('<div class="sub" data-sub="%s">%s'
            '<h4>1. Tu mini lista</h4><p class="small">%s Una línea por pauta, piezas separadas por comas.</p>%s'
            '<div class="row" style="margin:8px 0"><button class="btn sm" data-act="alcheck" data-a="%s">Comprobar mi lista</button></div>'
            '<h4>2. Escribe</h4><p class="small">Si puedes, escribe primero en papel, a mano, y cuenta las líneas a ojo (unas 10 palabras por línea). Después cópialo aquí para enviarlo a tu profesora. Escribe con la mini lista al lado.</p>'
            '<textarea data-w="%s" aria-label="Tu texto" placeholder="Escribe aquí tu texto..."></textarea><div class="saved" data-sv="%s" role="status"></div>'
            '<h4>3. Revisa con tu lista</h4><p class="small">Lee tu texto pieza por pieza. Marca solo lo que de verdad está escrito.</p><ul class="chk">%s</ul>'
            '<p class="prog" data-prog="%s"></p></div>'
            % (a["id"], lamina_html(l), trato, ml, a["id"], a["id"], a["id"], rev, a["id"]))

pick_a = "".join('<button type="button" data-act="apick" data-a="%s">%s</button>' % (a["id"], a["n"]) for a in B.AHORA)
V_AHORA = """
<span class="where">Ahora tú</span>
<h2>Ahora tú: escribe revisando con la lista</h2>
<p class="lead">Elige una tarea y hazla con los tres pasos: <b>mini lista → texto → revisión pieza por pieza</b>. Puedes hacer las cuatro.</p>
<div class="ahora">
 <div class="pick" id="apick" role="group" aria-label="Elige una tarea">""" + pick_a + """</div>
 """ + "".join(ahora_html(a) for a in B.AHORA) + """
 <p class="small muted">Tu lista, tu texto y tu revisión se guardan en este navegador. Para enviarlos, ve a <b>Tu opinión</b> y pulsa <b>Copiar</b>.</p>
</div>
<div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button></div>
"""

# ------------------------------------------------------------ VISTAS
STEPS = [("regla", "La regla"), ("leer", "Leer una pauta"), ("lista", "Tu mini lista"), ("falta", "¿Qué falta?"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo. Al copiar, también se copian tus mini listas y tus textos de «Ahora tú» para que tu profesora los corrija.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué te pasa más a menudo cuando escribes?</label>
 <div class="chips" role="group" aria-labelledby="o1l">__CHIPS1__</div>
 <label class="q" id="o2l">2. ¿Vas a hacer la mini lista antes de escribir?</label>
 <div class="chips" role="group" aria-labelledby="o2l">__CHIPS2__</div>
 <label class="q" id="o3l">3. ¿Qué parte te ha ayudado más?</label>
 <div class="chips" role="group" aria-labelledby="o3l">__CHIPS3__</div>
 <label class="q" for="o4">4. ¿Qué tipo de pauta o de texto te cuesta más? ¿Hay algo que no has entendido?</label>
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
V_OPINION = (V_OPINION.replace("__CHIPS1__", chips("o1", ["Me olvido de una pauta", "Hago una pauta a medias", "No entiendo bien qué pide la pauta", "Escribo mucho de una y no llego a la última", "No me pasa"]))
             .replace("__CHIPS2__", chips("o2", ["Sí, me ayuda", "A veces", "No, prefiero escribir directamente"]))
             .replace("__CHIPS3__", chips("o3", [l for k, l in STEPS[:5]]))
             .replace("__EMAIL__", EMAIL))

views = {"regla": V_REGLA, "leer": V_LEER, "lista": V_LISTA, "falta": V_FALTA, "ahora": V_AHORA, "opinion": V_OPINION}
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
body = BODY.replace("__TITLE__", TITLE).replace("__VIEWS__", "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS))

# ------------------------------------------------------------ DATOS PARA EL JS
def pz_por(pz, nota):
    return "Pide %d: %s%s" % (len(pz), pz_html(pz, None), (" " + nota) if nota else "")
nops = ["1 cosa", "2 cosas", "3 cosas", "4 cosas"]
EJ = {
 "piezas": {"t": "¿Cuántas cosas pide?", "i": "Lee la pauta y cuenta las piezas. Ocho pautas de láminas distintas.", "fixed": True, "nums": True, "pick": 8,
            "items": [{"ctx": "Pauta:", "p": "«%s»" % p, "ops": nops, "ok": len(pz) - 1, "por": pz_por(pz, n)} for p, pz, n in B.PIEZAS]},
 "tiempos": {"t": "¿Qué tiempo pide?", "i": "Mira las palabras de la pauta: ¿hoy, ya pasó o es un plan?", "fixed": True,
             "items": [{"ctx": "Pauta:", "p": "«%s»" % p, "ops": B.TIEMPOS_OPS, "ok": k, "por": por} for p, k, por in B.TIEMPOS]},
 "mlq": {"t": "¿Qué línea es mejor?", "i": "Cinco pautas y tres líneas de mini lista. Elige la mejor.", "items": B.ML_Q},
 "cumple": {"t": "¿Cumple la pauta?", "i": "Una pauta y la frase que ha escrito un estudiante. ¿La cumple?", "fixed": True, "pick": 8,
            "items": [dict(q, ops=B.CUMPLE_OPS) for q in B.CUMPLE]},
}
TEXTOS_JS = []
for t in B.TEXTOS:
    l = t["lamina"]
    TEXTOS_JS.append({"id": t["id"], "tipo": t["tipo"], "autor": t["autor"], "tarea": l["tarea"], "lam": lamina_html(l),
                      "let": letter_html(t["par"], False, "let-" + t["id"]), "lec": t["leccion"], "w": tw(t["par"]),
                      "pautas": [{"t": p["t"], "p": p["p"], "miss": e["miss"], "por": e["por"]} for p, e in zip(l["pautas"], t["est"])]})
AHORA_JS = [{"id": a["id"], "n": a["n"], "tarea": a["lamina"]["tarea"], "task": a["lamina"].get("instr") or a["lamina"].get("intro"),
             "pautas": [{"t": p["t"], "p": p["p"]} for p in a["lamina"]["pautas"]], "nchk": len(checks_for(a))} for a in B.AHORA]
MLP = {"pautas": [{"t": p["t"], "p": p["p"]} for p in B.ML_PRACT["lamina"]["pautas"]], "modelo": B.ML_PRACT["modelo"]}
TABEX = {"leer": ["piezas", "tiempos"], "lista": ["mlq", "mlp"], "falta": ["p_" + t["id"] for t in B.TEXTOS] + ["cumple"]}
EXNAME = {"piezas": "¿Cuántas cosas pide?", "tiempos": "¿Qué tiempo pide?", "mlq": "¿Qué línea es mejor?", "mlp": "Haz tu mini lista", "cumple": "¿Cumple la pauta?"}
for t in B.TEXTOS: EXNAME["p_" + t["id"]] = "¿Qué falta? %s (%s)" % (t["tipo"], t["autor"])
DATA = {"key": STORAGE, "steps": [{"id": k, "label": l} for k, l in STEPS], "ej": EJ, "textos": TEXTOS_JS, "ahora": AHORA_JS,
        "mlp": MLP, "tabex": TABEX, "exname": EXNAME}

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function blank(){ return {cur:'regla', seen:{}, ex:{}, ml:[], al:{}, w:{}, wc:{}, pp:D.textos[0].id, ap:D.ahora[0].id, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function shuffle(a){ for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function rec(id, ok, n){ var r=S.ex[id]; if(!r || ok>r.b || (ok===r.b && n!==r.n)) S.ex[id]={b:ok, n:n, l:ok}; else r.l=ok; save(); nav(); }

/* ---------------- navegacion ---------------- */
function tabDone(id){
 if(id==='regla') return !!S.seen.regla;
 if(id==='opinion') return !!(S.o1||S.o2||S.o3||S.o4||S.o5);
 if(id==='ahora') return D.ahora.some(function(a){ return S.w[a.id] && S.w[a.id].trim(); });
 var ex=D.tabex[id]||[]; return ex.length>0 && ex.every(function(e){ return !!S.ex[e]; });
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
 if(id==='opinion') summary();
 nav(); window.scrollTo(0,0);
}

/* ---------------- ejercicio q: elegir una opcion (una a una) ---------------- */
var Q={};
function qNew(id){ var e=D.ej[id], idx=shuffle(range(e.items.length)); if(e.pick) idx=idx.slice(0,e.pick);
 Q[id]={k:0, ok:0, ans:false, idx:idx, ord:idx.map(function(i){ var n=e.items[i].ops.length; return e.fixed?range(n):shuffle(range(n)); })}; qRender(id); }
function qRender(id){
 var e=D.ej[id], q=Q[id], box=$('ex-'+id), n=q.idx.length;
 var head='<h4>'+esc(e.t)+'</h4><p class="ei">'+esc(e.i)+'</p>';
 if(q.k>=n){
  rec(id, q.ok, n);
  box.innerHTML=head+'<div class="qn">RESULTADO</div><div class="score">'+q.ok+' / '+n+'</div><p>'+(q.ok===n?'¡Perfecto!':(q.ok>=n-2?'¡Muy bien! Mira otra vez las que has fallado.':'Vuelve a leer la explicación de arriba y prueba otra vez.'))+'</p>'+
   '<p class="small muted">Tu mejor resultado: '+S.ex[id].b+' / '+S.ex[id].n+'</p><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="qnew" data-ex="'+id+'">Otra vez'+(e.pick?' (otras frases)':'')+'</button></div>';
  return;
 }
 var it=e.items[q.idx[q.k]], o=head+'<div class="qn">'+(q.k+1)+' DE '+n+'</div><p class="qs">'+esc(it.ctx)+'</p>'+(it.p?'<p class="qp">'+esc(it.p)+'</p>':'')+'<div class="qops'+(e.nums?' nums':'')+'" role="group" aria-label="Opciones">';
 q.ord[q.k].forEach(function(i){ o+='<button type="button" class="qop" data-act="qpick" data-ex="'+id+'" data-i="'+i+'">'+esc(it.ops[i])+'</button>'; });
 o+='</div><div class="qfb"></div><div class="row qnx" style="margin-bottom:0" hidden><button class="btn cta" data-act="qnext" data-ex="'+id+'">'+(q.k===n-1?'Ver el resultado':'Siguiente')+'</button></div>';
 box.innerHTML=o;
}
function qPick(b){
 var id=b.getAttribute('data-ex'), q=Q[id], it=D.ej[id].items[q.idx[q.k]], box=$('ex-'+id); if(q.ans) return;
 var i=+b.getAttribute('data-i'), ok=i===it.ok; if(ok) q.ok++; q.ans=true;
 [].forEach.call(box.querySelectorAll('.qop'), function(x){ x.disabled=true; var j=+x.getAttribute('data-i'); if(j===it.ok) x.classList.add('ok'); else if(j===i) x.classList.add('bad'); });
 box.querySelector('.qfb').innerHTML='<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Correcto!':'No es esa: '+esc(it.ops[it.ok])+'.')+'</b> '+it.por+'</div>';
 box.querySelector('.qnx').hidden=false; box.querySelector('.qnx button').focus();
}

/* ---------------- mini lista: comprobar lineas ---------------- */
function items(v){ return String(v||'').split(/[,;\/+\n]| - | · /).map(function(x){ return x.trim(); }).filter(function(x){ return x.replace(/[^\wÀ-ſ¿?¡!]/g,'').length>0; }); }
function nwords(s){ return (s.match(/[\wÀ-ſ]+/g)||[]).length; }
function lineFb(v, need){
 var it=items(v), n=it.length, long=it.some(function(x){ return nwords(x)>6; });
 if(!n) return {c:'no', ok:false, t:'Línea vacía: esta pauta pide '+need+(need>1?' cosas':' cosa')+'.'};
 if(long) return {c:'am', ok:false, t:'Parece una frase: usa palabras clave (2-4 palabras por pieza).'+(n<need?' Y la pauta pide '+need+' cosas.':'')};
 if(n<need) return {c:'no', ok:false, t:'Tienes '+n+(n>1?' cosas':' cosa')+'; la pauta pide '+need+'. ¿Qué falta? Sepáralas con comas.'};
 return {c:'ok', ok:true, t:'✓ '+need+' de '+need};
}
function mlCheck(){
 var box=$('ex-mlp'), ok=0, n=D.mlp.pautas.length;
 D.mlp.pautas.forEach(function(p,i){ var f=lineFb(S.ml[i], p.p.length); if(f.ok) ok++;
  box.querySelector('[data-mlfb="'+i+'"]').innerHTML='<span class="mlfb '+f.c+'" style="display:block">'+esc(f.t)+'</span><span class="mod">Modelo: '+esc(D.mlp.modelo[i].join(', '))+'</span>';
  box.querySelector('[data-mlfb="'+i+'"]').className='mlfb'; });
 box.querySelector('.mlres').innerHTML='<div class="fb '+(ok===n?'ok':'bad')+'"><b>'+ok+' de '+n+' líneas completas.</b> '+(ok===n?'¡Muy bien! Tu lista tiene todas las piezas.':'Mira los avisos de cada línea y la lista modelo. Tu lista no tiene que ser igual: tiene que tener todas las piezas.')+'</div>';
 rec('mlp', ok, n);
}
function alCheck(aid){
 var a=D.ahora.filter(function(x){ return x.id===aid; })[0], al=S.al[aid]||[], ok=0;
 a.pautas.forEach(function(p,i){ var f=lineFb(al[i], p.p.length); if(f.ok) ok++; var el=document.querySelector('[data-alfb="'+aid+'|'+i+'"]'); el.className='mlfb '+f.c; el.textContent=f.t; });
}

/* ---------------- ¿que falta? ---------------- */
var STATE=['ok','medias','falta'], LBL={ok:'✓ Completa', medias:'½ A medias', falta:'✗ Falta'};
var P={ans:{}, done:false};
function pState(p){ return !p.miss.length?'ok':(p.miss.length===p.p.length?'falta':'medias'); }
function ppRender(){
 var box=$('ex-pp'), t=D.textos.filter(function(x){ return x.id===S.pp; })[0]; if(!t){ t=D.textos[0]; S.pp=t.id; }
 P={ans:{}, done:false};
 var pick='<div class="pick" role="group" aria-label="Elige un texto">'+D.textos.map(function(x,i){ return '<button type="button" class="'+(x.id===t.id?'on ':'')+(S.ex['p_'+x.id]?'dn':'')+'" data-act="pppick" data-t="'+x.id+'">'+(i+1)+'. '+esc(x.tipo)+(S.ex['p_'+x.id]?' ✓':'')+'</button>'; }).join('')+'</div>';
 var rows=t.pautas.map(function(p,i){
  return '<div class="prow" data-row="'+i+'"><div class="pt"><span class="bn">'+(i+1)+'</span><span>'+esc(p.t)+'</span></div><div class="tri" role="group" aria-label="Pauta '+(i+1)+'">'+
   STATE.map(function(s){ return '<button type="button" data-act="ppans" data-i="'+i+'" data-s="'+s+'" aria-pressed="false">'+LBL[s]+'</button>'; }).join('')+'</div><div class="pres"></div></div>';
 }).join('');
 box.innerHTML='<h4>¿Qué falta?</h4><p class="ei">Ocho textos de estudiantes: correos de tú y de usted, revista, diario, biografía y fotos. Elige uno, léelo con la lámina y marca cada pauta.</p>'+pick+
  t.lam+'<p class="small"><b>El texto de '+esc(t.autor)+'</b></p>'+t.let+'<p class="wc">Unas '+t.w+' palabras.</p>'+
  '<h4 style="margin-top:12px">¿Cómo están las pautas?</h4>'+rows+'<div class="ppres"></div>'+
  '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="ppcheck">Comprobar</button><button class="btn" data-act="ppnext">Siguiente texto</button></div>';
}
function ppAns(b){
 if(P.done) return; var i=+b.getAttribute('data-i'); P.ans[i]=b.getAttribute('data-s');
 [].forEach.call(b.parentNode.querySelectorAll('button'), function(x){ x.setAttribute('aria-pressed', x===b?'true':'false'); });
}
function ppCheck(){
 if(P.done) return;
 var t=D.textos.filter(function(x){ return x.id===S.pp; })[0], box=$('ex-pp'), ok=0;
 t.pautas.forEach(function(p,i){
  var right=pState(p), a=P.ans[i], row=box.querySelector('[data-row="'+i+'"]'), good=a===right; if(good) ok++;
  [].forEach.call(row.querySelectorAll('.tri button'), function(x){ x.disabled=true; var s=x.getAttribute('data-s'); if(s===right) x.classList.add('right'); else if(s===a) x.classList.add('wrong'); x.setAttribute('aria-pressed', s===a?'true':'false'); });
  row.querySelector('.pres').innerHTML=(good?'<b style="color:var(--ok)">✓ Bien.</b> ':(a?'<b style="color:var(--bad)">No: está '+LBL[right].slice(2).toLowerCase()+'.</b> ':'<b style="color:var(--bad)">Sin marcar: está '+LBL[right].slice(2).toLowerCase()+'.</b> '))+
   p.p.map(function(x,j){ return '<span class="pz '+(p.miss.indexOf(j)>=0?'no':'ok')+'">'+esc(x)+'</span>'; }).join('')+'<br>'+esc(p.por);
 });
 P.done=true; $('let-'+t.id).classList.add('shown');
 box.querySelector('.ppres').innerHTML='<div class="fb '+(ok===t.pautas.length?'ok':'bad')+'"><b>'+ok+' de '+t.pautas.length+' pautas bien juzgadas.</b> En el texto, cada frase lleva ahora el número de su pauta'+(box.querySelector('.nf')?'; en rojo, la frase que no responde a ninguna':'')+'.</div><div class="lec"><b>La lección:</b> '+esc(t.lec)+'</div>';
 rec('p_'+t.id, ok, t.pautas.length);
 var pk=box.querySelector('[data-t="'+t.id+'"]'); if(pk){ pk.classList.add('dn'); if(pk.textContent.indexOf('✓')<0) pk.textContent+=' ✓'; }
}
function ppNext(){ var i=D.textos.map(function(x){ return x.id; }).indexOf(S.pp); S.pp=D.textos[(i+1)%D.textos.length].id; save(); ppRender(); $('ex-pp').scrollIntoView({behavior:'smooth'}); }

/* ---------------- ahora tu ---------------- */
function aShow(aid){
 S.ap=aid; save();
 [].forEach.call(document.querySelectorAll('[data-sub]'), function(s){ s.classList.toggle('on', s.getAttribute('data-sub')===aid); });
 [].forEach.call(document.querySelectorAll('#apick button'), function(b){ var id=b.getAttribute('data-a'); b.classList.toggle('on', id===aid); b.classList.toggle('dn', !!(S.w[id]&&S.w[id].trim())); });
}
function prog(aid){
 var a=D.ahora.filter(function(x){ return x.id===aid; })[0], tot=0, n=0;
 a.pautas.forEach(function(p,i){ p.p.forEach(function(_,j){ tot++; if(S.wc[aid+'|p'+i+'-'+j]) n++; }); });
 var el=document.querySelector('[data-prog="'+aid+'"]'); if(el) el.textContent = n===tot ? '✓ Todas las piezas revisadas ('+n+' de '+tot+').' : 'Piezas revisadas: '+n+' de '+tot+'.';
 return {n:n, tot:tot};
}
function nChecks(aid){ var n=0; for(var k in S.wc){ if(S.wc[k] && k.split('|')[0]===aid && k.split('|')[1].charAt(0)==='c') n++; } return n; }
function initWriting(){
 [].forEach.call(document.querySelectorAll('input[data-ml]'), function(t){ t.value=S.ml[+t.getAttribute('data-ml')]||''; });
 [].forEach.call(document.querySelectorAll('input[data-al]'), function(t){ var k=t.getAttribute('data-al').split('|'); t.value=(S.al[k[0]]||[])[+k[1]]||''; });
 [].forEach.call(document.querySelectorAll('textarea[data-w]'), function(t){ t.value=S.w[t.getAttribute('data-w')]||''; });
 [].forEach.call(document.querySelectorAll('input[data-wc]'), function(c){ c.checked=!!S.wc[c.getAttribute('data-wc')]; });
 D.ahora.forEach(function(a){ prog(a.id); });
 aShow(D.ahora.some(function(a){ return a.id===S.ap; }) ? S.ap : D.ahora[0].id);
}
var svT={};
function savedMsg(id){ var el=document.querySelector('[data-sv="'+id+'"]'); if(!el) return; el.textContent='✓ Guardado en este navegador'; clearTimeout(svT[id]); svT[id]=setTimeout(function(){ el.textContent=''; },1800); }

/* ---------------- opinion ---------------- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked = r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function allEx(){ var a=[]; ['leer','lista','falta'].forEach(function(t){ a=a.concat(D.tabex[t]); }); return a; }
function summary(){
 var ex=allEx(), done=ex.filter(function(e){ return S.ex[e]; }).length, tx=D.ahora.filter(function(a){ return S.w[a.id] && S.w[a.id].trim(); });
 $('sum').innerHTML='<li>Ejercicios hechos: '+done+' de '+ex.length+'.</li><li>Textos escritos en «Ahora tú»: '+(tx.length?tx.map(function(a){ return esc(a.n); }).join(', '):'ninguno todavía')+'.</li>';
}
function pack(){
 var L=['CURSO DELE A2 - ESCRITURA: LAS PAUTAS COMO LISTA DE CONTROL', 'Nombre: '+(S.name||'-'), '', 'EJERCICIOS (mejor resultado):'];
 allEx().forEach(function(id){ var r=S.ex[id]; L.push('  '+D.exname[id]+': '+(r?(id==='mlp'?r.b+'/'+r.n+' líneas completas':r.b+'/'+r.n):'sin hacer')); });
 if(S.ml.some(function(x){ return x && x.trim(); })){ L.push('', 'MI MINI LISTA (ejercicio del curso de fotografía):'); D.mlp.pautas.forEach(function(p,i){ L.push('  '+(i+1)+'. '+(S.ml[i]||'-')); }); }
 L.push('', 'MIS TEXTOS ("Ahora tú"):');
 var any=false;
 D.ahora.forEach(function(a){ var w=(S.w[a.id]||'').trim(), al=S.al[a.id]||[]; if(!w && !al.some(function(x){ return x && x.trim(); })) return; any=true; var pr=prog(a.id);
  L.push('', '== '+a.n+' (tarea '+a.tarea+') ==', 'Tarea: '+a.task, 'Mi mini lista:');
  a.pautas.forEach(function(p,i){ L.push('  '+(i+1)+'. '+(al[i]||'-')); });
  L.push('Revisión: '+pr.n+' de '+pr.tot+' piezas marcadas; '+nChecks(a.id)+' de '+a.nchk+' puntos generales', '', w||'(sin texto todavía)'); });
 if(!any) L.push('  (todavía no he escrito ninguno)');
 L.push('', 'OPINIÓN:', '1. Lo que me pasa más: '+(S.o1||'-'), '2. ¿Voy a hacer la mini lista?: '+(S.o2||'-'), '3. La parte que más me ha ayudado: '+(S.o3||'-'), '4. Lo que me cuesta / no he entendido: '+(S.o4||'-'), '5. Sensación de control en la Escritura (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 qnew:function(b){ qNew(b.getAttribute('data-ex')); },
 qpick:function(b){ qPick(b); },
 qnext:function(b){ var id=b.getAttribute('data-ex'); Q[id].k++; Q[id].ans=false; qRender(id); },
 mlcheck:function(){ mlCheck(); },
 alcheck:function(b){ alCheck(b.getAttribute('data-a')); },
 pppick:function(b){ S.pp=b.getAttribute('data-t'); save(); ppRender(); },
 ppans:function(b){ ppAns(b); },
 ppcheck:function(){ ppCheck(); },
 ppnext:function(){ ppNext(); },
 apick:function(b){ aShow(b.getAttribute('data-a')); },
 print:function(b){ var v=$('v-'+b.getAttribute('data-p')); v.classList.add('printme'); window.print(); setTimeout(function(){ v.classList.remove('printme'); },500); },
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
 if(t.getAttribute('data-wc')){ S.wc[t.getAttribute('data-wc')]=t.checked; save(); prog(t.getAttribute('data-wc').split('|')[0]); return; }
 if(t.name==='o1'||t.name==='o2'||t.name==='o3'||t.name==='o5'){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){ var t=e.target;
 if(t.getAttribute('data-ml')!==null){ S.ml[+t.getAttribute('data-ml')]=t.value; save(); return; }
 if(t.getAttribute('data-al')){ var k=t.getAttribute('data-al').split('|'); if(!S.al[k[0]]) S.al[k[0]]=[]; S.al[k[0]][+k[1]]=t.value; save(); return; }
 if(t.getAttribute('data-w')){ var id=t.getAttribute('data-w'); S.w[id]=t.value; save(); nav(); savedMsg(id); var b=document.querySelector('#apick [data-a="'+id+'"]'); if(b) b.classList.toggle('dn', !!t.value.trim()); return; }
 if(t.id==='o4'){ S.o4=t.value; save(); nav(); } if(t.id==='sname'){ S.name=t.value; save(); } });
window.addEventListener('afterprint', function(){ [].forEach.call(document.querySelectorAll('.printme'), function(v){ v.classList.remove('printme'); }); });

Object.keys(D.ej).forEach(qNew); ppRender(); initWriting(); renderScale();
go(D.steps.some(function(s){ return s.id===S.cur; }) ? S.cur : 'regla');
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_P, body, js))
print("ok", FILE, "· regla:", REGLA_W, "· textos:", "; ".join("%s %d pal. %s" % (i, n, "/".join(s)) for i, n, s in STATS),
      "· entradas:", lam_words(R["lamina"]), lam_words(B.ML_PRACT["lamina"]), ", ".join(str(lam_words(t["lamina"])) for t in B.TEXTOS if t["lamina"].get("input")),
      ", ".join(str(lam_words(a["lamina"])) for a in B.AHORA if a["lamina"].get("input")), "· fotos:", NFOTOS[0])
