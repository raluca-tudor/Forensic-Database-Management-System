import tkinter as tk
from tkinter import messagebox
from search_window import SearchWindow 
from results_window import ResultsWindow

class MainWindow:
    def __init__(self, root, username, role, db):
        self.root=root
        self.username=username
        self.role=role
        self.db=db
        #configuram fereastra principala
        self.root.title("Sistem Criminalistic - Panoul Principal")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        #meniul
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        #meniul fisier
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Fisier", menu=file_menu)
        file_menu.add_command(label="Iesire", command=self.root.quit)
        
        #meniul cautare
        search_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Cautare", menu=search_menu)
        search_menu.add_command(label="Cauta persoana", command=self.open_search)
        
        #meniul ajutor
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajutor", menu=help_menu)
        help_menu.add_command(label="Despre", command=self.show_about)
        
        #frame principal cu scroll
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        #header
        header = tk.Frame(main_frame, bg="#2c3e50", height=80)
        header.pack(fill='x', pady=(0, 20))
        header.pack_propagate(False)
        tk.Label(header, text="Sistem Criminalistic", font=('Arial', 20, 'bold'), fg='white', bg='#2c3e50').pack(expand=True)
        
        #informatii despre utilizator
        info_frame = tk.Frame(main_frame)
        info_frame.pack(fill='x', pady=10)
        tk.Label(info_frame, text=f"Utilizator: {username}", font=('Arial', 12), anchor='w').pack(side='left')
        tk.Label(info_frame, text=f"Rol: {role}", font=('Arial', 12), anchor='e').pack(side='right')
        
        #butoanele principale
        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack(expand=True)
        
        #buton de cautare a unei persoane
        search_btn = tk.Button(buttons_frame, text="Cauta persoana", command=self.open_search, font=('Arial', 14), bg="#3498db", fg='white', width=25, height=2)
        search_btn.grid(row=0, column=0, padx=20, pady=10)
        
        #buton cu care vezi toate persoanele
        view_all_btn = tk.Button(buttons_frame, text="Vezi toate persoanele", command=self.view_all_persons, font=('Arial', 14), bg="#2ecc71", fg='white', width=25, height=2)
        view_all_btn.grid(row=0, column=1, padx=20, pady=10)
        
        #buton rapoarte (doar pt admin)
        if role.lower() == 'Admin':
            reports_btn = tk.Button(buttons_frame, text="Rapoarte", command=self.show_reports, font=('Arial', 14), bg="#e67e22", fg='white', width=25, height=2)
            reports_btn.grid(row=1, column=0, padx=20, pady=10)
        
        #buton de delogare
        logout_btn = tk.Button(buttons_frame, text="Deconectare", command=self.logout, font=('Arial', 14), bg='#e74c3c', fg='white', width=25, height=2)
        logout_btn.grid(row=1 if role.lower()=='Admin' else 1, column=1 if role.lower()=='Admin' else 0, padx=20, pady=10)
        
        #status bar
        status_frame = tk.Frame(self.root, bg='#ecf0f1', height=30)
        status_frame.pack(side='bottom', fill='x')
    def open_search(self):
        SearchWindow(self.root, self.db)
    def view_all_persons(self):
        from results_window import ResultsWindow
        persons = self.db.get_all_persons()
        ResultsWindow(self.root, "Toate persoanele", persons, ["ID", "Nume", "Prenume", "CNP"])
    def show_reports(self):
        messagebox.showinfo("Rapoarte", "Functionalitate in deszzvoltare")
    def show_about(self):
        messagebox.showinfo("Despre",
                            "Sistem Criminalistic v1.0\n\n"
                            "Aplicatie pentru gestionarea bazei de date\n"
                            "criminalistice cu amprente, ADN si date personale.♥")
    def logout(self):
        if messagebox.askyesno("Confirmare", "Sigur doriti sa va deconectati? :("):
            self.db.disconnect()
            self.root.destroy()
            #recream fereastra de login
            import main
            main.create_login_window()    