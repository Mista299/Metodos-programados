#Maria Fernanda Atencia Oliva
#Michael Stiven Tabares Tobón

import sympy as sp
import pandas as pd

def diferencia_hacia_adelante(f_expr, x0, h, max_iterations=5):
    f_prime = sp.diff(f_expr,x)
    f_2prime = sp.diff(f_expr,x,2)
    errors = []
    valores = []
    hs = []
    for n in range(max_iterations):
        
        f_x_h = f_expr.subs(x, x0+h)
        f_x0 = f_expr.subs(x, x0)
        valor_final = (f_x_h.evalf() - f_x0.evalf())/h
        error = h*(f_2prime.subs(x,x0))/2
        error = round(error,6)
        valores.append(valor_final)
        errors.append(error)
        hs.append(h)
        h = h/10

    tabla_iteraciones = pd.DataFrame({
        'h': hs,
        'valor funcion': valores,
        'Error': errors
    })

    return tabla_iteraciones

def diferencia_hacia_atras(f_expr, x0, h, max_iterations=5):
    f_prime = sp.diff(f_expr,x)
    f_2prime = sp.diff(f_expr,x,2)
    errors = []
    valores = []
    hs = []
    for n in range(max_iterations):
        f_x_h = f_expr.subs(x, x0-h)
        f_x0 = f_expr.subs(x, x0)
        valor_final = (f_x0.evalf() - f_x_h.evalf())/h
        error = h*(f_2prime.subs(x,x0))/2
        error = round(error,6)
        valores.append(valor_final)
        errors.append(error)
        hs.append(h)
        h = h/10

    tabla_iteraciones = pd.DataFrame({
        'h': hs,
        'valor funcion': valores,
        'Error': errors
    })

    return tabla_iteraciones
def diferencia_centrada(f_expr, x0, h, max_iterations=5):
    f_prime = sp.diff(f_expr,x)
    f_3prime = sp.diff(f_expr,x,3)
    errors = []
    valores = []
    hs = []
    for n in range(max_iterations):
        f_x_h = f_expr.subs(x, x0-h)
        f_x_h_pos = f_expr.subs(x, x0+h)
        valor_final = (f_x_h_pos.evalf() - f_x_h.evalf())/(2*h)
        error = (h**2)*(f_3prime.subs(x,x0))/6
        error = round(error,6)
        valores.append(valor_final)
        errors.append(error)
        hs.append(h)
        h = h/10

    tabla_iteraciones = pd.DataFrame({
        'h': hs,
        'valor funcion': valores,
        'Error': errors
    })

    return tabla_iteraciones
def diferencia_5_puntos(f_expr, x0, h, max_iterations=5):
    f_5prime = sp.diff(f_expr, x, 5)  # para calcular el error
    errores = []
    valores = []
    hs = []

    for _ in range(max_iterations):
        fx_m2h = f_expr.subs(x, x0 - 2*h)
        fx_mh = f_expr.subs(x, x0 - h)
        fx_ph = f_expr.subs(x, x0 + h)
        fx_p2h = f_expr.subs(x, x0 + 2*h)

        valor_final = (-fx_p2h.evalf() + 8*fx_ph.evalf() - 8*fx_mh.evalf() + fx_m2h.evalf()) / (12*h)
        error = ((h**4)/30) * f_5prime.subs(x, x0)  # Error teórico
        error = round(error.evalf(), 6)
        
        valores.append(valor_final)
        errores.append(error)
        hs.append(h)
        h = h / 10

    tabla = pd.DataFrame({
        'h': hs,
        'valor funcion': valores,
        'Error': errores
    })

    return tabla


#Se añade la funcion y un punto
x = sp.symbols('x')
f_expr = sp.tan(x)
x0 = sp.pi/4
print(x0)
#----------------------------------#

print("---------diferencias hacia adelante----------")
tabla_iteraciones = diferencia_hacia_adelante(f_expr, x0, h=1)
print(tabla_iteraciones)
print("---------diferencias hacia atras----------")
tabla_iteraciones2 = diferencia_hacia_atras(f_expr, x0, h=1)
print(tabla_iteraciones2)
print("---------diferencias centradas----------")
tabla_iteraciones3 = diferencia_centrada(f_expr, x0, h=1)
print(tabla_iteraciones3)
print("---------diferencias centradas de 5 puntos----------")
tabla_5pt = diferencia_5_puntos(f_expr, x0, h=1)
print(tabla_5pt)