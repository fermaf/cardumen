# Protocolo de ejecución guiada para modelos de menor capacidad

> Estado: operativo para la fase de armonización D3.  
> Fecha de corte: 2026-07-31.  
> Repositorio: `fermaf/cardumen`.  
> Rama de trabajo: `agent/gobernanza-decisiones-integridad`.  
> PR: #5.  
> Regla rectora: el modelo lee, contrasta y propone; la persona decide. No se completa ninguna brecha por inferencia.

## 1. Propósito

Este protocolo permite continuar la corrección de los Estatutos con un modelo de inferencia de menor capacidad, especialmente GPT-5.6 Luna, sin depender de memoria conversacional débil.

El modelo no debe reconstruir por intuición el estado del proyecto. Antes de actuar debe leer las fuentes indicadas, declarar la línea base que encontró y ejecutar una sola unidad de corrección por ciclo.

La palabra **“continuemos”** significa exclusivamente:

1. leer o refrescar las fuentes obligatorias;
2. localizar la siguiente unidad elegible;
3. presentar una ficha de corrección;
4. deliberar con la persona;
5. registrar el resultado sólo después de una respuesta humana inequívoca.

No significa redactar varios artículos, cerrar comentarios, modificar Drive, aprobar decisiones ni fusionar el PR.

## 2. Jerarquía de autoridad

Cuando dos fuentes difieran, se aplica este orden:

1. Normativa chilena vigente verificada en fuente oficial.
2. Decisión humana expresa registrada con evidencia.
3. `REGISTRO_DECISIONES.json`.
4. Este protocolo y `PLAN_ARMONIZACION_ESTATUTOS_2026-07-31.md`.
5. Texto vigente de la pestaña `ESTATUTOS (JUNIO)` y sus comentarios.
6. Levantamiento integral y matrices del PR #5.
7. Borradores D2 y anteriores.
8. Inferencias o recomendaciones del modelo.

Una fuente de menor jerarquía no puede alterar otra superior. Los números, fechas y referencias normativas de los documentos de trabajo deben verificarse antes de usarse como fundamento.

## 3. Lectura obligatoria al iniciar o reanudar

Antes de responder al primer “continuemos” de una sesión, el modelo debe leer en este orden:

1. `docs/00_gobernanza_documental/PROTOCOLO_EJECUCION_GUIADA_MODELO_LIGERO.md`.
2. `docs/00_gobernanza_documental/METODOLOGIA_CONTROL_DECISIONES.md`.
3. `docs/00_gobernanza_documental/REGISTRO_DECISIONES.json`.
4. `docs/00_gobernanza_documental/PLAN_ARMONIZACION_ESTATUTOS_2026-07-31.md`.
5. `docs/01_borradores/LEVANTAMIENTO_INTEGRAL_ESTATUTOS_JUNIO_2026-07-31.md`.
6. `docs/01_borradores/MATRIZ_COMENTARIOS_ESTATUTOS_JUNIO_D2.md`.
7. La revisión actual de la pestaña `ESTATUTOS (JUNIO)` y los comentarios aplicables.
8. El último borrador D3, la bitácora y la matriz de cambios, si ya existen.

Luego debe informar brevemente:

- repositorio, rama y commit leídos;
- revisión de Google Docs, si está disponible;
- última unidad cerrada;
- siguiente unidad elegible;
- bloqueos detectados.

Si no puede leer una fuente obligatoria, debe detenerse y decir exactamente cuál falta. No debe sustituirla por memoria.

## 4. Unidad mínima de trabajo

Una unidad es una corrección sustantiva identificable. Puede afectar una cláusula o varios artículos sólo cuando resuelven el mismo problema jurídico o semántico.

Cada unidad recibe un ID estable:

- `OBJ-##`: objeto, fines y actividades;
- `ID-##`: identidad y domicilio;
- `PAT-##`: patrimonio;
- `GOB-##`: gobierno;
- `DON-##`: donaciones y financiamiento;
- `DIG-##`: activos y operación digital;
- `NOR-##`: adecuación normativa;
- `COM-F##`: comentario de Fernando;
- `COM-G##`: comentario de Gonzalo, siempre reservado a discusión humana;
- `TRI-##`: disposiciones transitorias.

Un ID nunca se reutiliza. Las correcciones puramente ortográficas pueden agruparse; toda modificación que cambie alcance, deberes, facultades, quórums, patrimonio, responsabilidad o efectos jurídicos requiere unidad propia.

## 5. Ciclo obligatorio por unidad

### Paso 1 — Seleccionar

Elegir la primera unidad pendiente que:

- pertenezca a la fase activa;
- tenga fuentes suficientes;
- no esté reservada a decisión humana previa;
- no corresponda a un comentario de Gonzalo.

No saltar a una unidad “más fácil” sin explicarlo.

### Paso 2 — Leer el contexto local

Leer el artículo completo, los artículos relacionados, el comentario asociado, la decisión registrada y la normativa aplicable.

No analizar una frase aislada si su significado depende de otro artículo, del Reglamento o de una política.

### Paso 3 — Clasificar el problema

Usar una o más categorías:

- ilegalidad o incompatibilidad normativa;
- contradicción interna;
- duplicidad o circularidad;
- vacío;
- ambigüedad;
- exceso reglamentario;
- detalle técnico cambiante;
- problema semántico u ontológico;
- comentario improcedente;
- decisión humana pendiente.

### Paso 4 — Presentar la ficha

El modelo debe usar siempre esta estructura:

```text
ID:
Bloque y artículo:
Estado actual:
Texto vigente relevante:
Problema identificado:
Autoridad o fuente:
Tipo de intervención: obligatoria / coherencia / recomendada / decisión humana.
Propuesta:
Efectos en otros artículos o documentos:
Destino: Estatutos / Reglamento / política / matriz / ninguno.
Pregunta humana: [una sola pregunta, sólo si es necesaria].
```

La propuesta debe ser mínima: corregir el problema sin reescribir materias no discutidas.

### Paso 5 — Deliberar

La persona puede responder con una de estas órdenes:

- `APROBAR`: acepta el sentido y el texto.
- `APROBAR SENTIDO`: acepta la decisión, pero permite una última depuración de redacción.
- `AJUSTAR: ...`: exige el cambio indicado.
- `DESCARTAR`: rechaza la propuesta.
- `RESERVAR`: deja la unidad pendiente para discusión humana posterior.
- `INVESTIGAR`: exige verificación adicional antes de decidir.

Una aceptación ambigua, una pregunta o una conversación exploratoria no equivalen a aprobación.

### Paso 6 — Registrar

Después de una orden inequívoca, registrar:

- ID;
- fecha;
- artículo;
- estado decisorio;
- texto anterior;
- texto aprobado o sentido aprobado;
- fundamento;
- fuentes;
- destino documental;
- dependencias;
- persona que decidió;
- commit o referencia pendiente.

Actualizar `REGISTRO_DECISIONES.json` cuando cambie una decisión fundacional. Registrar toda corrección D3 en la matriz de cambios o bitácora correspondiente.

### Paso 7 — Integrar

Aplicar la corrección sólo en el borrador D3. No sobrescribir D2, el texto canónico ni Google Docs durante la deliberación.

Una corrección aprobada no se considera implementada hasta que figure en:

1. borrador D3;
2. registro o matriz de cambios;
3. commit de la rama del PR #5.

### Paso 8 — Verificar

Comprobar:

- que el texto conserva la decisión humana;
- que no crea contradicciones;
- que las referencias cruzadas funcionan;
- que no introduce datos personales;
- que el asunto queda en el documento correcto;
- que no se resolvió una materia distinta por accidente.

Informar `PASS` o `BLOCKED`, con una frase de fundamento.

### Paso 9 — Cerrar el ciclo

Terminar indicando:

```text
Unidad: [ID]
Decisión: [...]
Implementación: pendiente / aplicada
Registro: pendiente / actualizado
Verificación: PASS / BLOCKED
Siguiente unidad: [...]
```

No comenzar otra unidad en la misma respuesta salvo orden humana expresa.

## 6. Persistencia y escritura

### GitHub

GitHub es el registro canónico de decisiones y trazabilidad. Cada corrección aprobada debe quedar incorporada a la rama del PR #5.

Los commits pueden agrupar correcciones estrechamente relacionadas, pero ninguna corrección sustantiva puede quedar fuera del registro.

### Google Docs

Google Docs es la base material de discusión. Durante la elaboración D3:

- leer el texto y los comentarios;
- no cerrar comentarios;
- no responder comentarios;
- no reemplazar el texto vigente;
- no modificar los dos comentarios de Gonzalo.

Drive se actualiza sólo en la Fase 9, después de la aprobación humana de D3.

### Conversación

La conversación sirve para deliberar, no como único registro. Una decisión no debe depender de que el modelo recuerde un mensaje antiguo.

## 7. Reglas KISS de redacción

1. Una regla debe aparecer una sola vez.
2. Los Estatutos contienen reglas estables; los procedimientos van al Reglamento; los controles variables, a políticas o matrices.
3. Evitar enumeraciones superpuestas, cláusulas circulares y habilitaciones ilimitadas.
4. Evitar anglicismos cuando existe una expresión española suficientemente precisa.
5. Evitar detalle técnico que envejezca el objeto fundacional.
6. No transformar principios en acumulaciones hiperbólicas de adjetivos.
7. Distinguir obligación legal, decisión fundacional y recomendación.
8. Conservar placeholders cuando falte una decisión humana.
9. La inteligencia artificial y los agentes pueden tener autonomía operativa, pero no desplazan dirección, aprobación ni responsabilidad humanas.

## 8. Límites del modelo

El modelo debe detenerse y escalar cuando:

- falta una fuente obligatoria;
- dos decisiones humanas registradas se contradicen;
- la norma vigente no está verificada;
- el cambio altera la arquitectura completa de gobierno;
- existe riesgo tributario, laboral, patrimonial o regulatorio no resuelto;
- la solución exige escoger nombre, persona, cargo inicial, beneficiario o entidad destinataria;
- el asunto corresponde a un comentario de Gonzalo;
- se requiere publicar datos personales;
- no puede escribir o verificar el registro persistente.

Debe decir `BLOCKED`, explicar el motivo y formular como máximo una pregunta concreta.

## 9. Distribución de trabajo entre modelos

### GPT-5.6 Sol

Usar para:

- diseñar o modificar esta metodología;
- resolver conflictos entre normas o fuentes;
- rediseñar la arquitectura de varios títulos;
- evaluar problemas jurídicos nuevos o inciertos;
- revisar semántica y ontología de alto impacto;
- auditar la D3 completa y emitir el control final.

### GPT-5.6 Luna

Usar para:

- ejecutar unidades ya delimitadas;
- extraer y comparar textos;
- completar fichas con el formato obligatorio;
- aplicar decisiones humanas explícitas;
- actualizar matrices y registros;
- verificar consistencia local;
- producir respuestas breves a comentarios ya resueltos.

Luna no debe decidir por sí sola cuestiones fundacionales ni resolver incertidumbres jurídicas nuevas.

### Retorno a Sol

Volver a Sol cuando se active cualquiera de los límites de la sección 8, al terminar cada bloque o antes de declarar completa la D3.

## 10. Punto actual de reanudación

Al corte de este protocolo:

- El PR #5 está abierto y en borrador.
- `REGISTRO_DECISIONES.json` v0.4.0 contiene 18 entradas: 16 completas, 2 parciales, 0 brechas y 1 decisión pendiente.
- `ID-01`, nombre legal y relación con Cardumen, continúa pendiente.
- La membresía con voto está descartada.
- Los períodos iniciales son 3, 4 y 5 años; el período ordinario posterior es de 5 años.
- Los dos comentarios de Gonzalo permanecen reservados a discusión humana.
- No se ha autorizado cerrar comentarios ni sustituir la pestaña `ESTATUTOS (JUNIO)`.
- El artículo cuarto se encuentra en deliberación y todavía no tiene texto final aprobado.

### Próxima unidad

`OBJ-01 — Artículo Cuarto: objeto general`.

Criterios ya expresados durante la deliberación, aún sujetos a consolidación:

- evitar redundancia entre objeto, fines, actividades y tecnologías;
- conservar un objeto suficientemente amplio, pero no hiperbólico;
- incluir inteligencia artificial y el entorno de agentes autónomos o semiautónomos bajo dirección, supervisión y responsabilidad humanas;
- evitar el calificativo “responsable” como parte del nombre de la inteligencia artificial;
- reducir anglicismos y detalle técnico de nicho;
- eliminar cláusulas interpretativas circulares;
- distinguir autonomía tecnológica, soberanía digital, derechos digitales y capacidades institucionales sin repetirlos;
- no presentar como aprobado el último texto conversacional.

La siguiente ejecución debe presentar la ficha `OBJ-01`, contrastada con los artículos cuarto, quinto y sexto, el levantamiento y la normativa aplicable. No debe proponer todavía una versión completa de D3.

## 11. Instrucción de arranque para GPT-5.6 Luna

Usar este texto al cambiar de modelo o al iniciar una conversación nueva:

```text
Trabaja en fermaf/cardumen, PR #5, rama agent/gobernanza-decisiones-integridad.

Antes de razonar, lee íntegramente:
1. docs/00_gobernanza_documental/PROTOCOLO_EJECUCION_GUIADA_MODELO_LIGERO.md
2. docs/00_gobernanza_documental/METODOLOGIA_CONTROL_DECISIONES.md
3. docs/00_gobernanza_documental/REGISTRO_DECISIONES.json
4. docs/00_gobernanza_documental/PLAN_ARMONIZACION_ESTATUTOS_2026-07-31.md
5. docs/01_borradores/LEVANTAMIENTO_INTEGRAL_ESTATUTOS_JUNIO_2026-07-31.md
6. docs/01_borradores/MATRIZ_COMENTARIOS_ESTATUTOS_JUNIO_D2.md
7. la revisión actual de la pestaña ESTATUTOS (JUNIO) de Google Docs.

No reconstruyas decisiones desde memoria ni completes vacíos por inferencia. Confirma la línea base y ejecuta una sola unidad según el protocolo.

“Continuemos” significa preparar la siguiente ficha de corrección elegible. El punto actual es OBJ-01, artículo cuarto. No edites Drive, no cierres comentarios y no resuelvas los comentarios de Gonzalo.
```

En la misma conversación, después de ejecutar correctamente esta instrucción una vez, basta decir **“continuemos”**. En una conversación nueva debe repetirse la instrucción de arranque o existir una instrucción de proyecto equivalente.
