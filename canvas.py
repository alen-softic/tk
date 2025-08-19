import tkinter as tk

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

canvas = tk.Canvas(root, width=400, height=300, bg='lightblue')
canvas.pack()

canvas.create_text(200, 50, text='Welcome to the Canvas', font=('Arial', 24), fill='black')
canvas.create_rectangle(50, 100, 350, 200, fill='white', outline='black', width=2)
canvas.create_text(200, 150, text='This is a simple canvas example', font=('Arial', 16), fill='black')      
canvas.create_oval(150, 200, 250, 250, fill='red', outline='black', width=2)

root.mainloop()