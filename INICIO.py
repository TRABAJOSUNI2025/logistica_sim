"""
INICIO.py - Punto de entrada principal del Sistema de Logística Ferreyros

Interfaz unificada para acceder a todas las funcionalidades:
- Simulación rápida
- Notebook Jupyter
- Interfaz gráfica PyQt6
- Validación y diagnóstico

📖 Ver COMIENZA_AQUI.md para guía rápida
📖 Ver PRIMEROS_PASOS.md para más opciones
📖 Ver README.md para documentación técnica
"""

import sys
import os
from pathlib import Path
from typing import Optional


def mostrar_banner():
    """Muestra banner de bienvenida"""
    print("\n" + "█" * 80)
    print("█" + " " * 78 + "█")
    print(
        "█"
        + "  SISTEMA DE SIMULACIÓN LOGÍSTICA - FERREYROS / ANDES LOGISTICS  ".center(78)
        + "█"
    )
    print("█" + " " * 78 + "█")
    print("█" * 80 + "\n")


def mostrar_menu_principal():
    """Muestra menú principal"""
    print("┌" + "─" * 78 + "┐")
    print("│ SELECCIONA UNA OPCIÓN:".ljust(79) + "│")
    print("├" + "─" * 78 + "┤")
    print("│ 1. 🚀 SIMULACIÓN RÁPIDA (CLI - 3 días)                                  │")
    print("│ 2. 📊 NOTEBOOK INTERACTIVO (Jupyter - análisis completo)               │")
    print("│ 3. 🖥️  INTERFAZ GRÁFICA (PyQt6 - GUI profesional)                       │")
    print("│ 4. 🔧 INSTALACIÓN Y VALIDACIÓN (Diagnosticar problemas)                │")
    print("│ 5. 📋 VER CONFIGURACIÓN ACTUAL                                         │")
    print("│ 6. 📖 VER DOCUMENTACIÓN                                                │")
    print("│ 0. ❌ SALIR                                                             │")
    print("└" + "─" * 78 + "┘\n")


def opcion_simulacion_rapida():
    """Opción 1: Ejecutar simulación rápida"""
    print("┌" + "─" * 78 + "┐")
    print("│ 🚀 SIMULACIÓN RÁPIDA - 3 DÍAS".ljust(79) + "│")
    print("└" + "─" * 78 + "┘\n")

    try:
        from quick_start import ejecutar_simulacion_3_dias

        ejecutar_simulacion_3_dias()
        print("\n✅ Simulación completada exitosamente")
        return True
    except FileNotFoundError:
        print("❌ Error: No se encuentra quick_start.py")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def opcion_notebook():
    """Opción 2: Lanzar Jupyter Notebook"""
    print("┌" + "─" * 78 + "┐")
    print("│ 📊 NOTEBOOK INTERACTIVO".ljust(79) + "│")
    print("└" + "─" * 78 + "┘\n")

    try:
        import subprocess

        notebook_path = Path(__file__).parent / "simulador.ipynb"

        if not notebook_path.exists():
            print(f"❌ Error: No se encuentra {notebook_path}")
            return False

        print(f"▶ Lanzando Jupyter en: {notebook_path}\n")
        print("📝 El navegador se abrirá automáticamente...")
        print("💡 Para detener: presiona Ctrl+C en la terminal\n")

        subprocess.run(f"jupyter notebook {notebook_path}", shell=True)
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Asegúrate de tener Jupyter instalado: pip install jupyter")
        return False


def opcion_gui():
    """Opción 3: Lanzar GUI PyQt6"""
    print("┌" + "─" * 78 + "┐")
    print("│ 🖥️  INTERFAZ GRÁFICA (PyQt6)".ljust(79) + "│")
    print("└" + "─" * 78 + "┘\n")

    try:
        from gui import main as gui_main

        print("▶ Inicializando aplicación gráfica...\n")
        print("✅ GUI iniciada")
        print("💡 Cierra la ventana para terminar\n")

        gui_main.main()

    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("💡 Asegúrate de instalar dependencias: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def opcion_instalacion():
    """Opción 4: Instalar y validar"""
    print("┌" + "─" * 78 + "┐")
    print("│ 🔧 INSTALACIÓN Y VALIDACIÓN".ljust(79) + "│")
    print("└" + "─" * 78 + "┘\n")

    try:
        import subprocess

        resultado = subprocess.run(f"{sys.executable} instalar_y_probar.py", shell=True)
        return resultado.returncode == 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def opcion_configuracion():
    """Opción 5: Ver configuración actual"""
    print("┌" + "─" * 78 + "┐")
    print("│ 📋 CONFIGURACIÓN ACTUAL".ljust(79) + "│")
    print("└" + "─" * 78 + "┘\n")

    try:
        from config import CONFIGURACION, mostrar_configuracion

        mostrar_configuracion()
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def opcion_documentacion():
    """Opción 6: Ver documentación"""
    print("┌" + "─" * 78 + "┐")
    print("│ 📖 DOCUMENTACIÓN".ljust(79) + "│")
    print("└" + "─" * 78 + "┘\n")

    print("Documentos disponibles:\n")

    docs = [
        ("README.md", "Documentación técnica completa"),
        ("INICIO_RAPIDO.md", "Guía de inicio rápido"),
        ("RESUMEN_PROYECTO.md", "Resumen del proyecto"),
        ("gui/recursos/README.md", "Guía de recursos (iconos, logos)"),
    ]

    directorio = Path(__file__).parent

    for archivo, descripcion in docs:
        ruta = directorio / archivo
        existe = "✅" if ruta.exists() else "❌"
        print(f"{existe} {archivo}")
        print(f"   {descripcion}\n")

    return True


def obtener_opcion_valida() -> str:
    """Obtiene opción válida del usuario"""
    while True:
        try:
            opcion = input("Ingresa tu selección (0-6): ").strip()
            if opcion in ["0", "1", "2", "3", "4", "5", "6"]:
                return opcion
            print("❌ Opción no válida. Intenta de nuevo.\n")
        except KeyboardInterrupt:
            print("\n\n⚠️ Operación cancelada por el usuario")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Error: {e}\n")


def main():
    """Función principal"""
    # Cambiar al directorio del script
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    # Agregar directorio a path
    sys.path.insert(0, str(script_dir))

    while True:
        mostrar_banner()
        mostrar_menu_principal()

        opcion = obtener_opcion_valida()

        print()

        if opcion == "0":
            print(
                "👋 ¡Hasta luego! Gracias por usar el Sistema de Logística Ferreyros\n"
            )
            break

        elif opcion == "1":
            opcion_simulacion_rapida()

        elif opcion == "2":
            opcion_notebook()

        elif opcion == "3":
            opcion_gui()

        elif opcion == "4":
            opcion_instalacion()

        elif opcion == "5":
            opcion_configuracion()

        elif opcion == "6":
            opcion_documentacion()

        # Pausa antes de volver al menú
        if opcion != "0":
            print("\n" + "─" * 80)
            input("Presiona Enter para volver al menú principal...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        sys.exit(1)
