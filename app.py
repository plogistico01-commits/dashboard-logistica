elif opcion == "🚜 Agente 2: Picking":
    st.markdown("<h1>🚜 Agente 2 - Optimización de Rutas (Picking)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 14px;'>Filtro de pedidos pendientes clasificados automáticamente por ubicación física</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Conexión directa a la pestaña de Picking de producción mediante su GID
    URL_PICKING = "https://google.com"
    
    try:
        df_picking = pd.read_csv(URL_PICKING, encoding='utf-8')
        # Estandarizamos nombres de columnas por si se pegan con espacios o variaciones en minúsculas
        df_picking.columns = df_picking.columns.str.strip().str.upper()
    except Exception:
        # Respaldo inmediato en caso de error de red sin caída del servidor
        datos_picking_crudos = {
            'PEDIDO': ['#1024', '#1025', '#1026', '#1027', '#1028'],
            'PASILLO': ['Pasillo B', 'Pasillo A', 'Pasillo C', 'Pasillo A', 'Pasillo B'],
            'ESTANTERÍA': ['Nivel 3', 'Nivel 1', 'Nivel 2', 'Nivel 4', 'Nivel 1'],
            'ARTÍCULO': ['Filtros', 'Bujías', 'Soportes', 'Pastillas', 'Correas'],
            'CANTIDAD': [5, 12, 3, 8, 4]
        }
        df_picking = pd.DataFrame(datos_picking_crudos)

    # Variables dinámicas para ordenación según las columnas estandarizadas
    # Asegúrate de que en el Excel las columnas se llamen 'PASILLO' y 'ESTANTERÍA' (o adáptalas aquí)
    col_pasillo = 'PASILLO' if 'PASILLO' in df_picking.columns else df_picking.columns[1]
    col_estanteria = 'ESTANTERÍA' if 'ESTANTERÍA' in df_picking.columns else df_picking.columns[2]
    
    # Lógica de Negocio Lean: Ordenación secuencial por ubicación en almacén
    df_optimizado = df_picking.sort_values(by=[col_pasillo, col_estanteria]).reset_index(drop=True)
    
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        st.metric(label="Eficiencia de la Ruta Activa", value="85.00%", delta="-13.00% vs Objetivo (98%)")
    with p_col2:
        st.markdown("""
            <div class='ruta-optima'>
                ✅ <strong>Ruta Logística Secuencial:</strong> Filas reorganizadas automáticamente de extremo a extremo del pasillo para minimizar desplazamientos nulos de los operarios.
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><h3>📋 Hoja de Ruta de Picking Generada (Tiempo Real)</h3>", unsafe_allow_html=True)
    st.dataframe(df_optimizado, use_container_width=True)














