#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSCRIPCION DE LA PRUEBA ORAL DELE (A2 y B2) con ElevenLabs Scribe
Carpeta: Documentos/DELE_ORAL (separada de DELE_AUDIO)

Uso (en Terminal, dentro de esta carpeta):
    python3 transcribir_oral.py grabacion.m4a
    python3 transcribir_oral.py grabacion.m4a --nombre "Anna"     -> pone el nombre en los archivos
    python3 transcribir_oral.py grabacion.m4a --cambiar            -> si ha confundido profesora y estudiante
    python3 transcribir_oral.py --rehacer Oral_Anna_2026-10-19.json -> rehace el texto sin volver a pagar
    python3 transcribir_oral.py --nombre "Anna"                    -> sin archivo: se abre una ventana para elegirlo
                                                                     (puedes elegir varios: se unen en un solo .txt, por orden de nombre)
    python3 transcribir_oral.py parte1.m4a parte2.m4a              -> varias grabaciones del mismo oral, en ese orden
    ... --tareas 2:40,5:15   -> si nadie dijo "Tarea dos / tres": minuto en que empiezan la tarea 2 y la 3

Acepta m4a, mp3, wav y tambien el video de Zoom (mp4).
Durante la prueba, di en voz alta "Tarea uno", "Tarea dos" y "Tarea tres":
asi la transcripcion se divide sola por tareas.

La API key se lee de clave.txt en esta carpeta o, si no esta, de ../DELE_AUDIO/clave.txt
(no hace falta copiarla).

Salida en la carpeta "transcripciones":
    Oral_<nombre>_<fecha>.txt   -> transcripcion por tareas + datos de fluidez (para la libreta)
    Oral_<nombre>_<fecha>.json  -> respuesta completa de ElevenLabs (para rehacer sin pagar)
Coste aproximado: unos 330 creditos por minuto de audio (un oral de 12 min, unos 4.000).
"""
import sys, os, json, re, time, uuid, datetime, unicodedata
import urllib.request, urllib.error

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "transcripciones")
MODELOS = ["scribe_v2", "scribe_v1"]   # si el primero no esta disponible, prueba el siguiente
PAUSA_LARGA = 3.0                      # segundos de silencio del estudiante que cuentan como pausa larga
MULETILLAS = ["eh", "ehm", "em", "emm", "mm", "mmm", "hmm", "pues", "bueno", "o sea", "a ver", "vale"]
NUM = {"uno": 1, "1": 1, "dos": 2, "2": 2, "tres": 3, "3": 3}

def salir(msg): sys.exit("\n" + msg + "\n")

def leer_clave():
    for ruta in (os.path.join(AQUI, "clave.txt"), os.path.join(AQUI, "..", "DELE_AUDIO", "clave.txt")):
        if os.path.exists(ruta):
            return open(ruta, encoding="utf-8").read().strip()
    salir("No encuentro clave.txt ni aqui ni en Documentos/DELE_AUDIO.")

def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^\w\s]", "", t).strip()

def mmss(s): return "%02d:%02d" % (int(s) // 60, int(s) % 60)

# ---------------------------------------------------------------- ElevenLabs
def multipart(campos, archivo):
    b = uuid.uuid4().hex
    partes = []
    for k, v in campos.items():
        partes.append(('--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n' % (b, k, v)).encode("utf-8"))
    nombre = os.path.basename(archivo)
    partes.append(('--%s\r\nContent-Disposition: form-data; name="file"; filename="%s"\r\n'
                   'Content-Type: application/octet-stream\r\n\r\n' % (b, nombre)).encode("utf-8"))
    partes.append(open(archivo, "rb").read())
    partes.append(("\r\n--%s--\r\n" % b).encode("utf-8"))
    return b"".join(partes), "multipart/form-data; boundary=" + b

def transcribir(clave, archivo):
    if os.environ.get("DELE_PRUEBA"):                 # modo prueba sin internet
        return json.load(open(os.environ["DELE_PRUEBA"], encoding="utf-8"))
    for modelo in MODELOS:
        campos = {"model_id": modelo, "language_code": "spa", "diarize": "true", "num_speakers": "2",
                  "tag_audio_events": "true", "timestamps_granularity": "word"}
        cuerpo, tipo = multipart(campos, archivo)
        for intento in range(4):
            req = urllib.request.Request("https://api.elevenlabs.io/v1/speech-to-text", data=cuerpo, method="POST",
                                         headers={"xi-api-key": clave, "Content-Type": tipo})
            try:
                print("Enviando a ElevenLabs (%s)... puede tardar un par de minutos." % modelo)
                with urllib.request.urlopen(req, timeout=900) as r:
                    return json.loads(r.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                detalle = e.read().decode("utf-8", "ignore")[:300]
                if e.code in (429, 500, 502, 503) and intento < 3:
                    print("   ElevenLabs esta ocupado, reintento..."); time.sleep(8 * (intento + 1)); continue
                if e.code in (400, 422) and "model" in detalle.lower() and modelo != MODELOS[-1]:
                    print("   El modelo %s no esta disponible, pruebo el siguiente." % modelo); break
                salir("Error de ElevenLabs (%d): %s" % (e.code, detalle))
            except urllib.error.URLError as e:
                if intento < 3: time.sleep(5); continue
                salir("No hay conexion con ElevenLabs: %s" % e)
    salir("No he podido transcribir el archivo.")

# ---------------------------------------------------------------- analisis
def turnos(resp):
    """Agrupa las palabras en turnos de palabra por hablante."""
    T = []
    for w in resp.get("words", []):
        tipo = w.get("type", "word")
        if tipo == "spacing": continue
        sp = w.get("speaker_id") or "speaker_0"
        txt = w.get("text", "").strip()
        if not txt: continue
        if tipo == "audio_event": txt = "(" + txt.strip("()[]") + ")"
        if T and T[-1]["sp"] == sp:
            T[-1]["w"].append((txt, w.get("start", 0), w.get("end", 0), tipo))
        else:
            T.append({"sp": sp, "w": [(txt, w.get("start", 0), w.get("end", 0), tipo)]})
    return T

def quien_es_quien(T, cambiar):
    cuenta = {}
    for t in T: cuenta[t["sp"]] = cuenta.get(t["sp"], 0) + sum(1 for x in t["w"] if x[3] == "word")
    if set(cuenta) <= {"PROFESORA", "ESTUDIANTE"}:      # varios audios ya unidos: los papeles vienen fijados
        r = {k: k for k in cuenta}
        if cambiar: r = {k: ("ESTUDIANTE" if k == "PROFESORA" else "PROFESORA") for k in cuenta}
        return r, cuenta
    orden = sorted(cuenta, key=lambda k: -cuenta[k])
    est = orden[0] if orden else "speaker_0"          # por defecto, el estudiante es quien mas habla
    # Mejor pista: la profesora es quien anuncia las tareas ("tarea dos", "la segunda tarea"...)
    anuncia = {}
    for t in T:
        ws = [norm(x[0]) for x in t["w"] if x[3] == "word"]
        for i, w in enumerate(ws):
            if w == "tarea" and ((i + 1 < len(ws) and ws[i + 1] in NUM) or (i > 0 and ws[i - 1] in ("primera", "segunda", "tercera"))):
                anuncia[t["sp"]] = anuncia.get(t["sp"], 0) + 1
    if anuncia and len(orden) > 1:
        prof = max(anuncia, key=lambda k: anuncia[k])
        est = [k for k in orden if k != prof][0]
    if cambiar and len(orden) > 1: est = orden[1]
    return {k: ("ESTUDIANTE" if k == est else "PROFESORA") for k in cuenta}, cuenta

def cortes_tareas(T):
    """Busca 'tarea uno/dos/tres' (o 'tarea 1/2/3') y devuelve el segundo en que empieza cada tarea."""
    plano = [(norm(x[0]), x[1]) for t in T for x in t["w"] if x[3] == "word"]
    cortes, siguiente = {}, 1
    for i in range(len(plano) - 1):
        if plano[i][0] == "tarea" and NUM.get(plano[i + 1][0]) == siguiente:
            cortes[siguiente] = plano[i][1]; siguiente += 1
            if siguiente > 3: break
    return cortes

def tarea_de(seg, cortes):
    n = 0
    for k in sorted(cortes):
        if seg >= cortes[k] - 0.01: n = k
    return n

def analizar(resp, cambiar=False):
    T = turnos(resp)
    roles, cuenta = quien_es_quien(T, cambiar)
    cortes = dict(CORTES_MANUALES) if CORTES_MANUALES else cortes_tareas(T)
    datos = {}
    for t in T:
        rol = roles[t["sp"]]
        for txt, ini, fin, tipo in t["w"]:
            d = datos.setdefault(tarea_de(ini, cortes), {"ini": ini, "fin": fin, "est_seg": 0.0, "est_pal": 0,
                                                         "pausas": [], "mul": {}, "lineas": []})
            d["fin"] = max(d["fin"], fin)
    # tiempo, palabras, pausas y muletillas del estudiante
    for t in T:
        rol = roles[t["sp"]]
        ws = [x for x in t["w"] if x[3] == "word"]
        if rol != "ESTUDIANTE" or not ws: continue
        for j, (txt, ini, fin, tipo) in enumerate(ws):
            d = datos[tarea_de(ini, cortes)]
            d["est_pal"] += 1
            d["est_seg"] += max(0.0, fin - ini)
            if j > 0:
                hueco = ini - ws[j - 1][2]
                if hueco >= PAUSA_LARGA: d["pausas"].append((ws[j - 1][2], hueco))
                elif 0 < hueco < 1.2: d["est_seg"] += hueco   # pausas cortas cuentan como habla seguida
        texto = " " + norm(" ".join(x[0] for x in ws)) + " "
        for m in MULETILLAS:
            c = texto.count(" " + m + " ")
            if c:
                d = datos[tarea_de(ws[0][1], cortes)]
                d["mul"][m] = d["mul"].get(m, 0) + c
    return T, roles, cuenta, cortes, datos

# ---------------------------------------------------------------- texto de salida
OBJETIVO = {1: "2-3 min", 2: "2-3 min", 3: "3-4 min"}

def escribir(resp, archivo_audio, nombre, cambiar=False):
    T, roles, cuenta, cortes, datos = analizar(resp, cambiar)
    L = ["TRANSCRIPCION DE LA PRUEBA ORAL", "Estudiante: " + (nombre or "-"),
         "Grabacion: " + os.path.basename(archivo_audio), "Fecha: " + datetime.date.today().strftime("%d/%m/%Y"), ""]
    L.append("Hablantes detectados: " + ", ".join("%s = %s (%d palabras)" % (k, roles[k], cuenta[k]) for k in cuenta))
    L.append("(Si estan al reves, vuelve a ejecutar con --rehacer y --cambiar.)")
    if CORTES_MANUALES:
        L.append("Tareas divididas a mano: " + ", ".join("tarea %d desde %s" % (k, mmss(v)) for k, v in sorted(cortes.items())))
    elif not cortes:
        L.append("AVISO: en la grabacion nadie dice «Tarea uno/dos/tres», asi que sale todo junto.")
        L.append("Para dividirla, mira en la transcripcion el minuto en que empiezan la tarea 2 y la 3 y repite con:")
        L.append("   python3 transcribir_oral.py --rehacer <este .json> --tareas 2:40,5:15   (sin volver a pagar)")
    elif len(cortes) < 3:
        L.append("AVISO: solo he encontrado las marcas de la tarea %s. Puedes dividirla a mano con --rehacer y --tareas."
                 % ", ".join(str(k) for k in sorted(cortes)))
    L.append("AVISO: el transcriptor puede corregir solo algunos errores del estudiante. Antes de poner")
    L.append("la nota de corrección, contrasta con el audio las frases dudosas. La pronunciacion no sale aqui.")
    L += ["", "=" * 70, "DATOS DE FLUIDEZ DEL ESTUDIANTE (orientativos)", "=" * 70]
    for n in sorted(datos):
        d = datos[n]
        if n == 0 and d["est_pal"] == 0 and cortes: continue
        tit = "Tarea %d" % n if n else ("Toda la prueba" if not cortes else "Antes de empezar")
        dur = d["fin"] - d["ini"]
        ppm = ("%d" % round(d["est_pal"] / (d["est_seg"] / 60.0))) if d["est_seg"] > 5 else "-"
        L.append("%s · duracion %s%s" % (tit, mmss(dur), (" (objetivo %s)" % OBJETIVO[n]) if n in OBJETIVO else ""))
        L.append("   Habla del estudiante: %s · %d palabras · %s palabras por minuto"
                 % (mmss(d["est_seg"]), d["est_pal"], ppm))
        L.append("   Silencios de %d s o mas: %d%s" % (PAUSA_LARGA, len(d["pausas"]),
                 (" (" + ", ".join("%s: %d s" % (mmss(a), round(b)) for a, b in d["pausas"][:8]) + ")") if d["pausas"] else ""))
        if d["mul"]:
            L.append("   Muletillas o relleno: " + ", ".join("%s ×%d" % (k, v) for k, v in sorted(d["mul"].items(), key=lambda x: -x[1])))
    L += ["", "=" * 70, "TRANSCRIPCION", "=" * 70]
    actual = None
    for t in T:
        ini = t["w"][0][1]
        n = tarea_de(t["w"][-1][1], cortes)   # el turno que dice "Tarea dos" ya va en la tarea 2
        if n != actual:
            actual = n
            L += ["", "--- " + ("TAREA %d" % n if n else ("TODA LA PRUEBA" if not cortes else "ANTES DE EMPEZAR")) + " ---"]
        piezas, prev = [], None
        for txt, a, b, tipo in t["w"]:
            if prev is not None and roles[t["sp"]] == "ESTUDIANTE" and a - prev >= PAUSA_LARGA:
                piezas.append("[pausa %d s]" % round(a - prev))
            piezas.append(txt); prev = b
        frase = re.sub(r"\s+([,.;:?!])", r"\1", " ".join(piezas))
        L.append("[%s] %s: %s" % (mmss(ini), "P" if roles[t["sp"]] == "PROFESORA" else "E", frase))
    total = max((x[2] for t in T for x in t["w"]), default=0)
    L += ["", "Duracion total transcrita: %s · coste aproximado: %d creditos" % (mmss(total), round(total / 60 * 330))]
    return "\n".join(L) + "\n"

CORTES_MANUALES = None

def unir(resps):
    """Une las transcripciones de varios audios en una sola, con el tiempo seguido y los papeles fijados."""
    words, desfase = [], 0.0
    for resp in resps:
        T = turnos(resp)
        roles, _ = quien_es_quien(T, False)
        fin = 0.0
        for w in resp.get("words", []):
            x = dict(w)
            sp = w.get("speaker_id") or "speaker_0"
            x["speaker_id"] = roles.get(sp, "ESTUDIANTE")
            if "start" in x: x["start"] = (x.get("start") or 0) + desfase
            if "end" in x: x["end"] = (x.get("end") or 0) + desfase; fin = max(fin, x["end"])
            words.append(x)
        desfase = fin + 2.0
    return {"text": " ".join(r.get("text", "") for r in resps), "words": words}

def elegir_archivos():
    """Sin archivo en el comando: en el Mac se abre una ventana para elegir una o varias grabaciones."""
    if sys.platform == "darwin":
        scr = ('set f to choose file with prompt "Elige la grabacion del oral (si son varias, seleccionalas todas con Cmd)" with multiple selections allowed\n'
               'set r to ""\nrepeat with x in f\nset r to r & POSIX path of x & linefeed\nend repeat\nreturn r')
        r = os.popen("osascript -e '%s' 2>/dev/null" % scr.replace("'", "'\\''")).read()
        r = [x.strip() for x in r.splitlines() if x.strip()]
        if r: return sorted(r, key=lambda x: os.path.basename(x).lower())
    salir("Falta la grabacion. Escribe el comando y arrastra el archivo (o los archivos) de audio a la ventana de Terminal.")

# ---------------------------------------------------------------- main
def main():
    a = sys.argv[1:]
    if not a: salir(__doc__)
    nombre, cambiar = "", "--cambiar" in a
    if "--nombre" in a:
        i = a.index("--nombre"); nombre = a[i + 1] if i + 1 < len(a) else ""; del a[i:i + 2]
    manual = None
    if "--tareas" in a:
        i = a.index("--tareas"); manual = a[i + 1] if i + 1 < len(a) else ""; del a[i:i + 2]
        global CORTES_MANUALES
        try:
            CORTES_MANUALES = {1: 0.0}
            for n, m in enumerate(x for x in manual.split(",") if x.strip()):
                mm, ss = m.strip().split(":"); CORTES_MANUALES[n + 2] = int(mm) * 60 + int(ss)
        except ValueError:
            salir('No entiendo --tareas. Escribelo asi: --tareas 2:40,5:15 (minuto:segundo de la tarea 2 y de la 3)')
    a = [x for x in a if x != "--cambiar"]
    if not a or (a[0] != "--rehacer" and not a[0].strip()):
        a = elegir_archivos()
    os.makedirs(SALIDA, exist_ok=True)
    if a and a[0] == "--rehacer":
        if len(a) < 2: salir("Falta el .json: python3 transcribir_oral.py --rehacer Oral_xxx.json")
        js = a[1] if os.path.exists(a[1]) else os.path.join(SALIDA, a[1])
        if not os.path.exists(js): salir("No encuentro " + a[1])
        guardado = json.load(open(js, encoding="utf-8"))
        txt = escribir(guardado["respuesta"], guardado["audio"], nombre or guardado.get("nombre", ""), cambiar)
        destino = js[:-5] + ".txt"
    else:
        audios = [x.strip().strip("'\"") for x in a]
        for x in audios:
            if not os.path.exists(x): salir("No encuentro el archivo: " + x)
        if len(audios) > 1:
            print("Voy a unir %d grabaciones, en este orden:" % len(audios))
            for i, x in enumerate(audios): print("  %d. %s" % (i + 1, os.path.basename(x)))
        clave = "" if os.environ.get("DELE_PRUEBA") else leer_clave()
        resps = []
        for x in audios:
            if len(audios) > 1: print("\n" + os.path.basename(x))
            resps.append(transcribir(clave, x))
        resp = resps[0] if len(resps) == 1 else unir(resps)
        audio = audios[0] if len(audios) == 1 else " + ".join(os.path.basename(x) for x in audios)
        base = "Oral_%s_%s" % (re.sub(r"\W+", "_", nombre).strip("_") or "estudiante",
                               datetime.datetime.now().strftime("%Y-%m-%d_%H%M"))
        json.dump({"audio": audio, "nombre": nombre, "respuesta": resp},
                  open(os.path.join(SALIDA, base + ".json"), "w", encoding="utf-8"), ensure_ascii=False)
        txt = escribir(resp, audio, nombre, cambiar)
        destino = os.path.join(SALIDA, base + ".txt")
    open(destino, "w", encoding="utf-8").write(txt)
    print("\nListo: " + destino)
    if sys.platform == "darwin": os.system('open "%s"' % destino)

if __name__ == "__main__":
    main()
