# -*- coding: utf-8 -*-
# Añade el GUION EN VIVO (libreta_vivo.py) a la libreta oral de la profesora, DELE_oral_profesora.py.
# Uso (en la carpeta del motor, con libreta_vivo.py al lado):
#     python3 patch_libreta_vivo.py                 (cambia DELE_oral_profesora.py)
#     python3 patch_libreta_vivo.py otro_archivo.py
# Cada cambio busca un trozo exacto y se para si no lo encuentra o lo encuentra dos veces: nunca deja la libreta
# a medias. Si ya está aplicado, no hace nada. Las libretas B2 no cambian (el guion en vivo es solo para A2) y,
# si falta libreta_vivo.py, la libreta funciona como siempre.
import sys
P = sys.argv[1] if len(sys.argv) > 1 else "DELE_oral_profesora.py"
s = open(P, encoding="utf-8").read()
if "libreta_vivo" in s:
    sys.exit("%s ya lleva el guion en vivo: no hago nada" % P)

CAMBIOS = [
 ("import json, re",
  "import json, re\n"
  "try:  # guion en vivo de la libreta A2 (23/10/2026): libreta_vivo.py en la misma carpeta\n"
  "    from libreta_vivo import CSS_VIVO, JS_VIVO, vivo_a2\n"
  "except ImportError:  # sin libreta_vivo.py, la libreta de siempre\n"
  "    CSS_VIVO, JS_VIVO, vivo_a2 = \"\", \"\", None"),
 ("o+='<div class=\"cols\"><div class=\"col\">';",
  "if(tk.live) o+=vLive(tk,n,st);\n o+='<div class=\"cols\"><div class=\"col\">';"),
 ("o+='<div class=\"card\"><h4>Lo que ve el estudiante</h4>'",
  "if(!tk.live) o+='<div class=\"card\"><h4>Lo que ve el estudiante</h4>'"),
 ("o+='<div class=\"card\"><h4>'+(tk.guionTitle",
  "if(!tk.live) o+='<div class=\"card\"><h4>'+(tk.guionTitle"),
 ("function noteCard(n){",
  "__JS_VIVO__\nfunction noteCard(n){"),
 ("else if(a==='op'){ E.t[n].op=+b.getAttribute('data-i'); }",
  "else if(a==='op'){ E.t[n].op=+b.getAttribute('data-i'); if(n===2 && E.t[3] && D.tasks[2] && D.tasks[2].live && E.t[3].op!==E.t[2].op && E.t[2].op<D.tasks[2].opts.length){ E.t[3].op=E.t[2].op; E.t[3].steps={}; } }\n"
  " else if(a==='lvstep'){ var LS=E.t[n].steps||(E.t[n].steps={}), lk=b.getAttribute('data-i'); LS[lk]=!LS[lk]; }\n"
  " else if(a==='lvreset'){ E.t[n].steps={}; }\n"
  " else if(a==='lvans'){ LV_ANS=!LV_ANS; saveJ('2st_oral_lv_respuestas', LV_ANS); }\n"
  " else if(a==='lvzoom'){ b.classList.toggle('big'); return; }"),
 ("def build(level, examen, codigo, title, oral, cats, base_css, guion=None, errores=None):",
  "def build(level, examen, codigo, title, oral, cats, base_css, guion=None, errores=None, extra=None):"),
 ("        tasks, mirar = tareas_a2(oral, guion)",
  "        tasks, mirar = tareas_a2(oral, guion)\n"
  "        if vivo_a2: tasks = vivo_a2(tasks, oral, guion, extra)  # extra: imgBase y oralModelos (si no, los del motor)"),
 ("js = JS.replace(\"__DATA__\"",
  "js = JS.replace(\"__JS_VIVO__\", JS_VIVO).replace(\"__DATA__\""),
 ("'<style>' + _enc_html(base_css + CSS)",
  "'<style>' + _enc_html(base_css + CSS + CSS_VIVO)"),
]
for viejo, nuevo in CAMBIOS:
    n = s.count(viejo)
    if n != 1:
        sys.exit("PARADO: en %s el trozo %r aparece %d veces (tiene que aparecer 1). No se ha cambiado nada." % (P, viejo[:60], n))
for viejo, nuevo in CAMBIOS:
    s = s.replace(viejo, nuevo)
s = s.replace("# - Apuntes al vuelo por categorías,",
              "# - A2: guion en vivo (libreta_vivo.py, 23/10/2026): solo la opción o la foto elegida, grande; la tarea 3 paso a paso.\n"
              "# - Apuntes al vuelo por categorías,", 1)
open(P, "w", encoding="utf-8").write(s)
print("ok:", P, "con", len(CAMBIOS), "cambios")
