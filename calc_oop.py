import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Simple Python Calculator')
        self.root.geometry('400x300')

        self.result = tk.StringVar()

        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.pack(pady=20)

        tk.Label(root, textvariable=self.result, font=('Arial', 14)).pack(pady=10)

        tk.Button(root, text='Calculate', command=self.calculate).pack(pady=10)

        # Allow pressing Enter to calculate

        self.entry.bind('<Return>', lambda event: self.calculate())

    def calculate(self):
        try:
            # Evaluate the expression from the entry widget
            self.result.set(eval(self.entry.get())) 
        except Exception as e:
            self.result.set(f"Error")  
            messagebox.showerror("Error", "This is an error message: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
