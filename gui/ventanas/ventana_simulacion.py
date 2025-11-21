"""
ventana_simulacion.py - Pantalla de simulación de demanda
"""

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSpinBox,
    QCheckBox,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from sistema.catalogos import dic_sku, dic_clientes
from sistema.demanda import (
    simular_demanda,
    contar_unidades_pedidos,
    obtener_sku_mas_solicitado,
)


class VentanaSimulacion(QWidget):
    """Pantalla de simulación de demanda"""

    def __init__(self, ventana_principal):
        super().__init__()
        self.ventana_principal = ventana_principal
        self.pedidos_simulados = None
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz"""
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Título
        titulo = QLabel("SIMULACIÓN DE DEMANDA")
        titulo_font = QFont("Arial", 18, QFont.Weight.Bold)
        titulo.setFont(titulo_font)
        layout.addWidget(titulo)

        # Controles de entrada
        h_controles = QHBoxLayout()

        h_controles.addWidget(QLabel("Número de días:"))
        self.spin_dias = QSpinBox()
        self.spin_dias.setMinimum(1)
        self.spin_dias.setMaximum(30)
        self.spin_dias.setValue(7)
        h_controles.addWidget(self.spin_dias)

        h_controles.addSpacing(30)

        self.check_seed = QCheckBox("Usar semilla para reproducibilidad")
        h_controles.addWidget(self.check_seed)

        self.spin_seed = QSpinBox()
        self.spin_seed.setMinimum(0)
        self.spin_seed.setMaximum(999999)
        self.spin_seed.setValue(42)
        self.spin_seed.setEnabled(False)
        self.check_seed.stateChanged.connect(
            lambda: self.spin_seed.setEnabled(self.check_seed.isChecked())
        )
        h_controles.addWidget(self.spin_seed)

        h_controles.addStretch()

        btn_simular = QPushButton("🚀 Simular")
        btn_simular.setFixedWidth(120)
        btn_simular.clicked.connect(self.ejecutar_simulacion)
        h_controles.addWidget(btn_simular)

        layout.addLayout(h_controles)
        layout.addSpacing(10)

        # Tabla de resultados
        self.tabla_resultados = QTableWidget()
        self.tabla_resultados.setColumnCount(4)
        self.tabla_resultados.setHorizontalHeaderLabels(
            ["Día", "Pedidos", "Unidades", "SKU Popular"]
        )
        layout.addWidget(self.tabla_resultados)

        # Información resumen
        self.label_resumen = QLabel("Simulación no ejecutada")
        self.label_resumen.setStyleSheet("color: #666; font-style: italic;")
        layout.addWidget(self.label_resumen)

        # Botones de acción
        h_botones = QHBoxLayout()

        btn_guardar = QPushButton("💾 Guardar Simulación")
        btn_guardar.setFixedWidth(150)
        btn_guardar.clicked.connect(self.guardar_simulacion)

        btn_volver = QPushButton("◀ Volver")
        btn_volver.setFixedWidth(100)
        btn_volver.clicked.connect(self.ventana_principal.volver_menu)

        h_botones.addStretch()
        h_botones.addWidget(btn_guardar)
        h_botones.addWidget(btn_volver)
        layout.addLayout(h_botones)

    def ejecutar_simulacion(self):
        """Ejecuta la simulación de demanda"""
        n_dias = self.spin_dias.value()
        seed = self.spin_seed.value() if self.check_seed.isChecked() else None

        # Ejecutar simulación
        self.pedidos_simulados = simular_demanda(
            n_dias, dic_clientes, dic_sku, seed=seed
        )

        # Llenar tabla
        self.tabla_resultados.setRowCount(n_dias)
        total_unidades = 0
        total_pedidos = 0

        for dia in range(1, n_dias + 1):
            pedidos_dia = self.pedidos_simulados[dia]
            num_pedidos = len(pedidos_dia)
            unidades = contar_unidades_pedidos(pedidos_dia)
            sku_popular, _ = obtener_sku_mas_solicitado(pedidos_dia)

            total_unidades += unidades
            total_pedidos += num_pedidos

            self.tabla_resultados.setItem(dia - 1, 0, QTableWidgetItem(str(dia)))
            self.tabla_resultados.setItem(
                dia - 1, 1, QTableWidgetItem(str(num_pedidos))
            )
            self.tabla_resultados.setItem(dia - 1, 2, QTableWidgetItem(str(unidades)))
            self.tabla_resultados.setItem(
                dia - 1, 3, QTableWidgetItem(sku_popular or "N/A")
            )

        self.tabla_resultados.resizeColumnsToContents()

        # Actualizar resumen
        promedio_pedidos = total_pedidos / n_dias
        promedio_unidades = total_unidades / n_dias
        self.label_resumen.setText(
            f"✓ Simulación exitosa: {total_pedidos} pedidos, {total_unidades:,} unidades "
            f"(promedio: {promedio_pedidos:.1f} pedidos, {promedio_unidades:.0f} unidades/día)"
        )

    def guardar_simulacion(self):
        """Guarda la simulación (placeholder)"""
        if self.pedidos_simulados is None:
            QMessageBox.warning(
                self, "Advertencia", "Debe ejecutar una simulación primero"
            )
            return
        print("Guardando simulación...")
