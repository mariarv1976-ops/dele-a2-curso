# -*- coding: utf-8 -*-
# BANCO DE "TEXTOS MODELO: APROBADO Y EXCELENTE" (MODULO 3 · TALLER DE ESCRITURA · PIEZA 5) DEL CURSO DE PREPARACION DELE A2
# Lo usa build_M3_modelos.py. Para cambiar bandas, textos, mejoras o ejercicios, solo se toca este archivo.
#
# MARCAS en los textos modelo (dentro de cada frase):
#   {c:texto}  conector (se subraya)
#   {pr:..} presente · {in:..} indefinido · {im:..} imperfecto · {pe:..} perfecto · {fu:..} futuro (ir a + infinitivo)
#   {co:..} condicional (me gustaría, podría) · {ip:..} imperativo
#   Se marcan TODOS los verbos conjugados: el build cuenta los tiempos distintos de cada texto.
# Cada texto es una lista de párrafos; cada párrafo, una lista de frases:
#   aprobado:  (pauta, texto)                 pauta 0 = sin pauta (la firma)
#   excelente: (pauta, texto, [mejoras])      mejoras = claves de MEJORAS que usa esa frase
# El build comprueba: palabras dentro del límite de la tarea (los dos textos), una frase para cada pauta,
#   tú/usted coherente en los correos, que el excelente usa más conectores distintos y más tiempos distintos
#   que el aprobado, que cada excelente usa al menos 3 mejoras y que entre todos salen las 6.
# En los textos de «¿Aprueba?»: {T:..} palabra de tú, {U:..} palabra de usted (se marcan al corregir).
# FOTOS (12/10/2026): las laminas con fotos llevan "photos" (descripcion = texto alternativo), "img" (nombre fijo
# de las imagenes), "persona" y "escenas" (para los prompts). Ver fotos_M3.py.

# ------------------------------------------------------------------ 1. LAS BANDAS
QUE_MIRA = [  # (categoría, pregunta, peso, qué mira)
 ("Cumplimiento de la tarea", "¿Qué dices?", "un tercio de la nota",
  ["¿Hay una frase para cada pauta de la lámina?", "¿Es el tipo de texto que piden (correo, blog, biografía...)?", "¿El trato es el correcto (tú o usted) del saludo a la despedida?", "¿Tiene más o menos las palabras que piden?"]),
 ("Uso de la lengua", "¿Cómo lo dices?", "dos tercios de la nota",
  ["¿Se entiende todo sin esfuerzo?", "¿Los verbos están bien (sobre todo los pasados)?", "¿Las frases están unidas con conectores?", "¿Las palabras son las adecuadas?"]),
]

BANDAS = [  # (banda, nombre, cumplimiento, uso, puntos sobre 25)
 (3, "Excelente: más que A2",
  "Todas las pautas y, además, algo más: un detalle, una opinión, un porqué.",
  "Frases bien unidas con conectores variados (además, como, así que, aunque...), pasados bien combinados y palabras precisas. Puede tener algún error.",
  "25"),
 (2, "Aprobado: es un A2",
  "La información que pide la lámina, clara. (Si una pauta falla, ya estás en el límite.)",
  "Frases sencillas y unidas con conectores básicos (y, pero, porque, primero, después, por eso). Hay errores, pero se entiende todo.",
  "16,67"),
 (1, "Todavía no es A2",
  "Fallan dos pautas o más: faltan, están a medias o no se entienden.",
  "Frases sueltas, muy básicas, con errores que hacen difícil entender el mensaje.",
  "8,33"),
 (0, "No hay texto suficiente", "No responde a la tarea o solo hay palabras sueltas.", "No se entiende.", "0"),
]

UNA_FRASE = [  # aprobado / excelente en una frase
 ("Aprobado (banda 2)", "Dices <b>todo</b> lo que pide la lámina, con frases <b>sencillas</b> que se entienden."),
 ("Excelente (banda 3)", "Dices todo <b>y un poco más</b> (un detalle, un porqué, una opinión), con frases <b>bien unidas</b> y palabras <b>precisas</b>."),
]

DIFICIL = [  # «difícil no es excelente»
 "La banda 3 no pide subjuntivo, ni frases larguísimas, ni palabras raras del diccionario: pide <b>control</b>. Pasados bien combinados, conectores, palabras precisas.",
 "Una frase difícil con errores baja la nota. Una frase sencilla y correcta, no.",
 "El excelente <b>no es más largo</b>: tiene las mismas líneas que el aprobado. Lo que cambia es lo que hay dentro.",
]

# ¿Por qué un texto difícil puede no aprobar? (dos textos para la misma lámina, con sus dos notas)
DOS_NOTAS = {
 "lamina": "Una amiga te invita a su cumpleaños. Pautas: 1 saludar y agradecer · 2 decir si vas y por qué · 3 responder a su pregunta: ¿puedes llevar algo? · 4 proponer un plan para otro día · 5 despedirte.",
 "textos": [
  {"n": "Texto A · sencillo", "txt": "¡Hola, Marta! Gracias por la invitación. Sí, voy a ir, porque me encantan tus fiestas. Puedo llevar una tarta de chocolate. ¿Quieres ir al cine conmigo el domingo? Un beso, Ana",
   "cum": 2, "uso": 2, "nota": "Las cinco pautas, frases sencillas y correctas. <b>Aprobado seguro.</b>"},
  {"n": "Texto B · difícil", "txt": "¡Hola, Marta! ¡Qué ilusión que me hayas invitado! Por supuesto que iré, aunque llegaré tarde, ya que el sábado trabajo hasta las ocho. Ojalá tengamos tiempo para charlar con calma. Un fuerte abrazo, Ana",
   "cum": 1, "uso": 3, "nota": "Frases muy buenas... pero no dice si lleva algo (pauta 3) ni propone otro plan (pauta 4). Dos pautas fuera: <b>en el cumplimiento, todavía no es A2.</b>"},
 ],
 "regla": "Son <b>dos notas separadas</b>: las frases bonitas del uso de la lengua no arreglan una pauta que falta. Si falta una pauta, el cumplimiento ya no puede ser un 3 y te quedas en el límite. Si falta otra (o está a medias), baja a 1. Y escribir difícil tiene otro riesgo: más errores.",
 "moraleja": "Hacer todas las pautas depende de ti, no de tu nivel. Por eso es lo primero: con todas las pautas y frases sencillas, apruebas. Después, con dos o tres mejoras fáciles, subes a excelente.",
}

# ------------------------------------------------------------------ 2. LAS MEJORAS (de aprobado a excelente)
MEJORAS = [  # clave, nombre corto, qué haces, antes, después, a qué nota ayuda
 {"k": "con", "n": "Un conector más", "que": "Cambia un «y» o una frase suelta por un conector: después, además, por eso, así que, aunque.",
  "antes": "Perdí el autobús y llegué tarde.", "despues": "Perdí el autobús, <b>así que</b> llegué tarde.", "ayuda": "Uso de la lengua: el texto está mejor unido."},
 {"k": "pas", "n": "Un pasado bien combinado", "que": "Indefinido para lo que pasó y, al lado, imperfecto para describir cómo era o cómo estabas.",
  "antes": "Fui a la playa. Hizo sol.", "despues": "<b>Fui</b> a la playa: <b>hacía</b> un sol precioso.", "ayuda": "Uso de la lengua: es lo que la escala llama «combinación de pasados»."},
 {"k": "det", "n": "Un detalle o un porqué", "que": "Añade a una pauta una razón, una opinión o un detalle concreto: dónde, con quién, qué tal.",
  "antes": "Me gustó el museo.", "despues": "Me gustó el museo, <b>porque tiene cuadros de Sorolla</b>.", "ayuda": "Cumplimiento: la banda 3 pide «algún detalle, comentario, valoración o motivo»."},
 {"k": "pal", "n": "Una palabra más precisa", "que": "Cambia «bueno», «bonito», «cosa», «muy cansado» por la palabra exacta.",
  "antes": "La comida estaba buena. Estábamos muy cansados.", "despues": "La <b>paella</b> estaba <b>buenísima</b>. Estábamos <b>agotados</b>.", "ayuda": "Uso de la lengua: vocabulario más rico."},
 {"k": "preg", "n": "Una pregunta al lector", "que": "Habla con quien lee: en un blog, «¿Y vosotros...?»; en un correo, «¿Qué te parece...?».",
  "antes": "Os lo recomiendo.", "despues": "Os lo recomiendo. <b>¿Y vosotros? ¿Habéis estado en Toledo?</b>", "ayuda": "Cumplimiento: el texto parece un blog o un correo de verdad."},
 {"k": "cuan", "n": "Una frase con «cuando» o «porque» bien construida", "que": "Une dos frases cortas en una: cuando + pasado, como + causa, porque + razón.",
  "antes": "Llegamos al hotel. Llovía.", "despues": "<b>Cuando llegamos</b> al hotel, llovía.", "ayuda": "Uso de la lengua: frases enlazadas (la escala habla de subordinadas)."},
]

NO_ES = [  # lo que NO es subir de nivel
 "Escribir más: el excelente tiene las mismas líneas. Si añades una frase, quita otra.",
 "Usar estructuras que no controlas (subjuntivo, condicional compuesto...) «para impresionar».",
 "Palabras del diccionario que no conoces bien.",
 "Quitar una pauta para tener sitio para las frases bonitas.",
]

# ------------------------------------------------------------------ 3. LOS TEXTOS MODELO (5 tipos)
TIPOS = [
# ============================================================ CORREO A UN AMIGO
{"id": "inf", "tab": "Correo a un amigo", "trato": "tu", "donde": "Tarea 1 · 60-70 palabras",
 "lamina": {"tarea": 1, "instr": "Un amigo le escribe porque va a visitar su ciudad.",
   "input": ["¡Hola! ¿Qué tal? El mes que viene tengo unos días libres y quiero visitar tu ciudad. ¿Puedo quedarme en tu casa dos noches? Ah, y otra cosa: ¿conoces algún restaurante bueno? Me encanta probar la comida de cada sitio.", "Un abrazo, Hugo"],
   "lead": "Conteste a su amigo. En el correo tiene que:",
   "pautas": ["saludar;", "decir si puede quedarse en su casa y por qué;", "recomendarle un restaurante y explicar por qué le gusta;", "proponerle un plan para hacer juntos;", "despedirse."]},
 "ap": [
  [(1, "¡Hola, Hugo! ¿Qué tal? Gracias por tu correo.")],
  [(2, "¡Claro que {pr:puedes} quedarte en mi casa dos noches, {c:porque} {pr:tengo} una habitación libre!"),
   (3, "Te {pr:recomiendo} el restaurante Casa Pepa. {pr:Está} en el centro y me {pr:gusta} {c:porque} la comida {pr:es} muy buena y no {pr:es} cara.")],
  [(4, "¿{pr:Quieres} ir a la playa conmigo el sábado? {c:Después} {pr:podemos} comer allí.")],
  [(5, "Hasta pronto. Un abrazo,"), (0, "Ana")],
 ],
 "ex": [
  [(1, "¡Hola, Hugo! ¡Qué alegría tu correo!", [])],
  [(2, "¡Claro que {pr:puedes} quedarte en casa! Mi compañera de piso {pe:se ha ido} a Italia, {c:así que} {pr:tengo} una habitación libre.", ["det", "con"]),
   (3, "Te {pr:recomiendo} Casa Pepa, en el puerto. {c:Cuando} {in:fui} con mi familia, {in:probamos} un arroz buenísimo y, {c:además}, {im:era} muy barato.", ["cuan", "pas", "pal"])],
  [(4, "¿Qué te {pr:parece} si el sábado {pr:vamos} en bici a la playa? Seguro que te {fu:va a encantar}.", ["preg", "det"])],
  [(5, "Un abrazo,", []), (0, "Ana", [])],
 ],
 "por_ap": ["Las cinco pautas, una detrás de otra: saludo, sí y por qué, el restaurante con su porqué, un plan y la despedida.",
            "Todo es de tú: «tu correo», «puedes», «te recomiendo», «¿quieres...?», «un abrazo».",
            "Frases cortas, todas en presente y correctas. No hace falta más para aprobar."],
 "por_ex": ["Las mismas cinco pautas y casi las mismas líneas, pero cada una con algo más: por qué tiene la habitación libre, un recuerdo del restaurante, «seguro que te va a encantar».",
            "Cinco tiempos sin forzar nada: presente, perfecto (se ha ido), indefinido (fui, probamos), imperfecto (era) y futuro (va a encantar).",
            "Conectores que ordenan las ideas: así que, cuando, además. Y una palabra precisa: «buenísimo» en vez de «muy bueno».",
            "El plan es una pregunta a Hugo («¿Qué te parece si...?»): el correo habla con él."]},
# ============================================================ CORREO DE USTED
{"id": "for", "tab": "Correo de usted", "trato": "usted", "donde": "Tarea 1 · 60-70 palabras",
 "lamina": {"tarea": 1, "instr": "Usted ha visto este anuncio y quiere más información.",
   "anuncio": ["CLUB DE LECTURA · BIBLIOTECA MUNICIPAL", "Un libro al mes y una reunión para hablar de él. Gratis.", "Grupo especial en español para extranjeros.", "Información: Sra. Pastor (clublectura@biblioteca.es)"],
   "lead": "Escriba un correo a la señora Pastor. En el correo tiene que:",
   "pautas": ["saludar;", "presentarse y explicar por qué le interesa el club;", "decir qué tipo de libros le gustan;", "preguntar qué día y a qué hora son las reuniones;", "agradecer y despedirse."]},
 "ap": [
  [(1, "Estimada señora Pastor:")],
  [(2, "Me {pr:llamo} Kate Wilson y {pr:soy} inglesa. {pr:Vivo} en Sevilla desde hace un año. Le {pr:escribo} {c:porque} {pr:quiero} leer más en español."),
   (3, "Me {pr:gustan} mucho las novelas y los libros de viajes, {c:pero} no me {pr:gustan} los libros muy largos."),
   (4, "{pr:Trabajo} por las mañanas. ¿Qué día y a qué hora {pr:son} las reuniones?")],
  [(5, "Muchas gracias por su atención. Un saludo,"), (0, "Kate Wilson")],
 ],
 "ex": [
  [(1, "Estimada señora Pastor:", [])],
  [(2, "Me {pr:llamo} Kate Wilson, {pr:soy} inglesa y {pr:vivo} en Sevilla. Le {pr:escribo} {c:porque} {pe:he visto} su anuncio y {co:me gustaría} leer más en español.", ["det"]),
   (3, "{c:Cuando} {im:era} pequeña, {in:leí} todos los libros de Agatha Christie, {c:pero} ahora {pr:prefiero} los libros de viajes.", ["cuan", "pas", "det"]),
   (4, "{c:Como} {pr:trabajo} por las mañanas, ¿{co:podría} decirme qué día y a qué hora {pr:son} las reuniones?", ["con", "cuan"])],
  [(5, "Muchas gracias por su atención. Un saludo,", []), (0, "Kate Wilson", [])],
 ],
 "por_ap": ["Todo es de usted: «le escribo», «su atención», «un saludo». Ni un tú.",
            "Cada pauta tiene su frase. En la pauta 4 incluso da una razón (trabaja por las mañanas).",
            "Solo presente, frases cortas y claras: es un correo correcto y completo."],
 "por_ex": ["El mismo trato de usted, pero más educado todavía: «me gustaría», «¿podría decirme...?».",
            "Un pasado bien combinado en la pauta 3: «cuando era pequeña, leí...» (imperfecto + indefinido), y un contraste con «pero ahora».",
            "«Como trabajo por las mañanas» une la razón y la pregunta en una sola frase.",
            "Más detalles sin más líneas: por qué escribe (ha visto el anuncio), qué libros leía de niña."]},
# ============================================================ BLOG O DIARIO
{"id": "blog", "tab": "Blog o diario", "trato": None, "donde": "Tarea 2 · opción 1 · 70-80 palabras",
 "lamina": {"tarea": 2, "op": 1, "intro": "Escriba una entrada en su blog sobre su primera clase de un deporte o una actividad nueva. Hable de:",
   "pautas": ["qué actividad es y por qué empezó;", "cuándo y dónde fue la primera clase y con quién;", "qué hicieron en la clase;", "qué fue lo más difícil;", "si va a continuar y por qué."]},
 "ap": [
  [(1, "¡Hola a todos! Hoy os {pr:cuento} mi primera clase de pádel. {in:Empecé} {c:porque} mi amiga Lola {pr:juega} y me {in:invitó}."),
   (2, "La clase {in:fue} el martes por la tarde en el polideportivo de mi barrio. {in:Fui} con Lola.")],
  [(3, "{c:Primero} {in:corrimos} un poco. {c:Después} el profesor nos {in:explicó} las reglas y {in:jugamos} un partido."),
   (4, "Lo más difícil {in:fue} correr detrás de la pelota: ¡{pr:es} muy rápida!")],
  [(5, "Sí, {fu:voy a continuar} {c:porque} me {in:gustó} mucho.")],
 ],
 "ex": [
  [(1, "¡Hola a todos! Hoy os {pr:cuento} mi primera clase de pádel. {c:Antes} {im:hacía} poco deporte, {c:pero} mi amiga Lola me {pe:ha convencido}.", ["pas", "con"]),
   (2, "La clase {in:fue} el martes en el polideportivo del barrio, con Lola y cuatro chicas simpáticas.", ["det"])],
  [(3, "{c:Primero} {in:calentamos} y {c:luego} {in:aprendimos} a coger la pala.", ["pal"]),
   (4, "Lo más difícil {in:fue} el saque: {c:cuando} {in:lancé} la pelota, ¡{in:salió} de la pista!", ["cuan"])],
  [(5, "{fu:Voy a seguir}, {c:porque} lo {in:pasé} genial y, {c:además}, {pr:es} un deporte social. ¿Y vosotros? ¿{pr:Practicáis} algún deporte?", ["det", "con", "preg"])],
 ],
 "por_ap": ["Las cinco pautas en orden, como en la lámina: así es fácil ver que no falta ninguna.",
            "Habla a sus lectores de vosotros («os cuento»), como en un blog de verdad.",
            "Pasados correctos (empecé, fue, corrimos) y el futuro para la última pauta (voy a continuar).",
            "Conectores básicos para ordenar la clase: primero, después."]},
# placeholder: por_ex del blog se añade abajo para que la línea no sea tan larga
]
TIPOS[2]["por_ex"] = ["«Antes hacía poco deporte, pero...»: el imperfecto para cómo era su vida antes, el perfecto para lo reciente.",
                      "Siete conectores distintos en 7-8 líneas: antes, pero, primero, luego, cuando, porque, además.",
                      "La pauta 4 con una pequeña historia («cuando lancé la pelota, ¡salió de la pista!») en vez de una frase general.",
                      "Termina con preguntas a los lectores: «¿Y vosotros? ¿Practicáis algún deporte?»."]
TIPOS += [
# ============================================================ BIOGRAFIA
{"id": "bio", "tab": "Biografía", "trato": None, "donde": "Tarea 2 · opción 2 · 70-80 palabras",
 "lamina": {"tarea": 2, "op": 2, "intro": "Marta Ibáñez es guía de montaña. Aquí tiene algunas fotos y datos sobre su vida.",
   "photos": ["Una niña de unos ocho años, con gorro y guantes, hace un muñeco de nieve con su padre.", "Una mujer joven trabaja con un ordenador en una oficina llena de carteles de viajes.", "La misma mujer, hoy, con mochila y botas, habla con un grupo de turistas en lo alto de una montaña."],
   "img": "M3_09_bio_marta_guia_montana",
   "rotulo": "Biografia Marta guia de montana: 1 nina hace un muneco de nieve con su padre, 2 joven en oficina de viajes, 3 guia con turistas en la montana",
   "persona": "These three photos show the same Spanish woman, Marta, at three ages, and she must be clearly recognisable in all of them: copper-red hair in a single long braid, many freckles, green eyes, a strong square jaw and a wide mouth.",
   "escenas": ["1980s look, slightly faded colours: Marta at about 8, with a woolly hat, gloves and a red ski jacket, builds a snowman with her father in a snowy mountain village; she presses snow onto the snowman, laughing.",
               "Early 2000s look: Marta at about 28, with her red braid and a white blouse, works at a computer at her desk in a small travel agency office with colourful posters of mountains and beaches on the wall, with no text on them.",
               "Today: Marta at about 50, with a big backpack, hiking boots and her red braid with some grey, talks to a small group of tourists on the top of a mountain in the Pyrenees, pointing at the view."],
   "ficha": ["Nació en Jaca (Huesca) en 1975.", "De niña: muy aventurera; le encanta la nieve.", "1993: se va a Zaragoza y estudia Turismo.", "1998-2012: trabaja en una agencia de viajes en Madrid.", "2013: vuelve a los Pirineos; empieza a trabajar como guía de montaña.", "Hoy: lleva grupos de turistas a la montaña; vive en un pueblo con su familia.", "El año que viene: va a recorrer los Andes."],
   "intro2": "Escriba un texto sobre Marta. Hable de:",
   "pautas": ["dónde y cuándo nació y cómo era de niña;", "qué estudió y en qué trabajó;", "qué cambió en 2013 y qué hace ahora."]},
 "ap": [
  [(1, "Marta Ibáñez {in:nació} en Jaca en 1975. De niña {im:era} muy aventurera y le {im:encantaba} la nieve.")],
  [(2, "En 1993 {in:se fue} a Zaragoza y {in:estudió} Turismo. {c:Después} {in:trabajó} en una agencia de viajes en Madrid durante catorce años.")],
  [(3, "En 2013 {in:volvió} a los Pirineos y {in:empezó} a trabajar como guía de montaña. Ahora {pr:lleva} grupos de turistas a la montaña y {pr:vive} en un pueblo pequeño con su familia. Le {pr:gusta} mucho su trabajo.")],
 ],
 "ex": [
  [(1, "Marta Ibáñez {in:nació} en Jaca en 1975. De niña {im:era} muy aventurera: {c:cuando} {im:nevaba}, {im:pasaba} el día en la nieve con su padre.", ["det", "cuan", "pas"])],
  [(2, "En 1993 {in:se fue} a Zaragoza para estudiar Turismo y, {c:después}, {in:trabajó} catorce años en una agencia de viajes. {c:Aunque} le {im:gustaba} su trabajo, {im:quería} volver a la montaña.", ["con", "det"])],
  [(3, "{c:Por eso}, en 2013 {in:volvió} a los Pirineos. Hoy {pr:es} guía de montaña, {pr:lleva} grupos de turistas y el año que viene {fu:va a recorrer} los Andes.", ["con", "pal", "det"])],
 ],
 "por_ap": ["Cada dato de la ficha se convierte en una frase: 1993 → «En 1993 se fue a Zaragoza y estudió Turismo».",
            "Tres pautas, tres párrafos: de niña → estudios y trabajo → hoy.",
            "Indefinido para los hechos (nació, estudió, volvió), imperfecto para cómo era (era, le encantaba) y presente para hoy."],
 "por_ex": ["Las tres pautas y una historia que se entiende: la montaña de niña, el trabajo en la ciudad y la vuelta.",
            "Un detalle que explica: «cuando nevaba, pasaba el día en la nieve con su padre».",
            "Conectores que unen las etapas y dan razones: después, aunque, por eso. «Aunque le gustaba su trabajo, quería volver» explica el cambio de 2013.",
            "Usa también el último dato de la ficha (los Andes) con el futuro: cuatro tiempos en un texto corto."]},
# ============================================================ TEXTO CON FOTOS
{"id": "fotos", "tab": "Con fotos", "trato": None, "donde": "Tarea 2 · opción 2 · 70-80 palabras",
 "lamina": {"tarea": 2, "op": 2, "intro": "El invierno pasado usted pasó un día en la nieve con su familia. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la mañana. Ustedes alquilan esquís; hace sol. Su hija pequeña no quiere ponerse las botas.", "A mediodía. Usted se cae en la nieve; todos se ríen y su hija le hace una foto.", "Por la tarde. Toda la familia toma chocolate caliente al lado de una chimenea."],
   "img": "M3_10_dia_nieve_familia",
   "rotulo": "Dia en la nieve en familia: 1 alquilan esquis y la nina no quiere botas, 2 se cae en la nieve, 3 chocolate junto a la chimenea",
   "persona": "The same family appears in all three photos and must look identical: a Moroccan-Spanish mother of about 40 with a turquoise headscarf and a white ski jacket (the main person); her husband, about 42, with a short black beard and a black jacket; their son of about 10 in a green jacket; and their daughter Nora, about 5, in a pink snowsuit.",
   "escenas": ["Sunny morning inside a ski rental shop at the bottom of a ski slope, skis on racks: little Nora sits on a bench with her arms crossed, refusing to put on her ski boots, while her mother kneels in front of her holding a boot and the father and son wait.",
               "Midday on a gentle snowy ski slope: the mother has fallen and sits in the snow, laughing, with snow on her jacket and her skis crossed; the husband and son laugh, and Nora takes a photo of her with a phone.",
               "Late afternoon in a cosy wooden mountain café: the whole family sits on a sofa next to a stone fireplace with a fire, drinking hot chocolate from big mugs, relaxed, with rosy cheeks."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": ["qué hicieron por la mañana y qué tiempo hacía;", "qué pasó a mediodía;", "cómo terminó el día y cómo se sintieron."]},
 "ap": [
  [(1, "El invierno pasado {in:fui} a la nieve con mi familia. Por la mañana {in:alquilamos} los esquís. {im:Hacía} sol, {c:pero} {im:hacía} mucho frío. Mi hija no {im:quería} ponerse las botas {c:porque} {im:tenía} miedo.")],
  [(2, "A mediodía yo {in:me caí} en la nieve y todos {in:se rieron}. Mi hija me {in:hizo} una foto. ¡Qué vergüenza!")],
  [(3, "Por la tarde {in:tomamos} chocolate caliente al lado de una chimenea. {im:Estábamos} muy cansados, {c:pero} muy contentos. {in:Fue} un día muy bonito.")],
 ],
 "ex": [
  [(1, "El invierno pasado {in:pasé} un día en la nieve con mi marido y mis hijos. {c:Cuando} {in:llegamos}, {im:hacía} un sol precioso, {c:aunque} {im:hacía} muchísimo frío. {c:Primero} {in:alquilamos} los esquís, {c:pero} Nora, la pequeña, no {im:quería} ponerse las botas: ¡{im:tenía} miedo!", ["cuan", "pas", "pal"])],
  [(2, "A mediodía, {c:mientras} {im:bajaba} por la pista, {in:me caí} en la nieve. ¡Todos {in:se rieron} y Nora me {in:hizo} una foto!", ["pas", "con"])],
  [(3, "{c:Al final}, {in:tomamos} un chocolate junto a la chimenea. {im:Estábamos} agotados, {c:pero} felices. ¡{fu:Vamos a volver} en febrero!", ["con", "pal", "det"])],
 ],
 "por_ap": ["Cuenta la historia en pasado, no describe las fotos: «fui, alquilamos, me caí».",
            "Una foto, un párrafo, una pauta: mañana → mediodía → tarde.",
            "Indefinido para lo que pasó e imperfecto para el tiempo y cómo estaban: ya es un buen A2.",
            "Las frases son cortas y algunas palabras se repiten (muy, muy, muy), pero todo es correcto."]},
]
TIPOS[4]["por_ex"] = ["La misma historia, con conectores que la ordenan: cuando, aunque, primero, pero, mientras, al final.",
                      "«Mientras bajaba por la pista, me caí»: imperfecto para lo que estaba pasando e indefinido para lo que pasó de repente.",
                      "Palabras precisas en vez de «muy»: un sol precioso, muchísimo frío, agotados, felices.",
                      "Termina con un plan («¡Vamos a volver en febrero!»): un comentario final que cierra la historia."]

# ------------------------------------------------------------------ 4. EJERCICIOS
CLAS_OPS = ["Aprobado (banda 2)", "Excelente (banda 3)"]
CLAS = [  # ¿Aprobado o excelente? (se eligen 8 al azar). ok = índice en CLAS_OPS
 {"ctx": "Pauta: «contar qué hizo el sábado»", "p": "«El sábado fui a la playa con mis amigos. Comimos paella. Me gustó mucho.»", "ok": 0,
  "por": "Correcto y completo, pero son frases sueltas, sin conectores ni detalles. Es un buen aprobado."},
 {"ctx": "Pauta: «contar qué hizo el sábado»", "p": "«El sábado fui a la playa con mis amigos. Como hacía mucho calor, nos bañamos toda la tarde y, después, comimos una paella buenísima en el puerto.»", "ok": 1,
  "por": "«Como hacía calor» (causa + imperfecto), «después», un detalle (en el puerto) y una palabra precisa (buenísima)."},
 {"ctx": "Pauta: «decir si va a ir a la fiesta y por qué»", "p": "«Sí, voy a ir porque es tu cumpleaños.»", "ok": 0,
  "por": "Las dos piezas de la pauta (sí y por qué), correctas y sencillas: aprobado."},
 {"ctx": "Pauta: «decir si va a ir a la fiesta y por qué»", "p": "«¡Claro que voy! Es tu cumpleaños y, además, hace meses que no veo a Luis y a Sara.»", "ok": 1,
  "por": "Un porqué y otro más con «además»: es un detalle que no pedía la pauta."},
 {"ctx": "Pauta: «cómo era el hotel»", "p": "«El hotel era bonito. Estaba cerca de la playa.»", "ok": 0,
  "por": "Imperfecto correcto, pero «bonito» dice poco. Aprobado."},
 {"ctx": "Pauta: «cómo era el hotel»", "p": "«El hotel era pequeño y muy tranquilo, con un jardín lleno de flores, y estaba a cinco minutos de la playa.»", "ok": 1,
  "por": "Palabras precisas (tranquilo, un jardín lleno de flores) y un dato concreto (a cinco minutos)."},
 {"ctx": "Pauta: «qué le gustó más»", "p": "«Lo que más me gustó fue la cosa del museo.»", "ok": 0,
  "por": "Se entiende, pero «la cosa del museo» es poco precisa. «La visita al museo» o «los cuadros de Goya» lo suben."},
 {"ctx": "Pauta: «si lo recomienda» (blog)", "p": "«Sí, os lo recomiendo, sobre todo en primavera, cuando los campos están verdes. ¿Y vosotros? ¿Conocéis algún sitio así?»", "ok": 1,
  "por": "Un detalle (en primavera), una frase con «cuando» y preguntas a los lectores."},
 {"ctx": "Pauta: «qué hace ahora» (biografía)", "p": "«Ahora vive en Málaga. Trabaja en un hotel.»", "ok": 0,
  "por": "Responde a la pauta con dos frases correctas. Sin más: aprobado."},
 {"ctx": "Pauta: «qué planes tiene para el verano»", "p": "«Este verano voy a trabajar en un campamento de niños, porque quiero ahorrar para un viaje a México.»", "ok": 1,
  "por": "Futuro (voy a trabajar) y un porqué con un detalle (ahorrar para un viaje a México)."},
 {"ctx": "Pauta: «cómo se sintió ese día»", "p": "«Al principio estaba un poco nerviosa, pero cuando empezó la música, me olvidé de todo y bailé toda la noche.»", "ok": 1,
  "por": "Imperfecto (estaba) + indefinido (empezó, me olvidé, bailé), «al principio», «pero» y «cuando»."},
 {"ctx": "Pauta: «cómo se sintió ese día»", "p": "«Estaba muy contenta.»", "ok": 0,
  "por": "Responde, con el tiempo correcto. Es suficiente para aprobar, pero no añade nada."},
]

SUBE = [  # Sube un escalón: elige la versión mejorada (ops[0] es la buena; se barajan). Se eligen 8.
 {"ctx": "Frase aprobada: «Fui a la playa y comí y nadé.»", "p": "¿Qué versión sube a excelente?",
  "ops": ["Primero comí en un chiringuito y después nadé un rato.", "Fui a la playa, comí, nadé, tomé el sol, leí, dormí y volví.", "Habría ido a la playa si hubiera hecho sol."],
  "por": "Conectores (primero, después) y detalles. La segunda solo es una lista más larga; la tercera es de B1 y cambia lo que pasó."},
 {"ctx": "Frase aprobada: «La comida estaba buena.»", "p": "¿Qué versión sube a excelente?",
  "ops": ["La paella estaba buenísima.", "La comida estaba muy bueno.", "La comida estaba buena, la comida."],
  "por": "Palabras precisas: «la paella», «buenísima». La segunda tiene un error de concordancia (la comida... buena)."},
 {"ctx": "Frases aprobadas: «Llegué al hotel. Llovía.»", "p": "¿Qué versión sube a excelente?",
  "ops": ["Cuando llegué al hotel, llovía muchísimo.", "Cuando llegaba al hotel, llovió.", "Llegué al hotel. Llovía. Era tarde."],
  "por": "Una frase con «cuando» y los pasados en su sitio: llegué (lo que pasó), llovía (cómo era). La segunda los cambia de sitio."},
 {"ctx": "Frase aprobada: «Me gustó mucho el museo.»", "p": "¿Qué versión sube a excelente?",
  "ops": ["Me gustó mucho el museo, porque tiene cuadros de pintores muy famosos.", "Me gustó el museo muy.", "El museo, me gustó, me gustó mucho."],
  "por": "Un porqué con un detalle. «Me gustó muy» es un error: con el verbo, «mucho»."},
 {"ctx": "Frase aprobada (blog): «Os lo recomiendo.»", "p": "¿Qué versión sube a excelente?",
  "ops": ["Os lo recomiendo. ¿Y vosotros? ¿Habéis estado en Toledo?", "Le recomiendo a usted visitarlo.", "Os lo recomiendo, os lo recomiendo mucho."],
  "por": "Preguntas a los lectores, de vosotros. En un blog no se escribe de usted."},
 {"ctx": "Frase aprobada: «Perdí el autobús y llegué tarde.»", "p": "¿Qué versión sube a excelente?",
  "ops": ["Perdí el autobús, así que llegué tarde a clase.", "Perdí el autobús, aunque llegué tarde.", "Perdí el autobús porque llegué tarde."],
  "por": "«Así que» dice la consecuencia. «Aunque» no tiene sentido aquí y con «porque» la causa va al revés."},
 {"ctx": "Frase aprobada: «Tengo muchas cosas en la maleta.»", "p": "¿Qué versión sube a excelente?",
  "ops": ["En la maleta llevo ropa de abrigo, las botas y un libro.", "Tengo mucho cosas en la maleta.", "Tengo cosas, muchas cosas, en la maleta."],
  "por": "Palabras precisas en vez de «cosas». «Mucho cosas» es un error: muchas cosas."},
 {"ctx": "Frase aprobada (proponer un plan): «El sábado vamos al cine.»", "p": "¿Qué versión sube a excelente?",
  "ops": ["¿Qué te parece si el sábado vamos al cine? Ponen una película muy divertida.", "El sábado iríamos al cine si quisieras.", "El sábado fuimos al cine. Fue bueno."],
  "por": "Una pregunta a tu amigo y un porqué. La segunda es de B1; la tercera está en pasado: ya no es un plan."},
 {"ctx": "Frase aprobada: «Mi abuela era simpática.»", "p": "¿Qué versión sube a excelente?",
  "ops": ["Mi abuela era muy cariñosa: cuando iba a su casa, siempre me hacía galletas.", "Mi abuela fue simpática cuando fui siempre a su casa.", "Mi abuela era simpática y era simpática con todos."],
  "por": "Una palabra precisa (cariñosa) y un detalle con «cuando» + imperfecto para lo que pasaba siempre."},
]

HUECOS = {  # Una palabra mejor: cada hueco tiene [la que sube, la correcta pero sencilla, la que es un error]
 "titulo": "Una palabra mejor",
 "intro": "Leo escribe en su diario un texto que aprueba. Elige en cada hueco la palabra que lo sube a excelente. Ojo: una de las opciones es correcta, pero no sube; la otra es un error.",
 "texto": "Querido diario:\nEl domingo [[0]] con mis primos al campo. La comida estaba [[1]] y el paisaje era [[2]]. A mediodía empezó a hacer mucho viento, [[3]] comimos dentro del coche. [[4]] volvimos a casa, estábamos [[5]].\n¡Fue un día [[6]]!",
 "huecos": [
  {"ops": ["fui de excursión", "fui", "iba"], "por": "«Fui de excursión» dice más que «fui». «Iba» es imperfecto: aquí es una acción de ese día."},
  {"ops": ["buenísima", "buena", "bueno"], "por": "«Buenísima» es más preciso. «Bueno» no concuerda con «la comida»."},
  {"ops": ["precioso", "bonito", "bonita"], "por": "«Precioso» es más fuerte que «bonito». «Bonita» no concuerda con «el paisaje»."},
  {"ops": ["así que", "y", "aunque"], "por": "«Así que» dice la consecuencia. Con «aunque» la frase no tiene sentido."},
  {"ops": ["Cuando", "Después", "Porque"], "por": "«Cuando volvimos..., estábamos...» une las dos frases. «Después» es correcto, pero la frase queda más suelta. «Porque» no tiene sentido."},
  {"ops": ["agotados", "muy cansados", "cansado"], "por": "«Agotados» = muy, muy cansados. «Cansado» no concuerda con «nosotros»."},
  {"ops": ["estupendo", "bueno", "buena"], "por": "«Estupendo» es más preciso que «bueno». «Buena» no concuerda con «un día»."},
 ],
}

# ------------------------------------------------------------------ 5. ¿APRUEBA? (textos de estudiantes)
# veredicto: 0 = aprueba · 1 = le falta una pauta (y otra a medias) · 2 = mezcla tú y usted
VEREDICTOS = ["Aprueba: sencillo, pero completo", "En peligro: le falta una pauta", "En peligro: mezcla tú y usted"]
APRUEBA = [
# ---------------------------------------------------------------- 1. sencillo, aprueba
{"id": "s1", "tipo": "Correo a un amigo", "autor": "Bilal", "trato": "tu", "v": 0,
 "lamina": {"tarea": 1, "instr": "Un amigo le escribe para pedirle un favor.",
   "input": ["¡Hola! ¿Qué tal? El fin de semana que viene voy de camping a la sierra con mi novia. ¿Me puedes dejar tu tienda de campaña? Ah, tú conoces bien la sierra, ¿verdad? ¿Adónde podemos ir?", "Un abrazo, Rubén"],
   "lead": "Conteste a su amigo. En el correo tiene que:",
   "pautas": ["saludar;", "decir si le puede dejar la tienda y por qué;", "decir cuándo puede pasar a recogerla;", "recomendarle un lugar de la sierra y explicar por qué;", "despedirse."]},
 "est": ["si", "si", "si", "si", "si"],
 "par": [[(1, "¡Hola, Rubén! ¿Qué tal estás?")],
         [(2, "Sí, claro, {T:te} dejo mi tienda, porque este fin de semana no la necesito.")],
         [(3, "{T:Puedes} venir a mi casa el jueves por la tarde. Yo vuelvo del trabajo a las seis.")],
         [(4, "{T:Te} recomiendo el lago de Valdemar. Es muy bonito y hay pocas personas. También hay un río para bañarse.")],
         [(5, "¡Pasadlo muy bien! Un {T:abrazo},"), (0, "Bilal")]],
 "por": "Frases cortas y muy sencillas, pero las cinco pautas están, todo es de tú y no hay errores. Aprueba.",
 "leccion": "No hace falta escribir difícil: un texto sencillo y completo es un A2. Y para subirlo a excelente bastaría con dos mejoras, por ejemplo «Cuando fui en verano, me encantó...» en la pauta 4."},
# ---------------------------------------------------------------- 2. difícil, le falta la pauta 5 (y la 2 a medias)
{"id": "s2", "tipo": "Texto para una revista", "autor": "Sofía", "trato": None, "v": 1,
 "lamina": {"tarea": 2, "op": 1, "intro": "Una revista de cocina busca textos de sus lectores sobre «Mi plato favorito». Hable de:",
   "pautas": ["cuál es su plato favorito y de dónde es;", "quién lo cocina normalmente y cuándo lo come;", "cómo se prepara;", "un recuerdo especial con ese plato;", "si sabe cocinarlo o si quiere aprender y por qué."]},
 "est": ["si", "medias", "si", "si", "falta"],
 "par": [[(1, "Mi plato favorito son los pierogi, unas empanadillas típicas de Polonia, mi país, de queso, patata o carne."),
          (2, "Siempre los ha preparado mi abuela, que tiene unas manos mágicas para la cocina.")],
         [(3, "Primero se hace una masa con harina y agua; después se rellena y, por último, se cuecen en agua con sal.")],
         [(4, "Recuerdo especialmente la Nochebuena en que mi abuela me dejó cerrarlos por primera vez: tenía seis años y me sentía la persona más importante del mundo.")]],
 "por": "Un texto precioso, de nivel alto... pero no dice si sabe cocinarlos o si quiere aprender (pauta 5), y en la pauta 2 dice quién los cocina, pero no cuándo los come. Una pauta fuera y otra a medias: el cumplimiento baja a 1.",
 "leccion": "Sofía escribe mucho de las pautas 3 y 4 y se queda sin sitio para la última. Con una frase menos en la pauta 4, cabía «Todavía no sé hacerlos, pero este invierno quiero aprender con ella».",
 "corto": False},
# ---------------------------------------------------------------- 3. difícil, mezcla tú y usted
{"id": "s3", "tipo": "Correo de usted", "autor": "Jan", "trato": "usted", "v": 2,
 "lamina": {"tarea": 1, "instr": "Usted ha visto este anuncio y quiere pasar unos días en esta casa.",
   "anuncio": ["CASA RURAL EL ROBLE", "En plena naturaleza, a 10 km del pueblo. Cuatro habitaciones, jardín y barbacoa.", "Se admiten mascotas.", "Reservas: Sr. Delgado (reservas@elroble.es)"],
   "lead": "Escriba un correo al señor Delgado. En el correo tiene que:",
   "pautas": ["saludar;", "presentarse y decir por qué escribe;", "decir cuándo quiere ir y con quién;", "preguntar si puede llevar a su perro y qué actividades hay cerca;", "agradecer y despedirse."]},
 "est": ["si", "si", "si", "si", "si"],
 "par": [[(1, "Estimado señor Delgado:")],
         [(2, "Me llamo Jan Novak y {U:le escribo} porque un compañero de trabajo me ha recomendado {U:su} casa rural.")],
         [(3, "Nos gustaría pasar allí el puente de mayo, del jueves al domingo: seremos mi mujer, mis dos hijos y yo.")],
         [(4, "¿{T:Podrías} decirme si podemos llevar a nuestro perro? Además, ¿qué actividades {T:me recomiendas} para hacer con niños?")],
         [(5, "Muchas gracias de antemano por {T:tu} ayuda. Un {T:abrazo},"), (0, "Jan Novak")]],
 "por": "Muy buen español y todas las pautas... pero empieza de usted («le escribo», «su casa») y sigue de tú («¿podrías?», «me recomiendas», «tu ayuda», «un abrazo»). El señor Delgado no es su amigo: el registro no es el de la tarea.",
 "leccion": "El trato es parte de la tarea: un correo al dueño de una casa rural es de usted del principio al final. Cuatro palabras cambiadas (podría, me recomienda, su ayuda, un saludo) y era un texto excelente."},
# ---------------------------------------------------------------- 4. sencillo, aprueba
{"id": "s4", "tipo": "Biografía", "autor": "Amira", "trato": None, "v": 0,
 "lamina": {"tarea": 2, "op": 2, "intro": "Pedro Gil es cartero. Aquí tiene algunas fotos y datos sobre su vida.",
   "photos": ["Un niño de unos diez años monta en bici por un camino del campo.", "Un hombre joven, con uniforme amarillo, reparte cartas en bicicleta por un pueblo.", "El mismo hombre, hoy, con el pelo gris, enseña a unos niños a arreglar una bici en un taller."],
   "img": "M3_11_bio_pedro_cartero",
   "rotulo": "Biografia Pedro cartero: 1 nino en bici por el campo, 2 cartero joven de amarillo en bici, 3 mayor arregla bicis con ninos",
   "persona": "These three photos show the same Spanish man, Pedro, at three ages, and he must be clearly recognisable in all of them: stocky, with big ears, very thick dark eyebrows, a wide nose and a small gap between his front teeth; from his twenties on he has a thick moustache.",
   "escenas": ["1970s look, slightly faded colours: Pedro at about 10 rides an old red bicycle along a dirt path between wheat fields, smiling with his mouth open, his shirt blowing in the wind.",
               "1990s look: Pedro at about 25, with a moustache, a yellow postman's shirt and cap, gets off his bicycle in a village street with stone houses and hands a letter to an old woman at her door.",
               "Today: Pedro at about 57, with grey hair, a grey moustache and a work apron, shows three children how to fix a bicycle wheel in a small workshop with bikes and tools on the walls."],
   "ficha": ["Nació en un pueblo de Teruel en 1968.", "De niño: muy activo; le encanta la bici.", "1987: empieza a trabajar de cartero en su pueblo.", "1987-2020: reparte las cartas en bici.", "2021: se jubila y abre un taller de bicis.", "Hoy: arregla bicis y da clases a los niños del pueblo."],
   "intro2": "Escriba un texto sobre Pedro. Hable de:",
   "pautas": ["dónde y cuándo nació y cómo era de niño;", "en qué trabajó y cómo iba al trabajo;", "qué cambió en 2021 y qué hace ahora."]},
 "est": ["si", "si", "si"],
 "par": [[(1, "Pedro Gil nació en un pueblo de Teruel en 1968. De niño era muy activo y le encantaba montar en bici.")],
         [(2, "En 1987 empezó a trabajar de cartero en su pueblo. Durante muchos años repartió las cartas en bici. Le gustaba mucho su trabajo porque conocía a todo el mundo.")],
         [(3, "En 2021 se jubiló y abrió un taller de bicis. Ahora arregla bicis y da clases a los niños del pueblo. Es un hombre muy feliz.")]],
 "por": "Cada dato de la ficha es una frase, con los tiempos correctos (nació, era, empezó, arregla). Frases sencillas y todas las pautas: aprueba.",
 "leccion": "Fíjate: Amira incluso añade un porqué («porque conocía a todo el mundo»). Con un conector más y una frase con «cuando», sería excelente."},
# ---------------------------------------------------------------- 5. difícil, le falta la pauta 3 (y la 4 a medias)
{"id": "s5", "tipo": "Correo a una amiga", "autor": "Luca", "trato": "tu", "v": 1,
 "lamina": {"tarea": 1, "instr": "Una amiga le escribe porque ha encontrado trabajo.",
   "input": ["¡Hola! ¡Tengo trabajo nuevo! Empiezo el lunes en una empresa de diseño. Estoy muy contenta, pero también un poco nerviosa. ¿Y tú? ¿Qué tal en tu trabajo? ¿Quedamos para celebrarlo?", "Un beso, Clara"],
   "lead": "Conteste a su amiga. En el correo tiene que:",
   "pautas": ["saludar y felicitarla;", "darle un consejo para su primer día;", "contarle qué tal le va en su trabajo;", "responder a su propuesta y proponer un plan;", "despedirse."]},
 "est": ["si", "si", "falta", "medias", "si"],
 "par": [[(1, "¡Hola, Clara! ¡Enhorabuena! Me alegro muchísimo de que por fin hayas encontrado un trabajo que te guste tanto.")],
         [(2, "Mi consejo: el primer día sonríe mucho, haz preguntas y no tengas miedo de equivocarte, porque al principio todo el mundo se equivoca.")],
         [(4, "¡Pues claro que lo celebramos! Llevo semanas con ganas de verte.")],
         [(5, "Un beso enorme,"), (0, "Luca")]],
 "por": "Frases de nivel alto (subjuntivo, «llevo semanas con ganas»)... pero no cuenta qué tal le va en su trabajo (pauta 3), y en la pauta 4 dice que sí, pero no propone ningún plan. Y el correo es corto.",
 "leccion": "Clara hace dos preguntas en su correo («¿Qué tal en tu trabajo?», «¿Quedamos?») y las dos son pautas. Una frase sencilla para cada una («Yo estoy bien, aunque tengo mucho trabajo» · «¿El viernes a las ocho?») valía más que el subjuntivo."},
# ---------------------------------------------------------------- 6. difícil, mezcla tú y usted
{"id": "s6", "tipo": "Correo a un amigo", "autor": "Mei", "trato": "tu", "v": 2,
 "lamina": {"tarea": 1, "instr": "Un amigo le escribe desde otra ciudad.",
   "input": ["¡Hola! ¿Qué tal? El mes que viene es mi cumpleaños y hago una fiesta en mi casa nueva de Valencia. ¿Puedes venir? Si quieres, puedes dormir aquí. ¿Vienes en tren o en coche?", "Un abrazo, Diego"],
   "lead": "Conteste a su amigo. En el correo tiene que:",
   "pautas": ["saludar y agradecer la invitación;", "decir si puede ir y por qué;", "responder a su pregunta sobre el viaje;", "preguntarle qué quiere de regalo;", "despedirse."]},
 "est": ["si", "si", "si", "si", "si"],
 "par": [[(1, "¡Hola, Diego! Muchas gracias por {U:su} amable invitación.")],
         [(2, "Por supuesto que iré: hace meses que no nos vemos y tengo muchísimas ganas de conocer {T:tu} casa nueva y {T:tu} ciudad.")],
         [(3, "Pienso ir en tren el viernes por la tarde, porque es más cómodo y puedo leer durante el viaje.")],
         [(4, "Por cierto, ¿{U:podría} decirme qué {U:le gustaría} de regalo? No tengo ni idea.")],
         [(5, "{U:Atentamente},"), (0, "Mei")]],
 "por": "Contesta a todo con frases muy buenas, pero Diego es su amigo y Mei mezcla: «tu casa», «tu ciudad» (tú) con «su amable invitación», «¿podría...?», «le gustaría», «Atentamente» (usted).",
 "leccion": "Con un amigo, todo de tú: «gracias por tu invitación», «¿puedes decirme qué te gustaría?», «Un abrazo». Mira el saludo de tu mini lista (TÚ) antes de escribir cada pregunta."},
]

# ------------------------------------------------------------------ 6. AHORA TÚ: láminas nuevas para escribir
AHORA_NUEVAS = [
 {"id": "n1", "n": "Correo a una amiga", "trato": "tu",
  "lamina": {"tarea": 1, "instr": "Una amiga le escribe porque quiere aprender su idioma.",
   "input": ["¡Hola! ¿Cómo estás? Tengo una noticia: he empezado a estudiar tu idioma. ¡Es difícil! Tú aprendiste español muy rápido. ¿Qué hiciste? ¿Me das algún consejo?", "Un beso, Irene"],
   "lead": "Conteste a su amiga. En el correo tiene que:",
   "pautas": ["saludar;", "contar cómo aprendió usted español y qué le ayudó más;", "darle dos consejos;", "proponerle quedar para practicar;", "despedirse."]}},
 {"id": "n2", "n": "Correo de usted", "trato": "usted",
  "lamina": {"tarea": 1, "instr": "Usted ha visto este anuncio en su barrio.",
   "anuncio": ["FIESTA DEL BARRIO · SE BUSCAN VOLUNTARIOS", "Para preparar la comida, la música y los juegos para niños.", "Sábado 14, de 10:00 a 20:00.", "Información: Sra. Llorca (fiesta@barriosur.es)"],
   "lead": "Escriba un correo a la señora Llorca. En el correo tiene que:",
   "pautas": ["saludar;", "presentarse y decir por qué quiere ayudar;", "explicar qué sabe hacer;", "preguntar a qué hora tiene que ir y qué tiene que llevar;", "agradecer y despedirse."]}},
 {"id": "n3", "n": "Entrada de blog", "trato": None,
  "lamina": {"tarea": 2, "op": 1, "intro": "Escriba una entrada en su blog sobre un lugar que visitó y que le sorprendió. Hable de:",
   "pautas": ["qué lugar fue, cuándo y con quién;", "cómo era;", "qué hizo allí;", "qué le sorprendió más;", "si quiere volver y por qué."]}},
 {"id": "n4", "n": "Texto con fotos", "trato": None,
  "lamina": {"tarea": 2, "op": 2, "intro": "El mes pasado usted organizó una cena en su casa para unos amigos. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la mañana. Usted compra pescado y verduras en un mercado lleno de gente.", "Por la tarde. Hay humo en la cocina: el arroz se ha quemado y suena el timbre.", "Por la noche. Todos cenan pizza en la terraza y se ríen."],
   "img": "M3_12_dia_cena_amigos",
   "rotulo": "Cena en casa con amigos: 1 compra en el mercado, 2 humo en la cocina y suena el timbre, 3 cenan pizza en la terraza",
   "persona": "The same main person appears in all three photos and must look identical: a Polish woman of about 60 with short grey hair, blue eyes, small round glasses, long colourful earrings and a mustard-yellow cardigan.",
   "escenas": ["Morning in a busy covered food market: she buys fresh fish at a fish stall, pointing at a fish on the ice, with a cloth shopping bag full of vegetables on her arm; other shoppers around her.",
               "Afternoon in her small kitchen: grey smoke rises from a big paella pan with burnt rice on the stove; she holds a wooden spoon and turns her head towards the hallway and the front door, worried, because someone is at the door.",
               "Night on a small terrace with plants and string lights: she and five friends of different ages and origins sit around a table eating pizza from open boxes and laughing."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": ["qué compró por la mañana y qué quería preparar;", "qué problema tuvo por la tarde;", "cómo terminó la noche y cómo se sintió."]}},
]

TEXTO_PROPIO_TIPOS = ["Correo a un amigo", "Correo de usted", "Blog, diario o revista", "Biografía", "Texto con fotos"]

# lista corta: ¿mi texto es «aprobado»? (las pautas se añaden una a una si se conoce la lámina)
CHECK_APROBADO = [
 ("pautas", "Cada pauta tiene su frase (con todas sus piezas)."),
 ("trato", "El trato es el mismo del saludo a la despedida."),
 ("lineas", "Las líneas, a ojo: tarea 1, unas 6-7; tarea 2, unas 7-8."),
 ("gram", "He revisado los pasados, las concordancias y muy / mucho."),
]
