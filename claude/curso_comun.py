# -*- coding: utf-8 -*-
# Piezas comunes de los ejecutables del CURSO DE PREPARACION DELE A2.
# Paleta y tipografia de los simulacros (coral A2). Todo se escribe en ASCII puro:
# fuera del script, entidades HTML; dentro del script, escapes \uXXXX.

BASE_URL = "https://2spanishteachers.com/biblioteca/recursos/A2/dele-curso/"
EMAIL = "mariar2st@gmail.com"

CSS = r"""
:root{--paper:#FBF9F6;--ink:#14161C;--coral:#E8603C;--coral-soft:#FCE9E1;--cta:#FF6B45;
--line:#E6DFD6;--muted:#5E5A55;--ok:#2F7D4F;--ok-soft:#E3F1E8;--amb:#B7791F;--amb-soft:#FBF0DA;
--bad:#B3261E;--bad-soft:#F8E1DE;--card:#FFFFFF}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink)}
body{font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:17px;line-height:1.6}
h1,h2,h3,h4{font-family:Georgia,"Times New Roman",serif;font-weight:700;line-height:1.25;margin:0 0 .5em}
h2{font-size:1.45rem}h3{font-size:1.15rem}h4{font-size:1.02rem}
.wrap{max-width:820px;margin:0 auto;padding:0 20px 80px}
header.top{border-bottom:3px solid var(--coral);background:var(--card);position:sticky;top:0;z-index:10}
.top-in{max-width:820px;margin:0 auto;padding:14px 20px 0}
.brand small{display:block;color:var(--muted);font-size:.85rem}
nav.steps{display:flex;overflow-x:auto;margin-top:12px}
nav.steps button{flex:0 0 auto;border:0;background:none;padding:8px 9px 10px;font:inherit;font-size:.92rem;color:var(--muted);cursor:pointer;border-bottom:4px solid transparent;display:flex;align-items:center;gap:6px}
nav.steps button .n{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;border:1.5px solid currentColor;font-size:.75rem;font-weight:700}
nav.steps button.on{color:var(--ink);border-bottom-color:var(--coral);font-weight:600}
nav.steps button.done .n{background:var(--ok);border-color:var(--ok);color:#fff}
button:focus-visible,input:focus-visible,textarea:focus-visible,select:focus-visible,summary:focus-visible,a:focus-visible{outline:3px solid var(--cta);outline-offset:2px}
section.view{display:none;padding-top:28px}
section.view.on{display:block}
.lead{font-size:1.05rem;color:var(--muted);max-width:62ch}
.tip{background:var(--coral-soft);border-radius:8px;padding:10px 14px;font-size:.95rem;margin:12px 0}
.note{background:var(--card);border-left:5px solid var(--ink);padding:12px 16px;margin:16px 0;border-radius:0 8px 8px 0}
.btn{font:inherit;font-weight:600;border-radius:999px;padding:10px 22px;cursor:pointer;border:2px solid var(--ink);background:#fff;color:var(--ink);text-decoration:none;display:inline-block}
.btn.cta{background:var(--cta);border-color:var(--cta);color:#fff}
.btn.sm{padding:5px 14px;font-size:.88rem}
.btn:disabled{opacity:.45;cursor:not-allowed}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:18px 0}
.muted{color:var(--muted)}.small{font-size:.88rem}
details{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 16px;margin:10px 0}
summary{cursor:pointer;font-weight:600}
details[open] summary{margin-bottom:8px}
table.t{width:100%;border-collapse:collapse;background:#fff;margin:8px 0 14px}
table.t th{text-align:left;font-size:.85rem;color:var(--muted);font-weight:600;padding:8px 10px;border-bottom:2px solid var(--line)}
table.t td{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.5}
.mono{font-family:'SF Mono',Consolas,monospace;font-size:.9em}
.copied-box{background:var(--ok-soft);color:var(--ok);border-radius:10px;padding:12px 16px;margin:4px 0 10px;font-weight:500}
.copied-box.bad{background:var(--amb-soft);color:#7A4E0E}
.copied-box[hidden]{display:none}
footer.legal{font-size:.85rem;color:var(--muted);border-top:1px solid var(--line);padding-top:14px;margin-top:40px}
@media (max-width:600px){body{font-size:16px}table.t td,table.t th{padding:7px 6px}}
"""

# BARRA DE PESTANAS (14/10): una sola fila en movil y en ordenador. Si no caben todas, se ven flechas
# con degradado en el borde (se pueden pulsar) y la pestana actual se centra sola. La rueda del raton
# tambien la mueve. No necesita nada en los builds: page() lo anade a cualquier <nav class="steps">.
NAV_CSS = r"""
.top-in{position:relative}
nav.steps{scrollbar-width:none;scroll-behavior:smooth}
nav.steps::-webkit-scrollbar{display:none}
.navarr{position:absolute;width:52px;border:0;padding:0 6px 4px;display:none;align-items:center;cursor:pointer;font:700 2rem/1 Georgia,serif;color:var(--coral);z-index:2}
.navarr.r{right:0;justify-content:flex-end;background:linear-gradient(to right,rgba(255,255,255,0),#fff 55%)}
.navarr.l{left:0;justify-content:flex-start;background:linear-gradient(to left,rgba(255,255,255,0),#fff 55%)}
.navarr.show{display:flex}
@media print{.navarr{display:none!important}}
"""

NAV_JS = r"""
(function(){
 var nav=document.querySelector('nav.steps'); if(!nav) return;
 var box=nav.parentNode, L=document.createElement('button'), R=document.createElement('button');
 L.className='navarr l'; R.className='navarr r'; L.type=R.type='button';
 L.textContent='‹'; R.textContent='›';
 L.setAttribute('aria-label','Ver las pestañas anteriores'); R.setAttribute('aria-label','Ver más pestañas');
 box.appendChild(L); box.appendChild(R);
 function upd(){
  L.style.top=R.style.top=nav.offsetTop+'px'; L.style.height=R.style.height=nav.offsetHeight+'px';
  var max=nav.scrollWidth-nav.clientWidth;
  L.classList.toggle('show', nav.scrollLeft>4); R.classList.toggle('show', nav.scrollLeft<max-4);
 }
 function center(){
  var on=nav.querySelector('button.on'); if(!on) return upd();
  var x=on.offsetLeft-nav.offsetLeft-(nav.clientWidth-on.offsetWidth)/2;
  nav.scrollLeft=Math.max(0,x); upd();
 }
 function step(d){ nav.scrollBy({left:d*nav.clientWidth*0.7}); }
 L.addEventListener('click',function(){ step(-1); }); R.addEventListener('click',function(){ step(1); });
 nav.addEventListener('scroll',upd,{passive:true}); window.addEventListener('resize',center);
 nav.addEventListener('wheel',function(e){ if(nav.scrollWidth>nav.clientWidth && Math.abs(e.deltaY)>Math.abs(e.deltaX)){ nav.scrollLeft+=e.deltaY; e.preventDefault(); } },{passive:false});
 if(window.MutationObserver) new MutationObserver(function(){ setTimeout(center,0); }).observe(nav,{childList:true});
 setTimeout(center,0);
})();
"""

def enc_html(s):
    return ''.join(c if ord(c) < 128 else '&#x%X;' % ord(c) for c in s)

def enc_js(s):
    out = []
    for c in s:
        o = ord(c)
        if o < 128: out.append(c)
        elif o <= 0xFFFF: out.append('\\u%04X' % o)
        else:
            o -= 0x10000; out.append('\\u%04X\\u%04X' % (0xD800 + (o >> 10), 0xDC00 + (o & 0x3FF)))
    return ''.join(out)

def page(title, css, body, js, extra_head=""):
    return ('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="robots" content="noindex, nofollow">\n'
            '<title>' + enc_html(title) + '</title>\n' + extra_head +
            '<style>' + enc_html(css + NAV_CSS) + '</style>\n</head>\n<body>\n' + enc_html(body) +
            '\n<script>\n' + enc_js(js + "\n" + NAV_JS) + '\n</script>\n</body>\n</html>\n')
