# -*- coding: utf-8 -*-
# PROMPTS Y NOMBRES DE LAS FOTOS DEL TALLER DE ESCRITURA (Modulo 3 del curso de preparacion DELE A2)
# Uso: python3 build_M3_fotos.py
#  -> M3_prompts_imagenes.txt  (un prompt por lamina: un triptico con las tres fotos; orden de nombres.txt)
#  -> nombres.txt              (para la accion rapida "Imagen DELE": Documentos/IMAGENES_2ST/nombres.txt)
#  -> M3_laminas_fotos.txt     (lista de laminas con fotos: en que piezas sale cada una)
# 13/10/2026 (Maria): nombres que dicen que foto es (M3_01_bio_rosa_cocinera) y en nombres.txt que se ve en cada panel.
# Lee las laminas de los cinco bancos. Una lamina que sale en varias piezas tiene UNA sola imagen.
# Estilo, nombres y comprobaciones: fotos_M3.py.
import re
import fotos_M3 as FT
import banco_frases_M3 as BF, banco_pautas_M3 as BP, banco_revision_M3 as BR, banco_modelos_M3 as BM, banco_banda1_M3 as BB

PIEZAS = ["Kit de frases", "Las pautas", "Revisión final", "Textos modelo", "Banda 1 a banda 2"]
KIT, PAU, REV, MOD, B1 = PIEZAS

# (lamina, de donde sale, en que piezas aparece)
L = []
for t in BF.TIPOS:
    L.append((t["lamina"], "Kit · %s (ejemplo)" % t["tab"], [KIT]))
    L.append((t["ahora"], "Kit · %s (Ahora tú)" % t["tab"], [KIT, REV, MOD]))      # rev y modelos lo traen en «Ahora tú»
for x in BP.TEXTOS: L.append((x["lamina"], "Pautas · ¿Qué falta? (%s, %s)" % (x["tipo"], x["autor"]), [PAU]))
for a in BP.AHORA: L.append((a["lamina"], "Pautas · Ahora tú (%s)" % a["n"], [PAU, REV, MOD]))
for x in BR.RELOJ: L.append((x["lamina"], "Revisión · A contrarreloj (%s, %s)" % (x["tipo"], x["autor"]), [REV]))
for t in BM.TIPOS: L.append((t["lamina"], "Modelos · Textos modelo (%s)" % t["tab"], [MOD]))
for a in BM.APRUEBA: L.append((a["lamina"], "Modelos · ¿Aprueba? (%s, %s)" % (a["tipo"], a["autor"]), [MOD]))
for a in BM.AHORA_NUEVAS: L.append((a["lamina"], "Modelos · Ahora tú, lámina nueva (%s)" % a["n"], [MOD]))
L.append((BB.DEMO["lamina"], "Banda 1 · Operación rescate", [B1]))
for r in BB.RESCATE: L.append((r["lamina"], "Banda 1 · Rescata textos (%s, %s)" % (r["tipo"], r["autor"]), [B1]))

TANDA = []  # [(img, lamina, origen, piezas)]
vistos = {}
for l, origen, piezas in L:
    if not l.get("photos"): continue
    FT.check(l, origen)
    if l["img"] in vistos:
        assert vistos[l["img"]][1] is l, "%s: el mismo nombre en dos laminas distintas" % l["img"]
        continue
    vistos[l["img"]] = (origen, l)
    TANDA.append((l["img"], l, origen, piezas))
nums = [img[3:5] for img, _, _, _ in TANDA]
assert nums == ["%02d" % (i + 1) for i in range(len(TANDA))], "Los numeros de las imagenes van seguidos y en orden: %s" % nums
nfotos = sum(len(l["photos"]) for _, l, _, _ in TANDA)

def ascii_desc(s):
    s = s.replace("ñ", "n").replace("Ñ", "N")
    for a, b in zip("áéíóúüÁÉÍÓÚÜ", "aeiouuAEIOUU"): s = s.replace(a, b)
    return re.sub(r"[\"'«»|]", "", s)

with open("M3_laminas_fotos.txt", "w", encoding="utf-8") as fp:
    fp.write("LÁMINAS CON FOTOS DEL TALLER DE ESCRITURA (Módulo 3) · %d láminas = %d trípticos (%d fotos)\n" % (len(TANDA), len(TANDA), nfotos))
    fp.write("Imágenes en WordPress, carpeta del mes %s\n\n" % FT.MES_WP)
    for img, l, origen, piezas in TANDA:
        fp.write("%s.jpg  ·  %s\n   Lámina: %s  ·  Sale en: %s\n" % (img, l["rotulo"], origen, ", ".join(piezas)))

with open("M3_prompts_imagenes.txt", "w", encoding="utf-8") as fp:
    fp.write("PROMPTS DE LAS FOTOS · TALLER DE ESCRITURA (curso DELE A2, Módulo 3)\n")
    fp.write("%d trípticos (%d fotos) · una imagen por lámina, 3:1, tres paneles cuadrados iguales · mismo orden que nombres.txt\n" % (len(TANDA), nfotos))
    fp.write("Como Uxx_escrita.jpg de los simulacros: al generar las tres fotos a la vez, la persona sale igual en las tres.\n")
    fp.write("Fotos reales y naturales: sin HDR ni contraste, luz plana, posturas naturales, nadie posa.\n")
    fp.write("Si la herramienta no da 3:1, elige el formato más ancho y recorta a 3:1 sin cortar los paneles (que queden tres tercios iguales:\n")
    fp.write("en el móvil, la página recorta cada tercio).\n")
    fp.write("Después: acción rápida «Imagen DELE» (%d px, %d KB) y subir a WordPress, carpeta del mes %s.\n\n" % (FT.ANCHO, FT.KB, FT.MES_WP))
    for img, l, origen, piezas in TANDA:
        fp.write("=" * 78 + "\n%s.jpg\n%s\nLámina: %s  ·  Sale en: %s\n" % (img, l["rotulo"], origen, ", ".join(piezas)))
        fp.write("".join("  Foto %d: %s\n" % (i + 1, a) for i, a in enumerate(l["photos"])) + "\n")
        fp.write(FT.prompt(l) + "\n\n")

with open("nombres.txt", "w", encoding="utf-8") as fp:
    fp.write("CARPETA: DELE_A2_curso\n")
    for img, l, origen, piezas in TANDA:
        fp.write("%s | %d | %d | %s\n" % (img, FT.ANCHO, FT.KB, ascii_desc(l["rotulo"])))

print("ok · %d trípticos (%d fotos) · M3_prompts_imagenes.txt, nombres.txt, M3_laminas_fotos.txt" % (len(TANDA), nfotos))
for img, l, origen, piezas in TANDA: print("  %-22s %s" % (img, ", ".join(piezas)))
