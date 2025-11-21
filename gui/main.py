"""
main.py - Punto de entrada de la aplicación PyQt6
"""

import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication

# Agregar directorio padre al path para imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from gui.ventanas.ventana_principal import VentanaPrincipal


def main():
    """Función principal que inicia la aplicación"""
    app = QApplication(sys.argv)

    # Configurar estilo
    app.setStyle("Fusion")

    # Crear ventana principal
    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
