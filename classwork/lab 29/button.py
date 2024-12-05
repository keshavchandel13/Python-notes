import tkinter as tk
from tkinter import messagebox

# Functions to handle button actions
def submit_action():
    value = entry.get()
    messagebox.showinfo("Input", f"You entered: {value}")

def check_button_action():
    status = "Checked" if checkbox_var.get() else "Unchecked"
    messagebox.showinfo("Checkbox Status", f"Checkbox is {status}")

def radio_button_action():
    messagebox.showinfo("Radio Selection", f"Selected option: {radio_var.get()}")

# Main window
root = tk.Tk()
root.title("Tkinter Buttons and Input Boxes Example")
root.geometry("400x300")

# Entry box
tk.Label(root, text="Enter text:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button
submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.pack(pady=5)

# Checkbox
checkbox_var = tk.BooleanVar()
check_button = tk.Checkbutton(root, text="I agree", variable=checkbox_var, command=check_button_action)
check_button.pack(pady=5)

# Radio buttons
tk.Label(root, text="Select an option:").pack(pady=5)
radio_var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=radio_button_action)
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=radio_button_action)
radio3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3", command=radio_button_action)
radio1.pack()
radio2.pack()
radio3.pack()

# Text Box (multi-line input)
tk.Label(root, text="Enter multi-line text:").pack(pady=5)
text_box = tk.Text(root, height=5, width=30)
text_box.pack(pady=5)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

# Start the Tkinter loop
root.mainloop()
