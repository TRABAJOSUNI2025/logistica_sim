# 🚀 COMIENZA AQUI

## Bienvenido al Sistema de Logística Ferreyros

Sistema profesional de simulación logística con GUI, análisis y reportes automáticos.

---

## ⚡ INICIO RÁPIDO (2 minutos)

### Paso 1: Crear Entorno Virtual

```bash
# Windows (CMD o PowerShell)
python -m venv venv
venv\Scripts\activate
```

### Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar (elige uno)

```bash
python INICIO.py              # Menú interactivo (RECOMENDADO)
# O
python quick_start.py         # Simulación directa (5 segundos)
# O
python gui/main.py            # Interfaz gráfica
```

---

## 📚 DOCUMENTACIÓN

| Documento                  | Para     | Contenido                                                     |
| -------------------------- | -------- | ------------------------------------------------------------- |
| **PRIMEROS_PASOS.md**      | Todos    | 5 opciones de ejecución, instalación, configuración           |
| **README.md**              | Técnicos | Documentación completa del código y API                       |
| **EQUIPO_TRABAJO.md**      | Equipo   | División de trabajo, roles, responsabilidades (5 integrantes) |
| **gui/recursos/README.md** | Diseño   | Cómo agregar iconos y logos                                   |

---

## 🎯 OPCIONES DE USO

### 1. Menú Interactivo (Mejor para empezar)

```bash
python INICIO.py
```

→ Elige opción en el menú

### 2. Simulación Rápida (5 segundos)

```bash
python quick_start.py
```

→ Genera archivos automáticamente

### 3. Interfaz Gráfica

```bash
python gui/main.py
```

→ Navega 5 ventanas profesionales

### 4. Análisis Interactivo

```bash
jupyter notebook simulador.ipynb
```

→ 10 secciones ejecutables

### 5. Validar Sistema

```bash
python verificador_integridad.py
```

→ Diagnóstico completo

---

## 🛠️ CONFIGURACIÓN

Personaliza en `config.py`:

- Capacidad picking
- Punto de reorden
- Stock inicial
- Parámetros transporte

---

## ✅ CHECKLIST

- [ ] Python 3.10+ instalado
- [ ] `python -m venv venv` → crear entorno
- [ ] `venv\Scripts\activate` → activar entorno
- [ ] `pip install -r requirements.txt` → instalar
- [ ] `python INICIO.py` → ejecutar
- [ ] ¡Listo!

---

## 📊 RÁPIDO RESUMEN

- **8 SKUs** Caterpillar
- **10 Clientes** (5 mineras, 3 distribuidoras, 2 centros)
- **4 Vehículos** con capacidades
- **6 KPIs** principales
- **3 Métodos** de uso (CLI, GUI, Notebook)
- **100%** Documentado

---

## 🆘 PROBLEMAS

**Error de módulo?**

```bash
pip install -r requirements.txt
```

**GUI no abre?**

```bash
pip install PyQt6==6.6.1
python gui/main.py
```

**Más ayuda?** Ver `README.md` o `PRIMEROS_PASOS.md`

---

## 📞 REFERENCIA RÁPIDA

```
Archivo              Función
─────────────────────────────────────
INICIO.py            Menú principal
quick_start.py       Simulación
gui/main.py          GUI
config.py            Configuración
README.md            Docs completas
```

---

**¡Ya está todo listo. Ejecuta: `python INICIO.py`**
