import sympy as sp

# Definir el símbolo x
x = sp.symbols('x')

# Crear una expresión simbólica f(x) = x^2 + 2x + 1
f_expr = x**2 + 2*x + 1
print(f_expr)

# Convertir la expresión simbólica en una función numérica utilizando lambdify
f_numeric = sp.lambdify(x, f_expr, 'numpy')

resultado1 = f_numeric(0)
resultado2 = f_numeric(2)
resultado3 = f_numeric(3)

r1 = f_expr.evalf(2)
print("--------con evalf()---------")
print(r1)
print("--------con lambdify()---------")
print(resultado1)
print(resultado2)
print(resultado3)




