import pandas as pd

import pandas as pd

def diferencias_divididas(x, y):
    n = len(x)

    # Cada orden será una lista
    ordenes = [[] for _ in range(n)]
    ordenes[0] = y.copy()  # Orden 0 son los valores de f(x)

    # Calcular ordenes superiores
    for j in range(1, n):
        for i in range(n - j):
            numerador = ordenes[j - 1][i + 1] - ordenes[j - 1][i]
            denominador = x[i + j] - x[i]
            valor = numerador / denominador
            ordenes[j].append(valor)
        # Rellenamos con None para que todas las listas tengan el mismo largo
        ordenes[j] += [None] * j

    # Crear diccionario con datos para el DataFrame
    data = {'x': x}
    for j in range(n):
        data[f'Orden {j}'] = ordenes[j]

    # Crear el DataFrame directamente
    tabla = pd.DataFrame(data)
    return tabla


x = [1, 2, 4, 7]
y = [3, 6, 9, 15]  # Por ejemplo, puede ser f(x) = 2x + 1 o algo más complejo

tabla_dd = diferencias_divididas(x, y)
print("Tabla de diferencias divididas:")
print(tabla_dd)
