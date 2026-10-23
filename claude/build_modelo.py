# -*- coding: utf-8 -*-
# BUILD DE LOS MODELOS COMPLETOS DEL CURSO DE PREPARACIÓN DELE A2 (M1-M8)
# Uso:  python3 build_modelo.py fuente_M06 [carpeta]
# Genera desde fuente_Mxx.py, sin contradicciones entre archivos:
#   DELEA2_curso_Mxx_datos.py      -> python3 DELE_A2_motor_modelo.py DELEA2_curso_Mxx_datos
#                                     (motor adaptado: python3 adaptar_motor.py, una vez)
#                                     -> DELEA2_curso_Mxx_examen.html y DELEA2_curso_Mxx_oral_profesora.html
#   DELEA2_curso_Mxx_estudiante.txt y DELEA2_curso_Mxx_profesora.txt (cuadernillos para revisar)
#   Mxx_guion.txt (audio, para generar_audios.py), nombres.txt y Mxx_prompts_imagenes.txt
# Diferencias con build_unidad.py: nombres del curso, código de la oral A2-Mxx, sin portada ni foto de bloqueo,
# contenidos con fichas de remedio, talleres, control de progreso, textos modelo de la escritura (aprobado /
# excelente) y modelos de la tarea 3 de la oral. Comprueba además extensiones oficiales, claves sin rachas,
# repartos de las tareas de relacionar, voces que no se repiten con el simulacro anterior y fotos nunca usadas.
# 20/10/2026 (M7):
#  - Las extensiones de CA-T2, CA-T3 y CA-T4 se cuentan sin las etiquetas de emoción ([cheerful], [laughs]...),
#    como ya se hacía en CA-T1.
#  - PERFIL en la fuente ({"lectura": "+", "auditiva": "=", ...}) -> perfil del modelo al final de Resultados.
#  - SIN_EFECTOS = True en la fuente: se para si queda algún SONIDO (sintonía, din-don, pitido) en el audio.
#  - ETIQUETAS = True en la fuente: se para si alguna intervención del audio (personajes, radio, mensajes) no lleva
#    su etiqueta de emoción, o si una etiqueta no es de letras inglesas (v3 solo entiende [palabras en inglés]).
import sys, json, importlib, re, os
sys.path.insert(0, '.')
F = importlib.import_module(sys.argv[1])
M = F.M; OUT = sys.argv[2] if len(sys.argv) > 2 else '.'
PRE = "DELEA2_curso_M%s" % M
COD = "A2-M%s" % M
LET = 'ABCDEFGHIJK'
NUM = ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','once','doce','trece','catorce','quince','dieciséis','diecisiete','dieciocho','diecinueve','veinte','veintiuno','veintidós','veintitrés','veinticuatro','veinticinco']
WP = "https://2spanishteachers.com/wp-content/uploads/"
base = WP + F.MES_WP.strip("/") + "/"
U2 = importlib.import_module('DELEA2_F1_U02_datos').DATA
EST = dict(U2['estrategias']); EST.update(getattr(F, 'ESTRATEGIAS_NUEVAS', {}))
LECT = F.LECTURA; AUD = F.AUDITIVA
ERR = []
def chk(cond, msg):
    if not cond: ERR.append(msg)

def limpio(t): return re.sub(r"\s*\[[a-zA-Z ]+\]\s*", " ", t).strip()
def plain(t): return re.sub(r'<br>', '\n', re.sub(r'<(?!br)[^>]+>', '', t))
def nw(t): return len(re.findall(r"\S+", re.sub(r"<[^>]+>", " ", t)))
def tr_conv(c): return ['(' + c['pres'] + ')'] + ['%s: %s' % (r, limpio(t)) for r, v, t in c['lines']]
def tr_mono(c): return ['%s: %s' % (c['lab'], limpio(c['text']))]
def clean_item(it, extra=()):
    return {k: v for k, v in it.items() if k not in ('pc', 'pres', 'lines', 'prompt', 'solucion', 'voice', 'text', 'lab', 'sound') + tuple(extra)}

# ======================= COMPROBACIONES =======================
# Extensiones oficiales (Especificación del formato) · con margen pequeño en el ejemplo
def rng(n, a, b, que): chk(a <= n <= b, "%s: %d palabras (oficial %d-%d)" % (que, n, a, b))
for tk in LECT:
    if tk['type'] == 'mail': rng(sum(nw(p) for p in tk['body']), 250, 300, "CL-T1")
    if tk['type'] == 'ads':
        for it in [tk['example']] + tk['items']: rng(nw(it['body']), 50, 80, "CL-T2 " + it['title'][:30])
    if tk['type'] == 'people':
        for t in tk['texts']: rng(nw(t['body']), 100, 120, "CL-T3 " + t['name'])
        rep = sorted([sum(1 for it in tk['items'] if it['ok'] == i) for i in range(3)])
        chk(rep in ([2, 2, 2], [1, 2, 3]), "CL-T3: reparto de claves %s (2-2-2 o 3-2-1)" % rep)
    if tk['type'] == 'long': rng(sum(nw(p) for p in tk['body']), 375, 425, "CL-T4")
for tk in AUD:
    if tk['type'] == 'pics':
        for c in [tk['example']] + tk['items']: rng(sum(nw(limpio(t)) for r, v, t in c['lines']), 50, 80, "CA-T1 " + c['q'][:30])
    if tk['type'] == 'radio':
        for c in [tk['example']] + tk['items']: rng(nw(limpio(c['text'])), 40, 60, "CA-T2 " + c['q'][:30])
    if tk['type'] == 'friends':
        rng(sum(nw(limpio(t)) for r, t in tk['lines']), 225, 275, "CA-T3")
        rep = sorted([sum(1 for it in tk['items'] if it['ok'] == i) for i in range(3)])
        chk(rep == [2, 2, 2], "CA-T3: reparto %s (2 A, 2 B, 2 C)" % rep)
    if tk['type'] == 'msgs':
        for c in [tk['example']] + tk['items']: rng(nw(limpio(c['text'])), 30, 50, "CA-T4 " + c.get('conv', 'ejemplo'))
        oks = [tk['example']['ok']] + [it['ok'] for it in tk['items']]
        chk(len(set(oks)) == 8 and len(tk['enun']) == 11, "CA-T4: 11 enunciados, 8 usados (ejemplo + 7) y 3 que sobran")
# Claves: sin rachas de 3 iguales en las tareas de A/B/C
for tk in LECT + AUD:
    if tk['type'] in ('msgs',): continue
    ks = [it['ok'] for it in tk['items']]
    for i in range(len(ks) - 2):
        chk(not (ks[i] == ks[i + 1] == ks[i + 2]), "racha de 3 claves iguales en %s T%d (ítems %d-%d)" % ('CL' if tk in LECT else 'CA', tk['n'], tk['items'][i]['n'], tk['items'][i + 2]['n']))
    for it in tk['items']:
        chk(0 <= it['ok'] < len(it.get('o', 'ABC')), "clave fuera de rango en el ítem %d" % it['n'])
        for c in it['cats']: chk(c in F.CATS, "categoría desconocida %s (ítem %d)" % (c, it['n']))
        chk(it['es'] in EST, "estrategia desconocida %s" % it['es'])
        chk(it.get('why'), "falta la explicación del ítem %d" % it['n'])
# Numeración oficial
nums = [it['n'] for tk in LECT for it in tk['items']]; chk(nums == list(range(1, 26)), "lectura: ítems 1-25")
nums = [it['n'] for tk in AUD for it in tk['items']]; chk(nums == list(range(1, 26)), "auditiva: ítems 1-25")
usadas = {c for tk in LECT + AUD for it in tk['items'] for c in it['cats']}
chk(usadas == set(F.CATS), "contenidos sin ítems: %s" % (set(F.CATS) - usadas))
for k, c in F.CATS.items(): chk(c.get('fichas') is not None, "el contenido %s no tiene fichas" % k)
# Cifras con letras en lo que se oye
def oye():
    for tk in AUD:
        for c in ([tk['example']] + tk['items']) if 'example' in tk else tk['items']:
            if 'lines' in c:
                for r, v, t in c['lines']: yield t
            if 'text' in c: yield c['text']
        if tk['type'] == 'friends':
            for r, t in tk['lines']: yield t
for t in oye(): chk(not re.search(r"\d", t), "cifra en un audio: " + t[:60])
# Etiquetas de emoción (ElevenLabs v3) y efectos de sonido
if getattr(F, 'ETIQUETAS', False):
    for t in oye():
        chk(re.match(r"^\s*\[[a-z][a-z ]*\]", t), "intervención sin etiqueta de emoción al principio: " + t[:60])
        for e in re.findall(r"\[([^\]]*)\]", t): chk(re.match(r"^[a-z][a-z ]*$", e), "etiqueta rara (solo palabras en inglés): [%s]" % e)
if getattr(F, 'SIN_EFECTOS', False):
    for tk in AUD:
        for c in ([tk.get('example')] if tk.get('example') else []) + tk['items']:
            chk(not c.get('sound'), "efecto de sonido en %s (este modelo va sin efectos)" % c.get('conv', c.get('q', 'ejemplo')))
# Voces: ninguna del simulacro anterior
VOCES = []
for tk in AUD:
    for c in ([tk.get('example')] if tk.get('example') else []) + tk['items']:
        VOCES += [v for r, v, t in c.get('lines', [])] + ([c['voice'].split('/')[0]] if c.get('voice') else [])
    VOCES += list(tk.get('voices', {}).values())
evitar = set(getattr(F, 'VOCES_EVITAR', []))
chk(not (set(VOCES) & evitar), "voces repetidas del simulacro anterior: %s" % (set(VOCES) & evitar))
if os.path.exists('voces.txt'):
    cod = set(re.findall(r"^([A-Z_0-9]+)\s*=", open('voces.txt', encoding='utf-8').read(), re.M))
    chk(set(VOCES) <= cod, "voces que no están en voces.txt: %s" % (set(VOCES) - cod))
else:
    print("AVISO: no hay voces.txt en la carpeta; no compruebo que existan los códigos de voz")
# Fotos: perfil completo, situaciones nunca usadas, las dos de la oral muy distintas
PF = F.PERFIL_FOTOS; SU = F.SITUACIONES_USADAS
CAMPOS = ("situacion", "personas", "edades", "aspecto", "espacio", "lugar", "momento", "estacion", "tiempo", "gente", "accion", "fondo", "objetos", "detalle")
for k in ("oral_foto1", "oral_foto2", "escrita"):
    chk(not [c for c in CAMPOS if not PF.get(k, {}).get(c)], "PERFIL_FOTOS[%s] incompleto" % k)
ya = {x.lower() for u, l in SU.items() if u != "M" + M for x in l}
for k in ("oral_foto1", "oral_foto2"): chk(PF[k]["situacion"].lower() not in ya, "situación ya usada: " + PF[k]["situacion"])
chk([x.lower() for x in SU.get("M" + M, [])] == [PF["oral_foto1"]["situacion"].lower(), PF["oral_foto2"]["situacion"].lower()], "SITUACIONES_USADAS['M%s'] = [foto1, foto2]" % M)
dif = [c for c in ("espacio", "momento", "estacion", "tiempo", "gente", "personas") if PF["oral_foto1"][c] != PF["oral_foto2"][c]]
chk(len(dif) >= 3, "las dos fotos de la oral se parecen demasiado: " + str(dif))
for k, n in F.IMG_NAMES.items(): chk(re.match(r"^M%s_[a-z0-9_]+$" % M, n), "nombre de imagen raro: " + n)
for tk in AUD:
    if tk['type'] == 'pics':
        for c in [tk['example']] + tk['items']: chk(re.match(r"^M%s_CA1_\d_[a-z_]+\.jpg$" % M, c['img']), "viñeta sin nombre que diga qué es: " + c['img'])
# Perfil del modelo (lo que se enseña al final de Resultados)
PERFIL = getattr(F, 'PERFIL', None)
if PERFIL:
    chk(set(PERFIL.get('pruebas', {})) == {"lectura", "auditiva", "escrita", "oral"} and all(v in ("+", "=", "-", "−") for v in PERFIL['pruebas'].values()), "PERFIL: las cuatro pruebas con +, = o -")

# ======================= ESCRITURA: textos modelo =======================
CONECT = r"(?i)\b(y|pero|porque|además|también|tampoco|entonces|primero|después|luego|más tarde|al final|al principio|por eso|cuando|de repente|mientras)\b"
def modelo(x, pautas, mn, mx, que):
    txt = "\n".join(x['texto']); limpio_ = re.sub(r"\[\d\]|_", "", txt)
    pal = nw(limpio_)
    chk(mn <= pal <= mx, "%s: %d palabras (límite %d-%d)" % (que, pal, mn, mx))
    marcas = [int(n) for n in re.findall(r"\[(\d)\]", txt)]
    chk(sorted(set(marcas)) == list(range(1, pautas + 1)), "%s: pautas marcadas %s (tienen que estar las %d)" % (que, marcas, pautas))
    html = "".join("<p>%s</p>" % re.sub(r"_([^_]+)_", r"<u>\1</u>", re.sub(r"\[(\d)\]", r'<sup class="pn">\1</sup>', l)) for l in x['texto'])
    lin = round(pal / 10.0)
    d = {"html": html, "pal": pal, "lin": "unas %d líneas a ojo" % lin, "porque": x['porque']}
    if x.get('mejoras'): d['mejoras'] = x['mejoras']
    return d, set(c.lower() for c in re.findall(r"_([^_]+)_", txt))
ESC = json.loads(json.dumps(F.ESCRITA))
MODS = {}
for k, m in F.ESCRITA.get('modelos', {}).items():
    if k == 't1': np_, mn, mx = len(F.ESCRITA['t1']['pautas']), F.ESCRITA['t1']['min'], F.ESCRITA['t1']['max']
    else: np_, mn, mx = len(F.ESCRITA['t2'][k]['pautas']), F.ESCRITA['t2']['min'], F.ESCRITA['t2']['max']
    a, ca = modelo(m['aprobado'], np_, mn, mx, m['titulo'] + " (aprobado)")
    e, ce = modelo(m['excelente'], np_, mn, mx, m['titulo'] + " (excelente)")
    chk(len(ce) > len(ca), "%s: el excelente tiene que usar más conectores distintos que el aprobado" % m['titulo'])
    chk(len(m['excelente'].get('mejoras', [])) >= 3, "%s: el excelente necesita al menos 3 mejoras" % m['titulo'])
    MODS[k] = {"titulo": m['titulo'], "aprobado": a, "excelente": e}
    # trato de la tarea 1: lo dice ESCRITA['t1']['trato'] ("tú", lo normal en el examen, o "usted")
    if k == 't1':
        tr1 = F.ESCRITA['t1'].get('trato', 'usted')
        for x in (m['aprobado'], m['excelente']):
            t = " ".join(x['texto']).lower()
            if tr1 == 'usted': chk(not re.search(r"\b(hola|querid[oa]s?|un abrazo|un beso|te |tú|tienes|puedes)\b", t), "correo de usted con palabras de tú")
            else: chk(not re.search(r"\b(usted|ustedes|estimad[oa]s?|atentamente|le escribo|les escribo|su ayuda)\b", t), "correo de tú con palabras de usted")
ESC['modelos'] = MODS
chk(30 <= nw(" ".join(F.ESCRITA['t1']['input'])) <= 50, "texto de entrada de la escritura T1: %d palabras (35-45 + firma)" % nw(" ".join(F.ESCRITA['t1']['input'])))

# ======================= ORAL: modelos de la tarea 3 =======================
TU = re.compile(r"(?i)\b(tú|tienes|puedes|quieres|te |ti\b|contigo|perdona|oye|mira,|¿te va)")
US = re.compile(r"(?i)\b(usted|ustedes|perdone|oiga|disculpe|¿me deja|le |les )")
for m in getattr(F, 'ORAL_MODELOS', {}).get('t3', []):
    cand = " ".join(d[1] for d in m['dialogo'] if d[0] == 'C')
    if m['trato'] == 'tú': chk(not US.search(cand), "%s: el candidato dice palabras de usted" % m['titulo'])
    else: chk(not TU.search(cand), "%s: el candidato dice palabras de tú" % m['titulo'])
    chk(sum(1 for d in m['dialogo'] if len(d) > 2 and d[2]) == 1, "%s: tiene que haber un solo pequeño problema" % m['titulo'])
    chk(m['dialogo'][0][0] == 'E' and m['dialogo'][-1][0] == 'C', "%s: empieza el examinador y termina el candidato" % m['titulo'])
    chk(sum(1 for d in m['dialogo'] if d[0] == 'C' and '?' in d[1]) >= 3, "%s: el candidato hace al menos 3 preguntas" % m['titulo'])
    chk(len(m['notas']) == len(F.ORAL['t3']['ops'][F.ORAL_MODELOS['t3'].index(m)]['pautas']), "%s: una nota por pauta" % m['titulo'])
    # Desde 2020 todas las láminas publicadas de la tarea 3 son de tú (amigo, familiar, compañero): ver
    # claude/DELE_A2_examen_real_hallazgos.txt. Una de servicio (usted) solo si la fuente lo pide con T3_SERVICIO = True.
    if m['trato'] != 'tú' and not getattr(F, 'T3_SERVICIO', False):
        chk(False, "%s: la tarea 3 del examen actual es de tú (pon T3_SERVICIO = True si de verdad quieres una de usted)" % m['titulo'])

if ERR:
    print("\n".join("ERROR: " + e for e in ERR)); sys.exit("PARADO: %d problemas en la fuente" % len(ERR))

# ======================= DATOS =======================
def datos_task(tk):
    d = {k: v for k, v in tk.items() if k not in ('items', 'example', 'lines', 'voices', 'who')}
    if tk['type'] == 'pics':
        ex = tk['example']
        d['example'] = {'q': ex['q'], 'o': ex['o'], 'ok': ex['ok'], 'img': ex['img'], 'tr': tr_conv(ex)}
        d['items'] = [dict(clean_item(it), tr=tr_conv(it)) for it in tk['items']]
    elif tk['type'] == 'friends':
        d['tr'] = ['%s: %s' % (tk['who'][[w.upper().replace('Í', 'I').replace('É', 'E').replace('Á', 'A') for w in tk['who']].index(r)] if r in [w.upper().replace('Í', 'I').replace('É', 'E').replace('Á', 'A') for w in tk['who']] else r.capitalize(), limpio(t)) for r, t in tk['lines']]
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
# Guion de la profesora: el de la fuente + los diálogos modelo de la tarea 3 (antes de «Qué mirar»)
dlg = []
for m in getattr(F, 'ORAL_MODELOS', {}).get('t3', []):
    dlg.append("    DIÁLOGO MODELO · %s (%s). Pequeño problema: %s" % (m['titulo'], m['trato'], m['problema']))
    dlg += ["      %s: %s" % ("Examinador" if d[0] == 'E' else "Candidato", d[1]) for d in m['dialogo']]
G0 = F.GUION_ENTREVISTADOR
G0 = G0.replace("  Qué mirar", "\n".join(dlg) + "\n  Qué mirar", 1) if dlg else G0
TITULO = "%s · %s" % (F.NOMBRE, F.TITLE)
DATA = {"unit": "M" + M, "nombre": F.NOMBRE, "title": TITULO, "modelo": True, "codigoExamen": COD,
 "h1": "DELE A2 · %s (%s)" % (F.NOMBRE, F.NIVEL), "packHead": "MODELO DE EXAMEN DELE A2 - %s" % F.NOMBRE.upper(),
 "fileHtml": PRE + "_examen.html", "fileProf": PRE + "_oral_profesora.html",
 "storageKey": "dele_a2_curso_m%s_v1" % M, "email": U2['email'],
 "audio": {"t%d" % tk['n']: base + "%s_CA_T%d.m4a" % (PRE, tk['n']) for tk in AUD}, "imgBase": base, "imgs": {},
 "recLabel": F.REC_LABEL, "recordatorio": F.RECORDATORIO, "tipsInicio": F.TIPS_INICIO, "cats": F.CATS, "estrategias": EST,
 "lectura": {"tasks": [datos_task(t) for t in LECT]}, "auditiva": {"tasks": [datos_task(t) for t in AUD]},
 "escrita": ESC, "oral": F.ORAL, "oralModelos": getattr(F, 'ORAL_MODELOS', {}),
 "talleres": F.TALLERES, "crono": F.CRONO, "tiempos": F.TIEMPOS,
 "profesora": {"guion": G0, "errores": getattr(F, "ERRORES", "")}}
if PERFIL: DATA["perfil"] = PERFIL
open(os.path.join(OUT, PRE + '_datos.py'), 'w').write("# -*- coding: utf-8 -*-\n# DATOS DEL MODELO %s (curso de preparación DELE A2) · generado con build_modelo.py\ntrue, false, null = True, False, None\nDATA = %s\n" % (M, json.dumps(DATA, ensure_ascii=True, indent=1)))

# ======================= CUADERNILLO DEL ESTUDIANTE =======================
E = []; w = E.append
nL = sum(len(t['items']) for t in LECT); nA = sum(len(t['items']) for t in AUD)
w("DELE A2 — %s · %s (%s)" % (F.NOMBRE.upper(), F.TITLE, F.NIVEL)); w("Cuadernillo del estudiante (%s_estudiante.txt)" % PRE); w("=" * 75)
w("Material de preparación original. No es un examen oficial y es independiente\ndel Instituto Cervantes.\n")
w(F.REC_LABEL.upper()); [w("  · " + plain(r)) for r in F.RECORDATORIO]; w("")
w("TIPS DE ARRANQUE"); [w("  · " + plain(r)) for r in F.TIPS_INICIO]; w("")
w("=" * 75); w("PRUEBA 1. COMPRENSIÓN DE LECTURA"); w("Esta prueba tiene 4 tareas. Usted debe responder a %d preguntas.\nLa duración es de %d minutos. Marque sus opciones únicamente en la Hoja de\nrespuestas." % (nL, F.TIEMPOS['lectura'])); w("=" * 75)
def opts(it, ind="    "):
    for i, o in enumerate(it['o']): w("%s%s) %s" % (ind, LET[i], o))
for tk in LECT:
    w("\nTAREA %d\nINSTRUCCIONES\n%s Marque las opciones elegidas en la Hoja de\nrespuestas.\n(Tip: %s)\n" % (tk['n'], tk['instr'], plain(tk.get('tip', ''))))
    if tk['type'] == 'mail':
        [w("  " + h) for h in tk['head']]; w(""); [w(plain(p) + "\n") for p in tk['body']]; w("PREGUNTAS")
        for it in tk['items']: w("%d. %s" % (it['n'], it['q'])); opts(it)
    elif tk['type'] == 'people':
        w("PREGUNTAS" + " " * 40 + "   ".join("%s. %s" % (LET[i], t['name'].upper()) for i, t in enumerate(tk['texts'])))
        for it in tk['items']: w("%d. %s" % (it['n'], it['q']))
        for i, t in enumerate(tk['texts']): w("\n%s. %s\n%s" % (LET[i], t['name'].upper(), t['body']))
    elif tk['type'] == 'long':
        w(tk['title'].upper()); w(tk.get('sub', '') + "\n"); [w(p + "\n") for p in tk['body']]; w("PREGUNTAS")
        for it in tk['items']: w("%d. %s" % (it['n'], it['q'])); opts(it)
    elif tk['type'] == 'ads':
        ex = tk['example']; w("EJEMPLO · TEXTO 0 · %s\n%s\n0. %s" % (ex['title'], plain(ex['body']), ex['q'])); opts(ex); w("   " + ex['why'] + "\n")
        for i, it in enumerate(tk['items']): w("TEXTO %d · %s\n%s\n%d. %s" % (i + 1, it['title'], plain(it['body']), it['n'], it['q'])); opts(it); w("")
w("\n" + "=" * 75); w("PRUEBA 2. COMPRENSIÓN AUDITIVA"); w("Esta prueba tiene 4 tareas. Usted debe responder a %d preguntas.\nLa duración es de %d minutos, aproximadamente.\n(Pon el audio de cada tarea al principio y no lo pares.)" % (nA, F.TIEMPOS['auditiva'])); w("=" * 75)
for tk in AUD:
    w("\nTAREA %d   [audio %s_CA_T%d]\nINSTRUCCIONES\n%s Marque las opciones elegidas en la Hoja de\nrespuestas.\n" % (tk['n'], PRE, tk['n'], tk['instr']))
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
Es = F.ESCRITA
w("\n" + "=" * 75); w("PRUEBA 3. EXPRESIÓN E INTERACCIÓN ESCRITAS · 45 minutos"); w("=" * 75)
w("CONSEJO: cuenta tus palabras con los ojos. Escribe unas 10 palabras por línea:\ntarea 1 = 6 o 7 líneas; tarea 2 = 7 u 8 líneas.\n")
w("TAREA 1\n" + Es['t1']['instr']); [w("  | " + l) for p in Es['t1']['input'] for l in plain(p).split("\n")]
w(Es['t1']['lead']); [w("  - " + p) for p in Es['t1']['pautas']]
w("Número de palabras recomendadas: entre %d y %d.\n" % (Es['t1']['min'], Es['t1']['max']))
w("TAREA 2\n" + Es['t2']['instr'])
o1 = Es['t2']['op1']; w("\nOPCIÓN 1\n" + o1['intro']); [w("  - " + p) for p in o1['pautas']]
o2 = Es['t2']['op2']; w("\nOPCIÓN 2\n" + o2['intro'])
for i, p in enumerate(o2.get('photos', [])): w("  Foto %d. %s" % (i + 1, p))
w(o2['intro2']); [w("  - " + p) for p in o2['pautas']]
w("Número de palabras recomendadas: entre %d y %d.\n" % (Es['t2']['min'], Es['t2']['max']))
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
open(os.path.join(OUT, PRE + '_estudiante.txt'), 'w').write("\n".join(E) + "\n")

# ======================= CUADERNILLO DE LA PROFESORA =======================
P = []; p = P.append
p("DELE A2 — %s · %s (%s)" % (F.NOMBRE.upper(), F.TITLE, F.NIVEL)); p("Cuadernillo de la profesora · USO INTERNO"); p("=" * 75)
p("Código de la oral: examen %s (el motor lo escribe al generar; también en el panel)." % COD)
if PERFIL: p("Perfil del modelo (lectura / auditiva / escritura / oral): %s" % " ".join(PERFIL['pruebas'][k] for k in ("lectura", "auditiva", "escrita", "oral")))
p("\n1) CLAVE")
for nom, tasks in (("LECTURA", LECT), ("AUDITIVA", AUD)):
    for tk in tasks:
        ex = ("0 %s (ej.) · " % LET[tk['example']['ok']]) if 'example' in tk and 'ok' in tk['example'] else ""
        p("  %s T%d: %s%s" % (nom, tk['n'], ex, " · ".join("%d %s" % (it['n'], LET[it['ok']]) for it in tk['items'])))
p("\n2) TEMAS DE CADA TAREA (mezclados, como en el examen)")
for tk in LECT: p("  CL-T%d: %s" % (tk['n'], tk.get('title') or (tk.get('head') or [''])[-1] or tk['instr'][:80]))
p("\n3) METADATOS POR ÍTEM")
for nom, tasks in (("CL", LECT), ("CA", AUD)):
    for tk in tasks:
        for it in tk['items']:
            p("  %s-T%d · %d · clave %s · %s · %s" % (nom, tk['n'], it['n'], LET[it['ok']], it['es'], it.get('pc', '')))
            p("     Contenido: %s" % " / ".join(F.CATS[c]['name'] for c in it['cats']))
            p("     Justificación: %s" % it['why'])
p("\n4) TRANSCRIPCIONES")
for tk in AUD:
    p("  TAREA %d" % tk['n'])
    if tk['type'] == 'pics':
        for c in [tk['example']] + tk['items']: p("   %s — %s" % (c.get('conv', 'Conversación 0 (ejemplo)'), c['q'])); [p("     " + l) for l in tr_conv(c)]
    elif tk['type'] == 'friends':
        [p("     %s" % l) for l in datos_task(tk)['tr']]
    else:
        for c in [tk['example']] + tk['items']:
            p("   %s%s · voz %s" % (c.get('conv', 'Ejemplo'), (" · ítem %d, clave %s" % (c['n'], LET[c['ok']])) if 'n' in c else "", c['voice'])); p("     %s: %s" % (c['lab'], limpio(c['text'])))
p("\n5) MAPA DE CONTENIDOS Y FICHAS")
for k, c in F.CATS.items():
    its = ["%s%d" % ('L' if tk in LECT else 'A', it['n']) for tk in LECT + AUD for it in tk['items'] if k in it['cats']]
    p("  %-9s %s: %s  ·  fichas: %s" % (k, c['name'], ", ".join(its), ", ".join(f['t'] for f in c['fichas']) or "-"))
p("\n6) ESCRITURA · TEXTOS MODELO")
for k, m in F.ESCRITA['modelos'].items():
    p("  " + m['titulo'])
    for lab in ('aprobado', 'excelente'):
        x = MODS[k][lab]; p("   %s (%d palabras):" % (lab.upper(), x['pal']))
        [p("     " + plain(re.sub(r"\[(\d)\]", r"(\1) ", re.sub(r"_", "", l)))) for l in m[lab]['texto']]
p("\n7) ORAL · GUION DEL ENTREVISTADOR"); p(G0)
p("\n8) ERRORES ESPERABLES"); p(F.ERRORES)
p("\n9) IMÁGENES (prompts en M%s_prompts_imagenes.txt · lista en nombres.txt)" % M)
for k in ("oral_foto1", "oral_foto2", "escrita"):
    f = PF[k]; p("  %s · %s.jpg · %s" % (k, F.IMG_NAMES[k], f["situacion"].upper()))
    for c in CAMPOS[1:]: p("     %-9s %s" % (c + ":", f[c]))
open(os.path.join(OUT, PRE + '_profesora.txt'), 'w').write("\n".join(P) + "\n")

# ======================= GUION DE AUDIO =======================
G = []; g = G.append
g("# GUION DE AUDIO · %s del curso DELE A2 · generado con build_modelo.py" % F.NOMBRE)
g("# Formato: \"VOZ: texto\" · [n] = silencio · \"# ARCHIVO nombre\" · \"SONIDO n: descripcion\"")
g(F.REPARTO)
def mono(c):
    if c.get('sound'): g(c['sound'])
    g("%s: %s" % (c['voice'], c['text']))
def dlgx(c):
    for r, v, t in c['lines']: g("%s: %s" % (v, t))
first = True
for tk in AUD:
    g("\n\n# ARCHIVO %s_CA_T%d" % (PRE, tk['n']))
    if first:
        g("0: Prueba de comprensión auditiva. Escuche con atención todas las instrucciones. Esta prueba contiene cuatro tareas. Usted debe responder a veinticinco preguntas. La duración es de cuarenta minutos, aproximadamente. Marque las opciones elegidas en la Hoja de respuestas.")
        g("[3]"); first = False
    n = tk['n']; a, b = tk['items'][0]['n'], tk['items'][-1]['n']
    if tk['type'] == 'pics':
        g("0: Tarea %s. Instrucciones. Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas, de la %s a la %s. Seleccione la opción correcta: a, be o ce. Marque las opciones elegidas en la Hoja de respuestas." % (NUM[n], NUM[a], NUM[b]))
        g("[2]\n0: A continuación va a oír un ejemplo.\n[1]")
        ex = tk['example']; g("\n# Conversación 0\n0: Ejemplo.\n[2]\n0: " + ex['pres']); dlgx(ex)
        g("0: Conteste a la pregunta: " + ex['q']); g("[3]"); g("0: " + ex['solucion']); g("[5]")
        for it in tk['items']:
            g("\n# Conversación %d (clave %s)" % (it['n'], LET[it['ok']])); g("0: Conversación %s.\n[2]" % NUM[it['n']])
            for rep in (0, 1):
                if rep: g("# (repetición)")
                g("0: " + it['pres']); dlgx(it); g("0: Conteste a la pregunta número %s: %s" % (NUM[it['n']], it['q'])); g("[5]")
    elif tk['type'] == 'friends':
        g("0: Tarea %s. Instrucciones. Usted va a escuchar una conversación entre dos amigos, %s y %s. Indique si los enunciados, del %s al %s, se refieren a %s, a, a %s, be, o a ninguno de los dos, ce. Escuchará la conversación dos veces. Marque las opciones elegidas en la Hoja de respuestas." % (NUM[n], tk['who'][0], tk['who'][1], NUM[a], NUM[b], tk['who'][0], tk['who'][1]))
        g("[2]\n0: Ahora tiene treinta segundos para leer los enunciados.\n[30]")
        for rep in (0, 1):
            g("\n# Conversación" + (" (repetición)" if rep else ""))
            for r, t in tk['lines']: g("%s: %s" % (tk['voices'][r], t))
            g("[10]")
    elif tk['type'] == 'radio':
        g("0: Tarea %s. Instrucciones. Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas, de la %s a la %s, y seleccione la opción correcta: a, be o ce. Marque las opciones elegidas en la Hoja de respuestas." % (NUM[n], NUM[a], NUM[b]))
        g("[2]\n0: A continuación va a oír un ejemplo.\n[1]")
        ex = tk['example']; g("\n# Audio 0\n0: Ejemplo.\n[2]"); mono(ex)
        g("[1]\n0: Conteste a la pregunta del ejemplo.\n[3]"); g("0: " + ex['solucion']); g("[5]")
        for i, it in enumerate(tk['items']):
            g("\n# Audio %d (ítem %d, clave %s)" % (i + 1, it['n'], LET[it['ok']])); g("0: Audio %s.\n[2]" % NUM[i + 1])
            mono(it); g("[10]\n# (repetición)"); mono(it); g("[3]\n0: Conteste a la pregunta número %s.\n[10]" % NUM[it['n']])
    elif tk['type'] == 'msgs':
        g("0: Tarea %s. Instrucciones. Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado, de la a a la ka, que corresponde a cada mensaje, del %s al %s. Hay once opciones, incluido el ejemplo. Seleccione siete. Marque las opciones elegidas en la Hoja de respuestas." % (NUM[n], NUM[a], NUM[b]))
        g("[2]\n0: A continuación va a oír un ejemplo.\n[1]")
        ex = tk['example']; g("0: Ejemplo.\n[2]"); mono(ex); g("[3]"); g("0: " + ex['solucion']); g("[3]")
        g("0: Ahora tiene cuarenta y cinco segundos para leer los enunciados.\n[45]")
        for i, it in enumerate(tk['items']):
            g("\n# Mensaje %d (ítem %d, clave %s)" % (i + 1, it['n'], LET[it['ok']])); g("0: Mensaje %s.\n[2]" % NUM[i + 1])
            mono(it); g("[15]\n# (repetición)"); mono(it); g("[3]\n0: Elija la opción correcta.\n[10]")
    g("0: Fin de la prueba de comprensión auditiva." if tk is AUD[-1] else "0: Fin de la tarea %s." % NUM[n])
guion = "\n".join(G) + "\n"
habla = [l.split(":", 1)[1] for l in guion.split("\n") if ":" in l and not l.startswith("#") and not l.startswith("SONIDO")]
assert not [h for h in habla if re.search(r"\d", h)], "cifras en el guion"
if getattr(F, 'SIN_EFECTOS', False): assert not [l for l in guion.split("\n") if l.startswith("SONIDO")], "queda un efecto de sonido en el guion"
open(os.path.join(OUT, 'M%s_guion.txt' % M), 'w').write(guion)

# ======================= IMÁGENES =======================
N = ["# LISTA DE IMAGENES - Curso DELE A2 - %s" % F.NOMBRE, "# nombre | ancho px | KB max | descripcion", "CARPETA: DELE_A2_curso", ""]
for k in ("oral_foto1", "oral_foto2", "escrita"): N.append("%s | 1600 | 90 | %s" % (F.IMG_NAMES[k], F.IMG_DESC[k]))
for tk in AUD:
    if tk['type'] == 'pics':
        for i, c in enumerate([tk['example']] + tk['items']): N.append("%s | 1200 | 90 | %s" % (c['img'][:-4], F.CA1_DESC[i]))
for l in N: chk(not re.search(r"[\"'’]", l) and all(ord(ch) < 128 for ch in l), "nombres.txt: sin tildes ni comillas: " + l)
if ERR: print("\n".join("ERROR: " + e for e in ERR)); sys.exit("PARADO")
open(os.path.join(OUT, 'nombres.txt'), 'w').write("\n".join(N) + "\n")
# Fotos: estilo natural (María, 14/10/2026), como fotos_M3.py; la escritura es un tríptico 3:1
ESTILO = ("An ordinary, unedited snapshot taken with a phone by a friend; it must look like a real photo, not AI-generated. "
          "Soft, flat, even daylight or normal indoor light, LOW CONTRAST, no HDR, no dramatic or cinematic lighting, "
          "no glow, no strong shadows, muted true-to-life colours (not saturated), slight natural grain. "
          "Real ordinary people with natural skin texture and small imperfections, normal everyday clothes with creases; "
          "relaxed, natural poses and postures caught in the middle of the action, nobody posing or looking at the camera, "
          "no perfect smiles. Clear composition: the main people large and clearly visible, an easy-to-recognise everyday "
          "place, a normal lived-in background, eye-level framing, everything in focus (no blurred background). "
          "No readable text, no logos. ")
# Fotos de la oral: como las de las láminas oficiales de 2022 (vistas el 15/10/2026): foto de móvil de aficionado,
# casi siempre DOS personas, UNA acción clara que dice el título, un sitio corriente, objetos fáciles de nombrar,
# luz normal; alguien puede mirar a la cámara; nada dramático.
ESTILO_ORAL = ("An ordinary snapshot taken with a phone by a family member or friend who is in the room, like the photos in "
               "the official DELE A2 speaking exam: real ordinary people in an ordinary place, caught in the middle of one "
               "clear everyday action. The light is just the light that was there (normal indoor light or daylight), natural "
               "colours, slight grain, no retouching, no HDR, no dramatic lighting. Simple composition at eye level: the two "
               "people large and clearly visible, some everyday objects around them and at the edges of the frame, a normal "
               "lived-in background, everything in focus. Relaxed, natural postures; one of them may glance at the camera or "
               "smile, but nobody poses like a model. No readable text, no logos. ")
NO_IA = (" Avoid: HDR, high contrast, oversharpening, glossy or airbrushed skin, plastic look, perfect symmetrical faces, "
         "studio or stock-photo look, posed smiles, dramatic sky, lens flare, bokeh, extra fingers.")
TRIPTICO = ("Layout: ONE wide image, aspect ratio 3:1, made of exactly three equal photo panels side by side "
            "(left, middle, right), separated by thin plain white gutters, like three snapshots of the same story printed "
            "next to each other. Each panel is a complete photo on its own. The same people must look exactly the same in "
            "the three panels (same face, hair, body and clothes, unless the panel says otherwise). ")
VIN = ("Simple flat vector illustration in the style of an exam booklet, thin dark outlines, limited palette of soft coral, teal "
       "and warm grey, plain white background, three separate panels side by side of equal size with white space between them, "
       "one subject per panel, centred, no text, no letters, no labels, 3:1. ")
Rr = ["PROMPTS DE IMÁGENES · Curso DELE A2 · %s (en inglés, uno por imagen; nombres en nombres.txt)" % F.NOMBRE, "=" * 75]
for k in ("oral_foto1", "oral_foto2", "escrita"):
    t = F.IMG_PROMPTS[k]
    if k == "escrita":
        assert not re.search(r"(?i)(look\w* (at|into) the camera|smil\w* (at|for) the camera|pos(es|ing) for)", t), k
        Rr.append("\n%s.jpg  (1600 px)\n%s%s%s%s" % (F.IMG_NAMES[k], ESTILO, TRIPTICO, t, NO_IA))
    else:
        Rr.append("\n%s.jpg  (1600 px)\n%s%s Aspect ratio 4:3.%s" % (F.IMG_NAMES[k], ESTILO_ORAL, t, NO_IA))
for tk in AUD:
    if tk['type'] == 'pics':
        for c in [tk['example']] + tk['items']: Rr.append("\n%s  (1200 px, viñetas A-B-C)\n%s%s" % (c['img'], VIN, c['prompt']))
open(os.path.join(OUT, 'M%s_prompts_imagenes.txt' % M), 'w').write("\n".join(Rr) + "\n")
print("ok", F.NOMBRE, "· lectura", nL, "· auditiva", nA, "·", PRE + "_datos.py, cuadernillos, guion, nombres.txt y prompts")
