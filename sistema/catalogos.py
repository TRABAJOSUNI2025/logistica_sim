"""
catalogos.py - Catálogos centrales del sistema logístico
Mantiene SKUs, clientes y vehículos adaptados a Ferreyros
"""

# Catálogo de SKUs (repuestos Caterpillar)
dic_sku = {
    "CAT140-0101": "Filtro de aceite para Motor C15",
    "CAT140-0235": "Filtro hidráulico para 966K",
    "CAT330-4410": "Bomba hidráulica 320D",
    "CAT777-8821": "Kit de frenos para Camión Minero 777F",
    "CAT950-3320": "Manguera hidráulica 950M",
    "CAT312-7722": "Sensor de presión 312D",
    "CAT992-1205": "Turboalimentador Motor 3516",
    "CAT601-5520": "Kit de sellos cilindro principal",
}

# Catálogo de clientes
dic_clientes = {
    "CL01": "Minera Antamina",
    "CL02": "Minera Toquepala",
    "CL03": "Minera Yanacocha",
    "CL04": "Minera Las Bambas",
    "CL05": "Minera Antapaccay",
    "CL06": "Distribuidor Piura",
    "CL07": "Distribuidor Arequipa",
    "CL08": "Distribuidor Trujillo",
    "CL09": "Centro de Mantenimiento Lima",
    "CL10": "Centro de Mantenimiento Arequipa",
}

# Catálogo de vehículos
dic_vehiculos = {
    "VH01": {"capacidad": 180, "costo_km": 6.5, "tipo": "Camión rígido 10T"},
    "VH02": {"capacidad": 220, "costo_km": 7.2, "tipo": "Camión 12T"},
    "VH03": {"capacidad": 140, "costo_km": 5.8, "tipo": "Camioneta 4x4 minera"},
    "VH04": {"capacidad": 260, "costo_km": 8.1, "tipo": "Tráiler liviano"},
}

# Distancias estimadas por zona (para costos)
distancias_km = {
    "Minera Antamina": 450,
    "Minera Toquepala": 980,
    "Minera Yanacocha": 620,
    "Minera Las Bambas": 780,
    "Minera Antapaccay": 890,
    "Distribuidor Piura": 940,
    "Distribuidor Arequipa": 1010,
    "Distribuidor Trujillo": 560,
    "Centro de Mantenimiento Lima": 15,
    "Centro de Mantenimiento Arequipa": 1010,
}


def get_cliente_nombre(cliente_id):
    """Obtiene el nombre del cliente por ID"""
    return dic_clientes.get(cliente_id, "Desconocido")


def get_sku_descripcion(sku_id):
    """Obtiene la descripción del SKU por ID"""
    return dic_sku.get(sku_id, "Desconocido")


def get_vehiculo_info(vehiculo_id):
    """Obtiene la información del vehículo"""
    return dic_vehiculos.get(vehiculo_id, {})
