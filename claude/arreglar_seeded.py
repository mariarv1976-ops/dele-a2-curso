# -*- coding: utf-8 -*-
# ARREGLO DEL MOTOR DE HUECOS (curso DELE A2, 14/10/2026)
# La funcion seeded() que baraja las opciones de los desplegables dejaba la opcion BUENA casi nunca
# en el primer lugar (R04: 0/27/10 en sus 37 huecos). Este script cambia esa linea por la de la R05
# (reparto R04: 10/12/15) en los archivos que le pases: los build_*.py o los .html ya generados.
#
# Uso:  python3 arreglar_seeded.py build_R01_pasados.py build_R02_hay_esta_es.py build_R04_concordancia_posesivos.py
#       python3 arreglar_seeded.py DELEA2_curso_R01_pasados.html ...
# Un archivo ya arreglado se deja como esta. Despues de arreglar un build, volver a ejecutarlo.
import sys

VIEJO = "h=(h*1103515245+12345)>>>0; var r=h%(j+1);"
NUEVO = "h=(Math.imul(h,1103515245)+12345)>>>0; var r=(h>>>16)%(j+1);"

def arreglar(path):
    raw = open(path, "rb").read()
    txt = raw.decode("utf-8")
    n = txt.count(VIEJO)
    if n == 0:
        return "ya arreglado" if NUEVO in txt else "SIN seeded() (no hace falta)"
    open(path, "wb").write(txt.replace(VIEJO, NUEVO).encode("utf-8"))
    return "arreglado (%d)" % n

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__ or "Uso: python3 arreglar_seeded.py archivo [archivo...]"); sys.exit(1)
    for p in sys.argv[1:]:
        print("%-50s %s" % (p, arreglar(p)))
