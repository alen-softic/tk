import tkinter as tk
from tkinter import messagebox, filedialog

class TextEditor:

    def __init__(self, root):
        self.root = root
        self.root.title('Simple Text Editor')

        self.current_file = ''

        self.create_widgets()

        self.bind_keys()


    def bind_keys(self):
        self.root.bind('<Command-o>', lambda event : self.open_file())
        self.root.bind('<Command-Shift-S>', lambda event : self.save_file_as())
        self.root.bind('<Command-s>', lambda event : self.save_file())

        self.root.bind('<Control-o>', lambda event : self.open_file())
        self.root.bind('<Control-Shift-S>', lambda event : self.save_file_as())
        self.root.bind('<Control-s>', lambda event : self.save_file())


    def create_widgets(self):
            self.text_area = tk.Text(self.root)
            self.text_area.pack(fill='both', expand=True)

            self.menu = tk.Menu(self.root)
            self.root.config(menu = self.menu)

            file_menu = tk.Menu(self.menu, tearoff=0)
            file_menu.add_command(label='Open', command=self.open_file,
                       accelerator='Cmd+O')
            file_menu.add_command(label='Save', command=self.save_file,
                       accelerator='Cmd+S')
            file_menu.add_command(label='Save As', command=self.save_file_as,
                       accelerator='Cmd+Shift+S')
            
            self.menu.add_cascade(label='File', menu=file_menu)

    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt'),
                                                     ('Python Scripts', '*.py')])
        if file:
            with open(file, 'r') as f:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, f.read())

        self.current_file = file

    def save_file(self):
        
        text = self.text_area.get(1.0, tk.END)
        if self.current_file:
            with open(self.current_file, 'w') as f:
                f.write(self.text_area.get(1.0, tk.END))
        else:
            messagebox.showwarning('Warning', "File doesn't exist yet. Use 'Save As'.")


    def save_file_as(self):
        file = filedialog.asksaveasfilename(defaultextension='.txt',
                filetypes=[('Text Files', '*.txt'),
                           ('Python Scripts', '*.py')])
        if file:
            with open(file, 'w') as f:
                f.write(self.text_area.get(1.0, tk.END))
        self.current_file = file
            
if __name__ == "__main__":
    root = tk.Tk() 
    calc = TextEditor(root) 
    root.mainloop()
