# -*- coding: utf-8 -*-
# Pone el GUION EN VIVO a una libreta oral A2 YA HECHA (DELEA2_..._oral_profesora.html), sin el motor ni los datos:
# lee los datos que la libreta lleva dentro (código, láminas, guion, errores, contenidos) y la vuelve a escribir con
# DELE_oral_profesora.py (con patch_libreta_vivo.py aplicado) + libreta_vivo.py. El código de la oral NO cambia.
# Uso:  python3 actualizar_libreta_html.py DELEA2_F1_U05_oral_profesora.html [imgBase] [foto1.jpg foto2.jpg]
#   imgBase por defecto: U01-U03 -> wp-content/uploads/2026/09/, el resto -> 2026/10/ (si la foto no carga, se ve su descripción)
#   fotos por defecto: Uxx_oral_foto1.jpg y Uxx_oral_foto2.jpg
# Escribe el archivo nuevo en la carpeta nuevas/ con el mismo nombre (el original no se toca).
import sys, re, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import DELE_oral_profesora as OP, libreta_vivo as LV
from css_motor import CSS
WP = "https://2spanishteachers.com/wp-content/uploads/"

def leer(path):
    h = open(path, encoding="ascii", errors="strict").read()
    if "lvStep" in h or "class=\"live\"" in h or "vLive" in h:
        raise SystemExit("%s ya tiene el guion en vivo" % path)
    m = re.search(r"var D = (\{.*?\});\nvar ALL = ", h, re.S)
    if not m:
        raise SystemExit("PARADO: no encuentro los datos de la libreta en %s" % path)
    return json.loads(m.group(1))

def lis(html):
    return [re.sub(r"\s+", " ", x).strip() for x in re.findall(r"<li>(.*?)</li>", html, re.S)]
def par(html):
    m = re.search(r"<p class='small'>(.*?)</p>", html, re.S)
    return m.group(1) if m else ""

def convertir(path, base=None, fotos=None):
    D = leer(path)
    if D.get("level") != "A2":
        raise SystemExit("PARADO: %s no es una libreta A2" % path)
    T = {t["n"]: t for t in D["tasks"]}
    code = re.sub(r"^A2-", "", D["examen"])
    if base is None:
        base = WP + ("2026/09/" if re.match(r"U0[1-3]$", code) else "2026/10/")
    fotos = fotos or ["%s_oral_foto%d.jpg" % (code, i + 1) for i in range(len(T[2]["opts"]))]
    oral = {
        "t1": {"ops": [{"title": o["title"], "pautas": lis(o["lamina"])} for o in T[1]["opts"]]},
        "t2": {"fotos": [{"title": o["title"], "desc": par(o["lamina"]), "img": fotos[i] if i < len(fotos) else ""} for i, o in enumerate(T[2]["opts"])],
               "pautas": lis(T[2]["opts"][0]["lamina"])},
        "t3": {"ops": [{"title": o["title"], "intro": par(o["lamina"]), "pautas": lis(o["lamina"])} for o in T[3]["opts"]]},
    }
    guion = "\n".join(T[n].get("guion", "") for n in (1, 2, 3))
    html = OP.build("A2", D["examen"], D["codigo"], D["title"], oral, D["cats"], CSS, guion, D.get("errores", ""),
                    extra={"imgBase": base, "oralModelos": {}})
    tk, _ = OP.tareas_a2(oral, guion)
    av = LV.comprobar(LV.vivo_a2(tk, oral, guion, {"imgBase": base, "oralModelos": {}}))
    # comprobación: lo que se conserva es igual
    D2 = json.loads(re.search(r"var D = (\{.*?\});\nvar ALL = ", html, re.S).group(1))
    assert D2["codigo"] == D["codigo"] and D2["examen"] == D["examen"] and D2["cats"] == D["cats"], "datos distintos"
    for n in (1, 2, 3):
        assert [o["lamina"] for o in D2["tasks"][n - 1]["opts"]] == [o["lamina"] for o in T[n]["opts"]], "láminas distintas T%d" % n
    os.makedirs("nuevas", exist_ok=True)
    out = os.path.join("nuevas", os.path.basename(path))
    open(out, "w", encoding="ascii").write(html)
    return out, D["examen"], D["codigo"], tk[2]["live"], av

if __name__ == "__main__":
    a = sys.argv[1:]
    out, ex, cod, live, av = convertir(a[0], a[1] if len(a) > 1 else None, a[2:] or None)
    print("ok", out, ex, "codigo", cod, "| T3:", ["%s (%s, %d filas, %d frases)" % (o["rol"], o["trato"] or "?", len(o["rows"]), len(o["libre"])) for o in live["ops"]], "| avisos:", av or "ninguno")
