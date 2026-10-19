import streamlit as st
import pandas as pd

# Configuración y carga de datos desde Google Sheets para la aplicación logística en Streamlit.
st.set_page_config(page_title="Proyecto Logístico", layout="wide")
SHEET_BASE_URL = "https://google.com"

GIDS = {
    "Dashboard": "1440866900", "Recepcion": "0", "Picking": "537805708",
    "Packing": "822850707", "Devoluciones": "1865557384", "Ruteo": "773965386"
}

def cargar_datos(gid_name):
    try:
        return pd.read_csv(f"{SHEET_BASE_URL}&gid={GIDS[gid_name]}")
    except Exception as e:
        st.error(f"Error: {e}")
        return pd.DataFrame()

opcion = st.sidebar.radio("Menú:", ["Dashboard", "Recepción", "Picking", "Packing", "Devoluciones", "Ruteo"])
df = cargar_datos(opcion)
if not df.empty:
    st.dataframe(df, use_container_width=True)

