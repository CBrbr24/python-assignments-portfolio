





def gradient_descent(x0, y0, f, grad_f, alpha, num_iterations):
    #Parameters:
    #x0, y0: Initial point for the descent.
    #f: a function of two variables
    #grad_f: the gradient of f
    #alpha: Learning rate.
   # num_iterations: Number of iterations to perform.
   # Returns:
   # (x, y): The coordinates of the final point after gradient descent.


    x, y = x0, y0
    for i in range(num_iterations):
        grad_x, grad_y = grad_f(x), grad_f(y)

        xpro = xpro - alpha * grad_x
        ypro = ypro - alpha * grad_y

    x = xpro
    y = ypro
    return x, y


def fun_1(x,y):
    return x**2+y**2

def grad_f_1(x,y):
    grad_x = 2*x
    grad_y = 2*y
    return grad_x, grad_y


import numpy as np

def fun_2(x,y):
    return 1 - np.exp(-x ** 2 - (y - 2) ** 2) - 2 * np.exp(-x ** 2 - (y + 2) ** 2)

def grad_f_2(x,y):
    grad_x = 2*x*np.exp(-x ** 2 - (y - 2) ** 2) + 4*x*np.exp(-x ** 2 - (y + 2) ** 2)
    grad_y = 2*(y-2)*np.exp(-x ** 2 - (y + 2) ** 2) + 4*(y+2)*np.exp(-x ** 2 - (y + 2) ** 2)
    return grad_x, grad_y