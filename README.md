# Forensic-Database-Management-System
A Python-based forensic information system with a graphical user interface (Tkinter) designed to manage and search criminalistic databases. It supports user authentication, person registration and multi-criteria searches using CNP (Personal Numeric Code), fingerprint hashes and DNA profiles (D3S1358 marker) with MySQL integration.


# Project Overview
This project is a **Python-based Forensic Information System** developed with a graphical user interface (GUI) using Tkinter. It is designed to assist forensic experts and criminal investigators in managing, storing and retrieving critical data related to individuals involved in criminal investigations.
The system integrates a secure login module and connects to a MySQL database, populated with random data in a previous project (Parallel DNA Identification System), allowing users to perform advanced searches based on unique biometric and genetic identifiers such as **CNP (Personal Numeric Code)**, **fingerprint hashes**, and **DNA profiles (D3S1358 marker)**. This tool streamlines the identification process and enhances the efficiency of forensic data management.


# Objectives
- Build a secure and user-friendly forensic database interface.
- Implement role-based authentication (Admin vs. Regular User).
- Enable fast and accurate searches using multiple forensic identifiers.
- Facilitate the management of personal, fingerprint and DNA data.
- Provide a clear and structured view of investigation results.
- Simulate a real-world criminalistics database workflow.


# Technologies
- **Python 3** – Core programming language.
- **Tkinter** – GUI library for building the desktop application.
- **MySQL Connector** – For database connectivity and query execution.
- **MySQL** – Relational database management system for storing forensic records.
- **bcrypt** – For secure password hashing (implemented but simulated in login logic).
- **Object-Oriented Programming (OOP)** – For modular and maintainable code structure.


# Features
- **Secure User Authentication:** Login system with username and password verification.
- **Role-Based Access Control:** Different functionalities available for "Admin" and standard users.
- **Multi-Criteria Search Engine:**
  - **CNP Search:** Find individuals by their unique 13-digit Personal Numeric Code.
  - **Fingerprint Search:** Locate individuals using fingerprint template hashes or by selecting the specific finger type.
  - **DNA Search:** Query the database using specific allele values for the D3S1358 genetic marker.
- **Data Visualization:** Display search results in a structured, scrollable table format (Treeview).
- **Detailed Person View:** View comprehensive details for selected individuals (ID, Name, CNP, Address, Gender, Occupation, Fingerprint type, DNA source).
- **View All Records:** Admin users can export or view the complete list of persons in the database.
- **Professional UI:** Clean, organized interface with menu bars, tabbed search panels and status bars.


# Database Schema Overview
The system is built around a relational database ('proiectcriminalistica') with the following core tables:
- **Utilizator** - Stores user credentials ('ID', 'Nume', 'ParolaHash', 'Rol')/
- **Persoana** - Stores personal information ('ID', 'Nume', 'Prenume', 'CNP', 'Adresa', 'Sex', 'Ocupatie').
- **ProfilADN** - Links individuals to their DNA profiles ('IdPersoana', 'D3S1358_a1', 'D3S1358_a2', 'vWA_a1', 'vWA_a2', 'FGA_a1', 'FGA_a2', 'D8S1179_a1', 'D8S1179_a2', 'sursa_proba', 'data_prelevarii').
- **Amprenta** - Links individuals to their fingerprint data ('IdPersoana', 'Tip_Deget', 'Template_Hash', 'Scor_Calitate', 'DataPrelevare').


# Project Structure
Forensic Database Management System:
  - criminalistica.sql # The database used
  - database_images/:
    - Utilizatori.DB.png
    - Persoane.DB.png
    - ProfilADN.DB.png
    - Amprente.DB.png
  - project_images/:
    - Autentificare.png
    - PanouPrincipal.png
    - CautareDupaCNP.png
    - RezultatePentruCNP.png
    - CautareDupaAmprenta.png
    - RezultatePentruAmprenta.png
    - CautareDupaADN.png
    - RezultatePentruADN.png
    - ToatePersoanele.png
    - Deconectare.png
  - database.py # MySQL database connection and query methods
  - login_window.py # Login interface and authentication logic
  - main_window.py # Main dashboard with menus and navigation
  - search_window.py # Advanced search interface (CNP, Fingerprint, DNA)
  - results_window.py # Displays search results in a table format
  - main.py # Entry point of the application
  - README.md



# How to Run
1. **Install Python 3** on your computer/laptop.
2. **Install MySQL Server** and create the database ('proiectcriminalistica') with the required tables.
3. **Install the required Python libraries**:
   bash
   pip install mysql-connector-python bcrypt
4. Update the database credentials in 'database.py' (host, user, password) to match your local MySQL setup.
5. Run the application:
   bash
   python main.py
6. Use the login credentials (example: username: Popa Marius, password: criminaLISTica2513 - or set up your own in the database) to access the system.


# Concepts Used
- Object-Oriented Programming (OOP) – Classes and objects for UI components and database handling.
- Database Management Systems (DBMS) – Designing and querying relational databases using SQL.
- GUI Development – Creating interactive desktop applications using Tkinter.
- Event-Driven Programming – Handling user interactions (button clicks, keyboard events, double-clicks).
- Software Architecture – Separating logic into layers (Database layer, UI layer, Business logic).
- Forensic Science Concepts – Understanding biometric identifiers (DNA, fingerprints) and their role in criminal investigations.


# Academic Context
Developed as a personal project for studying database systems, GUI programming, and applied computer science in the field of criminalistics and forensic data management.


# Author
Raluca-Ana-Maria Tudor

University of Craiova

2026



