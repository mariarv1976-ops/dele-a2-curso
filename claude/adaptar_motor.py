# -*- coding: utf-8 -*-
# Crea DELE_A2_motor_modelo.py a partir de DELE_A2_motor_simulacro.py (sin tocar el original).
# Uso (en la carpeta del motor, con motor_modelo_extra.py al lado):
#     python3 adaptar_motor.py
#     python3 DELE_A2_motor_modelo.py DELEA2_curso_M06_datos
# Cada cambio busca un trozo exacto del motor y se para si no lo encuentra (o si lo encuentra dos veces),
# así nunca sale un motor a medias. Si el motor original cambia, se vuelve a ejecutar este script.
# El motor adaptado sigue sirviendo para las unidades: lo nuevo solo se activa con "modelo": true en los datos.
# 20/10/2026 (M7): al final de Resultados, el perfil del modelo y cómo leer la nota (xPerfil, en motor_modelo_extra.py).
import sys
SRC = sys.argv[1] if len(sys.argv) > 1 else "DELE_A2_motor_simulacro.py"
DST = sys.argv[2] if len(sys.argv) > 2 else "DELE_A2_motor_modelo.py"
s = open(SRC, encoding="utf-8").read()

CAMBIOS = [
 # --- Python: código del examen, título, archivos, noindex y piezas nuevas ---
 ('EXAMEN = "A2-U" + DATA["unit"]',
  'EXAMEN = DATA.get("codigoExamen") or ("A2-U" + DATA["unit"])'),
 ('\nHTML_BODY = r"""',
  '\nfrom motor_modelo_extra import CSS_MODELO, JS_MODELO\nCSS += CSS_MODELO\nHTML_BODY = r"""'),
 ("H1 = 'Simulacro DELE A2 · Unidad %d: %s' % (int(DATA['unit']), DATA['title'])",
  "H1 = DATA.get('h1') or ('Simulacro DELE A2 · Unidad %d: %s' % (int(DATA['unit']), DATA['title']))"),
 ("js = JS.replace('__DATA__', json.dumps(DATA, ensure_ascii=True))",
  "js = JS.replace('__JS_MODELO__', JS_MODELO).replace('__DATA__', json.dumps(DATA, ensure_ascii=True))"),
 ("'<title>'+enc_html(H1)",
  "'<meta name=\"robots\" content=\"noindex, nofollow\">'+'<title>'+enc_html(H1)"),
 ("open('DELEA2_F1_U%s_simulacro.html' % DATA['unit'],'w',encoding='ascii')",
  "open(DATA.get('fileHtml') or ('DELEA2_F1_U%s_simulacro.html' % DATA['unit']),'w',encoding='ascii')"),
 ("open('DELEA2_F1_U%s_oral_profesora.html' % DATA['unit'],'w',encoding='ascii')",
  "open(DATA.get('fileProf') or ('DELEA2_F1_U%s_oral_profesora.html' % DATA['unit']),'w',encoding='ascii')"),
 # --- JS: estado, tiempos de cada prueba, textos ---
 ("name:'', oral:false};}",
  "name:'', oral:false, crono:{}, notas:{}, fin:{}};}"),
 ("S.done[part]=true; save(); go(",
  "S.done[part]=true; S.fin=S.fin||{}; S.fin[part]=Date.now(); save(); go("),
 ("function(){ S.done.escrita=true; save(); render();",
  "function(){ S.done.escrita=true; S.fin=S.fin||{}; S.fin.escrita=Date.now(); save(); render();"),
 ("o += '<h3>Qué repasas en esta unidad</h3><ul>';",
  "o += '<h3>'+(D.recLabel||'Qué repasas en esta unidad')+'</h3><ul>';"),
 ("'SIMULACRO DELE A2 - UNIDAD '+D.unit+': '+D.title",
  "(D.packHead||('SIMULACRO DELE A2 - UNIDAD '+D.unit))+': '+D.title"),
 # --- JS: resultados (grupos 30/50, fichas, talleres, control de progreso, perfil del modelo) ---
 ("o += '<p class=\"muted\">Referencia DELE: para el APTO necesitas aproximadamente un 60 % en cada grupo de pruebas.</p>';",
  "o += xGrupos(R);"),
 ("Mini reto: '+c.reto+'</div></div>'",
  "Mini reto: '+c.reto+'</div>'+xFichas(c)+'</div>'"),
 ("o += '<h3>Transcripciones de los audios</h3>",
  "o += xTalleres()+xCrono()+xPerfil(R);\n o += '<h3>Transcripciones de los audios</h3>"),
 ("L.push('  Mini reto: '+plain(d.reto));",
  "L.push('  Mini reto: '+plain(d.reto));\n  xPackFichas(L, d);"),
 ("return L.join('\\n'); }\nfunction packVocab",
  "xPackExtra(L, R); return L.join('\\n'); }\nfunction packVocab"),
 # --- JS: textos modelo de la escritura y de la oral ---
 ("sendRow('escrita')+'</div>';",
  "sendRow('escrita')+'</div>'+xModelosEsc();"),
 ("o += '<p class=\"muted small noprint\" style=\"margin:28px 0 0\">",
  "o += xModelosOral();\n o += '<p class=\"muted small noprint\" style=\"margin:28px 0 0\">"),
 ("/* ---------- render ---------- */",
  "__JS_MODELO__\n/* ---------- render ---------- */"),
]
for viejo, nuevo in CAMBIOS:
    n = s.count(viejo)
    if n != 1:
        sys.exit("PARADO: en %s el trozo %r aparece %d veces (tiene que aparecer 1). No se ha creado nada." % (SRC, viejo[:70], n))
    s = s.replace(viejo, nuevo)
s = s.replace("# MOTOR DEL SIMULACRO DELE A2 (2spanishteachers.com)",
              "# MOTOR DE LOS MODELOS COMPLETOS DEL CURSO DELE A2 · generado con adaptar_motor.py desde\n"
              "# DELE_A2_motor_simulacro.py (no editar a mano: cambiar el original o motor_modelo_extra.py y volver a generar).\n"
              "# MOTOR DEL SIMULACRO DELE A2 (2spanishteachers.com)", 1)
open(DST, "w", encoding="utf-8").write(s)
print("ok:", DST, "con", len(CAMBIOS), "cambios")
