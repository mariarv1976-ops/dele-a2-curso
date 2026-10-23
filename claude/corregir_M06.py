# -*- coding: utf-8 -*-
# Corrige fuente_M06.py según lo visto en los exámenes reales (15/10/2026, claude/DELE_A2_examen_real_hallazgos.txt):
#  - escritura T1: correo a un amigo, de tú (antes: de usted a una tienda);
#  - oral T1: una pauta que sorprende en cada opción;
#  - oral T2: fotos sencillas y domésticas como las de 2022 (antes: tienda de montaña con mucha gente y hotel de noche);
#  - oral T3: las dos opciones de tú, con pautas que mezclan planificar y contar cosas propias (antes: la 2 era un hotel).
# Uso: python3 corregir_M06.py   (en la carpeta de fuente_M06.py). Si ya está corregido, no hace nada.
import re, sys
P = "fuente_M06.py"
s = open(P, encoding="utf-8").read()
if "Pintar la casa" in s:
    sys.exit("fuente_M06.py ya está corregido")

def cambia(ini, fin, nuevo):
    """Sustituye desde la línea que empieza por `ini` hasta justo antes de la que empieza por `fin`."""
    global s
    a = s.find(ini); b = s.find(fin, a + 1)
    assert a >= 0 and b > a and s.count(ini) == 1, (ini, a, b)
    s = s[:a] + nuevo + s[b:]

def rep(viejo, nuevo):
    global s
    assert s.count(viejo) == 1, viejo[:60]
    s = s.replace(viejo, nuevo)

rep("un trabajo de verano, un viaje a la montaña y un hotel.", "un trabajo de verano, un viaje a la montaña y pintar la casa.")

# ---------------- ESCRITURA T1 + su modelo ----------------
cambia('ESCRITA = {"t1":', ' "t2": {"instr": "Elija solo una',
'''ESCRITA = {"t1": {"instr": "Su amigo Pablo, que vive en otra ciudad, le ha escrito este correo.", "trato": "tú",
  "input": ["¡Hola! ¿Qué tal todo? ¡Por fin tengo vacaciones! Voy a tu ciudad del 3 al 6 de diciembre. ¿Qué podemos hacer esos días? ¿Puedo dormir en tu casa o busco un hotel? Cuéntame también qué tal estás tú.", "Un abrazo,<br>Pablo"],
  "lead": "Conteste a Pablo. En el correo tiene que:",
  "pautas": ["saludar y decirle qué le parece su visita;", "contarle qué ha hecho usted estas últimas semanas;", "proponerle dos planes para esos días y explicar por qué;", "contestar si puede dormir en su casa y por qué;", "hacerle dos preguntas sobre su viaje y despedirse."],
  "min": 60, "max": 70},
''')
cambia(' "modelos": {\n  "t1":', '  "op1": {"titulo": "Tarea 2 · Opción 1',
''' "modelos": {
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
''')

# ---------------- ORAL T1, T2, T3 + modelos de la T3 ----------------
cambia('ORAL = {"t1":', '# ---------------- PROFESORA ----------------',
'''ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
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

''')

# ---------------- GUION DEL EXAMINADOR (esquema para la interacción, como el Modelo 0) ----------------
cambia('GUION_ENTREVISTADOR = """', 'ERRORES = """',
'''GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
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
''')
rep("*Hay el recepcionista (está / hay un recepcionista)", "*Hay el sofá en el centro (el sofá está / hay un sofá)")
rep("*Quiero ir en la playa (a\n  la playa)", "*Quiero ir en la montaña (a\n  la montaña)")

# ---------------- FOTOS: receta de 2022 (dos personas, una acción, sitio corriente) ----------------
cambia(' "oral_foto1": {"situacion": "tienda de material', ' "escrita": {"situacion":',
''' "oral_foto1": {"situacion": "salón de casa: dos hermanos preparan las mochilas para la montaña",
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
''')
rep('''  "problema": "Bruno pasa vergüenza cuando se le cae la bandeja delante de los clientes"},''',
    '''  "detalle": "Bruno pasa vergüenza cuando se le cae la bandeja delante de los clientes"},''')
rep('"M06": ["tienda de material de montaña una mañana de otoño", "recepción de un hotel pequeño de costa una noche de verano con tormenta"],',
    '"M06": ["salón de casa: dos hermanos preparan las mochilas para la montaña", "padre e hija pintan el salón de un piso"],')
cambia(' "oral_foto1": "A photo inside a large outdoor-gear shop', '}\nIMG_NAMES = {',
''' "oral_foto1": "A brother and a sister of about 30 in the living room of an ordinary Spanish flat on an autumn evening, packing for a weekend in the mountains. The sister, with long dark hair in a ponytail, glasses and a grey sweatshirt, kneels on the floor and pushes a rolled-up sleeping bag into a big red backpack. Her brother, with a short beard, a checked flannel shirt and jeans, sits on the sofa holding a pair of hiking boots and looking at the soles; he is wearing a woolly bobble hat indoors, which looks a bit funny. Around them on the floor and the sofa: a second backpack, a folded rain jacket, woolly hats, a torch, a thermos, a water bottle, a packet of biscuits, a small first-aid bag and an open paper map. Behind them an ordinary room: a lamp switched on, a bookshelf, a switched-off TV, a plant, and a window with the dark street outside.",
 "oral_foto2": "A father of about 60 and his daughter of about 25 painting the small living room of a Spanish flat on a sunny spring morning. The daughter, with short curly hair, wears old paint-stained overalls and has a smear of light blue paint on her cheek; she paints a wall light blue with a long roller and laughs. The father, bald with a grey moustache, in an old blue T-shirt and a hat folded from newspaper, stands on a small stepladder painting near the ceiling with a brush. The sofa and a table are pushed to the middle of the room and covered with plastic sheets; on the floor, covered with old newspapers: open paint tins, a paint tray, brushes, masking tape, a small radio and two coffee cups. Daylight comes in through a big window.",
''')
rep('"oral_foto1": "M06_oral_foto1_tienda_montana", "oral_foto2": "M06_oral_foto2_recepcion_hotel"}',
    '"oral_foto1": "M06_oral_foto1_mochilas_montana", "oral_foto2": "M06_oral_foto2_pintar_salon"}')
rep('''            "oral_foto1": "Oral foto 1 tienda de montana: dos hermanos prueban botas y mochila, otono, manana",
            "oral_foto2": "Oral foto 2 recepcion de hotel de costa de noche con tormenta: familia con maletas y recepcionista mayor"}''',
    '''            "oral_foto1": "Oral foto 1 preparar un viaje: dos hermanos hacen las mochilas para la montana en el salon",
            "oral_foto2": "Oral foto 2 pintar la casa: padre e hija pintan el salon de azul claro"}''')
open(P, "w", encoding="utf-8").write(s)
print("ok: fuente_M06.py corregido")
