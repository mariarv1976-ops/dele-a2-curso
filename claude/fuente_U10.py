# -*- coding: utf-8 -*-
# FUENTE DE LA UNIDAD 10 (fase 1) · Momentos especiales
# EXAMEN COMPLETO · lectura T1+T2+T3+T4 (60 min, 25 ítems) · auditiva T1+T2+T3+T4 (40 min, 25 ítems)
U = "10"
TITLE = "Momentos especiales"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress (cambiar si se suben otro mes)
TIEMPOS = {"lectura": 60, "auditiva": 40}
RECORDATORIO = [
 "Pretérito indefinido irregular: verbos con raíz irregular (estar: estuve; tener: tuve; poder: pude; poner: puse; saber: supe; querer: quise; venir: vine; hacer: hice, hizo; haber: hubo), ser e ir (fui, fuiste, fue...) y verbos en -ir con cambio en la tercera persona (pedir: pidió, pidieron; sentir: sintió; dormir: durmió).",
 "Contraste indefinido / imperfecto: el indefinido cuenta los hechos y hace avanzar la historia; el imperfecto describe las circunstancias (la hora, el lugar, el tiempo, cómo estaban las personas). Por ejemplo: era domingo y las tiendas estaban cerradas, así que cenamos en casa.",
 "Estaba + gerundio para una acción en desarrollo cuando pasa otra cosa (estaba duchándome cuando sonó el timbre) y estuve + gerundio para un periodo cerrado (estuve estudiando toda la tarde).",
 "Marcadores para relatar: una vez, un día, el otro día, aquel día; entonces, en ese momento; luego, más tarde, poco después, al cabo de un rato; de repente; al final; al día siguiente; resulta que...",
 "Emociones: pasar / tener miedo, vergüenza, nervios; dar miedo, pena; ponerse nervioso/a, triste, contento/a, rojo/a; enfadarse, emocionarse. Para reaccionar: ¡Qué emoción! ¡Qué miedo! ¡Qué pena! ¡Qué nervios!",
 "Recuerdos y acontecimientos: recordar algo perfectamente o con todo detalle; fue un momento especial, increíble, horrible; un terremoto, un incendio, un huracán, un accidente, un descubrimiento, un invento.",
]
TIPS_INICIO = [
 "<b>Examen completo, como el día del DELE:</b> lectura 60 minutos (4 tareas, 25 preguntas) y auditiva 40 minutos (4 tareas, 25 preguntas). Reparte el tiempo de la lectura: unos 12 minutos para la tarea 1, 15 para la 2, 15 para la 3 y 18 para la 4.",
 "<b>Historias en pasado:</b> en esta unidad casi todos los textos cuentan anécdotas. Separa los hechos (lo que pasó) de las circunstancias (cómo era la situación) y sigue el orden de la historia con los marcadores. Muchas opciones falsas cuentan algo que la persona solo pensaba hacer, o algo que hizo otra persona.",
]
CATS = {
 "indefinido": {"name": "Pretérito indefinido: verbos irregulares",
  "repaso": "Verbos con raíz irregular, todos con las mismas terminaciones (-e, -iste, -o, -imos, -isteis, -ieron): estar → estuve, tener → tuve, poder → pude, poner → puse, saber → supe, querer → quise, venir → vine, hacer → hice (él hizo), haber → hubo. Ser e ir son iguales: fui, fuiste, fue, fuimos, fuisteis, fueron. Verbos en -ir con cambio solo en la tercera persona: pedir → pidió, pidieron; sentir → sintió, sintieron; dormir → durmió, durmieron. Cuidado: estuve y estuvo no llevan tilde. En el libro: unidad 10, verbos irregulares en pretérito indefinido.",
  "reto": "Escribe cinco frases sobre el último día de tus vacaciones con cinco verbos irregulares distintos (estuve, hice, pude, vine, fui...)."},
 "contraste": {"name": "Contraste indefinido / imperfecto (hechos y circunstancias)",
  "repaso": "El indefinido cuenta los hechos, lo que pasó (salí de casa, cogí el autobús, compré el pan): la historia avanza. El imperfecto describe lo que hay alrededor de esos hechos: la hora, el lugar, el tiempo, cómo eran las personas y cómo estaban (era tarde, no había nadie, estaba cansado). Por ejemplo: era domingo y las tiendas estaban cerradas, así que cenamos en casa. Con estaba + gerundio presentamos una acción en desarrollo que otra interrumpe: estaba leyendo cuando sonó el timbre. En el libro: unidad 10, contraste entre el pretérito indefinido y el imperfecto.",
  "reto": "Cuenta en seis frases tu último cumpleaños: tres circunstancias en imperfecto (dónde estabas, qué tiempo hacía, cómo te sentías) y tres hechos en indefinido."},
 "marcadores": {"name": "Marcadores para relatar y ordenar una historia",
  "repaso": "Para empezar: una vez, un día, el otro día, aquel día, resulta que... Para seguir: entonces, en ese momento, luego, más tarde, poco después, al cabo de un rato. Para algo inesperado: de repente. Para terminar: al final, al día siguiente. En el examen, busca el marcador y mira qué pasó antes y qué pasó después. En el libro: unidad 10, marcadores para relatar.",
  "reto": "Cuenta una anécdota de un viaje en cinco frases con: un día, entonces, de repente, al final y al día siguiente."},
 "emociones": {"name": "Emociones y reacciones (pasar miedo, ponerse nervioso, ¡qué vergüenza!)",
  "repaso": "Pasar / tener miedo, vergüenza, nervios; dar miedo, pena, vergüenza (me da miedo volar); ponerse nervioso/a, triste, contento/a, rojo/a; llorar, reírse, enfadarse, emocionarse; tener un ataque de risa. Para reaccionar cuando alguien te cuenta algo: ¡Qué emoción! ¡Qué miedo! ¡Qué pena! ¡Qué nervios! ¡Qué bien! En el examen, fíjate bien en quién siente cada emoción. En el libro: unidad 10, hablar de emociones y reaccionar expresando emoción.",
  "reto": "Escribe tres situaciones de tu vida: una en la que pasaste miedo, una en la que te pusiste nervioso/a y una en la que te emocionaste."},
 "recuerdos": {"name": "Recuerdos, momentos vividos y acontecimientos",
  "repaso": "Recordar algo perfectamente o con todo detalle; un recuerdo intenso; fue un momento especial, emocionante, increíble, horrible. Acontecimientos: una guerra, un terremoto, un incendio, un huracán, un accidente, un descubrimiento, un invento. Para hablar de un recuerdo: ¿Qué recuerdas de ese día? ¿Con quién estabas? En el libro: unidad 10, recuerdos y acontecimientos históricos.",
  "reto": "Elige un acontecimiento importante de tu país y escribe dónde estabas, con quién y qué hiciste aquel día."},
 "proponer": {"name": "Proponer, invitar y pedir favores",
  "repaso": "Para proponer: ¿Te apetece...?, ¿Por qué no...?, Podemos... Para invitar: Te invito a un café. Para pedir un favor: ¿Puedes llevarme al aeropuerto? En la tarea 1 de lectura y en los mensajes de la auditiva, la propuesta suele estar al final: léela con atención. En el libro: unidades anteriores (quedar, invitar, pedir favores).",
  "reto": "Escribe un mensaje a un amigo: cuéntale algo que te pasó el fin de semana y proponle quedar para hablar de ello."},
 "avisos": {"name": "Normas y condiciones en anuncios y avisos (hay que, no hace falta, está prohibido, como máximo)",
  "repaso": "En los anuncios, las palabras pequeñas cambian todo: hay que / tienes que (obligación), no hace falta (no es obligatorio), está prohibido / no se puede, como máximo / como mínimo, solo, excepto, gratis / gratuito. Lee la pregunta y busca solo esa condición en el texto. En el libro: repasa las normas y los avisos de unidades anteriores.",
  "reto": "Escribe un pequeño anuncio para un concurso de tu barrio con tres condiciones: algo que hay que hacer, algo que no hace falta y algo que está prohibido."},
}
ESTRATEGIAS_NUEVAS = {}

# ---------------- LECTURA ----------------
CL1 = {"n": 1, "type": "mail",
 "instr": "Usted va a leer el correo electrónico que Nacho ha escrito a su amiga Clara. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Nacho cuenta un día en orden: sitúa cada pregunta en su momento (el día antes, por la mañana, en la cena, ahora).",
 "head": ["De: Nacho", "Para: Clara", "Asunto: ¡Qué boda!"],
 "body": [
  "Hola, Clara:",
  "¿Qué tal? ¡Qué pena, no pudiste venir a la boda de mi hermano Álex! Te cuento cómo fue, porque fue un día increíble... y un poco horrible también.",
  "La boda fue el sábado, en el pueblo de Marta, en Asturias. Había más de cien invitados y la iglesia del pueblo estaba preciosa, llena de flores blancas. El viernes llovió todo el día y todos estábamos preocupados, pero el sábado por la mañana hacía sol y no hacía nada de frío. Por la noche, eso sí, hizo bastante fresco.",
  "Yo tenía que llevar los anillos y estaba nerviosísimo. Desayuné con mi hermano, que estaba muy tranquilo, y luego mi primo y yo fuimos a la iglesia en su coche. Pero cuando llegamos, de repente me di cuenta de que los anillos estaban en la habitación del hotel. ¡Qué miedo! Volví solo en taxi y la ceremonia empezó veinte minutos tarde. ¡Qué vergüenza! Por suerte, Álex no se enfadó: se rió.",
  "Después, en la cena, hice un discurso. Estaba muy nervioso, pero al final no tuve que mirar el papel. Conté la historia de los anillos y todos los invitados se rieron muchísimo. Mi madre lloró de emoción. Luego bailamos hasta las tres de la mañana.",
  "Ahora Álex y Marta están de viaje de novios en Grecia y vuelven dentro de dos semanas. Quiero prepararles una sorpresa: un vídeo con las fotos de la boda. Tú sabes mucho de vídeos, ¿me ayudas? ¿Quedamos el domingo en mi casa? Además, ¡hace mucho que no nos vemos!",
  "Un abrazo,<br>Nacho"],
 "items": [
  {"n": 1, "q": "Nacho escribe a Clara para...", "o": ["invitarla a la boda de su hermano.", "contarle qué pasó en una celebración familiar.", "pedirle perdón por llegar tarde."], "ok": 1,
   "cats": ["recuerdos", "marcadores"], "es": "ES-02", "pc": "FN narrar hechos pasados · indefinido (fue, llegamos, volví)",
   "why": "Nacho le cuenta cómo fue la boda de su hermano. La boda ya pasó, así que no la invita, y el que llegó tarde fue él a la iglesia, no a una cita con Clara."},
  {"n": 2, "q": "El sábado por la mañana...", "o": ["hacía buen tiempo.", "llovía mucho.", "hacía bastante frío."], "ok": 0,
   "cats": ["contraste"], "es": "ES-07", "pc": "imperfecto de circunstancia (hacía sol) · el viernes / el sábado / por la noche",
   "why": "El sábado por la mañana hacía sol y no hacía nada de frío. Llovió el viernes, y el fresco fue por la noche."},
  {"n": 3, "q": "Antes de la ceremonia, Nacho...", "o": ["desayunó solo en el hotel.", "fue a la iglesia con su hermano.", "tuvo que volver al hotel."], "ok": 2,
   "cats": ["indefinido", "marcadores"], "es": "ES-03", "pc": "indefinido (desayuné, fuimos, volví) · de repente · me di cuenta de",
   "why": "Los anillos estaban en el hotel y Nacho volvió a buscarlos en taxi. Desayunó con su hermano, no solo, y fue a la iglesia con su primo."},
  {"n": 4, "q": "Durante la cena...", "o": ["Nacho leyó su discurso en un papel.", "los invitados se rieron mucho con una historia.", "el hermano de Nacho se enfadó con él."], "ok": 1,
   "cats": ["emociones"], "es": "ES-08", "pc": "LX emociones (reírse, enfadarse, llorar de emoción) · indefinido",
   "why": "Nacho contó la historia de los anillos y los invitados se rieron muchísimo. No tuvo que mirar el papel, y su hermano no se enfadó: se rió en la iglesia."},
  {"n": 5, "q": "Nacho quiere...", "o": ["hacer un regalo a los novios con la ayuda de Clara.", "ir a Grecia con su hermano y con Marta.", "enseñarle a Clara las fotos del viaje de novios."], "ok": 0,
   "cats": ["proponer"], "es": "ES-03", "pc": "FN pedir ayuda y proponer (¿me ayudas?, ¿quedamos?)",
   "why": "Quiere preparar un vídeo de sorpresa para los novios y le pide ayuda a Clara. Los que están en Grecia son Álex y Marta, y las fotos del vídeo son de la boda, no del viaje."},
 ]}

CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 15 minutos: menos de dos minutos por anuncio. Lee la pregunta primero y busca solo ese dato. Cuidado con las palabras que limitan o niegan (solo, como máximo, no hace falta, está prohibido).",
 "example": {"title": "CAFETERÍA EL RINCÓN · NOCHE DE ANÉCDOTAS",
   "body": "Todos los jueves a las ocho de la tarde, micrófono abierto: sube al escenario y cuenta en cinco minutos tu anécdota más divertida. La entrada es libre y no hace falta reservar. Al final de cada mes, el público elige la mejor historia y su autor gana una cena para dos personas.",
   "q": "En esta cafetería, los jueves...", "o": ["hay que pagar para entrar.", "los clientes cuentan historias.", "hay conciertos de música."], "ok": 1,
   "why": "La opción correcta es la B porque los clientes suben al escenario y cuentan sus anécdotas."},
 "items": [
  {"n": 6, "title": "BIBLIOTECA MUNICIPAL · CONCURSO DE RELATOS «UN DÍA QUE NO OLVIDO»",
   "body": "¿Recuerdas un día especial de tu vida? Escribe lo que te pasó: un viaje, una fiesta, un encuentro... Solo aceptamos historias reales, de quinientas palabras como máximo. Puedes enviar tu relato por correo electrónico o dejarlo en el mostrador de la biblioteca antes del 15 de marzo. Premio: una tableta y la publicación del relato en la revista del barrio.",
   "q": "Las historias del concurso tienen que...", "o": ["ser sobre algo que pasó de verdad.", "tener más de quinientas palabras.", "contar un viaje o una fiesta."], "ok": 0,
   "cats": ["avisos", "recuerdos"], "es": "ES-03", "pc": "solo / como máximo · recordar un día especial",
   "why": "Solo aceptan historias reales: algo que pasó de verdad. Quinientas palabras es el máximo, y el viaje o la fiesta son solo ejemplos."},
  {"n": 7, "title": "FORO «MI PRIMER DÍA EN EL TRABAJO»",
   "body": "Respuesta de Lola_84:<br>El primer día en mi trabajo nuevo quería dar una buena imagen. Llegué media hora antes y saludé a todos. A las once, en la reunión, presenté mi proyecto... y en ese momento vi que llevaba la camiseta al revés. ¡Qué vergüenza! Mis compañeros no dijeron nada, pero la jefa se rió y me dijo: «Tranquila, a mí me pasó lo mismo el año pasado».",
   "q": "Lola cuenta que su primer día...", "o": ["llegó tarde a la oficina.", "llevaba la ropa mal puesta.", "sus compañeros se rieron de ella."], "ok": 1,
   "cats": ["emociones", "contraste"], "es": "ES-03", "pc": "¡Qué vergüenza! · en ese momento · llevaba (imperfecto)",
   "why": "Llevaba la camiseta al revés. Llegó media hora antes, y la que se rió fue la jefa; sus compañeros no dijeron nada."},
  {"n": 8, "title": "MUSEO DE LA CIUDAD · EXPOSICIÓN «¿DÓNDE ESTABAS TÚ?»",
   "body": "Cien fotografías de periódico de los momentos más importantes de los últimos cincuenta años: las Olimpiadas de Barcelona, la llegada del euro, el primer teléfono móvil... Al final de la visita, en nuestra cabina de vídeo, puedes grabar tu recuerdo de uno de esos días. Está prohibido hacer fotos en las salas. El catálogo se vende en la tienda del museo.",
   "q": "En esta exposición, los visitantes pueden...", "o": ["grabar un vídeo con sus recuerdos.", "hacer fotos en todas las salas.", "comprar las fotografías originales."], "ok": 0,
   "cats": ["avisos", "recuerdos"], "es": "ES-06", "pc": "está prohibido · LX acontecimientos y recuerdos",
   "why": "En la cabina de vídeo pueden grabar su recuerdo de uno de esos días. Está prohibido hacer fotos, y en la tienda se vende el catálogo, no las fotografías."},
  {"n": 9, "title": "NOTICIAS · RESCATAN A UN EXCURSIONISTA EN LA SIERRA",
   "body": "Un hombre de sesenta y tres años pasó la noche del domingo en un refugio de la sierra de Gredos. Subió a la montaña para hacer fotos, pero por la tarde empezó a nevar y no podía ver el camino. El lunes por la mañana, un perro del equipo de rescate lo encontró. El hombre está bien: no se hizo daño, solo estaba muy cansado.",
   "q": "Según la noticia, el excursionista...", "o": ["subió a la montaña con su perro.", "se hizo daño en la nieve.", "durmió fuera de su casa."], "ok": 2,
   "cats": ["indefinido", "contraste"], "es": "ES-03", "pc": "indefinido (pasó, subió, empezó) · imperfecto (no podía ver)",
   "why": "Pasó la noche en un refugio de la montaña: durmió fuera de casa. El perro era del equipo de rescate, y no se hizo daño."},
  {"n": 10, "title": "ESCUELA DE TEATRO LA ESCENA · CURSO «HABLAR SIN MIEDO»",
   "body": "¿Te pones nervioso cuando tienes que hablar delante de otras personas? ¿Te pones rojo en las reuniones? Este curso no es para actores: es para personas que quieren perder el miedo a hablar en público. No necesitas experiencia. Seis clases, los jueves de 19:00 a 20:30. La primera clase es gratis.",
   "q": "Este curso es para personas que...", "o": ["quieren trabajar como actores.", "pasan nervios al hablar delante de otros.", "ya han hecho teatro antes."], "ok": 1,
   "cats": ["emociones"], "es": "ES-03", "pc": "ponerse nervioso / rojo · pasar nervios · miedo",
   "why": "Es para personas que se ponen nerviosas al hablar delante de otras. No es para actores y no hace falta experiencia."},
  {"n": 11, "title": "ESTACIÓN DE AUTOBUSES · OFICINA DE OBJETOS PERDIDOS",
   "body": "¿Te olvidaste algo en un autobús? Guardamos los objetos perdidos durante un mes en la oficina de la planta baja, al lado de la cafetería. Para recogerlos, tienes que traer tu DNI o tu pasaporte y explicar cómo es el objeto. El servicio es gratuito y no hace falta llamar antes. Horario: de lunes a viernes, de 9:00 a 14:00.",
   "q": "Para recoger un objeto, hay que...", "o": ["llamar antes por teléfono.", "pagar una pequeña cantidad.", "llevar un documento de identidad."], "ok": 2,
   "cats": ["avisos"], "es": "ES-06", "pc": "tener que / no hace falta · gratuito",
   "why": "Hay que traer el DNI o el pasaporte. No hace falta llamar antes y el servicio es gratuito."},
  {"n": 12, "title": "BLOG «MI PRIMER CONCIERTO»",
   "body": "Entrada de Toni_rock:<br>Fue hace veinte años. Yo tenía quince años y mis padres no me dejaban ir solo a los conciertos, así que fui con mi tío Juan. Era agosto, pero esa noche llovía y hacía fresco. Cuando el grupo empezó a tocar mi canción favorita, lloré de emoción. ¡Nunca voy a olvidar ese momento!",
   "q": "Toni cuenta que en su primer concierto...", "o": ["fue sin nadie de su familia.", "se emocionó mucho.", "hacía mucho calor."], "ok": 1,
   "cats": ["emociones", "contraste"], "es": "ES-03", "pc": "llorar de emoción · imperfecto de circunstancia (llovía, hacía fresco)",
   "why": "Cuando el grupo tocó su canción favorita, lloró de emoción. Fue con su tío, y esa noche llovía y hacía fresco."},
  {"n": 13, "title": "AYUNTAMIENTO DE VILLAMAR · NOCHE DE HISTORIAS EN LA PLAZA",
   "body": "El viernes a las 21:00, los vecinos mayores del pueblo cuentan sus recuerdos: cómo eran las fiestas de antes, el año de la gran nevada, el primer coche del pueblo... Trae tu silla y escucha. Si llueve, la actividad no se cancela: se hace en el centro cultural, a la misma hora. ¡Te esperamos!",
   "q": "Si llueve, la actividad...", "o": ["se hace en otro lugar.", "se cancela.", "empieza más tarde."], "ok": 0,
   "cats": ["avisos"], "es": "ES-06", "pc": "si + presente · no se cancela · a la misma hora",
   "why": "Si llueve, se hace en el centro cultural: en otro lugar. No se cancela y es a la misma hora."},
 ]}

CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos de tres personas que hablan de un momento especial de su vida. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 15 minutos. Lee primero las seis preguntas. Las tres personas cuentan una anécdota: las preguntas dicen lo mismo con otras palabras, así que busca el sentido, no las palabras iguales.",
 "texts": [
  {"name": "Teresa", "body": "El día más emocionante de mi vida fue hace tres años, cuando nació mi primera nieta. Yo estaba en Sevilla de vacaciones con unas amigas y mi hijo me llamó a las seis de la mañana. Me vestí, cogí el primer tren a Madrid y llegué al hospital a mediodía. En el tren no podía estar tranquila: miraba el reloj todo el tiempo. Cuando vi a la niña, lloré de alegría. Era muy pequeña y tenía mucho pelo negro, como su padre de bebé. Ahora vive cerca de mi casa y voy a buscarla al colegio dos veces por semana. Todavía me emociono cada vez que veo las fotos de aquel día."},
  {"name": "Javier", "body": "Pasé muchísimo miedo hace cinco años, en un viaje por Noruega con mi mujer. Íbamos en coche por una carretera de montaña, de noche, y de repente empezó a nevar muchísimo. No se veía nada y no había nadie. Al final, el coche se paró: ¡no tenía gasolina! Yo intentaba estar tranquilo, pero mi mujer lloraba de miedo. Llamamos a emergencias, pero tardaron más de dos horas en llegar. Hacía muchísimo frío y solo teníamos una manta. Teníamos mucho miedo: no venía nadie. Por la mañana, ya en el hotel, mi mujer y yo nos reímos mucho de todo, pero aquella noche fue horrible."},
  {"name": "Paula", "body": "Mi momento más divertido fue en la boda de mi amiga Carla, hace dos años. Yo tenía que cantar una canción para los novios delante de todos los invitados. Llevaba un vestido largo y unos zapatos nuevos que me hacían mucho daño, y estaba muy nerviosa. Cuando empecé, me di cuenta de que el micrófono no funcionaba y nadie me oía. ¡Qué vergüenza! Pero entonces los invitados empezaron a cantar conmigo, muy alto. Los novios se reían y aplaudían, y yo tuve un ataque de risa. No pude terminar la canción, pero fue precioso. Desde entonces, todos los años, en su aniversario, Carla me pide la misma canción y yo la canto."}],
 "items": [
  {"n": 14, "q": "¿Quién viajó rápidamente para conocer a alguien de su familia?", "ok": 0, "cats": ["indefinido", "marcadores"], "es": "ES-03", "pc": "indefinido (me vestí, cogí, llegué) · cuando nació",
   "why": "Teresa cogió el primer tren a Madrid para conocer a su nieta recién nacida. Javier viajó con su mujer, pero de vacaciones."},
  {"n": 15, "q": "¿Quién tenía que actuar en una celebración?", "ok": 2, "cats": ["contraste"], "es": "ES-09", "pc": "tenía que + infinitivo · LX celebraciones (boda, invitados)",
   "why": "Paula tenía que cantar una canción en la boda de su amiga, delante de todos los invitados."},
  {"n": 16, "q": "¿Quién esperó ayuda durante bastante tiempo?", "ok": 1, "cats": ["indefinido"], "es": "ES-08", "pc": "indefinido (llamamos, tardaron) · más de dos horas",
   "why": "Javier llamó a emergencias y tardaron más de dos horas en llegar."},
  {"n": 17, "q": "¿Quién siente algo especial cuando mira imágenes de aquel día?", "ok": 0, "cats": ["emociones", "recuerdos"], "es": "ES-03", "pc": "emocionarse · todavía + presente · recuerdos",
   "why": "Teresa todavía se emociona cada vez que ve las fotos del día en que nació su nieta. Paula repite una canción, pero no habla de fotos."},
  {"n": 18, "q": "¿Quién tuvo un problema en una carretera?", "ok": 1, "cats": ["contraste"], "es": "ES-09", "pc": "imperfecto de circunstancia (íbamos, no se veía) · indefinido (se paró)",
   "why": "Javier iba en coche por una carretera de montaña y el coche se paró sin gasolina. Teresa viajó en tren."},
  {"n": 19, "q": "¿Quién repite cada año algo de aquel día?", "ok": 2, "cats": ["marcadores"], "es": "ES-07", "pc": "desde entonces · todos los años",
   "why": "Desde entonces, en el aniversario de su amiga, Paula canta la misma canción todos los años. Teresa va a buscar a su nieta dos veces por semana, pero eso no es algo de aquel día."}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un texto de un blog en el que un chico cuenta una anécdota de su vida. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto. Fíjate en los marcadores (una semana antes, la noche del domingo, de repente, cuando llegué, al día siguiente): te dicen en qué parte del texto está cada respuesta.",
 "title": "El día que perdí el tren (y encontré trabajo)",
 "sub": "Blog «Me pasó a mí», de Marcos Vidal",
 "body": [
  "Hace tres años yo vivía en Valencia y buscaba trabajo. Tenía veinticinco años y estaba un poco desesperado. Un día me llamaron de una agencia de viajes de Madrid: querían hacerme una entrevista el lunes a las doce. ¡Era el trabajo de mis sueños! Una semana antes compré el billete del tren de las ocho de la mañana y elegí la ropa: mi mejor camisa y unos zapatos nuevos.",
  "La noche del domingo casi no dormí: estaba nerviosísimo y pensaba todo el tiempo en las preguntas de la entrevista. A las cinco de la mañana por fin me quedé dormido... y el despertador no sonó. Cuando abrí los ojos, eran las siete y media. Me vestí en dos minutos, cogí un taxi y llegué a la estación a las ocho y dos minutos. El tren salió a su hora, a las ocho en punto. Yo lo vi desde el andén. ¡Qué horror!",
  "Llamé a la agencia y hablé con la recepcionista. Yo estaba muy nervioso, pero ella fue muy amable: «Tranquilo. Puede venir a la una». Compré otro billete para el tren de las diez.",
  "Pensaba repasar mis apuntes durante el viaje, pero no pude. A mi lado iba una señora de unos cincuenta años que leía una novela. Era una mujer muy elegante, con el pelo corto y unas gafas rojas. De repente, me preguntó: «¿Estás bien? Pareces preocupado». Yo le conté toda la historia del despertador, del taxi y del tren. Ella se rió mucho y después hablamos casi tres horas de viajes, de libros y de comida. Fue una conversación estupenda.",
  "Cuando llegué a Madrid, fui directamente a la agencia. Llegué cinco minutos antes de la una. La recepcionista me llevó al despacho de la directora, abrí la puerta... y me quedé sin palabras: ¡la directora era la señora del tren! Estaba sentada detrás de una mesa grande, con mi currículum en la mano. Me puse muy rojo. Ella sonrió y me dijo: «Bueno, Marcos, ya sé que te encanta viajar. ¿Empezamos?».",
  "La entrevista fue muy fácil: ¡ya nos conocíamos! Al día siguiente me llamaron para darme el trabajo, y desde entonces vivo en Madrid. Elena, la directora, todavía cuenta esta historia en todas las cenas de la empresa. Y yo, cuando tengo que coger un tren, ahora salgo de casa una hora antes."],
 "items": [
  {"n": 20, "q": "La noche antes de la entrevista, Marcos...", "o": ["durmió muy poco.", "compró el billete de tren.", "eligió la ropa para la entrevista."], "ok": 0,
   "cats": ["indefinido", "emociones"], "es": "ES-11", "pc": "casi no dormí · estaba nerviosísimo · una semana antes",
   "why": "La noche del domingo casi no durmió: se quedó dormido a las cinco. El billete y la ropa los preparó una semana antes."},
  {"n": 21, "q": "Marcos perdió el primer tren porque...", "o": ["el tren salió antes de su hora.", "no encontró ningún taxi.", "se despertó demasiado tarde."], "ok": 2,
   "cats": ["contraste"], "es": "ES-03", "pc": "el despertador no sonó · eran las siete y media (circunstancia)",
   "why": "El despertador no sonó y se despertó a las siete y media. El tren salió a su hora, y sí cogió un taxi."},
  {"n": 22, "q": "Cuando Marcos llamó a la agencia...", "o": ["habló con la directora.", "le dieron más tiempo para llegar.", "estaba muy tranquilo."], "ok": 1,
   "cats": ["emociones"], "es": "ES-08", "pc": "indefinido (llamé, hablé) · estaba muy nervioso",
   "why": "La recepcionista le dio una hora más: puede venir a la una, no a las doce. Habló con la recepcionista, no con la directora, y estaba muy nervioso."},
  {"n": 23, "q": "En el tren de las diez, Marcos...", "o": ["repasó sus apuntes para la entrevista.", "leyó una novela.", "habló mucho rato con otra pasajera."], "ok": 2,
   "cats": ["contraste"], "es": "ES-05", "pc": "pensaba + infinitivo, pero no pude · imperfecto (leía)",
   "why": "Habló casi tres horas con la señora que iba a su lado. Pensaba repasar sus apuntes, pero no pudo, y la que leía una novela era la señora."},
  {"n": 24, "q": "En la agencia, Marcos...", "o": ["llegó tarde otra vez.", "descubrió quién era la directora.", "vio que la directora estaba enfadada."], "ok": 1,
   "cats": ["emociones", "marcadores"], "es": "ES-11", "pc": "me quedé sin palabras · ponerse rojo · cuando llegué",
   "why": "Al abrir la puerta vio que la directora era la señora del tren. Llegó cinco minutos antes, y la directora sonrió."},
  {"n": 25, "q": "Hoy en día, Marcos...", "o": ["sale de casa con mucho tiempo cuando viaja en tren.", "cuenta la historia en las cenas de la empresa.", "vive todavía en Valencia."], "ok": 0,
   "cats": ["marcadores"], "es": "ES-08", "pc": "desde entonces · ahora · todavía",
   "why": "Ahora sale de casa una hora antes cuando tiene que coger un tren. La que cuenta la historia en las cenas es Elena, y desde entonces vive en Madrid."},
 ]}

# ---------------- AUDITIVA ----------------
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación: las tres aparecen. Las personas cuentan algo que pasó: escucha hasta el final, porque muchas veces primero dicen lo que querían hacer o lo que no pasó.",
 "example": {"q": "¿Qué perdió la mujer?", "o": ["un pasaporte", "un móvil", "una maleta"], "ok": 1,
   "pres": "Va a escuchar a una mujer que habla con un amigo de su viaje.",
   "lines": [("Mujer", "RITA", "[exhausted] ¡Hola, Pedro! Ya estoy en casa... [sighs] ¡Qué viaje tan horrible!"),
             ("Hombre", "TOMAS", "[surprised] ¿Por qué? ¿Qué te pasó?"),
             ("Mujer", "RITA", "[nervous] Pues en el aeropuerto de Roma no encontraba el pasaporte. ¡Qué nervios! [laughs] Al final estaba en el fondo del bolso."),
             ("Hombre", "TOMAS", "[relieved] ¡Menos mal!"),
             ("Mujer", "RITA", "[frustrated] Sí, pero luego me dejé el móvil en el avión, en el asiento. Ya no lo tengo."),
             ("Hombre", "TOMAS", "[sympathetic] ¡Vaya! ¿Y la maleta?"),
             ("Mujer", "RITA", "[laughs] La maleta llegó bien, eso sí.")],
   "solucion": "La opción correcta es la letra be. Perdió el móvil.",
   "img": "U10_CA1_0.jpg",
   "prompt": "Panel 1: a passport. Panel 2: a smartphone. Panel 3: a suitcase."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Dónde estaba el hombre cuando empezó la tormenta?", "o": ["en la playa", "en el coche", "en un restaurante"], "ok": 2,
   "cats": ["contraste"], "es": "ES-07", "pc": "mientras comíamos (imperfecto) + empezó (indefinido)",
   "pres": "Va a escuchar a dos compañeros de trabajo el lunes por la mañana.",
   "lines": [("Mujer", "SUSANA", "[cheerful] ¿Qué tal el fin de semana, Luis?"),
             ("Hombre", "GABRIEL_ES", "[excited] Pues mira, el sábado fuimos a la playa. ¡Hacía un sol increíble y nos bañamos toda la mañana!"),
             ("Mujer", "SUSANA", "[happy] ¡Qué bien!"),
             ("Hombre", "GABRIEL_ES", "[sighs] Sí, pero a las tres nos fuimos a comer a un restaurante del puerto y, mientras comíamos... [dramatic] ¡de repente empezó una tormenta enorme!"),
             ("Mujer", "SUSANA", "[laughs] ¡Vaya! ¿Y el coche?"),
             ("Hombre", "GABRIEL_ES", "[frustrated] Estaba en el aparcamiento con las ventanillas abiertas. [laughs] ¡Todo mojado!")],
   "why": "Mientras comían en el restaurante del puerto, empezó la tormenta. En la playa estuvieron por la mañana, y el coche estaba en el aparcamiento.",
   "img": "U10_CA1_1.jpg", "prompt": "Panel 1: a sunny beach with a towel and an umbrella. Panel 2: a car in a car park with its windows open. Panel 3: a seafood restaurant by a harbour with a table and plates."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Qué le regalaron a la mujer por su cumpleaños?", "o": ["una bicicleta", "un viaje", "un perro"], "ok": 1,
   "cats": ["indefinido"], "es": "ES-04", "pc": "indefinido (hicieron, regalaron, vino) · ¡Qué emoción!",
   "pres": "Va a escuchar a una mujer que habla con un amigo.",
   "lines": [("Hombre", "DAVID_CO", "[curious] Oye, Marta, ¿qué tal tu cumpleaños?"),
             ("Mujer", "VALENTINA", "[excited] ¡Genial! Mis amigos me hicieron una fiesta sorpresa. Cuando abrí la puerta de casa, ¡estaban todos allí! ¡Qué emoción!"),
             ("Hombre", "DAVID_CO", "[curious] ¿Y qué te regalaron? ¿La bicicleta que querías?"),
             ("Mujer", "VALENTINA", "[laughs] No, la bicicleta ya la compré yo en verano. [excited] ¡Me regalaron un viaje a Lisboa para dos personas!"),
             ("Hombre", "DAVID_CO", "[impressed] ¡Qué bien!"),
             ("Mujer", "VALENTINA", "[happy] Y mi hermana vino con su perro nuevo. ¡Es precioso!")],
   "why": "Le regalaron un viaje a Lisboa. La bicicleta la compró ella en verano, y el perro es de su hermana.",
   "img": "U10_CA1_2.jpg", "prompt": "Panel 1: a new bicycle with a ribbon. Panel 2: two plane tickets in an envelope with a small picture of a tram. Panel 3: a small cute dog."},
  {"n": 3, "conv": "Conversación tres", "q": "¿Qué pasó cuando el hombre vio al actor?", "o": ["se hicieron una foto", "el actor le firmó un autógrafo", "se dieron la mano"], "ok": 2,
   "cats": ["emociones"], "es": "ES-05", "pc": "quería + infinitivo, pero... · al final · ponerse rojo",
   "pres": "Va a escuchar a un hombre que cuenta algo a una amiga.",
   "lines": [("Hombre", "MARTIN_3", "[excited] ¿Sabes a quién vi ayer en el supermercado? ¡A Javier Ruiz, el actor!"),
             ("Mujer", "MIA", "[surprised] ¡No me digas! ¿Y le pediste un autógrafo?"),
             ("Hombre", "MARTIN_3", "[embarrassed] No, mi hermana ya tiene uno. Yo quería una foto con él, pero... estaba muy nervioso y no pude decir nada."),
             ("Mujer", "MIA", "[laughs] ¡Qué vergüenza!"),
             ("Hombre", "MARTIN_3", "[laughs] Al final él me dio la mano y me dijo: «Hola, ¿qué tal?». [embarrassed] Y yo me puse rojo.")],
   "why": "Al final el actor le dio la mano. Quería una foto, pero no pudo decir nada, y el autógrafo es de su hermana.",
   "img": "U10_CA1_3.jpg", "prompt": "Panel 1: two men taking a selfie together with a phone. Panel 2: a man signing an autograph on a small notebook for another man. Panel 3: two men shaking hands in a supermarket aisle."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Qué rompió la mujer?", "o": ["un plato", "una lámpara", "una botella"], "ok": 0,
   "cats": ["contraste"], "es": "ES-04", "pc": "cuando llevaba (imperfecto) + tropecé, rompí (indefinido)",
   "pres": "Va a escuchar a una mujer que habla con un amigo sobre una cena.",
   "lines": [("Hombre", "JUAN_RESTREPO", "[curious] ¿Qué tal la cena en casa de los padres de tu novio?"),
             ("Mujer", "SOFIA", "[sighs] ¡Ay, horrible! Yo estaba muy nerviosa. Ellos abrieron una botella de vino buenísima y la comida estaba riquísima..."),
             ("Hombre", "JUAN_RESTREPO", "[curious] ¿Entonces?"),
             ("Mujer", "SOFIA", "[embarrassed] Pues al final, cuando llevaba el café a la mesa, tropecé y... ¡rompí un plato antiguo de su madre! Y la lámpara del salón se movió, pero no se rompió."),
             ("Hombre", "JUAN_RESTREPO", "[gasps] ¡Qué vergüenza!"),
             ("Mujer", "SOFIA", "[laughs] Sí... Pero su madre se rió mucho.")],
   "why": "Rompió un plato antiguo de la madre de su novio. La lámpara se movió, pero no se rompió, y la botella de vino la abrieron sus padres.",
   "img": "U10_CA1_4.jpg", "prompt": "Panel 1: a broken plate on the floor. Panel 2: a ceiling lamp in a living room. Panel 3: a bottle of red wine."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Cómo volvió el hombre a casa el día de la nevada?", "o": ["en taxi", "a pie", "en bicicleta"], "ok": 1,
   "cats": ["marcadores"], "es": "ES-05", "pc": "primero... al final · no había autobuses (circunstancia)",
   "pres": "Va a escuchar a un hombre y a una mujer que hablan de un día de mucha nieve.",
   "lines": [("Mujer", "MARINA", "[curious] Oye, Andrés, ¿y tú cómo volviste a casa el día de la nevada? ¡No había autobuses!"),
             ("Hombre", "DIEGO", "[sighs] Uf, primero llamé a un taxi, pero no vino ninguno. Esperé casi una hora."),
             ("Mujer", "MARINA", "[curious] ¿Y entonces?"),
             ("Hombre", "DIEGO", "Una compañera me ofreció su bicicleta, pero con tanta nieve... [laughs] Al final volví andando. Tardé dos horas y llegué congelado."),
             ("Mujer", "MARINA", "[sympathetic] ¡Pobre! Yo me quedé a dormir en casa de mi hermana, que vive al lado de la oficina.")],
   "why": "Al final volvió andando, en dos horas. El taxi no llegó, y la bicicleta de su compañera no la usó por la nieve.",
   "img": "U10_CA1_5.jpg", "prompt": "Panel 1: a taxi on a snowy street. Panel 2: a man walking in the snow with a scarf. Panel 3: a bicycle covered in snow."},
  {"n": 6, "conv": "Conversación seis", "q": "¿Dónde conoció la mujer a su pareja?", "o": ["en una boda", "en un gimnasio", "en un tren"], "ok": 0,
   "cats": ["indefinido"], "es": "ES-08", "pc": "indefinido (conocí, tiró, volvimos) · ahora / hace cuatro años",
   "pres": "Va a escuchar a una mujer que cuenta a un compañero cómo conoció a su pareja.",
   "lines": [("Hombre", "ALEJANDRO", "[curious] Oye, Laura, ¿tú cómo conociste a Manuel? ¿En el gimnasio?"),
             ("Mujer", "CRISTINA", "[laughs] No, no. Ahora vamos juntos al gimnasio, pero lo conocí hace cuatro años, en la boda de mi prima."),
             ("Hombre", "ALEJANDRO", "[warmly] ¡Qué romántico!"),
             ("Mujer", "CRISTINA", "[laughs] ¡Qué va! Estaba sentado a mi lado y me tiró una copa de vino en el vestido. ¡El pobre pasó mucha vergüenza! Luego volvimos a Madrid en el mismo tren y hablamos durante tres horas."),
             ("Hombre", "ALEJANDRO", "[amused] ¡Qué historia!")],
   "why": "Lo conoció en la boda de su prima. Al gimnasio van juntos ahora, y en el tren volvieron a Madrid después de conocerse.",
   "img": "U10_CA1_6.jpg", "prompt": "Panel 1: a wedding reception with a round table and a wedding cake. Panel 2: a gym with exercise machines. Panel 3: the inside of a train with seats and a window."},
 ]}

RADIO_FX = "SONIDO 2: Short bright radio station jingle, three cheerful synth notes, clean, no voices, no background noise"
CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. En la primera escucha marca una opción; en la segunda, compruébala. Cuidado con los datos que aparecen pero no responden a la pregunta: otro día, otra persona u otro lugar.",
 "example": {"q": "En este programa, los oyentes...", "o": ["cuentan historias divertidas.", "hablan con actores de teatro.", "compran entradas para el teatro."], "ok": 0,
   "why": "La opción correcta es la A porque los oyentes llaman y cuentan sus anécdotas.",
   "lab": "Locutor", "voice": "EMILIO/RADIO",
   "text": "[enthusiastic] ¿Tienes una anécdota divertida de tus vacaciones? Llámanos y cuéntanos tu historia en «Tarde de anécdotas», de lunes a viernes, a las cinco. Cada semana, los oyentes eligen la historia más divertida y su autor gana dos entradas para el teatro.",
   "solucion": "La opción correcta es la letra a, porque los oyentes llaman y cuentan sus anécdotas."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "Según la noticia...", "o": ["los bomberos tardaron tres horas en llegar.", "ayer muchas personas estuvieron sin electricidad.", "hoy los ascensores todavía no funcionan."], "ok": 1,
   "cats": ["recuerdos"], "es": "ES-03", "pc": "hubo (indefinido de haber) · LX acontecimientos (un apagón)",
   "lab": "Locutora", "voice": "LUCIA/RADIO",
   "text": "Ayer por la tarde hubo un apagón en el centro de la ciudad. Durante tres horas no hubo luz en muchas casas, tiendas y oficinas. Algunas personas se quedaron en los ascensores y los bomberos fueron a ayudarlas. Hoy todo funciona con normalidad.",
   "why": "Durante tres horas no hubo luz en muchas casas, tiendas y oficinas. Tres horas es lo que duró el apagón, no lo que tardaron los bomberos, y hoy todo funciona."},
  {"n": 8, "conv": "Audio 2", "q": "Este mes, el estudio de fotografía...", "o": ["da el vídeo gratis con las fotos de boda.", "solo hace fotos de bodas.", "hace descuentos en los cumpleaños."], "ok": 0,
   "cats": ["avisos"], "es": "ES-06", "pc": "si + presente · gratis · LX celebraciones",
   "lab": "Locutor", "voice": "JAVIER/RADIO",
   "text": "[warmly] Estudio de fotografía Momentos. Bodas, cumpleaños, comuniones... Guardamos para siempre tus días más especiales. Y este mes tenemos una oferta: si reservas las fotos de tu boda, el vídeo es gratis. Ven a vernos a la calle Mayor, número doce.",
   "why": "Si reservas las fotos de la boda, el vídeo es gratis. También hacen fotos de cumpleaños y comuniones, pero la oferta es solo para las bodas."},
  {"n": 9, "conv": "Audio 3", "q": "El programa invita a los oyentes a...", "o": ["ver la llegada a la Luna en la televisión.", "hablar de la caída del muro de Berlín.", "contar sus recuerdos de un día histórico."], "ok": 2,
   "cats": ["recuerdos"], "es": "ES-07", "pc": "¿Dónde estabas tú? · LX acontecimientos históricos · hoy / mañana",
   "lab": "Locutora", "voice": "SARA/RADIO",
   "text": "[warmly] Hoy, en «Tal día como hoy», recordamos el veinte de julio de mil novecientos sesenta y nueve, el día que el primer hombre llegó a la Luna. ¿Dónde estabas tú? ¿Lo viste en la televisión? Llámanos y cuéntanos tus recuerdos. Mañana hablamos de la caída del muro de Berlín.",
   "why": "Piden a los oyentes que llamen y cuenten sus recuerdos de la llegada a la Luna. En la televisión la gente lo vio en mil novecientos sesenta y nueve, y del muro de Berlín hablan mañana."},
  {"n": 10, "conv": "Audio 4", "q": "Según la noticia, el abuelo...", "o": ["hizo el camino solo.", "se emocionó mucho al terminar.", "empezó el camino en Santiago."], "ok": 1,
   "cats": ["emociones"], "es": "ES-03", "pc": "llorar de emoción · indefinido (terminó, empezó, caminaron)",
   "lab": "Locutor", "voice": "LUIS_GUILLERMO/RADIO",
   "text": "Ramón Pardo tiene ochenta y un años y ayer terminó el Camino de Santiago. Empezó en León hace un mes con su nieto Daniel, de veinte años. Caminaron más de trescientos kilómetros. [warmly] Al llegar a la catedral de Santiago, Ramón lloró de emoción: «Es el mejor regalo de mi vida», dijo.",
   "why": "Al llegar a la catedral, lloró de emoción. Hizo el camino con su nieto y empezó en León."},
  {"n": 11, "conv": "Audio 5", "q": "Según el anuncio...", "o": ["no pueden jugar los niños de diez años.", "los grupos son de más de seis personas.", "los martes la entrada es gratis."], "ok": 0,
   "cats": ["avisos"], "es": "ES-06", "pc": "no pueden entrar menores de... · de dos a seis · dos por el precio de una",
   "lab": "Locutor", "voice": "HUGO/RADIO",
   "text": "[mysterious] ¿Te gusta pasar miedo? [excited] Ven a «La casa del miedo», el nuevo escape room del barrio de Triana. Tienes sesenta minutos para salir de una casa misteriosa. Para grupos de dos a seis personas. No pueden entrar menores de catorce años. ¡Y los martes, dos entradas por el precio de una!",
   "why": "No pueden entrar menores de catorce años, así que un niño de diez no puede jugar. Los grupos son de dos a seis, y los martes hay dos entradas por el precio de una, no gratis."},
  {"n": 12, "conv": "Audio 6", "q": "La cantante cuenta que en su primer concierto...", "o": ["estaba muy tranquila.", "cantó en las fiestas de otro pueblo.", "el público la ayudó."], "ok": 2,
   "cats": ["emociones", "contraste"], "es": "ES-03", "pc": "estaba muy nerviosa (circunstancia) + se olvidó (hecho) · entonces",
   "lab": "Locutor", "voice": "MARTIN_1/RADIO",
   "text": "[warmly] Esta semana, en «Vidas», la cantante Rosa Llamas nos cuenta su primer concierto. Fue en las fiestas de su pueblo, con dieciséis años. Estaba muy nerviosa y, en la primera canción, se olvidó de la letra. Entonces el público empezó a cantar con ella. [excited] ¡Un momento inolvidable!",
   "why": "Cuando se olvidó de la letra, el público cantó con ella. Estaba muy nerviosa, y el concierto fue en las fiestas de su pueblo."},
 ]}
for _x in [CA2["example"]] + CA2["items"]:
    _x["sound"] = RADIO_FX

CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Elena y Pablo. Indique si los enunciados (del 13 al 18) se refieren a Elena (A), a Pablo (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Elena y Pablo se cuentan lo que les pasó estos días. Las frases van en el orden de la conversación. Si algo lo hace otra persona de la que hablan, la respuesta es C.",
 "who": ["Elena", "Pablo"], "voices": {"ELENA": "ESTELA", "PABLO": "MILO"},
 "lines": [
  ("PABLO", "[curious] ¡Hola, Elena! ¿Qué te pasa? Pareces cansada."),
  ("ELENA", "[sighs] Uf, es que ayer tuve un día horrible. Por la mañana fui a la oficina en bici, como siempre, y de repente... ¡empezó a llover muchísimo! [frustrated] ¡Llegué completamente mojada!"),
  ("PABLO", "[sympathetic] ¡Qué mala suerte!"),
  ("ELENA", "Y en la oficina no tenía ropa para cambiarme, así que estuve toda la mañana con frío."),
  ("PABLO", "[sympathetic] ¡Pobre!"),
  ("ELENA", "[frustrated] Y eso no es todo. Por la tarde, cuando volví a casa, no encontraba las llaves. Estuve una hora sentada en la escalera hasta que llegó mi compañera de piso. [laughs] Al final, las llaves estaban en la bolsa del gimnasio."),
  ("PABLO", "[laughs] ¡Qué horror! Pues yo también tengo una historia. ¿Te acuerdas de que el sábado era la boda de mi hermano Raúl?"),
  ("ELENA", "[excited] ¡Claro! ¿Qué tal fue?"),
  ("PABLO", "[warmly] Muy bonita. Yo tenía que leer un poema en la ceremonia, pero cuando empecé, me emocioné y me puse a llorar. [laughs] No pude terminar."),
  ("ELENA", "[touched] ¡Ay, qué bonito! ¿Y quién lo terminó?"),
  ("PABLO", "[laughs] Mi madre. Ella estaba mucho más tranquila que yo. Pero después, en la fiesta, todo el mundo me dijo: «¡Qué poema tan bonito!»."),
  ("ELENA", "[laughs] ¡Qué familia! ¿Y adónde van de viaje de novios?"),
  ("PABLO", "Raúl y Ana se van a Japón el mes que viene. [sighs] Yo quería ir a Japón el año pasado, pero al final no fui porque no tenía dinero."),
  ("ELENA", "[excited] Pues yo estuve allí hace dos años, en primavera. ¡Me encantó!"),
  ("PABLO", "[excited] ¿Ah, sí? Pues tienes que enseñarme las fotos."),
  ("ELENA", "[cheerful] Vale. ¿Quedamos mañana en mi casa?"),
  ("PABLO", "[happy] ¡Perfecto!")],
 "items": [
  {"n": 13, "q": "Se mojó de camino al trabajo.", "ok": 0, "cats": ["contraste"], "es": "ES-08", "pc": "fui (indefinido) · de repente empezó a llover",
   "why": "Elena fue a la oficina en bici y empezó a llover muchísimo: llegó mojada."},
  {"n": 14, "q": "Esperó mucho tiempo para poder entrar en su casa.", "ok": 0, "cats": ["contraste"], "es": "ES-03", "pc": "no encontraba (imperfecto) · estuve una hora (indefinido)",
   "why": "Elena no encontraba las llaves y estuvo una hora sentada en la escalera hasta que llegó su compañera de piso."},
  {"n": 15, "q": "Lloró en una celebración familiar.", "ok": 1, "cats": ["emociones"], "es": "ES-08", "pc": "emocionarse · ponerse a llorar · LX celebraciones",
   "why": "En la boda de su hermano, Pablo se emocionó y se puso a llorar."},
  {"n": 16, "q": "Terminó de leer un poema.", "ok": 2, "cats": ["indefinido"], "es": "ES-08", "pc": "indefinido (no pude terminar, lo terminó)",
   "why": "Pablo no pudo terminar el poema: lo terminó su madre."},
  {"n": 17, "q": "Se va de viaje de novios.", "ok": 2, "cats": ["marcadores"], "es": "ES-07", "pc": "presente con valor de futuro · el mes que viene",
   "why": "Los que se van de viaje de novios a Japón son Raúl y Ana, el hermano de Pablo y su mujer."},
  {"n": 18, "q": "Quería viajar a un país, pero no pudo ir.", "ok": 1, "cats": ["contraste"], "es": "ES-05", "pc": "quería (imperfecto) + al final no fui (indefinido) · porque no tenía dinero",
   "why": "Pablo quería ir a Japón el año pasado, pero no fue porque no tenía dinero. Elena sí estuvo allí hace dos años."}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

CH = "SONIDO 2: Two-tone ding-dong chime of a public address announcement system, clean and clear, no voices, no background noise"
BP = "SONIDO 1: Single short electronic answering machine beep, clean, no background noise"
CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. En cada mensaje pregúntate: ¿quién habla, dónde y para qué? ¿Cuenta una noticia, da las gracias, invita, pregunta algo, avisa de un cambio? Sobran tres.",
 "enun": [
  "Alguien pide perdón por algo que pasó.",
  "Alguien cuenta una buena noticia.",
  "Se han encontrado unos objetos olvidados.",
  "Alguien invita a una celebración.",
  "Un vuelo sale más tarde por el mal tiempo.",
  "Alguien da las gracias por una ayuda.",
  "Un espectáculo empieza más tarde.",
  "Alguien pregunta qué pasó en una reunión.",
  "Los clientes tienen que salir de un edificio.",
  "Un niño espera a su familia en un lugar.",
  "Alguien cuenta un viaje con problemas."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "GABI/RADIO", "sound": BP,
   "text": "[embarrassed] Hola, Sara, soy Irene. Perdona por lo de anoche: llegué muy tarde a tu cena porque me quedé dormida en el sofá. ¡Qué vergüenza! Mañana te invito a comer, ¿vale? Un beso.",
   "solucion": "La opción correcta es la letra a: alguien pide perdón por algo que pasó."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 4, "cats": ["avisos"], "es": "ES-10", "pc": "megafonía · por la niebla · retraso",
   "lab": "Megafonía", "voice": "MARTIN_2/RADIO", "sound": CH,
   "text": "Atención, por favor. Por la niebla, el vuelo con destino Bilbao, con salida a las diez y cuarto, tiene un retraso de una hora y media. La nueva hora de salida es a las once y tres cuartos, por la puerta doce. Gracias por su paciencia.",
   "why": "El vuelo a Bilbao sale con una hora y media de retraso por la niebla. La G también habla de algo que empieza más tarde, pero es un espectáculo."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 1, "cats": ["emociones"], "es": "ES-10", "pc": "pretérito perfecto (me han dado) · estar contentísima",
   "lab": "Contestador", "voice": "LUISA/RADIO", "sound": BP,
   "text": "[excited] Hola, mamá, soy Andrea. ¿Sabes qué? ¡Me han dado el trabajo en el hospital! Empiezo el lunes que viene. Estoy contentísima. Esta noche te llamo y te cuento todo. ¡Un beso muy fuerte!",
   "why": "Andrea le cuenta a su madre que le han dado el trabajo: es una buena noticia."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 9, "cats": ["avisos"], "es": "ES-10", "pc": "megafonía · está esperando a sus padres",
   "lab": "Megafonía", "voice": "SANTIAGO_LAT/RADIO", "sound": CH,
   "text": "Atención, señores clientes: en el punto de información de la planta baja está Hugo, un niño de unos cinco años, con una camiseta roja y una gorra azul. Hugo está esperando a sus padres. Muchas gracias.",
   "why": "Hugo, un niño de cinco años, espera a sus padres en el punto de información. No se habla de objetos olvidados (C sobra)."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 5, "cats": ["indefinido"], "es": "ES-10", "pc": "dar las gracias por + infinitivo · indefinido (ayudaste, trabajaste)",
   "lab": "Contestador", "voice": "CRISTIAN/RADIO", "sound": BP,
   "text": "[warmly] Hola, Tomás, soy Rafa. Te llamo para darte las gracias por ayudarme ayer con la mudanza. Tú trabajaste más que nadie. Ya tengo todo en el piso nuevo. La próxima vez, te ayudo yo. ¡Un abrazo!",
   "why": "Rafa le da las gracias a Tomás por ayudarle con la mudanza."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 6, "cats": ["avisos"], "es": "ES-10", "pc": "megafonía · por un problema técnico · y no a las nueve",
   "lab": "Megafonía", "voice": "DAVID_M1/RADIO", "sound": CH,
   "text": "Señoras y señores, por un problema técnico con las luces, la función de esta noche empieza a las nueve y cuarto, y no a las nueve. Pueden esperar en el bar del teatro. Muchas gracias.",
   "why": "La función del teatro empieza un cuarto de hora más tarde por un problema técnico, no por el mal tiempo (E). Nadie tiene que salir del edificio (I sobra)."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 3, "cats": ["proponer"], "es": "ES-10", "pc": "FN invitar (¿vienes?) · presente con valor de futuro",
   "lab": "Contestador", "voice": "SUSANA/RADIO", "sound": BP,
   "text": "[excited] Hola, Jorge, soy Carmen. El viernes cumplo cuarenta años y hago una fiesta en mi casa a las nueve de la noche. ¿Vienes? Y trae a tu novia, por favor. ¡Va a ser genial!",
   "why": "Carmen invita a Jorge a la fiesta de su cumpleaños."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 7, "cats": ["indefinido"], "es": "ES-10", "pc": "indefinido (no pude ir, decidisteis) · estaba enfermo",
   "lab": "Contestador", "voice": "JAVI_ROJAS/RADIO", "sound": BP,
   "text": "[curious] Hola, Pilar, soy Luis, el vecino del tercero. Ayer no pude ir a la reunión de la comunidad porque estaba enfermo. ¿Qué decidisteis al final? ¿Vamos a pintar la escalera? Llámame esta tarde, por favor. Gracias.",
   "why": "Luis no fue a la reunión de vecinos y pregunta qué decidieron. Nadie cuenta un viaje con problemas (K sobra)."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

REPARTO = """# REPARTO DE VOCES U10 (ninguna protagonista de la U09)
# T1 conversaciones (v3, con marcas de emoción): 0 mujer y amigo, viaje = RITA (Argentina) + TOMAS (Argentina)
#   1 compañeros de trabajo, tormenta = SUSANA + GABRIEL_ES · 2 cumpleaños = VALENTINA (Colombia) + DAVID_CO (Colombia)
#   3 el actor = MARTIN_3 + MIA · 4 cena con los suegros = SOFIA (Colombia) + JUAN_RESTREPO (Colombia)
#   5 la nevada = MARINA (Argentina) + DIEGO (Argentina) · 6 cómo conoció a su pareja = CRISTINA + ALEJANDRO (México)
# T2 radio (perfil /RADIO, con sintonía antes de cada audio): 0 «Tarde de anécdotas» = EMILIO · 1 apagón = LUCIA
#   2 estudio de fotografía = JAVIER · 3 «Tal día como hoy» = SARA · 4 Camino de Santiago = LUIS_GUILLERMO (México)
#   5 escape room = HUGO (Latinoamérica) · 6 «Vidas» = MARTIN_1
# T3 conversación entre amigos: ELENA = ESTELA · PABLO = MILO
# T4 mensajes (/RADIO): 0 contestador Irene = GABI (Argentina) · 1 megafonía aeropuerto = MARTIN_2
#   2 contestador Andrea = LUISA (Latinoamérica) · 3 megafonía centro comercial = SANTIAGO_LAT (Latinoamérica)
#   4 contestador Rafa = CRISTIAN (Colombia) · 5 megafonía teatro = DAVID_M1 · 6 contestador Carmen = SUSANA (también en T1, otro papel)
#   7 contestador Luis = JAVI_ROJAS
# Efectos: sintonía de radio (T2), din-don de megafonía y pitido de contestador (T4); siempre la misma descripción (caché)"""

# ---------------- ESCRITURA ----------------
ESCRITA = {"t1": {"instr": "Una amiga le escribe este correo después de un viaje suyo.",
  "input": ["¡Hola! ¿Qué tal estás? Ana me ha contado que el sábado tuviste un problema en el viaje a Escocia. ¿Qué te pasó? ¿Al final pudiste ver el castillo de Edimburgo? Cuéntame todo. ¿Quedamos esta semana y me enseñas las fotos?", "Un abrazo,<br>Bea"],
  "lead": "Conteste a su amiga. En el correo tiene que:",
  "pautas": ["saludar;", "contar qué problema tuvo en el viaje y qué pasó;", "explicar cómo se sintió en ese momento;", "decir si al final pudo ver el castillo y qué le pareció;", "responder a su propuesta, proponer un día y despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Una revista para estudiantes de español busca historias de sus lectores con este título: «Aquel día pasé mucha vergüenza (o mucho miedo)». Escriba su historia. Hable de:",
   "pautas": ["cuándo fue y dónde estaba usted;", "cómo era el lugar y con quién estaba;", "qué pasó exactamente;", "cómo se sintió y qué hizo;", "cómo terminó la historia y qué piensa hoy de aquel día."]},
  "op2": {"title": "Opción 2", "intro": "Ayer Carmen tuvo un día muy especial. Aquí tiene tres fotos de ese día.",
   "photos": ["8:00. Llueve mucho. Carmen, con ropa de trabajo y un paraguas, está al lado de su coche: tiene una rueda pinchada.",
              "10:15. Carmen llega mojada a la oficina. En la sala de reuniones, su jefe y sus compañeros la miran y miran el reloj.",
              "21:00. Carmen abre la puerta de su casa: sus amigos y su familia están allí, con una tarta y globos. Es su cumpleaños. Carmen se ríe."],
   "ficha": [], "intro2": "Escriba un texto sobre el día de Carmen. Hable de:",
   "pautas": ["qué tiempo hacía y qué problema tuvo Carmen por la mañana;", "qué pasó en la oficina y cómo se sintió;", "qué pasó por la noche y cómo terminó el día."],
   "img": "U10_escrita.jpg", "imgAlt": "Tres fotos del día de Carmen: con su coche bajo la lluvia, llegando tarde a una reunión y con una fiesta sorpresa en su casa"},
  "min": 70, "max": 80}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: un momento especial de mi vida", "pautas": ["cuándo fue y dónde estaba usted;", "con quién estaba y cómo era el lugar;", "qué pasó exactamente;", "cómo se sintió;", "por qué recuerda tanto ese momento."]},
  {"title": "Opción 2: un acontecimiento que recuerdo", "pautas": ["qué acontecimiento fue (una noticia importante, un partido, una fiesta de su ciudad...) y cuándo pasó;", "dónde estaba usted y con quién;", "cómo se enteró;", "qué sintió usted y qué sintió la gente;", "si cambió algo después."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1", "desc": "La llegada de una carrera popular en el centro de una ciudad, una mañana de primavera con sol. Una corredora de unos sesenta años, con camiseta naranja y un número en el pecho, llora de alegría y abraza a su nieto. A su lado, un chico joven con barba está sentado en el suelo, muy cansado. Hay voluntarios con chalecos amarillos que dan agua y medallas, mucha gente detrás de las vallas, globos y un reloj grande.", "img": "U10_oral_foto1.jpg"},
  {"title": "Fotografía 2", "desc": "Una oficina de objetos perdidos en una estación de tren, una tarde de invierno. Fuera nieva. Un chico de unos veinte años, con gorro de lana, mochila y una muleta, habla preocupado con una empleada mayor con gafas y uniforme azul. En el mostrador hay un paraguas, una maleta pequeña y una caja con bufandas y guantes. En la pared, un reloj marca las siete. Detrás, un señor espera sentado con un perro.", "img": "U10_oral_foto2.jpg"}],
  "pautas": ["las personas: cómo son, qué ropa llevan, qué están haciendo;", "el lugar: dónde están, qué tiempo hace, qué cosas hay;", "cómo cree que se sienten las personas y por qué;", "qué cree que ha pasado antes y qué van a hacer después."]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1", "intro": "Usted ha corrido la carrera popular de su ciudad y va al punto de información. Hable con el voluntario o la voluntaria (su profesora). Tiene que:", "pautas": ["saludar y decir su nombre y su número de corredor;", "contar cómo fue la carrera para usted (qué pasó y cómo se sintió);", "preguntar por su tiempo y por las fotos de la llegada;", "preguntar por la próxima carrera y despedirse."]},
  {"title": "Si eligió la fotografía 2", "intro": "Ayer usted olvidó una bolsa en un tren y hoy va a la oficina de objetos perdidos de la estación. Hable con el empleado o la empleada (su profesora). Tiene que:", "pautas": ["saludar y explicar qué le pasó (en qué tren viajaba, a qué hora y dónde estaba sentado/a);", "describir la bolsa y lo que había dentro;", "responder a las preguntas del empleado y dar sus datos;", "preguntar qué tiene que hacer y despedirse."]}]}}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (un momento especial): ¿Qué tiempo hacía aquel día? · ¿Qué hizo después?
    Opción 2 (un acontecimiento): ¿Qué estaba haciendo cuando se enteró? (acepte también «qué hacía») · ¿Habló de ello con su familia?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (carrera popular): ¿Por qué cree que llora la señora? · ¿Ha corrido usted alguna vez una carrera?
    Foto 2 (objetos perdidos): ¿Qué cree que ha perdido el chico? · ¿Qué cree que le pasó en la pierna?
  Tarea 3 — su papel (aquí sí conversa: pregunte, reaccione y provoque un pequeño problema):
    Foto 1 (voluntario/a del punto de información, de tú: es una carrera popular): pida el número de corredor;
    reaccione a lo que cuenta («¡Qué bien!», «¡Qué pena!»); su tiempo es de cincuenta y dos minutos; las fotos
    están en la página web de la carrera dentro de dos días; la próxima carrera es en octubre, de diez kilómetros,
    y la inscripción cuesta 12 euros. Problema: su número no aparece en la lista de la llegada (pregúntele a qué
    hora llegó y qué llevaba puesto) o ya no quedan medallas (se envían por correo).
    Foto 2 (empleado/a de objetos perdidos, de usted): pregunte «¿En qué tren viajaba?», «¿A qué hora?»,
    «¿De qué color es la bolsa?», «¿Qué había dentro?». Hay tres bolsas parecidas: pídale más detalles.
    Problema: la bolsa no está aquí todavía, llega mañana en el tren de la mañana; tiene que rellenar un
    formulario y volver con el DNI (horario: de 9 a 14). Pida nombre y teléfono.
  Al reaccionar, que use el indefinido para los hechos (olvidé, llegué, me caí) y el imperfecto para las
  circunstancias (viajaba en el tren de las cinco, estaba sentado al lado de la ventana, hacía mucho calor),
  emociones (estaba muy nervioso, pasé miedo, ¡qué alegría!) y fórmulas de cortesía (quería..., ¿puede...?).
  Qué mirar en esta unidad: indefinidos irregulares (estuve, tuve, hice / hizo, pude, puse, vine, fui; pidió,
  sintió, durmió) sin tilde en estuve / estuvo; contraste indefinido (hechos) / imperfecto (circunstancias:
  hora, tiempo, lugar, cómo estaba); marcadores para relatar (un día, entonces, de repente, al final, al día
  siguiente); emociones (pasar miedo / vergüenza, ponerse nervioso / rojo, emocionarse) y reacciones (¡qué
  pena!, ¡qué miedo!); en la descripción, hay / está / están + gerundio, creo que..., parece que..."""
ERRORES = """  *estuvé / *tení / *tenió (estuve, tuve); *hací / *hició (hice, hizo); *pedió, *sentió, *dormió (pidió, sintió, durmió);
  *poní (puse); *sabí (supe); *Cuando llegué a casa, llovió (llovía: circunstancia); *Estaba muy nervioso y me ponía rojo
  (me puse: hecho puntual); *Fue muy cansado (estaba muy cansado); *Tuve mucho vergüenza (mucha vergüenza); *Me da vergüenza
  de hablar (me da vergüenza hablar); *Me di cuenta que (de que); *De repente estaba llover (de repente empezó a llover);
  *Al final de todo bien sin verbo; historias sin marcadores, todo con «y después... y después...»."""

# ---------------- IMÁGENES: FOTOS CON VARIEDAD REAL ----------------
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "llegada de una carrera popular en una ciudad una mañana de primavera",
  "personas": "un grupo: corredores, voluntarios y público", "edades": "corredora de unos 60 años, su nieto de unos 8, un corredor de unos 25, voluntarios de 20 a 40 años, público de todas las edades",
  "aspecto": "corredora con camiseta naranja, gorra blanca y un número en el pecho; nieto con una pancarta hecha a mano; corredor joven con barba y camiseta azul empapada; voluntarios con chalecos amarillos; un señor con un perro y una mujer con un bebé en una mochila",
  "espacio": "exterior", "lugar": "avenida del centro de una ciudad española con vallas, arco de llegada hinchable y edificios antiguos", "momento": "mañana",
  "estacion": "primavera", "tiempo": "sol y cielo azul con alguna nube; árboles con hojas nuevas", "gente": "mucha gente: las vallas están llenas de público",
  "accion": "la corredora llora de alegría al cruzar la llegada y abraza a su nieto",
  "fondo": "el corredor joven está sentado en el suelo, muy cansado, y un voluntario le da una botella de agua; un fotógrafo hace fotos; globos de colores en el arco",
  "objetos": "arco de llegada, reloj digital grande, vallas, medallas, botellas de agua, plátanos, globos, pancartas, números de corredor, mochilas, una cámara de fotos",
  "problema": "un corredor no aparece en la lista de tiempos de la llegada y no sabe dónde están las fotos"},
 "oral_foto2": {"situacion": "oficina de objetos perdidos de una estación de tren en una tarde de nieve",
  "personas": "un chico y una empleada; al fondo, un señor con un perro", "edades": "chico de unos 20 años, empleada de unos 60, señor de unos 75",
  "aspecto": "chico con gorro de lana, plumas verde, mochila y una muleta en la pierna derecha; empleada con gafas de pasta, el pelo gris recogido y uniforme azul de la compañía de trenes; señor con abrigo largo y sombrero",
  "espacio": "interior", "lugar": "oficina pequeña de una estación de tren, con un mostrador, estanterías y una ventana a los andenes", "momento": "tarde (casi de noche fuera)",
  "estacion": "invierno", "tiempo": "nieva fuera; se ve la nieve por la ventana", "gente": "casi vacía: solo tres personas y un perro",
  "accion": "el chico, preocupado, explica a la empleada qué ha perdido mientras ella busca en un ordenador",
  "fondo": "el señor espera sentado en un banco con un perro pequeño; por la ventana se ve un tren con nieve en el techo",
  "objetos": "mostrador, ordenador, estanterías con maletas, bolsas, paraguas y una guitarra; una caja con bufandas y guantes; un reloj de pared que marca las siete; un formulario",
  "problema": "la bolsa del chico no está en la oficina todavía y tiene que volver otro día con su documentación"},
 "escrita": {"situacion": "un día de mala suerte que termina con una fiesta sorpresa",
  "personas": "Carmen (en tres momentos), su jefe, sus compañeros, sus amigos y su familia",
  "edades": "Carmen de unos 35 años; jefe de unos 55; compañeros y amigos de 30 a 40; sus padres de unos 65",
  "aspecto": "Carmen con el pelo rizado, gabardina beige y ropa de oficina; mojada en la segunda foto; con un vestido sencillo y sonriendo en la tercera; jefe con traje gris y gafas",
  "espacio": "exterior y después interior", "lugar": "una calle de una ciudad, una sala de reuniones y el salón de un piso", "momento": "mañana, media mañana y noche",
  "estacion": "otoño", "tiempo": "lluvia fuerte por la mañana", "gente": "sola en la calle; seis personas en la reunión; unas diez personas en la fiesta",
  "accion": "mirar una rueda pinchada bajo la lluvia; entrar tarde en una reunión; abrir la puerta y encontrar una fiesta sorpresa",
  "fondo": "coches con los limpiaparabrisas en marcha; un reloj de pared en la sala de reuniones; globos y una pancarta sin texto legible en el salón",
  "objetos": "paraguas, coche, rueda pinchada, bolso, carpeta, mesa de reuniones, reloj, tarta con velas, globos, regalos",
  "problema": "Carmen pincha una rueda, llega tarde y mojada a una reunión importante; por la noche no sabe que la esperan para su cumpleaños"},
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
 "U09": ["mercadillo de antigüedades en una plaza un domingo de otoño", "tienda de fotografía de barrio en una tarde de lluvia de invierno"],
 "U10": ["llegada de una carrera popular en una ciudad una mañana de primavera", "oficina de objetos perdidos de una estación de tren en una tarde de nieve"],
}

IMG_PROMPTS = {
 "portada": "Photorealistic, candid photo of a group of five friends of different ages and backgrounds sitting around a wooden table on a terrace on a warm summer evening, string lights above them; a woman in her sixties with short white hair is telling a funny story with her hands in the air, a young man with curly hair and glasses is laughing so much he covers his face, a woman in her thirties with a headscarf wipes a tear of laughter, a bald man in his forties holds up his phone showing an old photo; glasses of lemonade and a plate of olives on the table, warm golden light, no readable text, 16:9",
 "oral": "Photorealistic, candid photo in a small, bright language classroom in the morning: a teacher in her fifties with short grey hair and red glasses listens and smiles while a female student in her thirties with long dark braids and a yellow jumper tells a story using her hands, looking surprised; a notebook, a pen and a cup of tea on the table, a plant and a large window behind them, no readable text, 3:2",
 "escrita": "Photorealistic triptych, three separate photos side by side of equal size with thin white borders, the same woman of about 35 with curly dark hair at three moments of the same autumn day in a Spanish city. Left: early morning, heavy rain, the woman in a beige trench coat with an umbrella looks with frustration at the flat front tyre of her small car parked in the street, cars with wipers on behind her. Centre: mid-morning, the same woman, wet hair and wet coat, opens the glass door of a meeting room; her boss, a man of about 55 with grey suit and glasses, and four colleagues sitting at a long table turn to look at her, one of them points at the clock on the wall. Right: night, the same woman in a simple dress opens the door of her flat and laughs with her hand on her mouth; her friends and her parents are in the living room with balloons, presents and a birthday cake with lit candles. Candid, natural light, no readable text, 3:1",
 "oral_foto1": "Photorealistic, candid photo of the finish line of a popular city run on a sunny spring morning in a wide avenue of a Spanish city centre with old buildings and trees with new leaves, blue sky with a few clouds: under an inflatable finish arch with coloured balloons and a big digital clock, a woman runner of about 60 with an orange T-shirt, a white cap and a race number on her chest cries with joy and hugs her grandson of about 8, who holds a hand-made banner with drawings only; next to them a young bearded runner of about 25 in a soaked blue T-shirt sits on the ground exhausted while a volunteer in a yellow vest gives him a bottle of water; volunteers hand out medals and bananas, a photographer takes pictures, crowds of people of all ages behind metal barriers, a man with a dog and a woman carrying a baby in a backpack; bright morning light, no readable text, 3:2",
 "oral_foto2": "Photorealistic, candid photo inside a small lost-property office in a Spanish train station on a winter evening, almost dark outside, snow falling, a window shows a platform and a train with snow on its roof: at the counter a young man of about 20 with a wool hat, a green puffer jacket, a backpack and a crutch under his right arm explains something with a worried face to a female employee of about 60 with thick glasses, grey hair tied back and a blue railway uniform, who looks at a computer screen; on the counter an umbrella, a small suitcase, a form and a box full of scarves and gloves; shelves behind with suitcases, bags, umbrellas and a guitar; a wall clock showing seven o'clock; in the background an elderly man of about 75 with a long coat and a hat waits on a bench with a small dog; warm indoor light, almost empty, no readable text, 3:2",
}
IMG_DESC = {"portada": "amigos en una terraza de verano contando anecdotas y riendo", "oral": "clase: alumna cuenta una historia a la profesora", "escrita": "tres fotos del dia de Carmen: rueda pinchada, reunion y fiesta sorpresa", "oral_foto1": "llegada de una carrera popular, primavera, mucha gente", "oral_foto2": "oficina de objetos perdidos de una estacion, invierno con nieve"}
CA1_DESC = {0: "pasaporte / movil / maleta", 1: "playa / coche en el aparcamiento / restaurante del puerto", 2: "bicicleta / billetes de viaje / perro", 3: "selfi / autografo / darse la mano", 4: "plato roto / lampara / botella de vino", 5: "taxi en la nieve / hombre andando en la nieve / bicicleta con nieve", 6: "boda / gimnasio / tren"}

LECTURA = [CL1, CL2, CL3, CL4]
AUDITIVA = [CA1, CA2, CA3, CA4]
