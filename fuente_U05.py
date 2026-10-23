# -*- coding: utf-8 -*-
# FUENTE DE LA UNIDAD 5 (fase 1) · ¿Cómo va todo?
# Rotación U05: lectura T1 (correo) + T4 (texto largo) · auditiva T1 (imágenes) + T4 (mensajes) · mitad de tiempo
U = "05"
TITLE = "¿Cómo va todo?"
MES_WP = "2026/10"   # carpeta del mes en que se suben audios e imágenes a WordPress (cambiar si se suben otro mes)
RECORDATORIO = [
 "Saludar, despedirse y presentar a alguien en situaciones formales e informales: ¿Qué tal? / ¿Cómo está usted?; Te presento a... / Le presento a...; Me tengo que ir; Cuídate / Cuídese; Recuerdos a tu familia; Hasta la próxima; dos besos o dar la mano.",
 "Agradecer y responder (Muchas gracias, te lo agradezco / De nada, no hay de qué) e interesarse por alguien: ¿Y la familia, qué tal?",
 "Tú y usted: con quién se usa cada uno (amigos, familia y compañeros / personas mayores, desconocidos y situaciones formales).",
 "Pedir cosas, acciones y favores: ¿Me dejas...?, ¿Me pasas...?, ¿Me pones...?, ¿Puedes...?, ¿Podrías...?, ¿Te importa...? Y los verbos dar, dejar, prestar, poner, pasar y tener.",
 "Pedir y dar permiso (¿Puedo...?, ¿Te importa si...?: Sí, claro / Es que...) y dar excusas: Lo siento, es que...; Me encantaría, pero...",
 "Estar + gerundio para acciones que pasan ahora (estoy trabajando, está durmiendo) y gerundios irregulares: durmiendo, pidiendo, diciendo, leyendo, yendo.",
]
TIPS_INICIO = [
 "<b>Lectura, tarea 1:</b> en un correo personal la primera pregunta casi siempre es «¿para qué escribe?». Lee todo el correo antes de contestarla: una excusa o un favor pueden estar al principio y al final.",
 "<b>Auditiva, tarea 1:</b> las tres imágenes aparecen en la conversación. Cuando alguien pide algo, escucha la respuesta: «Es que...» o «Lo siento» significan casi siempre que no.",
]
CATS = {
 "saludos": {"name": "Saludar, despedirse, presentar y agradecer",
  "repaso": "Saludar: ¡Hola! ¿Qué tal? ¿Cómo va todo? ¡Cuánto tiempo! / Buenos días, ¿cómo está usted? Presentar: Te presento a Ana / Le presento al señor Gil; Encantado/a, Mucho gusto, Igualmente. Interesarse: ¿Y la familia, qué tal? Despedirse: Bueno, me tengo que ir; Hablamos; Hasta la próxima; Cuídate / Cuídese; Recuerdos a tu familia; De tu / su parte. Agradecer: Muchas gracias, te lo agradezco / De nada, no hay de qué. En España, dos besos entre amigos y compañeros; la mano en situaciones formales. En el libro: unidad 5, situaciones de contacto social.",
  "reto": "Escribe dos presentaciones: una de un amigo a tu familia (tú) y una de tu jefe a un cliente (usted)."},
 "tuusted": {"name": "Tú y usted: niveles de formalidad",
  "repaso": "Tú con amigos, familia, compañeros y gente joven; usted con personas mayores que no conoces, en el banco, en el médico o con clientes. Usted va con el verbo en tercera persona: ¿Puede usted...?, Perdone, Siéntese. En el libro: unidad 5, situaciones formales e informales.",
  "reto": "Escribe la misma petición dos veces: a un amigo (tú) y a una señora mayor en el autobús (usted)."},
 "pedir": {"name": "Pedir cosas, acciones y favores (dar, dejar, prestar, pasar, poner)",
  "repaso": "Objetos: ¿Me dejas tu boli?, ¿Me prestas el coche?, ¿Me pasas la sal?, ¿Me pones un café?, ¿Tienes un cargador? Acciones y favores: ¿Puedes ayudarme?, ¿Podrías...?, ¿Te importa + infinitivo? Más cortés con podrías y te importaría. El pronombre va delante o detrás: ¿me puedes ayudar? / ¿puedes ayudarme? En el libro: unidad 5, pedir cosas, acciones y favores.",
  "reto": "Pide tres cosas a un compañero de piso: un objeto, una acción y un favor grande."},
 "permiso": {"name": "Pedir y dar permiso (¿Puedo...?, ¿Te importa si...?)",
  "repaso": "Pedir: ¿Puedo abrir la ventana?, ¿Te importa si abro la ventana? (si + presente). Dar permiso: Sí, claro; Claro, claro; Por supuesto. No darlo con cortesía: Es que... / Lo siento, pero... En el libro: unidad 5, pedir y conceder permiso.",
  "reto": "Escribe tres preguntas para pedir permiso en clase, en un tren y en casa de un amigo, con su respuesta."},
 "excusas": {"name": "Dar excusas y justificar (es que..., lo siento, pero...)",
  "repaso": "Para decir que no o explicar algo: Lo siento, es que tengo que trabajar; Me encantaría, pero no puedo; Perdona, es que se me olvidó. En España un no sin explicación suena mal: casi siempre se da una excusa. En el libro: unidad 5, dar excusas y justificar.",
  "reto": "Un amigo te invita a una cena el viernes. Escribe dos respuestas para decir que no, con una excusa diferente en cada una."},
 "gerundio": {"name": "Estar + gerundio (acciones en desarrollo)",
  "repaso": "Estar en presente + gerundio: estoy trabajando, está lloviendo, estamos comiendo. Regulares: -ar > -ando; -er, -ir > -iendo. Irregulares: dormir > durmiendo, pedir > pidiendo, decir > diciendo, leer > leyendo, ir > yendo, oír > oyendo. En el libro: unidad 5, el gerundio y estar + gerundio. Repasa también la píldora de gramática «Estar + gerundio» (teoría y ejercicios) que te da tu profesora.",
  "reto": "Son las ocho de la tarde: escribe qué está haciendo ahora cada persona de tu casa."},
}
ESTRATEGIAS_NUEVAS = {}

# ---------------- LECTURA ----------------
CL1 = {"n": 1, "type": "mail",
 "instr": "Usted va a leer el correo electrónico que Clara ha escrito a su amigo Pablo. A continuación, conteste a las preguntas (de la 1 a la 5). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 12 minutos. Lee las preguntas antes del correo. Cuando Clara pide algo, fíjate en para qué lo necesita y para cuándo.",
 "head": ["De: Clara", "Para: Pablo", "Asunto: ¡Perdona! Y... ¿me haces un favor?"],
 "body": [
  "Hola, Pablo:",
  "¿Cómo va todo? Primero, perdóname por no ir a tu cumpleaños el sábado. Es que mi hermana tuvo un niño el viernes y me fui a Zaragoza para conocerlo. ¡Se llama Leo y es precioso! Volví ayer por la noche, muy cansada pero muy feliz. Ya sé que no es una excusa normal, pero de verdad que lo siento mucho. Marta me contó que la fiesta fue genial.",
  "Te estoy escribiendo desde el tren. Estoy volviendo a casa y estoy pensando en la semana que viene, porque tengo un problema y necesito tu ayuda. Mis padres vienen a pasar unos días conmigo y llegan el miércoles a las once de la noche a la estación de autobuses. Pero mi coche está en el taller hasta el lunes. ¿Te importaría prestarme el tuyo esa noche? Te lo devuelvo el jueves temprano, con el depósito lleno, claro.",
  "Otra cosa: ¿me puedes dejar también tu cama plegable? En mi piso solo hay una cama de invitados, y mis padres prefieren dormir separados porque mi padre ronca muchísimo. Si no puedes, no pasa nada, ¿eh? Se la pido a mi vecina Rosa.",
  "Por cierto, ¿qué tal con tu nueva jefa? En tu último mensaje me dices que es muy seria y que en la oficina todos le hablan de usted. ¡Qué raro! En mi empresa nos hablamos de tú todos, también con el director.",
  "Te invito a cenar el viernes en el italiano de tu calle para darte las gracias... y tu regalo de cumpleaños.",
  "Dale recuerdos a tu familia de mi parte.",
  "Un abrazo,<br>Clara"],
 "items": [
  {"n": 1, "q": "Clara escribe a Pablo para...", "o": ["contarle cómo fue la fiesta de su cumpleaños.", "pedirle perdón y pedirle ayuda.", "invitarlo a conocer a su sobrino."], "ok": 1,
   "cats": ["excusas", "pedir"], "es": "ES-02", "pc": "FN-5.4 disculparse · FN-4.2 pedir favores",
   "why": "Clara se disculpa por no ir al cumpleaños y le pide el coche y la cama. Ella no fue a la fiesta (se la contó Marta), y a Leo lo conoció ella en Zaragoza."},
  {"n": 2, "q": "Clara no fue al cumpleaños de Pablo porque...", "o": ["fue a ver a su familia a Zaragoza.", "tuvo que trabajar ese día.", "tuvo un problema con el coche."], "ok": 0,
   "cats": ["excusas"], "es": "ES-03", "pc": "FN-5.4 justificar (es que...) · GR indefinido (U02)",
   "why": "Su hermana tuvo un niño y Clara se fue a Zaragoza para conocerlo. No habla de trabajo, y el problema del coche es para la semana que viene, no para el sábado."},
  {"n": 3, "q": "Clara necesita el coche de Pablo para...", "o": ["ir a trabajar el jueves.", "recoger a sus padres.", "llevar su coche al taller."], "ok": 1,
   "cats": ["pedir"], "es": "ES-03", "pc": "FN-4.2 · ¿Te importaría + infinitivo? (GR-15) · prestar",
   "why": "Sus padres llegan el miércoles por la noche a la estación de autobuses y su coche está en el taller. El jueves es cuando le devuelve el coche a Pablo."},
  {"n": 4, "q": "Según el correo, los padres de Clara...", "o": ["llegan a la ciudad en tren.", "van a dormir en casa de Rosa.", "no quieren dormir en la misma cama."], "ok": 2,
   "cats": ["pedir"], "es": "ES-04", "pc": "dejar / pedir objetos · prefieren + infinitivo",
   "why": "Prefieren dormir separados porque el padre ronca: por eso Clara necesita otra cama. Llegan en autobús (el tren es de Clara) y Rosa es la vecina que puede dejar una cama, no la casa."},
  {"n": 5, "q": "En la empresa de Clara...", "o": ["todos se tratan de tú.", "la jefa es muy seria.", "hablan de usted al director."], "ok": 0,
   "cats": ["tuusted"], "es": "ES-08", "pc": "tú / usted · LX-07 trabajo",
   "why": "«Nos hablamos de tú todos, también con el director» = todos se tratan de tú. La jefa seria y el usted son de la oficina de Pablo."},
 ]}

CL4 = {"n": 4, "type": "long",
 "instr": "Usted va a leer un texto de un blog en el que una mujer alemana cuenta su primer año en España. A continuación, conteste a las preguntas (de la 20 a la 25). Seleccione la opción correcta (A, B o C).",
 "tip": "Tienes unos 18 minutos. Las preguntas siguen el orden del texto. Fíjate en quién hace cada cosa: Hanna, su jefe, Rocío, Javier o la abuela.",
 "title": "«¿Me pones un café?»: mi primer año en Sevilla",
 "sub": "Blog «Vivir en España», de Hanna Becker",
 "body": [
  "Me llamo Hanna, soy alemana y vivo en Sevilla desde hace un año. Trabajo como ingeniera en una empresa de energía solar. Antes de venir, estudié español tres años en Múnich, pero aquí aprendí algo importante: las palabras no son lo más difícil. Lo más difícil son las costumbres.",
  "Primero, los saludos. El primer día en la oficina, mi jefe me presentó a mis compañeros, y una compañera, Rocío, se acercó y me dio dos besos. Yo me quedé quieta, con la mano preparada para saludar. ¡Qué vergüenza! Ahora ya sé que entre amigos y compañeros lo normal son los dos besos, y que dar la mano es más formal, por ejemplo en una reunión con clientes.",
  "Después, el tú y el usted. En mis clases de Múnich siempre usamos usted con la profesora, así que en la oficina yo hablé de usted a todo el mundo, también a mi jefe. Al final de la primera semana, él me dijo riéndose: «Hanna, por favor, háblame de tú, que no soy tan mayor». Hoy uso usted solo con personas mayores o en situaciones formales, como en el banco o en el médico.",
  "Pero lo más curioso para mí es cómo se piden las cosas. En Alemania, en un bar, pedimos algo como «¿Podría traerme un café, por favor?». Aquí la gente dice «¿Me pones un café?» o simplemente «Un café, por favor», y nadie piensa que es maleducado. Los primeros meses yo pedí siempre con «podría», y un camarero me dijo, muy simpático: «¡Qué educada! ¿Eres profesora de español?». Ahora pido como todo el mundo, aunque a veces todavía se me escapa un «podría».",
  "Con las invitaciones también aprendí mucho. Un día, unos compañeros me invitaron a cenar y yo contesté: «No, gracias, no quiero ir». ¡Silencio total! Nadie dijo nada. Después, mi compañero Javier me explicó que en España, para decir que no, normalmente das una excusa: «Lo siento, es que ya tengo planes» o «Me encantaría, pero hoy no puedo».",
  "Ahora, después de un año, me siento como en casa. Estoy aprendiendo a bailar flamenco con Rocío y muchos domingos como con su familia. Su abuela todavía me llama «la alemana», pero ya me saluda con dos besos... y yo a ella también. Mis amigos de Múnich no lo entienden, pero yo ya no sé saludar de otra manera."],
 "items": [
  {"n": 20, "q": "Según Hanna, al llegar a España...", "o": ["las costumbres le parecieron más difíciles que el idioma.", "tuvo problemas sobre todo con el idioma.", "empezó un curso de español."], "ok": 0,
   "cats": ["saludos"], "es": "ES-03", "pc": "comparar (más difícil que) · LX-06",
   "why": "«Las palabras no son lo más difícil. Lo más difícil son las costumbres.» Estudió español antes, en Múnich, no al llegar."},
  {"n": 21, "q": "El primer día en la oficina...", "o": ["Hanna dio dos besos a todos sus compañeros.", "su jefe la saludó con dos besos.", "una compañera la saludó de una forma que Hanna no esperaba."], "ok": 2,
   "cats": ["saludos"], "es": "ES-08", "pc": "FN-5.1 saludar · FN-5.2 presentar · dos besos / dar la mano",
   "why": "Rocío le dio dos besos y Hanna, sorprendida, tenía la mano preparada. Hanna no dio besos, y el jefe solo la presentó."},
  {"n": 22, "q": "La primera semana en la oficina, Hanna...", "o": ["habló de tú solo a sus compañeros.", "habló de usted también a su jefe.", "no habló con su jefe."], "ok": 1,
   "cats": ["tuusted"], "es": "ES-07", "pc": "tú / usted · GR indefinido (U02) · imperativo con pronombre (háblame)",
   "why": "Hanna habló de usted a todo el mundo, también a su jefe, y por eso él le pidió el tú. No usó el tú con nadie esa semana."},
  {"n": 23, "q": "Según Hanna, en los bares españoles...", "o": ["la gente pide las cosas de forma muy directa.", "es maleducado pedir sin decir «por favor».", "los camareros siempre usan «podría»."], "ok": 0,
   "cats": ["pedir"], "es": "ES-04", "pc": "¿Me pones...? · fórmulas de cortesía (GR-15)",
   "why": "La gente dice «¿Me pones un café?» o «Un café, por favor», y nadie lo ve maleducado. Quien usaba «podría» era Hanna, no los camareros."},
  {"n": 24, "q": "Cuando Hanna dijo que no a la invitación a cenar...", "o": ["sus compañeros se rieron.", "Javier la invitó otra vez.", "nadie contestó nada."], "ok": 2,
   "cats": ["excusas"], "es": "ES-03", "pc": "FN-4.5 rechazar con excusa (es que..., me encantaría, pero...)",
   "why": "«¡Silencio total! Nadie dijo nada.» Javier le explicó después cómo dar una excusa; no la invitó otra vez. Se ríe el jefe, en otro párrafo."},
  {"n": 25, "q": "Ahora, la abuela de Rocío...", "o": ["habla de usted a Hanna.", "saluda a Hanna con dos besos.", "baila flamenco con Hanna."], "ok": 1,
   "cats": ["saludos", "gerundio"], "es": "ES-08", "pc": "saludos · estar + gerundio (estoy aprendiendo)",
   "why": "«Ya me saluda con dos besos.» Hanna está aprendiendo flamenco con Rocío, no con la abuela."},
 ]}

# ---------------- AUDITIVA ----------------
# Cada conversación: pres (presentación del narrador), lines [(rol, voz, texto)], q, o, ok, why, cats, es, img, prompt
CA1 = {"n": 1, "type": "pics",
 "instr": "Usted va a escuchar seis conversaciones. Escuchará cada conversación dos veces. Después, tiene que contestar a las preguntas (de la 1 a la 6). Seleccione la opción correcta (A, B o C).",
 "tip": "Mira las tres imágenes antes de cada conversación. Cuando alguien pide algo, escucha bien la respuesta: «Es que...» o «Lo siento» casi siempre quieren decir que no.",
 "example": {"q": "¿Qué le deja la mujer al hombre?", "o": ["un cargador", "una batería externa", "un bolígrafo"], "ok": 1,
   "pres": "Va a escuchar a dos compañeros de trabajo en la oficina.",
   "lines": [("Hombre", "VOLU", "Marta, ¿me dejas tu cargador? Tengo el móvil sin batería."),
             ("Mujer", "SARA_JOVEN", "Lo siento, hoy no lo tengo aquí. Pero mira, ¿te sirve esta batería externa?"),
             ("Hombre", "VOLU", "Sí, perfecto. Te la devuelvo esta tarde."),
             ("Mujer", "SARA_JOVEN", "Vale. ¿Necesitas también un boli?"),
             ("Hombre", "VOLU", "No, no, boli tengo. Gracias."), ("Mujer", "SARA_JOVEN", "Muy bien. Pero devuélvemela antes de las cinco, que hoy me voy pronto.")],
   "solucion": "La opción correcta es la letra be. La mujer le deja una batería externa.",
   "img": "U05_CA1_0.jpg",
   "prompt": "Panel 1: a white phone charger with its cable. Panel 2: a small portable power bank with a cable. Panel 3: a blue ballpoint pen."},
 "items": [
  {"n": 1, "conv": "Conversación uno", "q": "¿Qué va a tomar la mujer?", "o": ["un café con leche", "un cruasán", "una manzanilla"], "ok": 2,
   "cats": ["pedir"], "es": "ES-05", "pc": "¿Me trae...? ¿Me pone...? · LX-05 · cambio de idea",
   "pres": "Va a escuchar a una mujer que habla con un camarero en una cafetería.",
   "lines": [("Mujer", "SOFIA", "Perdone, ¿me trae otro café con leche, por favor?"), ("Hombre", "DANI", "Ahora mismo. ¿Quiere algo más? Tenemos cruasanes recién hechos."),
             ("Mujer", "SOFIA", "No, gracias, no tengo hambre. Bueno, espere... mejor no tomo más café, que estoy un poco nerviosa. ¿Me pone una manzanilla?"),
             ("Hombre", "DANI", "Claro. Entonces una manzanilla y nada más, ¿verdad?"), ("Mujer", "SOFIA", "Eso es. Gracias.")],
   "why": "Primero pide un café con leche, pero cambia de idea porque está nerviosa y pide una manzanilla. El cruasán no lo quiere.",
   "img": "U05_CA1_1.jpg", "prompt": "Panel 1: a cup of white coffee with milk on a saucer. Panel 2: a croissant on a small plate. Panel 3: a cup of chamomile tea with a tea bag label hanging out."},
  {"n": 2, "conv": "Conversación dos", "q": "¿Qué puede hacer el hombre?", "o": ["abrir la ventana", "poner la maleta arriba", "sentarse al lado de la ventana"], "ok": 1,
   "cats": ["permiso", "tuusted"], "es": "ES-06", "pc": "¿Le importa si + presente? · ¿Puedo...? · usted",
   "pres": "Va a escuchar a un hombre que habla con una mujer en el tren.",
   "lines": [("Hombre", "GABRIEL_ES", "Perdone, señora, ¿le importa si abro la ventana? Hace mucho calor."),
             ("Mujer", "EVA", "Uy, es que estoy un poco resfriada... Mejor no, si no le importa."),
             ("Hombre", "GABRIEL_ES", "No, no, claro. ¿Y puedo sentarme en el asiento de la ventana?"),
             ("Mujer", "EVA", "Lo siento, es de mi hija. Está en la cafetería y vuelve ahora."),
             ("Hombre", "GABRIEL_ES", "Ah, vale. Entonces, ¿puedo poner mi maleta ahí arriba, encima de su asiento?"),
             ("Mujer", "EVA", "Sí, claro, póngala ahí, no hay problema."), ("Hombre", "GABRIEL_ES", "Muchas gracias, muy amable."), ("Mujer", "EVA", "De nada.")],
   "why": "La mujer le da permiso para poner la maleta arriba. No quiere la ventana abierta porque está resfriada, y el asiento de la ventana es de su hija.",
   "img": "U05_CA1_2.jpg", "prompt": "Panel 1: an open train window. Panel 2: a suitcase being placed on the luggage rack above the seats in a train. Panel 3: an empty train seat next to the window."},
  {"n": 3, "conv": "Conversación tres", "q": "¿Qué está haciendo el padre?", "o": ["cocinando", "regando las plantas", "duchándose"], "ok": 0,
   "cats": ["gerundio"], "es": "ES-08", "pc": "estar + gerundio · gerundios (regando, duchándose)",
   "pres": "Va a escuchar a dos hermanos que hablan en casa.",
   "lines": [("Mujer", "FIONA", "Oye, ¿y papá? ¿Se está duchando? Necesito el baño."),
             ("Hombre", "OSCAR", "No, el que se está duchando es el abuelo. Papá está en el jardín."),
             ("Mujer", "FIONA", "¿Regando las plantas otra vez? ¡Si está lloviendo!"),
             ("Hombre", "OSCAR", "No, mujer. Está haciendo la paella para la comida. Está cocinando fuera, debajo del porche."), ("Mujer", "FIONA", "¡Qué bien! ¿Y a qué hora comemos?"), ("Hombre", "OSCAR", "A las dos y media. ¿Pones tú la mesa?")],
   "why": "El padre está haciendo la paella: está cocinando en el jardín. El que se ducha es el abuelo, y no está regando porque está lloviendo.",
   "img": "U05_CA1_3.jpg", "prompt": "Panel 1: a middle-aged man cooking a large paella pan outdoors under a porch. Panel 2: a middle-aged man watering plants in a garden with a watering can. Panel 3: a shower with water running behind a shower curtain."},
  {"n": 4, "conv": "Conversación cuatro", "q": "¿Qué favor le pide la mujer a su vecino?", "o": ["regar las plantas", "dar de comer al gato", "recoger el correo"], "ok": 1,
   "cats": ["pedir"], "es": "ES-06", "pc": "¿Podrías hacerme un favor? · FN-4.2 · FN-4.6 ofrecerse",
   "pres": "Va a escuchar a una mujer que habla con su vecino en la escalera.",
   "lines": [("Mujer", "LUCIA", "Hola, Julián. Oye, ¿podrías hacerme un favor? Mañana me voy de viaje tres días."),
             ("Hombre", "MARIO", "Claro, dime. ¿Te riego las plantas?"),
             ("Mujer", "LUCIA", "No, las plantas se las dejo a mi hermana. Es por el gato. ¿Puedes ponerle la comida por la mañana?"),
             ("Hombre", "MARIO", "Sí, sin problema. ¿Y el correo? ¿Te lo recojo también?"),
             ("Mujer", "LUCIA", "No hace falta, gracias. Toma, las llaves. ¡Eres un sol!"), ("Hombre", "MARIO", "No hay de qué. ¡Que tengas buen viaje!")],
   "why": "Le pide que le ponga la comida al gato. Las plantas se las deja a su hermana, y el correo no hace falta: son ofrecimientos del vecino.",
   "img": "U05_CA1_4.jpg", "prompt": "Panel 1: a watering can next to potted plants. Panel 2: a cat eating from a food bowl. Panel 3: letters in an apartment mailbox."},
  {"n": 5, "conv": "Conversación cinco", "q": "¿Por qué no fue Carlos a la cena del sábado?", "o": ["Porque estuvo enfermo.", "Porque fue a la playa.", "Porque tuvo que trabajar."], "ok": 2,
   "cats": ["excusas"], "es": "ES-07", "pc": "FN-5.4 disculparse · es que... · GR indefinido (U02)",
   "pres": "Va a escuchar a dos amigos que hablan en la calle.",
   "lines": [("Mujer", "AITANA", "¡Carlos! Te esperamos el sábado en la cena de Ana. ¿Qué pasó? ¿Estuviste enfermo?"),
             ("Hombre", "DAVID_CO", "No, no. Perdona, de verdad. Es que tuve que ir a la oficina todo el día y terminé muy tarde."),
             ("Mujer", "AITANA", "¿Un sábado? ¿Y la excursión a la playa con tu hermano?"),
             ("Hombre", "DAVID_CO", "La excursión es el domingo que viene. Oye, ¿Ana está enfadada?"),
             ("Mujer", "AITANA", "Un poco. Llámala, ¿vale? Bueno, me tengo que ir. ¡Recuerdos a tu hermano!"), ("Hombre", "DAVID_CO", "De tu parte. ¡Hasta luego!")],
   "why": "Tuvo que ir a la oficina todo el sábado: trabajó. No estuvo enfermo, y la playa es el domingo que viene.",
   "img": "U05_CA1_5.jpg", "prompt": "Panel 1: a young man sick in bed with a thermometer. Panel 2: two young men walking on a beach with towels. Panel 3: a young man working late at an office desk with a computer, dark window behind."},
  {"n": 6, "conv": "Conversación seis", "q": "¿Qué le pasa el chico a su abuela?", "o": ["la sal", "el pan", "el agua"], "ok": 0,
   "cats": ["pedir"], "es": "ES-06", "pc": "¿Me pasas...? · tener · LX-05",
   "pres": "Va a escuchar a una abuela que habla con su nieto durante la comida.",
   "lines": [("Mujer", "NIEVE", "¡Qué buena está la tortilla, Javi! Pero le falta un poco de sal. ¿Me pasas la sal, por favor?"),
             ("Hombre", "ANTONIO", "Toma, abuela. Pero solo un poco, ¿eh? Ya sabes lo que dice el médico."),
             ("Mujer", "NIEVE", "Sí, hijo, sí. Ya lo sé."),
             ("Hombre", "ANTONIO", "¿Quieres también pan? ¿O agua?"),
             ("Mujer", "NIEVE", "No, gracias. Pan tengo aquí, y agua no quiero más. Así estoy bien.")],
   "why": "La abuela le pide la sal y Javi se la pasa. El pan y el agua se los ofrece él, pero ella no los quiere.",
   "img": "U05_CA1_6.jpg", "prompt": "Panel 1: a salt shaker on a dining table. Panel 2: a basket of bread on a dining table. Panel 3: a glass water jug on a dining table."},
 ]}

CH = "SONIDO 2: Two-tone ding-dong chime of a public address announcement system, clean and clear, no voices, no background noise"
BP = "SONIDO 1: Single short electronic answering machine beep, clean, no background noise"
CA4 = {"n": 4, "type": "msgs",
 "instr": "Usted va a escuchar ocho mensajes, incluido el ejemplo. Cada mensaje se repite dos veces. Seleccione el enunciado (de la A a la K) que corresponde a cada mensaje (del 19 al 25). Hay once opciones, incluido el ejemplo. Seleccione siete.",
 "tip": "Tienes 45 segundos para leer los enunciados. En cada mensaje pregúntate: ¿quién habla, a quién y para qué? ¿Pide algo, da las gracias, pide perdón, avisa? Sobran tres.",
 "enun": [
  "Alguien no puede ir a una cita y propone otro día.",
  "Una persona pide prestado un objeto.",
  "Se pide al público que apague el móvil.",
  "Alguien da las gracias por un favor.",
  "Una persona pide permiso para llegar más tarde.",
  "Se presenta a unas personas nuevas.",
  "Alguien pide ayuda para cuidar a un animal.",
  "Un establecimiento pide perdón por un problema.",
  "Se informa de que algo no funciona hoy.",
  "Alguien ofrece su coche.",
  "Una persona felicita a otra."],
 "example": {"q": "Mensaje 0", "ok": 0, "lab": "Contestador", "voice": "VALENTINA/RADIO", "sound": BP,
   "text": "Hola, Laura, soy Marisa. Oye, perdona, pero mañana no puedo ir contigo a la clase de yoga: tengo que llevar a mi madre al médico. ¿Te va bien el jueves? Llámame cuando puedas. Un beso.",
   "solucion": "La opción correcta es la letra a: alguien no puede ir a una cita y propone otro día."},
 "items": [
  {"n": 19, "conv": "Mensaje 1", "q": "Mensaje 1", "ok": 4, "cats": ["permiso", "tuusted", "gerundio"], "es": "ES-10", "pc": "¿Le importa si + presente? · usted · estar + gerundio",
   "lab": "Contestador", "voice": "MARINA_ES/RADIO", "sound": BP,
   "text": "Buenos días, señor Molina, soy Irene Castro, de contabilidad. Perdone, pero hay un accidente en la autopista y estoy esperando en el coche sin poder moverme. ¿Le importa si llego a la reunión a las diez y media? Muchas gracias.",
   "why": "Irene pide permiso para llegar más tarde a la reunión. Está en su coche, pero no lo ofrece (J sobra)."},
  {"n": 20, "conv": "Mensaje 2", "q": "Mensaje 2", "ok": 8, "cats": ["excusas"], "es": "ES-10", "pc": "LX-14 transporte · perdonen las molestias",
   "lab": "Megafonía", "voice": "LUIS_VEGA/RADIO", "sound": CH,
   "text": "Atención, señores viajeros: hoy el ascensor del andén dos no funciona. Las personas con maletas grandes o con carritos de bebé pueden usar el ascensor del andén uno. Perdonen las molestias.",
   "why": "Hoy no funciona el ascensor del andén dos. Pide perdón, pero no es por un problema ya resuelto en un establecimiento: eso es el mensaje 4 (H)."},
  {"n": 21, "conv": "Mensaje 3", "q": "Mensaje 3", "ok": 1, "cats": ["pedir", "gerundio"], "es": "ES-10", "pc": "¿Me la puedes dejar? · dejar / devolver · estar + gerundio",
   "lab": "Contestador", "voice": "DANIEL_ES/RADIO", "sound": BP,
   "text": "Hola, Andrés, soy Raúl, el vecino del segundo. Mira, estoy pintando la cocina y necesito una escalera alta. ¿Me la puedes dejar esta tarde? Te la devuelvo mañana por la mañana. ¡Gracias!",
   "why": "Raúl pide prestada una escalera a su vecino: se la devuelve mañana."},
  {"n": 22, "conv": "Mensaje 4", "q": "Mensaje 4", "ok": 7, "cats": ["excusas"], "es": "ES-07", "pc": "disculparse (sentimos, disculpen) · LX-12 compras",
   "lab": "Megafonía", "voice": "LYDIA/RADIO", "sound": CH,
   "text": "Estimados clientes: sentimos mucho el problema de esta mañana con las tarjetas. Ya se puede pagar con tarjeta en todas las cajas. Disculpen las molestias y gracias por su paciencia.",
   "why": "El supermercado pide perdón por el problema de esta mañana. Las tarjetas ya funcionan: no es la I."},
  {"n": 23, "conv": "Mensaje 5", "q": "Mensaje 5", "ok": 3, "cats": ["pedir"], "es": "ES-02", "pc": "dar las gracias por + infinitivo · FN-5.3",
   "lab": "Contestador", "voice": "JANET/RADIO", "sound": BP,
   "text": "Hola, Pilar, soy Encarna. Te llamo para darte las gracias por cuidar a mi perro el fin de semana. Está muy contento... ¡Creo que ahora te quiere más a ti que a mí! Mañana te llevo unos dulces del pueblo. ¡Te lo agradezco muchísimo!",
   "why": "Encarna da las gracias por cuidar a su perro. No pide ayuda con el animal: ya se la dieron (G sobra)."},
  {"n": 24, "conv": "Mensaje 6", "q": "Mensaje 6", "ok": 2, "cats": ["pedir"], "es": "ES-10", "pc": "imperativo usted (apaguen) · LX-18 espectáculos",
   "lab": "Megafonía", "voice": "SERGIO/RADIO", "sound": CH,
   "text": "Señoras y señores, buenas noches. La función va a empezar en cinco minutos. Por favor, apaguen sus teléfonos móviles y no hagan fotos durante el espectáculo. Les recordamos que no se puede entrar en la sala con comida ni bebida. Muchas gracias.",
   "why": "En el teatro piden al público que apague el móvil."},
  {"n": 25, "conv": "Mensaje 7", "q": "Mensaje 7", "ok": 5, "cats": ["saludos"], "es": "ES-10", "pc": "presentar (os presento a) · FN-5.2 · dar la bienvenida",
   "lab": "Aviso", "voice": "MARTIN_3/RADIO", "sound": "",
   "text": "Buenas tardes, vecinos. Antes de empezar la reunión, os presento a Lola y a Martín, los nuevos vecinos del cuarto. Llegaron la semana pasada desde Granada. Si necesitáis algo, viven en la puerta be. ¡Bienvenidos!",
   "why": "El presidente presenta a los vecinos nuevos. Les da la bienvenida, pero nadie felicita a nadie (K sobra)."},
 ]}
for it in CA4["items"]:
    it["o"] = CA4["enun"]
    if not it.get("sound"): it.pop("sound", None)

REPARTO = """# REPARTO DE VOCES U05 (ninguna protagonista de la U04)
# T1 conversaciones (v3, ritmo natural): 0 oficina = VOLU + SARA_JOVEN · 1 cafetería = SOFIA (Colombia) + DANI
#   2 tren = GABRIEL_ES + EVA · 3 hermanos = FIONA + OSCAR · 4 vecinos = LUCIA + MARIO
#   5 amigos en la calle = AITANA + DAVID_CO (Colombia) · 6 abuela y nieto = NIEVE (Argentina, mayor) + ANTONIO (Latinoamérica)
# T4 mensajes (/RADIO: cada mensaje entero con v3): 0 contestador Marisa = VALENTINA (Colombia) · 1 contestador Irene = MARINA_ES
#   2 megafonía estación = LUIS_VEGA · 3 contestador Raúl = DANIEL_ES · 4 megafonía supermercado = LYDIA
#   5 contestador Encarna = JANET (Argentina) · 6 megafonía teatro = SERGIO · 7 aviso en la reunión de vecinos = MARTIN_3
# Efectos: din-don de megafonía y pitido de contestador (siempre la misma descripción: caché); el aviso 7 va sin efecto"""

# ---------------- ESCRITURA ----------------
ESCRITA = {"t1": {"instr": "Una amiga le escribe para pedirle un favor.",
  "input": ["¡Hola! ¿Cómo va todo? Te escribo porque necesito un favor: el lunes me voy a Roma cinco días y no sé con quién dejar a mi perra, Lola. ¿Podrías cuidarla tú? Ya sé que es mucho pedir... Dime algo, ¿vale?", "Un beso,<br>Elena"],
  "lead": "Conteste a su amiga. En el correo tiene que:",
  "pautas": ["saludar;", "decir si puede cuidar a la perra o no, y explicar por qué;", "proponer otra solución o pedirle información sobre la perra;", "pedirle a ella un favor para cuando vuelva de Roma;", "despedirse."],
  "min": 60, "max": 70},
 "t2": {"instr": "Elija solo una de las dos opciones. En cada opción tiene que tratar todos los puntos.",
  "op1": {"title": "Opción 1", "intro": "Escriba un texto sobre cómo se saluda y cómo se habla con la gente en su país. Hable de:",
   "pautas": ["cómo se saluda a la familia y a los amigos;", "cómo se saluda en el trabajo y a las personas que no conoce;", "si hay una forma de hablar más formal (como usted) y con quién se usa;", "qué le sorprendió de los saludos en España o en otro país;", "qué costumbre prefiere y por qué."]},
  "op2": {"title": "Opción 2", "intro": "El invierno pasado usted empezó a trabajar en un hotel de una estación de esquí. Aquí tiene tres fotos de su primer día.",
   "photos": ["Por la mañana temprano, con mucha nieve, usted llega en autobús al hotel con una maleta grande. En la puerta le espera una señora mayor con el pelo blanco y un abrigo rojo.",
              "En la cocina del hotel, la señora le presenta a sus compañeros: un cocinero alto con barba y gorro blanco y una camarera joven con gafas. Todos sonríen.",
              "Por la noche, en el comedor lleno de clientes, a usted se le caen unos platos al suelo. Un niño se ríe y la camarera viene a ayudarle."],
   "ficha": [], "intro2": "Escriba un texto sobre ese día. Hable de:",
   "pautas": ["dónde está el hotel y cómo llegó usted;", "a quién conoció y cómo lo saludaron;", "qué pasó por la noche y cómo terminó el día."],
   "img": "U05_escrita.jpg", "imgAlt": "Tres fotos del primer día en el hotel: la llegada con nieve, la cocina y el comedor"},
  "min": 70, "max": 80}}

# ---------------- ORAL ----------------
ORAL = {"t1": {"instr": "Elija una de las dos opciones. Hable durante 2 o 3 minutos sobre el tema.", "ops": [
  {"title": "Opción 1: mis vecinos", "pautas": ["quiénes son sus vecinos y cómo los conoció;", "cómo se saludan y si se hablan de tú o de usted;", "qué favores les pide usted y qué favores le piden ellos;", "una vez que un vecino le ayudó mucho;", "si en su país los vecinos se ayudan más o menos que aquí."]},
  {"title": "Opción 2: hablar con la gente", "pautas": ["cómo saluda y cómo se despide de su familia, de sus amigos y en el trabajo;", "con quién habla de forma formal y con quién de forma informal;", "una situación en la que no supo qué decir o qué hacer;", "qué excusas da cuando no quiere hacer algo;", "qué le parece más difícil de hablar con españoles."]}]},
 "t2": {"instr": "Elija una de las dos fotografías y descríbala durante 2 o 3 minutos.", "fotos": [
  {"title": "Fotografía 1", "desc": "Una parada de autobús en una calle de ciudad, de noche, en invierno; está lloviendo. Un señor mayor con barba blanca, gafas, abrigo y bufanda le enseña su móvil a una chica de unos quince años con capucha, auriculares y mochila. El señor parece preocupado. Al fondo pasa un taxi y hay una tienda cerrada.", "img": "U05_oral_foto1.jpg"},
  {"title": "Fotografía 2", "desc": "Un taller de bicicletas en un pueblo, un día de verano con mucho sol. Un mecánico joven con mono azul y las manos negras de grasa mira la bicicleta rota de una niña con casco; la niña está triste y su abuela, con sombrero de paja, habla con el mecánico. En la pared hay ruedas y herramientas; un gato duerme en una silla y por la puerta se ve a unos ciclistas.", "img": "U05_oral_foto2.jpg"}],
  "pautas": ["las personas: cómo son, qué ropa llevan, qué están haciendo;", "el lugar: dónde están, qué tiempo hace, qué cosas hay y dónde están;", "qué cree que pasa o qué problema tienen las personas;", "qué cree que va a pasar después."]},
 "t3": {"instr": "La tarea 3 depende de la fotografía que eligió en la tarea 2.", "ops": [
  {"title": "Si eligió la fotografía 1", "intro": "Usted ha perdido el último autobús y está en la parada. Llame por teléfono a un amigo (su profesora) para pedirle ayuda. Tiene que:", "pautas": ["saludar, decir dónde está y explicar qué pasa;", "pedirle que venga a buscarle en coche;", "buscar otra solución si su amigo no puede;", "darle las gracias y despedirse."]},
  {"title": "Si eligió la fotografía 2", "intro": "Su bicicleta está rota y usted la lleva a un taller. Hable con el mecánico (su profesora). Tiene que:", "pautas": ["saludar y explicar qué le pasa a la bicicleta;", "preguntar si la puede arreglar hoy y cuánto cuesta;", "pedir permiso para dejarla allí o pedir prestada otra bicicleta;", "quedar para recogerla y despedirse."]}]}}

# ---------------- PROFESORA ----------------
GUION_ENTREVISTADOR = """  Tarea 1 · No interrumpa el monólogo. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Opción 1 (mis vecinos): ¿Le ha pedido algo un vecino hace poco? · ¿Qué hace usted si un vecino hace ruido?
    Opción 2 (hablar con la gente): ¿Da usted dos besos o la mano? · ¿Qué dice si llega tarde a una cita?
  Tarea 2 · No interrumpa la descripción. Solo si se bloquea o termina antes de 2 minutos, una ayuda:
    Foto 1 (parada de autobús de noche): ¿Qué cree que le pregunta el señor? · ¿Qué está haciendo la chica?
    Foto 2 (taller de bicicletas): ¿Qué le pasa a la niña? · ¿Qué cree que le dice la abuela al mecánico?
  Tarea 3 — su papel (aquí sí conversa: pregunte, reaccione y provoque un pequeño problema):
    Foto 1 (amigo/a al teléfono, de tú): está cenando con su familia y ha tomado una copa de vino, así que
    no puede conducir; su pareja tiene el coche. Pregunte «¿Dónde estás exactamente?» y «¿Tienes dinero
    para un taxi?». Solución posible: le paga el taxi y quedan mañana para devolverle el dinero, o le
    ofrece dormir en su sofá. Problema: tiene el móvil con poca batería y la llamada puede cortarse.
    Foto 2 (mecánico/a, de usted): la cadena está rota y la rueda pinchada; arreglarla cuesta 25 euros,
    pero la pieza no llega hasta el lunes. Puede prestar una bicicleta del taller por 5 euros al día.
    Cierra a las dos y abre a las cinco. Pregunte «¿Cómo se rompió?» y «¿Me deja un teléfono?».
    Problema: el sábado el taller está cerrado.
  Al pedir o al decir que no, que use fórmulas de cortesía y una excusa (es que...), nunca un «no» seco;
  que salude, agradezca y se despida al principio y al final de la tarea 3.
  Qué mirar en esta unidad: tú / usted coherentes en cada tarea (T3 foto 1 de tú, foto 2 de usted);
  peticiones con ¿puedes...?, ¿podría...?, ¿le importa...?; excusas con es que...; estar + gerundio
  en la descripción (está lloviendo, están hablando); gerundios irregulares."""
ERRORES = """  *Estoy hablo / *estoy hablar (estoy hablando); *dormiendo, *pediendo, *deciendo (durmiendo, pidiendo, diciendo);
  *¿Podrías me ayudar? (¿me podrías ayudar? / ¿podrías ayudarme?); *¿Te importa si abrir? (si abro);
  mezcla de tú y usted en la misma petición (*Perdone, ¿puedes...?); *Lo siento por no ir (siento no ir /
  perdona por no ir); *es porque... para excusarse (es que...); dejar / prestar / pedir confundidos
  (*¿Me pides tu coche? > ¿me dejas / me prestas tu coche?); dar / prestar (¿me das un boli? se queda;
  ¿me prestas el boli? se devuelve); *Te presento Ana (te presento a Ana); *Cuídate, señora (cuídese);
  «No» o «No quiero» sin excusa: correcto, pero suena brusco."""

# ---------------- IMÁGENES: FOTOS CON VARIEDAD REAL ----------------
# Perfil de cada foto (oral y escritura). Cambia de una unidad a otra: personas, edades, aspecto,
# lugar, momento, tiempo, acción, fondo, objetos y un pequeño problema para la tarea 3.
PERFIL_FOTOS = {
 "oral_foto1": {"situacion": "parada de autobús de noche",
  "personas": "dos (desconocidos)", "edades": "un señor de unos 75 años y una adolescente de unos 15",
  "aspecto": "él: barba blanca, gafas, abrigo largo, bufanda, gorra de lana y paraguas; ella: sudadera con capucha, auriculares grandes, mochila del instituto y zapatillas",
  "espacio": "exterior", "lugar": "calle de ciudad, parada de autobús con marquesina", "momento": "noche",
  "estacion": "invierno", "tiempo": "lluvia, charcos en el suelo", "gente": "casi vacío",
  "accion": "el señor le enseña su móvil a la chica y le pide ayuda; ella mira la pantalla",
  "fondo": "pasa un taxi con las luces encendidas; una tienda con la persiana bajada; una mujer corre con un paraguas",
  "objetos": "marquesina, banco, papelera, farola, panel de horarios, paraguas, bolsa de la compra con una barra de pan, charcos, móvil",
  "problema": "el señor está preocupado: no llega el autobús y no sabe usar la aplicación del móvil"},
 "oral_foto2": {"situacion": "taller de bicicletas en un pueblo",
  "personas": "tres", "edades": "una niña de unos 9 años, su abuela de unos 70 y un mecánico de unos 30",
  "aspecto": "niña: casco rosa, rodilleras y camiseta de rayas; abuela: canas, sombrero de paja, vestido de flores y gafas de sol en la cabeza; mecánico: mono azul de trabajo, gorra al revés, tatuaje en el brazo y manos negras de grasa",
  "espacio": "interior", "lugar": "taller pequeño con la puerta abierta a la calle de un pueblo", "momento": "día",
  "estacion": "verano", "tiempo": "mucho sol y calor", "gente": "lleno de cosas y gente",
  "accion": "el mecánico revisa la bicicleta rota de la niña mientras la abuela le habla",
  "fondo": "por la puerta se ven ciclistas con ropa de deporte bebiendo agua y una fuente en la plaza",
  "objetos": "bicicletas, ruedas colgadas en la pared, herramientas, bomba de aire, ventilador, radio, botella de agua, cadena, casco; un gato duerme en una silla",
  "problema": "la niña está triste porque su bicicleta tiene la cadena rota y una rueda pinchada"},
 "escrita": {"situacion": "primer día de trabajo en un hotel de montaña",
  "personas": "grupo (usted, una señora, un cocinero, una camarera, clientes, un niño)",
  "edades": "variadas: una señora de unos 65, adultos de 25 a 45 y un niño de unos 7",
  "aspecto": "señora: pelo blanco y abrigo rojo; cocinero: alto, barba y gorro blanco; camarera: joven con gafas y coleta; protagonista con ropa de invierno y luego con uniforme",
  "espacio": "exterior e interior", "lugar": "hotel pequeño de una estación de esquí", "momento": "de la mañana a la noche",
  "estacion": "invierno", "tiempo": "nieve", "gente": "de casi vacío (llegada) a lleno (comedor)",
  "accion": "llegar, ser presentado a los compañeros, servir en el comedor",
  "fondo": "montañas nevadas y un autobús; en la cocina, ollas y vapor; en el comedor, una chimenea",
  "objetos": "maleta, nieve, autobús, abrigo, ollas, gorro de cocinero, bandeja, platos rotos, mesas, chimenea",
  "problema": "por la noche al protagonista se le caen unos platos delante de los clientes"},
}
SITUACIONES_USADAS = {
 "U01": ["secretaría", "librería"],
 "U02": ["taquilla de cine", "museo"],
 "U03": ["tienda de ropa", "aeropuerto"],
 "U04": ["tienda de muebles", "piso vacío en alquiler"],
 "U05": ["parada de autobús de noche", "taller de bicicletas en un pueblo"],
}

IMG_PROMPTS = {
 "portada": "Photorealistic, candid photo of a small Spanish town square on a sunny spring morning at a street market: an elderly woman with a grey bun and a shopping trolley greets a young man with curly hair and a cycling helmet with two kisses on the cheeks, while a middle-aged man in a suit shakes hands with a woman in a red coat next to a fruit stall; children run in the background; colourful awnings, crates of oranges, flowers, no readable text, 16:9",
 "oral": "Photorealistic, candid photo in a small bright language classroom: a woman teacher in her fifties with short red hair and an adult male student in his sixties with a grey beard sit face to face and act out a phone call, both holding mobile phones and laughing; a whiteboard with drawings but no readable text, plants on the windowsill, warm afternoon light, 3:2",
 "escrita": "Photorealistic triptych, three separate photos side by side of equal size with thin white borders, the same young worker on the first day at a small mountain ski hotel in winter. Left: early morning, heavy snow, the young person gets off a bus with a big suitcase and an older woman with white hair in a red coat waits at the hotel door, snowy mountains behind. Centre: a busy hotel kitchen with steam and pots, the older woman introduces the newcomer to a tall bearded cook in a white hat and a young waitress with glasses and a ponytail, everyone smiling. Right: at night in a full dining room with a fireplace, the newcomer in uniform has just dropped a tray and broken plates on the floor, a little boy at a table laughs and the waitress comes to help. Candid, natural and warm indoor light, no readable text, 3:1",
 "oral_foto1": "Photorealistic, candid photo at night in winter in a Spanish city street, rain falling and puddles reflecting the street lights: at a bus stop with a glass shelter and a bench, an old man of about 75 with a white beard, glasses, a long dark coat, a scarf and a wool cap, holding an umbrella and a shopping bag with a baguette, shows his mobile phone to a teenage girl of about 15 in a hoodie with big headphones and a school backpack, who looks at the screen; the old man looks worried; in the background a taxi passes with its lights on, a closed shop with its metal shutter down and a woman running with an umbrella; a timetable panel without readable text, a litter bin, a street lamp; cold blue night light mixed with warm street lights, no readable text, 3:2",
 "oral_foto2": "Photorealistic, candid photo inside a small, cluttered bicycle repair workshop in a Spanish village on a hot, very sunny summer day, the big door open to the street: a young mechanic of about 30 in blue work overalls, a backwards cap, a tattoo on his forearm and hands black with grease kneels and checks a child's bicycle with a broken chain and a flat tyre; a sad girl of about 9 with a pink helmet, knee pads and a striped t-shirt stands next to it, and her grandmother of about 70 with grey hair, a straw hat, a flowered dress and sunglasses on her head talks to the mechanic, gesturing; wheels and tools hang on the wall, a pump, an electric fan, an old radio and a water bottle on the workbench, a cat sleeps on a chair; through the door, cyclists in sports clothes drink water at a fountain in a sunny square; bright warm light, no readable text, 3:2",
}
IMG_DESC = {"portada": "plaza de pueblo con mercado: saludos con dos besos y apreton de manos", "oral": "clase: profesora pelirroja y alumno con barba simulan una llamada", "escrita": "tres fotos del hotel de montaña: llegada con nieve, cocina, platos rotos", "oral_foto1": "parada de autobus de noche con lluvia: señor mayor y adolescente", "oral_foto2": "taller de bicis en un pueblo en verano: mecanico, niña y abuela"}
CA1_DESC = {0: "cargador / bateria externa / boligrafo", 1: "cafe con leche / cruasan / manzanilla", 2: "ventana abierta / maleta arriba / asiento de ventana", 3: "padre cocinando paella / regando / ducha", 4: "regadera y plantas / gato comiendo / buzon con cartas", 5: "chico enfermo / dos chicos en la playa / chico en la oficina de noche", 6: "salero / pan / jarra de agua"}

LECTURA = [CL1, CL4]
AUDITIVA = [CA1, CA4]
