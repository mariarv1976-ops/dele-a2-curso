# -*- coding: utf-8 -*-
# Genera a partir de fuente_Uxx.py: datos.py, cuadernillos, guion de audio (las 4 tareas de auditiva:
# pics T1, radio T2, friends T3, msgs T4), nombres.txt y Uxx_prompts_imagenes.txt.
# En la fuente: MES_WP = "2026/10" (carpeta del mes en que se suben audios e imágenes a WordPress),
# PERFIL_FOTOS y SITUACIONES_USADAS (variedad de las fotos, desde la U05).
# Oct. 2026: las marcas de emoción de v3 ([laughs], [sighs]...) van solo al guion; las transcripciones salen limpias.
# Oct. 2026: el narrador dice «Ejemplo», nunca «Conversación/Audio/Mensaje cero» (pronuncia «chero»).
import sys, json, importlib, re, os
sys.path.insert(0, '.')
F = importlib.import_module(sys.argv[1])
U = F.U; OUT = sys.argv[2] if len(sys.argv) > 2 else '.'
LET = 'ABCDEFGHIJK'
NUM = ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','once','doce','trece','catorce','quince','dieciséis','diecisiete','dieciocho','diecinueve','veinte','veintiuno','veintidós','veintitrés','veinticuatro','veinticinco']
WP = "https://2spanishteachers.com/wp-content/uploads/"
if getattr(F, "MES_WP", None): base = WP + F.MES_WP.strip("/") + "/"           # carpeta del mes de WordPress (en la fuente)
elif getattr(F, "BASE", None): base = F.BASE                                     # fuentes antiguas (U04)
else: base = WP + "2026/09/"; print("AVISO: la fuente no tiene MES_WP; uso 2026/09 (U01-U03)")
U2 = importlib.import_module('DELEA2_F1_U02_datos').DATA
EST = dict(U2['estrategias']); EST.update(getattr(F, 'ESTRATEGIAS_NUEVAS', {}))
LECT = F.LECTURA; AUD = F.AUDITIVA

def limpio(t):   # quita las marcas de emoción de ElevenLabs v3 ([laughs], [sighs]...): van al guion, no a las transcripciones
    return re.sub(r"\s*\[[a-zA-Z ]+\]\s*", " ", t).strip()
def tr_conv(c):
    return ['(' + c['pres'] + ')'] + ['%s: %s' % (r, limpio(t)) for r, v, t in c['lines']]
def tr_mono(c):
    return ['%s: %s' % (c['lab'], limpio(c['text']))]
def clean_item(it, extra=()):
    d = {k: v for k, v in it.items() if k not in ('pc', 'pres', 'lines', 'prompt', 'solucion', 'voice', 'text', 'lab', 'sound') + tuple(extra)}
    return d

# ---------- fotos con variedad real (desde la U05) ----------
PF = getattr(F, "PERFIL_FOTOS", None); SU = getattr(F, "SITUACIONES_USADAS", {})
CAMPOS = ("situacion", "personas", "edades", "aspecto", "espacio", "lugar", "momento", "estacion", "tiempo", "gente", "accion", "fondo", "objetos", "problema")
if PF:
    for k in ("oral_foto1", "oral_foto2", "escrita"):
        falta = [c for c in CAMPOS if not PF.get(k, {}).get(c)]
        assert not falta, "PERFIL_FOTOS[%s]: faltan %s" % (k, falta)
    usadas = {x.lower() for u, l in SU.items() if u != "U" + U for x in l}
    for k in ("oral_foto1", "oral_foto2"):
        assert PF[k]["situacion"].lower() not in usadas, "situación ya usada: " + PF[k]["situacion"]
    assert [x.lower() for x in SU.get("U" + U, [])] == [PF["oral_foto1"]["situacion"].lower(), PF["oral_foto2"]["situacion"].lower()], "SITUACIONES_USADAS['U%s'] tiene que ser [foto1, foto2]" % U
    a, b = PF["oral_foto1"], PF["oral_foto2"]
    dif = [c for c in ("espacio", "momento", "estacion", "tiempo", "gente", "personas") if a[c] != b[c]]
    assert len(dif) >= 4, "las dos fotos de la oral se parecen demasiado (solo cambian: %s)" % dif
else:
    print("AVISO: la fuente no tiene PERFIL_FOTOS (normal en U01-U04)")

# ---------- datos ----------
def datos_task(tk):
    d = {k: v for k, v in tk.items() if k not in ('items', 'example', 'lines', 'voices', 'who')}
    if tk['type'] == 'pics':
        ex = tk['example']
        d['example'] = {'q': ex['q'], 'o': ex['o'], 'ok': ex['ok'], 'img': ex['img'], 'tr': tr_conv(ex)}
        d['items'] = [dict(clean_item(it), tr=tr_conv(it)) for it in tk['items']]
    elif tk['type'] == 'friends':
        d['tr'] = ['%s: %s' % (r.capitalize(), limpio(t)) for r, t in tk['lines']]
        d['trLabel'] = 'Conversación entre %s y %s' % tuple(tk['who'])
        d['items'] = [clean_item(it) for it in tk['items']]
    elif tk['type'] in ('radio', 'msgs'):
        d['example'] = dict(clean_item(tk['example']), tr=tr_mono(tk['example']))
        if tk['type'] == 'msgs': d['exLabel'] = 'Mensaje 0 (ejemplo)'
        d['items'] = [dict(clean_item(it), tr=tr_mono(it)) for it in tk['items']]
    else:
        if 'example' in tk: d['example'] = tk['example']
        d['items'] = [clean_item(it) for it in tk['items']]
    return d
DATA = {"unit": U, "title": F.TITLE, "storageKey": "dele_a2_f1_u%s_v1" % U, "email": U2['email'],
 "audio": {"t%d" % tk['n']: base + "DELEA2_F1_U%s_CA_T%d.m4a" % (U, tk['n']) for tk in AUD}, "imgBase": base,
 "imgs": {"portada": "U%s_portada.jpg" % U, "oralLock": "U%s_oral.jpg" % U},
 "recordatorio": F.RECORDATORIO, "tipsInicio": F.TIPS_INICIO, "cats": F.CATS, "estrategias": EST,
 "lectura": {"tasks": [datos_task(t) for t in LECT]}, "auditiva": {"tasks": [datos_task(t) for t in AUD]},
 "escrita": F.ESCRITA, "oral": F.ORAL,
 "profesora": {"guion": getattr(F, "GUION_ENTREVISTADOR", ""), "errores": getattr(F, "ERRORES", "")}}
if getattr(F, 'TIEMPOS', None): DATA['tiempos'] = F.TIEMPOS
for tk in LECT + AUD:
    for it in tk['items']:
        for c in it['cats']: assert c in F.CATS, c
        assert it['es'] in EST, it['es']
open(os.path.join(OUT, 'DELEA2_F1_U%s_datos.py' % U), 'w').write("# -*- coding: utf-8 -*-\n# DATOS DE LA UNIDAD %s (fase 1) · generado con build_unidad.py\nDATA = %s\n" % (U, json.dumps(DATA, ensure_ascii=True, indent=1)))

# ---------- cuadernillo del estudiante ----------
def plain(t): return re.sub(r'<br>', '\n', re.sub(r'<(?!br)[^>]+>', '', t))
nL = sum(len(t['items']) for t in LECT); nA = sum(len(t['items']) for t in AUD)
tL = getattr(F, 'TIEMPOS', {}).get('lectura', 30); tA = getattr(F, 'TIEMPOS', {}).get('auditiva', 20)
E = []
w = E.append
w("SIMULACRO DELE A2 — UNIDAD %s: %s" % (int(U), F.TITLE))
w("Cuadernillo del estudiante (DELEA2_F1_U%s_estudiante.txt)" % U); w("=" * 75)
w("Material de preparación original. No es un examen oficial y es independiente\ndel Instituto Cervantes.\n")
w("QUÉ CONTIENE")
w("  1. Comprensión de lectura ........ Tareas %s · %d preguntas · %d minutos" % ((', '.join(str(t['n']) for t in LECT[:-1]) + ' y ' + str(LECT[-1]['n']) if len(LECT) > 1 else str(LECT[0]['n'])), nL, tL))
w("  2. Comprensión auditiva .......... Tareas %s · %d preguntas · %d minutos" % ((', '.join(str(t['n']) for t in AUD[:-1]) + ' y ' + str(AUD[-1]['n']) if len(AUD) > 1 else str(AUD[0]['n'])), nA, tA))
w("  3. Expresión e interacción escritas · Tareas 1 y 2 · 45 minutos")
w("  4. Resultados y corrección · 5. Vocabulario y dudas (sin tiempo)")
w("  6. Expresión e interacción orales · prueba completa, en clase con tu profesora\n")
w("QUÉ REPASAS EN ESTA UNIDAD"); [w("  · " + r) for r in F.RECORDATORIO]; w("")
w("TIPS DE ARRANQUE"); [w("  · " + plain(r)) for r in F.TIPS_INICIO]; w("")
w("=" * 75); w("PRUEBA 1. COMPRENSIÓN DE LECTURA"); w("Esta prueba tiene %d tareas. Usted debe responder a %d preguntas.\nLa duración es de %d minutos. Marque sus opciones únicamente en la Hoja de\nrespuestas." % (len(LECT), nL, tL)); w("=" * 75)
def opts(it, ind="    "):
    for i, o in enumerate(it['o']): w("%s%s) %s" % (ind, LET[i], o))
for tk in LECT:
    w("\nTAREA %d\nINSTRUCCIONES\n%s Marque las opciones elegidas en la Hoja de\nrespuestas.\n(Tip: %s)\n" % (tk['n'], tk['instr'], plain(tk.get('tip', ''))))
    if tk['type'] == 'mail':
        [w("  " + h) for h in tk['head']]; w("")
        [w(plain(p) + "\n") for p in tk['body']]
        w("PREGUNTAS")
        for it in tk['items']: w("%d. %s" % (it['n'], it['q'])); opts(it)
    elif tk['type'] == 'people':
        w("PREGUNTAS" + " " * 40 + "   ".join("%s. %s" % (LET[i], t['name'].upper()) for i, t in enumerate(tk['texts'])))
        for it in tk['items']: w("%d. %s" % (it['n'], it['q']))
        for i, t in enumerate(tk['texts']): w("\n%s. %s\n%s" % (LET[i], t['name'].upper(), t['body']))
    elif tk['type'] == 'long':
        w(tk['title'].upper()); w(tk.get('sub', '') + "\n"); [w(p + "\n") for p in tk['body']]
        w("PREGUNTAS")
        for it in tk['items']: w("%d. %s" % (it['n'], it['q'])); opts(it)
    elif tk['type'] == 'ads':
        ex = tk['example']; w("EJEMPLO · TEXTO 0 · %s\n%s\n0. %s" % (ex['title'], plain(ex['body']), ex['q'])); opts(ex); w("   " + ex['why'] + "\n")
        for i, it in enumerate(tk['items']): w("TEXTO %d · %s\n%s\n%d. %s" % (i + 1, it['title'], plain(it['body']), it['n'], it['q'])); opts(it); w("")
w("\n" + "=" * 75); w("PRUEBA 2. COMPRENSIÓN AUDITIVA"); w("Esta prueba tiene %d tareas. Usted debe responder a %d preguntas.\nLa duración es de %d minutos, aproximadamente.\n(Pon el audio de cada tarea al principio y no lo pares.)" % (len(AUD), nA, tA)); w("=" * 75)
for tk in AUD:
    w("\nTAREA %d   [audio DELEA2_F1_U%s_CA_T%d]\nINSTRUCCIONES\n%s Marque las opciones elegidas en la Hoja de\nrespuestas.\n" % (tk['n'], U, tk['n'], tk['instr']))
    if tk['type'] == 'pics':
        ex = tk['example']; w("Conversación 0 (ejemplo). %s" % ex['q']); opts(ex, "   (imagen) "); w("   La opción correcta es la %s.\n" % LET[ex['ok']])
        for it in tk['items']: w("%s. %s" % (it['n'], it['q'])); opts(it, "   (imagen) "); w("")
    elif tk['type'] == 'friends':
        w(" " * 52 + "A. %s  B. %s  C. NINGUNO" % tuple(x.upper() for x in tk['who']))
        for it in tk['items']: w("%d. %s" % (it['n'], it['q']))
    elif tk['type'] == 'msgs':
        w("ENUNCIADOS"); [w("%s. %s" % (LET[i], e)) for i, e in enumerate(tk['enun'])]
        w("Mensaje 0 (ejemplo): %s" % LET[tk['example']['ok']])
        for it in tk['items']: w("%d. %s  ____" % (it['n'], it['q']))
    elif tk['type'] == 'radio':
        ex = tk['example']; w("0. %s" % ex['q']); opts(ex); w("")
        for it in tk['items']: w("%d. %s" % (it['n'], it['q'])); opts(it); w("")
w("")
Es = F.ESCRITA
w("=" * 75); w("PRUEBA 3. EXPRESIÓN E INTERACCIÓN ESCRITAS · 45 minutos"); w("=" * 75)
w("CONSEJO: cuenta tus palabras con los ojos. Escribe unas 10 palabras por línea:\ntarea 1 = 6 o 7 líneas; tarea 2 = 7 u 8 líneas.\n")
w("TAREA 1\n" + Es['t1']['instr']); [w("  | " + l) for p in Es['t1']['input'] for l in plain(p).split("\n")]
w(Es['t1'].get('lead', 'Conteste. En el correo tiene que:')); [w("  - " + p) for p in Es['t1']['pautas']]
w("Número de palabras recomendadas: entre %d y %d.\n" % (Es['t1']['min'], Es['t1']['max']))
w("TAREA 2\n" + Es['t2']['instr'])
o1 = Es['t2']['op1']; w("\nOPCIÓN 1\n" + o1['intro']); [w("  - " + p) for p in o1['pautas']]
o2 = Es['t2']['op2']; w("\nOPCIÓN 2\n" + o2['intro'])
for i, p in enumerate(o2.get('photos', [])): w("  Foto %d. %s" % (i + 1, p))
[w("  · " + x) for x in o2.get('ficha', [])]
w(o2['intro2']); [w("  - " + p) for p in o2['pautas']]
w("Número de palabras recomendadas: entre %d y %d.\n" % (Es['t2']['min'], Es['t2']['max']))
w("=" * 75); w("VOCABULARIO Y DUDAS (sin tiempo · después de la escritura, con los textos y las transcripciones)"); w("=" * 75)
w("Palabras nuevas de los textos y los audios, con una frase tuya:\n  Palabra ............  Mi frase ..............................\n  Palabra ............  Mi frase ..............................\nDudas para tu profesora: ..........................................\n")
O = F.ORAL
w("=" * 75); w("PRUEBA 4. EXPRESIÓN E INTERACCIÓN ORALES (en clase)\n12 minutos de preparación para las tres tareas."); w("=" * 75)
w("TAREA 1. MONÓLOGO (2-3 minutos). " + O['t1']['instr'])
for op in O['t1']['ops']: w("  " + op['title'].upper()); [w("    - " + p) for p in op['pautas']]
w("\nTAREA 2. DESCRIPCIÓN DE UNA FOTOGRAFÍA (2-3 minutos). " + O['t2']['instr'])
for f in O['t2']['fotos']: w("  %s: %s" % (f['title'].upper(), f['desc']))
w("  Hable de:"); [w("    - " + p) for p in O['t2']['pautas']]
w("\nTAREA 3. DIÁLOGO (3-4 minutos). " + O['t3']['instr'])
for op in O['t3']['ops']: w("  " + op['title'].upper() + ": " + op['intro']); [w("    - " + p) for p in op['pautas']]
w("\n" + "=" * 75); w("HOJA DE RESPUESTAS"); w("=" * 75)
for nom, tasks in (("COMPRENSIÓN DE LECTURA", LECT), ("COMPRENSIÓN AUDITIVA", AUD)):
    w(nom)
    for tk in tasks:
        if tk['type'] == 'msgs': w("  Tarea %d:  " % tk['n'] + "  ".join("%d ___" % it['n'] for it in tk['items']) + "  (A-K)")
        else: w("  Tarea %d:  " % tk['n'] + "  ".join("%d [A][B][C]" % it['n'] for it in tk['items']))
open(os.path.join(OUT, 'DELEA2_F1_U%s_estudiante.txt' % U), 'w').write("\n".join(E) + "\n")

# ---------- cuadernillo de la profesora ----------
P = []; p = P.append
p("SIMULACRO DELE A2 — UNIDAD %s: %s" % (int(U), F.TITLE)); p("Cuadernillo de la profesora · USO INTERNO"); p("=" * 75)
p("Tareas: lectura %s · auditiva %s · código oral: en el panel de la profesora (examen A2-U%s)" % (' + '.join('T%d' % t['n'] for t in LECT), ' + '.join('T%d' % t['n'] for t in AUD), U))
p("\n1) CLAVE")
for nom, tasks in (("LECTURA", LECT), ("AUDITIVA", AUD)):
    for tk in tasks:
        ex = ("0 %s (ej.) · " % LET[tk['example']['ok']]) if 'example' in tk and 'ok' in tk['example'] else ""
        p("  %s T%d: %s%s" % (nom, tk['n'], ex, " · ".join("%d %s" % (it['n'], LET[it['ok']]) for it in tk['items'])))
p("\n2) METADATOS POR ÍTEM")
for nom, tasks in (("CL", LECT), ("CA", AUD)):
    for tk in tasks:
        for it in tk['items']:
            p("  %s-T%d · %d · clave %s · %s · %s" % (nom, tk['n'], it['n'], LET[it['ok']], it['es'], it.get('pc', '')))
            p("     Contenido: %s" % " / ".join(F.CATS[c]['name'] for c in it['cats']))
            p("     Justificación: %s" % it['why'])
p("\n3) TRANSCRIPCIONES")
for tk in AUD:
    p("  TAREA %d" % tk['n'])
    if tk['type'] == 'pics':
        for c in [tk['example']] + tk['items']:
            p("   %s — %s" % (c.get('conv', 'Conversación 0 (ejemplo)'), c['q'])); [p("     " + l) for l in tr_conv(c)]
    elif tk['type'] == 'friends':
        [p("     %s: %s" % (r.capitalize(), limpio(t))) for r, t in tk['lines']]
    elif tk['type'] in ('radio', 'msgs'):
        nom0 = 'Audio 0 (ejemplo)' if tk['type'] == 'radio' else 'Mensaje 0 (ejemplo)'
        for c in [tk['example']] + tk['items']:
            cl = (" · ítem %d, clave %s" % (c['n'], LET[c['ok']])) if 'n' in c else ""
            p("   %s%s · voz %s" % (c.get('conv', nom0), cl, c['voice'])); p("     %s: %s" % (c['lab'], limpio(c['text'])))
p("\n4) MAPA DE CONTENIDOS")
for k, c in F.CATS.items():
    its = ["%s%d" % ('L' if tk in LECT else 'A', it['n']) for tk in LECT + AUD for it in tk['items'] if k in it['cats']]
    p("  %-12s %s: %s" % (k, c['name'], ", ".join(its)))
p("\n5) ORAL · GUION DEL ENTREVISTADOR"); p(F.GUION_ENTREVISTADOR)
p("\n6) ERRORES ESPERABLES"); p(F.ERRORES)
p("\n7) IMÁGENES (prompts en U%s_prompts_imagenes.txt · lista en nombres.txt)" % U)
if PF:
    for k in ("oral_foto1", "oral_foto2", "escrita"):
        f = PF[k]; p("  %s · %s" % (k, f["situacion"].upper()))
        for c in CAMPOS[1:]: p("     %-9s %s" % (c + ":", f[c]))
    p("  Situaciones ya usadas en la oral: " + " · ".join("%s %s" % (u, ", ".join(l)) for u, l in sorted(SU.items())))
open(os.path.join(OUT, 'DELEA2_F1_U%s_profesora.txt' % U), 'w').write("\n".join(P) + "\n")

# ---------- guion de audio ----------
G = []; g = G.append
g("# GUION DE AUDIO · UNIDAD %s · generado con build_unidad.py" % U)
g("# Formato: \"VOZ: texto\" · [n] = silencio · \"# ARCHIVO nombre\" · \"SONIDO n: descripcion\"")
if getattr(F, 'REPARTO', ''): g(F.REPARTO)
first = True
CH = "SONIDO 2: Two-tone ding-dong chime of a public address announcement system, clean and clear, no voices, no background noise"
BP = "SONIDO 1: Single short electronic answering machine beep, clean, no background noise"
LETRA = ['a', 'be', 'ce', 'de', 'e', 'efe', 'ge', 'hache', 'i', 'jota', 'ka']
def mono(c):
    if c.get('sound'): g(c['sound'])
    g("%s: %s" % (c['voice'], c['text']))
def dlg(c):
    for r, v, t in c['lines']:
        if r == 'SONIDO': g(v)
        else: g("%s: %s" % (v, t))
for tk in AUD:
    g("\n\n# ARCHIVO DELEA2_F1_U%s_CA_T%d" % (U, tk['n']))
    if first:
        g("0: Prueba de comprensión auditiva. Escuche con atención todas las instrucciones. Esta prueba contiene %s tareas. Usted debe responder a %s preguntas. La duración es de %s minutos, aproximadamente. Marque las opciones elegidas en la Hoja de respuestas." % (NUM[len(AUD)], NUM[nA] if nA < 26 else str(nA), NUM[tA] if tA < 26 else ('cuarenta' if tA == 40 else str(tA))))
        g("[3]"); first = False
    n = tk['n']; a, b = tk['items'][0]['n'], tk['items'][-1]['n']
    if tk['type'] == 'pics':
        g("0: Tarea %s. Instrucciones. Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas, de la %s a la %s. Seleccione la opción correcta: a, be o ce. Marque las opciones elegidas en la Hoja de respuestas." % (NUM[n], NUM[a], NUM[b]))
        g("[2]\n0: A continuación va a oír un ejemplo.\n[1]")
        ex = tk['example']; g("\n# Conversación 0\n0: Ejemplo.\n[2]\n0: " + ex['pres']); dlg(ex)
        g("0: Conteste a la pregunta: " + ex['q']); g("[3]"); g("0: " + ex['solucion']); g("[5]")
        for it in tk['items']:
            g("\n# Conversación %d (clave %s)" % (it['n'], LET[it['ok']]))
            g("0: Conversación %s.\n[2]" % NUM[it['n']])
            for rep in (0, 1):
                if rep: g("# (repetición)")
                g("0: " + it['pres']); dlg(it); g("0: Conteste a la pregunta número %s: %s" % (NUM[it['n']], it['q'])); g("[5]")
    elif tk['type'] == 'friends':
        g("0: Tarea %s. Instrucciones. Usted va a escuchar una conversación entre dos amigos, %s y %s. Indique si los enunciados, del %s al %s, se refieren a %s, a, a %s, be, o a ninguno de los dos, ce. Escuchará la conversación dos veces. Marque las opciones elegidas en la Hoja de respuestas." % (NUM[n], tk['who'][0], tk['who'][1], NUM[a], NUM[b], tk['who'][0], tk['who'][1]))
        g("[2]\n0: Ahora tiene treinta segundos para leer los enunciados.\n[30]")
        V = tk['voices']
        for rep in (0, 1):
            g("\n# Conversación" + (" (repetición)" if rep else ""))
            for r, t in tk['lines']: g("%s: %s" % (V[r], t))
            g("[10]")
    elif tk['type'] == 'radio':
        g("0: Tarea %s. Instrucciones. Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas, de la %s a la %s, y seleccione la opción correcta: a, be o ce. Marque las opciones elegidas en la Hoja de respuestas." % (NUM[n], NUM[a], NUM[b]))
        g("[2]\n0: A continuación va a oír un ejemplo.\n[1]")
        ex = tk['example']; g("\n# Audio 0\n0: Ejemplo.\n[2]"); mono(ex)
        g("[1]\n0: Conteste a la pregunta del ejemplo.\n[3]"); g("0: " + ex['solucion']); g("[5]")
        for i, it in enumerate(tk['items']):
            g("\n# Audio %d (ítem %d, clave %s)" % (i + 1, it['n'], LET[it['ok']]))
            g("0: Audio %s.\n[2]" % NUM[i + 1])
            mono(it); g("[10]\n# (repetición)"); mono(it)
            g("[3]\n0: Conteste a la pregunta número %s.\n[10]" % NUM[it['n']])
    elif tk['type'] == 'msgs':
        g("0: Tarea %s. Instrucciones. Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado, de la a a la ka, que corresponde a cada mensaje, del %s al %s. Hay once opciones, incluido el ejemplo. Seleccione siete. Marque las opciones elegidas en la Hoja de respuestas." % (NUM[n], NUM[a], NUM[b]))
        g("[2]\n0: A continuación va a oír un ejemplo.\n[1]")
        ex = tk['example']; g("0: Ejemplo.\n[2]"); mono(ex); g("[3]"); g("0: " + ex['solucion']); g("[3]")
        g("0: Ahora tiene cuarenta y cinco segundos para leer los enunciados.\n[45]")
        for i, it in enumerate(tk['items']):
            g("\n# Mensaje %d (ítem %d, clave %s)" % (i + 1, it['n'], LET[it['ok']]))
            g("0: Mensaje %s.\n[2]" % NUM[i + 1])
            mono(it); g("[15]\n# (repetición)"); mono(it)
            g("[3]\n0: Elija la opción correcta.\n[10]")
    if tk is AUD[-1]: g("0: Fin de la prueba de comprensión auditiva.")
    else: g("0: Fin de la tarea %s." % NUM[n])
guion = "\n".join(G) + "\n"
habla = [l.split(":", 1)[1] for l in guion.split("\n") if ":" in l and not l.startswith("#") and not l.startswith("SONIDO")]
bad = [h for h in habla if re.search(r"\d", h)]
assert not bad, bad
open(os.path.join(OUT, 'U%s_guion.txt' % U), 'w').write(guion)

# ---------- nombres.txt ----------
N = ["# LISTA DE IMAGENES · Simulacro DELE A2 · Unidad %s" % int(U), "# nombre | ancho px | KB max | descripcion", "CARPETA: DELE_A2_U%s" % U, ""]
for k in ('portada', 'oral', 'escrita', 'oral_foto1', 'oral_foto2'):
    N.append("U%s_%-12s | 1600 | 90 | %s" % (U, k, F.IMG_DESC[k]))
for tk in AUD:
    if tk['type'] == 'pics':
        for i in range(7): N.append("U%s_CA1_%d       | 1200 | 90 | %s" % (U, i, F.CA1_DESC[i]))
open(os.path.join(OUT, 'nombres.txt'), 'w').write("\n".join(N) + "\n")

# ---------- prompts de imágenes ----------
VIN = ("Simple flat vector illustration in the style of an exam booklet, thin dark outlines, limited palette of soft coral, teal "
       "and warm grey, plain white background, three separate panels side by side of equal size with white space between them, "
       "one subject per panel, centred, no text, no letters, no labels, 3:1. ")
if getattr(F, "IMG_PROMPTS", None):
    R = ["PROMPTS DE IMÁGENES · Simulacro DELE A2 · Unidad %s (en inglés, uno por imagen)" % int(U), "=" * 75]
    for k in ('portada', 'oral', 'escrita', 'oral_foto1', 'oral_foto2'):
        R.append("\nU%s_%s.jpg  (1600 px)\n%s" % (U, k, F.IMG_PROMPTS[k]))
    for tk in AUD:
        if tk['type'] == 'pics':
            for i, c in enumerate([tk['example']] + tk['items']):
                R.append("\nU%s_CA1_%d.jpg  (1200 px, viñetas A-B-C)\n%s%s" % (U, i, VIN, c['prompt']))
    open(os.path.join(OUT, 'U%s_prompts_imagenes.txt' % U), 'w').write("\n".join(R) + "\n")
print("ok", U, "lectura", nL, "auditiva", nA)
