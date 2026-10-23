# -*- coding: utf-8 -*-
# BANCO DE "QUE HACER SI ME BLOQUEO" · ORAL (DELE A2) · curso de preparacion, Modulo 4
# Lo usa build_M4_bloqueo.py. Para cambiar contenidos, solo se toca este archivo.
#
# IDEA CENTRAL: en la oral, quedarse callado es lo peor que puede pasar. Siempre hay algo que decir,
# aunque no sepas una palabra o no entiendas al examinador.
#
# Trato: cada frase o respuesta del CANDIDATO lleva su trato ("tu", "usted" o None = sirve para los dos).
# El build comprueba que una frase de tu no tiene marcas de usted y al reves (como en la tarea 3).
# Las frases del examinador tambien llevan trato: el examinador habla de tu en las situaciones de
# planificar (tarea 3) y de usted en las preguntas de las tareas 1 y 2 y en las de servicio.

# ------------------------------------------------------------ POR QUE IMPORTA (fiel a la escala de la Guia)
# Cada fila: lo que haces, lo que ve el examinador (con la escala oficial en sencillo) y a que nota afecta.
IMPORTA = [
 {"k": "callado", "t": "Te quedas callado mucho rato",
  "ve": "La escala oficial describe así la banda más baja (0): «pausas o silencios prolongados y frecuentes». "
        "Y si no dices nada sobre una pauta, esa pauta queda sin responder.",
  "nota": "Baja el <b>uso de la lengua</b> (no hay discurso) y el <b>cumplimiento de la tarea</b> (faltan pautas).",
  "mejor": "Una pausa corta para pensar es normal. Di «Pues... a ver...» y sigue con algo, aunque sea sencillo."},
 {"k": "ayuda", "t": "El examinador tiene que ayudarte todo el tiempo",
  "ve": "Si te quedas callado, el examinador te hace preguntas para ayudarte. Una ayuda de vez en cuando cabe en la banda 2 "
        "(«puede necesitar ayuda del interlocutor»). Necesitar ayuda, repeticiones y preguntas siempre es la descripción de la banda 1.",
  "nota": "Baja el <b>uso de la lengua</b> y, en la nota del entrevistador, la <b>interacción</b>.",
  "mejor": "Pide ayuda tú, con una frase: «¿Puede repetir?», «¿Qué significa...?». Y después contesta con una frase completa."},
 {"k": "sino", "t": "Contestas solo «sí» o «no» (tarea 3)",
  "ve": "En la tarea 3, la banda 1 de cumplimiento es responder «brevemente, e incluso parcialmente». La banda 2: responder con la "
        "información que pide el examinador. La banda 3: añadir algún detalle, opinión o motivo.",
  "nota": "Baja el <b>cumplimiento de la tarea 3</b>, aunque tu español sea correcto.",
  "mejor": "Responde, añade un detalle o un porqué y devuelve una pregunta: «Sí, vale. Prefiero el sábado porque... ¿Y tú?»."},
 {"k": "leer", "t": "Lees las notas",
  "ve": "Puedes llevar tus notas a la sala y mirarlas: la Guía lo permite. El problema es leer frases enteras: no miras al examinador, "
        "hablas a trozos o muy deprisa y, cuando te pregunta algo que no está en el papel, te bloqueas.",
  "nota": "Baja el <b>uso de la lengua</b> (el discurso ya no es «razonablemente continuo») y la interacción.",
  "mejor": "Notas en palabras clave. Miras un segundo, levantas la cabeza y hablas tú."},
]

# Lo que SI puedes hacer sin miedo (la banda 2 lo admite)
SE_PUEDE = [
 ("Hacer pausas cortas para pensar", "La banda 2 admite errores «y/o alguna pausa». Con «Pues...», «A ver...» la pausa no se nota."),
 ("Pedir que te repitan alguna vez", "La banda 2 dice que puedes necesitar ayuda del examinador. Una vez, con educación, es normal."),
 ("Explicar una palabra que no sabes", "La banda 2 pide un repertorio suficiente para «dejar claro lo que quiere decir». Si explicas la palabra, lo dejas claro."),
 ("Corregirte", "Si te equivocas y te corriges rápido, el examinador ve que controlas la gramática básica."),
 ("Inventar", "Nadie comprueba si es verdad. Si no tienes hermanos o no fuiste a esa fiesta, imagina: lo que cuenta es hablar."),
]

# ------------------------------------------------------------ LAS SITUACIONES DE BLOQUEO
# frases: "n" = sirven con tu y con usted · "tu" · "us" (usted)
# ejemplos: [{"tarea", "trato", "l": [(quien, texto), ...]}]  quien: "E" examinador · "C" candidato
#   En las lineas del candidato, la frase de rescate va entre {{ }} (sale marcada en color).
SITUACIONES = [
 {"id": "palabra", "t": "No sé una palabra", "ico": "?",
  "cuando": "En las tres tareas, sobre todo en la foto y en la tarea 3.",
  "que": "No te pares. Explica la palabra con otras palabras: para qué sirve, cómo es, de qué es, dónde está o a qué se parece. "
         "También puedes decir lo contrario o dar un ejemplo.",
  "frases": {"n": ["Es una cosa que sirve para...", "Es como un..., pero más pequeño / más grande.", "No sé cómo se dice, pero es...",
                   "Es de metal / de plástico / de tela.", "Está en la cocina / en el baño / en la calle...",
                   "Es una persona que trabaja en...", "Es un sitio donde...", "Es lo contrario de...", "Por ejemplo, ..."],
             "tu": ["¿Sabes cómo se llama?", "¿Me entiendes?"],
             "us": ["¿Sabe cómo se llama?", "¿Me entiende?"]},
  "ejemplos": [
   {"tarea": "Tarea 2 · la foto", "trato": None, "l": [
    ("C", "Encima de la mesa hay pan, queso y una botella de vino. Y al lado hay... {{no sé cómo se dice, pero es una cosa de metal que sirve para abrir las botellas de vino}}."),
   ]},
   {"tarea": "Tarea 3 · en una tienda", "trato": "usted", "l": [
    ("E", "Buenos días. ¿Qué desea?"),
    ("C", "Buenos días. Quería... mmm... {{una cosa para secar el pelo, con aire caliente. ¿Sabe cómo se llama?}}"),
    ("E", "¿Un secador?"),
    ("C", "¡Sí, eso! Un secador. ¿Tiene alguno pequeño para viajar?"),
   ]},
   {"tarea": "Tarea 1 · el monólogo", "trato": None, "l": [
    ("C", "El hotel no era barato, era... {{lo contrario de barato}}. Pero las vistas eran increíbles."),
   ]}],
  "truco": "No digas la palabra en tu idioma o en inglés y te pares. Si el examinador te dice la palabra, repítela y sigue: «¡Eso! Un secador»."},

 {"id": "entiendo", "t": "No entiendo al examinador", "ico": "¿?",
  "cuando": "Sobre todo en la tarea 3 y cuando el examinador te hace preguntas después del monólogo o de la foto.",
  "que": "Pídele que repita o que hable más despacio, o comprueba lo que has entendido con una pregunta. "
         "Pedirlo una vez es normal en A2. Lo que baja la nota es no contestar o contestar «sí» sin entender.",
  "frases": {"n": ["¿Qué significa «...»?", "Perdón, no entiendo la palabra «...»."],
             "tu": ["Perdona, ¿puedes repetir?", "¿Puedes hablar más despacio, por favor?", "¿Quieres decir que...?", "Perdona, no te he entendido."],
             "us": ["Perdone, ¿puede repetir?", "¿Puede hablar más despacio, por favor?", "¿Quiere decir que...?", "Perdone, no le he entendido."]},
  "ejemplos": [
   {"tarea": "Tarea 3 · en el aeropuerto", "trato": "usted", "l": [
    ("E", "¿Lleva algún líquido en el equipaje de mano?"),
    ("C", "{{Perdone, ¿puede repetir más despacio?}}"),
    ("E", "Sí, claro: ¿lleva agua o perfume en la maleta pequeña?"),
    ("C", "Ah, vale. No, no llevo nada: solo ropa y un libro."),
   ]},
   {"tarea": "Tarea 3 · con un amigo", "trato": "tu", "l": [
    ("E", "¿Te viene bien quedar a las ocho o te pilla muy tarde?"),
    ("C", "{{¿Quieres decir que si a las ocho es tarde para mí?}} No, no, a las ocho me va bien."),
   ]}],
  "truco": "Cuando entiendas, contesta con una frase completa: así el examinador ve que ahora sí has entendido."},

 {"id": "pensar", "t": "Necesito pensar", "ico": "...",
  "cuando": "En las tres tareas: cuando la pregunta es difícil o no tienes la idea preparada.",
  "que": "Gana unos segundos con una palabra natural y empieza a hablar. Una pausa corta es normal; un silencio largo, no.",
  "frases": {"n": ["Pues...", "A ver...", "Bueno...", "Mmm, es una buena pregunta.", "La verdad es que no lo sé, pero creo que...",
                   "Es difícil, pero creo que..."],
             "tu": ["Déjame pensar...", "¿Y tú qué piensas?"],
             "us": ["Déjeme pensar...", "¿Y usted qué piensa?"]},
  "ejemplos": [
   {"tarea": "Tarea 1 · pregunta del examinador", "trato": "usted", "l": [
    ("E", "¿Y qué es lo que más le gusta de su ciudad?"),
    ("C", "{{Mmm, es una buena pregunta... A ver...}} Creo que la comida. Hay muchos bares con tapas muy buenas."),
   ]},
   {"tarea": "Tarea 3 · con una amiga", "trato": "tu", "l": [
    ("E", "¿Y qué le regalamos a Marta?"),
    ("C", "{{Uf, déjame pensar...}} Le encanta leer. ¿Un libro de viajes?"),
   ]}],
  "truco": "Una palabra para pensar y después habla. «Pues... pues... pues...» no te da tiempo: te lo quita."},

 {"id": "error", "t": "Me he equivocado", "ico": "!",
  "cuando": "En las tres tareas: un tiempo verbal, un día, un número, el / la...",
  "que": "Corrígete rápido, en la misma frase, y sigue. Corrige solo lo importante (un pasado, un día, un número). "
         "No empieces otra vez desde el principio y no te pares a pensar en cada error.",
  "frases": {"n": ["Perdón, quiero decir...", "No, no: ...", "Perdón, me he equivocado: ..."],
             "tu": ["Perdona, quiero decir..."],
             "us": ["Perdone, quiero decir..."]},
  "ejemplos": [
   {"tarea": "Tarea 1 · el monólogo", "trato": None, "l": [
    ("C", "El verano pasado voy... {{perdón, fui}} a Granada con mi hermana."),
   ]},
   {"tarea": "Tarea 3 · con un amigo", "trato": "tu", "l": [
    ("C", "¿Quedamos el lunes? {{No, no: el martes}}, que el lunes trabajo hasta tarde."),
   ]}],
  "truco": "Si te das cuenta tarde, no vuelvas atrás: sigue. Un error pequeño que no se corrige no es un drama; un silencio largo, sí."},

 {"id": "blanco", "t": "Me quedo en blanco (monólogo o foto)", "ico": "_",
  "cuando": "En la tarea 1 y en la tarea 2: hablas tú solo y, de repente, no sabes qué más decir.",
  "que": "Vuelve a la lámina o a tus notas: mira la pauta o la casilla siguiente. En la foto, recorre las seis preguntas: "
         "las personas, el lugar, qué hacen, qué relación tienen, qué sienten, qué han hecho antes y qué van a hacer. "
         "Di una frase para pasar al punto siguiente y sigue.",
  "frases": {"n": ["Bueno, ahora voy a hablar de...", "Y sobre..., creo que...", "A ver, ¿qué más hay en la foto? Pues...",
                   "Otra cosa importante es...", "Perdón, no me acuerdo. Bueno, ahora...", "Y para terminar, ..."],
             "tu": [], "us": []},
  "ejemplos": [
   {"tarea": "Tarea 1 · el monólogo", "trato": None, "l": [
    ("C", "... y por eso es muy importante para mí. Mmm... (mira la lámina) {{Bueno, ahora voy a hablar de}} cuándo la conocí. La conocí en 2015, en la universidad..."),
   ]},
   {"tarea": "Tarea 2 · la foto", "trato": None, "l": [
    ("C", "... y la niña está jugando con el perro. Eh... {{a ver, ¿qué más?}} ¿Cómo se sienten? Pues creo que la madre está cansada, porque..."),
   ]}],
  "truco": "Tus notas tienen el mismo orden que la lámina. Si te pierdes, mira el número siguiente, no el que ya has dicho."},

 {"id": "dialogo", "t": "No sé qué contestar (diálogo)", "ico": "↔",
  "cuando": "En la tarea 3: el examinador te pregunta algo que no esperabas o no tienes opinión.",
  "que": "Tres pasos: responde algo (sencillo o inventado), añade un detalle o un porqué y devuelve una pregunta. "
         "Si preguntas, el examinador habla y tú tienes tiempo para pensar.",
  "frases": {"n": ["No sé, la verdad. Creo que...", "Me da igual, pero...", "No estoy seguro / segura, pero..."],
             "tu": ["¿Y tú qué piensas?", "¿Tú qué prefieres?", "¿Qué te parece mejor?"],
             "us": ["¿Y usted qué me recomienda?", "¿Cuál me recomienda?", "¿Qué le parece mejor?"]},
  "ejemplos": [
   {"tarea": "Tarea 3 · con una amiga", "trato": "tu", "l": [
    ("E", "¿Y qué película vemos?"),
    ("C", "{{Uf, no sé, la verdad.}} No conozco las películas nuevas, pero me gustan las comedias. {{¿Tú qué prefieres?}}"),
   ]},
   {"tarea": "Tarea 3 · en un hotel", "trato": "usted", "l": [
    ("E", "¿Prefiere una habitación con vistas al mar o a la montaña?"),
    ("C", "{{Mmm, me da igual, pero}} quiero dormir bien. ¿Cuál es más tranquila? {{¿Qué me recomienda?}}"),
   ]}],
  "truco": "Responde + añade + pregunta. Nunca solo «sí», «no» o «no sé»."},
]
ORDEN = [s["id"] for s in SITUACIONES]

# Tu y usted en las frases de rescate (tabla)
TU_USTED = [("Perdona, ¿puedes repetir?", "Perdone, ¿puede repetir?"), ("¿Puedes hablar más despacio?", "¿Puede hablar más despacio?"),
            ("¿Quieres decir que...?", "¿Quiere decir que...?"), ("¿Sabes cómo se llama?", "¿Sabe cómo se llama?"),
            ("Déjame pensar...", "Déjeme pensar..."), ("¿Y tú qué piensas?", "¿Y usted qué piensa?"),
            ("Perdona, quiero decir...", "Perdone, quiero decir...")]

# Tarjeta imprimible: las frases de rescate en una hoja (por situacion: neutras + tu / usted)
TARJETA = {
 "palabra": {"n": ["Es una cosa que sirve para...", "Es como un..., pero más...", "No sé cómo se dice, pero es..."], "tu": "¿Sabes cómo se llama?", "us": "¿Sabe cómo se llama?"},
 "entiendo": {"n": ["¿Qué significa «...»?"], "tu": "Perdona, ¿puedes repetir? · ¿Quieres decir que...?", "us": "Perdone, ¿puede repetir? · ¿Quiere decir que...?"},
 "pensar": {"n": ["Pues... · A ver... · Bueno...", "Mmm, es una buena pregunta."], "tu": "Déjame pensar...", "us": "Déjeme pensar..."},
 "error": {"n": ["Perdón, quiero decir...", "No, no: ..."], "tu": "", "us": ""},
 "blanco": {"n": ["Bueno, ahora voy a hablar de...", "A ver, ¿qué más hay en la foto? Pues...", "Y para terminar, ..."], "tu": "", "us": ""},
 "dialogo": {"n": ["No sé, la verdad. Creo que...", "Respondo + añado + pregunto"], "tu": "¿Y tú qué piensas?", "us": "¿Qué me recomienda?"},
}

# ------------------------------------------------------------ EJERCICIO 1: "¿QUE DICES?"
# s: situacion de bloqueo · tarea · trato (del candidato; None = monologo) · sit: lo que pasa · e: lo que dice el examinador (opcional)
# ops: tres respuestas · ok: la buena · por: por que. La buena siempre respeta el trato (el build lo comprueba).
QUIZ = [
 {"s": "palabra", "tarea": "Tarea 2", "trato": None, "sit": "Describes la foto y no sabes cómo se dice «paraguas».",
  "ops": ["En la foto la niña lleva un... umbrella. Bueno, nada.",
          "La niña lleva... no sé cómo se dice: es una cosa que sirve para no mojarse cuando llueve.",
          "(Te quedas callado y miras al examinador.)"], "ok": 1,
  "por": "Explicas para qué sirve y sigues hablando. Decir la palabra en inglés y parar no comunica; quedarse callado es lo peor."},
 {"s": "palabra", "tarea": "Tarea 3", "trato": "usted", "sit": "En la farmacia quieres unas tiritas, pero no sabes la palabra.",
  "e": "Buenas tardes. ¿Qué necesita?",
  "ops": ["Quería... no sé. Nada, gracias.",
          "Quería... una cosa pequeña para poner en un dedo cuando una persona se corta. ¿Sabe cómo se llama?",
          "Quería... ¿tienes algo para el dedo?"], "ok": 1,
  "por": "Describes la cosa y preguntas cómo se llama, con usted. La tercera es de tú (tienes) y muy poco clara."},
 {"s": "palabra", "tarea": "Tarea 3", "trato": "tu", "sit": "Preparáis una excursión y quieres decir «saco de dormir».",
  "e": "¿Y qué tenemos que llevar?",
  "ops": ["Tenemos que llevar un sleeping bag.",
          "Tenemos que llevar... bueno, nada.",
          "Tenemos que llevar... ¿cómo se dice?... una cosa para dormir en el suelo, como una cama de tela. ¿Sabes qué digo?"], "ok": 2,
  "por": "Explicas la cosa con palabras sencillas y compruebas si te entiende. La palabra en inglés puede no entenderse."},
 {"s": "entiendo", "tarea": "Tarea 3", "trato": "usted", "sit": "En el aeropuerto no entiendes la pregunta.",
  "e": "¿Desea facturar el equipaje o lo lleva en cabina?",
  "ops": ["Sí.", "Perdone, no le he entendido. ¿Puede repetir más despacio?", "¿Qué dices? No entiendo nada."], "ok": 1,
  "por": "Pides que repita con educación y con usted. Decir «sí» sin entender es peligroso; «¿Qué dices?» es de tú y suena brusco."},
 {"s": "entiendo", "tarea": "Tarea 3", "trato": "tu", "sit": "Hablas con un amigo y no entiendes bien una expresión.",
  "e": "¿Te apetece que quedemos en el sitio de siempre?",
  "ops": ["¿Quieres decir en el bar de la plaza, como siempre? Vale, me parece bien.", "Sí, sí.", "Perdone, ¿puede repetir?"], "ok": 0,
  "por": "Compruebas lo que has entendido con «¿Quieres decir...?» y contestas. Con un amigo no se usa «perdone, ¿puede...?»."},
 {"s": "entiendo", "tarea": "Tarea 1", "trato": "usted", "sit": "Después del monólogo, el examinador te pregunta algo y no entiendes una palabra.",
  "e": "¿Y qué tal se le da cocinar?",
  "ops": ["No entiendo. (Y esperas.)", "¿Quiere decir si cocino bien? Pues regular: sé hacer tortilla y ensaladas, pero poco más.", "Me gusta mucho mi ciudad."], "ok": 1,
  "por": "Compruebas con «¿Quiere decir...?» y respondes con un detalle. La tercera contesta otra cosa."},
 {"s": "entiendo", "tarea": "Tarea 3", "trato": "usted", "sit": "En una tienda, la dependienta te dice algo que no entiendes bien.",
  "e": "Le recuerdo que la devolución solo se hace con el tique.",
  "ops": ["Vale.", "¿Quiere decir que sin el tique no me devuelven el dinero? Mire, es que lo he perdido...", "¿Qué? Repite."], "ok": 1,
  "por": "Compruebas lo que has entendido y sigues la conversación. «Vale» solo no da información; «Repite» es de tú y suena a orden."},
 {"s": "pensar", "tarea": "Tarea 1", "trato": "usted", "sit": "Después del monólogo, una pregunta difícil.",
  "e": "¿Qué es lo más difícil de vivir en otro país?",
  "ops": ["(Silencio de diez segundos.)", "Mmm, es una buena pregunta... A ver... Creo que estar lejos de la familia, porque la veo poco.",
          "Pues... pues... pues... no sé."], "ok": 1,
  "por": "Ganas unos segundos con naturalidad y respondes con un porqué. Repetir «pues» y terminar con «no sé» no responde."},
 {"s": "pensar", "tarea": "Tarea 2", "trato": "usted", "sit": "Has descrito la foto y el examinador te hace una pregunta.",
  "e": "¿Por qué cree que están tan contentos?",
  "ops": ["Porque sí.", "No sé.", "A ver... creo que es el cumpleaños de la abuela, porque hay una tarta con velas."], "ok": 2,
  "por": "Una palabra para pensar y una opinión con un motivo (creo que... porque...). Es lo que valora la banda 3."},
 {"s": "error", "tarea": "Tarea 1", "trato": None, "sit": "En el monólogo dices «Ayer voy al cine» y te das cuenta.",
  "ops": ["(Te paras y empiezas otra vez el monólogo desde el principio.)",
          "Ayer voy... perdón, fui al cine con mis amigos y vimos una comedia.",
          "Ayer voy al cine, no, ayer iba, no, ayer he ido, no..."], "ok": 1,
  "por": "Te corriges rápido y sigues. Empezar otra vez o probar todos los tiempos te hace perder tiempo y seguridad."},
 {"s": "error", "tarea": "Tarea 3", "trato": "tu", "sit": "Propones el lunes y te acuerdas de que el lunes trabajas.",
  "e": "Vale, ¿entonces quedamos el lunes?",
  "ops": ["Perdona, me he equivocado: el lunes no puedo. Mejor el martes, ¿vale?", "Bueno, el lunes. (Y no dices nada más.)",
          "Perdone, me he equivocado: el martes."], "ok": 0,
  "por": "Te corriges, explicas y propones otra cosa, con tú. «Perdone» es de usted: con un amigo, «perdona»."},
 {"s": "blanco", "tarea": "Tarea 1", "trato": None, "sit": "Estás en la pauta 3 del monólogo y no te acuerdas de qué más decir.",
  "ops": ["(Miras al examinador y esperas.)", "Bueno... ahora voy a hablar de mis planes: el verano que viene voy a ir a Italia con mi pareja.",
          "Lo siento, no me acuerdo de nada más. He terminado."], "ok": 1,
  "por": "Miras la lámina, pasas a la pauta siguiente con una frase puente y sigues. Si terminas antes de tiempo, faltan pautas."},
 {"s": "blanco", "tarea": "Tarea 2", "trato": None, "sit": "Has hablado de las personas y del lugar, y no sabes qué más decir.",
  "ops": ["Y... ya está.", "A ver, ¿qué están haciendo? Pues el chico está cocinando y la chica está poniendo la mesa.",
          "En mi casa también tengo una cocina así y mi madre cocina muy bien..."], "ok": 1,
  "por": "Recorres las seis preguntas de la foto: ahora toca «qué hacen». Hablar de tu vida en vez de describir la foto no cumple la tarea."},
 {"s": "dialogo", "tarea": "Tarea 3", "trato": "tu", "sit": "Tu amiga quiere ir al cine y te pregunta.",
  "e": "¿Y qué película vemos?",
  "ops": ["No sé.", "No sé, la verdad: no conozco las películas nuevas. Me gustan las comedias... ¿Tú qué prefieres?", "Lo que usted quiera."], "ok": 1,
  "por": "Responde, añade y pregunta. «No sé» solo para la conversación; «usted» no va con una amiga."},
 {"s": "dialogo", "tarea": "Tarea 3", "trato": "usted", "sit": "En una tienda te preguntan por el color y te da igual.",
  "e": "¿Lo quiere en azul o en negro?",
  "ops": ["Mmm, me da igual. ¿Cuál se vende más? ¿Qué me recomienda?", "Azul. (Y nada más.)", "¿Y tú cuál prefieres?"], "ok": 0,
  "por": "Respondes, preguntas y le das la palabra al dependiente. «Azul» es correcto, pero muy corto; «tú» no va en una tienda."},
 {"s": "dialogo", "tarea": "Tarea 3", "trato": "tu", "sit": "Un amigo te pregunta por un sitio donde no has estado.",
  "e": "¿Tú has estado alguna vez en Asturias?",
  "ops": ["No.", "No, nunca, pero me gustaría ir, porque dicen que es muy verde. ¿Y tú?", "No, nunca. ¿Y usted ha estado?"], "ok": 1,
  "por": "Contestas, añades un deseo con un porqué y devuelves la pregunta con tú."},
]

# ------------------------------------------------------------ EJERCICIO 2: "DESCRIBE LA PALABRA"
# w: la palabra · ctx: donde la necesitas · ops: tres descripciones · ok: la mejor · por: por que
# raiz: trozos que NO pueden salir en la descripcion buena (el build lo comprueba)
PALABRAS = [
 {"w": "el paraguas", "raiz": ["paragu"], "ctx": "Tarea 2: en la foto, un señor lleva uno porque llueve.",
  "ops": ["Es un umbrella.", "Es una cosa que sirve para no mojarse cuando llueve. Es como un techo pequeño que llevas en la mano.", "Es una cosa... de la lluvia. No sé."], "ok": 1},
 {"w": "la llave", "raiz": ["llave"], "ctx": "Tarea 3: has perdido una y llamas al hotel.",
  "ops": ["Es una cosa pequeña de metal que sirve para abrir la puerta de la habitación.", "Es la puerta.", "Es una cosa. Pequeña."], "ok": 0},
 {"w": "la cartera", "raiz": ["carter"], "ctx": "Tarea 2: en la foto, un señor la busca en los bolsillos.",
  "ops": ["Es dinero.", "Es una caja para guardar zapatos.", "Es una cosa de piel donde llevas el dinero y las tarjetas. Normalmente está en el bolsillo o en el bolso."], "ok": 2},
 {"w": "el cargador", "raiz": ["cargador"], "ctx": "Tarea 3: te lo has dejado en casa y lo pides en una tienda.",
  "ops": ["Es un cable que sirve para dar batería al móvil. Lo pones en la pared.", "Es el móvil.", "Es un charger, ¿sabe?"], "ok": 0},
 {"w": "la maleta", "raiz": ["maleta"], "ctx": "Tarea 1: hablas de un viaje.",
  "ops": ["Es como una bolsa grande y dura, con ruedas, para llevar la ropa cuando viajas.", "Es una cosa del viaje.", "Es el avión."], "ok": 0},
 {"w": "el horno", "raiz": ["horno"], "ctx": "Tarea 2: en la foto hay una cocina.",
  "ops": ["Es una cosa de la cocina.", "Está en la cocina. Es como una caja caliente que sirve para hacer pizza, pan o pasteles.", "Es el frigorífico, pero caliente... no, no sé."], "ok": 1},
 {"w": "la toalla", "raiz": ["toalla"], "ctx": "Tarea 1: hablas de tus vacaciones en la playa.",
  "ops": ["Es una ropa.", "Es una tela grande que usas para secarte después de la ducha o en la playa.", "Es una towel."], "ok": 1},
 {"w": "el despertador", "raiz": ["desperta"], "ctx": "Tarea 1: hablas de tu rutina.",
  "ops": ["Es un reloj pequeño que hace ruido por la mañana para no llegar tarde.", "Es la mañana.", "Es una cosa... que hace ruido."], "ok": 0},
 {"w": "la bufanda", "raiz": ["bufanda"], "ctx": "Tarea 2: en la foto, una mujer lleva una larga, de rayas.",
  "ops": ["Es un abrigo.", "Es una ropa. Para el frío.", "Es una cosa de lana que llevas en el cuello en invierno, cuando hace frío."], "ok": 2},
 {"w": "las tijeras", "raiz": ["tijera"], "ctx": "Tarea 3: preparáis una fiesta y necesitáis unas.",
  "ops": ["Es una cosa de metal con dos partes que sirve para cortar papel o tela.", "Es un cuchillo.", "Es para el papel."], "ok": 0},
 {"w": "el frigorífico", "raiz": ["frigor", "nevera"], "ctx": "Tarea 1: hablas de tu casa.",
  "ops": ["Es una cosa de la casa.", "Es un mueble grande y frío de la cocina. Dentro hay leche, fruta y agua fría.", "Es el horno."], "ok": 1},
 {"w": "el recepcionista", "raiz": ["recep"], "ctx": "Tarea 2: en la foto hay un hotel.",
  "ops": ["Es una persona del hotel.", "Es un cliente.", "Es la persona que trabaja en la entrada de un hotel: te da la llave de la habitación."], "ok": 2},
 {"w": "el andén", "raiz": ["andén", "anden"], "ctx": "Tarea 3: en la estación preguntas dónde sale tu tren.",
  "ops": ["Es el sitio de la estación donde esperas el tren y subes.", "Es el tren.", "Es una platform."], "ok": 0},
 {"w": "aparcar", "raiz": ["aparca"], "ctx": "Tarea 3: con un amigo decidís si vais en coche.",
  "ops": ["Es conducir.", "Es lo que haces con el coche cuando llegas: lo dejas en la calle o en un garaje.", "Es una cosa del coche."], "ok": 1},
 {"w": "devolver", "raiz": ["devol", "devuel"], "ctx": "Tarea 3: en una tienda, algo no funciona.",
  "ops": ["Es cuando vas a la tienda con algo que has comprado y no te gusta, y te dan el dinero otra vez.", "Es comprar.", "Es... return."], "ok": 0},
 {"w": "el sacacorchos", "raiz": ["sacacor", "corcho"], "ctx": "Tarea 2: en la foto hay una botella de vino.",
  "ops": ["Es una botella.", "Es una cosa para el vino.", "Es una cosa de metal que sirve para abrir una botella de vino."], "ok": 2},
]
# Tipo de fallo de cada opcion (None = la buena), en el mismo orden que ops
TIPOS_MALAS = {
 "el paraguas": ["ingles", None, "vago"], "la llave": [None, "otra", "vago"], "la cartera": ["vago", "otra", None],
 "el cargador": [None, "otra", "ingles"], "la maleta": [None, "vago", "otra"], "el horno": ["vago", None, "otra"],
 "la toalla": ["vago", None, "ingles"], "el despertador": [None, "otra", "vago"], "la bufanda": ["otra", "vago", None],
 "las tijeras": [None, "otra", "vago"], "el frigorífico": ["vago", None, "otra"], "el recepcionista": ["vago", "otra", None],
 "el andén": [None, "otra", "ingles"], "aparcar": ["otra", None, "vago"], "devolver": [None, "otra", "ingles"],
 "el sacacorchos": ["otra", "vago", None],
}
# Por que no valen las otras (por tipo de fallo): se elige automaticamente al comprobar
POR_PALABRA = {
 "ingles": "Decir la palabra en otro idioma no siempre se entiende y no demuestra tu español.",
 "vago": "Es demasiado poco: el examinador no sabe de qué cosa hablas.",
 "otra": "Describe otra cosa: el examinador va a entender algo diferente.",
}
# Las cuatro preguntas para describir una palabra (pistas del ejercicio y del entrenador)
PISTAS_PALABRA = ["¿Para qué sirve?", "¿Cómo es? ¿De qué es?", "¿Dónde está?", "¿A qué se parece? ¿Cuál es lo contrario?"]

# ------------------------------------------------------------ ENTRENADOR: TARJETAS
# Palabras para explicar sin decirlas (las de PALABRAS tambien salen)
PALABRAS_EXTRA = ["la escalera", "el ascensor", "la almohada", "el cepillo de dientes", "el mando de la tele", "el buzón", "la gorra",
                  "las gafas de sol", "el semáforo", "la papelera", "el enchufe", "la sartén", "la mochila", "la cuchara", "el billete",
                  "el jardín", "la farmacia", "el camarero", "la peluquería", "el mercado"]
# Preguntas del examinador: q · trato · t (tarea en la que suena)
PREGUNTAS = [
 {"q": "¿Qué es lo que más le gusta de su trabajo o de sus estudios?", "trato": "usted", "t": "Tarea 1"},
 {"q": "¿Cómo era su vida hace diez años?", "trato": "usted", "t": "Tarea 1"},
 {"q": "¿Qué va a hacer este fin de semana?", "trato": "usted", "t": "Tarea 1"},
 {"q": "¿Prefiere vivir en el campo o en la ciudad? ¿Por qué?", "trato": "usted", "t": "Tarea 1"},
 {"q": "¿Qué hace normalmente para relajarse?", "trato": "usted", "t": "Tarea 1"},
 {"q": "¿Qué plato típico de su país me recomienda?", "trato": "usted", "t": "Tarea 1"},
 {"q": "¿Ha estado alguna vez en un sitio como el de la foto?", "trato": "usted", "t": "Tarea 2"},
 {"q": "¿Por qué cree que esta persona está tan seria?", "trato": "usted", "t": "Tarea 2"},
 {"q": "¿Qué cree que van a hacer después?", "trato": "usted", "t": "Tarea 2"},
 {"q": "¿Qué día te viene mejor para quedar?", "trato": "tu", "t": "Tarea 3"},
 {"q": "¿Y si invitamos también a mis primos?", "trato": "tu", "t": "Tarea 3"},
 {"q": "Uf, es que ese restaurante es muy caro para mí.", "trato": "tu", "t": "Tarea 3"},
 {"q": "¿Tú qué prefieres, playa o montaña?", "trato": "tu", "t": "Tarea 3"},
 {"q": "No me gusta mucho tu idea, la verdad.", "trato": "tu", "t": "Tarea 3"},
 {"q": "¿Quién compra las bebidas?", "trato": "tu", "t": "Tarea 3"},
 {"q": "Lo siento, de esa talla ya no nos quedan.", "trato": "usted", "t": "Tarea 3"},
 {"q": "¿Va a pagar en efectivo o con tarjeta?", "trato": "usted", "t": "Tarea 3"},
 {"q": "El tren de las diez está completo.", "trato": "usted", "t": "Tarea 3"},
]
# Frases dificiles a proposito (para practicar "no entiendo"): q · trato · dif (la palabra dificil) · clar (como lo dice despues)
DIFICILES = [
 {"q": "¿Ha tenido algún percance durante el viaje?", "trato": "usted", "dif": "percance", "clar": "¿Ha tenido algún problema en el viaje?"},
 {"q": "¿Desea que se lo envuelva para regalo?", "trato": "usted", "dif": "envuelva", "clar": "¿Es un regalo? ¿Le pongo papel de regalo?"},
 {"q": "¿Le hago una factura o le basta con el tique?", "trato": "usted", "dif": "le basta", "clar": "¿Quiere una factura o solo el tique?"},
 {"q": "¿Lleva algún objeto punzante en la maleta?", "trato": "usted", "dif": "punzante", "clar": "¿Lleva cuchillos o tijeras en la maleta?"},
 {"q": "¿Tiene la tarjeta de fidelización?", "trato": "usted", "dif": "fidelización", "clar": "¿Tiene la tarjeta de cliente de la tienda?"},
 {"q": "¿Qué tal se le da la cocina?", "trato": "usted", "dif": "se le da", "clar": "¿Cocina bien?"},
 {"q": "¿Te viene bien quedar a las ocho o te pilla muy tarde?", "trato": "tu", "dif": "te pilla", "clar": "¿A las ocho puedes o es tarde para ti?"},
 {"q": "Oye, ¿y si hacemos un bote para el regalo?", "trato": "tu", "dif": "un bote", "clar": "¿Y si cada uno pone dinero para el regalo?"},
 {"q": "¿Te apuntas al plan o te lo piensas?", "trato": "tu", "dif": "Te apuntas", "clar": "¿Vienes con nosotros o quieres pensarlo?"},
 {"q": "¿Nos vemos en la boca de metro?", "trato": "tu", "dif": "la boca de metro", "clar": "¿Nos vemos en la entrada del metro?"},
]
# Frases con un error para corregirse en voz alta: mal · bien (lo que dices despues de "Perdon, quiero decir...")
ERRORES = [
 {"mal": "Ayer voy al cine con mi hermano.", "bien": "Ayer fui al cine con mi hermano."},
 {"mal": "Mi hermana es muy alto.", "bien": "Mi hermana es muy alta."},
 {"mal": "La foto hay dos personas.", "bien": "En la foto hay dos personas."},
 {"mal": "Cuando era pequeño, jugué todos los días en la calle.", "bien": "Cuando era pequeño, jugaba todos los días en la calle."},
 {"mal": "El lunes pasado he ido al médico.", "bien": "El lunes pasado fui al médico."},
 {"mal": "Hay la mesa en el centro de la foto.", "bien": "La mesa está en el centro de la foto."},
 {"mal": "El verano que viene voy a viajo a Italia.", "bien": "El verano que viene voy a viajar a Italia."},
 {"mal": "Los niños están muy contento.", "bien": "Los niños están muy contentos."},
]
# Tarjetas de "me quedo en blanco" en el entrenador: un tema para seguir hablando
BLANCO = ["Te quedas en blanco. Pasa a otro punto: habla de lo que vas a hacer este fin de semana.",
          "Te quedas en blanco. Mira «la lámina»: ahora toca hablar de cómo era antes.",
          "Te quedas en blanco en la foto. Sigue con la pregunta 5: ¿cómo se sienten las personas?",
          "Te quedas en blanco en la foto. Sigue con la pregunta 6: ¿qué han hecho antes?",
          "Te quedas en blanco. Habla de una persona importante para ti: quién es y cómo es."]

# Instrucciones de cada tipo de tarjeta del entrenador
TARJETA_TIPOS = {
 "palabra": {"n": "No te sale la palabra", "ins": "Explícala sin decirla: para qué sirve, cómo es, dónde está..."},
 "pregunta": {"n": "El examinador pregunta", "ins": "Contesta con una frase completa y añade un detalle o un porqué."},
 "dificil": {"n": "No entiendes", "ins": "Pide que repita o pregunta qué significa. Después contesta."},
 "error": {"n": "Te has equivocado", "ins": "Lee la frase en voz alta, corrígete («Perdón, quiero decir...») y sigue con otra frase."},
 "blanco": {"n": "Te quedas en blanco", "ins": "No te pares: frase puente y sigue hablando."},
}

# ------------------------------------------------------------ "AHORA TU": LAS LAMINAS DE LAS OTRAS PIEZAS DEL TALLER ORAL
# Resumidas de banco_temas_T1.py, banco_fotos_T2.py y banco_dialogos_T3.py (id, titulo, pautas...).
# Si se cambian alli, cambiarlas aqui. Los ids son los mismos: asi se leen las notas y el historial
# que el estudiante ha guardado en esas piezas (mismo navegador).
STORAGE_T1, STORAGE_T2, STORAGE_T3 = "dele-a2-curso-M4-T1", "dele-a2-curso-M4-T2", "dele-a2-curso-M4-T3"
MES_WP_T2 = "2026/10"   # carpeta de las fotos de la tarea 2 (igual que MES_WP en banco_fotos_T2.py)

FUENTES_T1 = [
 (1, "Una persona importante en mi vida", "Hable de una persona importante en su vida. Hable de:", ["quién es, cómo es y a qué se dedica;", "por qué es importante para usted;", "cuándo y cómo la conoció;", "cómo era su relación al principio y cómo es ahora;", "qué le gustaría hacer con esta persona en el futuro."]),
 (2, "Una persona de mi familia", "Hable de una persona de su familia. Hable de:", ["quién es, cómo es físicamente y de carácter, y a qué se dedica;", "por qué ha elegido a esta persona;", "cómo era su relación con ella cuando usted era pequeño y cómo es ahora;", "algo especial que hicieron juntos una vez;", "cuándo va a verla la próxima vez y qué van a hacer."]),
 (3, "Mi plato favorito", "Hable de su plato favorito. Hable de:", ["cómo se llama, qué ingredientes lleva y cómo se prepara;", "la última vez que lo comió: dónde, cuándo y con quién;", "qué comía normalmente cuando era niño;", "quién cocina en su casa ahora y qué tipo de comida hacen;", "qué va a cocinar o comer en su próxima comida especial."]),
 (4, "Mi red social favorita", "Hable de su red social favorita. Hable de:", ["cuál es su red social favorita, para qué la usa y por qué le gusta;", "cuánto tiempo pasa al día en las redes y si prefiere el móvil o el ordenador;", "cuándo empezó a usar las redes sociales y cómo era la comunicación antes;", "algo que le pasó una vez en una red social;", "si va a cambiar algo en su forma de usar las redes y por qué."]),
 (5, "Un regalo que he recibido", "Hable de un regalo especial que ha recibido. Hable de:", ["qué era, cómo era, quién se lo regaló y por qué;", "qué sintió al abrirlo y si todavía lo tiene;", "cuándo se hacen regalos en su país;", "qué regalos recibía cuando era pequeño;", "qué regalo va a hacer próximamente y a quién."]),
 (6, "Un curso que hice", "Hable de un curso que hizo. Hable de:", ["qué curso fue, cuándo, dónde y por qué lo hizo;", "cómo eran el profesor y los compañeros;", "qué le gustó más y qué no le gustó;", "qué asignatura le gustaba más en el colegio y por qué;", "qué curso le gustaría hacer en el futuro."]),
 (7, "Una fiesta especial para mí", "Hable de una fiesta especial para usted. Hable de:", ["cuándo fue, dónde y qué se celebró;", "quién estaba con usted;", "qué hizo ese día, desde la mañana hasta la noche;", "por qué fue especial y cómo celebra ahora ese día;", "cuál va a ser la próxima fiesta importante para usted."]),
 (8, "Mis mejores vacaciones", "Hable de sus mejores vacaciones. Hable de:", ["adónde fue, cuándo, con quién y en qué medio de transporte;", "dónde durmió, cuánto tiempo estuvo y qué hizo allí;", "por qué fueron sus mejores vacaciones;", "cómo eran las vacaciones de su familia cuando usted era pequeño;", "adónde va a ir en sus próximas vacaciones y con quién."]),
 (9, "Un viaje que he hecho", "Hable de un viaje que ha hecho. Hable de:", ["adónde fue, por qué hizo el viaje y por qué es importante para usted;", "cuánto tiempo duró, con quién fue y dónde se alojaron;", "cómo era el lugar: el tiempo, la gente, la comida;", "algo que le pasó durante el viaje;", "si va a hacer pronto otro viaje: cuándo, adónde y por qué."]),
 (10, "Mi deporte favorito", "Hable de su deporte o su actividad física favorita. Hable de:", ["qué deporte es, dónde lo practica y con quién;", "cuántas veces a la semana lo hace y por qué le gusta;", "cuándo y cómo empezó a practicarlo;", "qué deporte hacía cuando era más joven;", "qué objetivo tiene para el año que viene."]),
 (11, "Cómo era mi vida de niño", "Hable de cómo era su vida cuando era niño o niña. Hable de:", ["dónde vivía, con quién y cómo era su casa;", "cómo era un día normal: el colegio, las comidas, los juegos;", "un recuerdo especial de su infancia;", "qué es diferente ahora en la vida de los niños;", "qué le gustaría enseñar a los niños de su familia en el futuro."]),
 (12, "Mi trabajo o mis estudios", "Hable de su trabajo o de sus estudios. Hable de:", ["qué hace, dónde y cuál es su horario;", "qué es lo que más le gusta y lo que menos;", "cómo encontró este trabajo o por qué eligió estos estudios;", "qué quería ser cuando era pequeño;", "qué planes tiene para su futuro profesional."]),
 (13, "La ciudad donde vivo", "Hable de la ciudad o el pueblo donde vive. Hable de:", ["dónde está, cómo es y cuántos habitantes tiene;", "qué se puede hacer allí y qué le gusta más;", "cuándo y por qué fue a vivir allí;", "cómo era la ciudad hace unos años y qué ha cambiado;", "qué va a enseñar a un amigo que va a visitarle."]),
 (14, "Mi casa", "Hable de la casa o el piso donde vive. Hable de:", ["cómo es su casa: dónde está, cuántas habitaciones tiene...;", "cuál es su lugar favorito de la casa y qué hace allí;", "cuándo se mudó a esta casa y cómo la encontró;", "cómo era la casa donde vivía antes;", "qué cambios va a hacer o le gustaría hacer en el futuro."]),
 (15, "Mi tiempo libre", "Hable de su tiempo libre. Hable de:", ["qué hace en su tiempo libre y con quién;", "qué hizo el fin de semana pasado;", "qué hacía en su tiempo libre cuando era adolescente;", "por qué es importante para usted tener tiempo libre;", "qué planes tiene para el próximo fin de semana."]),
 (16, "Un libro, una película o una serie", "Hable de un libro, una película o una serie que le gusta mucho. Hable de:", ["qué es y de qué trata;", "cuándo y dónde lo leyó o la vio, y con quién;", "por qué le gustó tanto;", "qué libros o películas le gustaban cuando era más joven;", "qué va a leer o ver próximamente."]),
 (17, "Mi rutina: un día normal", "Hable de su rutina, de un día normal en su vida. Hable de:", ["a qué hora se levanta y qué hace por la mañana;", "qué hace por la tarde y por la noche;", "cómo era su rutina hace cinco años;", "un día en que su rutina cambió por completo;", "qué va a cambiar en su rutina y por qué."]),
 (18, "Mi estación del año favorita", "Hable de su estación del año favorita. Hable de:", ["cuál es y qué tiempo hace en esa estación donde vive;", "qué le gusta hacer en esa época del año;", "qué hacía en esa estación cuando era niño;", "un día especial que recuerda de esa estación;", "qué va a hacer la próxima vez que llegue esa estación."]),
 (19, "Una tienda o un mercado que me gusta", "Hable de una tienda o un mercado donde le gusta comprar. Hable de:", ["qué tienda o mercado es, dónde está y qué venden;", "cada cuánto va y qué compra normalmente;", "cómo hacía la compra su familia cuando usted era pequeño;", "algo especial que compró allí alguna vez;", "qué va a comprar la próxima vez y para qué."]),
 (20, "Mi salud y mis hábitos", "Hable de su salud y de sus hábitos. Hable de:", ["qué hace para cuidar su salud;", "cómo son sus hábitos de comida y de sueño;", "cómo eran sus hábitos hace unos años;", "algo que le pasó y que le hizo cambiar un hábito;", "qué hábito nuevo va a empezar y por qué."]),
]
# Las 6 preguntas de la lamina de la foto (siempre las mismas)
PREGUNTAS_FOTO = ["¿Cómo son las personas de la foto? ¿Qué ropa llevan?", "¿Dónde están esas personas? ¿Qué objetos hay?",
                  "¿Qué están haciendo las personas de la foto?", "¿Qué relación cree que hay entre ellas?",
                  "¿Qué cree que piensan, o cómo cree que se sienten, estas personas? ¿Por qué?",
                  "¿Qué cree que han hecho antes? ¿Y qué van a hacer después?"]
# id, titulo, lo que se ve (texto si la imagen no carga), palabras de la foto (para "no te sale la palabra")
FUENTES_T2 = [
 (1, "Una comida en el campo", "Una familia celebra el cumpleaños de la abuela en el campo, debajo de un olivo; la abuela sopla las velas.", ["el olivo", "el mantel de cuadros", "soplar las velas", "la boina", "el bastón", "el sombrero de paja"]),
 (2, "En el veterinario", "Sala de espera de un veterinario en un día de lluvia; una niña abraza a su perro, que tiene una venda en la pata.", ["la sala de espera", "la venda", "el chubasquero", "el transportín", "la báscula", "el paragüero"]),
 (3, "En la lavandería", "Lavandería de noche; sale mucha espuma de la lavadora de un chico pelirrojo y un señor mayor se ríe.", ["la lavadora", "la secadora", "la espuma", "el detergente", "doblar la sábana", "las zapatillas de casa"]),
 (4, "En la cocina de un restaurante", "Cocina de un restaurante a mediodía; sale humo de la sartén de un chico joven y la jefa se lleva las manos a la cabeza.", ["el fogón", "la sartén", "la olla", "el humo", "el delantal", "el gorro"]),
 (5, "En la pista de patinaje", "Pista de hielo en una plaza en Navidad; un niño se ha caído y su madre intenta ayudarle.", ["la pista de patinaje", "el hielo", "los patines", "el casco", "las orejeras", "la valla"]),
 (6, "Trabajar en casa", "Un padre trabaja en casa con una videollamada; su hija enseña un dibujo a la cámara y el bebé tira la comida.", ["el portátil", "la videollamada", "los auriculares", "las chanclas", "la trona", "el babero"]),
 (7, "Antes de salir de casa", "Recibidor de un piso por la mañana; la madre mira la hora y el niño busca su otro zapato.", ["el recibidor", "el perchero", "el espejo", "la mochila", "las llaves", "tener prisa"]),
 (8, "Hacer deporte", "Cuatro amigos se dan la mano en una pista de pádel al final del partido.", ["la pista de pádel", "la pala", "la red", "la visera", "la rodillera", "la toalla"]),
 (9, "De compras", "Caja de un supermercado; un señor mayor busca la cartera y la cajera espera sonriendo.", ["la caja", "la cajera", "la cinta", "la cartera", "el bolsillo", "el carro de la compra"]),
 (10, "Clases para adultos", "Clase de baile para adultos; el profesor enseña un paso y un chico pisa a su pareja.", ["la clase de baile", "el paso", "el espejo", "el altavoz", "pisar", "el centro cultural"]),
 (11, "Ver la televisión", "Tres amigos ven un partido en el salón; dos saltan de alegría y el otro se tapa la cara.", ["el sofá", "el cojín", "el partido", "marcar un gol", "las palomitas", "el mando a distancia"]),
 (12, "Regalos", "Dos amigas en una cafetería; una abre un regalo, una bufanda de colores, y el camarero trae una tarta con una vela.", ["el papel de regalo", "el lazo", "la bufanda", "la tarta", "la vela", "emocionarse"]),
]
# id, nombre, trato, rol del examinador, situacion, pautas
FUENTES_T3 = [
 (1, "Una fiesta sorpresa para tus padres", "tu", "su hermano / su hermana", "Sus padres cumplen treinta años de casados y usted quiere organizar una pequeña fiesta sorpresa con su hermano / su hermana.", ["dónde y cuándo van a hacer la fiesta;", "a quién van a invitar y cómo;", "qué comida y bebida va a haber;", "qué regalo les pueden hacer;", "qué tiene que hacer cada uno antes de la fiesta."]),
 (2, "Una escapada de fin de semana", "tu", "su amigo / su amiga", "Usted y un amigo / una amiga quieren hacer una escapada de fin de semana a otra ciudad el mes que viene.", ["adónde quieren ir y por qué;", "cómo van a viajar;", "dónde van a dormir y cuánto dinero pueden gastar;", "qué quieren hacer allí;", "cuándo y dónde quedan para salir."]),
 (3, "Una cena en casa con amigos", "tu", "su compañero / su compañera de piso", "Usted y su compañero / su compañera de piso quieren invitar a unos amigos a cenar en casa el sábado.", ["a cuántas personas van a invitar y a quiénes;", "qué van a cocinar (y si alguien no puede comer algo);", "qué tienen que comprar y dónde;", "cómo van a repartir las tareas: cocinar, poner la mesa, limpiar;", "a qué hora empieza la cena."]),
 (4, "La visita de una amiga extranjera", "tu", "su amigo / su amiga", "Emma, una amiga irlandesa de usted y de su amigo / su amiga, viene a pasar cuatro días a su ciudad. Ustedes quieren organizar su visita.", ["dónde va a dormir Emma;", "quién va a buscarla al aeropuerto y cómo;", "qué lugares de la ciudad le van a enseñar;", "a qué restaurantes o bares la van a llevar;", "qué van a hacer la última noche."]),
 (5, "Ir a un concierto", "tu", "su amigo / su amiga", "Su grupo de música favorito, Los Girasoles, da un concierto en su ciudad el mes que viene. Usted quiere ir con un amigo / una amiga.", ["qué música le gusta y por qué le gusta ese grupo;", "si ha ido antes a algún concierto: cuál, dónde, con quién;", "cómo van a comprar las entradas y cuánto cuestan;", "qué van a hacer antes del concierto;", "cómo van a volver a casa."]),
 (6, "La comida de despedida de una compañera", "tu", "su compañero / su compañera de trabajo", "Pilar, una compañera de su trabajo, se jubila después de treinta años en la empresa. Usted y otro compañero / otra compañera quieren organizarle una comida de despedida.", ["qué día y dónde van a hacer la comida;", "a quién van a invitar;", "cuánto dinero tiene que poner cada persona;", "qué regalo le van a hacer y por qué;", "qué tiene que hacer cada uno."]),
 (7, "En la farmacia: un resfriado", "usted", "el farmacéutico / la farmacéutica", "Usted está de viaje y tiene un resfriado muy fuerte. Entra en una farmacia.", ["saludar y explicar qué le pasa y desde cuándo;", "pedir algo para el resfriado;", "preguntar cómo y cuándo tiene que tomarlo;", "preguntar el precio y pagar;", "preguntar qué más puede hacer para estar mejor."]),
 (8, "Comprar un billete de tren", "usted", "el empleado / la empleada de la taquilla", "Usted quiere ir en tren a otra ciudad el viernes para ver a su familia. Está en la taquilla de la estación.", ["saludar y decir adónde quiere ir, qué día y a qué hora;", "preguntar el precio y si hay descuentos;", "elegir el asiento;", "preguntar cuánto tarda el tren y desde qué andén sale;", "pagar y despedirse."]),
 (9, "Reservar mesa por teléfono", "usted", "un empleado / una empleada del restaurante", "Usted quiere celebrar el cumpleaños de su madre en un restaurante el sábado. Llama por teléfono para reservar una mesa.", ["saludar y decir para cuántas personas, qué día y a qué hora quiere la mesa;", "pedir una mesa en un sitio concreto (terraza, al lado de la ventana...);", "preguntar por el menú y los precios;", "explicar si alguien no puede comer algo;", "dar su nombre y su teléfono y despedirse."]),
 (10, "Apuntarse a un gimnasio", "usted", "el recepcionista / la recepcionista del gimnasio", "Usted quiere apuntarse a un gimnasio de su barrio. Está en la recepción.", ["saludar y decir qué actividades le interesan y por qué;", "preguntar el horario de las clases;", "preguntar el precio y cómo se paga;", "preguntar qué necesita para apuntarse;", "decir si se apunta y despedirse."]),
 (11, "Cambiar unos auriculares que no funcionan", "usted", "el dependiente / la dependienta", "Hace una semana usted compró unos auriculares en una tienda de electrónica y no funcionan bien. Vuelve a la tienda.", ["saludar y explicar qué compró y cuándo;", "explicar qué problema tienen;", "pedir otros auriculares o el dinero;", "elegir otro modelo y preguntar las diferencias;", "despedirse."]),
 (12, "Enviar un paquete en correos", "usted", "el empleado / la empleada de correos", "Usted quiere enviar un paquete con regalos a su familia, que vive en otro país. Está en una oficina de correos.", ["saludar y explicar qué quiere enviar y adónde;", "preguntar las formas de envío, los precios y cuánto tarda en llegar;", "elegir una forma de envío;", "preguntar cómo puede saber dónde está el paquete;", "pagar y despedirse."]),
]
# Sucesos de bloqueo en "Ahora tu" para la tarea 3 (el texto del examinador depende del trato)
SUCESOS_T3 = {
 "entiendo": {"tu": "El examinador habla muy deprisa: «Oye, ¿te viene bien o te pilla fatal?». No lo entiendes.",
              "usted": "El examinador habla muy deprisa: «¿Le viene bien o prefiere otra opción?». No lo entiendes."},
 "no": {"tu": "Pequeño problema: el examinador te dice que no a tu idea. Reacciona y propón otra cosa.",
        "usted": "Pequeño problema: el examinador dice que no hay o que no se puede. Reacciona y busca otra solución."},
 "dialogo": {"tu": "El examinador te pregunta: «¿Y tú qué opinas?» y no tienes opinión.",
             "usted": "El examinador pregunta: «¿Y usted qué prefiere?» y no lo sabes."},
}

# ============================================================ ENTRAR Y TERMINAR (NUEVO, 23/10/2026)
# Pestaña 1. Lo OFICIAL (Guía del examen DELE A2, «Administración» de la prueba oral; Modelo 0) va en "o";
# lo HABITUAL (lo que suele pasar y dicen los examinadores, pero no está escrito en la Guía) va en "h".
# "tu": lo que haces tú en ese momento (consejo nuestro).
DIA_ORAL = [
 {"t": "La sala de preparación", "ico": "1",
  "o": ["Tienes <b>12 minutos</b> para preparar las tres tareas.",
        "En la tarea 1 eliges uno de los dos temas.",
        "Puedes tomar notas y hacer un esquema. Después, en el examen, puedes mirarlos, pero no leerlos."],
  "h": ["Te dan las láminas y papel para las notas.", "Alguien te avisa cuando se termina el tiempo y te acompaña a la sala del examen."],
  "tu": "Reparte el tiempo: unos 5 minutos para la tarea 1, 4 para la foto y 3 para la tarea 3. Escribe palabras clave, no frases enteras."},
 {"t": "La sala del examen", "ico": "2",
  "o": ["Hay <b>dos examinadores</b>. El entrevistador habla contigo y hace un papel en la tarea 3. El calificador solo escucha y pone la nota: no habla."],
  "h": ["Te saludan y te dicen: «Siéntese, por favor».", "El calificador está un poco más lejos y escribe todo el tiempo. Es su trabajo: no es una mala señal."],
  "tu": "Saluda («Buenos días» o «Buenas tardes»), siéntate y pon las notas delante. Cuando hablas, mira al entrevistador."},
 {"t": "Las preguntas de contacto", "ico": "3",
  "o": ["Primero hay unas preguntas para romper el hielo y para que estés más tranquilo. <b>No se evalúan.</b>"],
  "h": ["Te piden el documento de identidad.", "Te preguntan cómo te llamas, de dónde eres, a qué te dedicas, desde cuándo estudias español...",
        "Al final te preguntan: «¿Qué opción ha elegido?»."],
  "tu": "Contesta con una frase completa y un detalle pequeño. Es tu calentamiento: ni una palabra sola ni un discurso."},
 {"t": "La tarea 1: el monólogo", "ico": "4",
  "o": ["Hablas tú solo <b>de 2 a 3 minutos</b> sobre el tema que has elegido."],
  "h": ["«Muy bien. Ya puede empezar.»", "Si te pasas mucho de tiempo, el examinador te para con un gesto o con una frase."],
  "tu": "Di el tema, sigue tus notas pauta por pauta y cierra con una frase: «Y eso es todo sobre...»."},
 {"t": "El paso a la foto (tarea 2)", "ico": "5",
  "o": ["Describes la foto <b>de 2 a 3 minutos</b>. La lámina tiene unas preguntas para ayudarte."],
  "h": ["«Muy bien. Pasamos a la foto.»"],
  "tu": "Respira, mira la foto un segundo y empieza por lo general: dónde están y quiénes son. Cierra con «En resumen, en la foto veo...»."},
 {"t": "La tarea 3: el diálogo", "ico": "6",
  "o": ["Hablas con el entrevistador <b>de 3 a 4 minutos</b> en una situación imaginaria relacionada con la foto. Él hace un papel."],
  "h": ["El examinador te recuerda la situación y su papel antes de empezar.",
        "En los exámenes publicados, el diálogo es de tú: con un amigo, un hermano o un compañero de piso."],
  "tu": "Responde, añade un detalle y pregunta. Cuando el plan está claro, el examinador termina."},
 {"t": "El final", "ico": "7",
  "o": [],
  "h": ["«Muy bien, hemos terminado. Muchas gracias.»", "Dejas en la mesa las láminas y tus notas: no te las llevas.",
        "No te dicen la nota en la sala: los resultados llegan después."],
  "tu": "«Gracias a ustedes. Hasta luego.» Y sales tranquilo: lo difícil ya está hecho."},
]

# Preguntas de contacto (de usted). h = habitual (no está en la Guía). fijo: "ini" sale siempre la primera,
# "nom" la segunda, "fin" la última; el resto, al azar. mod = respuesta modelo de Anna, una candidata;
# evita = una respuesta que no conviene (con el porqué).
CONTACTO = [
 {"q": "Buenos días. ¿Me deja su documento de identidad, por favor?", "h": True, "fijo": "ini",
  "mod": "Sí, claro. Aquí tiene.", "evita": "(Lo das sin decir nada.)", "por": "Una frase educada y corta: es el primer contacto."},
 {"q": "¿Cómo se llama?", "h": False, "fijo": "nom",
  "mod": "Me llamo Anna Kowalska, pero todos me llaman Ania.", "evita": "Anna.", "por": "Una frase completa y un detalle. Una palabra sola suena a nervios."},
 {"q": "¿De dónde es? ¿Y dónde vive ahora?", "h": False,
  "mod": "Soy de Cracovia, en Polonia, pero ahora vivo en Alicante, cerca del mar.", "evita": "Polonia. Alicante.", "por": "Contestas las dos preguntas con frases y un detalle."},
 {"q": "¿A qué se dedica?", "h": False,
  "mod": "Soy enfermera. Trabajo en un hospital, casi siempre por la mañana.", "evita": "Enfermera.", "por": "La profesión y un detalle: dónde o cuándo trabajas."},
 {"q": "¿Desde cuándo estudia español?", "h": False,
  "mod": "Desde hace dos años. Voy a clase dos tardes a la semana.",
  "evita": "Empecé en 2019 con una aplicación, después lo dejé, en 2022 volví a empezar con una profesora que era de Sevilla y...",
  "por": "Una respuesta corta y clara. Esto no es la tarea 1: no hace falta contar toda la historia."},
 {"q": "¿Por qué estudia español?", "h": False,
  "mod": "Porque vivo aquí y quiero hablar mejor con mis compañeros del hospital.", "evita": "Porque sí.", "por": "Un motivo de verdad, con «porque»."},
 {"q": "¿Qué tal ha venido? ¿Ha encontrado bien el sitio?", "h": False,
  "mod": "Sí, muy bien. He venido en autobús y no ha sido difícil.", "evita": "Sí.", "por": "Contestas y añades cómo has venido."},
 {"q": "¿Qué tal está? ¿Muchos nervios?", "h": False,
  "mod": "Un poco, la verdad, pero estoy bien. Gracias.", "evita": "¡Muchísimos! No he dormido nada y no sé si voy a poder hablar...",
  "por": "Es normal estar nervioso y puedes decirlo, pero con calma y en una frase."},
 {"q": "Muy bien. ¿Qué opción ha elegido para la tarea 1?", "h": True, "fijo": "fin",
  "mod": "He elegido la opción 1: mi plato favorito.", "evita": "La uno.", "por": "Dices la opción y el tema: así empiezas la tarea 1 con seguridad."},
]

# Formulas para CERRAR la tarea 1 y la tarea 2 (A2, sin subjuntivo). Sin tú ni usted (el build lo comprueba).
CIERRES = {
 "T1": ["Y eso es todo sobre [el tema].", "Para terminar, creo que...", "Por eso [es / fue] tan importante para mí.", "Bueno, pues eso es lo más importante."],
 "T2": ["En resumen, en la foto veo a...", "Creo que es un día especial y que después van a...", "Para terminar, me parece una foto alegre / tranquila porque...", "Y eso es lo que veo en la foto."],
}
# Cierres que NO: (lo que dices, por que no)
CIERRES_MAL = [
 ("«Ya está.» / «Fin.»", "Corta de golpe: el examinador no sabe si has terminado o si te has bloqueado."),
 ("«No sé más.»", "Suena a bloqueo, no a final. Si te quedas en blanco, vuelve a la lámina."),
 ("Te callas y miras al examinador.", "Un silencio largo al final también cuenta como silencio."),
 ("«Eso es todo» a los 40 segundos", "Cerrar demasiado pronto: faltan pautas y tiempo. Cierra solo cuando has hablado de todo."),
]
# Despedida (final de la oral): examinador (habitual) y candidato
DESPEDIDA = {"e": "Muy bien, hemos terminado. Muchas gracias.", "c": ["Gracias a ustedes. Hasta luego.", "Muchas gracias. Adiós, buenos días."]}

# EJERCICIO «ELIGE EL CIERRE». tarea · ctx (lo que pasa) · e (lo que dice el examinador, opcional) · trato de la
# respuesta buena (None = monólogo) · ops · ok · por. tipo: "cierre" (hay que cerrar bien) o "pronto" (todavía no
# hay que cerrar) o "final" (despedida).
ELIGE_CIERRE = [
 {"tarea": "Tarea 1", "tipo": "cierre", "trato": None,
  "ctx": "«Mi plato favorito». Llevas 2 minutos y 40 segundos y has hablado de las cinco pautas.",
  "ops": ["Ya está.", "Y eso es todo sobre mi plato favorito. Para terminar, creo que la comida es una forma de estar con la familia.", "(Te callas y miras al examinador.)"],
  "ok": 1, "por": "Una fórmula para cerrar y una frase con tu opinión. «Ya está» corta de golpe y el silencio no dice nada."},
 {"tarea": "Tarea 1", "tipo": "cierre", "trato": None,
  "ctx": "«Mis mejores vacaciones». Has terminado la última pauta: tus próximas vacaciones.",
  "ops": ["...y el año que viene vamos a ir a Portugal. Por eso esas vacaciones fueron tan importantes para mí: fueron las primeras con mis hijos.",
          "...y el año que viene vamos a ir a Portugal. Fin.", "...y el año que viene vamos a ir a Portugal. ¿Y usted adónde va de vacaciones?"],
  "ok": 0, "por": "Una frase que une el final con el principio del monólogo. «Fin» corta de golpe, y en el monólogo no le haces preguntas al examinador."},
 {"tarea": "Tarea 1", "tipo": "pronto", "trato": None,
  "ctx": "«Una persona importante en mi vida». Llevas 50 segundos, has hablado de dos pautas y te quedas en blanco.",
  "ops": ["Y eso es todo sobre mi amiga Lucía.", "Bueno, ahora voy a hablar de cuándo la conocí: fue en un curso de fotografía, hace seis años...", "Perdón, no sé más."],
  "ok": 1, "por": "Todavía no es el momento de cerrar: faltan pautas y tiempo. Vuelve a la lámina y pasa a la pauta siguiente."},
 {"tarea": "Tarea 1", "tipo": "cierre", "trato": None,
  "ctx": "«Un regalo que he recibido». El examinador te hace un gesto: se termina el tiempo. Estás en la pauta 4 y te falta la 5.",
  "ops": ["(Sigues hablando de la pauta 4 un minuto más.)", "...y de pequeño recibía muchos juguetes. Y para terminar: mi próximo regalo es para mi madre, un viaje a Italia.", "Perdón, perdón, no he terminado..."],
  "ok": 1, "por": "Si se acaba el tiempo, di una frase rápida sobre la última pauta y cierra. Así no queda ninguna pauta sin tocar."},
 {"tarea": "Tarea 1", "tipo": "cierre", "trato": None,
  "ctx": "«Mi casa». Has hablado de las cinco pautas.",
  "ops": ["En resumen, en la foto veo una casa bonita.", "Bueno, pues eso es lo más importante de mi casa. Para terminar, creo que es pequeña, pero es mi sitio favorito.", "Y eso. Nada más."],
  "ok": 1, "por": "«En la foto veo...» es el cierre de la tarea 2, no del monólogo. «Y eso. Nada más» corta de golpe."},
 {"tarea": "Tarea 2", "tipo": "cierre", "trato": None,
  "ctx": "Foto «En la lavandería». Has contestado las seis preguntas de la lámina.",
  "ops": ["En resumen, en la foto veo a un chico con un problema con la lavadora y a un señor que se ríe. Creo que después van a limpiar todo juntos.",
          "Y la lavadora es blanca. Ya está.", "En mi casa la lavadora también es blanca y es muy vieja."],
  "ok": 0, "por": "Un resumen de la escena y lo que van a hacer después. Hablar de tu casa no es describir la foto."},
 {"tarea": "Tarea 2", "tipo": "cierre", "trato": None,
  "ctx": "Foto «Regalos». Te quedan unos segundos.",
  "ops": ["Para terminar, me parece una foto alegre porque las dos amigas están contentas y hay una tarta con una vela.", "Bueno, no sé qué más decir.", "Y para terminar, una pregunta: ¿le gustan las bufandas?"],
  "ok": 0, "por": "Una opinión sobre la foto con un porqué. En la tarea 2 no le haces preguntas al examinador."},
 {"tarea": "Tarea 2", "tipo": "pronto", "trato": None,
  "ctx": "Foto «Hacer deporte». Llevas un minuto. Has hablado de las personas y del lugar.",
  "ops": ["Y eso es lo que veo en la foto.", "A ver, ¿qué están haciendo? Pues se dan la mano porque ha terminado el partido...", "En resumen, son cuatro amigos."],
  "ok": 1, "por": "Todavía faltan preguntas de la lámina: qué hacen, qué relación tienen, cómo se sienten, qué han hecho antes. No cierres todavía."},
 {"tarea": "Tarea 2", "tipo": "cierre", "trato": None,
  "ctx": "Foto «Una comida en el campo». Has hablado de lo que ves, de la relación entre las personas y de cómo se sienten.",
  "ops": ["Creo que es un día especial: es el cumpleaños de la abuela. Después van a comer la tarta y a hacer fotos. Y eso es lo que veo en la foto.",
          "Es un olivo. Fin.", "(Miras la foto en silencio hasta que el examinador habla.)"],
  "ok": 0, "por": "Cierras con el antes y el después (la última pregunta de la lámina) y una fórmula. Así el examinador sabe que has terminado."},
 {"tarea": "Final", "tipo": "final", "trato": "usted",
  "ctx": "Termina la tarea 3. El examinador te dice:", "e": "Muy bien, hemos terminado. Muchas gracias.",
  "ops": ["Gracias a ustedes. Hasta luego.", "¿Ya está? ¿He aprobado?", "(Te levantas y te llevas las notas.)"],
  "ok": 0, "por": "Una despedida educada y sencilla. La nota no te la dicen en la sala, y las notas y las láminas se quedan en la mesa."},
]

# PRACTICA «TE QUEDAN 20 SEGUNDOS: CIERRA». k: tarea (T1 = id de FUENTES_T1; T2 = id de FUENTES_T2, sale su foto) ·
# dicho: lo que ya has dicho (una línea por pauta o pregunta) · mod: dos cierres modelo (sin tú ni usted).
CIERRA_20 = [
 {"k": "T1", "id": 3, "dicho": ["La paella de mi suegra: arroz, pollo y judías verdes.", "La última vez: el domingo pasado, en su casa, con toda la familia.",
   "De niña comía mucha sopa y mucho pescado.", "En casa cocina mi pareja; yo pongo la mesa.", "Próxima comida especial: el cumpleaños de mi hijo."],
  "mod": ["Y eso es todo sobre mi plato favorito. Para terminar, creo que la paella es especial porque siempre la comemos todos juntos.",
          "Bueno, pues eso es lo más importante. Por eso la paella es mi plato favorito: me recuerda los domingos en familia."]},
 {"k": "T1", "id": 8, "dicho": ["Tenerife, en 2019, en avión, con mi hermana.", "Un apartamento cerca de la playa, diez días; subimos al volcán.",
   "Fueron las mejores porque estuvimos juntas después de mucho tiempo.", "De pequeño iba siempre al pueblo de mis abuelos.", "Próximas vacaciones: Escocia, con unos amigos."],
  "mod": ["Y eso es todo sobre mis mejores vacaciones. Para terminar, creo que lo mejor fue estar con mi hermana, porque ahora vivimos lejos.",
          "Bueno, pues eso es lo más importante. Por eso fueron unas vacaciones tan especiales para mí."]},
 {"k": "T1", "id": 6, "dicho": ["Un curso de cocina japonesa, en 2023, en Valencia: quería aprender a hacer sushi.", "El profesor era muy simpático; los compañeros, de muchos países.",
   "Me gustó cocinar en grupo; no me gustó el horario, muy tarde.", "En el colegio me gustaba mucho la música.", "En el futuro: un curso de fotografía."],
  "mod": ["Y eso es todo sobre mi curso de cocina. Para terminar, creo que aprender cosas nuevas es muy bueno a cualquier edad.",
          "Bueno, pues eso es lo más importante. Por eso fue un curso tan especial para mí: ahora hago sushi para mis amigos."]},
 {"k": "T1", "id": 15, "dicho": ["Leo, camino por la playa y quedo con amigos.", "El fin de semana pasado fui a un concierto al aire libre.",
   "De adolescente jugaba al baloncesto todos los días.", "Es importante para descansar y no pensar en el trabajo.", "El próximo fin de semana voy a ir a la montaña."],
  "mod": ["Y eso es todo sobre mi tiempo libre. Para terminar, creo que tener tiempo para mí es tan importante como trabajar.",
          "Bueno, pues eso es lo más importante. Por eso los domingos no miro el móvil del trabajo: es mi día para descansar."]},
 {"k": "T2", "id": 3, "dicho": ["Una lavandería, de noche: lavadoras y secadoras.", "Un chico joven, pelirrojo, y un señor mayor con zapatillas de casa.",
   "Sale mucha espuma de la lavadora; el chico está preocupado.", "El señor se ríe: creo que no se conocen.", "Antes, el chico ha puesto mucho detergente."],
  "mod": ["En resumen, en la foto veo a un chico con un pequeño problema y a un señor muy simpático. Creo que después van a limpiar la espuma juntos.",
          "Para terminar, me parece una foto divertida, porque el problema no es grave y el señor se lo pasa muy bien. Y eso es lo que veo en la foto."]},
 {"k": "T2", "id": 7, "dicho": ["El recibidor de un piso, por la mañana: un perchero, un espejo, mochilas.", "Una madre y un niño pequeño.",
   "La madre mira la hora; el niño busca un zapato.", "Creo que son madre e hijo y que llegan tarde al colegio.", "La madre está nerviosa; el niño, tranquilo."],
  "mod": ["En resumen, en la foto veo una mañana normal en una familia con prisa. Creo que después van a encontrar el zapato y van a salir corriendo.",
          "Para terminar, me parece una foto muy real, porque todas las familias tienen mañanas así. Y eso es lo que veo en la foto."]},
 {"k": "T2", "id": 9, "dicho": ["La caja de un supermercado: la cinta, bolsas, un carro.", "Un señor mayor y una cajera joven.",
   "El señor busca la cartera en los bolsillos; la cajera espera.", "No se conocen, pero creo que él compra allí todos los días.", "La cajera sonríe: está tranquila."],
  "mod": ["En resumen, en la foto veo a un señor que no encuentra la cartera y a una cajera muy paciente. Creo que después él va a pagar con el móvil.",
          "Para terminar, me parece una foto tranquila, porque nadie está enfadado. Y eso es lo que veo en la foto."]},
 {"k": "T2", "id": 11, "dicho": ["Un salón: un sofá, cojines, palomitas en la mesa.", "Tres amigos jóvenes, en ropa de casa.",
   "Ven un partido de fútbol en la tele; dos saltan de alegría.", "El tercero se tapa la cara: creo que es de otro equipo.", "Antes han preparado las palomitas."],
  "mod": ["En resumen, en la foto veo a tres amigos que ven un partido y un gol muy importante. Creo que después van a cenar juntos y a hablar del partido.",
          "Para terminar, me parece una foto alegre, pero uno de los amigos está triste porque su equipo pierde. Y eso es lo que veo en la foto."]},
]
