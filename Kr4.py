import matplotlib.pyplot as plt
import numpy as np


f = lambda x: x**2 

def gradient_descent(f, learning_rate, initial_point):
    def deriv(f, base_point):



        return (f(base_point + 10 ** (-10)) - f(base_point - 10 ** (-10))) / (2 * 10 ** (-10))
    x_coords = [initial_point]
    y_coords = [f(initial_point)]


    for i in range(100000):
        current_point = x_coords[i]

        gradient = deriv(f, current_point)
        next_point = current_point - learning_rate * gradient

        x_coords.append(next_point)
        y_coords.append(f(next_point))

        if (next_point - current_point)<(10 ** (-10)):
            break


    plot_range = np.linspace(min(x_coords) - 0.5, max(x_coords) + 0.5, 100000)
    function_range = [f(n) for n in plot_range]
    plt.plot(plot_range, function_range)
    plt.plot(x_coords, y_coords)
    plt.show()

    return round(x_coords[-1], 3), round(y_coords[-1], 3)

# returns last x_n and y_n, #rounded to three decimal places.



gradient_descent(f, 0.0001,0.5)
