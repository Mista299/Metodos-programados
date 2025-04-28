import sympy as sp

def trapecio(f, a, b):
    """
    Regla del trapecio para aproximar la integral de f desde a hasta b.
    """
    return (b - a) * (f(a) + f(b)) / 2

# Ejemplo de uso:
import math
resultado = trapecio(math.sin, 0, math.pi)
print(f"Resultado aproximado: {resultado}")


def trapecio_compuesta(f, a, b, n):
    """
    Regla del trapecio compuesta para n subintervalos.
    """
    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)

    return (h / 2) * suma

# Ejemplo de uso:
resultado = trapecio_compuesta(math.sin, 0, math.pi, 100)
print(f"Resultado con 100 subintervalos: {resultado}")


def regla_simpson(f, f4, x0, x2):
    """
    Regla de Simpson (n=2) con estimación de error.
    f: función a integrar
    f4: cuarta derivada de f (para estimar el error)
    x0, x2: extremos del intervalo
    """
    h = (x2 - x0) / 2
    x1 = (x0 + x2) / 2

    aproximacion = (h / 3) * (f(x0) + 4 * f(x1) + f(x2))
    error = (h**5 / 90) * f4(x1) 

    return aproximacion - error

def regla_simpson_3_8(f, f4, x0, x3):
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
    error = (3 * h**5 / 80) * f4((x0 + x3) / 2)

    return aproximacion - error

x = sp.symbols('x')
# Definir la función simbólicamente
f_expr = sp.sin(x)
f4_expr = sp.diff(f_expr, x, 4)

# Convertir expresiones simbólicas a funciones numéricas
f = sp.lambdify(x, f_expr, modules=['math'])
f4_prime = sp.lambdify(x, f4_expr, modules=['math'])

# Simpson n=2
resultado_simpson = regla_simpson(f, f4_prime, 0, math.pi)
print(f"Resultado Simpson (n=2): {resultado_simpson}")

# Simpson 3/8 n=3
resultado_3_8 = regla_simpson_3_8(f, f4_prime, 0, math.pi)
print(f"Resultado Simpson 3/8 (n=3): {resultado_3_8}")

