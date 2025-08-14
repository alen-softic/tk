import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

btn = tk.Button(root, text='Click Me!', command=on_button_click)
btn.pack(pady=20)


root.mainloop()