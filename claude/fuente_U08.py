# -*- coding: utf-8 -*-
# FUENTE DE LA UNIDAD 8 (fase 1) · Estamos muy bien
# EXAMEN COMPLETO · lectura T1+T2+T3+T4 (60 min, 25 ítems) · auditiva T1+T2+T3+T4 (40 min, 25 ítems)
U = "08"
TITLE = "Estamos muy bien"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress (cambiar si se suben otro mes)
TIEMPOS = {"lectura": 60, "auditiva": 40}
RECORDATORIO = [
 "Describir dolores, molestias y síntomas: me duele la cabeza / me duelen los pies (doler funciona como gustar); tengo fiebre, tos, gripe, dolor de espalda; estoy mareado/a, resfriado/a, afónico/a, enfermo/a.",
 "Partes del cuerpo (la cabeza, el cuello, la espalda, el brazo, la mano, la pierna, la rodilla, el pie...) y léxico de la salud y el deporte: el centro de salud, la farmacia, el jarabe, las pastillas, la receta; fortalecer, prevenir, combatir el estrés, mejorar el equilibrio.",
 "Dar consejos: lo mejor es / es bueno + infinitivo; ...va (muy) bien para...; tienes que, debes, puedes + infinitivo.",
 "Imperativo afirmativo: tú (toma, bebe, descansa; irregulares haz, pon, ven, di, sal, ten, ve, sé), vosotros (tomad, bebed), usted (tome, beba), ustedes (tomen, beban). Los pronombres van detrás y en una sola palabra: tómalo, levántate, llámame.",
 "Ser o estar: ser para describir y definir (es enfermera, es muy tranquilo); estar para estados físicos y de ánimo (está cansada, está nervioso), para la localización (la crema está en el baño) y en estar + gerundio.",
 "Estados de ánimo: estar contento/a, triste, nervioso/a, preocupado/a, enfadado/a, estresado/a, cansado/a, aburrido/a, tranquilo/a.",
]
TIPS_INICIO = [
 "<b>Examen completo, como el día del DELE:</b> lectura 60 minutos (4 tareas, 25 preguntas) y auditiva 40 minutos (4 tareas, 25 preguntas). Reparte el tiempo de la lectura: unos 12 minutos para la tarea 1, 15 para la 2, 15 para la 3 y 18 para la 4.",
 "<b>Escucha bien qué le duele a cada persona y qué le aconsejan:</b> muchas veces la primera idea no es la respuesta («no, la cabeza no; son los oídos», «nadar no; mejor caminar»). Espera al final de la conversación antes de marcar.",
]
CATS = {
 "doler": {"name": "El verbo doler y los síntomas (me duele, tengo fiebre, estoy mareado)",
  "repaso": "Doler funciona como gustar: me / te / le / nos / os / les + duele + nombre en singular (me duele la cabeza) o duelen + nombre en plural (me duelen los pies). Para otros síntomas: tener tos, fiebre, gripe, dolor de + parte del cuerpo; estar mareado/a, resfriado/a, afónico/a, enfermo/a. Preguntar: ¿Qué te pasa? ¿Qué te duele? En el libro: unidad 8, el verbo doler y hablar de enfermedades, molestias y síntomas.",
  "reto": "Imagina que hoy estás enfermo/a y escribe cinco frases: me duele..., me duelen..., tengo..., estoy..."},
 "cuerpo": {"name": "Partes del cuerpo",
  "repaso": "La cabeza, la cara, los ojos, la nariz, la boca, el cuello, la espalda, el pecho, el brazo, el codo, la mano, el dedo, la barriga, la pierna, la rodilla, el tobillo, el pie. Con doler y con los artículos: me duele la rodilla (no *mi rodilla). En el libro: unidad 8, las partes del cuerpo.",
  "reto": "Dibuja una persona y escribe diez partes del cuerpo con su artículo."},
 "salud": {"name": "Léxico de la salud: enfermedades, remedios, médico y farmacia",
  "repaso": "Enfermedades y síntomas: la gripe, el resfriado, la tos, la fiebre, el insomnio, el estrés, la alergia. Remedios: las pastillas, el jarabe, la crema, la infusión, la miel. Lugares y personas: el centro de salud, la farmacia (de guardia), el médico, el fisioterapeuta, la cita, la receta, las urgencias. Verbos: curar, prevenir, combatir, hidratar, calmar el dolor. En el libro: unidad 8, léxico de la salud y beneficios para la salud.",
  "reto": "Escribe qué tomas o qué haces cuando tienes tos, dolor de cabeza y problemas para dormir."},
 "consejos": {"name": "Dar consejos (lo mejor es, va bien para, es bueno, tienes que, debes, puedes)",
  "repaso": "Consejos impersonales: lo mejor es + infinitivo (lo mejor es dormir de lado); es bueno + infinitivo; ...va (muy) bien para... (el yoga va muy bien para la espalda). Consejos personales: tienes que, debes, puedes + infinitivo. También el imperativo: descansa, bebe agua. En el libro: unidad 8, dar consejos.",
  "reto": "Un amigo duerme muy mal. Dale cinco consejos con cinco estructuras diferentes."},
 "imperativo": {"name": "Imperativo afirmativo (forma y usos: consejos, instrucciones)",
  "repaso": "Tú: como el presente sin -s (toma, bebe, escribe; piensa, duerme, pide). Irregulares: haz, pon, ven, di, sal, ten, ve, sé. Vosotros: el infinitivo con -d (tomad, bebed, venid). Usted / ustedes: tome / tomen, beba / beban. Los pronombres van detrás y en una sola palabra: tómalo, levántate, llámame. Sirve para dar consejos, instrucciones y recetas. En el libro: unidad 8, el imperativo afirmativo. Repasa también la ficha «Imperativo afirmativo» que te da tu profesora.",
  "reto": "Escribe una receta de un remedio casero (una infusión, una mascarilla...) con cinco verbos en imperativo."},
 "serestar": {"name": "Ser y estar (cómo es / cómo está; dónde está; estar + gerundio)",
  "repaso": "Ser para identificar, definir y describir: es enfermera, es de Bilbao, es muy tranquilo. Estar para estados físicos y de ánimo (está cansada, está nervioso), para la localización (la farmacia está en la plaza) y en estar + gerundio (está haciendo un máster). En el libro: unidad 8, usos de ser y estar.",
  "reto": "Describe a una persona de tu familia con tres frases con ser y tres con estar."},
 "animo": {"name": "Estados de ánimo (estar contento, nervioso, preocupado, estresado...)",
  "repaso": "Estar contento/a, triste, nervioso/a, preocupado/a, enfadado/a, sorprendido/a, estresado/a, cansado/a, aburrido/a, tranquilo/a, de buen / mal humor. Recuerda: con estos adjetivos usamos estar. En el libro: unidad 8, estados de ánimo.",
  "reto": "Escribe cómo estás en cinco momentos de tu semana: el lunes por la mañana, antes de un examen..."},
 "deporte": {"name": "Deporte y beneficios para la salud (fortalecer, prevenir, combatir el estrés)",
  "repaso": "Deportes y actividades: nadar, correr, el yoga, el pilates, el taichí, el baloncesto, hacer estiramientos, ir al gimnasio. Beneficios: fortalecer la espalda, mejorar el equilibrio y la flexibilidad, perder peso, combatir el estrés, prevenir dolores. En el libro: unidad 8, es bueno para la espalda.",
  "reto": "Escribe tres deportes y para qué va bien cada uno."},
}
ESTRATEGIAS_NUEVAS = {}

# ---------------- LECTURA ----------------
CL1 = {"n": 1, "type": "mail",
 "instr": "Usted va a leer el correo electrónico que Lorena ha escrito a su amiga Isabel. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Fíjate en quién hace cada cosa (Lorena, Isabel, la médica, la hermana) y en qué pasó antes y qué pasa ahora.",
 "head": ["De: Lorena", "Para: Isabel", "Asunto: ¡Por fin estoy mejor!"],
 "body": [
  "Hola, Isabel:",
  "¿Qué tal estás? ¿Ya puedes caminar bien después de la operación de rodilla? Te escribo porque por fin tengo buenas noticias. Ya sabes que este año he estado muy estresada: en la tienda tenemos muchísimo trabajo y mi jefe está siempre de mal humor. En primavera tuve muchos dolores de cabeza y durante meses dormí fatal.",
  "En julio fui a la médica. Me dijo que no estoy enferma, que es el estrés, y me dio algunos consejos: hacer deporte, cenar menos y dejar el móvil fuera del dormitorio. Al principio no le hice mucho caso, pero en septiembre me apunté a natación. Ahora voy a la piscina tres días a la semana, antes del trabajo, y me encanta. Ya no me duele la cabeza y duermo como un bebé. Además, mis compañeros de la piscina son muy simpáticos y, después de nadar, tomamos un café juntos.",
  "Y mi hermana Celia, que es enfermera, me ha regalado un libro de yoga. Dice que el yoga va muy bien para la espalda y para los nervios. Lo hago en casa los domingos, con un vídeo. Todavía no soy muy flexible, ¡pero me río mucho!",
  "Y ahora, una propuesta: el mes que viene abren un balneario nuevo cerca de Granada, con piscinas de agua caliente y masajes. ¿Por qué no vamos juntas un fin de semana? Yo conduzco, así que no tienes que caminar mucho. El agua caliente va muy bien para la rodilla, ¿no? Yo te invito al masaje. Piénsalo y dime algo.",
  "Un abrazo muy fuerte y cuídate mucho,<br>Lorena"],
 "items": [
  {"n": 1, "q": "Lorena escribe a Isabel para...", "o": ["contarle cómo está y proponerle un plan.", "pedirle consejo para un problema de salud.", "contarle que la han operado de la rodilla."], "ok": 0,
   "cats": ["salud"], "es": "ES-02", "pc": "FN contar novedades · FN proponer (¿por qué no vamos...?)",
   "why": "Lorena le cuenta que ya está mejor y le propone ir juntas a un balneario. Los consejos se los dio la médica, y la operación de rodilla es de Isabel, no de Lorena."},
  {"n": 2, "q": "En primavera, Lorena...", "o": ["fue a la médica.", "durmió mal durante mucho tiempo.", "dejó su trabajo en la tienda."], "ok": 1,
   "cats": ["doler", "salud"], "es": "ES-03", "pc": "síntomas (dolores de cabeza) · indefinido (U02)",
   "why": "Durante meses durmió fatal: durmió mal mucho tiempo. Fue a la médica en julio, no en primavera, y sigue trabajando en la tienda."},
  {"n": 3, "q": "La médica le dijo a Lorena que...", "o": ["tiene que cambiar algunas costumbres.", "tiene una enfermedad.", "tiene que ir a nadar todos los días."], "ok": 0,
   "cats": ["consejos", "salud"], "es": "ES-03", "pc": "dar consejos · LX salud (estar enfermo, el estrés)",
   "why": "Le aconsejó hacer deporte, cenar menos y dejar el móvil fuera del dormitorio: cambiar costumbres. No está enferma, y la natación fue idea de Lorena, tres días a la semana."},
  {"n": 4, "q": "Ahora Lorena...", "o": ["va a la piscina todos los días.", "hace yoga con su hermana.", "se encuentra mejor que antes."], "ok": 2,
   "cats": ["doler", "deporte"], "es": "ES-08", "pc": "ya no me duele · LX deporte (natación, yoga)",
   "why": "Ya no le duele la cabeza y duerme muy bien: está mejor. Va a la piscina tres días a la semana, y hace yoga sola en casa con un vídeo; su hermana solo le regaló el libro."},
  {"n": 5, "q": "Lorena propone a Isabel...", "o": ["ir a una médica de Granada.", "descansar juntas unos días.", "ir a Granada en tren."], "ok": 1,
   "cats": ["imperativo", "salud"], "es": "ES-03", "pc": "FN proponer · imperativo (piénsalo, dime)",
   "why": "Le propone pasar un fin de semana juntas en un balneario. Granada es el lugar del balneario, no de una médica, y no van en tren: Lorena conduce."},
 ]}

CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 15 minutos: menos de dos minutos por anuncio. Lee la pregunta primero y busca solo ese dato. En los avisos de salud hay muchos imperativos (traiga, toque, ve, levántate): te dicen qué hay que hacer.",
 "example": {"title": "CENTRO DE SALUD LAS ROSAS · CITA PREVIA",
   "body": "Para pedir cita con su médico de familia, llame al 965 20 30 40, de lunes a viernes, de 8:00 a 14:00. También puede pedirla a cualquier hora con la aplicación del centro de salud en su móvil. Para las urgencias no hace falta cita: venga directamente al centro. Traiga siempre su tarjeta sanitaria.",
   "q": "Para pedir cita...", "o": ["solo se puede llamar por teléfono.", "se puede usar una aplicación.", "hay que ir al centro."], "ok": 1,
   "why": "La opción correcta es la B porque también se puede pedir cita con la aplicación del centro de salud."},
 "items": [
  {"n": 6, "title": "FARMACIA DEL CARMEN · FARMACIA DE GUARDIA",
   "body": "Del lunes 13 al domingo 19 estamos de guardia: abrimos las 24 horas. Por la noche, de 22:00 a 9:00, la puerta está cerrada por seguridad: toque el timbre y le atendemos por la ventanilla. Para los medicamentos con receta, traiga su tarjeta sanitaria. Estamos en la plaza del Carmen, número 4, al lado del mercado.",
   "q": "Por la noche, en esta farmacia...", "o": ["no se puede comprar nada.", "hay que llamar al timbre.", "no hace falta la tarjeta sanitaria."], "ok": 1,
   "cats": ["salud", "imperativo"], "es": "ES-03", "pc": "LX farmacia de guardia, receta · imperativo usted (toque, traiga)",
   "why": "Por la noche hay que tocar el timbre y te atienden por la ventanilla: sí se puede comprar. La tarjeta sanitaria hace falta para los medicamentos con receta."},
  {"n": 7, "title": "YOGA GRATIS EN EL PARQUE",
   "body": "Todos los domingos de octubre, de 10:00 a 11:00, clase de yoga al aire libre en el parque del Oeste. Para todos los niveles: no necesitas experiencia. Trae tu esterilla, ropa cómoda y una botella de agua. Si llueve, no hay clase: mira el aviso en nuestra página web el sábado por la noche. ¡Relájate y respira!",
   "q": "Las clases de yoga...", "o": ["son solo para personas con experiencia.", "tienen un precio especial los domingos.", "se cancelan si hace mal tiempo."], "ok": 2,
   "cats": ["deporte", "imperativo"], "es": "ES-03", "pc": "LX deporte (yoga, esterilla) · imperativo tú (trae, mira, relájate)",
   "why": "Si llueve, no hay clase: se cancelan con mal tiempo. Son para todos los niveles y son gratis, no tienen un precio especial."},
  {"n": 8, "title": "CAMPAÑA DEL AYUNTAMIENTO · ¡MUÉVETE MÁS!",
   "body": "Pasar muchas horas sentados es malo para la salud. Por eso, te damos algunos consejos: deja el coche en casa y ve al trabajo andando o en bici; sube por las escaleras, no por el ascensor; y levántate de la silla cada hora y camina un poco. ¡Es muy bueno para el corazón y para la espalda!",
   "q": "Según la campaña, es recomendable...", "o": ["moverse un poco cada hora.", "usar el ascensor.", "ir al trabajo en coche."], "ok": 0,
   "cats": ["imperativo", "consejos"], "es": "ES-03", "pc": "imperativo (ve, sube, levántate) · dar consejos",
   "why": "La campaña dice que hay que levantarse cada hora y caminar un poco. Aconseja subir por las escaleras y dejar el coche en casa."},
  {"n": 9, "title": "FORO DE SALUD · ¿QUÉ HAGO PARA EL DOLOR DE ESPALDA?",
   "body": "Respuesta de fisio_ana:<br>Soy fisioterapeuta y veo muchos casos como el tuyo. Lo mejor para la espalda es nadar dos o tres veces por semana. Si trabajas con ordenador, pon la pantalla a la altura de los ojos y usa una buena silla. Para dormir, lo mejor es hacerlo de lado. Y si el dolor no se va en una semana, ve al médico.",
   "q": "Según Ana, para cuidar la espalda...", "o": ["es bueno dormir boca arriba.", "hay que tener la pantalla a la altura de los ojos.", "no es recomendable nadar."], "ok": 1,
   "cats": ["consejos", "cuerpo"], "es": "ES-06", "pc": "lo mejor es + infinitivo · imperativo (pon, usa, ve) · LX cuerpo",
   "why": "Ana aconseja poner la pantalla a la altura de los ojos. Lo mejor es dormir de lado, no boca arriba, y nadar es lo mejor para la espalda."},
  {"n": 10, "title": "HERBOLARIO LA SALVIA",
   "body": "Productos naturales para cuidarte: miel de tomillo para la garganta, cremas de aloe vera para la piel, champús para la caída del pelo e infusiones para dormir mejor. Este mes, dos paquetes de infusiones por el precio de uno. Y los martes, a las 18:00, taller gratuito de remedios caseros. Plazas limitadas: apúntate en la tienda.",
   "q": "En La Salvia...", "o": ["las infusiones son gratis.", "el taller es todos los días.", "para el taller hay que apuntarse antes."], "ok": 2,
   "cats": ["salud", "imperativo"], "es": "ES-04", "pc": "LX remedios naturales · imperativo con pronombre (apúntate)",
   "why": "Hay plazas limitadas y te tienes que apuntar en la tienda. Las infusiones son dos por el precio de una, no gratis, y el taller es solo los martes."},
  {"n": 11, "title": "NOTICIAS · LAS MOCHILAS DE LOS NIÑOS PESAN DEMASIADO",
   "body": "Según un estudio de un hospital de Valencia, siete de cada diez niños llevan al colegio una mochila demasiado pesada. Los médicos dicen que la mochila no debe pesar más del 10 % del peso del niño. Su consejo: llevar solo los libros necesarios, llevarla siempre en los dos hombros y, si es posible, usar una mochila con ruedas.",
   "q": "Según la noticia, los médicos aconsejan...", "o": ["llevar menos peso en la mochila.", "llevar la mochila en un solo hombro.", "no llevar mochila al colegio."], "ok": 0,
   "cats": ["consejos", "cuerpo"], "es": "ES-03", "pc": "deber + infinitivo · LX cuerpo (hombros) · porcentajes",
   "why": "Aconsejan mochilas más ligeras: que no pesen más del 10 % del peso del niño y con solo los libros necesarios. Hay que llevarla en los dos hombros."},
  {"n": 12, "title": "GIMNASIO VITAL · PRECIOS Y HORARIOS",
   "body": "Abierto de lunes a sábado, de 7:00 a 23:00, y los domingos, de 9:00 a 14:00. Cuota mensual: 35 €; estudiantes: 25 €. En octubre, la matrícula es gratis. La cuota incluye la sala de musculación y todas las clases: pilates, zumba, ciclismo... La piscina se paga aparte: 10 € al mes.",
   "q": "En el gimnasio Vital...", "o": ["la piscina está incluida en la cuota.", "los estudiantes pagan menos.", "no se puede entrenar los domingos."], "ok": 1,
   "cats": ["deporte"], "es": "ES-06", "pc": "LX deporte y gimnasio · precios y horarios",
   "why": "Los estudiantes pagan 25 € en vez de 35 €. La piscina se paga aparte, y los domingos abre de 9:00 a 14:00."},
  {"n": 13, "title": "CENTRO DE SALUD SAN ROQUE · AVISO A LOS PACIENTES",
   "body": "La doctora Ruiz está de vacaciones del 1 al 15 de agosto. Durante esos días, sus pacientes van a la consulta 5, con el doctor Molina, en el mismo horario. Para pedir cita, llamen al número de siempre. Para las urgencias de noche, vayan al hospital de la ciudad. La doctora Ruiz vuelve el lunes 18.",
   "q": "Del 1 al 15 de agosto, los pacientes de la doctora Ruiz...", "o": ["no tienen médico.", "tienen que ir siempre al hospital.", "van a otro médico."], "ok": 2,
   "cats": ["salud", "imperativo"], "es": "ES-06", "pc": "LX centro de salud (consulta, cita, urgencias) · imperativo ustedes (llamen, vayan)",
   "why": "Esos días los atiende el doctor Molina, en la consulta 5. Al hospital solo van para las urgencias de noche."},
 ]}

CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos de tres personas que hablan de lo que hacen para cuidarse. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 15 minutos. Lee primero las seis preguntas. Las tres personas hablan de deporte y de salud: busca el detalle que las separa (qué deporte, quién les da consejos, qué toman).",
 "texts": [
  {"name": "Mónica", "body": "Soy abogada y trabajo muchas horas, así que el estrés es mi gran problema. Por eso me levanto a las seis y salgo a correr media hora con mi perro antes de ir a la oficina. Es mi momento favorito del día. Hace un año dejé el café, porque me pone muy nerviosa; ahora tomo té verde por las mañanas. Al principio fue difícil, pero ahora no lo necesito. Y los fines de semana apago el móvil desde el viernes por la noche hasta el domingo: así descanso de verdad. Mi marido dice que ahora estoy mucho más tranquila y más simpática."},
  {"name": "Iván", "body": "Soy diseñador y trabajo desde casa, ocho o nueve horas al día delante del ordenador. Hace unos meses empezaron a dolerme mucho el cuello y los ojos, y fui a una fisioterapeuta. Me dio varios consejos y ahora los sigo todos: cada hora me levanto y hago estiramientos, he comprado una silla nueva y pongo la pantalla más alta. Además, los jueves juego al baloncesto con unos amigos del barrio. Lo único que todavía no he solucionado es el sueño: me cuesta mucho dormirme. Mi abuela dice que una infusión de tila es lo mejor, pero yo no la he probado."},
  {"name": "Carmen", "body": "Tengo sesenta y ocho años y estoy jubilada. Tres mañanas a la semana voy a clase de taichí en el centro de mayores de mi barrio. Es una actividad muy tranquila, pero va muy bien para el equilibrio, y a mi edad eso es importante: no quiero caerme y romperme una pierna. Por las tardes cuido a mis nietos y voy andando con ellos al parque. En mi pequeño huerto tengo tomillo, menta y romero, y con esas plantas preparo infusiones y remedios para toda la familia. Mi profesor de taichí tiene ochenta años ¡y está más en forma que yo! Mi hijo dice que soy la mejor farmacia del barrio."}],
 "items": [
  {"n": 14, "q": "¿Quién practica un deporte de equipo?", "ok": 1, "cats": ["deporte"], "es": "ES-09", "pc": "LX deportes (baloncesto, correr, taichí)",
   "why": "Iván juega al baloncesto con unos amigos los jueves. Mónica corre con su perro y Carmen hace taichí: no son deportes de equipo."},
  {"n": 15, "q": "¿Quién ha dejado de tomar una bebida?", "ok": 0, "cats": ["animo", "salud"], "es": "ES-03", "pc": "dejar de + infinitivo · estados de ánimo (me pone nerviosa)",
   "why": "Mónica dejó el café hace un año porque la pone nerviosa. Iván no ha probado la tila, pero no dice que ha dejado una bebida."},
  {"n": 16, "q": "¿Quién sigue los consejos de una profesional de la salud?", "ok": 1, "cats": ["consejos", "salud"], "es": "ES-08", "pc": "dar consejos · LX salud (fisioterapeuta)",
   "why": "Iván fue a una fisioterapeuta y sigue todos sus consejos. El consejo de la tila es de su abuela, que no es una profesional, y no lo sigue."},
  {"n": 17, "q": "¿Quién hace ejercicio para no caerse?", "ok": 2, "cats": ["deporte", "cuerpo"], "es": "ES-03", "pc": "va bien para (el equilibrio) · LX deporte y cuerpo",
   "why": "Carmen hace taichí porque va muy bien para el equilibrio y no quiere caerse."},
  {"n": 18, "q": "¿Quién prepara remedios con sus propias plantas?", "ok": 2, "cats": ["salud"], "es": "ES-09", "pc": "LX remedios naturales (infusiones, tomillo)",
   "why": "Carmen prepara infusiones y remedios con las plantas de su huerto. A Iván su abuela le recomienda una infusión, pero no habla de plantas suyas."},
  {"n": 19, "q": "¿Quién pasa algunos días sin usar el teléfono?", "ok": 0, "cats": ["animo", "consejos"], "es": "ES-03", "pc": "hábitos · estados de ánimo (más tranquila)",
   "why": "Mónica apaga el móvil desde el viernes por la noche hasta el domingo."}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un texto de un blog en el que un cocinero cuenta cómo cambió su vida después de un problema de salud. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto. Fíjate en quién hace cada cosa: Andrés, la médica, su familia, Raúl o su hermana.",
 "title": "De la cocina a la meta",
 "sub": "Blog «Cuarenta y seis años y empezando», de Andrés Molina",
 "body": [
  "Me llamo Andrés, tengo cuarenta y seis años y soy jefe de cocina en un hotel de Málaga. Hace un año y medio, un sábado de agosto, me mareé en la cocina en medio del servicio de la cena. Mis compañeros llamaron a una ambulancia y pasé la noche en el hospital. ¡Qué miedo pasé!",
  "Al día siguiente, la médica me hizo muchas preguntas: cuántas horas duermo, qué como, si hago deporte... Mis respuestas no fueron muy buenas: duermo cinco horas, como de pie y muy rápido, fumo un paquete al día y no hago nada de ejercicio. «No tiene nada grave», me dijo, «pero está muy estresado y su cuerpo le está avisando. Cambie de hábitos ya». Esa noche no pude dormir: pensé mucho en sus palabras.",
  "Lo primero fue dejar de fumar, y fue lo más difícil: las primeras semanas estuve de muy mal humor y mi familia lo pasó fatal conmigo. Pero me ayudaron mucho: mi mujer me compró chicles de menta y mi hijo pequeño me escribió una nota en la nevera: «Papá, tú puedes». Todavía está allí. Ahora, cuando veo a alguien fumando, no siento nada.",
  "Después llegó el deporte. Raúl, un compañero del hotel, me invitó a su grupo de corredores. Salen tres tardes a la semana por el paseo marítimo. El primer día solo aguanté diez minutos y al día siguiente me dolieron las piernas, los pies... ¡me dolió todo! Pero Raúl me dio un buen consejo: «Ve despacio, escucha a tu cuerpo y piensa solo en ti».",
  "También probé la meditación con una aplicación del móvil, porque me la recomendó mi hermana. No funcionó: me dormí en la primera sesión y en la segunda también. Lo dejé, y ahora, para relajarme, cocino en casa platos sencillos con mis hijos los domingos. ¡Eso sí me funciona!",
  "En mayo corrí mi primera carrera, de diez kilómetros. Tardé una hora y cinco minutos y llegué de los últimos, pero mi familia me esperó en la meta con una pancarta enorme. Fue uno de los días más felices de mi vida. Ahora duermo siete horas, he perdido ocho kilos y en el hotel he organizado un grupo para salir a caminar después del trabajo. Ya somos doce. Mis hijos dicen que ahora estoy más tranquilo y más simpático. Mi próximo objetivo es la media maratón de diciembre."],
 "items": [
  {"n": 20, "q": "Hace un año y medio, Andrés...", "o": ["se puso malo en el trabajo.", "pasó varios días en el hospital.", "llamó a una ambulancia."], "ok": 0,
   "cats": ["salud", "doler"], "es": "ES-08", "pc": "síntomas (marearse) · indefinido (U02)",
   "why": "Se mareó en la cocina durante el servicio: se puso malo en el trabajo. Solo pasó una noche en el hospital, y la ambulancia la llamaron sus compañeros."},
  {"n": 21, "q": "Según la médica, Andrés...", "o": ["tiene una enfermedad grave.", "necesita cambiar su forma de vivir.", "tiene que quedarse más días en el hospital."], "ok": 1,
   "cats": ["consejos", "imperativo"], "es": "ES-03", "pc": "imperativo usted (cambie de hábitos) · estar estresado",
   "why": "La médica le dice que cambie de hábitos ya: tiene que cambiar su forma de vivir. No tiene nada grave, y solo pasó una noche en el hospital."},
  {"n": 22, "q": "Sobre el tabaco, Andrés dice que...", "o": ["dejar de fumar fue fácil.", "todavía fuma algunos cigarros.", "su familia lo ayudó a dejarlo."], "ok": 2,
   "cats": ["animo"], "es": "ES-03", "pc": "estados de ánimo (estar de mal humor) · dejar de + infinitivo",
   "why": "Su mujer le compró chicles y su hijo le escribió una nota: su familia lo ayudó. Fue lo más difícil, y ya no fuma."},
  {"n": 23, "q": "El primer día con el grupo de corredores, Andrés...", "o": ["corrió una hora sin parar.", "no pudo correr mucho tiempo.", "corrió con su hijo por el paseo marítimo."], "ok": 1,
   "cats": ["deporte", "doler"], "es": "ES-07", "pc": "doler en pasado (me dolieron las piernas) · LX deporte",
   "why": "El primer día solo aguantó diez minutos. La hora y cinco minutos es lo que tardó en la carrera de mayo, y corre con el grupo de Raúl, no con su hijo."},
  {"n": 24, "q": "Con la meditación, Andrés...", "o": ["no tuvo buenos resultados.", "consiguió relajarse.", "solo se durmió en la primera sesión."], "ok": 0,
   "cats": ["animo", "consejos"], "es": "ES-04", "pc": "relajarse · recomendar (me la recomendó mi hermana)",
   "why": "La meditación no le funcionó: se durmió en la primera sesión y también en la segunda, y la dejó. Para relajarse, ahora cocina con sus hijos."},
  {"n": 25, "q": "Ahora Andrés...", "o": ["ya ha corrido una media maratón.", "corre con su familia los domingos.", "anima a sus compañeros a hacer ejercicio."], "ok": 2,
   "cats": ["deporte"], "es": "ES-07", "pc": "pretérito perfecto (he organizado, U06) · LX deporte",
   "why": "En el hotel ha organizado un grupo para caminar después del trabajo. La media maratón es su próximo objetivo, en diciembre, y los domingos cocina con sus hijos."},
 ]}

# ---------------- AUDITIVA ----------------
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación: las tres aparecen. Atención a las negaciones y a los cambios: «la espalda ya está bien», «correr no es bueno para usted», «tos no tengo».",
 "example": {"q": "¿Qué compra el hombre?", "o": ["unas pastillas", "un jarabe", "una crema"], "ok": 1,
   "pres": "Va a escuchar a un hombre que habla con una farmacéutica.",
   "lines": [("Hombre", "GABRIEL_ES", "Buenos días. Quería algo para la tos. Tengo mucha tos por la noche y no puedo dormir."),
             ("Mujer", "LUCIA", "¿Tiene fiebre?"),
             ("Hombre", "GABRIEL_ES", "No, fiebre no. Me duele un poco la garganta, nada más."),
             ("Mujer", "LUCIA", "Pues tome este jarabe: una cucharada después de cada comida. ¿Quiere también esta crema para los labios? Está de oferta."),
             ("Hombre", "GABRIEL_ES", "No, gracias. Y pastillas para el dolor de cabeza tengo en casa."),
             ("Mujer", "LUCIA", "Muy bien. Son seis euros con cincuenta.")],
   "solucion": "La opción correcta es la letra be. Compra un jarabe.",
   "img": "U08_CA1_0.jpg",
   "prompt": "Panel 1: a blister pack of white pills. Panel 2: a bottle of cough syrup with a measuring spoon. Panel 3: a small tube of lip cream."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Qué le duele a la mujer?", "o": ["la espalda", "el cuello", "los pies"], "ok": 1,
   "cats": ["doler", "cuerpo"], "es": "ES-05", "pc": "doler (me duele el cuello) · LX cuerpo",
   "pres": "Va a escuchar a dos amigos que hablan en un parque.",
   "lines": [("Hombre", "DAVID_M2", "[worried] ¿Qué te pasa, Irene? ¿Otra vez la espalda?"),
             ("Mujer", "SOFIA", "[in pain] Ay... No, no, la espalda ya está bien. Es el cuello: esta noche he dormido en el sofá y [groans] me duele muchísimo."),
             ("Hombre", "DAVID_M2", "¿Y los pies? Ayer caminamos mucho por la montaña."),
             ("Mujer", "SOFIA", "Los pies, nada, porque llevé las botas nuevas. [sighs] Pero el cuello... [in pain] ¡ay! No lo puedo mover."),
             ("Hombre", "DAVID_M2", "[sympathetic] Pues ponte calor. Va muy bien.")],
   "why": "Le duele el cuello porque ha dormido en el sofá. La espalda ya está bien, y los pies no le duelen.",
   "img": "U08_CA1_1.jpg", "prompt": "Panel 1: a woman holding her lower back with one hand. Panel 2: a woman holding the back of her neck with a pained face. Panel 3: a woman sitting and rubbing her bare feet."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Qué actividad va a hacer el hombre?", "o": ["natación", "correr", "yoga"], "ok": 2,
   "cats": ["deporte", "consejos"], "es": "ES-05", "pc": "dar consejos (lo mejor es, va muy bien para) · imperativo usted (empiece)",
   "pres": "Va a escuchar a un paciente que habla con su médica.",
   "lines": [("Mujer", "MIA", "Para la espalda, lo mejor es nadar. ¿Le gusta la natación?"),
             ("Hombre", "RAFA", "Es que no me gusta nada el agua, doctora. ¿Y correr? Mi hermano corre todos los días."),
             ("Mujer", "MIA", "Con sus problemas de rodilla, correr no es bueno para usted. ¿Y el yoga? Va muy bien para la espalda y para el estrés."),
             ("Hombre", "RAFA", "El yoga... Bueno, en mi barrio hay un centro. Vale, lo pruebo."),
             ("Mujer", "MIA", "Perfecto. Empiece con dos clases a la semana.")],
   "why": "Al final va a probar el yoga. No le gusta el agua, y correr no es bueno para sus rodillas.",
   "img": "U08_CA1_2.jpg", "prompt": "Panel 1: a man swimming in a pool lane. Panel 2: a man running in a park. Panel 3: a man doing a yoga pose on a mat."},
  {"n": 3, "conv": "Conversación tres", "q": "¿Qué va a tomar el chico?", "o": ["una infusión", "un vaso de leche", "un jarabe"], "ok": 0,
   "cats": ["salud", "doler"], "es": "ES-06", "pc": "doler · LX remedios (infusión, jarabe) · imperativo (tómala)",
   "pres": "Va a escuchar a una madre que habla con su hijo en casa.",
   "lines": [("Hombre", "TOMAS", "Mamá, me duele mucho la garganta."),
             ("Mujer", "RITA", "¿Tienes tos? Tengo jarabe en el armario."),
             ("Hombre", "TOMAS", "No, tos no tengo. ¿Me haces un vaso de leche con cacao?"),
             ("Mujer", "RITA", "Leche no, que con la garganta así no te va bien. Mira, te preparo una infusión de miel y limón. Tómala despacio, que está muy caliente."),
             ("Hombre", "TOMAS", "Vale... Gracias, mamá.")],
   "why": "La madre le prepara una infusión de miel y limón. No le da leche porque no le va bien para la garganta, y el jarabe es para la tos, que no tiene.",
   "img": "U08_CA1_3.jpg", "prompt": "Panel 1: a steaming cup of herbal tea with a slice of lemon and a small honey jar. Panel 2: a glass of chocolate milk. Panel 3: a bottle of cough syrup."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Dónde está la crema para el sol?", "o": ["en el baño", "en la mochila", "en la mesilla"], "ok": 2,
   "cats": ["serestar"], "es": "ES-05", "pc": "estar para la localización · OD (¿la tienes tú?)",
   "pres": "Va a escuchar a una pareja que se prepara para ir a la playa.",
   "lines": [("Mujer", "SUSANA", "Oye, ¿dónde está la crema para el sol? ¿La tienes tú?"),
             ("Hombre", "SANTIAGO_ES", "Está en el baño, ¿no? En el armario."),
             ("Mujer", "SUSANA", "No, en el baño no está, ya lo he mirado."),
             ("Hombre", "SANTIAGO_ES", "Pues en la mochila de la playa."),
             ("Mujer", "SUSANA", "Tampoco. Aquí solo están las toallas y el agua."),
             ("Hombre", "SANTIAGO_ES", "¡Ah, ya sé! Está en la mesilla, al lado de mis gafas de sol. Ayer, al volver de la playa, la dejé ahí."),
             ("Mujer", "SUSANA", "Sí, aquí está. ¡Venga, vámonos!")],
   "why": "La crema está en la mesilla, al lado de las gafas de sol. En el baño y en la mochila ya la han buscado y no está.",
   "img": "U08_CA1_4.jpg", "prompt": "Panel 1: a bathroom cabinet with toiletries on the shelves. Panel 2: a beach backpack with towels and a water bottle. Panel 3: a bedside table with a lamp and a pair of sunglasses."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Qué le pasa al hombre?", "o": ["está resfriado", "está cansado", "le duele el brazo"], "ok": 1,
   "cats": ["serestar", "animo", "doler"], "es": "ES-06", "pc": "estar + adjetivo (resfriado, cansadísimo) · doler",
   "pres": "Va a escuchar a dos compañeros de trabajo en la oficina.",
   "lines": [("Mujer", "CRISTINA", "Rubén, ¿estás bien? Tienes mala cara."),
             ("Hombre", "JAVI_ROJAS", "No es nada. Es que esta noche casi no he dormido."),
             ("Mujer", "CRISTINA", "¿Estás resfriado? En la oficina hay mucha gripe."),
             ("Hombre", "JAVI_ROJAS", "No, no, resfriado no. Es que el perro de mi vecino ladra toda la noche y estoy cansadísimo."),
             ("Mujer", "CRISTINA", "¿Y el brazo? ¿Todavía te duele?"),
             ("Hombre", "JAVI_ROJAS", "No, el brazo ya está bien, gracias.")],
   "why": "Está cansadísimo porque no ha dormido. No está resfriado, y el brazo ya no le duele.",
   "img": "U08_CA1_5.jpg", "prompt": "Panel 1: a man sneezing into a tissue. Panel 2: a tired man yawning at his office desk. Panel 3: a man holding his arm with a pained face."},
  {"n": 6, "conv": "Conversación seis", "q": "¿Qué compra la mujer?", "o": ["miel", "champú", "aceite esencial"], "ok": 0,
   "cats": ["salud"], "es": "ES-05", "pc": "LX remedios naturales (miel de tomillo, champú, aceite) · es bueno para / va bien para",
   "pres": "Va a escuchar a una mujer que habla con el dependiente de una tienda de productos naturales.",
   "lines": [("Mujer", "SARA", "Buenos días. Quería champú de tomillo. Es para la caída del pelo."),
             ("Hombre", "DIEGO", "Uy, lo siento, no nos queda. Llega el jueves."),
             ("Mujer", "SARA", "Vaya... ¿Y la miel de tomillo? ¿Es buena para la tos?"),
             ("Hombre", "DIEGO", "Sí, va muy bien para la garganta. Es de aquí, de la sierra."),
             ("Mujer", "SARA", "Pues me llevo un bote. El aceite esencial no lo necesito, que ya tengo en casa."),
             ("Hombre", "DIEGO", "Muy bien. Son ocho euros.")],
   "why": "Se lleva un bote de miel. No quedan champús hasta el jueves, y el aceite ya lo tiene en casa.",
   "img": "U08_CA1_6.jpg", "prompt": "Panel 1: a glass jar of honey. Panel 2: a bottle of shampoo. Panel 3: a small dark glass bottle of essential oil with a dropper."},
 ]}

RADIO_FX = "SONIDO 2: Short bright radio station jingle, three cheerful synth notes, clean, no voices, no background noise"
CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. En la primera escucha marca una opción; en la segunda, compruébala. Cuidado con las palabras <i>gratis</i>, <i>solo</i> y <i>todos</i>, y con los números: «seis de cada diez» es más de la mitad.",
 "example": {"q": "Según el anuncio, la vacuna de la gripe...", "o": ["es para todas las edades.", "no cuesta dinero.", "se pone en la farmacia."], "ok": 1,
   "why": "La opción correcta es la B porque la vacuna es gratis.",
   "lab": "Locutor", "voice": "MARTIN_2/RADIO",
   "text": "Campaña de vacunación contra la gripe. Si tienes más de sesenta años, vacúnate. La vacuna es gratis y te vacunan en tu centro de salud. Pide cita por teléfono o en la aplicación. Desde el quince de octubre. ¡Protégete y protege a tu familia!",
   "solucion": "La opción correcta es la letra be, porque la vacuna es gratis."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "Según el programa, para dormir mejor...", "o": ["hay que acostarse cada día a una hora distinta.", "es bueno no tener el móvil en la habitación.", "hay que quedarse en la cama si te despiertas."], "ok": 1,
   "cats": ["imperativo", "consejos"], "es": "ES-03", "pc": "imperativo tú (cena, deja, acuéstate, levántate) · es mejor + infinitivo",
   "lab": "Locutora", "voice": "CRISTINA_LAT/RADIO",
   "text": "[cheerful] Hoy, en «Vida sana», consejos para dormir mejor. Cena pronto y poco, deja el móvil fuera del dormitorio y acuéstate siempre a la misma hora. Y si te despiertas por la noche, levántate y lee un rato: es mejor que estar despierto en la cama.",
   "why": "Aconseja dejar el móvil fuera del dormitorio. Hay que acostarse siempre a la misma hora, y si te despiertas, es mejor levantarse."},
  {"n": 8, "conv": "Audio 2", "q": "La clase de pilates...", "o": ["es todos los días de la semana.", "es dos tardes a la semana.", "se puede probar sin pagar."], "ok": 2,
   "cats": ["deporte", "imperativo"], "es": "ES-03", "pc": "LX deporte (pilates, equilibrio, fortalecer) · imperativo (ven a probarla)",
   "lab": "Locutor", "voice": "MARTIN_1/RADIO",
   "text": "Gimnasio Forma presenta su nueva clase de pilates para mayores de sesenta y cinco años: martes y jueves, a las diez de la mañana. Mejora tu equilibrio y fortalece la espalda con nuestros monitores. La primera clase es gratis. ¡Ven a probarla!",
   "why": "La primera clase es gratis: se puede probar sin pagar. Es solo martes y jueves, y es por la mañana."},
  {"n": 9, "conv": "Audio 3", "q": "Según la noticia...", "o": ["más de la mitad de los españoles tiene estrés por el trabajo.", "los hombres tienen más estrés que las mujeres.", "hay que dormir más de ocho horas."], "ok": 0,
   "cats": ["animo", "consejos"], "es": "ES-04", "pc": "estar estresado · porcentajes (seis de cada diez) · recomendar + infinitivo",
   "lab": "Locutor", "voice": "CESAR/RADIO",
   "text": "[energetic] Según una encuesta nacional, seis de cada diez españoles están estresados por el trabajo, y las mujeres más que los hombres. Los expertos recomiendan hacer deporte, dormir ocho horas y pasar más tiempo con los amigos. Es el dato más alto de los últimos diez años.",
   "why": "Seis de cada diez son más de la mitad. Las mujeres tienen más estrés que los hombres, y los expertos recomiendan dormir ocho horas, no más."},
  {"n": 10, "conv": "Audio 4", "q": "En la clínica dental Sonrisa...", "o": ["los niños no pagan nada.", "la primera visita no cuesta dinero.", "hay que esperar una semana para tener cita."], "ok": 1,
   "cats": ["doler", "salud"], "es": "ES-03", "pc": "doler (te duelen las muelas) · LX salud (revisión, tratamiento)",
   "lab": "Locutora", "voice": "GABI/RADIO",
   "text": "Clínica dental Sonrisa. ¿Te duelen las muelas? Llama hoy y te vemos mañana. La primera revisión es gratis, y los niños menores de doce años tienen un veinte por ciento de descuento en todos los tratamientos. Estamos en la calle Mayor, número treinta.",
   "why": "La primera revisión es gratis. Los niños tienen un descuento, no es gratis para ellos, y te dan cita para el día siguiente."},
  {"n": 11, "conv": "Audio 5", "q": "Según el aviso, con el calor...", "o": ["es mejor salir a la calle a mediodía.", "es importante preocuparse por las personas mayores.", "solo hay que beber cuando tienes sed."], "ok": 1,
   "cats": ["imperativo", "consejos"], "es": "ES-06", "pc": "imperativo (bebe, ponte, quédate, llama) · también cuando",
   "lab": "Locutor", "voice": "EMILIO/RADIO",
   "text": "Mañana llega una ola de calor, con temperaturas de hasta cuarenta grados en el sur. Bebe mucha agua, también cuando no tienes sed, ponte ropa ligera y quédate en casa de doce a cinco. Y llama a tus vecinos mayores para saber cómo están.",
   "why": "Aconseja llamar a los vecinos mayores para saber cómo están. Hay que quedarse en casa de doce a cinco y beber también sin sed."},
  {"n": 12, "conv": "Audio 6", "q": "Según el anuncio, la aplicación Muévete...", "o": ["necesita aparatos de gimnasio.", "siempre es gratis.", "propone ejercicios cortos."], "ok": 2,
   "cats": ["deporte"], "es": "ES-06", "pc": "LX deporte y ejercicio · precios",
   "lab": "Locutor", "voice": "JUAN_CARLOS/RADIO",
   "text": "¿Quieres hacer deporte y no tienes tiempo? Descarga la aplicación Muévete. Cada día te propone diez minutos de ejercicios para hacer en casa, sin aparatos: para la espalda, las piernas y los brazos. Los primeros quince días son gratis; después, cuesta tres euros al mes.",
   "why": "Propone diez minutos de ejercicios al día: son cortos. Es sin aparatos, y solo es gratis los primeros quince días."},
 ]}
for _x in [CA2["example"]] + CA2["items"]:
    _x["sound"] = RADIO_FX

CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Nerea y Javi. Indique si los enunciados (del 13 al 18) se refieren a Nerea (A), a Javi (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Atención a quién le pasa cada cosa: si lo dice uno de los dos, pero le pasa a otra persona (la madre, la hermana...) o nadie lo va a hacer, la respuesta es C.",
 "who": ["Nerea", "Javi"], "voices": {"NEREA": "ESTELA", "JAVI": "MILO"},
 "lines": [
  ("NEREA", "¡Hola, Javi! ¡Cuánto tiempo! Oye, ¿qué te pasa? Tienes mala cara."),
  ("JAVI", "Hola, Nerea. Pues estoy fatal: me duele muchísimo la espalda. Es que paso diez horas al día delante del ordenador."),
  ("NEREA", "Vaya... ¿Y has ido al médico?"),
  ("JAVI", "Sí, ayer. Me dijo que tengo que hacer ejercicio y cambiar la silla de la oficina. Ya he comprado una nueva."),
  ("NEREA", "Pues haz yoga, ¡va muy bien para la espalda! Yo voy a clase dos veces por semana desde hace cinco meses y estoy mucho mejor. Y además duermo muy bien."),
  ("JAVI", "Ya, pero el yoga me parece un poco aburrido. Yo prefiero la natación: el lunes empiezo en la piscina de mi barrio."),
  ("NEREA", "¡Genial! Oye, ¿y tu hermana? ¿Ya está bien?"),
  ("JAVI", "¿Laura? Sí, ya está bien, ya no tiene fiebre. Ahora la que está enferma es mi madre: tiene gripe y está en la cama."),
  ("NEREA", "¡Qué pena! Dale recuerdos. Yo también estoy un poco resfriada, ¿no lo notas? Estoy casi afónica."),
  ("JAVI", "Sí, un poco. Tómate una infusión de miel y limón, es lo mejor para la garganta."),
  ("NEREA", "Sí, luego la tomo en casa. Oye, el domingo vamos a hacer una ruta por la sierra con unos amigos. ¿Te vienes?"),
  ("JAVI", "¿Es muy larga? Con esta espalda..."),
  ("NEREA", "Unas tres horas, pero es fácil. Llevamos la comida y comemos al lado del río."),
  ("JAVI", "Uf, mejor no. Este domingo descanso, y la próxima vez voy, te lo prometo."),
  ("NEREA", "Vale. ¡Que te mejores!")],
 "items": [
  {"n": 13, "q": "Tiene un problema de salud por su trabajo.", "ok": 1, "cats": ["doler", "cuerpo"], "es": "ES-03", "pc": "doler (me duele la espalda) · LX cuerpo",
   "why": "A Javi le duele la espalda porque pasa diez horas al día delante del ordenador."},
  {"n": 14, "q": "Hace una actividad física desde hace tiempo.", "ok": 0, "cats": ["deporte"], "es": "ES-07", "pc": "desde hace + tiempo · LX deporte",
   "why": "Nerea va a clase de yoga desde hace cinco meses. Javi todavía no nada: empieza el lunes."},
  {"n": 15, "q": "Está en la cama con gripe.", "ok": 2, "cats": ["salud", "serestar"], "es": "ES-08", "pc": "estar enfermo, tener gripe · ser/estar",
   "why": "La que tiene gripe y está en la cama es la madre de Javi. Su hermana ya está bien."},
  {"n": 16, "q": "Tiene problemas con la voz.", "ok": 0, "cats": ["serestar", "salud"], "es": "ES-03", "pc": "estar resfriado, afónico",
   "why": "Nerea está resfriada y casi afónica: no tiene bien la voz."},
  {"n": 17, "q": "Ya ha cambiado algo en su lugar de trabajo.", "ok": 1, "cats": ["consejos"], "es": "ES-07", "pc": "tener que + infinitivo · ya + perfecto (U06)",
   "why": "Javi ya ha comprado una silla nueva para la oficina, como le dijo el médico."},
  {"n": 18, "q": "Va a empezar clases de yoga.", "ok": 2, "cats": ["deporte", "consejos"], "es": "ES-08", "pc": "imperativo para aconsejar (haz yoga) · ir a + infinitivo",
   "why": "Nerea ya hace yoga desde hace meses, y Javi no quiere: va a empezar natación. Ninguno de los dos va a empezar yoga."}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

CH = "SONIDO 2: Two-tone ding-dong chime of a public address announcement system, clean and clear, no voices, no background noise"
BP = "SONIDO 1: Single short electronic answering machine beep, clean, no background noise"
CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. En cada mensaje pregúntate: ¿quién habla, dónde y para qué? ¿Pide un favor, da un consejo, recuerda una norma, avisa de un cambio? Sobran tres.",
 "enun": [
  "Alguien cambia la hora de una cita.",
  "Una farmacia informa de su horario.",
  "Una persona da las gracias por unos consejos.",
  "Alguien pide a otra persona que le compre algo.",
  "Se ofrece una clase gratis.",
  "Se recuerda una norma a los usuarios.",
  "Alguien no puede ir a una actividad porque está mal.",
  "Un servicio está cerrado hoy.",
  "Un centro cambia de dirección.",
  "Alguien da un consejo para un problema de salud.",
  "Hay descuentos en algunos productos."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "DAVID_CO/RADIO", "sound": BP,
   "text": "Buenos días, le llamamos del centro de salud La Paz. Su cita con la doctora Gil no es el jueves a las diez: es el jueves a las doce, porque la doctora tiene una reunión. Si no puede venir, llámenos, por favor.",
   "solucion": "La opción correcta es la letra a: alguien cambia la hora de una cita."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 6, "cats": ["doler", "cuerpo"], "es": "ES-10", "pc": "doler (me duele la rodilla) · tener que + infinitivo",
   "lab": "Contestador", "voice": "DAVID_M1/RADIO", "sound": BP,
   "text": "Hola, Pilar, soy Toni. Oye, esta tarde no voy al partido de pádel: me duele mucho la rodilla y el médico dice que tengo que descansar una semana. Lo siento mucho. ¡Suerte en el partido!",
   "why": "Toni no puede ir al partido de pádel porque le duele la rodilla."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 5, "cats": ["deporte"], "es": "ES-10", "pc": "es obligatorio, tener que + infinitivo · LX piscina",
   "lab": "Megafonía", "voice": "SANTIAGO_LAT/RADIO", "sound": CH,
   "text": "Les recordamos que en la piscina es obligatorio usar gorro y ducharse antes de entrar en el agua. Además, los niños menores de diez años tienen que estar siempre con un adulto. Muchas gracias por su colaboración.",
   "why": "En la piscina recuerdan las normas: gorro, ducha y niños con un adulto."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 3, "cats": ["imperativo", "salud"], "es": "ES-10", "pc": "pedir favores (¿me puedes comprar...?) · imperativo (pasa por casa)",
   "lab": "Contestador", "voice": "MARINA/RADIO", "sound": BP,
   "text": "Hola, cariño, soy mamá. Estoy en la cama con fiebre y no puedo salir. ¿Me puedes comprar el jarabe para la tos en la farmacia? La receta está en la mesa de la cocina. Pasa por casa esta tarde, por favor. Un beso.",
   "why": "La madre le pide a su hijo o hija que le compre un jarabe. Habla de la farmacia, pero no de su horario (B sobra)."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 10, "cats": ["salud"], "es": "ES-10", "pc": "LX salud e higiene (crema para el sol, champú, cepillo de dientes) · porcentajes",
   "lab": "Megafonía", "voice": "JAVIER/RADIO", "sound": CH,
   "text": "Atención, señores clientes: esta semana, en nuestra sección de parafarmacia, todas las cremas para el sol tienen un veinticinco por ciento de descuento. Y por cada champú, les regalamos un cepillo de dientes. Gracias por su visita.",
   "why": "En la tienda hay descuentos en las cremas para el sol y un regalo con los champús."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 4, "cats": ["deporte", "imperativo"], "es": "ES-10", "pc": "LX gimnasio · imperativo ustedes (traigan)",
   "lab": "Megafonía", "voice": "HUGO/RADIO", "sound": CH,
   "text": "Buenas tardes. Hoy a las siete, en la sala dos, empieza la nueva clase de zumba. La primera clase es gratis para todos los socios del gimnasio. Traigan agua y una toalla. ¡Les esperamos!",
   "why": "El gimnasio ofrece la primera clase de zumba gratis."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 9, "cats": ["imperativo", "consejos", "doler"], "es": "ES-10", "pc": "imperativo para aconsejar (apaga, bebe, sal) · doler",
   "lab": "Contestador", "voice": "VALENTINA/RADIO", "sound": BP,
   "text": "Hola, Sara, soy Bea. He visto tu mensaje. ¿Todavía te duele la cabeza? Mira, apaga el ordenador, bebe mucha agua y sal a caminar un poco. A mí me va muy bien. ¡Llámame luego!",
   "why": "Bea le da consejos a Sara para el dolor de cabeza. No le da las gracias a nadie (C sobra)."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 8, "cats": ["serestar", "salud"], "es": "ES-10", "pc": "estar para la localización (estamos en..., al lado de...)",
   "lab": "Contestador", "voice": "ANTONIO/RADIO", "sound": BP,
   "text": "Hola, buenas tardes, le llamamos de la clínica de fisioterapia Bienestar. Desde el lunes estamos en un local nuevo, en la avenida del Mar, número quince, al lado del mercado. El horario y el teléfono son los mismos. Hasta pronto.",
   "why": "La clínica cambia de local. El horario no cambia y no está cerrada (H sobra)."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

REPARTO = """# REPARTO DE VOCES U08 (ninguna protagonista de la U07)
# T1 conversaciones (v3, ritmo natural): 0 farmacia = LUCIA + GABRIEL_ES · 1 amigos en el parque = SOFIA (Colombia) + DAVID_M2
#   2 médica y paciente = MIA + RAFA · 3 madre e hijo = RITA + TOMAS (Argentina) · 4 pareja = SUSANA + SANTIAGO_ES
#   5 compañeros de oficina = CRISTINA + JAVI_ROJAS · 6 tienda de productos naturales = SARA + DIEGO (Argentina)
# T2 radio (perfil /RADIO, con sintonía antes de cada audio): 0 vacuna de la gripe = MARTIN_2 · 1 «Vida sana» = CRISTINA_LAT (Latinoamérica; antes CLARA: sonaba enlatada)
#   2 gimnasio = MARTIN_1 · 3 noticia del estrés = CESAR (Latinoamérica; antes LUCIA_AR: monótona) · 4 clínica dental = GABI (Argentina)
#   5 ola de calor = EMILIO · 6 aplicación = JUAN_CARLOS (Latinoamérica)
# T3 conversación entre amigos: NEREA = ESTELA · JAVI = MILO
# T4 mensajes (/RADIO): 0 contestador centro de salud = DAVID_CO (Colombia) · 1 contestador Toni = DAVID_M1
#   2 megafonía piscina = SANTIAGO_LAT · 3 contestador madre = MARINA (Argentina) · 4 megafonía parafarmacia = JAVIER
#   5 megafonía gimnasio = HUGO (Latinoamérica) · 6 contestador Bea = VALENTINA (Colombia) · 7 contestador clínica = ANTONIO (Latinoamérica)
# Efectos: sintonía de radio (T2), din-don de megafonía y pitido de contestador (T4); siempre la misma descripción (caché)"""

# ---------------- ESCRITURA ----------------
ESCRITA = {"t1": {"instr": "Una amiga le escribe porque sabe que usted está enfermo/a.",
  "input": ["¡Hola! Me ha dicho Pablo que estás enfermo. ¿Qué te pasa? ¿Ya estás mejor? El sábado es la excursión en bici que organizamos el mes pasado. ¿Vas a poder venir? Si no puedes ir en bici, puedes venir en coche con Pablo. ¡Todos queremos verte!", "Un beso,<br>Alba"],
  "lead": "Conteste a su amiga. En el correo tiene que:",
  "pautas": ["saludar;", "explicar qué le pasa y cómo se encuentra ahora;", "contar qué le ha dicho el médico o qué está haciendo para curarse;", "decir si va a ir a la excursión y por qué;", "despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Una revista de salud busca textos de sus lectores sobre cómo cuidan su salud. Escriba un texto sobre usted. Hable de:",
   "pautas": ["qué hace para cuidarse (comida, deporte, descanso);", "qué deporte o actividad practica y para qué va bien;", "cómo se siente y qué hace cuando está estresado/a o nervioso/a;", "un remedio natural o casero que usa y cómo se prepara;", "qué consejo le da a una persona que trabaja muchas horas."]},
  "op2": {"title": "Opción 2", "intro": "El mes pasado usted fue de excursión a la montaña con unos amigos. Aquí tiene tres fotos de ese día.",
   "photos": ["Por la mañana, usted y tres amigos salen de un pueblo con mochilas y bastones. Hace sol y todos están muy contentos.",
              "A mediodía, en el camino, una amiga se cae y le duele mucho el tobillo. Usted le pone una venda y otro amigo le da agua.",
              "Por la tarde, todos están en un bar del pueblo. Su amiga tiene el pie en una silla con hielo, y todos se ríen."],
   "ficha": [], "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": ["adónde fueron, con quién y cómo empezó el día;", "qué le pasó a su amiga y qué hicieron;", "cómo terminó el día y qué le pareció la excursión."],
   "img": "U08_escrita.jpg", "imgAlt": "Tres fotos de la excursión: la salida del pueblo, la amiga con el tobillo vendado y el bar del pueblo"},
  "min": 70, "max": 80}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: mi salud y mis hábitos", "pautas": ["qué hace para estar en forma;", "qué deporte practica o le gustaría practicar y para qué va bien;", "qué hace cuando está enfermo/a (un resfriado, dolor de cabeza...);", "un remedio casero o natural de su familia o de su país;", "qué consejos da para dormir bien."]},
  {"title": "Opción 2: el estrés", "pautas": ["qué cosas le ponen nervioso/a o le producen estrés;", "qué le pasa cuando está estresado/a (qué le duele, cómo se siente);", "qué hace para relajarse;", "cuántas horas usa el móvil al día y si cree que es un problema;", "qué consejos le da a una persona muy estresada."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1", "desc": "Una farmacia de barrio, una tarde de invierno. Una mujer joven con un abrigo verde y un gorro de lana estornuda delante del mostrador; lleva a su bebé en una mochila portabebés. El farmacéutico, un señor mayor con bata blanca, bigote y gafas, le enseña una caja de medicamentos. Detrás, un chico con la mano vendada espera sentado. Fuera está nevando.", "img": "U08_oral_foto1.jpg"},
  {"title": "Fotografía 2", "desc": "Una clase de yoga para mayores en un parque al lado del mar, una mañana de primavera con sol. Una monitora joven con coleta y camiseta naranja levanta los brazos y ocho personas mayores la copian sobre esterillas de colores. Un señor calvo con bigote blanco no puede levantar los brazos y se ríe. Al fondo pasa un ciclista y hay palmeras.", "img": "U08_oral_foto2.jpg"}],
  "pautas": ["las personas: cómo son, qué ropa llevan, qué están haciendo;", "el lugar: dónde están, qué tiempo hace, qué cosas hay y dónde están;", "cómo cree que están las personas (cansadas, contentas, preocupadas...) y qué les pasa;", "qué cree que van a hacer después."]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1", "intro": "Usted está resfriado/a y va a una farmacia. Hable con el farmacéutico (su profesora). Tiene que:", "pautas": ["saludar y explicar qué le pasa (qué le duele, desde cuándo);", "contestar a sus preguntas (fiebre, tos, si toma otros medicamentos...);", "preguntar cómo y cuándo tiene que tomar lo que le da;", "pagar y despedirse."]},
  {"title": "Si eligió la fotografía 2", "intro": "Usted quiere apuntarse a una clase de yoga o de pilates en el polideportivo de su barrio. Hable con el recepcionista (su profesora). Tiene que:", "pautas": ["saludar y decir qué clase le interesa;", "preguntar los días, el horario y el precio;", "explicar un pequeño problema de salud (la espalda, la rodilla...) y preguntar si puede hacer la clase;", "decidir qué clase elige, dar sus datos y despedirse."]}]}}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (mi salud y mis hábitos): ¿Qué toma cuando le duele la garganta? · ¿Qué deporte me recomienda a mí?
    Opción 2 (el estrés): ¿Qué le pasa en el cuerpo cuando está nervioso/a? · ¿Qué le recomienda a un estudiante antes de un examen?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (farmacia): ¿Qué cree que le pasa a la mujer? · ¿Y al chico del fondo?
    Foto 2 (yoga en el parque): ¿Cómo cree que se siente el señor que se ríe? · ¿Qué van a hacer después de la clase?
  Tarea 3 — su papel (aquí sí conversa: pregunte, reaccione y provoque un pequeño problema):
    Foto 1 (farmacéutico/a, de usted): pregunte «¿Qué le pasa?», «¿Desde cuándo?», «¿Tiene fiebre?» y «¿Toma
    otros medicamentos?». Ofrezca un jarabe (una cucharada cada ocho horas, 6,50 euros) y unas pastillas para el
    dolor de cabeza (3 euros). Problema: las pastillas más fuertes solo se venden con receta; recomiéndele ir al
    centro de salud si en tres días no está mejor. Dé algún consejo en imperativo: descanse, beba mucha agua.
    Foto 2 (recepcionista del polideportivo, de usted): yoga martes y jueves a las 19:00; pilates lunes y miércoles a
    las 10:00 y a las 20:00; 30 euros al mes, 20 para mayores de 65 años; la primera clase es gratis. Pregunte
    «¿Ha hecho yoga alguna vez?» y «¿Tiene algún problema de salud?». Problema: la clase de las 20:00 está completa;
    o, si dice que le duele la espalda, recomiéndele pilates (va muy bien para la espalda). Pida nombre y teléfono.
  Al reaccionar, que use doler (me duele / me duelen), tener / estar + síntoma (tengo tos, estoy mareado/a),
  preguntas de cortesía (¿Tiene algo para...?, ¿Cada cuántas horas...?) y que salude, agradezca y se despida.
  Qué mirar en esta unidad: doler con el pronombre y la concordancia (me duelen los pies); ser / estar (es
  tranquilo / está nervioso; dónde está); imperativo afirmativo al dar consejos y su posición del pronombre
  (tómalo, levántate); lo mejor es / va bien para; léxico del cuerpo, de la salud y de los estados de ánimo;
  en la descripción, está/están + gerundio y creo que van a...."""
ERRORES = """  *Yo duelo la cabeza / *Me duele mi cabeza (me duele la cabeza); *Me duele los pies (me duelen); *Le duele a ella (sobra) o
  *Ella duele (a ella le duele); *Tengo mareado (estoy mareado); *Estoy fiebre (tengo fiebre); *Soy cansado / *Soy nervioso
  hoy (estoy); *La farmacia es en la plaza (está); *Toma lo (tómalo); *Levanta te (levántate); *Hace deporte (tú: haz);
  *Pone la pantalla (tú: pon); *Ves al médico (ve); *Tomad / *Toma usted (usted: tome); *Lo mejor es que hacer deporte (lo
  mejor es hacer); *va bien por la espalda (para); *Es bueno para dormir de lado (es bueno dormir de lado)."""

# ---------------- IMÁGENES: FOTOS CON VARIEDAD REAL ----------------
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "farmacia de barrio en una tarde de invierno",
  "personas": "una clienta con su bebé y un farmacéutico (y dos clientes esperando)", "edades": "clienta de unos 30 años, bebé de unos meses, farmacéutico de unos 65, un adolescente de unos 15 y un señor de unos 80",
  "aspecto": "clienta con un abrigo de plumas verde, gorro de lana gris, nariz roja y un pañuelo de papel en la mano, con el bebé en una mochila portabebés; farmacéutico con bata blanca, pelo canoso, bigote y gafas en la punta de la nariz; adolescente en chándal con la mano vendada; señor mayor con boina y bastón",
  "espacio": "interior", "lugar": "farmacia pequeña de un barrio de ciudad, con estanterías llenas y un mostrador de madera", "momento": "tarde (ya es de noche fuera)",
  "estacion": "invierno", "tiempo": "frío; nieva fuera (se ve por el escaparate)", "gente": "bastante gente: varias personas esperan su turno",
  "accion": "el farmacéutico le enseña una caja de medicamentos a la clienta, que estornuda; el bebé duerme",
  "fondo": "el adolescente con la mano vendada espera sentado en una silla; el señor mayor se pesa en la báscula; por el escaparate se ve la cruz verde encendida y la nieve",
  "objetos": "estanterías con cajas de medicamentos, cremas, cepillos de dientes y champús; termómetros; báscula; mostrador; bolsa de papel; paquete de pañuelos; paraguas; portabebés",
  "problema": "la clienta está muy resfriada y se ha dejado la receta en casa; el farmacéutico le explica que ese medicamento necesita receta"},
 "oral_foto2": {"situacion": "clase de yoga para mayores en un parque junto al mar",
  "personas": "grupo (ocho alumnos mayores y una monitora)", "edades": "alumnos de entre 65 y 80 años y monitora de unos 25",
  "aspecto": "monitora con coleta, mallas negras y camiseta naranja; un señor calvo con bigote blanco y gafas de sol; una señora con el pelo morado; un hombre con la camiseta de su equipo de fútbol; una señora con gorra de visera y pendientes grandes; todos con ropa cómoda de deporte",
  "espacio": "exterior", "lugar": "zona de césped con palmeras al lado del paseo marítimo de una ciudad de costa", "momento": "mañana temprano",
  "estacion": "primavera", "tiempo": "sol, cielo despejado y un poco de viento", "gente": "poca gente: solo el grupo y algún paseante",
  "accion": "la monitora levanta los brazos y los alumnos la copian sobre sus esterillas; el señor del bigote no puede levantar los brazos y se ríe",
  "fondo": "un ciclista por el paseo, una mujer pasea a dos perros, el mar con un velero, un quiosco de helados cerrado",
  "objetos": "esterillas de colores, botellas de agua, toallas, una bolsa de deporte, un altavoz pequeño, bancos, palmeras, farolas",
  "problema": "una señora llega tarde y sin esterilla, y el señor del bigote tiene dolor de hombro y no puede hacer la postura"},
 "escrita": {"situacion": "excursión a la montaña con una amiga lesionada",
  "personas": "grupo de cuatro amigos (el protagonista, dos amigas y un amigo) y la camarera del bar",
  "edades": "amigos de unos 40 años",
  "aspecto": "una amiga con el pelo rizado y una gorra roja; otra con trenzas y gafas de sol; un amigo alto con barba y pañuelo al cuello; mochilas, bastones y botas de montaña",
  "espacio": "exterior e interior", "lugar": "un pueblo de montaña, un camino entre pinos y el bar del pueblo", "momento": "de la mañana a la tarde",
  "estacion": "otoño", "tiempo": "sol", "gente": "de solo el grupo (camino) a bastante gente (bar)",
  "accion": "salir del pueblo con mochilas; poner una venda en el tobillo de la amiga; descansar en el bar con el pie en alto",
  "fondo": "casas de piedra, montañas y pinos; un río pequeño; la barra del bar",
  "objetos": "mochilas, bastones, botas, botella de agua, venda, botiquín, bolsa de hielo, silla, vasos, platos de tapas",
  "problema": "una amiga se cae y se hace daño en el tobillo"},
}
SITUACIONES_USADAS = {
 "U01": ["secretaría", "librería"],
 "U02": ["taquilla de cine", "museo"],
 "U03": ["tienda de ropa", "aeropuerto"],
 "U04": ["tienda de muebles", "piso vacío en alquiler"],
 "U05": ["parada de autobús de noche", "taller de bicicletas en un pueblo"],
 "U06": ["bolera", "alquiler de kayaks en una playa"],
 "U07": ["puesto de fruta y verdura en un mercado cubierto", "terraza de un bar de tapas en un pueblo"],
 "U08": ["farmacia de barrio en una tarde de invierno", "clase de yoga para mayores en un parque junto al mar"],
}

IMG_PROMPTS = {
 "portada": "Photorealistic, candid photo of a city park in Spain on a bright spring morning: people of all ages take care of their health, a woman in her sixties jogs with headphones, a young man in a wheelchair stretches his arms, two teenage girls ride bikes, a father does push-ups while his small daughter laughs on his back, an elderly couple walks arm in arm with walking sticks; green trees, a fountain, wooden benches, soft golden light, no readable text, 16:9",
 "oral": "Photorealistic, candid photo in a small, bright language classroom in the afternoon: a teacher in her fifties with short dark hair and glasses on her head and an adult male student in his thirties with a beard and his arm in a blue sling sit face to face and talk, the student points to his shoulder as if explaining what hurts, a tablet on the table shows a drawing of the human body without readable text, a cup of herbal tea and a plant on the table, a large window, no readable text, 3:2",
 "escrita": "Photorealistic triptych, three separate photos side by side of equal size with thin white borders, the same group of four friends in their forties on a sunny autumn day in the Spanish mountains. Left: morning, they leave a small stone village with backpacks, walking poles and hiking boots, a woman with curly hair and a red cap, a woman with braids and sunglasses, a tall bearded man with a scarf, all smiling. Centre: midday on a path among pine trees next to a small river, the woman with the red cap sits on the ground holding her ankle in pain, a friend wraps a bandage around her ankle and the bearded man gives her a water bottle, a first-aid kit is open. Right: afternoon inside a cosy village bar, the woman rests her foot with an ice pack on a chair and everyone laughs around a table with glasses and plates of tapas. Candid, natural light, no readable text, 3:1",
 "oral_foto1": "Photorealistic, candid photo inside a small neighbourhood pharmacy in a Spanish city on a winter evening, dark outside and snow falling behind the shop window with a lit green cross: at the wooden counter, a young woman of about 30 with a long green puffer coat, a grey wool hat and a red nose sneezes into a tissue, carrying a sleeping baby in a baby carrier on her chest; the pharmacist, a man of about 65 with grey hair, a moustache, glasses on the tip of his nose and a white coat, shows her a medicine box; in the background a teenage boy in a tracksuit with a bandaged hand waits on a chair and an elderly man with a beret and a walking stick stands on a weighing scale; shelves full of medicine boxes, creams, toothbrushes and shampoos, thermometers, a paper bag and an umbrella; warm indoor light, no readable text, 3:2",
 "oral_foto2": "Photorealistic, candid photo of an outdoor yoga class for older people on a grassy area with palm trees next to a seafront promenade in a Spanish coastal city, early on a sunny, slightly windy spring morning with a clear blue sky: a young female instructor of about 25 with a ponytail, black leggings and an orange t-shirt raises her arms, and eight older students between 65 and 80 copy her on colourful yoga mats; a bald man with a white moustache and sunglasses cannot lift his arms and laughs; a woman with purple hair, a man in a football team shirt, a woman with a cap and big earrings; water bottles, towels, a sports bag and a small speaker on the grass; in the background a cyclist on the promenade, a woman walking two dogs, the sea with a sailing boat and a closed ice-cream kiosk; bright morning light, no readable text, 3:2",
}
IMG_DESC = {"portada": "parque por la mañana: gente de todas las edades haciendo deporte", "oral": "clase: profesora y alumno con el brazo en cabestrillo hablando", "escrita": "tres fotos: salida del pueblo, amiga con el tobillo vendado, bar del pueblo", "oral_foto1": "farmacia de barrio en invierno con nieve: clienta resfriada con bebe y farmaceutico", "oral_foto2": "yoga para mayores en un parque junto al mar en primavera"}
CA1_DESC = {0: "pastillas / jarabe / crema de labios", 1: "espalda / cuello / pies", 2: "natacion / correr / yoga", 3: "infusion / leche con cacao / jarabe", 4: "armario del baño / mochila de playa / mesilla", 5: "estornudando / bostezando / dolor de brazo", 6: "miel / champu / aceite esencial"}

LECTURA = [CL1, CL2, CL3, CL4]
AUDITIVA = [CA1, CA2, CA3, CA4]
