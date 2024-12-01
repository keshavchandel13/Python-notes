#

import tkinter 

print(dir(tkinter))

print(type(tkinter))

from tkinter import ttk

print(type(ttk))
print(dir(ttk))


r=tkinter.Tk()
b1 = ttk.Button(r, text = "Click me !")
b1.grid(row=0,column=0,pady=100)

b2 = ttk.Button(r, text = "Click me !")
b2.grid(row=0,column=1,padx=50,pady=20)

b3 = ttk.Button(r, text = "Click me !")
b3.grid(row=1,column=0,padx=50,pady=20)



b4 = ttk.Button(r, text = "Click me !")
b4.grid(row=1,column=1,padx=50,pady=20)


b5 = ttk.Button(r, text = "Click me !")
b5.grid(row=2,column=0,padx=50,pady=20)


b6 = ttk.Button(r, text = "Click me too")
b6.grid(row=3,column=0,padx=500,pady=20,rowspan=True)
r.mainloop()