import tkinter as tk
from tkinter import messagebox  # To show error messages

# Function to calculate SGPA
def submit():
    try:
        grades_to_points = {'A': 10, 'B': 9, 'C': 8, 'D': 7, 'E': 6, 'F': 0}  # Example grade-to-point mapping
        total_credits = 0
        total_credit_points = 0
        
        for i in range(4):  # For each subject
            grade = grade_inputs[i].get().upper()  # Get the grade from the input field
            credit = sub_credit[i]  # Get the credit for the subject
            
            if grade not in grades_to_points:
                messagebox.showerror("Input Error", f"Invalid grade '{grade}' for Subject {i+1}. Use A, B, C, D, E, F.")
                return
            
            grade_point = grades_to_points[grade]  # Convert grade to points using the dictionary
            credit_points = grade_point * credit  # Calculate total credit points for this subject
            
            total_credits += credit  # Sum of subject credits
            total_credit_points += credit_points  # Sum of earned credit points
        
        sgpa = total_credit_points / total_credits  # Calculate SGPA
        ans_label.config(text=f"The SGPA is: {sgpa:.2f}")  # Update the label with SGPA value

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main window
root = tk.Tk()
root.geometry("500x500")

header = tk.Label(root, text="CGPA CALCULATOR", font=("Arial", 20, "bold"), fg="red")
header.pack()

input_frame = tk.Frame(root, bg='#ADD8E6')
input_frame.pack(pady=20)

# Name box
name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_input = tk.Entry(input_frame, width=10)
name_input.grid(row=0, column=1, padx=10, pady=10)

# Registration Number box
reg_label = tk.Label(input_frame, text="Reg Number:")
reg_label.grid(row=0, column=2, padx=20, pady=10)
reg_input = tk.Entry(input_frame, width=10)
reg_input.grid(row=0, column=3, padx=10)

# Roll Number box
roll_label = tk.Label(input_frame, text="Roll Number:")
roll_label.grid(row=1, column=0, padx=10, pady=10)
roll_input = tk.Entry(input_frame, width=10)
roll_input.grid(row=1, column=1, padx=10)

# Table Headers
head_label = tk.Label(input_frame, text="Serial No.")
head_label.grid(row=2, column=0, padx=10, pady=10)

head_label = tk.Label(input_frame, text="Subject")
head_label.grid(row=2, column=1, padx=10, pady=10)

head_label = tk.Label(input_frame, text="Grade")
head_label.grid(row=2, column=2, padx=10, pady=10)

head_label = tk.Label(input_frame, text="Subject Credit")
head_label.grid(row=2, column=3, padx=10, pady=10)

head_label = tk.Label(input_frame, text="Credit Points")
head_label.grid(row=2, column=4, padx=10, pady=10)

# Subject data
labels = ["Subject 1", "Subject 2", "Subject 3", "Subject 4"]
sub_credit = [4, 4, 3, 2]  # Subject credits
grade_inputs = []  # To store entry widgets for grades

row_count = 3
for i in range(1, 5):
    serial_num = tk.Label(input_frame, text=f"{i}")
    serial_num.grid(row=row_count, column=0, padx=10)
    
    subject_label = tk.Label(input_frame, text=f"{labels[i-1]}")
    subject_label.grid(row=row_count, column=1, padx=10)
    
    grade_input = tk.Entry(input_frame, width=5)
    grade_input.grid(row=row_count, column=2, padx=10)
    grade_inputs.append(grade_input)  # Store the grade input field
    
    subject_credit_label = tk.Label(input_frame, text=f"{sub_credit[i-1]}")
    subject_credit_label.grid(row=row_count, column=3, padx=10)
    
    row_count += 1

# Submit button
btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

# Result label to display SGPA
ans_label = tk.Label(root, text="The SGPA is: ")
ans_label.pack()

# Start the main event loop
root.mainloop()
