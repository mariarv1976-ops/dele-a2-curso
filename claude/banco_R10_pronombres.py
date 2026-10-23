# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R10: LO, LA, LE (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R10_pronombres.py
#
# ENFOQUE COGNITIVO (aprobado por Maria, 22/10): EL PAQUETE Y EL DESTINATARIO
#   El verbo mueve un PAQUETE (lo que compras, ves, llamas, traes...) hacia un DESTINATARIO (la persona que lo
#   recibe).
#   d  EL PAQUETE: lo / la / los / las. Lleva la camiseta de su nombre (R04): la tarta -> la compro.
#   i  EL DESTINATARIO: le / les. Solo dice "a que persona"; no tiene genero: le escribo (a Juan, a Ana).
#   m  ME, TE, NOS, OS: sirven para los dos papeles y no cambian nunca.
#   p  EL IMAN (donde va): delante del verbo conjugado (lo compro, lo voy a comprar) o PEGADO detras del
#      infinitivo, del gerundio o del imperativo afirmativo (comprarlo, comprandolo, compralo). Nunca en medio,
#      nunca suelto detras del verbo conjugado, nunca dos veces.
#   Espana: "le vi" (a un hombre) es correcto y vale en el examen (el detector no lo marca); *la dije, *la gusta
#   y le para una cosa son errores. Usted = el / ella: le escribo, lo / la (o le) espero (R07).
#   NIVEL: solo [P] del Plan curricular (GR-06, GR-16). Las combinaciones (se lo, me la), la duplicacion del
#   paquete (el pan lo compro yo) y el imperativo negativo (no lo toques) son [R]: solo en el recuadro plegado
#   "Lo veras en los textos", nunca en ejercicios, huecos, modelos ni en el detector (el build lo comprueba).
#
# MARCAS
#   [d:la] el paquete (turquesa) · [i:le] el destinatario (violeta) · [m:te] me/te/nos/os (verde)
#   [p:comprarla] pegado al infinitivo, al gerundio o al imperativo (coral)
#   Huecos: [[correcta|distractor|distractor#motivo]]  (la primera es la buena; se barajan)
# Espanol de Espana. Ejemplos propios: ninguno sale de los materiales de Maria ni repite los de R01-R08.

# ------------------------------------------------------------------ LAS PIEZAS
FAMILIAS = {
    "d": {"n": "El paquete", "dib": "la caja que mueve el verbo", "q": "¿Qué? (o ¿a quién?, sin nada más)",
          "words": ["lo", "la", "los", "las"],
          "txt": "Es lo que <b>recibe la acción directamente</b>: lo que compras, ves, llamas, esperas. Lleva la camiseta de su nombre: <b>lo</b>, <b>la</b>, <b>los</b>, <b>las</b>."},
    "i": {"n": "El destinatario", "dib": "la persona que recibe el paquete", "q": "¿A quién le llega?",
          "words": ["le", "les"],
          "txt": "Es la <b>persona que recibe el paquete</b>: a quien le das, mandas, escribes o dices algo. Solo cambia para varios: <b>le</b>, <b>les</b>."},
    "m": {"n": "Me, te, nos, os", "dib": "los comodines", "q": "¿Yo, tú, nosotros, vosotros?",
          "words": ["me", "te", "nos", "os"],
          "txt": "Sirven para <b>los dos papeles</b> y no cambian nunca: <b>te</b> llamo (paquete), <b>te</b> regalo un libro (destinatario)."},
    "p": {"n": "Pegado", "dib": "el imán", "q": "¿Dónde va?",
          "words": [],
          "txt": "Delante del verbo conjugado (<b>lo</b> compro) o <b>pegado</b> al final del infinitivo, del gerundio y del imperativo: <b>comprarlo</b>, <b>comprándolo</b>, <b>cómpralo</b>."},
}
ORDEN_FAM = ["d", "i", "m", "p"]
PRONOMBRES = ["lo", "la", "los", "las", "le", "les", "me", "te", "nos", "os"]

# Mira la diferencia. Cada lado: f = frase marcada; k = d (solo paquete) o i (paquete + destinatario);
# verbo, paq (el paquete), per (la persona que lo recibe, solo en i) y pron (el pronombre de la frase).
PAREJAS = [
    {"tema": "La tarta",
     "a": {"f": "¿La tarta? [d:La] compro yo.", "k": "d", "verbo": "compro", "paq": "la tarta", "per": "", "pron": "la"},
     "b": {"f": "Mañana es el cumpleaños de mi madre: [i:le] compro una tarta.", "k": "i", "verbo": "compro", "paq": "una tarta", "per": "mi madre", "pron": "le"},
     "expl": "El mismo verbo, otro papel. En la primera, la tarta es el paquete: <b>la</b> (tarta es femenino y singular). En la segunda, el paquete es «una tarta» y tu madre lo recibe: es la destinataria, <b>le</b>."},
    {"tema": "Ana",
     "a": {"f": "¿Ana? [d:La] llamo esta noche.", "k": "d", "verbo": "llamo", "paq": "Ana", "per": "", "pron": "la"},
     "b": {"f": "¿Ana? [i:Le] escribo un mensaje esta noche.", "k": "i", "verbo": "escribo", "paq": "un mensaje", "per": "Ana", "pron": "le"},
     "expl": "<b>Llamar</b>: Ana recibe la llamada directamente, no hay otro paquete: <b>la</b>. <b>Escribir</b>: el paquete es el mensaje y Ana lo recibe: <b>le</b>. Y le no cambia: le escribo a Ana, le escribo a Pedro."},
    {"tema": "Mis padres",
     "a": {"f": "¿Mis padres? [d:Los] visito los domingos.", "k": "d", "verbo": "visito", "paq": "mis padres", "per": "", "pron": "los"},
     "b": {"f": "¿Mis padres? [i:Les] mando fotos de los niños.", "k": "i", "verbo": "mando", "paq": "fotos", "per": "mis padres", "pron": "les"},
     "expl": "Visitas a tus padres: ellos son el paquete, <b>los</b> (masculino y plural). Les mandas fotos: el paquete son las fotos y tus padres las reciben: <b>les</b>."},
    {"tema": "El profesor",
     "a": {"f": "¿El profesor? [d:Lo] espero en la puerta.", "k": "d", "verbo": "espero", "paq": "el profesor", "per": "", "pron": "lo"},
     "b": {"f": "¿El profesor? [i:Le] pregunto una duda.", "k": "i", "verbo": "pregunto", "paq": "una duda", "per": "el profesor", "pron": "le"},
     "expl": "Esperas al profesor: es el paquete, <b>lo</b>. Le preguntas una duda: el paquete es la duda, él la recibe, <b>le</b>. En España también oirás «le espero» con un hombre: es correcto. Tú puedes usar <b>lo</b>."},
    {"tema": "Las fotos",
     "a": {"f": "¿Las fotos del viaje? [d:Las] miro todos los días.", "k": "d", "verbo": "miro", "paq": "las fotos", "per": "", "pron": "las"},
     "b": {"f": "¿Mis amigos? [i:Les] enseño las fotos del viaje.", "k": "i", "verbo": "enseño", "paq": "las fotos", "per": "mis amigos", "pron": "les"},
     "expl": "Las fotos son el paquete en las dos frases. En la primera no hay nadie más: <b>las</b>. En la segunda, tus amigos las reciben: los destinatarios son <b>les</b>."},
    {"tema": "Tú",
     "a": {"f": "[m:Te] invito a cenar el sábado.", "k": "d", "verbo": "invito", "paq": "tú", "per": "", "pron": "te"},
     "b": {"f": "[m:Te] regalo un libro para tu cumpleaños.", "k": "i", "verbo": "regalo", "paq": "un libro", "per": "tú", "pron": "te"},
     "expl": "Con <b>me</b>, <b>te</b>, <b>nos</b> y <b>os</b> no tienes que pensar: sirven para el paquete y para el destinatario. Solo cambian lo, la, los, las y le, les."},
]

# Para que sirven: el mismo texto con y sin pronombres
SIN = "Tengo un piso nuevo. El piso es pequeño, pero el piso tiene terraza. Mis padres van a ver el piso el sábado y yo voy a enseñar el piso a mis padres con mucha ilusión."
CON_OK = "Tengo un piso nuevo. Es pequeño, pero tiene terraza. Mis padres [d:lo] van a ver el sábado. ¡[d:Lo] estoy limpiando todos los días!"

# ------------------------------------------------------------------ DONDE VA: EL IMAN
# El constructor: un verbo + una forma -> las frases buenas (marcadas)
FORMAS = [
    ("pres", "Presente", "Verbo conjugado: el pronombre va <b>delante</b>, separado. Nunca detrás: *compro lo."),
    ("ira", "Ir a + infinitivo", "Dos sitios buenos: <b>delante</b> del verbo conjugado (voy) o <b>pegado</b> al final del infinitivo. Nunca en medio (*voy a lo comprar) y nunca dos veces (*lo voy a comprarlo)."),
    ("tener", "Tener que + infinitivo", "Igual que ir a: <b>delante</b> de tengo o <b>pegado</b> al infinitivo. Nunca entre que y el infinitivo."),
    ("estar", "Estar + gerundio", "<b>Delante</b> de estoy o <b>pegado</b> al gerundio. Si lo pegas, pon tilde: comprándola, escribiéndole."),
    ("perf", "Pretérito perfecto", "Con haber, el pronombre va <b>delante</b> de he, has, ha... Nunca pegado al participio (*he compradola)."),
    ("neg", "Con no", "El orden es fijo: <b>no + pronombre + verbo</b>. No lo compro, no le escribo."),
    ("imp_tu", "Imperativo (tú)", "Imperativo afirmativo: siempre <b>pegado</b> al final, y casi siempre con tilde: cómprala, escríbele."),
    ("imp_ud", "Imperativo (usted)", "También <b>pegado</b>: cómprela, escríbale. Usted es como él o ella (ficha R07)."),
]
# Cada verbo: txt (lo que se hace), pron, k (d / i / m) y una lista de frases buenas por forma.
VERBOS = [
    {"id": "tarta", "txt": "comprar la tarta", "pron": "la", "k": "d", "f": {
        "pres": ["[d:La] compro hoy."], "ira": ["[d:La] voy a comprar.", "Voy a [p:comprarla]."],
        "tener": ["[d:La] tengo que comprar.", "Tengo que [p:comprarla]."], "estar": ["[d:La] estoy comprando.", "Estoy [p:comprándola]."],
        "perf": ["Ya [d:la] he comprado."], "neg": ["No [d:la] compro."], "imp_tu": ["[p:Cómprala], por favor."], "imp_ud": ["[p:Cómprela], por favor."]}},
    {"id": "pedro", "txt": "llamar a Pedro", "pron": "lo", "k": "d", "f": {
        "pres": ["[d:Lo] llamo esta tarde."], "ira": ["[d:Lo] voy a llamar.", "Voy a [p:llamarlo]."],
        "tener": ["[d:Lo] tengo que llamar.", "Tengo que [p:llamarlo]."], "estar": ["[d:Lo] estoy llamando.", "Estoy [p:llamándolo]."],
        "perf": ["Ya [d:lo] he llamado."], "neg": ["No [d:lo] llamo."], "imp_tu": ["[p:Llámalo] ahora."], "imp_ud": ["[p:Llámelo] ahora."]}},
    {"id": "billetes", "txt": "imprimir los billetes", "pron": "los", "k": "d", "f": {
        "pres": ["[d:Los] imprimo en casa."], "ira": ["[d:Los] voy a imprimir.", "Voy a [p:imprimirlos]."],
        "tener": ["[d:Los] tengo que imprimir.", "Tengo que [p:imprimirlos]."], "estar": ["[d:Los] estoy imprimiendo.", "Estoy [p:imprimiéndolos]."],
        "perf": ["Ya [d:los] he imprimido."], "neg": ["No [d:los] imprimo."], "imp_tu": ["[p:Imprímelos], por favor."], "imp_ud": ["[p:Imprímalos], por favor."]}},
    {"id": "fotos", "txt": "enviar las fotos", "pron": "las", "k": "d", "f": {
        "pres": ["[d:Las] envío esta noche."], "ira": ["[d:Las] voy a enviar.", "Voy a [p:enviarlas]."],
        "tener": ["[d:Las] tengo que enviar.", "Tengo que [p:enviarlas]."], "estar": ["[d:Las] estoy enviando.", "Estoy [p:enviándolas]."],
        "perf": ["Ya [d:las] he enviado."], "neg": ["No [d:las] envío."], "imp_tu": ["[p:Envíalas] hoy."], "imp_ud": ["[p:Envíelas] hoy."]}},
    {"id": "abuela", "txt": "escribir un mensaje a mi abuela", "pron": "le", "k": "i", "f": {
        "pres": ["[i:Le] escribo un mensaje."], "ira": ["[i:Le] voy a escribir un mensaje.", "Voy a [p:escribirle] un mensaje."],
        "tener": ["[i:Le] tengo que escribir un mensaje.", "Tengo que [p:escribirle] un mensaje."],
        "estar": ["[i:Le] estoy escribiendo un mensaje.", "Estoy [p:escribiéndole] un mensaje."],
        "perf": ["Ya [i:le] he escrito un mensaje."], "neg": ["No [i:le] escribo."], "imp_tu": ["[p:Escríbele] un mensaje."], "imp_ud": ["[p:Escríbale] un mensaje."]}},
    {"id": "amigos", "txt": "explicar el plan a mis amigos", "pron": "les", "k": "i", "f": {
        "pres": ["[i:Les] explico el plan."], "ira": ["[i:Les] voy a explicar el plan.", "Voy a [p:explicarles] el plan."],
        "tener": ["[i:Les] tengo que explicar el plan.", "Tengo que [p:explicarles] el plan."],
        "estar": ["[i:Les] estoy explicando el plan.", "Estoy [p:explicándoles] el plan."],
        "perf": ["Ya [i:les] he explicado el plan."], "neg": ["No [i:les] explico nada."], "imp_tu": ["[p:Explícales] el plan."], "imp_ud": ["[p:Explíqueles] el plan."]}},
    {"id": "nos", "txt": "ayudarnos (a nosotros)", "pron": "nos", "k": "m", "f": {
        "pres": ["¿[m:Nos] ayudas?"], "ira": ["¿[m:Nos] vas a ayudar?", "¿Vas a [p:ayudarnos]?"],
        "tener": ["[m:Nos] tienes que ayudar.", "Tienes que [p:ayudarnos]."], "estar": ["¿[m:Nos] estás ayudando?", "¿Estás [p:ayudándonos]?"],
        "perf": ["Ya [m:nos] has ayudado mucho."], "neg": ["No [m:nos] ayudas nada."], "imp_tu": ["[p:Ayúdanos], por favor."], "imp_ud": ["[p:Ayúdenos], por favor."]}},
]
# Lo que nunca se hace (sale debajo del iman)
NUNCA = [
    ("*Compro lo.", "suelto detrás del verbo conjugado"),
    ("*Voy a lo comprar.", "en medio"),
    ("*Lo voy a comprarlo.", "dos veces"),
    ("*Voy a comprar lo.", "separado del infinitivo"),
]

# ------------------------------------------------------------------ LO, LA O LE
SOLO_PAQ = [
    ("comprar", "¿La leche? [d:La] compro yo."), ("ver", "¿Tu hermano? [d:Lo] veo los lunes."),
    ("llamar", "¿Ana? [d:La] llamo luego."), ("conocer", "¿Los vecinos? No [d:los] conozco."),
    ("invitar", "¿Tus amigas? [d:Las] invito a mi fiesta."), ("esperar", "¿El autobús? [d:Lo] espero aquí."),
    ("ayudar", "¿Tu madre? [d:La] ayudo en casa."), ("visitar", "¿Tus abuelos? [d:Los] visito en verano."),
]
PAQ_DEST = [
    ("dar", "[i:Le] doy las llaves."), ("regalar", "[i:Les] regalo un viaje."), ("mandar / enviar", "[i:Le] mando un mensaje."),
    ("escribir", "[i:Les] escribo una postal."), ("decir", "[i:Le] digo la verdad."), ("contar", "[i:Les] cuento un secreto."),
    ("explicar", "[i:Le] explico el problema."), ("preguntar", "[i:Le] pregunto el camino."), ("prestar", "[i:Le] presto mi bici."),
]
DOS_PREGUNTAS = [
    "<b>1. ¿El verbo ya lleva un paquete?</b> (das <i>algo</i>, mandas <i>algo</i>, dices <i>algo</i>...) Entonces la persona que lo recibe es el destinatario: <b>le</b> o <b>les</b>. No mira si es hombre o mujer.",
    "<b>2. ¿No hay otro paquete?</b> Entonces lo que recibe la acción (una cosa o una persona) es el paquete: <b>lo, la, los, las</b>, con la camiseta de su nombre (ficha R04).",
]
LEISMO = ("En España mucha gente dice <b>le</b> cuando el paquete es un hombre: <i>«¿Has visto a Pedro? Sí, le vi ayer.»</i> "
          "Es correcto y vale en el examen. Con mujeres y con cosas, no: <i>la vi</i> (a Ana), <i>lo compré</i> (el pan). "
          "Lo más fácil para ti: usa siempre <b>lo / la</b> para el paquete y <b>le</b> solo para el destinatario.")
USTED = [
    "[i:Le] escribo para pedir información sobre el curso.",
    "¿[i:Le] puedo hacer una pregunta?",
    "Señora Pons, [d:la] espero en la recepción.",
]
USTED_TXT = ("Usted habla como <b>él / ella</b> (ficha R07), así que sus pronombres son los de él y ella: <b>le</b> para el destinatario "
             "y <b>lo / la</b> para el paquete. En España vas a oír mucho <i>le espero</i>, <i>le llamo</i> a usted: también es correcto.")
REFLEXIVOS = ("Ojo: <b>me levanto</b>, <b>se ducha</b>, <b>nos vamos</b> son verbos reflexivos (ya los conoces). Ese <b>se</b> no es un paquete ni un "
              "destinatario. Pero <b>dónde va</b> sí es igual: me voy a duchar = voy a ducharme; ¡levántate!")
# [R] del Plan curricular: se ven en los textos, no hacen falta para aprobar (no se practican)
LOS_VERAS = [
    ("se lo, se la...", "Dos pronombres juntos: le + lo se dice se lo.", "¿El libro? Se lo di a Marta."),
    ("me lo, te la...", "Dos pronombres juntos.", "Esta pulsera me la regaló mi abuela."),
    ("el pan lo compro yo", "El paquete delante, y otra vez el pronombre.", "Las entradas las tengo yo."),
    ("no lo toques", "El imperativo con no: el pronombre va delante.", "No lo abras todavía."),
]

# ------------------------------------------------------------------ EN EL EXAMEN
DONDE = [
    ("Escritura · tarea 1", "En el correo escribes a una persona: <b>te</b> escribo, <b>te</b> mando las fotos, <b>llámame</b>. Y contestas a sus preguntas sin repetir el nombre.",
     "¿Tu libro? Sí, [d:lo] tengo yo. [p:Llámame] y quedamos."),
    ("Escritura · tarea 2", "En una biografía o en un relato, los pronombres unen las frases: no repites el nombre de la persona en cada línea.",
     "Conocí a Lola en 2015. [d:La] vi por primera vez en una clase de baile."),
    ("Oral · tarea 3", "El examinador te pregunta quién hace cada cosa. Contesta con un pronombre, sin repetir: suena natural y rápido.",
     "—¿Quién compra las bebidas? —[d:Las] compro yo."),
    ("Oral · tarea 3 de usted", "Con un dependiente o un recepcionista, le y lo / la de usted.",
     "Perdone, ¿[i:le] puedo hacer una pregunta?"),
    ("Lectura y auditiva", "Una pregunta típica: ¿a quién se refiere ese <b>le</b> o ese <b>la</b>? Busca hacia atrás el nombre que tiene la misma camiseta.",
     "Mi madre quería un perro y mi padre [i:le] regaló uno por Navidad."),
    ("Lectura · instrucciones", "En los avisos y formularios, el imperativo de usted lleva el pronombre pegado.",
     "[p:Rellénelo] con letras mayúsculas y [p:entréguelo] en recepción."),
]
REGLA_ORO = ("En la revisión final, haz una pasada solo para los pronombres: ¿a qué se refiere cada <b>lo, la, le</b>? "
             "¿Va delante del verbo conjugado o pegado al infinitivo? Y si repites un nombre dos veces seguidas, cambia el segundo por un pronombre.")
# Errores tipicos: (mal, bien marcado, por que). Cada "mal" tiene que dar un aviso del detector.
ERRORES = [
    ("Compro lo mañana.", "[d:Lo] compro mañana.",
     "Con un verbo conjugado, el pronombre va <b>delante</b>, nunca suelto detrás."),
    ("Voy a lo comprar el sábado.", "[d:Lo] voy a comprar el sábado. O: Voy a [p:comprarlo] el sábado.",
     "Nunca <b>en medio</b>: delante de voy o pegado a comprar."),
    ("Lo voy a comprarlo.", "[d:Lo] voy a comprar. O: Voy a [p:comprarlo].",
     "El pronombre va <b>una sola vez</b>: delante o pegado, no en los dos sitios."),
    ("Tengo que escribir le un correo.", "Tengo que [p:escribirle] un correo.",
     "Detrás del infinitivo, <b>pegado</b>: una sola palabra."),
    ("Estamos esperando te en la puerta.", "[m:Te] estamos esperando en la puerta. O: Estamos [p:esperándote] en la puerta.",
     "Con el gerundio, delante de estar o <b>pegado</b> (y con tilde)."),
    ("La dije que no podía ir.", "[i:Le] dije que no podía ir.",
     "Le dices algo a ella: el paquete es lo que dices y ella es la destinataria: <b>le</b>, también para una mujer."),
    ("Llama me esta tarde.", "[p:Llámame] esta tarde.",
     "Imperativo afirmativo: el pronombre va <b>pegado</b> al final y el verbo lleva tilde."),
    ("Mi abuela vive sola: la escribo un correo cada semana.", "Mi abuela vive sola: [i:le] escribo un correo cada semana.",
     "El paquete es el correo; tu abuela lo recibe: <b>le</b>."),
    ("La gusta mucho el cine.", "[i:Le] gusta mucho el cine.",
     "Con gustar, encantar, interesar o doler, siempre <b>le / les</b> (ficha R09)."),
    ("Ayer compré la camiseta azul. La camiseta es muy bonita.", "Ayer compré la camiseta azul. Es muy bonita: [d:la] llevo hoy.",
     "No repitas el nombre en la frase siguiente: el texto pesa. Cámbialo por un pronombre o quítalo."),
    ("Le voy a mandarle las fotos.", "[i:Le] voy a mandar las fotos. O: Voy a [p:mandarle] las fotos.",
     "Una sola vez: delante o pegado."),
]
REQ = ["suelto", "en_medio", "doble", "inf_sep", "ger_sep", "laismo", "gusta_lo", "repite"]

# ------------------------------------------------------------------ EJERCICIOS
# 1. ¿Que pronombre? q con ____, f = pieza de la buena (d / i / m), o = [buena, d1, d2]
P_PRON = [
    {"q": "—¿Dónde está la llave? —No sé, no ____ encuentro.", "f": "d", "o": ["la", "le", "lo"], "why": "La llave es el paquete, femenino y singular: <b>la</b>."},
    {"q": "Mañana es el cumpleaños de mi padre. ____ voy a regalar un reloj.", "f": "i", "o": ["Le", "Lo", "La"], "why": "El paquete es el reloj; tu padre lo recibe: <b>le</b>."},
    {"q": "—¿Has visto a Pablo? —Sí, ____ he visto esta mañana en el gimnasio.", "f": "d", "o": ["lo", "la", "los"], "why": "Pablo es el paquete (ves a Pablo, no hay nada más): <b>lo</b>. En España también se oye «le he visto»."},
    {"q": "Mis abuelos viven en el pueblo. ____ escribo una carta cada mes.", "f": "i", "o": ["Les", "Los", "Le"], "why": "El paquete es la carta; tus abuelos la reciben: <b>les</b> (son varios)."},
    {"q": "—¿Te gustan estas gafas? —Sí, ____ compro.", "f": "d", "o": ["las", "les", "los"], "why": "Las gafas son el paquete, femenino y plural: <b>las</b>."},
    {"q": "—¿Me ayudas con la maleta? —Claro, ahora ____ ayudo.", "f": "m", "o": ["te", "le", "me"], "why": "Te lo pide a ti: <b>te</b> ayudo. Me y te no cambian."},
    {"q": "—¿Has llamado a tu hermana? —No, ____ llamo esta tarde.", "f": "d", "o": ["la", "le", "lo"], "why": "Tu hermana es el paquete (la llamas): <b>la</b>. «Le llamo» para una mujer no es correcto."},
    {"q": "Lucía, ¿____ dejas tu bolígrafo un momento?", "f": "m", "o": ["me", "te", "le"], "why": "Tú lo recibes: ¿<b>me</b> dejas...? El paquete es el bolígrafo."},
    {"q": "Profesora, ¿____ puedo hacer una pregunta?", "f": "i", "o": ["le", "la", "te"], "why": "A usted: como él o ella. El paquete es la pregunta y usted la recibe: <b>le</b>."},
    {"q": "Chicos, ____ espero en la puerta del cine a las ocho.", "f": "m", "o": ["os", "les", "los"], "why": "Hablas a vosotros: <b>os</b>. Os no cambia."},
    {"q": "Los niños tienen hambre. ¿____ preparo un bocadillo?", "f": "i", "o": ["Les", "Los", "Le"], "why": "El paquete es el bocadillo; los niños lo reciben: <b>les</b>."},
    {"q": "—¿Y el pan? —Ya ____ he comprado.", "f": "d", "o": ["lo", "le", "la"], "why": "El pan es el paquete, masculino y singular: <b>lo</b>."},
    {"q": "—¿Conoces a Marta y a Elena? —Sí, ____ conocí en la boda de Juan.", "f": "d", "o": ["las", "les", "los"], "why": "Ellas son el paquete (las conoces), femenino y plural: <b>las</b>."},
    {"q": "Señor Gil: ____ escribo para confirmar la reserva del sábado.", "f": "i", "o": ["le", "lo", "te"], "why": "Correo de usted: el paquete es lo que escribes, él lo recibe: <b>le</b>."},
    {"q": "—¿Qué ____ decimos a los vecinos? —Que la fiesta termina a las once.", "f": "i", "o": ["les", "los", "le"], "why": "El paquete es lo que dices; los vecinos lo reciben: <b>les</b>."},
    {"q": "Mi madre ____ llama todos los domingos a mi hermano y a mí.", "f": "m", "o": ["nos", "les", "los"], "why": "Mi hermano y yo = nosotros: <b>nos</b>."},
]
# 2. ¿Donde va? (q con ____ = la frase entera; o = [buena, d1, d2])
P_DONDE = [
    {"q": "—¿Y la tarta? —____", "o": ["Voy a comprarla mañana.", "Voy a la comprar mañana.", "Voy a comprar la mañana."], "why": "Con ir a + infinitivo: delante de voy o <b>pegado</b> al infinitivo. Nunca en medio ni suelto."},
    {"q": "—¿Y los billetes? —____", "o": ["Los tengo yo.", "Tengo los yo.", "Tengo yo los."], "why": "Verbo conjugado: el pronombre va <b>delante</b>."},
    {"q": "—¿Y la cena? —____", "o": ["Estoy preparándola.", "Estoy la preparando.", "Estoy preparando la."], "why": "Con el gerundio, <b>pegado</b> y con tilde (o delante: la estoy preparando)."},
    {"q": "—¿Y tu hermano? —____", "o": ["Lo voy a ver el sábado.", "Voy a lo ver el sábado.", "Lo voy a verlo el sábado."], "why": "Delante de voy, y una sola vez."},
    {"q": "—Necesito hablar contigo. —Vale, ____", "o": ["llámame esta tarde.", "llama me esta tarde.", "me llámame esta tarde."], "why": "Imperativo afirmativo: <b>pegado</b> al final y con tilde. Una sola vez."},
    {"q": "—¿Dónde dejo las maletas? —____", "o": ["Déjelas aquí, por favor.", "Deje las aquí, por favor.", "Las déjelas aquí, por favor."], "why": "Imperativo de usted: también <b>pegado</b> al final."},
    {"q": "—¿Has visto mis gafas? —____", "o": ["No, no las he visto.", "No, no he las visto.", "No, no he visto las."], "why": "Con haber, <b>delante</b> de he, has, ha. Nunca entre he y el participio."},
    {"q": "—¿Y Ana? —____", "o": ["Tenemos que llamarla hoy.", "Tenemos que la llamar hoy.", "Tenemos la que llamar hoy."], "why": "Pegado al infinitivo (o delante de tenemos: la tenemos que llamar)."},
    {"q": "—¿Y tus padres? —____", "o": ["Les escribo todas las semanas.", "Escribo les todas las semanas.", "Escribo a les todas las semanas."], "why": "Verbo conjugado: <b>delante</b>."},
    {"q": "—¿Me ayudas? —____", "o": ["Sí, ahora te ayudo.", "Sí, ahora ayudo te.", "Sí, ahora te ayudo te."], "why": "Delante del verbo conjugado, y una sola vez."},
    {"q": "—¿Y el libro? —____", "o": ["Lo estoy leyendo.", "Estoy lo leyendo.", "Lo estoy leyéndolo."], "why": "Delante de estoy (o pegado: estoy leyéndolo). Nunca en medio ni dos veces."},
    {"q": "—Hace mucho calor aquí. —Es verdad. ____", "o": ["Abre la ventana y déjala abierta.", "Abre la ventana y deja la abierta.", "Abre la ventana y la déjala abierta."], "why": "Imperativo afirmativo: <b>pegado</b> (déjala), una sola vez."},
]
# 4. Bien o mal: ok 0 = bien, 1 = mal
E_BIENMAL = [
    {"q": "Necesito el libro: ¿puedes traer lo mañana?", "ok": 1, "fix": "Necesito el libro: ¿puedes <b>traerlo</b> mañana?", "why": "Detrás del infinitivo, pegado: traerlo."},
    {"q": "Tengo que la llamar esta tarde.", "ok": 1, "fix": "<b>La</b> tengo que llamar esta tarde. O: Tengo que <b>llamarla</b>.", "why": "Nunca en medio."},
    {"q": "Los vamos a verlos el domingo.", "ok": 1, "fix": "<b>Los</b> vamos a ver el domingo.", "why": "Una sola vez: delante o pegado."},
    {"q": "Estoy escuchando la. ¡Me encanta esta canción!", "ok": 1, "fix": "<b>La</b> estoy escuchando. O: Estoy <b>escuchándola</b>.", "why": "Nunca suelto: delante de estoy o pegado al gerundio."},
    {"q": "La pregunté una duda a la profesora.", "ok": 1, "fix": "<b>Le</b> pregunté una duda a la profesora.", "why": "El paquete es la duda; la profesora la recibe: le."},
    {"q": "Ayer vi a Marta y la di un abrazo.", "ok": 1, "fix": "Ayer vi a Marta y <b>le</b> di un abrazo.", "why": "El paquete es el abrazo; Marta lo recibe: le."},
    {"q": "A Luis lo gusta mucho cocinar.", "ok": 1, "fix": "A Luis <b>le</b> gusta mucho cocinar.", "why": "Con gustar, siempre le / les."},
    {"q": "Voy a ayudar te con los deberes.", "ok": 1, "fix": "Voy a <b>ayudarte</b> con los deberes. O: <b>Te</b> voy a ayudar.", "why": "Pegado al infinitivo, en una sola palabra."},
    {"q": "¿El libro? Trae lo, por favor.", "ok": 1, "fix": "¿El libro? <b>Tráelo</b>, por favor.", "why": "Con el imperativo afirmativo, el pronombre va pegado y el verbo lleva tilde."},
    {"q": "¿Los billetes? Los tengo yo.", "ok": 0, "fix": "", "why": "Correcto: verbo conjugado, pronombre delante."},
    {"q": "Voy a comprarlo esta tarde.", "ok": 0, "fix": "", "why": "Correcto: pegado al infinitivo."},
    {"q": "Lo estoy leyendo y me encanta.", "ok": 0, "fix": "", "why": "Correcto: delante de estoy."},
    {"q": "Señora Ruiz, le escribo para pedir información.", "ok": 0, "fix": "", "why": "Correcto: usted recibe lo que escribo, le."},
    {"q": "Pásame la sal, por favor.", "ok": 0, "fix": "", "why": "Correcto: imperativo con el pronombre pegado y tilde."},
    {"q": "Ayer vi a Pedro y le saludé.", "ok": 0, "fix": "", "why": "Correcto en España: le para un hombre (también se dice lo saludé)."},
    {"q": "No la conozco, pero parece simpática.", "ok": 0, "fix": "", "why": "Correcto: no + pronombre + verbo."},
    {"q": "Les he mandado un mensaje a mis primos.", "ok": 0, "fix": "", "why": "Correcto: el mensaje es el paquete y tus primos lo reciben, les."},
]

# 3. Textos con huecos: motivos (pieza, explicacion, respuestas buenas: lista o regex)
MOTIVOS = {
    "paq_lo": ("d", "El paquete es masculino y singular: <b>lo</b>.", ["lo"]),
    "paq_la": ("d", "El paquete es femenino y singular: <b>la</b>.", ["la"]),
    "paq_los": ("d", "El paquete es masculino y plural: <b>los</b>.", ["los"]),
    "paq_las": ("d", "El paquete es femenino y plural: <b>las</b>.", ["las"]),
    "dest_le": ("i", "Una persona recibe el paquete: <b>le</b> (para él y para ella).", ["le"]),
    "dest_les": ("i", "Varias personas reciben el paquete: <b>les</b>.", ["les"]),
    "usted": ("i", "Usted es como él o ella y recibe el paquete: <b>le</b>.", ["le"]),
    "dos": ("m", "<b>Me, te, nos, os</b> sirven para los dos papeles y no cambian.", ["me", "te", "nos", "os"]),
    "pos_conj": ("p", "Con el verbo conjugado, <b>delante</b> y separado.", r"^(?:lo|la|los|las|le|les|me|te|nos|os) \S+$"),
    "pos_inf": ("p", "Con el infinitivo, <b>pegado</b> al final en una sola palabra.", r"^\S+(?:ar|er|ir)(?:lo|la|los|las|le|les|me|te|nos|os)$"),
    "pos_ger": ("p", "Con el gerundio, <b>pegado</b> al final y con tilde.", r"^\S+(?:ándo|iéndo|yéndo)(?:lo|la|los|las|le|les|me|te|nos|os)$"),
    "pos_imp": ("p", "Imperativo afirmativo: <b>pegado</b> al final, casi siempre con tilde.", r"^\S*[áéíóú]\S*(?:lo|la|los|las|le|les|me|te|nos|os)$"),
}
TEXTOS = [
    {"id": "nuria", "tipo": "Escritura · tarea 1 · correo a una amiga", "titulo": "Correo a Nuria",
     "texto": "¡Hola, Nuria!<br>¡Qué bien, piso nuevo! Claro que [[te|le|la#dos]] ayudo con la mudanza. ¿Y el sofá? Mi hermano tiene una furgoneta: "
              "[[lo|le|la#paq_lo]] llevamos nosotros el sábado. Las cajas de libros pesan mucho, pero tranquila: voy a [[subirlas|las subir|subir las#pos_inf]] yo. "
              "¿Y tus padres? ¿Vienen? Si quieren, [[les|los|le#dest_les]] preparo algo de comer. Por cierto, ¿tienes ya las llaves del garaje? "
              "Yo [[las|les|los#paq_las]] necesito para dejar el coche dentro. [[Llámame|Llama me|Me llámame#pos_imp]] el viernes y hablamos.<br>Un beso,<br>Sara"},
    {"id": "bici", "tipo": "Escritura · tarea 2 · blog", "titulo": "La bici de mi abuela",
     "texto": "Cuando cumplí dieciocho años, mi abuela Rosa [[me|te|le#dos]] regaló una bicicleta roja. Era de segunda mano, pero mi abuelo y ella "
              "[[la|le|lo#paq_la]] arreglaron en su garaje y estaba como nueva. Al principio no me gustó mucho, pero ahora [[la|le|lo#paq_la]] uso todos los días "
              "para ir a la universidad. Mi abuela vive en otra ciudad y no [[la|le|lo#paq_la]] veo mucho, pero [[le|la|lo#dest_le]] mando fotos de mis paseos. "
              "Ella todavía tiene sus dos bicis viejas y [[las|les|los#paq_las]] cuida mucho. El mes que viene voy a [[visitarla|la visitar|visitar la#pos_inf]] "
              "y vamos a pasear juntas por el río."},
    {"id": "marcos", "tipo": "Oral · tarea 3 · planificar con un amigo", "titulo": "Una fiesta para Marcos",
     "texto": "<b>Examinadora:</b> ¿Organizamos una fiesta sorpresa para Marcos? Cumple treinta años.<br>"
              "<b>Candidato:</b> ¡Sí! ¿[[Lo|La|Les#paq_lo]] invitamos a cenar en tu casa?<br>"
              "<b>Examinadora:</b> Vale. ¿Y quién compra la tarta?<br>"
              "<b>Candidato:</b> [[La compro|Compro la|Comprarla#pos_conj]] yo. Conozco una pastelería muy buena.<br>"
              "<b>Examinadora:</b> ¿Y los amigos del trabajo?<br>"
              "<b>Candidato:</b> [[Les|Los|Le#dest_les]] escribo yo un mensaje esta noche. Tengo una lista de canciones: [[te|le|la#dos]] mando el enlace mañana.<br>"
              "<b>Examinadora:</b> Perfecto. Pero Marcos no puede saber nada: ¿quién lo trae a casa?<br>"
              "<b>Candidato:</b> Yo. Voy a [[recogerlo|lo recoger|recoger lo#pos_inf]] al trabajo a las ocho.<br>"
              "<b>Examinadora:</b> ¿Y el regalo?<br>"
              "<b>Candidato:</b> Estoy [[buscándolo|lo buscando|buscando lo#pos_ger]] en internet: algo de música."},
    {"id": "academia", "tipo": "Escritura · tarea 1 · correo de usted", "titulo": "A la academia Lenguas Vivas",
     "texto": "Estimada señora Pons:<br>[[Le|La|Te#usted]] escribo para pedir información sobre los cursos de verano. Vi su folleto en la biblioteca y "
              "[[lo|le|la#paq_lo]] leí con mucho interés. Quiero apuntar también a mis dos hijos: ¿[[los|les|las#paq_los]] puedo inscribir en el mismo grupo? "
              "Por favor, [[envíeme|me envíe|envíe me#pos_imp]] el formulario de inscripción y el horario. Si necesita mis datos, puede "
              "[[llamarme|me llamar|llamar me#pos_inf]] por la tarde. [[Le|La|Te#usted]] agradezco mucho su ayuda.<br>Atentamente,<br>Carlos Medina"},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
# pautas: (texto, [focos]); focos -> piezas
FOCOS = {"paquete": "lo / la / los / las", "dest": "le / les", "dos": "me / te", "pegado": "pegado: comprarlo"}
FOCO_FAM = {"paquete": "d", "dest": "i", "dos": "m", "pegado": "p"}
LAMINAS = [
    {"id": "lucia", "tarea": "Tarea 1 · correo a una amiga", "palabras": [60, 70],
     "intro": "Ha recibido este mensaje de su amiga Lucía:",
     "mensaje": "¡Hola! El sábado es el cumpleaños de mi madre y le preparamos una fiesta sorpresa. ¿Me ayudas? Necesito a alguien para comprar la tarta y las flores. Ah, ¿todavía tienes mi libro de fotografía? Besos, Lucía",
     "consigna": "Escriba un correo a Lucía. En él tiene que:",
     "pautas": [("saludar y decir si puede ayudarla;", ["dos"]),
                ("decir qué va a comprar usted y cuándo;", ["paquete", "pegado"]),
                ("proponer un regalo para su madre;", ["dest"]),
                ("contestar a su pregunta sobre el libro;", ["paquete"]),
                ("despedirse.", [])]},
    {"id": "persona", "tarea": "Tarea 2 · texto para una revista", "palabras": [70, 80],
     "intro": "Una revista para estudiantes de español busca textos sobre este tema:",
     "mensaje": "«Una persona que me ha ayudado mucho»",
     "consigna": "Escriba un texto para la revista. Hable de:",
     "pautas": [("quién es y cómo la conoció;", ["paquete"]),
                ("cómo era su vida en aquel momento;", []),
                ("qué le enseñó o qué le dijo esa persona;", ["dos"]),
                ("qué relación tienen ahora: cuándo la ve, qué hacen juntos;", ["paquete"]),
                ("qué va a hacer para darle las gracias.", ["dest", "pegado"])]},
]

# ------------------------------------------------------------------ DETECTOR (texto sin tildes, en minusculas)
_PRON = r"(?:lo|la|los|las|le|les|me|te|nos|os)"
_LO_NA = r"lo(?!\s+(?:que|mismo|mejor|peor|bueno|malo|mas|de|antes|importante|primero|siguiente|unico|normal|contrario)\b)"
_PRON_NA = r"(?:" + _LO_NA + r"|le|les|me|te|nos|os)"
_EXCL = (r"(?:ayer|mujer|lugar|mar|bar|par|hogar|taller|alquiler|placer|cualquier|sueter|poster|caracter|super|collar|azucar|dolar|"
         r"familiar|militar|regular|similar|particular|popular|nectar|bazar|oscar|pilar|edgar|omar|esther|ester|gaspar|baltasar|"
         r"cuando|fernando|orlando|armando|rolando|mando)")
_NEXT = r"(?:para|con|por|a|al|en|de|del|un|una|y|pero|porque|tambien|bien|mal|muy|mucho)"
_TIEMPO = (r"(?:manana|hoy|ahora|luego|pronto|esta (?:tarde|noche|semana)|"
           r"el (?:lunes|martes|miercoles|jueves|viernes|sabado|domingo|fin de semana)|en (?:el|la|casa)\b)")
_AUX = (r"(?:voy|vas|va|vamos|vais|van|iba|ibas|ibamos|iban|quiero|quieres|quiere|queremos|quieren|queria|puedo|puedes|puede|"
        r"podemos|pueden|podia|tengo|tienes|tiene|tenemos|tienen|tenia|estoy|estas|esta|estamos|estan|estaba|necesito|necesitas|"
        r"prefiero|pienso|debo|debes|debe)")
_CUE = (r"(?:a|que|voy|vas|va|vamos|vais|van|quiero|quieres|quiere|queremos|quieren|puedo|puedes|puede|podemos|pueden|estoy|estas|"
        r"esta|estamos|estan|debo|debes|necesito|prefiero)")
_DAR = (r"(?:dije|digo|dijimos|decimos|di|doy|dimos|damos|escribi|escribo|escribimos|mande|mando|mandamos|envie|regale|regalo|"
        r"regalamos|conte|cuento|contamos|explique|explico|ensene|enseno|pregunte|pregunto|preste|presto|devolvi|devuelvo|traje|"
        r"traigo|lleve|llevo|compre|compro|compramos)")
_TIEMPOS_OBJ = r"(?:semanas?|dias?|mes|meses|anos?|horas?|vez|veces|ratos?|tardes?|noches?|momentos?|minutos?)"
_NO_REP = (r"(?:manana|tarde|noche|semana|vez|veces|gente|mitad|verdad|hora|horas|lunes|martes|miercoles|jueves|viernes|"
           r"sabado|domingo|primera|segunda|ultima|mano|casa|derecha|izquierda)")
# s = se mira frase a frase (como en la pagina); x = se mira el texto entero
DETECTOR = [
    {"id": "suelto", "t": "r", "sc": "s",
     "re": (r"[a-z]\s+" + _PRON + r"\s*(?:[.,;:!?)]|$)|[a-z]\s+(?:lo|los|le|les|me|te|nos|os)\s+" + _TIEMPO +
            r"|[a-z]\s+(?:lo|los|le|les|me|te|nos|os)\s+(?:yo|tu|nosotros|nosotras|vosotros|vosotras|ellos|ellas)\b"),
     "msg": "Hay un pronombre <b>suelto</b> detrás de un verbo. Con un verbo conjugado va <b>delante</b> (lo compro); con el infinitivo, el gerundio o el imperativo, <b>pegado</b> (comprarlo, comprándolo, cómpralo)."},
    {"id": "en_medio", "t": "r", "sc": "s",
     "re": r"\b" + _CUE + r"\s+" + _PRON + r"\s+(?!" + _EXCL + r"\b)[a-z]+(?:ar|er|ir|ando|iendo|yendo)\b",
     "msg": "El pronombre está <b>en medio</b>. Ponlo delante del verbo conjugado (lo voy a comprar) o pegado al final (voy a comprarlo)."},
    {"id": "doble", "t": "r", "sc": "s",
     "re": r"\b(lo|la|los|las|le|les|me|te|nos|os)\s+" + _AUX + r"\s+(?:a\s+|que\s+)?[a-z]+(?:ar|er|ir|ando|iendo|yendo)\1\b",
     "msg": "El mismo pronombre sale <b>dos veces</b>. Elige un sitio: delante (lo voy a comprar) o pegado (voy a comprarlo)."},
    {"id": "inf_sep", "t": "r", "sc": "s",
     "re": r"\b(?!" + _EXCL + r"\b)[a-z]+(?:ar|er|ir)\s+" + _PRON_NA + r"\s+" + _NEXT + r"\b",
     "msg": "Detrás del infinitivo, el pronombre va <b>pegado</b>, en una sola palabra: escribirle, ayudarte, comprarlo."},
    {"id": "ger_sep", "t": "r", "sc": "s",
     "re": r"\b(?!" + _EXCL + r"\b)[a-z]+(?:ando|iendo|yendo)\s+" + _PRON_NA + r"\s+" + _NEXT + r"\b",
     "msg": "Detrás del gerundio, el pronombre va <b>pegado</b> (y con tilde): esperándote, comprándolo. O delante de estar: te estoy esperando."},
    {"id": "laismo", "t": "r", "sc": "s",
     "re": r"(?:^\s*|[^a-z\s]\s*|\b(?!(?:se|me|te|nos|os)\b)[a-z]+\s+)las?\s+" + _DAR + r"\s+(?!un[oa]?s?\s+" + _TIEMPOS_OBJ + r"\b)"
           r"(?:un|una|unos|unas|los|las|mi|mis|tu|tus|su|sus|nuestr[oa]s?|que|algo|nada|flores|fotos|regalos?)\b"
           r"|(?:^\s*|[^a-z\s]\s*|\b(?!(?:se|me|te|nos|os)\b)[a-z]+\s+)las?\s+(?:dije|digo|dijiste|dijimos|decimos)\s+a\b",
     "msg": "Aquí hay un paquete (lo que das, dices, escribes...) y una persona que lo recibe. Para la persona, <b>le / les</b>, también si es una mujer: <i>le dije</i>, <i>le escribo un correo</i>."},
    {"id": "gusta_lo", "t": "r", "sc": "s",
     "re": r"\b(?:lo|la|los|las)\s+(?:gusta|gustan|gustaba|gustaban|encanta|encantan|encantaba|interesa|interesan|duele|duelen)\b",
     "msg": "Con <b>gustar</b>, encantar, interesar o doler, siempre <b>le / les</b>: le gusta, les encanta (ficha R09)."},
    {"id": "repite", "t": "a", "sc": "x",
     "re": r"\b(?:el|la|los|las)\s+((?!" + _NO_REP + r"\b)[a-z]{4,})\b[^.!?]*[.!?]+[^.!?]*?\b(?:el|la|los|las)\s+\1\b",
     "msg": "Repites <b>el mismo nombre</b> en dos frases seguidas. ¿Puedes cambiar el segundo por <b>lo, la, los, las</b> o quitarlo?"},
]
# Para contar en el texto del estudiante (sin tildes, en minusculas). Es orientativo: la pagina lo dice.
CUENTA = {
    "d": (r"\b" + _LO_NA + r"\b|\b(?:la|las|los)\s+(?=(?:he|has|ha|hemos|han|voy|vas|va|vamos|van|tengo|tienes|tiene|tenemos|quiero|"
          r"quieres|puedo|puedes|podemos|estoy|estas|estamos|conoci|conozco|conoces|vi|veo|ves|llamo|llame|llamas|compro|compre|llevo|"
          r"lleve|traigo|traje|invito|invite|ayudo|espero|busco|hago|hice|necesito|uso|tenia|miro|visito|recojo|cuido|preparo|guardo|"
          r"echo|quiero|adoro|leo|lei)\b)|\b[a-z]+(?:ar|er|ir|ando|iendo|yendo)(?:lo|la|los|las)\b"),
    "i": r"\bles?\b|\b[a-z]+(?:ar|er|ir|ando|iendo|yendo)les?\b",
    "m": r"\b(?:me|te|nos|os)\b",
    "p": r"\b[a-z]+(?:ar|er|ir|ando|iendo|yendo)(?:lo|la|los|las|le|les|me|te|nos|os)\b",
}
# Pruebas: (texto, ids que tienen que saltar). El build las comprueba en Python y en node.
DETECTOR_PRUEBAS = [
    ("Compro lo mañana.", ["suelto"]),
    ("Voy a lo comprar el sábado.", ["en_medio"]),
    ("Lo voy a comprarlo.", ["doble"]),
    ("Tengo que escribir le un correo.", ["inf_sep"]),
    ("Estamos esperando te en la puerta.", ["ger_sep", "suelto"]),
    ("La dije que no podía ir.", ["laismo"]),
    ("Llama me esta tarde.", ["suelto"]),
    ("Mi abuela vive sola: la escribo un correo cada semana.", ["laismo"]),
    ("La gusta mucho el cine.", ["gusta_lo"]),
    ("Ayer compré la camiseta azul. La camiseta es muy bonita.", ["repite"]),
    ("Le voy a mandarle las fotos.", ["doble"]),
    ("¿El libro? Trae lo, por favor.", ["suelto"]),
    ("Ayer vi a Marta y la di un abrazo.", ["laismo"]),
    ("Voy a ayudar te con los deberes.", ["inf_sep"]),
    ("Tengo que la llamar esta tarde.", ["en_medio"]),
    ("¿Tu libro? Tengo lo yo.", ["suelto"]),
    ("La dije a tu madre que no.", ["laismo"]),
    # no tienen que saltar
    ("Lo compro mañana.", []),
    ("Voy a comprarlo mañana.", []),
    ("Lo voy a comprar el sábado.", []),
    ("Estoy haciéndolo ahora.", []),
    ("Llámame esta tarde.", []),
    ("Le dije que no podía ir.", []),
    ("Antes de salir te llamo.", []),
    ("Al llegar a casa le escribo un mensaje.", []),
    ("Me voy a casa a ducharme.", []),
    ("Voy a hacer lo que me dices.", []),
    ("Pilar me ha llamado. En el bar te espero.", []),
    ("Ayer lo vi en el mercado.", []),
    ("Se lo di a mi madre y me la devolvió ayer.", []),
    ("Por la mañana la llamo.", []),
    ("La compré una semana antes.", []),
    ("Le espero en la puerta, señor García. Le vi ayer.", []),
    ("Cuando me llames, te abro la puerta.", []),
    ("Estoy preparando la cena y voy a comprar los billetes.", []),
    ("Voy a la playa con mis amigos. Es para ti, no para él.", []),
    ("La casa de mis abuelos es grande. En la casa hay un jardín.", []),
    ("Le gusta mucho el cine y le encantan las series.", []),
    ("A la mujer le regalé unas flores.", []),
    ("¿La bici? La regalé a mi prima. Lo hago yo.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL (contesta sin repetir)
# q = lo que pregunta el examinador; dato = lo que tienes que decir; m = respuesta modelo marcada
ORAL = [
    {"q": "¿Quién compra las bebidas?", "dato": "tú", "m": "[d:Las] compro yo."},
    {"q": "¿Cuándo llamamos a Pedro?", "dato": "esta tarde", "m": "[d:Lo] llamamos esta tarde."},
    {"q": "¿Has invitado a Ana?", "dato": "sí, ayer", "m": "Sí, [d:la] invité ayer."},
    {"q": "¿Vas a traer la guitarra?", "dato": "sí", "m": "Sí, [d:la] voy a traer. / Sí, voy a [p:traerla]."},
    {"q": "¿Qué le regalamos a Pablo?", "dato": "un libro", "m": "[i:Le] regalamos un libro."},
    {"q": "¿Me llamas mañana?", "dato": "sí, por la mañana", "m": "Sí, [m:te] llamo por la mañana."},
    {"q": "¿Nos ayudas con la mudanza?", "dato": "sí, el sábado (a vosotros)", "m": "Sí, [m:os] ayudo el sábado."},
    {"q": "¿Dónde dejo las llaves?", "dato": "en la mesa (dale una instrucción)", "m": "[p:Déjalas] en la mesa."},
    {"q": "¿Puedo usar tu ordenador?", "dato": "sí, claro (dale permiso)", "m": "Sí, claro, [p:úsalo]."},
    {"q": "¿Quién recoge a los niños?", "dato": "tú", "m": "[d:Los] recojo yo."},
    {"q": "¿Has visto la exposición de fotos?", "dato": "no, todavía no", "m": "No, todavía no [d:la] he visto."},
    {"q": "¿Escribimos a los vecinos?", "dato": "sí, una nota", "m": "Sí, [i:les] escribimos una nota."},
    {"q": "¿Cuándo vas a hacer la reserva?", "dato": "esta noche", "m": "[d:La] voy a hacer esta noche. / Voy a [p:hacerla] esta noche."},
    {"q": "¿Estás preparando la cena?", "dato": "sí", "m": "Sí, [d:la] estoy preparando. / Sí, estoy [p:preparándola]."},
    {"q": "¿Conoces a mi hermana?", "dato": "no", "m": "No, no [d:la] conozco."},
    {"q": "¿Qué les decimos a los invitados?", "dato": "la hora y la dirección", "m": "[i:Les] decimos la hora y la dirección."},
]
