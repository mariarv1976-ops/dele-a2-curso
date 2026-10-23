# -*- coding: utf-8 -*-
# TAREAS DE ESCRITURA DEL CURSO DE PREPARACION DELE A2 QUE CONOCE EL CORRECTOR DE LA PROFESORA
# (modelos completos y laminas de "Ahora tu" de los talleres de escritura y de las fichas de remedio).
# Lo usa patch_corrector.py. Cada modelo nuevo (M7, M1...) se anade aqui con su clave A2-Mxx.
# "keys": nombres con los que la pieza copia el texto (sirven para reconocer la lamina en lo que pega la profesora).
# "pz": pieza del curso de la que sale la lamina (para el desplegable).
# 23/10/2026 (chat de la R14a): FICHAS con los nombres de archivo reales de R10 y R14a y los titulos de R08, R10 y R13;
# FICHAS_LISTAS con R08, R10, R13 y R14; laminas de "Ahora tu" de R08, R10, R13 y R14a en FICHAS_AT.
# 23/10/2026 noche (chat de la R14b): ficha R14b (vocabulario de fuera de casa) en FICHAS y FICHAS_LISTAS, y sus dos laminas.

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

NUEVOS = MODELOS + TALLERES + FICHAS_AT
