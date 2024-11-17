import tkinter as tk
from tkinter import messagebox

class SettingsWindow(tk.Toplevel):
    def __init__(self, master, user_manager):
        super().__init__(master)
        self.master = master
        self.user_manager = user_manager

        self.title("Settings")
        self.geometry("300x400")

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self, text="Settings", font=("Helvetica", 24))
        self.title_label.pack(pady=10)

        # Change Master Password
        self.change_password_frame = tk.Frame(self)
        self.change_password_frame.pack(pady=10)

        self.change_password_label = tk.Label(self.change_password_frame, text="Change Master Password:")
        self.change_password_label.pack(pady=(0, 5))
        
        self.new_password_entry = tk.Entry(self.change_password_frame, show="*")
        self.new_password_entry.pack(pady=(0, 5))
        
        self.change_password_button = tk.Button(self.change_password_frame, text="Change Password", command=self.change_master_password)
        self.change_password_button.pack(pady=(5, 0))

        # Enable/Disable Password Visibility
        self.visibility_var = tk.BooleanVar(value=False)  # Default to False (hidden)
        self.visibility_checkbox = tk.Checkbutton(self, text="Show Passwords", variable=self.visibility_var, command=self.toggle_password_visibility)
        self.visibility_checkbox.pack(pady=10)

        # Save Settings Button
        self.save_button = tk.Button(self, text="Save Settings", command=self.save_settings)
        self.save_button.pack(pady=20)

    def change_master_password(self):
        """Change the user's master password."""
        new_password = self.new_password_entry.get()
        if not new_password:
            messagebox.showwarning("Input Error", "New password cannot be empty.")
            return

        if self.user_manager.change_master_password(new_password):
            messagebox.showinfo("Success", "Master password changed successfully!")
            self.new_password_entry.delete(0, tk.END)  # Clear the entry
        else:
            messagebox.showerror("Error", "Failed to change master password.")

    def toggle_password_visibility(self):
        """Toggle password visibility in the vault."""
        if self.visibility_var.get():
            # Logic to show passwords (e.g., change entry field's show='*' to show='')
            messagebox.showinfo("Visibility", "Passwords will now be visible.")
        else:
            # Logic to hide passwords
            messagebox.showinfo("Visibility", "Passwords will now be hidden.")

    def save_settings(self):
        """Save user settings."""
        # Here you could save user preferences to a file or database if needed
        messagebox.showinfo("Settings Saved", "Your settings have been saved.")

if __name__ == "__main__":
    # This block is for testing the SettingsWindow independently.
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Mock user manager for testing
    class MockUserManager:
        def change_master_password(self, new_password):
            # Simulate changing the master password
            return True

    settings_window = SettingsWindow(root, MockUserManager())
    settings_window.mainloop()