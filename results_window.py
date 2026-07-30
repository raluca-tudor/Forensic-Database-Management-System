import tkinter as tk
from tkinter import ttk, messagebox

class ResultsWindow:
    def __init__(self, parent, title, data, columns):
        self.parent = parent
        
        #cream o fereastra noua
        self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.window.geometry("800x400")
        self.window.grab_set()
        
        #frame principal
        main_frame = tk.Frame(self.window, padx=10, pady=10)
        main_frame.pack(fill='both', expand=True)
        
        #setam si titlul
        tk.Label(main_frame, text=title, font=('Arial', 14, 'bold')).pack(pady=5)
        tk.Label(main_frame, text=f"Numar rezultate: {len(data)}", font=('Arial', 10)).pack()
        
        #frame pentru tabel
        table_frame = tk.Frame(main_frame)
        table_frame.pack(fill='both', expand=True, pady=10)
        
        #facem si scrollbar
        scrollbar = tk.Scrollbar(table_frame)
        scrollbar.pack(side='right', fill='y')
        
        #treeview (tabel)
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
        
        #configuram coloanele
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')
        
        #trebuie sa ajustam latimea pentru CNP
        if 'CNP' in columns:
            self.tree.column('CNP', width=130)
        
        #acum adaugam datele
        for row in data:
            self.tree.insert('', 'end', values=row)
        self.tree.pack(fill='both', expand=True)
        scrollbar.config(command=self.tree.yview)
        
        #buton pentru a afisa si detalii
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Vezi detalii", command=self.view_details, bg='#3498db', fg='white', width=15).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Inchide", command=self.window.destroy, bg='#e74c3c', fg='white', width=15).pack(side='left', padx=5)
        
        #dublu click pentru a afisa detalii
        self.tree.bind('<Double-1>', lambda e: self.view_details())
    def view_details(self):
        selection=self.tree.selection()
        if not selection:
            messagebox.showwarning("Atentie", "Selectati o persoana!")
            return
        #obtinem id-ul persoanei
        values = self.tree.item(selection[0])['values']
        person_id = values[0]
        messagebox.showinfo("Detalii persoana", f"ID: {person_id}\n" f"Nume: {values[1] if len(values) > 1 else 'N/A'}\n" f"Prenume: {values[2] if len(values) > 2 else 'N/A'}\n" f"CNP: {values[3] if len(values) > 3 else 'N/A'}\n\n" "Pentru mai multe detalii, consultati baza de date!")
        