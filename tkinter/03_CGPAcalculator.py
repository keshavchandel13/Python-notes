import tkinter as tk
root = tk.Tk()
root.geometry("400x400")

header = tk.Label(root,text="CGPA CALCULATOR",font=("Arial",20,"bold"),fg="red")
header.pack()

input_frame = tk.Frame(root,bg='#ADD8E6')
input_frame.pack(pady=20)

# Name box
name_label = tk.Label(input_frame,text="Name:")
name_label.grid(row=0,column=0,padx=10,pady=10)
name_input = tk.Entry(input_frame,width=10)
name_input.grid(row=0,column=1,padx=10,pady=10)

# regNumber box
reg_label = tk.Label(input_frame,text="Reg Number:")
reg_label.grid(row=0,column=2,padx=20,pady=10)
reg_input = tk.Entry(input_frame,width=10)
reg_input.grid(row=0,column=3,padx=10)

#roll number box
roll_label = tk.Label(input_frame,text="Roll Number:")
roll_label.grid(row=1,column=0,padx=10,pady=10)
roll_input = tk.Entry(input_frame,width=10)
roll_input.grid(row=1,column=1,padx=10)


root.mainloop()