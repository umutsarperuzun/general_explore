from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(300, 200)
window.config(padx=20, pady=20)

# Title
title_label = Label(text="BMI Calculator", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Weight input
weight_label = Label(text="Enter Your Weight (kg):")
weight_label.grid(row=1, column=0, sticky="e", pady=5)
weight_entry = Entry(width=20)
weight_entry.grid(row=1, column=1, pady=5)

# Height input
height_label = Label(text="Enter Your Height (cm):")
height_label.grid(row=2, column=0, sticky="e", pady=5)
height_entry = Entry(width=20)
height_entry.grid(row=2, column=1, pady=5)

# Result display label
result_label = Label(text="", wraplength=250)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# BMI classification function
def classification(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi <= 34.9:
        return "Obesity (1st Class)"
    elif 35 <= bmi <= 39.9:
        return "Obesity (2nd Class)"
    else:
        return "Extreme Obesity (3rd Class)"

# Calculate BMI and update result label
def calculate():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        status = classification(bmi)
        result_label.config(text=f"Your BMI is {bmi:.2f}. You are {status}.")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Calculate button
button = Button(text="Calculate BMI", command=calculate)
button.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()
