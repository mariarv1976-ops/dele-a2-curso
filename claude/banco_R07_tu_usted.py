# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R07: TU Y USTED, REGISTRO COHERENTE DEL SALUDO A LA DESPEDIDA (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R07_tu_usted.py
#
# ENFOQUE COGNITIVO (aprobado por Maria, 14/10): LA DISTANCIA Y EL CARRIL
#   1. LA DISTANCIA DECIDE: antes de saludar miras el hueco entre tu y la otra persona. Cerca (amigo,
#      familia, companero, un nino) -> TU. Un paso de distancia (el examinador en una tienda, la recepcion,
#      un desconocido mayor, un correo formal) -> USTED.
#   2. USTED HABLA COMO "EL / ELLA": usted es la persona que pones un paso mas alla, en la casilla de el o
#      ella; por eso sus formas son las de el: tiene, puede, le, su. Si no sabes la forma de usted, piensa
#      en "el". Formas fijas para aprender: con usted, a usted, perdone, oiga, mire, sientese.
#   3. EL CARRIL: al saludar eliges carril (tu naranja, usted azul) y no cambias hasta la despedida. Cada
#      senal del camino (verbo, te/le, tu/su, perdona/perdone, y tu?/y usted?) va en el mismo carril.
#      Cambiar de carril a mitad = el accidente (el error).
#
# MARCAS
#   [t:tienes]  tu (naranja)     [u:tiene]  usted (azul)     [n:Un saludo]  sirve para los dos (verde)
#   Huecos: [[correcta|distractor|distractor#motivo]]  (la primera es la buena; se barajan)
# Espanol de Espana. Ejemplos propios: ninguno sale de los materiales de Maria ni repite los ejemplos
# del kit (M3-1), la revision final (M3-4), los textos modelo (M3-5), la T3 (M4-3) o "Si me bloqueo".

# ------------------------------------------------------------------ MOTIVOS DE LOS HUECOS
# clave: (carril, explicacion, respuestas buenas posibles en minusculas)
MOTIVOS = {
    "saludo_t": ("tu", "Saludo de un correo a alguien cercano: <b>¡Hola, ...!</b> o <b>Querido / Querida</b> + nombre.", ["querido", "querida", "hola", "¡hola"]),
    "saludo_u": ("usted", "Saludo de un correo de usted: <b>Estimado / Estimada</b> + señor / señora + apellido.", ["estimado", "estimada"]),
    "desp_t": ("tu", "Despedida de tú: <b>Un abrazo</b>, <b>Un beso</b>, <b>Besos</b>.", ["un abrazo", "un beso", "besos"]),
    "desp_u": ("usted", "Despedida de usted: <b>Atentamente</b> o <b>Un cordial saludo</b>. Nada de besos ni abrazos.", ["atentamente", "un cordial saludo", "saludos cordiales"]),
    "verbo_t": ("tu", "El verbo de tú termina en <b>-s</b>: tienes, puedes, quieres, llegas.", ["puedes", "llegas", "quieres", "tienes", "prefieres", "traes", "eres", "sabes"]),
    "verbo_u": ("usted", "Usted habla como «él»: el verbo de él, <b>sin -s</b>: tiene, puede, quiere. Con ser: <b>es usted</b>.", ["tiene", "puede", "quiere", "es usted", "sabe"]),
    "pron_t": ("tu", "El pronombre de tú: <b>te</b> (te escribo), <b>ti</b> (para ti), <b>contigo</b>.", ["te", "ti", "contigo"]),
    "pron_u": ("usted", "El pronombre de usted es el de «él»: <b>le</b> (le escribo); después de para, a o con: <b>usted</b>.", ["le", "usted", "con usted"]),
    "pos_t": ("tu", "El posesivo de tú: <b>tu</b> / <b>tus</b> (tu correo, tu casa).", ["tu", "tus"]),
    "pos_u": ("usted", "El posesivo de usted es el de «él»: <b>su</b> / <b>sus</b> (su anuncio, su atención).", ["su", "sus"]),
    "imp_t": ("tu", "Para llamar la atención de alguien cercano: <b>oye</b>, <b>mira</b>, <b>perdona</b>.", ["oye", "mira", "perdona", "disculpa"]),
    "imp_u": ("usted", "Para llamar la atención con usted: <b>oiga</b>, <b>mire</b>, <b>perdone</b>, <b>disculpe</b>.", ["oiga", "mire", "perdone", "disculpe"]),
    "preg_t": ("tu", "Devuelves la pregunta en el mismo carril: <b>¿y tú?</b>", ["tú"]),
    "preg_u": ("usted", "Devuelves la pregunta en el mismo carril: <b>¿y usted?</b>", ["usted"]),
}
CARRILES = {"tu": "tú: cerca", "usted": "usted: a un paso"}

# ------------------------------------------------------------------ 1. LA DISTANCIA
# Personas para el selector: (quien, carril, por que)
PERSONAS = [
    ("Tu amigo Marcos", "tu", "Un amigo está cerca: tú. Con los amigos nunca usas usted."),
    ("Tu madre o tu abuela", "tu", "La familia está cerca: tú (en España, también con los abuelos)."),
    ("Tu compañera de piso", "tu", "Vivís juntas: tú."),
    ("Un compañero de clase o de trabajo", "tu", "En España, entre compañeros casi siempre tú, también con los mayores."),
    ("Un niño que se ha perdido", "tu", "A un niño siempre le hablas de tú, aunque no lo conozcas."),
    ("La dependienta de una zapatería", "usted", "Es un servicio y no la conoces: usted. (Si ella te habla de tú, puedes pasar a tú.)"),
    ("Un señor mayor en la calle", "usted", "Un desconocido mayor: usted, por respeto."),
    ("La recepcionista de una academia", "usted", "Le pides un servicio y no la conoces: usted."),
    ("La directora de una escuela (por correo)", "usted", "Un correo a alguien que no conoces, con un motivo formal: usted, del saludo a la despedida."),
    ("El conductor del autobús", "usted", "Un servicio y un desconocido: usted."),
]
# En el examen, la lamina te lo dice
LAMINA_DICE = [
    ("«El examinador es su amigo / su hermano / su compañero de piso».", "tu", "Oral, tarea 3 · planificar algo juntos"),
    ("«El examinador es el dependiente / el recepcionista / el camarero».", "usted", "Oral, tarea 3 · un servicio"),
    ("«Escriba un correo a su amiga Lucía...»", "tu", "Escritura, tarea 1"),
    ("«Escriba un correo a la señora Ferrer, de la academia...»", "usted", "Escritura, tarea 1"),
]

# El truco de el / ella: (tu, usted = el / ella)
EL_ELLA = [
    ("tú [t:tienes]", "usted [u:tiene]", "él [u:tiene]"),
    ("tú [t:puedes]", "usted [u:puede]", "ella [u:puede]"),
    ("tú [t:eres]", "usted [u:es]", "él [u:es]"),
    ("[t:te] llamo", "[u:le] llamo", "(a él) [u:le] llamo"),
    ("[t:te] llamas", "[u:se] llama", "él [u:se] llama"),
    ("[t:tu] casa", "[u:su] casa", "[u:su] casa (de él)"),
]
# Formas fijas: (tu, usted)
FIJAS = [
    ("[t:para ti] · [t:a ti]", "[u:para usted] · [u:a usted]"),
    ("[t:contigo]", "[u:con usted]"),
    ("[t:perdona] · [t:oye] · [t:mira]", "[u:perdone] · [u:oiga] · [u:mire]"),
    ("[t:espera] · [t:pasa] · [t:siéntate]", "[u:espere] · [u:pase] · [u:siéntese]"),
]

# ------------------------------------------------------------------ 2. EL CARRIL
# Todo lo que cambia: (pieza, tu, usted)
CAMBIA = [
    ("El verbo", "[t:tienes], [t:puedes], [t:eres], [t:estás]", "[u:tiene], [u:puede], [u:es], [u:está]"),
    ("Cómo te llamas", "¿Cómo [t:te llamas]?", "¿Cómo [u:se llama]?"),
    ("Te / le", "[t:te] escribo, [t:te] ayudo", "[u:le] escribo, [u:le] ayudo"),
    ("Después de para, a, de", "[t:para ti], [t:a ti]", "[u:para usted], [u:a usted]"),
    ("Con", "[t:contigo]", "[u:con usted]"),
    ("Los posesivos", "[t:tu] correo, [t:tus] hijos", "[u:su] correo, [u:sus] hijos"),
    ("Llamar la atención", "[t:perdona], [t:oye], [t:mira]", "[u:perdone], [u:oiga], [u:mire], [u:disculpe]"),
    ("Pedir o invitar", "[t:pasa], [t:siéntate], [t:espera]", "[u:pase], [u:siéntese], [u:espere]"),
    ("Devolver la pregunta", "¿[t:Y tú]? ¿Qué [t:te parece]?", "¿[u:Y usted]? ¿Qué [u:le parece]?"),
    ("Saludo del correo", "[t:¡Hola, Ana!] · [t:Querida Ana]:", "[u:Estimada señora Gil]:"),
    ("Despedida del correo", "[t:Un beso] · [t:Un abrazo]", "[u:Atentamente] · [u:Un cordial saludo]"),
]
PARA_LOS_DOS = "[n:Hola, buenos días] · [n:Un saludo] · [n:Muchas gracias] · [n:Hasta luego]"

# Cambia de carril: la misma frase en los dos carriles (mismo numero de marcas, en el mismo orden)
FRASES_CARRIL = [
    {"tema": "Un momento", "t": "¿[t:Tienes] un momento? [t:Te] quiero preguntar una cosa.", "u": "¿[u:Tiene] un momento? [u:Le] quiero preguntar una cosa."},
    {"tema": "La parada", "t": "[t:Perdona], ¿[t:sabes] dónde está la parada del 7?", "u": "[u:Perdone], ¿[u:sabe] dónde está la parada del 7?"},
    {"tema": "El paraguas", "t": "¡[t:Oye]! [t:Te has dejado] [t:tu] paraguas en la silla.", "u": "¡[u:Oiga]! [u:Se ha dejado] [u:su] paraguas en la silla."},
    {"tema": "La mesa", "t": "[t:Mira], esta es [t:tu] mesa. ¿Puedo sentarme [t:contigo]?", "u": "[u:Mire], esta es [u:su] mesa. ¿Puedo sentarme [u:con usted]?"},
    {"tema": "El regalo", "t": "Este regalo es [t:para ti]. ¿[t:Te gusta]?", "u": "Este regalo es [u:para usted]. ¿[u:Le gusta]?"},
    {"tema": "¿Y tú?", "t": "Yo quiero un café con leche. ¿[t:Y tú], qué [t:quieres]?", "u": "Yo quiero un café con leche. ¿[u:Y usted], qué [u:quiere]?"},
]

# ------------------------------------------------------------------ 3. LOS CORREOS
SALUDOS = {
    "tu": ["[t:¡Hola, Marta!]", "[t:Querida Marta]:", "[t:¡Hola!] ¿Qué tal todo?"],
    "usted": ["[u:Estimado señor Pons]:", "[u:Estimada señora Vidal]:", "[u:Estimados señores]:"],
    "dos": ["[n:Hola, buenos días]:", "[n:Buenos días]:"],
}
DESPEDIDAS = {
    "tu": ["[t:Un beso]", "[t:Un abrazo]", "[t:Besos] · [t:¡Hasta pronto!]"],
    "usted": ["[u:Atentamente]", "[u:Un cordial saludo]", "[u:Saludos cordiales]"],
    "dos": ["[n:Un saludo]", "[n:Muchas gracias]"],
}
# La misma peticion dos veces (Leo quiere comprar una bici de segunda mano)
DOS_CORREOS = {
    "tu": {"para": "A su amigo Iker", "texto": "[t:¡Hola, Iker!] ¿Qué tal [t:estás]? He visto que [t:vendes] [t:tu] bici. ¿Todavía la [t:tienes]? "
           "Me interesa mucho, porque ahora voy al trabajo andando y tardo casi una hora. ¿Cuánto [t:pides] por ella? ¿[t:Te va] bien el sábado por la mañana para verla? "
           "Si [t:quieres], [t:te] invito a un café en el bar de la plaza. ¡Muchas gracias!<br>[t:Un abrazo],<br>Leo"},
    "usted": {"para": "Al señor Mira, que vende su bici en internet", "texto": "[u:Estimado señor Mira]: He visto [u:su] anuncio de la bici. ¿Todavía la [u:tiene]? "
              "Me interesa mucho, porque ahora voy al trabajo andando y tardo casi una hora. ¿Cuánto [u:pide] por ella? ¿[u:Le va] bien el sábado por la mañana para verla? "
              "Si [u:quiere], [u:le] llamo por teléfono esta tarde y quedamos. Muchas gracias por [u:su] atención.<br>[n:Un saludo],<br>Leo Brandt"},
}

# ------------------------------------------------------------------ 4. EN EL EXAMEN
DONDE = [
    ("Escritura · tarea 1 (correo)", "La lámina te dice a quién escribes: a un amigo o a un familiar, tú; a una escuela, una tienda, un hotel o un vecino que no conoces, usted.",
     "[t:Querida Lucía]: [t:¡Gracias por tu invitación!] · [u:Estimada señora Ferrer]: [u:le] escribo porque..."),
    ("Oral · tarea 3 (diálogo)", "Planificar algo con un amigo, un hermano o un compañero de piso: tú. Un servicio (tienda, recepción, oficina): usted. El examinador hace ese papel.",
     "Planificar: ¿Qué [t:te parece] el sábado? · Servicio: [u:Perdone], ¿[u:tiene] esta camisa en azul?"),
    ("Oral · tareas 1 y 2", "Hablas de ti o de la foto. Si el examinador te pregunta algo, contesta en su trato: si te habla de usted, usted; si te habla de tú, tú.",
     "—¿Y usted tiene hermanos? —Sí, tengo dos. ¿[u:Y usted]?"),
    ("Las instrucciones del examen", "Las instrucciones siempre te hablan de usted («Escriba un correo...», «Usted va a escuchar...»). Eso NO decide el trato de tu correo: lo decide la persona a la que escribes.",
     "«Escriba un correo a su amigo Pablo» → tu correo, de [t:tú]."),
]
REGLA_ORO = "Regla de oro 8: en la escritura, el mismo trato del saludo a la despedida (tú o usted). Y en la revisión final, la pasada 2 mira solo eso."
# Errores tipicos: (mal, bien marcado, porque)
ERRORES = [
    ("¡Hola, Marta! ¿Qué tal estás? Te escribo para contarte una cosa. (...) Atentamente, Luis.",
     "[t:¡Hola, Marta!] ¿Qué tal [t:estás]? [t:Te] escribo para contarte una cosa. (...) [t:Un abrazo], Luis.",
     "Saludo de tú y despedida de usted. Si empiezas en el carril de tú, terminas en él: <b>un abrazo</b>, <b>un beso</b>."),
    ("Estimado señor Roig: le escribo para reservar una mesa para el sábado. (...) Un beso, Ana.",
     "[u:Estimado señor Roig]: [u:le] escribo para reservar una mesa para el sábado. (...) [u:Atentamente], Ana.",
     "Al revés: saludo de usted y despedida de tú. A alguien que no conoces no le mandas un beso: <b>atentamente</b> o <b>un saludo</b>."),
    ("Señora, ¿puedo ayudarte? ¿Usted busca algo?",
     "Señora, ¿puedo [u:ayudarle]? ¿[u:Busca usted] algo?",
     "Verbo y pronombre en carriles distintos. Con usted, el pronombre es el de «él»: <b>ayudarle</b> (nunca «ayudarte»)."),
    ("¿Puede usted ayudarte?",
     "¿[u:Puede usted ayudarle]? (a ella) · ¿[u:Puede usted ayudarme]? (a mí)",
     "<i>Puede usted</i> es de usted, pero <i>-te</i> es de tú: en la misma frase no pueden ir juntos."),
    ("Querido señor García: muchas gracias por todo. Un beso, Eva.",
     "[u:Estimado señor García]: muchas gracias por todo. [u:Atentamente], Eva.",
     "<i>Querido</i> es para alguien cercano; con <i>señor</i> + apellido, <b>Estimado</b>. Y la despedida, en el mismo carril."),
    ("Estimada Sra. López: ¿qué tal estás?",
     "[u:Estimada Sra. López]: ¿qué tal [u:está]?",
     "El saludo es de usted: el verbo también, el de «ella»: <b>está</b>."),
    ("Perdona, ¿tiene usted la tarjeta de la biblioteca? (a un cliente)",
     "[u:Perdone], ¿[u:tiene usted] la tarjeta de la biblioteca?",
     "A un cliente, usted: también al llamar su atención, <b>perdone</b>."),
    ("¡Oiga, Marcos! ¿Vienes al cine? (a un amigo)",
     "¡[t:Oye], Marcos! ¿[t:Vienes] al cine?",
     "A un amigo, tú: <b>oye</b>. <i>Oiga</i> es de usted y suena muy raro con un amigo."),
    ("Gracias por tu correo. ¿Cuándo es su cumpleaños? (el de tu amigo)",
     "Gracias por [t:tu] correo. ¿Cuándo es [t:tu] cumpleaños?",
     "<i>Su</i> y <i>tu</i> mezclados: si hablas del cumpleaños de tu amigo, <b>tu</b>. <i>Su</i> es de usted o de otra persona."),
]
# Claves de los errores pedidos por Maria (el build comprueba que salen en errores, bien/mal y detector)
REQ = ["atentamente", "un beso", "ayudarte", "querido señor", "qué tal estás", "perdona", "oiga", "su cumpleaños"]

# ------------------------------------------------------------------ EJERCICIOS
# 1. ¿Que dices? q = situacion, carril, o = [buena, otro carril, mezcla]
P_DICES = [
    {"q": "En una zapatería, a la dependienta:", "c": "usted", "o": ["Perdone, ¿tiene estas botas en el 38?", "Perdona, ¿tienes estas botas en el 38?", "Perdone, ¿tienes estas botas en el 38?"],
     "why": "Un servicio, alguien que no conoces: usted. <i>Perdone</i> y <i>tiene</i>, los dos en el mismo carril."},
    {"q": "A tu compañero de piso:", "c": "tu", "o": ["Oye, ¿has visto mis llaves?", "Oiga, ¿ha visto mis llaves?", "Oiga, ¿has visto mis llaves?"],
     "why": "Vivís juntos: tú. <i>Oye</i> y <i>has visto</i>."},
    {"q": "En la calle, a un señor mayor que no conoces:", "c": "usted", "o": ["Perdone, ¿sabe a qué hora pasa el autobús?", "Perdona, ¿sabes a qué hora pasa el autobús?", "Perdone, ¿sabes a qué hora pasa el autobús?"],
     "why": "Un desconocido mayor: usted. El verbo, sin -s: <i>sabe</i>."},
    {"q": "Empiezas un correo a la directora de una escuela que no conoces:", "c": "usted", "o": ["Estimada señora Pons: le escribo para pedir información.", "Querida Laura: te escribo para pedir información.", "Estimada señora Pons: te escribo para pedir información."],
     "why": "Correo formal: <i>Estimada</i> + <i>le escribo</i>. <i>Te escribo</i> es de tú."},
    {"q": "Terminas un correo a tu prima:", "c": "tu", "o": ["¡Escríbeme pronto! Un beso.", "Quedo a la espera de su respuesta. Atentamente.", "¡Escríbeme pronto! Atentamente."],
     "why": "A tu prima, todo de tú: <i>escríbeme</i> y <i>un beso</i>."},
    {"q": "En la recepción de tu academia de idiomas:", "c": "usted", "o": ["Buenos días. ¿Me puede dar el horario de las clases?", "Hola, ¿me puedes dar el horario de las clases?", "Disculpe, ¿me puedes dar el horario de las clases?"],
     "why": "Un servicio: usted. <i>Disculpe</i> va con <i>puede</i>, no con <i>puedes</i>."},
    {"q": "En la tarea 3, el examinador es tu hermano:", "c": "tu", "o": ["¿Qué te parece si vamos el domingo?", "¿Qué le parece si vamos el domingo?", "¿Qué te parece si usted viene el domingo?"],
     "why": "Con tu hermano, tú: <i>¿qué te parece?</i>. <i>Usted</i> no va nunca con <i>te</i>."},
    {"q": "En la tarea 3, el examinador es el vendedor de una tienda de bicis:", "c": "usted", "o": ["¿Puede decirme cuánto cuesta esta bici?", "¿Puedes decirme cuánto cuesta esta bici?", "Perdone, ¿puedes decirme cuánto cuesta esta bici?"],
     "why": "Un servicio: usted. <i>Puede</i>, el verbo de «él»."},
    {"q": "A un niño de seis años que se ha perdido:", "c": "tu", "o": ["¿Cómo te llamas? ¿Dónde está tu mamá?", "¿Cómo se llama usted? ¿Dónde está su madre?", "¿Cómo se llama usted? ¿Dónde está tu mamá?"],
     "why": "A un niño siempre le hablas de tú: <i>te llamas</i>, <i>tu mamá</i>."},
    {"q": "Al conductor del autobús:", "c": "usted", "o": ["Perdone, ¿me avisa en la parada de la playa?", "Perdona, ¿me avisas en la parada de la playa?", "Perdone, ¿me avisas en la parada de la playa?"],
     "why": "Un servicio y un desconocido: usted. <i>Perdone</i> + <i>avisa</i>."},
    {"q": "A una compañera de clase:", "c": "tu", "o": ["¿Me dejas tus apuntes de ayer?", "¿Me deja sus apuntes de ayer?", "Disculpe, ¿me dejas tus apuntes de ayer?"],
     "why": "Entre compañeros, tú: <i>dejas</i>, <i>tus</i>."},
    {"q": "A una vecina mayor que lleva unas bolsas muy pesadas:", "c": "usted", "o": ["¿Le ayudo con las bolsas, señora?", "¿Te ayudo con las bolsas?", "Oiga, ¿te ayudo con las bolsas?"],
     "why": "Una señora mayor que no conoces bien: usted. El pronombre de «ella»: <i>le</i>."},
    {"q": "El examinador, que es tu amigo, te pregunta: «¿Qué haces el sábado?»", "c": "tu", "o": ["Nada especial. ¿Y tú?", "Nada especial. ¿Y usted?", "Nada especial, ¿y usted? ¿Vienes conmigo?"],
     "why": "Devuelves la pregunta en el mismo carril: <i>¿y tú?</i>"},
    {"q": "Te despides del examinador, que es el dependiente de una tienda:", "c": "usted", "o": ["Muchas gracias. Que tenga un buen día.", "Muchas gracias. ¡Que tengas un buen día!", "Muchas gracias, es usted muy amable. ¡Que tengas un buen día!"],
     "why": "La despedida, en el carril de usted hasta el final: <i>que tenga</i>."},
]
# 2. Cambia de carril: q = frase, d = a que carril pasas, o = [buena, a medias, mal]
P_CARRIL = [
    {"q": "¿Tienes un momento?", "d": "usted", "o": ["¿Tiene un momento?", "¿Tienes usted un momento?", "¿Tienen un momento?"], "why": "Usted habla como «él»: <i>tiene</i>. <i>Tienen</i> es de ellos (o de ustedes)."},
    {"q": "Perdona, ¿sabes dónde está el museo?", "d": "usted", "o": ["Perdone, ¿sabe dónde está el museo?", "Perdone, ¿sabes dónde está el museo?", "Perdonad, ¿sabéis dónde está el museo?"], "why": "Cambian las dos piezas: <i>perdone</i> y <i>sabe</i>. <i>Perdonad, sabéis</i> es vosotros."},
    {"q": "Te llamo mañana.", "d": "usted", "o": ["Le llamo mañana.", "Usted llamo mañana.", "Te llama mañana."], "why": "El pronombre de usted es el de «él»: <i>le</i>. El verbo sigue siendo el tuyo: <i>llamo</i>."},
    {"q": "¿Es tu coche?", "d": "usted", "o": ["¿Es su coche?", "¿Es tu coche, señor?", "¿Es suyo coche?"], "why": "El posesivo de usted: <i>su</i>. Con «señor» y <i>tu</i> mezclas los carriles."},
    {"q": "Oye, ¿vienes con nosotros?", "d": "usted", "o": ["Oiga, ¿viene con nosotros?", "Oiga, ¿vienes con nosotros?", "Oye, ¿viene con nosotros?"], "why": "Todo cambia a la vez: <i>oiga</i> y <i>viene</i>."},
    {"q": "Esto es para ti.", "d": "usted", "o": ["Esto es para usted.", "Esto es para le.", "Esto es para su."], "why": "Después de <i>para</i>, <i>a</i> o <i>de</i>: <b>usted</b>."},
    {"q": "¿Puedo ir contigo?", "d": "usted", "o": ["¿Puedo ir con usted?", "¿Puedo ir consigo?", "¿Puedo ir con le?"], "why": "<i>Contigo</i> pasa a <b>con usted</b>."},
    {"q": "Mira, aquí tienes tu billete.", "d": "usted", "o": ["Mire, aquí tiene su billete.", "Mire, aquí tiene tu billete.", "Mira, aquí tiene su billete."], "why": "Tres piezas: <i>mire</i>, <i>tiene</i>, <i>su</i>. Si cambias dos, el coche sigue entre dos carriles."},
    {"q": "¿Cómo te llamas?", "d": "usted", "o": ["¿Cómo se llama?", "¿Cómo le llama?", "¿Cómo te llama?"], "why": "Como «él»: <i>él se llama</i> → <i>usted se llama</i>."},
    {"q": "¿Le apetece un café?", "d": "tu", "o": ["¿Te apetece un café?", "¿Tú apetece un café?", "¿Te apeteces un café?"], "why": "Al revés: el pronombre de usted (<i>le</i>) pasa a <b>te</b>. <i>Apetece</i> no cambia: lo que apetece es el café."},
    {"q": "Disculpe, ¿es usted la profesora de baile?", "d": "tu", "o": ["Perdona, ¿eres tú la profesora de baile?", "Disculpe, ¿eres tú la profesora de baile?", "Perdona, ¿es tú la profesora de baile?"], "why": "Al pasar a tú, cambian <i>perdona</i>, <i>eres</i> y <i>tú</i>."},
    {"q": "Siéntese, por favor: está en su casa.", "d": "tu", "o": ["Siéntate, por favor: estás en tu casa.", "Siéntate, por favor: está en su casa.", "Siéntese, por favor: estás en tu casa."], "why": "Todo al carril de tú: <i>siéntate</i>, <i>estás</i>, <i>tu</i>."},
]
# 4. Bien o mal: ok 0 = bien, 1 = mal
E_BIENMAL = [
    {"q": "¡Hola, Marta! ¿Qué tal estás? (...) Atentamente, Luis.", "ok": 1, "fix": "¡Hola, Marta! ¿Qué tal estás? (...) <b>Un abrazo</b>, Luis.", "why": "Saludo de tú y despedida de usted."},
    {"q": "Estimado señor Roig: le escribo para reservar una mesa. (...) Un beso, Ana.", "ok": 1, "fix": "Estimado señor Roig: le escribo para reservar una mesa. (...) <b>Atentamente</b>, Ana.", "why": "Saludo de usted y despedida de tú."},
    {"q": "¿Puede usted ayudarte?", "ok": 1, "fix": "¿Puede usted <b>ayudarle</b>? / ¿Puede usted <b>ayudarme</b>?", "why": "<i>Usted</i> y <i>-te</i> en la misma frase."},
    {"q": "Querido señor García: muchas gracias por todo. Un beso.", "ok": 1, "fix": "<b>Estimado</b> señor García: muchas gracias por todo. <b>Atentamente</b>.", "why": "<i>Querido</i> y <i>un beso</i> no van con «señor García»."},
    {"q": "Estimada Sra. López: ¿qué tal estás?", "ok": 1, "fix": "Estimada Sra. López: ¿qué tal <b>está</b>?", "why": "Saludo de usted: el verbo también, sin -s."},
    {"q": "Perdona, ¿tiene usted la tarjeta de la biblioteca?", "ok": 1, "fix": "<b>Perdone</b>, ¿tiene usted la tarjeta de la biblioteca?", "why": "Con usted: perdone."},
    {"q": "¡Oiga, Marcos! ¿Vienes al cine?", "ok": 1, "fix": "¡<b>Oye</b>, Marcos! ¿Vienes al cine?", "why": "A un amigo: oye."},
    {"q": "Gracias por tu correo. ¿Cuándo es su cumpleaños, Pablo?", "ok": 1, "fix": "Gracias por tu correo. ¿Cuándo es <b>tu</b> cumpleaños, Pablo?", "why": "Hablas con Pablo de tú: tu cumpleaños."},
    {"q": "Disculpe, ¿me dejas tu bolígrafo?", "ok": 1, "fix": "Disculpe, ¿me <b>deja su</b> bolígrafo?", "why": "<i>Disculpe</i> es de usted; <i>dejas</i> y <i>tu</i>, de tú."},
    {"q": "Estimada señora Pons: le escribo para pedir información sobre su curso. Atentamente, Kenji.", "ok": 0, "fix": "", "why": "Correcto: todo de usted, del saludo a la despedida."},
    {"q": "¡Hola, Iker! He visto que vendes tu bici. ¿Te va bien el sábado? Un abrazo.", "ok": 0, "fix": "", "why": "Correcto: todo de tú."},
    {"q": "Buenos días. ¿Tiene estas botas en el 38? Muchas gracias.", "ok": 0, "fix": "", "why": "Correcto: usted, y «buenos días» y «gracias» sirven para los dos."},
    {"q": "¿Quiere usted un té con leche?", "ok": 0, "fix": "", "why": "Correcto: <i>té</i> es la bebida, no el pronombre de tú."},
    {"q": "Mi abuelo me dio su reloj. Ahora es mío.", "ok": 0, "fix": "", "why": "Correcto: <i>su</i> también es de «él»: el reloj de mi abuelo."},
]

# 3. Textos con huecos (pueden llevar <br> y <b>); c = carril del texto (todos sus huecos son de ese carril)
TEXTOS = [
    {"id": "joel", "c": "tu", "tipo": "Escritura · tarea 1 · correo a un amigo", "titulo": "Correo a Joel",
     "texto": "[[Querido|Estimado|Distinguido#saludo_t]] Joel:<br>¡Qué alegría! Gracias por [[tu|su|vuestro#pos_t]] correo. Claro que [[puedes|puede|podéis#verbo_t]] dormir en mi casa en mayo: hay una habitación libre para [[ti|usted|vosotros#pron_t]]. "
              "¿Qué día [[llegas|llega|llegan#verbo_t]]? Si [[quieres|quiere|queréis#verbo_t]], [[te|le|os#pron_t]] recojo en la estación. [[Oye|Oiga|Oigan#imp_t]], ¿[[tienes|tiene|tenéis#verbo_t]] bicicleta? Aquí es la mejor forma de moverse. "
              "¿Y [[tú|usted|vosotros#preg_t]], qué [[prefieres|prefiere|preferís#verbo_t]]: playa o montaña?<br>[[Un abrazo|Atentamente|Un cordial saludo#desp_t]],<br>Mateo"},
    {"id": "kenji", "c": "usted", "tipo": "Escritura · tarea 1 · correo de usted", "titulo": "Clases de cerámica",
     "texto": "[[Estimada|Querida|Hola#saludo_u]] señora Lladó:<br>Me llamo Kenji Sato y [[le|te|os#pron_u]] escribo porque he visto [[su|tu|vuestro#pos_u]] anuncio de clases de cerámica para adultos. "
              "Me gustaría saber si [[tiene|tienes|tenéis#verbo_u]] plazas en el grupo de los martes. ¿[[Puede|Puedes|Podéis#verbo_u]] decirme también cuánto cuesta el curso? "
              "[[Disculpe|Disculpa|Perdona#imp_u]] tantas preguntas. Muchas gracias por [[su|tu|vuestra#pos_u]] atención.<br>[[Atentamente|Un beso|Un abrazo#desp_u]],<br>Kenji Sato"},
    {"id": "juegos", "c": "tu", "tipo": "Oral · tarea 3 · planificar con un amigo", "titulo": "Una tarde de juegos",
     "texto": "<b>Examinadora:</b> ¿Organizamos una tarde de juegos de mesa?<br>"
              "<b>Candidato:</b> ¡Buena idea! ¿[[Te|Le|Os#pron_t]] parece bien el viernes?<br>"
              "<b>Examinadora:</b> El viernes no puedo, tengo clase.<br>"
              "<b>Candidato:</b> Vale, pues el sábado. ¿[[Tienes|Tiene|Tenéis#verbo_t]] juegos en casa?<br>"
              "<b>Examinadora:</b> Sí, tengo tres o cuatro.<br>"
              "<b>Candidato:</b> Perfecto: tú [[traes|trae|traen#verbo_t]] los juegos y yo compro algo para merendar. [[Mira|Mire|Miren#imp_t]], podemos invitar también a [[tu|su|vuestra#pos_t]] hermana.<br>"
              "<b>Examinadora:</b> ¡Sí! Le va a encantar.<br>"
              "<b>Candidato:</b> Genial. Entonces voy a [[tu|su|vuestra#pos_t]] casa a las cinco. ¿Y [[tú|usted|vosotros#preg_t]], invitas a alguien más?"},
    {"id": "optica", "c": "usted", "tipo": "Oral · tarea 3 · un servicio", "titulo": "En la óptica",
     "texto": "<b>Examinador:</b> Buenos días. ¿Qué tal?<br>"
              "<b>Candidata:</b> Bien, gracias, ¿y [[usted|tú|vosotros#preg_u]]? Mire, se me han roto las gafas. ¿[[Puede|Puedes|Pueden#verbo_u]] arreglarlas hoy?<br>"
              "<b>Examinador:</b> Hoy es difícil. ¿Las necesita para trabajar?<br>"
              "<b>Candidata:</b> Sí, para conducir. [[Perdone|Perdona|Perdonad#imp_u]], ¿[[tiene|tienes|tenéis#verbo_u]] unas gafas para dejarme hasta mañana?<br>"
              "<b>Examinador:</b> Sí, claro. Aquí tiene.<br>"
              "<b>Candidata:</b> Muchas gracias, [[es usted|eres|sois#verbo_u]] muy amable. ¿[[Le|Te|Os#pron_u]] va bien si vengo mañana a las diez?<br>"
              "<b>Examinador:</b> Perfecto. Hasta mañana.<br>"
              "<b>Candidata:</b> Hasta mañana. ¡Que [[le|te|os#pron_u]] vaya bien!"},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
# pautas: (texto, [focos]); focos: saludo, verbo, pron, pos, preg, desp
FOCOS = {"saludo": "saludo", "verbo": "verbo", "pron": "te / le", "pos": "tu / su", "preg": "pregunta", "desp": "despedida"}
LAMINAS = [
    {"id": "noa", "c": "tu", "tarea": "Tarea 1 · correo a una amiga", "palabras": [60, 70],
     "intro": "Ha recibido este mensaje de su amiga Noa:",
     "mensaje": "¡Hola! ¡Tengo una noticia! En junio me mudo a tu ciudad por trabajo. Busco piso y no conozco a nadie. ¿Me ayudas? ¿Qué barrio me recomiendas? Un beso, Noa",
     "consigna": "Escriba un correo a Noa. En él tiene que:",
     "pautas": [("saludar;", ["saludo"]),
                ("decir que se alegra y ofrecerle ayuda;", ["pron", "verbo"]),
                ("recomendarle un barrio y decir por qué;", ["verbo"]),
                ("preguntarle cuándo llega y si necesita algo más;", ["preg", "verbo"]),
                ("despedirse.", ["desp"])]},
    {"id": "compas", "c": "usted", "tarea": "Tarea 1 · correo de usted", "palabras": [60, 70],
     "intro": "Ha visto este anuncio en su barrio:",
     "mensaje": "ACADEMIA COMPÁS · Clases de baile para adultos: salsa, flamenco y tango. Grupos de mañana y de tarde. Información: Sra. Ferrer (info@academiacompas.es)",
     "consigna": "Escriba un correo a la señora Ferrer. En él tiene que:",
     "pautas": [("saludar;", ["saludo"]),
                ("presentarse y decir por qué escribe;", ["pron", "pos"]),
                ("preguntar por los horarios y el precio;", ["verbo", "preg"]),
                ("preguntar si puede hacer una clase de prueba;", ["verbo"]),
                ("agradecer y despedirse.", ["pos", "desp"])]},
]

# ------------------------------------------------------------------ DETECTOR DE MEZCLA (texto sin tildes, en minusculas)
# Palabras que solo son de un carril. Ojo: su, le, tiene... NO estan, porque tambien son de el / ella.
_V2 = (r"(?:tienes|puedes|quieres|sabes|eres|vienes|vas|has|haces|necesitas|prefieres|llegas|traes|vendes|pides|estudias|trabajas|vives|dices|piensas|"
       r"tengas|vengas|puedas|quieras|dejas|avisas|invitas|conoces|ayudas|llamas)")
_TEV = (r"(?:escribo|llamo|llamas|veo|espero|mando|envio|invito|ayudo|digo|cuento|pregunto|gusta|gustan|parece|apetece|va|vaya|has|he|quiero|puedo|"
        r"recomiendo|echo|presento|llevo|acompano|interesa|queda|quedan|importa|recojo|dejo|aviso|debo|alegras|vienes|olvides|acuerdas)")
_CLIT = (r"(?:ayudar|llamar|escribir|ver|decir|preguntar|invitar|esperar|enviar|mandar|contar|explicar|recoger|conocer|visitar|acompanar|dar|avisar|presentar)")
TU_RX = [r"\btus?\b", r"\bti\b", r"\bcontigo\b", r"\btuy[oa]s?\b", r"\bte\s+" + _TEV + r"\b", r"\b" + _CLIT + r"te\b", r"\b" + _V2 + r"\b",
         r"\b(?:que tal|como)\s+estas\b", r"\b(?:oye|perdona|disculpa|mira|espera|perdoname)\s*[,!]", r"\b(?:sientate|escribeme|llamame|dime|avisame|cuentame)\b",
         r"\bquerid[oa]s?\b", r"\b(?:un beso|besos|un abrazo|abrazos|besitos)\b"]
US_RX = [r"\busted(?:es)?\b", r"\bestimad[oa]s?\b", r"\batentamente\b", r"\bcordial(?:es)?\b", r"\b(?:perdone|disculpe|oiga|sientese|digame|pase|espere)\b",
         r"\bmire\s*[,!]", r"\b(?:sr|sra|srta)\b", r"\bque tenga\b"]
_TU = "(?:" + "|".join(TU_RX) + ")"
_US = "(?:" + "|".join(US_RX) + ")"
_TUW = r"(?:\b" + _V2 + r"\b|\bte\b|\bti\b|\bcontigo\b|\btus?\b|\b" + _CLIT + r"te\b)"
# s = se mira frase a frase (como en la pagina); x = se mira el texto entero
DETECTOR = [
    {"id": "usted_tu", "t": "r", "sc": "s", "re": r"\busted(?:es)?\b[^.!?]*" + _TU + r"|" + _TU + r"[^.!?]*\busted(?:es)?\b",
     "msg": "En la misma frase hay <b>usted</b> y una palabra de <b>tú</b>. Elige un carril: ¿puede usted ayudar<b>le</b>? · ¿puedes ayudar<b>te</b>?"},
    {"id": "imp_mezcla", "t": "r", "sc": "s", "re": r"\b(?:perdone|disculpe|oiga|mire)\b[^.!?]*" + _TUW,
     "msg": "Empiezas con <b>perdone / disculpe / oiga</b> (usted) y sigues con una palabra de tú. Con usted: perdone, ¿<b>tiene</b>...?"},
    {"id": "querido_senor", "t": "r", "sc": "s", "re": r"\bquerid[oa]s?\s+(?:senor|senora|senores|sr|sra|director|directora)\b",
     "msg": "<b>Querido / Querida</b> es para alguien cercano. Con señor / señora + apellido: <b>Estimado / Estimada</b>."},
    {"id": "mezcla", "t": "r", "sc": "x", "re": r"^(?=(?:.|\n)*" + _TU + r")(?=(?:.|\n)*" + _US + r")",
     "msg": "En tu texto hay palabras de los dos carriles. Del saludo a la despedida, todo de <b>tú</b> o todo de <b>usted</b>."},
    {"id": "beso_formal", "t": "r", "sc": "x", "re": r"^(?=(?:.|\n)*\b(?:estimad[oa]s?|sra?|srta)\b)(?=(?:.|\n)*\b(?:un beso|besos|un abrazo|abrazos)\b)",
     "msg": "Saludo de usted (<b>Estimado...</b>) y despedida de tú (<b>un beso, un abrazo</b>). Con usted: <b>Atentamente</b> o <b>Un saludo</b>."},
    {"id": "formal_estas", "t": "r", "sc": "x", "re": r"^(?=(?:.|\n)*\b(?:estimad[oa]s?|sra?|srta)\b)(?=(?:.|\n)*\b(?:que tal|como)\s+estas\b)",
     "msg": "El saludo es de usted, pero <b>¿qué tal estás?</b> es de tú. Con usted: <b>¿qué tal está?</b>"},
    {"id": "saludo_atent", "t": "a", "sc": "x", "re": r"^(?=(?:.|\n)*\b(?:querid[oa]s?|hola)\b)(?=(?:.|\n)*\b(?:atentamente|saludos cordiales|un cordial saludo)\b)",
     "msg": "Empiezas con <b>Hola</b> o <b>Querido/a</b> y terminas con <b>Atentamente</b>. ¿Es un correo de tú? Entonces: un abrazo, un beso. ¿De usted? Entonces: Estimado/a..."},
    {"id": "su_y_tu", "t": "a", "sc": "x", "re": r"^(?=(?:.|\n)*" + _TU + r")(?=(?:.|\n)*\bsus?\b)",
     "msg": "Escribes de tú, pero hay un <b>su</b>. ¿Es de otra persona (su hermana = la hermana de él)? Bien. ¿Es de la persona a la que escribes? Entonces es <b>tu</b>."},
]
# Pruebas: (texto, ids que tienen que saltar). El build las comprueba en Python y en node.
DETECTOR_PRUEBAS = [
    ("¡Hola, Marta! ¿Qué tal estás? Te escribo para contarte una cosa. Atentamente, Luis.", ["mezcla", "saludo_atent"]),
    ("Estimado señor Roig: le escribo para reservar una mesa. Un beso, Ana.", ["beso_formal", "mezcla"]),
    ("Señora, ¿puedo ayudarte? ¿Usted busca algo?", ["mezcla"]),
    ("¿Puede usted ayudarte?", ["mezcla", "usted_tu"]),
    ("Querido señor García: muchas gracias por todo. Un beso.", ["querido_senor"]),
    ("Querida señora Vidal: le escribo porque quiero información.", ["querido_senor"]),
    ("Estimada Sra. López: ¿qué tal estás?", ["formal_estas", "mezcla"]),
    ("Perdona, ¿tiene usted la tarjeta de la biblioteca?", ["mezcla", "usted_tu"]),
    ("¡Oiga, Marcos! ¿Vienes al cine?", ["mezcla"]),
    ("Oiga, ¿vienes al cine con nosotros?", ["imp_mezcla", "mezcla"]),
    ("Gracias por tu correo. ¿Cuándo es su cumpleaños?", ["su_y_tu"]),
    ("Disculpe, ¿me dejas tu bolígrafo?", ["imp_mezcla", "mezcla"]),
    ("Hola, buenos días. Quería información sobre las clases. Atentamente, Eva.", ["saludo_atent"]),
    ("Estimada señora Pons: le escribo para pedir información sobre su curso. Muchas gracias por su atención. Atentamente, Kenji.", []),
    ("¡Hola, Iker! ¿Qué tal estás? He visto que vendes tu bici. Un abrazo.", []),
    ("¿Quiere usted un té con leche?", []),
    ("Mi abuelo me dio su reloj.", []),
    ("Te llamo mañana y te cuento.", []),
    ("Buenos días. ¿Tiene estas botas en el 38? Muchas gracias. Que tenga un buen día.", []),
    ("Mira las fotos de estas vacaciones.", []),
    ("Ella mira, pero no dice nada.", []),
    ("Un saludo, Leo.", []),
    ("Pase, por favor: está en su casa.", []),
    ("Hola, Ana: ¿qué tal? Mi hermano y su novia vienen a verme.", []),
    ("Le escribo porque he visto su anuncio. ¿Le va bien el sábado?", []),
    ("Mi madre tiene un perro y le encanta pasear.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL (la misma peticion dos veces)
# sit = lo que quieres decir; a = a quien de tu; b = a quien de usted; mt / mu = modelos marcados
ORAL = [
    {"sit": "Necesitas un bolígrafo un momento.", "a": "a tu compañero de clase", "b": "al examinador, que trabaja en una oficina", "mt": "[t:Oye], ¿me [t:dejas] [t:tu] boli un momento?", "mu": "[u:Perdone], ¿me [u:deja] [u:su] bolígrafo un momento?"},
    {"sit": "Buscas la calle Sagasta.", "a": "a una amiga", "b": "a un señor mayor en la calle", "mt": "[t:Perdona], ¿[t:sabes] dónde está la calle Sagasta?", "mu": "[u:Perdone], ¿[u:sabe] dónde está la calle Sagasta?"},
    {"sit": "Habla muy rápido y no entiendes.", "a": "a tu vecino de tu edad", "b": "a la recepcionista de una academia", "mt": "¿[t:Puedes] hablar más despacio, por favor? No [t:te] entiendo.", "mu": "¿[u:Puede] hablar más despacio, por favor? No [u:le] entiendo."},
    {"sit": "Necesitas cambio de veinte euros.", "a": "a tu hermano", "b": "al dependiente de un quiosco", "mt": "[t:Oye], ¿[t:tienes] cambio de veinte euros?", "mu": "[u:Perdone], ¿[u:tiene] cambio de veinte euros?"},
    {"sit": "Quieres ayudar con una maleta muy grande.", "a": "a un amigo", "b": "a una señora en la estación", "mt": "¿[t:Te] ayudo con la maleta?", "mu": "¿[u:Le] ayudo con la maleta?"},
    {"sit": "Quieres saber su nombre.", "a": "a un chico nuevo en tu clase", "b": "al examinador, que es el nuevo director", "mt": "Hola, ¿cómo [t:te llamas]?", "mu": "Buenos días, ¿cómo [u:se llama usted]?"},
    {"sit": "Se ha olvidado las llaves en la mesa.", "a": "a tu compañera de piso", "b": "a un cliente del bar donde trabajas", "mt": "¡[t:Oye]! [t:Te has dejado] las llaves en la mesa.", "mu": "¡[u:Oiga]! [u:Se ha dejado] las llaves en la mesa."},
    {"sit": "Le ofreces una silla.", "a": "a tu abuela", "b": "a un señor que espera en tu oficina", "mt": "[t:Siéntate] aquí, si [t:quieres].", "mu": "[u:Siéntese] aquí, si [u:quiere]."},
    {"sit": "Hace calor: quieres abrir la ventana.", "a": "a tu compañero de trabajo", "b": "a una señora en el tren", "mt": "¿[t:Te importa] si abro la ventana?", "mu": "¿[u:Le importa] si abro la ventana?"},
    {"sit": "Te ha dejado un paraguas: das las gracias.", "a": "a tu prima", "b": "a la dependienta de una tienda", "mt": "¡Mil gracias por el paraguas! [t:Eres] un sol.", "mu": "Muchísimas gracias por el paraguas: [u:es usted] muy amable."},
    {"sit": "Quieres saber su opinión sobre el plan.", "a": "a tu amigo (tarea 3: planificar)", "b": "al examinador, que es un agente de viajes", "mt": "Yo prefiero el tren. ¿[t:Y tú] qué [t:piensas]?", "mu": "Yo prefiero el tren. ¿[u:Y usted] qué [u:piensa]?"},
    {"sit": "Te despides hasta mañana.", "a": "a una compañera de clase", "b": "al señor de la biblioteca", "mt": "¡Hasta mañana! Que [t:te vaya] bien.", "mu": "Hasta mañana. Que [u:le vaya] bien."},
]
