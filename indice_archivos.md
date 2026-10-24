# Índice de archivos · Curso y simulacros DELE A2

Dónde está cada archivo y para qué sirve. **Proyecto** = en el proyecto de claude.ai (se lee en cada chat). **Repo** = en el repositorio privado `mariarv1976-ops/dele-a2-curso` (se abre solo cuando hace falta).

## En el proyecto (lo esencial)

- `claude/DELE_A2_instrucciones_proyecto.txt` · instrucciones del proyecto
- `claude/DELE_A2_curso_estado.txt` · estado corto: qué está hecho, qué falta y el siguiente paso
- `claude/DELE_A2_examen_real_hallazgos.txt` · cómo es de verdad el examen (manda sobre todo)
- `claude/DELE_A2_curso_preparacion_plan.txt` · plan del curso
- `DELE_A2_plan_curricular.txt`, `DELE_A2_especificacion_formato_simulacros.txt`, `DELE_A2_sistema_correccion_informe.txt`, `DELE_A2_plantilla_oral_y_tips.txt` · referencias
- `claude/DELE_A2_referencias_oficiales.md` · lo útil de los PDF y la imagen subidos (sustituye a los PDF)
- `indice_archivos.md` · este índice

## En el repo (todo, con las mismas rutas)

| Archivo | Tamaño | Qué es |
|---|---|---|
| `DELEA2_F1_U01_datos.py` | 37 KB | DATOS DE LA UNIDAD 1 (fase 1) para DELE_A2_motor_simulacro.py |
| `DELEA2_F1_U02_datos.py` | 38 KB | DATOS DE LA UNIDAD 2 (fase 1) para DELE_A2_motor_simulacro.py |
| `DELE_A2_especificacion_formato_simulacros.txt` | 17 KB | ESPECIFICACIÓN DEL EXAMEN DELE A2 Y DEL SIMULACRO POR UNIDAD |
| `DELE_A2_motor_simulacro.py` | 54 KB | MOTOR DEL SIMULACRO DELE A2 (2spanishteachers.com) |
| `DELE_A2_plan_curricular.txt` | 33 KB | PLAN CURRICULAR A2 DEL PROYECTO — REFERENCIA DE NIVEL PARA SIMULACROS DELE |
| `DELE_A2_plantilla_entrega_y_registro.txt` | 7 KB | PLANTILLA DE ENTREGA DEL SIMULACRO Y REGISTRO DE PRODUCCIÓN — DELE A2 |
| `DELE_A2_plantilla_oral_y_tips.txt` | 7 KB | PLANTILLA DE EVALUACIÓN ORAL Y CONSEJOS DE EXAMEN — DELE A2 |
| `DELE_A2_produccion_audio_imagenes_ejecutable.txt` | 14 KB | PRODUCCIÓN DE LOS SIMULACROS DELE A2: AUDIOS, IMÁGENES Y EJECUTABLE |
| `DELE_A2_sistema_correccion_informe.txt` | 7 KB | SISTEMA DE CORRECCIÓN E INFORME DE REPASO — DELE A2 |
| `DELE_oral_profesora.py` | 54 KB | LIBRETA ORAL DE LA PROFESORA · común a los simulacros DELE A2 y B2 (2spanishteachers.com) |
| `README.md` | 1 KB | Curso y simulacros DELE A2 · 2spanishteachers.com (privado) |
| `U02_guion.txt` | 11 KB | GUION DE AUDIO · UNIDAD 2 |
| `build_unidad.py` | 21 KB | Genera a partir de fuente_Uxx.py: datos.py, cuadernillos, guion de audio (las 4 tareas de auditiva: |
| `claude/DELEA2_curso_M01_datos.py` | 92 KB | DATOS DEL MODELO 01 (curso de preparación DELE A2) · generado con build_modelo.py |
| `claude/DELEA2_curso_M02_datos.py` | 97 KB | Datos del Modelo 2 (generado por build_modelo.py desde fuente_M02.py) |
| `claude/DELEA2_curso_M03_datos.py` | 98 KB | Datos del Modelo 3 (generado por build_modelo.py desde fuente_M03.py) |
| `claude/DELEA2_curso_M06_datos.py` | 95 KB | Datos del Modelo 6 (generado por build_modelo.py desde fuente_M06.py; en el repo desde el 24/10) |
| `claude/DELEA2_curso_M07_datos.py` | 97 KB | DATOS DEL MODELO 07 (curso de preparación DELE A2) · generado con build_modelo.py |
| `claude/DELE_A2_curso_estado.txt` | 22 KB | ESTADO DEL CURSO DE PREPARACIÓN DELE A2 · VERSIÓN CORTA (actualizar en cada chat) |
| `claude/DELE_A2_curso_preparacion_plan.txt` | 25 KB | PLAN DEL CURSO DE PREPARACIÓN DELE A2 |
| `claude/DELE_A2_examen_real_hallazgos.txt` | 16 KB | CÓMO ES DE VERDAD EL DELE A2 (investigación 15/10/2026) · para calibrar los modelos M1-M8 |
| `claude/DELE_A2_instrucciones_proyecto.txt` | 5 KB | PROYECTO DELE A2 · SIMULACROS Y CURSO DE PREPARACIÓN (2spanishteachers.com) |
| `claude/DELE_A2_referencias_oficiales.md` | 7 KB | Referencias oficiales y manuales · lo útil de los PDF |
| `claude/actualizar_libreta_html.py` | 4 KB | Pone el GUION EN VIVO a una libreta oral A2 YA HECHA (DELEA2_..._oral_profesora.html), sin el motor ni los datos: |
| `claude/adaptar_motor.py` | 4 KB | Crea DELE_A2_motor_modelo.py a partir de DELE_A2_motor_simulacro.py (sin tocar el original). |
| `claude/anadir_fichas_modelos.py` | 4 KB | Anade las fichas de remedio R08, R10, R13, R14a y R14b a los contenidos de los modelos completos (fuente_Mxx.py). |
| `claude/anadir_modelos_corrector.py` | 3 KB | Añade a curso_tareas.py (MODELOS) la escritura de un modelo completo copiada de su fuente_Mxx.py (uso: python3 anadir_modelos_corrector.py fuente_M02). |
| `claude/arreglar_R06_tiempo.py` | 4 KB | Mete la pestana "Hace y durante" (tiempo_R06.py) en la ficha R06 de preposiciones. |
| `claude/arreglar_seeded.py` | 1 KB | ARREGLO DEL MOTOR DE HUECOS (curso DELE A2, 14/10/2026) |
| `claude/banco_R01_pasados.py` | 32 KB | BANCO DE LA FICHA DE REMEDIO R01: LOS PASADOS Y LAS PREGUNTAS (curso DELE A2) |
| `claude/banco_R02_hay_esta_es.py` | 24 KB | BANCO DE LA FICHA DE REMEDIO R02: HAY / ESTA / ES (curso DELE A2) |
| `claude/banco_R04_concordancia_posesivos.py` | 34 KB | BANCO DE LA FICHA DE REMEDIO R04: CONCORDANCIA Y POSESIVOS (curso DELE A2) |
| `claude/banco_R05_muy_mucho.py` | 37 KB | BANCO DE LA FICHA DE REMEDIO R05: MUY / MUCHO; TAMBIEN / TAMPOCO (curso DELE A2) |
| `claude/banco_R06_preposiciones.py` | 36 KB | BANCO DE LA FICHA DE REMEDIO R06: PREPOSICIONES FRECUENTES (curso DELE A2) |
| `claude/banco_R07_tu_usted.py` | 37 KB | BANCO DE LA FICHA DE REMEDIO R07: TU Y USTED, REGISTRO COHERENTE DEL SALUDO A LA DESPEDIDA (curso DELE A2) |
| `claude/banco_R08_conectores.py` | 41 KB | BANCO DE LA FICHA DE REMEDIO R08: CONECTORES (curso DELE A2) |
| `claude/banco_R10_pronombres.py` | 42 KB | BANCO DE LA FICHA DE REMEDIO R10: LO, LA, LE (curso DELE A2) |
| `claude/banco_R13_funciones.py` | 54 KB | BANCO DE LA FICHA DE REMEDIO R13 DEL CURSO DE PREPARACION DELE A2: LAS FUNCIONES DE LOS CORREOS |
| `claude/banco_R14a_vocabulario.py` | 61 KB | BANCO DE LA FICHA DE REMEDIO R14a: VOCABULARIO EN ESCENAS (1) · LA CASA Y EL DIA A DIA (curso DELE A2) |
| `claude/banco_R14b_vocabulario.py` | 67 KB | BANCO DE LA FICHA DE REMEDIO R14b: VOCABULARIO EN ESCENAS (2) · FUERA DE CASA (curso DELE A2) |
| `claude/banco_banda1_M3.py` | 41 KB | BANCO DE "DE LA BANDA 1 A LA BANDA 2" (MODULO 3 · TALLER DE ESCRITURA · PIEZA 3) DEL CURSO DE PREPARACION DELE A2 |
| `claude/banco_bloqueo_M4.py` | 48 KB | BANCO DE "QUE HACER SI ME BLOQUEO" · ORAL (DELE A2) · curso de preparacion, Modulo 4 |
| `claude/banco_dialogos_T3.py` | 47 KB | BANCO DE DIALOGOS · TAREA 3 DE LA ORAL (DELE A2) · curso de preparacion, Modulo 4 |
| `claude/banco_dosier_M4.py` | 44 KB | BANCO DEL DOSIER ORAL A2 DE ESTRUCTURAS (curso de preparacion DELE A2, Modulo 4, pieza M4-5) |
| `claude/banco_fotos_T2.py` | 70 KB | BANCO DE FOTOS DE LA TAREA 2 DE LA ORAL (curso de preparacion DELE A2, Modulo 4) |
| `claude/banco_frases_M3.py` | 42 KB | BANCO DEL KIT DE FRASES (MODULO 3 · TALLER DE ESCRITURA) DEL CURSO DE PREPARACION DELE A2 |
| `claude/banco_modelos_M3.py` | 47 KB | BANCO DE "TEXTOS MODELO: APROBADO Y EXCELENTE" (MODULO 3 · TALLER DE ESCRITURA · PIEZA 5) DEL CURSO DE PREPARACION DELE A2 |
| `claude/banco_pautas_M3.py` | 39 KB | BANCO DE "LAS PAUTAS COMO LISTA DE CONTROL" (MODULO 3 · TALLER DE ESCRITURA · PIEZA 2) DEL CURSO DE PREPARACION DELE A2 |
| `claude/banco_revision_M3.py` | 32 KB | BANCO DE "LA REVISION FINAL DE 5 MINUTOS" (MODULO 3 · TALLER DE ESCRITURA · PIEZA 4) DEL CURSO DE PREPARACION DELE A2 |
| `claude/banco_temas_T1.py` | 60 KB | BANCO DE TEMAS DE LA TAREA 1 DE LA ORAL: MONOLOGO (curso de preparacion DELE A2, Modulo 4) |
| `claude/build_M0.py` | 33 KB | MODULO 0 DEL CURSO DE PREPARACION DELE A2: CONOCE EL EXAMEN |
| `claude/build_M3_banda1.py` | 66 KB | MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 3: DE LA BANDA 1 A LA BANDA 2 |
| `claude/build_M3_fotos.py` | 5 KB | PROMPTS Y NOMBRES DE LAS FOTOS DEL TALLER DE ESCRITURA (Modulo 3 del curso de preparacion DELE A2) |
| `claude/build_M3_kit_frases.py` | 43 KB | MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 1: KIT DE FRASES POR TIPO DE TEXTO |
| `claude/build_M3_modelos.py` | 66 KB | MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 5: TEXTOS MODELO (APROBADO Y EXCELENTE) |
| `claude/build_M3_pautas.py` | 54 KB | MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 2: LAS PAUTAS COMO LISTA DE CONTROL |
| `claude/build_M3_revision.py` | 60 KB | MODULO 3 DEL CURSO DE PREPARACION DELE A2 · TALLER DE ESCRITURA · PIEZA 4: LA REVISION FINAL DE 5 MINUTOS |
| `claude/build_M4_T1_temas.py` | 65 KB | MODULO 4 DEL CURSO DE PREPARACION DELE A2 · ORAL TAREA 1: MONOLOGO (PRESENTACION DE UN TEMA) |
| `claude/build_M4_T2_foto.py` | 60 KB | MODULO 4 DEL CURSO DE PREPARACION DELE A2 · ORAL TAREA 2: DESCRIPCION DE LA FOTO |
| `claude/build_M4_T3_dialogos.py` | 72 KB | MODULO 4 DEL CURSO DE PREPARACION DELE A2 · ORAL TAREA 3: DIALOGO EN UNA SITUACION IMAGINARIA |
| `claude/build_M4_bloqueo.py` | 77 KB | MODULO 4 DEL CURSO DE PREPARACION DELE A2 · ORAL: QUE HACER SI ME BLOQUEO |
| `claude/build_M4_dosier.py` | 38 KB | DOSIER ORAL A2 DE ESTRUCTURAS (curso de preparacion DELE A2, Modulo 4, pieza M4-5) |
| `claude/build_R01_pasados.py` | 59 KB | FICHA DE REMEDIO R01 DEL CURSO DE PREPARACION DELE A2: LOS PASADOS Y LAS PREGUNTAS |
| `claude/build_R02_hay_esta_es.py` | 60 KB | FICHA DE REMEDIO R02 DEL CURSO DE PREPARACION DELE A2: HAY / ESTA / ES |
| `claude/build_R04_concordancia_posesivos.py` | 72 KB | FICHA DE REMEDIO R04 DEL CURSO DE PREPARACION DELE A2: CONCORDANCIA Y POSESIVOS |
| `claude/build_R05_muy_mucho.py` | 80 KB | FICHA DE REMEDIO R05 DEL CURSO DE PREPARACION DELE A2: MUY / MUCHO; TAMBIEN / TAMPOCO |
| `claude/build_R06_preposiciones.py` | 82 KB | FICHA DE REMEDIO R06 DEL CURSO DE PREPARACION DELE A2: PREPOSICIONES FRECUENTES |
| `claude/build_R07_tu_usted.py` | 70 KB | FICHA DE REMEDIO R07 DEL CURSO DE PREPARACION DELE A2: TU Y USTED, REGISTRO COHERENTE DEL SALUDO A LA DESPEDIDA |
| `claude/build_R08_conectores.py` | 71 KB | FICHA DE REMEDIO R08 DEL CURSO DE PREPARACION DELE A2: CONECTORES (LAS FLECHAS ENTRE FRASES) |
| `claude/build_R10_pronombres.py` | 71 KB | FICHA DE REMEDIO R10 DEL CURSO DE PREPARACION DELE A2: LO, LA, LE (EL PAQUETE Y EL DESTINATARIO) |
| `claude/build_R13_funciones.py` | 72 KB | FICHA DE REMEDIO R13 DEL CURSO DE PREPARACION DELE A2: LAS FUNCIONES DE LOS CORREOS |
| `claude/build_R14a_vocabulario.py` | 91 KB | FICHA DE REMEDIO R14a DEL CURSO DE PREPARACION DELE A2: VOCABULARIO EN ESCENAS (1) · LA CASA Y EL DIA A DIA |
| `claude/build_R14b_vocabulario.py` | 92 KB | FICHA DE REMEDIO R14b DEL CURSO DE PREPARACION DELE A2: VOCABULARIO EN ESCENAS (2) · FUERA DE CASA |
| `claude/build_corrector.py` | 42 KB | CORRECTOR DE LA ESCRITURA DE LA PROFESORA (curso DELE A2) |
| `claude/build_indice.py` | 20 KB | INDICE DEL CURSO DE PREPARACION DELE A2 (solo para la profesora) |
| `claude/build_modelo.py` | 35 KB | BUILD DE LOS MODELOS COMPLETOS DEL CURSO DE PREPARACIÓN DELE A2 (M1-M8) |
| `claude/corrector_curso_nota.txt` | 2 KB | CORRECTOR DE LA ESCRITURA + CURSO DELE A2 (15/10/2026) |
| `claude/corrector_oral.html` | 93 KB | :root{--paper:#FBF9F6;--ink:#14161C;--coral:#E8603C;--coral-soft:#FCE9E1;--cta:#FF6B45; |
| `claude/corrector_tareas.py` | 18 KB | TAREAS DE ESCRITURA QUE CONOCE EL CORRECTOR DE LA PROFESORA |
| `claude/corregir_M06.py` | 21 KB | Corrige fuente_M06.py según lo visto en los exámenes reales (15/10/2026, claude/DELE_A2_examen_real_hallazgos.txt): |
| `claude/css_motor.py` | 12 KB | Copia exacta del CSS de DELE_A2_motor_simulacro.py (el que el motor le pasa a la libreta como base_css). |
| `claude/curso_comun.py` | 7 KB | Piezas comunes de los ejecutables del CURSO DE PREPARACION DELE A2. |
| `claude/curso_tareas.py` | 24 KB | TAREAS DE ESCRITURA DEL CURSO DE PREPARACION DELE A2 QUE CONOCE EL CORRECTOR DE LA PROFESORA |
| `claude/fotos_M3.py` | 9 KB | FOTOS DE LAS LAMINAS DEL TALLER DE ESCRITURA (Modulo 3 del curso de preparacion DELE A2) |
| `claude/fuente_M01.py` | 85 KB | FUENTE DEL MODELO 1 · Curso de preparación DELE A2 (Módulo 2, modelos completos) |
| `claude/fuente_M02.py` | 92 KB | FUENTE DEL MODELO 2 · Curso de preparación DELE A2 (de entrada, perfil + = − =) |
| `claude/fuente_M03.py` | 93 KB | FUENTE DEL MODELO 3 · Curso de preparación DELE A2 (auditiva exigente, perfil = + = =) |
| `claude/fuente_M06.py` | 83 KB | FUENTE DEL MODELO 6 · Curso de preparación DELE A2 (Módulo 2, modelos completos) |
| `claude/fuente_M07.py` | 89 KB | FUENTE DEL MODELO 7 · Curso de preparación DELE A2 (Módulo 2, modelos completos) |
| `claude/fuente_U06.py` | 66 KB | FUENTE DE LA UNIDAD 6 (fase 1) · Guía del ocio |
| `claude/fuente_U07.py` | 69 KB | FUENTE DE LA UNIDAD 7 (fase 1) · ¿Comes de todo? |
| `claude/fuente_U08.py` | 68 KB | FUENTE DE LA UNIDAD 8 (fase 1) · Estamos muy bien |
| `claude/fuente_U09.py` | 69 KB | FUENTE DE LA UNIDAD 9 (fase 1) · Antes y ahora |
| `claude/fuente_U10.py` | 71 KB | FUENTE DE LA UNIDAD 10 (fase 1) · Momentos especiales |
| `claude/libreta_desde_extracto.py` | 1 KB | Genera SOLO la libreta oral de la profesora de un modelo, sin el motor, a partir de un extracto con lo que la |
| `claude/libreta_vivo.py` | 22 KB | GUION EN VIVO para la libreta oral de la profesora (DELE A2) · 2spanishteachers.com |
| `claude/motor_modelo_extra.py` | 21 KB | PIEZAS DE LOS MODELOS COMPLETOS DEL CURSO (M1-M8) que se añaden al motor de los simulacros. |
| `claude/patch_corrector.py` | 16 KB | Anade al corrector de la escritura (corrector_escritura.html, todos los niveles) las tareas del curso de |
| `claude/patch_libreta_vivo.py` | 3 KB | Añade el GUION EN VIVO (libreta_vivo.py) a la libreta oral de la profesora, DELE_oral_profesora.py. |
| `claude/tiempo_R06.py` | 31 KB | R06 PREPOSICIONES FRECUENTES: PESTANA "HACE Y DURANTE" (hace, desde, desde hace, durante, en + tiempo) |
| `claude/transcribir_oral.py` | 17 KB | """ |
| `fuente_U03.py` | 29 KB | FUENTE DE LA UNIDAD 3 (fase 1) · Así somos |
| `fuente_U04.py` | 39 KB | FUENTE DE LA UNIDAD 4 (fase 1) · Hogar, dulce hogar |
| `fuente_U05.py` | 44 KB | FUENTE DE LA UNIDAD 5 (fase 1) · ¿Cómo va todo? |
| `generar_audios.py` | 22 KB | """ |
| `historial/DELE_A2_curso_historial_hasta_23oct.txt` | 187 KB | ESTADO DEL CURSO DE PREPARACIÓN DELE A2 (actualizar en cada chat) |
| `indice_archivos.md` | 13 KB | Índice de archivos · Curso y simulacros DELE A2 |
| `voces.txt` | 10 KB | VOCES DEL PROYECTO DELE (colección DELE de ElevenLabs) · 82 voces (actualizado 22/10/2026) |

Nota: el proyecto tenía dos versiones de `DELE_A2_plantilla_oral_y_tips.txt` (18/09 y 25/09). Se ha guardado la del 25/09, que es la que se lee; la del 18/09 era la versión anterior del mismo documento.
