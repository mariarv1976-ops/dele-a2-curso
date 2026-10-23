# -*- coding: utf-8 -*-
# BANCO DE "LA REVISION FINAL DE 5 MINUTOS" (MODULO 3 · TALLER DE ESCRITURA · PIEZA 4) DEL CURSO DE PREPARACION DELE A2
# Lo usa build_M3_revision.py. Para cambiar la lista, los textos o los ejercicios, solo se toca este archivo.
#
# LA LISTA: 8 pasadas en un orden fijo. Cada pasada tiene una clave (k) que usan los ejercicios:
#   pautas · trato · pas · hay · conc · muy · con · lin
# CAZA POR PASADAS: un ejercicio por pasada. tipo "c" = caza los errores (frases; las que tienen "fix" son
#   las que hay que marcar; "por" = explicacion corta); tipo "q" = elegir una opcion.
# CONTRARRELOJ: textos completos con la lamina. "par" = parrafos; cada frase {"p": pauta, "t": texto,
#   "fix": correccion, "k": pasada, "por": explicacion}. "falta" = pautas sin ninguna frase. "largo" = como
#   queda el texto corregido: "bien" (dentro de las palabras) o "corto".
# El build comprueba: frases con error en su pasada, correcciones distintas del original, tu/usted coherente
#   en los correos corregidos, palabras del texto corregido, que una pauta que falta no tiene frase y las
#   demas si, y que cada pasada de gramatica sale en el contrarreloj.
# FOTOS (12/10/2026): las laminas con fotos llevan "photos" (descripcion = texto alternativo), "img" (nombre fijo
# de las imagenes), "persona" y "escenas" (para los prompts). Ver fotos_M3.py.

# ------------------------------------------------------------------ LOS 5 MINUTOS
REPARTO = [(5, "Leer y elegir", "Lee las dos tareas, elige la opción de la tarea 2 y haz tus mini listas."),
           (15, "Tarea 1", "El correo: 60-70 palabras."),
           (20, "Tarea 2", "El texto de la opción elegida: 70-80 palabras."),
           (5, "Revisar", "La lista de revisión, en orden: 2 minutos para la tarea 1 y 3 para la tarea 2.")]

POR_QUE = [  # por qué una lista fija y no "leer otra vez"
 ("Leer el texto otra vez no sirve", "Cuando lees tu texto, tus ojos leen lo que querías escribir, no lo que has escrito. Por eso los errores se escapan."),
 ("Una pasada, una cosa", "Si buscas solo una cosa (solo los verbos, solo el saludo y la despedida), la ves. Es más rápido y se escapan menos fallos."),
 ("Siempre el mismo orden", "Primero lo que más cuenta (las pautas). Si se acaba el tiempo, lo importante ya está hecho. Y con el mismo orden siempre, el día del examen no tienes que pensar."),
]

# ------------------------------------------------------------------ LA LISTA (8 pasadas)
PASADAS = [
 {"k": "pautas", "n": "Las pautas", "s": 60,
  "mira": "La lámina y tu mini lista, pauta por pauta. No leas el texto entero: busca la frase de cada pieza.",
  "busca": "Una frase para cada pieza: el «y por qué», el «con quién», la despedida... Y que la frase responda de verdad (si pide planes, futuro).",
  "ej": [("Pauta «decir si va a ir y por qué»: <i>Sí, voy a ir.</i>", "<i>Sí, voy a ir <b>porque es tu cumpleaños</b>.</i>"),
         ("Pauta «despedirse»: el correo termina con una pregunta.", "<i>¿Quedamos el jueves? <b>Un abrazo,</b></i>")],
  "truco": "Va la primera porque es la que más cuenta: una pauta que falta baja la nota más que tres errores pequeños. Y si tienes que añadir una frase, mejor ahora, cuando todavía tienes tiempo."},
 {"k": "trato", "n": "Tú o usted", "s": 20,
  "mira": "Solo el saludo, la despedida y las palabras de tú o de usted: los verbos de las preguntas, te / le, tu / su.",
  "busca": "El mismo trato del principio al final: TÚ o USTED, lo que escribiste arriba en tu mini lista. En un blog, vosotros («os cuento»).",
  "ej": [("Estimada señora Gómez: ... <i>¿Puedes decirme...?</i>", "<i>¿<b>Puede</b> decirme...?</i>"),
         ("Correo a un amigo: <i>Atentamente,</i>", "<i><b>Un abrazo,</b></i>")],
  "truco": "Lee la primera línea y salta a la última: si el saludo y la despedida no son del mismo trato, ya tienes un error. Después, solo las preguntas."},
 {"k": "pas", "n": "Los pasados", "s": 50,
  "mira": "Solo los verbos en pasado. Pasa el dedo de verbo en verbo y mira la palabra que dice cuándo.",
  "busca": "Indefinido para lo que pasó (ayer, el sábado, en 2019): <i>fui, comimos</i>. Imperfecto para describir (cómo era, qué había): <i>era, había, tenía</i>. Perfecto con hoy, esta semana, este año: <i>he ido</i>. Y las formas difíciles: <i>hicimos, fui, estuve, tuve</i>.",
  "ej": [("<i>Ayer he ido al cine.</i>", "<i>Ayer <b>fui</b> al cine.</i>"),
         ("<i>El hotel estuvo en el centro.</i>", "<i>El hotel <b>estaba</b> en el centro.</i>"),
         ("<i>Hacimos muchas fotos.</i>", "<i><b>Hicimos</b> muchas fotos.</i>")],
  "truco": "Mira la pauta: si dice «qué hizo», indefinido; si dice «cómo era», imperfecto. La lámina ya te da el tiempo."},
 {"k": "hay", "n": "Hay / está / es", "s": 25,
  "mira": "Solo las palabras <b>hay</b>, <b>está / están</b> y <b>es / son</b> (y en pasado: había, estaba, era).",
  "busca": "<b>hay</b> + un, una, números o nada: algo existe (<i>hay un parque</i>). <b>el / la / mi... + está</b>: dónde está algo que ya conocemos (<i>el parque está al lado</i>). <b>es</b>: qué es o cómo es (<i>es profesora, es pequeño</i>).",
  "ej": [("<i>En mi calle está un mercado.</i>", "<i>En mi calle <b>hay</b> un mercado.</i>"),
         ("<i>El hotel hay en el centro.</i>", "<i>El hotel <b>está</b> en el centro.</i>"),
         ("<i>Mi vecina está profesora.</i>", "<i>Mi vecina <b>es</b> profesora.</i>")],
  "truco": "Pregúntate: ¿digo que algo existe (hay), dónde está algo conocido (está) o qué es (es)?"},
 {"k": "conc", "n": "Concordancias y posesivos", "s": 40,
  "mira": "Cada nombre con lo que lleva delante y detrás: el artículo, el adjetivo y el posesivo.",
  "busca": "Masculino o femenino, singular o plural, todo igual: <i>la comida estaba buena, unas vacaciones bonitas</i>. Los posesivos también: <i>mi amigo / mis amigos, su casa / sus casas</i>.",
  "ej": [("<i>con mis amigo</i>", "<i>con mis amigo<b>s</b></i> o <i>con mi amigo</i>"),
         ("<i>La comida estaba muy bueno.</i>", "<i>La comida estaba muy buen<b>a</b>.</i>"),
         ("<i>un clínica</i>", "<i>un<b>a</b> clínica</i>")],
  "truco": "Busca las <b>-s</b>: si el nombre lleva -s, mira que el posesivo y el adjetivo también la lleven. Y al revés."},
 {"k": "muy", "n": "Muy / mucho", "s": 20,
  "mira": "Solo las palabras <b>muy</b> y <b>mucho</b> (mucha, muchos, muchas).",
  "busca": "<b>muy</b> + adjetivo o adverbio: <i>muy bonito, muy bien</i>. <b>mucho</b> detrás del verbo: <i>me gustó mucho</i>. <b>mucho, mucha, muchos, muchas</b> + nombre: <i>mucha gente, muchas cosas</i>.",
  "ej": [("<i>Me gustó muy.</i>", "<i>Me gustó <b>mucho</b>.</i>"),
         ("<i>un restaurante mucho bueno</i>", "<i>un restaurante <b>muy</b> bueno</i>"),
         ("<i>Había mucho gente.</i>", "<i>Había <b>mucha</b> gente.</i>")],
  "truco": "Mira la palabra de después: ¿un adjetivo? muy. ¿Un nombre? mucho, mucha, muchos, muchas. ¿Nada? mucho."},
 {"k": "con", "n": "Conectores", "s": 30,
  "mira": "El principio de cada frase y las palabras <b>y</b> y <b>porque</b>.",
  "busca": "Que no todo sea «y... y...» o «porque... porque...». En la tarea 2, tres o cuatro conectores distintos: <i>primero, después, además, por eso, así que, pero, al final</i>. Y que tengan sentido.",
  "ej": [("<i>Cenamos y bailamos y cantamos y volvimos tarde.</i>", "<i><b>Primero</b> cenamos, <b>después</b> bailamos y cantamos y, <b>al final</b>, volvimos tarde.</i>"),
         ("<i>No fuimos al campo porque llovía y comimos en un bar.</i>", "<i><b>Como</b> llovía, no fuimos al campo, <b>así que</b> comimos en un bar.</i>")],
  "truco": "Si ves tres «y» en la misma frase, cambia una por <i>después</i> o <i>además</i>. Es un cambio pequeño y se nota mucho."},
 {"k": "lin", "n": "Las líneas", "s": 15,
  "mira": "Las líneas, no las palabras. Cuéntalas con el dedo, sin contar palabra por palabra.",
  "busca": "Tarea 1: 6-7 líneas (60-70 palabras). Tarea 2: 7-8 líneas (70-80). Unas 10 palabras por línea escrita a mano.",
  "ej": [("Tarea 1 con 4 líneas y media", "Añade una frase a la pauta más corta: un porqué, un detalle."),
         ("Tarea 1 con 11 líneas", "Tacha con una raya una frase que no pide ninguna pauta.")],
  "truco": "Va la última porque es la más rápida. Y si faltaba una pauta, ya la has añadido en la primera pasada: por eso las líneas se cuentan al final."},
]

# la tarjeta para imprimir (una línea por pasada, en el mismo orden que PASADAS)
TARJETA = ["Mini lista en la mano: cada pieza, su frase (y el tiempo que pide la pauta).",
           "Saludo y despedida: el mismo trato. Preguntas, te / le, tu / su.",
           "Solo los verbos: ¿lo que pasó (fui) o cómo era (era, había)? ¿Hoy (he ido)?",
           "Solo hay / está / es: ¿existe, dónde está o qué es?",
           "Cada nombre con su artículo, su adjetivo y su posesivo: mis amigos.",
           "Solo muy / mucho: muy bonito · me gustó mucho · mucha gente.",
           "¿Solo «y» y «porque»? Primero, después, además, por eso, al final.",
           "Cuenta las líneas: tarea 1, 6-7; tarea 2, 7-8."]

# ------------------------------------------------------------------ COMO CORREGIR
REGLAS = [  # tres reglas grandes
 ("Tacha limpio", "Una sola raya encima de lo que está mal. Que se lea: el corrector tiene que ver qué cambias. Nada de tachones ni de borrar."),
 ("Escribe encima", "La corrección, encima de la palabra tachada, pequeña y clara. Para añadir una palabra, una marca ‸ en la línea y la palabra encima."),
 ("No reescribas todo", "No hay tiempo y, al copiar, escribes errores nuevos. Corrige solo las palabras que están mal."),
]

SITUACIONES = [  # encuentras | haces
 ("Una palabra está mal", "Táchala con una raya y escribe la buena encima."),
 ("Falta una palabra (un artículo, un «porque»)", "Una marca ‸ donde va y la palabra encima."),
 ("Falta una frase (una pieza de una pauta)", "Escríbela al final del párrafo si hay sitio. Si no, al final del texto con un asterisco (*) y otro asterisco donde va."),
 ("Sobra una frase (el texto es muy largo y no la pide ninguna pauta)", "Táchala con una raya."),
 ("No estás seguro", "Déjalo como está. Cambia solo lo que sabes que está mal."),
]

NO_HACER = [
 "Cambiar una frase correcta por otra más difícil en el último minuto.",
 "Pasar el texto a limpio: no da tiempo y salen errores nuevos.",
 "Tachar tanto que no se lee lo que has escrito.",
 "Leer el texto de principio a fin «a ver si veo algo»: usa la lista.",
]

# la carta corregida a mano: <s> tachado, <rt> lo que se escribe encima, ‸ marca, * asterisco
DEMO = [
 "Estimada señora Ruiz:",
 "Me llamo Paul y le escribo porque ayer <ruby><s>he visto</s><rt>vi</rt></ruby> su anuncio.",
 "<ruby><s>¿Puedes</s><rt>¿Puede</rt></ruby> decirme el precio del curso?",
 "Trabajo por las mañanas, <ruby><span class=\"car\">‸</span><rt>así que</rt></ruby> prefiero un curso de tarde.",
 "Tengo <ruby><s>mucho</s><rt>muchas</rt></ruby> ganas de aprender. <span class=\"ast\">*</span>",
 "Muchas gracias por su atención.",
 "<ruby><s>Un beso</s><rt>Un saludo</rt></ruby>,",
 "Paul Weber",
 "<span class=\"ast\">*</span> ¿Hay que llevar algo a las clases?",
]
DEMO_NOTAS = ["Un pasado mal: tachado y la forma buena encima.",
              "Un tú en un correo de usted: tachado y corregido.",
              "Faltaba una palabra: marca ‸ y la palabra encima.",
              "«ganas» es femenino plural: muchas.",
              "Faltaba la pregunta de la pauta 4: al final, con un asterisco en los dos sitios.",
              "Despedida de tú: tachada y corregida."]

# ------------------------------------------------------------------ CAZA POR PASADAS (un ejercicio por pasada)
LIN_OPS = ["Corto: añado una frase.", "Bien: lo dejo así.", "Largo: tacho una frase que sobra."]
EJ = {
 "pautas": {"tipo": "q", "fixed": False, "titulo": "Si falta algo de una pauta, ¿qué haces?",
  "tarea": "Las dos tareas · con tu mini lista",
  "intro": "Estás en la primera pasada, con la lámina y tu mini lista. Elige qué haces en cada caso.",
  "items": [
   {"ctx": "Revisas y ves que falta la despedida. Quedan 3 minutos.", "p": "¿Qué haces?", "ops": ["La escribo ahora al final: «Un abrazo, Ana».", "Nada: es solo una palabra.", "Escribo otra vez todo el correo."], "ok": 0, "por": "La despedida es una pauta: sin ella, la tarea está incompleta. Se arregla en cinco segundos."},
   {"ctx": "Pauta «decir si va a ir y por qué». En tu texto: «Sí, voy a ir.»", "p": "¿Qué haces?", "ops": ["Añado el porqué con una marca ‸: «Sí, voy a ir ‸ porque es tu cumpleaños.»", "Nada: ya he dicho que sí.", "Tacho la frase."], "ok": 0, "por": "La pauta tiene dos piezas: sí o no, y por qué. Una marca y tres palabras encima completan la pauta."},
   {"ctx": "Falta una pauta entera (la 4) y no hay sitio en el párrafo.", "p": "¿Qué haces?", "ops": ["La escribo al final del texto con un asterisco (*) y pongo otro asterisco donde va.", "La escribo en el margen, muy pequeña y sin marcas.", "No la escribo: el texto ya tiene bastantes palabras."], "ok": 0, "por": "Con dos asteriscos el corrector sabe dónde va la frase. En el margen y sin marcas se puede perder."},
   {"ctx": "La pauta 5 pide planes y tu última frase es «El verano pasado fui a Italia».", "p": "¿Qué haces?", "ops": ["Añado una frase en futuro: «Este verano voy a ir a Grecia».", "Nada: también hablo de un viaje.", "Cambio «fui» por «iba»."], "ok": 0, "por": "La frase está en el sitio de la pauta 5, pero no responde: pide planes. Hace falta una frase en futuro."},
   {"ctx": "En tu mini lista, todas las piezas tienen su ✓.", "p": "¿Qué haces?", "ops": ["Paso a la siguiente pasada: tú o usted.", "Leo otra vez todo el texto desde el principio.", "Escribo una frase más, por si acaso."], "ok": 0, "por": "Pasada hecha: a la siguiente. Leer todo otra vez gasta el tiempo de las demás pasadas."},
  ]},
 "trato": {"tipo": "c", "titulo": "Caza los errores de tú y usted",
  "tarea": "Tarea 1 · Correo de usted · Kofi escribe a su profesora para cambiar de grupo.",
  "intro": "Kofi empieza de usted, pero se le escapa el tú. Mira solo el saludo, la despedida, los verbos y tu / su. Toca las frases con error y pulsa «Comprobar».",
  "seg": [
   {"t": "Estimada señora Prieto:"},
   {"t": "Me llamo Kofi Mensah y soy alumno del curso de español de los martes."},
   {"t": "Le escribo porque la semana que viene no puedo ir a clase: tengo que viajar por trabajo."},
   {"t": "¿Puedes cambiarme a un grupo de los jueves?", "fix": "¿Puede cambiarme a un grupo de los jueves?", "por": "«Estimada señora Prieto» = usted: puede."},
   {"t": "También quería preguntarle si hay deberes para esa semana."},
   {"t": "Si hay deberes, ¿me los mandas por correo?", "fix": "Si hay deberes, ¿me los manda por correo?", "por": "Usted: manda."},
   {"t": "Siento mucho las molestias y gracias por tu ayuda.", "fix": "Siento mucho las molestias y gracias por su ayuda.", "por": "Usted: su ayuda."},
   {"t": "Un abrazo,", "fix": "Un saludo,", "por": "«Un abrazo» es para amigos. De usted: Un saludo, Saludos cordiales, Atentamente."},
   {"t": "Kofi Mensah"},
  ]},
 "pas": {"tipo": "c", "titulo": "Caza los errores de los pasados",
  "tarea": "Tarea 2 · Opción 1 · Entrada de blog · Anna cuenta su fin de semana en Cuenca.",
  "intro": "Mira solo los verbos en pasado y la palabra que dice cuándo. Toca las frases con error y pulsa «Comprobar».",
  "seg": [
   {"t": "¡Hola a todos! Hoy os cuento mi fin de semana en Cuenca."},
   {"t": "El sábado por la mañana he ido en tren con mi amigo Paul.", "fix": "El sábado por la mañana fui en tren con mi amigo Paul.", "por": "«El sábado» ya terminó: indefinido."},
   {"t": "Cuenca es una ciudad pequeña y muy bonita."},
   {"t": "El hotel estuvo en el centro y tuvo un balcón con vistas.", "fix": "El hotel estaba en el centro y tenía un balcón con vistas.", "por": "Describir cómo era el hotel: imperfecto."},
   {"t": "Primero visitamos las Casas Colgadas y después comimos en una terraza."},
   {"t": "Por la tarde paseamos por el río y hacimos muchas fotos.", "fix": "Por la tarde paseamos por el río e hicimos muchas fotos.", "por": "Hacer en indefinido: hice, hiciste, hizo, hicimos. (Y delante de «hi-», «y» se escribe «e».)"},
   {"t": "El domingo volvemos a casa muy cansados, pero contentos.", "fix": "El domingo volvimos a casa muy cansados, pero contentos.", "por": "«Volvemos» es presente. El domingo pasado: volvimos."},
   {"t": "Lo mejor fue la comida: ¡qué rica!"},
   {"t": "¿Y vosotros? ¿Habéis estado en Cuenca?"},
  ]},
 "hay": {"tipo": "c", "titulo": "Caza los errores de hay, está y es",
  "tarea": "Tarea 1 · Correo a un amigo · Iván le cuenta a Clara cómo es su piso nuevo.",
  "intro": "Mira solo hay, está y es. Toca las frases con error y pulsa «Comprobar».",
  "seg": [
   {"t": "¡Hola, Clara! ¿Qué tal todo?"},
   {"t": "Ya vivo en mi piso nuevo: está en el barrio de San Blas, cerca del metro."},
   {"t": "El piso es pequeño, pero tiene mucha luz."},
   {"t": "En mi calle está un mercado muy grande.", "fix": "En mi calle hay un mercado muy grande.", "por": "Algo existe («un mercado»): hay."},
   {"t": "El mercado hay al lado de mi portal.", "fix": "El mercado está al lado de mi portal.", "por": "Dónde está algo que ya conocemos («el mercado»): está."},
   {"t": "La parada del autobús es enfrente de mi casa.", "fix": "La parada del autobús está enfrente de mi casa.", "por": "Dónde está la parada: está."},
   {"t": "Mi vecina es muy simpática y está profesora de música.", "fix": "Mi vecina es muy simpática y es profesora de música.", "por": "Qué es (su profesión): es."},
   {"t": "¿Por qué no vienes el sábado? Te enseño el barrio."},
   {"t": "Un abrazo,"},
   {"t": "Iván"},
  ]},
 "conc": {"tipo": "c", "titulo": "Caza los errores de concordancia y posesivos",
  "tarea": "Tarea 2 · Opción 2 · Biografía · Martina Gil, veterinaria.",
  "intro": "Mira cada nombre con su artículo, su adjetivo y su posesivo. Toca las frases con error y pulsa «Comprobar».",
  "seg": [
   {"t": "Martina Gil nació en Valencia en 1970."},
   {"t": "De niña era muy tranquilo y le encantaban los animales.", "fix": "De niña era muy tranquila y le encantaban los animales.", "por": "Martina, una niña: tranquila."},
   {"t": "A los veinte años empezó a trabajar en un clínica veterinaria.", "fix": "A los veinte años empezó a trabajar en una clínica veterinaria.", "por": "La clínica: una."},
   {"t": "Allí conoció a su marido, Jorge, y tuvieron dos hijas."},
   {"t": "En 2005 abrió su propia clínica con dos compañera de trabajo.", "fix": "En 2005 abrió su propia clínica con dos compañeras de trabajo.", "por": "Dos: compañeras, en plural."},
   {"t": "Hoy sus clínica es muy famosa en la ciudad.", "fix": "Hoy su clínica es muy famosa en la ciudad.", "por": "Una clínica: su. Sus va con plural (sus clínicas)."},
   {"t": "Todavía trabaja todos los días y sus hijas la ayudan."},
   {"t": "Los fines de semana pasea con su perros por la playa.", "fix": "Los fines de semana pasea con sus perros por la playa.", "por": "Perros, plural: sus."},
  ]},
 "muy": {"tipo": "c", "titulo": "Caza los errores de muy y mucho",
  "tarea": "Tarea 2 · Opción 1 · Diario · Sara escribe sobre un día largo.",
  "intro": "Mira solo muy y mucho (mucha, muchos, muchas). Toca las frases con error y pulsa «Comprobar».",
  "seg": [
   {"t": "Querido diario: hoy ha sido un día muy largo."},
   {"t": "Por la mañana he tenido mucho trabajo en la oficina."},
   {"t": "A mediodía he comido con Eva en un restaurante mucho bueno.", "fix": "A mediodía he comido con Eva en un restaurante muy bueno.", "por": "Delante de un adjetivo (bueno): muy."},
   {"t": "Había muy gente, así que hemos esperado veinte minutos.", "fix": "Había mucha gente, así que hemos esperado veinte minutos.", "por": "Delante de un nombre (la gente): mucha."},
   {"t": "Por la tarde he ido al gimnasio y me ha gustado muy la clase nueva.", "fix": "Por la tarde he ido al gimnasio y me ha gustado mucho la clase nueva.", "por": "Con el verbo (me ha gustado): mucho."},
   {"t": "Ahora estoy muy cansada, pero contenta."},
   {"t": "Mañana quiero dormir mucho y leer un poco."},
   {"t": "¡Tengo mucha cosas que hacer este fin de semana!", "fix": "¡Tengo muchas cosas que hacer este fin de semana!", "por": "Cosas, femenino plural: muchas."},
  ]},
 "con": {"tipo": "c", "titulo": "Busca las frases con «y... y...» o «porque... porque...»",
  "tarea": "Tarea 2 · Opción 2 · Texto con fotos · Lucía cuenta una excursión con su clase de español.",
  "intro": "Aquí no hay errores de gramática: busca las frases que solo usan «y» o «porque» y que se pueden mejorar con otros conectores. Tócalas y pulsa «Comprobar».",
  "seg": [
   {"t": "El sábado pasado fui con mi clase de español a un pueblo de la montaña."},
   {"t": "Fuimos en autobús y llegamos a las diez y desayunamos chocolate con churros y subimos al castillo.", "fix": "Llegamos en autobús a las diez. Primero desayunamos chocolate con churros y después subimos al castillo.", "por": "Cuatro «y»: con primero y después la historia queda ordenada."},
   {"t": "A mediodía empezó a llover."},
   {"t": "No pudimos comer en el campo porque llovía y comimos en un bar porque estaba abierto.", "fix": "Como llovía, no pudimos comer en el campo, así que comimos en un bar.", "por": "Dos «porque»: con como (la causa) y así que (la consecuencia) se entiende mejor."},
   {"t": "El bar era pequeño, pero la comida estaba buenísima."},
   {"t": "Volvimos tarde porque el autobús se rompió y esperamos una hora y llegamos a casa a las once.", "fix": "Volvimos tarde porque el autobús se rompió: esperamos una hora y, al final, llegamos a casa a las once.", "por": "Con al final se ve que es lo último del día."},
   {"t": "Estaba cansada y estaba contenta y me reí mucho.", "fix": "Estaba cansada, pero muy contenta, y además me reí mucho.", "por": "Cansada pero contenta: es un contraste, pero. Y además añade."},
  ]},
 "lin": {"tipo": "q", "fixed": True, "titulo": "¿Corto, bien o largo?",
  "tarea": "Las dos tareas · cuenta las líneas",
  "intro": "Cuenta a ojo: unas 10 palabras por línea escrita a mano. Elige qué haces.",
  "items": [
   {"ctx": "Tarea 1 (60-70 palabras). Tu correo tiene 4 líneas y media.", "p": "¿Qué haces?", "ops": LIN_OPS, "ok": 0, "por": "Unas 45 palabras: faltan unas 20. Busca la pauta más corta y añade una frase (un porqué, un detalle)."},
   {"ctx": "Tarea 2 (70-80 palabras). Tu texto tiene 8 líneas.", "p": "¿Qué haces?", "ops": LIN_OPS, "ok": 1, "por": "Unas 80 palabras: perfecto. A la siguiente tarea."},
   {"ctx": "Tarea 1 (60-70 palabras). Tu correo tiene 11 líneas.", "p": "¿Qué haces?", "ops": LIN_OPS, "ok": 2, "por": "Unas 110 palabras: casi el doble. Pasarse mucho también baja la nota y, con más texto, hay más errores. Tacha con una raya lo que no pide ninguna pauta."},
   {"ctx": "Tarea 2 (70-80 palabras). Tienes 7 líneas, pero tu letra es grande: en una línea caben unas 7 palabras.", "p": "¿Qué haces?", "ops": LIN_OPS, "ok": 0, "por": "7 × 7 = unas 50 palabras. Con letra grande, escribe una o dos líneas más."},
   {"ctx": "Tarea 1 (60-70 palabras). Tienes 6 líneas y tu letra es pequeña: en una línea caben unas 12 palabras.", "p": "¿Qué haces?", "ops": LIN_OPS, "ok": 1, "por": "6 × 12 = unas 70 palabras. Está bien."},
   {"ctx": "Tarea 2 (70-80 palabras). Tu texto tiene 6 líneas.", "p": "¿Qué haces?", "ops": LIN_OPS, "ok": 0, "por": "Unas 60 palabras: faltan 10 o 20. ¿Alguna pauta tiene solo media línea?"},
  ]},
}

# ------------------------------------------------------------------ A CONTRARRELOJ (revisión completa)
TIEMPOS = [(300, "5 minutos (para aprender)"), (180, "3 minutos (como en el examen, tarea 2)"), (120, "2 minutos (como en el examen, tarea 1)"), (0, "Sin reloj")]

RELOJ = [
# ---------------------------------------------------------------- 1. correo a un amigo (completo)
{"id": "r1", "tipo": "Correo a una amiga", "autor": "Sam", "trato": "tu", "largo": "bien",
 "lamina": {"tarea": 1, "instr": "Una amiga le escribe para pedirle una recomendación.",
   "input": ["¡Hola! ¿Qué tal? En agosto voy a pasar una semana en tu ciudad con mi novio. ¿Qué podemos visitar? ¿Conoces un hotel bonito y no muy caro? Ah, ¿tienes tiempo para tomar algo un día?", "Un beso, Nuria"],
   "lead": "Conteste a su amiga. En el correo tiene que:",
   "pautas": ["saludar;", "recomendarle dos lugares de su ciudad y explicar por qué;", "responder a su pregunta sobre el hotel;", "decir si puede quedar con ellos y proponer un día;", "despedirse."]},
 "par": [[{"p": 1, "t": "¡Hola, Nuria! ¿Qué tal?"}],
         [{"p": 2, "t": "Tienes que visitar el castillo: las vistas son mucho bonitas.", "fix": "Tienes que visitar el castillo: las vistas son muy bonitas.", "k": "muy", "por": "Delante de un adjetivo: muy."},
          {"p": 2, "t": "Y el mercado central también me encanta, porque es antiguo."}],
         [{"p": 3, "t": "Mi hermana ha estado en el hotel Mirador el año pasado.", "fix": "Mi hermana estuvo en el hotel Mirador el año pasado.", "k": "pas", "por": "«El año pasado»: indefinido."},
          {"p": 3, "t": "El hotel hay en el centro y no es caro.", "fix": "El hotel está en el centro y no es caro.", "k": "hay", "por": "Dónde está el hotel: está."}],
         [{"p": 4, "t": "¡Claro que quiero quedar! ¿Qué te parece el domingo por la tarde?"},
          {"p": 4, "t": "Podemos tomar algo con mis amiga Laura.", "fix": "Podemos tomar algo con mi amiga Laura.", "k": "conc", "por": "Una amiga: mi."}],
         [{"p": 5, "t": "Gracias por su correo.", "fix": "Gracias por tu correo.", "k": "trato", "por": "A una amiga: tu correo."},
          {"p": 5, "t": "Un beso,"}, {"p": 0, "t": "Sam"}]],
 "leccion": "Todas las pautas están y la longitud es buena: un texto que aprueba... con cinco errores pequeños de cinco pasadas distintas. Ninguno se ve leyendo de corrido; cada uno salta en su pasada."},
# ---------------------------------------------------------------- 2. correo de usted (falta la pauta 4)
{"id": "r2", "tipo": "Correo de usted", "autor": "Greta", "trato": "usted", "largo": "corto",
 "lamina": {"tarea": 1, "instr": "Usted está de vacaciones y ha visto este anuncio.",
   "anuncio": ["BICIRUTA", "Alquiler de bicicletas y excursiones guiadas por la costa.", "Bicicletas eléctricas y para niños.", "Información: Sra. Campos (info@biciruta.es)"],
   "lead": "Escriba un correo a la señora Campos. En el correo tiene que:",
   "pautas": ["saludar;", "presentarse y decir por qué escribe;", "preguntar por el precio y el horario de las excursiones;", "explicar con quién va a ir y preguntar si hay bicicletas para niños;", "agradecer y despedirse."]},
 "falta": [4],
 "par": [[{"p": 1, "t": "Estimada señora Campos:"}],
         [{"p": 2, "t": "Me llamo Greta Lind y le escribo porque ayer he visto su anuncio.", "fix": "Me llamo Greta Lind y le escribo porque ayer vi su anuncio.", "k": "pas", "por": "«Ayer»: indefinido."},
          {"p": 2, "t": "Mis vacaciones es muy cortas: solo tengo cinco días.", "fix": "Mis vacaciones son muy cortas: solo tengo cinco días.", "k": "conc", "por": "Las vacaciones (plural): son."}],
         [{"p": 3, "t": "Me gustaría saber el precio y el horario de las excursiones."},
          {"p": 3, "t": "¿Puedes enviarme también un mapa de las rutas?", "fix": "¿Puede enviarme también un mapa de las rutas?", "k": "trato", "por": "De usted: puede."}],
         [{"p": 5, "t": "Muchas gracias por su atención."},
          {"p": 5, "t": "Un abrazo,", "fix": "Un saludo,", "k": "trato", "por": "De usted: Un saludo, Atentamente."},
          {"p": 0, "t": "Greta Lind"}]],
 "leccion": "Falta la pauta 4: Greta no dice con quién va ni pregunta por las bicicletas para niños. Por eso el correo es corto (unas 5 líneas). En la primera pasada, con la mini lista, se ve enseguida, y una frase al final con un asterisco arregla las dos cosas."},
# ---------------------------------------------------------------- 3. revista (completo)
{"id": "r3", "tipo": "Texto para una revista", "autor": "Paolo", "trato": None, "largo": "bien",
 "lamina": {"tarea": 2, "op": 1, "intro": "Una revista busca textos de sus lectores sobre «Mi mejor cumpleaños». Hable de:",
   "pautas": ["qué cumpleaños fue, cuándo y dónde;", "con quién lo celebró;", "qué hicieron;", "qué regalo le gustó más y por qué;", "cómo se sintió ese día."]},
 "par": [[{"p": 1, "t": "Mi mejor cumpleaños fue el de los treinta años, en 2022, en una casa rural de Asturias."},
          {"p": 1, "t": "La casa estuvo al lado de un río.", "fix": "La casa estaba al lado de un río.", "k": "pas", "por": "Describir dónde estaba la casa: imperfecto."},
          {"p": 2, "t": "Lo celebré con mi familia y mis mejores amigos."}],
         [{"p": 3, "t": "Cenamos y bailamos y cantamos y fuimos a dormir muy tarde.", "fix": "Primero cenamos, después bailamos y cantamos y, al final, fuimos a dormir muy tarde.", "k": "con", "por": "Cuatro «y»: primero, después, al final."}],
         [{"p": 4, "t": "Mi hermana me regaló una guitarra y me gustó muy, porque siempre he querido tocar.", "fix": "Mi hermana me regaló una guitarra y me gustó mucho, porque siempre he querido tocar.", "k": "muy", "por": "Con el verbo: me gustó mucho."},
          {"p": 5, "t": "Me sentí muy feliz, porque todos mis amigo estaban allí.", "fix": "Me sentí muy feliz, porque todos mis amigos estaban allí.", "k": "conc", "por": "Todos mis amigos: plural."}]],
 "leccion": "Paolo tiene todas las pautas y la longitud. Sus fallos son de gramática y uno de estilo (cuatro «y» seguidas). Fíjate: en un texto de buen nivel también hay fallos pequeños, y la lista los encuentra."},
# ---------------------------------------------------------------- 4. fotos (falta la pauta 3)
{"id": "r4", "tipo": "Texto con fotos", "autor": "Lin", "trato": None, "largo": "corto",
 "lamina": {"tarea": 2, "op": 2, "intro": "El mes pasado usted fue con su familia a un parque de atracciones. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la mañana. Hay una cola muy larga en la entrada; su sobrino llora.", "A mediodía. Ustedes bajan muy mojados de una atracción de agua y se ríen.", "Por la tarde. Su sobrino duerme en el coche con un peluche muy grande."],
   "img": "M3_08_dia_parque_atracciones",
   "rotulo": "Parque de atracciones: 1 cola larga y sobrino llora, 2 bajan mojados de la atraccion de agua, 3 sobrino duerme en el coche con peluche",
   "persona": "The same people appear in all three photos and must look identical: a Chinese woman of about 30 with a short black bob, a white T-shirt and a green bucket hat (the main person); her older sister, about 35, with a long black ponytail and a denim shirt; and her sister's son Leo, a boy of about 5 with a red and white striped T-shirt.",
   "escenas": ["Sunny morning at the entrance of an amusement park with a very long queue of families: little Leo is crying, and she crouches down next to him trying to comfort him while her sister looks at the long queue.",
               "Midday at a water ride in the amusement park: the three of them walk off the ride completely soaked, water dripping from their hair and clothes, laughing a lot.",
               "Late afternoon in the back seat of a parked car: Leo sleeps hugging a very big brown teddy bear; she sits next to him and looks at him, smiling and tired."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": ["con quién fue y qué pasó al llegar;", "qué hicieron a mediodía;", "cómo terminó el día y qué le pareció."]},
 "falta": [3],
 "par": [[{"p": 1, "t": "El mes pasado fui a un parque de atracciones con mi hermana y su hijo Leo."},
          {"p": 1, "t": "Cuando llegamos, estaba una cola muy larga y Leo empezó a llorar.", "fix": "Cuando llegamos, había una cola muy larga y Leo empezó a llorar.", "k": "hay", "por": "Algo existe («una cola»): había."},
          {"p": 1, "t": "Esperamos una hora, pero al final entramos."}],
         [{"p": 2, "t": "A mediodía subimos a una atracción de agua y acabamos muy mojado.", "fix": "A mediodía subimos a una atracción de agua y acabamos muy mojados.", "k": "conc", "por": "Nosotros: mojados."},
          {"p": 2, "t": "La atracción era mucho divertida y nos reímos mucho.", "fix": "La atracción era muy divertida y nos reímos mucho.", "k": "muy", "por": "Delante de un adjetivo: muy."},
          {"p": 2, "t": "Después comíamos unas hamburguesas enormes.", "fix": "Después comimos unas hamburguesas enormes.", "k": "pas", "por": "Una acción de ese día: comimos."}]],
 "leccion": "Falta la pauta 3 entera: Lin no cuenta cómo terminó el día ni qué le pareció. El texto parece terminado... y no lo está. Por eso es corto (unas 6 líneas). Con la mini lista, la primera pasada lo encuentra."},
]

# ------------------------------------------------------------------ AHORA TU
TEXTO_PROPIO_TIPOS = ["Correo a un amigo", "Correo de usted", "Blog, diario o revista", "Biografía", "Texto con fotos"]
