import tkinter as tk

def show_status():
    """Update the label based on the radio button selection."""
    selected = choice.get()
    lab.config(text=f'Selected: {selected}', font=('Arial', 20))
    send_btn.config(state='disabled')

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

choice = tk.StringVar(value='Option 1')  # Default selection
tk.Radiobutton(root, text='Option 1', variable=choice, value='Option 1', font=('Arial', 20)).pack(pady=20)
tk.Radiobutton(root, text='Option 2', variable=choice, value='Option 2', font=('Arial', 20)).pack(pady=20)

lab = tk.Label(root, text='Select one option.', font=('Arial', 20))
lab.pack(pady=20)

send_btn = tk.Button(root, text='Send', command=show_status, font=('Arial', 20))
send_btn.pack(pady=20)

root.mainloop()