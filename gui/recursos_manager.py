"""
recursos.py - Gestor de recursos (estilos e ícono) para la GUI

Proporciona funciones para cargar estilos, ícono y logos
"""

import os
from pathlib import Path
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize


def obtener_ruta_recursos():
    """Obtiene la ruta absoluta de la carpeta de recursos"""
    ruta_actual = Path(__file__).parent
    return ruta_actual / "recursos"


def cargar_estilos(app):
    """
    Carga y aplica los estilos CSS a la aplicación
    
    Args:
        app: Instancia de QApplication
    
    Returns:
        bool: True si se cargó correctamente, False en caso contrario
    """
    try:
        ruta_estilos = obtener_ruta_recursos() / "estilos.qss"
        
        if not ruta_estilos.exists():
            print(f"⚠️ Archivo de estilos no encontrado: {ruta_estilos}")
            return False
        
        with open(ruta_estilos, 'r', encoding='utf-8') as f:
            stylesheet = f.read()
        
        app.setStyleSheet(stylesheet)
        print(f"✓ Estilos cargados correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error al cargar estilos: {e}")
        return False


def cargar_icono(nombre_icono, tamaño=64):
    """
    Carga un ícono desde la carpeta de ícono
    
    Args:
        nombre_icono: Nombre del archivo sin extensión (ej: 'inicio', 'simulacion')
        tamaño: Tamaño del ícono en píxeles
    
    Returns:
        QIcon: Ícono cargado o None si no existe
    """
    try:
        ruta_icono = obtener_ruta_recursos() / "iconos" / f"{nombre_icono}.png"
        
        if not ruta_icono.exists():
            print(f"⚠️ Ícono no encontrado: {ruta_icono}")
            # Retornar ícono vacío para no romper la interfaz
            return QIcon()
        
        icono = QIcon(str(ruta_icono))
        return icono
        
    except Exception as e:
        print(f"❌ Error al cargar ícono {nombre_icono}: {e}")
        return QIcon()


def cargar_logo(nombre_logo, ancho=200):
    """
    Carga un logo desde la carpeta de logos
    
    Args:
        nombre_logo: Nombre del archivo sin extensión (ej: 'ferreyros_logo')
        ancho: Ancho en píxeles para redimensionar
    
    Returns:
        QPixmap: Logo cargado o None si no existe
    """
    try:
        ruta_logo = obtener_ruta_recursos() / "logos" / f"{nombre_logo}.png"
        
        if not ruta_logo.exists():
            print(f"⚠️ Logo no encontrado: {ruta_logo}")
            return None
        
        pixmap = QPixmap(str(ruta_logo))
        if pixmap.isNull():
            print(f"⚠️ No se pudo cargar la imagen: {ruta_logo}")
            return None
        
        # Redimensionar manteniendo aspecto
        pixmap = pixmap.scaledToWidth(ancho)
        return pixmap
        
    except Exception as e:
        print(f"❌ Error al cargar logo {nombre_logo}: {e}")
        return None


def obtener_icono_con_emoji(emoji_char, nombre_fallback="inicio"):
    """
    Retorna un ícono usando emoji como alternativa
    
    Args:
        emoji_char: Carácter emoji (ej: '🚀')
        nombre_fallback: Nombre del archivo PNG como alternativa
    
    Returns:
        str: String con emoji listo para usar en botones
    """
    return emoji_char


def obtener_diccionario_iconos():
    """
    Retorna diccionario con todos los ícono disponibles
    
    Returns:
        dict: {nombre_icono: QIcon}
    """
    iconos = {
        'inicio': cargar_icono('inicio', 64),
        'simulacion': cargar_icono('simulacion', 64),
        'indicadores': cargar_icono('indicadores', 64),
        'reporte': cargar_icono('reporte', 64),
        'catalogo': cargar_icono('catalogo', 64),
        'guardar': cargar_icono('guardar', 32),
        'exportar': cargar_icono('exportar', 32),
        'volver': cargar_icono('volver', 32),
        'actualizar': cargar_icono('actualizar', 32),
    }
    return iconos


def obtener_diccionario_emojis():
    """
    Retorna diccionario con emojis como alternativa a ícono PNG
    
    Returns:
        dict: {accion: emoji}
    """
    emojis = {
        'inicio': '🏠',
        'simulacion': '🚀',
        'indicadores': '📊',
        'reporte': '📋',
        'catalogo': '📦',
        'guardar': '💾',
        'exportar': '📥',
        'volver': '◀',
        'actualizar': '🔄',
        'alertas': '⚠️',
        'exito': '✅',
        'error': '❌',
        'info': 'ℹ️',
    }
    return emojis


# Función de prueba
def probar_recursos():
    """Prueba la disponibilidad de recursos"""
    print("\n" + "=" * 70)
    print("PRUEBA DE RECURSOS")
    print("=" * 70 + "\n")
    
    ruta = obtener_ruta_recursos()
    print(f"Ruta de recursos: {ruta}")
    print(f"Existe: {ruta.exists()}")
    
    # Verificar estilos
    estilos = ruta / "estilos.qss"
    print(f"\n✓ estilos.qss: {'✅' if estilos.exists() else '❌'}")
    
    # Verificar carpetas
    carpeta_iconos = ruta / "iconos"
    carpeta_logos = ruta / "logos"
    print(f"✓ Carpeta iconos: {'✅' if carpeta_iconos.exists() else '❌'}")
    print(f"✓ Carpeta logos: {'✅' if carpeta_logos.exists() else '❌'}")
    
    # Listar ícono disponibles
    if carpeta_iconos.exists():
        iconos = list(carpeta_iconos.glob("*.png"))
        print(f"\nÍcono disponibles ({len(iconos)}):")
        for ico in sorted(iconos):
            print(f"  - {ico.name}")
    
    # Listar logos disponibles
    if carpeta_logos.exists():
        logos = list(carpeta_logos.glob("*.png"))
        print(f"\nLogos disponibles ({len(logos)}):")
        for logo in sorted(logos):
            print(f"  - {logo.name}")
    
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    probar_recursos()
