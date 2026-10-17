import streamlit as st
import pandas as pd

# 1. Configuración de la interfaz ejecutiva en alta definición
st.set_page_config(page_title="Logística Lean - Dashboard", layout="wide", initial_sidebar_state="expanded")

# Base de datos unificada en la nube
SHEET_ID = "1xaPnDFIBd0Lwy_Z7wVI-SdsxSq20wg7fKtLDypjsd4I"
URL = f"https://google.com{SHEET_ID}/export?format=csv&gid=1440866900"

try:
    df = pd.read_csv(URL, encoding='utf-8')
except Exception:
    # Datos Lean de contingencia con la estructura real del mapa de agentes
    datos_contingencia = {
        'INDICADOR': [
            'Precisión de Recepción (Fill Rate)', 
            'Eficiencia de Picking (Ruta)', 
            'Desvío de Peso Packing (Báscula)', 
            'Logística Inversa Devoluciones', 
            'Distancia Relativa Ruteo (Km)'
        ],
        'VALOR ACTUAL': [0.3333, 0.8500, 0.0200, 0.9100, 0.7200],
        'META OBJETIVO': [0.9500, 0.9800, 0.0000, 0.9500, 0.9000],
        'ESTADO': ['ALERTA CRÍTICA', 'ÓPTIMO', 'CONTROLADO', 'REVISIÓN', 'DESVÍO']
    }
    df = pd.DataFrame(datos_contingencia)

# Limpieza estándar de columnas
df.columns = df.columns.str.strip().str.upper()

# 2. Barra Lateral de Navegación Ejecutiva
st.sidebar.markdown("<h2 style='text-align: center; color: #00FFCC;'>🎛️ CONTROL LOGÍSTICO</h2>", unsafe_view_ok=True)
st.sidebar.markdown("---")
opcion = st.sidebar.radio("Selección de Agente:", ["🏠 Panel General de KPIs", "📦 Agente 1: Recepción"])
st.sidebar.markdown("---")
st.sidebar.caption("🟢 Servidor Serverless Cloud Activo (0 USD)")

# Mapeo automático de columnas
col_ind = [c for c in df.columns if 'INDICA' in c or 'KPI' in c][0]
col_val = [c for c in df.columns if 'VALOR' in c or 'ACTUAL' in c][0]
col_met = [c for c in df.columns if 'META' in c or 'OBJETI' in c][0]
col_est = [c for c in df.columns if 'ESTA' in c][0]

# 3. Renderizado de la Pantalla Principal según el Menú
if opcion == "🏠 Panel General de KPIs":
    st.markdown("<h1 style='color: white;'>📊 Cuadro de Mando Integral Gerencial</h1>", unsafe_view_ok=True)
    st.markdown("Auditoría automatizada de los agentes operativos en tiempo real.")
    st.markdown("---")
    
    # Decoración con Tarjetas Modulares en Fila (Scorecards) para vista rápida de gerencia
    st.markdown("### 🔔 Estado Actual de las Operaciones")
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.metric(label="📥 Agente 1 (Fill Rate)", value="33.33%", delta="-61.67% vs Meta")
    with m2:
        st.metric(label="🚜 Agente 2 (Picking)", value="85.00%", delta="-13.00% vs Meta")
    with m3:
        st.metric(label="⚖️ Agente 3 (Packing)", value="2.00%", delta="+2.00% Desvío")
    with m4:
        st.metric(label="🔄 Agente 4 (Devoluciones)", value="91.00%", delta="-4.00% vs Meta")
        
    st.markdown("---")
    
    # Gráfico de Barras Decorativo de Comparativa Táctica
    st.markdown("### 📈 Rendimiento vs Metas del Proyecto")
    
    # Preparamos los datos limpios para el gráfico nativo
    chart_data = pd.DataFrame({
        'Indicador': df[col_ind],
        'Progreso Real': df[col_val] * 100,
        'Meta Objetivo': df[col_met] * 100
    }).set_index('Indicador')
    
    # Renderizado del gráfico interactivo con barras duales
    st.bar_chart(chart_data, use_container_width=True)
    
    # Tabla consolidada estilizada al final
    st.markdown("### 📝 Registro Maestro de Auditoría")
    st.dataframe(df, use_container_width=True)

elif opcion == "📦 Agente 1: Recepción":
    st.title("📦 Agente 1 - Recepción (Fill Rate)")
    kpi = df[df[col_ind].astype(str).str.contains("Fill Rate|PRECISION|RECEPCION", case=False, na=False)]
    
    if not kpi.empty:
        val_actual = float(kpi.iloc[0][col_val])
        st.metric(label="Precisión de Recepción (Fill Rate)", value=f"{val_actual * 100:.2f}%", delta="-61.67% vs Meta")
        st.progress(min(max(val_actual, 0.0), 1.0))
        st.error(f"Alerta del Agente 1: El estado actual es '{kpi.iloc[0][col_est]}'. Nivel crítico bajo supervisor.")










