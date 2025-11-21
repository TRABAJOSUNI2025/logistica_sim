"""
verificador_integridad.py - Verifica la integridad completa del proyecto

Valida:
- Estructura de carpetas
- Existencia de archivos clave
- Integridad de código
- Importaciones
- Configuración
"""

import os
import sys
from pathlib import Path
from datetime import datetime


class VerificadorIntegridad:
    """Verifica la integridad del proyecto"""
    
    def __init__(self):
        self.base = Path(__file__).parent
        self.resultados = {
            'estructura': [],
            'archivos': [],
            'codigo': [],
            'importaciones': [],
            'configuracion': [],
        }
        self.total_checks = 0
        self.checks_pasados = 0
        
    def verificar_estructura(self):
        """Verifica estructura de carpetas"""
        print("\n" + "="*70)
        print("1️⃣ VERIFICANDO ESTRUCTURA DE CARPETAS")
        print("="*70)
        
        carpetas = {
            "sistema": self.base / "sistema",
            "gui": self.base / "gui",
            "gui/ventanas": self.base / "gui" / "ventanas",
            "gui/recursos": self.base / "gui" / "recursos",
            "gui/recursos/iconos": self.base / "gui" / "recursos" / "iconos",
            "gui/recursos/logos": self.base / "gui" / "recursos" / "logos",
        }
        
        for nombre, ruta in carpetas.items():
            self.total_checks += 1
            existe = ruta.exists()
            self.resultados['estructura'].append((nombre, existe))
            
            if existe:
                print(f"✅ {nombre}")
                self.checks_pasados += 1
            else:
                print(f"❌ {nombre}")
    
    def verificar_archivos_clave(self):
        """Verifica existencia de archivos críticos"""
        print("\n" + "="*70)
        print("2️⃣ VERIFICANDO ARCHIVOS CLAVE")
        print("="*70)
        
        archivos = {
            "INICIO.py": self.base / "INICIO.py",
            "quick_start.py": self.base / "quick_start.py",
            "config.py": self.base / "config.py",
            "instalar_y_probar.py": self.base / "instalar_y_probar.py",
            "simulador.ipynb": self.base / "simulador.ipynb",
            "requirements.txt": self.base / "requirements.txt",
            "README.md": self.base / "README.md",
            "PRIMEROS_PASOS.md": self.base / "PRIMEROS_PASOS.md",
            "gui/main.py": self.base / "gui" / "main.py",
            "gui/recursos_manager.py": self.base / "gui" / "recursos_manager.py",
            "gui/recursos/estilos.qss": self.base / "gui" / "recursos" / "estilos.qss",
            "sistema/catalogos.py": self.base / "sistema" / "catalogos.py",
            "sistema/demanda.py": self.base / "sistema" / "demanda.py",
            "sistema/inventario.py": self.base / "sistema" / "inventario.py",
            "sistema/picking.py": self.base / "sistema" / "picking.py",
            "sistema/transporte.py": self.base / "sistema" / "transporte.py",
            "sistema/indicadores.py": self.base / "sistema" / "indicadores.py",
            "sistema/alertas.py": self.base / "sistema" / "alertas.py",
            "sistema/reporte.py": self.base / "sistema" / "reporte.py",
        }
        
        for nombre, ruta in archivos.items():
            self.total_checks += 1
            existe = ruta.exists()
            self.resultados['archivos'].append((nombre, existe))
            
            if existe:
                tamaño = ruta.stat().st_size
                print(f"✅ {nombre} ({tamaño:,} bytes)")
                self.checks_pasados += 1
            else:
                print(f"❌ {nombre} - NO ENCONTRADO")
    
    def verificar_codigo(self):
        """Verifica integridad de archivos Python"""
        print("\n" + "="*70)
        print("3️⃣ VERIFICANDO INTEGRIDAD CÓDIGO PYTHON")
        print("="*70)
        
        archivos_py = list(self.base.rglob("*.py"))
        
        for archivo in archivos_py:
            if "__pycache__" in str(archivo):
                continue
                
            self.total_checks += 1
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    # Validar sintaxis básica
                    compile(contenido, archivo, 'exec')
                print(f"✅ {archivo.relative_to(self.base)}")
                self.checks_pasados += 1
                self.resultados['codigo'].append((str(archivo.name), True))
            except SyntaxError as e:
                print(f"❌ {archivo.relative_to(self.base)}: {e}")
                self.resultados['codigo'].append((str(archivo.name), False))
            except Exception as e:
                print(f"⚠️  {archivo.relative_to(self.base)}: {type(e).__name__}")
    
    def verificar_importaciones(self):
        """Verifica importaciones críticas"""
        print("\n" + "="*70)
        print("4️⃣ VERIFICANDO IMPORTACIONES")
        print("="*70)
        
        modulos = [
            ("numpy", "NumPy"),
            ("pandas", "Pandas"),
            ("PyQt6.QtWidgets", "PyQt6 Widgets"),
            ("PyQt6.QtCore", "PyQt6 Core"),
            ("PyQt6.QtGui", "PyQt6 GUI"),
        ]
        
        for modulo, nombre in modulos:
            self.total_checks += 1
            try:
                __import__(modulo)
                print(f"✅ {nombre}")
                self.checks_pasados += 1
                self.resultados['importaciones'].append((nombre, True))
            except ImportError:
                print(f"❌ {nombre} - No instalado")
                self.resultados['importaciones'].append((nombre, False))
    
    def verificar_configuracion(self):
        """Verifica configuración del sistema"""
        print("\n" + "="*70)
        print("5️⃣ VERIFICANDO CONFIGURACIÓN")
        print("="*70)
        
        try:
            from config import (
                CAPACIDAD_PICKING_DIARIA,
                PUNTO_REORDEN,
                STOCK_INICIAL_POR_SKU,
                TAMAÑO_BATCH_REPOSICION,
                VELOCIDAD_TRANSPORTE,
            )
            
            configs = [
                ("CAPACIDAD_PICKING_DIARIA", CAPACIDAD_PICKING_DIARIA),
                ("PUNTO_REORDEN", PUNTO_REORDEN),
                ("STOCK_INICIAL_POR_SKU", STOCK_INICIAL_POR_SKU),
                ("TAMAÑO_BATCH_REPOSICION", TAMAÑO_BATCH_REPOSICION),
                ("VELOCIDAD_TRANSPORTE", VELOCIDAD_TRANSPORTE),
            ]
            
            for nombre, valor in configs:
                self.total_checks += 1
                if valor > 0:
                    print(f"✅ {nombre} = {valor}")
                    self.checks_pasados += 1
                    self.resultados['configuracion'].append((nombre, True))
                else:
                    print(f"❌ {nombre} = {valor} (valor inválido)")
                    self.resultados['configuracion'].append((nombre, False))
                    
        except Exception as e:
            print(f"❌ Error cargando configuración: {e}")
    
    def generar_reporte(self):
        """Genera reporte final"""
        print("\n" + "="*70)
        print("📊 REPORTE FINAL")
        print("="*70 + "\n")
        
        for categoria, resultados in self.resultados.items():
            if not resultados:
                continue
            
            pasados = sum(1 for _, resultado in resultados if resultado)
            total = len(resultados)
            porcentaje = (pasados / total * 100) if total > 0 else 0
            
            categoria_display = categoria.replace('_', ' ').title()
            print(f"{categoria_display}: {pasados}/{total} ({porcentaje:.0f}%)")
        
        print(f"\n{'─'*70}")
        print(f"TOTAL: {self.checks_pasados}/{self.total_checks} checks pasados")
        print(f"{'─'*70}\n")
        
        porcentaje_total = (self.checks_pasados / self.total_checks * 100) if self.total_checks > 0 else 0
        
        if porcentaje_total == 100:
            print("🎉 ¡PROYECTO ÍNTEGRO Y FUNCIONAL! 🎉\n")
            return True
        elif porcentaje_total >= 90:
            print("⚠️  Proyecto mayormente íntegro (90%+)\n")
            return True
        else:
            print("❌ Problemas detectados\n")
            return False
    
    def ejecutar_verificacion_completa(self):
        """Ejecuta verificación completa"""
        print("\n" + "█" * 70)
        print("█" + " VERIFICADOR DE INTEGRIDAD - PROYECTO LOGÍSTICA ".center(68) + "█")
        print("█" * 70)
        
        self.verificar_estructura()
        self.verificar_archivos_clave()
        self.verificar_codigo()
        self.verificar_importaciones()
        self.verificar_configuracion()
        
        exitoso = self.generar_reporte()
        
        print("\n📋 INFORMACIÓN DEL SISTEMA")
        print("─" * 70)
        print(f"Ruta base: {self.base}")
        print(f"Python: {sys.version.split()[0]}")
        print(f"Fecha verificación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Plataforma: {sys.platform}")
        print()
        
        return 0 if exitoso else 1


def main():
    """Función principal"""
    try:
        verificador = VerificadorIntegridad()
        return verificador.ejecutar_verificacion_completa()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
