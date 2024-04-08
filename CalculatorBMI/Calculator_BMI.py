import numpy as np
import tkinter as tk
from tkinter import messagebox
def calculate_bmi(weight, height):
    return weight / (height/100)**2
root=tk.Tk()
root.title("BMI Calculator")
root.geometry("400x200")
label = tk.Label(root,text ="Welcome to BMI calculator!",font=("Arial", 20))
label.pack()

def check_number():
    try:
        float(Weight.get())
        float(Height.get())
        return True
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")
        return False
def check_zero():
    if int(Height.get()) == 0:
        messagebox.showerror("Error", "Height cannot be 0")
        return False
    elif int(Weight.get()) == 0:
        messagebox.showerror("Error", "Weight cannot be 0")
        return False
    elif int(Height.get()) == 0:
        messagebox.showerror("Error", "Height cannot be 0")
        return False
    elif int(Height.get()) > 250:
        messagebox.showerror("Error", "Height cannot be greater than 250")
        return False
    elif int(Height.get()) < 50:
        messagebox.showerror("Error", "Height cannot be less than 50")
        return False
    return True
def calculate_bmi(weight, height):
    if check_number() and check_zero():
        bmi = weight / (height/100)**2
        messagebox.showinfo("BMI", f"Your BMI is: {bmi}")
        if bmi < 18.5:
            messagebox.showinfo("BMI", "You are underweight")
        elif 18.5 <= bmi < 24.9:
            messagebox.showinfo("BMI", "You have normal weight")
        elif 25 <= bmi < 29.9:
            messagebox.showinfo("BMI", "You are overweight")
        else:
            messagebox.showinfo("BMI", "You are obese")
        exit()
    return
frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.pack(pady=10)
height_label = tk.Label(frame, text="Height in cm:")
height_label.grid(row=0, column=0, padx=30, pady=10)
Height = tk.Entry(frame, text="Enter your height in centimeters")
Height.grid(row=1, column=0, padx=30, pady=10)
weight_label = tk.Label(frame, text="Weight in kg:")
weight_label.grid(row=0, column=1, padx=30, pady=10)
Weight = tk.Entry(frame, text="Enter your weight in kilograms")
Weight.grid(row=1, column=1, padx=30, pady=10)


button = tk.Button(root, text="Calculate", command = lambda: calculate_bmi(int(Weight.get()),int(Height.get())))
button.pack(pady=10)

root.mainloop()