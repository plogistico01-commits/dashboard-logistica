import streamlit as st
import pandas as pd

st.set_page_config(page_title="Logística Lean", layout="wide")

# CONEXIÓN INTEGRAL: Apunta directamente al ID real de tu pestaña Dashboard_KPIs
URL = "https://google.com"

try:
    df = pd.read_csv(URL)
    
    # Normalización automática: Eliminamos espacios raros y pasamos todo a mayúsculas
    df.columns = df.columns.str.strip().str.upper()
    
    st.sidebar.title("LOGÍSTICA LEAN")
    opcion = st.sidebar.radio("Agentes Activos:", ["📦 Agente 1: Recepción", "🏠 Ver Datos Crudos"])
    
    # Identificación inteligente de columnas por aproximación de texto
    col_indicador = [c for c in df.columns if 'INDICA' in c or 'KPI' in c or 'NOMBRE' in c or 'MÉTRICA' in c or 'METRICA' in c]
    col_valores = [c for c in df.columns if 'VALOR' in c or 'ACTUAL' in c or 'CUMPLI' in c or 'DATO' in c]
    
    if opcion == "📦 Agente 1: Recepción":
        st.title("📦 Agente 1 - Recepción (Fill Rate)")
        
        if col_indicador and col_valores:
            c_ind = col_indicador[0]
            c_val = col_valores[0]
            
            # Filtramos la fila del Fill Rate de forma elástica
            kpi = df[df[c_ind].astype(str).str.contains("Fill Rate|PRECISION|RECEPCION", case=False, na=False)]
            
            if not kpi.empty:
                # Extraemos y limpiamos el número decimal de Sheets
                val_raw = kpi.iloc[0][c_val]
                val_str = str(val_raw).replace(',', '.').replace('%', '').strip()
                val_actual = float(val_str)
                
                # Corrección automática de escala si viene en formato entero (ej. 33.33)
                if val_actual > 1.0:
                    val_actual = val_actual / 100.0
                
                # Despliegue de tarjeta modular premium en Modo Oscuro nativo
                st.metric(label=f"Indicador: {kpi.iloc[0][c_ind]}", value=f"{val_actual * 100:.2f}%")
                st.progress(min(max(val_actual, 0.0), 1.0))
            else:
                st.warning("No se encontró una fila con el texto 'Fill Rate' o 'Recepción'.")
                st.info("Filas disponibles detectadas en esta pestaña:")
                st.write(list(df[c_ind].unique()))
        else:
            st.error("Estructura de columnas no reconocida en 'Dashboard_KPIs'.")
            st.info("Columnas leídas en tiempo real por el servidor:")
            st.write(list(df.columns))
            
    else:
        st.title("📊 Datos Crudos Sincronizados de Sheets")
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Error al conectar con la pestaña logísticamente estructurada: {e}")




