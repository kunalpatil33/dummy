import tkinter as tk
from tkinter import messagebox
def new_file():
    messagebox.showinfo("New File", "New file created!")
def open_file():
    messagebox.showinfo("Open File", "Open file dialog!")
def exit_app():
    root.destroy()
def copy_text():
    messagebox.showinfo("Copy", "Text copied!")
def paste_text():
    messagebox.showinfo("Paste", "Text pasted!")
def about_app():
    messagebox.showinfo("About", "This is a sample Tkinter menu app")
root = tk.Tk()
root.title("Tkinter Menu Example")
root.geometry("400x300")
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about_app)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)
root.mainloop()