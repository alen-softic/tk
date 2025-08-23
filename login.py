import tkinter as tk
from tkinter import messagebox
import pandas as pd 
import os 


class LoginApp:
    def __init__(self, root, file_name):
        self.root = root
        self.root.title('Login')
        self.root.geometry('300x250')

        self.file_name = file_name

        if not os.path.exists(self.file_name):
            df = pd.DataFrame(columns= ['username', 'password'])
            df.to_csv(self.file_name, index=False)

        self.create_widgets()
    
    def create_widgets(self):

        tk.Label(self.root, text='username:').grid(padx=3, row=0, column=0, pady = 10)
        self.user_entry = tk.Entry(self.root)
        self.user_entry.grid(padx=3, row = 0, column=1, pady=10)

        tk.Label(self.root, text='password:').grid(padx=3, row=1, column=0, pady = 10)
        self.pass_entry = tk.Entry(self.root, show='*')
        self.pass_entry.grid(padx=3, row = 1, column=1, pady=10)

        tk.Button(self.root, text = "Login", command=self.login).grid(pady=10, row = 2, columnspan=2)
        tk.Button(self.root, text = "Register", command=self.register).grid(pady=5, row = 3, columnspan=2)

    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()

        if not username or not password:
            messagebox.showwarning("Warning", "Please enter username and password.")
            return
        
        # check if in base

        df = pd.read_csv(self.file_name, index_col=None, dtype=str)
        df.info()

        if ((df['username']==username) & (df['password']==password)).any():
            messagebox.showinfo('Success', f'Welcome, {username}!')
        else:
            messagebox.showerror('Error', 'Invalid username or password.')


    def register(self):
        username = str(self.user_entry.get())
        password = str(self.pass_entry.get())

        if not username or not password:
            messagebox.showwarning("Warning", "Please enter username and password.")
            return

        df = pd.read_csv(self.file_name, index_col=None, dtype=str)

        if username in df['username'].values:
            messagebox.showerror('Error', 'Username already exists.')
            return
        
        new_user_df = pd.DataFrame([[str(username), str(password)]], columns=['username', 'password'])
        pd.concat([df, new_user_df], ignore_index=True).to_csv(self.file_name, index=False)

        messagebox.showinfo('Success', f'User {username} succesfully registerd!')


if __name__ == "__main__":
    root = tk.Tk() 
    calc = LoginApp(root, 'app_14_users.csv') 
    root.mainloop()
