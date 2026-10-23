# -*- coding: utf-8 -*-
# MODULO 4 DEL CURSO DE PREPARACION DELE A2 · ORAL TAREA 3: DIALOGO EN UNA SITUACION IMAGINARIA
# Uso: python3 build_M4_T3_dialogos.py
#  -> DELEA2_curso_M4_T3_dialogos.html  (subir a biblioteca/recursos/A2/dele-curso/)
# Contenido (situaciones, laminas, notas, dialogos modelo, frases y ejercicio): banco_dialogos_T3.py.
# Para anadir situaciones, solo se toca ese archivo.
# Mismo estilo y motor que los talleres de la tarea 1 y de la foto (build_M4_T1_temas.py, build_M4_T2_foto.py):
# modo guiado turno a turno / modo examen con reloj, preparacion con notas, grabacion opcional que se queda en el
# navegador del estudiante, modo concentracion.
import json, re
from curso_comun import CSS, EMAIL, page
import banco_dialogos_T3 as B

TITLE = "Habla con el examinador"
FILE = "DELEA2_curso_M4_T3_dialogos.html"
STORAGE = "dele-a2-curso-M4-T3"
WPM = 105   # palabras por minuto de un candidato A2 que habla con calma (el examinador adapta su ritmo)
PAUSA = 1.5 # segundos de silencio en cada cambio de turno (pensar, empezar a responder)

# ------------------------------------------------------------ comprobaciones del banco
TAG = re.compile(r"\{([pqar]):(.+?)\}")
TU_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(tú|tienes|puedes|quieres|prefieres|sabes|conoces|te|contigo|mira|perdona)(?![\wÀ-ſ])")
US_PAL = re.compile(r"(?i)(?<![\wÀ-ſ])(usted|ustedes)(?![\wÀ-ſ])")

def plain(s):
    return TAG.sub(r"\2", s)
def marked(s):
    return TAG.sub(lambda m: '<span class="f f-%s">%s</span>' % (m.group(1), m.group(2)), s)

ids = [d["id"] for d in B.DIALOGOS]
assert len(ids) == len(set(ids)), "Hay dos situaciones con el mismo id"
assert B.EJEMPLO in ids and B.EJEMPLO_NOTAS in ids
for d in B.DIALOGOS:
    n, tu = len(d["pautas"]), d["turnos"]
    ref = "Situacion %d" % d["id"]
    assert d["tipo"] in B.TIPOS and d["area"] in B.AREAS and d["trato"] in ("tu", "usted"), ref + ": tipo, area o trato desconocido"
    assert len(d["notas"]) == n, ref + ": hace falta una nota por pauta"
    assert tu[0]["k"] == "s" and tu[-1]["k"] == "d", ref + ": el primer turno es el saludo y el ultimo la despedida"
    cub = set(x["p"] for x in tu if x["p"] is not None)
    falta = [i + 1 for i in range(n) if i not in cub]
    assert not falta, ref + ": ningun turno trabaja la pauta %s" % falta
    probs = [x for x in tu if x["x"]]
    assert len(probs) == 1, ref + ": tiene que haber un (y solo un) pequeno problema"
    assert "{r:" in probs[0]["c"], ref + ": despues del problema, el candidato busca otra solucion ({r:...})"
    todo = " ".join(x["c"] for x in tu)
    usadas = set(m for m, _ in TAG.findall(todo))
    assert usadas == set(B.ORDEN_F), ref + ": faltan frases de tipo %s" % (set(B.ORDEN_F) - usadas)
    assert todo.count("{q:") >= 3, ref + ": el candidato tiene que preguntar al menos tres veces"
    for x in tu:
        assert not re.search(r"\{(?![pqar]:)", x["c"]), ref + ": marca mal escrita: " + x["c"][:50]
        txt = plain(x["c"])
        if d["trato"] == "usted":
            assert not TU_PAL.search(txt), ref + ": el candidato habla de tu en un dialogo de usted: " + txt[:60]
        else:
            assert not US_PAL.search(txt), ref + ": el candidato habla de usted en un dialogo de tu: " + txt[:60]
for q in B.QUIZ:
    assert len(q["ops"]) == 3 and 0 <= q["ok"] < 3

DIAL_JS, AVISOS = [], []
for d in B.DIALOGOS:
    we = sum(len(x["e"].split()) for x in d["turnos"])
    wc = sum(len(plain(x["c"]).split()) for x in d["turnos"])
    mins = (we + wc) / WPM + len(d["turnos"]) * 2 * PAUSA / 60
    if not 2.75 <= mins <= 4.4:
        AVISOS.append("Situacion %d: unos %.1f min (lo normal: 3-4)" % (d["id"], mins))
    DIAL_JS.append({"id": d["id"], "tipo": d["tipo"], "tr": d["trato"], "t": d["titulo"], "n": d["nombre"], "area": B.AREAS[d["area"]],
                    "rol": d["rol"], "quien": d["quien"], "sit": d["sit"], "pa": d["pautas"], "notas": d["notas"], "planb": d["planb"],
                    "prob": d["problema"],
                    "tu": [{"e": x["e"], "c": marked(x["c"]), "p": x["p"], "k": x["k"], "x": x["x"], "wc": len(plain(x["c"]).split()),
                            "we": len(x["e"].split()), "f": sorted(set(m for m, _ in TAG.findall(x["c"])), key=B.ORDEN_F.index)} for x in d["turnos"]],
                    "we": we, "wc": wc, "min": round(mins * 2) / 2})

# ------------------------------------------------------------ CSS
CSS_T3 = CSS + r"""
:root{--blu:#2B5FA8;--blu-soft:#E4ECF8;--grn:#2F7D4F;--grn-soft:#E3F1E8}
.f{border-radius:3px;padding:0 2px;font-weight:600}
.f-p{background:var(--blu-soft);color:#1E4A87}
.f-q{background:var(--amb-soft);color:#7A4E0E}
.f-a{background:var(--grn-soft);color:#22603C}
.f-r{background:#FFE2D6;color:#9C3A1E}
.ch{display:inline-block;font-size:.76rem;font-weight:700;letter-spacing:.03em;border-radius:999px;padding:1px 9px;margin:0 3px 3px 0;vertical-align:middle;white-space:nowrap}
.ch.p{background:var(--blu-soft);color:#1E4A87}.ch.q{background:var(--amb-soft);color:#7A4E0E}.ch.a{background:var(--grn-soft);color:#22603C}.ch.r{background:#FFE2D6;color:#9C3A1E}
.ch.tr{background:var(--ink);color:#fff}.ch.ty{background:#EFEAE4;color:var(--muted)}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.88rem;margin:6px 0 10px}
section.view > h3,.quizwrap > h3{margin-top:28px}
/* lamina */
.lam{background:#fff;border:2px solid var(--ink);border-radius:6px;padding:14px 18px;margin:12px 0;font-size:.97rem}
.lam .lh{font-size:.78rem;letter-spacing:.06em;color:var(--muted);text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:6px;margin-bottom:8px;display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
.lam h3{margin:0 0 6px;font-size:1.05rem;letter-spacing:.02em}
.lam .ins{font-size:.78rem;font-weight:700;letter-spacing:.08em;color:var(--muted);margin-top:8px}
.lam p{margin:4px 0 6px}
.lam ul{margin:0;padding-left:0;list-style:none}
.lam li{padding:5px 0 5px 30px;position:relative;border-bottom:1px dashed var(--line)}
.lam li:last-child{border-bottom:0}
.lam li .bn{position:absolute;left:0;top:6px;width:22px;height:22px;border-radius:50%;background:var(--ink);color:#fff;font-size:.78rem;font-weight:700;display:grid;place-items:center}
.lam li.cur{background:var(--coral-soft);border-radius:6px;margin:0 -6px;padding-left:36px;padding-right:6px}
.lam li.cur .bn{background:var(--coral);left:6px}
.lam li.done{color:var(--muted)}
.lam li.done .bn{background:var(--ok)}
.lam .tg2{margin:2px 0 4px}
.lam.sm{font-size:.9rem;padding:10px 14px}
/* tarea */
.tl{display:grid;grid-template-columns:.8fr repeat(5,1fr) .8fr;gap:4px;margin:14px 0 4px}
.tl div{background:var(--coral-soft);border-top:5px solid var(--coral);border-radius:4px;padding:6px 4px;text-align:center;font-size:.8rem;line-height:1.3}
.tl div.ed{background:#fff;border-top-color:var(--ink)}
.tl div.pb{background:#FFE2D6;border-top-color:#9C3A1E}
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
.tipo{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:12px 16px}
.tipo h3{margin:0 0 4px}
.tipo dl{display:grid;grid-template-columns:6em 1fr;gap:4px 8px;margin:6px 0 0;font-size:.93rem}
.tipo dt{font-size:.74rem;font-weight:700;letter-spacing:.05em;color:var(--muted);padding-top:3px;text-transform:uppercase}
.tipo dd{margin:0}
/* frases */
.fgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.fcard{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px;border-top:6px solid var(--line)}
.fcard.p{border-top-color:var(--blu)}.fcard.q{border-top-color:var(--amb)}.fcard.a{border-top-color:var(--grn)}.fcard.r{border-top-color:var(--coral)}
.fcard h3{margin:0 0 2px}
.fcard .qq{color:var(--muted);font-size:.92rem;margin:0 0 8px}
.fcols{display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:.92rem}
.fcols b{display:block;font-size:.74rem;letter-spacing:.05em;color:var(--muted);text-transform:uppercase}
.fcols ul{margin:2px 0 0;padding-left:1em}
.fcols li{font-style:italic}
table.t td:first-child,table.t th:first-child{width:50%}
.quiz{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 18px;margin:14px 0}
.quiz .qn{font-size:.8rem;font-weight:700;letter-spacing:.06em;color:var(--coral)}
.quiz .qs{font-size:.88rem;color:var(--muted);margin:0 0 6px}
.quiz .qe{font-size:1.08rem;font-family:Georgia,serif;margin:4px 0 10px}
.qop{display:block;width:100%;text-align:left;font:inherit;background:#fff;border:2px solid var(--line);border-radius:10px;padding:9px 14px;margin:6px 0;cursor:pointer;color:inherit}
.qop:hover:not(:disabled){border-color:var(--coral)}
.qop:disabled{cursor:default}
.qop.ok{border-color:var(--ok);background:var(--ok-soft)}
.qop.bad{border-color:var(--bad);background:var(--bad-soft)}
.fb{border-radius:10px;padding:10px 14px;margin:10px 0 0;font-size:.95rem}
.fb.ok{background:var(--ok-soft)}.fb.bad{background:var(--bad-soft)}
.score{font-family:Georgia,serif;font-size:2.2rem;font-weight:700}
/* dialogo */
.dlg{margin:8px 0}
.dl{border-radius:12px;padding:8px 12px;margin:6px 0;max-width:88%;font-size:.97rem;line-height:1.5}
.dl b.who{display:block;font-size:.74rem;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.dl.e{background:#F1EDE8;margin-right:auto}
.dl.c{background:#fff;border:1px solid var(--line);margin-left:auto}
.dl.x{box-shadow:inset 4px 0 0 #9C3A1E}
.dl .pn{display:inline-grid;place-items:center;min-width:20px;height:20px;border-radius:99px;background:var(--ink);color:#fff;font-size:.72rem;font-weight:700;padding:0 6px;margin-right:4px}
.dl .px{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.04em;background:#FFE2D6;color:#9C3A1E;border-radius:99px;padding:0 8px;margin-left:4px}
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
.eb{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:8px 12px 10px;min-height:4.4em}
.eh{display:flex;align-items:center;gap:8px;font-weight:700;font-size:.9rem;margin-bottom:4px;flex-wrap:wrap}
.en{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--coral);color:#fff;font-family:Georgia,serif;font-size:1.05rem;flex:0 0 auto}
.en.b{background:#9C3A1E;font-size:.85rem}
.eh .px{font-weight:400;color:var(--muted);font-size:.86rem;flex:1 1 12em}
.enote{font-size:.95rem;line-height:1.45;white-space:pre-wrap}
.esq.blank .eb{min-height:6em}
.eb textarea{width:100%;font:inherit;font-size:.95rem;line-height:1.5;border:1px dashed #CFC6BB;border-radius:8px;padding:6px 8px;min-height:3.2em;resize:vertical;background:var(--paper)}
.eb .wn{font-size:.8rem;color:#7A4E0E;background:var(--amb-soft);border-radius:6px;padding:2px 8px;margin-top:4px;display:none}
.eb.many .wn{display:block}
.eb.end{border-style:dashed;min-height:0}
.eb.tr{border-color:var(--coral);min-height:0}
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
.exq{background:#F1EDE8;border-radius:12px;padding:10px 14px;margin:8px 0 10px;font-family:Georgia,serif;font-size:1.15rem;line-height:1.45}
.exq b{display:block;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:.74rem;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.probl{background:#FFE2D6;color:#7A2A12;border-radius:10px;padding:8px 12px;margin:6px 0;font-size:.92rem}
.clock{font-family:Georgia,serif;font-size:2.6rem;font-weight:700;font-variant-numeric:tabular-nums;line-height:1}
.clock.green{color:var(--ok)}.clock.red{color:var(--bad)}
.bar{height:12px;background:var(--line);border-radius:99px;overflow:hidden;margin:10px 0}
.bar i{display:block;height:100%;background:var(--coral);width:0}
.esc{list-style:none;padding:0;margin:10px 0}
.esc li{padding:7px 10px;border-radius:8px;margin:4px 0;color:#B5ADA4;border:1px dashed var(--line)}
.esc li.on{color:var(--ink);background:var(--coral-soft);border:1px solid transparent;font-weight:600}
.forms{font-size:.92rem;margin:8px 0;padding:8px 12px;border-left:4px solid var(--amb);background:var(--amb-soft);border-radius:0 8px 8px 0}
.forms div{margin:2px 0}
.dots{display:flex;gap:4px;margin:4px 0 8px}
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
.modtxt{font-size:.98rem;margin:6px 0 0;background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 12px}
.res{background:#fff;border:2px solid var(--ink);border-radius:14px;padding:16px 20px;margin:12px 0}
.res .big{font-family:Georgia,serif;font-size:2.4rem;font-weight:700;line-height:1}
.verd{border-radius:10px;padding:10px 14px;font-weight:600;margin:10px 0}
.verd.ok{background:var(--ok-soft);color:var(--ok)}.verd.amb{background:var(--amb-soft);color:#7A4E0E}.verd.bad{background:var(--bad-soft);color:var(--bad)}
.zone{position:relative;height:16px;background:var(--line);border-radius:99px;margin:20px 0 26px}
.zone .ok{position:absolute;top:0;bottom:0;left:60%;width:20%;background:var(--ok-soft);border-left:2px solid var(--ok);border-right:2px solid var(--ok)}
.zone .me{position:absolute;top:-6px;width:4px;height:28px;background:var(--ink);border-radius:2px}
.zone span{position:absolute;top:20px;font-size:.75rem;color:var(--muted);transform:translateX(-50%)}
.hist{font-size:.92rem;margin:6px 0}
audio{width:100%;margin:8px 0}
.warnbox{background:var(--amb-soft);border-radius:10px;padding:12px 14px;margin:10px 0}
.warnbox[hidden]{display:none}
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
 body.focus .run .side .lam{max-height:30vh;overflow:auto;margin:0}
 body.focus.notas .run .side .lam{max-height:20vh}
 body.focus .pan{padding:12px 14px}body.focus .clock{font-size:2rem}
 body.focus .mini{display:flex;justify-content:space-between;gap:10px;background:var(--ink);color:#fff;border-radius:8px;padding:6px 12px;margin-top:6px;font-weight:600;font-size:.92rem}
 body.focus .mini b{font-family:Georgia,serif;font-variant-numeric:tabular-nums}}
@media (max-width:760px){.grid,.modes,.two,.vs,.cmp,.duo,.fgrid{grid-template-columns:1fr}.r12 div{font-size:.7rem;padding:6px 2px}.tl div{font-size:.66rem}.tipo dl{grid-template-columns:1fr}.dl{max-width:96%}}
@media (max-width:420px){.fcols{grid-template-columns:1fr}}
@media print{header.top,.row,.noprint,footer.legal,.quizwrap{display:none!important}body{background:#fff}section.view{display:none!important}section.view.printme{display:block!important;padding-top:0}
 body.ps main,body.ps header{display:none!important}body.ps #sheet{display:block;padding:0 4mm}
 #sheet h2{font-size:15pt;margin:0 0 2mm}#sheet .eb{min-height:24mm;break-inside:avoid}
 .fcard,.lam,.box,.tipo{break-inside:avoid}details{border:0}details>*{display:block}}
"""

# ------------------------------------------------------------ VISTAS
STEPS = [("tarea", "La tarea"), ("frases", "Las frases"), ("prep", "La preparación"), ("practica", "Practica"), ("opinion", "Tu opinión")]

def ch(k):
    return '<span class="ch %s">%s</span>' % (k, B.FUNCIONES[k]["nombre"])
LEG = '<div class="legend">' + "".join(ch(k) for k in B.ORDEN_F) + '</div>'

def D(i):
    return [d for d in B.DIALOGOS if d["id"] == i][0]

def lamina_html(d, opc="1"):
    lis = "".join('<li><span class="bn">%d</span>%s</li>' % (i + 1, p) for i, p in enumerate(d["pautas"]))
    return ('<div class="lam"><div class="lh"><span>Tarea 3. Diálogo en una situación imaginaria</span><span>Opción %s</span></div>'
            '<h3>%s</h3><p>%s El examinador / La examinadora es %s. Hable con él/ella siguiendo estas indicaciones.</p>'
            '<div class="ins">CANDIDATO</div><p>Durante la conversación, tiene que%s</p><ul>%s</ul></div>'
            % (opc, d["titulo"], d["sit"], d["rol"], " hablar de:" if d["tipo"] == "plan" else ":", lis))

def dialogo_html(d):
    o = ['<div class="dlg">']
    for x in d["turnos"]:
        pn = '<span class="pn">%s</span>' % ("Hola" if x["k"] == "s" else ("Adiós" if x["k"] == "d" else x["p"] + 1)) if (x["p"] is not None or x["k"]) else ""
        o.append('<div class="dl e%s"><b class="who">%s%s%s</b>%s</div>' % (" x" if x["x"] else "", pn, d["quien"],
                 '<span class="px">PEQUEÑO PROBLEMA</span>' if x["x"] else "", x["e"]))
        o.append('<div class="dl c"><b class="who">Candidato</b>%s</div>' % marked(x["c"]))
    return "".join(o) + "</div>"

EJ = D(B.EJEMPLO)
tl = ('<div class="ed"><b>Hola</b>saludo</div><div><b>1</b>pauta</div><div><b>2</b>pauta</div><div class="pb"><b>!</b>problema</div>'
      '<div><b>3</b>pauta</div><div><b>4-5</b>pautas</div><div class="ed"><b>Adiós</b>plan claro</div>')

def tipo_box(k):
    v = B.TIPOS[k]
    return ('<div class="tipo"><h3>%s</h3><p class="small muted" style="margin:0">%s</p><dl><dt>El examinador</dt><dd>%s</dd>'
            '<dt>Trato</dt><dd><b>%s</b></dd><dt>Qué haces</dt><dd>%s</dd><dt>En el examen</dt><dd>%s</dd></dl></div>'
            % (v["nombre"], v["largo"], v["quien"], v["trato"], v["que"], v["oficial"]))

V_TAREA = """
<h2>La tarea 3 de la oral: un diálogo con el examinador</h2>
<p class="lead">Es la última tarea. Hablas con el examinador <b>entre 3 y 4 minutos</b> en una situación imaginaria. La situación va con la foto que has descrito en la tarea 2: está en la misma lámina, debajo de las preguntas de la foto. El examinador hace un papel (tu amigo, tu hermano, un dependiente...) y tú eres tú.</p>
<div class="note"><b>Así es la lámina</b> (esta situación es de práctica; en el examen el formato es igual):""" + lamina_html(EJ) + """</div>

<h3>Cómo trabaja el examinador</h3>
<p>Tiene un guion con preguntas para cada pauta. Empieza él: te saluda y te pregunta. Elige las preguntas según lo que dices: si das detalles, pregunta menos; si contestas poco, tiene que preguntar más. Y no siempre dice que sí: a veces ese día no puede, no le gusta tu idea, algo es caro o no hay. Es el <b>pequeño problema</b>: quiere ver si sabes reaccionar y buscar otra solución. Cuando habéis hablado de todas las pautas, termina.</p>
<div class="tl" aria-hidden="true">""" + tl + """</div>
<div class="tl-cap"><span>0:00</span><span>en cualquier momento puede llegar el problema</span><span>3-4 min</span></div>

<h3>Dos tipos de diálogo</h3>
<div class="two">""" + tipo_box("plan") + tipo_box("serv") + """</div>

<h3>Lo que pasa a muchos candidatos</h3>
<div class="vs">
 <div class="no"><b>Solo «sí», «no», «vale»</b>Contestan con una palabra y esperan la pregunta siguiente. El examinador tiene que hacer todo el trabajo, la conversación se para y la tarea queda a medias.</div>
 <div class="si"><b>Responden, añaden y preguntan</b>Contestan, dan un detalle o un porqué y después preguntan o proponen algo. Hablan los dos, como en una conversación de verdad.</div>
</div>

<h3>Cinco claves</h3>
<ol class="keys">
 <li><b>Tú o usted, del saludo a la despedida.</b> Con un amigo o un familiar, tú. Con un dependiente o un empleado, usted. No lo mezcles: <i>¿Tienes...?</i> o <i>¿Tiene...?</i></li>
 <li><b>Tres cosas en cada turno.</b> Responde, añade un detalle o di por qué, y pregunta o propón algo.</li>
 <li><b>Propón tú también.</b> No esperes solo a contestar: <i>«¿Qué te parece si...?», «¿Por qué no...?», «Quería...»</i>.</li>
 <li><b>Si dice que no, busca otra solución.</b> <i>«Vaya, qué pena. ¿Y si...?»</i>. Quedarse callado o decir solo «vale» es perder la oportunidad.</li>
 <li><b>Termina con el plan claro.</b> Día, hora y lugar (o qué compras y cuánto pagas), y una despedida.</li>
</ol>
<div class="tip"><b>Puedes inventar.</b> """ + B.INVENTAR + """</div>
<div class="tip"><b>Cómo practicar aquí:</b> aprende las frases y prueba el ejercicio «¿Qué respondes?». Después mira cómo preparar el diálogo en 2 minutos. Para practicar, empieza con el <b>modo guiado</b> (cada frase del examinador en pantalla, con tiempo para responder) y, cuando lo hagas sin ayuda, pasa al <b>modo examen</b>.</div>
<div class="row"><button class="btn cta" data-go="frases">Siguiente: las frases</button></div>
"""

def fcard(k):
    v = B.FUNCIONES[k]
    return ('<div class="fcard %s"><h3>%s</h3><p class="qq">%s</p><div class="fcols"><div><b>Con un amigo (tú)</b><ul>%s</ul></div>'
            '<div><b>En una tienda (usted)</b><ul>%s</ul></div></div></div>'
            % (k, v["nombre"], v["que"], "".join("<li>%s</li>" % x for x in v["plan"]), "".join("<li>%s</li>" % x for x in v["serv"])))
def cols(dct):
    return ('<div class="fcols"><div><b>Con un amigo (tú)</b><ul>%s</ul></div><div><b>En una tienda (usted)</b><ul>%s</ul></div></div>'
            % ("".join("<li>%s</li>" % x for x in dct["plan"]), "".join("<li>%s</li>" % x for x in dct["serv"])))

V_FRASES = ("""
<h2>Las frases para interactuar</h2>
<p class="lead">En la tarea 3 no tienes que contar nada largo: tienes que <b>proponer, preguntar, reaccionar y negociar</b>. Estas frases son tus herramientas. En los diálogos modelo salen con estos colores:</p>""" + LEG + """
<div class="fgrid">""" + "".join(fcard(k) for k in B.ORDEN_F) + """</div>
<div class="two">
 <div class="box"><h4>Para empezar</h4>""" + cols(B.SALUDAR) + """</div>
 <div class="box"><h4>Para terminar</h4>""" + cols(B.DESPEDIR) + """</div>
</div>
<h3>Tú o usted</h3>
<table class="t"><thead><tr><th>Con un amigo, tu hermano, un compañero</th><th>Con un dependiente, un empleado</th></tr></thead><tbody>""" +
 "".join("<tr><td><i>%s</i></td><td><i>%s</i></td></tr>" % x for x in B.TU_USTED) + """</tbody></table>
<div class="box"><h4>Si no entiendes o no sabes una palabra</h4><ul>""" + "".join("<li><i>%s</i></li>" % x for x in B.NO_ENTIENDO) + """</ul><p class="small muted">Pedir que repita o preguntar una palabra es normal en A2. Lo que baja la nota es quedarse callado.</p></div>
<details><summary>Ver un diálogo modelo con las frases marcadas: «""" + EJ["nombre"] + """»</summary>""" + LEG + dialogo_html(EJ) + """</details>

<div class="quizwrap">
<h3>Practica: ¿qué respondes?</h3>
<p>Ocho frases del examinador. Elige la mejor respuesta y mira por qué.</p>
<div id="quiz"></div>
</div>
<div class="row"><button class="btn" data-act="print" data-p="frases">Imprimir esta página</button><button class="btn cta" data-go="prep">Siguiente: la preparación</button></div>
""")

REPARTO = [(1, "Elegir", "Lee los dos temas de la tarea 1 y mira las dos fotos de la tarea 2 (con su tarea 3 debajo)."),
           (4, "Tarea 1", "El monólogo: el esquema de cinco casillas."),
           (4, "Tarea 2", "La foto: el esquema de las seis casillas."),
           (2, "Tarea 3", "El diálogo: tus ideas y tus preguntas para cada pauta."),
           (1, "Repasar", "Mira tus notas de las tres tareas y respira.")]
assert sum(m for m, _, _ in REPARTO) == 12
r12 = "".join('<div class="%s" style="flex:%d"><b>%d min</b>%s</div>' % ("me" if t == "Tarea 3" else "", m, m, t) for m, t, _ in REPARTO)
r12l = "".join("<li><b>%s (%d min):</b> %s</li>" % (t, m, d) for m, t, d in REPARTO)
p2 = "".join('<li><span class="tm">%s</span><span><b>%s.</b> %s</span></li>' % x for x in B.PASOS_T3)
reg = "".join("<li>%s</li>" % x for x in B.REGLAS_NOTAS_T3)
EJN = D(B.EJEMPLO_NOTAS)
V_PREP = """
<h2>La preparación: 2 minutos para el diálogo</h2>
<p class="lead">Antes de entrar tienes <b>12 minutos para preparar las tres tareas</b>. Para la tarea 3 bastan unos 2 minutos: no puedes escribir el diálogo, porque no sabes qué va a decir el examinador. Preparas <b>ideas y preguntas</b>.</p>
<h3>Cómo repartir los 12 minutos</h3>
<div class="r12" aria-hidden="true">""" + r12 + """</div>
<div class="r12cap"><span>0:00</span><span>12:00</span></div>
<ul class="r12list">""" + r12l + """</ul>
<div class="tip">Es una recomendación, no una regla del examen. La tarea 3 va con la foto que eliges: cuando elijas foto, mira también la situación de abajo. Elige la opción en la que tienes más que decir.</div>

<h3>Tus 2 minutos, paso a paso</h3>
<ol class="steps4">""" + p2 + """</ol>

<h3>El esquema del diálogo</h3>
<p>Arriba, TÚ o USTED. Después, una casilla por pauta: tu idea en palabras clave y una pregunta para el examinador. Al final, tu segunda opción por si te dice que no.</p>
<div id="esq-blank"></div>
<div class="row"><button class="btn" data-act="print" data-p="sheet">Imprimir el esquema en blanco</button></div>

<h3>Un ejemplo: así quedan las notas</h3>
<p>Estas son las notas de la situación <i>«""" + EJN["nombre"] + """»</i>. Fíjate: palabras sueltas, horas, flechas y una pregunta con «?» en casi todas las casillas.</p>
<div class="two"><div>""" + lamina_html(EJN) + """</div><div id="esq-ej"></div></div>

<h3>Reglas para tus notas</h3>
<ul class="keys">""" + reg + """</ul>
<div class="row"><button class="btn cta" data-go="practica">Siguiente: practica</button></div>
"""

V_PRACTICA = '<div id="pr"></div>'

CUESTA = ["Proponer", "Preguntar", "Reaccionar", "Decir que no y buscar otra solución", "Usar usted"]
V_OPINION = """
<h2>Tu opinión</h2>
<p class="lead">Estás probando este curso antes que nadie. Tus respuestas me ayudan mucho a mejorarlo.</p>
<div class="opn">
 <label class="q" id="o1l">1. ¿El modo guiado te ha ayudado a no contestar solo «sí» o «no»?</label>
 <div class="chips" role="group" aria-labelledby="o1l">
  <label><input type="radio" name="o1" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o1" value="Un poco">Un poco</label>
  <label><input type="radio" name="o1" value="No">No</label>
  <label><input type="radio" name="o1" value="No lo he probado">No lo he probado</label>
 </div>
 <label class="q" id="o5l">2. ¿Te ha servido el esquema de ideas y preguntas para preparar el diálogo?</label>
 <div class="chips" role="group" aria-labelledby="o5l">
  <label><input type="radio" name="o5" value="Sí, mucho">Sí, mucho</label>
  <label><input type="radio" name="o5" value="Un poco">Un poco</label>
  <label><input type="radio" name="o5" value="No">No</label>
  <label><input type="radio" name="o5" value="No lo he probado">No lo he probado</label>
 </div>
 <label class="q" id="o3l">3. ¿Qué te cuesta más en el diálogo?</label>
 <div class="chips" role="group" aria-labelledby="o3l">__CHIPS__</div>
 <label class="q" for="o2">4. ¿Te has grabado? ¿Qué has notado al escucharte? (O, si no, ¿qué falta o no has entendido?)</label>
 <textarea id="o2"></textarea>
 <label class="q" id="o4l">5. Ahora, ¿cuánto control sientes en el diálogo con el examinador? (1 = nada, 10 = total)</label>
 <div class="scale" role="group" aria-labelledby="o4l" id="o4"></div>
</div>
<div class="sendbox">
 <h3>Envía tu opinión y tus tiempos a tu profesora</h3>
 <label><b>Tu nombre</b><br><input type="text" id="sname" autocomplete="name"></label>
 <div class="row"><button class="btn cta" data-act="copy">Copiar</button></div>
 <div class="copied-box" id="cbox" role="status" hidden></div>
 <p class="muted small">Pégalo en un correo para tu profesora: __EMAIL__. Tus grabaciones no se copian: si quieres que tu profesora te escuche, guarda el audio y envíalo tú.</p>
</div>
""".replace("__CHIPS__", "".join('<label><input type="radio" name="o3" value="%s">%s</label>' % (x, x) for x in CUESTA)).replace("__EMAIL__", EMAIL)

BODY = """
<header class="top"><div class="top-in">
 <div class="brand"><h1 style="font-size:1.35rem;margin:0">__TITLE__</h1><small>Preparación DELE A2 · Oral · Tarea 3</small></div>
 <nav class="steps" id="steps" aria-label="Partes de esta página"></nav>
</div></header>
<main class="wrap">
__VIEWS__
<footer class="legal">Material de preparación original. No es un examen oficial y es independiente del Instituto Cervantes.</footer>
</main>
<div id="sheet"><h2>El diálogo · mis notas</h2><p style="margin:0 0 3mm">Situación: ______________________________________</p><div id="esq-sheet"></div></div>
"""

views = {"tarea": V_TAREA, "frases": V_FRASES, "prep": V_PREP, "practica": V_PRACTICA, "opinion": V_OPINION}
VIEWS_HTML = "\n".join('<section class="view" id="v-%s">%s</section>' % (k, views[k]) for k, _ in STEPS)
body = BODY.replace("__TITLE__", TITLE).replace("__VIEWS__", VIEWS_HTML)

FN = {k: {"n": v["nombre"], "plan": v["plan"], "serv": v["serv"]} for k, v in B.FUNCIONES.items()}
DATA = {"key": STORAGE, "steps": [{"id": k, "label": l} for k, l in STEPS], "dl": DIAL_JS, "fn": FN, "ord": B.ORDEN_F,
        "tipos": {k: v["nombre"] for k, v in B.TIPOS.items()}, "sal": B.SALUDAR, "des": B.DESPEDIR, "esc": B.ESC,
        "ej": B.EJEMPLO_NOTAS, "quiz": B.QUIZ, "wpm": WPM, "pausa": PAUSA}

# ------------------------------------------------------------ JS
JS = r"""
(function(){
var D = __DATA__;
function $(id){ return document.getElementById(id); }
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;'); }
function blank(){ return {cur:'tarea', seen:{}, dl:null, duo:null, o:{mode:'guiado', ritmo:20, prep:'notas', modelo:false, rec:false, beep:true}, h:{}, n:{}, qz:{best:null, last:null}, o1:'', o2:'', o3:'', o4:'', o5:'', name:''}; }
var S = (function(){ try{ var r=localStorage.getItem(D.key); if(r){ var o=JSON.parse(r), b=blank(); for(var k in b){ if(!(k in o)) o[k]=b[k]; } for(var j in b.o){ if(!(j in o.o)) o.o[j]=b.o[j]; } return o; } }catch(e){} return blank(); })();
function save(){ try{ localStorage.setItem(D.key, JSON.stringify(S)); }catch(e){} }
function G(id){ for(var i=0;i<D.dl.length;i++) if(D.dl[i].id===id) return D.dl[i]; return null; }
function mmss(s){ s=Math.max(0,Math.round(s)); return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2); }
function chip(k){ return '<span class="ch '+k+'">'+esc(D.fn[k].n)+'</span>'; }
function legend(){ return '<div class="legend">'+D.ord.map(chip).join('')+'</div>'; }
function trChip(g){ return '<span class="ch tr">'+(g.tr==='tu'?'TÚ':'USTED')+'</span><span class="ch ty">'+esc(D.tipos[g.tipo])+'</span>'; }
function shuffle(a){ for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }

/* ---------------- navegacion ---------------- */
function practiced(){ return Object.keys(S.h).length>0; }
function nav(){
 var o='';
 D.steps.forEach(function(st,i){
  var done = st.id==='practica' ? practiced() : (st.id==='opinion' ? !!(S.o1||S.o2||S.o3||S.o4||S.o5) : (st.id==='frases' ? S.qz.best!==null : !!S.seen[st.id]));
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

/* ---------------- lamina y dialogo ---------------- */
function lamina(g, o){
 o=o||{};
 var lis=g.pa.map(function(p,i){
  var cls = (o.cur===i) ? 'cur' : (o.done && o.done[i] ? 'done' : '');
  return '<li class="'+cls+'"><span class="bn">'+(i+1)+'</span>'+esc(p)+'</li>';
 }).join('');
 return '<div class="lam'+(o.sm?' sm':'')+'"'+(o.attr||'')+'><div class="lh"><span>Tarea 3. Diálogo en una situación imaginaria</span><span>'+(o.opc?'Opción '+o.opc:esc(g.area))+'</span></div>'+
  (o.tags?'<div class="tg2">'+trChip(g)+'</div>':'')+'<h3>'+esc(g.t)+'</h3><p>'+esc(g.sit)+' El examinador / La examinadora es '+esc(g.rol)+'. Hable con él/ella siguiendo estas indicaciones.</p>'+
  '<div class="ins">CANDIDATO</div><p>Durante la conversación, tiene que'+(g.tipo==='plan'?' hablar de:':':')+'</p><ul>'+lis+'</ul></div>';
}
function pnum(x){ return x.k==='s'?'Hola':(x.k==='d'?'Adiós':(x.p!==null?(x.p+1):'')); }
function dialogHTML(g){
 var o='<p class="small muted">Unas '+(g.we+g.wc)+' palabras entre los dos: unos '+String(g.min).replace('.',',')+' minutos de conversación, hablando con calma. En color, las frases para interactuar:</p>'+legend()+'<div class="dlg">';
 g.tu.forEach(function(x){
  var pn=pnum(x);
  o+='<div class="dl e'+(x.x?' x':'')+'"><b class="who">'+(pn!==''?'<span class="pn">'+pn+'</span>':'')+esc(g.quien)+(x.x?'<span class="px">PEQUEÑO PROBLEMA</span>':'')+'</b>'+esc(x.e)+'</div>';
  o+='<div class="dl c"><b class="who">Candidato</b>'+x.c+'</div>';
 });
 return o+'</div>';
}

/* ---------------- ejercicio: que respondes ---------------- */
var QZ=null;
function newQuiz(){
 var items=shuffle(D.quiz.slice()).slice(0,8).map(function(q){ var ord=shuffle([0,1,2]); return {q:q, ord:ord}; });
 QZ={items:items, k:0, ok:0, answered:false};
 renderQuiz();
}
function renderQuiz(){
 var q=QZ, box=$('quiz');
 if(q.k>=q.items.length){
  var n=q.items.length, ok=q.ok;
  if(S.qz.best===null || ok>S.qz.best) S.qz.best=ok; S.qz.last=ok; save(); nav();
  box.innerHTML='<div class="quiz"><div class="qn">RESULTADO</div><div class="score">'+ok+' / '+n+'</div><p>'+(ok>=7?'¡Muy bien! Sabes cómo seguir la conversación.':(ok>=5?'Bien. Recuerda: responde, añade algo y pregunta o propón.':'Vuelve a mirar las cuatro tarjetas de frases y prueba otra vez.'))+'</p>'+
   (S.qz.best!==null?'<p class="small muted">Tu mejor resultado: '+S.qz.best+' / '+n+'</p>':'')+'<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="qnew">Otras ocho frases</button></div></div>';
  return;
 }
 var it=q.items[q.k];
 var o='<div class="quiz"><div class="qn">FRASE '+(q.k+1)+' DE '+q.items.length+'</div><p class="qs">'+esc(it.q.ctx)+'. El examinador dice:</p><div class="qe">«'+esc(it.q.e)+'»</div><div role="group" aria-label="Respuestas">';
 it.ord.forEach(function(i){ o+='<button type="button" class="qop" data-act="qpick" data-i="'+i+'">'+esc(it.q.ops[i])+'</button>'; });
 o+='</div><div id="qfb"></div><div class="row" style="margin-bottom:0" id="qnext" hidden><button class="btn cta" data-act="qnext">'+(q.k===q.items.length-1?'Ver el resultado':'Siguiente frase')+'</button></div></div>';
 box.innerHTML=o;
}
function pickQuiz(b){
 var q=QZ, it=q.items[q.k]; if(q.answered) return;
 var i=+b.getAttribute('data-i'), ok = i===it.q.ok;
 if(ok) q.ok++; q.answered=true;
 [].forEach.call(document.querySelectorAll('#quiz .qop'), function(x){ x.disabled=true; var j=+x.getAttribute('data-i'); if(j===it.q.ok) x.classList.add('ok'); else if(j===i) x.classList.add('bad'); });
 $('qfb').innerHTML='<div class="fb '+(ok?'ok':'bad')+'"><b>'+(ok?'¡Correcto!':'Mejor la otra respuesta.')+'</b> '+esc(it.q.por)+'</div>';
 $('qnext').hidden=false;
}

/* ---------------- esquema del dialogo ---------------- */
var FW={'el':1,'la':1,'los':1,'las':1,'un':1,'una':1,'que':1,'es':1,'muy':1,'porque':1,'y':1,'de':1,'en':1,'con':1,'me':1,'mi':1,'te':1,'para':1};
function wordsOf(t){ return String(t||'').toLowerCase().match(/[a-záéíóúüñ0-9]+/g)||[]; }
function tooLong(t){ var w=wordsOf(t), n=0; w.forEach(function(x){ if(FW[x]) n++; }); return n>=6 || w.length>24; }
function hasNote(i){ return !!(R.notes && R.useNotes && i!==null && wordsOf(R.notes[i]).length); }
function ehead(g,i){ return '<div class="eh"><span class="en">'+(i+1)+'</span><span class="px">'+esc(g.pa[i])+'</span></div>'; }
function bhead(){ return '<div class="eh"><span class="en b">B</span><span class="px">Si dice que no: mi segunda opción</span></div>'; }
function esqBlank(){
 var o='<div class="esq blank"><div class="eb tr end"><b>TÚ / USTED:</b> <span class="muted">______</span> &nbsp; <b>Con:</b> <span class="muted">____________</span></div>';
 for(var i=0;i<5;i++) o+='<div class="eb"><div class="eh"><span class="en">'+(i+1)+'</span><span class="px">Mi idea · ¿mi pregunta?</span></div></div>';
 return o+'<div class="eb end"><div class="eh"><span class="en b">B</span><span class="px">Si dice que no: ¿Y si...?</span></div></div><div class="eb end"><b>Al final:</b> <span class="muted">día · hora · lugar (o qué compro y cuánto pago)</span></div></div>';
}
function esqStatic(g, notes){
 var o='<div class="esq"><div class="eb tr end"><b>'+(g.tr==='tu'?'TÚ':'USTED')+'</b> · '+esc(g.quien)+'</div>';
 for(var i=0;i<g.pa.length;i++){ var x=String(notes[i]||'').trim(); o+='<div class="eb">'+ehead(g,i)+'<div class="enote">'+(wordsOf(x).length?esc(x):'<span class="muted">(vacía)</span>')+'</div></div>'; }
 var b=String(notes[g.pa.length]||'').trim();
 return o+'<div class="eb end">'+bhead()+'<div class="enote">'+(wordsOf(b).length?esc(b):'<span class="muted">(vacía)</span>')+'</div></div></div>';
}
function modelNotes(g){ return g.notas.concat([g.planb]); }
function esqEdit(g, notes){
 var o='<div class="esq"><div class="eb tr end"><b>'+(g.tr==='tu'?'TÚ':'USTED')+'</b> · '+esc(g.quien)+'</div>';
 for(var i=0;i<=g.pa.length;i++){
  var last=i===g.pa.length;
  o+='<div class="eb'+(tooLong(notes[i])?' many':'')+(last?' end':'')+'">'+(last?bhead():ehead(g,i))+'<textarea data-ni="'+i+'" rows="2" placeholder="'+(last?'Otro día, otro sitio, otro precio...':'Palabras clave · ¿una pregunta?')+'" aria-label="'+(last?'Segunda opción':'Notas de la pauta '+(i+1))+'">'+esc(notes[i]||'')+'</textarea><div class="wn">¿Estás escribiendo frases? Mejor solo palabras clave.</div></div>';
 }
 return o+'</div>';
}
function renderPrep(){
 $('esq-blank').innerHTML=esqBlank(); $('esq-sheet').innerHTML=esqBlank();
 var g=G(D.ej); if(g) $('esq-ej').innerHTML=esqStatic(g, modelNotes(g));
}

/* ---------------- practica: elegir ---------------- */
function lastTime(id){ var h=S.h[id]; return h&&h.length ? h[h.length-1] : null; }
function card(g){
 var l=lastTime(g.id);
 return '<button type="button" class="card" data-act="pick" data-id="'+g.id+'"><span class="ci">'+g.id+'</span><span><b>'+esc(g.n)+'</b><span class="s">'+(g.tr==='tu'?'Tú':'Usted')+' · '+esc(g.quien)+' · '+(l?'Última vez: '+mmss(l.s)+(l.m==='guiado'?' (guiado)':' (examen)'):'Sin practicar')+'</span></span></button>';
}
function showPick(){
 var o='<h2>Practica un diálogo</h2><p class="lead">En el examen eliges una de las dos fotos y la tarea 3 es la que va con esa foto. Puedes practicar así o elegir directamente una situación.</p>';
 o+='<div class="row"><button class="btn cta" data-act="duo">Como en el examen: dos opciones al azar</button></div>';
 [['plan','Planificar con un amigo, un familiar o un compañero (tú)','Lo que más sale en las láminas del examen.'],
  ['serv','Situaciones de servicio (usted)','Tienda, farmacia, estación, restaurante, oficina.']].forEach(function(gr){
  var gs=D.dl.filter(function(g){ return g.tipo===gr[0]; }); if(!gs.length) return;
  o+='<h3 class="grp">'+gr[1]+'</h3><p class="small muted" style="margin:0">'+gr[2]+'</p><div class="grid">'+gs.map(card).join('')+'</div>';
 });
 $('pr').innerHTML=o;
}
function showDuo(){
 var pl=shuffle(D.dl.filter(function(g){ return g.tipo==='plan'; }).map(function(g){ return g.id; }));
 var all=shuffle(D.dl.map(function(g){ return g.id; }).filter(function(id){ return id!==pl[0]; }));
 S.duo=shuffle([pl[0], all[0]]); save();
 var o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="back">← Todas las situaciones</button><button class="btn sm" data-act="duo">Otras dos</button></div>';
 o+='<h2>Elige una de las dos opciones</h2><p class="lead">En el examen eliges por la foto, pero mira también la situación de abajo: elige la opción en la que tienes más que decir.</p><div class="duo">';
 S.duo.forEach(function(id,k){ var g=G(id); o+='<div>'+lamina(g,{opc:k+1, attr:' data-act="pick" data-id="'+id+'" role="button" tabindex="0"'})+'<div class="pick"><button class="btn sm cta" data-act="pick" data-id="'+id+'">Elijo esta</button></div></div>'; });
 $('pr').innerHTML=o+'</div>';
}
function showSetup(){
 var g=G(S.dl); if(!g){ showPick(); return; }
 var O=S.o, o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="back">← Otras situaciones</button></div>';
 o+='<div class="run"><div>'+lamina(g,{tags:true})+'</div><div>';
 o+='<h3>¿Cómo quieres practicar?</h3><div class="modes">'+
  '<label class="mode"><input type="radio" name="md" value="guiado"'+(O.mode==='guiado'?' checked':'')+'><b>Modo guiado</b><p>Cada frase del examinador en pantalla, con tiempo para responder y ayudas.</p></label>'+
  '<label class="mode"><input type="radio" name="md" value="libre"'+(O.mode==='libre'?' checked':'')+'><b>Modo examen</b><p>Las frases del examinador, la lámina y el reloj. Sin ayudas.</p></label></div>';
 o+='<div class="opts">';
 o+='<label><span style="flex:1">Preparación <select id="prepsel">'+[['notas','2 minutos con notas (como en el examen)'],['leer','30 segundos leyendo la lámina'],['no','Sin preparación']].map(function(r){ return '<option value="'+r[0]+'"'+(O.prep===r[0]?' selected':'')+'>'+r[1]+'</option>'; }).join('')+'</select><small>Con notas rellenas el esquema (ideas y preguntas) y después lo tienes a la vista mientras hablas, como tu hoja en el examen.</small></span></label>';
 if(O.mode==='guiado'){
  o+='<label><span style="flex:1">Tiempo para cada respuesta <select id="ritmo">'+[[15,'15 segundos'],[20,'20 segundos'],[25,'25 segundos (con calma)']].map(function(r){ return '<option value="'+r[0]+'"'+(O.ritmo===r[0]?' selected':'')+'>'+r[1]+'</option>'; }).join('')+'</select><small>Empieza con 20 segundos: es lo que dura una respuesta con tres cosas (respondo, añado, pregunto).</small></span></label>';
  o+='<label><input type="checkbox" data-o="modelo"'+(O.modelo?' checked':'')+'><span>Con las respuestas modelo en la pantalla<small>Léelas en voz alta para sentir el ritmo del diálogo. Después, inténtalo con tus palabras.</small></span></label>';
  o+='<label><input type="checkbox" data-o="beep"'+(O.beep?' checked':'')+'><span>Sonido al cambiar de turno</span></label>';
 }
 o+='<label><input type="checkbox" data-o="rec"'+(O.rec?' checked':'')+'><span>Grabarme (opcional)<small>La grabación se queda en tu ordenador o tu móvil: no se envía a ningún sitio y se borra al cerrar la página (al final puedes guardarla en Descargas). El navegador te pedirá permiso para usar el micrófono; mientras grabas, la barrita verde se mueve cuando hablas.</small></span></label>';
 o+='</div><div class="tip">Lee en voz alta la frase del examinador (o pide a alguien que haga de examinador y la lea) y después responde tú.</div><div class="row"><button class="btn cta" data-act="start">Empezar</button></div>';
 o+='<details><summary>Ver las notas modelo</summary><p class="small muted">Mejor después de preparar tus notas.</p>'+esqStatic(g,modelNotes(g))+'</details>';
 o+='<details><summary>Ver el diálogo modelo</summary><p class="small muted">Mejor después de practicar: primero inténtalo tú.</p>'+dialogHTML(g)+'</details>';
 o+='<details><summary>Para quien hace de examinador</summary><p class="small">Lee las frases del examinador una a una, con naturalidad. Si el candidato contesta poco, pregunta «¿Y por qué?» o «¿Y tú qué prefieres?». El pequeño problema: '+esc(g.prob)+'</p></details>';
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
 if(REC.url) return '<h4>Escúchate</h4><audio controls src="'+REC.url+'"></audio><div class="row" style="margin:6px 0"><a class="btn sm" href="'+REC.url+'" download="mi_dialogo_'+S.dl+'.'+REC.ext+'">Guardar el audio en mi dispositivo</a><button class="btn sm" data-act="delrec">Borrar la grabación</button></div>'+
  '<p class="small muted">La grabación no se guarda sola: está en esta página hasta que la cierras o haces otra. Si quieres conservarla, pulsa «Guardar el audio en mi dispositivo» y la tendrás en tu carpeta de Descargas.</p><p class="small muted">Al escucharte, fíjate: ¿contestas solo «sí» o «vale», o añades algo y preguntas? ¿Usas siempre tú (o siempre usted)? ¿Qué haces cuando hay un problema?</p>';
 if(REC.mr) return '<p class="small muted">Preparando la grabación...</p>';
 if(REC.err) return '<div class="warnbox">'+REC.err+'</div>';
 if(REC.used) return '<p class="small muted">No hay grabación.</p>';
 return '';
}

/* ---------------- practica: estado ---------------- */
var R={active:false, mode:'', phase:0, phases:[], t0:0, acc:0, paused:false, timer:null, spoken:0, warned:false, ti:0, done:{}};
function now(){ return (window.performance&&performance.now)?performance.now():Date.now(); }
function elapsed(){ return R.acc + (R.paused?0:(now()-R.t0)/1000); }
function curG(){ return G(S.dl); }
function startRun(){
 var g=curG(); if(!g) return;
 try{ if(!AC){ var C=window.AudioContext||window.webkitAudioContext; if(C) AC=new C(); } if(AC && AC.resume) AC.resume(); }catch(e){}
 $('pr').innerHTML='<p class="muted">Un momento...</p>';
 recPrepare(function(){
  R.active=true; R.mode=S.o.mode; R.paused=false; R.warned=false; R.spoken=0; R.ti=0; R.done={};
  R.phases=[]; R.useNotes = S.o.prep==='notas'; R.notes=[]; for(var n=0;n<=g.pa.length;n++) R.notes.push('');
  if(S.o.prep==='leer') R.phases.push({k:'leer', d:30});
  if(S.o.prep==='notas') R.phases.push({k:'notas', d:120});
  if(R.mode==='guiado'){
   g.tu.forEach(function(x,i){
    var d=S.o.ritmo; if(x.k) d=Math.round(d*0.75);
    if(S.o.modelo) d=Math.max(d, Math.round(x.wc/2)+3);
    R.phases.push({k:'t', i:i, d:d});
   });
  } else R.phases.push({k:'libre'});
  R.phase=0; wake(true); renderRun(); enterPhase(0);
  R.timer=setInterval(tick, 200);
 });
}
function enterPhase(n){
 R.phase=n; R.acc=0; R.t0=now(); R.paused=false;
 var ph=R.phases[n];
 document.body.classList.toggle('notas', ph.k==='notas');
 if(ph.k==='t' || ph.k==='libre') recStart();
 if(ph.k==='t' && n>0 && R.phases[n-1].k==='t') beep();
 if(ph.k==='libre') R.ti=0;
 renderSide(); renderPhase(); tick();
}
function curTurn(){ var ph=R.phases[R.phase], g=curG(); if(ph.k==='t') return g.tu[ph.i]; if(ph.k==='libre') return g.tu[R.ti]; return null; }
function renderRun(){
 document.body.classList.add('focus');
 $('pr').innerHTML='<div class="run"><div class="side"><div id="side"></div><div class="mini" aria-hidden="true"><span id="minil"></span><b id="minic"></b></div></div><div><div class="pan" id="pan" aria-live="polite"></div>'+
  '<div class="warnbox" id="micw" hidden><b>No llega sonido del micrófono.</b> Revisa que el navegador tiene permiso para usarlo (en el Mac: Ajustes del Sistema &gt; Privacidad y seguridad &gt; Micrófono) y que no está silenciado. Puedes seguir practicando sin grabación.</div>'+
  '<div class="row"><button class="btn" data-act="pause" id="bpause">Pausa</button><button class="btn" data-act="stop">Parar</button></div></div></div>';
}
function renderSide(){
 var ph=R.phases[R.phase], g=curG(), x=curTurn();
 var cur = (ph.k==='t' && x) ? x.p : null;
 $('side').innerHTML=lamina(g,{tags:true, sm:true, cur:cur, done:ph.k==='t'?R.done:null});
}
function phrases(g, x){
 var ks=x.f.length ? x.f.slice() : ['q'];
 if(x.x && ks.indexOf('r')<0) ks.push('r');
 var o='';
 if(x.k==='s') o+='<div><b>Para empezar:</b> <i>'+esc(D.sal[g.tipo].join(' · '))+'</i></div>';
 ks.forEach(function(k){ o+='<div><b>'+esc(D.fn[k].n)+':</b> <i>'+esc(D.fn[k][g.tipo].slice(0,3).join(' · '))+'</i></div>'; });
 if(x.k==='d') o+='<div><b>Para terminar:</b> <i>'+esc(D.des[g.tipo].join(' · '))+'</i></div>';
 return '<div class="forms">'+o+'</div>';
}
function exq(g, x){
 return (x.x?'<div class="probl"><b>Pequeño problema:</b> el examinador no dice que sí. Reacciona y busca otra solución.</div>':'')+
  '<div class="exq"><b>'+esc(g.quien)+' (examinador)</b>'+esc(x.e)+'</div>';
}
function renderPhase(){
 var g=curG(), ph=R.phases[R.phase], o='';
 var recd = (REC.stream && (ph.k==='t'||ph.k==='libre')) ? ' <span class="recdot">Grabando</span><span class="lvl" title="Nivel del micrófono"><i id="lvl"></i></span>' : '';
 if(ph.k==='leer'){
  o='<div class="kk">PREPARACIÓN</div><h3>Lee la situación en silencio</h3><div class="clock" id="clk">0:30</div><div class="bar"><i id="br"></i></div>'+
   '<p>¿Hablas de tú o de usted? Para cada pauta, piensa una idea y una pregunta. ¿Qué haces si te dice que no?</p><div class="row"><button class="btn cta" data-act="skip">Ya estoy listo</button></div>';
 } else if(ph.k==='notas'){
  o='<div class="kk">PREPARACIÓN · TUS NOTAS</div><h3>Rellena el esquema: ideas y preguntas</h3><div class="clock" id="clk">2:00</div><div class="bar"><i id="br"></i></div>'+esqEdit(g, R.notes)+
   (S.n[S.dl]?'<div class="row" style="margin:6px 0"><button class="btn sm" data-act="oldnotes">Usar mis notas de la otra vez</button></div>':'')+
   '<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="skip">Ya he terminado: a hablar</button></div>';
 } else if(ph.k==='t'){
  var x=g.tu[ph.i], dots='', E=D.esc[x.x?'x':(x.k||'base')];
  for(var d=0; d<g.tu.length; d++) dots+='<i class="'+(d<ph.i?'d':(d===ph.i?'c':''))+'"></i>';
  o='<div class="kk">TURNO '+(ph.i+1)+' DE '+g.tu.length+(x.p!==null?' · PAUTA '+(x.p+1):'')+recd+'</div><div class="dots" aria-hidden="true">'+dots+'</div>'+exq(g,x)+
   '<div class="clock" id="clk"></div><div class="bar"><i id="br"></i></div>';
  if(S.o.modelo){
   o+='<div class="modtxt"><b class="small muted">CANDIDATO</b><br>'+x.c+'</div>';
  } else {
   o+='<ul class="esc">'+E.map(function(e,k){ return '<li id="es'+k+'">'+(k+1)+'. '+esc(e)+'</li>'; }).join('')+'</ul>';
   if(hasNote(x.p)) o+='<div class="myn"><b>TUS NOTAS</b>'+esc(String(R.notes[x.p]).trim())+'</div>';
   if(x.x && hasNote(g.pa.length)) o+='<div class="myn"><b>TU SEGUNDA OPCIÓN</b>'+esc(String(R.notes[g.pa.length]).trim())+'</div>';
   o+=phrases(g,x);
  }
  o+='<div class="row" style="margin-bottom:0"><button class="btn cta" data-act="next" id="bnext" disabled>Siguiente</button></div>';
 } else {
  var y=g.tu[R.ti], last=R.ti===g.tu.length-1;
  o='<div class="kk">MODO EXAMEN'+recd+'</div><h3>Habla con el examinador entre 3 y 4 minutos</h3><div class="clock" id="clk">0:00</div><p class="small" id="clmsg"></p>'+
   exq(g,y)+'<div class="row" style="margin:8px 0">'+(last?'<button class="btn cta" data-act="finish">Terminar</button>':'<button class="btn cta" data-act="enext">Siguiente frase del examinador</button>')+'</div>'+
   '<p class="small muted">'+(R.useNotes?'Tus notas, en orden. Míralas, pero no las leas. ':'')+'Marca cada pauta cuando ya habéis hablado de ella:</p><ul class="chk">'+
   g.pa.map(function(p,k){ return '<li><label><input type="checkbox"'+(R.done[k]?' checked':'')+' data-dn="'+k+'"><span>'+(k+1)+'. '+esc(p)+(hasNote(k)?'<span class="lq-n">'+esc(String(R.notes[k]).trim())+'</span>':'')+'</span></label></li>'; }).join('')+'</ul>'+
   (last?'':'<div class="row" style="margin-bottom:0"><button class="btn" data-act="finish">Terminar ya</button></div>')+
   '<div class="warnbox" id="warn" hidden><b id="warnt"></b> En el examen, el diálogo dura entre 3 y 4 minutos. ¿Has añadido detalles y has hecho preguntas en cada turno?<div class="row" style="margin:8px 0 0"><button class="btn sm cta" data-act="goon">Sigo hablando</button><button class="btn sm" data-act="finish2">Terminar igualmente</button></div></div>';
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
  clk.className='clock'+(e>=240?' red':(e>=180?' green':''));
  var m=$('clmsg'); if(m) m.textContent = e<180 ? 'Todavía no has llegado a 3 minutos: responde, añade algo y pregunta.' : (e<240 ? '¡Bien! Ya estás entre 3 y 4 minutos.' : (e<270 ? 'Ya has pasado de 4 minutos: cierra el plan y despídete.' : 'En el examen, el examinador terminaría aquí.'));
 } else {
  var rem=ph.d-e, fr=Math.min(1,e/ph.d);
  clk.textContent=mmss(Math.ceil(rem)); clk.className='clock'+(rem<=5?' red':'');
  var br=$('br'); if(br) br.style.width=(fr*100)+'%';
  if(ph.k==='t'){
   for(var k=0;k<3;k++){ var li=$('es'+k); if(li) li.classList.toggle('on', fr>=k/3); }
   var bn=$('bnext'); if(bn){ var ready=fr>=2/3; bn.disabled=!ready; bn.textContent = ready ? (R.phase===R.phases.length-1?'Terminar':'Siguiente turno') : 'Siguiente (en '+Math.ceil(ph.d*2/3-e)+' s)'; }
  }
 }
 var ml=$('minil'), mc=$('minic'); if(ml&&mc){ ml.textContent=(ph.k==='t'?'Turno '+(ph.i+1)+'/'+curG().tu.length:(ph.k==='libre'?'Modo examen':'Preparación')); mc.textContent=clk.textContent; mc.style.color=clk.className.indexOf('red')>=0?'#FF9C85':(clk.className.indexOf('green')>=0?'#8FE3AE':''); }
 if(ph.k!=='libre' && ph.d-e<=0) advance();
}
function advance(){
 var ph=R.phases[R.phase];
 if(ph.k==='t'){ R.spoken+=Math.min(elapsed(), ph.d); var x=curG().tu[ph.i]; if(x.p!==null) R.done[x.p]=true; }
 if(ph.k==='notas'){ S.n[S.dl]=R.notes.slice(); save(); window.scrollTo(0,0); }
 if(R.phase<R.phases.length-1) enterPhase(R.phase+1); else finish();
}
function examNext(){ var g=curG(); if(R.ti<g.tu.length-1){ R.ti++; renderPhase(); tick(); } }
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
 var g=curG(), secs, mine=null;
 if(R.mode==='libre') secs=elapsed();
 else { mine=R.spoken; secs=R.spoken + g.we/(D.wpm/60) + g.tu.length*D.pausa; }
 document.body.classList.remove('focus','notas');
 if(R.timer) clearInterval(R.timer); R.timer=null; R.active=false; wake(false); recStop(); beep();
 var h=S.h[S.dl]||[]; h.push({s:Math.round(secs), m:R.mode, d:new Date().toISOString().slice(0,10)}); S.h[S.dl]=h.slice(-10); save(); nav();
 showDone(secs, mine);
}
function showDone(secs, mine){
 var g=curG(), v, cl;
 if(secs<120){ cl='bad'; v='Muy corto. En cada turno, responde, añade un detalle o un porqué y pregunta o propón algo. Prueba el modo guiado.'; }
 else if(secs<180){ cl='amb'; v='Casi. Te falta un poco para llegar a 3 minutos: pregunta más («¿Y tú qué prefieres?») y da razones («porque...»).'; }
 else if(secs<=240){ cl='ok'; v='¡Perfecto! Entre 3 y 4 minutos, como en el examen.'; }
 else { cl='amb'; v='Un poco largo. No pasa nada, pero en el examen el examinador termina cuando habéis hablado de todas las pautas: llega al plan final antes.'; }
 var pos=Math.min(100, secs/300*100);
 var h=(S.h[S.dl]||[]).slice(-6).reverse();
 var o='<div class="row noprint" style="margin-top:0"><button class="btn sm" data-act="back">← Otras situaciones</button></div>';
 o+='<div class="run"><div class="side">'+lamina(g,{tags:true})+'</div><div><div class="res"><div class="kk muted small">'+(R.mode==='guiado'?'MODO GUIADO':'MODO EXAMEN')+'</div><div class="big">'+mmss(secs)+'</div>'+
  (mine!==null?'<p class="small muted" style="margin:4px 0 0">Tú has hablado unos '+mmss(mine)+'; con las frases del examinador, el diálogo dura unos '+mmss(secs)+'.</p>':'')+
  '<div class="zone" aria-hidden="true"><div class="ok"></div><div class="me" style="left:calc('+pos+'% - 2px)"></div><span style="left:0;transform:none">0</span><span style="left:20%">1 min</span><span style="left:40%">2 min</span><span style="left:60%">3 min</span><span style="left:80%">4 min</span></div>'+
  '<div class="verd '+cl+'">'+v+'</div>';
 if(h.length>1){ o+='<p class="small" style="margin:8px 0 0"><b>Tus tiempos con esta situación:</b></p><ul class="hist">'+h.map(function(x){ return '<li>'+x.d.split('-').reverse().join('/')+' · '+mmss(x.s)+' ('+(x.m==='guiado'?'guiado':'examen')+')</li>'; }).join('')+'</ul>'; }
 o+='</div><div id="recout">'+recBlock()+'</div>';
 o+='<h4>Revísate</h4><ul class="chk">'+['He saludado y he dicho de qué quería hablar o qué necesitaba.','He usado siempre '+(g.tr==='tu'?'tú':'usted')+', del saludo a la despedida.','He hablado de todas las pautas.','No he contestado solo «sí», «no» o «vale»: he añadido un detalle o un porqué.','He hecho al menos tres preguntas al examinador.','Cuando ha dicho que no, he propuesto otra solución.','He terminado con el plan claro y me he despedido.'].map(function(x){ return '<li><label><input type="checkbox"><span>'+x+'</span></label></li>'; }).join('')+'</ul>';
 o+='<details open><summary>El diálogo modelo</summary>'+dialogHTML(g)+'</details>';
 o+='<div class="row"><button class="btn cta" data-act="again">Otra vez con esta situación</button><button class="btn" data-act="back">Otra situación</button><button class="btn" data-go="opinion">Tu opinión</button></div></div></div>';
 if(R.useNotes){ o+='<h3 style="margin-top:24px">Tus notas y las notas modelo</h3><p class="small muted">Compara: ¿tienes algo en cada casilla? ¿Hay una pregunta en casi todas? ¿Tenías una segunda opción? ¿Son palabras clave o frases?</p><div class="cmp"><div><h4>Tus notas</h4>'+esqStatic(g,R.notes)+'</div><div><h4>Notas modelo</h4>'+esqStatic(g,modelNotes(g))+'</div></div>'; }
 else { o+='<details><summary>Ver las notas modelo de esta situación</summary>'+esqStatic(g,modelNotes(g))+'</details>'; }
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
 var L=['CURSO DELE A2 - ORAL TAREA 3: HABLA CON EL EXAMINADOR', 'Nombre: '+(S.name||'-'), '', 'Ejercicio "Que respondes": '+(S.qz.best===null?'sin hacer':'mejor resultado '+S.qz.best+'/8'), '', 'Mis tiempos:'];
 var any=false;
 D.dl.forEach(function(g){ var h=S.h[g.id]; if(h&&h.length){ any=true; L.push('  Situacion '+g.id+' ('+g.n+'): '+h.map(function(x){ return mmss(x.s)+' '+(x.m==='guiado'?'guiado':'examen'); }).join(' > ')); } });
 if(!any) L.push('  (todavia no he practicado)');
 L.push('', '1. El modo guiado me ha ayudado: '+(S.o1||'-'), '2. El esquema de ideas y preguntas me ha servido: '+(S.o5||'-'), '3. Lo que me cuesta mas: '+(S.o3||'-'), '4. Al escucharme / falta: '+(S.o2||'-'), '5. Sensacion de control (1-10): '+(S.o4||'-'));
 return L.join('\n');
}

/* ---------------- eventos ---------------- */
var ACTS={
 pick:function(b){ S.dl=+b.getAttribute('data-id'); save(); showSetup(); window.scrollTo(0,0); },
 duo:function(){ showDuo(); window.scrollTo(0,0); },
 back:function(){ if(R.active) stopRun(true); showPick(); window.scrollTo(0,0); },
 start:function(){ startRun(); window.scrollTo(0,0); },
 skip:function(){ advance(); },
 next:function(b){ if(!b.disabled) advance(); },
 enext:function(){ examNext(); },
 pause:function(){ togglePause(); },
 stop:function(){ stopRun(false); },
 finish:function(){ var e=elapsed(); if(e<180 && !R.warned){ R.warned=true; $('warnt').textContent='Solo llevas '+mmss(e)+'.'; $('warn').hidden=false; return; } finish(); },
 finish2:function(){ finish(); },
 goon:function(){ $('warn').hidden=true; },
 again:function(){ showSetup(); window.scrollTo(0,0); },
 delrec:function(){ recClear(); var a=$('recout'); if(a) a.innerHTML=''; },
 qnew:function(){ newQuiz(); },
 qpick:function(b){ pickQuiz(b); },
 qnext:function(){ QZ.k++; QZ.answered=false; renderQuiz(); },
 oldnotes:function(){ if(S.n[S.dl]){ R.notes=S.n[S.dl].slice(); while(R.notes.length<=curG().pa.length) R.notes.push(''); renderPhase(); tick(); } },
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
 if(t.getAttribute && t.getAttribute('data-dn')!==null){ R.done[+t.getAttribute('data-dn')]=t.checked; return; }
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
if(start==='practica' && S.dl) showSetup();
})();
"""

js = JS.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(FILE, "w", encoding="ascii").write(page(TITLE + " · Preparación DELE A2", CSS_T3, body, js))
print("ok", FILE, "·", len(B.DIALOGOS), "situaciones ·", ", ".join("%d: %s min" % (d["id"], str(d["min"]).replace(".", ",")) for d in DIAL_JS))
for a in AVISOS: print("  AVISO", a)
