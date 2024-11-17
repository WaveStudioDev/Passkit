import tkinter as tk

class ThemeSwitcher:
    def __init__(self, master):
        self.master = master
        self.is_dark_mode = False  # Start with light mode

        # Define light and dark theme colors
        self.light_theme = {
            "bg": "white",
            "fg": "black",
            "button_bg": "lightgrey",
            "button_fg": "black",
        }

        self.dark_theme = {
            "bg": "#2E2E2E",
            "fg": "white",
            "button_bg": "#444444",
            "button_fg": "white",
        }

        # Create a button to switch themes
        self.theme_button = tk.Button(
            master,
            text="Switch to Dark Mode",
            command=self.toggle_theme,
            bg=self.light_theme["button_bg"],
            fg=self.light_theme["button_fg"]
        )
        self.theme_button.pack(pady=10)

        # Apply the light theme initially
        self.apply_theme(self.light_theme)

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        self.is_dark_mode = not self.is_dark_mode
        new_theme = self.dark_theme if self.is_dark_mode else self.light_theme
        self.apply_theme(new_theme)

        # Update button text
        self.theme_button.config(
            text="Switch to Light Mode" if self.is_dark_mode else "Switch to Dark Mode",
            bg=new_theme["button_bg"],
            fg=new_theme["button_fg"]
        )

    def apply_theme(self, theme):
        """Apply the selected theme to the master window."""
        self.master.config(bg=theme["bg"])
        for widget in self.master.winfo_children():
            widget.config(bg=theme["bg"], fg=theme["fg"])
