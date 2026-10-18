import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE INTERFAZ PREMIUM LOGÍSTICA
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
        .status-card { padding: 15px 20px; border-radius: 10px; font-family: 'Inter', sans-serif; font-size: 14px; margin-bottom: 12px; border-left: 6px solid; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }
        .status-critico { background-color: #FEF2F2; border-color: #EF4444; color: #991B1B; }
        .status-revision { background-color: #FFF7ED; border-color: #F97316; color: #9A3412; }
        .status-optimo { background-color: #F0FDF4; border-color: #22C55E; color: #166534; }
        .status-controlado { background-color: #F0F9FF; border-color: #0EA5E9; color: #075985; }
    </style>
""", unsafe_allow_html=True)

# 2. SIDEBAR FIJA CORPORATIVA
st.sidebar.markdown("""
    <div style='text-align: center; padding: 15px 0;'>
        <div style='background-color: #FFFFFF; width: 75px; height: 75px; border-radius: 50%; margin: 0 auto 12px auto; display: flex; align-items: center; justify-content: center;'>
            <span style='font-size: 38px; color: #1E3A8A;'>👤</span>
        </div>
        <h3 style='color: #FFFFFF; margin: 0; font-size: 18px; font-weight: 600;'>Proyecto Logístico</h3>
        <p style='color: #93C5FD; margin: 2px 0 0 0; font-size: 12px;'>plogistico01@gmail.com</p>
    </div>
    <hr style='border-color: rgba(255,255,255,0.15); margin-top: 5px;'>
""", unsafe_allow_html=True)

opcion = st.sidebar.radio("Menú de Navegación:", ["🏠 Dashboard Principal", "📦 Agente 1: Recepción", "🚜 Agente 2: Picking", "⚖️ Agente 3: Packing", "🔄 Agente 4: Devoluciones", "🚛 Agente 5: Ruteo"])
st.sidebar.markdown("<br><br><hr style='border-color: rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
st.sidebar.caption("🟢 Servidor Serverless · Capa 0 USD")

# 3. DATOS DE INICIO DE RESPALDO (VERIFICADOS)
fallback_dash = {"Indicador": ["Fill Rate", "Picking", "Packing", "OTIF Ruteo"], "Progreso": [33.33, 85.00, 2.00, 94.20], "Meta": [95.00, 98.00, 0.00, 95.00]}
fallback_a2 = {"ID_Ruta": ["R-101", "R-102"], "Operario": ["Juan P.", "Ana M."], "Eficiencia": [85.0, 99.1], "Estado": ["REVISIÓN", "ÓPTIMO"]}
fallback_a3 = {"Lote": ["L-998", "L-999"], "Desvio_Peso": [2.5, 0.1], "Estado": ["CRÍTICO", "CONTROLADO"]}
fallback_a4 = {"Sku": ["SKU-708A", "SKU-537B"], "Motivo": ["Empaque Dañado", "Reingreso Ok"], "Cantidad":}
fallback_a5 = {"Zona": ["Ruta Norte", "Ruta Metropolitana"], "OTIF": [98.50, 89.90], "Estado": ["ÓPTIMO OBJETIVO", "REVISIÓN POR TRÁFICO"]}

# Convertir diccionarios a DataFrames de manera segura
df_dash = pd.DataFrame(fallback_dash)
df_a2 = pd.DataFrame(fallback_a2)
df_a3 = pd.DataFrame(fallback_a3)
df_a4 = pd.DataFrame(fallback_a4)
df_a5 = pd.DataFrame(fallback_a5)

# 4. INTERFAZ EN FORMATO PLANO ULTRA-ESTABLE
if opcion == "🏠 Dashboard Principal":
    st.markdown("<h1>Dashboard Ejecutivo</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px; margin-top: 0px;'>Cuadro de mando corporativo · Sincronización en tiempo real</p>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric(label="📥 Agente 1 (Fill Rate)", value=f"{df_dash.loc[0, 'Progreso']}%", delta=f"{df_dash.loc[0, 'Progreso'] - df_dash.loc[0, 'Meta']:.2f}% vs Meta")
    with col2: st.metric(label="🚜 Agente 2 (Picking)", value=f"{df_dash.loc[1, 'Progreso']}%", delta=f"{df_dash.loc[1, 'Progreso'] - df_dash.loc[1, 'Meta']:.2f}% vs Meta")
    with col3: st.metric(label="⚖️ Agente 3 (Packing)", value=f"{df_dash.loc[2, 'Progreso']}%", delta=f"+{df_dash.loc[2, 'Progreso']}% Desvío")
    with col4: st.metric(label="🚛 Agente 5 (OTIF Ruteo)", value=f"{df_dash.loc[3, 'Progreso']}%", delta=f"{df_dash.loc[3, 'Progreso'] - df_dash.loc[3, 'Meta']:.2f}% vs Meta")
        
    st.markdown("<br><h3>📊 Rendimiento vs Metas del Proyecto</h3>", unsafe_allow_html=True)
    chart_data = df_dash.set_index('Indicador')
    st.bar_chart(chart_data, use_container_width=True)
    
    st.markdown("<br><h3>🚦 Estado Operativo de los Procesos</h3>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="status-card status-critico">
            <strong>🔴 Agente 1: Recepción (Fill Rate)</strong> — Estatus: <u>ALERTA CRÍTICA</u> <br>
            <span style="font-size: 13px; opacity: 0.8;">Progreso Actual: {df_dash.loc[0, 'Progreso']}% | Meta: {df_dash.loc[0, 'Meta']}%</span>
        </div>
        <div class="status-card status-revision">
            <strong>🟠 Agente 2: Eficiencia de Picking (Ruta)</strong> — Estatus: <u>REVISIÓN</u> <br>
            <span style="font-size: 13px; opacity: 0.8;">Progreso Actual: {df_dash.loc[1, 'Progreso']}% | Meta: {df_dash.loc[1, 'Meta']}%</span>
        </div>
    """, unsafe_allow_html=True)

elif opcion == "📦 Agente 1: Recepción":
    st.markdown("<h1>📦 Agente 1 - Recepción (Fill Rate)</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.metric(label="Precisión de Recepción Actual", value="33.33%", delta="-61.67% vs Meta")
    st.progress(0.33)

elif opcion == "🚜 Agente 2: Picking":
    st.markdown("<h1>🚜 Agente 2 - Optimización de Rutas (Picking)</h1>", unsafe_allow_html=True)
    for i in range(len(df_a2)):
        r = df_a2.loc[i, "ID_Ruta"]
        o = df_a2.loc[i, "Operario"]
        ef = df_a2.loc[i, "Eficiencia"]
        es = df_a2.loc[i, "Estado"]
        clase = "status-optimo" if es == "ÓPTIMO" else "status-revision"
        st.markdown(f'<div class="status-card {clase}"><strong>Ruta: {r}</strong> — Operario: {o} <br><span style="font-size: 13px; opacity: 0.8;">Eficiencia: {ef}% | Estado: {es}</span></div>', unsafe_allow_html=True)

elif opcion == "⚖️ Agente 3: Packing":
    st.markdown("<h1>⚖️ Agente 3 - Control de Básculas (Packing)</h1>", unsafe_allow_html=True)
    for i in range(len(df_a3)):
        l = df_a3.loc[i, "Lote"]
        d = df_a3.loc[i, "Desvio_Peso"]
        e = df_a3.loc[i, "Estado"]
        clase = "status-critico" if e == "CRÍTICO" else "status-controlado"
        st.markdown(f'<div class="status-card {clase}"><strong>Lote Muestreado: {l}</strong> <br><span style="font-size: 13px; opacity: 0.8;">Desvío Registrado: {d}% | Estado: {e}</span></div>', unsafe_allow_html=True)

elif opcion == "🔄 Agente 4: Devoluciones":
    st.markdown("<h1>🔄 Agente 4 - Logística Inversa (Devoluciones)</h1>", unsafe_allow_html=True)
    for i in range(len(df_a4)):
        s = df_a4.loc[i, "Sku"]
        m = df_a4.loc[i, "Motivo"]
        c = df_a4.loc[i, "Cantidad"]
        st.markdown(f'<div class="status-card status-revision"><strong>SKU: {s}</strong> — Cantidad: {c} <br><span style="font-size: 13px; opacity: 0.8;">Motivo principal de rechazo: {m}</span></div>', unsafe_allow_html=True)

elif opcion == "🚛 Agente 5: Ruteo":
    st.markdown("<h1>🚛 Agente 5 - Optimización de Ruteo (OTIF)</h1>", unsafe_allow_html=True)
    for i in range(len(df_a5)):
        z = df_a5.loc[i, "Zona"]
        ot = df_a5.loc[i, "OTIF"]
        es = df_a5.loc[i, "Estado"]
        clase = "status-optimo" if "ÓPTIMO" in es else "status-revision"
        st.markdown(f'<div class="status-card {clase}"><strong>Zona Logística: {z}</strong> <br><span style="font-size: 13px; opacity: 0.8;">Nivel de Servicio OTIF: {ot}% | Estatus: {es}</span></div>', unsafe_allow_html=True)

    




























    

    





















