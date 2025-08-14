import tkinter as tk

def show_check_status():
    print(var.get())

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')
root.minsize(200, 150)

var = tk.BooleanVar()
chk = tk.Checkbutton(root, text='Check me!', variable=var, font=('Arial', 16))
chk.pack(pady=20)

tk.Button(root, text='Show Status', command=show_check_status).pack(pady=10)


root.mainloop()