# -*- coding: utf-8 -*-
# GUION EN VIVO para la libreta oral de la profesora (DELE A2) · 2spanishteachers.com
# Lo usa DELE_oral_profesora.py (después de pasarle patch_libreta_vivo.py). Tiene que estar en la misma carpeta.
# Qué hace (María, 23/10/2026: «vienen las dos fotos juntas y no es fácil leer y hablar con el estudiante»):
#   - en cada tarea, solo la opción o la foto que ha elegido el estudiante, arriba y en letra grande;
#   - tarea 1: la lámina y las dos ayudas de ESA opción;
#   - tarea 2: la foto de verdad (o su descripción si no carga), las seis preguntas y las ayudas de ESA foto;
#   - tarea 3: se elige sola con la foto de la tarea 2; TÚ / USTED bien visible; el esquema pauta por pauta
#     (lo que dice usted en grande, la respuesta modelo debajo, el pequeño problema en coral con la solución
#     modelo y otra solución posible); se toca cada paso al terminarlo y se marca el siguiente; el diálogo
#     modelo completo, plegado.
# Los datos salen del guion de la profesora (GUION_ENTREVISTADOR) y, si están, de oralModelos e imgBase.
# Si algo no se puede leer, la libreta enseña el guion de siempre (no se pierde nada).
import re, sys, unicodedata

STOP = set("""para pero como cuando donde quien quién este esta esto esos esas eso algo alguna alguno algun tambien ahora
despues entonces vale hola bien muy mucho mucha todo todos toda todas tiene tienes tenemos tengo hace hacer
oye mira pues bueno claro usted ustedes nosotros vosotros""".split())

def _norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    out = set()
    for w in re.findall(r"[a-zñ]+", s):
        if len(w) < 4 or w in STOP:
            continue
        out.add(w[:5])
    return out

def _pregunta(t):
    """La parte de la frase del examinador que pide algo (lo que contesta el candidato)."""
    q = re.findall(r"¿[^?]*\?", t)
    return " ".join(q) if q else t

def _main_extra():
    m = sys.modules.get("__main__")
    D = getattr(m, "DATA", None)
    if isinstance(D, dict):
        return {"imgBase": D.get("imgBase", ""), "oralModelos": D.get("oralModelos") or {}}
    return {}

def _bloques(guion):
    out, cur = {}, None
    for raw in (guion or "").split("\n"):
        st = raw.strip()
        ind = len(raw) - len(raw.lstrip())
        m = re.match(r"Tarea (\d)", st)
        if m and ind <= 2:
            cur = int(m.group(1))
        elif st.startswith("Qué mirar") and ind <= 2:
            cur = "mirar"
        if cur is not None:
            out.setdefault(cur, []).append(raw.rstrip())
    return out

def _cierra(st, i):
    """Índice del paréntesis que cierra el que se abre en st[i]."""
    n = 0
    for j in range(i, len(st)):
        if st[j] == "(":
            n += 1
        elif st[j] == ")":
            n -= 1
            if n == 0:
                return j
    return -1

def _cabecera(st, palabra):
    """'Foto 1 (rol): texto' -> (0, 'rol', 'texto'); None si no lo es."""
    m = re.match(palabra + r"\s+(\d)\s*\(", st)
    if not m:
        return None
    a = m.end() - 1
    b = _cierra(st, a)
    if b < 0:
        return None
    resto = st[b + 1:].lstrip()
    if resto.startswith(":"):
        resto = resto[1:].strip()
    return int(m.group(1)) - 1, st[a + 1:b].strip(), resto

def _ayudas(lineas):
    res, ult = {}, None
    for raw in lineas:
        st = raw.strip()
        if not st or re.match(r"Tarea \d", st):
            continue
        c = _cabecera(st, r"(?:Opción|Foto)")
        if c:
            ult = c[0]
            res[ult] = {"tema": c[1], "txt": c[2]}
        elif ult is not None:
            res[ult]["txt"] += " " + st
    for k, v in res.items():
        v["ayudas"] = [x.strip() for x in v.pop("txt").split(" · ") if x.strip()]
    return res

GENERAL = re.compile(r"^(Al reaccionar|Qué mirar|En general|Que use|Recuerde)")

def _t3(lineas):
    """Lee el bloque de la tarea 3. Funciona con el guion con sangrías (fuente) y sin ellas (libretas ya hechas)."""
    res = {"intro": [], "notas": [], "ops": {}, "dlg": {}}
    cur, modo, dcur = None, None, None
    plano = all(len(r) == len(r.lstrip()) for r in lineas if r.strip())
    for raw in lineas:
        st = raw.strip()
        if not st:
            continue
        ind = len(raw) - len(raw.lstrip())
        if plano and not re.match(r"(Tarea 3|Foto\s+\d|DIÁLOGO MODELO|El diálogo modelo|Examinador|Candidat)", st):
            # sin sangrías: lo que va detrás de «Foto N» es de esa foto, salvo los consejos generales
            if GENERAL.match(st):
                cur, modo = None, None
            if cur is None:
                ind = 0
            elif re.match(r"^(.+?)\s\.{2,}\s*(.*)$", st) or st.startswith("PEQUEÑO PROBLEMA"):
                ind = 6
            elif res["ops"][cur]["rows"]:
                ind = 6 if re.match(r"^([A-ZÁÉÍÓÚÑ][^¿¡«:]{1,40}?)\s+([¿¡«].*)$", st) else 8
            else:
                ind = 4
            if cur is not None and ind == 4:
                res["ops"][cur]["libre"].append(st)
                continue
        elif plano:
            ind = 4 if st.startswith("Foto") else (6 if st.startswith(("Examinador", "Candidat")) else 0)
        if re.match(r"Tarea 3", st) and ind <= 2:
            res["intro"].append(re.sub(r"^Tarea 3\s*[—·\-]*\s*", "", st))
            continue
        m = re.match(r"DIÁLOGO MODELO\s*·\s*Fotograf[íi]a\s*(\d)", st)
        if m:
            modo, dcur, cur = "dlg", int(m.group(1)) - 1, None
            res["dlg"][dcur] = []
            continue
        if st.startswith("El diálogo modelo"):
            modo, cur = "fuera", None
            continue
        if modo == "dlg" and ind >= 6:
            m = re.match(r"(Examinador|Examinadora|Candidato|Candidata)\s*:\s*(.*)$", st)
            if m:
                res["dlg"][dcur].append(["E" if m.group(1).startswith("Exam") else "C", m.group(2), False])
            continue
        c = _cabecera(st, "Foto") if ind <= 4 else None
        if c:
            cur, modo = c[0], "op"
            res["ops"][cur] = {"rol": c[1], "rows": [], "libre": [c[2]] if c[2] else []}
            continue
        if ind <= 2 or cur is None or modo != "op":
            cur, modo = None, None
            (res["notas"] if res["ops"] else res["intro"]).append(st)
            continue
        op = res["ops"][cur]
        mr = re.match(r"^(.+?)\s\.{2,}\s*(.*)$", st)
        if not mr and ind == 6 and op["rows"]:
            mr = re.match(r"^([A-ZÁÉÍÓÚÑ][^¿¡«:]{1,40}?)\s+([¿¡«].*)$", st)
        if mr and 6 <= ind < 10:
            op["rows"].append({"k": mr.group(1).strip(), "t": mr.group(2).strip()})
        elif op["rows"] and ind >= 6:
            op["rows"][-1]["t"] += " " + st
        else:
            op["libre"].append(st)
    return res

def _filas(rows):
    for r in rows:
        if "PROBLEMA" in r["k"].upper():
            r["p"] = True
            m = re.match(r"^(«.*?»\.?)\s*(.*)$", r["t"])
            if m:
                r["t"], r["h"] = m.group(1), m.group(2)
    return rows

def _frases(libre):
    txt = " ".join(libre).strip()
    if not txt:
        return []
    out = []
    for f in re.split(r"(?<=[.;])\s+(?=\S)", txt):
        f = f.strip()
        if f:
            out.append({"t": f, "p": bool(re.match(r"(Problema|Pequeño problema)\s*:", f))})
    return out

def _trato(rol, intro, modelo):
    if modelo:
        return modelo
    r = rol.lower()
    if re.search(r"\bde usted\b", r):
        return "usted"
    if re.search(r"\bde tú\b", r):
        return "tú"
    i = intro.upper()
    if "DE TÚ" in i:
        return "tú"
    if "DE USTED" in i:
        return "usted"
    # sin dato: amigo, hermano, compañero de piso... = tú; un servicio o alguien que no conoce = usted
    if re.search(r"amig|herman|compañer[oa]/?a? de piso|prim[oa]|novi[oa]|pareja", r):
        return "tú"
    return "usted" if r else ""

def _respuestas(rows, dlg):
    """Pone debajo de cada paso del esquema lo que contesta el candidato en el diálogo modelo."""
    E = [k for k, d in enumerate(dlg) if d[0] == "E"]
    if not rows or not E:
        return
    def resp(k):
        return dlg[k + 1][1] if k + 1 < len(dlg) and dlg[k + 1][0] == "C" else ""
    pe = next((k for k in E if len(dlg[k]) > 2 and dlg[k][2]), None)
    pr = next((j for j, r in enumerate(rows) if r.get("p")), None)
    if pe is None and pr is not None:
        obj = _norm(rows[pr]["t"] + " " + rows[pr].get("h", ""))
        pe = max(E, key=lambda k: len(_norm(dlg[k][1]) & obj))
        dlg[pe][2] = True
    asig = {0: E[0]}
    if pr is not None and pe is not None:
        asig[pr] = pe
    ult = len(rows) - 1
    if ult > 0 and ult not in asig and E[-1] != pe and E[-1] != E[0]:
        asig[ult] = E[-1]
    # el resto de pasos, en orden: alineación que da más palabras en común (la pregunta del examinador
    # y la etiqueta del paso), sin cruzarse con los pasos ya fijados (saludo, problema, despedida)
    fijos = sorted(asig.items())
    for (j0, k0), (j1, k1) in zip(fijos, fijos[1:] + [(len(rows), len(dlg))]):
        R = list(range(j0 + 1, j1))
        C = [k for k in E if k0 < k < k1]
        if not R or not C:
            continue
        sc = [[len(_norm(_pregunta(dlg[k][1])) & _norm(rows[j]["k"] + " " + rows[j]["t"])) for k in C] for j in R]
        dp = [[0] * (len(C) + 1) for _ in range(len(R) + 1)]
        for x in range(1, len(R) + 1):
            for y in range(1, len(C) + 1):
                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1] + sc[x - 1][y - 1] if sc[x - 1][y - 1] else -1)
        x, y = len(R), len(C)
        while x and y:
            if sc[x - 1][y - 1] and dp[x][y] == dp[x - 1][y - 1] + sc[x - 1][y - 1]:
                asig[R[x - 1]] = C[y - 1]; x -= 1; y -= 1
            elif dp[x][y] == dp[x - 1][y]:
                x -= 1
            else:
                y -= 1
    for j, k in asig.items():
        a = resp(k)
        if a:
            rows[j]["a"] = a

def vivo_a2(tasks, oral, guion=None, extra=None):
    """Añade a las tareas A2 los datos del guion en vivo (clave "live"). No cambia nada más."""
    try:
        extra = extra if extra is not None else _main_extra()
        base = (extra or {}).get("imgBase") or ""
        modelos = ((extra or {}).get("oralModelos") or {}).get("t3") or []
        bl = _bloques(guion)
        t1, t2, t3 = oral["t1"], oral["t2"], oral["t3"]
        a1, a2 = _ayudas(bl.get(1, [])), _ayudas(bl.get(2, []))
        tasks[0]["live"] = {"kind": "mono", "ops": [
            {"pautas": o.get("pautas", []), "ayudas": a1.get(i, {}).get("ayudas", []), "tema": a1.get(i, {}).get("tema", "")}
            for i, o in enumerate(t1["ops"])]}
        imgs = [(base + f["img"]) if base and f.get("img") else "" for f in t2["fotos"]]
        tasks[1]["live"] = {"kind": "foto", "preguntas": t2.get("pautas", []), "ops": [
            {"img": imgs[i], "desc": f.get("desc", ""), "ayudas": a2.get(i, {}).get("ayudas", []), "tema": a2.get(i, {}).get("tema", "")}
            for i, f in enumerate(t2["fotos"])]}
        p3 = _t3(bl.get(3, []))
        intro = " ".join(p3["intro"]).strip()
        ops = []
        for i, o in enumerate(t3["ops"]):
            g = p3["ops"].get(i, {})
            m = modelos[i] if i < len(modelos) else {}
            dlg = [[d[0], d[1], bool(d[2]) if len(d) > 2 else False] for d in (m.get("dialogo") or p3["dlg"].get(i) or [])]
            rows = _filas([dict(r) for r in g.get("rows", [])])
            _respuestas(rows, dlg)
            ops.append({"rol": g.get("rol", ""), "trato": _trato(g.get("rol", ""), intro, m.get("trato", "")),
                        "rows": rows, "libre": _frases(g.get("libre", [])), "img": imgs[i] if i < len(imgs) else "",
                        "segunda": m.get("segunda", ""), "problema": m.get("problema", ""), "dialogo": dlg,
                        "pautas": o.get("pautas", []), "intro": o.get("intro", "")})
        tasks[2]["live"] = {"kind": "dial", "intro": intro, "notas": " ".join(p3["notas"]).strip(), "ops": ops}
    except Exception as e:  # la libreta de siempre, sin guion en vivo
        sys.stderr.write("AVISO libreta_vivo: no se ha podido preparar el guion en vivo (%s)\n" % e)
        for t in tasks:
            t.pop("live", None)
    return tasks

def comprobar(tasks):
    """Comprobaciones para el build: devuelve una lista de avisos (vacía si todo está bien)."""
    av = []
    L = [t.get("live") for t in tasks]
    if not all(L):
        return ["no hay guion en vivo"]
    for i, o in enumerate(L[0]["ops"]):
        if not o["ayudas"]:
            av.append("T1 opción %d sin ayudas" % (i + 1))
    for i, o in enumerate(L[1]["ops"]):
        if not o["ayudas"]:
            av.append("T2 foto %d sin ayudas" % (i + 1))
        if not o["img"]:
            av.append("T2 foto %d sin imagen (se verá la descripción)" % (i + 1))
    for i, o in enumerate(L[2]["ops"]):
        if not o["rows"] and not o["libre"]:
            av.append("T3 foto %d sin esquema ni papel" % (i + 1))
        if o["rows"]:
            if sum(1 for r in o["rows"] if r.get("p")) != 1:
                av.append("T3 foto %d: el esquema no tiene un solo pequeño problema" % (i + 1))
            if o["dialogo"] and not o["rows"][0].get("a"):
                av.append("T3 foto %d: el saludo no tiene respuesta modelo" % (i + 1))
            pr = [r for r in o["rows"] if r.get("p")]
            if o["dialogo"] and pr and not pr[0].get("a"):
                av.append("T3 foto %d: el pequeño problema no tiene solución modelo" % (i + 1))
    return av


CSS_VIVO = r"""
.live{margin:0 0 18px}
.lv-grid{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;align-items:start}
@media (max-width:900px){.lv-grid{grid-template-columns:1fr}}
.lv-card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:0 0 12px}
.lv-lbl{font-size:.76rem;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:700;margin:0 0 8px}
.lv-pautas{margin:0;padding-left:1.4em;font-size:1.08rem;line-height:1.5}.lv-pautas li{margin:7px 0}
.lv-preg{margin:0;padding-left:1.4em;font-size:.95rem;line-height:1.45;color:var(--ink)}.lv-preg li{margin:4px 0}
.lv-help .lv-say{background:#FFF5DD;border-left:5px solid #C98A1B;border-radius:0 10px 10px 0;padding:10px 14px;margin:8px 0;font-size:1.2rem;line-height:1.4;font-weight:600}
.lv-gen{font-size:.86rem;color:var(--muted);margin-top:8px}
.lv-img{width:100%;max-height:64vh;object-fit:contain;border-radius:10px;background:#F1ECE6;display:block;cursor:zoom-in}
.lv-img.big{max-height:none;cursor:zoom-out}
.lv-desc{font-size:.95rem;line-height:1.5;margin-top:8px}
.lv-desc.nofoto{background:#F1ECE6;border-radius:10px;padding:12px 14px}
.lv-head{display:flex;flex-wrap:wrap;align-items:center;gap:12px;margin:0 0 10px}
.lv-trato{font:800 1.1rem/1 system-ui,sans-serif;letter-spacing:.08em;padding:9px 16px;border-radius:999px;color:#fff;background:#2F7D4F}
.lv-trato.u{background:#3A5BA0}
.lv-rol{font-size:1.05rem;font-weight:700}
.lv-auto{font-size:.85rem;color:var(--muted)}
.lv-thumb{height:70px;width:auto;border-radius:8px;display:block}
.lv-ctrl{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:4px 0 6px}
.lv-steps{list-style:none;margin:0;padding:0}
.lv-step{display:grid;grid-template-columns:150px 1fr 36px;gap:14px;align-items:start;background:#fff;border:1.5px solid var(--line);border-radius:12px;padding:12px 14px;margin:8px 0;cursor:pointer;transition:opacity .15s}
.lv-step:hover{border-color:#9A948C}
.lv-step.now{border-color:var(--ink);box-shadow:0 0 0 2px var(--ink)}
.lv-step.done{opacity:.45}
.lv-step.prob{background:#FDEDE7;border-color:var(--coral)}
.lv-step.prob.now{box-shadow:0 0 0 2px var(--coral)}
.lv-k{font-weight:700;font-size:.92rem;padding-top:5px;line-height:1.3}
.lv-step.prob .lv-k{color:#B23A1A;text-transform:uppercase;letter-spacing:.03em}
.lv-say{font-size:1.2rem;line-height:1.42;font-weight:600;color:var(--ink)}
.lv-say .alt{display:block;margin-top:4px}
.lv-hint{font-size:.92rem;color:#8A3B22;margin-top:6px}
.lv-ans{margin-top:8px;font-size:.95rem;line-height:1.45;color:#2E2B28;background:#F2F6F3;border-radius:8px;padding:8px 11px}
.lv-ans span{display:block;font-size:.7rem;text-transform:uppercase;letter-spacing:.06em;color:#2F7D4F;font-weight:800;margin-bottom:2px}
.lv-ans.seg{background:#FFF8EA}.lv-ans.seg span{color:#9A6512}
.lv-ck{width:32px;height:32px;border-radius:50%;border:2px solid var(--line);display:grid;place-items:center;font-weight:800;color:#2F7D4F;background:#fff}
.lv-step.done .lv-ck{border-color:#2F7D4F;background:#EAF5EE}
.lv-libre{list-style:none;margin:0;padding:0}
.lv-libre li{font-size:1.08rem;line-height:1.45;padding:8px 12px;border-bottom:1px solid var(--line)}
.lv-libre li.prob{background:#FDEDE7;border-left:5px solid var(--coral);font-weight:600}
.lv-chat{display:flex;flex-direction:column;gap:6px;margin-top:8px}
.lv-chat .b{max-width:85%;padding:8px 12px;border-radius:12px;font-size:.95rem;line-height:1.45}
.lv-chat .b.e{align-self:flex-start;background:#FCE9E1}.lv-chat .b.c{align-self:flex-end;background:#EEF2F7}
.lv-chat .b.x{border:2px solid var(--coral)}
.lv-chat .b b{display:block;font-size:.72rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.lv-done{font-size:.95rem;color:#2F7D4F;font-weight:700;margin:6px 0}
@media (max-width:700px){.lv-step{grid-template-columns:1fr 32px}.lv-k{grid-column:1/-1;padding-top:0}.lv-say{font-size:1.1rem}}
"""

JS_VIVO = r"""/* ---------- guion en vivo (A2): solo la opción elegida, grande y paso a paso ---------- */
var LV_ANS = loadJ('2st_oral_lv_respuestas', true);
function lvAlt(t){ return esc(t).split(' · ').map(function(x,i){ return i? '<span class="alt">'+x+'</span>' : x; }).join(''); }
function lvImg(src, alt, cls){ return src ? '<img class="'+cls+'" src="'+esc(src)+'" alt="'+esc(alt||'')+'" loading="lazy" data-a="lvzoom" onerror="this.style.display=\'none\';var d=this.parentNode.querySelector(\'.lv-desc\');if(d){d.hidden=false;d.className=\'lv-desc nofoto\';}">' : ''; }
function vLive(tk, n, st){
 var L=tk.live, i=st.op||0, o='<div class="live">';
 if(L.kind==='mono'){
  var x=L.ops[i]||{pautas:[],ayudas:[]};
  o+='<div class="lv-grid"><div class="lv-card"><div class="lv-lbl">La lámina del candidato · '+esc((tk.opts[i]||{}).title||'')+'</div><ol class="lv-pautas">'+x.pautas.map(function(p){ return '<li>'+p+'</li>'; }).join('')+'</ol></div>';
  o+='<div class="lv-card lv-help"><div class="lv-lbl">No interrumpa. Solo si se bloquea o termina antes de 2 min</div>'+x.ayudas.map(function(q){ return '<div class="lv-say">'+esc(q)+'</div>'; }).join('')+'<div class="lv-gen">Otras ayudas: '+tk.ayudas.join(' · ')+'</div></div></div>';
 }
 else if(L.kind==='foto'){
  var f=L.ops[i]||{ayudas:[]};
  o+='<div class="lv-grid"><div class="lv-card"><div class="lv-lbl">La foto que describe · '+esc((tk.opts[i]||{}).title||'')+'</div>'+lvImg(f.img, f.desc, 'lv-img')+'<div class="lv-desc'+(f.img?'':' nofoto')+'"'+(f.img?' hidden':'')+'>'+esc(f.desc)+'</div>'+(f.img?'<details><summary class="small">Descripción de la foto</summary><div class="small">'+esc(f.desc)+'</div></details>':'')+'</div>';
  o+='<div><div class="lv-card lv-help"><div class="lv-lbl">No interrumpa. Solo si se bloquea o termina antes de 2 min</div>'+f.ayudas.map(function(q){ return '<div class="lv-say">'+esc(q)+'</div>'; }).join('')+'<div class="lv-gen">Otras ayudas: '+tk.ayudas.join(' · ')+'</div></div>';
  if(L.preguntas&&L.preguntas.length) o+='<div class="lv-card"><div class="lv-lbl">Lo que tiene que contar (lámina)</div><ol class="lv-preg">'+L.preguntas.map(function(p){ return '<li>'+p+'</li>'; }).join('')+'</ol></div>';
  o+='</div></div>';
 }
 else if(L.kind==='dial'){
  var d=L.ops[i]||{rows:[],libre:[],dialogo:[]}, S=st.steps||{}, now=-1;
  for(var k=0;k<d.rows.length;k++){ if(!S[k]){ now=k; break; } }
  o+='<div class="lv-head">'+(d.trato?'<span class="lv-trato'+(d.trato==='usted'?' u':'')+'">'+esc(d.trato.toUpperCase())+'</span>':'')+'<span class="lv-rol">Usted es: '+esc(d.rol||'')+'</span>'+lvImg(d.img,'','lv-thumb')+'<span class="lv-auto">Va con la foto de la tarea 2 (se cambia sola).</span></div>';
  if(d.rows.length){
   o+='<div class="lv-ctrl"><button class="chip small-chip'+(LV_ANS?' on':'')+'" data-a="lvans">'+(LV_ANS?'✓ ':'')+'Respuestas modelo</button><button class="linkbtn" data-a="lvreset" data-n="'+n+'">Empezar de nuevo</button><span class="small muted">Toque cada paso cuando lo termine: el siguiente se marca solo.</span></div><ol class="lv-steps">';
   d.rows.forEach(function(r,k){
    o+='<li class="lv-step'+(r.p?' prob':'')+(S[k]?' done':'')+(k===now?' now':'')+'" data-a="lvstep" data-n="'+n+'" data-i="'+k+'"><div class="lv-k">'+(r.p?'Pequeño problema':esc(r.k))+'</div><div><div class="lv-say">'+lvAlt(r.t)+'</div>'+(r.h?'<div class="lv-hint">'+esc(r.h)+'</div>':'')+(LV_ANS&&!r.a&&k===1&&d.rows[0].a?'<div class="lv-gen">En el modelo, el candidato ya lo cuenta al saludar.</div>':'')+
     (LV_ANS&&r.a?'<div class="lv-ans"><span>'+(r.p?'Solución modelo':'Respuesta modelo')+'</span>'+esc(r.a)+'</div>':'')+(LV_ANS&&r.p&&d.segunda?'<div class="lv-ans seg"><span>Otra solución posible</span>'+esc(d.segunda)+'</div>':'')+'</div><div class="lv-ck">'+(S[k]?'✓':'')+'</div></li>';
   });
   o+='</ol>'+(now<0?'<div class="lv-done">✓ Todas las pautas hechas. Cierre la tarea y pare el cronómetro.</div>':'');
  }
  if(d.libre&&d.libre.length) o+='<div class="lv-card"><div class="lv-lbl">Su papel y sus datos</div><ul class="lv-libre">'+d.libre.map(function(x){ return '<li'+(x.p?' class="prob"':'')+'>'+esc(x.t)+'</li>'; }).join('')+'</ul></div>';
  if(d.dialogo&&d.dialogo.length) o+='<details class="lv-card"><summary>Diálogo modelo completo</summary><div class="lv-chat">'+d.dialogo.map(function(t){ return '<div class="b '+(t[0]==='E'?'e':'c')+(t[2]?' x':'')+'"><b>'+(t[0]==='E'?'Usted':'Candidato')+(t[2]?' · pequeño problema':'')+'</b>'+esc(t[1])+'</div>'; }).join('')+'</div></details>';
  o+='<details class="lv-card"'+(d.rows.length?'':' open')+'><summary>Lo que ve el estudiante</summary>'+((tk.opts[i]||{}).lamina||'')+'</details>';
  if(L.intro||L.notas) o+='<div class="lv-gen">'+esc(L.intro)+(L.notas?'<br>'+esc(L.notas):'')+'</div>';
 }
 return o+'</div>';
}
"""
