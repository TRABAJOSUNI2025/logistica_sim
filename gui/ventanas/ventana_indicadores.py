"""
ventana_indicadores.py - Pantalla de indicadores y alertas
"""

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor


class VentanaIndicadores(QWidget):
    """Pantalla de indicadores y alertas"""

    def __init__(self, ventana_principal):
        super().__init__()
        self.ventana_principal = ventana_principal
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz"""
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Título
        titulo = QLabel("INDICADORES Y ALERTAS")
        titulo_font = QFont("Arial", 18, QFont.Weight.Bold)
        titulo.setFont(titulo_font)
        layout.addWidget(titulo)

        # Grid de indicadores principales
        h_indicadores = QHBoxLayout()

        indicadores_info = [
            ("OTIF", "95.2%", "verde"),
            ("Fill Rate", "97.1%", "verde"),
            ("Backlog", "2.9%", "amarillo"),
            ("Productividad", "181.25 unid/h", "verde"),
            ("Flota", "86.7%", "amarillo"),
        ]

        for titulo_ind, valor, color in indicadores_info:
            card = self.crear_card_indicador(titulo_ind, valor, color)
            h_indicadores.addWidget(card)

        layout.addLayout(h_indicadores)
        layout.addSpacing(10)

        # Alertas
        label_alertas = QLabel("ALERTAS DETECTADAS")
        label_alertas.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(label_alertas)

        tabla_alertas = QTableWidget()
        tabla_alertas.setColumnCount(3)
        tabla_alertas.setHorizontalHeaderLabels(["Tipo", "Severidad", "Mensaje"])
        tabla_alertas.setRowCount(2)

        # Ejemplos de alertas
        alertas_ejemplo = [
            ("OTIF_BAJO", "ALTO", "OTIF menor al 95% - Verificar tiempos"),
            ("FLOTA_SATURADA", "MEDIO", "Utilización de flota > 85%"),
        ]

        for i, (tipo, severidad, mensaje) in enumerate(alertas_ejemplo):
            tabla_alertas.setItem(i, 0, QTableWidgetItem(tipo))
            item_sev = QTableWidgetItem(severidad)
            if severidad == "ALTO":
                item_sev.setBackground(QColor("#FFB6C6"))
            elif severidad == "MEDIO":
                item_sev.setBackground(QColor("#FFEB99"))
            tabla_alertas.setItem(i, 1, item_sev)
            tabla_alertas.setItem(i, 2, QTableWidgetItem(mensaje))

        tabla_alertas.resizeColumnsToContents()
        layout.addWidget(tabla_alertas)

        # Botones
        h_botones = QHBoxLayout()

        btn_actualizar = QPushButton("🔄 Actualizar")
        btn_actualizar.setFixedWidth(120)

        btn_volver = QPushButton("◀ Volver")
        btn_volver.setFixedWidth(100)
        btn_volver.clicked.connect(self.ventana_principal.volver_menu)

        h_botones.addStretch()
        h_botones.addWidget(btn_actualizar)
        h_botones.addWidget(btn_volver)
        layout.addLayout(h_botones)

    def crear_card_indicador(self, titulo, valor, color):
        """Crea una tarjeta de indicador"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(5)

        label_titulo = QLabel(titulo)
        label_titulo.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_valor = QLabel(valor)
        label_valor.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        label_valor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        color_map = {"verde": "#D4EDDA", "amarillo": "#FFF3CD", "rojo": "#F8D7DA"}

        border_color_map = {
            "verde": "#28A745",
            "amarillo": "#FFC107",
            "rojo": "#DC3545",
        }

        bg_color = color_map.get(color, "#E9ECEF")
        border_color = border_color_map.get(color, "#6C757D")

        widget.setStyleSheet(
            f"""
            QWidget {{
                background-color: {bg_color};
                border: 2px solid {border_color};
                border-radius: 8px;
                padding: 10px;
            }}
        """
        )

        layout.addWidget(label_titulo)
        layout.addWidget(label_valor)

        return widget
