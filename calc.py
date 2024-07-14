import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input\n{e}")

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to insert the button text into the entry
def button_click(value):
    entry.insert(tk.END, value)

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for the input
entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# Define button layout
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

# Create and place buttons in the window
row = 1
col = 0
for button in buttons:
    action = lambda x=button: button_click(x)
    tk.Button(root, text=button, width=10, height=3, command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create clear button
tk.Button(root, text='C', width=10, height=3, command=clear_entry).grid(row=row, column=col)
col += 1

# Bind the Enter key to evaluate the expression
root.bind('<Return>', evaluate_expression)

# Main loop
root.mainloop()
