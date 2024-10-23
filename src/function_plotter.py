import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def plot_functions(functions):
    """
    Plot the growth of multiple mathematical functions.
    :param functions: List of sympy expressions
    """
    n_vals = np.linspace(1, 100, 400)  # Range of n values to plot
    for func in functions:
        f_lambdified = sp.lambdify('n', func, 'numpy')
        plt.plot(n_vals, f_lambdified(n_vals), label=str(func))

    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.title('Function Growth Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


