# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R06: PREPOSICIONES FRECUENTES (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R06_preposiciones.py
#
# ENFOQUE COGNITIVO (aprobado por Maria, 14/10): EL MAPA DEL VIAJE
#   Cada preposicion es una pieza de un viaje dibujado en un plano; el mismo dibujo sirve para el
#   espacio y para el tiempo.
#   A      = LA FLECHA que llega a un punto: voy a Madrid, a las cinco, veo a mi madre.
#   EN     = LA CAJA: estas dentro del sitio, del vehiculo o del periodo: en casa, en tren, en mayo.
#            Por eso "a pie / andando": no vas dentro de nada. CON es una persona (voy con Ana).
#   DE...A / DESDE...HASTA = LA LINEA: de donde sale y donde termina; los dos extremos van en pareja
#            (de 9 a 2, desde las 9 hasta las 2). DE solo = de donde sale (soy de, vengo de).
#   POR    = LA ZONA por donde pasas, sin punto exacto (por el parque, por la manana) y lo que esta
#            DETRAS de algo (gracias por, por eso). Tambien el camino de un mensaje (por telefono).
#   PARA   = LA DIANA, la meta que esta DELANTE: para ti, para aprender, para el viernes.
#   Truco: POR mira hacia atras (el camino, la causa); PARA mira hacia delante (la meta).
#
# MARCAS
#   [a:a Madrid]  la flecha (azul)       [e:en tren]   la caja (turquesa)
#   [l:de 9 a 2]  la linea (ambar)       [p:por la manana]  por (violeta)   [m:para ti]  para (coral)
#   Huecos: [[correcta|distractor|distractor#motivo]]  (la primera es la buena; se barajan)
# Espanol de Espana. Ejemplos propios (ninguno sale de los materiales de Maria).

# ------------------------------------------------------------------ MOTIVOS
# clave: (familia, explicacion, respuestas buenas posibles). La familia decide el color.
MOTIVOS = {
    "destino":  ("flecha", "Te mueves hacia un sitio (ir, venir, llegar, volver): la flecha, <b>a</b>. Y a + el = <b>al</b>.", ["a", "al"]),
    "hora":     ("flecha", "Una hora exacta es un punto del reloj: la flecha llega ahí, <b>a</b> las cinco.", ["a"]),
    "persona":  ("flecha", "La flecha también apunta a personas: llamo <b>a</b> mi madre, veo <b>a</b> Pedro.", ["a", "al"]),
    "dentro":   ("caja", "No hay movimiento: estás <b>dentro</b> del sitio (estar, vivir, trabajar, quedar): <b>en</b>.", ["en"]),
    "vehiculo": ("caja", "Vas dentro del vehículo: <b>en</b> tren, <b>en</b> coche, <b>en</b> metro. Nunca «con tren».", ["en"]),
    "periodo":  ("caja", "Un mes, una estación o un año son una caja grande del calendario: <b>en</b> agosto, <b>en</b> verano.", ["en"]),
    "a_pie":    ("caja", "Sin vehículo no estás dentro de nada: <b>a pie</b> (o andando). Nunca «en pie».", ["a"]),
    "origen":   ("linea", "El principio de la línea: de dónde sales o de dónde eres, <b>de</b> (de + el = <b>del</b>).", ["de", "del"]),
    "de_a":     ("linea", "Los dos extremos van en pareja: <b>de</b>... <b>a</b> (de 9 a 2, de lunes a viernes).", ["de", "a", "al"]),
    "desde_hasta": ("linea", "Los dos extremos van en pareja: <b>desde</b>... <b>hasta</b> (desde las 9 hasta las 2).", ["desde", "hasta"]),
    "hasta":    ("linea", "El final de la línea, donde paras: <b>hasta</b> el final, <b>hasta</b> la plaza.", ["hasta"]),
    "zona":     ("por", "Una zona por donde pasas, sin punto exacto: <b>por</b> el centro, <b>por</b> la mañana.", ["por"]),
    "causa":    ("por", "Lo que está <b>detrás</b> (la causa): gracias <b>por</b>, <b>por</b> eso, <b>por</b> la lluvia.", ["por"]),
    "camino":   ("por", "El camino del mensaje: <b>por</b> teléfono, <b>por</b> correo, <b>por</b> internet.", ["por"]),
    "meta_persona": ("para", "La meta es una persona, el destinatario: es <b>para</b> ti.", ["para"]),
    "meta_fin": ("para", "La meta está delante: el objetivo, <b>para</b> + infinitivo (para aprender).", ["para"]),
    "meta_fecha": ("para", "La meta en el calendario, el día límite: <b>para</b> el viernes.", ["para"]),
}
FAMILIAS = {"flecha": "a: la flecha", "caja": "en: la caja", "linea": "de... a: la línea", "por": "por: zona y causa", "para": "para: la meta"}

# ------------------------------------------------------------------ 1. EL MAPA
# Parejas: dos frases que se parecen y un dibujo para cada una.
# k = tipo de dibujo: a (flecha), en (caja), l (linea), p (zona), m (diana), pie (andando)
# la / lb = rotulos del dibujo (para l: "principio|final")
PAREJAS = [
    {"tema": "voy a / estoy en",
     "a": "El sábado voy [a:a Valencia].", "ka": "a", "la": "Valencia",
     "ea": "<i>Ir</i> es movimiento: la flecha sale de ti y llega a Valencia. <b>A</b> = adónde vas.",
     "b": "Mi hermana vive [e:en Valencia].", "kb": "en", "lb": "Valencia",
     "eb": "<i>Vivir</i> no es movimiento: estás dentro del sitio. <b>En</b> = dónde estás."},
    {"tema": "en tren / a pie",
     "a": "Voy a clase [e:en tren].", "ka": "en", "la": "tren",
     "ea": "Vas <b>dentro</b> del tren: es una caja que se mueve. Igual: en coche, en metro, en bici.",
     "b": "Hoy voy a clase [a:a pie].", "kb": "pie", "lb": "a pie",
     "eb": "No hay vehículo: no estás dentro de nada. Por eso <b>a pie</b> (o <i>andando</i>), nunca «en pie»."},
    {"tema": "a las diez / en octubre",
     "a": "La clase empieza [a:a las diez].", "ka": "a", "la": "10:00",
     "ea": "Una hora exacta es un <b>punto</b> del reloj: la flecha llega ahí.",
     "b": "El curso empieza [e:en octubre].", "kb": "en", "lb": "octubre",
     "eb": "Un mes es un <b>trozo</b> grande del calendario: una caja. En octubre, en verano, en 2026."},
    {"tema": "a las nueve / de nueve a dos",
     "a": "La tienda abre [a:a las nueve].", "ka": "a", "la": "9:00",
     "ea": "Un solo momento: la hora en que abre. La flecha, <b>a</b>.",
     "b": "La tienda abre [l:de nueve a dos].", "kb": "l", "lb": "9:00|14:00",
     "eb": "Ahora es una <b>línea</b> con dos extremos: dónde empieza y dónde termina. <b>De</b> va con <b>a</b>."},
    {"tema": "al parque / por el parque",
     "a": "Los domingos vamos [a:al parque].", "ka": "a", "la": "parque",
     "ea": "El parque es el destino: la flecha llega allí. A + el = <b>al</b>.",
     "b": "Los domingos paseamos [p:por el parque].", "kb": "p", "lb": "parque",
     "eb": "El parque es una <b>zona</b> por donde pasas: entras, das vueltas, sales. <b>Por</b>."},
    {"tema": "gracias por / es para",
     "a": "Gracias [p:por el regalo].", "ka": "p", "la": "el regalo",
     "ea": "El regalo está <b>detrás</b> de tu «gracias»: es la causa. Por mira hacia atrás.",
     "b": "El regalo es [m:para ti].", "kb": "m", "lb": "ti",
     "eb": "Tú eres la <b>meta</b> del regalo, el destinatario. Para mira hacia delante."},
]

# El verbo te ayuda: (titulo, clase, ejemplos marcados)
VERBOS = [
    ("Movimiento → a", "flecha", ["voy [a:a Bilbao]", "llego [a:a casa] a las seis", "vuelvo [a:al trabajo]", "viajo [a:a Roma] en mayo"]),
    ("Sin movimiento → en", "caja", ["estoy [e:en casa]", "vivo [e:en Elche]", "trabajo [e:en un hotel]", "quedamos [e:en la plaza]"]),
    ("Origen → de", "linea", ["soy [l:de Perú]", "vengo [l:del médico]", "salgo [l:de clase] a las dos"]),
    ("Con quién → con", "con", ["voy al cine con Ana", "vivo con mis padres", "quedo con unos amigos"]),
]

# Avisos (cierres): (titulo, bien marcado, mal, explicacion)
CIERRES = [
    ("Con es una persona; en, el vehículo", "Voy a la playa [e:en coche] con Marta.", "Voy con coche.",
     "<b>Con</b> dice con quién vas. El vehículo es una caja: <b>en</b>."),
    ("A + el = al · de + el = del", "Voy [a:al cine]. Vengo [l:del cine].", "Voy a el cine.",
     "Delante de <i>el</i>, <b>a</b> y <b>de</b> se juntan: al, del. Con <i>la</i>, no: a la playa, de la playa."),
    ("Casa, sin artículo", "Voy [a:a casa]. Estoy [e:en casa].", "Estoy a casa.",
     "Con <i>casa</i> (la tuya) no hay artículo. Y sigue la regla: ir <b>a</b>, estar <b>en</b>."),
    ("Los días, sin nada", "El lunes voy al médico. Este sábado trabajo.", "En el lunes voy al médico.",
     "Con los días y las fechas no hay preposición: <b>el lunes</b>, <b>el 3 de mayo</b>, <b>este sábado</b>."),
]

# Monta tu plan (la frase de la tarea 3): Quedamos {donde} {hora} y vamos {como} {destino}.
PLAN = {
    "donde": ["[e:en la puerta del cine]", "[e:en la plaza Mayor]", "[e:en mi casa]"],
    "hora": ["[a:a las ocho]", "[a:a las siete y media]", "[a:a mediodía]"],
    "como": ["[e:en metro]", "[e:en bici]", "[a:a pie]", "andando"],
    "destino": ["[a:al concierto]", "[a:a la playa]", "[a:a casa de Lucía]"],
}
PLAN_WHY = {
    "donde": "<b>Dónde quedáis</b>: un sitio donde estáis, sin movimiento. La caja, <b>en</b>.",
    "hora": "<b>A qué hora</b>: un punto del reloj. La flecha, <b>a</b>.",
    "como": "<b>Cómo vais</b>: dentro de un vehículo, <b>en</b>; sin vehículo, <b>a pie</b> o <b>andando</b>.",
    "destino": "<b>Adónde vais</b>: el destino. La flecha, <b>a</b> (a + el = al).",
}

# ------------------------------------------------------------------ 2. EL RELOJ
# (titulo, clase, ejemplos marcados, explicacion)
RELOJ = [
    ("A + la hora exacta", "flecha", ["[a:a las cinco]", "[a:a las ocho y media]", "[a:a mediodía]"],
     "Un punto del reloj: la flecha llega ahí. ¿A qué hora? A las cinco."),
    ("EN + un mes, una estación, un año", "caja", ["[e:en mayo]", "[e:en verano]", "[e:en 2019]", "[e:en Navidad]"],
     "Un trozo grande del calendario: estás dentro. ¿Cuándo? En verano."),
    ("POR + una parte del día", "por", ["[p:por la mañana]", "[p:por la tarde]", "[p:por la noche]"],
     "Una zona del día, sin hora exacta. En España: <b>por</b> la mañana, nunca «a la mañana» ni «en la mañana»."),
    ("Con la hora: DE la mañana", "linea", ["a las ocho [l:de la mañana]", "a las diez [l:de la noche]"],
     "Si dices la hora, la parte del día va con <b>de</b>: a las ocho de la mañana."),
    ("DE... A · DESDE... HASTA", "linea", ["[l:de nueve a dos]", "[l:de lunes a viernes]", "[l:desde las nueve hasta las dos]"],
     "Una línea con principio y final. Las parejas no se mezclan: nunca «de 9 hasta 2» ni «desde 9 a 2»."),
    ("PARA + el día límite", "para", ["[m:para el viernes]", "[m:para mañana]"],
     "La meta en el calendario: tiene que estar hecho antes de ese día."),
    ("Sin nada: los días y las fechas", "nada", ["el lunes", "este sábado", "el 3 de mayo", "mañana"],
     "Con los días y las fechas no hay preposición: el lunes voy al médico."),
]

# ------------------------------------------------------------------ 3. POR Y PARA
# Frases del selector: f (marcada), k ("p" o "m"), uso, explicacion
POR_PARA = [
    {"f": "Damos un paseo [p:por el centro].", "k": "p", "uso": "la zona", "why": "El centro es una zona por donde pasas, sin un punto exacto."},
    {"f": "[p:Por la noche] leo un rato.", "k": "p", "uso": "la zona del día", "why": "Una parte del día sin hora exacta: también es una zona."},
    {"f": "Gracias [p:por la cena].", "k": "p", "uso": "la causa", "why": "La cena está detrás de tu «gracias»: es la causa."},
    {"f": "Llovía mucho; [p:por eso] no salimos.", "k": "p", "uso": "la causa", "why": "<i>Por eso</i> mira hacia atrás, a la causa que ya has dicho."},
    {"f": "Te llamo [p:por teléfono].", "k": "p", "uso": "el camino", "why": "El mensaje pasa por el teléfono: es el camino."},
    {"f": "Este pastel es [m:para ti].", "k": "m", "uso": "la persona", "why": "Tú eres la meta: el pastel llega a ti."},
    {"f": "Estudio español [m:para trabajar en Madrid].", "k": "m", "uso": "el objetivo", "why": "Trabajar en Madrid es la meta que tienes delante."},
    {"f": "Tengo que terminar el informe [m:para el lunes].", "k": "m", "uso": "el día límite", "why": "El lunes es la meta en el calendario."},
]

# ------------------------------------------------------------------ 4. EN EL EXAMEN
DONDE = [
    ("Oral · tarea 3 (diálogo)", "Planificar algo con el examinador: dónde y a qué hora quedáis, cómo vais, adónde.",
     "Quedamos [e:en la puerta del cine] [a:a las ocho] y vamos [e:en metro], ¿vale?"),
    ("Oral · tarea 1 (monólogo)", "Tu rutina, tu trabajo, un viaje: cómo vas, tu horario, adónde fuiste.",
     "Cada día voy [a:al trabajo] [e:en bici] y trabajo [l:de nueve a cinco]."),
    ("Oral · tarea 2 (foto)", "¿Dónde están? ¿Qué hora es, más o menos?",
     "Están [e:en una cafetería]; creo que es domingo [p:por la tarde]."),
    ("Escritura · tarea 1 (correo)", "Quedar con un amigo, dar indicaciones para llegar a tu casa, contar un plan.",
     "Mi casa está [e:en la calle del Sol]; [l:desde la estación] son diez minutos [a:a pie]."),
    ("Escritura · tarea 2 (blog, diario)", "Tu semana, tus estudios, un viaje: por la mañana, de... a, para qué.",
     "[p:Por la mañana] estudio y [p:por la tarde] trabajo [m:para ahorrar] un poco."),
    ("Auditiva y lectura (horarios, anuncios)", "La respuesta suele ser una hora exacta o los dos extremos de un horario: escucha los dos.",
     "Abierto [l:de lunes a sábado], [l:de 10 a 20 h]. Cerrado [e:en agosto]."),
]
# Errores tipicos: (mal, bien marcado, porque)
ERRORES = [
    ("El viernes voy en Madrid.", "El viernes voy [a:a Madrid].", "<i>Ir</i> es movimiento: la flecha, <b>a</b>. <i>En</i> es para estar dentro."),
    ("Hoy estoy a casa todo el día.", "Hoy estoy [e:en casa] todo el día.", "<i>Estar</i> no es movimiento: la caja, <b>en</b>."),
    ("Voy al trabajo con tren.", "Voy al trabajo [e:en tren].", "El vehículo es una caja: <b>en</b>. <i>Con</i> es para personas."),
    ("Si hace buen tiempo, voy en pie.", "Si hace buen tiempo, voy [a:a pie] (o andando).", "Sin vehículo: <b>a pie</b>, una expresión fija."),
    ("La tienda abre de 9 hasta 2.", "La tienda abre [l:de 9 a 2].", "<b>De</b> va con <b>a</b>: las parejas no se mezclan."),
    ("Trabajo desde las 9 a las 2.", "Trabajo [l:desde las 9 hasta las 2].", "<b>Desde</b> va con <b>hasta</b>."),
    ("Gracias para tu invitación.", "Gracias [p:por tu invitación].", "La invitación está detrás de tu «gracias»: la causa, <b>por</b>."),
    ("Este regalo es por ti.", "Este regalo es [m:para ti].", "Tú eres la meta del regalo: <b>para</b>."),
    ("Voy a clase por aprender español.", "Voy a clase [m:para aprender] español.", "Aprender es el objetivo, la meta: <b>para</b> + infinitivo."),
    ("Trabajo a la mañana.", "Trabajo [p:por la mañana].", "Una parte del día es una zona: <b>por</b> la mañana."),
    ("En la mañana voy al gimnasio.", "[p:Por la mañana] voy al gimnasio.", "En España: <b>por</b> la mañana, por la tarde, por la noche."),
]
# Claves de los errores pedidos por Maria (el build comprueba que salen en todas partes)
REQ = ["en madrid", "a casa", "con tren", "en pie", "de 9 hasta", "desde las 9 a", "gracias para", "es por ti", "por aprender", "a la mañana", "en la mañana"]

# ------------------------------------------------------------------ EJERCICIOS DE OPCION MULTIPLE
# q (con un ____), o (la PRIMERA es la buena), why
P_PREP = [
    {"q": "Mañana voy ____ Bilbao a ver a mis primos.", "o": ["a", "en", "de"], "why": "<i>Ir</i> es movimiento: la flecha llega a Bilbao, <b>a</b>."},
    {"q": "Mi hermana vive ____ Sevilla desde hace dos años.", "o": ["en", "a", "por"], "why": "<i>Vivir</i> no es movimiento: estás dentro, <b>en</b>."},
    {"q": "Siempre voy al trabajo ____ metro.", "o": ["en", "con", "por"], "why": "Vas dentro del metro: <b>en</b>. Con es para personas."},
    {"q": "El museo está cerca: podemos ir ____ pie.", "o": ["a", "en", "de"], "why": "Sin vehículo: <b>a pie</b>."},
    {"q": "La película empieza ____ las nueve y media.", "o": ["a", "en", "por"], "why": "Una hora exacta es un punto: <b>a</b> las nueve y media."},
    {"q": "Mis padres se casaron ____ 1995.", "o": ["en", "a", "de"], "why": "Un año es una caja grande del calendario: <b>en</b> 1995."},
    {"q": "—¿____ dónde eres? —De Ourense.", "o": ["De", "A", "En"], "why": "El origen, el principio de la línea: <b>de</b>."},
    {"q": "La biblioteca abre de lunes ____ viernes.", "o": ["a", "hasta", "en"], "why": "<b>De</b> va con <b>a</b>: de lunes a viernes."},
    {"q": "Estuvimos en la playa desde las diez ____ las dos.", "o": ["hasta", "a", "por"], "why": "<b>Desde</b> va con <b>hasta</b>."},
    {"q": "Los sábados ____ la mañana voy al mercado.", "o": ["por", "en", "a"], "why": "Una parte del día es una zona: <b>por</b> la mañana."},
    {"q": "Cuando llegues ____ la estación, llámame.", "o": ["a", "en", "por"], "why": "<i>Llegar</i> es movimiento: <b>a</b> la estación."},
    {"q": "Esta noche llamo ____ mi abuela.", "o": ["a", "en", "de"], "why": "La flecha también apunta a personas: llamo <b>a</b> mi abuela."},
    {"q": "Vengo ____ Madrid: he estado allí tres días.", "o": ["de", "en", "por"], "why": "De dónde vienes, el principio de la línea: <b>de</b>."},
    {"q": "Ponte el abrigo: estamos ____ invierno.", "o": ["en", "a", "por"], "why": "Una estación es una caja: <b>en</b> invierno."},
    {"q": "¿Vamos ____ coche o en tren?", "o": ["en", "con", "a"], "why": "Dentro del coche: <b>en</b>."},
    {"q": "Quedamos ____ la plaza a las ocho.", "o": ["en", "a", "por"], "why": "Dónde quedáis es un sitio donde estáis: <b>en</b> la plaza."},
]
P_PP = [
    {"q": "Gracias ____ el regalo: me encanta.", "o": ["por", "para", "a"], "why": "El regalo es la causa, está detrás: <b>por</b>."},
    {"q": "Este pastel es ____ tu madre.", "o": ["para", "por", "a"], "why": "Tu madre es la meta, la destinataria: <b>para</b>."},
    {"q": "Estudio español ____ trabajar en un hotel.", "o": ["para", "por", "a"], "why": "Trabajar en un hotel es el objetivo: <b>para</b> + infinitivo."},
    {"q": "Envíame el trabajo ____ el viernes, por favor.", "o": ["para", "por", "en"], "why": "El viernes es el día límite, la meta: <b>para</b>."},
    {"q": "Los domingos paseo ____ el centro.", "o": ["por", "para", "a"], "why": "El centro es una zona por donde pasas: <b>por</b>."},
    {"q": "____ la noche veo una serie.", "o": ["Por", "Para", "En"], "why": "Una parte del día: <b>por</b> la noche."},
    {"q": "Llovía mucho; ____ eso nos quedamos en casa.", "o": ["por", "para", "en"], "why": "<b>Por eso</b> mira hacia atrás, a la causa."},
    {"q": "Te llamo ____ teléfono esta tarde.", "o": ["por", "para", "en"], "why": "El mensaje pasa por el teléfono: <b>por</b>."},
    {"q": "Ahorro dinero ____ comprar una bici.", "o": ["para", "por", "a"], "why": "Comprar una bici es la meta: <b>para</b>."},
    {"q": "Perdona ____ llegar tarde.", "o": ["por", "para", "a"], "why": "Llegar tarde es la causa de tu «perdona»: <b>por</b>."},
    {"q": "Vamos al parque ____ jugar al fútbol.", "o": ["para", "por", "en"], "why": "Jugar al fútbol es el objetivo: <b>para</b>."},
    {"q": "El autobús 4 pasa ____ la plaza Mayor.", "o": ["por", "para", "en"], "why": "El autobús pasa por esa zona y sigue: <b>por</b>."},
]
# Bien o mal: ok = 0 (bien) o 1 (mal); fix solo en las malas
E_BIENMAL = [
    {"q": "El viernes voy en Madrid.", "ok": 1, "fix": "El viernes voy <b>a</b> Madrid.", "why": "Movimiento: <i>a</i>."},
    {"q": "Hoy estoy a casa todo el día.", "ok": 1, "fix": "Hoy estoy <b>en</b> casa todo el día.", "why": "Estar: <i>en</i>."},
    {"q": "Voy al trabajo con tren.", "ok": 1, "fix": "Voy al trabajo <b>en</b> tren.", "why": "El vehículo: <i>en</i>."},
    {"q": "Si hace buen tiempo, voy en pie.", "ok": 1, "fix": "Si hace buen tiempo, voy <b>a pie</b>.", "why": "Sin vehículo: <i>a pie</i>."},
    {"q": "La tienda abre de 9 hasta 2.", "ok": 1, "fix": "La tienda abre de 9 <b>a</b> 2.", "why": "De va con a."},
    {"q": "Trabajo desde las 9 a las 2.", "ok": 1, "fix": "Trabajo desde las 9 <b>hasta</b> las 2.", "why": "Desde va con hasta."},
    {"q": "Gracias para tu invitación.", "ok": 1, "fix": "Gracias <b>por</b> tu invitación.", "why": "La causa: <i>por</i>."},
    {"q": "Este regalo es por ti.", "ok": 1, "fix": "Este regalo es <b>para</b> ti.", "why": "La meta, el destinatario: <i>para</i>."},
    {"q": "Voy a clase por aprender español.", "ok": 1, "fix": "Voy a clase <b>para</b> aprender español.", "why": "El objetivo: <i>para</i> + infinitivo."},
    {"q": "Trabajo a la mañana.", "ok": 1, "fix": "Trabajo <b>por</b> la mañana.", "why": "Una parte del día: <i>por</i>."},
    {"q": "En la mañana voy al gimnasio.", "ok": 1, "fix": "<b>Por</b> la mañana voy al gimnasio.", "why": "En España: <i>por</i> la mañana."},
    {"q": "Llego a casa a las siete de la tarde.", "ok": 0, "fix": "", "why": "Correcto: llegar <i>a</i>, la hora con <i>a</i> y la parte del día con <i>de</i>."},
    {"q": "Voy al cine con Ana en metro.", "ok": 0, "fix": "", "why": "Correcto: <i>con</i> la persona, <i>en</i> el vehículo."},
    {"q": "Mi madre vive en un pueblo de Teruel.", "ok": 0, "fix": "", "why": "Correcto: vivir <i>en</i>."},
    {"q": "Necesito el informe para el lunes.", "ok": 0, "fix": "", "why": "Correcto: el día límite, <i>para</i>."},
    {"q": "Gracias por venir a mi fiesta.", "ok": 0, "fix": "", "why": "Correcto: la causa, <i>por</i> (también con infinitivo)."},
]

# ------------------------------------------------------------------ TEXTOS CON HUECOS (pueden llevar <br> y <b>)
TEXTOS = [
    {"id": "quedar", "tipo": "Escritura · tarea 1 · correo a un amigo", "titulo": "¿Quedamos el sábado?",
     "texto": "¡Hola, Álex! Gracias [[por|para|a#causa]] tu mensaje. Este sábado hay un concierto de jazz [[en|a|por#dentro]] el parque del Retiro. "
              "Empieza [[a|en|por#hora]] las ocho. ¿Quedamos [[en|a|por#dentro]] la puerta del parque [[a|en|por#hora]] las siete y media? "
              "Yo trabajo desde las diez [[hasta|a|en#desde_hasta]] las seis, así que antes no puedo. Podemos ir [[en|con|a#vehiculo]] metro: es rápido. "
              "Después cenamos algo [[por|para|a#zona]] el centro. ¡Ah! El domingo es el cumpleaños de Marta: he comprado un libro [[para|por|a#meta_persona]] ella. "
              "Esta noche llamo [[a|en|por#persona]] su hermano para organizar la fiesta. Un abrazo, Nerea"},
    {"id": "llegar", "tipo": "Escritura · tarea 1 · correo con indicaciones", "titulo": "Cómo llegar a mi casa",
     "texto": "Hola, Paula: así llegas [[a|en|por#destino]] mi casa. El autobús 12 sale [[de|en|por#origen]] la puerta de la estación y para delante de mi portal. "
              "Si hace bueno, puedes venir [[a|en|de#a_pie]] pie: son quince minutos. Cruzas el parque y sigues [[por|para|en#zona]] la calle del Sol [[hasta|a|en#hasta]] el final. "
              "Mi casa está [[en|a|por#dentro]] la plaza de la Fuente, número 4. Vivo [[en|a|de#dentro]] el tercer piso. "
              "Yo llego del trabajo [[a|en|por#hora]] las seis, así que ven después. Trae el bañador [[para|por|a#meta_fin]] ir a la piscina el domingo. ¡Un beso! Inés"},
    {"id": "horario", "tipo": "Lectura · anuncio con horarios", "titulo": "Biblioteca del barrio",
     "texto": "<b>Biblioteca San Blas</b><br>Horario: de lunes [[a|hasta|en#de_a]] viernes, de 9:00 [[a|hasta|por#de_a]] 21:00. "
              "Sábados: desde las 10:00 [[hasta|a|en#desde_hasta]] las 14:00. Cerrado [[en|a|por#periodo]] agosto. En julio, abierto solo [[por|en|a#zona]] la mañana.<br>"
              "Taller de cuentos [[para|por|a#meta_persona]] niños de 4 a 8 años: los miércoles [[a|en|por#hora]] las 17:30. "
              "Inscripción [[en|a|por#dentro]] la recepción o [[por|para|en#camino]] teléfono. Los libros del préstamo hay que devolverlos [[para|por|en#meta_fecha]] la fecha de la etiqueta."},
    {"id": "dialogo", "tipo": "Oral · tarea 3 · diálogo con un amigo", "titulo": "Planes para el cine",
     "texto": "<b>Examinador:</b> ¿Vamos al cine este fin de semana?<br>"
              "<b>Candidato:</b> ¡Vale! ¿Quedamos el sábado [[por|en|a#zona]] la tarde?<br>"
              "<b>Examinador:</b> Perfecto. ¿A qué hora?<br>"
              "<b>Candidato:</b> La película es [[a|en|por#hora]] las seis. ¿Quedamos a las cinco y media [[en|a|por#dentro]] la puerta del cine?<br>"
              "<b>Examinador:</b> Muy bien. ¿Y cómo vamos? Yo no tengo coche.<br>"
              "<b>Candidato:</b> Podemos ir [[en|con|a#vehiculo]] autobús. O [[a|en|de#a_pie]] pie: desde mi casa son veinte minutos.<br>"
              "<b>Examinador:</b> Mejor andando. ¿Compramos las entradas [[por|para|en#camino]] internet?<br>"
              "<b>Candidato:</b> Sí, ahora las compro. Y una entrada más [[para|por|a#meta_persona]] Óscar, ¿no?<br>"
              "<b>Examinador:</b> ¡Claro! Gracias [[por|para|a#causa]] organizarlo.<br>"
              "<b>Candidato:</b> ¡De nada! [[Para|Por|En#meta_fin]] llegar a tiempo, salgo de casa a las cinco."},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
# pautas: (texto, [focos]) con focos flecha, caja, linea, por, para
LAMINAS = [
    {"id": "quedar", "tarea": "Tarea 1 · correo a un amigo", "palabras": [60, 70],
     "intro": "Has recibido este mensaje de tu amigo Rubén:",
     "mensaje": "¡Hola! Este sábado estoy libre por fin. Trabajo por la mañana, pero por la tarde puedo. ¿Hacemos algo juntos? ¿Qué te apetece? Dime algo. Rubén",
     "consigna": "Escribe un correo a Rubén. En él tienes que:",
     "pautas": [("saludar;", []),
                ("proponer un plan: qué hacéis y adónde vais;", ["flecha"]),
                ("decir dónde y a qué hora quedáis;", ["caja", "flecha"]),
                ("explicar cómo vais a ir;", ["caja"]),
                ("despedirte.", [])]},
    {"id": "semana", "tarea": "Tarea 2 · opción 1 · blog", "palabras": [70, 80],
     "intro": "", "mensaje": "",
     "consigna": "Escribe una entrada para tu blog: «Mi semana». Habla de:",
     "pautas": [("dónde vives y dónde trabajas o estudias;", ["caja"]),
                ("cómo vas cada día;", ["caja"]),
                ("tu horario: de qué hora a qué hora trabajas o estudias;", ["linea"]),
                ("qué haces por la mañana, por la tarde y el fin de semana;", ["por"]),
                ("para qué estudias español.", ["para"])]},
]
FOCOS = {"flecha": "a", "caja": "en", "linea": "de... a", "por": "por", "para": "para"}

# Detector de errores tipicos (sobre el texto sin tildes y en minusculas).
# t: "r" (rojo: casi seguro un error) o "a" (ambar: mira si es un error)
_MOVE = (r"(?:voy|vas|va|vamos|vais|van|ir|fui|fuiste|fue|fuimos|fueron|iba|ibamos|iban|llego|llegas|llega|llegamos|llegan|llegar|"
         r"vuelvo|vuelves|vuelve|volvemos|vuelven|volver|vengo|vienes|viene|venimos|vienen|venir|viajo|viaja|viajamos|viajan|viajar)")
_CITY = (r"(?:madrid|barcelona|valencia|sevilla|alicante|bilbao|malaga|granada|zaragoza|murcia|elche|cadiz|toledo|salamanca|"
         r"espana|francia|italia|alemania|portugal|inglaterra|londres|paris|roma|berlin|lisboa)")
_VEH = r"(?:coche|tren|autobus|bus|metro|avion|barco|bici|bicicleta|moto|taxi|tranvia|furgoneta|patinete)"
_NUM = r"(?:\d{1,2}|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce)"
_DAY = r"(?:lunes|martes|miercoles|jueves|viernes|sabado|domingo)"
_PLACE = r"(?:cine|centro|trabajo|parque|mercado|colegio|gimnasio|aeropuerto|hospital|museo|supermercado|teatro|pueblo|campo|bar|restaurante|medico)"
DETECTOR = [
    {"id": "ir_en", "t": "r",
     "re": r"\b" + _MOVE + r"\s+en\s+(" + _CITY + r"|casa|clase)\b|\b" + _MOVE + r"\s+en\s+(el|la)\s+(?!" + _VEH + r"\b|manana\b|tarde\b|noche\b|semana\b|mes\b)[a-z]+",
     "msg": "Con <b>ir, venir, llegar o volver</b> hay movimiento: la flecha, <b>a</b> (voy a Madrid, vuelvo a casa). <i>En</i> es para estar dentro o para el vehículo."},
    {"id": "estar_a", "t": "r",
     "re": r"\b(estoy|estas|esta|estamos|estais|estan|estaba|estabamos|estuve|estuvimos|vivo|vives|vive|vivimos|viven|vivia|trabajo|trabajas|trabaja|trabajamos|trabajan|quedamos)\s+(a\s+(casa|clase|" + _CITY + r")|al\s+" + _PLACE + r")\b",
     "msg": "Con <b>estar, vivir, trabajar o quedar</b> no hay movimiento: la caja, <b>en</b> (estoy en casa, vivo en Elche)."},
    {"id": "con_vehiculo", "t": "r",
     "re": r"\bcon\s+" + _VEH + r"\b",
     "msg": "El vehículo es una caja: <b>en</b> tren, <b>en</b> coche. <i>Con</i> es para personas (voy con Ana)."},
    {"id": "con_el_vehiculo", "t": "a",
     "re": r"\bcon\s+(el|la)\s+" + _VEH + r"\b",
     "msg": "¿Hablas de cómo vas? Entonces es <b>en</b>: voy en el coche de mi padre, vamos en la moto."},
    {"id": "en_pie", "t": "r",
     "re": r"\b" + _MOVE + r"\s+en\s+pie\b",
     "msg": "Sin vehículo se dice <b>a pie</b> (o <b>andando</b>), nunca «en pie»."},
    {"id": "de_hasta", "t": "r",
     "re": r"\bde\s+((las|la)\s+)?" + _NUM + r"(:\d\d|\s+y\s+media|\s+y\s+cuarto)?\s+hasta\b|\bde\s+" + _DAY + r"\s+hasta\b",
     "msg": "Las parejas no se mezclan: <b>de</b>... <b>a</b> (de 9 a 2) o <b>desde</b>... <b>hasta</b> (desde las 9 hasta las 2)."},
    {"id": "desde_a", "t": "r",
     "re": r"\bdesde\s+((las|la)\s+)?" + _NUM + r"(:\d\d|\s+y\s+media|\s+y\s+cuarto)?\s+a\s+((las|la)\s+)?" + _NUM + r"\b|\bdesde\s+(el\s+)?" + _DAY + r"\s+(a|al)\s+" + _DAY + r"\b",
     "msg": "Las parejas no se mezclan: <b>desde</b> va con <b>hasta</b> (desde las 9 hasta las 2); <b>de</b> va con <b>a</b>."},
    {"id": "gracias_para", "t": "r",
     "re": r"\bgracias\s+para\b",
     "msg": "Lo que agradeces está detrás, es la causa: gracias <b>por</b>."},
    {"id": "es_por_persona", "t": "a",
     "re": r"\b(es|son|sera|era)\s+por\s+(ti|usted|ustedes|vosotros|vosotras|ella|ellos|ellas|mi(?=\s*([.,;:!?]|$)))\b",
     "msg": "¿Hablas de a quién va un regalo o una cosa? Entonces es <b>para</b>: es para ti."},
    {"id": "por_fin", "t": "r",
     "re": r"\b(?!gracias\b|perdon\b|perdona\b|perdone\b|disculpa\b|disculpe\b|enhorabuena\b|felicito\b)[a-z]+\s+por\s+(aprender|mejorar|practicar|aprobar|ahorrar|conocer)\b",
     "msg": "¿Es tu objetivo? Entonces es <b>para</b> + infinitivo: estudio <b>para</b> aprender."},
    {"id": "manana", "t": "r",
     "re": r"\b(a|en)\s+la\s+(manana|tarde|noche)\b(?!\s+(siguiente|anterior|de)\b)",
     "msg": "En España, una parte del día va con <b>por</b>: por la mañana, por la tarde, por la noche. (Con la hora: a las ocho <b>de</b> la mañana.)"},
    {"id": "en_hora", "t": "r",
     "re": r"\ben\s+(las\s+" + _NUM + r"|la\s+una)(?=\s*([.,;:!?]|$)|\s+(y|menos|de|en)\b)",
     "msg": "Una hora exacta es un punto: <b>a</b> las cinco, <b>a</b> la una."},
    {"id": "a_el", "t": "r",
     "re": r"\b(a|de)\s+el\s+" + _PLACE + r"\b",
     "msg": "Delante de <i>el</i>, se juntan: a + el = <b>al</b>, de + el = <b>del</b> (voy al cine, vengo del cine)."},
]
# Pruebas del detector: (texto, ids que tienen que saltar). El build las comprueba (en Python y en node).
DETECTOR_PRUEBAS = [
    ("El viernes voy en Madrid.", ["ir_en"]),
    ("Hoy estoy a casa todo el día.", ["estar_a"]),
    ("Voy al trabajo con tren.", ["con_vehiculo"]),
    ("Si hace buen tiempo, voy en pie.", ["en_pie"]),
    ("La tienda abre de 9 hasta 2.", ["de_hasta"]),
    ("Trabajo desde las 9 a las 2.", ["desde_a"]),
    ("Gracias para tu invitación.", ["gracias_para"]),
    ("Este regalo es por ti.", ["es_por_persona"]),
    ("Voy a clase por aprender español.", ["por_fin"]),
    ("Trabajo a la mañana.", ["manana"]),
    ("En la mañana voy al gimnasio.", ["manana"]),
    ("Vuelvo en casa a las seis.", ["ir_en"]),
    ("Vamos en el cine a las ocho.", ["ir_en"]),
    ("Trabajo al centro.", ["estar_a"]),
    ("Voy con el coche de mi padre.", ["con_el_vehiculo"]),
    ("La clase empieza en las cinco.", ["en_hora"]),
    ("Voy a el cine con Ana.", ["a_el"]),
    ("Trabajo de lunes hasta viernes.", ["de_hasta"]),
    ("Abrimos desde el lunes al viernes.", ["desde_a"]),
    ("Voy en tren a Madrid y estoy en casa a las seis.", []),
    ("Vivo a dos calles del centro.", []),
    ("Llego en cinco minutos.", []),
    ("Voy con Ana al cine en el coche de su padre.", []),
    ("Trabajo de nueve a dos y desde las cuatro hasta las siete.", []),
    ("Gracias por venir. Lo hago por ti.", []),
    ("Es para ti: estudio para aprender.", []),
    ("Por la mañana voy a clase.", []),
    ("Te llamo a las ocho de la mañana.", []),
    ("Llegamos a la mañana siguiente.", []),
    ("Voy en julio a Roma.", []),
    ("La tienda está a la derecha.", []),
    ("Compré flores en las dos tiendas.", []),
    ("Muchas gracias por practicar conmigo.", []),
    ("Tengo problemas con mi coche.", []),
    ("Quedamos al lado del cine a las siete.", []),
    ("Es por mi culpa.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL 1 (quedamos)
# Tarjetas como en la tarea 3: q (lo que dice el examinador), pista (los datos), m (respuesta modelo marcada)
ORAL = [
    {"q": "¿A qué hora quedamos?", "pista": "19:30", "m": "Quedamos [a:a las siete y media], ¿vale?"},
    {"q": "¿Dónde quedamos?", "pista": "la puerta del museo", "m": "Quedamos [e:en la puerta del museo]."},
    {"q": "¿Cómo vamos al concierto?", "pista": "metro", "m": "Vamos [e:en metro]: es más rápido."},
    {"q": "¿Cogemos el autobús?", "pista": "andando · 10 minutos", "m": "No, mejor vamos [a:a pie]: son diez minutos."},
    {"q": "¿Qué horario tiene la piscina?", "pista": "10:00 – 20:00", "m": "Está abierta [l:de diez de la mañana a ocho de la tarde]."},
    {"q": "¿Cuándo es la fiesta?", "pista": "sábado · noche", "m": "Es el sábado [p:por la noche]."},
    {"q": "¿Para quién es ese regalo?", "pista": "mi hermana", "m": "Es [m:para mi hermana]: mañana es su cumpleaños."},
    {"q": "¿Para qué vas a la biblioteca?", "pista": "estudiar", "m": "[m:Para estudiar]: el lunes tengo un examen."},
    {"q": "¿Dónde vive tu amiga Carla?", "pista": "Málaga", "m": "Vive [e:en Málaga], pero el sábado viene [a:a Alicante]."},
    {"q": "¿De dónde vienes tan cansado?", "pista": "el gimnasio", "m": "Vengo [l:del gimnasio]: he estado dos horas."},
    {"q": "¿Por dónde vamos?", "pista": "el parque", "m": "Vamos [p:por el parque]: es más bonito."},
    {"q": "¿Cuándo tienes que entregar el trabajo?", "pista": "viernes", "m": "Lo tengo que entregar [m:para el viernes]."},
    {"q": "¿Qué horario tienes en el trabajo?", "pista": "lunes–viernes · 8:00–15:00", "m": "Trabajo [l:de lunes a viernes], [l:de ocho a tres]."},
    {"q": "¿Cuándo te vas de vacaciones?", "pista": "agosto · la playa", "m": "Me voy [e:en agosto], [a:a la playa]."},
    {"q": "¿Por qué no viniste ayer?", "pista": "la lluvia", "m": "[p:Por la lluvia]: llovía muchísimo."},
    {"q": "¿A quién vas a llamar?", "pista": "mi madre", "m": "Voy a llamar [a:a mi madre]."},
]

# ------------------------------------------------------------------ AHORA TU: ORAL 2 (como se llega)
# Plano dibujado (SVG, sin fotos). Cada ruta: puntos del camino y explicacion modelo marcada.
LUGARES = [
    # id, rotulo, x, y, ancho, alto, tipo
    ("biblio", "Biblioteca", 40, 40, 130, 60, "edif"),
    ("mercado", "Mercado", 490, 150, 120, 60, "edif"),
    ("estacion", "Estación", 40, 340, 140, 56, "edif"),
    ("cine", "Cine", 490, 340, 120, 56, "edif"),
    ("parque", "Parque", 230, 150, 200, 140, "parque"),
    ("casa", "Casa de Lucía", 500, 40, 110, 56, "casa"),
]
# Calles: rotulo, x1, y1, x2, y2 y donde va el nombre de cada calle (fuera de los caminos)
# Donde va el nombre de cada calle (fuera de los caminos): rotulo, x1, y1, x2, y2, x del rotulo, y del rotulo
CALLES_ROT = [
    ("Calle Mayor", 20, 120, 620, 120, 250, 120),
    ("Avenida del Mar", 20, 320, 620, 320, 500, 320),
    ("Calle del Sol", 200, 20, 200, 410, 200, 104),
    ("Calle Real", 460, 20, 460, 410, 460, 280),
]
CALLES = [c[:5] for c in CALLES_ROT]
PLAZA = ("Plaza Mayor", 460, 120)
PARADAS = [(200, 320), (200, 120)]
RUTAS = [
    {"id": "casa", "titulo": "A casa de Lucía", "modo": "a pie",
     "pts": [(110, 340), (110, 320), (230, 300), (430, 150), (460, 120), (520, 96)],
     "m": "Sales [l:de la estación] y vas [a:a pie]. Cruzas la avenida del Mar y vas [p:por el parque] [l:hasta la plaza Mayor]. "
          "La casa de Lucía está [e:en la plaza], [e:en el número 3]. Son quince minutos andando."},
    {"id": "biblio", "titulo": "A la biblioteca", "modo": "en autobús",
     "pts": [(110, 340), (110, 320), (200, 320), (200, 120), (105, 100)],
     "m": "[l:Desde la estación hasta la biblioteca] es mejor ir [e:en autobús]. Coges la línea 4 [e:en la parada] de la avenida del Mar y vas [p:por la calle del Sol]. "
          "Bajas [e:en la calle Mayor] y la biblioteca está a la izquierda."},
    {"id": "cine", "titulo": "Al cine", "modo": "a pie",
     "pts": [(110, 340), (110, 320), (460, 320), (480, 360)],
     "m": "Es muy fácil: sales [l:de la estación] y vas [p:por la avenida del Mar] todo recto [l:hasta la calle Real]. "
          "El cine está [e:en la esquina], a la derecha. [a:A pie] son diez minutos."},
]
