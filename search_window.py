import tkinter as tk
from tkinter import ttk, messagebox
from results_window import ResultsWindow

class SearchWindow:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        #cream o fereastra noua
        self.window=tk.Toplevel(parent)
        self.window.geometry("1000x800")
        self.window.resizable(False, False)
        self.window.grab_set() #face fereastra sa fie mobila
        
        #frame principal
        main_frame=tk.Frame(self.window, padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        #titlu
        tk.Label(main_frame, text="Cautare persoane", font=('Arial', 16, 'bold')).pack(pady=10)
        
        #facem si un notebook pentru tipuri de cautare
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill='both', expand=True, pady=10)
        
        # tab 1: cautare dupa cnp
        tab_cnp = tk.Frame(notebook)
        notebook.add(tab_cnp, text="CNP")
        self.create_cnp_search(tab_cnp)
        
        #tab 2: cautare dupa amprenta
        tab_amprenta = tk.Frame(notebook)
        notebook.add(tab_amprenta, text="Amprenta")
        self.create_amprenta_search(tab_amprenta)
        
        #tab 3: cautare dupa adn
        tab_adn = tk.Frame(notebook)
        notebook.add(tab_adn, text="ADN")
        self.create_adn_search(tab_adn)
        
        #buton de inchidere
        tk.Button(main_frame, text="Inchide", command=self.window.destroy, bg='#e74c3c', fg='white', font=('Arial', 10), width=15).pack(pady=10)
    def create_cnp_search(self, parent):
        #cream interfata pentru cautare dupa cnp
        frame=tk.Frame(parent, padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        tk.Label(frame, text="CNP: ", font=("Arial", 12)).pack(anchor='w')
        cnp_entry=tk.Entry(frame, font=('Arial', 12), width=20)
        cnp_entry.pack(pady=5, anchor='w')
        def search_cnp():
            cnp = cnp_entry.get().strip()
            if not cnp:
                messagebox.showwarning("Atentie", "Introduceti un CNP!")
                return
            if len(cnp) != 13:
                messagebox.showwarning("Atentie", "CNP-ul trebuie sa aiba 13 caractere!")
                return
            results=self.db.search_person_by_cnp(cnp)
            if results:
                ResultsWindow(self.window, f"Rezultate pentru CNP: {cnp}", results, ["ID", "Nume", "Prenume", "CNP", "Adresa", "Sex", "Ocupatie"])
            else:
                messagebox.showinfo("Rezultate", "Nu s-a gasit nicio persoana cu acest CNP.")
        tk.Button(frame, text="Cauta", command=search_cnp, bg='#3498db', fg='white', font=('Arial', 11), width=15, height=1).pack(pady=10)
    def create_amprenta_search(self, parent):
        frame = tk.Frame(parent, padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        tk.Label(frame, text="Hash amprenta: ", font=('Arial', 12)).pack(anchor='w')
        hash_entry = tk.Entry(frame, font=('Arial', 12), width=100)
        hash_entry.pack(pady=5, anchor='w')
        tk.Label(frame, text="Sau selectati degetul: ", font=('Arial', 12)).pack(anchor='w', pady=(10,0))
        degete_frame = tk.Frame(frame)
        degete_frame.pack(pady=5, anchor='w')
        degete=["Police stanga", "Police dreapta",
                "Aratator stanga", "Aratator dreapta",
                "Mijlociu stanga", "Mijlociu dreapta",
                "Inelar stanga", "Inelar dreapta",
                "Deget mic stanga", "Deget mic dreapta"]
        deget_var = tk.StringVar()
        deget_var.set("")
        deget_dropdown = ttk.Combobox(degete_frame, textvariable=deget_var, values=degete, width=20)
        deget_dropdown.pack(side='left')

        def search_amprenta():
            hash_val = hash_entry.get().strip()

            if not hash_val:
                messagebox.showwarning("Atentie", "Introduceti hash-ul amprentei!")
                return

            print(f"Caut hash-ul: '{hash_val}' (lungime: {len(hash_val)})")

            results = self.db.search_person_by_fingerprint(hash_val)
            print(f"Rezultate gasite: {len(results)}")

            if results:
                ResultsWindow(self.window, "Rezultate amprenta",
                            results, ["ID", "Nume", "Prenume", "CNP", "Adresa", "Sex", "Ocupatie",
                                    "Tip_Deget", "Scor_Calitate"])
            else:
                messagebox.showinfo("Rezultate", "Nu s-a gasit nicio persoana cu aceasta amprenta.")

        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="Cauta după amprenta",
                command=search_amprenta,
                bg='#3498db', fg='white', font=('Arial', 11, 'bold'),
                width=25, height=1).pack(pady=5)
        
        
    def create_adn_search(self, parent):
        frame=tk.Frame(parent, padx=20, pady=20)
        frame.pack(fill='both', expand=True)
        tk.Label(frame, text="Cautare dupa profilul ADN", font=('Arial', 12, 'bold')).pack(pady=(0,10))
        tk.Label(frame, text="Introduceti markerul D3S1358: ", font=('Arial', 11)).pack(anchor='w')
        
        #facem un frame pentru genele alele
        alele_frame = tk.Frame(frame)
        alele_frame.pack(pady=5)
        tk.Label(alele_frame, text="Alela 1: ").pack(side='left', padx=5)
        alela1_entry = tk.Entry(alele_frame, width=10)
        alela1_entry.pack(side='left', padx=5)
        tk.Label(alele_frame, text="Alela 2: ").pack(side='left', padx=5)
        alela2_entry = tk.Entry(alele_frame, width=10)
        alela2_entry.pack(side='left', padx=5)
        
        def search_adn():
            try:
                alela1 = float(alela1_entry.get().strip())
                alela2 = float(alela2_entry.get().strip())
                results = self.db.search_person_by_dna((alela1, alela2))
                if results:
                    ResultsWindow(self.window, f"Rezultate ADN", results, ["ID", "Nume", "Prenume", "CNP", "Adresa", "Sex", "Ocupatie", "D3S1358_a1", "D3S1358_a2", "Sursa proba"])
                else:
                    messagebox.showinfo("Rezultate", "Nu s-a gasit nicio persoana cu acest profil ADN.")
            except ValueError:
                messagebox.showerror("Eroare", "Introduceti valori numerice pentru genele alele!")
        tk.Button(frame, text="Cauta ADN", command=search_adn, bg='#3498db', fg='white', font=('Arial', 11), width=20, height=1).pack(pady=15)
        