import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.config(text=f"BMI: {bmi} ({category})")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for height and weight.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

# Header
header = tk.Label(root, text="BMI Calculator", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333")
header.pack(pady=20)

# Input Frame
input_frame = tk.Frame(root, bg='#f5f5f5')
input_frame.pack(pady=20)

# Height Input
height_label = tk.Label(input_frame, text="Height (m):", font=("Arial", 14), bg="#f5f5f5", fg="#555")
height_label.grid(row=0, column=0, padx=10, pady=10)
height_entry = tk.Entry(input_frame, font=("Arial", 14), width=10, bd=2, relief="ridge")
height_entry.grid(row=0, column=1, padx=10, pady=10)

# Weight Input
weight_label = tk.Label(input_frame, text="Weight (kg):", font=("Arial", 14), bg="#f5f5f5", fg="#555")
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(input_frame, font=("Arial", 14), width=10, bd=2, relief="ridge")
weight_entry.grid(row=1, column=1, padx=10, pady=10)

# Calculate Button
calculate_button = tk.Button(
    root, 
    text="Calculate BMI", 
    font=("Arial", 14), 
    bg="#4caf50", 
    fg="white", 
    activebackground="#45a049", 
    activeforeground="white", 
    command=calculate_bmi, 
    relief="raised", 
    bd=2, 
    width=15
)
calculate_button.pack(pady=20)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333")
result_label.pack(pady=20)

# Footer
footer = tk.Label(root, text="Stay Healthy!", font=("Arial", 12, "italic"), bg="#f5f5f5", fg="#999")
footer.pack(pady=10)

# Start the application
root.mainloop()
