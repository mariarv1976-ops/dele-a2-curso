# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R05: MUY / MUCHO; TAMBIEN / TAMPOCO (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R05_muy_mucho.py
#
# ENFOQUE COGNITIVO (aprobado por Maria, 14/10)
#   Una pregunta para cada palabra: ¿COMO? -> MUY; ¿CUANTO? -> MUCHO. Y mira la palabra de al lado.
#   1. MUY es el BOTON DEL VOLUMEN: sube la intensidad de una cualidad (adjetivo o adverbio:
#      muy cansada, muy lejos, muy bien). No se viste nunca. No se sube dos veces (*muy mucho)
#      y no se queda solo (*Si, muy).
#   2. MUCHO es la CANTIDAD (un monton). Dos sitios: delante de un nombre se pone su camiseta
#      (como en la R04: mucha gente, muchos amigos); detras del verbo no cambia (trabajo mucho).
#      Mas, menos, mejor, peor ya comparan: llevan mucho (mucho mejor).
#   3. TAMBIEN / TAMPOCO es EL ECO: miras que dice el otro (+ o -) y decides si REPITES
#      (tambien / tampoco) o CAMBIAS (no / si). ¿Yo o a mi? Lo decide el verbo: gustar y sus
#      amigos -> a mi; los demas -> yo. Tampoco ya es un "no".
#
# MARCAS
#   [m:muy alta]       muy + lo que sube (ambar)
#   [c:mucha gente]    mucho + lo que cuenta o el verbo (turquesa)
#   [t:a mi tambien]   el eco que repite: tambien / tampoco (azul)
#   [x:a mi no]        el eco que cambia: si / no (coral)
#   Huecos:            [[correcta|distractor|distractor#motivo]]  (la primera es la buena; se barajan)
# Espanol de Espana. Ejemplos propios (ninguno sale de los materiales de Maria).

# ------------------------------------------------------------------ MOTIVOS
# clave: (familia, explicacion). La familia decide el color.
MOTIVOS = {
    "adj":   ("vol", "Detrás va un adjetivo (cómo es o cómo está): el volumen, <b>muy</b>. Muy no cambia nunca."),
    "adv":   ("vol", "Detrás va un adverbio (cerca, lejos, bien, tarde, pronto...): <b>muy</b>, que no cambia."),
    "nom":   ("can", "Detrás va un nombre: ¿cuánto? <b>Mucho</b> se pone la camiseta del nombre (mucha gente, muchos turistas)."),
    "verbo": ("can", "Va con el verbo: ¿cuánto? <b>Mucho</b>, que aquí no cambia nunca (trabajo mucho, me gusta mucho)."),
    "comp":  ("can", "Más, menos, mejor y peor ya comparan: llevan <b>mucho</b>, no muy (mucho mejor, mucho más)."),
    "expr":  ("can", "Frío, calor, viento, hambre, sueño... aquí son nombres (hace frío, tengo hambre): <b>mucho</b> con su camiseta."),
    "igual_pos": ("eco", "El otro dice algo en positivo y tú piensas lo mismo: repites con <b>también</b>."),
    "igual_neg": ("eco", "El otro dice algo con <i>no</i> y tú piensas lo mismo: repites con <b>tampoco</b> (tampoco ya es un no)."),
    "cambio":    ("eco", "Tú piensas lo contrario: cambias. Después de algo positivo, <b>no</b>; después de un no, <b>sí</b>."),
}
FAMILIAS = {"vol": "muy: el volumen", "can": "mucho: la cantidad", "eco": "el eco"}

# ------------------------------------------------------------------ 1. MUY Y MUCHO
# Parejas: frase con muy (a) y frase con mucho (b). kind de b: "nom" (con camiseta bt), "verb" o "comp".
PAREJAS = [
    {"tema": "el frío",
     "a": "El agua del mar está [m:muy fría].",
     "ea": "<i>Fría</i> es un adjetivo: dice <b>cómo</b> está el agua. <b>Muy</b> sube el volumen y no cambia.",
     "b": "En enero hace [c:mucho frío].", "kind": "nom", "bt": "ms",
     "eb": "Aquí <i>frío</i> es un nombre (hace frío, tengo frío). <b>¿Cuánto</b> frío? <b>Mucho</b>, con la camiseta de <i>frío</i>: masculino, uno."},
    {"tema": "cansada",
     "a": "Hoy estoy [m:muy cansada].",
     "ea": "<i>Cansada</i> dice cómo estoy: <b>muy</b>. Si lo dice un chico: muy cansado. Muy no se viste.",
     "b": "Hoy he trabajado [c:mucho].", "kind": "verb",
     "eb": "Detrás del verbo: <b>¿cuánto</b> he trabajado? <b>Mucho</b>. Aquí no cambia nunca: ella trabaja mucho, ellos trabajan mucho."},
    {"tema": "la playa",
     "a": "La playa está [m:muy cerca].",
     "ea": "<i>Cerca</i> es un adverbio (dónde): <b>muy</b> cerca, muy lejos.",
     "b": "En verano hay [c:muchos turistas].", "kind": "nom", "bt": "mp",
     "eb": "Delante del nombre: <b>muchos</b> lleva la camiseta de <i>turistas</i>: masculino y varios."},
    {"tema": "la plaza",
     "a": "La plaza es [m:muy bonita].",
     "ea": "<i>Bonita</i> dice cómo es la plaza: <b>muy</b>. Nunca «mucho bonita».",
     "b": "Los sábados hay [c:mucha gente].", "kind": "nom", "bt": "fs",
     "eb": "<i>Gente</i> es un nombre femenino y singular: <b>mucha</b> gente. Nunca «muy gente»."},
    {"tema": "el pueblo",
     "a": "Mi pueblo es [m:muy tranquilo].",
     "ea": "<b>Muy</b> + adjetivo: el volumen de <i>tranquilo</i> sube.",
     "b": "Me gusta [c:mucho].", "kind": "verb",
     "eb": "Con <i>me gusta</i> no hay adjetivo: ¿cuánto me gusta? <b>Mucho</b>. Nunca «me gusta muy»."},
    {"tema": "hablar español",
     "a": "Hablas español [m:muy bien].",
     "ea": "<i>Bien</i> es un adverbio (cómo hablas): <b>muy</b> bien.",
     "b": "Ahora hablas [c:mucho mejor] que en septiembre.", "kind": "comp",
     "eb": "<i>Mejor</i> ya compara (antes y ahora): la diferencia es grande, <b>mucho</b> mejor. Nunca «muy mejor»."},
]

# Lo que va al lado: (titulo, clase, ejemplos)
LADO = [
    ("muy + adjetivo", "vol", ["[m:muy alto], [m:muy alta], [m:muy altos]", "[m:muy cansado], [m:muy contenta]", "[m:muy caro], [m:muy barato]"]),
    ("muy + adverbio", "vol", ["[m:muy bien], [m:muy mal]", "[m:muy cerca], [m:muy lejos]", "[m:muy pronto], [m:muy tarde]"]),
    ("mucho/a/os/as + nombre", "can", ["[c:mucho tiempo], [c:mucho dinero]", "[c:mucha gente], [c:mucha hambre]", "[c:muchos amigos], [c:muchas veces]"]),
    ("verbo + mucho", "can", ["trabajo [c:mucho], llueve [c:mucho]", "me gusta [c:mucho], me duele [c:mucho]", "—¿Te gusta? —Sí, [c:mucho]."]),
    ("mucho + más, menos, mejor, peor", "can", ["[c:mucho más] caro", "[c:mucho mejor], [c:mucho peor]", "[c:mucho menos] gente"]),
]

# Avisos (los cierres del volumen): (titulo, bien, mal, explicacion)
CIERRES = [
    ("El volumen no se sube dos veces", "Me gusta [c:muchísimo].", "Me gusta muy mucho.",
     "<b>Muy mucho</b> no existe. Si quieres más: <b>muchísimo</b> (o muy, muy bonito, hablando)."),
    ("Muy no se queda solo", "—¿Te gusta? —Sí, [c:mucho].", "—¿Te gusta? —Sí, muy.",
     "Muy necesita una palabra detrás (muy bonito, muy bien). Sola, al final, va <b>mucho</b>."),
    ("Hace frío, tengo hambre: son nombres", "Hace [c:mucho calor] y tengo [c:mucha sed].", "Hace muy calor y tengo muy sed.",
     "Con <i>hacer</i> (frío, calor, viento, sol) y con <i>tener</i> (hambre, sed, sueño, miedo, prisa) van nombres: <b>mucho</b> con su camiseta. Pero: la sopa está [m:muy caliente]."),
    ("Muy mayor sí existe", "Mi abuela es [m:muy mayor]. Mi hermano es [c:mucho mayor] que yo.", "",
     "<i>Mayor</i> como «con muchos años» es un adjetivo: <b>muy</b> mayor. Pero si comparas (mayor que), <b>mucho</b> mayor."),
    ("Poco funciona igual", "Hay [c:poca gente]. Duermo [c:poco]. Es [m:muy poco].", "",
     "<b>Poco</b> es el contrario de mucho: se viste delante del nombre (pocos amigos) y no cambia detrás del verbo. <i>Muy poco</i> está bien."),
]

# ------------------------------------------------------------------ 2. EL ECO
# Frases del constructor: f, s (+/-), g (True = gustar y amigos -> "a mi"), igual (texto largo), dif (texto largo).
# El build calcula la respuesta corta (A mi tambien, Yo no...) y comprueba que el texto largo empieza con ella.
ECO_FRASES = [
    {"f": "Me encanta el mar.", "s": "+", "g": True, "igual": "A mí también. Me encanta nadar.", "dif": "A mí no. Prefiero la montaña."},
    {"f": "No me gusta madrugar.", "s": "-", "g": True, "igual": "A mí tampoco. Me levanto tarde siempre que puedo.", "dif": "A mí sí. Por la mañana estoy muy bien."},
    {"f": "Vivo cerca del centro.", "s": "+", "g": False, "igual": "Yo también. Voy andando a todas partes.", "dif": "Yo no. Vivo un poco lejos."},
    {"f": "No tengo mucho tiempo libre.", "s": "-", "g": False, "igual": "Yo tampoco. Trabajo mucho.", "dif": "Yo sí. Por las tardes estoy libre."},
    {"f": "Me interesa mucho la historia.", "s": "+", "g": True, "igual": "A mí también. Leo muchos libros de historia.", "dif": "A mí no. Me aburre un poco."},
    {"f": "No sé cocinar.", "s": "-", "g": False, "igual": "Yo tampoco. En casa cocina mi pareja.", "dif": "Yo sí. Cocino bastante bien."},
    {"f": "Hago deporte todos los días.", "s": "+", "g": False, "igual": "Yo también. Corro por la playa.", "dif": "Yo no. No tengo tiempo."},
    {"f": "No me gustan las películas de miedo.", "s": "-", "g": True, "igual": "A mí tampoco. Prefiero las comedias.", "dif": "A mí sí. Me encantan."},
]
# ¿Yo o a mi?: dos columnas de ejemplos (frase del otro, respuesta marcada)
YO_AMI = {
    "yo": [("Vivo en Elche.", "[t:Yo también]."), ("No tengo coche.", "[t:Yo tampoco]."), ("Hablo alemán.", "[x:Yo no]."), ("No fumo.", "[x:Yo sí].")],
    "ami": [("Me gusta el jazz.", "[t:A mí también]."), ("No me gusta el frío.", "[t:A mí tampoco]."), ("Me encanta el fútbol.", "[x:A mí no]."), ("No me interesa la política.", "[x:A mí sí].")],
}
GUSTAR_AMIGOS = "gustar, encantar, interesar, apetecer, doler, preocupar, aburrir"
# Tampoco ya es un no: (frase bien marcada, explicacion)
TAMPOCO = [
    ("—No tengo hambre. —[t:Yo tampoco].", "Corto: <b>tampoco</b> solo. Ya dice «no»."),
    ("Mi hermana [t:tampoco] come carne.", "Tampoco <b>delante</b> del verbo: sin <i>no</i>."),
    ("Mi hermana no come carne [t:tampoco].", "Tampoco <b>detrás</b> del verbo: entonces sí, con <i>no</i> delante del verbo."),
    ("A mí [t:tampoco] me gusta.", "Con gustar: <b>a mí tampoco me gusta</b>. Nunca «a mí también no me gusta»."),
]
# Devolver la pregunta (oral, tarea 3)
DEVOLVER = [("¿Y tú?", "verbos normales: Yo vivo en Murcia, ¿y tú?"), ("¿Y a ti?", "gustar y sus amigos: Me encanta el cine, ¿y a ti?"),
            ("¿Y usted? / ¿Y a usted?", "con usted (tienda, consulta): ¿Y a usted le gusta?")]

# ------------------------------------------------------------------ 3. EN EL EXAMEN
DONDE = [
    ("Oral · tarea 3 (diálogo)", "El examinador te dice qué le gusta o qué piensa: reaccionas en un segundo y devuelves la pregunta. Contestar solo «sí» o «no» es poco.",
     "—Me encanta la comida italiana. —¡[t:A mí también]! ¿Vamos a una pizzería? —No me gusta ir en coche. —[x:A mí sí], pero vamos en tren si quieres."),
    ("Oral · tarea 1 (monólogo)", "Muy y mucho dan color a tu monólogo: tu plato favorito, tu ciudad, tus vacaciones.",
     "La paella me gusta [c:mucho] y la como [c:muchas veces]: es [m:muy fácil] y mi madre la hace [m:muy bien]."),
    ("Oral · tarea 2 (foto)", "¿Cómo están las personas? ¿Qué hay? Mucha gente, muy contentos, mucho calor.",
     "En la foto hay [c:mucha gente]. Hace [c:mucho sol] y las personas parecen [m:muy contentas]."),
    ("Escritura · tarea 1 (correo)", "Contestas el correo de un amigo: reaccionas a lo que te cuenta y le describes tu ciudad o tu casa.",
     "Dices que no te gusta el invierno: ¡[t:a mí tampoco]! Aquí hace [c:mucho frío] y la calefacción es [m:muy cara]."),
    ("Escritura · tarea 2 (blog, revista)", "Describir un lugar, contar un viaje o una fiesta: casi todas las frases piden muy o mucho.",
     "Mi barrio es [m:muy tranquilo], pero tiene [c:muchas tiendas] y me gusta [c:mucho]."),
    ("Auditiva y lectura", "En las conversaciones, «yo también», «a mí tampoco» o «yo no» te dicen quién está de acuerdo: escucha la reacción, no solo la primera frase.",
     "—Yo el sábado no puedo ir. —[t:Yo tampoco]. (Ninguno de los dos va.)"),
]
# Errores tipicos: (mal, bien marcado, porque)
ERRORES = [
    ("Valencia es mucho bonita.", "Valencia es [m:muy bonita].", "<i>Bonita</i> es un adjetivo: el volumen, <b>muy</b>."),
    ("En la playa hay muy gente.", "En la playa hay [c:mucha gente].", "<i>Gente</i> es un nombre: la cantidad, <b>mucha</b>."),
    ("Hoy estoy mucho cansado.", "Hoy estoy [m:muy cansado].", "<i>Cansado</i> dice cómo estoy: <b>muy</b>."),
    ("Me gusta muy el cine.", "Me gusta [c:mucho] el cine.", "Con el verbo, <b>mucho</b>. Muy necesita un adjetivo o un adverbio."),
    ("Me gusta muy mucho.", "Me gusta [c:muchísimo].", "El volumen no se sube dos veces: <b>muchísimo</b>."),
    ("Hay mucho personas en el mercado.", "Hay [c:muchas personas] en el mercado.", "Delante del nombre, mucho se viste: <b>muchas</b> personas."),
    ("—No me gusta el frío. —Yo también no.", "—No me gusta el frío. —[t:A mí tampoco].", "Para repetir un no: <b>tampoco</b>. Y con gustar: <b>a mí</b>."),
    ("A mí también no me gusta el café.", "A mí [t:tampoco] me gusta el café.", "<b>También no</b> no existe: <b>tampoco</b>."),
    ("Yo tampoco me gusta bailar.", "A mí [t:tampoco] me gusta bailar.", "Con gustar la persona va con <b>a</b>: a mí, a ti, a él."),
    ("En invierno hace muy frío.", "En invierno hace [c:mucho frío].", "Con hacer, <i>frío</i> es un nombre: <b>mucho</b>."),
    ("Ahora hablo muy mejor.", "Ahora hablo [c:mucho mejor].", "<i>Mejor</i> ya compara: <b>mucho</b> mejor."),
]

# ------------------------------------------------------------------ EJERCICIOS DE OPCION MULTIPLE
# q (con un ____), o (la PRIMERA es la buena), why
P_MM = [
    {"q": "Mi abuela es ____ simpática.", "o": ["muy", "mucha", "mucho"], "why": "<i>Simpática</i> es un adjetivo: el volumen, <b>muy</b>."},
    {"q": "En agosto hay ____ turistas en la playa.", "o": ["muchos", "mucho", "muy"], "why": "Delante del nombre: <b>muchos</b>, con la camiseta de <i>turistas</i>."},
    {"q": "Me gusta ____ el chocolate.", "o": ["mucho", "muy", "mucha"], "why": "Con el verbo (me gusta): <b>mucho</b>, que no cambia."},
    {"q": "La estación está ____ lejos de mi casa.", "o": ["muy", "mucho", "mucha"], "why": "<i>Lejos</i> es un adverbio: <b>muy</b>."},
    {"q": "Hoy hace ____ calor.", "o": ["mucho", "muy", "mucha"], "why": "Con hacer, <i>calor</i> es un nombre (masculino): <b>mucho</b> calor."},
    {"q": "No puedo salir: tengo ____ trabajo.", "o": ["mucho", "muy", "mucha"], "why": "<i>Trabajo</i> es un nombre masculino: <b>mucho</b> trabajo."},
    {"q": "Tu casa es ____ más grande que la mía.", "o": ["mucho", "muy", "mucha"], "why": "<i>Más</i> ya compara: <b>mucho</b> más."},
    {"q": "Estoy ____ cansada porque he dormido poco.", "o": ["muy", "mucho", "mucha"], "why": "<i>Cansada</i> dice cómo estoy: <b>muy</b> (nunca «mucha cansada»)."},
    {"q": "En la fiesta había ____ gente.", "o": ["mucha", "muy", "muchas"], "why": "<i>Gente</i>: femenino y singular. <b>Mucha</b> gente."},
    {"q": "—¿Te gustó la película? —Sí, ____.", "o": ["mucho", "muy", "mucha"], "why": "Al final, solo: <b>mucho</b>. Muy nunca se queda solo."},
    {"q": "Mi hermano estudia ____ para el examen.", "o": ["mucho", "muy", "muchos"], "why": "Detrás del verbo: <b>mucho</b>, sin cambiar."},
    {"q": "Tengo ____ hambre: ¿comemos ya?", "o": ["mucha", "muy", "muchas"], "why": "<i>Hambre</i> es un nombre femenino: <b>mucha</b> hambre."},
    {"q": "Ahora hablas español ____ mejor.", "o": ["mucho", "muy", "mucha"], "why": "<i>Mejor</i> ya compara: <b>mucho</b> mejor."},
    {"q": "Las clases son ____ interesantes.", "o": ["muy", "muchas", "mucho"], "why": "<i>Interesantes</i> es un adjetivo: <b>muy</b>, que no tiene plural."},
    {"q": "Esta semana he ido ____ veces al gimnasio.", "o": ["muchas", "muchos", "muy"], "why": "<i>Veces</i> es femenino y varios: <b>muchas</b> veces."},
    {"q": "Llegamos ____ tarde a la estación.", "o": ["muy", "mucho", "mucha"], "why": "<i>Tarde</i> aquí es un adverbio (cuándo): <b>muy</b> tarde."},
]
# ¿Que dices tu? s/g/a: lo que dice el otro (+/-), si es gustar y amigos, y si piensas lo mismo (1) o lo contrario (0).
# El build comprueba que la primera opcion es la respuesta que sale de la regla.
P_ECO = [
    {"q": "Examinador: «Me encanta viajar en tren.» Tú piensas lo mismo. Tú: «____»", "s": "+", "g": True, "a": 1,
     "o": ["A mí también.", "Yo también.", "A mí tampoco."], "why": "Positivo y piensas lo mismo: <b>también</b>. Encantar es como gustar: <b>a mí</b>."},
    {"q": "Examinador: «No me gusta el café.» Tú piensas lo mismo. Tú: «____»", "s": "-", "g": True, "a": 1,
     "o": ["A mí tampoco.", "A mí también no.", "Yo tampoco."], "why": "Repites un no: <b>tampoco</b>. Con gustar: <b>a mí</b>."},
    {"q": "Examinador: «Trabajo los sábados.» Tú no. Tú: «____»", "s": "+", "g": False, "a": 0,
     "o": ["Yo no.", "A mí no.", "Yo tampoco."], "why": "Cambias un positivo: <b>no</b>. Trabajar es un verbo normal: <b>yo</b>."},
    {"q": "Examinador: «No tengo coche.» Tú tampoco tienes. Tú: «____»", "s": "-", "g": False, "a": 1,
     "o": ["Yo tampoco.", "Yo también no.", "A mí tampoco."], "why": "Repites un no: <b>yo tampoco</b>. «También no» no existe."},
    {"q": "Examinador: «Me duele mucho la espalda.» A ti también te duele. Tú: «____»", "s": "+", "g": True, "a": 1,
     "o": ["A mí también.", "Yo también.", "A mí sí."], "why": "Doler funciona como gustar (me duele): <b>a mí también</b>."},
    {"q": "Examinador: «No sé nadar.» Tú sí sabes. Tú: «____»", "s": "-", "g": False, "a": 0,
     "o": ["Yo sí.", "Yo también.", "A mí sí."], "why": "Cambias un no: <b>sí</b>. Saber es un verbo normal: <b>yo</b>."},
    {"q": "Examinador: «Me gustan mucho los perros.» A ti no. Tú: «____»", "s": "+", "g": True, "a": 0,
     "o": ["A mí no.", "Yo no.", "A mí tampoco."], "why": "Cambias un positivo: <b>no</b>. Con gustar: <b>a mí</b>."},
    {"q": "Examinador: «Vivo con mis padres.» Tú también. Tú: «____»", "s": "+", "g": False, "a": 1,
     "o": ["Yo también.", "A mí también.", "Yo tampoco."], "why": "Vivir es un verbo normal: <b>yo también</b>."},
    {"q": "Examinador: «No me interesa el fútbol.» A ti sí. Tú: «____»", "s": "-", "g": True, "a": 0,
     "o": ["A mí sí.", "A mí también.", "Yo sí."], "why": "Cambias un no: <b>sí</b>. Interesar es como gustar: <b>a mí</b>."},
    {"q": "Examinador: «Voy al gimnasio todas las semanas.» Tú no. Tú: «____»", "s": "+", "g": False, "a": 0,
     "o": ["Yo no.", "Yo tampoco.", "A mí no."], "why": "Cambias un positivo: <b>yo no</b>. Tampoco solo repite un no."},
    {"q": "Yo no fumo y mi novio ____ fuma.", "o": ["tampoco", "también", "no"],
     "why": "Repites un no y va delante del verbo: <b>tampoco</b>, sin otro no."},
    {"q": "A Pablo no le gusta el teatro y a Lucía ____.", "o": ["tampoco", "también no", "no también"],
     "why": "Repites un no: <b>a Lucía tampoco</b>."},
]
# Bien o mal: ok = 0 (bien) o 1 (mal); fix solo en las malas
E_BIENMAL = [
    {"q": "Valencia es mucho bonita.", "ok": 1, "fix": "Valencia es <b>muy</b> bonita.", "why": "Adjetivo: <i>muy</i>."},
    {"q": "En la playa hay muy gente.", "ok": 1, "fix": "En la playa hay <b>mucha</b> gente.", "why": "Nombre: <i>mucha</i>, con la camiseta de <i>gente</i>."},
    {"q": "Hoy estoy mucho cansado.", "ok": 1, "fix": "Hoy estoy <b>muy</b> cansado.", "why": "Adjetivo: <i>muy</i>."},
    {"q": "Me gusta muy el cine.", "ok": 1, "fix": "Me gusta <b>mucho</b> el cine.", "why": "Con el verbo: <i>mucho</i>."},
    {"q": "Me gusta muy mucho.", "ok": 1, "fix": "Me gusta <b>muchísimo</b>.", "why": "<i>Muy mucho</i> no existe."},
    {"q": "Hay mucho personas en el mercado.", "ok": 1, "fix": "Hay <b>muchas</b> personas en el mercado.", "why": "Mucho se viste como <i>personas</i>."},
    {"q": "—No me gusta el frío. —Yo también no.", "ok": 1, "fix": "—No me gusta el frío. —<b>A mí tampoco</b>.", "why": "Repites un no con gustar: <i>a mí tampoco</i>."},
    {"q": "A mí también no me gusta el café.", "ok": 1, "fix": "A mí <b>tampoco</b> me gusta el café.", "why": "<i>También no</i> = <i>tampoco</i>."},
    {"q": "Yo tampoco me gusta bailar.", "ok": 1, "fix": "<b>A mí</b> tampoco me gusta bailar.", "why": "Con gustar: <i>a mí</i>."},
    {"q": "En invierno hace muy frío.", "ok": 1, "fix": "En invierno hace <b>mucho</b> frío.", "why": "Con hacer, <i>frío</i> es un nombre."},
    {"q": "Me gusta muy poco el fútbol.", "ok": 0, "fix": "", "why": "Correcto: <i>muy poco</i> (el volumen de poco)."},
    {"q": "Mi abuelo es muy mayor.", "ok": 0, "fix": "", "why": "Correcto: <i>mayor</i> = con muchos años, un adjetivo."},
    {"q": "—No tengo hambre. —Yo tampoco.", "ok": 0, "fix": "", "why": "Correcto: repites un no con un verbo normal."},
    {"q": "Ahora vivo mucho más cerca del trabajo.", "ok": 0, "fix": "", "why": "Correcto: <i>más</i> compara, <i>mucho más</i>."},
    {"q": "El café está muy caliente.", "ok": 0, "fix": "", "why": "Correcto: <i>caliente</i> es un adjetivo (cómo está)."},
]

# ------------------------------------------------------------------ TEXTOS CON HUECOS (pueden llevar <br> y <b>)
TEXTOS = [
    {"id": "correo", "tipo": "Escritura · tarea 1 · respuesta a una amiga", "titulo": "Querida Marta",
     "texto": "¡Hola, Marta! Gracias por tu correo. Dices que te encanta el cine: ¡a mí [[también|tampoco|sí#igual_pos]]! "
              "Y no te gusta el teatro... a mí [[tampoco|también|no#igual_neg]]: es [[muy|mucho|mucha#adj]] caro y me aburro. "
              "Pero tú no lees novelas y yo [[sí|también|tampoco#cambio]]: leo [[mucho|muy|muchas#verbo]] en el tren. "
              "Aquí en Valencia hace [[mucho|muy|mucha#expr]] calor estos días y hay [[muchos|mucho|muy#nom]] turistas. "
              "¿Vienes en junio? Es [[mucho|muy|mucha#comp]] mejor que agosto. Un beso, Irene"},
    {"id": "blog", "tipo": "Escritura · tarea 2 · blog", "titulo": "Mi ciudad",
     "texto": "Vivo en Cádiz, una ciudad [[muy|mucho|mucha#adj]] antigua. Tiene [[muchas|muchos|muy#nom]] playas y el centro está [[muy|mucho|muchos#adv]] cerca del mar. "
              "En invierno no hace [[mucho|mucha|muy#expr]] frío, pero a veces hace [[mucho|muy|mucha#expr]] viento. La gente es [[muy|mucho|mucha#adj]] abierta "
              "y en verano hay [[mucha|mucho|muchas#nom]] gente en la calle hasta tarde. Me gusta [[mucho|muy|mucha#verbo]] pasear por la playa al atardecer. "
              "Para mí, es [[mucho|muy|mucha#comp]] más bonita que las playas grandes."},
    {"id": "dialogo", "tipo": "Oral · tarea 3 · diálogo con un amigo", "titulo": "Planes para el sábado",
     "texto": "<b>Examinador:</b> El sábado no tengo planes. ¿Hacemos algo?<br>"
              "<b>Candidato:</b> ¡Vale! Yo [[tampoco|también|no#igual_neg]] tengo planes. ¿Vamos al cine?<br>"
              "<b>Examinador:</b> Mmm... no me gustan [[mucho|muy|muchas#verbo]] las películas de ahora.<br>"
              "<b>Candidato:</b> ¿No? A mí [[sí|también|tampoco#cambio]]: veo [[muchas|muchos|muy#nom]] películas. Bueno, ¿y una excursión?<br>"
              "<b>Examinador:</b> ¡Me encanta la montaña!<br>"
              "<b>Candidato:</b> ¡A mí [[también|tampoco|sí#igual_pos]]! Conozco una ruta [[muy|mucho|mucha#adj]] bonita.<br>"
              "<b>Examinador:</b> ¿Está lejos?<br>"
              "<b>Candidato:</b> No, está [[muy|mucho|mucha#adv]] cerca: a media hora en coche.<br>"
              "<b>Examinador:</b> Pero yo no tengo coche.<br>"
              "<b>Candidato:</b> Yo [[tampoco|también no|no#igual_neg]], pero mi hermana nos deja el suyo."},
    {"id": "foto", "tipo": "Oral · tarea 2 · descripción de la foto", "titulo": "En el mercado",
     "texto": "En la foto hay [[mucha|muchas|muy#nom]] gente en un mercado. Es un mercado [[muy|mucho|mucha#adj]] grande y hay [[muchas|muchos|mucha#nom]] frutas de colores. "
              "A la derecha, una señora [[muy|mucha|mucho#adj]] mayor compra tomates. Parece [[muy|mucho|mucha#adj]] contenta: creo que le gusta [[mucho|muy|mucha#verbo]] ese puesto. "
              "El vendedor trabaja [[mucho|muy|muchos#verbo]]: tiene [[muchos|mucho|muy#nom]] clientes. Seguramente hoy hace [[mucho|muy|mucha#expr]] calor, porque todos llevan ropa de verano."},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
# pautas: (texto, [focos]) con focos "vol" (muy), "can" (mucho) o "eco" (tambien / tampoco)
LAMINAS = [
    {"id": "nico", "tarea": "Tarea 1 · correo a un amigo", "palabras": [60, 70],
     "intro": "Has recibido este correo de tu amigo Nico:",
     "mensaje": "¡Hola! Te cuento cosas de mí para conocernos mejor: me encanta la música, sobre todo el rock, pero no me gusta nada bailar. Hago mucho deporte y no veo la tele. ¿Y tú? En mayo voy a tu ciudad: ¿cómo es? Un abrazo, Nico",
     "consigna": "Escribe un correo a Nico. En él tienes que:",
     "pautas": [("saludar;", []),
                ("reaccionar a sus gustos: qué cosas tenéis en común y cuáles no;", ["eco"]),
                ("describir tu ciudad: cómo es y qué hay;", ["vol", "can"]),
                ("proponerle un plan para su visita;", []),
                ("despedirte.", [])]},
    {"id": "lugar", "tarea": "Tarea 2 · opción 1 · revista", "palabras": [70, 80],
     "intro": "", "mensaje": "",
     "consigna": "Una revista de estudiantes de español busca textos sobre «Un lugar que me gusta mucho». Escribe un texto. Habla de:",
     "pautas": [("dónde está y cómo es;", ["vol"]),
                ("qué hay allí;", ["can"]),
                ("qué haces allí y con quién;", ["can"]),
                ("cuándo fuiste por primera vez;", []),
                ("por qué te gusta tanto.", ["vol", "can"])]},
]
FOCOS = {"vol": "muy", "can": "mucho", "eco": "también / tampoco"}

# Detector de errores tipicos (sobre el texto sin tildes y en minusculas).
# t: "r" (rojo: casi seguro un error) o "a" (ambar: mira si es un error)
_ADJ = (r"(?:(?:bonit|guap|fe|cansad|content|simpatic|antipatic|alt|baj|barat|pequen|tranquil|divertid|abiert|"
        r"aburrid|cerrad|nervios|preocupad|enfadad|ocupad|delgad|rapid|lent|limpi|suci|precios)(?:o|a|os|as)"
        r"|caros?|grandes?|interesantes?|importantes?|dificil(?:es)?|facil(?:es)?|amables?|alegres?|tristes?"
        r"|feliz|felices|calientes?|lejos|cerca|tarde|temprano|pronto)")
_NOM = (r"(?:gente|personas|amigos|amigas|tiempo|dinero|trabajo|cosas|turistas|trafico|ruido|coches|tiendas|"
        r"gracias|hambre|sed|sueno|miedo|prisa|suerte|ganas|paciencia|deberes|veces|anos)")
DETECTOR = [
    {"id": "muy_nombre", "t": "r",
     "re": r"\bmuy\s+" + _NOM + r"\b|\b(hace|hacia|hizo|hara|tengo|tiene|tienes|tenia|tenemos|teneis|tienen|tuve|tuvo|pase|paso|pasamos)\s+muy\s+(frio|calor|sol|viento|hambre|sed|sueno|miedo|prisa|suerte)\b",
     "msg": "Delante de un nombre (gente, tiempo, frío, hambre...) no va <b>muy</b>: es una cantidad, <b>mucho</b> con su camiseta (mucha gente, hace mucho frío)."},
    {"id": "muy_mucho", "t": "r",
     "re": r"\bmuy\s+(mucho|mucha|muchos|muchas|muchisimo|muchisima)\b",
     "msg": "<b>Muy mucho</b> no existe: el volumen no se sube dos veces. Di <b>muchísimo</b> o solo <b>mucho</b>."},
    {"id": "mucho_adj", "t": "r",
     "re": r"\b(mucho|mucha|muchos|muchas)\s+" + _ADJ + r"\b",
     "msg": "Delante de un adjetivo o de un adverbio (bonito, cansado, lejos...) va <b>muy</b>, el volumen: muy bonito, estoy muy cansado."},
    {"id": "verbo_muy", "t": "r",
     "re": r"\b(gusta|gustan|gustaba|gustaban|encanta|encantan|interesa|interesan|duele|duelen|apetece)\s+muy\b(?!\s+(poco|mucho|mucha|muchos|muchas|muchisimo)\b)"
           r"|\b(trabajo|trabaja|trabajan|estudio|estudia|estudian|llueve|llovia|duermo|duerme|viajo|viaja|leo|lee|salgo|sale|camino|corro|nado|bailo|baila)\s+muy\s+(el|la|los|las|un|una|mi|tu|su|y|en|con|cuando|porque|aqui|alli|todos|todas)\b",
     "msg": "Con el verbo no va <b>muy</b>: ¿cuánto? <b>mucho</b> (me gusta mucho, trabajo mucho)."},
    {"id": "muy_solo", "t": "r",
     "re": r"\bmuy\s*([.,;:!?)]|$)",
     "msg": "<b>Muy</b> no se queda solo al final: «Sí, <b>mucho</b>»."},
    {"id": "mucho_genero", "t": "r",
     "re": r"\b(mucho|poco|muchos|pocos)\s+(personas|cosas|horas|veces|tiendas|ciudades|amigas|chicas|casas|playas|calles|flores|clases|plantas|fiestas|frutas|peliculas|gente|hambre|agua|sed|comida|ropa|musica|lluvia|ganas)\b",
     "msg": "Mucho se viste como el nombre: ese nombre es <b>femenino</b>. Mucha gente, mucha hambre, muchas personas, muchas veces."},
    {"id": "mucho_num", "t": "r",
     "re": r"\b(mucho|poco)\s+(amigos|turistas|libros|anos|coches|ninos|estudiantes|museos|bares|restaurantes|parques|dias|meses|deportes|perros|gatos|hermanos|primos|clientes|idiomas|problemas)\b",
     "msg": "Mucho se viste como el nombre: si son <b>varios</b>, muchos (muchos amigos, pocos turistas)."},
    {"id": "muy_comp", "t": "r",
     "re": r"\bmuy\s+(mas|menos|mejor|mejores|peor|peores)\b",
     "msg": "Más, menos, mejor y peor ya comparan: llevan <b>mucho</b> (mucho mejor, mucho más)."},
    {"id": "tambien_no", "t": "r",
     "re": r"\btambien\s+no\b|\btampoco\s+no\b",
     "msg": "<b>También no</b> no existe y <b>tampoco</b> ya es un no: «yo tampoco», «a mí tampoco me gusta»."},
    {"id": "yo_gustar", "t": "r",
     "re": r"\byo\s+((tambien|tampoco|si|no)\s+)?(me|te)\s+(gusta|gustan|encanta|encantan|interesa|interesan|apetece|duele|duelen)\b",
     "msg": "Con gustar (y encantar, interesar, doler...) la persona va con <b>a</b>: <b>a mí</b> también / tampoco me gusta."},
    {"id": "no_tambien", "t": "a",
     "re": r"\bno\s+(?!solo\b)[a-z]+(\s+[a-z]+){0,2}\s+tambien\b",
     "msg": "¿Repites algo negativo? Entonces es <b>tampoco</b>: «ella no come carne tampoco» o «ella tampoco come carne»."},
    {"id": "mi_sin_a", "t": "a",
     "re": r"(^|[.,;:!?¡¿—-]\s*)mi\s+(tambien|tampoco)\b",
     "msg": "¿Falta la <b>a</b>? Se dice <b>a mí también</b> / <b>a mí tampoco</b>."},
    {"id": "ami_normal", "t": "a",
     "re": r"\ba\s+mi\s+(tambien|tampoco|si|no)\s+(?!(me|nos|no|mucho|poco|tanto|demasiado)\b)[a-z]+(o|oy)\b",
     "msg": "Con un verbo normal (vivir, trabajar, tener...) se dice <b>yo también</b>, <b>yo tampoco</b>. «A mí» es para gustar y sus amigos."},
]
# Pruebas del detector: (texto, ids que tienen que saltar). El build las comprueba (en Python y en node).
DETECTOR_PRUEBAS = [
    ("Valencia es mucho bonita.", ["mucho_adj"]),
    ("En la playa hay muy gente.", ["muy_nombre"]),
    ("Hoy estoy mucho cansado.", ["mucho_adj"]),
    ("Me gusta muy el cine.", ["verbo_muy"]),
    ("Me gusta muy mucho.", ["muy_mucho"]),
    ("Hay mucho personas en el mercado.", ["mucho_genero"]),
    ("Yo también no.", ["tambien_no"]),
    ("A mí también no me gusta el café.", ["tambien_no"]),
    ("Yo tampoco me gusta bailar.", ["yo_gustar"]),
    ("En invierno hace muy frío.", ["muy_nombre"]),
    ("Tengo muy hambre.", ["muy_nombre"]),
    ("Ahora hablo muy mejor.", ["muy_comp"]),
    ("—¿Te gusta? —Sí, muy.", ["muy_solo"]),
    ("Tengo mucho amigos en Madrid.", ["mucho_num"]),
    ("Yo tampoco no tengo coche.", ["tambien_no"]),
    ("Ella no come carne también.", ["no_tambien"]),
    ("Mí también.", ["mi_sin_a"]),
    ("A mí también vivo en Madrid.", ["ami_normal"]),
    ("Es una ciudad muy bonita y hay mucha gente.", []),
    ("Me gusta muy poco el fútbol.", []),
    ("Hablas muy bien y ahora mucho mejor.", []),
    ("Tengo muchos buenos amigos.", []),
    ("A mí tampoco me gusta bailar.", []),
    ("Yo tampoco. Mi hermana tampoco come carne.", []),
    ("El café está muy frío y la sopa muy caliente.", []),
    ("Mi abuela es muy mayor.", []),
    ("Un café para mí también, por favor.", []),
    ("No sé si Ana viene también.", []),
    ("Trabajo mucho todos los días y me gusta muchísimo.", []),
    ("Yo sí. A mí no.", []),
    ("Hace mucho calor y tengo mucha sed.", []),
    ("Hay muy pocas tiendas en mi barrio.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL 1 (reacciona)
# Frases del examinador (de tu, como en la tarea 3 de planificar): s, g, y dos reacciones largas.
# El build calcula la respuesta corta y comprueba que cada reaccion larga empieza con ella.
ORAL = [
    {"f": "Me encanta el verano.", "s": "+", "g": True, "igual": "A mí también. Voy mucho a la playa.", "dif": "A mí no. Hace mucho calor."},
    {"f": "No me gusta nada el invierno.", "s": "-", "g": True, "igual": "A mí tampoco. Hace mucho frío.", "dif": "A mí sí. Me encanta la nieve."},
    {"f": "Vivo muy cerca de aquí.", "s": "+", "g": False, "igual": "Yo también. Vengo andando.", "dif": "Yo no. Vivo bastante lejos."},
    {"f": "No tengo hermanos.", "s": "-", "g": False, "igual": "Yo tampoco. En casa somos tres: mis padres y yo.", "dif": "Yo sí. Tengo dos hermanas."},
    {"f": "Me gusta mucho cocinar.", "s": "+", "g": True, "igual": "A mí también. Hago una paella muy buena.", "dif": "A mí no. Cocino muy poco."},
    {"f": "No me gustan las fiestas grandes.", "s": "-", "g": True, "igual": "A mí tampoco. Prefiero cenar con pocos amigos.", "dif": "A mí sí. Me encanta bailar."},
    {"f": "Trabajo mucho los fines de semana.", "s": "+", "g": False, "igual": "Yo también. Termino muy tarde.", "dif": "Yo no. Los sábados descanso."},
    {"f": "No sé hablar inglés.", "s": "-", "g": False, "igual": "Yo tampoco. Solo sé decir hola.", "dif": "Yo sí. Lo estudié en el colegio."},
    {"f": "Me interesan mucho los museos.", "s": "+", "g": True, "igual": "A mí también. Voy mucho al Prado.", "dif": "A mí no. Prefiero pasear."},
    {"f": "No me apetece salir esta noche.", "s": "-", "g": True, "igual": "A mí tampoco. Prefiero ver una película en casa.", "dif": "A mí sí. ¿Vamos a cenar?"},
    {"f": "Voy al trabajo en bici.", "s": "+", "g": False, "igual": "Yo también. Es muy práctico.", "dif": "Yo no. Voy en autobús."},
    {"f": "No como carne.", "s": "-", "g": False, "igual": "Yo tampoco. Como mucha verdura.", "dif": "Yo sí. Me gusta mucho el pollo."},
    {"f": "Me duele mucho la cabeza.", "s": "+", "g": True, "igual": "A mí también. Hay mucho ruido aquí.", "dif": "A mí no. Estoy muy bien."},
    {"f": "No veo mucho la tele.", "s": "-", "g": False, "igual": "Yo tampoco. Veo series en el móvil.", "dif": "Yo sí. La veo todas las noches."},
    {"f": "Me gustan mucho los perros.", "s": "+", "g": True, "igual": "A mí también. Tengo uno muy pequeño.", "dif": "A mí no. Prefiero los gatos."},
    {"f": "No tengo mucho tiempo libre.", "s": "-", "g": False, "igual": "Yo tampoco. Trabajo mucho.", "dif": "Yo sí. Por las tardes estoy libre."},
]

# ------------------------------------------------------------------ AHORA TU: ORAL 2 (la foto con muy y mucho)
# Fotos de M4T2 que ya estan en WordPress (M4T2_fotoN.jpg). Solo las "como en el examen" (7-12).
MES_WP_T2 = "2026/10"
FOTOS = [
    {"id": 7, "titulo": "Antes de salir de casa",
     "alt": "Recibidor de un piso por la mañana: una madre mira la hora en el móvil, un niño con un solo zapato busca el otro en el suelo y una niña espera al lado de la puerta abierta.",
     "mm": "En la foto hay una madre y dos niños en el recibidor de su casa. Es [m:muy temprano] y la madre tiene [c:mucha prisa]: mira la hora en el móvil y parece [m:muy nerviosa]. "
           "El niño busca su zapato; creo que no le gusta [c:mucho] madrugar. La niña está [m:muy tranquila] al lado de la puerta. Seguramente llegan [m:muy tarde] al colegio."},
    {"id": 8, "titulo": "Hacer deporte",
     "alt": "Pista de pádel al aire libre: cuatro amigos se dan la mano en la red al final del partido; en un banco, botellas de agua y toallas.",
     "mm": "En la foto hay cuatro amigos en una pista de pádel. Hace [c:mucho sol] y en el banco hay [c:muchas botellas] de agua. Están [m:muy cansados], pero parecen [m:muy contentos]. "
           "Creo que juegan [c:mucho] juntos: son amigos desde hace [c:muchos años]. Ahora se dan la mano: ha sido un partido [m:muy bonito]."},
    {"id": 9, "titulo": "De compras",
     "alt": "Caja de un supermercado de barrio: un señor mayor busca la cartera, su mujer mete la compra en un carro y la cajera espera sonriendo.",
     "mm": "En la foto hay una pareja mayor en la caja de un supermercado. El señor es [m:muy mayor] y busca la cartera: tarda [c:mucho]. Su mujer mete [c:muchas cosas] en el carro. "
           "La cajera es [m:muy amable]: espera y sonríe. Es un supermercado pequeño y hoy no hay [c:mucha gente]."},
    {"id": 10, "titulo": "Clases para adultos",
     "alt": "Clase de baile para adultos en una sala con espejo: el profesor enseña un paso, una pareja mayor baila bien y un chico joven pisa a su pareja.",
     "mm": "En la foto hay una clase de baile para adultos. La pareja mayor baila [m:muy bien]: seguramente practica [c:mucho]. El chico joven baila [c:mucho peor]: pisa a su pareja. "
           "Ella se ríe [c:mucho] y parece [m:muy simpática]. El profesor tiene [c:mucha paciencia]."},
    {"id": 11, "titulo": "Ver la televisión",
     "alt": "Salón de un piso por la noche: dos amigos saltan de alegría delante de un partido en la tele y otro se tapa la cara en el sofá; las palomitas se caen al suelo.",
     "mm": "En la foto hay tres jóvenes en un salón por la noche. Ven un partido de fútbol y dos están [m:muy contentos]: saltan [c:mucho]. El otro chico está [m:muy triste] y se tapa la cara. "
           "Hay [c:muchas palomitas] en el suelo. Creo que les gusta [c:mucho] el fútbol."},
    {"id": 12, "titulo": "Regalos",
     "alt": "Cafetería pequeña en otoño: una mujer abre un regalo, una bufanda de colores, y su amiga la mira; un camarero trae dos cafés y una tarta con una vela.",
     "mm": "En la foto hay dos amigas en una cafetería [m:muy pequeña]. Una abre un regalo: es una bufanda de colores [m:muy bonita]. Parece [m:muy sorprendida] y [m:muy contenta]. "
           "Creo que hoy es su cumpleaños, porque hay una tarta con una vela. Seguramente son amigas desde hace [c:muchos años] y se quieren [c:mucho]."},
]
