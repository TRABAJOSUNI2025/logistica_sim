"""
transporte.py - Planificación de rutas y asignación de vehículos
"""


def agrupar_pedidos_por_cliente(pedidos_preparados):
    """
    Agrupa pedidos preparados por cliente.

    Args:
        pedidos_preparados: Diccionario de pedidos preparados

    Returns:
        Diccionario {cliente_id: {pedido_id: pedido_info}}
    """
    agrupados = {}
    for id_pedido, pedido_info in pedidos_preparados.items():
        cliente_id = pedido_info["cliente"]
        if cliente_id not in agrupados:
            agrupados[cliente_id] = {}
        agrupados[cliente_id][id_pedido] = pedido_info
    return agrupados


def contar_unidades_grupo(grupo_pedidos):
    """Cuenta unidades en un grupo de pedidos"""
    total = 0
    for pedido_info in grupo_pedidos.values():
        for linea in pedido_info["lineas"]:
            total += linea["cantidad"]
    return total


def asignar_vehiculos_greedy(
    grupos_por_cliente, vehiculos, distancias_km, dic_clientes
):
    """
    Asigna vehículos a grupos de clientes usando algoritmo greedy.

    Args:
        grupos_por_cliente: Grupos de pedidos por cliente
        vehiculos: Catálogo de vehículos
        distancias_km: Distancias por zona
        dic_clientes: Catálogo de clientes

    Returns:
        Tupla (rutas_asignadas, no_asignadas, costo_total)
    """
    rutas_asignadas = []
    no_asignadas = {}
    costo_total = 0.0

    # Ordenar vehículos por capacidad descendente
    vehiculos_disponibles = sorted(
        vehiculos.items(), key=lambda x: x[1]["capacidad"], reverse=True
    )

    # Crear lista de vehículos reutilizables (pueden hacer múltiples rutas)
    for cliente_id, grupo_pedidos in grupos_por_cliente.items():
        unidades = contar_unidades_grupo(grupo_pedidos)
        cliente_nombre = dic_clientes.get(cliente_id, "Desconocido")
        distancia = distancias_km.get(cliente_nombre, 100)

        # Buscar vehículo con capacidad suficiente
        asignado = False
        for vehiculo_id, vehiculo_info in vehiculos_disponibles:
            if vehiculo_info["capacidad"] >= unidades:
                utilizacion = (unidades / vehiculo_info["capacidad"]) * 100
                costo_ruta = distancia * vehiculo_info["costo_km"]

                rutas_asignadas.append(
                    {
                        "vehiculo": vehiculo_id,
                        "cliente": cliente_nombre,
                        "unidades": unidades,
                        "capacidad": vehiculo_info["capacidad"],
                        "utilizacion": utilizacion,
                        "distancia_km": distancia,
                        "costo_km": vehiculo_info["costo_km"],
                        "costo_total": costo_ruta,
                        "pedidos": list(grupo_pedidos.keys()),
                    }
                )

                costo_total += costo_ruta
                asignado = True
                break

        if not asignado:
            no_asignadas[cliente_id] = grupo_pedidos

    return rutas_asignadas, no_asignadas, costo_total


def planificar_rutas(dia, pedidos_preparados, vehiculos, distancias_km, dic_clientes):
    """
    Planifica rutas de transporte para pedidos preparados.

    Args:
        dia: Número de día
        pedidos_preparados: Pedidos listos para transportar
        vehiculos: Catálogo de vehículos
        distancias_km: Distancias por zona
        dic_clientes: Catálogo de clientes

    Returns:
        Diccionario con información de rutas, utilización y costos
    """

    if not pedidos_preparados:
        return {
            "dia": dia,
            "rutas": [],
            "no_transportados": {},
            "unidades_transportadas": 0,
            "unidades_no_transportadas": 0,
            "num_rutas": 0,
            "utilizacion_promedio": 0.0,
            "costo_total": 0.0,
        }

    # Agrupar por cliente
    grupos = agrupar_pedidos_por_cliente(pedidos_preparados)

    # Asignar vehículos
    rutas, no_transportados, costo_total = asignar_vehiculos_greedy(
        grupos, vehiculos, distancias_km, dic_clientes
    )

    # Calcular estadísticas
    unidades_transportadas = sum(ruta["unidades"] for ruta in rutas)
    unidades_no_transportadas = sum(
        contar_unidades_grupo(grupo) for grupo in no_transportados.values()
    )

    utilizacion_promedio = 0.0
    if rutas:
        utilizacion_promedio = sum(ruta["utilizacion"] for ruta in rutas) / len(rutas)

    return {
        "dia": dia,
        "rutas": rutas,
        "no_transportados": no_transportados,
        "unidades_transportadas": unidades_transportadas,
        "unidades_no_transportadas": unidades_no_transportadas,
        "num_rutas": len(rutas),
        "utilizacion_promedio": utilizacion_promedio,
        "costo_total": costo_total,
    }
