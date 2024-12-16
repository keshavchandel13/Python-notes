# a widget is an element of a graphical user interface (GUI) that displays information or provides controls for user interaction
def display():
    pass
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry('400x400')

# Label Widget
label = tk.Label(root, text="Label Widgets")
label.pack(pady=10)

# button widget
btn = tk.Button(root,text="submit",command=display)
btn.pack()

# Entry Widget (Single line text input)
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# entry widget (multiline line text input)
text = tk.Text(root,width=20, height=5)
text.pack()

# Radio widget
radio_val = tk.StringVar(value="option1")
radio1 = tk.Radiobutton(root,text="option1",variable=radio_val, value="option1")
radio2 = tk.Radiobutton(root,text="option2",variable=radio_val, value="option2")
radio1.pack()
radio2.pack()

#checkbox
check_val1 =tk.BooleanVar()
check_val2 =tk.BooleanVar()
check1 = tk.Checkbutton(root,variable=check_val1)
check2 = tk.Checkbutton(root,variable=check_val2)
check1.pack()
check2.pack()

#ListBox widget 
listbox = tk.Listbox(root,height=5)
items = ["item1","item2","item3","item4"]
for item in items:
    listbox.insert(tk.END,item)
listbox.pack()

# combobox widget
combobox = ttk.Combobox(root,values=["Select One", "option1","option 2"])
combobox.current(0)
combobox.pack()

# slider 
slider = tk.Scale(root,from_=0,to=100)
slider.pack()

# Message Widget 
message = tk.Message(root, text="This is a Message widget. It works like a label but for larger text.", width=300)
message.pack(pady=10)

# SCROLL text widget
scrollbar_frame = tk.Frame(root)
scrollbar_frame.pack()

scrollbar = tk.Scrollbar(scrollbar_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

listbox_with_scroll = tk.Listbox(scrollbar_frame, yscrollcommand=scrollbar.set, height=5)
for i in range(50):
    listbox_with_scroll.insert(tk.END, f"Item {i+1}")

listbox_with_scroll.pack(side="left")
scrollbar.config(command=listbox_with_scroll.yview)


root.mainloop()
