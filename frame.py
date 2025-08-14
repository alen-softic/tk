import tkinter as tk

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x600')

root.minsize(400, 600)

frame = tk.Frame(root, bg='lightblue', relief='flat')
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

tk.Label(frame, text='This is a frame with a flat border', 
         font=('Arial', 16)).pack(pady=20)
tk.Label(frame, text='This is a frame with a flat border', 
         font=('Arial', 16), relief='raised', bg='orange').pack(pady=20)


tk.Frame(frame, bg='lightgrey', relief='raised').pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

tk.Frame(root, bg='lightgrey', relief='raised').pack(pady=20, padx=20, fill=tk.BOTH, expand=True)


root.mainloop()