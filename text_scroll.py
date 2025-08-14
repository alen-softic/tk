import tkinter as tk

def print_text():
    content = text_widget.get("1.0", tk.END)
    print(content)

root = tk.Tk()
root.title('My GUI Application')
root.geometry('600x400')

root.minsize(200, 150)

text_frame = tk.Frame(root)
text_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
text_frame.config(borderwidth=2, relief=tk.SUNKEN)


text_widget = tk.Text(text_frame, font=('Arial', 16), height=5, width=10)
scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)



button_frame = tk.Frame(root, bg='lightgrey')   
button_frame.pack(pady=10)

tk.Button(button_frame, text='Print Text', font=('Arial', 16)).\
    pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text='Clear Text', font=('Arial', 16)).\
    pack(side=tk.LEFT, padx=5)



root.mainloop()