import tkinter as tk
from tkinter import messagebox, simpledialog
from gui.widgets.password_list import PasswordList
from gui.widgets.password_entry import PasswordEntry

class VaultWindow(tk.Toplevel):
    def __init__(self, master, db_manager):
        super().__init__(master)
        self.master = master
        self.db_manager = db_manager

        self.title("Password Vault")
        self.geometry("400x600")

        self.create_widgets()
        self.load_passwords()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self, text="Your Password Vault", font=("Helvetica", 24))
        self.title_label.pack(pady=10)

        # Password List
        self.password_list = PasswordList(self)
        self.password_list.pack(fill=tk.BOTH, expand=True)

        # Buttons Frame
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(pady=10)

        # Add Password Button
        self.add_button = tk.Button(self.buttons_frame, text="Add Password", command=self.add_password)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Edit Password Button
        self.edit_button = tk.Button(self.buttons_frame, text="Edit Password", command=self.edit_password)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        # Delete Password Button
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Password", command=self.delete_password)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Logout Button
        self.logout_button = tk.Button(self.buttons_frame, text="Logout", command=self.logout)
        self.logout_button.pack(side=tk.LEFT, padx=5)

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

    def edit_password(self):
        """Edit the selected password entry."""
        selected_item = self.password_list.get_selected_item()
        if selected_item:
            entry = PasswordEntry(self, selected_item)
            if entry.show():
                self.db_manager.update_password(selected_item['id'], entry.site, entry.username, entry.password)
                self.load_passwords()
            else:
                messagebox.showinfo("Cancelled", "Password edit cancelled.")
        else:
            messagebox.showwarning("Selection Error", "Please select a password to edit.")

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

    def logout(self):
        """Logout and return to the login window."""
        self.master.deiconify()  # Show the login window again
        self.destroy()  # Close the vault window

if __name__ == "__main__":
    # This block is for testing the VaultWindow independently.
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Mock database manager for testing
    class MockDatabaseManager:
        def __init__(self):
            self.passwords = []

        def get_all_passwords(self):
            return self.passwords

        def add_password(self, site, username, password):
            self.passwords.append({'id': len(self.passwords) + 1, 'site': site, 'username': username, 'password': password})

        def update_password(self, password_id, site, username, password):
            for entry in self.passwords:
                if entry['id'] == password_id:
                    entry.update({'site': site, 'username': username, 'password': password})

        def delete_password(self, password_id):
            self.passwords = [entry for entry in self.passwords if entry['id'] != password_id]

    vault_window = VaultWindow(root, MockDatabaseManager())
    vault_window.mainloop()