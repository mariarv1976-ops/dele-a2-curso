# -*- coding: utf-8 -*-
# Genera SOLO la libreta oral de la profesora de un modelo, sin el motor, a partir de un extracto con lo que la
# libreta necesita (h1, examen, oral, oralModelos, guion, errores, cats). Mismo código de la oral que el motor.
# Uso: python3 libreta_desde_extracto.py extracto_M07   -> DELEA2_curso_M07_oral_profesora.html
# (Cuando el motor y los datos estén en la carpeta, lo normal es el motor: python3 DELE_A2_motor_modelo.py ...)
import sys, importlib, hashlib
sys.path.insert(0, ".")
import DELE_oral_profesora as OP
from css_motor import CSS
X = importlib.import_module(sys.argv[1]).X

SECRETO = "cc48d40b16aba76d2ebe1f29"   # el mismo del motor: NO compartir
LETRAS = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"
def codigo_oral(examen):
    d = hashlib.sha256((SECRETO + "|" + examen).encode()).digest()
    return "".join(LETRAS[b % len(LETRAS)] for b in d[:5])

cod = codigo_oral(X["examen"])
cats = {k: {"name": v[0], "repaso": v[1]} for k, v in X["cats"].items()}
html = OP.build("A2", X["examen"], cod, X["h1"], X["oral"], cats, CSS, X["guion"], X["errores"],
                extra={"imgBase": X["imgBase"], "oralModelos": X.get("oralModelos", {})})
open(X["fileProf"], "w", encoding="ascii").write(html)
import libreta_vivo as LV
tk, _ = OP.tareas_a2(X["oral"], X["guion"])
av = LV.comprobar(LV.vivo_a2(tk, X["oral"], X["guion"], {"imgBase": X["imgBase"], "oralModelos": X.get("oralModelos", {})}))
print("ok", X["fileProf"], len(html), "examen", X["examen"], "codigo", cod, "| avisos:", av or "ninguno")
