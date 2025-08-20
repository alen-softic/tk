import tkinter as tk
from tkinter import messagebox

class Calculator:
    """
    A simple calculator class using Tkinter for GUI.
    """

    def __init__(self, root):
        """
        Initialize the calculator application.
        :param root: The root window for the Tkinter application.
        """

        self.root = root
        self.root.title('Python Calculator')
        self.root.geometry('350x250')

        self.result = tk.StringVar()
        self.result.set("0")

        self.create_widgets()

    def create_widgets(self):
        """
        Create the calculator widgets.
        """

        display = tk.Entry(
            self.root,
            textvariable=self.result,
            font=('Arial', 18),
            state='readonly',
            justify='right'
            )
        
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        buttons = [
            ['C', '-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                if button == '0':

                    btn = tk.Button(
                        self.root,
                        text=button,
                        command=lambda b=button: self.button_click(b)
                    )
                    btn.grid(row=i + 1, column=j, columnspan = 2, sticky='ew', padx=2, pady=2)

                else:
                    btn = tk.Button(
                        self.root,
                        text=button,
                        command=lambda b=button: self.button_click(b)
                    )
                    btn.grid(row=i + 1, column=j, sticky='ew', padx=2, pady=2)


        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def button_click(self, button):
        """
        Handle button clicks.
        :param button: The button that was clicked.
        """

        current = self.result.get()

        if button == 'C':
            self.result.set("0")
        elif button == '=':
            try:
                self.result.set(eval(current))
            except Exception as e:
                self.result.set("Error")
                messagebox.showerror("Error", "Invalid expression: " + str(e))
        else:
            if current == "0":
                self.result.set(button)
            else:
                self.result.set(current + button)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()