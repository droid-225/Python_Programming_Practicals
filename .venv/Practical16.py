import tkinter as tk
from tkinter import messagebox

# Function to be called when the button is clicked
def on_button_click():
    user_input = entry.get()
    messagebox.showinfo("Message", f"Hello, {user_input}!")

# Create the main window
root = tk.Tk()
root.title("Tkinter GUI Example")

# Set the window size
root.geometry("300x150")

# Create a label widget
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button widget
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()