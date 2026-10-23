# -*- coding: utf-8 -*-
# BANCO DE "LAS PAUTAS COMO LISTA DE CONTROL" (MODULO 3 · TALLER DE ESCRITURA · PIEZA 2) DEL CURSO DE PREPARACION DELE A2
# Lo usa build_M3_pautas.py. Para cambiar laminas, textos o ejercicios, solo se toca este archivo.
#
# PAUTAS: cada pauta es {"t": texto de la lamina, "p": [piezas]}.
#   Las piezas son lo que la pauta pide, en palabras clave: una pauta doble («decir qué hizo y con quién»)
#   tiene dos piezas. El build las usa para contar, para la mini lista y para la revisión de «Ahora tú».
# TEXTOS DE ESTUDIANTES: lista de párrafos; cada párrafo, lista de (pauta, texto). pauta 0 = sin pauta (firma).
#   En "est", para cada pauta: "miss" = índices de las piezas que faltan ([] = completa; todas = falta) y "por".
#   El build comprueba que una pauta que falta no tiene ninguna frase y que una completa o a medias sí la tiene.
# FOTOS (12/10/2026): las laminas con fotos llevan "photos" (descripcion = texto alternativo), "img" (nombre fijo
# de las imagenes), "persona" y "escenas" (para los prompts). Ver fotos_M3.py.
# 12/10/2026: la nota del texto B (Max) dice lo mismo que la escala oficial: una pauta que falta te deja en el límite.

# ------------------------------------------------------------------ 1. LA REGLA (dos textos para la misma lámina)
REGLA = {
 "lamina": {"tarea": 1, "instr": "Un amigo le escribe para darle una noticia.",
   "input": ["¡Hola! Te escribo con una noticia: ¡me han dado el trabajo en Bilbao! Me voy a vivir allí en marzo. El viernes hago una pequeña fiesta de despedida en mi casa. ¿Vienes? Ah, y una pregunta: ¿tú conoces Bilbao?", "Un abrazo, Jorge"],
   "lead": "Conteste a su amigo. En el correo tiene que:",
   "pautas": [{"t": "saludar y felicitarlo por el trabajo;", "p": ["saludar", "felicitar"]},
              {"t": "decir si va a ir a la fiesta y por qué;", "p": ["¿va o no?", "¿por qué?"]},
              {"t": "responder a su pregunta sobre Bilbao;", "p": ["¿conoce Bilbao?"]},
              {"t": "darle un consejo para su nueva vida;", "p": ["un consejo"]},
              {"t": "despedirse.", "p": ["despedida"]}]},
 "textos": [
  {"autor": "Lucía", "tit": "Texto A · sencillo", "ok": True,
   "par": [[(1, "¡Hola, Jorge! ¿Qué tal? ¡Enhorabuena por el trabajo!")],
           [(2, "Claro que voy a tu fiesta el viernes, porque eres un buen amigo y quiero despedirme de ti.")],
           [(3, "Sí, conozco Bilbao: estuve allí hace dos años con mi hermana. Es una ciudad muy bonita.")],
           [(4, "Mi consejo: apúntate a un club de deporte. Así puedes conocer gente nueva.")],
           [(5, "Un abrazo y hasta el viernes,"), (0, "Lucía")]],
   "nota": "Frases cortas, vocabulario de todos los días... y las cinco pautas. <b>Aprueba.</b>"},
  {"autor": "Max", "tit": "Texto B · difícil", "ok": False,
   "par": [[(1, "¡Hola, Jorge! ¡Qué notición! ¡Enhorabuena! Llevabas meses buscando un trabajo así y por fin lo has conseguido.")],
           [(2, "Por supuesto que iré a tu fiesta, aunque el viernes salgo tarde de la oficina, así que llegaré sobre las diez. No me la perdería por nada del mundo.")],
           [(4, "Te recomiendo que no te encierres en casa los primeros meses: sal, apúntate a algo y habla con tus vecinos.")],
           [(5, "Un fuerte abrazo,"), (0, "Max")]],
   "nota": "Frases muy buenas, incluso por encima del A2... pero Jorge preguntaba por Bilbao y Max no contesta. <b>Le falta la pauta 3: está en el límite del aprobado.</b> Si le faltara otra, o una estuviera a medias, ya no sería un A2."},
 ],
}

# reparto de líneas: cuánto escribir de cada pauta
REPARTO = [("Tarea 1 · 5 pautas", "60-70 palabras ≈ 6-7 líneas", "algo más de 1 línea por pauta"),
           ("Tarea 2 · 5 pautas", "70-80 palabras ≈ 7-8 líneas", "1 línea y media por pauta"),
           ("Tarea 2 · 3 pautas", "70-80 palabras ≈ 7-8 líneas", "2 o 3 líneas por pauta")]

# ------------------------------------------------------------------ 2. LEER UNA PAUTA
VERBOS = [  # verbo de la pauta, qué pide, ejemplo
 ("saludar / despedirse", "una fórmula", "¡Hola, Jorge! · Un abrazo"),
 ("agradecer / felicitar", "una frase con gracias o enhorabuena", "Gracias por la invitación. · ¡Enhorabuena!"),
 ("decir si...", "sí o no, con claridad", "Sí, voy a ir. · No puedo ir."),
 ("explicar por qué", "una razón (porque, es que, como...)", "...porque trabajo hasta tarde."),
 ("contar / decir qué hizo", "lo que pasó, en pasado", "Fuimos a la playa y comimos paella."),
 ("describir / cómo es / cómo era", "cómo es una persona o un lugar", "Es un pueblo pequeño. · Era muy tímida."),
 ("preguntar / hacer una pregunta", "una frase con ¿...?", "¿Hay que llevar algo?"),
 ("proponer / invitar", "un plan: día, hora o lugar", "¿Quedamos el sábado a las seis?"),
 ("responder a su pregunta / propuesta", "contestar lo que pregunta el correo", "Sí, conozco Bilbao: estuve allí en 2024."),
 ("recomendar / dar un consejo", "una recomendación", "Te recomiendo el museo. · Mi consejo: ..."),
]

PISTAS = [  # palabra de la pauta, qué significa para la lista, ejemplo
 ("y", "una pieza más", "decir qué hizo <b>y</b> con quién → 2 piezas"),
 ("la coma ( , )", "una pieza más", "adónde fue<b>,</b> cuándo y con quién → 3 piezas"),
 ("y por qué", "una pieza más: la que más se olvida", "decir si va a ir <b>y por qué</b> → 2 piezas"),
 ("qué... y qué no", "lo bueno y lo malo: dos piezas", "qué le gustó más <b>y qué no</b> le gustó → 2 piezas"),
 ("o", "eliges una: no son dos piezas", "proponer otra solución <b>o</b> pedirle información → 1 pieza"),
 ("( ... )", "ejemplos para ayudarte, no obligatorios", "qué hace para cuidarse <b>(comida, deporte, descanso)</b> → 1 pieza"),
 ("dos o tres cosas", "una pieza, pero con al menos dos ejemplos", "contar <b>dos o tres</b> cosas que hizo"),
]

# ejercicio "¿Cuántas cosas pide?" (se eligen 8 al azar). nota = explicación corta (opcional)
PIEZAS = [
 ("decir adónde fue, con quién y cuántos días estuvo allí;", ["adónde", "con quién", "cuántos días"], ""),
 ("saludar;", ["saludo"], "Una sola cosa: ¡no la olvides!"),
 ("decir si va a ir a la excursión y por qué;", ["¿va o no?", "¿por qué?"], "«y por qué» es una pieza más."),
 ("decir qué le gustó más y qué no le gustó;", ["lo mejor", "lo que no le gustó"], "Lo bueno y lo malo: dos piezas."),
 ("explicar cómo era la ciudad o el pueblo donde vivía de pequeño;", ["cómo era el lugar"], "«la ciudad o el pueblo»: el que sea. Una pieza."),
 ("proponer quedar para enseñarle las fotos y despedirse.", ["proponer quedar", "despedida"], "La despedida va al final de una pauta doble: se olvida mucho."),
 ("decir dónde trabaja o estudia y cómo va;", ["dónde trabaja o estudia", "cómo va"], "«trabaja o estudia»: lo que hagas tú. Pero «y cómo va» es otra pieza."),
 ("qué compraron, dónde y para qué;", ["qué", "dónde", "para qué"], ""),
 ("cuándo fue, dónde y con quién;", ["cuándo", "dónde", "con quién"], ""),
 ("decir qué plato va a llevar y explicar cómo se prepara;", ["qué plato", "cómo se prepara"], ""),
 ("presentarse y explicar por qué escribe;", ["quién es", "por qué escribe"], ""),
 ("responder a su propuesta, proponer un día y despedirse.", ["responder", "un día", "despedida"], "Tres piezas en una pauta: la última, la despedida."),
 ("dónde vive, desde cuándo y a qué se dedica;", ["dónde vive", "desde cuándo", "a qué se dedica"], ""),
 ("qué hace para cuidarse (comida, deporte, descanso);", ["qué hace para cuidarse"], "Lo del paréntesis son ideas, no tres pautas."),
 ("agradecer y despedirse.", ["gracias", "despedida"], ""),
 ("decir si puede cuidar a la perra o no, y explicar por qué;", ["¿puede o no?", "¿por qué?"], "«o no» no es otra pieza: es la misma respuesta."),
 ("describirla físicamente;", ["cómo es (físico)"], ""),
 ("qué cosas de entonces todavía hace y qué cosas ya no hace;", ["todavía hace", "ya no hace"], ""),
 ("cómo terminó el día y cómo se sintieron.", ["cómo terminó", "cómo se sintieron"], ""),
 ("preguntar por los horarios de las clases y el precio;", ["horarios", "precio"], ""),
]

# ejercicio "¿Qué tiempo pide?" (opciones fijas)
TIEMPOS_OPS = ["Presente (hoy, normalmente)", "Pasado (ya pasó)", "Futuro (planes)"]
TIEMPOS = [
 ("qué va a hacer el próximo verano;", 2, "«Va a hacer» y «el próximo verano»: un plan. Futuro: voy a..., quiero..., pienso..."),
 ("qué hizo el fin de semana pasado;", 1, "«Hizo» y «pasado»: lo que pasó. Indefinido: fui, comí, vi..."),
 ("qué suele desayunar y a qué hora;", 0, "«Suele» = normalmente. Presente: desayuno, tomo..."),
 ("cómo era su barrio cuando era pequeño;", 1, "«Era»: describir el pasado. Imperfecto: era, había, tenía..."),
 ("qué piensa hacer en su ciudad los próximos meses;", 2, "«Piensa hacer» y «los próximos meses»: futuro."),
 ("dónde trabaja y cómo va;", 0, "Su vida de ahora: presente (trabajo en..., voy en metro)."),
 ("cómo se sintió ese día;", 1, "«Se sintió» y «ese día»: pasado (estaba nervioso, me sentí...)."),
 ("qué cosas ya no hace;", 0, "«Ya no hace»: se habla de hoy. Presente: ya no fumo, ya no trabajo..."),
]

# ------------------------------------------------------------------ 3. LA MINI LISTA
MINI = {
 "lamina": {"tarea": 2, "op": 1, "intro": "Una revista busca textos de sus lectores con este título: «Mi primer día de trabajo». Escriba un texto sobre usted. Hable de:",
   "pautas": [{"t": "cuándo fue, dónde y qué trabajo era;", "p": ["cuándo", "dónde", "qué trabajo"]},
              {"t": "cómo se sintió antes de empezar y por qué;", "p": ["cómo se sintió", "¿por qué?"]},
              {"t": "qué hizo ese día y a quién conoció;", "p": ["qué hizo", "a quién conoció"]},
              {"t": "qué fue lo más difícil;", "p": ["lo más difícil"]},
              {"t": "qué piensa hoy de ese día.", "p": ["qué piensa hoy"]}]},
 "cabecera": "revista · yo · casi todo en pasado",
 "lista": [["2019", "hotel Valencia", "recepcionista"],
           ["nerviosa", "porque: primer trabajo"],
           ["ordenador, llaves", "Pilar (jefa)"],
           ["teléfono en inglés"],
           ["hoy: buen recuerdo (pres.)"]],
 "frases": "1. En 2019 empecé a trabajar en un hotel de Valencia como recepcionista y estaba muy contenta, pero...",
 "incompleta": [["2019", "hotel"], ["nerviosa"], ["ordenador"], [], ["buen recuerdo"]],
}

MINI_PASOS = [
 ("Arriba, el trato y el tipo de texto", "En la tarea 1, escribe <b>TÚ</b> o <b>USTED</b>. En la tarea 2, qué texto es (blog, revista, biografía...) y el tiempo principal."),
 ("Una línea por pauta, con su número", "Así ves enseguida si te falta una."),
 ("Las piezas, separadas por comas", "Si la pauta pide tres cosas, en tu línea hay tres cosas. Cuenta las comas."),
 ("Palabras clave, no frases", "Dos o tres palabras por pieza: la frase la escribes después, en el texto."),
 ("Mientras escribes, marca ✓", "Cada pieza que escribes en el texto, ✓ en tu lista. Al final, todo con ✓."),
]

# ejercicio "¿Qué línea es mejor?" (q)
ML_Q = [
 {"ctx": "Pauta: «decir adónde fue, con quién y cuántos días estuvo allí»", "p": "¿Qué línea escribes en tu mini lista?",
  "ops": ["Lisboa, con Marta, 4 días", "Fui a Lisboa con mi amiga Marta y estuvimos allí cuatro días.", "Lisboa, con Marta"], "ok": 0,
  "por": "Tres piezas, tres palabras clave. La frase completa tiene las tres, pero tardas mucho; en la tercera falta «cuántos días»."},
 {"ctx": "Pauta: «decir si va a ir a la excursión y por qué»", "p": "¿Qué línea escribes?",
  "ops": ["no voy, porque: boda prima", "no voy", "Lo siento mucho, pero no puedo ir porque el sábado es la boda de mi prima."], "ok": 0,
  "por": "«y por qué» es una pieza: apúntala en la lista para no olvidarla. La frase larga va en el texto, no en la lista."},
 {"ctx": "Pauta: «qué le gustó más y qué no le gustó»", "p": "¿Qué línea escribes?",
  "ops": ["+ vistas / − hotel lejos", "vistas, comida, playa", "Lo mejor fueron las vistas y lo peor fue el hotel, que estaba lejos."], "ok": 0,
  "por": "Lo bueno y lo malo: con + y − lo ves claro. «vistas, comida, playa» son tres cosas buenas, pero falta lo que no le gustó."},
 {"ctx": "Pauta: «presentarse y explicar por qué escribe» (correo a una academia)", "p": "¿Qué línea escribes?",
  "ops": ["Ana Silva, brasileña, enfermera / anuncio curso", "anuncio curso", "Me llamo Ana Silva, soy brasileña y le escribo porque he visto su anuncio."], "ok": 0,
  "por": "Dos piezas: quién es usted y por qué escribe. Con «anuncio curso» te olvidas de presentarte."},
 {"ctx": "Pauta: «responder a su propuesta, proponer un día y despedirse»", "p": "¿Qué línea escribes?",
  "ops": ["sí, cena / ¿jueves? / un beso", "¿jueves? / un beso", "sí, cena / ¿jueves?"], "ok": 0,
  "por": "Tres piezas. La segunda línea no responde a la propuesta; la tercera se olvida de la despedida."},
]

# ejercicio "Haz tu mini lista" (con lista modelo)
ML_PRACT = {
 "lamina": {"tarea": 1, "instr": "Una amiga le escribe para proponerle un curso.",
   "input": ["¡Hola! El mes que viene empiezo un curso de fotografía, los martes por la tarde. ¿Te apuntas conmigo? Es en el centro cultural y no es caro. Tú hiciste un curso de pintura el año pasado, ¿verdad? ¿Qué tal fue?", "Un beso, Inés"],
   "lead": "Conteste a su amiga. En el correo tiene que:",
   "pautas": [{"t": "saludar;", "p": ["saludo"]},
              {"t": "decir si quiere hacer el curso de fotografía con ella y por qué;", "p": ["¿sí o no?", "¿por qué?"]},
              {"t": "contar qué tal fue su curso de pintura y qué aprendió;", "p": ["qué tal fue", "qué aprendió"]},
              {"t": "hacerle una pregunta sobre el curso de fotografía;", "p": ["una pregunta"]},
              {"t": "despedirse.", "p": ["despedida"]}]},
 "cabecera": "TÚ",
 "modelo": [["¡Hola, Inés!"], ["sí", "porque: me gusta la foto, martes libre"], ["muy bien, profe simpático (pas.)", "aprendí: colores, retratos"], ["¿cámara?"], ["un beso"]],
}

# ------------------------------------------------------------------ 4. ¿QUÉ FALTA? (textos de estudiantes)
CASOS = [  # lo que más se olvida
 "el «y por qué» o el «y con quién» del final de la pauta;",
 "contestar a la pregunta que hace el amigo en su correo;",
 "el saludo o la despedida, sobre todo cuando van pegados a otra cosa («proponer un día y despedirse»);",
 "lo malo, cuando la pauta pide lo bueno y lo malo;",
 "la última pauta, porque el texto ya es largo: se escribe mucho de una y no quedan líneas para otra;",
 "el tiempo: la pauta pide planes (futuro) y el texto cuenta el pasado, o al revés.",
]

TEXTOS = [
# ---------------------------------------------------------------- 1. correo a un amigo
{"id": "t1", "tipo": "Correo a un amigo", "autor": "Yuki",
 "lamina": {"tarea": 1, "instr": "Un amigo le escribe para pedirle ayuda.",
   "input": ["¡Hola! ¿Qué tal? Por fin tengo piso nuevo y el sábado hago la mudanza. ¿Puedes ayudarme por la mañana? Somos tres y tengo una furgoneta. Después os invito a comer. Ah, ¿sabes dónde puedo comprar muebles baratos?", "Un abrazo, Sergio"],
   "lead": "Conteste a su amigo. En el correo tiene que:",
   "pautas": [{"t": "saludar y felicitarlo por el piso nuevo;", "p": ["saludar", "felicitar"]},
              {"t": "decir si puede ayudarle el sábado y por qué;", "p": ["¿puede o no?", "¿por qué?"]},
              {"t": "responder a su pregunta sobre los muebles;", "p": ["dónde comprar muebles"]},
              {"t": "proponerle un plan para celebrar el piso nuevo;", "p": ["un plan"]},
              {"t": "despedirse.", "p": ["despedida"]}]},
 "par": [[(1, "¡Hola, Sergio! ¿Qué tal estás?")],
         [(2, "Sí, el sábado puedo ayudarte por la mañana. Tengo el día libre y, además, me gusta mucho hacer mudanzas con amigos.")],
         [(4, "Y después de la mudanza, ¿por qué no hacemos una fiesta en tu piso? Yo puedo hacer una tortilla de patatas y llevar bebidas para todos. ¿Qué te parece? Podemos invitar también a Laura y a Pedro.")],
         [(5, "Un abrazo,"), (0, "Yuki")]],
 "est": [{"miss": [1], "por": "Saluda, pero no felicita a Sergio por el piso nuevo. Bastaba con «¡Enhorabuena por el piso!»."},
         {"miss": [], "por": "Dice que sí y por qué (tiene el día libre)."},
         {"miss": [0], "por": "Sergio pregunta dónde comprar muebles baratos y Yuki no contesta. Las preguntas del correo casi siempre son pautas."},
         {"miss": [], "por": "Propone una fiesta en el piso, con muchos detalles."},
         {"miss": [], "por": "«Un abrazo»: despedida de tú, correcta."}],
 "leccion": "Yuki escribe cinco frases de la pauta 4 y se olvida de la 3. Con una frase menos en la 4 («Podemos invitar también a Laura y a Pedro»), cabía la respuesta sobre los muebles."},
# ---------------------------------------------------------------- 2. correo a un amigo (completo)
{"id": "t2", "tipo": "Correo a un amigo", "autor": "Tom",
 "lamina": {"tarea": 1, "instr": "Una amiga le escribe porque necesita ayuda con un regalo.",
   "input": ["¡Hola! El viernes es el cumpleaños de Pablo y no sé qué regalarle. Tú lo conoces muy bien. ¿Qué le gusta? ¿Me ayudas a buscar algo? Yo puedo el jueves por la tarde. Ah, ¿vienes a la cena del viernes?", "Besos, Rocío"],
   "lead": "Conteste a su amiga. En el correo tiene que:",
   "pautas": [{"t": "saludar;", "p": ["saludo"]},
              {"t": "decirle qué cosas le gustan a Pablo y proponer un regalo;", "p": ["qué le gusta", "un regalo"]},
              {"t": "decir si puede ir de compras con ella el jueves;", "p": ["¿puede o no?"]},
              {"t": "responder a su pregunta sobre la cena;", "p": ["¿va a la cena?"]},
              {"t": "despedirse.", "p": ["despedida"]}]},
 "par": [[(1, "¡Hola, Rocío! ¿Qué tal?")],
         [(2, "A Pablo le encantan la música, el fútbol y la cocina. ¿Qué te parece si le regalamos una camiseta de su equipo?")],
         [(3, "El jueves por la tarde no puedo porque tengo clase de inglés, pero el miércoles sí puedo ir contigo.")],
         [(4, "Y claro, el viernes voy a la cena. ¡Qué ganas! ¿Llevo algo de beber?")],
         [(5, "Un beso,"), (0, "Tom")]],
 "est": [{"miss": [], "por": "Saludo de tú."},
         {"miss": [], "por": "Dice qué le gusta a Pablo y propone un regalo: las dos piezas."},
         {"miss": [], "por": "No puede el jueves, pero responde a la pauta con claridad («no puedo porque...») y además propone otro día."},
         {"miss": [], "por": "Contesta a la pregunta del correo: sí va a la cena."},
         {"miss": [], "por": "«Un beso»: despedida de tú."}],
 "leccion": "¡Este está completo! No todos los textos tienen fallos: si cada pieza tiene su frase, la pauta está hecha. Decir que no («no puedo») también cumple la pauta."},
# ---------------------------------------------------------------- 3. correo de usted
{"id": "t3", "tipo": "Correo de usted", "autor": "Lena",
 "lamina": {"tarea": 1, "instr": "Usted ha visto este anuncio y quiere alquilar la habitación.",
   "anuncio": ["SE ALQUILA HABITACIÓN", "En piso compartido, cerca de la universidad. Habitación grande con balcón.", "350 € al mes, gastos incluidos.", "Contacto: Sra. Ortega (alquiler.ortega@correo.es)"],
   "lead": "Escriba un correo a la señora Ortega. En el correo tiene que:",
   "pautas": [{"t": "saludar;", "p": ["saludo"]},
              {"t": "presentarse y decir por qué escribe;", "p": ["quién es", "por qué escribe"]},
              {"t": "preguntar cuántas personas viven en el piso y cómo son;", "p": ["cuántas personas", "cómo son"]},
              {"t": "decir cuándo puede ver la habitación y cuándo quiere entrar a vivir;", "p": ["cuándo verla", "cuándo entrar a vivir"]},
              {"t": "agradecer y despedirse.", "p": ["gracias", "despedida"]}]},
 "par": [[(1, "Estimada señora Ortega:")],
         [(2, "Le escribo porque he visto su anuncio y me interesa mucho la habitación. La habitación con balcón me parece perfecta y el precio también.")],
         [(3, "Me gustaría saber cuántas personas viven en el piso y cómo son. ¿Hay lavadora en el piso?")],
         [(4, "Puedo ver la habitación el lunes o el martes por la tarde, después de clase.")],
         [(5, "Un saludo,"), (0, "Lena Fischer")]],
 "est": [{"miss": [], "por": "«Estimada señora Ortega:»: saludo de usted, perfecto."},
         {"miss": [0], "por": "Dice por qué escribe, pero no se presenta: falta quién es («Me llamo Lena Fischer, soy estudiante de Medicina...»). La firma no cuenta."},
         {"miss": [], "por": "Las dos preguntas, en una frase educada."},
         {"miss": [1], "por": "Dice cuándo puede ver la habitación, pero no cuándo quiere entrar a vivir."},
         {"miss": [0], "por": "Se despide, pero no agradece. Faltaba «Muchas gracias por su atención»."}],
 "leccion": "Ningún fallo grave... pero tres pautas a medias. Las pautas dobles son la trampa: Lena hace la primera parte y se olvida de la segunda. Y la pregunta de la lavadora no la pide nadie: ese espacio era para presentarse."},
# ---------------------------------------------------------------- 4. revista (difícil, le faltan cosas)
{"id": "t4", "tipo": "Texto para una revista", "autor": "Ahmed",
 "lamina": {"tarea": 2, "op": 1, "intro": "Una revista busca textos de sus lectores sobre «Una fiesta especial». Hable de:",
   "pautas": [{"t": "qué fiesta fue, cuándo y dónde;", "p": ["qué fiesta", "cuándo", "dónde"]},
              {"t": "con quién estuvo;", "p": ["con quién"]},
              {"t": "qué hicieron;", "p": ["qué hicieron"]},
              {"t": "qué fue lo mejor y qué fue lo peor;", "p": ["lo mejor", "lo peor"]},
              {"t": "si quiere repetir el año que viene y por qué.", "p": ["¿repite?", "¿por qué?"]}]},
 "par": [[(1, "El pasado mes de junio celebré por primera vez la Noche de San Juan en Alicante, una fiesta que llevaba años queriendo conocer."),
          (2, "Fui con mis compañeros de piso, que son de aquí y me lo explicaron todo.")],
         [(3, "Cenamos en la playa, vimos las hogueras arder hasta la madrugada y, a medianoche, nos bañamos en el mar, porque dicen que trae buena suerte.")],
         [(4, "Lo que más me impresionó fue el ambiente: miles de personas cantando y bailando juntas sin conocerse.")]],
 "est": [{"miss": [], "por": "Qué fiesta (San Juan), cuándo (junio) y dónde (Alicante): las tres piezas en una frase."},
         {"miss": [], "por": "Con sus compañeros de piso."},
         {"miss": [], "por": "Cena, hogueras, baño a medianoche: muy completo."},
         {"miss": [1], "por": "Dice lo mejor (el ambiente), pero no dice lo peor."},
         {"miss": [0, 1], "por": "No hay ni una frase sobre el año que viene. Falta la pauta entera."}],
 "leccion": "Un texto de muy buen nivel (llevaba años queriendo, lo que más me impresionó...) al que le falta una pauta y media. Con 80 palabras ya, no quedaba sitio: con una mini lista y una línea menos en la pauta 3, cabía «El año que viene quiero repetir porque...»."},
# ---------------------------------------------------------------- 5. diario (frase sí, pauta no)
{"id": "t5", "tipo": "Diario", "autor": "Olga",
 "lamina": {"tarea": 2, "op": 1, "intro": "Escriba una entrada en su diario sobre un cambio importante en su vida. Hable de:",
   "pautas": [{"t": "qué cambio ha sido y cuándo empezó;", "p": ["qué cambio", "cuándo"]},
              {"t": "cómo era su vida antes;", "p": ["cómo era antes"]},
              {"t": "qué cosas son diferentes ahora;", "p": ["qué es diferente ahora"]},
              {"t": "cómo se siente;", "p": ["cómo se siente"]},
              {"t": "qué planes tiene para los próximos meses.", "p": ["planes"]}]},
 "par": [[(1, "Querido diario: hace tres meses dejé la ciudad y me vine a vivir a un pueblo pequeño.")],
         [(2, "Antes vivía en un piso pequeño en Madrid, trabajaba diez horas al día y casi no veía a mis amigos."),
          (3, "Ahora trabajo desde casa, tengo un huerto y por las tardes paseo con mi perro por el bosque."),
          (4, "Me siento más tranquila y duermo mucho mejor.")],
         [(0, "El mes pasado aprendí a hacer pan y conocí a mis vecinos, que son muy simpáticos.")]],
 "est": [{"miss": [], "por": "Qué cambio (del piso al pueblo) y cuándo (hace tres meses)."},
         {"miss": [], "por": "Imperfecto para el antes: vivía, trabajaba, veía."},
         {"miss": [], "por": "Presente para el ahora: trabajo, tengo, paseo."},
         {"miss": [], "por": "Más tranquila, duerme mejor."},
         {"miss": [0], "por": "La última frase habla del mes pasado, no de los planes. Parece la pauta 5, pero no lo es: faltaba «Este verano quiero...» o «Voy a...»."}],
 "leccion": "Cuidado con la última frase: está en el sitio de la pauta 5, pero cuenta el pasado. Una frase no cumple la pauta si no responde a lo que pide. Mira siempre el tiempo: «planes» = futuro."},
# ---------------------------------------------------------------- 6. biografía
{"id": "t6", "tipo": "Biografía", "autor": "Pierre",
 "lamina": {"tarea": 2, "op": 2, "intro": "Lucía Ramos es pintora. Aquí tiene algunas fotos y datos sobre su vida.",
   "photos": ["Una niña de unos siete años dibuja en la pared de su casa con una tiza; su madre la mira.", "Una mujer joven, con gafas, enseña a dibujar a un grupo de adolescentes en un aula.", "La misma mujer, hoy, con el pelo blanco, delante de un cuadro grande en una galería."],
   "img": "M3_05_bio_lucia_pintora",
   "rotulo": "Biografia Lucia pintora: 1 nina dibuja con tiza en la pared, 2 profesora de dibujo con gafas, 3 mayor ante un cuadro en galeria",
   "persona": "These three photos show the same Spanish woman, Lucía, at three ages, and she must be clearly recognisable in all of them: a narrow face, big dark eyes, thick dark eyebrows, a pointed chin and long straight hair (black when she is young, white in the last photo); from her twenties on she wears round tortoiseshell glasses.",
   "escenas": ["1970s look, slightly faded colours: Lucía at about 7, without glasses, kneels and draws a big sun and a house on the wall of her home with a piece of white chalk; her mother watches from the doorway with her arms crossed, half smiling.",
               "Early 1990s look: Lucía at about 30, with round glasses and a paint-stained shirt, teaches a group of teenagers to draw in a school art room, leaning over a student's drawing and pointing at it.",
               "Today: Lucía at about 60, with long straight white hair and round glasses, stands calmly in front of a large colourful abstract painting in an art gallery with white walls and wooden floor, looking at it."],
   "ficha": ["Nació en Zaragoza en 1965.", "De niña: dibuja en todas partes; muy tímida.", "1984: estudia Bellas Artes en Barcelona.", "1990-2005: profesora de dibujo en un instituto.", "2006: deja el instituto y abre su propio taller.", "Hoy: expone en galerías de Europa; da clases a niños los sábados."],
   "intro2": "Escriba un texto sobre Lucía. Hable de:",
   "pautas": [{"t": "dónde y cuándo nació y cómo era de niña;", "p": ["dónde", "cuándo", "cómo era"]},
              {"t": "qué estudió y en qué trabajó;", "p": ["qué estudió", "en qué trabajó"]},
              {"t": "qué cambió en 2006 y qué hace ahora.", "p": ["el cambio de 2006", "qué hace ahora"]}]},
 "par": [[(1, "Lucía Ramos nació en 1965. De niña era muy tímida y dibujaba en todas partes.")],
         [(2, "En 1984 se fue a Barcelona y estudió Bellas Artes. Después, durante quince años, fue profesora de dibujo en un instituto.")],
         [(3, "En 2006 dejó el instituto y abrió su propio taller, porque quería pintar todo el día. Sus cuadros son muy bonitos y tienen muchos colores. Me gusta mucho su historia.")]],
 "est": [{"miss": [0], "por": "Dice cuándo nació y cómo era, pero no dónde: falta «en Zaragoza». Tres piezas, dos frases... y una se escapa."},
         {"miss": [], "por": "Qué estudió (Bellas Artes) y en qué trabajó (profesora de dibujo)."},
         {"miss": [1], "por": "Cuenta el cambio de 2006, pero no qué hace ahora (expone en galerías, da clases a niños). «Sus cuadros son muy bonitos» es una opinión, no lo que hace."}],
 "leccion": "Además, el texto es corto: unas 65 palabras, y la tarea pide 70-80. ¡Tenía sitio para las dos piezas que faltan! En la biografía, mira la ficha: cada dato que piden las pautas tiene que estar en el texto."},
# ---------------------------------------------------------------- 7. fotos
{"id": "t7", "tipo": "Texto con fotos", "autor": "Kenji",
 "lamina": {"tarea": 2, "op": 2, "intro": "El sábado pasado usted fue con unos amigos a un concierto al aire libre. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la tarde. Usted y tres amigos hacen cola en la entrada de un parque; hace mucho calor y todos llevan gorra.", "Por la noche. En el concierto, de repente, se va la luz y la música para. La gente espera con la linterna del móvil.", "Más tarde. Vuelve la luz; el cantante baja del escenario y canta entre el público."],
   "img": "M3_06_dia_concierto_apagon",
   "rotulo": "Concierto con apagon: 1 cola con calor y gorras, 2 se va la luz y linternas del movil, 3 el cantante canta entre el publico",
   "persona": "The same main person appears in all three photos and must look identical: a Japanese man of about 25 with short black hair, a white T-shirt, a red cap and a small black backpack. His three friends (a tall blond man, a woman with very short hair and a woman with long red hair, all about 25) are with him.",
   "escenas": ["Late afternoon, very hot and sunny: he and his three friends wait in a long queue at the entrance gate of a city park for an open-air concert; they all wear caps, one fans herself with her hand, another drinks from a water bottle.",
               "Night at the open-air concert: the stage lights have gone out and the music has stopped; the crowd in the dark holds up their phone torches; he and his friends look around, surprised, lit only by the phones.",
               "Later at night: the stage lights are back on; the singer, a man with a microphone, has come down from the stage and sings in the middle of the crowd; he stands right next to the singer, singing along with one arm up."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": [{"t": "dónde fue, con quién y qué hicieron antes del concierto;", "p": ["dónde", "con quién", "qué hicieron antes"]},
              {"t": "qué problema hubo durante el concierto;", "p": ["el problema"]},
              {"t": "cómo terminó la noche y qué le pareció el concierto.", "p": ["cómo terminó", "su opinión"]}]},
 "par": [[(1, "El sábado pasado fui a un concierto en el parque con tres amigos de la universidad. Antes de entrar hicimos cola casi una hora y hacía muchísimo calor.")],
         [(2, "Durante el concierto, de repente, se fue la luz y la música paró. Todos encendimos la linterna del móvil y esperamos. Algunas personas gritaban, pero otras cantaban sin música.")],
         [(3, "Al final volvió la luz y el cantante bajó del escenario a cantar con la gente.")]],
 "est": [{"miss": [], "por": "Dónde (el parque), con quién (tres amigos) y qué hicieron antes (cola, calor)."},
         {"miss": [], "por": "El apagón, contado en pasado, con muy buenos detalles."},
         {"miss": [1], "por": "Cuenta cómo terminó, pero no dice qué le pareció el concierto. Una frase bastaba: «Fue un concierto increíble»."}],
 "leccion": "La última pieza de la última pauta es la que más se olvida: el texto parece terminado y no lo está. Antes de entregar, lee tu mini lista hasta el final."},
# ---------------------------------------------------------------- 8. correo a un amigo (sin despedida)
{"id": "t8", "tipo": "Correo a un amigo", "autor": "Irina",
 "lamina": {"tarea": 1, "instr": "Un amigo le escribe porque ha vuelto de un viaje.",
   "input": ["¡Hola! Ya estoy en casa después de un mes en México. ¡Ha sido increíble! Te he traído un regalo. ¿Quedamos esta semana y te lo doy? Por cierto, ¿qué tal tu examen de conducir?", "Un abrazo, Álex"],
   "lead": "Conteste a su amigo. En el correo tiene que:",
   "pautas": [{"t": "saludar y preguntarle por el viaje;", "p": ["saludar", "preguntar por el viaje"]},
              {"t": "contar qué tal fue su examen de conducir y cómo se sintió;", "p": ["qué tal fue", "cómo se sintió"]},
              {"t": "contarle algo que ha hecho usted este mes;", "p": ["algo de este mes"]},
              {"t": "responder a su propuesta, proponer un día y despedirse.", "p": ["responder", "un día", "despedida"]}]},
 "par": [[(1, "¡Hola, Álex! ¡Qué bien que ya estás en casa! ¿Qué tal México? ¿Qué ciudades visitaste?")],
         [(2, "Mi examen de conducir fue un desastre: suspendí porque estaba muy nerviosa y no vi una señal de stop. Pero en diciembre lo hago otra vez.")],
         [(3, "Este mes he empezado a ir a clases de yoga y me encantan.")],
         [(4, "¡Sí, claro! ¿Quedamos el jueves en la cafetería de siempre?")]],
 "est": [{"miss": [], "por": "Saluda y pregunta por el viaje (¿Qué tal México?)."},
         {"miss": [], "por": "Qué tal fue (un desastre) y cómo se sintió (muy nerviosa)."},
         {"miss": [], "por": "Las clases de yoga: algo de este mes, con el perfecto («he empezado»)."},
         {"miss": [2], "por": "Responde («¡Sí, claro!») y propone el jueves, pero no se despide. Ni «Un abrazo» ni «Hasta el jueves»."}],
 "leccion": "La despedida es la pieza más fácil... y la que más se olvida cuando va al final de una pauta de tres cosas. En la mini lista, escríbela siempre: «un abrazo»."},
]

# ejercicio "¿Cumple la pauta?" (opciones fijas; se eligen 8 al azar)
CUMPLE_OPS = ["Sí: está completa.", "A medias: falta una parte.", "No: no responde a la pauta."]
CUMPLE = [
 {"ctx": "Pauta: «decir si va a ir a la fiesta y por qué»", "p": "Frase: «Sí, voy a ir a tu fiesta.»", "ok": 1, "por": "Dice que sí, pero falta el porqué. Por ejemplo: «...porque me encantan tus fiestas»."},
 {"ctx": "Pauta: «proponer otro plan para el domingo»", "p": "Frase: «¿Por qué no vamos al cine el domingo por la tarde?»", "ok": 0, "por": "Un plan, con día y hora. Completa."},
 {"ctx": "Pauta: «contar qué hizo el fin de semana pasado»", "p": "Frase: «Normalmente los fines de semana voy al gimnasio y veo series.»", "ok": 2, "por": "Habla de lo que hace normalmente, no de ese fin de semana. Pedía pasado: «El sábado fui...»."},
 {"ctx": "Pauta: «decir qué le gustó más y qué no le gustó»", "p": "Frase: «Lo mejor fue la comida, pero el hotel era muy ruidoso.»", "ok": 0, "por": "Lo bueno y lo malo, en una sola frase. Completa."},
 {"ctx": "Pauta: «preguntar por el horario y el precio del curso»", "p": "Frase: «¿Cuánto cuesta el curso?»", "ok": 1, "por": "Pregunta el precio, pero no el horario."},
 {"ctx": "Pauta: «explicar cómo se siente en su nueva ciudad»", "p": "Frase: «Mi nueva ciudad es grande y tiene muchos parques.»", "ok": 2, "por": "Describe la ciudad, pero la pauta pregunta cómo se siente usted: «Me siento muy bien / un poco solo...»."},
 {"ctx": "Pauta: «despedirse»", "p": "Frase: «Hasta pronto, Ana»", "ok": 0, "por": "Una despedida de tú. Completa."},
 {"ctx": "Pauta: «qué va a hacer el próximo verano»", "p": "Frase: «El verano pasado fui a Italia con mi familia.»", "ok": 2, "por": "Pide planes (futuro) y la frase cuenta el pasado. No responde: «El próximo verano voy a ir...»."},
 {"ctx": "Pauta: «presentarse y explicar por qué escribe»", "p": "Frase: «Me llamo Iván, soy estudiante y le escribo porque quiero información sobre el curso.»", "ok": 0, "por": "Quién es y por qué escribe: las dos piezas."},
 {"ctx": "Pauta: «decir adónde fue, cuándo y con quién»", "p": "Frase: «En agosto fui a Galicia.»", "ok": 1, "por": "Adónde y cuándo, sí; con quién, no."},
]

# ------------------------------------------------------------------ 5. AHORA TÚ
AHORA = [
 {"id": "a1", "n": "Correo a una amiga", "trato": "tu",
  "lamina": {"tarea": 1, "instr": "Una amiga le escribe para proponerle un plan.",
   "input": ["¡Hola! ¿Cómo estás? El domingo es el día sin coches en la ciudad y hay actividades en el parque: conciertos, juegos, comida... ¿Te vienes? Podemos ir en bici. ¿Tienes bici? Si no, yo te dejo la de mi hermano.", "Un beso, Paula"],
   "lead": "Conteste a su amiga. En el correo tiene que:",
   "pautas": [{"t": "saludar;", "p": ["saludo"]},
              {"t": "decir si quiere ir y qué actividad le interesa más;", "p": ["¿va o no?", "qué actividad"]},
              {"t": "responder a su pregunta sobre la bici;", "p": ["¿tiene bici?"]},
              {"t": "proponer una hora y un lugar para quedar;", "p": ["hora", "lugar"]},
              {"t": "despedirse.", "p": ["despedida"]}]}},
 {"id": "a2", "n": "Correo de usted", "trato": "usted",
  "lamina": {"tarea": 1, "instr": "Usted ha visto este anuncio y quiere más información.",
   "anuncio": ["CURSO DE FOTOGRAFÍA PARA PRINCIPIANTES", "Centro cultural La Lonja. Grupos de mañana y de tarde.", "Salidas a fotografiar la ciudad los sábados.", "Información: Sr. Morales (cursos@lalonja.es)"],
   "lead": "Escriba un correo al señor Morales. En el correo tiene que:",
   "pautas": [{"t": "saludar;", "p": ["saludo"]},
              {"t": "presentarse y explicar por qué le interesa el curso;", "p": ["quién es", "por qué le interesa"]},
              {"t": "preguntar por el precio y la duración del curso;", "p": ["precio", "duración"]},
              {"t": "preguntar si necesita una cámara profesional;", "p": ["¿cámara profesional?"]},
              {"t": "agradecer y despedirse.", "p": ["gracias", "despedida"]}]}},
 {"id": "a3", "n": "Texto para una revista", "trato": None,
  "lamina": {"tarea": 2, "op": 1, "intro": "Una revista busca textos de sus lectores sobre «Mi lugar favorito de la ciudad». Hable de:",
   "pautas": [{"t": "qué lugar es y dónde está;", "p": ["qué lugar", "dónde"]},
              {"t": "cómo es;", "p": ["cómo es"]},
              {"t": "cuándo va y con quién;", "p": ["cuándo", "con quién"]},
              {"t": "qué hace allí;", "p": ["qué hace"]},
              {"t": "por qué es especial para usted.", "p": ["¿por qué es especial?"]}]}},
 {"id": "a4", "n": "Texto con fotos", "trato": None,
  "lamina": {"tarea": 2, "op": 2, "intro": "El verano pasado usted fue a la boda de una prima en un pueblo. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la mañana. Usted, con ropa de fiesta, cambia una rueda del coche en una carretera; un amigo mira el reloj.", "A mediodía. Usted llega a la iglesia cuando los novios ya salen; todos les tiran arroz.", "Por la noche. Usted baila con la abuela de la novia en el banquete; todos aplauden."],
   "img": "M3_07_dia_boda_prima",
   "rotulo": "Boda de una prima: 1 cambia una rueda en la carretera, 2 llega a la iglesia y tiran arroz, 3 baila con la abuela de la novia",
   "persona": "The same main person appears in all three photos and must look identical: a Colombian man of about 40 with wavy black hair, a thick black moustache, a light blue suit, a white shirt and a pink tie. His friend in the first photo is a bald man of about 40 in a dark grey suit.",
   "escenas": ["Summer morning on a quiet country road next to fields: in his light blue suit he kneels by a car changing a flat tyre with a jack, his jacket on the car roof; his friend stands beside him looking at his watch, worried.",
               "Midday in front of a small stone village church: he arrives hurrying, a bit out of breath, just as the bride and groom come out of the church door and the guests throw rice at them.",
               "Night at the wedding banquet in a garden with string lights: he dances with the bride's grandmother, a small elderly woman with white hair and a dark blue dress, both laughing, while the guests around them clap."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": [{"t": "qué problema tuvo por la mañana y qué hizo;", "p": ["el problema", "qué hizo"]},
              {"t": "qué pasó cuando llegó a la boda;", "p": ["qué pasó al llegar"]},
              {"t": "cómo fue la fiesta y cómo se sintió.", "p": ["cómo fue la fiesta", "cómo se sintió"]}]}},
]

CHECK_COMUN = ["He contado las líneas a ojo (unas 10 palabras por línea).", "Ninguna pauta tiene muchas líneas y otra casi nada."]
CHECK_CORREO = ["Saludo y despedida del mismo trato: todo de tú o todo de usted."]
CHECK_TEXTO = ["El tiempo de cada pauta es el que pide (pasado, presente o planes)."]
