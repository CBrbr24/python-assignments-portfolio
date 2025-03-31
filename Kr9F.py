import sympy as sp

x, y = sp.symbols('x y')

# Define a function
f = x ** 2 + sp.sin(y)

# Differentiate f with respect to x
df_dx = sp.diff(f, x)

# Differentiate f with respect to y
df_dy = sp.diff(f, y)


g = sp.exp(x)*sp.sin(y) + y**3
dg_dx = sp.diff(g, x)
dg_dy = sp.diff(g, y)

print("The derivative with respect to x is ", dg_dx)
print("The derivative with respect to y is ", dg_dy)

def gradient (a, b):
    h = (x**2)*y + x*(y**2)
    h_0 = (a**2)*b + a*(b**2)

    dh_dx = sp.diff(h, x)
    dh_dy = sp.diff(h, y)

    dhxa = dh_dx.subs({x: a, y: b})
    dhyb = dh_dy.subs({x: a, y: b})

    grad_eq = h_0 + dhxa*(x-a) + dhyb*(y-b)

    return grad_eq

print(gradient(1, -1))


k = sp.ln(x**2 +y**2)
dk_dx = sp.diff(k, x)
dk_dy = sp.diff(k, y)

scnd_dk_dx = sp.diff(dk_dx, x)
scnd_dk_dy = sp.diff(dk_dy, y)
mixed_dk = sp.diff(dk_dx, y)

print("This is the second derivative with respect to x: ", scnd_dk_dx, "This is the second derivative with respect to y: ", scnd_dk_dy, "This is the mixed partial derivative:", mixed_dk)

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def ex_contour():
    j = x**3- 3*x*y + y**3

    j_func = sp.lambdify((x, y), j, 'numpy')

    x_vals = np.linspace(-3, 3, 400)
    y_vals = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = j_func(X, Y)

    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar()
    plt.title('Contour plot of $j(x, y) = x^3- 3xy + y^3$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()

def my_contour():
    t = x*y**2 + 2*x*y - y**3
    t_func = sp.lambdify((x, y), t, 'numpy')

    x_vals = np.linspace(-10, 6, 400)
    y_vals = np.linspace(-10, 6, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = t_func(X, Y)

    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar()
    plt.title('Contour plot of $t(x, y) = xy^2 + 2xy - y^3$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()

my_contour()


