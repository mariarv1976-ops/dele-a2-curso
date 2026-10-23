# -*- coding: utf-8 -*-
# Mete la pestana "Hace y durante" (tiempo_R06.py) en la ficha R06 de preposiciones.
# Uso:
#   python3 arreglar_R06_tiempo.py build_R06_preposiciones.py      -> arregla el build (y ya no hace falta mas)
#   python3 arreglar_R06_tiempo.py DELEA2_curso_R06_preposiciones.html  -> arregla el HTML ya subido
# Las dos cosas dan el mismo resultado: el HTML arreglado es el que saldria del build arreglado.
# Si el archivo ya tiene la pestana, no hace nada. Necesita tiempo_R06.py y curso_comun.py en la misma carpeta.
import json, sys
import tiempo_R06 as T
from curso_comun import enc_html, enc_js, NAV_CSS, NAV_JS

BTN_OLD = 'data-go="examen">Siguiente: en el examen</button>'
BTN_NEW = 'data-go="tiempo">Siguiente: hace y durante</button>'
OPN_OLD = '<label><input type="radio" name="o1" value="Por y para">Por y para</label>'
OPN_NEW = OPN_OLD + '\n  <label><input type="radio" name="o1" value="Hace y durante">Hace y durante</label>'
PACK_OLD = "L.push('','OPINION'"
PACK_NEW = "if(window.__R06tiempo) L=L.concat(window.__R06tiempo());\n L.push('','OPINION'"

def once(s, old, new, where):
    n = s.count(old)
    if n != 1: sys.exit("No encuentro una sola vez (%d) el sitio para %s. No he cambiado nada." % (n, where))
    return s.replace(old, new)

def build(s):
    if "tiempo_R06" in s: print("El build ya tiene la pestana: no cambio nada."); return None
    s = once(s, "import banco_R06_preposiciones as B\n", "import banco_R06_preposiciones as B\nimport tiempo_R06 as T  # pestana Hace y durante (14/10)\nT.extend(B)\n", "importar el modulo")
    s = once(s, '("porpara", "Por y para"), ', '("porpara", "Por y para"), ("tiempo", "Hace y durante"), ', "la pestana nueva")
    s = once(s, BTN_OLD, BTN_NEW, "el boton de Por y para")
    s = once(s, OPN_OLD, OPN_NEW, "la pregunta 1 de la opinion")
    s = once(s, "    o += '<h3>Los errores típicos</h3>' + errores()\n", "    o += '<h3>Los errores típicos</h3>' + errores()\n    o += T.resumen()\n", "el resumen")
    s = once(s, 'VIEWS_HTML = "\\n".join(', 'views["tiempo"] = T.view()\nT.check(B.DETECTOR)\nVIEWS_HTML = "\\n".join(', "la vista")
    s = once(s, PACK_OLD, PACK_NEW, "Copiar")
    s = once(s, 'html = page(TITLE + " · Preparación DELE A2", CSS_R, BODY, js)', 'html = page(TITLE + " · Preparación DELE A2", CSS_R + T.CSS, BODY, js + "\\n" + T.js())', "page()")
    return s

def html(s):
    if 'id="v-tiempo"' in s: print("El HTML ya tiene la pestana: no cambio nada."); return None
    # 1. detector: leer el de la pagina, comprobar la pestana con el detector completo y anadir los avisos nuevos
    k = s.index('"detector": [') + len('"detector": ')
    det, end = json.JSONDecoder().raw_decode(s, k)
    have = {d["id"] for d in det}
    new = [d for d in T.DETECTOR if d["id"] not in have]
    T.check(det + new)
    add = "".join(", " + json.dumps(d, ensure_ascii=False) for d in new)
    s = s[:end - 1] + enc_js(add) + s[end - 1:]
    # 2. pestana, boton, opinion, Copiar
    s = once(s, '{"id": "porpara", "label": "Por y para"}, ', '{"id": "porpara", "label": "Por y para"}, {"id": "tiempo", "label": "Hace y durante"}, ', "la pestana nueva")
    s = once(s, BTN_OLD, BTN_NEW, "el boton de Por y para")
    s = once(s, OPN_OLD, enc_html(OPN_NEW), "la pregunta 1 de la opinion")
    s = once(s, PACK_OLD, PACK_NEW, "Copiar")
    # 3. la vista (despues de Por y para) y el resumen imprimible (al final de su seccion)
    s = once(s, '<section class="view" id="v-examen">', '<section class="view" id="v-tiempo">' + enc_html(T.view()) + '</section>\n<section class="view" id="v-examen">', "la vista")
    i = s.index('<section class="view" id="v-resumen">'); j = s.index("</section>", i)
    s = s[:j] + enc_html(T.resumen()) + s[j:]
    # 4. CSS y JS en el mismo sitio que los pondria page()
    s = once(s, enc_html(NAV_CSS) + "</style>", enc_html(T.CSS + NAV_CSS) + "</style>", "el CSS")
    s = once(s, enc_js("\n" + NAV_JS), enc_js("\n" + T.js() + "\n" + NAV_JS), "el JS")
    s.encode("ascii")
    return s

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__ or "Uso: python3 arreglar_R06_tiempo.py ARCHIVO")
    for f in sys.argv[1:]:
        src = open(f, encoding="utf-8").read()
        out = build(src) if f.endswith(".py") else html(src)
        if out is None: continue
        open(f, "w", encoding="ascii" if f.endswith(".html") else "utf-8").write(out)
        print("ok:", f, "| buena en el desplegable de los textos nuevos (1a/2a/3a):", "/".join(map(str, T.POS)) if T.POS else "-")
