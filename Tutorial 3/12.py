import tkinter as tk

def convert_to_uppercase():
    input_text = text_entry.get()
    result_label.config(text=f"Uppercase: {input_text.upper()}")

root = tk.Tk()
root.title("Uppercase Converter")

tk.Label(root, text="Enter text:").pack(pady=10)
text_entry = tk.Entry(root)
text_entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Uppercase: ")
result_label.pack(pady=10)

root.mainloop()
