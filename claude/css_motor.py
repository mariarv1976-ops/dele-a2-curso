# -*- coding: utf-8 -*-
# Copia exacta del CSS de DELE_A2_motor_simulacro.py (el que el motor le pasa a la libreta como base_css).
# Solo para generar libretas sin el motor (libreta_desde_extracto.py).
CSS = r"""
:root{--paper:#FBF9F6;--ink:#14161C;--coral:#E8603C;--coral-soft:#FCE9E1;--cta:#FF6B45;
--line:#E6DFD6;--muted:#5E5A55;--ok:#2F7D4F;--ok-soft:#E3F1E8;--amb:#B7791F;--amb-soft:#FBF0DA;
--bad:#B3261E;--bad-soft:#F8E1DE;--card:#FFFFFF}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink)}
body{font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:17px;line-height:1.6}
h1,h2,h3{font-family:Georgia,"Times New Roman",serif;font-weight:700;line-height:1.25;margin:0 0 .5em}
h1{font-size:1.9rem}h2{font-size:1.45rem}h3{font-size:1.15rem}
.wrap{max-width:820px;margin:0 auto;padding:0 20px 80px}
header.top{border-bottom:3px solid var(--coral);background:var(--card);position:sticky;top:0;z-index:10}
.top-in{max-width:820px;margin:0 auto;padding:14px 20px 0}
.brand{display:flex;justify-content:space-between;align-items:center;gap:12px}.brand>div:first-child{min-width:0}
.brand small{display:block;color:var(--muted);font-size:.85rem}
.timer{font-variant-numeric:tabular-nums;border:2px solid var(--ink);border-radius:999px;padding:4px 14px;font-weight:700;font-size:1rem;white-space:nowrap}
.timer.low{border-color:var(--bad);color:var(--bad)}
.timer[hidden]{display:none}
nav.steps{display:flex;gap:0;overflow-x:auto;margin-top:12px;padding-bottom:0}
nav.steps button{flex:0 0 auto;border:0;background:none;padding:8px 9px 10px;font:inherit;font-size:.92rem;color:var(--muted);cursor:pointer;border-bottom:4px solid transparent;display:flex;align-items:center;gap:6px}
nav.steps button .n{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;border:1.5px solid currentColor;font-size:.75rem;font-weight:700}
nav.steps button.on{color:var(--ink);border-bottom-color:var(--coral);font-weight:600}
nav.steps button.done .n{background:var(--ok);border-color:var(--ok);color:#fff}
nav.steps button.locked{opacity:.55}
nav.steps button:focus-visible,button:focus-visible,textarea:focus-visible,input:focus-visible{outline:3px solid var(--cta);outline-offset:2px}
section.view{display:none;padding-top:28px}
section.view.on{display:block}
.lead{font-size:1.05rem;color:var(--muted);max-width:62ch}
.instr{border-left:5px solid var(--ink);background:var(--card);padding:14px 18px;margin:18px 0;border-radius:0 8px 8px 0}
.instr b{display:block;font-family:Georgia,serif;margin-bottom:4px}
.tip{background:var(--coral-soft);border-radius:8px;padding:10px 14px;font-size:.95rem;margin:12px 0}
.paper{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:22px 26px;margin:16px 0;font-family:Georgia,serif;font-size:1.02rem;line-height:1.7}
.paper .mailhead{font-family:system-ui,sans-serif;font-size:.9rem;color:var(--muted);border-bottom:1px solid var(--line);padding-bottom:8px;margin-bottom:12px}
.paper p{margin:0 0 .9em}
.ad{background:var(--card);border:2px solid var(--ink);border-radius:4px;padding:16px 20px;margin:22px 0 12px}
.ad h4{margin:0 0 6px;font-family:Georgia,serif;font-size:1.05rem}
.ad .lbl{font-size:.8rem;color:var(--muted);font-weight:600;margin-bottom:6px}
.q{margin:14px 0 22px}
.q .qt{font-weight:600;margin-bottom:8px}
.q .qt .num{display:inline-block;min-width:2em;color:var(--coral);font-family:Georgia,serif}
.opt{display:flex;align-items:flex-start;gap:12px;padding:8px 10px;border-radius:8px;cursor:pointer;border:1px solid transparent}
.opt:hover{background:#F4EFE9}
.opt input{position:absolute;opacity:0;width:1px;height:1px}
.bub{flex:0 0 30px;width:30px;height:30px;border-radius:50%;border:2px solid var(--ink);display:grid;place-items:center;font-weight:700;font-size:.9rem;background:#fff}
.opt input:checked + .bub,.pic input:checked + .bub{background:var(--ink);color:#fff}
.pic:has(input:checked) .plbl{outline:2px solid var(--ink)}
.opt input:focus-visible + .bub{outline:3px solid var(--cta);outline-offset:2px}
.locked-q .opt{cursor:default}
.locked-q .opt:hover{background:none}
.pics{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.pic{border:2px solid var(--line);border-radius:10px;padding:10px;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;background:#fff;position:relative}
.pic input{position:absolute;opacity:0}
.pic .ph{width:100%;aspect-ratio:16/9;border-radius:6px;background:#F1ECE6;display:grid;place-items:center;font-size:.92rem;color:var(--ink);padding:6px}
.pic img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:6px}
.pic:has(input:checked){border-color:var(--ink);box-shadow:0 0 0 2px var(--ink)}
.pic:has(input:focus-visible){outline:3px solid var(--cta);outline-offset:2px}
.example{border:1px dashed var(--muted);border-radius:10px;padding:12px 16px;margin:14px 0;background:#FFFDFB}
.example .ex-ok{color:var(--ok);font-weight:600;margin-top:6px}
.btn{font:inherit;font-weight:600;border-radius:999px;padding:10px 22px;cursor:pointer;border:2px solid var(--ink);background:#fff;color:var(--ink)}
.btn.cta{background:var(--cta);border-color:var(--cta);color:#fff}
.btn:disabled{opacity:.5;cursor:not-allowed}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:18px 0}
.done-note{background:var(--ok-soft);border-radius:8px;padding:10px 14px;margin:16px 0}
.warn{background:var(--amb-soft);border-radius:8px;padding:10px 14px;margin:16px 0}
audio{width:100%;margin:10px 0}
.audio-miss{font-size:.9rem;color:var(--bad);background:var(--bad-soft);border-radius:8px;padding:10px 14px;margin:8px 0}
.audio-miss .btn{display:block;margin-top:8px}
textarea,input[type=text]{width:100%;font:inherit;border:1.5px solid #CFC6BB;border-radius:8px;padding:10px 12px;background:#fff;color:var(--ink)}
textarea{min-height:190px;line-height:1.6;resize:vertical}
.wc{font-size:.9rem;margin-top:4px}
.wc.good{color:var(--ok)}.wc.bad{color:var(--amb)}
.vocab-row{display:grid;grid-template-columns:1fr 2fr auto;gap:8px;margin-bottom:8px}
.vocab-row button{border:0;background:none;cursor:pointer;color:var(--muted);font-size:1.3rem}
.pautas{margin:8px 0 8px 0;padding-left:1.2em}
.checks label{display:flex;gap:10px;align-items:flex-start;margin:6px 0;cursor:pointer}
.checks input{margin-top:6px;accent-color:var(--ink)}
.choice{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0}
.choice label{border:2px solid var(--line);border-radius:999px;padding:6px 16px;cursor:pointer;background:#fff}
.choice label:has(input:checked){border-color:var(--ink);background:var(--ink);color:#fff}
.choice input{position:absolute;opacity:0}
.photo{background:#F1ECE6;border-radius:8px;padding:12px 14px;font-size:.95rem;margin:8px 0}
.ficha{background:#fff;border:1px solid var(--line);border-radius:8px;padding:12px 16px;margin:10px 0}
.ficha div{margin:3px 0}
.score{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}
.score div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px}
.score b{display:block;font-family:Georgia,serif;font-size:1.9rem;line-height:1.1}
.score span{font-size:.9rem;color:var(--muted)}
.sem{width:100%;border-collapse:collapse;margin:10px 0 20px;background:#fff}
.sem td{padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.5}
.dot{display:inline-block;width:14px;height:14px;border-radius:50%;margin-right:8px;vertical-align:-2px}
.dot.g{background:var(--ok)}.dot.a{background:var(--amb)}.dot.r{background:var(--bad)}
.fail{border-left:4px solid var(--bad);background:#fff;padding:10px 14px;margin:10px 0;border-radius:0 8px 8px 0}
.fail .yours{font-size:.92rem;color:var(--muted)}
.review{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin:12px 0}
.review .reto{margin-top:8px;font-style:italic}
.lockbox{background:var(--card);border:2px solid var(--ink);border-radius:12px;padding:24px;max-width:460px}
.lockbox svg{width:34px;height:34px}
.err{color:var(--bad);font-size:.95rem;margin-top:6px}
.lamina{background:#fff;border:1px solid var(--line);border-radius:10px;padding:18px 22px;margin:16px 0}
.muted{color:var(--muted)}
footer.legal{font-size:.85rem;color:var(--muted);border-top:1px solid var(--line);padding-top:14px;margin-top:40px}

.ask{position:fixed;inset:0;background:rgba(20,22,28,.45);display:grid;place-items:center;z-index:50;padding:20px}
.ask[hidden]{display:none}
.ask-box{background:#fff;border-radius:12px;padding:22px 24px;max-width:440px;box-shadow:0 12px 40px rgba(20,22,28,.25)}
.gap{margin-top:36px}
.conv{margin-top:18px;font-weight:600;color:var(--muted)}
img.hero{width:100%;aspect-ratio:16/7;object-fit:cover;border-radius:12px;margin-bottom:18px}
img.trip{width:100%;max-width:600px;border-radius:8px;border:1px solid var(--line);margin-bottom:6px;display:block}
.withimg .pics{gap:10px;max-width:600px}
.withimg .pic{border:0;background:none;padding:4px}
.withimg .plbl{display:none}
.noimg .plbl{display:block}
.pic .plbl{background:#F1ECE6;border-radius:6px;padding:14px 6px;width:100%;font-size:.92rem}
img.lam-img{width:100%;border-radius:8px;margin:8px 0;display:block}
.lamina.q .lam-img + .photo-txt, .lamina.q .lam-img + .photo{display:none}
.lamina.q.noimg .photo-txt, .lamina.q.noimg .photo{display:block}
img.lock-img{width:100%;border-radius:8px;margin-bottom:12px;aspect-ratio:3/2;object-fit:cover}
details{background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px 14px;margin:8px 0}
summary{cursor:pointer;font-weight:600}
.tr p{margin:.35em 0;font-family:Georgia,serif}
.copied-box{background:var(--ok-soft);color:var(--ok);border-radius:10px;padding:12px 16px;margin:4px 0 10px;font-weight:500}
.copied-box.bad{background:var(--amb-soft);color:#7A4E0E}
.copied-box[hidden]{display:none}
.sendbox{border:2px solid var(--coral);border-radius:12px;padding:18px 22px;margin:26px 0;background:#fff}
.lbl-name{display:block;max-width:360px}.lbl-name input{margin-top:6px}
.small{font-size:.88rem}
.print-only{display:none}
.inl .opts{display:flex;flex-wrap:wrap;gap:4px 14px}
.inl .opt{padding:6px 8px}
.letters{display:flex;flex-wrap:wrap;gap:6px}
.letters .opt{padding:2px}
.enun{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 18px;margin:14px 0}
.enun div{margin:4px 0}.enun b{display:inline-block;width:1.6em;color:var(--coral);font-family:Georgia,serif}
.people .paper h4{margin:0 0 6px;font-family:system-ui,sans-serif;font-size:.95rem;letter-spacing:.04em}
.paper .sub{font-family:system-ui,sans-serif;font-size:.9rem;color:var(--muted);margin:-4px 0 14px}
textarea.lined{max-width:45ch;display:block;line-height:2em;padding:0 12px;background-color:#fff;background-image:repeating-linear-gradient(to bottom,transparent 0,transparent calc(2em - 1px),#E3DBD1 calc(2em - 1px),#E3DBD1 2em);background-attachment:local;min-height:18em}
@media print{.noprint,#ask,footer.legal{display:none!important}.print-only{display:block}details{border:0;padding:0}summary{display:none}body{background:#fff}}

@media (max-width:600px){body{font-size:16px}.paper{padding:16px}.pics{grid-template-columns:1fr 1fr 1fr;gap:6px}.pic{padding:6px}.pic .ph{font-size:.8rem}.score{grid-template-columns:1fr}.vocab-row{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
@media print{header.top,nav.steps,.row,.btn{display:none!important}section.view{display:block!important}}
.sw{display:inline-flex;align-items:center;gap:6px;border:1.5px solid var(--line);border-radius:999px;padding:3px 4px 3px 12px;background:#fff;font-size:.85rem;vertical-align:middle;margin-left:10px;font-family:system-ui,sans-serif;font-weight:400}
.sw-lbl{color:var(--muted)}
.sw-t{font-variant-numeric:tabular-nums;font-weight:700;min-width:3.2em;text-align:right;color:var(--ink)}
.sw-b{border:0;background:var(--coral-soft);color:var(--ink);border-radius:50%;width:28px;height:28px;cursor:pointer;font-size:.8rem;line-height:28px;padding:0}
.sw-b:hover{background:var(--coral);color:#fff}
.sw.near{border-color:#C98A1B}.sw.near .sw-t{color:#9A6512}
.sw.ok{border-color:#2F7D4F;background:#EAF5EE}.sw.ok .sw-t{color:#2F7D4F}
.sw.over{border-color:#B3261E;background:#FBEAEA}.sw.over .sw-t{color:#B3261E}
.sw.run .sw-t::after{content:" \25CF";font-size:.6em;color:#B3261E;vertical-align:middle}
.hsw{display:flex;flex-wrap:wrap;align-items:center;gap:6px}
"""
