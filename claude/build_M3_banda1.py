# -*- coding: utf-8 -*-
# MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 3: DE LA BANDA 1 A LA BANDA 2
# Uso: python3 build_M3_banda1.py
#  -> DELEA2_curso_M3_banda1_a_banda2.html  (subir a biblioteca/recursos/A2/dele-curso/)
# Contenido (la banda 1, los fallos, la operación rescate, textos para rescatar, ejercicios): banco_banda1_M3.py.
# En «Ahora tú» el estudiante puede traer un texto que escribió en el kit, en las pautas, en la revisión final o
# en los textos modelo (se lee del mismo navegador) o pegar uno nuevo.
# Mismo estilo que las otras piezas del taller: pestañas, progreso en el navegador (storageKey propio), botón
# Copiar con el diagnóstico y los textos rescatados antes y después, y preguntas de opinión al final.
# Sin contador de palabras para el estudiante: las líneas se cuentan a ojo (unas 10 palabras por línea).
# 12/10/2026: las laminas con fotos llevan imagenes de verdad (fotos_M3.py); el build comprueba nombre, prompt y alt.
import json, re
from curso_comun import CSS, EMAIL, page
import fotos_M3 as FT
import banco_banda1_M3 as B

TITLE = "De la banda 1 a la banda 2"
FILE = "DELEA2_curso_M3_banda1_a_banda2.html"
STORAGE = "dele-a2-curso-M3-banda1"
KEYS_OTRAS = {"kit": "dele-a2-curso-M3-kit", "pautas": "dele-a2-curso-M3-pautas", "rev": "dele-a2-curso-M3-revision", "mod": "dele-a2-curso-M3-modelos"}

PAL = re.compile(r"[\wÀ-ſ]+(?:-[\wÀ-ſ]+)*")
TU_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(tú|tu|tus|te|ti|contigo|tienes|puedes|quieres|podrías|recomiendas|perdona|oye|beso|abrazo)(?![\wÀ-ſ])")
US_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(usted|ustedes|su|sus|atentamente|estimad[oa]s?|cordiales?|perdone|disculpe|podría|saludo)(?![\wÀ-ſ])")
def words(s): return len(PAL.findall(s))
def limits(tarea): return (60, 70) if tarea == 1 else (70, 80)
def lineas(n):
    l, r = n // 10, n % 10
    return "unas %d líneas" % (l + (1 if r > 7 else 0)) if r < 3 or r > 7 else "unas %d líneas y media" % l
def norm(s): return " ".join(s.split())

DKEYS = [k for k, _ in B.DIAG]
assert DKEYS == ["pautas", "tipo", "entiende", "con", "gram", "trato", "lin"], DKEYS
PKEYS = [p["k"] for p in B.PASOS]
assert PKEYS == ["pautas", "entiende", "con", "gram", "lin"], "La operación rescate va siempre en este orden"
PASO_DE = {}
for i, p in enumerate(B.PASOS):
    for k in p["trae"]: PASO_DE[k] = i + 1
assert set(PASO_DE) == set(DKEYS), "Cada fallo tiene su paso"
CUMPLE = {"pautas", "tipo", "entiende"}  # fallos que hacen que una pauta no llegue
NFOTOS = [0]

# ------------------------------------------------------------ comprobaciones: la demo
d = B.DEMO; np_ = len(d["lamina"]["pautas"]); mn, mx = limits(d["lamina"]["tarea"])
NFOTOS[0] += FT.check(d["lamina"], "Demo")
assert len(d["etapas"]) == 6 and len(d["notas"]) == 6
for i in range(1, 6): assert norm(d["etapas"][i]) != norm(d["etapas"][i - 1]), "La etapa %d no cambia nada" % i
fin = " ".join(s[1] for par in d["final"] for s in par)
assert norm(fin) == norm(d["etapas"][-1]), "DEMO: «final» no es igual que la última etapa"
assert set(s[0] for par in d["final"] for s in par if s[0]) == set(range(1, np_ + 1)), "DEMO: falta la frase de alguna pauta"
DEMO_N = [words(e) for e in d["etapas"]]
assert mn <= DEMO_N[-1] <= mx, "DEMO: la versión final tiene %d palabras" % DEMO_N[-1]
assert DEMO_N[0] <= mn - 6, "DEMO: el original no es corto (%d)" % DEMO_N[0]
assert not US_PAL.search(d["etapas"][-1]), "DEMO: usted en un correo de tú"

# ------------------------------------------------------------ comprobaciones: los textos para rescatar
def rescued(r):
    """Frases de la versión rescatada: [(pauta, texto, origen)] origen = 's' (frase del original) o 'a' (añadida)."""
    out = [[s["p"], s.get("fix", s["t"]), "s"] for s in r["seg"]]
    for a in r["add"]:
        idx = max([i for i, x in enumerate(out) if x[0] == a["p"]] or [i for i, x in enumerate(out) if 0 < x[0] < a["p"]] or [-1])
        out.insert(idx + 1, [a["p"], a["ops"][0], "a"])
    return out

RST = []
for r in B.RESCATE:
    ref = "Rescate " + r["id"]; l = r["lamina"]; np_ = len(l["pautas"]); mn, mx = limits(l["tarea"])
    NFOTOS[0] += FT.check(l, ref)
    for s in r["seg"]:
        assert 0 <= s["p"] <= np_, ref
        if "fix" in s:
            assert s.get("k") in PASO_DE and s["k"] != "lin", ref + ": clave desconocida en " + s["t"]
            assert norm(s["fix"]) != norm(s["t"]) and s.get("por"), ref + ": corrección igual o sin explicación: " + s["t"]
        else: assert "k" not in s and "por" not in s, ref
    for a in r["add"]:
        assert 1 <= a["p"] <= np_ and len(a["ops"]) == 3 and len(set(a["ops"])) == 3 and a.get("por"), ref + ": frase añadida"
    orig = " ".join(s["t"] for s in r["seg"]); n0 = words(orig)
    res = rescued(r); txt = " ".join(x[1] for x in res); n1 = words(txt)
    assert mn <= n1 <= mx, ref + ": la versión rescatada tiene %d palabras (%d-%d)" % (n1, mn, mx)
    assert set(x[0] for x in res if x[0]) == set(range(1, np_ + 1)), ref + ": en la versión rescatada falta la frase de alguna pauta"
    falla = set(s["p"] for s in r["seg"] if s.get("k") in CUMPLE) | set(a["p"] for a in r["add"])
    assert len(falla) >= 2 or any(s.get("k") == "entiende" for s in r["seg"]), ref + ": en el original no fallan dos pautas ni hay frases que no se entienden"
    if r["trato"] == "tu": assert not US_PAL.search(txt), ref + ": usted en la versión rescatada: " + US_PAL.search(txt).group(0)
    if r["trato"] == "usted": assert not TU_PAL.search(txt), ref + ": tú en la versión rescatada: " + TU_PAL.search(txt).group(0)
    if r["trato"] is None: assert not re.search(r"(?i)(?<![\wÀ-ſ])usted(?![\wÀ-ſ])", txt), ref + ": usted en un texto de la tarea 2"
    if any(s.get("k") == "trato" for s in r["seg"]):
        assert (TU_PAL.search(orig) and US_PAL.search(orig)), ref + ": un fallo de trato, pero el original no mezcla tú y usted"
    truth = set(s["k"] for s in r["seg"] if "k" in s)
    if r["add"]: truth.add("pautas")
    if n0 <= mn - 6: truth.add("lin")
    assert set(r["diag"]) == truth, ref + ": «diag» explica %s, pero los fallos son %s" % (sorted(r["diag"]), sorted(truth))
    r["_n0"], r["_n1"], r["_res"], r["_truth"], r["_falla"] = n0, n1, res, truth, falla
    RST.append("%s %s: %d -> %d pal., pautas que fallan %s, fallos %s" % (r["id"], r["tipo"], n0, n1, sorted(falla), ",".join(k for k in DKEYS if k in truth)))
assert len(B.RESCATE) == 5 and len(set(r["tipo"] for r in B.RESCATE)) == 5, "Cinco textos, uno de cada tipo"
assert any(r["trato"] == "tu" for r in B.RESCATE) and any(r["trato"] == "usted" for r in B.RESCATE)
assert any(r["add"] for r in B.RESCATE) and any(not r["add"] for r in B.RESCATE)

# ejercicios
assert len(B.BANDA) >= 10 and sum(q["ok"] == 0 for q in B.BANDA) >= 4 and sum(q["ok"] == 1 for q in B.BANDA) >= 4
assert len(B.ENTIENDE) >= 8 and all(len(q["ops"]) == 3 and len(set(q["ops"])) == 3 for q in B.ENTIENDE)
assert len(B.COMPLETA) >= 5 and all(q["texto"].count("[[...]]") == 1 and len(q["ops"]) == 3 for q in B.COMPLETA)
assert len(B.FUENTES_KIT) == 5 and len(B.FUENTES_PAUTAS) == 4

# ------------------------------------------------------------ CSS
CSS_B = CSS + r"""
section.view > h3{margin-top:30px}
.row[hidden],[hidden]{display:none!important}
.where{display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.04em;background:var(--ink);color:#fff;border-radius:999px;padding:2px 12px;margin-bottom:8px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px}
.box h4{margin:0 0 2px}.box p{margin:4px 0;font-size:.95rem}
.box .wt{display:inline-block;font-size:.78rem;font-weight:700;background:var(--bad-soft);color:var(--bad);border-radius:999px;padding:1px 10px;margin:2px 0 6px}
.box ul{margin:6px 0 0;padding-left:1.1em;font-size:.95rem}.box li{margin:6px 0}
.box li i{display:block;color:var(--muted);font-size:.9rem}
.big{font-family:Georgia,serif;font-size:1.3rem;line-height:1.35;background:#fff;border:3px solid var(--coral);border-radius:14px;padding:16px 20px;margin:14px 0}
.big small{display:block;font-family:system-ui,sans-serif;font-size:.92rem;color:var(--muted);margin-top:6px}
.b2box{background:var(--ok-soft);border-radius:12px;padding:12px 16px;margin:12px 0}
table.esc td.c1{font-weight:600;width:42%}
table.esc tr.ok td{background:var(--ok-soft)}table.esc tr.mid td{background:var(--amb-soft)}table.esc tr.bad td{background:var(--bad-soft)}
/* fallos */
.fcard{background:#fff;border:1px solid var(--line);border-left:6px solid var(--coral);border-radius:0 12px 12px 0;padding:12px 16px;margin:12px 0}
.fcard .fh{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:6px}
.fcard h3{margin:0;flex:1;font-size:1.08rem}
.fcard .nt{font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 10px;background:#F1EDE8;color:var(--muted)}
.fcard .ps{font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 10px;background:var(--ink);color:#fff}
.mb{width:100%;border-collapse:collapse;margin:6px 0;font-size:.95rem}
.mb td{padding:6px 10px;vertical-align:top;width:50%}
.mb td.x{background:var(--bad-soft)}.mb td.v{background:var(--ok-soft)}
.mb td.x:before{content:"\2717  ";color:var(--bad);font-weight:700}.mb td.v:before{content:"\2713  ";color:var(--ok);font-weight:700}
.truco{background:#F6F3EF;border-radius:8px;padding:8px 12px;font-size:.92rem;margin-top:6px}
/* pasos */
.pasos{list-style:none;padding:0;margin:12px 0;counter-reset:p}
.pasos li{counter-increment:p;background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 14px 10px 56px;margin:8px 0;position:relative}
.pasos li:before{content:counter(p);position:absolute;left:14px;top:10px;width:30px;height:30px;border-radius:50%;background:var(--coral);color:#fff;font-weight:700;display:grid;place-items:center;font-family:Georgia,serif}
.pasos li b{display:block}.pasos li span{font-size:.93rem}.pasos li small{display:block;color:var(--muted);font-size:.86rem;margin-top:4px}
.stepbar{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}
.stepbar button{font:inherit;font-size:.86rem;font-weight:600;border:2px solid var(--line);background:#fff;border-radius:999px;padding:4px 12px;cursor:pointer;color:inherit}
.stepbar button.on{border-color:var(--coral);background:var(--coral);color:#fff}
.stepbar button.dn:not(.on){border-color:var(--ok);color:var(--ok)}
.seg2{display:inline-flex;border:2px solid var(--ink);border-radius:999px;overflow:hidden}
.seg2 button{font:inherit;font-size:.86rem;font-weight:600;border:0;background:#fff;padding:4px 12px;cursor:pointer;color:inherit}
.seg2 button[aria-pressed="true"]{background:var(--ink);color:#fff}
.dtxt{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 16px;white-space:pre-wrap;line-height:1.85;font-size:1rem}
.dtxt.before{border-left:5px solid var(--bad)}.dtxt.after{border-left:5px solid var(--ok)}
.dtxt del{background:var(--bad-soft);color:var(--bad);text-decoration:line-through;text-decoration-thickness:2px;border-radius:3px;padding:0 2px}
.dtxt ins{background:var(--ok-soft);color:var(--ok);text-decoration:none;font-weight:600;border-radius:3px;padding:0 2px}
.dlabel{font-size:.78rem;font-weight:700;letter-spacing:.05em;color:var(--muted);text-transform:uppercase;margin:4px 0}
.dmeta{font-size:.86rem;color:var(--muted);margin:4px 0 0}
.dnotes{background:var(--coral-soft);border-radius:10px;padding:10px 14px 10px 32px;margin:10px 0;font-size:.95rem}
.dnotes li{margin:3px 0}
/* pautas en color */
.p1{--pc:#2B5FA8;--ps:#E4ECF8}.p2{--pc:#C2410C;--ps:#FFE2D6}.p3{--pc:#2F7D4F;--ps:#E3F1E8}.p4{--pc:#9A6A10;--ps:#FBF0DA}.p5{--pc:#6E4FB8;--ps:#ECE6F7}
.sg{background:var(--ps,transparent);border-radius:5px;padding:1px 3px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.sg.fail{background:none;text-decoration:underline wavy var(--bad);text-underline-offset:4px}
.sg.new{outline:2px dashed var(--pc);outline-offset:1px}
.pn{display:inline-grid;place-items:center;min-width:19px;height:19px;border-radius:50%;background:var(--pc);color:#fff;font-size:.7rem;font-weight:700;margin-right:4px;vertical-align:2px;font-family:system-ui,sans-serif}
.miss{display:inline-block;font-size:.78rem;font-weight:700;border:2px dashed var(--bad);color:var(--bad);border-radius:999px;padding:0 8px;margin:0 2px}
/* lamina */
.lam{background:#fff;border:2px solid var(--ink);border-radius:6px;padding:14px 18px;margin:12px 0;font-size:.97rem}
.lam .lh{font-size:.78rem;letter-spacing:.06em;color:var(--muted);text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:6px;margin-bottom:8px;display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
.lam p{margin:4px 0 8px}
.lam ul.pa{margin:0;padding-left:0;list-style:none}
.lam ul.pa li{padding:4px 0 4px 30px;position:relative}
.lam ul.pa li .bn{position:absolute;left:0;top:6px;width:22px;height:22px;border-radius:50%;background:var(--pc,var(--ink));color:#fff;font-size:.78rem;font-weight:700;display:grid;place-items:center}
.lam .pw{font-size:.88rem;color:var(--muted);margin-top:8px;font-style:italic}
.msg{background:#F6F3EF;border-radius:8px;padding:10px 14px;margin:8px 0;font-size:.95rem}
.msg p{margin:0 0 4px}
.ad{border:2px dashed var(--ink);border-radius:8px;padding:10px 14px;margin:8px 0;text-align:center;font-size:.95rem}
.ad p{margin:2px 0}.ad p:first-child{font-weight:800;letter-spacing:.05em;font-family:Georgia,serif}
ul.ficha{background:#F6F3EF;border-radius:8px;padding:8px 14px 8px 30px;margin:8px 0;font-size:.93rem}
/* ejercicios */
.ex{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin:10px 0 18px}
.ex h4{margin:0 0 2px}.ex .ei{font-size:.92rem;color:var(--muted);margin:0 0 10px}
.ex .qn{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.ex .qs{font-size:.95rem;margin:4px 0 2px;color:var(--muted)}
.ex .qp{font-weight:600;margin:4px 0;font-size:1.02rem}
.qop{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:10px;padding:9px 14px;margin:6px 0;cursor:pointer;color:inherit}
.qop:hover:not(:disabled){border-color:var(--coral)}
.qop:disabled{cursor:default}
.qop.ok{border-color:var(--ok);background:var(--ok-soft)}.qop.bad{border-color:var(--bad);background:var(--bad-soft)}
.fb{border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
.fb.ok{background:var(--ok-soft)}.fb.bad{background:var(--bad-soft)}.fb.mid{background:var(--amb-soft)}
.score{font-family:Georgia,serif;font-size:2.2rem;font-weight:700}
.gap{display:inline-block;min-width:80px;border-bottom:2px dashed var(--coral);color:var(--coral);font-weight:700;text-align:center}
.ctxt{background:#FBF9F6;border-radius:10px;padding:10px 14px;line-height:1.8;margin:8px 0}
.own{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.own input{flex:1 1 260px;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:7px 10px}
.pick{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 12px}
.pick button{font:inherit;font-size:.88rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:4px 14px;cursor:pointer;color:inherit}
.pick button.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pick button.dn:not(.on){border-color:var(--ok);color:var(--ok)}
/* rescate */
.phase{display:flex;gap:6px;margin:0 0 12px;flex-wrap:wrap}
.phase span{font-size:.82rem;font-weight:700;border-radius:999px;padding:2px 12px;background:#fff;border:2px solid var(--line);color:var(--muted)}
.phase span.on{border-color:var(--coral);color:var(--ink)}.phase span.dn{border-color:var(--ok);color:var(--ok)}
.stxt{background:#fff;border:1px solid var(--line);border-left:5px solid var(--muted);border-radius:0 10px 10px 0;padding:10px 16px;line-height:1.9}
.dg{list-style:none;padding:0;margin:8px 0}
.dg li{border-bottom:1px dashed var(--line);padding:6px 0}
.dg label{display:flex;gap:10px;align-items:flex-start;cursor:pointer}
.dg input{width:20px;height:20px;accent-color:var(--ink);margin-top:3px;flex:0 0 auto}
.dg .res{display:block;font-size:.88rem;margin:4px 0 0 30px}
.dg li.hit .res{color:var(--ok)}.dg li.miss2 .res{color:#7A4E0E}.dg li.fp .res{color:var(--bad)}
.dg li.hit{background:var(--ok-soft)}.dg li.miss2{background:var(--amb-soft)}.dg li.fp{background:var(--bad-soft)}
.dg .ps{font-size:.72rem;font-weight:700;border-radius:999px;padding:0 8px;background:var(--ink);color:#fff;margin-left:6px;white-space:nowrap}
.segs{background:#FBF9F6;border-radius:10px;padding:10px 12px}
.seg{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:8px;padding:6px 12px;margin:5px 0;cursor:pointer;color:inherit}
.seg:hover:not(:disabled){border-color:var(--coral)}
.seg.mk{border-color:var(--coral);background:var(--coral-soft)}
.seg.ok{border-color:var(--ok);background:var(--ok-soft)}.seg.bad{border-color:var(--bad);background:var(--bad-soft)}.seg.miss{border-color:var(--amb);background:var(--amb-soft)}
.seg:disabled{cursor:default}
.seg .fix{display:block;font-size:.9rem;font-weight:600;color:var(--ok);margin-top:2px}
.seg .fix.w{color:var(--bad)}
.seg .por{display:block;font-size:.84rem;color:var(--muted);font-weight:400}
.seg .tag{display:inline-block;font-size:.72rem;font-weight:700;border-radius:999px;padding:0 8px;margin-right:6px;background:var(--ink);color:#fff}
.addq{background:#FFF8F2;border:2px dashed var(--coral);border-radius:12px;padding:10px 14px;margin:10px 0}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:12px 0}
.card{background:#fff;border:2px solid var(--line);border-radius:14px;padding:12px 16px}
.card.b1{border-top:8px solid var(--bad)}.card.b2{border-top:8px solid var(--ok)}
.card h4{margin:0 0 6px;display:flex;gap:8px;align-items:center}
.bd{font-size:.75rem;font-weight:700;border-radius:999px;padding:1px 10px;color:#fff}.bd.b1{background:var(--bad)}.bd.b2{background:var(--ok)}
.card .txt{line-height:1.95}
.card .meta{font-size:.85rem;color:var(--muted);border-top:1px dashed var(--line);padding-top:6px;margin-top:8px}
.lec{background:var(--coral-soft);border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
.breakout{width:min(1100px,calc(100vw - 32px));position:relative;left:50%;transform:translateX(-50%)}
/* ahora tu */
.ahora{background:#FFF8F2;border:2px solid var(--coral);border-radius:14px;padding:16px 18px;margin:14px 0}
.ahora h4{margin:14px 0 6px}
.ahora textarea{width:100%;font:inherit;font-size:1rem;line-height:1.7;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;min-height:200px;background:#fff;resize:vertical}
.ahora select{font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:6px 10px;background:#fff}
.srcs{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.src{text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:10px;padding:8px 12px;cursor:pointer;color:inherit}
.src:hover:not(:disabled){border-color:var(--coral)}
.src:disabled{opacity:.5;cursor:not-allowed}
.src b{display:block}.src small{color:var(--muted)}
.chk{list-style:none;padding:0;margin:6px 0}
.chk li label{display:flex;gap:8px;align-items:flex-start;padding:5px 0;cursor:pointer}
.chk input{width:19px;height:19px;accent-color:var(--ok);margin-top:4px;flex:0 0 auto}
.pgide{background:#fff;border:2px solid var(--coral);border-radius:12px;padding:10px 14px;margin:10px 0}
.pgide h4{margin:0 0 4px}
.pgide ol{margin:6px 0 0;padding-left:1.3em;font-size:.93rem}
.saved{font-size:.82rem;color:var(--ok);min-height:1.2em}
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
.chips label:has(input:focus-visible){outline:3px solid var(--cta);outline-offset:2px}
.sendbox{border:2px solid var(--coral);border-radius:12px;padding:18px 22px;margin:26px 0;background:#fff}
.sendbox input[type=text]{width:100%;max-width:360px;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 12px;margin-top:6px}
.sum{font-size:.92rem;margin:6px 0;padding-left:1.1em}
@media (max-width:860px){.pair{grid-template-columns:1fr}.breakout{width:auto;left:0;transform:none}}
@media (max-width:760px){.two,.srcs{grid-template-columns:1fr}.mb td{display:block;width:auto}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff}section.view{display:none!important}
 section.view.printme{display:block!important;padding-top:0}.fcard,.box{break-inside:avoid}}
""" + FT.CSS

# ------------------------------------------------------------ HTML de apoyo
def lamina_html(l, color=False):
    h = "Tarea %d" % l["tarea"] + (" · Opción %d" % l["op"] if l.get("op") else "")
    mn, mx = limits(l["tarea"])
    o = ['<div class="lam"><div class="lh"><span>%s</span><span>%d-%d palabras</span></div>' % (h, mn, mx)]
    if l.get("instr"): o.append("<p>%s</p>" % l["instr"])
    if l.get("input"): o.append('<div class="msg">' + "".join("<p>%s</p>" % x for x in l["input"]) + "</div>")
    if l.get("anuncio"): o.append('<div class="ad">' + "".join("<p>%s</p>" % x for x in l["anuncio"]) + "</div>")
    if l.get("intro"): o.append("<p>%s</p>" % l["intro"])
    if l.get("photos"): o.append(FT.fotos_html(l))
    if l.get("ficha"): o.append('<ul class="ficha">' + "".join("<li>%s</li>" % x for x in l["ficha"]) + "</ul>")
    if l.get("intro2"): o.append("<p>%s</p>" % l["intro2"])
    if l.get("lead"): o.append("<p>%s</p>" % l["lead"])
    o.append('<ul class="pa">' + "".join('<li%s><span class="bn">%d</span>%s</li>' % (' class="p%d"' % (i + 1) if color else "", i + 1, p) for i, p in enumerate(l["pautas"])) + "</ul>")
    o.append('<div class="pw">Número de palabras recomendadas: entre %d y %d.</div></div>' % (mn, mx))
    return "".join(o)

def sg(p, t, cls=""):
    if not p: return t
    return '<span class="sg p%d%s"><b class="pn">%d</b>%s</span>' % (p, (" " + cls) if cls else "", p, t)

# ------------------------------------------------------------ 1. LA BANDA 1
qe = "".join('<div class="box"><h4>%s</h4><span class="wt">Banda 1 · %s</span><ul>%s</ul></div>' % (n, q, "".join("<li>%s<i>%s</i></li>" % x for x in L)) for n, q, L in B.QUE_ES)
esc = "".join('<tr class="%s"><td class="c1">%s</td><td>%s</td></tr>' % (c, a, b) for a, b, c in B.ESCALA)
V_BANDA = """
<span class="where">Escritura · Taller de escritura</span>
<h2>De la banda 1 a la banda 2</h2>
<p class="lead">La banda 1 es «todavía no es un A2». Aquí vas a ver qué la provoca, cómo se arregla y, sobre todo, cómo encontrar esos fallos en tus propios textos.</p>
<div class="big">""" + B.IDEA[0] + "<small>" + B.IDEA[1] + """</small></div>
<h3>¿Qué es la banda 1?</h3>
<p>El corrector pone dos notas a cada tarea, de 0 a 3. La banda 1 puede salir en cualquiera de las dos:</p>
<div class="two">""" + qe + """</div>
<h3>¿Y la banda 2?</h3>
<div class="b2box">""" + B.BANDA2 + """</div>
<h3>Las pautas y el cumplimiento, con la escala oficial</h3>
<table class="t esc"><thead><tr><th>Pautas que fallan</th><th>Cumplimiento de la tarea</th></tr></thead><tbody>""" + esc + """</tbody></table>
<div class="note">""" + B.ESCALA_NOTA + """</div>
<div class="tip"><b>Una pauta «falla»</b> si falta, si está a medias (falta una pieza: «y por qué», «con quién»...) o si la frase no se entiende o contesta otra cosa.</div>
<div class="row"><button class="btn cta" data-go="fallos">Siguiente: los fallos que llevan a la banda 1</button></div>
"""

# ------------------------------------------------------------ 2. LOS FALLOS
def fcard(f):
    paso = PASO_DE.get(f["k"], 1)
    return ('<div class="fcard"><div class="fh"><h3>%s</h3><span class="nt">%s</span><span class="ps">Se arregla en el paso %d</span></div>'
            '<table class="mb" aria-label="Ejemplo"><tr><td class="x">%s</td><td class="v">%s</td></tr></table><div class="truco"><b>Arreglo rápido:</b> %s</div></div>'
            % (f["n"], f["nota"], paso, f["mal"], f["bien"], f["truco"]))
V_FALLOS = """
<span class="where">Lo que lleva a la banda 1</span>
<h2>Siete fallos y su arreglo rápido</h2>
<p class="lead">Casi todos los textos de banda 1 tienen dos o tres de estos fallos. Ninguno necesita un español más difícil: solo hay que verlos.</p>
""" + "".join(fcard(f) for f in B.FALLOS) + """
<div class="tip">Fíjate en que casi todos son del <b>cumplimiento</b>: dependen de leer bien la lámina, no de tu nivel. Por eso se arreglan primero.</div>
<div class="row"><button class="btn" data-act="print" data-p="fallos">Imprimir los fallos</button><button class="btn cta" data-go="rescate">Siguiente: la operación rescate</button></div>
"""

# ------------------------------------------------------------ 3. LA OPERACIÓN RESCATE
pasos_li = "".join("<li><b>%s</b><span>%s</span><small>%s</small></li>" % (p["n"], p["que"], p["por"]) for p in B.PASOS)
V_RESCATE = """
<span class="where">Cinco pasos, siempre en el mismo orden</span>
<h2>La operación rescate</h2>
<p class="lead">Para pasar un texto de la banda 1 a la banda 2 no hace falta escribirlo otra vez. Se arregla en cinco pasos, siempre en este orden: primero lo que más cuenta.</p>
<ol class="pasos">""" + pasos_li + """</ol>
<h3>Míralo en un texto de verdad</h3>
<p>Clara se va a vivir a Berlín y escribe a su amiga Mila. Esta es la lámina:</p>
<details><summary>Ver la lámina</summary>""" + lamina_html(B.DEMO["lamina"], True) + """</details>
<div class="ex" id="demo"></div>
<div class="row"><button class="btn cta" data-go="textos">Siguiente: rescata tú</button></div>
"""

# ------------------------------------------------------------ 4. RESCATA TEXTOS
V_TEXTOS = """
<span class="where">Practica · textos de estudiantes</span>
<h2>Rescata estos textos</h2>
<p class="lead">Cinco textos de banda 1, uno de cada tipo. Primero, el diagnóstico: ¿qué falla? Después, el rescate: caza las frases con fallos y completa lo que falta. Al final verás tu versión de banda 2 al lado de la original.</p>
<div class="ex" id="rs"></div>
<div class="row"><button class="btn cta" data-go="ejercicios">Siguiente: ejercicios cortos</button></div>
"""

# ------------------------------------------------------------ 5. EJERCICIOS
V_EJ = """
<span class="where">Practica</span>
<h2>Ejercicios cortos</h2>
<p class="lead">Tres ejercicios para entrenar los ojos: reconocer la banda 1, hacer que una frase se entienda y completar una pauta.</p>
<div class="ex" id="ex-banda"></div>
<div class="ex" id="ex-ent"></div>
<div class="ex" id="ex-comp"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

# ------------------------------------------------------------ 6. AHORA TÚ
V_AHORA = """
<span class="where">Ahora tú</span>
<h2>Ahora tú: rescata un texto tuyo</h2>
<p class="lead">Elige un texto que escribiste en el kit de frases, en las pautas, en la revisión final o en los textos modelo (si lo hiciste en este navegador), o pega uno nuevo. Después, la operación rescate: cinco pasos, en orden, y marca en cada uno lo que has arreglado.</p>
<div class="ahora" id="ahora"></div>
<div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button></div>
"""

# ------------------------------------------------------------ 7. OPINION
STEPS = [("banda", "La banda 1"), ("fallos", "Los fallos"), ("rescate", "Operación rescate"), ("textos", "Rescata textos"),
         ("ejercicios", "Ejercicios"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]
V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo. Al copiar, también se copian tu diagnóstico de los textos y tus textos de «Ahora tú» (antes y después) para que tu profesora los vea.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué fallo de la banda 1 te pasa más a ti?</label>
 <div class="chips" role="group" aria-labelledby="o1l">__CHIPS1__</div>
 <label class="q" id="o2l">2. ¿Te sirve hacer la operación rescate siempre en el mismo orden?</label>
 <div class="chips" role="group" aria-labelledby="o2l">__CHIPS2__</div>
 <label class="q" id="o3l">3. ¿Qué paso te cuesta más?</label>
 <div class="chips" role="group" aria-labelledby="o3l">__CHIPS3__</div>
 <label class="q" for="o4">4. ¿Qué has descubierto en tu texto? ¿Falta algo o hay algo que no has entendido?</label>
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
V_OPINION = (V_OPINION.replace("__CHIPS1__", chips("o1", B.OPINION_FALLOS))
             .replace("__CHIPS2__", chips("o2", ["Sí, mucho", "Un poco", "Prefiero arreglar lo que veo primero"]))
             .replace("__CHIPS3__", chips("o3", ["%d. %s" % (i + 1, p["n"]) for i, p in enumerate(B.PASOS)]))
             .replace("__EMAIL__", EMAIL))

views = {"banda": V_BANDA, "fallos": V_FALLOS, "rescate": V_RESCATE, "textos": V_TEXTOS, "ejercicios": V_EJ, "ahora": V_AHORA, "opinion": V_OPINION}
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
def orig_html(r):
    """El original con la pauta de cada frase; las que fallan, subrayadas; las pautas que faltan, avisadas."""
    o = []
    for s in r["seg"]:
        o.append(sg(s["p"], s["t"], "fail" if s.get("k") else ""))
        for a in r["add"]:
            if a["p"] == s["p"] and s is [x for x in r["seg"] if x["p"] == a["p"]][-1]:
                o.append('<span class="miss">✗ falta: pauta %d</span>' % a["p"])
    return " ".join(o)
def res_html(r):
    return " ".join(sg(p, t, "new" if src == "a" else "") for p, t, src in r["_res"])
TRATO = {"tu": "TÚ", "usted": "USTED", None: ""}
RS_JS = []
for r in B.RESCATE:
    l = r["lamina"]
    RS_JS.append({"id": r["id"], "tipo": r["tipo"], "autor": r["autor"], "tarea": l["tarea"], "trato": TRATO[r["trato"]],
                  "lam": lamina_html(l, True), "pautas": l["pautas"],
                  "seg": [{"p": s["p"], "t": s["t"], "fix": s.get("fix", ""), "k": s.get("k", ""), "por": s.get("por", "")} for s in r["seg"]],
                  "add": [{"p": a["p"], "ops": a["ops"], "por": a["por"]} for a in r["add"]],
                  "truth": [k for k in DKEYS if k in r["_truth"]], "diag": r["diag"],
                  "n0": lineas(r["_n0"]), "n1": lineas(r["_n1"]), "falla": sorted(r["_falla"]),
                  "orig": orig_html(r), "res": res_html(r), "plain0": " ".join(s["t"] for s in r["seg"]),
                  "plain1": " ".join(x[1] for x in r["_res"]), "lec": r["leccion"]})
DEMO_JS = {"etapas": B.DEMO["etapas"], "notas": B.DEMO["notas"], "lineas": [lineas(n) for n in DEMO_N],
           "final": "<br>".join(" ".join(sg(p, t) for p, t in par) for par in B.DEMO["final"]), "autor": B.DEMO["autor"]}
def fuente(s, kind):
    i, n, tarea, trato, pautas = s
    return {"s": kind, "id": i, "n": ("Kit de frases · " if kind == "kit" else "Las pautas · ") + n, "tarea": tarea, "trato": TRATO[trato], "pautas": pautas}
SRC = [fuente(s, "kit") for s in B.FUENTES_KIT] + [fuente(s, "pautas") for s in B.FUENTES_PAUTAS]
DATA = {"key": STORAGE, "otras": KEYS_OTRAS, "steps": [{"id": k, "label": l} for k, l in STEPS],
        "pasos": [{"k": p["k"], "n": p["n"], "que": p["que"], "items": p["items"]} for p in B.PASOS],
        "dlab": dict(B.DIAG), "dkeys": DKEYS, "pasode": PASO_DE, "demo": DEMO_JS, "rs": RS_JS,
        "banda": {"t": "¿Banda 1 o banda 2?", "i": "Textos y fragmentos de estudiantes. Lee el contexto y decide: ¿todavía no aprueba (banda 1) o ya es un A2 (banda 2)?", "ops": B.BANDA_OPS, "items": B.BANDA, "show": 8, "fixed": True},
        "ent": {"t": "¿Se entiende?", "i": "Frases de estudiantes que no se entienden. Elige la versión que se entiende y responde a la pauta.", "items": [dict(q, ok=0) for q in B.ENTIENDE], "show": 8, "fixed": False},
        "comp": B.COMPLETA, "src": SRC, "propio": B.TEXTO_PROPIO_TIPOS}

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function blank(){ return {cur:'banda', seen:{}, ex:{}, dcur:0, dmax:0, dview:'side', rsSel:D.rs[0].id, rs:{}, comp:{}, at:null, hist:[], own:{tipo:'', txt:''}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function shuffle(a){ for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function rec(id, ok, n){ var r=S.ex[id]; if(!r || ok>r.b || (ok===r.b && n!==r.n)) S.ex[id]={b:ok, n:n, l:ok}; else r.l=ok; save(); nav(); }

/* ---------------- diferencias palabra a palabra ---------------- */
function toks(s){ return String(s).split(/(\s+)/).filter(function(x){ return x!==''; }); }
function diff(a, b){
 var A=toks(a), B=toks(b), n=A.length, m=B.length, L=[], i, j;
 for(i=0;i<=n;i++){ L.push(new Array(m+1).fill(0)); }
 for(i=n-1;i>=0;i--) for(j=m-1;j>=0;j--) L[i][j]= A[i]===B[j] ? L[i+1][j+1]+1 : Math.max(L[i+1][j], L[i][j+1]);
 var o=[], dl=[], ad=[];
 function flush(){ if(dl.length){ var t=dl.join(''); o.push(/\S/.test(t)?'<del>'+esc(t)+'</del>':esc(t)); dl=[]; } if(ad.length){ var u=ad.join(''); o.push(/\S/.test(u)?'<ins>'+esc(u)+'</ins>':esc(u)); ad=[]; } }
 i=0; j=0;
 while(i<n && j<m){ if(A[i]===B[j]){ flush(); o.push(esc(A[i])); i++; j++; } else if(L[i+1][j]>=L[i][j+1]){ dl.push(A[i]); i++; } else { ad.push(B[j]); j++; } }
 while(i<n){ dl.push(A[i]); i++; } while(j<m){ ad.push(B[j]); j++; } flush();
 return o.join('');
}
function nwords(s){ var m=String(s).match(/[A-Za-zÀ-ſ]+(?:-[A-Za-zÀ-ſ]+)*/g); return m?m.length:0; }
function lineas(n){ var l=Math.floor(n/10), r=n%10; return (r<3||r>7)?'unas '+(l+(r>7?1:0))+' líneas':'unas '+l+' líneas y media'; }

/* ---------------- navegacion ---------------- */
function tabDone(id){
 if(id==='banda'||id==='fallos') return !!S.seen[id];
 if(id==='rescate') return S.dmax>=5;
 if(id==='textos') return D.rs.every(function(r){ return S.rs[r.id] && S.rs[r.id].done; });
 if(id==='ejercicios') return !!(S.ex.banda && S.ex.ent && S.ex.comp);
 if(id==='ahora') return S.hist.length>0;
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
 if(id==='opinion') summary();
 nav(); window.scrollTo(0,0);
}

/* ---------------- la operacion rescate (demo) ---------------- */
function demoRender(){
 var d=D.demo, k=S.dcur, box=$('demo');
 var bar='<div class="stepbar" role="group" aria-label="Pasos">'+['Original'].concat(D.pasos.map(function(p,i){ return (i+1)+'. '+p.n; })).map(function(t,i){
   return '<button type="button" class="'+(i===k?'on ':'')+(i<k?'dn':'')+'" data-act="dstep" data-i="'+i+'" aria-pressed="'+(i===k?'true':'false')+'">'+esc(t)+'</button>'; }).join('')+'</div>';
 var view='<span class="seg2" role="group" aria-label="Cómo verlo"><button type="button" data-act="dview" data-v="side" aria-pressed="'+(S.dview==='side'?'true':'false')+'">Antes / después</button><button type="button" data-act="dview" data-v="diff" aria-pressed="'+(S.dview==='diff'?'true':'false')+'">Ver los cambios</button></span>';
 var o='<h4>El correo de '+esc(d.autor)+', paso a paso</h4><p class="ei">Pulsa cada paso. «Antes / después» enseña el texto antes y después de ese paso; «Ver los cambios», lo que se ha tachado y lo que se ha añadido.</p>'+bar+'<div class="row" style="margin:6px 0">'+view+'</div>';
 if(k===0){
  o+='<div class="dlabel">El texto original · banda 1</div><div class="dtxt before">'+esc(d.etapas[0])+'</div><p class="dmeta">'+d.lineas[0]+' a mano.</p><h4 style="margin-top:12px">¿Qué falla?</h4><ul class="dnotes">'+d.notas[0].map(function(x){ return '<li>'+esc(x)+'</li>'; }).join('')+'</ul>';
 } else {
  var p=D.pasos[k-1];
  o+='<div class="pgide"><h4>Paso '+k+': '+esc(p.n)+'</h4><span class="small">'+esc(p.que)+'</span></div>';
  if(S.dview==='side') o+='<div class="two"><div><div class="dlabel">Antes del paso '+k+'</div><div class="dtxt before">'+esc(d.etapas[k-1])+'</div><p class="dmeta">'+d.lineas[k-1]+'</p></div><div><div class="dlabel">Después del paso '+k+'</div><div class="dtxt after">'+esc(d.etapas[k])+'</div><p class="dmeta">'+d.lineas[k]+'</p></div></div>';
  else o+='<div class="dlabel">Los cambios del paso '+k+'</div><div class="dtxt">'+diff(d.etapas[k-1], d.etapas[k])+'</div><p class="dmeta">'+d.lineas[k-1]+' → '+d.lineas[k]+'</p>';
  o+='<h4 style="margin-top:12px">Qué se ha hecho</h4><ul class="dnotes">'+d.notas[k].map(function(x){ return '<li>'+esc(x)+'</li>'; }).join('')+'</ul>';
  if(k===5) o+='<div class="fb ok"><b>¡Rescatado!</b> Las cinco pautas, frases que se entienden, conectores y unas 6 líneas: banda 2. No es un texto excelente, y no hace falta.</div>'+
   '<div class="two"><div><div class="dlabel">Original · banda 1</div><div class="dtxt before">'+esc(d.etapas[0])+'</div></div><div><div class="dlabel">Rescatado · banda 2</div><div class="dtxt after" style="white-space:normal">'+d.final+'</div></div></div>'+
   '<p class="small"><a href="#" data-act="dall">Ver todos los cambios del original al rescatado</a></p><div id="dall"></div>';
 }
 o+='<div class="row" style="margin-bottom:0">'+(k>0?'<button class="btn" data-act="dstep" data-i="'+(k-1)+'">← Paso anterior</button>':'')+(k<5?'<button class="btn cta" data-act="dstep" data-i="'+(k+1)+'">'+(k===0?'Empezar el rescate →':'Siguiente paso →')+'</button>':'')+'</div>';
 box.innerHTML=o;
}

/* ---------------- ejercicio q: elegir una opcion ---------------- */
var Q={};
function qNew(id){ var e=D[id], n=e.items.length, idx=shuffle(range(n)).slice(0, Math.min(e.show||n, n));
 Q[id]={k:0, ok:0, ans:false, idx:idx, ord:idx.map(function(i){ var m=(e.items[i].ops||e.ops).length; return e.fixed?range(m):shuffle(range(m)); })}; qRender(id); }
function qRender(id){
 var e=D[id], q=Q[id], box=$('ex-'+id), n=q.idx.length;
 var head='<h4>'+esc(e.t)+'</h4><p class="ei">'+esc(e.i)+'</p>';
 if(q.k>=n){
  rec(id, q.ok, n);
  box.innerHTML=head+'<div class="qn">RESULTADO</div><div class="score">'+q.ok+' / '+n+'</div><p>'+(q.ok===n?'¡Perfecto!':(q.ok>=n-2?'¡Muy bien! Mira otra vez las que has fallado.':'Vuelve a mirar «La banda 1» y «Los fallos», y prueba otra vez.'))+'</p>'+
   '<p class="small muted">Tu mejor resultado: '+S.ex[id].b+' / '+S.ex[id].n+'</p><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="qnew" data-ex="'+id+'">Otra vez</button></div>';
  return;
 }
 var it=e.items[q.idx[q.k]], ops=it.ops||e.ops, o=head+'<div class="qn">'+(q.k+1)+' DE '+n+'</div><p class="qs">'+esc(it.ctx)+'</p>'+(it.p?'<p class="qp">'+esc(it.p)+'</p>':'')+'<div role="group" aria-label="Opciones">';
 q.ord[q.k].forEach(function(i){ o+='<button type="button" class="qop" data-act="qpick" data-ex="'+id+'" data-i="'+i+'">'+esc(ops[i])+'</button>'; });
 o+='</div><div class="qfb"></div><div class="row qnx" style="margin-bottom:0" hidden><button class="btn cta" data-act="qnext" data-ex="'+id+'">'+(q.k===n-1?'Ver el resultado':'Siguiente')+'</button></div>';
 box.innerHTML=o;
}
function qPick(b){
 var id=b.getAttribute('data-ex'), q=Q[id], e=D[id], it=e.items[q.idx[q.k]], ops=it.ops||e.ops, box=$('ex-'+id); if(q.ans) return;
 var i=+b.getAttribute('data-i'), ok=i===it.ok; if(ok) q.ok++; q.ans=true;
 [].forEach.call(box.querySelectorAll('.qop'), function(x){ x.disabled=true; var j=+x.getAttribute('data-i'); if(j===it.ok) x.classList.add('ok'); else if(j===i) x.classList.add('bad'); });
 box.querySelector('.qfb').innerHTML='<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Correcto!':'No es esa: '+esc(ops[it.ok]))+'</b> '+esc(it.por)+'</div>';
 box.querySelector('.qnx').hidden=false; box.querySelector('.qnx button').focus();
}

/* ---------------- completa la pauta ---------------- */
var C={k:0, ok:0, ans:false, ord:[]};
function cNew(){ C={k:0, ok:0, ans:false, ord:D.comp.map(function(){ return shuffle(range(3)); })}; cRender(); }
function cRender(){
 var box=$('ex-comp'), n=D.comp.length, head='<h4>Completa la pauta</h4><p class="ei">A estos textos les falta una pauta o media. Elige la frase que la completa o, si quieres, escribe la tuya y compárala con la nuestra.</p>';
 if(C.k>=n){
  rec('comp', C.ok, n);
  box.innerHTML=head+'<div class="qn">RESULTADO</div><div class="score">'+C.ok+' / '+n+'</div><p>'+(C.ok===n?'¡Perfecto!':'Mira otra vez las pautas de cada texto: qué piezas piden y en qué tiempo.')+'</p><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="cnew">Otra vez</button></div>';
  return;
 }
 var it=D.comp[C.k], own=S.comp[C.k]||'';
 var txt=esc(it.texto).replace('[[...]]','<span class="gap" id="cgap">?</span>');
 var o=head+'<div class="qn">'+(C.k+1)+' DE '+n+' · '+esc(it.tipo).toUpperCase()+'</div><p class="qs"><b>Pautas:</b> '+esc(it.pautas)+'</p><div class="ctxt">'+txt+'</div><p class="qp">'+esc(it.falta)+' ¿Qué frase va en el hueco?</p><div role="group" aria-label="Opciones">';
 C.ord[C.k].forEach(function(i){ o+='<button type="button" class="qop" data-act="cpick" data-i="'+i+'">'+esc(it.ops[i])+'</button>'; });
 o+='</div><div class="own"><input type="text" id="cown" aria-label="Tu frase" placeholder="O escribe tu frase..." value="'+esc(own)+'"><button class="btn sm" data-act="cownok">Usar mi frase</button></div>'+
  '<div class="cfb"></div><div class="row cnx" style="margin-bottom:0" hidden><button class="btn cta" data-act="cnext">'+(C.k===n-1?'Ver el resultado':'Siguiente')+'</button></div>';
 box.innerHTML=o;
}
function cAnswer(i, ownTxt){
 if(C.ans) return; var it=D.comp[C.k], box=$('ex-comp'); C.ans=true;
 var ok=i===0; if(ok) C.ok++;
 [].forEach.call(box.querySelectorAll('.qop'), function(x){ x.disabled=true; var j=+x.getAttribute('data-i'); if(j===0) x.classList.add('ok'); else if(j===i) x.classList.add('bad'); });
 $('cgap').textContent=ownTxt||it.ops[0];
 var msg=ownTxt?'<div class="fb mid"><b>Tu frase:</b> '+esc(ownTxt)+'<br><b>La nuestra:</b> '+esc(it.ops[0])+'<br>¿Responde a la misma pauta, en el mismo tiempo? '+esc(it.por)+'</div>'
  :'<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Correcto!':'No es esa: '+esc(it.ops[0]))+'</b> '+esc(it.por)+'</div>';
 box.querySelector('.cfb').innerHTML=msg;
 box.querySelector('.cnx').hidden=false; box.querySelector('.cnx button').focus();
}

/* ---------------- rescata textos ---------------- */
function rsText(){ var r=D.rs.filter(function(x){ return x.id===S.rsSel; })[0]; if(!r){ r=D.rs[0]; S.rsSel=r.id; } return r; }
function rsState(r){ if(!S.rs[r.id]) S.rs[r.id]={ph:'diag', mk:{}, dres:null, marks:[], cres:null, add:{}, done:false}; return S.rs[r.id]; }
function phaseBar(ph){ var L=[['diag','1. Diagnóstico'],['caza','2. Rescate'],['fin','3. Banda 2']], k=L.map(function(x){ return x[0]; }).indexOf(ph);
 return '<div class="phase">'+L.map(function(x,i){ return '<span class="'+(i===k?'on':i<k?'dn':'')+'">'+(i<k?'✓ ':'')+x[1]+'</span>'; }).join('')+'</div>'; }
function rsRender(){
 var r=rsText(), st=rsState(r), box=$('rs');
 var pick='<div class="pick" role="group" aria-label="Elige un texto">'+D.rs.map(function(x,i){ var s=S.rs[x.id]; return '<button type="button" class="'+(x.id===r.id?'on ':'')+(s&&s.done?'dn':'')+'" data-act="rspick" data-t="'+x.id+'" aria-pressed="'+(x.id===r.id?'true':'false')+'">'+(i+1)+'. '+esc(x.tipo)+(s&&s.done?' ✓':'')+'</button>'; }).join('')+'</div>';
 var o='<h4>Elige un texto</h4>'+pick+phaseBar(st.ph)+'<p class="qn" style="margin:0">'+esc(r.tipo).toUpperCase()+' · '+esc(r.autor)+'</p>'+
  '<details'+(st.ph==='diag'?' open':'')+'><summary>La lámina</summary>'+r.lam+'</details>';
 if(st.ph==='diag'){
  o+='<h4>El texto de '+esc(r.autor)+'</h4><div class="stxt">'+esc(r.plain0)+'</div><p class="dmeta">'+r.n0+' a mano.</p>'+
   '<h4 style="margin-top:14px">Diagnóstico: ¿qué falla?</h4><p class="small">Marca todo lo que ves. Con la lámina al lado.</p><ul class="dg">';
  D.dkeys.forEach(function(k){
   var c='', res='';
   if(st.dres){ var t=r.truth.indexOf(k)>=0, m=!!st.mk[k];
    if(t&&m){ c='hit'; res='✓ Bien visto. '+esc(r.diag[k]); } else if(t){ c='miss2'; res='Se te ha escapado. '+esc(r.diag[k]); } else if(m){ c='fp'; res='Esto no falla en este texto.'; } }
   o+='<li class="'+c+'"><label><input type="checkbox" data-dg="'+k+'"'+(st.mk[k]?' checked':'')+(st.dres?' disabled':'')+'><span>'+esc(D.dlab[k])+(st.dres&&r.truth.indexOf(k)>=0?'<span class="ps">paso '+D.pasode[k]+'</span>':'')+'</span></label>'+(res?'<span class="res">'+res+'</span>':'')+'</li>';
  });
  o+='</ul>';
  if(st.dres){
   var pf=r.falla.length;
   o+='<div class="fb '+(st.dres.ok===st.dres.n&&!st.dres.fp?'ok':'mid')+'"><b>Has visto '+st.dres.ok+' de '+st.dres.n+' fallos'+(st.dres.fp?' y has marcado '+st.dres.fp+' que no está':'')+'.</b> '+
    (pf>=2?'En este texto fallan '+pf+' pautas: por eso el cumplimiento es banda 1.':'Hay frases que no se entienden: por eso es banda 1.')+'</div>'+
    '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="rsgo" data-ph="caza">Ahora, el rescate →</button></div>';
  } else o+='<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="rsdiag">Comprobar mi diagnóstico</button></div>';
 }
 else if(st.ph==='caza'){
  o+='<h4>Paso a paso: caza las frases con fallos</h4><p class="small">Toca las frases que hay que arreglar (de cualquier tipo: pautas, se entiende, conectores, verbos, trato) y pulsa «Comprobar». Verás cómo queda cada una.</p><div class="segs" role="group" aria-label="Frases del texto">';
  r.seg.forEach(function(s,i){
   var cls='', extra='';
   if(st.cres){ var m=st.marks.indexOf(i)>=0;
    if(s.fix){ cls=m?'ok':'miss'; extra='<span class="fix">→ '+esc(s.fix)+'</span><span class="por"><span class="tag">paso '+D.pasode[s.k]+'</span>'+esc(s.por)+'</span>'; }
    else if(m){ cls='bad'; extra='<span class="fix w">Esta frase está bien.</span>'; } }
   else if(st.marks.indexOf(i)>=0) cls='mk';
   o+='<button type="button" class="seg '+cls+'" data-act="rsmark" data-i="'+i+'" aria-pressed="'+(st.marks.indexOf(i)>=0?'true':'false')+'"'+(st.cres?' disabled':'')+'>'+esc(s.t)+extra+'</button>';
  });
  o+='</div>';
  if(!st.cres) o+='<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="rscheck">Comprobar</button></div>';
  else {
   o+='<div class="fb '+(st.cres.ok===st.cres.n&&!st.cres.fp?'ok':'mid')+'"><b>Has encontrado '+st.cres.ok+' de '+st.cres.n+'.</b>'+(st.cres.fp?' Has marcado '+st.cres.fp+' frase'+(st.cres.fp>1?'s':'')+' sin fallo.':'')+' En amarillo, lo que se te ha escapado; en verde, cómo queda.</div>';
   r.add.forEach(function(a,ai){
    var ch=st.add[ai];
    o+='<div class="addq"><h4 style="margin:0 0 4px">Falta algo en la pauta '+a.p+': «'+esc(r.pautas[a.p-1])+'»</h4><p class="small" style="margin:0">¿Qué frase la completa?</p><div role="group" aria-label="Opciones">';
    (st.addOrd&&st.addOrd[ai]?st.addOrd[ai]:[0,1,2]).forEach(function(i){ var c=''; if(ch!=null){ if(i===0) c=' ok'; else if(i===ch) c=' bad'; }
     o+='<button type="button" class="qop'+c+'" data-act="rsadd" data-a="'+ai+'" data-i="'+i+'"'+(ch!=null?' disabled':'')+'>'+esc(a.ops[i])+'</button>'; });
    o+='</div>'+(ch!=null?'<div class="fb '+(ch===0?'ok':'bad')+'"><b>'+(ch===0?'¡Correcto!':'Mejor: '+esc(a.ops[0]))+'</b> '+esc(a.por)+'</div>':'')+'</div>';
   });
   var allAdd=r.add.every(function(a,ai){ return st.add[ai]!=null; });
   o+='<div class="row" style="margin-bottom:0"><button class="btn" data-act="rsredo">Cazar otra vez</button><button class="btn cta" data-act="rsgo" data-ph="fin"'+(allAdd?'':' disabled')+'>Ver mi texto de banda 2 →</button></div>'+(allAdd?'':'<p class="small muted">Primero, completa lo que falta.</p>');
  }
 }
 else {
  o+='<div class="pair"><div class="card b1"><h4><span class="bd b1">Banda 1</span>El original</h4><div class="txt">'+r.orig+'</div><div class="meta">'+r.n0+' · fallan las pautas '+r.falla.join(', ')+(r.falla.length?'':'—')+'</div></div>'+
   '<div class="card b2"><h4><span class="bd b2">Banda 2</span>Rescatado</h4><div class="txt">'+r.res+'</div><div class="meta">'+r.n1+' · las '+r.pautas.length+' pautas con su frase</div></div></div>'+
   '<p class="small muted">En color, la frase de cada pauta. Subrayado en rojo, lo que fallaba; con borde de puntos, la frase que has añadido.</p>'+
   '<details><summary>Ver los cambios palabra a palabra</summary><div class="dtxt">'+diff(r.plain0, r.plain1)+'</div></details>'+
   '<div class="lec"><b>La lección:</b> '+esc(r.lec)+'</div>'+
   '<div class="row" style="margin-bottom:0"><button class="btn" data-act="rsreset">Empezar otra vez este texto</button>'+(D.rs.some(function(x){ return !(S.rs[x.id]&&S.rs[x.id].done); })?'<button class="btn cta" data-act="rsnext">Siguiente texto</button>':'')+'</div>';
 }
 box.innerHTML=o;
}
function rsDiag(){
 var r=rsText(), st=rsState(r), ok=0, fp=0;
 D.dkeys.forEach(function(k){ var t=r.truth.indexOf(k)>=0, m=!!st.mk[k]; if(t&&m) ok++; if(!t&&m) fp++; });
 st.dres={ok:ok, n:r.truth.length, fp:fp}; save(); rsRender();
}
function rsCheck(){
 var r=rsText(), st=rsState(r), ok=0, n=0, fp=0;
 r.seg.forEach(function(s,i){ var m=st.marks.indexOf(i)>=0; if(s.fix){ n++; if(m) ok++; } else if(m) fp++; });
 st.cres={ok:ok, n:n, fp:fp}; st.addOrd=r.add.map(function(){ return shuffle([0,1,2]); }); save(); rsRender();
}

/* ---------------- ahora tu ---------------- */
function other(key){ try{ var r=localStorage.getItem(key); return r?JSON.parse(r):null; }catch(e){ return null; } }
function srcText(s){ var o=other(D.otras[s.s]); return (o && o.w && o.w[s.id] && String(o.w[s.id]).trim()) ? String(o.w[s.id]) : ''; }
function histList(kind){ var o=other(D.otras[kind]); if(!o || !o.hist) return []; return o.hist.map(function(h){ return {n:h.n, t:String(kind==='rev'?(h.rev||''):(h.b||h.a||''))}; }).filter(function(h){ return h.t.trim(); }); }
function short(t){ return esc(String(t).trim().split(/\s+/).slice(0,9).join(' '))+'...'; }
function byName(n){ var nn=String(n||'').replace(/^(Revisado|Nueva) · /,''); return D.src.filter(function(s){ return s.n===nn; })[0]||null; }
function atStart(n, txt, s){
 S.at={n:n, tarea:s?s.tarea:0, trato:s?s.trato:'', pautas:s?s.pautas:[], a:txt, b:txt, step:0, chk:{}, done:false};
 save(); atRender(); $('ahora').scrollIntoView({behavior:'smooth', block:'start'});
}
function atRender(){
 var box=$('ahora'), v=S.at;
 if(!v){
  var any=false, kit=D.src.map(function(s,i){ var w=srcText(s); if(w) any=true;
   return '<button type="button" class="src" data-act="atsrc" data-i="'+i+'"'+(w?'':' disabled')+'><b>'+esc(s.n)+'</b><small>'+(w?short(w):'Sin texto en este navegador')+'</small></button>'; }).join('');
  var hs=[['rev','La revisión final · '],['mod','Textos modelo · ']].map(function(x){ return histList(x[0]).map(function(h,i){
   return '<button type="button" class="src" data-act="athist" data-k="'+x[0]+'" data-i="'+i+'"><b>'+esc(x[1]+h.n)+'</b><small>'+short(h.t)+'</small></button>'; }).join(''); }).join('');
  box.innerHTML='<h4 style="margin-top:0">1. Elige un texto</h4><p class="small">Textos que escribiste en «Ahora tú» del kit de frases y de las pautas'+(any?'':' (en este navegador no hay ninguno todavía)')+':</p><div class="srcs">'+kit+'</div>'+
   (hs?'<h4>Textos que revisaste o mejoraste en otras piezas</h4><div class="srcs">'+hs+'</div>':'')+
   '<h4>... o pega otro texto tuyo</h4><p><label>Tipo de texto: <select id="otipo"><option value="">— elige —</option>'+D.propio.map(function(x){ return '<option'+(S.own.tipo===x?' selected':'')+'>'+esc(x)+'</option>'; }).join('')+'</select></label></p>'+
   '<textarea id="otxt" aria-label="Tu texto" placeholder="Pega o escribe aquí tu texto...">'+esc(S.own.txt||'')+'</textarea>'+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="atown">Rescatar este texto</button></div><div class="saved" id="atmsg" role="status"></div>'+
   (S.hist.length?'<p class="small muted" style="margin-top:14px">Textos rescatados y guardados: '+S.hist.length+'. Se copian en «Tu opinión».</p>':'');
  return;
 }
 var pl=v.pautas.length?'<details><summary>Las pautas de tu tarea</summary><ol class="small">'+v.pautas.map(function(p){ return '<li>'+esc(p)+'</li>'; }).join('')+'</ol></details>':'';
 var bar='<div class="phase">'+D.pasos.map(function(p,i){ return '<span class="'+(i===v.step&&!v.done?'on':(i<v.step||v.done)?'dn':'')+'">'+((i<v.step||v.done)?'✓ ':'')+(i+1)+'. '+esc(p.n)+'</span>'; }).join('')+'</div>';
 var head='<h4 style="margin-top:0">'+esc(v.n)+'</h4>'+bar+pl;
 if(v.done){
  var nmk=Object.keys(v.chk).filter(function(k){ return v.chk[k]; }).length;
  box.innerHTML=head+'<div class="fb ok"><b>¡Rescate terminado!</b> Has marcado '+nmk+' arreglo'+(nmk===1?'':'s')+'. Tu texto antes y después está guardado y se copia con tu opinión.</div>'+
   '<div class="two"><div><div class="dlabel">Antes</div><div class="dtxt before">'+esc(v.a)+'</div><p class="dmeta">'+lineas(nwords(v.a))+'</p></div><div><div class="dlabel">Después</div><div class="dtxt after">'+esc(v.b)+'</div><p class="dmeta">'+lineas(nwords(v.b))+'</p></div></div>'+
   '<details><summary>Ver los cambios palabra a palabra</summary><div class="dtxt">'+diff(v.a, v.b)+'</div></details>'+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="atreset">Rescatar otro texto</button></div>';
  return;
 }
 var p=D.pasos[v.step], extra='';
 if(p.k==='pautas' && v.pautas.length) extra='<p class="small">Comprueba cada pauta de tu lámina: '+v.pautas.map(function(x,i){ return '<b>'+(i+1)+'</b> '+esc(x); }).join(' · ')+'.</p>';
 if(p.k==='gram' && v.trato) extra='<p class="small">Tu texto es de <b>'+v.trato+'</b>: el saludo, las preguntas y la despedida, todo igual.</p>';
 if(p.k==='lin') extra='<p class="small">Ahora tu texto tiene '+lineas(nwords(v.b))+' a mano'+(v.tarea?' (tarea '+v.tarea+': '+(v.tarea===1?'unas 6-7':'unas 7-8')+')':'')+'. Cuenta tú también a ojo: es lo que harás en el examen.</p>';
 box.innerHTML=head+'<div class="pgide"><h4>Paso '+(v.step+1)+': '+esc(p.n)+'</h4><span class="small">'+esc(p.que)+'</span>'+extra+'</div>'+
  '<h4>Tu texto</h4><textarea id="atb" aria-label="Tu texto">'+esc(v.b)+'</textarea><div class="saved" id="atsv" role="status"></div>'+
  '<h4>Lo que he arreglado en este paso</h4><ul class="chk">'+p.items.map(function(x,i){ var id=p.k+i; return '<li><label><input type="checkbox" data-atk="'+id+'"'+(v.chk[id]?' checked':'')+'><span>'+esc(x)+'</span></label></li>'; }).join('')+'</ul>'+
  '<p class="small muted">Si en tu texto no había nada de este paso, no marques nada y sigue.</p>'+
  '<div class="row" style="margin-bottom:0"><button class="btn" data-act="atstep" data-d="-1"'+(v.step===0?' disabled':'')+'>← Paso anterior</button>'+(v.step<4?'<button class="btn cta" data-act="atstep" data-d="1">Hecho: paso '+(v.step+2)+' →</button>':'<button class="btn cta" data-act="atend">Terminar el rescate</button>')+'<button class="btn" data-act="atreset">Elegir otro texto</button></div><div class="saved" id="atmsg" role="status"></div>';
}
function atEnd(){
 var v=S.at; if(String(v.b).trim()===String(v.a).trim()){ $('atmsg').textContent='Tu texto está igual que al principio: ¿no has arreglado nada?'; return; }
 v.done=true;
 var per=D.pasos.map(function(p){ return p.items.filter(function(x,i){ return v.chk[p.k+i]; }); });
 S.hist.push({n:v.n, a:v.a, b:v.b, per:per, d:new Date().toISOString().slice(0,10)});
 if(S.hist.length>6) S.hist=S.hist.slice(-6);
 save(); nav(); atRender();
}

/* ---------------- opinion ---------------- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name="'+k+'"]'); for(var i=0;i<r.length;i++) r[i].checked = r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function exLine(id){ var r=S.ex[id]; return r?r.b+'/'+r.n:'sin hacer'; }
function summary(){
 var dn=D.rs.filter(function(r){ return S.rs[r.id] && S.rs[r.id].done; }).length;
 $('sum').innerHTML='<li>Operación rescate (ejemplo): '+(S.dmax>=5?'vista entera':'paso '+S.dmax+' de 5')+'.</li><li>Textos rescatados: '+dn+' de '+D.rs.length+'.</li><li>Ejercicios: '+['banda','ent','comp'].filter(function(k){ return S.ex[k]; }).length+' de 3.</li><li>Textos tuyos rescatados en «Ahora tú»: '+S.hist.length+'.</li>';
}
function pack(){
 var L=['CURSO DELE A2 - ESCRITURA: DE LA BANDA 1 A LA BANDA 2', 'Nombre: '+(S.name||'-'), '', 'RESCATA TEXTOS:'];
 D.rs.forEach(function(r){ var st=S.rs[r.id];
  if(!st || !st.dres){ L.push('  '+r.tipo+' ('+r.autor+'): sin hacer'); return; }
  var vi=D.dkeys.filter(function(k){ return st.mk[k] && r.truth.indexOf(k)>=0; }).map(function(k){ return D.dlab[k]; }),
      es=r.truth.filter(function(k){ return !st.mk[k]; }).map(function(k){ return D.dlab[k]; }),
      fp=D.dkeys.filter(function(k){ return st.mk[k] && r.truth.indexOf(k)<0; }).map(function(k){ return D.dlab[k]; });
  L.push('  '+r.tipo+' ('+r.autor+'): diagnóstico '+st.dres.ok+'/'+st.dres.n+(st.dres.fp?' (+'+st.dres.fp+' que no fallaba)':'')+(st.cres?' · caza '+st.cres.ok+'/'+st.cres.n+(st.cres.fp?' (+'+st.cres.fp+' bien marcada como fallo)':''):' · caza sin hacer')+
   (r.add.length?' · completar: '+r.add.map(function(a,ai){ var c=st.add[ai]; return c==null?'sin hacer':(c===0?'bien':'mal'); }).join(', '):''));
  if(vi.length) L.push('     Ha visto: '+vi.join(' · ')); if(es.length) L.push('     Se le ha escapado: '+es.join(' · ')); if(fp.length) L.push('     Ha marcado sin fallo: '+fp.join(' · '));
 });
 L.push('', 'EJERCICIOS (mejor resultado):', '  ¿Banda 1 o banda 2?: '+exLine('banda'), '  ¿Se entiende?: '+exLine('ent'), '  Completa la pauta: '+exLine('comp'));
 var own=Object.keys(S.comp).filter(function(k){ return String(S.comp[k]).trim(); });
 if(own.length){ L.push('  Mis frases para completar la pauta:'); own.forEach(function(k){ L.push('   - '+D.comp[+k].tipo+': '+S.comp[k]); }); }
 L.push('', 'MIS TEXTOS RESCATADOS ("Ahora tú"):');
 if(!S.hist.length) L.push('  (todavía no he rescatado ningún texto)');
 S.hist.forEach(function(h,i){
  L.push('', '== '+(i+1)+'. '+h.n+' ('+h.d+') ==');
  D.pasos.forEach(function(p,j){ L.push('Paso '+(j+1)+' · '+p.n+': '+(h.per[j]&&h.per[j].length?h.per[j].join(' / '):'nada que arreglar')); });
  L.push('', 'ANTES:', String(h.a).trim(), '', 'DESPUÉS:', String(h.b).trim());
 });
 L.push('', 'OPINIÓN:', '1. El fallo que más me pasa: '+(S.o1||'-'), '2. ¿Me sirve el orden fijo?: '+(S.o2||'-'), '3. El paso que más me cuesta: '+(S.o3||'-'), '4. Lo que he descubierto / falta algo: '+(S.o4||'-'), '5. Sensación de control en la Escritura (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 dstep:function(b){ S.dcur=+b.getAttribute('data-i'); S.dmax=Math.max(S.dmax, S.dcur); save(); nav(); demoRender(); },
 dview:function(b){ S.dview=b.getAttribute('data-v'); save(); demoRender(); },
 dall:function(b, e){ $('dall').innerHTML='<div class="dtxt">'+diff(D.demo.etapas[0], D.demo.etapas[5])+'</div>'; },
 qnew:function(b){ qNew(b.getAttribute('data-ex')); },
 qpick:function(b){ qPick(b); },
 qnext:function(b){ var id=b.getAttribute('data-ex'); Q[id].k++; Q[id].ans=false; qRender(id); },
 cnew:function(){ cNew(); },
 cpick:function(b){ cAnswer(+b.getAttribute('data-i'), ''); },
 cownok:function(){ var t=($('cown').value||'').trim(); if(!t){ $('cown').focus(); return; } S.comp[C.k]=t; save(); cAnswer(-1, t); },
 cnext:function(){ C.k++; C.ans=false; cRender(); },
 rspick:function(b){ S.rsSel=b.getAttribute('data-t'); save(); rsRender(); },
 rsdiag:function(){ rsDiag(); },
 rsgo:function(b){ var st=rsState(rsText()); st.ph=b.getAttribute('data-ph'); if(st.ph==='fin') st.done=true; save(); nav(); rsRender(); $('rs').scrollIntoView({behavior:'smooth', block:'start'}); },
 rsmark:function(b){ var st=rsState(rsText()); if(st.cres) return; var i=+b.getAttribute('data-i'), k=st.marks.indexOf(i); if(k>=0) st.marks.splice(k,1); else st.marks.push(i); save(); rsRender(); },
 rscheck:function(){ rsCheck(); },
 rsredo:function(){ var st=rsState(rsText()); st.cres=null; st.marks=[]; st.add={}; save(); rsRender(); },
 rsadd:function(b){ var st=rsState(rsText()), a=+b.getAttribute('data-a'); if(st.add[a]!=null) return; st.add[a]=+b.getAttribute('data-i'); save(); rsRender(); },
 rsreset:function(){ delete S.rs[S.rsSel]; save(); nav(); rsRender(); },
 rsnext:function(){ var n=D.rs.filter(function(x){ return !(S.rs[x.id]&&S.rs[x.id].done); })[0]; if(n){ S.rsSel=n.id; save(); rsRender(); $('rs').scrollIntoView({behavior:'smooth'}); } },
 atsrc:function(b){ var s=D.src[+b.getAttribute('data-i')], w=srcText(s); if(w) atStart(s.n, w, s); },
 athist:function(b){ var k=b.getAttribute('data-k'), h=histList(k)[+b.getAttribute('data-i')]; if(h) atStart((k==='rev'?'La revisión final · ':'Textos modelo · ')+h.n, h.t, byName(h.n)); },
 atown:function(){ var t=($('otxt').value||'').trim(), tp=$('otipo').value; if(!t){ $('atmsg').textContent='Primero pega o escribe tu texto.'; return; }
  var tarea=(tp.indexOf('Correo')===0)?1:(tp?2:0), trato=tp==='Correo a un amigo'?'TÚ':tp==='Correo de usted'?'USTED':'';
  atStart('Mi texto'+(tp?' · '+tp:''), t, {tarea:tarea, trato:trato, pautas:[]}); },
 atstep:function(b){ S.at.step=Math.max(0, Math.min(4, S.at.step+(+b.getAttribute('data-d')))); save(); atRender(); $('ahora').scrollIntoView({behavior:'smooth', block:'start'}); },
 atend:function(){ atEnd(); },
 atreset:function(){ S.at=null; save(); atRender(); },
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
 var a=e.target.closest('[data-act]'); if(a && !a.disabled && ACTS[a.getAttribute('data-act')]){ if(a.tagName==='A') e.preventDefault(); ACTS[a.getAttribute('data-act')](a, e); }
});
var svT;
function savedMsg(id){ var el=$(id); if(!el) return; el.textContent='✓ Guardado en este navegador'; clearTimeout(svT); svT=setTimeout(function(){ el.textContent=''; },1800); }
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.getAttribute('data-dg')!==null){ var st=rsState(rsText()); st.mk[t.getAttribute('data-dg')]=t.checked; save(); return; }
 if(t.getAttribute('data-atk')!==null){ S.at.chk[t.getAttribute('data-atk')]=t.checked; save(); return; }
 if(t.id==='otipo'){ S.own.tipo=t.value; save(); return; }
 if(t.name==='o1'||t.name==='o2'||t.name==='o3'||t.name==='o5'){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){ var t=e.target;
 if(t.id==='atb'){ S.at.b=t.value; save(); savedMsg('atsv'); return; }
 if(t.id==='otxt'){ S.own.txt=t.value; save(); return; }
 if(t.id==='o4'){ S.o4=t.value; save(); nav(); } if(t.id==='sname'){ S.name=t.value; save(); } });
window.addEventListener('afterprint', function(){ [].forEach.call(document.querySelectorAll('.printme'), function(v){ v.classList.remove('printme'); }); });

demoRender(); qNew('banda'); qNew('ent'); cNew(); rsRender(); atRender(); renderScale();
go(D.steps.some(function(s){ return s.id===S.cur; }) ? S.cur : 'banda');
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_B, body, js))
print("ok", FILE, "· fotos comprobadas:", NFOTOS[0])
print("  demo: palabras por etapa", DEMO_N)
for x in RST: print("  " + x)
print("  ejercicios: banda %d, se entiende %d, completa %d · fuentes de Ahora tú: %d" % (len(B.BANDA), len(B.ENTIENDE), len(B.COMPLETA), len(SRC)))
