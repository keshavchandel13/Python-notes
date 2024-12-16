import tkinter as tk

def open_new_window():
    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.geometry("300x200")
    new_window.title("New Window")
    
    # Add content to the new window
    label = tk.Label(new_window, text="This is a new window!", font=("Arial", 16))
    label.pack(pady=20)

    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack()

root = tk.Tk()
root.geometry("400x300")
root.title("Main Window")

open_button = tk.Button(root, text="Open New Window", command=open_new_window)
open_button.pack(pady=50)

root.mainloop()
