# -*- coding: utf-8 -*-
# FUENTE DEL MODELO 3 · Curso de preparación DELE A2 (Módulo 2, modelos completos)
# Perfil = + = =: lectura como el examen; auditiva en la parte alta del examen, sin salir del A2 (como la del M7);
# escritura y oral como el examen. "+" = parte alta del examen real, nunca gramática de B1.
# Temas MEZCLADOS como en el examen real: cada tarea de un área distinta.
# Se construye con:  python3 build_modelo.py fuente_M03
# Todo el contenido es original. Español de España.
M = "03"
NOMBRE = "Modelo 3"
NIVEL = "auditiva exigente"
TITLE = "Examen completo"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress (si se suben en noviembre: "2026/11")
TIEMPOS = {"lectura": 60, "auditiva": 40}
REC_LABEL = "Qué vas a encontrar en este modelo"
RECORDATORIO = [
 "Un examen completo con el formato y los tiempos del DELE A2: lectura (60 minutos), auditiva (40 minutos), escritura (45 minutos) y, en clase con tu profesora, la oral.",
 "Como en el examen, cada tarea habla de un tema distinto: una librería nueva, anuncios del barrio, tres tiendas con historia, unas bañistas de invierno, recados y cambios de última hora, la radio, los vecinos, mensajes del contestador, una cena de antiguos compañeros, el primer trabajo, un pianista, el deporte y la tele.",
 "La lectura, la escritura y la oral son como en el examen. La auditiva es más exigente: audios más largos, más datos, opciones que se descartan al final y respuestas dichas con otras palabras.",
 "Al terminar, en Resultados ves tu nota de cada grupo (lectura + escritura; auditiva + oral), si estás listo para presentarte, qué fichas repasar, tu control de progreso y cómo leer la nota de este modelo.",
]
TIPS_INICIO = [
 "<b>Reparte el tiempo de la lectura:</b> unos 12 minutos para la tarea 1, 15 para la 2, 15 para la 3 y 18 para la 4. Lee primero las preguntas y busca solo lo que te piden. Los errores no restan.",
 "<b>En la auditiva de este modelo, espera hasta el final:</b> muchas veces alguien dice una cosa, la cambia y, al final, decide otra («al principio la pusieron..., pero ya no está allí»). La respuesta buena es la última.",
 "<b>Auditiva, tareas 2 y 4:</b> la opción buena casi nunca repite las palabras del audio: «se paga aparte» = «no está incluido»; «la escuela infantil» = «un niño». Las opciones falsas sí usan palabras que se oyen, pero con otro dato.",
 "<b>Al terminar cada prueba, apunta cuánto has tardado en cada tarea y qué te ha costado:</b> lo vas a necesitar en el control de progreso de Resultados.",
]

# Perfil del modelo frente al examen real (+ más difícil, = como el examen, - más fácil).
# Se enseña al final de Resultados, solo después de entregar (motor_modelo_extra.py, xPerfil).
PERFIL = {"pruebas": {"lectura": "=", "auditiva": "+", "escrita": "=", "oral": "="},
 "cuando": "Es el tercer modelo del curso: está pensado para hacerlo después de los dos modelos de entrada, cuando ya conoces el examen y quieres entrenar la auditiva.",
 "nota": "Lo que lo hacía distinto: la auditiva estaba en la parte alta del examen (audios largos con muchos datos, opciones que se mencionan y se descartan al final, respuestas dichas con otras palabras y, en la tarea 3, frases que hablan de otra persona o de algo que solo se quiere hacer); la lectura, la escritura y la oral eran como en el examen. La gramática era la del A2, como en el examen."}
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
  "repaso": "El indefinido cuenta lo que pasó y terminó (se jubiló hace cuatro años, cerraron tres meses, la movieron la semana pasada); el imperfecto describe cómo era o qué hacía antes (vendía más periódicos, el niño lloraba toda la noche); el perfecto habla de lo que has hecho hasta ahora (he abierto una librería, nunca se ha bañado). En las preguntas, fíjate en las palabras de tiempo: antes, ahora, ya, todavía, al principio.",
  "reto": "Escribe tres frases sobre tu barrio: cómo era antes (imperfecto), algo que pasó un día (indefinido) y algo que ha cambiado este año (perfecto).",
  "fichas": F("R01")},
 "planes": {"name": "Planes, propuestas y cambios de plan (pensaba..., al final..., ya no...)",
  "repaso": "En el examen, la persona dice primero lo que pensaba hacer y después lo que hace de verdad: «al principio quería un local en el centro, pero al final...», «pensaba escribirles una nota, pero...». En la auditiva de este modelo el cambio llega muy tarde: «ah, espere, que ya no está allí». La respuesta buena es siempre la última decisión. Y cuidado: querer hacer algo no es hacerlo.",
  "reto": "Escribe un mensaje a un amigo con un plan que cambia dos veces: «Primero pensaba..., después... y al final...».",
  "fichas": F("R01", "M4-3", "R13", "R08", "R14b")},
 "normas": {"name": "Normas y condiciones en anuncios y avisos (hay que, solo, excepto, no es necesario)",
  "repaso": "En los anuncios, las palabras pequeñas lo cambian todo: hay que (obligación), no es necesario (no es obligatorio), solo, excepto, mínimo, gratis, aparte, no está incluido. Lee la pregunta y busca solo esa condición: muchas veces la respuesta buena la dice con otras palabras (mientras esperas = se puede esperar; se paga aparte = no está incluido).",
  "reto": "Escribe un anuncio para alquilar una plaza de garaje con tres condiciones: algo que no está incluido, algo que hay que hacer y un horario.",
  "fichas": F("M0", "R14b")},
 "tiempo": {"name": "Horas, fechas, horarios y duración (a las, de... a, todos los días, desde hace, durante)",
  "repaso": "A las + hora; de... a... / desde... hasta... para horarios; por la mañana / tarde / noche; los sábados = todos los sábados; hace + tiempo para el pasado; desde hace + tiempo para algo que sigue hoy; cada diez minutos. En los horarios, fíjate en las excepciones (los domingos, solo por la mañana) y en los cambios (en vez de a las cinco, a las doce).",
  "reto": "Escribe cinco frases sobre tu semana con: a las..., de... a..., los sábados, desde hace..., cada...",
  "fichas": F("R06", "R14b")},
 "lugares": {"name": "Lugares y localización (hay, está, en, al lado de, enfrente de, encima de)",
  "repaso": "Hay presenta algo nuevo (hay un patio con dos mesas); está sitúa algo que ya conocemos (la parada está enfrente del mercado). Ir a + lugar, estar en + lugar, salir de + lugar. Cuidado: en la auditiva el lugar cambia muchas veces antes del final (delante del banco, al lado de la iglesia... y por fin enfrente del mercado).",
  "reto": "Describe en cuatro frases dónde están las cosas importantes de tu casa: hay..., está..., encima de..., al lado de...",
  "fichas": F("R02", "R06", "R14a")},
 "cantidad": {"name": "Precios, descuentos y cantidades (gratis, la mitad, aparte, muy, mucho)",
  "repaso": "Gratis / gratuito / sin coste = no cuesta dinero; la mitad; un veinte por ciento de descuento; se paga aparte = no está incluido; más de / menos de. Muy va con adjetivos (muy caro); mucho, con nombres y verbos (mucha gente, vende mucho). En los anuncios, mira a quién se aplica el precio especial y a qué cosa: los colchones no son lo mismo que las almohadas.",
  "reto": "Escribe un anuncio de una tienda con tres ofertas: algo gratis, algo a mitad de precio y algo que se paga aparte.",
  "fichas": F("R05", "R14a")},
 "personas": {"name": "Quién hace qué: personas, relaciones y trato (su nieta, su marido, la hermana de...)",
  "repaso": "Muchas opciones falsas cuentan lo que hace otra persona: el marido, la nieta, la hermana, el hijo, la vecina. Fíjate en los posesivos (su hermana, sus vecinos) y en quién es el sujeto de cada verbo. En la auditiva tarea 3, si lo hace una tercera persona, la respuesta es «ninguno de los dos».",
  "reto": "Escribe dos frases sobre lo que haces tú y dos sobre lo que hace una persona de tu familia, con posesivos (mi, su, nuestro).",
  "fichas": F("R04", "R07", "R10", "R14a")},
 "opinion": {"name": "Gustos, opiniones y sentimientos (me encanta, me daba vergüenza, prefiere)",
  "repaso": "Me gusta / me encanta / no me gusta nada + nombre o infinitivo; me da vergüenza; prefiero; estar + contento, cansado; para mí, creo que. La opinión puede cambiar con el tiempo (antes no le gustaban los niños; ahora cuida al bebé): escucha y lee hasta el final.",
  "reto": "Escribe tres frases sobre algo que antes no te gustaba y ahora sí: «Antes..., pero ahora...».",
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

# ---------------- LECTURA ("=": como el examen) ----------------
CL1 = {"n": 1, "type": "mail",
 "instr": "Usted va a leer el correo electrónico que Teresa ha escrito a su amiga Olga. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Teresa habla de varias personas (su marido, su hijo, una antigua compañera) y de una idea que cambió: para cada pregunta, busca quién hace cada cosa y qué pasó al final.",
 "head": ["De: Teresa", "Para: Olga", "Asunto: ¡Una gran noticia!"],
 "body": [
  "Querida Olga:",
  "¿Cómo estás? ¿Y tus niñas? Perdona por no escribirte antes, pero estos meses han sido una locura. Te cuento la gran noticia: ¡he dejado el banco! Después de veinte años en la oficina, en enero decidí cambiar de vida y he abierto una pequeña librería con cafetería en mi barrio, en Ruzafa. Se llama La Hoja Verde.",
  "Al principio quería un local en el centro, cerca de la catedral, pero los alquileres eran carísimos. Al final encontré uno en mi calle, en una antigua tienda de lámparas, a dos minutos de casa. Es pequeño, pero tiene un patio con dos mesas y un limonero. Mi marido, Ernesto, pintó las paredes y montó las estanterías, pero no trabaja conmigo: sigue en el hospital, con sus turnos de siempre.",
  "Abro de martes a domingo, de diez a ocho. Los lunes descanso o voy a buscar libros a ferias y a casas de gente que los vende. Los sábados me ayuda mi hijo Marcos, que tiene diecinueve años: él prepara los cafés y yo atiendo a los clientes. Vendo sobre todo libros de segunda mano y libros para niños, y los jueves por la tarde hay un cuentacuentos.",
  "Y ahora, la invitación: el 12 de marzo presentamos en la librería la primera novela de Inés Bravo. ¿Te acuerdas de ella? Era nuestra compañera en el instituto. Empezamos a las siete y después hay una pequeña cena en el patio. ¿Puedes venir? Puedes dormir en casa, en la habitación de Marcos, que ese fin de semana se va a la playa con sus amigos.",
  "Escríbeme pronto.",
  "Un abrazo muy fuerte,<br>Teresa"],
 "items": [
  {"n": 1, "q": "Teresa escribe a Olga para...", "o": ["contarle un cambio en su vida e invitarla.", "pedirle consejo para buscar un local.", "felicitarla por su primera novela."], "ok": 0,
   "cats": ["planes", "personas"], "es": "ES-02", "pc": "te cuento la gran noticia · y ahora, la invitación",
   "why": "Teresa le cuenta que ha dejado el banco y ha abierto una librería, y la invita a una presentación. El local ya lo ha encontrado, y la novela es de Inés, no de Olga."},
  {"n": 2, "q": "La librería de Teresa está...", "o": ["en el centro de la ciudad.", "muy cerca de su casa.", "dentro de una tienda de lámparas."], "ok": 1,
   "cats": ["lugares", "planes"], "es": "ES-05", "pc": "al principio quería un local en el centro · al final... a dos minutos de casa",
   "why": "Está en su calle, a dos minutos de casa. El centro era su primera idea, y la tienda de lámparas es lo que había antes en el local: ya no existe."},
  {"n": 3, "q": "Ernesto, el marido de Teresa,...", "o": ["trabaja ahora en la librería.", "ha dejado su trabajo en el hospital.", "ayudó a preparar el local."], "ok": 2,
   "cats": ["personas", "pasados"], "es": "ES-08", "pc": "pintó las paredes y montó las estanterías, pero no trabaja conmigo",
   "why": "Ernesto pintó las paredes y montó las estanterías: ayudó a preparar el local. No trabaja en la librería y sigue en el hospital."},
  {"n": 4, "q": "En La Hoja Verde...", "o": ["solo se venden libros nuevos.", "hay una actividad para niños cada semana.", "se puede comprar todos los días."], "ok": 1,
   "cats": ["tiempo", "normas"], "es": "ES-03", "pc": "los jueves por la tarde hay un cuentacuentos = una actividad cada semana",
   "why": "Los jueves por la tarde hay un cuentacuentos: una actividad para niños cada semana. Vende sobre todo libros de segunda mano, y los lunes cierra."},
  {"n": 5, "q": "El día de la presentación, Olga...", "o": ["puede quedarse a dormir en casa de Teresa.", "va a conocer a una compañera nueva.", "va a ir a la playa con Marcos."], "ok": 0,
   "cats": ["planes", "personas"], "es": "ES-05", "pc": "puedes dormir en casa · era nuestra compañera en el instituto",
   "why": "Teresa le dice que puede dormir en su casa, en la habitación de Marcos. A Inés ya la conoce del instituto, y el que va a la playa es Marcos, con sus amigos."},
 ]}

CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 15 minutos: menos de dos minutos por anuncio. Lee la pregunta primero y busca solo ese dato. Cuidado con las condiciones (solo, excepto, no es necesario) y con las palabras que están en el anuncio pero con otro dato.",
 "example": {"title": "PUNTO LIMPIO MÓVIL · AYUNTAMIENTO",
   "body": "El camión del punto limpio móvil pasa por tu barrio el primer martes de cada mes, de 9:00 a 14:00, en la plaza del mercado. Puedes traer pilas, bombillas, aceite de cocina usado, ropa vieja y pequeños aparatos eléctricos. No recogemos muebles ni electrodomésticos grandes: para eso, llama al ayuntamiento y vamos a tu casa sin coste. El servicio es gratuito.",
   "q": "En el punto limpio móvil...", "o": ["se pueden dejar las pilas viejas.", "recogen sofás y frigoríficos.", "hay que pagar un poco."], "ok": 0,
   "why": "La opción correcta es la A porque en el camión se pueden dejar pilas."},
 "items": [
  {"n": 6, "title": "INSTITUTO MIGUEL HERNÁNDEZ · BANCO DE LIBROS",
   "body": "¿Tus hijos ya no usan los libros de texto del curso pasado? Tráelos a la biblioteca del instituto del 1 al 15 de julio, de 9:00 a 13:00. Los libros tienen que estar en buen estado: sin páginas rotas y sin escribir con bolígrafo. En septiembre, las familias que han traído libros se llevan los del curso siguiente gratis. Las demás familias pagan 10 € por cada lote.",
   "q": "En el banco de libros...", "o": ["todas las familias reciben libros gratis.", "no aceptan libros escritos con bolígrafo.", "los libros se dejan en septiembre."], "ok": 1,
   "cats": ["normas", "cantidad"], "es": "ES-03", "pc": "sin escribir con bolígrafo · las demás familias pagan",
   "why": "Los libros tienen que estar sin escribir con bolígrafo. Solo son gratis para las familias que han traído libros, y se dejan en julio: en septiembre se recogen."},
  {"n": 7, "title": "TRASTEROS EL ALMACÉN",
   "body": "Alquilamos trasteros de 3, 6 y 10 metros en la calle Mayor, 40. Puedes entrar todos los días, de 7:00 a 23:00, con tu tarjeta. El primer mes cuesta la mitad. El contrato mínimo es de tres meses. No se puede guardar comida ni productos peligrosos. Hay cámaras y una persona en recepción por las mañanas. ¿No tienes coche? Te dejamos una furgoneta gratis el día de la mudanza.",
   "q": "En estos trasteros...", "o": ["el primer mes es más barato.", "se puede entrar a cualquier hora.", "se puede alquilar uno solo un mes."], "ok": 0,
   "cats": ["cantidad", "tiempo"], "es": "ES-03", "pc": "el primer mes cuesta la mitad = más barato · de 7:00 a 23:00 · mínimo tres meses",
   "why": "El primer mes cuesta la mitad. Por la noche no se puede entrar (de siete a once), y el contrato es de tres meses como mínimo."},
  {"n": 8, "title": "BIBLIOTECA MUNICIPAL · AJEDREZ PARA MAYORES",
   "body": "Los lunes y los miércoles, de 17:00 a 18:30, en la sala de estudio de la primera planta. Para mayores de 65 años, también para los que no saben jugar: los voluntarios del club de ajedrez enseñan desde el principio. Es gratis, pero hay pocas plazas: hay que apuntarse en el mostrador con el carné de la biblioteca. Los tableros los pone la biblioteca. En junio hay un torneo con los niños del taller infantil.",
   "q": "Para ir a las clases de ajedrez...", "o": ["es necesario saber jugar.", "hay que llevar un tablero.", "hay que tener el carné de la biblioteca."], "ok": 2,
   "cats": ["normas", "personas"], "es": "ES-04", "pc": "hay que apuntarse en el mostrador con el carné · también para los que no saben jugar",
   "why": "Para apuntarse hay que enseñar el carné de la biblioteca. No hace falta saber jugar, y los tableros los pone la biblioteca."},
  {"n": 9, "title": "FERRETERÍA HERMANOS RUIZ · COPIA DE LLAVES",
   "body": "Copias de llaves normales en cinco minutos, mientras esperas: 3 € cada una. Las llaves de seguridad tardan dos días y hay que traer la tarjeta del propietario. No hacemos copias de llaves de coche ni de mandos de garaje. También vendemos cerraduras y buzones, y los instalamos en tu casa. Abrimos de lunes a sábado, de 9:00 a 14:00 y de 17:00 a 20:30.",
   "q": "En esta ferretería...", "o": ["las llaves de seguridad están listas en el momento.", "hacen copias de las llaves del coche.", "se pueden esperar las llaves normales en la tienda."], "ok": 2,
   "cats": ["tiempo", "normas"], "es": "ES-03", "pc": "en cinco minutos, mientras esperas = se pueden esperar en la tienda",
   "why": "Las llaves normales se hacen en cinco minutos, mientras esperas. Las de seguridad tardan dos días, y no copian llaves de coche."},
  {"n": 10, "title": "OFICINA DE TURISMO · HORARIO DE INVIERNO",
   "body": "Del 1 de noviembre al 31 de marzo abrimos de lunes a sábado, de 10:00 a 14:00 y de 16:00 a 18:00; los domingos, solo por la mañana. Las visitas guiadas gratuitas al casco antiguo salen de la puerta de la oficina a las 11:00, los sábados y los domingos. Tenemos mapas y folletos en seis idiomas. Prestamos sillas de ruedas sin coste: solo hay que dejar el DNI.",
   "q": "En invierno, en la oficina de turismo...", "o": ["hay visitas guiadas todos los días.", "el domingo por la tarde está cerrada.", "se paga por las visitas guiadas."], "ok": 1,
   "cats": ["tiempo", "cantidad"], "es": "ES-06", "pc": "los domingos, solo por la mañana = cerrada el domingo por la tarde",
   "why": "Los domingos solo abre por la mañana: por la tarde está cerrada. Las visitas son solo el fin de semana, y son gratuitas."},
  {"n": 11, "title": "FESTIVAL DE CORTOMETRAJES DE LA VILLA",
   "body": "Del 10 al 14 de abril, todas las sesiones son en el teatro Principal, a las 20:00. Entradas: 4 € por sesión o 15 € el abono para las cinco noches. Los menores de 14 años y los mayores de 65 pagan la mitad. Las entradas se compran en la taquilla del teatro desde una hora antes: no hay venta por internet. El último día, el público vota su corto favorito.",
   "q": "En el festival de cortos...", "o": ["las entradas se pueden comprar en la web.", "los niños pagan menos.", "hay sesiones de tarde y de noche."], "ok": 1,
   "cats": ["cantidad", "personas"], "es": "ES-03", "pc": "los menores de 14 años pagan la mitad = los niños pagan menos",
   "why": "Los menores de catorce años pagan la mitad. No hay venta por internet, y todas las sesiones son a las ocho."},
  {"n": 12, "title": "FORO DEL BARRIO · COMPARTIR COCHE",
   "body": "Hola, soy Álvaro. Trabajo en el polígono industrial de Las Torres y voy en coche todos los días, de lunes a viernes. Salgo a las 7:15 de la plaza de la Constitución y vuelvo a las 15:30. Busco a dos personas para compartir el viaje y la gasolina: 30 € al mes cada una. No fumo en el coche y tampoco acepto animales. Si te interesa, escríbeme por aquí.",
   "q": "Álvaro busca personas para...", "o": ["pagar entre todos el viaje.", "ir al polígono por las tardes.", "viajar con su perro."], "ok": 0,
   "cats": ["personas", "cantidad"], "es": "ES-07", "pc": "compartir el viaje y la gasolina: 30 € al mes cada una",
   "why": "Cada persona paga treinta euros al mes por el viaje y la gasolina. Álvaro trabaja por la mañana, y no acepta animales."},
  {"n": 13, "title": "LAVADO DE COCHES BRILLO · ESTACIÓN DE SERVICIO NORTE",
   "body": "Lavado por fuera: 6 €. Lavado completo, por dentro y por fuera: 15 €; tarda unos cuarenta minutos y puedes esperar en nuestra cafetería. Si echas más de 30 € de gasolina, el lavado por fuera es gratis. Abrimos todos los días de 8:00 a 21:00, excepto los domingos por la tarde. No lavamos furgonetas grandes ni camiones.",
   "q": "En este lavado de coches...", "o": ["se puede esperar tomando algo.", "también lavan furgonetas grandes.", "abren todo el domingo."], "ok": 0,
   "cats": ["normas", "tiempo"], "es": "ES-03", "pc": "puedes esperar en nuestra cafetería = esperar tomando algo",
   "why": "Mientras lavan el coche se puede esperar en la cafetería. No lavan furgonetas grandes, y el domingo por la tarde está cerrado."},
 ]}

CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos sobre tres tiendas de barrio con historia. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 15 minutos. Lee primero las seis preguntas. Los tres textos hablan de cosas parecidas (la familia, los horarios, los clientes, cómo ha cambiado el negocio): busca el detalle que los separa. Cuidado: una persona de la familia más joven no es lo mismo que un hermano.",
 "texts": [
  {"name": "La mercería de Amparo", "body": "Amparo Cuesta tiene ochenta y un años y todavía abre cada mañana la mercería que abrió su madre en 1958, en la calle Platerías de Valladolid. Vende botones, hilos, lana y ropa interior. Antes la ayudaba su hermana; hoy trabaja con su nieta Sara, que ha abierto una tienda en internet: ahora mandan botones antiguos a clientes de Japón y de Canadá. Los martes por la tarde, un grupo de vecinas se sienta al fondo de la tienda para hacer punto y charlar. Amparo no quiere jubilarse: dice que la tienda es su casa. Cierra los domingos y todo el mes de agosto."},
  {"name": "Ferretería Gil", "body": "Los hermanos Luis y Jorge Gil tienen la ferretería más antigua de Oviedo, que abrió su abuelo en 1932. En las estanterías de madera hay de todo: tornillos, herramientas, cerraduras y hasta cuerdas para tender la ropa. Muchos clientes no saben cómo se llama lo que necesitan y traen la pieza rota en la mano: Luis casi siempre la encuentra. Desde hace dos años también arreglan pequeños electrodomésticos, como planchas y tostadoras. En 2019 tuvieron que cerrar tres meses por unas obras en el edificio. Abren de lunes a sábado y no tienen página web, porque, según Jorge, la mejor publicidad son los clientes."},
  {"name": "El quiosco de Tomás", "body": "Tomás Herrera vende periódicos desde hace cuarenta años en su quiosco de la plaza de las Flores, en Cádiz. Antes vendía más de doscientos periódicos al día; ahora, unos cincuenta. Por eso también vende agua, caramelos, postales y tarjetas del autobús. Abre a las seis y media de la mañana todos los días del año, también los festivos. Los turistas le preguntan por los monumentos y él les dibuja un pequeño mapa en un papel. En el quiosco hay una libreta donde los vecinos dejan mensajes para otros vecinos. Tomás quiere jubilarse el año que viene, pero su hijo no quiere seguir con el negocio."}],
 "items": [
  {"n": 14, "q": "¿Qué negocio está abierto todos los días?", "ok": 2, "cats": ["tiempo"], "es": "ES-03", "pc": "todos los días del año, también los festivos",
   "why": "El quiosco de Tomás abre todos los días del año. La mercería cierra los domingos y en agosto, y la ferretería, los domingos."},
  {"n": 15, "q": "¿En qué negocio trabaja una persona con alguien más joven de su familia?", "ok": 0, "cats": ["personas"], "es": "ES-08", "pc": "hoy trabaja con su nieta Sara",
   "why": "Amparo trabaja con su nieta. En la ferretería trabajan dos hermanos, y el hijo de Tomás no trabaja en el quiosco."},
  {"n": 16, "q": "¿Qué negocio envía productos a otros países?", "ok": 0, "cats": ["lugares", "pasados"], "es": "ES-03", "pc": "mandan botones antiguos a clientes de Japón y de Canadá",
   "why": "La mercería manda botones a clientes de Japón y de Canadá. A Tomás le preguntan los turistas, pero no envía nada fuera."},
  {"n": 17, "q": "¿Qué negocio ofrece desde hace poco un servicio de reparaciones?", "ok": 1, "cats": ["pasados", "tiempo"], "es": "ES-05", "pc": "desde hace dos años también arreglan pequeños electrodomésticos",
   "why": "Desde hace dos años, en la ferretería arreglan planchas y tostadoras. Encontrar una pieza no es arreglar algo."},
  {"n": 18, "q": "¿Qué negocio estuvo cerrado durante un tiempo?", "ok": 1, "cats": ["pasados"], "es": "ES-05", "pc": "en 2019 tuvieron que cerrar tres meses",
   "why": "La ferretería cerró tres meses en 2019 por unas obras. Que la mercería cierre en agosto es un horario de todos los años, no un cierre especial."},
  {"n": 19, "q": "¿En qué negocio se pueden dejar avisos para otras personas?", "ok": 2, "cats": ["personas", "opinion"], "es": "ES-09", "pc": "una libreta donde los vecinos dejan mensajes para otros vecinos",
   "why": "En el quiosco hay una libreta para los mensajes de los vecinos. En la mercería las vecinas se reúnen para hacer punto, pero no dejan avisos."}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un reportaje sobre un grupo de mujeres que se bañan en el mar en invierno. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto: cada párrafo responde, más o menos, a una pregunta. Atención a lo que pasó el primer día y a lo que pasa ahora, a quién hace cada cosa y a lo que solo quieren hacer.",
 "title": "Las bañistas de invierno",
 "sub": "Reportaje · Revista «Vivir en A Coruña»",
 "body": [
  "Son las ocho de la mañana de un martes de enero y en la playa de Riazor hace nueve grados. Hay poca gente: algunos corredores, un señor con su perro... y un grupo de doce mujeres con gorros de colores que entran en el mar riéndose. Son «Las Focas», y se bañan todos los días del año, también en invierno.",
  "Carmen Barreiro, de sesenta y tres años, es una de las primeras. Fue enfermera durante treinta y cinco años y se jubiló hace cuatro. «Al principio no sabía qué hacer con tanto tiempo libre», cuenta. «Mi vecina Lola se bañaba en el mar todos los inviernos. Un día me invitó y fui solo para mirar. Al final me metí en el agua... ¡y estuve solo un minuto!».",
  "Ahora Carmen está unos diez minutos en el agua. Antes de entrar, el grupo camina un rato por la arena para calentar el cuerpo y, al salir, todas se secan rápido y se ponen ropa de abrigo. Después toman un café caliente en un bar del paseo, donde el dueño les guarda siempre la misma mesa. Carmen dice que es su momento favorito del día: «Hablamos de todo, nos reímos y llego a casa con mucha energía».",
  "Su marido, Andrés, no entiende esta afición. «Él dice que estamos locas», explica Carmen. «Ha venido a la playa a vernos muchas veces, pero nunca se ha bañado. Prefiere el sofá y el periódico». Su hija, que vive en Madrid y trabaja en una agencia de viajes, sí lo probó una vez en Navidad. Le gustó mucho y quiere repetir este verano, pero con el agua un poco más caliente.",
  "Los médicos recomiendan tener cuidado. Antes de empezar, Carmen habló con su médica, que le dijo que sí, pero con algunas normas: nunca sola, nunca después de comer y poco tiempo al principio. «Las Focas» siguen estas normas: cada día hay una persona en la arena que mira el reloj y vigila a las demás. Ese día, esa persona no se baña.",
  "El grupo empezó con tres amigas en 2019 y hoy tiene más de cuarenta personas, pero no todas van cada día. Cada febrero organizan un baño especial para recoger dinero para el hospital infantil de la ciudad, y el año pasado consiguieron casi cuatro mil euros. Carmen ya piensa en el próximo: «Este año queremos ir disfrazadas»."],
 "items": [
  {"n": 20, "q": "«Las Focas» son...", "o": ["un grupo que se baña en el mar todo el año.", "unas mujeres que solo se bañan en verano.", "un club de corredores de la playa."], "ok": 0,
   "cats": ["tiempo", "personas"], "es": "ES-03", "pc": "se bañan todos los días del año, también en invierno",
   "why": "Se bañan todos los días del año, también en invierno. Los corredores son otras personas que están en la playa."},
  {"n": 21, "q": "Carmen empezó a bañarse en invierno...", "o": ["cuando todavía trabajaba de enfermera.", "porque se lo propuso una vecina.", "y el primer día estuvo diez minutos en el agua."], "ok": 1,
   "cats": ["pasados", "personas"], "es": "ES-05", "pc": "un día me invitó · se jubiló hace cuatro · ¡y estuve solo un minuto!",
   "why": "Su vecina Lola la invitó un día. Empezó después de jubilarse, y el primer día estuvo solo un minuto: diez minutos es lo que está ahora."},
  {"n": 22, "q": "Después del baño, el grupo...", "o": ["camina un rato por la arena.", "va a casa de Carmen.", "toma algo en una cafetería."], "ok": 2,
   "cats": ["lugares", "tiempo"], "es": "ES-03", "pc": "antes de entrar, el grupo camina · después toman un café en un bar del paseo",
   "why": "Después toman un café en un bar del paseo. Caminar por la arena es lo que hacen antes de entrar en el agua."},
  {"n": 23, "q": "Andrés, el marido de Carmen,...", "o": ["se baña con ellas los fines de semana.", "no ha probado nunca el baño de invierno.", "lo probó una vez en Navidad."], "ok": 1,
   "cats": ["personas", "opinion"], "es": "ES-08", "pc": "nunca se ha bañado · su hija... sí lo probó una vez en Navidad",
   "why": "Andrés va a verlas, pero nunca se ha bañado. La que lo probó en Navidad es su hija."},
  {"n": 24, "q": "Según el texto, para bañarse en invierno...", "o": ["es mejor no estar solo.", "hay que ir al médico cada mes.", "hay que comer antes de entrar en el agua."], "ok": 0,
   "cats": ["normas"], "es": "ES-03", "pc": "nunca sola · nunca después de comer",
   "why": "Una de las normas es no bañarse nunca sola. La médica le habló una vez, antes de empezar, y no hay que bañarse después de comer."},
  {"n": 25, "q": "Cada febrero, «Las Focas»...", "o": ["se bañan disfrazadas.", "hacen un baño para ayudar a un hospital.", "celebran que empezó el grupo."], "ok": 1,
   "cats": ["planes", "cantidad"], "es": "ES-08", "pc": "un baño especial para recoger dinero para el hospital · este año queremos ir disfrazadas",
   "why": "Cada febrero hacen un baño para recoger dinero para el hospital infantil. Ir disfrazadas es solo una idea para este año, y el texto no dice que el grupo empezó en febrero."},
 ]}

# ---------------- AUDITIVA ("+": parte alta de la extensión, más datos, descartes tardíos, paráfrasis) ----------------
# Sin efectos de sonido (como el examen real). Cada intervención empieza con una etiqueta de emoción de ElevenLabs v3
# (en inglés, entre corchetes): va al guion, no a las transcripciones.
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación: las tres aparecen en el audio y dos se descartan, a veces en la última frase («ah, espere, que ya no está allí»). Fíjate en la pregunta: ¿qué ha comprado ya?, ¿qué hace ahora?, ¿qué va a arreglar? No marques hasta el final.",
 "example": {"q": "¿Qué ha comprado ya la mujer para el cumpleaños?", "o": ["las velas", "los globos", "los platos de papel"], "ok": 0,
   "pres": "Va a escuchar a una mujer que habla por teléfono con su marido.",
   "lines": [("Hombre", "MARIO", "[curious] ¿Dónde estás? ¿Ya has comprado las cosas para el cumpleaños de Pablo?"),
             ("Mujer", "AITANA", "[hurried] Estoy en el supermercado. Los platos de papel aquí no los tienen, así que los compro mañana en la tienda de la esquina."),
             ("Hombre", "MARIO", "[worried] ¿Y los globos? Que Pablo quiere globos azules, no se te olvide, ¿eh?"),
             ("Mujer", "AITANA", "[laughs] Que sí, hombre. Los globos los tiene tu hermana, los compró el domingo. Yo ya tengo las velas, las de números, y ahora voy a por los zumos.")],
   "solucion": "La opción correcta es la letra a. Ya ha comprado las velas.",
   "img": "M03_CA1_0_velas_globos_platos.jpg",
   "prompt": "Panel 1: a small packet of birthday candles shaped like numbers on a kitchen table. Panel 2: a bunch of blue balloons. Panel 3: a stack of white paper plates."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Dónde van a colgar el cuadro?", "o": ["en el salón", "en el dormitorio", "en el pasillo"], "ok": 2,
   "cats": ["lugares", "planes"], "es": "ES-05", "pc": "encima del sofá ya está la foto · el dormitorio es muy oscuro · ¿y en el pasillo? · bueno, vale",
   "pres": "Va a escuchar a una pareja que acaba de comprar un cuadro.",
   "lines": [("Mujer", "EVA", "[excited] ¿Lo ponemos en el salón, encima del sofá? Con las cortinas nuevas queda precioso."),
             ("Hombre", "DANIEL_ES", "[doubtful] Es que encima del sofá ya está la foto de la boda de tus padres... ¿Y en el dormitorio?"),
             ("Mujer", "EVA", "[thoughtful] Mmm, el dormitorio es muy oscuro, no se va a ver. ¿Y en el pasillo, enfrente de la entrada? Es lo primero que se ve."),
             ("Hombre", "DANIEL_ES", "[unsure] No sé, no sé... Bueno, vale, pero el clavo lo pones tú, que yo siempre rompo la pared.")],
   "why": "Lo van a colgar en el pasillo, enfrente de la entrada. En el salón ya está la foto de la boda, y el dormitorio es muy oscuro.",
   "img": "M03_CA1_1_salon_dormitorio_pasillo.jpg", "prompt": "Panel 1: a living room with a sofa and an empty wall above it. Panel 2: a bedroom with a bed and a wardrobe. Panel 3: a narrow hallway of a flat seen from the front door, with an empty wall."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Qué se ha dejado el hombre en el taxi?", "o": ["unos guantes", "una bufanda", "un gorro"], "ok": 1,
   "cats": ["personas", "pasados"], "es": "ES-05", "pc": "los guantes no, que los llevo puestos · el gorro es rojo, de niño · aquí también hay una bufanda gris · ¡esa es!",
   "pres": "Va a escuchar a un hombre que llama a una compañía de taxis.",
   "lines": [("Hombre", "DAVID_M2", "[worried] Buenas tardes. Esta mañana he cogido un taxi en la estación y creo que me he dejado algo dentro."),
             ("Mujer", "LINA", "[helpful] Dígame qué es y lo buscamos. Hoy nos han traído unos guantes negros y un gorro de lana."),
             ("Hombre", "DAVID_M2", "[hopeful] Los guantes no, que los llevo puestos. ¿El gorro es gris?"),
             ("Mujer", "LINA", "[apologetic] No, es rojo, de niño... Ah, espere, aquí detrás hay una bufanda gris, muy larga."),
             ("Hombre", "DAVID_M2", "[relieved] ¡Esa es! Es un regalo de mi madre. Paso a buscarla esta tarde.")],
   "why": "Se ha dejado una bufanda gris. Los guantes los lleva puestos, y el gorro que tienen es de un niño.",
   "img": "M03_CA1_2_guantes_bufanda_gorro.jpg", "prompt": "Panel 1: a pair of black leather gloves on a car seat. Panel 2: a long grey wool scarf on a car seat. Panel 3: a small red woolly hat for a child on a car seat."},
  {"n": 3, "conv": "Conversación tres", "q": "¿Qué hace ahora Leo los martes?", "o": ["inglés", "fútbol", "natación"], "ok": 0,
   "cats": ["tiempo", "pasados"], "es": "ES-07", "pc": "ya no · lo han cambiado al martes · eso era el año pasado · la natación la ha dejado",
   "pres": "Va a escuchar a una madre y a un padre que hablan a la salida del colegio.",
   "lines": [("Mujer", "SARA_JOVEN", "[friendly] Oye, ¿Leo sigue yendo a inglés los lunes con mi hija?"),
             ("Hombre", "VOLU", "[sighs] Ya no. Los lunes el grupo era enorme y la academia lo ha cambiado al martes."),
             ("Mujer", "SARA_JOVEN", "[surprised] ¿Al martes? Pero los martes tenía fútbol, ¿no? Me lo dijo tu mujer."),
             ("Hombre", "VOLU", "[laughs] Eso era el año pasado. Ahora el fútbol es los jueves, y la natación la ha dejado, porque no le gustaba nada. Así que los martes, inglés. ¡Tengo que hacerme un calendario!")],
   "why": "Ahora los martes Leo va a inglés. El fútbol era el martes el año pasado, pero ahora es el jueves, y la natación la ha dejado.",
   "img": "M03_CA1_3_ingles_futbol_natacion.jpg", "prompt": "Panel 1: a boy of about 9 in a small classroom with an English flashcard on the table. Panel 2: a boy of about 9 kicking a football on a school pitch. Panel 3: a boy of about 9 with swimming goggles at the edge of an indoor pool."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Qué va a comprar el chico en la ferretería?", "o": ["una bombilla", "pilas", "cinta para cajas"], "ok": 2,
   "cats": ["personas", "cantidad"], "es": "ES-05", "pc": "la bombilla ya la he cambiado · pilas tenemos · lo que no queda es cinta · eso sí lo compro",
   "pres": "Va a escuchar a una chica que habla con su compañero de piso.",
   "lines": [("Mujer", "FIONA", "[hurried] Oye, ¿vas a la ferretería? Es que se ha fundido la bombilla del baño."),
             ("Hombre", "MILO", "[calm] No, la bombilla ya la he cambiado yo esta mañana. Había una en el cajón de la cocina."),
             ("Mujer", "FIONA", "[relieved] ¡Ah, genial! Entonces, ¿me compras pilas para el mando de la tele?"),
             ("Hombre", "MILO", "[amused] Pilas tenemos, mujer, están en el mismo cajón. Lo que no queda es cinta, y la necesito para cerrar las cajas de la mudanza de mi hermano. Eso sí lo compro.")],
   "why": "Va a comprar cinta para cerrar unas cajas. La bombilla ya la ha cambiado, y pilas tienen en casa.",
   "img": "M03_CA1_4_bombilla_pilas_cinta.jpg", "prompt": "Panel 1: a light bulb on a shop counter. Panel 2: a packet of batteries on a shop counter. Panel 3: a roll of brown packing tape on a shop counter."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Dónde está ahora la parada del autobús?", "o": ["delante del banco", "al lado de la iglesia", "enfrente del mercado"], "ok": 2,
   "cats": ["lugares", "pasados"], "es": "ES-07", "pc": "estaba, pero la han quitado · al principio la pusieron al lado de la iglesia · ya no está allí · la movieron enfrente del mercado",
   "pres": "Va a escuchar a una mujer que pregunta en la calle.",
   "lines": [("Mujer", "TATIANA", "[confused] Perdone, ¿la parada del cuarenta y dos no estaba aquí, delante del banco?"),
             ("Hombre", "LUIS_VEGA", "[friendly] Estaba, sí, pero por las obras la han quitado. Al principio la pusieron al lado de la iglesia..."),
             ("Mujer", "TATIANA", "[relieved] Ah, ¿al lado de la iglesia? Muy bien, muchas gracias."),
             ("Hombre", "LUIS_VEGA", "[apologetic] No, no, espere, que ya no está allí. La semana pasada la movieron enfrente del mercado, porque la calle de la iglesia es muy estrecha. Son dos minutos andando.")],
   "why": "Ahora está enfrente del mercado. Delante del banco estaba antes de las obras, y al lado de la iglesia estuvo solo al principio.",
   "img": "M03_CA1_5_banco_iglesia_mercado.jpg", "prompt": "Panel 1: a bus stop in front of a bank branch in a Spanish town. Panel 2: a bus stop next to a small stone church. Panel 3: a bus stop in front of the entrance of a covered market."},
  {"n": 6, "conv": "Conversación seis", "q": "¿Qué va a arreglar mañana el dueño del piso?", "o": ["la ducha", "la persiana", "la calefacción"], "ok": 1,
   "cats": ["planes", "tiempo"], "es": "ES-05", "pc": "la ducha ya funciona · la persiana no baja · la calefacción, en noviembre · lo de la persiana... mañana",
   "pres": "Va a escuchar a una chica que llama al dueño de su piso.",
   "lines": [("Mujer", "SOFIA", "[worried] Hola, Andrés, soy Paula, la del tercero. Es que esta mañana la ducha no tenía agua caliente..."),
             ("Hombre", "JAVI_ROJAS", "[sighs] ¿Otra vez? Si el técnico la arregló en septiembre..."),
             ("Mujer", "SOFIA", "[apologetic] No, no, la ducha ya funciona: era la luz del calentador. Lo que pasa es que la persiana del dormitorio no baja... Y la calefacción calienta poco, pero eso ya lo sabe."),
             ("Hombre", "JAVI_ROJAS", "[resigned] La calefacción la miramos en noviembre. Lo de la persiana es más urgente: mañana voy yo a verla.")],
   "why": "Mañana va a arreglar la persiana. La ducha ya funciona, y la calefacción la van a mirar en noviembre.",
   "img": "M03_CA1_6_ducha_persiana_calefaccion.jpg", "prompt": "Panel 1: a shower with a white shower head in a small bathroom. Panel 2: a bedroom window with a half-closed roller shutter. Panel 3: a white radiator under a living room window."},
 ]}

CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. Los audios de este modelo tienen muchos datos: busca solo el que te pide la pregunta. Las opciones falsas usan palabras que sí se oyen (gratis, los sábados, los padres), pero con otro dato; la buena dice lo mismo con otras palabras.",
 "example": {"q": "Hoy en el programa...", "o": ["hablan con un cocinero.", "dan las noticias del día.", "ponen solo música."], "ok": 0,
   "why": "La opción correcta es la A porque hoy hablan con un cocinero que ha abierto un restaurante.",
   "lab": "Locutor", "voice": "SERGIO/RADIO",
   "text": "[cheerful] ¡Muy buenos días y bienvenidos a «Mañanas de domingo»! Hasta la una os acompañamos con música, recetas y planes para el fin de semana. Hoy hablamos con Nacho Prieto, un cocinero de Alicante que ha abierto un restaurante sin carne ni pescado. Y a las doce, como siempre, el concurso de los oyentes.",
   "solucion": "La opción correcta es la letra a, porque hoy hablan con un cocinero."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "En Colchones Sueño Azul...", "o": ["montar la cama no está incluido en el precio.", "las almohadas tienen un veinte por ciento de descuento.", "hay que pagar para recibir el colchón en casa."], "ok": 0,
   "cats": ["cantidad", "normas"], "es": "ES-03", "pc": "el montaje de las camas se paga aparte = no está incluido · las almohadas, dos por el precio de una",
   "lab": "Locutor", "voice": "BOBBY/RADIO",
   "text": "[excited] ¡Llega la semana del descanso a Colchones Sueño Azul! Todos los colchones, con un veinte por ciento de descuento, y las almohadas, dos por el precio de una. Y si no duermes bien, tienes cien noches para probarlo y devolverlo. Te lo llevamos a casa gratis, pero el montaje de las camas se paga aparte.",
   "why": "El montaje de las camas se paga aparte: no está incluido. El veinte por ciento es para los colchones, y llevar el colchón a casa es gratis."},
  {"n": 8, "conv": "Audio 2", "q": "La noche de estrellas del observatorio...", "o": ["se cambia de día si el cielo no está despejado.", "cuesta muy poco dinero.", "empieza a media tarde."], "ok": 0,
   "cats": ["planes", "tiempo"], "es": "ES-06", "pc": "si hay nubes, lo dejamos para el sábado siguiente · la entrada es gratuita · desde las diez de la noche",
   "lab": "Locutora", "voice": "DIANA/RADIO",
   "text": "[warm] Este sábado, noche de estrellas en el observatorio de la sierra. Desde las diez de la noche, los astrónomos del club explican el cielo y se puede mirar por los telescopios. La entrada es gratuita, pero hay que reservar en la web, porque solo hay cien plazas. Si hay nubes, lo dejamos para el sábado siguiente.",
   "why": "Si hay nubes, se hace el sábado siguiente: cambia de día. La entrada es gratis, no barata, y empieza a las diez de la noche."},
  {"n": 9, "conv": "Audio 3", "q": "Con la nueva parada del tranvía...", "o": ["todos los viajeros van gratis una semana.", "por la tarde pasan menos tranvías.", "se abre una parada en la plaza del Sol."], "ok": 1,
   "cats": ["tiempo", "lugares"], "es": "ES-03", "pc": "cada diez minutos por la mañana y cada veinte por la tarde = menos por la tarde · gratis solo los estudiantes",
   "lab": "Locutor", "voice": "SANTIAGO_ES/RADIO",
   "text": "[informative] Desde el lunes, la línea dos del tranvía tiene una parada nueva en la universidad. Los tranvías pasan cada diez minutos por la mañana y cada veinte por la tarde. Durante la primera semana, los estudiantes viajan gratis con el carné universitario. Atención: la parada de la plaza del Sol está cerrada hasta marzo por obras.",
   "why": "Por la tarde pasa un tranvía cada veinte minutos, no cada diez: pasan menos. Solo viajan gratis los estudiantes, y la parada de la plaza del Sol está cerrada."},
  {"n": 10, "conv": "Audio 4", "q": "En el mercadillo de ropa infantil...", "o": ["solo se puede comprar ropa.", "las familias pueden vender ropa usada.", "no hace falta apuntarse para vender."], "ok": 1,
   "cats": ["normas", "personas"], "es": "ES-03", "pc": "puedes vender la ropa que ya no usan tus hijos · para vender, hay que apuntarse antes",
   "lab": "Locutora", "voice": "TAMARA/RADIO",
   "text": "[cheerful] Ven al mercadillo de ropa infantil de segunda mano, el domingo de diez a dos, en el patio del colegio Cervantes. Puedes vender la ropa que ya no usan tus hijos y comprar otra a precios muy bajos. Para vender, hay que apuntarse antes en la asociación de padres. ¡Y hay juegos para los niños!",
   "why": "Las familias pueden vender la ropa que ya no usan sus hijos. También se compra, y para vender hay que apuntarse antes."},
  {"n": 11, "conv": "Audio 5", "q": "En el taller de cocina del mercado...", "o": ["los niños hacen la compra antes de cocinar.", "los padres cocinan con sus hijos.", "hay que llevar los ingredientes."], "ok": 0,
   "cats": ["personas", "cantidad"], "es": "ES-03", "pc": "compran en los puestos con un cocinero y después preparan una receta · los padres no pueden entrar",
   "lab": "Locutora", "voice": "LYDIA/RADIO",
   "text": "[friendly] Este mes, el mercado central organiza talleres de cocina para niños de seis a doce años. Los sábados a las once, los niños compran en los puestos con un cocinero y después preparan una receta sencilla. Cuesta cinco euros y los ingredientes están incluidos. Los padres no entran en la cocina: esperan en la cafetería.",
   "why": "Primero compran en los puestos y después cocinan. Los padres no entran en la cocina, y los ingredientes están incluidos."},
  {"n": 12, "conv": "Audio 6", "q": "En la oficina de empleo...", "o": ["para renovar la demanda hay que pedir cita.", "para hablar con un orientador hay que llamar antes.", "se puede ir también por la tarde."], "ok": 1,
   "cats": ["normas", "tiempo"], "es": "ES-03", "pc": "para hablar con un orientador, sí hay que pedir cita, por teléfono = llamar antes",
   "lab": "Locutor", "voice": "DAVID_LAT/RADIO",
   "text": "[neutral] La oficina de empleo del ayuntamiento informa: desde el uno de diciembre ya no es necesario pedir cita para renovar la demanda de empleo. Se puede hacer por internet. Para hablar con un orientador, en cambio, sí hay que pedir cita por teléfono. La oficina abre de lunes a viernes, de ocho a dos.",
   "why": "Para ver a un orientador hay que pedir cita por teléfono: llamar antes. Para renovar ya no hace falta cita, y la oficina cierra a las dos."},
 ]}

CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Irene y Héctor. Indique si los enunciados (del 13 al 18) se refieren a Irene (A), a Héctor (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Irene y Héctor hablan de sus vecinos. Cuidado con lo que hace otra persona (la hermana de Héctor) y con lo que alguien piensa o quiere hacer, pero no ha hecho: en esos casos, la respuesta es C.",
 "who": ["Irene", "Héctor"], "voices": {"IRENE": "ESTELA", "HECTOR": "DANI"},
 "lines": [
  ("HECTOR", "[curious] Irene, ¡qué ojeras! ¿No duermes bien?"),
  ("IRENE", "[laughs] Ahora ya sí. Es que en septiembre llegaron vecinos nuevos al piso de arriba, con un bebé de tres meses, y el niño lloraba toda la noche. Las primeras semanas casi no dormía."),
  ("HECTOR", "[sympathetic] Uf, qué horror. ¿Y no les dijiste nada?"),
  ("IRENE", "[thoughtful] Al principio pensaba escribirles una nota, pero me daba vergüenza. Al final me compré unos tapones para los oídos y desde entonces duermo como un tronco. Y la semana pasada los invité a cenar a casa: son majísimos."),
  ("HECTOR", "[sighs] Pues lo mío no tiene solución. Ya sabes que vivo en un primero, encima de un bar. Hasta la una de la mañana, música y gente en la terraza."),
  ("IRENE", "[surprised] ¿Y no te mudas?"),
  ("HECTOR", "[frustrated] Quiero, pero llevo dos meses buscando piso y no encuentro nada barato. Mi hermana Marta vive en el ático del mismo edificio y dice que allí arriba no se oye nada... ¡Qué suerte tiene!"),
  ("IRENE", "[teasing] ¿Y por qué no te vas a vivir con ella?"),
  ("HECTOR", "[laughs] ¿Con Marta y sus tres gatos? No, gracias. Además, el dueño del bar es muy simpático. A veces bajo a tomar algo con él y me olvido del ruido."),
  ("IRENE", "[cheerful] Ya ves. Yo ahora hasta cuido al bebé algún sábado, y así sus padres pueden ir al cine."),
  ("HECTOR", "[impressed] ¿Tú? ¡Pero si antes no te gustaban nada los niños!"),
  ("IRENE", "[laughs] La gente cambia. Oye, en tu edificio, ¿hay reuniones de vecinos? Yo quiero organizar una para poner un sitio para las bicis en el patio."),
  ("HECTOR", "[amused] Sí, una al mes, pero yo no voy nunca. Siempre va mi hermana, que es la presidenta.")],
 "items": [
  {"n": 13, "q": "Ha encontrado una forma de dormir bien.", "ok": 0, "cats": ["pasados", "opinion"], "es": "ES-07", "pc": "me compré unos tapones... desde entonces duermo como un tronco",
   "why": "Irene se compró tapones y desde entonces duerme bien. El problema de Héctor, en cambio, no tiene solución."},
  {"n": 14, "q": "Vive en la parte más alta de su edificio.", "ok": 2, "cats": ["lugares", "personas"], "es": "ES-08", "pc": "mi hermana Marta vive en el ático · vivo en un primero",
   "why": "La que vive en el ático es Marta, la hermana de Héctor: una tercera persona. Héctor vive en un primero, e Irene tiene vecinos arriba: ninguno de los dos."},
  {"n": 15, "q": "Ha comido con sus vecinos en su casa.", "ok": 0, "cats": ["personas", "pasados"], "es": "ES-03", "pc": "la semana pasada los invité a cenar a casa",
   "why": "Irene invitó a cenar a sus vecinos la semana pasada. Pensó en escribirles una nota, pero no lo hizo."},
  {"n": 16, "q": "Está buscando otra casa.", "ok": 1, "cats": ["planes", "lugares"], "es": "ES-03", "pc": "llevo dos meses buscando piso",
   "why": "Héctor lleva dos meses buscando piso, todavía sin suerte."},
  {"n": 17, "q": "Va a las reuniones de la comunidad.", "ok": 2, "cats": ["planes", "personas"], "es": "ES-05", "pc": "yo quiero organizar una · yo no voy nunca · siempre va mi hermana",
   "why": "A las reuniones va la hermana de Héctor; él no va nunca, e Irene solo quiere organizar una: ninguno de los dos."},
  {"n": 18, "q": "Tiene buena relación con el dueño de un negocio.", "ok": 1, "cats": ["personas", "opinion"], "es": "ES-03", "pc": "el dueño del bar es muy simpático · bajo a tomar algo con él",
   "why": "Héctor dice que el dueño del bar es muy simpático y a veces toma algo con él."}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. Son frases generales («un pedido», «un servicio», «alguien») y hay parejas muy parecidas (pedir prestado / ofrecer, abrir más tarde / cerrar antes): en cada mensaje pregúntate quién habla y qué cambia exactamente. Sobran tres enunciados.",
 "enun": [
  "Una clase cambia de lugar.",
  "Alguien pide que le presten algo.",
  "Un pedido va a llegar otro día.",
  "Hay que ir a buscar algo a una oficina.",
  "Un arreglo va a costar más de lo previsto.",
  "Un servicio abre más tarde de lo normal.",
  "Hay que recoger antes a un niño.",
  "Alguien ofrece dejar algo suyo.",
  "Un pedido se ha cancelado.",
  "Un servicio cierra antes de lo normal.",
  "Alguien invita a una celebración y pide que no se lo cuenten a nadie."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "MARINA_ES/RADIO",
   "text": "[polite] Buenas tardes, le llamamos de la academia Idiomas Plus. Le recordamos que desde esta semana su clase de francés ya no es en el aula tres, sino en la sala del segundo piso. El horario no cambia: martes y jueves a las siete.",
   "solucion": "La opción correcta es la letra a: una clase cambia de lugar."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 2, "cats": ["planes", "tiempo"], "es": "ES-10", "pc": "su nevera no puede llegar mañana martes · se la llevamos el jueves",
   "lab": "Contestador", "voice": "OSCAR/RADIO",
   "text": "[professional] Buenos días, le llamamos de Electrodomésticos Ramírez. Su nevera nueva no puede llegar mañana martes, como le dijimos, porque el camión ha tenido una avería. Se la llevamos el jueves, a la misma hora. Si no le va bien, llámenos, por favor.",
   "why": "La nevera llega el jueves en vez del martes: el pedido llega otro día. No se ha cancelado (I sobra)."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 4, "cats": ["cantidad", "normas"], "es": "ES-10", "pc": "el presupuesto ya no es de doscientos euros, sino de trescientos cincuenta",
   "lab": "Contestador", "voice": "DANIEL_CO/RADIO",
   "text": "[apologetic] Soy Ramón, del taller. Ya hemos mirado su coche. El problema no son solo los frenos: también hay que cambiar una pieza del motor. Así que el presupuesto ya no es de doscientos euros, sino de trescientos cincuenta. ¿Seguimos con el arreglo?",
   "why": "El arreglo del coche va a costar más de lo que le dijeron: trescientos cincuenta euros en vez de doscientos."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 6, "cats": ["personas", "tiempo"], "es": "ES-10", "pc": "¿puede venir a buscarlo antes de comer, en vez de a las cinco?",
   "lab": "Contestador", "voice": "SARA_2/RADIO",
   "text": "[calm] Hola, buenos días, le llamo de la escuela infantil Los Peques. Lucas está bien, no se preocupe, pero tiene un poco de fiebre y está muy cansado. ¿Puede venir a buscarlo antes de comer, sobre las doce, en vez de a las cinco?",
   "why": "La escuela infantil pide ir a buscar a Lucas a las doce, no a las cinco: hay que recoger antes a un niño."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 10, "cats": ["planes", "personas"], "es": "ES-10", "pc": "una fiesta sorpresa · ¡no le digas nada a nadie!",
   "lab": "Contestador", "voice": "RITA/RADIO",
   "text": "[excited] ¡Hola, Nuria! Soy Lorena. El sábado que viene Toni cumple cuarenta años y le estamos preparando una fiesta sorpresa en casa de su hermano, a las nueve. ¿Te vienes? Eso sí, no le digas nada a nadie, que Toni se entera de todo.",
   "why": "Lorena invita a una fiesta sorpresa y pide que no se lo digan a nadie."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 9, "cats": ["tiempo", "lugares"], "es": "ES-10", "pc": "megafonía · hoy cierra a las ocho, dos horas antes que otros días",
   "lab": "Megafonía", "voice": "ENRIQUE/RADIO",
   "text": "[neutral] Atención, por favor. Les informamos de que hoy, por la fiesta local, el centro comercial cierra a las ocho de la tarde, dos horas antes que otros días. El aparcamiento cierra a las ocho y media. Muchas gracias por su visita.",
   "why": "El centro comercial cierra hoy dos horas antes. No abre más tarde (F sobra)."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 7, "cats": ["personas", "planes"], "es": "ES-10", "pc": "yo tengo una que casi no uso · si quieres, te la dejo",
   "lab": "Contestador", "voice": "JANET/RADIO",
   "text": "[friendly] Hola, Pablo, soy Silvia. Me ha dicho tu hermana que este fin de semana os vais de acampada y que no tenéis tienda. Yo tengo una para cuatro que casi no uso. Si quieres, te la dejo: pásate esta tarde por mi casa.",
   "why": "Silvia ofrece dejarle su tienda de campaña. No es ella la que pide algo prestado (B sobra)."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 3, "cats": ["lugares", "normas"], "es": "ES-10", "pc": "no había nadie en casa · puede recogerlo en nuestra oficina",
   "lab": "Contestador", "voice": "ALBERTO/RADIO",
   "text": "[neutral] Buenos días. Le informamos desde Correos de que esta mañana hemos intentado entregarle un paquete, pero no había nadie en casa. Puede recogerlo en nuestra oficina de la calle Colón, con su documento de identidad, desde mañana y durante quince días.",
   "why": "Hay que ir a la oficina de Correos a recoger un paquete."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

# Voces del último modelo que han hecho (M2): no se repiten aquí. Más las descartadas por María (22/10).
VOCES_EVITAR = ["CAROLINA", "JAVIER", "EMILIO", "SUSANA", "VALENTINA", "CRISTINA", "SARA", "DAVID_M1", "ERIK", "MARTIN_3",
                "ANA_MARIA", "AGUSTIN", "TOMAS", "MIA", "EFRAYN", "MARTIN_2", "JUAN_CARLOS", "GABI", "LUCIA", "NINOSKA",
                "SANTIAGO_LAT", "RAQUEL", "GABRIEL_ES", "MAYA", "LUISA", "CRISTINA_LAT", "CRISTIAN", "MARTIN_1",
                "LUIS_GUILLERMO", "JUAN_RESTREPO", "DIEGO_PE",
                "HUGO", "CLARA", "LUCIA_AR"]   # estas tres, descartadas por María (22/10)
REPARTO = """# REPARTO DE VOCES M03 (ninguna voz del M2, el último modelo que han hecho, ni de las descartadas)
# SIN EFECTOS DE SONIDO: ni sintonía, ni din-don, ni pitido (el examen real tampoco los tiene).
# Cada intervención lleva al principio su etiqueta de emoción de ElevenLabs v3 ([cheerful], [sighs]...).
# T1 conversaciones (v3): 0 el cumpleaños = MARIO + AITANA · 1 el cuadro = EVA + DANIEL_ES · 2 el taxi = DAVID_M2 + LINA (Colombia)
#   3 el inglés de Leo = SARA_JOVEN + VOLU · 4 la ferretería = FIONA + MILO · 5 la parada = TATIANA (Latinoamérica) + LUIS_VEGA
#   6 el dueño del piso = SOFIA (Colombia) + JAVI_ROJAS
# T2 radio (perfil /RADIO): 0 «Mañanas de domingo» = SERGIO · 1 Sueño Azul = BOBBY · 2 observatorio = DIANA (Colombia)
#   3 tranvía = SANTIAGO_ES · 4 mercadillo infantil = TAMARA (México) · 5 taller de cocina = LYDIA · 6 oficina de empleo = DAVID_LAT
# T3 conversación entre amigos: IRENE = ESTELA · HÉCTOR = DANI
# T4 mensajes (/RADIO): 0 academia = MARINA_ES · 1 nevera = OSCAR · 2 taller = DANIEL_CO (Colombia) · 3 escuela infantil = SARA_2
#   4 fiesta sorpresa = RITA (Argentina) · 5 megafonía del centro comercial = ENRIQUE (México) · 6 la tienda de campaña = JANET (Argentina)
#   7 Correos = ALBERTO (Latinoamérica)"""

# ---------------- ESCRITURA ("=": como el examen) ----------------
# Textos modelo: [n] = empieza la frase de la pauta n · _texto_ = conector (sale subrayado).
ESCRITA = {"t1": {"instr": "Su amigo Fede le ha escrito este correo.", "trato": "tú",
  "input": ["¡Hola! ¿Te acuerdas de mí? Estoy organizando una cena con los compañeros del instituto: ¡hace veinte años que terminamos! Es el sábado 14 de junio, en Salamanca. ¿Vas a venir? Y cuéntame qué es de tu vida, que no sé nada de ti.", "Un abrazo,<br>Fede"],
  "lead": "Conteste a Fede. En el correo tiene que:",
  "pautas": ["saludar y decirle qué le parece la idea de la cena;", "decirle si va a ir o no, y por qué;", "contarle qué ha hecho estos años y a qué se dedica ahora;", "proponerle quedar los dos antes del verano: día, lugar y qué pueden hacer;", "hacerle dos preguntas sobre los antiguos compañeros y despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Una revista en español busca textos de sus lectores sobre el trabajo. Escriba un texto sobre su primer trabajo. Hable de:",
   "pautas": ["qué trabajo era, cuántos años tenía y cómo lo encontró;", "cómo era un día normal: el horario, las tareas y los compañeros;", "algo bueno o malo que le pasó allí y qué aprendió;", "qué hace ahora y en qué se parece o no a ese primer trabajo;", "cómo es para usted un buen trabajo."]},
  "op2": {"title": "Opción 2", "intro": "Mateo Ruiz es profesor de piano en Calatayud, un pueblo de Zaragoza. Aquí tiene tres fotos de su vida.",
   "photos": ["1998. Mateo, un niño de unos ocho años, toca el piano en el salón de su casa. Su abuela, sentada a su lado, le enseña las notas.",
              "2012. Mateo, de unos veintidós años, toca el teclado con la orquesta de las fiestas, en un escenario en la plaza de un pueblo, de noche.",
              "Hoy. Mateo da clase de piano a una niña en una escuela de música; detrás, otros niños esperan con sus mochilas."],
   "ficha": [], "intro2": "Escriba un texto sobre la vida de Mateo. Hable de:",
   "pautas": ["cómo empezó Mateo con la música y cómo era su abuela;", "qué hacía en la orquesta y cómo era su vida en esa época;", "qué hace ahora y por qué cree usted que dejó la orquesta."],
   "img": "M03_escrita_mateo_piano.jpg", "imgAlt": "Tres fotos de la vida de Mateo: de niño toca el piano con su abuela, de joven toca el teclado con una orquesta en la plaza de un pueblo y hoy da clase de piano a una niña"},
  "min": 70, "max": 80},
 "modelos": {
  "t1": {"titulo": "Tarea 1 · Correo a un amigo (de tú)", "tarea": 1,
   "aprobado": {"texto": [
     "[1]¡Hola, Fede! ¡Qué sorpresa! Me parece una idea muy buena.",
     "[2]Sí, voy a ir a la cena. Tengo muchas ganas de ver a todos. [3]Estos años he vivido en Lisboa y ahora trabajo en un hotel en Sevilla. [4]¿Quedamos el sábado 10 de mayo en la Plaza Mayor? Podemos comer y pasear. [5]¿Va a ir Marta? ¿Sabes algo de Javier?",
     "Un abrazo,<br>Elena"],
    "porque": "Contesta a las cinco pautas con frases sencillas: le gusta la idea, dice que va, cuenta lo que ha hecho con el pretérito perfecto (he vivido) y lo que hace ahora en presente, propone día, lugar y plan, y hace dos preguntas. Todo de tú, del saludo a la despedida."},
   "excelente": {"texto": [
     "[1]¡Hola, Fede! ¡Qué alegría saber de ti! La cena me parece una idea genial.",
     "[2]Claro que voy, _porque_ no quiero perderme la fiesta. [3]Estos años he vivido en Lisboa _y ahora_ trabajo de recepcionista en un hotel de Sevilla. [4]¿Te va bien el sábado 10 de mayo? Quedamos en la Plaza Mayor _y después_ comemos juntos. [5]_Por cierto_, ¿vienen los profesores? ¿Qué es de Javier?",
     "¡Un abrazo!<br>Elena"],
    "porque": "Las mismas cinco pautas, con dos o tres mejoras del A2: conectores para unir las ideas (porque, y ahora, y después, por cierto), palabras más precisas (genial, perderme, de recepcionista), un porqué y una propuesta más amable (¿te va bien...?). Sigue siendo corto y de tú.",
    "mejoras": ["un conector más (porque, y después, por cierto)", "una palabra más precisa (genial, trabajo de recepcionista)", "un porqué (no quiero perderme la fiesta)", "una propuesta más amable (¿Te va bien el sábado...?)"]}},
  "op1": {"titulo": "Tarea 2 · Opción 1 · Mi primer trabajo", "tarea": 2,
   "aprobado": {"texto": [
     "[1]Mi primer trabajo fue en una tienda de ropa de mi barrio. Tenía dieciocho años y lo encontré por una amiga. [2]Trabajaba los sábados de diez a ocho. Doblaba la ropa y ayudaba a los clientes. Mis compañeros eran muy simpáticos. [3]Un día perdí las llaves de la tienda y mi jefa se enfadó mucho. Aprendí a ser más ordenada. [4]Ahora soy profesora y también hablo con mucha gente. [5]Para mí, un buen trabajo tiene buenos compañeros."],
    "porque": "Cumple las cinco pautas, una o dos frases para cada una. Usa el imperfecto para describir el trabajo y lo que hacía (tenía, trabajaba, doblaba), el indefinido para lo que pasó (fue, encontré, perdí) y el presente para ahora. Es sencillo y aprueba."},
   "excelente": {"texto": [
     "[1]Mi primer trabajo fue en una tienda de ropa de mi barrio. Tenía dieciocho años _y_ lo encontré gracias a una amiga. [2]Trabajaba los sábados de diez a ocho: doblaba ropa, ordenaba el almacén _y_ atendía a los clientes. [3]Una vez perdí las llaves de la tienda _y_ mi jefa se enfadó muchísimo, _pero_ aprendí a ser ordenada. [4]Ahora soy profesora _y también_ hablo con gente todo el día. [5]_Por eso_ creo que un buen trabajo necesita buenos compañeros."],
    "porque": "Las mismas cinco pautas, con más variedad: verbos más precisos para las tareas (ordenaba, atendía), conectores para contar y explicar (pero, y también, por eso), una opinión con creo que y una relación clara entre el pasado y el presente. Todo sigue siendo A2.",
    "mejoras": ["verbos más precisos (ordenaba el almacén, atendía a los clientes)", "un conector más (pero, y también, por eso)", "una opinión con creo que", "una relación entre el pasado y ahora (también hablo con gente todo el día)"]}},
  "op2": {"titulo": "Tarea 2 · Opción 2 · Mateo y el piano", "tarea": 2,
   "aprobado": {"texto": [
     "[1]Mateo empezó con el piano en 1998, cuando tenía ocho años. Su abuela le enseñaba en el salón de su casa. Era una mujer muy paciente y le encantaba la música. [2]En 2012 tocaba el teclado en una orquesta. Iba a muchas fiestas de pueblos y dormía poco. [3]Ahora da clases de piano a niños en una escuela de música. Creo que dejó la orquesta porque estaba muy cansado de viajar."],
    "porque": "Cuenta la vida de Mateo en pasado y en presente (no describe las fotos): el imperfecto para describir a la abuela y cómo era su vida en la orquesta (era, tocaba, iba), el indefinido para lo que empezó (empezó) y el presente para ahora. Responde a las tres pautas, también a la suposición del final (creo que dejó la orquesta porque...)."},
   "excelente": {"texto": [
     "[1]Mateo empezó a tocar el piano en 1998, _cuando_ tenía ocho años. Su abuela, una mujer muy paciente, le enseñaba las notas todas las tardes. [2]_Después_, en 2012, tocaba el teclado en la orquesta de las fiestas: viajaba todos los fines de semana _y_ volvía a casa muy tarde. [3]Hoy da clase a niños en una escuela de música. Supongo que dejó la orquesta _porque_ quería una vida más tranquila."],
    "porque": "Más variedad: conectores que ordenan la vida de Mateo (cuando, después, porque), detalles de cómo era su vida (todas las tardes, todos los fines de semana, volvía muy tarde), palabras más precisas (supongo, las notas) y una suposición con su porqué.",
    "mejoras": ["un conector más (cuando, después)", "detalles de costumbre en imperfecto (todas las tardes, todos los fines de semana)", "una palabra más precisa (supongo, las notas)", "una suposición con su porqué (quería una vida más tranquila)"]}}}}

# ---------------- ORAL ("=": como el examen) ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: una persona importante en mi vida", "pautas": ["quién es, cómo es y desde cuándo la conoce;", "cómo la conoció y cómo era su relación al principio;", "qué hacen juntos normalmente o qué hacían antes;", "a qué personas admira la gente de su país y por qué;", "qué quiere hacer con esa persona este año."]},
  {"title": "Opción 2: mi barrio", "pautas": ["dónde está su barrio y desde cuándo vive allí;", "cómo es: qué hay y qué sitios le gustan más;", "cómo era el barrio donde vivía cuando era pequeño o pequeña;", "si en su país la gente conoce normalmente a sus vecinos y por qué;", "qué cosas faltan en su barrio y qué hace allí los fines de semana."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1 · Hacer deporte", "desc": "Los aparatos de gimnasia de un parque de una ciudad, una mañana de otoño. Una mujer de unos cincuenta y cinco años, con mallas negras, una sudadera rosa y una cinta en el pelo, pedalea en una de las máquinas y se ríe. A su lado, un chico de unos veinticinco años, con pantalón corto, camiseta gris y auriculares al cuello, le enseña algo en el móvil. En el suelo hay una botella de agua, una mochila y una toalla. Al fondo, un señor mayor hace ejercicio en otro aparato; hay árboles con hojas amarillas, unos bancos y un perro atado a una farola que los mira.", "img": "M03_oral_foto1_parque_deporte.jpg"},
  {"title": "Fotografía 2 · Ver la televisión", "desc": "El salón de un piso, una tarde de domingo de invierno. Una señora de unos setenta y cinco años, con el pelo gris recogido, gafas y una rebeca azul, está sentada en el sofá con una manta en las piernas y el mando de la tele en la mano; mira la pantalla con cara de no entender nada. A su lado, un chico de unos dieciséis años, con una sudadera con capucha y calcetines de colores, le señala un botón del mando y se ríe. En la pantalla se ve el menú de una plataforma con muchas películas. En la mesa baja hay una bandeja con dos tazones de sopa, pan y dos vasos de agua. Al fondo hay una estantería con fotos de familia, una planta y unas zapatillas en el suelo.", "img": "M03_oral_foto2_salon_tele_mando.jpg"}],
  "pautas": ["¿Cómo son las personas de la foto (físico, personalidad que cree que tienen...)? ¿Qué ropa llevan?", "¿Dónde están esas personas? ¿Qué objetos hay? Describa el lugar.", "¿Qué están haciendo las personas de la foto?", "¿Qué relación cree que hay entre ellas?", "¿Qué cree que piensan o cómo se sienten estas personas? ¿Por qué?", "¿Qué cree que han hecho antes? ¿Y qué van a hacer después?"]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1 · Empezar un deporte juntos", "intro": "Usted y un amigo o una amiga quieren empezar a hacer deporte juntos. Hoy hablan de qué deporte pueden hacer. El examinador / La examinadora es su amigo/a. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su amigo/a, tiene que hablar de:", "pautas": ["qué deporte hacía cuando era pequeño o pequeña y si hace alguno ahora;", "cómo es su horario de trabajo o de estudios esta temporada;", "qué deporte quieren hacer y por qué;", "dónde lo van a hacer: en un gimnasio, en un club o al aire libre;", "qué días y a qué hora van a quedar, y qué tienen que comprar."]},
  {"title": "Si eligió la fotografía 2 · ¿Qué serie vemos?", "intro": "Usted comparte piso con un amigo o una amiga. Este fin de semana no van a salir y quieren empezar a ver una serie juntos en casa. El examinador / La examinadora es su compañero/a de piso. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su compañero/a, tiene que hablar de:", "pautas": ["qué tipo de series o películas le gustan y cuáles no;", "qué veía en la tele cuando era pequeño o pequeña;", "qué serie quieren ver y por qué;", "si prefiere verla en español o en su idioma, con subtítulos o sin ellos, y por qué;", "qué día empiezan, cuántos capítulos ven y qué cenan ese día."]}]}}

# Modelos de la tarea 3 (se ven en la oral del estudiante después de la prueba y en la libreta de la profesora).
# En el diálogo, "E" = examinador y "C" = candidato. La frase del pequeño problema lleva True.
# Como en las láminas de 2022, las dos situaciones son de tú y mezclan planificar con contar cosas propias.
ORAL_MODELOS = {"t3": [
 {"titulo": "Fotografía 1 · Empezar un deporte juntos", "trato": "tú",
  "notas": [["deporte de pequeño y ahora", "baloncesto en el colegio, diez años · ahora nada: solo ando"],
            ["mi horario", "oficina de 8 a 3 · tardes libres · los viernes, clase de inglés"],
            ["qué deporte", "correr: barato, al aire libre · o natación"],
            ["dónde", "parque del río por la tarde · si llueve, piscina municipal"],
            ["días, hora, comprar", "martes y jueves a las 6 · zapatillas nuevas, una botella"]],
  "segunda": "Si el examinador no puede correr: ir a nadar a la piscina municipal o montar en bici por el río.",
  "problema": "El examinador quiere hacer deporte, pero el médico le ha dicho que no puede correr unos meses porque tiene mal la rodilla.",
  "dialogo": [
   ["E", "¡Hola! Oye, ¿al final empezamos a hacer deporte juntos? ¿Hablamos un poco?"],
   ["C", "¡Hola! Sí, claro. De pequeño jugaba al baloncesto en el colegio, pero ahora no hago nada: solo ando un poco. ¿Y tú?"],
   ["E", "Yo hacía un poco de todo, pero hace años que no hago nada. ¿Qué horario tienes ahora?"],
   ["C", "Trabajo en una oficina de ocho a tres, así que tengo las tardes libres. Los viernes voy a clase de inglés. ¿Y tú cuándo puedes?"],
   ["E", "Yo también tengo las tardes libres. ¿Y qué deporte hacemos?"],
   ["C", "¿Qué te parece correr? Es barato y estamos al aire libre."],
   ["E", "Pues mira, hay un problema: tengo mal la rodilla y el médico me ha dicho que no puedo correr unos meses...", True],
   ["C", "¡Vaya, lo siento! Entonces, ¿y si vamos a nadar? Nadar es bueno para la rodilla. La piscina municipal está cerca de casa. ¿Te va bien?"],
   ["E", "¡Buena idea! Me encanta nadar. ¿Qué días vamos?"],
   ["C", "Los martes y los jueves a las seis, por ejemplo. Los viernes yo no puedo."],
   ["E", "Perfecto. ¿Y tenemos que comprar algo?"],
   ["C", "Yo necesito un bañador y unas gafas de piscina. Podemos ir a comprarlas juntos el sábado. ¡Hasta luego!"]]},
 {"titulo": "Fotografía 2 · ¿Qué serie vemos?", "trato": "tú",
  "notas": [["qué me gusta", "series de policías y comedias · no me gustan las de miedo"],
            ["la tele de pequeño", "dibujos por la tarde, con mi hermano · los sábados, películas con mis padres"],
            ["qué serie", "una serie de policías española, muy famosa · tres temporadas"],
            ["idioma y subtítulos", "en español con subtítulos en español: aprendo vocabulario"],
            ["día, capítulos, cena", "el viernes por la noche · dos o tres capítulos · pizza en casa"]],
  "segunda": "Si el examinador ya ha visto la primera temporada: elegir otra serie que no conoce ninguno de los dos, o empezar por la segunda y contarle un resumen.",
  "problema": "El examinador ya ha visto la primera temporada de la serie que propone el candidato.",
  "dialogo": [
   ["E", "¡Hola! Oye, este fin de semana nos quedamos en casa, ¿no? ¿Empezamos una serie juntos?"],
   ["C", "¡Sí! A mí me encantan las series de policías y las comedias, pero las de miedo no me gustan nada. ¿Y a ti?"],
   ["E", "A mí me gusta casi todo. ¿Tú veías mucho la tele de pequeño?"],
   ["C", "Sí, por las tardes veía dibujos con mi hermano, y los sábados veíamos una película con mis padres. ¿Y tú?"],
   ["E", "Yo, sobre todo dibujos. ¿Y qué serie vemos?"],
   ["C", "Hay una serie española de policías muy famosa. Tiene tres temporadas. ¿La conoces?"],
   ["E", "Uy, sí... Es que la primera temporada ya la vi el año pasado...", True],
   ["C", "¡Vaya! Entonces podemos empezar por la segunda y te cuento yo un resumen de la primera. O buscamos otra que no conocemos ninguno. ¿Qué prefieres?"],
   ["E", "Mejor la segunda, así no la veo dos veces. ¿La vemos en español?"],
   ["C", "Sí, en español con subtítulos en español. Así aprendo vocabulario nuevo."],
   ["E", "Vale. ¿Qué día empezamos? ¿Y qué cenamos?"],
   ["C", "El viernes por la noche. Vemos dos o tres capítulos y pedimos una pizza. ¡Hasta el viernes!"]]}]}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (una persona importante): ¿Cuándo la vio la última vez? ¿Qué hicieron? · ¿Qué le ha enseñado esa persona?
    Opción 2 (mi barrio): ¿Qué tiendas hay cerca de su casa? · ¿Cómo va normalmente al centro desde su barrio?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (deporte en el parque): ¿Qué cree que le enseña el chico en el móvil? · ¿De quién cree que es el perro?
    Foto 2 (ver la televisión): ¿Por qué cree que la señora no entiende el mando? · ¿Qué cree que van a ver después?
  Tarea 3 — su papel: amigo/a o compañero/a de piso del candidato, SIEMPRE DE TÚ (como en las láminas de 2022).
  Vaya pauta por pauta, elija las preguntas según lo que diga el candidato, improvise con sus datos y provoque UN
  pequeño problema. Esquema para la interacción:
    Foto 1 (amigo/a · empezar un deporte juntos)
      Saludar ............. ¡Hola! ¿Al final empezamos a hacer deporte juntos? ¿Hablamos un poco?
      Deporte antes ....... ¿Qué deporte hacías de pequeño/a? ¿Y ahora haces alguno?
      Horario ............. ¿Qué horario tienes ahora? ¿Cuándo tienes tiempo libre?
      Qué deporte ......... ¿Qué deporte hacemos? ¿Por qué ese?
      PEQUEÑO PROBLEMA .... «Tengo mal la rodilla y el médico me ha dicho que no puedo correr unos meses...».
                            Espere a que proponga algo (nadar, la bici, otro deporte suave).
      Dónde ............... ¿Dónde lo hacemos? ¿En un gimnasio, en un club o al aire libre?
      Días y adiós ........ ¿Qué días vamos? ¿A qué hora? ¿Tenemos que comprar algo? · Vale, ¡hasta luego!
    Foto 2 (compañero/a de piso · empezar una serie juntos en casa)
      Saludar ............. ¡Hola! Este fin de semana nos quedamos en casa, ¿no? ¿Empezamos una serie juntos?
      Gustos .............. ¿Qué series o películas te gustan? ¿Y cuáles no?
      La tele de pequeño .. ¿Veías mucho la tele de pequeño/a? ¿Qué veías? ¿Con quién?
      Qué serie ........... ¿Qué serie vemos? ¿Por qué esa?
      PEQUEÑO PROBLEMA .... «Es que la primera temporada ya la vi el año pasado...». Espere a que proponga algo
                            (empezar por la segunda, contarle un resumen, otra serie).
      Idioma .............. ¿La vemos en español o en tu idioma? ¿Con subtítulos o sin ellos?
      Día y adiós ......... ¿Qué día empezamos? ¿Cuántos capítulos vemos? ¿Qué cenamos? · Vale, ¡hasta el viernes!
    El diálogo modelo de las dos situaciones está en la pestaña Oral del estudiante (se ve al abrir la prueba).
  Qué mirar en este modelo: tú coherente en toda la tarea 3; que no conteste solo sí o no (responde + detalle o
  porqué + pregunta); reaccionar al problema (¡Vaya!, lo siento) y proponer otra cosa (¿y si...?, ¿te va bien...?);
  el imperfecto en las pautas de cuando era pequeño/a (jugaba, veía, veíamos); en el monólogo, presente + pasado +
  planes con ir a / querer, y la pauta que se sale de la historia personal (a quién admira la gente de su país / si
  la gente conoce a sus vecinos); en la foto, las seis preguntas en orden, hay / está, estar + gerundio y
  «seguramente han...» / «van a...»."""
ERRORES = """  *Tú puede / *¿Usted quieres...? (mezcla tú / usted); *Cuando era pequeño, jugué al baloncesto todos los días
  (jugaba: costumbre); *Ayer he visto un capítulo (vi); *Me gusta mucho las series (me gustan); *Hago el deporte
  (hago deporte); *Juego fútbol (juego al fútbol); *Hay el perro al lado de la farola (el perro está... / hay un
  perro...); *La señora está muy confundido (confundida); *El chico enseña a la señora cómo usa el mando (cómo se
  usa / a usar el mando); *Conozco a mi amiga desde cinco años (desde hace cinco años); *¿Quedamos en las seis? (a
  las seis); frases sueltas sin conectores en el monólogo («y... y... y...»)."""

# ---------------- IMÁGENES: FOTOS ----------------
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "aparatos de gimnasia de un parque: una mujer y un chico joven hacen ejercicio y miran un móvil",
  "personas": "una mujer y un chico joven", "edades": "ella de unos 55 años, él de unos 25",
  "aspecto": "ella con mallas negras, una sudadera rosa y una cinta en el pelo; él con pantalón corto, camiseta gris y auriculares al cuello",
  "espacio": "exterior", "lugar": "zona de aparatos de gimnasia de un parque de una ciudad", "momento": "mañana",
  "estacion": "otoño", "tiempo": "sol suave de otoño, hojas amarillas en el suelo", "gente": "un señor mayor en otro aparato, al fondo",
  "accion": "ella pedalea en una máquina del parque y se ríe; él, a su lado, le enseña algo en el móvil",
  "fondo": "árboles con hojas amarillas, bancos, un señor mayor en otro aparato, una farola",
  "objetos": "aparatos de gimnasia, móvil, auriculares, botella de agua, mochila, toalla, bancos, farola",
  "detalle": "un perro atado a la farola los mira con cara de aburrido"},
 "oral_foto2": {"situacion": "salón de un piso: un chico enseña a una señora mayor a usar el mando de la tele",
  "personas": "una señora mayor y un chico adolescente", "edades": "ella de unos 75 años, él de unos 16",
  "aspecto": "ella con el pelo gris recogido, gafas y una rebeca azul; él con una sudadera con capucha y calcetines de colores",
  "espacio": "interior", "lugar": "salón de un piso normal, con un sofá y una tele en un mueble", "momento": "tarde",
  "estacion": "invierno", "tiempo": "luz de lámpara; fuera ya casi es de noche", "gente": "solo ellos dos",
  "accion": "ella tiene el mando en la mano y no entiende la pantalla; él le señala un botón y se ríe",
  "fondo": "una estantería con fotos de familia, una planta, una lámpara de pie y la tele con el menú de una plataforma",
  "objetos": "sofá, mando, manta, tele, bandeja, dos tazones de sopa, pan, vasos, fotos, planta, zapatillas",
  "detalle": "en la pantalla hay un menú con muchísimas películas y la señora no sabe qué botón tocar"},
 "escrita": {"situacion": "la vida de Mateo, un pianista de un pueblo de Zaragoza, en tres momentos",
  "personas": "Mateo, su abuela, los músicos de una orquesta y una niña con otros niños", "edades": "Mateo de unos 8, 22 y 36 años; la abuela de unos 70; la niña de unos 9",
  "aspecto": "Mateo de niño con jersey de rayas; de joven con camisa negra y el pelo largo; hoy con gafas y barba corta; la abuela con el pelo blanco y una bata de flores",
  "espacio": "interior y exterior", "lugar": "el salón de una casa de pueblo, el escenario de las fiestas en una plaza y un aula de una escuela de música", "momento": "tarde, noche y mañana",
  "estacion": "invierno, verano y primavera", "tiempo": "luz de casa; noche de verano con las luces del escenario; luz de día por la ventana", "gente": "la abuela; los músicos y la gente de la plaza; los niños de la escuela",
  "accion": "Mateo aprende a tocar el piano con su abuela; toca el teclado con la orquesta de las fiestas; da clase de piano a una niña",
  "fondo": "un piano viejo con fotos encima; un escenario con luces de colores y gente bailando; un aula con partituras en la pared",
  "objetos": "piano, partitura, fotos antiguas, teclado, micrófonos, luces de escenario, mochilas, atril",
  "detalle": "en la escuela de música hay una foto pequeña de la abuela encima del piano"},
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
 "M03": ["aparatos de gimnasia de un parque: una mujer y un chico joven hacen ejercicio y miran un móvil", "salón de un piso: un chico enseña a una señora mayor a usar el mando de la tele"],
 "M06": ["salón de casa: dos hermanos preparan las mochilas para la montaña", "padre e hija pintan el salón de un piso"],
 "M07": ["salón de un estudio: dos amigas buscan piso de alquiler en un portátil", "huerto urbano entre edificios: un abuelo y su nieta recogen tomates"],
}

IMG_PROMPTS = {
 "escrita": "The life of Mateo, a piano teacher from a small town in Zaragoza, Spain, in three moments. The same man in the three panels, at different ages. Panel 1 (left, 1998): a winter afternoon in the living room of an old village house, Mateo as a boy of about 8 in a striped jumper sits at an old upright piano with old family photos on top; his grandmother, a woman of about 70 with white hair and a flowered housecoat, sits next to him on the bench and points at the notes on the sheet music; warm lamp light. Panel 2 (middle, 2012): a summer night at the town festival, Mateo at about 22 with long hair and a black shirt plays an electric keyboard on an open-air stage in a village square with a small band (a singer, a drummer and a guitarist), coloured stage lights, people dancing in front of the stage. Panel 3 (right, today): a spring morning in a small classroom of a music school, Mateo at about 36 with glasses and a short beard sits next to a girl of about 9 at a piano and shows her where to put her hands; behind them, two other children wait with their school bags; sheet music pinned on the wall and a small framed photo of the grandmother on top of the piano.",
 "oral_foto1": "An outdoor exercise area with green metal fitness machines in a city park on a sunny autumn morning in Spain. A woman of about 55 with black leggings, a pink sweatshirt and a headband pedals on one of the machines and laughs. Next to her, a young man of about 25 with shorts, a grey T-shirt and headphones around his neck stands and shows her something on his mobile phone. On the ground: a bottle of water, a small backpack and a towel. In the background: an older man of about 75 doing exercise on another machine, trees with yellow leaves, yellow leaves on the ground, two wooden benches and a small dog tied to a lamp post that looks at them with a bored face.",
 "oral_foto2": "The living room of an ordinary flat in Spain on a winter Sunday afternoon, lamp light, it is almost dark outside. A woman of about 75 with grey hair in a bun, glasses and a blue cardigan sits on the sofa with a blanket on her legs, holding the TV remote control and looking at the screen with a confused face. Next to her, a teenage boy of about 16 with a hooded sweatshirt and colourful socks points at a button on the remote and laughs. On the TV screen, the menu of a streaming platform with many film covers (no readable titles). On the coffee table: a tray with two bowls of soup, bread and two glasses of water. In the background: a bookshelf with family photos, a plant, a floor lamp and a pair of slippers on the floor.",
}
IMG_NAMES = {"escrita": "M03_escrita_mateo_piano", "oral_foto1": "M03_oral_foto1_parque_deporte", "oral_foto2": "M03_oral_foto2_salon_tele_mando"}
IMG_DESC = {"escrita": "Escritura opcion 2 triptico Mateo y el piano: 1 de nino con su abuela, 2 con la orquesta de las fiestas, 3 da clase en una escuela de musica",
            "oral_foto1": "Oral foto 1 hacer deporte: una mujer y un chico en los aparatos de gimnasia de un parque, miran un movil",
            "oral_foto2": "Oral foto 2 ver la television: un chico ensenya a una senyora a usar el mando de la tele"}
CA1_DESC = {0: "Auditiva T1 ejemplo: velas / globos / platos de papel", 1: "Auditiva T1 conv 1: salon / dormitorio / pasillo",
            2: "Auditiva T1 conv 2: guantes / bufanda / gorro", 3: "Auditiva T1 conv 3: ingles / futbol / natacion",
            4: "Auditiva T1 conv 4: bombilla / pilas / cinta", 5: "Auditiva T1 conv 5: parada delante del banco / al lado de la iglesia / enfrente del mercado",
            6: "Auditiva T1 conv 6: ducha / persiana / calefaccion"}

LECTURA = [CL1, CL2, CL3, CL4]
AUDITIVA = [CA1, CA2, CA3, CA4]
