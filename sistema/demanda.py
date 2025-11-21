"""
demanda.py - Simulación de pedidos y demanda diaria
"""

import random
from datetime import datetime, timedelta


def simular_demanda(n_dias, dic_clientes, dic_sku, seed=None):
    """
    Simula la llegada de pedidos diarios por cliente.

    Args:
        n_dias: Número de días a simular
        dic_clientes: Diccionario de clientes
        dic_sku: Diccionario de SKUs
        seed: Semilla para reproducibilidad (opcional)

    Returns:
        Diccionario con estructura: {dia: {"PED{dia}-{i}": [{"sku": ..., "cantidad": ...}]}}
    """
    if seed is not None:
        random.seed(seed)

    pedidos_por_dia = {}
    lista_clientes = list(dic_clientes.keys())
    lista_skus = list(dic_sku.keys())

    for dia in range(1, n_dias + 1):
        pedidos_dia = {}
        num_pedidos = random.randint(10, 15)  # Entre 10 y 15 pedidos por día

        for i in range(1, num_pedidos + 1):
            id_pedido = f"PED{dia:02d}-{i:03d}"
            cliente = random.choice(lista_clientes)

            # 1-3 líneas por pedido
            num_lineas = random.randint(1, 3)
            lineas = []

            for _ in range(num_lineas):
                sku = random.choice(lista_skus)
                cantidad = random.randint(5, 50)
                lineas.append({"sku": sku, "cantidad": cantidad})

            pedidos_dia[id_pedido] = {
                "cliente": cliente,
                "lineas": lineas,
                "fecha_solicitud": datetime.now() + timedelta(days=dia - 1),
            }

        pedidos_por_dia[dia] = pedidos_dia

    return pedidos_por_dia


def contar_unidades_pedidos(pedidos_dia):
    """Cuenta el total de unidades en un día"""
    total = 0
    for pedido_info in pedidos_dia.values():
        for linea in pedido_info["lineas"]:
            total += linea["cantidad"]
    return total


def obtener_sku_mas_solicitado(pedidos_dia):
    """Encuentra el SKU más solicitado en un día"""
    conteo_sku = {}
    for pedido_info in pedidos_dia.values():
        for linea in pedido_info["lineas"]:
            sku = linea["sku"]
            conteo_sku[sku] = conteo_sku.get(sku, 0) + linea["cantidad"]

    if not conteo_sku:
        return None, 0

    sku_mas_solicitado = max(conteo_sku, key=conteo_sku.get)
    return sku_mas_solicitado, conteo_sku[sku_mas_solicitado]
