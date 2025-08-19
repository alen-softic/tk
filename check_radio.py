import tkinter as tk

def show_selected_options():
    selected_checks = []
    if check_var1.get():
        selected_checks.append('Option 1')
    if check_var2.get():
        selected_checks.append('Option 2')
    if check_var3.get():
        selected_checks.append('Option 3')

    selected_radio = radio_var.get()

    result = f'Selected Check Options: {", ".join(selected_checks)}\nSelected Radio Option: {selected_radio}'
    
    lab.config(text=result)
    btn.config(state='disabled')

root = tk.Tk()
root.title('My GUI Application')
root.geometry('500x800')
root.minsize(500,800)

tk.Label(root, text='Check and Radio Buttons Example', font=('Arial', 18)).\
    pack(pady=10)

check_frame = tk.LabelFrame(root,
                            text='Check Button Frame',
                            padx=20,
                            pady=20,
                            border=5)
check_frame.pack(padx=10, pady=10, fill=tk.X)

# Create Boolean variables for check buttons
check_var1 = tk.BooleanVar()
check_var2 = tk.BooleanVar()
check_var3 = tk.BooleanVar()

# Create check buttons with variables
chk_button1 = tk.Checkbutton(check_frame,
                             text='Option 1',
                             variable=check_var1)
chk_button2 = tk.Checkbutton(check_frame,
                             text='Option 2',   
                             variable=check_var2)
chk_button3 = tk.Checkbutton(check_frame,
                             text='Option 3',   
                             variable=check_var3)

# Pack the check buttons into the frame
chk_button1.pack(anchor=tk.W, padx=10, pady=5) # anchor=tk.W aligns the button to the left
chk_button2.pack(anchor=tk.W, padx=10, pady=5)
chk_button3.pack(anchor=tk.W, padx=10, pady=5)


radio_frame = tk.LabelFrame(root,  
                            text='Radio Button Frame',
                            padx=20,
                            pady=20,
                            border=5)
radio_frame.pack(padx=10, pady=10, fill=tk.X)

# Create a StringVar for radio buttons
radio_var = tk.StringVar(value='Choice A')  # Default value

# Create radio buttons with the same variable
radio_button1 = tk.Radiobutton(radio_frame,
                                text='Choice A',
                                variable=radio_var,
                                value='Choice A')
radio_button2 = tk.Radiobutton(radio_frame,
                                text='Choice B',    
                                variable=radio_var,
                                value='Choice B')
radio_button3 = tk.Radiobutton(radio_frame,
                                text='Choice C',
                                variable=radio_var,
                                value='Choice C')

# Pack the radio buttons into the frame
radio_button1.pack(anchor=tk.W, padx=10, pady=5)  # anchor=tk.W aligns the button to the left
radio_button2.pack(anchor=tk.W, padx=10, pady=5)
radio_button3.pack(anchor=tk.W, padx=10, pady=5)

# Create a button to show selected options
btn = tk.Button(root,
          text='Show Selected Options',
          command=show_selected_options)
btn.pack(pady=20)

lab = tk.Label(root, text='Select options.')
lab.pack(pady=10)


root.mainloop()