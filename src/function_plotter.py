import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.animation import FuncAnimation
import seaborn as sns

def plot_functions(functions):
    """
    Plot the growth of multiple mathematical functions.
    :param functions: List of sympy expressions
    """
    # Set Seaborn style
    sns.set(style="whitegrid")

    n_vals = np.linspace(1, 100, 400)
    fig, ax = plt.subplots(figsize=(10, 6))

    lines = []
    for func in functions:
        f_lambdified = sp.lambdify('n', func, 'numpy')
        line, = ax.plot([], [], label=str(func))
        lines.append((line, f_lambdified))

    ax.set_xlabel('n')
    ax.set_ylabel('f(n)')
    ax.set_title('Function Growth Comparison')

    ax.legend()
    ax.grid(True)

    ax.set_xlim(1, 100)
    ax.set_ylim(0, 100)

    # Zoom functionality
    def zoom(event):
        if event.key == 'up':
            ax.set_ylim(ax.get_ylim()[0], ax.get_ylim()[1] * 1.1)
        elif event.key == 'down':
            ax.set_ylim(ax.get_ylim()[0], ax.get_ylim()[1] * 0.9)
        elif event.key == 'right':
            ax.set_xlim(ax.get_xlim()[0], ax.get_xlim()[1] * 1.1)
        elif event.key == 'left':
            ax.set_xlim(ax.get_xlim()[0], ax.get_xlim()[1] * 0.9)
        plt.draw()

    fig.canvas.mpl_connect('key_press_event', zoom)

    def animate(frame):
        for line, f_lambdified in lines:
            y_vals = f_lambdified(n_vals)
            line.set_data(n_vals[:frame + 1], y_vals[:frame + 1])  # Only plot up to the current frame
        return [line for line, _ in lines]

    ani = FuncAnimation(fig, animate, frames=len(n_vals), interval=50, blit=True)

    plt.show()

if __name__ == "__main__":
    functions = [sp.exp(sp.Symbol('n')), sp.log(sp.Symbol('n')), sp.Symbol('n')**2, sp.Symbol('n')**3]
    plot_functions(functions)
