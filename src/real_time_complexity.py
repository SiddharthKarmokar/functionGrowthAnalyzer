import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
from function_code import example_function 
import random


sns.set(style="darkgrid")


min_n = 10**3      # Minimum value for n
max_n = 10**6      # Maximum value for n
num_values = 50    # Total number of n values you want

n_values = sorted(random.sample(range(min_n, max_n + 1), num_values))
times = []
line = None


def measure_time_complexity(func, n):
    """Measure execution time of a function for a specific input size."""
    start_time = time.perf_counter()  # High-resolution timer
    func(n)
    end_time = time.perf_counter()

    return end_time - start_time


def update(frame):
    """Update function for the animation."""
    global line
    n = n_values[frame]
    time_taken = measure_time_complexity(example_function, n)

    time_taken = max(time_taken, 1e-6)

    times.append(time_taken)

    print(f"Frame: {frame}, n: {n}, Time Taken: {time_taken:.6f}, "
          f"Lengths -> n_values: {len(n_values)}, times: {len(times)}")

    # Check if we're at the correct frame
    if frame < len(n_values):
        # Clear the previous line if it exists
        if line:
            line.remove()

        line, = ax.plot(n_values[:frame + 1], times[:frame + 1], marker='o', color='b')

        ax.set_title("Time Complexity")
        ax.set_xlabel("Input Size (n)")
        ax.set_ylabel("Time (seconds)")
        ax.set_xscale('log')  
        ax.set_yscale('log')
        ax.grid(True)

    return line,




fig, ax = plt.subplots(figsize=(10, 6))

ani = FuncAnimation(fig, update, frames=len(n_values), repeat=False)

plt.show()
