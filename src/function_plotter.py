import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import tkinter as tk
from tkinter import simpledialog

def plot_functions(functions):
    """
    Plot the growth of multiple mathematical functions.
    :param functions: List of sympy expressions
    """
    n_vals = np.linspace(1, 100, 400)
    plt.figure()

    for func in functions:
        f_lambdified = sp.lambdify('n', func, 'numpy')
        plt.plot(n_vals, f_lambdified(n_vals), label=str(func))

    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.title('Function Growth Comparison')

    plt.legend()
    plt.grid(True)

    plt.gcf().canvas.mpl_connect('key_press_event', lambda event: update_limits(event, plt))

    plt.show()

def update_limits(event, plt):
    """
    Update x and y limits based on key presses.
    :param event: Key press event
    :param plt: The matplotlib pyplot module
    """
    if event.key == 'y':
        y_max = simpledialog.askfloat("Input", "Enter new y_max:", parent=plt.get_current_fig_manager().window)
        if y_max is not None:
            plt.ylim(0, y_max)

    elif event.key == 'x':
        x_min = simpledialog.askfloat("Input", "Enter new x_min:", parent=plt.get_current_fig_manager().window)
        x_max = simpledialog.askfloat("Input", "Enter new x_max:", parent=plt.get_current_fig_manager().window)
        if x_min is not None and x_max is not None:
            plt.xlim(x_min, x_max)

    plt.draw()

