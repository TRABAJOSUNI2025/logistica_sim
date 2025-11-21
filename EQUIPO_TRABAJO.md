# 👥 DIVISIÓN DE TRABAJO - EQUIPO DE 5 INTEGRANTES

## 📊 Asignación de Responsabilidades

Sistema de Simulación Logística Ferreyros - Mantenimiento y Mejora Continua

---

## 👨‍💼 **INTEGRANTE 1: CRISTHIAN FLORES**
### Rol: **Arquitecto Backend & Configuración**

#### 📁 Archivos a Revisar:
- `config.py` - Configuración centralizada
- `sistema/__init__.py` - Exportación módulos
- `requirements.txt` - Dependencias
- `README.md` - Documentación técnica

#### 🔗 Conexiones (comunica con):
- **Integrante 2** (demanda) - Parámetros de demanda
- **Integrante 3** (picking/transporte) - Capacidades
- **Integrante 5** (GUI/validación) - Dependencias

#### ✅ Responsabilidades:
- Mantener coherencia de parámetros
- Validar versiones de dependencias
- Revisar imports y exportaciones
- Documentar cambios en config.py

#### 🔍 Errores a Buscar:
- Parámetros inconsistentes
- Versiones desactualizadas
- Imports circulares
- Configuraciones conflictivas

---

## 📊 **INTEGRANTE 2: ALEX RAMÍREZ**
### Rol: **Especialista Backend - Demanda & Datos**

#### 📁 Archivos a Revisar:
- `sistema/demanda.py` - Generación de demanda
- `sistema/catalogos.py` - SKUs, clientes, vehículos
- `sistema/indicadores.py` - Cálculo de KPIs
- `quick_start.py` - Script simulación

#### 🔗 Conexiones (comunica con):
- **Integrante 1** (config) - Parámetros demanda
- **Integrante 3** (inventario/picking) - Pedidos generados
- **Integrante 4** (reportes) - Datos consolidados

#### ✅ Responsabilidades:
- Validar lógica de demanda
- Revisar cálculos de KPIs
- Verificar consistencia de catálogos
- Probar script quick_start

#### 🔍 Errores a Buscar:
- Demanda fuera de rangos
- KPIs mal calculados
- SKUs/clientes duplicados
- Seeds inconsistentes

---

## 🚚 **INTEGRANTE 3: MARIA SANTOS**
### Rol: **Especialista Backend - Logística Operativa**

#### 📁 Archivos a Revisar:
- `sistema/inventario.py` - Gestión stock
- `sistema/picking.py` - Asignación pedidos
- `sistema/transporte.py` - Rutas y vehículos
- `sistema/alertas.py` - Sistema de alertas

#### 🔗 Conexiones (comunica con):
- **Integrante 1** (config) - Capacidades
- **Integrante 2** (demanda) - Pedidos
- **Integrante 4** (reportes) - Datos alertas

#### ✅ Responsabilidades:
- Validar lógica de inventario
- Revisar asignación de picking
- Verificar rutas optimizadas
- Probar sistema de alertas

#### 🔍 Errores a Buscar:
- Stock negativo
- Picking sobre capacidad
- Rutas ineficientes
- Alertas no disparadas

---

## 📋 **INTEGRANTE 4: CARLOS MENDEZ**
### Rol: **Especialista Backend - Reportes & Análisis**

#### 📁 Archivos a Revisar:
- `sistema/reporte.py` - Generación reportes
- `simulador.ipynb` - Notebook análisis
- Exportación TXT/CSV/JSON
- `instalar_y_probar.py` - Validación

#### 🔗 Conexiones (comunica con):
- **Integrante 2** (KPIs) - Datos para reportes
- **Integrante 3** (alertas) - Datos alertas
- **Integrante 5** (GUI) - Visualización datos

#### ✅ Responsabilidades:
- Validar formatos de reportes
- Revisar notebook funcionando
- Probar exportación de datos
- Ejecutar validaciones

#### 🔍 Errores a Buscar:
- Reportes incompletos
- Formatos corrupto
- Datos no exportados
- Validaciones fallidas

---

## 🖥️ **INTEGRANTE 5: PATRICIA COHEN**
### Rol: **Especialista Frontend & Integración**

#### 📁 Archivos a Revisar:
- `INICIO.py` - Menú principal
- `gui/main.py` - Punto entrada GUI
- `gui/recursos_manager.py` - Gestor recursos
- Todas las ventanas:
  - `gui/ventanas/ventana_principal.py`
  - `gui/ventanas/ventana_catalogos.py`
  - `gui/ventanas/ventana_simulacion.py`
  - `gui/ventanas/ventana_indicadores.py`
  - `gui/ventanas/ventana_reporte.py`

#### 🔗 Conexiones (comunica con):
- **Integrante 1** (config) - Parámetros UI
- **Integrante 4** (reportes) - Datos mostrar
- Todo el equipo (testing final)

#### ✅ Responsabilidades:
- Validar interfaz gráfica
- Revisar navegación entre ventanas
- Probar carga de estilos
- Verificar integración completa

#### 🔍 Errores a Buscar:
- Botones que no funcionan
- Ventanas no abren
- Estilos no aplican
- Datos no se actualizan

---

## 🔄 FLUJO DE COMUNICACIÓN

```
┌─────────────────────────────────────────────────────┐
│         INTEGRANTE 1: ARQUITECTO BACKEND             │
│              (config.py, validación)                  │
└────────────┬────────────────────────────┬────────────┘
             │                            │
    ┌────────▼─────────┐        ┌─────────▼────────┐
    │ INTEGRANTE 2      │        │ INTEGRANTE 3     │
    │ Demanda & Datos   │        │ Logística        │
    │ (demanda, KPI)    │        │ (inventario,     │
    │                   │        │  picking,        │
    │ + Integrante 4    │        │  transporte,     │
    │                   │        │  alertas)        │
    └────────┬──────────┘        └────────┬─────────┘
             │                            │
             └───────────┬────────────────┘
                        │
                 ┌──────▼──────┐
                 │ INTEGRANTE 4 │
                 │ Reportes     │
                 │ Análisis     │
                 └──────┬───────┘
                        │
                 ┌──────▼──────────┐
                 │ INTEGRANTE 5    │
                 │ GUI & Testing   │
                 │ (Integración)   │
                 └─────────────────┘
```

---

## 📝 MATRIZ DE RESPONSABILIDADES

| Archivo | Responsable | Revisores |
|---------|-------------|-----------|
| `config.py` | #1 | #2, #3, #5 |
| `sistema/demanda.py` | #2 | #1, #3, #4 |
| `sistema/catalogos.py` | #2 | #1, #3 |
| `sistema/inventario.py` | #3 | #1, #2, #4 |
| `sistema/picking.py` | #3 | #1, #2, #4 |
| `sistema/transporte.py` | #3 | #1, #2, #4 |
| `sistema/indicadores.py` | #2 | #1, #4 |
| `sistema/alertas.py` | #3 | #1, #2, #4 |
| `sistema/reporte.py` | #4 | #2, #3, #5 |
| `quick_start.py` | #2 | #1, #4, #5 |
| `simulador.ipynb` | #4 | #2, #3 |
| `INICIO.py` | #5 | #1, #4 |
| `gui/main.py` | #5 | #1 |
| `gui/ventanas/*` | #5 | #1, #4 |
| `instalar_y_probar.py` | #4 | #1, #5 |

---

## 🎯 CICLO DE REVISIÓN

### **Fase 1: Revisión Individual (2 horas)**
Cada integrante revisa sus archivos:
- ✓ Código limpio
- ✓ Sin errores sintácticos
- ✓ Lógica correcta
- ✓ Documentación actualizada

### **Fase 2: Pruebas Locales (1.5 horas)**
Cada integrante prueba:
- Módulo funcionando aislado
- Integración con dependencias
- Manejo de errores

### **Fase 3: Revisión Cruzada (1 hora)**
- #1 revisa trabajo de #2 y #3
- #2 valida con #1 y #4
- #3 coordina con #1 y #2
- #4 valida reportes con #2, #3
- #5 prueba GUI con todos

### **Fase 4: Testing Integrado (1.5 horas)**
Ejecutar en conjunto:
```bash
python INICIO.py              # Menú
python quick_start.py         # Simulación
python gui/main.py            # GUI
jupyter notebook simulador.ipynb  # Análisis
```

---

## 📋 CHECKLIST DE REVISIÓN

### **Cada Integrante Verifica:**

- [ ] Código sin errores sintácticos
- [ ] Importaciones correctas
- [ ] Funciones documentadas
- [ ] Manejo de errores
- [ ] Parámetros válidos
- [ ] Tests pasando
- [ ] Conecta con otros módulos

### **Coordinador Final (#1):**

- [ ] Configuración consistente
- [ ] No hay conflictos de parámetros
- [ ] Dependencias actualizadas
- [ ] Sistema completo funciona
- [ ] Documentación coherente

---

## 💬 REUNIONES SINCRONIZACIÓN

| Momento | Participantes | Duración | Objetivo |
|---------|--------------|----------|----------|
| Inicio sprint | Todos | 15 min | Asignaciones |
| Fin Phase 2 | #1-5 | 20 min | Validar pruebas |
| Fin Phase 3 | #1,2,3,4,5 | 15 min | Revisar cruzada |
| Fin Phase 4 | Todos | 20 min | Integración final |

---

## 📞 PROTOCOLO DE COMUNICACIÓN

**Cuando encuentres un error:**

1. **Documenta el error:** Archivo, línea, descripción
2. **Identifica impacto:** ¿Afecta a otros módulos?
3. **Comunica:** A integrantes conectados
4. **Propón solución:** Draft de fix
5. **Revisa juntos:** Confirma que no quiebra otras cosas

**Ejemplo:**
```
De: #3 (Logística)
Para: #1 (Arquitecto), #2 (Demanda)
Asunto: Error en inventario.py línea 45

El stock se vuelve negativo cuando demanda > disponible.
Necesita revisar: parámetro PUNTO_REORDEN en config.py
Propongo: Usar max(stock - demanda, 0)
¿Afecta a demanda.py? Revisar con #2
```

---

## ✅ RESPONSABILIDADES FINALES

**TODOS** son responsables de:
- Código limpio y documentado
- Testing en su sección
- Comunicar cambios
- No romper lo de otros

**CRISTHIAN (#1)** además:
- Validar coherencia global
- Resolver conflictos
- Dar OK final

---

## 📊 MÉTRICAS DE CALIDAD

Cada integrante debe lograr:
- ✅ 0 errores sintácticos
- ✅ 100% documentación
- ✅ 100% funcionalidad probada
- ✅ Integración sin conflictos

---

## 🚀 PRÓXIMOS PASOS

1. Cada integrante estudia sus archivos
2. Sincronización inicial (15 min)
3. Revisión individual (2 horas)
4. Pruebas locales (1.5 horas)
5. Revisión cruzada (1 hora)
6. Testing integrado (1.5 horas)
7. ✅ Sistema listo para producción

---

**¡Equipo de 5, uniendo fuerzas para la excelencia! 💪**

Duración estimada: **~7.5 horas** para ciclo completo

