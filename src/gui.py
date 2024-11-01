import customtkinter as ctk
import subprocess
import os
from tkinter import filedialog

processes = []

def show_error(title, message):
    error_window = ctk.CTkToplevel(root)
    error_window.title(title)
    error_window.geometry("300x150")
    
    label = ctk.CTkLabel(error_window, text=message, wraplength=250, font=ctk.CTkFont(size=14))
    label.pack(pady=20)
    
    close_button = ctk.CTkButton(error_window, text="OK", command=error_window.destroy)
    close_button.pack(pady=10)

def initialize_file():
    with open("../functions.txt", "w") as file:
        file.write("")

def save_input():
    user_input = show_input_dialog("Input", "Please enter your input:")
    if user_input:
        with open("../functions.txt", "w") as file:
            file.write(user_input + "\n")

def plot_input():
    global processes
    if os.path.exists("./src/main.py"):
        process = subprocess.Popen(["python", "./src/main.py"])
        processes.append(process)
    else:
        show_error("Error", "main.py not found.")

def compare_input():
    user_input = show_input_dialog("Input", "Please enter your input to compare:")
    if user_input:
        with open("../functions.txt", "a") as file:
            file.write(user_input + "\n")

def upload_function_code():
    file_path = filedialog.askopenfilename(title="Select Function Code File", filetypes=[("Python Files", "*.py")])
    if file_path and os.path.exists(file_path):
        try:
            # Read the uploaded file content
            with open(file_path, 'r') as uploaded_file:
                code_content = uploaded_file.read()

            # Write the content to function_code.py
            with open("./src/function_code.py", "w") as function_file:
                function_file.write(code_content)

            # Call real_time_complexity.py after saving the uploaded file
            subprocess.Popen(["python", "./src/real_time_complexity.py"])
        except Exception as e:
            show_error("Error", str(e))
    else:
        show_error("Error", "Invalid file path or file does not exist.")

def exit_application():
    global processes
    for process in processes:
        if process.poll() is None:
            process.terminate()
    root.quit()

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("Function Growth Analyzer")
root.geometry("800x600")

button_frame = ctk.CTkFrame(root)
button_frame.pack(expand=True)

button_config = {
    "width": 200,
    "height": 40,
    "corner_radius": 10,
    "font": ctk.CTkFont(size=14, weight="bold"),
}

input_button = ctk.CTkButton(button_frame, text="Input", command=save_input, **button_config)
input_button.pack(pady=10)

plot_button = ctk.CTkButton(button_frame, text="Plot", command=plot_input, **button_config)
plot_button.pack(pady=10)

compare_button = ctk.CTkButton(button_frame, text="Compare", command=compare_input, **button_config)
compare_button.pack(pady=10)

upload_button = ctk.CTkButton(button_frame, text="Upload Function Code", command=upload_function_code, **button_config)
upload_button.pack(pady=10)

clear_button = ctk.CTkButton(button_frame, text="Clear", command=initialize_file, **button_config)
clear_button.pack(pady=10)

exit_button = ctk.CTkButton(button_frame, text="Exit", command=exit_application, **button_config)
exit_button.pack(pady=10)

root.mainloop()
