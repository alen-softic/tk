import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Simple Python Calculator')
root.geometry('400x300')

def calculate():
    try:
        # Evaluate the expression from the entry widget
        result.set(eval(entry.get())) 
    except Exception as e:
        result.set(f"Error")  
        messagebox.showerror("Error", "This is an error message: " + str(e))


entry = tk.Entry(root, width=40, borderwidth=5)
entry.pack(pady=20) 

result = tk.StringVar()
tk.Label(root, textvariable=result, font=('Arial', 14)).pack(pady=10)

tk.Button(root, text='Calculate', command=calculate).pack(pady=10)


# Allow pressing Enter to calculate
entry.bind('<Return>', lambda event: calculate())  

root.mainloop()