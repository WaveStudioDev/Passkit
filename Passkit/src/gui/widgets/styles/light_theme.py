# gui/styles/light_theme.py

# Define light theme styles
LIGHT_THEME = {
    "bg": "white",               # Background color
    "fg": "black",               # Foreground (text) color
    "button_bg": "lightgrey",    # Button background color
    "button_fg": "black",        # Button text color
    "entry_bg": "white",         # Entry background color
    "entry_fg": "black",         # Entry text color
    "border_color": "grey",      # Border color for widgets
}

# Optional: Define font styles for the light theme
FONT_STYLE = {
    "title": ("Helvetica", 24),
    "default": ("Helvetica", 12),
}

import tkinter as tk

def apply_light_theme(master):
    """Apply the light theme to the master window and its children."""
    master.config(bg=LIGHT_THEME["bg"])
    for widget in master.winfo_children():
        widget.config(bg=LIGHT_THEME["bg"], fg=LIGHT_THEME["fg"], highlightbackground=LIGHT_THEME["border_color"])
        # Apply specific styles for buttons and entries
        if isinstance(widget, tk.Button):
            widget.config(bg=LIGHT_THEME["button_bg"], fg=LIGHT_THEME["button_fg"])
        elif isinstance(widget, tk.Entry):
            widget.config(bg=LIGHT_THEME["entry_bg"], fg=LIGHT_THEME["entry_fg"])