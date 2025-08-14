import tkinter as tk

def get_entry_text():
    entry_text = ent.get()
    label.config(text=f"You entered: {entry_text}")

def clear_entry_text():
    ent.delete(0, tk.END)

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

root.minsize(200, 150)

ent = tk.Entry(root, font=('Arial', 16), show='*')
ent.pack(pady=20)

# Button to get entry text
btn_get = tk.Button(root, text='Print text', font=('Arial', 16),
                  command=get_entry_text)
btn_get.pack(pady=10)

# Button to clear entry text
btn_clear = tk.Button(root, text='Clear Text', font=('Arial', 16),
                     command=clear_entry_text)
btn_clear.pack(pady=10)

label = tk.Label(root, text='Enter text above and click the buttons!',
                font=('Arial', 14))
label.pack(pady=20)

root.mainloop()