import tkinter as tk
# wrapper around Tk - GUItoolkit

root = tk.Tk()
# This creates a new Tkinter window, which is the main window of the app.

root.title("My GUI Application")
# This sets the title of the main window.

root.geometry("400x300")
# This sets the size of the main window to 400 pixels wide and 300 pixels tall

root.minsize(200, 150)
# This sets the minimum size of the main window to 200 pixels wide and 150 pixels

root.maxsize(800, 600)
# This sets the maximum size of the main window to 800 pixels wide and 600 pixelstall

root.iconphoto(True, tk.PhotoImage(file='icon.png'))
# This sets the icon of the main window to an image file named 'icon.png'.

root.config(bg='lightblue')
# This sets the icon of the main window to an image file named 'icon.png' and


# Widgets
# You can add widgets like buttons, labels, etc. to the main window here.

# Label - displays or images on the window
label1 = tk.Label(root, text="Hello, Tkinter 1!", font=("Arial", 16, 'bold'),
                bg='darkblue', fg='white')
label1.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

label2 = tk.Label(root, text="Hello, Tkinter 2!", font=("Arial", 16, 'bold'),
                bg='darkblue', fg='white')
label2.grid(row=1, column=0, padx=10, pady=10, columnspan=1)

label3 = tk.Label(root, text="Hello, Tkinter 3!", font=("Arial", 16, 'bold'),
                bg='darkblue', fg='white')
label3.grid(row=1, column=1, padx=10, pady=10, columnspan=1)

# Button - clickable button






root.mainloop()
# This starts the Tkinter event loop, 
# which waits for events such as button clicks or key presses.
