#!/usr/bin/env python3
"""Valida la estructura mínima de los registros de decisiones."""

import json
import sys
from pathlib import Path


RUTAS_REGISTROS = (
    Path("docs/00_gobernanza_documental/PLANTILLA_REGISTRO_DECISIONES.json"),
    Path("docs/00_gobernanza_documental/REGISTRO_DECISIONES.json"),
)
ESTADOS_DECISORIOS = {
    "pendiente",
    "aprobada",
    "aprobada_consolidacion_pendiente",
    "descartada",
    "sustituida",
}
ESTADOS_INTEGRIDAD = {"completa", "parcial", "brecha"}
CLASIFICACIONES = {"publico", "reservado"}
CAMPOS_OBLIGATORIOS = {
    "id",
    "titulo",
    "estado_decisorio",
    "integridad",
    "clasificacion",
    "decision",
    "fecha",
    "fuentes",
    "evidencia_aprobacion",
    "destinos",
    "dependencias",
    "contradicciones",
    "accion_siguiente",
    "instruccion_agente",
}


def cargar_registro(ruta: Path) -> dict:
    """Carga un registro JSON desde una ruta controlada."""
    with ruta.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def validar_decision(decision: dict, identificadores: set[str]) -> list[str]:
    """Comprueba identidad, estados y consistencia estructural."""
    errores: list[str] = []
    faltantes = CAMPOS_OBLIGATORIOS - set(decision)
    if faltantes:
        errores.append(f"Faltan campos: {sorted(faltantes)}")
        return errores

    identificador = decision["id"]
    if identificador in identificadores:
        errores.append("Identificador duplicado.")
    identificadores.add(identificador)

    if decision["estado_decisorio"] not in ESTADOS_DECISORIOS:
        errores.append("Estado decisorio no permitido.")
    if decision["integridad"] not in ESTADOS_INTEGRIDAD:
        errores.append("Estado de integridad no permitido.")
    if decision["clasificacion"] not in CLASIFICACIONES:
        errores.append("Clasificación no permitida.")
    if not decision["fuentes"]:
        errores.append("Debe existir al menos una fuente.")
    if not decision["accion_siguiente"]:
        errores.append("Debe existir una acción siguiente.")
    if not decision["instruccion_agente"]:
        errores.append("Debe existir una instrucción para agentes.")

    if decision["integridad"] == "completa":
        if not decision["decision"]:
            errores.append("Integridad completa exige contenido decisorio.")
        if not decision["evidencia_aprobacion"]:
            errores.append("Integridad completa exige evidencia de aprobación.")
        if not decision["destinos"]:
            errores.append("Integridad completa exige destinos documentales.")

    if decision["integridad"] == "brecha":
        if decision["decision"] is not None:
            errores.append("Una brecha exige decision=null hasta su recuperación.")
        if "inferir" not in decision["instruccion_agente"].lower():
            errores.append("La instrucción de una brecha debe prohibir inferencias.")

    return errores


def calcular_indicadores(decisiones: list[dict]) -> dict[str, int]:
    """Calcula indicadores sin ocultar brechas semánticas."""
    return {
        "total": len(decisiones),
        "integridad_completa": sum(d["integridad"] == "completa" for d in decisiones),
        "integridad_parcial": sum(d["integridad"] == "parcial" for d in decisiones),
        "brechas": sum(d["integridad"] == "brecha" for d in decisiones),
        "pendientes": sum(d["estado_decisorio"] == "pendiente" for d in decisiones),
        "reservadas": sum(d["clasificacion"] == "reservado" for d in decisiones),
    }


def validar_registro(ruta: Path) -> tuple[list[str], dict[str, int] | None]:
    """Valida un registro completo y devuelve errores e indicadores."""
    try:
        registro = cargar_registro(ruta)
    except (OSError, json.JSONDecodeError) as error:
        return [f"No fue posible cargar el registro: {error}"], None

    decisiones = registro.get("decisiones")
    if not isinstance(decisiones, list):
        return ["El campo decisiones debe ser una lista."], None

    errores: list[str] = []
    identificadores: set[str] = set()
    for decision in decisiones:
        identificador = decision.get("id", "SIN-ID")
        for error in validar_decision(decision, identificadores):
            errores.append(f"{identificador}: {error}")

    return errores, calcular_indicadores(decisiones)


def main() -> int:
    """Ejecuta todas las validaciones para integración continua."""
    hubo_errores = False
    for ruta in RUTAS_REGISTROS:
        errores, indicadores = validar_registro(ruta)
        if errores:
            hubo_errores = True
            print(f"VALIDACIÓN FALLIDA: {ruta}")
            for error in errores:
                print(f"- {error}")
            continue

        print(f"VALIDACIÓN ESTRUCTURAL APROBADA: {ruta}")
        for nombre, valor in (indicadores or {}).items():
            print(f"- {nombre}: {valor}")

    print("ADVERTENCIA: la validación estructural no reemplaza la revisión semántica ni la aprobación humana.")
    return 1 if hubo_errores else 0


if __name__ == "__main__":
    sys.exit(main())
