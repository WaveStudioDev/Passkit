import tkinter as tk
from tkinter import messagebox

class RegisterWindow(tk.Toplevel):
    def __init__(self, master, user_manager):
        super().__init__(master)
        self.master = master
        self.user_manager = user_manager

        self.title("Register")
        self.geometry("300x300")

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self, text="Create Account", font=("Helvetica", 24))
        self.title_label.pack(pady=10)

        # Username Label and Entry
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(pady=(10, 0))
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=(0, 10))

        # Password Label and Entry
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(pady=(10, 0))
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=(0, 20))

        # Register Button
        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack(pady=5)

    def register(self):
        """Handle user registration."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Username and password cannot be empty.")
            return

        if self.user_manager.create_user(username, password):
            messagebox.showinfo("Registration Successful", "Your account has been created successfully!")
            self.destroy()  # Close the registration window
        else:
            messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")

if __name__ == "__main__":
    # This block is for testing the RegisterWindow independently.
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Mock user manager for testing
    class MockUserManager:
        def __init__(self):
            self.users = {}

        def create_user(self, username, password):
            if username in self.users:
                return False
            self.users[username] = password
            return True

    register_window = RegisterWindow(root, MockUserManager())
    register_window.mainloop()