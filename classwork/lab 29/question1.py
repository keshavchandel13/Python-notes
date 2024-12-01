import tkinter as tk
from tkinter import *

def getsum():
    a = int(value_a.get())
    b = int(value_b.get())
    c = a + b
    # Update the label with the result
    result_label.config(text=f"Sum of {a} and {b} is: {c}")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# Input labels and entry fields
Label(root, text="A:").grid(row=1, column=0, padx=10, pady=5, sticky=W)
value_a = Entry(root, width=10)
value_a.grid(row=1, column=1)

Label(root, text="+").grid(row=1, column=2, padx=10, pady=5, sticky=W)

Label(root, text="B:").grid(row=1, column=3, padx=10, pady=5, sticky=W)
value_b = Entry(root, width=10)
value_b.grid(row=1, column=4)


button = tk.Button(root, text="Calculate", command=getsum)
button.grid(row=2, column=1, columnspan=2, pady=10)


result_label = Label(root, text="")
result_label.grid(row=3, column=0, columnspan=5)

root.mainloop()
