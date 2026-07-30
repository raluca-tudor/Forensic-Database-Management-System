import tkinter as tk
from tkinter import messagebox
import bcrypt
from database import Database

class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root=root
        self.on_login_success=on_login_success
        self.db=Database()
        self.db.connect()
        
        self.root.title("Autentificare - Sistem")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        main_frame = tk.Frame(self.root, padx=50, pady=50)
        main_frame.pack(expand=True, fill='both')
        
        tk.Label(main_frame, text="AUTENTIFICARE", font=('Arial', 16, 'bold')).pack(pady=20)
        
        tk.Label(main_frame, text="Nume utilizator:", font=('Arial', 10)).pack(anchor='w')
        self.username_entry = tk.Entry(main_frame, width=30, font=('Arial', 10))
        self.username_entry.pack(pady=5, ipady=3)
        self.username_entry.focus()
        
        tk.Label(main_frame, text="Parola:", font=('Arial', 10)).pack(anchor='w')
        self.password_entry = tk.Entry(main_frame, width=30, show="*", font=('Arial', 10))
        self.password_entry.pack(pady=5, ipady=3)
        
        login_btn = tk.Button(main_frame, text="Autentificare", command=self.login, bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'), width=20, height=2)
        login_btn.pack(pady=20)
        
        exit_btn = tk.Button(main_frame, text="Iesire", command=self.root.quit, bg="#f44336", fg='white', font=('Arial', 10, 'bold'), width=20, height=1)
        exit_btn.pack()
        
        #legare cu tasta Enter
        self.root.bind('<Return>', lambda event: self.login())
    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if not username or not password:
            messagebox.showerror("Eroare", "Introduceti nume utilizator si parola!")
            return
        #cautam utilizatorul in baza noastra de date
        user = self.db.get_user_by_username(username)
        if user:
            # user[0]=ID, user[1]=Nume, user[2]=ParolaHash, user[3]=Rol
            stored_hash = user[2]
            #verificam parola, doar pentru test
            if password == "criminaLISTica2513":
                messagebox.showinfo("Succes", f"Autentificare reusita!\nBun venit, {username}!")
                self.on_login_success(username, user[3], self.db)
            else:
                messagebox.showerror("Eroare", "Parola introdusa este incorecta!")
        else:
            messagebox.showerror("Eroare", "Utilizator inexistent!")
    def __del__(self):
        #inchidem conexiunea la baza de date
        if hasattr(self, 'db'):
            self.db.disconnect()
