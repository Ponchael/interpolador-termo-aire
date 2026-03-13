# Archivo: app.py
import streamlit as st
import idiomas
from vistas import t_a4, t_a5, t_a6, t_a11, t_a12, t_a13, t_a17 

st.set_page_config(page_title="Fisikka", layout="wide")

# ==========================================
# 1. CONTROLES SUPERIORES (Idioma)
# ==========================================
col_vacia, col_idioma = st.columns([8, 2])
with col_idioma:
    idioma_seleccionado = st.selectbox("🌐 Language", ["Español", "English", "Français"], label_visibility="collapsed")

t = idiomas.textos[idioma_seleccionado]
st.title(t["titulo"])

# ==========================================
# 2. MENÚ PRINCIPAL MULTIFILA
# ==========================================
# Extraemos la lista de nombres
opciones_menu = list(t["menu_nombres"].values())

# st.pills dibuja botones ovalados que se acomodan en varias filas si es necesario.
# Ponemos la tabla A-17 como la opción seleccionada por defecto.
tabla_elegida = st.pills(
    t["selecciona_tabla"], 
    opciones_menu, 
    default=t["menu_nombres"]["a17"]
)

st.divider() # Una línea sutil para separar el menú de la calculadora

# ==========================================
# 3. ENRUTADOR (Dibuja la vista elegida)
# ==========================================
# Si el usuario no ha seleccionado nada (desmarcó la píldora), le pedimos que elija una
if not tabla_elegida:
    # Llamamos al texto desde el diccionario
    st.info(t["info_selecciona"])
else:
    if tabla_elegida == t["menu_nombres"]["a4"]:
        t_a4.mostrar(t)
    elif tabla_elegida == t["menu_nombres"]["a5"]:
        t_a5.mostrar(t)
    elif tabla_elegida == t["menu_nombres"]["a6"]:
        t_a6.mostrar(t)
    elif tabla_elegida == t["menu_nombres"]["a11"]:
        t_a11.mostrar(t)
    elif tabla_elegida == t["menu_nombres"]["a12"]:
        t_a12.mostrar(t)
    elif tabla_elegida == t["menu_nombres"]["a13"]:
        t_a13.mostrar(t)
    elif tabla_elegida == t["menu_nombres"]["a17"]:
        t_a17.mostrar(t)


## Para cargar el Código:
# git add .
# git commit -m "Actualización: Versión 1.3"
# git push