#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERADOR DE AUDIOS DELE A2 y B2 (ElevenLabs)
Uso (en Terminal, dentro de esta carpeta):
    python3 generar_audios.py U01_guion.txt              -> genera los audios de la unidad
    python3 generar_audios.py U01_guion.txt --contar     -> solo cuenta caracteres (no gasta creditos)
    python3 generar_audios.py U01_guion.txt --rehacer "texto"  -> vuelve a generar las frases que contienen ese texto
    python3 generar_audios.py --voces   -> crea voces_disponibles.txt con todas tus voces (nombre, ID, acento, sexo, edad)

Efectos de sonido (antes de hablar, nunca debajo de la voz):
    SONIDO: descripcion en ingles            -> efecto de 2 segundos
    SONIDO 1.5: descripcion en ingles        -> efecto de 1,5 segundos
Se generan una sola vez con la API de efectos de ElevenLabs y se guardan en la cache.

Perfil radio (noticias, locutores, mensajes): LUCIA/RADIO: texto  -> se genera con eleven_v3, el fragmento entero de una vez.
Monologos naturales (B2, auditiva T4...): SUSANA/V3: texto -> igual que /RADIO (v3, entero), sin pausas de locutor.
Volumen: todas las voces se igualan solas al mismo nivel (narrador, conversaciones y monologos).
Marcas de voz (solo en conversaciones, modelo v3): [laughs], [sighs], [hesitates]...
Si ElevenLabs no puede hacer la conversacion entera y pasa a frase a frase, las marcas se quitan solas.
Conversaciones largas (entrevistas B2): se cortan solas en trozos por turnos de palabra.
Oct. 2026: el recorte del final ya no se come las consonantes suaves del final (la -s de "molestias").

Necesita en esta misma carpeta:
    clave.txt  -> tu API key de ElevenLabs (una sola linea)
    voces.txt  -> el ID de cada voz (0, A, B, C, D, E, F)
Cada frase se guarda en la carpeta "cache": si una frase ya existe (por ejemplo las del narrador,
que se repiten en todas las unidades) no se vuelve a pagar.
"""
import sys, os, json, hashlib, wave, subprocess, time, shutil
import urllib.request, urllib.error

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, "cache")
SALIDA = os.path.join(AQUI, "salida")
RATE = 24000
MODELO = "eleven_multilingual_v2"
PAUSA_ENTRE_FRASES = 0.25   # segundos que se anaden solos despues de cada frase

AJUSTES_NARRADOR = {"stability": 0.80, "similarity_boost": 0.90, "style": 0.0, "use_speaker_boost": True, "speed": 0.95}
AJUSTES_PERSONAJE = {"stability": 0.45, "similarity_boost": 0.80, "style": 0.25, "use_speaker_boost": True, "speed": 1.0}
# Perfil "radio" para noticias y locutores (VOZ/RADIO: texto): se genera con eleven_v3, como las conversaciones,
# porque da un ritmo mas natural. Estos ajustes solo se usan si v3 falla (plan B frase a frase).
AJUSTES_RADIO = {"stability": 0.40, "similarity_boost": 0.80, "style": 0.35, "use_speaker_boost": True, "speed": 1.0}
MODELO_DIALOGO = "eleven_v3"   # las conversaciones se generan de una vez, con varias voces, para que suenen naturales
PAUSA_DIALOGO = 0.15          # pausa extra minima tras un dialogo (el propio dialogo ya trae sus pausas)
PAUSA_RADIO = 0.5             # silencio entre frases de una noticia (VOZ/RADIO): da respiro y hace el ritmo mas pausado
LIMITE_DIALOGO = 2500         # caracteres maximos por peticion de conversacion; si hay mas, se corta por turnos

import re
def sin_marcas(t): return re.sub(r"\s*\[[a-zA-Z ]+\]\s*", " ", t).strip()

def aviso(t): print(t, flush=True)

class Voces(dict):
    """Diccionario de voces que entiende el perfil: LYDIA/RADIO busca el ID de LYDIA."""
    def __getitem__(self, k): return dict.__getitem__(self, k.split("/")[0])
    def get(self, k, d=None): return dict.get(self, k.split("/")[0], d)

def leer_config(necesita_clave=True):
    clave = ""
    ruta_clave = os.path.join(AQUI, "clave.txt")
    if necesita_clave:
        if not os.path.exists(ruta_clave):
            sys.exit("Falta el archivo clave.txt con tu API key de ElevenLabs.")
        clave = open(ruta_clave, encoding="utf-8").read().strip()
        if not clave or "PEGA" in clave:
            sys.exit("El archivo clave.txt esta vacio: pega dentro tu API key.")
    voces = Voces()
    ruta_voces = os.path.join(AQUI, "voces.txt")
    if not os.path.exists(ruta_voces):
        sys.exit("Falta el archivo voces.txt.")
    for linea in open(ruta_voces, encoding="utf-8"):
        linea = linea.split("#")[0].strip()
        if "=" in linea:
            k, v = linea.split("=", 1)
            v = v.strip()
            if v and "PEGA" not in v:
                voces[k.strip().upper()] = v
    return clave, voces

def leer_guion(ruta):
    """Devuelve lista de (archivo, [piezas]); pieza = ('voz', letra, texto) o ('sil', segundos)."""
    archivos, actual = [], None
    for n, bruta in enumerate(open(ruta, encoding="utf-8"), 1):
        linea = bruta.strip()
        if not linea:
            continue
        if linea.startswith("# ARCHIVO"):
            actual = (linea.split("ARCHIVO", 1)[1].strip(), [])
            archivos.append(actual)
            continue
        if linea.startswith("#"):
            continue
        if actual is None:
            sys.exit("Linea %d: falta '# ARCHIVO nombre' antes del texto." % n)
        if linea.startswith("[") and linea.endswith("]"):
            actual[1].append(("sil", float(linea[1:-1].replace(",", "."))))
            continue
        if ":" not in linea:
            sys.exit("Linea %d: no entiendo esta linea (falta 'VOZ: texto'):\n  %s" % (n, linea))
        voz, texto = linea.split(":", 1)
        voz = voz.strip().upper()
        if voz.startswith("SONIDO"):
            resto = voz[6:].strip().replace(",", ".")
            actual[1].append(("son", texto.strip(), float(resto) if resto else 2.0))
            continue
        actual[1].append(("voz", voz, texto.strip()))
    return archivos

def ajustes(voz): return AJUSTES_NARRADOR if voz == "0" else (AJUSTES_RADIO if voz.endswith("/RADIO") else AJUSTES_PERSONAJE)

def clave_cache(voz, voice_id, texto):
    h = hashlib.sha1((voice_id + "|" + texto + "|" + json.dumps(ajustes(voz), sort_keys=True) + "|" + MODELO).encode("utf-8")).hexdigest()[:16]
    return os.path.join(CACHE, "%s_%s.pcm" % (voz.replace("/", "-"), h))

def pedir_tts(clave, voice_id, voz, texto):
    if os.environ.get("DELE_PRUEBA"):          # modo prueba sin internet: genera un pitido
        import math
        n = int(RATE * max(0.5, len(texto) / 15.0))
        return b"".join(int(3000 * math.sin(2 * math.pi * 440 * i / RATE)).to_bytes(2, "little", signed=True) for i in range(n))
    url = "https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=pcm_%d" % (voice_id, RATE)
    cuerpo = json.dumps({"text": texto, "model_id": MODELO, "voice_settings": ajustes(voz)}).encode("utf-8")
    for intento in range(5):
        req = urllib.request.Request(url, data=cuerpo, method="POST",
                                     headers={"xi-api-key": clave, "Content-Type": "application/json", "Accept": "audio/pcm"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            detalle = e.read().decode("utf-8", "ignore")[:300]
            if e.code in (429, 500, 502, 503) and intento < 4:
                aviso("   ElevenLabs esta ocupado, reintento en unos segundos...")
                time.sleep(5 * (intento + 1)); continue
            sys.exit("\nError de ElevenLabs (%d): %s\nRevisa la API key y los IDs de voces.txt." % (e.code, detalle))
        except urllib.error.URLError as e:
            if intento < 4:
                time.sleep(3); continue
            sys.exit("\nNo hay conexion con ElevenLabs: %s" % e)

def listar_voces():
    clave, _ = leer_config(necesita_clave=True) if os.path.exists(os.path.join(AQUI, "voces.txt")) else (open(os.path.join(AQUI, "clave.txt"), encoding="utf-8").read().strip(), {})
    req = urllib.request.Request("https://api.elevenlabs.io/v1/voices", headers={"xi-api-key": clave})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            datos = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit("Error de ElevenLabs (%d): %s" % (e.code, e.read().decode("utf-8", "ignore")[:300]))
    filas = []
    for v in datos.get("voices", []):
        if v.get("category") == "premade":
            continue
        et = v.get("labels") or {}
        filas.append("%s | %s | %s | %s | %s | %s" % (v.get("name", ""), v.get("voice_id", ""), et.get("accent", ""), et.get("gender", ""), et.get("age", ""), et.get("use_case", "") or et.get("descriptive", "")))
    filas.sort()
    ruta = os.path.join(AQUI, "voces_disponibles.txt")
    open(ruta, "w", encoding="utf-8").write("NOMBRE | ID | ACENTO | SEXO | EDAD | USO\n" + "\n".join(filas) + "\n")
    aviso("He encontrado %d voces. Estan en voces_disponibles.txt" % len(filas))

def clave_dialogo(lineas):
    h = hashlib.sha1((json.dumps(lineas, ensure_ascii=False) + "|" + MODELO_DIALOGO).encode("utf-8")).hexdigest()[:16]
    return os.path.join(CACHE, "DIALOGO_%s.pcm" % h)

def pedir_dialogo(clave, lineas):
    """lineas = [(voice_id, texto), ...]. Devuelve pcm o None si el modo dialogo no esta disponible."""
    if os.environ.get("DELE_PRUEBA"):
        return b"".join(pedir_tts(clave, v, "X", t) for v, t in lineas)
    url = "https://api.elevenlabs.io/v1/text-to-dialogue?output_format=pcm_%d" % RATE
    cuerpo = json.dumps({"inputs": [{"text": t, "voice_id": v} for v, t in lineas], "model_id": MODELO_DIALOGO,
                         "settings": {"stability": 0.5}}).encode("utf-8")
    for intento in range(5):
        req = urllib.request.Request(url, data=cuerpo, method="POST",
                                     headers={"xi-api-key": clave, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            detalle = e.read().decode("utf-8", "ignore")[:300]
            if e.code in (429, 500, 502, 503) and intento < 4:
                aviso("   ElevenLabs esta ocupado, reintento en unos segundos...")
                time.sleep(5 * (intento + 1)); continue
            aviso("   AVISO: el modo conversacion no esta disponible (%d: %s). Genero frase a frase." % (e.code, detalle[:150]))
            return None
        except urllib.error.URLError:
            if intento < 4:
                time.sleep(3); continue
            return None

def clave_sonido(texto, dur):
    h = hashlib.sha1(("%s|%.2f" % (texto, dur)).encode("utf-8")).hexdigest()[:16]
    return os.path.join(CACHE, "SONIDO_%s.pcm" % h)

def pedir_sonido(clave, texto, dur):
    """Genera un efecto con la API de efectos de ElevenLabs y lo devuelve como PCM 24 kHz mono, a volumen moderado."""
    import array
    if os.environ.get("DELE_PRUEBA"):
        import math
        n = int(RATE * dur)
        return b"".join(int(2000 * math.sin(2 * math.pi * 880 * i / RATE)).to_bytes(2, "little", signed=True) for i in range(n))
    if not shutil.which("afconvert"):
        sys.exit("Para los efectos de sonido hace falta afconvert (viene con el Mac).")
    cuerpo = json.dumps({"text": texto, "duration_seconds": dur, "prompt_influence": 0.6}).encode("utf-8")
    for intento in range(5):
        req = urllib.request.Request("https://api.elevenlabs.io/v1/sound-generation", data=cuerpo, method="POST",
                                     headers={"xi-api-key": clave, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                mp3 = r.read(); break
        except urllib.error.HTTPError as e:
            detalle = e.read().decode("utf-8", "ignore")[:300]
            if e.code in (429, 500, 502, 503) and intento < 4:
                aviso("   ElevenLabs esta ocupado, reintento en unos segundos...")
                time.sleep(5 * (intento + 1)); continue
            sys.exit("\nError de ElevenLabs con el efecto de sonido (%d): %s" % (e.code, detalle))
        except urllib.error.URLError as e:
            if intento < 4:
                time.sleep(3); continue
            sys.exit("\nNo hay conexion con ElevenLabs: %s" % e)
    tmp_mp3 = os.path.join(CACHE, "_tmp_sonido.mp3"); tmp_wav = os.path.join(CACHE, "_tmp_sonido.wav")
    open(tmp_mp3, "wb").write(mp3)
    subprocess.run(["afconvert", "-f", "WAVE", "-d", "LEI16@%d" % RATE, "-c", "1", tmp_mp3, tmp_wav], check=True)
    with wave.open(tmp_wav, "rb") as w:
        datos = w.readframes(w.getnframes())
    os.remove(tmp_mp3); os.remove(tmp_wav)
    a = array.array("h"); a.frombytes(datos)
    pico = max((abs(x) for x in a), default=0)
    if pico:
        f = 12000.0 / pico          # pico a unos -8 dB: suave, por debajo de la voz
        a = array.array("h", (int(x * f) for x in a))
    return a.tobytes()

def limpiar_final(datos):
    """Quita el ruido del final (respiracion cortada) y suaviza la entrada y la salida para que no haya chasquidos.
    No toca la cache: se aplica al montar el audio.
    Oct. 2026: antes cortaba 150 ms despues de la ultima silaba fuerte y se comia las consonantes suaves
    del final (la -s de "molestias", "nosotros"). Ahora, desde la ultima silaba fuerte, sigue mientras haya
    voz suave pegada (una -s, una -n), hasta 0,6 s; solo corta en el primer silencio de verdad. Una
    respiracion que llega despues de ese silencio se sigue quitando."""
    import array
    a = array.array("h"); a.frombytes(datos)
    v = int(RATE * 0.02)                                  # ventanas de 20 ms
    if len(a) > v * 10:
        rms = [(sum(x * x for x in a[i:i + v]) / v) ** 0.5 for i in range(0, len(a) - v, v)]
        tope = max(rms)
        fuerte = [i for i, r in enumerate(rms) if r > tope * 0.10]
        if fuerte:
            j = fuerte[-1] + 1
            limite = min(len(rms), j + int(0.6 / 0.02))   # como mucho 0,6 s de consonante o cola suave
            while j < limite and rms[j] > tope * 0.015:    # -s, -n, final de la voz: energia baja pero continua
                j += 1
            fin = min(len(a), j * v + int(RATE * 0.12))    # 120 ms de margen despues del ultimo sonido
            a = a[:fin]
    n_in, n_out = min(len(a), int(RATE * 0.01)), min(len(a), int(RATE * 0.08))
    for i in range(n_in): a[i] = int(a[i] * i / n_in)
    for i in range(n_out): a[len(a) - 1 - i] = int(a[len(a) - 1 - i] * i / n_out)
    return a.tobytes()

NIVEL_VOZ = 2600     # volumen medio (RMS de las partes con voz) al que se igualan todas las piezas
def normalizar(pcm):
    """Iguala el volumen de una pieza de voz: mismo nivel medio para todas las voces, sin saturar."""
    import array, math
    a = array.array("h"); a.frombytes(bytes(pcm))
    if not a: return pcm
    voz = [x for x in a if abs(x) > 300]
    if len(voz) < RATE // 10: return pcm
    rms = math.sqrt(sum(x * x for x in voz) / len(voz))
    pico = max(abs(x) for x in a)
    g = min(NIVEL_VOZ / rms if rms else 1.0, 30000.0 / pico if pico else 1.0, 3.0)
    if 0.92 < g < 1.08: return pcm
    return array.array("h", (max(-32767, min(32767, int(x * g))) for x in a)).tobytes()

def trocear(bloque):
    """Corta una conversacion larga en trozos de LIMITE_DIALOGO caracteres como maximo, siempre entre turnos."""
    trozos, actual, n = [], [], 0
    for x in bloque:
        if actual and n + len(x[2]) > LIMITE_DIALOGO:
            trozos.append(actual); actual, n = [], 0
        actual.append(x); n += len(x[2])
    if actual: trozos.append(actual)
    return trozos

def cerrar(bloque, salida):
    """Varias voces -> conversacion (v3). Una sola voz (monologo, varios parrafos) -> frase a frase."""
    if len(bloque) > 1 and len(set(x[1] for x in bloque)) > 1:
        for t in trocear(bloque):
            if len(set(x[1] for x in t)) > 1:
                salida.append(("dialogo", t))
            else:
                salida.extend(t)
    else:
        for x in bloque:
            if not x[1].endswith(("/RADIO", "/V3")):
                salida.append(x); continue
            # El fragmento entero de una vez (antes iba frase a frase: sonaba enlatado y cortaba respiraciones).
            # Solo si es muy largo se parte, siempre entre frases.
            frases = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡«])", x[2])
            trozo = ""
            for f in frases:
                if trozo and len(trozo) + len(f) > LIMITE_DIALOGO:
                    salida.append(("dialogo", [(x[0], x[1], trozo)])); salida.append(("sil", PAUSA_RADIO)); trozo = ""
                trozo = (trozo + " " + f).strip()
            if trozo: salida.append(("dialogo", [(x[0], x[1], trozo)]))

def agrupar(piezas):
    """Junta las frases seguidas de personajes (sin silencio entre ellas) en un bloque de dialogo."""
    salida, bloque = [], []
    for p in piezas:
        if p[0] == "voz" and p[1] != "0":
            bloque.append(p); continue
        if bloque:
            cerrar(bloque, salida); bloque = []
        salida.append(p)
    if bloque:
        cerrar(bloque, salida)
    return salida

def main():
    args = sys.argv[1:]
    if args and args[0] == "--voces":
        return listar_voces()
    if not args:
        sys.exit(__doc__)
    ruta = args[0] if os.path.isabs(args[0]) else os.path.join(AQUI, args[0])
    contar = "--contar" in args
    rehacer = args[args.index("--rehacer") + 1].lower() if "--rehacer" in args else None
    clave, voces = leer_config(necesita_clave=not contar)
    archivos = leer_guion(ruta)
    os.makedirs(CACHE, exist_ok=True); os.makedirs(SALIDA, exist_ok=True)

    faltan = set(p[1] for _, piezas in archivos for p in piezas if p[0] == "voz" and not voces.get(p[1]))
    if faltan and not contar:
        sys.exit("En voces.txt falta el ID de: %s" % ", ".join(sorted(faltan)))

    # contar caracteres nuevos (los que no estan en cache)
    vistos, nuevos, total, dvistos = set(), 0, 0, set()
    for _, piezas in archivos:
        for g in agrupar(piezas):
            if g[0] == "dialogo":
                k = tuple((x[1], x[2]) for x in g[1])
                if k in dvistos: continue
                dvistos.add(k)
                for x in g[1]: vistos.add((x[1], x[2]))
                if contar or not os.path.exists(clave_dialogo([(voces.get(x[1], ""), x[2]) for x in g[1]])):
                    nuevos += sum(len(x[2]) for x in g[1])
            elif g[0] == "voz":
                k = (g[1], g[2])
                if k in vistos: continue
                vistos.add(k)
                if contar or not os.path.exists(clave_cache(g[1], voces.get(g[1], ""), g[2])):
                    nuevos += len(g[2])
    sonidos = set((p[1], p[2]) for _, piezas in archivos for p in piezas if p[0] == "son")
    son_nuevos = [x for x in sonidos if contar or not os.path.exists(clave_sonido(*x))]
    aviso("Frases distintas: %d · caracteres que se van a generar ahora: %d" % (len(vistos), nuevos))
    if sonidos:
        aviso("Efectos de sonido distintos: %d · nuevos (se pagan aparte): %d" % (len(sonidos), len(son_nuevos)))
    if contar:
        return

    if rehacer:
        borradas = 0
        for voz, texto in vistos:
            if rehacer in texto.lower():
                f = clave_cache(voz, voces[voz], texto)
                if os.path.exists(f): os.remove(f); borradas += 1
        for nombre, piezas in archivos:
            for g in agrupar(piezas):
                if g[0] == "dialogo" and any(rehacer in x[2].lower() for x in g[1]):
                    f = clave_dialogo([(voces[x[1]], x[2]) for x in g[1]])
                    if os.path.exists(f): os.remove(f); borradas += 1
        for t, d in sonidos:
            if rehacer in t.lower():
                f = clave_sonido(t, d)
                if os.path.exists(f): os.remove(f); borradas += 1
        aviso("Voy a rehacer %d frase(s) o conversacion(es) que contienen '%s'." % (borradas, rehacer))

    hechas = 0
    for nombre, piezas in archivos:
        aviso("\n== %s ==" % nombre)
        pcm = bytearray()
        for p in agrupar(piezas):
            if p[0] == "sil":
                pcm += b"\x00\x00" * int(RATE * p[1]); continue
            if p[0] == "son":
                f = clave_sonido(p[1], p[2])
                if not os.path.exists(f):
                    hechas += 1
                    aviso("  generando efecto: %s" % p[1][:60])
                    open(f, "wb").write(pedir_sonido(clave, p[1], p[2]))
                pcm += open(f, "rb").read()
                pcm += b"\x00\x00" * int(RATE * 0.4)
                continue
            if p[0] == "dialogo":
                lineas = [(voces[x[1]], x[2]) for x in p[1]]
                f = clave_dialogo(lineas)
                if not os.path.exists(f):
                    aviso("  generando conversacion: %s..." % p[1][0][2][:55])
                    datos = pedir_dialogo(clave, lineas)
                    if datos:
                        hechas += 1
                        open(f, "wb").write(datos)
                if os.path.exists(f):
                    pcm += normalizar(limpiar_final(open(f, "rb").read()))
                    pcm += b"\x00\x00" * int(RATE * PAUSA_DIALOGO)
                    continue
                sueltas = p[1]          # plan B: frase a frase
            else:
                sueltas = [p]
            for q in sueltas:
                voz, texto = q[1], sin_marcas(q[2])
                f = clave_cache(voz, voces[voz], texto)
                if not os.path.exists(f):
                    hechas += 1
                    aviso("  generando [%s] %s" % (voz, texto[:70]))
                    datos = pedir_tts(clave, voces[voz], voz, texto)
                    open(f, "wb").write(datos)
                pcm += normalizar(open(f, "rb").read())
                pcm += b"\x00\x00" * int(RATE * PAUSA_ENTRE_FRASES)
        wav = os.path.join(SALIDA, nombre + ".wav")
        with wave.open(wav, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(bytes(pcm))
        dur = len(pcm) / 2 / RATE
        final = wav
        if shutil.which("afconvert"):
            m4a = os.path.join(SALIDA, nombre + ".m4a")
            subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-b", "64000", wav, m4a], check=True)
            os.remove(wav); final = m4a
        aviso("  listo: %s (%d min %02d s)" % (os.path.basename(final), dur // 60, dur % 60))
    aviso("\nTerminado. Frases nuevas generadas: %d. Los audios estan en la carpeta 'salida'." % hechas)

if __name__ == "__main__":
    main()
