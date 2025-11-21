#!/usr/bin/env python3
"""
quick_start.py - Inicio rápido del sistema de simulación logística

Este script ejecuta una simulación básica de 3 días y muestra los resultados.
"""

import sys
import os
from pathlib import Path

# Agregar el directorio del sistema al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sistema.catalogos import dic_sku, dic_clientes, dic_vehiculos, distancias_km
from sistema.demanda import simular_demanda, contar_unidades_pedidos, obtener_sku_mas_solicitado
from sistema.inventario import inicializar_stock, reservar_y_actualizar, reponer_simple
from sistema.picking import asignar_picking
from sistema.transporte import planificar_rutas
from sistema.indicadores import calcular_indicadores, consolidar_indicadores_multiples_dias
from sistema.alertas import generar_alertas, generar_recomendaciones
from sistema.reporte import reporte_logistica, formatear_reporte_texto


def main():
    """Ejecuta una simulación rápida del sistema"""
    
    print("\n" + "=" * 70)
    print("🚚 SISTEMA DE SIMULACIÓN LOGÍSTICA - INICIO RÁPIDO")
    print("   Andes Logistics S.A. / Ferreyros")
    print("=" * 70 + "\n")
    
    # Configuración
    N_DIAS = 3
    SEED = 42
    CAPACIDAD_PICKING = 1500
    HORAS_JORNADA = 8
    PUNTO_REORDEN = 50
    LOTE_REPOSICION = 100
    STOCK_INICIAL = 200
    
    print(f"📋 Configuración:")
    print(f"   - Días a simular: {N_DIAS}")
    print(f"   - Seed: {SEED}")
    print(f"   - Capacidad picking: {CAPACIDAD_PICKING} unidades")
    print(f"   - Stock inicial: {STOCK_INICIAL} unidades/SKU\n")
    
    # 1. Simular demanda
    print("1️⃣  Simulando demanda...")
    pedidos = simular_demanda(N_DIAS, dic_clientes, dic_sku, seed=SEED)
    total_pedidos = sum(len(pedidos[dia]) for dia in range(1, N_DIAS + 1))
    total_unidades = sum(contar_unidades_pedidos(pedidos[dia]) for dia in range(1, N_DIAS + 1))
    print(f"    ✓ {total_pedidos} pedidos generados, {total_unidades:,} unidades solicitadas\n")
    
    # 2. Gestionar inventario
    print("2️⃣  Gestionando inventario...")
    stock = inicializar_stock(dic_sku, STOCK_INICIAL)
    unidades_entregadas_total = 0
    unidades_no_entregadas_total = 0
    
    for dia in range(1, N_DIAS + 1):
        stock, entregadas, no_entregadas, _ = reservar_y_actualizar(
            stock, pedidos[dia], dic_clientes
        )
        stock, _ = reponer_simple(stock, dic_sku, PUNTO_REORDEN, LOTE_REPOSICION)
        unidades_entregadas_total += entregadas
        unidades_no_entregadas_total += no_entregadas
    
    print(f"    ✓ {unidades_entregadas_total:,} unidades entregadas")
    print(f"    ✓ {unidades_no_entregadas_total:,} unidades no entregadas\n")
    
    # 3. Picking y transporte
    print("3️⃣  Ejecutando operaciones de picking y transporte...")
    lista_indicadores = []
    
    for dia in range(1, N_DIAS + 1):
        picking = asignar_picking(dia, pedidos[dia], CAPACIDAD_PICKING)
        rutas = planificar_rutas(dia, picking['preparados'], dic_vehiculos, distancias_km, dic_clientes)
        
        indicadores = calcular_indicadores(
            len(pedidos[dia]),
            rutas['unidades_transportadas'],
            contar_unidades_pedidos(pedidos[dia]),
            picking['unidades_preparadas'],
            rutas['unidades_transportadas'],
            picking['unidades_pendientes'],
            rutas['utilizacion_promedio'],
            HORAS_JORNADA
        )
        
        lista_indicadores.append(indicadores)
    
    print(f"    ✓ Picking: {sum(i['unidades_preparadas'] for i in lista_indicadores):,} unidades")
    print(f"    ✓ Transporte: {sum(i['unidades_entregadas'] for i in lista_indicadores):,} unidades\n")
    
    # 4. Consolidar indicadores
    print("4️⃣  Consolidando indicadores...")
    indicadores_consolidados = consolidar_indicadores_multiples_dias(lista_indicadores)
    print(f"    ✓ OTIF promedio: {indicadores_consolidados['otif_promedio']:.2f}%")
    print(f"    ✓ Fill Rate promedio: {indicadores_consolidados['fill_rate_promedio']:.2f}%")
    print(f"    ✓ Backlog: {indicadores_consolidados['backlog_rate_promedio']:.2f}%\n")
    
    # 5. Generar alertas
    print("5️⃣  Generando alertas automáticas...")
    alertas = generar_alertas(indicadores_consolidados)
    print(f"    ✓ {len(alertas)} alertas detectadas\n")
    
    # 6. Generar reporte
    print("6️⃣  Generando reporte final...")
    recomendaciones = generar_recomendaciones(alertas, indicadores_consolidados)
    reporte = reporte_logistica(
        total_pedidos,
        total_unidades,
        unidades_entregadas_total,
        indicadores_consolidados,
        alertas,
        recomendaciones
    )
    
    # Mostrar reporte
    texto_reporte = formatear_reporte_texto(reporte)
    print("\n" + texto_reporte)
    
    # Guardar archivos
    print("\n7️⃣  Guardando archivos...")
    
    # Crear carpeta data si no existe
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)
    
    with open(data_dir / "reporte_final.txt", 'w', encoding='utf-8') as f:
        f.write(texto_reporte)
    print(f"    ✓ Reporte guardado en: data/reporte_final.txt")
    
    print("\n✅ Simulación completada exitosamente!\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error durante la simulación: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
