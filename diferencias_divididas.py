#Maria Fernanda Atencia Oliva
#Michael Stiven Tabares Tobón

import pandas as pd
import numpy as np
import sympy as sp

def diferencias_divididas(x, y):
    n = len(x)
    # ordenes[j][i] contendrá f[x_i, x_{i+1}, …, x_{i+j}]
    ordenes = [[] for _ in range(n)]
    ordenes[0] = y.copy()       # Orden 0: f[x_i] = y[i]

    for j in range(1, n):       # Para cada orden j = 1, 2, …, n-1 - primera formula, segunda formula, etc
        for i in range(n - j):  # Hay n–j valores de este orden
            # Fórmula: (f[... en orden j-1 en i+1] – f[... en orden j-1 en i]) / (x[i+j] - x[i])
            numerador   = ordenes[j - 1][i + 1] - ordenes[j - 1][i]
            denominador = x[i + j] - x[i]
            valor       = numerador / denominador
            ordenes[j].append(valor)
        # Relleno con None para alinear la tabla (opcional, solo para mostrar)
        ordenes[j] += [None] * j

    # Construye un DataFrame para presentar:
    data = {'x': x}
    for j in range(n):
        data[f'Orden {j}'] = ordenes[j]

    return pd.DataFrame(data)
#----------------entradas-----------------#
def f(x):
    return np.log(2 * x)


x_vals = [1.0, 1.3, 1.6, 1.9, 2.2]
#------------------------------------------#
y_vals = [ f(x) for x in x_vals]
#------------------------------------------#

# Construir la tabla
tabla = diferencias_divididas(x_vals, y_vals)


# Obtener coeficientes ai
coeficientes = [round(float(tabla[f'Orden {j}'][0]), 2) for j in range(len(x_vals))]

# Construcción simbólica del polinomio (usando sympy)
x_sym = sp.symbols('x')
polinomio = coeficientes[0]
terminos = [f"{coeficientes[0]}"]

for j in range(1, len(coeficientes)):
    producto = 1
    term_text = f"{coeficientes[j]}"
    for i in range(j):
        producto *= (x_sym - x_vals[i])
        term_text += f"*(x - {x_vals[i]})"
    polinomio += coeficientes[j] * producto
    terminos.append(term_text)

# Mostrar resultados
print("\nTabla de diferencias divididas:")
print(tabla)

print("\nCoeficientes del polinomio interpolante:")
print(coeficientes)

print("\nPolinomio interpolante (forma simbólica):")
print(sp.expand(polinomio))

print("\nPolinomio interpolante (forma explícita con coeficientes):")
print(" + ".join(terminos))
