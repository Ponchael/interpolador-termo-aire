import streamlit as st
import pandas as pd

# 1. Cargar tus datos
df = pd.read_csv('Tabla_A17_Aire1.csv')

# --- TRADUCTOR UNICODE ---
# Usamos caracteres especiales (como ᵣ y °) que Streamlit y las tablas sí entienden nativamente.
nombres_bonitos = {
    df.columns[0]: "T (K) | Temperatura",
    df.columns[1]: "h (kJ/kg) | Entalpía",
    df.columns[2]: "Pᵣ | Presión relativa",
    df.columns[3]: "u (kJ/kg) | Energía interna",
    df.columns[4]: "vᵣ | Volumen relativo",
    df.columns[5]: "s° (kJ/kg·K) | Entropía"
}

st.title("Calculadora de Propiedades: Aire (Tabla A-17)")

# 2. Configuración de la interfaz usando format_func
# format_func toma el nombre crudo de la columna y busca su versión bonita en el diccionario
col_ref = st.selectbox(
    "¿Qué propiedad usas para buscar?", 
    df.columns,
    format_func=lambda x: nombres_bonitos.get(x, x) 
)

min_val = float(df[col_ref].iloc[0])
max_val = float(df[col_ref].iloc[-1])

# El texto del input también usa el nombre bonito
st.markdown(f"**Ingresa el valor de {nombres_bonitos.get(col_ref, col_ref)} para interpolar:**")
valor = st.number_input(
    "", # Dejamos la etiqueta vacía porque ya la pusimos arriba con st.markdown
    value=min_val,
    format="%0.7g",
    label_visibility="collapsed"
)

# 3. Lógica de interpolación
if st.button("Calcular"):
    if valor < min_val or valor > max_val:
        st.warning(f"El valor está fuera del rango de la tabla (Rango válido: {min_val:0.7g} - {max_val:0.7g}).")
    else:
        idx = df[col_ref].searchsorted(valor, side='right')
        if idx == len(df):
            idx = len(df) - 1
            
        fila_inf = df.iloc[idx - 1]
        fila_sup = df.iloc[idx]
        
        x1, x2 = fila_inf[col_ref], fila_sup[col_ref]
        
        if x2 == x1:
            factor = 0.0
        else:
            factor = (valor - x1) / (x2 - x1)
        
        resultado = fila_inf + (fila_sup - fila_inf) * factor
        resultado[col_ref] = valor 
        
        # 4. Mostrar el resultado
        st.subheader("Resultado de la Interpolación")
        
        # Mostramos la fórmula de interpolación lineal para darle rigor técnico
        st.latex(r"y = y_1 + \frac{y_2 - y_1}{x_2 - x_1} (x - x_1)")
        
        res_df = pd.DataFrame([fila_inf, resultado, fila_sup], 
                              index=["Fila Inferior", "RESULTADO", "Fila Superior"])
        
        # Le cambiamos los nombres a las columnas de la tabla final para que se vean bien
        res_df.rename(columns=nombres_bonitos, inplace=True)
        res_df_formateada = res_df.apply(lambda col: col.map(lambda x: f"{x:.7g}"))
        
        st.table(res_df_formateada)

# --- Sección de Referencia ---
st.divider()
st.subheader("Tabla de Referencia Completa")

# Creamos una copia visual de la tabla maestra para cambiarle los títulos sin afectar los cálculos
df_visual = df.copy()
df_visual.rename(columns=nombres_bonitos, inplace=True)
st.dataframe(df_visual.style.format("{:.7g}"), use_container_width=True)