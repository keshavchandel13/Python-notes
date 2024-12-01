from tkinter import *
from tkinter import messagebox



# Initialize main application
app = Tk()
app.title("Admission Form")
app.geometry("400x500")
app.configure(bg='lightblue')

# Header
header = Label(app, text="Admission Form", font=("Arial", 16, "bold"), bg="lightblue")
header.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entry Fields
Label(app, text="Name:", bg="lightblue", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky=W)
e_name = Entry(app, width=30)
e_name.grid(row=1, column=1, padx=10, pady=5)

Label(app, text="Roll No:", bg="lightblue", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=5, sticky=W)
e_roll = Entry(app, width=30)
e_roll.grid(row=2, column=1, padx=10, pady=5)

Label(app, text="Email:", bg="lightblue", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=5, sticky=W)
e_email = Entry(app, width=30)
e_email.grid(row=3, column=1, padx=10, pady=5)

Label(app, text="Phone No:", bg="lightblue", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=5, sticky=W)
e_phone = Entry(app, width=30)
e_phone.grid(row=4, column=1, padx=10, pady=5)

Label(app, text="Gender:", bg="lightblue", font=("Arial", 10)).grid(row=5, column=0, padx=10, pady=5, sticky=W)
gender_var = StringVar()
Radiobutton(app, text="Male", variable=gender_var, value="Male", bg="lightblue").grid(row=5, column=1, sticky=W, padx=10)
Radiobutton(app, text="Female", variable=gender_var, value="Female", bg="lightblue").grid(row=5, column=1, sticky=E, padx=10)

# Label(app, text="Course:", bg="lightblue", font=("Arial", 10)).grid(row=6, column=0, padx=10, pady=5, sticky=W)
# course_var = StringVar()
# OptionMenu(app, course_var, "B.Tech", "B.Sc", "BCA", "M.Tech", "MBA").grid(row=6, column=1, padx=10, pady=5)

Label(app, text="Address:", bg="lightblue", font=("Arial", 10)).grid(row=7, column=0, padx=10, pady=5, sticky=NW)
e_address = Text(app, width=23, height=4)
e_address.grid(row=7, column=1, padx=10, pady=5)

# Submit Button
submit_button = Button(app, text="Submit", bg="green", fg="white", font=("Arial", 10))
submit_button.grid(row=8, column=0, columnspan=2, pady=20)

# Run application
app.mainloop()
