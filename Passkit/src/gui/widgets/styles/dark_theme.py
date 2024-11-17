# gui/styles/dark_theme.py

# Define dark theme styles
DARK_THEME = {
    "bg": "#2E2E2E",              # Background color
    "fg": "white",               # Foreground (text) color
    "button_bg": "#444444",       # Button background color
    "button_fg": "white",         # Button text color
    "entry_bg": "#333333",        # Entry background color
    "entry_fg": "white",          # Entry text color
    "border_color": "#444444",    # Border color for widgets
}

# Optional: Define font styles for the dark theme
FONT_STYLE = {
    "title": ("Helvetica", 24),
    "default": ("Helvetica", 12),
}
import tkinter as tk
def apply_dark_theme(master):
    """Apply the dark theme to the master window and its children."""
    master.config(bg=DARK_THEME["bg"])
    for widget in master.winfo_children():
        widget.config(bg=DARK_THEME["bg"], fg=DARK_THEME["fg"], highlightbackground=DARK_THEME["border_color"])
        # Apply specific styles for buttons and entries
        if isinstance(widget, tk.Button):
            widget.config(bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"])
        elif isinstance(widget, tk.Entry):
            widget.config(bg=DARK_THEME["entry_bg"], fg=DARK_THEME["entry_fg"])