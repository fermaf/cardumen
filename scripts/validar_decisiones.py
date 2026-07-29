#!/usr/bin/env python3
"""Valida la estructura mínima del registro de decisiones de Cardumen."""

import json
import sys
from pathlib import Path


RUTA_REGISTRO = Path("docs/00_gobernanza_documental/REGISTRO_MAESTRO_DECISIONES_CARDUMEN.json")
ESTADOS_DECISORIOS = {
    "pendiente",
    "aprobada",
    "aprobada_consolidacion_pendiente",
    "descartada",
    "sustituida",
}
ESTADOS_INTEGRIDAD = {"completa", "parcial", "brecha"}
CAMPOS_OBLIGATORIOS = {
    "id",
    "titulo",
    "estado_decisorio",
    "integridad",
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
    """Carga el registro JSON desde una ruta controlada."""
    with ruta.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def validar_decision(decision: dict, identificadores: set[str]) -> list[str]:
    """Comprueba identidad, estados y consistencia estructural de una decisión."""
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
            errores.append("Una brecha de contenido debe conservar decision=null hasta su recuperación.")
        if "inferir" not in decision["instruccion_agente"].lower():
            errores.append("La instrucción de una brecha debe prohibir inferencias.")

    return errores


def calcular_indicadores(decisiones: list[dict]) -> dict[str, int]:
    """Calcula indicadores simples sin ocultar las brechas semánticas."""
    return {
        "total": len(decisiones),
        "integridad_completa": sum(d["integridad"] == "completa" for d in decisiones),
        "integridad_parcial": sum(d["integridad"] == "parcial" for d in decisiones),
        "brechas": sum(d["integridad"] == "brecha" for d in decisiones),
        "pendientes": sum(d["estado_decisorio"] == "pendiente" for d in decisiones),
    }


def main() -> int:
    """Ejecuta la validación y devuelve un código útil para integración continua."""
    try:
        registro = cargar_registro(RUTA_REGISTRO)
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERROR: no fue posible cargar el registro: {error}")
        return 1

    decisiones = registro.get("decisiones")
    if not isinstance(decisiones, list):
        print("ERROR: el campo decisiones debe ser una lista.")
        return 1

    errores_totales: list[str] = []
    identificadores: set[str] = set()

    for decision in decisiones:
        identificador = decision.get("id", "SIN-ID")
        for error in validar_decision(decision, identificadores):
            errores_totales.append(f"{identificador}: {error}")

    if errores_totales:
        print("VALIDACIÓN FALLIDA")
        for error in errores_totales:
            print(f"- {error}")
        return 1

    indicadores = calcular_indicadores(decisiones)
    print("VALIDACIÓN ESTRUCTURAL APROBADA")
    for nombre, valor in indicadores.items():
        print(f"- {nombre}: {valor}")
    print("ADVERTENCIA: la validación estructural no reemplaza la revisión semántica ni la aprobación humana.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
