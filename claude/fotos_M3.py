# -*- coding: utf-8 -*-
# FOTOS DE LAS LAMINAS DEL TALLER DE ESCRITURA (Modulo 3 del curso de preparacion DELE A2)
# Pieza comun que usan los cinco builds del taller (kit, pautas, revision, textos modelo, banda 1)
# y build_M3_fotos.py (que escribe M3_prompts_imagenes.txt y nombres.txt).
#
# Cada lamina "con fotos" (texto con fotos o biografia con fotos) lleva en su banco:
#   "photos":  [descripcion 1, 2, 3]   en espanol: es el texto alternativo (alt) y lo que se ve si la imagen no carga
#   "img":     "M3_NN_tipo_quien_que"  nombre fijo de la imagen (M3_NN_....jpg): NN = numero de orden (01, 02...),
#                                      tipo = bio (biografia) o dia (historia de un dia), y quien/que en dos o tres palabras.
#                                      13/10/2026 (Maria): el nombre tiene que decir de que foto se trata.
#   "rotulo":  "..."                   para nombres.txt: que lamina es y que se ve en cada panel (sin tildes ni comillas)
#   "persona": "..."                   en ingles: la persona (o el grupo) que tiene que ser la MISMA en los tres paneles
#                                      (en las biografias, la misma persona a distintas edades: rasgos que no cambian)
#   "escenas": [escena 1, 2, 3]        en ingles: lo que pasa en cada panel
# 12/10/2026 (Maria): las tres fotos de una lamina son UN TRIPTICO (una sola imagen con tres paneles iguales, 3:1),
# como Uxx_escrita.jpg de los simulacros: al generarse a la vez, la persona sale igual en las tres.
# El prompt de cada lamina = ESTILO + TRIPTICO + persona + panel 1, 2, 3 + NO_IA.
# En el ordenador se ve el triptico entero; en el movil, la pagina recorta cada tercio y los pone uno debajo de otro.
# Si una lamina sale en dos piezas, viene del mismo banco (el kit y las pautas se importan en la revision y en los
# textos modelo): una sola imagen.
# Imagenes en WordPress, carpeta del mes MES_WP (igual que las fotos del taller de la foto de la oral).
import re

MES_WP = "2026/10"
IMG_BASE = "https://2spanishteachers.com/wp-content/uploads/" + MES_WP.strip("/") + "/"
ANCHO, KB = 1600, 90          # lo que lee la accion rapida "Imagen DELE" (nombres.txt), como Uxx_escrita.jpg

# Como las fotos de la Escritura del examen (Modelo 0): fotos reales, sencillas, una accion que se entiende,
# la persona grande y reconocible. En color (en el examen van en blanco y negro, pequenas).
# Maria (12/10/2026): que NO parezcan hechas con IA: sin contraste ni HDR, luz plana y natural, poses y posturas
# naturales (nadie posa), piel y ropa normales. Va al principio del prompt y se repite al final (NO_IA).
ESTILO = ("An ordinary, unedited snapshot taken with a phone by a friend; it must look like a real photo, not AI-generated. "
          "Soft, flat, even daylight or normal indoor light, LOW CONTRAST, no HDR, no dramatic or cinematic lighting, "
          "no glow, no strong shadows, muted true-to-life colours (not saturated), slight natural grain. "
          "Real ordinary people with natural skin texture and small imperfections, normal everyday clothes with creases; "
          "relaxed, natural poses and postures caught in the middle of the action, nobody posing or looking at the camera, "
          "no perfect smiles. Simple, clear composition like the photos of an official language exam: the main person "
          "large and clearly visible, one action that is easy to understand, an easy-to-recognise everyday place, "
          "a normal lived-in background, eye-level framing, everything in focus (no blurred background). "
          "No readable text, no logos. ")
NO_IA = (" Avoid: HDR, high contrast, oversharpening, glossy or airbrushed skin, plastic look, perfect symmetrical faces, "
         "studio or stock-photo look, posed smiles, dramatic sky, lens flare, bokeh, extra fingers.")
TRIPTICO = ("Layout: ONE wide image, aspect ratio 3:1, made of exactly three equal square photo panels side by side "
            "(left, middle, right), separated by thin plain white gutters, like three snapshots of the same story printed "
            "next to each other. Each panel is a complete photo on its own. The same people must look exactly the same in "
            "the three panels (same face, hair, body and clothes, unless the panel says otherwise). ")
POSE = re.compile(r"(?i)\b(smil\w* (at|for) the camera|look\w* (at|into) the camera|pos(es|ing) for)\b")

NOMBRE = re.compile(r"^M3_\d\d_(bio|dia)_[a-z0-9]+(_[a-z0-9]+)+$")

def nombre(l):
    return l["img"]

def prompt(l):
    paneles = " ".join("Panel %d (%s): %s" % (i + 1, ("left", "middle", "right")[i], e.strip()) for i, e in enumerate(l["escenas"]))
    return ESTILO + TRIPTICO + l["persona"].strip() + " " + paneles + NO_IA

def check(l, ref):
    """Comprueba una lamina: su imagen (triptico) con nombre y prompt, y cada foto con su panel y su texto alternativo.
    Devuelve cuantas fotos tiene."""
    if not l.get("photos"):
        assert not l.get("img") and not l.get("escenas") and not l.get("rotulo"), ref + ": tiene nombre o escenas de fotos, pero no fotos"
        return 0
    n = len(l["photos"])
    assert n == 3, ref + ": una lamina con fotos lleva 3 fotos (tiene %d)" % n
    assert NOMBRE.match(l.get("img", "")), ref + ": falta el nombre fijo de las fotos (img = M3_NN_bio_quien_que o M3_NN_dia_que)"
    r = l.get("rotulo", "")
    assert len(r.split()) >= 8 and re.search(r"1 .+, 2 .+, 3 ", r) and not re.search(r"[\"'|«»áéíóúñÁÉÍÓÚÑ]", r), ref + ": rotulo (que lamina es y 1..., 2..., 3..., sin tildes ni comillas)"
    assert len(l.get("persona", "").split()) >= 15, ref + ": falta la persona que se repite en las tres fotos"
    esc = l.get("escenas", [])
    assert len(esc) == n, ref + ": %d fotos y %d escenas: cada foto necesita su prompt" % (n, len(esc))
    for i, (alt, e) in enumerate(zip(l["photos"], esc)):
        assert len(alt.split()) >= 6, ref + ": la foto %d no tiene texto alternativo" % (i + 1)
        assert '"' not in alt, ref + ": comillas dobles en el texto alternativo de la foto %d" % (i + 1)
        assert len(e.split()) >= 12, ref + ": la foto %d no tiene escena (prompt)" % (i + 1)
    for i, e in enumerate(esc):
        assert not POSE.search(e), ref + ": la foto %d pide una pose (mirar o sonreir a la camara): sin posar" % (i + 1)
    p = prompt(l)
    assert "no readable text" in p.lower() and "no HDR" in p and "3:1" in p, ref + ": el prompt tiene que decir 3:1, no readable text y no HDR"
    return n

def _attr(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")

def fotos_html(l):
    """El triptico de la lamina. En el ordenador, la imagen entera con Foto 1, 2, 3 encima de cada tercio.
    En el movil, cada tercio recortado de la misma imagen, uno debajo de otro, con su Foto N.
    Si la imagen no carga (todavia no esta subida), se ven las tres descripciones."""
    src = IMG_BASE + nombre(l) + ".jpg"
    err = "onerror=\"this.closest('.fts').classList.add('ftno')\""
    alt_todo = " ".join("Foto %d: %s" % (i + 1, a) for i, a in enumerate(l["photos"]))
    o = ['<div class="fts">',
         '<div class="ftw"><div class="ftl" aria-hidden="true">%s</div><img src="%s" alt="%s" width="%d" height="%d" loading="lazy" %s></div>'
         % ("".join("<span>Foto %d</span>" % (i + 1) for i in range(len(l["photos"]))), src, _attr(alt_todo), ANCHO, ANCHO // 3, err),
         '<div class="ftm">']
    for i, alt in enumerate(l["photos"]):
        o.append('<figure class="ft"><figcaption>Foto %d</figcaption><div class="ftc"><img src="%s" alt="%s" loading="lazy" style="left:-%d%%" %s></div></figure>'
                 % (i + 1, src, _attr(alt), i * 100, err))
    o.append('</div><ol class="ftd">' + "".join("<li><b>Foto %d.</b> %s</li>" % (i + 1, a) for i, a in enumerate(l["photos"])) + "</ol></div>")
    return "".join(o)

CSS = r"""
.fts{margin:10px 0}
.ftw{background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.ftl{display:grid;grid-template-columns:repeat(3,1fr);background:#F6F3EF;border-bottom:1px solid var(--line)}
.ftl span{font-size:.74rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding:3px 10px}
.ftw img{display:block;width:100%;height:auto;aspect-ratio:3/1;object-fit:cover;background:#EEE8E1}
.ftm{display:none}
.ft{margin:0 0 12px;background:#fff;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.ft figcaption{font-size:.74rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding:3px 10px;background:#F6F3EF;border-bottom:1px solid var(--line)}
.ftc{position:relative;aspect-ratio:1/1;overflow:hidden;background:#EEE8E1}
.ftc img{position:absolute;top:0;width:300%;height:100%;max-width:none;object-fit:cover}
.ftd{display:none;list-style:none;margin:0;padding:8px 12px;font-size:.88rem;font-style:italic;line-height:1.45;background:#F1EDE8;border-radius:8px}
.ftd li{margin:3px 0}.ftd b{font-style:normal}
.fts.ftno .ftw,.fts.ftno .ftm{display:none!important}.fts.ftno .ftd{display:block}
@media (max-width:760px){.ftw{display:none}.ftm{display:block}}
@media print{.fts{break-inside:avoid}.ftw{display:block!important}.ftm{display:none!important}}
"""
