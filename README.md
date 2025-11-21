# 🚚 Sistema de Simulación Logística - Andes Logistics S.A.

## 📋 Descripción

Sistema modular en Python con interfaz gráfica en **PyQt6** que simula, consolida y analiza el desempeño logístico en operaciones de distribución de repuestos Caterpillar para Ferreyros.

El sistema modela:

- Recepción y gestión de stock
- Preparación de pedidos (picking)
- Planificación de rutas y transporte
- Cálculo de indicadores logísticos (KPIs)
- Generación automática de alertas
- Reportes consolidados con recomendaciones

---

## 📁 Estructura del Proyecto

```
logistica_sim/
├── simulador.ipynb                 # Cuaderno Jupyter con pruebas completas
├── requirements.txt                # Dependencias Python
├── README.md                       # Este archivo
│
├── sistema/                        # Módulos principales del sistema
│   ├── __init__.py
│   ├── catalogos.py               # Catálogos de SKUs, clientes y vehículos
│   ├── demanda.py                 # Simulación de demanda diaria
│   ├── inventario.py              # Gestión de stock y reposición
│   ├── picking.py                 # Operaciones de picking
│   ├── transporte.py              # Planificación de rutas
│   ├── indicadores.py             # Cálculo de KPIs
│   ├── alertas.py                 # Generación de alertas
│   └── reporte.py                 # Generación de reportes
│
├── gui/                            # Interfaz gráfica PyQt6
│   ├── main.py                    # Punto de entrada de la aplicación
│   ├── __init__.py
│   ├── ventanas/
│   │   ├── __init__.py
│   │   ├── ventana_principal.py   # Menú principal
│   │   ├── ventana_catalogos.py   # Gestión de catálogos
│   │   ├── ventana_simulacion.py  # Simulación de demanda
│   │   ├── ventana_indicadores.py # Indicadores y alertas
│   │   └── ventana_reporte.py     # Reporte final
│   └── recursos/                  # Estilos y recursos
│
└── data/                           # Datos de simulación generados
    ├── simulacion.json            # Datos en JSON
    ├── reporte_final.txt          # Reporte en texto
    └── reporte_final.csv          # Reporte en CSV
```

---

## 🚀 Instalación y Configuración

### 1. Requisitos Previos

- Python 3.10 o superior
- pip (gestor de paquetes)

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el Sistema

#### Opción A: Notebook Jupyter (Recomendado para análisis)

```bash
jupyter notebook simulador.ipynb
```

#### Opción B: Interfaz Gráfica PyQt6

```bash
python gui/main.py
```

---

## 📊 Funcionalidades Principales

### 1. **Simulación de Demanda**

- Genera 10-15 pedidos diarios
- Asigna clientes y SKUs aleatoriamente
- Cantidades de 5 a 50 unidades por línea
- Reproducible mediante seed

### 2. **Gestión de Inventario**

- Stock inicial: 200 unidades por SKU
- Reposición automática cuando stock < 50 unidades
- Lote de reposición: 100 unidades
- Registro de transacciones

### 3. **Operaciones de Picking**

- Capacidad diaria: 1,500 unidades
- Priorización por tipo de cliente:
  - Clientes mineros (CL01-CL05)
  - Distribuidores regionales (CL06-CL08)
  - Otros clientes
- Detección automática de backlog

### 4. **Planificación de Rutas**

- Agrupación de pedidos por cliente/zona
- Asignación de vehículos por capacidad
- Cálculo de costos y utilización de flota
- Selección greedy de vehículos

### 5. **Indicadores Logísticos (KPIs)**

- **OTIF**: % de pedidos entregados completos y a tiempo
- **Fill Rate**: % de unidades entregadas vs solicitadas
- **Backlog Rate**: % de unidades pendientes
- **Productividad Picking**: unidades/hora
- **Utilización de Flota**: % promedio

### 6. **Alertas Automáticas**

Se disparan automáticamente cuando:

- OTIF < 95%
- Fill Rate < 96%
- Backlog > 5%
- Utilización de flota > 85%

Incluyen nivel de severidad y recomendaciones.

### 7. **Reportes**

- Resumen ejecutivo
- Indicadores globales consolidados
- Alertas detectadas
- Recomendaciones automáticas
- Exportación a TXT y CSV

---

## 🎯 Ejemplo de Uso

### Mediante el Notebook Jupyter:

```python
from sistema.demanda import simular_demanda
from sistema.catalogos import dic_sku, dic_clientes

# Simular 3 días
pedidos = simular_demanda(3, dic_clientes, dic_sku, seed=42)

# Procesar demanda, picking, transporte
# Calcular indicadores
# Generar alertas y reporte
```

### Mediante la GUI:

1. Ejecutar `python gui/main.py`
2. Seleccionar "Simular Demanda" desde el menú
3. Configurar parámetros (días, seed)
4. Visualizar resultados en tablas
5. Exportar reporte final

---

## 📈 Catálogos del Sistema

### SKUs (Repuestos Caterpillar)

- CAT140-0101: Filtro de aceite para Motor C15
- CAT140-0235: Filtro hidráulico para 966K
- CAT330-4410: Bomba hidráulica 320D
- CAT777-8821: Kit de frenos para Camión Minero 777F
- CAT950-3320: Manguera hidráulica 950M
- CAT312-7722: Sensor de presión 312D
- CAT992-1205: Turboalimentador Motor 3516
- CAT601-5520: Kit de sellos cilindro principal

### Clientes

- Clientes mineros: Antamina, Toquepala, Yanacocha, Las Bambas, Antapaccay
- Distribuidores: Piura, Arequipa, Trujillo
- Centros de mantenimiento: Lima, Arequipa

### Vehículos

- VH01: Camión rígido 10T (180 unid, S/. 6.50/km)
- VH02: Camión 12T (220 unid, S/. 7.20/km)
- VH03: Camioneta 4x4 minera (140 unid, S/. 5.80/km)
- VH04: Tráiler liviano (260 unid, S/. 8.10/km)

---

## 🔧 Configuración de Parámetros

Editar en el notebook o en los módulos:

```python
SEED_SIMULACION = 42                  # Para reproducibilidad
CAPACIDAD_PICKING_DIARIA = 1500       # unidades
HORAS_JORNADA = 8
PUNTO_REORDEN = 50
LOTE_REPOSICION = 100
STOCK_INICIAL = 200
```

---

## 📝 Convenciones del Sistema

### Identificadores

- **Pedido**: `PED{dia:02d}-{i:03d}` (ej: PED01-003)
- **SKU**: `CAT{número}` (ej: CAT140-0101)
- **Cliente**: `CL01`, `CL02`, etc.
- **Vehículo**: `VH01`, `VH02`, etc.

### Tiempos

- Lead time estándar: 48 horas
- Jornada de picking: 8 horas

---

## 📊 Archivos de Salida Generados

El sistema genera automáticamente:

1. **data/simulacion.json**: Datos estructurados de la simulación
2. **data/reporte_final.txt**: Reporte en formato texto
3. **data/reporte_final.csv**: Reporte en formato CSV (para Excel)

---

## 🧪 Pruebas

El archivo `simulador.ipynb` incluye:

- Simulación de 3 días completa
- Verificación manual de KPIs
- Ejecución de picking y transporte
- Generación de reporte final
- Ejemplos de cálculos

---

## 🔐 Dependencias

| Paquete    | Versión | Propósito           |
| ---------- | ------- | ------------------- |
| PyQt6      | 6.6.1   | Interfaz gráfica    |
| pandas     | 2.0.3   | Análisis de datos   |
| numpy      | 1.24.3  | Cálculos numéricos  |
| matplotlib | 3.7.2   | Gráficos (opcional) |

---

## 👥 Autor

**Sistema de Simulación Logística**  
Desarrollado para: Andes Logistics S.A. - Ferreyros  
Ciclo: SEPTIMO - Sistemas Integrados Empresariales  
Año: 2025

---

## 📌 Notas Importantes

1. **Reproducibilidad**: Usar el mismo `seed` para obtener siempre los mismos resultados
2. **Capacidad Picking**: El límite diario es 1,500 unidades
3. **Priorización**: Los pedidos de clientes mineros siempre se procesan primero
4. **Alertas**: Se generan automáticamente según umbrales configurables
5. **Exportación**: Los reportes se guardan en la carpeta `data/`

---

## 📞 Soporte

Para preguntas o problemas con el sistema, revisar:

- Documentación en docstrings de cada módulo
- Ejemplos en `simulador.ipynb`
- Estructura de catálogos en `sistema/catalogos.py`

---

**Última actualización**: Noviembre 2025
