import tkinter as tk

def show_selection():
    selected = listbox.get(listbox.curselection())
    print("Selected item:", selected)

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

listbox = tk.Listbox(root)
for item in ['Item 1', 'Item 2', 'Item 3', 'Item 4']:
    listbox.insert(tk.END, item)
listbox.pack(pady=20)   


btn = tk.Button(root, text='Show Selection', command=show_selection)
btn.pack(pady=5)
root.mainloop()