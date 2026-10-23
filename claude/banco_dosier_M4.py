# -*- coding: utf-8 -*-
# BANCO DEL DOSIER ORAL A2 DE ESTRUCTURAS (curso de preparacion DELE A2, Modulo 4, pieza M4-5)
# Lo usa build_M4_dosier.py, que genera con el MISMO contenido:
#   - DELEA2_dosier_oral_estructuras.pdf (hoja de consulta imprimible, 10 secciones + soluciones)
#   - DELEA2_curso_M4_dosier_oral.html   (ejecutable del curso, con la practica interactiva)
# Base: el dosier A2 de Maria (PDF de 18 paginas). Corregido el 15/10/2026 para que diga lo mismo que la
# Guia oficial y que las demas piezas del curso:
#   1) los 12 minutos de preparacion son para las TRES tareas (reparto 1 + 4 + 4 + 2 + 1, como M4-1/2/3);
#   2) la foto: las SEIS preguntas oficiales en su orden (personas y ropa, lugar y objetos, que hacen,
#      RELACION, que sienten, antes y despues), como la plantilla de M4-2;
#   3) la tarea 3: los dos tipos, PLANIFICAR con un amigo (tu) y SERVICIO (usted), con el pequeno problema;
#      la situacion viene en la lamina (no la explica el entrevistador);
#   4) tu o usted lo dice la lamina (como la R07), no "escucha al entrevistador";
#   5) monologo y descripcion modelo con la longitud real (unas 230-260 palabras = 2-3 minutos; antes 150 y 110);
#   6) la lamina de la tarea 1 con cinco pautas, como las oficiales.
# Marcas: en los textos modelo, las frases del dosier van entre <b></b>.
# Para cambiar contenidos: solo este archivo.

TITULO = "Hablar con estructura"
SUBTITULO = "Dosier de estructuras, consejos y práctica para las tres tareas de la prueba oral"

# Enlaces a otras piezas del curso (codigo -> (titulo, archivo))
PIEZAS = {
 "M4-1": ("Tarea 1: banco de temas", "DELEA2_curso_M4_T1_temas.html"),
 "M4-2": ("Tarea 2: la plantilla de la foto", "DELEA2_curso_M4_T2_foto.html"),
 "M4-3": ("Tarea 3: habla con el examinador", "DELEA2_curso_M4_T3_dialogos.html"),
 "M4-4": ("Qué hacer si me bloqueo", "DELEA2_curso_M4_bloqueo.html"),
 "R01": ("Ficha: los pasados y las preguntas", "DELEA2_curso_R01_pasados.html"),
 "R02": ("Ficha: hay, está y es", "DELEA2_curso_R02_hay_esta_es.html"),
 "R04": ("Ficha: concordancia y posesivos", "DELEA2_curso_R04_concordancia_posesivos.html"),
 "R05": ("Ficha: muy y mucho, también y tampoco", "DELEA2_curso_R05_muy_mucho_tambien_tampoco.html"),
 "R07": ("Ficha: tú y usted", "DELEA2_curso_R07_tu_usted.html"),
}
PDF = "DELEA2_dosier_oral_estructuras.pdf"

# ---------------------------------------------------------------- SECCIONES
# Bloques: ("p", html) · ("h", titulo) · ("tabla", [cabeceras], [[celdas]]) · ("consejo", titulo, html)
#          ("caja", titulo, [lineas]) · ("modelo", intro, [parrafos], nota) · ("dialogo", intro, [(quien, texto)])
#          ("ol", [items]) · ("ul", [items]) · ("enlaces", [codigos])
S = []

S.append({"id": "uso", "n": "", "tab": "inicio", "titulo": "Cómo usar este dosier", "bloques": [
 ("p", "Este dosier es tu caja de herramientas. En el examen los temas cambian (la familia, el trabajo, la casa, las "
       "vacaciones…), pero las tareas piden siempre lo mismo: contar, describir, preguntar y reaccionar. Si tienes las "
       "frases preparadas, solo tienes que pensar en las ideas."),
 ("tabla", ["Sección", "Qué encuentras"], [
   ["1. La prueba por dentro", "Las tareas, el tiempo y qué miran los examinadores"],
   ["2. Los 12 minutos de preparación", "Cómo repartir el tiempo y hacer un esquema con palabras clave"],
   ["3. Tarea 1", "Hablar de un tema: plantilla, frases y modelo"],
   ["4. Tarea 2", "La foto: las seis preguntas, frases y modelo"],
   ["5. Tarea 3", "El diálogo: con un amigo y en una tienda o un servicio"],
   ["6. Recursos de supervivencia", "Qué decir cuando no entiendes o no sabes una palabra"],
   ["7. Errores que bajan la nota", "Los diez más frecuentes, con la forma correcta"],
   ["8. Practica", "Ejercicios con temas variados"],
   ["9. Soluciones", "Respuestas de los ejercicios"],
   ["10. Tarjeta de bolsillo", "Resumen de una página para el día del examen"]]),
 ("h", "Método en cuatro pasos"),
 ("ol", ["Lee una sección y marca las frases que no usas nunca.",
         "Elige tres y dilas en voz alta con un tema cualquiera. Grábate con el móvil.",
         "Practica con los ejercicios de la sección 8 y con la prueba oral de cada simulacro.",
         "Repite. Cuando una frase sale sola, ya es tuya. Entonces elige otra."]),
 ("consejo", "Consejo de examen", "No uses todas las frases a la vez. Es mejor usar bien cinco frases que mezclar veinte. "
             "Elige tus favoritas y practícalas mucho."),
]})

S.append({"id": "prueba", "n": "1", "tab": "inicio", "titulo": "La prueba por dentro", "bloques": [
 ("p", "La prueba oral dura unos 12 minutos. Antes tienes <b>12 minutos para preparar las tres tareas</b>. Hay dos "
       "examinadores: uno habla contigo (el entrevistador) y otro escucha y pone la nota."),
 ("tabla", ["Tarea", "Qué haces", "Tiempo", "¿Se prepara?"], [
   ["1. Hablar de un tema", "Eliges un tema entre dos. Hablas tú solo sobre las cinco pautas de la lámina: tu familia, tu casa, tus vacaciones…", "2-3 min", "Sí (unos 4 min)"],
   ["2. Describir una foto", "Eliges una foto entre dos. Contestas a las seis preguntas de la lámina: cómo son las personas, dónde están, qué hacen…", "2-3 min", "Sí (unos 4 min)"],
   ["3. Diálogo", "Hablas con el entrevistador en una situación relacionada con tu foto. La situación está en la lámina: organizar algo con un amigo (tú) o comprar, reservar o pedir algo (usted).", "3-4 min", "Sí (unos 2 min)"]]),
 ("p", "En las tareas 1 y 2 hablas tú solo. El entrevistador no te pregunta nada; solo te ayuda si te quedas en silencio. "
       "En la tarea 3 es una conversación: él hace un papel (tu amigo, tu compañero de piso, el dependiente…) y tú haces "
       "otro. En algún momento va a crear un <b>pequeño problema</b> (ese día no puede, ya no quedan entradas…): tú "
       "tienes que buscar otra solución."),
 ("h", "Qué miran los examinadores"),
 ("p", "Usan cuatro criterios. Cada uno tiene una nota de 0 a 3. Un 2 es exactamente el nivel A2."),
 ("tabla", ["Criterio", "Qué significa", "Cómo subir la nota"], [
   ["Coherencia", "Tus ideas tienen orden y respondes a lo que te piden.", "Usa <i>primero, después, al final</i>. Une frases con <i>y, pero, porque, también</i>."],
   ["Fluidez", "Hablas sin parar mucho tiempo.", "Las pausas cortas son normales. Usa <i>pues…, a ver…, bueno…</i> para pensar."],
   ["Corrección", "Usas bien lo básico.", "Cuida el presente, los pasados, ser/estar y el masculino/femenino. Una frase simple y correcta es mejor que una frase difícil con errores."],
   ["Alcance", "Tienes palabras para hablar del tema.", "Usa palabras concretas del tema. Si no sabes una palabra, explícala con otras."]]),
 ("consejo", "Consejo de examen", "El examinador no espera perfección. Espera frases sencillas, claras y con orden. Si te "
             "equivocas y te corriges (<i>Ayer voy, perdón, fui al cine</i>), eso es positivo."),
]})

ESQUEMA_T1 = ["Tema: mis mejores vacaciones",
 "1. Adónde y cuándo → Galicia, pueblo, playa · verano pasado (fueron)",
 "2. Con quién y cómo → pareja + hermana · avión + coche (fui, cogimos)",
 "3. Qué hicimos → marisco, playa, barco · lo mejor: tranquilidad (comimos, me gustó)",
 "4. De pequeña → pueblo de los abuelos, calle con mis primos (íbamos, jugaba)",
 "5. Ahora y la próxima vez → descansar, leer · diciembre: Sevilla, flamenco (me gusta, voy a ir)",
 "Final: «Para mí, unas vacaciones perfectas son…»"]

S.append({"id": "prep", "n": "2", "tab": "prep", "titulo": "Los 12 minutos de preparación", "bloques": [
 ("p", "Preparas las tres tareas a la vez. Puedes escribir notas y llevarlas a la sala. Puedes mirarlas, pero no "
       "leerlas: tus notas son un mapa, no un texto."),
 ("tabla", ["Minutos", "Qué hacer"], [
   ["0-1 · Elegir", "Lee los dos temas de la tarea 1 y mira las dos fotos. Elige el tema en el que tienes más ideas y más palabras. Elige la foto mirando también su tarea 3: va en la misma hoja."],
   ["1-5 · Tarea 1", "Para cada pauta de la lámina, 3 o 4 palabras clave y un verbo ya conjugado en el tiempo que pide. Piensa en una frase para empezar y otra para terminar."],
   ["5-9 · Tarea 2", "Escribe los números del 1 al 6 (las seis preguntas de la lámina) y, en cada uno, palabras clave: lo que ves, un detalle y tu opinión."],
   ["9-11 · Tarea 3", "Lee la situación: ¿tú o usted? Para cada pauta, una idea y una pregunta. Piensa también qué vas a decir si el examinador dice que no."],
   ["11-12 · Repasar", "Mira tus notas y repite mentalmente tu primera frase de cada tarea. Empezar es lo más difícil."]]),
 ("caja", "Un esquema que funciona (tarea 1): palabras clave y flechas, nada de frases completas", ESQUEMA_T1),
 ("h", "Lo que no debes hacer"),
 ("ul", ["<b>Escribir el texto entero.</b> No tienes tiempo. Y si lo memorizas, se nota: hablas como un robot y te pierdes si el examinador dice algo.",
         "<b>Olvidar la foto o la tarea 3.</b> Respeta el reparto: unos 4 minutos para el tema, 4 para la foto y 2 para el diálogo.",
         "<b>Buscar una palabra durante mucho tiempo.</b> Si no la sabes, escribe cómo vas a explicarla (<i>el sitio donde…, una cosa para…</i>)."]),
 ("consejo", "Consejo de examen", "Escribe en tu esquema, con otro color, tres frases que quieres usar sí o sí (por ejemplo: "
             "<i>lo que más me gusta es…, a lo mejor, ¿qué te parece si…?</i>). Así no repites siempre lo mismo."),
 ("enlaces", ["M4-1", "M4-2", "M4-3"]),
]})

# Lamina del monologo modelo (formato oficial: titulo + cinco pautas)
LAMINA_T1 = {"titulo": "Mis mejores vacaciones", "pautas": [
 "adónde fue y cuándo;", "con quién fue y cómo viajó;", "qué hizo allí y qué le gustó más;",
 "cómo eran sus vacaciones cuando era pequeño/a;", "qué le gusta hacer ahora en vacaciones y adónde va a ir la próxima vez."]}
MONOLOGO = [
 "«<b>Voy a hablar de</b> mis mejores vacaciones. Fueron <b>el verano pasado</b>, en agosto, en Galicia, en un pueblo pequeño al lado del mar que se llama Cambados.",
 "Fui con mi pareja y con mi hermana. <b>Primero</b> cogimos un avión a Santiago y <b>después</b> alquilamos un coche, <b>porque</b> el pueblo está bastante lejos. El viaje fue muy cómodo y no tardamos mucho.",
 "Allí comimos mucho marisco, nos bañamos en la playa y <b>un día</b> hicimos una excursión en barco. <b>Además</b>, visitamos Santiago y vimos la catedral. <b>Lo que más me gustó fue</b> la tranquilidad: no había mucha gente y la comida era buenísima. ¡Fue genial!",
 "<b>De pequeña</b>, mis vacaciones eran muy diferentes. Siempre <b>íbamos</b> al pueblo de mis abuelos, en el interior, y pasábamos allí todo el verano. No había playa, <b>pero</b> jugaba en la calle con mis primos hasta la noche. Mi abuela cocinaba para todos y por la tarde íbamos al río a bañarnos.",
 "<b>Ahora</b>, en vacaciones, <b>me gusta</b> descansar, leer y pasear, pero <b>no me gustan</b> los sitios con mucha gente. <b>Prefiero</b> los pueblos <b>porque</b> son <b>más tranquilos que</b> las ciudades. <b>Este año todavía no he tenido</b> vacaciones, así que estoy un poco cansada. En diciembre <b>voy a ir</b> a Sevilla con mi hermana y <b>me gustaría</b> ver un espectáculo de flamenco.",
 "<b>Para mí</b>, unas vacaciones perfectas son buena comida, sol y tiempo libre con la gente que quiero.»"]

S.append({"id": "t1", "n": "3", "tab": "t1", "titulo": "Tarea 1. Hablar de un tema", "bloques": [
 ("p", "Hablas 2-3 minutos sobre un tema de tu vida. La lámina tiene cinco pautas (por ejemplo: dónde, con quién, qué "
       "hiciste, cómo era antes, qué planes tienes). Tienes que hablar de <b>todas</b>, en orden. Casi siempre piden "
       "presente, pasado, «antes» (imperfecto) y futuro: es un examen de tiempos verbales."),
 ("h", "La plantilla en tres pasos"),
 ("tabla", ["Paso", "Qué dices", "Tiempo aprox."], [
   ["1. Empezar", "El tema, en una frase.", "10 s"],
   ["2. Desarrollar", "Cada pauta de la lámina, con 2 o 3 frases. Da detalles y ejemplos.", "2 min (unos 25 s por pauta)"],
   ["3. Terminar", "Tu opinión o una frase final.", "10-15 s"]]),
 ("h", "1. Empezar"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Voy a hablar de…", "Voy a hablar de mi barrio."],
   ["He elegido el tema de… porque…", "He elegido el tema de la comida porque me encanta cocinar."]]),
 ("h", "2. Hablar de tu vida ahora (presente)"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Normalmente / Todos los días / Los fines de semana + presente", "Los fines de semana normalmente voy al mercado."],
   ["Vivo en… desde hace…", "Vivo en Alicante desde hace tres años."],
   ["(Casi) siempre / A veces / (Casi) nunca", "A veces como en un restaurante, pero casi nunca ceno fuera."],
   ["Soy… / Trabajo como… / Estudio…", "Trabajo como enfermera en un hospital."]]),
 ("h", "3. Hablar del pasado"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Hoy / Esta semana / Este año + he + participio", "Este año he viajado mucho."],
   ["Ayer / El año pasado / En 2020 + indefinido", "El verano pasado fui a Italia con mi familia."],
   ["Antes / De pequeño(a) + imperfecto", "De pequeña vivía en un pueblo y jugaba en la calle."],
   ["Una vez / Un día…", "Un día perdí el tren y llegué tarde a una boda."]]),
 ("consejo", "Truco: ¿he ido o fui?", "<i>Hoy, esta semana, este año, ya, nunca</i> → <b>he ido</b> (el tiempo todavía no ha "
             "terminado). <i>Ayer, la semana pasada, en 2019</i> → <b>fui</b> (tiempo terminado). (In English: “I have gone” ≠ "
             "“I went” works in a similar way.)"),
 ("h", "4. Gustos y opiniones"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["(No) me gusta + infinitivo / nombre singular", "Me gusta mucho pasear. Me gusta el cine."],
   ["(No) me gustan + nombre plural", "No me gustan las ciudades grandes."],
   ["Me encanta(n) / Odio…", "Me encantan los fines de semana tranquilos."],
   ["Prefiero… porque…", "Prefiero la montaña porque hay menos gente."],
   ["Lo que más me gusta es…", "Lo que más me gusta de mi trabajo es la gente."],
   ["Para mí / Creo que + es…", "Para mí, lo más importante es tener tiempo libre."]]),
 ("h", "5. Comparar"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["más / menos + adjetivo + que", "Mi casa nueva es más grande que la antigua."],
   ["tan + adjetivo + como", "Mi barrio no es tan bonito como el centro."],
   ["mejor / peor que", "Para mí, el tren es mejor que el coche."]]),
 ("h", "6. Planes y deseos"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Voy a + infinitivo", "El próximo verano voy a visitar a mi hermano."],
   ["Quiero / Me gustaría + infinitivo", "Me gustaría aprender a bailar flamenco."],
   ["Pienso + infinitivo", "Pienso cambiar de trabajo el año que viene."]]),
 ("h", "7. Terminar"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Para mí, … es muy importante porque…", "Para mí, mi familia es muy importante porque siempre me ayuda."],
   ["En resumen, …", "En resumen, estoy muy contento en mi barrio."],
   ["Y esto es todo.", "Y esto es todo sobre mi rutina."]]),
 ("h", "Conectores: dan orden a lo que dices"),
 ("tabla", ["Para empezar", "Para seguir", "Para contrastar", "Para explicar", "Para terminar"], [
   ["Primero…<br>Para empezar…", "Después… / Luego…<br>Además… / También…", "Pero…<br>En cambio…", "Porque…<br>Por eso…", "Al final…<br>Para terminar…<br>En resumen…"]]),
 ("h", "Modelo de monólogo"),
 ("modelo", "Lámina: <b>" + LAMINA_T1["titulo"] + "</b>. Hable de: " + " ".join(LAMINA_T1["pautas"]) +
            " Las frases del dosier están en negrita; cada párrafo es una pauta.", MONOLOGO,
  "Unas 250 palabras: dos minutos y medio si hablas tranquilo. Responde a las cinco pautas en orden, usa presente, "
  "pasado, «antes» y futuro, y tiene principio y final."),
 ("consejo", "Consejo de examen", "No memorices este texto. Memoriza la plantilla y las frases: empezar → las pautas de la "
             "lámina en orden → terminar. Así funciona con cualquier tema."),
 ("enlaces", ["M4-1", "R01"]),
]})

# Las seis preguntas oficiales de la lamina de la foto (las mismas que la plantilla de M4-2)
PREGUNTAS_T2 = [
 ("Las personas", "¿Cómo son? ¿Qué ropa llevan?", "Edad, aspecto, cómo parecen ser, ropa."),
 ("El lugar", "¿Dónde están? ¿Qué objetos hay?", "El sitio, lo que hay, el tiempo, la estación."),
 ("Las acciones", "¿Qué están haciendo?", "Lo que pasa ahora en la foto."),
 ("La relación", "¿Qué relación hay entre ellas?", "Familia, amigos, compañeros, desconocidos… y por qué lo crees."),
 ("Los sentimientos", "¿Qué piensan o cómo se sienten? ¿Por qué?", "Contentos, cansados, nerviosos… y por qué."),
 ("Antes y después", "¿Qué han hecho antes? ¿Qué van a hacer después?", "Tu idea: imagina un poco la historia."),
]
FOTO_MODELO = ("Foto: una frutería de barrio una mañana de invierno. Una señora mayor con abrigo marrón compra fruta; "
               "un dependiente joven, con barba y delantal verde, le da una bolsa. Al fondo hay cajas de fruta; la "
               "señora lleva un carro de la compra con una barra de pan.")
DESCRIPCION = [
 "«<b>En la foto hay</b> dos personas. <b>A la izquierda hay</b> una señora mayor; <b>tiene</b> setenta años, más o menos. <b>Tiene el pelo</b> blanco y corto, y <b>lleva</b> un abrigo marrón y un bolso negro. <b>Parece</b> una persona tranquila y simpática. <b>A la derecha está</b> el dependiente. <b>Es</b> joven, alto y delgado, <b>tiene</b> barba y <b>lleva</b> una camiseta gris y un delantal verde.",
 "<b>Están en</b> una frutería de barrio. <b>Al fondo hay</b> muchas cajas de fruta: naranjas, manzanas, plátanos… <b>En el centro hay</b> un mostrador con una balanza y, <b>al lado de</b> la señora, <b>hay</b> un carro de la compra. <b>Creo que es</b> invierno, <b>porque</b> la señora lleva abrigo, y es por la mañana.",
 "El dependiente <b>está dando</b> una bolsa a la señora. Ella <b>está buscando</b> el monedero en su bolso: <b>creo que va a pagar</b> en efectivo. En la bolsa <b>hay</b> naranjas, y en el carro <b>hay</b> una barra de pan.",
 "<b>Creo que</b> no son familia, pero <b>se conocen</b>: <b>seguramente</b> la señora compra en esta tienda todas las semanas. <b>Parece que se llevan bien</b>, <b>porque</b> los dos sonríen y están hablando.",
 "Los dos <b>están</b> contentos. <b>A lo mejor</b> la señora piensa: «¡Qué naranjas tan buenas!». El dependiente <b>parece</b> un poco cansado, <b>porque</b> por la mañana hay mucho trabajo.",
 "<b>Creo que antes</b> la señora <b>ha ido</b> a la panadería, <b>porque</b> lleva una barra de pan en el carro. <b>Después va a</b> volver a casa y <b>va a</b> preparar la comida para su familia.»"]

S.append({"id": "t2", "n": "4", "tab": "t2", "titulo": "Tarea 2. Describir una foto", "bloques": [
 ("p", "Hablas 2-3 minutos sobre una foto de una situación de todos los días: una tienda, una estación, una casa, un "
       "parque… La lámina tiene siempre <b>las mismas seis preguntas</b>, en el mismo orden. Contesta a las seis, en "
       "orden: dices lo que ves e imaginas lo que no ves."),
 ("h", "Las seis preguntas: siempre en el mismo orden"),
 ("tabla", ["Pregunta", "En la lámina", "Qué dices"], [["%d. %s" % (i + 1, p[0]), p[1], p[2]] for i, p in enumerate(PREGUNTAS_T2)]),
 ("consejo", "Consejo de examen", "Si sigues siempre este orden, nunca te quedas sin saber qué decir. En cada pregunta, "
             "<b>tres frases</b>: lo que ves, un detalle y tu opinión. Seis preguntas × tres frases = dos minutos y medio."),
 ("h", "1. Describir a las personas"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Es + alto, joven, rubio…", "El chico es alto y moreno."],
   ["Tiene + el pelo… / los ojos…", "La señora tiene el pelo blanco y los ojos azules."],
   ["Tiene unos … años / … años, más o menos", "Tiene unos setenta años. Tiene treinta años, más o menos."],
   ["Lleva + ropa", "Lleva una camiseta azul y unos vaqueros."],
   ["Parece + simpático, tímido, serio…", "Parece una persona muy tranquila."]]),
 ("h", "2. Situar las cosas"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["En la foto hay…", "En la foto hay tres personas y una mesa grande."],
   ["Están en…", "Están en una estación de tren."],
   ["A la izquierda / A la derecha…", "A la derecha hay una mujer con un carro de la compra."],
   ["En el centro / Delante / Detrás / Al fondo…", "Al fondo hay muchas botellas en una estantería."],
   ["Encima de / Debajo de / Al lado de…", "Al lado de la caja hay un perro pequeño."]]),
 ("consejo", "Diferencia importante: hay / está", "<b>Hay</b> + un, una, unos, dos, muchos… (<i>hay una mesa</i>). "
             "<b>Está / Están</b> + el, la, los, las (<i>la mesa está a la izquierda</i>)."),
 ("h", "3. Decir qué hacen (ahora)"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Está / Están + gerundio (-ando, -iendo)", "La camarera está sirviendo un café. Los niños están comiendo."],
   ["Va a + infinitivo", "El hombre va a pagar con tarjeta."],
   ["Mientras, … / Al fondo, …", "Mientras, al fondo, un señor está leyendo el periódico."]]),
 ("h", "4. La relación entre ellos"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Creo que son + una familia / amigos / compañeros…", "Creo que son compañeros de trabajo."],
   ["Seguramente es su… (madre, jefe, nieto…)", "Seguramente el señor mayor es el abuelo de los niños."],
   ["Parece que se conocen / que no se conocen", "Parece que no se conocen: esperan su turno."],
   ["Se llevan bien porque…", "Se llevan muy bien, porque se ríen juntos."]]),
 ("h", "5. Decir cómo están"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Está / Parece + contento, cansado, nervioso…", "El chico parece un poco nervioso."],
   ["Creo que está + adjetivo porque…", "Creo que está cansada porque lleva muchas bolsas."],
   ["Creo que piensa: «…»", "Creo que piensa: «¡Voy a llegar tarde!»."]]),
 ("h", "6. Imaginar (da puntos)"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Creo que / Me parece que…", "Creo que son turistas."],
   ["A lo mejor / Seguramente / Quizás…", "A lo mejor están esperando a un amigo."],
   ["Antes han + participio", "Creo que antes han ido al médico."],
   ["Después van a + infinitivo", "Después van a comer en un restaurante."]]),
 ("h", "Modelo"),
 ("modelo", FOTO_MODELO + " Cada párrafo contesta a una de las seis preguntas.", DESCRIPCION,
  "Unas 230 palabras: unos dos minutos y medio. Contesta a las seis preguntas en orden, con lo que se ve y con lo que imagina."),
 ("consejo", "Consejo de examen", "Si no sabes qué decir de una pregunta, imagina: <i>No sé, pero a lo mejor…</i>. Inventar "
             "es parte de la tarea. Lo malo es quedarse en silencio o hablar de tu vida en vez de describir la foto."),
 ("enlaces", ["M4-2", "R02", "R04"]),
]})

DIALOGO_AMIGO = [
 ("Entrevistadora", "¡Hola! ¿Qué tal? ¿Hacemos algo el domingo?"),
 ("Candidato", "¡Hola, Lucía! Muy bien. Oye, <b>¿qué te parece si</b> hacemos un pícnic en el parque? Va a hacer buen tiempo."),
 ("Entrevistadora", "¡Buena idea! ¿A qué hora?"),
 ("Candidato", "<b>¿Por qué no</b> quedamos a las doce en la puerta del parque? <b>¿Te parece bien?</b>"),
 ("Entrevistadora", "Perfecto. ¿Y qué llevamos?"),
 ("Candidato", "Pues yo <b>puedo</b> hacer una tortilla de patatas y llevar pan. <b>¿Tú puedes</b> llevar fruta y algo de beber?"),
 ("Entrevistadora", "Vale. Oye, ¿y si invitamos a Pablo y a Sara?"),
 ("Candidato", "<b>¡Claro!</b> Así somos cuatro. Entonces llevo también una manta grande."),
 ("Entrevistadora", "Uy, acabo de ver en el móvil que el domingo va a llover."),
 ("Candidato", "<b>¡Vaya, qué pena!</b> Bueno, <b>¿y si</b> comemos en mi casa? Tengo una terraza pequeña, pero con un toldo."),
 ("Entrevistadora", "¡Genial!"),
 ("Candidato", "Pues <b>quedamos a las</b> doce <b>en</b> mi casa. Yo hago la tortilla y tú traes la fruta. ¡<b>Hasta el domingo</b>!"),
]
DIALOGO_SERVICIO = [
 ("Entrevistador", "Buenos días. ¿Qué le pongo?"),
 ("Candidato", "Buenos días. <b>Quería</b> fruta para una comida con amigos. Somos seis. <b>¿Qué me recomienda?</b>"),
 ("Entrevistador", "Pues las fresas están muy buenas ahora. Y las naranjas también."),
 ("Candidato", "<b>Ah, vale.</b> ¿Y <b>cuánto cuestan</b> las fresas?"),
 ("Entrevistador", "Cuatro euros el kilo."),
 ("Candidato", "Mmm, <b>es un poco caro</b>, pero vale. <b>¿Me pone</b> un kilo de fresas y dos kilos de naranjas?"),
 ("Entrevistador", "Aquí tiene. ¿Algo más?"),
 ("Candidato", "Sí, <b>¿tiene</b> sandía?"),
 ("Entrevistador", "Lo siento, hoy no tenemos."),
 ("Candidato", "<b>¡Qué pena!</b> Bueno, no pasa nada. <b>¿Cuánto es</b> todo?"),
 ("Entrevistador", "Son seis euros."),
 ("Candidato", "<b>¿Puedo pagar</b> con tarjeta?"),
 ("Entrevistador", "Sí, claro."),
 ("Candidato", "Perfecto. <b>Muchas gracias. ¡Adiós!</b>"),
]

S.append({"id": "t3", "n": "5", "tab": "t3", "titulo": "Tarea 3. Diálogo en una situación", "bloques": [
 ("p", "Se prepara: unos 2 minutos de los 12. La situación está en la lámina de tu foto, por ejemplo: <i>«Vas a hacer un "
       "pícnic con una amiga. El examinador es tu amiga.»</i> o <i>«Usted está en una frutería y quiere comprar fruta para "
       "una comida. El examinador es el dependiente.»</i> Él hace un papel y tú haces otro. Habláis 3-4 minutos."),
 ("h", "Los dos tipos de diálogo"),
 ("tabla", ["Tipo", "Con quién", "Qué haces"], [
   ["<b>Planificar</b> (el más frecuente en las láminas oficiales)", "Un amigo, un hermano, un compañero de piso → <b>tú</b>", "Proponer, preguntar su opinión, aceptar, decir que no y buscar otra solución, quedar."],
   ["<b>Servicio</b>", "El dependiente, el camarero, el recepcionista… → <b>usted</b>", "Pedir, preguntar precio y horario, decidir, quejarse con educación, pagar."]]),
 ("consejo", "¿Tú o usted? Te lo dice la lámina", "No lo tienes que adivinar. <i>«El examinador es tu amigo / tu hermano / tu "
             "compañero de piso»</i> → <b>tú</b> (<i>¿Puedes…? ¿Tienes…?</i>). <i>«El examinador es el dependiente / el camarero / "
             "el recepcionista»</i> → <b>usted</b> (<i>¿Me puede ayudar? ¿Tiene…?</i>). Y del saludo a la despedida, siempre el "
             "mismo. (Usted = the polite form of “you”.)"),
 ("h", "La conversación en cinco pasos"),
 ("ol", ["<b>Saludar.</b> <i>¡Hola, Marta! / Buenos días.</i>",
         "<b>Proponer o decir qué quieres.</b> <i>¿Qué te parece si…? / Quería…</i>",
         "<b>Preguntar</b> lo que necesitas saber: el día, la hora, el precio, el horario…",
         "<b>Decidir:</b> aceptar, o decir que no y buscar otra solución (aquí llega el pequeño problema).",
         "<b>Quedar o pagar, y despedirse.</b> <i>Entonces, quedamos el sábado a las ocho. ¡Hasta luego! / Muchas gracias. Adiós.</i>"]),
 ("h", "Con un amigo: proponer y quedar (tú)"),
 ("tabla", ["Para…", "Frase", "Ejemplo"], [
   ["proponer", "¿Qué te parece si…? / ¿Por qué no…? / Podemos…", "¿Qué te parece si hacemos una paella?"],
   ["preguntar su opinión", "¿Tú qué prefieres? / ¿Te parece bien?", "Yo prefiero el sábado. ¿Te parece bien?"],
   ["aceptar", "¡Vale! / ¡Buena idea! / Me parece genial.", "¡Buena idea! Así vamos todos juntos."],
   ["decir que no, con una razón", "Es que… / No puedo porque…", "Es que el sábado trabajo."],
   ["buscar otra solución", "¿Y si…? / Entonces, mejor…", "¿Y si quedamos el domingo?"],
   ["quedar", "¿A qué hora quedamos? / ¿Dónde quedamos? / Quedamos a las… en…", "Quedamos a las siete en la puerta del cine."]]),
 ("h", "En una tienda o un servicio: pedir (usted)"),
 ("tabla", ["Frase", "Ejemplo"], [
   ["Quería / Quiero + nombre o infinitivo", "Quería un kilo de tomates. Quiero reservar una mesa."],
   ["Necesito…", "Necesito un billete para Valencia."],
   ["¿Me pone / Me da…?", "¿Me pone dos cafés, por favor?"],
   ["¿Puedo + infinitivo?", "¿Puedo probarme esta chaqueta?"]]),
 ("h", "Preguntar"),
 ("tabla", ["Para preguntar…", "Frase"], [
   ["el precio", "¿Cuánto cuesta / cuestan? ¿Cuánto es?"],
   ["la hora", "¿A qué hora sale / abre / cierra…?"],
   ["si hay algo", "¿Tiene…? ¿Hay…?"],
   ["la talla, el color, el tamaño", "¿Lo tiene en otra talla / en azul / más grande?"],
   ["el lugar", "¿Dónde está…? ¿Está lejos?"],
   ["cómo pagar", "¿Puedo pagar con tarjeta?"],
   ["pedir ayuda", "¿Me puede ayudar? ¿Me puede decir…? (con un amigo: ¿Me ayudas?)"]]),
 ("h", "Decidir"),
 ("tabla", ["Para…", "Frase"], [
   ["aceptar", "Vale, perfecto. / Muy bien, me lo llevo. / Sí, de acuerdo."],
   ["rechazar con educación", "Es un poco caro. / No, gracias. Prefiero… / Lo voy a pensar."],
   ["pedir otra opción", "¿Tiene algo más barato? / ¿Hay otro tren más tarde?"],
   ["quejarse con educación", "Perdone, pero esto no funciona. / Perdone, pero he pedido…"]]),
 ("h", "Reaccionar (el examinador quiere ver que escuchas)"),
 ("tabla", ["Para…", "Frase"], [
   ["decir que entiendes", "Ah, vale. / Entiendo. / De acuerdo."],
   ["mostrar sorpresa", "¿De verdad? / ¿Ah, sí? / ¡Qué caro!"],
   ["mostrar alegría", "¡Qué bien! / ¡Genial! / ¡Perfecto!"],
   ["mostrar pena", "¡Qué pena! / Vaya… / ¡Qué lástima!"]]),
 ("h", "Modelo 1: planificar con una amiga (tú)"),
 ("dialogo", "Lámina: <i>Vas a hacer un pícnic el domingo con una amiga. Habla con ella y decidid dónde y a qué hora "
             "quedáis, qué lleva cada uno y a quién invitáis. La examinadora es tu amiga.</i> El pequeño problema: el "
             "domingo va a llover.", DIALOGO_AMIGO),
 ("h", "Modelo 2: en una tienda (usted)"),
 ("dialogo", "Lámina: <i>Usted está en una frutería. Quiere comprar fruta para una comida con amigos. El examinador es el "
             "dependiente.</i> El pequeño problema: no tienen sandía.", DIALOGO_SERVICIO),
 ("consejo", "Consejo de examen", "No contestes solo sí o no. Responde, añade un detalle y, si puedes, haz una pregunta: "
             "<i>Sí, quería fresas. ¿Son de aquí?</i> Así la conversación sigue y tú demuestras más."),
 ("enlaces", ["M4-3", "R07", "R05"]),
]})

S.append({"id": "super", "n": "6", "tab": "bloqueo", "titulo": "Recursos de supervivencia", "bloques": [
 ("p", "Quedarse en blanco es normal. Lo importante es saber qué decir para seguir. Estas frases son tu «plan B»."),
 ("tabla", ["Situación", "Qué decir"], [
   ["Necesitas pensar", "Pues… / A ver… / Bueno… / Un momento, por favor…"],
   ["No entiendes", "¿Perdone? / ¿Puede repetir, por favor? / ¿Puede hablar más despacio, por favor? (con un amigo: ¿Perdona? ¿Puedes repetir?)"],
   ["No entiendes una palabra", "¿Qué significa «…»?"],
   ["No sabes una palabra", "No sé cómo se dice, pero es una cosa para… / Es un sitio donde… / Es como un… pero más pequeño."],
   ["Te equivocas", "Perdón, quiero decir… / No, no, perdón…"],
   ["Te pierdes", "Bueno, como decía… / Bueno, ¿qué más? Ah, sí…"],
   ["No sabes qué decir", "No sé, pero creo que… / Es difícil, pero a lo mejor…"]]),
 ("consejo", "Consejo de examen", "Explicar una palabra con otras palabras (<i>es una cosa para cortar el pan</i>) no es un "
             "error: es una estrategia de buen nivel y puntúa a favor. Preguntar <i>¿Puede repetir?</i> también es normal en el examen."),
 ("enlaces", ["M4-4"]),
]})

S.append({"id": "errores", "n": "7", "tab": "bloqueo", "titulo": "Diez errores que bajan la nota", "bloques": [
 ("p", "Son los más frecuentes en los simulacros. Lee esta página antes de cada práctica."),
 ("tabla", ["Error frecuente", "Forma correcta", "Por qué"], [
   ["Me gusta los perros.", "Me gustan los perros.", "Nombre en plural → gustan."],
   ["Yo gusto la playa.", "Me gusta la playa.", "Con gustar se dice me, te, le…"],
   ["Ayer he ido al cine.", "Ayer fui al cine.", "Ayer → indefinido."],
   ["Hay la mesa a la izquierda.", "La mesa está a la izquierda. / Hay una mesa a la izquierda.", "Hay + un/una; está + el/la."],
   ["Es en la cocina.", "Está en la cocina.", "Dónde está algo → estar."],
   ["Está profesora.", "Es profesora.", "Profesión → ser."],
   ["…y es cansada.", "…y está cansada.", "Cómo se siente → estar."],
   ["Una casa bonito. Los niños pequeñas.", "Una casa bonita. Los niños pequeños.", "El adjetivo concuerda con el nombre."],
   ["Tengo 30 años que vivo aquí.", "Vivo aquí desde hace 30 años.", "Tiempo hasta ahora → desde hace."],
   ["Hola, Pedro… ¿Puede usted venir? (a un amigo)", "Hola, Pedro… ¿Puedes venir?", "Con un amigo, tú del principio al final."]]),
 ("h", "Errores de estrategia"),
 ("ul", ["Recitar un texto memorizado. Se nota mucho y te pierdes si el examinador dice algo.",
         "No hablar de todas las pautas de la lámina en la tarea 1.",
         "En la foto, hacer solo una lista (<i>hay una mesa, hay una silla, hay un perro…</i>) o hablar de tu vida en vez de describir. Contesta a las seis preguntas e imagina un poco.",
         "Repetir siempre la misma frase (<i>me gusta… me gusta… me gusta…</i>). Cambia: <i>me encanta, prefiero, lo que más me gusta es…</i>",
         "Contestar con una palabra en la tarea 3. Responde, da un detalle y haz una pregunta.",
         "Pedir algo en una tienda sin educación (<i>Quiero un café.</i>, seco). Mejor: <i>¿Me pone un café, por favor?</i>"]),
 ("enlaces", ["R01", "R02", "R04", "R07"]),
]})

# ---------------------------------------------------------------- PRACTICA
# tipo "elige": cada item con frase (con ____), opciones, buena (o lista de buenas) y porque
# tipo "huecos": dialogo con [n] y opciones por hueco
# tipo "pregunta": frases -> numero de pregunta de la foto (1-6)
EJ = []
EJ.append({"id": "e1", "titulo": "¿He ido o fui?", "inst": "Elige el pretérito perfecto o el indefinido.", "tipo": "elige", "items": [
 {"f": "Este fin de semana ____ a la playa con mis amigos. (ir, yo)", "o": ["he ido", "fui"], "ok": "he ido", "why": "Este fin de semana: el tiempo todavía no ha terminado → perfecto."},
 {"f": "El año pasado ____ a estudiar español. (empezar, yo)", "o": ["empecé", "he empezado"], "ok": "empecé", "why": "El año pasado: tiempo terminado → indefinido."},
 {"f": "Hoy ____ en un restaurante italiano. (comer, nosotros)", "o": ["hemos comido", "comimos"], "ok": "hemos comido", "why": "Hoy → perfecto."},
 {"f": "En 2018 mi hermana ____ un bebé. (tener)", "o": ["tuvo", "ha tenido"], "ok": "tuvo", "why": "En 2018: una fecha terminada → indefinido."},
 {"f": "Ayer ____ tarde a clase. (llegar, yo)", "o": ["llegué", "he llegado"], "ok": "llegué", "why": "Ayer → indefinido, nunca perfecto."},
 {"f": "¿____ alguna vez en México? (estar, tú)", "o": ["Has estado", "Estuviste"], "ok": "Has estado", "why": "Alguna vez: toda tu vida hasta ahora → perfecto (en España)."},
 {"f": "La semana pasada mis padres ____ Madrid. (visitar)", "o": ["visitaron", "han visitado"], "ok": "visitaron", "why": "La semana pasada → indefinido."},
 {"f": "Esta mañana ____ a las siete. (levantarse, yo)", "o": ["me he levantado", "me levanté"], "ok": "me he levantado", "why": "Esta mañana, si todavía es hoy → perfecto."}]})
EJ.append({"id": "e2", "titulo": "¿Hay o está / están?", "inst": "Elige la forma correcta.", "tipo": "elige", "items": [
 {"f": "En la foto ____ un hombre con gafas.", "o": ["hay", "está", "están"], "ok": "hay", "why": "Presentas algo nuevo (un hombre) → hay."},
 {"f": "El hombre ____ al lado de la puerta.", "o": ["hay", "está", "están"], "ok": "está", "why": "El hombre ya lo conocemos: dices dónde → está."},
 {"f": "Al fondo ____ muchos libros.", "o": ["hay", "está", "están"], "ok": "hay", "why": "Muchos + nombre → hay (hay no cambia en plural)."},
 {"f": "Los libros ____ en una estantería.", "o": ["hay", "está", "están"], "ok": "están", "why": "Los libros (ya conocidos, plural) → están."},
 {"f": "Encima de la mesa ____ un ordenador.", "o": ["hay", "está", "están"], "ok": "hay", "why": "Un ordenador: algo nuevo → hay."},
 {"f": "Las llaves ____ debajo de la silla.", "o": ["hay", "está", "están"], "ok": "están", "why": "Las llaves (plural, ya conocidas) → están."}]})
EJ.append({"id": "e3", "titulo": "Gustos", "inst": "Elige una forma correcta. Después di la frase sobre ti.", "tipo": "elige", "items": [
 {"f": "____ las películas de risa.", "o": ["Me gusta", "Me gustan", "Prefiero"], "ok": ["Me gustan"], "why": "Las películas: plural → me gustan (o me encantan)."},
 {"f": "____ el café sin azúcar.", "o": ["Me gusta", "Me gustan", "Me encantan"], "ok": ["Me gusta"], "why": "El café: singular → me gusta (o prefiero)."},
 {"f": "____ viajar en tren porque puedo leer.", "o": ["Me gusta", "Me gustan", "Me encantan"], "ok": ["Me gusta"], "why": "Gustar + infinitivo → siempre en singular: me gusta (o me encanta, prefiero)."},
 {"f": "No ____ los lunes.", "o": ["me gusta", "me gustan", "prefiero"], "ok": ["me gustan"], "why": "Los lunes: plural → me gustan."},
 {"f": "____ el verano al invierno.", "o": ["Prefiero", "Me gusta", "Me gustan"], "ok": ["Prefiero"], "why": "Prefiero A a B: comparas dos cosas."},
 {"f": "____ cocinar para mis amigos.", "o": ["Me encanta", "Me encantan", "Me gustan"], "ok": ["Me encanta"], "why": "Encantar + infinitivo → singular: me encanta (o me gusta)."}]})
EJ.append({"id": "e4", "titulo": "De la lista a la descripción", "inst": "Imagina que describes una foto. Escribe qué hace la persona ahora (estar + gerundio).", "tipo": "escribe", "items": [
 {"f": "Una mujer ____ el periódico. (leer)", "ok": ["está leyendo"]},
 {"f": "Dos niños ____ con una pelota. (jugar)", "ok": ["están jugando"]},
 {"f": "Un camarero ____ una cerveza. (servir)", "ok": ["está sirviendo"]},
 {"f": "Un chico ____ en el móvil. (escribir)", "ok": ["está escribiendo"]},
 {"f": "Una pareja ____ un mapa. (mirar)", "ok": ["está mirando"]},
 {"f": "Un señor ____ el autobús. (esperar)", "ok": ["está esperando"]}]})
EJ.append({"id": "e5", "titulo": "Tarea 3 en la estación (usted)", "inst": "Situación: Usted está en la estación y quiere comprar un billete de tren para Valencia. El examinador es el empleado. Completa el diálogo.", "tipo": "huecos", "lineas": [
 ("Empleado", "Buenas tardes. ¿Qué desea?"),
 ("Tú", "Buenas tardes. [1] un billete para Valencia, por favor."),
 ("Empleado", "¿Para hoy?"),
 ("Tú", "Sí. ¿[2] sale el próximo tren?"),
 ("Empleado", "A las seis y media."),
 ("Tú", "Ah, [3]. ¿Y [4] cuesta?"),
 ("Empleado", "Treinta y cinco euros."),
 ("Tú", "¡[5]! ¿Hay algo más barato?"),
 ("Empleado", "Sí, el regional. Sale a las siete y cuesta veinte euros."),
 ("Tú", "Vale, [6]. ¿[7] pagar con tarjeta?"),
 ("Empleado", "Sí, claro. Aquí tiene su billete."),
 ("Tú", "[8]. ¡Adiós!")], "huecos": [
 {"o": ["Quería", "Puedo", "Me gusta"], "ok": "Quería", "why": "Para pedir con educación: quería (o necesito)."},
 {"o": ["A qué hora", "Cuánto", "Dónde"], "ok": "A qué hora", "why": "El empleado contesta una hora."},
 {"o": ["vale", "adiós", "perdón"], "ok": "vale", "why": "Dices que entiendes: ah, vale."},
 {"o": ["cuánto", "qué", "cuál"], "ok": "cuánto", "why": "El precio: ¿cuánto cuesta?"},
 {"o": ["Qué caro", "Qué bien", "Qué bonito"], "ok": "Qué caro", "why": "Después preguntas por algo más barato: ¡qué caro!"},
 {"o": ["perfecto", "lo siento", "qué pena"], "ok": "perfecto", "why": "Aceptas: vale, perfecto (o de acuerdo)."},
 {"o": ["Puedo", "Quiero", "Tengo"], "ok": "Puedo", "why": "Para preguntar si está permitido: ¿puedo pagar...?"},
 {"o": ["Muchas gracias", "De nada", "Perdone"], "ok": "Muchas gracias", "why": "Te dan el billete: das las gracias y te despides."}]})
EJ.append({"id": "e6", "titulo": "Tarea 3 con un amigo (tú)", "inst": "Situación: Tu amigo y tú queréis ir al cine el viernes. El examinador es tu amigo. Completa el diálogo.", "tipo": "huecos", "lineas": [
 ("Amigo", "¡Hola! ¿Qué hacemos el viernes?"),
 ("Tú", "¿Qué te [1] si vamos al cine?"),
 ("Amigo", "Vale. ¿Qué película quieres ver?"),
 ("Tú", "Una comedia. ¿Tú qué [2]?"),
 ("Amigo", "A mí también me gustan las comedias. ¿A qué hora vamos?"),
 ("Tú", "¿Por [3] no vamos a la sesión de las ocho?"),
 ("Amigo", "Es que salgo de trabajar a las ocho."),
 ("Tú", "Ah, vale. ¿Y [4] vamos a la de las diez?"),
 ("Amigo", "¡Perfecto!"),
 ("Tú", "¿Dónde [5]?"),
 ("Amigo", "En la puerta del cine, ¿no?"),
 ("Tú", "¡[6] idea! Entonces, [7] a las diez menos cuarto en la puerta. ¡Hasta el [8]!")], "huecos": [
 {"o": ["parece", "gusta", "quieres"], "ok": "parece", "why": "Para proponer: ¿qué te parece si...?"},
 {"o": ["prefieres", "prefiere", "prefiero"], "ok": "prefieres", "why": "Es tu amigo: tú prefieres (prefiere es de usted)."},
 {"o": ["qué", "que", "cuál"], "ok": "qué", "why": "¿Por qué no...? sirve para proponer; en la pregunta, qué con tilde."},
 {"o": ["si", "sí", "cuando"], "ok": "si", "why": "Otra solución: ¿y si...? (si sin tilde)."},
 {"o": ["quedamos", "estamos", "vivimos"], "ok": "quedamos", "why": "Para decidir el sitio del encuentro: ¿dónde quedamos?"},
 {"o": ["Buena", "Bien", "Bueno"], "ok": "Buena", "why": "Idea es femenino: ¡buena idea!"},
 {"o": ["quedamos", "quedan", "quedáis"], "ok": "quedamos", "why": "Tú y tu amigo: nosotros quedamos."},
 {"o": ["viernes", "lunes", "sábado"], "ok": "viernes", "why": "El plan es para el viernes."}]})
EJ.append({"id": "e7", "titulo": "¿A qué pregunta de la foto contesta?", "inst": "Cada frase contesta a una de las seis preguntas de la lámina. Elige el número.", "tipo": "pregunta", "items": [
 {"f": "Tiene unos cuarenta años y el pelo rizado.", "ok": 1},
 {"f": "Lleva una chaqueta vaquera y unas zapatillas blancas.", "ok": 1},
 {"f": "Están en la sala de espera de un hospital.", "ok": 2},
 {"f": "Al fondo hay una máquina de café.", "ok": 2},
 {"f": "El padre está leyendo un cuento a su hija.", "ok": 3},
 {"f": "Creo que son abuelo y nieto, porque se parecen mucho.", "ok": 4},
 {"f": "Parece nerviosa, porque mira el reloj todo el rato.", "ok": 5},
 {"f": "Seguramente han comido juntos en un restaurante.", "ok": 6},
 {"f": "Después van a coger un taxi para volver a casa.", "ok": 6}]})

# Ejercicio 8: el esquema de la tarea 1 (sin solucion unica)
TEMAS_ESQUEMA = [
 {"titulo": "Mi casa", "pautas": ["dónde vives y desde cuándo;", "cómo es tu casa;", "lo que más te gusta y lo que no;", "cómo era la casa donde vivías de pequeño/a;", "cómo va a ser tu casa ideal en el futuro."]},
 {"titulo": "Mi trabajo o mis estudios", "pautas": ["qué haces y dónde;", "cómo es un día normal;", "lo que te gusta y lo que no;", "cuál fue tu primer trabajo o cómo era tu escuela;", "qué planes tienes."]},
 {"titulo": "La comida", "pautas": ["qué comes normalmente;", "tu plato favorito y por qué;", "una comida especial que recuerdas;", "qué comías de pequeño/a;", "qué plato vas a aprender a cocinar."]},
]
# Ejercicio 9: autoevaluacion (tras grabarse)
AUTOEVAL = [
 "He empezado diciendo de qué voy a hablar.",
 "He hablado de las cinco pautas de la lámina, en orden.",
 "He usado presente, pasado, «antes» (imperfecto) y futuro (voy a…).",
 "He dado mi opinión o mis gustos con frases distintas.",
 "He usado al menos tres conectores (primero, después, pero, porque, además…).",
 "He terminado con una frase final.",
 "He hablado unos 2-3 minutos.",
 "No he leído ni he recitado de memoria.",
]

# ---------------------------------------------------------------- TARJETA DE BOLSILLO
TARJETA = [
 ("Tarea 1 · Tema", [
   ("3 pasos", "empezar → las 5 pautas en orden → terminar"),
   ("Empezar", "Voy a hablar de…"),
   ("Ahora", "Normalmente… · Vivo aquí desde hace…"),
   ("Pasado", "Este año he… · Ayer fui… · De pequeño vivía…"),
   ("Gustos", "Me gusta(n)… · Prefiero… · Lo que más me gusta es…"),
   ("Futuro", "Voy a… · Me gustaría…"),
   ("Terminar", "Para mí, … es importante porque…")]),
 ("Tarea 2 · Foto", [
   ("6 preguntas", "personas y ropa · lugar y objetos · qué hacen · relación · qué sienten · antes y después"),
   ("Personas", "Es… · Tiene… años · Lleva…"),
   ("Lugar", "En la foto hay… · A la izquierda… · Al fondo…"),
   ("Acciones", "Está + -ando / -iendo"),
   ("Relación", "Creo que son… · Seguramente es su…"),
   ("Sentimientos", "Parece contento… porque…"),
   ("Antes y después", "Antes han… · Después van a…")]),
 ("Tarea 3 · Diálogo", [
   ("¿Tú o usted?", "Te lo dice la lámina. Siempre el mismo, del saludo a la despedida."),
   ("Con un amigo", "¿Qué te parece si…? · Es que… · ¿Y si…? · Quedamos a las… en…"),
   ("En una tienda", "Quería… · ¿Me pone…? · ¿Cuánto cuesta? · ¿Tiene algo más barato?"),
   ("Decidir", "Vale, me lo llevo. · Es un poco caro."),
   ("Reaccionar", "¡Qué bien! · ¡Qué pena! · ¿De verdad?"),
   ("Pequeño problema", "No pasa nada. ¿Y si…? / ¿Tiene otro…?")]),
]
TARJETA_PIE = [("Preparación (12 min)", "1 elegir · 4 tema · 4 foto · 2 diálogo · 1 repasar"),
               ("Conectores", "primero · después · luego · además · también · pero · porque · por eso · al final · en resumen"),
               ("Supervivencia", "Pues… · A ver… · ¿Puede repetir, por favor? · Es una cosa para… · Perdón, quiero decir…")]
TARJETA_ANTES = ("Respira, sonríe y empieza con tu primera frase. No buscas la perfección: buscas un 2, es decir, hablar "
                 "claro, con orden y con frases sencillas. ¡Tú puedes!")

# ---------------------------------------------------------------- OPINION (ejecutable)
OPINION = [
 {"id": "o1", "q": "¿Qué tarea te parece más difícil ahora?", "chips": ["Tarea 1 (el tema)", "Tarea 2 (la foto)", "Tarea 3 (el diálogo)"]},
 {"id": "o2", "q": "¿Qué parte del dosier te ha servido más?", "chips": ["Las frases", "Los modelos", "La práctica", "La tarjeta de bolsillo"]},
 {"id": "o3", "q": "¿Vas a llevar la tarjeta de bolsillo al examen (para leerla antes)?", "chips": ["Sí", "No sé", "No"]},
 {"id": "o4", "q": "¿Qué falta o qué no has entendido?", "texto": True},
 {"id": "o5", "q": "Ahora, ¿cuánto control sientes en la prueba oral? (1 = nada, 10 = mucho)", "escala": True},
]
