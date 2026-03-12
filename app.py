import streamlit as st
import pandas as pd

# Mantenemos el lienzo expandido para tener espacio de maniobra
st.set_page_config(page_title="Fisikka - Aire", layout="wide")

# --- FUNCIÓN DE MÁRGENES ---
def crear_columnas_con_margen(porcentaje_margen):
    c = porcentaje_margen
    a = c
    b = 100.0 - (a + c)
    return st.columns([a, b, c])

# 1. Cargar tus datos
df = pd.read_csv('Tabla_A17_Aire1.csv')

nombres_bonitos = {
    df.columns[0]: "Temperatura T (K)",
    df.columns[1]: "Entalpía h (kJ/kg)",
    df.columns[2]: "Presión relativa Pᵣ",
    df.columns[3]: "Energía interna u (kJ/kg)",
    df.columns[4]: "Volumen relativo vᵣ",
    df.columns[5]: "Entropía s° (kJ/kg·K)"
}

# ==========================================
# 1. SECCIÓN SUPERIOR: Controles
# ==========================================
espacio_izq, col_superior, espacio_der = crear_columnas_con_margen(31.0)

with col_superior:
    st.title("Calculadora de Propiedades: Aire (Tabla A-17)")

    col_ref = st.selectbox(
        "¿Qué propiedad usas para buscar?", 
        df.columns,
        format_func=lambda x: nombres_bonitos.get(x, x) 
    )

    min_val = float(df[col_ref].iloc[0])
    max_val = float(df[col_ref].iloc[-1])

    st.markdown(f"**Ingresa el valor de {nombres_bonitos.get(col_ref, col_ref)} para interpolar:**")
    valor = st.number_input(
        "", 
        value=min_val,
        format="%0.7g",
        label_visibility="collapsed"
    )
    
    # GUARDAMOS EL ESTADO DEL BOTÓN Y SALIMOS DEL BLOQUE
    boton_calcular = st.button("Calcular")


# ==========================================
# 2. SECCIÓN INTERMEDIA: Resultados (Ancho independiente)
# ==========================================
# Al evaluar la variable afuera, recuperamos el lienzo completo
if boton_calcular:
    if valor < min_val or valor > max_val:
        # Si hay error, lo alineamos con la sección de arriba
        espacio_izq_err, col_error, espacio_der_err = crear_columnas_con_margen(31.0)
        with col_error:
            st.warning(f"El valor está fuera del rango de la tabla (Rango válido: {min_val:0.7g} - {max_val:0.7g}).")
    else:
        # Cálculos de interpolación
        idx = df[col_ref].searchsorted(valor, side='right')
        if idx == len(df):
            idx = len(df) - 1
            
        fila_inf = df.iloc[idx - 1]
        fila_sup = df.iloc[idx]
        
        x1, x2 = fila_inf[col_ref], fila_sup[col_ref]
        factor = 0.0 if x2 == x1 else (valor - x1) / (x2 - x1)
        
        resultado = fila_inf + (fila_sup - fila_inf) * factor
        resultado[col_ref] = valor 
        
        res_df = pd.DataFrame([fila_inf, resultado, fila_sup], 
                              index=["Fila Inferior", "RESULTADO", "Fila Superior"])
        
        res_df.rename(columns=nombres_bonitos, inplace=True)
        res_df_formateada = res_df.apply(lambda col: col.map(lambda x: f"{x:.7g}"))
        
        # --- NUEVOS MÁRGENES SOLO PARA LOS RESULTADOS ---
        # Cambia este 20.0 por el porcentaje que mejor te funcione
        margen_res_izq, col_resultados, margen_res_der = crear_columnas_con_margen(21.0)
        
        with col_resultados:
            st.subheader("Resultado de la Interpolación")
            st.latex(r"y = y_1 + \frac{y_2 - y_1}{x_2 - x_1} (x - x_1)")
            
            st.table(res_df_formateada)
            
            # TEXTO PEQUEÑO AGREGADO AQUÍ
            st.caption("""
            **Notas sobre el programa:**
            1. La interpolación asume un comportamiento lineal entre los estados termodinámicos adyacentes.
            2. Los valores mostrados mantienen una precisión de 7 cifras significativas.
            3. Si el valor coincide exactamente con un punto tabulado, el factor de interpolación es cero.
            """)

st.divider()

# ==========================================
# 3. SECCIÓN INFERIOR: Tabla de referencia
# ==========================================
margen_izq, col_tabla, margen_der = crear_columnas_con_margen(21.0)

with col_tabla:
    st.subheader("Tabla de Referencia Completa")
    df_visual = df.copy()
    df_visual.rename(columns=nombres_bonitos, inplace=True)
    
    st.table(df_visual.style.format("{:.7g}"))


## Para cargar el Código:
# git add .
# git commit -m "Actualización: Versión 1.3"
# git push