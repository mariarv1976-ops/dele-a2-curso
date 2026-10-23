# -*- coding: utf-8 -*-
# BANCO DE REFUERZO DE LA ESCRITURA (curso de preparacion DELE A2, Modulo 3, pieza 6)
# Lo usa build_M3_banco.py. Para ANADIR UNA LAMINA: copia un bloque de LAMINAS, cambia el id, el titulo,
# la lamina, las pautas (texto, piezas y tiempos) y el texto modelo, y vuelve a ejecutar el build.
#
# Decidido con Maria (23/10/2026): los cinco tipos del kit M3-1; el correo de usted con pocas laminas, marcadas
# «por si acaso» y fuera de «Como en el examen» (la T1 real es de tu). Se descarto «describir una foto por escrito»
# porque no es una tarea de la escritura del A2 y choca con la trampa del kit (describir las fotos en presente).
# Todo original: no repite el kit, las pautas, la banda 1, la revision, los textos modelo ni M1, M6 y M7
# (ni lo previsto para el M2: amigo que viene de visita, comida especial, diario de viaje).
#
# Cada pauta lleva:
#   "t"  -> el texto de la pauta, como en la lamina
#   "p"  -> las piezas de la pauta (salen en la lista de control: cada pieza, al menos una frase)
#   "ti" -> los tiempos que pide: "pres" (presente), "pas" (lo que paso: fui, he ido),
#           "antes" (como era: era, tenia, iba) y "fut" (planes: voy a, quiero, me gustaria). Puede ir vacio (saludar).
# Texto modelo: lista de (pauta, texto). Pauta 0 = la firma. Marcas: {p:...} {s:...} {a:...} {f:...} para los
# tiempos (p presente, s pasado, a antes, f futuro y planes) y {c:...} para los conectores.
# El build comprueba: palabras del modelo (T1 60-70, T2 70-80), texto de entrada de la T1 (35-45), que cada pauta
# use sus tiempos en su parrafo, que cada lamina mezcle al menos tres tiempos, tu/usted y que no haya formas de B1.

TIEMPOS = {
 "pres":  {"n": "Presente", "f": "es, tengo, me gusta, hay"},
 "pas":   {"n": "Pasado", "f": "fui, conocí, he hecho, ha sido"},
 "antes": {"n": "Cómo era", "f": "era, tenía, había, iba"},
 "fut":   {"n": "Planes", "f": "voy a, vamos a, quiero, me gustaría"},
}
ORDEN_TIEMPOS = ["pres", "pas", "antes", "fut"]

TIPOS = {
 "inf":  {"n": "Correo a un amigo", "tarea": 1, "kit": "Correo a un amigo"},
 "blog": {"n": "Blog, diario o revista", "tarea": 2, "op": 1, "kit": "Blog o diario"},
 "bio":  {"n": "Biografía", "tarea": 2, "op": 2, "kit": "Biografía"},
 "dia":  {"n": "Un día con fotos", "tarea": 2, "op": 2, "kit": "Con fotos"},
 "for":  {"n": "Correo de usted (por si acaso)", "tarea": 1, "kit": "Correo de usted"},
}
ORDEN_TIPOS = ["inf", "blog", "bio", "dia", "for"]

# Frases nuevas para cada tipo (no repiten las del kit: en el kit hay mas)
FRASES = {
 "inf":  ["¡Me alegro mucho por ti!", "Te cuento una cosa:", "¿Te parece bien el sábado a las seis?", "¡Qué ganas tengo de verte!", "Cuéntame qué tal todo.", "¡Hasta muy pronto!"],
 "for":  ["Le escribo para contestar a su correo.", "Le confirmo que...", "Lo siento, pero no voy a poder...", "Quería preguntarle también...", "Muchas gracias por todo.", "Un cordial saludo,"],
 "blog": ["Os quiero contar...", "Al principio..., pero después...", "Lo que más recuerdo es...", "Desde entonces...", "Normalmente, cuando...", "¿Y vosotros?"],
 "bio":  ["Al terminar sus estudios...", "Unos años después...", "Por las noches, estudiaba...", "Al principio..., pero luego...", "Hoy todavía...", "Creo que... porque..."],
 "dia":  ["Ese día...", "Primero... y después...", "De repente...", "Por suerte...", "Al final del día...", "Creo que la próxima vez..."],
}

# Avisos por tipo (se ven encima de la lamina en Practica)
AVISO = {
 "inf":  "Todo de <b>tú</b>, del saludo a la despedida. Las preguntas del correo de tu amigo casi siempre son pautas: contéstalas.",
 "for":  "<b>Por si acaso.</b> En los exámenes publicados la tarea 1 es de tú, con un amigo o un familiar. Este correo de <b>usted</b> sirve por si te toca uno: todo de usted, sin besos ni abrazos.",
 "blog": "Hablas de tu vida, así que los tiempos se mezclan: lo que pasó, cómo era, cómo es ahora y tus planes. Mira el color de cada pauta.",
 "bio":  "Convierte cada dato en una frase en pasado y únelas con marcadores de tiempo. La última pauta pide tu opinión: «Creo que... porque...».",
 "dia":  "<b>No describes las fotos: cuentas lo que pasó</b>, en pasado y en orden, porque tú estabas allí. Nada de «En la foto 1 hay...».",
}

LAMINAS = [
# ====================================================================== T1 · CORREO A UN AMIGO (6)
{"id": "a1", "tipo": "inf", "titulo": "Lola empieza la universidad",
 "lamina": {"tarea": 1, "instr": "Su amiga Lola le ha escrito este correo.",
   "input": ["¡Hola! ¿Cómo va todo? Te cuento una noticia: con cincuenta años, ¡he empezado a estudiar Historia en la universidad! Tengo clase tres tardes a la semana y estoy muy contenta, pero un poco nerviosa. ¿Y tú? ¿Qué tal estás?", "Un beso,<br>Lola"],
   "lead": "Conteste a Lola. En el correo tiene que:",
   "pautas": [
    {"t": "saludar y felicitarla por la noticia;", "p": ["saludar", "felicitarla"], "ti": ["pres"]},
    {"t": "contarle si usted ha estudiado algo en los últimos años y qué tal fue;", "p": ["qué ha estudiado", "qué tal fue"], "ti": ["pas"]},
    {"t": "explicarle qué asignatura le gustaba más en el colegio y por qué;", "p": ["qué asignatura", "por qué"], "ti": ["antes"]},
    {"t": "proponerle una cena para celebrarlo: el día y el lugar;", "p": ["la cena", "el día", "el lugar"], "ti": ["fut"]},
    {"t": "hacerle dos preguntas sobre sus clases y despedirse.", "p": ["dos preguntas", "despedirse"], "ti": ["pres"]}]},
 "modelo": [
  (1, "¡Hola, Lola! ¡Enhorabuena! Tu noticia me {p:parece} fantástica."),
  (2, "Yo {s:he hecho} un curso de fotografía este año y {s:ha sido} muy divertido."),
  (3, "En el colegio me {a:gustaba} mucho la Historia {c:porque} la profesora {a:contaba} unas historias increíbles."),
  (4, "Para celebrarlo, ¿{f:vamos a cenar} el viernes al restaurante del puerto?"),
  (5, "¿{p:Son} difíciles los exámenes? ¿{p:Hay} mucha gente de tu edad? Un beso muy fuerte,"),
  (0, "Elena")]},

{"id": "a2", "tipo": "inf", "titulo": "Hugo y su perro Rufo",
 "lamina": {"tarea": 1, "instr": "Su amigo Hugo le ha escrito este correo.",
   "input": ["¡Hola! ¿Qué tal? Te escribo para pedirte un favor. El próximo fin de semana voy a una boda en Sevilla y no puedo llevar a Rufo. ¿Puedes cuidarlo en tu casa? Es muy bueno y solo come dos veces al día.", "Un abrazo,<br>Hugo"],
   "lead": "Conteste a Hugo. En el correo tiene que:",
   "pautas": [
    {"t": "saludar y decirle si puede cuidar a Rufo y por qué;", "p": ["saludar", "sí o no", "por qué"], "ti": ["pres"]},
    {"t": "contarle qué hizo usted el último fin de semana;", "p": ["qué hizo"], "ti": ["pas"]},
    {"t": "explicarle si tenía animales cuando era pequeño o pequeña y cómo eran;", "p": ["si tenía animales", "cómo eran"], "ti": ["antes"]},
    {"t": "decirle qué va a hacer con Rufo o, si no puede cuidarlo, proponerle otra solución;", "p": ["qué va a hacer con Rufo (u otra solución)"], "ti": ["fut"]},
    {"t": "hacerle dos preguntas sobre la boda y despedirse.", "p": ["dos preguntas", "despedirse"], "ti": ["pres"]}]},
 "modelo": [
  (1, "¡Hola, Hugo! ¡Claro que {p:puedo} cuidar a Rufo! Ese fin de semana {p:estoy} en casa."),
  (2, "El sábado pasado {s:fui} a la montaña con mi hermana y {s:comimos} en un pueblo precioso."),
  (3, "De pequeña {a:tenía} dos gatos: {a:eran} muy perezosos y {a:dormían} todo el día."),
  (4, "Con Rufo {f:voy a ir} al parque todas las mañanas, ¡no te preocupes!"),
  (5, "¿Quién {p:se casa}? ¿{p:Vuelves} el domingo por la noche? Un abrazo,"),
  (0, "Marta")]},

{"id": "a3", "tipo": "inf", "titulo": "Iván no fue a la clase de inglés",
 "lamina": {"tarea": 1, "instr": "Iván, un compañero de su clase de inglés, le ha escrito este correo.",
   "input": ["¡Hola! ¿Qué tal? El martes no fui a clase porque estaba enfermo. ¿Qué hicisteis? ¿Hay deberes para el jueves? Ah, y el sábado quiero estudiar un poco para el examen de diciembre. ¿Te apetece estudiar conmigo?", "Hasta pronto,<br>Iván"],
   "lead": "Conteste a Iván. En el correo tiene que:",
   "pautas": [
    {"t": "saludar y preguntarle cómo está;", "p": ["saludar", "preguntar cómo está"], "ti": ["pres"]},
    {"t": "contarle qué hicieron en la clase del martes;", "p": ["qué hicieron"], "ti": ["pas"]},
    {"t": "explicarle qué deberes tienen para el jueves;", "p": ["qué deberes"], "ti": ["pres"]},
    {"t": "contestar si quiere estudiar con él y proponerle la hora y el lugar;", "p": ["sí o no", "la hora", "el lugar"], "ti": ["fut"]},
    {"t": "contarle cómo preparaba usted antes los exámenes y despedirse.", "p": ["cómo preparaba los exámenes", "despedirse"], "ti": ["antes"]}]},
 "modelo": [
  (1, "¡Hola, Iván! ¿{p:Estás} mejor?"),
  (2, "El martes {s:vimos} un vídeo sobre Londres y después {s:hablamos} en parejas de las vacaciones."),
  (3, "Para el jueves {p:hay que} hacer los ejercicios de la página cuarenta y {p:tenemos que} llevar una foto de nuestra familia."),
  (4, "{f:Vamos a estudiar} el sábado a las diez en la biblioteca de mi barrio, ¿vale?"),
  (5, "Antes yo {a:estudiaba} sola, {c:pero} con un compañero {p:es} más fácil. ¡Hasta el sábado!"),
  (0, "Sara")]},

{"id": "a4", "tipo": "inf", "titulo": "Una invitación del tío Paco",
 "lamina": {"tarea": 1, "instr": "Su tío Paco le ha escrito este correo.",
   "input": ["¡Hola! ¿Cómo estás? Este verano vamos a pasar todo agosto en la casa del pueblo. ¿Por qué no vienes unos días? Hay sitio para ti y en el pueblo hace menos calor que en la ciudad. Tus primos también van a venir.", "Un beso muy fuerte,<br>tío Paco"],
   "lead": "Conteste a su tío. En el correo tiene que:",
   "pautas": [
    {"t": "saludar y agradecerle la invitación;", "p": ["saludar", "agradecer"], "ti": ["pres"]},
    {"t": "contarle qué ha hecho usted este verano;", "p": ["qué ha hecho"], "ti": ["pas"]},
    {"t": "decirle qué días puede ir y cómo va a viajar;", "p": ["qué días", "cómo va a viajar"], "ti": ["fut"]},
    {"t": "recordar algo que hacía en el pueblo cuando era pequeño o pequeña;", "p": ["un recuerdo del pueblo"], "ti": ["antes"]},
    {"t": "preguntarle qué tiene que llevar y despedirse.", "p": ["qué tiene que llevar", "despedirse"], "ti": ["pres"]}]},
 "modelo": [
  (1, "¡Hola, tío! Muchas gracias por invitarme. ¡Me {p:encanta} la idea!"),
  (2, "Este verano {s:he trabajado} mucho, {c:pero} en julio {s:he pasado} una semana en la playa con unos amigos."),
  (3, "{p:Puedo} ir del diez al quince de agosto y {f:voy a ir} en autobús."),
  (4, "¿Te acuerdas? De pequeño {a:iba} al río con mis primos y siempre {a:volvíamos} muy tarde a casa."),
  (5, "¿{p:Tengo que} llevar algo? Un beso muy fuerte para todos,"),
  (0, "Javi")]},

{"id": "a5", "tipo": "inf", "titulo": "Álex quiere salir a correr",
 "lamina": {"tarea": 1, "instr": "Su amigo Álex le ha escrito este correo.",
   "input": ["¡Hola! ¿Qué tal todo? Tengo una idea: quiero empezar a correr los domingos por la mañana en el parque del río. Solo un poco, ¡no soy deportista! ¿Quieres venir conmigo? Así es más divertido. ¿Tú haces algún deporte?", "Un abrazo,<br>Álex"],
   "lead": "Conteste a Álex. En el correo tiene que:",
   "pautas": [
    {"t": "saludar y decirle qué le parece su idea;", "p": ["saludar", "qué le parece"], "ti": ["pres"]},
    {"t": "contestar a su pregunta: qué deporte hace usted ahora y cuándo;", "p": ["qué deporte", "cuándo"], "ti": ["pres"]},
    {"t": "contarle qué deporte hacía antes y por qué lo dejó;", "p": ["qué deporte hacía", "por qué lo dejó"], "ti": ["antes", "pas"]},
    {"t": "decirle si va a ir con él el domingo y a qué hora quedan;", "p": ["sí o no", "la hora"], "ti": ["fut"]},
    {"t": "hacerle una pregunta y despedirse.", "p": ["una pregunta", "despedirse"], "ti": ["pres"]}]},
 "modelo": [
  (1, "¡Hola, Álex! Tu idea me {p:parece} genial."),
  (2, "Ahora {p:voy} a la piscina los martes y los jueves después del trabajo."),
  (3, "Antes {a:jugaba} al baloncesto en un equipo, {c:pero} {s:lo dejé} hace dos años {c:porque} {s:me cambié} de ciudad."),
  (4, "¡Claro que {f:voy a ir} contigo el domingo! ¿Quedamos a las nueve en la entrada del parque?"),
  (5, "¿{p:Tienes} zapatillas para correr? Un abrazo,"),
  (0, "Nico")]},

{"id": "a6", "tipo": "inf", "titulo": "Carla y el mercadillo del barrio",
 "lamina": {"tarea": 1, "instr": "Su amiga Carla le ha escrito este correo.",
   "input": ["¡Hola! ¿Qué tal? El domingo organizo con la asociación de vecinos un mercadillo de ropa y libros usados para ayudar al comedor del barrio. ¿Puedes ayudarnos? Necesitamos gente de diez a dos. ¿Tienes cosas que ya no usas?", "Un beso,<br>Carla"],
   "lead": "Conteste a Carla. En el correo tiene que:",
   "pautas": [
    {"t": "saludar y decirle qué le parece el mercadillo;", "p": ["saludar", "qué le parece"], "ti": ["pres"]},
    {"t": "decirle si puede ayudar el domingo y, si no puede, explicar por qué;", "p": ["sí o no", "por qué"], "ti": ["pres"]},
    {"t": "contarle qué cosas le va a llevar y cuándo;", "p": ["qué cosas", "cuándo"], "ti": ["fut"]},
    {"t": "explicarle qué hacía usted antes con la ropa vieja y qué hace ahora;", "p": ["qué hacía antes", "qué hace ahora"], "ti": ["antes", "pres"]},
    {"t": "hacerle una pregunta sobre el mercadillo y despedirse.", "p": ["una pregunta", "despedirse"], "ti": ["pres"]}]},
 "modelo": [
  (1, "¡Hola, Carla! El mercadillo me {p:parece} una idea muy bonita."),
  (2, "Lo siento, el domingo por la mañana no {p:puedo} ayudaros {c:porque} {p:trabajo} en la tienda hasta las tres."),
  (3, "{c:Pero} el sábado {f:voy a llevarte} dos bolsas con ropa y unos libros de cocina."),
  (4, "Antes {a:tiraba} la ropa vieja a la basura; ahora la {p:doy} o la {p:vendo} por internet."),
  (5, "¿A qué hora {p:termina} el mercadillo? Un beso,"),
  (0, "Ana")]},

# ====================================================================== T2 OPCION 1 · BLOG, DIARIO O REVISTA (4)
{"id": "b1", "tipo": "blog", "titulo": "Revista: «Mi primer trabajo»",
 "lamina": {"tarea": 2, "op": 1, "intro": "Una revista en español busca textos de sus lectores sobre «Mi primer trabajo». Escriba su texto. Hable de:",
   "pautas": [
    {"t": "cuál fue su primer trabajo, cuándo y dónde;", "p": ["qué trabajo", "cuándo", "dónde"], "ti": ["pas"]},
    {"t": "cómo era un día normal en ese trabajo y cómo eran sus compañeros;", "p": ["un día normal", "los compañeros"], "ti": ["antes"]},
    {"t": "algo que pasó un día y que usted recuerda bien;", "p": ["qué pasó"], "ti": ["pas"]},
    {"t": "a qué se dedica ahora y qué le gusta de su trabajo o de sus estudios;", "p": ["a qué se dedica", "qué le gusta"], "ti": ["pres"]},
    {"t": "qué trabajo le gustaría tener en el futuro y por qué.", "p": ["qué trabajo", "por qué"], "ti": ["fut"]}]},
 "modelo": [
  (1, "Mi primer trabajo {s:fue} en una tienda de discos de Bilbao, en el verano de 2010."),
  (2, "Por las mañanas {a:ordenaba} los discos y por las tardes {a:atendía} a los clientes. Mis compañeros {a:eran} muy simpáticos."),
  (3, "Un día {s:entró} un cantante famoso y yo no lo {s:reconocí}. ¡Mis compañeros {s:se rieron} muchísimo!"),
  (4, "Ahora {p:soy} enfermera en un hospital y me {p:gusta} mucho ayudar a la gente."),
  (5, "En el futuro me {f:gustaría} trabajar unos años en otro país {c:porque} {f:quiero} aprender idiomas.")]},

{"id": "b2", "tipo": "blog", "titulo": "Diario: un día en que todo salió mal",
 "lamina": {"tarea": 2, "op": 1, "intro": "Escriba una entrada en su diario sobre un día reciente en que todo salió mal. Hable de:",
   "pautas": [
    {"t": "qué día fue y qué tenía que hacer ese día;", "p": ["qué día", "qué tenía que hacer"], "ti": ["pas", "antes"]},
    {"t": "qué problemas tuvo por la mañana y por la tarde;", "p": ["por la mañana", "por la tarde"], "ti": ["pas"]},
    {"t": "cómo se sentía y qué hizo para solucionarlos;", "p": ["cómo se sentía", "qué hizo"], "ti": ["antes", "pas"]},
    {"t": "qué hace normalmente cuando tiene un mal día;", "p": ["qué hace normalmente"], "ti": ["pres"]},
    {"t": "qué va a hacer de otra manera la próxima vez.", "p": ["qué va a hacer"], "ti": ["fut"]}]},
 "modelo": [
  (1, "Querido diario: el martes {s:fue} un día horrible. {a:Tenía} una entrevista de trabajo a las diez."),
  (2, "Por la mañana el despertador no {s:sonó} y {s:perdí} el autobús. Por la tarde el móvil {s:dejó} de funcionar."),
  (3, "{a:Estaba} muy nerviosa, {c:así que} {s:llamé} a la empresa y {s:cambiamos} la hora de la entrevista."),
  (4, "Normalmente, cuando {p:tengo} un mal día, {p:llamo} a mi madre o {p:salgo} a caminar."),
  (5, "La próxima vez {f:voy a poner} dos despertadores y {f:voy a salir} antes de casa.")]},

{"id": "b3", "tipo": "blog", "titulo": "Blog: mi barrio antes y ahora",
 "lamina": {"tarea": 2, "op": 1, "intro": "Escriba una entrada en su blog sobre el barrio donde vive. Hable de:",
   "pautas": [
    {"t": "cómo se llama su barrio, dónde está y desde cuándo vive allí;", "p": ["el nombre", "dónde está", "desde cuándo"], "ti": ["pres"]},
    {"t": "cómo era el barrio cuando usted llegó;", "p": ["cómo era"], "ti": ["antes"]},
    {"t": "qué ha cambiado en los últimos años;", "p": ["qué ha cambiado"], "ti": ["pas"]},
    {"t": "qué es lo que más le gusta y lo que menos;", "p": ["lo que más", "lo que menos"], "ti": ["pres"]},
    {"t": "qué cosas nuevas va a haber en el barrio o le gustaría tener.", "p": ["cosas nuevas"], "ti": ["fut"]}]},
 "modelo": [
  (1, "¡Hola a todos! {p:Vivo} en el barrio de la Magdalena, en el centro de Zaragoza, desde 2015."),
  (2, "Cuando llegué, {a:había} pocas tiendas y las calles {a:estaban} un poco sucias."),
  (3, "En los últimos años {s:han abierto} cafeterías y una biblioteca, y {s:han plantado} muchos árboles."),
  (4, "Lo que más me {p:gusta} {p:es} el mercado; lo que menos, el ruido de los bares por la noche."),
  (5, "El año que viene {f:van a abrir} un polideportivo. ¿Y vosotros? ¿Os {p:gusta} vuestro barrio?")]},

{"id": "b4", "tipo": "blog", "titulo": "Revista: «Una costumbre de mi familia»",
 "lamina": {"tarea": 2, "op": 1, "intro": "Una revista busca textos de sus lectores sobre «Una costumbre de mi familia». Escriba su texto. Hable de:",
   "pautas": [
    {"t": "qué costumbre es y cuándo la hacen;", "p": ["qué costumbre", "cuándo"], "ti": ["pres"]},
    {"t": "quién empezó esta costumbre y cómo era cuando usted era pequeño o pequeña;", "p": ["quién empezó", "cómo era"], "ti": ["pas", "antes"]},
    {"t": "la última vez que la hicieron: cuándo fue y quién estaba;", "p": ["cuándo fue", "quién estaba"], "ti": ["pas"]},
    {"t": "qué es lo que más le gusta de esta costumbre;", "p": ["lo que más le gusta"], "ti": ["pres"]},
    {"t": "si quiere seguir con ella en el futuro y por qué.", "p": ["sí o no", "por qué"], "ti": ["fut"]}]},
 "modelo": [
  (1, "En mi familia, todos los diciembres {p:hacemos} roscos de anís en casa de mi abuela."),
  (2, "La {s:empezó} mi bisabuela. Cuando yo {a:era} pequeño, solo {a:podía} poner el azúcar."),
  (3, "La última vez {s:fue} en diciembre del año pasado: {a:estábamos} todos en la cocina y {s:hicimos} más de cien roscos."),
  (4, "Lo que más me {p:gusta} {p:es} el olor de la cocina y las historias de mi abuela."),
  (5, "Sí, {f:quiero} seguir con ella {c:porque} {f:me gustaría} hacerla con mis hijos.")]},

# ====================================================================== T2 OPCION 2 · BIOGRAFIA (4 tripticos)
{"id": "c1", "tipo": "bio", "titulo": "Julián Prieto, del fútbol al huerto",
 "lamina": {"tarea": 2, "op": 2, "intro": "Julián Prieto vive en un pueblo de Teruel. Aquí tiene algunas fotos y datos sobre su vida.",
   "photos": ["1975. Un chico de unos dieciséis años, con la camiseta de un equipo, juega al fútbol en un campo de tierra.",
              "1995. Un hombre de unos treinta y cinco años, con un silbato, entrena a un grupo de niños.",
              "Hoy. El mismo hombre, mayor y con gorra, recoge tomates en su huerto con su nieta."],
   "img": "M3_15_bio_julian_futbol_huerto",
   "rotulo": "Biografia Julian: 1 chico juega al futbol en campo de tierra, 2 entrena a ninos con silbato, 3 mayor recoge tomates con su nieta",
   "persona": "These three photos show the same Spanish man, Julián, at three ages, and he must be clearly recognisable in all of them: stocky and broad-shouldered, a square face, thick dark eyebrows, brown eyes, a slightly crooked nose and big ears (dark wavy hair when he is young, short white hair in the last photo).",
   "escenas": ["Mid-1970s look, warm slightly faded colours: Julián at about 16, in a red-and-white striped football shirt and shorts, runs with the ball on a dusty dirt football pitch of a small Spanish village, other boys around him, a small stone church tower in the distance.",
               "Mid-1990s look: Julián at about 36, in a blue tracksuit with a whistle around his neck, explains a game to a group of eight children of about nine in football kits on the same village pitch, orange cones on the ground.",
               "Today: Julián at about 66, in a cap, an old checked shirt and work trousers, picks red tomatoes in his vegetable garden next to a girl of about eight who holds a basket; tomato plants, a green hose and a small shed."],
   "ficha": ["Nació en Teruel en 1959.", "De joven: muy deportista; juega en el equipo de su pueblo.", "1980: deja el fútbol; empieza a trabajar en una fábrica de muebles.", "1990-2020: entrena a los niños del pueblo los fines de semana.", "2021: se jubila.", "Hoy: tiene un huerto; su nieta lo ayuda los sábados."],
   "intro2": "Escriba un texto sobre Julián. Hable de:",
   "pautas": [
    {"t": "dónde y cuándo nació y cómo era de joven;", "p": ["dónde", "cuándo", "cómo era"], "ti": ["pas", "antes"]},
    {"t": "a qué se dedicó y qué hacía los fines de semana;", "p": ["a qué se dedicó", "los fines de semana"], "ti": ["pas", "antes"]},
    {"t": "qué hace ahora y por qué cree usted que dejó el fútbol en 1980.", "p": ["qué hace ahora", "por qué cree que lo dejó"], "ti": ["pres", "pas"]}]},
 "modelo": [
  (1, "Julián Prieto {s:nació} en Teruel en 1959. De joven {a:era} muy deportista y {a:jugaba} al fútbol en el equipo de su pueblo."),
  (2, "En 1980 {s:empezó} a trabajar en una fábrica de muebles. {c:Además}, los fines de semana {a:entrenaba} a los niños del pueblo."),
  (3, "Ahora {p:está} jubilado y {p:tiene} un huerto, donde su nieta lo {p:ayuda} los sábados. {p:Creo} que {s:dejó} el fútbol {c:porque} {a:necesitaba} trabajar y ya no {a:tenía} tiempo para entrenar.")]},

{"id": "c2", "tipo": "bio", "titulo": "Nuria Vidal, enfermera",
 "lamina": {"tarea": 2, "op": 2, "intro": "Nuria Vidal es enfermera. Aquí tiene algunas fotos y datos sobre su vida.",
   "photos": ["Una niña de unos ocho años juega a ser enfermera: le pone una venda a su muñeca.",
              "Una mujer joven, con ropa de enfermera, vacuna a un niño en un centro de salud pequeño de un pueblo de Perú.",
              "La misma mujer, hoy, con el pelo corto y gris, da una clase a estudiantes de Enfermería."],
   "img": "M3_16_bio_nuria_enfermera",
   "rotulo": "Biografia Nuria enfermera: 1 nina pone una venda a su muneca, 2 joven vacuna a un nino en Peru, 3 mayor da clase a estudiantes",
   "persona": "These three photos show the same Spanish woman, Nuria, at three ages, and she must be clearly recognisable in all of them: slim, a long oval face, green eyes, a small gap between her front teeth and a few freckles on her nose (straight light brown hair when she is young, short grey hair in the last photo).",
   "escenas": ["1970s look, warm slightly faded colours: Nuria at about 8, in a home-made white apron, sits on the floor of a family living room putting a bandage on the arm of her doll, very concentrated; a sofa and toys around her.",
               "Late 1990s look: Nuria at about 27, in a light blue nurse uniform, gives a vaccine to a small boy sitting on his mother's lap in a simple rural health post in the Andes of Peru; a wooden table with medical boxes and plain posters with no readable text.",
               "Today: Nuria at about 55, with short grey hair, glasses on a cord and a white coat, shows a group of five nursing students of about 20 how to take blood pressure on a classmate in a university practice room."],
   "ficha": ["Nació en Lleida en 1970.", "De niña: le encanta cuidar a la gente; quiere ser enfermera.", "1992: termina sus estudios de Enfermería.", "1994-2001: trabaja en un centro de salud de Perú; aprende quechua.", "2002: vuelve a España.", "Hoy: es profesora en la universidad; viaja a Perú todos los veranos."],
   "intro2": "Escriba un texto sobre Nuria. Hable de:",
   "pautas": [
    {"t": "dónde y cuándo nació y qué le gustaba de niña;", "p": ["dónde", "cuándo", "qué le gustaba"], "ti": ["pas", "antes"]},
    {"t": "dónde trabajó después de sus estudios y cómo era su vida allí;", "p": ["dónde trabajó", "cómo era su vida"], "ti": ["pas", "antes"]},
    {"t": "qué hace ahora y por qué cree usted que todavía viaja a Perú.", "p": ["qué hace ahora", "por qué cree que viaja"], "ti": ["pres"]}]},
 "modelo": [
  (1, "Nuria Vidal {s:nació} en Lleida en 1970. De niña le {a:encantaba} cuidar a la gente y ya {a:quería} ser enfermera."),
  (2, "En 1992 {s:terminó} sus estudios y dos años después {s:se fue} a Perú. Allí {a:trabajaba} en un centro de salud pequeño, en las montañas, y {s:aprendió} quechua."),
  (3, "Ahora {p:es} profesora de Enfermería en la universidad. {p:Creo} que todavía {p:viaja} a Perú {c:porque} {p:tiene} amigos allí y le {p:gusta} mucho el país.")]},

{"id": "c3", "tipo": "bio", "titulo": "Pilar y Ramón, una vida bailando",
 "lamina": {"tarea": 2, "op": 2, "intro": "Pilar y Ramón están juntos desde hace casi cincuenta años. Aquí tiene algunas fotos y datos sobre su vida.",
   "photos": ["1976. Una chica y un chico de unos veinte años bailan de noche en las fiestas de un pueblo, con luces de colores.",
              "1990. Los dos, de unos treinta y cinco años, enseñan a bailar a varias parejas en una sala con espejos.",
              "Hoy. Los dos, ya mayores, bailan en el salón de su casa con su nieto pequeño."],
   "img": "M3_17_bio_pilar_ramon_baile",
   "rotulo": "Biografia Pilar y Ramon: 1 jovenes bailan en las fiestas con luces, 2 ensenan a bailar en sala con espejos, 3 mayores bailan con su nieto",
   "persona": "The same couple appears in the three photos at three ages and both must be clearly recognisable in all of them: Pilar, small and slim, with big dark eyes, a round face and curly black hair (short curly white hair in the last photo); Ramón, tall, with a long face, a thick moustache (black when young, white later) and big hands.",
   "escenas": ["Late 1970s look, warm slightly faded colours, at night: Pilar and Ramón at about 20, she in a flowered summer dress and he in a white shirt, dance together in the square of a small Spanish coastal town during the local festival, strings of coloured light bulbs above them and other couples dancing around.",
               "1990s look: Pilar and Ramón at about 35, in comfortable dance clothes, show a step to four couples in a dance studio with a wooden floor and a long wall mirror; Ramón counts the beat with his hand.",
               "Today: Pilar and Ramón at about 70 dance slowly in the living room of their flat, holding the hands of their grandson of about five, who dances between them; a sofa, family photos on a shelf and an old radio."],
   "ficha": ["1976: se conocen en las fiestas de Benicàssim.", "Entonces: ella es peluquera; él, conductor de autobús.", "1979: se casan.", "1988: abren una escuela de baile en Castellón.", "2018: cierran la escuela.", "Hoy: bailan todos los domingos con sus nietos."],
   "intro2": "Escriba un texto sobre Pilar y Ramón. Hable de:",
   "pautas": [
    {"t": "cómo y cuándo se conocieron y a qué se dedicaban entonces;", "p": ["cómo y cuándo", "a qué se dedicaban"], "ti": ["pas", "antes"]},
    {"t": "qué hicieron después y cómo era su escuela;", "p": ["qué hicieron", "cómo era la escuela"], "ti": ["pas", "antes"]},
    {"t": "cómo es su vida ahora y por qué cree usted que cerraron la escuela.", "p": ["cómo es su vida", "por qué cree que la cerraron"], "ti": ["pres", "pas"]}]},
 "modelo": [
  (1, "Pilar y Ramón {s:se conocieron} en 1976, en las fiestas de Benicàssim. Entonces ella {a:era} peluquera y él {a:conducía} un autobús."),
  (2, "{s:Se casaron} en 1979 y en 1988 {s:abrieron} una escuela de baile en Castellón. La escuela {a:tenía} una sala grande con espejos y siempre {a:estaba} llena de alumnos."),
  (3, "Ahora {p:están} jubilados y {p:bailan} con sus nietos todos los domingos. {p:Creo} que {s:cerraron} la escuela {c:porque} {a:estaban} cansados y {a:querían} descansar.")]},

{"id": "c4", "tipo": "bio", "titulo": "Karim Haddad y su taller de bicis",
 "lamina": {"tarea": 2, "op": 2, "intro": "Karim Haddad tiene un taller de bicicletas en Valencia. Aquí tiene algunas fotos y datos sobre su vida.",
   "photos": ["Un niño de unos doce años arregla una bicicleta vieja delante de su casa, en un pueblo de Marruecos.",
              "Un hombre joven trabaja en un campo de naranjos; lleva una caja llena de naranjas.",
              "El mismo hombre, hoy, con barba gris, arregla una bici en su taller y habla con una clienta."],
   "img": "M3_18_bio_karim_taller_bicis",
   "rotulo": "Biografia Karim: 1 nino arregla una bici en Marruecos, 2 joven lleva una caja de naranjas, 3 adulto arregla una bici en su taller",
   "persona": "These three photos show the same Moroccan man, Karim, at three ages, and he must be clearly recognisable in all of them: thin, a narrow face, dark brown eyes with thick eyelashes, a small scar on his left eyebrow and short curly black hair (with a short grey beard in the last photo).",
   "escenas": ["1990s look, warm slightly faded colours: Karim at about 12, in a T-shirt and old trousers, squats in front of a simple white house in a Moroccan village, fixing the chain of an old bicycle turned upside down, his hands dirty with grease; a friend of the same age watches.",
               "Early 2000s look: Karim at about 21, in a cap, a long-sleeved shirt and work gloves, carries a plastic box full of oranges between rows of orange trees in a field near Valencia; other workers in the background.",
               "Today: Karim at about 44, with a short grey beard and a dark blue work apron, repairs a bicycle on a stand in his small bike workshop while he talks with a woman customer of about 30 who holds a helmet; tools on the wall and tyres hanging from the ceiling."],
   "ficha": ["Nació cerca de Fez (Marruecos) en 1981.", "De niño: le encantan las bicis; arregla las de sus amigos.", "2001: llega a Valencia; trabaja en el campo, en la recogida de la naranja.", "2001-2008: estudia español por las noches.", "2009: abre un taller de bicicletas.", "Hoy: tiene dos empleados; da clases de mecánica a jóvenes."],
   "intro2": "Escriba un texto sobre Karim. Hable de:",
   "pautas": [
    {"t": "dónde nació y qué le gustaba hacer de niño;", "p": ["dónde", "qué le gustaba"], "ti": ["pas", "antes"]},
    {"t": "cómo fue su vida cuando llegó a Valencia;", "p": ["cómo fue su vida"], "ti": ["pas", "antes"]},
    {"t": "qué hace ahora y por qué cree usted que da clases a jóvenes.", "p": ["qué hace ahora", "por qué cree que da clases"], "ti": ["pres"]}]},
 "modelo": [
  (1, "Karim Haddad {s:nació} en 1981 en un pueblo cerca de Fez, en Marruecos. De niño le {a:encantaban} las bicis y {a:arreglaba} las de sus amigos."),
  (2, "En 2001 {s:llegó} a Valencia con veinte años. Al principio {a:trabajaba} en el campo, recogiendo naranjas, y por las noches {a:estudiaba} español."),
  (3, "En 2009 {s:abrió} su taller y ahora {p:tiene} dos empleados. {p:Creo} que {p:da} clases a jóvenes {c:porque} {p:recuerda} sus primeros años y {p:quiere} ayudarlos a encontrar trabajo.")]},

# ====================================================================== T2 OPCION 2 · UN DIA CON FOTOS (4 tripticos)
{"id": "d1", "tipo": "dia", "titulo": "La fiesta sorpresa de mamá",
 "lamina": {"tarea": 2, "op": 2, "intro": "El mes pasado usted organizó con sus hermanos una fiesta sorpresa por la jubilación de su madre. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la mañana. Usted y su hermano ponen globos y una guirnalda en el salón de su hermana.",
              "Por la tarde. Su madre abre la puerta y ve a toda la familia; se pone las manos en la cara.",
              "Por la noche. Su madre abre su regalo: es una bicicleta con un lazo rojo."],
   "img": "M3_19_dia_fiesta_sorpresa_madre",
   "rotulo": "Fiesta sorpresa por la jubilacion: 1 ponen globos en el salon, 2 la madre abre la puerta sorprendida, 3 abre el regalo una bici",
   "persona": "The same main people appear in the three photos and must look identical in each one: a Spanish woman of about 40 with a dark ponytail, a green jumper and jeans; her brother, about 45, bald, with glasses and a striped shirt; and their mother, about 65, small, with short dyed red hair and a beige cardigan.",
   "escenas": ["Morning in an ordinary Spanish living room: the woman stands on a chair tying colourful balloons to a ceiling lamp while her brother sticks a long paper garland with coloured stars (no letters) on the wall; bags of balloons on the sofa.",
               "Afternoon in the same living room, now full of balloons: the mother has just come through the front door and puts her hands on her cheeks, surprised and laughing, while about ten relatives of different ages, including the woman and her brother, clap.",
               "Evening in the same room: the mother laughs as she pulls the wrapping paper off a new city bicycle with a big red bow, while her children and two grandchildren watch; plates with cake on the table."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": [
    {"t": "por qué organizaron la fiesta, dónde y qué hicieron por la mañana;", "p": ["por qué", "dónde", "qué hicieron por la mañana"], "ti": ["pas"]},
    {"t": "qué pasó cuando llegó su madre y cómo estaba ella;", "p": ["qué pasó", "cómo estaba"], "ti": ["pas", "antes"]},
    {"t": "qué le regalaron y qué cree usted que va a hacer su madre ahora.", "p": ["qué le regalaron", "qué va a hacer"], "ti": ["pas", "fut"]}]},
 "modelo": [
  (1, "El mes pasado mi madre {s:se jubiló} y mis hermanos y yo le {s:preparamos} una fiesta sorpresa en casa de mi hermana. Por la mañana {s:pusimos} globos en el salón."),
  (2, "Por la tarde, cuando mi madre {s:abrió} la puerta, todos {s:gritamos}: «¡Sorpresa!». Ella {a:estaba} muy emocionada y no {a:podía} hablar."),
  (3, "Por la noche le {s:dimos} nuestro regalo: una bicicleta. {p:Creo} que ahora {f:va a pasear} por el río todas las mañanas.")]},

{"id": "d2", "tipo": "dia", "titulo": "El sábado que pintamos el piso",
 "lamina": {"tarea": 2, "op": 2, "intro": "El sábado pasado usted pintó el salón de su piso con dos amigos. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la mañana. Usted y sus amigos tapan los muebles con plásticos; hay botes de pintura en el suelo.",
              "A mediodía. A un amigo se le cae un bote de pintura azul en los pies; todos se ríen.",
              "Por la noche. El salón ya está azul; ustedes brindan con limonada en el balcón."],
   "img": "M3_20_dia_pintar_piso_amigos",
   "rotulo": "Pintar el piso con amigos: 1 tapan los muebles con plasticos, 2 a un amigo se le cae la pintura azul, 3 brindan en el balcon",
   "persona": "The same three friends appear in the three photos and must look identical in each one: a woman of about 30 with short blond hair and a big old T-shirt; Marcos, about 32, tall, with a black beard and a red cap; and Ana, about 29, with long brown braids and denim dungarees.",
   "escenas": ["Morning in the small living room of a flat with white walls: the three friends cover a sofa and a table with plastic sheets; open tins of blue paint, rollers and a stepladder on a floor covered with old newspapers (no readable text).",
               "Midday in the same room, one wall already blue: a tin of blue paint has just fallen on Marcos's feet and his trainers are covered in blue paint; the two women laugh with their hands over their mouths, rollers in their hands.",
               "Evening: the living room behind them is now blue and tidy; the three friends, tired and with paint on their clothes, toast with glasses of lemonade on the small balcony of the flat, city roofs in the background."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": [
    {"t": "por qué pintaron el salón, con quién y qué hicieron primero;", "p": ["por qué", "con quién", "qué hicieron primero"], "ti": ["pas"]},
    {"t": "qué pasó a mediodía y qué hicieron todos;", "p": ["qué pasó", "qué hicieron"], "ti": ["pas"]},
    {"t": "cómo era el salón antes, cómo es ahora y qué más va a cambiar en su casa.", "p": ["cómo era antes", "cómo es ahora", "qué más va a cambiar"], "ti": ["antes", "pres", "fut"]}]},
 "modelo": [
  (1, "El sábado pasado {s:pinté} el salón de mi piso con Marcos y Ana {c:porque} las paredes {a:estaban} muy sucias. Primero {s:tapamos} todos los muebles con plásticos."),
  (2, "A mediodía, a Marcos {s:se le cayó} un bote de pintura azul en los pies. ¡Todos {s:nos reímos} muchísimo, también Marcos!"),
  (3, "Antes el salón {a:era} blanco y un poco triste; ahora {p:es} azul y muy alegre. El mes que viene {f:voy a cambiar} las cortinas del salón.")]},

{"id": "d3", "tipo": "dia", "titulo": "Voluntaria en la carrera popular",
 "lamina": {"tarea": 2, "op": 2, "intro": "El domingo pasado usted fue voluntario o voluntaria en una carrera popular de su ciudad. Aquí tiene tres fotos de ese día.",
   "photos": ["Muy temprano. Usted, con la camiseta amarilla de los voluntarios, pone botellas de agua y plátanos en unas mesas.",
              "A mediodía. Pasan los corredores y usted les da agua. Una corredora mayor le choca la mano.",
              "Por la tarde. Los voluntarios, cansados, comen bocadillos sentados en el césped y se ríen."],
   "img": "M3_21_dia_voluntaria_carrera",
   "rotulo": "Voluntaria en la carrera popular: 1 pone agua y platanos en las mesas, 2 una corredora mayor le choca la mano, 3 comen en el cesped",
   "persona": "The same main person appears in the three photos and must look identical in each one: a Latin American woman of about 35, with long black hair in a ponytail, a yellow volunteer T-shirt, black leggings and a white cap. The other volunteers also wear yellow T-shirts.",
   "escenas": ["Early morning in a city street closed to traffic: the woman and two other volunteers put bottles of water and bunches of bananas on long folding tables; cardboard boxes on the ground and plain banners with no readable text.",
               "Midday at the same tables: runners with plain number bibs (no readable text) pass by; the woman holds out a bottle of water and an energetic woman runner of about 70, with short white hair, gives her a high five as she passes.",
               "Afternoon in a city park: the woman and five other volunteers in yellow T-shirts, tired, sit on the grass eating sandwiches and laughing; caps and empty boxes on the grass around them."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": [
    {"t": "por qué fue voluntario o voluntaria, a qué hora empezó y qué tenía que hacer;", "p": ["por qué", "a qué hora", "qué tenía que hacer"], "ti": ["pas", "antes"]},
    {"t": "qué pasó cuando llegaron los corredores;", "p": ["qué pasó"], "ti": ["pas"]},
    {"t": "cómo terminó el día, cómo se sentía y si quiere repetir el año que viene.", "p": ["cómo terminó", "cómo se sentía", "si quiere repetir"], "ti": ["pas", "antes", "fut"]}]},
 "modelo": [
  (1, "El domingo pasado {s:fui} voluntaria en la carrera de mi ciudad {c:porque} mi hermana {a:corría}. {s:Empecé} a las siete: {a:tenía} que preparar las mesas del agua."),
  (2, "A mediodía {s:llegaron} los corredores y les {s:dimos} agua y plátanos. Una señora de setenta años me {s:chocó} la mano. ¡Qué energía!"),
  (3, "Por la tarde {s:comimos} todos juntos en el parque. {a:Estaba} cansada, {c:pero} muy contenta, y el año que viene {f:voy a repetir}.")]},

{"id": "d4", "tipo": "dia", "titulo": "La excursión en bici y el tractor",
 "lamina": {"tarea": 2, "op": 2, "intro": "El verano pasado usted hizo una excursión en bici con su familia. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la mañana. Usted, su pareja y sus dos hijos van en bici por un camino entre campos de girasoles.",
              "A mediodía. La bici de su hijo tiene una rueda pinchada; ustedes la miran sentados en el suelo.",
              "Por la tarde. Un agricultor lleva a la familia y las bicis en el remolque de su tractor."],
   "img": "M3_22_dia_excursion_bici_tractor",
   "rotulo": "Excursion en bici con la familia: 1 van en bici entre girasoles, 2 rueda pinchada sentados en el suelo, 3 vuelven en un tractor",
   "persona": "The same family appears in the three photos and must look identical in each one: a man of about 40 with short grey hair and a blue T-shirt, his partner, a woman of about 38 with red curly hair and a green T-shirt, and their two children, a boy of about 10 with glasses and a girl of about 7 with two plaits; they all wear bike helmets.",
   "escenas": ["Summer morning on a dirt track between big fields of sunflowers in the Spanish countryside: the four ride their bicycles in a line, the girl's bike has a small basket; blue sky with a few clouds.",
               "Midday on the same track: the four sit on the dry ground next to the boy's bike, which has a flat back tyre; the father looks at the tyre and the boy looks worried; water bottles on the ground.",
               "Afternoon on a country road: the four sit in the open trailer of an old green tractor with their bicycles, while an older farmer in a straw hat drives; the children wave at a field, sunflowers behind."],
   "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": [
    {"t": "adónde fueron, qué tiempo hacía y cómo era el camino;", "p": ["adónde", "qué tiempo hacía", "cómo era el camino"], "ti": ["pas", "antes"]},
    {"t": "qué problema tuvieron a mediodía y qué hicieron;", "p": ["qué problema", "qué hicieron"], "ti": ["pas"]},
    {"t": "cómo volvieron a casa, qué le pareció el día y qué excursión quiere hacer la próxima vez.", "p": ["cómo volvieron", "qué le pareció", "la próxima excursión"], "ti": ["pas", "fut"]}]},
 "modelo": [
  (1, "En agosto {s:hicimos} una excursión en bici cerca de mi pueblo. {a:Hacía} mucho calor y el camino {a:era} muy bonito, con girasoles por todas partes."),
  (2, "A mediodía la bici de mi hijo {s:tuvo} un pinchazo y no {a:teníamos} nada para arreglarla. ¡Qué mala suerte!"),
  (3, "{c:Por suerte}, un agricultor nos {s:llevó} al pueblo en su tractor. {s:Fue} un día muy divertido. La próxima vez {f:vamos a ir} al lago, ¡sin pinchazos!")]},

# ====================================================================== T1 · CORREO DE USTED, POR SI ACASO (2)
{"id": "u1", "tipo": "for", "titulo": "La profesora de pilates cambia el horario", "porsiacaso": True,
 "lamina": {"tarea": 1, "instr": "Usted va a clases de pilates en el centro cultural de su barrio. Su profesora, Isabel Gómez, le ha escrito este correo.",
   "input": ["Estimados alumnos: a partir de noviembre las clases de los lunes y los miércoles van a ser a las siete de la tarde, no a las seis. Si alguien no puede venir a esa hora, escríbame. Hay plazas en el grupo de los sábados.", "Un saludo,<br>Isabel Gómez"],
   "lead": "Conteste a Isabel Gómez. En el correo tiene que:",
   "pautas": [
    {"t": "saludar;", "p": ["saludo"], "ti": []},
    {"t": "decirle si va a poder ir a la nueva hora y por qué;", "p": ["sí o no", "por qué"], "ti": ["fut"]},
    {"t": "contarle cuándo empezó sus clases y qué le parecen;", "p": ["cuándo empezó", "qué le parecen"], "ti": ["pas", "pres"]},
    {"t": "preguntarle por el grupo de los sábados: la hora y el número de alumnos;", "p": ["la hora", "el número de alumnos"], "ti": ["pres"]},
    {"t": "agradecerle la información y despedirse.", "p": ["agradecer", "despedirse"], "ti": []}]},
 "modelo": [
  (1, "Estimada Isabel:"),
  (2, "Lo siento mucho, {c:pero} en noviembre no {f:voy a poder} ir a las siete {c:porque} {p:salgo} del trabajo a las siete y media."),
  (3, "{s:Empecé} sus clases hace dos años y me {p:gustan} mucho: ahora {p:duermo} mejor y {p:tengo} más energía."),
  (4, "¿A qué hora {p:es} la clase de los sábados? ¿Cuántos alumnos {p:hay} en ese grupo?"),
  (5, "Muchas gracias por la información. Un saludo,"),
  (0, "Julia Martín")]},

{"id": "u2", "tipo": "for", "titulo": "Una reserva en la casa rural", "porsiacaso": True,
 "lamina": {"tarea": 1, "instr": "Usted ha reservado dos noches en una casa rural y ha recibido este correo.",
   "input": ["Estimado cliente: muchas gracias por su reserva en Casa Las Encinas para las noches del 14 y el 15 de marzo. ¿A qué hora piensa llegar? La cena no está incluida, pero podemos prepararla por quince euros por persona. ¿Necesita algo más?", "Atentamente,<br>Pilar Rubio"],
   "lead": "Conteste a Pilar Rubio. En el correo tiene que:",
   "pautas": [
    {"t": "saludar y confirmar la reserva;", "p": ["saludar", "confirmar"], "ti": ["pres"]},
    {"t": "decir a qué hora va a llegar y con quién va a ir;", "p": ["la hora", "con quién"], "ti": ["fut"]},
    {"t": "contestar si quiere la cena y explicar por qué;", "p": ["sí o no", "por qué"], "ti": ["pres"]},
    {"t": "contar cómo conoció la casa rural;", "p": ["cómo la conoció"], "ti": ["pas"]},
    {"t": "hacer una pregunta sobre la zona, agradecer y despedirse.", "p": ["una pregunta", "agradecer", "despedirse"], "ti": ["pres"]}]},
 "modelo": [
  (1, "Buenos días, señora Rubio: le {p:confirmo} la reserva para el catorce y el quince de marzo."),
  (2, "{f:Vamos a llegar} el viernes sobre las siete de la tarde. {f:Voy a ir} con mi marido."),
  (3, "Sí, {p:queremos} la cena del viernes {c:porque} {p:llegamos} cansados del viaje."),
  (4, "{s:Conocí} su casa por una amiga: {s:estuvo} allí el verano pasado."),
  (5, "¿{p:Hay} rutas para caminar cerca? Muchas gracias por todo. Un saludo,"),
  (0, "Teresa Gil")]},
]
