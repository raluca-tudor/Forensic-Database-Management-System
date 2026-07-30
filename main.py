import tkinter as tk
from login_window import LoginWindow
from main_window import MainWindow

def create_login_window():
    #cream fereastra de login
    root = tk.Tk()
    
    def on_login_success(username, role, db):
        #ditrugem fereastra de login
        root.destroy()
        #cream fereastra principala
        main_root = tk.Tk()
        MainWindow(main_root, username, role, db)
        main_root.mainloop()
    #initializam fereastra de login
    LoginWindow(root, on_login_success)
    root.mainloop()

if __name__ == "__main__":
    create_login_window()