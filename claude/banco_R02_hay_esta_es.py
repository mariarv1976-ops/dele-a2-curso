# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R02: HAY / ESTA / ES (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R02_hay_esta_es.py
#
# MARCAS
#   En textos modelo:  [h:hay] presentar algo nuevo · [e:esta] situar algo conocido · [s:es] donde pasa un evento
#   En huecos:         [[correcta|distractor|distractor#motivo]]  (la primera es la buena; se barajan)
# Enfoque cognitivo: HAY = algo NUEVO para el que escucha; ESTA = algo que LOS DOS YA CONOCEMOS, solo
# falta saber donde; ES = DONDE (o cuando) PASA un evento. Espanol de Espana. Ejemplos propios.
# Ser/estar en general queda para la R03.

# ------------------------------------------------------------------ MOTIVOS
# clave: (verbo, explicacion corta). El verbo decide el color: hay / esta / es.
MOTIVOS = {
    "nuevo":   ("hay", "Algo nuevo para el que escucha: un, una, unos, unas."),
    "cant":    ("hay", "Una cantidad: números, mucho, poco, varios, algún... van con hay."),
    "sin":     ("hay", "Sin artículo (no hay ascensor, hay mucha gente): presentas algo, no una cosa concreta."),
    "igual":   ("hay", "Hay no cambia nunca: hay una silla, hay dos sillas (nunca «han»)."),
    "conoc":   ("esta", "Algo que los dos ya conocéis (el, la, mi, este...): solo dices dónde está."),
    "plural":  ("esta", "Varias cosas conocidas (los, las, mis...): están."),
    "persona": ("esta", "Una persona concreta (mi hermano, el profesor, Marta): está, nunca hay."),
    "evento":  ("es", "Un evento (fiesta, concierto, boda, reunión, comida...): dónde o cuándo pasa = es."),
}
VERBOS = {
    "hay":  ("Hay", "presenta algo nuevo"),
    "esta": ("Está", "sitúa algo que ya conocemos"),
    "es":   ("Es", "dónde pasa un evento"),
}

# ------------------------------------------------------------------ 1. LA IDEA
# Parejas: a y b con su verbo (ta, tb). Se ve el diagrama de cada uno.
# obj = lo que se presenta o se situa (sale en el dibujo).
PARES = [
    {"tema": "una panadería", "obj": "panadería", "ta": "hay", "tb": "esta",
     "a": "En mi calle [h:hay] una panadería muy buena.",
     "b": "La panadería [e:está] en mi calle, al lado del banco.",
     "ra": "Tu amigo <b>no sabe que existe</b>. Se la presentas: «hay una panadería». Para él es nueva.",
     "rb": "Los dos sabéis <b>de qué panadería habláis</b> (la de siempre, la que te ha recomendado). Solo falta saber dónde está."},
    {"tema": "un cajero", "obj": "cajero", "ta": "hay", "tb": "esta",
     "a": "Perdone, ¿[h:hay] un cajero por aquí?",
     "b": "Perdone, ¿dónde [e:está] el cajero?",
     "ra": "Buscas <b>cualquier cajero</b>. No sabes si existe uno cerca: preguntas si hay.",
     "rb": "Ya sabes que <b>hay uno</b> (el del hotel, el de la estación). Solo preguntas el lugar."},
    {"tema": "un perro en la foto", "obj": "perro", "ta": "hay", "tb": "esta",
     "a": "En la foto [h:hay] un perro.",
     "b": "El perro [e:está] debajo de la mesa.",
     "ra": "El examinador <b>todavía no sabe</b> qué has visto: lo presentas.",
     "rb": "Ya lo has presentado: ahora es <b>«el perro»</b>, y dices dónde está. Primero hay, después está."},
    {"tema": "dos sofás", "obj": "sofás", "ta": "hay", "tb": "esta",
     "a": "En el salón [h:hay] dos sofás.",
     "b": "Los sofás [e:están] delante de la ventana.",
     "ra": "Con un número presentas cosas nuevas. <b>Hay</b> no cambia: hay un sofá, hay dos sofás.",
     "rb": "<b>Los sofás</b>: ya sabemos cuáles. En plural, <b>están</b>."},
    {"tema": "la fiesta", "obj": "fiesta", "ta": "es", "tb": "esta",
     "a": "La fiesta [s:es] en casa de Nuria.",
     "b": "La casa de Nuria [e:está] en el centro.",
     "ra": "La fiesta es <b>un evento</b>: algo que pasa. Para decir dónde pasa, <b>es en</b> (y cuándo: es a las nueve).",
     "rb": "La casa es <b>un lugar</b>, una cosa que no se mueve: <b>está</b> en el centro."},
]

# Lo que va detras de cada uno (tabla de la pestana 1)
DETRAS = {
    "hay":  ["un, una, unos, unas: [h:hay] un parque", "sin artículo: no [h:hay] ascensor, [h:hay] sitio",
             "números: [h:hay] tres habitaciones", "mucho, poco, varios, algún, ningún: [h:hay] mucha gente",
             "qué: ¿Qué [h:hay] en la nevera?"],
    "esta": ["el, la, los, las: la estación [e:está] cerca", "mi, tu, su...: mis llaves [e:están] aquí",
             "este, ese: este autobús [e:está] lleno", "nombres propios: Marta [e:está] en casa",
             "¿dónde?: ¿Dónde [e:está] el baño?"],
    "es":   ["la fiesta, la boda, el concierto: la boda [s:es] en un pueblo", "la reunión, la clase, el examen: el examen [s:es] en el aula 4",
             "la comida, la cena, el partido: la cena [s:es] a las nueve", "¿dónde? / ¿cuándo?: ¿Dónde [s:es] la fiesta?"],
}

# La cadena: primero HAY (presentas), despues ESTA (situas)
CADENA = [
    ("En la foto [h:hay] una mujer mayor y un niño.", "La mujer [e:está] a la izquierda y el niño [e:está] a su lado."),
    ("Cerca de mi casa [h:hay] un parque muy grande.", "El parque [e:está] al final de mi calle."),
    ("Este sábado [h:hay] una fiesta en el barrio.", "La fiesta [s:es] en la plaza, a las ocho."),
]

AVISOS = [
    ("Hay no cambia", "[h:Hay] una silla, [h:hay] dos sillas, [h:hay] muchas sillas. Nunca <s>han</s> dos sillas."),
    ("Está sí cambia", "estoy, estás, [e:está], estamos, estáis, [e:están]: mis padres [e:están] en casa."),
    ("¿Dónde es? o ¿Dónde está?", "¿Dónde [s:es] la fiesta? (un evento) · ¿Dónde [e:está] tu casa? (un lugar)."),
    ("Hay también con eventos", "Para presentar el evento, hay: «Esta noche [h:hay] un concierto». Para decir dónde pasa, es: «El concierto [s:es] en el parque»."),
]

# ------------------------------------------------------------------ 2. EN EL EXAMEN
DONDE = [
    ("Oral · tarea 2 (foto)", "La pregunta 2 de la lámina ya lo dice: «¿Dónde están? ¿Qué objetos hay?».",
     "En la foto [h:hay] tres personas. A la izquierda [h:hay] una ventana. La chica [e:está] en el centro."),
    ("Oral · tarea 1 (monólogo)", "Temas como «mi casa», «mi ciudad», «una fiesta especial».",
     "Mi piso [e:está] en el centro y [h:hay] un mercado al lado. Mi cumpleaños siempre [s:es] en casa de mis padres."),
    ("Escritura · tarea 1 (correo)", "Describir un piso nuevo, dar indicaciones, invitar a una fiesta.",
     "Mi casa [e:está] enfrente de la estación. En la esquina [h:hay] una farmacia. La comida [s:es] el domingo a las dos."),
    ("Escritura · tarea 2 (blog o revista)", "«Mi barrio», «mi lugar favorito», «una fiesta de mi ciudad».",
     "En mi barrio no [h:hay] cines, pero [h:hay] muchos bares. La fiesta del barrio [s:es] en junio."),
    ("Lectura · tarea 2 (anuncios)", "Los anuncios dicen qué hay y dónde está algo: la pregunta busca ese dato.",
     "Piso de dos habitaciones. [e:Está] a cinco minutos de la playa. No [h:hay] ascensor. La visita [s:es] el lunes, a las once."),
]

ERRORES = [
    ("En mi pueblo está un parque muy grande.", "En mi pueblo [h:hay] un parque muy grande.",
     "Presentas un parque nuevo (un parque): hay."),
    ("En el centro hay el museo de arte.", "El museo de arte [e:está] en el centro.",
     "«El museo» ya lo conocemos: solo dices dónde está."),
    ("La fiesta está en mi casa.", "La fiesta [s:es] en mi casa.",
     "La fiesta es un evento: dónde pasa = es en."),
    ("Hay mi hermano en la foto.", "Mi hermano [e:está] en la foto. / En la foto [e:está] mi hermano.",
     "«Mi hermano» es una persona concreta: está."),
    ("Están muchos turistas en la playa.", "En la playa [h:hay] muchos turistas.",
     "Muchos, pocos, números: hay. Y el lugar, mejor delante: «En la playa hay...»."),
    ("En el salón han dos sofás.", "En el salón [h:hay] dos sofás.",
     "Hay no cambia en plural."),
]

# ------------------------------------------------------------------ EJERCICIOS DE OPCION MULTIPLE
# Cada item: q (enunciado con ____), o (opciones; LA PRIMERA ES LA BUENA), why.

# P1 Hay, esta o es
P_VERBO = [
    {"q": "Perdona, ¿____ un supermercado por aquí?", "o": ["hay", "está", "es"],
     "why": "Buscas <b>cualquier</b> supermercado: no sabes si existe. <i>Un supermercado</i> = algo nuevo: hay."},
    {"q": "Perdona, ¿dónde ____ el mercado central?", "o": ["está", "hay", "es"],
     "why": "<i>El mercado central</i>: sabes que existe y cuál es. Solo preguntas dónde: está."},
    {"q": "La boda de mi prima ____ en un pueblo de la montaña.", "o": ["es", "está", "hay"],
     "why": "Una boda es un evento: algo que pasa. Dónde pasa = <b>es en</b>."},
    {"q": "En mi habitación ____ una cama, un armario y una mesa.", "o": ["hay", "está", "es"],
     "why": "Presentas cosas nuevas con <i>un, una</i>: hay. Y hay no cambia aunque sean varias."},
    {"q": "Mis libros ____ encima de la mesa.", "o": ["están", "hay", "son"],
     "why": "<i>Mis libros</i>: cosas concretas que ya conocemos. Dónde = están (plural)."},
    {"q": "En la foto ____ dos niños jugando con un perro.", "o": ["hay", "están", "son"],
     "why": "Presentas lo que ves, con un número: hay. Es la primera frase típica de la foto."},
    {"q": "Los niños ____ a la derecha, al lado del árbol.", "o": ["están", "hay", "son"],
     "why": "Ya has presentado a los niños: ahora son <i>los niños</i>. Los sitúas: están."},
    {"q": "—¿Dónde ____ la reunión de mañana? —En la sala 3.", "o": ["es", "está", "hay"],
     "why": "La reunión es un evento: ¿dónde <b>es</b>? Pasa en la sala 3."},
    {"q": "—¿Dónde ____ la sala 3? —En el segundo piso.", "o": ["está", "es", "hay"],
     "why": "La sala es un lugar, no un evento: ¿dónde está?"},
    {"q": "En el centro de la plaza ____ una fuente muy bonita.", "o": ["hay", "está", "es"],
     "why": "<i>Una fuente</i>: la presentas. Primero el lugar, después hay + lo nuevo."},
    {"q": "Lucía no ____ en casa: ha ido al médico.", "o": ["está", "hay", "es"],
     "why": "Lucía es una persona concreta (un nombre propio): está. Nunca <s>hay Lucía</s>."},
    {"q": "En la nevera no ____ leche. ¿Puedes comprar?", "o": ["hay", "está", "es"],
     "why": "<i>No hay leche</i>: sin artículo, hablas de que existe o no. Hay."},
    {"q": "Esta noche ____ un concierto gratis en el parque.", "o": ["hay", "es", "está"],
     "why": "Presentas un evento nuevo (<i>un concierto</i>): hay. Si ya lo conocemos y dices dónde pasa: <i>el concierto es en el parque</i>."},
    {"q": "—Hola, ¿____ tu madre? —No, ha salido.", "o": ["está", "hay", "es"],
     "why": "Preguntas por una persona concreta (<i>tu madre</i>): ¿está?"},
]

# P2 Que va detras
P_DETRAS = [
    {"q": "En mi barrio <b>hay</b> ____ mercado muy grande.", "o": ["un", "el", "mi"],
     "why": "Detrás de hay va algo nuevo: <i>un</i> mercado. Con <i>el</i> o <i>mi</i> sería algo conocido."},
    {"q": "____ mercado <b>está</b> en la plaza mayor.", "o": ["El", "Un", "Algún"],
     "why": "Con está hablas de algo conocido: <i>el</i> mercado."},
    {"q": "Encima de la mesa <b>hay</b> ____ libros.", "o": ["unos", "los", "mis"],
     "why": "Hay + <i>unos</i>: cosas nuevas. Si son tus libros: <i>mis libros están encima de la mesa</i>."},
    {"q": "____ gafas <b>están</b> en el baño.", "o": ["Tus", "Unas", "Muchas"],
     "why": "Están + algo concreto: <i>tus</i> gafas. <i>Unas gafas</i> o <i>muchas</i> irían con hay."},
    {"q": "En esta calle <b>hay</b> ____ tiendas de ropa.", "o": ["muchas", "las", "sus"],
     "why": "Cantidades (<i>mucho, poco, varios</i>) van con hay."},
    {"q": "¿Dónde <b>está</b> ____?", "o": ["Carlos", "un chico", "algún chico"],
     "why": "Está + una persona concreta o un nombre propio."},
    {"q": "En mi clase <b>hay</b> ____ estudiantes de Italia.", "o": ["tres", "los", "mis"],
     "why": "Números + hay: <i>hay tres estudiantes</i>."},
    {"q": "En la nevera no <b>hay</b> ____.", "o": ["leche", "la leche", "tu leche"],
     "why": "No hay + sin artículo. <i>La leche</i> iría con está: <i>la leche está en la nevera</i>."},
    {"q": "____ fiesta <b>es</b> en el jardín.", "o": ["La", "Una", "Alguna"],
     "why": "Con es en hablas de un evento que ya conocemos: <i>la</i> fiesta (la de Ana, la del sábado)."},
    {"q": "En el salón <b>hay</b> ____ sofá rojo.", "o": ["un", "el", "este"],
     "why": "Presentas algo nuevo: <i>un</i> sofá."},
]

# E4 Bien o mal. ok = 0 (bien) o 1 (mal); fix = correccion (solo en las malas)
E_BIENMAL = [
    {"q": "En mi pueblo está un parque muy grande.", "ok": 1, "fix": "En mi pueblo <b>hay</b> un parque muy grande.",
     "why": "<i>Un parque</i> es nuevo para el que escucha: hay."},
    {"q": "En el centro hay el museo de arte.", "ok": 1, "fix": "<b>El museo de arte está</b> en el centro.",
     "why": "<i>El museo</i> es conocido: está. Hay nunca va con el, la."},
    {"q": "La fiesta está en mi casa.", "ok": 1, "fix": "La fiesta <b>es</b> en mi casa.",
     "why": "Un evento: dónde pasa = es."},
    {"q": "Hay mi hermano en la foto.", "ok": 1, "fix": "<b>Mi hermano está</b> en la foto.",
     "why": "Una persona concreta: está."},
    {"q": "En la plaza hay muchos turistas.", "ok": 0, "fix": "",
     "why": "Correcto: cantidad (<i>muchos</i>) + hay."},
    {"q": "Mis padres están en la cocina.", "ok": 0, "fix": "",
     "why": "Correcto: personas concretas, en plural: están."},
    {"q": "En el salón han dos sofás.", "ok": 1, "fix": "En el salón <b>hay</b> dos sofás.",
     "why": "Hay no cambia en plural."},
    {"q": "El concierto es en el parque de la ciudad.", "ok": 0, "fix": "",
     "why": "Correcto: el concierto es un evento; dónde pasa = es."},
    {"q": "La farmacia está al lado del banco.", "ok": 0, "fix": "",
     "why": "Correcto: la farmacia es conocida; la sitúas."},
    {"q": "Están muchas personas en la playa.", "ok": 1, "fix": "En la playa <b>hay</b> muchas personas.",
     "why": "<i>Muchas personas</i>: cantidad, hay."},
    {"q": "¿Hay un cajero cerca de aquí?", "ok": 0, "fix": "",
     "why": "Correcto: buscas cualquier cajero."},
    {"q": "En mi calle no hay supermercado.", "ok": 0, "fix": "",
     "why": "Correcto: no hay + sin artículo."},
]

# ------------------------------------------------------------------ TEXTOS CON HUECOS
TEXTOS = [
    {"id": "piso", "tipo": "Lectura · tarea 2 · anuncio", "titulo": "Habitación en piso compartido",
     "texto": "Alquilo una habitación en un piso de estudiantes. El piso [[está|hay|es#conoc]] en un barrio tranquilo, muy cerca de la estación. "
              "[[Hay|Están|Son#cant]] tres habitaciones, dos baños y una cocina grande. La habitación libre [[está|hay|es#conoc]] al lado del salón y tiene balcón. "
              "En el edificio no [[hay|está|es#sin]] ascensor, pero solo es un segundo piso. Cerca [[hay|están|son#cant]] dos supermercados y una parada de autobús: "
              "la parada [[está|hay|es#conoc]] enfrente del portal. La cena de bienvenida para el nuevo compañero [[es|está|hay#evento]] el primer viernes del mes, en la terraza."},
    {"id": "llegar", "tipo": "Escritura · tarea 1 · correo a un amigo", "titulo": "Cómo llegar a mi casa",
     "texto": "¡Hola, Pablo! ¡Qué bien que vienes el sábado! La comida [[es|está|hay#evento]] en mi casa nueva, a las dos. Te explico cómo llegar. "
              "Sales de la estación de metro y [[hay|está|es#nuevo]] una plaza con una fuente. Mi calle [[está|hay|es#conoc]] a la derecha de la plaza. "
              "En la esquina [[hay|está|es#nuevo]] una farmacia; mi portal [[está|hay|es#conoc]] justo al lado. Es el número 14, tercero B. "
              "Si no encuentras la calle, llámame: Marta [[está|hay|es#persona]] en casa desde las doce y puede bajar a buscarte. "
              "¡Ah! Si quieres comprar algo para el postre, cerca de casa [[hay|están|son#cant]] varias pastelerías. Un abrazo, Irene"},
    {"id": "foto", "tipo": "Oral · tarea 2 · descripción de la foto", "titulo": "En el mercado",
     "texto": "En la foto [[hay|están|son#cant]] cuatro personas en un mercado. En el centro [[hay|está|es#nuevo]] un puesto de fruta con muchas cajas. "
              "El vendedor [[está|hay|es#conoc]] detrás del puesto y lleva un delantal verde. A la izquierda [[hay|está|es#nuevo]] una señora mayor con un carro de la compra. "
              "Su nieto [[está|hay|es#persona]] a su lado y come una manzana. Al fondo [[hay|están|son#cant]] muchos puestos más y [[hay|está|es#sin]] mucha gente."},
    {"id": "barrio", "tipo": "Escritura · tarea 2 · revista", "titulo": "Mi barrio",
     "texto": "Vivo en un barrio pequeño y tranquilo, cerca del puerto. Mi casa [[está|hay|es#conoc]] en una calle estrecha y antigua. "
              "En mi calle [[hay|está|es#nuevo]] un bar con las mejores tapas de la ciudad. El parque de las Palmeras [[está|hay|es#conoc]] a cinco minutos andando. "
              "En el barrio no [[hay|está|es#sin]] cines, pero [[hay|están|son#cant]] muchas tiendas pequeñas y dos mercados. "
              "En junio, la fiesta del barrio [[es|está|hay#evento]] en la plaza de la iglesia y todos los vecinos bajan a la calle. "
              "Mis amigos [[están|hay|son#plural]] siempre en el puesto de las bebidas: ¡ven a verlos!"},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
# pautas: (texto, [verbos que pide]) con verbos de VERBOS
LAMINAS = [
    {"id": "piso", "tarea": "Tarea 1 · correo a un amigo", "palabras": [60, 70], "pide_es": True,
     "intro": "Has recibido este mensaje de tu amigo Héctor:",
     "mensaje": "¡Hola! Me han dicho que ya vives en tu piso nuevo. ¡Enhorabuena! ¿Dónde está? ¿Cómo es el barrio? ¿Hay tiendas cerca? Cuéntame. Un abrazo, Héctor",
     "consigna": "Escribe un correo a Héctor. En él tienes que:",
     "pautas": [("saludar;", []),
                ("decirle dónde está tu piso nuevo;", ["esta"]),
                ("contarle qué hay en el barrio;", ["hay"]),
                ("invitarle a la fiesta del piso: dónde y cuándo es;", ["es"]),
                ("despedirte.", [])]},
    {"id": "barrio", "tarea": "Tarea 2 · opción 1 · revista", "palabras": [70, 80], "pide_es": True,
     "intro": "", "mensaje": "",
     "consigna": "Una revista para estudiantes de español busca textos sobre «Mi barrio». Escribe un texto. Habla de:",
     "pautas": [("dónde está tu barrio y cómo es;", ["esta"]),
                ("qué hay en tu barrio (tiendas, parques, transporte...);", ["hay"]),
                ("tu lugar favorito y dónde está;", ["esta"]),
                ("qué no hay y te gustaría tener;", ["hay"]),
                ("una fiesta o un mercado del barrio: cuándo y dónde es.", ["es"])]},
]

# Detector de errores tipicos (sobre el texto sin tildes y en minusculas, salvo case=True).
# t: "r" (rojo: casi seguro un error) o "a" (ambar: mira si es un error)
DETECTOR = [
    {"id": "esta_nuevo", "t": "r",
     "re": r"\b(esta|estan)\s+(un(?!\s+poco)|una|unos|unas|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|muchos|muchas|mucha|pocos|pocas|varios|varias|algun|alguna|algunos|algunas)\b",
     "msg": "Presentas algo nuevo (un, una, un número, muchos...) con está. Usa <b>hay</b>: «En mi calle hay un parque»."},
    {"id": "hay_conoc", "t": "r",
     "re": r"\bhay\s+(el|la|los|las|mi|mis|tu|tus|su|sus|nuestro|nuestra|nuestros|nuestras|este|esta|estos|estas|ese|esa|esos|esas)\b",
     "msg": "Hay no va con el, la, mi, este... Si ya lo conocemos, usa <b>está</b>: «El museo está en el centro»."},
    {"id": "evento_esta", "t": "r",
     "re": r"\b(la fiesta|el concierto|la boda|la reunion|el cumpleanos|la inauguracion|el partido|la excursion|la celebracion)\s+(esta|estara)\s+en\b",
     "msg": "Si hablas del evento (dónde pasa), no va está sino <b>es</b>: «La fiesta es en mi casa»."},
    {"id": "han", "t": "r",
     "re": r"\bhan\s+(un|una|unos|unas|dos|tres|cuatro|cinco|muchos|muchas|pocos|pocas|varios|varias)\b",
     "msg": "Hay no cambia en plural: <b>hay</b> dos sofás, nunca «han»."},
    {"id": "hay_nombre", "t": "a", "case": True,
     "re": r"(?:^|[^A-Za-z])[Hh]ay\s+([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)",
     "msg": "¿Es un nombre propio (una persona, un lugar)? Con nombres propios, <b>está</b>: «Marta está en casa». Si es una tienda o una marca (hay un Mercadona), está bien con «un»."},
]
# Pruebas del detector: (texto, ids que tienen que saltar). El build las comprueba.
DETECTOR_PRUEBAS = [
    ("En mi calle está un parque muy bonito.", ["esta_nuevo"]),
    ("Mi casa está un poco lejos del centro.", []),
    ("En el centro hay el museo y la catedral.", ["hay_conoc"]),
    ("La fiesta está en mi casa, a las nueve.", ["evento_esta"]),
    ("La cena está muy buena.", []),
    ("En el salón han dos sofás.", ["han"]),
    ("Hay Marta en la cocina.", ["hay_nombre"]),
    ("En mi barrio hay un parque y hay muchas tiendas.", []),
    ("Hay que comprar pan.", []),
    ("Están muchos turistas en verano.", ["esta_nuevo"]),
    ("Mis padres están en casa y la boda es en junio.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL (fotos de la tarea 2)
# Fotos de M4T2 que ya estan en WordPress (M4T2_fotoN.jpg). Solo las "como en el examen" (7-12).
MES_WP_T2 = "2026/10"
LUGAR = ["a la izquierda", "a la derecha", "en el centro", "delante (de)", "detrás de", "al fondo",
         "encima de", "debajo de", "al lado de", "entre... y...", "enfrente de", "en la pared", "en el suelo"]
FOTOS = [
    {"id": 7, "titulo": "Antes de salir de casa",
     "alt": "Recibidor de un piso por la mañana: una madre mira la hora en el móvil, un niño con un solo zapato busca el otro en el suelo y una niña espera al lado de la puerta abierta.",
     "hay": "En la foto [h:hay] tres personas: una mujer y dos niños. A la derecha [h:hay] una puerta abierta. En la pared [h:hay] un espejo y un perchero con abrigos. En el suelo [h:hay] zapatos.",
     "esta": "La madre [e:está] en el centro, con el móvil en la mano. El niño [e:está] en el suelo, delante del mueble de los zapatos. La niña [e:está] al lado de la puerta. Los abrigos [e:están] en el perchero."},
    {"id": 8, "titulo": "Hacer deporte",
     "alt": "Pista de pádel al aire libre: cuatro amigos se dan la mano en la red al final del partido; en un banco, botellas de agua y toallas.",
     "hay": "En la foto [h:hay] cuatro personas: dos mujeres y dos hombres. En el centro de la pista [h:hay] una red. En el suelo [h:hay] pelotas amarillas y delante [h:hay] un banco con botellas de agua y toallas.",
     "esta": "Las dos mujeres [e:están] a la izquierda. El hombre de la barba [e:está] a la derecha, al lado de su compañero. Las mochilas [e:están] en el banco. Las montañas [e:están] al fondo, detrás de los árboles."},
    {"id": 9, "titulo": "De compras",
     "alt": "Caja de un supermercado de barrio: un señor mayor busca la cartera, su mujer mete la compra en un carro y la cajera espera sonriendo.",
     "hay": "En la foto [h:hay] tres personas en la caja de un supermercado. En la cinta [h:hay] una barra de pan, leche, huevos y fruta. Al fondo [h:hay] estanterías y un chico con una cesta.",
     "esta": "La cajera [e:está] detrás de la caja. El señor [e:está] delante de ella y busca su cartera. La señora [e:está] a su lado, con el carro de la compra. La máquina para pagar [e:está] a la derecha."},
    {"id": 10, "titulo": "Clases para adultos",
     "alt": "Clase de baile para adultos en una sala con espejo: el profesor enseña un paso, una pareja mayor baila bien y un chico joven pisa a su pareja.",
     "hay": "En la foto [h:hay] cinco personas. En la pared [h:hay] un espejo muy grande. En una esquina [h:hay] un altavoz y unas sillas con abrigos y bolsos.",
     "esta": "El profesor [e:está] en el centro. La pareja mayor [e:está] a la izquierda y la pareja joven [e:está] a la derecha. Los bolsos [e:están] en las sillas, al fondo."},
    {"id": 11, "titulo": "Ver la televisión",
     "alt": "Salón de un piso por la noche: dos amigos saltan de alegría delante de un partido en la tele y otro se tapa la cara en el sofá; las palomitas se caen al suelo.",
     "hay": "En la foto [h:hay] tres jóvenes en un salón. Delante del sofá [h:hay] una mesa baja con pizza, patatas y latas. En la pared [h:hay] una televisión grande.",
     "esta": "La chica del pelo azul [e:está] en el centro. El chico rubio [e:está] en el sofá, a la derecha. La televisión [e:está] en la pared, delante de ellos. Las palomitas [e:están] en el suelo."},
    {"id": 12, "titulo": "Regalos",
     "alt": "Cafetería pequeña en otoño: una mujer abre un regalo, una bufanda de colores, y su amiga la mira; un camarero trae dos cafés y una tarta con una vela.",
     "hay": "En la foto [h:hay] dos mujeres y un camarero en una cafetería. Encima de la mesa [h:hay] papel de regalo, un lazo y dos bolsos. Al fondo [h:hay] una ventana grande y plantas.",
     "esta": "Las dos amigas [e:están] en una mesa, al lado de la ventana. El camarero [e:está] a la derecha, con los cafés y la tarta. Los regalos [e:están] encima de la mesa."},
]
