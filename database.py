import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection=None
        self.cursor=None
    def connect(self):
        try:
            self.connection=mysql.connector.connect(
                host='localhost',
                database='proiectcriminalistica',
                user='root',
                password='root123'
            )
            self.cursor=self.connection.cursor()
            print("Conectat la baza de date cu succes!♥")
            return True
        except Error as e:
            print(f"Eroare la conectare: {e}")
            return False
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexiune inchisa")
    def get_user_by_username(self, username):
        try:
            query="SELECT ID, Nume, ParolaHash, Rol FROM Utilizator WHERE Nume=%s"
            self.cursor.execute(query, (username,))
            return self.cursor.fetchone()
        except Error as e:
            print(f"Eroare la cautare utilizator: {e}")
            return None
    def search_person_by_cnp(self, cnp):
        try:
            query = "SELECT ID, Nume, Prenume, CNP, Adresa, Sex, Ocupatie FROM Persoana WHERE CNP=%s"
            self.cursor.execute(query, (cnp,))
            return self.cursor.fetchall()
        except Error as e:
            print(f"Eroare la cautare CNP: {e}")
            return []
    def search_person_by_fingerprint(self, template_hash):
        try:
            query= "SELECT p.ID, p.Nume, p.Prenume, p.CNP, p.Adresa, p.Sex, p.Ocupatie, a.Tip_Deget, a.Scor_Calitate FROM Persoana p JOIN Amprenta a ON p.ID=a.IdPersoana WHERE a.Template_Hash=%s"
            self.cursor.execute(query, (template_hash,))
            return self.cursor.fetchall()
        except Error as e:
            print(f"Eroare la cautare amprenta: {e}")
            return []
    def search_person_by_dna(self, dna_profile):
        try:
            query="SELECT p.ID, p.Nume, p.Prenume, p.CNP, p.Adresa, p.Sex, p.Ocupatie, a.D3S1358_a1, a.D3S1358_a2, a.sursa_proba FROM Persoana p JOIN ProfilADN a ON p.ID = a.IdPersoana WHERE a.D3S1358_a1 = %s AND a.D3S1358_a2=%s"
            self.cursor.execute(query, (dna_profile[0], dna_profile[1]))
            return self.cursor.fetchall()
        except Error as e:
            print(f"Eroare la cautare ADN: {e}")
            return []
    def get_all_persons(self):
        try:
            query="SELECT ID, Nume, Prenume, CNP FROM Persoana"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Eroare: {e}")
            return []
        
               
                 
            