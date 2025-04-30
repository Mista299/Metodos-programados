import sympy as sp
import math

def trapecio(f, f2_prime, a, b, e):
    """
    Regla del trapecio para aproximar la integral de f desde a hasta b.
    """
    x = sp.symbols('x')

    error = ((b - a)**3 / 12) * f2_prime(e)
    r = ((b - a) * (f(a) + f(b)) / 2)
    return [r, error]

import sympy as sp


def trapecio_compuesta(f, f2_prime, a, b, n, e):
    """
    Regla del trapecio compuesta para n subintervalos, con estimación de error.
    """
    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)

    r = (h / 2) * suma

    # Estimación del error usando la fórmula: -(b-a)/(12n^2) * f''(ξ)
    # Usamos el punto medio del intervalo para ξ
    error = ((b - a) / (12 * n**2)) * f2_prime(e)

    return [r, error]

    """
    Regla del trapecio compuesta para n subintervalos, con estimación de error.
    """
    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)

    r = (h / 2) * suma

    # Estimación del error usando la fórmula: -(b-a)/(12n^2) * f''(ξ)
    # Usamos el punto medio del intervalo para ξ
    xi = (a + b) / 2
    error = ((b - a) / (12 * n**2)) * f2_prime(xi)

    return [r, error]

    """
    Regla del trapecio compuesta para n subintervalos.
    """
    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)

    r = (h / 2) * suma
    return [r, error]


def regla_simpson(f, f4, x0, x2, e):
    """
    Regla de Simpson (n=2) con estimación de error.
    f: función a integrar
    f4: cuarta derivada de f (para estimar el error)
    x0, x2: extremos del intervalo
    """
    h = (x2 - x0) / 2
    x1 = (x0 + x2) / 2

    aproximacion = (h / 3) * (f(x0) + 4 * f(x1) + f(x2))
    error = (h**5 / 90) * f4(e) 

    return [aproximacion, error]

def regla_simpson_3_8(f, f4_prime, x0, x3, e):
    """
    Regla de 3/8 de Simpson (n=3) con estimación de error.
    f: función a integrar
    f4: cuarta derivada de f (para estimar el error)
    x0, x3: extremos del intervalo
    """
    h = (x3 - x0) / 3
    x1 = x0 + h
    x2 = x0 + 2 * h

    aproximacion = (3 * h / 8) * (f(x0) + 3*f(x1) + 3*f(x2) + f(x3))
    error = (3 * h**5 / 80) * f4_prime(e)

    return [aproximacion, error]

def regla_simpson_compuesta(f, f4_prime, a, b, n, e):
    """
    Regla de Simpson compuesta para n subintervalos (n debe ser par).
    f4_prime: cuarta derivada de f, para estimar el error.
    """
    if n % 2 != 0:
        raise ValueError("n debe ser par para aplicar la regla de Simpson compuesta.")

    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h
        peso = 4 if i % 2 != 0 else 2
        suma += peso * f(xi)

    resultado = (h / 3) * suma
    error = ((b - a) * h**4 / 180) * f4_prime(e)

    return [resultado, error]

def regla_punto_medio_compuesta(f, f2_prime, a, b, n, e):
    """
    Regla del punto medio compuesta con n subintervalos.
    f2_prime: segunda derivada de f, para estimar el error.
    """
    h = (b - a) / n
    suma = 0

    for i in range(n):
        xi = a + (i + 0.5) * h
        suma += f(xi)

    resultado = h * suma
    error = ((b - a) * h**2 / 24) * f2_prime(e)

    return [resultado, error]


x = sp.symbols('x')
# Definir la función simbólicamente
f_expr = sp.exp(-x**2)
f2_expr = sp.diff(f_expr, x, 4)
f4_expr = sp.diff(f_expr, x, 4)

f = sp.lambdify(x, f_expr, modules=['math'])
f2_prime = sp.lambdify(x, f2_expr, modules=['math'])
f4_prime = sp.lambdify(x, f4_expr, modules=['math'])



# Convertir expresiones simbólicas a funciones numéricas
resultado, error_t = trapecio(f, f2_prime, 0, 1, 0.5)
print("-----------------Trapecio simple-----------------")
print(f"Resultado aproximado: {resultado}")
print(f"error (Trapecio simple): {error_t}")

n = 100
resultado, error_tc = trapecio_compuesta(f, f2_prime, 0, 1, n, 0.5)
print("-----------------Trapecio compuesto-----------------")
print(f"Resultado con {n} subintervalos: {resultado}")
print(f"Error estimado (Trapecio compuesto): {error_tc}")


# Simpson n=2
print("-----------------Regla Simpson-----------------")
resultado_simpson, error_s = regla_simpson(f, f4_prime, 0, 1, 0.5)
print(f"Resultado Simpson (n=2): {resultado_simpson}")
print(f"Error estimado (Trapecio compuesto): {error_s}")

print("-----------------Regla Simpson 3/8-----------------")
# Simpson 3/8 n=3
resultado_3_8, error_s3_8 = regla_simpson_3_8(f, f4_prime, 0, 1, 0.5)
print(f"Resultado Simpson 3/8 (n=3): {resultado_3_8}")
print(f"Error estimado (Trapecio compuesto): {error_s3_8}")

print("-----------------Simpson compuesta-----------------")
resultado_s_comp, error_s_comp = regla_simpson_compuesta(f, f4_prime, 0, 1, 4, 0.5)
print(f"Resultado Simpson compuesta (n=4): {resultado_s_comp}")
print(f"Error estimado: {error_s_comp}")

print("-----------------Punto medio compuesta-----------------")
resultado_pm, error_pm = regla_punto_medio_compuesta(f, f2_prime, 0, 1, 6, 0.5)
print(f"Resultado Punto medio compuesta (n=6): {resultado_pm}")
print(f"Error estimado: {error_pm}")
