import tkinter as tk
from tkinter import messagebox

def show_selection():
    choice = selected_option.get()
    messagebox.showinfo("Your Selection", f"You selected: {choice}")

# Main window
root = tk.Tk()
root.title("RadioButton Example")
root.geometry("300x200")

# StringVar to store selected value
selected_option = tk.StringVar()
selected_option.set("Option 1")   # default selection

# RadioButtons
r1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1")
r2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2")
r3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3")

r1.pack(anchor='w')
r2.pack(anchor='w')
r3.pack(anchor='w')

# Button to display selection
btn = tk.Button(root, text="Show Selection", command=show_selection)
btn.pack(pady=10)

root.mainloop()