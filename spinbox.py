import tkinter as tk

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

spinbox = tk.Spinbox(root, from_=0, to=10, increment=1)
spinbox.pack(pady=20)

tk.Button(root, text='Get Spinbox Value', 
    command=lambda: print(f'Spinbox value: {spinbox.get()}')).pack(pady=5)
root.mainloop()