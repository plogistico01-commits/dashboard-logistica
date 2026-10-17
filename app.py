import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Logística Lean", layout="wide")

# Enlace de descarga directa forzada a formato CSV plano
SHEET_ID = "1xaPnDFIBd0Lwy_Z7wVI-SdsxSq20wg7fKtLDypjsd4I"
URL = f"https://google.com{SHEET_ID}/export?format=csv&gid=1440866900"

@st.cache_data(ttl=30)  # Limpia la memoria del servidor cada 30 segundos
def cargar_datos_con_reintento(url_api):
    # Mecanismo Lean de reintento automático si la red de Google falla
    for _ in range(3):
        try:
            return pd.read_csv(url_api)
        except Exception:
            time.sleep(1)
    return pd.read_csv(url_api)

try:
    df = cargar_datos_con_reintento(URL)
    
    # Normalización de los nombres de columnas
    df.columns = df.columns.str.strip().str.upper()
    
    st.sidebar.title("LOGÍSTICA LEAN")
    opcion = st.sidebar.radio("Agentes Activos:", ["📦 Agente 1: Recepción", "🏠 Ver Datos Crudos"])
    
    # Mapeo inteligente de las columnas reales
    col_indicador = [c for c in df.columns if 'INDICA' in c or 'KPI' in c or 'NOMBRE' in c or 'MÉTRICA' in c]
    col_valores = [c for c in df.columns if 'VALOR' in c or 'ACTUAL' in c or 'CUMPLI' in c or 'DATO' in c]
    
    if opcion == "📦 Agente 1: Recepción":
        st.title("📦 Agente 1 - Recepción (Fill Rate)")
        
        if col_indicador and col_valores:
            c_ind = col_indicador[0]
            c_val = col_valores[0]
            
            # Buscamos la fila del Fill Rate de forma elástica
            kpi = df[df[c_ind].astype(str).str.contains("Fill Rate|PRECISION|RECEPCION", case=False, na=False)]
            
            if not kpi.empty:
                val_raw = kpi.iloc[0][c_val]
                val_str = str(val_raw).replace(',', '.').replace('%', '').strip()
                val_actual = float(val_str)
                
                if val_actual > 1.0:
                    val_actual = val_actual / 100.0
                
                # Despliegue de tarjeta modular premium en Modo Oscuro
                st.metric(label=f"Métrica: {kpi.iloc[0][c_ind]}", value=f"{val_actual * 100:.2f}%")
                st.progress(min(max(val_actual, 0.0), 1.0))
            else:
                st.warning("No se encontró la fila 'Fill Rate' en la columna de indicadores.")
                st.info("Filas encontradas en esta pestaña:")
                st.write(list(df[c_ind].unique()))
        else:
            st.error("Estructura de columnas no reconocida.")
            st.info("Columnas leídas en tiempo real:")
            st.write(list(df.columns))
            
    else:
        st.title("📊 Datos Crudos Sincronizados de Sheets")
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("Error temporal de red entre los servidores remotos.")
    st.info("Por favor, presiona la tecla 'R' en unos segundos para reintentar la conexión automática.")
    st.caption(f"Detalle técnico de red: {e}")







