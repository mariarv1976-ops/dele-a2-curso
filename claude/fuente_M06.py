# -*- coding: utf-8 -*-
# FUENTE DEL MODELO 6 · Curso de preparación DELE A2 (Módulo 2, modelos completos)
# Nivel: "como el examen". Temas MEZCLADOS como en el examen real: cada tarea de un área distinta.
# Se construye con:  python3 build_modelo.py fuente_M06
# Todo el contenido es original. Español de España.
M = "06"
NOMBRE = "Modelo 6"
NIVEL = "como el examen"
TITLE = "Examen completo"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress
TIEMPOS = {"lectura": 60, "auditiva": 40}
REC_LABEL = "Qué vas a encontrar en este modelo"
RECORDATORIO = [
 "Un examen completo con la dificultad del DELE A2 real: lectura (60 minutos), auditiva (40 minutos), escritura (45 minutos) y, en clase con tu profesora, la oral.",
 "Como en el examen, cada tarea habla de un tema distinto: la vida con un animal, anuncios de la ciudad, voluntariado, un autobús biblioteca, compras, el tiempo, la tecnología, un trabajo de verano, un viaje a la montaña y pintar la casa.",
 "Los textos están en la parte alta de la extensión oficial y las opciones falsas son finas: la información aparece, pero es de otra persona, de otro día o es un plan que cambia.",
 "Al terminar, en Resultados ves tu nota de cada grupo (lectura + escritura; auditiva + oral), si estás listo para presentarte, qué fichas repasar y tu control de progreso.",
]
TIPS_INICIO = [
 "<b>Reparte el tiempo de la lectura:</b> unos 12 minutos para la tarea 1, 15 para la 2, 15 para la 3 y 18 para la 4. Si una pregunta te bloquea, marca una opción y sigue: los errores no restan.",
 "<b>Cuidado con las trampas finas:</b> muchas opciones dicen algo que aparece en el texto, pero de otra persona, de otro momento o un plan que al final no se hace. Busca siempre quién, cuándo y si al final pasó.",
 "<b>Al terminar cada prueba, apunta cuánto has tardado en cada tarea y qué te ha costado:</b> lo vas a necesitar en el control de progreso de Resultados.",
]

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
  "repaso": "El indefinido cuenta lo que pasó y terminó (adopté, fui, se rompió); el imperfecto describe cómo era o qué hacía normalmente (antes me levantaba, estaba nervioso); el perfecto habla de un tiempo que todavía no ha terminado (este mes he leído, he conocido). En las preguntas, fíjate en el marcador: antes, ahora, el primer día, desde entonces.",
  "reto": "Escribe tres frases sobre un cambio en tu vida: cómo era antes (imperfecto), qué pasó (indefinido) y qué has hecho este año (perfecto).",
  "fichas": F("R01")},
 "planes": {"name": "Planes, propuestas y cambios de plan (pensaba..., al final..., ¿y si...?)",
  "repaso": "En el examen, la persona dice primero lo que pensaba hacer y después lo que hace de verdad: «primero pensaba dejarlo en una residencia, pero...», «iba a llevar vino, pero al final...». La respuesta buena es siempre la última decisión. Para proponer: ¿y si...?, podemos..., ¿te va bien el jueves?",
  "reto": "Escribe un mensaje a un amigo con un plan que cambia: «Iba a..., pero al final...».",
  "fichas": F("R01", "M4-3", "R13", "R08", "R14b")},
 "normas": {"name": "Normas y condiciones en anuncios y avisos (hay que, no hace falta, solo, excepto)",
  "repaso": "En los anuncios, las palabras pequeñas lo cambian todo: hay que / es obligatorio (obligación), no hace falta (no es obligatorio), solo, excepto, como máximo, gratis, se paga aparte. Lee la pregunta y busca solo esa condición en el texto.",
  "reto": "Escribe un aviso para la piscina de tu barrio con tres condiciones: algo obligatorio, algo que no hace falta y algo que solo se puede hacer un día.",
  "fichas": F("M0", "R14b")},
 "tiempo": {"name": "Horas, fechas, horarios y duración (a las, de... a, desde hace, durante, en)",
  "repaso": "A las + hora; de... a... / desde... hasta... para horarios; por la mañana / tarde / noche; hace + tiempo para el pasado; desde hace + tiempo para algo que sigue hoy; durante para un periodo cerrado. En la auditiva, las horas y los días parecidos son la trampa más frecuente.",
  "reto": "Escribe tu horario de la semana con cinco frases: a las..., de... a..., por la tarde, desde hace..., durante...",
  "fichas": F("R06", "R14b")},
 "lugares": {"name": "Lugares y localización (hay, está, en, a, por, al lado de)",
  "repaso": "Hay presenta algo nuevo (hay un aparcamiento nuevo); está sitúa algo que ya conocemos (el aparcamiento está al lado de la estación). Ir a + lugar, estar en + lugar, pasar por + zona. Cuidado: el examen cambia a menudo el lugar (en el centro / al lado de la estación).",
  "reto": "Describe en cuatro frases dónde están las cosas importantes de tu barrio: hay..., está..., al lado de..., enfrente de...",
  "fichas": F("R02", "R06", "R14a")},
 "cantidad": {"name": "Precios, descuentos y cantidades (gratis, un 20 %, la mitad, muy, mucho)",
  "repaso": "Gratis / gratuito = no se paga; un veinte por ciento de descuento; dos por el precio de uno; la mitad; más de / menos de. Muy va con adjetivos (muy caro); mucho, con nombres y verbos (mucha gente, cuesta mucho). En los anuncios, mira a quién se aplica el descuento y cuándo.",
  "reto": "Escribe un anuncio de una tienda con tres ofertas: algo gratis, un descuento y una condición.",
  "fichas": F("R05", "R14a")},
 "personas": {"name": "Quién hace qué: personas, relaciones y trato (su hermana, tú / usted)",
  "repaso": "Muchas opciones falsas cuentan lo que hace otra persona: la hermana, el vecino, el médico. Fíjate en los posesivos (su marido, sus hijos) y en el trato: en un correo formal y en un servicio se habla de usted del saludo a la despedida.",
  "reto": "Escribe dos frases sobre lo que haces tú y dos sobre lo que hace una persona de tu familia, con posesivos (mi, su, nuestro).",
  "fichas": F("R04", "R07", "R10", "R14a")},
 "opinion": {"name": "Gustos, opiniones y sentimientos (me encanta, me cuesta, estoy nervioso)",
  "repaso": "Me gusta / me encanta / me cuesta + infinitivo; estar + nervioso, cansado, contento; para mí, creo que. Para reaccionar: a mí también / a mí tampoco. En la auditiva, la emoción o la opinión suele ser de una sola de las dos personas: escucha quién lo dice.",
  "reto": "Escribe tres frases sobre algo que te cuesta, algo que te encanta y algo que te pone nervioso, y reacciona a la frase «No me gusta madrugar».",
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
 "instr": "Usted va a leer el correo electrónico que Claudia ha escrito a su amigo Hugo. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Claudia compara su vida antes y ahora, cuenta un problema y al final pide algo: busca en qué parte del correo está cada pregunta.",
 "head": ["De: Claudia", "Para: Hugo", "Asunto: ¡Tengo compañero de piso nuevo!"],
 "body": [
  "Hola, Hugo:",
  "¿Qué tal por Zaragoza? ¿Ya has terminado la mudanza? Yo tengo una noticia: ¡tengo compañero de piso nuevo! Se llama Tango, tiene tres años, cuatro patas y mucho pelo. Sí, por fin he adoptado un perro. Lo encontré hace un mes en la protectora de animales de mi barrio. Mi hermana quería un cachorro, pero yo prefería un perro adulto y tranquilo, y Tango es perfecto.",
  "Mi vida ha cambiado bastante. Antes me levantaba a las ocho y media y salía corriendo a la oficina. Ahora me levanto a las siete, porque Tango tiene que pasear antes de mi trabajo. Al principio me costaba mucho, pero ahora me encanta: el parque a esa hora está muy tranquilo y he conocido a muchos vecinos. Antes no hablaba con nadie del edificio; ahora conozco a la señora del tercero, a un chico que trabaja en el hospital y, claro, a sus perros.",
  "El primer fin de semana fue un desastre. El sábado fui al supermercado y dejé a Tango solo en casa una hora. Cuando volví, ¡el sofá estaba lleno de trozos de cojín! No me enfadé mucho: el pobre estaba nervioso en una casa nueva. Ahora, cuando salgo, le dejo la radio puesta y un juguete, y no rompe nada.",
  "Y ahora te pido un favor. En el puente de diciembre voy a Lisboa con unas amigas. Primero pensaba dejar a Tango en una residencia canina, pero son muy caras y él no conoce a nadie allí. Tú tienes jardín y te encantan los perros... ¿Puedes cuidarlo esos cuatro días? Yo te lo llevo el jueves por la tarde con su comida y su cama.",
  "Un abrazo,<br>Claudia"],
 "items": [
  {"n": 1, "q": "Claudia escribe a Hugo para...", "o": ["contarle que va a compartir piso con otra persona.", "contarle un cambio en su vida y pedirle ayuda.", "invitarle a pasar unos días en Lisboa."], "ok": 1,
   "cats": ["pasados", "planes"], "es": "ES-02", "pc": "FN contar novedades · pedir un favor (¿puedes...?)",
   "why": "Claudia le cuenta que ha adoptado un perro y le pide que lo cuide. El «compañero de piso» es el perro, no una persona, y a Lisboa va con unas amigas, no con Hugo."},
  {"n": 2, "q": "Claudia eligió a Tango porque...", "o": ["era el perro favorito de su hermana.", "era un cachorro muy tranquilo.", "no quería un perro muy joven."], "ok": 2,
   "cats": ["personas"], "es": "ES-08", "pc": "prefería (imperfecto) · quería un cachorro (su hermana)",
   "why": "Claudia prefería un perro adulto: no quería un cachorro. El cachorro lo quería su hermana, no ella."},
  {"n": 3, "q": "Desde que tiene a Tango, Claudia...", "o": ["habla con más gente de su barrio.", "llega más tarde a la oficina.", "pasea por el parque por la tarde."], "ok": 0,
   "cats": ["pasados"], "es": "ES-03", "pc": "antes + imperfecto / ahora + perfecto (he conocido)",
   "why": "Antes no hablaba con nadie del edificio y ahora conoce a muchos vecinos. Se levanta antes, no llega más tarde, y pasea con Tango por la mañana, antes del trabajo."},
  {"n": 4, "q": "El primer fin de semana...", "o": ["Tango estropeó algo de la casa.", "Claudia se enfadó mucho con Tango.", "Tango estuvo solo casi todo el día."], "ok": 0,
   "cats": ["pasados", "opinion"], "es": "ES-03", "pc": "indefinido (fui, dejé, volví) + imperfecto (estaba lleno, estaba nervioso)",
   "why": "Cuando Claudia volvió, el sofá estaba lleno de trozos de cojín: Tango rompió algo. Claudia no se enfadó mucho, y Tango estuvo solo una hora, no todo el día."},
  {"n": 5, "q": "Claudia le propone a Hugo...", "o": ["ir con ella a Lisboa en diciembre.", "buscar una residencia para el perro.", "tener al perro en su casa unos días."], "ok": 2,
   "cats": ["planes"], "es": "ES-05", "pc": "primero pensaba..., pero · ¿puedes cuidarlo?",
   "why": "Le pide que cuide a Tango cuatro días en su casa. La residencia era su primera idea, pero la descartó porque son caras."},
 ]}

CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 15 minutos: menos de dos minutos por anuncio. Lee la pregunta primero y busca solo ese dato. Cuidado con las palabras que limitan o niegan: solo, excepto, no hace falta, es obligatorio, se paga aparte.",
 "example": {"title": "INSTITUTO LUIS VIVES · MERCADILLO SOLIDARIO",
   "body": "El domingo 23, de 10:00 a 14:00, en el patio del instituto. Los alumnos de bachillerato venden libros, ropa y juguetes de segunda mano. Todo el dinero es para el comedor social del barrio. ¿Tienes cosas en buen estado que ya no usas? Tráelas a la conserjería antes del viernes. ¡Gracias por ayudar!",
   "q": "En el mercadillo...", "o": ["venden cosas nuevas.", "el dinero es para una organización del barrio.", "se puede comprar todo el fin de semana."], "ok": 1,
   "why": "La opción correcta es la B porque todo el dinero es para el comedor social del barrio."},
 "items": [
  {"n": 6, "title": "PISCINA MUNICIPAL EL PINAR · HORARIO DE INVIERNO",
   "body": "Desde el 1 de octubre, la piscina cubierta abre de lunes a viernes, de 7:00 a 22:00, y los sábados, de 9:00 a 14:00. Los domingos está cerrada. Para el baño libre no hace falta reservar, pero en las clases de natación las plazas son limitadas: apúntate en la recepción. Es obligatorio usar gorro y chanclas.",
   "q": "En esta piscina...", "o": ["se puede nadar los domingos por la mañana.", "hay que inscribirse para las clases.", "es obligatorio reservar para nadar."], "ok": 1,
   "cats": ["normas", "tiempo"], "es": "ES-06", "pc": "no hace falta / es obligatorio · de lunes a viernes",
   "why": "Las plazas de las clases son limitadas y hay que apuntarse en la recepción. Los domingos está cerrada, y para el baño libre no hace falta reservar."},
  {"n": 7, "title": "COMUNIDAD DE VECINOS · CALLE ALMENDROS, 14 · AVISO",
   "body": "El martes 12, de 9:00 a 13:00, no hay agua en todo el edificio por unas obras en la calle. Les recomendamos guardar agua el lunes por la noche. El ascensor funciona con normalidad. Si tienen alguna pregunta, pueden llamar al presidente de la comunidad, Julián (2.º B), por la tarde.",
   "q": "Según el aviso, el martes por la mañana los vecinos...", "o": ["no van a poder usar el agua.", "no van a poder usar el ascensor.", "tienen que llamar a Julián."], "ok": 0,
   "cats": ["normas", "tiempo"], "es": "ES-07", "pc": "de 9:00 a 13:00 · funciona con normalidad",
   "why": "De nueve a una no hay agua en el edificio. El ascensor funciona, y a Julián solo hay que llamarlo si tienen preguntas, y por la tarde."},
  {"n": 8, "title": "BICIS DE LA CIUDAD · NUEVO SERVICIO",
   "body": "Más de 50 estaciones en toda la ciudad. Con el abono anual (25 €), los primeros 30 minutos de cada viaje son gratis; después, 50 céntimos cada media hora. Puedes coger la bici en una estación y dejarla en otra. Para darte de alta solo necesitas el móvil: descarga la aplicación. Menores de 16 años, solo con un adulto.",
   "q": "Con el abono anual...", "o": ["todos los viajes son gratis.", "hay que dejar la bici en la misma estación.", "la primera media hora no se paga."], "ok": 2,
   "cats": ["cantidad", "normas"], "es": "ES-03", "pc": "gratis = no se paga · los primeros 30 minutos",
   "why": "Los primeros treinta minutos de cada viaje son gratis: la primera media hora no se paga. Después sí se paga, y la bici se puede dejar en otra estación."},
  {"n": 9, "title": "FORO «APRENDER A NADAR DE MAYOR»",
   "body": "Respuesta de Mamen_51:<br>Yo aprendí a nadar el año pasado, con cincuenta años. Siempre me daba vergüenza ir a la piscina con niños, pero encontré un curso solo para adultos en el polideportivo de mi barrio. Al principio iba con miedo: ¡no quería quitar el pie del suelo! El profesor tenía muchísima paciencia. Ahora nado tres días a la semana y mi hija, que nada fatal, quiere venir conmigo.",
   "q": "Mamen cuenta que...", "o": ["aprendió a nadar en un grupo de niños.", "ya nada con su hija varios días a la semana.", "al principio tenía miedo en el agua."], "ok": 2,
   "cats": ["pasados", "opinion"], "es": "ES-07", "pc": "al principio + imperfecto (iba con miedo) · quiere venir (plan)",
   "why": "Al principio iba con miedo y no quería quitar el pie del suelo. Su curso era solo para adultos, y su hija todavía no nada con ella: solo quiere ir."},
  {"n": 10, "title": "BIBLIOTECA SAN ANTÓN · TALLER «ARREGLA TU MÓVIL»",
   "body": "¿Se te ha roto la pantalla? ¿La batería dura muy poco? En la biblioteca aprendemos a hacer pequeñas reparaciones en casa. Taller gratuito, el jueves 7, de 18:00 a 20:00. Trae tu móvil y su cargador. Las piezas nuevas no están incluidas: si necesitas una, el profesor te dice dónde comprarla. Plazas limitadas: inscripción en la biblioteca.",
   "q": "En este taller...", "o": ["hay que llevar el propio teléfono.", "las piezas nuevas son gratis.", "el profesor arregla los móviles de los participantes."], "ok": 0,
   "cats": ["normas", "cantidad"], "es": "ES-04", "pc": "trae tu móvil · no están incluidas · aprendemos a",
   "why": "Hay que traer el móvil y su cargador. El taller es gratis, pero las piezas no están incluidas, y los participantes aprenden a repararlo ellos: el profesor no lo arregla."},
  {"n": 11, "title": "NOTICIAS · VILLAFRÍA CIERRA SU CENTRO A LOS COCHES",
   "body": "Desde el 1 de noviembre, los coches no pueden entrar en el centro histórico de Villafría. Solo pueden pasar los vecinos que viven allí, los taxis y las ambulancias. El ayuntamiento ha abierto un aparcamiento gratuito al lado de la estación de autobuses, a cinco minutos andando de la plaza Mayor. Las tiendas del centro creen que van a tener más clientes.",
   "q": "Según la noticia, en el centro de Villafría...", "o": ["no puede entrar ningún coche.", "los vecinos del centro pueden entrar con su coche.", "hay un aparcamiento nuevo gratuito."], "ok": 1,
   "cats": ["lugares", "normas"], "es": "ES-06", "pc": "solo pueden pasar · al lado de la estación",
   "why": "Los vecinos que viven en el centro pueden pasar con su coche. Sí entran algunos coches (taxis, ambulancias), y el aparcamiento nuevo está al lado de la estación, no en el centro."},
  {"n": 12, "title": "AUTOBÚS DE DONACIÓN DE SANGRE",
   "body": "El viernes 15, el autobús de donación de sangre está en la plaza del Mercado, de 10:00 a 14:00 y de 17:00 a 21:00. Pueden donar personas de 18 a 65 años que pesan más de 50 kilos. Es necesario traer el DNI. No hace falta venir sin desayunar: es mejor comer algo antes. La donación dura unos diez minutos.",
   "q": "Para donar sangre...", "o": ["hay que llevar un documento de identidad.", "no se puede desayunar antes.", "hay que pedir cita antes."], "ok": 0,
   "cats": ["normas"], "es": "ES-06", "pc": "es necesario · no hace falta + infinitivo",
   "why": "Es necesario traer el DNI. Es mejor comer algo antes, y el anuncio no habla de pedir cita."},
  {"n": 13, "title": "FRUTERÍA LAS DELICIAS · AHORA TE LLEVAMOS LA COMPRA",
   "body": "Haz tu pedido por teléfono o por WhatsApp antes de las 12:00 y lo recibes en casa el mismo día por la tarde. El servicio es gratis para compras de más de 30 €; si no, cuesta 3 €. Solo repartimos en el barrio. Puedes pagar con tarjeta o en efectivo cuando llega el pedido.",
   "q": "En esta frutería...", "o": ["el reparto siempre es gratis.", "hay que pagar el pedido al hacerlo.", "si pides por la mañana, te llega ese día."], "ok": 2,
   "cats": ["cantidad", "tiempo"], "es": "ES-03", "pc": "antes de las 12:00 · gratis para compras de más de · cuando llega",
   "why": "Si haces el pedido antes de las doce, lo recibes esa tarde. El reparto solo es gratis para compras de más de treinta euros, y se paga cuando llega el pedido."},
 ]}

CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos de tres personas que hablan de su experiencia como voluntarios. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 15 minutos. Lee primero las seis preguntas. Las tres personas hacen algo parecido: busca el detalle que las separa (con quién va, cuándo, por qué empezó, qué quiere hacer).",
 "texts": [
  {"name": "Rocío", "body": "Soy voluntaria en el banco de alimentos de mi ciudad desde hace dos años. Voy los sábados por la mañana: clasificamos la comida que traen los supermercados y preparamos cajas para las familias. Empecé porque una compañera de trabajo me lo propuso, y ahora vamos juntas. Es un trabajo físico y a veces terminas cansada, pero el ambiente es muy bueno: hay estudiantes, jubilados, familias con niños... En Navidad hay muchísimo trabajo y siempre buscamos más gente. Lo que más me gusta es que en pocas horas ves el resultado: decenas de cajas listas para salir. Mi marido dice que paso más tiempo allí que en casa."},
  {"name": "Alberto", "body": "Hace un año me apunté a un programa del ayuntamiento para acompañar a personas mayores que viven solas. Me presentaron a Pepe, un señor de ochenta y seis años que vive en mi calle. Los martes por la tarde voy a su casa: tomamos un café, jugamos a las cartas y a veces lo acompaño al médico. Al principio era un poco tímido y casi no hablaba, pero ahora me cuenta historias de cuando era camionero y viajaba por toda Europa. Yo trabajo desde casa y antes pasaba muchos días sin hablar con nadie. La verdad es que Pepe me ayuda a mí tanto como yo a él."},
  {"name": "Nuria", "body": "Vivo en Alicante y desde el verano pasado participo en las limpiezas de playas de una asociación. Las hacemos un domingo al mes a primera hora de la mañana, cuando todavía no hay bañistas. Recogemos plásticos, latas y, sobre todo, colillas: el mes pasado recogimos más de dos mil. No hace falta experiencia ni material, porque la asociación da los guantes y las bolsas. Al principio iba sola, pero luego convencí a mis dos hijos adolescentes y ahora vienen siempre conmigo. Después, desayunamos todos juntos en un chiringuito. Me gustaría organizar también limpiezas en el río, pero todavía no hemos encontrado gente."}],
 "items": [
  {"n": 14, "q": "¿Quién empezó a colaborar gracias a la idea de otra persona?", "ok": 0, "cats": ["personas", "pasados"], "es": "ES-08", "pc": "empecé porque... me lo propuso",
   "why": "Rocío empezó porque una compañera de trabajo se lo propuso. Nuria convenció a sus hijos: la idea fue suya."},
  {"n": 15, "q": "¿Quién hace la actividad con personas de su familia?", "ok": 2, "cats": ["personas"], "es": "ES-09", "pc": "sus hijos vienen siempre conmigo",
   "why": "Los hijos de Nuria van siempre con ella. Rocío habla de su marido, pero él no va: dice que ella pasa mucho tiempo allí."},
  {"n": 16, "q": "¿Quién ayuda siempre a la misma persona?", "ok": 1, "cats": ["personas"], "es": "ES-03", "pc": "me presentaron a Pepe · los martes voy a su casa",
   "why": "Alberto acompaña a Pepe todos los martes. Rocío y Nuria ayudan a muchas personas o al medio ambiente."},
  {"n": 17, "q": "¿Quién dice que su actividad le ayuda a no sentirse solo?", "ok": 1, "cats": ["opinion", "pasados"], "es": "ES-03", "pc": "antes pasaba muchos días sin hablar con nadie · me ayuda a mí",
   "why": "Alberto trabaja desde casa y antes pasaba días sin hablar con nadie; dice que Pepe también le ayuda a él."},
  {"n": 18, "q": "¿Quién dice que en algunas épocas del año hace falta más ayuda?", "ok": 0, "cats": ["tiempo"], "es": "ES-09", "pc": "en Navidad hay muchísimo trabajo",
   "why": "Rocío dice que en Navidad hay muchísimo trabajo y buscan más gente. Nuria también busca gente, pero para un proyecto nuevo, no para una época del año."},
  {"n": 19, "q": "¿Quién tiene un plan que todavía no ha empezado?", "ok": 2, "cats": ["planes"], "es": "ES-07", "pc": "me gustaría + infinitivo · todavía no",
   "why": "A Nuria le gustaría organizar limpiezas en el río, pero todavía no han encontrado gente."}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un reportaje sobre una bibliotecaria que trabaja en un autobús. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto: cada párrafo responde, más o menos, a una pregunta. Atención a lo que pasó antes, a lo que pasa ahora y a lo que Rosa quiere hacer.",
 "title": "Rosa y la biblioteca que viaja",
 "sub": "Revista «Vivir en el pueblo» · Reportaje",
 "body": [
  "Cada dos miércoles, a las diez en punto, un autobús azul aparca en la plaza de Valdecuervos, un pueblo de ciento veinte habitantes en la sierra de Albarracín. No es un autobús normal: dentro hay más de tres mil libros, revistas, películas y dos ordenadores con internet. Es el bibliobús de la comarca, y su conductora y bibliotecaria es Rosa Lahoz, de cuarenta y siete años.",
  "Rosa estudió Historia en Zaragoza y trabajó doce años en la biblioteca de la universidad. «Me gustaba mi trabajo, pero no me gustaba vivir en la ciudad», explica. En 2016 vio un anuncio en el periódico: la comarca buscaba una bibliotecaria con carné de conducir autobuses. Ella no tenía ese carné, pero se apuntó a una autoescuela y lo consiguió en tres meses. «Mi familia pensaba que estaba loca», recuerda riéndose.",
  "Hoy visita catorce pueblos cada quince días. En algunos no hay tienda ni bar, y el bibliobús es también un lugar para encontrarse. «La gente no viene solo a buscar libros: viene a charlar, a pedirme ayuda con el móvil o a imprimir un documento del banco», cuenta. Sus lectores más fieles son las personas mayores y los niños de las escuelas pequeñas. Por la tarde, cuando termina la ruta, vuelve a Teruel y deja el autobús en el garaje de la comarca.",
  "El invierno más difícil fue el de 2021. Una gran nevada dejó las carreteras cerradas durante casi dos semanas y el bibliobús no pudo salir. Rosa no quería dejar a sus lectores sin libros, así que preparó bolsas con novelas y periódicos, y unos vecinos con tractor las llevaron a los pueblos. «Fue una cadena de favores preciosa», dice.",
  "Su lector favorito se llama Eusebio y tiene noventa años. Durante toda su vida trabajó en el campo y casi no leía. Hace tres años le pidió a Rosa «un libro fácil, con letra grande». Desde entonces ha leído más de sesenta novelas, sobre todo del oeste. El año pasado, en su cumpleaños, los vecinos le regalaron un carné de lector de oro.",
  "Ahora Rosa tiene un nuevo proyecto: un club de lectura por videollamada para lectores de pueblos diferentes. «Muchos no tienen coche y no pueden reunirse», explica. Todavía está buscando ordenadores para los vecinos que no tienen. Y no piensa volver a la ciudad: «Aquí he encontrado mi sitio»."],
 "items": [
  {"n": 20, "q": "Según el texto, el bibliobús...", "o": ["solo lleva libros y revistas.", "tiene también aparatos para conectarse a internet.", "visita Valdecuervos todas las semanas."], "ok": 1,
   "cats": ["lugares"], "es": "ES-03", "pc": "dentro hay... dos ordenadores con internet · cada dos miércoles",
   "why": "Dentro hay dos ordenadores con internet. También lleva películas, y va a Valdecuervos cada dos miércoles, no todas las semanas."},
  {"n": 21, "q": "Para conseguir este trabajo, Rosa...", "o": ["sacó un carné nuevo en pocos meses.", "tuvo que mudarse a Zaragoza.", "respondió a un anuncio de la universidad."], "ok": 0,
   "cats": ["pasados", "tiempo"], "es": "ES-11", "pc": "indefinido (vio, se apuntó, consiguió) · en tres meses",
   "why": "Se apuntó a una autoescuela y consiguió el carné de autobús en tres meses. Ya vivía en Zaragoza, y el anuncio era de la comarca, no de la universidad."},
  {"n": 22, "q": "En algunos pueblos, el bibliobús...", "o": ["es la única tienda que hay.", "lo usan sobre todo los jóvenes.", "sirve para hacer gestiones y hablar con los vecinos."], "ok": 2,
   "cats": ["lugares", "personas"], "es": "ES-03", "pc": "no hay tienda ni bar · viene a charlar, a imprimir un documento",
   "why": "La gente va a charlar, a pedir ayuda con el móvil o a imprimir documentos del banco. No es una tienda, y sus lectores más fieles son los mayores y los niños."},
  {"n": 23, "q": "Durante la nevada de 2021...", "o": ["el bibliobús repartió los libros en un tractor.", "los libros llegaron a los pueblos gracias a los vecinos.", "Rosa no pudo salir de su casa en dos semanas."], "ok": 1,
   "cats": ["pasados", "personas"], "es": "ES-08", "pc": "unos vecinos con tractor las llevaron",
   "why": "Rosa preparó las bolsas y unos vecinos las llevaron en tractor. El bibliobús no pudo salir, y lo que estuvo cerrado fueron las carreteras, no la casa de Rosa."},
  {"n": 24, "q": "Eusebio...", "o": ["empezó a leer mucho de mayor.", "trabajó en una biblioteca de la zona.", "prefiere los libros con muchas fotos."], "ok": 0,
   "cats": ["pasados", "tiempo"], "es": "ES-07", "pc": "casi no leía (imperfecto) · desde entonces ha leído (perfecto)",
   "why": "Casi no leía en su vida y, desde hace tres años, ha leído más de sesenta novelas. Trabajó en el campo, y pidió libros con letra grande, no con fotos."},
  {"n": 25, "q": "Ahora Rosa quiere...", "o": ["volver a vivir en la ciudad.", "comprar un coche para la biblioteca.", "reunir a lectores que viven lejos."], "ok": 2,
   "cats": ["planes"], "es": "ES-07", "pc": "un nuevo proyecto · no piensa volver",
   "why": "Quiere crear un club de lectura por videollamada para lectores de pueblos distintos. No piensa volver a la ciudad, y los que no tienen coche son los vecinos."},
 ]}

# ---------------- AUDITIVA ----------------
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación: las tres aparecen. En casi todas, la primera idea no es la buena: alguien cambia de plan o dice que no. Espera al final.",
 "example": {"q": "¿Qué se ha dejado el chico en casa de su abuela?", "o": ["unas gafas de sol", "una bufanda", "un cargador"], "ok": 2,
   "pres": "Va a escuchar a un chico que habla por teléfono con su abuela.",
   "lines": [("Hombre", "DANI", "Abuela, soy Pablo. Oye, ¿me he dejado las gafas de sol en tu casa?"),
             ("Mujer", "NIEVE", "No, hijo, las gafas las llevabas puestas. Aquí hay una bufanda... Ah, no, esa es de tu primo."),
             ("Hombre", "DANI", "¿Entonces qué tienes?"),
             ("Mujer", "NIEVE", "Tu cargador del móvil. Estaba en el enchufe de la cocina."),
             ("Hombre", "DANI", "¡Por eso no tengo batería! Mañana paso a buscarlo.")],
   "solucion": "La opción correcta es la letra ce. Se ha dejado el cargador.",
   "img": "M06_CA1_0_gafas_bufanda_cargador.jpg",
   "prompt": "Panel 1: a pair of sunglasses. Panel 2: a knitted scarf. Panel 3: a phone charger with its cable."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Qué va a llevar la mujer a la cena?", "o": ["una tarta", "una botella de vino", "una ensalada"], "ok": 2,
   "cats": ["planes"], "es": "ES-05", "pc": "iba a llevar..., pero · voy a hacer",
   "pres": "Va a escuchar a dos amigas que hablan de una cena en casa de un amigo.",
   "lines": [("Mujer", "FIONA", "Oye, Marta, para la cena del sábado en casa de Javi, ¿qué llevas? ¿Vino?"),
             ("Mujer", "LYDIA", "Iba a llevar vino, pero Javi ya ha comprado tres botellas."),
             ("Mujer", "FIONA", "Pues lleva una tarta, ¿no? Te salen muy ricas."),
             ("Mujer", "LYDIA", "La tarta la hace su hermana. Yo voy a hacer una ensalada de pasta, que es fácil."),
             ("Mujer", "FIONA", "¡Genial! Entonces yo llevo pan y queso.")],
   "why": "Al final va a hacer una ensalada de pasta. El vino ya lo ha comprado Javi y la tarta la hace su hermana.",
   "img": "M06_CA1_1_tarta_vino_ensalada.jpg", "prompt": "Panel 1: a homemade cake on a plate. Panel 2: a bottle of red wine. Panel 3: a big bowl of pasta salad."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Dónde quedan los dos amigos?", "o": ["en la puerta del cine", "en una cafetería", "en la estación de metro"], "ok": 0,
   "cats": ["lugares", "planes"], "es": "ES-05", "pc": "¿y si quedamos...? · mejor directamente en...",
   "pres": "Va a escuchar a dos amigos que quedan para ir al cine.",
   "lines": [("Hombre", "OSCAR", "Entonces, ¿quedamos en el metro a las siete?"),
             ("Mujer", "SARA_JOVEN", "Uf, en el metro hay muchísima gente a esa hora. ¿Y si quedamos en la cafetería de la esquina?"),
             ("Hombre", "OSCAR", "Los martes está cerrada. Mejor directamente en la puerta del cine, que es más fácil."),
             ("Mujer", "SARA_JOVEN", "Vale, en la puerta. Y si llego tarde, te mando un mensaje."),
             ("Hombre", "OSCAR", "Perfecto. Las entradas las compro yo.")],
   "why": "Quedan en la puerta del cine. En el metro hay mucha gente, y la cafetería está cerrada los martes.",
   "img": "M06_CA1_2_cine_cafeteria_metro.jpg", "prompt": "Panel 1: the entrance of a cinema with film posters without text. Panel 2: a small corner café with tables. Panel 3: the entrance of a metro station with stairs going down."},
  {"n": 3, "conv": "Conversación tres", "q": "¿Qué tiempo va a hacer el sábado en la sierra?", "o": ["sol", "lluvia", "nieve"], "ok": 1,
   "cats": ["tiempo"], "es": "ES-07", "pc": "hoy y mañana / el sábado / el domingo · va a llover",
   "pres": "Va a escuchar a dos amigos que quieren ir a la sierra.",
   "lines": [("Mujer", "AITANA", "¿Has visto el tiempo para el sábado? Quería subir a la sierra."),
             ("Hombre", "DANIEL_ES", "Sí. Hoy y mañana hace sol, pero el sábado va a llover toda la tarde."),
             ("Mujer", "AITANA", "¿Y nieve? En noviembre a veces nieva allí arriba."),
             ("Hombre", "DANIEL_ES", "No, todavía no hace tanto frío. Nieve, no. Agua, mucha."),
             ("Mujer", "AITANA", "Bueno, pues vamos el domingo, que vuelve a salir el sol.")],
   "why": "El sábado va a llover toda la tarde. Hace sol hoy, mañana y el domingo, y no va a nevar.",
   "img": "M06_CA1_3_sol_lluvia_nieve.jpg", "prompt": "Panel 1: a sunny mountain landscape with a bright sun. Panel 2: a mountain landscape with dark clouds and rain. Panel 3: a snowy mountain landscape with snowflakes."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Qué le compra el chico a su madre?", "o": ["un libro", "un pañuelo", "unos pendientes"], "ok": 2,
   "cats": ["personas", "cantidad"], "es": "ES-05", "pc": "había pensado en..., pero · me los llevo",
   "pres": "Va a escuchar a un chico que habla con una dependienta en una tienda.",
   "lines": [("Mujer", "ANA_MARIA", "Hola, buenas tardes. ¿Le puedo ayudar?"),
             ("Hombre", "VOLU", "Sí, busco un regalo para mi madre, que es su cumpleaños. Había pensado en un libro, pero ya tiene muchísimos."),
             ("Mujer", "ANA_MARIA", "¿Y un pañuelo de seda? Estos son de la colección nueva."),
             ("Hombre", "VOLU", "Es bonito, pero ella casi nunca lleva pañuelos. ¿Y esos pendientes de plata?"),
             ("Mujer", "ANA_MARIA", "Treinta y cinco euros. Si quiere, se los envuelvo para regalo."),
             ("Hombre", "VOLU", "Sí, por favor. Me los llevo.")],
   "why": "Se lleva los pendientes de plata. El libro no, porque su madre ya tiene muchos, y el pañuelo tampoco, porque casi nunca lleva.",
   "img": "M06_CA1_4_libro_panuelo_pendientes.jpg", "prompt": "Panel 1: a hardback book. Panel 2: a folded silk scarf. Panel 3: a pair of silver earrings in a small box."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿A qué actividad van a apuntar a la niña?", "o": ["a teatro", "a natación", "a música"], "ok": 0,
   "cats": ["planes", "tiempo"], "es": "ES-05", "pc": "ella quería... · está llena · pues teatro",
   "pres": "Va a escuchar a una madre y a un padre que hablan de su hija.",
   "lines": [("Mujer", "SARA_2", "¿Al final a qué apuntamos a Lucía? Ella quería natación."),
             ("Hombre", "AGUSTIN", "Las clases de natación son a las cinco, y ese día yo salgo tarde del trabajo."),
             ("Mujer", "SARA_2", "¿Y música? La escuela está al lado de casa."),
             ("Hombre", "AGUSTIN", "La de música está llena hasta enero. Me han dicho que el teatro del colegio tiene plazas los jueves."),
             ("Mujer", "SARA_2", "Pues teatro. Le va a encantar, es muy habladora.")],
   "why": "Al final la apuntan a teatro, los jueves. A la niña le gustaba la natación, pero no les va bien la hora, y la escuela de música está llena.",
   "img": "M06_CA1_5_teatro_natacion_musica.jpg", "prompt": "Panel 1: children acting on a small school stage. Panel 2: a child swimming in a pool. Panel 3: a child playing the piano."},
  {"n": 6, "conv": "Conversación seis", "q": "¿Cómo va a ir el hombre al aeropuerto?", "o": ["en el coche de su hermano", "en taxi", "en tren"], "ok": 1,
   "cats": ["planes", "tiempo"], "es": "ES-05", "pc": "me iba a llevar, pero · demasiado tarde · ya lo he reservado",
   "pres": "Va a escuchar a un hombre y a una mujer que hablan de un viaje.",
   "lines": [("Mujer", "TATIANA", "¿A qué hora sale tu vuelo mañana?"),
             ("Hombre", "RAFA", "A las siete de la mañana. Mi hermano me iba a llevar en coche, pero ahora tiene una reunión."),
             ("Mujer", "TATIANA", "¿Y el tren? Hay uno que va directo a la terminal."),
             ("Hombre", "RAFA", "El primero sale a las seis: demasiado tarde. Voy a llamar a un taxi. Bueno, ya lo he reservado para las cinco."),
             ("Mujer", "TATIANA", "¡Uf, qué madrugón!")],
   "why": "Ha reservado un taxi para las cinco. Su hermano no puede llevarle, y el primer tren sale demasiado tarde.",
   "img": "M06_CA1_6_coche_taxi_tren.jpg", "prompt": "Panel 1: a private family car. Panel 2: a white taxi. Panel 3: an airport train at a platform."},
 ]}

RADIO_FX = "SONIDO 2: Short bright radio station jingle, three cheerful synth notes, clean, no voices, no background noise"
CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. En la primera escucha marca una opción; en la segunda, compruébala. Cuidado con los descuentos y las condiciones: a quién se aplican, qué día y qué se paga.",
 "example": {"q": "En este programa...", "o": ["hablan de planes para el fin de semana.", "entrevistan a músicos famosos.", "venden entradas para conciertos."], "ok": 0,
   "why": "La opción correcta es la A porque el programa cuenta los planes del fin de semana.",
   "lab": "Locutor", "voice": "JUAN_CARLOS/RADIO",
   "text": "Esta tarde, en «Tu ciudad», te contamos los planes del fin de semana: conciertos, mercadillos y rutas para hacer en familia. Y si tienes un plan que recomendar, mándanos un mensaje de voz. Todos los viernes, de cinco a siete.",
   "solucion": "La opción correcta es la letra a, porque el programa cuenta los planes del fin de semana."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "Según el aviso, mañana...", "o": ["es mejor no ir a la playa.", "no hay clase en los colegios.", "va a hacer buen tiempo."], "ok": 0,
   "cats": ["tiempo", "normas"], "es": "ES-07", "pc": "se recomienda no ir · mañana / el viernes",
   "lab": "Locutor", "voice": "SERGIO/RADIO",
   "text": "Atención: la Agencia de Meteorología avisa de lluvias fuertes y viento para mañana jueves en toda la costa. Se recomienda no ir a la playa y no aparcar debajo de los árboles. Las clases en los colegios son normales. El viernes ya vuelve el buen tiempo.",
   "why": "Recomiendan no ir a la playa. Las clases son normales, y el buen tiempo vuelve el viernes, no mañana."},
  {"n": 8, "conv": "Audio 2", "q": "Según el anuncio, en esta academia...", "o": ["las clases son solo por la tarde.", "los grupos son de más de seis alumnos.", "hay un precio especial si vas con otra persona."], "ok": 2,
   "cats": ["cantidad"], "es": "ES-03", "pc": "como máximo · si te apuntas con un amigo, un diez por ciento",
   "lab": "Locutora", "voice": "TAMARA/RADIO",
   "text": "Academia Puerta del Sol. ¿Quieres aprender inglés, francés o alemán? Grupos de seis alumnos como máximo, por la mañana o por la tarde. Este mes la matrícula es gratis y, si te apuntas con un amigo, los dos tenéis un diez por ciento de descuento. ¡Llámanos!",
   "why": "Si te apuntas con un amigo, los dos tenéis un descuento. Hay clases de mañana y de tarde, y los grupos son de seis como máximo."},
  {"n": 9, "conv": "Audio 3", "q": "En el programa de hoy...", "o": ["preparan un plato con carne.", "explican un plato económico.", "hacen un postre sin horno."], "ok": 1,
   "cats": ["cantidad", "tiempo"], "es": "ES-07", "pc": "hoy / mañana · fácil y barato",
   "lab": "Locutora", "voice": "MARINA_ES/RADIO",
   "text": "Buenos días. Hoy, en «La cocina de casa», preparamos unas lentejas con verduras, un plato fácil y barato. No necesitáis carne: solo lentejas, zanahoria, pimiento, cebolla y un poco de pimentón. Y mañana, para los más golosos, un bizcocho de naranja sin horno.",
   "why": "Las lentejas son un plato barato: económico. No llevan carne, y el bizcocho sin horno es para mañana."},
  {"n": 10, "conv": "Audio 4", "q": "En Tecnocasa...", "o": ["los móviles tienen un descuento.", "regalan algo al comprar un teléfono.", "venden lavadoras de segunda mano."], "ok": 1,
   "cats": ["cantidad"], "es": "ES-04", "pc": "por la compra de un móvil, te regalamos",
   "lab": "Locutor", "voice": "ZABRA/RADIO",
   "text": "¡Solo este fin de semana en Tecnocasa! Todos los portátiles, con un veinte por ciento de descuento y, por la compra de un móvil, te regalamos unos auriculares. Y si tu lavadora ya no funciona, te recogemos la vieja gratis cuando compras una nueva. ¡Te esperamos!",
   "why": "Al comprar un móvil te regalan unos auriculares. El descuento es para los portátiles, y las lavadoras que venden son nuevas: la vieja se la llevan."},
  {"n": 11, "conv": "Audio 5", "q": "Según el anuncio, el cine de verano...", "o": ["no cuesta dinero.", "es todos los días de julio.", "cambia de lugar si llueve."], "ok": 0,
   "cats": ["normas", "tiempo"], "es": "ES-06", "pc": "la entrada es libre · si llueve, pasa al viernes",
   "lab": "Locutor", "voice": "CESAR/RADIO",
   "text": "Vuelve el cine de verano al parque del Castillo. Todos los jueves de julio y agosto, a las diez de la noche, una película para toda la familia. La entrada es libre, pero hay pocas sillas: puedes traer la tuya. Si llueve, la película pasa al viernes.",
   "why": "La entrada es libre: no cuesta dinero. Es solo los jueves, y si llueve cambia de día, no de lugar."},
  {"n": 12, "conv": "Audio 6", "q": "En la fiesta del barrio...", "o": ["la paella es gratis para los vecinos.", "los juegos para niños son por la tarde.", "hay que comprar antes el tique para comer."], "ok": 2,
   "cats": ["normas", "cantidad"], "es": "ES-06", "pc": "a cinco euros el plato · se compran antes",
   "lab": "Locutor", "voice": "DAVID_LAT/RADIO",
   "text": "Este sábado, fiesta del barrio de San Isidro. Por la mañana, juegos para niños en la plaza; a las dos, una gran paella para todos los vecinos, a cinco euros el plato, y por la noche, música y baile hasta la una. Los tiques de la paella se compran antes en la asociación de vecinos.",
   "why": "Los tiques de la paella se compran antes, en la asociación. La paella cuesta cinco euros, y los juegos son por la mañana."},
 ]}
for _x in [CA2["example"]] + CA2["items"]:
    _x["sound"] = RADIO_FX

CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Lucía y Andrés. Indique si los enunciados (del 13 al 18) se refieren a Lucía (A), a Andrés (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Lucía y Andrés hablan de la tecnología en su vida. Cuidado con los planes que cambian y con lo que hace otra persona: en esos casos, la respuesta es C.",
 "who": ["Lucía", "Andrés"], "voices": {"LUCIA": "EVA", "ANDRES": "MARIO"},
 "lines": [
  ("ANDRES", "¡Lucía! ¿Dónde te metes? Te escribí varios mensajes y no contestaste."),
  ("LUCIA", "Ya, perdona. Es que he pasado un mes sin redes sociales. Borré todas las aplicaciones del móvil."),
  ("ANDRES", "¿En serio? ¿Y qué tal?"),
  ("LUCIA", "Los primeros días, fatal: cogía el móvil cada cinco minutos sin pensar. Pero luego, genial. He leído tres novelas y duermo muchísimo mejor."),
  ("ANDRES", "Pues yo he hecho lo contrario: me he comprado un reloj inteligente. Mira, me cuenta los pasos, las horas de sueño, el corazón..."),
  ("LUCIA", "¿Y para qué quieres todo eso?"),
  ("ANDRES", "Para moverme más. El médico me dijo que camino muy poco. Ahora intento hacer diez mil pasos al día. Ayer subí andando a la oficina: ¡seis pisos!"),
  ("LUCIA", "¡Qué bien! ¿Y lo vas a usar también para correr?"),
  ("ANDRES", "Bueno, quería apuntarme a una carrera en diciembre, pero al final no. Primero, caminar."),
  ("LUCIA", "Mi hermano Raúl sí corre. Se ha apuntado a la media maratón de diciembre."),
  ("ANDRES", "¡Uf! ¿Y tú vas a volver a las redes?"),
  ("LUCIA", "Solo a una, para ver las fotos de la familia. Las demás, no. Ahora, cuando quedo con alguien, llamo por teléfono, como antes. Y la verdad es que hablamos mucho más."),
  ("ANDRES", "Oye, pues el sábado hay una exposición de fotografía en el centro cultural. ¿Vamos?"),
  ("LUCIA", "El sábado no puedo, tengo una comida con mis compañeros. ¿El domingo por la mañana?"),
  ("ANDRES", "Vale, el domingo. Y te llamo por teléfono, ¡nada de mensajes!")],
 "items": [
  {"n": 13, "q": "Ha dejado de usar algunas aplicaciones.", "ok": 0, "cats": ["pasados"], "es": "ES-08", "pc": "he pasado un mes sin · borré",
   "why": "Lucía borró las aplicaciones de las redes sociales y ha pasado un mes sin ellas."},
  {"n": 14, "q": "Ha empezado a ir andando a algunos sitios.", "ok": 1, "cats": ["pasados"], "es": "ES-03", "pc": "intento hacer diez mil pasos · subí andando",
   "why": "Andrés intenta caminar más: ayer subió andando los seis pisos de la oficina."},
  {"n": 15, "q": "Va a correr una carrera en diciembre.", "ok": 2, "cats": ["planes", "personas"], "es": "ES-05", "pc": "quería..., pero al final no · mi hermano se ha apuntado",
   "why": "Andrés quería apuntarse, pero al final no. El que va a correr es Raúl, el hermano de Lucía."},
  {"n": 16, "q": "Sigue el consejo de un profesional de la salud.", "ok": 1, "cats": ["personas"], "es": "ES-03", "pc": "el médico me dijo que...",
   "why": "El médico le dijo a Andrés que camina muy poco, y por eso ahora camina más."},
  {"n": 17, "q": "Va a ir a una exposición el sábado.", "ok": 2, "cats": ["planes", "tiempo"], "es": "ES-07", "pc": "el sábado no puedo · ¿el domingo?",
   "why": "La exposición es el sábado, pero Lucía no puede: van a ir el domingo por la mañana."},
  {"n": 18, "q": "Ahora llama más por teléfono que antes.", "ok": 0, "cats": ["pasados", "opinion"], "es": "ES-08", "pc": "ahora, cuando quedo, llamo por teléfono",
   "why": "Lucía dice que ahora, para quedar, llama por teléfono, como antes de las redes."}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

CH = "SONIDO 2: Two-tone ding-dong chime of a public address announcement system, clean and clear, no voices, no background noise"
BP = "SONIDO 1: Single short electronic answering machine beep, clean, no background noise"
CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. En cada mensaje pregúntate: ¿quién habla, dónde y para qué? Sobran tres enunciados y se parecen a otros: un tren que sale por otra vía no es un tren con retraso.",
 "enun": [
  "Alguien cambia la fecha de una cita.",
  "Una instalación deportiva no abre hoy.",
  "Un tren tiene retraso.",
  "Alguien ha recogido un envío para otra persona.",
  "Hay productos más baratos durante unas horas.",
  "Alguien invita a una fiesta de cumpleaños.",
  "Un vehículo ya está reparado.",
  "Un tren sale por otra vía.",
  "Una persona pide ayuda para un traslado.",
  "Una tienda cierra antes de lo normal.",
  "Se busca a la persona que ha perdido algo."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "DIANA/RADIO", "sound": BP,
   "text": "Buenos días, le llamamos de la clínica dental Sonríe. Su cita con la doctora Ramos no es el lunes: la cambiamos al miércoles, a la misma hora, a las cinco y media. Si no le va bien, llámenos. Gracias.",
   "solucion": "La opción correcta es la letra a: alguien cambia la fecha de una cita."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 7, "cats": ["lugares"], "es": "ES-10", "pc": "megafonía · no sale por la vía dos: sale por la vía cinco · a su hora",
   "lab": "Megafonía", "voice": "LUIS_VEGA/RADIO", "sound": CH,
   "text": "Atención, por favor. El tren con destino Málaga, con salida a las once y veinte, hoy no sale por la vía dos: sale por la vía cinco. Repetimos: vía cinco. El tren sale a su hora. Gracias.",
   "why": "El tren a Málaga sale por la vía cinco y no por la dos. Sale a su hora: no tiene retraso (C sobra)."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 8, "cats": ["planes"], "es": "ES-10", "pc": "me cambio de piso · ¿me puedes ayudar?",
   "lab": "Contestador", "voice": "TOMAS/RADIO", "sound": BP,
   "text": "Hola, Carla, soy Iván. El sábado me cambio de piso y mi hermano no puede venir. ¿Me puedes ayudar a llevar las cajas por la mañana? Después os invito a comer a todos. Llámame, por favor.",
   "why": "Iván pide ayuda para su mudanza. Invita a comer después, pero no es una fiesta de cumpleaños (F sobra)."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 4, "cats": ["cantidad", "tiempo"], "es": "ES-10", "pc": "solo hasta las dos · un treinta por ciento · como siempre",
   "lab": "Megafonía", "voice": "BOBBY/RADIO", "sound": CH,
   "text": "Atención, señores clientes: solo hasta las dos de la tarde, toda la fruta y la verdura con un treinta por ciento de descuento. Y en la panadería, la segunda barra de pan, gratis. Les recordamos que hoy cerramos a las nueve y media, como siempre.",
   "why": "Hay descuentos en la fruta y la verdura hasta las dos. La tienda cierra a la hora de siempre, no antes (J sobra)."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 3, "cats": ["personas"], "es": "ES-10", "pc": "un paquete para ti y lo tengo yo",
   "lab": "Contestador", "voice": "LINA/RADIO", "sound": BP,
   "text": "Hola, Mario, soy Pilar, tu vecina del cuarto. Esta mañana ha venido el repartidor con un paquete para ti y lo tengo yo. Estoy en casa toda la tarde, a partir de las cinco. Pasa cuando quieras.",
   "why": "La vecina ha recogido un paquete para Mario."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 1, "cats": ["normas", "tiempo"], "es": "ES-10", "pc": "hoy la piscina está cerrada · mañana abrimos",
   "lab": "Megafonía", "voice": "SANTIAGO_ES/RADIO", "sound": CH,
   "text": "Estimados usuarios: por una avería, hoy la piscina del polideportivo está cerrada todo el día. El gimnasio y las pistas de tenis funcionan con normalidad. Mañana abrimos a las siete, como siempre. Disculpen las molestias.",
   "why": "La piscina del polideportivo no abre hoy por una avería."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 10, "cats": ["lugares"], "es": "ES-10", "pc": "tenemos una cartera · su dueña puede recogerla",
   "lab": "Megafonía", "voice": "NINOSKA/RADIO", "sound": CH,
   "text": "Atención, por favor: en la oficina de información de la estación de autobuses tenemos una cartera roja con documentos. La encontramos esta mañana en el autobús de las ocho que llega de Murcia. Su dueña puede recogerla en la oficina.",
   "why": "En la estación buscan a la dueña de una cartera perdida."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 6, "cats": ["cantidad"], "es": "ES-10", "pc": "su coche ya está arreglado",
   "lab": "Contestador", "voice": "JUAN_CARLOS_2/RADIO", "sound": BP,
   "text": "Buenas tardes, le llamamos del taller Hermanos Gil. Su coche ya está arreglado: hemos cambiado los frenos y la batería. Puede pasar a recogerlo mañana, de nueve a dos. Son ciento ochenta euros.",
   "why": "El taller avisa de que el coche ya está arreglado."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

# Voces protagonistas del último simulacro que han hecho (U10): no se repiten aquí
VOCES_EVITAR = ["CLARA", "DAVID_M2", "SUSANA", "GABRIEL_ES", "VALENTINA", "DAVID_CO", "MARTIN_3", "MIA", "JUAN_RESTREPO", "SOFIA",
                "MARINA", "DIEGO", "CRISTINA", "ALEJANDRO", "EMILIO", "LUCIA", "JAVIER", "SARA", "LUIS_GUILLERMO", "HUGO",
                "MARTIN_1", "ESTELA", "MILO", "GABI", "MARTIN_2", "LUISA", "SANTIAGO_LAT", "CRISTIAN", "DAVID_M1", "JAVI_ROJAS"]
REPARTO = """# REPARTO DE VOCES M06 (ninguna voz de la U10, el último simulacro que han hecho)
# T1 conversaciones (v3, ritmo natural): 0 chico y abuela = DANI + NIEVE (Argentina, mayor)
#   1 dos amigas, la cena = FIONA + LYDIA · 2 quedar para el cine = OSCAR + SARA_JOVEN · 3 el tiempo = AITANA + DANIEL_ES
#   4 tienda, el regalo = ANA_MARIA (México) + VOLU · 5 la niña = SARA_2 + AGUSTIN (Argentina) · 6 aeropuerto = TATIANA (Latinoamérica) + RAFA
# T2 radio (perfil /RADIO, sintonía antes de cada audio): 0 «Tu ciudad» = JUAN_CARLOS · 1 aviso de lluvias = SERGIO
#   2 academia = TAMARA (México) · 3 «La cocina de casa» = MARINA_ES · 4 Tecnocasa = ZABRA · 5 cine de verano = CESAR · 6 fiesta del barrio = DAVID_LAT
# T3 conversación entre amigos: LUCÍA = EVA · ANDRÉS = MARIO
# T4 mensajes (/RADIO): 0 contestador dentista = DIANA (Colombia) · 1 megafonía estación = LUIS_VEGA · 2 contestador Iván = TOMAS (Argentina)
#   3 megafonía súper = BOBBY · 4 contestador vecina = LINA (Colombia) · 5 megafonía polideportivo = SANTIAGO_ES
#   6 megafonía estación de autobuses = NINOSKA · 7 contestador taller = JUAN_CARLOS_2
# Efectos: sintonía de radio (T2), din-don de megafonía y pitido de contestador (T4); siempre la misma descripción (caché)"""

# ---------------- ESCRITURA ----------------
# Textos modelo: [n] = empieza la frase de la pauta n · _texto_ = conector (sale subrayado).
ESCRITA = {"t1": {"instr": "Su amigo Pablo, que vive en otra ciudad, le ha escrito este correo.", "trato": "tú",
  "input": ["¡Hola! ¿Qué tal todo? ¡Por fin tengo vacaciones! Voy a tu ciudad del 3 al 6 de diciembre. ¿Qué podemos hacer esos días? ¿Puedo dormir en tu casa o busco un hotel? Cuéntame también qué tal estás tú.", "Un abrazo,<br>Pablo"],
  "lead": "Conteste a Pablo. En el correo tiene que:",
  "pautas": ["saludar y decirle qué le parece su visita;", "contarle qué ha hecho usted estas últimas semanas;", "proponerle dos planes para esos días y explicar por qué;", "contestar si puede dormir en su casa y por qué;", "hacerle dos preguntas sobre su viaje y despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Una revista para estudiantes de español busca textos de sus lectores con este título: «El mejor consejo que me han dado». Escriba su texto. Hable de:",
   "pautas": ["quién le dio el consejo y cómo es esa persona;", "cuándo fue y qué le pasaba a usted en ese momento;", "qué le dijo exactamente;", "qué hizo usted después;", "por qué piensa que fue un buen consejo."]},
  "op2": {"title": "Opción 2", "intro": "Bruno tiene diecisiete años y el verano pasado trabajó en una heladería. Aquí tiene tres fotos de su primer día.",
   "photos": ["10:00. La jefa, una mujer de unos cincuenta años con delantal, le enseña a Bruno a servir helados. Bruno escucha con atención.",
              "18:00. Hay una cola muy larga de clientes. A Bruno se le cae una bandeja con tres copas de helado.",
              "22:00. La heladería está cerrada. La jefa y Bruno toman un helado en la terraza y se ríen."],
   "ficha": [], "intro2": "Escriba un texto sobre el primer día de Bruno. Hable de:",
   "pautas": ["qué aprendió Bruno por la mañana;", "qué pasó por la tarde y cómo se sintió;", "cómo terminó el día y qué piensa usted de la jefa."],
   "img": "M06_escrita_bruno_heladeria.jpg", "imgAlt": "Tres fotos del primer día de Bruno en la heladería: aprende con la jefa, se le cae una bandeja y toman un helado al cerrar"},
  "min": 70, "max": 80},
 "modelos": {
  "t1": {"titulo": "Tarea 1 · Correo a un amigo (de tú)", "tarea": 1,
   "aprobado": {"texto": [
     "[1]¡Hola, Pablo!",
     "¡Qué bien que vienes a mi ciudad! Me parece una idea genial. [2]Yo estas semanas he trabajado mucho y he empezado un curso de cocina. [3]Esos días podemos ir al museo del centro, _porque_ tiene una exposición muy buena, y cenar en el puerto. [4]Claro que puedes dormir en mi casa: tengo una habitación libre. [5]¿A qué hora llega tu tren? ¿Vienes solo?",
     "Un abrazo,<br>Lucía"],
    "porque": "Contesta a las cinco pautas con frases sencillas: dice qué le parece la visita, cuenta lo que ha hecho con el pretérito perfecto (he trabajado, he empezado), propone dos planes con un porqué, contesta lo de dormir y hace dos preguntas. Todo de tú, del saludo a la despedida."},
   "excelente": {"texto": [
     "[1]¡Hola, Pablo!",
     "¡Qué alegría que vienes! [2]Yo estas semanas he estado muy ocupada: he cambiado de horario y, _además_, he empezado un curso de cocina. [3]El sábado podemos subir al castillo, _porque_ desde allí se ve todo el mar, y _después_ cenar en el puerto. [4]Puedes dormir en mi casa, claro: el sofá es muy cómodo. [5]¿Llegas en tren o en avión? ¿Vienes con tu novia?",
     "Un abrazo,<br>Lucía"],
    "porque": "Las mismas cinco pautas, con dos o tres mejoras del A2: más conectores para unir las ideas (además, después), un detalle que da vida al plan (desde allí se ve todo el mar), palabras más precisas y preguntas más concretas. Sigue siendo corto y de tú.",
    "mejoras": ["un conector más (además, después)", "un detalle o un porqué (desde allí se ve todo el mar)", "una palabra más precisa (subir al castillo, muy ocupada)", "una pregunta al lector más concreta (¿Llegas en tren o en avión?)"]}},
  "op1": {"titulo": "Tarea 2 · Opción 1 · El mejor consejo que me han dado", "tarea": 2,
   "aprobado": {"texto": [
     "[1]Mi abuela Carmen me dio el mejor consejo de mi vida. Es una mujer muy alegre y tranquila. [2]Fue en 2019. Tenía exámenes en la universidad y estaba muy nervioso. [3]Ella me dijo: «Estudia un poco cada día y duerme ocho horas». [4]_Después_, cambié mi horario y empecé a dormir más. [5]Creo que fue un buen consejo _porque_ aprobé todos los exámenes y ahora estoy más tranquilo antes de una prueba."],
    "porque": "Cumple las cinco pautas, una frase (o dos) para cada una. Usa bien el indefinido para lo que pasó (me dio, me dijo, cambié) y el imperfecto para la situación (tenía, estaba). Es sencillo y aprueba."},
   "excelente": {"texto": [
     "[1]Mi abuela Carmen me dio el mejor consejo de mi vida. Es muy alegre y nunca se pone nerviosa. [2]Fue en 2019, cuando estudiaba en la universidad: tenía cinco exámenes en una semana y casi no dormía. [3]Una noche me llamó y me dijo: «Estudia un poco cada día y duerme ocho horas». [4]_Al principio_ no la creí, _pero_ cambié mi horario. [5]_Por eso_ creo que fue un gran consejo: aprobé todo y, desde entonces, ¡duermo como un bebé!"],
    "porque": "Las mismas cinco pautas, con más variedad: conectores para ordenar (al principio, pero, por eso), un pasado bien combinado (cuando estudiaba..., me llamó), un detalle concreto (cinco exámenes en una semana) y un final con humor. Todo sigue siendo A2.",
    "mejoras": ["un conector más (al principio, por eso)", "un pasado bien combinado (cuando estudiaba..., me llamó)", "un detalle o un porqué (cinco exámenes en una semana)", "una frase con cuando"]}},
  "op2": {"titulo": "Tarea 2 · Opción 2 · El primer día de Bruno", "tarea": 2,
   "aprobado": {"texto": [
     "[1]El verano pasado, Bruno empezó a trabajar en una heladería. Por la mañana, la jefa le enseñó a servir los helados y él escuchó con mucha atención. [2]Por la tarde había muchísimos clientes y Bruno estaba muy nervioso. Se le cayó una bandeja con tres helados y pasó mucha vergüenza. [3]Por la noche, cuando cerraron la heladería, la jefa y Bruno tomaron un helado en la terraza y se rieron mucho. Creo que es una jefa muy simpática."],
    "porque": "Cuenta las tres fotos en pasado (no las describe en presente), responde a las tres pautas y da su opinión sobre la jefa. Frases claras y ordenadas por las horas del día."},
   "excelente": {"texto": [
     "[1]El verano pasado, Bruno trabajó en una heladería. El primer día, por la mañana, la jefa le explicó cómo servir los helados y él lo apuntaba todo en un cuaderno. [2]_Pero_ por la tarde la cola era enorme y Bruno estaba nerviosísimo. _De repente_, se le cayó una bandeja con tres copas. ¡Qué vergüenza! [3]_Al final_, cuando cerraron, la jefa lo invitó a un helado y se rieron juntos. Para mí, es una jefa estupenda, _porque_ entiende a los jóvenes."],
    "porque": "Más variedad de pasados (explicó / apuntaba, la cola era enorme / se le cayó), conectores de relato (por la tarde, de repente, al final), una exclamación con emoción y una opinión con su porqué.",
    "mejoras": ["un conector más (de repente, al final)", "un pasado bien combinado (la cola era enorme y se le cayó...)", "una palabra más precisa (nerviosísimo, estupenda)", "un detalle o un porqué (entiende a los jóvenes)"]}}}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: un objeto muy especial para mí", "pautas": ["qué objeto es, cómo es y dónde está ahora;", "cuándo y cómo lo consiguió y por qué es especial para usted;", "qué objeto especial tenía usted de niño o de niña y qué hacía con él;", "qué cosas guarda la gente de su país como recuerdo (fotos, cartas, joyas...) y qué piensa usted de eso;", "si piensa regalarlo algún día o guardarlo siempre, y por qué."]},
  {"title": "Opción 2: la música en mi vida", "pautas": ["qué música le gusta y cuándo la escucha;", "qué música escuchaban en su casa cuando era pequeño o pequeña;", "el mejor concierto o la mejor fiesta con música de su vida: dónde fue y con quién;", "qué música es típica de su país y en qué fiestas se escucha;", "qué planes tiene: un concierto, una clase, un festival..."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1 · Preparar un viaje", "desc": "El salón de un piso, una tarde de otoño. Dos hermanos de unos treinta años preparan las mochilas para un fin de semana en la montaña. Ella, con el pelo largo recogido, gafas y una sudadera gris, está de rodillas en el suelo y mete un saco de dormir en una mochila roja. Él, con barba corta y camisa de cuadros, está sentado en el sofá, mira unas botas de montaña y lleva un gorro de lana puesto, aunque está en casa. Alrededor hay otra mochila, un chubasquero, gorros, una linterna, un termo, una botella de agua, galletas y un mapa abierto.", "img": "M06_oral_foto1_mochilas_montana.jpg"},
  {"title": "Fotografía 2 · Pintar la casa", "desc": "El salón de un piso pequeño, una mañana de primavera con sol. Un padre de unos sesenta años y su hija de unos veinticinco pintan las paredes de azul claro. Ella, con el pelo corto y rizado y un mono viejo, pinta con un rodillo y tiene una mancha de pintura en la cara; se ríe. Él, calvo, con bigote y un gorro de papel de periódico, está subido a una escalera pequeña y pinta con una brocha cerca del techo. El sofá y la mesa están en el centro, tapados con plástico; en el suelo hay periódicos, botes de pintura, una bandeja, cinta, una radio y dos tazas de café.", "img": "M06_oral_foto2_pintar_salon.jpg"}],
  "pautas": ["¿Cómo son las personas de la foto (físico, personalidad que cree que tienen...)? ¿Qué ropa llevan?", "¿Dónde están esas personas? ¿Qué objetos hay? Describa el lugar.", "¿Qué están haciendo las personas de la foto?", "¿Qué relación cree que hay entre ellas?", "¿Qué cree que piensan o cómo se sienten estas personas? ¿Por qué?", "¿Qué cree que han hecho antes? ¿Y qué van a hacer después?"]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1 · Preparar un viaje a la montaña", "intro": "Usted y su hermano o hermana van a pasar un fin de semana en una casa rural en la montaña. Antes del viaje tienen que organizarse y comprar algunas cosas. El examinador / La examinadora es su hermano/a. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su hermano/a, tiene que hablar de:", "pautas": ["qué cosas tienen ya y qué tienen que comprar (ropa, calzado, comida...);", "si ha ido alguna vez a la montaña: cuándo, con quién y qué tal fue;", "qué actividades les gustaría hacer allí y por qué;", "dónde van a comprar las cosas, quién compra qué y cuánto dinero pueden gastar;", "cómo y cuándo van a ir, y dónde quedan para salir."]},
  {"title": "Si eligió la fotografía 2 · Pintar la casa", "intro": "Usted quiere pintar su salón y cambiar un poco la decoración. Un amigo o una amiga le va a ayudar. El examinador / La examinadora es su amigo/a. Hable con él/ella siguiendo estas indicaciones. Durante la conversación con su amigo/a, tiene que hablar de:", "pautas": ["cómo es su salón ahora y qué quiere cambiar;", "qué colores le gustan para las paredes y por qué;", "si ha pintado o arreglado alguna vez una casa: cuándo, dónde y con quién;", "qué necesitan comprar y dónde lo van a comprar;", "qué día van a pintar, a qué hora quedan y quién hace cada cosa."]}]}}

# Modelos de la tarea 3 (se ven en la oral del estudiante después de la prueba y en la libreta de la profesora).
# En el diálogo, "E" = examinador y "C" = candidato. La frase del pequeño problema lleva "problema": True.
# Como en las láminas de 2022, las dos situaciones son de tú y mezclan planificar con contar cosas propias.
ORAL_MODELOS = {"t3": [
 {"titulo": "Fotografía 1 · Preparar un viaje a la montaña", "trato": "tú",
  "notas": [["qué tenemos y qué comprar", "yo: mochila, saco · comprar: botas (las mías, rotas) · ¿y tú?"],
            ["¿he ido a la montaña?", "Pirineos, hace 2 años, con amigos · ruta bonita · mucho frío · ¿y tú?"],
            ["actividades", "ruta al lago (precioso) · cenar en el pueblo · ¿qué te parece?"],
            ["dónde, quién, dinero", "tienda de deporte del centro comercial · yo botas / tú chaqueta · comida juntos · 100 € cada uno"],
            ["cómo y cuándo", "mi coche · viernes a las 5 · en tu casa"]],
  "segunda": "Si va a llover: comprar dos chubasqueros y cambiar el orden (el sábado, el pueblo; el domingo, la ruta).",
  "problema": "El examinador ha visto que el sábado va a llover todo el día.",
  "dialogo": [
   ["E", "¡Hola! ¿Qué tal? Oye, ¿preparamos ya el viaje a la montaña? ¿Qué tenemos que comprar?"],
   ["C", "¡Hola! Sí, vamos a ver. Yo ya tengo la mochila y el saco de dormir, pero necesito unas botas nuevas, porque las mías están rotas. ¿Tú qué tienes?"],
   ["E", "Yo tengo botas, pero no tengo chaqueta para el frío. Oye, ¿tú has ido alguna vez a la montaña?"],
   ["C", "Sí, fui hace dos años a los Pirineos con unos amigos. Hicimos una ruta muy bonita, pero hacía muchísimo frío. ¿Y tú?"],
   ["E", "Yo solo una vez, de pequeño, con el colegio. ¿Y qué quieres hacer allí?"],
   ["C", "Me gustaría hacer la ruta hasta el lago, porque dicen que es precioso. Y por la noche podemos cenar en el pueblo. ¿Qué te parece?"],
   ["E", "¡Genial! ¿Y dónde compramos las cosas?"],
   ["C", "En la tienda de deporte del centro comercial: tiene de todo y no es cara. Yo compro las botas y tú la chaqueta, y la comida la compramos juntos. ¿Gastamos unos cien euros cada uno?"],
   ["E", "Vale. Pero, oye, he visto el tiempo: el sábado va a llover todo el día.", True],
   ["C", "¡Vaya! Entonces tenemos que comprar también dos chubasqueros. ¿Y si el sábado visitamos el pueblo y hacemos la ruta el domingo?"],
   ["E", "Buena idea. ¿Y cómo vamos?"],
   ["C", "En mi coche. Quedamos el viernes a las cinco en la puerta de tu casa, ¿vale? ¡Hasta el viernes!"]]},
 {"titulo": "Fotografía 2 · Pintar la casa", "trato": "tú",
  "notas": [["mi salón ahora", "oscuro · paredes marrones · muebles viejos · cambiar el sofá de sitio"],
            ["colores", "azul claro (tranquilo, parece más grande) · ¿a ti te gusta?"],
            ["¿he pintado?", "el año pasado · mi habitación con mi padre · 2 días · pintura en el pelo · ¿y tú?"],
            ["comprar", "pintura, 2 rodillos, plástico para los muebles · tienda de bricolaje del barrio"],
            ["día, hora, quién", "sábado por la mañana · tú las paredes / yo las puertas · después, pizza"]],
  "segunda": "Si no puede por la mañana: empezar por la tarde (a las cuatro) o el domingo; el candidato compra y prepara todo antes.",
  "problema": "El examinador no puede el sábado por la mañana: tiene que llevar a su madre al médico.",
  "dialogo": [
   ["E", "¡Hola! Me ha dicho tu hermana que quieres pintar el salón. ¿Te ayudo?"],
   ["C", "¡Hola! ¡Sí, por favor! Es que mi salón es muy oscuro: las paredes son marrones y los muebles son viejos. Quiero pintarlo y cambiar el sofá de sitio. ¿Tú qué opinas?"],
   ["E", "Me parece muy buena idea. ¿Y de qué color lo quieres pintar?"],
   ["C", "Me gusta el azul claro, porque es un color tranquilo y el salón va a parecer más grande. ¿A ti te gusta?"],
   ["E", "Sí, mucho. Oye, ¿tú has pintado alguna vez?"],
   ["C", "Sí, el año pasado pinté mi habitación con mi padre. Tardamos dos días y al final teníamos pintura hasta en el pelo. ¿Y tú?"],
   ["E", "Yo pinté la casa de mis abuelos un verano. ¿Y qué tenemos que comprar?"],
   ["C", "Pues la pintura, dos rodillos y plástico para tapar los muebles. Lo podemos comprar en la tienda de bricolaje de mi barrio. ¿Pintamos el sábado por la mañana?"],
   ["E", "Uy, el sábado por la mañana no puedo: tengo que llevar a mi madre al médico.", True],
   ["C", "No pasa nada. ¿Y si empezamos el sábado a las cuatro? Yo compro todo por la mañana y lo preparo. Tú pintas las paredes grandes y yo las puertas, ¿vale?"],
   ["E", "Perfecto. Y después, ¿cenamos algo?"],
   ["C", "¡Claro! Te invito a una pizza. Entonces, el sábado a las cuatro en mi casa. ¡Hasta el sábado!"]]}]}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (un objeto especial): ¿Quién se lo regaló? · ¿Qué hacía con ese objeto de pequeño/a?
    Opción 2 (la música): ¿Qué canción le recuerda a su infancia? · ¿Va a ir a algún concierto este año?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (preparar un viaje): ¿Adónde cree que van a ir? · ¿Por qué cree que él lleva un gorro en casa?
    Foto 2 (pintar la casa): ¿Por qué cree que pintan el salón? · ¿Qué van a hacer cuando terminen?
  Tarea 3 — su papel: hermano/a o amigo/a del candidato, SIEMPRE DE TÚ (como en las láminas de 2022). Vaya pauta
  por pauta, elija las preguntas según lo que diga el candidato, improvise con sus datos y provoque UN pequeño
  problema. Esquema para la interacción:
    Foto 1 (hermano/a · viaje a la montaña)
      Saludar ............. ¡Hola! ¿Qué tal? ¿Preparamos ya el viaje? ¿Qué tenemos que comprar?
      Qué tienen .......... Yo tengo botas, pero no tengo chaqueta. ¿Y tú qué tienes? ¿Qué te falta?
      La montaña .......... ¿Tú has ido alguna vez a la montaña? ¿Cuándo? ¿Con quién? ¿Qué tal fue?
      Actividades ......... ¿Qué quieres hacer allí? ¿Por qué? ¿Y por la noche?
      Comprar y dinero .... ¿Dónde compramos las cosas? ¿Quién compra qué? ¿Cuánto podemos gastar?
      PEQUEÑO PROBLEMA .... «He visto el tiempo: el sábado va a llover todo el día». Espere a que proponga algo
                            (chubasqueros, cambiar el orden de los planes).
      Viaje y despedida ... ¿Cómo vamos? ¿A qué hora salimos? ¿Dónde quedamos? · De acuerdo, ¡hasta el viernes!
    Foto 2 (amigo/a · pintar el salón)
      Saludar ............. ¡Hola! Me han dicho que quieres pintar el salón. ¿Te ayudo?
      El salón ahora ...... ¿Cómo es tu salón ahora? ¿Qué no te gusta? ¿Qué quieres cambiar?
      Colores ............. ¿De qué color lo quieres pintar? ¿Por qué ese color?
      Experiencia ......... ¿Tú has pintado alguna vez? ¿Cuándo? ¿Con quién? ¿Qué tal fue?
      Comprar ............. ¿Qué tenemos que comprar? ¿Dónde? ¿Cuánto cuesta más o menos?
      PEQUEÑO PROBLEMA .... «El sábado por la mañana no puedo: tengo que llevar a mi madre al médico». Espere a que
                            proponga otra hora u otro día.
      Organizar y adiós ... ¿Quién hace cada cosa? ¿Cenamos algo después? · Vale, ¡hasta el sábado!
    El diálogo modelo de las dos situaciones está en la pestaña Oral del estudiante (se ve al abrir la prueba).
  Qué mirar en este modelo: tú coherente en toda la tarea 3; que no conteste solo sí o no (responde + detalle o
  porqué + pregunta); proponer y aceptar o rechazar con otra propuesta (¿y si...?, ¿te va bien...?); en la tarea 3,
  la pauta de experiencia en pasado (fui, hicimos, pinté, hacía frío); en el monólogo, presente + pasado
  (indefinido / imperfecto: cuando era pequeño tenía...) + planes, y la pauta que se sale de la historia personal
  (lo que se guarda o la música típica de su país); en la foto, las seis preguntas en orden, hay / está,
  estar + gerundio y «seguramente han...» / «van a...»."""
ERRORES = """  *Tú puede / *¿Usted tienes...? (mezcla tú / usted); *Yo propongo que compramos (propongo comprar / ¿compramos...?);
  *El sábado va a lluvia (va a llover); *Necesitamos un botas (unas botas); *Cuando era niño, tuve una bicicleta
  roja para un hábito (tenía); *Este objeto me regaló mi abuela (me lo regaló / este objeto es un regalo de mi
  abuela); *Hay el sofá en el centro (el sofá está / hay un sofá); *Están cansado (cansados); *Quiero ir en la montaña (a
  la montaña); *A las ocho de la tarde (de la noche, en España después de las ocho y media); frases sueltas sin
  conectores en el monólogo («y... y... y...»)."""

# ---------------- IMÁGENES: FOTOS CON VARIEDAD REAL ----------------
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "salón de casa: dos hermanos preparan las mochilas para la montaña",
  "personas": "dos hermanos", "edades": "los dos de unos 30 años",
  "aspecto": "ella con el pelo largo y oscuro recogido en una coleta, gafas y una sudadera gris; él con barba corta, camisa de cuadros, vaqueros y un gorro de lana con pompón puesto dentro de casa",
  "espacio": "interior", "lugar": "salón normal de un piso, con sofá, estantería, televisión, una lámpara y una ventana", "momento": "tarde-noche",
  "estacion": "otoño", "tiempo": "fuera ya es de noche; la lámpara está encendida", "gente": "solo ellos dos",
  "accion": "ella mete un saco de dormir en una mochila roja, de rodillas en el suelo; él, sentado en el sofá, mira unas botas de montaña",
  "fondo": "estantería con libros, televisión apagada, una planta, la calle de noche por la ventana",
  "objetos": "dos mochilas, saco de dormir, botas de montaña, chubasquero, gorros, linterna, termo, botella de agua, galletas, un botiquín, un mapa abierto",
  "detalle": "él lleva un gorro de lana con pompón aunque está en casa (¿se lo está probando? ¿le hace gracia?)"},
 "oral_foto2": {"situacion": "padre e hija pintan el salón de un piso",
  "personas": "un padre y su hija", "edades": "él de unos 60 años, ella de unos 25",
  "aspecto": "él calvo, con bigote gris, camiseta azul vieja y un gorro hecho con papel de periódico; ella con el pelo corto y rizado, un mono viejo con manchas y una mancha de pintura azul en la cara",
  "espacio": "interior", "lugar": "salón pequeño de un piso, con una ventana grande", "momento": "mañana",
  "estacion": "primavera", "tiempo": "sol: entra mucha luz por la ventana", "gente": "solo ellos dos",
  "accion": "ella pinta una pared de azul claro con un rodillo y se ríe; él, subido a una escalera pequeña, pinta con una brocha cerca del techo",
  "fondo": "el sofá y la mesa en el centro, tapados con plástico; la ventana con la luz del sol",
  "objetos": "rodillo, brocha, botes de pintura, bandeja de pintura, escalera, plástico, periódicos en el suelo, cinta de pintor, una radio, dos tazas de café",
  "detalle": "la hija tiene pintura en la cara y el padre lleva un gorro de papel de periódico"},
 "escrita": {"situacion": "primer día de trabajo de verano de un chico en una heladería",
  "personas": "Bruno (en tres momentos), su jefa y clientes", "edades": "Bruno de 17 años; jefa de unos 50; clientes de todas las edades",
  "aspecto": "Bruno, delgado, con el pelo castaño un poco largo, camiseta blanca, delantal de rayas rosas y gorra de papel; jefa con el pelo corto y canoso, gafas en la cabeza y el mismo delantal",
  "espacio": "interior y exterior", "lugar": "heladería pequeña de un paseo marítimo y su terraza", "momento": "mañana, tarde y noche",
  "estacion": "verano", "tiempo": "sol y calor; noche templada", "gente": "vacía por la mañana; una cola larga por la tarde; vacía por la noche",
  "accion": "aprender a servir con la jefa; dejar caer una bandeja con tres copas de helado; tomar un helado los dos en la terraza",
  "fondo": "la vitrina de helados de colores; la cola de clientes con niños y una pareja mayor; las farolas del paseo encendidas",
  "objetos": "vitrina de helados, cucuruchos, copas de cristal, bandeja, cucharas, servilletas, sillas y mesas de terraza, farolas",
  "detalle": "Bruno pasa vergüenza cuando se le cae la bandeja delante de los clientes"},
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
}

IMG_PROMPTS = {
 "escrita": "The same teenage boy of about 17, thin, with slightly long brown hair, a white T-shirt, a pink-and-white striped apron and a paper cap, on his first day working in a small ice-cream shop on a Spanish seaside promenade in summer. Panel 1 (left): morning, the shop is empty, his boss, a woman of about 50 with short grey hair, glasses pushed up on her head and the same striped apron, shows him how to scoop ice cream into a cone behind a counter full of colourful ice-cream tubs; he listens carefully. Panel 2 (middle): afternoon, a long queue of customers (children, a mother, an elderly couple) in front of the counter; the boy has just dropped a tray with three glass cups of ice cream, which fall towards the floor; he looks embarrassed and the customers look surprised. Panel 3 (right): night, the shop is closed, the boy and his boss sit at a table on the terrace under the lit street lamps of the promenade, each eating an ice cream and laughing together.",
 "oral_foto1": "A brother and a sister of about 30 in the living room of an ordinary Spanish flat on an autumn evening, packing for a weekend in the mountains. The sister, with long dark hair in a ponytail, glasses and a grey sweatshirt, kneels on the floor and pushes a rolled-up sleeping bag into a big red backpack. Her brother, with a short beard, a checked flannel shirt and jeans, sits on the sofa holding a pair of hiking boots and looking at the soles; he is wearing a woolly bobble hat indoors, which looks a bit funny. Around them on the floor and the sofa: a second backpack, a folded rain jacket, woolly hats, a torch, a thermos, a water bottle, a packet of biscuits, a small first-aid bag and an open paper map. Behind them an ordinary room: a lamp switched on, a bookshelf, a switched-off TV, a plant, and a window with the dark street outside.",
 "oral_foto2": "A father of about 60 and his daughter of about 25 painting the small living room of a Spanish flat on a sunny spring morning. The daughter, with short curly hair, wears old paint-stained overalls and has a smear of light blue paint on her cheek; she paints a wall light blue with a long roller and laughs. The father, bald with a grey moustache, in an old blue T-shirt and a hat folded from newspaper, stands on a small stepladder painting near the ceiling with a brush. The sofa and a table are pushed to the middle of the room and covered with plastic sheets; on the floor, covered with old newspapers: open paint tins, a paint tray, brushes, masking tape, a small radio and two coffee cups. Daylight comes in through a big window.",
}
IMG_NAMES = {"escrita": "M06_escrita_bruno_heladeria", "oral_foto1": "M06_oral_foto1_mochilas_montana", "oral_foto2": "M06_oral_foto2_pintar_salon"}
IMG_DESC = {"escrita": "Escritura opcion 2 triptico Bruno heladeria: 1 aprende con la jefa, 2 se le cae la bandeja con la cola, 3 helado en la terraza de noche",
            "oral_foto1": "Oral foto 1 preparar un viaje: dos hermanos hacen las mochilas para la montana en el salon",
            "oral_foto2": "Oral foto 2 pintar la casa: padre e hija pintan el salon de azul claro"}
CA1_DESC = {0: "Auditiva T1 ejemplo: gafas de sol / bufanda / cargador", 1: "Auditiva T1 conv 1: tarta / vino / ensalada de pasta",
            2: "Auditiva T1 conv 2: puerta del cine / cafeteria / metro", 3: "Auditiva T1 conv 3: sol / lluvia / nieve en la montana",
            4: "Auditiva T1 conv 4: libro / panuelo / pendientes", 5: "Auditiva T1 conv 5: teatro / natacion / piano",
            6: "Auditiva T1 conv 6: coche / taxi / tren del aeropuerto"}

LECTURA = [CL1, CL2, CL3, CL4]
AUDITIVA = [CA1, CA2, CA3, CA4]
