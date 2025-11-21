"""
picking.py - Operaciones de preparación de pedidos (picking)
"""


def prioridad_cliente(cliente_id):
    """
    Determina la prioridad del cliente.
    1. Clientes mineros (CL01-CL05): Mayor prioridad
    2. Distribuidores y otros: Menor prioridad
    
    Args:
        cliente_id: ID del cliente
    
    Returns:
        Tupla (prioridad_numerica, nombre_grupo)
    """
    if cliente_id in ["CL01", "CL02", "CL03", "CL04", "CL05"]:
        return (1, "Minero")
    elif cliente_id in ["CL06", "CL07", "CL08"]:
        return (2, "Distribuidor")
    else:
        return (3, "Otros")


def contar_unidades_pedidos(pedidos_dia):
    """Cuenta total de unidades en los pedidos"""
    total = 0
    for pedido_info in pedidos_dia.values():
        for linea in pedido_info["lineas"]:
            total += linea["cantidad"]
    return total


def asignar_picking(dia, pedidos_dia, capacidad_diaria=1500):
    """
    Asigna picking a pedidos según prioridad y capacidad.
    
    Args:
        dia: Número de día
        pedidos_dia: Diccionario de pedidos del día
        capacidad_diaria: Capacidad de picking en unidades
    
    Returns:
        Diccionario con: {
            "preparados": {...},
            "pendientes": {...},
            "unidades_preparadas": n,
            "unidades_pendientes": m,
            "capacidad_disponible": cap,
            "capacidad_usada": used
        }
    """
    
    # Ordenar pedidos por prioridad de cliente
    pedidos_ordenados = sorted(
        pedidos_dia.items(),
        key=lambda x: (prioridad_cliente(x[1]["cliente"])[0], x[0])
    )
    
    preparados = {}
    pendientes = {}
    unidades_preparadas = 0
    unidades_pendientes = 0
    
    for id_pedido, pedido_info in pedidos_ordenados:
        unidades_pedido = sum(linea["cantidad"] for linea in pedido_info["lineas"])
        
        if unidades_preparadas + unidades_pedido <= capacidad_diaria:
            # Cabe en la capacidad
            preparados[id_pedido] = pedido_info
            unidades_preparadas += unidades_pedido
        else:
            # Va al backlog
            pendientes[id_pedido] = pedido_info
            unidades_pendientes += unidades_pedido
    
    return {
        "dia": dia,
        "preparados": preparados,
        "pendientes": pendientes,
        "unidades_preparadas": unidades_preparadas,
        "unidades_pendientes": unidades_pendientes,
        "capacidad_disponible": capacidad_diaria,
        "capacidad_usada": unidades_preparadas,
        "num_pedidos_preparados": len(preparados),
        "num_pedidos_pendientes": len(pendientes)
    }


def calcular_productividad_picking(unidades_preparadas, horas_jornada=8):
    """
    Calcula productividad en unidades por hora.
    
    Args:
        unidades_preparadas: Total de unidades preparadas
        horas_jornada: Horas de trabajo en la jornada
    
    Returns:
        Productividad en unidades/hora
    """
    if horas_jornada == 0:
        return 0
    return unidades_preparadas / horas_jornada
