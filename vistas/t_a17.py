# Archivo: vistas/t_a17.py
import streamlit as st
import pandas as pd
import calculos

def crear_columnas_con_margen(porcentaje_margen):
    c = porcentaje_margen
    a = c
    b = 100.0 - (a + c)
    return st.columns([a, b, c])

def mostrar(t):
    df = pd.read_csv('Tabla_A17_Aire1.csv')
    nombres_bonitos = {df.columns[i]: t["A17_cols"][i] for i in range(6)}

    # ==========================================
    # 1. EL "DISCO DURO" DE ESTA TABLA
    # ==========================================
    # Creamos un bloque de memoria seguro que Streamlit no puede borrar al cambiar de pestaña
    if 'mem_a17' not in st.session_state:
        st.session_state['mem_a17'] = {
            'propiedad': df.columns[0],
            'valor': float(df[df.columns[0]].iloc[0]),
            'resultados': None
        }
    
    # Creamos un apodo corto para no escribir tanto
    mem = st.session_state['mem_a17']

    espacio_izq, col_superior, espacio_der = crear_columnas_con_margen(25.0)
    
    with col_superior:
        st.subheader(t["menu_nombres"]["a17"])
        
        # --- RECUPERAR LA PROPIEDAD SELECCIONADA ---
        # Buscamos en qué posición está la propiedad que teníamos guardada
        idx_prop = list(df.columns).index(mem['propiedad']) if mem['propiedad'] in df.columns else 0
        
        col_ref = st.selectbox(
            t["preg_prop"], 
            df.columns, 
            index=idx_prop, 
            format_func=lambda x: nombres_bonitos.get(x, x).replace('\n', ' — '), 
            
            # MAGIA AQUÍ: Pegamos un texto traducido a la llave. 
            # Si el idioma cambia, la llave cambia, y el widget se reinicia limpio.
            key=f"ref_a17_{t['preg_prop']}" 
        )
        mem['propiedad'] = col_ref # Si el usuario la cambia, actualizamos el disco duro
        
        min_val = float(df[col_ref].iloc[0])
        
        # --- RECUPERAR EL NÚMERO INGRESADO ---
        st.markdown(t["ingresa_val"].format(prop=nombres_bonitos.get(col_ref, col_ref).replace('\n', ' ')))
        
        # Validación de seguridad: si cambias de T a Pᵣ, el mínimo cambia. Evitamos errores.
        if mem['valor'] < min_val:
            mem['valor'] = min_val

        valor = st.number_input(
            "", 
            value=mem['valor'], # Le inyectamos el último número guardado
            format="%0.7g", 
            label_visibility="collapsed", 
            key="val_a17"
        )
        mem['valor'] = valor # Si el usuario teclea algo nuevo, actualizamos el disco duro

        boton_calcular = st.button(t["btn_calc"], key="btn_a17")

    # ==========================================
    # 2. CÁLCULO Y GUARDADO DE RESULTADOS
    # ==========================================
    if boton_calcular:
        fila_inf, resultado, fila_sup, error = calculos.interpolar_estado(df, col_ref, valor)
        # Guardamos el "paquete" de resultados en el disco duro
        mem['resultados'] = {
            'fila_inf': fila_inf,
            'resultado': resultado,
            'fila_sup': fila_sup,
            'error': error
        }

    # ==========================================
    # 3. DIBUJAR LOS RESULTADOS (Desde el disco duro)
    # ==========================================
    # Ya no dependemos del botón. Si hay resultados guardados, los dibujamos.
    if mem['resultados'] is not None:
        datos = mem['resultados']
        error = datos['error']
        
        if error:
            _, col_error, _ = crear_columnas_con_margen(31.0)
            with col_error: st.warning(error)
        else:
            fila_inf = datos['fila_inf']
            resultado = datos['resultado']
            fila_sup = datos['fila_sup']
            
            res_df = pd.DataFrame([fila_inf, resultado, fila_sup], index=[t["fila_inf"], t["fila_res"], t["fila_sup"]])
            res_df.rename(columns=nombres_bonitos, inplace=True)
            res_df_formateada = res_df.apply(lambda col: col.map(lambda x: f"{x:.7g}"))
            res_df_formateada.columns = pd.MultiIndex.from_tuples([col.split('\n') for col in res_df_formateada.columns])
            
            _, col_resultados, _ = crear_columnas_con_margen(21.0)
            with col_resultados:
                st.subheader(t["res_titulo"])
                st.latex(r"y = y_1 + \frac{y_2 - y_1}{x_2 - x_1} (x - x_1)")
                st.table(res_df_formateada)
                st.caption(t["notas"])

    st.divider()
    _, col_tabla, _ = crear_columnas_con_margen(21.0)
    with col_tabla:
        st.subheader(t["tabla_ref"])
        df_visual = df.copy()
        df_visual.rename(columns=nombres_bonitos, inplace=True)
        df_visual.columns = pd.MultiIndex.from_tuples([col.split('\n') for col in df_visual.columns])
        st.table(df_visual.style.format("{:.7g}"))