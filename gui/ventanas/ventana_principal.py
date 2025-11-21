"""
ventana_principal.py - Pantalla principal de la aplicación
"""

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
    QStackedWidget,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QColor
from PyQt6.QtCore import QSize

from .ventana_catalogos import VentanaCatalogos
from .ventana_simulacion import VentanaSimulacion
from .ventana_indicadores import VentanaIndicadores
from .ventana_reporte import VentanaReporte


class VentanaPrincipal(QMainWindow):
    """Ventana principal de la aplicación"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Simulación Logística - Andes Logistics S.A.")
        self.setGeometry(100, 100, 1200, 800)

        # Crear widget central con stack (para cambiar pantallas)
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)

        # Stack para cambiar entre pantallas
        self.stacked_widget = QStackedWidget()

        # Crear todas las ventanas
        self.ventana_menu = self.crear_menu_principal()
        self.ventana_catalogos = VentanaCatalogos(self)
        self.ventana_simulacion = VentanaSimulacion(self)
        self.ventana_indicadores = VentanaIndicadores(self)
        self.ventana_reporte = VentanaReporte(self)

        # Agregar al stack
        self.stacked_widget.addWidget(self.ventana_menu)
        self.stacked_widget.addWidget(self.ventana_catalogos)
        self.stacked_widget.addWidget(self.ventana_simulacion)
        self.stacked_widget.addWidget(self.ventana_indicadores)
        self.stacked_widget.addWidget(self.ventana_reporte)

        # Layout principal
        layout = QVBoxLayout(self.widget_central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.stacked_widget)

        self.aplicar_estilos()

    def crear_menu_principal(self):
        """Crea la pantalla del menú principal"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)

        # Header
        header = QFrame()
        header_layout = QVBoxLayout(header)

        titulo = QLabel("SISTEMA DE SIMULACIÓN LOGÍSTICA")
        titulo_font = QFont("Arial", 24, QFont.Weight.Bold)
        titulo.setFont(titulo_font)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitulo = QLabel("Andes Logistics S.A. - Ferreyros")
        subtitulo_font = QFont("Arial", 14)
        subtitulo.setFont(subtitulo_font)
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitulo.setStyleSheet("color: #666;")

        header_layout.addWidget(titulo)
        header_layout.addWidget(subtitulo)
        layout.addWidget(header)

        # Espaciador
        layout.addSpacing(30)

        # Botones principales
        botones_info = [
            ("📚 Catálogos", "Gestionar SKUs, clientes y vehículos", 0),
            ("🚀 Simular Demanda", "Generar pedidos y simulación", 2),
            ("📊 Indicadores", "Análisis de KPIs y alertas", 3),
            ("📋 Reporte Final", "Resumen y recomendaciones", 4),
        ]

        for texto, desc, indice in botones_info:
            btn = self.crear_boton_menu(texto, desc, indice)
            layout.addWidget(btn)

        layout.addStretch()

        # Footer
        footer = QLabel("© 2025 Andes Logistics S.A. Todos los derechos reservados.")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setStyleSheet("color: #999; font-size: 10px;")
        layout.addWidget(footer)

        return widget

    def crear_boton_menu(self, titulo, descripcion, indice):
        """Crea un botón del menú"""
        btn = QPushButton(f"{titulo}\n{descripcion}")
        btn.setFixedHeight(80)
        btn.setStyleSheet(
            """
            QPushButton {
                background-color: #FFD700;
                color: black;
                border: 2px solid #FFA500;
                border-radius: 8px;
                font-weight: bold;
                font-size: 13px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FFC700;
                border: 2px solid #FF8C00;
            }
        """
        )
        btn.clicked.connect(lambda: self.mostrar_pantalla(indice))
        return btn

    def mostrar_pantalla(self, indice):
        """Cambia a la pantalla indicada"""
        self.stacked_widget.setCurrentIndex(indice)

    def volver_menu(self):
        """Vuelve al menú principal"""
        self.mostrar_pantalla(0)

    def aplicar_estilos(self):
        """Aplica estilos globales a la ventana"""
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: white;
            }
            QLabel {
                color: black;
            }
        """
        )
