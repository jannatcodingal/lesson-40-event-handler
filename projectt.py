import tkinter as tk
from tkinter import messagebox
def convert_inches_to_cm():
    """Converts inches to centimeters and displays the result."""
    try:
        inches = float(entry_inches.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for inches.")
root = tk.Tk()
root.title("Length converter app")
root.geometry("400x400")
label_inches = tk.Label(root, text="Enter length in inches:")
label_inches.pack(pady=10)
entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)
convert_button = tk.Button(root, text="Convert to CM", command=convert_inches_to_cm)
convert_button.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
root.mainloop()