# -*- coding: utf-8 -*-
# MODULO 4 DEL CURSO DE PREPARACION DELE A2 · ORAL TAREA 1: MONOLOGO (PRESENTACION DE UN TEMA)
# Uso: python3 build_M4_T1_temas.py
#  -> DELEA2_curso_M4_T1_temas.html  (subir a biblioteca/recursos/A2/dele-curso/)
# Contenido (temas, laminas, notas y monologos modelo): banco_temas_T1.py. Para anadir temas, solo se toca ese archivo.
# Mismo estilo que el taller de la foto (build_M4_T2_foto.py): modo guiado / modo examen, preparacion con notas,
# grabacion opcional que se queda en el navegador del estudiante.
import json, re, random
from curso_comun import CSS, EMAIL, page
import banco_temas_T1 as B

TITLE = "Habla de un tema"
FILE = "DELEA2_curso_M4_T1_temas.html"
STORAGE = "dele-a2-curso-M4-T1"
WPM = 115   # palabras por minuto de un candidato A2 que habla con calma

# ------------------------------------------------------------ comprobaciones del banco
TAG = re.compile(r"\{([psaf]):(.+?)\}")
LETRA = {"p": "pres", "s": "pas", "a": "antes", "f": "fut"}
ids = [t["id"] for t in B.TEMAS]
assert len(ids) == len(set(ids)), "Hay dos temas con el mismo id"
for t in B.TEMAS:
    assert len(t["pautas"]) == 5 and len(t["notas"]) == 5 and len(t["mod"]) == 5, "Tema %d: hacen falta 5 pautas, 5 notas y 5 parrafos" % t["id"]
    assert t["fuente"] in B.FUENTES and t["area"] in B.AREAS, "Tema %d: fuente o area desconocida" % t["id"]
    for p in t["pautas"]:
        assert p["t"] and all(x in B.TIEMPOS for x in p["t"]), "Tema %d: tiempo desconocido en una pauta" % t["id"]
    for txt in [t["abre"], t["cierra"]] + t["mod"]:
        assert not re.search(r"\{(?![psaf]:)", txt), "Tema %d: marca mal escrita: %s" % (t["id"], txt[:60])
    usados = set(LETRA[m] for x in t["mod"] for m, _ in TAG.findall(x))
    for i, p in enumerate(t["pautas"]):
        hay = set(LETRA[m] for m, _ in TAG.findall(t["mod"][i]))
        falta = [x for x in p["t"] if x not in hay]
        assert not falta, "Tema %d, pauta %d: el parrafo modelo no usa %s" % (t["id"], i + 1, falta)
assert B.EJEMPLO_NOTAS in ids

def plain(s):
    return TAG.sub(r"\2", s)
def marked(s):
    return TAG.sub(lambda m: '<span class="v v-%s">%s</span>' % (LETRA[m.group(1)], m.group(2)), s)

TEMAS_JS = []
for t in B.TEMAS:
    partes = [t["abre"]] + t["mod"] + [t["cierra"]]
    ws = [len(plain(x).split()) for x in partes]
    words = sum(ws)
    TEMAS_JS.append({"id": t["id"], "t": t["titulo"], "area": B.AREAS[t["area"]], "fu": t["fuente"], "intro": t["intro"],
                     "pa": [{"x": p["txt"], "t": p["t"], "k": p["clave"]} for p in t["pautas"]],
                     "notas": t["notas"], "ab": marked(t["abre"]), "ci": marked(t["cierra"]), "mod": [marked(x) for x in t["mod"]],
                     "ws": ws[1:6], "wab": ws[0], "wci": ws[6], "w": words, "min": round(words / WPM * 2) / 2})

TI = {k: {"n": v["nombre"], "q": v["que"], "c": v["claves"], "f": v["formas"], "pu": B.PUENTES_TIEMPO[k]} for k, v in B.TIEMPOS.items()}

# ------------------------------------------------------------ CSS
CSS_T1 = CSS + r"""
:root{--blu:#2B5FA8;--blu-soft:#E4ECF8;--grn:#2F7D4F;--grn-soft:#E3F1E8}
.v{border-radius:3px;padding:0 2px;font-weight:600}
.v-pres{background:var(--blu-soft);color:#1E4A87}
.v-pas{background:#FFE2D6;color:#9C3A1E}
.v-antes{background:var(--amb-soft);color:#7A4E0E}
.v-fut{background:var(--grn-soft);color:#22603C}
.ch{display:inline-block;font-size:.76rem;font-weight:700;letter-spacing:.03em;border-radius:999px;padding:1px 9px;margin:0 3px 3px 0;vertical-align:middle;white-space:nowrap}
.ch.pres{background:var(--blu-soft);color:#1E4A87}.ch.pas{background:#FFE2D6;color:#9C3A1E}.ch.antes{background:var(--amb-soft);color:#7A4E0E}.ch.fut{background:var(--grn-soft);color:#22603C}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.88rem;margin:6px 0 10px}
/* lamina (como la hoja del examen) */
.lam{background:#fff;border:2px solid var(--ink);border-radius:6px;padding:14px 18px;margin:12px 0;font-size:.97rem}
.lam .lh{font-size:.78rem;letter-spacing:.06em;color:var(--muted);text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:6px;margin-bottom:8px;display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
.lam h3{margin:0 0 6px;font-size:1.12rem;text-transform:uppercase;letter-spacing:.02em}
.lam .ins{font-size:.78rem;font-weight:700;letter-spacing:.08em;color:var(--muted)}
.lam p{margin:4px 0 6px}
.lam ul{margin:0;padding-left:0;list-style:none}
.lam li{padding:5px 0 5px 30px;position:relative;border-bottom:1px dashed var(--line)}
.lam li:last-child{border-bottom:0}
.lam li .bn{position:absolute;left:0;top:6px;width:22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:.78rem;font-weight:700;display:grid;place-items:center}
.lam li.cur{background:var(--coral-soft);border-radius:6px;margin:0 -6px;padding-left:36px;padding-right:6px}
.lam li.cur .bn{background:var(--coral);left:6px}
.lam li.done{color:var(--muted)}
.lam li.done .bn{background:var(--ok)}
.lam .tg2{display:block;margin-top:3px}
.lam.sm{font-size:.9rem;padding:10px 14px}
/* tarea */
.tl{display:grid;grid-template-columns:.6fr repeat(5,1fr) .6fr;gap:4px;margin:14px 0 4px}
.tl div{background:var(--coral-soft);border-top:5px solid var(--coral);border-radius:4px;padding:6px 4px;text-align:center;font-size:.8rem;line-height:1.3}
.tl div.ed{background:#fff;border-top-color:var(--ink)}
.tl div b{display:block;font-size:1rem;font-family:Georgia,serif}
.tl-cap{display:flex;justify-content:space-between;font-size:.82rem;color:var(--muted)}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}
.vs div{border-radius:12px;padding:12px 16px;font-size:.95rem}
.vs .no{background:var(--bad-soft)}.vs .si{background:var(--ok-soft)}
.vs b{display:block;margin-bottom:4px}
.keys{counter-reset:k;list-style:none;padding:0}
.keys li{counter-increment:k;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 14px 10px 52px;margin:8px 0;position:relative}
.keys li:before{content:counter(k);position:absolute;left:14px;top:8px;font-family:Georgia,serif;font-size:1.5rem;font-weight:700;color:var(--coral)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px}
.box ul{margin:6px 0 0;padding-left:1.1em}
.box h4{margin:0 0 4px}
/* tiempos */
.tgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.tcard{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px;border-top:6px solid var(--line)}
.tcard.pres{border-top-color:var(--blu)}.tcard.pas{border-top-color:var(--coral)}.tcard.antes{border-top-color:var(--amb)}.tcard.fut{border-top-color:var(--grn)}
.tcard h3{margin:0 0 2px}
.tcard .q{color:var(--muted);font-size:.92rem;margin:0 0 8px}
.tcard dl{display:grid;grid-template-columns:5.4em 1fr;gap:4px 8px;margin:0;font-size:.92rem}
.tcard dt{font-size:.74rem;font-weight:700;letter-spacing:.05em;color:var(--muted);padding-top:3px;text-transform:uppercase}
.tcard dd{margin:0}
.quiz{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin:14px 0}
.quiz .qn{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.quiz .qt{font-size:1.1rem;font-family:Georgia,serif;margin:4px 0 2px}
.quiz .qs{font-size:.88rem;color:var(--muted);margin:0 0 10px}
.tsel{display:flex;flex-wrap:wrap;gap:8px}
.tsel label{border:2px solid var(--line);border-radius:999px;padding:6px 14px;cursor:pointer;background:#fff;font-weight:600;font-size:.95rem}
.tsel input{position:absolute;opacity:0}
.tsel label.pres:has(input:checked){background:var(--blu);border-color:var(--blu);color:#fff}
.tsel label.pas:has(input:checked){background:var(--coral);border-color:var(--coral);color:#fff}
.tsel label.antes:has(input:checked){background:var(--amb);border-color:var(--amb);color:#fff}
.tsel label.fut:has(input:checked){background:var(--grn);border-color:var(--grn);color:#fff}
.tsel label:has(input:focus-visible){outline:3px solid var(--cta);outline-offset:2px}
.fb{border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
.fb.ok{background:var(--ok-soft)}.fb.bad{background:var(--bad-soft)}
.score{font-family:Georgia,serif;font-size:2.2rem;font-weight:700}
/* preparacion */
.r12{display:flex;border-radius:10px;overflow:hidden;margin:14px 0 4px;border:2px solid var(--ink)}
.r12 div{padding:8px 6px;text-align:center;font-size:.82rem;line-height:1.25;border-right:2px solid var(--ink);background:#fff}
.r12 div:last-child{border-right:0}
.r12 div b{display:block;font-family:Georgia,serif;font-size:1.05rem}
.r12 div.me{background:var(--coral);color:#fff}
.r12cap{display:flex;justify-content:space-between;font-size:.8rem;color:var(--muted)}
.r12list{margin:10px 0;padding-left:1.1em;font-size:.95rem}
.steps4{list-style:none;padding:0;margin:12px 0}
.steps4 li{display:grid;grid-template-columns:4em 1fr;gap:12px;padding:10px 0;border-bottom:1px dashed var(--line)}
.steps4 .tm{font-family:Georgia,serif;font-weight:700;font-size:1.15rem;color:var(--coral)}
.esq{display:grid;grid-template-columns:1fr;gap:8px;margin:10px 0}
.eb{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:8px 12px 10px;min-height:5.2em}
.eh{display:flex;align-items:center;gap:8px;font-weight:700;font-size:.9rem;margin-bottom:4px;flex-wrap:wrap}
.en{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--coral);color:#fff;font-family:Georgia,serif;font-size:1.05rem;flex:0 0 auto}
.eh .px{font-weight:400;color:var(--muted);font-size:.86rem;flex:1 1 12em}
.enote{font-size:.95rem;line-height:1.45;white-space:pre-wrap}
.esq.blank .eb{min-height:7.5em}
.esq.blank .tslot{font-size:.8rem;color:var(--muted);border:1px dashed #CFC6BB;border-radius:999px;padding:1px 10px}
.eb textarea{width:100%;font:inherit;font-size:.95rem;line-height:1.5;border:1px dashed #CFC6BB;border-radius:8px;padding:6px 8px;min-height:4.4em;resize:vertical;background:var(--paper)}
.eb .wn{font-size:.8rem;color:#7A4E0E;background:var(--amb-soft);border-radius:6px;padding:2px 8px;margin-top:4px;display:none}
.eb.many .wn{display:block}
.eb.end{border-style:dashed;min-height:0}
.myn{white-space:pre-wrap;font-size:.95rem;background:#FFF8F2;border:1px solid var(--coral-soft);border-radius:8px;padding:8px 12px;margin:8px 0}
.myn b{display:block;font-size:.78rem;letter-spacing:.05em;color:var(--coral);white-space:normal}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.cmp h4{margin:6px 0 0}
#sheet{display:none}
/* practica */
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:12px 0}
.card{background:#fff;border:2px solid var(--line);border-radius:12px;cursor:pointer;text-align:left;font:inherit;padding:10px 14px;color:inherit;display:flex;gap:12px;align-items:flex-start}
.card:hover{border-color:var(--coral)}
.card .ci{font-family:Georgia,serif;font-size:1.5rem;font-weight:700;color:var(--coral);line-height:1;min-width:1.4em}
.card b{display:block;font-size:.98rem;line-height:1.3}
.card span.s{font-size:.82rem;color:var(--muted)}
h3.grp{margin:22px 0 2px}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.duo .lam{cursor:pointer;margin:0;position:relative}
.duo .lam:hover{border-color:var(--coral);box-shadow:0 0 0 3px var(--coral-soft)}
.duo .pick{margin-top:8px}
.modes{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}
.mode{background:#fff;border:2px solid var(--line);border-radius:12px;padding:12px 16px;cursor:pointer;display:block}
.mode:has(input:checked){border-color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
.mode input{margin-right:6px;accent-color:var(--coral)}
.mode p{margin:4px 0 0;font-size:.9rem;color:var(--muted)}
.opts{background:#fff;border:1px solid var(--line);border-radius:12px;padding:6px 16px;margin:10px 0}
.opts label{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px dashed var(--line)}
.opts label:last-child{border-bottom:0}
.opts input[type=checkbox]{width:20px;height:20px;accent-color:var(--coral);flex:0 0 auto;margin-top:3px}
.opts select{font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:4px 8px;background:#fff;max-width:100%}
.opts small{display:block;color:var(--muted);font-size:.85rem}
.run{display:grid;grid-template-columns:1fr 1.05fr;gap:16px;align-items:start;margin-top:8px}
.run .side{position:sticky;top:120px}
.pan{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px}
.pan .kk{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.pan h3{margin:2px 0 8px;font-size:1.2rem}
.clock{font-family:Georgia,serif;font-size:2.6rem;font-weight:700;font-variant-numeric:tabular-nums;line-height:1}
.clock.green{color:var(--ok)}.clock.red{color:var(--bad)}
.bar{height:12px;background:var(--line);border-radius:99px;overflow:hidden;margin:10px 0}
.bar i{display:block;height:100%;background:var(--coral);width:0}
.esc{list-style:none;padding:0;margin:10px 0}
.esc li{padding:7px 10px;border-radius:8px;margin:4px 0;color:#B5ADA4;border:1px dashed var(--line)}
.esc li.on{color:var(--ink);background:var(--coral-soft);border:1px solid transparent;font-weight:600}
.forms{font-size:.92rem;margin:8px 0;padding:8px 12px;border-left:4px solid var(--amb);background:var(--amb-soft);border-radius:0 8px 8px 0}
.dots{display:flex;gap:5px;margin:4px 0 8px}
.dots i{flex:1;height:6px;border-radius:99px;background:var(--line)}
.dots i.d{background:var(--ok)}.dots i.c{background:var(--coral)}
.recdot{display:inline-flex;align-items:center;gap:6px;font-size:.85rem;font-weight:600;color:var(--bad)}
.recdot:before{content:"";width:10px;height:10px;border-radius:50%;background:var(--bad);animation:bl 1s infinite}
@keyframes bl{50%{opacity:.25}}
.lvl{display:inline-block;width:60px;height:8px;background:var(--line);border-radius:99px;overflow:hidden;vertical-align:middle;margin-left:6px}
.lvl i{display:block;height:100%;width:0;background:var(--ok);transition:width .15s}
.chk{list-style:none;padding:0;margin:8px 0}
.chk li label{display:flex;gap:10px;align-items:flex-start;padding:6px 0;border-bottom:1px dashed var(--line);cursor:pointer}
.chk input{width:20px;height:20px;accent-color:var(--ok);flex:0 0 auto;margin-top:3px}
.chk li label:has(input:checked) > span{color:var(--muted);text-decoration:line-through}
.lq-n{display:block;white-space:pre-wrap;font-size:.85rem;color:var(--muted);margin-top:2px}
.modtxt{font-size:.98rem;margin:6px 0 0}
.res{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 20px;margin:12px 0}
.res .big{font-family:Georgia,serif;font-size:2.4rem;font-weight:700;line-height:1}
.verd{border-radius:10px;padding:10px 14px;font-weight:600;margin:10px 0}
.verd.ok{background:var(--ok-soft);color:var(--ok)}.verd.amb{background:var(--amb-soft);color:#7A4E0E}.verd.bad{background:var(--bad-soft);color:var(--bad)}
.zone{position:relative;height:16px;background:var(--line);border-radius:99px;margin:20px 0 26px}
.zone .ok{position:absolute;top:0;bottom:0;left:50%;width:25%;background:var(--ok-soft);border-left:2px solid var(--ok);border-right:2px solid var(--ok)}
.zone .me{position:absolute;top:-6px;width:4px;height:28px;background:var(--ink);border-radius:2px}
.zone span{position:absolute;top:20px;font-size:.75rem;color:var(--muted);transform:translateX(-50%)}
.hist{font-size:.92rem;margin:6px 0}
audio{width:100%;margin:8px 0}
.warnbox{background:var(--amb-soft);border-radius:10px;padding:12px 14px;margin:10px 0}
.warnbox[hidden]{display:none}
.mono-mod h4{margin:12px 0 2px;font-size:.95rem}
.mono-mod .px{font-size:.86rem;color:var(--muted);font-style:italic;margin:0}
/* opinion */
.scale{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.scale label{cursor:pointer}
.scale input{position:absolute;opacity:0}
.scale span{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;border:2px solid var(--line);background:#fff;font-weight:700}
.scale input:checked + span{background:var(--ink);border-color:var(--ink);color:#fff}
.scale input:focus-visible + span{outline:3px solid var(--cta);outline-offset:2px}
.opn label.q{display:block;font-weight:600;margin:18px 0 6px}
.opn textarea{width:100%;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;min-height:80px;background:#fff}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips label{border:2px solid var(--line);border-radius:999px;padding:5px 14px;cursor:pointer;background:#fff}
.chips label:has(input:checked){border-color:var(--ink);background:var(--ink);color:#fff}
.chips input{position:absolute;opacity:0}
.sendbox{border:2px solid var(--coral);border-radius:12px;padding:18px 22px;margin:26px 0;background:#fff}
.sendbox input[type=text]{width:100%;max-width:360px;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:8px 12px;margin-top:6px}
/* modo concentracion */
body.wide .wrap,body.wide .top-in{max-width:1180px}
body.focus header.top{display:none}
body.focus section.view{padding-top:12px}
body.focus .run .side{top:12px}
.mini{display:none}
@media (max-width:900px){.run{grid-template-columns:1fr}.run .side{position:static}
 body.focus .run .side{position:sticky;top:0;z-index:6;background:var(--paper);padding:6px 0 8px}
 body.focus .run .side .lam{max-height:34vh;overflow:auto;margin:0}
 body.focus.notas .run .side .lam{max-height:20vh}
 body.focus .pan{padding:12px 14px}body.focus .clock{font-size:2rem}
 body.focus .mini{display:flex;justify-content:space-between;gap:10px;background:var(--ink);color:#fff;border-radius:8px;padding:6px 12px;margin-top:6px;font-weight:600;font-size:.92rem}
 body.focus .mini b{font-family:Georgia,serif;font-variant-numeric:tabular-nums}}
@media (max-width:760px){.grid,.modes,.two,.vs,.cmp,.duo,.tgrid{grid-template-columns:1fr}.r12 div{font-size:.7rem;padding:6px 2px}.tl div{font-size:.66rem}.tcard dl{grid-template-columns:1fr}}
@media print{header.top,.row,.noprint,footer.legal{display:none!important}body{background:#fff}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}
 body.ps main,body.ps header{display:none!important}body.ps #sheet{display:block;padding:0 4mm}
 #sheet h2{font-size:15pt;margin:0 0 2mm}#sheet .eb{min-height:38mm;break-inside:avoid}
 .tcard,.lam,.box{break-inside:avoid}}
"""

# ------------------------------------------------------------ VISTAS
STEPS = [("tarea", "La tarea"), ("tiempos", "Los tiempos"), ("prep", "La preparación"), ("practica", "Practica"), ("opinion", "Tu opinión")]

def ch(k):
    return '<span class="ch %s">%s</span>' % (k, B.TIEMPOS[k]["nombre"])
LEG = '<div class="legend">' + "".join(ch(k) for k in B.ORDEN_TIEMPOS) + '</div>'

def lamina_html(t, tags=False, opc="1"):
    lis = "".join('<li><span class="bn">%d</span>%s%s</li>' % (i + 1, p["txt"], ('<span class="tg2">' + "".join(ch(x) for x in p["t"]) + '</span>') if tags else "")
                  for i, p in enumerate(t["pautas"]))
    return ('<div class="lam"><div class="lh"><span>Tarea 1. Presentación de un tema</span><span>Opción %s</span></div><h3>%s</h3>'
            '<div class="ins">INSTRUCCIONES</div><p>%s</p><ul>%s</ul></div>' % (opc, t["titulo"], t["intro"], lis))

EJ = [t for t in B.TEMAS if t["id"] == 1][0]
tl = ('<div class="ed"><b>0:00</b>Empiezo</div>' + "".join('<div><b>%d</b>pauta</div>' % (i + 1) for i in range(5)) +
      '<div class="ed"><b>2:30</b>Termino</div>')

V_TAREA = """
<h2>La tarea 1 de la oral: hablar de un tema</h2>
<p class="lead">En el examen te dan dos temas y eliges uno. Hablas tú solo <b>entre 2 y 3 minutos</b>: el examinador no te pregunta nada. En la lámina hay <b>cinco preguntas o pautas</b> y tienes que hablar de todas.</p>
<div class="note"><b>Así es una lámina</b> (este tema es de práctica; en el examen el formato es igual):""" + lamina_html(EJ) + """</div>

<h3>Lo que pasa a muchos candidatos</h3>
<div class="vs">
 <div class="no"><b>Un texto aprendido de memoria</b>Se nota enseguida: hablan muy rápido, sin pausas, como si leyeran. Si olvidan una frase, se quedan en blanco. Y muchas veces el texto no responde a las pautas de la lámina.</div>
 <div class="si"><b>Palabras clave y las cinco pautas en orden</b>Preparan solo ideas: nombres, lugares, fechas y un verbo. Hablan con sus palabras, de cada pauta, y si se pierden, miran la casilla siguiente.</div>
</div>
<p>La estructura es siempre la misma: <b>una frase para empezar</b>, <b>las cinco pautas en orden</b> (unas tres frases cada una, unos 25 segundos) y <b>una frase para terminar</b>.</p>
<div class="tl" aria-hidden="true">""" + tl + """</div>
<div class="tl-cap"><span>0:00</span><span>unos 25 segundos por pauta</span><span>2:30</span></div>

<h3>Cinco claves</h3>
<ol class="keys">
 <li><b>Las cinco pautas, en orden.</b> Cada pauta que olvidas es una parte de la tarea sin hacer. Marca cada una en tu hoja cuando ya has hablado de ella.</li>
 <li><b>Mira el tiempo de cada pauta.</b> Una pide presente, otra pasado, otra «antes» y otra futuro. Es un examen de tiempos verbales: lo ves en la pestaña siguiente.</li>
 <li><b>Tres frases por pauta.</b> Responde, añade un detalle (un nombre, una fecha, un número) y di por qué o cómo te sientes.</li>
 <li><b>Empieza y termina con una frase.</b> <i>«Voy a hablar de...»</i> al principio y <i>«Por eso, para mí... es muy importante»</i> al final. Así el examinador sabe que has terminado.</li>
 <li><b>Puedes inventar.</b> """ + B.INVENTAR + """</li>
</ol>
<div class="tip"><b>Cómo practicar aquí:</b> aprende los cuatro tiempos y prueba el ejercicio «¿Qué tiempo pide?». Después mira cómo preparar el tema en 4 minutos con el esquema de cinco casillas. Para practicar, empieza con el <b>modo guiado</b> (cada pauta en pantalla con su tiempo) y, cuando llegues a 2 minutos sin ayuda, pasa al <b>modo examen</b>.</div>
<div class="row"><button class="btn cta" data-go="tiempos">Siguiente: los tiempos</button></div>
"""

def tcard(k):
    v = B.TIEMPOS[k]
    return ('<div class="tcard %s"><h3>%s</h3><p class="q">%s</p><dl><dt>En la lámina</dt><dd>%s</dd><dt>Verbos</dt><dd><i>%s</i></dd><dt>Para empezar</dt><dd><i>%s</i></dd></dl></div>'
            % (k, v["nombre"], v["que"], " · ".join("«%s»" % c for c in v["claves"]), ", ".join(v["formas"]), " · ".join(B.PUENTES_TIEMPO[k])))
EJ_T = [t for t in B.TEMAS if t["id"] == 5][0]
V_TIEMPOS = ("""
<h2>Los tiempos: el secreto de la tarea 1</h2>
<p class="lead">Las cinco pautas de la lámina mezclan casi siempre <b>presente</b>, <b>pasado</b>, <b>cómo era antes</b> y <b>futuro</b>. Parece un tema personal, pero en realidad el examinador escucha si usas bien los tiempos.</p>
<div class="tgrid">""" + "".join(tcard(k) for k in B.ORDEN_TIEMPOS) + """</div>
<h3>Mira una lámina con sus tiempos</h3>
<p>Lee cada pauta y busca las palabras que te dicen el tiempo: <i>¿quién te lo regaló?</i> (pasado), <i>cuando era pequeño</i> (antes), <i>próximamente</i> (futuro).</p>""" +
 lamina_html(EJ_T, tags=True) + """
<div class="tip"><b>Pasado o «antes»:</b> si es una vez, un día, una historia (<i>fui, me regaló, me pasó</i>) es pasado. Si es cómo era algo o lo que hacías normalmente hace años (<i>era, tenía, iba</i>) es «antes». Muchas veces van juntos: <i>«Cuando <b>era</b> pequeña, un día mi abuelo me <b>regaló</b>...»</i>.</div>

<h3>Practica: ¿qué tiempo pide?</h3>
<p>Diez pautas de temas distintos. Marca el tiempo o los tiempos que pide cada una (a veces son dos).</p>
<div id="quiz"></div>

<h3>Frases para todo el monólogo</h3>
<div class="two">
 <div class="box"><h4>Para empezar</h4><ul>""" + "".join("<li><i>%s</i></li>" % x for x in B.ABRIR) + """</ul></div>
 <div class="box"><h4>Para terminar</h4><ul>""" + "".join("<li><i>%s</i></li>" % x for x in B.CERRAR) + """</ul></div>
 <div class="box"><h4>Para pasar de una pauta a otra</h4><ul>""" + "".join("<li><i>%s</i></li>" % x for x in B.PASAR) + """</ul></div>
 <div class="box"><h4>Para unir las frases</h4><p><i>""" + " · ".join(B.UNIR) + """</i></p><p class="small muted">No solo «y» y «porque»: con «por eso», «además» y «cuando» el monólogo suena mucho mejor.</p></div>
</div>
<div class="row"><button class="btn" data-act="print" data-p="tiempos">Imprimir esta página</button><button class="btn cta" data-go="prep">Siguiente: la preparación</button></div>
""")

REPARTO = [(1, "Elegir", "Lee los dos temas de la tarea 1 y mira las dos fotos de la tarea 2."),
           (4, "Tarea 1", "El monólogo: el esquema de cinco casillas con palabras clave."),
           (4, "Tarea 2", "La foto: el esquema de las seis casillas."),
           (2, "Tarea 3", "La situación del diálogo: ideas y dos o tres preguntas."),
           (1, "Repasar", "Mira tus notas de las tres tareas y respira.")]
assert sum(m for m, _, _ in REPARTO) == 12
r12 = "".join('<div class="%s" style="flex:%d"><b>%d min</b>%s</div>' % ("me" if t == "Tarea 1" else "", m, m, t) for m, t, _ in REPARTO)
r12l = "".join("<li><b>%s (%d min):</b> %s</li>" % (t, m, d) for m, t, d in REPARTO)
p4 = "".join('<li><span class="tm">%s</span><span><b>%s.</b> %s</span></li>' % x for x in B.PASOS_T1)
reg = "".join("<li>%s</li>" % x for x in B.REGLAS_NOTAS_T1)
EJN = [t for t in B.TEMAS if t["id"] == B.EJEMPLO_NOTAS][0]
V_PREP = """
<h2>La preparación: 4 minutos para el tema</h2>
<p class="lead">Antes de entrar tienes <b>12 minutos para preparar las tres tareas</b> de la oral. Puedes escribir notas y llevarlas a la sala: puedes <b>mirarlas</b>, pero no leerlas en voz alta.</p>
<h3>Cómo repartir los 12 minutos</h3>
<div class="r12" aria-hidden="true">""" + r12 + """</div>
<div class="r12cap"><span>0:00</span><span>12:00</span></div>
<ul class="r12list">""" + r12l + """</ul>
<div class="tip">Es una recomendación, no una regla del examen. Lo importante: no escribas un texto completo para la tarea 1. No hay tiempo, y si lo escribes, lo vas a leer.</div>

<h3>Tus 4 minutos con el tema, paso a paso</h3>
<ol class="steps4">""" + p4 + """</ol>

<h3>El esquema de cinco casillas</h3>
<p>Una casilla para cada pauta, en el mismo orden que la lámina. Al lado del número, el tiempo que pide. Dentro, solo palabras clave y un verbo ya conjugado. Antes y después, una línea para empezar y otra para terminar.</p>
<div id="esq-blank"></div>
<div class="row"><button class="btn" data-act="print" data-p="sheet">Imprimir el esquema en blanco</button></div>

<h3>Un ejemplo: así quedan las notas</h3>
<p>Estas son las notas del tema <i>«""" + EJN["titulo"] + """»</i>. Fíjate: palabras sueltas, números, flechas y un verbo en cada casilla (<i>repetí, comía, voy a hacer</i>). Con estas notas se habla dos minutos y medio sin leer.</p>
<div class="two"><div>""" + lamina_html(EJN, tags=True) + """</div><div id="esq-ej"></div></div>

<h3>Reglas para tus notas</h3>
<ul class="keys">""" + reg + """</ul>
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACTICA = '<div id="pr"></div>'

V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿El modo guiado te ha ayudado a hablar de las cinco pautas sin correr?</label>
 <div class="chips" role="group" aria-labelledby="o1l">
  <label><input type="radio" name="o1" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o1" value="Un poco">Un poco</label>
  <label><input type="radio" name="o1" value="No">No</label>
  <label><input type="radio" name="o1" value="No lo he probado">No lo he probado</label>
 </div>
 <label class="q" id="o5l">2. ¿Te ha servido el esquema de cinco casillas para preparar el tema?</label>
 <div class="chips" role="group" aria-labelledby="o5l">
  <label><input type="radio" name="o5" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o5" value="Un poco">Un poco</label>
  <label><input type="radio" name="o5" value="No">No</label>
  <label><input type="radio" name="o5" value="No lo he probado">No lo he probado</label>
 </div>
 <label class="q" id="o3l">3. ¿Qué tiempo te cuesta más usar cuando hablas?</label>
 <div class="chips" role="group" aria-labelledby="o3l">__CHIPS__</div>
 <label class="q" for="o2">4. ¿Te has grabado? ¿Qué has notado al escucharte? (O, si no, ¿qué falta o no has entendido?)</label>
 <textarea id="o2"></textarea>
 <label class="q" id="o4l">5. Ahora, ¿cuánto control sientes cuando hablas de un tema? (1 = nada, 10 = total)</label>
 <div class="scale" role="group" aria-labelledby="o4l" id="o4"></div>
</div>
<div class="sendbox">
 <h3>Envía tu opinión y tus tiempos a tu profesora</h3>
 <label><b>Tu nombre</b><br><input type="text" id="sname" autocomplete="name"></label>
 <div class="row"><button class="btn cta" data-act="copy">Copiar</button></div>
 <div class="copied-box" id="cbox" role="status" hidden></div>
 <p class="muted small">Pégalo en un correo para tu profesora: __EMAIL__. Tus grabaciones no se copian: si quieres que tu profesora te escuche, guarda el audio y envíalo tú.</p>
</div>
""".replace("__CHIPS__", "".join('<label><input type="radio" name="o3" value="%s">%s</label>' % (B.TIEMPOS[k]["nombre"], B.TIEMPOS[k]["nombre"]) for k in B.ORDEN_TIEMPOS) +
            '<label><input type="radio" name="o3" value="Ninguno">Ninguno</label>').replace("__EMAIL__", EMAIL)

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Oral · Tarea 1</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
<div id="sheet"><h2>El tema · mis notas</h2><p style="margin:0 0 3mm">Tema: ______________________________________</p><div id="esq-sheet"></div></div>
"""

views = {"tarea": V_TAREA, "tiempos": V_TIEMPOS, "prep": V_PREP, "practica": V_PRACTICA, "opinion": V_OPINION}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
body = BODY.replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

ESC = ["Responde a la pauta.", "Añade un detalle: un nombre, una fecha, un número.", "Di por qué o cómo te sientes."]
DATA = {"key": STORAGE, "steps": [{"id": k, "label": l} for k, l in STEPS], "temas": TEMAS_JS, "ti": TI, "ord": B.ORDEN_TIEMPOS,
        "ej": B.EJEMPLO_NOTAS, "esc": ESC, "abrir": B.ABRIR[0], "cerrar": B.CERRAR[0]}

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function blank(){ return {cur:'tarea', seen:{}, tema:null, duo:null, o:{mode:'guiado', ritmo:30, prep:'notas', modelo:false, rec:false, beep:true}, h:{}, n:{}, qz:{best:null, last:null}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } for(var j in b.o){ if(!(j in o.o)) o.o[j]=b.o[j]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function T(id){ for(var i=0;i<D.temas.length;i++) if(D.temas[i].id===id) return D.temas[i]; return null; }
function mmss(s){ s=Math.max(0,Math.round(s)); return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2); }
function chip(k){ return '<span class="ch '+k+'">'+esc(D.ti[k].n)+'</span>'; }
function chips(ts){ return ts.map(chip).join(''); }

/* ---------------- navegacion ---------------- */
function practiced(){ return Object.keys(S.h).length>0; }
function nav(){
 var o='';
 D.steps.forEach(function(st,i){
  var done = st.id==='practica' ? practiced() : (st.id==='opinion' ? !!(S.o1||S.o2||S.o3||S.o4||S.o5) : (st.id==='tiempos' ? S.qz.best!==null : !!S.seen[st.id]));
  var on = S.cur===st.id;
  o += '<button type="button" class="'+(on?'on ':'')+(done&&!on?'done':'')+'" data-go="'+st.id+'"'+(on?' aria-current="step"':'')+'><span class="n">'+(done&&!on?'✓':(i+1))+'</span>'+st.label+'</button>';
 });
 $('steps').innerHTML = o;
}
function go(id){
 if(R.active && id!=='practica'){ stopRun(true); }
 S.seen[S.cur]=true; S.cur=id; save();
 var vs=document.querySelectorAll('section.view');
 for(var i=0;i<vs.length;i++) vs[i].classList.toggle('on', vs[i].id==='v-'+id);
 document.body.classList.toggle('wide', id==='practica');
 if(id==='practica' && !R.active) showPick();
 nav(); window.scrollTo(0,0);
}

/* ---------------- lamina ---------------- */
function lamina(t, o){
 o=o||{};
 var lis=t.pa.map(function(p,i){
  var cls = o.cur===i ? 'cur' : (o.cur!==undefined && o.cur!==null && i<o.cur ? 'done' : '');
  return '<li class="'+cls+'"><span class="bn">'+(i+1)+'</span>'+esc(p.x)+(o.tags?'<span class="tg2">'+chips(p.t)+'</span>':'')+'</li>';
 }).join('');
 return '<div class="lam'+(o.sm?' sm':'')+'"'+(o.attr||'')+'><div class="lh"><span>Tarea 1. Presentación de un tema</span><span>'+(o.opc?'Opción '+o.opc:esc(t.area))+'</span></div><h3>'+esc(t.t)+'</h3><div class="ins">INSTRUCCIONES</div><p>'+esc(t.intro)+'</p><ul>'+lis+'</ul></div>';
}

/* ---------------- ejercicio: que tiempo pide ---------------- */
var QZ=null;
function allPautas(){ var a=[]; D.temas.forEach(function(t){ t.pa.forEach(function(p,i){ a.push({tema:t.t, p:p, i:i}); }); }); return a; }
function newQuiz(){
 var a=allPautas(), used={}, items=[];
 /* diez pautas de temas distintos, con todos los tiempos representados */
 a.sort(function(){ return Math.random()-.5; });
 for(var i=0;i<a.length && items.length<10;i++){ if(used[a[i].tema]) continue; used[a[i].tema]=1; items.push(a[i]); }
 QZ={items:items, k:0, ok:0, answered:false};
 renderQuiz();
}
function renderQuiz(){
 var q=QZ, box=$('quiz');
 if(q.k>=q.items.length){
  var n=q.items.length, ok=q.ok;
  if(S.qz.best===null || ok>S.qz.best) S.qz.best=ok; S.qz.last=ok; save(); nav();
  box.innerHTML='<div class="quiz"><div class="qn">RESULTADO</div><div class="score">'+ok+' / '+n+'</div><p>'+(ok>=9?'¡Muy bien! Reconoces los tiempos de las pautas.':(ok>=6?'Bien. Repasa las palabras que dicen el tiempo: «la última vez», «cuando era pequeño», «próximamente»...':'Vuelve a mirar las cuatro tarjetas de arriba y prueba otra vez.'))+'</p>'+
   (S.qz.best!==null?'<p class="small muted">Tu mejor resultado: '+S.qz.best+' / '+n+'</p>':'')+'<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="qnew">Otras diez pautas</button></div></div>';
  return;
 }
 var it=q.items[q.k];
 var o='<div class="quiz"><div class="qn">PAUTA '+(q.k+1)+' DE '+q.items.length+'</div><p class="qs">Tema: '+esc(it.tema)+'</p><div class="qt">… '+esc(it.p.x)+'</div><p class="qs">¿Qué tiempo pide? Puedes marcar dos.</p><div class="tsel" role="group" aria-label="Tiempos">';
 D.ord.forEach(function(k){ o+='<label class="'+k+'"><input type="checkbox" value="'+k+'"'+(q.answered?' disabled':'')+'>'+esc(D.ti[k].n)+'</label>'; });
 o+='</div><div id="qfb"></div><div class="row" style="margin-bottom:0"><button class="btn cta" data-act="qcheck" id="qbtn">Comprobar</button></div></div>';
 box.innerHTML=o;
}
function checkQuiz(){
 var q=QZ, it=q.items[q.k];
 if(q.answered){ q.k++; q.answered=false; renderQuiz(); return; }
 var sel=[].slice.call(document.querySelectorAll('#quiz .tsel input:checked')).map(function(x){ return x.value; });
 if(!sel.length){ $('qfb').innerHTML='<div class="fb bad">Marca al menos un tiempo.</div>'; return; }
 var want=it.p.t.slice().sort().join(','), got=sel.slice().sort().join(',');
 var ok = want===got;
 /* si pide dos y marca uno de ellos, es medio acierto: cuenta como fallo, pero se explica */
 if(ok) q.ok++;
 q.answered=true;
 [].forEach.call(document.querySelectorAll('#quiz .tsel input'), function(x){ x.disabled=true; });
 $('qfb').innerHTML='<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Correcto!':'No exactamente.')+'</b> Pide: '+chips(it.p.t)+'<br>Las palabras que lo dicen: <i>'+esc(it.p.k)+'</i>. Por ejemplo: <i>'+esc(it.p.t.map(function(k){ return D.ti[k].f.slice(0,3).join(', '); }).join(' / '))+'</i>.</div>';
 $('qbtn').textContent = q.k===q.items.length-1 ? 'Ver el resultado' : 'Siguiente pauta';
}

/* ---------------- esquema de cinco casillas ---------------- */
var FW={'el':1,'la':1,'los':1,'las':1,'un':1,'una':1,'unos':1,'unas':1,'que':1,'es':1,'son':1,'muy':1,'porque':1,'y':1,'de':1,'en':1,'con':1,'me':1,'mi':1};
function wordsOf(t){ return String(t||'').toLowerCase().match(/[a-záéíóúüñ0-9]+/g)||[]; }
function tooLong(t){ var w=wordsOf(t), n=0; w.forEach(function(x){ if(FW[x]) n++; }); return n>=6 || w.length>26; }
function hasNote(i){ return !!(R.notes && R.useNotes && wordsOf(R.notes[i]).length); }
function ehead(t,i){ return '<div class="eh"><span class="en">'+(i+1)+'</span>'+chips(t.pa[i].t)+'<span class="px">'+esc(t.pa[i].x)+'</span></div>'; }
function esqBlank(){
 var o='<div class="esq blank"><div class="eb end"><b>Empiezo:</b> <span class="muted">Voy a hablar de...</span></div>';
 for(var i=0;i<5;i++) o+='<div class="eb"><div class="eh"><span class="en">'+(i+1)+'</span><span class="tslot">tiempo: ________</span></div></div>';
 return o+'<div class="eb end"><b>Termino:</b> <span class="muted">Para mí...</span></div></div>';
}
function esqStatic(t, notes){
 var o='<div class="esq">';
 for(var i=0;i<5;i++){ var x=String(notes[i]||'').trim(); o+='<div class="eb">'+ehead(t,i)+'<div class="enote">'+(wordsOf(x).length?esc(x):'<span class="muted">(vacía)</span>')+'</div></div>'; }
 return o+'</div>';
}
function esqEdit(t, notes){
 var o='<div class="esq">';
 for(var i=0;i<5;i++){
  var ph=t.pa[i].t.map(function(k){ return D.ti[k].n.toLowerCase()+': '+D.ti[k].f[0]; }).join(' / ');
  o+='<div class="eb'+(tooLong(notes[i])?' many':'')+'">'+ehead(t,i)+'<textarea data-ni="'+i+'" rows="2" placeholder="Palabras clave + un verbo ('+esc(ph)+'...)" aria-label="Notas de la pauta '+(i+1)+'">'+esc(notes[i])+'</textarea><div class="wn">¿Estás escribiendo frases? Mejor solo palabras clave.</div></div>';
 }
 return o+'</div>';
}
function renderPrep(){
 $('esq-blank').innerHTML=esqBlank(); $('esq-sheet').innerHTML=esqBlank();
 var t=T(D.ej); if(t) $('esq-ej').innerHTML=esqStatic(t, t.notas);
}

/* ---------------- monologo modelo ---------------- */
function legend(){ return '<div class="legend">'+D.ord.map(chip).join('')+'</div>'; }
function modelHTML(t){
 var o='<div class="mono-mod"><p class="small muted">Unas '+t.w+' palabras: unos '+String(t.min).replace('.',',')+' minutos hablando con calma. En color, los verbos de cada tiempo:</p>'+legend();
 o+='<h4>Empiezo</h4><p class="modtxt">'+t.ab+'</p>';
 t.mod.forEach(function(p,i){ o+='<h4>'+(i+1)+'. '+chips(t.pa[i].t)+'</h4><p class="px">'+esc(t.pa[i].x)+'</p><p class="modtxt">'+p+'</p>'; });
 o+='<h4>Termino</h4><p class="modtxt">'+t.ci+'</p></div>';
 return o;
}

/* ---------------- practica: elegir ---------------- */
function lastTime(id){ var h=S.h[id]; return h&&h.length ? h[h.length-1] : null; }
function card(t){
 var l=lastTime(t.id);
 return '<button type="button" class="card" data-act="pick" data-id="'+t.id+'"><span class="ci">'+t.id+'</span><span><b>'+esc(t.t)+'</b><span class="s">'+esc(t.area)+' · '+(l?'Última vez: '+mmss(l.s)+(l.m==='guiado'?' (guiado)':' (examen)'):'Sin practicar')+'</span></span></button>';
}
function showPick(){
 var o='<h2>Practica con un tema</h2><p class="lead">En el examen te dan dos temas y eliges uno. Puedes practicar así o elegir directamente un tema de la lista.</p>';
 o+='<div class="row"><button class="btn cta" data-act="duo">Como en el examen: dos temas al azar</button></div>';
 [['of','Temas de las láminas oficiales','Los temas que han salido en el examen (con pautas nuevas, escritas para este curso).', function(t){ return t.fu!=='frecuente'; }],
  ['fr','Otros temas frecuentes','Temas que salen mucho en el nivel A2: también pueden caer.', function(t){ return t.fu==='frecuente'; }]].forEach(function(g){
  var ts=D.temas.filter(g[3]); if(!ts.length) return;
  o+='<h3 class="grp">'+g[1]+'</h3><p class="small muted" style="margin:0">'+g[2]+'</p><div class="grid">'+ts.map(card).join('')+'</div>';
 });
 $('pr').innerHTML=o;
}
function showDuo(){
 var ids=D.temas.map(function(t){ return t.id; }).sort(function(){ return Math.random()-.5; });
 S.duo=ids.slice(0,2); save();
 var o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="back">← Todos los temas</button><button class="btn sm" data-act="duo">Otros dos</button></div>';
 o+='<h2>Elige uno de los dos temas</h2><p class="lead">Léelos rápido: elige el que te da más ideas, no el más fácil. En el examen tienes unos 20 segundos para decidir.</p><div class="duo">';
 S.duo.forEach(function(id,k){ var t=T(id); o+='<div>'+lamina(t,{opc:k+1, attr:' data-act="pick" data-id="'+id+'" role="button" tabindex="0"'})+'<div class="pick"><button class="btn sm cta" data-act="pick" data-id="'+id+'">Elijo este</button></div></div>'; });
 $('pr').innerHTML=o+'</div>';
}
function showSetup(){
 var t=T(S.tema); if(!t){ showPick(); return; }
 var O=S.o, o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="back">← Otros temas</button></div>';
 o+='<div class="run"><div>'+lamina(t,{tags:true})+'</div><div>';
 o+='<h3>¿Cómo quieres practicar?</h3><div class="modes">'+
  '<label class="mode"><input type="radio" name="md" value="guiado"'+(O.mode==='guiado'?' checked':'')+'><b>Modo guiado</b><p>Cada pauta en la pantalla, con su tiempo y su reloj. Para aprender el ritmo.</p></label>'+
  '<label class="mode"><input type="radio" name="md" value="libre"'+(O.mode==='libre'?' checked':'')+'><b>Modo examen</b><p>La lámina y el reloj. Como el día del examen.</p></label></div>';
 o+='<div class="opts">';
 o+='<label><span style="flex:1">Preparación <select id="prepsel">'+[['notas','4 minutos con notas (como en el examen)'],['leer','1 minuto leyendo la lámina'],['no','Sin preparación']].map(function(r){ return '<option value="'+r[0]+'"'+(O.prep===r[0]?' selected':'')+'>'+r[1]+'</option>'; }).join('')+'</select><small>Con notas rellenas el esquema de cinco casillas y después lo tienes a la vista mientras hablas, como tu hoja en el examen.</small></span></label>';
 if(O.mode==='guiado'){
  o+='<label><span style="flex:1">Ritmo <select id="ritmo">'+[[24,'2 minutos (24 segundos por pauta)'],[30,'2 minutos y medio (30 segundos)'],[36,'3 minutos (36 segundos)']].map(function(r){ return '<option value="'+r[0]+'"'+(O.ritmo===r[0]?' selected':'')+'>'+r[1]+'</option>'; }).join('')+'</select><small>Empieza con 2 minutos y medio. El primer tiempo incluye tu frase para empezar y el último, tu frase para terminar.</small></span></label>';
  o+='<label><input type="checkbox" data-o="modelo"'+(O.modelo?' checked':'')+'><span>Con el monólogo modelo en la pantalla<small>Léelo en voz alta, despacio, para sentir cuánto dura cada pauta. Después, inténtalo con tus palabras.</small></span></label>';
  o+='<label><input type="checkbox" data-o="beep"'+(O.beep?' checked':'')+'><span>Sonido al cambiar de pauta</span></label>';
 }
 o+='<label><input type="checkbox" data-o="rec"'+(O.rec?' checked':'')+'><span>Grabarme (opcional)<small>La grabación se queda en tu ordenador o tu móvil: no se envía a ningún sitio y se borra al cerrar la página (al final puedes guardarla en Descargas). El navegador te pedirá permiso para usar el micrófono; mientras grabas, la barrita verde se mueve cuando hablas.</small></span></label>';
 o+='</div><div class="row"><button class="btn cta" data-act="start">Empezar</button></div>';
 o+='<details><summary>Ver las notas modelo</summary><p class="small muted">Mejor después de preparar tus notas.</p>'+esqStatic(t,t.notas)+'</details>';
 o+='<details><summary>Ver el monólogo modelo</summary><p class="small muted">Mejor después de practicar: primero inténtalo tú.</p>'+modelHTML(t)+'</details>';
 o+='</div></div>';
 $('pr').innerHTML=o;
}

/* ---------------- sonido, pantalla, grabacion ---------------- */
var AC=null, WL=null;
function beep(){
 if(!S.o.beep || S.o.mode!=='guiado' || !AC) return;
 try{ var t=AC.currentTime, os=AC.createOscillator(), g=AC.createGain(); os.type='sine'; os.frequency.value=660;
  g.gain.setValueAtTime(0.0001,t); g.gain.exponentialRampToValueAtTime(0.25,t+0.02); g.gain.exponentialRampToValueAtTime(0.0001,t+0.35);
  os.connect(g); g.connect(AC.destination); os.start(t); os.stop(t+0.4); }catch(e){}
}
function wake(on){
 try{ if(on && navigator.wakeLock){ navigator.wakeLock.request('screen').then(function(w){ WL=w; }, function(){}); } else if(!on && WL){ WL.release(); WL=null; } }catch(e){}
}
var REC={stream:null, mr:null, url:null, ext:'webm', err:'', used:false};
function recType(){
 if(!window.MediaRecorder || !MediaRecorder.isTypeSupported) return '';
 var ts=['audio/mp4','audio/webm;codecs=opus','audio/webm','audio/ogg'];
 for(var i=0;i<ts.length;i++) if(MediaRecorder.isTypeSupported(ts[i])) return ts[i];
 return '';
}
function recClear(){ if(REC.url){ try{ URL.revokeObjectURL(REC.url); }catch(e){} } REC.url=null; }
function recPrepare(done){
 REC.err=''; REC.used=false; recClear();
 if(REC.mr){ var old=REC.mr; REC.mr=null; try{ if(old.state!=='inactive') old.stop(); }catch(e){} }
 if(REC.stream){ try{ REC.stream.getTracks().forEach(function(k){ k.stop(); }); }catch(e){} REC.stream=null; }
 if(!S.o.rec){ done(); return; }
 REC.used=true;
 if(!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia || !window.MediaRecorder){ REC.err='Este navegador no puede grabar. Practica sin grabación o prueba con otro navegador.'; done(); return; }
 navigator.mediaDevices.getUserMedia({audio:true}).then(function(st){ REC.stream=st; done(); }, function(){ REC.err='No hay permiso para usar el micrófono: practicas sin grabación.'; done(); });
}
function recStart(){
 if(!REC.stream || REC.mr) return;
 var st=REC.stream, t=recType(), mr, chunks=[];
 REC.ext = t.indexOf('mp4')>=0 ? 'm4a' : (t.indexOf('ogg')>=0 ? 'ogg' : 'webm');
 try{ mr = t ? new MediaRecorder(st,{mimeType:t}) : new MediaRecorder(st); }catch(e){ REC.err='No se ha podido empezar a grabar.'; return; }
 REC.mr=mr;
 mr.ondataavailable=function(e){ if(e.data && e.data.size) chunks.push(e.data); };
 mr.onstop=function(){
  try{ st.getTracks().forEach(function(k){ k.stop(); }); }catch(e){}
  if(REC.stream===st) REC.stream=null;
  if(REC.mr!==mr) return;
  REC.mr=null;
  if(chunks.length){ var b=new Blob(chunks,{type:mr.mimeType||t||'audio/webm'}); REC.url=URL.createObjectURL(b); }
  else REC.err='No se ha grabado nada esta vez. Vuelve a cargar la página y prueba otra vez; si sigue igual, prueba con otro navegador (Chrome o Safari).';
  var a=$('recout'); if(a) a.innerHTML=recBlock();
 };
 try{ mr.start(); }catch(e){ REC.mr=null; REC.err='No se ha podido empezar a grabar.'; return; }
 lvStart(); R.recSince=now(); R.micWarned=false;
}
var LV={an:null, buf:null, max:0, src:null, g:null};
function lvStart(){ try{ if(!AC||!REC.stream) return; LV.src=AC.createMediaStreamSource(REC.stream); LV.an=AC.createAnalyser(); LV.an.fftSize=512; LV.buf=new Uint8Array(LV.an.fftSize);
 LV.g=AC.createGain(); LV.g.gain.value=0; LV.src.connect(LV.an); LV.an.connect(LV.g); LV.g.connect(AC.destination); LV.max=0; }catch(e){ LV.an=null; } }
function lvRead(){ if(!LV.an) return -1; try{ LV.an.getByteTimeDomainData(LV.buf); }catch(e){ return -1; } var m=0; for(var i=0;i<LV.buf.length;i++){ var v=Math.abs(LV.buf[i]-128); if(v>m) m=v; } if(m>LV.max) LV.max=m; return m/128; }
function lvStop(){ try{ if(LV.src) LV.src.disconnect(); if(LV.g) LV.g.disconnect(); }catch(e){} LV.an=null; LV.src=null; LV.g=null; }
function recStop(){
 lvStop();
 if(REC.mr && REC.mr.state!=='inactive'){ try{ REC.mr.stop(); }catch(e){ REC.mr=null; } }
 else { REC.mr=null; if(REC.stream){ try{ REC.stream.getTracks().forEach(function(k){ k.stop(); }); }catch(e){} REC.stream=null; } }
 setTimeout(function(){ if(REC.mr && REC.mr.state==='inactive'){ REC.mr=null; if(!REC.url) REC.err='No se ha grabado nada esta vez. Vuelve a cargar la página y prueba otra vez.'; var a=$('recout'); if(a) a.innerHTML=recBlock(); } }, 4000);
}
function recBlock(){
 if(REC.url) return '<h4>Escúchate</h4><audio controls src="'+REC.url+'"></audio><div class="row" style="margin:6px 0"><a class="btn sm" href="'+REC.url+'" download="mi_monologo_tema'+S.tema+'.'+REC.ext+'">Guardar el audio en mi dispositivo</a><button class="btn sm" data-act="delrec">Borrar la grabación</button></div>'+
  '<p class="small muted">La grabación no se guarda sola: está en esta página hasta que la cierras o haces otra. Si quieres conservarla, pulsa «Guardar el audio en mi dispositivo» y la tendrás en tu carpeta de Descargas.</p><p class="small muted">Al escucharte, fíjate: ¿hablas de las cinco pautas? ¿Usas el pasado cuando la pauta pide pasado? ¿Suenas natural o parece que lees?</p>';
 if(REC.mr) return '<p class="small muted">Preparando la grabación...</p>';
 if(REC.err) return '<div class="warnbox">'+REC.err+'</div>';
 if(REC.used) return '<p class="small muted">No hay grabación.</p>';
 return '';
}

/* ---------------- practica: estado ---------------- */
var R={active:false, mode:'', phase:0, phases:[], t0:0, acc:0, paused:false, timer:null, spoken:0, warned:false};
function now(){ return (window.performance&&performance.now)?performance.now():Date.now(); }
function elapsed(){ return R.acc + (R.paused?0:(now()-R.t0)/1000); }
function curT(){ return T(S.tema); }
function startRun(){
 var t=curT(); if(!t) return;
 try{ if(!AC){ var C=window.AudioContext||window.webkitAudioContext; if(C) AC=new C(); } if(AC && AC.resume) AC.resume(); }catch(e){}
 $('pr').innerHTML='<p class="muted">Un momento...</p>';
 recPrepare(function(){
  R.active=true; R.mode=S.o.mode; R.paused=false; R.warned=false; R.spoken=0;
  R.phases=[]; R.useNotes = S.o.prep==='notas'; R.notes=['','','','',''];
  if(S.o.prep==='leer') R.phases.push({k:'leer', d:60});
  if(S.o.prep==='notas') R.phases.push({k:'notas', d:240});
  if(R.mode==='guiado'){
   for(var i=0;i<5;i++){
    var d=S.o.ritmo;
    if(S.o.modelo){ var w=t.ws[i]+(i===0?t.wab:0)+(i===4?t.wci:0); d=Math.max(d, Math.round(w/2)+3); }
    R.phases.push({k:'q', i:i, d:d});
   }
  } else R.phases.push({k:'libre'});
  R.phase=0; wake(true); renderRun(); enterPhase(0);
  R.timer=setInterval(tick, 200);
 });
}
function enterPhase(n){
 R.phase=n; R.acc=0; R.t0=now(); R.paused=false;
 var ph=R.phases[n];
 document.body.classList.toggle('notas', ph.k==='notas');
 if(ph.k==='q' || ph.k==='libre') recStart();
 if(ph.k==='q' && n>0 && R.phases[n-1].k==='q') beep();
 renderSide(); renderPhase(); tick();
}
function renderRun(){
 document.body.classList.add('focus');
 $('pr').innerHTML='<div class="run"><div class="side"><div id="side"></div><div class="mini" aria-hidden="true"><span id="minil"></span><b id="minic"></b></div></div><div><div class="pan" id="pan" aria-live="polite"></div>'+
  '<div class="warnbox" id="micw" hidden><b>No llega sonido del micrófono.</b> Revisa que el navegador tiene permiso para usarlo (en el Mac: Ajustes del Sistema &gt; Privacidad y seguridad &gt; Micrófono) y que no está silenciado. Puedes seguir practicando sin grabación.</div>'+
  '<div class="row"><button class="btn" data-act="pause" id="bpause">Pausa</button><button class="btn" data-act="stop">Parar</button></div></div></div>';
}
function renderSide(){
 var ph=R.phases[R.phase], t=curT();
 $('side').innerHTML=lamina(t,{tags:true, sm:true, cur: ph.k==='q' ? ph.i : null});
}
function renderPhase(){
 var t=curT(), ph=R.phases[R.phase], o='';
 var recd = (REC.stream && (ph.k==='q'||ph.k==='libre')) ? ' <span class="recdot">Grabando</span><span class="lvl" title="Nivel del micrófono"><i id="lvl"></i></span>' : '';
 if(ph.k==='leer'){
  o='<div class="kk">PREPARACIÓN</div><h3>Lee la lámina en silencio</h3><div class="clock" id="clk">1:00</div><div class="bar"><i id="br"></i></div>'+
   '<p>Para cada pauta, piensa: ¿qué tiempo pide? ¿Qué nombre, qué lugar, qué fecha voy a decir?</p><div class="row"><button class="btn cta" data-act="skip">Ya estoy listo</button></div>';
 } else if(ph.k==='notas'){
  o='<div class="kk">PREPARACIÓN · TUS NOTAS</div><h3>Rellena el esquema: palabras clave y un verbo</h3><div class="clock" id="clk">4:00</div><div class="bar"><i id="br"></i></div>'+esqEdit(t, R.notes)+
   (S.n[S.tema]?'<div class="row" style="margin:6px 0"><button class="btn sm" data-act="oldnotes">Usar mis notas de la otra vez</button></div>':'')+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="skip">Ya he terminado: a hablar</button></div>';
 } else if(ph.k==='q'){
  var p=t.pa[ph.i], dots='';
  for(var d=0; d<5; d++) dots+='<i class="'+(d<ph.i?'d':(d===ph.i?'c':''))+'"></i>';
  o='<div class="kk">PAUTA '+(ph.i+1)+' DE 5'+recd+'</div><div class="dots" aria-hidden="true">'+dots+'</div><h3>'+esc(p.x)+'</h3><div>'+chips(p.t)+'</div>'+
   '<div class="clock" id="clk"></div><div class="bar"><i id="br"></i></div>';
  if(S.o.modelo){
   o+=(ph.i===0?'<p class="modtxt">'+t.ab+'</p>':'')+'<p class="modtxt">'+t.mod[ph.i]+'</p>'+(ph.i===4?'<p class="modtxt">'+t.ci+'</p>':'');
  } else {
   if(ph.i===0) o+='<p class="small" style="margin:4px 0"><b>Empieza:</b> <i>«Voy a hablar de '+esc(t.t.charAt(0).toLowerCase()+t.t.slice(1))+'...»</i></p>';
   o+='<ul class="esc">'+D.esc.map(function(e,k){ return '<li id="es'+k+'">'+(k+1)+'. '+esc(e)+'</li>'; }).join('')+'</ul>';
   if(hasNote(ph.i)) o+='<div class="myn"><b>TUS NOTAS</b>'+esc(String(R.notes[ph.i]).trim())+'</div>';
   o+='<div class="forms"><b>Verbos:</b> '+p.t.map(function(k){ return esc(D.ti[k].n)+': <i>'+esc(D.ti[k].f.join(', '))+'</i>'; }).join('<br>')+'</div>';
   if(ph.i===4) o+='<p class="small" style="margin:4px 0"><b>Termina:</b> <i>«'+esc(D.cerrar)+'»</i></p>';
  }
  o+='<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="next" id="bnext" disabled>Siguiente</button></div>';
 } else {
  o='<div class="kk">MODO EXAMEN'+recd+'</div><h3>Habla del tema entre 2 y 3 minutos</h3><div class="clock" id="clk">0:00</div><p class="small" id="clmsg"></p>'+
   '<p class="small muted">'+(R.useNotes?'Tus notas, en orden. Míralas, pero no las leas. ':'')+'Marca cada pauta cuando ya has hablado de ella:</p><ul class="chk">'+
   t.pa.map(function(p,k){ return '<li><label><input type="checkbox"><span>'+(k+1)+'. '+esc(p.x)+' '+chips(p.t)+(hasNote(k)?'<span class="lq-n">'+esc(String(R.notes[k]).trim())+'</span>':'')+'</span></label></li>'; }).join('')+'</ul>'+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="finish">Terminar</button></div>'+
   '<div class="warnbox" id="warn" hidden><b id="warnt"></b> En el examen tienes que hablar entre 2 y 3 minutos. ¿Has hablado de las cinco pautas, con tres frases cada una?<div class="row" style="margin:8px 0 0"><button class="btn sm cta" data-act="goon">Sigo hablando</button><button class="btn sm" data-act="finish2">Terminar igualmente</button></div></div>';
 }
 $('pan').innerHTML=o;
}
function tick(){
 if(!R.active) return;
 var ph=R.phases[R.phase], e=elapsed(), clk=$('clk'); if(!clk) return;
 var lv=lvRead(), lb=$('lvl'); if(lb && lv>=0) lb.style.width=Math.min(100, Math.round(Math.sqrt(lv)*160))+'%';
 if(lv>=0 && !R.micWarned && R.recSince && now()-R.recSince>10000){ R.micWarned=true; if(LV.max<1){ var mw=$('micw'); if(mw) mw.hidden=false; } }
 if(ph.k==='libre'){
  clk.textContent=mmss(e);
  clk.className='clock'+(e>=180?' red':(e>=120?' green':''));
  var m=$('clmsg'); if(m) m.textContent = e<120 ? 'Sigue: todavía no has llegado a 2 minutos.' : (e<180 ? '¡Bien! Ya estás entre 2 y 3 minutos. Termina con tu frase final.' : (e<210 ? 'Ya has pasado de 3 minutos: termina tu frase.' : 'En el examen, el examinador te pararía aquí.'));
 } else {
  var rem=ph.d-e, fr=Math.min(1,e/ph.d);
  clk.textContent=mmss(Math.ceil(rem)); clk.className='clock'+(rem<=5?' red':'');
  var br=$('br'); if(br) br.style.width=(fr*100)+'%';
  if(ph.k==='q'){
   for(var k=0;k<3;k++){ var li=$('es'+k); if(li) li.classList.toggle('on', fr>=k/3); }
   var bn=$('bnext'); if(bn){ var ready=fr>=2/3; bn.disabled=!ready; bn.textContent = ready ? (R.phase===R.phases.length-1?'Terminar':'Siguiente pauta') : 'Siguiente (en '+Math.ceil(ph.d*2/3-e)+' s)'; }
  }
 }
 var ml=$('minil'), mc=$('minic'); if(ml&&mc){ ml.textContent=(ph.k==='q'?'Pauta '+(ph.i+1)+'/5':(ph.k==='libre'?'Modo examen':'Preparación')); mc.textContent=clk.textContent; mc.style.color=clk.className.indexOf('red')>=0?'#FF9C85':(clk.className.indexOf('green')>=0?'#8FE3AE':''); }
 if(ph.k!=='libre' && ph.d-e<=0) advance();
}
function advance(){
 var ph=R.phases[R.phase];
 if(ph.k==='q') R.spoken+=Math.min(elapsed(), ph.d);
 if(ph.k==='notas'){ S.n[S.tema]=R.notes.slice(); save(); window.scrollTo(0,0); }
 if(R.phase<R.phases.length-1) enterPhase(R.phase+1); else finish();
}
function togglePause(){
 if(!R.active) return;
 if(R.paused){ R.paused=false; R.t0=now(); } else { R.acc=elapsed(); R.paused=true; }
 var b=$('bpause'); if(b) b.textContent = R.paused ? 'Seguir' : 'Pausa';
}
function stopRun(silent){
 document.body.classList.remove('focus','notas');
 if(R.timer) clearInterval(R.timer); R.timer=null; R.active=false; wake(false); recStop();
 if(!silent) showSetup();
}
function finish(){
 var secs = R.mode==='libre' ? elapsed() : R.spoken;
 document.body.classList.remove('focus','notas');
 if(R.timer) clearInterval(R.timer); R.timer=null; R.active=false; wake(false); recStop(); beep();
 var h=S.h[S.tema]||[]; h.push({s:Math.round(secs), m:R.mode, d:new Date().toISOString().slice(0,10)}); S.h[S.tema]=h.slice(-10); save(); nav();
 showDone(secs);
}
function showDone(secs){
 var t=curT(), v, cl;
 if(secs<90){ cl='bad'; v='Muy corto. Habla de las cinco pautas con tres frases cada una. Prueba el modo guiado.'; }
 else if(secs<120){ cl='amb'; v='Casi. Te falta un poco para llegar a 2 minutos: añade un detalle (un nombre, una fecha) o un «porque» en cada pauta.'; }
 else if(secs<=180){ cl='ok'; v='¡Perfecto! Entre 2 y 3 minutos, como pide el examen.'; }
 else { cl='amb'; v='Un poco largo. No pasa nada: en el examen, el examinador te para a los 3 minutos. Pero asegúrate de llegar a la pauta 5 antes.'; }
 var pos=Math.min(100, secs/240*100);
 var h=(S.h[S.tema]||[]).slice(-6).reverse();
 var o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="back">← Otros temas</button></div>';
 o+='<div class="run"><div class="side">'+lamina(t,{tags:true})+'</div><div><div class="res"><div class="kk muted small">'+(R.mode==='guiado'?'MODO GUIADO':'MODO EXAMEN')+'</div><div class="big">'+mmss(secs)+'</div>'+
  '<div class="zone" aria-hidden="true"><div class="ok"></div><div class="me" style="left:calc('+pos+'% - 2px)"></div><span style="left:0;transform:none">0</span><span style="left:25%">1 min</span><span style="left:50%">2 min</span><span style="left:75%">3 min</span></div>'+
  '<div class="verd '+cl+'">'+v+'</div>';
 if(h.length>1){ o+='<p class="small" style="margin:8px 0 0"><b>Tus tiempos con este tema:</b></p><ul class="hist">'+h.map(function(x){ return '<li>'+x.d.split('-').reverse().join('/')+' · '+mmss(x.s)+' ('+(x.m==='guiado'?'guiado':'examen')+')</li>'; }).join('')+'</ul>'; }
 o+='</div><div id="recout">'+recBlock()+'</div>';
 o+='<h4>Revísate</h4><ul class="chk">'+['He empezado con una frase: «Voy a hablar de...».','He hablado de las cinco pautas, en orden.','He usado el tiempo que pide cada pauta (presente, pasado, antes, futuro).','He dicho al menos tres frases en cada pauta.','He unido las frases con porque, por eso, además, cuando...','He terminado con una frase final.','He mirado mis notas, pero no las he leído.'].map(function(x){ return '<li><label><input type="checkbox"><span>'+x+'</span></label></li>'; }).join('')+'</ul>';
 o+='<details open><summary>El monólogo modelo</summary>'+modelHTML(t)+'</details>';
 o+='<div class="row"><button class="btn cta" data-act="again">Otra vez con este tema</button><button class="btn" data-act="back">Otro tema</button><button class="btn" data-go="opinion">Tu opinión</button></div></div></div>';
 if(R.useNotes){ o+='<h3 style="margin-top:24px">Tus notas y las notas modelo</h3><p class="small muted">Compara: ¿tienes algo en las cinco casillas? ¿Hay un verbo en el tiempo correcto en cada una? ¿Son palabras clave o frases?</p><div class="cmp"><div><h4>Tus notas</h4>'+esqStatic(t,R.notes)+'</div><div><h4>Notas modelo</h4>'+esqStatic(t,t.notas)+'</div></div>'; }
 else { o+='<details><summary>Ver las notas modelo de este tema</summary>'+esqStatic(t,t.notas)+'</details>'; }
 $('pr').innerHTML=o; window.scrollTo(0,0);
}

/* ---------------- opinion ---------------- */
function renderScale(){
 var o=''; for(var i=1;i<=10;i++){ o+='<label><input type="radio" name="o4" value="'+i+'"'+(String(S.o4)===String(i)?' checked':'')+'><span>'+i+'</span></label>'; }
 $('o4').innerHTML=o;
 ['o1','o3','o5'].forEach(function(k){ var r=document.querySelectorAll('input[name='+k+']'); for(var i=0;i<r.length;i++) r[i].checked = r[i].value===S[k]; });
 $('o2').value=S.o2; $('sname').value=S.name;
}
function pack(){
 var L=['CURSO DELE A2 - ORAL TAREA 1: HABLA DE UN TEMA', 'Nombre: '+(S.name||'-'), '', 'Ejercicio "Que tiempo pide": '+(S.qz.best===null?'sin hacer':'mejor resultado '+S.qz.best+'/10'), '', 'Mis tiempos:'];
 var any=false;
 D.temas.forEach(function(t){ var h=S.h[t.id]; if(h&&h.length){ any=true; L.push('  Tema '+t.id+' ('+t.t+'): '+h.map(function(x){ return mmss(x.s)+' '+(x.m==='guiado'?'guiado':'examen'); }).join(' > ')); } });
 if(!any) L.push('  (todavia no he practicado)');
 L.push('', '1. El modo guiado me ha ayudado: '+(S.o1||'-'), '2. El esquema de cinco casillas me ha servido: '+(S.o5||'-'), '3. El tiempo que me cuesta mas: '+(S.o3||'-'), '4. Al escucharme / falta: '+(S.o2||'-'), '5. Sensacion de control (1-10): '+(S.o4||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 pick:function(b){ S.tema=+b.getAttribute('data-id'); save(); showSetup(); window.scrollTo(0,0); },
 duo:function(){ showDuo(); window.scrollTo(0,0); },
 back:function(){ if(R.active) stopRun(true); showPick(); window.scrollTo(0,0); },
 start:function(){ startRun(); window.scrollTo(0,0); },
 skip:function(){ advance(); },
 next:function(b){ if(!b.disabled) advance(); },
 pause:function(){ togglePause(); },
 stop:function(){ stopRun(false); },
 finish:function(){ var e=elapsed(); if(e<120 && !R.warned){ R.warned=true; $('warnt').textContent='Solo llevas '+mmss(e)+'.'; $('warn').hidden=false; return; } finish(); },
 finish2:function(){ finish(); },
 goon:function(){ $('warn').hidden=true; },
 again:function(){ showSetup(); window.scrollTo(0,0); },
 delrec:function(){ recClear(); var a=$('recout'); if(a) a.innerHTML=''; },
 qnew:function(){ newQuiz(); },
 qcheck:function(){ checkQuiz(); },
 oldnotes:function(){ if(S.n[S.tema]){ R.notes=S.n[S.tema].slice(); renderPhase(); tick(); } },
 print:function(b){ var p=b.getAttribute('data-p'); if(p==='sheet'){ document.body.classList.add('ps'); window.print(); setTimeout(function(){ document.body.classList.remove('ps'); },500); return; }
  var v=$('v-'+p); v.classList.add('printme'); window.print(); setTimeout(function(){ v.classList.remove('printme'); },500); },
 copy:function(){
  var t=pack(), box=$('cbox');
  function ok(){ box.hidden=false; box.className='copied-box'; box.textContent='✓ Copiado. Pégalo en un correo para tu profesora.'; }
  function bad(){ box.hidden=false; box.className='copied-box bad'; box.textContent='No se ha podido copiar automáticamente. Escribe tus respuestas en un correo para tu profesora.'; }
  function fb(){ var ta=document.createElement('textarea'); ta.value=t; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.left='-9999px'; document.body.appendChild(ta); ta.select(); var d=false; try{ d=document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); if(d) ok(); else bad(); }
  if(navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) navigator.clipboard.writeText(t).then(ok, fb); else fb();
 }
};
document.addEventListener('click', function(e){
 var g=e.target.closest('[data-go]'); if(g){ go(g.getAttribute('data-go')); return; }
 var a=e.target.closest('[data-act]'); if(a && ACTS[a.getAttribute('data-act')]) ACTS[a.getAttribute('data-act')](a);
});
document.addEventListener('change', function(e){
 var t=e.target;
 if(t.name==='md'){ S.o.mode=t.value; save(); showSetup(); return; }
 if(t.id==='ritmo'){ S.o.ritmo=+t.value; save(); return; }
 if(t.getAttribute && t.getAttribute('data-o')){ S.o[t.getAttribute('data-o')]=t.checked; save(); return; }
 if(t.id==='prepsel'){ S.o.prep=t.value; save(); return; }
 if(t.name==='o1'||t.name==='o3'||t.name==='o4'||t.name==='o5'){ S[t.name]=t.value; save(); nav(); }
});
document.addEventListener('input', function(e){ var t=e.target;
 if(t.getAttribute && t.getAttribute('data-ni')!==null){ var i=+t.getAttribute('data-ni'); R.notes[i]=t.value; t.parentNode.classList.toggle('many', tooLong(t.value)); return; }
 if(t.id==='o2'){ S.o2=t.value; save(); nav(); } if(t.id==='sname'){ S.name=t.value; save(); } });
document.addEventListener('keydown', function(e){
 if((e.key==='Enter'||e.key===' ') && e.target.classList && e.target.classList.contains('lam') && e.target.getAttribute('data-act')){ e.preventDefault(); ACTS.pick(e.target); return; }
 if(R.active && e.code==='Space' && e.target===document.body){ e.preventDefault(); togglePause(); } });
document.addEventListener('visibilitychange', function(){ if(document.hidden && R.active && !R.paused) togglePause(); });
window.addEventListener('afterprint', function(){ [].forEach.call(document.querySelectorAll('.printme'), function(v){ v.classList.remove('printme'); }); document.body.classList.remove('ps'); });

renderScale(); renderPrep(); newQuiz();
var start=S.cur; go(start);
if(start==='practica' && S.tema) showSetup();
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_T1, body, js))
print("ok", FILE, "·", len(B.TEMAS), "temas ·", ", ".join("%d: %d pal." % (t["id"], t["w"]) for t in TEMAS_JS))
