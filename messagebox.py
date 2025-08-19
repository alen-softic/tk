
# --------------------------- Libraries ----------------------------

import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser

# ----------------- Function to show a message box -----------------

def show_info():
    messagebox.showinfo("Information", "This is a message box!")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message!")

def show_error():
    messagebox.showerror("Error", "This is an error message!")

def ask_question():
    result = messagebox.askyesno("Question", "Do you want to proceed?")
    if result:
        messagebox.showinfo("Response", "You chose Yes!")
    else:
        messagebox.showinfo("Response", "You chose No!")

def open_file():
    file_path = filedialog.askopenfilename(title="Select a file", 
                                           filetypes=[("Text files", "*.txt"), 
                                                      ("All files", "*.*")])
    if file_path:
        messagebox.showinfo("File Selected", f"You selected: {file_path}")
    else:
        messagebox.showwarning("No File", "No file was selected.")

def save_file():
    file_path = filedialog.asksaveasfilename(title="Save file", 
                                              defaultextension=".txt",
                                              filetypes=[("Text files", "*.txt"), 
                                                         ("All files", "*.*")])
    if file_path:
        messagebox.showinfo("File Saved", f"File saved as: {file_path}")
    else:
        messagebox.showwarning("No File", "No file was saved.")

def choose_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color:  # If a color was selected
        messagebox.showinfo("Color Selected", f"You selected: {color[1]}")
    else:
        messagebox.showwarning("No Color", "No color was selected.")

# ------------------------- Main GUI setup -------------------------

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')



tk.Button(root, text='Show Info', command=show_info).pack(pady=5)
tk.Button(root, text='Show Warning', command=show_warning).pack(pady=5)
tk.Button(root, text='Show Error', command=show_error).pack(pady=5)
tk.Button(root, text='Ask Question', command=ask_question).pack(pady=5)

tk.Button(root, text='Open File', command=open_file).pack(pady=(15,5))
tk.Button(root, text='Save File', command=save_file).pack(pady=(5))

tk.Button(root, text='Choose Color', command=choose_color).pack(pady=(15,5))


root.mainloop()