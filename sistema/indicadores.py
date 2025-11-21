"""
indicadores.py - Cálculo de indicadores logísticos (KPIs)
"""


def calcular_indicadores(
    pedidos_totales,
    unidades_entregadas,
    unidades_solicitadas,
    unidades_preparadas,
    unidades_transportadas,
    unidades_no_transportadas,
    utilizacion_flota,
    horas_jornada=8,
):
    """
    Calcula los KPIs principales del sistema logístico.

    Args:
        pedidos_totales: Total de pedidos recibidos
        unidades_entregadas: Unidades realmente entregadas
        unidades_solicitadas: Total de unidades solicitadas
        unidades_preparadas: Unidades preparadas en picking
        unidades_transportadas: Unidades efectivamente transportadas
        unidades_no_transportadas: Unidades sin transporte asignado
        utilizacion_flota: Porcentaje de utilización promedio
        horas_jornada: Horas de jornada laboral

    Returns:
        Diccionario con todos los indicadores
    """

    # OTIF: On-Time In-Full (asumiendo lead time estándar 48h)
    # Por ahora: pedidos completamente entregados / total
    otif = 0.0
    if pedidos_totales > 0:
        # Aproximación: si se entregaron todas las unidades solicitadas
        otif = (
            (unidades_entregadas / unidades_solicitadas * 100)
            if unidades_solicitadas > 0
            else 0.0
        )
        otif = min(otif, 100.0)

    # Fill Rate: unidades entregadas / solicitadas
    fill_rate = 0.0
    if unidades_solicitadas > 0:
        fill_rate = (unidades_entregadas / unidades_solicitadas) * 100

    # Backlog Rate: unidades no entregadas / solicitadas
    unidades_no_entregadas = unidades_solicitadas - unidades_entregadas
    backlog_rate = 0.0
    if unidades_solicitadas > 0:
        backlog_rate = (unidades_no_entregadas / unidades_solicitadas) * 100

    # Productividad Picking: unidades / hora
    productividad_picking = 0.0
    if horas_jornada > 0:
        productividad_picking = unidades_preparadas / horas_jornada

    # Índice de transporte (unidades transportadas / preparadas)
    indice_transporte = 0.0
    if unidades_preparadas > 0:
        indice_transporte = (unidades_transportadas / unidades_preparadas) * 100

    return {
        "otif": round(otif, 2),
        "fill_rate": round(fill_rate, 2),
        "backlog_rate": round(backlog_rate, 2),
        "productividad_picking": round(productividad_picking, 2),
        "utilizacion_flota": round(utilizacion_flota, 2),
        "indice_transporte": round(indice_transporte, 2),
        "unidades_entregadas": unidades_entregadas,
        "unidades_no_entregadas": unidades_no_entregadas,
        "pedidos_totales": pedidos_totales,
    }


def consolidar_indicadores_multiples_dias(lista_indicadores_diarios):
    """
    Consolida indicadores de múltiples días en promedios globales.

    Args:
        lista_indicadores_diarios: Lista de diccionarios de indicadores diarios

    Returns:
        Diccionario con indicadores consolidados
    """

    if not lista_indicadores_diarios:
        return {}

    n_dias = len(lista_indicadores_diarios)

    # Sumar valores
    suma_otif = sum(ind["otif"] for ind in lista_indicadores_diarios)
    suma_fill_rate = sum(ind["fill_rate"] for ind in lista_indicadores_diarios)
    suma_backlog = sum(ind["backlog_rate"] for ind in lista_indicadores_diarios)
    suma_prod = sum(ind["productividad_picking"] for ind in lista_indicadores_diarios)
    suma_util_flota = sum(ind["utilizacion_flota"] for ind in lista_indicadores_diarios)

    total_entregadas = sum(
        ind["unidades_entregadas"] for ind in lista_indicadores_diarios
    )
    total_no_entregadas = sum(
        ind["unidades_no_entregadas"] for ind in lista_indicadores_diarios
    )
    total_pedidos = sum(ind["pedidos_totales"] for ind in lista_indicadores_diarios)

    return {
        "otif_promedio": round(suma_otif / n_dias, 2),
        "fill_rate_promedio": round(suma_fill_rate / n_dias, 2),
        "backlog_rate_promedio": round(suma_backlog / n_dias, 2),
        "productividad_picking_promedio": round(suma_prod / n_dias, 2),
        "utilizacion_flota_promedio": round(suma_util_flota / n_dias, 2),
        "unidades_entregadas_total": total_entregadas,
        "unidades_no_entregadas_total": total_no_entregadas,
        "pedidos_totales": total_pedidos,
        "dias_simulados": n_dias,
    }
