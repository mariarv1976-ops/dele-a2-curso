# -*- coding: utf-8 -*-
# DOSIER ORAL A2 DE ESTRUCTURAS (curso de preparacion DELE A2, Modulo 4, pieza M4-5)
# Uso: python3 build_M4_dosier.py   (con banco_dosier_M4.py y curso_comun.py en la misma carpeta)
# Genera:
#   DELEA2_curso_M4_dosier_oral.html  -> ejecutable del curso (recursos/A2/dele-curso/)
#   DELEA2_dosier_oral_impresion.html -> version para imprimir (de aqui sale el PDF)
#   DELEA2_dosier_oral_estructuras.pdf -> si hay Chromium (playwright); el PDF va tambien a dele-curso/
# Contenido: solo banco_dosier_M4.py. storageKey dele-a2-curso-M4-dosier.
import json, re, sys, os
sys.path.insert(0, ".")
import curso_comun as C
import banco_dosier_M4 as B

LET = "ABC"

# ---------------------------------------------------------------- comprobaciones
def palabras(ps):
    return len(re.sub(r"<[^>]+>", "", " ".join(ps)).replace("«", "").replace("»", "").split())
def check():
    sec = {s["id"]: s for s in B.S}
    assert [s["n"] for s in B.S] == ["", "1", "2", "3", "4", "5", "6", "7"], "orden de las secciones"
    # 1) 12 minutos para las tres tareas (y nada de "tareas 1 y 2" ni "no se prepara")
    todo = json.dumps(B.S, ensure_ascii=False)
    assert "preparar las tres tareas" in todo
    assert not re.search(r"(?i)no se prepara|preparar las tareas 1 y 2", todo), "queda la idea antigua de la preparacion"
    filas = sec["prep"]["bloques"][1][2]
    mins = [re.match(r"(\d+)-(\d+)", f[0]).groups() for f in filas]
    assert [int(b) - int(a) for a, b in mins] == [1, 4, 4, 2, 1], "reparto 1 + 4 + 4 + 2 + 1"
    # 2) la foto: seis preguntas en el orden oficial, con la relacion
    assert [p[0] for p in B.PREGUNTAS_T2] == ["Las personas", "El lugar", "Las acciones", "La relación", "Los sentimientos", "Antes y después"]
    assert len(B.DESCRIPCION) == 6, "la descripcion modelo: un parrafo por pregunta"
    assert 200 <= palabras(B.DESCRIPCION) <= 280, "descripcion modelo: %d palabras" % palabras(B.DESCRIPCION)
    assert "Relación" in B.TARJETA[1][1][0][1] or "relación" in B.TARJETA[1][1][0][1]
    # 3) monologo: cinco pautas, un parrafo por pauta + cierre, longitud real
    assert len(B.LAMINA_T1["pautas"]) == 5 and len(B.MONOLOGO) == 6
    assert 220 <= palabras(B.MONOLOGO) <= 280, "monologo modelo: %d palabras" % palabras(B.MONOLOGO)
    for v in ("fueron", "íbamos", "me gusta", "voy a ir", "he tenido"):
        assert v in re.sub(r"<[^>]+>", "", " ".join(B.MONOLOGO)).lower(), "el monologo tiene que usar: " + v
    # 4) tarea 3: dos dialogos, uno de tu y otro de usted, sin mezclar
    TU = re.compile(r"(?i)\b(puedes|tienes|prefieres|te parece|oye|tú)\b")
    UD = re.compile(r"(?i)\b(usted|puede|tiene|recomienda|perdone|quería)\b")
    cand = lambda d: " ".join(re.sub(r"<[^>]+>", "", t) for q, t in d if q == "Candidato")
    assert TU.search(cand(B.DIALOGO_AMIGO)) and not UD.search(cand(B.DIALOGO_AMIGO)), "dialogo con amiga: solo tu"
    assert UD.search(cand(B.DIALOGO_SERVICIO)) and not TU.search(cand(B.DIALOGO_SERVICIO)), "dialogo de servicio: solo usted"
    assert "Te lo dice la lámina" in todo and "escucha al entrevistador" not in todo
    # ejercicios
    for e in B.EJ:
        if e["tipo"] == "elige":
            for it in e["items"]:
                ok = it["ok"] if isinstance(it["ok"], list) else [it["ok"]]
                assert all(o in it["o"] for o in ok) and len(set(it["o"])) == len(it["o"]) and it["f"].count("____") == 1 and it["why"], it
        elif e["tipo"] == "escribe":
            for it in e["items"]: assert it["f"].count("____") == 1 and it["ok"], it
        elif e["tipo"] == "huecos":
            n = sum(len(re.findall(r"\[\d\]", t)) for q, t in e["lineas"])
            assert n == len(e["huecos"]), e["id"]
            for h in e["huecos"]: assert h["ok"] in h["o"] and len(set(h["o"])) == 3 and h["why"], h
        elif e["tipo"] == "pregunta":
            assert sorted({it["ok"] for it in e["items"]}) == [1, 2, 3, 4, 5, 6], "e7: las seis preguntas"
    # las buenas no siempre en el mismo sitio
    pos = [it["o"].index(it["ok"] if isinstance(it["ok"], str) else it["ok"][0]) for e in B.EJ if e["tipo"] == "elige" for it in e["items"]]
    pos += [h["o"].index(h["ok"]) for e in B.EJ if e["tipo"] == "huecos" for h in e["huecos"]]
    for p in B.PIEZAS: pass
    for t in B.TEMAS_ESQUEMA: assert len(t["pautas"]) == 5
    return pos

# ---------------------------------------------------------------- bloques -> HTML
def tabla(cab, filas):
    o = '<table class="t"><thead><tr>' + "".join("<th>%s</th>" % c for c in cab) + "</tr></thead><tbody>"
    for f in filas:
        o += "<tr>" + "".join('<td data-l="%s">%s</td>' % (re.sub(r"<[^>]+>", "", cab[i]), c) for i, c in enumerate(f)) + "</tr>"
    return o + "</tbody></table>"

def enlaces(cods, pdf):
    if pdf:
        return '<p class="enl">En el curso: ' + " · ".join(B.PIEZAS[c][0] for c in cods) + ".</p>"
    return '<div class="enl"><b>Para practicar más:</b> ' + " · ".join(
        '<a href="%s%s" target="_blank" rel="noopener">%s</a>' % (C.BASE_URL, B.PIEZAS[c][1], B.PIEZAS[c][0]) for c in cods) + "</div>"

def bloque(b, pdf=False):
    k = b[0]
    if k == "p": return "<p>%s</p>" % b[1]
    if k == "h": return "<h3>%s</h3>" % b[1]
    if k == "tabla": return tabla(b[1], b[2])
    if k == "consejo": return '<div class="cons"><div class="ct">%s</div><div>%s</div></div>' % (b[1], b[2])
    if k == "caja": return '<div class="caja"><div class="caja-t">%s</div>%s</div>' % (b[1], "".join("<div>%s</div>" % l for l in b[2]))
    if k == "modelo": return '<p class="mod-int">%s</p><div class="modelo">%s</div><p class="mod-nota">%s</p>' % (b[1], "".join("<p>%s</p>" % p for p in b[2]), b[3])
    if k == "dialogo":
        return '<p class="mod-int">%s</p><div class="modelo dlg">%s</div>' % (b[1], "".join(
            '<p class="%s"><span class="who">%s:</span> %s</p>' % ("c" if q == "Candidato" else "e", q, t) for q, t in b[2]))
    if k == "ol": return "<ol>%s</ol>" % "".join("<li>%s</li>" % x for x in b[1])
    if k == "ul": return "<ul>%s</ul>" % "".join("<li>%s</li>" % x for x in b[1])
    if k == "enlaces": return enlaces(b[1], pdf)
    raise ValueError(k)

def seccion(s, pdf=False):
    num = ('<span class="num">%s</span> ' % s["n"]) if s["n"] else ""
    return '<section class="sec" id="s-%s"><h2>%s%s</h2>%s</section>' % (s["id"], num, s["titulo"], "".join(bloque(b, pdf) for b in s["bloques"]))

def tarjeta_html():
    o = '<div class="tarjeta"><div class="tj-h">DELE A2 · Prueba oral · Tu tarjeta de bolsillo</div><div class="tj-cols">'
    for tit, filas in B.TARJETA:
        o += '<div class="tj-c"><div class="tj-t">%s</div>%s</div>' % (tit, "".join('<div class="tj-f"><b>%s</b><span>%s</span></div>' % f for f in filas))
    o += '</div><div class="tj-pie">' + "".join('<div><b>%s:</b> %s</div>' % f for f in B.TARJETA_PIE) + '</div>'
    return o + '<div class="tj-antes"><b>Antes de entrar.</b> %s</div></div>' % B.TARJETA_ANTES

# ---------------------------------------------------------------- PDF (version imprimible)
def ejercicio_pdf(e, i):
    o = '<div class="ej"><h3>Ejercicio %d. %s</h3><p class="mod-int">%s</p>' % (i, e["titulo"], e["inst"])
    if e["tipo"] in ("elige", "escribe"):
        o += "<ol>"
        for it in e["items"]:
            f = it["f"].replace("____", "<span class='blank'></span>")
            if e["tipo"] == "elige": f += ' <span class="opts">(%s)</span>' % " / ".join(it["o"])
            o += "<li>%s</li>" % f
        o += "</ol>"
    elif e["tipo"] == "huecos":
        o += '<div class="modelo dlg">' + "".join('<p><span class="who">%s:</span> %s</p>' % (q, re.sub(r"\[(\d)\]", r"(\1) <span class='blank'></span>", t)) for q, t in e["lineas"]) + "</div>"
        o += '<p class="small">Opciones: ' + " · ".join("(%d) %s" % (n + 1, " / ".join(h["o"])) for n, h in enumerate(e["huecos"])) + "</p>"
    elif e["tipo"] == "pregunta":
        o += '<p class="small">1 personas y ropa · 2 lugar y objetos · 3 qué hacen · 4 relación · 5 qué sienten · 6 antes y después</p><ol>' + "".join("<li>%s <span class='blank sm'></span></li>" % it["f"] for it in e["items"]) + "</ol>"
    return o + "</div>"

def soluciones_pdf():
    o = []
    for i, e in enumerate(B.EJ, 1):
        if e["tipo"] in ("elige", "escribe"):
            s = " · ".join("%d. %s" % (n, (" / ".join(it["ok"]) if isinstance(it["ok"], list) else it["ok"])) for n, it in enumerate(e["items"], 1))
        elif e["tipo"] == "huecos":
            s = " · ".join("%d. %s" % (n, h["ok"]) for n, h in enumerate(e["huecos"], 1))
        else:
            s = " · ".join("%d. pregunta %d" % (n, it["ok"]) for n, it in enumerate(e["items"], 1))
        nota = {"e3": " (también valen me encanta(n) o prefiero cuando tienen sentido)"}.get(e["id"], "")
        o.append("<p><b>Ejercicio %d.</b> %s%s</p>" % (i, s, nota))
    o.append("<p><b>Ejercicios 8 y 9:</b> no tienen una única solución. Llévalos a clase y coméntalos con tu profesora.</p>")
    return "".join(o)

def esquema_pdf():
    o = '<div class="ej"><h3>Ejercicio 8. Tu esquema de la tarea 1</h3><p class="mod-int">Elige un tema y prepara el esquema en 4 minutos, como en el examen. Después habla 2-3 minutos sin leer y grábate.</p><div class="temas">'
    for t in B.TEMAS_ESQUEMA:
        o += '<div><b>%s</b><ol>%s</ol></div>' % (t["titulo"], "".join("<li>%s</li>" % p for p in t["pautas"]))
    o += '</div><table class="t esq"><thead><tr><th>Pauta</th><th>Palabras clave y un verbo</th></tr></thead><tbody>'
    o += "".join("<tr><td>%s</td><td></td></tr>" % x for x in ["Empezar", "Pauta 1", "Pauta 2", "Pauta 3", "Pauta 4", "Pauta 5", "Terminar"])
    o += '</tbody></table></div><div class="ej"><h3>Ejercicio 9. Tarjeta de autoevaluación</h3><p class="mod-int">Escucha tu grabación y marca lo que has hecho.</p><ul class="checks">'
    return o + "".join("<li>&#9744; %s</li>" % a for a in B.AUTOEVAL) + "</ul></div>"

PDF_CSS = r"""
@page{size:A4;margin:16mm 15mm 18mm}
*{box-sizing:border-box}
body{font-family:'Helvetica Neue',Arial,sans-serif;font-size:10.3pt;line-height:1.45;color:#14161C;margin:0}
h1,h2,h3{font-family:Georgia,serif;line-height:1.2}
h2{font-size:17pt;margin:0 0 10px;border-bottom:3px solid #E8603C;padding-bottom:6px}
h2 .num{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:#E8603C;color:#fff;font-size:14pt;margin-right:6px}
h3{font-size:12pt;margin:14px 0 6px;color:#14161C;break-after:avoid}
.cons,.caja,.modelo{break-inside:avoid}
p{margin:0 0 8px}
.sec{break-before:page}
.cover{height:250mm;display:flex;flex-direction:column;justify-content:center;padding:0 10mm;break-after:page}
.cover .k{font-size:10pt;letter-spacing:.12em;color:#E8603C;font-weight:700}
.cover h1{font-size:44pt;margin:10px 0 6px}
.cover .sub{font-size:14pt;color:#5E5A55;margin-bottom:30px}
.cover .ts div{font-size:12pt;padding:8px 0;border-top:1px solid #E6DFD6}
.cover .fin{margin-top:30px;font-size:11pt;background:#FCE9E1;border-radius:8px;padding:12px 16px}
table.t{width:100%;border-collapse:collapse;margin:6px 0 12px;break-inside:auto}
table.t th{text-align:left;font-size:8.6pt;color:#5E5A55;text-transform:uppercase;letter-spacing:.04em;padding:6px 8px;border-bottom:2px solid #E6DFD6;background:#FBF9F6}
table.t td{padding:6px 8px;border-bottom:1px solid #E6DFD6;vertical-align:top}
table.t tr{break-inside:avoid}
.cons{background:#FCE9E1;border-radius:8px;padding:9px 13px;margin:10px 0;break-inside:avoid}
.cons .ct{font-weight:700;color:#B4401D;margin-bottom:2px}
.caja{border:1.5px dashed #5E5A55;border-radius:8px;padding:10px 14px;margin:8px 0;font-family:'Courier New',monospace;font-size:9.6pt;break-inside:avoid}
.caja-t{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;margin-bottom:4px}
.modelo{background:#fff;border:1px solid #E6DFD6;border-left:4px solid #E8603C;border-radius:0 8px 8px 0;padding:10px 14px;font-family:Georgia,serif;font-size:10.3pt}
.modelo p{margin:0 0 6px}
.modelo b{color:#B4401D}
.dlg p{margin:0 0 3px}.dlg .who{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:9pt}
.dlg p.c .who{color:#B4401D}
.mod-int{color:#5E5A55;font-size:9.6pt}.mod-nota{font-size:9pt;color:#5E5A55;margin-top:4px}
.enl{font-size:9pt;color:#5E5A55;border-top:1px solid #E6DFD6;padding-top:6px;margin-top:10px}
ol,ul{margin:4px 0 10px;padding-left:20px}li{margin:3px 0}
.ej{break-inside:avoid;margin-bottom:10px}
.blank{display:inline-block;width:110px;border-bottom:1px solid #14161C;height:1em;vertical-align:baseline}
.blank.sm{width:40px}
.opts{color:#5E5A55;font-size:9pt}
.small{font-size:9pt}
.temas{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;font-size:9.2pt}
.esq td{height:30px}
.checks{list-style:none;padding:0}
.tarjeta{border:2px solid #E8603C;border-radius:10px;padding:12px 14px}
.tj-h{font-family:Georgia,serif;font-weight:700;font-size:13pt;margin-bottom:8px}
.tj-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.tj-t{background:#E8603C;color:#fff;font-weight:700;padding:4px 8px;border-radius:5px;margin-bottom:6px}
.tj-f{margin:0 0 6px;font-size:9.2pt}.tj-f b{display:block;font-size:8.4pt;color:#B4401D;text-transform:uppercase;letter-spacing:.03em}
.tj-pie{border-top:1px solid #E6DFD6;margin-top:8px;padding-top:6px;font-size:9.2pt}
.tj-antes{background:#FCE9E1;border-radius:6px;padding:8px 10px;margin-top:8px;font-size:9.4pt}
"""

def pdf_html():
    cover = ('<div class="cover"><div class="k">DELE A2 · EXPRESIÓN E INTERACCIÓN ORALES</div><h1>%s</h1><div class="sub">%s</div><div class="ts">'
             '<div><b>Tarea 1</b> · Hablar de un tema de tu vida</div><div><b>Tarea 2</b> · Describir una foto</div>'
             '<div><b>Tarea 3</b> · Hablar con el examinador: organizar algo con un amigo o pedir algo en una tienda o un servicio</div></div>'
             '<div class="fin">Las frases de este dosier sirven para cualquier tema: el tema cambia, la estructura se queda. '
             'Apréndelas, practícalas y úsalas en cada simulacro.</div></div>') % (B.TITULO, B.SUBTITULO)
    body = cover + "".join(seccion(s, True) for s in B.S)
    body += '<section class="sec"><h2><span class="num">8</span> Practica</h2><p>Temas distintos, mismas frases. Escribe tus respuestas y después dilas en voz alta. Las soluciones están en la sección 9.</p>'
    body += "".join(ejercicio_pdf(e, i) for i, e in enumerate(B.EJ, 1)) + esquema_pdf() + "</section>"
    body += '<section class="sec"><h2><span class="num">9</span> Soluciones</h2>%s</section>' % soluciones_pdf()
    body += '<section class="sec"><h2><span class="num">10</span> Tu tarjeta de bolsillo</h2><p>Léela la noche antes y en la sala de espera. No leas nada más.</p>%s</section>' % tarjeta_html()
    return ('<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>Dosier oral A2</title><style>' + PDF_CSS +
            '</style></head><body>' + body + '</body></html>')

def hacer_pdf(html_path, pdf_path):
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        print("AVISO: sin playwright; abre %s en el navegador e imprime en PDF" % html_path); return False
    pie = ('<div style="width:100%;font-size:7.5pt;color:#5E5A55;padding:0 15mm;display:flex;justify-content:space-between;font-family:Arial">'
           '<span>Preparación para el examen DELE A2 · Material no oficial e independiente del Instituto Cervantes</span>'
           '<span>Dosier oral A2 · <span class="pageNumber"></span></span></div>')
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto("file://" + os.path.abspath(html_path)); pg.wait_for_timeout(300)
        pg.pdf(path=pdf_path, format="A4", print_background=True, display_header_footer=True,
               header_template="<span></span>", footer_template=pie,
               margin={"top": "16mm", "bottom": "18mm", "left": "15mm", "right": "15mm"})
        b.close()
    return True

# ---------------------------------------------------------------- EJECUTABLE
TABS = [("inicio", "Empieza aquí"), ("prep", "Preparación"), ("t1", "Tarea 1"), ("t2", "Tarea 2"), ("t3", "Tarea 3"),
        ("bloqueo", "Si me bloqueo"), ("practica", "Practica"), ("tarjeta", "Tarjeta"), ("opinion", "Tu opinión")]

EXE_CSS = r"""
.sec{margin-bottom:34px}
.sec h2 .num{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--coral);color:#fff;font-size:1rem;margin-right:6px;vertical-align:2px}
.sec h3{margin-top:22px}
.cons{background:var(--coral-soft);border-radius:10px;padding:10px 14px;margin:14px 0}
.cons .ct{font-weight:700;color:#B4401D}
.caja{border:1.5px dashed var(--muted);border-radius:10px;padding:12px 16px;margin:12px 0;font-family:'SF Mono',Consolas,monospace;font-size:.88rem;background:#fff}
.caja-t{font-family:system-ui,sans-serif;font-weight:700;margin-bottom:6px}
.modelo{background:#fff;border:1px solid var(--line);border-left:5px solid var(--coral);border-radius:0 10px 10px 0;padding:14px 18px;font-family:Georgia,serif}
.modelo p{margin:0 0 .7em}.modelo b{color:#B4401D}
.modelo.plain b{color:inherit;font-weight:400}
.dlg p{margin:0 0 .35em}.dlg .who{font-family:system-ui,sans-serif;font-weight:700;font-size:.85rem}
.dlg p.c .who{color:#B4401D}
.mod-int{color:var(--muted);font-size:.95rem}.mod-nota{color:var(--muted);font-size:.88rem}
.enl{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:16px 0;font-size:.93rem}
.enl a{color:#B4401D;font-weight:600}
.ex{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:18px 0}
.ex h3{margin:0 0 4px}
.it{padding:10px 0;border-top:1px solid var(--line)}
.it .f{margin-bottom:6px}
.it .gap{display:inline-block;min-width:90px;border-bottom:2px solid var(--ink);text-align:center;font-weight:700;padding:0 4px}
.ops{display:flex;flex-wrap:wrap;gap:8px}
.op{font:inherit;border:1.5px solid var(--line);background:#fff;border-radius:999px;padding:6px 14px;cursor:pointer}
.op:hover{border-color:var(--ink)}
.op.ok{background:var(--ok);border-color:var(--ok);color:#fff}
.op.ko{background:var(--bad-soft);border-color:var(--bad);color:var(--bad)}
.fb{font-size:.92rem;margin-top:6px;border-radius:8px;padding:6px 10px}
.fb.ok{background:var(--ok-soft);color:var(--ok)}.fb.ko{background:var(--bad-soft);color:var(--bad)}
.fb[hidden]{display:none}
.it input[type=text]{font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:6px 10px;width:220px;max-width:100%}
.dl{margin:4px 0}.dl .who{font-weight:700;font-size:.88rem}
.dl select{font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:3px 6px;background:#fff}
.dl select.ok{border-color:var(--ok);background:var(--ok-soft)}.dl select.ko{border-color:var(--bad);background:var(--bad-soft)}
.res{font-weight:600;margin-top:10px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 14px}
.chips label{border:1.5px solid var(--line);border-radius:999px;padding:6px 14px;cursor:pointer;background:#fff}
.chips label:has(input:checked){background:var(--ink);border-color:var(--ink);color:#fff}
.chips input{position:absolute;opacity:0}
textarea{width:100%;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 10px;min-height:56px}
.esq td:first-child{width:110px;font-weight:600}
.esq textarea{min-height:44px}
.lam{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:10px 0}
.timer{display:inline-block;font-variant-numeric:tabular-nums;border:2px solid var(--ink);border-radius:999px;padding:3px 14px;font-weight:700}
.timer.low{border-color:var(--bad);color:var(--bad)}
.checks label{display:flex;gap:10px;align-items:flex-start;margin:6px 0;cursor:pointer}
.checks input{margin-top:6px;accent-color:var(--ink)}
.tarjeta{border:2px solid var(--coral);border-radius:12px;padding:14px 16px;background:#fff}
.tj-h{font-family:Georgia,serif;font-weight:700;font-size:1.15rem;margin-bottom:10px}
.tj-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.tj-t{background:var(--coral);color:#fff;font-weight:700;padding:4px 10px;border-radius:6px;margin-bottom:8px}
.tj-f{margin:0 0 8px;font-size:.92rem}.tj-f b{display:block;font-size:.75rem;color:#B4401D;text-transform:uppercase;letter-spacing:.04em}
.tj-pie{border-top:1px solid var(--line);margin-top:8px;padding-top:8px;font-size:.92rem}
.tj-antes{background:var(--coral-soft);border-radius:8px;padding:8px 12px;margin-top:10px;font-size:.93rem}
@media (max-width:700px){
 .tj-cols{grid-template-columns:1fr}
 table.t thead{display:none}
 table.t tr{display:block;border-bottom:1px solid var(--line);padding:6px 0}
 table.t td{display:block;border:0;padding:3px 8px}
 table.t td::before{content:attr(data-l);display:block;font-size:.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
 table.t td[data-l=""]::before{display:none}
}
@media print{
 header.top,.row,.noprint,footer.legal{display:none!important}
 body{background:#fff;font-size:12px}
 body.only-card section.view{display:none!important}
 body.only-card #v-tarjeta{display:block!important}
 body.only-card #v-tarjeta > *:not(.tarjeta){display:none!important}
 .tj-cols{grid-template-columns:repeat(3,1fr)!important}
}
"""

def vista(tab):
    secs = [s for s in B.S if s["tab"] == tab]
    return "".join(seccion(s) for s in secs)

def body_exe():
    v = {}
    v["inicio"] = ('<h2>Hablar con estructura</h2><p class="lead">%s. Léelo por partes, marca tus frases favoritas y practícalas en voz alta.</p>'
                   '<div class="row"><a class="btn" href="%s%s" target="_blank" rel="noopener">Descargar el dosier en PDF</a>'
                   '<button class="btn" data-go="tarjeta">Ver la tarjeta de bolsillo</button></div>' % (B.SUBTITULO, C.BASE_URL, B.PDF)) + vista("inicio")
    for t in ("prep", "t1", "t2", "t3", "bloqueo"):
        v[t] = vista(t)
    v["practica"] = ('<h2><span class="num" style="display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--coral);color:#fff;font-size:1rem;margin-right:6px">8</span> Practica</h2>'
                     '<p class="lead">Temas distintos, mismas frases. Contesta y mira la corrección al momento. Después, di las frases en voz alta.</p><div id="prac"></div>')
    v["tarjeta"] = ('<h2>Tu tarjeta de bolsillo</h2><p class="lead">Léela la noche antes y en la sala de espera. No leas nada más.</p>'
                    '<div class="row"><button class="btn cta" data-act="printcard">Imprimir la tarjeta</button></div>' + tarjeta_html())
    v["opinion"] = '<h2>Tu opinión</h2><p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo.</p><div id="opn"></div>'
    nav = "".join('<button type="button" data-go="%s">%s</button>' % (k, l) for k, l in TABS)
    main = "".join('<section class="view" id="v-%s">%s<div class="row noprint">%s</div></section>' % (
        k, v[k], ('<button class="btn cta" data-go="%s">Siguiente: %s</button>' % (TABS[i + 1][0], TABS[i + 1][1].lower())) if i + 1 < len(TABS) else "")
        for i, (k, l) in enumerate(TABS))
    return ('<header class="top"><div class="top-in"><div class="brand"><div style="font-family:Georgia,serif;font-weight:700;font-size:1.3rem">Dosier oral: hablar con estructura</div>'
            '<small>Preparación DELE A2 · Expresión e interacción orales</small></div><nav class="steps" id="steps" aria-label="Partes del dosier">' + nav +
            '</nav></div></header><main class="wrap">' + main +
            '<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer></main>')

JS = r"""
(function(){
var D=__DATA__;
var KEY='dele-a2-curso-M4-dosier';
var S=load();
function blank(){ return {cur:'inicio', r:{}, esq:{t:0, l:{}}, auto:{}, op:{}, name:''}; }
function load(){ try{ var o=JSON.parse(localStorage.getItem(KEY)||'null'); if(o){ var b=blank(); for(var k in b) if(!(k in o)) o[k]=b[k]; return o; } }catch(e){} return blank(); }
function save(){ try{ localStorage.setItem(KEY, JSON.stringify(S)); }catch(e){} }
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function norm(s){ return String(s||'').toLowerCase().replace(/\s+/g,' ').trim(); }
function sinTilde(s){ return norm(s).normalize('NFD').replace(/[̀-ͯ]/g,''); }
function oks(it){ return Array.isArray(it.ok)?it.ok:[it.ok]; }

/* ---------- navegacion ---------- */
function go(id){ S.cur=id; save(); show(); window.scrollTo(0,0); }
function show(){
 var bs=document.querySelectorAll('#steps button'); for(var i=0;i<bs.length;i++){ var on=bs[i].getAttribute('data-go')===S.cur; bs[i].className=on?'on':''; if(on) bs[i].setAttribute('aria-current','page'); else bs[i].removeAttribute('aria-current'); }
 var vs=document.querySelectorAll('section.view'); for(var j=0;j<vs.length;j++) vs[j].className='view'+(vs[j].id==='v-'+S.cur?' on':'');
 if(S.cur==='practica') prac(); if(S.cur==='opinion') opn();
}

/* ---------- practica ---------- */
function R(e,i){ S.r[e]=S.r[e]||{}; return S.r[e][i]; }
function setR(e,i,v){ S.r[e]=S.r[e]||{}; var o=S.r[e][i]||{}; if(o.first===undefined) o.first=v.ok; o.last=v.val; o.ok=v.ok; S.r[e][i]=o; save(); }
function score(e){ var n=0, t=0, r=S.r[e.id]||{}; var tot=e.tipo==='huecos'?e.huecos.length:e.items.length; for(var i=0;i<tot;i++){ if(r[i]){ t++; if(r[i].first) n++; } } return {n:n,t:t,tot:tot}; }
function resLine(e){ var s=score(e); return s.t? 'A la primera: '+s.n+' de '+s.tot+(s.t<s.tot?' (te faltan '+(s.tot-s.t)+')':'') : ''; }
function exHtml(e,k){
 var o='<div class="ex" id="ex-'+e.id+'"><h3>Ejercicio '+(k+1)+'. '+e.titulo+'</h3><p class="mod-int">'+e.inst+'</p>';
 if(e.tipo==='elige'||e.tipo==='pregunta'){
  e.items.forEach(function(it,i){
   var r=R(e.id,i), f=e.tipo==='pregunta'?it.f:it.f.replace('____','<span class="gap">'+(r&&r.ok?esc(r.last):'&nbsp;')+'</span>');
   var opts=e.tipo==='pregunta'?[1,2,3,4,5,6]:it.o;
   o+='<div class="it"><div class="f">'+(i+1)+'. '+f+'</div><div class="ops">'+opts.map(function(x){
     var c=''; if(r){ if(String(r.last)===String(x)) c=r.ok?' ok':' ko'; }
     return '<button type="button" class="op'+c+'" data-e="'+e.id+'" data-i="'+i+'" data-v="'+esc(x)+'">'+(e.tipo==='pregunta'?D.preg[x-1]:esc(x))+'</button>'; }).join('')+'</div>';
   o+='<div class="fb '+(r?(r.ok?'ok':'ko'):'')+'"'+(r?'':' hidden')+'>'+(r?fbTxt(e,it,r):'')+'</div></div>';
  });
 } else if(e.tipo==='escribe'){
  e.items.forEach(function(it,i){
   var r=R(e.id,i);
   o+='<div class="it"><div class="f">'+(i+1)+'. '+it.f.replace('____','<span class="gap">…</span>')+'</div><input type="text" data-w="'+e.id+'" data-i="'+i+'" value="'+esc(r?r.last:'')+'" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Respuesta '+(i+1)+'"> <button type="button" class="btn sm" data-chk="'+e.id+'" data-i="'+i+'">Comprobar</button>';
   o+='<div class="fb '+(r?(r.ok?'ok':'ko'):'')+'"'+(r?'':' hidden')+'>'+(r?fbW(it,r):'')+'</div></div>';
  });
 } else if(e.tipo==='huecos'){
  o+='<div class="modelo dlg">';
  e.lineas.forEach(function(l){
   o+='<p class="dl"><span class="who">'+l[0]+':</span> '+l[1].replace(/\[(\d)\]/g,function(m,n){
     var i=+n-1, h=e.huecos[i], r=R(e.id,i);
     return '<select data-h="'+e.id+'" data-i="'+i+'" class="'+(r?(r.ok?'ok':'ko'):'')+'" aria-label="Hueco '+n+'"><option value="">('+n+') …</option>'+D.order[e.id][i].map(function(x){ return '<option'+(r&&r.last===x?' selected':'')+'>'+esc(x)+'</option>'; }).join('')+'</select>'; })+'</p>';
  });
  o+='</div><div id="hfb-'+e.id+'">'+hfb(e)+'</div>';
 }
 return o+'<div class="res" id="res-'+e.id+'">'+resLine(e)+'</div></div>';
}
function fbTxt(e,it,r){ if(e.tipo==='pregunta'){ return r.ok?'✓ Sí: pregunta '+it.ok+' ('+D.preg[it.ok-1]+').':'✗ No. Es la pregunta '+it.ok+' ('+D.preg[it.ok-1]+').'; }
 return (r.ok?'✓ ':'✗ ')+it.why+(r.ok?'':' Prueba otra vez.'); }
function fbW(it,r){ if(r.ok) return '✓ ¡Bien! '+esc(it.ok[0])+'.'+(r.tilde?' Ojo con la tilde: '+esc(it.ok[0])+'.':''); return '✗ Todavía no. Estar + gerundio: '+(r.hint||'')+' Prueba otra vez.'; }
function hfb(e){ var o=''; e.huecos.forEach(function(h,i){ var r=R(e.id,i); if(r) o+='<div class="fb '+(r.ok?'ok':'ko')+'">('+(i+1)+') '+(r.ok?'✓ ':'✗ ')+h.why+'</div>'; }); return o; }
function prac(){
 var o=''; D.ej.forEach(function(e,k){ o+=exHtml(e,k); });
 // ejercicio 8: esquema
 var t=D.temas[S.esq.t||0];
 o+='<div class="ex" id="ex-esq"><h3>Ejercicio 8. Tu esquema de la tarea 1</h3><p class="mod-int">Elige un tema y prepara el esquema en 4 minutos, como en el examen: palabras clave y un verbo, nada de frases. Después habla 2-3 minutos sin leer y grábate.</p>';
 o+='<div class="chips">'+D.temas.map(function(x,i){ return '<label><input type="radio" name="esqt" value="'+i+'"'+((S.esq.t||0)===i?' checked':'')+'>'+x.titulo+'</label>'; }).join('')+'</div>';
 o+='<div class="lam"><b>'+t.titulo+'</b>. Hable de:<ol>'+t.pautas.map(function(p){return '<li>'+p+'</li>';}).join('')+'</ol></div>';
 o+='<div class="row"><button class="btn" data-act="t4">Empezar los 4 minutos</button><span id="t4" class="timer" hidden></span></div>';
 o+='<table class="t esq"><tbody>'+['Empezar','Pauta 1','Pauta 2','Pauta 3','Pauta 4','Pauta 5','Terminar'].map(function(x,i){ var k=(S.esq.t||0)+'-'+i; return '<tr><td>'+x+'</td><td><textarea data-esq="'+k+'" aria-label="'+x+'">'+esc(S.esq.l[k]||'')+'</textarea></td></tr>'; }).join('')+'</tbody></table>';
 o+='<p class="small muted" id="esqw"></p></div>';
 o+='<div class="ex"><h3>Ejercicio 9. Tarjeta de autoevaluación</h3><p class="mod-int">Escucha tu grabación y marca lo que has hecho.</p><div class="checks">'+D.auto.map(function(a,i){ return '<label><input type="checkbox" data-auto="'+i+'"'+(S.auto[i]?' checked':'')+'><span>'+a+'</span></label>'; }).join('')+'</div></div>';
 $('prac').innerHTML=o; esqWarn();
}
function esqWarn(){ var el=$('esqw'); if(!el) return; var t=S.esq.t||0, bad=0; for(var i=0;i<7;i++){ var v=S.esq.l[t+'-'+i]||''; if(v.split(/\s+/).filter(Boolean).length>12) bad++; } el.textContent= bad? 'Ojo: en '+bad+' casilla(s) has escrito casi una frase. En el examen, solo palabras clave: si escribes frases, las vas a leer.' : ''; }

/* ---------- opinion ---------- */
function opn(){
 var o='<div>'; D.opinion.forEach(function(q,i){
  o+='<p><b>'+(i+1)+'. '+q.q+'</b></p>';
  if(q.chips) o+='<div class="chips">'+q.chips.map(function(c){ return '<label><input type="radio" name="'+q.id+'" value="'+esc(c)+'"'+(S.op[q.id]===c?' checked':'')+'>'+c+'</label>'; }).join('')+'</div>';
  else if(q.escala) o+='<div class="chips">'+[1,2,3,4,5,6,7,8,9,10].map(function(c){ return '<label><input type="radio" name="'+q.id+'" value="'+c+'"'+(String(S.op[q.id])===String(c)?' checked':'')+'>'+c+'</label>'; }).join('')+'</div>';
  else o+='<textarea data-op="'+q.id+'">'+esc(S.op[q.id]||'')+'</textarea>';
 });
 o+='</div><label style="display:block;max-width:360px;margin-top:14px"><b>Tu nombre</b><input type="text" id="sname" value="'+esc(S.name)+'" autocomplete="name" style="width:100%;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 10px;margin-top:6px"></label>';
 o+='<div class="row"><button class="btn cta" data-act="copy">Copiar mis resultados y mi opinión</button></div><div class="copied-box" id="cpok" role="status" hidden></div><p class="muted small">Pégalo en un correo para tu profesora: '+D.email+'</p>';
 $('opn').innerHTML=o;
}
function pack(){
 var L=['DOSIER ORAL A2 - HABLAR CON ESTRUCTURA','Nombre: '+(S.name||'-'),''];
 L.push('PRACTICA (a la primera):');
 D.ej.forEach(function(e,k){ var s=score(e); L.push('- Ejercicio '+(k+1)+' ('+e.titulo+'): '+(s.t?s.n+'/'+s.tot+(s.t<s.tot?' (hechos '+s.t+')':''):'sin hacer'));
  var r=S.r[e.id]||{}; Object.keys(r).forEach(function(i){ if(!r[i].first){ var it=e.tipo==='huecos'?e.huecos[i]:e.items[i]; L.push('    fallo '+(+i+1)+(it.f?': '+it.f.replace(/<[^>]+>/g,''):'')+' -> buena: '+(e.tipo==='pregunta'?'pregunta '+it.ok:oks(it).join(' / '))); } }); });
 var t=D.temas[S.esq.t||0], has=false, E=['','ESQUEMA DE LA TAREA 1 ('+t.titulo+'):'];
 ['Empezar','Pauta 1','Pauta 2','Pauta 3','Pauta 4','Pauta 5','Terminar'].forEach(function(x,i){ var v=S.esq.l[(S.esq.t||0)+'-'+i]; if(v){ has=true; E.push('- '+x+': '+v.replace(/\n/g,' / ')); } });
 if(has) L=L.concat(E);
 var a=D.auto.filter(function(x,i){ return S.auto[i]; }); L.push(''); L.push('AUTOEVALUACION ('+a.length+' de '+D.auto.length+'):'); D.auto.forEach(function(x,i){ L.push((S.auto[i]?'[x] ':'[ ] ')+x); });
 L.push(''); L.push('OPINION:'); D.opinion.forEach(function(q,i){ L.push((i+1)+'. '+q.q.replace(/<[^>]+>/g,'')+' '+(S.op[q.id]||'-')); });
 return L.join('\n');
}

/* ---------- eventos ---------- */
var T4=null;
document.addEventListener('click', function(ev){
 var g=ev.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var b=ev.target.closest('.op[data-e]'); if(b){
  var e=D.ej.filter(function(x){return x.id===b.getAttribute('data-e');})[0], i=+b.getAttribute('data-i'), it=e.items[i], v=b.getAttribute('data-v');
  var ok = e.tipo==='pregunta' ? (+v===it.ok) : (oks(it).indexOf(v)>-1);
  setR(e.id,i,{ok:ok, val:e.tipo==='pregunta'?+v:v}); var y=window.scrollY; prac(); window.scrollTo(0,y); return; }
 var c=ev.target.closest('[data-chk]'); if(c){
  var e2=D.ej.filter(function(x){return x.id===c.getAttribute('data-chk');})[0], i2=+c.getAttribute('data-i'), it2=e2.items[i2];
  var inp=document.querySelector('input[data-w="'+e2.id+'"][data-i="'+i2+'"]'), val=norm(inp.value);
  if(!val){ inp.focus(); return; }
  var ok2=it2.ok.some(function(x){ return norm(x)===val; }), til=false;
  if(!ok2 && it2.ok.some(function(x){ return sinTilde(x)===sinTilde(val); })){ ok2=true; til=true; }
  var hint = /^est(a|á|an|án)\s/.test(val) ? 'el verbo estar está bien; revisa el gerundio (-ando, -iendo).' : (it2.f.indexOf('Dos')===0||it2.f.indexOf('Una pareja')===0 ? '¿uno o varios? está / están + -ando, -iendo.' : 'está / están + -ando, -iendo.');
  setR(e2.id,i2,{ok:ok2, val:inp.value}); S.r[e2.id][i2].tilde=til; S.r[e2.id][i2].hint=hint; save();
  var y2=window.scrollY; prac(); window.scrollTo(0,y2); return; }
 var a=ev.target.closest('[data-act]'); if(!a) return; var act=a.getAttribute('data-act');
 if(act==='printcard'){ document.body.classList.add('only-card'); window.print(); setTimeout(function(){ document.body.classList.remove('only-card'); },500); }
 if(act==='t4'){ var el=$('t4'), end=Date.now()+240000; el.hidden=false; if(T4) clearInterval(T4);
  T4=setInterval(function(){ var l=Math.max(0,Math.round((end-Date.now())/1000)); el.textContent=Math.floor(l/60)+':'+((l%60)<10?'0':'')+(l%60); el.className='timer'+(l<=30?' low':''); if(!l){ clearInterval(T4); el.textContent='¡Tiempo! Ahora habla 2-3 minutos.'; } },250); }
 if(act==='copy'){ var t=pack(), box=$('cpok');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar. Selecciona el texto y cópialo a mano.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(x){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard&&navigator.clipboard.writeText&&window.isSecureContext) navigator.clipboard.writeText(t).then(ok,fb); else fb(); }
});
document.addEventListener('change', function(ev){
 var t=ev.target;
 if(t.matches('select[data-h]')){ var e=D.ej.filter(function(x){return x.id===t.getAttribute('data-h');})[0], i=+t.getAttribute('data-i'); if(!t.value) return;
  setR(e.id,i,{ok:t.value===e.huecos[i].ok, val:t.value}); t.className=t.value===e.huecos[i].ok?'ok':'ko'; $('hfb-'+e.id).innerHTML=hfb(e); $('res-'+e.id).textContent=resLine(e); }
 if(t.name==='esqt'){ S.esq.t=+t.value; save(); var y=window.scrollY; prac(); window.scrollTo(0,y); }
 if(t.matches('[data-auto]')){ S.auto[t.getAttribute('data-auto')]=t.checked; save(); }
 if(t.closest('#opn') && t.type==='radio'){ S.op[t.name]=t.value; save(); }
});
document.addEventListener('input', function(ev){
 var t=ev.target;
 if(t.matches('[data-esq]')){ S.esq.l[t.getAttribute('data-esq')]=t.value; save(); esqWarn(); }
 if(t.matches('[data-op]')){ S.op[t.getAttribute('data-op')]=t.value; save(); }
 if(t.id==='sname'){ S.name=t.value; save(); }
});
document.addEventListener('keydown', function(ev){ if(ev.key==='Enter' && ev.target.matches('input[data-w]')){ ev.preventDefault(); var b=ev.target.parentNode.querySelector('[data-chk]'); if(b) b.click(); } });
show();
})();
"""

def barajar_huecos():
    """Orden fijo de las opciones de cada hueco (sin Math.random): rota la lista para que la buena no caiga
    siempre en el mismo sitio. Devuelve {id: [[opciones], ...]}."""
    out = {}
    for e in B.EJ:
        if e["tipo"] != "huecos": continue
        out[e["id"]] = []
        for i, h in enumerate(e["huecos"]):
            o = list(h["o"]); r = (i * 2 + len(e["id"])) % 3
            out[e["id"]].append(o[r:] + o[:r])
    return out

def barajar_elige():
    """Orden fijo de las opciones de los ejercicios de elegir: el banco las tiene con la buena casi siempre
    delante; aqui se rota cada lista (sin azar) para que la buena cambie de sitio."""
    import copy
    ej = copy.deepcopy(B.EJ)
    for e in ej:
        if e["tipo"] != "elige": continue
        for i, it in enumerate(e["items"]):
            o = it["o"]; r = (i * 7 + len(e["titulo"])) % len(o)
            it["o"] = o[r:] + o[:r]
    return ej

def build():
    pos = check()
    B.EJ = barajar_elige()
    order = barajar_huecos()
    rep = [0, 0, 0]
    for e in B.EJ:
        if e["tipo"] == "elige":
            for it in e["items"]: rep[it["o"].index(it["ok"] if isinstance(it["ok"], str) else it["ok"][0])] += 1
    for eid, lst in order.items():
        e = [x for x in B.EJ if x["id"] == eid][0]
        for h, o in zip(e["huecos"], lst): rep[o.index(h["ok"])] += 1
    print("posicion de la buena (1.a/2.a/3.a):", rep)
    data = {"ej": B.EJ, "order": order, "temas": B.TEMAS_ESQUEMA, "auto": B.AUTOEVAL, "opinion": B.OPINION, "email": C.EMAIL,
            "preg": ["1 personas y ropa", "2 lugar y objetos", "3 qué hacen", "4 relación", "5 qué sienten", "6 antes y después"]}
    # ejercicios "elige": las opciones salen en el orden del banco, que ya esta repartido a mano
    html = C.page("Dosier oral A2", C.CSS + EXE_CSS, body_exe(), JS.replace("__DATA__", json.dumps(data, ensure_ascii=False)))
    open("DELEA2_curso_M4_dosier_oral.html", "w", encoding="ascii").write(html)
    open("DELEA2_dosier_oral_impresion.html", "w", encoding="utf-8").write(pdf_html())
    ok = hacer_pdf("DELEA2_dosier_oral_impresion.html", B.PDF)
    print("ok · ejecutable %d bytes · PDF %s" % (len(html), "hecho" if ok else "pendiente"))

if __name__ == "__main__":
    build()
