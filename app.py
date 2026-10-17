import streamlit as st
import pandas as pd

st.set_page_config(page_title="Logística Lean", layout="wide")

# CAMBIO CRÍTICO: Usamos el puente directo de exportación pública de Sheets a CSV
URL = "https://google.com"

try:
    # Descarga directa de la primera pestaña de la hoja de cálculo
    df = pd.read_csv(URL)
    
    # Limpieza automática de nombres de columnas (quita espacios y pasa a mayúsculas)
    df.columns = df.columns.str.strip().str.upper()
    
    st.sidebar.title("LOGÍSTICA LEAN")
    opcion = st.sidebar.radio("Agentes Activos:", ["📦 Agente 1: Recepción", "🏠 Ver Datos Crudos"])
    
    if opcion == "📦 Agente 1: Recepción":
        st.title("📦 Agente 1 - Recepción (Fill Rate)")
        
        # Identificamos las columnas sin importar cómo estén escritas en tu Sheets
        col_indicador = [c for c in df.columns if 'INDICA' in c or 'KPI' in c or 'NOMBRE' in c]
        col_valores = [c for c in df.columns if 'VALOR' in c or 'ACTUAL' in c or 'CUMPLI' in c]
        
        if col_indicador and col_valores:
            c_ind = col_indicador[0]
            c_val = col_valores[0]
            
            # Buscamos la fila del Fill Rate
            kpi = df[df[c_ind].astype(str).str.contains("Fill Rate|RECEPCION", case=False, na=False)]
            
            if not kpi.empty:
                # Extraemos el valor y lo convertimos a número limpio
                val_str = str(kpi.iloc[0][c_val]).replace(',', '.')
                val_actual = float(val_str)
                
                # Despliegue de la tarjeta modular ejecutiva en modo oscuro
                st.metric(label=f"Métrica: {kpi.iloc[0][c_ind]}", value=f"{val_actual * 100:.2f}%")
                st.progress(min(max(val_actual, 0.0), 1.0))
            else:
                st.warning("No se encontró el texto 'Fill Rate' en la columna de indicadores.")
                st.info("Filas reales encontradas en tu archivo:")
                st.write(list(df[c_ind].unique()))
        else:
            st.error("Estructura de columnas no reconocida.")
            st.info("Columnas actuales en tu Sheets:")
            st.write(list(df.columns))
            
    else:
        st.title("📊 Datos Crudos Sincronizados de Sheets")
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("El archivo de Google Sheets sigue estando privado.")
    st.info("Por favor, verifica en tu Sheets: Compartir -> Acceso General -> Cualquier persona con el enlace (como Lector).")
    st.markdown("---")
    st.caption(f"Error Técnico de Lectura: {e}")


