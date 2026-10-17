import streamlit as st
import pandas as pd

# Configuración de interfaz ejecutiva
st.set_page_config(page_title="Logística Lean", layout="wide")

# Conexión directa y limpia a la API pública de Google Sheets exportada a CSV
URL = "https://google.com"

try:
    # Lectura serverless del reporte crudo de Atenea
    df = pd.read_csv(URL)
    
    st.sidebar.title("LOGÍSTICA LEAN")
    opcion = st.sidebar.radio("Agentes Activos:", ["📦 Agente 1: Recepción", "🏠 Ver Datos Crudos"])
    
    if opcion == "📦 Agente 1: Recepción":
        st.title("📦 Agente 1 - Recepción (Fill Rate)")
        
        # Filtro automático del KPI en la nube
        kpi = df[df['Indicador'].str.contains("Fill Rate", case=False, na=False)]
        
        if not kpi.empty:
            # Limpieza matemática de caracteres decimales de Sheets
            val_str = str(kpi.iloc[0]['Valor Actual']).replace(',', '.')
            val_actual = float(val_str)
            
            # Renderizado de Tarjeta Flotante en Modo Oscuro
            st.metric(label="Precisión de Recepción Actual", value=f"{val_actual * 100:.2f}%")
            st.progress(min(max(val_actual, 0.0), 1.0))
        else:
            st.warning("Indicador no detectado. Revisa la columna A en la pestaña de Sheets.")
            
    else:
        st.title("📊 Datos Crudos Sincronizados de Sheets")
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Configura tu Sheets como 'Cualquier persona con el enlace puede ver'. Detalle Técnico: {e}")

