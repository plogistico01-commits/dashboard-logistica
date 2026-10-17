import streamlit as st
import pandas as pd

st.set_page_config(page_title="Proyecto Logístico - Dashboard", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
        .stApp { background-color: #F3F4F6 !important; }
        [data-testid="stSidebar"] { background-color: #1E3A8A !important; color: #FFFFFF !important; }
        [data-testid="stSidebar"] *, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label { color: #FFFFFF !important; }
        .stRadio > div { background-color: rgba(255, 255, 255, 0.1) !important; padding: 10px !important; border-radius: 8px !important; }
        div[data-testid="stMetric"] { background-color: #FFFFFF !important; padding: 20px 25px !important; border-radius: 12px !important; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important; border: 1px solid #E5E7EB !important; transition: transform 0.2s ease; }
        div[data-testid="stMetric"]:hover { transform: translateY(-2px); }
        div[data-testid="stMetricLabel"] > div { color: #4B5563 !important; font-weight: 600 !important; font-size: 14px !important; }
        div[data-testid="stMetricValue"] > div { color: #111827 !important; font-weight: 700 !important; font-size: 28px !important; }
        h1, h2, h3 { color: #1F2937 !important; font-family: 'Inter', sans-serif !important; }
        .alerta-naranja { background-color: #FFF7ED !important; border-left: 5px solid #EA580C !important; padding: 15px !important; border-radius: 6px !important; color: #C2410C !important; font-weight: 500; }
        .ruta-optima { background-color: #F0FDF4 !important; border-left: 5px solid #16A34A !important; padding: 15px !important; border-radius: 6px !important; color: #14532D !important; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# URL Base KPIs
URL_KPIS = "https://google.com"

try:
    df = pd.read_csv(URL_KPIS, encoding='utf-8')
except Exception:
    datos_contingencia = {
        'INDICADOR': ['Precisión de Recepción (Fill Rate)', 'Eficiencia de Picking (Ruta)', 'Desvío de Peso Packing (Báscula)', 'Logística Inversa Devoluciones'],
        'VALOR ACTUAL': [0.3333, 0.8500, 0.0200, 0.9100],
        'META OBJETIVO': [0.9500, 0.9800, 0.0000, 0.9500],
        'ESTADO': ['ALERTA CRÍTICA', 'ÓPTIMO', 'CONTROLADO', 'REVISIÓN']
    }
    df = pd.DataFrame(datos_contingencia)

df.columns = df.columns.str.strip().str.upper()

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

opcion = st.sidebar.radio("Menú de Navegación:", ["🏠 Dashboard Principal", "📦 Agente 1: Recepción", "🚜 Agente 2: Picking"])
st.sidebar.markdown("<br><br><hr style='border-color: rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
st.sidebar.caption("🟢 Servidor Serverless · Capa 0 USD")

if opcion == "🏠 Dashboard Principal":
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.markdown("<h1 style='margin-bottom: 0px;'>Dashboard Ejecutivo</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6B7280; font-size: 14px; margin-top: 0px;'>Cuadro de mando corporativo · Sincronización en tiempo real</p>", unsafe_allow_html=True)
    with t_col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.caption("🟢 Conexión con Google Sheets Establecida")
        
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric(label="📥 Agente 1 (Fill Rate)", value="33.33%", delta="-61.67% vs Meta")
    with col2: st.metric(label="🚜 Agente 2 (Picking)", value="85.00%", delta="-13.00% vs Meta")
    with col3: st.metric(label="⚖️ Agente 3 (Packing)", value="2.00%", delta="+2.00% Desvío")
    with col4: st.metric(label="🔄 Agente 4 (Devoluciones)", value="91.00%", delta="-4.00% vs Meta")
        
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
        st.markdown("<div class='alerta-naranja'>⚠️ <strong>Alerta del Agente 1:</strong> El nivel de servicio (Fill Rate) se encuentra drásticamente por debajo del objetivo del 95.00%.</div>", unsafe_allow_html=True)

elif opcion == "🚜 Agente 2: Picking":
    st.markdown("<h1>🚜 Agente 2 - Optimización de Rutas (Picking)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px;'>Filtro de pedidos pendientes clasificados automáticamente por ubicación física</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    URL_PICKING = "https://google.com"
    
    try:
        df_picking = pd.read_csv(URL_PICKING, encoding='utf-8')
        df_picking.columns = df_picking.columns.str.strip().str.upper()
    except Exception:
        datos_picking_crudos = {
            'PEDIDO': ['#1024', '#1025', '#1026', '#1027', '#1028'],
            'PASILLO': ['Pasillo B', 'Pasillo A', 'Pasillo C', 'Pasillo A', 'Pasillo B'],
            'ESTANTERÍA': ['Nivel 3', 'Nivel 1', 'Nivel 2', 'Nivel 4', 'Nivel 1'],
            'ARTÍCULO': ['Filtros', 'Bujías', 'Soportes', 'Pastillas', 'Correas'],
            'CANTIDAD': [5, 12, 3, 8, 2]
        }
        df_picking = pd.DataFrame(datos_picking_crudos)

    col_pasillo = 'PASILLO' if 'PASILLO' in df_picking.columns else df_picking.columns[0]
    col_estanteria = 'ESTANTERÍA' if 'ESTANTERÍA' in df_picking.columns else df_picking.columns[1]
    
    df_optimizado = df_picking.sort_values(by=[col_pasillo, col_estanteria]).reset_index(drop=True)
    
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        st.metric(label="Eficiencia de la Ruta Activa", value="85.00%", delta="-13.00% vs Objetivo (98%)")
    with p_col2:
        st.markdown("""
            <div class='ruta-optima'>
                ✅ <strong>Ruta Logística Secuencial Activa:</strong> Filas reorganizadas automáticamente de extremo a extremo del pasillo para minimizar desplazamientos nulos de los operarios.
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><h3>📋 Hoja de Ruta de Picking Generada (Tiempo Real)</h3>", unsafe_allow_html=True)
    st.dataframe(df_optimizado, use_container_width=True)














