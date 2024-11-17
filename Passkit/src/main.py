import tkinter as tk
from tkinter import messagebox
from gui.main_window import MainWindow
from gui.login_window import LoginWindow
from gui.register_window import RegisterWindow
from gui.vault_window import VaultWindow
from gui.settings_window import SettingsWindow
from database.db_manager import DatabaseManager
from security.authenticator import Authenticator

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # Provide the path to your database file
        db_file = "path_to_your_database.db"  # Update this path to your actual database file
        self.db_manager = DatabaseManager(db_file)  # Pass the db_file argument
        self.authenticator = Authenticator(self.db_manager)  # Pass the db_manager to Authenticator

        # Load the login window
        self.show_login_window()

    def show_login_window(self):
        self.login_window = LoginWindow(self.root, self.authenticator, self.show_main_window)
        self.login_window.pack(fill=tk.BOTH, expand=True)

    def show_register_window(self):
        self.register_window = RegisterWindow(self.root, self.authenticator, self.show_login_window)
        self.register_window.pack(fill=tk.BOTH, expand=True)

    def show_main_window(self):
        self.login_window.pack_forget()  # Hide the login window
        self.main_window = MainWindow(self.root, self.db_manager)
        self.main_window.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()