import tkinter as tk
from tkinter import messagebox
import math

def compute_sqrt():
    try:
        num = int(entry.get()) 
        if num < 0:
            raise ValueError("Negative number")
        result = math.sqrt(num)
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid non-negative integer.")

root = tk.Tk()
root.title("Square Root Calculator")

tk.Label(root, text="Enter an integer:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Compute √", command=compute_sqrt).pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
