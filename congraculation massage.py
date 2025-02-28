import tkinter as tk
from tkinter import messagebox

def show_message():
    name = name_entry.get()
    occasion = occasion_entry.get()
    if name and occasion:
        message = f"Congratulations, {name}! Wishing you all the best on your {occasion}!"
        messagebox.showinfo("Congratulation Message", message)
    else:
        messagebox.showwarning("Input Error", "Please enter both name and occasion.")

# Create the main window
root = tk.Tk()
root.title("Congratulation Message Generator")
root.geometry("400x300")

# Labels and Entry fields
tk.Label(root, text="Enter Name:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

tk.Label(root, text="Enter Occasion:").pack(pady=5)
occasion_entry = tk.Entry(root, width=40)
occasion_entry.pack(pady=5)

# Button to generate message
tk.Button(root, text="Generate Message", command=show_message).pack(pady=20)

# Run the application
root.mainloop()
