import streamlit as st
import pandas as pd

# 1. Cargar tus datos
# Asegúrate de que el archivo esté en la misma carpeta que app.py
df = pd.read_csv('Tabla_A17_Aire1.csv')

st.title("Calculadora de Propiedades: Aire (Tabla A-17)")

# 2. Configuración de la interfaz
col_ref = st.selectbox("¿Qué propiedad usas para buscar?", df.columns)
valor = st.number_input(f"Ingresa el valor de {col_ref} para interpolar", value=float(df[col_ref].iloc[0]))

# 3. Lógica de interpolación al presionar el botón
if st.button("Calcular"):
    # Buscar dónde caería el valor en la columna de referencia
    idx = df[col_ref].searchsorted(valor)
    
    # Validar rangos (para no intentar extrapolar fuera de la tabla)
    if idx == 0 or idx >= len(df):
        st.warning("El valor está fuera del rango de la tabla.")
    else:
        # Extraer las dos filas adyacentes
        fila_inf = df.iloc[idx - 1]
        fila_sup = df.iloc[idx]
        
        # Calcular el factor de interpolación
        # Fórmula: y = y1 + (y2 - y1) * ((x - x1) / (x2 - x1))
        x1, x2 = fila_inf[col_ref], fila_sup[col_ref]
        factor = (valor - x1) / (x2 - x1)
        
        # Crear la fila resultado
        resultado = fila_inf + (fila_sup - fila_inf) * factor
        resultado[col_ref] = valor # Mantener el valor exacto del input
        
        # 4. Mostrar el resultado
        st.subheader("Resultado de la Interpolación")
        # Creamos una tabla para mostrar el contexto visual
        res_df = pd.DataFrame([fila_inf, resultado, fila_sup], 
                              index=["Fila Inferior", "RESULTADO", "Fila Superior"])
        
        st.table(res_df)

# --- Sección de Referencia (Al final) ---
st.divider() # Una línea visual para separar
st.subheader("Tabla de Referencia Completa")
st.write("Puedes explorar todos los datos utilizados para el cálculo aquí abajo:")

# Mostramos la tabla completa con barra de desplazamiento
st.dataframe(df, use_container_width=True)