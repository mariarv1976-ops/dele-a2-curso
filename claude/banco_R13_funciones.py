# -*- coding: utf-8 -*-
# BANCO DE LA FICHA DE REMEDIO R13 DEL CURSO DE PREPARACION DELE A2: LAS FUNCIONES DE LOS CORREOS
# Lo usa build_R13_funciones.py. Para cambiar contenidos, solo se toca este archivo.
#
# ENFOQUE COGNITIVO: ATRAS, ADELANTE Y CONTESTAR. Cada pauta de la tarea 1 es un verbo (agradecer, invitar...)
# y cada verbo es un gesto hacia la otra persona, en una de tres direcciones:
#   a = MIRA ATRAS, a algo que ya ha pasado: agradecer, disculparse, felicitar ("por" + lo que paso, como en la R06).
#   d = MIRA ADELANTE, a lo que quieres que pase: invitar, proponer, pedir, dar un consejo, desear algo bueno.
#   c = CONTESTA a una propuesta del otro: aceptar, rechazar con excusa.
# EL MOLDE DE TRES PIEZAS: la formula fija + el dato de la lamina + un detalle (por que, cuando, que bien).
#
# MARCAS en las frases: [f:formula] [d:dato] [x:detalle] [p:otra propuesta] (la p solo en "Si y no").
# CARRIL: "tu" (naranja) o "us" (usted, azul), los colores de la R07.
# NIVEL: solo formulas [P] del Plan curricular (GR-15: me gustaria, me encantaria, ¿podria...?, ¿le importaria...?;
# GR-17: ¡Que aproveche!, ¡Que te mejores!, ¡Que lo pases bien!, ¡Que tengas buen viaje! y sus formas de usted).
# Lo [R] o de B1 (deberias, yo que tu, espero que + subjuntivo, me gustaria que...) solo en LOS_VERAS.
# EJEMPLOS PROPIOS: nada del kit M3-1 (Marta, Lucas, Irene, Dani, escuela de cocina, Aquaforma), de la R07 (Leo,
# Iker, Joel, Noa, Ferrer) ni de los correos de los modelos (Pablo, Irene, Alba).

DIRS = {
 "a": {"n": "Mira atrás", "q": "¿Qué ha pasado ya?", "dib": "una flecha hacia lo que ya pasó",
       "txt": "Agradecer, disculparse y felicitar miran a algo que <b>ya ha pasado</b>: un regalo, un error, un examen aprobado. Por eso llevan <b>por</b> + lo que pasó: <i>gracias por, perdona por, enhorabuena por</i>."},
 "d": {"n": "Mira adelante", "q": "¿Qué quieres que pase?", "dib": "una flecha hacia lo que quieres",
       "txt": "Invitar, proponer, pedir, dar un consejo y desear algo bueno miran a lo que <b>todavía no ha pasado</b>. Por eso salen preguntas (<i>¿te apetece...?, ¿puedes...?</i>), recomendaciones y frases fijas con <i>que</i> (<i>¡que te mejores!</i>)."},
 "c": {"n": "Contesta", "q": "¿Qué te proponen?", "dib": "una respuesta que vuelve: sí o no",
       "txt": "Aceptar y rechazar <b>contestan</b> a lo que te propone el otro. El sí lleva alegría y un detalle; el no lleva siempre una excusa y, si puedes, otra propuesta."},
}
ORDEN_DIR = ["a", "d", "c"]

CARRIL = {"tu": "tú", "us": "usted"}

PIEZAS = {"f": ("La fórmula", "la frase fija de la función"), "d": ("El dato", "lo concreto de la lámina: qué, quién, cuándo"),
          "x": ("El detalle", "por qué, cómo te sientes o una pregunta"), "p": ("Otra propuesta", "un plan B")}

# ------------------------------------------------------------------ LAS DIEZ FUNCIONES
FUNCIONES = [
{"id": "agr", "n": "Agradecer", "dir": "a", "q": "¿Qué te han dado o qué han hecho por ti?",
 "molde": ["Gracias por...", "lo que te dieron o hicieron", "qué te parece"],
 "tu": ["Muchas gracias por...", "Gracias por + infinitivo (gracias por avisarme)", "¡Qué detalle!"],
 "us": ["Muchas gracias por...", "Le agradezco mucho...", "Muchas gracias por su ayuda."],
 "ej_tu": "[f:Muchas gracias por] [d:las fotos de la excursión]. [x:¡Salimos todos guapísimos!]",
 "ej_us": "[f:Muchas gracias por] [d:su respuesta tan rápida]. [x:Me ha ayudado mucho.]",
 "ojo": "Gracias <b>por</b>, nunca «gracias para». Con un verbo, el pronombre va pegado detrás: <i>gracias por invitarme</i>, no «gracias por me invitar»."},
{"id": "dis", "n": "Disculparse", "dir": "a", "q": "¿Qué has hecho mal o qué no puedes hacer?",
 "molde": ["Perdona por... / Siento...", "lo que pasó", "la razón"],
 "tu": ["Perdona por + infinitivo (perdona por no llamar)", "Lo siento mucho.", "Siento + infinitivo (siento llegar tarde)", "..., es que + la razón"],
 "us": ["Disculpe por... / Perdone por...", "Siento mucho + infinitivo", "Siento mucho las molestias.", "..., porque + la razón"],
 "ej_tu": "[f:Perdona por] [d:no contestar antes]: [x:es que he estado de viaje toda la semana.]",
 "ej_us": "[f:Siento mucho] [d:no poder ir a la reunión del jueves], [x:porque tengo cita con el médico.]",
 "ojo": "Detrás de «por» o de «siento», infinitivo: <i>perdona por no llamar</i>, <i>siento no poder ir</i>. Nunca «siento no puedo»."},
{"id": "fel", "n": "Felicitar", "dir": "a", "q": "¿Qué celebra o qué ha conseguido la otra persona?",
 "molde": ["¡Felicidades! / ¡Enhorabuena por...!", "lo que celebra o ha conseguido", "cómo te sientes tú"],
 "tu": ["¡Felicidades! / ¡Feliz cumpleaños!", "¡Enhorabuena por + lo que ha conseguido!", "Me alegro mucho por ti."],
 "us": ["¡Felicidades!", "Enhorabuena por + lo que ha conseguido.", "Me alegro mucho por usted."],
 "ej_tu": "[f:¡Enhorabuena por] [d:el trabajo nuevo]! [x:Me alegro muchísimo por ti.]",
 "ej_us": "[f:Enhorabuena por] [d:el premio de su panadería]. [x:¡Es una noticia estupenda!]",
 "ojo": "<b>¡Felicidades!</b> sirve para las fiestas: cumpleaños, santo, Navidad. <b>¡Enhorabuena!</b> es para algo que la persona ha conseguido: un examen, un trabajo, un piso, un bebé. Nunca «enhorabuena por tu cumpleaños»."},
{"id": "inv", "n": "Invitar", "dir": "d", "q": "¿A qué quieres llevar a la otra persona?",
 "molde": ["¿Te apetece...? / Te invito a...", "qué, cuándo y dónde", "por qué le va a gustar"],
 "tu": ["¿Quieres venir a...?", "¿Te apetece + infinitivo?", "Te invito a + algo / infinitivo.", "¿Te vienes?"],
 "us": ["¿Quiere venir a...?", "¿Le apetece + infinitivo?", "Le invito a + algo / infinitivo.", "Me gustaría invitarle a..."],
 "ej_tu": "[f:¿Te apetece venir] [d:a la cena del barrio el viernes]? [x:Va a haber música en la plaza.]",
 "ej_us": "[f:Le invito a] [d:la inauguración de la tienda el sábado a las doce]. [x:Vamos a tener una pequeña fiesta.]",
 "ojo": "Te invito <b>a</b> + algo o + infinitivo: <i>te invito a cenar</i>. Y «¿te apetece venir?», sin «de»."},
{"id": "pro", "n": "Proponer", "dir": "d", "q": "¿Qué plan, qué día o qué solución propones?",
 "molde": ["¿Qué te parece si...? / ¿Por qué no...?", "el plan: día, lugar, hora", "por qué es buena idea"],
 "tu": ["¿Qué te parece si + presente?", "¿Por qué no + presente?", "¿Y si + presente?", "Podemos + infinitivo.", "¿Quedamos el...?"],
 "us": ["¿Qué le parece si + presente?", "¿Le parece bien + día u hora?", "Podemos + infinitivo."],
 "ej_tu": "[f:¿Qué te parece si] [d:quedamos el domingo a las once en la puerta del parque]? [x:Así damos un paseo antes de comer.]",
 "ej_us": "[f:¿Le parece bien] [d:el martes a las diez en su oficina]? [x:Por la mañana tengo más tiempo.]",
 "ojo": "Para proponer, «¿Por qué <b>no</b>...?». Sin «no», «¿Por qué...?» pregunta la causa. Y después de «si», presente: <i>¿qué te parece si vamos...?</i>"},
{"id": "ped", "n": "Pedir", "dir": "d", "q": "¿Qué necesitas: un favor, una cosa, una información?",
 "molde": ["¿Puedes...? / ¿Podría...?", "lo que necesitas", "para qué o por qué"],
 "tu": ["¿Puedes + infinitivo? / ¿Me puedes + infinitivo?", "¿Me dejas...? / ¿Me ayudas a...?", "¿Te importa + infinitivo?"],
 "us": ["¿Podría + infinitivo?", "¿Le importaría + infinitivo?", "Me gustaría saber...", "¿Me puede decir...?"],
 "ej_tu": "[f:¿Me puedes dejar] [d:tu tienda de campaña para el puente]? [x:La mía está rota.]",
 "ej_us": "[f:¿Podría decirme] [d:qué documentos tengo que llevar el primer día]? [x:No quiero olvidarme de nada.]",
 "ojo": "El pronombre va delante del verbo conjugado o pegado detrás del infinitivo: <i>¿me puedes ayudar?</i> o <i>¿puedes ayudarme?</i>, nunca «¿puedes me ayudar?». Con usted, <i>¿podría...?</i> es lo más educado."},
{"id": "con", "n": "Dar un consejo", "dir": "d", "q": "¿Qué es lo mejor para la otra persona?",
 "molde": ["Te recomiendo... / Tienes que...", "lo que tiene que hacer", "por qué"],
 "tu": ["Te recomiendo + algo / infinitivo.", "Tienes que + infinitivo.", "Es mejor + infinitivo.", "Imperativo: lleva, prueba, llama..."],
 "us": ["Le recomiendo + algo / infinitivo.", "Tiene que + infinitivo.", "Es mejor + infinitivo.", "Imperativo: lleve, pruebe, llame..."],
 "ej_tu": "[f:Te recomiendo] [d:el autobús de las ocho]: [x:es más rápido y no tienes que cambiar.]",
 "ej_us": "[f:Le recomiendo] [d:reservar mesa antes del viernes], [x:porque los fines de semana hay mucha gente.]",
 "ojo": "Te recomiendo + infinitivo, sin «de»: <i>te recomiendo ir temprano</i>. «Deberías» y «yo que tú» los verás, pero no los necesitas en el A2."},
{"id": "des", "n": "Desear algo bueno", "dir": "d", "q": "¿Qué le va a pasar: un viaje, un examen, una fiesta, está enfermo?",
 "molde": ["¡Que...! / ¡Mucha suerte!", "para qué", "una frase más"],
 "tu": ["¡Que te mejores!", "¡Que lo pases bien!", "¡Que tengas buen viaje!", "¡Que aproveche!", "¡Mucha suerte! / ¡Buen viaje!"],
 "us": ["¡Que se mejore!", "¡Que lo pase bien!", "¡Que tenga buen viaje!", "¡Que aproveche!", "¡Mucha suerte!"],
 "ej_tu": "[f:¡Que lo pases muy bien] [d:en Menorca]! [x:Ya me contarás.]",
 "ej_us": "[f:¡Que tenga] [d:muy buen viaje a Roma]! [x:Ya nos contará qué tal.]",
 "ojo": "Son frases fijas: apréndelas enteras. Es «¡Que te mejores!», no «¡Que te mejoras!». Con usted: «¡Que se mejore!», «¡Que tenga buen viaje!». Antes de algo difícil, <b>¡Mucha suerte!</b>; después, si ha salido bien, <b>¡Enhorabuena!</b>"},
{"id": "ace", "n": "Aceptar", "dir": "c", "q": "¿Qué te proponen? Di que sí... ¡y algo más!",
 "molde": ["¡Claro que sí! / Me parece muy bien", "a qué dices que sí", "un detalle o una pregunta"],
 "tu": ["¡Claro que sí! / ¡Claro que voy!", "¡Qué buena idea! Me apunto.", "Vale, perfecto.", "Cuenta conmigo."],
 "us": ["Con mucho gusto.", "Me parece muy bien.", "Por supuesto.", "Cuente conmigo."],
 "ej_tu": "[f:¡Claro que voy] [d:a tu cena del viernes]! [x:¿Llevo algo de beber?]",
 "ej_us": "[f:Me parece muy bien] [d:la reunión del martes a las diez]. [x:Allí estaré.]",
 "ojo": "Un «sí» solo es muy seco. Añade un detalle o una pregunta: <i>¿llevo algo?</i>, <i>¿a qué hora quedamos?</i>"},
{"id": "rec", "n": "Rechazar con excusa", "dir": "c", "q": "¿Qué te proponen? Di que no, con cariño y con una razón.",
 "molde": ["¡Qué pena! / Lo siento, pero...", "lo que no puedes hacer", "la excusa (es que / porque)"],
 "tu": ["¡Qué pena! Me encantaría, pero...", "Esta vez no puedo: es que...", "Lo siento, pero no puedo porque..."],
 "us": ["Lo siento mucho, pero no puedo porque...", "Me encantaría, pero...", "Siento mucho no poder ir, porque..."],
 "ej_tu": "[f:¡Qué pena! Me encantaría, pero] [d:el sábado no puedo]: [x:es que tengo la boda de mi prima.]",
 "ej_us": "[f:Lo siento mucho, pero] [d:el jueves no puedo ir], [x:porque trabajo hasta las ocho.]",
 "ojo": "Nunca un «no» solo: siempre la excusa (con un amigo, «es que»; de usted, «porque») y, si puedes, otra propuesta."},
]

# Una regex por funcion (sobre el texto sin tildes y en minusculas): el detector mira si cada pauta tiene su formula.
FUNC_RX = {
 "agr": r"\bgracias\b|\bagradezco\b|\bagradecer",
 "dis": r"\bperdon(a|e)?\b|\blo siento\b|\bsiento (mucho )?(no|las|el|la|llegar)\b|\bdisculp(a|e|as)\b",
 "fel": r"\bfelicidades\b|\benhorabuena\b|\bfelicit(o|arte|arle|aros)\b|\bfeliz (cumpleanos|navidad|ano nuevo|aniversario|santo|dia)\b",
 "inv": r"\b(te|le|os|les) invito\b|\binvitar(te|le|os|les)\b|\b(quieres|quiere|quereis) venir\b|\b(te|le|os) apetece\b|\bte vienes\b|\bos venis\b",
 "pro": r"\bque (te|le|os) parece si\b|\bpor que no\b|¿y si\b|\bpodemos\b|\bquedamos\b|\b(te|le|os) parece bien\b",
 "ped": r"\b(puedes|podria)\b|\b(me|nos) (puede|dejas|deja|ayudas|ayuda|prestas|presta|traes|trae|mandas|manda|dices|dice)\b|\b(te|le) importa(ria)?\b|\bme gustaria saber\b",
 "con": r"\b(tienes|tiene) que\b|\bes mejor\b|\b(te|le|os) recomiendo\b",
 "des": r"\bque (te|se|os) mejor(es|e|eis)\b|\bque lo pas(es|e|eis)\b|\bque (tengas|tenga|tengais)\b|\bque aproveche\b|\bmucha suerte\b|\bbuen viaje\b",
 "ace": r"\bclaro que (?!no\b)|\bque buena idea\b|\bme apunto\b|\bcuent(a|e) conmigo\b|\bcon mucho gusto\b|\bme parece (muy )?bien\b|\bvale\b|\bperfecto\b|\bpor supuesto\b|\bme encantaria(?!,? pero)\b",
 "rec": r"\bno (puedo|podre|voy a poder)\b|\bsiento (mucho )?no poder\b|\bme encantaria,? pero\b|\besta vez no\b|\bque pena\b",
}

# Palabras que solo son de un carril (para las comprobaciones del build y la revision de la escritura).
TU_RX = (r"\b(tu|tus|ti|contigo|tuyo|tuya)\b|\bte\b|\bperdona\b|\boye\b|\bun (beso|abrazo)\b|\bbesos\b|\bquerid[oa]s?\b"
         r"|\b(puedes|quieres|tienes|vienes|sabes|necesitas|vas|pases|tengas|dejas|ayudas|dices|contaras)\b|\bcuenta conmigo\b")
US_RX = (r"\busted(es)?\b|\bestimad[oa]s?\b|\batentamente\b|\bcordial(es|mente)?\b|\b(perdone|disculpe|oiga)\b"
         r"|\bque (tenga|se mejore|lo pase)\b|\ble (escribo|invito|agradezco|recomiendo|parece|importaria|apetece)\b|\bpodria\b"
         r"|\bsu (ayuda|atencion|respuesta|correo|invitacion|oficina)\b|\bsra?\b\.|\bcuente conmigo\b|\b(quiere|tiene|puede) (venir|que|decirme|ayudarme)\b")

VISTAZO_NOTA = "Las fórmulas que sirven para los dos carriles van en los dos: <i>muchas gracias por, me encantaría, ¡felicidades!, ¡mucha suerte!</i>."

# ------------------------------------------------------------------ LOS VERAS ([R] y B1: solo para entenderlos)
LOS_VERAS = [
 ("Deberías... / Yo que tú...", "Dar un consejo", "Deberías descansar.", "Tienes que descansar. / Te recomiendo descansar."),
 ("Espero que estés bien.", "Desear algo bueno", "Espero que estés bien.", "¿Qué tal estás?"),
 ("Me gustaría que vinieras / que vengas", "Invitar", "Me gustaría que vengas a mi boda.", "¿Quieres venir a mi boda?"),
 ("¡Que te vaya bien! / ¡Que disfrutes!", "Desear algo bueno", "¡Que disfrutes del viaje!", "¡Que lo pases bien!"),
 ("Te lo agradezco / Te lo mando", "Dos pronombres juntos", "Te lo mando mañana.", "Mañana te mando las fotos."),
 ("Ojalá...", "Desear algo bueno", "Ojalá apruebes.", "¡Mucha suerte en el examen!"),
]

# ------------------------------------------------------------------ DE LA PAUTA A LA FRASE
LEER_PAUTA = [
 "<b>El verbo de la pauta es la función.</b> «Agradecer la invitación» pide <i>gracias por...</i>; «felicitarlo» pide <i>¡enhorabuena!</i> o <i>¡felicidades!</i>",
 "<b>«y» o una coma = dos frases.</b> «Saludar y felicitarla por la beca» son dos piezas: el saludo y la felicitación.",
 "<b>«Decir si puede...» = aceptar o rechazar.</b> Tú eliges, pero siempre con una razón o un detalle.",
 "<b>«y por qué» = el detalle del molde.</b> Si no está, la pauta queda a medias.",
 "<b>Las preguntas del correo también son pautas.</b> Si tu amigo pregunta «¿Vienes?», tu correo tiene que contestar.",
]

OTRAS_PAUTAS = [
 ("saludar / despedirse", "El saludo y la despedida del mismo carril, de tú o de usted.", "R07"),
 ("decir qué ha hecho estas semanas", "Pasado con perfecto: <i>he trabajado mucho, he empezado un curso</i>.", "R01"),
 ("explicar sus planes", "<i>Voy a</i> + infinitivo: <i>voy a buscar piso</i>.", "R01"),
 ("decir un día, un lugar y una hora", "Proponer + <i>quedamos el sábado a las seis en la plaza</i>.", "R06"),
 ("hacerle dos preguntas", "Dos frases con ¿ ? de tu carril: <i>¿Qué tal...? ¿Cuándo...?</i>", "R01 · R07"),
]

# Constructor: cada situacion tiene una version de tu y otra de usted; cada pauta, su frase en los dos carriles.
SITUACIONES = [
{"id": "inv", "tit": "Una invitación",
 "tu": {"quien": "Tu amiga Rocío", "msg": "Te invita a la comida de su cumpleaños, el domingo, en la casa de sus padres en el pueblo."},
 "us": {"quien": "La señora Campos, presidenta del club de senderismo", "msg": "Le invita a la comida de fin de temporada del club, el domingo, en un restaurante de la sierra."},
 "pautas": [
  {"f": "agr", "p": "agradecer la invitación;",
   "tu": "[f:Muchas gracias por] [d:invitarme a tu comida de cumpleaños]. [x:¡Qué ilusión!]",
   "us": "[f:Muchas gracias por] [d:su invitación a la comida del club]. [x:Es un detalle muy bonito.]"},
  {"f": "ace", "p": "aceptar la invitación;",
   "tu": "[f:¡Claro que voy] [d:el domingo]! [x:¿Llevo yo el postre?]",
   "us": "[f:Me parece muy bien] [d:la comida del domingo]. [x:Allí estaré con mucho gusto.]"},
  {"f": "rec", "p": "decir que no puede ir y por qué;",
   "tu": "[f:¡Qué pena! Me encantaría ir, pero] [d:el domingo no puedo]: [x:es que trabajo todo el día.]",
   "us": "[f:Lo siento mucho, pero] [d:el domingo no puedo ir], [x:porque ese día tengo una boda familiar.]"},
  {"f": "ped", "p": "pedir una información;",
   "tu": "[f:¿Me puedes mandar] [d:la dirección de la casa del pueblo]? [x:Nunca he estado allí.]",
   "us": "[f:¿Podría decirme] [d:a qué hora sale el autobús del club]? [x:Me gustaría ir con el grupo.]"},
  {"f": "pro", "p": "proponer otro plan;",
   "tu": "[f:¿Por qué no] [d:quedamos el lunes por la tarde]? [x:Así lo celebramos las dos.]",
   "us": "[f:¿Le parece bien] [d:si voy a la próxima excursión del club]? [x:Así conozco a los socios.]"},
 ]},
{"id": "not", "tit": "Una buena noticia",
 "tu": {"quien": "Tu primo Íñigo", "msg": "Te cuenta que tiene trabajo nuevo de bombero y que en julio se va de vacaciones a Islandia."},
 "us": {"quien": "El señor Ibáñez, su antiguo profesor de guitarra", "msg": "Le cuenta que se jubila este mes y que va a viajar por Italia."},
 "pautas": [
  {"f": "fel", "p": "felicitarlo;",
   "tu": "[f:¡Enhorabuena por] [d:el trabajo de bombero]! [x:Me alegro muchísimo por ti.]",
   "us": "[f:Enhorabuena por] [d:su jubilación]. [x:Me alegro mucho por usted.]"},
  {"f": "des", "p": "desearle buen viaje;",
   "tu": "[f:¡Que tengas] [d:muy buen viaje a Islandia]! [x:Mándame muchas fotos.]",
   "us": "[f:¡Que tenga] [d:muy buen viaje por Italia]! [x:Seguro que va a ser precioso.]"},
  {"f": "con", "p": "darle un consejo para el viaje;",
   "tu": "[f:Te recomiendo] [d:llevar ropa de abrigo, también en julio]: [x:allí hace frío por la noche.]",
   "us": "[f:Le recomiendo] [d:visitar Florencia en primavera]: [x:hay menos turistas y hace buen tiempo.]"},
  {"f": "ped", "p": "pedirle algo;",
   "tu": "[f:¿Me puedes traer] [d:un imán para la nevera]? [x:Hago una colección.]",
   "us": "[f:¿Podría mandarme] [d:alguna foto del viaje]? [x:Me encanta Italia.]"},
  {"f": "inv", "p": "invitarlo a algo;",
   "tu": "[f:¿Te apetece venir] [d:a cenar a casa antes del viaje]? [x:Así lo celebramos.]",
   "us": "[f:Me gustaría invitarle a] [d:mi concierto de diciembre en la escuela]. [x:Usted me enseñó a tocar.]"},
 ]},
{"id": "fav", "tit": "Te piden un favor",
 "tu": {"quien": "Tu amiga Celia", "msg": "Te escribe porque el sábado se cambia de piso y necesita ayuda con las cajas."},
 "us": {"quien": "La señora Roca, su vecina del cuarto", "msg": "Le escribe porque se va un mes a casa de su hija y necesita a alguien para regar las plantas."},
 "pautas": [
  {"f": "ace", "p": "decir que puede ayudarla;",
   "tu": "[f:¡Claro que te ayudo!] [d:El sábado por la mañana estoy libre]. [x:¿A qué hora quedamos?]",
   "us": "[f:Por supuesto.] [d:Puedo regar sus plantas todo el mes]. [x:¿Cada cuántos días necesitan agua?]"},
  {"f": "rec", "p": "decir que no puede y por qué;",
   "tu": "[f:Lo siento mucho, pero] [d:el sábado no puedo ayudarte]: [x:es que tengo un examen el lunes.]",
   "us": "[f:Lo siento mucho, pero] [d:en agosto no puedo], [x:porque me voy de vacaciones con mi familia.]"},
  {"f": "dis", "p": "disculparse;",
   "tu": "[f:Perdona por] [d:no poder llevar la furgoneta]: [x:es que mi hermano la necesita ese día.]",
   "us": "[f:Disculpe por] [d:no contestar antes]: [x:he estado fuera unos días.]"},
  {"f": "con", "p": "darle un consejo;",
   "tu": "[f:Tienes que] [d:pedir cajas en el supermercado]: [x:allí las dan gratis.]",
   "us": "[f:Le recomiendo] [d:dejar las plantas pequeñas en la bañera]: [x:así no se secan tan rápido.]"},
  {"f": "ped", "p": "pedirle una información;",
   "tu": "[f:¿Me dices] [d:a qué hora empezáis]? [x:Así me organizo.]",
   "us": "[f:¿Podría dejarme] [d:las llaves el viernes]? [x:El sábado salgo muy temprano.]"},
 ]},
{"id": "sal", "tit": "Alguien está enfermo",
 "tu": {"quien": "Tu amigo Samu", "msg": "Te escribe: se ha roto una pierna jugando al fútbol y tiene que estar tres semanas en casa."},
 "us": {"quien": "El señor Prats, su profesor de yoga", "msg": "Ha escrito al grupo: tiene gripe y esta semana no hay clase."},
 "pautas": [
  {"f": "des", "p": "desearle algo bueno;",
   "tu": "[f:¡Que te mejores] [d:muy pronto]! [x:Te echamos de menos en el equipo.]",
   "us": "[f:¡Que se mejore] [d:pronto]! [x:Le esperamos en clase.]"},
  {"f": "agr", "p": "agradecer el aviso;",
   "tu": "[f:Gracias por] [d:avisarme]. [x:¡Qué mala suerte!]",
   "us": "[f:Muchas gracias por] [d:avisarnos tan pronto]. [x:Es usted muy amable.]"},
  {"f": "con", "p": "darle un consejo;",
   "tu": "[f:Tienes que] [d:descansar mucho y no mover la pierna]: [x:así se cura antes.]",
   "us": "[f:Le recomiendo] [d:beber mucha agua y descansar]: [x:a mí me fue muy bien.]"},
  {"f": "pro", "p": "proponer algo;",
   "tu": "[f:¿Qué te parece si] [d:voy a tu casa el viernes con unas pizzas]? [x:Así vemos el partido juntos.]",
   "us": "[f:¿Qué le parece si] [d:recuperamos la clase el sábado por la mañana]? [x:Casi todo el grupo está libre.]"},
  {"f": "ped", "p": "pedirle algo;",
   "tu": "[f:¿Me puedes decir] [d:a qué hora estás en casa]? [x:No quiero llegar en mal momento.]",
   "us": "[f:¿Podría mandarnos] [d:algunos ejercicios para hacer en casa]? [x:Así no perdemos la costumbre.]"},
 ]},
]

# ------------------------------------------------------------------ SI Y NO
PIEZAS_NO = [("¡Qué pena! / Lo siento, pero...", "la pena"), ("no puedo + el plan", "el no"),
             ("es que... (tú) / porque... (usted)", "la excusa"), ("¿Y si...? / ¿Por qué no...?", "otra propuesta")]
PIEZAS_SI = [("¡Claro que sí! / Me parece muy bien", "el sí"), ("a qué dices que sí", "el dato"), ("¿Llevo algo? / ¿A qué hora?", "un detalle o una pregunta")]
ES_QUE = [
 ("es que", "Con amigos y familia, para explicar un no o un problema. Va al principio de la excusa.", "Perdona, es que no he visto tu mensaje."),
 ("porque", "Con todos. En un correo de usted, mejor «porque».", "No puedo ir, porque tengo una reunión."),
]
INVITACIONES = [
 {"t": "tu", "quien": "Tu amigo Gael", "msg": "¿Te vienes al concierto de jazz del jueves? Tengo dos entradas.",
  "ace": "[f:¡Qué buena idea! Me apunto.] [d:El jueves salgo a las seis]. [x:¿Dónde quedamos?]",
  "rec": "[f:¡Qué pena! Me encantaría, pero] [d:el jueves no puedo]: [x:es que tengo clase de alemán.] [p:¿Por qué no vamos juntos al próximo?]"},
 {"t": "tu", "quien": "Tu amiga Lidia", "msg": "¿Te apetece hacer una ruta en kayak el domingo por la mañana?",
  "ace": "[f:¡Claro que sí!] [d:Nunca he ido en kayak]. [x:¿Qué tengo que llevar?]",
  "rec": "[f:Lo siento, pero] [d:el domingo no puedo]: [x:es que voy a comer con mis abuelos.] [p:¿Y si vamos el domingo que viene?]"},
 {"t": "tu", "quien": "Tu compañero Jaime", "msg": "Hago una barbacoa en mi terraza el sábado. ¿Vienes?",
  "ace": "[f:¡Claro que voy!] [d:El sábado no tengo planes]. [x:¿Llevo pan y bebidas?]",
  "rec": "[f:¡Qué pena!] [d:Esta vez no puedo ir]: [x:es que tengo turno en el hospital.] [p:¿Quedamos para tomar algo el lunes?]"},
 {"t": "us", "quien": "La señora Medina, de la asociación de vecinos", "msg": "Le invitamos a la presentación del libro de fotos del barrio, el viernes a las siete.",
  "ace": "[f:Muchas gracias por la invitación. Con mucho gusto] [d:voy el viernes]. [x:¿Puedo ir con mi marido?]",
  "rec": "[f:Lo siento mucho, pero] [d:el viernes no puedo ir], [x:porque tengo una reunión de trabajo.] [p:¿Podría mandarme información del libro?]"},
 {"t": "us", "quien": "La señora Cano, directora del colegio de su hijo", "msg": "Le invitamos a la fiesta de fin de curso, el 20 de junio a las seis, en el patio del colegio.",
  "ace": "[f:Me parece muy bien.] [d:El día veinte estaré allí a las seis]. [x:¿Hace falta llevar algo?]",
  "rec": "[f:Siento mucho no poder ir] [d:a la fiesta del día veinte], [x:porque estoy de viaje esa semana.] [p:¿Le parece bien si va mi hermana?]"},
 {"t": "us", "quien": "Su jefe, el señor Ortega", "msg": "Le invito a comer con un cliente el miércoles a las dos.",
  "ace": "[f:Por supuesto.] [d:El miércoles a las dos me va muy bien]. [x:¿Dónde es la comida?]",
  "rec": "[f:Lo siento mucho, pero] [d:el miércoles no puedo], [x:porque tengo cita con el médico.] [p:¿Le parece bien el jueves?]"},
]

# ------------------------------------------------------------------ EN EL EXAMEN
DONDE = [
 ("Escritura · tarea 1", "Casi todas las pautas del correo son funciones: agradecer, felicitar, invitar, decir si puedes ir... Cada una, su frase.", "fel", "[f:¡Enhorabuena por] [d:el piso nuevo]! [x:¿Cuándo me lo enseñas?]"),
 ("Oral · tarea 3", "Con el examinador propones, aceptas, dices que no y buscas otra solución. Es lo mismo que en el correo, pero hablado.", "pro", "[f:¿Y si] [d:vamos el domingo]? [x:El sábado trabajo.]"),
 ("Lectura · tarea 1", "El correo de un amigo: ¿te invita, te pide algo, te da las gracias? Muchas preguntas son eso: para qué escribe.", "inv", "[f:¿Te apetece venir] [d:a mi casa en agosto]? [x:Tengo una habitación libre.]"),
 ("Auditiva · tarea 4", "Mensajes del contestador: ¿para qué llama? Para invitar, pedir un favor, disculparse o cambiar una cita.", "dis", "[f:Perdona por] [d:no llamarte ayer]: [x:es que llegué muy tarde.]"),
]
REGLA = "En la escala oficial, el cumplimiento mira si cada pauta tiene su frase. Una pauta que pide <b>agradecer</b> se cumple con una frase que agradece, aunque sea muy sencilla. Si falta la fórmula, la pauta queda a medias: es lo primero que se mira en la <b>pasada 1</b> de la revisión final."

ERRORES = [  # mal, bien, por que
 ("¡Enhorabuena por tu cumpleaños!", "¡Felicidades! ¡Feliz cumpleaños!", "El cumpleaños es una fiesta: ¡Felicidades! «Enhorabuena» es para algo que has conseguido."),
 ("Muchas gracias para la invitación.", "Muchas gracias por la invitación.", "Agradecer mira atrás: gracias POR lo que pasó, nunca «para»."),
 ("Gracias por me invitar.", "Gracias por invitarme.", "Con el infinitivo, el pronombre va pegado detrás."),
 ("Te invito venir a mi casa el sábado.", "Te invito a venir a mi casa el sábado.", "Te invito A + infinitivo."),
 ("Siento no puedo ir a tu fiesta.", "Siento no poder ir a tu fiesta.", "Detrás de «siento», infinitivo."),
 ("Perdona por no he contestado antes.", "Perdona por no contestar antes.", "Detrás de «por», infinitivo, también con «no»."),
 ("¡Que te mejoras pronto!", "¡Que te mejores pronto!", "Es una frase fija: apréndela entera, con «mejores»."),
 ("¿Puedes me ayudar con la mudanza?", "¿Me puedes ayudar con la mudanza?", "El pronombre va delante del verbo conjugado o pegado al infinitivo (¿puedes ayudarme?)."),
 ("Te recomiendo de visitar el museo.", "Te recomiendo visitar el museo.", "Te recomiendo + infinitivo, sin «de»."),
 ("Me gustaría que vienes a mi boda.", "¿Quieres venir a mi boda?", "«Me gustaría que...» necesita una forma de B1. En el A2, invita con una pregunta."),
 ("No puedo ir el sábado.", "No puedo ir el sábado: es que trabajo. ¿Quedamos el domingo?", "Un «no» solo queda muy seco: añade la excusa y, si puedes, otra propuesta."),
 ("¿Por qué quedamos el viernes?", "¿Por qué no quedamos el viernes?", "Para proponer, «¿Por qué NO...?». Sin «no», preguntas la causa."),
]

# ------------------------------------------------------------------ EJERCICIOS
# 1. ¿Que funcion pide la pauta? q = la pauta; o[0] = la buena (nombre de una funcion o "Aceptar o rechazar").
P_FUNC = [
 {"q": "darle las gracias por el regalo;", "f": "agr", "o": ["Agradecer", "Felicitar", "Pedir"], "why": "«Darle las gracias» = agradecer: mira atrás, a algo que ya te han dado."},
 {"q": "decir que no puede ir y explicar por qué;", "f": "rec", "o": ["Rechazar con excusa", "Aceptar", "Proponer"], "why": "Dices que no a algo que te proponen, con la razón: rechazar con excusa."},
 {"q": "felicitarla por su nuevo trabajo;", "f": "fel", "o": ["Felicitar", "Agradecer", "Desear algo bueno"], "why": "El trabajo ya lo ha conseguido: felicitar (¡Enhorabuena por...!)."},
 {"q": "proponerle otro día para quedar;", "f": "pro", "o": ["Proponer", "Aceptar", "Agradecer"], "why": "Un plan nuevo, otro día: proponer (¿Qué te parece si...?)."},
 {"q": "pedirle perdón por no ir a su fiesta;", "f": "dis", "o": ["Disculparse", "Agradecer", "Felicitar"], "why": "«Pedir perdón» = disculparse: perdona por / siento + infinitivo."},
 {"q": "recomendarle un restaurante de su ciudad;", "f": "con", "o": ["Dar un consejo", "Invitar", "Pedir"], "why": "Recomendar = dar un consejo: te recomiendo + algo."},
 {"q": "desearle suerte en el examen;", "f": "des", "o": ["Desear algo bueno", "Felicitar", "Dar un consejo"], "why": "El examen todavía no ha pasado: miras adelante y deseas algo bueno (¡Mucha suerte!). Felicitar es después."},
 {"q": "pedirle que le traiga algo de su viaje;", "f": "ped", "o": ["Pedir", "Proponer", "Desear algo bueno"], "why": "Quieres algo de la otra persona: pedir (¿Me puedes traer...?)."},
 {"q": "invitarlo a su casa el fin de semana;", "f": "inv", "o": ["Invitar", "Agradecer", "Pedir"], "why": "Le ofreces venir a tu casa: invitar (¿Te apetece venir...?)."},
 {"q": "aceptar la invitación;", "f": "ace", "o": ["Aceptar", "Agradecer", "Invitar"], "why": "Contestas que sí a algo que te proponen: aceptar, con un detalle."},
 {"q": "decirle qué tiene que visitar en su ciudad;", "f": "con", "o": ["Dar un consejo", "Pedir", "Felicitar"], "why": "Le dices qué es lo mejor para él: dar un consejo (tienes que, te recomiendo)."},
 {"q": "decirle que se alegra por su boda;", "f": "fel", "o": ["Felicitar", "Agradecer", "Desear algo bueno"], "why": "Alegrarse por algo bueno que ha pasado: felicitar (¡Felicidades por la boda!)."},
 {"q": "preguntarle si puede ayudarle con la mudanza;", "f": "ped", "o": ["Pedir", "Invitar", "Aceptar"], "why": "Necesitas su ayuda: pedir un favor (¿Me puedes ayudar...?)."},
 {"q": "decir si puede ayudarle y por qué;", "f": "ace|rec", "o": ["Aceptar o rechazar: tú eliges", "Proponer", "Agradecer"], "why": "«Decir si puede» = contestar: sí (aceptar) o no (rechazar). Tú eliges, pero con la razón."},
 {"q": "desearle buen viaje;", "f": "des", "o": ["Desear algo bueno", "Felicitar", "Proponer"], "why": "El viaje todavía no ha empezado: deseas algo bueno (¡Que tengas buen viaje!)."},
 {"q": "explicarle por qué no contestó antes;", "f": "dis", "o": ["Disculparse", "Rechazar con excusa", "Agradecer"], "why": "No contestaste: es algo que hiciste mal y ya pasó. Te disculpas (perdona por no contestar) y das la razón."},
]

# 2. ¿Que frase escribes? ctx = la situacion; t = carril; o[0] = la buena.
P_FRASE = [
 {"ctx": "Tu amiga Celia te ha regalado un libro de cocina.", "t": "tu", "f": "agr",
  "o": ["¡Muchas gracias por el libro! Ya he hecho dos recetas.", "Le agradezco mucho el libro, señora.", "¡Muchas gracias para el libro! Me encanta."],
  "why": "Con una amiga, de tú: gracias POR + lo que te ha dado y un detalle. «Le agradezco» es de usted y «gracias para» es un error."},
 {"ctx": "Escribes al hotel Mirador, que ha guardado la cartera que olvidaste.", "t": "us", "f": "agr",
  "o": ["Muchas gracias por guardar mi cartera. Son ustedes muy amables.", "¡Gracias por guardar mi cartera, sois geniales!", "Muchas gracias para guardar mi cartera."],
  "why": "A un hotel, de usted (ustedes): gracias por + infinitivo. La segunda es de amigos y la tercera lleva «para»."},
 {"ctx": "Tu hermano ha aprobado el examen de conducir.", "t": "tu", "f": "fel",
  "o": ["¡Enhorabuena por el carné! Ahora me llevas a la playa.", "¡Feliz cumpleaños! Ya puedes conducir.", "¡Que tengas buen viaje con el coche!"],
  "why": "Ha conseguido algo: ¡Enhorabuena por...! «Feliz cumpleaños» es para otra fiesta y «que tengas buen viaje» desea algo, no felicita."},
 {"ctx": "Tu amiga Nerea cumple treinta años el sábado.", "t": "tu", "f": "fel",
  "o": ["¡Felicidades, Nerea! ¡Feliz cumpleaños!", "¡Enhorabuena por tu cumpleaños, Nerea!", "¡Que te mejores, Nerea!"],
  "why": "El cumpleaños es una fiesta: ¡Felicidades! «Enhorabuena» es para algo que has conseguido."},
 {"ctx": "Quieres invitar a tu compañera de piso al teatro el viernes.", "t": "tu", "f": "inv",
  "o": ["¿Te apetece venir al teatro conmigo el viernes?", "¿Le apetece venir al teatro el viernes?", "¿Te apetece de venir al teatro el viernes?"],
  "why": "De tú: ¿te apetece + infinitivo?, sin «de». La segunda es de usted."},
 {"ctx": "Quieres invitar a tu vecino mayor, el señor Luna, a tomar un café en tu casa.", "t": "us", "f": "inv",
  "o": ["¿Quiere venir a tomar un café a mi casa esta tarde?", "¿Quieres venir a tomar un café a mi casa?", "Le invito venir a tomar un café a mi casa."],
  "why": "Con un vecino mayor, de usted: ¿quiere venir...? «Le invito venir» necesita «a»: le invito a tomar un café."},
 {"ctx": "Tu amigo no puede quedar el sábado. Propones otro día.", "t": "tu", "f": "pro",
  "o": ["¿Qué te parece si quedamos el domingo por la tarde?", "¿Por qué quedamos el domingo por la tarde?", "¿Qué le parece si quedamos el domingo?"],
  "why": "Proponer de tú: ¿qué te parece si + presente? «¿Por qué quedamos?» pregunta la causa (para proponer: ¿por qué NO...?)."},
 {"ctx": "Necesitas que tu amiga te deje su bici el lunes.", "t": "tu", "f": "ped",
  "o": ["¿Me puedes dejar tu bici el lunes? La mía tiene una rueda pinchada.", "¿Puedes me dejar tu bici el lunes?", "¿Podría dejarme su bici el lunes?"],
  "why": "El pronombre va delante del verbo conjugado (¿me puedes...?). La tercera es de usted."},
 {"ctx": "En la recepción de un hotel quieres saber a qué hora abre la piscina.", "t": "us", "f": "ped",
  "o": ["¿Podría decirme a qué hora abre la piscina?", "¿Me dices a qué hora abre la piscina?", "¿Puede me decir a qué hora abre la piscina?"],
  "why": "De usted, la fórmula educada: ¿podría + infinitivo? «¿Me dices?» es de tú y en la tercera el pronombre está en mal sitio."},
 {"ctx": "Tu amigo va a visitar Salamanca por primera vez.", "t": "tu", "f": "con",
  "o": ["Te recomiendo ir a la Plaza Mayor por la noche: es preciosa con las luces.", "Le recomiendo ir a la Plaza Mayor por la noche.", "Te recomiendo de ir a la Plaza Mayor por la noche."],
  "why": "De tú: te recomiendo + infinitivo, sin «de», y un porqué. La segunda es de usted."},
 {"ctx": "Tu compañera de trabajo tiene gripe y está en casa.", "t": "tu", "f": "des",
  "o": ["¡Que te mejores pronto! Aquí te esperamos.", "¡Que te mejoras pronto!", "¡Que se mejore pronto, señora!"],
  "why": "La frase fija es «¡Que te mejores!». La tercera es de usted, y a una compañera le hablas de tú."},
 {"ctx": "Su profesora de inglés, la señora Hall, se va de vacaciones a Japón.", "t": "us", "f": "des",
  "o": ["¡Que tenga muy buen viaje! Ya nos contará qué tal.", "¡Que tengas muy buen viaje! Ya me contarás.", "¡Que tiene muy buen viaje!"],
  "why": "De usted: ¡Que tenga buen viaje! La segunda es de tú y la tercera rompe la frase fija."},
 {"ctx": "Tu hermano te invita a ver el partido en su casa el domingo y te apetece.", "t": "tu", "f": "ace",
  "o": ["¡Claro que voy! ¿Llevo algo de picar?", "Sí.", "Con mucho gusto, señor Ortega."],
  "why": "Aceptar: sí, con alegría, y un detalle o una pregunta. Un «sí» solo es muy seco, y a tu hermano no le hablas de usted."},
 {"ctx": "Tu amiga te invita a una excursión el domingo, pero trabajas.", "t": "tu", "f": "rec",
  "o": ["¡Qué pena! El domingo no puedo: es que trabajo. ¿Vamos el próximo?", "No puedo.", "Lo siento mucho, pero no puedo, porque trabajo. Atentamente."],
  "why": "El no completo: la pena, el no, la excusa y otra propuesta. La segunda no da ninguna razón y la tercera termina de usted."},
 {"ctx": "No puede ir a la cita con la señora Duran para ver el piso que quiere alquilar.", "t": "us", "f": "dis",
  "o": ["Siento mucho no poder ir el martes. ¿Le parece bien el miércoles?", "Siento mucho no puedo ir el martes.", "Perdona, el martes no puedo, ¿vale?"],
  "why": "De usted: siento + infinitivo (no poder) y otra propuesta. La tercera es de tú."},
 {"ctx": "Ayer llegaste muy tarde a la cena de tu amiga.", "t": "tu", "f": "dis",
  "o": ["Perdona por llegar tan tarde ayer: es que había un atasco enorme.", "Perdona por llegué tan tarde ayer.", "Disculpe por llegar tan tarde ayer."],
  "why": "Perdona por + infinitivo (llegar) y la razón con «es que». «Disculpe» es de usted."},
]

E_BIENMAL = [  # ok 0 = bien, 1 = mal (con fix)
 {"q": "¡Enhorabuena por tu cumpleaños, Celia!", "ok": 1, "fix": "¡Felicidades, Celia! ¡Feliz cumpleaños!", "why": "Para el cumpleaños, ¡Felicidades! «Enhorabuena» es para algo que se consigue."},
 {"q": "Muchas gracias para las flores.", "ok": 1, "fix": "Muchas gracias por las flores.", "why": "Gracias POR lo que te han dado."},
 {"q": "Gracias por me ayudar con la mudanza.", "ok": 1, "fix": "Gracias por ayudarme con la mudanza.", "why": "Con el infinitivo, el pronombre va pegado detrás."},
 {"q": "Te invito cenar en mi casa el sábado.", "ok": 1, "fix": "Te invito a cenar en mi casa el sábado.", "why": "Te invito A + infinitivo."},
 {"q": "Siento no puedo ir a tu cumpleaños.", "ok": 1, "fix": "Siento no poder ir a tu cumpleaños.", "why": "Detrás de «siento», infinitivo."},
 {"q": "¡Que te mejoras pronto, Samu!", "ok": 1, "fix": "¡Que te mejores pronto, Samu!", "why": "La frase fija es «¡Que te mejores!»."},
 {"q": "¿Puedes me mandar las fotos?", "ok": 1, "fix": "¿Me puedes mandar las fotos?", "why": "El pronombre, delante del verbo conjugado o pegado al infinitivo (¿puedes mandarme...?)."},
 {"q": "Te recomiendo de probar el pulpo.", "ok": 1, "fix": "Te recomiendo probar el pulpo.", "why": "Te recomiendo + infinitivo, sin «de»."},
 {"q": "Me gustaría que vienes a mi graduación.", "ok": 1, "fix": "¿Quieres venir a mi graduación?", "why": "«Me gustaría que...» es de B1. En el A2, invita con una pregunta."},
 {"q": "Perdona por no he contestado antes.", "ok": 1, "fix": "Perdona por no contestar antes.", "why": "Detrás de «por», infinitivo."},
 {"q": "¿Por qué quedamos el viernes en la playa?", "ok": 1, "fix": "¿Por qué no quedamos el viernes en la playa?", "why": "Para proponer, ¿por qué NO...?"},
 {"q": "Espero que estás bien.", "ok": 1, "fix": "¿Qué tal estás?", "why": "«Espero que...» necesita una forma de B1. En el A2, pregunta: ¿Qué tal estás?"},
 {"q": "Muchas gracias por invitarme a la boda.", "ok": 0, "why": "Gracias por + infinitivo, con el pronombre pegado: perfecto."},
 {"q": "¡Que lo pases muy bien en las fiestas del pueblo!", "ok": 0, "why": "La frase fija de desear algo bueno, bien escrita."},
 {"q": "¿Me puedes ayudar el sábado con las cajas?", "ok": 0, "why": "El pronombre delante de «puedes»: bien."},
 {"q": "¡Qué pena! El viernes no puedo: es que tengo un examen.", "ok": 0, "why": "El no con su pena y su excusa: bien."},
 {"q": "¿Por qué no vamos al mercado el domingo?", "ok": 0, "why": "Proponer con «¿por qué no...?»: bien."},
 {"q": "¡Enhorabuena por el bebé! Me alegro mucho.", "ok": 0, "why": "El bebé es algo que han conseguido: ¡Enhorabuena!"},
 {"q": "Le recomiendo reservar la habitación pronto.", "ok": 0, "why": "Le recomiendo + infinitivo, de usted: bien."},
]

# Textos con huecos: [[buena|d1|d2#motivo]]. Cada motivo: (funcion, explicacion, respuestas buenas que admite).
MOTIVOS = {
 "agr_por": ("agr", "Agradecer mira atrás: gracias <b>por</b> + lo que pasó (nunca «para»).", ["muchas gracias por", "gracias por"]),
 "agr_us": ("agr", "Agradecer de usted: le agradezco.", ["le agradezco"]),
 "dis_tu": ("dis", "Disculparse con un amigo: perdona; de usted, perdone o disculpe.", ["perdona"]),
 "dis_us": ("dis", "Disculparse de usted: siento mucho + infinitivo.", ["siento mucho"]),
 "fel_enh": ("fel", "Algo que ha conseguido: ¡Enhorabuena! (¡Felicidades! es para las fiestas).", ["enhorabuena"]),
 "inv_tu": ("inv", "Invitar con un amigo: te invito (a algo, a + infinitivo).", ["te invito"]),
 "pro_si": ("pro", "Proponer: ¿qué te parece si + presente? / ¿por qué no...? (sin «no» preguntas la causa).", ["¿qué te parece si", "¿por qué no"]),
 "pro_ysi": ("pro", "Proponer: ¿y si + presente?", ["¿y si"]),
 "ped_pron": ("ped", "Pedir: el pronombre delante del verbo conjugado: ¿me puedes...?", ["¿me puedes mandar", "me puedes mandar", "me puedes llamar"]),
 "ped_us": ("ped", "Pedir de usted: ¿podría + infinitivo?", ["¿podría decirme"]),
 "con_rec": ("con", "Consejo: te recomiendo + infinitivo (sin «de»).", ["te recomiendo"]),
 "con_tener": ("con", "Consejo: tienes que + infinitivo (de usted, tiene que).", ["tienes que"]),
 "des_que": ("des", "Desear: frases fijas con «que»: ¡que tengas buen viaje!, ¡que tenga un buen día!", ["¡que tengas", "¡que tenga"]),
 "des_suerte": ("des", "Antes de algo difícil: ¡Mucha suerte! (¡Enhorabuena! es después, si sale bien).", ["¡mucha suerte!"]),
 "ace_mas": ("ace", "Aceptar: sí, con alegría y del mismo carril (un «sí» solo es muy seco).", ["¡claro que sí!", "me parece muy bien"]),
 "rec_pero": ("rec", "Decir que no empieza con la pena: ¡qué pena!", ["¡qué pena!"]),
 "rec_esque": ("rec", "La excusa con un amigo: es que.", ["es que"]),
 "rec_porque": ("rec", "La excusa de usted: porque.", ["porque"]),
}

TEXTOS = [
 {"id": "t1", "t": "tu", "tipo": "Correo a un amigo", "titulo": "Celia contesta a Gael",
  "texto": "¡Hola, Gael!\n¡[[Enhorabuena|Felicidades por tu cumpleaños|Que te mejores#fel_enh]] por el trabajo en Oporto! Me alegro muchísimo por ti. Y [[gracias por|gracias para|perdona por#agr_por]] la invitación a tu cena de despedida.\n[[¡Qué pena!|¡Qué buena idea!|¡Claro que sí!#rec_pero]] El viernes 12 no puedo ir: [[es que|por eso|además#rec_esque]] tengo que trabajar hasta las once. [[Perdona|Perdone|Gracias#dis_tu]], de verdad.\n[[¿Qué te parece si|¿Qué le parece si|¿Por qué#pro_si]] comemos juntos el domingo 14? Y [[te recomiendo|te recomiendo de|le recomiendo#con_rec]] llevar un buen paraguas a Oporto: allí llueve mucho en invierno.\n[[¡Que tengas|¡Que tienes|¡Que tenga#des_que]] muy buen viaje!\nUn abrazo,\nCelia"},
 {"id": "t2", "t": "us", "tipo": "Correo de usted", "titulo": "Íñigo escribe a la academia de pintura",
  "texto": "Estimada señora Soler:\n[[Muchas gracias por|Muchas gracias para|Gracias por me#agr_por]] su correo y por la plaza en el curso de los sábados. [[Me parece muy bien|Sí.|¡Me apunto, guapa!#ace_mas]] empezar el 3 de febrero.\n[[Siento mucho|Perdona por|Enhorabuena por#dis_us]] no poder ir a la reunión del viernes, [[porque|es que|por eso#rec_porque]] ese día tengo que trabajar hasta tarde.\n[[¿Podría decirme|¿Puedes decirme|¿Puede me decir#ped_us]] qué materiales tengo que llevar a la primera clase? [[Le agradezco|Te agradezco|Agradezco para#agr_us]] mucho su ayuda.\n[[¡Que tenga|¡Que tengas|¡Que tiene#des_que]] un buen fin de semana.\nUn saludo,\nÍñigo Sanz"},
 {"id": "t3", "t": "tu", "tipo": "Mensaje a un amigo", "titulo": "Lidia escribe a Jaime antes de su entrevista",
  "texto": "¡Hola, Jaime!\nMañana es tu entrevista en Bilbao, ¿no? [[¡Mucha suerte!|¡Enhorabuena!|¡Felicidades!#des_suerte]] Seguro que sale muy bien. [[Te recomiendo|Le recomiendo|Te recomiendo de#con_rec]] llegar diez minutos antes y [[tienes que|tiene que|tienes de#con_tener]] llevar el currículum en papel.\nAh, ¿[[me puedes llamar|puedes me llamar|me podría llamar#ped_pron]] después? Quiero saber qué tal.\n[[¿Por qué no|¿Por qué|¿Qué le parece si#pro_si]] cenamos el viernes para celebrarlo? Yo [[te invito|le invito|te invito de#inv_tu]].\nUn beso,\nLidia"},
 {"id": "t4", "t": "tu", "tipo": "Diálogo de la tarea 3", "titulo": "Un sábado con la sobrina",
  "texto": "EXAMINADOR: El sábado viene mi sobrina Ana, de diez años. ¿Qué podemos hacer con ella?\nCANDIDATO: [[¿Qué te parece si|¿Qué le parece si|¿Por qué#pro_si]] vamos al zoo? A los niños les encanta.\nEXAMINADOR: ¡Buena idea! ¿Vienes tú también?\nCANDIDATO: [[¡Claro que sí!|Sí.|Con mucho gusto, señor.#ace_mas]] Me apetece mucho ver los elefantes.\nEXAMINADOR: Y por la tarde, ¿vamos al cine los tres?\nCANDIDATO: [[¡Qué pena!|¡Qué buena idea!|¡Enhorabuena!#rec_pero]] Por la tarde no puedo: [[es que|además|por eso#rec_esque]] tengo clase de inglés. [[¿Y si|¿Y por qué|¿Le parece si#pro_ysi]] vamos el domingo?\nEXAMINADOR: Perfecto. Ah, mi sobrina es un poco tímida.\nCANDIDATO: No pasa nada. [[Tienes que|Tiene que|Tienes de#con_tener]] dejarla elegir los animales: así está más contenta. ¿[[Me puedes mandar|Puedes me mandar|Me podría mandar#ped_pron]] una foto de ella?"},
]

# ------------------------------------------------------------------ AHORA TU: ESCRITURA
# Cada pauta: (texto, [grupos]); un grupo "a|b" se cumple con cualquiera de esas funciones. Sin grupos = no se mira.
LAMINAS = [
 {"id": "vanesa", "t": "tu", "tarea": "Tarea 1 · correo a una amiga", "intro": "Su amiga Vanesa le escribe este correo:",
  "mensaje": "¡Hola! ¡Tengo una noticia buenísima! Me han dado una beca y en enero me voy seis meses a estudiar a Lisboa. Antes de irme, el sábado 20, hago una cena de despedida en mi casa. ¿Vienes? Besos, Vanesa",
  "consigna": "Conteste a Vanesa. En el correo tiene que:",
  "pautas": [("saludar y felicitarla por la beca;", ["fel"]), ("decir si puede ir a la cena y por qué;", ["ace|rec"]),
             ("darle un consejo para su vida en Lisboa;", ["con"]), ("pedirle algo de Lisboa o proponerle una visita;", ["ped|pro"]),
             ("desearle buen viaje y despedirse.", ["des"])],
  "palabras": [60, 70]},
 {"id": "medina", "t": "us", "tarea": "Tarea 1 · correo de usted", "intro": "Usted ha recibido este correo de la asociación de vecinos de su barrio:",
  "mensaje": "Estimado vecino: El sábado 14 celebramos los veinte años de la asociación con una comida en la plaza, a las dos. Nos gustaría contar con usted. ¿Puede ayudarnos con las mesas por la mañana? Un saludo, Elvira Medina",
  "consigna": "Conteste a la señora Medina. En el correo tiene que:",
  "pautas": [("saludar y agradecer la invitación;", ["agr"]), ("decir si puede ir a la comida y por qué;", ["ace|rec"]),
             ("contestar si puede ayudar por la mañana (si no puede, disculparse);", ["ace|rec|dis"]),
             ("pedir información sobre la comida (qué hay que llevar, el precio...);", ["ped"]),
             ("desearle una buena fiesta y despedirse.", ["des"])],
  "palabras": [60, 70]},
]

# ------------------------------------------------------------------ DETECTOR (sin tildes, minusculas)
# t: r = rojo (error seguro) / a = ambar (mira esto). sc: s = frase a frase / x = el texto entero.
DETECTOR = [
 {"id": "enh", "t": "r", "sc": "s", "re": r"\benhorabuena\b[^.!?]{0,25}\b(cumpleanos|cumple|santo|navidad)\b",
  "msg": "Para el cumpleaños, el santo o la Navidad: <b>¡Felicidades!</b> «Enhorabuena» es para algo que se consigue."},
 {"id": "para", "t": "r", "sc": "s", "re": r"\bgracias para\b", "msg": "Se dice <b>gracias por</b>: agradecer mira atrás, a lo que pasó."},
 {"id": "porpron", "t": "r", "sc": "s", "re": r"\b(gracias|perdona|perdone|perdon|disculpa|disculpe) por (no )?(me|te|le|nos|os) [a-z]+(ar|er|ir)\b",
  "msg": "Con el infinitivo, el pronombre va pegado detrás: <b>gracias por invitarme</b>, <b>perdona por no llamarte</b>."},
 {"id": "porconj", "t": "r", "sc": "s", "re": r"\b(gracias|perdona|perdone|perdon|disculpa|disculpe) por (no )?(he|has|ha|hemos|habeis|han|puedo|pude|voy|fui|escribo|escribi|contesto|conteste|llegue|vienes|viniste|vino|invitas|invitaste|ayudas|ayudaste)\b",
  "msg": "Detrás de <b>por</b> va el infinitivo: <i>perdona por no contestar</i>, <i>gracias por venir</i>."},
 {"id": "siento", "t": "r", "sc": "s", "re": r"\bsiento (mucho )?no (puedo|pude|voy|podre)\b", "msg": "Detrás de <b>siento</b>, infinitivo: <b>siento no poder ir</b>."},
 {"id": "invito", "t": "r", "sc": "s", "re": r"\b(te|le|os|les) invito (venir|ir|comer|cenar|tomar|pasar|celebrar|ver|bailar)\b|\binvitar(te|le|os) (venir|ir|comer|cenar)\b",
  "msg": "Se invita <b>a</b> algo: <b>te invito a cenar</b>, <b>le invito a venir</b>."},
 {"id": "deseo", "t": "r", "sc": "s", "re": r"\bque (te mejoras|se mejora|os mejorais|lo pasas|lo pasais|tienes (un )?buen viaje|tiene (un )?buen viaje|aprovecha)\b",
  "msg": "Las frases de desear algo bueno son fijas: <b>¡Que te mejores!</b>, <b>¡Que lo pases bien!</b>, <b>¡Que tengas buen viaje!</b> (de usted: <i>se mejore, lo pase, tenga</i>)."},
 {"id": "puedes", "t": "r", "sc": "s", "re": r"\b(puedes|puede|podria) (me|te|le|nos) [a-z]+(ar|er|ir)\b",
  "msg": "El pronombre va delante del verbo conjugado o pegado al infinitivo: <b>¿me puedes ayudar?</b> o <b>¿puedes ayudarme?</b>"},
 {"id": "de", "t": "r", "sc": "s", "re": r"\b(recomiendo|apetece) de\b", "msg": "Sin «de»: <b>te recomiendo ir</b>, <b>¿te apetece venir?</b>"},
 {"id": "gustq", "t": "r", "sc": "s", "re": r"\bme gustaria que\b", "msg": "«Me gustaría que...» necesita una forma de B1. En el A2: <b>me gustaría + infinitivo</b> (me gustaría verte) o una pregunta (<i>¿quieres venir?</i>)."},
 {"id": "espero", "t": "a", "sc": "s", "re": r"\bespero que\b", "msg": "«Espero que...» necesita una forma de B1. En el A2 es más seguro <b>¿Qué tal estás?</b> o <b>Espero verte pronto</b>."},
 {"id": "porque", "t": "a", "sc": "s", "re": r"\bpor que (vamos|quedamos|hacemos|comemos|cenamos|salimos|nos vemos)\b",
  "msg": "¿Propones algo? Entonces es <b>¿por qué no...?</b> Sin «no», preguntas la causa."},
 {"id": "deb", "t": "a", "sc": "s", "re": r"\bdeberias?\b|\byo que tu\b", "msg": "Es correcto, pero no lo necesitas en el A2: <b>tienes que</b>, <b>es mejor</b> o <b>te recomiendo</b> + infinitivo."},
 {"id": "sinexc", "t": "a", "sc": "x", "re": r"^(?!(?:.|\n)*\b(porque|es que|tengo que|tengo (un|una|mi|el|la|clase|turno|cita)|trabajo|estoy|ese dia|voy a|me voy)\b)(?:.|\n)*\bno (puedo|voy a poder|podre)\b",
  "msg": "Dices que no puedes, pero no veo la excusa (<i>es que...</i>, <i>porque...</i>). Si ya la has escrito con otras palabras, no pasa nada."},
]
REQ = [d["id"] for d in DETECTOR if d["id"] != "deb"]  # «deberias» no es un error: solo un aviso de nivel

DETECTOR_PRUEBAS = [
 ("¡Enhorabuena por tu cumpleaños!", ["enh"]),
 ("Muchas gracias para el regalo.", ["para"]),
 ("Gracias por me invitar a la fiesta.", ["porpron"]),
 ("Perdona por no te llamar ayer.", ["porpron"]),
 ("Perdona por no he contestado.", ["porconj"]),
 ("Gracias por vienes a mi casa.", ["porconj"]),
 ("Siento mucho no puedo ir.", ["siento", "sinexc"]),
 ("Te invito venir el sábado. Es que es mi santo.", ["invito"]),
 ("¡Que te mejoras pronto!", ["deseo"]),
 ("¡Que tienes buen viaje!", ["deseo"]),
 ("¿Puedes me ayudar?", ["puedes"]),
 ("¿Podría me decir el precio?", ["puedes"]),
 ("Te recomiendo de visitar el castillo.", ["de"]),
 ("Me gustaría que vienes.", ["gustq"]),
 ("Espero que estás bien.", ["espero"]),
 ("¿Por qué quedamos el sábado?", ["porque"]),
 ("Deberías descansar más.", ["deb"]),
 ("No puedo ir a tu cena.", ["sinexc"]),
 # no deben saltar
 ("¡Felicidades! ¡Enhorabuena por el trabajo nuevo!", []),
 ("Muchas gracias por invitarme a tu boda.", []),
 ("Perdona por no llamarte ayer: es que llegué tarde.", []),
 ("Siento no poder ir, porque trabajo.", []),
 ("Te invito a cenar el viernes.", []),
 ("¡Que te mejores! ¡Que lo pases bien! ¡Que tenga buen viaje!", []),
 ("Es un hotel que tiene un buen desayuno.", []),
 ("¿Me puedes ayudar? ¿Puedes ayudarme?", []),
 ("Le recomiendo reservar pronto.", []),
 ("Me gustaría saber el precio. Me gustaría verte.", []),
 ("¿Por qué no quedamos el sábado?", []),
 ("¿Por qué vienes tan tarde?", []),
 ("El domingo no puedo: es que tengo la boda de mi prima.", []),
 ("No puedo ir, porque estoy enferma.", []),
 ("Gracias por todo. Gracias por la ayuda.", []),
 ("Lo siento mucho, pero el jueves no puedo, porque trabajo.", []),
]

# ------------------------------------------------------------------ AHORA TU: ORAL (responde rapido)
ORAL = [
 {"sit": "Tu amigo te ha dejado su coche todo el fin de semana.", "f": "agr", "t": "tu", "m": "Muchas gracias por dejarme el coche. ¡Me has salvado el fin de semana!"},
 {"sit": "La recepcionista del hotel le ha pedido un taxi para las seis de la mañana.", "f": "agr", "t": "us", "m": "Muchas gracias por su ayuda. Es usted muy amable."},
 {"sit": "Llegas media hora tarde al cine. Tu amiga te espera en la puerta.", "f": "dis", "t": "tu", "m": "¡Perdona por llegar tan tarde! Es que el metro se ha parado."},
 {"sit": "No puede ir a la cita del dentista y llama a la clínica.", "f": "dis", "t": "us", "m": "Siento mucho no poder ir mañana, porque tengo que trabajar. ¿Podría cambiarme la cita?"},
 {"sit": "Tu compañero de piso ha terminado la carrera.", "f": "fel", "t": "tu", "m": "¡Enhorabuena por terminar la carrera! Esta noche lo celebramos."},
 {"sit": "Su vecina, la señora Pons, cumple noventa años.", "f": "fel", "t": "us", "m": "¡Felicidades, señora Pons! ¡Feliz cumpleaños! Está usted estupenda."},
 {"sit": "Quieres llevar a tu amiga a una exposición de fotos el domingo.", "f": "inv", "t": "tu", "m": "¿Te apetece venir conmigo a una exposición de fotos el domingo? Es gratis."},
 {"sit": "Quiere invitar a su profesora de español a la cena de fin de curso.", "f": "inv", "t": "us", "m": "Nos gustaría invitarle a la cena de fin de curso. ¿Quiere venir el viernes?"},
 {"sit": "Tu amigo quiere ir a la playa el sábado, pero va a llover.", "f": "pro", "t": "tu", "m": "¿Por qué no vamos al cine el sábado? Y el domingo, si hace sol, vamos a la playa."},
 {"sit": "El técnico de la lavadora quiere venir el lunes por la mañana, pero usted trabaja.", "f": "pro", "t": "us", "m": "¿Le parece bien el lunes por la tarde? Por la mañana no estoy en casa."},
 {"sit": "Necesitas un cargador y tu compañera de clase tiene uno.", "f": "ped", "t": "tu", "m": "¿Me dejas tu cargador un momento? Me queda muy poca batería."},
 {"sit": "En la estación quiere saber de qué andén sale el tren a Valencia.", "f": "ped", "t": "us", "m": "Perdone, ¿podría decirme de qué andén sale el tren a Valencia?"},
 {"sit": "Tu amigo empieza a correr y le duelen mucho las piernas.", "f": "con", "t": "tu", "m": "Tienes que empezar despacio: diez minutos al día y después más."},
 {"sit": "Un turista le pregunta qué plato típico puede probar en su ciudad.", "f": "con", "t": "us", "m": "Le recomiendo probar el arroz a banda: es muy típico aquí."},
 {"sit": "Tu prima se va mañana dos semanas a Japón.", "f": "des", "t": "tu", "m": "¡Que tengas muy buen viaje! Mándame fotos."},
 {"sit": "Su compañero de trabajo, el señor Vera, está enfermo en casa.", "f": "des", "t": "us", "m": "¡Que se mejore pronto, señor Vera! Aquí le esperamos."},
 {"sit": "Tu hermano te invita a ver el partido en su casa el domingo.", "f": "ace", "t": "tu", "m": "¡Claro que voy! ¿Llevo algo de picar?"},
 {"sit": "La empleada del banco le propone firmar los papeles el jueves a las diez.", "f": "ace", "t": "us", "m": "Me parece muy bien. El jueves a las diez estoy allí."},
 {"sit": "Tu amiga te invita a correr el sábado a las siete de la mañana.", "f": "rec", "t": "tu", "m": "¡Qué pena! El sábado no puedo: es que trabajo por la mañana. ¿Vamos el domingo?"},
 {"sit": "Su jefa le invita a un curso de formación el sábado.", "f": "rec", "t": "us", "m": "Lo siento mucho, pero el sábado no puedo, porque tengo una boda familiar."},
]

# Formas de B1 que no pueden salir en nada de lo que la ficha da por bueno (fuera de LOS_VERAS).
B1_RX = (r"\bespero que\b|\bdeberias?\b|\byo que tu\b|\bme gustaria que\b|\bojala\b|\bque (vengas|vinieras|puedas|estes|disfrutes|te vaya)\b"
         r"|\b(se|me|te) (lo|la|los|las) (mando|doy|traigo|dejo|agradezco)\b|\bpodriamos\b|\bpodrias\b")
