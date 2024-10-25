import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess

# List to hold the subprocess references
processes = []

# Clear the content of functions.txt initially
def initialize_file():
    with open("../functions.txt", "w") as file:
        file.write("")  # This clears the file

def save_input():
    user_input = simpledialog.askstring("Input", "Please enter your input:")
    if user_input:
        with open("../functions.txt", "w") as file:  # Append input instead of overwriting
            file.write(user_input + "\n")
        messagebox.showinfo("Success", "Input saved to ../functions.txt")

def plot_input():
    global processes
    process = subprocess.Popen(["python", "main.py"])  # Run the plotting script
    processes.append(process)  # Add to the list of processes

def compare_input():
    user_input = simpledialog.askstring("Input", "Please enter your input to compare:")
    if user_input:
        with open("../functions.txt", "a") as file:  # Append input instead of overwriting
            file.write(user_input + "\n")
        messagebox.showinfo("Success", "Input saved to ../functions.txt")


def exit_application():
    global processes
    # Terminate all main.py processes
    for process in processes:
        if process.poll() is None:  # Check if the process is still running
            process.terminate()  # Terminate the process

    root.quit()  # Close the main window

# Create the main window
root = tk.Tk()
root.title("Main Menu")

# Clear the file at the start
initialize_file()

# Create buttons for different functions
input_button = tk.Button(root, text="Input", command=save_input)
input_button.pack(padx=20, pady=20)

plot_button = tk.Button(root, text="Plot", command=plot_input)
plot_button.pack(padx=20, pady=20)

compare_button = tk.Button(root, text="Compare", command=compare_input)
compare_button.pack(padx=20, pady=20)

clear_button = tk.Button(root, text="Clear", command=initialize_file)
clear_button.pack(padx=20, pady=20)

exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.pack(padx=20, pady=20)



# Start the GUI event loop
root.mainloop()
