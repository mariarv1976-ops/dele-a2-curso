# -*- coding: utf-8 -*-
# MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 4: LA REVISION FINAL DE 5 MINUTOS
# Uso: python3 build_M3_revision.py
#  -> DELEA2_curso_M3_revision_final.html  (subir a biblioteca/recursos/A2/dele-curso/)
# Contenido (lista de pasadas, cómo corregir, textos de estudiantes y ejercicios): banco_revision_M3.py.
# Usa también las láminas de «Ahora tú» del kit (banco_frases_M3.py) y de las pautas (banco_pautas_M3.py): en
# «Ahora tú» el estudiante puede revisar el texto que escribió allí (se lee del mismo navegador).
# Mismo estilo que el kit y las pautas: pestañas, progreso en el navegador (storageKey propio), botón Copiar
# con los textos revisados y preguntas de opinión al final. Sin contador de palabras: las líneas se cuentan a ojo.
# 12/10/2026: las laminas con fotos llevan imagenes de verdad (fotos_M3.py); el build comprueba nombre, prompt y alt.
import json, re
from curso_comun import CSS, EMAIL, page
import fotos_M3 as FT
import banco_revision_M3 as B
import banco_frases_M3 as BF
import banco_pautas_M3 as BP

TITLE = "La revisión final de 5 minutos"
FILE = "DELEA2_curso_M3_revision_final.html"
STORAGE = "dele-a2-curso-M3-revision"
KIT_KEY = "dele-a2-curso-M3-kit"
PAUTAS_KEY = "dele-a2-curso-M3-pautas"

PAL = re.compile(r"[\wÀ-ſ]+(?:-[\wÀ-ſ]+)*")
TU_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(tú|tu|tus|te|ti|contigo|tienes|puedes|quieres|mandas|perdona|oye|beso|abrazo)(?![\wÀ-ſ])")
US_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(usted|ustedes|su|sus|atentamente|estimad[oa]s?|cordiales|perdone|disculpe|saludo)(?![\wÀ-ſ])")
YP = re.compile(r"(?i)(?<![\wÀ-ſ])(y|porque)(?![\wÀ-ſ])")
def words(s): return len(PAL.findall(s))

# ------------------------------------------------------------ comprobaciones del banco
KEYS = [p["k"] for p in B.PASADAS]
assert KEYS == ["pautas", "trato", "pas", "hay", "conc", "muy", "con", "lin"], KEYS
NAME = {p["k"]: p["n"] for p in B.PASADAS}
SUMA = sum(p["s"] for p in B.PASADAS)
MARGEN = 300 - SUMA
assert 0 < MARGEN <= 60, "La lista dura %d s: tiene que caber en 5 minutos con un margen" % SUMA
assert len(B.TARJETA) == len(B.PASADAS)
assert sum(m for m, _, _ in B.REPARTO) == 45
assert set(B.EJ) == set(KEYS), "Un ejercicio por pasada"

for k, e in B.EJ.items():
    if e["tipo"] == "q":
        for q in e["items"]: assert len(q["ops"]) == 3 and 0 <= q["ok"] < 3, k
    else:
        errs = [s for s in e["seg"] if s.get("fix")]
        assert len(errs) >= 3, k + ": pocos errores para cazar"
        for s in errs: assert s["fix"] != s["t"] and s.get("por"), k + ": " + s["t"]
if True:  # tú/usted: los errores lo son y las correcciones y las frases buenas, no
    for s in B.EJ["trato"]["seg"]:
        if s.get("fix"):
            assert TU_PAL.search(s["t"]), "trato: no veo el tú en: " + s["t"]
            assert not TU_PAL.search(s["fix"]), "trato: la corrección sigue con tú: " + s["fix"]
        else: assert not TU_PAL.search(s["t"]), "trato: frase buena con tú: " + s["t"]
    for s in B.EJ["con"]["seg"]:
        if s.get("fix"): assert len(YP.findall(s["fix"])) < len(YP.findall(s["t"])), "con: la corrección no quita «y/porque»: " + s["t"]

def lam_words(l): return sum(words(x) for x in l.get("input", []))
RSTAT = []
VISTOS = set()
NFOTOS = [0]
for t in B.RELOJ:
    l, ref = t["lamina"], "Contrarreloj " + t["id"]
    NFOTOS[0] += FT.check(l, ref)
    np_ = len(l["pautas"]); falta = set(t.get("falta", []))
    if l.get("input"): assert 30 <= lam_words(l) <= 50, ref + ": entrada de %d palabras" % lam_words(l)
    segs = [s for par in t["par"] for s in par]
    cub = set(s["p"] for s in segs if s["p"])
    assert cub == set(range(1, np_ + 1)) - falta, ref + ": pautas con frase %s, faltan %s" % (sorted(cub), sorted(falta))
    for s in segs:
        if s.get("fix"):
            assert s["k"] in KEYS and s["k"] not in ("pautas", "lin") and s["fix"] != s["t"] and s.get("por"), ref + ": " + s["t"]
            VISTOS.add(s["k"])
    fixed = " ".join(s.get("fix", s["t"]) for s in segs)
    n = words(fixed)
    mn, mx = (60, 70) if l["tarea"] == 1 else (70, 80)
    if t["largo"] == "bien": assert mn <= n <= mx, ref + ": %d palabras (%d-%d)" % (n, mn, mx)
    else: assert t["largo"] == "corto" and n <= mn - 5, ref + ": %d palabras: no es corto" % n
    if t["trato"] == "tu":
        assert not US_PAL.search(fixed), ref + ": usted en el correo corregido: " + US_PAL.search(fixed).group(0)
    if t["trato"] == "usted":
        assert not TU_PAL.search(fixed), ref + ": tú en el correo corregido: " + TU_PAL.search(fixed).group(0)
    RSTAT.append((t["id"], n, len([s for s in segs if s.get("fix")]), sorted(falta)))
assert VISTOS >= {"trato", "pas", "hay", "conc", "muy", "con"}, "Faltan pasadas en el contrarreloj: %s" % ({"trato", "pas", "hay", "conc", "muy", "con"} - VISTOS)
assert any(t.get("falta") for t in B.RELOJ) and any(not t.get("falta") for t in B.RELOJ)
for t in BF.TIPOS: NFOTOS[0] += FT.check(t["ahora"], "Kit (ahora tú) " + t["id"])
for a in BP.AHORA: NFOTOS[0] += FT.check(a["lamina"], "Pautas (ahora tú) " + a["id"])

# ------------------------------------------------------------ CSS
CSS_R = CSS + r"""
section.view > h3{margin-top:30px}
.row[hidden],[hidden]{display:none!important}
.where{display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.04em;background:var(--ink);color:#fff;border-radius:999px;padding:2px 12px;margin-bottom:8px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:12px 0}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px}
.box h4{margin:0 0 4px}.box p{margin:4px 0;font-size:.95rem}
.keys{counter-reset:k;list-style:none;padding:0}
.keys li{counter-increment:k;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 14px 10px 52px;margin:8px 0;position:relative}
.keys li:before{content:counter(k);position:absolute;left:14px;top:8px;font-family:Georgia,serif;font-size:1.5rem;font-weight:700;color:var(--coral)}
.big{font-family:Georgia,serif;font-size:1.35rem;line-height:1.35;background:#fff;border:3px solid var(--coral);border-radius:14px;padding:16px 20px;margin:14px 0}
.big small{display:block;font-family:system-ui,sans-serif;font-size:.9rem;color:var(--muted);margin-top:6px}
/* colores de las pasadas */
.k0{--kc:#2B5FA8;--ks:#E4ECF8}.k1{--kc:#6E4FB8;--ks:#ECE6F7}.k2{--kc:#E8603C;--ks:#FFE2D6}.k3{--kc:#2A8C86;--ks:#DDF1F0}
.k4{--kc:#B8407A;--ks:#F8E1EC}.k5{--kc:#B7791F;--ks:#FBF0DA}.k6{--kc:#2F7D4F;--ks:#E3F1E8}.k7{--kc:#7C8424;--ks:#EEF0D9}
.kn{display:inline-grid;place-items:center;min-width:26px;height:26px;border-radius:50%;background:var(--kc);color:#fff;font-weight:700;font-size:.85rem;flex:0 0 auto}
/* reparto 45 */
.r45{display:flex;border-radius:10px;overflow:hidden;margin:14px 0 4px;border:2px solid var(--ink)}
.r45 div{padding:8px 6px;text-align:center;font-size:.82rem;line-height:1.25;border-right:2px solid var(--ink);background:#fff}
.r45 div:last-child{border-right:0}
.r45 div b{display:block;font-family:Georgia,serif;font-size:1.05rem}
.r45 div.me{background:var(--coral);color:#fff}
.r45cap{display:flex;justify-content:space-between;font-size:.8rem;color:var(--muted)}
/* la lista en un vistazo */
.tbar{display:flex;border-radius:8px;overflow:hidden;height:30px;margin:10px 0 4px;border:1.5px solid var(--ink)}
.tbar div{background:var(--kc,#D9D2C8);color:#fff;font-size:.72rem;font-weight:700;display:grid;place-items:center;border-right:1.5px solid #fff;overflow:hidden;white-space:nowrap}
.tbar div.mg{background:repeating-linear-gradient(45deg,#EEE7DD,#EEE7DD 6px,#E2D9CC 6px,#E2D9CC 12px);color:var(--muted)}
.olist{list-style:none;padding:0;margin:8px 0}
.olist li{display:flex;gap:10px;align-items:center;padding:7px 0;border-bottom:1px dashed var(--line)}
.olist li .nm{font-weight:600;flex:1}
.olist li .sec{font-size:.85rem;color:var(--muted);white-space:nowrap}
/* tarjetas de pasada */
.pcard{background:#fff;border:1px solid var(--line);border-top:6px solid var(--kc);border-radius:12px;padding:12px 16px 14px;margin:14px 0}
.pcard .ph{display:flex;gap:10px;align-items:center;margin-bottom:6px}
.pcard .ph h3{margin:0;flex:1}
.pcard .sec{font-size:.85rem;font-weight:700;color:var(--kc);white-space:nowrap}
.pcard p{margin:6px 0}
.pcard .lbl{font-size:.78rem;font-weight:700;letter-spacing:.05em;color:var(--kc);text-transform:uppercase;display:block}
.mb{width:100%;border-collapse:collapse;margin:8px 0;font-size:.95rem}
.mb td{padding:6px 8px;border-top:1px solid var(--line);vertical-align:top}
.mb td.x{background:var(--bad-soft);width:50%}.mb td.v{background:var(--ok-soft)}
.mb td.x:before{content:"\2717  ";color:var(--bad);font-weight:700}.mb td.v:before{content:"\2713  ";color:var(--ok);font-weight:700}
.truco{background:var(--ks);border-radius:8px;padding:8px 12px;font-size:.93rem;margin-top:8px}
/* tarjeta imprimible y papel a mano */
.paper{background:#FFFDF6;border:1px solid #D9CFA8;border-radius:4px;padding:12px 18px;font-family:"Bradley Hand","Segoe Print","Comic Sans MS",cursive;font-size:1.08rem;line-height:30px;box-shadow:2px 3px 0 #EDE6CC;background-image:repeating-linear-gradient(transparent,transparent 29px,#D7E2F0 30px)}
.paper .hd{font-weight:700;color:var(--coral);border-bottom:1.5px solid var(--coral);margin-bottom:2px}
.paper .ln{display:flex;gap:8px}
.paper .ln b{min-width:1.3em}
.paper .bx{display:inline-block;width:14px;height:14px;border:1.5px solid #555;border-radius:2px;margin-left:6px;vertical-align:-1px}
.hand{line-height:46px;padding-top:6px;background-image:repeating-linear-gradient(transparent,transparent 45px,#D7E2F0 46px)}
.hand ruby{ruby-position:over}
.hand rt{font-size:.78rem;color:#1E4A87;font-weight:700}
.hand s{text-decoration-thickness:2px;text-decoration-color:#1E4A87}
.hand .car{color:#1E4A87;font-weight:700}
.hand .ast{color:#1E4A87;font-weight:700}
.dnotes{font-size:.92rem;margin:8px 0;padding-left:1.2em}
/* ejercicios */
.ex{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin:10px 0 14px}
.ex h4{margin:0 0 2px}.ex .ei{font-size:.92rem;color:var(--muted);margin:0 0 10px}
.ex .qn{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.ex .qs{font-size:.95rem;margin:4px 0 2px}
.ex .qp{font-weight:600;margin:4px 0}
.qop{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:10px;padding:9px 14px;margin:6px 0;cursor:pointer;color:inherit}
.qop:hover:not(:disabled){border-color:var(--coral)}
.qop:disabled{cursor:default}
.qop.ok,.seg.ok{border-color:var(--ok);background:var(--ok-soft)}
.qop.bad,.seg.bad{border-color:var(--bad);background:var(--bad-soft)}
.fb{border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
.fb.ok{background:var(--ok-soft)}.fb.bad{background:var(--bad-soft)}
.score{font-family:Georgia,serif;font-size:2.2rem;font-weight:700}
.segs{background:#FBF9F6;border-radius:10px;padding:10px 12px}
.segs .pp{margin:0 0 10px}
.seg{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:8px;padding:6px 12px;margin:5px 0;cursor:pointer;color:inherit}
.seg:hover:not(:disabled){border-color:var(--coral)}
.seg.mk{border-color:var(--coral);background:var(--coral-soft)}
.seg.miss{border-color:var(--amb);background:var(--amb-soft)}
.seg:disabled{cursor:default}
.seg .fix{display:block;font-size:.88rem;font-weight:600;color:var(--ok);margin-top:2px}
.seg .fix.w{color:var(--bad)}
.seg .por{display:block;font-size:.84rem;color:var(--muted);font-weight:400}
.seg .tag{display:inline-block;font-size:.72rem;font-weight:700;border-radius:999px;padding:0 8px;margin-right:6px;background:var(--ks);color:var(--kc)}
.pick{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 12px}
.pick button{font:inherit;font-size:.86rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:4px 12px;cursor:pointer;display:inline-flex;gap:6px;align-items:center;color:inherit}
.pick button.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pick button.dn:not(.on){border-color:var(--ok);color:var(--ok)}
.pick button .kn{min-width:20px;height:20px;font-size:.72rem}
.pex{display:none}.pex.on{display:block}
.pstrip{display:flex;gap:10px;align-items:flex-start;background:var(--ks);border-radius:10px;padding:10px 14px;font-size:.93rem}
.pstrip b{display:block}
.tline{font-size:.85rem;font-weight:600;color:var(--muted);margin:10px 0 0;letter-spacing:.02em}
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
/* contrarreloj */
.clock{position:sticky;top:8px;z-index:5;display:flex;gap:12px;align-items:center;justify-content:space-between;background:var(--ink);color:#fff;border-radius:12px;padding:8px 16px;margin:10px 0}
.clock .tm{font-family:Georgia,serif;font-size:1.8rem;font-weight:700;font-variant-numeric:tabular-nums}
.clock.warn{background:var(--amb)}.clock.over{background:var(--bad)}
.clock .msg2{font-size:.9rem}
.prow{border-top:1px dashed var(--line);padding:8px 0;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.prow .pt{flex:1 1 260px;font-size:.95rem}
.tri{display:flex;gap:6px;flex-wrap:wrap}
.tri button{font:inherit;font-size:.86rem;font-weight:600;border:2px solid var(--line);background:#fff;border-radius:999px;padding:3px 12px;cursor:pointer;color:inherit}
.tri button[aria-pressed="true"]{border-color:var(--ink);background:var(--ink);color:#fff}
.tri button.right{border-color:var(--ok);background:var(--ok-soft);color:var(--ok)}
.tri button.wrong{border-color:var(--bad);background:var(--bad-soft);color:var(--bad)}
.tri button:disabled{cursor:default}
table.res td:first-child{white-space:nowrap}
.lec{background:var(--coral-soft);border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
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
.orig{background:#fff;border:1px solid var(--line);border-left:5px solid var(--muted);border-radius:0 10px 10px 0;padding:10px 14px;white-space:pre-wrap;font-size:.98rem;line-height:1.7}
.run{background:#fff;border:2px solid var(--kc,var(--ink));border-radius:14px;padding:14px 16px;margin:12px 0}
.run .ph{display:flex;gap:10px;align-items:center}
.run .ph h4{margin:0;flex:1}
.run .pbar{height:8px;border-radius:999px;background:#EEE7DD;overflow:hidden;margin:8px 0}
.run .pbar i{display:block;height:100%;background:var(--kc);width:0}
.cnt{display:inline-flex;align-items:center;gap:8px;margin:6px 0}
.cnt button{font:inherit;font-weight:700;width:34px;height:34px;border-radius:50%;border:2px solid var(--ink);background:#fff;cursor:pointer}
.cnt output{font-family:Georgia,serif;font-size:1.4rem;font-weight:700;min-width:1.5em;text-align:center}
.chkp{list-style:none;padding:0;margin:6px 0}
.chkp li label{display:flex;gap:8px;align-items:flex-start;padding:4px 0;cursor:pointer}
.chkp input{width:19px;height:19px;accent-color:var(--ok);margin-top:3px}
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
@media (max-width:760px){.two,.three,.srcs{grid-template-columns:1fr}.r45 div{font-size:.7rem;padding:6px 2px}.tbar div{font-size:0}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff}section.view{display:none!important}
 section.view.printme{display:block!important;padding-top:0}.pcard,.paper,.box{break-inside:avoid}}
""" + FT.CSS

# ------------------------------------------------------------ HTML de apoyo
def pauta_t(p): return p["t"] if isinstance(p, dict) else p

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
    o.append('<ul class="pa">' + "".join('<li><span class="bn">%d</span>%s</li>' % (i + 1, pauta_t(p)) for i, p in enumerate(l["pautas"])) + "</ul>")
    o.append('<div class="pw">Número de palabras recomendadas: entre %d y %d.</div></div>' % (mn, mx))
    return "".join(o)

def kc(k): return "k%d" % KEYS.index(k)
def mmss(s): return "%d:%02d" % (s // 60, s % 60) if s >= 60 else "%d s" % s

# ------------------------------------------------------------ 1. LOS 5 MINUTOS
r45 = "".join('<div class="%s" style="flex:%d"><b>%d min</b>%s</div>' % ("me" if t == "Revisar" else "", m, m, t) for m, t, _ in B.REPARTO)
r45l = "".join("<li><b>%s (%d min):</b> %s</li>" % (t, m, d) for m, t, d in B.REPARTO)
tbar = "".join('<div class="%s" style="flex:%d" title="%s: %s">%d</div>' % (kc(p["k"]), p["s"], p["n"], mmss(p["s"]), i + 1) for i, p in enumerate(B.PASADAS)) + '<div class="mg" style="flex:%d" title="Margen">+%d s</div>' % (MARGEN, MARGEN)
olist = "".join('<li class="%s"><span class="kn">%d</span><span class="nm">%s</span><span class="sec">%s</span></li>' % (kc(p["k"]), i + 1, p["n"], mmss(p["s"])) for i, p in enumerate(B.PASADAS))
porque = "".join('<div class="box"><h4>%s</h4><p>%s</p></div>' % x for x in B.POR_QUE)
V_IDEA = """
<span class="where">Escritura · Taller de escritura</span>
<h2>La revisión final: 5 minutos que suben la nota</h2>
<p class="lead">Muchos candidatos pierden puntos por fallos que podían ver en un minuto: una despedida que falta, un «¿puedes...?» en un correo de usted, un «mis amigo». Este taller te enseña a encontrarlos.</p>
<div class="big">Guarda siempre 5 minutos al final.<br>Revisa con una lista fija, en un orden fijo: una pasada para cada cosa.<small>En cada pasada miras solo una cosa (solo los verbos, solo el saludo y la despedida...) y buscas los fallos que más bajan la nota.</small></div>
<h3>Los 45 minutos de la Escritura</h3>
<div class="r45" aria-hidden="true">""" + r45 + """</div>
<div class="r45cap"><span>0:00</span><span>45:00</span></div>
<ul>""" + r45l + """</ul>
<div class="tip">Es una recomendación, no una regla del examen. Pero los últimos 5 minutos son para revisar <b>siempre</b>: si a los 40 minutos todavía escribes, termina la frase y empieza a revisar.</div>
<h3>¿Por qué una lista y no «leer otra vez»?</h3>
<div class="three">""" + porque + """</div>
<h3>La lista en un vistazo</h3>
<p>Ocho pasadas, siempre en este orden. Al lado de cada pasada, el tiempo que necesitas más o menos para un texto; en el examen tienes dos textos, así que vas más rápido: <b>2 minutos para la tarea 1 y 3 para la tarea 2</b>.</p>
<div class="tbar" aria-hidden="true">""" + tbar + """</div>
<ol class="olist">""" + olist + """</ol>
<p class="small muted">En total, """ + mmss(SUMA) + """ y un margen de """ + str(MARGEN) + """ segundos para corregir con calma.</p>
<div class="tip"><b>Si se acaba el tiempo:</b> las primeras pasadas son las que más cuentan. Por eso van primero: si solo te da tiempo de hacer tres, has hecho las importantes.</div>
<div class="row"><button class="btn cta" data-go="lista">Siguiente: la lista, paso a paso</button></div>
"""

# ------------------------------------------------------------ 2. LA LISTA
def pcard(i, p):
    ej = "".join('<tr><td class="x">%s</td><td class="v">%s</td></tr>' % x for x in p["ej"])
    return ('<div class="pcard %s"><div class="ph"><span class="kn">%d</span><h3>%s</h3><span class="sec">unos %s</span></div>'
            '<p><span class="lbl">Mira solo</span>%s</p><p><span class="lbl">Buscas</span>%s</p>'
            '<table class="mb" aria-label="Ejemplos">%s</table><div class="truco"><b>Truco:</b> %s</div></div>'
            % (kc(p["k"]), i + 1, p["n"], mmss(p["s"]), p["mira"], p["busca"], ej, p["truco"]))
tarjeta = ('<div class="paper"><div class="hd">MI LISTA DE REVISIÓN · 5 minutos (T1: 2 · T2: 3)</div>'
           + "".join('<div class="ln"><b>%d.</b><span>%s <span class="bx"></span><span class="bx"></span></span></div>' % (i + 1, x) for i, x in enumerate(B.TARJETA)) + "</div>")
V_LISTA = """
<span class="where">Las 8 pasadas</span>
<h2>La lista de revisión, paso a paso</h2>
<p class="lead">Para cada pasada: qué miras (solo eso), qué buscas y un ejemplo de lo que vas a encontrar. Lo que está en rojo es un error típico; en verde, cómo queda corregido.</p>
""" + "".join(pcard(i, p) for i, p in enumerate(B.PASADAS)) + """
<h3>Tu tarjeta de revisión</h3>
<p>Imprímela y tenla al lado cuando escribas en casa. Las dos casillas son para la tarea 1 y la tarea 2. Después de unos cuantos textos, la sabrás de memoria: en el examen la llevas en la cabeza.</p>
""" + tarjeta + """
<div class="row"><button class="btn" data-act="print" data-p="lista">Imprimir la lista y la tarjeta</button><button class="btn cta" data-go="corregir">Siguiente: cómo corregir</button></div>
"""

# ------------------------------------------------------------ 3. COMO CORREGIR
reglas = "".join("<li><b>%s.</b> %s</li>" % x for x in B.REGLAS)
demo = '<div class="paper hand">' + "".join('<div>%s</div>' % x for x in B.DEMO) + "</div>"
sit = "".join("<tr><td><b>%s</b></td><td>%s</td></tr>" % x for x in B.SITUACIONES)
V_CORREGIR = """
<span class="where">Si encuentras un fallo</span>
<h2>Cómo corregir en el examen</h2>
<p class="lead">En el examen escribes a mano y no puedes borrar. No pasa nada: el corrector acepta las correcciones si se leen bien. Lo importante es corregir rápido y limpio.</p>
<ol class="keys">""" + reglas + """</ol>
<h3>Así queda un correo corregido a mano</h3>
""" + demo + """
<ul class="dnotes">""" + "".join("<li>%s</li>" % x for x in B.DEMO_NOTAS) + """</ul>
<h3>Si encuentras...</h3>
<table class="t"><thead><tr><th>Encuentras</th><th>Haces</th></tr></thead><tbody>""" + sit + """</tbody></table>
<h3>Lo que no tienes que hacer</h3>
<ul>""" + "".join("<li>%s</li>" % x for x in B.NO_HACER) + """</ul>
<div class="tip"><b>En el ordenador</b> (en «Ahora tú») no puedes tachar: corrige directamente en tu texto. Tu profesora verá el texto antes y después de la revisión.</div>
<div class="row"><button class="btn cta" data-go="pasadas">Siguiente: caza los errores, pasada por pasada</button></div>
"""

# ------------------------------------------------------------ 4. CAZA POR PASADAS
pick_p = "".join('<button type="button" class="%s" data-act="ppick" data-k="%s"><span class="kn">%d</span>%s</button>' % (kc(p["k"]), p["k"], i + 1, p["n"]) for i, p in enumerate(B.PASADAS))
pexs = "".join('<div class="pex %s" data-pk="%s"><div class="pstrip"><span class="kn">%d</span><span><b>Pasada %d · %s</b>Mira solo: %s</span></div><p class="tline">%s</p><div class="ex" id="ex-%s"></div></div>'
               % (kc(p["k"]), p["k"], i + 1, i + 1, p["n"], p["mira"], B.EJ[p["k"]]["tarea"], p["k"]) for i, p in enumerate(B.PASADAS))
V_PASADAS = """
<span class="where">Practica · una pasada cada vez</span>
<h2>Caza los errores, pasada por pasada</h2>
<p class="lead">Textos de estudiantes de las dos tareas: correos de tú y de usted, blog, diario, biografía y fotos. En cada uno, busca solo los errores de una pasada. Así entrenas los ojos para mirar una sola cosa.</p>
<div class="pick" id="ppick" role="group" aria-label="Elige una pasada">""" + pick_p + """</div>
""" + pexs + """
<div class="row"><button class="btn" data-act="pnext">Siguiente pasada</button><button class="btn cta" data-go="reloj">Siguiente: la revisión completa a contrarreloj</button></div>
"""

# ------------------------------------------------------------ 5. A CONTRARRELOJ
V_RELOJ = """
<span class="where">Practica · todo junto</span>
<h2>Revisión completa a contrarreloj</h2>
<p class="lead">Ahora, un texto entero con la lámina y el reloj. Haz las ocho pasadas en orden: marca las frases con error, di si cada pauta tiene su frase y si el texto es corto, está bien o es largo. Cuando termines (o cuando se acabe el tiempo), comprueba.</p>
<div class="ex" id="rel"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: revisa tu texto</button></div>
"""

# ------------------------------------------------------------ 6. AHORA TU
V_AHORA = """
<span class="where">Ahora tú</span>
<h2>Ahora tú: revisa un texto tuyo en 5 minutos</h2>
<p class="lead">Elige un texto que ya escribiste en el kit de frases o en las pautas (si lo hiciste en este navegador), o pega uno nuevo. Después, cronómetro de 5 minutos y la lista: una pasada cada vez.</p>
<div class="ahora" id="ahora"></div>
<div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button></div>
"""

# ------------------------------------------------------------ 7. OPINION
STEPS = [("idea", "Los 5 minutos"), ("lista", "La lista"), ("corregir", "Cómo corregir"), ("pasadas", "Caza por pasadas"),
         ("reloj", "A contrarreloj"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]
V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo. Al copiar, también se copian los textos que has revisado en «Ahora tú» (antes y después) para que tu profesora los vea.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué pasada te cuesta más?</label>
 <div class="chips" role="group" aria-labelledby="o1l">__CHIPS1__</div>
 <label class="q" id="o2l">2. En el examen, ¿vas a guardar 5 minutos para revisar?</label>
 <div class="chips" role="group" aria-labelledby="o2l">__CHIPS2__</div>
 <label class="q" id="o3l">3. ¿Te sirve revisar con una lista y en un orden fijo?</label>
 <div class="chips" role="group" aria-labelledby="o3l">__CHIPS3__</div>
 <label class="q" for="o4">4. ¿Qué fallo has encontrado en tu texto que antes no veías? ¿Falta algo en la lista o hay algo que no has entendido?</label>
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
V_OPINION = (V_OPINION.replace("__CHIPS1__", chips("o1", [p["n"] for p in B.PASADAS]))
             .replace("__CHIPS2__", chips("o2", ["Sí, siempre", "Lo voy a intentar", "No creo: no me da tiempo"]))
             .replace("__CHIPS3__", chips("o3", ["Sí, mucho", "Un poco", "No, prefiero leer el texto entero"]))
             .replace("__EMAIL__", EMAIL))

views = {"idea": V_IDEA, "lista": V_LISTA, "corregir": V_CORREGIR, "pasadas": V_PASADAS, "reloj": V_RELOJ, "ahora": V_AHORA, "opinion": V_OPINION}
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
PAS_JS = [{"k": p["k"], "n": p["n"], "s": p["s"], "mira": p["mira"], "busca": p["busca"], "c": kc(p["k"])} for p in B.PASADAS]
EJ_JS = {}
for k, e in B.EJ.items():
    d = {"tipo": e["tipo"], "t": e["titulo"], "i": e["intro"]}
    if e["tipo"] == "q": d["items"] = e["items"]; d["fixed"] = e.get("fixed", False)
    else: d["seg"] = [{"t": s["t"], "fix": s.get("fix", ""), "por": s.get("por", "")} for s in e["seg"]]
    EJ_JS[k] = d
RELOJ_JS = [{"id": t["id"], "tipo": t["tipo"], "autor": t["autor"], "tarea": t["lamina"]["tarea"], "trato": t["trato"], "lam": lamina_html(t["lamina"]),
             "np": len(t["lamina"]["pautas"]), "pautas": [pauta_t(p) for p in t["lamina"]["pautas"]], "falta": t.get("falta", []), "largo": t["largo"],
             "lec": t["leccion"], "par": [[{"t": s["t"], "fix": s.get("fix", ""), "k": s.get("k", ""), "por": s.get("por", "")} for s in par] for par in t["par"]]}
            for t in B.RELOJ]
TRATO = {"tu": "TÚ", "usted": "USTED", None: ""}
SRC = []
for t in BF.TIPOS:
    a = t["ahora"]
    SRC.append({"s": "kit", "id": t["id"], "n": "Kit de frases · " + t["tab"], "tarea": a["tarea"], "trato": TRATO[t["trato"]],
                "lam": lamina_html(a), "pautas": [pauta_t(p) for p in a["pautas"]]})
for a in BP.AHORA:
    SRC.append({"s": "pautas", "id": a["id"], "n": "Las pautas · " + a["n"], "tarea": a["lamina"]["tarea"], "trato": TRATO[a["trato"]],
                "lam": lamina_html(a["lamina"]), "pautas": [pauta_t(p) for p in a["lamina"]["pautas"]]})
DATA = {"key": STORAGE, "kitKey": KIT_KEY, "pautasKey": PAUTAS_KEY, "steps": [{"id": k, "label": l} for k, l in STEPS],
        "pas": PAS_JS, "ej": EJ_JS, "reloj": RELOJ_JS, "tiempos": B.TIEMPOS, "src": SRC, "propio": B.TEXTO_PROPIO_TIPOS}

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
var PK = D.pas.map(function(p){ return p.k; }), PN = {}, PC = {};
D.pas.forEach(function(p){ PN[p.k]=p.n; PC[p.k]=p.c; });
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function blank(){ return {cur:'idea', seen:{}, ex:{}, pp:'pautas', rp:D.reloj[0].id, rt:300, rr:{}, rv:null, hist:[], own:{tipo:'', txt:''}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function shuffle(a){ for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function mmss(s){ s=Math.max(0,Math.round(s)); return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2); }
function rec(id, ok, n){ var r=S.ex[id]; if(!r || ok>r.b || (ok===r.b && n!==r.n)) S.ex[id]={b:ok, n:n, l:ok}; else r.l=ok; save(); nav(); }

/* ---------------- navegacion ---------------- */
function tabDone(id){
 if(id==='idea'||id==='lista'||id==='corregir') return !!S.seen[id];
 if(id==='pasadas') return PK.every(function(k){ return !!S.ex[k]; });
 if(id==='reloj') return D.reloj.some(function(t){ return !!S.rr[t.id]; });
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

/* ---------------- ejercicio q: elegir una opcion ---------------- */
var Q={};
function qNew(id){ var e=D.ej[id], idx=range(e.items.length);
 Q[id]={k:0, ok:0, ans:false, idx:idx, ord:idx.map(function(i){ var n=e.items[i].ops.length; return e.fixed?range(n):shuffle(range(n)); })}; qRender(id); }
function qRender(id){
 var e=D.ej[id], q=Q[id], box=$('ex-'+id), n=q.idx.length;
 var head='<h4>'+esc(e.t)+'</h4><p class="ei">'+esc(e.i)+'</p>';
 if(q.k>=n){
  rec(id, q.ok, n); pickMarks();
  box.innerHTML=head+'<div class="qn">RESULTADO</div><div class="score">'+q.ok+' / '+n+'</div><p>'+(q.ok===n?'¡Perfecto!':(q.ok>=n-2?'¡Muy bien! Mira otra vez las que has fallado.':'Vuelve a leer la pasada en «La lista» y prueba otra vez.'))+'</p>'+
   '<p class="small muted">Tu mejor resultado: '+S.ex[id].b+' / '+S.ex[id].n+'</p><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="qnew" data-ex="'+id+'">Otra vez</button></div>';
  return;
 }
 var it=e.items[q.idx[q.k]], o=head+'<div class="qn">'+(q.k+1)+' DE '+n+'</div><p class="qs">'+esc(it.ctx)+'</p>'+(it.p?'<p class="qp">'+esc(it.p)+'</p>':'')+'<div role="group" aria-label="Opciones">';
 q.ord[q.k].forEach(function(i){ o+='<button type="button" class="qop" data-act="qpick" data-ex="'+id+'" data-i="'+i+'">'+esc(it.ops[i])+'</button>'; });
 o+='</div><div class="qfb"></div><div class="row qnx" style="margin-bottom:0" hidden><button class="btn cta" data-act="qnext" data-ex="'+id+'">'+(q.k===n-1?'Ver el resultado':'Siguiente')+'</button></div>';
 box.innerHTML=o;
}
function qPick(b){
 var id=b.getAttribute('data-ex'), q=Q[id], it=D.ej[id].items[q.idx[q.k]], box=$('ex-'+id); if(q.ans) return;
 var i=+b.getAttribute('data-i'), ok=i===it.ok; if(ok) q.ok++; q.ans=true;
 [].forEach.call(box.querySelectorAll('.qop'), function(x){ x.disabled=true; var j=+x.getAttribute('data-i'); if(j===it.ok) x.classList.add('ok'); else if(j===i) x.classList.add('bad'); });
 box.querySelector('.qfb').innerHTML='<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Correcto!':'No es esa: '+esc(it.ops[it.ok]))+'</b> '+esc(it.por)+'</div>';
 box.querySelector('.qnx').hidden=false; box.querySelector('.qnx button').focus();
}

/* ---------------- ejercicio c: caza los errores ---------------- */
function cRender(id){
 var e=D.ej[id], o='<h4>'+esc(e.t)+'</h4><p class="ei">'+esc(e.i)+'</p><div class="segs" role="group" aria-label="Frases del texto">';
 e.seg.forEach(function(s,i){ o+='<button type="button" class="seg" data-act="cmark" data-i="'+i+'" aria-pressed="false">'+esc(s.t)+'</button>'; });
 o+='</div><div class="cres"></div><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="ccheck" data-ex="'+id+'">Comprobar</button><button class="btn" data-act="cnew" data-ex="'+id+'">Empezar otra vez</button></div>';
 $('ex-'+id).innerHTML=o;
}
function cMark(b){ if(b.disabled) return; var on=!b.classList.contains('mk'); b.classList.toggle('mk', on); b.setAttribute('aria-pressed', on?'true':'false'); }
function segOut(b, s, mk){
 b.disabled=true; b.classList.remove('mk');
 if(s.fix){ if(mk) b.classList.add('ok'); else b.classList.add('miss'); b.innerHTML+='<span class="fix">→ '+esc(s.fix)+'</span>'+(s.por?'<span class="por">'+esc(s.por)+'</span>':''); return mk?1:0; }
 if(mk){ b.classList.add('bad'); b.innerHTML+='<span class="fix w">Esta frase está bien.</span>'; return -1; }
 return 0;
}
function cCheck(id){
 var e=D.ej[id], box=$('ex-'+id), found=0, tot=0, fp=0;
 [].forEach.call(box.querySelectorAll('.seg'), function(b){
  var s=e.seg[+b.getAttribute('data-i')], r=segOut(b, s, b.classList.contains('mk'));
  if(s.fix) tot++; if(r===1) found++; if(r===-1) fp++;
 });
 var all=found===tot && fp===0;
 box.querySelector('.cres').innerHTML='<div class="fb '+(all?'ok':'bad')+'"><b>Has encontrado '+found+' de '+tot+'.</b> '+(fp?'Has marcado '+fp+' frase'+(fp>1?'s':'')+' sin error. ':'')+(all?'¡Perfecto!':'En amarillo, lo que se te ha escapado; en verde, cómo queda.')+'</div>';
 rec(id, Math.max(0, found-fp), tot); pickMarks();
}

/* ---------------- caza por pasadas: elegir pasada ---------------- */
function pShow(k){
 S.pp=k; save();
 [].forEach.call(document.querySelectorAll('.pex'), function(x){ x.classList.toggle('on', x.getAttribute('data-pk')===k); });
 pickMarks();
}
function pickMarks(){
 [].forEach.call(document.querySelectorAll('#ppick button'), function(b){ var k=b.getAttribute('data-k'); b.classList.toggle('on', k===S.pp); b.classList.toggle('dn', !!S.ex[k]); b.setAttribute('aria-pressed', k===S.pp?'true':'false'); });
}

/* ---------------- a contrarreloj ---------------- */
var R={t0:0, timer:null, run:false, done:false, pz:{}, len:''};
function rText(){ var t=D.reloj.filter(function(x){ return x.id===S.rp; })[0]; if(!t){ t=D.reloj[0]; S.rp=t.id; } return t; }
function rRender(){
 clearInterval(R.timer); R={t0:0, timer:null, run:false, done:false, pz:{}, len:''};
 var t=rText(), box=$('rel');
 var pick='<div class="pick" role="group" aria-label="Elige un texto">'+D.reloj.map(function(x,i){ var dn=!!S.rr[x.id]; return '<button type="button" class="'+(x.id===t.id?'on ':'')+(dn?'dn':'')+'" data-act="rpick" data-t="'+x.id+'">'+(i+1)+'. '+esc(x.tipo)+(dn?' ✓':'')+'</button>'; }).join('')+'</div>';
 var tms='<div class="pick" role="group" aria-label="Tiempo">'+D.tiempos.map(function(x){ return '<button type="button" class="'+(S.rt===x[0]?'on':'')+'" data-act="rtime" data-s="'+x[0]+'">'+esc(x[1])+'</button>'; }).join('')+'</div>';
 var segs=t.par.map(function(par,pi){ return '<div class="pp">'+par.map(function(s,si){ return '<button type="button" class="seg" data-act="rmark" data-i="'+pi+'-'+si+'" aria-pressed="false">'+esc(s.t)+'</button>'; }).join('')+'</div>'; }).join('');
 var pz=t.pautas.map(function(p,i){ return '<div class="prow" data-pr="'+(i+1)+'"><span class="pt"><b>'+(i+1)+'.</b> '+esc(p)+'</span><span class="tri" role="group" aria-label="Pauta '+(i+1)+'"><button type="button" data-act="rpz" data-i="'+(i+1)+'" data-v="si" aria-pressed="false">✓ Tiene su frase</button><button type="button" data-act="rpz" data-i="'+(i+1)+'" data-v="no" aria-pressed="false">✗ Falta</button></span></div>'; }).join('');
 var ln=['corto','bien','largo'].map(function(v){ return '<button type="button" data-act="rlen" data-v="'+v+'" aria-pressed="false">'+(v==='corto'?'Corto':v==='bien'?'Bien':'Largo')+'</button>'; }).join('');
 box.innerHTML='<h4>Elige un texto</h4>'+pick+'<h4>Elige el tiempo</h4>'+tms+
  '<p class="small">Esta es la tarea de '+esc(t.autor)+'. Léela primero (sin reloj); cuando estés listo, pulsa «Empezar» y aparece su texto.</p>'+t.lam+
  '<div class="row"><button class="btn cta" data-act="rstart">Empezar'+(S.rt?' ('+mmss(S.rt)+')':'')+'</button></div>'+
  '<div id="rarea" hidden><div class="clock" id="rclock" role="timer" aria-live="off"><span class="tm" id="rtm">'+(S.rt?mmss(S.rt):'0:00')+'</span><span class="msg2" id="rmsg">'+(S.rt?'Tiempo que queda':'Tiempo')+'</span></div>'+
  '<h4>El texto de '+esc(t.autor)+'</h4><p class="small muted">Toca las frases con un error (de cualquier pasada).</p><div class="segs" role="group" aria-label="Frases del texto">'+segs+'</div>'+
  '<h4 style="margin-top:14px">Pasada 1: ¿cada pauta tiene su frase?</h4>'+pz+
  '<h4 style="margin-top:14px">Pasada 8: las líneas</h4><p class="small">A mano tendría unas '+t.lines+' líneas. Para esta tarea es...</p><div class="tri" role="group" aria-label="Longitud">'+ln+'</div>'+
  '<div class="rres"></div><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="rcheck">He terminado: comprobar</button><button class="btn" data-act="rreset">Empezar otra vez</button></div></div>';
}
function rStart(){
 if(R.run) return; R.run=true; R.t0=Date.now();
 $('rarea').hidden=false; document.querySelector('[data-act="rstart"]').closest('.row').hidden=true;
 R.timer=setInterval(rTick, 250); rTick(); $('rclock').scrollIntoView({behavior:'smooth', block:'start'});
}
function rTick(){
 var el=(Date.now()-R.t0)/1000, c=$('rclock'); if(!c) return;
 if(S.rt){ var left=S.rt-el; $('rtm').textContent=mmss(Math.ceil(left)); c.classList.toggle('warn', left<=60 && left>0);
  if(left<=0){ c.classList.add('over'); rCheck(true); } }
 else $('rtm').textContent=mmss(el);
}
function rPz(b){ if(R.done) return; var i=b.getAttribute('data-i'); R.pz[i]=b.getAttribute('data-v');
 [].forEach.call(b.parentNode.querySelectorAll('button'), function(x){ x.setAttribute('aria-pressed', x===b?'true':'false'); }); }
function rLen(b){ if(R.done) return; R.len=b.getAttribute('data-v');
 [].forEach.call(b.parentNode.querySelectorAll('button'), function(x){ x.setAttribute('aria-pressed', x===b?'true':'false'); }); }
function rCheck(timeout){
 if(R.done || !R.run) return; R.done=true; clearInterval(R.timer);
 var t=rText(), used=Math.min((Date.now()-R.t0)/1000, S.rt||1e9), tot={}, fnd={}, fp=0;
 PK.forEach(function(k){ tot[k]=0; fnd[k]=0; });
 [].forEach.call($('rarea').querySelectorAll('.seg'), function(b){
  var ij=b.getAttribute('data-i').split('-'), s=t.par[+ij[0]][+ij[1]], r=segOut(b, s, b.classList.contains('mk'));
  if(s.fix){ tot[s.k]++; if(r===1) fnd[s.k]++; b.insertAdjacentHTML('afterbegin','<span class="tag '+PC[s.k]+'">'+esc(PN[s.k])+'</span>'); }
  if(r===-1) fp++;
 });
 tot.pautas=t.np;
 for(var i=1;i<=t.np;i++){ var right=t.falta.indexOf(i)>=0?'no':'si', a=R.pz[i]; if(a===right) fnd.pautas++;
  [].forEach.call($('rarea').querySelectorAll('[data-pr="'+i+'"] button'), function(x){ x.disabled=true; var v=x.getAttribute('data-v'); if(v===right) x.classList.add('right'); else if(v===a) x.classList.add('wrong'); }); }
 tot.lin=1; if(R.len===t.largo) fnd.lin=1;
 [].forEach.call($('rarea').querySelectorAll('[data-act="rlen"]'), function(x){ x.disabled=true; var v=x.getAttribute('data-v'); if(v===t.largo) x.classList.add('right'); else if(v===R.len) x.classList.add('wrong'); });
 var sf=0, st=0, rows=PK.map(function(k){ if(!tot[k]) return ''; sf+=fnd[k]; st+=tot[k]; var ok=fnd[k]===tot[k];
  return '<tr><td><span class="kn '+PC[k]+'" style="min-width:22px;height:22px;font-size:.75rem">'+(PK.indexOf(k)+1)+'</span> '+esc(PN[k])+'</td><td><b style="color:var(--'+(ok?'ok':'bad')+')">'+fnd[k]+' de '+tot[k]+'</b></td></tr>'; }).join('');
 var score=Math.max(0, sf-fp);
 $('rarea').querySelector('.rres').innerHTML=(timeout?'<div class="fb bad"><b>¡Tiempo!</b> En el examen, aquí entregas. Mira qué has encontrado y qué se te ha escapado.</div>':'')+
  '<div class="fb '+(score===st?'ok':'bad')+'"><b>'+sf+' de '+st+' bien</b> en '+mmss(used)+(fp?'. Has marcado '+fp+' frase'+(fp>1?'s':'')+' sin error':'')+'.</div>'+
  '<table class="t res"><thead><tr><th>Pasada</th><th>Encontrado</th></tr></thead><tbody>'+rows+'</tbody></table>'+
  '<div class="lec"><b>La lección:</b> '+esc(t.lec)+'</div>';
 var per={}; PK.forEach(function(k){ if(tot[k]) per[k]=[fnd[k],tot[k]]; });
 var prev=S.rr[t.id]; if(!prev || score>prev.b) S.rr[t.id]={b:score, n:st, per:per, fp:fp, used:Math.round(used), lim:S.rt};
 save(); nav();
 var pk=$('rel').querySelector('[data-t="'+t.id+'"]'); if(pk && pk.textContent.indexOf('✓')<0){ pk.classList.add('dn'); pk.textContent+=' ✓'; }
 document.querySelector('[data-act="rcheck"]').disabled=true;
}

/* ---------------- ahora tu ---------------- */
var A={t0:0, timer:null, base:0, ps:0};
function other(key){ try{ var r=localStorage.getItem(key); return r?JSON.parse(r):null; }catch(e){ return null; } }
function srcText(s){ var o=other(s.s==='kit'?D.kitKey:D.pautasKey); return (o && o.w && o.w[s.id] && String(o.w[s.id]).trim()) ? String(o.w[s.id]) : ''; }
function aRender(){
 clearInterval(A.timer); A.timer=null;
 var box=$('ahora'), v=S.rv;
 if(!v){
  var any=false, list=D.src.map(function(s,i){ var w=srcText(s); if(w) any=true;
   return '<button type="button" class="src" data-act="asrc" data-i="'+i+'"'+(w?'':' disabled')+'><b>'+esc(s.n)+'</b><small>'+(w?esc(w.trim().split(/\s+/).slice(0,9).join(' '))+'...':'Sin texto en este navegador')+'</small></button>'; }).join('');
  box.innerHTML='<h4 style="margin-top:0">1. Elige el texto</h4><p class="small">Textos que escribiste en «Ahora tú» del kit de frases y de las pautas'+(any?'':' (en este navegador no hay ninguno todavía: escribe uno allí o pega uno aquí abajo)')+'.</p><div class="srcs">'+list+'</div>'+
   '<h4>... o pega otro texto tuyo</h4><p><label>Tipo de texto: <select id="otipo"><option value="">— elige —</option>'+D.propio.map(function(x){ return '<option'+(S.own.tipo===x?' selected':'')+'>'+esc(x)+'</option>'; }).join('')+'</select></label></p>'+
   '<textarea id="otxt" aria-label="Tu texto" placeholder="Pega o escribe aquí tu texto...">'+esc(S.own.txt||'')+'</textarea>'+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="aown">Revisar este texto</button></div><div class="saved" id="aownmsg" role="status"></div>'+
   (S.hist.length?'<p class="small muted" style="margin-top:14px">Revisiones guardadas: '+S.hist.length+'. Se copian en «Tu opinión».</p>':'');
  return;
 }
 var head='<h4 style="margin-top:0">'+esc(v.n)+'</h4>'+(v.lam?'<details><summary>Ver la lámina</summary>'+v.lam+'</details>':'')+
  '<h4>Tu texto antes de revisar</h4><div class="orig">'+esc(v.orig)+'</div>'+
  '<h4>Tu texto revisado</h4><p class="small">Corrige aquí, directamente. En el examen, a mano, tachas con una raya y escribes encima.</p><textarea id="arev" aria-label="Tu texto revisado">'+esc(v.rev)+'</textarea><div class="saved" id="arevmsg" role="status"></div>';
 if(v.done){
  var rows=PK.map(function(k){ return '<tr><td>'+esc(PN[k])+'</td><td><b>'+(v.f[k]||0)+'</b></td></tr>'; }).join(''), tf=PK.reduce(function(a,k){ return a+(v.f[k]||0); },0);
  var most=PK.filter(function(k){ return (v.f[k]||0)>0; }).sort(function(a,b){ return (v.f[b]||0)-(v.f[a]||0); })[0];
  box.innerHTML=head+'<div class="fb ok"><b>Revisión terminada en '+mmss(v.used)+'.</b> Has corregido '+tf+' fallo'+(tf===1?'':'s')+'.'+(v.used>300?' Te has pasado de los 5 minutos: con la práctica irás más rápido.':'')+(most?' Lo que más se te escapa: <b>'+esc(PN[most])+'</b>. Mira esa pasada en «La lista» antes de tu próximo texto.':'')+'</div>'+
   '<table class="t"><thead><tr><th>Pasada</th><th>Fallos corregidos</th></tr></thead><tbody>'+rows+'</tbody></table>'+
   '<p class="small">Tu revisión está guardada: se copia con tu opinión, con el texto antes y después.</p><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="anew">Revisar otro texto</button></div>';
  return;
 }
 if(!v.started){
  box.innerHTML=head+'<div class="row"><button class="btn cta" data-act="astart">Empezar los 5 minutos</button><button class="btn" data-act="anew">Elegir otro texto</button></div>';
  return;
 }
 var p=D.pas[v.step], k=p.k, extra='';
 if(k==='pautas'){
  extra=v.pautas.length?'<ul class="chkp">'+v.pautas.map(function(x,i){ return '<li><label><input type="checkbox" data-apz="'+i+'"'+(v.pz[i]?' checked':'')+'><span><b>'+(i+1)+'.</b> '+esc(x)+'</span></label></li>'; }).join('')+'</ul><p class="small muted">Marca cada pauta que tiene su frase (con todas sus piezas). Si falta algo, añádelo en tu texto revisado.</p>'
   :'<p class="small muted">Con tu mini lista: ¿cada pieza tiene su ✓? Si falta algo, añádelo en tu texto revisado.</p>';
 }
 if(k==='trato') extra='<p class="small">'+(v.trato?'Este texto es de <b>'+v.trato+'</b>: el saludo, la despedida y las preguntas, todo igual.':'Si es un correo: ¿tú o usted? Si es un blog: vosotros. Todo igual, del principio al final.')+'</p>';
 if(k==='lin') extra='<p class="small">A mano, ¿cuántas líneas tendría? Tarea '+(v.tarea||'1 o 2')+': '+(v.tarea===2?'7-8 líneas':v.tarea===1?'6-7 líneas':'T1, 6-7 líneas; T2, 7-8')+'.</p><div class="tri" role="group" aria-label="Longitud">'+['Corto','Bien','Largo'].map(function(x){ return '<button type="button" data-act="alen" data-v="'+x+'" aria-pressed="'+(v.len===x?'true':'false')+'">'+x+'</button>'; }).join('')+'</div>';
 box.innerHTML=head+'<div class="clock" id="aclock" role="timer" aria-live="off"><span class="tm" id="atm">5:00</span><span class="msg2" id="amsg">Pasada '+(v.step+1)+' de 8</span></div>'+
  '<div class="run '+p.c+'"><div class="ph"><span class="kn">'+(v.step+1)+'</span><h4>'+esc(p.n)+'</h4><span class="small muted">unos '+mmss(p.s)+'</span></div><div class="pbar"><i id="apbar"></i></div>'+
  '<p><b>Mira solo:</b> '+p.mira+'</p><p class="small"><b>Buscas:</b> '+p.busca+'</p>'+extra+
  '<p style="margin-bottom:0"><b>Fallos que he encontrado y corregido en esta pasada:</b></p><div class="cnt"><button type="button" data-act="afal" data-d="-1" aria-label="Uno menos">−</button><output id="afcnt">'+(v.f[k]||0)+'</output><button type="button" data-act="afal" data-d="1" aria-label="Uno más">+</button></div>'+
  '<div class="row" style="margin-bottom:0"><button class="btn" data-act="astep" data-d="-1"'+(v.step===0?' disabled':'')+'>← Anterior</button>'+(v.step<7?'<button class="btn cta" data-act="astep" data-d="1">Hecho: siguiente pasada →</button>':'<button class="btn cta" data-act="aend">Terminar la revisión</button>')+'</div></div>';
 A.base=v.used||0; A.t0=Date.now(); A.ps=Date.now(); A.timer=setInterval(aTick, 250); aTick();
}
function aTick(){
 var v=S.rv; if(!v || !$('atm')) return;
 var used=A.base+(Date.now()-A.t0)/1000, left=300-used, c=$('aclock');
 $('atm').textContent=left>=0?mmss(Math.ceil(left)):'+'+mmss(-left);
 c.classList.toggle('warn', left<=60 && left>0); c.classList.toggle('over', left<=0);
 if(left<=0) $('amsg').textContent='¡Tiempo! En el examen, aquí entregas · pasada '+(v.step+1)+' de 8';
 var p=D.pas[v.step], ps=(Date.now()-A.ps)/1000, bar=$('apbar'); if(bar) bar.style.width=Math.min(100, ps/p.s*100)+'%';
 v.used=Math.round(used);
}
function aSaveTime(){ if(S.rv && A.timer){ S.rv.used=Math.round(A.base+(Date.now()-A.t0)/1000); } save(); }
function aStart(){ S.rv.started=true; S.rv.step=0; S.rv.used=0; save(); aRender(); $('aclock').scrollIntoView({behavior:'smooth', block:'start'}); }
function aChoose(n, orig, s){
 S.rv={n:n, orig:orig, rev:orig, tarea:s?s.tarea:0, trato:s?s.trato:'', lam:s?s.lam:'', pautas:s?s.pautas:[], step:0, f:{}, pz:{}, len:'', used:0, started:false, done:false};
 save(); aRender();
}
function aEnd(){
 aSaveTime(); clearInterval(A.timer); A.timer=null; var v=S.rv; v.done=true;
 S.hist.push({n:v.n, orig:v.orig, rev:v.rev, f:v.f, pz:Object.keys(v.pz).filter(function(i){ return v.pz[i]; }).length, np:v.pautas.length, len:v.len, used:v.used, d:new Date().toISOString().slice(0,10)});
 if(S.hist.length>6) S.hist=S.hist.slice(-6);
 save(); nav(); aRender();
}

/* ---------------- opinion ---------------- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked = r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function summary(){
 var done=PK.filter(function(k){ return S.ex[k]; }).length, rr=D.reloj.filter(function(t){ return S.rr[t.id]; }).length;
 $('sum').innerHTML='<li>Caza por pasadas: '+done+' de 8.</li><li>A contrarreloj: '+rr+' de '+D.reloj.length+' textos.</li><li>Textos revisados en «Ahora tú»: '+S.hist.length+'.</li>';
}
function pack(){
 var L=['CURSO DELE A2 - ESCRITURA: LA REVISIÓN FINAL DE 5 MINUTOS', 'Nombre: '+(S.name||'-'), '', 'CAZA POR PASADAS (mejor resultado):'];
 D.pas.forEach(function(p,i){ var r=S.ex[p.k]; L.push('  '+(i+1)+'. '+p.n+': '+(r?r.b+'/'+r.n:'sin hacer')); });
 L.push('', 'A CONTRARRELOJ (mejor resultado):');
 D.reloj.forEach(function(t){ var r=S.rr[t.id]; if(!r){ L.push('  '+t.tipo+' ('+t.autor+'): sin hacer'); return; }
  L.push('  '+t.tipo+' ('+t.autor+'): '+r.b+'/'+r.n+' en '+mmss(r.used)+(r.lim?' (con '+mmss(r.lim)+')':' (sin reloj)')+(r.fp?', '+r.fp+' frase(s) bien marcadas como error':''));
  L.push('     '+PK.filter(function(k){ return r.per[k]; }).map(function(k){ return PN[k]+' '+r.per[k][0]+'/'+r.per[k][1]; }).join(' · ')); });
 L.push('', 'MIS REVISIONES ("Ahora tú"):');
 if(!S.hist.length) L.push('  (todavía no he revisado ningún texto)');
 S.hist.forEach(function(h,i){
  var tf=PK.reduce(function(a,k){ return a+(h.f[k]||0); },0);
  L.push('', '== '+(i+1)+'. '+h.n+' ('+h.d+') ==', 'Tiempo: '+mmss(h.used)+' · fallos corregidos: '+tf+(h.np?' · pautas con su frase: '+h.pz+' de '+h.np:'')+(h.len?' · longitud: '+h.len:''),
   'Por pasada: '+PK.map(function(k){ return PN[k]+' '+(h.f[k]||0); }).join(' · '), '', 'ANTES:', h.orig.trim(), '', 'DESPUÉS:', (h.rev||'').trim());
 });
 L.push('', 'OPINIÓN:', '1. La pasada que más me cuesta: '+(S.o1||'-'), '2. ¿Voy a guardar 5 minutos?: '+(S.o2||'-'), '3. ¿Me sirve la lista en orden fijo?: '+(S.o3||'-'), '4. Fallo que no veía / falta algo: '+(S.o4||'-'), '5. Sensación de control en la Escritura (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 qnew:function(b){ qNew(b.getAttribute('data-ex')); },
 qpick:function(b){ qPick(b); },
 qnext:function(b){ var id=b.getAttribute('data-ex'); Q[id].k++; Q[id].ans=false; qRender(id); },
 cmark:function(b){ cMark(b); },
 ccheck:function(b){ cCheck(b.getAttribute('data-ex')); },
 cnew:function(b){ cRender(b.getAttribute('data-ex')); },
 ppick:function(b){ pShow(b.getAttribute('data-k')); },
 pnext:function(){ var i=PK.indexOf(S.pp); pShow(PK[(i+1)%PK.length]); $('ppick').scrollIntoView({behavior:'smooth'}); },
 rpick:function(b){ S.rp=b.getAttribute('data-t'); save(); rRender(); },
 rtime:function(b){ S.rt=+b.getAttribute('data-s'); save(); rRender(); },
 rstart:function(){ rStart(); },
 rmark:function(b){ if(!R.done) cMark(b); },
 rpz:function(b){ rPz(b); },
 rlen:function(b){ rLen(b); },
 rcheck:function(){ rCheck(false); },
 rreset:function(){ rRender(); },
 asrc:function(b){ var s=D.src[+b.getAttribute('data-i')], w=srcText(s); if(w) aChoose(s.n, w, s); },
 aown:function(){ var t=($('otxt').value||'').trim(), tp=$('otipo').value; if(!t){ $('aownmsg').textContent='Primero pega o escribe tu texto.'; return; }
  var tarea=(tp.indexOf('Correo')===0)?1:(tp?2:0), trato=tp==='Correo a un amigo'?'TÚ':tp==='Correo de usted'?'USTED':'';
  aChoose('Mi texto'+(tp?' · '+tp:''), t, {tarea:tarea, trato:trato, lam:'', pautas:[]}); },
 astart:function(){ aStart(); },
 astep:function(b){ aSaveTime(); var d=+b.getAttribute('data-d'); S.rv.step=Math.max(0, Math.min(7, S.rv.step+d)); save(); aRender(); },
 aend:function(){ aEnd(); },
 anew:function(){ aSaveTime(); S.rv=null; save(); aRender(); },
 afal:function(b){ var k=D.pas[S.rv.step].k, n=(S.rv.f[k]||0)+(+b.getAttribute('data-d')); S.rv.f[k]=Math.max(0, Math.min(20, n)); $('afcnt').textContent=S.rv.f[k]; aSaveTime(); },
 alen:function(b){ S.rv.len=b.getAttribute('data-v'); [].forEach.call(b.parentNode.querySelectorAll('button'), function(x){ x.setAttribute('aria-pressed', x===b?'true':'false'); }); aSaveTime(); },
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
 var a=e.target.closest('[data-act]'); if(a && !a.disabled && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
var svT;
function savedMsg(id){ var el=$(id); if(!el) return; el.textContent='✓ Guardado en este navegador'; clearTimeout(svT); svT=setTimeout(function(){ el.textContent=''; },1800); }
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.getAttribute('data-apz')!==null){ S.rv.pz[t.getAttribute('data-apz')]=t.checked; aSaveTime(); return; }
 if(t.id==='otipo'){ S.own.tipo=t.value; save(); return; }
 if(t.name==='o1'||t.name==='o2'||t.name==='o3'||t.name==='o5'){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){ var t=e.target;
 if(t.id==='arev'){ S.rv.rev=t.value; aSaveTime(); savedMsg('arevmsg'); return; }
 if(t.id==='otxt'){ S.own.txt=t.value; save(); return; }
 if(t.id==='o4'){ S.o4=t.value; save(); nav(); } if(t.id==='sname'){ S.name=t.value; save(); } });
window.addEventListener('afterprint', function(){ [].forEach.call(document.querySelectorAll('.printme'), function(v){ v.classList.remove('printme'); }); });
window.addEventListener('pagehide', aSaveTime);

PK.forEach(function(k){ if(D.ej[k].tipo==='q') qNew(k); else cRender(k); });
pShow(PK.indexOf(S.pp)>=0?S.pp:'pautas'); rRender(); aRender(); renderScale();
go(D.steps.some(function(s){ return s.id===S.cur; }) ? S.cur : 'idea');
})();
"""

for t in DATA["reloj"]:  # líneas a mano del texto tal como está (sin corregir), para la pasada 8
    t["lines"] = (lambda n: "%d" % round(n / 10) if n % 10 < 3 or n % 10 > 7 else "%d y media" % (n // 10))(sum(words(s["t"]) for par in t["par"] for s in par))
js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_R, body, js))
print("ok", FILE, "· lista: %s + %d s de margen" % (SUMA, MARGEN),
      "· caza:", ", ".join("%s %d" % (k, len(e.get("items") or [s for s in e["seg"] if s.get("fix")])) for k, e in B.EJ.items()),
      "· contrarreloj:", "; ".join("%s %d pal. %d errores falta %s" % x for x in RSTAT),
      "· fuentes de Ahora tú:", len(SRC), "· fotos comprobadas:", NFOTOS[0])
