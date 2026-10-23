# -*- coding: utf-8 -*-
# MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 5: TEXTOS MODELO (APROBADO Y EXCELENTE)
# Uso: python3 build_M3_modelos.py
#  -> DELEA2_curso_M3_textos_modelo.html  (subir a biblioteca/recursos/A2/dele-curso/)
# Contenido (bandas, textos modelo, mejoras, ejercicios, «¿Aprueba?», láminas nuevas): banco_modelos_M3.py.
# Usa también las láminas de «Ahora tú» del kit (banco_frases_M3.py) y de las pautas (banco_pautas_M3.py): en
# «Ahora tú» el estudiante puede subir de nivel un texto que escribió allí o que revisó en la revisión final
# (se lee del mismo navegador).
# Mismo estilo que el kit, las pautas y la revisión: pestañas, progreso en el navegador (storageKey propio),
# botón Copiar con los textos antes y después de mejorarlos y preguntas de opinión al final.
# Sin contador de palabras para el estudiante: las líneas se cuentan a ojo (unas 10 palabras por línea).
# 12/10/2026: las laminas con fotos llevan imagenes de verdad (fotos_M3.py); el build comprueba nombre, prompt y alt.
import json, re
from curso_comun import CSS, EMAIL, page
import fotos_M3 as FT
import banco_modelos_M3 as B
import banco_frases_M3 as BF
import banco_pautas_M3 as BP

TITLE = "Textos modelo: aprobado y excelente"
FILE = "DELEA2_curso_M3_textos_modelo.html"
STORAGE = "dele-a2-curso-M3-modelos"
KIT_KEY = "dele-a2-curso-M3-kit"
PAUTAS_KEY = "dele-a2-curso-M3-pautas"
REV_KEY = "dele-a2-curso-M3-revision"

PAL = re.compile(r"[\wÀ-ſ]+(?:-[\wÀ-ſ]+)*")
MK = re.compile(r"\{(\w+):([^{}]+)\}")
TU_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(tú|tu|tus|te|ti|contigo|tienes|puedes|quieres|podrías|recomiendas|perdona|oye|beso|abrazo)(?![\wÀ-ſ])")
US_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(usted|ustedes|su|sus|atentamente|estimad[oa]s?|cordiales?|perdone|disculpe|podría|saludo)(?![\wÀ-ſ])")
TENSES = {"pr": "presente", "in": "indefinido", "im": "imperfecto", "pe": "perfecto", "fu": "futuro (ir a)", "co": "condicional", "ip": "imperativo"}
MARKS = set(TENSES) | {"c", "T", "U"}

def strip(s): return MK.sub(lambda m: m.group(2), s)
def words(s): return len(PAL.findall(s))
def lineas(n):
    l, r = n // 10, n % 10
    return "unas %d líneas" % (l + (1 if r > 7 else 0)) if r < 3 or r > 7 else "unas %d líneas y media" % l
MEJ = {m["k"]: m for m in B.MEJORAS}
MKEYS = [m["k"] for m in B.MEJORAS]
assert MKEYS == ["con", "pas", "det", "pal", "preg", "cuan"], MKEYS
CORTO = {"con": "+ conector", "pas": "pasados", "det": "detalle", "pal": "palabra precisa", "preg": "pregunta", "cuan": "cuando / porque"}

def limits(tarea): return (60, 70) if tarea == 1 else (70, 80)

# ------------------------------------------------------------ comprobaciones del banco
def segs_of(t, k):
    return [s for par in t[k] for s in par]

def marks_ok(txt, ref):
    for m in MK.finditer(txt): assert m.group(1) in MARKS, ref + ": marca desconocida {%s:" % m.group(1)
    assert "{" not in strip(txt) and "}" not in strip(txt), ref + ": llaves sueltas en: " + txt

def text_stats(segs):
    con, ten = [], []
    for s in segs:
        for m in MK.finditer(s[1]):
            if m.group(1) == "c":
                w = m.group(2).lower()
                if w not in con: con.append(w)
            elif m.group(1) in TENSES and m.group(1) not in ten: ten.append(m.group(1))
    n = words(" ".join(strip(s[1]) for s in segs))
    return {"n": n, "con": con, "ten": [t for t in TENSES if t in ten]}

STATS = {}
USADAS = set()
NFOTOS = [0]
for t in B.TIPOS:
    l = t["lamina"]; np_ = len(l["pautas"]); mn, mx = limits(l["tarea"])
    NFOTOS[0] += FT.check(l, "Modelo " + t["id"])
    for k in ("ap", "ex"):
        ref = "%s/%s" % (t["id"], k)
        segs = segs_of(t, k)
        for s in segs:
            marks_ok(s[1], ref)
            assert not re.search(r"\{[TU]:", s[1]), ref + ": {T:}/{U:} solo en «¿Aprueba?»"
            if k == "ap": assert len(s) == 2, ref + ": el aprobado no lleva mejoras"
            else:
                assert len(s) == 3 and all(m in MEJ for m in s[2]), ref + ": mejoras desconocidas en " + s[1]
        cub = set(s[0] for s in segs if s[0])
        assert cub == set(range(1, np_ + 1)), ref + ": pautas con frase %s de %d" % (sorted(cub), np_)
        st = text_stats(segs)
        assert mn <= st["n"] <= mx, ref + ": %d palabras (%d-%d)" % (st["n"], mn, mx)
        plain = " ".join(strip(s[1]) for s in segs)
        if t["trato"] == "tu": assert not US_PAL.search(plain), ref + ": usted en un correo de tú: " + US_PAL.search(plain).group(0)
        if t["trato"] == "usted": assert not TU_PAL.search(plain), ref + ": tú en un correo de usted: " + TU_PAL.search(plain).group(0)
        if t["trato"] is None: assert not re.search(r"(?i)(?<![\wÀ-ſ])usted(?![\wÀ-ſ])", plain), ref + ": usted en un texto de la tarea 2"
        STATS[ref] = st
    a, e = STATS[t["id"] + "/ap"], STATS[t["id"] + "/ex"]
    assert len(e["con"]) > len(a["con"]), t["id"] + ": el excelente no usa más conectores distintos (%d / %d)" % (len(e["con"]), len(a["con"]))
    assert len(e["ten"]) > len(a["ten"]), t["id"] + ": el excelente no usa más tiempos distintos (%d / %d)" % (len(e["ten"]), len(a["ten"]))
    mej = set(m for s in segs_of(t, "ex") for m in s[2])
    assert len(mej) >= 3, t["id"] + ": el excelente usa solo %d mejoras" % len(mej)
    USADAS |= mej
    assert len(t["por_ap"]) >= 3 and len(t["por_ex"]) >= 3
assert USADAS == set(MKEYS), "Mejoras que no salen en ningún excelente: %s" % (set(MKEYS) - USADAS)

assert len(B.CLAS) >= 10 and all(q["ok"] in (0, 1) for q in B.CLAS)
assert sum(q["ok"] == 0 for q in B.CLAS) >= 4 and sum(q["ok"] == 1 for q in B.CLAS) >= 4
assert len(B.SUBE) >= 8 and all(len(q["ops"]) == 3 for q in B.SUBE)
assert B.HUECOS["texto"].count("[[") == len(B.HUECOS["huecos"]) and all(len(h["ops"]) == 3 for h in B.HUECOS["huecos"])

AST = []
for a in B.APRUEBA:
    ref = "¿Aprueba? " + a["id"]; l = a["lamina"]; np_ = len(l["pautas"]); mn, mx = limits(l["tarea"])
    NFOTOS[0] += FT.check(l, ref)
    assert len(a["est"]) == np_ and set(a["est"]) <= {"si", "medias", "falta"}, ref
    segs = [s for par in a["par"] for s in par]
    for s in segs: marks_ok(s[1], ref)
    cub = set(s[0] for s in segs if s[0])
    for i, e in enumerate(a["est"]):
        if e == "falta": assert i + 1 not in cub, ref + ": la pauta %d «falta» pero tiene frase" % (i + 1)
        else: assert i + 1 in cub, ref + ": la pauta %d no tiene frase" % (i + 1)
    plain = " ".join(strip(s[1]) for s in segs); n = words(plain)
    if a["v"] == 0:
        assert set(a["est"]) == {"si"} and mn <= n <= mx, ref + ": un texto que aprueba tiene todas las pautas y las palabras (%d)" % n
        if a["trato"] == "tu": assert not US_PAL.search(plain), ref
        if a["trato"] == "usted": assert not TU_PAL.search(plain), ref
    elif a["v"] == 1:
        assert "falta" in a["est"] and ("medias" in a["est"] or a["est"].count("falta") > 1), ref + ": una pauta falta y otra está a medias (banda 1 de cumplimiento)"
    else:
        assert set(a["est"]) == {"si"} and TU_PAL.search(plain) and US_PAL.search(plain), ref + ": mezcla tú y usted con todas las pautas"
        assert re.search(r"\{T:", " ".join(s[1] for s in segs)) and re.search(r"\{U:", " ".join(s[1] for s in segs)), ref + ": marca {T:} y {U:}"
    AST.append("%s %s %d pal." % (a["id"], ["aprueba", "falta", "mezcla"][a["v"]], n))
for v in (0, 1, 2): assert sum(a["v"] == v for a in B.APRUEBA) >= 2, "Al menos dos textos de cada veredicto"
assert len(B.AHORA_NUEVAS) >= 3
for a in B.AHORA_NUEVAS: NFOTOS[0] += FT.check(a["lamina"], "Nueva " + a["id"])
for t in BF.TIPOS: NFOTOS[0] += FT.check(t["ahora"], "Kit (ahora tú) " + t["id"])
for a in BP.AHORA: NFOTOS[0] += FT.check(a["lamina"], "Pautas (ahora tú) " + a["id"])

# ------------------------------------------------------------ CSS
CSS_M = CSS + r"""
section.view > h3{margin-top:30px}
.row[hidden],[hidden]{display:none!important}
.where{display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.04em;background:var(--ink);color:#fff;border-radius:999px;padding:2px 12px;margin-bottom:8px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px}
.box h4{margin:0 0 2px}.box p{margin:4px 0;font-size:.95rem}.box ul{margin:6px 0 0;padding-left:1.2em;font-size:.95rem}
.box .wt{display:inline-block;font-size:.78rem;font-weight:700;background:var(--coral-soft);color:#9A3412;border-radius:999px;padding:1px 10px;margin:2px 0 6px}
.big{font-family:Georgia,serif;font-size:1.3rem;line-height:1.35;background:#fff;border:3px solid var(--coral);border-radius:14px;padding:16px 20px;margin:14px 0}
.big small{display:block;font-family:system-ui,sans-serif;font-size:.9rem;color:var(--muted);margin-top:6px}
table.bands td.b{font-family:Georgia,serif;font-size:1.5rem;font-weight:700;text-align:center;width:52px}
table.bands tr.b2 td{background:var(--ok-soft)}table.bands tr.b3 td{background:#E4ECF8}
table.bands td.pt{white-space:nowrap;font-weight:600}
.notes{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.ncard{background:#fff;border:2px solid var(--line);border-radius:12px;padding:12px 16px}
.ncard h4{margin:0 0 6px}.ncard .q{font-size:.95rem;font-style:italic;background:#F6F3EF;border-radius:8px;padding:8px 12px}
.ncard .sc{display:flex;gap:8px;margin:10px 0 6px}
.ncard .sc span{flex:1;border:2px solid var(--ink);border-radius:10px;padding:4px 8px;text-align:center;font-size:.8rem;line-height:1.2}
.ncard .sc b{display:block;font-family:Georgia,serif;font-size:1.5rem}
.ncard .sc span.lo{border-color:var(--bad);background:var(--bad-soft)}.ncard .sc span.hi{border-color:#2B5FA8;background:#E4ECF8}
.ncard p{margin:4px 0;font-size:.93rem}
/* pautas, conectores, tiempos, mejoras */
.p1{--pc:#2B5FA8;--ps:#E4ECF8}.p2{--pc:#C2410C;--ps:#FFE2D6}.p3{--pc:#2F7D4F;--ps:#E3F1E8}.p4{--pc:#9A6A10;--ps:#FBF0DA}.p5{--pc:#6E4FB8;--ps:#ECE6F7}
.sg{background:var(--ps,transparent);border-radius:5px;padding:1px 3px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.pn{display:inline-grid;place-items:center;min-width:19px;height:19px;border-radius:50%;background:var(--pc);color:#fff;font-size:.7rem;font-weight:700;margin-right:4px;vertical-align:2px;font-family:system-ui,sans-serif}
.cx{text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:3px;text-decoration-color:var(--coral);font-weight:600}
.mj{display:inline-block;font-style:normal;font-size:.68rem;font-weight:700;border-radius:999px;padding:0 7px;margin-left:3px;vertical-align:2px;color:#fff;background:var(--mc);font-family:system-ui,sans-serif;line-height:1.6}
.m-con{--mc:#2F7D4F}.m-pas{--mc:#E8603C}.m-det{--mc:#2B5FA8}.m-pal{--mc:#B8407A}.m-preg{--mc:#6E4FB8}.m-cuan{--mc:#9A6A10}
.v-pr{--vc:#2B5FA8}.v-in{--vc:#C2410C}.v-im{--vc:#9A6A10}.v-pe{--vc:#6E4FB8}.v-fu{--vc:#2F7D4F}.v-co{--vc:#B8407A}.v-ip{--vc:#2A8C86}
.tv .vb{color:var(--vc);font-weight:700;border-bottom:2px dotted var(--vc)}
.nomark .sg{background:none;padding:0}.nomark .pn,.nomark .mj{display:none}.nomark .cx{text-decoration:none;font-weight:inherit}
.nomark .vb{color:inherit!important;font-weight:inherit!important;border:0!important}
mark.mt,mark.mu{border-radius:4px;padding:0 3px;font-weight:700}
mark.mt{background:#FFD7C2;color:#9A3412}mark.mu{background:#D6E4F7;color:#1E4A87}
/* barra de herramientas y leyenda */
.tools{position:sticky;top:96px;z-index:5;background:var(--paper);padding:8px 0;display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;border-bottom:1px solid var(--line)}
.seg2{display:inline-flex;border:2px solid var(--ink);border-radius:999px;overflow:hidden}
.seg2 button{font:inherit;font-size:.86rem;font-weight:600;border:0;background:#fff;padding:4px 12px;cursor:pointer;color:inherit}
.seg2 button[aria-pressed="true"]{background:var(--ink);color:#fff}
.tools label{font-size:.88rem;display:inline-flex;gap:6px;align-items:center;cursor:pointer}
.tools input{width:18px;height:18px;accent-color:var(--ink)}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.84rem;color:var(--muted);margin:10px 0}
.legend .sg{color:var(--ink)}
.legend .tl{display:none;gap:6px 12px;flex-wrap:wrap}.tv .legend .tl{display:flex}
.nomark .legend .ml{display:none}
.pick{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 12px}
.pick button{font:inherit;font-size:.88rem;border:2px solid var(--line);background:#fff;border-radius:999px;padding:4px 14px;cursor:pointer;color:inherit}
.pick button.on{border-color:var(--ink);background:var(--ink);color:#fff}
.pick button.dn:not(.on){border-color:var(--ok);color:var(--ok)}
/* textos modelo */
.breakout{width:min(1140px,calc(100vw - 32px));position:relative;left:50%;transform:translateX(-50%)}
.mod{display:none}.mod.on{display:block}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start;margin:12px 0}
.stack .pair{grid-template-columns:1fr;max-width:780px;margin-left:auto;margin-right:auto}
.card{background:#fff;border:2px solid var(--line);border-radius:14px;padding:14px 18px 16px}
.card.apr{border-top:8px solid var(--ok)}.card.exc{border-top:8px solid #2B5FA8}
.pstrip{list-style:none;padding:10px 14px;margin:8px 0 4px;background:#fff;border:1px solid var(--line);border-radius:10px;display:flex;flex-wrap:wrap;gap:4px 18px;font-size:.92rem}
.pstrip li{display:flex;gap:6px;align-items:center}
.pstrip .pn{margin:0}
.lamd summary{font-size:.92rem}
.card header{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.card header h3{margin:0;flex:1}
.bd{font-size:.78rem;font-weight:700;border-radius:999px;padding:2px 10px;color:#fff}
.bd.b2{background:var(--ok)}.bd.b3{background:#2B5FA8}
.txt{font-size:1.02rem;line-height:1.95}
.txt p{margin:0 0 10px}
.stats{list-style:none;padding:8px 0 0;margin:6px 0 0;border-top:1px dashed var(--line);font-size:.86rem;color:var(--muted);display:flex;flex-wrap:wrap;gap:4px 14px}
.stats b{color:var(--ink)}
.why{background:#F6F3EF;border-radius:10px;padding:10px 14px;margin-top:10px}
.why h4{margin:0 0 4px;font-size:.98rem}.why ul{margin:0;padding-left:1.15em;font-size:.93rem}
.cmp table td{font-size:.93rem}.cmp td.pn2{width:34px}
.cmp .pn{margin:0}
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
/* mejoras */
table.mej td{font-size:.94rem}
table.mej td.nm{font-weight:700;white-space:nowrap}
table.mej td.ad{color:var(--muted);font-size:.86rem}
.ba{display:block;padding:2px 8px;border-radius:6px;margin:2px 0}
.ba.x{background:#F6F3EF}.ba.v{background:var(--ok-soft)}
.mcards{display:none}
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
.htxt{background:#FBF9F6;border-radius:10px;padding:12px 14px;line-height:2.3;white-space:pre-wrap}
.htxt select{font:inherit;font-size:.95rem;border:2px solid #CFC6BB;border-radius:8px;padding:2px 6px;background:#fff;max-width:100%}
.htxt select.ok{border-color:var(--ok);background:var(--ok-soft)}.htxt select.mid{border-color:var(--amb);background:var(--amb-soft)}.htxt select.bad{border-color:var(--bad);background:var(--bad-soft)}
ol.hpor{font-size:.92rem;padding-left:1.3em;margin:10px 0 0}
ol.hpor li{margin:3px 0}
.tag{display:inline-block;font-size:.72rem;font-weight:700;border-radius:999px;padding:0 8px;margin-right:6px}
.tag.ok{background:var(--ok);color:#fff}.tag.mid{background:var(--amb);color:#fff}.tag.bad{background:var(--bad);color:#fff}
/* ¿aprueba? */
.stxt{background:#fff;border:1px solid var(--line);border-left:5px solid var(--muted);border-radius:0 10px 10px 0;padding:10px 16px;line-height:1.9}
.stxt p{margin:0 0 8px}
.vbtn{display:block;width:100%;text-align:left;font:inherit;font-weight:600;background:#fff;border:2px solid var(--line);border-radius:10px;padding:9px 14px;margin:6px 0;cursor:pointer;color:inherit}
.vbtn:hover:not(:disabled){border-color:var(--coral)}
.vbtn:disabled{cursor:default}
.vbtn.ok{border-color:var(--ok);background:var(--ok-soft)}.vbtn.bad{border-color:var(--bad);background:var(--bad-soft)}
ul.est{list-style:none;padding:0;margin:10px 0}
ul.est li{display:flex;gap:10px;align-items:flex-start;padding:5px 0;border-bottom:1px dashed var(--line);font-size:.94rem}
ul.est li .st{flex:0 0 auto;font-weight:700;font-size:.82rem;border-radius:999px;padding:1px 10px;margin-top:2px}
ul.est li .st.si{background:var(--ok-soft);color:var(--ok)}ul.est li .st.medias{background:var(--amb-soft);color:#7A4E0E}ul.est li .st.falta{background:var(--bad-soft);color:var(--bad)}
.lec{background:var(--coral-soft);border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
/* ahora tu */
.ahora{background:#FFF8F2;border:2px solid var(--coral);border-radius:14px;padding:16px 18px;margin:14px 0}
.ahora h4{margin:14px 0 6px}
.ahora textarea{width:100%;font:inherit;font-size:1rem;line-height:1.7;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;min-height:210px;background:#fff;resize:vertical}
.ahora select{font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:6px 10px;background:#fff}
.srcs{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.src{text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:10px;padding:8px 12px;cursor:pointer;color:inherit}
.src:hover:not(:disabled){border-color:var(--coral)}
.src:disabled{opacity:.5;cursor:not-allowed}
.src b{display:block}.src small{color:var(--muted)}
.steps3{display:flex;gap:6px;margin:0 0 12px;flex-wrap:wrap}
.steps3 span{font-size:.82rem;font-weight:700;border-radius:999px;padding:2px 12px;background:#fff;border:2px solid var(--line);color:var(--muted)}
.steps3 span.on{border-color:var(--coral);color:var(--ink)}.steps3 span.dn{border-color:var(--ok);color:var(--ok)}
.orig{background:#fff;border:1px solid var(--line);border-left:5px solid var(--ok);border-radius:0 10px 10px 0;padding:10px 14px;white-space:pre-wrap;font-size:.98rem;line-height:1.7}
.orig.ex2{border-left-color:#2B5FA8}
.chk{list-style:none;padding:0;margin:6px 0}
.chk li label{display:flex;gap:8px;align-items:flex-start;padding:5px 0;cursor:pointer}
.chk input{width:19px;height:19px;accent-color:var(--ok);margin-top:4px;flex:0 0 auto}
.chk .mx{font-size:.84rem;color:var(--muted);display:block}
.chk .mx s{color:var(--muted)}
.cnt2{font-size:.9rem;font-weight:600;margin:6px 0}
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
@media (max-width:860px){.pair{grid-template-columns:1fr}.breakout{width:auto;left:0;transform:none}.tools{top:88px}}
@media (max-width:760px){.two,.notes,.srcs{grid-template-columns:1fr}
 table.mej{display:none}.mcards{display:block}}
@media print{header.top,.row,.tools,.noprint,footer.legal{display:none!important}body{background:#fff}section.view{display:none!important}
 section.view.printme{display:block!important;padding-top:0}.breakout{width:auto;left:0;transform:none}.card,.why,.lam{break-inside:avoid}
 .pair{grid-template-columns:1fr 1fr}.mod:not(.on){display:none}}
""" + FT.CSS

# ------------------------------------------------------------ HTML de apoyo
def pauta_t(p): return p["t"] if isinstance(p, dict) else p

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
    o.append('<ul class="pa">' + "".join('<li%s><span class="bn">%d</span>%s</li>' % (' class="p%d"' % (i + 1) if color else "", i + 1, pauta_t(p)) for i, p in enumerate(l["pautas"])) + "</ul>")
    o.append('<div class="pw">Número de palabras recomendadas: entre %d y %d.</div></div>' % (mn, mx))
    return "".join(o)

def inline(txt):
    def rep(m):
        k, w = m.group(1), m.group(2)
        if k == "c": return '<span class="cx">%s</span>' % w
        if k == "T": return '<mark class="mt" title="tú">%s</mark>' % w
        if k == "U": return '<mark class="mu" title="usted">%s</mark>' % w
        return '<span class="vb v-%s" title="%s">%s</span>' % (k, TENSES[k], w)
    return MK.sub(rep, txt)

def seg_html(s, ex=False):
    p, txt = s[0], s[1]
    if not p: return '<span class="firma">%s</span>' % inline(txt)
    mj = "".join('<i class="mj m-%s">%s</i>' % (m, CORTO[m]) for m in (s[2] if ex else []))
    return '<span class="sg p%d"><b class="pn">%d</b>%s%s</span>' % (p, p, inline(txt), mj)

def text_html(t, k):
    return "".join("<p>%s</p>" % " ".join(seg_html(s, k == "ex") for s in par) for par in t[k])

def stats_html(st, np_):
    con = ", ".join(st["con"]) if st["con"] else "ninguno"
    ten = ", ".join(TENSES[x] for x in st["ten"])
    return ('<ul class="stats"><li><b>%s</b> (≈ %d palabras)</li><li><b>%d de %d</b> pautas</li>'
            '<li><b>%d</b> conector%s: %s</li><li><b>%d</b> tiempo%s: %s</li></ul>'
            % (lineas(st["n"]), st["n"], np_, np_, len(st["con"]), "" if len(st["con"]) == 1 else "es", con,
               len(st["ten"]), "" if len(st["ten"]) == 1 else "s", ten))

def cmp_html(t):
    np_ = len(t["lamina"]["pautas"]); rows = []
    for i in range(1, np_ + 1):
        a = " ".join(strip(s[1]) for s in segs_of(t, "ap") if s[0] == i)
        es = [s for s in segs_of(t, "ex") if s[0] == i]
        e = " ".join(strip(s[1]) for s in es)
        mj = "".join('<i class="mj m-%s">%s</i>' % (m, CORTO[m]) for m in dict.fromkeys(m for s in es for m in s[2]))
        rows.append('<tr class="p%d"><td class="pn2"><b class="pn">%d</b></td><td>%s</td><td>%s %s</td></tr>' % (i, i, a, e, mj))
    return ('<details class="cmp"><summary>Pauta por pauta: ¿qué ha cambiado?</summary><table class="t"><thead><tr><th></th><th>Aprobado</th><th>Excelente</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></details>")

# ------------------------------------------------------------ 1. LAS BANDAS
qm = "".join('<div class="box"><h4>%s</h4><span class="wt">%s · %s</span><ul>%s</ul></div>' % (c, p, w, "".join("<li>%s</li>" % x for x in l)) for c, p, w, l in B.QUE_MIRA)
bt = "".join('<tr class="b%d"><td class="b">%d</td><td><b>%s</b></td><td>%s</td><td>%s</td><td class="pt">%s</td></tr>' % (b, b, n, c, u, pt) for b, n, c, u, pt in B.BANDAS)
una = "".join('<div class="box"><h4>%s</h4><p>%s</p></div>' % x for x in B.UNA_FRASE)
def ncard(x):
    def sc(lbl, v): return '<span class="%s">%s<b>%d</b></span>' % ("lo" if v < 2 else "hi" if v > 2 else "", lbl, v)
    return ('<div class="ncard"><h4>%s</h4><div class="q">%s</div><div class="sc">%s%s</div><p>%s</p></div>'
            % (x["n"], x["txt"], sc("Cumplimiento", x["cum"]), sc("Uso de la lengua", x["uso"]), x["nota"]))
V_BANDAS = """
<span class="where">Escritura · Taller de escritura</span>
<h2>Aprobado y excelente: qué mira el corrector</h2>
<p class="lead">No hace falta escribir difícil para aprobar. En esta página vas a ver, con textos de verdad, qué tiene un texto que aprueba y qué cambia en uno excelente, sin salir del A2.</p>
<h3>El corrector te pone dos notas</h3>
<div class="two">""" + qm + """</div>
<div class="tip">Cada tarea de la Escritura tiene estas dos notas, de 0 a 3. Las corrigen dos personas y se hace la media.</div>
<h3>Las bandas, en sencillo</h3>
<table class="t bands"><thead><tr><th>Banda</th><th></th><th>Cumplimiento: ¿qué dices?</th><th>Uso de la lengua: ¿cómo lo dices?</th><th>Puntos</th></tr></thead><tbody>""" + bt + """</tbody></table>
<p class="small muted">Puntos sobre 25 si las dos notas de las dos tareas tienen esa banda. Con un 2 en la Escritura (16,67), en la Lectura te bastan 14 aciertos para llegar a 30 en el grupo.</p>
<h3>En una frase</h3>
<div class="two">""" + una + """</div>
<div class="big">Difícil no es lo mismo que excelente.<small>""" + " ".join(B.DIFICIL) + """</small></div>
<h3>¿Por qué un texto difícil puede no aprobar?</h3>
<p class="small">""" + B.DOS_NOTAS["lamina"] + """</p>
<div class="notes">""" + "".join(ncard(x) for x in B.DOS_NOTAS["textos"]) + """</div>
<div class="note">""" + B.DOS_NOTAS["regla"] + """</div>
<div class="tip"><b>La idea de esta página:</b> """ + B.DOS_NOTAS["moraleja"] + """</div>
<div class="row"><button class="btn cta" data-go="modelos">Siguiente: los textos modelo</button></div>
"""

# ------------------------------------------------------------ 2. LOS TEXTOS MODELO
pick_m = "".join('<button type="button" data-act="mpick" data-t="%s">%s</button>' % (t["id"], t["tab"]) for t in B.TIPOS)
def mod_html(t):
    l = t["lamina"]; np_ = len(l["pautas"])
    return ('<div class="mod" data-mt="%s"><span class="where">%s</span>'
            '<details class="lamd"><summary>Ver la lámina completa</summary>%s</details><ol class="pstrip" aria-label="Las pautas">%s</ol>'
            '<div class="pair">'
            '<article class="card apr"><header><span class="bd b2">Banda 2</span><h3>Aprobado</h3></header><div class="txt">%s</div>%s'
            '<div class="why"><h4>Por qué aprueba</h4><ul>%s</ul></div></article>'
            '<article class="card exc"><header><span class="bd b3">Banda 3</span><h3>Excelente</h3></header><div class="txt">%s</div>%s'
            '<div class="why"><h4>Por qué es excelente</h4><ul>%s</ul></div></article>'
            '</div>%s</div>'
            % (t["id"], t["donde"], lamina_html(l, True), "".join('<li class="p%d"><b class="pn">%d</b>%s</li>' % (i + 1, i + 1, pauta_t(x).rstrip(";.")) for i, x in enumerate(l["pautas"])),
               text_html(t, "ap"), stats_html(STATS[t["id"] + "/ap"], np_), "".join("<li>%s</li>" % x for x in t["por_ap"]),
               text_html(t, "ex"), stats_html(STATS[t["id"] + "/ex"], np_), "".join("<li>%s</li>" % x for x in t["por_ex"]),
               cmp_html(t)))
legend = ('<div class="legend"><span class="ml"><span class="sg p1"><b class="pn">1</b>frase de la pauta 1</span></span>'
          '<span class="ml"><span class="cx">conector</span></span>'
          '<span class="ml"><i class="mj m-det">mejora</i> lo que sube a excelente</span>'
          '<span class="tl">' + "".join('<span class="vb v-%s">%s</span>' % (k, v) for k, v in TENSES.items()) + '</span></div>')
V_MODELOS = """
<span class="where">Cinco tipos de texto</span>
<h2>Los textos modelo</h2>
<p class="lead">Para cada tipo de texto, la misma lámina con dos respuestas: una que aprueba (banda 2) y otra excelente (banda 3). Las dos tienen todas las pautas y más o menos las mismas líneas.</p>
<div class="pick" id="mpick" role="group" aria-label="Elige un tipo de texto">""" + pick_m + """</div>
<div id="mods" class="breakout">
<div class="tools" role="group" aria-label="Cómo ver los textos">
 <span class="seg2" role="group" aria-label="Disposición"><button type="button" data-act="lay" data-v="side" aria-pressed="true">Lado a lado</button><button type="button" data-act="lay" data-v="stack" aria-pressed="false">Uno debajo de otro</button></span>
 <span class="seg2" role="group" aria-label="Marcas"><button type="button" data-act="mk" data-v="1" aria-pressed="true">Con marcas</button><button type="button" data-act="mk" data-v="0" aria-pressed="false">Ver sin marcas</button></span>
 <label><input type="checkbox" id="tvchk"> Colorear los tiempos verbales</label>
</div>
""" + legend + "".join(mod_html(t) for t in B.TIPOS) + """
</div>
<div class="tip">Primero, lee los dos textos <b>sin marcas</b>, como los leería el corrector. Después, con marcas: busca la frase de cada pauta y los cambios.</div>
<div class="row"><button class="btn" data-act="print" data-p="modelos">Imprimir este modelo</button><button class="btn" data-act="mnext">Siguiente tipo de texto</button><button class="btn cta" data-go="mejoras">Siguiente: qué cambia</button></div>
"""

# ------------------------------------------------------------ 3. QUE CAMBIA
mrows = "".join('<tr><td class="nm"><i class="mj m-%s">%s</i><br>%s</td><td>%s</td><td><span class="ba x">%s</span><span class="ba v">%s</span></td><td class="ad">%s</td></tr>'
                % (m["k"], CORTO[m["k"]], m["n"], m["que"], m["antes"], m["despues"], m["ayuda"]) for m in B.MEJORAS)
mcards = "".join('<div class="box" style="margin:8px 0"><h4><i class="mj m-%s">%s</i> %s</h4><p>%s</p><span class="ba x">%s</span><span class="ba v">%s</span><p class="small muted">%s</p></div>'
                 % (m["k"], CORTO[m["k"]], m["n"], m["que"], m["antes"], m["despues"], m["ayuda"]) for m in B.MEJORAS)
V_MEJORAS = """
<span class="where">De la banda 2 a la banda 3</span>
<h2>Qué cambia de aprobado a excelente</h2>
<p class="lead">Seis mejoras pequeñas, todas del A2. No necesitas las seis: con dos o tres en un texto, ya se nota. Cada una tiene su color, el mismo que en los textos modelo.</p>
<table class="t mej"><thead><tr><th>Mejora</th><th>Qué haces</th><th>Antes → después</th><th>A qué nota ayuda</th></tr></thead><tbody>""" + mrows + """</tbody></table>
<div class="mcards">""" + mcards + """</div>
<h3>Lo que no es subir de nivel</h3>
<ul>""" + "".join("<li>%s</li>" % x for x in B.NO_ES) + """</ul>
<div class="tip"><b>En el examen:</b> primero, un texto que aprueba (todas las pautas, el trato, las líneas). Si te sobra tiempo antes de la revisión, cambia dos o tres frases con estas mejoras. Nunca al revés.</div>
<div class="row"><button class="btn" data-act="print" data-p="mejoras">Imprimir la tabla</button><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

# ------------------------------------------------------------ 4. PRACTICA
V_PRACTICA = """
<span class="where">Practica</span>
<h2>¿Aprobado o excelente? Sube un escalón</h2>
<p class="lead">Tres ejercicios: reconocer un texto excelente, elegir la mejora buena y cambiar palabras sencillas por palabras precisas.</p>
<div class="ex" id="ex-clas"></div>
<div class="ex" id="ex-sube"></div>
<div class="ex" id="ex-hue"></div>
<div class="row"><button class="btn cta" data-go="aprueba">Siguiente: ¿aprueba?</button></div>
"""

# ------------------------------------------------------------ 5. ¿APRUEBA?
V_APRUEBA = """
<span class="where">Practica · textos de estudiantes</span>
<h2>¿Aprueba?</h2>
<p class="lead">Seis textos de estudiantes, cada uno con su lámina. Algunos son sencillos y aprueban; otros tienen muy buen español... y algo que los pone en peligro. Léelos con la lámina al lado y decide.</p>
<div class="ex" id="ap"></div>
<div class="row"><button class="btn cta" data-go="ahora">Siguiente: ahora tú</button></div>
"""

# ------------------------------------------------------------ 6. AHORA TU
V_AHORA = """
<span class="where">Ahora tú</span>
<h2>Ahora tú: de aprobado a excelente</h2>
<p class="lead">Elige un texto tuyo: uno que escribiste en el kit de frases, en las pautas o en la revisión final (si lo hiciste en este navegador), o escribe uno nuevo. Primero, comprueba que aprueba. Después, súbelo a excelente con dos o tres mejoras.</p>
<div class="ahora" id="ahora"></div>
<div class="row"><button class="btn cta" data-go="opinion">Siguiente: tu opinión</button></div>
"""

# ------------------------------------------------------------ 7. OPINION
STEPS = [("bandas", "Las bandas"), ("modelos", "Los textos modelo"), ("mejoras", "Qué cambia"), ("practica", "Practica"),
         ("aprueba", "¿Aprueba?"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]
V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo. Al copiar, también se copian tus textos de «Ahora tú» (el aprobado y el excelente) para que tu profesora los vea.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué te ha sorprendido más?</label>
 <div class="chips" role="group" aria-labelledby="o1l">__CHIPS1__</div>
 <label class="q" id="o2l">2. ¿Qué mejora vas a usar primero en el examen?</label>
 <div class="chips" role="group" aria-labelledby="o2l">__CHIPS2__</div>
 <label class="q" id="o3l">3. ¿Te ayuda ver el aprobado y el excelente lado a lado?</label>
 <div class="chips" role="group" aria-labelledby="o3l">__CHIPS3__</div>
 <label class="q" for="o4">4. ¿Qué te cuesta más para subir a excelente? ¿Falta algo o hay algo que no has entendido?</label>
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
V_OPINION = (V_OPINION.replace("__CHIPS1__", chips("o1", ["Que un texto sencillo aprueba", "Que un texto difícil puede no aprobar", "Que el excelente no es más largo", "Que las mejoras son fáciles"]))
             .replace("__CHIPS2__", chips("o2", [m["n"] for m in B.MEJORAS]))
             .replace("__CHIPS3__", chips("o3", ["Sí, mucho", "Un poco", "Prefiero verlos uno debajo de otro"]))
             .replace("__EMAIL__", EMAIL))

views = {"bandas": V_BANDAS, "modelos": V_MODELOS, "mejoras": V_MEJORAS, "practica": V_PRACTICA, "aprueba": V_APRUEBA, "ahora": V_AHORA, "opinion": V_OPINION}
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
def ap_html(a, marked):
    def sg(s):
        p, t = s[0], s[1]
        if not marked: return strip(t)
        return ('<span class="sg p%d"><b class="pn">%d</b>%s</span>' % (p, p, inline(t))) if p else inline(t)
    return "".join("<p>%s</p>" % " ".join(sg(s) for s in par) for par in a["par"])
AP_JS = [{"id": a["id"], "tipo": a["tipo"], "autor": a["autor"], "v": a["v"], "lam": lamina_html(a["lamina"], True),
          "pautas": [pauta_t(p) for p in a["lamina"]["pautas"]], "est": a["est"], "plain": ap_html(a, False), "marked": ap_html(a, True),
          "por": a["por"], "lec": a["leccion"]} for a in B.APRUEBA]
TRATO = {"tu": "TÚ", "usted": "USTED", None: ""}
SRC = []
for t in BF.TIPOS:
    a = t["ahora"]
    SRC.append({"s": "kit", "id": t["id"], "n": "Kit de frases · " + t["tab"], "tarea": a["tarea"], "trato": TRATO[t["trato"]],
                "lam": lamina_html(a), "pautas": [pauta_t(p) for p in a["pautas"]]})
for a in BP.AHORA:
    SRC.append({"s": "pautas", "id": a["id"], "n": "Las pautas · " + a["n"], "tarea": a["lamina"]["tarea"], "trato": TRATO[a["trato"]],
                "lam": lamina_html(a["lamina"]), "pautas": [pauta_t(p) for p in a["lamina"]["pautas"]]})
NEW = [{"id": a["id"], "n": "Nueva · " + a["n"], "tarea": a["lamina"]["tarea"], "trato": TRATO[a["trato"]], "lam": lamina_html(a["lamina"]),
        "pautas": [pauta_t(p) for p in a["lamina"]["pautas"]]} for a in B.AHORA_NUEVAS]
MEJ_JS = [{"k": m["k"], "n": m["n"], "c": CORTO[m["k"]], "que": m["que"], "antes": m["antes"], "despues": m["despues"]} for m in B.MEJORAS]
DATA = {"key": STORAGE, "kitKey": KIT_KEY, "pautasKey": PAUTAS_KEY, "revKey": REV_KEY, "steps": [{"id": k, "label": l} for k, l in STEPS],
        "tipos": [{"id": t["id"], "n": t["tab"]} for t in B.TIPOS],
        "clas": {"t": "¿Aprobado o excelente?", "i": "Frases de estudiantes para una pauta. Todas son correctas: ¿esta respuesta es un aprobado (banda 2) o un excelente (banda 3)?", "ops": B.CLAS_OPS, "items": B.CLAS, "show": 8, "fixed": True},
        "sube": {"t": "Sube un escalón", "i": "Una frase que aprueba y tres versiones. Elige la que la sube a excelente sin salir del A2.", "items": [dict(q, ok=0) for q in B.SUBE], "show": 8, "fixed": False},
        "hue": B.HUECOS, "ap": AP_JS, "ver": B.VEREDICTOS, "src": SRC, "nuevas": NEW, "propio": B.TEXTO_PROPIO_TIPOS,
        "chk": B.CHECK_APROBADO, "mej": MEJ_JS}

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
var MN = {}; D.mej.forEach(function(m){ MN[m.k]=m; });
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function blank(){ return {cur:'bandas', seen:{}, ex:{}, mt:D.tipos[0].id, ms:{}, lay:'side', mk:true, tv:false, ap:{}, apSel:D.ap[0].id, at:null, hist:[], own:{tipo:'', txt:''}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function shuffle(a){ for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function range(n){ var a=[]; for(var i=0;i<n;i++) a.push(i); return a; }
function rec(id, ok, n){ var r=S.ex[id]; if(!r || ok>r.b || (ok===r.b && n!==r.n)) S.ex[id]={b:ok, n:n, l:ok}; else r.l=ok; save(); nav(); }
function para(t){ return esc(t).replace(/\n/g,'<br>'); }

/* ---------------- navegacion ---------------- */
function tabDone(id){
 if(id==='bandas'||id==='mejoras') return !!S.seen[id];
 if(id==='modelos') return D.tipos.every(function(t){ return !!S.ms[t.id]; });
 if(id==='practica') return !!(S.ex.clas && S.ex.sube && S.ex.hue);
 if(id==='aprueba') return D.ap.every(function(a){ return !!S.ap[a.id]; });
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
 if(id==='modelos'){ S.ms[S.mt]=true; save(); }
 if(id==='opinion') summary();
 nav(); window.scrollTo(0,0);
}

/* ---------------- textos modelo ---------------- */
function mShow(t){
 S.mt=t; S.ms[t]=true; save();
 [].forEach.call(document.querySelectorAll('.mod'), function(x){ x.classList.toggle('on', x.getAttribute('data-mt')===t); });
 [].forEach.call(document.querySelectorAll('#mpick button'), function(b){ var k=b.getAttribute('data-t'); b.classList.toggle('on', k===t); b.classList.toggle('dn', !!S.ms[k]); b.setAttribute('aria-pressed', k===t?'true':'false'); });
 nav();
}
function mView(){
 var m=$('mods'); m.classList.toggle('stack', S.lay==='stack'); m.classList.toggle('nomark', !S.mk); m.classList.toggle('tv', !!S.tv && S.mk);
 [].forEach.call(document.querySelectorAll('[data-act="lay"]'), function(b){ b.setAttribute('aria-pressed', b.getAttribute('data-v')===S.lay?'true':'false'); });
 [].forEach.call(document.querySelectorAll('[data-act="mk"]'), function(b){ b.setAttribute('aria-pressed', (b.getAttribute('data-v')==='1')===S.mk?'true':'false'); });
 $('tvchk').checked=!!S.tv; $('tvchk').disabled=!S.mk;
}

/* ---------------- ejercicio q: elegir una opcion (con muestra al azar) ---------------- */
var Q={};
function qNew(id){ var e=D[id], n=e.items.length, idx=shuffle(range(n)).slice(0, Math.min(e.show||n, n));
 Q[id]={k:0, ok:0, ans:false, idx:idx, ord:idx.map(function(i){ var m=(e.items[i].ops||e.ops).length; return e.fixed?range(m):shuffle(range(m)); })}; qRender(id); }
function qRender(id){
 var e=D[id], q=Q[id], box=$('ex-'+id), n=q.idx.length;
 var head='<h4>'+esc(e.t)+'</h4><p class="ei">'+esc(e.i)+'</p>';
 if(q.k>=n){
  rec(id, q.ok, n);
  box.innerHTML=head+'<div class="qn">RESULTADO</div><div class="score">'+q.ok+' / '+n+'</div><p>'+(q.ok===n?'¡Perfecto!':(q.ok>=n-2?'¡Muy bien! Mira otra vez las que has fallado.':'Vuelve a mirar los textos modelo y la tabla de mejoras, y prueba otra vez.'))+'</p>'+
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

/* ---------------- huecos: la que sube / la correcta / el error ---------------- */
var H={ord:[]};
function hRender(){
 var e=D.hue, box=$('ex-hue'); H.ord=e.huecos.map(function(h){ return shuffle(range(h.ops.length)); });
 var txt=esc(e.texto).replace(/\[\[(\d+)\]\]/g, function(_, i){ i=+i;
  return '<select data-h="'+i+'" aria-label="Hueco '+(i+1)+'"><option value="">— '+(i+1)+' —</option>'+H.ord[i].map(function(j){ return '<option value="'+j+'">'+esc(e.huecos[i].ops[j])+'</option>'; }).join('')+'</select>'; });
 box.innerHTML='<h4>'+esc(e.titulo)+'</h4><p class="ei">'+esc(e.intro)+'</p><div class="htxt">'+txt+'</div><div class="hres"></div>'+
  '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="hcheck">Comprobar</button><button class="btn" data-act="hnew">Empezar otra vez</button></div>';
}
function hCheck(){
 var e=D.hue, box=$('ex-hue'), up=0, mid=0, li='';
 [].forEach.call(box.querySelectorAll('select'), function(s){
  var i=+s.getAttribute('data-h'), v=s.value===''?-1:+s.value, h=e.huecos[i], c=v===0?'ok':v===1?'mid':'bad';
  if(v===0) up++; if(v===1) mid++;
  s.classList.remove('ok','mid','bad'); s.classList.add(c); s.disabled=true;
  li+='<li><span class="tag '+c+'">'+(v===0?'Sube':v===1?'Correcta, pero no sube':v<0?'Sin responder':'Error')+'</span><b>'+esc(h.ops[0])+'</b>. '+esc(h.por)+'</li>';
 });
 var n=e.huecos.length;
 box.querySelector('.hres').innerHTML='<div class="fb '+(up===n?'ok':up+mid===n?'mid':'bad')+'"><b>'+up+' de '+n+' suben a excelente.</b>'+(mid?' '+mid+' son correctas, pero no suben: tu texto aprueba igual.':'')+'</div><ol class="hpor">'+li+'</ol>';
 box.querySelector('[data-act="hcheck"]').disabled=true;
 rec('hue', up, n);
}

/* ---------------- ¿aprueba? ---------------- */
function apText(){ var a=D.ap.filter(function(x){ return x.id===S.apSel; })[0]; if(!a){ a=D.ap[0]; S.apSel=a.id; } return a; }
function apRender(){
 var a=apText(), r=S.ap[a.id], box=$('ap');
 var pick='<div class="pick" role="group" aria-label="Elige un texto">'+D.ap.map(function(x,i){ var dn=S.ap[x.id]; return '<button type="button" class="'+(x.id===a.id?'on ':'')+(dn?'dn':'')+'" data-act="appick" data-t="'+x.id+'" aria-pressed="'+(x.id===a.id?'true':'false')+'">'+(i+1)+'. '+esc(x.autor)+(dn?(dn.ok?' ✓':' ✗'):'')+'</button>'; }).join('')+'</div>';
 var o='<h4>Elige un texto</h4>'+pick+'<p class="qn" style="margin:6px 0 0">'+esc(a.tipo).toUpperCase()+' · '+esc(a.autor)+'</p>'+
  '<details open><summary>La lámina</summary>'+a.lam+'</details><h4>El texto de '+esc(a.autor)+'</h4><div class="stxt">'+(r?a.marked:a.plain)+'</div>'+
  '<h4 style="margin-top:14px">¿Aprueba?</h4><div role="group" aria-label="Tu respuesta">'+D.ver.map(function(v,i){
   var c=''; if(r){ if(i===a.v) c=' ok'; else if(i===r.a) c=' bad'; }
   return '<button type="button" class="vbtn'+c+'" data-act="apans" data-i="'+i+'"'+(r?' disabled':'')+'>'+esc(v)+'</button>'; }).join('')+'</div>';
 if(r){
  o+='<div class="fb '+(r.ok?'ok':'bad')+'"><b>'+(r.ok?'¡Bien visto!':'No: '+esc(D.ver[a.v]).toLowerCase()+'.')+'</b> '+esc(a.por)+'</div>'+
   '<ul class="est">'+a.pautas.map(function(p,i){ var e=a.est[i]; return '<li><span class="st '+e+'">'+(e==='si'?'✓ tiene su frase':e==='medias'?'½ a medias':'✗ falta')+'</span><span><b>'+(i+1)+'.</b> '+esc(p)+'</span></li>'; }).join('')+'</ul>'+
   (a.v===2?'<p class="small"><mark class="mt">en naranja</mark>, palabras de tú; <mark class="mu">en azul</mark>, palabras de usted.</p>':'')+
   '<div class="lec"><b>La lección:</b> '+esc(a.lec)+'</div>'+
   '<div class="row" style="margin-bottom:0"><button class="btn" data-act="apagain">Probar otra vez este texto</button>'+(D.ap.some(function(x){ return !S.ap[x.id]; })?'<button class="btn cta" data-act="apnext">Siguiente texto</button>':'')+'</div>';
 }
 var done=D.ap.filter(function(x){ return S.ap[x.id]; }), okn=done.filter(function(x){ return S.ap[x.id].ok; }).length;
 if(done.length) o+='<p class="small muted" style="margin-top:12px">Llevas '+done.length+' de '+D.ap.length+' textos: '+okn+' bien a la primera.</p>';
 box.innerHTML=o;
}
function apAns(b){ var a=apText(); if(S.ap[a.id]) return; var i=+b.getAttribute('data-i'); S.ap[a.id]={a:i, ok:i===a.v}; save(); nav(); apRender(); }

/* ---------------- ahora tu ---------------- */
function other(key){ try{ var r=localStorage.getItem(key); return r?JSON.parse(r):null; }catch(e){ return null; } }
function srcText(s){ var o=other(s.s==='kit'?D.kitKey:D.pautasKey); return (o && o.w && o.w[s.id] && String(o.w[s.id]).trim()) ? String(o.w[s.id]) : ''; }
function revList(){ var o=other(D.revKey); return (o && o.hist && o.hist.length) ? o.hist.filter(function(h){ return h && String(h.rev||'').trim(); }) : []; }
function srcByName(n){ return D.src.filter(function(s){ return s.n===n; })[0] || D.nuevas.filter(function(s){ return s.n===n; })[0] || null; }
function short(t){ return esc(String(t).trim().split(/\s+/).slice(0,9).join(' '))+'...'; }
function stepBar(st){ var L=[['write','Tu texto'],['check','¿Aprueba?'],['up','A excelente'],['done','Hecho']], k=L.map(function(x){ return x[0]; }).indexOf(st);
 return '<div class="steps3">'+L.map(function(x,i){ return '<span class="'+(i===k?'on':i<k?'dn':'')+'">'+(i<k?'✓ ':'')+x[1]+'</span>'; }).join('')+'</div>'; }
function atStart(n, txt, s, write){
 S.at={n:n, tarea:s?s.tarea:0, trato:s?s.trato:'', lam:s?s.lam:'', pautas:s?s.pautas:[], a:txt||'', b:'', chk:{}, mej:{}, step:write?'write':'check'};
 save(); atRender(); $('ahora').scrollIntoView({behavior:'smooth', block:'start'});
}
function chkItems(){
 var v=S.at, L=[];
 if(v.pautas.length) v.pautas.forEach(function(p,i){ L.push(['p'+i, 'Pauta '+(i+1)+': '+p+' — tiene su frase.']); });
 D.chk.forEach(function(c){
  if(c[0]==='pautas' && v.pautas.length) return;
  if(c[0]==='trato' && !(v.trato || v.tarea===1)) return;
  var t=c[1]; if(c[0]==='trato' && v.trato) t='Todo de '+v.trato+', del saludo a la despedida.';
  if(c[0]==='lineas' && v.tarea) t='Las líneas, a ojo: '+(v.tarea===1?'unas 6-7 (tarea 1, 60-70 palabras).':'unas 7-8 (tarea 2, 70-80 palabras).');
  L.push([c[0], t]);
 });
 return L;
}
function atRender(){
 var box=$('ahora'), v=S.at;
 if(!v){
  var kit='', any=false;
  D.src.forEach(function(s,i){ var w=srcText(s); if(w) any=true;
   kit+='<button type="button" class="src" data-act="atsrc" data-i="'+i+'"'+(w?'':' disabled')+'><b>'+esc(s.n)+'</b><small>'+(w?short(w):'Sin texto en este navegador')+'</small></button>'; });
  var rv=revList(), rev=rv.map(function(h,i){ return '<button type="button" class="src" data-act="atrev" data-i="'+i+'"><b>Revisado · '+esc(h.n)+'</b><small>'+short(h.rev)+'</small></button>'; }).join('');
  var nw=D.nuevas.map(function(s,i){ return '<button type="button" class="src" data-act="atnew" data-i="'+i+'"><b>'+esc(s.n)+'</b><small>Tarea '+s.tarea+(s.trato?' · '+s.trato:'')+'</small></button>'; }).join('');
  box.innerHTML='<h4 style="margin-top:0">1. Elige un texto</h4><p class="small">Textos que escribiste en «Ahora tú» del kit de frases y de las pautas'+(any?'':' (en este navegador no hay ninguno todavía)')+':</p><div class="srcs">'+kit+'</div>'+
   (rev?'<h4>Textos que revisaste en «La revisión final»</h4><div class="srcs">'+rev+'</div>':'')+
   '<h4>... o escribe uno nuevo con una de estas láminas</h4><div class="srcs">'+nw+'</div>'+
   '<h4>... o pega otro texto tuyo</h4><p><label>Tipo de texto: <select id="otipo"><option value="">— elige —</option>'+D.propio.map(function(x){ return '<option'+(S.own.tipo===x?' selected':'')+'>'+esc(x)+'</option>'; }).join('')+'</select></label></p>'+
   '<textarea id="otxt" aria-label="Tu texto" placeholder="Pega o escribe aquí tu texto...">'+esc(S.own.txt||'')+'</textarea>'+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="atown">Usar este texto</button></div><div class="saved" id="atmsg" role="status"></div>'+
   (S.hist.length?'<p class="small muted" style="margin-top:14px">Textos mejorados y guardados: '+S.hist.length+'. Se copian en «Tu opinión».</p>':'');
  return;
 }
 var lam=v.lam?'<details'+(v.step==='write'?' open':'')+'><summary>Ver la lámina</summary>'+v.lam+'</details>':'';
 var head=stepBar(v.step)+'<h4 style="margin-top:0">'+esc(v.n)+'</h4>'+lam;
 if(v.step==='write'){
  box.innerHTML=head+'<h4>Escribe tu texto</h4><p class="small">Con frases sencillas y una frase para cada pauta. Cuenta las líneas a ojo: unas 10 palabras por línea.</p>'+
   '<textarea id="ata" aria-label="Tu texto">'+esc(v.a)+'</textarea><div class="saved" id="atsv" role="status"></div>'+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="atgo" data-s="check">He terminado: ¿aprueba?</button><button class="btn" data-act="atreset">Elegir otro texto</button></div><div class="saved" id="atmsg" role="status"></div>';
  return;
 }
 if(v.step==='check'){
  var L=chkItems(), all=L.every(function(x){ return v.chk[x[0]]; });
  box.innerHTML=head+'<h4>Paso 1: ¿tu texto aprueba?</h4><p class="small">Antes de subir de nivel, comprueba que es un texto «aprobado». Marca cada punto solo si es verdad. Si algo falla, arréglalo aquí mismo en tu texto.</p>'+
   '<textarea id="ata" aria-label="Tu texto">'+esc(v.a)+'</textarea><div class="saved" id="atsv" role="status"></div>'+
   '<ul class="chk">'+L.map(function(x){ return '<li><label><input type="checkbox" data-chk="'+x[0]+'"'+(v.chk[x[0]]?' checked':'')+'><span>'+esc(x[1])+'</span></label></li>'; }).join('')+'</ul>'+
   '<div class="fb '+(all?'ok':'mid')+'" id="atchkmsg">'+(all?'<b>Tu texto aprueba.</b> Ahora, a excelente.':'Cuando todo esté marcado, tu texto aprueba. Un texto que no aprueba no sube a excelente: primero, las pautas.')+'</div>'+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="atgo" data-s="up" id="atup"'+(all?'':' disabled')+'>Mi texto aprueba: ahora, a excelente →</button><button class="btn" data-act="atreset">Elegir otro texto</button></div>';
  return;
 }
 if(v.step==='up'){
  if(!v.b) v.b=v.a;
  var nm=Object.keys(v.mej).filter(function(k){ return v.mej[k]; }).length;
  box.innerHTML=head+'<h4>Paso 2: súbelo a excelente</h4><p class="small">Cambia dos o tres frases con las mejoras de la tabla y marca las que has usado. <b>Cambia, no añadas:</b> si escribes una frase nueva, quita otra; el texto tiene que tener más o menos las mismas líneas.</p>'+
   '<div class="two"><div><h4 style="margin-top:0">Tu texto aprobado</h4><div class="orig">'+esc(v.a)+'</div></div>'+
   '<div><h4 style="margin-top:0">Tu texto excelente</h4><textarea id="atb" aria-label="Tu texto excelente">'+esc(v.b)+'</textarea><div class="saved" id="atsv" role="status"></div></div></div>'+
   '<h4>Las mejoras que he usado</h4><ul class="chk">'+D.mej.map(function(m){ return '<li><label><input type="checkbox" data-mej="'+m.k+'"'+(v.mej[m.k]?' checked':'')+'><span><i class="mj m-'+m.k+'">'+esc(m.c)+'</i> <b>'+esc(m.n)+'</b><span class="mx">'+m.antes+' → '+m.despues+'</span></span></label></li>'; }).join('')+'</ul>'+
   '<p class="cnt2" id="atcnt">Has marcado '+nm+(nm===1?' mejora':' mejoras')+'.'+(nm<2?' Marca al menos dos.':'')+'</p>'+
   '<div class="tip">Sin salir del A2: nada de estructuras que no controlas. Y mira que siguen todas las pautas y el mismo trato.</div>'+
   '<div class="row" style="margin-bottom:0"><button class="btn" data-act="atgo" data-s="check">← Volver a la lista</button><button class="btn cta" data-act="atsave">Guardar mi texto excelente</button></div><div class="saved" id="atmsg" role="status"></div>';
  return;
 }
 var used=Object.keys(v.mej).filter(function(k){ return v.mej[k]; });
 box.innerHTML=head+'<div class="fb ok"><b>¡Hecho!</b> Tu texto aprobado y tu texto excelente están guardados: se copian con tu opinión para que tu profesora los vea.</div>'+
  '<div class="two"><div><h4>Aprobado</h4><div class="orig">'+esc(v.a)+'</div></div><div><h4>Excelente</h4><div class="orig ex2">'+esc(v.b)+'</div></div></div>'+
  '<p><b>Mejoras:</b> '+used.map(function(k){ return '<i class="mj m-'+k+'">'+esc(MN[k].c)+'</i>'; }).join(' ')+'</p>'+
  '<ul class="small"><li>¿Siguen todas las pautas, cada una con su frase?</li><li>¿El mismo trato del principio al final?</li><li>¿Más o menos las mismas líneas que el aprobado?</li></ul>'+
  '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="atreset">Mejorar otro texto</button></div>';
}
function atSave(){
 var v=S.at, nm=Object.keys(v.mej).filter(function(k){ return v.mej[k]; });
 if(nm.length<2){ $('atmsg').textContent='Marca al menos dos mejoras que has usado.'; return; }
 if(String(v.b).trim()===String(v.a).trim()){ $('atmsg').textContent='Tu texto excelente es igual que el aprobado: cambia dos o tres frases.'; return; }
 v.step='done';
 S.hist.push({n:v.n, a:v.a, b:v.b, mej:nm, d:new Date().toISOString().slice(0,10)});
 if(S.hist.length>6) S.hist=S.hist.slice(-6);
 save(); nav(); atRender();
}

/* ---------------- opinion ---------------- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o+='<label><input type="radio" name="o5" value="'+i+'"'+(String(S.o5)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o5').innerHTML=o;
 ['o1','o2','o3'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked = r[i].value===S[k]; });
 $('o4').value=S.o4; $('sname').value=S.name;
}
function exLine(id){ var r=S.ex[id]; return r?r.b+'/'+r.n:'sin hacer'; }
function summary(){
 var apn=D.ap.filter(function(a){ return S.ap[a.id]; }).length;
 $('sum').innerHTML='<li>Textos modelo vistos: '+D.tipos.filter(function(t){ return S.ms[t.id]; }).length+' de '+D.tipos.length+'.</li><li>Ejercicios: '+['clas','sube','hue'].filter(function(k){ return S.ex[k]; }).length+' de 3.</li><li>¿Aprueba?: '+apn+' de '+D.ap.length+' textos.</li><li>Textos subidos a excelente en «Ahora tú»: '+S.hist.length+'.</li>';
}
function pack(){
 var L=['CURSO DELE A2 - ESCRITURA: TEXTOS MODELO (APROBADO Y EXCELENTE)', 'Nombre: '+(S.name||'-'), '', 'EJERCICIOS (mejor resultado):',
  '  ¿Aprobado o excelente?: '+exLine('clas'), '  Sube un escalón: '+exLine('sube'), '  Una palabra mejor (huecos que suben): '+exLine('hue'), '', '¿APRUEBA? (primera respuesta):'];
 D.ap.forEach(function(a){ var r=S.ap[a.id]; L.push('  '+a.autor+' ('+a.tipo+'): '+(r?(r.ok?'bien':'mal')+' · respondí «'+D.ver[r.a]+'»'+(r.ok?'':' · era «'+D.ver[a.v]+'»'):'sin hacer')); });
 L.push('', 'MIS TEXTOS ("Ahora tú"):');
 if(!S.hist.length) L.push('  (todavía no he subido ningún texto a excelente)');
 S.hist.forEach(function(h,i){
  L.push('', '== '+(i+1)+'. '+h.n+' ('+h.d+') ==', 'Mejoras que he usado: '+h.mej.map(function(k){ return MN[k]?MN[k].n:k; }).join(' · '), '', 'ANTES (aprobado):', String(h.a).trim(), '', 'DESPUÉS (excelente):', String(h.b).trim());
 });
 L.push('', 'OPINIÓN:', '1. Lo que más me ha sorprendido: '+(S.o1||'-'), '2. La mejora que voy a usar primero: '+(S.o2||'-'), '3. ¿Me ayudan los textos lado a lado?: '+(S.o3||'-'), '4. Lo que me cuesta / falta algo: '+(S.o4||'-'), '5. Sensación de control en la Escritura (1-10): '+(S.o5||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 mpick:function(b){ mShow(b.getAttribute('data-t')); },
 mnext:function(){ var ids=D.tipos.map(function(t){ return t.id; }), i=ids.indexOf(S.mt); mShow(ids[(i+1)%ids.length]); $('mpick').scrollIntoView({behavior:'smooth'}); },
 lay:function(b){ S.lay=b.getAttribute('data-v'); save(); mView(); },
 mk:function(b){ S.mk=b.getAttribute('data-v')==='1'; save(); mView(); },
 qnew:function(b){ qNew(b.getAttribute('data-ex')); },
 qpick:function(b){ qPick(b); },
 qnext:function(b){ var id=b.getAttribute('data-ex'); Q[id].k++; Q[id].ans=false; qRender(id); },
 hcheck:function(){ hCheck(); },
 hnew:function(){ hRender(); },
 appick:function(b){ S.apSel=b.getAttribute('data-t'); save(); apRender(); },
 apans:function(b){ apAns(b); },
 apagain:function(){ delete S.ap[S.apSel]; save(); nav(); apRender(); },
 apnext:function(){ var n=D.ap.filter(function(x){ return !S.ap[x.id]; })[0]; if(n){ S.apSel=n.id; save(); apRender(); $('ap').scrollIntoView({behavior:'smooth'}); } },
 atsrc:function(b){ var s=D.src[+b.getAttribute('data-i')], w=srcText(s); if(w) atStart(s.n, w, s, false); },
 atrev:function(b){ var h=revList()[+b.getAttribute('data-i')]; if(h) atStart('Revisado · '+h.n, String(h.rev), srcByName(h.n), false); },
 atnew:function(b){ var s=D.nuevas[+b.getAttribute('data-i')]; atStart(s.n, '', s, true); },
 atown:function(){ var t=($('otxt').value||'').trim(), tp=$('otipo').value; if(!t){ $('atmsg').textContent='Primero pega o escribe tu texto.'; return; }
  var tarea=(tp.indexOf('Correo')===0)?1:(tp?2:0), trato=tp==='Correo a un amigo'?'TÚ':tp==='Correo de usted'?'USTED':'';
  atStart('Mi texto'+(tp?' · '+tp:''), t, {tarea:tarea, trato:trato, lam:'', pautas:[]}, false); },
 atgo:function(b){ var s=b.getAttribute('data-s'); if(s==='check' && !String(S.at.a).trim()){ $('atmsg').textContent='Primero escribe tu texto.'; return; } S.at.step=s; save(); atRender(); $('ahora').scrollIntoView({behavior:'smooth', block:'start'}); },
 atsave:function(){ atSave(); },
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
 var a=e.target.closest('[data-act]'); if(a && !a.disabled && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
var svT;
function savedMsg(id){ var el=$(id); if(!el) return; el.textContent='✓ Guardado en este navegador'; clearTimeout(svT); svT=setTimeout(function(){ el.textContent=''; },1800); }
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.id==='tvchk'){ S.tv=t.checked; save(); mView(); return; }
 if(t.getAttribute('data-chk')!==null){ S.at.chk[t.getAttribute('data-chk')]=t.checked; save();
  var all=chkItems().every(function(x){ return S.at.chk[x[0]]; }); $('atup').disabled=!all;
  var m=$('atchkmsg'); m.className='fb '+(all?'ok':'mid'); m.innerHTML=all?'<b>Tu texto aprueba.</b> Ahora, a excelente.':'Cuando todo esté marcado, tu texto aprueba. Un texto que no aprueba no sube a excelente: primero, las pautas.'; return; }
 if(t.getAttribute('data-mej')!==null){ S.at.mej[t.getAttribute('data-mej')]=t.checked; save();
  var nm=Object.keys(S.at.mej).filter(function(k){ return S.at.mej[k]; }).length; $('atcnt').textContent='Has marcado '+nm+(nm===1?' mejora':' mejoras')+'.'+(nm<2?' Marca al menos dos.':''); return; }
 if(t.id==='otipo'){ S.own.tipo=t.value; save(); return; }
 if(t.name==='o1'||t.name==='o2'||t.name==='o3'||t.name==='o5'){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){ var t=e.target;
 if(t.id==='ata'){ S.at.a=t.value; save(); savedMsg('atsv'); return; }
 if(t.id==='atb'){ S.at.b=t.value; save(); savedMsg('atsv'); return; }
 if(t.id==='otxt'){ S.own.txt=t.value; save(); return; }
 if(t.id==='o4'){ S.o4=t.value; save(); nav(); } if(t.id==='sname'){ S.name=t.value; save(); } });
window.addEventListener('afterprint', function(){ [].forEach.call(document.querySelectorAll('.printme'), function(v){ v.classList.remove('printme'); }); });

qNew('clas'); qNew('sube'); hRender(); apRender(); atRender(); renderScale();
mShow(D.tipos.some(function(t){ return t.id===S.mt; }) ? S.mt : D.tipos[0].id); mView();
go(D.steps.some(function(s){ return s.id===S.cur; }) ? S.cur : 'bandas');
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_M, body, js))
print("ok", FILE, "· fotos comprobadas:", NFOTOS[0])
for t in B.TIPOS:
    a, e = STATS[t["id"] + "/ap"], STATS[t["id"] + "/ex"]
    print("  %-6s aprobado %d pal. %d con. %d tiempos | excelente %d pal. %d con. %d tiempos | mejoras %s" % (
        t["id"], a["n"], len(a["con"]), len(a["ten"]), e["n"], len(e["con"]), len(e["ten"]),
        ",".join(sorted(set(m for s in segs_of(t, "ex") for m in s[2])))))
print("  ¿Aprueba?:", "; ".join(AST), "· ejercicios: clas %d, sube %d, huecos %d" % (len(B.CLAS), len(B.SUBE), len(B.HUECOS["huecos"])),
      "· fuentes de Ahora tú: %d + %d nuevas" % (len(SRC), len(NEW)))
