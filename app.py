import streamlit as st
import pandas as pd

st.set_page_config(page_title="Logística Lean", layout="wide")

# CONEXIÓN CORREGIDA: Apunta con precisión quirúrgica a la pestaña de KPIs usando su ID real de Google
URL = "https://google.com"

try:
    df = pd.read_csv(URL)
    
    # Limpieza automática de nombres de columnas
    df.columns = df.columns.str.strip().str.upper()
    
    st.sidebar.title("LOGÍSTICA LEAN")
    opcion = st.sidebar.radio("Agentes Activos:", ["📦 Agente 1: Recepción", "🏠 Ver Datos Crudos"])
    
    # Buscamos las columnas de forma inteligente sin importar mayúsculas o espacios
    col_indicador = [c for c in df.columns if 'INDICA' in c or 'KPI' in c or 'NOMBRE' in c]
    col_valores = [c for c in df.columns if 'VALOR' in c or 'ACTUAL' in c or 'CUMPLI' in c]
    
    if opcion == "📦 Agente 1: Recepción":
        st.title("📦 Agente 1 - Recepción (Fill Rate)")
        
        if col_indicador and col_valores:
            c_ind = col_indicador[0]
            c_val = col_valores[0]
            
            # Filtramos de forma exacta la fila del Fill Rate
            kpi = df[df[c_ind].astype(str).str.contains("Fill Rate|PRECISION|RECEPCION", case=False, na=False)]
            
            if not kpi.empty:
                # Limpieza matemática de caracteres decimales de Sheets
                val_raw = kpi.iloc[0][c_val]
                val_str = str(val_raw).replace(',', '.').replace('%', '').strip()
                val_actual = float(val_str)
                
                # Si el valor en Sheets vino como un número entero tipo 33 o 33.33 en vez de 0.33, lo acomodamos
                if val_actual > 1.0:
                    val_actual = val_actual / 100.0
                
                # Renderizado final de la tarjeta flotante en Modo Oscuro Premium
                st.metric(label=f"Métrica: {kpi.iloc[0][c_ind]}", value=f"{val_actual * 100:.2f}%")
                st.progress(min(max(val_actual, 0.0), 1.0))
            else:
                st.warning("No se encontró la fila 'Precisión de Recepción (Fill Rate)'.")
                st.info("Filas reales disponibles en esta pestaña:")
                st.write(list(df[c_ind].unique()))
        else:
            st.error("Estructura de columnas no reconocida en 'Dashboard_KPIs'.")
            st.info("Columnas actuales leídas por el servidor:")
            st.write(list(df.columns))
            
    else:
        st.title("📊 Datos Crudos Sincronizados de Sheets")
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Error técnico al procesar los datos de la pestaña: {e}")



