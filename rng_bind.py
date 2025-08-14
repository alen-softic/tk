import tkinter as tk
import random

# random.seed(42)  # Optional: for reproducibility

def generate_random_integer():
    _min = int(ent_min.get() or 0)  # Default to 0 if empty
    _max = int(ent_max.get() or 9)  # Default to 9

    if _min > _max: # Swap if min is greater than max
        (_min, _max) = (_max, _min)

    random_integer = random.randint(_min, _max)
    lab.config(text=random_integer)

root = tk.Tk()
root.title('My GUI Application')
root.geometry('400x300')

root.minsize(475, 150)
root.bind('<Return>', lambda event: generate_random_integer())  # Bind Return key to function

lab = tk.Label(root, text=7, font=('Arial', 20))
lab.grid(row=0,columnspan=2 ,pady=(30,10))

bt = tk.Button(root, text='Generate a random integer!', font=('Arial', 16), 
               command=generate_random_integer)
bt.grid(row=1,columnspan=2 ,pady=20)

# Entry for minimum value
lab_min = tk.Label(root, text='Enter the minimum: ', font=('Arial', 14))
lab_min.grid(row=2, column=0, padx=10, pady=10)

ent_min = tk.Entry(root, font=('Arial', 14))
ent_min.grid(row=2, column=1, padx=10, pady=10)
# Optional: Bind the Return key to generate a random integer
# Default function
# ent_min.bind('<KEY>', fun)

# Entry for maximum value
lab_max = tk.Label(root, text='Enter the maximum: ', font=('Arial', 14))
lab_max.grid(row=3, column=0, padx=10, pady=10)

ent_max = tk.Entry(root, font=('Arial', 14))
ent_max.grid(row=3, column=1, padx=10, pady=10)


root.mainloop()