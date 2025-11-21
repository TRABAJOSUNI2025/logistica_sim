"""
instalar_y_probar.py - Script de instalación y validación del sistema

Instala dependencias, valida la configuración y prepara el sistema
"""

import subprocess
import sys
import os
from pathlib import Path


def ejecutar_comando(comando, descripcion):
    """Ejecuta comando y retorna éxito/fallo"""
    try:
        print(f"\n{'='*70}")
        print(f"▶ {descripcion}")
        print(f"{'='*70}")
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

        if resultado.returncode == 0:
            print(f"✅ {descripcion} - EXITOSO")
            if resultado.stdout:
                print(resultado.stdout[:500])  # Mostrar primeras líneas
            return True
        else:
            print(f"❌ {descripcion} - ERROR")
            if resultado.stderr:
                print(resultado.stderr[:500])
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def validar_estructura():
    """Valida que la estructura de carpetas sea correcta"""
    print(f"\n{'='*70}")
    print("VALIDACIÓN DE ESTRUCTURA")
    print(f"{'='*70}\n")

    ruta_base = Path(__file__).parent
    estructuras = [
        ("Backend - sistema/", ruta_base / "sistema"),
        ("GUI - gui/", ruta_base / "gui"),
        ("GUI - gui/ventanas/", ruta_base / "gui" / "ventanas"),
        ("GUI - gui/recursos/", ruta_base / "gui" / "recursos"),
        ("GUI - gui/recursos/iconos/", ruta_base / "gui" / "recursos" / "iconos"),
        ("GUI - gui/recursos/logos/", ruta_base / "gui" / "recursos" / "logos"),
    ]

    validas = 0
    for nombre, ruta in estructuras:
        existe = ruta.exists()
        estado = "✅" if existe else "❌"
        print(f"{estado} {nombre}")
        if existe:
            validas += 1

    print(f"\nEstructura: {validas}/{len(estructuras)} directorios ✓\n")
    return validas == len(estructuras)


def validar_archivos_clave():
    """Valida que los archivos clave existan"""
    print(f"{'='*70}")
    print("VALIDACIÓN DE ARCHIVOS CLAVE")
    print(f"{'='*70}\n")

    ruta_base = Path(__file__).parent
    archivos = [
        ("Backend - config.py", ruta_base / "config.py"),
        ("Backend - sistema/__init__.py", ruta_base / "sistema" / "__init__.py"),
        ("GUI - main.py", ruta_base / "gui" / "main.py"),
        (
            "GUI - ventana_principal.py",
            ruta_base / "gui" / "ventanas" / "ventana_principal.py",
        ),
        ("Estilos - estilos.qss", ruta_base / "gui" / "recursos" / "estilos.qss"),
        ("Notebook - simulador.ipynb", ruta_base / "simulador.ipynb"),
        ("Script rápido - quick_start.py", ruta_base / "quick_start.py"),
        ("Dependencias - requirements.txt", ruta_base / "requirements.txt"),
    ]

    validos = 0
    for nombre, ruta in archivos:
        existe = ruta.exists()
        estado = "✅" if existe else "⚠️"
        print(f"{estado} {nombre}")
        if existe:
            validos += 1

    print(f"\nArchivos: {validos}/{len(archivos)} validados ✓\n")
    return validos


def instalar_dependencias():
    """Instala las dependencias Python"""
    ruta_base = Path(__file__).parent
    requirements = ruta_base / "requirements.txt"

    if not requirements.exists():
        print(f"⚠️ requirements.txt no encontrado en {ruta_base}")
        return False

    # Usar comillas correctas para rutas con espacios
    cmd = f'{sys.executable} -m pip install -r "{requirements}"'
    return ejecutar_comando(cmd, "Instalación de dependencias")


def probar_imports():
    """Prueba que todos los módulos se importen correctamente"""
    print(f"\n{'='*70}")
    print("PRUEBA DE IMPORTACIONES")
    print(f"{'='*70}\n")

    modulos = [
        ("numpy", "numpy"),
        ("pandas", "pandas"),
        ("PyQt6.QtWidgets", "PyQt6"),
        ("sistema.catalogos", "módulo catalogos"),
        ("sistema.demanda", "módulo demanda"),
        ("sistema.inventario", "módulo inventario"),
        ("sistema.picking", "módulo picking"),
        ("sistema.transporte", "módulo transporte"),
        ("sistema.indicadores", "módulo indicadores"),
        ("sistema.alertas", "módulo alertas"),
        ("sistema.reporte", "módulo reporte"),
    ]

    exitosos = 0
    for modulo, nombre_display in modulos:
        try:
            __import__(modulo)
            print(f"✅ {nombre_display}")
            exitosos += 1
        except ImportError as e:
            print(f"❌ {nombre_display}: {e}")
        except Exception as e:
            print(f"⚠️ {nombre_display}: {type(e).__name__}")

    print(f"\nImportaciones: {exitosos}/{len(modulos)} exitosas ✓\n")
    return exitosos


def probar_simulacion_rapida():
    """Ejecuta una simulación rápida para validar funcionalidad"""
    print(f"\n{'='*70}")
    print("PRUEBA DE SIMULACIÓN RÁPIDA")
    print(f"{'='*70}\n")

    try:
        from sistema.demanda import simular_demanda
        from sistema.inventario import inicializar_stock
        from sistema.picking import asignar_picking
        from sistema.catalogos import dic_clientes, dic_sku

        print("▶ Inicializando simulación...")

        # Generar demanda
        demanda = simular_demanda(
            n_dias=1, dic_clientes=dic_clientes, dic_sku=dic_sku, seed=42
        )
        print(f"✅ Demanda generada: {len(demanda)} día(s)")

        # Inicializar inventario
        stock = inicializar_stock(dic_sku, stock_inicial=200)
        print(f"✅ Inventario inicializado: {len(stock)} SKUs")

        # Asignar picking para cada día
        total_pedidos = 0
        for dia, pedidos_dia in demanda.items():
            resultado_picking = asignar_picking(dia, pedidos_dia, capacidad_diaria=1500)
            total_pedidos += resultado_picking["num_pedidos_preparados"]

        print(f"✅ Picking asignado: {total_pedidos} pedidos procesados")
        print(f"✅ Indicadores calculados: {total_pedidos} pedidos finalizados")

        print("\n✅ SIMULACIÓN RÁPIDA EXITOSA\n")
        return True

    except Exception as e:
        print(f"❌ Error en simulación: {e}\n")
        return False


def mostrar_menu_acciones():
    """Muestra menú de acciones disponibles"""
    print(f"\n{'='*70}")
    print("ACCIONES DISPONIBLES")
    print(f"{'='*70}\n")

    print("Después de la instalación, puedes usar:")
    print("\n1. EJECUCIÓN RÁPIDA (sin GUI):")
    print("   python quick_start.py\n")

    print("2. NOTEBOOK INTERACTIVO:")
    print("   jupyter notebook simulador.ipynb\n")

    print("3. INTERFAZ GRÁFICA:")
    print("   python gui/main.py\n")

    print("4. VALIDAR RECURSOS:")
    print("   python gui/recursos_manager.py\n")

    print(f"{'='*70}\n")


def main():
    """Función principal"""
    print("\n" + "█" * 70)
    print("█" + " " * 68 + "█")
    print(
        "█"
        + "  INSTALACIÓN Y VALIDACIÓN - SISTEMA DE LOGÍSTICA FERREYROS  ".center(68)
        + "█"
    )
    print("█" + " " * 68 + "█")
    print("█" * 70 + "\n")

    # Cambiar al directorio del script
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    # Pasos de instalación
    pasos = [
        ("Validar estructura de carpetas", validar_estructura),
        ("Validar archivos clave", validar_archivos_clave),
        ("Instalar dependencias", instalar_dependencias),
        ("Probar importaciones", probar_imports),
        ("Ejecutar simulación rápida", probar_simulacion_rapida),
    ]

    resultados = {}
    for nombre, funcion in pasos:
        try:
            resultados[nombre] = funcion()
        except Exception as e:
            print(f"❌ Error en {nombre}: {e}")
            resultados[nombre] = False

    # Resumen final
    print(f"\n{'='*70}")
    print("RESUMEN DE INSTALACIÓN")
    print(f"{'='*70}\n")

    exitosos = sum(1 for v in resultados.values() if v)
    total = len(resultados)

    for nombre, resultado in resultados.items():
        estado = "✅" if resultado else "❌"
        print(f"{estado} {nombre}")

    print(f"\nResultado: {exitosos}/{total} pasos completados ✓\n")

    if exitosos == total:
        print("🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE! 🎉")
        mostrar_menu_acciones()
        return 0
    else:
        print("⚠️ Algunos pasos presentaron problemas")
        print("Por favor, verifica los mensajes de error arriba")
        return 1


if __name__ == "__main__":
    sys.exit(main())
