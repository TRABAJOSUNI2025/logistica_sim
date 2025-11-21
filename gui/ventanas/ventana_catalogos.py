"""
ventana_catalogos.py - Pantalla de gestión de catálogos
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                            QTableWidget, QTableWidgetItem, QTabWidget, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from sistema.catalogos import dic_sku, dic_clientes, dic_vehiculos


class VentanaCatalogos(QWidget):
    """Pantalla para visualizar catálogos"""
    
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
        titulo = QLabel("GESTIÓN DE CATÁLOGOS")
        titulo_font = QFont("Arial", 18, QFont.Weight.Bold)
        titulo.setFont(titulo_font)
        layout.addWidget(titulo)
        
        # Tabs para diferentes catálogos
        tabs = QTabWidget()
        
        # Tab SKUs
        tab_skus = self.crear_tab_skus()
        tabs.addTab(tab_skus, "SKUs")
        
        # Tab Clientes
        tab_clientes = self.crear_tab_clientes()
        tabs.addTab(tab_clientes, "Clientes")
        
        # Tab Vehículos
        tab_vehiculos = self.crear_tab_vehiculos()
        tabs.addTab(tab_vehiculos, "Vehículos")
        
        layout.addWidget(tabs)
        
        # Botones de acción
        h_botones = QHBoxLayout()
        
        btn_exportar = QPushButton("📥 Exportar CSV")
        btn_exportar.setFixedWidth(150)
        btn_exportar.clicked.connect(self.exportar_catalogos)
        
        btn_volver = QPushButton("◀ Volver")
        btn_volver.setFixedWidth(100)
        btn_volver.clicked.connect(self.ventana_principal.volver_menu)
        
        h_botones.addStretch()
        h_botones.addWidget(btn_exportar)
        h_botones.addWidget(btn_volver)
        layout.addLayout(h_botones)
    
    def crear_tab_skus(self):
        """Crea el tab de SKUs"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        tabla = QTableWidget()
        tabla.setColumnCount(2)
        tabla.setHorizontalHeaderLabels(["Código SKU", "Descripción"])
        tabla.setRowCount(len(dic_sku))
        
        for i, (sku, desc) in enumerate(dic_sku.items()):
            tabla.setItem(i, 0, QTableWidgetItem(sku))
            tabla.setItem(i, 1, QTableWidgetItem(desc))
        
        tabla.resizeColumnsToContents()
        layout.addWidget(tabla)
        
        return widget
    
    def crear_tab_clientes(self):
        """Crea el tab de clientes"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        tabla = QTableWidget()
        tabla.setColumnCount(2)
        tabla.setHorizontalHeaderLabels(["Código Cliente", "Nombre"])
        tabla.setRowCount(len(dic_clientes))
        
        for i, (cid, nombre) in enumerate(dic_clientes.items()):
            tabla.setItem(i, 0, QTableWidgetItem(cid))
            tabla.setItem(i, 1, QTableWidgetItem(nombre))
        
        tabla.resizeColumnsToContents()
        layout.addWidget(tabla)
        
        return widget
    
    def crear_tab_vehiculos(self):
        """Crea el tab de vehículos"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        tabla = QTableWidget()
        tabla.setColumnCount(4)
        tabla.setHorizontalHeaderLabels(["Código", "Tipo", "Capacidad", "Costo/km"])
        tabla.setRowCount(len(dic_vehiculos))
        
        for i, (vid, info) in enumerate(dic_vehiculos.items()):
            tabla.setItem(i, 0, QTableWidgetItem(vid))
            tabla.setItem(i, 1, QTableWidgetItem(info["tipo"]))
            tabla.setItem(i, 2, QTableWidgetItem(str(info["capacidad"])))
            tabla.setItem(i, 3, QTableWidgetItem(f"S/. {info['costo_km']:.2f}"))
        
        tabla.resizeColumnsToContents()
        layout.addWidget(tabla)
        
        return widget
    
    def exportar_catalogos(self):
        """Exporta los catálogos a CSV (placeholder)"""
        print("Exportación de catálogos en desarrollo...")
