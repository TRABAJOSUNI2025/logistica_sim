"""
alertas.py - Generación de alertas automáticas según umbrales
"""


def generar_alertas(indicadores, umbrales=None):
    """
    Genera alertas si los indicadores superan los umbrales definidos.
    
    Args:
        indicadores: Diccionario de indicadores
        umbrales: Diccionario con umbrales (opcional, usa defaults si no se proporciona)
    
    Returns:
        Lista de alertas con severidad
    """
    
    # Umbrales por defecto
    if umbrales is None:
        umbrales = {
            "otif_minimo": 95.0,
            "fill_rate_minimo": 96.0,
            "backlog_maximo": 5.0,
            "utilizacion_flota_maxima": 85.0,
            "productividad_minima": 150.0
        }
    
    alertas = []
    
    # Alerta OTIF
    if indicadores.get("otif", 100) < umbrales["otif_minimo"]:
        alertas.append({
            "tipo": "OTIF_BAJO",
            "mensaje": f"OTIF bajo ({indicadores['otif']:.1f}% < {umbrales['otif_minimo']:.1f}%)",
            "severidad": "ALTO",
            "recomendacion": "Verificar tiempos de preparación y transporte"
        })
    
    # Alerta Fill Rate
    if indicadores.get("fill_rate", 100) < umbrales["fill_rate_minimo"]:
        alertas.append({
            "tipo": "FILL_RATE_BAJO",
            "mensaje": f"Fill Rate bajo ({indicadores['fill_rate']:.1f}% < {umbrales['fill_rate_minimo']:.1f}%)",
            "severidad": "ALTO",
            "recomendacion": "Revisar disponibilidad de inventario"
        })
    
    # Alerta Backlog
    if indicadores.get("backlog_rate", 0) > umbrales["backlog_maximo"]:
        alertas.append({
            "tipo": "BACKLOG_ALTO",
            "mensaje": f"Backlog alto ({indicadores['backlog_rate']:.1f}% > {umbrales['backlog_maximo']:.1f}%)",
            "severidad": "MEDIO",
            "recomendacion": "Aumentar capacidad de picking o reasignar recursos"
        })
    
    # Alerta Utilización de flota
    if indicadores.get("utilizacion_flota", 0) > umbrales["utilizacion_flota_maxima"]:
        alertas.append({
            "tipo": "FLOTA_SATURADA",
            "mensaje": f"Utilización de flota alta ({indicadores['utilizacion_flota']:.1f}% > {umbrales['utilizacion_flota_maxima']:.1f}%)",
            "severidad": "MEDIO",
            "recomendacion": "Riesgo de saturación - considerar flota adicional"
        })
    
    # Alerta Productividad
    if indicadores.get("productividad_picking", 0) < umbrales["productividad_minima"]:
        alertas.append({
            "tipo": "PRODUCTIVIDAD_BAJA",
            "mensaje": f"Productividad baja ({indicadores['productividad_picking']:.1f} unid/h < {umbrales['productividad_minima']:.1f})",
            "severidad": "BAJO",
            "recomendacion": "Revisar procesos de picking y capacitación del personal"
        })
    
    return alertas


def generar_recomendaciones(alertas, indicadores):
    """
    Genera recomendaciones específicas basadas en alertas y indicadores.
    
    Args:
        alertas: Lista de alertas
        indicadores: Diccionario de indicadores
    
    Returns:
        Lista de recomendaciones ordenadas por prioridad
    """
    
    recomendaciones = []
    
    # Recolectar recomendaciones únicas
    recomendaciones_set = set()
    for alerta in alertas:
        recomendaciones_set.add(alerta["recomendacion"])
    
    # Recomendaciones adicionales basadas en análisis
    if indicadores.get("backlog_rate", 0) > 3.0:
        recomendaciones_set.add("Reasignar pedidos entre zonas para equilibrar carga")
    
    if indicadores.get("utilizacion_flota", 0) > 80.0:
        recomendaciones_set.add("Optimizar rutas de transporte para mejorar eficiencia")
    
    if indicadores.get("productividad_picking", 0) < 180.0:
        recomendaciones_set.add("Incrementar personal de picking en horas pico")
    
    if indicadores.get("fill_rate", 100) < 98.0:
        recomendaciones_set.add("Mejorar pronóstico de demanda y reaprovisionamiento")
    
    # Convertir a lista ordenada
    recomendaciones = sorted(list(recomendaciones_set))
    
    return recomendaciones
