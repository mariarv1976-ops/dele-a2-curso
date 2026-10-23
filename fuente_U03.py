# -*- coding: utf-8 -*-
# FUENTE DE LA UNIDAD 3 (fase 1) · Así somos
U = "03"
TITLE = "Así somos"
TEMA_CL3 = "su mejor amigo o amiga"
RECORDATORIO = [
 "Describir a una persona: ser (alto, delgado, moreno, rubio), tener (el pelo largo, rizado; los ojos azules; barba) y llevar (gafas, el pelo corto, una gorra).",
 "Hablar del carácter (simpático, tímido, serio, divertido, tranquilo, desordenado) y de las relaciones: llevarse bien/mal con alguien, caer bien/mal.",
 "Parecerse a alguien: Me parezco a mi madre. Nos parecemos mucho.",
 "Presentes con -zc-: conozco, parezco, conduzco, traduzco.",
 "Identificar personas: este, ese, aquel; el que lleva gafas, la que tiene el pelo rizado.",
]
TIPS_INICIO = [
 "<b>Lectura, tarea 1:</b> lee primero las preguntas. Cuando una opción describe a una persona, comprueba de quién habla el texto: muchas trampas describen a otra persona del correo.",
 "<b>Auditiva, tarea 1:</b> mira las tres imágenes antes de escuchar. Las tres aparecen en la conversación; solo una responde a la pregunta. Espera al final: a veces la persona cambia de idea.",
]
CATS = {
 "descripcion": {"name": "Descripción física (ser, tener, llevar)",
  "repaso": "Ser + adjetivo (es alto, es rubia); tener + partes del cuerpo (tiene los ojos verdes, el pelo rizado, barba); llevar + cosas que se pueden quitar (lleva gafas, una gorra, el pelo corto). En el libro: unidad 3, descripción física.",
  "reto": "Describe a tres personas de tu familia con ser, tener y llevar."},
 "caracter": {"name": "Carácter y relaciones (llevarse bien, caer bien)",
  "repaso": "Adjetivos de carácter (simpático, tímido, serio, abierto, divertido, desordenado) y relaciones: me llevo bien con mi hermano; mi jefe me cae bien (como gustar: me cae, te cae, le cae). En el libro: unidad 3, relaciones.",
  "reto": "Escribe cuatro frases: con quién te llevas bien, con quién te llevas mal, quién te cae muy bien y quién no."},
 "parecerse": {"name": "Parecerse a alguien y comparar personas",
  "repaso": "Parecerse a alguien (me parezco a mi padre), parecerse en algo (nos parecemos en el carácter) y ser diferentes. Cuidado: parecerse es reflexivo (me, te, se...). En el libro: unidad 3, el verbo parecerse.",
  "reto": "¿A quién te pareces físicamente? ¿Y de carácter? Escríbelo en tres frases."},
 "zc": {"name": "Presentes irregulares c > zc",
  "repaso": "Verbos en -cer y -ducir hacen la primera persona con -zc-: conozco, parezco, conduzco, traduzco, ofrezco. Las demás personas son regulares (conoces, conduce). En el libro: unidad 3, presentes irregulares.",
  "reto": "Escribe cinco frases sobre ti con conozco, me parezco, conduzco, traduzco y ofrezco."},
 "identificar": {"name": "Identificar personas (este, ese, aquel; el que...)",
  "repaso": "Para señalar a una persona entre varias: este/ese/aquel chico; el que lleva gafas, la que está hablando, los que tienen barba. En el libro: unidad 3, este, ese, aquel y el/la que + verbo.",
  "reto": "Mira una foto de grupo y escribe cuatro frases como: Mi prima es la que lleva un vestido rojo."},
 "familia": {"name": "Familia y relaciones de pareja",
  "repaso": "Familia (abuelo, primo, cuñado, suegra, sobrino) y pareja (novio/a, conocer a alguien, quedar, salir con alguien, casarse, separarse). En el libro: unidad 3, relaciones de pareja.",
  "reto": "Dibuja el árbol de tu familia y escribe una frase sobre cinco personas."},
}
ESTRATEGIAS_NUEVAS = {}

# ---------------- LECTURA ----------------
CL1 = {"n": 1, "type": "mail",
 "instr": "Usted va a leer el correo electrónico que Irene ha escrito a su amiga Paula. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las cinco preguntas antes del correo y subraya de quién habla cada una.",
 "head": ["De: Irene", "Para: Paula", "Asunto: ¡Por fin conozco a la familia de Marcos!"],
 "body": [
  "Hola, Paula:",
  "¿Qué tal por Santander? Yo estoy muy contenta. ¡Por fin conozco a la familia de Marcos! El sábado fuimos a comer a casa de sus padres, en Toledo, y la verdad es que me cayeron todos muy bien. Te cuento cómo son.",
  "Su madre, Carmen, es muy simpática y habla muchísimo. Es bajita, lleva gafas y tiene el pelo blanco y muy corto. Su padre es más serio y tímido, pero muy amable. Marcos se parece mucho a él: los dos son altos y delgados y tienen los mismos ojos verdes. También conocí a su hermana pequeña, Lucía, que tiene dieciséis años. Es morena, lleva el pelo largo y rizado y es muy divertida. Nos llevamos bien desde el primer momento: me enseñó fotos de Marcos de pequeño... ¡con unas gafas enormes! Toda la familia es muy cariñosa.",
  "La única persona un poco difícil es su abuelo Tomás. Vive con ellos desde el año pasado y no habla mucho con la gente que no conoce. Pero al final de la comida empezamos a hablar de fútbol y... ¡es del mismo equipo que yo! Ahora creo que le caigo bien.",
  "Y tú, ¿qué tal con tu compañero de piso nuevo? En tu último mensaje dices que no os lleváis muy bien porque es muy desordenado. ¿Habéis hablado ya? Espero que sí.",
  "Por cierto, en diciembre vamos a Santander a pasar un fin de semana. ¿Quedamos para cenar? Así conoces por fin a Marcos. ¡Tengo muchas ganas de verte!",
  "Un beso muy fuerte,<br>Irene"],
 "items": [
  {"n": 1, "q": "Irene escribe a Paula para...", "o": ["contarle cómo es la familia de su novio.", "invitarla a comer en Toledo.", "presentarle a su compañero de piso."], "ok": 0, "cats": ["familia"], "es": "ES-01",
   "why": "Todo el correo cuenta la comida con la familia de Marcos. Toledo es donde viven los padres, no una invitación; el compañero de piso es de Paula.", "pc": "FN-4 describir personas · LX-04 relaciones personales"},
  {"n": 2, "q": "Según el correo, la madre de Marcos...", "o": ["es alta y delgada.", "es muy habladora.", "es seria y tímida."], "ok": 1, "cats": ["caracter", "descripcion"], "es": "ES-08",
   "why": "«Habla muchísimo» = es muy habladora. Alto y delgado es Marcos (y su padre); serio y tímido es el padre.", "pc": "LX-02 carácter · LX-01 descripción física"},
  {"n": 3, "q": "Marcos...", "o": ["lleva gafas.", "es el hermano menor de Lucía.", "tiene los ojos como su padre."], "ok": 2, "cats": ["parecerse", "descripcion"], "es": "ES-03",
   "why": "Marcos y su padre «tienen los mismos ojos verdes». Las gafas son de la madre (y de Marcos solo en fotos de pequeño); Lucía es la hermana pequeña, así que Marcos es mayor.", "pc": "GR parecerse · LX-01"},
  {"n": 4, "q": "El abuelo de Marcos...", "o": ["habló mucho con Irene durante toda la comida.", "tiene algo en común con Irene.", "vive solo en su casa de Toledo."], "ok": 1, "cats": ["caracter"], "es": "ES-03",
   "why": "Los dos son del mismo equipo de fútbol. Al principio no habló mucho, y vive con sus hijos desde el año pasado.", "pc": "LX-02 · FN relaciones"},
  {"n": 5, "q": "En diciembre, Irene...", "o": ["quiere cenar con Paula y Marcos.", "va a conocer al compañero de piso de Paula.", "se va a vivir a Santander."], "ok": 0, "cats": ["familia"], "es": "ES-07",
   "why": "Van a Santander un fin de semana y propone quedar para cenar para que Paula conozca a Marcos. No se muda y no habla de conocer al compañero de piso.", "pc": "GR ir a + infinitivo · FN proponer"},
 ]}
CL3 = {"n": 3, "type": "people",
 "instr": "Usted va a leer tres textos de tres personas que hablan de su mejor amigo o amiga. Relacione las preguntas (14-19) con los textos (A, B o C).",
 "tip": "Tienes unos 12 minutos. Cuidado con parecerse: parecerse físicamente no es lo mismo que parecerse de carácter.",
 "texts": [
  {"name": "Marta", "body": "Mi mejor amiga se llama Sonia y la conozco desde el colegio. Físicamente somos muy diferentes: ella es alta y rubia, y yo soy bajita y morena. Pero de carácter nos parecemos mucho: las dos somos muy habladoras y un poco desordenadas. Ahora ella vive en Berlín, así que no nos vemos mucho, pero hablamos por videollamada todos los domingos. Casi nunca nos enfadamos. Bueno, una vez sí: le presté mi vestido favorito para una boda y me lo devolvió roto. ¡Estuvimos dos semanas sin hablar! Ahora nos reímos mucho cuando lo recordamos. Nuestras familias también son muy buenas amigas."},
  {"name": "Javier", "body": "Mi mejor amigo es Andrés, mi compañero de trabajo. Lo conocí hace cinco años, el primer día en la oficina. Al principio no me cayó bien: me pareció serio y un poco antipático. Pero no es antipático, es tímido. Cuando lo conoces, es la persona más divertida del mundo. Él es muy tranquilo y yo, muy nervioso, así que nos complementamos. Mucha gente piensa que somos hermanos porque nos parecemos: los dos llevamos barba y gafas y tenemos el pelo rizado. Los viernes, después del trabajo, jugamos al pádel y luego tomamos algo. Además, los dos somos muy aficionados al fútbol."},
  {"name": "Elena", "body": "Mi mejor amiga es mi hermana Clara. Tiene dos años menos que yo y vivimos juntas en un piso en el centro. Nos llevamos muy bien, aunque somos muy distintas: yo soy ordenada y tranquila, y ella es un desastre, pero es muy generosa y alegre. Su novio, Pedro, también es muy simpático. Clara es enfermera y trabaja por las noches, así que a veces solo nos vemos en el desayuno. Lo que más nos gusta es viajar juntas: el verano pasado fuimos a Portugal en coche. Siempre conduzco yo, porque ella no tiene carné. ¡Y canta durante todo el viaje!"}],
 "items": [
  {"n": 14, "q": "¿Quién comparte casa con su amiga?", "ok": 2, "cats": ["familia"], "es": "ES-03", "why": "Elena y su hermana Clara viven juntas en un piso. La amiga de Marta vive en Berlín.", "pc": "LX vivienda · FN relaciones"},
  {"n": 15, "q": "¿Quién tiene un carácter parecido al de su amiga?", "ok": 0, "cats": ["parecerse", "caracter"], "es": "ES-09", "why": "Marta: «de carácter nos parecemos mucho». Javier y Andrés se parecen físicamente, pero tienen caracteres opuestos; Elena y Clara son distintas.", "pc": "GR parecerse · LX-02"},
  {"n": 16, "q": "¿Quién se parece físicamente a su amigo?", "ok": 1, "cats": ["parecerse", "descripcion"], "es": "ES-09", "why": "Javier y Andrés llevan barba y gafas y tienen el pelo rizado. Marta y Sonia son físicamente muy diferentes.", "pc": "GR parecerse · LX-01"},
  {"n": 17, "q": "¿Quién es la única persona que conduce en los viajes?", "ok": 2, "cats": ["zc"], "es": "ES-03", "why": "Elena: «siempre conduzco yo, porque ella no tiene carné».", "pc": "GR presente c > zc"},
  {"n": 18, "q": "¿Quién tuvo una mala primera impresión de su amigo?", "ok": 1, "cats": ["caracter"], "es": "ES-03", "why": "A Javier, al principio, Andrés no le cayó bien: le pareció serio y antipático.", "pc": "GR caer bien/mal · LX-02"},
  {"n": 19, "q": "¿Quién se enfadó con su amiga por algo que le dejó?", "ok": 0, "cats": ["caracter"], "es": "ES-03", "why": "Marta le prestó un vestido a Sonia y se lo devolvió roto: estuvieron dos semanas sin hablar.", "pc": "LX-04 · GR indefinido (U02)"}],
}
for it in CL3["items"]:
    it["o"] = [t["name"] for t in CL3["texts"]]

# ---------------- AUDITIVA ----------------
# Cada conversación: pres (presentación del narrador), lines [(rol, voz, texto)], q, o, ok, why, cats, es, img
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación. Las tres aparecen en el diálogo: escucha hasta el final.",
 "example": {"q": "¿Quién es el novio de Laura?", "o": ["el chico con barba", "el chico alto con gafas", "el chico rubio"], "ok": 1,
   "pres": "Va a escuchar a dos amigas que hablan en una fiesta.",
   "lines": [("Mujer", "AITANA", "Oye, ¿cuál es el novio de Laura? ¿Ese chico de la barba?"),
             ("Mujer 2", "GABI", "No, ese es su hermano. Su novio es el que lleva gafas, el que está hablando con aquel chico rubio."),
             ("Mujer", "AITANA", "¿El alto?"),
             ("Mujer 2", "GABI", "Sí, ese. Se llama Óscar y es muy simpático. Ven, te lo presento."), ("Mujer", "AITANA", "¡Ah, vale! Pues es muy guapo.")],
   "solucion": "La opción correcta es la letra be. El novio de Laura es el chico alto con gafas.",
   "img": "U03_CA1_0.jpg",
   "prompt": "Panel 1: a young man with a dark beard, casual shirt. Panel 2: a tall young man with glasses. Panel 3: a young man with blond hair."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Cómo es el hijo de la mujer?", "o": ["rubio y con gafas", "rubio y con el pelo largo", "rubio y con una gorra"], "ok": 2, "cats": ["descripcion"], "es": "ES-05",
   "pres": "Va a escuchar a una mujer que habla con un guarda de seguridad en un centro comercial.",
   "lines": [("Mujer", "LYDIA", "Perdone, ¡he perdido a mi hijo!"), ("Hombre", "SANTIAGO_ES", "Tranquila, señora. ¿Cómo es?"), ("Mujer", "LYDIA", "Tiene seis años, es rubio y tiene el pelo corto."), ("Hombre", "SANTIAGO_ES", "¿Lleva gafas?"), ("Mujer", "LYDIA", "No, gafas no. Lleva una gorra roja y una camiseta azul."), ("Hombre", "SANTIAGO_ES", "Un momento... ¿Es ese niño que está en la tienda de juguetes?"), ("Mujer", "LYDIA", "¡Sí, es él! ¡Muchas gracias!")],
   "why": "El niño es rubio, tiene el pelo corto y lleva una gorra roja. El guarda pregunta por las gafas, pero la madre dice que no.",
   "img": "U03_CA1_1.jpg", "prompt": "Panel 1: a blond boy of about six wearing glasses. Panel 2: a blond boy of about six with long hair. Panel 3: a blond boy of about six with short hair wearing a red cap and a blue t-shirt.", "pc": "LX-01 · FN describir"},
  {"n": 2, "conv": "Conversación dos", "q": "¿Qué peinado quiere la mujer?", "o": ["el pelo corto", "el pelo largo y liso", "el pelo rizado"], "ok": 1, "cats": ["descripcion"], "es": "ES-05",
   "pres": "Va a escuchar a una mujer que habla con un peluquero.",
   "lines": [("Hombre", "OSCAR", "Hola, Rocío. ¿Qué te hacemos hoy? ¿Cortamos?"), ("Mujer", "LUCIA", "No, no, cortar no. Me gusta largo."), ("Hombre", "OSCAR", "Pues tú dirás."), ("Mujer", "LUCIA", "Es que estoy cansada de los rizos. Quiero el pelo liso."), ("Hombre", "OSCAR", "¿Liso y corto? Corto te queda genial."), ("Mujer", "LUCIA", "Que no, que no. Largo. Solo liso, por favor."), ("Hombre", "OSCAR", "Muy bien, como tú quieras. Siéntate aquí.")],
   "why": "Rocío no quiere cortarse el pelo: lo quiere largo y liso. Ahora lo tiene rizado; el corto es la idea del peluquero.",
   "img": "U03_CA1_2.jpg", "prompt": "Panel 1: a woman with short straight hair. Panel 2: a woman with long straight hair. Panel 3: a woman with long curly hair. Same young woman, head and shoulders.", "pc": "LX-01"},
  {"n": 3, "conv": "Conversación tres", "q": "Según el padre, ¿a quién se parece el bebé?", "o": ["a su abuela", "a su padre", "a su madre"], "ok": 0, "cats": ["parecerse", "familia"], "es": "ES-08",
   "pres": "Va a escuchar a dos amigos que hablan de un bebé.",
   "lines": [("Mujer", "SARA_2", "¡Qué bebé tan guapo! Se parece mucho a ti, ¿no?"), ("Hombre", "MARTIN_1", "Todo el mundo dice eso, pero yo creo que se parece a mi madre: tiene los mismos ojos azules."), ("Mujer", "SARA_2", "Pues la nariz es de tu mujer."), ("Hombre", "MARTIN_1", "Sí, pero mira esta foto de mi madre de pequeña. ¡Son iguales!"), ("Mujer", "SARA_2", "¡Es verdad! Tienen la misma cara.")],
   "why": "El padre cree que el bebé se parece a su madre, es decir, a la abuela del bebé. La amiga dice que se parece al padre y que la nariz es de la madre.", "img": "U03_CA1_3.jpg",
   "prompt": "Panel 1: a smiling grandmother with white hair and blue eyes. Panel 2: a young father holding a baby. Panel 3: a young mother holding a baby.", "pc": "GR parecerse · LX-04"},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Qué gafas compra el hombre?", "o": ["unas gafas redondas", "unas gafas grandes negras", "unas gafas de sol"], "ok": 1, "cats": ["descripcion"], "es": "ES-05",
   "pres": "Va a escuchar a un hombre que habla con una dependienta en una óptica.",
   "lines": [("Mujer", "CRISTINA_LAT", "¿Qué le parecen estas redondas? Están muy de moda."), ("Hombre", "ENRIQUE", "Mmm, no sé... Con estas parezco mucho mayor. ¿Tiene unas más grandes?"), ("Mujer", "CRISTINA_LAT", "Estas negras grandes son muy modernas. Pruébeselas."), ("Hombre", "ENRIQUE", "Sí, estas me gustan. También necesito unas de sol, pero eso otro día. Me llevo las negras."), ("Mujer", "CRISTINA_LAT", "Muy bien. Son ciento veinte euros.")],
   "why": "Se lleva las negras grandes. Las redondas no le gustan y las de sol las va a comprar otro día.", "img": "U03_CA1_4.jpg",
   "prompt": "Panel 1: a pair of small round eyeglasses. Panel 2: a pair of large black eyeglasses. Panel 3: a pair of sunglasses.", "pc": "GR parecer (parezco) · LX compras"},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Con quién se lleva mal el hombre?", "o": ["con su jefa", "con su vecino", "con su cuñado"], "ok": 2, "cats": ["caracter", "familia"], "es": "ES-08",
   "pres": "Va a escuchar a dos amigos que hablan en un bar.",
   "lines": [("Mujer", "SUSANA", "¿Qué tal en el trabajo nuevo?"), ("Hombre", "MARIO", "Muy bien. Mi jefa es muy simpática y los compañeros me caen genial."), ("Mujer", "SUSANA", "¿Y tu vecino, el de la música alta?"), ("Hombre", "MARIO", "Ahora nos llevamos bien. Hablamos y ya no pone la música por la noche. El problema es mi cuñado: siempre me critica. No nos llevamos nada bien.")],
   "why": "Con su cuñado no se lleva nada bien. La jefa le cae muy bien y con el vecino ahora se lleva bien.", "img": "U03_CA1_5.jpg",
   "prompt": "Panel 1: a smiling woman at an office desk. Panel 2: a man at an apartment door holding a loudspeaker. Panel 3: a man with crossed arms at a family dinner table.", "pc": "GR llevarse bien/mal, caer bien · LX-04"},
  {"n": 6, "conv": "Conversación seis", "q": "¿Qué ropa se va a poner el hombre para la boda?", "o": ["un traje azul sin corbata", "un traje gris con corbata", "un traje azul con corbata"], "ok": 0, "cats": ["descripcion"], "es": "ES-05",
   "pres": "Va a escuchar a una pareja que habla en su casa.",
   "lines": [("Hombre", "GABRIEL_ES", "¿Qué me pongo para la boda de tu prima? ¿El traje gris?"), ("Mujer", "EVA", "No, el gris es muy serio. Ponte el azul, con la camisa blanca."), ("Hombre", "GABRIEL_ES", "Vale. ¿Y la corbata roja?"), ("Mujer", "EVA", "Sin corbata. Es una boda en la playa, ¿no te acuerdas?"), ("Hombre", "GABRIEL_ES", "¡Ah, es verdad! Entonces nada de corbata. ¿Y los zapatos negros?"), ("Mujer", "EVA", "Sí, los negros.")],
   "why": "Se pone el traje azul con camisa blanca y sin corbata, porque la boda es en la playa. El gris es demasiado serio.", "img": "U03_CA1_6.jpg",
   "prompt": "Panel 1: a blue suit with a white shirt and no tie on a hanger. Panel 2: a grey suit with a tie on a hanger. Panel 3: a blue suit with a red tie on a hanger.", "pc": "LX ropa · GR llevar"},
 ]}
CA3 = {"n": 3, "type": "friends",
 "instr": "Usted va a escuchar una conversación entre dos amigos, Alba y Nacho. Indique si los enunciados (del 13 al 18) se refieren a Alba (A), a Nacho (B) o a ninguno de los dos (C). Escuchará la conversación dos veces.",
 "tip": "Tienes 30 segundos para leer las frases. Si algo lo hace otra persona (un amigo, una hermana...) o el día no coincide, la respuesta es C.",
 "who": ["Alba", "Nacho"], "voices": {"ALBA": "FIONA", "NACHO": "DAVID_M2"},
 "lines": [
  ("NACHO", "¡Alba! ¿Qué tal la cita del sábado? ¿Por fin conociste al chico de la aplicación?"),
  ("ALBA", "¡Sí! Se llama Jorge y es profesor de música. Quedamos en un café del centro y hablamos tres horas."),
  ("NACHO", "¿Y cómo es? ¿Es guapo?"),
  ("ALBA", "Para mí, sí. Es alto, moreno, lleva barba y tiene unos ojos muy bonitos. Y es muy divertido. Lo único: es un poco despistado. Llegó media hora tarde."),
  ("NACHO", "¡Uf! Yo no soporto a la gente impuntual. ¿Y vais a volver a quedar?"),
  ("ALBA", "Sí, el viernes vamos al cine. ¿Y tú? ¿Qué tal con tu compañero de piso nuevo?"),
  ("NACHO", "Pues mejor de lo que pensaba. Es muy tranquilo y muy ordenado, y cocina muy bien. Ayer hizo una paella buenísima. Y además es muy simpático: el sábado vienen unos amigos suyos a cenar y me ha invitado."),
  ("ALBA", "¡Qué suerte! Yo vivo con mi hermana y es un desastre: nunca friega los platos. El domingo pasado, por ejemplo, dejó la cocina fatal."),
  ("NACHO", "Oye, el domingo es el cumpleaños de mi madre y voy a Valencia. ¿Te acuerdas de mi madre?"),
  ("ALBA", "¡Claro! Me cae genial. Te pareces muchísimo a ella."),
  ("NACHO", "Eso dice todo el mundo, pero yo creo que me parezco más a mi padre."),
  ("ALBA", "Bueno, pues dale un beso de mi parte y felicítala. Y el lunes te cuento qué tal con Jorge."),
  ("NACHO", "¡Vale! Y me enseñas una foto, ¿eh?")],
 "items": [
  {"n": 13, "q": "Conoció a alguien el fin de semana pasado.", "ok": 0, "cats": ["familia"], "es": "ES-08", "why": "Alba conoció el sábado al chico de la aplicación, Jorge.", "pc": "LX pareja · GR indefinido"},
  {"n": 14, "q": "Vive con una persona que cocina muy bien.", "ok": 1, "cats": ["caracter"], "es": "ES-08", "why": "El compañero de piso de Nacho cocina muy bien: ayer hizo una paella buenísima.", "pc": "LX-02"},
  {"n": 15, "q": "Llegó tarde a una cita.", "ok": 2, "cats": ["caracter"], "es": "ES-08", "why": "Quien llegó tarde fue Jorge, el chico de la cita de Alba: ni Alba ni Nacho.", "pc": "LX-02 (despistado, impuntual)"},
  {"n": 16, "q": "Va a visitar a su familia.", "ok": 1, "cats": ["familia"], "es": "ES-03", "why": "Nacho va a Valencia el domingo por el cumpleaños de su madre.", "pc": "LX-04 · GR ir a"},
  {"n": 17, "q": "Comparte piso con una persona desordenada.", "ok": 0, "cats": ["caracter", "familia"], "es": "ES-03", "why": "Alba vive con su hermana, que es un desastre y nunca friega los platos. El compañero de Nacho es muy ordenado.", "pc": "LX-02"},
  {"n": 18, "q": "Va a ir al cine el sábado.", "ok": 2, "cats": ["familia"], "es": "ES-07", "why": "Alba y Jorge van al cine el viernes, no el sábado. Nadie habla de ir al cine el sábado.", "pc": "FN planes"}],
}
for it in CA3["items"]:
    it["o"] = CA3["who"] + ["Ninguno de los dos"]

# ---------------- ESCRITURA ----------------
ESCRITA = {"t1": {"instr": "Una amiga le escribe porque usted tiene una pareja nueva.",
  "input": ["¡Hola! ¡Qué alegría! Me ha dicho Pablo que tienes pareja nueva. ¡Qué callado lo tenías! ¿Cómo se llama? ¿Qué hace? ¿Cómo es? ¿Dónde os conocisteis? Tengo muchas ganas de conocer a tu pareja. Cuéntamelo todo, ¿eh?", "Un beso,<br>Andrea"],
  "lead": "Conteste a su amiga. En el correo tiene que:",
  "pautas": ["saludar;", "decir cómo se llama su pareja y cómo y cuándo se conocieron;", "describirla físicamente;", "hablar de su carácter;", "proponer quedar los tres y despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Escriba un texto sobre su familia y sobre usted. Hable de:",
   "pautas": ["cuántos son en su familia y quiénes son;", "a quién se parece usted físicamente;", "a quién se parece de carácter;", "con quién se lleva mejor y por qué;", "con quién tiene menos relación."]},
  "op2": {"title": "Opción 2", "intro": "El mes pasado usted fue a la boda de su amigo Samuel. Aquí tiene tres fotos de ese día.",
   "photos": ["Los novios, muy sonrientes, en la puerta del ayuntamiento: él lleva un traje gris y ella, un vestido blanco corto.", "Una mesa larga en un jardín con muchos invitados comiendo; una señora mayor con sombrero se ríe.", "Por la noche, los invitados bailan; un chico alto con barba baila con una niña pequeña."],
   "ficha": [], "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": ["quiénes son las personas de las fotos y cómo son;", "qué pasó durante el día;", "con quién estuvo usted y cómo lo pasó."],
   "img": "U03_escrita.jpg", "imgAlt": "Tres fotos de una boda: los novios, la comida y el baile"},
  "min": 70, "max": 80}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: mi mejor amigo o amiga", "pautas": ["quién es y desde cuándo lo/la conoce;", "cómo es físicamente;", "cómo es su carácter;", "qué hacen juntos/as;", "por qué se llevan bien."]},
  {"title": "Opción 2: mi pareja ideal", "pautas": ["cómo es físicamente (o si eso no es importante para usted);", "cómo es su carácter;", "qué cosas le tienen que gustar;", "qué cosas no soporta usted en una pareja;", "si conoce a alguien así."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1", "desc": "Una tienda de ropa. Un hombre joven se prueba una chaqueta delante de un espejo; una dependienta le enseña otra chaqueta de otro color. Al fondo, estanterías con camisetas y un probador.", "img": "U03_oral_foto1.jpg"},
  {"title": "Fotografía 2", "desc": "La zona de llegadas de un aeropuerto. Una mujer de unos cincuenta años, con el pelo corto y gris, espera con un cartel en blanco y el móvil en la mano. Alrededor, viajeros con maletas y familias que se abrazan.", "img": "U03_oral_foto2.jpg"}],
  "pautas": ["las personas: cómo son, qué ropa llevan, qué hacen;", "el lugar: dónde están, qué cosas hay;", "qué cree que piensan o necesitan las personas;", "qué cree que va a pasar después."]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1", "intro": "Usted necesita ropa para una fiesta y está en una tienda. Hable con el dependiente (su profesora). Tiene que:", "pautas": ["explicar qué busca y para qué ocasión;", "decir su talla y el color que prefiere;", "preguntar si se lo puede probar y decir qué tal le queda;", "preguntar el precio y si se puede cambiar."]},
  {"title": "Si eligió la fotografía 2", "intro": "Usted va a buscar al aeropuerto a una persona de su trabajo que no conoce. Hable con ella por teléfono (su profesora). Tiene que:", "pautas": ["saludar y presentarse;", "describirse físicamente y decir qué ropa lleva;", "explicar dónde está exactamente;", "preguntar cómo es la otra persona y despedirse."]}]}}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (mi mejor amigo/a): ¿Se parecen en algo? · ¿Desde cuándo se conocen?
    Opción 2 (mi pareja ideal): ¿Qué es lo más importante para usted? · ¿Cree que existe la pareja ideal?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (tienda de ropa): ¿Qué tal cree que le queda la chaqueta? · ¿Cuál va a comprar?
    Foto 2 (aeropuerto): ¿A quién cree que espera la mujer? · ¿Cómo va a reconocer a esa persona?
  Tarea 3 — su papel (aquí sí conversa: pregunte, reaccione y provoque un pequeño problema):
    Foto 1 (dependiente/a): tallas S, M, L; hay la chaqueta en azul y en negro; 75 euros; se puede
    cambiar con el tique durante 30 días. Pregunte «¿Qué tal le queda?».
    Foto 2 (persona que llega): usted lleva un abrigo rojo y una maleta verde, es alto/a y tiene el pelo
    rizado; está en la puerta B, al lado de una cafetería.
  Qué mirar en esta unidad: ser/tener/llevar bien usados; parecerse con pronombre (me parezco);
  caer bien con pronombre (me cae); presentes en -zc- (conozco)."""
ERRORES = """  *Es pelo largo / *tiene gafas por «lleva gafas» (aceptable, pero trabajar llevar);
  *Yo parezco a mi madre (sin me); *Yo caigo bien mi jefe (por «Mi jefe me cae bien»);
  *conoco, *conduco; *la que lleva gafas es mi prima → bien, pero *el que lleva
  gafas (para mujer); concordancia de adjetivos (*mi hermana es alto)."""
IMG_PROMPTS = {
 "portada": "Photorealistic, candid photo: three generations of a Spanish family (grandmother, mother and teenage daughter) laughing together on a sofa and comparing their faces in an old family photo; you can see they look alike; warm natural light, cozy living room, no readable text, 16:9",
 "oral": "Photorealistic, candid photo of an adult Spanish class in a bright classroom: two adult students describe a photo of a person to each other at a table while the teacher listens; natural light, friendly atmosphere, no readable text, 3:2",
 "escrita": "Photorealistic triptych, three separate photos side by side of equal size with thin white borders, same wedding day. Left: a smiling bride in a short white dress and a groom in a grey suit at the door of a Spanish town hall. Centre: a long table in a garden with many guests eating; an older lady with a hat laughing. Right: at night, guests dancing under string lights; a tall young man with a beard dances with a little girl. Natural light, candid, no readable text, 3:1",
 "oral_foto1": "Photorealistic, candid photo of a clothing store in Spain: a young man tries on a jacket in front of a mirror while a female shop assistant shows him another jacket in a different colour; shelves with t-shirts and a fitting room in the background; bright indoor light, no readable text, 3:2",
 "oral_foto2": "Photorealistic, candid photo of the arrivals hall of an airport: a woman of about fifty with short grey hair waits holding a blank sign and a mobile phone; around her, travellers with suitcases and families hugging; natural light, no readable text, 3:2",
}
IMG_DESC = {"portada": "abuela, madre e hija en un sofá mirando una foto antigua", "oral": "clase: dos alumnos describiendo una foto", "escrita": "tres fotos de una boda: novios, comida, baile", "oral_foto1": "tienda de ropa: chico probándose una chaqueta", "oral_foto2": "aeropuerto: mujer de pelo gris con un cartel"}
CA1_DESC = {0: "novio de Laura: barba / alto con gafas / rubio", 1: "niño rubio: gafas / pelo largo / gorra roja", 2: "peinados: corto / largo liso / rizado", 3: "abuela / padre con bebé / madre con bebé", 4: "gafas: redondas / grandes negras / de sol", 5: "jefa / vecino con música / cuñado en la cena", 6: "trajes: azul sin corbata / gris / azul con corbata roja"}

LECTURA = [CL1, CL3]
AUDITIVA = [CA1, CA3]
