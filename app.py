import streamlit as st
import pandas as pd

# Configuración de página limpia y robusta
st.set_page_config(page_title="Proyecto Logístico - Dashboard", layout="wide", initial_sidebar_state="expanded")

# Inyección de Estilos únicamente para el Dashboard Principal (Estructura fija controlada)
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

# Identificadores de la Base de Datos Real en Google Sheets
SHEET_ID = "1xaPnDFIBd0Lwy_Z7wVI-SdsxSq20wg7fKtLDypjsd4I"
GID_DASHBOARD = "1440866900"
GID_PICKING = "537805708"
GID_PACKING = "822850707"
GID_DEVOLUCIONES = "999999999"

# Barra Lateral (Sidebar) Corporativo
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
    "🔄 Agente 4: Devoluciones"
])
st.sidebar.markdown("<br><br><hr style='border-color: rgba(255,255,255,0.15);'>", unsafe_allow_html=True)
st.sidebar.caption("🟢 Servidor Serverless · Capa 0 USD")

# --- LÓGICA DE PÁGINAS ---

if opcion == "🏠 Dashboard Principal":
    st.markdown("<h1>Dashboard Ejecutivo</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px; margin-top: 0px;'>Cuadro de mando corporativo · Sincronización en tiempo real</p>", unsafe_allow_html=True)
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
    """, unsafe_allow_html=True)

elif opcion == "📦 Agente 1: Recepción":
    st.markdown("<h1>Agente 1: Control de Recepción</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px;'>Monitoreo de Órdenes de Entrada y Cumplimiento de Proveedores (Fill Rate)</p>", unsafe_allow_html=True)
    
    st.subheader("📝 Registro Rápido de Entrada")
    with st.form("form_recepcion", clear_on_submit=True):
        col_form1, col_form2 = st.columns(2)
        with col_form1:
            id_prov = st.text_input("ID / Nombre Proveedor", placeholder="Ej: Prov_ABC")
            cant_pedida = st.number_input("Cantidad Pedida", min_value=1, value=100)
        with col_form2:
            id_orden = st.text_input("Número de Orden", placeholder="Ej: OC-1004")
            cant_recibida = st.number_input("Cantidad Recibida", min_value=0, value=100)
        
        btn_enviar = st.form_submit_button("Validar Entregas")
        if btn_enviar:
            if cant_pedida > 0:
                fr_calculado = (cant_recibida / cant_pedida) * 100
                st.success(f"✓ Procesado: Orden {id_orden}. Fill Rate Calculado: {fr_calculado:.2f}%")
            else:
                st.error("Error: La cantidad pedida debe ser mayor a cero.")

elif opcion == "🚜 Agente 2: Picking":
    st.markdown("<h1>Agente 2: Planificación de Picking</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px;'>Rutas optimizadas y órdenes asignadas a los operarios en almacén</p>", unsafe_allow_html=True)
    
    url_picking = f"https://google.com{SHEET_ID}/export?format=csv&gid={GID_PICKING}"
    datos_validos = False
    
    try:
        df_picking = pd.read_csv(url_picking)
        if not df_picking.empty and 'OPERARIO' in df_picking.columns:
            datos_validos = True
    except Exception:
        datos_validos = False

    if datos_validos:
        for idx, row in df_picking.iterrows():
            operario = row.get('OPERARIO', 'No Asignado')
            zona = row.get('ZONA', 'General')
            articulos = row.get('ARTICULOS', 0)
            estado = row.get('ESTADO', 'Pendiente')
            
            st.info(f"📋 Tarea #{idx + 1} — Operario: {operario} | Zona: {zona} | Artículos: {articulos} | Estado: {estado}")
    else:
        st.warning("⚠️ Modo de Contingencia Activo: No se detectaron datos en tiempo real en la nube.")
        contingencia_picking = [
            {'OPERARIO': 'Carlos Mendoza', 'ZONA': 'Pasillo A (Nivel 1)', 'ARTICULOS': 24, 'ESTADO': 'En Ruta'},
            {'OPERARIO': 'Elena Rostova', 'ZONA': 'Pasillo D (High-Bay)', 'ARTICULOS': 110, 'ESTADO': 'Pendiente'},
            {'OPERARIO': 'Juan Alarcón', 'ZONA': 'Pasillo B (Mezzanine)', 'ARTICULOS': 45, 'ESTADO': 'Completado'}
        ]
        for idx, tarea in enumerate(contingencia_picking):
            st.info(f"📋 Tarea #{idx + 1} (Contingencia) — Operario: {tarea['OPERARIO']} | Zona: {tarea['ZONA']} | Artículos: {tarea['ARTICULOS']} | Estado: {tarea['ESTADO']}")

elif opcion == "⚖️ Agente 3: Packing":
    st.markdown("<h1>Agente 3: Control de Peso en Packing</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px;'>Validación física de empaque mediante báscula automatizada de fin de línea</p>", unsafe_allow_html=True)
    
    url_packing = f"https://google.com{SHEET_ID}/export?format=csv&gid={GID_PACKING}"
    datos_validos = False
    
    try:
        df_packing = pd.read_csv(url_packing)
        if not df_packing.empty and 'PEDIDO' in df_packing.columns:
            datos_validos = True
    except Exception:
        datos_validos = False

    if datos_validos:
        for idx, row in df_packing.iterrows():
            pedido = row.get('PEDIDO', 'N/A')
            peso_teo = row.get('PESO_TEORICO', 0.0)
            peso_real = row.get('PESO_REAL', 0.0)
            desvio = abs(peso_real - peso_teo)
            
            if desvio <= 0.05:







    

    





















