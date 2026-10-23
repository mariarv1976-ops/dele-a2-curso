# -*- coding: utf-8 -*-
# BANCO DE TEMAS DE LA TAREA 1 DE LA ORAL: MONOLOGO (curso de preparacion DELE A2, Modulo 4)
# Lo usa build_M4_T1_temas.py. Para ANADIR UN TEMA: copia un bloque de TEMAS, cambia el id
# (siguiente numero), el titulo, el area, la lamina (intro + 5 pautas), las notas y el monologo
# modelo, y vuelve a ejecutar el build.
#
# Las laminas son ORIGINALES: los temas son los de las laminas oficiales y los mas frecuentes,
# pero las pautas estan redactadas por nosotras (mismo formato: 5 pautas que mezclan tiempos).
#
# Cada pauta lleva:
#   "t"     -> los tiempos que pide: "pres" (presente), "pas" (lo que paso: fui, he ido),
#              "antes" (como era antes: era, tenia, iba) y "fut" (planes: voy a, me gustaria)
#   "clave" -> las palabras de la pauta que dicen el tiempo (sale en la practica de los tiempos)
# En el monologo modelo, los verbos se marcan asi: {p:vivo} {s:fui} {a:era} {f:voy a ir}
#   p = presente · s = pasado (indefinido o perfecto) · a = antes (imperfecto) · f = futuro y planes
# Unas 270-300 palabras por monologo = unos 2 minutos y medio hablando con calma.

# ------------------------------------------------------------ LOS TIEMPOS
TIEMPOS = {
 "pres":  {"nombre": "Presente", "que": "Cómo es ahora, qué haces normalmente, qué te gusta",
           "claves": ["quién es", "cómo es", "a qué se dedica", "qué hace normalmente", "por qué le gusta", "cuándo, cuánto tiempo al día"],
           "formas": ["es", "vivo", "trabajo", "me gusta", "suelo", "normalmente"]},
 "pas":   {"nombre": "Pasado", "que": "Lo que pasó: una vez, un día concreto, una historia",
           "claves": ["cuándo fue", "qué hizo", "la última vez", "alguna vez", "una historia que le pasó", "cómo lo conoció"],
           "formas": ["fui", "conocí", "comí", "me regaló", "he estado", "ha sido"]},
 "antes": {"nombre": "Antes (y ahora)", "que": "Cómo era antes, qué hacías de niño o hace años",
           "claves": ["cómo era antes", "cuando era pequeño", "antes y ahora", "ha cambiado", "qué hacía"],
           "formas": ["era", "tenía", "vivía", "iba", "jugaba", "había"]},
 "fut":   {"nombre": "Futuro y planes", "que": "Lo que vas a hacer o te gustaría hacer",
           "claves": ["en el futuro", "próximo / próximas", "le gustaría", "va a", "algún día", "planes"],
           "formas": ["voy a ir", "vamos a hacer", "me gustaría", "quiero", "pienso", "el año que viene"]},
}
ORDEN_TIEMPOS = ["pres", "pas", "antes", "fut"]

# Frases para cada parte del monologo
ABRIR = ["Voy a hablar de...", "Hoy quiero hablar de...", "El tema que he elegido es...", "Bueno, pues voy a hablar de..."]
PASAR = ["Primero...", "Ahora voy a hablar de...", "Sobre... (la segunda pregunta)...", "Además...", "Otra cosa importante es...", "Y una historia: una vez..."]
CERRAR = ["Por eso, para mí... es muy importante.", "En resumen, ...", "Y eso es todo. Para mí, ... es...", "Bueno, pues esto es todo sobre..."]
UNIR = ["y", "pero", "porque", "por eso", "además", "también", "cuando", "después", "al final", "por ejemplo"]
PUENTES_TIEMPO = {
 "pres":  ["Normalmente...", "Ahora...", "Todos los días / los fines de semana..."],
 "pas":   ["Una vez...", "El año pasado...", "La última vez fue...", "Este año he..."],
 "antes": ["Antes..., pero ahora...", "Cuando era pequeño/a...", "Hace diez años..."],
 "fut":   ["El año que viene voy a...", "En el futuro me gustaría...", "Algún día quiero..."],
}

# Si la lamina pregunta algo que no has vivido
INVENTAR = ("Si no tienes una red social favorita o no recuerdas un curso, invéntalo. El examinador no comprueba si es verdad: "
            "valora que respondas a las pautas con los tiempos correctos. Es mejor una historia inventada y clara que decir «no sé».")

# ------------------------------------------------------------ PREPARACION (los 4 minutos de la tarea 1)
PASOS_T1 = [
 ("0:00", "Elige el tema", "Lee los dos temas y elige el que te da más ideas, no el más fácil de escribir. 20 segundos."),
 ("0:20", "Dibuja el esquema", "Cinco casillas, una por pauta, en el mismo orden. Arriba de cada casilla, el tiempo que pide: presente, pasado, antes o futuro."),
 ("0:40", "Rellena las casillas", "Palabras clave: nombres, lugares, fechas, números. En cada casilla, escribe UN verbo ya en su tiempo (fui, era, voy a): es tu ancla para no equivocarte."),
 ("3:20", "Marca el principio y el final", "Una palabra para empezar (el tema) y otra para terminar (tu opinión). Repasa: ¿tienen algo las cinco casillas?"),
]
REGLAS_NOTAS_T1 = [
 "Palabras clave, no frases: <i>conocí 2010 · universidad · curso inglés</i>, no <i>\"La conocí en el año 2010 en la universidad...\"</i>.",
 "En cada casilla, un verbo ya conjugado en el tiempo que pide la pauta: <b>fui</b>, <b>era</b>, <b>voy a</b>. Si lo escribes bien en la hoja, lo dices bien en la sala.",
 "Puedes mirar tus notas, pero no leerlas. Un monólogo leído o aprendido de memoria se nota y baja la nota.",
 "Números, nombres y lugares ayudan mucho: son detalles fáciles de decir y alargan cada respuesta.",
 "Escribe con letra grande y deja espacio entre las casillas: en la sala miras la hoja solo un segundo.",
]

# ------------------------------------------------------------ TEMAS
TEMAS = [
 {"id": 1, "titulo": "Una persona importante en mi vida", "area": "A1", "fuente": "oficial",
  "intro": "Hable de una persona importante en su vida (un amigo, alguien de su familia, un compañero de trabajo...). Hable de:",
  "pautas": [
   {"txt": "quién es, cómo es y a qué se dedica;", "t": ["pres"], "clave": "quién es · cómo es · a qué se dedica"},
   {"txt": "por qué es importante para usted;", "t": ["pres"], "clave": "por qué es importante"},
   {"txt": "cuándo y cómo la conoció;", "t": ["pas"], "clave": "cuándo · la conoció"},
   {"txt": "cómo era su relación al principio y cómo es ahora;", "t": ["antes", "pres"], "clave": "cómo era al principio · cómo es ahora"},
   {"txt": "qué le gustaría hacer con esta persona en el futuro.", "t": ["fut"], "clave": "le gustaría · en el futuro"}],
  "notas": ["Lucía · amiga · enfermera · Valencia | alta, divertida, paciente",
            "me ayuda siempre · mudanza · perdí trabajo → confío",
            "conocí 2010 · universidad · curso inglés · me dejó apuntes → café",
            "antes: tímida, nos veíamos poco | ahora: teléfono cada semana, domingos",
            "vamos a ir a Lisboa · verano | me gustaría: Camino de Santiago"],
  "abre": "Voy a hablar de una persona muy importante en mi vida: mi amiga Lucía.",
  "mod": [
   "Lucía {p:es} enfermera y {p:trabaja} en un hospital de Valencia. {p:Tiene} cuarenta años, como yo. {p:Es} alta, morena y muy divertida, pero también {p:es} muy paciente: casi nunca {p:se enfada}. {p:Vive} con su pareja y dos gatos en un piso cerca de la playa.",
   "{p:Es} importante para mí porque siempre me {p:ayuda}. Cuando {p:tengo} un problema, la {p:llamo} a ella primero. Por ejemplo, el año pasado me {s:ayudó} mucho con mi mudanza, y también cuando {s:perdí} mi trabajo. {p:Confío} en ella totalmente y ella {p:confía} en mí.",
   "La {s:conocí} en el año 2010, en la universidad. Las dos {s:hicimos} un curso de inglés por las tardes. El primer día yo {s:llegué} tarde y no {a:tenía} los apuntes, y ella me {s:dejó} los suyos. Después de la clase {s:fuimos} a tomar un café y {s:hablamos} durante dos horas.",
   "Al principio no {a:éramos} muy amigas: yo {a:era} muy tímida y solo {a:nos veíamos} en clase. Pero ahora todo {p:es} diferente. {p:Hablamos} por teléfono todas las semanas y {p:comemos} juntas casi todos los domingos. Para mí {p:es} casi como una hermana.",
   "Este verano {f:vamos a hacer} un viaje juntas a Lisboa para celebrar su cumpleaños; ya {s:hemos reservado} el hotel. Y algún día me {f:gustaría} hacer con ella el Camino de Santiago, andando, pero todavía no {p:tenemos} fecha, porque ella {p:trabaja} mucho."],
  "cierra": "Por eso, para mí, Lucía {p:es} una persona muy especial."},

 {"id": 2, "titulo": "Una persona de mi familia", "area": "A1", "fuente": "oficial",
  "intro": "Hable de una persona de su familia (su madre, su padre, un hermano, su pareja, un abuelo...). Hable de:",
  "pautas": [
   {"txt": "quién es, cómo es físicamente y de carácter, y a qué se dedica;", "t": ["pres"], "clave": "quién es · cómo es · a qué se dedica"},
   {"txt": "por qué ha elegido a esta persona;", "t": ["pres", "pas"], "clave": "por qué ha elegido"},
   {"txt": "cómo era su relación con ella cuando usted era pequeño y cómo es ahora;", "t": ["antes", "pres"], "clave": "cómo era · cuando era pequeño · cómo es ahora"},
   {"txt": "algo especial que hicieron juntos una vez;", "t": ["pas"], "clave": "hicieron · una vez"},
   {"txt": "cuándo va a verla la próxima vez y qué van a hacer.", "t": ["fut"], "clave": "va a verla · la próxima vez"}],
  "notas": ["abuelo Paco · 82 · bajo, bigote blanco | tranquilo, gracioso · jubilado, era panadero",
            "he elegido: me enseñó muchas cosas · cocinar, bici",
            "antes: vivía con nosotros · me llevaba al cole | ahora: pueblo · llamo domingos",
            "una vez · 12 años · fuimos a pescar · río · no pescamos nada → tormenta",
            "voy a ir · Navidad · vamos a hacer pan juntos"],
  "abre": "Hoy quiero hablar de una persona de mi familia: mi abuelo Paco.",
  "mod": [
   "Mi abuelo {p:se llama} Paco y {p:tiene} ochenta y dos años. {p:Es} bajo, delgado y {p:tiene} un bigote blanco muy grande. De carácter {p:es} tranquilo y muy gracioso: siempre {p:cuenta} chistes. Ahora {p:está} jubilado, pero durante cuarenta años {s:fue} panadero en su pueblo, en Teruel.",
   "Lo {s:he elegido} porque {p:es} la persona de mi familia que más cosas me {s:ha enseñado}. Con él {s:aprendí} a montar en bici, a cocinar y a hacer pan. Además, {p:es} la persona que mejor me {p:escucha}: nunca me {p:dice} «eso es una tontería».",
   "Cuando yo {a:era} pequeño, mi abuelo {a:vivía} con nosotros en Zaragoza. Todas las mañanas me {a:llevaba} al colegio y por la tarde {a:jugábamos} a las cartas. Ahora él {p:vive} otra vez en el pueblo y yo {p:trabajo} en Barcelona, así que lo {p:llamo} todos los domingos. {p:Hablamos} menos, pero {p:seguimos} muy unidos.",
   "Una vez, cuando yo {a:tenía} doce años, {s:fuimos} a pescar los dos solos a un río cerca del pueblo. {s:Estuvimos} allí toda la mañana y no {s:pescamos} nada. Después {s:empezó} una tormenta enorme y {s:volvimos} a casa completamente mojados, pero riéndonos. {p:Es} uno de mis mejores recuerdos.",
   "La próxima vez que lo {f:voy a ver} {f:va a ser} en Navidad. {f:Voy a ir} al pueblo una semana con mi novia, porque mi abuelo todavía no la {s:ha conocido}. Y ya {s:hemos decidido} que {f:vamos a hacer} pan juntos en el horno de su casa, como antes."],
  "cierra": "Para mí, mi abuelo {p:es} un ejemplo y una persona muy importante."},

 {"id": 3, "titulo": "Mi plato favorito", "area": "A4", "fuente": "oficial",
  "intro": "Hable de su plato favorito. Hable de:",
  "pautas": [
   {"txt": "cómo se llama, qué ingredientes lleva y cómo se prepara;", "t": ["pres"], "clave": "cómo se llama · qué lleva · cómo se prepara"},
   {"txt": "la última vez que lo comió: dónde, cuándo y con quién;", "t": ["pas"], "clave": "la última vez · lo comió"},
   {"txt": "qué comía normalmente cuando era niño;", "t": ["antes"], "clave": "comía · cuando era niño"},
   {"txt": "quién cocina en su casa ahora y qué tipo de comida hacen;", "t": ["pres"], "clave": "quién cocina ahora"},
   {"txt": "qué va a cocinar o comer en su próxima comida especial.", "t": ["fut"], "clave": "va a cocinar · próxima comida"}],
  "notas": ["lentejas de mi madre · lentejas, chorizo, zanahoria, patata, cebolla | 1 hora, olla",
            "última vez: domingo pasado · casa de mis padres · hermana + sobrinos → repetí",
            "de niño: comía en el cole · pasta, pescado (¡no me gustaba!) · merienda: pan con chocolate",
            "ahora: cocino yo · mi pareja: postres | sano, verduras, poca carne",
            "voy a hacer · paella · cumpleaños pareja · sábado 20 · 8 amigos"],
  "abre": "Voy a hablar de mi plato favorito, que {p:es} muy sencillo: las lentejas de mi madre.",
  "mod": [
   "Las lentejas {p:son} un plato típico de España, sobre todo en invierno. Mi madre las {p:prepara} con chorizo, zanahoria, patata, cebolla, ajo y un poco de pimentón. {p:Es} fácil: {p:pones} todo en una olla con agua y lo {p:cocinas} una hora, más o menos. {p:Es} un plato barato, caliente y muy sano.",
   "La última vez que las {s:comí} {s:fue} el domingo pasado. {s:Fui} a comer a casa de mis padres con mi hermana y mis sobrinos. {a:Hacía} mucho frío y mi madre {s:preparó} una olla enorme. ¡Yo {s:repetí} dos veces! Después {s:tomamos} café y {s:jugamos} a las cartas toda la tarde.",
   "Cuando {a:era} niño, {a:comía} en el comedor del colegio de lunes a viernes. Allí {a:comíamos} mucha pasta y pescado, y el pescado no me {a:gustaba} nada. Lo mejor {a:era} la merienda: mi abuela me {a:daba} pan con chocolate todas las tardes.",
   "Ahora en mi casa {p:cocino} yo casi siempre, porque mi pareja {p:trabaja} hasta tarde. {p:Intentamos} comer sano: {p:hacemos} muchas verduras, ensaladas y legumbres, y poca carne. Mi pareja {p:prepara} los postres los fines de semana; {p:hace} un flan buenísimo.",
   "Mi próxima comida especial {f:va a ser} el sábado 20, porque {p:es} el cumpleaños de mi pareja. {f:Vamos a invitar} a ocho amigos y {f:voy a cocinar} una paella. Todavía no {s:he hecho} nunca una paella para tanta gente, así que {f:voy a practicar} antes."],
  "cierra": "En resumen, mi plato favorito no {p:es} un plato de restaurante: {p:es} un plato de familia."},

 {"id": 4, "titulo": "Mi red social favorita", "area": "A12", "fuente": "oficial",
  "intro": "Hable de su red social favorita. Hable de:",
  "pautas": [
   {"txt": "cuál es su red social favorita, para qué la usa y por qué le gusta;", "t": ["pres"], "clave": "cuál es · para qué la usa · por qué le gusta"},
   {"txt": "cuánto tiempo pasa al día en las redes y si prefiere el móvil o el ordenador;", "t": ["pres"], "clave": "cuánto tiempo al día · prefiere"},
   {"txt": "cuándo empezó a usar las redes sociales y cómo era la comunicación antes;", "t": ["pas", "antes"], "clave": "cuándo empezó · cómo era antes"},
   {"txt": "algo que le pasó una vez en una red social;", "t": ["pas"], "clave": "le pasó · una vez"},
   {"txt": "si va a cambiar algo en su forma de usar las redes y por qué.", "t": ["fut"], "clave": "va a cambiar"}],
  "notas": ["Instagram · fotos, viajes, recetas · amigos lejos | me gusta: visual, inspira",
            "1 hora y media / día · noche, autobús | móvil ← siempre conmigo",
            "empecé 2012 · Facebook · universidad | antes: SMS, llamar a casa, cartas abuela",
            "una vez · foto playa · mensaje: amigo del cole, 20 años sin vernos → café",
            "voy a usar menos · no móvil en la cama | me gustaría: leer más"],
  "abre": "El tema que {s:he elegido} {p:es} mi red social favorita, que {p:es} Instagram.",
  "mod": [
   "{p:Uso} Instagram sobre todo para ver fotos: viajes, recetas de cocina y cosas de diseño. También {p:es} la forma más fácil de saber qué {p:hacen} mis amigos que {p:viven} lejos. Me {p:gusta} porque {p:es} muy visual: no {p:hay} que leer mucho y siempre {p:encuentro} ideas nuevas.",
   "{p:Paso} una hora y media al día, más o menos, en las redes. Normalmente las {p:miro} en el autobús, cuando {p:voy} al trabajo, y por la noche. {p:Prefiero} el móvil, claro, porque siempre lo {p:llevo} conmigo; el ordenador solo lo {p:uso} para trabajar.",
   "{s:Empecé} a usar las redes en 2012, en la universidad, con Facebook. Antes la comunicación {a:era} muy diferente: {a:mandábamos} mensajes SMS cortos, porque {a:eran} caros, y para hablar con mis abuelos {a:llamaba} al teléfono de casa. Mi abuela incluso me {a:escribía} cartas.",
   "Una vez me {s:pasó} algo muy bonito. {s:Subí} una foto de una playa de Asturias y un chico me {s:escribió} un mensaje: {a:era} un amigo del colegio. No {a:nos veíamos} desde hacía veinte años. {s:Quedamos} esa semana para tomar un café y ahora {p:somos} amigos otra vez.",
   "Pero creo que {p:paso} demasiado tiempo con el móvil. Por eso, este año {f:voy a cambiar} algunas cosas: no {f:voy a usar} el móvil en la cama y {f:voy a quitar} las notificaciones. Me {f:gustaría} usar ese tiempo para leer más y dormir mejor."],
  "cierra": "Para mí, Instagram {p:es} útil y divertido, pero sin exagerar."},

 {"id": 5, "titulo": "Un regalo que he recibido", "area": "A5", "fuente": "oficial",
  "intro": "Hable de un regalo especial que ha recibido. Hable de:",
  "pautas": [
   {"txt": "qué era, cómo era, quién se lo regaló y por qué;", "t": ["pas", "antes"], "clave": "qué era · quién se lo regaló"},
   {"txt": "qué sintió al abrirlo y si todavía lo tiene;", "t": ["pas", "pres"], "clave": "qué sintió · todavía lo tiene"},
   {"txt": "cuándo se hacen regalos en su país;", "t": ["pres"], "clave": "cuándo se hacen regalos"},
   {"txt": "qué regalos recibía cuando era pequeño;", "t": ["antes"], "clave": "recibía · cuando era pequeño"},
   {"txt": "qué regalo va a hacer próximamente y a quién.", "t": ["fut"], "clave": "va a hacer · próximamente"}],
  "notas": ["una cámara antigua · años 70, negra, pesada | me la regaló mi tío · terminé la carrera",
            "sorpresa, emoción → lloré | todavía: estantería, la uso a veces",
            "España: cumple, Reyes (6 enero), Navidad, bodas · amigo invisible",
            "de pequeña: muñecas, puzles, libros · Reyes: carta, zapatos en la ventana",
            "voy a regalar · madre · 65 · fin de semana en un balneario"],
  "abre": "Voy a hablar de un regalo que {s:recibí} hace diez años y que {p:es} muy especial para mí.",
  "mod": [
   "{a:Era} una cámara de fotos antigua, de los años setenta. {a:Era} negra, pequeña y muy pesada. Me la {s:regaló} mi tío Andrés cuando {s:terminé} la carrera de Bellas Artes. Él {a:era} fotógrafo y {a:sabía} que a mí me {a:encantaba} la fotografía, por eso me {s:dio} su primera cámara.",
   "Cuando {s:abrí} el paquete, {s:sentí} una emoción enorme y {s:lloré} un poco, porque {a:era} la cámara de su vida. Todavía la {p:tengo}: {p:está} en una estantería de mi salón y a veces la {p:uso} para hacer fotos en blanco y negro. {p:Es} lo más bonito que {p:tengo} en casa.",
   "En España {p:hacemos} regalos en los cumpleaños, en Navidad y, sobre todo, el seis de enero, el día de los Reyes Magos. También {p:se hacen} regalos en las bodas, pero ahora mucha gente {p:prefiere} dar dinero. En muchas oficinas {p:hacemos} el «amigo invisible»: cada persona {p:hace} un regalo a un compañero secreto.",
   "Cuando {a:era} pequeña, {a:recibía} muñecas, puzles y muchos libros. Para los Reyes, mi hermano y yo {a:escribíamos} una carta y la noche del cinco de enero {a:poníamos} los zapatos en la ventana. Por la mañana {a:había} regalos al lado de los zapatos y {a:estábamos} nerviosísimos.",
   "El mes que viene mi madre {f:va a cumplir} sesenta y cinco años y {f:se va a jubilar}. Mi hermano y yo {f:vamos a regalarle} un fin de semana en un balneario, porque siempre {p:dice} que {p:está} cansada. Todavía no se lo {s:hemos dicho}: {f:va a ser} una sorpresa."],
  "cierra": "Para mí, los mejores regalos no {p:son} los más caros, sino los que {p:tienen} una historia."},

 {"id": 6, "titulo": "Un curso que hice", "area": "A9", "fuente": "oficial",
  "intro": "Hable de un curso que hizo (de idiomas, de cocina, de informática, de baile...). Hable de:",
  "pautas": [
   {"txt": "qué curso fue, cuándo, dónde y por qué lo hizo;", "t": ["pas"], "clave": "qué curso fue · cuándo · por qué lo hizo"},
   {"txt": "cómo eran el profesor y los compañeros;", "t": ["antes"], "clave": "cómo eran"},
   {"txt": "qué le gustó más y qué no le gustó;", "t": ["pas"], "clave": "le gustó"},
   {"txt": "qué asignatura le gustaba más en el colegio y por qué;", "t": ["antes"], "clave": "le gustaba · en el colegio"},
   {"txt": "qué curso le gustaría hacer en el futuro.", "t": ["fut"], "clave": "le gustaría · en el futuro"}],
  "notas": ["curso de cocina · 2023 · 3 meses · escuela en Málaga · martes · quería comer mejor",
            "profesora Carmen · 60, simpática, exigente | 10 compañeros · jóvenes y jubilados",
            "me gustó: pan, practicar | no me gustó: limpiar, horario (8-10 noche)",
            "colegio: me gustaba Geografía · mapas · profesor contaba viajes",
            "me gustaría: curso de italiano · Italia · Roma · año que viene"],
  "abre": "Voy a hablar de un curso que {s:hice} hace dos años y que me {s:cambió} un poco la vida.",
  "mod": [
   "{s:Fue} un curso de cocina, en una escuela pequeña de Málaga, en 2023. {s:Duró} tres meses y las clases {a:eran} los martes por la noche, de ocho a diez. Lo {s:hice} porque {a:quería} comer mejor: antes {a:comía} siempre comida preparada del supermercado y {a:estaba} cansado de comer mal.",
   "La profesora {a:se llamaba} Carmen y {a:tenía} unos sesenta años. {a:Era} muy simpática, pero también bastante exigente: {a:quería} todo limpio y perfecto. {a:Éramos} diez compañeros muy diferentes: {a:había} estudiantes jóvenes, una pareja de jubilados y un chico alemán que {a:vivía} en Málaga.",
   "Lo que más me {s:gustó} {s:fue} la clase de pan: {s:aprendí} a hacer pan en casa y ahora lo {p:hago} todas las semanas. También me {s:gustó} mucho cocinar en grupo. Lo que no me {s:gustó} {s:fue} el horario, porque {a:terminábamos} muy tarde, y tener que limpiar toda la cocina al final.",
   "En el colegio, mi asignatura favorita {a:era} la Geografía. Me {a:encantaba} mirar mapas y aprender los nombres de los países. Además, el profesor {a:era} muy divertido y siempre nos {a:contaba} historias de sus viajes. Creo que por eso ahora me {p:gusta} tanto viajar.",
   "En el futuro me {f:gustaría} hacer un curso de italiano. {p:Tengo} una amiga en Roma y el año que viene {f:voy a pasar} un mes allí. {f:Quiero} hablar con la gente en su idioma y, claro, aprender recetas italianas. {f:Voy a buscar} un curso en septiembre."],
  "cierra": "En resumen, {s:fue} un curso muy útil y lo {p:recomiendo} a todo el mundo."},

 {"id": 7, "titulo": "Una fiesta especial para mí", "area": "A11", "fuente": "oficial",
  "intro": "Hable de una fiesta especial para usted (un cumpleaños, una boda, una fiesta con amigos...). Hable de:",
  "pautas": [
   {"txt": "cuándo fue, dónde y qué se celebró;", "t": ["pas"], "clave": "cuándo fue · qué se celebró"},
   {"txt": "quién estaba con usted;", "t": ["pas", "antes"], "clave": "quién estaba"},
   {"txt": "qué hizo ese día, desde la mañana hasta la noche;", "t": ["pas"], "clave": "qué hizo ese día"},
   {"txt": "por qué fue especial y cómo celebra ahora ese día;", "t": ["pas", "pres"], "clave": "por qué fue especial · cómo celebra ahora"},
   {"txt": "cuál va a ser la próxima fiesta importante para usted.", "t": ["fut"], "clave": "va a ser · la próxima fiesta"}],
  "notas": ["boda de mi hermana Marta · junio 2024 · pueblo de Cuenca · una finca",
            "estaban: toda la familia · 120 invitados · primos de Argentina (10 años sin vernos)",
            "mañana: peluquería, vestir a Marta · 12: ceremonia al aire libre · comida · baile hasta las 3",
            "especial: di un discurso · lloré | ahora: aniversario → cena familiar",
            "próxima: 50 cumpleaños de mi padre · marzo · vamos a organizar una sorpresa"],
  "abre": "Voy a hablar de una fiesta muy especial para mí: la boda de mi hermana Marta.",
  "mod": [
   "La boda {s:fue} en junio del año pasado, en una finca cerca de un pueblo de Cuenca. {s:Celebramos} que mi hermana y su novio, Jorge, {s:se casaron} después de diez años juntos. {a:Hacía} un tiempo perfecto: sol, pero no mucho calor, y el campo {a:estaba} precioso.",
   "{a:Estaba} toda la familia: mis padres, mis abuelos, mis tíos y muchos amigos. En total {a:éramos} ciento veinte invitados. Lo más bonito {s:fue} que {s:vinieron} mis primos de Argentina. No los {a:veía} desde hacía diez años y {s:fue} muy emocionante.",
   "Por la mañana {s:fui} con Marta a la peluquería y la {s:ayudé} a vestirse. A las doce {s:empezó} la ceremonia, al aire libre, debajo de unos árboles. Después {s:comimos} en la finca: {a:había} jamón, cordero y una tarta enorme. Por la tarde y por la noche {s:bailamos} hasta las tres de la mañana.",
   "{s:Fue} especial porque yo {s:di} un discurso delante de todos los invitados. {a:Estaba} muy nervioso, pero al final todo el mundo {s:aplaudió} y mi hermana {s:lloró}. Ahora, cada año, el día del aniversario, {p:hacemos} una cena familiar y {p:vemos} el vídeo de la boda.",
   "La próxima fiesta importante {f:va a ser} el cincuenta cumpleaños de mi padre, en marzo. Mi hermana y yo {f:vamos a organizar} una fiesta sorpresa en un restaurante y {f:vamos a invitar} a sus amigos de la universidad. Él no {p:sabe} nada, ¡espero que no lo descubra!"],
  "cierra": "Para mí, esa boda {s:fue} uno de los días más felices de mi vida."},

 {"id": 8, "titulo": "Mis mejores vacaciones", "area": "A6", "fuente": "oficial",
  "intro": "Hable de sus mejores vacaciones. Hable de:",
  "pautas": [
   {"txt": "adónde fue, cuándo, con quién y en qué medio de transporte;", "t": ["pas"], "clave": "adónde fue · con quién"},
   {"txt": "dónde durmió, cuánto tiempo estuvo y qué hizo allí;", "t": ["pas"], "clave": "dónde durmió · qué hizo"},
   {"txt": "por qué fueron sus mejores vacaciones;", "t": ["pas"], "clave": "por qué fueron"},
   {"txt": "cómo eran las vacaciones de su familia cuando usted era pequeño;", "t": ["antes"], "clave": "cómo eran · cuando era pequeño"},
   {"txt": "adónde va a ir en sus próximas vacaciones y con quién.", "t": ["fut"], "clave": "va a ir · próximas vacaciones"}],
  "notas": ["Sicilia · agosto 2022 · con mi pareja · avión Valencia–Palermo + coche alquilado",
            "2 semanas · casas rurales, 1 hotel · playas, Etna, mercados, granizado",
            "mejores: tranquilidad, comida, gente amable · subimos al volcán",
            "de pequeño: siempre Benidorm · apartamento tía · coche 6 horas, calor",
            "voy a ir · Noruega · julio · mi hermano · fiordos · barco"],
  "abre": "Voy a hablar de mis mejores vacaciones, que {s:fueron} en Sicilia, en Italia.",
  "mod": [
   "{s:Fui} a Sicilia en agosto de 2022 con mi pareja. {s:Volamos} de Valencia a Palermo y allí {s:alquilamos} un coche pequeño para viajar por toda la isla. {s:Fue} una buena idea, porque en Sicilia los autobuses no {p:son} muy cómodos y así {s:pudimos} ir a pueblos pequeños.",
   "{s:Estuvimos} dos semanas. {s:Dormimos} casi siempre en casas rurales y la última noche en un hotel en Catania. {s:Hicimos} muchas cosas: {s:fuimos} a playas preciosas, {s:visitamos} mercados y pueblos de montaña y {s:probamos} el granizado de limón, que {p:es} un helado típico. ¡{s:Comí} uno cada día!",
   "{s:Fueron} mis mejores vacaciones por tres cosas: la tranquilidad, la comida y la gente, que {s:fue} muy amable con nosotros. Además, un día {s:subimos} al volcán Etna. {s:Fue} difícil, porque {a:hacía} mucho viento, pero arriba las vistas {a:eran} increíbles.",
   "Cuando {a:era} pequeño, mi familia siempre {a:iba} de vacaciones al mismo sitio: a Benidorm, a un apartamento de mi tía. {a:Íbamos} en coche, seis horas con mucho calor, porque el coche no {a:tenía} aire acondicionado. Pero {a:éramos} felices: {a:pasábamos} todo el día en la playa.",
   "Mis próximas vacaciones {f:van a ser} en julio. {f:Voy a ir} a Noruega con mi hermano, porque los dos {f:queremos} ver los fiordos. {f:Vamos a hacer} un viaje en barco y {f:vamos a dormir} en cabañas. {s:He comprado} ya los billetes, pero todavía {p:tenemos} que buscar ropa de abrigo."],
  "cierra": "En resumen, Sicilia {p:es} un lugar perfecto y me {f:gustaría} volver algún día."},

 {"id": 9, "titulo": "Un viaje que he hecho", "area": "A6", "fuente": "modelo0",
  "intro": "Hable de un viaje que ha hecho (de trabajo, de estudios, de vacaciones...). Hable de:",
  "pautas": [
   {"txt": "adónde fue, por qué hizo el viaje y por qué es importante para usted;", "t": ["pas", "pres"], "clave": "adónde fue · por qué es importante"},
   {"txt": "cuánto tiempo duró, con quién fue y dónde se alojaron;", "t": ["pas"], "clave": "cuánto duró · con quién fue"},
   {"txt": "cómo era el lugar: el tiempo, la gente, la comida;", "t": ["antes"], "clave": "cómo era el lugar"},
   {"txt": "algo que le pasó durante el viaje;", "t": ["pas"], "clave": "le pasó"},
   {"txt": "si va a hacer pronto otro viaje: cuándo, adónde y por qué.", "t": ["fut"], "clave": "va a hacer · pronto"}],
  "notas": ["Japón · Tokio y Kioto · 2019 · trabajo (feria de diseño) · importante: primer viaje solo, lejos",
            "10 días · solo + 2 compañeros · hotel moderno Tokio / ryokan Kioto (dormí en el suelo)",
            "Tokio: enorme, limpio, mucha gente, silencio en el metro · comida: sushi, ramen · primavera, cerezos",
            "perdí la cartera · metro · un señor la llevó a la policía → me la devolvieron entera",
            "voy a ir · Marruecos · Semana Santa · mi pareja · desierto"],
  "abre": "El tema que {s:he elegido} {p:es} un viaje que {s:hice} a Japón hace unos años.",
  "mod": [
   "{s:Fui} a Japón en 2019 por trabajo: mi empresa me {s:mandó} a una feria de diseño en Tokio. Después {s:visité} también Kioto. {p:Es} un viaje importante para mí porque {s:fue} mi primer viaje solo tan lejos de casa. Antes nunca {a:viajaba} solo y {a:tenía} un poco de miedo.",
   "El viaje {s:duró} diez días. En Tokio {s:estuve} con dos compañeros de trabajo y {s:dormimos} en un hotel muy moderno. Después {s:fui} solo a Kioto y allí {s:me alojé} en un «ryokan», un hotel tradicional japonés. ¡{s:Dormí} en el suelo, en una cama muy fina, y {s:dormí} muy bien!",
   "Tokio {a:era} enorme y muy limpio. {a:Había} muchísima gente, pero en el metro {a:había} un silencio increíble: nadie {a:hablaba} por teléfono. La gente {a:era} muy amable y la comida, deliciosa: {a:comía} sushi y ramen todos los días. {a:Era} primavera y los cerezos {a:estaban} en flor.",
   "Un día {s:perdí} la cartera en el metro, con el dinero y las tarjetas. {a:Estaba} muy nervioso y {s:fui} a una comisaría. Allí {s:tuve} una sorpresa: un señor la {s:encontró} en el tren y la {s:llevó} a la policía. Me la {s:devolvieron} entera, ¡con todo el dinero! {s:Fue} una lección muy bonita.",
   "Sí, pronto {f:voy a hacer} otro viaje: en Semana Santa {f:voy a ir} a Marruecos con mi pareja. {f:Queremos} ver el desierto y dormir una noche en una tienda, debajo de las estrellas. {f:Vamos a ir} en barco desde Algeciras, porque a mi pareja no le {p:gusta} nada el avión."],
  "cierra": "Para mí, viajar {p:es} la mejor forma de aprender cosas nuevas."},

 {"id": 10, "titulo": "Mi deporte favorito", "area": "A7", "fuente": "frecuente",
  "intro": "Hable de su deporte o su actividad física favorita. Hable de:",
  "pautas": [
   {"txt": "qué deporte es, dónde lo practica y con quién;", "t": ["pres"], "clave": "qué deporte es · dónde lo practica"},
   {"txt": "cuántas veces a la semana lo hace y por qué le gusta;", "t": ["pres"], "clave": "cuántas veces · por qué le gusta"},
   {"txt": "cuándo y cómo empezó a practicarlo;", "t": ["pas"], "clave": "cuándo · empezó"},
   {"txt": "qué deporte hacía cuando era más joven;", "t": ["antes"], "clave": "hacía · cuando era más joven"},
   {"txt": "qué objetivo tiene para el año que viene.", "t": ["fut"], "clave": "objetivo · el año que viene"}],
  "notas": ["natación · piscina municipal · sola / a veces amiga Rosa · 20 €/mes",
            "3 veces · L, X, V · 7 de la mañana · 40 min | me gusta: relaja, espalda",
            "empecé 2021 · dolor de espalda · médico: «Tiene que nadar» · 1.er día: 10 min",
            "de joven: baloncesto · equipo del instituto · era alta · entrenaba 2 tardes",
            "voy a nadar · travesía en el mar · 2 km · septiembre → entrenar en el mar"],
  "abre": "Voy a hablar de mi deporte favorito, que {p:es} la natación.",
  "mod": [
   "{p:Nado} en la piscina municipal de mi barrio, que {p:está} a diez minutos de mi casa. Normalmente {p:voy} sola, porque {p:prefiero} nadar tranquila, pero a veces {p:viene} conmigo mi amiga Rosa. La piscina {p:es} grande, cubierta y no muy cara: {p:cuesta} veinte euros al mes.",
   "{p:Nado} tres veces a la semana: los lunes, los miércoles y los viernes, a las siete de la mañana, antes de ir a trabajar. {p:Nado} unos cuarenta minutos cada día. Me {p:gusta} porque me {p:relaja} mucho y {p:es} muy bueno para la espalda. Además, en el agua no {p:pienso} en el trabajo.",
   "{s:Empecé} a nadar en 2021. Ese año {a:trabajaba} muchas horas con el ordenador y me {a:dolía} mucho la espalda. {s:Fui} al médico y me {s:dijo}: «Tiene que nadar». Al principio {s:fue} difícil: el primer día solo {s:pude} nadar diez minutos. Pero poco a poco {s:mejoré}.",
   "Cuando {a:era} más joven, {a:jugaba} al baloncesto en el equipo de mi instituto. {a:Era} la más alta de la clase, por eso me {a:querían} en el equipo. {a:Entrenábamos} dos tardes a la semana y los sábados {a:teníamos} partido. {s:Dejé} el baloncesto cuando {s:empecé} la universidad.",
   "El año que viene {f:quiero} hacer algo nuevo: {f:voy a participar} en una travesía en el mar, en septiembre. {p:Son} dos kilómetros nadando de una playa a otra. {f:Voy a entrenar} más y este verano {f:voy a nadar} en el mar, porque no {p:es} igual que la piscina."],
  "cierra": "Para mí, nadar {p:es} mucho más que un deporte: {p:es} mi momento del día."},

 {"id": 11, "titulo": "Cómo era mi vida de niño", "area": "A3", "fuente": "frecuente",
  "intro": "Hable de cómo era su vida cuando era niño o niña. Hable de:",
  "pautas": [
   {"txt": "dónde vivía, con quién y cómo era su casa;", "t": ["antes"], "clave": "dónde vivía · cómo era"},
   {"txt": "cómo era un día normal: el colegio, las comidas, los juegos;", "t": ["antes"], "clave": "cómo era un día normal"},
   {"txt": "un recuerdo especial de su infancia;", "t": ["pas"], "clave": "un recuerdo especial"},
   {"txt": "qué es diferente ahora en la vida de los niños;", "t": ["pres", "antes"], "clave": "qué es diferente ahora"},
   {"txt": "qué le gustaría enseñar a los niños de su familia en el futuro.", "t": ["fut"], "clave": "le gustaría · en el futuro"}],
  "notas": ["pueblo de Galicia · padres + 2 hermanos + abuela · casa de piedra, huerto, perro Lobo",
            "7:30 autobús al cole · comida en casa (abuela) · tarde: calle, bici, río · tele 1 hora",
            "recuerdo: 8 años · nevó · no hubo cole · muñeco de nieve con la abuela → chocolate",
            "ahora: móviles, menos calle, muchas actividades | antes: más libertad",
            "me gustaría: sobrinos · huerto, pescar · este verano voy a llevarlos al pueblo"],
  "abre": "Hoy quiero hablar de cómo {a:era} mi vida cuando {a:era} niño, en los años ochenta.",
  "mod": [
   "{a:Vivía} en un pueblo pequeño de Galicia, con mis padres, mis dos hermanos y mi abuela. Nuestra casa {a:era} vieja y de piedra, con un huerto detrás y mucho espacio. {a:Teníamos} un perro que {a:se llamaba} Lobo, y también gallinas. En el pueblo solo {a:vivían} cien personas.",
   "Un día normal {a:empezaba} muy temprano. A las siete y media {a:cogíamos} el autobús para ir al colegio, en otro pueblo. A mediodía {a:comíamos} en casa: mi abuela {a:cocinaba} siempre. Por la tarde {a:jugábamos} en la calle, {a:íbamos} en bici al río y solo {a:veíamos} la tele una hora.",
   "{p:Tengo} un recuerdo muy especial: un invierno, cuando {a:tenía} ocho años, {s:nevó} mucho. En Galicia {p:nieva} poco, así que {s:fue} increíble. Ese día no {s:hubo} colegio y {s:hice} un muñeco de nieve enorme con mi abuela. Después {s:tomamos} chocolate caliente al lado del fuego.",
   "Ahora la vida de los niños {p:es} muy diferente. {p:Tienen} móviles y tabletas, {p:juegan} menos en la calle y {p:hacen} muchas actividades: inglés, música, deporte... Creo que antes los niños {a:teníamos} más libertad, pero ahora {p:tienen} más oportunidades para aprender.",
   "{p:Tengo} dos sobrinos de seis y nueve años que {p:viven} en Madrid. En el futuro me {f:gustaría} enseñarles las cosas del pueblo: cómo {p:funciona} un huerto o cómo {p:se pesca} en el río. Por eso este verano {f:voy a llevarlos} una semana a la casa de mi abuela."],
  "cierra": "En resumen, {s:tuve} una infancia sencilla, pero muy feliz."},

 {"id": 12, "titulo": "Mi trabajo o mis estudios", "area": "A10", "fuente": "frecuente",
  "intro": "Hable de su trabajo o de sus estudios. Hable de:",
  "pautas": [
   {"txt": "qué hace, dónde y cuál es su horario;", "t": ["pres"], "clave": "qué hace · horario"},
   {"txt": "qué es lo que más le gusta y lo que menos;", "t": ["pres"], "clave": "lo que más le gusta"},
   {"txt": "cómo encontró este trabajo o por qué eligió estos estudios;", "t": ["pas"], "clave": "cómo encontró · por qué eligió"},
   {"txt": "qué quería ser cuando era pequeño;", "t": ["antes"], "clave": "quería ser · cuando era pequeño"},
   {"txt": "qué planes tiene para su futuro profesional.", "t": ["fut"], "clave": "planes · futuro"}],
  "notas": ["recepcionista · hotel 4 estrellas · Sevilla · turnos mañana / tarde · 40 h",
            "más: idiomas, gente de todo el mundo | menos: noches, clientes enfadados",
            "estudié Turismo · 2020 prácticas aquí · director me ofreció contrato",
            "de pequeño quería: piloto · avión de juguete · domingos aeropuerto con mi padre",
            "este año voy a estudiar alemán · me gustaría: director de hotel · 5 años"],
  "abre": "Voy a hablar de mi trabajo: {p:soy} recepcionista en un hotel.",
  "mod": [
   "{p:Trabajo} en un hotel de cuatro estrellas en el centro de Sevilla. En la recepción {p:atiendo} a los clientes, {p:hago} las reservas y {p:contesto} preguntas sobre la ciudad. {p:Trabajo} cuarenta horas a la semana, con turnos: una semana {p:trabajo} de mañana y otra semana, de tarde.",
   "Lo que más me {p:gusta} {p:es} hablar idiomas y conocer a gente de todo el mundo. Cada día {p:hablo} en inglés, en francés y a veces en italiano. Lo que menos me {p:gusta} {p:son} los turnos de noche, una vez al mes, y los clientes que {p:se enfadan} por cosas pequeñas.",
   "{s:Estudié} Turismo en la universidad y en 2020 {s:hice} las prácticas en este hotel. {s:Trabajé} mucho y al final de las prácticas el director me {s:ofreció} un contrato. {s:Fue} uno de los días más felices de mi vida, porque {a:era} un momento muy difícil para el turismo.",
   "Cuando {a:era} pequeño, {a:quería} ser piloto de avión. {a:Tenía} un avión de juguete y lo {a:llevaba} a todas partes. Los domingos mi padre me {a:llevaba} al aeropuerto para ver los aviones. Al final no {s:he sido} piloto, pero {p:trabajo} con viajeros, que {p:es} parecido.",
   "Para el futuro {p:tengo} dos planes. Este año {f:voy a estudiar} alemán, porque {p:vienen} muchos clientes alemanes al hotel. Y en unos cinco años me {f:gustaría} ser director de un hotel. {p:Sé} que {p:es} difícil, pero {f:voy a intentarlo}."],
  "cierra": "Para mí, mi trabajo {p:es} cansado a veces, pero muy interesante."},

 {"id": 13, "titulo": "La ciudad donde vivo", "area": "A2", "fuente": "frecuente",
  "intro": "Hable de la ciudad o el pueblo donde vive. Hable de:",
  "pautas": [
   {"txt": "dónde está, cómo es y cuántos habitantes tiene;", "t": ["pres"], "clave": "dónde está · cómo es"},
   {"txt": "qué se puede hacer allí y qué le gusta más;", "t": ["pres"], "clave": "qué se puede hacer · qué le gusta"},
   {"txt": "cuándo y por qué fue a vivir allí;", "t": ["pas"], "clave": "cuándo · fue a vivir"},
   {"txt": "cómo era la ciudad hace unos años y qué ha cambiado;", "t": ["antes", "pas"], "clave": "cómo era · ha cambiado"},
   {"txt": "qué va a enseñar a un amigo que va a visitarle.", "t": ["fut"], "clave": "va a enseñar · va a visitarle"}],
  "notas": ["Bilbao · norte, País Vasco · 350.000 · montañas, ría, verde ← llueve",
            "Guggenheim, paseo por la ría, funicular Artxanda | me gusta: pintxos, gente abierta",
            "vine 2015 · trabajo de mi pareja · antes Salamanca · al principio: nadie, lluvia",
            "antes: industrial, gris, río sucio | ha cambiado: metro, museo, parques, turistas",
            "va a venir Ana · octubre · vamos a: casco viejo + pintxos · playa Sopelana · museo"],
  "abre": "Voy a hablar de la ciudad donde {p:vivo}, que {p:es} Bilbao.",
  "mod": [
   "Bilbao {p:está} en el norte de España, en el País Vasco. {p:Tiene} unos trescientos cincuenta mil habitantes, así que no {p:es} muy grande. {p:Está} entre montañas y {p:tiene} un río en el centro, que aquí {p:llamamos} «la ría». {p:Es} una ciudad muy verde, porque {p:llueve} bastante.",
   "En Bilbao {p:se pueden} hacer muchas cosas. {p:Puedes} visitar el museo Guggenheim, pasear al lado de la ría o subir al monte Artxanda en funicular. Pero lo que más me {p:gusta} {p:es} la comida: los «pintxos», que {p:son} pequeñas tapas. Además, la gente {p:es} muy abierta y simpática.",
   "Yo {s:vine} a vivir a Bilbao en 2015, porque mi pareja {s:encontró} trabajo aquí. Antes {a:vivíamos} en Salamanca. Al principio {s:fue} un poco difícil: no {a:conocía} a nadie y {a:llovía} casi todos los días. Pero después de unos meses {s:empecé} a trabajar en una escuela y {s:hice} amigos.",
   "Hace unos años Bilbao {a:era} una ciudad industrial y gris, y el río {a:estaba} muy sucio. Ahora {p:es} muy diferente. La ciudad {s:ha cambiado} mucho: {s:han construido} el metro, el museo y muchos parques, y el río {p:está} limpio. Ahora {p:vienen} turistas de todo el mundo.",
   "En octubre mi amiga Ana {f:va a venir} a visitarme desde Madrid. Primero {f:vamos a ir} al casco viejo a comer pintxos. Al día siguiente, si {p:hace} buen tiempo, {f:vamos a ir} en metro a la playa de Sopelana, que {p:está} muy cerca. Y, claro, {f:vamos a visitar} el Guggenheim."],
  "cierra": "En resumen, Bilbao {p:es} una ciudad perfecta para vivir."},

 {"id": 14, "titulo": "Mi casa", "area": "A2", "fuente": "frecuente",
  "intro": "Hable de la casa o el piso donde vive. Hable de:",
  "pautas": [
   {"txt": "cómo es su casa: dónde está, cuántas habitaciones tiene...;", "t": ["pres"], "clave": "cómo es · dónde está"},
   {"txt": "cuál es su lugar favorito de la casa y qué hace allí;", "t": ["pres"], "clave": "lugar favorito · qué hace allí"},
   {"txt": "cuándo se mudó a esta casa y cómo la encontró;", "t": ["pas"], "clave": "cuándo se mudó · cómo la encontró"},
   {"txt": "cómo era la casa donde vivía antes;", "t": ["antes"], "clave": "cómo era · donde vivía antes"},
   {"txt": "qué cambios va a hacer o le gustaría hacer en el futuro.", "t": ["fut"], "clave": "va a hacer · le gustaría"}],
  "notas": ["piso · Ruzafa, Valencia · 3.º sin ascensor · 2 habitaciones, salón, cocina pequeña, balcón · luz",
            "favorito: balcón · plantas, mesa, 2 sillas · tarde: sol, café, leer | finde: desayuno con mi novio",
            "me mudé 2022 · internet · 3 meses buscando · 5 pisos → balcón: «¡Este!»",
            "antes: piso compartido · 4 personas · habitación pequeña · fiestas, ruido · 1 baño",
            "voy a pintar salón: verde · sofá nuevo | me gustaría: casa con jardín, pueblo, mar, perro"],
  "abre": "Hoy quiero hablar de mi casa, que {p:es} un piso pequeño en Valencia.",
  "mod": [
   "Mi piso {p:está} en Ruzafa, un barrio del centro de Valencia. {p:Es} un tercero sin ascensor, así que {p:subo} muchas escaleras cada día. {p:Tiene} dos habitaciones, un salón, una cocina pequeña, un baño y un balcón. No {p:es} muy grande, pero {p:es} muy luminoso.",
   "Mi lugar favorito {p:es} el balcón. {p:Tengo} muchas plantas, una mesa pequeña y dos sillas. Por la tarde {p:da} el sol y me {p:siento} allí a tomar café y a leer. Los fines de semana también {p:desayuno} allí con mi novio y {p:miramos} a la gente de la calle.",
   "Me {s:mudé} a este piso en 2022. Lo {s:encontré} en internet, después de buscar durante tres meses. {s:Vi} cinco pisos, pero ninguno me {s:gustó}. Cuando {s:entré} en este y {s:vi} el balcón, {s:pensé}: «¡Este es mi piso!». {s:Firmé} el contrato esa misma semana.",
   "Antes {a:vivía} en un piso compartido con otras tres personas. {a:Era} un piso grande, pero mi habitación {a:era} muy pequeña y {a:había} mucho ruido: mis compañeros {a:hacían} fiestas casi todos los fines de semana. Además, solo {a:teníamos} un baño para cuatro.",
   "Este invierno {f:voy a pintar} el salón de color verde claro y {f:voy a comprar} un sofá nuevo. Y en el futuro me {f:gustaría} vivir en una casa con jardín, en un pueblo cerca del mar, con un perro. Pero de momento {p:estoy} muy contenta en mi piso."],
  "cierra": "Para mí, mi casa {p:es} mi lugar tranquilo."},

 {"id": 15, "titulo": "Mi tiempo libre", "area": "A7", "fuente": "frecuente",
  "intro": "Hable de su tiempo libre. Hable de:",
  "pautas": [
   {"txt": "qué hace en su tiempo libre y con quién;", "t": ["pres"], "clave": "qué hace · con quién"},
   {"txt": "qué hizo el fin de semana pasado;", "t": ["pas"], "clave": "qué hizo · el fin de semana pasado"},
   {"txt": "qué hacía en su tiempo libre cuando era adolescente;", "t": ["antes"], "clave": "qué hacía · cuando era adolescente"},
   {"txt": "por qué es importante para usted tener tiempo libre;", "t": ["pres"], "clave": "por qué es importante"},
   {"txt": "qué planes tiene para el próximo fin de semana.", "t": ["fut"], "clave": "planes · el próximo fin de semana"}],
  "notas": ["leer (novela policíaca), cine · senderismo: grupo de montaña · sábados · sierra",
            "finde pasado: sábado ruta 15 km Guadarrama, 8 → 18 h · domingo cine + cena mexicana con mi hermana",
            "adolescente: guitarra · banda con 3 amigos · garaje · una vez: fiesta del barrio, 200 personas",
            "importante: desconectar del trabajo · amigos · salud, buen humor",
            "voy a ir · Segovia · ruta corta + cordero asado · domingo: descansar, terminar un libro"],
  "abre": "El tema que {s:he elegido} {p:es} mi tiempo libre.",
  "mod": [
   "En mi tiempo libre {p:hago} varias cosas. Me {p:encanta} leer, sobre todo novelas policíacas, y {p:voy} mucho al cine. Pero mi gran afición {p:es} el senderismo: {p:estoy} en un grupo de montaña y casi todos los sábados {p:hacemos} una ruta por la sierra, cerca de Madrid.",
   "El fin de semana pasado {s:fue} muy completo. El sábado {s:hice} una ruta de quince kilómetros por la Sierra de Guadarrama con el grupo. {s:Salimos} a las ocho y {s:volvimos} a las seis, muy cansados. El domingo {s:fui} al cine con mi hermana y después {s:cenamos} en un restaurante mexicano.",
   "Cuando {a:era} adolescente, mi tiempo libre {a:era} muy diferente: {a:tocaba} la guitarra en una banda con tres amigos del instituto. {a:Ensayábamos} en el garaje del padre de un amigo y {a:hacíamos} mucho ruido. Una vez {s:tocamos} en la fiesta del barrio, delante de doscientas personas.",
   "Para mí, el tiempo libre {p:es} muy importante. Durante la semana {p:trabajo} mucho y {p:necesito} desconectar. Además, en mi tiempo libre {p:veo} a mis amigos y {p:hago} deporte, y eso {p:es} bueno para la salud y para estar de buen humor.",
   "El próximo fin de semana {f:voy a ir} a Segovia con el grupo de montaña. El sábado {f:vamos a hacer} una ruta corta y después {f:vamos a comer} cordero asado, que {p:es} típico de allí. El domingo {f:voy a descansar}: {f:quiero} terminar un libro."],
  "cierra": "En resumen, mi tiempo libre {p:es} sencillo, pero me {p:hace} muy feliz."},

 {"id": 16, "titulo": "Un libro, una película o una serie", "area": "A7", "fuente": "frecuente",
  "intro": "Hable de un libro, una película o una serie que le gusta mucho. Hable de:",
  "pautas": [
   {"txt": "qué es y de qué trata;", "t": ["pres"], "clave": "qué es · de qué trata"},
   {"txt": "cuándo y dónde lo leyó o la vio, y con quién;", "t": ["pas"], "clave": "cuándo · la vio / lo leyó"},
   {"txt": "por qué le gustó tanto;", "t": ["pas"], "clave": "le gustó"},
   {"txt": "qué libros o películas le gustaban cuando era más joven;", "t": ["antes"], "clave": "le gustaban · cuando era más joven"},
   {"txt": "qué va a leer o ver próximamente.", "t": ["fut"], "clave": "va a leer o ver · próximamente"}],
  "notas": ["serie «La casa de papel» · española · ladrones · Fábrica de Moneda · el Profesor · mono rojo",
            "vi 2018 · Berlín · compañera de piso española · sofá · 1 semana (4 capítulos / noche)",
            "gustó: suspense, personajes, «Bella ciao» · aprendí español ← versión original",
            "más joven: dibujos japoneses, aventuras · domingos cine con mi padre + pizza · no leía",
            "voy a ver · serie coreana (mi hermana) | verano: novela en español + diccionario"],
  "abre": "Voy a hablar de una serie que me {p:gusta} mucho: «La casa de papel».",
  "mod": [
   "{p:Es} una serie española. {p:Trata} de un grupo de ladrones que {p:entran} en la Fábrica de Moneda de Madrid para robar dinero. El jefe {p:se llama} «el Profesor» y {p:es} muy inteligente: lo {p:tiene} todo planeado. Los ladrones {p:llevan} un mono rojo y una máscara.",
   "La {s:vi} en 2018, cuando {a:vivía} en Berlín. Mi compañera de piso {a:era} española y una noche me {s:dijo}: «Tienes que ver esta serie». La {s:empezamos} juntas, en el sofá, y la {s:terminamos} en una semana. ¡Algunas noches {s:vimos} cuatro capítulos!",
   "Me {s:gustó} por el suspense: en cada capítulo {p:pasa} algo nuevo. También me {s:gustaron} mucho los personajes y la música, sobre todo la canción «Bella ciao». Y además, gracias a esta serie {s:aprendí} mucho español, porque la {s:vi} en versión original con subtítulos.",
   "Cuando {a:era} más joven, me {a:gustaban} los dibujos animados japoneses y las películas de aventuras. Los domingos mi padre me {a:llevaba} al cine y después {a:comíamos} una pizza. No {a:leía} mucho: los libros me {a:parecían} aburridos. Ahora, en cambio, {p:leo} bastante.",
   "Próximamente {f:voy a ver} una serie coreana que me {s:ha recomendado} mi hermana; {p:dice} que {p:es} muy divertida. Y este verano {f:quiero} leer una novela en español. {f:Va a ser} difícil, pero {f:voy a intentarlo} con un diccionario."],
  "cierra": "Para mí, las series {p:son} una forma muy divertida de aprender idiomas."},

 {"id": 17, "titulo": "Mi rutina: un día normal", "area": "A3", "fuente": "frecuente",
  "intro": "Hable de su rutina, de un día normal en su vida. Hable de:",
  "pautas": [
   {"txt": "a qué hora se levanta y qué hace por la mañana;", "t": ["pres"], "clave": "a qué hora se levanta"},
   {"txt": "qué hace por la tarde y por la noche;", "t": ["pres"], "clave": "qué hace por la tarde"},
   {"txt": "cómo era su rutina hace cinco años;", "t": ["antes"], "clave": "cómo era · hace cinco años"},
   {"txt": "un día en que su rutina cambió por completo;", "t": ["pas"], "clave": "un día · cambió"},
   {"txt": "qué va a cambiar en su rutina y por qué.", "t": ["fut"], "clave": "va a cambiar"}],
  "notas": ["me levanto 6:30 · ducha, café, tostadas · bici al trabajo, 20 min · oficina 8-15",
            "15:30 como · siesta 20 min · gimnasio o compra · cena 21 h · serie · cama 23 h",
            "hace 5 años: estudiante, Cracovia · me levantaba tarde · clases de tarde · salía · cenaba a las 6",
            "cambió: marzo, llegué a Alicante · 1.er día perdí el autobús → tarde · compré bici",
            "voy a: levantarme antes · yoga · móvil fuera del dormitorio ← duermo mal"],
  "abre": "Voy a hablar de mi rutina, de un día normal en mi vida aquí en Alicante.",
  "mod": [
   "De lunes a viernes me {p:levanto} a las seis y media. Primero me {p:ducho} y {p:tomo} un café con tostadas. Después {p:voy} al trabajo en bici; {p:tardo} veinte minutos. {p:Trabajo} en la oficina de una empresa de exportación, de ocho a tres.",
   "A las tres y media {p:como} en casa y a veces {p:duermo} una siesta corta, de veinte minutos. Por la tarde {p:voy} al gimnasio o {p:hago} la compra. {p:Ceno} sobre las nueve, que en España {p:es} normal, y después {p:veo} una serie. Normalmente me {p:acuesto} a las once.",
   "Hace cinco años mi rutina {a:era} muy diferente. {a:Era} estudiante en Cracovia, en Polonia. Me {a:levantaba} tarde, porque las clases {a:eran} por la tarde, y por la noche {a:salía} mucho con mis amigos. Además, {a:cenaba} a las seis, ¡como todo el mundo en Polonia!",
   "Mi rutina {s:cambió} por completo en marzo del año pasado, cuando {s:llegué} a Alicante para empezar este trabajo. El primer día {s:perdí} el autobús y {s:llegué} tarde a la oficina. ¡Qué vergüenza! Por eso, la semana siguiente {s:compré} la bicicleta y nunca más {s:he llegado} tarde.",
   "Pero {f:quiero} cambiar algunas cosas. A partir del mes que viene {f:voy a levantarme} un poco antes para hacer yoga por la mañana. También {f:voy a dejar} el móvil fuera del dormitorio, porque {p:duermo} mal cuando lo {p:miro} por la noche."],
  "cierra": "En resumen, {p:tengo} una rutina tranquila y me {p:gusta} mucho."},

 {"id": 18, "titulo": "Mi estación del año favorita", "area": "T", "fuente": "frecuente",
  "intro": "Hable de su estación del año favorita (primavera, verano, otoño o invierno). Hable de:",
  "pautas": [
   {"txt": "cuál es y qué tiempo hace en esa estación donde vive;", "t": ["pres"], "clave": "cuál es · qué tiempo hace"},
   {"txt": "qué le gusta hacer en esa época del año;", "t": ["pres"], "clave": "qué le gusta hacer"},
   {"txt": "qué hacía en esa estación cuando era niño;", "t": ["antes"], "clave": "qué hacía · cuando era niño"},
   {"txt": "un día especial que recuerda de esa estación;", "t": ["pas"], "clave": "un día especial · recuerda"},
   {"txt": "qué va a hacer la próxima vez que llegue esa estación.", "t": ["fut"], "clave": "va a hacer · la próxima vez"}],
  "notas": ["otoño · Lyon (Francia) · 10-18 grados · lluvia, viento · hojas amarillas, rojas",
            "pasear: parque Tête d'Or · castañas asadas, sopa · domingos: sofá, manta, té, libro",
            "de niña: recogía hojas para el cole · setas con el abuelo · Halloween, disfraces de mamá",
            "octubre 2020 · montaña con amigos · niebla → nos perdimos · 2 horas → pueblo, chocolate",
            "voy a ir · La Rioja · vendimia: recoger uvas · bodegas · 1.ª vez"],
  "abre": "Voy a hablar de mi estación favorita, que {p:es} el otoño.",
  "mod": [
   "{p:Vivo} en Lyon, en Francia, y allí el otoño {p:es} precioso. {p:Hace} fresco, entre diez y dieciocho grados, y a veces {p:llueve} o {p:hace} viento. Pero lo más bonito {p:son} los árboles: en octubre los parques {p:están} llenos de hojas amarillas, naranjas y rojas.",
   "En otoño me {p:gusta} mucho pasear por el parque de la Tête d'Or, que {p:está} cerca de mi casa. También me {p:encanta} comer castañas asadas y preparar sopas calientes. Y los domingos por la tarde, cuando {p:llueve}, me {p:quedo} en el sofá con una manta, un té y un libro.",
   "Cuando {a:era} niña, en otoño {a:recogía} hojas en el parque para el colegio. Los fines de semana {a:iba} al bosque con mi abuelo a buscar setas: él {a:sabía} qué setas {a:eran} buenas y cuáles no. Además, {a:celebrábamos} Halloween con disfraces que {a:hacía} mi madre.",
   "{p:Recuerdo} un día de octubre de 2020. {s:Fuimos} de excursión a la montaña con unos amigos. De repente {s:llegó} una niebla muy densa y {s:nos perdimos}. {s:Caminamos} dos horas y al final {s:encontramos} un pueblo pequeño. Allí {s:tomamos} un chocolate caliente buenísimo y {s:nos reímos} mucho.",
   "El próximo otoño {f:voy a ir} a La Rioja, en España, con unos amigos. {f:Vamos a participar} en la vendimia, es decir, {f:vamos a recoger} uvas para hacer vino. {f:Va a ser} la primera vez y {p:estoy} muy ilusionada. También {f:queremos} visitar algunas bodegas."],
  "cierra": "Para mí, el otoño {p:es} la estación más bonita y más tranquila del año."},

 {"id": 19, "titulo": "Una tienda o un mercado que me gusta", "area": "A5", "fuente": "frecuente",
  "intro": "Hable de una tienda o un mercado donde le gusta comprar. Hable de:",
  "pautas": [
   {"txt": "qué tienda o mercado es, dónde está y qué venden;", "t": ["pres"], "clave": "qué es · dónde está · qué venden"},
   {"txt": "cada cuánto va y qué compra normalmente;", "t": ["pres"], "clave": "cada cuánto va · normalmente"},
   {"txt": "cómo hacía la compra su familia cuando usted era pequeño;", "t": ["antes"], "clave": "cómo hacía · cuando era pequeño"},
   {"txt": "algo especial que compró allí alguna vez;", "t": ["pas"], "clave": "compró · alguna vez"},
   {"txt": "qué va a comprar la próxima vez y para qué.", "t": ["fut"], "clave": "va a comprar · la próxima vez"}],
  "notas": ["Mercado Central · Valencia · centro, al lado de la Lonja · +300 puestos · fruta, pescado, jamón, especias",
            "casi todos los sábados · fruta de temporada, pescado, queso · café + bocadillo · vendedores me conocen",
            "de pequeño: Inglaterra · supermercado enorme · coche · 1 vez/semana · lista de mi padre",
            "una vez: arroz + azafrán · 1.ª paella · mis padres vinieron · vendedor: receta → ¡les encantó!",
            "voy a comprar · cena de Navidad · gambas, pescado, turrón · ir temprano"],
  "abre": "Voy a hablar de un lugar donde me {p:encanta} comprar: el Mercado Central de Valencia.",
  "mod": [
   "El Mercado Central {p:está} en el centro de la ciudad, al lado de la Lonja. {p:Es} un edificio antiguo y muy bonito, con mucha luz. {p:Tiene} más de trescientos puestos: {p:venden} fruta, verdura, pescado, carne, jamón, quesos y especias. Siempre {p:hay} mucha gente y mucho ruido.",
   "{p:Voy} casi todos los sábados por la mañana. Normalmente {p:compro} fruta de temporada, pescado fresco y un poco de queso. Antes de comprar, {p:tomo} un café con un bocadillo en el bar del mercado. Ya {p:conozco} a algunos vendedores y siempre me {p:preguntan} por mi familia.",
   "Cuando {a:era} pequeño, en Inglaterra, mi familia {a:hacía} la compra de una forma muy diferente. {a:Íbamos} en coche a un supermercado enorme, fuera de la ciudad, una vez a la semana. Mi padre {a:hacía} una lista larga y lo {a:comprábamos} todo en una hora. No {a:había} mercados como este.",
   "Una vez {s:compré} allí algo muy especial: arroz, azafrán y verduras para hacer mi primera paella. Mis padres {s:vinieron} a visitarme desde Inglaterra y {s:quise} cocinar algo típico. Un vendedor me {s:explicó} la receta paso a paso. La paella no {s:salió} perfecta, ¡pero les {s:encantó}!",
   "El próximo sábado {f:voy a comprar} los ingredientes para la cena de Navidad. Este año mi familia {f:va a venir} a Valencia y {f:voy a preparar} gambas, pescado al horno y turrón de postre. {f:Voy a ir} muy temprano, porque en diciembre el mercado {p:está} lleno."],
  "cierra": "Para mí, el mercado {p:es} el mejor sitio para conocer una ciudad."},

 {"id": 20, "titulo": "Mi salud y mis hábitos", "area": "A8", "fuente": "frecuente",
  "intro": "Hable de su salud y de sus hábitos. Hable de:",
  "pautas": [
   {"txt": "qué hace para cuidar su salud;", "t": ["pres"], "clave": "qué hace para cuidar"},
   {"txt": "cómo son sus hábitos de comida y de sueño;", "t": ["pres"], "clave": "cómo son sus hábitos"},
   {"txt": "cómo eran sus hábitos hace unos años;", "t": ["antes"], "clave": "cómo eran · hace unos años"},
   {"txt": "algo que le pasó y que le hizo cambiar un hábito;", "t": ["pas"], "clave": "le pasó · le hizo cambiar"},
   {"txt": "qué hábito nuevo va a empezar y por qué.", "t": ["fut"], "clave": "va a empezar"}],
  "notas": ["andar 1 h/día · al trabajo y vuelta · escaleras, no ascensor · médico 1 vez al año",
            "como en casa · poca carne, verdura, fruta · no café después de las 5 · duermo 7 h (23:30-6:30)",
            "hace 10 años: fumaba · comida rápida · trabajaba de noche · restaurante São Paulo · cansado",
            "2019: esquí · me caí, me rompí la pierna · 2 meses en casa · decidí dejar de fumar",
            "voy a empezar: pilates · 2 días/semana · gimnasio del barrio · lunes ← espalda"],
  "abre": "Hoy quiero hablar de mi salud y de mis hábitos.",
  "mod": [
   "Para cuidar mi salud, {p:intento} moverme mucho. {p:Ando} una hora cada día: {p:voy} andando al trabajo y {p:vuelvo} andando a casa. Además, siempre {p:subo} por las escaleras y nunca {p:cojo} el ascensor. Una vez al año {p:voy} al médico para hacer una revisión.",
   "{p:Como} casi siempre en casa, porque así {p:sé} lo que {p:como}. {p:Tomo} poca carne y mucha verdura y fruta. No {p:bebo} café después de las cinco de la tarde, porque si no, no {p:puedo} dormir. Normalmente {p:duermo} siete horas, de once y media a seis y media.",
   "Hace diez años mis hábitos {a:eran} muy malos. {a:Fumaba} un paquete de tabaco al día y {a:comía} comida rápida casi todos los días, porque {a:trabajaba} de noche en un restaurante de São Paulo, en Brasil. No {a:hacía} deporte y siempre {a:estaba} cansado.",
   "Todo {s:cambió} en 2019. {s:Fui} a esquiar por primera vez, {s:me caí} y {s:me rompí} la pierna. {s:Estuve} dos meses en casa, sin poder salir. En ese tiempo {s:pensé} mucho en mi vida y {s:decidí} dejar de fumar. Desde entonces no {s:he fumado} ni un cigarro.",
   "Ahora me {p:duele} un poco la espalda, por eso {f:voy a empezar} a hacer pilates. {f:Voy a ir} dos días a la semana a un gimnasio de mi barrio; la primera clase {f:va a ser} el lunes que viene. También me {f:gustaría} aprender a cocinar más platos sanos."],
  "cierra": "En resumen, ahora me {p:cuido} mucho más que antes y me {p:siento} mucho mejor."},
]

# Tema cuyo esquema relleno sale como ejemplo en la pestana La preparacion
EJEMPLO_NOTAS = 3
AREAS = {"A1": "Personas", "A2": "Vivienda y ciudad", "A3": "Vida diaria", "A4": "Comida", "A5": "Compras y regalos",
         "A6": "Viajes", "A7": "Ocio y deporte", "A8": "Salud", "A9": "Estudios", "A10": "Trabajo", "A11": "Fiestas",
         "A12": "Tecnología y redes", "T": "Tiempo atmosférico"}
FUENTES = {"oficial": "Tema de las láminas oficiales", "modelo0": "Tema del modelo oficial", "frecuente": "Tema frecuente"}
