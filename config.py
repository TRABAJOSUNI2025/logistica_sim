"""
config.py - Archivo de configuración centralizado del sistema

Aquí se definen todos los parámetros del sistema que pueden ser ajustados
sin modificar el código fuente.
"""

# ============================================================================
# CONFIGURACIÓN DE SIMULACIÓN
# ============================================================================

# Seed para reproducibilidad
SEED_SIMULACION = 42

# Número de días por defecto
DIAS_DEFAULT = 3

# ============================================================================
# CAPACIDADES Y LÍMITES
# ============================================================================

# Capacidad diaria de picking en unidades
CAPACIDAD_PICKING_DIARIA = 1500

# Horas de jornada laboral
HORAS_JORNADA = 8

# ============================================================================
# GESTIÓN DE INVENTARIO
# ============================================================================

# Stock inicial por SKU
STOCK_INICIAL = 200

# Punto de reorden para reposición
PUNTO_REORDEN = 50

# Cantidad a reponer cuando se alcanza punto de reorden
LOTE_REPOSICION = 100

# ============================================================================
# INDICADORES Y UMBRALES DE ALERTAS
# ============================================================================

# Umbrales de alertas
UMBRALES_ALERTAS = {
    "otif_minimo": 95.0,  # % mínimo de OTIF
    "fill_rate_minimo": 96.0,  # % mínimo de Fill Rate
    "backlog_maximo": 5.0,  # % máximo de Backlog
    "utilizacion_flota_maxima": 85.0,  # % máximo de utilización de flota
    "productividad_minima": 150.0,  # Mínimo unidades/hora
}

# Lead time estándar en horas (para OTIF)
LEAD_TIME_STANDAR_HORAS = 48

# ============================================================================
# PRIORIZACIÓN DE CLIENTES
# ============================================================================

# Grupos de clientes y su prioridad (menor número = mayor prioridad)
GRUPOS_CLIENTES = {
    "mineros": {
        "ids": ["CL01", "CL02", "CL03", "CL04", "CL05"],
        "prioridad": 1,
        "descripcion": "Clientes mineros (máxima criticidad)",
    },
    "distribuidores": {
        "ids": ["CL06", "CL07", "CL08"],
        "prioridad": 2,
        "descripcion": "Distribuidores regionales",
    },
    "otros": {
        "ids": ["CL09", "CL10"],
        "prioridad": 3,
        "descripcion": "Centros de mantenimiento y otros",
    },
}

# ============================================================================
# CONFIGURACIÓN DE INTERFAZ GRÁFICA
# ============================================================================

# Tema de la aplicación
TEMA_APLICACION = "Fusion"

# Colores corporativos Ferreyros
COLORES = {
    "primario": "#FFD700",  # Amarillo Ferreyros
    "secundario": "#FFA500",  # Naranja
    "fondo": "white",
    "texto": "black",
    "exito": "#D4EDDA",
    "advertencia": "#FFF3CD",
    "error": "#F8D7DA",
    "info": "#D1ECF1",
}

# ============================================================================
# CONFIGURACIÓN DE ARCHIVOS Y PERSISTENCIA
# ============================================================================

# Directorio para datos generados
DIRECTORIO_DATOS = "data"

# Archivos de salida
ARCHIVO_REPORTE_TXT = "reporte_final.txt"
ARCHIVO_REPORTE_CSV = "reporte_final.csv"
ARCHIVO_SIMULACION_JSON = "simulacion.json"

# ============================================================================
# PARÁMETROS DE TRANSPORTE
# ============================================================================

# Algoritmo de asignación de vehículos
ALGORITMO_TRANSPORTE = "greedy"  # "greedy", "optimal", "first-fit"

# Distancias mínimas y máximas (km) para validación
DISTANCIA_MINIMA = 10
DISTANCIA_MAXIMA = 1100

# ============================================================================
# CONFIGURACIÓN DE PICKING
# ============================================================================

# Cantidad mínima de líneas por pedido
LINEAS_PEDIDO_MINIMO = 1

# Cantidad máxima de líneas por pedido
LINEAS_PEDIDO_MAXIMO = 3

# Cantidad mínima de unidades por línea
UNIDADES_MINIMO = 5

# Cantidad máxima de unidades por línea
UNIDADES_MAXIMO = 50

# Rango de pedidos diarios
PEDIDOS_DIARIOS_MINIMO = 10
PEDIDOS_DIARIOS_MAXIMO = 15

# ============================================================================
# CONFIGURACIÓN DE LOGGING
# ============================================================================

# Nivel de verbosidad
NIVEL_VERBOSIDAD = 2  # 0=silencioso, 1=crítico, 2=informativo, 3=detallado

# Mostrar resultados intermedios
MOSTRAR_INTERMEDIOS = True

# ============================================================================
# VALIDACIONES
# ============================================================================


def validar_configuracion():
    """Valida la configuración del sistema"""
    errores = []

    if CAPACIDAD_PICKING_DIARIA <= 0:
        errores.append("CAPACIDAD_PICKING_DIARIA debe ser positivo")

    if HORAS_JORNADA <= 0 or HORAS_JORNADA > 24:
        errores.append("HORAS_JORNADA debe estar entre 1 y 24")

    if STOCK_INICIAL < LOTE_REPOSICION:
        errores.append("STOCK_INICIAL debe ser >= LOTE_REPOSICION")

    if PUNTO_REORDEN >= STOCK_INICIAL:
        errores.append("PUNTO_REORDEN debe ser < STOCK_INICIAL")

    for clave, valor in UMBRALES_ALERTAS.items():
        if valor < 0 or valor > 100:
            if "minimo" in clave or "maximo" in clave:
                if valor < 0 or valor > 100:
                    errores.append(f"Umbral {clave} debe estar entre 0 y 100")

    if LEAD_TIME_STANDAR_HORAS <= 0:
        errores.append("LEAD_TIME_STANDAR_HORAS debe ser positivo")

    return errores


def obtener_resumen_configuracion():
    """Devuelve un diccionario con el resumen de configuración"""
    return {
        "seed": SEED_SIMULACION,
        "capacidad_picking": CAPACIDAD_PICKING_DIARIA,
        "horas_jornada": HORAS_JORNADA,
        "stock_inicial": STOCK_INICIAL,
        "punto_reorden": PUNTO_REORDEN,
        "umbrales_alertas": UMBRALES_ALERTAS,
        "directorio_datos": DIRECTORIO_DATOS,
    }


# Validar al importar el módulo
errores = validar_configuracion()
if errores:
    print("⚠️  Errores en la configuración:")
    for error in errores:
        print(f"  - {error}")
