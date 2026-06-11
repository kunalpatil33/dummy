import tkinter as tk

def show_state():
    if var.get() == 1:
        label.config(text="Checkbutton is ON")
    else:
        label.config(text="Checkbutton is OFF")

# Create main window
root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("300x200")

# IntVar to store the checkbutton state
var = tk.IntVar()

# Create Checkbutton
check = tk.Checkbutton(root, text="Enable Option", variable=var, command=show_state)
check.pack(pady=20)

# Label to show status
label = tk.Label(root, text="Checkbutton is OFF", font=("Arial", 12))
label.pack()

# Run window
root.mainloop()