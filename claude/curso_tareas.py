# -*- coding: utf-8 -*-
# TAREAS DE ESCRITURA DEL CURSO DE PREPARACION DELE A2 QUE CONOCE EL CORRECTOR DE LA PROFESORA
# (modelos completos y laminas de "Ahora tu" de los talleres de escritura y de las fichas de remedio).
# Lo usa patch_corrector.py. Cada modelo nuevo (M7, M1...) se anade aqui con su clave A2-Mxx.
# "keys": nombres con los que la pieza copia el texto (sirven para reconocer la lamina en lo que pega la profesora).
# "pz": pieza del curso de la que sale la lamina (para el desplegable).
# 23/10/2026 (chat de la R14a): FICHAS con los nombres de archivo reales de R10 y R14a y los titulos de R08, R10 y R13;
# FICHAS_LISTAS con R08, R10, R13 y R14; laminas de "Ahora tu" de R08, R10, R13 y R14a en FICHAS_AT.
# 23/10/2026 noche (chat de la R14b): ficha R14b (vocabulario de fuera de casa) en FICHAS y FICHAS_LISTAS, y sus dos laminas.
# 24/10/2026: BANCO con las 20 laminas del banco de escritura (M3-6).

def t1(instr, inp, lead, pautas):
    return {"instr": instr, "input": inp, "lead": lead, "pautas": pautas, "min": 60, "max": 70}

def t2(intro, pautas, photos=None, ficha=None, intro2=""):
    return {"intro": intro, "photos": photos or [], "ficha": ficha or [], "intro2": intro2, "pautas": pautas}

def solo(clave, nombre, pz, keys, tarea, data):
    e = {"id": clave, "nombre": nombre, "pz": pz, "keys": keys, "solo": tarea}
    if tarea == 1:
        e["t1"] = data
        e["t2"] = {"instr": "", "op1": None, "op2": None, "min": 70, "max": 80}
    else:
        e["t1"] = None
        e["t2"] = {"instr": "", "op1": data, "op2": None, "min": 70, "max": 80}
    return e

T2_INSTR = "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos."

# ------------------------------------------------------------------ MODELOS COMPLETOS
MODELOS = [
 {"id": "A2-M06", "nombre": "Modelo 6 · como el examen", "pz": "Modelos completos",
  "t1": t1("Su amigo Pablo, que vive en otra ciudad, le ha escrito este correo.",
           ["¡Hola! ¿Qué tal todo? ¡Por fin tengo vacaciones! Voy a tu ciudad del 3 al 6 de diciembre. ¿Qué podemos hacer esos días? ¿Puedo dormir en tu casa o busco un hotel? Cuéntame también qué tal estás tú.", "Un abrazo, Pablo"],
           "Conteste a Pablo. En el correo tiene que:",
           ["saludar y decirle qué le parece su visita;", "contarle qué ha hecho usted estas últimas semanas;", "proponerle dos planes para esos días y explicar por qué;", "contestar si puede dormir en su casa y por qué;", "hacerle dos preguntas sobre su viaje y despedirse."]),
  "t2": {"instr": T2_INSTR, "min": 70, "max": 80,
         "op1": t2("Una revista para estudiantes de español busca textos de sus lectores con este título: «El mejor consejo que me han dado». Escriba su texto. Hable de:",
                   ["quién le dio el consejo y cómo es esa persona;", "cuándo fue y qué le pasaba a usted en ese momento;", "qué le dijo exactamente;", "qué hizo usted después;", "por qué piensa que fue un buen consejo."]),
         "op2": t2("Bruno tiene diecisiete años y el verano pasado trabajó en una heladería. Aquí tiene tres fotos de su primer día.",
                   ["qué aprendió Bruno por la mañana;", "qué pasó por la tarde y cómo se sintió;", "cómo terminó el día y qué piensa usted de la jefa."],
                   photos=["10:00. La jefa, una mujer de unos cincuenta años con delantal, le enseña a Bruno a servir helados. Bruno escucha con atención.",
                           "18:00. Hay una cola muy larga de clientes. A Bruno se le cae una bandeja con tres copas de helado.",
                           "22:00. La heladería está cerrada. La jefa y Bruno toman un helado en la terraza y se ríen."],
                   intro2="Escriba un texto sobre el primer día de Bruno. Hable de:")}},
]

# ------------------------------------------------------------------ TALLER DE ESCRITURA (M3): "Ahora tú"
KIT = "Kit de frases · "
PAU = "Las pautas · "
NUE = "Nueva · "
TALLERES = [
 # --- kit de frases (M3-1)
 solo("A2-K-inf", "Kit de frases · Correo a un amigo (Dani, excursión en bici)", "Taller de escritura", [KIT + "Correo a un amigo"], 1,
      t1("Un amigo le escribe para invitarle a una excursión.",
         ["¡Hola! ¿Qué tal todo? El domingo vamos a hacer una ruta en bici por el río con unos amigos y después comemos en el campo. ¿Te vienes? Salimos a las nueve de la plaza. ¡Va a ser genial!", "Un abrazo, Dani"],
         "Conteste a su amigo. En el correo tiene que:",
         ["saludar y agradecer la invitación;", "decir que no puede ir y explicar por qué;", "disculparse;", "proponer otro plan para otro día;", "despedirse."])),
 solo("A2-K-for", "Kit de frases · Correo de usted (gimnasio Aquaforma)", "Taller de escritura", [KIT + "Correo de usted"], 1,
      t1("Usted quiere apuntarse a un gimnasio y ha visto este anuncio.",
         ["GIMNASIO AQUAFORMA", "Piscina, sala de máquinas y clases de yoga y pilates.", "Abierto de lunes a sábado.", "¡Este mes, la primera semana es gratis!", "Información: Sr. Navarro (info@aquaforma.es)"],
         "Escriba un correo al señor Navarro. En el correo tiene que:",
         ["saludar;", "presentarse y decir por qué escribe;", "preguntar por los horarios de las clases y el precio;", "preguntar por otra cosa (la piscina, qué hay que llevar...);", "agradecer y despedirse."])),
 solo("A2-K-blog", "Kit de frases · Blog (una comida o una cena especial)", "Taller de escritura", [KIT + "Blog o diario", KIT + "Blog ("], 2,
      t2("Escriba una entrada en su blog sobre una comida o una cena especial. Hable de:",
         ["cuándo fue, dónde y con quién;", "qué celebraban o por qué era especial;", "qué comieron y qué hicieron;", "qué le gustó más y qué no le gustó;", "si quiere repetir y por qué."])),
 solo("A2-K-bio", "Kit de frases · Biografía (Tomás Ferrer, biólogo)", "Taller de escritura", [KIT + "Biografía"], 2,
      t2("Tomás Ferrer es biólogo. Aquí tiene algunas fotos y datos sobre su vida.",
         ["dónde y cuándo nació y cómo era de niño;", "qué estudió y a qué se dedicó;", "qué hace ahora y qué ha cambiado en su vida."],
         photos=["Un niño de unos diez años, con gafas de bucear, en una playa con rocas.", "Un hombre joven con barba trabaja en un barco grande, en medio del mar.", "El mismo hombre, hoy, con el pelo gris, enseña a bucear a un grupo de niños en una piscina."],
         ficha=["Nació en Palma en 1972.", "De niño: muy deportista; le encanta el mar.", "1990: empieza a estudiar Biología en Barcelona.", "1996-2010: trabaja en un barco de investigación; viaja por todo el mundo.", "2011: vuelve a Palma y abre una escuela de buceo.", "Hoy: enseña a bucear a niños y adultos; ya no viaja tanto."],
         intro2="Escriba un texto sobre Tomás. Hable de:")),
 solo("A2-K-fotos", "Kit de frases · Con fotos (curso de cocina)", "Taller de escritura", [KIT + "Con fotos", KIT + "Texto con fotos (curso de cocina"], 2,
      t2("El mes pasado usted hizo un curso de cocina con unos compañeros de trabajo. Aquí tiene tres fotos de ese día.",
         ["dónde estaba, con quién y qué hicieron por la mañana;", "qué pasó a mediodía;", "cómo terminó el día y qué le pareció el curso."],
         photos=["Por la mañana. Usted y cinco compañeros, con delantal, escuchan a un cocinero con gorro blanco en una cocina grande.", "A mediodía. A usted se le quema la tortilla: hay humo en la cocina y sus compañeros se ríen.", "Por la tarde. Todos comen en una mesa larga lo que han cocinado; el cocinero les da un diploma."],
         intro2="Escriba un texto sobre ese día. Hable de:")),
 # --- las pautas como lista de control (M3-2)
 solo("A2-P-a1", "Las pautas · Correo a una amiga (Paula, día sin coches)", "Taller de escritura", [PAU + "Correo a una amiga"], 1,
      t1("Una amiga le escribe para proponerle un plan.",
         ["¡Hola! ¿Cómo estás? El domingo es el día sin coches en la ciudad y hay actividades en el parque: conciertos, juegos, comida... ¿Te vienes? Podemos ir en bici. ¿Tienes bici? Si no, yo te dejo la de mi hermano.", "Un beso, Paula"],
         "Conteste a su amiga. En el correo tiene que:",
         ["saludar;", "decir si quiere ir y qué actividad le interesa más;", "responder a su pregunta sobre la bici;", "proponer una hora y un lugar para quedar;", "despedirse."])),
 solo("A2-P-a2", "Las pautas · Correo de usted (curso de fotografía La Lonja)", "Taller de escritura", [PAU + "Correo de usted"], 1,
      t1("Usted ha visto este anuncio y quiere más información.",
         ["CURSO DE FOTOGRAFÍA PARA PRINCIPIANTES", "Centro cultural La Lonja. Grupos de mañana y de tarde.", "Salidas a fotografiar la ciudad los sábados.", "Información: Sr. Morales (cursos@lalonja.es)"],
         "Escriba un correo al señor Morales. En el correo tiene que:",
         ["saludar;", "presentarse y explicar por qué le interesa el curso;", "preguntar por el precio y la duración del curso;", "preguntar si necesita una cámara profesional;", "agradecer y despedirse."])),
 solo("A2-P-a3", "Las pautas · Revista (mi lugar favorito de la ciudad)", "Taller de escritura", [PAU + "Texto para una revista", PAU + "Revista ("], 2,
      t2("Una revista busca textos de sus lectores sobre «Mi lugar favorito de la ciudad». Hable de:",
         ["qué lugar es y dónde está;", "cómo es;", "cuándo va y con quién;", "qué hace allí;", "por qué es especial para usted."])),
 solo("A2-P-a4", "Las pautas · Texto con fotos (boda de una prima)", "Taller de escritura", [PAU + "Texto con fotos"], 2,
      t2("El verano pasado usted fue a la boda de una prima en un pueblo. Aquí tiene tres fotos de ese día.",
         ["qué problema tuvo por la mañana y qué hizo;", "qué pasó cuando llegó a la boda;", "cómo fue la fiesta y cómo se sintió."],
         photos=["Por la mañana. Usted, con ropa de fiesta, cambia una rueda del coche en una carretera; un amigo mira el reloj.", "A mediodía. Usted llega a la iglesia cuando los novios ya salen; todos les tiran arroz.", "Por la noche. Usted baila con la abuela de la novia en el banquete; todos aplauden."],
         intro2="Escriba un texto sobre ese día. Hable de:")),
 # --- textos modelo (M3-5): laminas nuevas
 solo("A2-N-n1", "Textos modelo · Correo a una amiga (Irene aprende tu idioma)", "Taller de escritura", [NUE + "Correo a una amiga"], 1,
      t1("Una amiga le escribe porque quiere aprender su idioma.",
         ["¡Hola! ¿Cómo estás? Tengo una noticia: he empezado a estudiar tu idioma. ¡Es difícil! Tú aprendiste español muy rápido. ¿Qué hiciste? ¿Me das algún consejo?", "Un beso, Irene"],
         "Conteste a su amiga. En el correo tiene que:",
         ["saludar;", "contar cómo aprendió usted español y qué le ayudó más;", "darle dos consejos;", "proponerle quedar para practicar;", "despedirse."])),
 solo("A2-N-n2", "Textos modelo · Correo de usted (voluntarios de la fiesta del barrio)", "Taller de escritura", [NUE + "Correo de usted"], 1,
      t1("Usted ha visto este anuncio en su barrio.",
         ["FIESTA DEL BARRIO · SE BUSCAN VOLUNTARIOS", "Para preparar la comida, la música y los juegos para niños.", "Sábado 14, de 10:00 a 20:00.", "Información: Sra. Llorca (fiesta@barriosur.es)"],
         "Escriba un correo a la señora Llorca. En el correo tiene que:",
         ["saludar;", "presentarse y decir por qué quiere ayudar;", "explicar qué sabe hacer;", "preguntar a qué hora tiene que ir y qué tiene que llevar;", "agradecer y despedirse."])),
 solo("A2-N-n3", "Textos modelo · Blog (un lugar que me sorprendió)", "Taller de escritura", [NUE + "Entrada de blog"], 2,
      t2("Escriba una entrada en su blog sobre un lugar que visitó y que le sorprendió. Hable de:",
         ["qué lugar fue, cuándo y con quién;", "cómo era;", "qué hizo allí;", "qué le sorprendió más;", "si quiere volver y por qué."])),
 solo("A2-N-n4", "Textos modelo · Texto con fotos (cena en casa con amigos)", "Taller de escritura", [NUE + "Texto con fotos"], 2,
      t2("El mes pasado usted organizó una cena en su casa para unos amigos. Aquí tiene tres fotos de ese día.",
         ["qué compró por la mañana y qué quería preparar;", "qué problema tuvo por la tarde;", "cómo terminó la noche y cómo se sintió."],
         photos=["Por la mañana. Usted compra pescado y verduras en un mercado lleno de gente.", "Por la tarde. Hay humo en la cocina: el arroz se ha quemado y suena el timbre.", "Por la noche. Todos cenan pizza en la terraza y se ríen."],
         intro2="Escriba un texto sobre ese día. Hable de:")),
]

# ------------------------------------------------------------------ FICHAS DE REMEDIO (R): "Ahora tú", escritura
def rl(clave, nombre, tarea, intro, mensaje, consigna, pautas):
    if tarea == 1:
        return solo(clave, nombre, "Fichas de remedio", [], 1, t1(intro, [mensaje] if mensaje else [], consigna, pautas))
    return solo(clave, nombre, "Fichas de remedio", [], 2, t2(consigna, pautas))

FICHAS_AT = [
 rl("A2-R01-lola", "R01 Pasados · Correo a Lola (el fin de semana)", 1, "Has recibido este mensaje de tu amiga Lola:",
    "¡Hola! ¿Qué tal? Hace mucho que no sé nada de ti. Yo este fin de semana he ido a un concierto de jazz en la playa y ha sido increíble. ¿Y tú? ¿Qué hiciste el sábado? ¡Cuéntame! Besos, Lola",
    "Escribe un correo a Lola. En él tienes que:",
    ["saludar;", "contarle qué hiciste el fin de semana y con quién;", "decirle cómo era el lugar y qué tiempo hacía;", "preguntarle por el concierto (dos preguntas);", "despedirte."]),
 rl("A2-R01-dia", "R01 Pasados · Blog: un día que no salió como pensabas", 2, "", "",
    "Escribe una entrada para tu blog sobre un día que no salió como pensabas. Cuenta:",
    ["cuándo fue, dónde estabas y con quién;", "qué ibas a hacer ese día;", "qué pasó;", "cómo te sentiste y cómo terminó el día;", "si te ha pasado algo parecido otra vez."]),
 rl("A2-R02-piso", "R02 Hay / está / es · Correo a Héctor (el piso nuevo)", 1, "Has recibido este mensaje de tu amigo Héctor:",
    "¡Hola! Me han dicho que ya vives en tu piso nuevo. ¡Enhorabuena! ¿Dónde está? ¿Cómo es el barrio? ¿Hay tiendas cerca? Cuéntame. Un abrazo, Héctor",
    "Escribe un correo a Héctor. En él tienes que:",
    ["saludar;", "decirle dónde está tu piso nuevo;", "contarle qué hay en el barrio;", "invitarle a la fiesta del piso: dónde y cuándo es;", "despedirte."]),
 rl("A2-R02-barrio", "R02 Hay / está / es · Revista: Mi barrio", 2, "", "",
    "Una revista para estudiantes de español busca textos sobre «Mi barrio». Escribe un texto. Habla de:",
    ["dónde está tu barrio y cómo es;", "qué hay en tu barrio (tiendas, parques, transporte...);", "tu lugar favorito y dónde está;", "qué no hay y te gustaría tener;", "una fiesta o un mercado del barrio: cuándo y dónde es."]),
 rl("A2-R04-familia", "R04 Concordancia y posesivos · Correo a Clara (tu familia)", 1, "Has recibido este mensaje de tu amiga Clara:",
    "¡Hola! ¡Qué bien que en agosto voy a tu casa! Pero no conozco a tu familia... ¿Cuántos sois? ¿Cómo son? Cuéntame un poco, porfa. Un beso, Clara",
    "Escribe un correo a Clara. En él tienes que:",
    ["saludar;", "decirle quiénes son las personas de tu familia;", "describir a una de ellas: cómo es y qué ropa lleva normalmente;", "contarle cómo es vuestra casa;", "despedirte."]),
 rl("A2-R04-persona", "R04 Concordancia y posesivos · Revista: una persona importante", 2, "", "",
    "Una revista de estudiantes de español busca textos sobre «Una persona importante en mi vida». Escribe un texto. Habla de:",
    ["quién es y dónde vive;", "cómo es físicamente;", "cómo es su carácter;", "qué cosas hacéis juntos o hacíais antes;", "por qué es importante para ti."]),
 rl("A2-R05-nico", "R05 Muy / mucho · Correo a Nico (gustos y tu ciudad)", 1, "Has recibido este correo de tu amigo Nico:",
    "¡Hola! Te cuento cosas de mí para conocernos mejor: me encanta la música, sobre todo el rock, pero no me gusta nada bailar. Hago mucho deporte y no veo la tele. ¿Y tú? En mayo voy a tu ciudad: ¿cómo es? Un abrazo, Nico",
    "Escribe un correo a Nico. En él tienes que:",
    ["saludar;", "reaccionar a sus gustos: qué cosas tenéis en común y cuáles no;", "describir tu ciudad: cómo es y qué hay;", "proponerle un plan para su visita;", "despedirte."]),
 rl("A2-R05-lugar", "R05 Muy / mucho · Revista: un lugar que me gusta mucho", 2, "", "",
    "Una revista de estudiantes de español busca textos sobre «Un lugar que me gusta mucho». Escribe un texto. Habla de:",
    ["dónde está y cómo es;", "qué hay allí;", "qué haces allí y con quién;", "cuándo fuiste por primera vez;", "por qué te gusta tanto."]),
 rl("A2-R06-quedar", "R06 Preposiciones · Correo a Rubén (quedar el sábado)", 1, "Has recibido este mensaje de tu amigo Rubén:",
    "¡Hola! Este sábado estoy libre por fin. Trabajo por la mañana, pero por la tarde puedo. ¿Hacemos algo juntos? ¿Qué te apetece? Dime algo. Rubén",
    "Escribe un correo a Rubén. En él tienes que:",
    ["saludar;", "proponer un plan: qué hacéis y adónde vais;", "decir dónde y a qué hora quedáis;", "explicar cómo vais a ir;", "despedirte."]),
 rl("A2-R06-semana", "R06 Preposiciones · Blog: Mi semana", 2, "", "",
    "Escribe una entrada para tu blog: «Mi semana». Habla de:",
    ["dónde vives y dónde trabajas o estudias;", "cómo vas cada día;", "tu horario: de qué hora a qué hora trabajas o estudias;", "qué haces por la mañana, por la tarde y el fin de semana;", "para qué estudias español."]),
 rl("A2-R07-noa", "R07 Tú y usted · Correo a Noa (se muda a tu ciudad)", 1, "Ha recibido este mensaje de su amiga Noa:",
    "¡Hola! ¡Tengo una noticia! En junio me mudo a tu ciudad por trabajo. Busco piso y no conozco a nadie. ¿Me ayudas? ¿Qué barrio me recomiendas? Un beso, Noa",
    "Escriba un correo a Noa. En él tiene que:",
    ["saludar;", "decir que se alegra y ofrecerle ayuda;", "recomendarle un barrio y decir por qué;", "preguntarle cuándo llega y si necesita algo más;", "despedirse."]),
 rl("A2-R07-compas", "R07 Tú y usted · Correo a la señora Ferrer (Academia Compás)", 1, "Ha visto este anuncio en su barrio:",
    "ACADEMIA COMPÁS · Clases de baile para adultos: salsa, flamenco y tango. Grupos de mañana y de tarde. Información: Sra. Ferrer (info@academiacompas.es)",
    "Escriba un correo a la señora Ferrer. En él tiene que:",
    ["saludar;", "presentarse y decir por qué escribe;", "preguntar por los horarios y el precio;", "preguntar si puede hacer una clase de prueba;", "agradecer y despedirse."]),
 # --- 23/10: R08, R10, R13 y R14a (mismos textos que sus bancos: banco_R08_conectores.py, banco_R10_pronombres.py,
 #     banco_R13_funciones.py y banco_R14a_vocabulario.py, LAMINAS)
 rl("A2-R08-raul", "R08 Conectores · Correo a Raúl (la paella en el pueblo)", 1, "Ha recibido este mensaje de su amigo Raúl:",
    "¡Hola! El domingo hacemos una paella en la casa de mis padres, en el pueblo. Vienen mis hermanos y algunos amigos del trabajo. ¿Te apuntas? Podemos ir juntos en mi coche. Escríbeme. Un abrazo, Raúl",
    "Escriba un correo a Raúl. En él tiene que:",
    ["saludar y darle las gracias por la invitación;", "decir que no puede ir y explicar por qué;", "contarle qué ha hecho este fin de semana;", "proponerle otro plan para otro día;", "despedirse."]),
 rl("A2-R08-cambio", "R08 Conectores · Revista: un cambio importante en mi vida", 2, "", "",
    "Una revista para estudiantes de español busca textos sobre «Un cambio importante en mi vida». Escriba un texto para la revista. Hable de:",
    ["qué cambio fue y cuándo pasó;", "cómo era su vida antes del cambio;", "por qué decidió cambiar;", "qué fue difícil al principio y qué fue fácil;", "cómo es su vida ahora y qué piensa del cambio."]),
 rl("A2-R10-lucia", "R10 Lo, la, le · Correo a Lucía (fiesta sorpresa para su madre)", 1, "Ha recibido este mensaje de su amiga Lucía:",
    "¡Hola! El sábado es el cumpleaños de mi madre y le preparamos una fiesta sorpresa. ¿Me ayudas? Necesito a alguien para comprar la tarta y las flores. Ah, ¿todavía tienes mi libro de fotografía? Besos, Lucía",
    "Escriba un correo a Lucía. En él tiene que:",
    ["saludar y decir si puede ayudarla;", "decir qué va a comprar usted y cuándo;", "proponer un regalo para su madre;", "contestar a su pregunta sobre el libro;", "despedirse."]),
 rl("A2-R10-persona", "R10 Lo, la, le · Revista: una persona que me ha ayudado mucho", 2, "", "",
    "Una revista para estudiantes de español busca textos sobre «Una persona que me ha ayudado mucho». Escriba un texto para la revista. Hable de:",
    ["quién es y cómo la conoció;", "cómo era su vida en aquel momento;", "qué le enseñó o qué le dijo esa persona;", "qué relación tienen ahora: cuándo la ve, qué hacen juntos;", "qué va a hacer para darle las gracias."]),
 rl("A2-R13-vanesa", "R13 Funciones de los correos · Correo a Vanesa (beca en Lisboa, de tú)", 1, "Su amiga Vanesa le escribe este correo:",
    "¡Hola! ¡Tengo una noticia buenísima! Me han dado una beca y en enero me voy seis meses a estudiar a Lisboa. Antes de irme, el sábado 20, hago una cena de despedida en mi casa. ¿Vienes? Besos, Vanesa",
    "Conteste a Vanesa. En el correo tiene que:",
    ["saludar y felicitarla por la beca;", "decir si puede ir a la cena y por qué;", "darle un consejo para su vida en Lisboa;", "pedirle algo de Lisboa o proponerle una visita;", "desearle buen viaje y despedirse."]),
 rl("A2-R13-medina", "R13 Funciones de los correos · Correo a la señora Medina (asociación de vecinos, de usted)", 1, "Usted ha recibido este correo de la asociación de vecinos de su barrio:",
    "Estimado vecino: El sábado 14 celebramos los veinte años de la asociación con una comida en la plaza, a las dos. Nos gustaría contar con usted. ¿Puede ayudarnos con las mesas por la mañana? Un saludo, Elvira Medina",
    "Conteste a la señora Medina. En el correo tiene que:",
    ["saludar y agradecer la invitación;", "decir si puede ir a la comida y por qué;", "contestar si puede ayudar por la mañana (si no puede, disculparse);", "pedir información sobre la comida (qué hay que llevar, el precio...);", "desearle una buena fiesta y despedirse."]),
 rl("A2-R14a-nacho", "R14a Vocabulario · Correo a Nacho (se muda a tu ciudad)", 1, "Ha recibido este mensaje de su amigo Nacho:",
    "¡Hola! ¡Tengo trabajo en tu ciudad! Me mudo el mes que viene, pero no conozco nada. ¿Dónde haces tú la compra? ¿Hay tiendas de ropa baratas? ¿Y qué hago si me pongo enfermo? Escríbeme pronto. Un abrazo, Nacho",
    "Escriba un correo a Nacho. En él tiene que:",
    ["saludarle y decirle qué le parece la noticia;", "recomendarle dónde hacer la compra y qué comprar allí;", "explicarle dónde puede comprar ropa y cómo son los precios;", "decirle qué tiene que hacer si se pone enfermo;", "invitarle a cenar en su casa, decirle qué va a cocinar y despedirse."]),
 rl("A2-R14a-casa", "R14a Vocabulario · Revista: Mi casa, antes y ahora", 2, "", "",
    "Una revista para estudiantes de español busca textos sobre «Mi casa: antes y ahora». Escriba un texto para la revista. Hable de:",
    ["cómo era la casa donde vivía de niño o de niña;", "con quién vivía y cómo era esa persona;", "cómo es su casa ahora: las partes y los muebles;", "qué tareas de la casa hace usted y cuáles no le gustan;", "qué quiere cambiar en su casa y por qué."]),
 # --- 23/10 noche: R14b (mismos textos que banco_R14b_vocabulario.py, LAMINAS)
 rl("A2-R14b-sara", "R14b Vocabulario · Correo a Sara (un viaje en julio)", 1, "Ha recibido este mensaje de su amiga Sara:",
    "¡Hola! ¡Por fin he terminado los exámenes! Ahora quiero hacer un viaje contigo en julio. ¿Adónde podemos ir? ¿Cómo viajamos? ¿Y qué tiempo hace allí? Cuéntame también qué tal en tu trabajo nuevo. Muchos besos, Sara",
    "Escriba un correo a Sara. En él tiene que:",
    ["felicitarla por los exámenes y preguntarle por sus notas;", "contarle qué tal en su trabajo este mes;", "proponerle un sitio para ir y cómo viajar;", "decirle qué tiempo hace allí en julio y qué tiene que llevar;", "proponerle qué hacer allí en el tiempo libre y despedirse."]),
 rl("A2-R14b-semana", "R14b Vocabulario · Revista: Mi semana (trabajo, estudios y tiempo libre)", 2, "", "",
    "Una revista para estudiantes de español busca textos sobre «Mi semana: trabajo, estudios y tiempo libre». Escriba un texto para la revista. Hable de:",
    ["dónde trabaja o estudia y cómo es su horario;", "qué hacía en su tiempo libre cuando era niño o niña;", "qué hace ahora los fines de semana y con quién;", "para qué usa el móvil y las redes sociales;", "qué estación del año prefiere para salir y por qué."]),
]

# ------------------------------------------------------------------ BANCO DE ESCRITURA (M3-6, 24/10/2026)
# 20 laminas de banco_escritura_M3.py (build_M3_banco.py). La pieza copia «== Banco de escritura · <titulo> (tarea n) ==»;
# las de «Como en el examen» llevan el mismo nombre, asi que se reconocen igual. Se corrigen como una sola tarea (sobre 25).
BAN = "Banco de escritura · "
BANCO = [
 solo("A2-B-a1", BAN + 'Lola empieza la universidad', "Taller de escritura", [BAN + 'Lola empieza la universidad'], 1,
      t1('Su amiga Lola le ha escrito este correo.',
         ['¡Hola! ¿Cómo va todo? Te cuento una noticia: con cincuenta años, ¡he empezado a estudiar Historia en la universidad! Tengo clase tres tardes a la semana y estoy muy contenta, pero un poco nerviosa. ¿Y tú? ¿Qué tal estás?', 'Un beso, Lola'],
         'Conteste a Lola. En el correo tiene que:',
         ['saludar y felicitarla por la noticia;', 'contarle si usted ha estudiado algo en los últimos años y qué tal fue;', 'explicarle qué asignatura le gustaba más en el colegio y por qué;', 'proponerle una cena para celebrarlo: el día y el lugar;', 'hacerle dos preguntas sobre sus clases y despedirse.'])),
 solo("A2-B-a2", BAN + 'Hugo y su perro Rufo', "Taller de escritura", [BAN + 'Hugo y su perro Rufo'], 1,
      t1('Su amigo Hugo le ha escrito este correo.',
         ['¡Hola! ¿Qué tal? Te escribo para pedirte un favor. El próximo fin de semana voy a una boda en Sevilla y no puedo llevar a Rufo. ¿Puedes cuidarlo en tu casa? Es muy bueno y solo come dos veces al día.', 'Un abrazo, Hugo'],
         'Conteste a Hugo. En el correo tiene que:',
         ['saludar y decirle si puede cuidar a Rufo y por qué;', 'contarle qué hizo usted el último fin de semana;', 'explicarle si tenía animales cuando era pequeño o pequeña y cómo eran;', 'decirle qué va a hacer con Rufo o, si no puede cuidarlo, proponerle otra solución;', 'hacerle dos preguntas sobre la boda y despedirse.'])),
 solo("A2-B-a3", BAN + 'Iván no fue a la clase de inglés', "Taller de escritura", [BAN + 'Iván no fue a la clase de inglés'], 1,
      t1('Iván, un compañero de su clase de inglés, le ha escrito este correo.',
         ['¡Hola! ¿Qué tal? El martes no fui a clase porque estaba enfermo. ¿Qué hicisteis? ¿Hay deberes para el jueves? Ah, y el sábado quiero estudiar un poco para el examen de diciembre. ¿Te apetece estudiar conmigo?', 'Hasta pronto, Iván'],
         'Conteste a Iván. En el correo tiene que:',
         ['saludar y preguntarle cómo está;', 'contarle qué hicieron en la clase del martes;', 'explicarle qué deberes tienen para el jueves;', 'contestar si quiere estudiar con él y proponerle la hora y el lugar;', 'contarle cómo preparaba usted antes los exámenes y despedirse.'])),
 solo("A2-B-a4", BAN + 'Una invitación del tío Paco', "Taller de escritura", [BAN + 'Una invitación del tío Paco'], 1,
      t1('Su tío Paco le ha escrito este correo.',
         ['¡Hola! ¿Cómo estás? Este verano vamos a pasar todo agosto en la casa del pueblo. ¿Por qué no vienes unos días? Hay sitio para ti y en el pueblo hace menos calor que en la ciudad. Tus primos también van a venir.', 'Un beso muy fuerte, tío Paco'],
         'Conteste a su tío. En el correo tiene que:',
         ['saludar y agradecerle la invitación;', 'contarle qué ha hecho usted este verano;', 'decirle qué días puede ir y cómo va a viajar;', 'recordar algo que hacía en el pueblo cuando era pequeño o pequeña;', 'preguntarle qué tiene que llevar y despedirse.'])),
 solo("A2-B-a5", BAN + 'Álex quiere salir a correr', "Taller de escritura", [BAN + 'Álex quiere salir a correr'], 1,
      t1('Su amigo Álex le ha escrito este correo.',
         ['¡Hola! ¿Qué tal todo? Tengo una idea: quiero empezar a correr los domingos por la mañana en el parque del río. Solo un poco, ¡no soy deportista! ¿Quieres venir conmigo? Así es más divertido. ¿Tú haces algún deporte?', 'Un abrazo, Álex'],
         'Conteste a Álex. En el correo tiene que:',
         ['saludar y decirle qué le parece su idea;', 'contestar a su pregunta: qué deporte hace usted ahora y cuándo;', 'contarle qué deporte hacía antes y por qué lo dejó;', 'decirle si va a ir con él el domingo y a qué hora quedan;', 'hacerle una pregunta y despedirse.'])),
 solo("A2-B-a6", BAN + 'Carla y el mercadillo del barrio', "Taller de escritura", [BAN + 'Carla y el mercadillo del barrio'], 1,
      t1('Su amiga Carla le ha escrito este correo.',
         ['¡Hola! ¿Qué tal? El domingo organizo con la asociación de vecinos un mercadillo de ropa y libros usados para ayudar al comedor del barrio. ¿Puedes ayudarnos? Necesitamos gente de diez a dos. ¿Tienes cosas que ya no usas?', 'Un beso, Carla'],
         'Conteste a Carla. En el correo tiene que:',
         ['saludar y decirle qué le parece el mercadillo;', 'decirle si puede ayudar el domingo y, si no puede, explicar por qué;', 'contarle qué cosas le va a llevar y cuándo;', 'explicarle qué hacía usted antes con la ropa vieja y qué hace ahora;', 'hacerle una pregunta sobre el mercadillo y despedirse.'])),
 solo("A2-B-b1", BAN + 'Revista: «Mi primer trabajo»', "Taller de escritura", [BAN + 'Revista: «Mi primer trabajo»'], 2,
      t2('Una revista en español busca textos de sus lectores sobre «Mi primer trabajo». Escriba su texto. Hable de:',
         ['cuál fue su primer trabajo, cuándo y dónde;', 'cómo era un día normal en ese trabajo y cómo eran sus compañeros;', 'algo que pasó un día y que usted recuerda bien;', 'a qué se dedica ahora y qué le gusta de su trabajo o de sus estudios;', 'qué trabajo le gustaría tener en el futuro y por qué.'])),
 solo("A2-B-b2", BAN + 'Diario: un día en que todo salió mal', "Taller de escritura", [BAN + 'Diario: un día en que todo salió mal'], 2,
      t2('Escriba una entrada en su diario sobre un día reciente en que todo salió mal. Hable de:',
         ['qué día fue y qué tenía que hacer ese día;', 'qué problemas tuvo por la mañana y por la tarde;', 'cómo se sentía y qué hizo para solucionarlos;', 'qué hace normalmente cuando tiene un mal día;', 'qué va a hacer de otra manera la próxima vez.'])),
 solo("A2-B-b3", BAN + 'Blog: mi barrio antes y ahora', "Taller de escritura", [BAN + 'Blog: mi barrio antes y ahora'], 2,
      t2('Escriba una entrada en su blog sobre el barrio donde vive. Hable de:',
         ['cómo se llama su barrio, dónde está y desde cuándo vive allí;', 'cómo era el barrio cuando usted llegó;', 'qué ha cambiado en los últimos años;', 'qué es lo que más le gusta y lo que menos;', 'qué cosas nuevas va a haber en el barrio o le gustaría tener.'])),
 solo("A2-B-b4", BAN + 'Revista: «Una costumbre de mi familia»', "Taller de escritura", [BAN + 'Revista: «Una costumbre de mi familia»'], 2,
      t2('Una revista busca textos de sus lectores sobre «Una costumbre de mi familia». Escriba su texto. Hable de:',
         ['qué costumbre es y cuándo la hacen;', 'quién empezó esta costumbre y cómo era cuando usted era pequeño o pequeña;', 'la última vez que la hicieron: cuándo fue y quién estaba;', 'qué es lo que más le gusta de esta costumbre;', 'si quiere seguir con ella en el futuro y por qué.'])),
 solo("A2-B-c1", BAN + 'Julián Prieto, del fútbol al huerto', "Taller de escritura", [BAN + 'Julián Prieto, del fútbol al huerto'], 2,
      t2('Julián Prieto vive en un pueblo de Teruel. Aquí tiene algunas fotos y datos sobre su vida.',
         ['dónde y cuándo nació y cómo era de joven;', 'a qué se dedicó y qué hacía los fines de semana;', 'qué hace ahora y por qué cree usted que dejó el fútbol en 1980.'],
         photos=['1975. Un chico de unos dieciséis años, con la camiseta de un equipo, juega al fútbol en un campo de tierra.', '1995. Un hombre de unos treinta y cinco años, con un silbato, entrena a un grupo de niños.', 'Hoy. El mismo hombre, mayor y con gorra, recoge tomates en su huerto con su nieta.'],
         ficha=['Nació en Teruel en 1959.', 'De joven: muy deportista; juega en el equipo de su pueblo.', '1980: deja el fútbol; empieza a trabajar en una fábrica de muebles.', '1990-2020: entrena a los niños del pueblo los fines de semana.', '2021: se jubila.', 'Hoy: tiene un huerto; su nieta lo ayuda los sábados.'],
         intro2='Escriba un texto sobre Julián. Hable de:')),
 solo("A2-B-c2", BAN + 'Nuria Vidal, enfermera', "Taller de escritura", [BAN + 'Nuria Vidal, enfermera'], 2,
      t2('Nuria Vidal es enfermera. Aquí tiene algunas fotos y datos sobre su vida.',
         ['dónde y cuándo nació y qué le gustaba de niña;', 'dónde trabajó después de sus estudios y cómo era su vida allí;', 'qué hace ahora y por qué cree usted que todavía viaja a Perú.'],
         photos=['Una niña de unos ocho años juega a ser enfermera: le pone una venda a su muñeca.', 'Una mujer joven, con ropa de enfermera, vacuna a un niño en un centro de salud pequeño de un pueblo de Perú.', 'La misma mujer, hoy, con el pelo corto y gris, da una clase a estudiantes de Enfermería.'],
         ficha=['Nació en Lleida en 1970.', 'De niña: le encanta cuidar a la gente; quiere ser enfermera.', '1992: termina sus estudios de Enfermería.', '1994-2001: trabaja en un centro de salud de Perú; aprende quechua.', '2002: vuelve a España.', 'Hoy: es profesora en la universidad; viaja a Perú todos los veranos.'],
         intro2='Escriba un texto sobre Nuria. Hable de:')),
 solo("A2-B-c3", BAN + 'Pilar y Ramón, una vida bailando', "Taller de escritura", [BAN + 'Pilar y Ramón, una vida bailando'], 2,
      t2('Pilar y Ramón están juntos desde hace casi cincuenta años. Aquí tiene algunas fotos y datos sobre su vida.',
         ['cómo y cuándo se conocieron y a qué se dedicaban entonces;', 'qué hicieron después y cómo era su escuela;', 'cómo es su vida ahora y por qué cree usted que cerraron la escuela.'],
         photos=['1976. Una chica y un chico de unos veinte años bailan de noche en las fiestas de un pueblo, con luces de colores.', '1990. Los dos, de unos treinta y cinco años, enseñan a bailar a varias parejas en una sala con espejos.', 'Hoy. Los dos, ya mayores, bailan en el salón de su casa con su nieto pequeño.'],
         ficha=['1976: se conocen en las fiestas de Benicàssim.', 'Entonces: ella es peluquera; él, conductor de autobús.', '1979: se casan.', '1988: abren una escuela de baile en Castellón.', '2018: cierran la escuela.', 'Hoy: bailan todos los domingos con sus nietos.'],
         intro2='Escriba un texto sobre Pilar y Ramón. Hable de:')),
 solo("A2-B-c4", BAN + 'Karim Haddad y su taller de bicis', "Taller de escritura", [BAN + 'Karim Haddad y su taller de bicis'], 2,
      t2('Karim Haddad tiene un taller de bicicletas en Valencia. Aquí tiene algunas fotos y datos sobre su vida.',
         ['dónde nació y qué le gustaba hacer de niño;', 'cómo fue su vida cuando llegó a Valencia;', 'qué hace ahora y por qué cree usted que da clases a jóvenes.'],
         photos=['Un niño de unos doce años arregla una bicicleta vieja delante de su casa, en un pueblo de Marruecos.', 'Un hombre joven trabaja en un campo de naranjos; lleva una caja llena de naranjas.', 'El mismo hombre, hoy, con barba gris, arregla una bici en su taller y habla con una clienta.'],
         ficha=['Nació cerca de Fez (Marruecos) en 1981.', 'De niño: le encantan las bicis; arregla las de sus amigos.', '2001: llega a Valencia; trabaja en el campo, en la recogida de la naranja.', '2001-2008: estudia español por las noches.', '2009: abre un taller de bicicletas.', 'Hoy: tiene dos empleados; da clases de mecánica a jóvenes.'],
         intro2='Escriba un texto sobre Karim. Hable de:')),
 solo("A2-B-d1", BAN + 'La fiesta sorpresa de mamá', "Taller de escritura", [BAN + 'La fiesta sorpresa de mamá'], 2,
      t2('El mes pasado usted organizó con sus hermanos una fiesta sorpresa por la jubilación de su madre. Aquí tiene tres fotos de ese día.',
         ['por qué organizaron la fiesta, dónde y qué hicieron por la mañana;', 'qué pasó cuando llegó su madre y cómo estaba ella;', 'qué le regalaron y qué cree usted que va a hacer su madre ahora.'],
         photos=['Por la mañana. Usted y su hermano ponen globos y una guirnalda en el salón de su hermana.', 'Por la tarde. Su madre abre la puerta y ve a toda la familia; se pone las manos en la cara.', 'Por la noche. Su madre abre su regalo: es una bicicleta con un lazo rojo.'],
         ficha=[],
         intro2='Escriba un texto sobre ese día. Hable de:')),
 solo("A2-B-d2", BAN + 'El sábado que pintamos el piso', "Taller de escritura", [BAN + 'El sábado que pintamos el piso'], 2,
      t2('El sábado pasado usted pintó el salón de su piso con dos amigos. Aquí tiene tres fotos de ese día.',
         ['por qué pintaron el salón, con quién y qué hicieron primero;', 'qué pasó a mediodía y qué hicieron todos;', 'cómo era el salón antes, cómo es ahora y qué más va a cambiar en su casa.'],
         photos=['Por la mañana. Usted y sus amigos tapan los muebles con plásticos; hay botes de pintura en el suelo.', 'A mediodía. A un amigo se le cae un bote de pintura azul en los pies; todos se ríen.', 'Por la noche. El salón ya está azul; ustedes brindan con limonada en el balcón.'],
         ficha=[],
         intro2='Escriba un texto sobre ese día. Hable de:')),
 solo("A2-B-d3", BAN + 'Voluntaria en la carrera popular', "Taller de escritura", [BAN + 'Voluntaria en la carrera popular'], 2,
      t2('El domingo pasado usted fue voluntario o voluntaria en una carrera popular de su ciudad. Aquí tiene tres fotos de ese día.',
         ['por qué fue voluntario o voluntaria, a qué hora empezó y qué tenía que hacer;', 'qué pasó cuando llegaron los corredores;', 'cómo terminó el día, cómo se sentía y si quiere repetir el año que viene.'],
         photos=['Muy temprano. Usted, con la camiseta amarilla de los voluntarios, pone botellas de agua y plátanos en unas mesas.', 'A mediodía. Pasan los corredores y usted les da agua. Una corredora mayor le choca la mano.', 'Por la tarde. Los voluntarios, cansados, comen bocadillos sentados en el césped y se ríen.'],
         ficha=[],
         intro2='Escriba un texto sobre ese día. Hable de:')),
 solo("A2-B-d4", BAN + 'La excursión en bici y el tractor', "Taller de escritura", [BAN + 'La excursión en bici y el tractor'], 2,
      t2('El verano pasado usted hizo una excursión en bici con su familia. Aquí tiene tres fotos de ese día.',
         ['adónde fueron, qué tiempo hacía y cómo era el camino;', 'qué problema tuvieron a mediodía y qué hicieron;', 'cómo volvieron a casa, qué le pareció el día y qué excursión quiere hacer la próxima vez.'],
         photos=['Por la mañana. Usted, su pareja y sus dos hijos van en bici por un camino entre campos de girasoles.', 'A mediodía. La bici de su hijo tiene una rueda pinchada; ustedes la miran sentados en el suelo.', 'Por la tarde. Un agricultor lleva a la familia y las bicis en el remolque de su tractor.'],
         ficha=[],
         intro2='Escriba un texto sobre ese día. Hable de:')),
 solo("A2-B-u1", BAN + 'La profesora de pilates cambia el horario' + " (por si acaso)", "Taller de escritura", [BAN + 'La profesora de pilates cambia el horario'], 1,
      t1('Usted va a clases de pilates en el centro cultural de su barrio. Su profesora, Isabel Gómez, le ha escrito este correo.',
         ['Estimados alumnos: a partir de noviembre las clases de los lunes y los miércoles van a ser a las siete de la tarde, no a las seis. Si alguien no puede venir a esa hora, escríbame. Hay plazas en el grupo de los sábados.', 'Un saludo, Isabel Gómez'],
         'Conteste a Isabel Gómez. En el correo tiene que:',
         ['saludar;', 'decirle si va a poder ir a la nueva hora y por qué;', 'contarle cuándo empezó sus clases y qué le parecen;', 'preguntarle por el grupo de los sábados: la hora y el número de alumnos;', 'agradecerle la información y despedirse.'])),
 solo("A2-B-u2", BAN + 'Una reserva en la casa rural' + " (por si acaso)", "Taller de escritura", [BAN + 'Una reserva en la casa rural'], 1,
      t1('Usted ha reservado dos noches en una casa rural y ha recibido este correo.',
         ['Estimado cliente: muchas gracias por su reserva en Casa Las Encinas para las noches del 14 y el 15 de marzo. ¿A qué hora piensa llegar? La cena no está incluida, pero podemos prepararla por quince euros por persona. ¿Necesita algo más?', 'Atentamente, Pilar Rubio'],
         'Conteste a Pilar Rubio. En el correo tiene que:',
         ['saludar y confirmar la reserva;', 'decir a qué hora va a llegar y con quién va a ir;', 'contestar si quiere la cena y explicar por qué;', 'contar cómo conoció la casa rural;', 'hacer una pregunta sobre la zona, agradecer y despedirse.'])),
]

# Fichas de remedio publicadas (el informe enlaza la ficha cuando hay errores de ese contenido)
# R14 = vocabulario de la casa y del día a día (R14a); R14b = vocabulario de fuera de casa (viajes, ocio, estudios, trabajo,
# tiempo, servicios). patch_corrector.py pone los dos códigos en la petición para Claude.
FICHAS = {
 "R01": ["Los pasados y las preguntas", "DELEA2_curso_R01_pasados.html"],
 "R02": ["Hay, está y es", "DELEA2_curso_R02_hay_esta_es.html"],
 "R03": ["Ser y estar", "DELEA2_curso_R03_ser_estar.html"],
 "R04": ["Concordancia y posesivos", "DELEA2_curso_R04_concordancia_posesivos.html"],
 "R05": ["Muy y mucho, también y tampoco", "DELEA2_curso_R05_muy_mucho_tambien_tampoco.html"],
 "R06": ["Preposiciones (también hace, desde hace y durante)", "DELEA2_curso_R06_preposiciones.html"],
 "R07": ["Tú y usted", "DELEA2_curso_R07_tu_usted.html"],
 "R08": ["Conectores: las flechas entre frases", "DELEA2_curso_R08_conectores.html"],
 "R09": ["Verbos como gustar", "DELEA2_curso_R09_gustar.html"],
 "R10": ["Lo, la, le: el paquete y el destinatario", "DELEA2_curso_R10_lo_la_le.html"],
 "R11": ["Planes y futuro", "DELEA2_curso_R11_futuro.html"],
 "R12": ["Traer / llevar · ir / venir · pedir / preguntar", "DELEA2_curso_R12_traer_llevar.html"],
 "R13": ["Las funciones de los correos", "DELEA2_curso_R13_formulas_correo.html"],
 "R14": ["Vocabulario en escenas (1): la casa y el día a día", "DELEA2_curso_R14a_vocabulario_casa_dia_a_dia.html"],
 "R14b": ["Vocabulario en escenas (2): fuera de casa", "DELEA2_curso_R14b_vocabulario_fuera_de_casa.html"],
}
FICHAS_LISTAS = ["R01", "R02", "R04", "R05", "R06", "R07", "R08", "R10", "R13", "R14", "R14b"]

NUEVOS = MODELOS + TALLERES + BANCO + FICHAS_AT
