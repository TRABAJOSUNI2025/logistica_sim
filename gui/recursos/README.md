# 📁 Recursos de la GUI - Sistema de Simulación Logística

Este directorio contiene todos los recursos visuales para la interfaz gráfica PyQt6.

---

## 📂 Estructura

```
recursos/
├── estilos.qss              ✅ Archivo de estilos CSS (YA INCLUIDO)
├── iconos/                  📥 Ícono para descargar
│   ├── inicio.png           (64x64 px) - Ícono para menú principal
│   ├── simulacion.png       (64x64 px) - Ícono simulación de demanda
│   ├── indicadores.png      (64x64 px) - Ícono indicadores/KPIs
│   ├── reporte.png          (64x64 px) - Ícono reporte final
│   ├── catalogo.png         (64x64 px) - Ícono catálogos
│   ├── guardar.png          (32x32 px) - Ícono guardar
│   ├── exportar.png         (32x32 px) - Ícono exportar
│   ├── volver.png           (32x32 px) - Ícono volver atrás
│   └── actualizar.png       (32x32 px) - Ícono actualizar
│
└── logos/                   📥 Logos para descargar
    ├── ferreyros_logo.png   (200x200 px) - Logo Ferreyros
    ├── andes_logo.png       (200x200 px) - Logo Andes Logistics
    └── banner.png           (800x100 px) - Banner principal
```

---

## ✅ Lo que ya está incluido

### **estilos.qss**

Archivo de estilos CSS profesional con:

- ✅ Colores corporativos Ferreyros (Amarillo #FFD700, Naranja #FFA500)
- ✅ Estilos para botones, labels, tablas
- ✅ Estilos para tabs, inputs, frames
- ✅ Tarjetas de color para alertas
- ✅ Scroll bars personalizados
- ✅ Efectos hover y focus

**Cómo usar:**

```python
# En gui/main.py o cualquier ventana:
app = QApplication(sys.argv)

# Cargar estilos
with open('gui/recursos/estilos.qss', 'r') as f:
    stylesheet = f.read()
    app.setStyleSheet(stylesheet)
```

---

## 📥 Cómo Obtener los Iconos

### **Opción 1: Descargar de sitios gratuitos** (RECOMENDADO)

#### Para Ícono de Menú (64x64):

1. Ir a: https://www.flaticon.com o https://www.icooon-mono.com
2. Buscar:
   - `home icon` → guardar como `inicio.png`
   - `rocket icon` → guardar como `simulacion.png`
   - `chart icon` → guardar como `indicadores.png`
   - `document icon` → guardar como `reporte.png`
   - `box icon` → guardar como `catalogo.png`

#### Para Ícono de Acciones (32x32):

- `save icon` → guardar como `guardar.png`
- `export icon` → guardar como `exportar.png`
- `back arrow` → guardar como `volver.png`
- `refresh icon` → guardar como `actualizar.png`

3. Redimensionar a 64x64 o 32x32 respectivamente
4. Guardar en `gui/recursos/iconos/`

### **Opción 2: Usar Iconos de Material Design**

Descargar de: https://www.material-icons.com

```
Material Icons (PNG 24px o 48px)
- home
- rocket_launch
- analytics
- description
- inventory_2
- save
- download
- arrow_back
- refresh
```

Redimensionar y guardar en `iconos/`

### **Opción 3: Generar con Python** (Script)

```python
# script_generar_iconos.py
from PIL import Image, ImageDraw
import os

def crear_icono_simple(nombre, emoji_char, size=64):
    """Crea ícono simple con emoji"""
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Dibujar fondo
    draw.rectangle([0, 0, size, size], fill='#FFD700', outline='#FFA500', width=2)

    # Guardar
    img.save(f'gui/recursos/iconos/{nombre}.png')

# Crear ícono de ejemplo
crear_icono_simple('inicio', '🏠')
crear_icono_simple('simulacion', '🚀')
crear_icono_simple('indicadores', '📊')
crear_icono_simple('reporte', '📋')
crear_icono_simple('catalogo', '📦')
```

---

## 🎨 Logos Corporativos

### **Para Ferreyros Logo:**

1. Ir a: https://www.ferreyros.com.pe
2. Descargar logo en alta resolución
3. Redimensionar a 200x200 px
4. Guardar como `ferreyros_logo.png`

### **Para Andes Logistics Logo:**

Si no tienen logo, puedes crear uno simple con Python:

```python
from PIL import Image, ImageDraw, ImageFont

# Crear imagen
img = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(img)

# Dibujar fondo amarillo
draw.rectangle([0, 0, 200, 200], fill='#FFD700', outline='#FFA500', width=3)

# Agregar texto
draw.text((50, 85), "ANDES", fill='black', font=None)
draw.text((50, 110), "LOGISTICS", fill='black', font=None)

# Guardar
img.save('gui/recursos/logos/andes_logo.png')
```

### **Para Banner:**

- Dimensiones: 800x100 px
- Contenido: Logo + Texto "Sistema de Simulación Logística"
- Colores: Fondo #FFD700, texto negro

---

## 🔧 Cómo Usar los Recursos en el Código

### **Cargar Estilos:**

```python
def aplicar_estilos(app):
    """Carga los estilos de la aplicación"""
    ruta_estilos = os.path.join(
        os.path.dirname(__file__),
        'recursos/estilos.qss'
    )

    with open(ruta_estilos, 'r', encoding='utf-8') as f:
        stylesheet = f.read()

    app.setStyleSheet(stylesheet)
```

### **Cargar Ícono en Botón:**

```python
from PyQt6.QtGui import QIcon

# Crear botón con ícono
btn = QPushButton("Simular")
ruta_icono = os.path.join(
    os.path.dirname(__file__),
    'recursos/iconos/simulacion.png'
)
btn.setIcon(QIcon(ruta_icono))
btn.setIconSize(QSize(64, 64))
```

### **Cargar Logo:**

```python
from PyQt6.QtGui import QPixmap

# Mostrar logo en label
label_logo = QLabel()
ruta_logo = os.path.join(
    os.path.dirname(__file__),
    'recursos/logos/ferreyros_logo.png'
)
pixmap = QPixmap(ruta_logo)
pixmap = pixmap.scaledToWidth(200)
label_logo.setPixmap(pixmap)
```

---

## 📋 Checklist de Instalación

- [ ] `estilos.qss` - ✅ Ya incluido
- [ ] Crear carpeta `iconos/` - ✅ Ya creada
- [ ] Crear carpeta `logos/` - ✅ Ya creada
- [ ] Descargar 9 ícono (64x64 y 32x32)
- [ ] Descargar 3 logos
- [ ] Guardar en carpetas respectivas
- [ ] Verificar rutas en código
- [ ] Probar interfaz gráfica

---

## 💾 Alternativa: Usar Unicode Emojis

Si no quieres descargar ícono, puedes usar emojis Unicode:

```python
# En botones
btn_inicio = QPushButton("🏠 Menú Principal")
btn_simulacion = QPushButton("🚀 Simular")
btn_indicadores = QPushButton("📊 Indicadores")
btn_reporte = QPushButton("📋 Reporte")
btn_catalogo = QPushButton("📦 Catálogos")
```

**Ventajas:**

- ✅ Sin necesidad de descargar archivos
- ✅ Funciona en todos los sistemas
- ✅ Fácil de cambiar
- ✅ Ligero

---

## 🎯 Recomendación Final

**Solución 3 en 1:**

1. ✅ Usar `estilos.qss` (YA INCLUIDO)
2. ✅ Usar emojis Unicode en botones (SIN DESCARGAS)
3. ✅ Agregar ícono PNG cuando sea necesario (OPCIONAL)

Esta combinación te da:

- 🎨 Interfaz profesional
- ⚡ Implementación rápida
- 💻 Compatibilidad total
- 📦 Fácil de mantener

---

## 📝 Notas

- Los estilos se aplican automáticamente a toda la aplicación
- Redimensiona las imágenes para consistencia visual
- Usa colores corporativos: #FFD700 (amarillo), #FFA500 (naranja)
- Mantén las imágenes en formato PNG con transparencia

---

**¡Recursos listos para usar!** 🎨
