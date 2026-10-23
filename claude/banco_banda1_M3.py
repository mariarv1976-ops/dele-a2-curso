# -*- coding: utf-8 -*-
# BANCO DE "DE LA BANDA 1 A LA BANDA 2" (MODULO 3 · TALLER DE ESCRITURA · PIEZA 3) DEL CURSO DE PREPARACION DELE A2
# Lo usa build_M3_banda1.py. Para cambiar contenidos, solo se toca este archivo.
#
# CLAVES DE LOS FALLOS (diagnóstico y rescate):
#   pautas   una pauta falta, está a medias o contesta otra cosa (cumplimiento)
#   tipo     no es el tipo de texto que piden: describe las fotos, copia la ficha (cumplimiento)
#   entiende una frase que no se entiende: verbos sin conjugar, palabras de otra lengua, desorden
#   con      todo con «y» / «porque»: faltan conectores
#   gram     verbos (pasados) y concordancias
#   trato    tú y usted mezclados
#   lin      texto muy corto (no se marca en las frases: el build lo calcula con las palabras del original)
# LA OPERACIÓN RESCATE: 5 pasos en un orden fijo (PASOS). pautas y tipo -> paso 1; entiende -> 2; con -> 3;
#   gram y trato -> 4; lin -> 5.
# TEXTOS PARA RESCATAR: "seg" = frases del original, cada una {"p": pauta, "t": texto} y, si tiene un fallo,
#   "fix" (cómo queda en la versión de banda 2), "k" (clave del fallo) y "por" (explicación corta).
#   "add" = frases que faltan en el original: {"p": pauta, "ops": [la buena, otra, otra], "por": ...}; la
#   buena (ops[0]) se añade a la versión rescatada detrás de la última frase de esa pauta.
#   "diag" = explicación de cada fallo que tiene el texto (las claves tienen que ser justo las que tiene).
# El build comprueba: palabras de cada versión rescatada dentro del límite de su tarea, una frase para cada
#   pauta en la versión rescatada, que en el original fallan al menos dos pautas o hay frases que no se
#   entienden, tú/usted coherente en las versiones rescatadas, que cada corrección es distinta del original
#   y tiene su explicación, y que "diag" explica justo los fallos que tiene el texto.
# FOTOS (12/10/2026): las laminas con fotos llevan "photos" (descripcion = texto alternativo), "img" (nombre fijo
# de las imagenes), "persona" y "escenas" (para los prompts). Ver fotos_M3.py.

# ------------------------------------------------------------------ 1. LA BANDA 1
IDEA = ("Un texto de banda 1 casi nunca está lejos del aprobado.",
        "Suele fallar por dos o tres cosas concretas: una pauta que falta, unas frases que no se entienden, todo con «y». Si aprendes a verlas, las arreglas en tu propio texto.")

QUE_ES = [  # (nota, pregunta, [(qué pasa, ejemplo)])
 ("Cumplimiento de la tarea", "¿Qué dices?",
  [("Fallan dos pautas o más: faltan, están a medias o no se entienden.", "No dice si va a la fiesta ni propone otro día."),
   ("El texto es muy corto: la información no llega.", "Cuatro líneas en la tarea 2, que pide siete u ocho."),
   ("No es el tipo de texto que piden.", "Describe las fotos («En la foto 1 hay...») o copia la ficha de datos.")]),
 ("Uso de la lengua", "¿Cómo lo dices?",
  [("Frases sueltas, sin unir.", "Fui a la playa. Comí. Nadé. Volví."),
   ("Solo «y» y «porque».", "Comimos y bailamos y cantamos y volvimos porque era tarde."),
   ("Errores que hacen difícil entender el mensaje.", "«Yo ayer no poder ir, trabajo mi.»")]),
]

BANDA2 = ("En la banda 2 también hay errores: «mis amigo», «ayer he ido», «la comida estaba bueno». "
          "La diferencia es que <b>se entiende todo a la primera</b> y <b>están todas las pautas</b>.")

ESCALA = [  # (pautas que fallan, cumplimiento, clase)
 ("Ninguna", "2 o 3: depende de los detalles que añadas.", "ok"),
 ("Una (falta, está a medias o no se entiende)", "Todavía 2, pero <b>en el límite</b>: ya no puede ser 3.", "mid"),
 ("Dos o más", "<b>1: banda 1</b>, aunque tu español sea muy bueno.", "bad"),
]
ESCALA_NOTA = ("Son dos notas separadas. El uso de la lengua no arregla una pauta que falta, y unas pautas completas "
               "no arreglan frases que no se entienden. Para aprobar, las dos en banda 2.")

# ------------------------------------------------------------------ 2. LOS FALLOS
FALLOS = [  # clave, nombre, nota, ejemplo mal, arreglo rápido, truco
 {"k": "pautas", "n": "Pautas que faltan o a medias", "nota": "Cumplimiento",
  "mal": "Pauta «decir si va a ir y por qué»: <i>Sí, voy a ir.</i>",
  "bien": "<i>Sí, voy a ir, <b>porque es tu cumpleaños</b>.</i>",
  "truco": "Con la mini lista: cada pieza de la pauta, su frase. «Y por qué» es una pieza más."},
 {"k": "lin", "n": "Texto muy corto", "nota": "Cumplimiento",
  "mal": "Tarea 2 con cuatro líneas (unas 40 palabras).",
  "bien": "Una frase más en las pautas más cortas: un porqué, un detalle, cómo te sentiste.",
  "truco": "Cuenta las líneas a ojo: tarea 1, unas 6-7; tarea 2, unas 7-8."},
 {"k": "entiende", "n": "Frases que no se entienden", "nota": "Uso de la lengua",
  "mal": "<i>Yo ayer cine Marta, no gusta, mucho larga.</i>",
  "bien": "<i>Ayer fui al cine con Marta, pero la película no me gustó: era muy larga.</i>",
  "truco": "Frase corta: quién + verbo conjugado + lo demás. Sin palabras de otra lengua: si no sabes una palabra, di la idea con otras."},
 {"k": "tipo", "n": "Describir las fotos en presente", "nota": "Cumplimiento",
  "mal": "<i>En la foto 1 hay una playa y llueve.</i>",
  "bien": "<i>Cuando llegamos a la playa, empezó a llover.</i>",
  "truco": "Las fotos son tu día: lo cuentas en pasado y en primera persona. «En la foto hay...» es la oral, no la escritura."},
 {"k": "otra", "n": "Contestar otra cosa", "nota": "Cumplimiento",
  "mal": "Pauta «qué planes tiene para el verano»: <i>El verano pasado fui a Italia.</i>",
  "bien": "<i>Este verano <b>voy a ir</b> a Grecia con mi hermana.</i>",
  "truco": "Mira el tiempo de la pauta: «planes» es futuro; «qué hizo», pasado; «cómo es», presente."},
 {"k": "trato", "n": "Tú y usted mezclados", "nota": "Las dos",
  "mal": "<i>Estimada señora Ruiz: ... ¿Puedes decirme el precio? ... Un beso,</i>",
  "bien": "<i>Estimada señora Ruiz: ... ¿<b>Puede</b> decirme el precio? ... <b>Un saludo</b>,</i>",
  "truco": "Escribe TÚ o USTED arriba de tu mini lista y mira el saludo, la despedida y las preguntas."},
 {"k": "con", "n": "Todo con «y»", "nota": "Uso de la lengua",
  "mal": "<i>Fuimos a la playa y comimos y nadamos y volvimos tarde.</i>",
  "bien": "<i><b>Primero</b> fuimos a la playa, <b>después</b> comimos y nadamos y, <b>al final</b>, volvimos tarde.</i>",
  "truco": "Si ves tres «y» en una frase, cambia una por primero, después, además, por eso o al final."},
]

# ------------------------------------------------------------------ 3. LA OPERACIÓN RESCATE (orden fijo)
PASOS = [
 {"k": "pautas", "n": "Completa las pautas", "trae": ["pautas", "tipo"],
  "que": "Con la lámina al lado, busca la frase de cada pieza de cada pauta. Si falta, escríbela. Si responde a otra cosa (pasado en vez de planes, la foto en vez de la historia), cámbiala.",
  "por": "Va primero porque es lo que más cuenta: con dos pautas que fallan, el cumplimiento es banda 1 aunque el resto esté perfecto.",
  "items": ["He añadido una pauta que faltaba.", "He completado una pauta que estaba a medias.", "He cambiado una frase que contestaba otra cosa (otro tiempo, la foto, la ficha).", "Ahora todas las pautas tienen su frase."]},
 {"k": "entiende", "n": "Que cada frase se entienda", "trae": ["entiende"],
  "que": "Lee frase por frase. Si una frase no se entiende a la primera, hazla más corta y más sencilla: quién + verbo conjugado + lo demás.",
  "por": "Una frase que no se entiende es como una pauta que no está: el corrector no puede adivinar lo que querías decir.",
  "items": ["He conjugado un verbo que estaba en infinitivo (yo trabajar → trabajo).", "He cambiado una palabra de otra lengua.", "He partido o he ordenado una frase muy larga o desordenada.", "Ahora cada frase se entiende a la primera."]},
 {"k": "con", "n": "Ordena con conectores", "trae": ["con"],
  "que": "Busca las cadenas de «y... y... y» y los «porque... porque». Cambia uno o dos por un conector básico: primero, después, pero, además, por eso, así que, al final.",
  "por": "Con tres o cuatro conectores distintos, el texto ya no son frases sueltas: es lo que pide la banda 2.",
  "items": ["He cambiado una cadena de «y... y... y».", "He usado primero, después o al final para ordenar.", "He usado pero, además, por eso o así que.", "Hay al menos tres conectores distintos."]},
 {"k": "gram", "n": "Verbos, concordancias y trato", "trae": ["gram", "trato"],
  "que": "Ahora sí, los errores pequeños: los pasados (fui / era / he ido), las concordancias (mis amigos, la comida buena) y el mismo trato del saludo a la despedida.",
  "por": "Va después porque un error pequeño baja menos la nota que una pauta que falta o una frase que no se entiende.",
  "items": ["He corregido un pasado.", "He corregido una concordancia o un posesivo.", "He corregido hay / está / es o muy / mucho.", "Todo el texto tiene el mismo trato (tú o usted)."]},
 {"k": "lin", "n": "Cuenta las líneas", "trae": ["lin"],
  "que": "A ojo, unas 10 palabras por línea: tarea 1, unas 6-7 líneas; tarea 2, unas 7-8. Si es corto, añade un detalle o un porqué a la pauta más corta. Si es largo, quita lo que no pide ninguna pauta.",
  "por": "Va al final porque los pasos anteriores cambian la longitud: al completar las pautas, el texto crece.",
  "items": ["Tarea 1: unas 6-7 líneas · tarea 2: unas 7-8.", "Si era corto, he añadido un detalle a la pauta más corta.", "Si era largo, he quitado lo que no pide ninguna pauta."]},
]

# el texto que se transforma paso a paso (correo a una amiga, tarea 1)
DEMO = {
 "autor": "Mila",
 "lamina": {"tarea": 1, "instr": "Una amiga le escribe porque se va a vivir a otro país.",
   "input": ["¡Hola! ¡Me voy a trabajar a Berlín! El sábado hago una fiesta de despedida en mi casa. ¿Vienes? ¿Me ayudas a preparar la comida? Y una pregunta: tú has vivido en Alemania, ¿qué me recomiendas llevar?", "Un beso, Clara"],
   "lead": "Conteste a su amiga. En el correo tiene que:",
   "pautas": ["saludar;", "decir si va a ir a la fiesta y por qué;", "decir si puede ayudarla con la comida;", "darle un consejo para su viaje;", "despedirse."]},
 # etapas: 0 = original; 1-5 = después de cada paso de la operación rescate
 "etapas": [
  "¡Hola Clara! ¡Enhorabuena por el trabajo!\nSí, voy a tu fiesta. Por la mañana yo trabajar y por la tarde yo cocinar contigo y llevo una tortilla y unos bebidas y mi novio viene también.\nEn Berlín es mucho frío.\nHasta luego",
  "¡Hola, Clara! ¡Enhorabuena por el trabajo!\nSí, voy a tu fiesta, porque eres mi mejor amiga. Por la mañana yo trabajar y por la tarde yo cocinar contigo y llevo una tortilla y unos bebidas y mi novio viene también.\nEn Berlín es mucho frío. Te recomiendo llevar un abrigo bueno.\nUn beso,\nMila",
  "¡Hola, Clara! ¡Enhorabuena por el trabajo!\nSí, voy a tu fiesta, porque eres mi mejor amiga. Por la mañana trabajo y por la tarde puedo ayudarte con la comida y llevo una tortilla y unos bebidas y mi novio viene también.\nEn Berlín es mucho frío. Te recomiendo llevar un abrigo bueno.\nUn beso,\nMila",
  "¡Hola, Clara! ¡Enhorabuena por el trabajo!\nSí, voy a tu fiesta, porque eres mi mejor amiga. Por la mañana trabajo, pero por la tarde puedo ayudarte con la comida. Además, llevo una tortilla y unos bebidas. Mi novio también viene.\nEn Berlín es mucho frío, así que te recomiendo llevar un abrigo bueno.\nUn beso,\nMila",
  "¡Hola, Clara! ¡Enhorabuena por el trabajo!\nSí, voy a tu fiesta, porque eres mi mejor amiga. Por la mañana trabajo, pero por la tarde puedo ayudarte con la comida. Además, llevo una tortilla y unas bebidas. Mi novio también viene.\nEn Berlín hace mucho frío, así que te recomiendo llevar un abrigo bueno.\nUn beso,\nMila",
  "¡Hola, Clara! ¡Enhorabuena por el trabajo!\nSí, voy a tu fiesta, porque eres mi mejor amiga. Por la mañana trabajo, pero por la tarde puedo ayudarte con la comida. Además, llevo una tortilla y unas bebidas. Mi novio también viene.\nEn Berlín hace mucho frío, así que te recomiendo llevar un abrigo bueno y unas botas para la nieve.\nUn beso,\nMila",
 ],
 "notas": [  # qué hay mal en el original / qué se ha hecho en cada paso
  ["Pauta 2 a medias: dice que va, pero no por qué.", "Pauta 3 que no se entiende: «yo trabajar... yo cocinar contigo»: ¿puede ayudar o no?", "Pauta 4 que contesta otra cosa: «es mucho frío» no es un consejo.", "Sin despedida de verdad ni firma, todo con «y» y muy corto: unas 4 líneas."],
  ["Pauta 2: el porqué («porque eres mi mejor amiga»).", "Pauta 4: un consejo de verdad («Te recomiendo llevar un abrigo»).", "Pauta 5: «Un beso» y la firma."],
  ["«Yo trabajar... yo cocinar contigo» → «trabajo... puedo ayudarte con la comida»: verbos conjugados y la respuesta clara a la pauta 3."],
  ["Una frase con cuatro «y» → pero, además y una frase nueva.", "«así que» une el frío y el consejo."],
  ["«unos bebidas» → unas bebidas (femenino).", "«es mucho frío» → hace mucho frío."],
  ["Unas 4 líneas → unas 6 líneas: un detalle en la pauta 4 («y unas botas para la nieve»)."],
 ],
 # la versión final, frase a frase con su pauta (tiene que ser igual que la última etapa)
 "final": [[(1, "¡Hola, Clara! ¡Enhorabuena por el trabajo!")],
           [(2, "Sí, voy a tu fiesta, porque eres mi mejor amiga."), (3, "Por la mañana trabajo, pero por la tarde puedo ayudarte con la comida. Además, llevo una tortilla y unas bebidas. Mi novio también viene.")],
           [(4, "En Berlín hace mucho frío, así que te recomiendo llevar un abrigo bueno y unas botas para la nieve.")],
           [(5, "Un beso,")], [(0, "Mila")]],
}

# ------------------------------------------------------------------ 4. TEXTOS PARA RESCATAR (cinco tipos)
DIAG = [  # clave, lo que marca el estudiante
 ("pautas", "Falta una pauta, está a medias o contesta otra cosa"),
 ("tipo", "No es el tipo de texto: describe las fotos o copia la ficha"),
 ("entiende", "Hay frases que no se entienden"),
 ("con", "Todo con «y» o «porque»: faltan conectores"),
 ("gram", "Errores de verbos o de concordancia"),
 ("trato", "Mezcla tú y usted"),
 ("lin", "Es muy corto"),
]

RESCATE = [
# ============================================================ CORREO A UN AMIGO
{"id": "r1", "tipo": "Correo a un amigo", "autor": "Lena", "trato": "tu",
 "lamina": {"tarea": 1, "instr": "Un amigo le escribe porque va a vivir en su ciudad.",
   "input": ["¡Hola! ¡Tengo una noticia! El mes que viene me voy a vivir a tu ciudad: ¡tengo trabajo allí! ¿Qué barrio me recomiendas para vivir? Ah, y el sábado 12 hago la mudanza. ¿Me puedes ayudar?", "Un abrazo, Óscar"],
   "lead": "Conteste a su amigo. En el correo tiene que:",
   "pautas": ["saludar;", "recomendarle un barrio y explicar por qué;", "decir si puede ayudarle con la mudanza y por qué;", "proponerle un plan para su primer fin de semana en la ciudad;", "despedirse."]},
 "seg": [
  {"p": 1, "t": "¡Hola, Óscar! ¿Qué tal? ¡Qué bien que vienes a vivir aquí!"},
  {"p": 2, "t": "Te recomiendo el barrio del Carmen y es bonito y hay muchos bares y es cerca de mi casa.",
   "fix": "Te recomiendo el barrio del Carmen, porque es bonito y hay muchos bares. Además, está cerca de mi casa.", "k": "con",
   "por": "Tres «y» seguidas: con «porque» y «además» se ve cuál es la razón. Y para decir dónde: está cerca, no es cerca."},
  {"p": 3, "t": "El sábado yo no poder, mi trabajo.",
   "fix": "Lo siento, pero el sábado no puedo ayudarte con la mudanza, porque tengo que trabajar todo el día.", "k": "entiende",
   "por": "«Yo no poder, mi trabajo» no se entiende bien: ¿no puedes ayudar?, ¿por qué? Verbo conjugado (puedo) y la razón completa."},
  {"p": 4, "t": "El año pasado mi hermano también cambió de casa y fue muy cansado.",
   "fix": "¿Quieres dar un paseo por el barrio el domingo? Después podemos comer en mi restaurante favorito.", "k": "pautas",
   "por": "La pauta 4 pide proponer un plan y esta frase cuenta otra cosa (la mudanza de tu hermano). Una propuesta para el fin de semana sí responde."},
  {"p": 5, "t": "Un abrazo,"},
  {"p": 0, "t": "Lena"},
 ],
 "add": [],
 "diag": {"pautas": "La pauta 4 contesta otra cosa: cuenta la mudanza del hermano y no propone ningún plan.",
          "entiende": "«El sábado yo no poder, mi trabajo»: verbo sin conjugar y una frase rota. No se entiende bien la pauta 3.",
          "con": "«...y es bonito y hay muchos bares y es cerca...»: todo con «y».",
          "lin": "Unas 5 líneas: para la tarea 1 (6-7 líneas) es corto."},
 "leccion": "Lena sabe muchas palabras, pero dos pautas fallan (la 3 no se entiende y la 4 contesta otra cosa): banda 1. Con tres frases cambiadas, es un aprobado."},
# ============================================================ CORREO DE USTED
{"id": "r2", "tipo": "Correo de usted", "autor": "Ahmed", "trato": "usted",
 "lamina": {"tarea": 1, "instr": "Usted ha visto este anuncio en el polideportivo de su barrio.",
   "anuncio": ["PISCINA MUNICIPAL", "Cursos de natación para adultos: desde cero hasta nivel avanzado.", "Grupos de mañana y de tarde.", "Información: Sra. Ortega (natacion@piscinamunicipal.es)"],
   "lead": "Escriba un correo a la señora Ortega. En el correo tiene que:",
   "pautas": ["saludar;", "presentarse y explicar por qué le interesa el curso;", "decir si sabe nadar y qué nivel tiene;", "preguntar por los horarios y el precio;", "agradecer y despedirse."]},
 "seg": [
  {"p": 1, "t": "Estimada señora Ortega:"},
  {"p": 2, "t": "Me llamo Ahmed Benali y te escribo porque he visto tu anuncio en el polideportivo.",
   "fix": "Me llamo Ahmed Benali y le escribo porque he visto su anuncio en el polideportivo.", "k": "trato",
   "por": "Empieza de usted («Estimada señora Ortega»), así que sigue de usted: le escribo, su anuncio."},
  {"p": 2, "t": "Quiero aprender a nadar porque en verano voy mucho a la playa con mis hijos."},
  {"p": 3, "t": "Yo no swimming nunca, solo en el agua de poco.",
   "fix": "No sé nadar: nunca he ido a clases de natación.", "k": "entiende",
   "por": "«Swimming» es inglés y «el agua de poco» no se entiende. Una frase corta con palabras que conoces: no sé nadar."},
  {"p": 4, "t": "¿Qué horarios tienen los cursos?",
   "fix": "¿Qué horarios tienen los cursos de tarde y cuánto cuestan?", "k": "pautas",
   "por": "La pauta 4 tiene dos piezas: los horarios y el precio. Faltaba el precio: estaba a medias."},
  {"p": 4, "t": "¿Puedes enviarme la información?",
   "fix": "¿Puede enviarme la información por correo?", "k": "trato", "por": "De usted: puede."},
  {"p": 5, "t": "Muchas gracias. Un beso,",
   "fix": "Muchas gracias por su atención. Un saludo,", "k": "trato",
   "por": "«Un beso» es para amigos. De usted: un saludo, saludos cordiales, atentamente."},
  {"p": 0, "t": "Ahmed Benali"},
 ],
 "add": [],
 "diag": {"pautas": "La pauta 4 está a medias: pregunta los horarios, pero no el precio.",
          "entiende": "«Yo no swimming nunca, solo en el agua de poco»: una palabra en inglés y una frase que no se entiende. La pauta 3 no llega.",
          "trato": "Empieza de usted y sigue de tú: «te escribo», «tu anuncio», «¿puedes...?», «un beso»."},
 "leccion": "Ahmed tiene la longitud y casi todo bien escrito, pero la pauta 3 no se entiende y la 4 está a medias: banda 1 en el cumplimiento. Y el tú en un correo de usted también resta."},
# ============================================================ BLOG
{"id": "r3", "tipo": "Blog", "autor": "Nils", "trato": None,
 "lamina": {"tarea": 2, "op": 1, "intro": "Escriba una entrada en su blog sobre su último fin de semana. Hable de:",
   "pautas": ["dónde estuvo y con quién;", "qué hizo el sábado;", "qué hizo el domingo;", "qué fue lo mejor y lo peor;", "qué planes tiene para el próximo fin de semana."]},
 "seg": [
  {"p": 1, "t": "Hola a todos. El fin de semana estoy en Valencia con mi novia Sara.",
   "fix": "¡Hola a todos! El fin de semana pasado estuve en Valencia con mi novia, Sara.", "k": "gram",
   "por": "Ya ha pasado: estuve, no estoy. Con el presente, el lector no sabe si estás allí ahora."},
  {"p": 2, "t": "El sábado vamos a la playa y comemos paella y paseamos y volvemos tarde al hotel.",
   "fix": "El sábado fuimos a la playa. Primero comimos paella, después paseamos y, al final, volvimos tarde al hotel.", "k": "con",
   "por": "Todo con «y» y en presente. Con primero, después y al final se ve el orden; y en pasado: fuimos, comimos, volvimos."},
  {"p": 3, "t": "El domingo visitamos la Ciudad de las Artes y las Ciencias. Es muy grande y moderna."},
  {"p": 4, "t": "Lo mejor fue la comida.",
   "fix": "Lo mejor fue la comida y lo peor, el tráfico de la vuelta.", "k": "pautas",
   "por": "La pauta pide lo mejor y lo peor. Faltaba lo peor: estaba a medias."},
  {"p": 5, "t": "El otro fin de semana fui a Madrid con mis padres y me gustó mucho.",
   "fix": "El próximo fin de semana voy a quedarme en casa, porque tengo que estudiar.", "k": "pautas",
   "por": "La pauta pide planes (futuro) y la frase cuenta un viaje del pasado: contesta otra cosa."},
 ],
 "add": [],
 "diag": {"pautas": "La pauta 4 está a medias (falta lo peor) y la 5 contesta otra cosa: cuenta un viaje pasado y no los planes.",
          "con": "«...vamos a la playa y comemos paella y paseamos y volvemos...»: todo con «y».",
          "gram": "Cuenta el fin de semana pasado en presente: «estoy», «vamos», «comemos»."},
 "leccion": "Nils escribe frases correctas, pero dos pautas fallan: lo peor no está y los planes son del pasado. Dos frases cambiadas y el blog aprueba."},
# ============================================================ BIOGRAFÍA
{"id": "r4", "tipo": "Biografía", "autor": "Yusuf", "trato": None,
 "lamina": {"tarea": 2, "op": 2, "intro": "Carmen Soto es maestra jubilada. Aquí tiene algunas fotos y datos sobre su vida.",
   "photos": ["Una niña de unos seis años canta delante de su familia en una fiesta del pueblo.", "Una mujer joven escribe en la pizarra delante de una clase de niños.", "La misma mujer, hoy, con el pelo blanco, canta en un coro en una iglesia."],
   "img": "M3_13_bio_carmen_maestra",
   "rotulo": "Biografia Carmen maestra: 1 nina canta en fiesta del pueblo, 2 maestra joven en la pizarra, 3 mayor canta en un coro",
   "persona": "These three photos show the same Spanish woman from Galicia, Carmen, at three ages, and she must be clearly recognisable in all of them: a heart-shaped face, a dimple in her chin, light brown eyes, rosy cheeks, a wide mouth and wavy hair (dark brown when she is young, short and white in the last photo).",
   "escenas": ["1950s look, faded colours: Carmen at about 6, in a simple flowered dress, sings standing on a chair at an outdoor village festival in Galicia while her parents and grandparents sit at a long table around her and clap.",
               "Early 1970s look: Carmen at about 25, in a long skirt and a cardigan, writes simple sums with chalk on a blackboard in front of a class of young children sitting at old wooden desks.",
               "Today: Carmen at about 75, with short wavy white hair, sings in a choir of older men and women inside a stone church, holding a black music folder, her mouth open on a high note."],
   "ficha": ["Nació en Ourense en 1950.", "De niña: muy alegre; le encanta cantar.", "1968: empieza a estudiar Magisterio en Santiago.", "1972-2010: maestra en un colegio de Vigo.", "2011: se jubila y entra en un coro.", "Hoy: canta en el coro y viaja con sus amigas."],
   "intro2": "Escriba un texto sobre Carmen. Hable de:",
   "pautas": ["dónde y cuándo nació y cómo era de niña;", "qué estudió y en qué trabajó;", "qué cambió en 2011 y qué hace ahora."]},
 "seg": [
  {"p": 1, "t": "Carmen Soto nació en Ourense en 1950."},
  {"p": 1, "t": "De niña: muy alegre, cantar.",
   "fix": "De niña era muy alegre y le encantaba cantar.", "k": "tipo",
   "por": "Es la ficha copiada, sin verbos. Una biografía son frases: era, le encantaba."},
  {"p": 2, "t": "1968 estudiar Magisterio Santiago.",
   "fix": "En 1968 empezó a estudiar Magisterio en Santiago.", "k": "entiende",
   "por": "Sin verbo conjugado ni «en» no es una frase: ¿estudió?, ¿va a estudiar? En 1968 empezó a estudiar..."},
  {"p": 2, "t": "Después es maestra en un colegio de Vigo muchos años y le gusta mucho.",
   "fix": "Después fue maestra en un colegio de Vigo durante casi cuarenta años y le gustaba mucho su trabajo.", "k": "gram",
   "por": "Es el pasado: fue, le gustaba. Y «durante» para el tiempo que duró."},
  {"p": 3, "t": "En 2011 se jubila y entra en un coro.",
   "fix": "En 2011 se jubiló y entró en un coro, porque le encanta la música.", "k": "gram",
   "por": "Un hecho de 2011: indefinido (se jubiló, entró)."},
 ],
 "add": [
  {"p": 3, "ops": ["Hoy tiene setenta y seis años, canta en el coro todas las semanas y viaja mucho con sus amigas.",
                   "Hoy cantaba en el coro y viajaba con sus amigas.",
                   "La música es muy importante en la vida."],
   "por": "Faltaba la segunda pieza de la pauta 3: qué hace ahora. Para hoy, presente (canta, viaja). La tercera es una opinión general: no dice nada de Carmen."},
 ],
 "diag": {"pautas": "La pauta 3 está a medias: dice qué cambió en 2011, pero no qué hace ahora.",
          "tipo": "«De niña: muy alegre, cantar» es la ficha copiada, no una frase.",
          "entiende": "«1968 estudiar Magisterio Santiago»: sin verbo conjugado, no es una frase.",
          "gram": "Cuenta la vida de Carmen en presente: «es maestra», «se jubila», «entra».",
          "lin": "Unas 4 líneas: para la tarea 2 (7-8 líneas) es muy corto."},
 "leccion": "Yusuf tiene los datos, pero no los convierte en frases: copia la ficha, deja verbos sin conjugar y se olvida de «qué hace ahora». La pauta 1, la 2 y la 3 fallan. Cada dato, una frase en pasado, y aprueba."},
# ============================================================ TEXTO CON FOTOS
{"id": "r5", "tipo": "Texto con fotos", "autor": "Chiara", "trato": None,
 "lamina": {"tarea": 2, "op": 2, "intro": "El sábado pasado usted fue con unos amigos a un concierto al aire libre. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la tarde. Ustedes hacen cola en la entrada; empieza a llover.", "Por la noche. Todos bailan delante del escenario con chubasqueros de colores.", "Al final. Ustedes esperan un taxi en la calle; su móvil no tiene batería."],
   "img": "M3_14_dia_concierto_lluvia",
   "rotulo": "Concierto con lluvia: 1 cola y empieza a llover, 2 bailan con chubasqueros, 3 esperan un taxi sin bateria en el movil",
   "persona": "The same three people appear in all three photos and must look identical: an Italian woman of about 25 with long dark curly hair, a small nose ring and a denim jacket (the main person); her friend Tom, a tall Black man of about 25 with glasses; and her friend Eva, a woman of about 25 with short blond hair.",
   "escenas": ["Late afternoon at the entrance of an open-air concert: the three friends wait in a long queue of people; it is starting to rain, she holds out her hand to feel the drops and Tom looks up at the grey sky.",
               "Night in front of a lit concert stage in the rain: the three friends dance happily among the crowd, all wearing cheap colourful plastic rain ponchos, wet hair, arms in the air.",
               "Late at night on a wet city street with street lights: the three friends wait for a taxi at the kerb, tired and wet; she looks at her phone with a black screen and shrugs, Eva waves at a passing car."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": ["con quién fue y qué pasó al llegar;", "cómo fue el concierto;", "cómo volvieron a casa y cómo se sintió."]},
 "seg": [
  {"p": 1, "t": "En la foto 1 hay mis amigos y yo en una cola y llueve.",
   "fix": "El sábado pasado fui a un concierto con mis amigos Tom y Eva. Cuando llegamos, había mucha cola y empezó a llover.", "k": "tipo",
   "por": "Describe la foto en presente («en la foto 1 hay...»). La tarea pide contar la historia de ese día, en pasado. Y faltaba con quién."},
  {"p": 2, "t": "En la foto 2 todos bailan con chubasqueros de colores.",
   "fix": "Durante el concierto todos bailamos con chubasqueros de colores.", "k": "tipo",
   "por": "Otra vez la foto en presente. Cuenta lo que hicisteis: bailamos."},
  {"p": 2, "t": "El grupo tocar muy bien, mucho gente feliz.",
   "fix": "El grupo tocó muy bien y había mucha gente feliz.", "k": "entiende",
   "por": "Un verbo sin conjugar y una frase sin verbo: no se entiende quién hace qué. Tocó, había mucha gente."},
  {"p": 3, "t": "En la foto 3 esperamos un taxi y mi móvil no tiene batería.",
   "fix": "Al final esperamos un taxi más de media hora, porque mi móvil no tenía batería.", "k": "tipo",
   "por": "Ya no es «la foto 3»: es el final del día. En pasado: no tenía batería."},
 ],
 "add": [
  {"p": 3, "ops": ["Llegué a casa a las tres, cansada y mojada, pero muy contenta: fue una noche genial.",
                   "Estoy cansada y mojada, pero es una noche genial.",
                   "Me gustan mucho los conciertos al aire libre."],
   "por": "Faltaba cómo se sintió. Es ese día: en pasado (llegué, fue). En presente vuelves a describir la foto; la tercera es una opinión general."},
 ],
 "diag": {"pautas": "La pauta 1 está a medias (no dice con quién) y la 3 también: falta cómo se sintió.",
          "tipo": "Describe las tres fotos en presente («En la foto 1 hay...») en vez de contar el día.",
          "entiende": "«El grupo tocar muy bien, mucho gente feliz»: verbo sin conjugar y una frase sin verbo.",
          "lin": "Unas 4 líneas y media: para la tarea 2 (7-8 líneas) es muy corto."},
 "leccion": "Chiara mira las fotos y las describe, como en la oral. La escritura pide otra cosa: contar el día en pasado y responder a las pautas. Con eso y la frase que falta, aprueba."},
]

# ------------------------------------------------------------------ 5. EJERCICIOS CORTOS
BANDA_OPS = ["Banda 1: todavía no aprueba", "Banda 2: aprueba"]
BANDA = [  # ¿Banda 1 o banda 2? (se eligen 8 al azar). ok = índice en BANDA_OPS
 {"ctx": "Correo a una amiga (60-70 palabras): 65 palabras, las cinco pautas y algunos errores («mis amigo», «ayer he ido»). Todo se entiende.", "p": "", "ok": 1,
  "por": "Errores sí, pero se entiende todo y están todas las pautas: banda 2."},
 {"ctx": "Entrada de blog (70-80 palabras): 75 palabras y buen español, pero la pauta 4 falta y la 5 cuenta el pasado cuando pide planes.", "p": "", "ok": 0,
  "por": "Dos pautas fallan (una falta y otra contesta otra cosa): en el cumplimiento es banda 1, aunque el español sea bueno."},
 {"ctx": "Fragmento de un correo a un amigo. Todo el texto es así:", "p": "«Yo ayer cine con Marta, película no me gusta, mucho larga y aburrido.»", "ok": 0,
  "por": "Sin verbo en pasado (fui), «no me gusta» por «no me gustó», «mucho larga»: cuesta entender qué pasó. Un texto entero así es banda 1 en el uso de la lengua."},
 {"ctx": "Fragmento del mismo correo, escrito por otro estudiante. Todo el texto es así:", "p": "«Ayer fui al cine con Marta. La película no me gustó mucho porque era muy larga y aburrido.»", "ok": 1,
  "por": "Hay un error (aburrida), pero se entiende todo a la primera: banda 2."},
 {"ctx": "Correo a una amiga (60-70 palabras): 63 palabras. La pauta 3 pide «decir qué va a llevar a la fiesta» y escribe «Llevo algo.». El resto está bien.", "p": "", "ok": 1,
  "por": "Una sola pauta a medias: todavía banda 2, pero en el límite. ¡No te arriesgues! «Llevo una tortilla» es igual de fácil."},
 {"ctx": "Biografía. El texto es la ficha copiada:", "p": "«1990: estudia Derecho. 1995: trabaja en un banco. Hoy: vive en Sevilla.»", "ok": 0,
  "por": "Es una lista de datos, no un texto: no es el tipo de texto que piden y casi no hay frases. Banda 1."},
 {"ctx": "Biografía (70-80 palabras): 74 palabras y las tres pautas. Casi todo con «y»:", "p": "«Nació en Lima y estudió Medicina y trabajó en un hospital y ahora vive en Madrid y tiene dos hijos.»", "ok": 1,
  "por": "Tantas «y» bajan la nota, pero se entiende todo y están las pautas: banda 2, justo. Con «después» y «ahora» sería un 2 más seguro."},
 {"ctx": "Texto con fotos (70-80 palabras): unas 45 palabras. Describe las fotos en presente: «En la foto 1 hay...», «En la foto 2 comen...».", "p": "", "ok": 0,
  "por": "No es el tipo de texto (describe las fotos en vez de contar el día) y es muy corto: banda 1."},
 {"ctx": "Correo de usted (60-70 palabras): 68 palabras, las cinco pautas, todo de usted. Algún error: «quiero informaciones», «el curso empieza en lunes».", "p": "", "ok": 1,
  "por": "Errores pequeños que no impiden entender, todas las pautas y el trato bien: banda 2."},
 {"ctx": "Fragmento de un texto para una revista. Todo el texto es así:", "p": "«Mi ciudad favorito es Oporto porque hay río y comida rico y gente es simpático y yo vivir allí dos años.»", "ok": 0,
  "por": "Muchos errores juntos (favorito, rico, simpático, «yo vivir») y todo con «y»: se entiende con esfuerzo. Un texto entero así es banda 1."},
 {"ctx": "Correo a un amigo (60-70 palabras): 66 palabras. La pauta 4 («proponer un plan») falta y la 5 («despedirse») también.", "p": "", "ok": 0,
  "por": "Dos pautas fuera: banda 1 en el cumplimiento. ¡Y la despedida es la pauta más fácil de todas!"},
]

ENTIENDE = [  # ¿Se entiende? ops[0] es la buena (se barajan)
 {"ctx": "Pauta: «decir si puede ir a la fiesta y por qué»", "p": "«Sábado no ir, trabajo mi.»",
  "ops": ["El sábado no puedo ir, porque tengo que trabajar.", "El sábado no ir porque trabajo de mí.", "El sábado fui a trabajar."],
  "por": "Verbo conjugado (puedo) y la razón completa. La segunda sigue sin conjugar; la tercera cuenta el pasado y no responde."},
 {"ctx": "Pauta: «qué hizo en las vacaciones»", "p": "«En vacaciones yo visitar mis abuelos en pueblo muchas días.»",
  "ops": ["En las vacaciones visité a mis abuelos en el pueblo muchos días.", "En vacaciones yo visitar a mis abuelos muchos días.", "En vacaciones voy a visitar a mis abuelos."],
  "por": "Pasado (visité), «a mis abuelos», «muchos días». La tercera habla de planes: la pauta pide qué hizo."},
 {"ctx": "Pauta: «recomendar un restaurante y decir por qué»", "p": "«Restaurante Sol is very good, the fish.»",
  "ops": ["Te recomiendo el restaurante Sol, porque el pescado está muy bueno.", "Restaurante Sol es very good por el fish.", "Me gusta comer pescado en casa."],
  "por": "Sin palabras de otra lengua: si no sabes cómo se dice, usa palabras que conoces. La tercera no recomienda nada."},
 {"ctx": "Pauta: «cómo era su casa de niño»", "p": "«Mi casa niño tener jardín grande y perro.»",
  "ops": ["De niño vivía en una casa con un jardín grande y tenía un perro.", "Mi casa de niño tener un jardín grande y un perro.", "Ahora vivo en una casa con jardín."],
  "por": "Imperfecto para describir el pasado: vivía, tenía. La tercera habla de ahora."},
 {"ctx": "Pauta: «qué pasó a mediodía» (texto con fotos)", "p": "«Mediodía la lluvia, todos corriendo bar.»",
  "ops": ["A mediodía empezó a llover y todos corrimos a un bar.", "A mediodía la lluvia y todos corriendo al bar.", "Cuando llueve, me gusta ir a un bar."],
  "por": "Verbos conjugados en pasado: empezó, corrimos. La tercera es una costumbre, no lo que pasó ese día."},
 {"ctx": "Pauta: «preguntar por el precio» (correo de usted)", "p": "«Precio cuánto el curso por mes es?»",
  "ops": ["¿Cuánto cuesta el curso al mes?", "¿Precio cuánto es el curso por mes?", "El curso me parece caro."],
  "por": "Primero la palabra de pregunta, después el verbo: ¿Cuánto cuesta...? La tercera no pregunta nada."},
 {"ctx": "Pauta: «qué planes tiene para el verano»", "p": "«Verano yo ir México con familia mía, visitar playas.»",
  "ops": ["Este verano voy a ir a México con mi familia para visitar las playas.", "Verano yo voy México con familia mía.", "El verano pasado fui a México con mi familia."],
  "por": "Planes: ir a + infinitivo (voy a ir). La tercera está en pasado: contesta otra cosa."},
 {"ctx": "Pauta: «cómo se sintió»", "p": "«Yo muy nervioso en principio después bien.»",
  "ops": ["Al principio estaba muy nervioso, pero después me sentí bien.", "Yo muy nervioso en el principio y después bien.", "Los nervios son normales en un examen."],
  "por": "Con verbos (estaba, me sentí) y un conector (pero). La tercera es una opinión general: no dice cómo te sentiste."},
]

COMPLETA = [  # Completa la pauta: [[...]] = el hueco; ops[0] es la buena (se barajan)
 {"tipo": "Correo a un amigo", "pautas": "1 saludar · 2 agradecer el regalo · 3 decir qué le pareció · 4 contar cuándo lo va a usar · 5 despedirse",
  "falta": "Falta la pauta 4.",
  "texto": "¡Hola, Javi! Muchas gracias por el libro de cocina. Me ha encantado: tiene unas fotos preciosas y las recetas son fáciles. [[...]] Un abrazo, Nadia",
  "ops": ["El sábado voy a hacer la paella del libro para mis compañeros de piso.", "El sábado pasado hice una paella para mis compañeros.", "A mí me gusta mucho cocinar."],
  "por": "La pauta pide cuándo lo va a usar: futuro (voy a hacer). La segunda cuenta el pasado y la tercera no habla del libro."},
 {"tipo": "Correo de usted", "pautas": "1 saludar · 2 decir por qué escribe · 3 explicar el problema · 4 decir qué quiere que hagan · 5 agradecer y despedirse",
  "falta": "Falta la pauta 3.",
  "texto": "Estimado señor Ruiz: Le escribo porque ayer compré una cafetera en su tienda. [[...]] ¿Puede cambiármela por otra? Muchas gracias. Un saludo, Eva Lindqvist",
  "ops": ["Cuando llegué a casa, vi que no funcionaba: no se enciende.", "¿Puedes cambiármela? No funciona.", "Me gusta mucho el café por la mañana."],
  "por": "Explica el problema y sigue de usted. La segunda mezcla el tú; la tercera no es un problema."},
 {"tipo": "Blog", "pautas": "1 dónde fue y con quién · 2 cómo era el hotel · 3 qué hizo · 4 qué le gustó más y qué no le gustó · 5 si lo recomienda",
  "falta": "La pauta 4 está a medias.",
  "texto": "... Lo que más me gustó fue la playa: el agua estaba muy limpia. [[...]] ¡Os lo recomiendo!",
  "ops": ["Lo que no me gustó fue la comida del hotel: siempre era igual.", "La playa me gustó mucho, muchísimo.", "No me gusta la comida de los hoteles."],
  "por": "Faltaba la segunda pieza: qué no le gustó, en pasado. La segunda repite lo mismo y la tercera es una opinión general en presente."},
 {"tipo": "Biografía", "pautas": "1 dónde y cuándo nació · 2 qué estudió y en qué trabajó · 3 qué hace ahora",
  "falta": "Falta la pauta 3.",
  "texto": "Ana Ferrer nació en Alicante en 1980. Estudió Periodismo en Madrid y después trabajó en una radio durante diez años. [[...]]",
  "ops": ["Ahora vive en Barcelona y presenta un programa de televisión.", "Antes trabajaba en una radio.", "Ahora vivir en Barcelona, televisión."],
  "por": "«Qué hace ahora»: presente (vive, presenta). La segunda habla del pasado; la tercera no se entiende."},
 {"tipo": "Texto con fotos", "pautas": "1 qué hicieron por la mañana · 2 qué pasó a mediodía · 3 cómo terminó el día y cómo se sintieron",
  "falta": "La pauta 3 está a medias.",
  "texto": "El domingo fuimos al campo con los niños. Por la mañana hicimos una ruta por el bosque. A mediodía nos olvidamos la comida en el coche: ¡qué desastre! Por la tarde volvimos a casa muy pronto. [[...]]",
  "ops": ["Estábamos cansados, pero nos reímos mucho con lo de la comida.", "En la foto 3 están en el coche y están cansados.", "Por la tarde volvimos a casa."],
  "por": "Faltaba cómo se sintieron: estábamos cansados, nos reímos. La segunda describe la foto; la tercera repite lo que ya está."},
 {"tipo": "Correo a una amiga", "pautas": "1 saludar · 2 aceptar · 3 decir qué va a llevar · 4 proponer una hora y un lugar para quedar · 5 despedirse",
  "falta": "La pauta 4 está a medias.",
  "texto": "¡Hola, Lucía! ¡Claro que voy al picnic! Llevo una tortilla y fruta. Podemos quedar en la puerta del parque [[...]]. ¡Hasta el domingo! Un beso, Ana",
  "ops": ["a las once, ¿vale?", "porque es muy grande", "con mucha gente"],
  "por": "La pauta pide una hora y un lugar. Estaba el lugar; faltaba la hora."},
]

# ------------------------------------------------------------------ 6. AHORA TÚ
TEXTO_PROPIO_TIPOS = ["Correo a un amigo", "Correo de usted", "Blog, diario o revista", "Biografía", "Texto con fotos"]

# textos de las otras piezas que el estudiante puede traer (se leen del mismo navegador):
# kit de frases y pautas guardan el texto en w[id]; la revisión final, en hist (orig/rev); los textos modelo, en hist (a/b)
FUENTES_KIT = [  # id, nombre, tarea, trato, pautas
 ("inf", "Correo a un amigo (excursión en bici de Dani)", 1, "tu", ["saludar y agradecer la invitación", "decir que no puede ir y explicar por qué", "disculparse", "proponer otro plan para otro día", "despedirse"]),
 ("for", "Correo de usted (gimnasio Aquaforma)", 1, "usted", ["saludar", "presentarse y decir por qué escribe", "preguntar por los horarios de las clases y el precio", "preguntar por otra cosa (la piscina, qué hay que llevar...)", "agradecer y despedirse"]),
 ("blog", "Blog (una comida o una cena especial)", 2, None, ["cuándo fue, dónde y con quién", "qué celebraban o por qué era especial", "qué comieron y qué hicieron", "qué le gustó más y qué no le gustó", "si quiere repetir y por qué"]),
 ("bio", "Biografía (Tomás Ferrer, biólogo)", 2, None, ["dónde y cuándo nació y cómo era de niño", "qué estudió y a qué se dedicó", "qué hace ahora y qué ha cambiado en su vida"]),
 ("fotos", "Texto con fotos (curso de cocina)", 2, None, ["dónde estaba, con quién y qué hicieron por la mañana", "qué pasó a mediodía", "cómo terminó el día y qué le pareció el curso"]),
]
FUENTES_PAUTAS = [
 ("a1", "Correo a una amiga (Paula, día sin coches)", 1, "tu", ["saludar", "decir si quiere ir y qué actividad le interesa más", "responder a su pregunta sobre la bici", "proponer una hora y un lugar para quedar", "despedirse"]),
 ("a2", "Correo de usted (curso de fotografía)", 1, "usted", ["saludar", "presentarse y explicar por qué le interesa el curso", "preguntar por el precio y la duración del curso", "preguntar si necesita una cámara profesional", "agradecer y despedirse"]),
 ("a3", "Revista (mi lugar favorito)", 2, None, ["qué lugar es y dónde está", "cómo es", "cuándo va y con quién", "qué hace allí", "por qué es especial para usted"]),
 ("a4", "Texto con fotos (boda de una prima)", 2, None, ["qué problema tuvo por la mañana y qué hizo", "qué pasó cuando llegó a la boda", "cómo fue la fiesta y cómo se sintió"]),
]

# ------------------------------------------------------------------ 7. OPINIÓN
OPINION_FALLOS = ["Me faltan pautas", "Mis textos son cortos", "Frases que no se entienden", "Todo con «y»", "Los verbos", "Tú y usted"]
