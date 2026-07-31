CREATE DATABASE proiectcriminalistica;

USE proiectcriminalistica;


CREATE TABLE Utilizator(
	ID int Primary Key AUTO_INCREMENT,
	Nume nvarchar(20),
	ParolaHash nvarchar(255),
	Rol nvarchar(30));


CREATE TABLE Persoana(
	ID int Primary Key AUTO_INCREMENT,
	Nume nvarchar(20) NOT NULL,
	Prenume nvarchar(20) NOT NULL,
	CNP char(13) UNIQUE NOT NULL,
	Adresa nvarchar(50) NOT NULL,
	Sex nvarchar(10) NOT NULL,
	Ocupatie nvarchar(30) NOT NULL); 



CREATE TABLE ProfilADN(
	ID int Primary Key AUTO_INCREMENT,
    IdPersoana int,
	FOREIGN KEY (IdPersoana) REFERENCES Persoana(ID),
	D3S1358_a1 decimal(4,1) NOT NULL,
	D3S1358_a2 decimal(4,1) NOT NULL,
	vWA_a1 decimal(4,1) NOT NULL,
	vWA_a2 decimal(4,1) NOT NULL,
	FGA_a1 decimal(4,1) NOT NULL,
	FGA_a2 decimal(4,1) NOT NULL,
	D8S1179_a1 decimal(4,1) NOT NULL,
	D8S1179_a2 decimal(4,1) NOT NULL,
	sursa_proba nvarchar(20) NOT NULL,
	data_prelevarii date NOT NULL);


CREATE TABLE Amprenta(
	ID int Primary Key AUTO_INCREMENT,
    IdPersoana int,
	FOREIGN KEY (IdPersoana) REFERENCES Persoana(ID),
	Tip_Deget nvarchar(20) NOT NULL,
	Template_Hash char(64) NOT NULL,
	Scor_Calitate tinyint CHECK (Scor_Calitate <= 100),
	DataPrelevare date NOT NULL);
    


CREATE TABLE CazPenal(
	ID int Primary Key AUTO_INCREMENT,
	tip_infractiune nvarchar(30) NOT NULL,
	gravitate nvarchar(20) NOT NULL,
	locatie nvarchar(30) NOT NULL,
	data_fapta date NOT NULL,
	status_caz nvarchar(20) NOT NULL);


CREATE TABLE Cazier(
	ID int Primary Key AUTO_INCREMENT,
    IdPersoana int,
    IdCaz int,
	FOREIGN KEY (IdPersoana) REFERENCES Persoana(ID),
	FOREIGN KEY (IdCaz) REFERENCES CazPenal(ID),
	pedeapsa nvarchar(20) NOT NULL,
	data_condamnare date NOT NULL);


CREATE TABLE Proba(
	ID int Primary Key AUTO_INCREMENT,
    IdCaz int,
	FOREIGN KEY (IdCaz) REFERENCES CazPenal(ID),
	tip_proba nvarchar(30) NOT NULL,
	descriere nvarchar(100) NOT NULL,
	data_colectare date NOT NULL);


CREATE TABLE CorelareProba(
	ID int Primary Key AUTO_INCREMENT,
	IdProba int,
    IdADN int,
	FOREIGN KEY (IdProba) REFERENCES Proba(ID),
    FOREIGN KEY (IdADN) REFERENCES ProfilADN(ID),
	Scor_Potrivire tinyint CHECK (Scor_Potrivire <=100),
	Metoda_Potrivire nvarchar(50),
	status_corelare nvarchar(20));


CREATE TABLE BunuriPersoana(
	ID int Primary Key AUTO_INCREMENT,
    IdPersoana int,
	FOREIGN KEY (IdPersoana) REFERENCES Persoana(ID),
	denumire_bun nvarchar(100) NOT NULL,
	valoare decimal(10,2) NOT NULL);


CREATE TABLE ModOperare(
	ID int Primary Key AUTO_INCREMENT,
    IdCaz int,
	FOREIGN KEY (IdCaz) REFERENCES CazPenal(ID),
	metoda_intrare nvarchar(100) NOT NULL,
	instrumente_folosite nvarchar(255) NOT NULL,
	semnatura_specifica nvarchar(100) NOT NULL);
    
INSERT INTO Utilizator ( Nume, ParolaHash, Rol)
VALUES 
("Popa Marius", "rezolva-crima-123", "Admin"),
("Olaru Laura", "vreau-Cafea-Acum", "Ofiter Omucideri"),
("Prunea Alexandru", "oTona-de-energizante", "Sergent Omucideri"),
("Sava Emilia", "parola-cu-Pisici", "Subofiter Criminalistica"),
("Barbu Andrei", "hot-dog-Crokant", "Ofiter Criminalistica"),
("Stanca Valentin", "tort-Cu-lamaie-siAfine", "Agent Criminalistica"),
("Marinescu Paula", "ma-doare-spaTele", "Locotenent");
SELECT * FROM Utilizator;

SELECT * FROM Persoana;

SELECT * FROM Amprenta;

SELECT * FROM ProfilADN;








    
    
	

 
    
    






	




	 
