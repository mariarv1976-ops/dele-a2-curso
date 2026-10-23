# -*- coding: utf-8 -*-
# FUENTE DEL MODELO 7 · Curso de preparación DELE A2 (Módulo 2, modelos completos)
# Nivel: el más exigente del curso (perfil + + + =: lectura, auditiva y escritura en la parte alta del examen;
# oral como en el examen). Se hace 2-3 semanas antes del examen. Nunca gramática de B1.
# Temas MEZCLADOS como en el examen real: cada tarea de un área distinta.
# Se construye con:  python3 build_modelo.py fuente_M07
# Todo el contenido es original. Español de España.
M = "07"
NOMBRE = "Modelo 7"
NIVEL = "nivel alto"
TITLE = "Examen completo"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress
TIEMPOS = {"lectura": 60, "auditiva": 40}
REC_LABEL = "Qué vas a encontrar en este modelo"
RECORDATORIO = [
 "Un examen completo con el formato y los tiempos del DELE A2: lectura (60 minutos), auditiva (40 minutos), escritura (45 minutos) y, en clase con tu profesora, la oral.",
 "Como en el examen, cada tarea habla de un tema distinto: una fiesta familiar, anuncios de la ciudad, trabajos de noche, un alumno de sesenta y ocho años, la comida de la semana, un grupo de teatro, una amistad de la infancia, buscar piso y un huerto.",
 "Lee con atención quién hace cada cosa, cuándo y si al final lo hace: muchas opciones falsas dicen algo que aparece en el texto, pero no es exactamente así.",
 "Al terminar, en Resultados ves tu nota de cada grupo (lectura + escritura; auditiva + oral), si estás listo para presentarte, qué fichas repasar, tu control de progreso y cómo leer la nota de este modelo.",
]
TIPS_INICIO = [
 "<b>Reparte el tiempo de la lectura:</b> unos 12 minutos para la tarea 1, 15 para la 2, 15 para la 3 y 18 para la 4. Si una pregunta te bloquea, marca una opción y sigue: los errores no restan.",
 "<b>Cuidado con los cambios de plan:</b> «al principio pensábamos...», «primero quería...», «eso era antes». La respuesta buena es lo que pasa al final o lo que pasa ahora.",
 "<b>Auditiva:</b> en la tarea 1 se oyen las tres opciones. Fíjate en la pregunta: ¿qué ha hecho ya?, ¿dónde trabaja ahora?, ¿qué tiene que llevar? Espera al final de la conversación antes de marcar.",
 "<b>Al terminar cada prueba, apunta cuánto has tardado en cada tarea y qué te ha costado:</b> lo vas a necesitar en el control de progreso de Resultados.",
]

# Perfil del modelo frente al examen real (+ más difícil, = como el examen, - más fácil).
# Se enseña al final de Resultados, solo después de entregar (motor_modelo_extra.py, xPerfil).
PERFIL = {"pruebas": {"lectura": "+", "auditiva": "+", "escrita": "+", "oral": "="},
 "cuando": "Este es el modelo más exigente del curso: está pensado para hacerlo dos o tres semanas antes del examen.",
 "nota": "Lo que lo hacía más difícil: textos largos con mucha información, opciones falsas muy parecidas a la buena (otra persona, otro momento, un plan que cambia), palabras menos frecuentes del A2 y, en la escritura, pautas con dos o tres cosas que mezclan los pasados con el presente. La gramática era la del A2, como en el examen."}
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
  "repaso": "El indefinido cuenta lo que pasó y terminó (dejó el colegio, aprobó, se jubiló); el imperfecto describe cómo era o qué hacía antes (me gustaba estudiar, jugábamos en el parque); el perfecto habla de lo que has hecho hasta ahora (este curso ha empezado, todavía no lo he abierto). En las preguntas, fíjate en las palabras de tiempo: antes, ahora, ya, todavía, al principio.",
  "reto": "Escribe tres frases sobre algo que estudiaste: cómo era la clase (imperfecto), qué pasó un día (indefinido) y qué has aprendido este año (perfecto).",
  "fichas": F("R01")},
 "planes": {"name": "Planes, propuestas y cambios de plan (pensábamos..., al final..., ¿y si...?)",
  "repaso": "En el examen, la persona dice primero lo que pensaba hacer y después lo que hace de verdad: «al principio pensábamos hacer la comida en el restaurante, pero al final...», «quería apuntarme, pero al final no». La respuesta buena es siempre la última decisión. Para proponer: ¿y si...?, ¿quedamos...?, ¿te va bien el jueves?",
  "reto": "Escribe un mensaje a un amigo con un plan que cambia: «Al principio pensaba..., pero al final...».",
  "fichas": F("R01", "M4-3", "R13", "R08", "R14b")},
 "normas": {"name": "Normas y condiciones en anuncios y avisos (hay que, solo, excepto, mínimo)",
  "repaso": "En los anuncios, las palabras pequeñas lo cambian todo: hay que (obligación), no es necesario (no es obligatorio), solo, excepto, mínimo, como máximo, gratis, se paga aparte. Lee la pregunta y busca solo esa condición en el texto: muchas veces la respuesta buena la dice con otras palabras (mínimo seis meses = no se puede alquilar un mes).",
  "reto": "Escribe un anuncio para alquilar tu plaza de garaje o tu bici con tres condiciones: algo obligatorio, algo que no está incluido y algo que solo es posible un día.",
  "fichas": F("M0", "R14b")},
 "tiempo": {"name": "Horas, fechas, horarios y duración (a las, de... a, desde hace, durante, en)",
  "repaso": "A las + hora; de... a... / desde... hasta... para horarios; por la mañana / tarde / noche; hace + tiempo para el pasado; desde hace + tiempo para algo que sigue hoy; durante para un periodo cerrado; tardar + tiempo. En la auditiva, las horas parecidas (las ocho y diez, las ocho y cuarenta) son la trampa más frecuente.",
  "reto": "Escribe cinco frases sobre tu semana con: a las..., de... a..., por la noche, desde hace..., durante...",
  "fichas": F("R06", "R14b")},
 "lugares": {"name": "Lugares y localización (hay, está, en, a, debajo de, al lado de)",
  "repaso": "Hay presenta algo nuevo (hay un huerto entre los edificios); está sitúa algo que ya conocemos (las llaves están en la panadería). Ir a + lugar, estar en + lugar, pasar por + zona. Cuidado: el examen cambia muchas veces el lugar al final (no en el buzón, en la panadería).",
  "reto": "Describe en cuatro frases dónde están las cosas importantes de tu casa: hay..., está..., debajo de..., al lado de...",
  "fichas": F("R02", "R06", "R14a")},
 "cantidad": {"name": "Precios, descuentos y cantidades (gratis, la mitad, un 50 %, el doble, muy, mucho)",
  "repaso": "Gratis / gratuito / no pagar = no cuesta dinero; a mitad de precio = la mitad; el doble; un cincuenta por ciento de descuento; más de / menos de. Muy va con adjetivos (muy caro); mucho, con nombres y verbos (mucho dinero, cuesta mucho). En los anuncios, mira a quién se aplica el descuento y a qué cosa: la matrícula no es lo mismo que las clases.",
  "reto": "Escribe un anuncio de una tienda con tres ofertas: algo gratis, algo a mitad de precio y una condición.",
  "fichas": F("R05", "R14a")},
 "personas": {"name": "Quién hace qué: personas, relaciones y trato (su nieta, la tía, tú / usted)",
  "repaso": "Muchas opciones falsas cuentan lo que hace otra persona: la tía, el primo, la hermana, la mujer. Fíjate en los posesivos (su nieta, sus compañeros) y en quién es el sujeto de cada verbo. En la auditiva tarea 3, si lo hace una tercera persona, la respuesta es «ninguno de los dos».",
  "reto": "Escribe dos frases sobre lo que haces tú y dos sobre lo que hace una persona de tu familia, con posesivos (mi, su, nuestro).",
  "fichas": F("R04", "R07", "R10", "R14a")},
 "opinion": {"name": "Gustos, opiniones y sentimientos (me encanta, me da vergüenza, estoy contento)",
  "repaso": "Me gusta / me encanta / me cuesta + infinitivo; me da miedo, me da vergüenza; estar + contento, nervioso, cansado; para mí, creo que. En la lectura, la opinión puede cambiar con el tiempo (al principio no lo entendía; ahora...): lee hasta el final.",
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
 "instr": "Usted va a leer el correo electrónico que Remedios ha escrito a su nieto Álex. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Remedios cuenta un plan que ha cambiado y habla de varias personas de la familia: para cada pregunta, busca quién hace cada cosa y cuál es la decisión final.",
 "head": ["De: Remedios", "Para: Álex", "Asunto: ¡Cincuenta años!"],
 "body": [
  "Querido Álex:",
  "¿Cómo va todo por Valencia? Tu madre me ha contado que ya has terminado las prácticas en el hospital y que estás muy contento. ¡Enhorabuena, hijo! Te escribo porque el sábado 14 de junio tu abuelo y yo celebramos nuestras bodas de oro: cincuenta años casados. ¡Quién lo iba a decir!",
  "Al principio pensábamos hacer una comida en el restaurante del puerto, donde celebramos la boda en 1976, pero ahora es muy caro y además no tiene sitio para tantas personas. Así que al final la hacemos en la casa del pueblo, en el jardín, como las fiestas de antes. Tu tía Pilar va a pedir mesas y sillas al ayuntamiento, y tu primo Sergio, que es cocinero, va a preparar una paella gigante. Yo solo hago los postres: ya sabes que mi tarta de almendras no puede faltar. Empezamos a la una y, por la tarde, tus primos van a poner música para bailar.",
  "Tu abuelo no quería ninguna fiesta. Decía que a nuestra edad lo mejor era una cena tranquila en casa, los dos solos. Pero cuando supo que venían sus hermanos de Argentina, cambió de opinión. ¡Hace veinte años que no los ve!",
  "Y ahora, el favor. Tú sabes mucho de ordenadores y tienes muy buen gusto. ¿Puedes preparar un vídeo con fotos antiguas de la familia? Tengo dos cajas llenas en el armario del pasillo: de la boda, de los viajes, de tu madre de pequeña... Si vienes el puente de mayo, las miramos juntos y eliges las mejores. Puedes dormir en la habitación de arriba, la del balcón, que ya no la usa nadie. No tienes que traer nada más: solo tu ordenador y tu alegría.",
  "Un beso muy grande,<br>tu abuela Remedios"],
 "items": [
  {"n": 1, "q": "Remedios escribe a Álex para...", "o": ["invitarle a una boda en el puerto.", "contarle una celebración y pedirle ayuda.", "felicitarle por su nuevo trabajo en un hospital."], "ok": 1,
   "cats": ["planes", "personas"], "es": "ES-02", "pc": "te escribo porque... · ¿puedes preparar...?",
   "why": "Remedios le cuenta que celebran sus bodas de oro y le pide un vídeo con fotos. La boda en el puerto fue en 1976, y Álex ha terminado unas prácticas: no tiene un trabajo nuevo."},
  {"n": 2, "q": "La fiesta va a ser...", "o": ["en el restaurante donde se casaron.", "en un local del ayuntamiento.", "en una casa con jardín."], "ok": 2,
   "cats": ["planes", "lugares"], "es": "ES-05", "pc": "al principio pensábamos..., pero... así que al final",
   "why": "Al final la hacen en el jardín de la casa del pueblo. El restaurante era el primer plan, y el ayuntamiento solo presta las mesas y las sillas."},
  {"n": 3, "q": "Para la comida...", "o": ["Sergio va a cocinar el plato principal.", "la tía Pilar va a hacer los postres.", "Remedios va a preparar la paella."], "ok": 0,
   "cats": ["personas"], "es": "ES-08", "pc": "tu primo Sergio va a preparar... · yo solo hago los postres",
   "why": "El primo Sergio, que es cocinero, prepara la paella. Los postres los hace Remedios, y la tía Pilar se ocupa de las mesas y las sillas."},
  {"n": 4, "q": "Al principio, el abuelo...", "o": ["prefería celebrarlo solo con su mujer.", "quería invitar a sus hermanos.", "pensaba viajar a Argentina."], "ok": 0,
   "cats": ["pasados", "opinion"], "es": "ES-05", "pc": "no quería · decía que lo mejor era (imperfecto) · cambió de opinión (indefinido)",
   "why": "El abuelo quería una cena tranquila en casa, los dos solos. Cambió de opinión cuando supo que venían sus hermanos: no fue idea suya invitarlos."},
  {"n": 5, "q": "Remedios le propone a Álex...", "o": ["comprar un ordenador nuevo.", "elegir las fotos con ella antes de la fiesta.", "traer fotos de su madre de pequeña."], "ok": 1,
   "cats": ["planes", "tiempo"], "es": "ES-03", "pc": "si vienes el puente de mayo, las miramos juntos",
   "why": "Le propone mirar juntos las fotos en el puente de mayo y elegir las mejores. Las fotos las tiene ella: Álex solo tiene que llevar su ordenador."},
 ]}

CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 15 minutos: menos de dos minutos por anuncio. Lee la pregunta primero y busca solo ese dato. La opción buena casi nunca repite las palabras del anuncio: dice lo mismo de otra forma.",
 "example": {"title": "COLEGIO SAN PABLO · RECOGIDA DE ROPA",
   "body": "Del 3 al 14 de marzo recogemos ropa de abrigo, mantas y calzado para la Cruz Roja del barrio. Este año queremos llegar a mil prendas. Solo aceptamos prendas limpias y en buen estado. Podéis dejar las bolsas en la portería, de lunes a viernes, de 8:30 a 17:00. Los alumnos de sexto van a clasificar la ropa el último viernes. ¡Gracias por vuestra ayuda!",
   "q": "En el colegio...", "o": ["recogen ropa de verano.", "aceptan solo ropa limpia.", "los alumnos llevan la ropa a la Cruz Roja."], "ok": 1,
   "why": "La opción correcta es la B porque solo aceptan prendas limpias y en buen estado."},
 "items": [
  {"n": 6, "title": "AYUNTAMIENTO DE SAN VICENTE · RECOGIDA DE MUEBLES",
   "body": "¿Tienes un sofá, un colchón o una mesa que ya no usas? El servicio es gratuito, pero hay que pedir cita antes por teléfono o en la web municipal. El camión pasa los martes por la noche: deja los muebles en la puerta de tu portal después de las nueve. Por favor, no dejes bolsas de basura al lado: el camión no las recoge. Los electrodomésticos (lavadoras, frigoríficos...) solo se pueden llevar al punto limpio.",
   "q": "Para tirar un mueble viejo...", "o": ["hay que pagar un precio pequeño.", "hay que avisar antes al ayuntamiento.", "se puede dejar en la calle cualquier día."], "ok": 1,
   "cats": ["normas"], "es": "ES-03", "pc": "hay que pedir cita = avisar antes · gratuito · los martes",
   "why": "Hay que pedir cita antes, es decir, avisar al ayuntamiento. El servicio es gratis, y los muebles solo se dejan los martes por la noche."},
  {"n": 7, "title": "AUTOESCUELA RUEDA · CURSO INTENSIVO DE VERANO",
   "body": "Saca el carné de coche en julio. Clases teóricas por la mañana, de lunes a jueves; las prácticas, cuando tú quieras, también los sábados. Grupos de ocho alumnos como máximo. La matrícula cuesta 90 € y este mes tiene un 50 % de descuento para estudiantes con carné joven. El precio de las clases prácticas no cambia: 30 € cada una. La primera clase práctica es gratis. Oferta válida hasta el 30 de junio.",
   "q": "En esta autoescuela...", "o": ["las clases prácticas son más baratas para los estudiantes.", "la primera clase teórica es gratis.", "se pueden hacer prácticas el fin de semana."], "ok": 2,
   "cats": ["cantidad", "tiempo"], "es": "ES-04", "pc": "también los sábados · la matrícula / las clases prácticas",
   "why": "Las prácticas se pueden hacer también los sábados. El descuento es solo para la matrícula, y la clase gratis es la primera práctica, no la teórica."},
  {"n": 8, "title": "SE ALQUILA PLAZA DE GARAJE · CALLE OLIVO, 22",
   "body": "Plaza grande para coche, en el primer sótano, al lado del ascensor. 65 € al mes, gastos de comunidad incluidos. También sirve para dos motos. No se pueden guardar muebles ni cajas. Hay cámaras de seguridad. Se alquila desde el 1 de septiembre, mínimo seis meses. El mando de la puerta cuesta 20 € de fianza (te los devolvemos al final). Llamar por las tardes a Merche.",
   "q": "Según el anuncio...", "o": ["no se puede alquilar solo para un mes.", "el precio no incluye los gastos de la comunidad.", "la plaza sirve solo para un coche."], "ok": 0,
   "cats": ["normas", "cantidad"], "es": "ES-03", "pc": "mínimo seis meses · gastos incluidos · también sirve para dos motos",
   "why": "Hay que alquilarla un mínimo de seis meses: no se puede alquilar solo un mes. Los gastos están incluidos, y también sirve para dos motos."},
  {"n": 9, "title": "FORO «MOVERSE POR LA CIUDAD»",
   "body": "Respuesta de Toni_84:<br>Yo antes iba al trabajo en coche, pero desde enero uso el abono joven: 20 € al mes para metro, autobús y tranvía, sin límite de viajes. Al principio pensaba que iba a tardar más, pero ahora llego antes y leo en el tren. Lo único malo: los fines de semana el tranvía pasa cada veinte minutos. Mi novia tiene más de treinta años y paga el abono normal, el doble.",
   "q": "Toni cuenta que...", "o": ["el abono joven solo sirve para el metro.", "su novia también tiene el abono joven.", "en transporte público tarda menos que antes."], "ok": 2,
   "cats": ["pasados", "personas"], "es": "ES-05", "pc": "al principio pensaba..., pero ahora llego antes",
   "why": "Ahora llega antes que cuando iba en coche: tarda menos. El abono sirve para metro, autobús y tranvía, y su novia paga el abono normal."},
  {"n": 10, "title": "MUSEO DEL MAR · ENTRADA GRATUITA",
   "body": "Todos los domingos por la tarde, de 16:00 a 19:00, la entrada al museo es gratuita, excepto para la exposición temporal «Barcos del mundo», que cuesta 4 €. Los menores de 12 años y los mayores de 65 entran gratis todos los días. Las visitas guiadas (sábados a las 11:00) hay que reservarlas en la web. La cafetería del museo tiene una terraza con vistas al puerto. Los lunes, cerrado.",
   "q": "En este museo...", "o": ["los niños pequeños no pagan nunca.", "la exposición de barcos es gratis los domingos.", "se puede ir con guía sin reservar."], "ok": 0,
   "cats": ["normas", "cantidad"], "es": "ES-06", "pc": "excepto · todos los días · hay que reservarlas",
   "why": "Los menores de doce años entran gratis todos los días: no pagan nunca. La exposición de barcos cuesta cuatro euros también los domingos, y las visitas guiadas hay que reservarlas."},
  {"n": 11, "title": "CERCANÍAS · LÍNEA C3 · AVISO A LOS VIAJEROS",
   "body": "Del 7 al 20 de abril, por obras en la vía, no hay trenes entre Las Arenas y Villanueva. Un autobús gratuito sustituye al tren en ese tramo: sale cada 30 minutos desde la puerta principal de la estación. Hay que llevar el billete del tren. Las bicicletas no pueden subir al autobús. El viaje dura unos 15 minutos más. En el resto de la línea, los horarios son los de siempre.",
   "q": "Durante las obras, los viajeros que van de Las Arenas a Villanueva...", "o": ["tienen que comprar un billete de autobús.", "van a tardar un poco más.", "no pueden usar el transporte público."], "ok": 1,
   "cats": ["tiempo", "normas"], "es": "ES-03", "pc": "dura unos 15 minutos más = tardar un poco más · gratuito",
   "why": "El viaje en el autobús dura unos quince minutos más: tardan un poco más. El autobús es gratis con el billete del tren."},
  {"n": 12, "title": "ASOCIACIÓN DE VECINOS DEL CARMEN · CONCURSO DE FOTOGRAFÍA",
   "body": "Tema de este año: «Mi barrio por la noche». Pueden participar todos los vecinos mayores de 16 años, con un máximo de dos fotos cada uno. Las fotos se envían por correo electrónico antes del 30 de octubre. No es necesario tener una cámara profesional: también aceptamos fotos hechas con el móvil. Las diez mejores se exponen en el centro cívico en diciembre. Premio: una cena para dos en el restaurante La Lonja.",
   "q": "Para participar en el concurso...", "o": ["hay que usar una cámara profesional.", "se puede presentar más de una foto.", "hay que llevar las fotos a la asociación."], "ok": 1,
   "cats": ["normas"], "es": "ES-03", "pc": "un máximo de dos fotos = más de una · no es necesario · por correo electrónico",
   "why": "Cada vecino puede presentar hasta dos fotos: más de una. No hace falta una cámara profesional, y las fotos se envían por correo electrónico."},
  {"n": 13, "title": "ZAPATERÍA PASO A PASO · CAMBIOS Y DEVOLUCIONES",
   "body": "Tienes 30 días para cambiar tu compra, con el tique y los zapatos sin usar. Si prefieres el dinero, solo lo devolvemos en los primeros 15 días; después, te damos un vale para gastar en la tienda. Los artículos rebajados no se pueden devolver, pero sí cambiar por otra talla. La ropa interior y los calcetines no se cambian. Calzado deportivo con un 10 % de descuento hasta el domingo.",
   "q": "En esta zapatería, unos zapatos rebajados...", "o": ["se pueden cambiar por otro número.", "se pueden devolver en los primeros 15 días.", "tienen un 10 % de descuento más."], "ok": 0,
   "cats": ["normas", "cantidad"], "es": "ES-06", "pc": "no se pueden devolver, pero sí cambiar por otra talla",
   "why": "Los rebajados se pueden cambiar por otra talla, es decir, por otro número. No se pueden devolver, y el diez por ciento es para el calzado deportivo."},
 ]}

CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos de tres personas que trabajan de noche. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 15 minutos. Lee primero las seis preguntas. Las tres personas tienen un trabajo parecido: busca el detalle que las separa (por qué eligieron la noche, cuántos días trabajan, qué hacen en las horas tranquilas, quién las ayudó a empezar).",
 "texts": [
  {"name": "Marisa", "body": "Trabajo de recepcionista en un hotel del centro de Sevilla desde hace seis años, siempre de once de la noche a siete de la mañana. Antes trabajaba de día, pero cuando nació mi hijo pedí el turno de noche: así lo llevo al colegio por la mañana y por la tarde estoy con él. Duermo de ocho a dos y luego voy a buscarlo. Lo más difícil es el verano, porque los turistas llegan muy tarde. Por la noche hay poco trabajo, así que estudio alemán con el ordenador de la recepción. Mi jefe dice que el año que viene puedo pasar al turno de mañana, pero yo no quiero."},
  {"name": "Fermín", "body": "Soy conductor del autobús nocturno de Madrid, el que llaman «el búho». Empiezo a las doce y media y termino a las seis. Llevo once años en esta línea. Elegí este horario porque se cobra más y porque por la noche no hay atascos. Al principio dormía muy mal de día, pero ya me he acostumbrado. Mis pasajeros son muy variados: jóvenes que vuelven de fiesta, enfermeras, panaderos, limpiadores... A algunos los conozco desde hace años y ya sé dónde se bajan. Lo peor es que veo poco a mi familia: cuando llego a casa, mi mujer ya se ha ido a trabajar. Por eso, por la tarde, antes de salir de casa, siempre ceno con mis hijos."},
  {"name": "Andrea", "body": "Soy vigilante en un museo de arte de Bilbao. Hago tres noches a la semana, de diez a seis, y los otros días estudio Historia del Arte en la universidad. Empecé en este trabajo por una amiga, que lo hacía antes que yo y me recomendó. Antes de empezar, hice un curso de seguridad de dos semanas. Por la noche recorro las salas cada hora con una linterna y miro las cámaras. Al principio me daban un poco de miedo los ruidos y las estatuas en la oscuridad, pero ahora me encanta: tengo los cuadros para mí sola. El año que viene termino la carrera y me gustaría ser guía en el mismo museo."}],
 "items": [
  {"n": 14, "q": "¿Quién eligió trabajar de noche por su familia?", "ok": 0, "cats": ["personas", "pasados"], "es": "ES-09", "pc": "cuando nació mi hijo pedí el turno de noche",
   "why": "Marisa pidió el turno de noche cuando nació su hijo, para estar con él. Fermín habla de su familia, pero eligió la noche por el dinero y por el tráfico."},
  {"n": 15, "q": "¿Quién gana más dinero gracias a su horario?", "ok": 1, "cats": ["cantidad"], "es": "ES-03", "pc": "se cobra más",
   "why": "Fermín eligió la noche porque se cobra más: gana más dinero."},
  {"n": 16, "q": "¿Quién trabaja solo algunos días de la semana?", "ok": 2, "cats": ["tiempo"], "es": "ES-09", "pc": "tres noches a la semana",
   "why": "Andrea trabaja tres noches a la semana; los otros días estudia. Marisa y Fermín hablan de sus horas de trabajo, pero no dicen que trabajen solo algunos días."},
  {"n": 17, "q": "¿Quién aprovecha las horas tranquilas del trabajo para aprender algo?", "ok": 0, "cats": ["opinion"], "es": "ES-09", "pc": "hay poco trabajo, así que estudio alemán",
   "why": "Marisa estudia alemán en la recepción cuando hay poco trabajo. Andrea estudia en la universidad, pero los días que no trabaja."},
  {"n": 18, "q": "¿Quién consiguió el trabajo gracias a otra persona?", "ok": 2, "cats": ["personas", "pasados"], "es": "ES-08", "pc": "por una amiga, que me recomendó",
   "why": "Una amiga de Andrea, que trabajaba allí antes, la recomendó."},
  {"n": 19, "q": "¿Quién conoce desde hace tiempo a algunas de las personas que atiende?", "ok": 1, "cats": ["tiempo", "personas"], "es": "ES-03", "pc": "a algunos los conozco desde hace años",
   "why": "Fermín conoce a algunos pasajeros desde hace años y sabe dónde se bajan."}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un reportaje sobre un hombre de sesenta y ocho años que ha vuelto a estudiar. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto: cada párrafo responde, más o menos, a una pregunta. Atención a lo que Julián pensaba hacer y a lo que hizo de verdad, y a quién hace cada cosa.",
 "title": "Julián vuelve a clase",
 "sub": "Periódico «La Voz de Elche» · Gente del barrio",
 "body": [
  "Son las siete de la tarde y en el aula 4 del Centro de Educación de Personas Adultas de Elche hay doce alumnos. El mayor se llama Julián Sempere, tiene sesenta y ocho años y es siempre el primero en llegar. Lleva una mochila azul, un estuche lleno de bolígrafos de colores y, todos los días, un termo de café para la profesora.",
  "Julián dejó el colegio a los trece años. Su padre tenía un taller de fontanería y necesitaba ayuda, así que empezó a trabajar con él. «Me gustaba estudiar, sobre todo las matemáticas, pero en mi casa no había dinero para seguir», recuerda. Durante cuarenta y cinco años arregló grifos, calderas y tuberías por toda la provincia. Se casó, tuvo tres hijas y nunca volvió a abrir un libro de texto.",
  "Cuando se jubiló, en 2021, pensaba dedicarse a su huerto y a jugar a la petanca. Pero un día su nieta Laia, que entonces tenía diez años, le pidió ayuda con unos problemas de matemáticas y él no supo hacerlos. «Me dio mucha vergüenza», cuenta. Esa misma semana fue al centro de adultos a preguntar. Primero quería hacer solo un curso corto de matemáticas, pero la directora le convenció para estudiar la secundaria completa.",
  "Tardó dos años en terminarla. Las clases son de lunes a jueves, por la tarde, y el resto del tiempo estudia en la biblioteca municipal, porque en casa, dice, su mujer pone la televisión muy alta. Lo más difícil para él fue el inglés: «Al principio no entendía nada, pero ahora veo películas en versión original con subtítulos». Lo que más le gusta es la historia. Algunos días está tan cansado que se duerme en el sofá con el libro abierto.",
  "En junio del año pasado aprobó todos los exámenes con buenas notas y este curso ha empezado el bachillerato, también en el centro de adultos. Sus compañeros son muy distintos: hay chicos de veinte años que dejaron el instituto, una cocinera que quiere ser enfermera y un taxista colombiano. «Ellos me ayudan con el ordenador y yo les explico matemáticas», dice riéndose.",
  "Su sueño es estudiar Historia en la universidad. Su familia le apoya, aunque su mujer, Rosa, no lo entendía al principio: «¿A tu edad, para qué?», le preguntaba. Ahora es ella la que le prepara el termo de café cada tarde. Y Laia, que ya tiene catorce años, a veces hace los deberes con su abuelo en la mesa de la cocina."],
 "items": [
  {"n": 20, "q": "Según el texto, Julián...", "o": ["es el alumno que más tiempo lleva en el centro.", "lleva algo para su profesora todos los días.", "llega a clase a las siete en punto."], "ok": 1,
   "cats": ["personas"], "es": "ES-04", "pc": "el mayor / el primero en llegar · un termo de café para la profesora",
   "why": "Todos los días lleva un termo de café para la profesora. Es el mayor y el primero en llegar, pero el texto no dice que lleve más tiempo en el centro ni a qué hora llega."},
  {"n": 21, "q": "Julián dejó los estudios porque...", "o": ["no le gustaba ir al colegio.", "tenía que trabajar con su familia.", "suspendía las matemáticas."], "ok": 1,
   "cats": ["pasados", "personas"], "es": "ES-03", "pc": "su padre necesitaba ayuda · me gustaba estudiar",
   "why": "Su padre necesitaba ayuda en el taller y no había dinero para seguir. A Julián le gustaba estudiar, sobre todo las matemáticas."},
  {"n": 22, "q": "Julián decidió volver a estudiar...", "o": ["después de no poder ayudar a su nieta.", "porque se lo aconsejó su mujer.", "para hacer solo un curso de matemáticas."], "ok": 0,
   "cats": ["pasados", "planes"], "es": "ES-05", "pc": "no supo hacerlos · primero quería..., pero la directora le convenció",
   "why": "No supo hacer los problemas de su nieta y le dio vergüenza. El curso corto era su primera idea, pero al final estudió la secundaria completa; su mujer, al principio, no lo entendía."},
  {"n": 23, "q": "Cuando no tiene clase, Julián...", "o": ["prefiere estudiar fuera de su casa.", "ve la televisión en inglés con su mujer.", "estudia sobre todo historia."], "ok": 0,
   "cats": ["lugares", "opinion"], "es": "ES-03", "pc": "estudia en la biblioteca, porque en casa su mujer pone la televisión muy alta",
   "why": "Estudia en la biblioteca porque en casa hay mucho ruido. Las películas en inglés las ve él, y la historia es lo que más le gusta, no lo que más estudia."},
  {"n": 24, "q": "Este curso, Julián...", "o": ["ha terminado la secundaria.", "estudia con compañeros de edades distintas.", "ha empezado en la universidad."], "ok": 1,
   "cats": ["pasados", "personas"], "es": "ES-07", "pc": "en junio del año pasado aprobó · este curso ha empezado",
   "why": "En el bachillerato tiene compañeros muy distintos, también chicos de veinte años. La secundaria la terminó el curso pasado, y la universidad es su sueño para el futuro."},
  {"n": 25, "q": "Según el último párrafo, Rosa...", "o": ["siempre apoyó la idea de Julián.", "hace los deberes con su nieta.", "ahora le prepara algo cada día antes de clase."], "ok": 2,
   "cats": ["opinion", "personas"], "es": "ES-08", "pc": "no lo entendía al principio · ahora es ella la que le prepara",
   "why": "Ahora Rosa le prepara el termo de café cada tarde. Al principio no lo entendía, y la que hace los deberes con el abuelo es Laia, la nieta."},
 ]}

# ---------------- AUDITIVA ----------------
# Sin efectos de sonido (como el examen real). Cada intervención empieza con una etiqueta de emoción de ElevenLabs v3
# (en inglés, entre corchetes): va al guion, no a las transcripciones.
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación: las tres aparecen en el audio. Fíjate en la pregunta: ¿qué ha hecho ya?, ¿dónde trabaja ahora?, ¿qué tiene que llevar? La primera cosa que se dice casi nunca es la buena.",
 "example": {"q": "¿Qué ha arreglado ya el técnico?", "o": ["la lavadora", "el horno", "el lavavajillas"], "ok": 1,
   "pres": "Va a escuchar a una mujer que habla con un técnico en su casa.",
   "lines": [("Mujer", "RAQUEL", "[curious] Buenos días. ¿Qué tal? ¿Ya funciona la lavadora?"),
             ("Hombre", "MARTIN_3", "[sighs] Todavía no, señora. Necesito una pieza y no llega hasta el jueves. El horno, en cambio, ya está: era el cable. Y le he cambiado la luz, que no funcionaba."),
             ("Mujer", "RAQUEL", "[relieved] ¡Ay, menos mal! ¿Y el lavavajillas? Hace un ruido muy raro..."),
             ("Hombre", "MARTIN_3", "[thoughtful] Eso lo miro el jueves. Vuelvo con la pieza y lo hago todo el mismo día.")],
   "solucion": "La opción correcta es la letra be. Ha arreglado el horno.",
   "img": "M07_CA1_0_lavadora_horno_lavavajillas.jpg",
   "prompt": "Panel 1: a front-loading washing machine. Panel 2: a kitchen oven. Panel 3: an open dishwasher with plates."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Dónde trabaja ahora Elena?", "o": ["en una residencia de mayores", "en una farmacia", "en un hospital"], "ok": 0,
   "cats": ["pasados", "lugares"], "es": "ES-07", "pc": "eso era antes · después estuvo... · ahora trabaja",
   "pres": "Va a escuchar a dos amigos que hablan de una compañera de la universidad.",
   "lines": [("Hombre", "GABRIEL_ES", "[surprised] ¿Sabes a quién vi ayer? A Elena, la de la universidad. Estaba en la farmacia de la plaza."),
             ("Mujer", "ESTELA", "[laughs] Seguramente fue a comprar algo. En esa farmacia trabajó dos años, pero eso era antes. Después estuvo unos meses en el hospital..."),
             ("Hombre", "GABRIEL_ES", "[curious] ¿Y ahora?"),
             ("Mujer", "ESTELA", "[warm] Ahora trabaja en una residencia de mayores, cerca de casa de sus padres. Dice que le encanta."),
             ("Hombre", "GABRIEL_ES", "[amused] ¡Qué cambio! Pues ayer la vi muy contenta.")],
   "why": "Ahora trabaja en una residencia de mayores. En la farmacia trabajó antes, y en el hospital estuvo unos meses después.",
   "img": "M07_CA1_1_residencia_farmacia_hospital.jpg", "prompt": "Panel 1: a caregiver with an elderly woman in a care home lounge. Panel 2: a pharmacy counter with shelves of medicines. Panel 3: a hospital corridor with a nurse."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Qué deporte hace ahora el hombre?", "o": ["correr", "nadar", "montar en bici"], "ok": 2,
   "cats": ["pasados", "opinion"], "es": "ES-05", "pc": "¿sigues...? · qué va · primero probé..., pero · ahora voy en bici",
   "pres": "Va a escuchar a una mujer y a un hombre que trabajan juntos.",
   "lines": [("Mujer", "CAROLINA", "[cheerful] ¡Qué moreno estás, Pedro! ¿Sigues corriendo por el río?"),
             ("Hombre", "EMILIO", "[sighs] Qué va. Me hice daño en la rodilla en marzo y el médico me dijo que nada de correr. Primero probé la natación, pero el cloro me molesta en los ojos..."),
             ("Mujer", "CAROLINA", "[curious] ¿Entonces?"),
             ("Hombre", "EMILIO", "[happy] Ahora vengo en bici al trabajo todos los días, y los domingos hago rutas por la sierra con mi cuñado. Por eso estoy tan moreno. Bueno, mi cuñado va mucho más rápido que yo, claro.")],
   "why": "Ahora va en bici al trabajo y hace rutas los domingos. Correr lo dejó por la rodilla, y la natación la probó, pero no le gustó por el cloro.",
   "img": "M07_CA1_2_correr_nadar_bici.jpg", "prompt": "Panel 1: a man running along a river path. Panel 2: a man swimming in an indoor pool. Panel 3: a man riding a bicycle on a mountain road."},
  {"n": 3, "conv": "Conversación tres", "q": "¿Qué han reservado ya para la cena de la empresa?", "o": ["el restaurante", "el autobús", "un grupo de música"], "ok": 1,
   "cats": ["planes", "tiempo"], "es": "ES-07", "pc": "no he reservado todavía · eso ya está: lo reservé ayer",
   "pres": "Va a escuchar a dos compañeras de trabajo que organizan la cena de Navidad.",
   "lines": [("Mujer", "SUSANA", "[stressed] A ver, Inma, ¿cómo vamos con la cena de Navidad? ¿Has llamado al restaurante?"),
             ("Mujer", "VALENTINA", "[calm] Sí, pero solo tienen sitio el día veinte, y Paco quiere el diecinueve. Todavía no he reservado: lo decidimos mañana en la reunión."),
             ("Mujer", "SUSANA", "[nervous] Vale. ¿Y el autobús para volver?"),
             ("Mujer", "VALENTINA", "[proud] Eso ya está: lo reservé ayer, para las doce y media. Lo de la música, ni idea. ¿Contratamos un grupo o la ponemos nosotras?"),
             ("Mujer", "SUSANA", "[laughs] Nosotras, que es gratis.")],
   "why": "El autobús ya está reservado desde ayer. El restaurante todavía no, porque no se ponen de acuerdo con el día, y la música la van a poner ellas.",
   "img": "M07_CA1_3_restaurante_autobus_grupo.jpg", "prompt": "Panel 1: a restaurant dining room with set tables. Panel 2: a coach bus parked at night. Panel 3: a small music band with a guitar and a microphone."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿A qué hora sale el autobús que va a coger la chica?", "o": ["a las ocho y diez", "a las ocho y cuarenta", "a las nueve"], "ok": 1,
   "cats": ["tiempo", "planes"], "es": "ES-07", "pc": "ya no sale a... · a las nueve sale el directo, pero · yo cojo el de",
   "pres": "Va a escuchar a una chica que habla por teléfono con su padre.",
   "lines": [("Mujer", "CRISTINA", "[worried] Papá, ¿me recoges mañana en la estación? Es que el autobús ya no sale a las ocho y diez: han cambiado el horario."),
             ("Hombre", "JAVIER", "[calm] ¿Y a qué hora sale ahora? ¿A las nueve?"),
             ("Mujer", "CRISTINA", "[explaining] No, a las nueve sale el directo, pero es mucho más caro. Yo cojo el de las ocho y cuarenta, que para en todos los pueblos."),
             ("Hombre", "JAVIER", "[teasing] Vale, hija. Pues entonces llegas tardísimo... Llámame al salir. Y coge el paraguas, que mañana llueve.")],
   "why": "Va a coger el autobús de las ocho y cuarenta. El de las ocho y diez ya no existe, y el de las nueve es el directo, que es más caro.",
   "img": "M07_CA1_4_reloj_ocho_diez_ocho_cuarenta_nueve.jpg", "prompt": "Panel 1: an analogue clock showing ten past eight. Panel 2: an analogue clock showing twenty to nine. Panel 3: an analogue clock showing nine o'clock."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Qué tiene que llevar la mujer al curso de cerámica?", "o": ["un delantal", "una toalla", "barro"], "ok": 0,
   "cats": ["normas"], "es": "ES-06", "pc": "están incluidos · le dejamos también · sí tiene que traer",
   "pres": "Va a escuchar a una mujer que llama por teléfono a un taller de cerámica.",
   "lines": [("Mujer", "SARA", "[polite] Hola, buenas tardes. Llamo por el curso de cerámica del sábado. ¿Tengo que llevar algo? ¿El barro, las herramientas...?"),
             ("Hombre", "DAVID_M1", "[friendly] No, no, el barro y las herramientas están incluidos. También le dejamos una toalla para las manos."),
             ("Mujer", "SARA", "[hesitant] ¿Y un delantal? Porque yo no tengo..."),
             ("Hombre", "DAVID_M1", "[friendly] Delantal sí tiene que traer, o una camiseta vieja, porque se mancha mucho. Ah, y el pelo recogido."),
             ("Mujer", "SARA", "[thoughtful] Vale... Creo que tengo uno de cocina por algún sitio. Muchas gracias.")],
   "why": "Tiene que llevar un delantal o una camiseta vieja. El barro está incluido y la toalla se la dejan en el taller.",
   "img": "M07_CA1_5_delantal_toalla_barro.jpg", "prompt": "Panel 1: a work apron. Panel 2: a folded hand towel. Panel 3: a block of grey modelling clay."},
  {"n": 6, "conv": "Conversación seis", "q": "¿Dónde están las llaves del vecino?", "o": ["en el buzón", "debajo del felpudo", "en la panadería"], "ok": 2,
   "cats": ["lugares", "personas"], "es": "ES-05", "pc": "al final no las he dejado en... · eso no es seguro · las tiene Paco, el de la panadería",
   "pres": "Va a escuchar a dos vecinos que hablan por teléfono.",
   "lines": [("Hombre", "ERIK", "[hurried] Lola, soy Marcos, el del segundo. Me voy ya de viaje. Te dejo las llaves para regar las plantas, ¿vale? Al final no las he dejado en el buzón, que está roto."),
             ("Mujer", "LUCIA", "[confused] ¿Entonces? ¿Debajo del felpudo, como siempre?"),
             ("Hombre", "ERIK", "[laughs] No, mujer, eso no es seguro. Las tiene Paco, el de la panadería de abajo. Pásate cuando quieras."),
             ("Mujer", "LUCIA", "[cheerful] Perfecto. ¿Y cuándo vuelves? ¿El domingo?"),
             ("Hombre", "ERIK", "[hurried] No, el lunes por la noche. ¡Muchas gracias, Lola!")],
   "why": "Las llaves las tiene Paco, en la panadería. El buzón está roto, y debajo del felpudo no es seguro.",
   "img": "M07_CA1_6_buzon_felpudo_panaderia.jpg", "prompt": "Panel 1: a row of metal mailboxes in a building entrance. Panel 2: a doormat in front of a flat door. Panel 3: a small bakery counter with bread."},
 ]}

CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. Las opciones falsas usan palabras que sí se oyen (los sábados, los domingos, gratis), pero con otro dato. La buena suele decir lo mismo con otras palabras.",
 "example": {"q": "En este programa...", "o": ["hoy hablan de salud.", "solo ponen música.", "dan las noticias de la noche."], "ok": 0,
   "why": "La opción correcta es la A porque hoy hablan de cómo dormir mejor con una médica.",
   "lab": "Locutor", "voice": "DANIEL_CO/RADIO",
   "text": "[warm] ¡Buenos días! Son las siete y en «Despierta con nosotros» os acompañamos hasta las diez con noticias, el tiempo y vuestras llamadas. Hoy hablamos con una médica del sueño de cómo dormir mejor. ¿Tenéis alguna pregunta? Escribidnos un mensaje. Y a las nueve, como siempre, el tráfico de la ciudad.",
   "solucion": "La opción correcta es la letra a, porque hoy hablan de cómo dormir mejor con una médica."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "Durante el mercado medieval...", "o": ["no puede pasar ningún vehículo por la calle Mayor.", "algunos autobuses paran en otro sitio.", "el mercado está abierto solo el domingo."], "ok": 1,
   "cats": ["lugares", "normas"], "es": "ES-06", "pc": "cambian su recorrido y paran en · los taxis sí pueden pasar",
   "lab": "Locutor", "voice": "MARTIN_2/RADIO",
   "text": "[informative] Este fin de semana se celebra el mercado medieval en el casco antiguo. Por eso, desde el viernes por la tarde hasta el domingo por la noche, la calle Mayor está cerrada al tráfico. Los autobuses de las líneas tres y cinco cambian su recorrido y paran en la avenida del Puerto. Los taxis sí pueden pasar.",
   "why": "Los autobuses de las líneas tres y cinco cambian su recorrido y paran en la avenida del Puerto. Los taxis sí pueden pasar, y el mercado es todo el fin de semana."},
  {"n": 8, "conv": "Audio 2", "q": "Según el anuncio, en la óptica...", "o": ["la segunda montura es más barata.", "hay que pedir cita para revisar la vista.", "las lentillas tienen descuento este mes."], "ok": 0,
   "cats": ["cantidad", "normas"], "es": "ES-03", "pc": "a mitad de precio · sin cita · como siempre",
   "lab": "Locutora", "voice": "GABI/RADIO",
   "text": "[excited] ¡Óptica Visión Clara cumple veinte años! Y para celebrarlo, durante todo el mes, si te compras unas gafas graduadas, la segunda montura te sale a mitad de precio. Revisión de la vista gratis y sin cita, de lunes a viernes. Y las lentillas, como siempre, al mejor precio. Estamos en la calle Colón, al lado del mercado.",
   "why": "La segunda montura sale a mitad de precio: es más barata. La revisión es sin cita, y las lentillas tienen el precio de siempre."},
  {"n": 9, "conv": "Audio 3", "q": "Según el programa, para gastar menos luz...", "o": ["es mejor lavar la ropa con agua caliente.", "hay que comprar bombillas baratas.", "hay que apagar algunos aparatos por la noche."], "ok": 2,
   "cats": ["cantidad", "opinion"], "es": "ES-04", "pc": "agua fría · un poco más caras · apaga la tele y el ordenador",
   "lab": "Locutora", "voice": "CAROLINA/RADIO",
   "text": "[calm] En «Tu casa, tu dinero», consejos para gastar menos luz este invierno. Pon la lavadora con agua fría y llena: gastas casi la mitad. Apaga la tele y el ordenador por la noche. Y si cambias las bombillas, elige las de bajo consumo: son un poco más caras, pero duran años.",
   "why": "Aconsejan apagar la tele y el ordenador por la noche. La lavadora, con agua fría, y las bombillas de bajo consumo son un poco más caras."},
  {"n": 10, "conv": "Audio 4", "q": "En Ciclos Martín...", "o": ["venden bicis de segunda mano.", "si llevas pronto la bici, te la arreglan en un día.", "la revisión de la bici es gratis."], "ok": 1,
   "cats": ["tiempo", "cantidad"], "es": "ES-03", "pc": "antes del viernes · al día siguiente · te compramos la vieja",
   "lab": "Locutor", "voice": "ELEGUAR/RADIO",
   "text": "[enthusiastic] ¿Tu bici está guardada en el trastero desde el verano? En Ciclos Martín te la ponemos a punto por solo veinticinco euros: frenos, cadena y ruedas. Si la traes antes del viernes, te la devolvemos al día siguiente. Y si quieres cambiar de bici, te compramos la vieja. Abrimos también los sábados por la mañana.",
   "why": "Si llevas la bici antes del viernes, te la devuelven al día siguiente. La revisión cuesta veinticinco euros, y la tienda compra bicis viejas, no las vende."},
  {"n": 11, "conv": "Audio 5", "q": "Para la obra de teatro...", "o": ["quedan entradas para la tarde.", "los niños de tres años no pagan.", "hay funciones todo el fin de semana."], "ok": 0,
   "cats": ["tiempo", "cantidad"], "es": "ES-06", "pc": "la de la mañana ya está completa · menores de tres años",
   "lab": "Locutor", "voice": "MARTIN_1/RADIO",
   "text": "[cheerful] Este domingo, en el Teatro Principal, llega «El dragón que no sabía volar», una obra para niños de tres a ocho años. Hay dos funciones, a las doce y a las cinco y media. La de la mañana ya está completa. Las entradas cuestan seis euros y los menores de tres años no pagan.",
   "why": "La función de la mañana está completa, así que solo quedan entradas para la de la tarde. Los que no pagan son los menores de tres años, y la obra es solo el domingo."},
  {"n": 12, "conv": "Audio 6", "q": "Para participar en el concurso...", "o": ["hay que escribir un mensaje.", "hay que llamar por teléfono.", "hay que ir el lunes a la radio."], "ok": 1,
   "cats": ["normas", "tiempo"], "es": "ES-06", "pc": "no vale mandar un mensaje · tiene que ser una llamada · el ganador, el lunes",
   "lab": "Locutora", "voice": "RAQUEL/RADIO",
   "text": "[excited] ¡Concurso! ¿Quieres ganar dos noches en un hotel de la costa? Llama al programa entre las cinco y las seis y contesta a tres preguntas sobre nuestra ciudad. Pero ojo: no vale mandar un mensaje, tiene que ser una llamada. El nombre del ganador lo decimos el lunes, en directo. ¡Mucha suerte!",
   "why": "Hay que llamar al programa: los mensajes no valen. El lunes solo dicen el nombre del ganador."},
 ]}

CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Paula y Rubén. Indique si los enunciados (del 13 al 18) se refieren a Paula (A), a Rubén (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Paula y Rubén hablan de la comida y de cocinar. Cuidado con lo que hace otra persona (la hermana de Rubén) y con los planes que no se hacen: en esos casos, la respuesta es C.",
 "who": ["Paula", "Rubén"], "voices": {"PAULA": "MIA", "RUBEN": "MILO"},
 "lines": [
  ("RUBEN", "[surprised] ¡Paula! ¿Qué llevas en esas bolsas? ¿Vas a dar de comer a todo el barrio?"),
  ("PAULA", "[laughs] Casi. Es la compra de la semana. Los domingos cocino para toda la semana: lentejas, pollo, verduras... y lo guardo en táperes. Así no pienso cada día qué comer y ahorro mucho."),
  ("RUBEN", "[impressed] ¡Qué organizada! Yo últimamente pido casi todo a domicilio. Llego tan cansado del trabajo que no tengo ganas de cocinar."),
  ("PAULA", "[teasing] Ya, pero eso sale carísimo, ¿no?"),
  ("RUBEN", "[sighs] Muchísimo. El mes pasado me gasté doscientos euros solo en pizzas y hamburguesas. Mi hermana, que es cocinera en un hotel, me riñe cada vez que me ve."),
  ("PAULA", "[curious] Oye, ¿y por qué no hacemos el curso de cocina rápida del centro cívico? Es los jueves."),
  ("RUBEN", "[hesitates] Bueno... quería apuntarme en septiembre, pero al final no lo hice. Los jueves juego al pádel."),
  ("PAULA", "[laughing] ¡Excusas! Mira, yo antes también comía fatal. Cuando vivía con mis padres no sabía hacer ni un huevo frito. Aprendí con vídeos de internet."),
  ("RUBEN", "[thoughtful] Pues yo, al revés: antes cocinaba bastante. Cuando vivía en Bilbao con dos compañeros de piso, cada uno hacía la cena un día. Ahora, solo, me da pereza."),
  ("PAULA", "[curious] ¿Y no tienes ningún libro de cocina en casa?"),
  ("RUBEN", "[embarrassed] Sí... Mi hermana me regaló un libro de recetas fáciles por mi cumpleaños. Todavía no lo he abierto..."),
  ("PAULA", "[excited] ¡Pues ya está! El sábado vienes a mi casa, elegimos una receta del libro y la hacemos juntos."),
  ("RUBEN", "[amused] Vale, pero yo traigo el postre. Bueno... lo compro en la pastelería, ¿eh?"),
  ("PAULA", "[laughs] Me parece bien. Y la semana que viene cocinas tú en tu casa.")],
 "items": [
  {"n": 13, "q": "Prepara la comida de varios días de una vez.", "ok": 0, "cats": ["tiempo"], "es": "ES-03", "pc": "los domingos cocino para toda la semana",
   "why": "Paula cocina los domingos para toda la semana."},
  {"n": 14, "q": "Gasta mucho dinero en comida que no hace él mismo.", "ok": 1, "cats": ["cantidad"], "es": "ES-03", "pc": "pido a domicilio · me gasté doscientos euros",
   "why": "Rubén pide comida a domicilio y el mes pasado se gastó doscientos euros en pizzas y hamburguesas."},
  {"n": 15, "q": "Trabaja en una cocina.", "ok": 2, "cats": ["personas"], "es": "ES-08", "pc": "mi hermana, que es cocinera en un hotel",
   "why": "La cocinera es la hermana de Rubén, una tercera persona: ni Paula ni Rubén."},
  {"n": 16, "q": "Se ha apuntado a un curso de cocina.", "ok": 2, "cats": ["planes", "pasados"], "es": "ES-05", "pc": "quería apuntarme, pero al final no lo hice · ¿y por qué no hacemos...?",
   "why": "Rubén quería apuntarse, pero al final no lo hizo, y Paula solo lo propone: ninguno de los dos se ha apuntado."},
  {"n": 17, "q": "Aprendió a cocinar sola.", "ok": 0, "cats": ["pasados"], "es": "ES-03", "pc": "aprendí con vídeos de internet",
   "why": "Paula aprendió a cocinar con vídeos de internet, sin profesor."},
  {"n": 18, "q": "Va a llevar algo dulce el sábado.", "ok": 1, "cats": ["planes", "personas"], "es": "ES-07", "pc": "yo traigo el postre",
   "why": "Rubén va a llevar el postre a casa de Paula, aunque lo compra en la pastelería."}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. Hay parejas muy parecidas (dos de citas, dos de tiendas, dos de espectáculos): en cada mensaje pregúntate quién habla, dónde y qué cambia exactamente. Sobran tres enunciados.",
 "enun": [
  "Alguien cambia la hora de una cita.",
  "Un espectáculo se suspende por el mal tiempo.",
  "Alguien tiene que pedir una cita.",
  "Una tienda tiene un horario más largo estos días.",
  "Alguien ofrece hacer una compra.",
  "Alguien acepta una invitación.",
  "Un espectáculo empieza más tarde.",
  "Un servicio no funciona durante un viaje.",
  "Una tienda abre más tarde por la mañana.",
  "Algo que alguien había pedido ya está disponible.",
  "Alguien no puede ir a una celebración."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "SOFIA/RADIO",
   "text": "[friendly] Hola, Begoña, te llamo de la peluquería Rizos. Tu cita del jueves no es a las cinco, sino a las seis y media, porque Ana está enferma. Si no te va bien, llámanos y buscamos otro día. ¡Un beso!",
   "solucion": "La opción correcta es la letra a: alguien cambia la hora de una cita."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 3, "cats": ["tiempo", "normas"], "es": "ES-10", "pc": "megafonía · cierra a las diez, una hora más tarde de lo habitual",
   "lab": "Megafonía", "voice": "SANTIAGO_LAT/RADIO",
   "text": "[neutral] Estimados clientes: les recordamos que, durante las fiestas, el supermercado cierra a las diez de la noche, una hora más tarde de lo habitual. El domingo abrimos de diez a dos. El aparcamiento sigue siendo gratis durante dos horas. Gracias por su visita.",
   "why": "El supermercado cierra una hora más tarde durante las fiestas: tiene un horario más largo. No dice que abra más tarde por la mañana (I sobra)."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 10, "cats": ["personas", "planes"], "es": "ES-10", "pc": "no puedo ir a tu cena del sábado",
   "lab": "Contestador", "voice": "CRISTINA_LAT/RADIO",
   "text": "[apologetic] Hola, Nacho, soy Irene. Lo siento muchísimo, pero no puedo ir a tu cena del sábado: mi madre está en el hospital y me voy al pueblo. Ya está mejor, no te preocupes. Pásalo bien y nos vemos a la vuelta.",
   "why": "Irene no puede ir a la cena de Nacho. No acepta la invitación (F sobra)."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 7, "cats": ["lugares", "tiempo"], "es": "ES-10", "pc": "la cafetería del tren está cerrada · el tren para diez minutos",
   "lab": "Megafonía", "voice": "LUIS_GUILLERMO/RADIO",
   "text": "[calm] Señores viajeros, les informamos de que la cafetería del tren está cerrada por una avería. En la próxima parada, Albacete, el tren para diez minutos: pueden comprar bebidas en la estación. El tren llega a Madrid a su hora. Disculpen las molestias.",
   "why": "La cafetería del tren no funciona durante el viaje. Parar diez minutos en Albacete es lo normal: el viaje no se retrasa."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 2, "cats": ["personas", "normas"], "es": "ES-10", "pc": "la doctora quiere hablar con usted · puede pedir cita",
   "lab": "Contestador", "voice": "MAYA/RADIO",
   "text": "[professional] Buenos días, le llamamos del centro de salud de San Blas. Ya tenemos los resultados de sus análisis. Todo está bien, pero la doctora Molina quiere hablar con usted. Puede pedir cita en la web o por teléfono. Gracias.",
   "why": "La persona tiene que pedir cita con la doctora. Nadie cambia la hora de una cita: eso es el ejemplo (A)."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 9, "cats": ["lugares", "tiempo"], "es": "ES-10", "pc": "el libro que reservó ya ha llegado",
   "lab": "Contestador", "voice": "LUISA/RADIO",
   "text": "[friendly] Hola, buenas tardes. Le llamamos de la biblioteca Gloria Fuertes. El libro que reservó ya ha llegado. Puede recogerlo hasta el viernes en el mostrador de préstamo. Si no viene, se lo damos a la siguiente persona de la lista.",
   "why": "El libro que reservó ya está en la biblioteca: ya está disponible."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 6, "cats": ["tiempo", "planes"], "es": "ES-10", "pc": "empieza a las diez, media hora más tarde, por la lluvia",
   "lab": "Megafonía", "voice": "BOGA/RADIO",
   "text": "[energetic] ¡Atención! El concierto de esta noche empieza a las diez, media hora más tarde, por la lluvia. Las puertas del recinto se abren a las nueve. Les recomendamos venir en transporte público: no hay sitio para aparcar. Gracias y que disfruten del concierto.",
   "why": "El concierto empieza media hora más tarde. Llueve, pero no se suspende (B sobra)."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 4, "cats": ["personas", "planes"], "es": "ES-10", "pc": "¿necesitas algo del súper? te llevo la leche",
   "lab": "Contestador", "voice": "DAVID_CO/RADIO",
   "text": "[hurried] Mamá, soy Lucas. Ya he salido del trabajo. ¿Necesitas algo del súper? Te llevo la leche y el pan, que me lo dijiste ayer. Si quieres algo más, mándame un mensaje, que voy conduciendo y no puedo hablar.",
   "why": "Lucas le ofrece a su madre hacer la compra."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

# Voces del último modelo que han hecho (M6): no se repiten aquí
VOCES_EVITAR = ["DANI", "NIEVE", "FIONA", "LYDIA", "OSCAR", "SARA_JOVEN", "AITANA", "DANIEL_ES", "ANA_MARIA", "VOLU", "SARA_2", "AGUSTIN",
                "TATIANA", "RAFA", "JUAN_CARLOS", "SERGIO", "TAMARA", "MARINA_ES", "ZABRA", "CESAR", "DAVID_LAT", "EVA", "MARIO",
                "DIANA", "LUIS_VEGA", "TOMAS", "BOBBY", "LINA", "SANTIAGO_ES", "NINOSKA", "JUAN_CARLOS_2"]
REPARTO = """# REPARTO DE VOCES M07 (ninguna voz del M6, el último modelo que han hecho)
# SIN EFECTOS DE SONIDO: ni sintonía, ni din-don, ni pitido (el examen real tampoco los tiene).
# Cada intervención lleva al principio su etiqueta de emoción de ElevenLabs v3 ([cheerful], [sighs]...).
# T1 conversaciones (v3): 0 técnico = RAQUEL + MARTIN_3 · 1 Elena = GABRIEL_ES + ESTELA · 2 el deporte = CAROLINA + EMILIO
#   3 cena de empresa = SUSANA + VALENTINA (Colombia) · 4 el autobús = CRISTINA (hija) + JAVIER (padre)
#   5 taller de cerámica = SARA + DAVID_M1 · 6 las llaves = ERIK (Venezuela) + LUCIA
# T2 radio (perfil /RADIO): 0 «Despierta con nosotros» = DANIEL_CO (Colombia) · 1 mercado medieval = MARTIN_2 · 2 óptica = GABI (Argentina)
#   3 «Tu casa, tu dinero» = CAROLINA · 4 Ciclos Martín = ELEGUAR · 5 teatro infantil = MARTIN_1 · 6 concurso = RAQUEL
#   (22/10: HUGO, CLARA y LUCIA_AR sonaban enlatadas: descartadas de voces.txt. CAROLINA y RAQUEL también salen en la T1.)
# T3 conversación entre amigos: PAULA = MIA · RUBÉN = MILO
# T4 mensajes (/RADIO): 0 contestador peluquería = SOFIA (Colombia) · 1 megafonía súper = SANTIAGO_LAT · 2 contestador Irene = CRISTINA_LAT
#   3 megafonía tren = LUIS_GUILLERMO (México) · 4 contestador centro de salud = MAYA · 5 contestador biblioteca = LUISA
#   6 megafonía concierto = BOGA (Colombia) · 7 contestador Lucas = DAVID_CO (Colombia)"""

# ---------------- ESCRITURA ----------------
# Textos modelo: [n] = empieza la frase de la pauta n · _texto_ = conector (sale subrayado).
ESCRITA = {"t1": {"instr": "Su amiga Irene, que hace teatro, le ha escrito este correo.", "trato": "tú",
  "input": ["¡Hola! ¿Qué tal? Te escribo con una noticia: el sábado 22 estrenamos la obra de mi grupo de teatro en el centro cultural, a las ocho. ¡Estoy muy nerviosa! ¿Vienes? ¿Y tú cómo estás? ¿Qué has hecho estas semanas?", "Un beso,<br>Irene"],
  "lead": "Conteste a Irene. En el correo tiene que:",
  "pautas": ["saludar y felicitarla por el estreno;", "contarle qué ha hecho usted estas semanas y cómo está;", "decirle si va a ir al estreno y, si no puede, explicarle por qué;", "proponerle quedar otro día: el día, el lugar y la hora;", "hacerle dos preguntas sobre la obra y despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Una revista en español prepara un número especial sobre la amistad. Escriba un texto sobre un amigo o una amiga de su infancia. Hable de:",
   "pautas": ["quién es y cómo y dónde se conocieron;", "qué hacían juntos cuando eran pequeños y cómo era él o ella entonces;", "algo especial o divertido que les pasó juntos;", "cómo es su vida ahora y si todavía se ven;", "por qué cree que algunas amistades duran toda la vida."]},
  "op2": {"title": "Opción 2", "intro": "Encarna es panadera en un pueblo de Cuenca. Aquí tiene tres fotos de su vida.",
   "photos": ["1982. Encarna, una niña de unos ocho años, ayuda a su padre a sacar el pan del horno en la panadería de la familia.",
              "2003. Encarna, ya adulta, abre la puerta de la panadería por la mañana. Ahora la panadería es suya.",
              "Hoy. Encarna, con el pelo gris, enseña a hacer pan a un grupo de personas en la cocina de su casa."],
   "ficha": [], "intro2": "Escriba un texto sobre la vida de Encarna. Hable de:",
   "pautas": ["cómo era su vida de niña y qué hacía en la panadería;", "qué cambió en 2003 y cómo era entonces su trabajo;", "qué hace ahora y por qué cree usted que ya no tiene la panadería."],
   "img": "M07_escrita_encarna_panadera.jpg", "imgAlt": "Tres fotos de Encarna: de niña con su padre en la panadería, abriendo su panadería de adulta y enseñando a hacer pan en su cocina"},
  "min": 70, "max": 80},
 "modelos": {
  "t1": {"titulo": "Tarea 1 · Correo a una amiga (de tú)", "tarea": 1,
   "aprobado": {"texto": [
     "[1]¡Hola, Irene!",
     "¡Enhorabuena por el estreno! [2]Yo estas semanas he trabajado mucho y he empezado a correr en el parque. Estoy bien, pero un poco cansada. [3]El sábado no puedo ir, _porque_ es la boda de mi prima en Murcia. [4]¿Quedamos el jueves a las siete en la cafetería de la plaza? [5]¿Cuántas personas sois en el grupo? ¿De qué trata la obra?",
     "Un beso,<br>Marta"],
    "porque": "Contesta a las cinco pautas con frases sencillas: felicita a Irene, cuenta lo que ha hecho con el pretérito perfecto (he trabajado, he empezado), dice que no puede ir y por qué, propone día, lugar y hora, y hace dos preguntas sobre la obra. Todo de tú, del saludo a la despedida."},
   "excelente": {"texto": [
     "[1]¡Hola, Irene! ¡Enhorabuena por el estreno!",
     "[2]Yo estas semanas he estado muy liada: he cambiado de trabajo y, _además_, me he apuntado a clases de guitarra. [3]_Pero_ el sábado, por desgracia, no puedo ir: se casa mi prima y _por eso_ me voy el viernes. [4]¿Te va bien el jueves a las siete en la terraza de la plaza? [5]¿Quién escribió la obra? ¿Tienes un papel importante?",
     "Un beso,<br>Marta"],
    "porque": "Las mismas cinco pautas, con dos o tres mejoras del A2: conectores para unir las ideas (además, pero, por eso), palabras más precisas (liada, por desgracia), un detalle que explica el porqué (me voy el viernes) y preguntas más concretas. Sigue siendo corto y de tú.",
    "mejoras": ["un conector más (además, pero, por eso)", "una palabra más precisa (muy liada, por desgracia)", "un detalle o un porqué (me voy el viernes)", "una pregunta al lector más concreta (¿Tienes un papel importante?)"]}},
  "op1": {"titulo": "Tarea 2 · Opción 1 · Un amigo o una amiga de la infancia", "tarea": 2,
   "aprobado": {"texto": [
     "[1]Mi mejor amiga de la infancia se llama Lucía. Nos conocimos en el colegio, en Valladolid, cuando teníamos seis años. [2]Jugábamos en el parque todas las tardes. Lucía era muy alegre y un poco traviesa. [3]Un verano nos perdimos en la feria y su padre nos buscó durante una hora. [4]Ahora vive en Londres y trabaja de enfermera. Nos vemos en Navidad. [5]Creo que algunas amistades duran _porque_ tenemos muchos recuerdos juntos."],
    "porque": "Cumple las cinco pautas, una o dos frases para cada una. Usa el imperfecto para lo que hacían y cómo era Lucía (jugábamos, era), el indefinido para lo que pasó (nos conocimos, nos perdimos) y el presente para ahora. Es sencillo y aprueba."},
   "excelente": {"texto": [
     "[1]Mi amiga de la infancia es Lucía. Nos conocimos el primer día de colegio, en Valladolid: _cuando_ yo lloraba, ella me dio la mano. [2]_Después_, jugábamos juntas en el parque todas las tardes. Era alegre, valiente y un poco traviesa. [3]Una vez nos perdimos en la feria y, _al final_, nos encontró un policía. ¡Qué susto! [4]Ahora vive en Londres, _pero_ hablamos cada semana. [5]Para mí, duran las amistades con buenos recuerdos."],
    "porque": "Las mismas cinco pautas, con más variedad: un pasado bien combinado (cuando yo lloraba, ella me dio la mano), conectores para contar (después, al final, pero), adjetivos más precisos para describir a Lucía y una exclamación con emoción. Todo sigue siendo A2.",
    "mejoras": ["un pasado bien combinado (cuando yo lloraba, ella me dio la mano)", "un conector más (después, al final, pero)", "una palabra más precisa (valiente, traviesa)", "una frase con cuando"]}},
  "op2": {"titulo": "Tarea 2 · Opción 2 · La vida de Encarna", "tarea": 2,
   "aprobado": {"texto": [
     "[1]Encarna nació en un pueblo de Cuenca. De niña, ayudaba a su padre en la panadería: se levantaba muy pronto y sacaba el pan del horno con él. [2]En 2003, Encarna se quedó con la panadería. Trabajaba muchas horas, pero estaba contenta. [3]Ahora la panadería está cerrada y Encarna da clases de pan en su cocina. Creo que la cerró _porque_ estaba cansada y en el pueblo vive poca gente."],
    "porque": "Cuenta la vida de Encarna en pasado (no describe las fotos en presente): el imperfecto para cómo era su vida (ayudaba, trabajaba), el indefinido para el cambio (se quedó con la panadería) y el presente para ahora. Responde a las tres pautas, también a la suposición del final (creo que la cerró porque...)."},
   "excelente": {"texto": [
     "[1]Encarna creció en un pueblo de Cuenca. _Cuando_ era niña, ayudaba a su padre: se levantaba a las cinco y sacaba el pan del horno con él. [2]En 2003 su padre se jubiló y, _por eso_, Encarna se quedó con la panadería. Trabajaba muchísimo, _pero_ le encantaba. [3]Ahora da talleres de pan en la cocina de su casa. Supongo que cerró la tienda _porque_ en el pueblo ya casi no queda gente."],
    "porque": "Más variedad de pasados (cuando era niña, ayudaba / su padre se jubiló), conectores que explican la historia (cuando, por eso, pero, porque), palabras más precisas (creció, talleres, supongo) y una suposición con su porqué.",
    "mejoras": ["un pasado bien combinado (su padre se jubiló y, por eso, se quedó con la panadería)", "un conector más (por eso, pero)", "una palabra más precisa (creció, talleres, supongo)", "un detalle o un porqué (se levantaba a las cinco)"]}}}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: una tradición de mi familia", "pautas": ["qué tradición es, cuándo la celebran y quién participa;", "cómo la vivía usted de niño o de niña y qué recuerdo tiene de ella;", "qué ha cambiado y qué es igual que antes;", "una costumbre de su país que a la gente de fuera le parece curiosa;", "si va a continuar esa tradición en el futuro y por qué."]},
  {"title": "Opción 2: los animales y yo", "pautas": ["si tiene o ha tenido animales y cómo son o eran;", "qué animal tenía su familia cuando usted era pequeño o pequeña, o qué animal quería tener;", "una historia divertida o especial con un animal;", "qué piensa de llevar animales a los bares, a las tiendas o en el transporte público;", "si le gustaría tener un animal en el futuro y cuál."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1 · Buscar piso", "desc": "El salón de un estudio pequeño, una tarde de invierno. Dos amigas de unos veinticinco años, sentadas en el sofá, miran anuncios de pisos de alquiler en un portátil. Una, con el pelo rizado y un jersey amarillo, señala la pantalla; tiene un gato dormido en las piernas. La otra, con el pelo liso, gafas y una sudadera azul, apunta algo en una libreta. En la mesa baja hay dos tazas, un plano de la ciudad, un móvil y un bolígrafo; al lado del sofá, una caja de cartón con libros.", "img": "M07_oral_foto1_buscar_piso_alquiler.jpg"},
  {"title": "Fotografía 2 · En el huerto", "desc": "Un huerto urbano entre edificios, una mañana de verano. Un abuelo de unos setenta años, con sombrero de paja y camisa de cuadros, y su nieta de unos diez años, con gorra y botas de agua, recogen tomates. Ella sujeta una cesta llena y se ríe; él le enseña un tomate muy grande. Alrededor hay tomateras, lechugas, una regadera, una manguera, un cubo, unas tijeras de podar y una silla de plástico. Al fondo, otras personas trabajan en sus huertos.", "img": "M07_oral_foto2_huerto_abuelo_nieta.jpg"}],
  "pautas": ["¿Cómo son las personas de la foto (físico, personalidad que cree que tienen...)? ¿Qué ropa llevan?", "¿Dónde están esas personas? ¿Qué objetos hay? Describa el lugar.", "¿Qué están haciendo las personas de la foto?", "¿Qué relación cree que hay entre ellas?", "¿Qué cree que piensan o cómo se sienten estas personas? ¿Por qué?", "¿Qué cree que han hecho antes? ¿Y qué van a hacer después?"]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1 · Un piso para compartir", "intro": "Usted y un amigo o una amiga van a alquilar un piso juntos. Mañana tienen una cita en una agencia para ver uno. Antes, hablan de lo que buscan. El examinador / La examinadora es su amigo/a. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su amigo/a, tiene que hablar de:", "pautas": ["dónde vive ahora, cómo es su casa y qué no le gusta de ella;", "si ha compartido piso alguna vez: dónde, con quién y qué tal fue;", "cómo tiene que ser el piso nuevo (barrio, habitaciones, precio...) y por qué;", "cómo van a organizar el dinero y las tareas de la casa;", "qué van a preguntar en la agencia y a qué hora quedan para ir."]},
  {"title": "Si eligió la fotografía 2 · Plantas para la oficina", "intro": "En su trabajo hay una terraza que nadie usa. Usted y un compañero o una compañera quieren poner plantas. El examinador / La examinadora es su compañero/a. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su compañero/a, tiene que hablar de:", "pautas": ["si tiene plantas en casa y cómo las cuida;", "si ha cultivado algo alguna vez (en un huerto, en un balcón...): cuándo, dónde y qué tal fue;", "qué plantas quieren poner en la terraza y por qué;", "dónde las van a comprar, cuánto dinero pueden gastar y quién paga;", "quién las va a regar y cuándo van a empezar."]}]}}

# Modelos de la tarea 3 (se ven en la oral del estudiante después de la prueba y en la libreta de la profesora).
# En el diálogo, "E" = examinador y "C" = candidato. La frase del pequeño problema lleva True.
# Como en las láminas de 2022, las dos situaciones son de tú y mezclan planificar con contar cosas propias.
ORAL_MODELOS = {"t3": [
 {"titulo": "Fotografía 1 · Un piso para compartir", "trato": "tú",
  "notas": [["dónde vivo ahora", "estudio en el centro · pequeño, sin ascensor · ruido por la noche · ¿y tú?"],
            ["¿he compartido piso?", "Salamanca, de estudiante, 2 años, 3 chicas · divertido · problemas con la limpieza"],
            ["cómo es el piso", "2 habitaciones grandes · cerca del metro (trabajo lejos) · máx. 900 €/mes · ¿qué te parece?"],
            ["dinero y tareas", "la mitad cada uno (también luz y agua) · tareas por semanas: cocina / baño"],
            ["agencia y hora", "preguntar: animales, gastos, cuándo entrar · cita a las 10 · quedamos 9:30 en la puerta"]],
  "segunda": "Si no aceptan animales: preguntarlo en la agencia y, si dicen que no, buscar otro piso (otra agencia, otro barrio).",
  "problema": "El examinador tiene una gata y en el anuncio pone que no aceptan animales.",
  "dialogo": [
   ["E", "¡Hola! ¿Qué tal? Oye, mañana vamos a la agencia, ¿no? Antes de ir, ¿hablamos un poco del piso?"],
   ["C", "¡Hola! Sí, claro. Mira, yo ahora vivo en un estudio en el centro. Es bonito, pero muy pequeño y no tiene ascensor. Además, por la noche hay mucho ruido. ¿Y tú, dónde vives?"],
   ["E", "Yo todavía vivo con mis padres. ¿Tú has compartido piso alguna vez?"],
   ["C", "Sí, cuando estudiaba en Salamanca viví dos años con tres chicas. Fue muy divertido, aunque a veces había problemas con la limpieza. ¿Tú nunca?"],
   ["E", "No, nunca. ¿Y cómo tiene que ser el piso para ti?"],
   ["C", "Para mí, con dos habitaciones grandes y cerca del metro, porque trabajo lejos. Y no más de novecientos euros al mes. ¿Qué te parece?"],
   ["E", "Me parece bien. ¿Y cómo nos organizamos con el dinero y las tareas?"],
   ["C", "Pagamos la mitad cada uno, también la luz y el agua. Y las tareas, por semanas: una semana tú limpias la cocina y yo el baño, y la siguiente, al revés. ¿Vale?"],
   ["E", "Vale. Oye, una cosa: he visto el anuncio otra vez y pone que no aceptan animales. Y yo tengo a Misi, mi gata...", True],
   ["C", "¡Vaya! Pues mañana lo preguntamos en la agencia, y también si los gastos están incluidos. Si no quieren gatos, buscamos otro piso. ¿Llamamos hoy a otra agencia, por si acaso?"],
   ["E", "Buena idea. ¿Y a qué hora quedamos mañana?"],
   ["C", "La cita es a las diez. ¿Quedamos a las nueve y media en la puerta de la agencia? ¡Hasta mañana!"]]},
 {"titulo": "Fotografía 2 · Plantas para la oficina", "trato": "tú",
  "notas": [["mis plantas", "limonero, cactus, flores en el balcón · riego 2 veces por semana · ¿y tú?"],
            ["¿he cultivado algo?", "de niña: huerto con mi abuelo (tomates, lechugas) · año pasado: fresas en el balcón, los pájaros"],
            ["qué plantas", "poca agua (romero, lavanda) · mucho sol · flores para alegrar · ¿qué te parece?"],
            ["comprar y pagar", "vivero de la carretera · unos 100 € · la empresa o entre todos"],
            ["regar y empezar", "turnos por meses · riego automático · viernes al vivero · lunes plantar"]],
  "segunda": "Si no puede regar en agosto: regar yo en agosto y él en septiembre, o poner un riego automático.",
  "problema": "El examinador se va de vacaciones todo agosto y no puede regar.",
  "dialogo": [
   ["E", "¡Hola! Oye, ¿has visto la terraza del tercero? Nadie la usa. ¿Ponemos unas plantas?"],
   ["C", "¡Hola! ¡Qué buena idea! Yo en casa tengo muchas plantas: un limonero, cactus y unas flores en el balcón. Las riego dos veces por semana. ¿Tú tienes plantas?"],
   ["E", "Solo una, y está medio muerta... ¿Tú has cultivado algo alguna vez?"],
   ["C", "Sí, de pequeña tenía un huerto con mi abuelo en el pueblo. Plantábamos tomates y lechugas, ¡me encantaba! Y el año pasado planté fresas en el balcón, pero los pájaros se comieron todas."],
   ["E", "¡Qué pena! ¿Y qué plantas ponemos en la terraza?"],
   ["C", "Plantas que necesitan poca agua, como el romero o la lavanda, porque en la terraza hace mucho sol. Y unas macetas con flores, para alegrar un poco. ¿Qué te parece?"],
   ["E", "Muy bien. ¿Y dónde las compramos?"],
   ["C", "En el vivero de la carretera, que es barato. ¿Gastamos unos cien euros? Podemos pedir el dinero a la empresa o pagar entre todos los compañeros."],
   ["E", "Vale. Pero hay un problema: yo me voy de vacaciones todo agosto y no puedo regarlas.", True],
   ["C", "No pasa nada. En agosto riego yo, y en septiembre me voy yo y riegas tú. También podemos poner un riego automático. ¿Te parece bien?"],
   ["E", "Perfecto. ¿Y cuándo empezamos?"],
   ["C", "¿Te va bien el viernes después del trabajo? Vamos juntos al vivero y el lunes lo plantamos todo. ¡Hasta el viernes!"]]}]}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (una tradición): ¿Qué comida preparan ese día? · ¿Qué hacía usted ese día cuando era pequeño/a?
    Opción 2 (los animales): ¿Cómo se llamaba su primer animal? · ¿Hay muchos perros en su ciudad?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (buscar piso): ¿Qué tipo de piso cree que buscan? · ¿De quién cree que es el gato?
    Foto 2 (en el huerto): ¿Qué van a hacer con los tomates? · ¿Quién cree que cuida el huerto?
  Tarea 3 — su papel: amigo/a o compañero/a de trabajo del candidato, SIEMPRE DE TÚ (como en las láminas de 2022).
  Vaya pauta por pauta, elija las preguntas según lo que diga el candidato, improvise con sus datos y provoque UN
  pequeño problema. Esquema para la interacción:
    Foto 1 (amigo/a · un piso para compartir)
      Saludar ............. ¡Hola! Mañana vamos a la agencia, ¿no? ¿Hablamos antes del piso?
      Dónde vive .......... ¿Dónde vives ahora? ¿Cómo es tu casa? ¿Qué no te gusta de ella?
      Compartir piso ...... ¿Has compartido piso alguna vez? ¿Dónde? ¿Con quién? ¿Qué tal fue?
      El piso nuevo ....... ¿Cómo tiene que ser el piso? ¿En qué barrio? ¿Cuánto podemos pagar?
      Dinero y tareas ..... ¿Cómo pagamos? ¿Y la limpieza, la compra...? ¿Quién hace qué?
      PEQUEÑO PROBLEMA .... «He visto el anuncio otra vez y pone que no aceptan animales. Y yo tengo una gata...».
                            Espere a que proponga algo (preguntarlo en la agencia, buscar otro piso).
      Agencia y adiós ..... ¿Qué preguntamos en la agencia? ¿A qué hora quedamos? · Vale, ¡hasta mañana!
    Foto 2 (compañero/a de trabajo · plantas para la terraza de la oficina)
      Saludar ............. ¡Hola! ¿Has visto la terraza del tercero? ¿Ponemos unas plantas?
      Sus plantas ......... ¿Tienes plantas en casa? ¿Cuáles? ¿Cómo las cuidas?
      Experiencia ......... ¿Has cultivado algo alguna vez? ¿Cuándo? ¿Dónde? ¿Qué tal fue?
      Qué plantas ......... ¿Qué plantas ponemos? ¿Por qué esas?
      Comprar y pagar ..... ¿Dónde las compramos? ¿Cuánto gastamos? ¿Quién paga?
      PEQUEÑO PROBLEMA .... «Yo me voy de vacaciones todo agosto y no puedo regarlas». Espere a que proponga algo
                            (turnos, riego automático).
      Organizar y adiós ... ¿Cuándo empezamos? ¿Quién riega? · Vale, ¡hasta el viernes!
    El diálogo modelo de las dos situaciones está en la pestaña Oral del estudiante (se ve al abrir la prueba).
  Qué mirar en este modelo: tú coherente en toda la tarea 3; que no conteste solo sí o no (responde + detalle o
  porqué + pregunta); proponer y aceptar o rechazar con otra propuesta (¿y si...?, ¿te va bien...?); en la tarea 3,
  la pauta de experiencia en pasado (viví, fue, plantábamos, se comieron); en el monólogo, presente + pasado
  (cuando era pequeño/a + imperfecto, una historia en indefinido) + futuro, y la pauta que se sale de la historia
  personal (una costumbre de su país / los animales en los bares y el transporte); en la foto, las seis preguntas
  en orden, hay / está, estar + gerundio y «seguramente han...» / «van a...»."""
ERRORES = """  *Tú puede / *¿Usted tienes...? (mezcla tú / usted); *Cuando era niño, fui cada verano al pueblo (iba: costumbre);
  *Ayer he visto el anuncio (vi; con «hoy» o «otra vez», he visto); *Busco un piso que tiene... (en A2, mejor:
  «quiero un piso con dos habitaciones»); *Pagamos la mitad cada uno de la luz (pagamos la mitad de la luz);
  *Hay la gata en el sofá (la gata está en el sofá / hay una gata); *Los tomates están muy grandes (son);
  *Están cansado (cansadas); *Me gusta mucho las plantas (me gustan); *Riego las plantas dos veces a la semana
  (bien) / *dos veces por la semana (por semana); frases sueltas sin conectores en el monólogo («y... y... y...»)."""

# ---------------- IMÁGENES: FOTOS ----------------
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "salón de un estudio: dos amigas buscan piso de alquiler en un portátil",
  "personas": "dos amigas", "edades": "las dos de unos 25 años",
  "aspecto": "una con el pelo rizado y castaño, un jersey amarillo y vaqueros; la otra con el pelo liso y oscuro, gafas, una sudadera azul y pantalón de chándal",
  "espacio": "interior", "lugar": "salón pequeño de un estudio, con un sofá, una mesa baja, una estantería y una ventana", "momento": "tarde",
  "estacion": "invierno", "tiempo": "nublado; ya casi es de noche y la lámpara está encendida", "gente": "solo ellas dos (y un gato)",
  "accion": "miran anuncios de pisos de alquiler en un portátil: una señala la pantalla y la otra apunta algo en una libreta",
  "fondo": "estantería con libros y plantas, una ventana con la calle, una lámpara de pie encendida",
  "objetos": "portátil, libreta, bolígrafo, dos tazas, un plano de la ciudad, un móvil, una caja de cartón con libros, cojines, una manta",
  "detalle": "un gato duerme en las piernas de la chica del jersey amarillo (en la tarea 3, el piso no acepta animales)"},
 "oral_foto2": {"situacion": "huerto urbano entre edificios: un abuelo y su nieta recogen tomates",
  "personas": "un abuelo y su nieta", "edades": "él de unos 70 años, ella de unos 10",
  "aspecto": "él con sombrero de paja, bigote blanco, camisa de cuadros remangada y pantalón de trabajo; ella con una gorra, camiseta verde, pantalón corto y botas de agua amarillas",
  "espacio": "exterior", "lugar": "huerto urbano de un barrio, con parcelas pequeñas entre bloques de pisos", "momento": "mañana",
  "estacion": "verano", "tiempo": "sol", "gente": "otras personas trabajan al fondo en sus parcelas",
  "accion": "recogen tomates: ella sujeta una cesta llena y se ríe; él le enseña un tomate muy grande",
  "fondo": "otras parcelas con cañas y plantas, una caseta de herramientas y los bloques de pisos del barrio",
  "objetos": "cesta, tomateras con cañas, lechugas, regadera, manguera, cubo, tijeras de podar, silla de plástico, guantes",
  "detalle": "el abuelo le enseña a la niña un tomate enorme, como si fuera un premio"},
 "escrita": {"situacion": "la vida de Encarna, panadera de un pueblo, en tres momentos",
  "personas": "Encarna (de niña, de adulta y de mayor), su padre y un grupo de alumnos", "edades": "Encarna con unos 8 años, unos 30 y unos 50; su padre de unos 40",
  "aspecto": "Encarna con el pelo castaño recogido y la cara redonda, con un delantal blanco; de mayor, con el pelo gris corto y gafas; el padre con bigote y gorro de panadero",
  "espacio": "interior y exterior", "lugar": "panadería antigua de un pueblo con horno de leña, la puerta de la tienda en la calle y la cocina de una casa", "momento": "madrugada, mañana y tarde",
  "estacion": "invierno, primavera y otoño", "tiempo": "luz de horno, sol de la mañana y luz de interior", "gente": "solo la familia en las dos primeras; un grupo de cuatro adultos en la tercera",
  "accion": "la niña ayuda a su padre a sacar el pan del horno; Encarna adulta abre la puerta de la panadería; Encarna mayor enseña a amasar pan",
  "fondo": "el horno de leña y las estanterías con pan; la calle de un pueblo con casas blancas; la cocina con harina en la mesa",
  "objetos": "pala de horno, barras de pan, sacos de harina, cestas, llave de la puerta, toldo, delantales, masa, boles",
  "detalle": "en la tercera foto la panadería ya no está: Encarna enseña en su casa"},
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
}

IMG_PROMPTS = {
 "escrita": "The life of Encarna, a baker in a small village in inland Spain, in three moments. She has a round face and brown hair; her look changes only with age. Panel 1 (left): early morning in 1982, inside an old village bakery with a wood-fired oven, a girl of about 8 with her brown hair tied back and a small white apron helps her father, a man of about 40 with a moustache and a baker's cap, take loaves out of the oven with a long wooden peel; she holds a basket and watches the bread carefully; sacks of flour and shelves of bread behind them; warm light from the oven. Panel 2 (middle): a spring morning in 2003, the same woman, now about 30, with her hair tied back and a white apron, unlocks and opens the old wooden door of the bakery on a narrow village street with white houses; a canvas awning above the door, baskets of bread in the window, nobody else around. Panel 3 (right): today, an autumn afternoon in the kitchen of her house, the same woman, now about 50, with short grey hair and glasses, shows four adults of different ages how to knead bread dough on a wooden table covered in flour; bowls, a bag of flour and some round loaves on the table; she is explaining with her hands in the dough and the students copy her.",
 "oral_foto1": "Two female friends of about 25 sitting together on a sofa in the small living room of a studio flat on a grey winter afternoon, looking for a flat to rent on a laptop. One has curly brown hair, a yellow jumper and jeans; she points at the laptop screen and has a sleeping grey cat on her lap. The other has straight dark hair, glasses, a blue sweatshirt and tracksuit bottoms; she writes something in a small notebook. On the low coffee table in front of them: two mugs, a folded paper city map, a mobile phone and a pen. Next to the sofa, a cardboard box full of books. A blanket and cushions on the sofa, a bookshelf with books and plants, a floor lamp switched on, a window with a grey street outside. The laptop screen shows a property website with small photos of rooms (no readable text).",
 "oral_foto2": "A grandfather of about 70 and his granddaughter of about 10 picking tomatoes together in a small community vegetable garden between blocks of flats on a sunny summer morning. He wears a straw hat, a short-sleeved checked shirt and work trousers, has a white moustache, and proudly shows her a very big red tomato in his hand. She wears a cap, a green T-shirt, shorts and yellow rubber boots, holds a basket full of tomatoes and laughs. Around them: tomato plants tied to canes, rows of lettuces, a green watering can, a garden hose, a bucket, pruning shears and a plastic chair. In the background, two other people working in their own small plots, a small tool shed and the blocks of flats of the neighbourhood.",
}
IMG_NAMES = {"escrita": "M07_escrita_encarna_panadera", "oral_foto1": "M07_oral_foto1_buscar_piso_alquiler", "oral_foto2": "M07_oral_foto2_huerto_abuelo_nieta"}
IMG_DESC = {"escrita": "Escritura opcion 2 triptico Encarna panadera: 1 de nina saca el pan con su padre, 2 abre su panaderia de adulta, 3 de mayor ensena a hacer pan en su cocina",
            "oral_foto1": "Oral foto 1 buscar piso: dos amigas miran pisos de alquiler en un portatil en el sofa, con un gato",
            "oral_foto2": "Oral foto 2 en el huerto: un abuelo y su nieta recogen tomates en un huerto urbano"}
CA1_DESC = {0: "Auditiva T1 ejemplo: lavadora / horno / lavavajillas", 1: "Auditiva T1 conv 1: residencia de mayores / farmacia / hospital",
            2: "Auditiva T1 conv 2: correr / nadar / montar en bici", 3: "Auditiva T1 conv 3: restaurante / autobus / grupo de musica",
            4: "Auditiva T1 conv 4: relojes 8:10 / 8:40 / 9:00", 5: "Auditiva T1 conv 5: delantal / toalla / barro",
            6: "Auditiva T1 conv 6: buzon / felpudo / panaderia"}

LECTURA = [CL1, CL2, CL3, CL4]
AUDITIVA = [CA1, CA2, CA3, CA4]
