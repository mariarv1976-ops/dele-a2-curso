# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R04: CONCORDANCIA Y POSESIVOS (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R04_concordancia_posesivos.py
#
# ENFOQUE COGNITIVO
#   1. EL NOMBRE MANDA: es el capitan del equipo y lleva una camiseta con dos datos:
#      masculino o femenino, y uno o varios. Todo lo que va con el (el, un, este, mi, nuestro,
#      mucho, simpatico...) se pone LA MISMA CAMISETA.
#   2. EL POSESIVO MIRA A LA COSA: "¿de quien?" elige la palabra (mi, tu, su, nuestr-, vuestr-);
#      "¿que cosa?" le pone la camiseta (nuestra casa, sus hijos).
#   3. Los tonicos (el mio, la tuya): el nombre se va, pero su camiseta se queda.
#
# MARCAS
#   Grupos (equipos):  [ms:el ^piso nuevo]  [fs:...]  [mp:...]  [fp:...]
#                      m/f = masculino/femenino; s/p = uno/varios. ^ delante del nombre (el capitan).
#                      Un grupo puede ir sin nombre: [fs:simpatica] (despues de ser), [ms:el mio].
#   Huecos:            [[correcta|distractor|distractor#motivo]]  (la primera es la buena; se barajan)
# Espanol de Espana. Ejemplos propios (ninguno sale de los materiales de Maria).

# ------------------------------------------------------------------ MOTIVOS
# clave: (familia, explicacion). La familia decide el color: "nom" (el nombre manda) o "pos" (posesivos).
MOTIVOS = {
    "gen":    ("nom", "Mira el nombre: si es masculino, -o; si es femenino, -a. Todo el equipo lleva su camiseta."),
    "num":    ("nom", "Mira el nombre: ¿uno o varios? Si son varios, todo el equipo lleva -s."),
    "inv":    ("nom", "Este adjetivo termina en -e o en consonante (grande, azul, joven): no cambia de masculino a femenino, solo de uno a varios."),
    "engana": ("nom", "Un nombre que engaña: el problema, el día, el mapa (masculinos con -a); la mano, la foto, la moto (femeninos con -o). Mira su artículo."),
    "gente":  ("nom", "La gente es UNA cosa, femenina: la gente es simpática, mucha gente. Nunca «las gente» ni «la gente son»."),
    "mucho":  ("nom", "Mucho y poco también se ponen la camiseta del nombre: mucho tiempo, mucha gente, muchos amigos, muchas personas."),
    "pos_cosa":   ("pos", "El posesivo mira a la COSA, no a la persona: nuestra casa, sus hijos, mis amigas."),
    "pos_duenyo": ("pos", "¿De quién es? El dueño elige la palabra: mi (yo), tu (tú), su (él, ella, usted, ellos), nuestro (nosotros), vuestro (vosotros)."),
    "tonico": ("pos", "Sin nombre detrás (el mío, la tuya, es mía): el nombre se va, pero su camiseta se queda."),
}
FAMILIAS = {"nom": "el nombre manda", "pos": "el posesivo mira a la cosa"}

# ------------------------------------------------------------------ 1. LA IDEA
# Equipos: la frase bien (un grupo) y la frase con error (palabra, camiseta). ^ = el nombre.
EQUIPOS = [
    {"tema": "mis amigos",
     "bien": "[mp:mis ^amigos españoles]",
     "mal": [("mis", "mp"), ("^amigo", "ms"), ("español", "ms")],
     "rb": "El capitán es <b>amigos</b>: masculino y varios. <i>Mis</i> y <i>españoles</i> llevan su camiseta: los tres con <b>-s</b>.",
     "rm": "<i>Mis</i> dice «varios», pero <i>amigo</i> y <i>español</i> dicen «uno». Dos camisetas distintas en el mismo equipo."},
    {"tema": "nuestra casa",
     "bien": "[fs:nuestra ^casa nueva]",
     "mal": [("nuestro", "ms"), ("^casa", "fs"), ("nuevo", "ms")],
     "rb": "<b>Casa</b> es femenino: <i>nuestra</i> y <i>nueva</i> terminan en <b>-a</b>. No importa si los dueños somos chicos o chicas.",
     "rm": "<i>Nuestro</i> y <i>nuevo</i> llevan la camiseta masculina, pero el capitán, <i>casa</i>, es femenino."},
    {"tema": "unas chicas simpáticas",
     "bien": "[fp:unas ^chicas simpáticas]",
     "mal": [("unas", "fp"), ("^chicas", "fp"), ("simpático", "ms")],
     "rb": "Femenino y varios: <i>unas</i>, <i>chicas</i> y <i>simpáticas</i>, los tres con <b>-as</b>.",
     "rm": "El adjetivo va detrás y se olvida de mirar al capitán: <i>simpático</i> lleva otra camiseta."},
    {"tema": "un problema pequeño",
     "bien": "[ms:un ^problema pequeño]",
     "mal": [("una", "fs"), ("^problema", "ms"), ("pequeña", "fs")],
     "rb": "<b>Problema</b> termina en -a, pero es masculino: <i>el</i> problema. Su camiseta es masculina, y el equipo también.",
     "rm": "La -a de <i>problema</i> engaña: es un capitán masculino. <i>Una</i> y <i>pequeña</i> llevan la camiseta equivocada."},
    {"tema": "mucha gente",
     "bien": "[fs:mucha ^gente joven]",
     "mal": [("muchas", "fp"), ("^gente", "fs"), ("jóvenes", "fp")],
     "rb": "<b>Gente</b> son muchas personas, pero la palabra es UNA y femenina: <i>mucha</i> gente <i>joven</i>.",
     "rm": "Piensas en muchas personas y pones -s, pero el capitán <i>gente</i> lleva la camiseta de «uno»."},
    {"tema": "esta foto antigua",
     "bien": "[fs:esta ^foto antigua]",
     "mal": [("este", "ms"), ("^foto", "fs"), ("antiguo", "ms")],
     "rb": "<b>Foto</b> termina en -o, pero es femenino: <i>la</i> foto (es «la fotografía»). Todo el equipo, en femenino.",
     "rm": "La -o de <i>foto</i> engaña: <i>este</i> y <i>antiguo</i> llevan la camiseta masculina."},
]

# Lo que se viste y lo que no
VISTE = [
    ("Cambian en masculino / femenino y en uno / varios",
     ["el, la, los, las · un, una, unos, unas", "este, esta, estos, estas · ese, esa...", "nuestro, nuestra, nuestros, nuestras · vuestro...",
      "mucho, mucha, muchos, muchas · poco... · otro... · todo...", "los adjetivos en -o: alto, alta, altos, altas"]),
    ("Solo cambian en uno / varios",
     ["mi, mis · tu, tus · su, sus", "los adjetivos en -e: grande, grandes · inteligente, inteligentes",
      "los adjetivos en consonante: azul, azules · joven, jóvenes · fácil, fáciles"]),
    ("No cambian nunca",
     ["muy: muy alto, muy alta, muy altos", "los números: dos chicos, dos chicas (pero un chico, una chica)",
      "de + nombre: una camiseta de rayas, unos zapatos de piel"]),
]
PLURAL = [("vocal → -s", "casa → casas · grande → grandes"), ("consonante → -es", "ciudad → ciudades · azul → azules · joven → jóvenes"),
          ("-z → -ces", "lápiz → lápices · feliz → felices")]

# Capitanes que engañan: (grupo marcado, explicacion)
ENGANAN = [
    ("Masculinos con -a", ["[ms:el ^problema]", "[ms:el ^día]", "[ms:el ^mapa]", "[ms:el ^idioma]", "[ms:el ^tema]", "[ms:el ^sofá]"],
     "Muchas palabras en -ma (problema, tema, idioma, programa) son masculinas: un problema difícil, un idioma nuevo."),
    ("Femeninos con -o", ["[fs:la ^mano]", "[fs:la ^foto]", "[fs:la ^moto]", "[fs:la ^radio]"],
     "Foto, moto y radio son palabras cortas de fotografía, motocicleta y radiodifusión: por eso son femeninas. La mano, también."),
    ("La gente", ["[fs:la ^gente]", "[fs:mucha ^gente]", "[fs:poca ^gente]"],
     "Son muchas personas, pero la palabra es una y femenina: la gente es simpática; aquí vive mucha gente."),
    ("El agua", ["[fs:el ^agua fría]", "[fp:las ^aguas]"],
     "Es femenina (el agua está fría), pero lleva «el» para no decir «la agua». Con el adjetivo se ve su camiseta: fría."),
    ("Sin -o ni -a", ["[fs:la ^noche]", "[ms:el ^coche]", "[fs:la ^ciudad]", "[ms:el ^hotel]"],
     "Si el nombre no termina en -o ni en -a, no adivines: apréndelo con su artículo, como una pareja."),
]

# ------------------------------------------------------------------ 2. LOS POSESIVOS
# Duenos: id, etiqueta, cuantas personas (1 o 2 para el dibujo), raiz y tipo de camiseta:
#   "num" = solo uno / varios (mi, mis); "gen" = las dos cosas (nuestro, nuestra...).
DUENOS = [
    {"id": "yo", "lab": "yo", "n": 1, "raiz": "mi", "tipo": "num", "ton": "mí"},
    {"id": "tu", "lab": "tú", "n": 1, "raiz": "tu", "tipo": "num", "ton": "tuy"},
    {"id": "el", "lab": "él, ella, usted", "n": 1, "raiz": "su", "tipo": "num", "ton": "suy"},
    {"id": "nos", "lab": "nosotros, nosotras", "n": 2, "raiz": "nuestr", "tipo": "gen", "ton": "nuestr"},
    {"id": "vos", "lab": "vosotros, vosotras", "n": 2, "raiz": "vuestr", "tipo": "gen", "ton": "vuestr"},
    {"id": "ellos", "lab": "ellos, ellas, ustedes", "n": 2, "raiz": "su", "tipo": "num", "ton": "suy"},
]
COSAS = [
    {"w": "piso", "t": "ms"}, {"w": "casa", "t": "fs"}, {"w": "pisos", "t": "mp"}, {"w": "casas", "t": "fp"},
    {"w": "hermano", "t": "ms"}, {"w": "hermana", "t": "fs"}, {"w": "hermanos", "t": "mp"}, {"w": "hermanas", "t": "fp"},
]
# La trampa de su / sus: (quien, cuantas personas, grupo, cuantas cosas, explicacion)
SU_TRAMPA = [
    ("Ana y Luis", 2, "[fs:su ^casa]", 1, "Son dos dueños, pero tienen UNA casa: <b>su</b> casa."),
    ("Pedro", 1, "[mp:sus ^hijos]", 3, "Un dueño, pero TRES hijos: <b>sus</b> hijos."),
    ("Mis abuelos", 2, "[mp:sus ^amigos]", 3, "Dos dueños y muchos amigos: <b>sus</b> amigos."),
    ("Marta", 1, "[fs:su ^bicicleta]", 1, "Una dueña y una bici: <b>su</b> bicicleta."),
]
# Tonicos: la frase con el nombre y la frase sin el
TONICOS = [
    ("Mi piso es pequeño; ¿y [ms:tu ^piso]?", "Mi piso es pequeño; ¿y [ms:el tuyo]?"),
    ("—¿De quién es esta chaqueta? —Es [fs:mi ^chaqueta].", "—¿De quién es esta chaqueta? —Es [fs:mía]."),
    ("Tus padres viven en Madrid y [mp:mis ^padres] viven en Lyon.", "Tus padres viven en Madrid y [mp:los míos] viven en Lyon."),
    ("Nuestras vacaciones son en julio. ¿Y [fp:vuestras ^vacaciones]?", "Nuestras vacaciones son en julio. ¿Y [fp:las vuestras]?"),
]

# ------------------------------------------------------------------ 3. EN EL EXAMEN
DONDE = [
    ("Oral · tarea 2 (foto)", "La primera pregunta de la lámina: ¿cómo son las personas? ¿Qué ropa llevan? Todo son equipos: la ropa, los colores, el pelo.",
     "[fs:La ^chica] lleva [fp:unas ^gafas negras] y [ms:un ^abrigo largo]. Tiene [ms:el ^pelo rizado]."),
    ("Oral · tarea 1 (monólogo)", "Temas como «una persona de mi familia» o «una persona importante en mi vida».",
     "[fs:Mi ^abuela] es [fs:muy alegre]. [fp:Sus ^manos] son [fp:pequeñas] y siempre está en [fs:su ^cocina]."),
    ("Escritura · tarea 1 (correo)", "Presentar a tu familia, describir tu piso nuevo, contar cómo son tus compañeros.",
     "[mp:Mis ^compañeros] son [mp:muy simpáticos]. [ms:Nuestro ^piso] es [ms:pequeño], pero tiene [fs:una ^terraza grande]."),
    ("Escritura · tarea 2 (biografía, blog)", "Describir a una persona famosa o importante, o un lugar.",
     "Era [fs:una ^mujer tranquila] y [fs:muy trabajadora]. [mp:Sus ^libros] tienen [fs:mucha ^fuerza]."),
    ("Lectura · tarea 3 (textos de personas)", "Las preguntas dicen lo mismo con otras palabras: «su hermana» o «la hermana de Elena»; mira bien de quién habla.",
     "Elena vive con [fs:su ^hermana] y [mp:sus ^padres] viven en el pueblo."),
]
# Errores tipicos: (mal, bien marcado, porque)
ERRORES = [
    ("Tengo muchos amigos. Mis amigo de Italia viene mañana.", "[ms:Mi ^amigo] de Italia viene mañana. / [mp:Mis ^amigos] de Italia vienen mañana.",
     "<i>Mis</i> (varios) y <i>amigo</i> (uno) no son del mismo equipo."),
    ("Tengo la problema con mi ordenador.", "Tengo [ms:un ^problema] con mi ordenador.",
     "<i>Problema</i> es masculino, aunque termina en -a."),
    ("Las gente de mi ciudad son muy abiertas.", "[fs:La ^gente] de mi ciudad es [fs:muy abierta].",
     "<i>Gente</i> es una palabra singular: la gente <b>es</b>."),
    ("Nuestro casa tiene tres habitaciones.", "[fs:Nuestra ^casa] tiene tres habitaciones.",
     "El posesivo mira a la cosa: <i>casa</i> es femenino."),
    ("Mi hermano vive en Bilbao con su hijos.", "Mi hermano vive en Bilbao con [mp:sus ^hijos].",
     "Un dueño, pero varios hijos: <i>sus</i>."),
    ("En la foto hay unas chicas simpático.", "En la foto hay [fp:unas ^chicas simpáticas].",
     "El adjetivo también lleva la camiseta del nombre: femenino y varios."),
    ("En el mercado hay mucho personas.", "En el mercado hay [fp:muchas ^personas].",
     "<i>Mucho</i> se viste como el nombre: <i>personas</i> es femenino y varios."),
    ("Mi madre es alto y tiene el pelo rubia.", "[fs:Mi ^madre] es [fs:alta] y tiene [ms:el ^pelo rubio].",
     "Cada adjetivo mira a SU capitán: <i>madre</i> (femenino) y <i>pelo</i> (masculino)."),
]

# ------------------------------------------------------------------ EJERCICIOS DE OPCION MULTIPLE
# q (con un ____), o (la PRIMERA es la buena), why
P_FORMA = [
    {"q": "Tengo ____ amigos en Valencia.", "o": ["muchos", "mucho", "muchas"],
     "why": "El capitán es <i>amigos</i>: masculino y varios. <i>Mucho</i> se pone su camiseta: <b>muchos</b>."},
    {"q": "En mi barrio vive ____ gente mayor.", "o": ["mucha", "muchas", "mucho"],
     "why": "<i>Gente</i> es una palabra femenina y singular: <b>mucha</b> gente."},
    {"q": "Mi hermana es muy ____.", "o": ["alta", "alto", "altas"],
     "why": "El adjetivo mira a su capitán, <i>hermana</i>: femenino, uno."},
    {"q": "Lleva unos pantalones ____.", "o": ["azules", "azul", "azulos"],
     "why": "<i>Azul</i> termina en consonante: no cambia en femenino, pero en plural lleva <b>-es</b>."},
    {"q": "Ayer tuve ____ problema con el móvil.", "o": ["un", "una", "unos"],
     "why": "<i>Problema</i> engaña: termina en -a, pero es masculino. <b>Un</b> problema."},
    {"q": "¿Me enseñas ____ foto de tu boda?", "o": ["la", "el", "los"],
     "why": "<i>Foto</i> engaña: termina en -o, pero es femenino (la fotografía)."},
    {"q": "Mis abuelos tienen una casa muy ____ en el pueblo.", "o": ["grande", "granda", "grandes"],
     "why": "<i>Grande</i> termina en -e: igual en masculino y femenino. <i>Casa</i> es una: <b>grande</b>."},
    {"q": "Las chicas de la foto parecen muy ____.", "o": ["simpáticas", "simpáticos", "simpática"],
     "why": "Femenino y varios: <b>simpáticas</b>. <i>Muy</i> no cambia nunca."},
    {"q": "La gente de mi pueblo ____ muy abierta.", "o": ["es", "son", "están"],
     "why": "<i>La gente</i> es una sola palabra: el verbo también va en singular, <b>es</b>."},
    {"q": "____ día de mi cumpleaños siempre llueve.", "o": ["El", "La", "Los"],
     "why": "<i>Día</i> engaña: termina en -a, pero es masculino. <b>El</b> día."},
    {"q": "El niño lleva una camiseta ____ y unas botas rojas.", "o": ["blanca", "blanco", "blancas"],
     "why": "Cada adjetivo mira a SU capitán: <i>camiseta</i> es femenino y uno."},
    {"q": "En la clase hay ____ estudiantes nuevos.", "o": ["pocos", "poco", "pocas"],
     "why": "El capitán, <i>estudiantes nuevos</i>, es masculino y varios: <b>pocos</b>. (Si son chicas: pocas estudiantes nuevas.)"},
    {"q": "Me duele ____ mano derecha.", "o": ["la", "el", "mi"],
     "why": "<i>Mano</i> engaña: es femenino. Y con las partes del cuerpo usamos <b>la</b>, no <i>mi</i>: me duele la mano."},
    {"q": "Mis padres son ____.", "o": ["jóvenes", "joven", "jóvenas"],
     "why": "<i>Joven</i> termina en consonante: no tiene femenino; en plural, <b>jóvenes</b>."},
]
P_POS = [
    {"q": "Luis y Elena viven en Elche. ____ casa está cerca de la playa.", "o": ["Su", "Sus", "Suya"],
     "why": "Son dos dueños, pero una casa. El posesivo mira a la cosa: <b>su</b> casa."},
    {"q": "Mi hermano tiene dos perros. ____ perros se llaman Tom y Nala.", "o": ["Sus", "Su", "Suyos"],
     "why": "Un dueño y dos perros: mira la cosa, <b>sus</b> perros."},
    {"q": "Nosotros vivimos en un piso pequeño. ____ piso tiene un balcón.", "o": ["Nuestro", "Nuestra", "Nuestros"],
     "why": "El dueño (nosotros) elige <i>nuestr-</i>; la cosa (<i>piso</i>, masculino, uno) pone el final: <b>nuestro</b>."},
    {"q": "Somos tres chicas y compartimos piso. ____ cocina es muy grande.", "o": ["Nuestra", "Nuestras", "Nuestro"],
     "why": "No importa que seamos tres chicas: mira la cosa. <i>Cocina</i> es femenino y una: <b>nuestra</b>."},
    {"q": "¿Vosotros venís con ____ hijos a la fiesta?", "o": ["vuestros", "vuestro", "sus"],
     "why": "Dueños: vosotros → <i>vuestr-</i>. Cosa: <i>hijos</i>, masculino y varios → <b>vuestros</b>."},
    {"q": "Perdone, señora, ¿es este ____ paraguas?", "o": ["su", "tu", "sus"],
     "why": "Con <i>usted</i> el posesivo es <b>su</b>. <i>Paraguas</i> es uno (un paraguas), aunque termina en -s."},
    {"q": "Yo vivo con ____ abuela y ____ dos primos.", "o": ["mi / mis", "mis / mi", "mi / mi"],
     "why": "Cada cosa decide: <i>abuela</i> (una) → <b>mi</b>; <i>primos</i> (varios) → <b>mis</b>."},
    {"q": "—¿Es tu móvil? —Sí, es ____.", "o": ["mío", "mía", "mi"],
     "why": "Sin nombre detrás, la forma larga: el nombre (<i>móvil</i>, masculino) se va, pero su camiseta se queda: <b>mío</b>."},
    {"q": "Mi coche es rojo. ¿Y ____?", "o": ["el tuyo", "la tuya", "tu"],
     "why": "<i>El tuyo</i> = tu coche. Masculino, uno. <i>Tu</i> sola, sin nombre, no puede ir."},
    {"q": "Mis vacaciones son en julio. ¿Y ____?", "o": ["las tuyas", "los tuyos", "tus"],
     "why": "<i>Las tuyas</i> = tus vacaciones: femenino y varios."},
    {"q": "Ana me ha prestado ____ bici.", "o": ["su", "sus", "suya"],
     "why": "Una bici: <b>su</b>. <i>Suya</i> va sin nombre detrás (la bici es suya)."},
    {"q": "Queridos tíos: muchas gracias por ____ regalo.", "o": ["vuestro", "vuestra", "nuestro"],
     "why": "Dueños: vosotros (los tíos) → <i>vuestr-</i>; <i>regalo</i>, masculino → <b>vuestro</b>."},
]
# Bien o mal: ok = 0 (bien) o 1 (mal); fix solo en las malas
E_BIENMAL = [
    {"q": "Mis amigo de Italia viene mañana.", "ok": 1, "fix": "<b>Mi amigo</b> de Italia viene mañana.", "why": "<i>Mis</i> (varios) con <i>amigo</i> (uno): dos camisetas."},
    {"q": "Tengo la problema con mi ordenador.", "ok": 1, "fix": "Tengo <b>un problema</b> con mi ordenador.", "why": "<i>Problema</i> es masculino."},
    {"q": "Las gente de mi ciudad son muy abiertas.", "ok": 1, "fix": "<b>La gente</b> de mi ciudad <b>es</b> muy <b>abierta</b>.", "why": "<i>Gente</i> es una palabra singular y femenina."},
    {"q": "Nuestro casa tiene tres habitaciones.", "ok": 1, "fix": "<b>Nuestra casa</b> tiene tres habitaciones.", "why": "El posesivo mira a la cosa: <i>casa</i>, femenino."},
    {"q": "Mi hermano vive en Bilbao con su hijos.", "ok": 1, "fix": "Mi hermano vive en Bilbao con <b>sus hijos</b>.", "why": "Varios hijos: <i>sus</i>."},
    {"q": "En la foto hay unas chicas simpático.", "ok": 1, "fix": "En la foto hay unas chicas <b>simpáticas</b>.", "why": "El adjetivo lleva la camiseta del nombre."},
    {"q": "En el mercado hay mucho personas.", "ok": 1, "fix": "En el mercado hay <b>muchas</b> personas.", "why": "<i>Mucho</i> se viste como <i>personas</i>."},
    {"q": "La foto es muy antigua.", "ok": 0, "fix": "", "why": "Correcto: <i>la foto</i> es femenino, aunque termina en -o."},
    {"q": "Ana y Pedro viven con su hija.", "ok": 0, "fix": "", "why": "Correcto: dos dueños, una hija: <i>su</i>."},
    {"q": "Nuestras clases son por la tarde.", "ok": 0, "fix": "", "why": "Correcto: <i>clases</i> es femenino y varios."},
    {"q": "Mis padres son muy jóvenes.", "ok": 0, "fix": "", "why": "Correcto: <i>joven</i> no cambia en femenino; en plural, <i>jóvenes</i>."},
    {"q": "Mi tía lleva un vestido verde y unas sandalias blancas.", "ok": 0, "fix": "", "why": "Correcto: cada adjetivo mira a su nombre."},
]

# ------------------------------------------------------------------ TEXTOS CON HUECOS
TEXTOS = [
    {"id": "foto", "tipo": "Oral · tarea 2 · descripción de la foto", "titulo": "En la terraza",
     "texto": "En la foto hay [[unas|unos|una#gen]] chicas en la terraza de un bar. La chica de la izquierda es [[alta|alto|altas#gen]] y tiene el pelo [[rizado|rizada|rizados#gen]]. "
              "Lleva un vestido [[verde|verdes|verdo#inv]] y unas gafas de sol [[negras|negros|negra#num]]. Su amiga lleva una camiseta de rayas y unos pantalones [[cortos|cortas|corto#num]]. "
              "Al lado de la mesa hay [[una|un|unas#engana]] moto [[roja|rojo|rojas#engana]]. Al fondo hay [[mucha|muchas|mucho#gente]] gente. Las dos chicas parecen muy [[contentas|contentos|contenta#gen]]."},
    {"id": "familia", "tipo": "Escritura · tarea 1 · correo a una amiga", "titulo": "Te presento a mi familia",
     "texto": "¡Hola, Julia! Este verano vienes a casa y vas a conocer a [[mi|mis|mía#pos_cosa]] familia. Somos cinco: mis padres, mis dos hermanos y yo. "
              "[[Mi|Mis|Mío#pos_cosa]] padre es profesor y [[mi|mis|mía#pos_cosa]] madre trabaja en un hospital. [[Mis|Mi|Míos#pos_cosa]] hermanos son [[gemelos|gemelas|gemelo#gen]] y tienen doce años. "
              "Son muy [[divertidos|divertidas|divertido#num]], pero un poco [[ruidosos|ruidosas|ruidoso#num]]. Vivimos en un piso pequeño, pero [[nuestra|nuestro|nuestras#pos_cosa]] terraza es enorme: "
              "allí cenamos todas las noches de verano. Mis padres tienen [[muchas|muchos|mucha#mucho]] ganas de conocerte. Un beso, Lena"},
    {"id": "bio", "tipo": "Escritura · tarea 2 · biografía", "titulo": "Carmen Vidal, fotógrafa",
     "texto": "Carmen Vidal nació en un pueblo [[pequeño|pequeña|pequeños#gen]] de Huesca en 1948. De niña, [[su|sus|suya#pos_cosa]] padre le regaló una cámara [[antigua|antiguo|antiguas#gen]]. "
              "Con esa cámara hizo [[sus|su|suyas#pos_cosa]] primeras fotos: [[las|los|la#num]] montañas y la gente de [[su|sus|suyo#pos_cosa]] pueblo. "
              "Después vivió en Madrid y trabajó para [[muchos|muchas|mucho#mucho]] periódicos. [[Sus|Su|Suyas#pos_cosa]] fotos de la ciudad en los años setenta son muy [[famosas|famosos|famosa#engana]]. "
              "Hoy vive otra vez en el pueblo y enseña fotografía a [[los|las|el#num]] niños de la escuela."},
    {"id": "piso", "tipo": "Escritura · tarea 1 · correo a un amigo", "titulo": "Nuestro piso nuevo",
     "texto": "¡Hola, Marcos! Ya vivo en el piso nuevo con Sara y Teo. [[Nuestro|Nuestra|Nuestros#pos_cosa]] piso está en el centro y es muy [[luminoso|luminosa|luminosos#gen]]. "
              "Tiene tres habitaciones [[pequeñas|pequeños|pequeña#num]] y un salón [[grande|granda|grandes#inv]]. [[Mi|Mis|Mía#pos_cosa]] habitación tiene una ventana a la calle. "
              "El único problema es el agua: sale muy [[fría|frío|fríos#engana]] por la mañana. ¿Y tú? ¿Qué tal [[tu|tus|tuyo#pos_cosa]] nuevo trabajo? "
              "Ven a vernos con Laia: tenemos sitio para [[vuestras|vuestros|nuestras#pos_duenyo]] bicis. ¡Un abrazo!"},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
# pautas: (texto, [focos]) con focos "nom" (concordancia) o "pos" (posesivos)
LAMINAS = [
    {"id": "familia", "tarea": "Tarea 1 · correo a una amiga", "palabras": [60, 70],
     "intro": "Has recibido este mensaje de tu amiga Clara:",
     "mensaje": "¡Hola! ¡Qué bien que en agosto voy a tu casa! Pero no conozco a tu familia... ¿Cuántos sois? ¿Cómo son? Cuéntame un poco, porfa. Un beso, Clara",
     "consigna": "Escribe un correo a Clara. En él tienes que:",
     "pautas": [("saludar;", []),
                ("decirle quiénes son las personas de tu familia;", ["pos"]),
                ("describir a una de ellas: cómo es y qué ropa lleva normalmente;", ["nom"]),
                ("contarle cómo es vuestra casa;", ["pos", "nom"]),
                ("despedirte.", [])]},
    {"id": "persona", "tarea": "Tarea 2 · opción 1 · revista", "palabras": [70, 80],
     "intro": "", "mensaje": "",
     "consigna": "Una revista de estudiantes de español busca textos sobre «Una persona importante en mi vida». Escribe un texto. Habla de:",
     "pautas": [("quién es y dónde vive;", ["pos"]),
                ("cómo es físicamente;", ["nom"]),
                ("cómo es su carácter;", ["nom"]),
                ("qué cosas hacéis juntos o hacíais antes;", ["pos"]),
                ("por qué es importante para ti.", [])]},
]
FOCOS = {"nom": "concordancia", "pos": "posesivos"}

# Detector de errores tipicos (sobre el texto sin tildes y en minusculas).
# t: "r" (rojo: casi seguro un error) o "a" (ambar: mira si es un error)
_ADJ = r"(?:simpatic|alt|baj|guap|rubi|moren|delgad|gord|bonit|nuev|viej|pequen|antigu|tranquil|divertid|seri|generos|carinos|blanc|negr|amarill|roj|rizad|cort|larg|famos|ruidos|abiert|cerrad|cansad|content|nervios|preocupad|enfadad|ocupad)"
_FEMN = r"(?:madre|hermana|abuela|tia|prima|mujer|novia|amiga|hija|chica|nina|profesora|vecina|companera|jefa|senora|sobrina|nieta)"
_MASN = r"(?:padre|hermano|abuelo|tio|primo|marido|novio|amigo|hijo|chico|nino|profesor|vecino|companero|jefe|senor|sobrino|nieto)"
DETECTOR = [
    {"id": "pos_pl_sing", "t": "r",
     "re": r"\b(mis|tus|sus|nuestros|nuestras|vuestros|vuestras)\s+(?!(?:cuatro|cinco|siete|ocho|nueve|diez|once|doce|veinte|cien|mil|mejor|peor)\b)[a-z]+[a-rt-z]\b",
     "msg": "Un posesivo de «varios» (mis, tus, sus, nuestros...) con un nombre de «uno». El posesivo mira a la cosa: <b>mi amigo</b> o <b>mis amigos</b>."},
    {"id": "pos_sing_pl", "t": "r",
     "re": r"\b(mi|su|nuestro|nuestra|vuestro|vuestra)\s+(?!(?:cumpleanos|pais|mes|autobus|ingles|frances|portugues|japones|lunes|martes|miercoles|jueves|viernes|paraguas|interes|tenis|virus|bus|gas|dios|mas|tos|crisis|analisis|menos|dos|tres|seis)\b)[a-z]+s\b",
     "msg": "Un posesivo de «uno» (mi, su, nuestro...) con un nombre de «varios». Mira la cosa: <b>sus hijos</b>, <b>mis padres</b>."},
    {"id": "fem_con_a", "t": "r",
     "re": r"\b(la|una|esta|esa|mucha|poca|otra|las|unas|estas|esas|muchas|pocas|otras)\s+(problemas?|dias?|mapas?|idiomas?|temas?|programas?|sofas?|planetas?|climas?|sistemas?)\b",
     "msg": "Este nombre termina en -a, pero es <b>masculino</b>: el problema, el día, el idioma, un tema difícil."},
    {"id": "masc_con_o", "t": "r",
     "re": r"\b(el|un|este|ese|otro|los|unos|estos|esos|otros)\s+(manos?|fotos?|motos?)\b",
     "msg": "Este nombre termina en -o, pero es <b>femenino</b>: la mano, la foto, la moto."},
    {"id": "gente_pl", "t": "r",
     "re": r"\b(las|unas|muchas|pocas|algunas|los|unos|muchos|pocos|algunos|mucho|poco)\s+gente\b|\bgente\s+(son|estan|tienen|hablan|viven|van|eran|fueron|llevan|hacen|pueden|quieren|dicen)\b",
     "msg": "<b>La gente</b> es una palabra femenina y singular: la gente es, mucha gente."},
    {"id": "mucho_pl", "t": "r",
     "re": r"\b(mucho|poco|mucha|poca)\s+(?!(?:mas|menos|antes|despues|tres|seis|todos|todas|los|las|mis|tus|sus|estos|estas|esos|esas|unos|unas|nuestros|nuestras|vuestros|vuestras|ellos|ellas|nosotros|vosotros|ustedes|veces)\b)[a-z]+s\b",
     "msg": "<b>Mucho</b> y <b>poco</b> se visten como el nombre: muchos amigos, muchas personas."},
    {"id": "mucho_fem", "t": "r",
     "re": r"\b(muchos|pocos|algunos|otros|unos|los)\s+(personas|cosas|horas|veces|tiendas|ciudades|amigas|chicas|casas|playas|calles|flores|clases|plantas|fiestas)\b",
     "msg": "Ese nombre es <b>femenino</b>: muchas personas, muchas veces, unas amigas."},
    {"id": "nuestro_genero", "t": "r",
     "re": r"\b(nuestro|vuestro)\s+(?!(?:dia|problema|mapa|idioma|tema|programa|sofa|clima|sistema|planeta|papa)\b)[a-z]+a\b|\b(nuestra|vuestra)\s+(?!(?:mano|foto|moto|radio)\b)[a-z]+o\b",
     "msg": "El posesivo mira a la cosa: si la cosa es femenina, <b>nuestra / vuestra</b> (nuestra casa); si es masculina, <b>nuestro / vuestro</b>."},
    {"id": "adj_genero", "t": "a",
     "re": r"\b(la|una|mi|tu|su|esta|esa|nuestra|vuestra|las|unas|mis|tus|sus|estas|esas|nuestras|vuestras|muchas)\s+[a-z]+as?\s+(muy\s+)?" + _ADJ + r"os?\b"
           r"|\b(el|un|mi|tu|su|este|ese|nuestro|vuestro|los|unos|mis|tus|sus|estos|esos|nuestros|vuestros|muchos)\s+[a-z]+os?\s+(muy\s+)?" + _ADJ + r"as?\b",
     "msg": "¿El adjetivo lleva la camiseta de su nombre? Si el nombre es femenino, el adjetivo en -a (una camiseta blanca); si es masculino, en -o."},
    {"id": "ser_genero", "t": "a",
     "re": r"\b" + _FEMN + r"\s+(es|era|esta|parece)\s+(muy\s+|un poco\s+|bastante\s+)?" + _ADJ + r"os?\b"
           r"|\b" + _MASN + r"\s+(es|era|esta|parece)\s+(muy\s+|un poco\s+|bastante\s+)?" + _ADJ + r"as?\b",
     "msg": "Después de <b>es / está / parece</b>, el adjetivo sigue mirando al nombre: mi madre es alt<b>a</b>, mi padre es alt<b>o</b>."},
    {"id": "num_adj", "t": "a",
     "re": r"\b(unas|las|mis|tus|sus|estas|esas|muchas|nuestras)\s+[a-z]+as\s+(muy\s+)?" + _ADJ + r"a\b"
           r"|\b(unos|los|mis|tus|sus|estos|esos|muchos|nuestros)\s+[a-z]+os\s+(muy\s+)?" + _ADJ + r"o\b",
     "msg": "El nombre es de «varios», pero el adjetivo no lleva <b>-s</b>: unas chicas simpátic<b>as</b>."},
]
# Pruebas del detector: (texto, ids que tienen que saltar). El build las comprueba (en Python y en el navegador).
DETECTOR_PRUEBAS = [
    ("Mis amigo de Italia viene mañana.", ["pos_pl_sing"]),
    ("Tengo muchos amigos y mis dos hermanos viven en Roma.", []),
    ("Mis cuatro primos son muy simpáticos.", []),
    ("Mi hermano vive con su hijos en Bilbao.", ["pos_sing_pl"]),
    ("Mañana es mi cumpleaños y vienen mis padres.", []),
    ("Su país es muy bonito y su paraguas es rojo.", []),
    ("Tengo la problema con el ordenador.", ["fem_con_a"]),
    ("El día de mi cumpleaños hay un problema.", []),
    ("Esta es el foto de mi boda.", ["masc_con_o"]),
    ("La foto es antigua y me duele la mano.", []),
    ("Las gente de mi ciudad son abiertas.", ["gente_pl"]),
    ("La gente son muy simpáticas aquí.", ["gente_pl"]),
    ("En mi barrio vive mucha gente mayor.", []),
    ("En el mercado hay mucho personas.", ["mucho_pl"]),
    ("Me gusta mucho más el campo y tengo pocas cosas.", []),
    ("Hay muchos personas en la playa.", ["mucho_fem"]),
    ("Nuestro casa tiene tres habitaciones.", ["nuestro_genero"]),
    ("Nuestra piso es pequeño.", ["nuestro_genero"]),
    ("Nuestro problema es la foto: nuestra moto está rota.", []),
    ("En la foto hay unas chicas simpático.", ["adj_genero"]),
    ("Lleva una camiseta blanco y un abrigo negra.", ["adj_genero"]),
    ("Lleva una camiseta blanca y un abrigo negro.", []),
    ("Mi madre es muy alto y mi padre es baja.", ["ser_genero"]),
    ("Mi madre es alta y mi padre parece tranquilo.", []),
    ("Tengo unas amigas simpática.", ["num_adj"]),
    ("Tú vas a conocer a mis padres.", []),
    ("Trabajo mucho todos los días y como poco los lunes.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL (fotos de la tarea 2)
# Fotos de M4T2 que ya estan en WordPress (M4T2_fotoN.jpg). Solo las "como en el examen" (7-12).
# "como" = fisico y caracter (empieza con "En la foto hay"); "ropa" = que llevan (con "lleva").
MES_WP_T2 = "2026/10"
FOTOS = [
    {"id": 7, "titulo": "Antes de salir de casa",
     "alt": "Recibidor de un piso por la mañana: una madre mira la hora en el móvil, un niño con un solo zapato busca el otro en el suelo y una niña espera al lado de la puerta abierta.",
     "como": "En la foto hay [fs:una ^mujer] y [mp:dos ^niños]. [fs:La ^mujer] tiene cuarenta años, más o menos, y tiene [ms:el ^pelo castaño]. [ms:El ^niño] tiene diez años y [fs:la ^niña] es [fs:más pequeña]: tiene [fp:dos ^coletas]. [fs:La ^madre] parece [fs:nerviosa]; [fs:la ^niña], en cambio, parece [fs:muy tranquila].",
     "ropa": "[fs:La ^madre] lleva [ms:un ^abrigo gris] y [fs:una ^bufanda]. [ms:El ^niño] lleva [ms:un ^gorro] de lana y [fs:una ^mochila azul]. ¡Solo lleva [ms:un ^zapato]! [fs:La ^niña] lleva [ms:un ^abrigo rojo]."},
    {"id": 8, "titulo": "Hacer deporte",
     "alt": "Pista de pádel al aire libre: cuatro amigos se dan la mano en la red al final del partido; en un banco, botellas de agua y toallas.",
     "como": "En la foto hay [fp:dos ^mujeres] y [mp:dos ^hombres]. Tienen entre cuarenta y cincuenta años. [fs:Una ^mujer] tiene [fs:una ^coleta] y [fs:la ^otra] es [fs:morena]. [ms:Un ^hombre] es [ms:alto] y tiene [fs:una ^barba gris]; [ms:el ^otro] es [ms:más bajo]. Parecen [mp:muy simpáticos] y [mp:contentos].",
     "ropa": "Todos llevan [fs:^ropa] de deporte. [fs:La ^mujer] de la coleta lleva [fs:una ^visera blanca] y [fs:la ^otra] lleva [fp:unas ^gafas] de sol y [fs:una ^camiseta morada]. [ms:El ^hombre] alto lleva [fs:una ^cinta] en la frente y [ms:el ^otro] lleva [fs:una ^rodillera]."},
    {"id": 9, "titulo": "De compras",
     "alt": "Caja de un supermercado de barrio: un señor mayor busca la cartera, su mujer mete la compra en un carro y la cajera espera sonriendo.",
     "como": "En la foto hay [fs:una ^pareja mayor] y [fs:una ^cajera joven]. [ms:El ^señor] es [ms:calvo] y [fs:la ^señora] tiene [ms:el ^pelo corto] y [ms:blanco]. [fs:La ^cajera] tiene veinte años, más o menos, y tiene [ms:el ^pelo rizado]. Parece [fs:muy amable] y [fs:paciente].",
     "ropa": "[ms:El ^señor] lleva [fp:unas ^gafas] y [fs:una ^chaqueta] de punto [fs:marrón]. [fs:La ^señora] lleva [ms:un ^abrigo azul]. [fs:La ^cajera] lleva [ms:un ^uniforme verde] y [ms:un ^piercing pequeño] en la nariz."},
    {"id": 10, "titulo": "Clases para adultos",
     "alt": "Clase de baile para adultos en una sala con espejo: el profesor enseña un paso, una pareja mayor baila bien y un chico joven pisa a su pareja.",
     "como": "En la foto hay [fp:cinco ^personas]. [ms:El ^profesor] es [ms:joven] y tiene [ms:el ^pelo largo]. [fs:La ^pareja mayor] baila muy bien: [fs:la ^mujer] tiene [ms:el ^pelo gris] y [ms:corto]. [ms:El ^chico joven] es [ms:muy alto]. [fs:La ^chica] se ríe: parece [fs:muy simpática].",
     "ropa": "[ms:El ^profesor] lleva [fs:una ^camiseta negra]. [fs:La ^señora] lleva [ms:un ^vestido rojo] y [ms:su ^marido] lleva [fp:unas ^gafas] y [fs:una ^camisa blanca]. [fs:La ^chica] lleva [mp:unos ^vaqueros] y [fp:unas ^zapatillas]. [ms:El ^chico] lleva [fs:una ^camiseta] de rayas."},
    {"id": 11, "titulo": "Ver la televisión",
     "alt": "Salón de un piso por la noche: dos amigos saltan de alegría delante de un partido en la tele y otro se tapa la cara en el sofá; las palomitas se caen al suelo.",
     "como": "En la foto hay [mp:tres ^jóvenes]: [fs:una ^chica] y [mp:dos ^chicos]. Tienen veinticinco años, más o menos. [fs:La ^chica] tiene [ms:el ^pelo corto] y [ms:azul]. [ms:Un ^chico] es [ms:moreno] y tiene [fs:^barba]; [ms:el ^otro] es [ms:rubio]. [fs:La ^chica] y [ms:el ^chico moreno] están [mp:muy contentos].",
     "ropa": "[fs:La ^chica] lleva [fs:una ^camiseta] de fútbol. [ms:El ^chico moreno] lleva [fs:una ^gorra] y [ms:el ^chico rubio] lleva [fp:unas ^gafas] y [fs:una ^sudadera gris]. Todos llevan [fs:^ropa cómoda]: están en casa."},
    {"id": 12, "titulo": "Regalos",
     "alt": "Cafetería pequeña en otoño: una mujer abre un regalo, una bufanda de colores, y su amiga la mira; un camarero trae dos cafés y una tarta con una vela.",
     "como": "En la foto hay [fp:dos ^mujeres] y [ms:un ^camarero]. [fp:Las ^mujeres] tienen cincuenta años, más o menos. [fs:Una] tiene [ms:el ^pelo largo] y [ms:rizado]; [fs:la ^otra] tiene [ms:el ^pelo corto] y [ms:gris]. [ms:El ^camarero] es [ms:joven] y tiene [fs:^barba]. [fp:Las dos ^amigas] parecen [fp:muy contentas].",
     "ropa": "[fs:La ^mujer] del pelo rizado lleva [ms:un ^jersey amarillo]. [ms:Su ^regalo] es [fs:una ^bufanda] de colores. [fs:Su ^amiga] lleva [fp:unas ^gafas grandes] y [fs:una ^chaqueta] de cuero. [ms:El ^camarero] lleva [ms:un ^delantal negro]."},
]
