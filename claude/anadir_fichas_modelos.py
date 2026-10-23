# -*- coding: utf-8 -*-
# Anade las fichas de remedio R08, R10, R13 y R14a a los contenidos de los modelos completos (fuente_Mxx.py).
# Uso (en la carpeta de las fuentes):   python3 anadir_fichas_modelos.py fuente_M01.py fuente_M06.py fuente_M07.py
# Despues, volver a construir cada modelo (build_modelo.py -> adaptar_motor.py -> DELE_A2_motor_modelo.py) y subir
# su DELEA2_curso_Mxx_examen.html: en Resultados, "Que tienes que repasar" enlaza tambien las fichas nuevas.
# Seguro: primero comprueba todo y solo escribe si todo cuadra; si una fuente ya tiene las fichas, no la toca.
# Para el M2 y los siguientes: si se copia una fuente ya arreglada, ya las lleva; si no, pasarle este script.
import re, sys

NUEVAS = {
    "R08": ("Conectores: las flechas entre frases", "DELEA2_curso_R08_conectores.html"),
    "R10": ("Lo, la, le: el paquete y el destinatario", "DELEA2_curso_R10_lo_la_le.html"),
    "R13": ("Las funciones de los correos", "DELEA2_curso_R13_formulas_correo.html"),
    "R14a": ("Vocabulario en escenas (1): la casa y el día a día", "DELEA2_curso_R14a_vocabulario_casa_dia_a_dia.html"),
}
# contenido -> fichas que se anaden (detras de las que ya tiene)
ANADIR = {
    "personas": ["R10", "R14a"],   # descripcion de personas, familia; pronombres para no repetir
    "opinion": ["R08"],            # dar la opinion con porque / por eso / pero / ademas
    "planes": ["R13", "R08"],      # invitar, aceptar, rechazar, proponer; "al final" = el plan cambio
    "cantidad": ["R14a"],          # compras, tiendas, precios
    "lugares": ["R14a"],           # la casa, las tiendas del barrio
}

def arreglar(path):
    s = open(path, encoding="utf-8").read()
    orig = s
    # 1. el diccionario R: las fichas nuevas, justo antes de "M0"
    m = re.search(r"^R = \{\n(.*?)^\}\n", s, re.M | re.S)
    if not m: return "PARADO: no encuentro el diccionario R = {...}"
    bloque = m.group(1)
    if '"M0":' not in bloque: return "PARADO: el diccionario R no tiene la entrada \"M0\""
    faltan = [k for k in NUEVAS if '"%s":' % k not in bloque]
    if faltan:
        lineas = "".join(' "%s": ("%s", "%s"),\n' % (k, NUEVAS[k][0], NUEVAS[k][1]) for k in faltan)
        i = bloque.index(' "M0":')
        bloque = bloque[:i] + lineas + bloque[i:]
        s = s[:m.start(1)] + bloque + s[m.end(1):]
    # 2. los contenidos: "nombre": {... "fichas": F("R01", ...)}
    for cat, ks in ANADIR.items():
        mc = re.search(r'^ "%s": \{' % cat, s, re.M)
        if not mc: return "PARADO: no encuentro el contenido \"%s\" en CATS" % cat
        mf = re.compile(r'"fichas": F\(([^)]*)\)').search(s, mc.end())
        sig = re.compile(r'^ "[a-z_]+": \{', re.M).search(s, mc.end())
        if not mf or (sig and mf.start() > sig.start()): return "PARADO: el contenido \"%s\" no tiene \"fichas\": F(...)" % cat
        tiene = re.findall(r'"([^"]+)"', mf.group(1))
        nuevas = tiene + [k for k in ks if k not in tiene]
        if nuevas != tiene:
            s = s[:mf.start(1)] + ", ".join('"%s"' % k for k in nuevas) + s[mf.end(1):]
    if s == orig: return "ya estaba: no cambia nada"
    # 3. comprobar que sigue siendo Python valido y que F() encuentra todas las fichas
    try: compile(s, path, "exec")
    except SyntaxError as e: return "PARADO: el resultado no es Python valido (%s)" % e
    open(path, "w", encoding="utf-8").write(s)
    return "ok: %s en R y fichas nuevas en %s" % (", ".join(faltan) or "nada nuevo", ", ".join(ANADIR))

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__ or "Uso: python3 anadir_fichas_modelos.py fuente_M01.py fuente_M06.py ...")
    mal = False
    for p in sys.argv[1:]:
        r = arreglar(p); print(p, "->", r); mal = mal or r.startswith("PARADO")
    if mal: sys.exit(1)
