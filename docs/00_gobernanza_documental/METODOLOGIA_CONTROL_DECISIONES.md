# Metodología de control de decisiones

> Estado: borrador operativo.  
> Fecha: 2026-07-29.

## 1. Unidad mínima

Cada asunto recibe un identificador estable:

- `ID-##`: identidad, nombre y domicilio.
- `PAT-##`: patrimonio y aportes.
- `GOB-##`: gobierno, administración y controles.
- `OBJ-##`: objeto, fines y beneficiarios.
- `DON-##`: donaciones, fondos y franquicias.
- `DIG-##`: activos y tecnologías digitales.
- `NOR-##`: verificación normativa.
- `REP-##`: arquitectura y continuidad de repositorios.
- `PUB-##`: publicidad, reserva y clasificación.

Un ID no se reutiliza. Una decisión sustituida conserva su registro y apunta al ID que la reemplaza.

## 2. Dos estados distintos

El registro separa:

- **Estado decisorio:** pendiente, aprobada, aprobada con consolidación pendiente, descartada o sustituida.
- **Estado de integridad:** completa, parcial o brecha.

“Aprobada” no significa necesariamente “íntegramente preservada”.

## 3. Campos obligatorios

Cada registro contiene:

- identificador y título;
- estado decisorio;
- estado de integridad;
- clasificación pública o reservada;
- decisión o descripción expresa de la brecha;
- fecha conocida o `null`;
- fuentes y evidencia;
- documentos de destino;
- dependencias y contradicciones;
- acción siguiente;
- instrucción para agentes.

## 4. Ciclo

1. Levantamiento.
2. Deliberación.
3. Aprobación humana.
4. Consolidación.
5. Mapeo documental.
6. Implementación mediante PR.
7. Verificación semántica.
8. Cierre humano y registro del commit.

## 5. Regla para agentes IA

Los agentes pueden preparar, comparar, detectar omisiones y proponer texto. No pueden:

- marcar una decisión como aprobada;
- convertir una síntesis incompleta en contenido normativo;
- cerrar una brecha de evidencia;
- elegir entre alternativas fundacionales;
- fusionar un PR o declarar un documento final sin autorización humana.

Cuando falte información, registran `integridad: brecha` y una acción de recuperación.

## 6. Publicidad y reserva

La fase constituyente es pública por defecto desde el 29 de julio de 2026. Cada registro indica:

- `clasificacion: publico`, si puede incorporarse íntegramente;
- `clasificacion: reservado`, si existe razón concreta de protección.

La autorización no opera retroactivamente sobre conversaciones o documentos históricos no revisados. El índice público de una decisión reservada conservará, cuando sea posible, un resumen no sensible, su estado y una referencia controlada.

Los agentes no pueden desclasificar contenido ni usar la reserva para ocultar brechas, errores o desacuerdos.

## 7. Control de cambios

Todo PR que altere Estatutos, Reglamento, políticas o anexos indica:

- IDs afectados;
- texto anterior y propuesto;
- si preserva, implementa, modifica o contradice cada decisión;
- fundamento jurídico verificado y fecha;
- decisión humana requerida;
- resultado del validador estructural.

No se mezclan recuperación de decisiones perdidas y redacción jurídica final, salvo revisión separable en el cuerpo del PR.

## 8. Índice de integridad

| Dimensión | Peso |
|---|---:|
| Contenido decisorio completo. | 30. |
| Evidencia de origen y aprobación. | 20. |
| Destino documental identificado. | 20. |
| Implementación vinculada a commit o PR. | 20. |
| Validación humana o jurídica registrada. | 10. |

El puntaje no reemplaza el juicio humano. Una brecha de contenido impide declarar la decisión íntegramente implementada.

## 9. Situación heredada

El hilo paralelo terminó afirmando que `GOB-03` a `GOB-09` estaban aprobadas, pero el resumen no conservó su contenido individual. La pérdida se registra como brecha y deberá recuperarse desde la conversación completa o mediante ratificación humana; no se reconstruirá por inferencia.
