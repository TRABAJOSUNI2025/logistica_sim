"""
inventario.py - Control de inventario y reposición automática
"""


def inicializar_stock(dic_sku, stock_inicial=200):
    """
    Inicializa el stock para todos los SKUs.

    Args:
        dic_sku: Diccionario de SKUs
        stock_inicial: Cantidad inicial por SKU

    Returns:
        Diccionario {sku: cantidad}
    """
    return {sku: stock_inicial for sku in dic_sku.keys()}


def reservar_y_actualizar(stock, pedidos_dia, dic_clientes):
    """
    Procesa pedidos del día y actualiza el stock.
    Reduce inventario según líneas de pedidos.

    Args:
        stock: Diccionario actual de stock
        pedidos_dia: Pedidos del día
        dic_clientes: Catálogo de clientes

    Returns:
        Tupla (stock_actualizado, unidades_entregadas, unidades_no_entregadas, log_transacciones)
    """
    stock_actualizado = stock.copy()
    log_transacciones = []
    unidades_entregadas = 0
    unidades_no_entregadas = 0

    for id_pedido, pedido_info in pedidos_dia.items():
        cliente_id = pedido_info["cliente"]
        cliente_nombre = dic_clientes.get(cliente_id, "Desconocido")

        for linea in pedido_info["lineas"]:
            sku = linea["sku"]
            cantidad_solicitada = linea["cantidad"]

            # Verificar stock disponible
            stock_disponible = stock_actualizado.get(sku, 0)
            cantidad_entregada = min(stock_disponible, cantidad_solicitada)
            cantidad_no_entregada = cantidad_solicitada - cantidad_entregada

            # Actualizar stock
            stock_actualizado[sku] -= cantidad_entregada

            # Registrar transacción
            log_transacciones.append(
                {
                    "pedido": id_pedido,
                    "cliente": cliente_nombre,
                    "sku": sku,
                    "solicitado": cantidad_solicitada,
                    "entregado": cantidad_entregada,
                    "no_entregado": cantidad_no_entregada,
                }
            )

            unidades_entregadas += cantidad_entregada
            unidades_no_entregadas += cantidad_no_entregada

    return (
        stock_actualizado,
        unidades_entregadas,
        unidades_no_entregadas,
        log_transacciones,
    )


def reponer_simple(stock, dic_sku, punto_reorden=50, lote=100):
    """
    Reposición automática: si stock < punto_reorden, añade lote.

    Args:
        stock: Diccionario actual de stock
        dic_sku: Catálogo de SKUs
        punto_reorden: Umbral mínimo
        lote: Cantidad a reponer

    Returns:
        Tupla (stock_reaprovisionado, log_reaprovisionamiento)
    """
    stock_repuesto = stock.copy()
    log_reaprovisionamiento = []

    for sku in dic_sku.keys():
        stock_actual = stock_repuesto.get(sku, 0)

        if stock_actual < punto_reorden:
            stock_repuesto[sku] += lote
            log_reaprovisionamiento.append(
                {
                    "sku": sku,
                    "stock_anterior": stock_actual,
                    "stock_posterior": stock_repuesto[sku],
                    "cantidad_añadida": lote,
                }
            )

    return stock_repuesto, log_reaprovisionamiento


def obtener_estado_stock(stock, dic_sku):
    """Genera un informe del estado del stock"""
    informe = {}
    for sku, cantidad in stock.items():
        informe[sku] = {
            "cantidad": cantidad,
            "descripcion": dic_sku.get(sku, "Desconocido"),
        }
    return informe
