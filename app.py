import streamlit as st
import pandas as pd
import requests

# 1. CONFIGURACIÓN DE LA APP
st.set_page_config(page_title="Proyecto Logístico", layout="wide")

# URL de tu Google Sheet (Verificada)
SHEET_BASE_URL = "https://google.com"

# Diccionario de GIDs de tus pestañas
GIDS = {
    "Dashboard": "1440866900",
    "Recepcion": "0",
    "Picking": "537805708",
    "Packing": "822850707",
    "Devoluciones": "1865557384",
    "Ruteo": "773965386"
}

# 2. FUNCIÓN PARA CARGAR DATOS
def cargar_datos(gid_name):
    try:
        url = f"{SHEET_BASE_URL}&gid={GIDS[gid_name]}"
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Error al conectar con la pestaña {gid_name}: {e}")
        return pd.DataFrame()

# 3. MENÚ DE NAVEGACIÓN
st.sidebar.title("Proyecto Logístico")
opcion = st.sidebar.radio("Menú:", [
    "🏠 Dashboard Principal", 
    "📦 Agente 1: Recepción", 
    "🚜 Agente 2: Picking", 
    "⚖️ Agente 3: Packing", 
    "🔄 Agente 4: Devoluciones", 
    "🚛 Agente 5: Ruteo"
])

# 4. LÓGICA DE VISUALIZACIÓN (Estructura plana y probada)
if opcion == "🏠 Dashboard Principal":
    st.title("🏠 Dashboard Logístico Central")
    df = cargar_datos("Dashboard")
    if not df.empty:
        st.dataframe(df, use_container_width=True)

elif opcion == "📦 Agente 1: Recepción":
    st.title("📦 Control de Recepción")
    df = cargar_datos("Recepcion")
    if not df.empty:
        st.dataframe(df, use_container_width=True)

elif opcion == "🚜 Agente 2: Picking":
    st.title("🚜 Gestión de Picking")
    df = cargar_datos("Picking")
    if not df.empty:
        st.dataframe(df, use_container_width=True)

elif opcion == "⚖️ Agente 3: Packing":
    st.title("⚖️ Línea de Packing")
    df = cargar_datos("Packing")
    if not df.empty:
        st.dataframe(df, use_container_width=True)

elif opcion == "🔄 Agente 4: Devoluciones":
    st.title("🔄 Logística Inversa")
    df = cargar_datos("Devoluciones")
    if not df.empty:
        st.dataframe(df, use_container_width=True)

elif opcion == "🚛 Agente 5: Ruteo":
    st.title("🚛 Optimización de Ruteo")
    df = cargar_datos("Ruteo")
    if not df.empty:
        st.dataframe(df, use_container_width=True)
