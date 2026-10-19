import streamlit as st
import pandas as pd

# Configuración estructural del Dashboard Logístico
st.set_page_config(page_title="Proyecto Logístico", layout="wide")

# URL directa y verificada de tu Google Sheet en formato de exportación limpia (.csv)
SHEET_BASE_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRVoZ6vpNBIbJ7rXQcHMBTUQ9CNKA2O8E-KMMAM-w1FAOr9C-aKhLwgwBT4FgYFar-ycY6TZLfNW7wf/pub?output=csv"


# Diccionario de identificadores únicos (GIDs) por cada pestaña de operación
GIDS = {
    "Dashboard": "1440866900", 
    "Recepcion": "0", 
    "Picking": "537805708",
    "Packing": "822850707", 
    "Devoluciones": "1865557384", 
    "Ruteo": "773965386"
}

def cargar_datos(gid_name):
    """Extrae de forma directa las filas de datos desde Google Sheets usando el GID específico."""
    try:
        url_final = f"{SHEET_BASE_URL}&gid={GIDS[gid_name]}"
        return pd.read_csv(url_final)
    except Exception as e:
        st.error(f"Error de conexión: {e}")
        return pd.DataFrame()

# Panel lateral con el selector de control logístico
opcion = st.sidebar.radio("Menú:", ["Dashboard", "Recepcion", "Picking", "Packing", "Devoluciones", "Ruteo"])

# Ejecución y despliegue automático de la información en el contenedor visual
df = cargar_datos(opcion)
if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.warning(f"La pestaña '{opcion}' está conectada pero actualmente no contiene registros para mostrar.")


