# Referencias oficiales y manuales · lo útil de los PDF

Este documento sustituye en el proyecto a los 9 PDF y a la imagen que se subieron el 18/09/2026. Recoge, con palabras propias, los datos de formato y calificación que se usan al producir material. Los análisis de detalle ya están en otros archivos del proyecto:

- **Cómo es de verdad el examen** (Modelo 0, láminas de 2022, transcripciones): `claude/DELE_A2_examen_real_hallazgos.txt`. Manda sobre todo lo demás.
- **Estructura y reglas de redacción de ítems**: `DELE_A2_especificacion_formato_simulacros.txt`.
- **Qué aporta cada manual de preparación**: `claude/DELE_A2_curso_preparacion_plan.txt`, apartados 1.2 y 1.3.
- **Inventario de gramática, funciones y léxico A2**: `DELE_A2_plan_curricular.txt`.

Recordatorio: los documentos oficiales se usan solo como referencia de formato. Está prohibido reproducir sus textos, audios o ítems, y copiar ejercicios de cualquier manual.

## 1. Qué había en cada archivo subido

| Archivo | Qué es | Dónde está ya lo útil |
|---|---|---|
| `Guia Examen A2.pdf` | Guía oficial del examen (Instituto Cervantes, 2022) | Apartados 2 y 3 de este documento; hallazgos |
| `Especificaciones_DELE_A2_2020.pdf` | Especificaciones del formato vigente desde 2020 | Especificación de formato; hallazgos |
| `DELE-A2_v2020_Modelo0_0.pdf` | Modelo 0 oficial (formato 2020), con transcripción y material del examinador | Hallazgos (dificultad, escritura, oral) |
| `DELE_A2_0222_EIO_..._T1.pdf` | Láminas oficiales de la oral 2022, tarea 1 (8 temas) | Hallazgos; `banco_temas_T1.py` (M4-1) |
| `DELE_A2_0222_EIO_..._T2_T3.pdf` | Láminas oficiales de la oral 2022, tareas 2 y 3 (8 situaciones) | Hallazgos; M4-2 y M4-3 |
| `Examen A2.png` | Tabla oficial de pruebas, duración y puntuación | Apartado 2 de este documento |
| `Aula internacional 2 plus` (extracto) | Manual de clase. Base de los simulacros U01-U10 | Apartado 4; cada `fuente_Uxx.py` (RECORDATORIO y CATS) |
| `NUEVO-DELE-A2` (extracto) | Manual de preparación con formato actual | Plan, apartado 1.3 |
| `¡Dale al DELE! A2` (2013, extracto) | Manual de preparación con formato **antiguo** (5 tareas por prueba) | Plan, apartado 1.3; hallazgos |
| `CRONO A2` (extracto) | Manual de preparación con 7 modelos. Es escaneado y no tiene texto extraíble | Plan, apartado 1.3 (enfoque de «gestión del examen») |

## 2. Estructura del examen (formato 2020)

| Prueba | Duración | Tareas e ítems | Puntos |
|---|---|---|---|
| 1. Comprensión de lectura | 60 min | T1 5 · T2 8 · T3 6 · T4 6 = 25 ítems | 25 |
| 2. Comprensión auditiva | 40 min | T1 6 · T2 6 · T3 6 · T4 7 = 25 ítems | 25 |
| 3. Expresión e interacción escritas | 45 min | T1 interacción · T2 expresión (dos opciones, se elige una) | 25 |
| 4. Expresión e interacción orales | 12 min + 12 de preparación | T1 monólogo · T2 foto · T3 diálogo | 25 |

La lectura, la auditiva y la escritura se hacen el día oficial. La oral puede hacerse el día de antes o el de después, según el centro.

### Lectura

Ítems de tres opciones. Acierto = 1 punto, error = 0 (no resta). Total de texto: 1325-1725 palabras.

- **T1**: correo o carta personal, 250-300 palabras. Idea principal y datos concretos.
- **T2**: ocho textos breves de 50-80 palabras (anuncios, avisos, folletos, foros, normas).
- **T3**: tres textos de 100-120 palabras. Hay que relacionar seis enunciados con su texto.
- **T4**: texto narrativo de 375-425 palabras (biografía, diario, blog, noticia, guía).

### Auditiva

Cada audio se oye dos veces, con pausas para leer y para contestar, y sin ruidos ambientales. Total: 975-1465 palabras.

- **T1**: seis conversaciones de 50-80 palabras, con tres imágenes por pregunta.
- **T2**: seis cortes de radio de 40-60 palabras.
- **T3**: una conversación de 225-275 palabras. Seis enunciados: él, ella o ninguno.
- **T4**: siete mensajes de 30-50 palabras (megafonía, contestador) y enunciados para relacionar. La Guía dice «diez enunciados»; el Modelo 0 y nuestro formato usan once con el ejemplo. Ver hallazgos.

### Escritura

130-150 palabras en total.

- **T1**: respuesta epistolar a un texto de entrada de 35-45 palabras. El candidato escribe 60-70 palabras.
- **T2**: 70-80 palabras. Opción A: tema cotidiano de la vida personal. Opción B: biografía o narración a partir de fotos o datos.

### Oral

Hay 12 minutos de preparación con notas que se pueden consultar. Se empieza con preguntas de contacto, que no se evalúan. En la sala hay un entrevistador, que también es el interlocutor, y un calificador, que no interviene.

- **T1**: monólogo de 2-3 min sobre un tema personal; se elige entre dos.
- **T2**: descripción de una foto de la vida cotidiana, 2-3 min.
- **T3**: conversación de 3-4 min en una situación simulada a partir de la foto de la T2.

## 3. Calificación

- **Lectura y auditiva**: puntos = aciertos (de 0 a 25).
- **Escritura y oral**: bandas de 0 a 3 en dos categorías, Uso de la lengua (66 %) y Cumplimiento de la tarea (34 %).
  - La banda 2 equivale al A2.
  - Nota sobre 25 = puntuación directa × 25 / 3. Por ejemplo, banda 2 = 16,67 puntos.
- **Escritura**: dos calificadores independientes; cada tarea vale el 50 %; se hace la media de los dos.
  - Cumplimiento: 1 punto que falta o está mal resuelto → todavía banda 2. Dos o más → banda 1.
- **Oral**:
  - Calificador, 60 %: T1 25 %, T2 25 % y T3 50 % de su parte. Usa una escala para T1-T2 y otra para T3.
  - Entrevistador, 40 %: nota global de toda la prueba.
  - Pesos sobre el total de la oral:

    | | Uso de la lengua | Cumplimiento |
    |---|---|---|
    | T1 | 9,9 % | 5,0 % |
    | T2 | 9,9 % | 5,0 % |
    | T3 | 19,8 % | 10,2 % |
    | Entrevistador | 26,4 % | 13,6 % |

- **Apto**: 30 de 50 en cada grupo.
  - Grupo 1 = lectura + escritura.
  - Grupo 2 = auditiva + oral.
  - Un grupo no compensa al otro. Los resultados llegan en 1-3 meses.
- **Rasgos de cada banda (resumen)**:
  - Banda 2: repertorio limitado (presente y pasados de indicativo, perífrasis frecuentes) y conectores sencillos. Hay errores básicos que no impiden entender.
  - Banda 3: además, algún detalle, valoración u opinión; conectores como «además», «sin embargo» o «aunque»; algo de subordinación.
  - Banda 1: frases aisladas, conectores mínimos («y», «pero», «porque») y errores que dificultan la comprensión.
  - La rúbrica completa que se usa en el curso está en `claude/build_corrector.py` (RUBRICA) y en `DELE_A2_sistema_correccion_informe.txt`.

## 4. Manual de clase · temas de los simulacros U01-U10

Cada simulacro de unidad sigue una unidad de *Aula internacional 2 plus*. La gramática, el léxico y la página del libro de cada unidad están en el `RECORDATORIO` y en los `CATS` de su `fuente_Uxx.py` (o en `DELEA2_F1_U0x_datos.py` para U01 y U02).

| Unidad | Título del simulacro |
|---|---|
| U01 | Aprender idiomas |
| U02 | Historias de vida |
| U03 | Así somos |
| U04 | Hogar, dulce hogar |
| U05 | ¿Cómo va todo? |
| U06 | Guía del ocio |
| U07 | ¿Comes de todo? |
| U08 | Estamos muy bien |
| U09 | Antes y ahora |
| U10 | Momentos especiales |
