import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib.animation import FuncAnimation
import seaborn as sns

class CustomInputDialog(ctk.CTkToplevel):
    def __init__(self, master, title, prompt):
        super().__init__(master)
        self.title(title)
        self.geometry("300x150")
        self.resizable(False, False)

        self.label = ctk.CTkLabel(self, text=prompt, font=ctk.CTkFont(size=14))
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, width=200)
        self.entry.pack(pady=5)

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=10)

        self.result = None
        self.entry.focus_set()

        # Bind the Enter key to the on_submit method
        self.entry.bind("<Return>", lambda event: self.on_submit())

    def on_submit(self):
        try:
            self.result = float(self.entry.get())
            self.destroy()
        except ValueError:
            self.label.configure(text="Invalid input. Please enter a number.", text_color="red")

    def get_result(self):
        self.wait_window()
        return self.result

def plot_functions(functions):
    plot_window = ctk.CTk()
    plot_window.title("Function Growth Comparison")
    plot_window.geometry("900x700")

    n_vals = np.linspace(1, 100, 400)
    fig, ax = plt.subplots(figsize=(10, 6))

    lines = []
    for func in functions:
        f_lambdified = sp.lambdify('n', func, 'numpy')
        line, = ax.plot([], [], label=str(func))  # Create empty line for animation
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

    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20, fill='both', expand=True)

    fig.canvas.mpl_connect('key_press_event', lambda event: update_limits(event, ax))

    plot_window.mainloop()

def update_limits(event, ax):
    if event.key == 'y':
        y_max = show_custom_input_dialog("Enter new y_max")
        if y_max is not None:
            ax.set_ylim(0, y_max)

    elif event.key == 'x':
        x_min = show_custom_input_dialog("Enter new x_min")
        x_max = show_custom_input_dialog("Enter new x_max")
        if x_min is not None and x_max is not None:
            ax.set_xlim(x_min, x_max)

    ax.figure.canvas.draw()

def show_custom_input_dialog(prompt):
    dialog_root = ctk.CTk()
    dialog_root.withdraw()
    dialog = CustomInputDialog(dialog_root, "Input", prompt)
    result = dialog.get_result()
    dialog_root.destroy()
    return result

if __name__ == "__main__":
    functions = [sp.exp(sp.Symbol('n')), sp.log(sp.Symbol('n')), sp.Symbol('n')**2, sp.Symbol('n')**3]
    plot_functions(functions)
