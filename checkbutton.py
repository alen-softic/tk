import tkinter as tk

def show_status():
    """Update the label based on the checkbox state."""
    if var1.get() and var2.get():
        text='Both options selected!'
    elif var1.get():
        text='Only Option 1 selected!'
    elif var2.get():
        text='Only Option 2 selected!'
    else:   
        text='No options selected!'

    lab.config(text=text)
    send_btn.config(state='disabled')


root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

chk1 = tk.Checkbutton(root, text='Option 1', variable=var1)
chk1.pack(pady=20)

chk2 = tk.Checkbutton(root, text='Option 2', variable=var2)
chk2.pack(pady=20)

send_btn = tk.Button(root, text='Send', command=show_status)
send_btn.pack(pady=20)

lab = tk.Label(root, text='Check the box to agree.')
lab.pack(pady=20)

root.mainloop()