#para encontrar raices

#Maria Fernanda Atencia Oliva
#Michael Stiven Tabares Tobón

import pandas as pd
import numpy as np

def secante(f, x0, x1, tol=1e-6, max_iter=100):

    lista_x0 = []
    lista_x1 = []
    lista_fx0 = []
    lista_fx1 = []
    lista_x2 = []
    lista_error = []

    for _ in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            print("División por cero detectada.")
            break

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs((x2 - x1) / x2) * 100 if x2 != 0 else 0

        lista_x0.append(x0)
        lista_x1.append(x1)
        lista_fx0.append(fx0)
        lista_fx1.append(fx1)
        lista_x2.append(x2)
        lista_error.append(error)

        if error < tol:
            break

        x0, x1 = x1, x2

    # Crear el DataFrame
    df = pd.DataFrame({
        'xi-1': lista_x0,
        'xi': lista_x1,
        'f(xi-1)': lista_fx0,
        'f(xi)': lista_fx1,
        'xi+1': lista_x2,
        'error (%)': lista_error
    })

    return x2, df

def f(x):
    return np.cos(x)

raiz, tabla_resultados = secante(f, x0=np.pi/4, x1=2, tol=1e-5)
print("Raíz aproximada:", raiz)
print("\nTabla de iteraciones:")
print(tabla_resultados)
