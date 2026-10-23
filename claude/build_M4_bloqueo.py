# -*- coding: utf-8 -*-
# MODULO 4 DEL CURSO DE PREPARACION DELE A2 · ORAL: QUE HACER SI ME BLOQUEO
# Uso: python3 build_M4_bloqueo.py
#  -> DELEA2_curso_M4_bloqueo.html  (subir a biblioteca/recursos/A2/dele-curso/)
# Contenido (situaciones, frases, ejercicios, tarjetas del entrenador y laminas de "Ahora tu"): banco_bloqueo_M4.py.
# Para cambiar contenidos, solo se toca ese archivo.
# Mismo estilo y motor que los talleres de la oral (build_M4_T1_temas.py, build_M4_T2_foto.py, build_M4_T3_dialogos.py):
# reloj, grabacion opcional que se queda en el navegador del estudiante, modo concentracion. Novedad: con el
# microfono, el entrenador cuenta los silencios largos (el sonido no sale del navegador y no se analiza con IA).
# La oral no se corrige con IA: la corrige Maria (el estudiante le envia sus grabaciones si quiere).
import json, re
from curso_comun import CSS, EMAIL, page
import banco_bloqueo_M4 as B

TITLE = "Qué hacer si me bloqueo"
FILE = "DELEA2_curso_M4_bloqueo.html"
STORAGE = "dele-a2-curso-M4-bloqueo"
IMG_T2 = "https://2spanishteachers.com/wp-content/uploads/" + B.MES_WP_T2.strip("/") + "/M4T2_foto%d.jpg"

# ------------------------------------------------------------ comprobaciones del banco
W = r"A-Za-zÀ-ÿ"
TU_PAL = re.compile(r"(?i)(?<![%s])(tú|tienes|puedes|quieres|prefieres|piensas|sabes|conoces|entiendes|te|ti|contigo|perdona|mira|oye|dime|déjame|repite|apuntas|vienes)(?![%s])" % (W, W))
US_PAL = re.compile(r"(?i)(?<![%s])(usted|ustedes|perdone|oiga|mire|déjeme|disculpe|puede|quiere|prefiere|desea|sabe|conoce|entiende|le parece|le viene|me recomienda|se le da)(?![%s])" % (W, W))
MARCA = re.compile(r"\{\{(.+?)\}\}")

def limpio(s):
    s = MARCA.sub(r"\1", s)
    return re.sub(r"\([^)]*\)", " ", s)   # las acotaciones (mira la lamina...) no son lo que dice el candidato

def trato_ok(txt, trato, ref):
    t = limpio(txt)
    if trato == "usted":
        m = TU_PAL.search(t); assert not m, "%s: hay tú (%s) en un texto de usted: %s" % (ref, m.group(0), t[:70])
    elif trato == "tu":
        m = US_PAL.search(t); assert not m, "%s: hay usted (%s) en un texto de tú: %s" % (ref, m.group(0), t[:70])
    else:
        m = TU_PAL.search(t) or US_PAL.search(t); assert not m, "%s: un texto para los dos (o de monólogo) no puede llevar tú ni usted (%s): %s" % (ref, m.group(0), t[:70])

ids = [s["id"] for s in B.SITUACIONES]
assert len(ids) == len(set(ids)) == 6, "Tienen que ser seis situaciones con ids distintos"
assert set(B.TARJETA) == set(ids), "La tarjeta imprimible tiene que tener las seis situaciones"
for s in B.SITUACIONES:
    ref = "Situación «%s»" % s["t"]
    f = s["frases"]
    assert len(f["n"]) + len(f["tu"]) + len(f["us"]) >= 4, ref + ": pocas frases"
    for x in f["n"]: trato_ok(x, None, ref + " (frases para los dos)")
    for x in f["tu"]: trato_ok(x, "tu", ref + " (frases de tú)")
    for x in f["us"]: trato_ok(x, "usted", ref + " (frases de usted)")
    assert bool(f["tu"]) == bool(f["us"]), ref + ": si hay frases de tú, tiene que haber de usted (y al revés)"
    assert s["ejemplos"], ref + ": falta el ejemplo"
    for k, e in enumerate(s["ejemplos"]):
        er = "%s, ejemplo %d" % (ref, k + 1)
        assert any(q == "C" and MARCA.search(t) for q, t in e["l"]), er + ": marca la frase de rescate con {{ }}"
        for q, t in e["l"]:
            assert q in ("C", "E")
            if q == "C": trato_ok(t, e["trato"], er + " (candidato)")
            elif e["trato"]: trato_ok(t, e["trato"], er + " (examinador)")
for k, v in B.TARJETA.items():
    for x in v["n"]: trato_ok(x, None, "Tarjeta «%s»" % k)
    if v["tu"]: trato_ok(v["tu"], "tu", "Tarjeta «%s» (tú)" % k)
    if v["us"]: trato_ok(v["us"], "usted", "Tarjeta «%s» (usted)" % k)
for a, b in B.TU_USTED:
    trato_ok(a, "tu", "Tabla tú/usted"); trato_ok(b, "usted", "Tabla tú/usted")
# Ejercicio "¿Que dices?"
for i, q in enumerate(B.QUIZ, 1):
    ref = "¿Qué dices?, pregunta %d" % i
    assert q["s"] in ids and len(q["ops"]) == 3 and 0 <= q["ok"] < 3 and q["por"], ref + ": revisa situación, opciones o explicación"
    trato_ok(q["ops"][q["ok"]], q["trato"], ref + " (respuesta buena)")
    if q.get("e") and q["trato"]: trato_ok(q["e"], q["trato"], ref + " (examinador)")
for s in ids:
    assert sum(1 for q in B.QUIZ if q["s"] == s) >= 2, "¿Qué dices?: la situación «%s» necesita al menos dos preguntas" % s
# Ejercicio "Describe la palabra"
def sin_tilde(s):
    return s.lower().translate(str.maketrans("áéíóúü", "aeiouu"))
for p in B.PALABRAS:
    ref = "Describe la palabra «%s»" % p["w"]
    assert len(p["ops"]) == 3 and 0 <= p["ok"] < 3
    buena = sin_tilde(p["ops"][p["ok"]])
    for r in p["raiz"]:
        assert sin_tilde(r) not in buena, ref + ": la descripción buena dice la palabra (%s)" % r
    tp = B.TIPOS_MALAS[p["w"]]
    assert len(tp) == 3 and tp[p["ok"]] is None and all(tp[j] in B.POR_PALABRA for j in range(3) if j != p["ok"]), ref + ": revisa TIPOS_MALAS"
assert len(B.TIPOS_MALAS) == len(B.PALABRAS)
# Entrenador
for q in B.PREGUNTAS: trato_ok(q["q"], q["trato"], "Pregunta del entrenador")
for q in B.DIFICILES:
    trato_ok(q["q"], q["trato"], "Frase difícil"); trato_ok(q["clar"], q["trato"], "Frase difícil (aclaración)")
    assert q["dif"] in q["q"], "Frase difícil: «%s» no está en la frase" % q["dif"]
for e in B.ERRORES: assert e["mal"] != e["bien"]
for k, v in B.SUCESOS_T3.items():
    for tr in ("tu", "usted"):
        for cita in re.findall(r"«(.+?)»", v[tr]): trato_ok(cita, tr, "Suceso de la tarea 3 «%s»" % k)
# Laminas de las otras piezas
assert len(B.FUENTES_T1) == 20 and all(len(x[3]) == 5 for x in B.FUENTES_T1), "Tarea 1: 20 temas con 5 pautas"
assert len(B.FUENTES_T2) == 12 and all(len(x[3]) >= 5 for x in B.FUENTES_T2) and len(B.PREGUNTAS_FOTO) == 6, "Tarea 2: 12 fotos con sus palabras"
assert len(B.FUENTES_T3) == 12 and all(len(x[5]) == 5 and x[2] in ("tu", "usted") for x in B.FUENTES_T3), "Tarea 3: 12 situaciones con 5 pautas y trato"
for x in B.FUENTES_T3:
    # el candidato habla de tu en las de planificar y de usted en las de servicio: las frases de rescate se eligen por este trato
    assert ("su amigo" in x[3] or "su hermano" in x[3] or "su compañero" in x[3]) == (x[2] == "tu"), "Tarea 3, situación %d: el trato no va con el examinador" % x[0]
# Entrar y terminar (23/10)
assert len(B.DIA_ORAL) >= 6 and all(d["o"] or d["h"] for d in B.DIA_ORAL) and all(d["tu"] for d in B.DIA_ORAL), "El día de la oral: cada paso con lo oficial o lo habitual y el consejo"
fj = [c.get("fijo") for c in B.CONTACTO]
assert fj.count("ini") == fj.count("nom") == fj.count("fin") == 1 and sum(1 for f in fj if not f) >= 4, "Preguntas de contacto: una inicial, una del nombre, una final y al menos cuatro al azar"
for c in B.CONTACTO:
    trato_ok(c["q"], "usted", "Pregunta de contacto"); trato_ok(c["mod"], "usted", "Pregunta de contacto (respuesta modelo)")
    assert c["evita"] and c["por"]
for k in ("T1", "T2"):
    assert len(B.CIERRES[k]) >= 3
    for x in B.CIERRES[k]: trato_ok(x, None, "Fórmula de cierre %s" % k)
trato_ok(B.DESPEDIDA["e"], "usted", "Despedida (examinador)")
for x in B.DESPEDIDA["c"]: trato_ok(x, "usted", "Despedida (candidato)")
for i, q in enumerate(B.ELIGE_CIERRE, 1):
    ref = "Elige el cierre, %d" % i
    assert len(q["ops"]) == 3 and 0 <= q["ok"] < 3 and q["por"] and q["tipo"] in ("cierre", "pronto", "final"), ref
    trato_ok(q["ops"][q["ok"]], q["trato"], ref + " (respuesta buena)")
assert sum(1 for q in B.ELIGE_CIERRE if q["tipo"] == "pronto") >= 2, "Elige el cierre: al menos dos de «todavía no hay que cerrar»"
ID1, ID2 = {x[0] for x in B.FUENTES_T1}, {x[0] for x in B.FUENTES_T2}
for c in B.CIERRA_20:
    ref = "Cierra en 20 segundos (%s %d)" % (c["k"], c["id"])
    assert (c["k"] == "T1" and c["id"] in ID1) or (c["k"] == "T2" and c["id"] in ID2), ref + ": la lámina no existe"
    assert len(c["dicho"]) >= 4 and len(c["mod"]) == 2, ref
    for m in c["mod"]: trato_ok(m, None, ref + " (cierre modelo)")
# Nada de B1 en lo que dice el candidato en lo nuevo (formas frecuentes de subjuntivo y condicional)
B1 = re.compile(r"(?i)(?<![%s])(aunque|quiera|tenga|sea|vaya|haya|pueda|sepa|esté|gustaría que|ojalá|hubiera|habría)(?![%s])" % (W, W))
for t in [c["mod"] for c in B.CONTACTO] + B.CIERRES["T1"] + B.CIERRES["T2"] + B.DESPEDIDA["c"] + \
         [q["ops"][q["ok"]] for q in B.ELIGE_CIERRE] + [m for c in B.CIERRA_20 for m in c["mod"]]:
    m = B1.search(t); assert not m, "Forma de B1 (%s) en: %s" % (m.group(0), t[:70])

# ------------------------------------------------------------ datos para el JS
def mk(s):
    return MARCA.sub(r'<mark class="rs">\1</mark>', s)

SIT_JS = {s["id"]: {"t": s["t"], "n": s["frases"]["n"], "tu": s["frases"]["tu"], "us": s["frases"]["us"]} for s in B.SITUACIONES}
DATA = {
 "key": STORAGE, "keys": {"T1": B.STORAGE_T1, "T2": B.STORAGE_T2, "T3": B.STORAGE_T3},
 "sit": SIT_JS, "ord": B.ORDEN,
 "quiz": B.QUIZ,
 "pw": [{"w": p["w"], "raiz": p["raiz"], "ctx": p["ctx"], "ops": p["ops"], "ok": p["ok"], "tp": B.TIPOS_MALAS[p["w"]]} for p in B.PALABRAS],
 "porw": B.POR_PALABRA, "pistas": B.PISTAS_PALABRA,
 "words": [p["w"] for p in B.PALABRAS] + B.PALABRAS_EXTRA,
 "preg": B.PREGUNTAS, "dif": B.DIFICILES, "err": B.ERRORES, "blanco": B.BLANCO, "tipos": B.TARJETA_TIPOS,
 "t1": [{"id": a, "t": b, "intro": c, "pa": d} for a, b, c, d in B.FUENTES_T1],
 "t2": [{"id": a, "t": b, "alt": c, "pal": d, "img": IMG_T2 % a} for a, b, c, d in B.FUENTES_T2], "pf": B.PREGUNTAS_FOTO,
 "t3": [{"id": a, "t": b, "tr": c, "rol": d, "sit": e, "pa": f} for a, b, c, d, e, f in B.FUENTES_T3],
 "suc3": B.SUCESOS_T3,
 "contacto": B.CONTACTO, "cierres": B.CIERRES, "desp": B.DESPEDIDA, "ec": B.ELIGE_CIERRE,
 "c20": B.CIERRA_20,
}

# ------------------------------------------------------------ CSS
CSS_B = CSS + r"""
:root{--blu:#2B5FA8;--blu-soft:#E4ECF8;--grn:#2F7D4F;--grn-soft:#E3F1E8}
section.view > h3{margin-top:28px}
mark.rs{background:#FFE2D6;color:#7A2A12;border-radius:3px;padding:0 2px;font-weight:600}
.big1{font-family:Georgia,serif;font-size:1.35rem;line-height:1.35;background:#fff;border:2px solid var(--ink);border-radius:14px;padding:14px 18px;margin:14px 0}
.big1 b{color:var(--coral)}
.flow{display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:8px;align-items:center;margin:14px 0}
.flow div{background:#fff;border:2px solid var(--line);border-radius:12px;padding:10px 12px;text-align:center;font-size:.92rem;line-height:1.35}
.flow div b{display:block;font-family:Georgia,serif;font-size:1.05rem}
.flow div.bl{border-color:var(--bad);background:var(--bad-soft)}.flow div.rs{border-color:var(--coral);background:var(--coral-soft)}.flow div.go{border-color:var(--ok);background:var(--ok-soft)}
.flow i{font-style:normal;font-size:1.4rem;color:var(--muted)}
.imp{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.ic{background:#fff;border:1px solid var(--line);border-top:6px solid var(--bad);border-radius:12px;padding:12px 16px}
.ic h4{margin:0 0 6px}
.ic dl{margin:0;font-size:.93rem}
.ic dt{font-size:.72rem;font-weight:700;letter-spacing:.06em;color:var(--muted);text-transform:uppercase;margin-top:6px}
.ic dd{margin:0}
.ic dd.mj{background:var(--ok-soft);border-radius:8px;padding:6px 10px;margin-top:4px}
.okl{list-style:none;padding:0;margin:10px 0}
.okl li{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 14px 8px 44px;margin:6px 0;position:relative;font-size:.95rem}
.okl li:before{content:"\2713";position:absolute;left:14px;top:7px;width:22px;height:22px;border-radius:50%;background:var(--ok);color:#fff;font-weight:700;font-size:.8rem;display:grid;place-items:center}
.okl li b{display:block}
table.esc td:first-child{width:3.2em;text-align:center;font-family:Georgia,serif;font-weight:700;font-size:1.2rem}
table.esc tr.b2 td{background:var(--ok-soft)}
/* situaciones */
.sgrid{display:grid;grid-template-columns:1fr;gap:14px;margin:12px 0}
.sc{background:#fff;border:1px solid var(--line);border-left:8px solid var(--coral);border-radius:12px;padding:14px 18px}
.sc h3{margin:0 0 4px;display:flex;align-items:center;gap:10px}
.sc h3 .ico{display:inline-grid;place-items:center;min-width:34px;height:34px;border-radius:50%;background:var(--coral);color:#fff;font-family:system-ui,sans-serif;font-size:.9rem;padding:0 6px}
.sc .cu{font-size:.88rem;color:var(--muted);margin:0 0 6px}
.fcols{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;font-size:.93rem;margin:8px 0}
.fcols.c1{grid-template-columns:1fr}
.fcols b.h{display:block;font-size:.72rem;letter-spacing:.05em;color:var(--muted);text-transform:uppercase}
.fcols ul{margin:2px 0 0;padding-left:1.1em}
.fcols li{font-style:italic}
.dlg{margin:8px 0}
.dlg .tg{font-size:.74rem;font-weight:700;letter-spacing:.05em;color:var(--muted);text-transform:uppercase;margin-top:8px}
.dl{border-radius:12px;padding:7px 12px;margin:5px 0;max-width:90%;font-size:.95rem;line-height:1.5}
.dl b.who{display:block;font-size:.7rem;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.dl.e{background:#F1EDE8;margin-right:auto}
.dl.c{background:#FFFBF8;border:1px solid var(--coral-soft);margin-left:auto}
.truco{background:var(--amb-soft);border-radius:8px;padding:8px 12px;font-size:.92rem;margin-top:8px}
.ch{display:inline-block;font-size:.74rem;font-weight:700;letter-spacing:.03em;border-radius:999px;padding:1px 9px;margin:0 3px 3px 0;vertical-align:middle;white-space:nowrap;background:#EFEAE4;color:var(--muted)}
.ch.tr{background:var(--ink);color:#fff}.ch.co{background:var(--coral);color:#fff}.ch.ok{background:var(--ok);color:#fff}
/* ejercicios */
.quiz{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin:14px 0}
.quiz .qn{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.quiz .qs{font-size:.98rem;margin:4px 0 6px}
.quiz .qe{font-size:1.08rem;font-family:Georgia,serif;margin:4px 0 10px;background:#F1EDE8;border-radius:10px;padding:8px 12px}
.quiz .qe b{display:block;font-family:system-ui,sans-serif;font-size:.72rem;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.qop{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:10px;padding:9px 14px;margin:6px 0;cursor:pointer;color:inherit}
.qop:hover:not(:disabled){border-color:var(--coral)}
.qop:disabled{cursor:default}
.qop.ok{border-color:var(--ok);background:var(--ok-soft)}
.qop.bad{border-color:var(--bad);background:var(--bad-soft)}
.qop small{display:block;color:var(--muted);font-size:.84rem;margin-top:2px}
.fb{border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
.fb.ok{background:var(--ok-soft)}.fb.bad{background:var(--bad-soft)}
.score{font-family:Georgia,serif;font-size:2.2rem;font-weight:700}
.word{font-family:Georgia,serif;font-size:1.7rem;font-weight:700;background:var(--coral-soft);border:2px dashed var(--coral);border-radius:12px;padding:10px 16px;margin:6px 0 10px;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.word small{font-family:system-ui,sans-serif;font-size:.8rem;font-weight:600;color:#9C3A1E}
.pist{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 4px}
.pist span{background:#F1EDE8;border-radius:999px;padding:2px 10px;font-size:.86rem}
.mine{margin-top:12px;border-top:1px dashed var(--line);padding-top:10px}
.mine textarea,.opn textarea{width:100%;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 10px;min-height:64px;background:#fff}
.warn{background:var(--amb-soft);color:#7A4E0E;border-radius:8px;padding:6px 10px;font-size:.88rem;margin-top:6px}
.warn[hidden]{display:none}
audio{width:100%;margin:6px 0}
/* entrenador */
.opts{background:#fff;border:1px solid var(--line);border-radius:12px;padding:6px 16px;margin:10px 0}
.opts label{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px dashed var(--line)}
.opts label:last-child{border-bottom:0}
.opts input[type=checkbox]{width:20px;height:20px;accent-color:var(--coral);flex:0 0 auto;margin-top:3px}
.opts select{font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:4px 8px;background:#fff;max-width:100%}
.opts small{display:block;color:var(--muted);font-size:.85rem}
.pan{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px}
.pan .kk{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral);display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.card2{border-radius:14px;padding:14px 16px;margin:10px 0;background:var(--coral-soft);border:2px solid var(--coral)}
.card2 .ty{font-size:.75rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#9C3A1E}
.card2 .mn{font-family:Georgia,serif;font-size:1.45rem;line-height:1.35;margin:4px 0}
.card2 .in{font-size:.92rem}
.card2.ev{background:#FFF4E5;border-color:var(--amb)}
.card2.ev .ty{color:#7A4E0E}
.card2.pt{background:#fff;border-color:var(--ink)}
.card2.pt .ty{color:var(--muted)}
.clar{background:var(--ok-soft);border-radius:10px;padding:8px 12px;margin-top:8px;font-size:.95rem}
.clar[hidden]{display:none}
.forms{font-size:.92rem;margin:8px 0;padding:8px 12px;border-left:4px solid var(--amb);background:var(--amb-soft);border-radius:0 8px 8px 0}
.forms div{margin:2px 0}
.myn{white-space:pre-wrap;font-size:.92rem;background:#FFF8F2;border:1px solid var(--coral-soft);border-radius:8px;padding:6px 10px;margin:8px 0}
.myn b{display:block;font-size:.74rem;letter-spacing:.05em;color:var(--coral);white-space:normal}
.clock{font-family:Georgia,serif;font-size:2.6rem;font-weight:700;font-variant-numeric:tabular-nums;line-height:1}
.clock.red{color:var(--bad)}.clock.green{color:var(--ok)}
.bar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;margin:8px 0}
.bar i{display:block;height:100%;background:var(--coral);width:0}
.sil{display:flex;align-items:center;gap:10px;margin:10px 0 2px;font-size:.88rem}
.sil .sb{flex:1;height:14px;background:var(--line);border-radius:99px;overflow:hidden}
.sil .sb i{display:block;height:100%;width:0;background:var(--ok);transition:width .1s}
.sil .sb i.w{background:var(--amb)}.sil .sb i.r{background:var(--bad)}
.alarm{background:var(--bad);color:#fff;border-radius:10px;padding:8px 12px;font-weight:700;margin:6px 0;text-align:center}
.alarm[hidden]{display:none}
.recdot{display:inline-flex;align-items:center;gap:6px;font-size:.85rem;font-weight:600;color:var(--bad)}
.recdot:before{content:"";width:10px;height:10px;border-radius:50%;background:var(--bad);animation:bl 1s infinite}
@keyframes bl{50%{opacity:.25}}
.lvl{display:inline-block;width:60px;height:8px;background:var(--line);border-radius:99px;overflow:hidden;vertical-align:middle}
.lvl i{display:block;height:100%;width:0;background:var(--ok);transition:width .15s}
.cd{font-family:Georgia,serif;font-size:4rem;font-weight:700;text-align:center;color:var(--coral);margin:10px 0}
.res{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 20px;margin:12px 0}
.res .big{font-family:Georgia,serif;font-size:2.4rem;font-weight:700;line-height:1}
.kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:10px 0}
.kpis div{background:var(--paper);border-radius:10px;padding:8px 10px;text-align:center;font-size:.82rem;color:var(--muted)}
.kpis b{display:block;font-family:Georgia,serif;font-size:1.5rem;color:var(--ink)}
.verd{border-radius:10px;padding:10px 14px;font-weight:600;margin:10px 0}
.verd.ok{background:var(--ok-soft);color:var(--ok)}.verd.amb{background:var(--amb-soft);color:#7A4E0E}.verd.bad{background:var(--bad-soft);color:var(--bad)}
.chk{list-style:none;padding:0;margin:8px 0}
.chk li label{display:flex;gap:10px;align-items:flex-start;padding:6px 0;border-bottom:1px dashed var(--line);cursor:pointer}
.chk input{width:20px;height:20px;accent-color:var(--ok);flex:0 0 auto;margin-top:3px}
.chk li label:has(input:checked) > span{color:var(--muted);text-decoration:line-through}
.hist{font-size:.92rem;margin:6px 0}
.warnbox{background:var(--amb-soft);border-radius:10px;padding:12px 14px;margin:10px 0}
.warnbox[hidden]{display:none}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips label{border:2px solid var(--line);border-radius:999px;padding:5px 14px;cursor:pointer;background:#fff}
.chips label:has(input:checked){border-color:var(--ink);background:var(--ink);color:#fff}
.chips input{position:absolute;opacity:0}
/* ahora tu */
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:12px 0}
.card{background:#fff;border:2px solid var(--line);border-radius:12px;cursor:pointer;text-align:left;font:inherit;padding:10px 14px;color:inherit;display:flex;gap:12px;align-items:flex-start}
.card:hover{border-color:var(--coral)}
.card .ci{font-family:Georgia,serif;font-size:1.4rem;font-weight:700;color:var(--coral);line-height:1;min-width:1.4em}
.card b{display:block;font-size:.98rem;line-height:1.3}
.card span.s{font-size:.82rem;color:var(--muted)}
.card.pr{border-color:var(--ok)}
h3.grp{margin:22px 0 2px}
.lam{background:#fff;border:2px solid var(--ink);border-radius:6px;padding:12px 16px;margin:10px 0;font-size:.95rem}
.lam .lh{font-size:.76rem;letter-spacing:.06em;color:var(--muted);text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:6px;margin-bottom:8px;display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
.lam h3{margin:0 0 6px;font-size:1.05rem}
.lam p{margin:4px 0 6px}
.lam ul{margin:0;padding-left:0;list-style:none}
.lam li{padding:5px 0 5px 30px;position:relative;border-bottom:1px dashed var(--line)}
.lam li:last-child{border-bottom:0}
.lam li .bn{position:absolute;left:0;top:6px;width:22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:.78rem;font-weight:700;display:grid;place-items:center}
.lam li.cur{background:var(--coral-soft);border-radius:6px;margin:0 -6px;padding-left:36px;padding-right:6px}
.lam li.cur .bn{background:var(--coral);left:6px}
.lam li.done{color:var(--muted)}.lam li.done .bn{background:var(--ok)}
.lam .ins{font-size:.76rem;font-weight:700;letter-spacing:.08em;color:var(--muted);margin-top:8px}
.ph{position:relative;background:#EFEAE4;border-radius:6px;overflow:hidden;margin:6px 0 8px;aspect-ratio:3/2}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.ph .alt{position:absolute;inset:0;display:none;align-items:center;justify-content:center;text-align:center;padding:14px;font-size:.92rem;color:var(--muted)}
.ph.no img{display:none}.ph.no .alt{display:flex}
.run{display:grid;grid-template-columns:1fr 1.05fr;gap:16px;align-items:start;margin-top:8px}
.run .side{position:sticky;top:120px}
.run.one{grid-template-columns:1fr}
/* opinion */
.scale{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.scale label{cursor:pointer}
.scale input{position:absolute;opacity:0}
.scale span{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;border:2px solid var(--line);background:#fff;font-weight:700}
.scale input:checked + span{background:var(--ink);border-color:var(--ink);color:#fff}
.scale input:focus-visible + span{outline:3px solid var(--cta);outline-offset:2px}
.opn label.q{display:block;font-weight:600;margin:18px 0 6px}
.sendbox{border:2px solid var(--coral);border-radius:12px;padding:18px 22px;margin:26px 0;background:#fff}
.sendbox input[type=text]{width:100%;max-width:360px;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 12px;margin-top:6px}
/* tarjeta imprimible */
#sheet{display:none}
.tj{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.tj div{border:2px solid var(--ink);border-radius:10px;padding:8px 10px;break-inside:avoid}
.tj h4{margin:0 0 4px;font-size:1rem}
.tj p{margin:2px 0;font-size:.95rem}
.tj p.tu{color:#1E4A87}.tj p.us{color:#7A4E0E}
/* entrar y terminar */
.ch.of{background:var(--blu);color:#fff}.ch.hb{background:var(--amb);color:#fff}
.tl{list-style:none;padding:0;margin:14px 0;position:relative}
.tl:before{content:"";position:absolute;left:17px;top:6px;bottom:6px;width:3px;background:var(--line)}
.tl > li{position:relative;padding:0 0 14px 52px}
.tl .tn{position:absolute;left:0;top:0;width:37px;height:37px;border-radius:50%;background:var(--ink);color:#fff;font-family:Georgia,serif;font-weight:700;display:grid;place-items:center}
.tl .tb{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 16px}
.tl h4{margin:4px 0 6px}
.tl ul{margin:4px 0;padding-left:0;list-style:none;font-size:.94rem}
.tl ul li{padding:3px 0 3px 0}
.tl ul.of li:before{content:"OFICIAL";font-size:.66rem;font-weight:700;letter-spacing:.05em;background:var(--blu);color:#fff;border-radius:999px;padding:1px 7px;margin-right:7px;vertical-align:1px}
.tl ul.hb li:before{content:"HABITUAL";font-size:.66rem;font-weight:700;letter-spacing:.05em;background:var(--amb);color:#fff;border-radius:999px;padding:1px 7px;margin-right:7px;vertical-align:1px}
.tl .tu{background:var(--ok-soft);border-radius:8px;padding:6px 10px;font-size:.93rem;margin-top:6px}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:.9rem;margin:8px 0}
.part{border-top:3px solid var(--coral);margin-top:34px;padding-top:6px}
.part > .pn{font-size:.78rem;font-weight:700;letter-spacing:.08em;color:var(--coral)}
.f2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0}
.f2 > div{background:#fff;border:1px solid var(--line);border-top:5px solid var(--ok);border-radius:12px;padding:10px 16px}
.f2 ul{margin:4px 0 0;padding-left:1.1em}.f2 li{font-style:italic}
.nol{list-style:none;padding:0;margin:8px 0}
.nol li{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 14px 8px 44px;margin:6px 0;position:relative;font-size:.94rem}
.nol li:before{content:"\2715";position:absolute;left:14px;top:8px;width:22px;height:22px;border-radius:50%;background:var(--bad);color:#fff;font-weight:700;font-size:.75rem;display:grid;place-items:center}
.nol li b{display:block}
table.mods td:first-child{width:34%}
table.mods td i{color:var(--muted)}
.dch{list-style:none;padding:0;margin:6px 0;font-size:1rem;font-family:system-ui,sans-serif}
.dch li{padding:3px 0 3px 26px;position:relative}
.dch li:before{content:"\2713";position:absolute;left:4px;color:var(--ok);font-weight:700}
.oc{background:var(--ink);color:#fff;border:0;border-radius:14px;padding:16px 20px;width:100%;text-align:left;font:inherit;cursor:pointer;margin:12px 0}
.oc b{font-family:Georgia,serif;font-size:1.25rem;display:block}
.oc span{font-size:.92rem;opacity:.85}
.oc:hover{background:#2A2D36}
.prep{font-family:Georgia,serif;font-size:3rem;font-weight:700;font-variant-numeric:tabular-nums}
.prep.red{color:var(--bad)}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;align-items:start}
.g3 textarea{width:100%;font:inherit;font-size:.92rem;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 10px;min-height:120px;background:#fff}
.g3 .lam{font-size:.86rem}
@media (max-width:900px){.g3{grid-template-columns:1fr}}
@media (max-width:760px){.f2{grid-template-columns:1fr}}
/* modo concentracion */
body.wide .wrap,body.wide .top-in{max-width:1180px}
body.focus header.top{display:none}
body.focus section.view{padding-top:12px}
body.focus .run .side{top:12px}
@media (max-width:900px){.run{grid-template-columns:1fr}.run .side{position:static}
 body.focus .run .side{position:sticky;top:0;z-index:6;background:var(--paper);padding:6px 0 8px}
 body.focus .run .side .lam{max-height:32vh;overflow:auto;margin:0}
 body.focus .clock{font-size:2rem}}
@media (max-width:760px){.imp,.grid,.fcols{grid-template-columns:1fr}.flow{grid-template-columns:1fr}.flow i{transform:rotate(90deg);text-align:center}.kpis{grid-template-columns:1fr 1fr 1fr}.dl{max-width:98%}}
@media print{header.top,.row,.noprint,footer.legal,.quizbox{display:none!important}body{background:#fff}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}
 body.ps main,body.ps header{display:none!important}body.ps #sheet{display:block;padding:0 4mm}
 #sheet h2{font-size:15pt;margin:0 0 2mm}.sc,.ic,.lam{break-inside:avoid}details{border:0}details>*{display:block}}
"""

# ------------------------------------------------------------ VISTAS
STEPS = [("entrar", "Entrar y terminar"), ("importa", "Por qué importa"), ("frases", "Las frases"), ("dices", "¿Qué dices?"), ("palabra", "Describe la palabra"),
         ("entrena", "Entrenador"), ("ahora", "Ahora tú"), ("opinion", "Tu opinión")]

def ic(x):
    return ('<div class="ic"><h4>%s</h4><dl><dt>Qué ve el examinador</dt><dd>%s</dd><dt>En la nota</dt><dd>%s</dd>'
            '<dt>Mejor así</dt><dd class="mj">%s</dd></dl></div>' % (x["t"], x["ve"], x["nota"], x["mejor"]))

ESCALA = [("3", "Habla con cierta seguridad. Puede hacer alguna pausa, pero no molesta: se le entiende sin esfuerzo."),
          ("2", "Comete errores y hace alguna pausa. A veces necesita alguna ayuda del examinador. Es el A2: <b>aprueba</b>."),
          ("1", "Hace pausas o errores todo el tiempo. Necesita ayuda: que le repitan, que le pregunten otra vez."),
          ("0", "Silencios largos y frecuentes, palabras sueltas o de otras lenguas. No siempre se le entiende.")]

def paso(d):
    return ('<li><span class="tn">%s</span><div class="tb"><h4>%s</h4>%s%s<div class="tu"><b>Tú:</b> %s</div></div></li>'
            % (d["ico"], d["t"], '<ul class="of">%s</ul>' % "".join("<li>%s</li>" % x for x in d["o"]) if d["o"] else "",
               '<ul class="hb">%s</ul>' % "".join("<li>%s</li>" % x for x in d["h"]) if d["h"] else "", d["tu"]))

def fila_contacto(c):
    return ('<tr><td>«%s»%s</td><td><b>%s</b><br><span class="small"><i>Mejor no:</i> %s<br>%s</span></td></tr>'
            % (c["q"], ' <span class="ch hb">habitual</span>' if c["h"] else "", c["mod"], c["evita"], c["por"]))

V_ENTRAR = """
<h2>Entrar y terminar</h2>
<p class="lead">Muchos bloqueos llegan al principio, cuando entras en la sala, o al final de una tarea, cuando no sabes cómo terminar. Aquí ves cómo es el día de la oral, practicas las primeras preguntas y aprendes a cerrar sin cortar de golpe.</p>
<div class="legend"><span><span class="ch of">OFICIAL</span> lo dice la Guía del examen</span><span><span class="ch hb">HABITUAL</span> suele pasar así, pero no está escrito: puede cambiar un poco</span></div>

<div class="part"><div class="pn">1 · EL DÍA DE LA ORAL</div><h3>Paso a paso</h3>
<ol class="tl">""" + "".join(paso(d) for d in B.DIA_ORAL) + """</ol></div>

<div class="part" id="p-entrada"><div class="pn">2 · LA ENTRADA</div><h3>Simulador de las preguntas de contacto</h3>
<p>Las preguntas de contacto no se evalúan, pero son el momento de los nervios. Si las practicas, entras en la tarea 1 tranquilo. La regla: <b>una frase completa y un detalle pequeño</b>. Ni una palabra sola, ni un discurso.</p>
<div id="en"></div>
<details><summary>Todas las preguntas y las respuestas modelo</summary><p class="small muted">Las respuestas son de Anna, una candidata. Tú contesta con tus datos.</p>
<table class="t mods"><thead><tr><th>El examinador</th><th>Respuesta modelo</th></tr></thead><tbody>""" + "".join(fila_contacto(c) for c in B.CONTACTO) + """</tbody></table></details>
</div>

<div class="part" id="p-cierre"><div class="pn">3 · TERMINAR BIEN</div><h3>Cómo cerrar la tarea 1 y la tarea 2</h3>
<p>En la tarea 1 y en la tarea 2 hablas tú solo, y el examinador no sabe cuándo has terminado si no se lo dices. Un buen cierre es <b>una fórmula y una frase final</b>: tu opinión, un resumen o lo que van a hacer después. Cierra cuando has hablado de todas las pautas y llevas unos dos minutos o más.</p>
<div class="f2"><div><h4>Tarea 1 · el monólogo</h4><ul>""" + "".join("<li>%s</li>" % x for x in B.CIERRES["T1"]) + """</ul></div>
<div><h4>Tarea 2 · la foto</h4><ul>""" + "".join("<li>%s</li>" % x for x in B.CIERRES["T2"]) + """</ul></div></div>
<h4>Así no</h4><ul class="nol">""" + "".join("<li><b>%s</b>%s</li>" % x for x in B.CIERRES_MAL) + """</ul>
<div class="note"><b>Y al final de la oral:</b> el examinador dice algo como «""" + B.DESPEDIDA["e"] + """» <span class="ch hb">habitual</span>. Tú: <i>«""" + "» o «".join(B.DESPEDIDA["c"]) + """»</i>. Deja las notas en la mesa.</div>
<h3>Elige el cierre</h3>
<p class="small muted">Diez momentos del final de una tarea. Cuidado: a veces todavía no es el momento de cerrar.</p>
<div id="ec"></div>
<h3>Te quedan 20 segundos: cierra</h3>
<p>Ves lo que ya has dicho de un tema o de una foto. Tienes 20 segundos para cerrar en voz alta. Después escuchas tu cierre y lo comparas con dos cierres modelo.</p>
<div id="ci"></div>
</div>
<div class="row"><button class="btn cta" data-go="importa">Siguiente: por qué importa no quedarse callado</button></div>
"""

V_IMPORTA = """
<h2>Por qué importa no quedarse callado</h2>
<p class="lead">En la oral te van a pasar cosas: no te sale una palabra, no entiendes una pregunta, te quedas en blanco. Es normal y les pasa a todos. Lo que decide la nota es <b>lo que haces después</b>.</p>
<div class="big1">En la oral, quedarse callado es <b>lo peor que puede pasar</b>. Y siempre hay algo que decir, aunque no sepas una palabra o no entiendas al examinador.</div>
<div class="flow" aria-hidden="true"><div class="bl"><b>Me bloqueo</b>no sé, no entiendo, me quedo en blanco</div><i>→</i><div class="rs"><b>Frase de rescate</b>«Pues...», «¿Puede repetir?», «Es una cosa que...»</div><i>→</i><div class="go"><b>Sigo hablando</b>contesto, añado algo, sigo con la pauta</div></div>

<h3>Lo que pasa en la nota</h3>
<p>En la oral hay dos notas: el <b>uso de la lengua</b> (cómo hablas) y el <b>cumplimiento de la tarea</b> (si dices todo lo que pide la lámina). El examinador que habla contigo pone una nota a toda la prueba y el otro, que solo escucha, pone una nota a cada tarea. Esto es lo que ven cuando te bloqueas:</p>
<div class="imp">""" + "".join(ic(x) for x in B.IMPORTA) + """</div>

<h3>Las pausas y la ayuda en la escala oficial</h3>
<p class="small muted">Las bandas del uso de la lengua (de 0 a 3), explicadas en sencillo. La banda 2 es el A2: con 2 apruebas.</p>
<table class="t esc"><thead><tr><th>Banda</th><th>Qué dice la escala sobre las pausas y la ayuda</th></tr></thead><tbody>""" + \
 "".join('<tr class="%s"><td>%s</td><td>%s</td></tr>' % ("b2" if b == "2" else "", b, d) for b, d in ESCALA) + """</tbody></table>
<p class="small muted">Fuente: Guía del examen DELE A2, escalas de la Expresión e interacción orales (resumen nuestro).</p>

<h3>Lo que sí puedes hacer sin miedo</h3>
<ul class="okl">""" + "".join("<li><b>%s</b>%s</li>" % x for x in B.SE_PUEDE) + """</ul>

<h3>Qué valora el examinador cuando te bloqueas y sigues</h3>
<ul class="okl">
 <li><b>Que el mensaje llega.</b> Si no sabes «paraguas» y dices «una cosa para no mojarse cuando llueve», el examinador te entiende: eso es dejar claro lo que quieres decir.</li>
 <li><b>Que respondes a todas las pautas.</b> Un bloqueo de dos segundos no se nota. Una pauta sin respuesta, sí.</li>
 <li><b>Que la conversación sigue.</b> En la tarea 3, si preguntas y propones, el examinador no tiene que hacer todo el trabajo.</li>
</ul>
<div class="tip"><b>La regla de los cinco segundos.</b> Nunca más de cinco segundos callado. Si no sabes qué decir, di una frase de rescate: te da tiempo y el examinador ve que sigues comunicando. En el entrenador de esta página puedes practicarlo con el micrófono: cuenta tus silencios.</div>
<div class="row"><button class="btn cta" data-go="frases">Siguiente: las frases</button></div>
"""

def cols(f):
    if not f["tu"]:
        return '<div class="fcols c1"><div><b class="h">Sirven siempre</b><ul>%s</ul></div></div>' % "".join("<li>%s</li>" % x for x in f["n"])
    return ('<div class="fcols"><div><b class="h">Sirven siempre</b><ul>%s</ul></div><div><b class="h">Con un amigo (tú)</b><ul>%s</ul></div>'
            '<div><b class="h">Examinador, tienda (usted)</b><ul>%s</ul></div></div>'
            % ("".join("<li>%s</li>" % x for x in f["n"]), "".join("<li>%s</li>" % x for x in f["tu"]), "".join("<li>%s</li>" % x for x in f["us"])))

def ejemplo(e):
    tr = {"tu": " · tú", "usted": " · usted", None: ""}[e["trato"]]
    o = ['<div class="tg">%s%s</div>' % (e["tarea"], tr)]
    for q, t in e["l"]:
        o.append('<div class="dl %s"><b class="who">%s</b>%s</div>' % ("e" if q == "E" else "c", "Examinador" if q == "E" else "Candidato", mk(t)))
    return "".join(o)

def sc(s):
    return ('<div class="sc" id="s-%s"><h3><span class="ico" aria-hidden="true">%s</span>%s</h3><p class="cu">%s</p><p>%s</p>%s'
            '<div class="dlg">%s</div><div class="truco"><b>Truco:</b> %s</div></div>'
            % (s["id"], s["ico"], s["t"], s["cuando"], s["que"], cols(s["frases"]), "".join(ejemplo(e) for e in s["ejemplos"]), s["truco"]))

V_FRASES = """
<h2>Seis situaciones de bloqueo y sus frases</h2>
<p class="lead">Para cada situación, unas frases de rescate y un ejemplo corto. En la tarea 3 hay situaciones con un amigo (tú) y en una tienda o una oficina (usted); en las tareas 1 y 2, el examinador suele hablarte de usted. Por eso algunas frases van en dos columnas. En los ejemplos, la frase de rescate va <mark class="rs">en color</mark>.</p>
<div class="sgrid">""" + "".join(sc(s) for s in B.SITUACIONES) + """</div>
<h3>Tú o usted en las frases de rescate</h3>
<table class="t"><thead><tr><th>Con un amigo, tu hermano, un compañero</th><th>Con el examinador en las tareas 1 y 2, en una tienda, en una oficina</th></tr></thead><tbody>""" + \
 "".join("<tr><td><i>%s</i></td><td><i>%s</i></td></tr>" % x for x in B.TU_USTED) + """</tbody></table>
<div class="tip"><b>Tu tarjeta de rescate.</b> Imprímela y tenla delante cuando practiques en casa. En el examen no puedes llevarla, pero si la usas cada día, las frases salen solas.</div>
<div class="row"><button class="btn cta" data-act="print" data-p="sheet">Imprimir la tarjeta de rescate</button><button class="btn" data-act="print" data-p="frases">Imprimir esta página</button><button class="btn" data-go="dices">Siguiente: ¿qué dices?</button></div>
"""

V_DICES = """
<h2>¿Qué dices?</h2>
<p class="lead">Ocho situaciones de bloqueo del examen. Elige la mejor respuesta y mira por qué. Fíjate también en el trato: tú o usted.</p>
<div id="quiz"></div>
"""
V_PALABRA = """
<h2>Describe la palabra</h2>
<p class="lead">Imagina que no te sale la palabra. Elige la mejor forma de explicarla y, si quieres, escribe o graba tu propia descripción. Para describir una palabra, hazte estas preguntas:</p>
<div class="pist">""" + "".join("<span>%s</span>" % x for x in B.PISTAS_PALABRA) + """</div>
<div id="pw"></div>
"""
V_ENTRENA = '<div id="tr"></div>'
V_AHORA = '<div id="at"></div>'

CUESTA = ["No sé una palabra", "No entiendo al examinador", "Me quedo en blanco", "No sé qué contestar", "Me pongo nervioso y hablo muy deprisa"]
V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿Qué te pasa más cuando te bloqueas?</label>
 <div class="chips" role="group" aria-labelledby="o1l">__CHIPS__</div>
 <label class="q" id="o3l">2. ¿El entrenador te ha ayudado a no quedarte callado?</label>
 <div class="chips" role="group" aria-labelledby="o3l">
  <label><input type="radio" name="o3" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o3" value="Un poco">Un poco</label>
  <label><input type="radio" name="o3" value="No">No</label>
  <label><input type="radio" name="o3" value="No lo he probado">No lo he probado</label>
 </div>
 <label class="q" for="o5">3. ¿Qué frase de rescate vas a usar primero en el examen?</label>
 <textarea id="o5"></textarea>
 <label class="q" for="o2">4. ¿Qué falta en esta página, o qué no has entendido?</label>
 <textarea id="o2"></textarea>
 <label class="q" id="o4l">5. Ahora, si te bloqueas en la oral, ¿cuánto control sientes? (1 = nada, 10 = total)</label>
 <div class="scale" role="group" aria-labelledby="o4l" id="o4"></div>
 <label class="q" id="o6l">6. ¿Te ha ayudado saber cómo es el día de la oral y practicar la entrada y los cierres?</label>
 <div class="chips" role="group" aria-labelledby="o6l">
  <label><input type="radio" name="o6" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o6" value="Un poco">Un poco</label>
  <label><input type="radio" name="o6" value="No">No</label>
  <label><input type="radio" name="o6" value="No lo he mirado">No lo he mirado</label>
 </div>
</div>
<div class="sendbox">
 <h3>Envía tus resultados y tu opinión a tu profesora</h3>
 <label><b>Tu nombre</b><br><input type="text" id="sname" autocomplete="name"></label>
 <div class="row"><button class="btn cta" data-act="copy">Copiar</button></div>
 <div class="copied-box" id="cbox" role="status" hidden></div>
 <p class="muted small">Pégalo en un correo para tu profesora: __EMAIL__. Se copian tus prácticas de la entrada y de los cierres, los resultados de los ejercicios, tus descripciones, tus tiempos y silencios del entrenador y de «Ahora tú», y tus respuestas. Las grabaciones no se copian: si quieres que tu profesora te escuche, guarda el audio y envíalo tú.</p>
</div>
""".replace("__CHIPS__", "".join('<label><input type="radio" name="o1" value="%s">%s</label>' % (x, x) for x in CUESTA)).replace("__EMAIL__", EMAIL)

def tarjeta():
    o = []
    for s in B.SITUACIONES:
        v = B.TARJETA[s["id"]]
        o.append('<div><h4>%s</h4>%s%s%s</div>' % (s["t"], "".join("<p>%s</p>" % x for x in v["n"]),
                 '<p class="tu"><b>Tú:</b> %s</p>' % v["tu"] if v["tu"] else "", '<p class="us"><b>Usted:</b> %s</p>' % v["us"] if v["us"] else ""))
    return '<div class="tj">' + "".join(o) + "</div>"

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Oral · Las tres tareas</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
<div id="sheet"><h2>Mi tarjeta de rescate · Oral DELE A2</h2><p style="margin:0 0 3mm">Nunca más de cinco segundos callado. Respondo + añado + pregunto.</p>__TARJETA__<p style="margin:3mm 0 0"><b>Para cerrar.</b> Tarea 1: «Y eso es todo sobre...», «Para terminar, creo que...». Tarea 2: «En resumen, en la foto veo...», «Y eso es lo que veo en la foto». Al final: «Gracias a ustedes. Hasta luego».</p></div>
"""
views = {"entrar": V_ENTRAR, "importa": V_IMPORTA, "frases": V_FRASES, "dices": V_DICES, "palabra": V_PALABRA, "entrena": V_ENTRENA, "ahora": V_AHORA, "opinion": V_OPINION}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
body = BODY.replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML).replace("__TARJETA__", tarjeta())
DATA["steps"] = [{"id": k, "label": l} for k, l in STEPS]

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function shuffle(a){ for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function pick(a){ return a[Math.floor(Math.random()*a.length)]; }
function mmss(s){ s=Math.max(0,Math.round(s)); return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2); }
function sec1(s){ return (Math.round(s*10)/10).toFixed(1).replace('.',','); }
function today(){ return new Date().toISOString().slice(0,10); }
function fdate(d){ return d.split('-').reverse().join('/'); }
function blank(){ return {cur:'entrar', seen:{}, qz:{best:null,last:null}, pw:{best:null,last:null,mine:{}}, ec:{best:null,last:null},
 en:{n:5, d:20, lim:5, mic:true, rec:false, voz:false}, enh:[], cih:[], ci:null,
 oc:{t1:null, t2:null, t3:null, dur:'n', n:3, lim:5, prep:true, mic:true, rec:false, beep:true, voz:false, notes:{T1:'',T2:'',T3:''}}, o6:'',
 o:{dur:120, every:20, lim:5, mode:'mix', trato:'ambos', mic:true, rec:false, beep:true},
 ao:{n:3, lim:5, mic:true, rec:false, beep:true, notas:true, dur:{T1:150,T2:150,T3:210}}, trh:[], ath:[], sel:null,
 o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } ['o','ao','pw','ec','en','oc'].forEach(function(g){ for(var j in b[g]){ if(!(j in o[g])) o[g][j]=b[g][j]; } }); return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function other(k){ try{ var r=localStorage.getItem(D.keys[k]); return r ? JSON.parse(r) : null; }catch(e){ return null; } }

/* ---------------- navegacion ---------------- */
function tabDone(id){
 if(id==='entrar') return !!S.seen.entrar || S.enh.length>0 || S.ec.best!==null || S.cih.length>0;
 if(id==='dices') return S.qz.best!==null;
 if(id==='palabra') return S.pw.best!==null;
 if(id==='entrena') return S.trh.length>0;
 if(id==='ahora') return S.ath.length>0;
 if(id==='opinion') return !!(S.o1||S.o2||S.o3||S.o4||S.o5||S.o6);
 return !!S.seen[id];
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
 if(R.active) stopRun(true); prepStop();
 S.seen[S.cur]=true; S.cur=id; save();
 var vs=document.querySelectorAll('section.view');
 for(var i=0;i<vs.length;i++) vs[i].classList.toggle('on', vs[i].id==='v-'+id);
 document.body.classList.toggle('wide', id==='ahora');
 if(id==='entrar'){ renderEn(); renderCi(); }
 if(id==='entrena') showTrSetup();
 if(id==='ahora') showAtPick();
 nav(); window.scrollTo(0,0);
}

/* ---------------- frases de rescate ---------------- */
function frases(sid, trato, nmax){
 var s=D.sit[sid]; if(!s) return [];
 var o=s.n.slice(0, nmax||3);
 var nt=(sid==='pensar')?1:2; if(trato==='tu') o=o.concat(s.tu.slice(0,nt)); else if(trato==='usted') o=o.concat(s.us.slice(0,nt));
 return o;
}
function formsBox(list, lab){ return '<div class="forms"><b>'+(lab||'Frases de rescate')+':</b> <i>'+list.map(esc).join(' · ')+'</i></div>'; }
function trName(t){ return t==='tu'?'tú':(t==='usted'?'usted':''); }

/* ---------------- ejercicio 1: que dices ---------------- */
var QZ=null;
function newQuiz(){
 var by={}; D.quiz.forEach(function(q,i){ (by[q.s]=by[q.s]||[]).push(i); });
 var sel=[]; D.ord.forEach(function(s){ if(by[s]) sel.push(pick(by[s])); });
 var rest=shuffle(D.quiz.map(function(q,i){ return i; }).filter(function(i){ return sel.indexOf(i)<0; }));
 sel=shuffle(sel.concat(rest.slice(0, Math.max(0, 8-sel.length))));
 QZ={items:sel.map(function(i){ return {q:D.quiz[i], ord:shuffle([0,1,2])}; }), k:0, ok:0, done:false, fails:[]};
 renderQuiz();
}
function renderQuiz(){
 var q=QZ, box=$('quiz');
 if(q.k>=q.items.length){
  var n=q.items.length, ok=q.ok;
  if(S.qz.best===null || ok>S.qz.best) S.qz.best=ok; S.qz.last=ok; save(); nav();
  var fl={}; q.fails.forEach(function(s){ fl[s]=1; });
  box.innerHTML='<div class="quiz"><div class="qn">RESULTADO</div><div class="score">'+ok+' / '+n+'</div><p>'+(ok>=7?'¡Muy bien! Sabes qué decir cuando te bloqueas.':(ok>=5?'Bien. Repasa las frases de las situaciones donde has fallado.':'Vuelve a mirar las seis situaciones y prueba otra vez.'))+'</p>'+
   (Object.keys(fl).length?'<p class="small">Repasa: '+Object.keys(fl).map(function(s){ return '<a href="#s-'+s+'" data-go="frases">'+esc(D.sit[s].t)+'</a>'; }).join(' · ')+'</p>':'')+
   '<p class="small muted">Tu mejor resultado: '+S.qz.best+' / '+n+'</p><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="qnew">Otras ocho situaciones</button><button class="btn" data-go="palabra">Siguiente: describe la palabra</button></div></div>';
  return;
 }
 var it=q.items[q.k], Q=it.q;
 var o='<div class="quiz"><div class="qn">SITUACIÓN '+(q.k+1)+' DE '+q.items.length+'</div><div><span class="ch co">'+esc(D.sit[Q.s].t)+'</span><span class="ch">'+esc(Q.tarea)+'</span>'+(Q.trato?'<span class="ch tr">'+(Q.trato==='tu'?'TÚ':'USTED')+'</span>':'')+'</div>'+
  '<p class="qs">'+esc(Q.sit)+'</p>'+(Q.e?'<div class="qe"><b>El examinador</b>«'+esc(Q.e)+'»</div>':'')+'<div role="group" aria-label="Respuestas">';
 it.ord.forEach(function(i){ o+='<button type="button" class="qop" data-act="qpick" data-i="'+i+'">'+esc(Q.ops[i])+'</button>'; });
 o+='</div><div id="qfb"></div><div class="row" style="margin-bottom:0" id="qnext" hidden><button class="btn cta" data-act="qnext">'+(q.k===q.items.length-1?'Ver el resultado':'Siguiente situación')+'</button></div></div>';
 box.innerHTML=o;
}
function pickQuiz(b){
 var q=QZ, it=q.items[q.k]; if(q.done) return;
 var i=+b.getAttribute('data-i'), ok=i===it.q.ok;
 if(ok) q.ok++; else q.fails.push(it.q.s); q.done=true;
 [].forEach.call(document.querySelectorAll('#quiz .qop'), function(x){ x.disabled=true; var j=+x.getAttribute('data-i'); if(j===it.q.ok) x.classList.add('ok'); else if(j===i) x.classList.add('bad'); });
 $('qfb').innerHTML='<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Muy bien!':'Mejor la otra respuesta.')+'</b> '+esc(it.q.por)+'</div>'+formsBox(frases(it.q.s, it.q.trato, 2));
 $('qnext').hidden=false;
}

/* ---------------- ejercicio 2: describe la palabra ---------------- */
var PW=null, PWREC={};
function newPw(){ PW={items:shuffle(D.pw.slice()).slice(0,8).map(function(p){ return {p:p, ord:shuffle([0,1,2])}; }), k:0, ok:0, done:false, res:[]}; renderPw(); }
function sinTilde(s){ return String(s).toLowerCase().replace(/[áà]/g,'a').replace(/[éè]/g,'e').replace(/[íì]/g,'i').replace(/[óò]/g,'o').replace(/[úùü]/g,'u'); }
function saysWord(p, txt){ var t=sinTilde(txt); return p.raiz.some(function(r){ return t.indexOf(sinTilde(r))>=0; }); }
function renderPw(){
 var q=PW, box=$('pw');
 if(q.k>=q.items.length){
  var n=q.items.length, ok=q.ok;
  if(S.pw.best===null || ok>S.pw.best) S.pw.best=ok; S.pw.last=ok; save(); nav();
  var mine=q.items.filter(function(it){ return (S.pw.mine[it.p.w]||'').trim(); });
  box.innerHTML='<div class="quiz"><div class="qn">RESULTADO</div><div class="score">'+ok+' / '+n+'</div><p>'+(ok>=7?'¡Muy bien! Sabes explicar una palabra que no te sale.':'Recuerda: para qué sirve, cómo es, dónde está, a qué se parece.')+'</p>'+
   (mine.length?'<h4>Tus descripciones</h4><ul>'+mine.map(function(it){ return '<li><b>'+esc(it.p.w)+':</b> '+esc(S.pw.mine[it.p.w])+'</li>'; }).join('')+'</ul><p class="small muted">Se copian con el botón Copiar de «Tu opinión», para que tu profesora las vea.</p>':'')+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="pwnew">Otras ocho palabras</button><button class="btn" data-go="entrena">Siguiente: el entrenador</button></div></div>';
  return;
 }
 var it=q.items[q.k], p=it.p;
 var o='<div class="quiz"><div class="qn">PALABRA '+(q.k+1)+' DE '+q.items.length+'</div><p class="qs">'+esc(p.ctx)+'</p>'+
  '<div class="word"><span>'+esc(p.w)+'</span><small>No te sale esta palabra</small></div><p class="small muted" style="margin:0 0 4px">¿Cuál es la mejor forma de explicarla?</p><div role="group" aria-label="Descripciones">';
 it.ord.forEach(function(i){ o+='<button type="button" class="qop" data-act="pwpick" data-i="'+i+'">'+esc(p.ops[i])+'</button>'; });
 o+='</div><div id="pwfb"></div>';
 o+='<div class="mine" id="pwmine" hidden><b>Ahora tú (si quieres):</b> explícala con tus palabras, sin decirla. Escríbela o grábate.'+
  '<textarea id="pwtxt" data-w="'+esc(p.w)+'" placeholder="Es una cosa que sirve para...">'+esc(S.pw.mine[p.w]||'')+'</textarea><div class="warn" id="pwwarn" hidden>¡Has dicho la palabra! Explícala sin decirla.</div>'+
  '<div class="row" style="margin:8px 0"><button class="btn sm" data-act="pwrec" data-w="'+esc(p.w)+'" id="pwrecb">● Grabar mi descripción</button></div><div id="pwaud">'+(PWREC[p.w]?'<audio controls src="'+PWREC[p.w]+'"></audio>':'')+'</div></div>';
 o+='<div class="row" style="margin-bottom:0" id="pwnext" hidden><button class="btn cta" data-act="pwnext">'+(q.k===q.items.length-1?'Ver el resultado':'Siguiente palabra')+'</button></div></div>';
 box.innerHTML=o;
}
function pickPw(b){
 var q=PW, it=q.items[q.k], p=it.p; if(q.done) return;
 var i=+b.getAttribute('data-i'), ok=i===p.ok;
 if(ok) q.ok++; q.done=true;
 [].forEach.call(document.querySelectorAll('#pw .qop'), function(x){ x.disabled=true; var j=+x.getAttribute('data-i'); if(j===p.ok) x.classList.add('ok'); else if(j===i) x.classList.add('bad'); var t=p.tp[j]; if(t) x.innerHTML+='<small>'+esc(D.porw[t])+'</small>'; });
 $('pwfb').innerHTML='<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Muy bien!':'Mejor la otra.')+'</b> La buena dice para qué sirve o cómo es, y el examinador sabe enseguida de qué hablas.</div>';
 $('pwmine').hidden=false; $('pwnext').hidden=false;
}
/* grabacion corta de una descripcion */
var MREC={mr:null, st:null, w:null};
function recType(){
 if(!window.MediaRecorder || !MediaRecorder.isTypeSupported) return '';
 var ts=['audio/mp4','audio/webm;codecs=opus','audio/webm','audio/ogg'];
 for(var i=0;i<ts.length;i++) if(MediaRecorder.isTypeSupported(ts[i])) return ts[i];
 return '';
}
function pwRec(b){
 var w=b.getAttribute('data-w');
 if(MREC.mr){ try{ MREC.mr.stop(); }catch(e){} return; }
 if(!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia || !window.MediaRecorder){ $('pwaud').innerHTML='<div class="warnbox">Este navegador no puede grabar. Escribe tu descripción.</div>'; return; }
 navigator.mediaDevices.getUserMedia({audio:true}).then(function(st){
  var t=recType(), ch=[], mr; try{ mr=t?new MediaRecorder(st,{mimeType:t}):new MediaRecorder(st); }catch(e){ st.getTracks().forEach(function(k){ k.stop(); }); return; }
  MREC={mr:mr, st:st, w:w};
  mr.ondataavailable=function(e){ if(e.data && e.data.size) ch.push(e.data); };
  mr.onstop=function(){ st.getTracks().forEach(function(k){ k.stop(); }); MREC={mr:null, st:null, w:null};
   if(ch.length){ if(PWREC[w]) try{ URL.revokeObjectURL(PWREC[w]); }catch(e){} PWREC[w]=URL.createObjectURL(new Blob(ch,{type:mr.mimeType||t||'audio/webm'})); }
   var a=$('pwaud'); if(a) a.innerHTML=PWREC[w]?'<audio controls src="'+PWREC[w]+'"></audio>':'<div class="warnbox">No se ha grabado nada. Prueba otra vez.</div>';
   var bb=$('pwrecb'); if(bb) bb.textContent='● Grabar otra vez'; };
  mr.start(); b.textContent='■ Parar la grabación';
 }, function(){ $('pwaud').innerHTML='<div class="warnbox">No hay permiso para usar el micrófono. Escribe tu descripción.</div>'; });
}

/* ---------------- sonido, pantalla, microfono ---------------- */
var AC=null, WL=null;
function beep(f){
 if(!AC) return;
 try{ var t=AC.currentTime, os=AC.createOscillator(), g=AC.createGain(); os.type='sine'; os.frequency.value=f||660;
  g.gain.setValueAtTime(0.0001,t); g.gain.exponentialRampToValueAtTime(0.25,t+0.02); g.gain.exponentialRampToValueAtTime(0.0001,t+0.3);
  os.connect(g); g.connect(AC.destination); os.start(t); os.stop(t+0.35); }catch(e){}
}
function wake(on){ try{ if(on && navigator.wakeLock){ navigator.wakeLock.request('screen').then(function(w){ WL=w; }, function(){}); } else if(!on && WL){ WL.release(); WL=null; } }catch(e){} }
var MIC={stream:null, mr:null, url:null, ext:'webm', err:'', used:false, an:null, buf:null, src:null, g:null, max:0, thr:0.08};
function micClear(){ if(MIC.url){ try{ URL.revokeObjectURL(MIC.url); }catch(e){} } MIC.url=null; }
function micPrepare(useMic, done){
 MIC.err=''; MIC.used=useMic; micClear();
 if(MIC.stream){ try{ MIC.stream.getTracks().forEach(function(k){ k.stop(); }); }catch(e){} MIC.stream=null; }
 if(!useMic){ done(); return; }
 if(!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia){ MIC.err='Este navegador no puede usar el micrófono: practicas sin contar silencios.'; done(); return; }
 navigator.mediaDevices.getUserMedia({audio:true}).then(function(st){ MIC.stream=st; lvStart(); done(); }, function(){ MIC.err='No hay permiso para usar el micrófono: practicas sin contar silencios y sin grabación.'; done(); });
}
function lvStart(){ try{ if(!AC||!MIC.stream) return; MIC.src=AC.createMediaStreamSource(MIC.stream); MIC.an=AC.createAnalyser(); MIC.an.fftSize=1024; MIC.buf=new Uint8Array(MIC.an.fftSize);
 MIC.g=AC.createGain(); MIC.g.gain.value=0; MIC.src.connect(MIC.an); MIC.an.connect(MIC.g); MIC.g.connect(AC.destination); MIC.max=0; }catch(e){ MIC.an=null; } }
function lvRead(){ if(!MIC.an) return -1; try{ MIC.an.getByteTimeDomainData(MIC.buf); }catch(e){ return -1; } var m=0; for(var i=0;i<MIC.buf.length;i++){ var v=Math.abs(MIC.buf[i]-128); if(v>m) m=v; } if(m>MIC.max) MIC.max=m; return m/128; }
function recStart(){
 if(!MIC.stream || MIC.mr || !R.rec) return;
 var st=MIC.stream, t=recType(), mr, ch=[];
 MIC.ext = t.indexOf('mp4')>=0 ? 'm4a' : (t.indexOf('ogg')>=0 ? 'ogg' : 'webm');
 if(!window.MediaRecorder){ MIC.err='Este navegador no puede grabar.'; return; }
 try{ mr = t ? new MediaRecorder(st,{mimeType:t}) : new MediaRecorder(st); }catch(e){ MIC.err='No se ha podido empezar a grabar.'; return; }
 MIC.mr=mr;
 mr.ondataavailable=function(e){ if(e.data && e.data.size) ch.push(e.data); };
 mr.onstop=function(){ if(MIC.mr!==mr) return; MIC.mr=null;
  if(ch.length){ MIC.url=URL.createObjectURL(new Blob(ch,{type:mr.mimeType||t||'audio/webm'})); }
  else MIC.err='No se ha grabado nada esta vez. Vuelve a cargar la página y prueba otra vez (Chrome o Safari).';
  var a=$('recout'); if(a) a.innerHTML=recBlock(); };
 try{ mr.start(); }catch(e){ MIC.mr=null; MIC.err='No se ha podido empezar a grabar.'; }
}
function micStop(){
 try{ if(MIC.src) MIC.src.disconnect(); if(MIC.g) MIC.g.disconnect(); }catch(e){} MIC.an=null; MIC.src=null; MIC.g=null;
 if(MIC.mr && MIC.mr.state!=='inactive'){ try{ MIC.mr.stop(); }catch(e){ MIC.mr=null; } }
 var st=MIC.stream; MIC.stream=null;
 setTimeout(function(){ if(st){ try{ st.getTracks().forEach(function(k){ k.stop(); }); }catch(e){} } }, 300);
}
function recBlock(){
 if(MIC.url) return '<h4>Escúchate</h4><audio controls src="'+MIC.url+'"></audio><div class="row" style="margin:6px 0"><a class="btn sm" href="'+MIC.url+'" download="mi_practica_bloqueo.'+MIC.ext+'">Guardar el audio en mi dispositivo</a><button class="btn sm" data-act="delrec">Borrar la grabación</button></div>'+
  '<p class="small muted">La grabación está solo en esta página: se borra al cerrarla. Al escucharte, fíjate: ¿dónde te has quedado callado? ¿Qué frase de rescate has usado? ¿Repites siempre la misma («pues, pues...»)?</p>';
 if(MIC.mr) return '<p class="small muted">Preparando la grabación...</p>';
 if(MIC.err) return '<div class="warnbox">'+MIC.err+'</div>';
 return '';
}

/* ---------------- motor de practica (entrenador y ahora tu) ---------------- */
var R={active:false};
function now(){ return (window.performance&&performance.now)?performance.now():Date.now(); }
function elapsed(){ return R.acc + (R.paused?0:(now()-R.t0)/1000); }
function totalEl(){ return R.done + elapsed(); }
function startRun(cfg){
 initAC();
 R={active:false, kind:cfg.kind, segs:cfg.segs, lim:cfg.lim, rec:cfg.rec, beepOn:cfg.beep, src:cfg.src||null, i:0, acc:0, t0:0, paused:false, done:0,
    gap:0, last:0, inGap:false, count:0, longest:0, voiced:0, calib:true, cal:0, noMic:false, warned:false, tPrev:0, side:cfg.side||null,
    label:cfg.label||'', after:cfg.after||null, chk:cfg.chk||null, voz:!!cfg.voz};
 var box=cfg.box; R.box=box;
 box.innerHTML='<p class="muted">Un momento...</p>';
 micPrepare(cfg.mic, function(){
  R.active=true; wake(true); document.body.classList.add('focus');
  box.innerHTML='<div class="run'+(R.side?'':' one')+'">'+(R.side?'<div class="side" id="side"></div>':'')+'<div><div class="pan" id="pan" aria-live="polite"></div>'+
   '<div class="warnbox" id="micw" hidden><b>No llega sonido del micrófono.</b> Revisa el permiso del navegador y que no está silenciado. Sigue practicando: cuenta tú tus silencios.</div>'+
   '<div class="row"><button class="btn" data-act="pause" id="bpause">Pausa</button><button class="btn" data-act="stop">Parar</button></div></div></div>';
  if(MIC.an){ R.micOn=true; R.calib=true; R.cal=0; R.t0=now(); renderCalib(); }
  else { R.calib=false; R.noMic=true; enterSeg(0); }
  R.timer=setInterval(tick, 100);
 });
}
function renderCalib(){
 $('pan').innerHTML='<div class="kk">PREPARADOS</div><h3>No hables: mido el ruido de tu habitación</h3><div class="cd" id="cd">3</div><p class="small muted">Así el entrenador sabe cuándo hablas y cuándo estás callado. El sonido no sale de tu ordenador o de tu móvil.</p>';
}
function enterSeg(n){
 R.i=n; R.acc=0; R.t0=now(); R.paused=false; R.evShown=false; R.clarShown=false;
 var sg=R.segs[n];
 if(n===0){ recStart(); R.last=now(); R.gap=0; } else if(R.beepOn) beep(sg.ev?520:660);
 if(sg.skip||sg.quiet){ R.last=now(); R.inGap=false; }
 if(R.voz && sg.say) say(sg.say);
 renderSeg(); if(R.side) renderSide();
}
function say(t){ try{ if(!window.speechSynthesis || !window.SpeechSynthesisUtterance) return; var u=new SpeechSynthesisUtterance(t); u.lang='es-ES'; u.rate=0.95;
 var vs=speechSynthesis.getVoices(), v=null; for(var i=0;i<vs.length;i++){ if(/^es[-_]ES/i.test(vs[i].lang)){ v=vs[i]; break; } } if(!v) for(var j=0;j<vs.length;j++){ if(/^es/i.test(vs[j].lang)){ v=vs[j]; break; } }
 if(v) u.voice=v; speechSynthesis.cancel(); speechSynthesis.speak(u); }catch(e){} }
function hush(){ try{ if(window.speechSynthesis) speechSynthesis.cancel(); }catch(e){} }
function renderSide(){ var s=R.segs[R.i]; $('side').innerHTML=R.side(s.cur, s); var c=document.querySelector('#side li.cur'), l=c&&c.closest('.lam'); if(l && l.scrollHeight>l.clientHeight) l.scrollTop=Math.max(0,c.offsetTop-60); }
function segCard(c, cls){
 return '<div class="card2 '+(cls||'')+'"><div class="ty">'+esc(c.ty)+'</div><div class="mn">'+c.mn+'</div>'+(c.ins?'<div class="in">'+esc(c.ins)+'</div>':'')+
  (c.clar?'<div class="clar" id="clar'+(cls==='ev'?'e':'')+'" hidden><b>El examinador lo dice de otra forma:</b> «'+esc(c.clar)+'»</div>':'')+'</div>'+(c.ph&&c.ph.length?formsBox(c.ph, c.phl):'');
}
function renderSeg(){
 var s=R.segs[R.i], n=R.segs.length;
 var recd=(MIC.mr?' <span class="recdot">Grabando</span>':'')+(MIC.an?' <span class="lvl" title="Nivel del micrófono"><i id="lvl"></i></span>':'');
 var o='<div class="kk"><span>'+esc(s.head||'')+' · '+(R.i+1)+' DE '+n+'</span>'+recd+'</div><div style="display:flex;align-items:baseline;justify-content:space-between;gap:10px;flex-wrap:wrap"><div class="clock" id="clk"></div><span class="small muted" id="tot"></span></div><div class="bar"><i id="br"></i></div>';
 o+=segCard(s.card, s.kind==='pauta'?'pt':'');
 if(s.nota) o+='<div class="myn"><b>TUS NOTAS</b>'+esc(s.nota)+'</div>';
 if(s.ev) o+='<div id="evbox"></div>';
 if(s.skip) o+='<div class="row" style="margin:8px 0"><button class="btn cta sm" data-act="next">'+esc(s.skipl||'Siguiente →')+'</button></div>';
 if(s.quiet) o+='<p class="small muted">Ahora habla el examinador: escucha.</p>';
 else if(MIC.an && !R.noMic) o+='<div class="sil"><span>Silencio</span><span class="sb"><i id="silb"></i></span><b id="silt">0,0 s</b></div><div class="alarm" id="alarm" hidden>¡Habla! «Pues...», «A ver...», «Bueno, ahora...»</div>';
 else o+='<p class="small muted">Sin micrófono: fíjate tú en tus silencios. Nunca más de '+R.lim+' segundos callado.</p>';
 $('pan').innerHTML=o;
}
function tick(){
 if(!R.active || R.paused) return;
 var t=now(), lv=lvRead(), lb=$('lvl');
 if(lb && lv>=0) lb.style.width=Math.min(100, Math.round(Math.sqrt(lv)*160))+'%';
 if(R.calib){
  var e=(t-R.t0)/1000; if(lv>R.cal) R.cal=lv;
  var cd=$('cd'); if(cd) cd.textContent=Math.max(1, 3-Math.floor(e));
  if(e>=3){ R.calib=false; MIC.thr=Math.min(0.35, Math.max(0.06, R.cal*1.8+0.03)); MIC.max=0; R.tStart=t; enterSeg(0); }
  return;
 }
 var dt=R.tPrev ? Math.min(0.5,(t-R.tPrev)/1000) : 0; R.tPrev=t;
 if(R.segs[R.i].quiet){ R.last=t; R.inGap=false; }
 if(lv>=0 && !R.noMic){
  if(!R.warned && t-R.tStart>10000){ R.warned=true; if(MIC.max<2){ R.noMic=true; var mw=$('micw'); if(mw) mw.hidden=false; renderSeg(); } }
  if(lv>MIC.thr){ if(R.inGap){ R.inGap=false; } R.last=t; R.voiced+=dt; }
  R.gap=(t-R.last)/1000; if(R.gap>R.longest) R.longest=R.gap;
  if(R.gap>R.lim && !R.inGap){ R.inGap=true; R.count++; beep(330); }
  var sb=$('silb'), st=$('silt'), al=$('alarm');
  if(sb){ sb.style.width=Math.min(100, R.gap/R.lim*100)+'%'; sb.className=R.gap>R.lim?'r':(R.gap>R.lim*0.6?'w':''); }
  if(st) st.textContent=sec1(R.gap)+' s';
  if(al) al.hidden=!R.inGap;
 }
 var s=R.segs[R.i], e2=elapsed(), rem=s.d-e2, clk=$('clk');
 if(clk){ clk.textContent=mmss(Math.ceil(rem)); clk.className='clock'+(rem<=4?' red':''); }
 var br=$('br'); if(br) br.style.width=Math.min(100,e2/s.d*100)+'%';
 var tot=$('tot'); if(tot) tot.textContent='Total: '+mmss(totalEl())+' de '+mmss(R.total);
 if(s.card.clar && !R.clarShown && e2>=s.d*0.4){ R.clarShown=true; var c=$('clar'); if(c) c.hidden=false; }
 if(s.ev && !R.evShown && e2>=s.d*s.ev.at){ R.evShown=true; var eb=$('evbox'); if(eb){ eb.innerHTML=segCard(s.ev,'ev'); if(s.ev.clar) setTimeout(function(){ var c2=$('clare'); if(c2) c2.hidden=false; }, Math.max(2000,(s.d*(1-s.ev.at))*400)); } if(R.beepOn) beep(520); }
 if(rem<=0){ R.done+=s.d; if(R.i<R.segs.length-1) enterSeg(R.i+1); else finishRun(); }
}
function togglePause(){
 if(!R.active || R.calib) return;
 if(R.paused){ R.paused=false; R.t0=now(); R.last=now(); R.tPrev=0; } else { R.acc=elapsed(); R.paused=true; }
 var b=$('bpause'); if(b) b.textContent=R.paused?'Seguir':'Pausa';
}
function stopRun(silent){
 document.body.classList.remove('focus'); hush();
 if(R.timer) clearInterval(R.timer); R.timer=null; var was=R.active; R.active=false; wake(false); micStop();
 if(!silent && was){ if(R.kind==='tr') showTrSetup(); else if(R.kind==='at') showAtSetup(); else if(R.kind==='oc') showOcSetup(); else if(R.kind==='en') renderEn(); else renderCi(); }
}
function finishRun(){
 var secs=R.done;
 document.body.classList.remove('focus');
 if(R.timer) clearInterval(R.timer); R.timer=null; R.active=false; wake(false); micStop(); hush(); if(R.beepOn) beep(880);
 var heard=!!(R.micOn && !R.noMic);
 var res={d:today(), s:Math.round(secs), n:R.segs.length, ev:R.segs.filter(function(x){ return x.ev; }).length, mic:heard, sil:heard?R.count:null, lg:heard?Math.round(R.longest*10)/10:null, vo:heard?Math.round(R.voiced):null, self:null};
 if(R.kind==='tr') res.mode=S.o.mode;
 if(R.src){ res.src=R.src.k; res.id=R.src.id; res.t=R.src.t; }
 var hk=HK[R.kind]; S[hk].push(res); S[hk]=S[hk].slice(-12);
 save(); nav(); showDone(res);
}
function showDone(res){
 var v, cl;
 if(res.mic){
  if(res.sil===0){ cl='ok'; v='¡Perfecto! Ni un silencio de más de '+R.lim+' segundos.'; }
  else if(res.sil<=2){ cl='amb'; v='Bien. '+res.sil+' silencio'+(res.sil>1?'s':'')+' largo'+(res.sil>1?'s':'')+'. Mira en qué tarjetas te ha pasado y repasa esas frases.'; }
  else { cl='bad'; v=res.sil+' silencios largos. Ten la tarjeta de rescate delante y prueba con más tiempo por tarjeta.'; }
 } else { cl='amb'; v='Sin micrófono no he podido contar tus silencios. ¿Cuántas veces te has quedado callado más de '+R.lim+' segundos?'; }
 var hist=S[HK[R.kind]].slice(-6).reverse(), bk=BACK[R.kind];
 var o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="'+bk[0]+'">← '+bk[1]+'</button></div>';
 o+='<div class="res"><div class="kk muted small">'+esc(R.label||(R.kind==='tr'?'ENTRENADOR':'AHORA TÚ · '+R.src.t))+'</div><div class="big">'+mmss(res.s)+'</div>';
 if(res.mic) o+='<div class="kpis"><div><b>'+res.sil+'</b>silencios de más de '+R.lim+' s</div><div><b>'+sec1(res.lg)+' s</b>el silencio más largo</div><div><b>'+Math.min(100,Math.round(res.vo/Math.max(1,res.s)*100))+' %</b>del tiempo con voz</div></div>';
 o+='<div class="verd '+cl+'">'+v+'</div>';
 if(!res.mic) o+='<div class="chips" role="group" aria-label="Mis silencios">'+['Ninguna','1 o 2','3 o más'].map(function(x){ return '<label><input type="radio" name="selfsil" value="'+x+'">'+x+'</label>'; }).join('')+'</div>';
 if(hist.length>1) o+='<p class="small" style="margin:10px 0 0"><b>Tus últimas prácticas:</b></p><ul class="hist">'+hist.map(function(x){ return '<li>'+fdate(x.d)+' · '+mmss(x.s)+(x.t?' · '+esc(x.t):'')+' · '+(x.mic?x.sil+' silencios largos (máx. '+sec1(x.lg)+' s)':(x.self?'silencios: '+x.self:'sin micrófono'))+'</li>'; }).join('')+'</ul>';
 o+='</div>'+(R.after?R.after():'')+'<div id="recout">'+recBlock()+'</div>';
 o+='<h4>Revísate</h4><ul class="chk">'+(R.chk||['No me he quedado callado más de cinco segundos.','Cuando no sabía una palabra, la he explicado (para qué sirve, cómo es...).','Cuando no entendía, he pedido que repita o he preguntado qué significa.','He usado frases para pensar, pero no siempre la misma.','Me he corregido rápido y he seguido.','He usado tú o usted según la situación.']).map(function(x){ return '<li><label><input type="checkbox"><span>'+x+'</span></label></li>'; }).join('')+'</ul>';
 o+='<div class="row"><button class="btn cta" data-act="'+AGAIN[R.kind]+'">Otra vez</button><button class="btn" data-act="print" data-p="sheet">Imprimir la tarjeta de rescate</button><button class="btn" data-go="opinion">Tu opinión</button></div>';
 R.box.innerHTML=o; if(R.kind==='en'||R.kind==='ci') R.box.scrollIntoView(); else window.scrollTo(0,0);
}
var HK={tr:'trh', at:'ath', oc:'ath', en:'enh', ci:'cih'};
var BACK={tr:['trset','Volver al entrenador'], at:['atback','Otras láminas'], oc:['ocset','Volver a la oral completa'], en:['enset','Volver a la entrada'], ci:['ciset','Otro cierre']};
var AGAIN={tr:'tragain', at:'atagain', oc:'ocset', en:'enstart', ci:'cistart'};

/* ---------------- entrenador ---------------- */
function sel(id, opts, val){ return '<select id="'+id+'">'+opts.map(function(r){ return '<option value="'+r[0]+'"'+(String(val)===String(r[0])?' selected':'')+'>'+r[1]+'</option>'; }).join('')+'</select>'; }
function showTrSetup(){
 var O=S.o, o='<h2>El entrenador: sigue hablando</h2><p class="lead">Aparecen tarjetas a un ritmo fijo: palabras que «no te salen», preguntas del examinador, frases que no entiendes, errores para corregir. Tu trabajo: <b>no quedarte callado</b> más de unos segundos. Habla en voz alta todo el tiempo.</p>';
 o+='<div class="opts">';
 o+='<label><span style="flex:1">Tarjetas '+sel('tmode',[['mix','Todo mezclado'],['palabra','Solo palabras para explicar'],['pregunta','Preguntas del examinador (y frases difíciles)']],O.mode)+'<small>Empieza con «Todo mezclado».</small></span></label>';
 o+='<label><span style="flex:1">Con quién hablas '+sel('ttrato',[['ambos','Tú y usted, mezclado'],['usted','Usted (examinador, tiendas)'],['tu','Tú (un amigo)']],O.trato)+'<small>Para las preguntas: las frases de rescate cambian con el trato.</small></span></label>';
 o+='<label><span style="flex:1">Duración '+sel('tdur',[[90,'1 minuto y medio'],[120,'2 minutos'],[180,'3 minutos']],O.dur)+'</span></label>';
 o+='<label><span style="flex:1">Una tarjeta nueva cada '+sel('tevery',[[15,'15 segundos (difícil)'],[20,'20 segundos'],[25,'25 segundos (con calma)']],O.every)+'</span></label>';
 o+='<label><span style="flex:1">Silencio máximo '+sel('tlim',[[3,'3 segundos'],[5,'5 segundos'],[7,'7 segundos']],O.lim)+'<small>Con el micrófono, el entrenador avisa si te quedas callado más tiempo.</small></span></label>';
 o+='<label><input type="checkbox" data-o="mic"'+(O.mic?' checked':'')+'><span>Contar mis silencios con el micrófono<small>El navegador te pedirá permiso. Solo mide si hay voz o no: el sonido no sale de tu ordenador o de tu móvil y no se analiza con inteligencia artificial.</small></span></label>';
 o+='<label><input type="checkbox" data-o="rec"'+(O.rec?' checked':'')+'><span>Grabarme también (opcional)<small>La grabación se queda en esta página; al final puedes escucharla, guardarla en Descargas o borrarla.</small></span></label>';
 o+='<label><input type="checkbox" data-o="beep"'+(O.beep?' checked':'')+'><span>Sonido con cada tarjeta nueva</span></label>';
 o+='</div><div class="tip">Ten la <b>tarjeta de rescate</b> delante las primeras veces. Cuando ya no la necesites, guárdala.</div><div class="row"><button class="btn cta" data-act="trstart">Empezar</button><button class="btn" data-act="print" data-p="sheet">Imprimir la tarjeta de rescate</button></div>';
 if(S.trh.length){ o+='<details><summary>Tus prácticas con el entrenador</summary><ul class="hist">'+S.trh.slice().reverse().map(function(x){ return '<li>'+fdate(x.d)+' · '+mmss(x.s)+' · '+x.n+' tarjetas · '+(x.mic?x.sil+' silencios largos (máx. '+sec1(x.lg)+' s)':(x.self?'silencios: '+x.self:'sin micrófono'))+'</li>'; }).join('')+'</ul></details>'; }
 $('tr').innerHTML=o;
}
function cardFor(type, trato){
 var T=D.tipos[type], c={ty:T.n, ins:T.ins, ph:[]};
 if(type==='palabra'){ c.mn='«'+esc(pick(D.words))+'»'; c.ph=frases('palabra',null,3); }
 else if(type==='pregunta'){ var qs=D.preg.filter(function(q){ return trato==='ambos'||q.trato===trato; }); var q=pick(qs); c.mn='«'+esc(q.q)+'»'; c.ty+=' ('+trName(q.trato)+')'; c.ph=frases(q.t==='Tarea 3'?'dialogo':'pensar', q.trato, 2); }
 else if(type==='dificil'){ var ds=D.dif.filter(function(q){ return trato==='ambos'||q.trato===trato; }); var d=pick(ds); c.mn='«'+esc(d.q).replace(esc(d.dif),'<u>'+esc(d.dif)+'</u>')+'»'; c.ty+=' ('+trName(d.trato)+')'; c.clar=d.clar; c.ph=frases('entiendo', d.trato, 1); }
 else if(type==='error'){ var e=pick(D.err); c.mn=esc(e.mal); c.ph=frases('error',null,2); }
 else { c.mn=esc(pick(D.blanco)); c.ph=frases('blanco',null,3); }
 return c;
}
function trStart(){
 var O=S.o, n=Math.max(2, Math.round(O.dur/O.every)), types;
 if(O.mode==='palabra') types=['palabra'];
 else if(O.mode==='pregunta') types=['pregunta','pregunta','dificil'];
 else types=['palabra','palabra','pregunta','pregunta','dificil','error','blanco'];
 var segs=[], last='';
 for(var i=0;i<n;i++){ var ty; do{ ty=pick(types); } while(types.length>1 && ty===last && Math.random()<0.7); last=ty;
  segs.push({d:(i===n-1? O.dur-O.every*(n-1) : O.every), head:'TARJETA', kind:'card', card:cardFor(ty, O.trato)}); }
 segs[n-1].d=Math.max(10, segs[n-1].d);
 startRun({kind:'tr', box:$('tr'), segs:segs, lim:O.lim, mic:O.mic||O.rec, rec:O.rec, beep:O.beep});
 R.total=segs.reduce(function(a,s){ return a+s.d; },0);
}

/* ---------------- ahora tu ---------------- */
function srcList(){
 var o1=other('T1'), o2=other('T2'), o3=other('T3');
 function mk(k, items, st, name){ return items.map(function(x){ var h=st&&st.h&&st.h[x.id], n=st&&st.n&&st.n[x.id]; return {k:k, id:x.id, t:x.t, x:x, prac:!!(h&&h.length), notes:n||null}; }); }
 return {T1:mk('T1',D.t1,o1), T2:mk('T2',D.t2,o2), T3:mk('T3',D.t3,o3), found:!!(o1||o2||o3)};
}
function findSrc(k,id){ var L=srcList()[k]; for(var i=0;i<L.length;i++) if(L[i].id===id) return L[i]; return null; }
function showAtPick(){
 var L=srcList(), o='<h2>Ahora tú: una tarea entera sin quedarte callado</h2><p class="lead">Elige una lámina del taller oral. Haces la tarea completa con el reloj y, de vez en cuando, te pasa algo: no te sale una palabra, no entiendes al examinador, te quedas en blanco... Tú sigues hablando.</p>';
 o+='<button type="button" class="oc" data-act="ocpick"><b>Nuevo: la oral completa</b><span>La entrada, las tareas 1, 2 y 3 y la despedida, seguidas, como en el examen. Con los 12 minutos de preparación, si quieres.</span></button>';
 o+=L.found?'<div class="tip">He encontrado tus prácticas del taller oral en este navegador: las láminas que ya has practicado salen primero, en verde, y si tienes notas guardadas, las ves mientras hablas.</div>':
  '<div class="tip">No encuentro tus prácticas de las otras piezas del taller oral en este navegador (el monólogo, la foto y los diálogos). No pasa nada: elige cualquier lámina. Si practicas antes en esas piezas con el mismo navegador, aquí verás tus notas.</div>';
 [['T1','Tarea 1 · El monólogo','Hablas tú solo 2-3 minutos sobre un tema.'],['T2','Tarea 2 · La foto','Describes la foto 2-3 minutos con las seis preguntas.'],['T3','Tarea 3 · El diálogo','Hablas con el examinador 3-4 minutos. Necesitas a alguien que haga de examinador, o imagina sus frases.']].forEach(function(g){
  var it=L[g[0]].slice().sort(function(a,b){ return (b.prac?1:0)-(a.prac?1:0); });
  o+='<h3 class="grp">'+g[1]+'</h3><p class="small muted" style="margin:0">'+g[2]+'</p><div class="grid">'+it.map(function(s){
   var sub=(s.k==='T3'?(s.x.tr==='tu'?'Tú':'Usted')+' · ':'')+(s.prac?'Practicada en el taller':'Sin practicar en el taller')+(s.notes?' · tienes notas':'');
   return '<button type="button" class="card'+(s.prac?' pr':'')+'" data-act="atpick" data-k="'+s.k+'" data-id="'+s.id+'"><span class="ci">'+s.id+'</span><span><b>'+esc(s.t)+'</b><span class="s">'+sub+'</span></span></button>'; }).join('')+'</div>';
 });
 $('at').innerHTML=o;
}
function lamHTML(src, cur){
 var x=src.x, k=src.k, o;
 function lis(arr){ return arr.map(function(p,i){ var cls=(cur===i)?'cur':((cur!==null&&cur!==undefined&&i<cur)?'done':''); return '<li class="'+cls+'"><span class="bn">'+(i+1)+'</span>'+esc(p)+'</li>'; }).join(''); }
 if(k==='T1') o='<div class="lam"><div class="lh"><span>Tarea 1. Presentación de un tema</span><span>Tema '+x.id+'</span></div><h3>'+esc(x.t)+'</h3><p>'+esc(x.intro)+'</p><ul>'+lis(x.pa)+'</ul></div>';
 else if(k==='T2') o='<div class="lam"><div class="lh"><span>Tarea 2. Descripción de una fotografía</span><span>Foto '+x.id+'</span></div><h3>'+esc(x.t)+'</h3><div class="ph"><img src="'+esc(x.img)+'" alt="'+esc(x.alt)+'" onerror="this.parentNode.classList.add(\'no\')"><div class="alt">'+esc(x.alt)+'</div></div><ul>'+lis(D.pf)+'</ul></div>';
 else o='<div class="lam"><div class="lh"><span>Tarea 3. Diálogo en una situación imaginaria</span><span>'+(x.tr==='tu'?'TÚ':'USTED')+'</span></div><h3>'+esc(x.t)+'</h3><p>'+esc(x.sit)+' El examinador / La examinadora es '+esc(x.rol)+'.</p><div class="ins">CANDIDATO</div><ul>'+lis(x.pa)+'</ul></div>';
 return o;
}
function noteAt(src, i){
 var n=src.notes; if(!n) return '';
 var v=n[i]; if(v===undefined||v===null) return '';
 if(Object.prototype.toString.call(v)==='[object Array]') v=v.filter(function(z){ return String(z||'').trim(); }).join(' · ');
 else if(typeof v==='object') v=Object.keys(v).map(function(z){ return v[z]; }).filter(function(z){ return String(z||'').trim(); }).join(' · ');
 return String(v||'').trim();
}
function showAtSetup(){
 var s=S.sel && findSrc(S.sel.k, S.sel.id); if(!s){ showAtPick(); return; }
 var A=S.ao, durs=s.k==='T3'?[[180,'3 minutos'],[210,'3 minutos y medio'],[240,'4 minutos']]:[[120,'2 minutos'],[150,'2 minutos y medio'],[180,'3 minutos']];
 var o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="atback">← Otras láminas</button></div><div class="run"><div>'+lamHTML(s,null)+'</div><div>';
 o+='<h3>Cómo va a ser</h3><p>El reloj marca el tiempo de cada '+(s.k==='T2'?'pregunta':'pauta')+' y la lámina te enseña por dónde vas. '+(s.k==='T3'?'Lee en voz alta cada pauta como si fuera la pregunta del examinador (o pide a alguien que haga de examinador) y responde.':'Habla sin parar, como en el examen.')+' De vez en cuando aparece un <b>bloqueo</b>: resuélvelo con una frase de rescate y sigue.</p>';
 o+='<div class="opts">';
 o+='<label><span style="flex:1">Duración '+sel('adur',durs,A.dur[s.k])+'</span></label>';
 o+='<label><span style="flex:1">Bloqueos '+sel('an',[[2,'Pocos (2)'],[3,'Normal (3)'],[5,'Muchos (5)']],A.n)+'</span></label>';
 o+='<label><span style="flex:1">Silencio máximo '+sel('alim',[[3,'3 segundos'],[5,'5 segundos'],[7,'7 segundos']],A.lim)+'</span></label>';
 if(s.notes) o+='<label><input type="checkbox" data-a="notas"'+(A.notas?' checked':'')+'><span>Ver mis notas del taller<small>Tus palabras clave de esa pieza, en cada '+(s.k==='T2'?'pregunta':'pauta')+'. Míralas, pero no las leas.</small></span></label>';
 o+='<label><input type="checkbox" data-a="mic"'+(A.mic?' checked':'')+'><span>Contar mis silencios con el micrófono<small>Solo mide si hay voz o no. El sonido no sale de tu dispositivo.</small></span></label>';
 o+='<label><input type="checkbox" data-a="rec"'+(A.rec?' checked':'')+'><span>Grabarme también (opcional)</span></label>';
 o+='<label><input type="checkbox" data-a="beep"'+(A.beep?' checked':'')+'><span>Sonido al cambiar de pauta y con cada bloqueo</span></label>';
 o+='</div><div class="row"><button class="btn cta" data-act="atstart">Empezar</button></div></div></div>';
 $('at').innerHTML=o;
}
function evFor(s, k, used){
 var x=s.x, tr=k==='T3'?x.tr:'usted', kinds;
 if(k==='T1') kinds=['palabra','pregunta','error','blanco'];
 else if(k==='T2') kinds=['palabra','palabra','pregunta','blanco','error'];
 else kinds=['entiendo','no','dialogo','palabra'];
 var free=kinds.filter(function(z){ return used.indexOf(z)<0; }); var ty=pick(free.length?free:kinds); used.push(ty);
 var c={ty:'', mn:'', ins:'', ph:[], at:0.3+Math.random()*0.25};
 if(ty==='palabra'){ var w=k==='T2'?pick(x.pal):pick(D.words); c.ty='Bloqueo: no te sale la palabra'; c.mn='«'+esc(w)+'»'; c.ins='Explícala sin decirla y sigue.'; c.ph=frases('palabra', k==='T3'?tr:null, 2); }
 else if(ty==='pregunta'){ var qs=D.preg.filter(function(q){ return q.t===(k==='T1'?'Tarea 1':'Tarea 2'); }); var q=pick(qs); c.ty='El examinador te interrumpe'; c.mn='«'+esc(q.q)+'»'; c.ins='Gana un segundo, contesta y vuelve a tu monólogo.'; c.ph=frases('pensar','usted',2); }
 else if(ty==='error'){ var e=pick(D.err); c.ty='Bloqueo: te has equivocado'; c.mn=esc(e.mal); c.ins='Dila, corrígete rápido y sigue.'; c.ph=frases('error',null,2); }
 else if(ty==='blanco'){ c.ty='Bloqueo: te quedas en blanco'; c.mn=k==='T2'?'Mira la lista: ¿qué pregunta toca ahora?':'Mira la lámina: ¿de qué pauta toca hablar?'; c.ins='Frase puente y sigue.'; c.ph=frases('blanco',null,3); }
 else if(ty==='entiendo'){ c.ty='Bloqueo: no entiendes'; c.mn=esc(D.suc3.entiendo[tr]); c.ins='Pide que repita o comprueba con «¿Quieres / Quiere decir...?».'; c.ph=frases('entiendo',tr,1); }
 else if(ty==='no'){ c.ty='Pequeño problema'; c.mn=esc(D.suc3.no[tr]); c.ins='Reacciona y propón otra solución.'; c.ph=tr==='tu'?['Vaya, qué pena.','¿Y si...?','Bueno, pues entonces...']:['Vaya.','Entonces, ¿puedo...?','¿Hay otra solución?']; var b=noteAt(s,5); if(b && S.ao.notas) c.ins+=' Tu segunda opción: '+b; }
 else { c.ty='Bloqueo: no sabes qué contestar'; c.mn=esc(D.suc3.dialogo[tr]); c.ins='Responde algo, añade un porqué y devuelve la pregunta.'; c.ph=frases('dialogo',tr,1); }
 return c;
}
function atStart(){
 var s=S.sel && findSrc(S.sel.k, S.sel.id); if(!s) return;
 var A=S.ao, k=s.k, pa=k==='T2'?D.pf:s.x.pa, n=pa.length, dur=A.dur[k], each=Math.round(dur/n), segs=[];
 var cand=[]; for(var i=(k==='T3'?0:1);i<n;i++) cand.push(i); cand=shuffle(cand).slice(0, Math.min(A.n, cand.length));
 var used=[];
 for(var j=0;j<n;j++){
  var hd=k==='T2'?'PREGUNTA':'PAUTA', mn=esc(pa[j]);
  var ins=k==='T3'?(j===0?'Saluda y empieza con esta pauta. Responde, añade y pregunta.':(j===n-1?'Termina con el plan claro y despídete.':'El examinador te pregunta por esta pauta. Responde, añade y pregunta.')):(k==='T2'?'Lo que ves, un detalle y tu opinión.':'Responde con el tiempo que pide y añade detalles.');
  var nota=(A.notas && s.notes)?noteAt(s,j):'';
  segs.push({d:(j===n-1?dur-each*(n-1):each), head:hd, kind:'pauta', cur:j, card:{ty:(k==='T2'?'Pregunta ':'Pauta ')+(j+1), mn:mn, ins:ins, ph:[]}, nota:nota, ev:null});
 }
 cand.forEach(function(i){ segs[i].ev=evFor(s,k,used); });
 startRun({kind:'at', box:$('at'), segs:segs, lim:A.lim, mic:A.mic||A.rec, rec:A.rec, beep:A.beep, src:{k:k, id:s.id, t:s.t}, side:function(cur){ return lamHTML(s,cur); }});
 R.total=dur;
}

/* ---------------- entrar y terminar: la entrada ---------------- */
function initAC(){ try{ if(!AC){ var C=window.AudioContext||window.webkitAudioContext; if(C) AC=new C(); } if(AC && AC.resume) AC.resume(); }catch(e){} }
function contactList(n){
 var ini=null, nom=null, fin=null, rest=[];
 D.contacto.forEach(function(c){ if(c.fijo==='ini') ini=c; else if(c.fijo==='nom') nom=c; else if(c.fijo==='fin') fin=c; else rest.push(c); });
 return [ini,nom].concat(shuffle(rest).slice(0, Math.max(1,n-3))).concat([fin]);
}
function modTable(qs){ return '<table class="t mods"><tbody>'+qs.map(function(c){ return '<tr><td>«'+esc(c.q)+'»</td><td><b>'+esc(c.mod)+'</b><br><span class="small"><i>Mejor no:</i> '+esc(c.evita)+'<br>'+esc(c.por)+'</span></td></tr>'; }).join('')+'</tbody></table>'; }
function micOpts(G, attr){
 return '<label><input type="checkbox" data-'+attr+'="mic"'+(G.mic?' checked':'')+'><span>Contar mis silencios con el micrófono<small>Solo mide si hay voz o no. El sonido no sale de tu dispositivo.</small></span></label>'+
  '<label><input type="checkbox" data-'+attr+'="rec"'+(G.rec?' checked':'')+'><span>Grabarme también (opcional)<small>Al final puedes escucharte, guardar el audio o borrarlo.</small></span></label>';
}
function vozOpt(G, attr){ return '<label><input type="checkbox" data-'+attr+'="voz"'+(G.voz?' checked':'')+'><span>Leer en voz alta lo que dice el examinador<small>Con la voz de tu navegador, si tiene voz en español. Si no, léelo tú o pide a alguien que haga de examinador.</small></span></label>'; }
function renderEn(){
 if(R.active && R.kind==='en') return;
 var E=S.en, o='<div class="opts">';
 o+='<label><span style="flex:1">Preguntas '+sel('enn',[[4,'4 preguntas'],[5,'5 preguntas']],E.n)+'<small>Empiezan siempre con el documento y el nombre y terminan con «¿Qué opción ha elegido?».</small></span></label>';
 o+='<label><span style="flex:1">Tiempo máximo para cada respuesta '+sel('end',[[15,'15 segundos'],[20,'20 segundos']],E.d)+'<small>Cuando terminas de contestar, pulsa el botón y sale la pregunta siguiente.</small></span></label>';
 o+=vozOpt(E,'e')+micOpts(E,'e')+'</div><div class="row"><button class="btn cta" data-act="enstart">Empezar la entrada</button></div>';
 if(S.enh.length) o+='<details><summary>Tus prácticas de la entrada</summary><ul class="hist">'+S.enh.slice().reverse().map(function(x){ return '<li>'+fdate(x.d)+' · '+mmss(x.s)+' · '+x.n+' preguntas · '+(x.mic?x.sil+' silencios largos':(x.self?'silencios: '+x.self:'sin micrófono'))+'</li>'; }).join('')+'</ul></details>';
 $('en').innerHTML=o;
}
function enStart(){
 var qs=contactList(S.en.n);
 var segs=qs.map(function(c,i){ return {d:S.en.d, head:'PREGUNTA DE CONTACTO', kind:'card', skip:true, skipl:(i===qs.length-1?'He contestado: terminar':'He contestado: siguiente pregunta →'), say:c.q,
  card:{ty:'El examinador'+(c.h?' · habitual':''), mn:'«'+esc(c.q)+'»', ins:'Una frase completa y un detalle pequeño. Después pulsa el botón.'}}; });
 startRun({kind:'en', box:$('en'), segs:segs, lim:S.en.lim, mic:S.en.mic||S.en.rec, rec:S.en.rec, beep:!S.en.voz, voz:S.en.voz, label:'LA ENTRADA · PREGUNTAS DE CONTACTO',
  after:function(){ return '<h4>Compara con las respuestas modelo</h4>'+modTable(qs)+'<div class="tip">La última pregunta te lleva a la tarea 1. <button class="btn sm" data-go="ahora">Seguir con una tarea 1 en «Ahora tú»</button></div>'; },
  chk:['He contestado con frases completas, no con una palabra sola.','He añadido un detalle pequeño en cada respuesta.','No he contado una historia larga: no es la tarea 1.','He dicho la opción y el tema de la tarea 1.','He hablado de usted con el examinador.']});
 R.total=segs.reduce(function(a,s){ return a+s.d; },0);
}

/* ---------------- entrar y terminar: elige el cierre ---------------- */
var EC=null;
function newEc(){ EC={items:shuffle(D.ec.map(function(q,i){ return i; })).map(function(i){ return {q:D.ec[i], ord:shuffle([0,1,2])}; }), k:0, ok:0, done:false}; renderEc(); }
function renderEc(){
 var q=EC, box=$('ec');
 if(q.k>=q.items.length){
  var n=q.items.length, ok=q.ok;
  if(S.ec.best===null || ok>S.ec.best) S.ec.best=ok; S.ec.last=ok; save(); nav();
  box.innerHTML='<div class="quiz"><div class="qn">RESULTADO</div><div class="score">'+ok+' / '+n+'</div><p>'+(ok>=8?'¡Muy bien! Sabes cuándo y cómo cerrar.':'Recuerda: cierra solo cuando has hablado de todo, con una fórmula y una frase final.')+'</p><p class="small muted">Tu mejor resultado: '+S.ec.best+' / '+n+'</p><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="ecnew">Otra vez</button></div></div>';
  return;
 }
 var it=q.items[q.k], Q=it.q;
 var o='<div class="quiz"><div class="qn">MOMENTO '+(q.k+1)+' DE '+q.items.length+'</div><div><span class="ch">'+esc(Q.tarea)+'</span>'+(Q.trato?'<span class="ch tr">USTED</span>':'')+'</div><p class="qs">'+esc(Q.ctx)+'</p>'+(Q.e?'<div class="qe"><b>El examinador</b>«'+esc(Q.e)+'»</div>':'')+'<div role="group" aria-label="Respuestas">';
 it.ord.forEach(function(i){ o+='<button type="button" class="qop" data-act="ecpick" data-i="'+i+'">'+esc(Q.ops[i])+'</button>'; });
 o+='</div><div id="ecfb"></div><div class="row" style="margin-bottom:0" id="ecnext" hidden><button class="btn cta" data-act="ecnext">'+(q.k===q.items.length-1?'Ver el resultado':'Siguiente')+'</button></div></div>';
 box.innerHTML=o;
}
function pickEc(b){
 var q=EC, it=q.items[q.k]; if(q.done) return;
 var i=+b.getAttribute('data-i'), ok=i===it.q.ok; if(ok) q.ok++; q.done=true;
 [].forEach.call(document.querySelectorAll('#ec .qop'), function(x){ x.disabled=true; var j=+x.getAttribute('data-i'); if(j===it.q.ok) x.classList.add('ok'); else if(j===i) x.classList.add('bad'); });
 var k=it.q.tarea==='Tarea 1'?'T1':(it.q.tarea==='Tarea 2'?'T2':null);
 $('ecfb').innerHTML='<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Muy bien!':'Mejor la otra.')+'</b> '+esc(it.q.por)+'</div>'+(it.q.tipo==='cierre'&&k?formsBox(D.cierres[k],'Para cerrar'):(it.q.tipo==='final'?formsBox(D.desp.c,'Para despedirte'):''));
 $('ecnext').hidden=false;
}

/* ---------------- entrar y terminar: te quedan 20 segundos ---------------- */
function c20src(c){ return findSrc(c.k, c.id); }
function dichoHTML(c){ return '<ul class="dch">'+c.dicho.map(function(x){ return '<li>'+esc(x)+'</li>'; }).join('')+'</ul>'; }
function renderCi(){
 if(R.active && R.kind==='ci') return;
 var i=S.ci; if(i===null || i===undefined || !D.c20[i]){ i=S.ci=Math.floor(Math.random()*D.c20.length); save(); }
 var c=D.c20[i], src=c20src(c);
 var o='<div class="chips" role="group" aria-label="Elige un tema o una foto">'+D.c20.map(function(x,j){ return '<label><input type="radio" name="cisel" value="'+j+'"'+(j===i?' checked':'')+'>'+(x.k==='T1'?'Tarea 1':'Foto')+' · '+esc(c20src(x).t)+'</label>'; }).join('')+'</div>';
 o+='<div class="run"><div>'+lamHTML(src, c.k==='T1'?4:5)+'</div><div><h4>Lo que ya has dicho</h4>'+dichoHTML(c)+
  '<p class="small">Al pulsar «Empezar», tienes <b>20 segundos</b> para cerrar '+(c.k==='T1'?'tu monólogo':'tu descripción de la foto')+' en voz alta: una fórmula y una frase final.</p>'+
  '<div class="opts">'+micOpts(S.en,'e')+'</div><div class="row"><button class="btn cta" data-act="cistart">Empezar: 20 segundos</button><button class="btn" data-act="cirand">Otro al azar</button></div></div></div>';
 if(S.cih.length) o+='<details><summary>Tus cierres</summary><ul class="hist">'+S.cih.slice().reverse().map(function(x){ return '<li>'+fdate(x.d)+' · '+esc(x.t||'')+' · '+(x.mic?x.sil+' silencios largos':(x.self?'silencios: '+x.self:'sin micrófono'))+'</li>'; }).join('')+'</ul></details>';
 $('ci').innerHTML=o;
}
function ciStart(){
 var c=D.c20[S.ci], src=c20src(c), last=c.k==='T1'?4:5;
 var segs=[{d:20, head:'CIERRE', kind:'card', cur:last, card:{ty:'Te quedan 20 segundos: cierra', mn:dichoHTML(c), ins:'Cierra ahora en voz alta: una fórmula y una frase final.', ph:D.cierres[c.k], phl:'Para cerrar'}}];
 startRun({kind:'ci', box:$('ci'), segs:segs, lim:5, mic:S.en.mic||S.en.rec, rec:S.en.rec, beep:true, src:{k:c.k, id:c.id, t:src.t}, label:'TE QUEDAN 20 SEGUNDOS · '+src.t,
  side:function(cur){ return lamHTML(src,cur); },
  after:function(){ return '<h4>Dos cierres modelo</h4><ul class="okl">'+c.mod.map(function(m){ return '<li>'+esc(m)+'</li>'; }).join('')+'</ul>'; },
  chk:['He usado una fórmula para cerrar.','He dicho una frase final: mi opinión, un resumen o lo que van a hacer después.','No he cortado de golpe («Ya está», «Fin»).','No me he quedado callado al final.']});
 R.total=20;
}

/* ---------------- ahora tu: la oral completa ---------------- */
var OCD={c:[120,120,180], n:[150,150,210], l:[180,180,240]};
var PREP={t:null, end:0};
function prepStop(){ if(PREP.t) clearInterval(PREP.t); PREP.t=null; }
function ocFill(){ var O=S.oc; if(!findSrc('T1',O.t1)) O.t1=pick(D.t1).id; if(!findSrc('T2',O.t2)) O.t2=pick(D.t2).id; if(!findSrc('T3',O.t3)) O.t3=pick(D.t3.filter(function(x){ return x.tr==='tu'; })).id; }
function ocSrc(){ return {T1:findSrc('T1',S.oc.t1), T2:findSrc('T2',S.oc.t2), T3:findSrc('T3',S.oc.t3)}; }
function showOcSetup(){
 prepStop(); ocFill(); save();
 var O=S.oc, o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="atback">← Otras láminas</button></div><h2>La oral completa</h2>';
 o+='<p class="lead">Como el día del examen: la preparación, la entrada con las preguntas de contacto, las tres tareas seguidas y la despedida. Con bloqueos de vez en cuando, como en «Ahora tú».</p><div class="opts">';
 o+='<label><span style="flex:1">Tarea 1 · tema '+sel('oct1', D.t1.map(function(x){ return [x.id, x.id+'. '+x.t]; }), O.t1)+'</span></label>';
 o+='<label><span style="flex:1">Tarea 2 · foto '+sel('oct2', D.t2.map(function(x){ return [x.id, x.id+'. '+x.t]; }), O.t2)+'</span></label>';
 o+='<label><span style="flex:1">Tarea 3 · situación '+sel('oct3', D.t3.map(function(x){ return [x.id, x.id+'. '+x.t+(x.tr==='tu'?' (tú)':' (usted)')]; }), O.t3)+'<small>En el examen, la tarea 3 sale de la foto de la tarea 2 y suele ser de tú. Aquí la foto y la situación son de dos piezas distintas del taller.</small></span></label>';
 o+='<label><span style="flex:1"><button type="button" class="btn sm" data-act="ocrand">Otra combinación al azar</button></span></label>';
 o+='<label><span style="flex:1">Duración '+sel('ocdur',[['c','Corta: 2 + 2 + 3 minutos'],['n','Normal: 2 y medio + 2 y medio + 3 y medio'],['l','Larga: 3 + 3 + 4 minutos']],O.dur)+'</span></label>';
 o+='<label><span style="flex:1">Bloqueos '+sel('ocn',[[0,'Sin bloqueos'],[3,'Pocos (3)'],[5,'Normal (5)'],[7,'Muchos (7)']],O.n)+'</span></label>';
 o+='<label><span style="flex:1">Silencio máximo '+sel('oclim',[[3,'3 segundos'],[5,'5 segundos'],[7,'7 segundos']],O.lim)+'</span></label>';
 o+='<label><input type="checkbox" data-c="prep"'+(O.prep?' checked':'')+'><span>Empezar con los 12 minutos de preparación<small>Ves las tres láminas y escribes tus notas. Puedes entrar en la sala antes de tiempo.</small></span></label>';
 o+=vozOpt(O,'c')+micOpts(O,'c');
 o+='<label><input type="checkbox" data-c="beep"'+(O.beep?' checked':'')+'><span>Sonido al cambiar de pauta y con cada bloqueo</span></label>';
 o+='</div><div class="row"><button class="btn cta" data-act="ocgo">'+(O.prep?'Ir a la sala de preparación':'Entrar en la sala')+'</button></div>';
 var h=S.ath.filter(function(x){ return x.src==='OC'; });
 if(h.length) o+='<details><summary>Tus orales completas</summary><ul class="hist">'+h.slice().reverse().map(function(x){ return '<li>'+fdate(x.d)+' · '+mmss(x.s)+' · '+esc(x.t)+' · '+(x.mic?x.sil+' silencios largos (máx. '+sec1(x.lg)+' s)':(x.self?'silencios: '+x.self:'sin micrófono'))+'</li>'; }).join('')+'</ul></details>';
 $('at').innerHTML=o;
}
function ocPrep(){
 initAC();
 var X=ocSrc(), O=S.oc, nm={T1:'tarea 1',T2:'tarea 2',T3:'tarea 3'};
 var o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="ocset">← Volver</button></div><h2>Sala de preparación</h2>'+
  '<div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><div class="prep" id="prepclk">12:00</div><p class="small muted" style="margin:0;flex:1">Prepara las tres tareas. Escribe palabras clave, no frases: en la sala puedes mirar tus notas, pero no leerlas.</p></div><div id="prepend"></div>';
 o+='<div class="g3">'+['T1','T2','T3'].map(function(k){ return '<div>'+lamHTML(X[k],null)+'<label class="small"><b>Mis notas · '+nm[k]+'</b><textarea data-ocn="'+k+'">'+esc(O.notes[k]||'')+'</textarea></label></div>'; }).join('')+'</div>';
 o+='<div class="row"><button class="btn cta" data-act="ocstart">Entrar en la sala</button><button class="btn" data-act="occlear">Borrar mis notas</button></div>';
 $('at').innerHTML=o; window.scrollTo(0,0);
 prepStop(); PREP.end=now()+720000;
 PREP.t=setInterval(function(){ var r=(PREP.end-now())/1000, c=$('prepclk'); if(!c){ prepStop(); return; }
  c.textContent=mmss(Math.ceil(r)); c.className='prep'+(r<=60?' red':'');
  if(r<=0){ prepStop(); c.textContent='0:00'; beep(880); var pe=$('prepend'); if(pe) pe.innerHTML='<div class="alarm">Se ha terminado el tiempo de preparación. Entra en la sala.</div>'; } }, 250);
}
function ocStart(){
 prepStop();
 var X=ocSrc(), O=S.oc, dd=OCD[O.dur]||OCD.n, segs=[], cand=[];
 var qs=contactList(4);
 function entLam(){ return '<div class="lam"><div class="lh"><span>La entrada</span><span>No se evalúa</span></div><h3>Preguntas de contacto</h3><p>Una frase completa y un detalle pequeño. Con el examinador hablas de usted.</p></div>'; }
 qs.forEach(function(c,i){ segs.push({d:15, head:'ENTRADA', kind:'card', skip:true, skipl:'He contestado: siguiente →', say:c.q, lam:entLam,
  card:{ty:'El examinador'+(c.h?' · habitual':''), mn:'«'+esc(c.q)+'»', ins:(i===qs.length-1?'Di la opción y el tema: «He elegido la opción 1: '+X.T1.t.toLowerCase()+'».':'Una frase completa y un detalle pequeño.')}}); });
 function addTask(k, src, dur){
  var pa=k==='T2'?D.pf:src.x.pa, n=pa.length, each=Math.round(dur/n), mine=(O.notes[k]||'').trim(), tr=k==='T3'?src.x.tr:'usted';
  for(var j=0;j<n;j++){
   var last=j===n-1, ins;
   if(k==='T3') ins=j===0?'Saluda y empieza con esta pauta. Responde, añade y pregunta.':(last?'Termina con el plan claro.':'El examinador te pregunta por esta pauta. Responde, añade y pregunta.');
   else ins=(k==='T2'?'Lo que ves, un detalle y tu opinión.':'Responde con el tiempo que pide y añade detalles.')+(last?' Y al terminar, cierra sin cortar de golpe.':'');
   var nota=mine || ((S.ao.notas && src.notes)?noteAt(src,j):'');
   var sg={d:(last?dur-each*(n-1):each), head:'TAREA '+k.charAt(1)+' · '+(k==='T2'?'PREGUNTA':'PAUTA'), kind:'pauta', cur:j, lam:(function(s){ return function(cur){ return lamHTML(s,cur); }; })(src),
    card:{ty:(k==='T2'?'Pregunta ':'Pauta ')+(j+1)+(k==='T3'?' · '+(tr==='tu'?'tú':'usted'):''), mn:esc(pa[j]), ins:ins, ph:(last&&k!=='T3'?D.cierres[k]:[]), phl:'Para cerrar'}, nota:nota, ev:null};
   segs.push(sg); if(k==='T3' || j>0) cand.push({i:segs.length-1, k:k, s:src});
  }
 }
 addTask('T1', X.T1, dd[0]);
 segs.push({d:6, quiet:true, skip:true, skipl:'Siguiente →', head:'PASO A LA TAREA 2', say:'Muy bien. Pasamos a la foto.', lam:function(){ return lamHTML(X.T2,null); },
  card:{ty:'El examinador · habitual', mn:'«Muy bien. Pasamos a la foto.»', ins:'Mira la foto un segundo y empieza por lo general: dónde están y quiénes son.'}});
 addTask('T2', X.T2, dd[1]);
 segs.push({d:10, quiet:true, skip:true, skipl:'Siguiente →', head:'PASO A LA TAREA 3', say:'Muy bien. Ahora vamos a imaginar una situación. '+X.T3.x.sit, lam:function(){ return lamHTML(X.T3,null); },
  card:{ty:'El examinador', mn:'«Muy bien. Ahora vamos a imaginar una situación.»', ins:'Lee la situación en la lámina. El examinador es '+X.T3.x.rol+': hablas de '+(X.T3.x.tr==='tu'?'tú':'usted')+'.'}});
 addTask('T3', X.T3, dd[2]);
 segs.push({d:12, skip:true, skipl:'Terminar', head:'FINAL', say:D.desp.e, lam:function(){ return '<div class="lam"><div class="lh"><span>El final</span><span>Habitual</span></div><h3>La despedida</h3><p>Despídete con educación y deja en la mesa las láminas y tus notas.</p></div>'; },
  card:{ty:'El examinador · habitual', mn:'«'+esc(D.desp.e)+'»', ins:'Despídete y deja las notas en la mesa.', ph:D.desp.c, phl:'Para despedirte'}});
 var used={T1:[],T2:[],T3:[]};
 shuffle(cand).slice(0, Math.min(O.n, cand.length)).forEach(function(c){ segs[c.i].ev=evFor(c.s, c.k, used[c.k]); });
 startRun({kind:'oc', box:$('at'), segs:segs, lim:O.lim, mic:O.mic||O.rec, rec:O.rec, beep:O.beep, voz:O.voz, label:'ORAL COMPLETA',
  src:{k:'OC', id:0, t:'Oral completa: tema '+X.T1.id+' · foto '+X.T2.id+' · situación '+X.T3.id},
  side:function(cur, s){ return s.lam(cur); },
  chk:['En la entrada he contestado con frases completas y un detalle.','He cerrado la tarea 1 con una fórmula, sin cortar de golpe.','He cerrado la foto con un resumen o con lo que van a hacer después.','En la tarea 3 he respondido, he añadido algo y he preguntado.','No me he quedado callado más de cinco segundos.','Me he despedido y he dejado las notas en la mesa.']});
 R.total=segs.reduce(function(a,s){ return a+s.d; },0);
}

/* ---------------- opinion y copiar ---------------- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o+='<label><input type="radio" name="o4" value="'+i+'"'+(String(S.o4)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o4').innerHTML=o;
 ['o1','o3','o6'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked=r[i].value===S[k]; });
 $('o2').value=S.o2; $('o5').value=S.o5; $('sname').value=S.name;
}
function histLine(x){ return fdate(x.d)+' - '+mmss(x.s)+(x.t?' - '+x.src+' '+x.t:'')+' - '+(x.mic?x.sil+' silencios de mas de 5 s aprox. (max. '+sec1(x.lg)+' s)':(x.self?'silencios (segun yo): '+x.self:'sin microfono')); }
function pack(){
 var L=['CURSO DELE A2 - ORAL: QUE HACER SI ME BLOQUEO', 'Nombre: '+(S.name||'-'), ''];
 L.push('Entrar y terminar:');
 L.push('  Simulador de la entrada:'); if(S.enh.length) S.enh.forEach(function(x){ L.push('    '+histLine(x)+' - '+x.n+' preguntas'); }); else L.push('    (todavia no)');
 L.push('  Ejercicio "Elige el cierre": '+(S.ec.best===null?'sin hacer':'mejor '+S.ec.best+'/'+D.ec.length+', ultimo '+S.ec.last+'/'+D.ec.length));
 L.push('  Te quedan 20 segundos: cierra:'); if(S.cih.length) S.cih.forEach(function(x){ L.push('    '+histLine(x)); }); else L.push('    (todavia no)');
 L.push('');
 L.push('Ejercicio "Que dices": '+(S.qz.best===null?'sin hacer':'mejor '+S.qz.best+'/8, ultimo '+S.qz.last+'/8'));
 L.push('Ejercicio "Describe la palabra": '+(S.pw.best===null?'sin hacer':'mejor '+S.pw.best+'/8, ultimo '+S.pw.last+'/8'));
 var mine=Object.keys(S.pw.mine).filter(function(w){ return String(S.pw.mine[w]).trim(); });
 if(mine.length){ L.push('Mis descripciones:'); mine.forEach(function(w){ L.push('  '+w+': '+String(S.pw.mine[w]).trim()); }); }
 L.push('', 'Entrenador:'); if(S.trh.length) S.trh.forEach(function(x){ L.push('  '+histLine(x)+' - '+x.n+' tarjetas'); }); else L.push('  (todavia no)');
 L.push('', 'Ahora tu (y oral completa):'); if(S.ath.length) S.ath.forEach(function(x){ L.push('  '+histLine(x)+' - '+x.ev+' bloqueos'); }); else L.push('  (todavia no)');
 L.push('', '1. Lo que me pasa mas: '+(S.o1||'-'), '2. El entrenador me ha ayudado: '+(S.o3||'-'), '3. La frase que voy a usar primero: '+(S.o5||'-'), '4. Falta / no he entendido: '+(S.o2||'-'), '5. Sensacion de control (1-10): '+(S.o4||'-'), '6. Me ha ayudado saber como es el dia de la oral: '+(S.o6||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 qnew:function(){ newQuiz(); }, qpick:function(b){ pickQuiz(b); }, qnext:function(){ QZ.k++; QZ.done=false; renderQuiz(); },
 pwnew:function(){ newPw(); }, pwpick:function(b){ pickPw(b); }, pwnext:function(){ if(MREC.mr) try{ MREC.mr.stop(); }catch(e){} PW.k++; PW.done=false; renderPw(); window.scrollTo(0,$('pw').offsetTop-90); }, pwrec:function(b){ pwRec(b); },
 trstart:function(){ trStart(); window.scrollTo(0,0); }, trset:function(){ showTrSetup(); }, tragain:function(){ showTrSetup(); window.scrollTo(0,0); },
 atpick:function(b){ S.sel={k:b.getAttribute('data-k'), id:+b.getAttribute('data-id')}; save(); showAtSetup(); window.scrollTo(0,0); },
 atback:function(){ if(R.active) stopRun(true); prepStop(); showAtPick(); window.scrollTo(0,0); }, atstart:function(){ atStart(); window.scrollTo(0,0); }, atagain:function(){ showAtSetup(); window.scrollTo(0,0); },
 enstart:function(){ enStart(); $('en').scrollIntoView(); }, enset:function(){ renderEn(); $('p-entrada').scrollIntoView(); },
 ecnew:function(){ newEc(); $('ec').scrollIntoView(); }, ecpick:function(b){ pickEc(b); }, ecnext:function(){ EC.k++; EC.done=false; renderEc(); },
 cistart:function(){ ciStart(); $('ci').scrollIntoView(); }, ciset:function(){ renderCi(); $('ci').scrollIntoView(); },
 cirand:function(){ var j=S.ci; if(D.c20.length>1) while(j===S.ci) j=Math.floor(Math.random()*D.c20.length); S.ci=j; save(); renderCi(); },
 ocpick:function(){ showOcSetup(); window.scrollTo(0,0); }, ocset:function(){ showOcSetup(); window.scrollTo(0,0); },
 ocrand:function(){ S.oc.t1=S.oc.t2=S.oc.t3=null; showOcSetup(); },
 ocgo:function(){ if(S.oc.prep) ocPrep(); else { ocStart(); window.scrollTo(0,0); } }, ocstart:function(){ ocStart(); window.scrollTo(0,0); },
 occlear:function(){ S.oc.notes={T1:'',T2:'',T3:''}; save(); [].forEach.call(document.querySelectorAll('textarea[data-ocn]'), function(t){ t.value=''; }); },
 next:function(){ if(!R.active||R.calib||R.paused) return; hush(); R.done+=elapsed(); if(R.i<R.segs.length-1) enterSeg(R.i+1); else finishRun(); },
 pause:function(){ togglePause(); }, stop:function(){ stopRun(false); },
 delrec:function(){ micClear(); var a=$('recout'); if(a) a.innerHTML=''; },
 print:function(b){ var p=b.getAttribute('data-p'); if(p==='sheet'){ document.body.classList.add('ps'); window.print(); setTimeout(function(){ document.body.classList.remove('ps'); },500); return; }
  var v=$('v-'+p); v.classList.add('printme'); window.print(); setTimeout(function(){ v.classList.remove('printme'); },500); },
 copy:function(){
  var t=pack(), box=$('cbox');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar automáticamente. Escribe tus respuestas en un correo para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
 }
};
document.addEventListener('click', function(e){
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]){ ACTS[a.getAttribute('data-act')](a); return; }
 var g=e.target.closest('[data-go]'); if(g){ var h=g.getAttribute('href'); e.preventDefault(); go(g.getAttribute('data-go')); if(h && h.charAt(0)==='#'){ var el=document.querySelector(h); if(el) setTimeout(function(){ el.scrollIntoView(); },30); } }
});
document.addEventListener('change', function(e){
 var t=e.target, id=t.id;
 if(id==='tmode'){ S.o.mode=t.value; } else if(id==='ttrato'){ S.o.trato=t.value; } else if(id==='tdur'){ S.o.dur=+t.value; } else if(id==='tevery'){ S.o.every=+t.value; } else if(id==='tlim'){ S.o.lim=+t.value; }
 else if(id==='enn'){ S.en.n=+t.value; } else if(id==='end'){ S.en.d=+t.value; }
 else if(id==='oct1'){ S.oc.t1=+t.value; } else if(id==='oct2'){ S.oc.t2=+t.value; } else if(id==='oct3'){ S.oc.t3=+t.value; }
 else if(id==='ocdur'){ S.oc.dur=t.value; } else if(id==='ocn'){ S.oc.n=+t.value; } else if(id==='oclim'){ S.oc.lim=+t.value; }
 else if(t.name==='cisel'){ S.ci=+t.value; save(); renderCi(); return; }
 else if(t.getAttribute && t.getAttribute('data-e')){ S.en[t.getAttribute('data-e')]=t.checked; }
 else if(t.getAttribute && t.getAttribute('data-c')){ S.oc[t.getAttribute('data-c')]=t.checked; if(t.getAttribute('data-c')==='prep'){ save(); showOcSetup(); return; } }
 else if(id==='adur'){ S.ao.dur[S.sel.k]=+t.value; } else if(id==='an'){ S.ao.n=+t.value; } else if(id==='alim'){ S.ao.lim=+t.value; }
 else if(t.getAttribute && t.getAttribute('data-o')){ S.o[t.getAttribute('data-o')]=t.checked; }
 else if(t.getAttribute && t.getAttribute('data-a')){ S.ao[t.getAttribute('data-a')]=t.checked; }
 else if(t.name==='selfsil'){ var h=S[HK[R.kind]]; if(h.length) h[h.length-1].self=t.value; }
 else if(t.name==='o1'||t.name==='o3'||t.name==='o4'||t.name==='o6'){ S[t.name]=t.value; save(); nav(); return; }
 else return;
 save();
});
document.addEventListener('input', function(e){ var t=e.target;
 if(t.getAttribute && t.getAttribute('data-ocn')){ S.oc.notes[t.getAttribute('data-ocn')]=t.value; save(); return; }
 if(t.id==='pwtxt'){ var w=t.getAttribute('data-w'); S.pw.mine[w]=t.value; save(); var p=null; D.pw.forEach(function(x){ if(x.w===w) p=x; }); var wr=$('pwwarn'); if(wr && p) wr.hidden=!saysWord(p,t.value); return; }
 if(t.id==='o2'||t.id==='o5'){ S[t.id]=t.value; save(); nav(); } if(t.id==='sname'){ S.name=t.value; save(); } });
document.addEventListener('keydown', function(e){ if(R.active && e.code==='Space' && e.target===document.body){ e.preventDefault(); togglePause(); } });
document.addEventListener('visibilitychange', function(){ if(document.hidden && R.active && !R.paused && !R.calib) togglePause(); });
window.addEventListener('afterprint', function(){ [].forEach.call(document.querySelectorAll('.printme'), function(v){ v.classList.remove('printme'); }); document.body.classList.remove('ps'); });

renderScale(); newQuiz(); newPw(); newEc();
go(S.cur||'importa');
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_B, body, js))
print("ok", FILE, "·", len(B.SITUACIONES), "situaciones ·", len(B.QUIZ), "en ¿Qué dices? ·", len(B.PALABRAS), "palabras ·",
      len(B.PREGUNTAS) + len(B.DIFICILES) + len(B.ERRORES) + len(B.BLANCO), "tarjetas + %d palabras para el entrenador ·" % len(DATA["words"]),
      "láminas: %d + %d + %d" % (len(B.FUENTES_T1), len(B.FUENTES_T2), len(B.FUENTES_T3)))
