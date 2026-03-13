# Archivo: idiomas.py

textos = {
    "Español": {
        # --- GENERALES (Usados en todas las tablas) ---
        "titulo": "Calculadora de Propiedades Termodinámicas",
        "selecciona_tabla": "Selecciona la tabla con la que deseas trabajar:",
        "info_selecciona": "👆 Por favor, selecciona una tabla del menú superior para comenzar.",
        "preg_prop": "¿Qué propiedad usas para buscar?",
        "ingresa_val": "**Ingresa el valor de {prop} para interpolar:**",
        "btn_calc": "Calcular",
        "res_titulo": "Resultado de la Interpolación",
        "fila_inf": "Fila Inferior",
        "fila_res": "RESULTADO",
        "fila_sup": "Fila Superior",
        "tabla_ref": "Tabla de Referencia Completa",
        "notas": """
        **Notas sobre el programa:**
        1. La interpolación asume un comportamiento lineal entre los estados termodinámicos adyacentes.
        2. Los valores mostrados mantienen una precisión de 7 cifras significativas.
        3. Si el valor coincide exactamente con un punto tabulado, el factor de interpolación es cero.
        """,
        
        # --- MENÚ LATERAL ---
        "menu_nombres": {
            "a4": "Tabla A-4: Agua saturada (Temperatura)",
            "a5": "Tabla A-5: Agua saturada (Presión)",
            "a6": "Tabla A-6: Agua sobrecalentada",
            "a11": "Tabla A-11: R-134a saturado (Temperatura)",
            "a12": "Tabla A-12: R-134a saturado (Presión)",
            "a13": "Tabla A-13: R-134a sobrecalentado",
            "a17": "Tabla A-17: Propiedades de gas ideal del aire"
        },

        # --- ESPECÍFICOS: TABLA A-17 ---
        "A17_cols": [
            "Temperatura\nT (K)", "Entalpía\nh (kJ/kg)", "Presión relativa\nPᵣ", 
            "Energía interna\nu (kJ/kg)", "Volumen relativo\nvᵣ", "Entropía\ns° (kJ/kg·K)"
        ]
    },
    "English": {
        # --- GENERALES ---
        "titulo": "Thermodynamic Properties Calculator",
        "selecciona_tabla": "Select the table you want to work with:",
        "info_selecciona": "👆 Please select a table from the top menu to begin.",
        "preg_prop": "Which property are you using to search?",
        "ingresa_val": "**Enter the value of {prop} to interpolate:**",
        "btn_calc": "Calculate",
        "res_titulo": "Interpolation Result",
        "fila_inf": "Lower Row",
        "fila_res": "RESULT",
        "fila_sup": "Upper Row",
        "tabla_ref": "Complete Reference Table",
        "notas": """
        **Program Notes:**
        1. The interpolation assumes linear behavior between adjacent thermodynamic states.
        2. The displayed values maintain a precision of 7 significant figures.
        3. If the value exactly matches a tabulated point, the interpolation factor is zero.
        """,
        
        # --- MENÚ LATERAL ---
        "menu_nombres": {
            "a4": "Table A-4: Saturated Water (Temperature)",
            "a5": "Table A-5: Saturated Water (Pressure)",
            "a6": "Table A-6: Superheated Water",
            "a11": "Table A-11: Saturated R-134a (Temperature)",
            "a12": "Table A-12: Saturated R-134a (Pressure)",
            "a13": "Table A-13: Superheated R-134a",
            "a17": "Table A-17: Ideal Gas Properties of Air"
        },

        # --- ESPECÍFICOS: TABLA A-17 ---
        "A17_cols": [
            "Temperature\nT (K)", "Enthalpy\nh (kJ/kg)", "Relative pressure\nPᵣ", 
            "Internal energy\nu (kJ/kg)", "Relative volume\nvᵣ", "Entropy\ns° (kJ/kg·K)"
        ]
    },
    "Français": {
        # --- GENERALES ---
        "titulo": "Calculatrice de Propriétés Thermodynamiques",
        "selecciona_tabla": "Sélectionnez la table avec laquelle vous souhaitez travailler :",
        "info_selecciona": "👆 Veuillez sélectionner une table dans le menu supérieur pour commencer.",
        "preg_prop": "Quelle propriété utilisez-vous pour chercher ?",
        "ingresa_val": "**Entrez la valeur de {prop} pour interpoler :**",
        "btn_calc": "Calculer",
        "res_titulo": "Résultat de l'Interpolation",
        "fila_inf": "Ligne Inférieure",
        "fila_res": "RÉSULTAT",
        "fila_sup": "Ligne Supérieure",
        "tabla_ref": "Tableau de Référence Complet",
        "notas": """
        **Notes sur le programme :**
        1. L'interpolation suppose un comportement linéaire entre les états thermodynamiques adjacents.
        2. Les valeurs affichées conservent une précision de 7 chiffres significatifs.
        3. Si la valeur correspond exactement à un point tabulé, le facteur d'interpolation est nul.
        """,
        
        # --- MENÚ LATERAL ---
        "menu_nombres": {
            "a4": "Tableau A-4 : Eau saturée (Température)",
            "a5": "Tableau A-5 : Eau saturée (Pression)",
            "a6": "Tableau A-6 : Eau surchauffée",
            "a11": "Tableau A-11 : R-134a saturé (Température)",
            "a12": "Tableau A-12 : R-134a saturé (Pression)",
            "a13": "Tableau A-13 : R-134a surchauffé",
            "a17": "Tableau A-17 : Propriétés de gaz idéal de l'air"
        },

        # --- ESPECÍFICOS: TABLA A-17 ---
        "A17_cols": [
            "Température\nT (K)", "Enthalpie\nh (kJ/kg)", "Pression relative\nPᵣ", 
            "Énergie interne\nu (kJ/kg)", "Volume relatif\nvᵣ", "Entropie\ns° (kJ/kg·K)"
        ]
    }
}