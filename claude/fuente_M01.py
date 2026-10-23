# -*- coding: utf-8 -*-
# FUENTE DEL MODELO 1 · Curso de preparación DELE A2 (Módulo 2, modelos completos)
# Nivel: de entrada (perfil = − = −: lectura como el examen; auditiva en la parte fácil del examen; escritura como el
# examen; oral en la parte fácil del examen). "−" = la parte fácil del examen real, nunca por debajo del examen.
# Temas MEZCLADOS como en el examen real: cada tarea de un área distinta. Nunca gramática de B1.
# Se construye con:  python3 build_modelo.py fuente_M01
# Todo el contenido es original. Español de España.
M = "01"
NOMBRE = "Modelo 1"
NIVEL = "de entrada"
TITLE = "Examen completo"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress
TIEMPOS = {"lectura": 60, "auditiva": 40}
REC_LABEL = "Qué vas a encontrar en este modelo"
RECORDATORIO = [
 "Un examen completo con el formato y los tiempos del DELE A2: lectura (60 minutos), auditiva (40 minutos), escritura (45 minutos) y, en clase con tu profesora, la oral.",
 "Como en el examen, cada tarea habla de un tema distinto: un trabajo nuevo, anuncios del barrio, unas vacaciones diferentes, una árbitra de fútbol, la salud, la radio, los cambios en la rutina, una prima que vuelve de Irlanda, un profesor que recuerdas, un gato que se escapa, el mercado y las tareas de casa.",
 "Es el primer modelo del curso: la lectura y la escritura son como en el examen, y la auditiva y la oral están en la parte más amable del examen real. Es un buen punto de partida para saber dónde estás.",
 "Al terminar, en Resultados ves tu nota de cada grupo (lectura + escritura; auditiva + oral), si estás listo para presentarte, qué fichas repasar, tu control de progreso y cómo leer la nota de este modelo.",
]
TIPS_INICIO = [
 "<b>Reparte el tiempo de la lectura:</b> unos 12 minutos para la tarea 1, 15 para la 2, 15 para la 3 y 18 para la 4. Si una pregunta te bloquea, marca una opción y sigue: los errores no restan.",
 "<b>Lee primero las preguntas:</b> así sabes qué buscas en el texto. La opción que repite las mismas palabras del texto no siempre es la buena: la correcta muchas veces lo dice con otras palabras.",
 "<b>Auditiva:</b> en la tarea 1 se oyen las tres cosas de las imágenes, pero dos se descartan («no, la cabeza no», «eso era antes»). Espera al final de la conversación antes de marcar.",
 "<b>Al terminar cada prueba, apunta cuánto has tardado en cada tarea y qué te ha costado:</b> lo vas a necesitar en el control de progreso de Resultados.",
]

# Perfil del modelo frente al examen real (+ más difícil, = como el examen, - más fácil).
# Se enseña al final de Resultados, solo después de entregar (motor_modelo_extra.py, xPerfil).
PERFIL = {"pruebas": {"lectura": "=", "auditiva": "-", "escrita": "=", "oral": "-"},
 "cuando": "Este es el modelo de entrada del curso: está pensado para hacerlo al principio, para saber dónde estás.",
 "nota": "Lo que lo hacía más amable: en la auditiva, audios cortos con una sola idea, opciones falsas que se descartan con claridad y palabras muy frecuentes del A2; en la oral, temas muy cercanos (la familia, las estaciones, el mercado, la casa), fotos con una acción muy clara y una tarea 3 con un problema fácil. La lectura y la escritura tenían la dificultad del examen real. Ninguna prueba estaba por debajo del examen: solo en su parte más fácil."}
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
  "repaso": "El indefinido cuenta lo que pasó y terminó (empezó a arbitrar, se apuntó a un curso); el imperfecto describe cómo era o qué hacía antes (de pequeña jugaba con su hermano, ganaba quince euros); el perfecto habla de lo que has hecho hasta ahora (ha vendido el coche, este año he trabajado mucho). Fíjate en las palabras de tiempo: antes, ahora, ya, al principio, a los dieciséis.",
  "reto": "Escribe tres frases sobre un deporte o una afición: cómo era al principio (imperfecto), qué pasó un día (indefinido) y qué has hecho este año (perfecto).",
  "fichas": F("R01")},
 "planes": {"name": "Planes, propuestas y cambios de plan (pensaba..., al final..., ¿por qué no...?)",
  "repaso": "En el examen, muchas veces alguien dice primero lo que pensaba hacer y después lo que hace de verdad: «al principio pensaba alquilar un piso, pero...», «antes estaba ahí, pero ahora...». La respuesta buena es la última decisión. Para proponer: ¿por qué no...?, ¿quedamos...?, ¿te va bien el viernes?",
  "reto": "Escribe un mensaje a un amigo con un plan que cambia: «Al principio pensaba..., pero al final...».",
  "fichas": F("R01", "M4-3", "R13", "R08", "R14b")},
 "normas": {"name": "Normas y condiciones en anuncios y avisos (hay que, solo, prohibido, gratis)",
  "repaso": "En los anuncios, las palabras pequeñas lo cambian todo: hay que (obligación), solo, prohibido, no hay, gratis, se paga aparte. Lee la pregunta y busca solo esa condición en el texto: muchas veces la respuesta buena la dice con otras palabras (no hay bolsas de plástico = trae tu bolsa).",
  "reto": "Escribe un aviso para los vecinos de tu edificio con tres normas: algo obligatorio, algo prohibido y algo que solo se puede hacer un día.",
  "fichas": F("M0", "R14b")},
 "tiempo": {"name": "Horas, días, horarios y frecuencia (a las, de... a, los sábados, dos veces por semana)",
  "repaso": "A las + hora; de... a... para horarios; por la mañana / tarde / noche; los sábados = todos los sábados; dos veces por semana. En la auditiva, fíjate en el día y en la parte del día: el sábado por la mañana no es lo mismo que el viernes por la tarde.",
  "reto": "Escribe cinco frases sobre tu semana con: a las..., de... a..., por la tarde, los domingos, dos veces por semana.",
  "fichas": F("R06", "R14b")},
 "lugares": {"name": "Lugares y localización (hay, está, enfrente de, detrás de, al lado de)",
  "repaso": "Hay presenta algo nuevo (hay un mercado los sábados); está sitúa algo que ya conocemos (el centro de salud está enfrente del parque). Aprende bien las palabras de lugar: al lado de, enfrente de, detrás de, cerca de. Cuidado: a veces algo «antes estaba» en otro sitio.",
  "reto": "Describe en cuatro frases dónde están los sitios importantes de tu barrio: hay..., está..., enfrente de..., al lado de...",
  "fichas": F("R02", "R06", "R14a")},
 "cantidad": {"name": "Precios, descuentos y cantidades (gratis, un 20 %, incluido, muy, mucho)",
  "repaso": "Gratis / gratuito / no pagar = no cuesta dinero; un treinta por ciento de descuento; incluido = no se paga aparte. Muy va con adjetivos (muy cansado); mucho, con nombres y verbos (mucho azúcar, tose mucho). En los anuncios, mira a qué cosa se aplica el descuento o lo gratis: los sofás no son las camas.",
  "reto": "Escribe un anuncio de una tienda con tres ofertas: algo gratis, algo con descuento y algo que está incluido en el precio.",
  "fichas": F("R05", "R14a")},
 "personas": {"name": "Quién hace qué: personas, relaciones y trato (su tía, mi hermana, tú / usted)",
  "repaso": "Muchas opciones falsas cuentan lo que hace otra persona: la tía, la compañera, el hermano, la hermana de Nuria. Fíjate en los posesivos (su tía, mi hermana) y en quién es el sujeto de cada verbo. En la auditiva tarea 3, si lo hace una tercera persona, la respuesta es «ninguno de los dos».",
  "reto": "Escribe dos frases sobre lo que haces tú y dos sobre lo que hace una persona de tu familia, con posesivos (mi, su, nuestro).",
  "fichas": F("R04", "R07", "R10", "R14a")},
 "opinion": {"name": "Gustos, opiniones y sentimientos (me encanta, me da vergüenza, estoy contento)",
  "repaso": "Me gusta / me encanta + infinitivo o nombre; me da vergüenza; estar + contento, nervioso, cansado; para mí, creo que. La opinión puede cambiar con el tiempo (al principio no le gustaba; ahora le encanta): lee o escucha hasta el final.",
  "reto": "Escribe tres frases sobre algo que al principio no te gustaba y ahora sí: «Al principio..., pero ahora...».",
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
 {"g": "Oral", "t": "Tarea 1: el monólogo", "u": "DELEA2_curso_M4_T1_temas.html", "d": "Notas en palabras clave y los tiempos de cada pauta."},
 {"g": "Oral", "t": "Tarea 2: la foto", "u": "DELEA2_curso_M4_T2_foto.html", "d": "Las seis preguntas en orden y la regla de las tres frases."},
 {"g": "Oral", "t": "Tarea 3: habla con el examinador", "u": "DELEA2_curso_M4_T3_dialogos.html", "d": "Planificar con un amigo (tú) y servicio (usted), con el pequeño problema."},
 {"g": "Oral", "t": "Qué hacer si me bloqueo", "u": "DELEA2_curso_M4_bloqueo.html", "d": "Frases de rescate para no quedarte callado."},
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

# ---------------- LECTURA ----------------
CL1 = {"n": 1, "type": "mail",
 "instr": "Usted va a leer el correo electrónico que Carlos ha escrito a su amiga Inés. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Carlos habla de varias personas (su tía, su primo, una compañera): para cada pregunta, busca quién hace cada cosa y qué pasa al final.",
 "head": ["De: Carlos", "Para: Inés", "Asunto: Noticias desde Logroño"],
 "body": [
  "Querida Inés:",
  "¿Qué tal por Granada? Perdona por no escribirte antes, pero estas semanas han sido una locura. Como sabes, en septiembre empecé a trabajar de profesor de música en un colegio de Logroño. ¡Por fin tengo un trabajo fijo!",
  "Al principio pensaba alquilar un piso en el centro, pero los precios son muy altos y además todavía no conozco bien la ciudad. Así que, de momento, vivo con mi tía Rosario, la hermana de mi madre. Tiene una casa grande cerca del río y me ha dejado la habitación de mi primo, que ahora estudia en Zaragoza. En enero quiero buscar algo para mí solo.",
  "El colegio me encanta. Doy clase a niños de seis a doce años, de nueve a cinco, con una hora para comer. Mis compañeros son muy simpáticos, sobre todo Lola, la profesora de inglés, que vive en mi calle y me lleva en coche todas las mañanas. Mis alumnos aprenden a tocar la flauta y algunos ya cantan muy bien. Los viernes por la tarde ensayamos con el coro del colegio, y eso es lo que más me gusta. Lo único difícil es el ruido: ¡imagínate treinta niños con tambores!",
  "Te escribo también por otra cosa. El 18 de diciembre mis alumnos dan su primer concierto de Navidad en el salón de actos del colegio, a las seis de la tarde. ¿Por qué no vienes ese fin de semana? Puedes dormir en casa de mi tía: ella ya lo sabe y está encantada. El sábado te enseño la ciudad y vamos de tapas a la calle Laurel.",
  "Escríbeme pronto y dime algo.",
  "Un abrazo muy fuerte,<br>Carlos"],
 "items": [
  {"n": 1, "q": "Carlos escribe a Inés para...", "o": ["contarle su nueva vida e invitarla.", "pedirle ayuda para buscar un piso.", "presentarle a su tía Rosario."], "ok": 0,
   "cats": ["planes", "personas"], "es": "ES-02", "pc": "estas semanas... · te escribo también por otra cosa · ¿por qué no vienes?",
   "why": "Carlos le cuenta su trabajo nuevo y dónde vive, y la invita al concierto de sus alumnos. No le pide ayuda con el piso, y a su tía solo la nombra."},
  {"n": 2, "q": "Ahora Carlos vive...", "o": ["en un piso del centro.", "en casa de una familiar.", "con su primo en Zaragoza."], "ok": 1,
   "cats": ["planes", "lugares"], "es": "ES-05", "pc": "al principio pensaba alquilar..., pero... así que, de momento, vivo con mi tía",
   "why": "De momento vive con su tía Rosario: una familiar. El piso del centro era su primera idea, y el primo es el que estudia en Zaragoza."},
  {"n": 3, "q": "Lola...", "o": ["es la tía de Carlos.", "enseña música en el colegio.", "lleva a Carlos al trabajo."], "ok": 2,
   "cats": ["personas"], "es": "ES-08", "pc": "Lola, la profesora de inglés, que... me lleva en coche",
   "why": "Lola lleva a Carlos en coche al colegio todas las mañanas. Es profesora de inglés, no de música, y la tía se llama Rosario."},
  {"n": 4, "q": "Según el correo, en el colegio...", "o": ["Carlos trabaja solo por las mañanas.", "los alumnos aprenden a tocar un instrumento.", "trabajan treinta profesores."], "ok": 1,
   "cats": ["tiempo", "cantidad"], "es": "ES-03", "pc": "aprenden a tocar la flauta = un instrumento · de nueve a cinco · treinta niños",
   "why": "Los alumnos aprenden a tocar la flauta, un instrumento. Carlos trabaja de nueve a cinco, y los treinta son niños, no profesores."},
  {"n": 5, "q": "Carlos le propone a Inés...", "o": ["ir al concierto y dormir en casa de su tía.", "alquilar juntos un piso en enero.", "cantar en el concierto de Navidad."], "ok": 0,
   "cats": ["planes"], "es": "ES-01", "pc": "¿por qué no vienes ese fin de semana? Puedes dormir en casa de mi tía",
   "why": "La invita al concierto y le ofrece dormir en casa de su tía. En enero Carlos quiere buscar un piso para él solo, y en el concierto cantan sus alumnos."},
 ]}

CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 15 minutos: menos de dos minutos por anuncio. Lee la pregunta primero y busca solo ese dato. La opción buena muchas veces dice lo mismo que el anuncio con otras palabras.",
 "example": {"title": "BIBLIOTECA DEL BARRIO · INTERCAMBIO DE JUGUETES",
   "body": "¿Tus hijos ya no juegan con algunos juguetes? El sábado 12, de diez a una, organizamos un intercambio en la sala infantil. Trae un juguete en buen estado y llévate otro. No aceptamos juguetes rotos ni videojuegos. Los juguetes que sobran los regalamos a una asociación del barrio. La entrada es libre. ¡Te esperamos!",
   "q": "En el intercambio...", "o": ["se pueden cambiar videojuegos.", "los juguetes tienen que estar bien.", "hay que pagar una entrada."], "ok": 1,
   "why": "La opción correcta es la B porque solo aceptan juguetes en buen estado."},
 "items": [
  {"n": 6, "title": "POLIDEPORTIVO MUNICIPAL · CAMPAMENTO URBANO DE VERANO",
   "body": "Para niños y niñas de cuatro a doce años. Del 1 al 31 de julio, de lunes a viernes, de 9:00 a 14:00. Juegos, piscina, talleres y excursiones. Precio: 60 € a la semana. La comida no está incluida: si tu hijo se queda a comer, son 5 € más al día. Cada niño tiene que traer una gorra y una botella de agua. Inscripciones hasta el 15 de junio.",
   "q": "En el campamento...", "o": ["la comida está incluida en el precio.", "los niños tienen que llevar algo para el sol.", "pueden participar niños de quince años."], "ok": 1,
   "cats": ["normas", "cantidad"], "es": "ES-03", "pc": "tiene que traer una gorra = algo para el sol · no está incluida",
   "why": "Cada niño tiene que llevar una gorra, es decir, algo para el sol. La comida se paga aparte, y el campamento es para niños de cuatro a doce años."},
  {"n": 7, "title": "ESCUELA DE MÚSICA DO RE MI · CLASES PARA ADULTOS",
   "body": "¿Siempre has querido tocar un instrumento? Ofrecemos clases de guitarra, piano y batería para adultos, en grupos de cuatro personas. Las clases son de lunes a jueves, por la tarde. La matrícula cuesta 30 € y la primera clase es gratis: ven, prueba y decide. No hace falta tener instrumento: en la escuela te prestamos uno.",
   "q": "En esta escuela...", "o": ["la primera clase no se paga.", "hay clases los viernes.", "las clases son individuales."], "ok": 0,
   "cats": ["cantidad", "tiempo"], "es": "ES-03", "pc": "la primera clase es gratis = no se paga · de lunes a jueves · grupos de cuatro",
   "why": "La primera clase es gratis. Las clases son de lunes a jueves, y en grupos de cuatro personas, no individuales."},
  {"n": 8, "title": "CORREOS · OFICINA DE LA PLAZA MAYOR · HORARIO DE AGOSTO",
   "body": "Durante el mes de agosto, nuestra oficina abre de lunes a viernes de 8:30 a 14:30. Por la tarde y los sábados, la oficina está cerrada. Si no puedes venir, puedes recoger tus paquetes las veinticuatro horas en el punto de recogida de la estación de tren. En septiembre volvemos al horario normal.",
   "q": "En agosto, en esta oficina...", "o": ["se puede ir por la tarde.", "abren también los sábados.", "solo atienden por la mañana."], "ok": 2,
   "cats": ["tiempo", "normas"], "es": "ES-06", "pc": "de 8:30 a 14:30 · por la tarde y los sábados, cerrada",
   "why": "En agosto la oficina solo abre por la mañana, de ocho y media a dos y media. Por la tarde y los sábados está cerrada."},
  {"n": 9, "title": "COMUNIDAD DE VECINOS · CALLE OLMO, 14 · OBRAS EN EL ASCENSOR",
   "body": "Del 3 al 14 de noviembre cambiamos el ascensor y no va a funcionar. Sentimos las molestias. Los vecinos mayores que necesitan ayuda para subir la compra pueden hablar con Julián, el portero, por las mañanas. Recordamos que está prohibido dejar bicicletas y carros en el portal. Gracias por vuestra paciencia.",
   "q": "Durante las obras...", "o": ["el portero puede ayudar a algunos vecinos.", "el ascensor funciona por las mañanas.", "se pueden dejar las bicicletas en el portal."], "ok": 0,
   "cats": ["normas", "personas"], "es": "ES-04", "pc": "pueden hablar con Julián, el portero · por las mañanas · prohibido",
   "why": "Los vecinos mayores pueden pedir ayuda al portero. «Por las mañanas» es el horario del portero, no del ascensor, y las bicis están prohibidas en el portal."},
  {"n": 10, "title": "MERCADO ECOLÓGICO DE LOS SÁBADOS · PLAZA DE LA FUENTE",
   "body": "Todos los sábados, de 9:00 a 14:00, frutas, verduras, pan y quesos de los productores de la comarca. Trae tu bolsa o tu cesta: en el mercado no hay bolsas de plástico. Este mes, a las doce, hay talleres de cocina para niños con los productos del mercado. Son gratuitos, pero las plazas son pocas y hay que reservar en el puesto de información.",
   "q": "En el mercado...", "o": ["dan bolsas de plástico.", "los talleres para niños cuestan dinero.", "hay que reservar para los talleres."], "ok": 2,
   "cats": ["normas", "cantidad"], "es": "ES-06", "pc": "no hay bolsas de plástico · gratuitos, pero hay que reservar",
   "why": "Los talleres son gratis, pero hay que reservar. En el mercado no hay bolsas de plástico."},
  {"n": 11, "title": "FERIA DEL LIBRO · PASEO DEL PARQUE",
   "body": "Del 25 de abril al 4 de mayo, más de cuarenta librerías de la ciudad te esperan en el paseo del parque. Todos los libros tienen un 10 % de descuento. Los fines de semana, por la tarde, algunos escritores firman sus libros en las casetas. Abierto todos los días de 11:00 a 14:00 y de 17:00 a 21:00.",
   "q": "En la feria...", "o": ["los libros son más baratos.", "los escritores están todos los días.", "solo abren por la tarde."], "ok": 0,
   "cats": ["cantidad", "tiempo"], "es": "ES-03", "pc": "un 10 % de descuento = más baratos · los fines de semana · de 11 a 14 y de 17 a 21",
   "why": "Todos los libros tienen un diez por ciento de descuento: son más baratos. Los escritores van solo los fines de semana, y la feria abre por la mañana y por la tarde."},
  {"n": 12, "title": "BAR EL RINCÓN · MENÚ DEL DÍA",
   "body": "De lunes a viernes, menú del día por 12 €: primer plato, segundo plato, postre o café, pan y bebida. Los sábados, menú especial con arroz por 16 €. Los domingos, cerrado. ¿Tienes prisa? Te preparamos el menú para llevar por solo 1 € más. Reservas para grupos en el teléfono del bar.",
   "q": "Según el anuncio...", "o": ["el bar abre los domingos.", "el menú del día incluye la bebida.", "el menú del sábado cuesta lo mismo."], "ok": 1,
   "cats": ["cantidad", "normas"], "es": "ES-01", "pc": "primer plato, segundo plato, postre o café, pan y bebida · 16 €",
   "why": "El menú del día incluye la bebida. Los domingos el bar está cerrado, y el menú del sábado cuesta dieciséis euros, no doce."},
  {"n": 13, "title": "SE VENDE BICICLETA DE MONTAÑA",
   "body": "Vendo mi bicicleta de montaña: tiene tres años, pero casi no la he usado y está como nueva. Nueva costó 400 €; la vendo por 150 €. Con la bici regalo el casco y las luces. No la envío: hay que venir a buscarla a mi casa, en el barrio de San Blas. Llamar por las tardes a Óscar.",
   "q": "Óscar...", "o": ["manda la bici a casa del comprador.", "da algunas cosas gratis con la bici.", "usa la bici todos los días."], "ok": 1,
   "cats": ["cantidad", "personas"], "es": "ES-03", "pc": "con la bici regalo el casco y las luces = da cosas gratis · no la envío · casi no la he usado",
   "why": "Con la bici regala el casco y las luces. No la envía: hay que ir a buscarla, y casi no la ha usado."},
 ]}

CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos de tres personas que cuentan unas vacaciones diferentes. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 15 minutos. Lee primero las seis preguntas. Las tres personas cuentan unas vacaciones: busca el detalle que las separa (dónde durmieron, cuánto pagaron, qué problema tuvieron, quién las ayudó).",
 "texts": [
  {"name": "Lorena", "body": "El verano pasado alquilamos una casa rural en un pueblo de Galicia, mi marido, nuestros dos hijos y yo. Allí no había cobertura ni internet. El primer día los niños estaban enfadados y yo también, porque no podía mirar el correo del trabajo. Pero después todo cambió: por las mañanas caminábamos por el bosque y por las tardes jugábamos a las cartas. Llovió tres días seguidos, pero no importaba: leíamos al lado de la chimenea. Los dueños tenían vacas y mis hijos los ayudaban a darles de comer. Ha sido el mejor verano de mi vida y ya hemos reservado la misma casa para el año que viene."},
  {"name": "Iván", "body": "Este año mi mujer, mi hija y yo hicimos un intercambio de casa con una familia de Lyon. Ellos vivieron un mes en nuestro piso de Valencia y nosotros, en su casa. Así no pagamos nada por el alojamiento, solo el viaje. La casa tenía un jardín pequeño y nos dejaron sus bicicletas para ir al centro, que estaba a diez minutos. Los vecinos, muy simpáticos, nos invitaron a cenar dos veces en su terraza. El único problema fue el idioma: yo hablo muy poco francés, así que mi hija, que lo estudia en el instituto, nos traducía todo. Ahora seguimos en contacto con la familia francesa."},
  {"name": "Pilar", "body": "En agosto fui de camping a Asturias con dos amigas, en la caravana vieja de mis padres. Fue la primera vez que conduje una caravana y al principio estaba muy nerviosa. Estuvimos diez días: unos días en la montaña, cerca de unos lagos, y otros en la playa. Cocinábamos siempre fuera, en una mesa de camping, y comíamos con unas vistas preciosas al mar o a las montañas. El último día, cuando volvíamos a casa, la caravana se rompió en una carretera pequeña. Un agricultor nos ayudó con su tractor y nos llevó hasta un taller. Fue un buen susto, pero ahora nos reímos mucho cuando lo recordamos."}],
 "items": [
  {"n": 14, "q": "¿Quién no gastó dinero en el lugar donde dormía?", "ok": 1, "cats": ["cantidad"], "es": "ES-03", "pc": "no pagamos nada por el alojamiento",
   "why": "Iván hizo un intercambio de casa y no pagó por el alojamiento. Lorena alquiló una casa, y Pilar fue en la caravana de sus padres, pero en un camping."},
  {"n": 15, "q": "¿Quién no pudo usar el móvil ni el ordenador?", "ok": 0, "cats": ["lugares"], "es": "ES-03", "pc": "no había cobertura ni internet",
   "why": "En la casa rural de Lorena no había cobertura ni internet."},
  {"n": 16, "q": "¿Quién tuvo una avería en el viaje de vuelta?", "ok": 2, "cats": ["pasados"], "es": "ES-03", "pc": "cuando volvíamos a casa, la caravana se rompió",
   "why": "La caravana de Pilar se rompió el último día, cuando volvían a casa."},
  {"n": 17, "q": "¿Quién necesitó ayuda para entenderse con otras personas?", "ok": 1, "cats": ["personas"], "es": "ES-08", "pc": "hablo muy poco francés, así que mi hija nos traducía",
   "why": "Iván habla poco francés y su hija les traducía todo. Pilar también recibió ayuda, pero con la caravana, no con el idioma."},
  {"n": 18, "q": "¿Quién va a volver al mismo sitio?", "ok": 0, "cats": ["planes"], "es": "ES-07", "pc": "ya hemos reservado la misma casa para el año que viene",
   "why": "Lorena ya ha reservado la misma casa para el año que viene. Iván sigue en contacto con la familia francesa, pero no dice que vaya a volver."},
  {"n": 19, "q": "¿Quién comía al aire libre?", "ok": 2, "cats": ["lugares", "pasados"], "es": "ES-09", "pc": "cocinábamos siempre fuera, en una mesa de camping",
   "why": "Pilar y sus amigas cocinaban y comían fuera, en una mesa de camping. Iván tenía un jardín, pero no dice que comieran allí."}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un reportaje sobre una árbitra de fútbol. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto: cada párrafo responde, más o menos, a una pregunta. Atención a cómo era antes y cómo es ahora, y a quién hace cada cosa (Sandra, su hermano, sus padres).",
 "title": "Sandra, árbitra: «En el campo, yo decido»",
 "sub": "Revista «Deporte y barrio» · Gente que inspira",
 "body": [
  "Todos los domingos a las ocho de la mañana, Sandra Molina, de veinticuatro años, prepara su mochila: el silbato, dos tarjetas, una amarilla y una roja, un reloj y unas botas negras. No es jugadora: es árbitra de fútbol. Este año arbitra partidos de Tercera División y, entre semana, trabaja de enfermera en un hospital de Castellón. Hoy le toca un partido en un pueblo a una hora de su casa.",
  "De pequeña, Sandra jugaba al fútbol con su hermano Jorge y sus amigos en la plaza del pueblo. «Yo era la única niña y siempre me ponían de portera», recuerda riéndose. A los doce años entró en el equipo del colegio, pero no era muy buena: corría mucho, pero casi nunca marcaba goles. Su madre, en cambio, quería verla en clases de baile.",
  "Todo cambió a los dieciséis años. Un día el árbitro de un partido de su hermano no llegó y el entrenador le pidió ayuda a ella. «Me dio mucha vergüenza, pero lo hice y me encantó», cuenta. Esa misma semana se apuntó a un curso de árbitros. Sus padres al principio no estaban muy contentos: pensaban que era un mundo difícil para una chica.",
  "Los primeros años arbitró partidos de niños los sábados por la mañana. Ganaba quince euros por partido y volvía a casa en autobús. Muchas veces llovía y llegaba a casa con las botas llenas de barro. Lo más difícil no eran los jugadores, sino algunos padres que gritaban desde la grada. «Una vez un señor me gritó durante todo el partido. Al final, vino a pedirme perdón», dice.",
  "Ahora entrena cinco días a la semana: corre por la playa antes de ir al hospital y dos tardes hace ejercicios en el gimnasio. Cada mes tiene que pasar un examen físico y un examen de las reglas del juego. También mira los vídeos de sus partidos con un entrenador para ver sus errores. Los sábados por la noche se acuesta pronto, porque los partidos empiezan muy temprano.",
  "Su sueño es arbitrar en Primera División. Todavía hay pocas mujeres árbitras en España, pero cada año hay más. «Quiero demostrar que una mujer puede llegar arriba», dice. Los sábados por la tarde, Sandra da clases gratis a chicas de su pueblo que quieren ser árbitras. Y su hermano Jorge, que ya no juega, es ahora su mayor fan: no se pierde ningún partido."],
 "items": [
  {"n": 20, "q": "Según el texto, Sandra...", "o": ["juega en un equipo de Tercera División.", "tiene otro trabajo además del fútbol.", "trabaja los domingos en un hospital."], "ok": 1,
   "cats": ["personas", "tiempo"], "es": "ES-04", "pc": "no es jugadora · entre semana, trabaja de enfermera",
   "why": "Además de arbitrar, trabaja de enfermera. No juega: arbitra partidos de Tercera, y en el hospital trabaja entre semana, no los domingos."},
  {"n": 21, "q": "Cuando era pequeña, Sandra...", "o": ["era la mejor jugadora del colegio.", "jugaba con chicos.", "marcaba muchos goles."], "ok": 1,
   "cats": ["pasados"], "es": "ES-03", "pc": "yo era la única niña · no era muy buena · casi nunca marcaba goles",
   "why": "Era la única niña: jugaba con su hermano y sus amigos. No era muy buena y casi nunca marcaba goles."},
  {"n": 22, "q": "Sandra empezó a arbitrar porque...", "o": ["un día no llegó el árbitro de un partido.", "sus padres se lo aconsejaron.", "su hermano también era árbitro."], "ok": 0,
   "cats": ["pasados", "personas"], "es": "ES-08", "pc": "el árbitro no llegó y el entrenador le pidió ayuda · sus padres no estaban contentos",
   "why": "El árbitro de un partido de su hermano no llegó y el entrenador le pidió ayuda. Sus padres, al principio, no estaban contentos, y su hermano era jugador."},
  {"n": 23, "q": "En sus primeros años como árbitra, Sandra...", "o": ["tuvo problemas con algunas personas del público.", "arbitraba partidos de adultos.", "iba a los partidos en coche."], "ok": 0,
   "cats": ["pasados", "lugares"], "es": "ES-03", "pc": "algunos padres que gritaban desde la grada",
   "why": "Lo más difícil eran algunos padres que gritaban desde la grada, es decir, el público. Arbitraba partidos de niños y volvía en autobús."},
  {"n": 24, "q": "Ahora, Sandra...", "o": ["entrena solo en el gimnasio.", "hace exámenes con frecuencia.", "corre por la tarde, después del hospital."], "ok": 1,
   "cats": ["tiempo"], "es": "ES-03", "pc": "cada mes tiene que pasar un examen = con frecuencia · corre antes de ir al hospital",
   "why": "Cada mes pasa un examen físico y otro de las reglas: hace exámenes con frecuencia. Corre por la playa antes del hospital, y el gimnasio es solo dos tardes."},
  {"n": 25, "q": "Según el último párrafo, Jorge...", "o": ["sigue jugando al fútbol.", "da clases a chicas del pueblo.", "va a ver los partidos de su hermana."], "ok": 2,
   "cats": ["personas", "opinion"], "es": "ES-08", "pc": "ya no juega · no se pierde ningún partido · Sandra da clases",
   "why": "Jorge no se pierde ningún partido de Sandra. Ya no juega, y las clases a las chicas las da Sandra."},
 ]}

# ---------------- AUDITIVA ----------------
# Sin efectos de sonido (como el examen real). Cada intervención empieza con una etiqueta de emoción de ElevenLabs v3
# (en inglés, entre corchetes): va al guion, no a las transcripciones.
# Perfil "−": audios en la parte baja de la extensión oficial, una sola idea por audio, distractores que se descartan
# con claridad, palabras muy frecuentes del A2 y pocas paráfrasis.
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación: las tres aparecen en el audio, pero dos se descartan («no, la cabeza no», «antes estaba ahí»). Escucha hasta el final antes de marcar.",
 "example": {"q": "¿Qué le duele a la mujer?", "o": ["la cabeza", "la garganta", "la espalda"], "ok": 1,
   "pres": "Va a escuchar a una mujer que habla con su médico.",
   "lines": [("Hombre", "DANIEL_ES", "[calm] Buenos días, Ana. Siéntese. ¿Qué le pasa? ¿Le duele la cabeza otra vez?"),
             ("Mujer", "FIONA", "[tired] No, la cabeza no. Ahora me duele mucho la garganta. No puedo hablar bien y tengo un poco de fiebre."),
             ("Hombre", "DANIEL_ES", "[kind] Vale, ahora le miro la garganta. ¿Y la espalda? ¿Está mejor?"),
             ("Mujer", "FIONA", "[relieved] Sí, la espalda ya está bien, gracias. Ya no me duele nada.")],
   "solucion": "La opción correcta es la letra be. Le duele la garganta.",
   "img": "M01_CA1_0_cabeza_garganta_espalda.jpg",
   "prompt": "Panel 1: a woman holding her head with both hands (headache). Panel 2: a woman touching her throat (sore throat). Panel 3: a woman holding her lower back (back pain)."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Qué compra el hombre en la farmacia?", "o": ["un jarabe", "unas pastillas", "una crema para el sol"], "ok": 0,
   "cats": ["personas", "cantidad"], "es": "ES-04", "pc": "para niños, mejor un jarabe · las pastillas son para adultos · crema no",
   "pres": "Va a escuchar a un hombre que está en una farmacia.",
   "lines": [("Hombre", "MARIO", "[polite] Buenas tardes. Quería algo para la tos. Mi hijo tose mucho por la noche."),
             ("Mujer", "LYDIA", "[friendly] ¿Cuántos años tiene? Para niños es mejor un jarabe. Las pastillas son para adultos."),
             ("Hombre", "MARIO", "[thoughtful] Tiene seis años. Vale, el jarabe. Y crema para el sol no, que ya tengo en casa."),
             ("Mujer", "LYDIA", "[friendly] Muy bien. Una cucharada después de cenar.")],
   "why": "Compra un jarabe para la tos de su hijo. Las pastillas son para adultos, y la crema para el sol ya la tiene en casa.",
   "img": "M01_CA1_1_jarabe_pastillas_crema.jpg", "prompt": "Panel 1: a small bottle of cough syrup with a measuring spoon. Panel 2: a blister pack of pills. Panel 3: a tube of sun cream."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Dónde está ahora el centro de salud?", "o": ["al lado de la farmacia", "enfrente del parque", "detrás del mercado"], "ok": 1,
   "cats": ["lugares", "pasados"], "es": "ES-07", "pc": "antes estaba ahí, pero ahora está enfrente del parque",
   "pres": "Va a escuchar a una chica que pregunta a un señor por la calle.",
   "lines": [("Mujer", "SARA_JOVEN", "[polite] Perdone, ¿el centro de salud está al lado de la farmacia?"),
             ("Hombre", "VOLU", "[helpful] No, no. Antes estaba ahí, pero ahora está enfrente del parque, en un edificio nuevo."),
             ("Mujer", "SARA_JOVEN", "[curious] ¿El parque que está detrás del mercado?"),
             ("Hombre", "VOLU", "[helpful] Sí, ese. Pasa por el mercado y lo ve enseguida. Son cinco minutos andando, más o menos."),
             ("Mujer", "SARA_JOVEN", "[relieved] ¡Ah, vale! Muchas gracias.")],
   "why": "Ahora está enfrente del parque. Al lado de la farmacia estaba antes, y detrás del mercado está el parque, no el centro de salud.",
   "img": "M01_CA1_2_farmacia_parque_mercado.jpg", "prompt": "Panel 1: a small health centre building next to a pharmacy with a green cross. Panel 2: a small health centre building opposite a park with trees and benches. Panel 3: a small health centre building behind a covered market."},
  {"n": 3, "conv": "Conversación tres", "q": "¿Qué desayuna ahora Óscar?", "o": ["galletas", "tostadas", "fruta"], "ok": 2,
   "cats": ["pasados", "opinion"], "es": "ES-07", "pc": "¿ya no comes galletas? No, ya no · esas tampoco · ahora, fruta",
   "pres": "Va a escuchar a dos compañeros que hablan en el trabajo.",
   "lines": [("Mujer", "AITANA", "[surprised] ¡Óscar! ¿Fruta para desayunar? ¿Ya no comes galletas con el café?"),
             ("Hombre", "DANI", "[proud] No, ya no. El mes pasado el médico me dijo que como mucho azúcar. Así que ahora desayuno fruta todos los días."),
             ("Mujer", "AITANA", "[teasing] ¿Y las tostadas con mantequilla?"),
             ("Hombre", "DANI", "[laughs] Esas tampoco. Ahora, fruta y un café con leche. ¡Y me siento muy bien!")],
   "why": "Ahora desayuna fruta todos los días. Las galletas eran antes, y las tostadas con mantequilla tampoco las come.",
   "img": "M01_CA1_3_galletas_tostadas_fruta.jpg", "prompt": "Panel 1: a plate of biscuits next to a cup of coffee. Panel 2: two slices of toast with butter. Panel 3: a bowl of chopped fruit."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Qué le va a llevar la mujer a su amiga?", "o": ["flores", "un libro", "bombones"], "ok": 1,
   "cats": ["planes", "normas"], "es": "ES-05", "pc": "no dejan entrar flores · no puede comer dulces · mejor le llevo un libro",
   "pres": "Va a escuchar a una mujer que habla por teléfono con su marido.",
   "lines": [("Mujer", "MARINA_ES", "[thoughtful] Oye, Pablo, esta tarde voy al hospital a ver a Carmen, que ya está mejor. ¿Le llevo unas flores?"),
             ("Hombre", "LUIS_VEGA", "[calm] En el hospital no dejan entrar flores. ¿Y unos bombones?"),
             ("Mujer", "MARINA_ES", "[doubtful] No puede comer dulces... Mejor le llevo un libro. Le encantan las novelas."),
             ("Hombre", "LUIS_VEGA", "[warm] Muy buena idea. Dale un beso de mi parte. Yo voy a verla el sábado.")],
   "why": "Le va a llevar un libro. En el hospital no dejan entrar flores, y Carmen no puede comer dulces.",
   "img": "M01_CA1_4_flores_libro_bombones.jpg", "prompt": "Panel 1: a bunch of flowers. Panel 2: a paperback novel. Panel 3: a box of chocolates."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Cómo va el señor al fisioterapeuta?", "o": ["andando", "en autobús", "en taxi"], "ok": 0,
   "cats": ["planes", "opinion"], "es": "ES-05", "pc": "¿le pido un taxi? No, gracias · voy andando · puede coger el autobús",
   "pres": "Va a escuchar a dos vecinos que hablan en el portal.",
   "lines": [("Mujer", "SARA_2", "[friendly] Buenos días, Antonio. ¿Va al fisio? ¿Le pido un taxi? Hoy hace mucho frío."),
             ("Hombre", "SANTIAGO_ES", "[cheerful] No, gracias, hija. El fisio me ha dicho que tengo que caminar. Voy andando: está a diez minutos de aquí."),
             ("Mujer", "SARA_2", "[worried] ¿Y si llueve? Puede coger el autobús. La parada está aquí al lado."),
             ("Hombre", "SANTIAGO_ES", "[cheerful] Si llueve, llevo paraguas. ¡Hasta luego!")],
   "why": "Va andando, porque el fisio le ha dicho que tiene que caminar. El taxi y el autobús son ideas de la vecina.",
   "img": "M01_CA1_5_andando_autobus_taxi.jpg", "prompt": "Panel 1: an older man walking on a pavement. Panel 2: a city bus at a bus stop. Panel 3: a taxi on a street."},
  {"n": 6, "conv": "Conversación seis", "q": "¿Qué le recomienda la médica al chico?", "o": ["correr", "hacer yoga", "nadar"], "ok": 2,
   "cats": ["opinion", "tiempo"], "es": "ES-04", "pc": "correr no es bueno · el yoga está bien, pero... · lo mejor es nadar",
   "pres": "Va a escuchar a un chico que habla con su médica.",
   "lines": [("Mujer", "TATIANA", "[calm] Bueno, Jorge, tus análisis están bien. Para tu espalda correr no es bueno. Y el yoga está bien, pero..."),
             ("Hombre", "OSCAR", "[curious] ¿Entonces qué hago? ¿Nada?"),
             ("Mujer", "TATIANA", "[encouraging] Lo mejor es nadar. Dos o tres veces por semana, en la piscina del barrio. Y nada de correr, ¿eh?"),
             ("Hombre", "OSCAR", "[relieved] Vale. Me gusta mucho el agua, así que perfecto.")],
   "why": "La médica le dice que lo mejor es nadar. Correr no es bueno para su espalda, y del yoga no dice que lo haga.",
   "img": "M01_CA1_6_correr_yoga_nadar.jpg", "prompt": "Panel 1: a young man running in a park. Panel 2: a young man doing yoga on a mat. Panel 3: a young man swimming in a pool."},
 ]}

CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. En cada audio, busca solo el dato que te preguntan: el día, el precio, lo que es gratis o lo que hay que llevar.",
 "example": {"q": "En este programa...", "o": ["ponen las canciones que piden los oyentes.", "dan las noticias de la mañana.", "hablan de deporte."], "ok": 0,
   "why": "La opción correcta es la A porque los oyentes llaman y piden su canción favorita.",
   "lab": "Locutor", "voice": "SERGIO/RADIO",
   "text": "[warm] Buenas tardes. Son las cuatro y empieza «Tarde de música», con las canciones que vosotros pedís. Hoy también hablamos con un grupo joven de la ciudad que acaba de grabar su primer disco. Llamadnos por teléfono y pedid vuestra canción favorita. ¡Os esperamos!",
   "solucion": "La opción correcta es la letra a, porque los oyentes llaman y piden su canción favorita."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "La piscina municipal...", "o": ["abre por la mañana y por la tarde.", "cierra los domingos.", "es gratis para todos los niños."], "ok": 0,
   "cats": ["tiempo", "cantidad"], "es": "ES-03", "pc": "de once de la mañana a ocho de la tarde · todos los días · menores de cinco años",
   "lab": "Locutor", "voice": "BOBBY/RADIO",
   "text": "[cheerful] ¡Ya llega el calor! La piscina municipal abre el sábado uno de junio. Este año abre todos los días, de once de la mañana a ocho de la tarde. La entrada cuesta tres euros, y los niños menores de cinco años entran gratis. ¡Os esperamos!",
   "why": "Abre de once de la mañana a ocho de la tarde: por la mañana y por la tarde. Abre todos los días, y solo entran gratis los menores de cinco años."},
  {"n": 8, "conv": "Audio 2", "q": "En el colegio San Jorge...", "o": ["recogen botellas de plástico.", "se pueden llevar los tapones por la mañana.", "recogen tapones el fin de semana."], "ok": 1,
   "cats": ["normas", "tiempo"], "es": "ES-06", "pc": "de lunes a viernes, por la mañana · no traigáis botellas, solo los tapones",
   "lab": "Locutora", "voice": "TAMARA/RADIO",
   "text": "[warm] El colegio San Jorge recoge tapones de plástico para ayudar a una niña del barrio. Podéis traerlos a la entrada del colegio, de lunes a viernes, por la mañana. No traigáis botellas, solo los tapones. ¡Muchas gracias por vuestra ayuda!",
   "why": "Se pueden llevar los tapones de lunes a viernes, por la mañana. No recogen botellas, y el fin de semana no recogen."},
  {"n": 9, "conv": "Audio 3", "q": "En la tienda de muebles...", "o": ["las camas tienen descuento.", "no se paga por llevar los muebles a casa.", "abren todos los días."], "ok": 1,
   "cats": ["cantidad", "normas"], "es": "ES-03", "pc": "el transporte a casa es gratis · los sofás tienen descuento · de lunes a sábado",
   "lab": "Locutor", "voice": "JAVI_ROJAS/RADIO",
   "text": "[enthusiastic] ¡Rebajas en Muebles Casa Bonita! Este mes, todos los sofás tienen un treinta por ciento de descuento. Y si compras una cama, te regalamos la almohada. El transporte a casa es gratis. Estamos en la carretera de Valencia, abiertos de lunes a sábado.",
   "why": "El transporte a casa es gratis. El descuento es para los sofás (con la cama regalan la almohada), y los domingos no abren."},
  {"n": 10, "conv": "Audio 4", "q": "Según la radio, el domingo...", "o": ["va a hacer más calor.", "va a hacer sol por la tarde.", "va a llover."], "ok": 2,
   "cats": ["tiempo"], "es": "ES-07", "pc": "el sábado, sol y calor · el domingo llega la lluvia",
   "lab": "Locutor", "voice": "ENRIQUE/RADIO",
   "text": "[calm] Y ahora, el tiempo para el fin de semana. El sábado va a hacer sol y calor, con temperaturas de hasta treinta grados. Pero el domingo llega la lluvia, sobre todo por la tarde. Si vais a la playa, mejor el sábado.",
   "why": "El domingo llega la lluvia. El sol y el calor son del sábado."},
  {"n": 11, "conv": "Audio 5", "q": "En la academia Palabras...", "o": ["solo hay clases por la mañana.", "se puede probar una semana sin pagar.", "los cursos empiezan en junio."], "ok": 1,
   "cats": ["cantidad", "tiempo"], "es": "ES-03", "pc": "si no te gusta, no pagas nada · por la mañana y por la tarde · el ocho de julio",
   "lab": "Locutora", "voice": "LINA/RADIO",
   "text": "[friendly] ¿Quieres aprender inglés o francés? En la academia Palabras empiezan los cursos de verano el ocho de julio. Hay clases por la mañana y por la tarde, en grupos pequeños. La primera semana es de prueba: si no te gusta, no pagas nada.",
   "why": "La primera semana es de prueba: si no te gusta, no pagas. Hay clases por la mañana y por la tarde, y los cursos empiezan en julio."},
  {"n": 12, "conv": "Audio 6", "q": "Para la fiesta del barrio...", "o": ["hay que llevar plato y vaso.", "la comida es por la noche.", "el concierto es por la mañana."], "ok": 0,
   "cats": ["normas", "tiempo"], "es": "ES-01", "pc": "trae tu plato y tu vaso · paella a las dos · por la noche, concierto",
   "lab": "Locutor", "voice": "ZABRA/RADIO",
   "text": "[excited] ¡Este sábado es la fiesta del barrio del Carmen! Por la mañana hay juegos para niños en la plaza, y a las dos, paella para todos los vecinos. Por la noche, concierto y baile hasta la una. Trae tu plato y tu vaso: no vamos a usar plástico.",
   "why": "Hay que llevar el plato y el vaso. La paella es a las dos, y el concierto, por la noche."},
 ]}

CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Nuria y Marcos. Indique si los enunciados (del 13 al 18) se refieren a Nuria (A), a Marcos (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Nuria y Marcos hablan de cómo ha cambiado su rutina. Cuidado con lo que hace otra persona (la hermana de Nuria) y con lo que no existe o no se hace: en esos casos, la respuesta es C.",
 "who": ["Nuria", "Marcos"], "voices": {"NURIA": "EVA", "MARCOS": "RAFA"},
 "lines": [
  ("MARCOS", "[surprised] ¡Nuria! ¿Qué haces aquí un martes por la mañana? ¿No trabajas?"),
  ("NURIA", "[cheerful] Sí, pero desde septiembre trabajo en casa los lunes, los martes y los miércoles. Solo voy a la oficina los jueves y los viernes."),
  ("MARCOS", "[curious] ¡Qué bien! ¿Y te gusta trabajar en casa?"),
  ("NURIA", "[happy] Mucho. Ya no pierdo una hora en el coche cada día. Y por la tarde, después de trabajar, voy a caminar al parque."),
  ("MARCOS", "[laughs] Pues yo también he cambiado mucho. He vendido el coche."),
  ("NURIA", "[surprised] ¿En serio? ¿Y cómo vas al trabajo ahora?"),
  ("MARCOS", "[proud] En bici. Son veinte minutos por el río. Al principio llegaba muy cansado, pero ahora me encanta. Y además ahorro mucho dinero."),
  ("NURIA", "[thoughtful] Mi hermana también quiere dejar el coche, pero vive muy lejos de su oficina, a cuarenta kilómetros."),
  ("MARCOS", "[curious] ¿Y comes mejor ahora, en casa?"),
  ("NURIA", "[laughs] Sí, ahora cocino yo. Antes comía un bocadillo en la oficina. Ahora como verduras todos los días. Pero trabajar en casa también tiene cosas malas: a veces no hablo con nadie en todo el día."),
  ("MARCOS", "[sympathetic] Ya... A mí eso no me pasa. Yo, en cambio, como con mis compañeros en el comedor de la empresa. Oye, ¿por qué no vienes conmigo a clases de baile? Son los jueves por la tarde."),
  ("NURIA", "[hesitant] Uf, los jueves voy a la oficina y salgo tarde. ¿Los sábados no hay clase?"),
  ("MARCOS", "[thoughtful] Creo que no, solo los jueves. Pero pregunto y te digo algo."),
  ("NURIA", "[cheerful] Vale, gracias. Llámame esta semana. ¡Hasta luego!")],
 "items": [
  {"n": 13, "q": "Trabaja algunos días desde casa.", "ok": 0, "cats": ["tiempo"], "es": "ES-03", "pc": "trabajo en casa los lunes, los martes y los miércoles",
   "why": "Nuria trabaja en casa tres días a la semana y va a la oficina los otros dos."},
  {"n": 14, "q": "Ya no tiene coche.", "ok": 1, "cats": ["pasados"], "es": "ES-03", "pc": "he vendido el coche",
   "why": "Marcos ha vendido el coche y ahora va al trabajo en bici. Nuria dice que ya no pierde una hora en el coche, pero no dice que lo haya vendido."},
  {"n": 15, "q": "Vive lejos de su trabajo.", "ok": 2, "cats": ["personas", "lugares"], "es": "ES-08", "pc": "mi hermana... vive muy lejos de su oficina",
   "why": "La que vive lejos de su oficina es la hermana de Nuria, una tercera persona: ni Nuria ni Marcos."},
  {"n": 16, "q": "Ahora se prepara la comida.", "ok": 0, "cats": ["pasados", "opinion"], "es": "ES-07", "pc": "ahora cocino yo · antes comía un bocadillo",
   "why": "Nuria ahora cocina en casa; antes comía un bocadillo en la oficina."},
  {"n": 17, "q": "Come con otras personas en el trabajo.", "ok": 1, "cats": ["personas", "lugares"], "es": "ES-08", "pc": "como con mis compañeros en el comedor de la empresa",
   "why": "Marcos come con sus compañeros en el comedor de la empresa. Nuria, en cambio, a veces no habla con nadie."},
  {"n": 18, "q": "Va a clases de baile los sábados.", "ok": 2, "cats": ["planes", "tiempo"], "es": "ES-06", "pc": "son los jueves · ¿los sábados no hay clase? Creo que no",
   "why": "Las clases de baile de Marcos son los jueves, y los sábados no hay clase: ninguno de los dos va a clases de baile los sábados."}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. En cada mensaje pregúntate: ¿quién habla, dónde y para qué? Sobran tres enunciados.",
 "enun": [
  "Alguien cambia el día de una cita.",
  "Un tren llega tarde.",
  "Una tienda tiene ofertas.",
  "Alguien da las gracias por una ayuda.",
  "Hay que esperar en otro lugar.",
  "Alguien pide un favor.",
  "Un servicio está cerrado hoy.",
  "Alguien invita a una persona a comer.",
  "Un vuelo sale más temprano.",
  "Alguien ha perdido un objeto.",
  "Un espectáculo se cancela."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "DIANA/RADIO",
   "text": "[friendly] Hola, Pedro, te llamo de la autoescuela Ruedas. Tu clase de conducir no es el lunes, es el miércoles, a la misma hora, a las cinco. Si no puedes, llámame. ¡Hasta el miércoles!",
   "solucion": "La opción correcta es la letra a: alguien cambia el día de una cita."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 1, "cats": ["tiempo"], "es": "ES-10", "pc": "megafonía · llega con quince minutos de retraso",
   "lab": "Megafonía", "voice": "DAVID_M2/RADIO",
   "text": "[neutral] Atención, por favor. El tren que viene de Madrid llega con quince minutos de retraso. Va a entrar por la vía tres a las once y cuarto. Disculpen las molestias.",
   "why": "El tren de Madrid llega con quince minutos de retraso. No hay que esperar en otro lugar (E sobra)."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 3, "cats": ["personas", "opinion"], "es": "ES-10", "pc": "te llamo para darte las gracias por ayudarme",
   "lab": "Contestador", "voice": "RITA/RADIO",
   "text": "[grateful] Hola, Elena, soy Marta. Te llamo para darte las gracias por ayudarme ayer con la mudanza. ¡Sin ti no termino nunca! Ya tengo todo colocado en el piso nuevo. Te debo una cena. Un beso.",
   "why": "Marta le da las gracias a Elena por su ayuda con la mudanza. Habla de una cena, pero no la invita a comer un día concreto."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 2, "cats": ["cantidad"], "es": "ES-10", "pc": "un veinte por ciento de descuento · oferta válida",
   "lab": "Megafonía", "voice": "ALEJANDRO/RADIO",
   "text": "[cheerful] Estimados clientes: hoy, en la sección de frutas, las naranjas y los plátanos tienen un veinte por ciento de descuento. Oferta válida solo hasta las ocho de la tarde. Gracias por su visita.",
   "why": "En el supermercado hay ofertas: un veinte por ciento de descuento en naranjas y plátanos."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 5, "cats": ["personas", "planes"], "es": "ES-10", "pc": "¿me haces un favor? ¿Puedes recogerlo tú?",
   "lab": "Contestador", "voice": "DIEGO/RADIO",
   "text": "[hurried] Hola, Lucía, soy Toni. ¿Me haces un favor? Mañana no estoy en casa y llega un paquete. ¿Puedes recogerlo tú? El cartero viene por la mañana, entre las diez y las doce. Si no puedes, no pasa nada. ¡Gracias!",
   "why": "Toni le pide a Lucía un favor: recoger un paquete."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 6, "cats": ["tiempo", "lugares"], "es": "ES-10", "pc": "hoy la biblioteca está cerrada · mañana abrimos",
   "lab": "Megafonía", "voice": "MARINA/RADIO",
   "text": "[calm] Les informamos de que hoy la biblioteca municipal está cerrada por la fiesta local. Mañana abrimos con el horario de siempre, de nueve de la mañana a nueve de la noche.",
   "why": "Hoy la biblioteca está cerrada por la fiesta local. Mañana abre con el horario de siempre."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 7, "cats": ["personas", "planes"], "es": "ES-10", "pc": "¿quieres venir a comer? Te recojo a la una",
   "lab": "Contestador", "voice": "GABRIEL_CO/RADIO",
   "text": "[warm] Hola, abuela, soy Andrés. El domingo hacemos una paella en casa para celebrar mi cumpleaños. ¿Quieres venir a comer? Te recojo a la una con el coche. Llámame, ¿vale? ¡Un beso!",
   "why": "Andrés invita a su abuela a comer paella el domingo."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 9, "cats": ["lugares", "pasados"], "es": "ES-10", "pc": "me dejé las gafas de sol en tu coche",
   "lab": "Contestador", "voice": "JANET/RADIO",
   "text": "[worried] Hola, Rubén, soy Clara. Creo que ayer me dejé las gafas de sol en tu coche, cuando volvíamos de la playa. Son marrones, en una funda negra. ¿Puedes mirar, por favor? Gracias.",
   "why": "Clara ha perdido sus gafas de sol: cree que se las dejó en el coche."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

# Voces del último modelo que han hecho (M7): no se repiten aquí
VOCES_EVITAR = ["RAQUEL", "MARTIN_3", "GABRIEL_ES", "ESTELA", "CAROLINA", "EMILIO", "SUSANA", "VALENTINA", "CRISTINA", "JAVIER",
                "SARA", "DAVID_M1", "ERIK", "LUCIA", "HUGO", "MARTIN_2", "GABI", "CLARA", "ELEGUAR", "MARTIN_1", "LUCIA_AR",
                "MIA", "MILO", "SOFIA", "SANTIAGO_LAT", "CRISTINA_LAT", "LUIS_GUILLERMO", "MAYA", "LUISA", "BOGA", "DAVID_CO"]
REPARTO = """# REPARTO DE VOCES M01 (ninguna voz del M7, el último modelo que han hecho)
# SIN EFECTOS DE SONIDO: ni sintonía, ni din-don, ni pitido (el examen real tampoco los tiene).
# Cada intervención lleva al principio su etiqueta de emoción de ElevenLabs v3 ([calm], [cheerful], [worried]...).
# Perfil "−" de la auditiva: audios cortos, una idea por audio, descartes claros, palabras muy frecuentes.
# T1 conversaciones (v3): 0 médico = DANIEL_ES + FIONA · 1 farmacia = MARIO + LYDIA · 2 centro de salud = SARA_JOVEN + VOLU
#   3 el desayuno = AITANA + DANI · 4 el hospital = MARINA_ES + LUIS_VEGA · 5 el fisio = SARA_2 + SANTIAGO_ES
#   6 la médica = TATIANA + OSCAR
# T2 radio (perfil /RADIO): 0 «Tarde de música» = SERGIO · 1 piscina = BOBBY · 2 tapones = TAMARA (México)
#   3 muebles = JAVI_ROJAS · 4 el tiempo = ENRIQUE (México) · 5 academia = LINA (Colombia) · 6 fiesta del barrio = ZABRA
# T3 conversación entre amigos: NURIA = EVA · MARCOS = RAFA
# T4 mensajes (/RADIO): 0 contestador autoescuela = DIANA (Colombia) · 1 megafonía estación = DAVID_M2 · 2 contestador Marta = RITA (Argentina)
#   3 megafonía súper = ALEJANDRO (México) · 4 contestador Toni = DIEGO (Argentina) · 5 megafonía biblioteca = MARINA (Argentina)
#   6 contestador Andrés = GABRIEL_CO (Colombia) · 7 contestador Clara = JANET (Argentina)"""

# ---------------- ESCRITURA ----------------
# Textos modelo: [n] = empieza la frase de la pauta n · _texto_ = conector (sale subrayado).
ESCRITA = {"t1": {"instr": "Su prima Alba ha trabajado un año en Irlanda y le ha escrito este correo.", "trato": "tú",
  "input": ["¡Hola! ¿Qué tal? ¡Ya estoy en España! Llegué de Dublín el lunes y estoy muy contenta. Tengo muchas ganas de veros a todos. ¿Y tú? ¿Qué has hecho este año? ¿Tienes planes para el verano? Escríbeme pronto.", "Un beso,<br>Alba"],
  "lead": "Conteste a Alba. En el correo tiene que:",
  "pautas": ["saludar y decirle que se alegra de su vuelta;", "contarle qué ha hecho usted este año y cómo está;", "explicarle sus planes para el verano;", "proponerle una comida con la familia: el día, el lugar y la hora;", "hacerle dos preguntas sobre su año en Irlanda y despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Una revista en español pide a sus lectores textos sobre sus recuerdos del colegio. Escriba un texto sobre un profesor o una profesora que recuerda. Hable de:",
   "pautas": ["quién era, qué enseñaba y en qué colegio o escuela;", "cómo era él o ella y cómo eran sus clases;", "algo que pasó en una de sus clases y que usted recuerda bien;", "qué aprendió de él o de ella que todavía usa hoy;", "cómo cree que tiene que ser un buen profesor."]},
  "op2": {"title": "Opción 2", "intro": "Nora vive en un piso de una ciudad con su gato, Lunes. Aquí tiene tres fotos de un día especial.",
   "photos": ["Por la mañana. Nora, una chica de unos treinta años, ve desde la cocina cómo su gato sale por la ventana abierta.",
              "Por la tarde. Nora pega en una farola un cartel con la foto de su gato y habla con una vecina mayor.",
              "Por la noche. Nora encuentra a su gato dormido en una caja de la frutería de la planta baja; el frutero se ríe."],
   "ficha": [], "intro2": "Escriba un texto sobre el día que se escapó Lunes. Hable de:",
   "pautas": ["qué pasó por la mañana y cómo se sentía Nora;", "qué hizo Nora para buscar a su gato y quién la ayudó;", "cómo terminó el día y por qué cree usted que el gato se escapó."],
   "img": "M01_escrita_nora_gato_lunes.jpg", "imgAlt": "Tres fotos de Nora: su gato sale por la ventana, Nora pega un cartel en la calle y encuentra al gato dormido en la frutería"},
  "min": 70, "max": 80},
 "modelos": {
  "t1": {"titulo": "Tarea 1 · Correo a una prima (de tú)", "tarea": 1,
   "aprobado": {"texto": [
     "[1]¡Hola, Alba! ¡Qué alegría tu vuelta!",
     "[2]Este año he trabajado mucho y he aprendido a nadar. Estoy muy bien, _pero_ un poco cansado. [3]En verano voy a ir a la playa con mis amigos, a Cádiz. [4]¿Comemos todos juntos el domingo 15 a las dos en casa de los abuelos? [5]¿Te ha gustado vivir en Dublín? ¿Has aprendido mucho inglés?",
     "Un beso,<br>Luis"],
    "porque": "Contesta a las cinco pautas con frases sencillas: se alegra de la vuelta, cuenta lo que ha hecho con el pretérito perfecto (he trabajado, he aprendido), explica su plan con ir a + infinitivo, propone día, lugar y hora, y hace dos preguntas sobre Irlanda. Todo de tú, del saludo a la despedida."},
   "excelente": {"texto": [
     "[1]¡Hola, Alba! ¡Qué alegría saber que ya estás aquí!",
     "[2]Este año he cambiado de trabajo y, _además_, he empezado clases de natación. Estoy contento, _pero_ muy liado. [3]_Por eso_ en verano voy a descansar en el pueblo de los abuelos. [4]¿Te va bien comer con la familia el domingo 15 a las dos en su casa? [5]¿Qué te ha gustado más de Irlanda? ¿Has hecho amigos irlandeses?",
     "Un beso,<br>Luis"],
    "porque": "Las mismas cinco pautas, con dos o tres mejoras del A2: conectores para unir las ideas (además, pero, por eso), una palabra más precisa (muy liado), un porqué para el plan del verano y preguntas más personales. Sigue siendo corto y de tú.",
    "mejoras": ["un conector más (además, pero, por eso)", "una palabra más precisa (muy liado)", "un detalle o un porqué (por eso voy a descansar)", "una pregunta al lector más concreta (¿Has hecho amigos irlandeses?)"]}},
  "op1": {"titulo": "Tarea 2 · Opción 1 · Un profesor o una profesora que recuerdo", "tarea": 2,
   "aprobado": {"texto": [
     "[1]Mi profesora favorita se llamaba Julia y enseñaba Matemáticas en mi colegio de Toledo. [2]Era alta, muy simpática y un poco seria. Sus clases eran muy divertidas. [3]Un día nos llevó al patio para medir los árboles. ¡Fue genial! [4]Gracias a ella, hoy hago las cuentas de casa sin calculadora y me gustan los números. [5]Creo que un buen profesor tiene que ser paciente y explicar bien, _porque_ los alumnos necesitan entender las cosas."],
    "porque": "Cumple las cinco pautas, una o dos frases para cada una. Usa el imperfecto para describir a Julia y sus clases (era, eran), el indefinido para lo que pasó un día (nos llevó, fue) y el presente para hoy y para la opinión. Es sencillo y aprueba."},
   "excelente": {"texto": [
     "[1]Recuerdo mucho a Julia, mi profesora de Matemáticas en un colegio de Toledo. [2]Era alta y seria, _pero_ muy cariñosa, y sus clases nunca eran aburridas. [3]Una mañana de primavera nos llevó al patio para medir los árboles y, _al final_, todos queríamos ser científicos. [4]_Por eso_ todavía hoy hago las cuentas de casa sin calculadora. [5]Para mí, un buen profesor escucha, tiene paciencia y explica las cosas con ejemplos de la vida real."],
    "porque": "Las mismas cinco pautas, con más variedad: un pasado bien combinado (nos llevó al patio y todos queríamos ser científicos), conectores para contar y explicar (pero, al final, por eso), palabras más precisas (cariñosa, nunca eran aburridas) y una opinión con tres ideas. Todo sigue siendo A2.",
    "mejoras": ["un pasado bien combinado (nos llevó... todos queríamos)", "un conector más (pero, al final, por eso)", "una palabra más precisa (cariñosa, aburridas)", "un detalle o un porqué (con ejemplos de la vida real)"]}},
  "op2": {"titulo": "Tarea 2 · Opción 2 · El día que se escapó Lunes", "tarea": 2,
   "aprobado": {"texto": [
     "[1]Un sábado por la mañana, Nora estaba en la cocina y su gato Lunes salió por la ventana. Nora estaba muy nerviosa y triste. [2]Por la tarde hizo carteles con una foto de Lunes y los puso en la calle. Una vecina mayor la ayudó a buscarlo. [3]Por la noche, Nora encontró a Lunes en la frutería de abajo. Estaba dormido en una caja. Creo que se escapó _porque_ vio un pájaro."],
    "porque": "Cuenta la historia en pasado (no describe las fotos en presente): el imperfecto para cómo estaba Nora y para el gato dormido (estaba), el indefinido para lo que pasó (salió, hizo, encontró). Responde a las tres pautas, también a la suposición del final (creo que se escapó porque...)."},
   "excelente": {"texto": [
     "[1]Un sábado, _mientras_ Nora preparaba el desayuno, Lunes saltó por la ventana de la cocina. Nora estaba muy preocupada _porque_ su gato nunca sale de casa. [2]_Primero_ lo buscó por el barrio y _después_ pegó carteles en las farolas. Una vecina mayor la ayudó a preguntar en las tiendas. [3]_Al final_, por la noche, el frutero la llamó: ¡Lunes dormía en una caja de manzanas! Supongo que buscaba un sitio tranquilo."],
    "porque": "Más variedad de pasados (mientras preparaba, saltó / dormía), conectores que ordenan la historia (mientras, primero, después, al final), un porqué en la primera pauta y una suposición con supongo que. Sigue contando, no describe las fotos.",
    "mejoras": ["un pasado bien combinado (mientras Nora preparaba el desayuno, Lunes saltó)", "un conector más (primero, después, al final)", "un detalle o un porqué (porque su gato nunca sale de casa)", "una frase con cuando o mientras"]}}}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: una persona de mi familia", "pautas": ["quién es, cómo es y a qué se dedica;", "qué hacían juntos cuando usted era pequeño o pequeña;", "un día especial o divertido que pasaron juntos;", "cómo son normalmente las familias en su país (grandes o pequeñas, si viven cerca...);", "qué planes tienen juntos para los próximos meses."]},
  {"title": "Opción 2: la estación del año que más me gusta", "pautas": ["qué estación es y por qué le gusta;", "qué hacía en esa estación cuando era niño o niña;", "qué hizo la última vez en esa estación;", "qué estación prefiere la gente de su país para ir de vacaciones y por qué;", "qué planes tiene para esa estación este año."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1 · En el mercado", "desc": "Un mercado semanal en la plaza de un pueblo de costa, una mañana de verano. En un puesto de quesos y aceitunas, una señora de unos sesenta años, con un vestido de flores, gafas de sol en la cabeza y un carro de la compra, prueba un trozo de queso. El vendedor, un chico de unos veinticinco años con un delantal verde, le corta otro trozo. En el mostrador hay quesos, aceitunas, una báscula y bolsas de papel; arriba, un toldo de rayas. Del carro de la señora asoma la cabeza de un perro pequeño.", "img": "M01_oral_foto1_mercado_queso.jpg"},
  {"title": "Fotografía 2 · Limpiar la casa", "desc": "La cocina de un piso compartido, un domingo por la mañana. Dos compañeros de piso de unos veintitrés años limpian después de una cena con amigos. Un chico alto, con barba, camiseta gris y guantes amarillos, friega los platos. Una chica con el pelo recogido, sudadera roja y pantalón corto barre el suelo con una escoba; lleva auriculares y canta. En la encimera hay platos sucios, vasos, una botella vacía y una caja de pizza; en el suelo, una bolsa de basura.", "img": "M01_oral_foto2_limpiar_cocina_piso.jpg"}],
  "pautas": ["¿Cómo son las personas de la foto (físico, personalidad que cree que tienen...)? ¿Qué ropa llevan?", "¿Dónde están esas personas? ¿Qué objetos hay? Describa el lugar.", "¿Qué están haciendo las personas de la foto?", "¿Qué relación cree que hay entre ellas?", "¿Qué cree que piensan o cómo se sienten estas personas? ¿Por qué?", "¿Qué cree que han hecho antes? ¿Y qué van a hacer después?"]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1 · Una cena en casa", "intro": "Usted y un amigo o una amiga van a hacer una cena en casa el sábado para otros amigos. Antes, hablan de lo que van a cocinar y de la compra. El examinador / La examinadora es su amigo/a. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su amigo/a, tiene que hablar de:", "pautas": ["dónde hace usted la compra normalmente y qué compra;", "si ha organizado alguna cena en casa: cuándo, para quién y qué tal fue;", "qué van a cocinar y por qué;", "qué tienen que comprar y cuánto dinero van a gastar;", "cuándo van a ir al mercado y a qué hora quedan."]},
  {"title": "Si eligió la fotografía 2 · Organizar la casa", "intro": "Un amigo o una amiga va a vivir con usted en su piso desde la semana que viene. Hoy hablan de cómo organizar la casa. El examinador / La examinadora es su amigo/a. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su amigo/a, tiene que hablar de:", "pautas": ["a qué hora se levanta y cómo es su horario de trabajo o de estudios;", "qué tareas de la casa le gustan y cuáles no, y quién las hacía en su casa cuando era pequeño o pequeña;", "cómo van a repartir las tareas (limpiar, cocinar, hacer la compra...);", "qué normas quieren tener en casa (visitas, ruido, música...);", "qué van a hacer juntos el primer fin de semana."]}]}}

# Modelos de la tarea 3 (se ven en la oral del estudiante después de la prueba y en la libreta de la profesora).
# En el diálogo, "E" = examinador y "C" = candidato. La frase del pequeño problema lleva True.
# Como en las láminas de 2022, las dos situaciones son de tú y mezclan planificar con contar cosas propias.
# Perfil "−": pautas sencillas y un pequeño problema fácil de resolver.
ORAL_MODELOS = {"t3": [
 {"titulo": "Fotografía 1 · Una cena en casa", "trato": "tú",
  "notas": [["dónde compro", "súper de mi calle · fruta y pescado en el mercado (más frescos) · ¿y tú?"],
            ["¿he organizado una cena?", "año pasado, cumple de mi hermano, 10 personas · lasaña · salió muy bien"],
            ["qué cocinamos", "ensalada, tortilla, pollo al horno · fácil · postre: fruta · ¿te parece?"],
            ["compra y dinero", "patatas, huevos, pollo, lechuga, tomates, fruta + queso y aceitunas · 60 € (30 cada uno)"],
            ["cuándo y a qué hora", "sábado por la mañana al mercado · quedamos en la puerta"]],
  "segunda": "Si no puede el sábado: ir al mercado el viernes por la tarde o ir yo y él/ella compra la bebida.",
  "problema": "El examinador trabaja el sábado por la mañana y no puede ir al mercado.",
  "dialogo": [
   ["E", "¡Hola! Oye, ¿hablamos de la cena del sábado? Tenemos que organizar la compra."],
   ["C", "¡Hola! Sí, claro. Yo normalmente hago la compra en el supermercado de mi calle, pero la fruta y el pescado los compro en el mercado del barrio, porque son más frescos. ¿Y tú, dónde compras?"],
   ["E", "Yo voy siempre al súper. ¿Tú has organizado alguna cena en casa?"],
   ["C", "Sí, el año pasado hice una cena para el cumpleaños de mi hermano. Éramos diez personas y cociné una lasaña. ¡Salió muy bien! ¿Y tú?"],
   ["E", "Yo nunca. ¿Y qué cocinamos el sábado?"],
   ["C", "¿Qué te parece una ensalada, una tortilla de patatas y pollo al horno? Es fácil y siempre sale bien. De postre, fruta. ¿Te parece bien?"],
   ["E", "Perfecto. ¿Y qué compramos? ¿Cuánto gastamos?"],
   ["C", "Necesitamos patatas, huevos, pollo, lechuga, tomates y fruta. Y también queso y aceitunas para empezar. ¿Gastamos unos sesenta euros, treinta cada uno?"],
   ["E", "Vale. Pero hay un problema: el sábado por la mañana tengo que trabajar y no puedo ir al mercado.", True],
   ["C", "No pasa nada. ¿Por qué no vamos el viernes por la tarde? El mercado cierra a las ocho. Y si no puedes, voy yo y tú compras la bebida, ¿vale?"],
   ["E", "El viernes por la tarde sí puedo. ¿A qué hora quedamos?"],
   ["C", "¿Quedamos a las seis en la puerta del mercado? ¡Hasta el viernes!"]]},
 {"titulo": "Fotografía 2 · Organizar la casa", "trato": "tú",
  "notas": [["mi horario", "me levanto a las 7 · trabajo de 8:30 a 17:00 · ¿y tú?"],
            ["tareas: me gusta / no", "cocinar sí, limpiar la cocina bien, planchar no · de pequeño: madre cocinaba, padre y yo fregábamos"],
            ["repartir", "yo cocino entre semana · tú el baño · compra juntos el sábado · salón: una semana cada uno"],
            ["normas", "música alta no después de las 23:00 · avisar si vienen amigos · ¿de acuerdo?"],
            ["primer fin de semana", "cena con amigos (casa nueva) · domingo: mercadillo, plantas para el balcón"]],
  "segunda": "Si los dos necesitan el baño a las siete: turnos para la ducha (7 menos cuarto y 7 y cuarto) o me ducho por la noche.",
  "problema": "El examinador también necesita el baño a las siete de la mañana.",
  "dialogo": [
   ["E", "¡Hola! Ya tengo las cajas preparadas para la mudanza. ¿Hablamos un poco de cómo organizamos la casa?"],
   ["C", "¡Hola! Sí, buena idea. Mira, yo me levanto a las siete porque empiezo a trabajar a las ocho y media. Vuelvo a casa a las cinco. ¿Y tú, qué horario tienes?"],
   ["E", "Yo estudio por la mañana y trabajo en una tienda por la tarde. ¿Qué tareas de la casa te gustan?"],
   ["C", "Me gusta cocinar y no me importa limpiar la cocina, pero odio planchar. De pequeño, en mi casa, mi madre cocinaba y mi padre y yo fregábamos los platos. ¿Y a ti?"],
   ["E", "A mí no me gusta cocinar, pero limpio el baño sin problema. ¿Cómo repartimos las tareas?"],
   ["C", "Pues yo cocino entre semana y tú limpias el baño. La compra la hacemos juntos los sábados, y el salón, una semana cada uno. ¿Qué te parece?"],
   ["E", "Muy bien. ¿Y alguna norma para la casa?"],
   ["C", "Para mí, nada de música alta después de las once, porque me levanto pronto. Y si vienen amigos, avisamos antes. ¿Estás de acuerdo?"],
   ["E", "Sí, claro. Oye, una cosa: yo también me ducho a las siete, porque tengo clase a las ocho...", True],
   ["C", "Vaya, solo hay un baño. ¿Y si me ducho yo a las siete menos cuarto y tú a las siete y cuarto? O me ducho por la noche, no pasa nada. ¿Te va bien?"],
   ["E", "Perfecto. ¿Y qué hacemos el primer fin de semana?"],
   ["C", "¿Por qué no hacemos una cena con nuestros amigos para celebrar la casa nueva? Y el domingo podemos ir al mercadillo a comprar plantas para el balcón. ¡Hasta el sábado!"]]}]}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (una persona de mi familia): ¿Cuántas veces al mes la ve? · ¿Qué hacían juntos los domingos?
    Opción 2 (mi estación favorita): ¿Qué ropa lleva en esa estación? · ¿Qué comida le gusta en esa época?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (en el mercado): ¿Qué cree que va a comprar la señora? · ¿De quién es el perro?
    Foto 2 (limpiar la casa): ¿Qué cree que hicieron anoche? · ¿Quién trabaja más, el chico o la chica?
  Tarea 3 — su papel: amigo/a del candidato, SIEMPRE DE TÚ (como en las láminas de 2022). Modelo de entrada (perfil −):
  pautas sencillas y un pequeño problema fácil. Vaya pauta por pauta, elija las preguntas según lo que diga el candidato,
  improvise con sus datos y provoque UN pequeño problema. Esquema para la interacción:
    Foto 1 (amigo/a · una cena en casa el sábado)
      Saludar ............. ¡Hola! ¿Hablamos de la cena del sábado? Tenemos que organizar la compra.
      Dónde compra ........ ¿Dónde haces la compra normalmente? ¿Qué compras en el mercado?
      Experiencia ......... ¿Has organizado alguna cena en casa? ¿Cuándo? ¿Para quién? ¿Qué tal fue?
      Qué cocinar ......... ¿Qué cocinamos? ¿Por qué eso? ¿Y de postre?
      Compra y dinero ..... ¿Qué tenemos que comprar? ¿Cuánto gastamos?
      PEQUEÑO PROBLEMA .... «El sábado por la mañana tengo que trabajar y no puedo ir al mercado».
                            Espere a que proponga algo (ir el viernes por la tarde, ir solo/a).
      Quedar y adiós ...... ¿A qué hora quedamos? ¿Dónde? · Vale, ¡hasta el viernes!
    Foto 2 (amigo/a que va a vivir en el piso · organizar la casa)
      Saludar ............. ¡Hola! Ya tengo las cajas preparadas. ¿Hablamos de cómo organizamos la casa?
      Horario ............. ¿A qué hora te levantas? ¿Qué horario tienes en el trabajo o en clase?
      Tareas .............. ¿Qué tareas de la casa te gustan? ¿Y cuáles no? ¿Quién las hacía en tu casa de pequeño/a?
      Repartir ............ ¿Cómo repartimos las tareas? ¿Quién cocina? ¿Y la compra?
      Normas .............. ¿Qué normas ponemos? ¿Y si vienen amigos? ¿Y la música?
      PEQUEÑO PROBLEMA .... «Yo también me ducho a las siete, porque tengo clase a las ocho...». Espere a que proponga
                            algo (turnos, ducharse por la noche).
      Fin de semana y adiós ¿Qué hacemos el primer fin de semana? · Vale, ¡hasta el sábado!
    El diálogo modelo de las dos situaciones está en la pestaña Oral del estudiante (se ve al abrir la prueba).
  Qué mirar en este modelo: tú coherente en toda la tarea 3; que no conteste solo sí o no (responde + detalle o
  porqué + pregunta); proponer y aceptar o rechazar con otra propuesta (¿por qué no...?, ¿y si...?, ¿te va bien...?);
  en la tarea 3, la pauta de experiencia en pasado (hice, cociné, salió, mi madre cocinaba); en el monólogo, presente +
  pasado (cuando era pequeño/a + imperfecto, un día en indefinido) + futuro, y la pauta que se sale de la historia
  personal (cómo son las familias en su país / qué estación prefiere la gente de su país); en la foto, las seis
  preguntas en orden, hay / está, estar + gerundio y «seguramente han...» / «van a...»."""
ERRORES = """  *Tú puede / *¿Usted tienes...? (mezcla tú / usted); *Cuando era pequeño, fui cada verano a la playa (iba: costumbre);
  *El año pasado he hecho una cena (hice; con «este año», he hecho); *Mi hermana es muy simpático (simpática);
  *Hay la señora en el mercado (está la señora / hay una señora); *Los platos están sucio (sucios); *Me gusta mucho los
  quesos (me gustan); *Está limpiando (bien) / *Está limpiar (limpiando); *En invierno hace mucho frío y hay mucho nieve
  (mucha nieve); *Voy a mercado (al mercado); frases sueltas sin conectores en el monólogo («y... y... y...»)."""

# ---------------- IMÁGENES: FOTOS ----------------
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "mercado semanal de un pueblo de costa: una señora prueba queso en un puesto",
  "personas": "una señora y un vendedor joven", "edades": "ella de unos 60 años, él de unos 25",
  "aspecto": "ella con un vestido de flores, gafas de sol en la cabeza y el pelo corto y gris; él con el pelo corto, una camiseta blanca y un delantal verde",
  "espacio": "exterior", "lugar": "puesto de quesos y aceitunas de un mercado semanal en la plaza de un pueblo de costa", "momento": "mañana",
  "estacion": "verano", "tiempo": "sol", "gente": "otros puestos y algunas personas al fondo",
  "accion": "la señora prueba un trozo de queso y el vendedor le corta otro trozo",
  "fondo": "otros puestos del mercado con toldos, casas blancas de la plaza",
  "objetos": "quesos, cuencos de aceitunas, báscula, bolsas de papel, cuchillo, toldo de rayas, carro de la compra",
  "detalle": "del carro de la compra de la señora asoma la cabeza de un perro pequeño"},
 "oral_foto2": {"situacion": "cocina de un piso compartido: dos compañeros limpian después de una cena",
  "personas": "dos compañeros de piso", "edades": "los dos de unos 23 años",
  "aspecto": "él alto, con barba, camiseta gris, pantalón de chándal y guantes amarillos; ella con el pelo recogido, sudadera roja y pantalón corto",
  "espacio": "interior", "lugar": "cocina pequeña de un piso compartido, con fregadero, encimera y ventana", "momento": "mañana",
  "estacion": "otoño", "tiempo": "nublado", "gente": "solo ellos dos",
  "accion": "él friega los platos y ella barre el suelo con una escoba",
  "fondo": "armarios de cocina, una ventana con la calle, un calendario en la pared",
  "objetos": "platos sucios, vasos, botella vacía, caja de pizza, escoba, bolsa de basura, guantes, estropajo",
  "detalle": "ella lleva auriculares y canta mientras barre, como si la escoba fuera un micrófono"},
 "escrita": {"situacion": "el día que se escapó Lunes, el gato de Nora, en tres momentos",
  "personas": "Nora, su gato, una vecina mayor y el frutero", "edades": "Nora de unos 30 años; la vecina de unos 75; el frutero de unos 50",
  "aspecto": "Nora con el pelo negro y rizado, gafas redondas, un jersey verde y vaqueros; el gato atigrado gris con una mancha blanca en la cara",
  "espacio": "interior y exterior", "lugar": "la cocina del piso de Nora, la calle del barrio y la frutería de la planta baja", "momento": "mañana, tarde y noche",
  "estacion": "primavera", "tiempo": "sol y luz de la tienda por la noche", "gente": "Nora sola en la primera; con una vecina en la segunda; con el frutero en la tercera",
  "accion": "el gato sale por la ventana; Nora pega un cartel en una farola y habla con una vecina; Nora encuentra al gato dormido en una caja de la frutería",
  "fondo": "la cocina con la ventana abierta; una calle con tiendas y árboles; la frutería con cajas de fruta",
  "objetos": "taza de café, ventana, carteles, cinta adhesiva, farola, cajas de fruta, manzanas, báscula",
  "detalle": "en la tercera foto el gato duerme en una caja de manzanas y el frutero se ríe"},
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
 "M06": ["salón de casa: dos hermanos preparan las mochilas para la montaña", "padre e hija pintan el salón de un piso"],
 "M07": ["salón de un estudio: dos amigas buscan piso de alquiler en un portátil", "huerto urbano entre edificios: un abuelo y su nieta recogen tomates"],
 "M01": ["mercado semanal de un pueblo de costa: una señora prueba queso en un puesto", "cocina de un piso compartido: dos compañeros limpian después de una cena"],
}

IMG_PROMPTS = {
 "escrita": "The day Nora's cat escaped, in three moments, in an ordinary Spanish city neighbourhood in spring. Nora is a woman of about 30 with curly black hair, round glasses, a green jumper and jeans; her cat is a grey tabby with a white patch on its face. Panel 1 (left): morning, in a small kitchen, Nora stands by the table with a mug of coffee in her hand and a surprised face, while the grey tabby cat jumps out through the open kitchen window onto a balcony with plant pots. Panel 2 (middle): afternoon, on a pavement with small shops and trees, Nora sticks a paper poster with a photo of a cat on a lamppost with tape, while an elderly neighbour of about 75 with white hair, a cardigan and a shopping bag talks to her and points down the street. Panel 3 (right): evening, inside a small greengrocer's on the ground floor, under the shop lights, Nora bends over a wooden crate of red apples where the grey tabby cat is sleeping curled up; the greengrocer, a man of about 50 with an apron, laughs behind the counter with scales and boxes of fruit.",
 "oral_foto1": "A woman of about 60 and a young market stallholder of about 25 at a cheese and olive stall in the weekly open-air market in the square of a small Spanish seaside town on a sunny summer morning. She wears a flowery dress, has short grey hair and sunglasses pushed up on her head, and tastes a small piece of cheese with a pleased face; next to her stands a shopping trolley with a small dog's head peeking out of it. The stallholder, with short hair, a white T-shirt and a green apron, cuts another piece of cheese for her with a knife. On the counter: several round cheeses, bowls of olives, a weighing scale and paper bags. A striped awning above the stall; other market stalls, a few shoppers and white houses in the background.",
 "oral_foto2": "Two flatmates of about 23 cleaning the small kitchen of a shared flat on a grey Sunday morning, after a dinner party the night before. A tall young man with a beard, a grey T-shirt, tracksuit bottoms and yellow rubber gloves washes the dishes at the sink. A young woman with her hair tied up, a red sweatshirt and shorts sweeps the floor with a broom; she wears earphones and sings, holding the broom handle like a microphone. On the worktop: dirty plates, glasses, an empty bottle and an open pizza box; on the floor, a full rubbish bag. Kitchen cupboards, a window with a cloudy sky and a calendar on the wall.",
}
IMG_NAMES = {"escrita": "M01_escrita_nora_gato_lunes", "oral_foto1": "M01_oral_foto1_mercado_queso", "oral_foto2": "M01_oral_foto2_limpiar_cocina_piso"}
IMG_DESC = {"escrita": "Escritura opcion 2 triptico el gato de Nora: 1 el gato sale por la ventana, 2 Nora pega un cartel y habla con una vecina, 3 encuentra al gato dormido en la fruteria",
            "oral_foto1": "Oral foto 1 en el mercado: una senora prueba queso en un puesto y el vendedor le corta otro trozo",
            "oral_foto2": "Oral foto 2 limpiar la casa: dos companeros de piso limpian la cocina, el friega y ella barre"}
CA1_DESC = {0: "Auditiva T1 ejemplo: cabeza / garganta / espalda", 1: "Auditiva T1 conv 1: jarabe / pastillas / crema para el sol",
            2: "Auditiva T1 conv 2: centro de salud al lado de la farmacia / enfrente del parque / detras del mercado", 3: "Auditiva T1 conv 3: galletas / tostadas / fruta",
            4: "Auditiva T1 conv 4: flores / libro / bombones", 5: "Auditiva T1 conv 5: andando / autobus / taxi",
            6: "Auditiva T1 conv 6: correr / yoga / nadar"}

LECTURA = [CL1, CL2, CL3, CL4]
AUDITIVA = [CA1, CA2, CA3, CA4]
