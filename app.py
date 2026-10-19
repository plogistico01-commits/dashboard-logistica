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
# URL real de tu Google Sheet ya integrada correctamente
SHEET_BASE_URL = "https://google.com"

# Diccionario unificado de GIDs correspondientes a cada área logística
GIDS = {
    "Dashboard": "1440866900",
    "Recepcion": "0",
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
@st.cache_data(ttl=60)
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
        st.warning("No hay registros disponibles o la pestaña está vacía.")
        return
        
    st.markdown('<div class="premium-table-container">', unsafe_allow_html=True)
    for idx, row in df.iterrows():
        if columna_id not in df.columns or columna_texto not in df.columns or columna_status not in df.columns:
            st.error(f"Columnas requeridas no encontradas. Verifica que existan: {columna_id}, {columna_texto}, {columna_status}")
            break
            
        status_val = str(row[columna_status]).strip().upper()
        
        if "ALERTA" in status_val or "CRÍTICO" in status_val or "🔴" in status_val:
            bg_badge, txt_badge = "#FEF2F2", "#991B1B"
        elif "REVISIÓN" in status_val or "PENDIENTE" in status_val:
            bg_badge, txt_badge = "#FFF7ED", "#9A3412"
        elif "ÓPTIMO" in status_val or "🟢" in status_val or "ALTA" in status_val:
            bg_badge, txt_badge = "#F0FDF4", "#166534"
        else:
            bg_badge, txt_badge = "#F0F9FF", "#075985"
            
        # Generar un ID visual incremental basado en el índice de la fila
        id_visual = idx + 1
            
        st.markdown(f"""
            <div class="premium-row">
                <div class="premium-id">#{id_visual}</div>
                <div class="premium-text"><b>{row[columna_id]}</b> — Valor: {row[columna_texto]}</div>
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
st.sidebar.caption("🟢 Servidor Activo")

# ==============================================================================
# 5. LÓGICA DE ENRUTAMIENTO Y RENDERIZADO DE PÁGINAS
# ==============================================================================
if opcion == "🏠 Dashboard Principal":
    st.title("🏠 Dashboard Logístico Central")
    df_dash = cargar_datos_sheet("Dashboard")
    renderizar_tabla_premium(df_dash, columna_id="Indicador", columna_texto="Valor Actual", columna_status="Estado de Rendimiento")

elif opcion == "📦 Agente 1: Recepción":
    st.title("📦 Control de Recepción de Mercancías")
    df_rec = cargar_datos_sheet("Recepcion")
    renderizar_tabla_premium(df_rec, columna_id="Indicador", columna_texto="Valor Actual", columna_status="Estado de Rendimiento")

elif opcion == "🚜 Agente 2: Picking":
    st.title("🚜 Gestión de Picking en Almacén")
    df_pick = cargar_datos_sheet("Picking")
    renderizar_tabla_premium(df_pick, columna_id="Indicador", columna_texto="Valor Actual", columna_status="Estado de Rendimiento")

elif opcion == "⚖️ Agente 3: Packing":
    st.title("⚖️ Línea de Packing y Embalaje")
    df_pack = cargar_datos_sheet("Packing")
    renderizar_tabla_premium(df_pack, columna_id="Indicador", columna_texto="Valor Actual", columna_status="Estado de Rendimiento")
    
    if st.button("🚨 Reportar Incidencia de Packing"):



        



            



    



    


    




    




























    

    





















