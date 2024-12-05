def change():
    name = entry.get()
    revname = name[0::]
    t3.config(text="Reversed Name is: "+revname)
import tkinter as tk
root = tk.Tk()

t1 = tk.Label(root,text="Name")
t1.pack()
entry = tk.Entry(root,width=20)
entry.pack()
t2 = tk.Label(root,text="Name in the reverse")
t2.pack()
t3 = tk.Label(root,text="")
t3.pack()
btn = tk.Button(text="print",command=change)

root.mainloop()