# Protocolo de ejecución guiada para modelos de menor capacidad

> Estado: operativo para la fase de armonización D3.  
> Fecha de corte: 2026-07-31.  
> Repositorio: `fermaf/cardumen`.  
> Rama de trabajo: `agent/gobernanza-decisiones-integridad`.  
> PR: #5.  
> Base material y texto de partida: pestaña `ESTATUTOS (JUNIO)` del Google Doc `1BYsJleZ3nFw3vypWR1mXxd4hs5AUQEzEuaCpZVWOjfU`.  
> Función de GitHub: referencia, recuperación de decisiones y trazabilidad; no sustituye el texto de Google Drive.  
> Regla rectora: el modelo lee, contrasta y propone; la persona decide. No se completa ninguna brecha por inferencia.

## 1. Propósito

Este protocolo permite continuar la corrección de los Estatutos con un modelo de inferencia de menor capacidad, especialmente GPT-5.6 Luna, sin depender de memoria conversacional débil.

El modelo no debe reconstruir por intuición el estado del proyecto. Antes de actuar debe leer la revisión vigente de Google Drive, identificar los comentarios de Fernando vinculados a la unidad y contrastarlos con las fuentes de referencia. Debe declarar la línea base que encontró y ejecutar una sola unidad de corrección por ciclo.

La palabra **“continuemos”** significa exclusivamente:

1. leer o refrescar las fuentes obligatorias;
2. localizar la siguiente unidad elegible;
3. presentar una ficha de corrección;
4. deliberar con la persona;
5. registrar el resultado sólo después de una respuesta humana inequívoca.

No significa redactar varios artículos, cerrar comentarios, modificar Drive, aprobar decisiones ni fusionar el PR.

## 2. Base material, autoridad y referencias

No debe confundirse el texto que se corrige con las fuentes que orientan la corrección.

- **Base material:** la revisión vigente de la pestaña `ESTATUTOS (JUNIO)` de Google Drive. Toda propuesta debe partir de su texto exacto y de su estructura actual.
- **Comentarios de Fernando:** son insumos obligatorios de análisis y resolución. Cada comentario aplicable debe identificarse, evaluarse y recibir una salida fundada: acogido, acogido parcialmente, descartado, pendiente o reservado. No puede omitirse por el solo hecho de no aparecer en GitHub.
- **Comentarios de Gonzalo:** se conservan para discusión humana posterior y no se resuelven automáticamente.
- **Autoridad jurídica:** normativa chilena vigente verificada en fuente oficial.
- **Autoridad decisoria:** instrucciones humanas expresas y decisiones registradas con evidencia.
- **GitHub y PR #5:** contienen referencias, levantamientos, decisiones recuperadas y trazabilidad. Sirven para contrastar y registrar; no reemplazan ni gobiernan por sí solos el texto de Google Drive.
- **Borradores D2 y anteriores:** son antecedentes comparativos, nunca la base automática de D3.
- **Inferencias del modelo:** sólo pueden formularse como propuestas.

Si el texto de Google Drive contradice una norma o una decisión humana vigente, el modelo debe mostrar la contradicción y proponer su corrección. No debe sustituir silenciosamente el texto base. Los comentarios de Fernando son importantes y obligatorios de procesar, pero no se convierten por sí solos en normas ni decisiones aprobadas.

## 3. Lectura obligatoria al iniciar o reanudar

Antes de responder al primer “continuemos” de una sesión, el modelo debe leer en este orden:

1. `docs/00_gobernanza_documental/PROTOCOLO_EJECUCION_GUIADA_MODELO_LIGERO.md`, para conocer el procedimiento.
2. La revisión actual completa de la pestaña `ESTATUTOS (JUNIO)` de Google Drive, con su `revisionId`, `tabId` y estructura.
3. Todos los comentarios abiertos y resueltos pertinentes de Fernando, conservando su anclaje al texto; identificar separadamente los comentarios de Gonzalo.
4. `docs/01_borradores/LEVANTAMIENTO_INTEGRAL_ESTATUTOS_JUNIO_2026-07-31.md`.
5. `docs/01_borradores/MATRIZ_COMENTARIOS_ESTATUTOS_JUNIO_D2.md`.
6. `docs/00_gobernanza_documental/REGISTRO_DECISIONES.json`.
7. `docs/00_gobernanza_documental/METODOLOGIA_CONTROL_DECISIONES.md`.
8. `docs/00_gobernanza_documental/PLAN_ARMONIZACION_ESTATUTOS_2026-07-31.md`.
9. El último borrador D3, la bitácora y la matriz de cambios, si ya existen.
10. D2 y otros archivos de GitHub sólo cuando sean necesarios como referencia histórica.

Luego debe informar brevemente:

- Google Doc, pestaña, `revisionId` y `tabId` usados como base;
- comentarios de Fernando vinculados a la unidad y su estado;
- repositorio, rama y commit consultados como referencia;
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

Leer desde Google Drive el artículo completo y los artículos relacionados. Después leer todos los comentarios de Fernando asociados, la decisión registrada y la normativa aplicable. GitHub se consulta como referencia y trazabilidad.

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

GitHub es el registro persistente de decisiones, antecedentes y trazabilidad. No es la base textual de la corrección. Cada corrección aprobada debe quedar incorporada a la rama del PR #5 como evidencia de lo deliberado sobre Google Drive.

Los commits pueden agrupar correcciones estrechamente relacionadas, pero ninguna corrección sustantiva puede quedar fuera del registro.

### Google Docs

Google Docs es la base material y el texto de partida de la corrección. Los comentarios de Fernando son insumos obligatorios del proceso. Durante la elaboración D3:

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

- La pestaña `ESTATUTOS (JUNIO)` de Google Drive es la base textual vigente de la corrección.
- El PR #5 está abierto y en borrador y se usa como referencia y trazabilidad.
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

La siguiente ejecución debe leer desde Google Drive los artículos cuarto, quinto y sexto, junto con los comentarios de Fernando que los afecten; después debe contrastarlos con el levantamiento, las decisiones recuperadas y la normativa aplicable. Debe presentar la ficha `OBJ-01` y no proponer todavía una versión completa de D3.

## 11. Instrucción de arranque para GPT-5.6 Luna

Usar este texto al cambiar de modelo o al iniciar una conversación nueva:

```text
La base textual de la corrección es la pestaña ESTATUTOS (JUNIO) del Google Doc:
https://docs.google.com/document/d/1BYsJleZ3nFw3vypWR1mXxd4hs5AUQEzEuaCpZVWOjfU/edit?tab=t.v0xtswn6rj85

GitHub fermaf/cardumen, PR #5 y rama agent/gobernanza-decisiones-integridad son referencias y registro de trazabilidad; no sustituyen el documento de Google Drive.

Antes de razonar:
1. Lee íntegramente docs/00_gobernanza_documental/PROTOCOLO_EJECUCION_GUIADA_MODELO_LIGERO.md.
2. Lee la revisión vigente completa de ESTATUTOS (JUNIO), registra revisionId y tabId.
3. Lee y vincula todos los comentarios pertinentes de Fernando. Son insumos obligatorios de análisis; no los omitas aunque no aparezcan en GitHub.
4. Identifica por separado los comentarios de Gonzalo y no los resuelvas.
5. Consulta el levantamiento, la matriz, REGISTRO_DECISIONES.json y el plan del PR #5 como antecedentes y restricciones.

No reconstruyas decisiones desde memoria ni completes vacíos por inferencia. Confirma primero la línea base de Google Drive y ejecuta una sola unidad según el protocolo.

“Continuemos” significa preparar la siguiente ficha de corrección elegible. El punto actual es OBJ-01, artículo cuarto. No edites Drive ni cierres comentarios durante la deliberación.
```

En la misma conversación, después de ejecutar correctamente esta instrucción una vez, basta decir **“continuemos”**. En una conversación nueva debe repetirse la instrucción de arranque o existir una instrucción de proyecto equivalente.
