# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R08: CONECTORES (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R08_conectores.py
#
# ENFOQUE COGNITIVO (aprobado por Maria, 22/10): LAS FLECHAS ENTRE FRASES
#   Siguiendo el mapa de la R06, cada conector es una FLECHA que le dice al lector hacia donde va la frase
#   siguiente. Cinco flechas, cada una con su dibujo y su color:
#   o  LA LINEA DE PASOS (ordenar): primero -> despues / luego -> mas tarde -> al final; entonces = en ese momento.
#   s  EL MAS (sumar en la misma direccion): y, ademas, tambien, tampoco. Ademas solo suma cosas del mismo lado.
#   g  LA CURVA (girar): pero. Lo siguiente va contra lo que esperas.
#   c  LA FLECHA HACIA ATRAS (la causa): porque; es que para excusarse con un amigo.
#   r  LA FLECHA HACIA DELANTE (lo que pasa): por eso; entonces en la conversacion.
#   EL ESPEJO: los mismos dos hechos, la flecha se da la vuelta (me quede en casa porque llovia = llovia, por
#   eso me quede en casa). AL FINAL tambien avisa de que el plan cambio (trampa de la lectura y la auditiva).
#   NIVEL: solo los conectores [P] del Plan curricular (y, pero, o, porque, es que, tambien, tampoco, entonces,
#   primero, despues, luego, mas tarde, al final, por eso, ademas). Asi que, aunque, como y sin embargo son [R]:
#   salen en un recuadro "los veras en los textos", nunca en ejercicios ni en el detector.
#
# MARCAS
#   [o:primero] ordenar (azul) · [s:ademas] sumar (verde) · [g:pero] girar (violeta)
#   [c:porque] la causa (ambar) · [r:por eso] lo que pasa (coral)
#   Huecos: [[correcta|distractor|distractor#motivo]]  (la primera es la buena; se barajan)
# Espanol de Espana. Ejemplos propios: ninguno sale de los materiales de Maria ni repite los del kit (M3-1:
# playa con Ana, diario de Clara), la revision final (M3-4) o las fichas R01-R07.

# ------------------------------------------------------------------ LAS FLECHAS
FAMILIAS = {
    "o": {"n": "Ordenar", "dib": "la línea de pasos", "q": "¿Qué viene ahora?",
          "words": ["primero", "después", "luego", "más tarde", "al final", "entonces"],
          "txt": "Pones los hechos en fila, uno detrás de otro: <b>primero</b>, <b>después</b> o <b>luego</b>, <b>más tarde</b>, <b>al final</b>. En una historia, <b>entonces</b> = en ese momento."},
    "s": {"n": "Sumar", "dib": "el más", "q": "¿Y qué más?",
          "words": ["y", "además", "también", "tampoco"],
          "txt": "Añades algo que va <b>en la misma dirección</b>: bueno + bueno, malo + malo. <b>Y</b>, <b>además</b>, <b>también</b>; para sumar un no, <b>tampoco</b>."},
    "g": {"n": "Girar", "dib": "la curva", "q": "¿Algo distinto de lo que esperas?",
          "words": ["pero"],
          "txt": "La frase siguiente <b>gira</b>: va contra lo que esperas. Es pequeña, <b>pero</b> tiene un balcón precioso."},
    "c": {"n": "La causa", "dib": "la flecha hacia atrás", "q": "¿Por qué?",
          "words": ["porque", "es que"],
          "txt": "Dices lo que pasó y <b>miras hacia atrás</b>, a la causa: <b>porque</b>. Con un amigo, para explicar un no: <b>es que</b>."},
    "r": {"n": "Lo que pasa", "dib": "la flecha hacia delante", "q": "¿Y qué pasa entonces?",
          "words": ["por eso", "entonces"],
          "txt": "Dices la causa y <b>miras hacia delante</b>, a lo que pasa: <b>por eso</b>. En una conversación, también <b>entonces</b>."},
}
ORDEN_FAM = ["o", "s", "g", "c", "r"]

# Mira la diferencia: los mismos hechos (o casi), dos flechas distintas.
# Cada lado: f = frase marcada, fam = su flecha, x / y = las dos cajas del dibujo (en el orden de la frase).
PAREJAS = [
    {"tema": "La lluvia",
     "a": {"f": "Me quedé en casa [c:porque] llovía.", "fam": "c", "x": "me quedé en casa", "y": "llovía"},
     "b": {"f": "Llovía, [r:por eso] me quedé en casa.", "fam": "r", "x": "llovía", "y": "me quedé en casa"},
     "expl": "Los mismos dos hechos. Con <b>porque</b> dices primero lo que pasó y miras hacia atrás, a la causa. Con <b>por eso</b> dices primero la causa y miras hacia delante. Es el espejo."},
    {"tema": "La habitación",
     "a": {"f": "La habitación es pequeña, [g:pero] tiene un balcón precioso.", "fam": "g", "x": "es pequeña", "y": "tiene un balcón precioso"},
     "b": {"f": "La habitación es pequeña y, [s:además], no tiene ventana.", "fam": "s", "x": "es pequeña", "y": "no tiene ventana"},
     "expl": "«Pequeña» es algo malo. Si lo siguiente es bueno, giras: <b>pero</b>. Si es otra cosa mala, sumas: <b>además</b>. Además nunca gira."},
    {"tema": "Las tardes de Óscar",
     "a": {"f": "Por las tardes, Óscar estudia [s:y] trabaja en un bar.", "fam": "s", "x": "estudia", "y": "trabaja en un bar"},
     "b": {"f": "Por las tardes, Óscar estudia y [o:después] trabaja en un bar.", "fam": "o", "x": "estudia", "y": "trabaja en un bar"},
     "expl": "Con <b>y</b> solo sumas: hace las dos cosas. Con <b>después</b> pones un orden: primero una y luego la otra."},
    {"tema": "El cine",
     "a": {"f": "—¿Vienes al cine? —No puedo, [c:es que] tengo que trabajar.", "fam": "c", "x": "no puedo", "y": "tengo que trabajar"},
     "b": {"f": "—¿Vienes al cine? —Me apetece mucho, [g:pero] tengo que trabajar.", "fam": "g", "x": "me apetece mucho", "y": "tengo que trabajar"},
     "expl": "<b>Es que</b> da la razón de tu «no»: mira hacia atrás. <b>Pero</b> gira: te apetece y, en la dirección contraria, tienes que trabajar."},
    {"tema": "Entonces",
     "a": {"f": "—El sábado trabajo. —[r:Entonces] quedamos el domingo.", "fam": "r", "x": "el sábado trabajo", "y": "quedamos el domingo"},
     "b": {"f": "Estaba en la ducha y [o:entonces] sonó el teléfono.", "fam": "o", "x": "estaba en la ducha", "y": "sonó el teléfono"},
     "expl": "<b>Entonces</b> tiene dos caras. En una conversación, es lo que pasa por lo que te acaban de decir (= por eso). En una historia, es «en ese momento»."},
    {"tema": "El mar",
     "a": {"f": "Me gusta el mar y [s:también] la montaña.", "fam": "s", "x": "me gusta el mar", "y": "la montaña"},
     "b": {"f": "Me gusta el mar, [g:pero] prefiero la montaña.", "fam": "g", "x": "me gusta el mar", "y": "prefiero la montaña"},
     "expl": "<b>También</b> suma: te gustan los dos. <b>Pero</b> gira: te gusta el mar, y aun así eliges la montaña."},
]

# Las flechas en un vistazo: (flecha, palabras, ejemplo marcado, donde la usas)
VISTAZO = [
    ("o", "primero · después · luego · más tarde · al final · entonces (= en ese momento)", "[o:Primero] cenamos en casa y [o:después] fuimos a bailar.", "Contar algo que pasó: escritura T2, oral T1."),
    ("s", "y · además · también · tampoco", "El piso es luminoso y, [s:además], es barato.", "Añadir otra idea del mismo lado."),
    ("g", "pero", "Me encanta bailar, [g:pero] bailo fatal.", "Decir lo contrario de lo que se espera."),
    ("c", "porque · es que (con amigos)", "No te llamé [c:porque] no tenía batería.", "Explicar por qué. Es que, para excusarte."),
    ("r", "por eso · entonces (en una conversación)", "No tenía batería, [r:por eso] no te llamé.", "Decir qué pasa por eso."),
]
ELEGIR = "Y una flecha pequeña: <b>o</b>, cuando hay que elegir (¿Vamos en tren <b>o</b> en coche?)."
# [R] del Plan curricular: se ven en los textos, no hacen falta para aprobar (no se practican)
LOS_VERAS = [
    ("así que", "= por eso", "Perdí el autobús, así que llegué tarde."),
    ("aunque", "≈ pero", "Fuimos a la playa aunque hacía frío."),
    ("como (al principio de la frase)", "= porque", "Como llovía, nos quedamos en casa."),
    ("sin embargo", "= pero (más formal)", "El hotel era viejo; sin embargo, estaba muy limpio."),
]

# ------------------------------------------------------------------ CONTAR EN ORDEN
LINEA = ["primero", "después / luego", "más tarde", "al final"]
ANTES = ("El martes tuve el examen de conducir. Me levanté a las siete y desayuné y fui a la autoescuela y estaba muy nervioso "
         "y el examinador era muy serio y conduje por el centro y aparqué bien y aprobé.")
DESPUES = ("El martes tuve el examen de conducir. [o:Primero] me levanté a las siete [s:y] desayuné. [o:Después] fui a la autoescuela. "
           "Estaba muy nervioso [c:porque] el examinador era muy serio. [o:Luego] conduje por el centro [s:y], [o:al final], aparqué en una calle muy estrecha. "
           "[g:Pero] lo hice bien: ¡aprobé! [r:Por eso] el martes por la noche lo celebré con mi familia.")
ORDEN_TIPS = [
    "No repitas: <b>después</b>, <b>luego</b>, <b>más tarde</b>. Tres palabras para el mismo paso, y tu texto suena mucho mejor.",
    "<b>Primero</b> abre la fila y <b>al final</b> la cierra. Con esas dos ya tienes el principio y el final de tu historia.",
    "En una historia, <b>entonces</b> = en ese momento: Estaba en la ducha y <b>entonces</b> sonó el teléfono.",
    "Pon una coma detrás cuando la flecha va al principio de la frase y es larga: <b>Al final,</b> volvimos a casa en taxi.",
]
# Al final: el plan cambio (q = pregunta del examen; a = respuesta y por que)
AL_FINAL = [
    {"tipo": "Lectura", "txt": "Mi hermano quería celebrar su cumpleaños en un restaurante, pero al final lo celebró en casa, con una paella.",
     "q": "¿Dónde celebró su cumpleaños?", "a": "<b>En casa.</b> El restaurante era el plan; lo que pasó de verdad va detrás de «al final»."},
    {"tipo": "Auditiva", "txt": "—¿Te has comprado el abrigo negro? —Iba a comprarlo, pero era muy caro. Al final me he llevado el gris.",
     "q": "¿Qué abrigo se ha comprado?", "a": "<b>El gris.</b> «Iba a» es un plan que no pasó; «pero» y «al final» te avisan."},
    {"tipo": "Lectura", "txt": "Pensábamos ir a Sevilla en coche. Al final fuimos en tren, porque mi coche estaba en el taller.",
     "q": "¿Cómo fueron a Sevilla?", "a": "<b>En tren.</b> El coche sale en el texto, pero antes de «al final»: es la trampa."},
]

# ------------------------------------------------------------------ PORQUE Y POR ESO
# El constructor del espejo: a = la causa, b = lo que pasa (etiquetas del dibujo)
ESPEJO = [
    {"tema": "El autobús", "a": "no llegaba el autobús", "b": "fui andando",
     "c": "Fui andando [c:porque] no llegaba el autobús.", "r": "No llegaba el autobús, [r:por eso] fui andando."},
    {"tema": "El perro", "a": "tengo un perro", "b": "paseo mucho",
     "c": "Paseo mucho [c:porque] tengo un perro.", "r": "Tengo un perro, [r:por eso] paseo mucho."},
    {"tema": "El trabajo", "a": "trabajo cerca de casa", "b": "voy en bici",
     "c": "Voy al trabajo en bici [c:porque] trabajo cerca de casa.", "r": "Trabajo cerca de casa, [r:por eso] voy en bici."},
    {"tema": "El ruido", "a": "vivo en el centro", "b": "hay mucho ruido",
     "c": "En mi calle hay mucho ruido [c:porque] vivo en el centro.", "r": "Vivo en el centro, [r:por eso] hay mucho ruido en mi calle."},
    {"tema": "La cena", "a": "la nevera estaba vacía", "b": "pedimos una pizza",
     "c": "Pedimos una pizza [c:porque] la nevera estaba vacía.", "r": "La nevera estaba vacía, [r:por eso] pedimos una pizza."},
    {"tema": "El regalo", "a": "le encanta leer", "b": "le regalé un libro",
     "c": "Le regalé un libro a Elena [c:porque] le encanta leer.", "r": "A Elena le encanta leer, [r:por eso] le regalé un libro."},
]
ES_QUE = [
    "—¿Vienes a la playa? —Hoy no puedo, [c:es que] tengo visita.",
    "Perdona por no contestar antes: [c:es que] he estado de viaje.",
]
ES_QUE_USTED = "Estimada señora Gil: no puedo ir a la reunión del jueves [c:porque] tengo médico."
ENTONCES_CONV = [
    "—No hay entradas para el sábado. —[r:Entonces] vamos el domingo.",
    "—Yo llevo la bebida. —Vale, [r:entonces] yo compro el pan.",
]
# Por que, porque (pregunta y respuesta): (forma, cuando, ejemplo)
POR_QUE = [
    ("¿Por qué...?", "Para preguntar: dos palabras y tilde.", "¿Por qué no viniste ayer?"),
    ("Porque...", "Para contestar o explicar: una palabra, sin tilde.", "Porque estaba enfermo."),
]

# ------------------------------------------------------------------ EN EL EXAMEN
DONDE = [
    ("Escritura · tarea 2", "Cuentas algo que pasó: un día, un viaje, una biografía. Las flechas de orden ponen los hechos en fila y tu texto se lee fácil. La escala oficial deja en la banda 1 los textos desordenados que solo usan conectores muy básicos (y, pero, porque).",
     "[o:Primero] visitamos el castillo; [o:después] comimos en el puerto [s:y], [o:al final], vimos la puesta de sol."),
    ("Escritura · tarea 1", "En el correo explicas y te excusas: porque o es que (con un amigo), por eso. Y sumas ideas con además.",
     "Me encantaría ir, [g:pero] ese día trabajo: [c:es que] mi compañera está de vacaciones."),
    ("Oral · tarea 1", "En el monólogo, las flechas son tu guion: te ayudan a pasar de una pauta a otra sin quedarte callado.",
     "[o:Primero] voy a hablar de mi familia; [o:después], de lo que hacíamos de niños [s:y], [o:al final], de mis planes."),
    ("Oral · tarea 3", "En el diálogo: es que para explicar un no, entonces para proponer otra cosa, pero para decir que no del todo.",
     "No puedo el viernes, [c:es que] tengo una cena. [r:Entonces] quedamos el sábado, [g:pero] por la tarde."),
    ("Lectura y auditiva", "Pero y al final avisan de un cambio: la respuesta casi siempre va detrás.",
     "Íbamos a ir en coche, [g:pero] [o:al final] fuimos en tren."),
]
REGLA_ORO = "Pasada 7 de la revisión final: mira el principio de cada frase y las palabras <b>y</b> y <b>porque</b>. Si ves tres «y» en una frase, cambia una por una flecha."
# Errores tipicos: (mal, bien marcado, por que). Cada \"mal\" tiene que dar un aviso del detector.
ERRORES = [
    ("Fuimos a la playa y comimos y nadamos y volvimos y cenamos.",
     "Fuimos a la playa. [o:Primero] comimos, [o:después] nadamos [s:y], [o:al final], volvimos a casa para cenar.",
     "Todo con <b>y</b>: no hay flechas y parece una lista. Cambia algunas «y» por flechas de orden."),
    ("La comida estaba buena. Además, el camarero era antipático.",
     "La comida estaba buena, [g:pero] el camarero era antipático.",
     "<b>Además</b> suma en la misma dirección (bueno + bueno, malo + malo). Si la segunda idea va al revés, es <b>pero</b>."),
    ("Llovía, porque me quedé en casa.",
     "Llovía, [r:por eso] me quedé en casa.",
     "La flecha va al revés: la lluvia es la causa. Detrás de <b>porque</b> va la causa; detrás de <b>por eso</b>, lo que pasa."),
    ("Me quedé en casa, por eso llovía.",
     "Me quedé en casa [c:porque] llovía.",
     "¡No llueve porque tú te quedas en casa! Detrás de <b>por eso</b> va el resultado, no la causa."),
    ("En el final, compramos el sofá azul.",
     "[o:Al final] compramos el sofá azul.",
     "Es <b>al final</b>, con <i>a</i>. «En el final» no se dice."),
    ("—No puedo ir. —Yo también no.",
     "—No puedo ir. —Yo [s:tampoco].",
     "Para sumar un no: <b>tampoco</b> (mira la ficha R05)."),
    ("Estimada señora Gil: no puedo ir a la reunión, es que tengo médico.",
     "Estimada señora Gil: no puedo ir a la reunión [c:porque] tengo médico.",
     "<b>Es que</b> es de la conversación y de los correos a amigos. En un correo de usted, <b>porque</b>."),
    ("¿Porque no vienes a la fiesta?",
     "¿Por qué no vienes? —[c:Porque] tengo que estudiar.",
     "Para preguntar, <b>por qué</b> (dos palabras y con tilde). Para contestar, <b>porque</b>."),
    ("Fuimos al museo. Después comimos. Después paseamos. Después cenamos.",
     "Fuimos al museo. [o:Después] comimos, [o:luego] paseamos [s:y] [o:más tarde] cenamos.",
     "Tres veces «después» cansa. Cambia a <b>luego</b>, <b>más tarde</b>, <b>al final</b>."),
    ("Además de, el piso tiene una terraza.",
     "[s:Además], el piso tiene una terraza.",
     "<b>Además de</b> necesita algo detrás (además de la cocina...). Sola, con coma: <b>además</b>."),
]
# Errores tipicos que el detector tiene que ver (ids del detector)
REQ = ["muchas_y", "ademas_contra", "causa_al_reves", "por_eso_tiempo", "en_el_final", "tambien_no", "es_que_usted",
       "porque_pregunta", "despues_rep", "ademas_de"]

# ------------------------------------------------------------------ EJERCICIOS
# 1. ¿Que flecha? q con ____, f = flecha de la buena, o = [buena, d1, d2]
P_FLECHA = [
    {"q": "El restaurante es caro, ____ la comida es buenísima.", "f": "g", "o": ["pero", "además", "por eso"], "why": "Caro es malo; buenísima es bueno: la frase gira. <b>Pero</b>."},
    {"q": "Mañana tengo un examen; ____ hoy no salgo.", "f": "r", "o": ["por eso", "porque", "pero"], "why": "El examen es la causa y «no salgo» es lo que pasa: flecha hacia delante, <b>por eso</b>."},
    {"q": "No fui a clase ____ estaba enfermo.", "f": "c", "o": ["porque", "por eso", "además"], "why": "Primero lo que pasó (no fui) y después la causa: <b>porque</b>."},
    {"q": "____ desayunamos en el balcón y después fuimos a la playa.", "f": "o", "o": ["Primero", "Al final", "Además"], "why": "Es el primer paso de la fila: <b>primero</b>. Después viene detrás."},
    {"q": "El piso tiene tres habitaciones y, ____, un jardín pequeño.", "f": "s", "o": ["además", "pero", "porque"], "why": "Otra cosa buena del piso: sumas, <b>además</b>."},
    {"q": "Queríamos ir a la montaña, pero ____ fuimos a la playa: llovía en la sierra.", "f": "o", "o": ["al final", "primero", "además"], "why": "El plan cambió: lo que pasó de verdad va detrás de <b>al final</b>."},
    {"q": "—¿Vienes a la cena del viernes? —Lo siento, no puedo: ____ trabajo hasta las diez.", "f": "c", "o": ["es que", "por eso", "además"], "why": "Explicas tu «no» a un amigo: <b>es que</b>."},
    {"q": "—El sábado no puedo, tengo una boda. —Vale, ____ quedamos el domingo.", "f": "r", "o": ["entonces", "porque", "además"], "why": "En la conversación, lo que propones por lo que te han dicho: <b>entonces</b>."},
    {"q": "Estaba en la ducha y ____ sonó el teléfono.", "f": "o", "o": ["entonces", "por eso", "además"], "why": "En una historia, <b>entonces</b> = en ese momento."},
    {"q": "Este verano no tengo vacaciones, ____ mi hermano tampoco.", "f": "s", "o": ["y", "pero", "porque"], "why": "Sumas otro «no» en la misma dirección: <b>y</b> mi hermano tampoco."},
    {"q": "Vimos una película, cenamos y, ____, nos fuimos a dormir.", "f": "o", "o": ["al final", "primero", "porque"], "why": "Es el último paso de la noche: <b>al final</b>."},
    {"q": "¿Prefieres ir en tren ____ en coche?", "f": "s", "o": ["o", "y", "pero"], "why": "Hay que elegir una de las dos cosas: <b>o</b>."},
    {"q": "Mi barrio es muy tranquilo, ____ por la noche no hay nada abierto.", "f": "g", "o": ["pero", "además", "porque"], "why": "Tranquilo es bueno; «no hay nada abierto» es lo malo: gira, <b>pero</b>."},
    {"q": "Llegué tarde al trabajo ____ había mucho tráfico.", "f": "c", "o": ["porque", "por eso", "entonces"], "why": "Lo que pasó y después la causa: <b>porque</b>."},
    {"q": "El hotel estaba en el centro; ____, íbamos andando a todas partes.", "f": "r", "o": ["por eso", "porque", "pero"], "why": "Estar en el centro es la causa; ir andando es lo que pasa: <b>por eso</b>."},
    {"q": "Primero visitamos la catedral; ____ comimos en un bar del puerto.", "f": "o", "o": ["luego", "primero", "porque"], "why": "El paso siguiente de la fila: <b>luego</b> (= después)."},
]
# 2. ¿Porque o por eso? (o = [buena, la del espejo, pero])
P_PORQUE = [
    {"q": "Tengo mucha hambre ____ no he desayunado.", "o": ["porque", "por eso", "pero"], "why": "Primero lo que pasa (tengo hambre); detrás, la causa: <b>porque</b>."},
    {"q": "No he desayunado, ____ tengo mucha hambre.", "o": ["por eso", "porque", "pero"], "why": "Primero la causa; detrás, lo que pasa: <b>por eso</b>."},
    {"q": "Mi prima vive en Londres, ____ habla muy bien inglés.", "o": ["por eso", "porque", "pero"], "why": "Vivir en Londres es la causa: flecha hacia delante, <b>por eso</b>."},
    {"q": "Mi prima habla muy bien inglés ____ vive en Londres.", "o": ["porque", "por eso", "pero"], "why": "Detrás va la causa (vive en Londres): <b>porque</b>."},
    {"q": "El ascensor no funcionaba, ____ subimos andando.", "o": ["por eso", "porque", "pero"], "why": "El ascensor roto es la causa; subir andando, lo que pasa: <b>por eso</b>."},
    {"q": "Subimos andando ____ el ascensor no funcionaba.", "o": ["porque", "por eso", "pero"], "why": "Detrás va la causa: <b>porque</b>."},
    {"q": "Me encanta este barrio ____ hay muchos parques.", "o": ["porque", "por eso", "pero"], "why": "¿Por qué te encanta? Por los parques: <b>porque</b>."},
    {"q": "Hay muchos parques en mi barrio, ____ siempre veo niños jugando.", "o": ["por eso", "porque", "pero"], "why": "Los parques son la causa; los niños jugando, lo que pasa: <b>por eso</b>."},
    {"q": "Estudio español ____ quiero trabajar en Madrid.", "o": ["porque", "por eso", "pero"], "why": "Detrás va la razón: <b>porque</b>."},
    {"q": "Quiero trabajar en Madrid, ____ estudio español.", "o": ["por eso", "porque", "pero"], "why": "Primero la razón; después lo que haces: <b>por eso</b>."},
    {"q": "Hoy no hay clase ____ es fiesta.", "o": ["porque", "por eso", "pero"], "why": "Detrás va la causa: <b>porque</b> es fiesta."},
    {"q": "Hoy es fiesta, ____ no hay clase.", "o": ["por eso", "porque", "pero"], "why": "La fiesta es la causa: <b>por eso</b> no hay clase."},
]
# 4. Bien o mal: ok 0 = bien, 1 = mal
E_BIENMAL = [
    {"q": "Comimos y bebimos y bailamos y cantamos toda la noche.", "ok": 1, "fix": "<b>Primero</b> comimos y bebimos; <b>después</b> bailamos y cantamos toda la noche.", "why": "Todo con y: parece una lista."},
    {"q": "El museo era precioso. Además, la entrada era cara.", "ok": 1, "fix": "El museo era precioso, <b>pero</b> la entrada era cara.", "why": "Precioso es bueno y cara es malo: gira, pero."},
    {"q": "Hacía mucho calor, porque nos quedamos en la piscina.", "ok": 1, "fix": "Hacía mucho calor, <b>por eso</b> nos quedamos en la piscina.", "why": "El calor es la causa: por eso."},
    {"q": "Fui en bici al trabajo, por eso hacía sol.", "ok": 1, "fix": "Fui en bici al trabajo <b>porque</b> hacía sol.", "why": "El sol no es lo que pasa por ir en bici: es la causa, porque."},
    {"q": "En el final, cenamos en un restaurante chino.", "ok": 1, "fix": "<b>Al final</b> cenamos en un restaurante chino.", "why": "Se dice al final."},
    {"q": "—A mí no me gusta el fútbol. —A mí también no.", "ok": 1, "fix": "—A mí no me gusta el fútbol. —A mí <b>tampoco</b>.", "why": "Para sumar un no: tampoco."},
    {"q": "¿Porque llegas tan tarde?", "ok": 1, "fix": "¿<b>Por qué</b> llegas tan tarde?", "why": "Para preguntar: por qué, dos palabras y con tilde."},
    {"q": "Además de, hay una piscina para niños.", "ok": 1, "fix": "<b>Además</b>, hay una piscina para niños.", "why": "Además de necesita algo detrás; sola: además."},
    {"q": "Estimado señor Ruiz: no puedo ir el lunes, es que tengo un examen. Atentamente, Yuki.", "ok": 1, "fix": "Estimado señor Ruiz: no puedo ir el lunes <b>porque</b> tengo un examen. Atentamente, Yuki.", "why": "En un correo de usted: porque."},
    {"q": "Fuimos al parque. Después jugamos. Después merendamos. Después volvimos.", "ok": 1, "fix": "Fuimos al parque. Después jugamos, <b>luego</b> merendamos y <b>al final</b> volvimos.", "why": "Tres veces después: varía."},
    {"q": "La casa es vieja, pero es muy bonita.", "ok": 0, "fix": "", "why": "Correcto: vieja (malo) y bonita (bueno), la frase gira con pero."},
    {"q": "No pude ir a la fiesta porque estaba enferma.", "ok": 0, "fix": "", "why": "Correcto: detrás de porque va la causa."},
    {"q": "Estaba enferma, por eso no pude ir a la fiesta.", "ok": 0, "fix": "", "why": "Correcto: es el espejo de la frase con porque."},
    {"q": "El hotel era barato y, además, estaba en el centro.", "ok": 0, "fix": "", "why": "Correcto: dos cosas buenas, además suma."},
    {"q": "—No me gustan las películas de miedo. —A mí tampoco.", "ok": 0, "fix": "", "why": "Correcto: tampoco suma un no."},
    {"q": "—¿Vienes? —No puedo, es que tengo que estudiar.", "ok": 0, "fix": "", "why": "Correcto: con un amigo, es que explica el no."},
    {"q": "Primero visitamos la catedral, luego comimos y al final fuimos a la playa.", "ok": 0, "fix": "", "why": "Correcto: una fila de pasos sin repetir."},
    {"q": "Al final no fuimos a la montaña: fuimos a la playa.", "ok": 0, "fix": "", "why": "Correcto: al final avisa de que el plan cambió."},
]

# 3. Textos con huecos: motivos (flecha, explicacion, respuestas buenas posibles en minusculas)
MOTIVOS = {
    "ord_1": ("o", "El primer paso de la fila: <b>primero</b>.", ["primero"]),
    "ord_2": ("o", "El paso siguiente: <b>después</b>, <b>luego</b> o <b>más tarde</b>.", ["después", "luego", "más tarde"]),
    "ord_fin": ("o", "El último paso: <b>al final</b>.", ["al final"]),
    "ord_cambio": ("o", "El plan cambió: lo que pasó de verdad va detrás de <b>al final</b>.", ["al final"]),
    "ord_ent": ("o", "En una historia, «en ese momento»: <b>entonces</b>.", ["entonces"]),
    "suma": ("s", "Otra idea del mismo lado: <b>y</b>, <b>además</b>, <b>también</b>.", ["y", "además", "también"]),
    "suma_no": ("s", "Para sumar un no: <b>tampoco</b>.", ["tampoco"]),
    "giro": ("g", "La frase va contra lo que esperas: <b>pero</b>.", ["pero"]),
    "causa": ("c", "Detrás va la causa: <b>porque</b>.", ["porque"]),
    "excusa": ("c", "Explicas tu «no» a un amigo: <b>es que</b>.", ["es que"]),
    "result": ("r", "Detrás va lo que pasa: <b>por eso</b>.", ["por eso"]),
    "result_conv": ("r", "En la conversación, lo que propones por lo que te han dicho: <b>entonces</b>.", ["entonces"]),
}
TEXTOS = [
    {"id": "bea", "tipo": "Escritura · tarea 1 · correo a una amiga", "titulo": "Correo a Bea",
     "texto": "¡Hola, Bea!<br>Gracias por invitarme a tu cumpleaños. Me encantaría ir, [[pero|además|porque#giro]] el sábado por la tarde tengo que trabajar: "
              "[[es que|por eso|además#excusa]] mi compañera está de vacaciones. ¿Qué te parece si te llevo el regalo el domingo? "
              "[[Primero|Al final|Pero#ord_1]] podemos tomar un café en tu barrio y [[después|primero|porque#ord_2]] damos un paseo por el parque. "
              "Hace mucho que no hablamos, [[por eso|porque|pero#result]] tengo muchas ganas de verte. "
              "[[Además|Pero|Porque#suma]], quiero enseñarte las fotos de mi viaje a Lisboa.<br>¡Escríbeme!<br>Un beso,<br>Inés"},
    {"id": "surf", "tipo": "Escritura · tarea 2 · blog", "titulo": "Mi primera clase de surf",
     "texto": "El sábado pasado hice mi primera clase de surf. [[Primero|Al final|Además#ord_1]], el profesor nos explicó las normas en la arena "
              "y [[luego|primero|porque#ord_2]] entramos en el agua. Yo estaba muy nervioso [[porque|por eso|pero#causa]] no nado muy bien. "
              "Me caí muchas veces, [[pero|además|porque#giro]] no me importó: ¡era muy divertido! Una vez estaba en la tabla y [[entonces|por eso|además#ord_ent]] llegó una ola enorme. "
              "[[Más tarde|Primero|Porque#ord_2]], el profesor me ayudó a ponerme de pie y, [[al final|primero|además#ord_fin]], conseguí hacer una ola entera. "
              "Quería repetir el domingo, pero [[al final|primero|además#ord_cambio]] no pude: me dolía todo el cuerpo. "
              "[[Por eso|Porque|Pero#result]] este fin de semana descanso."},
    {"id": "pilar", "tipo": "Escritura · tarea 2 · biografía", "titulo": "Pilar Soto, ceramista",
     "texto": "Pilar Soto nació en Talavera en 1975. De niña pasaba los veranos en el taller de su abuelo [[y|pero|porque#suma]] allí aprendió a hacer platos y tazas. "
              "Estudió Derecho en Madrid, [[pero|además|por eso#giro]] no le gustaba trabajar en una oficina. "
              "[[Por eso|Porque|Además#result]], en 2005 volvió a su pueblo y abrió una tienda de cerámica. "
              "[[Primero|Al final|Porque#ord_1]] vendía solo en su tienda; [[después|primero|porque#ord_2]] empezó a vender por internet. "
              "Hoy tiene clientes en toda Europa [[porque|por eso|pero#causa]] sus piezas son muy originales. "
              "[[Además|Pero|Porque#suma]], da clases a niños los sábados."},
    {"id": "cena", "tipo": "Oral · tarea 3 · planificar con un amigo", "titulo": "Una cena para el profesor",
     "texto": "<b>Examinadora:</b> ¿Organizamos una cena de despedida para el profesor?<br>"
              "<b>Candidato:</b> ¡Buena idea! ¿El viernes?<br>"
              "<b>Examinadora:</b> El viernes no puedo, [[es que|por eso|además#excusa]] tengo una boda.<br>"
              "<b>Candidato:</b> Vale, [[entonces|porque|pero#result_conv]] el jueves. ¿Tú tienes planes el jueves?<br>"
              "<b>Examinadora:</b> No, no tengo nada.<br>"
              "<b>Candidato:</b> Yo [[tampoco|también|además#suma_no]]. ¿Cenamos en un restaurante?<br>"
              "<b>Examinadora:</b> Los restaurantes del centro son caros, ¿no?<br>"
              "<b>Candidato:</b> Sí, [[pero|además|por eso#giro]] hay uno italiano que está bien de precio. [[Además|Pero|Porque#suma]], tiene una sala para grupos.<br>"
              "<b>Examinadora:</b> Perfecto. ¿Y quién reserva?<br>"
              "<b>Candidato:</b> Yo. [[Primero|Al final|Porque#ord_1]] llamo al restaurante y [[luego|primero|pero#ord_2]] escribo a los compañeros. "
              "El profesor nos ha ayudado mucho, [[por eso|porque|pero#result]] quiero darle las gracias."},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
# pautas: (texto, [focos]); focos -> flechas
FOCOS = {"orden": "ordenar", "suma": "sumar", "giro": "girar (pero)", "causa": "la causa", "result": "lo que pasa"}
FOCO_FAM = {"orden": "o", "suma": "s", "giro": "g", "causa": "c", "result": "r"}
LAMINAS = [
    {"id": "raul", "tarea": "Tarea 1 · correo a un amigo", "palabras": [60, 70], "trato": "tu",
     "intro": "Ha recibido este mensaje de su amigo Raúl:",
     "mensaje": "¡Hola! El domingo hacemos una paella en la casa de mis padres, en el pueblo. Vienen mis hermanos y algunos amigos del trabajo. ¿Te apuntas? Podemos ir juntos en mi coche. Escríbeme. Un abrazo, Raúl",
     "consigna": "Escriba un correo a Raúl. En él tiene que:",
     "pautas": [("saludar y darle las gracias por la invitación;", ["suma"]),
                ("decir que no puede ir y explicar por qué;", ["giro", "causa"]),
                ("contarle qué ha hecho este fin de semana;", ["orden"]),
                ("proponerle otro plan para otro día;", ["result"]),
                ("despedirse.", [])]},
    {"id": "cambio", "tarea": "Tarea 2 · texto para una revista", "palabras": [70, 80], "trato": "",
     "intro": "Una revista para estudiantes de español busca textos sobre este tema:",
     "mensaje": "«Un cambio importante en mi vida»",
     "consigna": "Escriba un texto para la revista. Hable de:",
     "pautas": [("qué cambio fue y cuándo pasó;", ["orden"]),
                ("cómo era su vida antes del cambio;", ["suma"]),
                ("por qué decidió cambiar;", ["causa", "result"]),
                ("qué fue difícil al principio y qué fue fácil;", ["giro"]),
                ("cómo es su vida ahora y qué piensa del cambio.", ["orden"])]},
]
# Para contar las flechas en el texto del estudiante (sin tildes, en minusculas). La y no cuenta como flecha.
CUENTA = {
    "o": r"\b(?:primero|despues|luego|mas tarde|al final|entonces)\b",
    "s": r"\b(?:ademas|tambien|tampoco)\b",
    "g": r"\bpero\b",
    "c": r"\b(?:porque|es que)\b",
    "r": r"\bpor eso\b",
}

# ------------------------------------------------------------------ DETECTOR (texto sin tildes, en minusculas)
_POS = (r"(?:buen[oa]s?|bonit[oa]s?|precios[oa]s?|genial(?:es)?|barat[oa]s?|simpatic[oa]s?|agradables?|limpi[oa]s?|tranquil[oa]s?|"
        r"comod[oa]s?|ric[oa]s?|estupend[oa]s?|me gusto|me encanto)")
_NEG = (r"(?:mal[oa]?s?|fe[oa]s?|car[oa]s?|carisim[oa]s?|antipatic[oa]s?|suci[oa]s?|ruidos[oa]s?|aburrid[oa]s?|horribles?|"
        r"incomod[oa]s?|lent[oa]s?|no me gusto)")
_NONO = r"(?:(?!\bno\b)[^.!?]){0,60}"
_TIEMPO = r"(?:llovia|llovio|nevaba|nevo|hacia (?:mucho |muy )?(?:frio|calor|viento|sol|buen tiempo|mal tiempo)|hizo (?:mucho )?(?:frio|calor|viento|sol))"
# s = se mira frase a frase (como en la pagina); x = se mira el texto entero
DETECTOR = [
    {"id": "muchas_y", "t": "a", "sc": "s", "re": r"\by\b(?:[^.!?]*\by\b){2}",
     "msg": "Hay tres <b>y</b> (o más) en la misma frase: parece una lista. Cambia alguna por una flecha: <b>después</b>, <b>además</b>, <b>al final</b>..."},
    {"id": "ademas_contra", "t": "a", "sc": "x",
     "re": r"\b" + _POS + r"\b[^.!?]{0,60}[.!?]?\s*ademas\b" + _NONO + r"\b" + _NEG + r"\b|\b" + _NEG + r"\b[^.!?]{0,60}[.!?]?\s*ademas\b" + _NONO + r"\b" + _POS + r"\b",
     "msg": "Antes de <b>además</b> hay algo bueno y detrás algo malo (o al revés). Además solo suma del mismo lado: si la frase gira, es <b>pero</b>."},
    {"id": "causa_al_reves", "t": "a", "sc": "s", "re": r"\b" + _TIEMPO + r"\s*,\s*porque\s+(?:me|nos)\b",
     "msg": "¿Has mirado la flecha? Primero dices el tiempo que hacía y después <b>porque</b> + lo que hiciste. El tiempo es la causa: <b>por eso</b>."},
    {"id": "por_eso_tiempo", "t": "a", "sc": "s", "re": r"\bpor eso\s+" + _TIEMPO + r"\b",
     "msg": "Detrás de <b>por eso</b> va lo que pasa, no la causa. ¿El tiempo es la causa? Entonces: ... <b>porque</b> hacía sol."},
    {"id": "en_el_final", "t": "r", "sc": "s", "re": r"\ben el final\b",
     "msg": "Se dice <b>al final</b>, con <i>a</i>."},
    {"id": "tambien_no", "t": "r", "sc": "s", "re": r"\btambien no\b",
     "msg": "Para sumar un no: <b>tampoco</b> (yo tampoco, a mí tampoco)."},
    {"id": "porque_pregunta", "t": "r", "sc": "s", "re": r"¿\s*porque\b",
     "msg": "Es una pregunta: <b>¿Por qué...?</b>, dos palabras y con tilde. <i>Porque</i> es para contestar."},
    {"id": "ademas_de", "t": "r", "sc": "s", "re": r"\bademas de\s*[,.;:]",
     "msg": "<b>Además de</b> necesita algo detrás (además de la cocina...). Sola, con coma: <b>Además,</b> ..."},
    {"id": "es_que_usted", "t": "a", "sc": "x",
     "re": r"^(?=(?:.|\n)*\b(?:estimad[oa]s?|usted(?:es)?|atentamente|sra?)\b)(?=(?:.|\n)*(?:[,.;:!?]|^)\s*es que\b)",
     "msg": "Es un correo de usted y hay un <b>es que</b>. Es que es de la conversación y de los correos a amigos: en un correo formal, mejor <b>porque</b>."},
    {"id": "despues_rep", "t": "a", "sc": "x", "re": r"^(?=(?:(?:.|\n)*?\bdespues\b){3})",
     "msg": "Has escrito <b>después</b> tres veces o más. Varía: <b>luego</b>, <b>más tarde</b>, <b>al final</b>."},
    {"id": "porque_rep", "t": "a", "sc": "x", "re": r"^(?=(?:(?:.|\n)*?\bporque\b){3})",
     "msg": "Has escrito <b>porque</b> tres veces o más. Prueba el espejo en alguna: <b>por eso</b>."},
]
# Pruebas: (texto, ids que tienen que saltar). El build las comprueba en Python y en node.
DETECTOR_PRUEBAS = [
    ("Fuimos a la playa y comimos y nadamos y volvimos y cenamos.", ["muchas_y"]),
    ("La comida estaba buena. Además, el camarero era antipático.", ["ademas_contra"]),
    ("El piso es muy caro y además es feo, pero tiene terraza.", []),
    ("La habitación era bonita. Además, la cama era muy incómoda.", ["ademas_contra"]),
    ("Llovía, porque me quedé en casa.", ["causa_al_reves"]),
    ("Me quedé en casa, por eso llovía.", ["por_eso_tiempo"]),
    ("En el final, compramos el sofá azul.", ["en_el_final"]),
    ("—No puedo ir. —Yo también no.", ["tambien_no"]),
    ("Estimada señora Gil: no puedo ir a la reunión, es que tengo médico. Atentamente, Pilar.", ["es_que_usted"]),
    ("¿Porque no vienes a la fiesta?", ["porque_pregunta"]),
    ("Fuimos al museo. Después comimos. Después paseamos. Después cenamos.", ["despues_rep"]),
    ("Además de, el piso tiene una terraza.", ["ademas_de"]),
    ("Estudio español porque me gusta, porque quiero viajar y porque es útil para mi trabajo.", ["porque_rep"]),
    ("Primero fuimos al museo, después comimos en el puerto y al final volvimos en tren.", []),
    ("Me quedé en casa porque llovía.", []),
    ("Llovía, por eso me quedé en casa.", []),
    ("El hotel es bonito y, además, es barato.", []),
    ("La comida estaba buena y, además, no era cara.", []),
    ("La comida estaba buena, pero el camarero era antipático.", []),
    ("Estaba cansada, porque había trabajado mucho.", []),
    ("Hacía frío porque estábamos en enero.", []),
    ("Trabajé doce horas, por eso estaba muy cansada.", []),
    ("Al final del día, estábamos muy contentos.", []),
    ("Estimada señora Gil: le escribo porque no puedo ir a la reunión. Lo malo es que tengo médico ese día. Atentamente, Pilar.", []),
    ("Yo tampoco puedo ir.", []),
    ("¿Por qué no vienes a la fiesta? Porque tengo que estudiar.", []),
    ("Además de la playa, hay un castillo muy bonito.", []),
    ("Perdona, es que no puedo ir. Un beso.", []),
    ("—No puedo el sábado. —Entonces quedamos el domingo.", []),
    ("Ana y Luis comen y después pasean.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL (cuentalo en orden)
# hechos = palabras clave (como las notas del examen); m = modelo marcado (al menos tres flechas distintas)
ORAL = [
    {"tema": "Ayer: la cena en casa de Marta", "hechos": ["llegar tarde: mucho tráfico", "cenar paella", "la tarta se cae", "ver una película"],
     "m": "Ayer cené en casa de Marta. [o:Primero] llegué tarde [c:porque] había mucho tráfico. [o:Después] cenamos una paella buenísima. [o:Luego] Marta trajo una tarta, [g:pero] se cayó al suelo. [r:Por eso] no hubo postre. [o:Al final] vimos una película en el sofá."},
    {"tema": "El sábado pasado: el mercadillo", "hechos": ["levantarse muy pronto", "comprar una lámpara", "empezar a llover", "tomar chocolate"],
     "m": "El sábado pasado fui al mercadillo. [o:Primero] me levanté muy pronto [c:porque] quería llegar antes que nadie. [o:Después] compré una lámpara antigua muy barata. [o:Más tarde] empezó a llover, [r:por eso] entré en una cafetería [s:y] tomé un chocolate con churros."},
    {"tema": "Tu primer día en el gimnasio", "hechos": ["apuntarse", "clase de spinning", "terminar muy cansado/a", "ducha y a casa"],
     "m": "El lunes me apunté a un gimnasio. [o:Primero] hice una clase de spinning. Fue muy divertida, [g:pero] muy dura: ¡terminé muy cansado! [r:Por eso] no hice nada más. [o:Al final] me duché [s:y] volví a casa andando."},
    {"tema": "Las vacaciones en Granada", "hechos": ["tren a Granada", "la Alhambra", "mucho calor; hotel sin aire acondicionado", "volver un día antes"],
     "m": "En agosto fui a Granada en tren. [o:Primero] visité la Alhambra: es preciosa. [g:Pero] hacía muchísimo calor, más de cuarenta grados. [s:Además], el hotel no tenía aire acondicionado. [r:Por eso], [o:al final], volvimos a casa un día antes."},
    {"tema": "Un examen difícil", "hechos": ["estudiar toda la semana", "muchos nervios", "no tener bolígrafo", "aprobar"],
     "m": "La semana pasada tuve un examen de inglés. [o:Primero] estudié toda la semana. El día del examen estaba muy nervioso [c:porque] era muy importante. [o:Luego], en clase, vi que no tenía bolígrafo, [g:pero] una compañera me dejó uno. [o:Al final] aprobé con un siete."},
    {"tema": "Una tarde en la playa", "hechos": ["hacer bocadillos", "nadar", "mucho viento", "volver pronto"],
     "m": "El domingo fuimos a la playa. [o:Primero] hicimos unos bocadillos [s:y] [o:después] nadamos un rato. [o:Más tarde] empezó a hacer mucho viento. [r:Por eso] volvimos a casa muy pronto, [g:pero] lo pasamos muy bien."},
    {"tema": "La fiesta sorpresa de tu madre", "hechos": ["invitar a la familia en secreto", "decorar el salón", "tu madre llega antes", "todos se ríen"],
     "m": "Para el cumpleaños de mi madre hicimos una fiesta sorpresa. [o:Primero] invité a toda la familia en secreto. [o:Después] decoramos el salón con globos. [g:Pero] mi madre llegó una hora antes [s:y] nos vio con los globos en la mano. [o:Al final] todos nos reímos mucho."},
    {"tema": "El móvil perdido", "hechos": ["salir de un bar", "no encontrar el móvil", "volver al bar", "el camarero lo tiene"],
     "m": "El viernes salí de un bar con unos amigos [s:y], en la calle, no encontré mi móvil. Estaba muy preocupada [c:porque] tenía todas mis fotos. [r:Por eso] volví al bar corriendo. [o:Al final] el camarero lo tenía: ¡qué suerte!"},
    {"tema": "Una excursión a la montaña", "hechos": ["ruta de cinco horas", "comer junto a un río", "perderse: no hay señales", "llegar de noche"],
     "m": "El sábado hicimos una ruta de cinco horas por la montaña. [o:Primero] subimos hasta un lago [s:y] comimos junto a un río. [o:Luego] nos perdimos un poco [c:porque] no había señales. [o:Al final] llegamos al coche de noche, [g:pero] muy contentos."},
    {"tema": "La cena para tus amigos", "hechos": ["receta en internet", "comprar en el mercado", "el arroz se quema", "pedir pizzas"],
     "m": "El sábado cociné para mis amigos. [o:Primero] busqué una receta de arroz en internet. [o:Después] compré todo en el mercado. [g:Pero] hablé mucho con mis amigos [s:y] el arroz se quemó. [r:Por eso] pedimos unas pizzas."},
    {"tema": "El viaje en tren a Madrid", "hechos": ["el tren sale con retraso", "una señora muy simpática", "llegar muy tarde", "ir directamente al hotel"],
     "m": "El mes pasado fui a Madrid en tren. El tren salió con una hora de retraso, [g:pero] conocí a una señora muy simpática [s:y] hablamos todo el viaje. [o:Al final] llegué muy tarde, [r:por eso] fui directamente al hotel."},
    {"tema": "Una entrevista de trabajo", "hechos": ["preparar las respuestas", "llegar media hora antes", "preguntas fáciles; jefa simpática", "te llaman: ¡el trabajo es tuyo!"],
     "m": "Ayer tuve una entrevista de trabajo. [o:Primero] preparé las respuestas en casa. [o:Después] llegué media hora antes [c:porque] no quería llegar tarde. Las preguntas fueron fáciles [s:y], [s:además], la jefa era muy simpática. [o:Al final], hoy me han llamado: ¡tengo el trabajo!"},
]
