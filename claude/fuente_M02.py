# -*- coding: utf-8 -*-
# FUENTE DEL MODELO 2 · Curso de preparación DELE A2 (Módulo 2, modelos completos)
# Nivel: de entrada (perfil + = − =: lectura en la parte alta del examen, sin salir del A2; auditiva como el examen;
# escritura en la parte fácil del examen; oral como el examen). "−" = la parte fácil del examen real, nunca por debajo.
# Temas MEZCLADOS como en el examen real: cada tarea de un área distinta. Nunca gramática de B1.
# Se construye con:  python3 build_modelo.py fuente_M02
# Todo el contenido es original. Español de España.
M = "02"
NOMBRE = "Modelo 2"
NIVEL = "de entrada"
TITLE = "Examen completo"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress
TIEMPOS = {"lectura": 60, "auditiva": 40}
REC_LABEL = "Qué vas a encontrar en este modelo"
RECORDATORIO = [
 "Un examen completo con el formato y los tiempos del DELE A2: lectura (60 minutos), auditiva (40 minutos), escritura (45 minutos) y, en clase con tu profesora, la oral.",
 "Como en el examen, cada tarea habla de un tema distinto: un estudiante de intercambio, anuncios del barrio, tres restaurantes, un viaje a Oporto, restaurantes y estaciones, la radio, el transporte y la casa de los padres, una amiga con un trabajo nuevo, la primera casa, un día de nieve, una clase de guitarra y una comida en una terraza.",
 "Es un modelo de entrada con una lectura exigente: textos largos con muchos datos. La auditiva y la oral son como en el examen, y la escritura está en su parte más amable.",
 "Al terminar, en Resultados ves tu nota de cada grupo (lectura + escritura; auditiva + oral), si estás listo para presentarte, qué fichas repasar, tu control de progreso y cómo leer la nota de este modelo.",
]
TIPS_INICIO = [
 "<b>Reparte el tiempo de la lectura:</b> unos 12 minutos para la tarea 1, 15 para la 2, 15 para la 3 y 18 para la 4. Los textos son largos: lee primero las preguntas y busca solo lo que te piden. Los errores no restan.",
 "<b>Cuidado con los cambios de plan:</b> «al principio vivía...», «yo pensaba...», «pero al final...». La respuesta buena es lo que pasa al final o lo que pasa ahora.",
 "<b>Auditiva:</b> en la tarea 1 se oyen las tres opciones y dos se descartan. Fíjate en la pregunta: ¿qué pide al final?, ¿de dónde sale ahora?, ¿dónde quedan? Espera al final de la conversación antes de marcar.",
 "<b>Al terminar cada prueba, apunta cuánto has tardado en cada tarea y qué te ha costado:</b> lo vas a necesitar en el control de progreso de Resultados.",
]

# Perfil del modelo frente al examen real (+ más difícil, = como el examen, - más fácil).
# Se enseña al final de Resultados, solo después de entregar (motor_modelo_extra.py, xPerfil).
PERFIL = {"pruebas": {"lectura": "+", "auditiva": "=", "escrita": "-", "oral": "="},
 "cuando": "Este es el segundo modelo de entrada del curso: está pensado para hacerlo al principio, después del Modelo 1.",
 "nota": "Lo que lo hacía distinto: la lectura estaba en la parte alta del examen (textos largos con muchos datos, opciones falsas muy parecidas a la buena, como otra persona, otro día o un plan que cambia, y respuestas dichas con otras palabras); la auditiva y la oral eran como en el examen; la escritura estaba en su parte más amable (un correo de tú con pautas claras y temas muy cercanos). La gramática era la del A2, como en el examen."}
SIN_EFECTOS = True   # audio sin sintonía, din-don ni pitido (como el examen real)
ETIQUETAS = True     # cada intervención del audio con su etiqueta de emoción (ElevenLabs v3)

# ---------------- CONTENIDOS (enlazan con las fichas de remedio del curso) ----------------
R = {
 "R01": ("Los pasados y las preguntas", "DELEA2_curso_R01_pasados.html"),
 "R02": ("Hay, está y es", "DELEA2_curso_R02_hay_esta_es.html"),
 "R04": ("Concordancia y posesivos", "DELEA2_curso_R04_concordancia_posesivos.html"),
 "R05": ("Muy y mucho, también y tampoco", "DELEA2_curso_R05_muy_mucho_tambien_tampoco.html"),
 "R06": ("Preposiciones frecuentes (también hace, desde hace y durante)", "DELEA2_curso_R06_preposiciones.html"),
 "R07": ("Tú y usted", "DELEA2_curso_R07_tu_usted.html"),
 "R08": ("Conectores: las flechas entre frases", "DELEA2_curso_R08_conectores.html"),
 "R10": ("Lo, la, le: el paquete y el destinatario", "DELEA2_curso_R10_lo_la_le.html"),
 "R13": ("Las funciones de los correos", "DELEA2_curso_R13_formulas_correo.html"),
 "R14a": ("Vocabulario en escenas (1): la casa y el día a día", "DELEA2_curso_R14a_vocabulario_casa_dia_a_dia.html"),
 "R14b": ("Vocabulario en escenas (2): fuera de casa", "DELEA2_curso_R14b_vocabulario_fuera_de_casa.html"),
 "M0": ("Conoce el examen: las reglas de oro", "DELEA2_curso_M0_conoce_el_examen.html"),
 "M4-3": ("Taller oral: habla con el examinador", "DELEA2_curso_M4_T3_dialogos.html"),
}
def F(*ks): return [{"t": R[k][0], "u": R[k][1]} for k in ks]
CATS = {
 "pasados": {"name": "Los pasados: qué pasó, cómo era y qué has hecho",
  "repaso": "El indefinido cuenta lo que pasó y terminó (se rompió una pierna, fui en tren, abrió en 2015); el imperfecto describe cómo era o qué hacía antes (vivía en una residencia, me sentaba al fondo); el perfecto habla de lo que has hecho hasta ahora (ha empezado a estudiar, todavía no me he apuntado). En las preguntas, fíjate en las palabras de tiempo: antes, ahora, ya, todavía, al principio.",
  "reto": "Escribe tres frases sobre un viaje: cómo era el sitio (imperfecto), qué pasó un día (indefinido) y qué has hecho este año (perfecto).",
  "fichas": F("R01")},
 "planes": {"name": "Planes, propuestas y cambios de plan (pensaba..., al final..., ¿y si...?)",
  "repaso": "En el examen, la persona dice primero lo que pensaba hacer y después lo que hace de verdad: «yo pensaba volver en Navidad, pero al final vienen mis padres», «al principio pensé en cancelarlo todo». La respuesta buena es siempre la última decisión. Para proponer: ¿y si...?, ¿quedamos...?, ¿te va bien el jueves?",
  "reto": "Escribe un mensaje a un amigo con un plan que cambia: «Yo pensaba..., pero al final...».",
  "fichas": F("R01", "M4-3", "R13", "R08", "R14b")},
 "normas": {"name": "Normas y condiciones en anuncios y avisos (hay que, solo, excepto, no es necesario)",
  "repaso": "En los anuncios, las palabras pequeñas lo cambian todo: hay que (obligación), no es necesario (no es obligatorio), solo, excepto, mínimo, gratis, no está incluido. Lee la pregunta y busca solo esa condición en el texto: muchas veces la respuesta buena la dice con otras palabras (no hay que pagar nada = no se paga; hay que enseñar el tique = no todos aparcan gratis).",
  "reto": "Escribe un anuncio para vender un mueble con tres condiciones: algo que no está incluido, algo que el comprador tiene que hacer y un horario.",
  "fichas": F("M0", "R14b")},
 "tiempo": {"name": "Horas, fechas, horarios y duración (a las, de... a, todos los días, desde hace, durante)",
  "repaso": "A las + hora; de... a... / desde... hasta... para horarios; por la mañana / tarde / noche; los sábados = todos los sábados; hace + tiempo para el pasado; desde hace + tiempo para algo que sigue hoy; tardar + tiempo. En los horarios de fiestas, fíjate en las excepciones (excepto el día 25, solo por la mañana).",
  "reto": "Escribe cinco frases sobre tu semana con: a las..., de... a..., los sábados, desde hace..., tardo...",
  "fichas": F("R06", "R14b")},
 "lugares": {"name": "Lugares y localización (hay, está, en, al lado de, enfrente de, al fondo)",
  "repaso": "Hay presenta algo nuevo (hay una mesa libre al fondo); está sitúa algo que ya conocemos (el coche está enfrente del colegio). Ir a + lugar, estar en + lugar, salir de + lugar. Cuidado: el examen cambia muchas veces el lugar al final (no en la cafetería, en la puerta principal).",
  "reto": "Describe en cuatro frases dónde están las cosas importantes de tu barrio: hay..., está..., enfrente de..., al lado de...",
  "fichas": F("R02", "R06", "R14a")},
 "cantidad": {"name": "Precios, descuentos y cantidades (gratis, la mitad, el doble, muy, mucho)",
  "repaso": "Gratis / gratuito / no pagar nada = no cuesta dinero; la mitad; el doble; un treinta por ciento de descuento; más de / menos de. Muy va con adjetivos (muy caro); mucho, con nombres y verbos (mucho dinero, ahorro mucho). En los anuncios, mira a quién se aplica el descuento y a qué cosa: las lavadoras no son lo mismo que las cafeteras.",
  "reto": "Escribe un anuncio de una tienda con tres ofertas: algo gratis, algo a mitad de precio y algo que no tiene descuento.",
  "fichas": F("R05", "R14a")},
 "personas": {"name": "Quién hace qué: personas, relaciones y trato (su hermano, la dueña, tú / usted)",
  "repaso": "Muchas opciones falsas cuentan lo que hace otra persona: la compañera de piso, el hermano, la dueña de la pensión, la madre. Fíjate en los posesivos (sus padres, su hijo) y en quién es el sujeto de cada verbo. En la auditiva tarea 3, si lo hace una tercera persona, la respuesta es «ninguno de los dos».",
  "reto": "Escribe dos frases sobre lo que haces tú y dos sobre lo que hace una persona de tu familia, con posesivos (mi, su, nuestro).",
  "fichas": F("R04", "R07", "R10", "R14a")},
 "opinion": {"name": "Gustos, opiniones y sentimientos (me encanta, me da vergüenza, tengo miedo)",
  "repaso": "Me gusta / me encanta / no me gusta nada + nombre o infinitivo; me da vergüenza, tengo miedo; estar + contento, nervioso; para mí, creo que. En la lectura, la opinión puede cambiar con el tiempo (los primeros días tenía miedo; desde ese día, ya no): lee hasta el final.",
  "reto": "Escribe tres frases sobre algo que al principio te daba miedo o vergüenza y ahora no: «Al principio..., pero ahora...».",
  "fichas": F("R05", "R08")},
}
ESTRATEGIAS_NUEVAS = {}

# Talleres del curso que se recomiendan en Resultados (escritura y oral)
TALLERES = [
 {"g": "Escritura", "t": "Kit de frases para la escritura", "u": "DELEA2_curso_M3_kit_frases.html", "d": "Frases para cada tipo de texto: correo a un amigo, correo de usted, blog, biografía y fotos."},
 {"g": "Escritura", "t": "Las pautas como lista de control", "u": "DELEA2_curso_M3_pautas.html", "d": "Cada pauta, al menos una frase: la mini lista de 1 minuto."},
 {"g": "Escritura", "t": "De la banda 1 a la banda 2", "u": "DELEA2_curso_M3_banda1_a_banda2.html", "d": "Si tu texto no llega al aprobado: la operación rescate en cinco pasos."},
 {"g": "Escritura", "t": "La revisión final de 5 minutos", "u": "DELEA2_curso_M3_revision_final.html", "d": "Ocho pasadas en orden fijo antes de entregar."},
 {"g": "Escritura", "t": "Textos modelo aprobado / excelente", "u": "DELEA2_curso_M3_textos_modelo.html", "d": "Qué cambia de un texto que aprueba a uno excelente."},
 {"g": "Escritura", "t": "Banco de escritura", "u": "DELEA2_curso_M3_banco_escritura.html", "d": "Veinte láminas más para practicar, con su modelo, y un modo examen de 45 minutos."},
 {"g": "Oral", "t": "Tarea 1: el monólogo", "u": "DELEA2_curso_M4_T1_temas.html", "d": "Notas en palabras clave y los tiempos de cada pauta."},
 {"g": "Oral", "t": "Tarea 2: la foto", "u": "DELEA2_curso_M4_T2_foto.html", "d": "Las seis preguntas en orden y la regla de las tres frases."},
 {"g": "Oral", "t": "Tarea 3: habla con el examinador", "u": "DELEA2_curso_M4_T3_dialogos.html", "d": "Planificar con un amigo (tú) y servicio (usted), con el pequeño problema."},
 {"g": "Oral", "t": "Qué hacer si me bloqueo", "u": "DELEA2_curso_M4_bloqueo.html", "d": "Frases de rescate, la entrada y el cierre, y una oral completa de práctica."},
 {"g": "Oral", "t": "Dosier oral de estructuras", "u": "DELEA2_curso_M4_dosier_oral.html", "d": "Todas las estructuras de la oral en una hoja de consulta (también en PDF)."},
]

# Control de progreso estilo CRONO: tiempo recomendado por tarea y lo que puede costar
CRONO = {
 "lectura": {"tareas": [[1, 12], [2, 15], [3, 15], [4, 18]],
   "costes": ["el vocabulario", "entender el tema", "el tiempo", "las opciones parecidas", "quién dice qué", "los textos largos"]},
 "auditiva": {"tareas": [[1, 0], [2, 0], [3, 0], [4, 0]],
   "costes": ["la velocidad", "el vocabulario", "quién habla", "las opciones parecidas", "leer las preguntas a tiempo", "concentrarme todo el rato"]},
 "escrita": {"tareas": [[1, 20], [2, 25]],
   "costes": ["las pautas", "tú / usted", "los pasados", "el vocabulario", "el tiempo", "contar las palabras"]},
}

# ---------------- LECTURA ("+": parte alta de la extensión, mucha información, distractores finos) ----------------
CL1 = {"n": 1, "type": "mail",
 "instr": "Usted va a leer el correo electrónico que Jonas, un estudiante alemán, ha escrito a Carmen, la señora de la familia con la que vivió el verano pasado. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Jonas habla de varias personas (sus compañeras de piso, sus padres, la familia de Carmen) y de un plan que ha cambiado: para cada pregunta, busca quién hace cada cosa y cuál es la decisión final.",
 "head": ["De: Jonas", "Para: Carmen", "Asunto: ¡Saludos desde Granada!"],
 "body": [
  "Querida Carmen:",
  "¿Qué tal estáis todos? ¿Lucas ya ha empezado en el instituto? Yo llevo seis semanas en Granada y estoy muy contento. Las clases de la universidad son por la mañana, de nueve a dos, y los profesores hablan muy rápido, pero ya entiendo casi todo. ¡Gracias a vosotros, mi español ha mejorado muchísimo este verano!",
  "Al principio vivía en una residencia de estudiantes, pero era cara y la comida no me gustaba nada. Ahora comparto piso en el Albaicín, en una casa antigua desde donde se ve la Alhambra, con dos chicas: Ana, que es de Jaén y estudia Medicina, y Chloé, una francesa de mi clase. Ana cocina muy bien y los domingos comemos juntos. Yo friego los platos, claro.",
  "Por las tardes trabajo tres horas en una academia de idiomas: doy clases de alemán a niños. Son muy simpáticos y algunos ya cantan canciones en alemán. No gano mucho, pero así pago el alquiler y no tengo que pedir dinero a mis padres.",
  "Te escribo también por otra cosa. Yo pensaba volver a Hamburgo en Navidad, pero los billetes de avión están carísimos. Al principio buscaba algo para el 22, pero no había nada barato. Así que al final mis padres vienen aquí del 20 al 30 de diciembre. Quieren conocer Andalucía y, sobre todo, quieren conoceros a vosotros. ¿Podemos visitaros en Cádiz el día 27? Ellos duermen en un hotel, tranquilos. Mi madre quiere aprender a hacer tus croquetas, y mi padre, que no habla nada de español, ha empezado a estudiar con una aplicación del móvil. ¡Va a ser muy divertido!",
  "Escríbeme pronto y dale un abrazo muy fuerte a Paco y a Lucas.",
  "Un beso,<br>Jonas"],
 "items": [
  {"n": 1, "q": "Jonas escribe a Carmen para...", "o": ["contarle su vida en Granada y pedirle algo.", "invitar a la familia a Hamburgo en Navidad.", "darle las gracias por una visita."], "ok": 0,
   "cats": ["planes", "personas"], "es": "ES-02", "pc": "te escribo también por otra cosa · ¿podemos visitaros?",
   "why": "Jonas cuenta cómo es su vida en Granada y pregunta si puede visitarlos con sus padres. No los invita a Hamburgo, y les da las gracias por el verano, no por una visita."},
  {"n": 2, "q": "Ahora Jonas vive...", "o": ["en una residencia de estudiantes.", "con una compañera de la universidad.", "con una familia de Jaén."], "ok": 1,
   "cats": ["pasados", "lugares"], "es": "ES-05", "pc": "al principio vivía... · ahora comparto piso con... Chloé, una francesa de mi clase",
   "why": "Vive con Ana y con Chloé, que es de su clase. La residencia era al principio, y de Jaén es Ana, que es su compañera de piso, no una familia."},
  {"n": 3, "q": "Por las tardes, Jonas...", "o": ["estudia alemán en una academia.", "cocina para sus compañeras de piso.", "trabaja para pagar su casa."], "ok": 2,
   "cats": ["tiempo", "personas"], "es": "ES-03", "pc": "doy clases... así pago el alquiler = trabaja para pagar su casa",
   "why": "Trabaja tres horas en una academia y así paga el alquiler. No estudia alemán, lo enseña, y la que cocina es Ana."},
  {"n": 4, "q": "En Navidad...", "o": ["los padres de Jonas van a viajar a España.", "Jonas va a volver a Hamburgo.", "la familia de Carmen va a ir a Granada."], "ok": 0,
   "cats": ["planes"], "es": "ES-05", "pc": "yo pensaba volver..., pero... así que al final mis padres vienen aquí",
   "why": "Al final vienen sus padres a España del veinte al treinta de diciembre. Volver a Hamburgo era su primera idea, y los que viajan a Cádiz son Jonas y sus padres."},
  {"n": 5, "q": "Según el correo, el padre de Jonas...", "o": ["quiere aprender una receta de Carmen.", "está aprendiendo un poco de español.", "va a dormir en casa de Carmen."], "ok": 1,
   "cats": ["personas", "pasados"], "es": "ES-08", "pc": "mi madre quiere aprender... · mi padre ha empezado a estudiar",
   "why": "Su padre ha empezado a estudiar español con una aplicación. La receta la quiere aprender su madre, y los dos duermen en un hotel."},
 ]}

CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 15 minutos: menos de dos minutos por anuncio. Los anuncios son largos y tienen varias condiciones: lee la pregunta primero y busca solo ese dato. La opción buena casi nunca repite las palabras del anuncio: dice lo mismo de otra forma.",
 "example": {"title": "LAVANDERÍA BURBUJAS · AUTOSERVICIO",
   "body": "Abierta todos los días del año, de 8:00 a 22:00, también los festivos. Tenemos lavadoras grandes de 18 kilos, perfectas para edredones y mantas: 7 € cada lavado, con el detergente incluido. Las secadoras funcionan con monedas de 1 y 2 €: si no tienes, hay una máquina de cambio al lado de la puerta. Por favor, cuando terminen las máquinas, saca tu ropa enseguida: otros clientes esperan.",
   "q": "En esta lavandería...", "o": ["hay que llevar el detergente.", "se puede lavar ropa los domingos.", "se paga la secadora con tarjeta."], "ok": 1,
   "why": "La opción correcta es la B porque la lavandería abre todos los días del año, también los domingos."},
 "items": [
  {"n": 6, "title": "BAR EL FARO · INTERCAMBIO DE IDIOMAS",
   "body": "Todos los miércoles, de 20:00 a 22:00, quedamos en el bar El Faro para practicar idiomas: español, inglés, francés e italiano. La primera media hora hablamos en español y después cambiamos de idioma. No es una clase: no hay profesor y no hay que pagar nada, pero cada persona toma algo en la barra. No es necesario apuntarse antes: ven cualquier miércoles. El grupo de alemán empieza en noviembre: para más información, escribe a Klaus.",
   "q": "En el intercambio de idiomas...", "o": ["un profesor corrige los errores.", "hay que reservar plaza antes.", "no se paga por participar."], "ok": 2,
   "cats": ["normas", "cantidad"], "es": "ES-03", "pc": "no hay que pagar nada = no se paga · no es necesario apuntarse",
   "why": "Participar es gratis: no hay que pagar nada (solo lo que tomas en la barra). No hay profesor y no hace falta apuntarse antes."},
  {"n": 7, "title": "SE VENDE SOFÁ CAMA",
   "body": "Sofá cama de tres plazas, de color gris, con dos años. Está como nuevo porque lo hemos usado muy poco: solo cuando venían mis suegros. Lo vendemos porque nos mudamos a un piso más pequeño. Precio: 300 € (nuevo costó 600). El colchón no lo vendemos, porque es nuevo y nos lo llevamos. El sofá está en un tercero sin ascensor: tienes que venir a buscarlo con otra persona. Mensajes por la tarde a Rocío.",
   "q": "El sofá cama...", "o": ["cuesta la mitad que cuando era nuevo.", "se vende con el colchón.", "lo llevan a casa del comprador."], "ok": 0,
   "cats": ["cantidad", "normas"], "es": "ES-03", "pc": "300 € (nuevo costó 600) = la mitad · el colchón no lo vendemos",
   "why": "Cuesta trescientos euros y nuevo costó seiscientos: la mitad. El colchón no se vende, y el comprador tiene que ir a buscarlo."},
  {"n": 8, "title": "ARREGLOS CARMELA · COSTURA RÁPIDA",
   "body": "Cortamos pantalones, cambiamos cremalleras y arreglamos chaquetas y abrigos. Los arreglos pequeños, como el bajo de un pantalón, están listos en 24 horas; los abrigos tardan una semana. Si traes tres prendas, la más barata te sale gratis. No hacemos vestidos de novia ni trajes de fiesta. Abrimos de lunes a viernes, de 10:00 a 13:30 y de 17:00 a 20:00. Los sábados, solo por la mañana.",
   "q": "En este taller...", "o": ["arreglan un abrigo en un día.", "con tres arreglos, uno no se paga.", "hacen vestidos para bodas."], "ok": 1,
   "cats": ["cantidad", "tiempo"], "es": "ES-03", "pc": "la más barata te sale gratis = uno no se paga · los abrigos tardan una semana",
   "why": "Si llevas tres prendas, la más barata es gratis: un arreglo no se paga. Los abrigos tardan una semana, y no hacen vestidos de novia."},
  {"n": 9, "title": "MERCADILLO DE NAVIDAD · ARTESANÍA",
   "body": "Del 5 al 23 de diciembre, en la plaza del Ayuntamiento, más de treinta puestos de artesanía: cerámica, jabones, juguetes de madera y bisutería. Abierto de 11:00 a 21:00, y los fines de semana hasta las 22:00. Los sábados por la tarde hay talleres para niños de 4 a 10 años: hay que apuntarse en el puesto de información, porque hay pocas plazas. Este año no hay puestos de comida, pero los bares de la plaza tienen ofertas especiales.",
   "q": "En el mercadillo de Navidad...", "o": ["se puede comprar comida en los puestos.", "los talleres infantiles son por la mañana.", "cierran más tarde los sábados y domingos."], "ok": 2,
   "cats": ["tiempo", "normas"], "es": "ES-03", "pc": "los fines de semana hasta las 22:00 = más tarde los sábados y domingos",
   "why": "Los fines de semana cierran a las diez, una hora más tarde. Este año no hay puestos de comida, y los talleres son los sábados por la tarde."},
  {"n": 10, "title": "CENTRO COMERCIAL LAS PALMERAS · APARCAMIENTO",
   "body": "Las dos primeras horas son gratis para los clientes con una compra mínima de 20 €: enseña el tique en el punto de información antes de salir. A partir de la tercera hora, el aparcamiento cuesta 1,50 € cada hora. Las motos aparcan gratis siempre, en la zona de la entrada B. Los coches eléctricos se pueden cargar en la planta -1. El aparcamiento abre a las 9:00 y cierra media hora después que las tiendas.",
   "q": "En este aparcamiento...", "o": ["todos los coches aparcan gratis dos horas.", "las motos no pagan nunca.", "cierran a la misma hora que las tiendas."], "ok": 1,
   "cats": ["cantidad", "normas"], "es": "ES-04", "pc": "las motos aparcan gratis siempre = no pagan nunca · con una compra mínima",
   "why": "Las motos aparcan gratis siempre. Las dos horas gratis son solo para los clientes que compran veinte euros o más, y el aparcamiento cierra media hora después que las tiendas."},
  {"n": 11, "title": "GIMNASIO MUNICIPAL · HORARIO DE NAVIDAD",
   "body": "Del 24 de diciembre al 6 de enero, el gimnasio abre de 8:00 a 14:00, de lunes a sábado. Los días 25 de diciembre y 1 y 6 de enero está cerrado. Las clases de grupo (yoga, pilates y spinning) se suspenden estos días, excepto la de spinning de las 10:00, que sigue igual. La piscina está cerrada por limpieza del 2 al 5 de enero. A partir del día 7, horario normal.",
   "q": "Durante las fiestas, en el gimnasio...", "o": ["no hay ninguna clase de grupo.", "hay días en que no se puede nadar.", "se puede entrenar por la tarde."], "ok": 1,
   "cats": ["tiempo", "normas"], "es": "ES-06", "pc": "excepto la de spinning · la piscina está cerrada del 2 al 5",
   "why": "La piscina está cerrada del dos al cinco de enero: esos días no se puede nadar. La clase de spinning de las diez sigue, y el gimnasio cierra a las dos."},
  {"n": 12, "title": "ASOCIACIÓN DE VECINOS DE SAN ANTÓN · CONCURSO DE BELENES",
   "body": "Un año más, organizamos el concurso de belenes del barrio. Pueden participar familias, colegios y tiendas. Para apuntarse, hay que mandar una foto del belén por correo electrónico antes del 15 de diciembre. Después, el jurado visita los belenes elegidos entre el 18 y el 20. No importa el tamaño: también valen los belenes pequeños. Hay tres premios: 200 € para el mejor de una familia, una excursión para el mejor colegio y una placa para la mejor tienda.",
   "q": "En el concurso de belenes...", "o": ["el jurado ve primero una foto del belén.", "solo pueden participar las familias.", "los belenes tienen que ser grandes."], "ok": 0,
   "cats": ["normas", "personas"], "es": "ES-07", "pc": "hay que mandar una foto · después, el jurado visita",
   "why": "Primero se manda una foto y después el jurado visita los belenes elegidos. Participan también colegios y tiendas, y el tamaño no importa."},
  {"n": 13, "title": "SE BUSCA PROFESOR DE MATEMÁTICAS",
   "body": "Busco profesor o profesora de matemáticas para mi hijo, que tiene 15 años y está en tercero de la ESO. Son dos clases por semana, de una hora, en nuestra casa, los martes y los jueves a las seis de la tarde. Pagamos 15 € la hora. Es importante tener experiencia con adolescentes, pero no es necesario tener el título de profesor. Vivimos en el barrio de Benalúa, cerca de la parada del tranvía. Llamar a Paloma por la noche.",
   "q": "La persona que busca Paloma tiene que...", "o": ["dar clases en un colegio.", "ir a su casa dos tardes a la semana.", "tener el título de profesor."], "ok": 1,
   "cats": ["tiempo", "personas"], "es": "ES-03", "pc": "dos clases por semana, en nuestra casa, los martes y los jueves a las seis",
   "why": "Las clases son en su casa, los martes y los jueves por la tarde: dos tardes a la semana. No es en un colegio, y el título no es necesario."},
 ]}

CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos sobre tres restaurantes. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 15 minutos. Lee primero las seis preguntas. Los tres textos hablan de cosas parecidas (horarios, reservas, comida, cómo empezaron): busca el detalle que los separa. Cuidado con los horarios: cerrar un día no es lo mismo que abrir solo a mediodía.",
 "texts": [
  {"name": "La Despensa de Elvira", "body": "Elvira abrió este restaurante en 2015, en un antiguo almacén del centro de Burgos. Antes era profesora de química, pero siempre le gustó cocinar. Antes de abrir, estudió cocina un año en Madrid. Cada mañana compra en el mercado y escribe la carta en una pizarra según lo que encuentra: por eso no tiene platos fijos. Cierra los lunes, y las reservas solo se hacen por teléfono, porque Elvira no quiere usar aplicaciones. Hay solo doce mesas, así que los fines de semana hay que llamar varios días antes. Los niños tienen un menú especial con un postre casero. Lo que más piden los clientes es la crema de calabaza y el cordero asado."},
  {"name": "Arrocería Tomás", "body": "Tomás y su mujer, Amparo, tienen esta arrocería en Santa Pola desde hace treinta años. Solo abren a mediodía, de una a cuatro y media, porque dicen que el arroz no es una comida para la noche. Los lunes y los martes descansan. Tienen más de quince arroces diferentes, pero todos se preparan para dos personas como mínimo. En verano hay una terraza grande delante del mar; en invierno, el comedor es pequeño y muy agradable. No aceptan tarjetas: solo se puede pagar en efectivo. El más famoso es el arroz de verduras. Su hijo Rafa, que ha estudiado cocina en Valencia, prepara los postres. Muchos clientes vienen desde Elche y Alicante solo para comer allí los domingos."},
  {"name": "Casa Kimchi", "body": "Min-ji llegó de Corea a Zaragoza hace ocho años para estudiar español, y allí conoció a Pablo, un chico de Huesca. Hoy tienen juntos Casa Kimchi, un restaurante coreano en el barrio de la Magdalena. Al principio solo vendían comida para llevar; desde 2022 tienen también un comedor con veinte sillas. Pablo se ocupa del comedor y Min-ji de la cocina. En la carta hay platos picantes y otros suaves, y al lado de cada plato pone si lleva carne. Los sábados por la mañana, Min-ji da clases de cocina coreana para grupos de seis personas. Abren todos los días por la noche y, de martes a viernes, también a mediodía, con un menú más barato."}],
 "items": [
  {"n": 14, "q": "¿En qué restaurante la comida cambia según el día?", "ok": 0, "cats": ["opinion", "tiempo"], "es": "ES-09", "pc": "escribe la carta según lo que encuentra: no tiene platos fijos",
   "why": "Elvira escribe la carta cada día con lo que compra en el mercado: no hay platos fijos. En los otros dos hay una carta con muchos platos."},
  {"n": 15, "q": "¿En qué restaurante no se puede cenar?", "ok": 1, "cats": ["tiempo"], "es": "ES-03", "pc": "solo abren a mediodía",
   "why": "La arrocería de Tomás solo abre a mediodía. Casa Kimchi abre todas las noches, y La Despensa solo cierra los lunes."},
  {"n": 16, "q": "¿En qué restaurante se puede aprender a cocinar?", "ok": 2, "cats": ["planes"], "es": "ES-03", "pc": "da clases de cocina coreana",
   "why": "En Casa Kimchi, Min-ji da clases de cocina los sábados por la mañana. Elvira y Rafa cocinan, pero no dan clases."},
  {"n": 17, "q": "¿En qué restaurante hay que pagar con dinero en la mano?", "ok": 1, "cats": ["normas", "cantidad"], "es": "ES-03", "pc": "no aceptan tarjetas: solo en efectivo",
   "why": "En la arrocería no aceptan tarjetas, solo efectivo. Elvira no quiere usar aplicaciones, pero eso es para las reservas, no para pagar."},
  {"n": 18, "q": "¿Qué restaurante es ahora más grande que al principio?", "ok": 2, "cats": ["pasados", "lugares"], "es": "ES-05", "pc": "al principio solo vendían comida para llevar; desde 2022, un comedor",
   "why": "Casa Kimchi empezó solo con comida para llevar y ahora tiene un comedor. El comedor pequeño de la arrocería es el de invierno: no ha cambiado."},
  {"n": 19, "q": "¿Qué restaurante tiene algo pensado para los clientes más pequeños?", "ok": 0, "cats": ["personas"], "es": "ES-09", "pc": "los niños tienen un menú especial",
   "why": "En La Despensa los niños tienen un menú especial. En la arrocería, el hijo de Tomás hace los postres, pero es un adulto que trabaja allí."}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer el blog de una mujer que ha hecho su primer viaje sola. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto: cada párrafo responde, más o menos, a una pregunta. Atención a lo que Marta pensaba hacer y a lo que hizo de verdad, a quién hace cada cosa y a cómo cambia lo que siente.",
 "title": "Mi primer viaje sola",
 "sub": "Blog «Viajar a los cincuenta» · Marta, desde Valladolid",
 "body": [
  "Me llamo Marta, tengo cincuenta y dos años y vivo en Valladolid. El mes pasado hice algo totalmente nuevo para mí: un viaje sola. Durante toda mi vida viajé siempre con alguien: primero con mis padres, después con mi marido y mis dos hijos. Ahora mis hijos viven fuera y a mi marido no le gusta nada viajar, así que hoy os cuento cómo fueron mis cinco días en Oporto. Él me llevó a la estación y me dio un beso enorme.",
  "En realidad, la idea no era ir sola. Mi amiga Rosa y yo lo teníamos todo preparado para ir juntas en abril, pero dos semanas antes ella se rompió una pierna jugando al pádel. Me dijo: «Ve tú, que la pensión ya está pagada». Al principio pensé en cancelarlo todo, pero mi hija me animó por teléfono y, al final, decidí ir.",
  "Fui en tren hasta Vigo y allí cogí un autobús a Oporto. Fue un viaje largo, de casi ocho horas, pero muy bonito, y en el tren conocí a una pareja de Salamanca muy simpática. En Oporto me quedé en una pensión pequeña del centro, en una casa antigua con azulejos azules. La dueña, la señora Fernanda, hablaba un poco de español y todas las mañanas me preparaba el desayuno con unos pasteles de nata riquísimos.",
  "Los primeros días me daba mucha vergüenza comer sola en los restaurantes. Me sentaba en una mesa al fondo y miraba el móvil todo el rato. El tercer día, en una tasca del barrio de la Ribeira, el camarero me puso en una mesa grande con otros turistas, y terminamos todos hablando y riéndonos hasta las doce. Desde ese día, ya no tuve vergüenza.",
  "Lo que más me gustó fue pasear sin prisa por las calles, sin esperar a nadie. Hice una excursión en barco por el río Duero y fui a una librería muy famosa, pero había una cola enorme y solo estuve diez minutos dentro. Lo que menos me gustó: las cuestas. Oporto tiene muchísimas y yo llevaba unos zapatos nuevos. Por las noches escuchaba fados en un bar pequeño cerca de la pensión.",
  "Ahora ya estoy pensando en el próximo viaje. Rosa ya está bien y quiere venir conmigo, pero yo le he propuesto otra cosa: hacer cada una un viaje sola y después contarnos las historias en una cena. Mi hija dice que he vuelto otra persona. Creo que viajar sola es una forma diferente de conocerte a ti misma."],
 "items": [
  {"n": 20, "q": "Antes de este viaje, Marta...", "o": ["viajaba siempre con otras personas.", "viajaba mucho con su marido.", "no viajaba nunca a otros países."], "ok": 0,
   "cats": ["pasados", "personas"], "es": "ES-03", "pc": "viajé siempre con alguien · a mi marido no le gusta nada viajar",
   "why": "Antes viajaba siempre con alguien: con sus padres o con su familia. A su marido no le gusta viajar, y el texto no dice nada de viajes a otros países."},
  {"n": 21, "q": "Marta fue sola a Oporto porque...", "o": ["su hija no tenía vacaciones.", "quería conocer a gente nueva.", "su amiga tuvo un accidente."], "ok": 2,
   "cats": ["planes", "personas"], "es": "ES-05", "pc": "la idea no era ir sola · se rompió una pierna · al final, decidí ir",
   "why": "Iba a ir con Rosa, pero Rosa se rompió una pierna. Su hija solo la animó por teléfono, y conocer gente no era la razón del viaje."},
  {"n": 22, "q": "En el viaje de ida, Marta...", "o": ["fue todo el camino en tren.", "conoció a otros viajeros.", "tardó menos de lo que pensaba."], "ok": 1,
   "cats": ["pasados", "lugares"], "es": "ES-03", "pc": "en el tren conocí a una pareja de Salamanca",
   "why": "En el tren conoció a una pareja de Salamanca. Desde Vigo fue en autobús, y el viaje fue largo, de casi ocho horas."},
  {"n": 23, "q": "En la pensión...", "o": ["Marta hablaba portugués con la dueña.", "la dueña le daba algo dulce cada mañana.", "había otros turistas españoles."], "ok": 1,
   "cats": ["personas", "lugares"], "es": "ES-08", "pc": "todas las mañanas me preparaba el desayuno con pasteles de nata",
   "why": "Fernanda le preparaba cada mañana el desayuno con pasteles de nata. Fernanda hablaba un poco de español, y los otros turistas los conoció en la tasca."},
  {"n": 24, "q": "Después del tercer día, Marta...", "o": ["se sentía más tranquila comiendo fuera.", "comía siempre en la misma tasca.", "se sentaba siempre al fondo del restaurante."], "ok": 0,
   "cats": ["opinion", "pasados"], "es": "ES-05", "pc": "los primeros días me daba vergüenza · desde ese día, ya no tuve vergüenza",
   "why": "Desde ese día ya no tenía vergüenza de comer sola. Sentarse al fondo es lo que hacía los primeros días, y no dice que volviera a la misma tasca."},
  {"n": 25, "q": "Para el próximo viaje, Marta...", "o": ["va a ir con Rosa.", "quiere volver a Oporto.", "ha propuesto viajar por separado."], "ok": 2,
   "cats": ["planes", "opinion"], "es": "ES-08", "pc": "Rosa quiere venir conmigo, pero yo le he propuesto... cada una un viaje sola",
   "why": "Le ha propuesto a Rosa hacer cada una un viaje sola y contárselo después. Rosa quiere ir con ella, pero Marta prefiere otra cosa."},
 ]}

# ---------------- AUDITIVA ("=": como el examen) ----------------
# Sin efectos de sonido (como el examen real). Cada intervención empieza con una etiqueta de emoción de ElevenLabs v3
# (en inglés, entre corchetes): va al guion, no a las transcripciones.
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación: las tres aparecen en el audio y dos se descartan. Fíjate en la pregunta: ¿qué pide al final?, ¿de dónde sale ahora?, ¿dónde quedan? La primera cosa que se dice casi nunca es la buena.",
 "example": {"q": "¿Qué va a beber el hombre?", "o": ["una cerveza", "un zumo", "agua"], "ok": 2,
   "pres": "Va a escuchar a un hombre que habla con una camarera en un restaurante.",
   "lines": [("Mujer", "CAROLINA", "[friendly] Buenas noches. ¿Qué le pongo para beber? ¿Una cerveza?"),
             ("Hombre", "JAVIER", "[hesitant] Mmm, no, gracias, que luego tengo que conducir. ¿Tienen zumo de naranja natural?"),
             ("Mujer", "CAROLINA", "[apologetic] Natural hoy no, lo siento: se nos ha roto la máquina. Solo tenemos de botella."),
             ("Hombre", "JAVIER", "[resigned] Vaya... Pues entonces agua sin gas, por favor. Y bien fría, si puede ser.")],
   "solucion": "La opción correcta es la letra ce. Va a beber agua.",
   "img": "M02_CA1_0_cerveza_zumo_agua.jpg",
   "prompt": "Panel 1: a glass of beer on a bar table. Panel 2: a glass of orange juice. Panel 3: a bottle of still water and a glass."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Dónde se sientan al final?", "o": ["en la terraza", "al lado de la ventana", "cerca de la cocina"], "ok": 2,
   "cats": ["lugares", "planes"], "es": "ES-05", "pc": "uf, no · esa está reservada · ¿y aquella del fondo, cerca de la cocina? · vale",
   "pres": "Va a escuchar a una pareja que acaba de llegar a un restaurante.",
   "lines": [("Hombre", "EMILIO", "[cheerful] ¿Nos sentamos en la terraza? Hace un día buenísimo."),
             ("Mujer", "SUSANA", "[unsure] Uf, no, que hace mucho viento y ayer estuve resfriada. Mira, aquella mesa al lado de la ventana está libre."),
             ("Hombre", "EMILIO", "[disappointed] Esa no, que tiene un cartel de reservado. ¿Y aquella del fondo, cerca de la cocina?"),
             ("Mujer", "SUSANA", "[sighs] Bueno... hay un poco de ruido, pero vale. Lo importante es comer ya, que tengo un hambre...")],
   "why": "Se sientan en la mesa del fondo, cerca de la cocina. En la terraza hace viento y la mesa de la ventana está reservada.",
   "img": "M02_CA1_1_terraza_ventana_cocina.jpg", "prompt": "Panel 1: an empty table on a restaurant terrace in the street. Panel 2: a table for two next to a large restaurant window. Panel 3: a table at the back of a restaurant next to the swing door of the kitchen."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Qué postre van a tomar las amigas?", "o": ["flan", "helado", "tarta de queso"], "ok": 0,
   "cats": ["opinion", "personas"], "es": "ES-05", "pc": "¿pedimos la tarta? · lleva nueces y yo no puedo · con este frío, no · ¿compartimos un flan?",
   "pres": "Va a escuchar a dos amigas que terminan de comer en un restaurante.",
   "lines": [("Mujer", "VALENTINA", "[excited] ¿Pedimos la tarta de queso? Aquí es famosísima."),
             ("Mujer", "CRISTINA", "[regretful] Ay, me apetece mucho, pero la hacen con nueces y yo soy alérgica."),
             ("Mujer", "VALENTINA", "[thoughtful] Vaya... ¿Y un helado? Tienen de chocolate y de limón."),
             ("Mujer", "CRISTINA", "[laughs] ¿Con este frío? No, gracias, que vengo helada. ¿Compartimos el flan casero? Dicen que lo hace la dueña."),
             ("Mujer", "VALENTINA", "[cheerful] Vale, un flan con dos cucharas. ¡Y dos cafés!")],
   "why": "Van a compartir un flan. La tarta de queso lleva nueces, y el helado no lo quieren por el frío.",
   "img": "M02_CA1_2_flan_helado_tarta_queso.jpg", "prompt": "Panel 1: a homemade caramel flan on a small plate. Panel 2: two scoops of ice cream in a glass bowl. Panel 3: a slice of baked cheesecake on a plate."},
  {"n": 3, "conv": "Conversación tres", "q": "¿De qué andén sale hoy el tren de la mujer?", "o": ["del andén dos", "del andén cinco", "del andén siete"], "ok": 2,
   "cats": ["lugares", "tiempo"], "es": "ES-07", "pc": "normalmente sí, pero hoy... ahora sale del siete · el cinco es el de Madrid",
   "pres": "Va a escuchar a una mujer que pregunta en una estación de tren.",
   "lines": [("Mujer", "SARA", "[polite] Perdone, el tren de Valencia sale del andén dos, ¿verdad? Es lo que pone en el billete."),
             ("Hombre", "DAVID_M1", "[calm] Normalmente sí, pero hoy han cambiado la vía por unas obras. Ahora sale del siete."),
             ("Mujer", "SARA", "[confused] ¿Del siete? ¿Es el que está al lado del cinco, al final del pasillo?"),
             ("Hombre", "DAVID_M1", "[friendly] Eso es. El cinco es el de Madrid. Tiene usted diez minutos, no hace falta correr.")],
   "why": "Hoy sale del andén siete. El dos es el de siempre, y el cinco es el andén del tren de Madrid.",
   "img": "M02_CA1_3_anden_dos_cinco_siete.jpg", "prompt": "Panel 1: a train station platform sign with a big number 2. Panel 2: a train station platform sign with a big number 5. Panel 3: a train station platform sign with a big number 7."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Dónde quedan los dos amigos?", "o": ["en la cafetería", "en la puerta principal", "en las taquillas"], "ok": 1,
   "cats": ["lugares", "planes"], "es": "ES-05", "pc": "¿te espero en la cafetería? · no, que está llenísima · ¿y en las taquillas? · mejor en la puerta",
   "pres": "Va a escuchar a dos amigos que hablan por teléfono en una estación de autobuses.",
   "lines": [("Hombre", "ERIK", "[cheerful] Ya estoy en la estación. ¿Te espero en la cafetería?"),
             ("Hombre", "MARTIN_3", "[hurried] No, que a esta hora está llenísima y no nos vamos a ver. ¿Y en las taquillas?"),
             ("Hombre", "ERIK", "[doubtful] Uf, hay una cola enorme... Mejor en la puerta principal, al lado del reloj grande, que se ve muy bien, ¿vale?"),
             ("Hombre", "MARTIN_3", "[relieved] Perfecto, en la puerta. Llego en cinco minutos, que estoy aparcando.")],
   "why": "Quedan en la puerta principal, al lado del reloj. La cafetería está llena y en las taquillas hay mucha cola.",
   "img": "M02_CA1_4_cafeteria_puerta_taquillas.jpg", "prompt": "Panel 1: a busy café inside a bus station. Panel 2: the main glass entrance door of a bus station with a big clock above it. Panel 3: ticket windows in a bus station with a queue of people."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Qué día va a ir el técnico a casa del hombre?", "o": ["el lunes", "el miércoles", "el viernes"], "ok": 2,
   "cats": ["tiempo", "planes"], "es": "ES-07", "pc": "el lunes trabajo · el miércoles ya no hay huecos · el viernes, perfecto",
   "pres": "Va a escuchar a un hombre que llama a su compañía de internet.",
   "lines": [("Mujer", "ANA_MARIA", "[professional] Muy bien, ya tengo sus datos. El técnico puede ir el lunes por la mañana, de nueve a doce."),
             ("Hombre", "AGUSTIN", "[stressed] El lunes trabajo todo el día... ¿No puede ser el miércoles?"),
             ("Mujer", "ANA_MARIA", "[apologetic] El miércoles ya no tenemos huecos, lo siento. Le puedo dar el viernes por la tarde, de cuatro a seis."),
             ("Hombre", "AGUSTIN", "[relieved] Perfecto, el viernes. Ese día mi hija está en casa y puede abrir. Muchas gracias.")],
   "why": "El técnico va el viernes por la tarde. El lunes el hombre trabaja, y el miércoles no hay huecos.",
   "img": "M02_CA1_5_lunes_miercoles_viernes.jpg", "prompt": "Panel 1: a desk calendar page with the word LUNES circled. Panel 2: a desk calendar page with the word MIÉRCOLES circled. Panel 3: a desk calendar page with the word VIERNES circled."},
  {"n": 6, "conv": "Conversación seis", "q": "¿Dónde está el coche ahora?", "o": ["enfrente de un colegio", "en un aparcamiento", "delante de casa de la madre"], "ok": 0,
   "cats": ["lugares", "cantidad"], "es": "ES-05", "pc": "no, que es carísimo · allí no había sitio · está en la calle de al lado, enfrente del colegio",
   "pres": "Va a escuchar a una pareja que habla por teléfono.",
   "lines": [("Hombre", "TOMAS", "[curious] Oye, ¿has dejado el coche en el aparcamiento del centro comercial?"),
             ("Mujer", "MIA", "[amused] No, que después de dos horas es carísimo. Lo he dejado en la calle de tu madre."),
             ("Hombre", "TOMAS", "[surprised] ¿Delante de su casa? Si allí nunca hay sitio, ni de noche..."),
             ("Mujer", "MIA", "[laughs] Por eso. Está en la calle de al lado, enfrente del colegio. Te mando ahora la foto por el móvil.")],
   "why": "El coche está enfrente del colegio. En el aparcamiento no lo dejó porque es caro, y delante de la casa de la madre no había sitio.",
   "img": "M02_CA1_6_colegio_aparcamiento_casa.jpg", "prompt": "Panel 1: a car parked in a street in front of a primary school. Panel 2: a car inside an underground car park. Panel 3: a car parked in front of a small terraced house."},
 ]}

CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. Las opciones falsas usan palabras que sí se oyen (gratis, los sábados, el hospital), pero con otro dato. La buena suele decir lo mismo con otras palabras.",
 "example": {"q": "Hoy en el programa...", "o": ["entrevistan a una deportista.", "solo ponen música.", "hablan del tiempo del fin de semana."], "ok": 0,
   "why": "La opción correcta es la A porque hoy viene al estudio una nadadora que ha ganado una medalla.",
   "lab": "Locutor", "voice": "EFRAYN/RADIO",
   "text": "[warm] ¡Buenas tardes y bienvenidos a «La tarde contigo»! Hasta las seis os acompañamos con música, entrevistas y las noticias del barrio. Hoy viene al estudio Laura Pérez, la nadadora del club de la ciudad, que acaba de ganar una medalla en el campeonato de España. Y a las cinco y media, como cada día, vuestras llamadas.",
   "solucion": "La opción correcta es la letra a, porque hoy entrevistan a una nadadora que ha ganado una medalla."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "El domingo, durante la maratón...", "o": ["el metro funciona desde más temprano.", "todos los viajeros van gratis en metro.", "el paseo marítimo está cerrado todo el día."], "ok": 0,
   "cats": ["tiempo", "normas"], "es": "ES-03", "pc": "abre una hora antes = desde más temprano · gratis para los corredores",
   "lab": "Locutor", "voice": "MARTIN_2/RADIO",
   "text": "[informative] Este domingo se celebra la maratón de la ciudad. Desde las siete de la mañana hasta las dos de la tarde, no se puede circular por el paseo marítimo ni por la avenida de la Estación. El metro abre una hora antes, a las seis, y es gratis para los corredores con su número.",
   "why": "El metro abre una hora antes, a las seis. Solo es gratis para los corredores, y el paseo marítimo está cerrado hasta las dos."},
  {"n": 8, "conv": "Audio 2", "q": "En Electrohogar...", "o": ["las cafeteras están más baratas.", "no cobran por llevarse tu lavadora vieja.", "solo llevan las compras a casa en la ciudad."], "ok": 1,
   "cats": ["cantidad", "normas"], "es": "ES-03", "pc": "nos llevamos la vieja sin pagar nada · mantienen su precio · en toda la provincia",
   "lab": "Locutor", "voice": "JUAN_CARLOS/RADIO",
   "text": "[excited] ¡Llegan las rebajas a Electrohogar! Lavadoras y frigoríficos con hasta un treinta por ciento de descuento. Y si compras una lavadora nueva, nos llevamos la vieja sin pagar nada. Los pequeños electrodomésticos, como las cafeteras o las tostadoras, mantienen su precio. ¡Y la entrega a domicilio es gratis en toda la provincia!",
   "why": "Se llevan la lavadora vieja sin cobrar. Las cafeteras no tienen descuento, y la entrega es gratis en toda la provincia."},
  {"n": 9, "conv": "Audio 3", "q": "En los cines Odeón, los miércoles...", "o": ["todas las películas cuestan lo mismo.", "regalan palomitas a los niños.", "una película en tres dimensiones cuesta seis euros."], "ok": 2,
   "cats": ["cantidad", "tiempo"], "es": "ES-06", "pc": "a cuatro euros, excepto las de tres dimensiones, que cuestan dos euros más",
   "lab": "Locutora", "voice": "GABI/RADIO",
   "text": "[cheerful] En los cines Odeón, el miércoles es el día del espectador: todas las sesiones a cuatro euros, excepto las películas en tres dimensiones, que cuestan dos euros más. Y los domingos por la mañana, cine infantil con palomitas de regalo. Compra tus entradas en nuestra web y olvídate de las colas.",
   "why": "Las películas en tres dimensiones cuestan dos euros más: seis euros. No todas cuestan lo mismo, y las palomitas son los domingos."},
  {"n": 10, "conv": "Audio 4", "q": "La ludoteca del gimnasio...", "o": ["es para niños de todas las edades.", "cuesta dinero después de la primera hora.", "abre también los sábados."], "ok": 1,
   "cats": ["cantidad", "personas"], "es": "ES-03", "pc": "gratis durante la primera hora; después, dos euros la hora",
   "lab": "Locutora", "voice": "LUCIA/RADIO",
   "text": "[friendly] ¿Quieres hacer deporte y no sabes con quién dejar a tus hijos? En el gimnasio Activa abrimos una ludoteca: mientras tú entrenas, nuestros monitores cuidan a los niños de tres a diez años. La primera hora es gratis para los socios; después, dos euros la hora. Funciona por las tardes, de lunes a viernes.",
   "why": "La primera hora es gratis y después se pagan dos euros la hora. Es para niños de tres a diez años, y solo abre de lunes a viernes."},
  {"n": 11, "conv": "Audio 5", "q": "Las clases de baile del centro cívico...", "o": ["no cuestan dinero.", "son por la tarde.", "son solo de sevillanas."], "ok": 0,
   "cats": ["cantidad", "normas"], "es": "ES-03", "pc": "son gratuitas · de diez a once · además de sevillanas, tango",
   "lab": "Locutora", "voice": "NINOSKA/RADIO",
   "text": "[warm] El centro cívico de San Blas abre la inscripción para las clases de baile para mayores de sesenta años. Las clases son los martes y los jueves, de diez a once de la mañana, y son gratuitas: solo hay que traer ropa cómoda. Y este año hay una novedad: además de sevillanas, también hay clases de tango.",
   "why": "Las clases son gratuitas, es decir, no cuestan dinero. Son por la mañana, y este año también hay tango."},
  {"n": 12, "conv": "Audio 6", "q": "La nueva línea de autobús...", "o": ["tiene un billete especial.", "para en la entrada principal del hospital.", "pasa menos los sábados y domingos."], "ok": 2,
   "cats": ["tiempo", "lugares"], "es": "ES-03", "pc": "cada quince minutos... y cada media hora los fines de semana",
   "lab": "Locutor", "voice": "SANTIAGO_LAT/RADIO",
   "text": "[informative] Desde el lunes, la nueva línea veinte une el barrio de La Florida con el hospital general. Los autobuses pasan cada quince minutos, de siete de la mañana a diez de la noche, y cada media hora los fines de semana. La parada del hospital está justo delante de urgencias. El billete es el mismo que en las otras líneas.",
   "why": "Los fines de semana pasa cada media hora, no cada quince minutos: pasa menos. La parada está delante de urgencias, y el billete es el de siempre."},
 ]}

CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Celia y Samuel. Indique si los enunciados (del 13 al 18) se refieren a Celia (A), a Samuel (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Celia y Samuel hablan de cambios en su vida. Cuidado con lo que hace otra persona (el hermano de Samuel) y con lo que alguien quiere hacer, pero todavía no ha hecho: en esos casos, la respuesta es C.",
 "who": ["Celia", "Samuel"], "voices": {"CELIA": "RAQUEL", "SAMUEL": "GABRIEL_ES"},
 "lines": [
  ("SAMUEL", "[surprised] ¡Celia! ¿Qué haces con ese casco? ¿Te has comprado una moto?"),
  ("CELIA", "[laughs] Qué va, un patinete eléctrico. Desde octubre voy al trabajo en patinete. Antes cogía el autobús, pero tardaba cuarenta minutos y siempre iba lleno. Ahora tardo quince."),
  ("SAMUEL", "[impressed] ¡Qué bien! Yo, al contrario: desde el mes pasado vivo otra vez con mis padres, y ahora el trabajo me queda lejísimos. Tardo casi una hora en autobús."),
  ("CELIA", "[curious] ¿Con tus padres? ¿Y eso?"),
  ("SAMUEL", "[sighs] Para ahorrar. El alquiler de mi piso era carísimo y quiero comprarme uno el año que viene. Mi hermano Iván hizo lo mismo hace dos años y ya tiene su casa."),
  ("CELIA", "[thoughtful] Pues yo no puedo volver con mis padres: viven en Lugo, ¡y mi trabajo está aquí!"),
  ("SAMUEL", "[laughs] Ya, ya. Tú tienes suerte con el patinete."),
  ("CELIA", "[teasing] ¿Y qué tal? ¿Te hace la comida tu madre?"),
  ("SAMUEL", "[laughs] Mi padre, que está jubilado y cocina de maravilla. Engordo un kilo cada semana. Por eso quiero apuntarme al gimnasio del barrio... pero todavía no lo he hecho."),
  ("CELIA", "[cheerful] Yo con el patinete no hago nada de ejercicio, ¿eh? Pero los fines de semana salgo a correr con mi perra por el parque. ¿Por qué no vienes un sábado?"),
  ("SAMUEL", "[hesitant] Uf, los sábados trabajo en la tienda de mi tío hasta las dos... y por la tarde estoy muerto."),
  ("CELIA", "[encouraging] Pues el domingo. Quedamos a las nueve en la fuente del parque."),
  ("SAMUEL", "[laughs] ¿A las nueve un domingo? Bueno, vale, pero a las diez."),
  ("CELIA", "[happy] Trato hecho. Y después te invito a un café, que yo ahora ahorro mucho: el patinete casi no gasta nada.")],
 "items": [
  {"n": 13, "q": "Tarda menos que antes en llegar al trabajo.", "ok": 0, "cats": ["tiempo", "pasados"], "es": "ES-07", "pc": "antes tardaba cuarenta minutos... ahora tardo quince",
   "why": "Celia antes tardaba cuarenta minutos en autobús y ahora tarda quince. Samuel ahora tarda más, casi una hora."},
  {"n": 14, "q": "Ahora vive con su familia.", "ok": 1, "cats": ["personas", "lugares"], "es": "ES-03", "pc": "vivo otra vez con mis padres",
   "why": "Samuel vive otra vez con sus padres desde el mes pasado."},
  {"n": 15, "q": "Ya tiene una casa propia.", "ok": 2, "cats": ["personas", "pasados"], "es": "ES-08", "pc": "mi hermano Iván... ya tiene su casa · quiero comprarme uno el año que viene",
   "why": "El que ya tiene casa es Iván, el hermano de Samuel, una tercera persona. Samuel quiere comprarse un piso el año que viene: ninguno de los dos."},
  {"n": 16, "q": "Se ha apuntado a un gimnasio.", "ok": 2, "cats": ["planes"], "es": "ES-05", "pc": "quiero apuntarme... pero todavía no lo he hecho",
   "why": "Samuel quiere apuntarse, pero todavía no lo ha hecho, y Celia no va al gimnasio: ninguno de los dos."},
  {"n": 17, "q": "Hace deporte con su animal.", "ok": 0, "cats": ["opinion", "personas"], "es": "ES-03", "pc": "salgo a correr con mi perra",
   "why": "Celia sale a correr con su perra los fines de semana."},
  {"n": 18, "q": "Trabaja también algunos fines de semana.", "ok": 1, "cats": ["tiempo"], "es": "ES-03", "pc": "los sábados trabajo en la tienda de mi tío",
   "why": "Samuel trabaja los sábados por la mañana en la tienda de su tío."}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. Hay parejas muy parecidas (dos de cenas, dos de profesionales, dos de actividades): en cada mensaje pregúntate quién habla, dónde y qué cambia exactamente. Sobran tres enunciados.",
 "enun": [
  "Hay que llevar un animal a una clínica.",
  "Alguien cambia la hora de una cena.",
  "Una parte de un encargo todavía no está lista.",
  "Alguien cambia el sitio de una cena.",
  "Un profesional no puede ir hoy.",
  "Recuerdan lo que hay que llevar a una actividad.",
  "Un profesional va a llegar más tarde.",
  "Hay una actividad nueva.",
  "Alguien pide que le devuelvan algo.",
  "Una actividad se suspende.",
  "Van a llevar algo a casa de alguien."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "MAYA/RADIO",
   "text": "[friendly] Hola, buenos días. Le llamamos de la clínica veterinaria Cuatro Patas. Le recordamos que este mes a su gato Simba le toca la vacuna. Puede venir sin cita por las mañanas, de nueve a una. Si prefiere la tarde, llámenos y le damos hora.",
   "solucion": "La opción correcta es la letra a: hay que llevar un animal a una clínica."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 2, "cats": ["tiempo", "normas"], "es": "ES-10", "pc": "su abrigo ya está limpio, pero el vestido necesita dos días más",
   "lab": "Contestador", "voice": "LUISA/RADIO",
   "text": "[polite] Buenas tardes, le llamo de la tintorería Limpiasol. Su abrigo ya está limpio, pero el vestido azul necesita dos días más, porque tiene una mancha difícil. Puede recoger el abrigo desde hoy; el vestido, a partir del jueves.",
   "why": "El abrigo está listo, pero el vestido todavía no: una parte del encargo no está lista. Nadie va a llevarlo a casa (K sobra para este mensaje)."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 3, "cats": ["planes", "lugares"], "es": "ES-10", "pc": "el italiano está cerrado, así que vamos al mexicano · la hora es la misma",
   "lab": "Contestador", "voice": "CRISTINA_LAT/RADIO",
   "text": "[cheerful] Hola, Pili, soy Sonia. Cambio de planes para la cena del viernes: el restaurante italiano está cerrado por vacaciones, así que vamos al mexicano de la plaza. La hora es la misma, a las nueve. ¡Avisa tú a Carmen, porfa!",
   "why": "Sonia cambia el restaurante de la cena, no la hora: la hora es la misma (B sobra)."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 6, "cats": ["tiempo", "personas"], "es": "ES-10", "pc": "en vez de a las diez, llego sobre las doce",
   "lab": "Contestador", "voice": "CRISTIAN/RADIO",
   "text": "[apologetic] Buenos días, soy Julián, el fontanero. Hoy voy un poco tarde, porque el trabajo de antes se ha complicado. En vez de a las diez, llego sobre las doce. Si no está en casa a esa hora, dígamelo y vamos otro día.",
   "why": "El fontanero va hoy, pero llega dos horas más tarde. Sí puede ir hoy (E sobra)."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 5, "cats": ["normas", "planes"], "es": "ES-10", "pc": "mañana es la excursión... tienen que traer la comida y una gorra",
   "lab": "Contestador", "voice": "MARTIN_1/RADIO",
   "text": "[calm] Buenas tardes, familias. Les recordamos desde el colegio Los Almendros que mañana es la excursión a la granja escuela. Los niños tienen que estar a las ocho y media en la puerta, con la comida y una gorra. Volvemos a las cinco.",
   "why": "El colegio recuerda qué tienen que llevar los niños a la excursión: la comida y una gorra."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 7, "cats": ["tiempo", "cantidad"], "es": "ES-10", "pc": "megafonía · a partir del lunes empieza una nueva clase",
   "lab": "Megafonía", "voice": "LUIS_GUILLERMO/RADIO",
   "text": "[neutral] Atención, señores socios: a partir del lunes empieza una nueva clase de zumba, los martes y los jueves a las siete de la tarde, en la sala dos. Es gratis para todos los socios, pero hay pocas plazas: apúntense en recepción.",
   "why": "En el gimnasio empieza una clase nueva. Ninguna actividad se suspende (J sobra)."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 8, "cats": ["personas", "planes"], "es": "ES-10", "pc": "¿todavía tienes mi maleta? la necesito",
   "lab": "Contestador", "voice": "JUAN_RESTREPO/RADIO",
   "text": "[hurried] Oye, Marta, soy Jorge. ¿Todavía tienes mi maleta grande, la roja? Es que el sábado me voy a Londres y la necesito. ¿Paso a buscarla mañana por la tarde? Si no estás, déjasela al portero.",
   "why": "Jorge pide a Marta que le devuelva su maleta."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 10, "cats": ["lugares", "tiempo"], "es": "ES-10", "pc": "ya ha llegado el sofá · lo llevamos a su casa el miércoles",
   "lab": "Contestador", "voice": "DIEGO_PE/RADIO",
   "text": "[friendly] Hola, buenos días, le llamamos de Muebles Lorca. Ya ha llegado el sofá que pidió en septiembre. Se lo llevamos a casa el miércoles por la mañana, entre las nueve y las doce. Si ese día no le va bien, llámenos.",
   "why": "La tienda va a llevar el sofá a casa del cliente el miércoles."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

# Voces del último modelo que han hecho (M1): no se repiten aquí
VOCES_EVITAR = ["DANIEL_ES", "FIONA", "MARIO", "LYDIA", "SARA_JOVEN", "VOLU", "AITANA", "DANI", "MARINA_ES", "LUIS_VEGA", "SARA_2",
                "SANTIAGO_ES", "TATIANA", "OSCAR", "SERGIO", "BOBBY", "TAMARA", "JAVI_ROJAS", "ENRIQUE", "LINA", "ZABRA", "EVA",
                "RAFA", "DIANA", "DAVID_M2", "RITA", "ALEJANDRO", "DIEGO", "MARINA", "GABRIEL_CO", "JANET",
                "HUGO", "CLARA", "LUCIA_AR"]   # estas tres, descartadas por María (22/10)
REPARTO = """# REPARTO DE VOCES M02 (ninguna voz del M1, el último modelo que han hecho)
# SIN EFECTOS DE SONIDO: ni sintonía, ni din-don, ni pitido (el examen real tampoco los tiene).
# Cada intervención lleva al principio su etiqueta de emoción de ElevenLabs v3 ([cheerful], [sighs]...).
# T1 conversaciones (v3): 0 la bebida = CAROLINA (camarera) + JAVIER · 1 la mesa = EMILIO + SUSANA · 2 el postre = VALENTINA (Colombia) + CRISTINA
#   3 el andén = SARA + DAVID_M1 (empleado) · 4 dónde quedan = ERIK (Venezuela) + MARTIN_3 · 5 el técnico = ANA_MARIA (México) + AGUSTIN (Argentina)
#   6 el coche = TOMAS (Argentina) + MIA
# T2 radio (perfil /RADIO): 0 «La tarde contigo» = EFRAYN · 1 maratón = MARTIN_2 · 2 Electrohogar = JUAN_CARLOS · 3 cines Odeón = GABI (Argentina)
#   4 ludoteca = LUCIA · 5 baile en el centro cívico = NINOSKA · 6 línea veinte = SANTIAGO_LAT
# T3 conversación entre amigos: CELIA = RAQUEL · SAMUEL = GABRIEL_ES
# T4 mensajes (/RADIO): 0 contestador veterinario = MAYA · 1 tintorería = LUISA · 2 Sonia = CRISTINA_LAT · 3 fontanero = CRISTIAN (Colombia)
#   4 colegio = MARTIN_1 · 5 megafonía gimnasio = LUIS_GUILLERMO (México) · 6 Jorge = JUAN_RESTREPO (Colombia) · 7 Muebles Lorca = DIEGO_PE (Perú)"""

# ---------------- ESCRITURA ("−": tú con una amiga, pautas claras, temas muy cercanos) ----------------
# Textos modelo: [n] = empieza la frase de la pauta n · _texto_ = conector (sale subrayado).
ESCRITA = {"t1": {"instr": "Su amiga Bea le ha escrito este correo.", "trato": "tú",
  "input": ["¡Hola! ¿Cómo estás? ¡Tengo una noticia! He cambiado de trabajo y ahora estoy en una oficina muy cerca de tu casa. ¿Comemos juntos un día de la semana que viene? Cuéntame también qué tal todo: ¡hace mucho que no hablamos!", "Un abrazo,<br>Bea"],
  "lead": "Conteste a Bea. En el correo tiene que:",
  "pautas": ["saludar y decirle qué le parece su nuevo trabajo;", "contarle cómo es normalmente su semana;", "contarle qué ha hecho usted este mes;", "proponerle un día, un lugar y una hora para comer;", "hacerle dos preguntas sobre su nuevo trabajo y despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Una revista en español prepara un número especial sobre la casa. Escriba un texto sobre la primera casa en la que vivió sin sus padres. Hable de:",
   "pautas": ["dónde estaba y cuándo fue a vivir allí;", "cómo era la casa y con quién vivía;", "qué hacía allí un día normal;", "algo divertido o especial que le pasó en esa casa;", "cómo es su casa ahora y qué le gusta más de ella."]},
  "op2": {"title": "Opción 2", "intro": "Lucía vive en Valverde, un pueblo de Murcia donde casi nunca nieva. Aquí tiene tres fotos de un día de invierno.",
   "photos": ["Por la mañana. Lucía, una niña de unos nueve años, y su padre desayunan en la cocina y miran por la ventana: todo está blanco.",
              "Al mediodía. Lucía, su hermano pequeño y unos vecinos hacen un muñeco de nieve en la plaza del pueblo.",
              "Por la tarde. Toda la familia toma chocolate caliente en la cocina; los guantes y los gorros están encima del radiador."],
   "ficha": [], "intro2": "Escriba un texto sobre el día que nevó en el pueblo de Lucía. Hable de:",
   "pautas": ["qué vio Lucía al levantarse y cómo se sintió;", "qué hicieron en la plaza y con quién;", "qué hicieron por la tarde y por qué cree usted que ese día no hubo colegio."],
   "img": "M02_escrita_lucia_nieve_pueblo.jpg", "imgAlt": "Tres fotos de un día de nieve en un pueblo: Lucía y su padre miran la nieve por la ventana, los niños y los vecinos hacen un muñeco de nieve en la plaza y la familia toma chocolate en la cocina"},
  "min": 70, "max": 80},
 "modelos": {
  "t1": {"titulo": "Tarea 1 · Correo a una amiga (de tú)", "tarea": 1,
   "aprobado": {"texto": [
     "[1]¡Hola, Bea! ¡Qué buena noticia! Me alegro mucho por tu trabajo nuevo.",
     "[2]Yo trabajo de lunes a viernes y por las tardes voy a clase de inglés. [3]Este mes he estado en Valencia con mi hermana y he pintado mi habitación. [4]¿Comemos el martes a las dos en el bar Lola, al lado de mi casa? [5]¿Cómo son tus compañeros? ¿Qué horario tienes?",
     "Un abrazo,<br>Pedro"],
    "porque": "Contesta a las cinco pautas con frases sencillas: felicita a Bea, cuenta su semana en presente, lo que ha hecho este mes con el pretérito perfecto (he estado, he pintado), propone día, lugar y hora, y hace dos preguntas sobre el trabajo. Todo de tú, del saludo a la despedida."},
   "excelente": {"texto": [
     "[1]¡Hola, Bea! ¡Enhorabuena! Me parece genial tu trabajo nuevo, _y además_ ahora estamos cerca.",
     "[2]Mi semana es tranquila: trabajo por las mañanas y, _después_, voy al gimnasio. [3]Este mes he estado muy liado, _porque_ me he mudado de piso. [4]¿Te va bien el jueves a las dos en el bar Lola, enfrente de mi portal? [5]¿Qué haces exactamente? ¿Estás contenta?",
     "¡Un abrazo!<br>Pedro"],
    "porque": "Las mismas cinco pautas, con dos o tres mejoras del A2: conectores para unir las ideas (y además, después, porque), palabras más precisas (genial, liado, enfrente de mi portal), un porqué (me he mudado de piso) y una propuesta más amable (¿te va bien...?). Sigue siendo corto y de tú.",
    "mejoras": ["un conector más (y además, después, porque)", "una palabra más precisa (genial, muy liado, enfrente de mi portal)", "un detalle o un porqué (me he mudado de piso)", "una propuesta más amable (¿Te va bien el jueves...?)"]}},
  "op1": {"titulo": "Tarea 2 · Opción 1 · Mi primera casa sin mis padres", "tarea": 2,
   "aprobado": {"texto": [
     "[1]Mi primera casa sin mis padres estaba en Sevilla. Fui a vivir allí en 2010, cuando empecé la universidad. [2]Era un piso pequeño y viejo, con un balcón. Vivía con dos compañeras de clase. [3]Por las mañanas íbamos a clase y por las tardes estudiábamos en la cocina. [4]Un día se rompió la lavadora y la cocina se llenó de agua. [5]Ahora vivo en un piso grande. Me gusta más la terraza."],
    "porque": "Cumple las cinco pautas, una o dos frases para cada una. Usa el imperfecto para describir la casa y lo que hacían (era, vivía, íbamos), el indefinido para lo que pasó (fui, empecé, se rompió) y el presente para ahora. Es sencillo y aprueba."},
   "excelente": {"texto": [
     "[1]Mi primera casa sin mis padres estaba en Sevilla. Me fui a vivir allí en 2010, _cuando_ empecé la universidad. [2]Era un piso antiguo y luminoso, con un balcón lleno de plantas, y lo compartía con dos compañeras. [3]Normalmente estudiábamos juntas en la cocina _y luego_ cenábamos en el balcón. [4]Una noche se rompió la lavadora _y_, _al final_, ¡fregamos el suelo hasta las dos! [5]Ahora mi piso es más grande, _pero_ lo que más me gusta es la terraza."],
    "porque": "Las mismas cinco pautas, con más variedad: un pasado bien combinado (cuando empecé la universidad, me fui...), conectores para contar (cuando, y luego, al final, pero), palabras más precisas para describir (antiguo, luminoso) y una exclamación con emoción. Todo sigue siendo A2.",
    "mejoras": ["un pasado bien combinado (cuando empecé la universidad, me fui a vivir allí)", "un conector más (y luego, al final, pero)", "una palabra más precisa (antiguo, luminoso, compartía)", "una exclamación con emoción (¡fregamos el suelo hasta las dos!)"]}},
  "op2": {"titulo": "Tarea 2 · Opción 2 · El día que nevó en el pueblo", "tarea": 2,
   "aprobado": {"texto": [
     "[1]Un día de invierno, Lucía se levantó y miró por la ventana con su padre. Todo estaba blanco y ella estaba muy contenta, porque nunca nieva en su pueblo. [2]Al mediodía fue a la plaza con su hermano y unos vecinos. Hicieron un muñeco de nieve muy grande y se rieron mucho. [3]Por la tarde, la familia tomó chocolate caliente en la cocina. Creo que no hubo colegio porque las carreteras estaban cerradas."],
    "porque": "Cuenta el día de Lucía en pasado (no describe las fotos en presente): el indefinido para lo que pasó (se levantó, hicieron, tomó) y el imperfecto para describir (estaba blanco, estaba contenta). Responde a las tres pautas, también a la suposición del final (creo que no hubo colegio porque...)."},
   "excelente": {"texto": [
     "[1]Aquel día, Lucía se despertó muy pronto y, _cuando_ miró por la ventana, ¡todo estaba blanco! Estaba nerviosa _porque_ era la primera vez que veía la nieve. [2]_Después_ de desayunar, salió a la plaza con su hermano y los vecinos, y entre todos hicieron un muñeco enorme. [3]Por la tarde tomaron chocolate caliente en la cocina con sus padres. Supongo que no hubo colegio _porque_ el autobús no podía subir al pueblo."],
    "porque": "Más variedad de pasados (cuando miró, todo estaba blanco; era la primera vez), conectores que ordenan la historia (cuando, porque, después), palabras más precisas (se despertó, enorme, supongo) y una suposición con su porqué.",
    "mejoras": ["un pasado bien combinado (cuando miró por la ventana, todo estaba blanco)", "un conector más (cuando, después)", "una palabra más precisa (se despertó, enorme, supongo)", "un detalle o un porqué (era la primera vez que veía la nieve)"]}}}}

# ---------------- ORAL ("=": como el examen) ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: un regalo que he recibido", "pautas": ["qué regalo es, quién se lo hizo y por qué;", "dónde estaba y cómo se sintió cuando lo recibió;", "qué regalos le gustaba recibir cuando era pequeño o pequeña;", "qué piensa de regalar dinero en lugar de un objeto;", "qué regalo quiere hacer usted este año y a quién."]},
  {"title": "Opción 2: una fiesta especial para mí", "pautas": ["qué fiesta fue, cuándo y dónde la celebró;", "quién estaba y qué hicieron;", "cómo celebraba esa fiesta su familia cuando usted era pequeño o pequeña;", "qué fiesta de su país le recomienda a un turista y por qué;", "cómo quiere celebrar su próxima fiesta importante."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1 · Clases para adultos", "desc": "Una sala de un centro cívico, una tarde de otoño. Una mujer de unos sesenta años, con el pelo corto y blanco, gafas y un jersey morado, toca la guitarra sentada en una silla y mira sus dedos con mucha atención. A su lado, un chico de unos treinta años, con barba, camisa vaquera y otra guitarra en las piernas, le enseña cómo poner la mano. Delante tienen un atril con una partitura. En la sala hay más sillas, una pizarra blanca con notas de música, una funda de guitarra en el suelo con una pegatina de un grupo de rock, una botella de agua y un móvil.", "img": "M02_oral_foto1_clase_guitarra_adultos.jpg"},
  {"title": "Fotografía 2 · Comer fuera", "desc": "La terraza de un bar en una plaza, un mediodía de primavera. Dos amigas de unos treinta años están sentadas a una mesa. Una, con el pelo rizado y una camiseta de rayas, hace una foto a los platos con el móvil; la otra, con coleta y chaqueta vaquera, tiene la carta en la mano y se ríe. Un camarero joven con delantal negro llega con dos bebidas en una bandeja. En la mesa hay raciones (patatas, croquetas y una ensalada), pan, servilletas y unas gafas de sol. Al fondo hay una sombrilla, otras mesas con gente y una fuente.", "img": "M02_oral_foto2_terraza_amigas_comer.jpg"}],
  "pautas": ["¿Cómo son las personas de la foto (físico, personalidad que cree que tienen...)? ¿Qué ropa llevan?", "¿Dónde están esas personas? ¿Qué objetos hay? Describa el lugar.", "¿Qué están haciendo las personas de la foto?", "¿Qué relación cree que hay entre ellas?", "¿Qué cree que piensan o cómo se sienten estas personas? ¿Por qué?", "¿Qué cree que han hecho antes? ¿Y qué van a hacer después?"]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1 · Un curso para los dos", "intro": "Usted y un amigo o una amiga quieren apuntarse juntos a un curso por las tardes. Hoy hablan de qué curso pueden hacer. El examinador / La examinadora es su amigo/a. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su amigo/a, tiene que hablar de:", "pautas": ["qué hace normalmente en su tiempo libre;", "si ha hecho algún curso antes: cuál, dónde y qué tal fue;", "qué curso quieren hacer y por qué;", "si prefiere las clases presenciales o por ordenador y por qué;", "qué días van a ir, cuánto pueden pagar y cuándo se apuntan."]},
  {"title": "Si eligió la fotografía 2 · ¿Dónde comemos?", "intro": "El sábado es el cumpleaños de un amigo de los dos y usted y otro amigo o amiga quieren invitarlo a comer en un restaurante. El examinador / La examinadora es su amigo/a. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su amigo/a, tiene que hablar de:", "pautas": ["qué tipo de comida le gusta y si tiene alguna alergia;", "cuál es el último restaurante donde ha comido: con quién y qué tal fue;", "qué restaurante pueden elegir y por qué;", "cuánto puede pagar cada uno y si compran también un regalo;", "a qué hora quedan y quién hace la reserva."]}]}}

# Modelos de la tarea 3 (se ven en la oral del estudiante después de la prueba y en la libreta de la profesora).
# En el diálogo, "E" = examinador y "C" = candidato. La frase del pequeño problema lleva True.
# Como en las láminas de 2022, las dos situaciones son de tú y mezclan planificar con contar cosas propias.
ORAL_MODELOS = {"t3": [
 {"titulo": "Fotografía 1 · Un curso para los dos", "trato": "tú",
  "notas": [["mi tiempo libre", "leer · andar por la playa · cine los domingos · ¿y tú?"],
            ["¿he hecho algún curso?", "fotografía, academia del centro, 3 meses, 2023 · muy útil · profesor simpático"],
            ["qué curso", "cocina o guitarra · guitarra: siempre he querido · conocer gente"],
            ["presencial o por ordenador", "presencial: hablar con la gente, preguntar · por ordenador me canso"],
            ["días, precio, apuntarse", "lunes y miércoles · máx. 50 €/mes · apuntarse esta semana, por internet"]],
  "segunda": "Si no puede los lunes ni los miércoles: buscar el grupo de los martes y jueves o los sábados por la mañana.",
  "problema": "El examinador trabaja los lunes y los miércoles por la tarde, y el curso que eligen es esos días.",
  "dialogo": [
   ["E", "¡Hola! Oye, ¿al final nos apuntamos a un curso juntos? ¿Hablamos un poco?"],
   ["C", "¡Hola! Sí, claro. Mira, yo en mi tiempo libre leo mucho y ando por la playa. Y los domingos voy al cine. ¿Y tú qué haces?"],
   ["E", "Yo, poca cosa: veo series. ¿Tú has hecho algún curso antes?"],
   ["C", "Sí, en 2023 hice un curso de fotografía en una academia del centro. Duró tres meses y fue muy útil. El profesor era muy simpático. ¿Y tú?"],
   ["E", "Yo no, nunca. ¿Y qué curso hacemos?"],
   ["C", "Pues yo siempre he querido aprender a tocar la guitarra. Y en un curso así conocemos gente. ¿Qué te parece?"],
   ["E", "¡Me encanta! ¿Y lo hacemos presencial o por ordenador?"],
   ["C", "Presencial, mejor. Así hablamos con el profesor y con los compañeros. Por ordenador me canso mucho."],
   ["E", "Vale. Pero mira, el curso del centro cívico es los lunes y los miércoles, y yo esos días trabajo por la tarde...", True],
   ["C", "¡Vaya! ¿Y hay otro grupo? Podemos ir los martes y los jueves, o los sábados por la mañana. ¿Te va bien el sábado?"],
   ["E", "El sábado, perfecto. ¿Y cuánto cuesta? ¿Cuándo nos apuntamos?"],
   ["C", "Cuesta unos cincuenta euros al mes, está bien. Nos apuntamos esta semana por internet, que hay pocas plazas. ¡Hasta luego!"]]},
 {"titulo": "Fotografía 2 · ¿Dónde comemos?", "trato": "tú",
  "notas": [["comida y alergias", "me encanta la comida italiana y la verdura · alergia al marisco · ¿y tú?"],
            ["último restaurante", "el mes pasado, mexicano, con mi hermana · muy rico, un poco caro"],
            ["qué restaurante", "pizzería del puerto: terraza, música, Javi: loco de la pizza"],
            ["dinero y regalo", "unos 30 € cada uno · regalo: una camiseta de su equipo, entre los dos"],
            ["hora y reserva", "a las dos · reservo yo por teléfono hoy"]],
  "segunda": "Si el restaurante está completo a mediodía: cenar allí el sábado por la noche o elegir otro restaurante cerca.",
  "problema": "El examinador ha llamado a la pizzería y el sábado a mediodía está completa.",
  "dialogo": [
   ["E", "¡Hola! Oye, el sábado es el cumpleaños de Javi. ¿Lo invitamos a comer? ¿Dónde vamos?"],
   ["C", "¡Hola! ¡Qué buena idea! A mí me encanta la comida italiana, y también la verdura. Pero tengo alergia al marisco. ¿Y a ti qué te gusta?"],
   ["E", "A mí me gusta todo. ¿Cuál es el último restaurante donde has comido?"],
   ["C", "El mes pasado fui a un mexicano con mi hermana. La comida era muy rica, pero un poco cara. ¿Tú has ido a algún sitio nuevo?"],
   ["E", "No, últimamente no. ¿Y qué restaurante elegimos?"],
   ["C", "¿Qué tal la pizzería del puerto? Tiene una terraza muy bonita y ponen música. Y Javi es un loco de la pizza."],
   ["E", "Perfecto. ¿Y cuánto pagamos? ¿Compramos algo más?"],
   ["C", "Unos treinta euros cada uno, más o menos. Y entre los dos, una camiseta de su equipo de fútbol. ¿Vale?"],
   ["E", "Vale. Oye, una cosa: he llamado a la pizzería y el sábado a mediodía está completa...", True],
   ["C", "¡Qué pena! ¿Y si vamos el sábado por la noche? Si tampoco hay sitio, buscamos otro restaurante en el puerto. ¿Te parece bien?"],
   ["E", "Por la noche me va bien. ¿A qué hora quedamos? ¿Quién reserva?"],
   ["C", "A las nueve, delante de la pizzería. Yo hago la reserva hoy por teléfono. ¡Hasta el sábado!"]]}]}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (un regalo): ¿Todavía tiene ese regalo? ¿Dónde lo guarda? · ¿Qué regalo hizo usted la última vez?
    Opción 2 (una fiesta): ¿Qué comida había en la fiesta? · ¿Qué ropa llevaba usted ese día?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (clase de guitarra): ¿Quién cree que es el profesor? · ¿Por qué cree que la señora aprende a tocar la guitarra?
    Foto 2 (comer fuera): ¿Por qué cree que hace una foto a la comida? · ¿Qué cree que van a pedir de postre?
  Tarea 3 — su papel: amigo/a del candidato, SIEMPRE DE TÚ (como en las láminas de 2022).
  Vaya pauta por pauta, elija las preguntas según lo que diga el candidato, improvise con sus datos y provoque UN
  pequeño problema. Esquema para la interacción:
    Foto 1 (amigo/a · un curso para los dos)
      Saludar ............. ¡Hola! ¿Al final nos apuntamos a un curso juntos? ¿Hablamos un poco?
      Tiempo libre ........ ¿Qué haces normalmente en tu tiempo libre? ¿Y los fines de semana?
      Cursos antes ........ ¿Has hecho algún curso antes? ¿Cuál? ¿Dónde? ¿Qué tal fue?
      Qué curso ........... ¿Qué curso hacemos? ¿Por qué ese?
      Presencial ......... ¿Lo hacemos presencial o por ordenador? ¿Qué prefieres? ¿Por qué?
      PEQUEÑO PROBLEMA .... «El curso es los lunes y los miércoles, y yo esos días trabajo por la tarde...».
                            Espere a que proponga algo (otro grupo, otro día, los sábados).
      Días y adiós ........ ¿Cuánto cuesta? ¿Cuándo nos apuntamos? · Vale, ¡hasta luego!
    Foto 2 (amigo/a · una comida de cumpleaños para un amigo de los dos)
      Saludar ............. ¡Hola! El sábado es el cumpleaños de Javi. ¿Lo invitamos a comer?
      Comida y alergias ... ¿Qué comida te gusta? ¿Tienes alguna alergia? ¿Hay algo que no comes?
      Último restaurante .. ¿Cuál es el último restaurante donde has comido? ¿Con quién? ¿Qué tal?
      Qué restaurante ..... ¿Qué restaurante elegimos? ¿Por qué ese?
      Dinero y regalo ..... ¿Cuánto pagamos cada uno? ¿Le compramos también un regalo? ¿Qué?
      PEQUEÑO PROBLEMA .... «He llamado al restaurante y el sábado a mediodía está completo...». Espere a que proponga
                            algo (ir por la noche, otro restaurante).
      Hora y adiós ........ ¿A qué hora quedamos? ¿Quién hace la reserva? · Vale, ¡hasta el sábado!
    El diálogo modelo de las dos situaciones está en la pestaña Oral del estudiante (se ve al abrir la prueba).
  Qué mirar en este modelo: tú coherente en toda la tarea 3; que no conteste solo sí o no (responde + detalle o
  porqué + pregunta); proponer y aceptar o rechazar con otra propuesta (¿y si...?, ¿te va bien...?); en la tarea 3,
  la pauta de experiencia en pasado (hice, duró, fue, era); en el monólogo, presente + pasado (cuando era pequeño/a +
  imperfecto, un día concreto en indefinido) + planes con ir a / querer, y la pauta que se sale de la historia
  personal (regalar dinero / una fiesta de su país para un turista); en la foto, las seis preguntas en orden,
  hay / está, estar + gerundio y «seguramente han...» / «van a...»."""
ERRORES = """  *Tú puede / *¿Usted tienes...? (mezcla tú / usted); *Cuando era pequeño, recibí muchos regalos cada Navidad
  (recibía: costumbre); *El mes pasado he ido a un mexicano (fui); *Me gusta mucho los restaurantes (me gustan);
  *Soy alérgica de marisco (al marisco); *Hay la guitarra en el suelo (la guitarra está en el suelo / hay una
  guitarra); *La señora está muy concentrado (concentrada); *Están en una terraza de un bar, comen (están comiendo,
  para la foto); *¿Quedamos en las nueve? (a las nueve); *Yo hago la reservación (la reserva); frases sueltas sin
  conectores en el monólogo («y... y... y...»)."""

# ---------------- IMÁGENES: FOTOS ----------------
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "sala de un centro cívico: una señora aprende a tocar la guitarra con un chico joven",
  "personas": "una señora y un chico joven", "edades": "ella de unos 60 años, él de unos 30",
  "aspecto": "ella con el pelo corto y blanco, gafas y un jersey morado; él con barba corta, camisa vaquera y vaqueros",
  "espacio": "interior", "lugar": "sala de un centro cívico de barrio, con sillas de plástico, una pizarra blanca y una ventana", "momento": "tarde",
  "estacion": "otoño", "tiempo": "luz de interior; fuera ya empieza a oscurecer", "gente": "solo ellos dos",
  "accion": "ella toca la guitarra y mira sus dedos con mucha atención; él, con otra guitarra en las piernas, le enseña cómo poner la mano",
  "fondo": "más sillas vacías, una pizarra blanca con unas notas de música dibujadas, una ventana",
  "objetos": "dos guitarras, un atril con una partitura, una funda de guitarra, una botella de agua, un móvil, un bolso, una chaqueta en una silla",
  "detalle": "la funda de guitarra de la señora tiene una pegatina de un grupo de rock antiguo"},
 "oral_foto2": {"situacion": "terraza de un bar en una plaza: dos amigas comen raciones y una hace fotos a los platos",
  "personas": "dos amigas y un camarero", "edades": "ellas de unos 30 años, él de unos 25",
  "aspecto": "una con el pelo rizado y una camiseta de rayas; la otra con coleta y una chaqueta vaquera; el camarero con camisa blanca y delantal negro",
  "espacio": "exterior", "lugar": "terraza de un bar en una plaza peatonal de una ciudad", "momento": "mediodía",
  "estacion": "primavera", "tiempo": "sol, con sombra de una sombrilla", "gente": "otras mesas con gente al fondo",
  "accion": "una hace una foto a los platos con el móvil y la otra se ríe con la carta en la mano; el camarero llega con dos bebidas",
  "fondo": "una sombrilla, otras mesas con gente, una fuente y los balcones de la plaza",
  "objetos": "móvil, carta, platos de patatas, croquetas y ensalada, pan, servilletas, bandeja, dos bebidas, gafas de sol",
  "detalle": "la amiga hace una foto a la comida y la otra se ríe porque tiene hambre y quiere empezar"},
 "escrita": {"situacion": "un día de nieve en un pueblo de Murcia, en tres momentos",
  "personas": "Lucía, su padre, su hermano pequeño, unos vecinos y su madre", "edades": "Lucía de unos 9 años, su hermano de unos 6, los padres de unos 40, vecinos de varias edades",
  "aspecto": "Lucía con el pelo largo y castaño y un pijama en la primera foto; después con un anorak rojo, un gorro y guantes; el padre con barba y un jersey gris",
  "espacio": "interior y exterior", "lugar": "la cocina de una casa de pueblo y la plaza del pueblo con la iglesia", "momento": "mañana, mediodía y tarde",
  "estacion": "invierno", "tiempo": "nieve: el pueblo está todo blanco", "gente": "la familia; en la plaza, unos vecinos",
  "accion": "Lucía y su padre desayunan y miran la nieve por la ventana; los niños y los vecinos hacen un muñeco de nieve; la familia toma chocolate en la cocina",
  "fondo": "la ventana con tejados blancos; la plaza con la iglesia y las casas blancas; la cocina con un radiador",
  "objetos": "tazas, tostadas, la ventana, un muñeco de nieve con bufanda y zanahoria, gorros, guantes, una olla de chocolate, el radiador",
  "detalle": "en la tercera foto los guantes mojados se secan encima del radiador"},
}
SITUACIONES_USADAS = {
 "U01": ["secretaría", "librería"], "U02": ["taquilla de cine", "museo"], "U03": ["tienda de ropa", "aeropuerto"],
 "U04": ["tienda de muebles", "piso vacío en alquiler"], "U05": ["parada de autobús de noche", "taller de bicicletas en un pueblo"],
 "U06": ["bolera", "alquiler de kayaks en una playa"],
 "U07": ["puesto de fruta y verdura en un mercado cubierto", "terraza de un bar de tapas en un pueblo"],
 "U08": ["farmacia de barrio en una tarde de invierno", "clase de yoga para mayores en un parque junto al mar"],
 "U09": ["mercadillo de antigüedades en una plaza un domingo de otoño", "tienda de fotografía de barrio en una tarde de lluvia de invierno"],
 "U10": ["llegada de una carrera popular en una ciudad una mañana de primavera", "oficina de objetos perdidos de una estación de tren en una tarde de nieve"],
 "M4T2": ["comida familiar en el campo", "sala de espera de un veterinario", "lavandería de autoservicio de noche",
          "cocina de un restaurante a mediodía", "pista de patinaje sobre hielo en Navidad", "teletrabajo en casa con niños",
          "recibidor de un piso antes de salir", "pista de pádel", "caja de un supermercado de barrio",
          "clase de baile para adultos", "amigos viendo un partido en el salón", "cafetería: regalo de cumpleaños"],
 "M01": ["mercado semanal de un pueblo de costa: una señora prueba queso en un puesto", "cocina de un piso compartido: dos compañeros limpian después de una cena"],
 "M02": ["sala de un centro cívico: una señora aprende a tocar la guitarra con un chico joven", "terraza de un bar en una plaza: dos amigas comen raciones y una hace fotos a los platos"],
 "M06": ["salón de casa: dos hermanos preparan las mochilas para la montaña", "padre e hija pintan el salón de un piso"],
 "M07": ["salón de un estudio: dos amigas buscan piso de alquiler en un portátil", "huerto urbano entre edificios: un abuelo y su nieta recogen tomates"],
}

IMG_PROMPTS = {
 "escrita": "One snowy winter day in a small village in the mountains of Murcia, Spain, where it almost never snows, in three moments. The same family in the three panels: Lucía, a girl of about 9 with long brown hair, her little brother of about 6, and her father of about 40 with a short beard and a grey jumper. Panel 1 (left): early morning in the kitchen of a village house, Lucía in pyjamas and her father sit at the table with mugs and toast and both look out of the window, amazed: the roofs outside are completely white with snow; she has her hands on the glass. Panel 2 (middle): midday in the small village square with a church and white houses, everything covered in snow, Lucía in a red anorak, woolly hat and gloves, her little brother and three neighbours of different ages build a big snowman with a scarf and a carrot nose; the brother laughs with snow on his hat. Panel 3 (right): the afternoon in the same kitchen, the whole family (Lucía, her brother, her father and her mother of about 40) drinks hot chocolate at the table; wet gloves and woolly hats are drying on the radiator under the window; a pot of chocolate on the table.",
 "oral_foto1": "A woman of about 60 with short white hair, glasses and a purple jumper, sitting on a plastic chair in a room of a neighbourhood community centre on an autumn afternoon, learning to play the classical guitar; she looks at the fingers of her left hand on the guitar neck with great concentration. Next to her, a man of about 30 with a short beard, a denim shirt and jeans, with another guitar on his lap, leans towards her and shows her how to place her hand. In front of them, a black music stand with a sheet of music. Around them: more empty plastic chairs, a whiteboard with some music notes drawn in marker, a window, a guitar case on the floor with an old rock band sticker on it, a bottle of water, a mobile phone on a chair and a handbag. Indoor ceiling light, it is getting dark outside.",
 "oral_foto2": "Two female friends of about 30 sitting at a small table on the terrace of a bar in a pedestrian square of a Spanish city at midday in spring. One has curly hair and a striped T-shirt and is taking a photo of the food with her mobile phone, holding it above the plates. The other has a ponytail and a denim jacket, holds the paper menu in her hand and laughs. A young waiter of about 25 with a white shirt and a black apron arrives with two drinks on a tray. On the table: plates of fried potatoes, croquettes and a salad, bread, paper napkins in a napkin holder and a pair of sunglasses. In the background: a big parasol, other tables with people, a stone fountain and the balconies of the square. Bright sunshine with the shade of the parasol.",
}
IMG_NAMES = {"escrita": "M02_escrita_lucia_nieve_pueblo", "oral_foto1": "M02_oral_foto1_clase_guitarra_adultos", "oral_foto2": "M02_oral_foto2_terraza_amigas_comer"}
IMG_DESC = {"escrita": "Escritura opcion 2 triptico Lucia y la nieve: 1 miran la nieve por la ventana en el desayuno, 2 munyeco de nieve en la plaza, 3 chocolate en la cocina",
            "oral_foto1": "Oral foto 1 clases para adultos: una senyora aprende a tocar la guitarra con un chico en un centro civico",
            "oral_foto2": "Oral foto 2 comer fuera: dos amigas en una terraza, una hace fotos a la comida y llega el camarero"}
CA1_DESC = {0: "Auditiva T1 ejemplo: cerveza / zumo / agua", 1: "Auditiva T1 conv 1: terraza / mesa junto a la ventana / mesa cerca de la cocina",
            2: "Auditiva T1 conv 2: flan / helado / tarta de queso", 3: "Auditiva T1 conv 3: anden 2 / anden 5 / anden 7",
            4: "Auditiva T1 conv 4: cafeteria / puerta principal / taquillas", 5: "Auditiva T1 conv 5: lunes / miercoles / viernes",
            6: "Auditiva T1 conv 6: enfrente del colegio / aparcamiento / delante de una casa"}

LECTURA = [CL1, CL2, CL3, CL4]
AUDITIVA = [CA1, CA2, CA3, CA4]
