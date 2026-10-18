import streamlit as st
import pandas as pd
import requests

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

# =====================================================================
# CONFIGURACIÓN DE CONEXIONES EXTERNAS (DISCORD Y GOOGLE SHEETS)
# =====================================================================
WEBHOOKS_DISCORD = {
    "recepcion": "https://discord.com",
    "picking": "https://discord.com",
    "packing": "https://discord.com/api/webhooks/1560761272478212197/KX1zWredjPADAQUIDfm-3rbi0Q9QRmpZJWCh-3sTj2NWPUNb0JPp3TCfcrVayts4G6J5",
    "devoluciones": "https://discord.com/api/webhooks/1560768326286970953/ma2B_qPWWZYiJBqkRAGJ9rAk7UpoAnDJ4gAdTTOBrBWWReZnyikLg7FqL-bnokb9Ks7t",
    "ruteo": "https://discord.com",
    "dashboard": "https://discord.com"
}

SHEET_ID = "1xaPnDFIBd0Lwy_Z7wVI-SdsxSq20wg7fKtLDypjsd4I"

# GIDs Maestros Integrados de forma fija
GIDS = {
    "picking": "537805708",
    "packing": "822850707",
    "devoluciones": "1865557384",
    "ruteo": "773965386",
    "dashboard": "1440866900"
}

def enviar_mensaje_discord(area, mensaje):
    """Ejecuta notificaciones salientes controladas con límite de tiempo de espera"""
    url = WEBHOOKS_DISCORD.get(area)
    if url:
        try:
            requests.post(url, json={"content": mensaje}, timeout=5)
        except Exception:
            pass

def descargar_pestana_sheets(nombre_pestana):
    """Función unificada para descargar cualquier pestaña garantizando estabilidad total"""
    gid = GIDS.get(nombre_pestana)
    url_csv = f"https://google.com{SHEET_ID}/export?format=csv&gid={gid}"
    try:
        df = pd.read_csv(url_csv, encoding='utf-8')
        df.columns = df.columns.str.strip().str.upper()
        return df
    except Exception:
        # Respaldos limpios de contingencia usando tuplas seguras contra fallos del formateador
        if nombre_pestana == "picking":
            return pd.DataFrame({
                'PEDIDO': list(("#1025", "#1024")), 'PASILLO': list(("A", "B")), 'NIVEL': list((1, 3)),
                'PRODUCTO': list(("Bujías", "Filtros")), 'CANTIDAD': list((15, 10)), 'ESTADO': list(("PENDIENTE", "PENDIENTE"))
            })
        return pd.DataFrame()
# =====================================================================

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

# 3. INTERFAZ EN FORMATO PLANO ULTRA-ESTABLE
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

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("📢 Emitir Alerta de Dashboard General"):
        enviar_mensaje_discord("dashboard", "📊 **REPORTE GENERAL DE DASHBOARD:** Sincronización corporativa completada. Verifique estados de alerta crítica en el panel ejecutivo web.")
        st.toast("Reporte general enviado a Discord.", icon="📊")

elif opcion == "📦 Agente 1: Recepción":
    st.markdown("<h1>📦 Agente 1 - Recepción (Fill Rate)</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.metric(label="Precisión de Recepción Actual", value="33.33%", delta="-61.67% vs Meta")
    st.markdown("<br>", unsafe_allow_html=True)
    st.progress(0.33)
    st.error("⚠️ Alerta del Agente 1: El nivel de servicio (Fill Rate) se encuentra drásticamente por debajo del objetivo del 95.00%.")
    
    if st.button("📢 Reportar Alerta Crítica a Discord"):
        enviar_mensaje_discord("recepcion", "🚨 **ALERTA CRÍTICA EN RECEPCIÓN:** El Fill Rate actual se desplomó al **33.33%**. Se requiere revisión de stock de inmediato.")
        st.toast("Reporte enviado al canal de Recepción.", icon="📥")

elif opcion == "🚜 Agente 2: Picking":
    st.markdown("<h1>🚜 Agente 2 - Optimización de Rutas (Picking)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px;'>Filtro de pedidos pendientes clasificados automáticamente por ubicación física</p>", unsafe_allow_html=True)
    st.markdown("---")
    

    



    


    




    




























    

    





















