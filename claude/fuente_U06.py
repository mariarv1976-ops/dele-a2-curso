# -*- coding: utf-8 -*-
# FUENTE DE LA UNIDAD 6 (fase 1) · Guía del ocio
# Desde la U06: EXAMEN COMPLETO · lectura T1+T2+T3+T4 (60 min, 25 ítems) · auditiva T1+T2+T3+T4 (40 min, 25 ítems)
U = "06"
TITLE = "Guía del ocio"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress (cambiar si se suben otro mes)
TIEMPOS = {"lectura": 60, "auditiva": 40}
RECORDATORIO = [
 "Hablar de experiencias con el pretérito perfecto: ¿Has estado alguna vez en...? Nunca he montado a caballo. He ido dos veces. Participios irregulares: visto, hecho, dicho, escrito, puesto, vuelto, abierto, roto.",
 "Perfecto o indefinido: hoy, esta semana, este año, alguna vez → he visitado; ayer, el sábado pasado, en 2019, hace dos años → visité.",
 "Ya / todavía no: ¿Ya has visto la exposición? Sí, ya la he visto / No, todavía no la he visto.",
 "Valorar experiencias y lugares: me ha gustado / me gustó, me ha encantado / me encantó, me ha parecido / me pareció + adjetivo; lo he pasado / lo pasé genial, fatal; ¡Qué bonito!, ¡Qué rollo!, ¡Qué ciudad tan bonita!",
 "Hablar de planes e intenciones: ir a / pensar / querer + infinitivo, con esta tarde, este fin de semana, mañana, dentro de dos meses, el año que viene.",
 "Léxico de actividades y lugares de ocio (ir de copas, hacer senderismo, montar a caballo, ver un partido...) y para describir lugares: ambiente, decoración, servicio y precios.",
]
TIPS_INICIO = [
 "<b>Desde esta unidad, el examen es completo:</b> lectura 60 minutos (4 tareas, 25 preguntas) y auditiva 40 minutos (4 tareas, 25 preguntas), como el día del DELE. Reparte el tiempo de la lectura: entre 12 y 18 minutos por tarea, según la tarea.",
 "<b>Fíjate en los marcadores de tiempo:</b> «esta semana he ido», «ayer fui», «el sábado voy a ir». Muchas preguntas de esta unidad dependen de si algo ya ha pasado, todavía no ha pasado o es solo un plan.",
]
CATS = {
 "perfecto": {"name": "Pretérito perfecto y experiencias (¿Has estado alguna vez...?)",
  "repaso": "Presente de haber + participio: he, has, ha, hemos, habéis, han + visitado, comido, vivido. Participios irregulares: abrir > abierto, decir > dicho, escribir > escrito, hacer > hecho, poner > puesto, romper > roto, ver > visto, volver > vuelto. Para experiencias sin decir cuándo: ¿Has estado alguna vez en Roma? Nunca he hecho submarinismo. He ido dos veces. Nada va entre haber y el participio: ¿Ya has ido? (no *¿Has ya ido?). En el libro: unidad 6, el pretérito perfecto y hablar de experiencias.",
  "reto": "Escribe tres cosas que has hecho alguna vez y tres que no has hecho nunca."},
 "contraste": {"name": "Perfecto o indefinido (esta semana / la semana pasada)",
  "repaso": "Perfecto con tiempos que llegan hasta ahora: hoy, esta mañana, esta semana, este año, alguna vez. Indefinido con tiempos terminados: ayer, anoche, el sábado pasado, en 2020, hace tres días. Esta mañana he ido al gimnasio / Ayer fui al cine. En partes de España y en América se usa más el indefinido. En el libro: unidad 6, usos del perfecto y del indefinido. Repasa también la ficha «Contraste indefinido y compuesto» que te da tu profesora.",
  "reto": "Escribe cinco cosas: tres que has hecho esta semana y dos que hiciste el fin de semana pasado."},
 "yatodavia": {"name": "Ya / todavía no",
  "repaso": "Ya = algo esperado ha pasado: Ya he comprado las entradas. Todavía no = algo esperado no ha pasado (pero va a pasar): Todavía no he visto la película. Pregunta: ¿Ya has terminado? Respuestas cortas: Sí, ya. / No, todavía no. En el libro: unidad 6, ya / todavía no.",
  "reto": "Piensa en tus planes de este mes: escribe tres cosas que ya has hecho y tres que todavía no has hecho."},
 "valorar": {"name": "Valorar experiencias (gustar, encantar, parecer; ¡Qué...!)",
  "repaso": "Me ha gustado / me gustó la película; me han encantado / me encantaron los museos; me ha parecido / me pareció + adjetivo (interesante, aburrido, una maravilla, un rollo). Pasarlo bien, genial, fatal. Exclamativas: ¡Qué bonito!, ¡Qué pena!, ¡Qué ciudad tan / más bonita! En el libro: unidad 6, gustar, encantar y parecer para valorar; frases exclamativas.",
  "reto": "Valora tres cosas que hiciste el último fin de semana con me gustó, me encantó y me pareció."},
 "planes": {"name": "Planes e intenciones (ir a, pensar, querer + infinitivo)",
  "repaso": "Ir a + infinitivo (voy a ir), pensar + infinitivo (pienso descansar), querer + infinitivo (quiero ver la exposición). También el presente para planes firmes: mañana ceno con Ana. Marcadores: esta tarde, este fin de semana, mañana, pasado mañana, el mes que viene, dentro de dos semanas. En el libro: unidad 6, hablar de intenciones y proyectos; referirse al futuro.",
  "reto": "Escribe tus planes para el próximo fin de semana con voy a, pienso y quiero."},
 "ocio": {"name": "Actividades y lugares de ocio",
  "repaso": "Culturales (ir al teatro, a un concierto, a una exposición, ver una obra), deportivas (hacer senderismo, submarinismo, ir en bici, montar a caballo, correr una maratón), sociales (salir de copas, ir de tapas, comer fuera, quedar con amigos). Palabras de la agenda: entrada, taquilla, sesión, función, aforo, entrada libre, apuntarse. En el libro: unidad 6, léxico de actividades de ocio.",
  "reto": "Escribe tu fin de semana ideal con una actividad cultural, una deportiva y una social."},
 "lugares": {"name": "Describir y valorar lugares (ambiente, decoración, servicio, precio)",
  "repaso": "Ambiente agradable, acogedor, tranquilo, cosmopolita; decoración sencilla, moderna, original, anticuada; servicio amable, antipático, rápido, lento; precios económicos, altos, ajustados. El restaurante me pareció caro, pero la comida estaba buenísima. En el libro: unidad 6, describir y valorar lugares.",
  "reto": "Describe tu bar o restaurante favorito con una frase sobre el ambiente, la decoración, el servicio y el precio."},
}
ESTRATEGIAS_NUEVAS = {}

# ---------------- LECTURA ----------------
CL1 = {"n": 1, "type": "mail",
 "instr": "Usted va a leer el correo electrónico que Marta ha escrito a su amiga Ana. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Fíjate en el tiempo de cada cosa: lo que Marta ya ha hecho, lo que hizo ayer y lo que va a hacer.",
 "head": ["De: Marta", "Para: Ana", "Asunto: ¡Saludos desde Cádiz!"],
 "body": [
  "Hola, Ana:",
  "¿Qué tal todo por Madrid? Yo llevo cinco días en Cádiz por el curso de fotografía y estoy encantada. ¡Qué ciudad tan bonita! Esta semana he hecho muchísimas cosas: he paseado por el casco antiguo, he subido a una torre con unas vistas increíbles y he probado el pescaíto frito, un plato típico de aquí, en un bar del mercado. ¡Buenísimo!",
  "El curso también me está gustando mucho. Las clases son por la mañana y por la tarde salimos a hacer fotos por la ciudad. El profesor es un poco serio, pero explica muy bien. Ayer fuimos a una playa al lado del casco antiguo para fotografiar la puesta de sol y me pareció el lugar más bonito del viaje.",
  "Lo único malo ha sido el hotel. La habitación es pequeña y el primer día el aire acondicionado no funcionó. Me cambiaron de habitación, pero la nueva da a una calle con mucho ruido... ¡Y el desayuno me pareció carísimo! Así que ahora desayuno en una cafetería pequeña de la plaza, mucho más barata y con un ambiente muy agradable.",
  "El sábado quiero ir a un concierto de flamenco en una peña. ¿Por qué no vienes el fin de semana? En tren son cuatro horas. Si vienes, el domingo podemos hacer una excursión a Vejer, un pueblo blanco precioso. Mis compañeros ya lo han visitado y dicen que es una maravilla. Yo todavía no he ido.",
  "Y tú, ¿qué tal en el trabajo nuevo? ¿Ya has conocido a todos tus compañeros? ¿Qué tal tu jefa? Cuéntamelo todo.",
  "Un beso,<br>Marta"],
 "items": [
  {"n": 1, "q": "Marta escribe a Ana para...", "o": ["contarle su viaje e invitarla a visitarla.", "pedirle información sobre un curso de fotografía.", "contarle que ha empezado un trabajo nuevo."], "ok": 0,
   "cats": ["ocio", "planes"], "es": "ES-02", "pc": "FN contar experiencias · FN proponer e invitar",
   "why": "Marta le cuenta lo que ha hecho en Cádiz y le propone ir el fin de semana. Ella ya está haciendo el curso, y quien tiene un trabajo nuevo es Ana."},
  {"n": 2, "q": "Esta semana, Marta...", "o": ["ha hecho una excursión a un pueblo.", "ha probado comida típica.", "ha ido a un concierto de flamenco."], "ok": 1,
   "cats": ["perfecto", "ocio"], "es": "ES-07", "pc": "GR pretérito perfecto (esta semana he...) · LX ocio",
   "why": "Ha probado el pescaíto frito en un bar del mercado. La excursión a Vejer es solo una propuesta para el domingo, y el concierto es el sábado: todavía no ha ido."},
  {"n": 3, "q": "Según el correo, en el curso...", "o": ["solo hay clases por la mañana.", "el profesor es muy simpático.", "los alumnos trabajan también fuera de clase."], "ok": 2,
   "cats": ["ocio"], "es": "ES-03", "pc": "LX ocio (hacer fotos) · descripción de personas (U03)",
   "why": "Por la tarde salen a hacer fotos por la ciudad: trabajan también fuera del aula. Las clases no son solo por la mañana, y el profesor es un poco serio."},
  {"n": 4, "q": "Sobre el hotel, Marta dice que...", "o": ["su segunda habitación es ruidosa.", "el desayuno es barato.", "no quisieron cambiarla de habitación."], "ok": 0,
   "cats": ["lugares", "valorar"], "es": "ES-03", "pc": "LX valorar lugares · GR parecer (me pareció carísimo) · dar a (U04)",
   "why": "La nueva habitación da a una calle con mucho ruido. El desayuno le pareció carísimo, y sí la cambiaron de habitación."},
  {"n": 5, "q": "Marta propone a Ana...", "o": ["ir juntas a la playa a ver la puesta de sol.", "visitar con ella un lugar que no conoce.", "volver juntas a Madrid el domingo."], "ok": 1,
   "cats": ["yatodavia", "planes"], "es": "ES-08", "pc": "ya / todavía no · FN proponer (podemos + infinitivo)",
   "why": "Propone una excursión a Vejer, un pueblo que Marta todavía no ha visitado (sus compañeros sí). La puesta de sol en la playa la vio ayer con el curso, y no habla de volver a Madrid: el tren es para que venga Ana."},
 ]}

CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 15 minutos: menos de dos minutos por anuncio. Lee la pregunta primero y busca solo ese dato. Cuidado con <i>todos</i>, <i>solo</i>, <i>siempre</i> y <i>gratis</i>: suelen esconder la trampa.",
 "example": {"title": "CINE DE VERANO EN EL PARQUE",
   "body": "Todos los viernes de julio y agosto, cine al aire libre en el parque de los Pinos. Las películas empiezan a las 22:00, cuando ya es de noche. Entrada libre hasta completar el aforo. Puedes traer tu silla, tu manta y tu cena, pero no está permitido traer bebidas alcohólicas. Programa completo en la web del Ayuntamiento.",
   "q": "El cine de verano...", "o": ["es de pago.", "empieza cuando ya no hay luz.", "permite traer cualquier bebida."], "ok": 1,
   "why": "La opción correcta es la B porque las películas empiezan a las 22:00, cuando ya es de noche."},
 "items": [
  {"n": 6, "title": "MUSEO DE LA CIUDAD · HORARIO DE VERANO",
   "body": "Del 1 de julio al 31 de agosto, de martes a domingo, de 10:00 a 14:00 y de 18:00 a 21:00. Los lunes, cerrado. Entrada general: 5 €; estudiantes y mayores de 65 años: 3 €. Los domingos por la tarde, entrada gratuita. La sala 4 está cerrada por obras hasta septiembre. Visitas guiadas: sábados a las 11:00 (2 € más).",
   "q": "En verano, el museo...", "o": ["abre todos los días.", "es gratis los domingos por la mañana.", "no se puede visitar entero."], "ok": 2,
   "cats": ["ocio"], "es": "ES-04", "pc": "LX lugares de interés y ofertas culturales · horarios",
   "why": "La sala 4 está cerrada por obras: no se puede ver todo el museo. Los lunes cierra, y la entrada gratis es el domingo por la tarde, no por la mañana."},
  {"n": 7, "title": "GUÍA DE RESTAURANTES · LA HUERTA DE ROSA",
   "body": "Restaurante vegetariano con un ambiente tranquilo y acogedor y una decoración sencilla, con muchas plantas. Cocina de temporada con productos de la huerta de la familia. El menú del día (14 €) incluye primero, segundo, postre y bebida, solo de lunes a viernes. El servicio es amable, pero un poco lento cuando el local está lleno. Imprescindible reservar los sábados.",
   "q": "Según la guía, en este restaurante...", "o": ["el menú del día se puede pedir todos los días.", "a veces hay que esperar un poco.", "la decoración es muy moderna."], "ok": 1,
   "cats": ["lugares"], "es": "ES-03", "pc": "LX describir y valorar lugares (ambiente, decoración, servicio, precios)",
   "why": "El servicio es lento cuando el local está lleno: a veces hay que esperar. El menú es solo de lunes a viernes, y la decoración es sencilla."},
  {"n": 8, "title": "FORO DE VIAJES · ¿QUÉ HACER CON NIÑOS EN VALENCIA?",
   "body": "Mensaje de papa_viajero:<br>Hemos estado tres días en Valencia con nuestros hijos de seis y nueve años y lo hemos pasado genial. Lo que más les ha gustado: el acuario, aunque es bastante caro, y el parque del antiguo río, donde alquilamos bicis. El museo de ciencias nos pareció un poco aburrido para el pequeño. Un consejo: comprad las entradas por internet, que son más baratas.",
   "q": "Según este padre...", "o": ["sus hijos se aburrieron en el acuario.", "el acuario no es barato.", "las entradas en la taquilla son más baratas."], "ok": 1,
   "cats": ["valorar", "perfecto"], "es": "ES-03", "pc": "GR perfecto (hemos estado) · gustar y parecer para valorar · LX ocio",
   "why": "«El acuario, aunque es bastante caro» = no es barato. Lo aburrido fue el museo de ciencias, y las entradas más baratas son las de internet."},
  {"n": 9, "title": "ESCUELA DE SURF OLAS · CURSOS DE VERANO",
   "body": "¿Todavía no has probado el surf? ¡Este es tu verano! Cursos de una semana para adultos y niños a partir de ocho años, de lunes a viernes, dos horas al día. No necesitas experiencia. Nosotros te dejamos la tabla y el traje de neopreno. Grupos de seis personas como máximo. Precio: 120 €. Si vienes con un amigo, los dos tenéis un 15 % de descuento.",
   "q": "Para hacer el curso...", "o": ["hay que saber hacer surf.", "hay que llevar una tabla.", "no es necesario tener equipo."], "ok": 2,
   "cats": ["ocio", "yatodavia"], "es": "ES-06", "pc": "LX actividades deportivas · todavía no · dejar (U05)",
   "why": "La escuela deja la tabla y el traje: no hace falta tener equipo. No se necesita experiencia."},
  {"n": 10, "title": "NOTICIAS · EL FESTIVAL DE JAZZ CAMBIA DE LUGAR",
   "body": "El Festival de Jazz de la ciudad, que este año celebra su décima edición, no va a ser en la plaza Mayor como siempre, sino en el parque de la Alameda, porque la plaza está en obras. Las fechas no cambian: del 12 al 15 de julio. Los conciertos de la tarde son gratuitos; los de la noche cuestan 10 euros.",
   "q": "Este año el festival...", "o": ["se celebra por primera vez.", "se hace en un sitio diferente.", "tiene todos los conciertos gratis."], "ok": 1,
   "cats": ["ocio", "planes"], "es": "ES-04", "pc": "LX ofertas culturales · ir a + infinitivo",
   "why": "Este año va a ser en el parque, no en la plaza de siempre. Es la décima edición, y solo los conciertos de la tarde son gratis."},
  {"n": 11, "title": "SE BUSCAN COMPAÑEROS PARA HACER SENDERISMO",
   "body": "Somos un grupo de amigos de entre 40 y 60 años y salimos a la montaña un domingo al mes. Ya hemos hecho más de treinta rutas por la sierra. Las rutas son fáciles, de unas cuatro horas, y siempre comemos juntos en un restaurante del pueblo. No es necesario ser socio ni pagar nada: solo traer agua y buen calzado. Escríbenos: caminantes@correo.es",
   "q": "Este grupo...", "o": ["hace rutas difíciles.", "sale todos los domingos.", "no cobra por participar."], "ok": 2,
   "cats": ["ocio", "perfecto"], "es": "ES-03", "pc": "LX actividades deportivas · GR perfecto (ya hemos hecho)",
   "why": "No hay que pagar nada para ir con ellos. Las rutas son fáciles y salen un domingo al mes, no todos."},
  {"n": 12, "title": "TEATRO PRINCIPAL · AVISO A LOS ESPECTADORES",
   "body": "Por enfermedad de la actriz principal, se cancela la representación de «La casa de las flores» del viernes 8. Los espectadores con entrada para ese día pueden cambiarla por otra fecha (sábado 9 o domingo 10) o pedir la devolución del dinero en la taquilla hasta el jueves 14. Las entradas compradas por internet se devuelven automáticamente.",
   "q": "Las personas que tienen entrada para el viernes...", "o": ["pueden ver la obra otro día.", "tienen que ir siempre a la taquilla.", "pueden ver la obra con otra actriz."], "ok": 0,
   "cats": ["ocio"], "es": "ES-06", "pc": "LX espectáculos (función, representación, taquilla, devolución)",
   "why": "Pueden cambiar la entrada por el sábado o el domingo. A la taquilla solo van si quieren el dinero y no compraron por internet, y el viernes no hay función."},
  {"n": 13, "title": "NUEVO CAFÉ-LIBRERÍA LA PÁGINA",
   "body": "Desde el lunes, en la calle Olmo, 7. Un espacio luminoso y tranquilo para leer, tomar un buen café y descubrir libros. Los jueves por la tarde hay club de lectura (gratis, solo hay que apuntarse) y los sábados por la mañana, cuentacuentos para niños. Horario: de 9:00 a 21:00; domingos, cerrado. Con cada libro que compras, el café es gratis.",
   "q": "En La Página...", "o": ["te invitan a un café si compras un libro.", "los niños tienen actividades los jueves.", "abren todos los días."], "ok": 0,
   "cats": ["lugares", "ocio"], "es": "ES-03", "pc": "LX lugares de ocio · describir lugares (luminoso, tranquilo)",
   "why": "Con cada libro, el café es gratis: te invitan. El cuentacuentos es los sábados, y los domingos cierran."},
 ]}

CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos de tres personas que hablan de su último fin de semana. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 15 minutos. Lee primero las seis preguntas. Las tres personas hacen cosas parecidas (viajar, comer fuera, actividades): busca el detalle que las separa.",
 "texts": [
  {"name": "Nuria", "body": "Este fin de semana he estado en Granada con mi novio. Fuimos en tren el viernes por la tarde, porque no tenemos coche. El viaje fue muy cómodo. El sábado visitamos el palacio árabe y sus jardines: ¡qué maravilla! Eso sí, compramos las entradas con dos meses de antelación, porque siempre está todo lleno. Por la noche cenamos en el barrio antiguo; en Granada, con cada bebida te ponen una tapa gratis. El domingo queríamos subir a la sierra, pero llovió todo el día y nos quedamos en el hotel viendo películas. No importa: ya estamos pensando en volver en primavera para subir por fin a la sierra."},
  {"name": "Tomás", "body": "Yo he pasado el fin de semana en un pueblo de los Pirineos con mis dos hijos. Fuimos en coche desde Zaragoza, unas tres horas. Dormimos en una casa rural muy acogedora, con chimenea, jardín y una dueña amabilísima que nos preparó unos desayunos riquísimos. El sábado hicimos una ruta de senderismo de cinco horas hasta un lago. Mis hijos al principio protestaron mucho, pero al final les encantó. El domingo montamos a caballo por primera vez: ¡qué miedo pasé! Lo único malo fue la comida en el restaurante del pueblo: muy cara y no muy buena. Pero vamos a repetir en otoño, seguro."},
  {"name": "Rocío", "body": "Mi fin de semana ha sido muy tranquilo, porque me he quedado en Madrid. El sábado por la mañana fui al gimnasio, como todos los sábados, y luego quedé con unas amigas para ver una exposición de fotografía. A ellas les encantó, pero a mí me pareció bastante aburrida. Por la tarde fuimos a un concierto en un local pequeño: la música fue genial, pero hubo tanta gente que casi no vimos nada. El domingo no hice nada especial: leí, vi una serie, llamé a mis padres y comí en el restaurante peruano de mi calle, como casi todos los domingos. ¡Qué rico todo!"}],
 "items": [
  {"n": 14, "q": "¿Quién no pudo hacer todo lo que tenía pensado?", "ok": 0, "cats": ["planes", "contraste"], "es": "ES-03", "pc": "querer + infinitivo (queríamos subir) · indefinido",
   "why": "Nuria quería subir a la sierra el domingo, pero llovió y se quedaron en el hotel."},
  {"n": 15, "q": "¿Quién hizo una actividad nueva para él o ella?", "ok": 1, "cats": ["ocio", "perfecto"], "es": "ES-09", "pc": "experiencias (por primera vez) · LX actividades deportivas",
   "why": "Tomás montó a caballo por primera vez. Rocío va al restaurante peruano casi todos los domingos: no es nuevo."},
  {"n": 16, "q": "¿Quién tuvo una opinión diferente a la de sus acompañantes?", "ok": 2, "cats": ["valorar"], "es": "ES-09", "pc": "GR gustar, encantar y parecer para valorar",
   "why": "A las amigas de Rocío les encantó la exposición, pero a ella le pareció aburrida. A los hijos de Tomás, al final, les encantó la ruta, como a él."},
  {"n": 17, "q": "¿Quién tuvo que organizar algo con mucho tiempo?", "ok": 0, "cats": ["ocio"], "es": "ES-03", "pc": "LX entradas · con antelación",
   "why": "Nuria compró las entradas del palacio con dos meses de antelación."},
  {"n": 18, "q": "¿Quién no salió de su ciudad?", "ok": 2, "cats": ["contraste", "ocio"], "es": "ES-03", "pc": "GR perfecto (me he quedado) · LX ocio",
   "why": "Rocío se quedó en Madrid todo el fin de semana. Nuria y Tomás viajaron."},
  {"n": 19, "q": "¿Quién no quedó contento con el precio de una comida?", "ok": 1, "cats": ["lugares", "valorar"], "es": "ES-04", "pc": "LX valorar lugares (precios altos)",
   "why": "La comida del restaurante del pueblo le pareció a Tomás muy cara. Nuria habla de tapas gratis, y Rocío dice que la comida está muy rica, no habla del precio."}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un texto de un blog en el que una mujer cuenta su primer año después de jubilarse. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto. Atención a lo que Julia ya ha hecho, a lo que no salió bien y a lo que todavía no ha hecho.",
 "title": "Doce meses, doce primeras veces",
 "sub": "Blog «Nunca es tarde», de Julia Robles",
 "body": [
  "Me llamo Julia, tengo sesenta y cuatro años y el año pasado me jubilé después de treinta y cinco años como profesora de matemáticas. El primer día sin trabajo me senté en la cocina con un café y pensé: «¿Y ahora qué?». Entonces tuve una idea: escribir una lista con doce cosas que nunca he hecho y hacer una cada mes. Así nació este blog.",
  "En enero empecé con algo fácil: aprender a hacer pan. Fui a un curso de cuatro sábados en una panadería de mi barrio y ahora hago pan casi todas las semanas. Mis vecinos dicen que está buenísimo. En febrero me apunté a clases de baile. Mi marido, Ernesto, no quiso venir conmigo: dice que tiene dos pies izquierdos. Así que fui con mi vecina Pilar, y nos lo pasamos genial.",
  "El mes más difícil fue abril. Por primera vez en mi vida subí a una montaña de más de dos mil metros. Fui con un grupo de montaña de mi ciudad. Tardé siete horas y al día siguiente me dolió todo el cuerpo, pero las vistas desde arriba me parecieron increíbles. ¡Qué orgullosa me sentí!",
  "No todo ha salido bien. En junio quise aprender a nadar en el mar con un monitor, pero tuve tanto miedo que lo dejé después de dos clases. Y en agosto hice un curso de cocina japonesa: el sushi me salió tan mal que mis nietos todavía se ríen cuando se acuerdan. ¡Y yo también!",
  "Mi experiencia favorita, sin duda, ha sido la de octubre: viajé sola por primera vez. Pasé cinco días en Lisboa: visité museos, comí bacalao en restaurantes pequeños y escuché fado por la noche. Dormí en un albergue con gente joven de todo el mundo y conocí a una chica argentina que ahora es mi amiga. Nos escribimos casi todas las semanas. Mis hijos se preocuparon mucho, pero yo volví encantada.",
  "Ya he probado once de las doce cosas de la lista, y este blog ya tiene más de dos mil lectores. Todavía me falta la última: tocar el piano. He comprado un teclado de segunda mano y en enero voy a empezar las clases. ¿Y después? Pienso escribir una lista nueva, claro. Y esta vez quiero convencer a Ernesto para hacerla conmigo."],
 "items": [
  {"n": 20, "q": "Julia escribió su lista porque...", "o": ["se lo recomendó su marido.", "quería hacer cosas nuevas después de dejar de trabajar.", "tenía que escribir un blog para un curso."], "ok": 1,
   "cats": ["perfecto"], "es": "ES-03", "pc": "experiencias (cosas que nunca he hecho) · indefinido (me jubilé)",
   "why": "Al jubilarse pensó «¿Y ahora qué?» y decidió hacer doce cosas que nunca ha hecho. El blog nació de la lista, no al revés, y la idea fue suya."},
  {"n": 21, "q": "En febrero, Julia...", "o": ["fue a bailar con su marido.", "aprendió a hacer pan.", "hizo una actividad con una vecina."], "ok": 2,
   "cats": ["ocio"], "es": "ES-08", "pc": "LX actividades de ocio · apuntarse a",
   "why": "Fue a clases de baile con su vecina Pilar. Su marido no quiso ir, y el pan fue en enero."},
  {"n": 22, "q": "Sobre la excursión de abril, Julia dice que...", "o": ["le gustó mucho el paisaje.", "tardó poco tiempo.", "fue muy fácil."], "ok": 0,
   "cats": ["valorar"], "es": "ES-03", "pc": "parecer para valorar (me parecieron increíbles) · exclamativas",
   "why": "Las vistas desde arriba le parecieron increíbles. Fue el mes más difícil y tardó siete horas."},
  {"n": 23, "q": "Según el texto, Julia...", "o": ["ya sabe nadar en el mar.", "no terminó una de las actividades.", "cocina sushi para sus nietos."], "ok": 1,
   "cats": ["contraste"], "es": "ES-04", "pc": "indefinido (lo dejé) · LX ocio",
   "why": "Dejó las clases de natación después de dos clases. No sabe nadar en el mar, y el sushi le salió tan mal que sus nietos se ríen."},
  {"n": 24, "q": "En su viaje a Lisboa, Julia...", "o": ["viajó con sus hijos.", "durmió en un hotel de lujo.", "hizo una nueva amistad."], "ok": 2,
   "cats": ["contraste", "valorar"], "es": "ES-03", "pc": "indefinido (conocí) · perfecto (ha sido mi experiencia favorita)",
   "why": "Conoció a una chica argentina que ahora es su amiga. Viajó sola y durmió en un albergue."},
  {"n": 25, "q": "Ahora Julia...", "o": ["ya ha empezado sus clases de piano.", "tiene planes para el futuro.", "ha terminado toda la lista."], "ok": 1,
   "cats": ["yatodavia", "planes"], "es": "ES-07", "pc": "ya / todavía no · ir a, pensar, querer + infinitivo",
   "why": "Va a empezar el piano en enero, piensa escribir otra lista y quiere convencer a Ernesto. Todavía no ha empezado las clases y le falta una cosa de la lista."},
 ]}

# ---------------- AUDITIVA ----------------
# Cada conversación: pres (presentación del narrador), lines [(rol, voz, texto)], q, o, ok, why, cats, es, img, prompt
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación: las tres aparecen. Escucha bien el tiempo del verbo: «he ido», «voy a ir» y «todavía no» no significan lo mismo.",
 "example": {"q": "¿Adónde van a ir esta noche?", "o": ["al cine", "al teatro", "a un concierto"], "ok": 2,
   "pres": "Va a escuchar a dos amigos que hablan por teléfono.",
   "lines": [("Hombre", "DAVID_M2", "Oye, Lucía, ¿vamos al cine esta noche? Ponen la nueva película de ciencia ficción."),
             ("Mujer", "ESTELA", "Uf, ya la he visto. ¿Y si vamos al teatro? Hay una comedia muy buena."),
             ("Hombre", "DAVID_M2", "El teatro es muy caro... Mira, en la plaza hay un concierto gratis de un grupo de rock."),
             ("Mujer", "ESTELA", "¡Ah, genial! Pues vamos al concierto. ¿Quedamos a las nueve?"),
             ("Hombre", "DAVID_M2", "Vale, a las nueve en la plaza.")],
   "solucion": "La opción correcta es la letra ce. Van a ir a un concierto.",
   "img": "U06_CA1_0.jpg",
   "prompt": "Panel 1: a cinema screen with rows of red seats. Panel 2: a theatre stage with red curtains. Panel 3: a rock band playing on an outdoor stage in a town square."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Qué ha hecho hoy la mujer?", "o": ["ir al gimnasio", "comprar un regalo", "nadar en la piscina"], "ok": 1,
   "cats": ["perfecto", "contraste"], "es": "ES-07", "pc": "GR pretérito perfecto (hoy he...) · planes (mañana voy)",
   "pres": "Va a escuchar a una pareja que habla en casa por la noche.",
   "lines": [("Hombre", "MARTIN_3", "¡Hola! ¿Qué tal el día? ¿Al final has ido al gimnasio?"),
             ("Mujer", "SARA_JOVEN", "Uf, qué va, hoy no he tenido tiempo. Esta mañana he tenido una reunión larguísima y luego, por la tarde, he ido a comprar el regalo para tu madre."),
             ("Hombre", "MARTIN_3", "Ah, ¡genial! ¿Y la piscina? ¿Tú no vas los martes?"),
             ("Mujer", "SARA_JOVEN", "Sí, normalmente sí, pero hoy está cerrada. Así que mañana voy al gimnasio y a la piscina. ¡Las dos cosas!"),
             ("Hombre", "MARTIN_3", "¡Madre mía, qué energía!")],
   "why": "Por la tarde ha ido a comprar el regalo. No ha ido al gimnasio, y hoy la piscina está cerrada: va mañana.",
   "img": "U06_CA1_1.jpg", "prompt": "Panel 1: a woman lifting weights in a gym. Panel 2: a woman paying for a wrapped gift box in a shop. Panel 3: a woman swimming in an indoor swimming pool."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Qué lugar no ha visitado todavía el hombre?", "o": ["la catedral", "el castillo", "el museo"], "ok": 2,
   "cats": ["yatodavia", "ocio"], "es": "ES-06", "pc": "ya / todavía no · LX lugares de interés",
   "pres": "Va a escuchar a un turista que habla con una empleada en una oficina de turismo.",
   "lines": [("Mujer", "LINA", "Buenos días. ¿Ha estado ya en la catedral? Es lo más famoso de la ciudad."),
             ("Hombre", "JAVI_ROJAS", "Sí, ya la he visto, ayer por la mañana. Y también he subido al castillo. ¡Qué vistas!"),
             ("Mujer", "LINA", "¿Y el museo de arte moderno?"),
             ("Hombre", "JAVI_ROJAS", "Todavía no. Quiero ir esta tarde, pero no sé el horario."),
             ("Mujer", "LINA", "Abre de cinco a nueve. ¡Le va a encantar!")],
   "why": "Al museo todavía no ha ido: quiere ir esta tarde. La catedral y el castillo ya los ha visitado.",
   "img": "U06_CA1_2.jpg", "prompt": "Panel 1: a large gothic cathedral facade. Panel 2: a medieval castle on top of a hill. Panel 3: a modern art museum building with white geometric walls."},
  {"n": 3, "conv": "Conversación tres", "q": "¿Qué no le gustó a la mujer del restaurante?", "o": ["el camarero", "la comida", "el precio"], "ok": 0,
   "cats": ["lugares", "valorar"], "es": "ES-08", "pc": "parecer para valorar · LX servicio, precios",
   "pres": "Va a escuchar a dos compañeros de trabajo que hablan de un restaurante.",
   "lines": [("Hombre", "DAVID_M1", "¿Qué tal la cena de ayer en el japonés nuevo?"),
             ("Mujer", "MIA", "Pues la comida me pareció buenísima y el local es precioso, muy moderno."),
             ("Hombre", "DAVID_M1", "¿Y el precio? Dicen que es carísimo."),
             ("Mujer", "MIA", "Qué va, no fue caro. Lo único: el camarero fue un poco antipático y tardó muchísimo en traer los platos."),
             ("Hombre", "DAVID_M1", "Vaya. Bueno, si la comida es buena...")],
   "why": "No le gustó el camarero: fue antipático y lento. La comida le pareció buenísima y no fue caro.",
   "img": "U06_CA1_3.jpg", "prompt": "Panel 1: a waiter with a serious face holding a tray in a restaurant. Panel 2: a plate of sushi on a modern table. Panel 3: a restaurant bill on a small tray with coins."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Qué va a hacer el chico el domingo?", "o": ["ir a la playa", "ver un partido de fútbol", "estudiar"], "ok": 2,
   "cats": ["planes"], "es": "ES-07", "pc": "ir a / pensar + infinitivo · marcadores de futuro",
   "pres": "Va a escuchar a dos amigos que hablan de sus planes para el fin de semana.",
   "lines": [("Mujer", "CRISTINA_LAT", "Oye, ¿qué haces este finde? ¿Vienes a la playa con nosotros el sábado?"),
             ("Hombre", "JUAN_CARLOS_2", "Me encantaría, pero el sábado voy a ayudar a mi hermano con la mudanza."),
             ("Mujer", "CRISTINA_LAT", "¿Y el domingo? Hay un partido de fútbol en la tele, podemos verlo en el bar."),
             ("Hombre", "JUAN_CARLOS_2", "No puedo, de verdad. El domingo pienso estudiar todo el día: el lunes tengo un examen."),
             ("Mujer", "CRISTINA_LAT", "¡Qué rollo! Bueno, suerte con el examen.")],
   "why": "El domingo piensa estudiar todo el día. La playa es el sábado y no va, y el partido no lo va a ver.",
   "img": "U06_CA1_4.jpg", "prompt": "Panel 1: a sunny beach with umbrellas and towels. Panel 2: friends watching a football match on a TV in a bar. Panel 3: a young man studying at a desk with books and a laptop."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Qué ha hecho alguna vez la mujer?", "o": ["submarinismo", "montar en globo", "saltar en paracaídas"], "ok": 1,
   "cats": ["perfecto", "ocio"], "es": "ES-06", "pc": "experiencias (¿Has hecho alguna vez...? Nunca he...) · exclamativas",
   "pres": "Va a escuchar a dos amigos que hablan de experiencias.",
   "lines": [("Hombre", "RAFA", "Oye, Pilar, ¿has hecho alguna vez submarinismo?"),
             ("Mujer", "LUCIA", "No, nunca. Me da mucho miedo. Pero he montado en globo, en Turquía. ¡Qué experiencia!"),
             ("Hombre", "RAFA", "¡Qué envidia! ¿Y qué tal? ¿Te gustó?"),
             ("Mujer", "LUCIA", "Me encantó. Subimos muy temprano, al amanecer, y las vistas me parecieron increíbles."),
             ("Hombre", "RAFA", "¿Y paracaidismo? Yo quiero probarlo este verano."),
             ("Mujer", "LUCIA", "¡Qué va! ¿Estás loco? Saltar de un avión... ¡nunca!")],
   "why": "Ha montado en globo en Turquía. Submarinismo nunca, y el paracaidismo es lo que quiere probar él.",
   "img": "U06_CA1_5.jpg", "prompt": "Panel 1: a scuba diver underwater with fish. Panel 2: a colourful hot air balloon flying over a rocky landscape. Panel 3: a parachutist in the sky with an open parachute."},
  {"n": 6, "conv": "Conversación seis", "q": "¿A qué clase se apunta la mujer?", "o": ["pádel", "yoga", "natación"], "ok": 0,
   "cats": ["ocio", "valorar"], "es": "ES-05", "pc": "LX actividades deportivas · apuntarse · gustar en pasado",
   "pres": "Va a escuchar a una mujer que habla con el recepcionista de un polideportivo.",
   "lines": [("Mujer", "RITA", "Hola, buenas tardes. Quería información sobre las clases."),
             ("Hombre", "DIEGO", "Muy bien. Tenemos yoga, natación y pádel."),
             ("Mujer", "RITA", "El yoga ya lo he probado y no me gustó mucho. ¿La natación es por la mañana?"),
             ("Hombre", "DIEGO", "Sí, a las ocho."),
             ("Mujer", "RITA", "Uf, muy temprano. ¿Y el pádel?"),
             ("Hombre", "DIEGO", "Por la tarde, a las siete."),
             ("Mujer", "RITA", "Perfecto, pues me apunto a pádel.")],
   "why": "Se apunta a pádel, por la tarde. El yoga ya lo ha probado y no le gustó, y la natación es demasiado temprano.",
   "img": "U06_CA1_6.jpg", "prompt": "Panel 1: a woman playing padel tennis with a racket on a glass-walled court. Panel 2: a woman doing a yoga pose on a mat. Panel 3: a woman swimming in a lane of a sports centre pool."},
 ]}

RADIO_FX = "SONIDO 2: Short bright radio station jingle, three cheerful synth notes, clean, no voices, no background noise"
CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. En la primera escucha marca una opción; en la segunda, compruébala. Fíjate en las condiciones: qué día, a qué hora, cuánto cuesta, para quién.",
 "example": {"q": "Según el anuncio, el parque acuático Las Olas...", "o": ["abre todo el año.", "los martes no cobra a los niños.", "está en el centro de la ciudad."], "ok": 1,
   "why": "La opción correcta es la B porque los martes los niños entran gratis.",
   "lab": "Locutor", "voice": "MARTIN_1/RADIO",
   "text": "¿Todavía no has estado en el parque acuático Las Olas? ¡Este verano tienes que venir! Más de veinte toboganes, piscinas de olas y zona de restaurantes. Abrimos del quince de junio al quince de septiembre, a diez minutos de la ciudad. Y los martes, los niños entran gratis.",
   "solucion": "La opción correcta es la letra be, porque los martes los niños entran gratis."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "Según la noticia, el concierto del sábado...", "o": ["es gratis.", "es por la mañana.", "es la presentación de un disco."], "ok": 2,
   "cats": ["ocio"], "es": "ES-03", "pc": "LX ofertas culturales · GR perfecto (se ha cancelado)",
   "lab": "Locutora", "voice": "SARA/RADIO",
   "text": "Y en la agenda de este fin de semana: el sábado, a las ocho de la tarde, el grupo Los Faroles presenta su nuevo disco en el teatro Romea. Las entradas cuestan quince euros y ya se pueden comprar en la taquilla. Atención: el concierto del domingo se ha cancelado.",
   "why": "El grupo presenta su nuevo disco. Las entradas cuestan quince euros y es a las ocho de la tarde."},
  {"n": 8, "conv": "Audio 2", "q": "En La Terraza del Puerto...", "o": ["hay música en directo un día a la semana.", "se puede comer el menú del día todos los días.", "no hace falta reservar."], "ok": 0,
   "cats": ["lugares", "yatodavia"], "es": "ES-04", "pc": "LX restaurantes (menú del día, música en directo) · todavía no",
   "lab": "Locutor", "voice": "JAVIER/RADIO",
   "text": "¿Todavía no conoces La Terraza del Puerto? Cocina mediterránea con vistas al mar y un ambiente muy agradable. De lunes a jueves, menú del día por doce euros. Y los viernes, música en directo durante la cena. Es necesario reservar: reserva tu mesa en nuestra página web.",
   "why": "Los viernes hay música en directo. El menú es de lunes a jueves, y es necesario reservar en la web."},
  {"n": 9, "conv": "Audio 3", "q": "Según el programa, a Cuenca...", "o": ["se puede ir en coche y aparcar en el centro.", "es buena idea ir en tren desde Madrid.", "la reportera va a ir este fin de semana."], "ok": 1,
   "cats": ["contraste", "ocio"], "es": "ES-07", "pc": "GR perfecto (ha estado este fin de semana) · LX viajes",
   "lab": "Locutora", "voice": "LYDIA/RADIO",
   "text": "En nuestro programa «Escapadas» hoy hablamos de Cuenca. Nuestra reportera ha estado allí este fin de semana y dice que lo mejor son las casas colgadas y el casco antiguo. Su consejo: ir en tren desde Madrid, porque aparcar en el centro es muy difícil.",
   "why": "La reportera aconseja ir en tren desde Madrid. Aparcar en el centro es muy difícil, y ya ha estado allí este fin de semana."},
  {"n": 10, "conv": "Audio 4", "q": "Las personas que se apuntan en septiembre...", "o": ["tienen el primer mes gratis.", "no pagan la inscripción.", "solo pueden usar la piscina."], "ok": 1,
   "cats": ["ocio"], "es": "ES-03", "pc": "LX actividades deportivas · apuntarse (matrícula = inscripción)",
   "lab": "Locutor", "voice": "EMILIO/RADIO",
   "text": "Gimnasio Activa abre un nuevo centro en el barrio de San José. Tenemos piscina, sala de musculación y más de cincuenta clases a la semana. Si te apuntas en septiembre, no pagas la matrícula y el primer mes te cuesta solo veinte euros. ¡Te esperamos!",
   "why": "En septiembre no se paga la matrícula, es decir, la inscripción. El primer mes cuesta veinte euros: no es gratis."},
  {"n": 11, "conv": "Audio 5", "q": "Según la noticia, el club de lectura...", "o": ["ha tenido mucho éxito.", "es para personas de todas las edades.", "se reúne los fines de semana."], "ok": 0,
   "cats": ["perfecto", "planes"], "es": "ES-03", "pc": "GR perfecto (ya se han apuntado) · pensar + infinitivo",
   "lab": "Locutora", "voice": "CRISTINA/RADIO",
   "text": "La biblioteca municipal ha organizado este mes un club de lectura para jóvenes de catorce a dieciocho años. Las reuniones son los miércoles por la tarde. Ya se han apuntado más de cuarenta chicos y chicas, así que el Ayuntamiento piensa abrir otro grupo en octubre.",
   "why": "Se han apuntado más de cuarenta jóvenes y van a abrir otro grupo: ha tenido mucho éxito. Es solo para jóvenes y se reúne los miércoles."},
  {"n": 12, "conv": "Audio 6", "q": "Según la encuesta, la actividad preferida es...", "o": ["salir con los amigos.", "hacer deporte.", "ver series y películas."], "ok": 2,
   "cats": ["ocio"], "es": "ES-08", "pc": "LX actividades de ocio · ordinales",
   "lab": "Locutor", "voice": "BOBBY/RADIO",
   "text": "Y ahora, los resultados de nuestra encuesta de esta semana: ¿qué hacen los oyentes en su tiempo libre? La actividad favorita es ver series y películas en casa. En segundo lugar está salir con los amigos; en tercer lugar, hacer deporte, y en cuarto lugar, leer.",
   "why": "Lo primero es ver series y películas en casa. Salir con amigos es la segunda y hacer deporte, la tercera."},
 ]}
for _x in [CA2["example"]] + CA2["items"]:
    _x["sound"] = RADIO_FX

CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Elena y Álex. Indique si los enunciados (del 13 al 18) se refieren a Elena (A), a Álex (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Fíjate en si algo ya ha pasado o es un plan, y en quién lo hace: si lo hace otra persona (una hermana, un amigo...), la respuesta es C.",
 "who": ["Elena", "Álex"], "voices": {"ELENA": "SUSANA", "ÁLEX": "MILO"},
 "lines": [
  ("ÁLEX", "¡Hola, Elena! ¿Qué tal el fin de semana? ¿Fuiste por fin a la boda de tu prima?"),
  ("ELENA", "¡Sí! Fue en un pueblo de Asturias, al lado del mar. ¡Qué sitio tan bonito! La ceremonia fue en la playa y luego cenamos en un restaurante con vistas. Lo pasé genial y bailé hasta las cuatro de la mañana."),
  ("ÁLEX", "¡Qué envidia! Yo me quedé en casa todo el fin de semana. Estuve enfermo, con fiebre, y no salí ni para comprar el pan."),
  ("ELENA", "Vaya, lo siento. ¿Y ya estás mejor?"),
  ("ÁLEX", "Sí, sí, hoy ya he ido a trabajar. Oye, ¿has visto ya la exposición de fotografía del museo? Mi hermana fue el jueves con sus amigas y dice que es buenísima."),
  ("ELENA", "Todavía no. Quiero ir, pero esta semana tengo muchísimo trabajo: estoy preparando una presentación. ¿Vamos juntos el sábado?"),
  ("ÁLEX", "El sábado no puedo, voy a correr la media maratón. ¡Llevo tres meses entrenando!"),
  ("ELENA", "¡Es verdad! ¡Qué valiente! Yo no he corrido una carrera en mi vida."),
  ("ÁLEX", "Pues tienes que probarlo. Bueno, ¿y el domingo?"),
  ("ELENA", "El domingo pienso descansar. Pero el viernes por la tarde podemos ir al museo, ¿no? Cierra a las nueve."),
  ("ÁLEX", "Vale. Y después podemos cenar en el restaurante griego de la plaza. ¿Lo conoces?"),
  ("ELENA", "Sí, he estado dos veces. A mí me pareció un poco caro, pero la comida está muy rica."),
  ("ÁLEX", "Perfecto. Pues el viernes a las siete en la puerta del museo.")],
 "items": [
  {"n": 13, "q": "Fue a una celebración familiar.", "ok": 0, "cats": ["contraste"], "es": "ES-03", "pc": "indefinido (fue, cenamos, lo pasé) · LX ocio",
   "why": "Elena fue a la boda de su prima en Asturias."},
  {"n": 14, "q": "Pasó el fin de semana en casa.", "ok": 1, "cats": ["contraste"], "es": "ES-08", "pc": "indefinido (me quedé, estuve)",
   "why": "Álex se quedó en casa todo el fin de semana porque estuvo enfermo."},
  {"n": 15, "q": "Ya ha visto la exposición de fotografía.", "ok": 2, "cats": ["yatodavia"], "es": "ES-08", "pc": "ya / todavía no",
   "why": "La exposición la ha visto la hermana de Álex. Elena todavía no ha ido y Álex tampoco: van el viernes."},
  {"n": 16, "q": "Va a participar en una carrera.", "ok": 1, "cats": ["planes", "ocio"], "es": "ES-03", "pc": "ir a + infinitivo · LX actividades deportivas",
   "why": "Álex va a correr la media maratón el sábado."},
  {"n": 17, "q": "Ha estado más de una vez en un restaurante.", "ok": 0, "cats": ["perfecto", "lugares"], "es": "ES-03", "pc": "experiencias (he estado dos veces) · valorar lugares",
   "why": "Elena ha estado dos veces en el restaurante griego. Álex lo propone, pero no dice cuántas veces ha ido."},
  {"n": 18, "q": "Piensa descansar el sábado.", "ok": 2, "cats": ["planes"], "es": "ES-07", "pc": "pensar + infinitivo · marcadores de futuro",
   "why": "Elena piensa descansar el domingo, no el sábado, y el sábado Álex corre la media maratón. Nadie descansa el sábado."}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

CH = "SONIDO 2: Two-tone ding-dong chime of a public address announcement system, clean and clear, no voices, no background noise"
BP = "SONIDO 1: Single short electronic answering machine beep, clean, no background noise"
CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. En cada mensaje pregúntate: ¿quién habla, dónde y para qué? ¿Avisa de un cambio, valora algo, propone un plan, recuerda una norma? Sobran tres.",
 "enun": [
  "Alguien cambia la hora de una cita.",
  "Una persona cuenta qué le ha parecido un espectáculo.",
  "Un espectáculo va a empezar más tarde.",
  "Se ofrece una visita guiada gratis.",
  "Alguien propone un plan para el fin de semana.",
  "Un lugar de ocio cierra antes de lo normal.",
  "Una persona todavía no ha recibido algo.",
  "Se anuncia el ganador de un concurso.",
  "Se recuerda una norma al público.",
  "Alguien da las gracias por una invitación.",
  "Ya no quedan entradas para un día."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "GABI/RADIO", "sound": BP,
   "text": "Hola, Raquel, soy Pedro. Oye, mañana no puedo quedar a las seis para ir al cine: salgo tarde del trabajo. ¿Quedamos a las ocho? Hay otra sesión a las ocho y media. Llámame, ¿vale?",
   "solucion": "La opción correcta es la letra a: alguien cambia la hora de una cita."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 2, "cats": ["ocio"], "es": "ES-10", "pc": "LX espectáculos (función) · ir a + infinitivo",
   "lab": "Megafonía", "voice": "MARTIN_2/RADIO", "sound": CH,
   "text": "Señoras y señores, buenas noches. Por un problema técnico, la función de esta noche va a empezar con veinte minutos de retraso, a las nueve y veinte. Pueden esperar en la cafetería del teatro. Disculpen las molestias.",
   "why": "La función va a empezar veinte minutos más tarde. No faltan entradas (K)."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 1, "cats": ["valorar", "perfecto"], "es": "ES-10", "pc": "GR perfecto + encantar y parecer para valorar",
   "lab": "Contestador", "voice": "ANA_MARIA/RADIO", "sound": BP,
   "text": "Hola, Inés, soy Carmen. ¡Ya he visto el musical que me recomendaste! Me ha encantado: la música me ha parecido preciosa y los actores, fenomenales. Muchas gracias por la recomendación. Te llamo esta noche y te cuento.",
   "why": "Carmen cuenta que el musical le ha encantado. Da las gracias, pero por una recomendación, no por una invitación (J sobra)."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 3, "cats": ["ocio"], "es": "ES-10", "pc": "LX lugares de interés (visita guiada, exposición)",
   "lab": "Megafonía", "voice": "SANTIAGO_LAT/RADIO", "sound": CH,
   "text": "Estimados visitantes: a las doce, desde la entrada principal, sale una visita guiada por la exposición de pintura moderna. La visita dura una hora y es gratuita para todas las personas con entrada al museo. Les esperamos.",
   "why": "En el museo hay una visita guiada gratuita para los visitantes."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 5, "cats": ["ocio"], "es": "ES-07", "pc": "LX lugares de ocio · horarios (antes de lo habitual)",
   "lab": "Megafonía", "voice": "DIEGO_PE/RADIO", "sound": CH,
   "text": "Atención, por favor: hoy, por la tormenta, la piscina municipal cierra a las seis de la tarde, tres horas antes de lo habitual. Mañana abrimos a las diez, como siempre. Gracias por su comprensión.",
   "why": "Hoy la piscina cierra tres horas antes de lo normal. Mañana abre a su hora."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 4, "cats": ["planes", "ocio"], "es": "ES-10", "pc": "pensar + infinitivo · FN proponer (¿Te apetece venir?)",
   "lab": "Contestador", "voice": "MARINA/RADIO", "sound": BP,
   "text": "Hola, Marcos, soy Lola. ¿Qué haces el sábado? Unos amigos y yo pensamos ir a hacer senderismo a la sierra y comer en un pueblo. ¿Te apetece venir? Salimos a las nueve. ¡Dime algo!",
   "why": "Lola propone a Marcos ir de senderismo el sábado."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 8, "cats": ["ocio"], "es": "ES-10", "pc": "no está permitido / no se puede · LX espectáculos deportivos",
   "lab": "Megafonía", "voice": "JUAN_CARLOS/RADIO", "sound": CH,
   "text": "Les recordamos que en el estadio no está permitido entrar con botellas de cristal ni con latas. Tampoco se puede fumar en las gradas. Gracias por su colaboración y disfruten del partido.",
   "why": "En el estadio recuerdan al público qué no está permitido."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 10, "cats": ["ocio", "yatodavia"], "es": "ES-10", "pc": "ya no quedan · todavía hay · LX entradas, taquilla",
   "lab": "Contestador", "voice": "DANIEL_ES/RADIO", "sound": BP,
   "text": "Hola, buenas tardes, le llamamos de la taquilla del Auditorio. Ayer nos preguntó por el concierto del día quince: lo sentimos, pero ya no quedan entradas. Para el día dieciséis todavía hay algunas. Si las quiere, llámenos antes del viernes, por favor. Muchas gracias y buenas tardes.",
   "why": "Para el día quince ya no hay entradas (para el dieciséis sí). Nadie espera un envío: la G sobra."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

REPARTO = """# REPARTO DE VOCES U06 (ninguna protagonista de la U05)
# T1 conversaciones (v3, ritmo natural): 0 amigos al teléfono = DAVID_M2 + ESTELA · 1 pareja en casa = MARTIN_3 + SARA_JOVEN (cambiadas tras escucharlas: CLARA sonaba enlatada)
#   2 oficina de turismo = LINA (Colombia) + JAVI_ROJAS · 3 compañeros de trabajo = DAVID_M1 + MIA
#   4 amigos y planes = CRISTINA_LAT + JUAN_CARLOS_2 (Latinoamérica) · 5 experiencias = RAFA + LUCIA · 6 polideportivo = RITA + DIEGO (Argentina)
# T2 radio (perfil /RADIO, con sintonía antes de cada audio): 0 parque acuático = MARTIN_1 · 1 agenda = SARA · 2 restaurante = JAVIER
#   3 programa de viajes = LYDIA (antes LUCIA_AR: enlatada) · 4 gimnasio = EMILIO · 5 noticia biblioteca = CRISTINA · 6 encuesta = BOBBY (antes HUGO: eco)
# T3 conversación entre amigos: ELENA = SUSANA · ÁLEX = MILO
# T4 mensajes (/RADIO): 0 contestador Pedro = GABI (Argentina) · 1 megafonía teatro = MARTIN_2 · 2 contestador Carmen = ANA_MARIA (México)
#   3 megafonía museo = SANTIAGO_LAT · 4 megafonía piscina = DIEGO_PE (Perú) · 5 contestador Lola = MARINA (Argentina)
#   6 megafonía estadio = JUAN_CARLOS · 7 contestador taquilla = DANIEL_ES (antes ALBEIRO: ruido y final cortado)
# Efectos: sintonía de radio (T2), din-don de megafonía y pitido de contestador (T4); siempre la misma descripción (caché)"""

# ---------------- ESCRITURA ----------------
ESCRITA = {"t1": {"instr": "Un amigo le escribe porque va a visitar su ciudad.",
  "input": ["¡Hola! ¿Qué tal? El fin de semana que viene voy a estar dos días en tu ciudad. ¡Por fin! ¿Qué me recomiendas? ¿Has estado en el museo nuevo? Dicen que es muy interesante. ¿Tienes tiempo para quedar?", "Un abrazo,<br>Iván"],
  "lead": "Conteste a su amigo. En el correo tiene que:",
  "pautas": ["saludar;", "decir si ha estado en el museo nuevo y qué le pareció;", "recomendarle dos lugares o actividades de su ciudad y explicar por qué;", "proponerle un plan para hacer juntos;", "despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Una página web de viajes busca textos sobre las cosas más interesantes de las ciudades. Escriba un texto sobre su ciudad. Hable de:",
   "pautas": ["cómo es su ciudad y qué se puede hacer allí;", "un lugar que ha visitado y qué le pareció;", "un restaurante, un bar o un café que recomienda y por qué (ambiente, comida, precios);", "algo que no le gusta de su ciudad;", "qué piensa hacer en su ciudad los próximos meses."]},
  "op2": {"title": "Opción 2", "intro": "El verano pasado usted fue a un festival de música con unos amigos. Aquí tiene tres fotos de ese fin de semana.",
   "photos": ["Por la mañana, usted y tres amigos llegan en coche a un camping al lado de un río. Hace mucho sol y montan las tiendas de campaña. Una amiga lleva un sombrero de paja.",
              "Por la tarde, empieza a llover mucho. Todos corren con chubasqueros de colores y las botas llenas de barro. Un chico se ríe.",
              "Por la noche, un concierto delante de un escenario grande con muchas luces. Usted y sus amigos bailan y cantan entre mucha gente."],
   "ficha": [], "intro2": "Escriba un texto sobre ese fin de semana. Hable de:",
   "pautas": ["dónde fue el festival, con quién fue y cómo llegaron;", "qué pasó por la tarde;", "cómo fue el concierto y qué le pareció el festival."],
   "img": "U06_escrita.jpg", "imgAlt": "Tres fotos del festival: la llegada al camping, la lluvia y el concierto"},
  "min": 70, "max": 80}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: mi tiempo libre", "pautas": ["qué hace normalmente en su tiempo libre y con quién;", "qué ha hecho este fin de semana o esta semana;", "una actividad que ha hecho alguna vez y le encantó;", "algo que nunca ha hecho y quiere probar;", "qué planes tiene para el próximo fin de semana."]},
  {"title": "Opción 2: una ciudad que he visitado", "pautas": ["qué ciudad es, cuándo fue y con quién;", "qué lugares visitó y qué le parecieron;", "qué comió y dónde;", "algo que no le gustó o un pequeño problema que tuvo;", "a qué ciudad piensa ir en su próximo viaje y por qué."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1", "desc": "Una bolera por la noche, en invierno. En el mostrador, un grupo de cinco amigos de unos veinte años, con abrigos y gorros, recoge los zapatos de bolos. Un chico con el pelo azul y un piercing tiene unos zapatos en la mano y le dice algo a la empleada, una mujer de unos cincuenta años con uniforme rojo. Detrás hay pistas con luces de colores, bolas y pantallas.", "img": "U06_oral_foto1.jpg"},
  {"title": "Fotografía 2", "desc": "Un puesto de alquiler de kayaks en una playa, una mañana de verano con mucho sol y viento. Una familia (padre, madre, un niño de unos seis años y una niña de unos diez) habla con un señor mayor con gorra, gafas de sol y la piel muy morena. El niño llora. Hay kayaks de colores en la arena, chalecos salvavidas, remos y una pizarra. Al fondo, mucha gente en la playa y barcos en el mar.", "img": "U06_oral_foto2.jpg"}],
  "pautas": ["las personas: cómo son, qué ropa llevan, qué están haciendo;", "el lugar: dónde están, qué tiempo hace, qué cosas hay y dónde están;", "qué cree que pasa o qué problema tienen las personas;", "qué cree que van a hacer después."]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1", "intro": "Usted quiere ir a la bolera con unos amigos el sábado por la noche. Llame por teléfono a la bolera y hable con el empleado (su profesora). Tiene que:", "pautas": ["saludar y decir qué quiere;", "preguntar por los horarios y el precio;", "reservar una pista para su grupo (cuántas personas, a qué hora);", "preguntar si hay algo más: comida, fiestas de cumpleaños, descuentos...", "dar las gracias y despedirse."]},
  {"title": "Si eligió la fotografía 2", "intro": "Usted está de vacaciones en la playa y quiere alquilar un kayak. Hable con el encargado del puesto (su profesora). Tiene que:", "pautas": ["saludar y decir qué quiere alquilar y para cuántas personas;", "preguntar el precio y cuánto tiempo puede tenerlo;", "preguntar qué incluye y si es necesario tener experiencia;", "resolver un pequeño problema y despedirse."]}]}}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (mi tiempo libre): ¿Ha hecho algo especial este mes? · ¿Ha probado alguna vez un deporte de riesgo?
    Opción 2 (una ciudad que he visitado): ¿Qué fue lo que más le gustó? · ¿Le gustaría volver? ¿Por qué?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (bolera): ¿Qué cree que le dice el chico a la empleada? · ¿Qué van a hacer después de jugar?
    Foto 2 (alquiler de kayaks): ¿Por qué cree que llora el niño? · ¿Qué cree que pregunta la familia?
  Tarea 3 — su papel (aquí sí conversa: pregunte, reaccione y provoque un pequeño problema):
    Foto 1 (empleado/a de la bolera, de usted): abre de 17:00 a 01:00, los sábados hasta las 02:00; una
    partida cuesta 6 euros por persona con los zapatos incluidos; máximo 6 personas por pista. Hay
    hamburguesas, pizzas y bebidas, y menús de cumpleaños. Pregunte «¿Para cuántas personas?», «¿A qué
    hora?» y «¿A nombre de quién?». Problema: a las diez ya no quedan pistas; ofrezca las ocho o las
    once y media. Descuento del 20 % de lunes a jueves, no el sábado.
    Foto 2 (encargado/a del puesto, de usted): kayak individual 15 euros la hora, doble 25 euros;
    la mañana entera (de 10 a 14) 50 euros. Incluye chalecos y remos; no hace falta experiencia, pero los
    niños menores de 8 años van siempre con un adulto. Pregunte «¿Ha montado alguna vez en kayak?» y
    «¿Sabe nadar?». Problema: ahora no quedan kayaks dobles hasta las doce; o hay viento y por la tarde
    se cierra el puesto.
  Al reaccionar, que use exclamativas (¡Qué bien!, ¡Qué pena!, ¡Qué caro!) y ya / todavía no si sale;
  que salude, agradezca y se despida.
  Qué mirar en esta unidad: perfecto para experiencias (he estado, nunca he hecho) e indefinido con
  tiempo terminado (el verano pasado fui); participios irregulares (visto, hecho, vuelto); valorar con
  me gustó / me pareció + adjetivo; planes con voy a / pienso / quiero; en la descripción, está/están +
  gerundio y creo que van a...; léxico de ocio y de lugares (ambiente, servicio, precio)."""
ERRORES = """  *He fui / *he ido ayer (ayer fui; hoy he ido); *el año pasado he visitado (visité);
  *he hacido, *he escribido, *he vido, *he volvido, *he rompido (hecho, escrito, visto, vuelto, roto);
  *¿Has ya visto...? (¿Ya has visto...?); *Ya no he visto la película (todavía no la he visto);
  *Me ha gustado los museos (me han gustado); *La película me pareció aburrido (aburrida);
  *Yo parecí la ciudad bonita (la ciudad me pareció bonita); *Pienso de ir (pienso ir);
  *Voy ir (voy a ir); *¡Qué bonita ciudad tan! (¡Qué ciudad tan bonita!);
  *lo pasé muy bueno (lo pasé muy bien)."""

# ---------------- IMÁGENES: FOTOS CON VARIEDAD REAL ----------------
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "bolera",
  "personas": "grupo (cinco amigos y una empleada)", "edades": "amigos de unos 20 años y una empleada de unos 50",
  "aspecto": "un chico con el pelo azul y un piercing en la nariz; una chica con trenzas y gafas grandes; otro chico alto en silla de ruedas; todos con abrigos, gorros y bufandas de invierno; la empleada con uniforme rojo, moño gris y gafas colgadas al cuello",
  "espacio": "interior", "lugar": "bolera de un centro comercial de ciudad", "momento": "noche",
  "estacion": "invierno", "tiempo": "frío y nieve fuera (se ve por la puerta de cristal)", "gente": "lleno",
  "accion": "en el mostrador, la empleada da los zapatos de bolos al grupo; el chico del pelo azul le enseña unos zapatos demasiado pequeños",
  "fondo": "pistas con luces de neón de colores, una familia celebra un cumpleaños con globos, pantallas con las puntuaciones",
  "objetos": "zapatos de bolos, bolas de colores, bolos, mostrador, pantallas, globos, abrigos, máquina de bebidas, pizzas en una mesa",
  "problema": "los zapatos que le dan al chico no son de su número y el grupo tiene que esperar porque todas las pistas están ocupadas"},
 "oral_foto2": {"situacion": "alquiler de kayaks en una playa",
  "personas": "familia de cuatro y un encargado", "edades": "padre y madre de unos 40, un niño de unos 6, una niña de unos 10 y un encargado de unos 65",
  "aspecto": "padre: barba, gorra y camiseta de fútbol; madre: pelo rizado, sombrero y vestido de playa; niña: gafas de bucear en la cabeza; niño: bañador de dibujos y crema blanca en la nariz; encargado: piel muy morena, pelo blanco, gorra, gafas de sol y camisa abierta",
  "espacio": "exterior", "lugar": "playa de un pueblo de costa", "momento": "mañana",
  "estacion": "verano", "tiempo": "mucho sol y viento (banderas que se mueven)", "gente": "lleno de gente",
  "accion": "la familia habla con el encargado del puesto para alquilar kayaks; el niño llora",
  "fondo": "gente tomando el sol con sombrillas, un chiringuito, barcos de vela en el mar, un socorrista en su silla",
  "objetos": "kayaks de colores, remos, chalecos salvavidas, pizarra con precios (sin texto legible), toallas, nevera, sombrillas, cubo y pala",
  "problema": "el niño llora porque no le dejan ir solo en un kayak; además solo queda un kayak doble"},
 "escrita": {"situacion": "festival de música al aire libre con camping",
  "personas": "grupo de cuatro amigos (el protagonista y tres amigos) y mucha gente en el concierto",
  "edades": "amigos de unos 30 años",
  "aspecto": "una amiga con sombrero de paja y pelo largo; un chico con barba y camiseta de un grupo; otra chica con el pelo corto rosa; chubasqueros de colores y botas de agua",
  "espacio": "exterior", "lugar": "camping al lado de un río y escenario de un festival en el campo", "momento": "de la mañana a la noche",
  "estacion": "verano", "tiempo": "sol por la mañana, tormenta por la tarde", "gente": "de poca gente (camping) a lleno (concierto)",
  "accion": "llegar en coche y montar las tiendas; correr bajo la lluvia; bailar en el concierto",
  "fondo": "un río y montañas; tiendas de campaña de colores; un escenario con luces y pantallas",
  "objetos": "coche, tiendas de campaña, nevera, sombrero, chubasqueros, botas con barro, escenario, luces, pulseras del festival",
  "problema": "una tormenta por la tarde: todo se llena de barro"},
}
SITUACIONES_USADAS = {
 "U01": ["secretaría", "librería"],
 "U02": ["taquilla de cine", "museo"],
 "U03": ["tienda de ropa", "aeropuerto"],
 "U04": ["tienda de muebles", "piso vacío en alquiler"],
 "U05": ["parada de autobús de noche", "taller de bicicletas en un pueblo"],
 "U06": ["bolera", "alquiler de kayaks en una playa"],
}

IMG_PROMPTS = {
 "portada": "Photorealistic, candid photo of a lively evening in a Spanish old town square in late spring: groups of people of all ages sit on a busy bar terrace with tapas and drinks, a street musician plays the guitar, a teenage couple takes a selfie, an elderly couple walks arm in arm, a cyclist passes, warm golden light from street lamps and shop windows, flower pots on balconies, no readable text, 16:9",
 "oral": "Photorealistic, candid photo in a small, warm language classroom in the evening: a teacher in her forties with dark curly hair and glasses and an adult female student in her thirties with a headscarf sit face to face and talk, the student gestures enthusiastically as if describing a trip, a tablet on the table shows holiday photos without readable text, a world map on the wall, a lamp and books, no readable text, 3:2",
 "escrita": "Photorealistic triptych, three separate photos side by side of equal size with thin white borders, the same group of four friends in their thirties at a summer outdoor music festival in Spain. Left: sunny morning at a campsite next to a river with mountains behind, the friends get out of a car and set up colourful tents, one woman wears a straw hat and has long hair, a bearded man in a band t-shirt, a woman with short pink hair. Centre: afternoon thunderstorm, the friends run laughing in colourful rain ponchos and rubber boots covered in mud. Right: at night in front of a big stage with bright coloured lights and a huge crowd, the friends dance and sing with festival wristbands. Candid, natural light, no readable text, 3:1",
 "oral_foto1": "Photorealistic, candid photo inside a busy bowling alley in a Spanish shopping centre on a winter night: at the counter, a group of five friends of about 20 in winter coats, hats and scarves collect bowling shoes; a young man with blue hair and a nose piercing holds up a pair of shoes that are too small and talks to the female employee, a woman of about 50 in a red uniform with a grey bun and glasses hanging from a cord; a young woman with braids and big glasses laughs, a tall young man in a wheelchair checks his phone; behind them, bowling lanes with colourful neon lights, coloured bowling balls, score screens without readable text, a family celebrating a birthday with balloons, pizzas on a table, a drinks machine; through the glass door, snow falling outside; vivid artificial light, no readable text, 3:2",
 "oral_foto2": "Photorealistic, candid photo on a crowded Spanish beach on a very sunny, windy summer morning: at a small kayak rental stand, a family talks to the stand keeper, a man of about 65 with very tanned skin, white hair, a cap, sunglasses and an open shirt; the father of about 40 with a beard, a cap and a football shirt, the mother with curly hair, a sun hat and a beach dress, a girl of about 10 with diving goggles on her head, and a boy of about 6 in cartoon swim shorts with white sun cream on his nose who is crying; colourful kayaks on the sand, paddles, life jackets, a small chalkboard without readable text, a cool box, towels, a bucket and spade; flags blowing in the wind; in the background, people under beach umbrellas, a beach bar, sailing boats on the sea and a lifeguard on his tall chair; bright warm light, no readable text, 3:2",
}
IMG_DESC = {"portada": "terraza de bar en una plaza al atardecer con gente de todas las edades", "oral": "clase: profesora con gafas y alumna con pañuelo hablando de un viaje", "escrita": "tres fotos del festival: camping, tormenta con barro, concierto de noche", "oral_foto1": "bolera de noche en invierno: grupo de amigos y empleada con zapatos", "oral_foto2": "alquiler de kayaks en la playa en verano: familia, niño llorando, encargado mayor"}
CA1_DESC = {0: "cine / teatro / concierto en la plaza", 1: "gimnasio / pagando un regalo / piscina", 2: "catedral / castillo / museo moderno", 3: "camarero serio / sushi / cuenta", 4: "playa / partido en el bar / chico estudiando", 5: "submarinismo / globo / paracaidas", 6: "padel / yoga / natacion"}

LECTURA = [CL1, CL2, CL3, CL4]
AUDITIVA = [CA1, CA2, CA3, CA4]
