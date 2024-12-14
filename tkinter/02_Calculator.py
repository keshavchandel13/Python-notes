import tkinter as tk

def click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Minimalist Calculator")

# Create an entry widget for displaying input and output
entry = tk.Entry(root, font=("Arial", 16), justify="right", bd=8, relief="flat")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and arrange buttons in a grid
for i, button_text in enumerate(buttons):
    btn = tk.Button(root, text=button_text, font=("Arial", 16), bd=1, relief="flat", 
                    command=lambda x=button_text: click(x))
    btn.grid(row=(i // 4) + 1, column=i % 4, sticky="nsew")

# Make the grid expand
for i in range(5):  # 4 rows + 1 for the entry widget
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()