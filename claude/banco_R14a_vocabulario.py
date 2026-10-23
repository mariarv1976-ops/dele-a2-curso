# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R14a: VOCABULARIO EN ESCENAS (1) · LA CASA Y EL DIA A DIA (curso DELE A2)
# Para cambiar contenidos, solo este archivo. Despues: python3 build_R14a_vocabulario.py
#
# ENFOQUE COGNITIVO (aprobado por Maria, 22/10): LAS PALABRAS VIVEN EN ESCENAS, NO EN LISTAS
#   Tres herramientas para aprender y recordar el lexico A2 de frecuencia ALTA:
#   1) LA ESCENA: cada palabra se guarda en un sitio (el piso que visitas, el restaurante, el medico...) y en una red
#      de cuatro ramas (quien / que cosas / que haces / que dices, o las que pida la escena). Se recuerda volviendo a
#      la escena: «tapa y recuerda» (el texto de la escena con huecos y la primera letra).
#   2) EL TRIO: en la tarea 1 de la auditiva, las tres vinetas son de la misma familia (tres prendas, tres medicinas)
#      y dos se descartan («antes estaba ahi, pero ahora...», «eso ya lo tengo», «se ha terminado»). Las palabras se
#      aprenden en trios que se confunden, con las frases que descartan.
#   3) LA PAREJA DE PARAFRASIS: el examen dice lo mismo con otras palabras (amueblado = con muebles, gratis = no se
#      paga). Cada area trae sus parejas para la lectura (tareas 2 y 3) y las tareas 2 y 4 de la auditiva.
#   AREAS (las de frecuencia ALTA del Plan curricular, apartado 5; la R14b tendra las de fuera de casa):
#   pe personas (LX-01, LX-02, LX-04) · ca vivienda (LX-10) · co comida y restaurante (LX-05) ·
#   cm compras y ropa (LX-12) · sa salud (LX-13).
#   NIVEL: solo lexico LX del Plan curricular, nada de B1. Sin combinaciones de dos pronombres (me lo, se la) ni
#   duplicacion del objeto directo en los audios ni en los textos (son [R]).
#
# MARCAS
#   En el texto de cada escena: [n:forma] o [n:forma=lema]   (n = rama 1-4 de la red; el lema es la palabra de la red)
#   En los audios de «Escucha y elige»: [v:...] la opcion buena · [x:...] las que se mencionan y se descartan
#   Huecos: [[correcta|distractor|distractor#motivo]]  (la primera es la buena; se barajan)
# Espanol de Espana. Ejemplos propios: nada sale de los materiales de Maria ni de los manuales; no repite las
# conversaciones de la tarea 1 del M1 (cabeza/garganta/espalda, jarabe/pastillas/crema, correr/yoga/nadar...).

MES_WP = "2026/10"   # carpeta del mes en que se suben los audios y las vinetas a WordPress (si cambia, cambiar aqui)
MES_WP_T2 = "2026/10"   # carpeta de las fotos de la oral M4T2_fotoN.jpg (ya subidas)
SIGLA = "R14a"

# ------------------------------------------------------------------ AREAS
AREAS = {
    "pe": {"n": "Personas", "lx": "LX-01, LX-02, LX-04", "txt": "cómo es una persona, cómo está y quién es en tu familia"},
    "ca": {"n": "La casa", "lx": "LX-10", "txt": "el piso, los muebles, el edificio y las tareas de casa"},
    "co": {"n": "La comida", "lx": "LX-05", "txt": "el mercado, la cocina y el restaurante"},
    "cm": {"n": "Las compras", "lx": "LX-12", "txt": "la ropa, las tiendas y cómo pagas"},
    "sa": {"n": "La salud", "lx": "LX-13", "txt": "el cuerpo, el médico, la farmacia y los hábitos"},
}
ORDEN_AREAS = ["pe", "ca", "co", "cm", "sa"]

# ------------------------------------------------------------------ LAS ESCENAS
# Cada escena: id, area, titulo, lugar (donde pasa), ramas (4: nombre + palabras), texto marcado.
# En las ramas, los nombres van con su articulo: apréndelos asi (la camiseta del nombre, R04).
ESCENAS = [
 {"id": "pe1", "area": "pe", "titulo": "¿Cómo es?", "lugar": "Una foto de la boda de mi prima",
  "ramas": [("La cara y el pelo", ["el pelo", "largo", "corto", "rizado", "liso", "los ojos", "claro", "oscuro", "la barba", "el bigote", "las gafas", "calvo"]),
            ("El cuerpo y la edad", ["alto", "bajo", "delgado", "fuerte", "joven", "mayor", "de unos cuarenta años"]),
            ("El carácter", ["simpático", "tímido", "serio", "divertido", "abierto", "trabajador", "tranquilo", "amable"]),
            ("Lo que dices", ["Es alta y lleva gafas.", "Tiene el pelo rizado.", "Parece muy simpático.", "Tiene unos cuarenta años."])],
  "texto": "En esta foto de la boda de mi prima Lola está casi toda mi familia. El chico [2:alto] de las [1:gafas] es mi primo Dani: es muy [3:tímido], "
           "pero también muy [3:divertido]. A su lado está mi tía Pilar, que ya es [2:mayor] y tiene el [1:pelo] [1:corto]. Mi tío Juan es [1:calvo] y lleva [1:bigote]. "
           "Lola, la novia, es [2:delgada=delgado], tiene los [1:ojos] [1:claros=claro] y el pelo [1:rizado]. Es muy [3:abierta=abierto] y muy [3:trabajadora=trabajador]. "
           "¿Y el chico [2:joven] con [1:barba]? Es Marcos, su marido: en las fotos parece [3:serio], pero es muy [3:simpático]."},
 {"id": "pe2", "area": "pe", "titulo": "La familia y cómo estamos", "lugar": "La comida del domingo en casa de los abuelos",
  "ramas": [("La familia", ["los abuelos", "el abuelo", "la abuela", "el nieto", "el tío", "la tía", "el primo", "el sobrino", "el suegro", "la suegra", "el cuñado", "el marido", "la mujer", "la pareja"]),
            ("Las relaciones", ["el vecino", "el compañero", "el amigo", "llevarse bien", "llevarse mal", "conocer a alguien", "quedar", "casarse"]),
            ("Cómo estás (estar)", ["contento", "triste", "cansado", "aburrido", "preocupado", "enfadado", "nervioso"]),
            ("Lo que tienes (tener)", ["tener hambre", "tener sed", "tener frío", "tener calor", "tener sueño", "tener miedo"])],
  "texto": "Todos los domingos comemos en casa de mis [1:abuelos]. Hoy está toda la familia: mis padres, mi [1:tía] Rosa con su [1:marido] Antonio, y mis dos [1:primos=el primo]. "
           "Mi [1:cuñado] Luis ha venido con su hijo, mi [1:sobrino] Pablo, que tiene seis años. Pablo [4:tiene hambre=tener hambre] y está un poco [3:nervioso]. "
           "Mi [1:abuela] está muy [3:contenta=contento] porque estamos todos. Mi tía y su [1:suegra] no [2:se llevan bien=llevarse bien], pero hoy están muy simpáticas. "
           "Después de comer, mi [1:abuelo] [4:tiene sueño=tener sueño] y se va al sofá, y los niños, [3:aburridos=aburrido], salen al jardín."},
 {"id": "ca1", "area": "ca", "titulo": "El piso", "lugar": "La visita a un piso en alquiler",
  "ramas": [("Las partes", ["el salón", "el dormitorio", "la cocina", "el baño", "la terraza", "el balcón", "el pasillo"]),
            ("Los muebles y los aparatos", ["el sofá", "el armario", "la estantería", "la cama", "la mesa", "la silla", "la lavadora", "la nevera", "el horno", "el microondas"]),
            ("Cómo es", ["luminoso", "amueblado", "exterior", "interior", "grande", "pequeño", "cómodo", "tranquilo"]),
            ("El edificio", ["el portal", "el ascensor", "la planta", "la escalera", "el vecino", "el garaje"])],
  "texto": "Ayer vimos un piso en alquiler. Está en la tercera [4:planta] y el edificio tiene [4:ascensor]. Es muy [3:luminoso] porque es [3:exterior]: "
           "el [1:salón] tiene un [1:balcón] a la calle. Hay dos [1:dormitorios=el dormitorio], un [1:baño] y una [1:cocina] [3:pequeña=pequeño] con [2:nevera], [2:horno] y [2:lavadora]. "
           "Está [3:amueblado]: en el salón hay un [2:sofá] y una [2:estantería], y en los dormitorios, [2:camas=la cama] y [2:armarios=el armario]. "
           "El [4:portal] es un poco viejo, pero los [4:vecinos=el vecino] son muy simpáticos."},
 {"id": "ca2", "area": "ca", "titulo": "La vida en casa", "lugar": "Un piso compartido",
  "ramas": [("Cambiar de casa", ["alquilar", "el alquiler", "compartir piso", "el compañero de piso", "mudarse", "la mudanza", "la llave"]),
            ("Las tareas", ["hacer la cama", "poner la mesa", "fregar los platos", "hacer la compra", "sacar la basura", "limpiar", "planchar", "poner la lavadora"]),
            ("Las cosas de casa", ["la basura", "el suelo", "la ventana", "la puerta", "la luz", "la ropa"]),
            ("Lo que dices", ["¿Te ayudo?", "Hoy me toca a mí.", "Te toca fregar.", "¿Dónde dejo las llaves?"])],
  "texto": "El mes pasado [1:me mudé=mudarse] a un piso nuevo. Ahora [1:comparto piso=compartir piso] con Nuria, una [1:compañera de piso=el compañero de piso] muy ordenada. "
           "Pagamos el [1:alquiler] a medias y tenemos una lista de tareas en la nevera. Los lunes yo [2:saco la basura=sacar la basura] y ella [2:friega los platos=fregar los platos]. "
           "Los sábados [2:hacemos la compra=hacer la compra] juntas en el súper de la esquina. Yo [2:plancho=planchar] la [3:ropa] y ella [2:pone la lavadora=poner la lavadora]. "
           "El domingo [2:limpiamos=limpiar] el [3:suelo] y las [3:ventanas=la ventana]. ¡Y cada una [2:hace la cama=hacer la cama] de su habitación!"},
 {"id": "co1", "area": "co", "titulo": "En el mercado y en la cocina", "lugar": "El sábado: compras y una tortilla",
  "ramas": [("Los alimentos", ["la carne", "el pescado", "la verdura", "la fruta", "las legumbres", "los huevos", "el pan", "el arroz", "la pasta", "el queso", "el aceite"]),
            ("Envases y cantidades", ["una botella de", "una lata de", "un paquete de", "una docena de", "medio kilo de", "un kilo de"]),
            ("En la cocina", ["cortar", "pelar", "freír", "hervir", "mezclar", "añadir", "la sartén", "la olla"]),
            ("Cómo está", ["dulce", "salado", "picante", "rico", "fresco"])],
  "texto": "Los sábados hago la compra en el mercado. Compro [2:medio kilo de] [1:carne], [1:pescado] [4:fresco] y mucha [1:verdura]. En la frutería compro [1:fruta] y [2:una docena de] [1:huevos]. "
           "Después, en el súper, compro [2:un paquete de] [1:arroz] y [2:una botella de] [1:aceite]. Por la tarde cocino: [3:pelo=pelar] las patatas, las [3:corto=cortar] "
           "y las [3:frío=freír] en la [3:sartén]. Luego las [3:mezclo=mezclar] con los huevos y... ¡tortilla! A mi hija no le gusta la comida [4:picante]: prefiere los postres [4:dulces=dulce]."},
 {"id": "co2", "area": "co", "titulo": "En el restaurante", "lugar": "Una cena de cumpleaños",
  "ramas": [("Las personas y las cosas", ["el camarero", "la carta", "el menú del día", "la mesa", "la cuenta", "la propina", "la reserva"]),
            ("Los platos y las comidas", ["el primer plato", "el segundo plato", "el postre", "la ensalada", "la paella", "el gazpacho", "el desayuno", "la comida", "la merienda", "la cena"]),
            ("Lo que haces", ["reservar una mesa", "pedir", "pedir la cuenta", "dejar propina", "pagar"]),
            ("Lo que dices", ["¿Me trae la carta, por favor?", "De primero, una ensalada.", "Para mí, el pescado.", "La cuenta, por favor."])],
  "texto": "El viernes [3:reservamos una mesa=reservar una mesa] en un restaurante del centro para la [2:cena] de cumpleaños de Ana. El [1:camarero] nos trajo la [1:carta], "
           "pero todos pedimos el [1:menú del día]. De [2:primero=el primer plato], [2:gazpacho] o [2:ensalada]; de [2:segundo=el segundo plato], [2:paella]; "
           "y de [2:postre], fruta o helado. Al final, [3:pedimos la cuenta=pedir la cuenta]: veinte euros cada uno. Como el camarero fue muy amable, "
           "dejamos dos euros de [1:propina]."},
 {"id": "cm1", "area": "cm", "titulo": "La tienda de ropa", "lugar": "Un sábado de rebajas",
  "ramas": [("La ropa", ["el abrigo", "la chaqueta", "la camiseta", "la camisa", "el jersey", "los vaqueros", "la falda", "el vestido", "la bufanda", "los guantes"]),
            ("Los pies", ["los zapatos", "las zapatillas", "las botas", "las sandalias", "los calcetines"]),
            ("En la tienda", ["el probador", "la talla", "el número", "el dependiente", "las rebajas", "el descuento", "probarse", "quedar grande", "quedar pequeño"]),
            ("Lo que dices", ["¿Tiene una talla más grande?", "¿Dónde está el probador?", "Me queda pequeño.", "¿Cuánto cuesta?"])],
  "texto": "En [3:rebajas=las rebajas] siempre voy a la misma tienda. El sábado vi un [1:abrigo] azul con un [3:descuento] del treinta por ciento. "
           "Le pregunté al [3:dependiente] por mi [3:talla] y fui al [3:probador], pero me [3:quedaba grande=quedar grande]. "
           "Al final compré una [1:bufanda] y unos [1:guantes] de lana. También me [3:probé=probarse] unas [2:botas], pero no tenían mi [3:número]. Mi hermana se compró unas [2:sandalias] y una [1:camiseta] muy barata."},
 {"id": "cm2", "area": "cm", "titulo": "Las tiendas del barrio", "lugar": "Mi calle, de tienda en tienda",
  "ramas": [("Las tiendas", ["la panadería", "la frutería", "la carnicería", "la pescadería", "el supermercado", "el mercado", "el quiosco", "la librería", "la zapatería", "el centro comercial"]),
            ("El precio y el pago", ["el precio", "barato", "caro", "la oferta", "pagar en efectivo", "pagar con tarjeta", "el ticket"]),
            ("Cambiar y devolver", ["devolver", "cambiar", "estar roto", "abierto", "cerrado"]),
            ("Lo que dices", ["¿Cuánto es?", "¿Me pone medio kilo?", "Quería unas naranjas.", "¿Puedo pagar con tarjeta?"])],
  "texto": "En mi barrio hay de todo. Compro el pan en la [1:panadería] de la esquina y la fruta en la [1:frutería] de Toñi, que siempre tiene [2:ofertas=la oferta]. "
           "La [1:carnicería] es un poco [2:cara=caro], pero la carne es muy buena. El periódico lo compro en el [1:quiosco], y los libros, en una [1:librería] pequeña. "
           "Allí puedo [2:pagar con tarjeta], pero en el mercado siempre [2:pago en efectivo=pagar en efectivo]. Ayer [3:devolví=devolver] unas zapatillas en la [1:zapatería]: "
           "me dieron el dinero porque tenía el [2:ticket]."},
 {"id": "sa1", "area": "sa", "titulo": "En el médico", "lugar": "El lunes, con gripe... o casi",
  "ramas": [("El cuerpo", ["la cabeza", "la garganta", "el estómago", "la espalda", "el brazo", "la mano", "la pierna", "la rodilla", "el pie", "los oídos"]),
            ("Los síntomas", ["el dolor", "la fiebre", "la tos", "la gripe", "el resfriado", "estar mareado", "la alergia"]),
            ("El centro de salud", ["el médico", "el enfermero", "la cita", "pedir cita", "la receta", "las urgencias"]),
            ("Lo que dices", ["Me duele la cabeza.", "Tengo fiebre.", "Me encuentro mal.", "¿Qué le pasa?"])],
  "texto": "El lunes me levanté con [2:fiebre] y me dolía mucho la [1:garganta]. Llamé al centro de salud para [3:pedir cita]. "
           "Primero, el [3:enfermero] me tomó la temperatura. Después, la [3:médica=el médico] me preguntó qué me pasaba y le dije que tenía [2:tos] y me dolía la [1:cabeza]. "
           "Me dijo que no era la [2:gripe], solo un [2:resfriado]. Me dio una [3:receta] para un jarabe y me dijo: «Beba mucha agua y descanse»."},
 {"id": "sa2", "area": "sa", "titulo": "La farmacia y los hábitos", "lugar": "Cuidarse en casa",
  "ramas": [("En la farmacia", ["la farmacia", "la farmacia de guardia", "las pastillas", "el jarabe", "la crema", "el termómetro"]),
            ("Hábitos sanos", ["dormir bien", "hacer deporte", "comer sano", "beber agua", "descansar", "caminar"]),
            ("La higiene", ["ducharse", "lavarse los dientes", "lavarse las manos", "peinarse"]),
            ("Lo que dices", ["¿Tiene algo para la tos?", "Una pastilla cada ocho horas.", "¿Necesito receta?", "¡Que te mejores!"])],
  "texto": "Este año he cambiado mis hábitos. Ahora [2:duermo bien=dormir bien], [2:hago deporte=hacer deporte] tres veces por semana y [2:como sano=comer sano]. "
           "Cuando me duele la cabeza, no voy enseguida a la [1:farmacia] a comprar [1:pastillas]: primero [2:descanso=descansar] y [2:bebo agua=beber agua]. "
           "Pero el domingo pasado mi hijo tenía tos y fuimos a la [1:farmacia de guardia]. La farmacéutica nos dio un [1:jarabe] y un [1:termómetro] nuevo. "
           "Por la noche, mi hijo [3:se lavó los dientes=lavarse los dientes], [3:se duchó=ducharse] y se fue a la cama. Hoy ya está mucho mejor."},
]

# Trios que el examen pone juntos (las tres vinetas de la tarea 1): cada palabra tiene que estar en la red de su area
TRIOS = {
    "pe": [("La cara", ["las gafas", "la barba", "el bigote"]), ("Cómo está", ["cansado", "preocupado", "enfadado"]), ("La familia", ["el primo", "el sobrino", "el cuñado"])],
    "ca": [("Los muebles", ["el sofá", "la estantería", "el armario"]), ("Las partes", ["el salón", "la cocina", "la terraza"]), ("Los aparatos", ["la lavadora", "la nevera", "el horno"])],
    "co": [("Los platos", ["la paella", "el gazpacho", "la ensalada"]), ("En la cocina", ["pelar", "cortar", "freír"]), ("Los alimentos", ["el arroz", "los huevos", "el aceite"])],
    "cm": [("La ropa", ["la falda", "el vestido", "los vaqueros"]), ("Pagar", ["pagar con tarjeta", "pagar en efectivo", "el ticket"]), ("Las tiendas", ["la panadería", "la frutería", "el supermercado"])],
    "sa": [("El cuerpo", ["el brazo", "la rodilla", "el pie"]), ("Los síntomas", ["la fiebre", "la tos", "el dolor"]), ("En la farmacia", ["las pastillas", "el jarabe", "la crema"])],
}

# Parejas de parafrasis: lo que dice el texto (o el audio) y como lo dice la pregunta
PAREJAS = {
    "pe": [("Es calvo.", "No tiene pelo."), ("Es mayor.", "No es joven."), ("Tiene sueño.", "Quiere dormir."),
           ("Es muy tímido.", "Al principio no habla mucho con gente nueva."), ("Se llevan muy bien.", "Son muy buenos amigos.")],
    "ca": [("Está amueblado.", "Tiene muebles."), ("Es exterior.", "Las ventanas dan a la calle."), ("Es muy luminoso.", "Tiene mucha luz."),
           ("Compartimos piso.", "Vivimos en el mismo piso."), ("La luz y el agua están incluidas.", "No pagas aparte la luz ni el agua.")],
    "co": [("Una docena de huevos.", "Doce huevos."), ("Es vegetariano.", "No come carne ni pescado."), ("¿Me trae la cuenta?", "Quiere pagar."),
           ("El pescado se ha terminado.", "Ya no hay pescado."), ("Menú del día: primero, segundo y postre.", "Hay tres platos.")],
    "cm": [("Gratis.", "No se paga."), ("Estamos de rebajas.", "Los precios son más bajos."), ("En efectivo.", "Con billetes y monedas."),
           ("Me queda pequeño.", "Necesito una talla más grande."), ("Cerrado por vacaciones.", "Estos días no abre.")],
    "sa": [("Tengo fiebre.", "Tengo la temperatura alta."), ("Farmacia de guardia.", "Abre cuando las otras están cerradas."), ("Pedir cita.", "Pedir un día y una hora para ir al médico."),
           ("Me encuentro mal.", "No estoy bien."), ("Una pastilla cada ocho horas.", "Tres pastillas al día.")],
}

# ------------------------------------------------------------------ ESCUCHA Y ELIGE (tarea 1 de la auditiva)
# Las frases que descartan: (frase, que hace, ejemplo de esta ficha)
DESCARTE = [
    ("No, ... no.", "Dice que no claramente.", "—¿Te duele el brazo? —El brazo no."),
    ("Antes..., pero ahora...", "Lo de antes ya no vale: la respuesta es lo de ahora.", "Antes llevaba barba, pero ahora ya no."),
    ("Ya tengo... / ya estaba...", "Esa cosa ya la tiene: no la compra.", "Huevos tenemos, hay una docena en la nevera."),
    ("Se ha terminado / no hay / no tenemos", "Esa opción no es posible.", "Lo siento, el pescado se ha terminado."),
    ("Ese es... (otra persona)", "La palabra es de otra persona.", "No, ese es su hermano."),
    ("Pues entonces... / Mejor...", "La decisión final: casi siempre es la respuesta.", "Pues entonces, en la cocina."),
]
# 12 conversaciones (50-80 palabras): la mitad de una ronda sale al azar. lines = (etiqueta, voz, texto con etiqueta de emocion)
# ok = indice de la opcion buena; img = nombre de la imagen (las tres vinetas A-B-C en un triptico); prompt = un panel por opcion, en orden
CA1 = [
 {"area": "pe", "q": "¿Cómo es ahora Lucas?", "o": ["con gafas", "con barba", "con bigote"], "ok": 2,
  "pres": "Va a escuchar a dos amigas que están en una fiesta.",
  "lines": [("Mujer 1", "CAROLINA", "[curious] Oye, ¿cuál es Lucas, el novio de Ana? ¿Es ese chico alto de las [x:gafas]?"),
            ("Mujer 2", "RAQUEL", "[laughs] No, no, ese es su hermano. Lucas es más bajo. Antes llevaba [x:barba], pero ahora ya no."),
            ("Mujer 1", "CAROLINA", "[surprised] ¿Ah, sí? Entonces es el chico del [v:bigote], ¿no? El que está al lado de la ventana."),
            ("Mujer 2", "RAQUEL", "[cheerful] ¡Ese! Ahora lleva bigote. Dice que así parece mayor. Ven, vamos a saludarlo.")],
  "why": "Ahora Lucas lleva <b>bigote</b>. El chico de las gafas es su hermano, y la barba la llevaba antes.",
  "img": "R14a_CA1_01_gafas_barba_bigote",
  "prompt": "Panel 1: the face and shoulders of a young man with glasses and short hair. Panel 2: the face and shoulders of a young man with a full beard. Panel 3: the face and shoulders of a young man with a moustache."},
 {"area": "pe", "q": "¿Cómo está hoy Teresa?", "o": ["cansada", "preocupada", "enfadada"], "ok": 1,
  "pres": "Va a escuchar a un hombre y una mujer que hablan por teléfono de una compañera.",
  "lines": [("Hombre", "MARTIN_3", "[concerned] Hola, Elena. Oye, ¿qué le pasa a Teresa? Esta mañana no me ha saludado. ¿Está [x:enfadada] conmigo?"),
            ("Mujer", "SUSANA", "[reassuring] No, hombre, no está enfadada. Ayer estaba muy [x:cansada] por el trabajo, eso sí."),
            ("Hombre", "MARTIN_3", "[curious] ¿Y hoy?"),
            ("Mujer", "SUSANA", "[thoughtful] Hoy está [v:preocupada]: su hijo tiene fiebre y no sabe si puede venir a trabajar mañana. Por eso no te ha dicho nada.")],
  "why": "Hoy Teresa está <b>preocupada</b> por su hijo. Cansada estaba ayer, y enfadada no está.",
  "img": "R14a_CA1_02_cansada_preocupada_enfadada",
  "prompt": "Panel 1: a tired woman yawning at her desk. Panel 2: a worried woman looking at her phone with her hand on her forehead. Panel 3: an angry woman with crossed arms and a frown."},
 {"area": "ca", "q": "¿Qué ha comprado Iván para su piso?", "o": ["un sofá", "una lavadora", "una estantería"], "ok": 2,
  "pres": "Va a escuchar a dos amigos que hablan del piso nuevo de Iván.",
  "lines": [("Mujer", "ESTELA", "[cheerful] ¡Iván! ¿Qué tal el piso nuevo? ¿Ya tienes [x:sofá]?"),
            ("Hombre", "GABRIEL_ES", "[relaxed] Todavía no. Mi hermana me va a dar el suyo el mes que viene."),
            ("Mujer", "ESTELA", "[curious] ¿Y la [x:lavadora]? ¿Funciona bien?"),
            ("Hombre", "GABRIEL_ES", "[laughs] Sí, la lavadora ya estaba en el piso y es casi nueva. Ayer compré una [v:estantería] para los libros: la voy a montar el sábado.")],
  "why": "Ha comprado una <b>estantería</b>. El sofá se lo da su hermana más adelante, y la lavadora ya estaba en el piso.",
  "img": "R14a_CA1_03_sofa_lavadora_estanteria",
  "prompt": "Panel 1: a three-seater sofa. Panel 2: a washing machine. Panel 3: a wooden bookshelf."},
 {"area": "ca", "q": "¿Dónde van a poner la mesa nueva?", "o": ["en el salón", "en la cocina", "en la terraza"], "ok": 1,
  "pres": "Va a escuchar a una pareja que habla de una mesa nueva.",
  "lines": [("Hombre", "DAVID_M1", "[thinking] Bueno, ¿dónde ponemos la mesa nueva? ¿En el [x:salón], al lado del sofá?"),
            ("Mujer", "MIA", "[doubtful] En el salón ya no cabe nada. ¿Y en la [x:terraza]? Es muy bonita."),
            ("Hombre", "DAVID_M1", "[unconvinced] En la terraza no, que en invierno hace mucho frío y no salimos nunca."),
            ("Mujer", "MIA", "[decided] Pues entonces, en la [v:cocina]. Es grande y así desayunamos allí todos los días.")],
  "why": "La van a poner en la <b>cocina</b>. En el salón no cabe, y en la terraza hace frío en invierno.",
  "img": "R14a_CA1_04_salon_cocina_terraza",
  "prompt": "Panel 1: a small round table in a living room next to a sofa. Panel 2: a small round table in a kitchen. Panel 3: a small round table on a balcony terrace with plant pots."},
 {"area": "co", "q": "¿Qué pide el hombre de segundo plato?", "o": ["pescado", "carne", "tortilla"], "ok": 2,
  "pres": "Va a escuchar a un hombre que habla con una camarera en un restaurante.",
  "lines": [("Mujer", "SARA", "[polite] Buenas tardes. ¿Qué va a tomar de primero?"),
            ("Hombre", "JAVIER", "[friendly] Un gazpacho, por favor. Y de segundo, el [x:pescado] del día."),
            ("Mujer", "SARA", "[apologetic] Lo siento, el pescado se ha terminado. Tenemos [x:carne] a la plancha o [v:tortilla] de patatas."),
            ("Hombre", "JAVIER", "[thoughtful] Carne no como... Pues tortilla, entonces. ¿Y me trae un poco más de pan, por favor?")],
  "why": "Pide <b>tortilla</b>: el pescado se ha terminado y él no come carne.",
  "img": "R14a_CA1_05_pescado_carne_tortilla",
  "prompt": "Panel 1: a plate of grilled fish with a slice of lemon. Panel 2: a plate with a grilled steak. Panel 3: a plate with a slice of Spanish potato omelette."},
 {"area": "co", "q": "¿Qué tiene que comprar el chico?", "o": ["arroz", "huevos", "aceite"], "ok": 0,
  "pres": "Va a escuchar a dos compañeros de piso antes de ir al supermercado.",
  "lines": [("Hombre", "MILO", "[hurried] Me voy al súper, que cierra a las nueve. ¿Compro [x:huevos]?"),
            ("Mujer", "CRISTINA", "[calm] No, huevos tenemos: hay una docena en la nevera. Y [x:aceite] también, ayer compré una botella."),
            ("Hombre", "MILO", "[curious] ¿Entonces qué falta? ¿Pan?"),
            ("Mujer", "CRISTINA", "[cheerful] Pan tenemos de ayer. Falta [v:arroz]: compra un paquete, que el domingo hago paella para mis padres. ¡Y no tardes, eh!")],
  "why": "Tiene que comprar <b>arroz</b> para la paella. Huevos y aceite ya tienen en casa.",
  "img": "R14a_CA1_06_arroz_huevos_aceite",
  "prompt": "Panel 1: a packet of rice. Panel 2: an egg box with a dozen eggs. Panel 3: a bottle of olive oil."},
 {"area": "co", "q": "¿Qué tiene que hacer ahora el chico?", "o": ["pelar las patatas", "cortar la cebolla", "freír las patatas"], "ok": 2,
  "pres": "Va a escuchar a un chico que habla por teléfono con su abuela mientras cocina.",
  "lines": [("Hombre", "ANTONIO", "[eager] Abuela, ya he [x:pelado las patatas], ¡cinco! ¿Ahora [x:corto la cebolla]?"),
            ("Mujer", "LUCIA", "[warm] No, cariño, yo he cortado la cebolla esta mañana. Está en la nevera."),
            ("Hombre", "ANTONIO", "[curious] Vale. ¿Y ahora qué hago?"),
            ("Mujer", "LUCIA", "[kind] Ahora [v:fríe las patatas] en la sartén, con mucho aceite. Y cuidado, que el aceite quema mucho. Después las mezclamos con los huevos.")],
  "why": "Ahora tiene que <b>freír las patatas</b>. Ya las ha pelado, y la cebolla la ha cortado su abuela.",
  "img": "R14a_CA1_07_pelar_cortar_freir",
  "prompt": "Panel 1: hands peeling a potato with a small knife. Panel 2: hands cutting an onion on a chopping board. Panel 3: potato slices frying in a frying pan with oil."},
 {"area": "cm", "q": "¿Qué se va a probar la mujer?", "o": ["una falda", "un vestido", "unos vaqueros"], "ok": 1,
  "pres": "Va a escuchar a una mujer que habla con un dependiente en una tienda de ropa.",
  "lines": [("Mujer", "VALENTINA", "[polite] Hola, buenas. Busco una [x:falda] elegante para una boda."),
            ("Hombre", "MARTIN_2", "[helpful] Faldas elegantes ahora no tenemos, lo siento. Pero mire este [v:vestido] azul: es precioso y está rebajado."),
            ("Mujer", "VALENTINA", "[interested] ¡Ah, pues sí, es muy bonito! ¿Dónde está el probador?"),
            ("Hombre", "MARTIN_2", "[friendly] Al fondo, a la derecha. ¿Le traigo también unos [x:vaqueros]?"),
            ("Mujer", "VALENTINA", "[laughs] No, gracias, hoy solo el vestido.")],
  "why": "Se va a probar el <b>vestido</b>. Faldas elegantes no tienen, y los vaqueros no los quiere.",
  "img": "R14a_CA1_08_falda_vestido_vaqueros",
  "prompt": "Panel 1: a skirt on a hanger. Panel 2: a blue dress on a hanger. Panel 3: a pair of folded jeans."},
 {"area": "cm", "q": "¿Cómo paga el hombre?", "o": ["con tarjeta", "con el móvil", "en efectivo"], "ok": 2,
  "pres": "Va a escuchar a un hombre que paga en una tienda.",
  "lines": [("Mujer", "MAYA", "[friendly] Son veintitrés euros con cincuenta. ¿Va a pagar con [x:tarjeta]?"),
            ("Hombre", "EMILIO", "[searching] Sí, a ver... Uy, no la llevo. ¿Puedo pagar con el [x:móvil]?"),
            ("Mujer", "MAYA", "[apologetic] Lo siento, hoy la máquina no funciona. Solo podemos cobrar [v:en efectivo]."),
            ("Hombre", "EMILIO", "[relieved] Bueno, no pasa nada. Aquí tiene un billete de cincuenta. ¿Me da el ticket, por favor?")],
  "why": "Paga <b>en efectivo</b>, con un billete. No lleva la tarjeta y la máquina para el móvil no funciona.",
  "img": "R14a_CA1_09_tarjeta_movil_efectivo",
  "prompt": "Panel 1: a hand paying with a bank card at a card machine on a shop counter. Panel 2: a hand paying with a mobile phone at a card machine. Panel 3: a hand giving banknotes to a shop assistant."},
 {"area": "cm", "q": "¿Dónde compra ahora el pan la señora?", "o": ["en el supermercado", "en la panadería", "en el mercado"], "ok": 1,
  "pres": "Va a escuchar a dos vecinas que se encuentran en la calle.",
  "lines": [("Mujer 1", "SOFIA", "[friendly] Buenos días, Carmen. ¡Cuántas bolsas! ¿Vienes del [x:supermercado]?"),
            ("Mujer 2", "CRISTINA_LAT", "[cheerful] No, ya no compro el pan en el súper. Antes sí, pero ahora voy a la [v:panadería] nueva de la plaza. ¡El pan es buenísimo!"),
            ("Mujer 1", "SOFIA", "[curious] ¿Y la fruta?"),
            ("Mujer 2", "CRISTINA_LAT", "[cheerful] La fruta, en el [x:mercado], como siempre. Es más fresca y más barata. ¡Y los vendedores son muy simpáticos!")],
  "why": "Ahora compra el pan en la <b>panadería</b> nueva. En el súper lo compraba antes, y en el mercado compra la fruta.",
  "img": "R14a_CA1_10_supermercado_panaderia_mercado",
  "prompt": "Panel 1: the entrance of a supermarket with shopping trolleys. Panel 2: a small bakery with loaves of bread in the window. Panel 3: an indoor food market with fruit stalls."},
 {"area": "sa", "q": "¿Dónde se ha hecho daño el chico?", "o": ["en la rodilla", "en el brazo", "en el pie"], "ok": 0,
  "pres": "Va a escuchar a un chico que habla con una enfermera.",
  "lines": [("Mujer", "ESTELA", "[calm] A ver, ¿qué te ha pasado? ¿Te duele el [x:brazo]?"),
            ("Hombre", "ERIK", "[in pain] El brazo no. Me he caído de la bici en el parque y me duele muchísimo la [v:rodilla]."),
            ("Mujer", "ESTELA", "[calm] ¿Y el [x:pie]? ¿Puedes moverlo?"),
            ("Hombre", "ERIK", "[relieved] Sí, el pie está bien, no me duele nada. Es solo la rodilla, y está un poco roja.")],
  "why": "Se ha hecho daño en la <b>rodilla</b>. El brazo y el pie están bien.",
  "img": "R14a_CA1_11_rodilla_brazo_pie",
  "prompt": "Panel 1: a young man sitting and holding his knee in pain. Panel 2: a young man holding his arm in pain. Panel 3: a young man sitting and holding his foot in pain."},
 {"area": "sa", "q": "¿Qué le pasa a la niña?", "o": ["tiene fiebre", "tiene tos", "le duelen los oídos"], "ok": 1,
  "pres": "Va a escuchar a una madre que llama por teléfono al centro de salud.",
  "lines": [("Hombre", "MARTIN_1", "[polite] Centro de salud, buenos días. ¿Qué le pasa a la niña? ¿Tiene [x:fiebre]?"),
            ("Mujer", "CAROLINA", "[worried] No, fiebre no tiene: le he puesto el termómetro esta mañana. Pero [v:tose] mucho, sobre todo por la noche."),
            ("Hombre", "MARTIN_1", "[calm] ¿Y le duelen los [x:oídos]?"),
            ("Mujer", "CAROLINA", "[worried] No, los oídos no. Quería pedir cita con su médica para hoy, si es posible.")],
  "why": "La niña <b>tiene tos</b>: tose mucho por la noche. Fiebre no tiene, y los oídos no le duelen.",
  "img": "R14a_CA1_12_fiebre_tos_oidos",
  "prompt": "Panel 1: a girl in bed with a thermometer in her mouth. Panel 2: a girl coughing with her hand in front of her mouth. Panel 3: a girl holding her ears with a sad face."},
]
# Voces del ultimo modelo (M1): no se repiten aqui. Tampoco las descartadas por Maria (22/10).
VOCES_EVITAR = ["DANIEL_ES", "FIONA", "MARIO", "LYDIA", "SARA_JOVEN", "VOLU", "AITANA", "DANI", "MARINA_ES", "LUIS_VEGA", "SARA_2",
                "SANTIAGO_ES", "TATIANA", "OSCAR", "SERGIO", "BOBBY", "TAMARA", "JAVI_ROJAS", "ENRIQUE", "LINA", "ZABRA", "EVA", "RAFA",
                "DIANA", "DAVID_M2", "RITA", "ALEJANDRO", "DIEGO", "MARINA", "GABRIEL_CO", "JANET", "HUGO", "CLARA", "LUCIA_AR"]

# ------------------------------------------------------------------ DILO DE OTRA FORMA (tarea 2 de la lectura)
# Anuncios de 35-60 palabras. o[0] = la buena (dice lo mismo con otras palabras); una opcion repite palabras del texto
# con otro sentido (el distractor literal: lit = indice de esa opcion).
ANUNCIOS = [
 {"area": "ca", "titulo": "SE ALQUILA PISO · CALLE PINTOR SOROLLA",
  "texto": "Piso de dos dormitorios en la cuarta planta, con ascensor. Es exterior y muy luminoso: el salón da a un parque. Está amueblado, pero no tiene lavadora. Ideal para estudiantes o parejas. No se admiten animales. 650 euros al mes.",
  "q": "El piso...", "o": ["tiene muebles.", "tiene una lavadora nueva.", "acepta perros y gatos."], "lit": 1,
  "why": "Amueblado = tiene muebles. La lavadora sale en el anuncio, pero para decir que no tiene, y no se admiten animales."},
 {"area": "ca", "titulo": "BUSCO COMPAÑERA DE PISO",
  "texto": "Busco chica para compartir un piso en el centro. La habitación es interior, pero muy tranquila. La luz y el agua están incluidas en el precio: 380 euros al mes. Solo se puede fumar en la terraza. Llamar por las tardes a Sonia.",
  "q": "En este piso...", "o": ["no hay que pagar aparte la luz.", "la habitación da a la calle.", "no se puede usar la terraza."], "lit": 2,
  "why": "Incluida en el precio = no la pagas aparte. La habitación es interior (no da a la calle), y la terraza sí se usa: es el sitio para fumar."},
 {"area": "co", "titulo": "RESTAURANTE LA HUERTA · MENÚ DEL DÍA",
  "texto": "Menú del día por 13,50 €: primer plato, segundo plato, pan, bebida y postre o café. Todos los días tenemos un plato vegetariano. Los domingos no hay menú: solo carta. Cocina abierta de 13:00 a 16:00.",
  "q": "En este restaurante...", "o": ["siempre hay un plato sin carne ni pescado.", "el menú del día no incluye el postre.", "los domingos hay menú del día."], "lit": 2,
  "why": "Un plato vegetariano = sin carne ni pescado. El postre (o el café) está incluido, y los domingos solo hay carta."},
 {"area": "co", "titulo": "FRUTERÍA HERMANOS GIL",
  "texto": "Esta semana, naranjas a un euro el kilo y las fresas a mitad de precio. Si gastas más de treinta euros, te llevamos la compra a casa sin pagar nada más. Cerramos los lunes por la tarde.",
  "q": "En la frutería...", "o": ["algunas frutas son más baratas esta semana.", "las naranjas son gratis.", "los lunes no abren."], "lit": 2,
  "why": "A mitad de precio = más barato. Las naranjas cuestan un euro el kilo, y los lunes solo cierran por la tarde."},
 {"area": "cm", "titulo": "ZAPATERÍA PASO A PASO · ¡REBAJAS!",
  "texto": "Todos los zapatos y las botas de invierno, con un 40 % de descuento. Las zapatillas de deporte no tienen descuento. Para cambiar o devolver algo, trae el ticket: tienes un mes.",
  "q": "En la zapatería...", "o": ["sin el ticket no se puede devolver nada.", "las zapatillas de deporte son más baratas.", "las botas cuestan cuarenta euros."], "lit": 2,
  "why": "Hay que traer el ticket para cambiar o devolver. Las zapatillas no tienen descuento, y el cuarenta es el descuento, no el precio."},
 {"area": "cm", "titulo": "MERCADILLO DE ROPA EN LA PLAZA",
  "texto": "El domingo, en la plaza del barrio, mercadillo de ropa de segunda mano. Puedes vender la ropa que ya no usas o cambiarla por otra. Solo ropa limpia y en buen estado. La entrada es gratuita. Los puestos se reservan en el ayuntamiento.",
  "q": "En el mercadillo...", "o": ["se puede cambiar ropa.", "hay que pagar para entrar.", "venden ropa nueva."], "lit": 2,
  "why": "Puedes cambiar tu ropa por otra. La entrada es gratis, y la ropa es de segunda mano: ya la ha usado otra persona."},
 {"area": "sa", "titulo": "CENTRO DE SALUD SAN ANTÓN",
  "texto": "Para pedir cita con su médico, llame por teléfono o use la aplicación del centro. Si tiene fiebre alta, llame antes de venir. Las urgencias están abiertas las 24 horas. Recuerde traer su tarjeta sanitaria.",
  "q": "En el centro de salud...", "o": ["se puede pedir cita con el móvil.", "las urgencias cierran por la noche.", "con fiebre hay que venir sin llamar."], "lit": 2,
  "why": "Con la aplicación = con el móvil. Las urgencias abren las veinticuatro horas, y con fiebre hay que llamar antes."},
 {"area": "sa", "titulo": "FARMACIA DE GUARDIA",
  "texto": "Esta semana, la farmacia de guardia del barrio es la de la calle Mayor, 12. Abre toda la noche. Algunos medicamentos solo se venden con receta. Por la noche, llame al timbre y espere en la puerta.",
  "q": "Por la noche, en esta farmacia...", "o": ["hay que llamar y esperar fuera.", "no venden nada sin receta.", "cierran a las doce."], "lit": 1,
  "why": "Llame al timbre y espere en la puerta = llamar y esperar fuera. Solo ALGUNOS medicamentos necesitan receta, y la farmacia abre toda la noche."},
 {"area": "pe", "titulo": "INTERCAMBIO DE IDIOMAS",
  "texto": "Hola, me llamo Teo y soy de Dublín. Tengo 34 años. Al principio soy un poco tímido, pero luego hablo mucho. Busco a alguien para practicar español dos tardes a la semana; yo te ayudo con tu inglés. Me encanta cocinar y el cine.",
  "q": "Teo...", "o": ["no habla mucho con gente nueva al principio.", "es muy tímido con todo el mundo.", "quiere aprender inglés."], "lit": 1,
  "why": "Al principio es tímido, pero luego habla mucho: con gente nueva, al principio, habla poco. Él quiere practicar español; el inglés lo enseña él."},
 {"area": "pe", "titulo": "SE BUSCA PERSONA PARA ACOMPAÑAR A UNA SEÑORA MAYOR",
  "texto": "Mi madre tiene 85 años y vive sola. Buscamos a una persona alegre y paciente para acompañarla por las mañanas: pasear, hacer la compra y leerle el periódico. No hace falta cocinar. Mejor con experiencia con personas mayores.",
  "q": "La persona que buscan tiene que...", "o": ["ir con la señora a comprar.", "preparar la comida.", "vivir con la señora."], "lit": 2,
  "why": "Hacer la compra con ella = ir con la señora a comprar. No hace falta cocinar, y la señora vive sola."},
]

# ------------------------------------------------------------------ PRACTICA
# 1. ¿Que sobra? (cuatro palabras; o[0] es la que sobra)
P_SOBRA = [
    {"area": "ca", "q": "En la cocina", "o": ["la cama", "la nevera", "el horno", "el microondas"], "why": "La cama está en el dormitorio. La nevera, el horno y el microondas, en la cocina."},
    {"area": "ca", "q": "Las partes del piso", "o": ["el portal", "el salón", "el dormitorio", "el pasillo"], "why": "El portal es del edificio: es la entrada de la calle. Las otras tres son partes de tu piso."},
    {"area": "ca", "q": "Las tareas de casa", "o": ["alquilar", "planchar", "fregar los platos", "sacar la basura"], "why": "Alquilar es lo que haces para tener un piso, no una tarea de casa."},
    {"area": "cm", "q": "Tiendas de comida", "o": ["la librería", "la panadería", "la carnicería", "la pescadería"], "why": "En la librería venden libros. ¡Cuidado: no es la biblioteca!"},
    {"area": "cm", "q": "Para los pies", "o": ["la chaqueta", "los zapatos", "las botas", "las zapatillas"], "why": "La chaqueta es para el cuerpo; las otras tres, para los pies."},
    {"area": "cm", "q": "Para pagar", "o": ["con receta", "en efectivo", "con tarjeta", "con el móvil"], "why": "La receta es del médico. Se paga en efectivo, con tarjeta o con el móvil."},
    {"area": "pe", "q": "La cara", "o": ["la rodilla", "los ojos", "la barba", "el bigote"], "why": "La rodilla es de la pierna."},
    {"area": "pe", "q": "El carácter (ser)", "o": ["cansado", "simpático", "tímido", "trabajador"], "why": "Cansado es cómo estás (estar), no cómo eres: estoy cansado, soy simpático."},
    {"area": "pe", "q": "Cómo estás (estar)", "o": ["alto", "contento", "preocupado", "enfadado"], "why": "Alto es cómo eres (ser). Contento, preocupado y enfadado son estados: estoy contento."},
    {"area": "pe", "q": "La familia de tu pareja", "o": ["el vecino", "el suegro", "la suegra", "el cuñado"], "why": "El vecino vive cerca, pero no es de la familia."},
    {"area": "co", "q": "En el restaurante", "o": ["la receta", "la carta", "la cuenta", "la propina"], "why": "La receta es del médico (o de la cocina). En el restaurante: la carta, la cuenta y la propina."},
    {"area": "co", "q": "Envases y cantidades", "o": ["una talla", "una docena", "medio kilo", "una botella"], "why": "La talla es de la ropa."},
    {"area": "sa", "q": "Síntomas", "o": ["el jarabe", "la fiebre", "la tos", "el dolor"], "why": "El jarabe es la medicina, no el síntoma."},
    {"area": "sa", "q": "Hábitos sanos", "o": ["comer mucho dulce", "dormir bien", "hacer deporte", "beber agua"], "why": "Comer mucho dulce no es un hábito sano."},
]
# 2. El verbo que va con... (o[0] buena; ____ = el verbo)
P_VERBO = [
    {"area": "sa", "q": "Esta tarde voy a ____ cita con el médico.", "o": ["pedir", "poner", "llevar"], "why": "<b>Pedir cita</b> (al médico, a la peluquería...)."},
    {"area": "ca", "q": "Antes de comer, ¿me ayudas a ____ la mesa?", "o": ["poner", "hacer", "llevar"], "why": "<b>Poner la mesa</b>: platos, vasos, cubiertos. Después de comer, quitarla."},
    {"area": "co", "q": "Los sábados ____ la compra en el mercado.", "o": ["hago", "tomo", "llevo"], "why": "<b>Hacer la compra</b>."},
    {"area": "co", "q": "Camarero, ¿me puede ____ la cuenta, por favor?", "o": ["traer", "hacer", "tomar"], "why": "<b>Traer la cuenta</b> (el camarero) / <b>pedir la cuenta</b> (tú)."},
    {"area": "ca", "q": "Por la mañana siempre ____ la cama.", "o": ["hago", "pongo", "tengo"], "why": "<b>Hacer la cama</b>."},
    {"area": "ca", "q": "No queremos comprar un piso: lo vamos a ____.", "o": ["alquilar", "mudar", "compartir"], "why": "<b>Alquilar</b>: pagas cada mes para vivir en él."},
    {"area": "cm", "q": "¿Puedo pagar ____ tarjeta?", "o": ["con", "en", "de"], "why": "<b>Con tarjeta</b>, pero <b>en efectivo</b>."},
    {"area": "sa", "q": "Mi hijo ____ fiebre desde ayer.", "o": ["tiene", "está", "hace"], "why": "<b>Tener fiebre</b>, como tener tos o tener frío."},
    {"area": "sa", "q": "Tiene que ____ una pastilla después de comer.", "o": ["tomar", "beber", "poner"], "why": "<b>Tomar una pastilla</b> (o un jarabe)."},
    {"area": "ca", "q": "Hoy te toca a ti ____ la basura.", "o": ["sacar", "quitar", "abrir"], "why": "<b>Sacar la basura</b>: llevarla al contenedor de la calle."},
    {"area": "ca", "q": "Después de cenar, mi marido ____ los platos.", "o": ["friega", "barre", "plancha"], "why": "<b>Fregar los platos</b>. Barrer es el suelo, y planchar, la ropa."},
    {"area": "ca", "q": "El mes que viene voy a ____ a un piso más grande.", "o": ["mudarme", "moverme", "quedarme"], "why": "<b>Mudarse</b> = cambiar de casa. «Moverse» es otra cosa (ir de un sitio a otro)."},
    {"area": "pe", "q": "Mi hermana y yo nos ____ muy bien.", "o": ["llevamos", "tenemos", "estamos"], "why": "<b>Llevarse bien / mal</b> con alguien."},
    {"area": "co", "q": "Para el sábado, ¿____ una mesa para cuatro?", "o": ["reservamos", "compramos", "alquilamos"], "why": "<b>Reservar una mesa</b> en un restaurante."},
]
# 4. ¿Bien o mal? ok 0 = bien, 1 = mal. det = id del aviso del detector que la ve (si es un calco que se puede ver)
E_BIENMAL = [
    {"q": "Vivo en el tercer suelo.", "ok": 1, "fix": "Vivo en la tercera <b>planta</b>.", "why": "El suelo es donde pisas. El número del piso: la planta (o el piso).", "det": "suelo_planta"},
    {"q": "¿Puedo pagar con efectivo?", "ok": 1, "fix": "¿Puedo pagar <b>en efectivo</b>?", "why": "En efectivo, pero con tarjeta.", "det": "con_efectivo"},
    {"q": "El médico me ha dado una prescripción.", "ok": 1, "fix": "El médico me ha dado una <b>receta</b>.", "why": "El papel del médico para comprar medicinas es la receta.", "det": "prescripcion"},
    {"q": "El mes que viene voy a mover a un piso más grande.", "ok": 1, "fix": "El mes que viene <b>me voy a mudar</b> a un piso más grande.", "why": "Cambiar de casa = mudarse.", "det": "mover_piso"},
    {"q": "Hoy estoy mucha hambre.", "ok": 1, "fix": "Hoy <b>tengo</b> mucha hambre.", "why": "Hambre, sed, sueño, frío, calor y miedo van con tener.", "det": "estoy_hambre"},
    {"q": "Después del trabajo soy muy cansada.", "ok": 1, "fix": "Después del trabajo <b>estoy</b> muy cansada.", "why": "Cansado es un estado: estar.", "det": "soy_estado"},
    {"q": "Me duele mi cabeza.", "ok": 1, "fix": "Me duele <b>la</b> cabeza.", "why": "Con el cuerpo, el artículo: me duele la cabeza.", "det": "duele_mi"},
    {"q": "¿Qué número de camiseta usa?", "ok": 1, "fix": "¿Qué <b>talla</b> de camiseta usa?", "why": "La ropa tiene talla; los zapatos, número.", "det": "numero_ropa"},
    {"q": "Camarero, ¿nos trae la factura, por favor?", "ok": 1, "fix": "Camarero, ¿nos trae <b>la cuenta</b>, por favor?", "why": "En el bar o el restaurante se pide la cuenta.", "det": "factura_bar"},
    {"q": "Compro los libros en la biblioteca.", "ok": 1, "fix": "Compro los libros en la <b>librería</b>.", "why": "En la librería compras; en la biblioteca te los prestan.", "det": "biblioteca_comprar"},
    {"q": "Mi suegra es la madre de mi hermano.", "ok": 1, "fix": "Mi suegra es la madre de <b>mi marido</b> (o de mi mujer).", "why": "La suegra es la madre de tu pareja. La madre de tu hermano es tu madre.", "det": None},
    {"q": "Tengo frío: voy a ponerme el abrigo.", "ok": 0, "fix": "", "why": "Correcto: tener frío.", "det": None},
    {"q": "En el mercado siempre pago en efectivo.", "ok": 0, "fix": "", "why": "Correcto: pagar en efectivo.", "det": None},
    {"q": "Mi hermano es calvo y lleva barba.", "ok": 0, "fix": "", "why": "Correcto: ser calvo, llevar barba.", "det": None},
    {"q": "¿Me trae la cuenta, por favor?", "ok": 0, "fix": "", "why": "Correcto: así se pide la cuenta.", "det": None},
    {"q": "Esta falda me queda pequeña: ¿tiene una talla más grande?", "ok": 0, "fix": "", "why": "Correcto: quedar pequeño, una talla más.", "det": None},
]

# 3. Textos con huecos: motivos (area, explicacion, respuestas buenas posibles en minusculas)
MOTIVOS = {
    "planta": ("ca", "El número del piso es la <b>planta</b>; el suelo es donde pisas.", ["planta"]),
    "edificio": ("ca", "Para no subir andando: el <b>ascensor</b>.", ["ascensor"]),
    "luz": ("ca", "Mucha luz = <b>luminoso</b>.", ["luminoso"]),
    "muebles": ("ca", "Con muebles = <b>amueblado</b>.", ["amueblado"]),
    "mueble": ("ca", "Los libros van en la <b>estantería</b>.", ["estantería"]),
    "compartir": ("ca", "Vivir con otra persona en el mismo piso: <b>compartir</b> piso.", ["comparto"]),
    "caracter": ("pe", "Siempre se ríe y habla con todos: es <b>simpático</b> (no tímido ni serio).", ["simpático"]),
    "llevar": ("pe", "La barba, las gafas, la ropa: <b>llevar</b>.", ["lleva"]),
    "tienda": ("cm", "Cada cosa en su tienda: la fruta en la <b>frutería</b>, el pescado en la <b>pescadería</b>.", ["frutería", "pescadería"]),
    "cantidad": ("co", "Los huevos se cuentan por <b>docenas</b>; el queso, por <b>kilos</b>.", ["una docena", "kilo"]),
    "pagar": ("cm", "Con billetes y monedas: <b>en efectivo</b>.", ["en efectivo"]),
    "cuenta": ("co", "En el bar se pide <b>la cuenta</b> (la receta es del médico).", ["cuenta"]),
    "cocina": ("co", "Quitar la piel = <b>pelar</b>.", ["pelo"]),
    "sentirse": ("sa", "Cuando estás enfermo: me encuentro <b>mal</b>.", ["mal"]),
    "sintoma": ("sa", "Treinta y ocho grados: <b>fiebre</b>.", ["fiebre"]),
    "cuerpo": ("sa", "Lo que duele es una parte del cuerpo: la <b>garganta</b>.", ["garganta"]),
    "cita": ("sa", "Para ir al médico, primero <b>pides cita</b>.", ["pedido cita"]),
    "receta": ("sa", "El papel del médico para comprar el jarabe: la <b>receta</b>.", ["receta"]),
    "farmacia": ("sa", "Las medicinas se compran en la <b>farmacia</b>.", ["farmacia"]),
    "descansar": ("sa", "Con fiebre, a la cama a <b>descansar</b>.", ["descansar"]),
    "edad": ("pe", "De unos setenta años = <b>mayor</b>; de unos veinte = <b>joven</b>.", ["mayor", "joven"]),
    "pelo": ("pe", "Sin pelo = <b>calvo</b>; con el pelo así = <b>rizado</b>.", ["calvo", "rizado"]),
    "ropa": ("cm", "Unos... = una prenda en plural: <b>unos vaqueros</b>.", ["vaqueros"]),
    "estado": ("pe", "Se ríe: está <b>contenta</b>.", ["contenta"]),
    "familia": ("pe", "La hija de tu hijo es tu <b>nieta</b>.", ["nieta"]),
}
TEXTOS = [
    {"id": "piso", "tipo": "Escritura · tarea 1 · correo a una amiga", "titulo": "¡Ya tengo piso!",
     "texto": "¡Hola, Alicia!<br>¡Por fin tengo piso! Está en la cuarta [[planta|suelo|parte#planta]], pero no pasa nada, porque hay [[ascensor|escalera|portal#edificio]]. "
              "Es pequeño, pero muy [[luminoso|oscuro|interior#luz]]: el salón tiene un balcón grande a la calle. Está [[amueblado|cerrado|roto#muebles]]: ya tiene sofá, mesa y camas. "
              "Solo he comprado una [[estantería|nevera|lavadora#mueble]] para mis libros. [[Comparto|Mudo|Pongo#compartir]] el piso con Óscar, un chico de Valencia muy "
              "[[simpático|tímido|serio#caracter]]: siempre se ríe y habla con todos. Es alto, [[lleva|pone|está#llevar]] barba y canta en la ducha. ¿Vienes a verme?<br>Un beso,<br>Marta"},
    {"id": "mercado", "tipo": "Escritura · tarea 2 · blog", "titulo": "El mercado de los sábados",
     "texto": "Los sábados por la mañana hago la compra en el mercado de mi barrio. Primero voy a la [[frutería|carnicería|librería#tienda]] de Toñi y compro un kilo de naranjas. "
              "Luego compro [[una docena|una botella|una lata#cantidad]] de huevos y medio [[kilo|paquete|litro#cantidad]] de queso. En la [[pescadería|panadería|zapatería#tienda]] compro sardinas para la cena. "
              "En el mercado siempre pago [[en efectivo|con efectivo|en tarjeta#pagar]], porque en algunos puestos no se puede pagar con tarjeta. Al final tomo un café en el bar y el camarero me trae la "
              "[[cuenta|factura|receta#cuenta]]. Por la tarde cocino: primero [[pelo|corto|frío#cocina]] las patatas (les quito la piel) y después preparo una tortilla."},
    {"id": "enfermo", "tipo": "Escritura · tarea 1 · mensaje a un amigo", "titulo": "Mañana no puedo ir",
     "texto": "¡Hola, Rubén!<br>Perdona, pero mañana no puedo ir al cine. Me encuentro [[mal|bien|mejor#sentirse]]: tengo treinta y ocho de [[fiebre|tos|dolor#sintoma]] "
              "y me duele mucho la [[garganta|gripe|receta#cuerpo]]. Esta mañana he [[pedido cita|hecho cita|tomado cita#cita]] en el centro de salud y la médica me ha dado una "
              "[[receta|carta|cuenta#receta]] para un jarabe. Ahora voy a la [[farmacia|librería|panadería#farmacia]] y después, a la cama a [[descansar|bailar|correr#descansar]]. "
              "¿Vamos al cine el sábado que viene?<br>Un abrazo,<br>Hugo"},
    {"id": "foto", "tipo": "Oral · tarea 2 · describir una foto", "titulo": "En la foto hay...",
     "texto": "En la foto hay dos personas. A la izquierda hay un señor [[mayor|joven|nuevo#edad]], de unos setenta años. Es [[calvo|rubio|moreno#pelo]]: no tiene pelo. "
              "Lleva una chaqueta marrón y unos [[vaqueros|vestido|falda#ropa]]. A la derecha hay una chica [[joven|mayor|vieja#edad]], de unos veinte años. "
              "Tiene el pelo [[rizado|calvo|alto#pelo]] y [[lleva|es|está#llevar]] un vestido de flores. Parece [[contenta|cansada|enferma#estado]], porque se ríe. "
              "Creo que son abuelo y [[nieta|sobrina|suegra#familia]]: la chica es la hija de su hijo."},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
# pautas: (texto, [areas que ayudan]); las areas son las de AREAS
LAMINAS = [
    {"id": "nacho", "tarea": "Tarea 1 · correo a un amigo", "palabras": [60, 70], "trato": "tú",
     "intro": "Ha recibido este mensaje de su amigo Nacho:",
     "mensaje": "¡Hola! ¡Tengo trabajo en tu ciudad! Me mudo el mes que viene, pero no conozco nada. ¿Dónde haces tú la compra? ¿Hay tiendas de ropa baratas? ¿Y qué hago si me pongo enfermo? Escríbeme pronto. Un abrazo, Nacho",
     "consigna": "Escriba un correo a Nacho. En él tiene que:",
     "pautas": [("saludarle y decirle qué le parece la noticia;", ["pe"]),
                ("recomendarle dónde hacer la compra y qué comprar allí;", ["co", "cm"]),
                ("explicarle dónde puede comprar ropa y cómo son los precios;", ["cm"]),
                ("decirle qué tiene que hacer si se pone enfermo;", ["sa"]),
                ("invitarle a cenar en su casa, decirle qué va a cocinar y despedirse.", ["co", "ca"])]},
    {"id": "casa", "tarea": "Tarea 2 · texto para una revista", "palabras": [70, 80], "trato": "",
     "intro": "Una revista para estudiantes de español busca textos sobre este tema:",
     "mensaje": "«Mi casa: antes y ahora»",
     "consigna": "Escriba un texto para la revista. Hable de:",
     "pautas": [("cómo era la casa donde vivía de niño o de niña;", ["ca"]),
                ("con quién vivía y cómo era esa persona;", ["pe"]),
                ("cómo es su casa ahora: las partes y los muebles;", ["ca"]),
                ("qué tareas de la casa hace usted y cuáles no le gustan;", ["ca"]),
                ("qué quiere cambiar en su casa y por qué.", ["ca"])]},
]

# ------------------------------------------------------------------ DETECTOR (texto sin tildes, en minusculas)
# s = frase a frase (como en la pagina) · x = el texto entero. t: r = rojo (error seguro) · a = ambar (mira esto)
DETECTOR = [
    {"id": "suelo_planta", "t": "r", "sc": "s", "re": r"\b(?:primer|segundo|tercer|cuarto|quinto|sexto|septimo|octavo|ultimo)\s+suelo\b",
     "msg": "El número del piso es la <b>planta</b>: vivo en la tercera planta. El <i>suelo</i> es donde pisas."},
    {"id": "con_efectivo", "t": "r", "sc": "s", "re": r"\b(?:con (?:el )?efectivo|en (?:la )?tarjeta)\b",
     "msg": "Se paga <b>en efectivo</b> y <b>con tarjeta</b>."},
    {"id": "prescripcion", "t": "r", "sc": "s", "re": r"\bprescripcion(?:es)?\b",
     "msg": "El papel del médico para comprar medicinas es la <b>receta</b>."},
    {"id": "mover_piso", "t": "r", "sc": "s",
     "re": r"\b(?:mover|moverme|moverte|moverse|movernos|muevo|mueves|mueve|movemos|moveis|mueven|movi|moviste|movio|movimos|movieron)\s+(?:a|de)\s+(?:(?:un|una|otro|otra|mi|tu|su|nuestro|nuestra|el|la)\s+)?(?:piso|casa|ciudad|apartamento|barrio|pais)\b",
     "msg": "Cambiar de casa es <b>mudarse</b>: me mudo a un piso nuevo. <i>Moverse</i> es ir de un sitio a otro."},
    {"id": "estoy_hambre", "t": "r", "sc": "s",
     "re": r"\b(?:(?:estoy|estas|esta|estamos|estais|estan|estaba|estabas|estabamos|estaban|estuve|estuvo)\s+(?:con\s+)?(?:muchas?\s+|un poco de\s+)?(?:hambre|sed|sueno|miedo)|(?:estoy|estamos|estuve|estuvimos)\s+(?:mucho\s+|muy\s+|un poco de\s+)?(?:frio|calor))\b",
     "msg": "Hambre, sed, sueño, miedo, frío y calor van con <b>tener</b>: tengo hambre, tengo frío."},
    {"id": "soy_estado", "t": "r", "sc": "s",
     "re": r"\b(?:soy|eres|somos|sois)\s+(?:muy\s+|un poco\s+|bastante\s+)?(?:cansad[oa]s?|enfadad[oa]s?|preocupad[oa]s?|content[oa]s?)\b",
     "msg": "Cansado, enfadado, preocupado y contento son estados: van con <b>estar</b> (estoy cansada)."},
    {"id": "es_estado", "t": "a", "sc": "s",
     "re": r"\b(?:es|son|era|eran|fue)\s+(?:muy\s+|un poco\s+|bastante\s+)?(?:enfadad[oa]s?|preocupad[oa]s?|content[oa]s?)\b",
     "msg": "Si hablas de cómo está una persona ahora, es <b>estar</b>: está preocupada, está contento."},
    {"id": "duele_mi", "t": "r", "sc": "s",
     "re": r"\b(?:me|te|le|nos|os|les)\s+(?:duele|duelen|dolia|dolian|dolio|dolieron)\s+(?:mucho\s+|un poco\s+)?(?:mi|mis|tu|tus|su|sus|nuestr[oa]s?)\b",
     "msg": "Con las partes del cuerpo, el artículo: <b>me duele la cabeza</b> (no «mi cabeza»)."},
    {"id": "numero_ropa", "t": "r", "sc": "s",
     "re": r"\bnumero\s+(?:de|del)\s+(?:la\s+|el\s+|los\s+)?(?:camiseta|camisa|pantalon|pantalones|vestido|falda|chaqueta|jersey|abrigo|vaqueros)\b",
     "msg": "La ropa tiene <b>talla</b>; los zapatos, número."},
    {"id": "factura_bar", "t": "a", "sc": "s",
     "re": r"^(?=.*\b(?:camarer[oa]|restaurante|bar|menu|cenar|cena|comer|comida)\b).*\bfactura\b",
     "msg": "En el bar o el restaurante se pide <b>la cuenta</b>."},
    {"id": "biblioteca_comprar", "t": "a", "sc": "s", "re": r"\bcompr\w*\b[^.!?]{0,40}\bbiblioteca\b",
     "msg": "¿Compras en la biblioteca? Se compra en la <b>librería</b>; en la biblioteca te prestan los libros."},
    {"id": "cosa_rep", "t": "a", "sc": "x", "re": r"^(?=(?:(?:.|\n)*?\bcosas?\b){3})",
     "msg": "Has escrito <b>cosa</b> tres veces o más. Usa el nombre de verdad: la estantería, el abrigo, el jarabe..."},
    {"id": "bonito_rep", "t": "a", "sc": "x", "re": r"^(?=(?:(?:.|\n)*?\bbonit[oa]s?\b){3})",
     "msg": "Has escrito <b>bonito</b> tres veces o más. Varía: luminoso, cómodo, tranquilo, precioso, rico..."},
    {"id": "grande_rep", "t": "a", "sc": "x", "re": r"^(?=(?:(?:.|\n)*?\bgrandes?\b){3})",
     "msg": "Has escrito <b>grande</b> tres veces o más. Varía: enorme, luminoso, cómodo, alto, mayor..."},
]
# Errores de vocabulario que el detector tiene que ver (ids)
REQ = ["suelo_planta", "con_efectivo", "prescripcion", "mover_piso", "estoy_hambre", "soy_estado", "duele_mi", "numero_ropa",
       "factura_bar", "biblioteca_comprar"]
DETECTOR_PRUEBAS = [
    ("Vivo en el tercer suelo.", ["suelo_planta"]),
    ("¿Puedo pagar con efectivo?", ["con_efectivo"]),
    ("Pago en tarjeta.", ["con_efectivo"]),
    ("El médico me ha dado una prescripción.", ["prescripcion"]),
    ("El mes que viene voy a mover a un piso más grande.", ["mover_piso"]),
    ("Me muevo de casa en junio.", ["mover_piso"]),
    ("Hoy estoy mucha hambre.", ["estoy_hambre"]),
    ("En invierno estoy mucho frío.", ["estoy_hambre"]),
    ("Después del trabajo soy muy cansada.", ["soy_estado"]),
    ("Mi madre es muy preocupada por mí.", ["es_estado"]),
    ("Me duele mi cabeza.", ["duele_mi"]),
    ("¿Qué número de camiseta usa?", ["numero_ropa"]),
    ("Camarero, ¿nos trae la factura, por favor?", ["factura_bar"]),
    ("Compro los libros en la biblioteca.", ["biblioteca_comprar"]),
    ("Tengo muchas cosas en el salón, cosas viejas y cosas nuevas.", ["cosa_rep"]),
    ("Es una casa bonita, con un jardín bonito y una cocina bonita.", ["bonito_rep"]),
    ("Es grande, tiene una terraza grande y un salón grande.", ["grande_rep"]),
    ("Vivo en la tercera planta.", []),
    ("El suelo de la cocina es blanco.", []),
    ("En el mercado siempre pago en efectivo.", []),
    ("Pagué con tarjeta.", []),
    ("Me muevo en bici por la ciudad.", []),
    ("Tengo mucha hambre.", []),
    ("El café está frío.", []),
    ("Hoy estoy muy cansada.", []),
    ("Es un trabajo cansado.", []),
    ("Mi hermano es muy nervioso.", []),
    ("Me duele la cabeza.", []),
    ("¿Qué talla usa? ¿Y qué número de zapatos?", []),
    ("Pedimos la cuenta al camarero.", []),
    ("La factura de la luz llega cada mes.", []),
    ("Saco libros de la biblioteca y compro novelas en la librería.", []),
    ("Le duele mucho la rodilla.", []),
    ("Mi madre está muy contenta.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL (la escena en un minuto)
# Fotos 7-12 del taller de la foto (M4T2_fotoN.jpg, ya en WordPress). Tres grupos de palabras por foto.
ORAL = [
    {"id": 7, "titulo": "Antes de salir de casa", "desc": "Una madre mira la hora con las llaves en la mano; su hijo busca un zapato en el suelo y su hija espera junto a la puerta con un paraguas.",
     "grupos": [("Las personas y la ropa", ["la madre", "el hijo", "la hija", "el abrigo", "la bufanda", "el gorro de lana", "la mochila", "el zapato"]),
                ("El lugar y las cosas", ["el recibidor", "el perchero", "el espejo", "la puerta", "las llaves", "el móvil", "el paraguas"]),
                ("Qué hacen", ["mirar la hora", "buscar", "esperar", "tener prisa", "llegar tarde", "salir de casa"])]},
    {"id": 8, "titulo": "Hacer deporte", "desc": "Cuatro amigos se dan la mano en la red al final de un partido de pádel; uno se toca la rodilla y otro se seca con una toalla.",
     "grupos": [("Las personas y la ropa", ["las amigas", "los amigos", "la visera", "las gafas de sol", "la barba", "la camiseta", "la toalla"]),
                ("El lugar y las cosas", ["la pista", "la red", "la pala", "la pelota", "el banco", "la botella de agua", "la mochila"]),
                ("Qué hacen", ["jugar", "darse la mano", "ganar", "perder", "secarse", "doler la rodilla"])]},
    {"id": 9, "titulo": "De compras", "desc": "En la caja de un supermercado, un señor mayor busca la cartera y su mujer mete la compra en un carro; la cajera espera y sonríe.",
     "grupos": [("Las personas y la ropa", ["el señor", "la señora", "la cajera", "calvo", "las gafas", "la chaqueta", "el abrigo"]),
                ("El lugar y las cosas", ["el supermercado", "la caja", "el pan", "la leche", "los huevos", "la fruta", "el carro de la compra", "la cesta"]),
                ("Qué hacen", ["hacer la compra", "pagar", "buscar la cartera", "pagar con el móvil", "esperar", "sonreír"])]},
    {"id": 10, "titulo": "Clases para adultos", "desc": "En una clase de baile, el profesor enseña un paso; una pareja mayor baila muy bien y un chico pisa a su compañera.",
     "grupos": [("Las personas y la ropa", ["el profesor", "la pareja", "el vestido", "la camisa", "las gafas", "el pelo largo", "la camiseta de rayas", "los vaqueros", "las zapatillas"]),
                ("El lugar y las cosas", ["la sala", "el espejo", "el suelo", "el altavoz", "las sillas", "los abrigos", "los bolsos"]),
                ("Qué hacen", ["bailar", "enseñar", "pisar", "reírse", "equivocarse"])]},
    {"id": 11, "titulo": "Ver la televisión", "desc": "Tres amigos ven un partido de fútbol en el salón: dos saltan y gritan ¡gol! y el otro se tapa la cara; las palomitas se caen al suelo.",
     "grupos": [("Las personas y la ropa", ["los amigos", "la camiseta de fútbol", "la barba", "la gorra", "las gafas", "la sudadera"]),
                ("El lugar y las cosas", ["el salón", "el sofá", "los cojines", "la tele", "la mesa", "la pizza", "las patatas fritas", "las latas", "las palomitas"]),
                ("Qué hacen", ["ver un partido", "saltar", "gritar", "marcar un gol", "taparse la cara"])]},
    {"id": 12, "titulo": "Regalos", "desc": "En una cafetería, una mujer abre un regalo de cumpleaños (una bufanda) y su amiga la mira; el camarero trae dos cafés y una tarta con una vela.",
     "grupos": [("Las personas y la ropa", ["las amigas", "el camarero", "el pelo rizado", "el jersey", "las gafas", "la chaqueta", "el delantal"]),
                ("El lugar y las cosas", ["la cafetería", "la mesa", "la ventana", "las plantas", "el regalo", "la bufanda", "la tarta", "la vela", "las tazas"]),
                ("Qué hacen", ["abrir un regalo", "sonreír", "traer", "emocionarse", "celebrar el cumpleaños"])]},
]
