"""
reporte.py - Generación de reportes finales consolidados
"""

from datetime import datetime


def reporte_logistica(pedidos_totales, unidades_solicitadas, unidades_entregadas,
                     indicadores, alertas, recomendaciones=None):
    """
    Genera un reporte completo de la simulación logística.
    
    Args:
        pedidos_totales: Total de pedidos
        unidades_solicitadas: Total de unidades solicitadas
        unidades_entregadas: Total de unidades entregadas
        indicadores: Diccionario de indicadores
        alertas: Lista de alertas
        recomendaciones: Lista de recomendaciones (opcional)
    
    Returns:
        Diccionario con reporte formateado
    """
    
    unidades_no_entregadas = unidades_solicitadas - unidades_entregadas
    backlog_porcentaje = (unidades_no_entregadas / unidades_solicitadas * 100) if unidades_solicitadas > 0 else 0
    
    reporte = {
        "titulo": "REPORTE LOGÍSTICO - ANDES LOGISTICS S.A.",
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "resumen_operaciones": {
            "pedidos_recibidos": pedidos_totales,
            "unidades_solicitadas": unidades_solicitadas,
            "unidades_entregadas": unidades_entregadas,
            "unidades_no_entregadas": unidades_no_entregadas,
            "backlog_porcentaje": round(backlog_porcentaje, 2)
        },
        "indicadores_globales": indicadores,
        "alertas": alertas,
        "recomendaciones": recomendaciones if recomendaciones else []
    }
    
    return reporte


def formatear_reporte_texto(reporte):
    """
    Formatea el reporte como texto legible.
    
    Args:
        reporte: Diccionario del reporte
    
    Returns:
        String con reporte formateado
    """
    
    lineas = []
    lineas.append("=" * 70)
    lineas.append(f"  {reporte['titulo']}")
    lineas.append(f"  Fecha: {reporte['fecha']}")
    lineas.append("=" * 70)
    lineas.append("")
    
    # Resumen de operaciones
    lineas.append("RESUMEN DE OPERACIONES:")
    lineas.append("-" * 70)
    resumen = reporte["resumen_operaciones"]
    lineas.append(f"  Total pedidos recibidos: {resumen['pedidos_recibidos']}")
    lineas.append(f"  Total unidades solicitadas: {resumen['unidades_solicitadas']:,}")
    lineas.append(f"  Total unidades entregadas: {resumen['unidades_entregadas']:,}")
    lineas.append(f"  Total unidades no entregadas: {resumen['unidades_no_entregadas']:,}")
    lineas.append(f"  Backlog: {resumen['backlog_porcentaje']:.2f}%")
    lineas.append("")
    
    # Indicadores globales
    lineas.append("INDICADORES GLOBALES:")
    lineas.append("-" * 70)
    ind = reporte["indicadores_globales"]
    lineas.append(f"  OTIF: {ind.get('otif', ind.get('otif_promedio', 'N/A')):.2f}%")
    lineas.append(f"  Fill Rate: {ind.get('fill_rate', ind.get('fill_rate_promedio', 'N/A')):.2f}%")
    lineas.append(f"  Backlog Rate: {ind.get('backlog_rate', ind.get('backlog_rate_promedio', 'N/A')):.2f}%")
    lineas.append(f"  Productividad Picking: {ind.get('productividad_picking', ind.get('productividad_picking_promedio', 'N/A')):.2f} unid/h")
    lineas.append(f"  Utilización de Flota: {ind.get('utilizacion_flota', ind.get('utilizacion_flota_promedio', 'N/A')):.2f}%")
    lineas.append("")
    
    # Alertas
    if reporte["alertas"]:
        lineas.append("ALERTAS DETECTADAS:")
        lineas.append("-" * 70)
        for alerta in reporte["alertas"]:
            lineas.append(f"  [{alerta['severidad']}] {alerta['mensaje']}")
        lineas.append("")
    else:
        lineas.append("No hay alertas activas.")
        lineas.append("")
    
    # Recomendaciones
    if reporte["recomendaciones"]:
        lineas.append("RECOMENDACIONES:")
        lineas.append("-" * 70)
        for i, rec in enumerate(reporte["recomendaciones"], 1):
            lineas.append(f"  {i}. {rec}")
        lineas.append("")
    
    lineas.append("=" * 70)
    
    return "\n".join(lineas)


def exportar_reporte_csv(reporte):
    """
    Formatea el reporte para CSV.
    
    Args:
        reporte: Diccionario del reporte
    
    Returns:
        String con reporte en formato CSV
    """
    
    lineas = []
    lineas.append("Concepto,Valor")
    
    resumen = reporte["resumen_operaciones"]
    lineas.append(f"Pedidos recibidos,{resumen['pedidos_recibidos']}")
    lineas.append(f"Unidades solicitadas,{resumen['unidades_solicitadas']}")
    lineas.append(f"Unidades entregadas,{resumen['unidades_entregadas']}")
    lineas.append(f"Unidades no entregadas,{resumen['unidades_no_entregadas']}")
    lineas.append(f"Backlog (%),{resumen['backlog_porcentaje']}")
    lineas.append("")
    
    ind = reporte["indicadores_globales"]
    lineas.append(f"OTIF,{ind.get('otif', ind.get('otif_promedio', 'N/A'))}")
    lineas.append(f"Fill Rate,{ind.get('fill_rate', ind.get('fill_rate_promedio', 'N/A'))}")
    lineas.append(f"Backlog Rate,{ind.get('backlog_rate', ind.get('backlog_rate_promedio', 'N/A'))}")
    lineas.append(f"Productividad Picking,{ind.get('productividad_picking', ind.get('productividad_picking_promedio', 'N/A'))}")
    lineas.append(f"Utilización de Flota,{ind.get('utilizacion_flota', ind.get('utilizacion_flota_promedio', 'N/A'))}")
    
    return "\n".join(lineas)
