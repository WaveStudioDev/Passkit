import tkinter as tk
from tkinter import messagebox

class LoginWindow(tk.Frame):
    def __init__(self, master, authenticator, on_login_success):
        super().__init__(master)
        self.master = master
        self.authenticator = authenticator
        self.on_login_success = on_login_success

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self, text="Login", font=("Helvetica", 24))
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

        # Login Button
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        # Register Button
        self.register_button = tk.Button(self, text="Register", command=self.show_register_window)
        self.register_button.pack(pady=5)

    def login(self):
        """Handle user login."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.authenticator.authenticate(username, password):
            messagebox.showinfo("Login Successful", "Welcome to your Password Vault!")
            self.on_login_success()  # Call the function to show the main window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def show_register_window(self):
        """Show the registration window."""
        self.master.show_register_window()

if __name__ == "__main__":
    # This block is for testing the LoginWindow independently.
    root = tk.Tk()
    root.title("Password Manager - Login")
    root.geometry("300x400")

    # Mock authenticator for testing
    class MockAuthenticator:
        def authenticate(self, username, password):
            return username == "test" and password == "password"

    def on_login_success():
        print("Login successful! Proceeding to main window...")

    login_window = LoginWindow(root, MockAuthenticator(), on_login_success)
    login_window.pack(fill=tk.BOTH, expand=True)
    root.mainloop()