# -*- coding: utf-8 -*-
# FUENTE DE LA UNIDAD 4 (fase 1) · Hogar, dulce hogar
# Rotación U04: lectura T2 (anuncios) + T4 (texto largo) · auditiva T2 (radio) + T4 (mensajes)
U = "04"
TITLE = "Hogar, dulce hogar"
BASE = "https://2spanishteachers.com/wp-content/uploads/2026/10/"   # imágenes y audios subidos en octubre
RECORDATORIO = [
 "Describir una vivienda: es (luminoso, tranquilo, acogedor), está (en el centro, en las afueras, amueblado, bien situado), tiene (ascensor, terraza, tres habitaciones) y da a (la calle, un parque, un patio).",
 "Tipos de vivienda (piso, estudio, ático, chalé, casa adosada), partes de la casa, muebles, electrodomésticos y materiales (de madera, de piel, de cristal, de metal).",
 "Comparar: más / menos... que, tan... como, tanto/a/os/as... como, verbo + tanto como; mejor, peor, mayor, menor.",
 "Ubicar objetos: encima de, debajo de, delante de, detrás de, al lado de, entre, a la derecha / a la izquierda de, en el centro de, alrededor de.",
 "Posesivos tónicos (el mío, la tuya, los suyos...) y gustos y preferencias con gustar, encantar y preferir.",
]
TIPS_INICIO = [
 "<b>Lectura, tarea 2:</b> lee la pregunta antes del anuncio y busca solo esa información. Cuidado con palabras como <i>todo</i>, <i>solo</i>, <i>siempre</i> o <i>gratis</i>: muchas trampas cambian una condición del anuncio.",
 "<b>Auditiva, tarea 4:</b> en cada mensaje pregúntate primero quién habla y dónde está (¿un contestador?, ¿una tienda?, ¿una feria?). Eso descarta muchos enunciados. Sobran tres.",
]
CATS = {
 "vivienda": {"name": "Tipos y partes de la vivienda; alquilar y compartir piso",
  "repaso": "Tipos (piso, estudio, ático, chalé, casa adosada), partes (salón, dormitorio, cocina, baño, terraza, balcón, garaje) y palabras del alquiler: alquilar, compartir piso, mudarse, el dueño, la inmobiliaria, el ascensor, la planta. En el libro: unidad 4, tipos y partes de una vivienda.",
  "reto": "Describe en cinco frases la vivienda donde vives: tipo, planta, partes y con quién vives."},
 "describir": {"name": "Describir una vivienda (ser, estar, tener, dar a)",
  "repaso": "Es + adjetivo (es luminoso, es tranquilo); está + lugar o estado (está en el centro, está amueblado, está bien situado); tiene + partes o servicios (tiene ascensor, tiene terraza); da a + lo que se ve (da a un parque, da a la calle). En el libro: unidad 4, usos de ser y estar.",
  "reto": "Escribe un anuncio de tu piso con una frase con es, una con está, una con tiene y una con da a."},
 "muebles": {"name": "Muebles, objetos, electrodomésticos y materiales",
  "repaso": "Muebles (sofá, sillón, armario, estantería, mesilla de noche), electrodomésticos (lavadora, nevera, horno, microondas) y materiales con de: una mesa de madera, un sofá de piel, una lámpara de metal. En el libro: unidad 4, léxico de muebles y materiales.",
  "reto": "Elige tres muebles de tu salón y di de qué material y de qué color son."},
 "ubicar": {"name": "Ubicar objetos en el espacio (encima de, al lado de...)",
  "repaso": "Encima de, debajo de, delante de, detrás de, al lado de, enfrente de, entre... y..., a la derecha / izquierda de, en el centro de, alrededor de. Recuerda: de + el = del (al lado del sofá). En el libro: unidad 4, preposiciones y adverbios para ubicar.",
  "reto": "Mira tu habitación y escribe cinco frases: dónde está cada mueble."},
 "comparar": {"name": "Comparativos (más... que, tan... como, tanto como)",
  "repaso": "Más / menos + adjetivo o nombre + que; tan + adjetivo + como; tanto/a/os/as + nombre + como; verbo + tanto como. Formas especiales: mejor, peor, mayor, menor (nunca *más mejor). En el libro: unidad 4, comparativos.",
  "reto": "Compara tu casa con la de un amigo en cuatro frases: una con más, una con menos, una con tan y una con tanto."},
 "posesivos": {"name": "Posesivos tónicos (el mío, la tuya, los suyos...)",
  "repaso": "Para no repetir el nombre: mi piso > el mío; tu terraza > la tuya; sus habitaciones > las suyas. Concuerdan con la cosa, no con la persona: la casa de Juan > la suya. En el libro: unidad 4, pronombres posesivos.",
  "reto": "Escribe tres frases comparando tus cosas con las de otra persona: Mi habitación es grande, pero la tuya tiene más luz."},
 "gustos": {"name": "Gustos y preferencias (gustar, encantar, preferir)",
  "repaso": "Me gusta + singular o infinitivo / me gustan + plural; me encanta(n); prefiero + nombre o infinitivo (prefiero vivir en el centro). Con gustar va el pronombre: a mí me gusta, a ella le encanta. En el libro: unidad 4, expresar gustos y preferencias.",
  "reto": "Escribe dos cosas que te encantan de tu casa, una que no te gusta y dónde prefieres vivir."},
}
ESTRATEGIAS_NUEVAS = {}

# ---------------- LECTURA ----------------
CL2 = {"n": 2, "type": "ads",
 "instr": "Usted va a leer ocho anuncios. A continuación, responda a las preguntas (de la 6 a la 13). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos: un minuto y medio por anuncio. Lee la pregunta primero y busca solo ese dato. Las palabras <i>todo</i>, <i>solo</i>, <i>siempre</i> y <i>gratis</i> suelen esconder la trampa.",
 "example": {"title": "SE ALQUILA ESTUDIO EN EL CENTRO",
   "body": "Estudio de 35 m² en la calle Real, a cinco minutos de la estación. Es exterior y muy luminoso. Tiene cocina americana, baño con ducha y un pequeño balcón. Está amueblado y tiene calefacción. No hay ascensor: está en un tercer piso. Precio: 550 € al mes. No se admiten animales. Llamar por las tardes al 612 438 907.",
   "q": "El estudio...", "o": ["está en un edificio con ascensor.", "tiene muebles.", "acepta mascotas."], "ok": 1,
   "why": "La opción correcta es la B porque el estudio está amueblado."},
 "items": [
  {"n": 6, "title": "COMUNIDAD DE VECINOS · CALLE OLIVO, 14",
   "body": "Estimados vecinos: del 3 al 7 de marzo, unos técnicos van a cambiar el ascensor y durante esos días no se puede usar. Las personas mayores o con problemas para subir la escalera pueden pedir ayuda al portero, de 8:00 a 15:00. La reunión de la comunidad de marzo pasa al día 14, a las 19:00, en el portal. Gracias por su paciencia.<br>El presidente",
   "q": "Según el aviso, durante la primera semana de marzo...", "o": ["hay una reunión de vecinos en el portal.", "los vecinos tienen que subir a pie.", "el portero va a cambiar el ascensor."], "ok": 1,
   "cats": ["vivienda"], "es": "ES-03", "pc": "LX-10 vivienda (ascensor, portal, comunidad) · GR-08 estar/no se puede",
   "why": "Del 3 al 7 de marzo no se puede usar el ascensor: hay que subir por la escalera. La reunión es el día 14 y quienes cambian el ascensor son unos técnicos; el portero solo ayuda."},
  {"n": 7, "title": "MUEBLES ROBLE · ¡LIQUIDACIÓN POR CAMBIO DE LOCAL!",
   "body": "Nos vamos a un local más grande, en el polígono Las Eras. Por eso, hasta el 30 de abril, todos los muebles de la tienda tienen un 40 % de descuento: sofás de piel y de tela, mesas de madera, sillas, estanterías... Las lámparas y las alfombras, un 20 %. El transporte a domicilio es gratis para compras de más de 300 €. Avenida del Puerto, 22.",
   "q": "En esta tienda...", "o": ["todo cuesta un 40 % menos.", "el transporte siempre es gratis.", "las mesas son más baratas que antes."], "ok": 2,
   "cats": ["muebles", "comparar"], "es": "ES-04", "pc": "LX-10 muebles y materiales · GR-05 comparación",
   "why": "Las mesas tienen un 40 % de descuento: ahora son más baratas que antes. No es «todo»: las lámparas y las alfombras solo tienen un 20 %. El transporte es gratis solo si gastas más de 300 €."},
  {"n": 8, "title": "FORO · COMPARTIR PISO",
   "body": "Mensaje de lauri_92:<br>Comparto piso con dos chicas desde septiembre. El piso está muy bien y nos llevamos genial, pero tengo un problema: mi habitación es la más pequeña y pago lo mismo que ellas. La suya tiene balcón y la mía da a un patio interior muy oscuro. ¿Os parece justo? ¿Qué puedo hacer?",
   "q": "Laura...", "o": ["piensa que paga demasiado por su habitación.", "no se lleva bien con sus compañeras.", "tiene una habitación con balcón."], "ok": 0,
   "cats": ["posesivos", "comparar", "describir"], "es": "ES-03", "pc": "GR-03 posesivos tónicos · GR-05 · LX-10 (dar a, patio interior)",
   "why": "Su habitación es la más pequeña y oscura, pero paga lo mismo: cree que no es justo. Se lleva genial con sus compañeras, y el balcón es de la habitación de ellas (la suya), no de la de Laura (la mía)."},
  {"n": 9, "title": "MUDANZAS RÁPIDAS HERMANOS GIL",
   "body": "¿Te cambias de casa? Nosotros lo hacemos todo: llevamos tus muebles, montamos y desmontamos armarios y camas, y te damos cajas de cartón gratis. Trabajamos de lunes a sábado; los domingos, solo mudanzas pequeñas dentro de la ciudad. Pide tu presupuesto sin compromiso en nuestra web. ¡Clientes nuevos: 10 % de descuento!",
   "q": "Esta empresa...", "o": ["no trabaja los domingos.", "regala cajas para la mudanza.", "solo hace mudanzas dentro de la ciudad."], "ok": 1,
   "cats": ["vivienda", "muebles"], "es": "ES-06", "pc": "LX-10 (mudarse, muebles) · materiales (de cartón)",
   "why": "Dan cajas de cartón gratis: las regalan. Los domingos sí trabajan (solo mudanzas pequeñas), y la condición «dentro de la ciudad» es solo para los domingos."},
  {"n": 10, "title": "VENDO SOFÁ CAMA",
   "body": "Vendo sofá cama de tela gris, de tres plazas, en muy buen estado. Tiene dos años. Es muy cómodo y se abre fácilmente: perfecto para invitados. Lo vendo porque me voy a vivir a un piso más pequeño y no tengo sitio. Precio: 150 € (nuevo costó 450 €). Hay que recogerlo en mi casa: es un cuarto piso con ascensor. Óscar, 655 210 384.",
   "q": "Óscar vende el sofá porque...", "o": ["su nueva casa es más pequeña.", "está viejo.", "no es cómodo."], "ok": 0,
   "cats": ["comparar", "muebles"], "es": "ES-03", "pc": "GR-05 comparación · LX-10 muebles · GR-08 estar (en buen estado)",
   "why": "Se va a un piso más pequeño y no tiene sitio para el sofá. El sofá está en muy buen estado y es muy cómodo."},
  {"n": 11, "title": "NOTICIAS · LOS JÓVENES SE VAN DE CASA MÁS TARDE",
   "body": "Según un estudio publicado esta semana, los jóvenes españoles se van de casa de sus padres a los treinta años, más tarde que en el resto de Europa, donde la media es de veintiséis. La razón principal es el precio del alquiler. Por eso, cada vez más jóvenes comparten piso con amigos o con otras personas, también después de los treinta.",
   "q": "Según la noticia, los jóvenes españoles...", "o": ["se van de casa a los veintiséis años.", "prefieren vivir solos.", "viven con sus padres más años que otros jóvenes europeos."], "ok": 2,
   "cats": ["comparar", "vivienda"], "es": "ES-04", "pc": "GR-05 comparación (más tarde que) · LX-10 (alquiler, compartir piso)",
   "why": "Se van a los treinta, más tarde que en el resto de Europa: viven más años con sus padres. Veintiséis es la media europea, y la noticia dice que muchos comparten piso, no que prefieren vivir solos."},
  {"n": 12, "title": "TALLER: DALE UNA NUEVA VIDA A TUS MUEBLES",
   "body": "¿Tienes una silla vieja o una mesilla de noche que ya no te gusta? Aprende a pintar y a renovar muebles de madera en nuestro taller. Cuatro sábados de octubre, de 10:00 a 13:00, en el Centro Cultural Las Palmeras. Precio: 40 €, con todos los materiales incluidos. Solo tienes que traer un mueble pequeño. Plazas limitadas: inscripciones en la recepción del centro.",
   "q": "Para hacer el taller, hay que...", "o": ["comprar las pinturas.", "llevar un mueble.", "ir todos los días de octubre."], "ok": 1,
   "cats": ["muebles"], "es": "ES-03", "pc": "LX-10 muebles · materiales (de madera) · hay que + infinitivo",
   "why": "«Solo tienes que traer un mueble pequeño» = hay que llevar un mueble. Los materiales están incluidos en el precio y el taller es solo cuatro sábados."},
  {"n": 13, "title": "INTERCAMBIO DE CASA EN AGOSTO",
   "body": "Somos una familia de Sevilla (dos adultos y dos niños) y buscamos una casa en el norte de España para intercambiar en agosto. La nuestra es un chalé con jardín y piscina, a veinte minutos del centro. Tiene cuatro dormitorios y dos baños. Preferimos una casa cerca de la playa o de la montaña, no en una ciudad grande. Escríbenos: familiarosales@correo.es",
   "q": "La familia Rosales busca...", "o": ["una casa con piscina.", "una casa en una gran ciudad.", "una casa en la costa o en la montaña."], "ok": 2,
   "cats": ["gustos", "posesivos", "vivienda"], "es": "ES-08", "pc": "GR-07 preferir · GR-03 posesivos tónicos (la nuestra) · LX-10",
   "why": "Prefieren una casa cerca de la playa o de la montaña. La piscina es de su chalé (la nuestra), y no quieren una ciudad grande."},
 ]}

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un texto de un blog sobre una pareja que se cambió de casa. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto: busca cada respuesta un poco más abajo que la anterior. Atención a <i>el mío</i>, <i>el suyo</i>: ¿de quién habla?",
 "title": "De un piso pequeño en Bilbao a una casa de pueblo",
 "sub": "Blog «Cambio de casa, cambio de vida»",
 "body": [
  "Me llamo Nerea y soy diseñadora gráfica. Mi pareja, Íñigo, y yo vivimos ocho años en un piso pequeño en el centro de Bilbao, en un cuarto piso sin ascensor. Fue una época muy bonita: salimos mucho, tuvimos los cines y los bares al lado de casa y fuimos a trabajar andando todos los días.",
  "Pero hace tres años todo cambió. Primero, la empresa de Íñigo le ofreció trabajar desde casa. Después, el dueño de nuestro piso nos subió el alquiler: de setecientos a novecientos euros al mes. Una noche, Íñigo me enseñó en el móvil el anuncio de una casa en un pueblo de Burgos: «Casa de piedra de 1920, 150 metros cuadrados, con huerto. Necesita reforma». Y el precio: ¡solo cuatrocientos euros al mes!",
  "La casa nos encantó desde el primer momento, aunque necesitó mucho trabajo. Durante cuatro meses pintamos todas las paredes, cambiamos las ventanas y compramos una cocina nueva. Muchos muebles los encontramos en la propia casa: una mesa enorme de madera, un armario antiguo y dos sillones de piel. Solo tuvimos que limpiarlos y pintarlos. Los vecinos nos ayudaron mucho: Julián, el vecino de al lado, nos dejó sus herramientas, y su mujer nos regaló plantas para el huerto.",
  "Ahora la casa es muy diferente. Abajo están la cocina, el salón y un baño; arriba, tres dormitorios y otro baño. Mi lugar favorito es mi despacho: está al lado de nuestra habitación y tiene una ventana que da al huerto. Allí trabajo cada mañana, con mucha más luz que en Bilbao. Íñigo tiene el suyo en la planta baja, enfrente de la cocina, porque prefiere estar cerca de la cafetera.",
  "¿Es mejor la vida aquí? Para nosotros, sí. La casa es más grande que nuestro piso de Bilbao y cuesta menos, y el pueblo es mucho más tranquilo que la ciudad. Pero no todo es perfecto: no hay tantas tiendas como en Bilbao, el supermercado más cercano está a quince kilómetros y en invierno hace muchísimo frío. Además, internet funciona peor que en la ciudad, y para Íñigo eso es un problema. Y, claro, echamos de menos a nuestros amigos.",
  "Por eso, cada verano los invitamos a pasar unos días con nosotros. Este año vienen ocho. ¡Menos mal que tenemos tres dormitorios y un sofá cama en el salón!"],
 "items": [
  {"n": 20, "q": "En Bilbao, Nerea e Íñigo vivieron en un piso...", "o": ["cerca de lugares de ocio.", "con ascensor.", "de 150 metros cuadrados."], "ok": 0,
   "cats": ["vivienda", "ubicar"], "es": "ES-06", "pc": "LX-10 · al lado de · LX-08 ocio",
   "why": "Tenían los cines y los bares al lado de casa. El piso no tenía ascensor, y los 150 metros son de la casa del pueblo."},
  {"n": 21, "q": "Nerea e Íñigo dejaron su piso porque...", "o": ["Íñigo encontró un trabajo en Burgos.", "querían vivir más cerca de sus amigos.", "tuvieron que pagar más de alquiler."], "ok": 2,
   "cats": ["vivienda"], "es": "ES-03", "pc": "LX-10 alquiler · GR indefinido (U02)",
   "why": "El dueño les subió el alquiler de setecientos a novecientos euros. Íñigo no cambió de trabajo: empezó a trabajar desde casa. Burgos es donde está la casa nueva, y ahora echan de menos a sus amigos."},
  {"n": 22, "q": "Durante la reforma, Nerea e Íñigo...", "o": ["compraron una mesa enorme de madera.", "no tuvieron que comprar todos los muebles.", "trabajaron en la casa más de un año."], "ok": 1,
   "cats": ["muebles"], "es": "ES-04", "pc": "LX-10 muebles y materiales (de madera, de piel)",
   "why": "Muchos muebles ya estaban en la casa (la mesa, el armario, los sillones): solo los limpiaron y pintaron. La mesa no la compraron, y la reforma duró cuatro meses."},
  {"n": 23, "q": "El despacho de Nerea...", "o": ["está en la planta baja.", "tiene vistas al huerto.", "está enfrente de la cocina."], "ok": 1,
   "cats": ["ubicar", "posesivos", "describir"], "es": "ES-08", "pc": "GR-03 el suyo · preposiciones de lugar · dar a",
   "why": "Su despacho tiene una ventana que da al huerto. El que está en la planta baja, enfrente de la cocina, es el de Íñigo (el suyo)."},
  {"n": 24, "q": "Según Nerea, en el pueblo...", "o": ["hay menos tiendas que en la ciudad.", "el supermercado está muy cerca.", "la vida es más cara."], "ok": 0,
   "cats": ["comparar"], "es": "ES-03", "pc": "GR-05 (no hay tantas... como = hay menos... que)",
   "why": "«No hay tantas tiendas como en Bilbao» = hay menos tiendas. El supermercado está a quince kilómetros, y la casa cuesta menos que el piso."},
  {"n": 25, "q": "Este verano...", "o": ["Nerea e Íñigo van a visitar a sus amigos en Bilbao.", "van a comprar un sofá cama para el salón.", "un grupo de amigos va a dormir en su casa."], "ok": 2,
   "cats": ["vivienda"], "es": "ES-07", "pc": "LX-10 · GR ir a + infinitivo / presente con valor de futuro",
   "why": "Este año ocho amigos vienen a pasar unos días con ellos. El sofá cama ya lo tienen, y el texto no habla de un viaje a Bilbao."},
 ]}

# ---------------- AUDITIVA ----------------
RADIO_FX = "SONIDO 2: Short bright radio station jingle, three cheerful synth notes, clean, no voices, no background noise"
CA2 = {"n": 2, "type": "radio",
 "instr": "Usted va a escuchar seis anuncios o fragmentos de un programa de radio y tiene que responder a seis preguntas. Cada audición se repite dos veces. Lea las preguntas (de la 7 a la 12) y seleccione la opción correcta (A, B o C).",
 "tip": "Lee las seis preguntas antes de empezar. En la primera escucha marca una opción; en la segunda, compruébala. Fíjate en las condiciones: para quién es, cuándo, cuánto cuesta.",
 "example": {"q": "Según el anuncio, la inmobiliaria Puerta Azul...", "o": ["solo tiene pisos en el centro.", "este mes no cobra comisión.", "vende casas en la plaza Mayor."], "ok": 1,
   "why": "La opción correcta es la B porque este mes no se paga la comisión de la agencia.",
   "lab": "Locutor", "voice": "BOBBY/RADIO",
   "text": "¿Buscas piso? En la inmobiliaria Puerta Azul te ayudamos a encontrar tu casa ideal. Tenemos pisos, estudios y áticos en alquiler en todos los barrios de la ciudad. Y este mes, si alquilas con nosotros, no pagas la comisión de la agencia. Llámanos o ven a vernos a la plaza Mayor, número ocho.",
   "solucion": "La opción correcta es la letra be, porque este mes no se paga la comisión de la agencia."},
 "items": [
  {"n": 7, "conv": "Audio 1", "q": "Según la noticia, las ayudas son para...", "o": ["jóvenes que compran su primera casa.", "personas que llegan a la ciudad este año.", "jóvenes que quieren alquilar un piso."], "ok": 2,
   "cats": ["vivienda"], "es": "ES-04", "pc": "LX-10 alquilar · LX-17 ayudas",
   "lab": "Locutora", "voice": "CLARA/RADIO",
   "text": "Y ahora, una noticia de nuestra ciudad. Desde el lunes, el Ayuntamiento ofrece ayudas para jóvenes de dieciocho a treinta y cinco años que quieren alquilar su primera vivienda. Las ayudas son de doscientos euros al mes durante dos años. Para pedirlas, hay que vivir en la ciudad desde hace un año como mínimo.",
   "why": "Son para jóvenes que quieren alquilar su primera vivienda, no comprarla. Y hay que vivir en la ciudad desde hace un año como mínimo: no son para personas que llegan ahora."},
  {"n": 8, "conv": "Audio 2", "q": "En Muebles Nórdica, esta semana...", "o": ["dan una mesa con cada sofá.", "los sofás cuestan menos.", "cierran los domingos."], "ok": 0,
   "cats": ["muebles"], "es": "ES-03", "pc": "LX-10 muebles · LX-12 compras",
   "lab": "Locutora", "voice": "TAMARA/RADIO",
   "text": "¿Tu salón necesita un cambio? En Muebles Nórdica tenemos sofás, mesas y estanterías de estilo escandinavo, de madera natural y en colores claros. Y solo esta semana, si compras un sofá, te regalamos la mesa de centro. Abrimos todos los días, también los domingos, de diez de la mañana a nueve de la noche.",
   "why": "Si compras un sofá, te regalan la mesa de centro. No habla de precios más bajos para los sofás, y abren también los domingos."},
  {"n": 9, "conv": "Audio 3", "q": "Según el programa, en un salón pequeño es mejor...", "o": ["poner el sofá al lado de la ventana.", "tener varias lámparas pequeñas.", "poner un espejo delante del sofá."], "ok": 0,
   "cats": ["ubicar", "muebles"], "es": "ES-06", "pc": "preposiciones de lugar (delante de, al lado de, enfrente de) · LX-10",
   "lab": "Locutor", "voice": "JAVIER/RADIO",
   "text": "Bienvenidos a «Tu casa, tu estilo». Hoy, un consejo para salones pequeños: el sofá no tiene que estar delante de la ventana; es mejor ponerlo al lado, porque así entra más luz. Y en vez de muchas lámparas pequeñas, es mejor una lámpara de pie grande. Un espejo enfrente de la ventana también da más luz al salón.",
   "why": "El sofá, mejor al lado de la ventana, no delante. En vez de varias lámparas pequeñas, una grande; y el espejo va enfrente de la ventana, no del sofá."},
  {"n": 10, "conv": "Audio 4", "q": "Según la encuesta, los oyentes más jóvenes prefieren...", "o": ["el salón.", "la cocina.", "su dormitorio."], "ok": 2,
   "cats": ["gustos", "vivienda"], "es": "ES-08", "pc": "GR-07 preferir · LX-10 partes de la casa",
   "lab": "Locutora", "voice": "MIA/RADIO",
   "text": "Hoy os contamos los resultados de nuestra encuesta: ¿cuál es vuestro lugar favorito de la casa? Para la mayoría de los oyentes es el salón, porque allí ven la tele y están con la familia. En segundo lugar está la cocina. Los oyentes más jóvenes, en cambio, prefieren su habitación: dicen que es el único lugar tranquilo de la casa.",
   "why": "Los jóvenes prefieren su habitación (su dormitorio). El salón es el favorito de la mayoría y la cocina está en segundo lugar."},
  {"n": 11, "conv": "Audio 5", "q": "Según el anuncio, las personas que quieren vender en el mercadillo...", "o": ["pueden ir solo por la tarde.", "tienen que inscribirse antes.", "solo pueden vender muebles."], "ok": 1,
   "cats": ["muebles"], "es": "ES-03", "pc": "LX-10 muebles y objetos · hay que / tener que + infinitivo",
   "lab": "Locutor", "voice": "LUIS_GUILLERMO/RADIO",
   "text": "Este domingo, en la plaza del Mercado, vuelve el mercadillo de muebles de segunda mano. De nueve de la mañana a dos de la tarde, vecinos y tiendas venden sillas, lámparas, mesas y objetos de decoración a muy buen precio. Si quieres vender algo, tienes que apuntarte antes del viernes en la página web del Ayuntamiento.",
   "why": "Hay que apuntarse antes del viernes: inscribirse antes. El mercadillo es por la mañana y también se venden objetos de decoración."},
  {"n": 12, "conv": "Audio 6", "q": "La residencia Los Olivos...", "o": ["cuesta menos que un piso en el centro.", "tiene habitaciones sin baño.", "incluye todas las comidas."], "ok": 0,
   "cats": ["comparar", "vivienda"], "es": "ES-06", "pc": "GR-05 (más barata que) · LX-10 · LX-14 alojamiento",
   "lab": "Locutora", "voice": "CRISTINA/RADIO",
   "text": "¿Vienes a estudiar a Granada? La residencia universitaria Los Olivos tiene habitaciones individuales y dobles, todas con baño. Es más barata que un piso de alquiler en el centro y está a cinco minutos de la universidad en autobús. El precio incluye el desayuno y la cena. Reserva ya tu plaza para el próximo curso.",
   "why": "Es más barata que un piso en el centro: cuesta menos. Todas las habitaciones tienen baño, y el precio incluye el desayuno y la cena, no todas las comidas."},
 ]}
for _x in [CA2["example"]] + CA2["items"]:
    _x["sound"] = RADIO_FX

CH = "SONIDO 2: Two-tone ding-dong chime of a public address announcement system, clean and clear, no voices, no background noise"
BP = "SONIDO 1: Single short electronic answering machine beep, clean, no background noise"
CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. En cada mensaje pregúntate: ¿quién habla, dónde está y qué pasa? Sobran tres enunciados.",
 "enun": [
  "Una visita a una vivienda cambia de hora.",
  "Durante unas horas no se va a poder usar el ascensor.",
  "Hay descuentos en una tienda de muebles.",
  "Alguien ofrece su ayuda para un cambio de casa.",
  "Van a arreglar un aparato de la casa.",
  "Hay una reunión de la comunidad de vecinos.",
  "Una tienda no cobra por llevar las compras a casa.",
  "Una persona pide a otra que reciba algo por ella.",
  "Una persona busca compañero de piso.",
  "Una parte de una feria cierra antes de lo habitual.",
  "Alguien explica cómo ganar espacio en una vivienda pequeña."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "DIANA/RADIO", "sound": BP,
   "text": "Hola, buenos días, soy Paula, de la inmobiliaria Casa Nova. Le llamo por el piso de la calle Luna. Lo siento, pero la visita de mañana no puede ser a las cinco. ¿Le va bien a las siete? Llámeme, por favor. Gracias.",
   "solucion": "La opción correcta es la letra a: una visita a una vivienda cambia de hora."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 6, "cats": ["muebles"], "es": "ES-10", "pc": "LX-12 compras · LX-10",
   "lab": "Megafonía", "voice": "SARA/RADIO", "sound": CH,
   "text": "Atención, señores clientes. Les recordamos que el transporte a domicilio es gratis para compras de más de quinientos euros. Pueden pedirlo en la caja central, en la planta baja. Muchas gracias por su visita.",
   "why": "El transporte a casa es gratis (con compras de más de quinientos euros). No habla de descuentos: la C sobra."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 3, "cats": ["vivienda", "muebles"], "es": "ES-10", "pc": "LX-10 mudanza · FN ofrecer ayuda",
   "lab": "Contestador", "voice": "MILO/RADIO", "sound": BP,
   "text": "Hola, Clara, soy Toni. Oye, ¿el sábado necesitas ayuda con la mudanza? Tengo la furgoneta de mi hermano todo el día, así que puedo llevar las cajas y los muebles grandes al piso nuevo. Llámame y me dices a qué hora voy.",
   "why": "Toni se ofrece a ayudar a Clara con la mudanza. Nadie busca compañero de piso: la I sobra."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 10, "cats": ["vivienda", "describir"], "es": "ES-09", "pc": "LX-10 · LX-18 decoración",
   "lab": "Megafonía", "voice": "EMILIO/RADIO", "sound": CH,
   "text": "Estimados clientes: hoy, a las seis de la tarde, en la sección de hogar de la cuarta planta, la decoradora Ana Prieto da una charla con ideas para tener más espacio en las casas pequeñas. La entrada es libre. Les esperamos.",
   "why": "Una decoradora da ideas para tener más espacio en casas pequeñas. Es en unos grandes almacenes, pero no hay descuentos (C)."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 4, "cats": ["muebles"], "es": "ES-10", "pc": "LX-10 electrodomésticos · LX-11 servicios",
   "lab": "Contestador", "voice": "AGUSTIN/RADIO", "sound": BP,
   "text": "Buenas tardes, le llamo del servicio técnico de Electrodomésticos Faro. Ya tenemos la pieza para su lavadora. El técnico puede pasar por su casa el jueves por la mañana, entre las nueve y las doce. Si no le va bien, llámenos.",
   "why": "El técnico va a ir a casa a arreglar la lavadora, un aparato de la casa."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 7, "cats": ["vivienda"], "es": "ES-10", "pc": "LX-10 (vecina, tercero) · FN pedir un favor",
   "lab": "Contestador", "voice": "ESTELA/RADIO", "sound": BP,
   "text": "Hola, Marta, soy Carmen, la vecina del tercero. Mira, mañana no estoy en casa en todo el día y me llega un paquete con unas cortinas. ¿Lo puedes recoger tú? El repartidor viene por la tarde. ¡Muchas gracias, guapa!",
   "why": "Carmen le pide a su vecina que recoja un paquete por ella. Es una vecina, pero no hay reunión de la comunidad (F)."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 9, "cats": ["muebles"], "es": "ES-07", "pc": "LX-10 cocinas · horarios",
   "lab": "Megafonía", "voice": "NINOSKA/RADIO", "sound": CH,
   "text": "Aviso a los visitantes de la Feria del Mueble: hoy la exposición de cocinas del pabellón dos cierra a las ocho, una hora antes de lo normal. Los demás pabellones abren hasta las nueve. Mañana, último día de la feria, el horario es de diez a tres.",
   "why": "Hoy la zona de cocinas cierra una hora antes de lo normal. El resto de la feria tiene su horario de siempre."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 1, "cats": ["vivienda"], "es": "ES-09", "pc": "LX-10 (ascensor, edificio, escalera)",
   "lab": "Contestador", "voice": "TOMAS/RADIO", "sound": BP,
   "text": "Hola, soy Leo, el dueño del piso. Te llamo porque el lunes vienen a pintar la escalera del edificio y el ascensor no funciona por la mañana. Si tienes que bajar la bici, mejor hazlo el domingo. Perdona las molestias.",
   "why": "El lunes por la mañana el ascensor no funciona. Habla del edificio, pero no de una reunión de vecinos (F)."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]

REPARTO = """# REPARTO DE VOCES U04 (ninguna protagonista de la U03)
# T2 radio (perfil /RADIO, con sintonía antes de cada audio): 0 inmobiliaria = BOBBY · 1 noticia = CLARA
#   2 muebles = TAMARA (México) · 3 programa de decoración = JAVIER · 4 encuesta = MIA
#   5 mercadillo = LUIS_GUILLERMO (México) · 6 residencia = CRISTINA
# T4 mensajes (también /RADIO: cada mensaje entero con v3): 0 contestador inmobiliaria = DIANA (Colombia) · 1 megafonía tienda = SARA
#   2 contestador Toni = MILO · 3 megafonía grandes almacenes = EMILIO · 4 contestador técnico = AGUSTIN (Argentina)
#   5 contestador vecina = ESTELA · 6 megafonía feria = NINOSKA · 7 contestador dueño = TOMAS (Argentina)
# Efectos: sintonía de radio (T2), din-don de megafonía y pitido de contestador (T4); siempre la misma descripción (caché)"""

# ---------------- ESCRITURA ----------------
ESCRITA = {"t1": {"instr": "Un amigo le escribe porque usted se ha cambiado de casa.",
  "input": ["¡Hola! Me ha dicho Sara que ya vives en tu casa nueva. ¡Enhorabuena! ¿Dónde está? ¿Cómo es? ¿Es más grande que la otra? Tengo muchas ganas de verla. Cuéntamelo todo y dime cuándo puedo ir a visitarte.", "Un abrazo,<br>Hugo"],
  "lead": "Conteste a su amigo. En el correo tiene que:",
  "pautas": ["saludar;", "decir dónde está su casa nueva y cómo es;", "compararla con su casa anterior;", "explicar cuál es su lugar favorito de la casa y por qué;", "invitarlo a su casa, proponer un día y despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Escriba un texto sobre la casa de sus sueños. Hable de:",
   "pautas": ["dónde está y qué tipo de vivienda es;", "cuántas habitaciones tiene y cómo son;", "qué muebles hay en el salón y dónde están;", "en qué se parece y en qué es diferente de su casa actual;", "por qué le gusta."]},
  "op2": {"title": "Opción 2", "intro": "El verano pasado usted alquiló un apartamento para sus vacaciones. Aquí tiene el anuncio de la página web y tres fotos que usted hizo al llegar.",
   "photos": ["Desde la terraza no se ve el mar: delante hay un edificio alto y un aparcamiento.", "Una cocina muy pequeña con una nevera vieja; en la lavadora hay un papel: no funciona.", "Una calle con mucho tráfico y, al fondo, muy lejos, la playa."],
   "ficha": ["<b>Anuncio: Apartamento «Brisa del Mar»</b>", "A dos minutos de la playa", "60 m² · dos dormitorios · salón con terraza", "Vistas al mar · cocina totalmente equipada"],
   "intro2": "Escriba un texto sobre esas vacaciones. Hable de:",
   "pautas": ["dónde está el apartamento y con quién fue;", "en qué es diferente el apartamento real del apartamento del anuncio;", "qué hizo usted y cómo terminaron las vacaciones."],
   "img": "U04_escrita.jpg", "imgAlt": "Tres fotos del apartamento: la terraza, la cocina y la calle"},
  "min": 70, "max": 80}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: mi casa", "pautas": ["dónde está y qué tipo de vivienda es;", "cuántas habitaciones tiene y cómo es;", "cuál es su lugar favorito y qué hay en él;", "qué le gusta y qué no le gusta de su casa;", "con quién vive."]},
  {"title": "Opción 2: ¿vivir en el centro o en las afueras?", "pautas": ["dónde vive usted ahora: en el centro, en las afueras o en un pueblo;", "qué ventajas tiene vivir en el centro de una ciudad;", "qué ventajas tiene vivir en las afueras o en el campo;", "compare los precios, el ruido, el transporte y los servicios;", "dónde prefiere vivir usted y por qué."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1", "desc": "Una tienda de muebles. Una pareja joven está sentada en un sofá gris y lo prueba. Un dependiente les enseña un catálogo. Alrededor hay mesas, lámparas y estanterías.", "img": "U04_oral_foto1.jpg"},
  {"title": "Fotografía 2", "desc": "Un piso vacío en alquiler. Un agente inmobiliario con una carpeta enseña el salón a una mujer joven con una mochila. El salón tiene una ventana grande y el suelo de madera, y no hay muebles; al fondo se ve una cocina pequeña.", "img": "U04_oral_foto2.jpg"}],
  "pautas": ["las personas: cómo son, qué ropa llevan, qué hacen;", "el lugar: dónde están, qué cosas hay y dónde están;", "qué cree que piensan o necesitan las personas;", "qué cree que va a pasar después."]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1", "intro": "Usted quiere comprar un mueble para su casa y está en una tienda. Hable con el dependiente (su profesora). Tiene que:", "pautas": ["explicar qué mueble busca y para qué parte de la casa;", "decir de qué material, de qué color y de qué tamaño lo quiere;", "comparar dos modelos y elegir uno;", "preguntar el precio y si se lo llevan a casa."]},
  {"title": "Si eligió la fotografía 2", "intro": "Usted busca piso y llama por teléfono a una inmobiliaria por un anuncio. Hable con el agente (su profesora). Tiene que:", "pautas": ["saludar y decir qué anuncio ha visto;", "preguntar cómo es el piso y dónde está exactamente;", "preguntar el precio y qué incluye;", "quedar para visitarlo y despedirse."]}]}}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (mi casa): ¿Qué hay en su salón? · ¿Qué le gustaría cambiar de su casa?
    Opción 2 (centro o afueras): ¿Dónde es más caro vivir? · ¿Dónde vive su familia?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (tienda de muebles): ¿Qué cree que buscan? · ¿Van a comprar el sofá?
    Foto 2 (piso en alquiler): ¿Qué cree que pregunta la mujer? · ¿Le va a gustar el piso?
  Tarea 3 — su papel (aquí sí conversa: pregunte, reaccione y provoque un pequeño problema):
    Foto 1 (dependiente/a): sofás de tela (750 euros) y de piel (1200 euros), de dos y tres plazas,
    en gris, azul y beige; mesas de madera o de cristal. Llevar el mueble a casa cuesta 40 euros
    (gratis desde 1000 euros) y tarda una semana. Pregunte «¿Para qué parte de la casa?» y
    «¿Lo prefiere de tela o de piel?». Problema: el color que quiere no está hasta el mes que viene.
    Foto 2 (agente inmobiliario): piso de 70 m², dos habitaciones, tercero sin ascensor, da a un parque,
    amueblado, 750 euros al mes con la comunidad incluida, un mes de fianza; visitas el jueves por la
    tarde o el sábado por la mañana. Problema: el jueves a las seis ya está ocupado; no se admiten animales.
  Qué mirar en esta unidad: es / está / tiene / da a bien usados; comparativos (más... que, tan... como,
  tanto como, mejor); preposiciones de lugar con del / de la; posesivos tónicos; gustar / preferir."""
ERRORES = """  *Mi casa es en el centro (está); *Hay el sofá a la izquierda (está el sofá);
  *El sofá está de piel (es de piel); *al lado de el sofá (del sofá); *más grande como (que);
  *tan grande que (como); *más mejor / *más bueno (mejor); *tanto habitaciones (tantas);
  *Me gusta los muebles (me gustan); *Yo prefero (prefiero); *el mío casa / *la mía es mi casa
  (mi casa / la mía); concordancia del posesivo con la cosa (*mi terraza y el tuyo)."""
IMG_PROMPTS = {
 "portada": "Photorealistic, candid photo: a young Spanish couple sitting on the floor of their new bright living room among cardboard moving boxes, laughing and eating pizza from the box; a wooden shelf half filled with books and a plant by the big window; warm natural light, cozy atmosphere, no readable text, 16:9",
 "oral": "Photorealistic, candid photo of an adult Spanish class in a bright classroom: two adult students at a table look at a simple floor plan of an apartment and point at the rooms while the teacher listens; natural light, friendly atmosphere, no readable text, 3:2",
 "escrita": "Photorealistic triptych, three separate photos side by side of equal size with thin white borders, same holiday apartment in a Spanish coastal town. Left: view from a small balcony where a tall building and a car park block the view, no sea visible. Centre: a very small old kitchen with an old fridge and a washing machine with a handwritten paper note stuck on it, the note without readable text. Right: a street with heavy traffic and, far away in the background, a small strip of beach. Natural light, candid, no readable text, 3:1",
 "oral_foto1": "Photorealistic, candid photo inside a furniture store in Spain: a young couple sits on a grey sofa testing it while a male shop assistant shows them a catalogue; around them there are tables, lamps and bookshelves; bright indoor light, price tags without readable text, no readable text, 3:2",
 "oral_foto2": "Photorealistic, candid photo of an empty apartment for rent in Spain: a male real estate agent holding a folder shows the living room to a young woman with a backpack; big window, wooden floor, no furniture, a small kitchen visible in the background; natural light, no readable text, 3:2",
}
IMG_DESC = {"portada": "pareja joven en el suelo del salon nuevo entre cajas de mudanza", "oral": "clase: dos alumnos mirando el plano de un piso", "escrita": "tres fotos del apartamento: terraza sin vistas, cocina, calle", "oral_foto1": "tienda de muebles: pareja probando un sofa gris", "oral_foto2": "piso vacio en alquiler: agente y chica con mochila"}
CA1_DESC = {}

LECTURA = [CL2, CL4]
AUDITIVA = [CA2, CA4]
