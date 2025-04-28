
#Método de Gauss-seidel, hecho por
#Maria Fernanda Atencia Oliva
#Michael Stiven Tabares Tobón

import sympy as sp
import numpy as np
import pandas as pd


def isSimetric(A):
    if A.shape[0] != A.shape[1]:
        return False  # Si no es cuadrada, no puede ser simétrica

    for i in range(len(A)):
        for j in range(i, len(A)):  
            if A[i][j] != A[j][i]:
                return False 

    return True 

def isDominant(A):
    for i in range(0, len(A)):
        sum = 0
        for j in range(0, len(A)):
            if i != j:
                sum += A[i][j]
                if not (abs(A[i][i]) > abs(sum)):
                    return False
    return True

def isPositive(A):
    z = vector_aleatorio(len(A), -9, 9)
    if z.T @ A @ z > 0:
        return True
    return False

def vector_aleatorio(tamano, min_valor=0, max_valor=1):

    vector = np.random.uniform(min_valor, max_valor, tamano)
    return vector

def gauss_seidel(x1_sol, x2_sol, x3_sol, tol=0.001, max_iter=200):
    # Valores iniciales
    x1_val, x2_val, x3_val = 0, 0, 0
    iteraciones = []

    for i in range(max_iter):
        x1_prev, x2_prev, x3_prev = x1_val, x2_val, x3_val

        x1_val = x1_sol.subs({x2: x2_val, x3: x3_val})
        x2_val = x2_sol.subs({x1: x1_val, x3: x3_val})
        x3_val = x3_sol.subs({x1: x1_val, x2: x2_val})

        diff_vector = np.array([float(x1_val - x1_prev), float(x2_val - x2_prev), float(x3_val - x3_prev)])

        error = np.linalg.norm(diff_vector)

        iteraciones.append([i + 1, float(x1_val), float(x2_val), float(x3_val), float(error)])

        if error < tol:
            break

    columnas = ['Iteración', 'x1', 'x2', 'x3', 'Error']
    tabla_iteraciones = pd.DataFrame(iteraciones, columns=columnas)
    return tabla_iteraciones



# Definir las variables simbólicas
x1, x2, x3 = sp.symbols('x1 x2 x3')

# Pedir ecuaciones al usuario
ecuacion1 = 4*x1 - 0.2*x2 - 0.1*x3
ecuacion2 = 0.2*x1 + 5*x2 - 0.1*x3
ecuacion3 = 0.1*x1 - 0.4*x2 - 7*x3

resultado1 = 6.5
resultado2 = -12.2
resultado3 = 57.5

ecuacion1 = sp.Eq(ecuacion1, resultado1)
ecuacion2 = sp.Eq(ecuacion2, resultado2)
ecuacion3 = sp.Eq(ecuacion3, resultado3)


A, b = sp.linear_eq_to_matrix([ecuacion1, ecuacion2, ecuacion3], [x1, x2, x3])
A = np.array(A.tolist(), dtype=float)
b = np.array(b.tolist(), dtype=float)
print("La matriz a partir del sistema de ecuaciones es:")
sp.pprint(A)
print("El vector b es:")
sp.pprint(b)

x1_sol = sp.solve(ecuacion1, x1)[0]
x2_sol = sp.solve(ecuacion2, x2)[0]
x3_sol = sp.solve(ecuacion3, x3)[0]

# Mostrar las ecuaciones despejadas
print(f"x1 despejada: {x1_sol}")
print(f"x2 despejada: {x2_sol}")
print(f"x3 despejada: {x3_sol}")

print("--------------verificando cumplimiento de las pautas de convergencia:--------------")

if isSimetric(A) and isDominant(A):
    print("Es Simetrica?")
    print(isSimetric(A))  # Debería imprimir True
    print("Es dominante?")
    print(isDominant(A))  # Debería imprimir True
    print("--------------Iniciando Iteraciones--------------")
    tabla_resultados = gauss_seidel(x1_sol, x2_sol, x3_sol)
    print(tabla_resultados)
else:
    print("La matriz A del sistema de ecuaciones no cumple con Simetria o diagonalmente dominante")



print("---------prueba sin condiciones de simetria:----------")
print("Es Simetrica?")
print(isSimetric(A))  # Debería imprimir True
print("Es dominante?")
print(isDominant(A))  # Debería imprimir True
tabla_resultados = gauss_seidel(x1_sol, x2_sol, x3_sol)
print(tabla_resultados)
