import tkinter as tk

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

scale = tk.Scale(root, from_=0, to=100, orient='horizontal',
                 command=lambda val: print(f'Scale value: {val}'))
scale.pack(pady=20)

tk.Button(root, text='Get Scale Value', 
    command=lambda: print(f'Scale value: {scale.get()}')).pack(pady=5)


root.mainloop()