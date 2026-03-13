import pandas as pd

def interpolar_estado(df, col_ref, valor):
    min_val = float(df[col_ref].iloc[0])
    max_val = float(df[col_ref].iloc[-1])
    
    if valor < min_val or valor > max_val:
        return None, None, None, f"El valor está fuera del rango (Válido: {min_val:0.7g} - {max_val:0.7g})."
        
    idx = df[col_ref].searchsorted(valor, side='right')
    if idx == len(df):
        idx = len(df) - 1
        
    fila_inf = df.iloc[idx - 1]
    fila_sup = df.iloc[idx]
    
    x1, x2 = fila_inf[col_ref], fila_sup[col_ref]
    factor = 0.0 if x2 == x1 else (valor - x1) / (x2 - x1)
    
    resultado = fila_inf + (fila_sup - fila_inf) * factor
    resultado[col_ref] = valor 
    
    return fila_inf, resultado, fila_sup, None