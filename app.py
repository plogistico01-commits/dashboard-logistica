import streamlit as st
import pandas as pd
import requests

# ==============================================================================
# 1. CONFIGURACIÓN DE INTERFAZ PREMIUM LOGÍSTICA
# ==============================================================================
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
        
        /* Contenedores Premium para Tablas de Datos Sincronizados */
        .premium-table-container { background-color: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-top: 15px; }
        .premium-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 16px; border-bottom: 1px solid #F3F4F6; font-family: 'Inter', sans-serif; }
        .premium-row:last-child { border-bottom: none; }
        .premium-id { font-weight: 700; color: #1E3A8A; background: #E0E7FF; padding: 4px 8px; border-radius: 6px; font-size: 12px; }
        .premium-text { color: #374151; font-weight: 500; font-size: 14px; flex-grow: 1; margin-left: 15px; }
        .premium-badge { padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. CONFIGURACIÓN DE FUENTES DE DATOS Y ENLACES (GOOGLE SHEETS & DISCORD)
# ==============================================================================
# Base URL de tu Google Sheet publicado como Web (Formato CSV para extracción directa)
SHEET_BASE_URL = "https://google.com"

# Diccionario unificado de GIDs correspondientes a cada área logística
GIDS = {
    "Dashboard": "1440866900",
    "Picking": "537805708",
    "Packing": "822850707",
    "Devoluciones": "1865557384",
    "Ruteo": "773965386"
}

# Webhook único asignado para alertas de Devoluciones / Operaciones Integradas
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1560761272478212197/KX1zWredjPADAQUIDfm-3rbi0Q9QRmpZJWCh-3sTj2NWPUNb0JPp3TCfcrVayts4G6J5"

# ==============================================================================
# 3. FUNCIONES DE AUTOMATIZACIÓN (CONECTORES DE DATOS Y ALERTAS)
# ==============================================================================
@st.cache_data(ttl=60)  # Mantiene los datos en caché por 60 segundos para evitar saturar la red
def cargar_datos_sheet(gid_name):
    """Extrae dinámicamente datos desde una pestaña específica de Google Sheets vía GID."""
    try:
        url = f"{SHEET_BASE_URL}&gid={GIDS[gid_name]}"
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.sidebar.error(f"⚠️ Error conectando con pestaña {gid_name}: {e}")
        return pd.DataFrame()

def enviar_alerta_discord(titulo, descripcion, color_hex, campos=None):
    """Despacha notificaciones enriquecidas (Embeds) hacia el canal de Discord asignado."""
    if not DISCORD_WEBHOOK_URL:
        return False
    
    color_decimal = int(color_hex.replace("#", ""), 16)
    
    embed = {
        "title": titulo,
        "description": descripcion,
        "color": color_decimal,
        "footer": {"text": "Sistema Automatizado Logístico · Alerta en Tiempo Real"}
    }
    
    if campos:
        embed["fields"] = [{"name": k, "value": str(v), "inline": True} for k, v in campos.items()]
        
    payload = {"embeds": [embed]}
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        return response.status_code == 204
    except Exception:
        return False

def renderizar_tabla_premium(df, columna_id, columna_texto, columna_status):
    """Transforma un DataFrame crudo en una lista visual elegante y fácil de leer."""
    if df.empty:
        st.warning("No hay registros disponibles en esta sección.")
        return
        
    st.markdown('<div class="premium-table-container">', unsafe_allow_html=True)
    for _, row in df.iterrows():
        status_val = str(row[columna_status]).strip().upper()
        
        # Asignación dinámica de estilos según estado
        if status_val in ["CRÍTICO", "ALERTA", "FALLO", "REVISAR CONTENIDO", "X"]:
            bg_badge, txt_badge = "#FEF2F2", "#991B1B"
        elif status_val in ["REVISIÓN", "PENDIENTE", "PROCESO"]:
            bg_badge, txt_badge = "#FFF7ED", "#9A3412"
        elif status_val in ["ÓPTIMO", "COMPLETO", "EXITOSO", "A"]:
            bg_badge, txt_badge = "#F0FDF4", "#166534"
        else:
            bg_badge, txt_badge = "#F0F9FF", "#075985"
            
        st.markdown(f"""
            <div class="premium-row">
                <div class="premium-id">#{row[columna_id]}</div>
                <div class="premium-text">{row[columna_texto]}</div>
                <div class="premium-badge" style="background-color: {bg_badge}; color: {txt_badge};">
                    {row[columna_status]}
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 4. SIDEBAR FIJA CORPORATIVA
# ==============================================================================
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

opcion = st.sidebar.radio("Menú de Navegación:", [
    "🏠 Dashboard Principal", 
    "📦 Agente 1: Recepción", 
    "🚜 Agente 2: Picking", 
    "⚖️ Agente 3: Packing", 
    "🔄 Agente 4: Devoluciones", 
    "🚛 Agente 5: Ruteo"
])
st.sidebar.markdown("<br><br><hr style='border-color: rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
st.sidebar.caption("🟢 Servidor Serverless · Capa 0 USD")

# ==============================================================================
# 5. ENRUTAMIENTO DE INTERFAZ Y LOGICA DE NAVEGACIÓN
# ==============================================================================
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
        



            



    



    


    




    




























    

    





















