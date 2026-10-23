# -*- coding: utf-8 -*-
# Añade a curso_tareas.py (MODELOS) la escritura de los modelos completos, copiada de su fuente_Mxx.py.
# Uso: python3 anadir_modelos_corrector.py fuente_M01 fuente_M02 fuente_M07
# Si un modelo ya está (su id A2-Mxx), no lo toca. Se para si no encuentra la lista MODELOS.
import sys, importlib, json, re
P = "curso_tareas.py"
s = open(P, encoding="utf-8").read()
def q(x): return json.dumps(x, ensure_ascii=False)
def lista(xs): return "[" + ", ".join(q(x) for x in xs) + "]"
def br(t): return re.sub(r",?\s*<br>\s*", ", ", t)
NIV = {"de entrada": "de entrada", "nivel alto": "nivel alto", "como el examen": "como el examen"}
nuevos = []
for mod in sys.argv[1:]:
    F = importlib.import_module(mod)
    cid = "A2-M%s" % F.M
    if '"id": "%s"' % cid in s:
        print(cid, "ya estaba"); continue
    E = F.ESCRITA; a, b = E["t2"]["op1"], E["t2"]["op2"]
    txt = (' {"id": %s, "nombre": %s, "pz": "Modelos completos",\n' % (q(cid), q("%s · %s" % (F.NOMBRE, F.NIVEL))) +
      '  "t1": t1(%s,\n           %s,\n           %s,\n           %s),\n' % (q(E["t1"]["instr"]), lista([br(x) for x in E["t1"]["input"]]), q(E["t1"]["lead"]), lista(E["t1"]["pautas"])) +
      '  "t2": {"instr": T2_INSTR, "min": 70, "max": 80,\n' +
      '         "op1": t2(%s,\n                   %s),\n' % (q(a["intro"]), lista(a["pautas"])) +
      '         "op2": t2(%s,\n                   %s,\n                   photos=%s,\n                   intro2=%s)}},\n' % (q(b["intro"]), lista(b["pautas"]), lista(b["photos"]), q(b.get("intro2", ""))))
    nuevos.append(txt); print(cid, "añadido")
if nuevos:
    m = re.search(r"^MODELOS = \[\n(.*?)^\]\n", s, re.M | re.S)
    if not m: sys.exit("PARADO: no encuentro MODELOS = [...]")
    s = s[:m.end(1)] + "".join(nuevos) + s[m.end(1):]
    compile(s, P, "exec")
    open(P, "w", encoding="utf-8").write(s)
    import importlib as I; T = I.import_module("curso_tareas")
    print("MODELOS:", [x["id"] for x in T.MODELOS])
