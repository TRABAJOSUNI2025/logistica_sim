# 🚀 PRIMEROS PASOS - Sistema de Logística Ferreyros

## ¿Por dónde empezar?

### Opción 1: INICIO INTERACTIVO (Recomendado)

```bash
python INICIO.py
```

Esto abrirá un menú interactivo donde podrás:

- ▶️ Ejecutar simulación rápida (sin GUI)
- 📊 Abrir notebook Jupyter
- 🖥️ Lanzar interfaz gráfica
- 🔧 Validar instalación
- 📋 Ver configuración
- 📖 Acceder a documentación

---

## Opciones Rápidas Directas

### 1️⃣ Simulación Rápida (3 días en 5 segundos)

```bash
python quick_start.py
```

**Genera:**

- Reporte en consola
- Archivo `reporte_simulacion.txt`
- Archivo `datos_simulacion.csv`

---

### 2️⃣ Notebook Jupyter (Análisis Interactivo)

```bash
jupyter notebook simulador.ipynb
```

**Características:**

- 10 secciones con código ejecutable
- Gráficos y tablas interactivas
- Análisis de 3 días de simulación
- Editable para experimentar

---

### 3️⃣ Interfaz Gráfica (PyQt6)

```bash
python gui/main.py
```

**Acceso a:**

- 📦 Catálogos (SKUs, Clientes, Vehículos)
- 🚀 Simulación (ejecución interactiva)
- 📊 Indicadores (KPIs en vivo)
- 📋 Reportes (exportar TXT/CSV)

---

### 4️⃣ Validar Instalación

```bash
python instalar_y_probar.py
```

**Verifica:**

- Estructura de carpetas
- Archivos clave
- Dependencias instaladas
- Importaciones correctas
- Simulación básica funcional

---

## ⚙️ Instalación Completa

### Paso 1: Crear Entorno Virtual

```bash
# Windows (CMD o PowerShell)
python -m venv venv
venv\Scripts\activate
```

**Nota:** Verás `(venv)` al inicio de tu terminal cuando esté activo.

### Paso 2: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Validar

```bash
python instalar_y_probar.py
```

### Paso 4: Elegir método de uso

- **CLI:** `python quick_start.py`
- **Jupyter:** `jupyter notebook simulador.ipynb`
- **GUI:** `python gui/main.py`
- **Menú:** `python INICIO.py`

### Para desactivar el entorno (cuando termines)

```bash
deactivate
```

---

## 📁 Estructura del Proyecto

```
logistica_sim/
├── INICIO.py                 ← Punto de entrada principal
├── quick_start.py            ← Simulación rápida
├── instalar_y_probar.py      ← Validación
├── simulador.ipynb           ← Notebook Jupyter
├── config.py                 ← Configuración centralizada
├── requirements.txt          ← Dependencias
│
├── sistema/                  ← Backend (módulos de lógica)
│   ├── catalogos.py
│   ├── demanda.py
│   ├── inventario.py
│   ├── picking.py
│   ├── transporte.py
│   ├── indicadores.py
│   ├── alertas.py
│   ├── reporte.py
│   └── __init__.py
│
└── gui/                      ← Interfaz gráfica
    ├── main.py
    ├── recursos_manager.py
    ├── ventanas/
    │   ├── ventana_principal.py
    │   ├── ventana_catalogos.py
    │   ├── ventana_simulacion.py
    │   ├── ventana_indicadores.py
    │   ├── ventana_reporte.py
    │   └── __init__.py
    └── recursos/
        ├── estilos.qss       ← Estilos CSS
        ├── README.md         ← Guía de recursos
        ├── iconos/           ← Carpeta para PNGs
        └── logos/            ← Carpeta para logos
```

---

## 🎯 Casos de Uso

### Caso 1: Ejecutar simulación rápida

```bash
python quick_start.py
# Genera reporte en 5 segundos
```

### Caso 2: Análisis detallado

```bash
jupyter notebook simulador.ipynb
# Abre notebook con 10 secciones interactivas
```

### Caso 3: Usar como interfaz de usuario

```bash
python gui/main.py
# Interfaz gráfica profesional con Ferreyros colors
```

### Caso 4: Validar antes de usar

```bash
python instalar_y_probar.py
# Diagnostica y valida toda la instalación
```

---

## 🔧 Configuración Personalizable

Edita `config.py` para ajustar:

```python
CAPACIDAD_PICKING_DIARIA = 1500      # Unidades/día
PUNTO_REORDEN = 50                   # Stock mínimo
STOCK_INICIAL_POR_SKU = 200          # Unidades iniciales
TAMAÑO_BATCH_REPOSICION = 100        # Unidades por orden
VELOCIDAD_TRANSPORTE = 50            # km/hora
```

---

## 📊 Parámetros del Proyecto

### SKUs (8 productos Caterpillar)

- Repuestos para equipos mineros
- Códigos: REP001 a REP008

### Clientes (10 empresas)

- 5 Mineras (máxima prioridad)
- 3 Distribuidoras
- 2 Centros de acopio

### Vehículos (4 disponibles)

- Camioneta, Furgoneta, Camión, Tracto
- Capacidades: 500-3000 unidades

### Indicadores (6 KPIs)

- OTIF: On-Time-In-Full %
- Fill Rate: % de unidades entregadas
- Backlog: Órdenes pendientes
- Productivity: Unidades/hora picking
- Fleet Utilization: % capacidad usada
- Transport Index: Costo optimizado

---

## ✅ Checklist Rápido

- [ ] Python 3.10+ instalado
- [ ] `python -m venv venv` ejecutado
- [ ] `venv\Scripts\activate` ejecutado (verás `(venv)` en terminal)
- [ ] `pip install -r requirements.txt` ejecutado
- [ ] `python instalar_y_probar.py` validó exitosamente
- [ ] Elegí método preferido (CLI/Jupyter/GUI)
- [ ] ¡Sistema funcionando! 🎉

---

## 🆘 Solución de Problemas

### Error: "ModuleNotFoundError"

```bash
# Asegúrate que el entorno virtual está activado
venv\Scripts\activate
pip install -r requirements.txt
```

### No veo `(venv)` en la terminal

```bash
# Reactiva el entorno
venv\Scripts\activate
```

### GUI no abre

```bash
pip install PyQt6==6.6.1
python gui/main.py
```

### Jupyter no funciona

```bash
pip install jupyter
jupyter notebook simulador.ipynb
```

### Limpiar caché

```bash
python -m py_compile sistema/*.py gui/ventanas/*.py
```

---

## 📞 Soporte

- **Documentación completa:** Ver `README.md`
- **Inicio rápido:** Ver `INICIO_RAPIDO.md`
- **Resumen técnico:** Ver `RESUMEN_PROYECTO.md`
- **Recursos gráficos:** Ver `gui/recursos/README.md`

---

## 🎓 Estructura de Aprendizaje

1. **Principiante:** Ejecuta `python quick_start.py`
2. **Intermedio:** Abre `jupyter notebook simulador.ipynb`
3. **Avanzado:** Edita módulos en `sistema/`
4. **Experto:** Personaliza `config.py` y `gui/`

---

**¡Bienvenido al Sistema de Simulación Logística Ferreyros! 🚀**

Última actualización: 2024
Sistema completo y listo para producción ✅
