import streamlit as st
import pandas as pd

st.set_page_config(page_title="Logística Lean", layout="wide")

SHEET_ID = "1xaPnDFIBd0Lwy_Z7wVI-SdsxSq20wg7fKtLDypjsd4I"
URL = f"https://google.com{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=Dashboard_KPIs"

try:
    df = pd.read_csv(URL)
    st.sidebar.title("LOGÍSTICA LEAN")
    opcion = st.sidebar.radio("Agentes:", ["📦 Agente 1: Recepción", "🏠 Ver Datos Crudos"])
    
    if opcion == "📦 Agente 1: Recepción":
        st.title("📦 Agente 1 - Recepción")
        kpi = df[df['Indicador'].str.contains("Fill Rate", case=False, na=False)]
        val_actual = float(kpi.iloc['Valor Actual'].replace(',', '.')) if isinstance(kpi.iloc['Valor Actual'], str) else float(kpi.iloc['Valor Actual'])
        st.metric(label="Precisión de Recepción (Fill Rate)", value=f"{val_actual * 100:.2f}%")
        st.progress(min(max(val_actual, 0.0), 1.0))
    else:
        st.title("📊 Datos Crudos de Sheets")
        st.dataframe(df)
except Exception as e:
    st.error(f"Configura tu Sheets como 'Cualquier persona con el enlace puede ver'. Error: {e}")
