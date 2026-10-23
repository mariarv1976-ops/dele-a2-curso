# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R14b: VOCABULARIO EN ESCENAS (2) · FUERA DE CASA (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R14b_vocabulario.py
#
# Segunda mitad de la R14 (la R14a es la casa y el dia a dia). MISMO ENFOQUE (aprobado por Maria, 22/10):
# LAS PALABRAS VIVEN EN ESCENAS, NO EN LISTAS: 1) la escena (red de cuatro ramas + tapa y recuerda), 2) el trio (las tres
# vinetas de la tarea 1 de la auditiva: dos se descartan), 3) la pareja de parafrasis (lectura y auditiva).
#   AREAS de frecuencia ALTA (Plan curricular, apartado 5): vi viajes, transporte y alojamiento (LX-14) · oc ocio, deporte y
#   espectaculos (LX-08, LX-18) · es estudios (LX-06) · tr trabajo (LX-07) · ti el tiempo y las estaciones (LX-20).
#   Y un RINCON corto de frecuencia MEDIA (Maria, 23/10: dos escenas y una sola conversacion): ri servicios (LX-11),
#   medios y movil (LX-09, LX-16) y fiestas (LX-19).
#   NIVEL: solo lexico LX del Plan curricular, nada de B1. Sin combinaciones de dos pronombres ni duplicacion del objeto.
#
# MARCAS (las mismas que la R14a)
#   En el texto de cada escena: [n:forma] o [n:forma=lema]   (n = rama 1-4 de la red)
#   En los audios: [v:...] la opcion buena · [x:...] las que se mencionan y se descartan
#   Huecos: [[correcta|distractor|distractor#motivo]]
# Espanol de Espana. Ejemplos propios: nada sale de los materiales de Maria ni de los manuales; no repite la R14a ni las
# tareas 1 de M1, M6 y M7 (el tiempo en la sierra, como va al aeropuerto, que deporte hace ahora, donde trabaja ahora...).

MES_WP = "2026/10"      # carpeta del mes en que se suben los audios y las vinetas a WordPress (si cambia, cambiar aqui)
MES_WP_T2 = "2026/10"   # carpeta de las fotos de la oral M4T2_fotoN.jpg (ya subidas)
SIGLA = "R14b"
RINCON = "ri"           # el area corta: una sola conversacion en «Escucha y elige»

# ------------------------------------------------------------------ AREAS
AREAS = {
    "vi": {"n": "Los viajes", "lx": "LX-14", "txt": "el transporte, la estación, el alojamiento y el turismo"},
    "oc": {"n": "El ocio", "lx": "LX-08, LX-18", "txt": "el deporte, las aficiones y los espectáculos"},
    "es": {"n": "Los estudios", "lx": "LX-06", "txt": "los cursos, las clases y los exámenes"},
    "tr": {"n": "El trabajo", "lx": "LX-07", "txt": "buscar trabajo, las profesiones y el día a día en la empresa"},
    "ti": {"n": "El tiempo", "lx": "LX-20", "txt": "el tiempo que hace, las estaciones y el paisaje"},
    "ri": {"n": "Servicios, móvil y fiestas", "lx": "LX-11, LX-09, LX-16, LX-19", "txt": "los recados, el móvil, los medios y las fiestas (frecuencia media)"},
}
ORDEN_AREAS = ["vi", "oc", "es", "tr", "ti", "ri"]

# ------------------------------------------------------------------ LAS ESCENAS
ESCENAS = [
 {"id": "vi1", "area": "vi", "titulo": "El viaje", "lugar": "Un fin de semana en Santander, en tren",
  "ramas": [("Los transportes", ["el tren", "el avión", "el autobús", "el metro", "el tranvía", "el barco", "el taxi", "a pie", "en bici"]),
            ("En la estación", ["la estación", "el aeropuerto", "el andén", "la vía", "la parada", "la taquilla", "la salida", "la llegada", "el retraso"]),
            ("El billete y el equipaje", ["el billete de ida", "el billete de ida y vuelta", "la maleta", "el equipaje de mano", "facturar", "la puerta de embarque", "la mochila"]),
            ("Lo que dices", ["¿De qué andén sale el tren?", "Un billete de ida y vuelta, por favor.", "El tren lleva retraso.", "¿Dónde está la parada del autobús?"])],
  "texto": "El viernes fui a Santander en [1:tren]. Compré el [3:billete de ida y vuelta] por internet y llevé solo una [3:mochila] y una [3:maleta] pequeña. "
           "En la [2:estación] miré el panel: el tren salía del [2:andén] cinco, pero llevaba veinte minutos de [2:retraso]. Mi hermana prefiere el [1:avión], "
           "pero en el [2:aeropuerto] siempre hay que [3:facturar] y esperar mucho. En Santander fui en [1:autobús] al centro: la [2:parada] estaba justo en la "
           "[2:salida] de la estación. El domingo volví en tren, muy cansada pero contenta."},
 {"id": "vi2", "area": "vi", "titulo": "El hostal y la ciudad", "lugar": "Dos noches en un hostal de Granada",
  "ramas": [("El alojamiento", ["el hotel", "el hostal", "el albergue", "el apartamento", "la habitación doble", "la habitación individual", "la recepción", "la llave", "la reserva"]),
            ("Hacer turismo", ["la visita guiada", "el monumento", "el museo", "el mapa", "el plano", "la excursión", "la oficina de turismo", "el casco antiguo"]),
            ("Lo que haces", ["reservar", "alojarse", "visitar", "perderse", "hacer fotos", "hacer la maleta"]),
            ("Lo que dices", ["Tengo una reserva a nombre de Ruiz.", "¿A qué hora es el desayuno?", "¿Me da un plano de la ciudad?", "¿Dónde empieza la visita guiada?"])],
  "texto": "En Granada nos [3:alojamos=alojarse] en un [1:hostal] pequeño del [2:casco antiguo]. Yo [3:reservé=reservar] una [1:habitación doble] por internet, "
           "pero en la [1:recepción] no encontraban la [1:reserva]. Al final nos dieron la [1:llave] de una habitación con balcón. Por la mañana fuimos a la "
           "[2:oficina de turismo] y nos dieron un [2:plano] de la ciudad. Hicimos una [2:visita guiada] por los [2:monumentos=el monumento] más famosos y "
           "[3:hicimos fotos=hacer fotos] de todo. Por la tarde nos [3:perdimos=perderse] por las calles estrechas, pero fue muy divertido. El domingo, una "
           "[2:excursión] a la sierra y, por la noche, a casa."},
 {"id": "oc1", "area": "oc", "titulo": "Un sábado activo", "lugar": "Los planes de mi grupo de amigos",
  "ramas": [("Los deportes", ["jugar al fútbol", "jugar al tenis", "jugar al pádel", "jugar al baloncesto", "nadar", "correr", "montar en bici", "hacer senderismo", "ir al gimnasio"]),
            ("Las cosas", ["la pista", "el campo de fútbol", "la piscina", "el partido", "el equipo", "la raqueta", "la pelota"]),
            ("Las aficiones", ["leer", "bailar", "cocinar", "hacer fotos", "tocar la guitarra", "tocar el piano", "pintar", "ver series"]),
            ("Con los amigos", ["quedar", "salir", "ir de tapas", "el fin de semana", "el plan", "apuntarse"])],
  "texto": "Los sábados mi grupo de amigos tiene muchos [4:planes=el plan]. Por la mañana, Carlos y yo [1:jugamos al pádel=jugar al pádel] en una [2:pista] del barrio; "
           "si llueve, [1:vamos al gimnasio=ir al gimnasio]. Mi amiga Rocío prefiere [1:hacer senderismo] o [1:montar en bici]. Por la tarde, unos ven el "
           "[2:partido] de su [2:equipo] en el bar y otros [3:tocan la guitarra=tocar la guitarra] en casa de Julia. Yo [3:hago fotos=hacer fotos] de todo para "
           "nuestro grupo del móvil. Por la noche siempre [4:quedamos=quedar] para [4:ir de tapas] por el centro. ¡Y el domingo, a descansar!"},
 {"id": "oc2", "area": "oc", "titulo": "Una noche de espectáculo", "lugar": "El estreno de una obra de teatro",
  "ramas": [("Los espectáculos", ["el cine", "el teatro", "el concierto", "la exposición", "el museo", "la obra de teatro", "la película"]),
            ("Las personas", ["el actor", "la actriz", "el director", "el cantante", "el grupo", "el público", "el pintor"]),
            ("Las entradas", ["la entrada", "la taquilla", "el estreno", "la fila", "el asiento", "agotado", "la sesión"]),
            ("Lo que dices", ["¿Quedan entradas para hoy?", "Dos entradas para la sesión de las ocho.", "¡Qué obra tan buena!", "¿A qué hora empieza?"])],
  "texto": "Ayer fue el [3:estreno] de una [1:obra de teatro] en mi ciudad. Las [3:entradas=la entrada] estaban casi [3:agotadas=agotado], pero mi novio compró "
           "dos en la [3:taquilla] por la mañana. Teníamos [3:asientos=el asiento] en la quinta [3:fila]. La [2:actriz] principal es muy famosa: también sale en "
           "una [1:película] que vimos en el [1:cine] el mes pasado. Al final, el [2:público] aplaudió muchísimo y el [2:director] subió al escenario. Después "
           "tomamos algo y hablamos de la obra. El sábado que viene vamos a un [1:concierto] de un [2:grupo] de rock."},
 {"id": "es1", "area": "es", "titulo": "Me apunto a un curso", "lugar": "Una academia de idiomas en septiembre",
  "ramas": [("Los centros", ["el colegio", "el instituto", "la universidad", "la academia", "la biblioteca", "la escuela"]),
            ("El curso", ["el curso", "la clase", "el nivel", "el horario", "la matrícula", "el profesor", "el alumno", "el compañero de clase"]),
            ("Lo que haces", ["matricularse", "apuntarse", "aprender", "estudiar", "hacer los deberes", "practicar"]),
            ("Lo que dices", ["¿Cuánto cuesta la matrícula?", "¿Qué nivel tengo?", "¿Hay clases por la tarde?", "No lo entiendo, ¿puede repetir?"])],
  "texto": "Este año me he [3:apuntado=apuntarse] a un [2:curso] de inglés en una [1:academia] cerca de mi trabajo. Primero hice una prueba para saber mi "
           "[2:nivel]. Después [3:me matriculé=matricularse]: la [2:matrícula] cuesta cincuenta euros. Las [2:clases=la clase] son los martes y los jueves por la "
           "tarde, un [2:horario] perfecto para mí. La [2:profesora=el profesor] es irlandesa y muy simpática, y mis [2:compañeros de clase=el compañero de clase] "
           "son de muchos países. Todas las semanas [3:hago los deberes=hacer los deberes] en la [1:biblioteca] del barrio. Mi hija [3:estudia=estudiar] en el "
           "[1:instituto] y a veces me ayuda."},
 {"id": "es2", "area": "es", "titulo": "Época de exámenes", "lugar": "Junio en la universidad",
  "ramas": [("Las asignaturas", ["la asignatura", "las matemáticas", "la historia", "la química", "el inglés", "la informática", "la geografía"]),
            ("Los exámenes", ["el examen", "la nota", "aprobar", "suspender", "repetir", "sacar buena nota"]),
            ("Para estudiar", ["los apuntes", "el libro", "el diccionario", "el ordenador", "el cuaderno", "la sala de estudio"]),
            ("Lo que dices", ["¿Qué nota has sacado?", "¡He aprobado todo!", "Mañana tengo un examen.", "¡Mucha suerte!"])],
  "texto": "En junio, en la universidad, todo son [2:exámenes=el examen]. Esta semana tengo tres: [1:historia], [1:inglés] y [1:matemáticas]. Paso las tardes "
           "en la [3:sala de estudio] con mis [3:apuntes=los apuntes] y mi [3:ordenador]. Mi compañera Lucía siempre lleva un [3:diccionario] enorme. El año "
           "pasado [2:suspendí=suspender] la [1:química] y tuve que [2:repetir] el examen en septiembre, pero al final [2:aprobé=aprobar] con buena [2:nota]. "
           "Este año quiero aprobar todas las [1:asignaturas=la asignatura] en junio para tener el verano libre."},
 {"id": "tr1", "area": "tr", "titulo": "Busco trabajo", "lugar": "Ofertas, currículum y una entrevista",
  "ramas": [("Buscar trabajo", ["buscar trabajo", "la oferta de trabajo", "el currículum", "la entrevista", "el anuncio", "la experiencia"]),
            ("Las condiciones", ["la jornada completa", "la media jornada", "el sueldo", "el horario", "el contrato", "las vacaciones"]),
            ("Las profesiones", ["el camarero", "el dependiente", "el recepcionista", "el cocinero", "el enfermero", "el mecánico", "el peluquero", "el abogado"]),
            ("Lo que dices", ["Llamo por la oferta de trabajo.", "Tengo experiencia de camarera.", "¿Cuál es el horario?", "¿Cuándo puedo empezar?"])],
  "texto": "Mi primo Álvaro [1:busca trabajo=buscar trabajo] desde hace dos meses. Todos los días mira las [1:ofertas de trabajo=la oferta de trabajo] en "
           "internet y manda su [1:currículum]. Tiene [1:experiencia] de [3:camarero] y de [3:dependiente] en una tienda de deportes. La semana pasada tuvo una "
           "[1:entrevista] en un hotel para trabajar de [3:recepcionista]. Le ofrecen un [2:contrato] de [2:media jornada], de lunes a viernes por la mañana. El "
           "[2:sueldo] no es muy alto, pero el [2:horario] es bueno y puede estudiar por las tardes. Mañana le van a decir si lo eligen."},
 {"id": "tr2", "area": "tr", "titulo": "Mi primer mes en la empresa", "lugar": "Una oficina en el centro",
  "ramas": [("El lugar", ["la oficina", "la empresa", "la fábrica", "la tienda", "la sala de reuniones", "el despacho"]),
            ("Las personas", ["el jefe", "la jefa", "el compañero de trabajo", "el cliente", "el equipo"]),
            ("El horario", ["la reunión", "el turno de mañana", "el turno de tarde", "el turno de noche", "trabajar desde casa", "las vacaciones"]),
            ("Lo que haces", ["empezar a trabajar", "llegar tarde", "atender a los clientes", "enviar un correo", "salir del trabajo"])],
  "texto": "Hace un mes [4:empecé a trabajar=empezar a trabajar] en una [1:empresa] de viajes. Mi [1:oficina] está en el centro y desde la ventana veo el mar. "
           "Mi [2:jefa] se llama Inés: es seria, pero muy amable. Los lunes tenemos una [3:reunión] en la [1:sala de reuniones] con todo el [2:equipo]. Esta "
           "semana tengo [3:turno de mañana]: entro a las ocho y salgo a las tres. Por la mañana [4:atiendo a los clientes=atender a los clientes] por teléfono y "
           "por la tarde [4:envío correos=enviar un correo]. Mis [2:compañeros de trabajo=el compañero de trabajo] son muy simpáticos. ¡Y en agosto tengo una "
           "semana de [3:vacaciones]!"},
 {"id": "ti1", "area": "ti", "titulo": "¿Qué tiempo hace?", "lugar": "La previsión para el fin de semana",
  "ramas": [("Hace...", ["hace sol", "hace calor", "hace frío", "hace viento", "hace buen tiempo", "hace mal tiempo"]),
            ("Llueve o nieva", ["llover", "nevar", "la lluvia", "la nieve", "la tormenta", "la niebla", "está nublado"]),
            ("Cuánto y cómo", ["los grados", "la temperatura", "el cielo", "la previsión", "despejado", "la nube"]),
            ("Lo que llevas", ["el paraguas", "el chubasquero", "la gorra", "las gafas de sol", "la crema solar", "el abrigo"])],
  "texto": "Esta mañana he mirado la [3:previsión] del tiempo para el fin de semana. El sábado por la mañana el [3:cielo] va a estar [3:despejado] y va a "
           "[1:hacer sol=hace sol]: unos veinticinco [3:grados=los grados]. Pero por la tarde [2:va a estar nublado=está nublado] y puede haber [2:tormenta]. El "
           "domingo va a [2:llover] en toda la costa y la [3:temperatura] va a bajar mucho. Por eso, en la mochila llevo las [4:gafas de sol] y la "
           "[4:crema solar], pero también un [4:paraguas] y un [4:chubasquero]. ¡En mi ciudad, en otoño, nunca se sabe!"},
 {"id": "ti2", "area": "ti", "titulo": "Las estaciones y el paisaje", "lugar": "Un año en el pueblo de mis abuelos",
  "ramas": [("Las estaciones", ["la primavera", "el verano", "el otoño", "el invierno"]),
            ("El paisaje", ["el mar", "la playa", "la montaña", "el río", "el lago", "el bosque", "el campo", "la isla"]),
            ("La naturaleza", ["el árbol", "la flor", "la hoja", "el animal", "el pájaro", "la planta"]),
            ("Cuidar el planeta", ["reciclar", "la contaminación", "la basura", "el contenedor", "ahorrar agua"])],
  "texto": "Mis abuelos viven en un pueblo entre la [2:montaña] y el [2:mar]. En [1:primavera] el [2:campo] se llena de [3:flores=la flor] y se oyen los "
           "[3:pájaros=el pájaro]. En [1:verano] vamos a la [2:playa] o nos bañamos en el [2:río]. En [1:otoño] caen las [3:hojas=la hoja] de los "
           "[3:árboles=el árbol] y hace mucho viento. Y en [1:invierno], a veces, nieva en el [2:bosque]. Mi abuelo siempre dice que antes llovía más. En el "
           "pueblo todos [4:reciclan=reciclar]: hay un [4:contenedor] para cada tipo de [4:basura]."},
 {"id": "ri1", "area": "ri", "titulo": "Recados de la mañana", "lugar": "Correos, el banco y el ayuntamiento",
  "ramas": [("Los sitios", ["correos", "el banco", "el cajero", "el ayuntamiento", "la comisaría", "el centro de salud", "la oficina"]),
            ("Los trámites", ["hacer un trámite", "pedir cita", "rellenar un formulario", "firmar", "el documento", "el horario de atención"]),
            ("Enviar y pagar", ["enviar un paquete", "la carta", "el sobre", "el sello", "sacar dinero", "la tarjeta"]),
            ("Lo que dices", ["Quería enviar este paquete.", "¿Dónde firmo?", "¿Qué documentos necesito?", "¿Cuál es el horario de atención?"])],
  "texto": "Ayer tuve una mañana de recados. Primero fui a [1:correos] a [3:enviar un paquete] a mi hermana, que vive en Lyon. Compré también "
           "[3:sellos=el sello] para dos [3:cartas=la carta]. Después [3:saqué dinero=sacar dinero] en el [1:cajero] del [1:banco]. Luego fui al "
           "[1:ayuntamiento]: tenía que [2:hacer un trámite] para apuntarme a la piscina municipal. Allí tuve que [2:rellenar un formulario] y [2:firmar] dos "
           "veces. El [2:horario de atención] es de nueve a dos, y llegué a la una y media: ¡justo a tiempo!"},
 {"id": "ri2", "area": "ri", "titulo": "El móvil y las fiestas", "lugar": "Las fiestas del barrio, en el grupo del móvil",
  "ramas": [("El móvil", ["el móvil", "la aplicación", "el mensaje", "la llamada", "la batería", "el cargador", "la contraseña", "el wifi", "la pantalla"]),
            ("Lo que haces", ["descargar", "conectarse", "cargar el móvil", "mandar un mensaje", "funcionar", "no funcionar"]),
            ("Los medios", ["las redes sociales", "la página web", "la noticia", "el anuncio", "el programa", "la radio", "el periódico", "la televisión"]),
            ("Las fiestas", ["las fiestas del barrio", "la Navidad", "la Nochevieja", "la Semana Santa", "los Reyes"])],
  "texto": "Esta semana son las [4:fiestas del barrio=las fiestas del barrio]. El [3:programa] está en la [3:página web] del ayuntamiento y también en las "
           "[3:redes sociales]. En el grupo de vecinos del [1:móvil] no paran los [1:mensajes=el mensaje]: fotos, horarios, [3:noticias=la noticia]... Mi vecino "
           "Paco ha [2:descargado=descargar] una [1:aplicación] con todos los conciertos. Ayer mi móvil no [2:funcionaba=funcionar] bien: la [1:batería] se "
           "terminaba enseguida. Por suerte, mi hija tenía un [1:cargador]. ¡Me gustan las fiestas del barrio casi tanto como la [4:Nochevieja]!"},
]

TRIOS = {
    "vi": [("Los transportes", ["el tren", "el avión", "el autobús"]), ("En la estación", ["el andén", "la parada", "la taquilla"]), ("El alojamiento", ["la habitación doble", "la habitación individual", "el apartamento"])],
    "oc": [("Los espectáculos", ["el cine", "el teatro", "el concierto"]), ("Los deportes", ["jugar al tenis", "nadar", "montar en bici"]), ("Las aficiones", ["tocar la guitarra", "pintar", "bailar"])],
    "es": [("Los centros", ["el colegio", "el instituto", "la universidad"]), ("Las asignaturas", ["las matemáticas", "la historia", "la química"]), ("Para estudiar", ["los apuntes", "el diccionario", "el ordenador"])],
    "tr": [("Las profesiones", ["el camarero", "el recepcionista", "el cocinero"]), ("El horario", ["el turno de mañana", "el turno de tarde", "el turno de noche"]), ("Las personas", ["el jefe", "el compañero de trabajo", "el cliente"])],
    "ti": [("Llueve o nieva", ["la lluvia", "la nieve", "la tormenta"]), ("Lo que llevas", ["el paraguas", "la gorra", "el abrigo"]), ("Las estaciones", ["la primavera", "el otoño", "el invierno"])],
    "ri": [("Los sitios", ["correos", "el banco", "el ayuntamiento"]), ("El móvil", ["la batería", "el cargador", "la pantalla"]), ("Los medios", ["la radio", "el periódico", "la televisión"])],
}

PAREJAS = {
    "vi": [("Billete de ida y vuelta.", "Para ir y para volver."), ("El tren lleva retraso.", "El tren llega más tarde."), ("Habitación doble.", "Una habitación para dos personas."),
           ("Desayuno incluido.", "No pagas aparte el desayuno."), ("Equipaje de mano.", "La maleta pequeña que llevas contigo en el avión.")],
    "oc": [("Entradas agotadas.", "Ya no quedan entradas."), ("La entrada es libre.", "No hay que pagar para entrar."), ("El estreno es el viernes.", "El viernes es el primer día."),
           ("Se suspende el partido.", "Hoy no hay partido."), ("Me he apuntado a pádel.", "Voy a ir a clases de pádel.")],
    "es": [("He aprobado.", "El examen me ha salido bien."), ("He suspendido.", "No he aprobado."), ("La matrícula es gratuita.", "No pagas por apuntarte."),
           ("Nivel inicial.", "Para personas que empiezan."), ("Plazas limitadas.", "Hay pocas plazas.")],
    "tr": [("Media jornada.", "Cuatro horas al día."), ("Jornada completa.", "Ocho horas al día."), ("Con experiencia.", "Ya has trabajado antes en eso."),
           ("Trabajo los fines de semana.", "Trabajo los sábados y los domingos."), ("Mi jefa está de vacaciones.", "Mi jefa no trabaja estos días.")],
    "ti": [("Está nublado.", "Hay muchas nubes."), ("Cielo despejado.", "No hay nubes."), ("Las temperaturas bajan.", "Va a hacer más frío."),
           ("Hace un tiempo estupendo.", "Hace muy buen tiempo."), ("Lluvias por la tarde.", "Por la tarde va a llover.")],
    "ri": [("Horario de atención: de nueve a dos.", "Puedes ir por la mañana."), ("Me he quedado sin batería.", "El móvil se ha apagado."), ("Sin cita previa.", "No tienes que pedir cita."),
           ("Descarga la aplicación.", "Instala la aplicación en el móvil."), ("Rellene el formulario.", "Escriba sus datos en el papel.")],
}

# ------------------------------------------------------------------ ESCUCHA Y ELIGE
DESCARTE = [
    ("No, ... no.", "Dice que no claramente.", "—¿Vamos en autobús? —En autobús no, son ocho horas."),
    ("Antes..., pero ahora...", "Lo de antes ya no vale: la respuesta es lo de ahora.", "Antes nadaba todas las mañanas; ahora pinta."),
    ("Ya tengo... / ya está...", "Eso ya está hecho o ya lo tiene.", "Ya tengo el billete de ida y vuelta."),
    ("Está cerrado / lo han cancelado / no quedan", "Esa opción no es posible.", "Los lunes el museo está cerrado."),
    ("Eso es de... (otra persona)", "La palabra es de otra persona.", "A bailar va mi abuela, no él."),
    ("Al final... / Pues entonces...", "La decisión final: casi siempre es la respuesta.", "Al final voy en tren."),
]
# 12 conversaciones (50-80 palabras): tres de viajes, dos de cada area ALTA y una del rincon.
# VOCES (Maria, 23/10 noche): sin la R14a quedaban libres casi solo voces latinoamericanas (la unica peninsular libre era
# EFRAYN). Para compensar, cada conversacion lleva UNA voz peninsular que ya salio en la R14a y UNA voz latinoamericana
# libre. Ninguna del M1 (el ultimo modelo) ni de las descartadas (VOCES_EVITAR).
CA1 = [
 {"area": "vi", "q": "¿Cómo va a ir Marta a la boda de su prima?", "o": ["en avión", "en tren", "en autobús"], "ok": 1,
  "pres": "Va a escuchar a dos amigas que hablan de un viaje.",
  "lines": [("Mujer 1", "ANA_MARIA", "[curious] Oye, Marta, ¿cómo vas a ir a la boda de tu prima en Sevilla? ¿En [x:avión]?"),
            ("Mujer 2", "SUSANA", "[sighs] Pensaba ir en avión, pero esta semana los billetes están carísimos."),
            ("Mujer 1", "ANA_MARIA", "[helpful] ¿Y en [x:autobús]? Es muy barato."),
            ("Mujer 2", "SUSANA", "[unconvinced] Sí, pero son ocho horas... No, no. Al final voy en [v:tren]: tarda cinco horas y puedo leer tranquila. Ya tengo el billete de ida y vuelta.")],
  "why": "Va en <b>tren</b>. El avión es muy caro esta semana, y en autobús el viaje es demasiado largo.",
  "img": "R14b_CA1_01_avion_tren_autobus",
  "prompt": "Panel 1: a passenger plane taking off. Panel 2: a modern passenger train at a platform. Panel 3: a long-distance coach on a road."},
 {"area": "vi", "q": "¿Qué les dan en el hotel?", "o": ["un apartamento", "dos habitaciones individuales", "una habitación doble"], "ok": 2,
  "pres": "Va a escuchar a un cliente que habla con una recepcionista en un hotel.",
  "lines": [("Hombre", "MARTIN_3", "[tired] Buenas noches. Tenemos una reserva a nombre de Ramos: un [x:apartamento] para dos personas."),
            ("Mujer", "NINOSKA", "[apologetic] Lo siento mucho, señor Ramos. Hoy el apartamento no está libre: hay un problema con el agua."),
            ("Hombre", "MARTIN_3", "[worried] ¡Vaya! ¿Y qué podemos hacer? ¿Tiene dos [x:habitaciones individuales]?"),
            ("Mujer", "NINOSKA", "[helpful] Individuales no me quedan. Pero tengo una [v:habitación doble] muy grande, con balcón, por el mismo precio."),
            ("Hombre", "MARTIN_3", "[relieved] Perfecto, muchas gracias.")],
  "why": "Les dan una <b>habitación doble</b>. El apartamento tiene un problema con el agua y no quedan habitaciones individuales.",
  "img": "R14b_CA1_02_apartamento_individuales_doble",
  "prompt": "Panel 1: a small holiday apartment with a sofa and a kitchenette. Panel 2: two small single rooms side by side, each with one single bed. Panel 3: a hotel room with one double bed and a balcony."},
 {"area": "vi", "q": "¿Qué van a visitar mañana por la mañana?", "o": ["el castillo", "el museo", "el mercado"], "ok": 0,
  "pres": "Va a escuchar a una pareja que está de vacaciones.",
  "lines": [("Mujer", "ESTELA", "[excited] Mañana por la mañana podemos ir al [x:museo], ¿no? Dicen que es precioso."),
            ("Hombre", "DIEGO_PE", "[doubtful] Los lunes el museo está cerrado. Lo pone aquí, en el plano."),
            ("Mujer", "ESTELA", "[thinking] Ah, es verdad. ¿Y el [x:mercado]? Me apetece comprar algo para tu madre."),
            ("Hombre", "DIEGO_PE", "[calm] El mercado, mejor por la tarde, que abre a las cinco. Por la mañana vamos al [v:castillo]: hay una visita guiada a las diez."),
            ("Mujer", "ESTELA", "[cheerful] ¡Vale, pues al castillo!")],
  "why": "Por la mañana van al <b>castillo</b>. El museo está cerrado los lunes, y al mercado van por la tarde.",
  "img": "R14b_CA1_03_castillo_museo_mercado",
  "prompt": "Panel 1: an old stone castle on a small hill. Panel 2: the front of a classical museum building with columns. Panel 3: an outdoor street market with stalls and awnings."},
 {"area": "oc", "q": "¿Adónde van esta noche?", "o": ["a un concierto", "al cine", "al teatro"], "ok": 2,
  "pres": "Va a escuchar a dos amigos que hacen planes para la noche.",
  "lines": [("Hombre", "AGUSTIN", "[cheerful] ¿Qué hacemos esta noche? ¿Vamos al [x:cine]? Hay una película nueva de miedo."),
            ("Mujer", "RAQUEL", "[laughs] ¡Uf, de miedo no, por favor! Además, fuimos al cine el sábado."),
            ("Hombre", "AGUSTIN", "[curious] ¿Y el [x:concierto] de la plaza?"),
            ("Mujer", "RAQUEL", "[disappointed] Lo han cancelado por la lluvia. Mira, mi hermana tiene dos entradas para el [v:teatro] y no puede ir. ¿Te apetece?"),
            ("Hombre", "AGUSTIN", "[pleased] ¡Claro que sí! Me encanta el teatro.")],
  "why": "Van al <b>teatro</b>, con las entradas de la hermana. Al cine fueron el sábado y el concierto se ha cancelado.",
  "img": "R14b_CA1_04_concierto_cine_teatro",
  "prompt": "Panel 1: a band playing on an outdoor stage in a town square. Panel 2: a cinema screen seen from the seats. Panel 3: a theatre stage with red curtains and two actors."},
 {"area": "oc", "q": "¿Qué hace ahora los martes el abuelo de Lucía?", "o": ["nadar", "pintar", "bailar"], "ok": 1,
  "pres": "Va a escuchar a dos amigas que hablan del abuelo de una de ellas.",
  "lines": [("Mujer 1", "GABI", "[curious] Lucía, ¿tu abuelo sigue yendo a la piscina? Antes [x:nadaba] todas las mañanas."),
            ("Mujer 2", "CAROLINA", "[laughs] No, ya no nada: dice que el agua está muy fría. Ahora los martes [v:pinta] en el centro de mayores. ¡Pinta cuadros del pueblo!"),
            ("Mujer 1", "GABI", "[surprised] ¡Qué bien! ¿Y no iba a clases de [x:baile] con tu abuela?"),
            ("Mujer 2", "CAROLINA", "[amused] A bailar va mi abuela sola, los jueves. Él dice que no tiene paciencia.")],
  "why": "Ahora los martes <b>pinta</b>. Nadar lo hacía antes, y a bailar va su abuela.",
  "img": "R14b_CA1_05_nadar_pintar_bailar",
  "prompt": "Panel 1: an old man swimming in a swimming pool. Panel 2: an old man painting a landscape on a canvas. Panel 3: an old couple dancing."},
 {"area": "es", "q": "¿Qué asignatura ha suspendido Pablo?", "o": ["matemáticas", "inglés", "historia"], "ok": 2,
  "pres": "Va a escuchar a una madre que habla con su hijo de las notas.",
  "lines": [("Mujer", "MIA", "[curious] Pablo, ¿ya tienes las notas? ¿Qué tal las [x:matemáticas]? Estaba preocupada."),
            ("Hombre", "MARIO_LAT", "[proud] ¡Aprobadas, mamá! Un siete. Este año el profesor explica muy bien."),
            ("Mujer", "MIA", "[relieved] ¡Muy bien! ¿Y el [x:inglés]?"),
            ("Hombre", "MARIO_LAT", "[cheerful] Inglés, un nueve: la profe dice que hablo muy bien."),
            ("Mujer", "MIA", "[suspicious] Entonces... ¿has aprobado todo?"),
            ("Hombre", "MARIO_LAT", "[embarrassed] Todo no... He suspendido [v:historia]. Pero en septiembre la apruebo, de verdad.")],
  "why": "Ha suspendido <b>historia</b>. Matemáticas e inglés los ha aprobado.",
  "img": "R14b_CA1_06_matematicas_ingles_historia",
  "prompt": "Panel 1: a school notebook with simple sums and a ruler. Panel 2: an English dictionary and a small British flag. Panel 3: a history book with a picture of an old castle and a timeline."},
 {"area": "es", "q": "¿Dónde estudia ahora Irene por las tardes?", "o": ["en una cafetería", "en la biblioteca", "en casa"], "ok": 0,
  "pres": "Va a escuchar a dos compañeros de clase.",
  "lines": [("Hombre", "JUAN_RESTREPO", "[curious] Irene, ¿estudias por las tardes en la [x:biblioteca]? Nunca te veo."),
            ("Mujer", "SARA", "[tired] Antes sí, pero ahora está en obras y hay mucho ruido."),
            ("Hombre", "JUAN_RESTREPO", "[thoughtful] ¿Y en [x:casa]?"),
            ("Mujer", "SARA", "[sighs] En casa, imposible: mis hermanos ven la tele todo el día. Ahora voy a una [v:cafetería] tranquila al lado de la universidad. Tienen wifi y el café es barato.")],
  "why": "Ahora estudia en una <b>cafetería</b>. En la biblioteca estudiaba antes, y en casa hay mucho ruido.",
  "img": "R14b_CA1_07_cafeteria_biblioteca_casa",
  "prompt": "Panel 1: a young woman studying with a laptop and a coffee in a quiet café. Panel 2: a young woman studying at a long table in a library with bookshelves. Panel 3: a young woman studying at a desk in her bedroom."},
 {"area": "tr", "q": "¿Qué ropa lleva Andrés en su trabajo nuevo?", "o": ["un traje", "un uniforme", "ropa de deporte"], "ok": 1,
  "pres": "Va a escuchar a dos amigos que hablan de un trabajo nuevo.",
  "lines": [("Mujer", "LUISA", "[curious] ¡Andrés! ¿Qué tal en el hotel? ¿Tienes que ir con [x:traje] a la recepción?"),
            ("Hombre", "EMILIO", "[relaxed] No, traje no. El hotel nos da un [v:uniforme]: pantalón negro y camisa azul, con mi nombre."),
            ("Mujer", "LUISA", "[amused] ¡Qué elegante! ¿Y los fines de semana también?"),
            ("Hombre", "EMILIO", "[cheerful] Sí, siempre. En el hotel solo los monitores del gimnasio llevan [x:ropa de deporte]. Yo, uniforme todos los días.")],
  "why": "Lleva un <b>uniforme</b> que le da el hotel. Traje no, y la ropa de deporte es de los monitores del gimnasio.",
  "img": "R14b_CA1_08_traje_uniforme_deporte",
  "prompt": "Panel 1: a man in a dark suit and tie. Panel 2: a hotel receptionist in a uniform with black trousers, a blue shirt and a name badge. Panel 3: a man in a tracksuit and trainers."},
 {"area": "tr", "q": "¿Qué turno tiene Carlos este mes?", "o": ["el turno de mañana", "el turno de tarde", "el turno de noche"], "ok": 0,
  "pres": "Va a escuchar a dos compañeros de trabajo en un hospital.",
  "lines": [("Hombre 1", "MILO", "[hurried] Carlos, ¿este mes también tienes [x:turno de noche]? Necesito cambiar un día con alguien."),
            ("Hombre 2", "TOMAS", "[relieved] ¡No, por fin! El mes pasado tuve noches, pero este mes estoy [v:de mañana]: de siete a tres."),
            ("Hombre 1", "MILO", "[hopeful] ¿Y no puedes hacer una tarde el jueves? Tengo que ir al médico."),
            ("Hombre 2", "TOMAS", "[apologetic] Lo siento, el [x:turno de tarde] es imposible para mí: recojo a mis hijos del colegio. Pregúntale a Elena.")],
  "why": "Este mes tiene el <b>turno de mañana</b>. Las noches las hizo el mes pasado, y la tarde no puede.",
  "img": "R14b_CA1_09_manana_tarde_noche",
  "prompt": "Panel 1: a nurse arriving at a hospital at sunrise. Panel 2: a nurse at a hospital entrance in the afternoon sun. Panel 3: a nurse at a hospital entrance at night with the moon in the sky."},
 {"area": "ti", "q": "¿Qué se lleva Nuria a la excursión?", "o": ["el paraguas", "la gorra", "el abrigo"], "ok": 1,
  "pres": "Va a escuchar a un padre y a su hija antes de una excursión.",
  "lines": [("Hombre", "GABRIEL_ES", "[caring] Nuria, ¿llevas el [x:paraguas]? La previsión dice que va a llover."),
            ("Mujer", "ANA_MARIA", "[laughs] Papá, mira el móvil: han cambiado la previsión. Hoy no llueve: va a hacer sol y veinticinco grados."),
            ("Hombre", "GABRIEL_ES", "[insistent] Entonces, por lo menos, el [x:abrigo]... En la montaña hace frío."),
            ("Mujer", "ANA_MARIA", "[patient] ¿Con veinticinco grados? No, papá. Me llevo la [v:gorra] y la crema solar, y ya está.")],
  "why": "Se lleva la <b>gorra</b>. La previsión ha cambiado: no llueve y hace calor, por eso no necesita ni el paraguas ni el abrigo.",
  "img": "R14b_CA1_10_paraguas_gorra_abrigo",
  "prompt": "Panel 1: a closed umbrella. Panel 2: a baseball cap. Panel 3: a warm winter coat on a hanger."},
 {"area": "ti", "q": "¿Qué tiempo hizo casi todos los días en las vacaciones de Javier?", "o": ["llovió", "hizo calor", "nevó"], "ok": 0,
  "pres": "Va a escuchar a dos compañeros de trabajo que hablan de unas vacaciones.",
  "lines": [("Mujer", "NINOSKA", "[curious] ¡Javier! ¿Qué tal por Asturias? ¿Mucho [x:calor]?"),
            ("Hombre", "JAVIER", "[laughs] ¿Calor? ¡Qué va! Hizo sol el primer día, pero solo por la mañana."),
            ("Mujer", "NINOSKA", "[surprised] ¿Y luego? No me digas que [x:nevó]..."),
            ("Hombre", "JAVIER", "[amused] No, mujer, en agosto no nieva. Pero [v:llovió] todos los días, de la mañana a la noche. Veíamos la playa desde la ventana del apartamento.")],
  "why": "Casi todos los días <b>llovió</b>. Sol solo hizo una mañana, y en agosto no nieva.",
  "img": "R14b_CA1_11_lluvia_calor_nieve",
  "prompt": "Panel 1: a beach on a rainy day with dark clouds and rain. Panel 2: a beach on a very hot sunny day with a big sun. Panel 3: a snowy landscape with snow falling."},
 {"area": "ri", "q": "¿Qué le pasa al móvil de Laura?", "o": ["no tiene batería", "no se conecta al wifi", "tiene la pantalla rota"], "ok": 2,
  "pres": "Va a escuchar a una chica que habla con un dependiente en una tienda de móviles.",
  "lines": [("Mujer", "GABI", "[frustrated] Hola, buenas. Mi móvil no funciona bien. ¿Puede ser la [x:batería]?"),
            ("Hombre", "DAVID_M1", "[calm] A ver... No, la batería está bien: está al ochenta por ciento."),
            ("Mujer", "GABI", "[worried] ¿Entonces? En casa no puedo conectarme al [x:wifi]."),
            ("Hombre", "DAVID_M1", "[helpful] El wifi funciona: mire, aquí se conecta sin problema. El problema es la [v:pantalla]: está rota por dentro y por eso no responde. ¿Se ha caído al suelo?"),
            ("Mujer", "GABI", "[embarrassed] Sí... ayer, en la calle.")],
  "why": "Tiene la <b>pantalla rota</b>. La batería está bien y el wifi funciona.",
  "img": "R14b_CA1_12_bateria_wifi_pantalla",
  "prompt": "Panel 1: a mobile phone with an empty battery icon. Panel 2: a mobile phone with a crossed-out wifi icon. Panel 3: a mobile phone with a cracked screen."},
]
# Voces del ultimo modelo (M1) y descartadas por Maria (22/10): no se usan aqui.
VOCES_EVITAR = ["DANIEL_ES", "FIONA", "MARIO", "LYDIA", "SARA_JOVEN", "VOLU", "AITANA", "DANI", "MARINA_ES", "LUIS_VEGA", "SARA_2",
                "SANTIAGO_ES", "TATIANA", "OSCAR", "SERGIO", "BOBBY", "TAMARA", "JAVI_ROJAS", "ENRIQUE", "LINA", "ZABRA", "EVA", "RAFA",
                "DIANA", "DAVID_M2", "RITA", "ALEJANDRO", "DIEGO", "MARINA", "GABRIEL_CO", "JANET", "HUGO", "CLARA", "LUCIA_AR"]
# Voces de la R14a: solo las peninsulares se repiten (una por conversacion), las demas no.
VOCES_R14A = ["ANTONIO", "CAROLINA", "CRISTINA", "CRISTINA_LAT", "DAVID_M1", "EMILIO", "ERIK", "ESTELA", "GABRIEL_ES", "JAVIER", "LUCIA",
              "MARTIN_1", "MARTIN_2", "MARTIN_3", "MAYA", "MIA", "MILO", "RAQUEL", "SARA", "SOFIA", "SUSANA", "VALENTINA"]

# ------------------------------------------------------------------ DILO DE OTRA FORMA (tarea 2 de la lectura)
ANUNCIOS = [
 {"area": "vi", "titulo": "ALBERGUE LAS DUNAS · A 200 METROS DE LA PLAYA",
  "texto": "Habitaciones de cuatro y seis camas y dos habitaciones dobles con baño. El desayuno está incluido en el precio y hay una cocina para los clientes. Las toallas no están incluidas: se alquilan en la recepción por dos euros. Recepción abierta de 8:00 a 23:00.",
  "q": "En el albergue...", "o": ["no pagas aparte el desayuno.", "las toallas están incluidas.", "la recepción abre toda la noche."], "lit": 1,
  "why": "Incluido en el precio = no lo pagas aparte. Las toallas NO están incluidas, y la recepción cierra a las once de la noche."},
 {"area": "vi", "titulo": "TREN TURÍSTICO DEL VALLE",
  "texto": "Sale los sábados y los domingos a las 10:30 desde la estación de Riosol. El viaje dura una hora y media. Los niños menores de cuatro años no pagan billete. En invierno no hay tren los domingos. Compra tu billete en la taquilla o en nuestra página web.",
  "q": "El tren turístico...", "o": ["en invierno sale un solo día a la semana.", "sale todos los domingos del año.", "es gratis para todos los niños."], "lit": 1,
  "why": "En invierno no hay tren los domingos: solo sale el sábado. Gratis es solo para los niños menores de cuatro años."},
 {"area": "oc", "titulo": "CLUB DE SENDERISMO PASO LARGO",
  "texto": "Cada domingo organizamos una ruta por la montaña. Las rutas son fáciles: no hace falta experiencia. Hay que llevar botas, agua y comida. Si llueve, la ruta se cambia a otro día. Apúntate antes del jueves en nuestra página web.",
  "q": "En este club...", "o": ["pueden ir personas que nunca han hecho senderismo.", "la comida está incluida.", "si llueve, la ruta es más fácil."], "lit": 2,
  "why": "No hace falta experiencia = pueden ir personas que nunca lo han hecho. La comida la llevas tú, y si llueve la ruta se hace otro día."},
 {"area": "oc", "titulo": "TEATRO PRINCIPAL · LOS MIÉRCOLES, AL TEATRO",
  "texto": "Todos los miércoles, entradas a mitad de precio para todas las obras. Estas entradas se compran en la taquilla, solo el mismo día: no se pueden comprar por internet. Para el estreno de cada mes no hay descuento.",
  "q": "Los miércoles...", "o": ["las entradas son más baratas.", "las entradas se compran por internet.", "hay un estreno cada semana."], "lit": 1,
  "why": "A mitad de precio = más baratas. Por internet NO se pueden comprar, y el estreno es una vez al mes."},
 {"area": "es", "titulo": "ACADEMIA DE IDIOMAS PUERTO",
  "texto": "Cursos de inglés, francés y alemán para adultos. En septiembre, la matrícula es gratuita. Grupos de ocho alumnos como máximo. Clases de lunes a jueves, por la mañana o por la tarde. Antes de empezar, hacemos una prueba de nivel.",
  "q": "En esta academia...", "o": ["en septiembre no pagas por apuntarte.", "hay clases los viernes.", "las clases son gratuitas en septiembre."], "lit": 2,
  "why": "La matrícula gratuita = no pagas por apuntarte. Las clases sí se pagan, y no hay clases los viernes."},
 {"area": "es", "titulo": "BIBLIOTECA MUNICIPAL · ÉPOCA DE EXÁMENES",
  "texto": "Del 1 de mayo al 30 de junio, la sala de estudio abre también los fines de semana, de 9:00 a 21:00. Está prohibido comer en la sala, pero hay una zona para tomar café. Para usar los ordenadores hay que reservar.",
  "q": "En mayo y junio, la biblioteca...", "o": ["abre los sábados y los domingos.", "deja comer en la sala de estudio.", "tiene ordenadores sin reserva."], "lit": 1,
  "why": "Los fines de semana = los sábados y los domingos. En la sala no se puede comer, y los ordenadores se reservan."},
 {"area": "tr", "titulo": "SE BUSCA CAMARERO O CAMARERA",
  "texto": "Cafetería del centro busca camarero o camarera de media jornada, de 16:00 a 20:00, de martes a sábado. No hace falta experiencia: te enseñamos nosotros. Es necesario hablar inglés. Envía tu currículum a cafeteriaplaza@correo.es.",
  "q": "En este trabajo...", "o": ["trabajas cuatro horas al día.", "necesitas experiencia de camarero.", "trabajas de lunes a viernes."], "lit": 1,
  "why": "De cuatro a ocho = cuatro horas al día (media jornada). No hace falta experiencia, y se trabaja de martes a sábado."},
 {"area": "tr", "titulo": "HOTEL MIRAMAR · RECEPCIONISTA DE FIN DE SEMANA",
  "texto": "Buscamos recepcionista para los sábados y los domingos, de 8:00 a 15:00. Contrato de seis meses. Es necesario hablar español e inglés; el francés no es obligatorio. La comida del mediodía es gratis en el hotel.",
  "q": "La persona que buscan...", "o": ["no trabaja de lunes a viernes.", "tiene que hablar francés.", "trabaja seis meses sin contrato."], "lit": 1,
  "why": "Solo sábados y domingos = no trabaja de lunes a viernes. El francés no es obligatorio, y tiene contrato de seis meses."},
 {"area": "ti", "titulo": "EL TIEMPO PARA EL FIN DE SEMANA",
  "texto": "El sábado, cielo despejado en toda la región y temperaturas de hasta 26 grados. El domingo llegan las nubes por el norte y por la tarde habrá tormentas en la montaña. En la costa no va a llover.",
  "q": "El domingo...", "o": ["puede llover en la montaña.", "va a hacer sol en toda la región.", "va a llover en la costa."], "lit": 2,
  "why": "Tormentas en la montaña = puede llover allí. El sol en toda la región es el sábado, y en la costa no llueve."},
 {"area": "ri", "titulo": "FIESTAS DEL BARRIO DE SAN ROQUE",
  "texto": "Del 14 al 17 de agosto. Todas las mañanas, actividades para niños en el parque. El viernes, concierto gratuito en la plaza a las 22:00. El sábado, comida popular: compra tu ticket en la asociación de vecinos. Programa completo en la página web del ayuntamiento.",
  "q": "En las fiestas...", "o": ["no hay que pagar para ir al concierto.", "los niños tienen actividades solo el viernes.", "el programa completo está en la plaza."], "lit": 2,
  "why": "Concierto gratuito = no hay que pagar. Los niños tienen actividades todas las mañanas, y el programa está en la web."},
]

# ------------------------------------------------------------------ PRACTICA
P_SOBRA = [
    {"area": "vi", "q": "En la estación", "o": ["la sartén", "el andén", "la vía", "la taquilla"], "why": "La sartén es de la cocina. En la estación: el andén, la vía y la taquilla."},
    {"area": "vi", "q": "Viajar en avión", "o": ["la parada de autobús", "la puerta de embarque", "facturar", "el equipaje de mano"], "why": "La parada es del autobús. En el aeropuerto: facturar, la puerta de embarque, el equipaje de mano."},
    {"area": "vi", "q": "El alojamiento", "o": ["el andén", "el hostal", "el albergue", "el hotel"], "why": "El andén es de la estación. Hostal, albergue y hotel son sitios para dormir."},
    {"area": "oc", "q": "Los espectáculos", "o": ["la asignatura", "el teatro", "el concierto", "la exposición"], "why": "La asignatura es de los estudios."},
    {"area": "oc", "q": "Deportes con pelota", "o": ["nadar", "jugar al fútbol", "jugar al tenis", "jugar al baloncesto"], "why": "Para nadar no hace falta pelota."},
    {"area": "oc", "q": "En el teatro", "o": ["el sueldo", "la taquilla", "la actriz", "la fila"], "why": "El sueldo es del trabajo."},
    {"area": "es", "q": "Centros de estudio", "o": ["la oficina", "el colegio", "el instituto", "la universidad"], "why": "En la oficina se trabaja; en las otras tres, se estudia."},
    {"area": "es", "q": "Los exámenes", "o": ["el estreno", "aprobar", "suspender", "la nota"], "why": "El estreno es el primer día de una película o una obra de teatro."},
    {"area": "tr", "q": "Las profesiones", "o": ["el pasajero", "el cocinero", "el mecánico", "el peluquero"], "why": "El pasajero viaja en el tren o en el avión: no es una profesión."},
    {"area": "tr", "q": "Las condiciones del trabajo", "o": ["el billete", "el sueldo", "el contrato", "la media jornada"], "why": "El billete es para viajar."},
    {"area": "ti", "q": "Cuando llueve", "o": ["las gafas de sol", "el paraguas", "el chubasquero", "las botas de agua"], "why": "Las gafas de sol son para cuando hace sol."},
    {"area": "ti", "q": "Las estaciones", "o": ["la semana", "la primavera", "el otoño", "el invierno"], "why": "La semana tiene siete días; no es una estación."},
    {"area": "ti", "q": "El paisaje", "o": ["el ascensor", "el río", "el bosque", "el lago"], "why": "El ascensor está en un edificio."},
    {"area": "ri", "q": "En correos", "o": ["el cajero", "el sello", "el sobre", "el paquete"], "why": "El cajero es del banco: allí sacas dinero."},
    {"area": "ri", "q": "El móvil", "o": ["el sello", "la batería", "el cargador", "la pantalla"], "why": "El sello es para las cartas."},
]
P_VERBO = [
    {"area": "vi", "q": "En el aeropuerto tenemos que ____ la maleta grande.", "o": ["facturar", "aparcar", "reservar"], "why": "<b>Facturar</b> la maleta: la das en el mostrador y viaja en el avión."},
    {"area": "vi", "q": "Ya he ____ el hotel por internet.", "o": ["reservado", "alquilado", "comprado"], "why": "<b>Reservar</b> un hotel, una mesa, una habitación."},
    {"area": "oc", "q": "Los domingos ____ al tenis con mi padre.", "o": ["juego", "toco", "hago"], "why": "<b>Jugar al</b> tenis, al fútbol, al pádel."},
    {"area": "oc", "q": "Mi hermana ____ el piano desde pequeña.", "o": ["toca", "juega", "hace"], "why": "Los instrumentos se <b>tocan</b>: tocar el piano, la guitarra."},
    {"area": "oc", "q": "Esta noche vamos a ____ una película en casa.", "o": ["ver", "mirar", "tomar"], "why": "<b>Ver</b> una película (o una serie, un partido)."},
    {"area": "es", "q": "Este año me he ____ a un curso de francés.", "o": ["apuntado", "metido", "puesto"], "why": "<b>Apuntarse a</b> un curso, a una clase, al gimnasio."},
    {"area": "es", "q": "Si estudias mucho, vas a ____ el examen.", "o": ["aprobar", "pasar", "ganar"], "why": "<b>Aprobar</b> un examen (y si no, suspender)."},
    {"area": "es", "q": "El lunes ____ un examen de matemáticas.", "o": ["tengo", "tomo", "doy"], "why": "<b>Tener</b> un examen (o hacer un examen)."},
    {"area": "tr", "q": "He enviado mi ____ a cinco empresas.", "o": ["currículum", "contrato", "sueldo"], "why": "Para buscar trabajo, envías tu <b>currículum</b>."},
    {"area": "tr", "q": "Mi hermano ____ de camarero en un bar.", "o": ["trabaja", "es", "hace"], "why": "<b>Trabajar de</b> camarero (o ser camarero, sin «de»)."},
    {"area": "ti", "q": "Coge el paraguas: está ____ .", "o": ["lloviendo", "haciendo", "nevado"], "why": "<b>Está lloviendo</b> (llueve)."},
    {"area": "ti", "q": "Hoy ____ mucho viento.", "o": ["hace", "está", "es"], "why": "<b>Hace</b> viento, sol, frío, calor."},
    {"area": "ri", "q": "Tengo que ____ el móvil: no tiene batería.", "o": ["cargar", "llenar", "poner"], "why": "<b>Cargar</b> el móvil (con el cargador)."},
    {"area": "ri", "q": "En el ayuntamiento hay que ____ un formulario.", "o": ["rellenar", "llevar", "cerrar"], "why": "<b>Rellenar</b> un formulario: escribir tus datos."},
]
E_BIENMAL = [
    {"q": "Los sábados juego fútbol con mis amigos.", "ok": 1, "fix": "Los sábados juego <b>al</b> fútbol con mis amigos.", "why": "Jugar <b>al</b> fútbol, al tenis, al pádel.", "det": "jugar_sin_al"},
    {"q": "Mi hermano juega la guitarra muy bien.", "ok": 1, "fix": "Mi hermano <b>toca</b> la guitarra muy bien.", "why": "Los instrumentos se tocan.", "det": "jugar_instrumento"},
    {"q": "Todos los martes atiendo a clase de inglés.", "ok": 1, "fix": "Todos los martes <b>voy a</b> clase de inglés.", "why": "A clase se va (o se asiste). Atender es ayudar a alguien: atender a los clientes.", "det": "atender_clase"},
    {"q": "Mañana tomo un examen de historia.", "ok": 1, "fix": "Mañana <b>tengo</b> un examen de historia.", "why": "Tener un examen (o hacer un examen).", "det": "tomar_examen"},
    {"q": "He aplicado para un trabajo en un hotel.", "ok": 1, "fix": "He <b>enviado mi currículum</b> a un hotel.", "why": "En español no se dice «aplicar para»: envías el currículum o te presentas a una oferta.", "det": "aplicar_trabajo"},
    {"q": "Hoy hace lluvia y mucho viento.", "ok": 1, "fix": "Hoy <b>llueve</b> y hace mucho viento.", "why": "Hace sol, frío, viento; pero llueve, nieva, está nublado, hay tormenta.", "det": "hace_lluvia"},
    {"q": "En agosto es mucho calor.", "ok": 1, "fix": "En agosto <b>hace</b> mucho calor.", "why": "El tiempo: hace calor, hace sol, hace viento.", "det": "es_calor"},
    {"q": "Ya tengo los billetes del concierto.", "ok": 1, "fix": "Ya tengo las <b>entradas</b> del concierto.", "why": "Para un concierto, el cine o el teatro: la entrada. El billete es para viajar.", "det": "billete_espectaculo"},
    {"q": "El verano pasado hice vacaciones en Italia.", "ok": 1, "fix": "El verano pasado <b>fui de vacaciones</b> a Italia.", "why": "Ir de vacaciones, estar de vacaciones, pasar las vacaciones.", "det": "hacer_vacaciones"},
    {"q": "¿Dónde compro el ticket del tren?", "ok": 1, "fix": "¿Dónde compro el <b>billete</b> del tren?", "why": "Para el tren, el autobús o el avión: el billete. El ticket es el papel de la compra.", "det": "ticket_tren"},
    {"q": "Anoche miramos una película en casa.", "ok": 1, "fix": "Anoche <b>vimos</b> una película en casa.", "why": "Una película se ve.", "det": "mirar_pelicula"},
    {"q": "Mi hija ha pasado el examen de conducir.", "ok": 1, "fix": "Mi hija ha <b>aprobado</b> el examen de conducir.", "why": "Un examen se aprueba.", "det": "pasar_examen"},
    {"q": "Juego al tenis los martes y toco el piano los jueves.", "ok": 0, "fix": "", "why": "Correcto: jugar al tenis, tocar el piano.", "det": None},
    {"q": "El tren de Madrid lleva veinte minutos de retraso.", "ok": 0, "fix": "", "why": "Correcto: llevar retraso.", "det": None},
    {"q": "Mañana va a llover: llévate el paraguas.", "ok": 0, "fix": "", "why": "Correcto: va a llover.", "det": None},
    {"q": "He aprobado todas las asignaturas.", "ok": 0, "fix": "", "why": "Correcto: aprobar una asignatura.", "det": None},
    {"q": "Trabajo a media jornada en una tienda.", "ok": 0, "fix": "", "why": "Correcto: trabajar a media jornada.", "det": None},
    {"q": "¿Quedan entradas para el teatro?", "ok": 0, "fix": "", "why": "Correcto: las entradas del teatro.", "det": None},
]

MOTIVOS = {
    "transporte": ("vi", "Por la vía y desde la estación: el <b>tren</b>.", ["tren"]),
    "retraso": ("vi", "Si sale más tarde, lleva <b>retraso</b>.", ["retraso"]),
    "habitacion": ("vi", "Para dos personas: habitación <b>doble</b>.", ["doble"]),
    "incluido": ("vi", "No lo pagas aparte: está <b>incluido</b>.", ["incluido"]),
    "turismo": ("vi", "Un guía te enseña la ciudad: la <b>visita guiada</b>.", ["visita guiada"]),
    "fotos": ("oc", "Fotos se <b>hacen</b>: hacer fotos.", ["hicimos"]),
    "anden": ("vi", "El tren sale del <b>andén</b>; el autobús, de la parada.", ["andén"]),
    "jugar": ("oc", "Los deportes se <b>juegan</b>: jugar al pádel.", ["jugué"]),
    "entradas": ("oc", "Para el teatro o el cine: las <b>entradas</b>.", ["entradas"]),
    "taquilla": ("oc", "Las entradas se compran en la <b>taquilla</b>.", ["taquilla"]),
    "espectaculo": ("oc", "En una obra de teatro trabajan los <b>actores</b>.", ["actores"]),
    "tiempo": ("ti", "El tiempo: <b>hacía</b> buen tiempo, hace sol, hace frío.", ["hacía"]),
    "deporte": ("oc", "Andar por la montaña: <b>hacer senderismo</b>.", ["hacer senderismo"]),
    "instrumento": ("oc", "Los instrumentos se <b>tocan</b>.", ["tocó"]),
    "apuntarse": ("es", "<b>Apuntarse</b> a un curso.", ["apuntado"]),
    "centro": ("es", "Los cursos de idiomas se hacen en una <b>academia</b>.", ["academia"]),
    "nivel": ("es", "La prueba te dice tu <b>nivel</b>: inicial, intermedio...", ["nivel"]),
    "horario": ("es", "Los días y las horas de clase: el <b>horario</b>.", ["horario"]),
    "nota": ("es", "La profesora pone una <b>nota</b>: un ocho, un cinco...", ["nota"]),
    "aprobar": ("es", "Con un ocho, el examen está <b>aprobado</b>.", ["aprobado"]),
    "suspender": ("es", "Lo contrario de aprobar: <b>suspender</b>.", ["suspendido"]),
    "movil": ("ri", "Las fotos se mandan por el <b>móvil</b>.", ["móvil"]),
    "entrevista": ("tr", "Antes de darte el trabajo, te hacen una <b>entrevista</b>.", ["entrevista"]),
    "contrato": ("tr", "El papel que firmas para trabajar: el <b>contrato</b>.", ["contrato"]),
    "jornada": ("tr", "Cuatro horas al día: <b>media jornada</b>.", ["media jornada"]),
    "sueldo": ("tr", "El dinero que ganas cada mes: el <b>sueldo</b>.", ["sueldo"]),
    "jefe": ("tr", "La persona que manda en tu trabajo: la <b>jefa</b>.", ["jefa"]),
    "vacaciones": ("tr", "Los días sin trabajar en agosto: las <b>vacaciones</b>.", ["vacaciones"]),
}
TEXTOS = [
    {"id": "viaje", "tipo": "Escritura · tarea 1 · correo a una amiga", "titulo": "Desde Valencia",
     "texto": "¡Hola, Julia!<br>Te escribo desde Valencia. Llegué el viernes en [[tren|barco|taxi#transporte]], pero salió con una hora de [[retraso|salida|llegada#retraso]]. "
              "El hotel está en el centro: tenemos una habitación [[doble|individual|libre#habitacion]] para Pablo y para mí, con desayuno [[incluido|lleno|cerrado#incluido]]. "
              "Ayer hicimos una [[visita guiada|reserva|maleta#turismo]] por el casco antiguo y por la tarde [[hicimos|jugamos|tomamos#fotos]] muchas fotos en la playa. "
              "Mañana volvemos: el tren sale del [[andén|parada|puerta#anden]] tres a las seis.<br>Besos,<br>Clara"},
    {"id": "finde", "tipo": "Escritura · tarea 2 · blog", "titulo": "Un fin de semana genial",
     "texto": "El fin de semana pasado fue genial. El sábado por la mañana [[jugué|toqué|hice#jugar]] al pádel con mis compañeros de trabajo. Por la tarde fuimos al teatro: "
              "compramos las [[entradas|billetes|tickets#entradas]] en la [[taquilla|recepción|parada#taquilla]] media hora antes. La obra era muy divertida y los "
              "[[actores|cantantes|pintores#espectaculo]] eran muy buenos. El domingo [[hacía|era|estaba#tiempo]] muy buen tiempo y fuimos a la montaña a "
              "[[hacer senderismo|jugar senderismo|tocar senderismo#deporte]]. Por la noche, mi hermano [[tocó|jugó|hizo#instrumento]] la guitarra en la terraza."},
    {"id": "curso", "tipo": "Escritura · tarea 1 · mensaje a un amigo", "titulo": "Mi curso de alemán",
     "texto": "¡Hola, Pedro!<br>¿Sabes qué? Me he [[apuntado|metido|puesto#apuntarse]] a un curso de alemán en una [[academia|farmacia|estación#centro]] de mi barrio. "
              "Primero hice una prueba de [[nivel|nota|matrícula#nivel]]. Las clases son por la tarde: tengo un [[horario|sueldo|retraso#horario]] perfecto. Cada semana "
              "hacemos un examen corto y la profesora nos pone una [[nota|cuenta|receta#nota]]. El primero lo he [[aprobado|pasado|ganado#aprobar]] con un ocho, pero mi "
              "compañero de clase lo ha [[suspendido|perdido|caído#suspender]]. Te mando una foto de la clase por el [[móvil|sello|cajero#movil]].<br>Un abrazo,<br>Iván"},
    {"id": "trabajo", "tipo": "Escritura · tarea 1 · correo a una amiga", "titulo": "¡Tengo trabajo nuevo!",
     "texto": "¡Hola, Rosa!<br>¡Tengo trabajo nuevo! Hace dos semanas tuve una [[entrevista|reunión|oferta#entrevista]] en una agencia de viajes y me eligieron. Es un "
              "[[contrato|currículum|anuncio#contrato]] de un año, a [[media jornada|jornada completa|media hora#jornada]]: trabajo cuatro horas por la mañana. El "
              "[[sueldo|precio|billete#sueldo]] no es muy alto, pero me gusta mucho. Mi [[jefa|clienta|alumna#jefe]] es muy amable y mis compañeros también. ¡Y en "
              "agosto tengo dos semanas de [[vacaciones|fiestas|turnos#vacaciones]]!<br>Un abrazo,<br>Lola"},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
LAMINAS = [
    {"id": "sara", "tarea": "Tarea 1 · correo a una amiga", "palabras": [60, 70], "trato": "tú",
     "intro": "Ha recibido este mensaje de su amiga Sara:",
     "mensaje": "¡Hola! ¡Por fin he terminado los exámenes! Ahora quiero hacer un viaje contigo en julio. ¿Adónde podemos ir? ¿Cómo viajamos? ¿Y qué tiempo hace allí? Cuéntame también qué tal en tu trabajo nuevo. Muchos besos, Sara",
     "consigna": "Escriba un correo a Sara. En él tiene que:",
     "pautas": [("felicitarla por los exámenes y preguntarle por sus notas;", ["es"]),
                ("contarle qué tal en su trabajo este mes;", ["tr"]),
                ("proponerle un sitio para ir y cómo viajar;", ["vi"]),
                ("decirle qué tiempo hace allí en julio y qué tiene que llevar;", ["ti"]),
                ("proponerle qué hacer allí en el tiempo libre y despedirse.", ["oc"])]},
    {"id": "semana", "tarea": "Tarea 2 · texto para una revista", "palabras": [70, 80], "trato": "",
     "intro": "Una revista para estudiantes de español busca textos sobre este tema:",
     "mensaje": "«Mi semana: trabajo, estudios y tiempo libre»",
     "consigna": "Escriba un texto para la revista. Hable de:",
     "pautas": [("dónde trabaja o estudia y cómo es su horario;", ["tr"]),
                ("qué hacía en su tiempo libre cuando era niño o niña;", ["oc"]),
                ("qué hace ahora los fines de semana y con quién;", ["oc"]),
                ("para qué usa el móvil y las redes sociales;", ["ri"]),
                ("qué estación del año prefiere para salir y por qué.", ["ti"])]},
]

# ------------------------------------------------------------------ DETECTOR (texto sin tildes, en minusculas)
DETECTOR = [
    {"id": "jugar_sin_al", "t": "r", "sc": "s",
     "re": r"\b(?:juego|juegas|juega|jugamos|jugais|juegan|jugar|jugaba|jugabas|jugabamos|jugaban|jugue|jugaste|jugo|jugaron|jugado)\s+(?:futbol|tenis|baloncesto|padel|voleibol|golf)\b",
     "msg": "Los deportes con pelota llevan <b>al</b>: jugar al fútbol, al tenis, al pádel."},
    {"id": "jugar_instrumento", "t": "r", "sc": "s",
     "re": r"\b(?:jueg|jug)\w*\s+(?:a\s+|al\s+)?(?:la\s+|el\s+)?(?:guitarra|piano|violin|flauta|bateria)\b",
     "msg": "Los instrumentos se <b>tocan</b>: tocar la guitarra, tocar el piano."},
    {"id": "atender_clase", "t": "r", "sc": "s", "re": r"\bati?end\w*\s+(?:a\s+)?(?:la\s+|las\s+|una\s+)?clases?\b",
     "msg": "A clase <b>se va</b>: voy a clase de inglés. <i>Atender</i> es ayudar a alguien (atender a los clientes)."},
    {"id": "tomar_examen", "t": "r", "sc": "s",
     "re": r"\b(?:tomo|tomas|toma|tomamos|tomais|toman|tomar|tome|tomaste|tomaron|tomado|tomaba)\s+(?:un|el|mi|tu|su|este|ese|los)\s+examen(?:es)?\b",
     "msg": "Un examen se <b>tiene</b> o se <b>hace</b>: mañana tengo un examen."},
    {"id": "aplicar_trabajo", "t": "r", "sc": "s",
     "re": r"\baplic\w*\s+(?:para|a)\s+(?:(?:un|una|el|la|este|esta|ese|esa)\s+)?(?:trabajo|puesto|oferta|beca)\b",
     "msg": "Para pedir un trabajo: <b>envío mi currículum</b> o <b>me presento a la oferta</b>."},
    {"id": "hace_lluvia", "t": "r", "sc": "s",
     "re": r"\b(?:hace|hacia|hizo|va a hacer)\s+(?:mucha\s+|un poco de\s+)?(?:lluvia|nieve|nublado|niebla|tormentas?)\b",
     "msg": "Hace sol, frío o viento; pero <b>llueve</b>, <b>nieva</b>, <b>está nublado</b>, <b>hay niebla</b>, <b>hay tormenta</b>."},
    {"id": "es_calor", "t": "r", "sc": "s", "re": r"\b(?:es|era|fue|esta|estaba)\s+(?:mucho\s+|muy\s+)?(?:calor|sol|viento)\b",
     "msg": "El tiempo va con <b>hacer</b>: hace calor, hace sol, hace viento."},
    {"id": "billete_espectaculo", "t": "r", "sc": "s",
     "re": r"\bbilletes?\s+(?:de|del|para)\s+(?:el\s+|la\s+)?(?:concierto|cine|teatro|museo|partido|pelicula|exposicion|obra)\b",
     "msg": "Para el cine, el teatro o un concierto: la <b>entrada</b>. El billete es para viajar."},
    {"id": "hacer_vacaciones", "t": "r", "sc": "s", "re": r"\b(?:hago|haces|hace|hacemos|hacen|hacer|hice|hizo|hicimos|hicieron)\s+(?:las\s+|unas\s+|mis\s+|sus\s+)?vacaciones\b",
     "msg": "<b>Ir de vacaciones</b>, <b>estar de vacaciones</b> o <b>pasar las vacaciones</b> (no «hacer vacaciones»)."},
    {"id": "ticket_tren", "t": "a", "sc": "s", "re": r"\btickets?\s+(?:de|del|para)\s+(?:el\s+|la\s+)?(?:tren|autobus|avion|metro|barco)\b",
     "msg": "Para viajar se compra el <b>billete</b>. El ticket es el papel que te dan al pagar en una tienda."},
    {"id": "mirar_pelicula", "t": "a", "sc": "s", "re": r"\bmir\w*\s+(?:una|la|las|unas|esta|esa)\s+peliculas?\b",
     "msg": "Una película se <b>ve</b>: vimos una película."},
    {"id": "pasar_examen", "t": "a", "sc": "s", "re": r"\bpas\w*\s+(?:el|un|los|mi|tu|su|este)\s+examen(?:es)?\b",
     "msg": "Un examen se <b>aprueba</b>: he aprobado el examen."},
    {"id": "cosa_rep", "t": "a", "sc": "x", "re": r"^(?=(?:(?:.|\n)*?\bcosas?\b){3})",
     "msg": "Has escrito <b>cosa</b> tres veces o más. Usa el nombre de verdad: el andén, la taquilla, el currículum..."},
    {"id": "bonito_rep", "t": "a", "sc": "x", "re": r"^(?=(?:(?:.|\n)*?\bbonit[oa]s?\b){3})",
     "msg": "Has escrito <b>bonito</b> tres veces o más. Varía: precioso, divertido, tranquilo, interesante..."},
    {"id": "divertido_rep", "t": "a", "sc": "x", "re": r"^(?=(?:(?:.|\n)*?\bdivertid[oa]s?\b){3})",
     "msg": "Has escrito <b>divertido</b> tres veces o más. Varía: genial, estupendo, interesante, emocionante..."},
]
REQ = ["jugar_sin_al", "jugar_instrumento", "atender_clase", "tomar_examen", "aplicar_trabajo", "hace_lluvia", "es_calor",
       "billete_espectaculo", "hacer_vacaciones", "ticket_tren", "mirar_pelicula", "pasar_examen"]
DETECTOR_PRUEBAS = [
    ("Los sábados juego fútbol con mis amigos.", ["jugar_sin_al"]),
    ("Mi hijo jugaba baloncesto en el colegio.", ["jugar_sin_al"]),
    ("Mi hermano juega la guitarra muy bien.", ["jugar_instrumento"]),
    ("De pequeña jugaba al piano.", ["jugar_instrumento"]),
    ("Todos los martes atiendo a clase de inglés.", ["atender_clase"]),
    ("Mañana tomo un examen de historia.", ["tomar_examen"]),
    ("He aplicado para un trabajo en un hotel.", ["aplicar_trabajo"]),
    ("Hoy hace lluvia y mucho viento.", ["hace_lluvia"]),
    ("Ayer hizo nublado todo el día.", ["hace_lluvia"]),
    ("En agosto es mucho calor.", ["es_calor"]),
    ("Ya tengo los billetes del concierto.", ["billete_espectaculo"]),
    ("El verano pasado hice vacaciones en Italia.", ["hacer_vacaciones"]),
    ("¿Dónde compro el ticket del tren?", ["ticket_tren"]),
    ("Anoche miramos una película en casa.", ["mirar_pelicula"]),
    ("Mi hija ha pasado el examen de conducir.", ["pasar_examen"]),
    ("El viaje fue una cosa genial, con cosas buenas y cosas raras.", ["cosa_rep"]),
    ("Es un pueblo bonito, con una playa bonita y un río bonito.", ["bonito_rep"]),
    ("Fue divertido: un partido divertido y una cena divertida.", ["divertido_rep"]),
    ("Juego al fútbol los sábados.", []),
    ("Mi hermano toca la guitarra y juega al tenis.", []),
    ("Juego con mi hijo en el parque.", []),
    ("En el hotel atiendo a los clientes.", []),
    ("Mañana tengo un examen de historia.", []),
    ("Tomamos un café después del examen.", []),
    ("Hoy hace sol y mucho viento.", []),
    ("Hoy llueve y está nublado.", []),
    ("El café está frío y la sopa está caliente.", []),
    ("El invierno en mi ciudad es frío.", []),
    ("He comprado las entradas del concierto y el billete de tren.", []),
    ("En agosto hago la maleta y me voy de vacaciones.", []),
    ("Guarda el ticket de la tienda.", []),
    ("Vimos una película y miramos las fotos del viaje.", []),
    ("Paso las tardes en la biblioteca antes del examen.", []),
    ("He aprobado el examen de conducir.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL (la escena en un minuto)
# Fotos 1-6 del taller de la foto (M4T2_fotoN.jpg, ya en WordPress): las de fuera de casa. La R14a usa las fotos 7-12.
ORAL = [
    {"id": 1, "titulo": "Una comida en el campo", "desc": "Una familia celebra el cumpleaños de la abuela en el campo, debajo de un olivo: la abuela sopla las velas, el tío toca la guitarra y un perro se lleva un bocadillo.",
     "grupos": [("Las personas y la ropa", ["la abuela", "el abuelo", "el tío", "la nieta", "la boina", "el sombrero de paja", "la gorra", "el vestido de flores"]),
                ("El lugar y el tiempo", ["el campo", "el olivo", "las flores", "la casa de campo", "hace sol", "hace viento", "la primavera", "el mediodía"]),
                ("Qué hacen", ["celebrar el cumpleaños", "soplar las velas", "aplaudir", "tocar la guitarra", "correr", "comer al aire libre"])]},
    {"id": 2, "titulo": "En el veterinario", "desc": "En la sala de espera de un veterinario, una niña con chubasquero abraza a su perro, que tiene una venda en la pata; fuera llueve mucho.",
     "grupos": [("Las personas y la ropa", ["el padre", "la niña", "la señora", "el chico", "la recepcionista", "el chubasquero", "las botas de agua", "el traje", "el uniforme"]),
                ("El lugar y las cosas", ["la sala de espera", "el mostrador", "la báscula", "el transportín", "el paraguas", "la ventana", "llueve", "el invierno"]),
                ("Qué hacen", ["esperar", "abrazar", "hablar por teléfono", "estar preocupado", "estar herido"])]},
    {"id": 3, "titulo": "En la lavandería", "desc": "En una lavandería de barrio, de noche, sale mucha espuma de la lavadora de un chico pelirrojo; una pareja dobla una sábana y un señor mayor se ríe.",
     "grupos": [("Las personas y la ropa", ["el chico", "la pareja", "el señor mayor", "pelirrojo", "las gafas", "la sudadera", "la mochila", "el bigote"]),
                ("El lugar y las cosas", ["la lavandería", "la lavadora", "la secadora", "el detergente", "la espuma", "la máquina de café", "el banco", "la noche"]),
                ("Qué hacen", ["lavar la ropa", "doblar una sábana", "sorprenderse", "reírse", "leer", "esperar"])]},
    {"id": 4, "titulo": "En la cocina de un restaurante", "desc": "En la cocina de un restaurante, un sábado de verano a mediodía, sale humo de la sartén del aprendiz y la jefa de cocina se lleva las manos a la cabeza.",
     "grupos": [("Las personas y la ropa", ["la jefa de cocina", "el cocinero", "el aprendiz", "la camarera", "el delantal", "el gorro", "la barba", "la coleta"]),
                ("El lugar y las cosas", ["la cocina", "el restaurante", "el fogón", "la sartén", "la olla", "el humo", "el ventilador", "el comedor"]),
                ("Qué hacen", ["trabajar", "cocinar", "cortar verduras", "quemarse la comida", "llevar las paellas", "tener prisa", "hace calor"])]},
    {"id": 5, "titulo": "En la pista de patinaje", "desc": "En una pista de patinaje de una plaza, en Navidad, un niño se ha caído en el hielo; su madre intenta ayudarle y el abuelo hace una foto con el móvil.",
     "grupos": [("Las personas y la ropa", ["el niño", "la madre", "el abuelo", "el monitor", "el casco", "los guantes", "el gorro de lana", "la bufanda", "el abrigo"]),
                ("El lugar y las cosas", ["la pista de patinaje", "el hielo", "la plaza", "el árbol de Navidad", "las luces", "los patines", "la valla", "hace frío"]),
                ("Qué hacen", ["patinar", "caerse", "ayudar", "hacer una foto", "tomar chocolate", "celebrar la Navidad"])]},
    {"id": 6, "titulo": "Trabajar en casa", "desc": "Un padre teletrabaja en el salón con una videollamada; su hija enseña un dibujo a la cámara y el bebé tira la papilla desde la trona.",
     "grupos": [("Las personas y la ropa", ["el padre", "la hija", "el bebé", "los compañeros de trabajo", "los auriculares", "la camisa", "el pantalón corto", "las chanclas", "el pijama"]),
                ("El lugar y las cosas", ["el salón", "el portátil", "la videollamada", "la pantalla", "la mesa", "la trona", "el ventilador", "el balcón"]),
                ("Qué hacen", ["trabajar desde casa", "tener una reunión", "hablar con los compañeros", "enseñar un dibujo", "no poder trabajar tranquilo"])]},
]
