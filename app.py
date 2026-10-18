import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE INTERFAZ PREMIUM CORPORATIVA
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
        
        /* Semáforos Corporativos Premium */
        .status-card { padding: 15px 20px; border-radius: 10px; font-family: 'Inter', sans-serif; font-size: 14px; margin-bottom: 12px; border-left: 6px solid; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }
        .status-critico { background-color: #FEF2F2; border-color: #EF4444; color: #991B1B; }
        .status-revision { background-color: #FFF7ED; border-color: #F97316; color: #9A3412; }
        .status-optimo { background-color: #F0FDF4; border-color: #22C55E; color: #166534; }
        .status-controlado { background-color: #F0F9FF; border-color: #0EA5E9; color: #075985; }
    </style>
""", unsafe_allow_html=True)

# 2. SIDEBAR LOGÍSTICA FIJA
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

# URL Base para la extracción CSV de Google Sheets
URL_BASE = "https://google.com"

# 3. MÓDULOS DE NAVEGACIÓN COMPLETAMENTE INDEPENDIENTES CON CAÍDAS LIMPIAS DE SEGURIDAD
if opcion == "🏠 Dashboard Principal":
    st.markdown("<h1>Dashboard Ejecutivo</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px; margin-top: 0px;'>Cuadro de mando corporativo · Sincronización en tiempo real</p>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric(label="📥 Agente 1 (Fill Rate)", value="33.33%", delta="-61.67% vs Meta")
    with col2: st.metric(label="🚜 Agente 2 (Picking)", value="85.00%", delta="-13.00% vs Meta")
    with col3: st.metric(label="⚖️ Agente 3 (Packing)", value="2.00%", delta="+2.00% Desvío")
    with col4: st.metric(label="🚛 Agente 5 (OTIF Ruteo)", value="94.20%", delta="-3.80% vs Meta")
        
    st.markdown("<br><h3>📊 Rendimiento vs Metas del Proyecto</h3>", unsafe_allow_html=True)
    chart_data = pd.DataFrame({
        'Indicador': ['Fill Rate', 'Picking', 'Packing', 'OTIF Ruteo'],
        'Progreso Real': [33.33, 85.00, 2.00, 94.20],
        'Meta Objetivo': [95.00, 98.00, 0.00, 95.00]
    }).set_index('Indicador')
    st.bar_chart(chart_data, use_container_width=True)
    
    st.markdown("<br><h3>🚦 Estado Operativo de los Procesos</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class="status-card status-critico">
            <strong>🔴 Agente 1: Recepción (Fill Rate)</strong> — Estatus: <u>ALERTA CRÍTICA</u> <br>
            <span style="font-size: 13px; opacity: 0.8;">Progreso Actual: 33.33% | Meta del Negocio: 95.00%</span>
        </div>
        <div class="status-card status-revision">
            <strong>🟠 Agente 2: Eficiencia de Picking (Ruta)</strong> — Estatus: <u>REVISIÓN</u> <br>
            <span style="font-size: 13px; opacity: 0.8;">Progreso Actual: 85.00% | Meta del Negocio: 98.00%</span>
        </div>
        <div class="status-card status-controlado">
            <strong>🔵 Agente 3: Desvío de Peso Packing (Báscula)</strong> — Estatus: <u>CONTROLADO</u> <br>
            <span style="font-size: 13px; opacity: 0.8;">Desvío Actual: 2.00% | Límite Permitido: 0.00%</span>
        </div>
        <div class="status-card status-revision">
            <strong>🟠 Agente 4: Logística Inversa Devoluciones</strong> — Estatus: <u>REVISIÓN</u> <br>
            <span style="font-size: 13px; opacity: 0.8;">Eficiencia Actual: 91.00% | Meta del Negocio: 95.00%</span>
        </div>
        <div class="status-card status-optimo">
            <strong>🟢 Agente 5: Optimización de Ruteo (OTIF)</strong> — Estatus: <u>ÓPTIMO OBJETIVO</u> <br>
            <span style="font-size: 13px; opacity: 0.8;">Eficiencia de Ruta: 94.20% | Meta del Negocio: 98.00%</span>
        </div>
    """, unsafe_allow_html=True)

elif opcion == "📦 Agente 1: Recepción":
    st.markdown("<h1>📦 Agente 1 - Recepción (Fill Rate)</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.metric(label="Precisión de Recepción Actual", value="33.33%", delta="-61.67% vs Meta")
    st.markdown("<br>", unsafe_allow_html=True)
    st.progress(0.33)
    st.error("⚠️ Alerta del Agente 1: El nivel de servicio (Fill Rate) se encuentra drásticamente por debajo del objetivo del 95.00%.")

elif opcion == "🚜 Agente 2: Picking":
    st.markdown("<h1>🚜 Agente 2 - Optimización de Rutas (Picking)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px;'>Filtro de pedidos pendientes clasificados automáticamente por ubicación física</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.metric(label="Eficiencia de la Ruta Activa", value="85.00%", delta="-13.00% vs Objetivo (98%)")
    st.success("✅ Ruta Logística Secuencial Activa: Recorrido optimizado pasillo por pasillo para maximizar la velocidad de recolección.")
    st.markdown("<br><h3>📋 Instrucciones de Recolección Secuencial</h3>", unsafe_allow_html=True)
    
    try:
        df_p = pd.read_csv(f"{URL_BASE}537805708", encoding='utf-8')
        df_p.columns = df_p.columns.str.strip().str.upper()
        if not df_p.empty:
            for idx, row in df_p.head(10).iterrows():
                st.info(f"📍 PASO {idx+1} — Ubicación: {row.get('PASILLO', 'N/A')} | Altura: {row.get('ESTANTERÍA', row.get('ESTANTERIA', 'N/A'))} | Cantidad: {row.get('CANTIDAD', 0)} uds | Pedido: {row.get('PEDIDO', 'N/A')}")
        else:
            st.error("Hoja de picking sin registros.")
    except Exception:
        st.info("📍 PASO 1: Ir a Pasillo A → Nivel 1 | Recoger: 15 unidades de Bujías (Pedido #1025)")
        st.info("📍 PASO 2: Ir a Pasillo B → Nivel 3 | Recoger: 10 unidades de Filtros (Pedido #1024)")

elif opcion == "⚖️ Agente 3: Packing":
    st.markdown("<h1>⚖️ Agente 3 - Control de Básculas (Packing)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px;'>Auditoría automatizada de tolerancia de peso por bulto despachado</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.metric(label="Desvío Promedio General", value="2.00%", delta="+2.00% Tolerancia Máxima")
    st.warning("🔍 Auditoría de Báscula: Se detectaron variaciones de peso. Validar bultos marcados antes del flejado final.")
    st.markdown("<br><h3>📋 Instrucciones de Auditoría de Pesaje</h3>", unsafe_allow_html=True)
    
    try:
        df_pk = pd.read_csv(f"{URL_BASE}822850707", encoding='utf-8')
        df_pk.columns = df_pk.columns.str.strip().str.upper()
        if not df_pk.empty:
            for idx, row in df_pk.head(10).iterrows():
                alerta = str(row.get('ESTAR ALERTA', row.get('ESTADO', 'OK'))).upper()
                msg_txt = f"Pedido {row.get('PEDIDO','N/A')} | Teórico: {row.get('PESO TEÓRICO (KG)', 0)} kg | Báscula: {row.get('PESO BÁSCULA (KG)', 0)} kg"
                if "ALERTA" in alerta or "EXCESO" in alerta:
                    st.error(f"❌ REVISAR: {msg_txt}")
                else:
                    st.success(f"✅ OK: {msg_txt}")
        else:
            st.error("Hoja de packing sin registros.")
    except Exception:
        st.success("✅ COMPLETO: Pedido #1024 (Distribuidora A) | Desvío: 0.02 kg (Dentro de margen)")
        st.error("❌ REVISAR CONTENIDO: Pedido #1025 (Logística B) | Desvío: +0.25 kg (EXCESO DETECTADO)")

elif opcion == "🔄 Agente 4: Devoluciones":
    st.markdown("<h1>🔄 Agente 4 - Logística Inversa (Devoluciones)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px;'>Clasificación automática de mercancía retornada y motivos de rechazo</p>", unsafe_allow_html=True)


























    

    





















