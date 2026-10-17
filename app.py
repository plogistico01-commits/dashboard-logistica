import streamlit as st
import pandas as pd

st.set_page_config(page_title="Logística Lean", layout="wide")

# Conexión directa ultra-simplificada a la hoja principal de control
SHEET_ID = "1xaPnDFIBd0Lwy_Z7wVI-SdsxSq20wg7fKtLDypjsd4I"
URL = f"https://google.com{SHEET_ID}/export?format=csv&gid=1440866900"

try:
    # El servidor remoto descarga el archivo plano directamente
    df = pd.read_csv(URL, encoding='utf-8')
    df.columns = df.columns.str.strip().str.upper()
    
    st.sidebar.title("LOGÍSTICA LEAN")
    opcion = st.sidebar.radio("Agentes Activos:", ["📦 Agente 1: Recepción", "🏠 Ver Datos Crudos"])
    
    # Buscamos las columnas reales de forma automática
    col_indicador = [c for c in df.columns if 'INDICA' in c or 'KPI' in c or 'NOMBRE' in c][0]
    col_valores = [c for c in df.columns if 'VALOR' in c or 'ACTUAL' in c or 'CUMPLI' in c][0]
    
    if opcion == "📦 Agente 1: Recepción":
        st.title("📦 Agente 1 - Recepción (Fill Rate)")
        
        # Filtramos la fila exacta del indicador de entrada
        kpi = df[df[col_indicador].astype(str).str.contains("Fill Rate|PRECISION|RECEPCION", case=False, na=False)]
        
        if not kpi.empty:
            val_str = str(kpi.iloc[0][col_valores]).replace(',', '.').replace('%', '').strip()
            val_actual = float(val_str)
            
            if val_actual > 1.0:
                val_actual = val_actual / 100.0
                
            # Renderizado final en modo oscuro premium
            st.metric(label="Precisión de Recepción Actual", value=f"{val_actual * 100:.2f}%")
            st.progress(min(max(val_actual, 0.0), 1.0))
        else:
            st.warning("No se encontró la fila del indicador de recepción en la columna.")
            st.write(list(df[col_indicador].unique()))
    else:
        st.title("📊 Datos Crudos Sincronizados de Sheets")
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("Conexión establecida. Esperando actualización del canal de datos.")
    st.info("Presiona la tecla 'R' para forzar la lectura del archivo de Google Sheets.")
    st.caption(f"Aviso del sistema: {e}")








