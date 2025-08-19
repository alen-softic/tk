import tkinter as tk

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', command=lambda: print("New file"),
                       accelerator='Cmd+N')
file_menu.add_command(label='Open', command=lambda: print("Open file"), 
                       accelerator='Cmd+O')
file_menu.add_command(label='Save', command=lambda: print("Save file"),
                       accelerator='Cmd+S')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
menu_bar.add_cascade(label='File', menu=file_menu)


edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Copy', command=lambda: print("Copy file"))
edit_menu.add_command(label='Cut', command=lambda: print("Cut file"))
edit_menu.add_command(label='Paste', command=lambda: print("Paste file"))
menu_bar.add_cascade(label='Edit', menu=edit_menu)



def show_file_menu(event):
    file_menu.post(event.x_root, event.y_root)
    
root.bind('<Button-3>', show_file_menu)  # Right-click to show file menu

root.mainloop()