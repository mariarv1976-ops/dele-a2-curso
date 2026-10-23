# -*- coding: utf-8 -*-
# FUENTE DE LA UNIDAD 9 (fase 1) · Antes y ahora
# EXAMEN COMPLETO · lectura T1+T2+T3+T4 (60 min, 25 ítems) · auditiva T1+T2+T3+T4 (40 min, 25 ítems)
U = "09"
TITLE = "Antes y ahora"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress (cambiar si se suben otro mes)
TIEMPOS = {"lectura": 60, "auditiva": 40}
RECORDATORIO = [
 "Pretérito imperfecto: verbos regulares (estaba, estabas...; tenía, tenías...; vivía, vivías...) y los tres irregulares: ser (era), ir (iba) y ver (veía).",
 "Usos del imperfecto: hábitos y costumbres en el pasado (antes iba al trabajo en bici; de pequeña jugaba con mis primos en el parque) y descripciones de personas, lugares y circunstancias (mi abuela era muy alegre; en el pueblo no había cine).",
 "Marcadores de pasado: de niño/a, de joven, a los quince años, cuando tenía / era..., en aquella época, entonces, en aquellos tiempos. Marcadores de presente: ahora, hoy en día, actualmente, en estos momentos.",
 "Ya no + presente, para una acción que se ha interrumpido (ya no vivo en Madrid), y todavía + presente, para una acción que continúa (todavía vivo en Madrid).",
 "Épocas y etapas: a principios / a mediados / a finales del siglo XX, en los años sesenta, en la época de...; la infancia, la adolescencia, la juventud, la madurez, la vejez. Historia y sociedad (los derechos, la democracia, aprobar una ley, estar prohibido) e inventos y descubrimientos (la invención de la imprenta, el descubrimiento de la penicilina, la aparición de internet).",
 "Argumentar y debatir: yo creo que..., estoy de acuerdo, es verdad, eso depende, bueno, sí, pero..., además, por ejemplo.",
]
TIPS_INICIO = [
 "<b>Examen completo, como el día del DELE:</b> lectura 60 minutos (4 tareas, 25 preguntas) y auditiva 40 minutos (4 tareas, 25 preguntas). Reparte el tiempo de la lectura: unos 12 minutos para la tarea 1, 15 para la 2, 15 para la 3 y 18 para la 4.",
 "<b>¿Antes o ahora?</b> En esta unidad muchas preguntas dependen del momento. Fíjate en los marcadores (de niño, en aquella época, hoy en día, ya no, todavía): muchas opciones falsas dicen algo que es verdad, pero en otra época o de otra persona.",
]
CATS = {
 "imperfecto": {"name": "Pretérito imperfecto: formas (regulares y ser, ir, ver)",
  "repaso": "Verbos en -ar: -aba, -abas, -aba, -ábamos, -abais, -aban (estaba, trabajaba). Verbos en -er / -ir: -ía, -ías, -ía, -íamos, -íais, -ían (tenía, vivía). Solo hay tres irregulares: ser (era, eras, era, éramos, erais, eran), ir (iba, ibas, iba, íbamos, ibais, iban) y ver (veía, veías...). Cuidado con la tilde: vivía, tenía. En el libro: unidad 9, el pretérito imperfecto. Repasa también la ficha «El pretérito imperfecto» que te da tu profesora.",
  "reto": "Escribe seis frases sobre tu infancia: una con cada persona (yo, tú, él, nosotros, vosotros, ellos) y usa también era, iba y veía."},
 "habitos": {"name": "Hábitos, costumbres y descripciones en el pasado (antes, de pequeño, cuando era joven)",
  "repaso": "Usamos el imperfecto para contar lo que hacíamos normalmente en una época (de pequeño jugaba en la calle; antes íbamos al cine los domingos) y para describir cómo eran las personas, los lugares y las circunstancias (era muy tímida; en mi pueblo no había supermercado). Es como el presente, pero en el pasado: ahora vivo en Madrid / antes vivía en Sevilla. En el libro: unidad 9, describir hábitos y circunstancias del pasado.",
  "reto": "Escribe cinco frases sobre cómo era tu vida a los quince años: dónde vivías, cómo eras, qué hacías los fines de semana."},
 "yatodavia": {"name": "Ya no / todavía + presente",
  "repaso": "Ya no + presente: algo que hacías antes y que ahora no haces (ya no fumo = antes fumaba y ahora no). Todavía + presente: algo que hacías antes y que sigues haciendo (todavía vivo en el mismo barrio = antes vivía allí y ahora también). Cuidado: «ya no» y «todavía» cambian completamente el sentido de la frase. En el libro: unidad 9, ya no / todavía.",
  "reto": "Escribe tres cosas que ya no haces y tres cosas que todavía haces desde que eras pequeño/a."},
 "marcadores": {"name": "Marcadores temporales del pasado y del presente",
  "repaso": "Pasado: de niño/a, de joven, a los quince años, cuando tenía treinta años, cuando era pequeño; y, para volver a una época de la que ya hemos hablado, en esa / aquella época, entonces, en aquellos tiempos. Presente: ahora, hoy en día, actualmente, en estos momentos. Con ellos podemos comparar: en aquella época no había móviles; hoy en día todo el mundo tiene uno. En el libro: unidad 9, marcadores temporales.",
  "reto": "Elige un lugar que conoces bien y escribe tres frases sobre cómo era antes y tres sobre cómo es hoy en día."},
 "epocas": {"name": "Épocas, historia y sociedad (siglos, décadas, derechos, leyes)",
  "repaso": "A principios / a mediados / a finales del siglo XX; en los años sesenta; en la década de los veinte; la época de...; la antigua Grecia, la época medieval. Historia y sociedad: la democracia, la dictadura, los derechos, la libertad de expresión, la igualdad entre hombres y mujeres, aprobar una ley, legalizar, estar prohibido. En el libro: unidad 9, épocas y periodos históricos.",
  "reto": "Escribe tres frases sobre tu país a mediados del siglo XX: qué existía, qué no existía y qué estaba prohibido."},
 "inventos": {"name": "Inventos, descubrimientos y cambios en la vida diaria",
  "repaso": "La invención de (la rueda, la imprenta, el teléfono, el avión), el descubrimiento de (el fuego, la electricidad, la penicilina), la aparición de (el dinero, el turismo, internet). Para hablar de los cambios: antes de internet la gente escribía cartas; hoy en día mandamos mensajes. En el libro: unidad 9, hitos y eventos y grandes inventos.",
  "reto": "Elige un invento y explica en cuatro frases cómo era la vida antes y cómo es ahora."},
 "etapas": {"name": "Etapas de la vida (infancia, juventud, madurez, vejez)",
  "repaso": "Un bebé, un niño / una niña, un adolescente, un / una joven, un adulto, una persona mayor; la infancia, la adolescencia, la juventud, la madurez, la vejez. Con los marcadores: de niña, de joven, de mayor, a los veinte años. En el libro: unidad 9, etapas de la vida.",
  "reto": "Escribe una frase sobre una persona de tu familia en cada etapa de su vida."},
 "opinar": {"name": "Argumentar y debatir (estoy de acuerdo, eso depende, bueno, sí, pero...)",
  "repaso": "Dar una opinión: yo creo que, pienso que, para mí. Aceptarla: estoy de acuerdo, es verdad, sí, claro. Rechazarla: no estoy de acuerdo, yo creo que no. Acuerdo parcial: bueno, sí, pero...; eso depende; ya, pero... Dar un ejemplo o un argumento más: por ejemplo, además. En el libro: unidad 9, argumentar y debatir.",
  "reto": "Responde a esta frase con tu opinión y dos argumentos: «Antes la gente era más feliz»."},
}
ESTRATEGIAS_NUEVAS = {}

# ---------------- LECTURA ----------------
CL1 = {"n": 1, "type": "mail",
 "instr": "Usted va a leer el correo electrónico que Sergio ha escrito a su amiga Marta. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Sergio compara dos momentos: separa bien lo que pasaba antes y lo que pasa ahora.",
 "head": ["De: Sergio", "Para: Marta", "Asunto: ¡He vuelto a Valdelobos!"],
 "body": [
  "Hola, Marta:",
  "¿Qué tal todo por Valencia? Te escribo porque el fin de semana pasado volví a Valdelobos, el pueblo de mis abuelos. Mi última visita fue hace veinte años. Esta vez fui con mi mujer y los niños, y lo pasamos muy bien. Ya sabes que de pequeño pasaba allí todos los veranos: mis padres trabajaban en Madrid y yo me quedaba con mis abuelos de junio a septiembre.",
  "En aquella época el pueblo era muy diferente. No había supermercado y mi abuela compraba todo en el mercado de los sábados. Tampoco había internet, claro, así que los niños jugábamos todo el día en la calle o nos bañábamos en el río. Por las noches íbamos al cine de verano de la plaza y veíamos películas del oeste. ¡Me encantaba!",
  "Ahora el pueblo está muy cambiado. El cine ya no existe: en la plaza hay un hotel rural con piscina. Y en el río ya no se puede nadar, porque tiene muy poca agua. Pero hay cosas que no cambian: la panadería de la señora Lola todavía está abierta y el pan es igual de bueno. Además, encontré a Andrés, mi mejor amigo de aquellos veranos. Todavía vive allí y ahora es el alcalde. ¡Increíble!",
  "Andrés me contó que en agosto organizan una semana de fiestas, con conciertos y una cena en la calle para todos los vecinos. ¿Por qué no vienes conmigo? Podemos dormir en el hotel de la plaza y así te enseño mis rincones favoritos. Mira tus vacaciones y dime algo, ¿vale?",
  "Un abrazo,<br>Sergio"],
 "items": [
  {"n": 1, "q": "Sergio escribe a Marta para...", "o": ["contarle cómo ha cambiado un lugar e invitarla a ir.", "contarle que se va a vivir al pueblo de sus abuelos.", "pedirle información sobre unas fiestas."], "ok": 0,
   "cats": ["habitos", "marcadores"], "es": "ES-02", "pc": "FN contar y comparar (antes / ahora) · FN proponer (¿por qué no vienes?)",
   "why": "Sergio cuenta cómo era el pueblo antes, cómo es ahora y le propone ir juntos en agosto. No dice que se va a vivir allí, y la información de las fiestas la da él."},
  {"n": 2, "q": "De pequeño, Sergio...", "o": ["vivía con sus abuelos todo el año.", "pasaba las vacaciones de verano en el pueblo.", "trabajaba con sus padres en Madrid."], "ok": 1,
   "cats": ["imperfecto", "habitos"], "es": "ES-03", "pc": "imperfecto de hábito (pasaba, me quedaba) · de pequeño",
   "why": "Pasaba allí todos los veranos, de junio a septiembre. No vivía con sus abuelos todo el año, y los que trabajaban en Madrid eran sus padres."},
  {"n": 3, "q": "Según Sergio, en aquella época en Valdelobos...", "o": ["había un supermercado pequeño.", "los niños jugaban mucho al aire libre.", "no se podía nadar en el río."], "ok": 1,
   "cats": ["habitos", "marcadores"], "es": "ES-07", "pc": "imperfecto descriptivo (había, jugábamos) · en aquella época",
   "why": "Los niños jugaban todo el día en la calle o se bañaban en el río. No había supermercado, y lo de que no se puede nadar en el río es de ahora, no de entonces."},
  {"n": 4, "q": "Ahora, en Valdelobos...", "o": ["todavía hay cine de verano en la plaza.", "los niños se bañan en el río.", "sigue abierta una tienda de antes."], "ok": 2,
   "cats": ["yatodavia"], "es": "ES-03", "pc": "ya no / todavía + presente",
   "why": "La panadería de la señora Lola todavía está abierta. El cine ya no existe y en el río ya no se puede nadar."},
  {"n": 5, "q": "Sergio propone a Marta...", "o": ["ir juntos a las fiestas del pueblo.", "dormir en casa de Andrés.", "ir al pueblo el fin de semana que viene."], "ok": 0,
   "cats": ["marcadores"], "es": "ES-07", "pc": "FN proponer (¿por qué no vienes conmigo?) · marcadores (en agosto)",
   "why": "Le propone ir con él a la semana de fiestas de agosto. Quiere dormir en el hotel de la plaza, no en casa de Andrés, y fue al pueblo el fin de semana pasado."},
 ]}

CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 15 minutos: menos de dos minutos por anuncio. Lee la pregunta primero y busca solo ese dato. Cuidado con los números y con las palabras que limitan (solo, como mínimo, excepto...).",
 "example": {"title": "MUSEO DE LA ESCUELA ANTIGUA",
   "body": "Entra en una clase de los años cincuenta: pupitres de madera, pizarras pequeñas y los libros que usaban nuestros abuelos. Abierto de martes a domingo, de 10:00 a 14:00. Entrada: 3 €; menores de 12 años, gratis. Visitas guiadas para grupos: reserva en el teléfono 975 11 22 33. ¡Te esperamos!",
   "q": "En este museo...", "o": ["los niños pagan tres euros.", "se puede ver una clase de otra época.", "se puede entrar todos los días."], "ok": 1,
   "why": "La opción correcta es la B porque en el museo hay una clase de los años cincuenta."},
 "items": [
  {"n": 6, "title": "BIBLIOTECA MUNICIPAL · CONCURSO DE FOTOGRAFÍA «MI BARRIO ANTES Y AHORA»",
   "body": "¿Tienes en casa fotos antiguas de tu barrio? Busca el mismo lugar, haz una foto nueva desde el mismo sitio y envíanos las dos antes del 30 de noviembre. Máximo: tres parejas de fotos por persona. Premio: una cámara digital y una exposición en la biblioteca en enero. Más información en el mostrador de la biblioteca.",
   "q": "Para participar en el concurso hay que...", "o": ["mandar una foto antigua y una actual del mismo lugar.", "mandar tres fotos como mínimo.", "llevar las fotos a la biblioteca en enero."], "ok": 0,
   "cats": ["marcadores"], "es": "ES-06", "pc": "antes / ahora · imperativo (busca, haz, envíanos, U08) · máximo",
   "why": "Hay que enviar las dos fotos del mismo lugar: la antigua y la nueva. Tres parejas es el máximo, no el mínimo, y en enero es la exposición."},
  {"n": 7, "title": "EL TOCADISCOS · TIENDA DE OBJETOS RETRO",
   "body": "Discos de vinilo, radios antiguas y cámaras de fotos de los años sesenta, setenta y ochenta. ¿Tienes en casa discos que ya no escuchas? Tráelos y te pagamos en el momento. Abrimos de lunes a sábado, de 10:00 a 20:00; los domingos nos puedes encontrar en el mercadillo de la plaza Mayor.",
   "q": "En esta tienda...", "o": ["solo venden cosas nuevas.", "también compran cosas usadas.", "no venden cámaras de fotos."], "ok": 1,
   "cats": ["yatodavia", "epocas"], "es": "ES-03", "pc": "ya no + presente · los años sesenta, setenta...",
   "why": "Compran los discos que la gente ya no escucha y los pagan en el momento. Venden objetos antiguos, también cámaras de fotos."},
  {"n": 8, "title": "OFICINA DE TURISMO · RUTA «EL CENTRO HACE CIEN AÑOS»",
   "body": "¿Cómo era la ciudad a principios del siglo XX? ¿Dónde compraba la gente? ¿Qué medios de transporte había? Descúbrelo con nuestra ruta a pie por el centro histórico. Los sábados a las 11:00, con salida desde la oficina de turismo. Duración: dos horas. Precio: 8 €. Plazas limitadas: es necesario reservar en nuestra página web.",
   "q": "La ruta...", "o": ["se hace en autobús.", "es todos los días a las once.", "necesita reserva previa."], "ok": 2,
   "cats": ["epocas", "imperfecto"], "es": "ES-03", "pc": "a principios del siglo XX · imperfecto (era, compraba, había)",
   "why": "Hay plazas limitadas y es necesario reservar en la web. Es a pie, y solo los sábados."},
  {"n": 9, "title": "NOTICIAS · ADIÓS A LAS CABINAS DE TELÉFONO",
   "body": "Desde este mes ya no hay cabinas de teléfono en las calles de España. Hace veinte años había más de cincuenta mil, pero en los últimos años casi nadie las usaba, porque hoy en día todo el mundo tiene móvil. Algunas cabinas antiguas van a estar en un museo de las telecomunicaciones en Madrid.",
   "q": "Según la noticia, las cabinas de teléfono...", "o": ["han desaparecido de las calles.", "todavía se usan mucho.", "eran más de cincuenta mil el año pasado."], "ok": 0,
   "cats": ["yatodavia", "inventos"], "es": "ES-07", "pc": "ya no hay · hace veinte años había · hoy en día",
   "why": "Ya no hay cabinas en las calles: han desaparecido. Casi nadie las usaba, y había más de cincuenta mil hace veinte años, no el año pasado."},
  {"n": 10, "title": "CENTRO DE MAYORES LOS OLIVOS · TALLER «CUÉNTAME TU VIDA»",
   "body": "¿Quieres escribir tus recuerdos? En este taller, las personas mayores cuentan cómo eran su infancia y su juventud, y unos estudiantes del instituto del barrio escriben sus historias. Al final del curso hacemos un libro con todas ellas. Los jueves, de 17:00 a 18:30, de octubre a diciembre. Gratis. Inscripción en la recepción del centro.",
   "q": "En este taller...", "o": ["los mayores escriben un libro solos.", "los estudiantes cuentan su infancia.", "jóvenes y mayores trabajan juntos."], "ok": 2,
   "cats": ["etapas"], "es": "ES-08", "pc": "LX etapas de la vida (infancia, juventud, mayores)",
   "why": "Los mayores cuentan sus recuerdos y los estudiantes del instituto escriben sus historias: trabajan juntos. Los que cuentan su infancia son los mayores, no los estudiantes."},
  {"n": 11, "title": "FORO «¿CÓMO ERA TU COLEGIO?»",
   "body": "Respuesta de Paco_62:<br>Yo iba a la escuela de mi pueblo. Solo había una clase para niños de todas las edades y un maestro, don Julián, que era muy serio. Llevábamos los libros en una bolsa de tela y en invierno pasábamos mucho frío, porque no había calefacción. Hoy en día mis nietos tienen ordenadores en clase. ¡Cómo cambian las cosas!",
   "q": "Paco cuenta que en su escuela...", "o": ["había una clase para cada edad.", "la temperatura era muy baja en invierno.", "los alumnos usaban ordenadores."], "ok": 1,
   "cats": ["imperfecto", "habitos"], "es": "ES-03", "pc": "imperfecto descriptivo (había, era, pasábamos) · hoy en día",
   "why": "En invierno pasaban mucho frío porque no había calefacción. Había una sola clase para todas las edades, y los ordenadores son de sus nietos, hoy en día."},
  {"n": 12, "title": "MUSEO DEL JUGUETE ANTIGUO",
   "body": "Más de dos mil juguetes de los siglos XIX y XX: muñecas, trenes, coches de metal... ¿Con qué jugaban tus padres y tus abuelos? En la sala 3, los niños pueden jugar con copias de los juguetes de antes. Horario: de 10:00 a 19:00. Cerrado los lunes. Entrada: 5 €; jubilados y menores de 6 años, gratis.",
   "q": "En este museo...", "o": ["los niños pueden usar algunos juguetes.", "los jubilados pagan cinco euros.", "se puede entrar todos los días."], "ok": 0,
   "cats": ["imperfecto", "epocas"], "es": "ES-06", "pc": "imperfecto (jugaban) · siglos XIX y XX · cerrado los lunes",
   "why": "En la sala 3 los niños pueden jugar con copias de juguetes antiguos. Los jubilados entran gratis, y los lunes está cerrado."},
  {"n": 13, "title": "AYUNTAMIENTO · AVISO SOBRE EL MERCADO MUNICIPAL",
   "body": "El edificio del mercado municipal está en obras desde hace tres meses. De momento, los puestos de fruta, carne y pescado están en el parque de la Estación, de lunes a sábado, en el horario de siempre. El mercado nuevo va a tener un supermercado, una zona de restaurantes y un aparcamiento. Perdonen las molestias.",
   "q": "En estos momentos, los puestos del mercado...", "o": ["ya están en el edificio nuevo.", "están cerrados por obras.", "están en otro lugar."], "ok": 2,
   "cats": ["marcadores"], "es": "ES-03", "pc": "marcadores de presente (de momento, en estos momentos) · desde hace",
   "why": "Mientras duran las obras, los puestos están en el parque de la Estación: en otro lugar. El edificio está en obras, pero los puestos abren en su horario de siempre."},
 ]}

CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos de tres personas que hablan de cómo era su vida antes y cómo es ahora. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 15 minutos. Lee primero las seis preguntas. Las tres personas hablan de su pasado y de su presente: comprueba en cada respuesta si la pregunta habla de antes o de ahora.",
 "texts": [
  {"name": "Rosa", "body": "Tengo sesenta y siete años y vivo en el mismo barrio de Zaragoza desde que nací. De joven trabajaba en una fábrica de chocolate: entraba a las seis de la mañana y no tenía tiempo para nada. Era una chica muy alegre y hablaba con todo el mundo. ¡Eso no ha cambiado! Ahora estoy jubilada y por fin hago lo que me gusta: dos tardes a la semana voy a un curso de pintura en el centro cívico y pinto paisajes. Mi hija vive en Francia y, cuando la visito, pinto las calles de su ciudad. Antes compraba todo en el mercado; ahora a veces pido la compra por internet."},
  {"name": "Jorge", "body": "A los veinticinco años me fui a Londres y viví allí doce años. Trabajaba en un banco, ganaba bastante dinero y salía casi todas las noches con mis compañeros. Era una vida divertida, pero siempre estaba cansado. Hace tres años volví a España, pero no a Madrid, mi ciudad: ahora vivo en un pueblo pequeño de Asturias. Trabajo desde casa: traduzco documentos del inglés. Ya no voy a restaurantes caros: tengo un huerto con tomates, lechugas y patatas, y casi todo lo que como sale de allí. Todavía hablo con mis amigos de Londres por videollamada todas las semanas. Aquí estoy mucho más tranquilo y duermo mejor."},
  {"name": "Lucía", "body": "De niña vivía en un pueblo de Teruel y era muy tímida: en el colegio casi no hablaba y en las fiestas siempre estaba detrás de mi madre. Me encantaba dibujar sola en mi habitación. Cuando tenía dieciocho años, me fui a Toledo a estudiar Historia y todo empezó a cambiar. Ahora soy guía: todos los días enseño la catedral y las calles antiguas a grupos de turistas de todo el mundo, en español y en inglés. ¡Hablo durante horas delante de cincuenta personas! Mis padres todavía no lo creen. Mi hermano dice que ahora soy la más habladora de la familia."}],
 "items": [
  {"n": 14, "q": "¿Quién pasó una larga temporada en otro país?", "ok": 1, "cats": ["habitos"], "es": "ES-08", "pc": "imperfecto de hábito (trabajaba, ganaba, salía) · indefinido (viví allí, U02)",
   "why": "Jorge vivió doce años en Londres. Rosa visita a su hija en Francia, pero no vivió allí, y Lucía habla en inglés con turistas extranjeros, pero vive en España."},
  {"n": 15, "q": "¿Quién trabaja con visitantes extranjeros?", "ok": 2, "cats": ["marcadores"], "es": "ES-03", "pc": "marcadores de presente (ahora) · LX trabajo",
   "why": "Lucía es guía y enseña Toledo a turistas de todo el mundo. Jorge traduce documentos del inglés, pero no trabaja con visitantes."},
  {"n": 16, "q": "¿Quién vive todavía en el lugar donde nació?", "ok": 0, "cats": ["yatodavia"], "es": "ES-09", "pc": "todavía + presente · desde que nací",
   "why": "Rosa vive en el mismo barrio de Zaragoza desde que nació. Lucía nació en un pueblo de Teruel y ahora vive en Toledo, y Jorge, que es de Madrid, ahora vive en Asturias."},
  {"n": 17, "q": "¿Quién hace ahora una actividad artística?", "ok": 0, "cats": ["habitos", "marcadores"], "es": "ES-07", "pc": "antes / ahora · LX ocio (pintar, dibujar)",
   "why": "Rosa va ahora a un curso de pintura y pinta paisajes. A Lucía le encantaba dibujar, pero de niña, no ahora."},
  {"n": 18, "q": "¿Quién cultiva casi toda su comida?", "ok": 1, "cats": ["yatodavia"], "es": "ES-03", "pc": "ya no + presente · LX alimentación (huerto)",
   "why": "Jorge tiene un huerto y casi todo lo que come sale de allí. Rosa habla de la compra, pero en el mercado o por internet."},
  {"n": 19, "q": "¿Quién hablaba poco con los demás en su infancia?", "ok": 2, "cats": ["imperfecto", "etapas"], "es": "ES-08", "pc": "imperfecto descriptivo (era tímida, casi no hablaba) · de niña",
   "why": "De niña, Lucía era muy tímida y casi no hablaba en el colegio. Rosa, en cambio, hablaba con todo el mundo."}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un texto de un blog en el que una estudiante cuenta cómo era la vida de su abuela. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto. Fíjate en la época de cada pregunta (de niña, en Barcelona, hoy en día) y busca la respuesta en esa parte del texto.",
 "title": "Mi abuela Pilar: ochenta años de cambios",
 "sub": "Blog «Historias de familia», de Irene Soler",
 "body": [
  "Esta semana he hablado con mi abuela Pilar, que tiene ochenta y dos años, para un trabajo de clase sobre cómo era la vida antes. Hemos estado toda la tarde en su cocina, con un café y unas galletas. Aquí os dejo un resumen de lo que me contó.",
  "Mi abuela nació en un pueblo pequeño de Jaén. De niña, vivía con sus padres y sus cinco hermanos en una casa sin agua: todos los días iba con su madre a la fuente del pueblo con dos cubos. Por las mañanas iba a la escuela, pero por las tardes ayudaba a sus padres en el campo y con los animales. Solo estudió hasta los doce años. «En aquella época, los niños trabajábamos como los mayores», me dijo.",
  "En el pueblo no había televisión en las casas. La primera televisión estaba en el bar de la plaza, y los sábados por la noche los vecinos iban allí a ver los programas. Mi abuela se reía mucho al recordarlo: «¡Las mujeres llevábamos nuestras sillas de casa, porque en el bar no había sitio para todos!».",
  "A los diecinueve años se casó con mi abuelo y se fueron a vivir a Barcelona, porque en el pueblo no había trabajo. Él trabajaba en una fábrica de coches y ella cosía en un taller de ropa. Por las noches, mi abuela iba a una escuela para adultos: quería aprender a escribir sin faltas de ortografía. Además, me contó algo que me sorprendió mucho: en aquellos tiempos, una mujer casada no podía abrir una cuenta en el banco sin el permiso de su marido. «Por suerte, tu abuelo nunca me dijo que no a nada», me explicó.",
  "Hoy en día mi abuela vive sola en el mismo piso de Barcelona. Ya no cose para trabajar, pero todavía hace los vestidos de las muñecas de mis primas pequeñas. Tiene un móvil y lo usa mucho: todas las mañanas nos manda por WhatsApp fotos de las flores de su terraza. Además, los martes va a clase de baile con sus amigas del barrio.",
  "Al final le pregunté: «Abuela, ¿la vida era mejor antes o ahora?». Ella lo pensó un momento. «Bueno, eso depende. Antes la gente se ayudaba más y los vecinos eran como una familia. Pero ahora las mujeres tienen los mismos derechos que los hombres y pueden elegir su vida, y eso es mucho mejor». Yo estoy totalmente de acuerdo con ella."],
 "items": [
  {"n": 20, "q": "De niña, Pilar...", "o": ["también trabajaba, además de ir a la escuela.", "estudió hasta los dieciocho años.", "iba sola a la fuente todos los días."], "ok": 0,
   "cats": ["habitos", "etapas"], "es": "ES-03", "pc": "imperfecto de hábito (iba, ayudaba) · de niña",
   "why": "Por las mañanas iba a la escuela y por las tardes ayudaba a sus padres en el campo. Solo estudió hasta los doce años, y a la fuente iba con su madre, no sola."},
  {"n": 21, "q": "En el pueblo de Pilar, la televisión...", "o": ["estaba en todas las casas.", "se veía en un lugar público.", "solo la veían los hombres."], "ok": 1,
   "cats": ["imperfecto", "inventos"], "es": "ES-03", "pc": "imperfecto descriptivo (no había, estaba) · LX inventos",
   "why": "La primera televisión estaba en el bar de la plaza y los vecinos iban allí a verla. No había televisión en las casas, y las mujeres también iban: llevaban sus sillas."},
  {"n": 22, "q": "En Barcelona, Pilar...", "o": ["trabajaba en una fábrica de coches.", "vivía sola.", "iba a clase por las noches."], "ok": 2,
   "cats": ["habitos"], "es": "ES-08", "pc": "imperfecto de hábito (iba, cosía) · por las noches",
   "why": "Por las noches iba a una escuela para adultos. La fábrica de coches era el trabajo de su marido, y vive sola hoy en día, no en aquella época."},
  {"n": 23, "q": "Según Pilar, en aquellos tiempos las mujeres casadas...", "o": ["no podían hacer algunas cosas sin su marido.", "no podían trabajar fuera de casa.", "no podían estudiar."], "ok": 0,
   "cats": ["epocas", "marcadores"], "es": "ES-03", "pc": "historia y sociedad (derechos, permiso) · en aquellos tiempos",
   "why": "Una mujer casada no podía abrir una cuenta en el banco sin el permiso de su marido. Pilar trabajaba en un taller y estudiaba por las noches."},
  {"n": 24, "q": "Hoy en día, Pilar...", "o": ["todavía cose ropa para trabajar.", "va a clase de baile todos los días.", "está en contacto con su familia a través del móvil."], "ok": 2,
   "cats": ["yatodavia", "marcadores"], "es": "ES-06", "pc": "ya no / todavía + presente · hoy en día",
   "why": "Todas las mañanas manda fotos a la familia por WhatsApp. Ya no cose para trabajar, solo para las muñecas de sus nietas, y va a bailar solo los martes."},
  {"n": 25, "q": "Sobre la vida de antes y la de ahora, Pilar piensa que...", "o": ["antes todo era mejor.", "cada época tiene cosas buenas.", "ahora los vecinos se ayudan más."], "ok": 1,
   "cats": ["opinar"], "es": "ES-02", "pc": "argumentar (bueno, eso depende..., pero)",
   "why": "Dice que eso depende: antes la gente se ayudaba más, pero ahora las mujeres tienen los mismos derechos que los hombres. Ayudarse más es de antes, no de ahora."},
 ]}

# ---------------- AUDITIVA ----------------
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación: las tres aparecen. Escucha bien de qué momento hablan (de pequeño, en esta foto, ahora) y si la persona dice «ya no» o «todavía».",
 "example": {"q": "¿Con qué jugaba el abuelo de pequeño?", "o": ["una pelota", "una bicicleta", "un tren de madera"], "ok": 2,
   "pres": "Va a escuchar a una chica que habla con su abuelo.",
   "lines": [("Mujer", "AITANA", "Abuelo, ¿tú tenías juguetes de pequeño?"),
             ("Hombre", "ABUELO_CHARLIE", "Pocos, hija. Yo quería una bicicleta, pero mis padres no tenían dinero."),
             ("Mujer", "AITANA", "¿Y jugabas al fútbol con tus amigos?"),
             ("Hombre", "ABUELO_CHARLIE", "Muy poco, porque en el pueblo nadie tenía pelota. Mi juguete favorito era un tren de madera. Lo hizo mi padre."),
             ("Mujer", "AITANA", "¡Qué bonito! ¿Y todavía lo tienes?"),
             ("Hombre", "ABUELO_CHARLIE", "Sí, está en una caja. Mañana lo buscamos juntos.")],
   "solucion": "La opción correcta es la letra ce. Jugaba con un tren de madera.",
   "img": "U09_CA1_0.jpg",
   "prompt": "Panel 1: an old leather football. Panel 2: a classic old bicycle. Panel 3: a small wooden toy train."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Cómo llevaba el pelo la mujer a los veinte años?", "o": ["largo y rizado", "muy corto", "con trenzas"], "ok": 1,
   "cats": ["imperfecto", "etapas"], "es": "ES-08", "pc": "imperfecto descriptivo (llevaba, tenía) · LX aspecto físico",
   "pres": "Va a escuchar a dos amigas que miran fotos antiguas.",
   "lines": [("Mujer", "FIONA", "¡Mira, Carmen! ¿Esta eres tú? ¡Con trenzas!"),
             ("Mujer", "EVA", "No, no, esa es mi hermana Luisa. Yo de pequeña también llevaba trenzas, pero en esta foto tenía veinte años."),
             ("Mujer", "FIONA", "¿Y cuál eres tú?"),
             ("Mujer", "EVA", "La de la derecha, la del pelo cortito. En aquella época mis amigas llevaban el pelo largo y rizado, pero a mí me gustaba así."),
             ("Mujer", "FIONA", "¡Qué moderna!")],
   "why": "A los veinte años llevaba el pelo muy corto. Las trenzas son de su hermana y de cuando era pequeña, y el pelo largo y rizado era de sus amigas.",
   "img": "U09_CA1_1.jpg", "prompt": "Panel 1: a young woman with long curly hair. Panel 2: a young woman with a very short pixie haircut. Panel 3: a young woman with two braids."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Dónde vivía el hombre de niño?", "o": ["en una casa en el campo", "en un piso en la ciudad", "en una casa cerca de la playa"], "ok": 1,
   "cats": ["habitos", "marcadores"], "es": "ES-07", "pc": "imperfecto (vivía, íbamos) · de niño · ahora",
   "pres": "Va a escuchar a un hombre y a una mujer en una cena.",
   "lines": [("Mujer", "SARA_2", "Oye, Álex, tú eres de Cádiz, ¿no?"),
             ("Hombre", "DANIEL_ES", "Bueno, mis padres viven ahora en Cádiz, al lado de la playa. Pero yo de niño vivía en Madrid, en un piso pequeño del centro."),
             ("Mujer", "SARA_2", "¿En Madrid? ¿Y te gustaba?"),
             ("Hombre", "DANIEL_ES", "Sí, mucho. Y en verano íbamos al campo, a la casa de mis tíos. Allí lo pasaba genial con mis primos.")],
   "why": "De niño vivía en un piso del centro de Madrid. Cerca de la playa viven ahora sus padres, y al campo iba solo en verano, a casa de sus tíos.",
   "img": "U09_CA1_2.jpg", "prompt": "Panel 1: a stone house in the countryside with fields. Panel 2: an apartment building in a city centre. Panel 3: a small white house next to a sandy beach."},
  {"n": 3, "conv": "Conversación tres", "q": "¿Qué deporte hacía la mujer de joven?", "o": ["natación", "baloncesto", "tenis"], "ok": 0,
   "cats": ["yatodavia", "habitos"], "es": "ES-07", "pc": "de joven · ya no + presente · imperfecto de hábito (entrenaba)",
   "pres": "Va a escuchar a dos compañeros de trabajo.",
   "lines": [("Hombre", "OSCAR", "Marta, ¿juegas al tenis? Tienes una raqueta en la mesa."),
             ("Mujer", "ANA_MARIA", "Sí, pero empecé el año pasado. De joven era nadadora: entrenaba todos los días en la piscina de mi barrio."),
             ("Hombre", "OSCAR", "¿Y ya no nadas?"),
             ("Mujer", "ANA_MARIA", "No, ya no tengo tiempo. ¿Y tú? ¿Todavía juegas al baloncesto?"),
             ("Hombre", "OSCAR", "¡Qué va! Ahora solo lo veo en la tele.")],
   "why": "De joven era nadadora. Al tenis juega desde el año pasado, y el baloncesto es el deporte de su compañero.",
   "img": "U09_CA1_3.jpg", "prompt": "Panel 1: a woman swimming in a pool lane. Panel 2: a woman throwing a basketball. Panel 3: a woman playing tennis with a racket."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Qué compra la mujer?", "o": ["un tocadiscos", "una cámara de fotos", "una máquina de escribir"], "ok": 2,
   "cats": ["inventos", "yatodavia"], "es": "ES-05", "pc": "LX objetos de otra época · ya no + presente · imperfecto (era, escribía)",
   "pres": "Va a escuchar a una mujer en una tienda de objetos antiguos.",
   "lines": [("Mujer", "CRISTINA_LAT", "Buenos días. ¿Cuánto cuesta esa máquina de escribir?"),
             ("Hombre", "AGUSTIN", "Ciento veinte euros. Es de los años cincuenta y funciona perfectamente."),
             ("Mujer", "CRISTINA_LAT", "Es un poco cara... Es para mi padre: antes era periodista y escribía con una igual. ¿Y el tocadiscos?"),
             ("Hombre", "AGUSTIN", "Ese ya está vendido, lo siento. Tengo esta cámara de fotos de los años setenta, por cuarenta euros."),
             ("Mujer", "CRISTINA_LAT", "No, mi padre ya no hace fotos. Bueno, me llevo la máquina. ¡Le va a encantar!")],
   "why": "Al final se lleva la máquina de escribir. El tocadiscos ya está vendido, y la cámara no la quiere porque su padre ya no hace fotos.",
   "img": "U09_CA1_4.jpg", "prompt": "Panel 1: a vintage record player with a vinyl record. Panel 2: an old film camera from the seventies. Panel 3: an old typewriter."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Qué hace todavía el hombre los domingos?", "o": ["comer con su familia", "jugar al fútbol", "ir al cine"], "ok": 0,
   "cats": ["yatodavia"], "es": "ES-06", "pc": "ya no / todavía + presente · como siempre",
   "pres": "Va a escuchar a dos amigos que se encuentran por la calle.",
   "lines": [("Mujer", "JANET", "¡Hola, Pablo! ¿Todavía juegas al fútbol los domingos con los amigos del instituto?"),
             ("Hombre", "VOLU", "No, ya no. Me duele la rodilla y lo dejé hace dos años."),
             ("Mujer", "JANET", "¡Qué pena! ¿Y qué haces ahora los domingos? ¿Vas al cine, como antes?"),
             ("Hombre", "VOLU", "Al cine voy los viernes, que es más barato. Los domingos como en casa de mis padres, como siempre. Mi madre hace paella y vamos todos.")],
   "why": "Los domingos come en casa de sus padres, como siempre. Ya no juega al fútbol, y al cine va los viernes.",
   "img": "U09_CA1_5.jpg", "prompt": "Panel 1: a family eating paella together around a table. Panel 2: a man playing football with friends. Panel 3: a man sitting in a cinema with popcorn."},
  {"n": 6, "conv": "Conversación seis", "q": "¿Qué foto quiere hacer más grande el hombre?", "o": ["una foto de una boda", "una foto en la playa", "una foto de un bebé"], "ok": 1,
   "cats": ["marcadores", "epocas"], "es": "ES-05", "pc": "LX fotos antiguas · en mil novecientos sesenta",
   "pres": "Va a escuchar a un hombre en una tienda de fotografía.",
   "lines": [("Hombre", "MARIO", "Buenas tardes. Quería hacer más grande esta foto antigua, para ponerla en el salón."),
             ("Mujer", "NIEVE", "A ver... ¡Qué bonita! ¿Es una boda?"),
             ("Hombre", "MARIO", "No, la foto de la boda ya está en el salón. Esta es de mis abuelos en la playa de Gijón, en mil novecientos sesenta."),
             ("Mujer", "NIEVE", "¿Y esta del bebé? ¿También la quiere más grande?"),
             ("Hombre", "MARIO", "No, esa no, gracias. Es mi padre de bebé, pero está un poco rota."),
             ("Mujer", "NIEVE", "Muy bien. Puede venir a buscarla el jueves.")],
   "why": "Quiere hacer más grande la foto de sus abuelos en la playa. La foto de la boda ya está en el salón, y la del bebé no la quiere porque está rota.",
   "img": "U09_CA1_6.jpg", "prompt": "Panel 1: an old black and white wedding photo of a couple. Panel 2: an old black and white photo of a couple on a beach. Panel 3: an old black and white photo of a baby."},
 ]}

RADIO_FX = "SONIDO 2: Short bright radio station jingle, three cheerful synth notes, clean, no voices, no background noise"
CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. En la primera escucha marca una opción; en la segunda, compruébala. Atención a los números («siete de cada diez» es más de la mitad) y a qué época se refiere cada dato: antes, hoy en día o hace unos años.",
 "example": {"q": "Según el anuncio, la exposición...", "o": ["abre todos los días.", "no cuesta dinero.", "es sobre los años setenta."], "ok": 1,
   "why": "La opción correcta es la B porque la entrada es gratuita.",
   "lab": "Locutor", "voice": "SERGIO/RADIO",
   "text": "Exposición «Así éramos: los años ochenta», en el Centro Cultural Norte. Ropa, música, juguetes y los primeros ordenadores de aquella época. Hasta el treinta de noviembre, de martes a domingo. La entrada es gratuita para todos. ¡Ven a recordar cómo vivíamos!",
   "solucion": "La opción correcta es la letra be, porque la entrada es gratuita."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "Según la noticia, muchos abuelos españoles...", "o": ["usan internet para hablar con sus nietos.", "ya no hablan mucho con sus nietos.", "aprendieron a usar internet hace diez años."], "ok": 0,
   "cats": ["inventos", "marcadores"], "es": "ES-07", "pc": "hoy en día / hace diez años · porcentajes (siete de cada diez)",
   "lab": "Locutora", "voice": "MARINA_ES/RADIO",
   "text": "Según una encuesta, hoy en día siete de cada diez abuelos españoles hablan con sus nietos por videollamada al menos una vez a la semana. Hace diez años, en cambio, solo uno de cada diez abuelos usaba internet. Y muchos dicen que ahora ven más a sus nietos que antes, aunque es en la pantalla del móvil.",
   "why": "Siete de cada diez abuelos hablan con sus nietos por videollamada. Hace diez años solo uno de cada diez usaba internet, y dicen que ahora los ven más que antes."},
  {"n": 8, "conv": "Audio 2", "q": "Las clases de baile...", "o": ["son para gente joven.", "son por la mañana.", "son más baratas el primer mes."], "ok": 2,
   "cats": ["imperfecto", "epocas"], "es": "ES-03", "pc": "imperfecto (¿te encantaba bailar?) · de joven · en los años sesenta",
   "lab": "Locutora", "voice": "TAMARA/RADIO",
   "text": "¿Te encantaba bailar rock and roll de joven? En la escuela Paso a Paso tenemos clases de los bailes de los años sesenta para mayores de cincuenta y cinco años. Lunes y miércoles, de seis a siete de la tarde. Y el primer mes, ¡a mitad de precio! Llámanos.",
   "why": "El primer mes cuestan la mitad. Son para mayores de cincuenta y cinco años, y son por la tarde."},
  {"n": 9, "conv": "Audio 3", "q": "Según el programa, hoy en día...", "o": ["la mayoría de la gente vive en el campo.", "las familias tienen menos hijos que antes.", "cinco de cada diez personas viven en ciudades."], "ok": 1,
   "cats": ["epocas", "marcadores"], "es": "ES-07", "pc": "a principios del siglo XX / hoy en día · porcentajes",
   "lab": "Locutor", "voice": "DIEGO_PE/RADIO",
   "text": "Hoy, en «Nuestra historia», hablamos de cómo hemos cambiado. A principios del siglo veinte, la mayoría de los españoles vivía en el campo. Hoy en día, ocho de cada diez personas viven en ciudades. Y antes las familias tenían cinco hijos de media; ahora, poco más de uno.",
   "why": "Antes las familias tenían cinco hijos de media y ahora poco más de uno. La mayoría vivía en el campo a principios del siglo veinte, y hoy en día son ocho de cada diez las personas que viven en ciudades."},
  {"n": 10, "conv": "Audio 4", "q": "Según el anuncio, la biblioteca...", "o": ["devuelve las fotos el mismo día.", "compra fotos antiguas del barrio.", "busca fotos recientes del barrio."], "ok": 0,
   "cats": ["marcadores"], "es": "ES-03", "pc": "antes de mil novecientos ochenta · imperativo (tráelas, U08)",
   "lab": "Locutora", "voice": "LYDIA/RADIO",
   "text": "La biblioteca del barrio de San Pablo prepara un libro sobre la historia del barrio. ¿Tienes fotos de antes de mil novecientos ochenta? Tráelas a la biblioteca hasta el quince de diciembre. Nosotros las escaneamos y las devolvemos en el momento. ¡Ayúdanos a recordar cómo era el barrio!",
   "why": "Escanean las fotos y las devuelven en el momento: el mismo día. No las compran, y buscan fotos de antes de mil novecientos ochenta, no recientes."},
  {"n": 11, "conv": "Audio 5", "q": "Según la noticia, el tranvía...", "o": ["cruza la ciudad de norte a sur.", "funciona desde hace cincuenta años.", "se puede usar gratis durante un mes."], "ok": 2,
   "cats": ["marcadores", "inventos"], "es": "ES-07", "pc": "hace cincuenta años · ahora · desde el lunes",
   "lab": "Locutor", "voice": "DAVID_LAT/RADIO",
   "text": "Hace cincuenta años, un tranvía cruzaba la ciudad de norte a sur, pero en mil novecientos setenta y cinco lo cerraron porque había demasiados coches. Ahora el tranvía vuelve: desde el lunes, una línea nueva, moderna y eléctrica, va del centro a la universidad. Y durante el primer mes, el viaje es gratis.",
   "why": "Durante el primer mes, el viaje es gratis. El tranvía que cruzaba la ciudad de norte a sur era el de hace cincuenta años; el nuevo va del centro a la universidad y funciona desde el lunes."},
  {"n": 12, "conv": "Audio 6", "q": "En el programa, los oyentes pueden...", "o": ["recibir un libro sobre su antiguo colegio.", "contar sus recuerdos del colegio.", "hablar con sus antiguos profesores."], "ok": 1,
   "cats": ["imperfecto", "habitos"], "es": "ES-10", "pc": "imperfecto (cómo eran, había) · FN describir hábitos pasados",
   "lab": "Locutor", "voice": "ZABRA/RADIO",
   "text": "Esta semana, en nuestro programa «Así éramos», hablamos del colegio de antes. ¿Cómo eran tus profesores? ¿A qué jugabas en el recreo? Llámanos y cuéntanos tus recuerdos. Todos los oyentes que participan reciben un libro de fotos antiguas de la ciudad.",
   "why": "Pueden llamar y contar sus recuerdos del colegio. El libro que reciben es de fotos antiguas de la ciudad, no de su colegio, y hablan de sus profesores, pero no con ellos."},
 ]}
for _x in [CA2["example"]] + CA2["items"]:
    _x["sound"] = RADIO_FX

CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Inés y Raúl. Indique si los enunciados (del 13 al 18) se refieren a Inés (A), a Raúl (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Inés y Raúl hablan de cuando iban juntos al instituto y de su vida de ahora. Si algo lo hace otra persona o ya no lo hace ninguno de los dos, la respuesta es C.",
 "who": ["Inés", "Raúl"], "voices": {"INES": "SARA_JOVEN", "RAUL": "DANI"},
 "lines": [
  ("INES", "¿Raúl? ¡Qué sorpresa! ¡Raúl Ortega, del instituto!"),
  ("RAUL", "¡Inés! ¡Cuánto tiempo! Casi no te reconozco. Antes llevabas gafas, ¿no?"),
  ("INES", "Sí, unas gafas enormes. Ahora llevo lentillas. Oye, ¿todavía vives en el barrio?"),
  ("RAUL", "Sí, sí, en la calle de la Iglesia, al lado de mis padres. Nunca me he ido de aquí. ¿Y tú?"),
  ("INES", "Yo vivo en Valencia desde hace diez años. He venido a ver a mi hermana. ¿Y todavía juegas al baloncesto? Antes estabas siempre en la pista."),
  ("RAUL", "¡Qué va! Ya no. Ahora corro un poco los domingos, nada más. Y tú querías ser profesora de matemáticas, ¿verdad?"),
  ("INES", "Sí, y fui profesora seis años. Pero lo dejé y ahora tengo una tienda de bicicletas. ¡Me encanta!"),
  ("RAUL", "¡Qué cambio! Pues yo sigo en la empresa de mi padre, como siempre."),
  ("INES", "¡Qué tiempos! ¿Te acuerdas de las tardes en el parque? Íbamos todos después de clase."),
  ("RAUL", "¡Claro! Y comíamos pipas en el banco de siempre. Pero el parque ya no existe: ahora hay un aparcamiento."),
  ("INES", "Oye, ¿te acuerdas de Toni, el chico que siempre sacaba dieces?"),
  ("RAUL", "¡Claro! El mejor de la clase. Ahora es médico en Londres."),
  ("INES", "¿Y Marisa? Ella organizaba siempre las fiestas de cumpleaños."),
  ("RAUL", "Pues mira, Marisa quiere organizar una cena con toda la clase en diciembre. ¿Te apuntas?"),
  ("INES", "¡Claro que sí! Pero en diciembre tengo mucho trabajo en la tienda... ¿Me mandas la fecha por mensaje?"),
  ("RAUL", "Vale. Dame tu número y te escribo esta noche.")],
 "items": [
  {"n": 13, "q": "Ya no lleva gafas.", "ok": 0, "cats": ["yatodavia"], "es": "ES-08", "pc": "ya no + presente · antes llevabas",
   "why": "Inés antes llevaba gafas y ahora lleva lentillas."},
  {"n": 14, "q": "Nunca ha vivido fuera del barrio.", "ok": 1, "cats": ["yatodavia", "marcadores"], "es": "ES-03", "pc": "todavía + presente · nunca me he ido",
   "why": "Raúl todavía vive en el barrio y dice que nunca se ha ido. Inés vive en Valencia desde hace diez años."},
  {"n": 15, "q": "Ahora tiene un trabajo diferente al de antes.", "ok": 0, "cats": ["marcadores"], "es": "ES-07", "pc": "antes / ahora · indefinido (fui profesora, lo dejé, U02)",
   "why": "Inés fue profesora seis años y ahora tiene una tienda de bicicletas."},
  {"n": 16, "q": "Trabaja en un negocio de su familia.", "ok": 1, "cats": ["yatodavia"], "es": "ES-03", "pc": "seguir + en (sigo en la empresa) · como siempre",
   "why": "Raúl sigue en la empresa de su padre."},
  {"n": 17, "q": "Sacaba las mejores notas de la clase.", "ok": 2, "cats": ["imperfecto", "habitos"], "es": "ES-08", "pc": "imperfecto descriptivo (sacaba, era)",
   "why": "El que siempre sacaba dieces era Toni, otro compañero de clase."},
  {"n": 18, "q": "Va a organizar una cena de antiguos compañeros.", "ok": 2, "cats": ["habitos"], "es": "ES-08", "pc": "imperfecto de hábito (organizaba) · querer + infinitivo",
   "why": "La que quiere organizar la cena es Marisa. Inés y Raúl solo van a ir."}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

CH = "SONIDO 2: Two-tone ding-dong chime of a public address announcement system, clean and clear, no voices, no background noise"
BP = "SONIDO 1: Single short electronic answering machine beep, clean, no background noise"
CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. En cada mensaje pregúntate: ¿quién habla, dónde y para qué? ¿Pide algo, invita, da las gracias, recuerda el pasado, avisa de un cambio? Sobran tres.",
 "enun": [
  "Alguien cambia el día de una visita.",
  "Se informa del horario de un museo.",
  "Alguien pide unas fotos antiguas.",
  "Una persona invita a una cena de antiguos compañeros.",
  "Un tren antiguo hace un viaje especial.",
  "Alguien da las gracias por un regalo.",
  "Una tienda vende productos de otra época.",
  "Un servicio ya no se ofrece.",
  "Alguien recuerda cómo era un lugar.",
  "Se ofrece un curso gratuito.",
  "Alguien no puede ir a una cita."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "NINOSKA/RADIO", "sound": BP,
   "text": "Buenos días, señor Gómez. Le llamamos de la residencia Los Pinos. La visita de los alumnos de su colegio no es el jueves: es el viernes, a la misma hora. Los abuelos están muy contentos. ¡Hasta el viernes!",
   "solucion": "La opción correcta es la letra a: alguien cambia el día de una visita."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 2, "cats": ["etapas", "imperfecto"], "es": "ES-10", "pc": "cuando éramos pequeños · imperativo (tráelas, U08)",
   "lab": "Contestador", "voice": "LINA/RADIO", "sound": BP,
   "text": "Hola, Juan, soy Elena. Estoy haciendo un álbum para el cumpleaños de papá. ¿Tienes fotos de cuando éramos pequeños, de las vacaciones en el pueblo? Tráelas el domingo a casa de mamá, por favor. ¡Un beso!",
   "why": "Elena le pide a su hermano fotos de cuando eran pequeños para un álbum."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 4, "cats": ["epocas", "inventos"], "es": "ES-10", "pc": "LX épocas (de mil novecientos veinte, de época)",
   "lab": "Megafonía", "voice": "LUIS_VEGA/RADIO", "sound": CH,
   "text": "Atención, por favor. El Tren de la Fresa, un tren de vapor de mil novecientos veinte, sale a las diez y media de la vía uno con destino Aranjuez. Durante el viaje, los revisores llevan uniformes de época. ¡Buen viaje!",
   "why": "Es un tren de vapor de mil novecientos veinte que hace un viaje especial a Aranjuez."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 3, "cats": ["marcadores"], "es": "ES-10", "pc": "FN invitar (¿vienes?) · antiguos compañeros",
   "lab": "Contestador", "voice": "DIANA/RADIO", "sound": BP,
   "text": "Hola, Paco, soy Lola, del colegio San José. ¿Te acuerdas de mí? Estamos organizando una cena con los compañeros de nuestra clase para el sábado veinte. ¡Vamos a ser más de treinta! ¿Vienes? Llámame y te cuento.",
   "why": "Lola invita a Paco a una cena con sus compañeros del colegio. Es una invitación: nadie dice que no puede ir (K sobra)."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 6, "cats": ["epocas"], "es": "ES-10", "pc": "en los años setenta · LX objetos antiguos",
   "lab": "Megafonía", "voice": "BOBBY/RADIO", "sound": CH,
   "text": "Señores clientes: en la planta baja tienen nuestro mercadillo retro, con ropa de los años setenta, discos de vinilo y juguetes antiguos. Solo este fin de semana, de diez de la mañana a nueve de la noche. ¡No se lo pierdan!",
   "why": "En el centro comercial hay un mercadillo con ropa, discos y juguetes de otra época."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 5, "cats": ["etapas"], "es": "ES-10", "pc": "FN dar las gracias · LX familia (bisabuela)",
   "lab": "Contestador", "voice": "DANIEL_CO/RADIO", "sound": BP,
   "text": "Hola, abuela, soy Marcos. Muchas gracias por el libro de recetas de la bisabuela. ¡Me encanta! Ya he hecho las croquetas y estaban buenísimas. El domingo te llevo unas para probar. ¡Un beso muy grande!",
   "why": "Marcos le da las gracias a su abuela por el libro de recetas."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 7, "cats": ["yatodavia", "inventos"], "es": "ES-10", "pc": "ya no + presente · ahora",
   "lab": "Megafonía", "voice": "TATIANA/RADIO", "sound": CH,
   "text": "Estimados visitantes: les informamos de que el museo ya no tiene servicio de audioguías. Ahora pueden escuchar las explicaciones gratis en su móvil, con la aplicación del museo. Muchas gracias.",
   "why": "El museo ya no tiene audioguías. Habla del museo, pero no de su horario (B sobra)."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 8, "cats": ["imperfecto", "habitos"], "es": "ES-10", "pc": "imperfecto (había, íbamos) · antes / ahora",
   "lab": "Contestador", "voice": "JUAN_CARLOS_2/RADIO", "sound": BP,
   "text": "Hola, Pepe, soy Antonio. Ayer pasé por la plaza del Carmen. ¿Te acuerdas? Antes allí había un cine y una heladería, y nosotros íbamos todos los domingos. ¡Ahora hay un banco! Llámame y tomamos un café.",
   "why": "Antonio recuerda cómo era antes la plaza del Carmen: había un cine y una heladería."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

REPARTO = """# REPARTO DE VOCES U09 (ninguna protagonista de la U08)
# T1 conversaciones (v3, ritmo natural): 0 chica y abuelo = AITANA + ABUELO_CHARLIE (Latinoamérica, mayor)
#   1 amigas con fotos = FIONA + EVA · 2 cena = SARA_2 + DANIEL_ES · 3 compañeros de trabajo = OSCAR + ANA_MARIA (México)
#   4 tienda de objetos antiguos = CRISTINA_LAT + AGUSTIN (Argentina) · 5 amigos en la calle = JANET (Argentina) + VOLU
#   6 tienda de fotografía = MARIO + NIEVE (Argentina, mayor)
# T2 radio (perfil /RADIO, con sintonía antes de cada audio): 0 exposición = SERGIO · 1 encuesta abuelos = MARINA_ES
#   2 escuela de baile = TAMARA (México) · 3 «Nuestra historia» = DIEGO_PE (Perú) · 4 biblioteca = LYDIA
#   5 tranvía = DAVID_LAT (Latinoamérica) · 6 «Así éramos» = ZABRA (Latinoamérica)
# T3 conversación entre amigos: INÉS = SARA_JOVEN · RAÚL = DANI
# T4 mensajes (/RADIO): 0 contestador residencia = NINOSKA (Latinoamérica) · 1 contestador Elena = LINA (Colombia)
#   2 megafonía estación = LUIS_VEGA · 3 contestador Lola = DIANA (Colombia) · 4 megafonía centro comercial = BOBBY
#   5 contestador Marcos = DANIEL_CO (Colombia) · 6 megafonía museo = TATIANA (Latinoamérica) · 7 contestador Antonio = JUAN_CARLOS_2 (Latinoamérica)
# Efectos: sintonía de radio (T2), din-don de megafonía y pitido de contestador (T4); siempre la misma descripción (caché)"""

# ---------------- ESCRITURA ----------------
ESCRITA = {"t1": {"instr": "Un amigo le escribe porque está preparando un trabajo para su clase.",
  "input": ["¡Hola! ¿Qué tal? En mi clase de Historia estamos haciendo un trabajo sobre cómo era la vida de los niños antes en otros países. ¿Me ayudas? ¿Cómo era tu ciudad cuando eras pequeño? ¿Qué hacías después del colegio? ¡Gracias!", "Un abrazo,<br>Hugo"],
  "lead": "Conteste a su amigo. En el correo tiene que:",
  "pautas": ["saludar;", "explicar cómo era la ciudad o el pueblo donde vivía de pequeño/a;", "contar qué hacía normalmente después del colegio y los fines de semana;", "decir qué cosas de su infancia ya no existen o han cambiado;", "despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Una revista busca textos de sus lectores con este título: «Yo a los quince años». Escriba un texto sobre usted. Hable de:",
   "pautas": ["dónde vivía y con quién;", "cómo era usted (físico y carácter);", "qué hacía en su tiempo libre y con quién;", "qué cosas de entonces todavía hace y qué cosas ya no hace;", "qué época le gusta más, la de entonces o la de ahora, y por qué."]},
  "op2": {"title": "Opción 2", "intro": "Ramón es un vecino de su pueblo. Aquí tiene tres fotos de su vida.",
   "photos": ["1975. Ramón tiene veinticinco años, lleva bigote y una gorra de marinero. Está en su barca, en el puerto del pueblo, con redes de pesca.",
              "1990. Ramón y su mujer abren un restaurante pequeño en el puerto. Están en la puerta con sus dos hijos.",
              "Hoy. Ramón tiene setenta y cinco años y el pelo blanco. Está en el puerto con su nieta: le enseña cómo se hace un nudo marinero."],
   "ficha": [], "intro2": "Escriba un texto sobre Ramón. Hable de:",
   "pautas": ["cómo era Ramón de joven y a qué se dedicaba;", "qué cambió en su vida en los años noventa;", "cómo es su vida hoy: qué cosas ya no hace y qué cosas todavía hace."],
   "img": "U09_escrita.jpg", "imgAlt": "Tres fotos de la vida de Ramón: de joven en su barca, con su familia en el restaurante y hoy con su nieta en el puerto"},
  "min": 70, "max": 80}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: mi infancia", "pautas": ["dónde vivía y cómo era su casa;", "cómo era usted de niño/a (físico y carácter);", "a qué jugaba y con quién;", "cómo era su colegio y sus profesores;", "qué cosas de su infancia todavía hace hoy y cuáles ya no."]},
  {"title": "Opción 2: un invento que ha cambiado nuestra vida", "pautas": ["qué invento es (internet, el móvil, el avión, la televisión...);", "cómo era la vida antes de ese invento;", "qué podemos hacer ahora gracias a él;", "cuándo y para qué lo usa usted;", "si cree que tiene también cosas negativas."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1", "desc": "Un mercadillo de antigüedades en una plaza, un domingo por la mañana de otoño con sol. Una señora con un abrigo rojo y gafas de sol en la cabeza mira un tocadiscos antiguo; el vendedor, un hombre con barba gris y gorra, le enseña un disco. Al lado hay cajas de discos, radios viejas, lámparas y muñecas. Detrás, mucha gente pasea y un niño señala un tren de juguete.", "img": "U09_oral_foto1.jpg"},
  {"title": "Fotografía 2", "desc": "Una tienda de fotografía pequeña, una tarde de invierno con lluvia. Un señor mayor con boina y bufanda deja en el mostrador una caja de zapatos llena de fotos antiguas en blanco y negro. Su nieta, una niña de unos diez años con un chubasquero amarillo, mira una foto y se ríe. La dependienta, una mujer joven con un tatuaje en el brazo, escanea una foto. Fuera llueve y no pasa nadie por la calle.", "img": "U09_oral_foto2.jpg"}],
  "pautas": ["las personas: cómo son, qué ropa llevan, qué están haciendo;", "el lugar: dónde están, qué tiempo hace, qué cosas hay y dónde están;", "qué cosas de la foto son de otra época y cómo cree que se usaban antes;", "qué cree que van a hacer después."]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1", "intro": "Usted está en un mercadillo de antigüedades y quiere comprar un regalo para una persona de su familia. Hable con el vendedor (su profesora). Tiene que:", "pautas": ["saludar y explicar qué busca y para quién es;", "explicar por qué quiere ese objeto (qué recuerdos tiene esa persona de su época);", "preguntar el precio, si funciona y cómo se puede pagar;", "decidir qué compra y despedirse."]},
  {"title": "Si eligió la fotografía 2", "intro": "Usted tiene muchas fotos antiguas de su familia y quiere pasarlas al ordenador. Va a una tienda de fotografía. Hable con el dependiente (su profesora). Tiene que:", "pautas": ["saludar y explicar qué quiere hacer;", "explicar de qué época son las fotos y quién aparece en ellas;", "preguntar el precio y cuándo puede recogerlas;", "aceptar o no las condiciones, dar sus datos y despedirse."]}]}}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (mi infancia): ¿Qué hacía en verano cuando era pequeño/a? · ¿Quién era su mejor amigo/a y cómo era?
    Opción 2 (un invento): ¿Cómo hablaba la gente con su familia lejana antes de ese invento? · ¿Qué otro invento usa todos los días?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (mercadillo): ¿Qué cree que quiere comprar la señora? · ¿Había alguna de estas cosas en casa de sus abuelos?
    Foto 2 (tienda de fotografía): ¿Qué cree que hay en las fotos del señor? · ¿Por qué cree que se ríe la niña?
  Tarea 3 — su papel (aquí sí conversa: pregunte, reaccione y provoque un pequeño problema):
    Foto 1 (vendedor/a del mercadillo, de usted): tocadiscos de los años setenta, 90 euros; discos de vinilo, 5 euros
    cada uno; radio antigua, 60 euros. Pregunte «¿Para quién es?» y «¿Esa persona tenía uno antes?».
    Problema: el tocadiscos funciona, pero la aguja está rota (una nueva cuesta 15 euros) y solo acepta efectivo;
    si negocia, ofrézcale el tocadiscos con dos discos por 85 euros.
    Foto 2 (dependiente/a de la tienda de fotografía, de usted): pasar fotos al ordenador, 50 céntimos por foto
    (más de cien fotos, 40 céntimos); se entregan en una memoria USB en una semana; ampliar una foto, 10 euros.
    Pregunte «¿Cuántas fotos son?», «¿De qué años son?» y «¿Quién sale en ellas?». Problema: algunas fotos
    están rotas y tardan dos semanas, o la máquina está estropeada hasta el lunes. Pida nombre y teléfono.
  Al reaccionar, que use el imperfecto para explicar (mi abuelo tenía uno igual; estas fotos eran de mi madre),
  fórmulas de cortesía (quería..., ¿cuánto cuesta?, ¿puede...?) y que salude, agradezca y se despida.
  Qué mirar en esta unidad: imperfecto regular e irregular (era, iba, veía) y su tilde en -ía; hábitos y
  descripciones con antes / de pequeño / cuando era...; contraste con el presente (antes... / ahora...); ya no /
  todavía + presente; marcadores (en aquella época, entonces, hoy en día); en la descripción, hay / está /
  están + gerundio y creo que van a...; léxico de épocas, objetos antiguos y etapas de la vida."""
ERRORES = """  *Yo eraba / *iba → *ía (era, iba); *veiba / *vía (veía); *tenia, *vivia sin tilde (tenía, vivía); *Cuando era niño, soy
  muy tímido (era); *Antes vivo en Sevilla (vivía); *Antes yo jugé / *jugué mucho al fútbol para un hábito (jugaba);
  *Habían muchos coches (había); *Ya no vivo en Madrid todavía / *Todavía no vivo aquí para decir que sigue (todavía vivo);
  *No vivo ya (ya no vivo); *En los 60s / *en los años sesentas (en los años sesenta); *En el siglo veinte principio (a
  principios del siglo veinte); *Estoy de acuerdo de eso (con eso); *Yo pienso que sí, pero... sin conectores al debatir."""

# ---------------- IMÁGENES: FOTOS CON VARIEDAD REAL ----------------
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "mercadillo de antigüedades en una plaza un domingo de otoño",
  "personas": "una clienta y un vendedor, con mucha gente paseando alrededor", "edades": "clienta de unos 55 años, vendedor de unos 70, un niño de unos 6 años con su padre de unos 35",
  "aspecto": "clienta con un abrigo rojo, pañuelo de cuadros y gafas de sol en la cabeza; vendedor con barba gris, gorra de lana y chaleco de punto; un padre joven con barba y el niño sobre sus hombros; una pareja de chicos con mochilas",
  "espacio": "exterior", "lugar": "plaza mayor de una ciudad española con soportales, puestos con toldos y mesas plegables", "momento": "mañana",
  "estacion": "otoño", "tiempo": "sol, cielo despejado y hojas secas en el suelo", "gente": "mucha gente: la plaza está llena",
  "accion": "la clienta mira un tocadiscos antiguo y el vendedor le enseña un disco de vinilo",
  "fondo": "el niño señala un tren de juguete de metal en otro puesto; una mujer prueba un sombrero delante de un espejo antiguo; palomas en la plaza",
  "objetos": "tocadiscos, cajas de discos de vinilo, radios antiguas, una máquina de escribir, lámparas, muñecas de porcelana, relojes, cámaras de fotos viejas, trenes de juguete, postales",
  "problema": "la clienta quiere el tocadiscos, pero le parece caro y no sabe si funciona; el vendedor solo acepta efectivo"},
 "oral_foto2": {"situacion": "tienda de fotografía de barrio en una tarde de lluvia de invierno",
  "personas": "un abuelo con su nieta y una dependienta", "edades": "abuelo de unos 80 años, nieta de unos 10 y dependienta de unos 28",
  "aspecto": "abuelo con boina, bufanda de cuadros, gafas de pasta y bastón; nieta con un chubasquero amarillo y botas de agua; dependienta con el pelo rapado por un lado, un tatuaje de flores en el brazo y un jersey negro",
  "espacio": "interior", "lugar": "tienda pequeña y antigua de fotografía de un barrio, con un mostrador de madera y un escáner", "momento": "tarde (ya casi de noche fuera)",
  "estacion": "invierno", "tiempo": "llueve mucho; se ven gotas en el escaparate", "gente": "vacía: solo el abuelo, la nieta y la dependienta; nadie en la calle",
  "accion": "el abuelo deja en el mostrador una caja de zapatos llena de fotos antiguas en blanco y negro y la dependienta escanea una",
  "fondo": "la niña mira una foto de boda antigua y se ríe; en la pared hay fotos de bodas y comuniones de otras épocas; un paraguas mojado en un paragüero",
  "objetos": "caja de zapatos, fotos en blanco y negro, escáner, ordenador, álbumes de fotos, marcos, cámaras antiguas en una vitrina, paraguas, bastón",
  "problema": "algunas fotos están rotas o muy estropeadas y el abuelo tiene prisa porque quiere un regalo para el cumpleaños de su mujer"},
 "escrita": {"situacion": "la vida de un pescador de pueblo antes y ahora",
  "personas": "Ramón (en tres momentos), su mujer, sus dos hijos y su nieta",
  "edades": "Ramón a los 25, a los 40 y a los 75 años; hijos de unos 8 y 10 años; nieta de unos 7",
  "aspecto": "Ramón joven con bigote negro y gorra de marinero; de mayor, con el pelo blanco, jersey de lana y manos grandes; su mujer con delantal en la puerta del restaurante",
  "espacio": "exterior", "lugar": "puerto pequeño de un pueblo de Galicia", "momento": "mañana en las tres fotos",
  "estacion": "verano (1975), primavera (1990), otoño (hoy)", "tiempo": "sol y nubes", "gente": "solo la familia; algún barco al fondo",
  "accion": "pescar en la barca; abrir el restaurante con la familia; enseñar a su nieta a hacer un nudo marinero",
  "fondo": "casas de piedra del puerto, barcas de colores, gaviotas",
  "objetos": "barca, redes, cuerdas, gorra, cartel del restaurante, mesas en la terraza, cuerda con un nudo",
  "problema": "Ramón ya no puede pescar, pero todavía va al puerto todas las mañanas"},
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
}

IMG_PROMPTS = {
 "portada": "Photorealistic, candid photo split in a natural way by time: a family in a bright Spanish living room in the afternoon looking together at an old photo album on a wooden table; a grandmother in her eighties with white hair and a cardigan points at a black and white photo, her teenage grandson with headphones around his neck holds up his smartphone next to it to compare, a woman in her forties laughs; on the table an old film camera, a cassette tape and a tablet; warm window light, no readable text, 16:9",
 "oral": "Photorealistic, candid photo in a small, bright language classroom in the afternoon: a teacher in her fifties with short grey hair and red glasses and an adult male student in his forties with a shaved head and a denim shirt sit face to face and talk; the student shows her an old black and white family photo and smiles while explaining it; a notebook, a pen and a cup of coffee on the table, a plant and a large window behind them, no readable text, 3:2",
 "escrita": "Photorealistic triptych, three separate photos side by side of equal size with thin white borders, the same man at three moments of his life in a small fishing port in Galicia, Spain, stone houses and colourful boats in the background. Left: 1970s film photo look with warm faded colours, summer morning, a man of about 25 with a black moustache and a sailor cap stands in his small wooden fishing boat holding fishing nets. Centre: 1990s photo look, spring morning, the same man at about 40 with his wife in an apron and their two children of about 8 and 10 stand smiling at the door of a small seafood restaurant with tables on a terrace. Right: modern photo, autumn morning, the same man at about 75 with white hair, a wool jumper and big hands sits on the harbour wall teaching his granddaughter of about 7 how to tie a sailor's knot with a rope, seagulls flying. Candid, natural light, no readable text, 3:1",
 "oral_foto1": "Photorealistic, candid photo of a busy antiques flea market in an arcaded main square of a Spanish city on a sunny autumn Sunday morning, dry leaves on the ground, clear blue sky: at a stall with a striped awning, a woman of about 55 with a red coat, a checked scarf and sunglasses on her head looks at a vintage record player; the vendor, a man of about 70 with a grey beard, a wool cap and a knitted waistcoat, shows her a vinyl record; on the folding tables boxes of vinyl records, old radios, a typewriter, lamps, porcelain dolls, clocks and old cameras; in the background a crowd strolls, a young bearded father carries his son of about 6 on his shoulders and the boy points at a metal toy train at another stall, a woman tries on a hat in front of an antique mirror, pigeons in the square; bright morning light, no readable text, 3:2",
 "oral_foto2": "Photorealistic, candid photo inside a small old-fashioned neighbourhood photography shop on a rainy winter evening, almost dark outside, raindrops on the shop window and an empty street: at a wooden counter, an elderly man of about 80 with a beret, a checked scarf, thick glasses and a walking stick puts down a shoebox full of old black and white photos; his granddaughter of about 10 with a yellow raincoat and rain boots looks at an old wedding photo and laughs; the shop assistant, a woman of about 28 with one side of her head shaved, a flower tattoo on her arm and a black jumper, scans a photo on a flatbed scanner next to a computer; on the walls framed wedding and communion photos from other decades, old cameras in a glass cabinet, a wet umbrella in an umbrella stand; warm indoor light, no readable text, 3:2",
}
IMG_DESC = {"portada": "familia mirando un album de fotos antiguas con un movil al lado", "oral": "clase: alumno ensena una foto antigua a la profesora", "escrita": "tres fotos de Ramon: barca, restaurante con su familia y con su nieta", "oral_foto1": "mercadillo de antiguedades en una plaza, otono, mucha gente", "oral_foto2": "tienda de fotografia, invierno con lluvia: abuelo, nieta y dependienta"}
CA1_DESC = {0: "pelota / bicicleta / tren de madera", 1: "pelo largo rizado / muy corto / trenzas", 2: "casa en el campo / piso en la ciudad / casa cerca de la playa", 3: "natacion / baloncesto / tenis", 4: "tocadiscos / camara de fotos / maquina de escribir", 5: "comida familiar / futbol / cine", 6: "foto de boda / foto en la playa / foto de bebe"}

LECTURA = [CL1, CL2, CL3, CL4]
AUDITIVA = [CA1, CA2, CA3, CA4]
