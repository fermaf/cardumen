# Metodología de control de decisiones

> Estado: borrador operativo.  
> Fecha: 2026-07-29.

## 1. Unidad mínima

Cada asunto recibe un identificador estable por dominio:

- `ID-##`: identidad, nombre y domicilio.
- `PAT-##`: patrimonio y aportes.
- `GOB-##`: gobierno, administración y controles.
- `OBJ-##`: objeto, fines y beneficiarios.
- `DON-##`: donaciones, fondos y franquicias.
- `DIG-##`: activos y tecnologías digitales.
- `NOR-##`: verificación normativa.

Un ID no se reutiliza. Una decisión sustituida conserva su registro y apunta al ID que la reemplaza.

## 2. Dos estados distintos

El registro separa:

- **Estado decisorio:** pendiente, aprobada, aprobada con consolidación pendiente, descartada o sustituida.
- **Estado de integridad:** completa, parcial o brecha.

“Aprobada” no significa necesariamente “íntegramente preservada”. Este principio permite reconocer acuerdos humanos sin inventar el contenido que se perdió.

## 3. Campos obligatorios

Cada registro debe contener:

- identificador y título;
- estado decisorio;
- estado de integridad;
- decisión o descripción expresa de la brecha;
- fecha conocida o `null`;
- fuente y evidencia;
- documentos de destino;
- dependencias y contradicciones;
- acción siguiente;
- instrucción para agentes.

## 4. Ciclo de una decisión

1. **Levantada:** existe una pregunta o problema identificado.
2. **Deliberación:** alternativas y riesgos quedan documentados.
3. **Aprobación humana:** se conserva una evidencia inequívoca.
4. **Consolidación:** se redacta la decisión completa sin inducir contenido nuevo.
5. **Mapeo:** se asignan documentos, artículos o políticas de destino.
6. **Implementación:** un PR aplica el cambio.
7. **Verificación:** se compara semánticamente el texto con la decisión.
8. **Cierre:** una persona autoriza el cierre y se registra el commit.

## 5. Regla para agentes IA

Los agentes pueden preparar, comparar, detectar omisiones y proponer texto. No pueden:

- marcar una decisión como aprobada;
- convertir una síntesis incompleta en contenido normativo;
- cerrar una brecha de evidencia;
- elegir entre alternativas fundacionales;
- fusionar un PR o declarar un documento final sin autorización humana.

Cuando falte información, deben registrar `integridad: brecha` y formular una acción de recuperación.

## 6. Control de cambios

Todo PR que altere Estatutos, Reglamento, políticas o anexos deberá indicar:

- IDs afectados;
- texto anterior y propuesto;
- si preserva, implementa, modifica o contradice cada decisión;
- fundamento jurídico verificado y fecha;
- decisión humana requerida;
- resultado del validador estructural.

No se mezclan en un mismo PR la recuperación de decisiones perdidas y la redacción jurídica final, salvo que el cuerpo del PR permita revisarlas separadamente.

## 7. Índice de integridad

La evaluación por decisión usa cinco dimensiones:

| Dimensión | Peso |
|---|---:|
| Contenido decisorio completo. | 30. |
| Evidencia de origen y aprobación. | 20. |
| Destino documental identificado. | 20. |
| Implementación vinculada a commit o PR. | 20. |
| Validación humana/jurídica registrada. | 10. |

El puntaje no reemplaza el juicio humano. Sirve para detectar dónde se perdió la cadena de custodia. Una brecha en contenido decisorio impide declarar la decisión íntegramente implementada aunque el total numérico sea alto.

## 8. Situación heredada que origina este sistema

El hilo paralelo terminó afirmando que `GOB-03` a `GOB-09` estaban aprobadas, pero el resumen final no conservó el contenido individual de esas siete decisiones. Es una pérdida de procedencia y contenido. Se registra como brecha explícita y deberá recuperarse desde la conversación completa o mediante ratificación humana; no se reconstruirá por inferencia.
