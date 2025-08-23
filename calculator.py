import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
 
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        
        self.result_var = tk.StringVar()
        self.result_var.set("0")  
        
        self.create_widgets()
    
    def create_widgets(self):
        display = tk.Entry(self.root, textvariable=self.result_var, 
                          font=("Arial", 16), justify="right", state="readonly")
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
        
        buttons = [
            ['C', '⌫', '%', '/'],    # Row 1: Clear, backspace, percent, divide
            ['7', '8', '9', '*'],    # Row 2: Numbers and multiply
            ['4', '5', '6', '-'],    # Row 3: Numbers and subtract
            ['1', '2', '3', '+'],    # Row 4: Numbers and add
            ['0', '.', '=']          # Row 5: Zero (spans 2 columns), decimal, equals
        ]
        
        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                if button == '0':
                    btn = tk.Button(self.root, text=button,
                                   command=lambda b=button: self.button_click(b))
                    btn.grid(row=i+1, column=0, columnspan=2, padx=2, pady=2, sticky="ew")
                elif button == '.':
                    btn = tk.Button(self.root, text=button,
                                   command=lambda b=button: self.button_click(b))
                    btn.grid(row=i+1, column=2, columnspan=1, padx=2, pady=2, sticky="ew")

                elif button == '=':
                    btn = tk.Button(self.root, text=button,
                                   command=lambda b=button: self.button_click(b))
                    btn.grid(row=i+1, column=3, columnspan=1, padx=2, pady=2, sticky="ew")
                else:
                    btn = tk.Button(self.root, text=button,
                                   command=lambda b=button: self.button_click(b))
                    btn.grid(row=i+1, column=j, padx=2, pady=2, sticky="ew")
        
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, button):

        current = self.result_var.get() 
        
        if button == 'C':
            self.result_var.set("0")
            
        elif button == '⌫':
            if len(current) <= 1 or current == "0":
                self.result_var.set("0")
            else:
                self.result_var.set(current[:-1])
            
        elif button == '=':
            try:
                result = eval(current)  
                self.result_var.set(str(result)) 
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.result_var.set("0")
                
        elif button in ['+', '-', '*', '/', '%']:            
            if current == "0" or current == "":
                if button == '-':
                    self.result_var.set(button)
                return
            
            last_char = current[-1:] if current else ""
            
            if button == '-':
                if last_char == '-':
                    self.result_var.set(current[:-1])
                elif last_char in ['+', '*', '/', '%']:
                    self.result_var.set(current + button)
                elif last_char not in ['+', '-', '*', '/', '%']:
                    self.result_var.set(current + button)
            else:
                if last_char == '-':
                    if len(current)>1 and current[-2] in ['+', '*', '/', '%']:
                        self.result_var.set(current[:-2] + button)
                    else:
                        self.result_var.set(current[:-1] + button)
                elif last_char in ['+', '*', '/', '%']:
                    self.result_var.set(current[:-1] + button)
                else:
                    self.result_var.set(current + button)
                    
        else:
            if current == "0":
                if button == '.':
                    self.result_var.set(current + button)
                else:
                    self.result_var.set(button)
            else:
                self.result_var.set(current + button)

# ------------------------------
# ----- Fix decimal points -----
# ------------------------------

if __name__ == "__main__":
    root = tk.Tk() 
    calc = Calculator(root) 
    root.mainloop()
