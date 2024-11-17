import tkinter as tk
from tkinter import messagebox, simpledialog
from gui.widgets.password_list import PasswordList
from gui.widgets.password_entry import PasswordEntry

class MainWindow(tk.Frame):
    def __init__(self, master, db_manager):
        super().__init__(master)
        self.master = master
        self.db_manager = db_manager

        self.title_label = tk.Label(self, text="Password Vault", font=("Helvetica", 24))
        self.title_label.pack(pady=10)

        # Password List
        self.password_list = PasswordList(self)
        self.password_list.pack(fill=tk.BOTH, expand=True)

        # Add Password Button
        self.add_button = tk.Button(self, text="Add Password", command=self.add_password)
        self.add_button.pack(pady=5)

        # Delete Password Button
        self.delete_button = tk.Button(self, text="Delete Password", command=self.delete_password)
        self.delete_button.pack(pady=5)

        # Load existing passwords
        self.load_passwords()

    def load_passwords(self):
        """Load passwords from the database and display them in the list."""
        passwords = self.db_manager.get_all_passwords()
        self.password_list.populate(passwords)

    def add_password(self):
        """Prompt the user to add a new password."""
        entry = PasswordEntry(self)
        if entry.show():
            self.db_manager.add_password(entry.site, entry.username, entry.password)
            self.load_passwords()
        else:
            messagebox.showinfo("Cancelled", "Password addition cancelled.")

    def initialize_theme_switcher(self):
        # Initialize the Theme Switcher
        from gui.widgets.theme_switcher import ThemeSwitcher
        self.theme_switcher = ThemeSwitcher(self)
    def delete_password(self):
        """Delete the selected password from the list."""
        selected_item = self.password_list.get_selected_item()
        if selected_item:
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this password?")
            if confirm:
                self.db_manager.delete_password(selected_item['id'])
                self.load_passwords()
        else:
            messagebox.showwarning("Selection Error", "Please select a password to delete.")

if __name__ == "__main__":
    # This block is for testing the MainWindow independently.
    root = tk.Tk()
    root.title("Password Manager - Main Window")
    root.geometry("400x600")
    # Assuming db_manager is already defined or imported
    # main_window = MainWindow(root, db_manager)
    # main_window.pack(fill=tk.BOTH, expand=True)
    root.mainloop()