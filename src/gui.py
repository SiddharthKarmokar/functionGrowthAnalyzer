import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import os

processes = []

def initialize_file():
    with open("../functions.txt", "w") as file:
        file.write("") 

def save_input():
    user_input = simpledialog.askstring("Input", "Please enter your input:")
    if user_input:
        with open("../functions.txt", "w") as file:
            file.write(user_input + "\n")

def plot_input():
    global processes
    if os.path.exists("./src/main.py"):
        process = subprocess.Popen(["python", "./src/main.py"])
        processes.append(process)  
    else:
        messagebox.showerror("Error", "main.py not found.")

def compare_input():
    user_input = simpledialog.askstring("Input", "Please enter your input to compare:")
    if user_input:
        with open("../functions.txt", "a") as file:  
            file.write(user_input + "\n")

def exit_application():
    global processes
    for process in processes:
        if process.poll() is None:
            process.terminate()  

    root.quit() 


root = tk.Tk()
root.title("Main Menu")


root.geometry("800x600")


button_frame = tk.Frame(root)
button_frame.pack(expand=True)


button_config = {
    "width": 20,
    "height": 2,
    "bd": 4,  
    "relief": "raised",  
    "highlightthickness": 2,
    "highlightbackground": "lightgrey", 
    "highlightcolor": "blue",  
    "font": ("Arial", 12),  
}


input_button = tk.Button(button_frame, text="Input", command=save_input, **button_config)
input_button.pack(pady=10)

plot_button = tk.Button(button_frame, text="Plot", command=plot_input, **button_config)
plot_button.pack(pady=10)

compare_button = tk.Button(button_frame, text="Compare", command=compare_input, **button_config)
compare_button.pack(pady=10)

clear_button = tk.Button(button_frame, text="Clear", command=initialize_file, **button_config)
clear_button.pack(pady=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_application, **button_config)
exit_button.pack(pady=10)


root.mainloop()
