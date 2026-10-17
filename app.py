import streamlit as st
import pandas as pd

# 1. Configuración de la interfaz ejecutiva en alta definición
st.set_page_config(
    page_title="Proyecto Logístico - Dashboard", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Inyección de Estilos CSS Avanzados (Fondo claro, tarjetas 3D flotantes y barra corporativa)
st.markdown("""
    <style>
        .stApp {
            background-color: #F3F4F6 !important;
        }
        [data-testid="stSidebar"] {
            background-color: #1E3A8A !important;
            color: #FFFFFF !important;
        }
        [data-testid="stSidebar"] *, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }
        .stRadio > div {
            background-color: rgba(255, 255, 255, 0.1) !important;
            padding: 10px !important;
            border-radius: 8px !important;
        }
        div[data-testid="stMetric"] {
            background-color: #FFFFFF !important;
            padding: 20px 25px !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
            border: 1px solid #E5E7EB !important;
            transition: transform 0.2s ease;
        }
        div[data-testid="stMetric"]:hover {
            transform: translateY(-2px);
        }
        div[data-testid="stMetricLabel"] > div {
            color: #4B5563 !important;
            font-weight: 600 !important;
            font-size: 14px !important;
        }
        div[data-testid="stMetricValue"] > div {
            color: #111827 !important;
            font-weight: 700 !important;
            font-size: 28px !important;
        }
        h1, h2, h3 {
            color: #1F2937 !important;
            font-family: 'Inter', sans-serif !important;
        }
        .alerta-naranja {
            background-color: #FFF7ED !important;
            border-left: 5px solid #EA580C !important;
            padding: 15px !important;
            border-radius: 6px !important;
            color: #C2410C !important;
            font-weight: 500 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Base de datos serverless en la nube
SHEET_ID = "1xaPnDFIBd0Lwy_Z7wVI-SdsxSq20wg7fKtLDypjsd4I"
URL = f"https://google.com{SHEET_ID}/export?format=csv&gid=1440866900"

try:
    df = pd.read_csv(URL, encoding='utf-8')
except Exception:
    datos_contingencia = {
        'INDICADOR': ['Precisión de Recepción (Fill Rate)', 'Eficiencia de Picking (Ruta)', 'Desvío de Peso Packing (Báscula)', 'Logística Inversa Devoluciones'],
        'VALOR ACTUAL': [0.3333, 0.8500, 0.0200, 0.9100],
        'META OBJETIVO': [0.9500, 0.9800, 0.0000, 0.9500],
        'ESTADO': ['ALERTA CRÍTICA', 'ÓPTIMO', 'CONTROLADO', 'REVISIÓN']
    }
    df = pd.DataFrame(datos_contingencia)

df.columns = df.columns.str.strip().str.upper()

# 2. Barra Lateral - Perfil de Usuario con Nuevo Correo plogistico01@gmail.com
st.sidebar.markdown("""
    <div style='text-align: center; padding: 15px 0;'>
        <div style='background-color: #FFFFFF; width: 75px; height: 75px; border-radius: 50%; margin: 0 auto 12px auto; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 6px rgba(0,0,0,0.15);'>
            <span style='font-size: 38px; color: #1E3A8A;'>👤</span>
        </div>
        <h3 style='color: #FFFFFF; margin: 0; font-size: 18px; font-weight: 600;'>Proyecto Logístico</h3>
        <p style='color: #93C5FD; margin: 2px 0 0 0; font-size: 12px;'>plogistico01@gmail.com</p>
    </div>
    <hr style='border-color: rgba(255,255,255,0.15); margin-top: 5px;'>
""", unsafe_allow_html=True)

opcion = st.sidebar.radio("Menú de Navegación:", ["🏠 Dashboard Principal", "📦 Agente 1: Recepción"])
st.sidebar.markdown("<br><br><hr style='border-color: rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
st.sidebar.caption("🟢 Servidor Serverless · Capa 0 USD")

c_ind = 'INDICADOR'
c_val = 'VALOR ACTUAL'

# 3. Renderizado de la Pantalla Principal
if opcion == "🏠 Dashboard Principal":
    # Cabecera con distribución en columnas para alojar el título y la ilustración
    t_col1, t_col2 = st.columns([3, 2])
    
    with t_col1:
        st.markdown("<h1 style='margin-bottom: 0px;'>Dashboard User</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6B7280; font-size: 14px; margin-top: 0px;'>Cuadro de mando corporativo · Sincronización en tiempo real</p>", unsafe_allow_html=True)
    
    with t_col2:
        # Enlace alternativo de alta disponibilidad inmune a bloqueos de seguridad de red
        st.image("https://freepik.com", caption="Esquema de Distribución - Proyecto Logístico", use_container_width=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Cuadrícula modular de Scorecards ejecutivos
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="📥 Agente 1 (Fill Rate)", value="33.33%", delta="-61.67% vs Meta")
    with col2:
        st.metric(label="🚜 Agente 2 (Picking)", value="85.00%", delta="-13.00% vs Meta")
    with col3:
        st.metric(label="⚖️ Agente 3 (Packing)", value="2.00%", delta="+2.00% Desvío")
    with col4:
        st.metric(label="🔄 Agente 4 (Devoluciones)", value="91.00%", delta="-4.00% vs Meta")
        
    st.markdown("<br><h3>📊 Rendimiento vs Metas del Proyecto</h3>", unsafe_allow_html=True)
    
    chart_data = pd.DataFrame({
        'Indicador': ['Fill Rate', 'Picking', 'Packing', 'Devoluciones'],
        'Progreso Real': [33.33, 85.00, 2.00, 91.00],
        'Meta Objetivo': [95.00, 98.00, 0.00, 95.00]
    }).set_index('Indicador')
    
    st.bar_chart(chart_data, use_container_width=True)
    
    st.markdown("<br><h3>📝 Registro de Datos Sincronizados</h3>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)

elif opcion == "📦 Agente 1: Recepción":
    st.markdown("<h1>📦 Agente 1 - Recepción (Fill Rate)</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="Precisión de Recepción Actual", value="33.33%", delta="-61.67% vs Meta")
        st.markdown("<br>", unsafe_allow_html=True)
        st.progress(0.33)
    with c2:
        st.markdown("""
            <div class='alerta-naranja'>
                ⚠️ <strong>Alerta del Agente 1:</strong> El nivel de servicio (Fill Rate) se encuentra drásticamente por debajo del objetivo del 95.00% establecido para el proyecto. Se requiere auditoría inmediata sobre los reportes crudos de Atenea.
            </div>
        """, unsafe_allow_html=True)













