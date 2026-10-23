# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R01: LOS PASADOS Y LAS PREGUNTAS (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R01_pasados.py
#
# MARCAS
#   En textos modelo:  [f:fui] indefinido · [i:era] imperfecto · [v:he ido] perfecto
#   En huecos:         [[correcta|distractor|distractor#motivo]]  (la primera es la buena;
#                      el ejecutable baraja las opciones)
# Espanol de Espana: hoy, esta semana, este ano, alguna vez, ya... -> perfecto.

# ------------------------------------------------------------------ MOTIVOS
# clave: (tiempo, explicacion corta). El tiempo decide el color.
MOTIVOS = {
    "fin":    ("indef", "Acción completa: la ves desde fuera, con su final."),
    "serie":  ("indef", "Una acción detrás de otra: la historia avanza."),
    "val":    ("indef", "Valoras algo que ya terminó: fue, lo pasé..."),
    "cuando": ("indef", "Momento cerrado: ayer, en 2019, hace dos años, el sábado..."),
    "proc":   ("imperf", "Proceso: estás dentro de la acción y no ves el final."),
    "dec":    ("imperf", "Decorado: cómo era, qué había, qué tiempo hacía."),
    "cost":   ("imperf", "Costumbre de antes: lo que hacías normalmente."),
    "plan":   ("imperf", "Plan que no se hizo: iba a + infinitivo."),
    "ven":    ("perf", "Ventana de ahora: hoy, este año, alguna vez, nunca, ya..."),
}
TIEMPOS = {
    "indef":  ("Indefinido", "fui, comí, llegó"),
    "imperf": ("Imperfecto", "iba, comía, llegaba"),
    "perf":   ("Perfecto", "he ido, he comido, ha llegado"),
}

# ------------------------------------------------------------------ 1. LA IDEA
# Pares minimos (misma idea que la pildora de 2ST, con ejemplos nuevos).
# a = imperfecto (proceso), b = indefinido (fin). accion = la barra; evento = la estrella.
PARES = [
    {"accion": "cruzar la calle", "evento": "el semáforo se pone rojo",
     "a": "Cuando [i:cruzaba] la calle, el semáforo se puso rojo.",
     "b": "Cuando [f:crucé] la calle, el semáforo se puso rojo.",
     "ra": "Estás <b>en medio del paso de cebra</b>. Todavía estás cruzando... ¡y los coches esperan para salir!",
     "rb": "Ya estás <b>en la otra acera</b>. Primero cruzas, la acción termina, y después el semáforo cambia."},
    {"accion": "tender la ropa", "evento": "empieza a llover",
     "a": "Cuando [i:tendía] la ropa, empezó a llover.",
     "b": "Cuando [f:tendí] la ropa, empezó a llover.",
     "ra": "Todavía estás <b>tendiendo</b>, con una camiseta en la mano. Recoges todo deprisa.",
     "rb": "La ropa <b>ya está tendida</b>. Después empieza la lluvia... y se moja toda."},
    {"accion": "aparcar el coche", "evento": "pasa un perro corriendo",
     "a": "Cuando [i:aparcaba] el coche, pasó un perro corriendo.",
     "b": "Cuando [f:aparqué] el coche, pasó un perro corriendo.",
     "ra": "Todavía <b>estás maniobrando</b>: el perro pasa por detrás y frenas.",
     "rb": "<b>El coche ya está aparcado</b>. Bajas y ves pasar al perro."},
    {"accion": "salir del trabajo", "evento": "me llama mi madre",
     "a": "Cuando [i:salía] del trabajo, me llamó mi madre.",
     "b": "Cuando [f:salí] del trabajo, me llamó mi madre.",
     "ra": "Estás <b>en la puerta</b>, saliendo, con el abrigo a medias.",
     "rb": "<b>Ya estás en la calle</b>. Has salido y después suena el teléfono."},
    {"accion": "hablar por teléfono", "evento": "",
     "a": "Lucía [i:hablaba] por teléfono con su hermano.",
     "b": "Lucía [f:habló] por teléfono con su hermano.",
     "ra": "Ves la escena <b>por dentro</b>, como una foto: Lucía con el móvil en la oreja, riéndose. Esperas que pase algo más.",
     "rb": "Ves <b>la llamada entera</b>: habló, colgó y se acabó. La historia puede seguir: «...y después salió a correr»."},
]

# Era / fue: la descripcion frente a la valoracion de algo terminado
ERA_FUE = [
    ("Mi vecino [i:era] muy amable.", "Cómo era él: su carácter, una descripción (el decorado de tu historia)."),
    ("Ayer mi vecino [f:fue] muy amable: me [f:subió] las bolsas.", "Lo que pasó en un momento concreto que ya terminó."),
    ("El hotel [i:era] pequeño y [i:tenía] un jardín.", "Describes el hotel: cómo era."),
    ("El viaje [f:fue] fantástico. Lo [f:pasamos] muy bien.", "Valoras el viaje entero, ya terminado. Así se terminan muchos textos del examen."),
]

# ------------------------------------------------------------------ 2. CONTAR UNA HISTORIA
# Cada trozo: tipo A (accion: la historia avanza), D (decorado), V (ventana de ahora)
HISTORIA = [
    ("A", "El domingo pasado [f:hice] una ruta en bici con mi hermana por la costa."),
    ("D", "[i:Hacía] un poco de fresco y casi no [i:había] coches."),
    ("D", "Mientras [i:subíamos] una cuesta muy larga,"),
    ("A", "mi rueda [f:se pinchó]."),
    ("D", "No [i:teníamos] herramientas y el pueblo más cercano [i:estaba] lejos."),
    ("A", "Al final, un señor muy amable [f:paró] su furgoneta y nos [f:llevó] al pueblo."),
    ("A", "Allí [f:arreglamos] la rueda y [f:comimos] en un bar del puerto."),
    ("A", "[f:Volvimos] a casa muy tarde, pero [f:fue] un día genial."),
    ("V", "Este año [v:he hecho] muchas rutas, pero esa no la voy a olvidar."),
]

MARCADORES = {
    "indef":  ["ayer", "anoche", "el sábado (pasado)", "la semana pasada", "el año pasado", "en 2019",
               "hace dos años", "un día", "de repente", "después", "al final"],
    "imperf": ["antes", "de niño / de pequeña", "cuando era joven", "siempre", "todos los veranos",
               "normalmente", "a menudo", "mientras"],
    "perf":   ["hoy", "esta mañana", "esta semana", "este año", "últimamente", "alguna vez",
               "nunca", "ya", "todavía no"],
}

# ------------------------------------------------------------------ 3. LAS PREGUNTAS
# Tabla: la pregunta te da el tiempo. (pregunta, respuesta, tiempo)
PREG_TABLA = [
    ("¿Qué [v:has hecho] hoy?", "[v:He trabajado] y [v:he ido] al gimnasio.", "perf"),
    ("¿Alguna vez [v:has estado] en Sevilla?", "Sí, [v:he estado] dos veces. / No, nunca [v:he estado].", "perf"),
    ("¿Qué [f:hiciste] el fin de semana pasado?", "[f:Fui] a la montaña con unos amigos.", "indef"),
    ("¿Cuándo [f:empezaste] a estudiar español?", "[f:Empecé] hace dos años.", "indef"),
    ("¿Qué tal el viaje? ¿Lo [f:pasaste] bien?", "Sí, [f:fue] genial. Lo [f:pasamos] muy bien.", "indef"),
    ("¿Cómo [i:era] tu casa cuando [i:eras] pequeño?", "[i:Era] grande y [i:tenía] un jardín.", "imperf"),
    ("¿Qué [i:hacías] los veranos de niña?", "[i:Iba] al pueblo de mis abuelos.", "imperf"),
    ("¿Qué [i:estabas] haciendo cuando te [f:llamé]?", "[i:Estaba] en la ducha.", "imperf"),
]

# El salto: de la ventana abierta a una fecha cerrada
SALTO = [
    ("¿Alguna vez [v:has estado] en Sevilla?", "Sí, [v:he estado] una vez.", "[f:Estuve] en 2022, con mi familia."),
    ("¿[v:Has ido] al teatro este año?", "Sí, [v:he ido] una vez.", "[f:Fui] en marzo, con mi madre."),
    ("¿[v:Has visto] la película de la que te hablé?", "Sí, ya la [v:he visto].", "La [f:vi] el domingo con mi hermano."),
]

# De la pauta (escritura o lamina de la oral) a la pregunta directa
PAUTA_PREGUNTA = [
    ("Pregúntale qué tal fue su viaje.", "¿Qué tal tu viaje? ¿Lo [f:pasaste] bien?"),
    ("Pregúntale si ha visto la película que le recomendaste.", "¿[v:Has visto] ya la película que te recomendé?"),
    ("Pregúntale qué hizo el fin de semana.", "¿Qué [f:hiciste] el fin de semana?"),
    ("Pregúntale cómo era su barrio de niño.", "¿Cómo [i:era] tu barrio cuando [i:eras] niño?"),
    ("Pregunte si alguien ha encontrado su mochila. (usted)", "¿[v:Ha encontrado] alguien una mochila azul?"),
]

# ------------------------------------------------------------------ EJERCICIOS DE OPCION MULTIPLE
# Cada item: q (enunciado), o (opciones; LA PRIMERA ES LA BUENA), why, y opcional
# "fijo": True para no barajar (Bien / Mal).

# P1 Que tiempo pide la pregunta (pregunta -> respuesta que va con ella)
P_TIEMPO = [
    {"q": "¿Has estado alguna vez en Granada?",
     "o": ["Sí, he estado una vez, con mi familia.", "Sí, estaba una vez, con mi familia.", "Sí, iba una vez, con mi familia."],
     "why": "La pregunta usa el perfecto (<i>has estado</i>) con <i>alguna vez</i>: la ventana está abierta (toda tu vida hasta ahora). Contestas con el mismo tiempo."},
    {"q": "¿Cuándo fuiste a Granada?",
     "o": ["Fui en 2022.", "He ido en 2022.", "Iba en 2022."],
     "why": "<i>¿Cuándo...?</i> pide un momento cerrado. Con una fecha (<i>en 2022</i>) la ventana se cierra: indefinido."},
    {"q": "¿Qué hacías de niño los domingos?",
     "o": ["Comía en casa de mis abuelos.", "Comí en casa de mis abuelos.", "He comido en casa de mis abuelos."],
     "why": "<i>De niño</i> y <i>los domingos</i>: es una costumbre de antes. La pregunta va en imperfecto y la respuesta también."},
    {"q": "¿Qué has hecho esta mañana?",
     "o": ["He ido al mercado.", "Iba al mercado.", "Voy a ir al mercado."],
     "why": "<i>Esta mañana</i> está dentro de la ventana de ahora (hoy). En España: perfecto, como la pregunta."},
    {"q": "¿Qué tal el viaje del verano pasado?",
     "o": ["Genial, lo pasamos muy bien.", "Genial, lo pasábamos muy bien.", "Genial, lo hemos pasado muy bien."],
     "why": "Valoras algo terminado y cerrado (<i>el verano pasado</i>): indefinido. <i>Lo pasamos muy bien</i> es una frase de oro para el examen."},
    {"q": "¿Cómo era tu casa cuando eras pequeño?",
     "o": ["Era grande y tenía un jardín.", "Fue grande y tuvo un jardín.", "Ha sido grande y ha tenido un jardín."],
     "why": "<i>¿Cómo era...?</i> pide una descripción: el decorado. Imperfecto."},
    {"q": "¿Qué estabas haciendo cuando te llamé?",
     "o": ["Estaba en la ducha.", "Estuve en la ducha.", "He estado en la ducha."],
     "why": "La llamada te encuentra <b>dentro</b> de otra acción: proceso, imperfecto."},
    {"q": "¿Dónde vivías antes de venir a España?",
     "o": ["Vivía en Cracovia.", "He vivido en Cracovia.", "Viviré en Cracovia."],
     "why": "<i>Antes</i>: describes tu vida de antes. Imperfecto, como la pregunta. El perfecto no va: ya no vives allí."},
    {"q": "¿Qué te pasó el sábado en el partido?",
     "o": ["Me caí y me hice daño en el brazo.", "Me caía y me hacía daño en el brazo.", "Me he caído y me he hecho daño en el brazo."],
     "why": "Un hecho concreto, completo y en un día cerrado (<i>el sábado</i>): indefinido."},
    {"q": "¿Ya has terminado el libro?",
     "o": ["No, todavía no lo he terminado.", "No, todavía no lo terminaba.", "No, ya no lo he terminado."],
     "why": "<i>Ya</i> y <i>todavía no</i> miran hasta ahora: perfecto. Ojo: <i>ya no</i> significa otra cosa (antes sí, ahora no)."},
    {"q": "¿Cuántos años tenías cuando aprendiste a nadar?",
     "o": ["Tenía siete años.", "Tuve siete años.", "He tenido siete años."],
     "why": "La edad es el decorado de ese momento: imperfecto (<i>tenía</i>). La acción que pasa (<i>aprendiste</i>) va en indefinido."},
    {"q": "¿Cómo conociste a tu mejor amiga?",
     "o": ["La conocí en la universidad.", "La conocía en la universidad.", "La he conocido en la universidad."],
     "why": "Conocer a alguien pasa en un momento concreto y termina: indefinido."},
]

# P2 Completa la pregunta (preguntas personales para conocerse)
P_COMPLETA = [
    {"q": "¿Alguna vez <b>(perder)</b> ____ el pasaporte?", "o": ["has perdido", "perdías", "pierdes"],
     "why": "<i>Alguna vez</i> = en toda tu vida hasta ahora: ventana abierta, perfecto."},
    {"q": "Cuando eras pequeño, ¿qué <b>(comer)</b> ____ los domingos en casa?", "o": ["comías", "comiste", "has comido"],
     "why": "<i>Cuando eras pequeño</i> y <i>los domingos</i>: costumbre de antes, imperfecto."},
    {"q": "¿Qué <b>(hacer)</b> ____ anoche?", "o": ["hiciste", "hacías", "has hecho"],
     "why": "<i>Anoche</i> está cerrado: indefinido."},
    {"q": "¿Dónde <b>(conocer)</b> ____ a tu pareja?", "o": ["conociste", "conocías", "has conocido"],
     "why": "Un hecho concreto, en un momento, que terminó: indefinido."},
    {"q": "¿A qué <b>(jugar)</b> ____ en el recreo cuando eras pequeña?", "o": ["jugabas", "jugaste", "has jugado"],
     "why": "Costumbre de antes (todos los días, en el recreo): imperfecto."},
    {"q": "¿<b>(Leer)</b> ____ algún libro bueno últimamente?", "o": ["Has leído", "Leías", "Lees"],
     "why": "<i>Últimamente</i> llega hasta hoy: ventana abierta, perfecto."},
    {"q": "¿Qué <b>(cenar)</b> ____ en Nochebuena el año pasado?", "o": ["cenaste", "cenabas", "has cenado"],
     "why": "Una noche concreta, en un año cerrado: indefinido."},
    {"q": "¿Dónde vivías cuando <b>(empezar)</b> ____ a estudiar español?", "o": ["empezaste", "empezabas", "has empezado"],
     "why": "Empezar pasa en un momento: es la acción (indefinido). <i>Vivías</i> es el decorado."},
    {"q": "¿Dónde <b>(vivir)</b> ____ cuando empezaste a estudiar español?", "o": ["vivías", "viviste", "has vivido"],
     "why": "Dónde vivías es el decorado de ese momento: imperfecto."},
    {"q": "¿Qué <b>(estar)</b> ____ haciendo cuando te llamé?", "o": ["estabas", "estuviste", "has estado"],
     "why": "La llamada llega en medio: proceso, imperfecto."},
    {"q": "¿Cuántas veces <b>(viajar)</b> ____ en avión este año?", "o": ["has viajado", "viajabas", "viajas"],
     "why": "<i>Este año</i> todavía no ha terminado: ventana de ahora, perfecto."},
    {"q": "¿Qué tal te <b>(ir)</b> ____ el examen de ayer?", "o": ["fue", "iba", "ha ido"],
     "why": "<i>Ayer</i> y una valoración de algo terminado: indefinido."},
    {"q": "¿Cómo <b>(ser)</b> ____ tu primer día en el trabajo?", "o": ["fue", "ha sido", "eres"],
     "why": "Preguntas por una experiencia completa que ya terminó: <i>¿Cómo fue...?</i>"},
    {"q": "¿Qué tiempo <b>(hacer)</b> ____ cuando llegaste a Madrid?", "o": ["hacía", "hizo", "ha hecho"],
     "why": "El tiempo atmosférico en ese momento es el decorado: imperfecto."},
    {"q": "¿<b>(Dormir)</b> ____ bien anoche?", "o": ["Dormiste", "Dormías", "Has dormido"],
     "why": "<i>Anoche</i>: momento cerrado, indefinido."},
    {"q": "¿Ya <b>(terminar)</b> ____ los deberes de hoy?", "o": ["has terminado", "terminabas", "terminas"],
     "why": "<i>Ya</i> y <i>hoy</i>: perfecto."},
]

# P3 Haz la pregunta (de la pauta o la situacion a la pregunta directa)
P_HAZ = [
    {"q": "<span class='chip'>Escritura · correo a un amigo</span> Pauta: <i>Pregúntale qué tal fue su viaje a Roma.</i>",
     "o": ["¿Qué tal tu viaje a Roma? ¿Lo pasaste bien?", "¿Qué tal su viaje a Roma? ¿Lo pasó bien?", "¿Pregúntale qué tal fue tu viaje a Roma?"],
     "why": "La pauta habla de él (<i>su</i>), pero tú le escribes a él: <i>tu viaje</i>, de tú. Y nunca copies <i>pregúntale</i>: escribe la pregunta directa."},
    {"q": "<span class='chip'>Escritura · correo a un amigo</span> Pauta: <i>Pregúntale si ha visto la película que le recomendaste.</i>",
     "o": ["¿Has visto ya la película que te recomendé?", "¿Veías ya la película que te recomendé?", "¿Ha visto usted la película que le recomendé?"],
     "why": "<i>Ya</i> mira hasta ahora: perfecto (<i>has visto</i>). Es un amigo: de tú."},
    {"q": "<span class='chip'>Escritura · correo de usted</span> Escribes al hotel donde estuviste. Pauta: <i>Pregunte si han encontrado la chaqueta que olvidó en la habitación.</i>",
     "o": ["¿Han encontrado una chaqueta negra en la habitación 204? La olvidé el domingo.",
           "¿Has encontrado mi chaqueta? La olvidé el domingo.",
           "¿Encontraban una chaqueta negra en la habitación 204? La olvidaba el domingo."],
     "why": "Al hotel, de usted (<i>han encontrado</i>, ustedes). Hasta ahora: perfecto. Y <i>el domingo</i> es cerrado: <i>la olvidé</i>."},
    {"q": "<span class='chip'>Oral · tarea 3, con un amigo</span> Organizáis una cena. Quieres saber si tu amigo ya ha llamado al restaurante.",
     "o": ["¿Ya has llamado al restaurante?", "¿Ya llamabas al restaurante?", "¿Ya ha llamado usted al restaurante?"],
     "why": "<i>Ya</i> + hasta ahora: perfecto. Es un amigo: de tú."},
    {"q": "<span class='chip'>Oral · tarea 3, de usted</span> Estás en la oficina de objetos perdidos. Quieres saber si alguien ha traído tu mochila.",
     "o": ["¿Ha traído alguien una mochila azul?", "¿Traía alguien una mochila azul?", "¿Has traído una mochila azul?"],
     "why": "Hasta ahora (hoy, estos días): perfecto. <i>¿Has traído?</i> pregunta si la ha traído el empleado... y además es de tú."},
    {"q": "<span class='chip'>Escritura · correo a un amigo</span> Pauta: <i>Pregúntale cómo era su barrio de niño.</i>",
     "o": ["¿Cómo era tu barrio cuando eras niño?", "¿Cómo fue tu barrio cuando fuiste niño?", "¿Cómo era su barrio cuando era niño?"],
     "why": "Describir el barrio de antes: imperfecto. Y a un amigo, <i>tu</i> y <i>eras</i>."},
    {"q": "<span class='chip'>Escritura · correo a un amigo</span> Pauta: <i>Pregúntale qué hizo el fin de semana.</i>",
     "o": ["¿Qué hiciste el fin de semana?", "¿Qué hacías el fin de semana?", "¿Qué hace el fin de semana?"],
     "why": "Un fin de semana concreto, terminado: indefinido. <i>¿Qué hacías los fines de semana?</i> preguntaría por una costumbre de antes."},
    {"q": "<span class='chip'>Escritura · correo a una amiga</span> Pauta: <i>Pregúntale qué tal su primer día en el trabajo nuevo y cómo son sus compañeros.</i>",
     "o": ["¿Qué tal tu primer día? ¿Cómo son tus compañeros?", "¿Qué tal tu primer día? ¿Cómo eran tus compañeros?", "¿Qué tal su primer día? ¿Cómo son sus compañeros?"],
     "why": "Sus compañeros siguen siendo sus compañeros: presente (<i>son</i>). No todo en un correo tiene que ir en pasado."},
    {"q": "<span class='chip'>Oral · después del monólogo</span> El examinador te pregunta: <i>¿Has estado alguna vez en Asturias?</i> Tú quieres devolverle la pregunta.",
     "o": ["Sí, estuve el verano pasado. ¿Y tú? ¿Has estado alguna vez?", "Sí, estaba el verano pasado. ¿Y tú? ¿Estabas alguna vez?", "Sí, he estado el verano pasado. ¿Y tú? ¿Estuviste alguna vez?"],
     "why": "Con <i>el verano pasado</i> la ventana se cierra: <i>estuve</i>. Para devolver la pregunta, vuelves a la ventana abierta: <i>¿Has estado alguna vez?</i>"},
]

# E1 Proceso o fin
E_PROCESO = [
    {"q": "<b>Cuando entraba en el cine, me llamó Pablo.</b><br>¿Dónde estabas cuando sonó el teléfono?",
     "o": ["En la puerta, entrando.", "Ya sentado dentro del cine."],
     "why": "<i>Entraba</i>: estás dentro de la acción de entrar. La llamada llega en medio."},
    {"q": "<b>Cuando entré en el cine, me llamó Pablo.</b><br>¿Dónde estabas cuando sonó el teléfono?",
     "o": ["Ya dentro del cine.", "En la puerta, entrando."],
     "why": "<i>Entré</i>: la acción de entrar ya terminó. Después, la llamada."},
    {"q": "<b>Cuando cenábamos, se fue la luz.</b><br>¿Terminaron de cenar antes del apagón?",
     "o": ["No: estaban cenando.", "Sí: ya habían cenado."],
     "why": "<i>Cenábamos</i>: proceso. El apagón llega en medio de la cena."},
    {"q": "<b>Cuando cenamos, salimos a dar un paseo.</b><br>¿Qué pasó primero?",
     "o": ["Primero cenaron y después salieron.", "Salieron a mitad de la cena."],
     "why": "<i>Cenamos</i>: acción completa. Cuando + indefinido = primero eso y después lo otro."},
    {"q": "<b>Ana leía un libro en el tren.</b><br>¿Sabemos si lo terminó?",
     "o": ["No: solo la vemos leyendo.", "Sí: lo leyó entero."],
     "why": "El imperfecto es la foto por dentro: no ves el final de la acción."},
    {"q": "<b>Ana leyó un libro en el tren.</b><br>¿Sabemos si lo terminó?",
     "o": ["Sí: lo leyó entero.", "No: solo la vemos leyendo."],
     "why": "El indefinido ve la acción desde fuera, completa, con su final."},
    {"q": "<b>Cuando subía al autobús, vi a mi profesora.</b><br>¿Dónde estabas?",
     "o": ["En la puerta del autobús, subiendo.", "Sentado dentro del autobús."],
     "why": "<i>Subía</i>: en medio de la acción de subir."},
    {"q": "<b>Mi abuelo trabajaba en un banco.</b><br>¿Qué te cuenta esta frase?",
     "o": ["Cómo era su vida antes: una descripción.", "Algo que pasó un día concreto."],
     "why": "Imperfecto: el decorado de su vida, cómo eran las cosas antes."},
    {"q": "<b>Mi abuelo trabajó en un banco hasta 1990.</b><br>¿Qué te cuenta esta frase?",
     "o": ["Una etapa completa, con su final.", "Una costumbre sin final."],
     "why": "Con <i>hasta 1990</i> ves la etapa entera desde fuera: indefinido."},
    {"q": "<b>Iba a llamarte, pero me quedé sin batería.</b><br>¿Te llamó?",
     "o": ["No: era solo un plan.", "Sí, te llamó."],
     "why": "<i>Iba a</i> + infinitivo: un plan que no se hizo. Muy útil para el examen."},
]

# E4 Bien o mal (errores tipicos). o fijo = ["Bien", "Mal"]; ok = 0 o 1; fix = correccion
E_BIENMAL = [
    {"q": "Ayer he ido al cine con Laura.", "ok": 1, "fix": "Ayer <b>fui</b> al cine con Laura.",
     "why": "<i>Ayer</i> cierra la ventana. Ayer + perfecto no vale en ningún país."},
    {"q": "Cuando era pequeña, fui a la playa todos los veranos.", "ok": 1, "fix": "Cuando era pequeña, <b>iba</b> a la playa todos los veranos.",
     "why": "<i>Todos los veranos</i>: costumbre de antes, imperfecto."},
    {"q": "Mientras cocinaba, se quemó el arroz.", "ok": 0, "fix": "",
     "why": "Correcto: <i>cocinaba</i> es el proceso y <i>se quemó</i> lo que pasa en medio."},
    {"q": "En resumen, el viaje era fantástico.", "ok": 1, "fix": "En resumen, el viaje <b>fue</b> fantástico.",
     "why": "Valoras el viaje entero, ya terminado: indefinido."},
    {"q": "¿Alguna vez has comido paella?", "ok": 0, "fix": "",
     "why": "Correcto: <i>alguna vez</i>, ventana abierta, perfecto."},
    {"q": "Sí, he comido paella en 2019.", "ok": 1, "fix": "Sí, <b>comí</b> paella en 2019.",
     "why": "Con una fecha (<i>en 2019</i>) la ventana se cierra: indefinido."},
    {"q": "Hacía sol y fuimos a la playa.", "ok": 0, "fix": "",
     "why": "Correcto: decorado (<i>hacía sol</i>) + acción (<i>fuimos</i>)."},
    {"q": "De repente, sonaba el teléfono.", "ok": 1, "fix": "De repente, <b>sonó</b> el teléfono.",
     "why": "<i>De repente</i> presenta algo que pasa de golpe: acción, indefinido."},
    {"q": "Esta mañana he desayunado en casa.", "ok": 0, "fix": "",
     "why": "Correcto en España: <i>esta mañana</i> está dentro de hoy, perfecto."},
    {"q": "—¿Qué hacías cuando te llamé? —Estuve en la ducha.", "ok": 1, "fix": "—¿Qué hacías cuando te llamé? —<b>Estaba</b> en la ducha.",
     "why": "La pregunta pide el proceso (<i>hacías</i>): contestas con el mismo tiempo."},
    {"q": "Cuando tenía veinte años, viví un año en París.", "ok": 0, "fix": "",
     "why": "Correcto: <i>un año</i> es una etapa completa, con principio y fin. <i>Tenía</i> es el decorado."},
    {"q": "Ayer estuve dos horas en el médico.", "ok": 0, "fix": "",
     "why": "Correcto: aunque duró dos horas, la ves entera y terminada. Durar mucho no significa imperfecto."},
]

# ------------------------------------------------------------------ TEXTOS CON HUECOS (E2)
TEXTOS = [
    {"id": "lucas", "tipo": "Escritura · tarea 1 · correo a un amigo", "titulo": "Una semana rara",
     "texto": "¡Hola, Marta! ¿Qué tal? Yo [[he tenido|tuve|tenía#ven]] una semana muy rara. "
              "Mi plan era empezar las clases de guitarra, pero el primer día [[me puse|me ponía|me he puesto#fin]] enfermo y no [[pude|podía|he podido#fin]] ir. "
              "Ayer, por fin, [[fui|iba|he ido#cuando]] al médico. Mientras [[esperaba|esperé|he esperado#proc]] en la sala, "
              "[[vi|veía|he visto#fin]] a nuestra profesora de inglés. ¡Qué casualidad! ¿Y tú? ¿Qué [[has hecho|hacías|haces#ven]] esta semana? "
              "Un abrazo, Lucas"},
    {"id": "alicante", "tipo": "Escritura · tarea 2 · blog", "titulo": "Mi primer día en Alicante",
     "texto": "Hace dos años [[llegué|llegaba|he llegado#cuando]] a Alicante para estudiar español. "
              "[[Hacía|Hizo|Ha hecho#dec]] mucho calor y la ciudad [[estaba|estuvo|ha estado#dec]] llena de turistas. "
              "El primer día salí de casa para buscar la escuela, pero [[me perdí|me perdía|me he perdido#fin]]. "
              "Mientras [[miraba|miré|he mirado#proc]] el mapa del móvil, una señora mayor me [[preguntó|preguntaba|ha preguntado#fin]]: «¿Te puedo ayudar?». "
              "Al final, me [[acompañó|acompañaba|ha acompañado#serie]] hasta la puerta. [[Fue|Era|Es#val]] mi primera conversación en español. "
              "Desde entonces [[he hablado|hablé|hablaba#ven]] con muchas personas, pero nunca [[he olvidado|olvidé|olvidaba#ven]] a esa señora."},
    {"id": "ines", "tipo": "Escritura · tarea 2 · biografía", "titulo": "Inés Navarro, profesora de surf",
     "texto": "Inés Navarro [[nació|nacía|ha nacido#cuando]] en Cádiz en 1985. De niña [[iba|fue|ha ido#cost]] todos los días a la playa con su padre "
              "y le [[gustaba|gustó|ha gustado#cost]] mucho nadar. En 2005 [[empezó|empezaba|ha empezado#cuando]] a estudiar Medicina, "
              "pero dos años después lo [[dejó|dejaba|ha dejado#fin]] y [[abrió|abría|ha abierto#serie]] una escuela de surf. "
              "Ahora tiene cuarenta y un años y este año [[ha enseñado|enseñó|enseñaba#ven]] a más de doscientos alumnos."},
    {"id": "galicia", "tipo": "Oral · tarea 1 · monólogo", "titulo": "Mis mejores vacaciones",
     "texto": "Mis mejores vacaciones [[fueron|eran|son#val]] en Galicia, en 2023. [[Fui|Iba|He ido#cuando]] con dos amigos en tren. "
              "El pueblo [[era|fue|ha sido#dec]] muy pequeño y [[había|hubo|ha habido#dec]] muchas casas de piedra. "
              "Un día, mientras [[comíamos|comimos|hemos comido#proc]] en el puerto, [[llegó|llegaba|ha llegado#fin]] un barco de pesca "
              "y [[bajamos|bajábamos|hemos bajado#serie]] a verlo. Allí [[conocimos|conocíamos|hemos conocido#serie]] a un pescador muy simpático. "
              "Este año no [[he viajado|viajaba|viajo#ven]] mucho, pero el verano que viene voy a volver."},
]

# E3 Antes, ahora y el cambio
ANTES_AHORA = [
    {"tema": "Tomar café", "texto": "Antes [[tomaba|tomé|he tomado#cost]] cuatro cafés al día, pero ahora tomo té: lo [[dejé|dejaba|he dejado#cuando]] hace un año."},
    {"tema": "Tomar café (otra vez)", "texto": "Antes [[tomaba|tomé|he tomado#cost]] cuatro cafés al día, pero ahora ya no: lo [[he dejado|dejé|dejaba#ven]] este mes."},
    {"tema": "Ir en coche al trabajo", "texto": "Antes [[iba|fui|he ido#cost]] en coche al trabajo, pero ahora voy en bici porque en 2023 [[me mudé|me mudaba|me he mudado#cuando]] al centro."},
    {"tema": "Comer carne", "texto": "De joven [[comía|comí|he comido#cost]] carne todos los días, pero ahora soy vegetariana: el año pasado [[vi|veía|he visto#cuando]] un documental sobre los animales."},
    {"tema": "Bañarse en el mar", "texto": "Cuando era niño [[nadaba|nadé|he nadado#cost]] en el mar sin miedo, pero ahora no me baño: un verano me [[picó|picaba|ha picado#fin]] una medusa."},
    {"tema": "Vivir con mis padres", "texto": "Antes [[vivía|viví|he vivido#cost]] con mis padres, pero ahora vivo sola: este año [[he alquilado|alquilé|alquilaba#ven]] un piso."},
    {"tema": "Jugar al fútbol", "texto": "Antes [[jugaba|jugué|he jugado#cost]] al fútbol los domingos, pero ahora no juego porque el mes pasado me [[hice|hacía|he hecho#cuando]] daño en la rodilla."},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
LAMINAS = [
    {"id": "lola", "tarea": "Tarea 1 · correo a una amiga", "palabras": [60, 70], "preguntas": 2,
     "intro": "Has recibido este mensaje de tu amiga Lola:",
     "mensaje": "¡Hola! ¿Qué tal? Hace mucho que no sé nada de ti. Yo este fin de semana he ido a un concierto de jazz en la playa y ha sido increíble. ¿Y tú? ¿Qué hiciste el sábado? ¡Cuéntame! Besos, Lola",
     "consigna": "Escribe un correo a Lola. En él tienes que:",
     "pautas": [("saludar;", []),
                ("contarle qué hiciste el fin de semana y con quién;", ["indef"]),
                ("decirle cómo era el lugar y qué tiempo hacía;", ["imperf"]),
                ("preguntarle por el concierto (dos preguntas);", ["indef", "perf"]),
                ("despedirte.", [])]},
    {"id": "dia", "tarea": "Tarea 2 · opción 1 · blog", "palabras": [70, 80], "preguntas": 0,
     "intro": "",
     "mensaje": "",
     "consigna": "Escribe una entrada para tu blog sobre un día que no salió como pensabas. Cuenta:",
     "pautas": [("cuándo fue, dónde estabas y con quién;", ["indef", "imperf"]),
                ("qué ibas a hacer ese día;", ["imperf"]),
                ("qué pasó;", ["indef"]),
                ("cómo te sentiste y cómo terminó el día;", ["imperf", "indef"]),
                ("si te ha pasado algo parecido otra vez.", ["perf"])]},
]

# Detector de marcadores para «Revisa tus pasados». re = expresion regular (minusculas)
DETECTOR = [
    {"re": r"\bayer\b|\banoche\b|\banteayer\b", "t": "indef"},
    {"re": r"\b(el|la) (lunes|martes|mi[eé]rcoles|jueves|viernes|s[aá]bado|domingo|semana|mes|a[nñ]o|verano|invierno|fin de semana) pasad[oa]\b", "t": "indef"},
    {"re": r"\bhace (un|una|unos|unas|dos|tres|cuatro|cinco|diez|\d+) \w+", "t": "indef"},
    {"re": r"\ben (19|20)\d\d\b", "t": "indef"},
    {"re": r"\bde repente\b|\bun d[ií]a\b|\bal final\b", "t": "indef"},
    {"re": r"\bhoy\b|\besta (ma[nñ]ana|tarde|semana)\b|\beste (a[nñ]o|mes|verano|fin de semana)\b|\b[uú]ltimamente\b", "t": "perf"},
    {"re": r"\balguna vez\b|\bnunca\b|\btodav[ií]a no\b", "t": "perf"},
    {"re": r"\bde (ni[nñ][oa]|peque[nñ][oa]|joven)\b|\bcuando era\b|\bantes\b|\bsiempre\b|\btodos los\b|\btodas las\b|\bnormalmente\b|\bmientras\b|\ba menudo\b", "t": "imperf"},
]

# ------------------------------------------------------------------ AHORA TU: ORAL (preguntas en cadena)
# q con ____ ; o (la primera es la buena); modelo con marcas de tiempo
ORAL = [
    {"q": "¿Qué <b>(hacer)</b> ____ el fin de semana pasado?", "o": ["hiciste", "hacías", "has hecho"],
     "modelo": "El sábado [f:fui] al mercado con mi pareja y por la tarde [f:vimos] una película en casa. [i:Estábamos] muy cansados, así que no [f:salimos]. ¿Y tú? ¿Qué [f:hiciste]?"},
    {"q": "¿<b>(Estar)</b> ____ alguna vez en un concierto al aire libre?", "o": ["Has estado", "Estabas", "Estás"],
     "modelo": "Sí, [v:he estado] dos o tres veces. El último [f:fue] en verano, en Valencia: [i:hacía] mucho calor, pero [f:fue] genial. ¿Y tú? ¿[v:Has estado] alguna vez?"},
    {"q": "Cuando eras pequeño, ¿cómo <b>(ser)</b> ____ tu habitación?", "o": ["era", "fue", "ha sido"],
     "modelo": "[i:Era] pequeña y la [i:compartía] con mi hermano. [i:Había] dos camas y muchos juguetes por el suelo. Cuando [f:cumplí] quince años, por fin [f:tuve] una para mí solo. ¿Y la tuya? ¿Cómo [i:era]?"},
    {"q": "¿Qué tal te <b>(ir)</b> ____ la entrevista de trabajo del lunes?", "o": ["fue", "iba", "ha ido"],
     "modelo": "Me [f:fue] bastante bien. [i:Estaba] muy nervioso, pero la entrevistadora [i:era] simpática y me [f:hizo] preguntas fáciles. ¿Y a ti? ¿Qué tal te [f:fue] tu última entrevista?"},
    {"q": "¿Qué <b>(hacer)</b> ____ hoy antes de venir?", "o": ["has hecho", "hacías", "hiciste"],
     "modelo": "[v:He desayunado] tranquilamente y [v:he repasado] mis notas. Luego [v:he venido] en autobús. ¿Y tú? ¿Qué [v:has hecho]?"},
    {"q": "¿Dónde <b>(vivir)</b> ____ antes?", "o": ["vivías", "viviste", "has vivido"],
     "modelo": "Antes [i:vivía] en un pueblo pequeño, cerca de Lyon. Allí no [i:había] mucho que hacer, por eso [f:me mudé] a la ciudad. ¿Y tú? ¿Siempre [v:has vivido] aquí?"},
    {"q": "De niño, ¿qué <b>(hacer)</b> ____ normalmente después del colegio?", "o": ["hacías", "hiciste", "has hecho"],
     "modelo": "Normalmente [i:merendaba] en casa de mi abuela y luego [i:jugaba] en la calle con los vecinos. Los deberes los [i:hacía] por la noche. ¿Y tú? ¿Qué [i:hacías]?"},
    {"q": "¿Cuál es el mejor regalo que <b>(recibir)</b> ____ en tu vida?", "o": ["has recibido", "recibías", "recibes"],
     "modelo": "El mejor regalo que [v:he recibido] es una bicicleta roja. Me la [f:regalaron] mis padres cuando [f:cumplí] doce años. ¿Y tú? ¿Cuál es el mejor regalo que [v:has recibido]?"},
    {"q": "¿Dónde <b>(pasar)</b> ____ las últimas Navidades?", "o": ["pasaste", "pasabas", "has pasado"],
     "modelo": "Las [f:pasé] en casa de mis suegros, en Burgos. [i:Hacía] muchísimo frío, pero [f:comimos] muy bien y lo [f:pasamos] genial. ¿Y tú? ¿Dónde las [f:pasaste]?"},
    {"q": "¿Qué <b>(estar)</b> ____ haciendo ayer a las diez de la noche?", "o": ["estabas", "estuviste", "has estado"],
     "modelo": "[i:Estaba] cenando con mi familia. Después [f:vi] un rato la tele y [f:me acosté] pronto. ¿Y tú? ¿Qué [i:estabas] haciendo?"},
    {"q": "¿<b>(Salir)</b> ____ mucho este mes?", "o": ["Has salido", "Salías", "Sales"],
     "modelo": "No, este mes [v:he salido] poco: [v:he tenido] mucho trabajo. Solo [v:he ido] una vez al cine: [f:fui] el sábado con unas amigas y lo [f:pasamos] genial. ¿Y tú? ¿[v:Has salido] mucho?"},
    {"q": "¿Por qué <b>(empezar)</b> ____ a estudiar español?", "o": ["empezaste", "empezabas", "has empezado"],
     "modelo": "[f:Empecé] porque mi pareja es española y [i:quería] hablar con su familia. ¿Y tú? ¿Por qué [f:empezaste]?"},
]
