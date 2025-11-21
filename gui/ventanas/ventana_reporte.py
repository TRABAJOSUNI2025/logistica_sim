"""
ventana_reporte.py - Pantalla de reporte final
"""

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QTextEdit,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class VentanaReporte(QWidget):
    """Pantalla de reporte final"""

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
        titulo = QLabel("REPORTE LOGÍSTICO FINAL")
        titulo_font = QFont("Arial", 18, QFont.Weight.Bold)
        titulo.setFont(titulo_font)
        layout.addWidget(titulo)

        # Área de texto del reporte
        self.texto_reporte = QTextEdit()
        self.texto_reporte.setReadOnly(True)
        self.texto_reporte.setText(self.generar_reporte_ejemplo())
        self.texto_reporte.setFont(QFont("Courier New", 9))
        layout.addWidget(self.texto_reporte)

        # Botones de acción
        h_botones = QHBoxLayout()

        btn_exportar_txt = QPushButton("📄 Exportar TXT")
        btn_exportar_txt.setFixedWidth(140)
        btn_exportar_txt.clicked.connect(self.exportar_txt)

        btn_exportar_csv = QPushButton("📊 Exportar CSV")
        btn_exportar_csv.setFixedWidth(140)
        btn_exportar_csv.clicked.connect(self.exportar_csv)

        btn_reiniciar = QPushButton("🔄 Nueva Simulación")
        btn_reiniciar.setFixedWidth(140)
        btn_reiniciar.clicked.connect(self.ventana_principal.volver_menu)

        btn_volver = QPushButton("◀ Volver")
        btn_volver.setFixedWidth(100)
        btn_volver.clicked.connect(self.ventana_principal.volver_menu)

        h_botones.addStretch()
        h_botones.addWidget(btn_exportar_txt)
        h_botones.addWidget(btn_exportar_csv)
        h_botones.addWidget(btn_reiniciar)
        h_botones.addWidget(btn_volver)
        layout.addLayout(h_botones)

    def generar_reporte_ejemplo(self):
        """Genera un reporte de ejemplo"""
        reporte = """
================================================================================
              REPORTE LOGÍSTICO - ANDES LOGISTICS S.A.
================================================================================

RESUMEN DE OPERACIONES:
────────────────────────────────────────────────────────────────────────────
  Total pedidos recibidos: 72
  Total unidades solicitadas: 8,965
  Total unidades entregadas: 8,540
  Total unidades no entregadas: 425
  Backlog: 4.7%

INDICADORES GLOBALES:
────────────────────────────────────────────────────────────────────────────
  OTIF: 93.10%
  Fill Rate: 95.30%
  Backlog Rate: 4.70%
  Productividad de Picking: 182.40 unid/h
  Utilización de Flota: 87.50%

ALERTAS DETECTADAS:
────────────────────────────────────────────────────────────────────────────
  [ALTO] OTIF bajo (93.10% < 95.00%)
  [MEDIO] Utilización de flota alta (87.50% > 85.00%)

RECOMENDACIONES:
────────────────────────────────────────────────────────────────────────────
  1. Reasignar pedidos entre zonas para equilibrar carga
  2. Incrementar personal de picking en horas pico
  3. Optimizar rutas de transporte para mejorar eficiencia
  4. Revisar pronóstico de demanda y reaprovisionamiento

================================================================================
Generado: 2025-11-20 14:30:45
"""
        return reporte

    def exportar_txt(self):
        """Exporta el reporte a TXT"""
        print("Exportando a TXT...")

    def exportar_csv(self):
        """Exporta el reporte a CSV"""
        print("Exportando a CSV...")
