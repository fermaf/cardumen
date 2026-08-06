# Metodología de control de decisiones

> Estado: borrador operativo.  
> Fecha: 2026-07-29.

## 1. Unidad mínima

Cada asunto recibe un identificador estable: `ID-##`, `PAT-##`, `GOB-##`, `OBJ-##`, `DON-##`, `DIG-##`, `NOR-##`, `REP-##` o `PUB-##`. Un ID no se reutiliza.

## 2. Dos estados distintos

- **Estado decisorio:** pendiente, aprobada, aprobada con consolidación pendiente, descartada o sustituida.
- **Estado de integridad:** completa, parcial o brecha.

“Aprobada” no significa que exista texto jurídico definitivo ni implementación final.

## 3. Ciclo

1. Levantamiento.
2. Deliberación.
3. Aprobación humana.
4. Consolidación jurídica y documental.
5. Implementación mediante PR.
6. Verificación semántica.
7. Cierre humano y registro del commit.

## 4. Regla para agentes IA

Los agentes pueden preparar, comparar, detectar omisiones y proponer texto. No pueden marcar una decisión como aprobada, completar una brecha por inferencia, elegir alternativas fundacionales, fusionar un PR ni declarar un documento final sin autorización humana.

## 5. Publicidad y reserva

La fase constituyente es pública por defecto desde el 29 de julio de 2026. La reserva es excepcional, previa y justificada. La publicidad de una deliberación no la transforma en acuerdo institucional ni en texto jurídico vigente.

## 6. Control de cambios

Todo PR que altere Estatutos, Reglamento, políticas o anexos debe indicar IDs afectados, texto anterior y propuesto, fundamento jurídico verificado, decisión humana requerida y resultado del validador.

## 7. Recuperación de 2026-07-29

La recuperación desde `Proyecto_ONG_Cardumen_conversacion_completa.md` se conserva en [EVIDENCIA_RECUPERACION_2026-07-29.md](EVIDENCIA_RECUPERACION_2026-07-29.md). Sustituye la premisa anterior que calificaba como brechas a GOB-01, GOB-03 a GOB-09, GOB-11 a GOB-12 y el contenido base de GOB-13.

La siguiente etapa no es redactar por inferencia: es contrastar estas decisiones con la pestaña “ESTATUTOS (JUNIO)”, verificar la normativa chilena aplicable y generar una propuesta armonizada separando Estatutos, Reglamento, políticas y matrices.
